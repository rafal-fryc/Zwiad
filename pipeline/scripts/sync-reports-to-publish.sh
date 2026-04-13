#!/usr/bin/env bash
#
# sync-reports-to-publish.sh
#
# Publishes every report under ~/projecty/Zwiad/reports/{privacy,cybersecurity,ai-law}/
# to the zwiad-reports publish repo, classifies each report into a subject
# cluster via `claude -p` (once — assignments are cached in frontmatter),
# and generates a clusters.json manifest with LLM-written subject summaries.
#
# Idempotent:
#   - Reports with a cluster_slug already in frontmatter are NOT re-classified.
#   - Cluster summaries are only regenerated when a cluster's member set changed.
#
# Flags:
#   --force-recluster   re-classify every report (ignores existing cluster_slug)
#
set -euo pipefail

FORCE_RECLUSTER=0
for arg in "$@"; do
  case "$arg" in
    --force-recluster) FORCE_RECLUSTER=1 ;;
    *) echo "Unknown argument: $arg" >&2; exit 2 ;;
  esac
done

ZWIAD_REPO="${ZWIAD_REPO:-$HOME/projecty/Zwiad}"
REPORTS_REPO="${REPORTS_REPO:-$HOME/projecty/zwiad-reports}"

if [ ! -d "$ZWIAD_REPO/reports" ]; then
  echo "Error: $ZWIAD_REPO/reports not found" >&2
  exit 2
fi
if [ ! -d "$REPORTS_REPO/.git" ]; then
  echo "Error: $REPORTS_REPO is not a git checkout" >&2
  exit 2
fi
if ! command -v claude >/dev/null 2>&1; then
  echo "Warning: 'claude' CLI not found — cluster classification will be skipped" >&2
fi

export FORCE_RECLUSTER

python3 - "$ZWIAD_REPO" "$REPORTS_REPO" <<'PY'
import json, re, sys, os, subprocess, datetime, pathlib

zwiad_root = pathlib.Path(sys.argv[1])
reports_root = pathlib.Path(sys.argv[2])
src_reports = zwiad_root / "reports"
dst_memos = reports_root / "memos"
dst_memos.mkdir(exist_ok=True)
clusters_file = reports_root / "clusters.json"
force_recluster = os.environ.get("FORCE_RECLUSTER") == "1"

FM_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
DATE_SUFFIX_RE = re.compile(r"^(.*)-(\d{4}-\d{2}-\d{2})$")
H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
SUMMARY_HEADING_RE = re.compile(
    r"^##\s+(?:Executive\s+)?Summary(?:\s*\[[^\]]*\])?\s*$",
    re.MULTILINE | re.IGNORECASE,
)

def parse_frontmatter(text):
    m = FM_RE.match(text)
    if not m:
        return {}, text, None
    meta = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"').strip("'")
    body = text[m.end():]
    return meta, body, m.group(1)

def extract_title(body):
    m = H1_RE.search(body)
    return m.group(1).strip() if m else None

def extract_summary(body):
    m = SUMMARY_HEADING_RE.search(body)
    start = m.end() if m else 0
    rest = body[start:]
    paragraph_lines = []
    for line in rest.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            if paragraph_lines:
                break
            continue
        if not stripped:
            if paragraph_lines:
                break
            continue
        if stripped.startswith("**Jurisdiction:**") or stripped.startswith("**Category:**"):
            continue
        paragraph_lines.append(stripped)
    return " ".join(paragraph_lines).strip() or None

def normalize_slug(stem):
    m = DATE_SUFFIX_RE.match(stem)
    if not m:
        return None, None
    name, date = m.group(1), m.group(2)
    return f"{date}-{name}", date

def yaml_escape(s):
    return s.replace('"', '\\"')

# US state names + common federal signals for jurisdiction regex fallback
_US_STATES = [
    "Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut",
    "Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa",
    "Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan",
    "Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada",
    "New Hampshire","New Jersey","New Mexico","New York","North Carolina",
    "North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island",
    "South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont",
    "Virginia","Washington","West Virginia","Wisconsin","Wyoming",
    "District of Columbia",
]
_FEDERAL_HINTS = [
    r"\bFederal\b", r"\bFTC\b", r"\bFCC\b", r"\bHHS\b", r"\bOCR\b",
    r"\bDOJ\b", r"\bSEC\b", r"\bNIST\b", r"\bCongress\b", r"\bWhite House\b",
    r"\bFDA\b", r"\bFISA\b", r"\bTAKE IT DOWN\b", r"\bCOPPA\b", r"\bHIPAA\b",
    r"\bGLBA\b", r"\bCIRCIA\b", r"\bEO\b",
]

def infer_jurisdiction(title: str, summary: str = "") -> str:
    """Regex-based jurisdiction fallback for reports whose frontmatter lacks one."""
    if not title:
        return "Unknown"
    text = f"{title} {summary}"
    # State names first — prefer specificity
    for state in _US_STATES:
        if re.search(rf"\b{re.escape(state)}\b", text):
            return state
    # Federal fallback
    for pat in _FEDERAL_HINTS:
        if re.search(pat, text):
            return "Federal"
    return "Unknown"

def call_claude(prompt, timeout_sec=120):
    """Call `claude -p` with the prompt; return stdout text or None on error."""
    try:
        res = subprocess.run(
            ["claude", "-p", "--model", "sonnet", prompt],
            capture_output=True, text=True, timeout=timeout_sec,
        )
        if res.returncode != 0:
            print(f"  claude call failed rc={res.returncode}: {res.stderr[:200]}", file=sys.stderr)
            return None
        return res.stdout.strip()
    except FileNotFoundError:
        return None
    except subprocess.TimeoutExpired:
        print("  claude call timed out", file=sys.stderr)
        return None

def extract_json_from_response(text):
    """Pull the first JSON object out of a claude response (may include prose)."""
    if not text:
        return None
    # Try direct parse
    try:
        return json.loads(text)
    except Exception:
        pass
    # Find first {...} block
    m = re.search(r"\{[^{}]*\}", text, re.DOTALL)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except Exception:
        return None

def classify_report(title, summary, topic, existing_clusters):
    cluster_list = "\n".join(
        f'- {{"name": "{c["name"]}", "slug": "{c["slug"]}"}}' for c in existing_clusters
    ) or "(none yet)"
    prompt = f"""You are clustering regulatory research reports into subject areas (e.g. specific statutes, agency programs, or enforcement threads).

EXISTING CLUSTERS:
{cluster_list}

REPORT TO CLASSIFY:
Title: {title}
Summary: {summary}
Topic: {topic}

Assign this report to one of the existing clusters if it clearly belongs to the same subject, OR propose a new cluster with a short, stable name — proper noun form (statute, rule, agency program, or enforcement thread). Do not create a cluster that is merely a topic label like "Privacy" or "AI Law".

Output JSON ONLY (no prose):
{{"cluster_slug": "kebab-case-slug", "cluster_name": "Human Readable Name"}}"""
    resp = call_claude(prompt)
    obj = extract_json_from_response(resp)
    if not obj or "cluster_slug" not in obj or "cluster_name" not in obj:
        return None, None
    slug = re.sub(r"[^a-z0-9-]", "", obj["cluster_slug"].lower().replace(" ", "-"))
    name = obj["cluster_name"].strip()
    if not slug or not name:
        return None, None
    return slug, name

def summarize_cluster(name, reports):
    bullets = "\n".join(f"- {r['title']}: {r['summary']}" for r in reports)
    prompt = f"""Write a 2–3 sentence summary of the subject area covered by the cluster "{name}", given these reports inside it:

{bullets}

Cover: what the subject is, why it matters for compliance professionals, and what kind of developments this cluster tracks. Do NOT recap specific reports individually.

Output JSON ONLY (no prose):
{{"summary": "..."}}"""
    resp = call_claude(prompt)
    obj = extract_json_from_response(resp)
    if not obj or "summary" not in obj:
        return None
    return obj["summary"].strip()

def upsert_frontmatter_field(text, key, value):
    """Insert or update a YAML frontmatter key in a markdown file's frontmatter block."""
    line = f'{key}: "{yaml_escape(value)}"'
    m = FM_RE.match(text)
    if not m:
        # No frontmatter — prepend one
        return f"---\n{line}\n---\n\n{text}"
    fm_block = m.group(1)
    lines = fm_block.splitlines()
    replaced = False
    out_lines = []
    for ln in lines:
        if ":" in ln:
            k = ln.split(":", 1)[0].strip()
            if k == key:
                out_lines.append(line)
                replaced = True
                continue
        out_lines.append(ln)
    if not replaced:
        out_lines.append(line)
    new_fm = "\n".join(out_lines)
    return f"---\n{new_fm}\n---\n" + text[m.end():]

# ---------- Step 1: enumerate sources ----------
sources = []
for topic_dir in sorted(src_reports.iterdir()):
    if not topic_dir.is_dir():
        continue
    for f in sorted(topic_dir.rglob("*.md")):
        if f.name == "CLAUDE.md":
            continue
        sources.append(f)

# ---------- Step 2: load existing clusters ----------
existing_clusters = []
if clusters_file.exists():
    try:
        existing_clusters = json.loads(clusters_file.read_text())
    except Exception:
        existing_clusters = []
clusters_by_slug = {c["slug"]: c for c in existing_clusters}

# ---------- Step 3: classify each source report ----------
source_meta = []  # list of dicts with all extracted data for each source
for src in sources:
    text = src.read_text()
    meta, body, _ = parse_frontmatter(text)

    slug, date_from_filename = normalize_slug(src.stem)
    if slug is None:
        print(f"  SKIP (bad filename): {src.name}", file=sys.stderr)
        continue
    title = extract_title(body)
    if not title:
        print(f"  SKIP (no # heading): {src.name}", file=sys.stderr)
        continue
    date = meta.get("date") or date_from_filename
    # Topic is the first path segment under src_reports (privacy / cybersecurity / ai-law),
    # not the immediate parent dir — reports can live in nested subdirs like
    # reports/privacy/state-comprehensive-laws/foo.md.
    top_topic = src.relative_to(src_reports).parts[0]
    topic = meta.get("category") or top_topic
    jurisdiction = meta.get("jurisdiction") or infer_jurisdiction(title or "", extract_summary(body) or "")
    summary = extract_summary(body) or title

    cluster_slug = meta.get("cluster_slug")
    cluster_name = meta.get("cluster")

    needs_classify = force_recluster or not cluster_slug
    if needs_classify:
        print(f"  classifying: {title[:60]}…")
        slug_c, name_c = classify_report(title, summary, topic, existing_clusters)
        if slug_c and name_c:
            cluster_slug, cluster_name = slug_c, name_c
            # Track in the running list so next call's "existing clusters" sees it
            if slug_c not in clusters_by_slug:
                new_c = {"slug": slug_c, "name": name_c, "topic": topic,
                         "summary": "", "reports": [], "jurisdictions": []}
                existing_clusters.append(new_c)
                clusters_by_slug[slug_c] = new_c
            # Persist back to source file
            new_text = upsert_frontmatter_field(text, "cluster", cluster_name)
            new_text = upsert_frontmatter_field(new_text, "cluster_slug", cluster_slug)
            src.write_text(new_text)
        else:
            print(f"    (classification failed — leaving unassigned)", file=sys.stderr)

    source_meta.append({
        "src_path": src,
        "slug": slug,
        "title": title,
        "date": date,
        "topic": topic,
        "jurisdiction": jurisdiction,
        "summary": summary,
        "cluster_slug": cluster_slug,
        "cluster_name": cluster_name,
        "body": body,
    })

# ---------- Step 4: write normalized published copies ----------
written = []
for s in source_meta:
    fm_lines = [
        f'title: "{yaml_escape(s["title"])}"',
        f'date: {s["date"]}',
        f'topic: {s["topic"]}',
        f'jurisdiction: "{yaml_escape(s["jurisdiction"])}"',
        f'summary: "{yaml_escape(s["summary"])}"',
    ]
    if s["cluster_slug"] and s["cluster_name"]:
        fm_lines.append(f'cluster: "{yaml_escape(s["cluster_name"])}"')
        fm_lines.append(f'cluster_slug: {s["cluster_slug"]}')
    fm = "---\n" + "\n".join(fm_lines) + "\n---\n\n"
    new_text = fm + s["body"].lstrip("\n")
    dst = dst_memos / f"{s['slug']}.md"
    old = dst.read_text() if dst.exists() else None
    dst.write_text(new_text)
    if new_text != old:
        written.append(s["slug"])

# Remove placeholder seed
seed = dst_memos / "2026-04-13-hello-world.md"
if seed.exists():
    seed.unlink()
    written.append("removed:2026-04-13-hello-world")

# ---------- Step 5: rebuild index.json ----------
entries = []
for f in sorted(dst_memos.glob("*.md")):
    text = f.read_text()
    m = FM_RE.match(text)
    if not m:
        raise SystemExit(f"Generated report missing frontmatter: {f}")
    meta = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"').strip("'")
    entries.append({
        "slug": f.stem,
        "file": f"memos/{f.name}",
        "title": meta.get("title", ""),
        "date": meta.get("date", ""),
        "topic": meta.get("topic", ""),
        "jurisdiction": meta.get("jurisdiction", "Unknown"),
        "summary": meta.get("summary", ""),
        "cluster": meta.get("cluster", ""),
        "cluster_slug": meta.get("cluster_slug", ""),
    })
entries.sort(key=lambda e: e["date"], reverse=True)
index_out = {"generated": datetime.date.today().isoformat(), "memos": entries}
(reports_root / "index.json").write_text(json.dumps(index_out, indent=2) + "\n")

# ---------- Step 6: rebuild clusters.json ----------
# Group by cluster_slug
cluster_members = {}
for e in entries:
    cs = e.get("cluster_slug") or ""
    if not cs:
        continue
    cluster_members.setdefault(cs, []).append(e)

# Build new clusters list; preserve summaries for clusters whose members didn't change
previous_by_slug = {c["slug"]: c for c in existing_clusters}
new_clusters = []
for cs, members in cluster_members.items():
    prev = previous_by_slug.get(cs, {})
    # Topic = most common topic among members
    topics = {}
    for m in members:
        topics[m["topic"]] = topics.get(m["topic"], 0) + 1
    topic = max(topics, key=topics.get)
    # Jurisdictions = unique non-Unknown
    jurs = sorted({m["jurisdiction"] for m in members if m.get("jurisdiction") and m["jurisdiction"] != "Unknown"})
    # Date range
    dates = sorted(m["date"] for m in members if m.get("date"))
    date_range = {"first": dates[0], "latest": dates[-1]} if dates else {"first": "", "latest": ""}
    # Name: use prev, else first member's cluster_name
    name = prev.get("name") or next((m["cluster"] for m in members if m.get("cluster")), cs)
    # Members changed?
    prev_reports = set(prev.get("reports", []))
    curr_reports = {m["slug"] for m in members}
    summary_stale = prev_reports != curr_reports or not prev.get("summary")
    summary = prev.get("summary", "")
    if summary_stale:
        print(f"  summarizing cluster: {name} ({len(members)} reports)")
        s = summarize_cluster(name, members)
        if s:
            summary = s
    new_clusters.append({
        "slug": cs,
        "name": name,
        "topic": topic,
        "summary": summary,
        "reports": sorted(curr_reports, reverse=True),
        "dateRange": date_range,
        "jurisdictions": jurs,
    })

new_clusters.sort(key=lambda c: (-len(c["reports"]), c["name"]))
(reports_root / "clusters.json").write_text(json.dumps(new_clusters, indent=2) + "\n")

# ---------- Step 7: report ----------
print(f"Source reports: {len(sources)}")
print(f"Published:      {len(entries)}")
print(f"Clusters:       {len(new_clusters)}")
print(f"Changed files:  {len(written)}")
for s in written:
    print(f"  + {s}")
PY

cd "$REPORTS_REPO"
if git diff --quiet && git diff --cached --quiet; then
  echo "No changes to publish."
  exit 0
fi

git add memos/ index.json clusters.json
git commit -m "Bulk sync reports + clusters from Zwiad pipeline"
git push
echo "Published changes — Vercel rebuild should begin within seconds."
