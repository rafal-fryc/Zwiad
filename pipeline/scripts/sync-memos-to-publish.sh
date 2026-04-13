#!/usr/bin/env bash
#
# sync-memos-to-publish.sh
#
# Publishes every memo under ~/projecty/Zwiad/reports/{privacy,cybersecurity,ai-law}/
# to the zwiad-reports publish repo, translating Zwiad's internal frontmatter
# schema ({finding_id, category, ...}) into the site's expected schema
# ({title, date, topic, summary}) and normalizing filenames to the
# YYYY-MM-DD-<slug>.md convention.
#
# Idempotent — rerun anytime to publish new memos or update changed ones.
#
set -euo pipefail

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

python3 - "$ZWIAD_REPO" "$REPORTS_REPO" <<'PY'
import json, re, sys, shutil, datetime, pathlib

zwiad_root = pathlib.Path(sys.argv[1])
reports_root = pathlib.Path(sys.argv[2])
src_reports = zwiad_root / "reports"
dst_memos = reports_root / "memos"
dst_memos.mkdir(exist_ok=True)

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
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"').strip("'")
    body = text[m.end():]
    return meta, body

def extract_title(body):
    m = H1_RE.search(body)
    return m.group(1).strip() if m else None

def extract_summary(body):
    m = SUMMARY_HEADING_RE.search(body)
    start = m.end() if m else 0
    rest = body[start:]
    # Grab the first non-empty paragraph (stop at next ## or blank line after content)
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

# Build source list
sources = []
for topic_dir in sorted(src_reports.iterdir()):
    if not topic_dir.is_dir():
        continue
    for f in sorted(topic_dir.glob("*.md")):
        if f.name == "CLAUDE.md":
            continue
        sources.append(f)

# Render each to destination
written = []
skipped = []
for src in sources:
    text = src.read_text()
    meta, body = parse_frontmatter(text)

    slug, date_from_filename = normalize_slug(src.stem)
    if slug is None:
        skipped.append((src, "filename does not end in -YYYY-MM-DD"))
        continue

    title = extract_title(body)
    if not title:
        skipped.append((src, "missing # heading"))
        continue

    date = meta.get("date") or date_from_filename
    topic = meta.get("category") or src.parent.name
    jurisdiction = meta.get("jurisdiction") or "Unknown"
    summary = extract_summary(body)
    if not summary:
        summary = title  # last-resort fallback

    # Build normalized frontmatter
    fm = (
        "---\n"
        f'title: "{yaml_escape(title)}"\n'
        f"date: {date}\n"
        f"topic: {topic}\n"
        f'jurisdiction: "{yaml_escape(jurisdiction)}"\n'
        f'summary: "{yaml_escape(summary)}"\n'
        "---\n\n"
    )
    new_text = fm + body.lstrip("\n")
    dst = dst_memos / f"{slug}.md"
    old = dst.read_text() if dst.exists() else None
    dst.write_text(new_text)
    if new_text != old:
        written.append(slug)

# Remove the placeholder seed if present
seed = dst_memos / "2026-04-13-hello-world.md"
if seed.exists():
    seed.unlink()
    written.append("removed:2026-04-13-hello-world")

# Regenerate index.json (sorted by date desc)
entries = []
for f in sorted(dst_memos.glob("*.md")):
    text = f.read_text()
    m = FM_RE.match(text)
    if not m:
        raise SystemExit(f"Generated memo missing frontmatter: {f}")
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
    })
entries.sort(key=lambda e: e["date"], reverse=True)
out = {"generated": datetime.date.today().isoformat(), "memos": entries}
(reports_root / "index.json").write_text(json.dumps(out, indent=2) + "\n")

print(f"Source memos: {len(sources)}")
print(f"Changed/new:  {len(written)}")
for s in written:
    print(f"  + {s}")
for src, reason in skipped:
    print(f"  - SKIP {src}: {reason}", file=sys.stderr)
print(f"Index lists {len(entries)} memo(s)")
PY

cd "$REPORTS_REPO"
if git diff --quiet && git diff --cached --quiet; then
  echo "No changes to publish."
  exit 0
fi

git add memos/ index.json
git commit -m "Bulk sync memos from Zwiad pipeline"
git push
echo "Published changes — Vercel rebuild should begin within seconds."
