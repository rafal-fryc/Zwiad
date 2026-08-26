#!/usr/bin/env python3
"""One-shot: merge each cluster containing 2+ reports into a single canonical
report. Keeps the newest-dated file as the primary target path; deletes the
others after merging their content into it.

LLM (claude -p) is asked to produce the merged body + combined Sources. We
preserve the primary file's frontmatter and update `last_updated` to today.
"""
from __future__ import annotations

import datetime
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "lib"))
from clustering import call_claude, parse_frontmatter, FM_RE  # noqa: E402

ZWIAD = Path(__file__).resolve().parents[2]
STATE = ZWIAD / "pipeline" / "state" / "clusters.json"
DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-")


def find_report_file(slug: str) -> Path | None:
    # Reports are at reports/<topic>/<maybe subdir>/<name>-YYYY-MM-DD.md
    # The slug is YYYY-MM-DD-<name>; convert back to <name>-YYYY-MM-DD.
    m = DATE_RE.match(slug)
    if not m:
        return None
    date = m.group(1)
    name = slug[len(date) + 1:]
    filename = f"{name}-{date}.md"
    for f in (ZWIAD / "reports").rglob(filename):
        return f
    return None


def merge_cluster(cluster: dict) -> bool:
    slugs = cluster["reports"]
    files: list[tuple[str, Path, str]] = []  # (slug, path, text)
    for s in slugs:
        p = find_report_file(s)
        if not p:
            print(f"    !! file not found for slug {s}; skipping cluster", file=sys.stderr)
            return False
        files.append((s, p, p.read_text()))

    # Primary = newest date
    files.sort(key=lambda t: t[0], reverse=True)
    primary_slug, primary_path, primary_text = files[0]
    secondary = files[1:]

    print(f"  cluster '{cluster['name']}' — keeping {primary_slug} as primary")
    for s, p, _ in secondary:
        print(f"    + merging {s} from {p}")

    # Build LLM prompt
    blocks = []
    for s, _, t in files:
        blocks.append(f"\n\n===== REPORT {s} =====\n{t}")
    prompt = f"""You are merging multiple research reports that all cover the same subject into a single canonical report.

{''.join(blocks)}

Produce a single merged markdown document:
- Start with a YAML frontmatter block containing AT LEAST: title, date, jurisdiction, category, cluster, cluster_slug, first_reported, last_updated, status_history. Use the most recent last_updated.
- Keep the most comprehensive coverage. De-duplicate redundant paragraphs.
- Ensure a single '# Title' heading after frontmatter.
- Preserve the Executive Summary, Background, Key Facts, Why This Matters (as applicable) sections.
- Consolidate Sources: one list at the end under '## Sources' containing every unique source URL from all inputs, deduplicated.
- Do NOT include the separator lines '===== REPORT ... ====='.

Output the entire merged markdown document. No prose, no JSON, no code fence — just the raw markdown starting with the YAML frontmatter `---` line."""

    resp = call_claude(prompt, timeout_sec=300, model="sonnet")
    if resp:
        # Tolerate a wrapping code fence despite the no-fence instruction —
        # models occasionally add one, and dropping the merge over it wastes
        # the whole (expensive) call.
        fence = re.match(r"^```[a-zA-Z]*\s*(.*?)\s*```\s*$", resp.strip(), re.DOTALL)
        if fence:
            resp = fence.group(1)
    if not resp or "---" not in resp:
        print(f"    !! merge LLM failed for cluster '{cluster['name']}'", file=sys.stderr)
        return False

    # Strip any leading noise before first ---
    idx = resp.find("---")
    merged = resp[idx:].rstrip() + "\n"

    # Update last_updated to today in the merged frontmatter, just to be sure
    today = datetime.date.today().isoformat()
    fm_m = FM_RE.match(merged)
    if fm_m:
        fm_lines = fm_m.group(1).splitlines()
        replaced = False
        for i, ln in enumerate(fm_lines):
            if ln.strip().startswith("last_updated:"):
                fm_lines[i] = f"last_updated: {today}"
                replaced = True
                break
        if not replaced:
            fm_lines.append(f"last_updated: {today}")
        merged = "---\n" + "\n".join(fm_lines) + "\n---\n" + merged[fm_m.end():]

    # Write to primary file, delete others
    primary_path.write_text(merged)
    for s, p, _ in secondary:
        p.unlink()
        print(f"    - deleted {p}")

    return True


def main():
    if not STATE.exists():
        print("Run build-clusters-state.py first", file=sys.stderr)
        sys.exit(2)
    state = json.loads(STATE.read_text())
    clusters = state.get("clusters", state if isinstance(state, list) else [])
    dups = [c for c in clusters if len(c["reports"]) > 1]

    print(f"{len(dups)} clusters to collapse:")
    for c in dups:
        print(f"  - {c['name']} ({len(c['reports'])} reports)")

    ok = 0
    fail = 0
    for c in dups:
        print(f"\n==> {c['name']}")
        if merge_cluster(c):
            ok += 1
        else:
            fail += 1
    print(f"\nDone: {ok} merged, {fail} failed")


if __name__ == "__main__":
    main()
