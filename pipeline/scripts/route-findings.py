#!/usr/bin/env python3
"""Decide how each approved scanner finding should be integrated.

For each finding:
  1. Classify it into a cluster (existing or new).
  2. If the cluster has existing reports, call route_finding() to pick
     NEW_REPORT / MERGE / APPEND_SOURCE.
  3. Write scanner-routing.json to the run dir.

Usage:
  route-findings.py <run-dir>

Reads:
  <run-dir>/scanner-deduped.json   (findings to research)
  pipeline/state/clusters.json     (existing cluster manifest)
  reports/**/*.md                  (existing report bodies for MERGE decision)

Writes:
  <run-dir>/scanner-routing.json   (list of {finding_id, route, cluster_slug,
                                    cluster_name, target_report_slug?, rationale})
"""
from __future__ import annotations

import json
import sys
import re
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "lib"))
from clustering import (  # noqa: E402
    classify_report,
    route_finding,
    parse_frontmatter,
)


DATE_SUFFIX_RE = re.compile(r"^(.*)-(\d{4}-\d{2}-\d{2})$")


def load_existing_reports(zwiad_root: Path) -> list[dict]:
    """Load every report under Zwiad/reports/** with its body."""
    out = []
    for f in sorted((zwiad_root / "reports").rglob("*.md")):
        if f.name == "CLAUDE.md":
            continue
        stem = f.stem
        m = DATE_SUFFIX_RE.match(stem)
        if not m:
            continue
        name, date_s = m.group(1), m.group(2)
        slug = f"{date_s}-{name}"
        text = f.read_text()
        meta = parse_frontmatter(text)
        body = text[text.find("---", 3) + 3 :] if text.startswith("---") else text
        out.append({
            "slug": slug,
            "path": str(f),
            "title": meta.get("title", ""),
            "summary": meta.get("summary", ""),
            "topic": meta.get("category") or f.relative_to(zwiad_root / "reports").parts[0],
            "cluster": meta.get("cluster", ""),
            "cluster_slug": meta.get("cluster_slug", ""),
            "body": body,
        })
    return out


def main():
    if len(sys.argv) != 2:
        print("Usage: route-findings.py <run-dir>", file=sys.stderr)
        sys.exit(2)

    run_dir = Path(sys.argv[1]).resolve()
    zwiad_root = Path(__file__).resolve().parents[2]
    findings_file = run_dir / "scanner-deduped.json"
    if not findings_file.exists():
        print(f"Error: {findings_file} not found", file=sys.stderr)
        sys.exit(2)

    findings_wrapper = json.loads(findings_file.read_text())
    # scanner-deduped.json may be either a list or {data: {findings: [...]}} — handle both
    if isinstance(findings_wrapper, list):
        findings = findings_wrapper
    elif "data" in findings_wrapper and "findings" in findings_wrapper["data"]:
        findings = findings_wrapper["data"]["findings"]
    elif "findings" in findings_wrapper:
        findings = findings_wrapper["findings"]
    else:
        print(f"Error: unrecognized shape in {findings_file}", file=sys.stderr)
        sys.exit(2)

    state_file = zwiad_root / "pipeline" / "state" / "clusters.json"
    if state_file.exists():
        state = json.loads(state_file.read_text())
        existing_clusters = state.get("clusters", state if isinstance(state, list) else [])
    else:
        existing_clusters = []
    clusters_by_slug = {c["slug"]: c for c in existing_clusters}

    existing_reports = load_existing_reports(zwiad_root)
    reports_by_cluster: dict[str, list[dict]] = {}
    for r in existing_reports:
        cs = r.get("cluster_slug")
        if cs:
            reports_by_cluster.setdefault(cs, []).append(r)

    routing = []
    for f in findings:
        fid = f.get("finding_id") or f.get("id") or ""
        title = f.get("title", "")
        gist = f.get("gist") or f.get("summary") or f.get("description", "")
        url = f.get("url") or f.get("source_url") or ""
        topic = f.get("category") or f.get("topic") or "privacy"

        print(f"[{fid}] classifying: {title[:60]}…")
        slug, name = classify_report(title, gist, topic, existing_clusters)
        if not slug:
            routing.append({
                "finding_id": fid,
                "route": "NEW_REPORT",
                "cluster_slug": "",
                "cluster_name": "",
                "rationale": "classification failed; defaulting to new report",
            })
            continue

        # Register new cluster so subsequent findings can reuse it
        if slug not in clusters_by_slug:
            clusters_by_slug[slug] = {"slug": slug, "name": name, "topic": topic, "summary": "", "reports": []}
            existing_clusters.append(clusters_by_slug[slug])

        candidates = reports_by_cluster.get(slug, [])
        if not candidates:
            routing.append({
                "finding_id": fid,
                "route": "NEW_REPORT",
                "cluster_slug": slug,
                "cluster_name": name,
                "rationale": "first report in this cluster",
            })
            continue

        print(f"  routing against {len(candidates)} existing report(s)…")
        decision = route_finding(title, gist, url, candidates)
        if not decision:
            routing.append({
                "finding_id": fid,
                "route": "NEW_REPORT",
                "cluster_slug": slug,
                "cluster_name": name,
                "rationale": "route LLM failed; defaulting to new report",
            })
            continue

        entry = {
            "finding_id": fid,
            "route": decision["route"],
            "cluster_slug": slug,
            "cluster_name": name,
            "rationale": decision.get("rationale", ""),
        }
        if decision["route"] in ("MERGE", "APPEND_SOURCE"):
            entry["target_report_slug"] = decision.get("target_report_slug", "")
        routing.append(entry)

    out_file = run_dir / "scanner-routing.json"
    out_file.write_text(json.dumps({"routing": routing}, indent=2) + "\n")

    by_route = {}
    for r in routing:
        by_route[r["route"]] = by_route.get(r["route"], 0) + 1
    print(f"Wrote {out_file}")
    for k, v in by_route.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
