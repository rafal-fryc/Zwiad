#!/usr/bin/env python3
"""Process FPF emails chronologically to build up the bill tracker.

Usage: python3 tools/process_fpf_chronological.py [--start-from WEEK_NUM]
"""

import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
FIXTURES_DIR = PROJECT_ROOT / "tests" / "fixtures" / "fpf-emails"
RUNS_DIR = PROJECT_ROOT / "pipeline" / "runs"

# Chronological email pairs (AI + Privacy per week), excluding April (validation set)
WEEKLY_PAIRS = [
    # Week 1: Jan 22-23 (AI already processed, need Privacy)
    {
        "week": 1,
        "label": "Jan-22-23",
        "ai": "FPF-U.S.-AI-Legislation-Update-January-22",
        "privacy": "FPF-U.S.-Privacy-Legislation-Updates-January-23",
    },
    # Week 2: Jan 29-30
    {
        "week": 2,
        "label": "Jan-29-30",
        "ai": "FPF-U.S.-AI-Legislation-Update-January-29",
        "privacy": "FPF-U.S.-Privacy-Legislation-Updates-January-30",
    },
    # Week 3: Feb 5-6
    {
        "week": 3,
        "label": "Feb-5-6",
        "ai": "FPF-U.S.-AI-Legislation-Update-February-5",
        "privacy": "FPF-U.S.-Privacy-Legislation-Updates-February-6",
    },
    # Week 4: Feb 12-13 (AI email has different naming)
    {
        "week": 4,
        "label": "Feb-12-13",
        "ai": "AI-Legislation-Update_-Virginia-Bill-Movement-California-Chatbot-Updates--Illinois-Bill-Surge-February-12",
        "privacy": "FPF-U.S.-Privacy-Legislation-Updates-February-13",
    },
    # Week 5: Feb 19-20
    {
        "week": 5,
        "label": "Feb-19-20",
        "ai": "FPF-U.S.-AI-Legislation-Update-February-19",
        "privacy": "FPF-U.S.-Privacy-Legislation-Updates-February-20",
    },
    # Week 6: Feb 26-27
    {
        "week": 6,
        "label": "Feb-26-27",
        "ai": "FPF-U.S.-AI-Legislation-Update-February-26",
        "privacy": "FPF-U.S.-Privacy-Legislation-Updates-February-27",
    },
    # Week 7: Mar 5-6
    {
        "week": 7,
        "label": "Mar-5-6",
        "ai": "FPF-U.S.-AI-Legislation-Update-March-5",
        "privacy": "FPF-U.S.-Privacy-Legislation-Updates-March-6",
    },
    # Week 8: Mar 12-13
    {
        "week": 8,
        "label": "Mar-12-13",
        "ai": "FPF-U.S.-AI-Legislation-Update-March-12",
        "privacy": "FPF-U.S.-Privacy-Legislation-Updates-March-13",
    },
    # Week 9: Mar 19-20
    {
        "week": 9,
        "label": "Mar-19-20",
        "ai": "FPF-U.S.-AI-Legislation-Update-March-19",
        "privacy": "FPF-U.S.-Privacy-Legislation-Updates-March-20",
    },
    # Week 10: Mar 26-27
    {
        "week": 10,
        "label": "Mar-26-27",
        "ai": "FPF-U.S.-AI-Legislation-Update-March-26",
        "privacy": "FPF-U.S.-Privacy-Legislation-Updates-March-27",
    },
]


def setup_run(week: dict) -> tuple[str, Path]:
    """Create a run directory with the week's email files."""
    run_id = f"fpf-chronological-week-{week['week']:02d}-{week['label']}"
    run_dir = RUNS_DIR / run_id
    emails_dir = run_dir / "emails"
    emails_dir.mkdir(parents=True, exist_ok=True)

    for email_type in ("ai", "privacy"):
        base = week[email_type]
        html_src = FIXTURES_DIR / f"{base}.html"
        meta_src = FIXTURES_DIR / f"{base}.meta.json"

        if html_src.exists():
            shutil.copy2(html_src, emails_dir / f"{base}.html")
        if meta_src.exists():
            shutil.copy2(meta_src, emails_dir / f"{base}.meta.json")

    return run_id, run_dir


def run_fpf_scanner(run_id: str) -> bool:
    """Run the fpf-scanner agent on a run's emails."""
    prompt = (
        f"Scan FPF legislative tracking emails. Pipeline run ID: {run_id}. "
        f"Email files are in pipeline/runs/{run_id}/emails/. "
        f"Read the existing tracker at bills/tracker.json to check for existing bills. "
        f"Write output to pipeline/runs/{run_id}/fpf-scanner-output.json"
    )

    cmd = [
        "claude", "-p",
        "--agent", "fpf-scanner",
        "--output-format", "json",
        "--permission-mode", "acceptEdits",
        "--max-turns", "40",
        prompt,
    ]

    output_path = RUNS_DIR / run_id / "fpf-scanner-output.json"
    output_path.unlink(missing_ok=True)
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(PROJECT_ROOT))

    if result.returncode != 0:
        print(f"  Scanner: FAILED — exit {result.returncode}")
        return False
    if output_path.exists():
        with open(output_path) as f:
            data = json.load(f)
        bills = data.get("data", {}).get("bills", [])
        new_count = sum(1 for b in bills if b.get("is_new"))
        update_count = sum(1 for b in bills if not b.get("is_new"))
        print(f"  Scanner: {len(bills)} bills ({new_count} new, {update_count} updates)")
        return True
    else:
        print(f"  Scanner: FAILED — no output file")
        return False


def run_bill_processor(run_id: str) -> bool:
    """Run the bill processor on scanner output."""
    fpf_output = RUNS_DIR / run_id / "fpf-scanner-output.json"
    if not fpf_output.exists():
        print(f"  Processor: skipped (no scanner output)")
        return False

    cmd = [
        "python3", "tools/bill_processor.py", "process",
        "--fpf-output", str(fpf_output),
        "--run-id", run_id,
        "--skip-convert",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(PROJECT_ROOT))

    results_path = RUNS_DIR / run_id / "fpf-bills-processed.json"
    if results_path.exists():
        with open(results_path) as f:
            data = json.load(f)
        print(f"  Processor: {data['new_bills']} new, {data['status_updates']} updates, "
              f"{data['downloads_success']} downloads")
        return True
    else:
        print(f"  Processor: FAILED")
        # Print stderr for debugging
        if result.stderr:
            print(f"  stderr: {result.stderr[:300]}")
        return False


def print_tracker_summary():
    """Print current tracker state."""
    tracker_path = PROJECT_ROOT / "bills" / "tracker.json"
    with open(tracker_path) as f:
        tracker = json.load(f)

    bills = tracker.get("bills", {})
    by_status = {}
    for b in bills.values():
        status = b.get("current_status", "?")
        by_status[status] = by_status.get(status, 0) + 1

    print(f"\n  Tracker: {len(bills)} total bills")
    for status, count in sorted(by_status.items(), key=lambda x: -x[1]):
        print(f"    {status}: {count}")


def main():
    start_from = 1
    if len(sys.argv) > 1 and sys.argv[1] == "--start-from":
        start_from = int(sys.argv[2])

    for week in WEEKLY_PAIRS:
        if week["week"] < start_from:
            continue

        print(f"\n{'='*60}")
        print(f"WEEK {week['week']}: {week['label']}")
        print(f"{'='*60}")

        run_id, run_dir = setup_run(week)
        print(f"  Run ID: {run_id}")

        if not run_fpf_scanner(run_id):
            print(f"  STOPPING — scanner failed for week {week['week']}")
            break

        if not run_bill_processor(run_id):
            print(f"  WARNING — processor failed for week {week['week']}")

        print_tracker_summary()

    print(f"\n{'='*60}")
    print("CHRONOLOGICAL PROCESSING COMPLETE")
    print(f"{'='*60}")
    print_tracker_summary()


if __name__ == "__main__":
    main()
