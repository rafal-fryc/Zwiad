#!/usr/bin/env python3
"""Zwiad regulatory monitoring pipeline entry point.

Usage:
    python3 run_pipeline.py run --input <digest-file>   # Scan from email digest
    python3 run_pipeline.py run --web-only               # Scan web sources only
    python3 run_pipeline.py resume <run-id>              # Resume after approval
"""

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from tools.claude_stage import (
    RATE_LIMIT_MAX_WAITS,
    count_reviewable_reports,
    looks_rate_limited_err,
    rate_limit_wait_seconds,
    research_timeout,
    review_timeout,
    run_claude_and_log_cost,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent
PIPELINE_DIR = PROJECT_ROOT / "pipeline"
RUNS_DIR = PIPELINE_DIR / "runs"
PENDING_DIR = PIPELINE_DIR / "pending"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def create_run_id() -> str:
    """Generate a UTC-timestamped run ID (matches run-scanner.sh pattern)."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%S")


def setup_run_dir(run_id: str) -> Path:
    """Create and return the run directory for *run_id*."""
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir


def notify(title: str, message: str) -> None:
    """Send a desktop notification via notify-send (best-effort).

    Falls back to stdout if notify-send is unavailable or times out.
    """
    print(f"[NOTIFY] Zwiad: {title} -- {message}")
    if os.environ.get("ZWIAD_QUIET") == "1":
        return  # suppress desktop notifications (used for bulk backfills)
    try:
        subprocess.run(
            ["notify-send", "--urgency=normal", f"Zwiad: {title}", message],
            timeout=5,
            capture_output=True,
        )
    except FileNotFoundError:
        pass  # notify-send not installed -- stdout fallback above suffices
    except subprocess.TimeoutExpired:
        pass  # non-critical


def run_stage(
    name: str,
    cmd: list,
    run_id: str,
    run_dir: Path,
    audit_entries: list,
    timeout: int = 3600,
) -> None:
    """Execute a pipeline stage via the shared runner, record audit info, and handle errors.

    Usage/session rate limits are waited out and retried automatically (up to
    RATE_LIMIT_MAX_WAITS sleeps, each bounded by the shared wait policy) —
    stage outputs are per-item and idempotent, so a retry simply continues.
    """
    start = time.monotonic()
    start_wall = datetime.now(timezone.utc).isoformat()

    print(f"[STAGE] {name} -- starting at {start_wall}")

    cost = 0.0
    rl_waits = 0
    while True:
        ok, err, leg_cost = run_claude_and_log_cost(cmd, run_id, name, cwd=PROJECT_ROOT, timeout=timeout)
        cost += leg_cost
        if ok or not looks_rate_limited_err(err):
            break
        wait = rate_limit_wait_seconds(err, rl_waits)
        if wait is None:
            break  # wait budget exhausted or reset too far out -- fail the stage
        rl_waits += 1
        print(
            f"[STAGE] {name} -- rate-limited; sleeping {wait}s then resuming "
            f"(wait {rl_waits}/{RATE_LIMIT_MAX_WAITS})"
        )
        notify(
            "Rate limited",
            f"Stage {name} for run {run_id} hit a usage limit; auto-resuming in ~{wait // 60} min",
        )
        time.sleep(wait)

    end = time.monotonic()
    duration = round(end - start, 1)

    if not ok:
        # Write error.log
        error_log = run_dir / "error.log"
        with open(error_log, "a") as f:
            f.write(f"[{name}] duration={duration}s\n")
            f.write(f"error:\n{err}\n\n")

        audit_entries.append({
            "name": name,
            "duration_seconds": duration,
            "status": "error",
            "error": err[:500],
        })

        notify("Pipeline Failure", f"Stage {name} failed for run {run_id}")
        raise RuntimeError(f"Stage {name} failed: {err[:200]}")

    audit_entries.append({
        "name": name,
        "duration_seconds": duration,
        "status": "complete",
        "cost_usd": cost,
    })

    print(f"[STAGE] {name} -- completed in {duration}s")


# ---------------------------------------------------------------------------
# Phase runners
# ---------------------------------------------------------------------------


def run_scan_phase(
    run_id: str,
    run_dir: Path,
    audit_entries: list,
    input_file: str | None = None,
    web_only: bool = False,
) -> list:
    """Execute the scan phase via the orchestrator agent."""
    prompt_parts = [
        f"Scan phase for run {run_id}.",
        f"Write all output to pipeline/runs/{run_id}/.",
    ]

    if input_file:
        abs_input = str(Path(input_file).resolve())
        prompt_parts.append(f"Input digest file: {abs_input}")
    elif web_only:
        prompt_parts.append("Web sources only (--sources-only). No email digest.")

    prompt = " ".join(prompt_parts)

    cmd = [
        "claude", "-p",
        "--agent", "orchestrator",
        "--output-format", "json",
        "--permission-mode", "acceptEdits",
        "--max-turns", "30",
        prompt,
    ]

    run_stage("orchestrator-scan", cmd, run_id, run_dir, audit_entries)

    # Routing runs here in the driver, NOT inside the orchestrator:
    # route-findings.py spawns nested `claude -p` calls that stall inside a
    # non-interactive orchestrator session. Best-effort — the research phase
    # defaults findings to NEW_REPORT when scanner-routing.json is absent,
    # so a routing failure warns loudly but does not fail the scan.
    if (run_dir / "scanner-deduped.json").exists():
        for route_cmd, label in [
            (["python3", "pipeline/scripts/build-clusters-state.py"], "build-clusters"),
            (["python3", "pipeline/scripts/route-findings.py", str(run_dir)], "route-findings"),
        ]:
            try:
                # Routing makes up to two 120s-bounded claude calls per finding.
                result = subprocess.run(route_cmd, cwd=PROJECT_ROOT, timeout=7200)
                route_ok = result.returncode == 0
            except (OSError, subprocess.TimeoutExpired):
                route_ok = False
            if not route_ok:
                audit_entries.append({
                    "name": f"routing-{label}", "duration_seconds": 0, "status": "warning",
                    "error": f"{label} failed -- findings default to NEW_REPORT (duplicate risk)",
                })
                print(f"[WARN] routing step {label} failed; findings default to NEW_REPORT")
                break

    # Check for scan-complete marker
    marker = run_dir / "scan-complete.marker"
    if not marker.exists():
        audit_entries.append({
            "name": "scan-marker-check",
            "duration_seconds": 0,
            "status": "warning",
            "error": "scan-complete.marker not found -- orchestrator may not have finished cleanly",
        })
        print("[WARN] scan-complete.marker not found in run directory")

    notify(
        "Findings Ready",
        f"Run {run_id}: Review scanner findings at pipeline/runs/{run_id}/scanner-review.md",
    )

    return audit_entries


def run_research_phase(
    run_id: str,
    run_dir: Path,
    audit_entries: list,
) -> list:
    """Execute the research phase via the orchestrator agent."""
    # Validate state: approved findings must exist
    approved = run_dir / "scanner-approved.json"
    if not approved.exists():
        raise RuntimeError(
            f"Cannot resume: scanner-approved.json not found in {run_dir}. "
            "Approve findings first via pipeline/scripts/approve-findings.sh"
        )

    # Guard against duplicate runs
    cat_output = run_dir / "categorizer-output.json"
    if cat_output.exists():
        raise RuntimeError(
            f"Run {run_id} already complete (categorizer-output.json exists). "
            "Create a new run instead."
        )

    research_prompt = (
        f"Run Mode 2 (research-only) for run {run_id}, exactly as specified in your "
        f"instructions. Process approved findings from "
        f"pipeline/runs/{run_id}/scanner-approved.json: researcher per finding (skip "
        f"findings whose researcher-{{id}}.json already exists), then write "
        f"research-complete.marker and stop. The scope of this invocation is researcher "
        f"outputs only; review and categorization run in a later, separate invocation."
    )
    cmd = [
        "claude", "-p", "--agent", "orchestrator",
        "--output-format", "json", "--permission-mode", "acceptEdits",
        "--max-turns", "200", research_prompt,
    ]
    # Research cost scales with the finding count, so the timeout must too --
    # a fixed value gets the stage SIGKILLed mid-stride on large batches.
    # Re-running resume continues from the researcher outputs already on disk.
    try:
        approved_findings = json.loads(approved.read_text()).get("data", {}).get("findings", [])
    except (json.JSONDecodeError, OSError):
        approved_findings = []
    todo = sum(
        1 for f in approved_findings
        if not (run_dir / f"researcher-{f.get('id','')}.json").exists()
    )
    run_stage("orchestrator-research", cmd, run_id, run_dir, audit_entries,
              timeout=research_timeout(todo))

    if not (run_dir / "research-complete.marker").exists():
        audit_entries.append({
            "name": "research-marker-check", "duration_seconds": 0, "status": "warning",
            "error": "research-complete.marker not found -- re-run resume to retry (idempotent)",
        })
        print("[WARN] research-complete.marker not found; stopping before review phase")
        return audit_entries

    review_prompt = (
        f"Run Mode 4 (review & categorize) for run {run_id}, exactly as specified in "
        f"your instructions: verify research-complete.marker exists, run reviewer, "
        f"check escalations, run categorizer if no escalations, and write "
        f"pipeline-complete.marker. The scope of this invocation starts from the "
        f"researcher outputs already on disk; research is complete."
    )
    cmd = [
        "claude", "-p", "--agent", "orchestrator",
        "--output-format", "json", "--permission-mode", "acceptEdits",
        "--max-turns", "200", review_prompt,
    ]
    # Review wall-clock scales with the report count, same as research -- a
    # fixed 5400s SIGKILLed large batches mid-review. review_timeout() caps at
    # 6h; anything beyond that is picked up by an idempotent re-run.
    run_stage("orchestrator-review", cmd, run_id, run_dir, audit_entries,
              timeout=review_timeout(count_reviewable_reports(run_dir)))

    complete_marker = run_dir / "pipeline-complete.marker"
    escalation_marker = run_dir / "has-escalations.marker"
    if escalation_marker.exists() or any(run_dir.glob("escalation-*.json")):
        notify("Escalations Pending", f"Run {run_id}: Review escalations")
    elif complete_marker.exists():
        notify("Pipeline Complete", f"Run {run_id}: Reports filed")
    else:
        audit_entries.append({
            "name": "review-marker-check", "duration_seconds": 0, "status": "warning",
            "error": "Neither pipeline-complete.marker nor escalations found",
        })
        print("[WARN] No completion marker found in run directory")
    return audit_entries


# ---------------------------------------------------------------------------
# Audit log
# ---------------------------------------------------------------------------


def _read_json_safe(path: Path) -> dict | list | None:
    """Read a JSON file, returning None on any error."""
    try:
        with open(path) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return None


def _format_duration(seconds: float) -> str:
    """Human-readable duration string."""
    if seconds < 60:
        return f"{seconds:.1f}s"
    minutes = int(seconds // 60)
    secs = seconds % 60
    return f"{minutes}m {secs:.1f}s"


def write_audit_log(
    run_id: str,
    run_dir: Path,
    audit_entries: list,
    overall_status: str,
    start_time: str,
) -> None:
    """Write audit-log.md to the run directory."""
    end_time = datetime.now(timezone.utc).isoformat()

    lines = [
        "# Pipeline Audit Log",
        "",
        f"**Run ID:** {run_id}",
        f"**Started:** {start_time}",
        f"**Completed:** {end_time}",
        f"**Status:** {overall_status}",
        "",
    ]

    # Stage entries
    for entry in audit_entries:
        lines.append(f"## {entry['name']}")
        lines.append(f"- **Duration:** {_format_duration(entry['duration_seconds'])}")
        lines.append(f"- **Status:** {entry['status']}")
        if entry.get("error"):
            lines.append(f"- **Error:** {entry['error']}")
        lines.append("")

    # Summary counts from run directory artifacts
    lines.append("## Artifact Summary")
    lines.append("")

    scanner_output = _read_json_safe(run_dir / "scanner-output.json")
    if scanner_output and isinstance(scanner_output, dict):
        data = scanner_output.get("data", scanner_output)
        findings = data.get("findings", [])
        source_failures = data.get("source_failures", [])
        lines.append(f"- **Scanner findings:** {len(findings)}")
        lines.append(f"- **Source failures:** {len(source_failures)}")

    approved = _read_json_safe(run_dir / "scanner-approved.json")
    if approved and isinstance(approved, dict):
        data = approved.get("data", approved)
        approved_findings = data.get("findings", data.get("approved_findings", []))
        lines.append(f"- **Approved findings:** {len(approved_findings)}")

    reviewer = _read_json_safe(run_dir / "reviewer-output.json")
    if reviewer and isinstance(reviewer, dict):
        data = reviewer.get("data", reviewer)
        reviews = data.get("reviews", [])
        verified = sum(1 for r in reviews if r.get("status") == "verified")
        escalated = sum(1 for r in reviews if r.get("status") == "needs-human-review")
        lines.append(f"- **Reviewer verified:** {verified}")
        lines.append(f"- **Reviewer escalated:** {escalated}")

    categorizer = _read_json_safe(run_dir / "categorizer-output.json")
    if categorizer and isinstance(categorizer, dict):
        data = categorizer.get("data", categorizer)
        filed = data.get("filed", [])
        pending = data.get("pending", [])
        lines.append(f"- **Categorizer filed:** {len(filed)}")
        lines.append(f"- **Categorizer pending:** {len(pending)}")

    lines.append("")

    # Errors section
    errors = [e for e in audit_entries if e["status"] == "error"]
    lines.append("## Errors")
    lines.append("")
    if errors:
        for e in errors:
            lines.append(f"- **{e['name']}:** {e.get('error', 'unknown')}")
    else:
        lines.append("None")
    lines.append("")

    audit_path = run_dir / "audit-log.md"
    with open(audit_path, "w") as f:
        f.write("\n".join(lines))

    print(f"[AUDIT] Written to {audit_path}")


# ---------------------------------------------------------------------------
# Subcommand handlers
# ---------------------------------------------------------------------------


def cmd_run(args: argparse.Namespace) -> None:
    """Handle the 'run' subcommand -- execute scan phase."""
    if not args.input and not args.web_only:
        print("ERROR: Provide --input <file> or --web-only", file=sys.stderr)
        sys.exit(1)

    input_file = None
    if args.input:
        input_path = Path(args.input)
        if not input_path.exists():
            print(f"ERROR: Input file not found: {args.input}", file=sys.stderr)
            sys.exit(1)
        input_file = str(input_path)

    run_id = create_run_id()
    run_dir = setup_run_dir(run_id)
    audit_entries: list = []
    start_time = datetime.now(timezone.utc).isoformat()

    print(f"[RUN] Pipeline run {run_id}")
    print(f"[RUN] Run directory: {run_dir}")
    print(f"[ENV] PATH={os.environ.get('PATH', '(unset)')}")
    print(f"[ENV] DISPLAY={os.environ.get('DISPLAY', '(unset)')}")
    print(f"[ENV] Python={sys.executable}")

    try:
        run_scan_phase(
            run_id, run_dir, audit_entries,
            input_file=input_file, web_only=args.web_only,
        )
        write_audit_log(run_id, run_dir, audit_entries, "scan-complete", start_time)
    except RuntimeError as exc:
        write_audit_log(run_id, run_dir, audit_entries, "error", start_time)
        notify("Pipeline Failure", str(exc)[:200])
        print(f"[ERROR] {exc}", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        # Catch-all for unexpected errors
        error_log = run_dir / "error.log"
        with open(error_log, "a") as f:
            f.write(f"[unexpected] {type(exc).__name__}: {exc}\n")
        write_audit_log(run_id, run_dir, audit_entries, "error", start_time)
        notify("Pipeline Failure", f"Unexpected error: {exc}")
        print(f"[ERROR] Unexpected: {exc}", file=sys.stderr)
        sys.exit(1)

    print()
    print(f"Scan complete. Review findings at: pipeline/runs/{run_id}/scanner-review.md")
    print(f"After approval, run: python3 run_pipeline.py resume {run_id}")


def cmd_resume(args: argparse.Namespace) -> None:
    """Handle the 'resume' subcommand -- execute research phase."""
    run_id = args.run_id
    run_dir = RUNS_DIR / run_id

    if not run_dir.is_dir():
        print(f"ERROR: Run directory not found: {run_dir}", file=sys.stderr)
        sys.exit(1)

    audit_entries: list = []
    start_time = datetime.now(timezone.utc).isoformat()

    print(f"[RESUME] Pipeline run {run_id}")
    print(f"[RESUME] Run directory: {run_dir}")
    print(f"[ENV] PATH={os.environ.get('PATH', '(unset)')}")
    print(f"[ENV] DISPLAY={os.environ.get('DISPLAY', '(unset)')}")
    print(f"[ENV] Python={sys.executable}")

    try:
        run_research_phase(run_id, run_dir, audit_entries)
        write_audit_log(run_id, run_dir, audit_entries, "complete", start_time)
    except RuntimeError as exc:
        write_audit_log(run_id, run_dir, audit_entries, "error", start_time)
        notify("Pipeline Failure", str(exc)[:200])
        print(f"[ERROR] {exc}", file=sys.stderr)
        sys.exit(1)
    except Exception as exc:
        error_log = run_dir / "error.log"
        with open(error_log, "a") as f:
            f.write(f"[unexpected] {type(exc).__name__}: {exc}\n")
        write_audit_log(run_id, run_dir, audit_entries, "error", start_time)
        notify("Pipeline Failure", f"Unexpected error: {exc}")
        print(f"[ERROR] Unexpected: {exc}", file=sys.stderr)
        sys.exit(1)

    print()
    print(f"Pipeline complete for run {run_id}.")

    # Check for escalations
    if (run_dir / "has-escalations.marker").exists():
        print("NOTE: Some findings were escalated. Review escalation reports.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    """Parse arguments and dispatch to subcommand handler."""
    parser = argparse.ArgumentParser(
        description="Zwiad regulatory monitoring pipeline",
    )
    subparsers = parser.add_subparsers(dest="command", help="Pipeline commands")

    # run subcommand
    run_parser = subparsers.add_parser("run", help="Start a new pipeline scan")
    run_parser.add_argument(
        "--input",
        metavar="FILE",
        help="Path to email digest file (.eml, .html, .txt)",
    )
    run_parser.add_argument(
        "--web-only",
        action="store_true",
        help="Scan web sources only (no email digest)",
    )
    run_parser.set_defaults(func=cmd_run)

    # resume subcommand
    resume_parser = subparsers.add_parser(
        "resume", help="Resume pipeline after findings approval",
    )
    resume_parser.add_argument(
        "run_id",
        help="Run ID to resume (e.g. 2026-04-07T14-30-00)",
    )
    resume_parser.set_defaults(func=cmd_resume)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    args.func(args)


if __name__ == "__main__":
    main()
