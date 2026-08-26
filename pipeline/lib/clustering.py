"""Cluster classification + summarization helpers for the Zwiad pipeline.

Used by:
  - pipeline/scripts/sync-reports-to-publish.sh (publish time)
  - pipeline/scripts/classify-findings.py (pre-research routing)
  - pipeline/scripts/route-findings.py (augment decision)

All LLM calls go through the local `claude` CLI (no API keys).
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from typing import Any


def call_claude(prompt: str, timeout_sec: int = 120, model: str = "sonnet") -> str | None:
    """Call `claude -p --output-format json`. Return the session's result text
    (the assistant's answer, without the CLI envelope) or None on error."""
    try:
        res = subprocess.run(
            ["claude", "-p", "--model", model, "--output-format", "json", prompt],
            capture_output=True,
            text=True,
            timeout=timeout_sec,
        )
    except FileNotFoundError:
        return None
    except subprocess.TimeoutExpired:
        print("  claude timed out", file=sys.stderr)
        return None

    # The CLI envelope is authoritative over the exit code (the CLI can exit
    # nonzero after a session that completed cleanly) — parse it first.
    try:
        envelope = json.loads(res.stdout)
    except Exception:
        envelope = None
    if isinstance(envelope, dict):
        if envelope.get("is_error"):
            print(f"  claude error: {str(envelope.get('result'))[:200]}", file=sys.stderr)
            return None
        result = envelope.get("result")
        if isinstance(result, str):
            return result.strip()

    if res.returncode != 0:
        print(f"  claude rc={res.returncode}: {res.stderr[:200]}", file=sys.stderr)
        return None
    return res.stdout.strip()


def extract_json(text: str | None) -> Any | None:
    """Pull the first JSON object out of a claude response (may include prose
    or a code fence). Handles nested objects — the old single-level regex
    returned truncated garbage for any object containing another object."""
    if not text:
        return None
    text = text.strip()
    fence = re.match(r"^```(?:json)?\s*(.*?)\s*```\s*$", text, re.DOTALL)
    if fence:
        text = fence.group(1)
    try:
        return json.loads(text)
    except Exception:
        pass
    # Balanced-brace scan for the first complete top-level object.
    start = text.find("{")
    while start != -1:
        depth = 0
        in_str = False
        esc = False
        for i in range(start, len(text)):
            ch = text[i]
            if in_str:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == '"':
                    in_str = False
            elif ch == '"':
                in_str = True
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[start : i + 1])
                    except Exception:
                        break  # malformed — try the next opening brace
        start = text.find("{", start + 1)
    return None


def classify_report(
    title: str,
    summary: str,
    topic: str,
    existing_clusters: list[dict],
) -> tuple[str, str] | tuple[None, None]:
    """Assign a report to an existing cluster or propose a new one.

    Returns (cluster_slug, cluster_name) or (None, None) on failure.
    """
    cluster_list = (
        "\n".join(
            f'- {{"name": "{c["name"]}", "slug": "{c["slug"]}"}}'
            for c in existing_clusters
        )
        or "(none yet)"
    )
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
    obj = extract_json(resp)
    if not obj or "cluster_slug" not in obj or "cluster_name" not in obj:
        return None, None
    slug = re.sub(r"[^a-z0-9-]", "", obj["cluster_slug"].lower().replace(" ", "-"))
    name = obj["cluster_name"].strip()
    if not slug or not name:
        return None, None
    return slug, name


def summarize_cluster(name: str, reports: list[dict]) -> str | None:
    """Produce a 2-3 sentence subject-area summary for a cluster."""
    bullets = "\n".join(
        f"- {r['title']}: {r['summary']}" for r in reports
    )
    prompt = f"""Write a 2–3 sentence summary of the subject area covered by the cluster "{name}", given these reports inside it:

{bullets}

Cover: what the subject is, why it matters for compliance professionals, and what kind of developments this cluster tracks. Do NOT recap specific reports individually.

Output JSON ONLY (no prose):
{{"summary": "..."}}"""
    resp = call_claude(prompt)
    obj = extract_json(resp)
    if not obj or "summary" not in obj:
        return None
    return obj["summary"].strip()


def route_finding(
    finding_title: str,
    finding_gist: str,
    finding_url: str,
    existing_reports: list[dict],
) -> dict | None:
    """Decide if a finding should become a NEW_REPORT, MERGE into an existing
    report, or APPEND_SOURCE to an existing report. Returns dict with keys:
        route: "NEW_REPORT" | "MERGE" | "APPEND_SOURCE"
        target_report_slug: (present for MERGE/APPEND_SOURCE)
        rationale: short explanation
    """
    if not existing_reports:
        return {"route": "NEW_REPORT", "rationale": "no existing reports in cluster"}

    report_blocks = "\n\n".join(
        f"--- EXISTING REPORT: {r['slug']} ---\n"
        f"Title: {r['title']}\n"
        f"Summary: {r['summary']}\n"
        f"Body (first 2000 chars):\n{(r.get('body') or '')[:2000]}"
        for r in existing_reports
    )
    prompt = f"""You are deciding how a new regulatory research finding should be integrated with existing reports that already cover the same subject cluster.

NEW FINDING:
Title: {finding_title}
URL: {finding_url}
Gist: {finding_gist}

{report_blocks}

Pick one of three routes:
- NEW_REPORT: the finding's substance is genuinely distinct from all existing reports, even though they share a cluster. A new sibling report is warranted.
- MERGE: the finding adds substantive new information (facts, dates, analysis, next steps) that should be integrated into the body of an existing report. Pick the most appropriate existing report.
- APPEND_SOURCE: the finding covers material already adequately covered — it adds nothing substantive beyond another citation. Just append its URL to the Sources of the existing report.

Output JSON ONLY (no prose):
{{"route": "NEW_REPORT|MERGE|APPEND_SOURCE", "target_report_slug": "slug-if-MERGE-or-APPEND", "rationale": "one sentence"}}"""
    resp = call_claude(prompt)
    obj = extract_json(resp)
    if not obj or "route" not in obj:
        return None
    if obj["route"] not in {"NEW_REPORT", "MERGE", "APPEND_SOURCE"}:
        return None
    return obj


# ---- Cluster manifest builder -------------------------------------------

FM_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict:
    m = FM_RE.match(text)
    if not m:
        return {}
    meta: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta


def build_cluster_manifest(
    report_entries: list[dict],
    previous_clusters: list[dict] | None = None,
    regenerate_changed_summaries: bool = True,
) -> list[dict]:
    """Group report entries by cluster_slug and produce a cluster list.

    report_entries: each dict has slug, title, date, topic, jurisdiction,
                    summary, cluster, cluster_slug
    previous_clusters: prior manifest to preserve summaries for unchanged clusters
    """
    previous_by_slug = {c["slug"]: c for c in (previous_clusters or [])}
    grouped: dict[str, list[dict]] = {}
    for e in report_entries:
        cs = e.get("cluster_slug") or ""
        if not cs:
            continue
        grouped.setdefault(cs, []).append(e)

    out: list[dict] = []
    for cs, members in grouped.items():
        prev = previous_by_slug.get(cs, {})
        topics: dict[str, int] = {}
        for m in members:
            topics[m["topic"]] = topics.get(m["topic"], 0) + 1
        topic = max(topics, key=topics.get) if topics else ""
        jurs = sorted(
            {
                m["jurisdiction"]
                for m in members
                if m.get("jurisdiction") and m["jurisdiction"] != "Unknown"
            }
        )
        dates = sorted(m["date"] for m in members if m.get("date"))
        date_range = (
            {"first": dates[0], "latest": dates[-1]}
            if dates
            else {"first": "", "latest": ""}
        )
        name = prev.get("name") or next(
            (m["cluster"] for m in members if m.get("cluster")), cs
        )
        prev_reports = set(prev.get("reports", []))
        curr_reports = {m["slug"] for m in members}
        summary_stale = prev_reports != curr_reports or not prev.get("summary")
        summary = prev.get("summary", "")
        if regenerate_changed_summaries and summary_stale:
            print(f"  summarizing cluster: {name} ({len(members)} reports)")
            s = summarize_cluster(name, members)
            if s:
                summary = s
        out.append(
            {
                "slug": cs,
                "name": name,
                "topic": topic,
                "summary": summary,
                "reports": sorted(curr_reports, reverse=True),
                "dateRange": date_range,
                "jurisdictions": jurs,
            }
        )
    out.sort(key=lambda c: (-len(c["reports"]), c["name"]))
    return out
