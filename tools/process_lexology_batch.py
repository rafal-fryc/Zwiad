#!/usr/bin/env python3
"""Bulk-process archived Lexology digests through the Zwiad pipeline.

Runs the pipeline chronologically across the Lexology/ subdir of the
FileTransfer repo. Bypasses Discord entirely and replaces the human
approval gate with auto-approve-lexology.py (US privacy/cyber/AI-law
only, no crypto).

Fast scan path:
    scanner-archive agent  -> scanner-output.json   (no WebFetch, ~30-60s)
    topic_keys.py annotate -> annotates in place
    dedup-findings.sh      -> scanner-deduped.json
    auto-approve-lexology  -> scanner-approved.json + scanner-auto-rejected.json
    run_pipeline.py resume -> research + review + categorize (orchestrator)

Resume semantics:
    processed-emails.json is updated ONLY after the full pipeline succeeds for
    a digest. A Ctrl-C (or any crash) mid-digest leaves the Message-ID unset,
    so re-running this script retries that digest from scratch in a new run-dir.

Graceful stop:
    First Ctrl-C -> finish current digest, write state, then exit.
    Second Ctrl-C -> interrupt the current subprocess and exit immediately.

Usage:
    python3 tools/process_lexology_batch.py [options]

Options:
    --limit N           Attempt at most N digests this session (success or failure).
    --from-date DATE    YYYY-MM-DD; skip digests whose filename date is earlier.
    --refresh           Re-fetch emails from GitHub even if input/lexology exists.
    --dry-run           Run scan + auto-approve; skip research (no reports written).
    --skip-research     Same as --dry-run.
    --input-dir DIR     Override input directory (default: input/lexology).
"""

import argparse
import json
import os
import re
import signal
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
STATE_FILE = PROJECT_ROOT / "pipeline" / "state" / "processed-emails.json"
RUNS_DIR = PROJECT_ROOT / "pipeline" / "runs"

# Suppress desktop notifications for the entire backfill. run_pipeline.py
# respects this env var; set it once here so every subprocess inherits.
os.environ["ZWIAD_QUIET"] = "1"

DATE_PREFIX_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})")

# --- graceful stop -----------------------------------------------------------

STOP_AFTER_CURRENT = False


def _install_sigint_handler() -> None:
    def handler(signum, frame):
        global STOP_AFTER_CURRENT
        if not STOP_AFTER_CURRENT:
            STOP_AFTER_CURRENT = True
            print("\n[batch] SIGINT received — will stop after current digest. "
                  "Press Ctrl-C again to abort immediately.", flush=True)
        else:
            print("\n[batch] second SIGINT — aborting now.", flush=True)
            # restore default and re-raise so any running subprocess is terminated
            signal.signal(signal.SIGINT, signal.SIG_DFL)
            os.kill(os.getpid(), signal.SIGINT)
    signal.signal(signal.SIGINT, handler)


# --- state -------------------------------------------------------------------


def load_processed() -> dict:
    if not STATE_FILE.exists():
        return {"schema_version": "1.0", "processed": {}}
    return json.loads(STATE_FILE.read_text())


def save_processed(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_FILE.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, indent=2))
    tmp.replace(STATE_FILE)


def read_meta(html_path: Path) -> dict:
    meta_path = html_path.with_name(html_path.stem + ".meta.json")
    if meta_path.exists():
        try:
            return json.loads(meta_path.read_text())
        except json.JSONDecodeError:
            return {}
    return {}


def msgid_for(html_path: Path, meta: dict) -> str:
    msgid = (meta.get("message-id") or meta.get("Message-ID") or "").strip()
    return msgid or f"lexology-archive:{html_path.name}"


def create_run_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%S")


# --- pipeline steps ----------------------------------------------------------


def _run(cmd: list, cwd: Path = PROJECT_ROOT, check: bool = True) -> int:
    """Run a subprocess, streaming stdout/stderr. Returns exit code."""
    try:
        result = subprocess.run(cmd, cwd=str(cwd))
    except KeyboardInterrupt:
        # propagate SIGINT to our handler; re-raise so caller knows
        raise
    if check and result.returncode != 0:
        raise RuntimeError(
            f"command failed (exit {result.returncode}): {' '.join(str(c) for c in cmd)}"
        )
    return result.returncode


def run_scanner_archive(run_id: str, digest: Path) -> None:
    """Parse the digest HTML deterministically (no LLM, no network)."""
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    meta_path = digest.with_name(digest.stem + ".meta.json")
    output_path = run_dir / "scanner-output.json"

    _run([
        sys.executable,
        "pipeline/scripts/parse_lexology_archive.py",
        "--digest", str(digest),
        "--meta", str(meta_path),
        "--run-id", run_id,
        "--output", str(output_path),
    ])

    if not output_path.exists():
        raise RuntimeError(f"parser did not write {output_path}")


def run_topic_keys(run_id: str) -> None:
    scanner_output = RUNS_DIR / run_id / "scanner-output.json"
    _run([sys.executable, "tools/topic_keys.py", "annotate",
          "--input", str(scanner_output)])


def run_dedup(run_id: str) -> None:
    _run(["bash", "pipeline/scripts/dedup-findings.sh", run_id])


def run_auto_approve(run_id: str) -> None:
    _run([sys.executable, "pipeline/scripts/auto-approve-lexology.py", run_id])


def run_research(run_id: str) -> None:
    _run([sys.executable, "run_pipeline.py", "resume", run_id])


# --- fetch -------------------------------------------------------------------


def fetch_lexology_emails(output_dir: Path) -> None:
    _run([sys.executable, "tools/fetch_lexology_emails.py", str(output_dir)])


# --- main loop ---------------------------------------------------------------


def process_one(digest: Path, dry_run: bool) -> tuple[str, int, int]:
    """Process a single digest. Returns (run_id, approved_count, rejected_count)."""
    run_id = create_run_id()
    print(f"  [scan] run_id={run_id}")
    run_scanner_archive(run_id, digest)
    run_topic_keys(run_id)
    run_dedup(run_id)
    run_auto_approve(run_id)

    approved_path = RUNS_DIR / run_id / "scanner-approved.json"
    rejected_path = RUNS_DIR / run_id / "scanner-auto-rejected.json"
    approved_count = len(
        json.loads(approved_path.read_text()).get("data", {}).get("findings", [])
    )
    rejected_count = len(
        json.loads(rejected_path.read_text()).get("data", {}).get("findings", [])
    )
    print(f"  [approve] approved={approved_count} rejected={rejected_count}")

    if dry_run:
        print("  [dry-run] skipping research phase")
    elif approved_count == 0:
        print("  [skip-research] no approved findings")
    else:
        print(f"  [research] starting ({approved_count} findings)...")
        run_research(run_id)

    return run_id, approved_count, rejected_count


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--limit", type=int, default=None,
                    help="Attempt at most N digests this session")
    ap.add_argument("--from-date", default=None)
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--skip-research", action="store_true")
    ap.add_argument("--input-dir", default=str(PROJECT_ROOT / "input" / "lexology"))
    args = ap.parse_args()

    dry_run = args.dry_run or args.skip_research
    input_dir = Path(args.input_dir)

    if args.refresh or not input_dir.exists() or not any(input_dir.glob("*.html")):
        print(f"[fetch] populating {input_dir}")
        fetch_lexology_emails(input_dir)

    digests = sorted(input_dir.glob("*.html"))
    if args.from_date:
        cutoff = args.from_date
        digests = [
            d for d in digests
            if (m := DATE_PREFIX_RE.match(d.name)) and m.group(1) >= cutoff
        ]

    print(f"[batch] {len(digests)} digest(s) in {input_dir} (chronological order)")

    _install_sigint_handler()

    processed_state = load_processed()
    processed_ids = processed_state.get("processed", {})

    attempted = 0
    succeeded = 0
    failed = 0
    skipped_resume = 0

    for idx, digest in enumerate(digests, 1):
        if STOP_AFTER_CURRENT:
            print(f"[batch] stop requested — halting before digest {idx}")
            break

        meta = read_meta(digest)
        mid = msgid_for(digest, meta)

        if mid in processed_ids:
            skipped_resume += 1
            continue

        attempted += 1
        print(f"[{idx}/{len(digests)}] {digest.name}")

        try:
            run_id, approved, rejected = process_one(digest, dry_run)

            processed_ids[mid] = {
                "first_seen_run": run_id,
                "subject": meta.get("subject", ""),
                "from": meta.get("from", ""),
                "processed_at": datetime.now(timezone.utc).isoformat(),
                "source": "lexology-archive-backfill",
                "approved_count": approved,
                "rejected_count": rejected,
                "dry_run": dry_run,
            }
            processed_state["processed"] = processed_ids
            save_processed(processed_state)
            succeeded += 1
        except KeyboardInterrupt:
            print("  [abort] keyboard interrupt during digest — state not recorded")
            raise
        except Exception as exc:
            failed += 1
            print(f"  [error] {type(exc).__name__}: {exc}", file=sys.stderr)
            # do not record in processed-emails.json — next run will retry this digest

        if args.limit is not None and attempted >= args.limit:
            print(f"[batch] --limit {args.limit} reached")
            break

    total_processed = len(processed_ids)
    print(
        f"\n[batch] done. "
        f"attempted={attempted} succeeded={succeeded} failed={failed} "
        f"already_done={skipped_resume} total_in_state={total_processed}"
    )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[batch] interrupted.", file=sys.stderr)
        sys.exit(130)
