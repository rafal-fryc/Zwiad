#!/usr/bin/env python3
"""Scan Zwiad/reports/** and build pipeline/state/clusters.json.

This is the canonical cluster manifest on the Zwiad side. It's consumed by
route-findings.py (to know what clusters already exist) and mirrored into
zwiad-reports/clusters.json at publish time.

Only reports whose frontmatter already has a cluster_slug contribute.
Reports without cluster assignment are left as "unassigned" and a warning
is printed — run /publish-reports or the pipeline to classify them.
"""
from __future__ import annotations

import json
import re
import sys
import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "lib"))
from clustering import parse_frontmatter, build_cluster_manifest, FM_RE  # noqa: E402

DATE_SUFFIX_RE = re.compile(r"^(.*)-(\d{4}-\d{2}-\d{2})$")


def main():
    zwiad_root = Path(__file__).resolve().parents[2]
    src_reports = zwiad_root / "reports"
    state_dir = zwiad_root / "pipeline" / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    out_file = state_dir / "clusters.json"

    previous: list[dict] = []
    if out_file.exists():
        try:
            raw = json.loads(out_file.read_text())
            previous = raw["clusters"] if isinstance(raw, dict) and "clusters" in raw else raw
        except Exception:
            previous = []

    entries: list[dict] = []
    unassigned: list[str] = []
    for f in sorted(src_reports.rglob("*.md")):
        if f.name == "CLAUDE.md":
            continue
        text = f.read_text()
        meta = parse_frontmatter(text)
        stem = f.stem
        m = DATE_SUFFIX_RE.match(stem)
        if not m:
            continue  # skip files without date suffix
        name, date_s = m.group(1), m.group(2)
        slug = f"{date_s}-{name}"
        topic = meta.get("category") or f.relative_to(src_reports).parts[0]
        entries.append({
            "slug": slug,
            "title": meta.get("title", ""),
            "date": meta.get("date") or date_s,
            "topic": topic,
            "jurisdiction": meta.get("jurisdiction") or "Unknown",
            "summary": meta.get("summary") or "",
            "cluster": meta.get("cluster") or "",
            "cluster_slug": meta.get("cluster_slug") or "",
        })
        if not meta.get("cluster_slug"):
            unassigned.append(slug)

    clusters = build_cluster_manifest(
        entries,
        previous_clusters=previous,
        regenerate_changed_summaries=False,  # don't spend tokens here
    )
    manifest = {"generated": datetime.date.today().isoformat(), "clusters": clusters}
    out_file.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"wrote {out_file} — {len(clusters)} clusters, {len(entries)} reports")
    if unassigned:
        print(f"warning: {len(unassigned)} reports have no cluster_slug (run /publish-reports to classify):", file=sys.stderr)
        for s in unassigned[:5]:
            print(f"  - {s}", file=sys.stderr)
        if len(unassigned) > 5:
            print(f"  ... and {len(unassigned) - 5} more", file=sys.stderr)


if __name__ == "__main__":
    main()
