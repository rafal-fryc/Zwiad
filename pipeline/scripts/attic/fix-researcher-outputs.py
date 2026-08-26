#!/usr/bin/env python3
"""
Fix researcher output format for 2026-04-12T21-18-15 run.
Extracts report_markdown, writes to disk, reformats JSONs to proper envelope.
"""
import json
import os

run_id = "2026-04-12T21-18-15"
run_dir = f"pipeline/runs/{run_id}"

report_paths = {
    "SCAN-20260412-001": "reports/privacy/state-comprehensive-laws/alabama-hb351-pdpa-2026-04-12.md",
    "SCAN-20260412-002": "reports/privacy/maine-ld1822-privacy-bill-failed-2026-04-12.md",
    "SCAN-20260412-003": "reports/cybersecurity/anthropic-claude-mythos-cyberattack-2026-04-12.md",
    "SCAN-20260412-006": "reports/privacy/financial-privacy/glba-reform-huizenga-discussion-draft-2026-04-12.md",
    "SCAN-20260412-007": "reports/privacy/cppa-drop-audit-rulemaking-2026-04-12.md",
    "SCAN-20260412-008": "reports/privacy/illinois-bipa-7th-circuit-retroactivity-2026-04-12.md",
    "SCAN-20260412-009": "reports/privacy/take-it-down-act-first-conviction-2026-04-12.md",
    "SCAN-20260412-010": "reports/privacy/hhs-ocr-hipaa-risk-management-video-2026-04-12.md",
    "SCAN-20260412-014": "reports/privacy/doj-vppa-first-circuit-brief-2026-04-12.md",
    "SCAN-20260412-022": "reports/privacy/state-comprehensive-laws/alabama-pdpa-hb351-analysis-2026-04-12.md",
    "SCAN-20260412-023": "reports/privacy/state-privacy-roundup-ky-ny-me-april-2026.md",
    "SCAN-20260412-026": "reports/ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md",
    "SCAN-20260412-028": "reports/privacy/take-it-down-act-strahler-conviction-2026-04-12.md",
}

for fid, report_path in report_paths.items():
    json_path = f"{run_dir}/researcher-{fid}.json"

    with open(json_path) as f:
        data = json.load(f)

    inner = data.get("data", {})
    report_markdown = inner.get("report_markdown", "")
    title = inner.get("title", fid)
    sources = inner.get("sources", [])
    verification_status = inner.get("verification_status", "partial")
    produced_at = data.get("produced_at", "2026-04-12T22:00:00+00:00")

    # Write report markdown to disk
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w") as f:
        f.write(report_markdown)

    # Rewrite researcher JSON with proper envelope format
    new_json = {
        "schema_version": "1.0",
        "pipeline_run_id": run_id,
        "timestamp": produced_at,
        "stage": "researcher",
        "status": "complete",
        "data": {
            "finding_id": fid,
            "title": title,
            "report_path": report_path,
            "verification_status": verification_status,
            "sources_count": len(sources),
            "sources": sources,
        },
    }

    with open(json_path, "w") as f:
        json.dump(new_json, f, indent=2)

    print(f"OK: {fid} -> {report_path} ({len(report_markdown)} chars)")

print("Done.")
