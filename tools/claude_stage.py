"""Shared stage-runner module for Zwiad pipeline agents.

Provides subprocess execution helpers with process-group timeouts, rate-limit
detection, error persistence, and cost logging. Used by both discord_bot.py
and run_pipeline.py.
"""

from __future__ import annotations

import json
import os
import re
import signal
import subprocess
import tempfile
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tools.logging_setup import get_logger  # noqa: E402

logger = get_logger("zwiad.stage")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RUNS_DIR = PROJECT_ROOT / "pipeline" / "runs"


# ---------------------------------------------------------------------------
# Atomic JSON writer
# ---------------------------------------------------------------------------

def _atomic_write_json(path: Path, data) -> None:
    """Write *data* as JSON to *path* atomically via a temp file + os.replace.

    Prevents corrupt state files if the process dies mid-write. Write errors
    propagate to the caller after the temp file is cleaned up.
    """
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=f".{path.stem}-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        os.replace(tmp, path)
    except Exception:
        if os.path.exists(tmp):
            os.remove(tmp)
        raise


# ---------------------------------------------------------------------------
# Rate-limit detection
# ---------------------------------------------------------------------------

# Substrings (case-insensitive) that indicate the claude CLI session hit an
# Anthropic usage/rate limit rather than a genuine pipeline error.
_RATE_LIMIT_MARKERS = (
    "rate limit",
    "rate_limit",
    "usage limit",
    "usage_limit",
    "429",
    "too many requests",
    "overloaded",
    "quota",
    "exceeded your",
    "you've reached your",
    "claude usage limit reached",
)


def looks_rate_limited(text: str, parsed: dict | None) -> bool:
    """Heuristic: does this failed claude run look like a usage/rate limit?

    Scans the raw output and the parsed JSON's error-ish fields for known
    Anthropic rate/usage-limit phrasing.
    """
    haystack = (text or "").lower()
    if parsed:
        for key in ("terminal_reason", "subtype", "result", "error"):
            val = parsed.get(key)
            if isinstance(val, str):
                haystack += " " + val.lower()
    return any(marker in haystack for marker in _RATE_LIMIT_MARKERS)


# Marker embedded in the error message run_claude_and_log_cost returns for
# rate-limited runs. Callers use looks_rate_limited_err() on that message the
# same way looks_timed_out() pairs with _TIMEOUT_MARKER — keep them in sync.
_RATE_LIMIT_ERR_MARKER = "hit an Anthropic usage/rate limit"


def looks_rate_limited_err(err: str) -> bool:
    """True if *err* came from a stage that hit a usage/rate limit."""
    return _RATE_LIMIT_ERR_MARKER in (err or "")


# "Limit resets at 2026-06-29T12:30:00-04:00." — the machine-readable form
# run_claude_and_log_cost embeds in its own error message.
_RESET_ISO_RE = re.compile(r"resets at (\d{4}-\d{2}-\d{2}T[0-9:.+\-]+)")

# "resets 12:30pm (America/New_York)" / "resets at 3am (UTC)" — the human form
# the claude CLI puts in its result string. Requires minutes or am/pm so a bare
# number elsewhere in the text can't match.
_RESET_HUMAN_RE = re.compile(
    r"resets?\s+(?:at\s+)?"
    r"(?P<h>\d{1,2})"
    r"(?::(?P<m>\d{2}))?"
    r"\s*(?P<ampm>am|pm)?"
    r"(?:\s*\((?P<tz>[^)]+)\))?",
    re.IGNORECASE,
)


def parse_rate_limit_reset(text: str, now: datetime | None = None) -> datetime | None:
    """Extract the limit-reset time from a rate-limit error, if present.

    Handles both the ISO form this module embeds in its own error messages and
    the claude CLI's human phrasing ("resets 12:30pm (America/New_York)").
    Returns an aware datetime, or None when no reset time can be parsed.
    """
    if not text:
        return None
    now = now or datetime.now(timezone.utc)

    m = _RESET_ISO_RE.search(text)
    if m:
        try:
            # rstrip: the character class admits "." for fractional seconds, so
            # a sentence-ending period rides along with the match.
            dt = datetime.fromisoformat(m.group(1).rstrip("."))
            return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
        except ValueError:
            pass

    m = _RESET_HUMAN_RE.search(text)
    if not m or not (m.group("m") or m.group("ampm")):
        return None
    hour = int(m.group("h"))
    minute = int(m.group("m") or 0)
    ampm = (m.group("ampm") or "").lower()
    if hour > 23 or minute > 59:
        return None
    if ampm == "pm" and hour != 12:
        hour += 12
    elif ampm == "am" and hour == 12:
        hour = 0

    tzname = m.group("tz")
    if tzname:
        try:
            tz = ZoneInfo(tzname.strip())
        except Exception:
            # Unknown zone: guessing could be hours off — let the caller fall
            # back to blind backoff instead.
            return None
    else:
        # CLI omitted the zone: it formats to the machine's local time.
        tz = datetime.now(timezone.utc).astimezone().tzinfo

    local_now = now.astimezone(tz)
    candidate = local_now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if candidate <= local_now:
        candidate += timedelta(days=1)
    return candidate


# Auto-wait policy for rate-limited stages. A session limit usually lifts at a
# known reset time; waiting for it and resuming beats stopping the whole run
# (per-item checkpointing makes the resume idempotent).
RATE_LIMIT_MAX_WAIT_SECONDS = 6 * 3600   # never sleep longer than this
RATE_LIMIT_RESET_BUFFER_SECONDS = 120    # slack past the advertised reset
RATE_LIMIT_BACKOFF_SECONDS = (300, 900, 2700)  # when no reset time parses
RATE_LIMIT_MAX_WAITS = 4                 # per stage invocation


def rate_limit_wait_seconds(err: str, waits_used: int, now: datetime | None = None) -> int | None:
    """Seconds to sleep before resuming a rate-limited stage.

    Returns None when the caller should stop instead: wait budget exhausted,
    or the advertised reset is further out than RATE_LIMIT_MAX_WAIT_SECONDS.
    """
    if waits_used >= RATE_LIMIT_MAX_WAITS:
        return None
    now = now or datetime.now(timezone.utc)
    reset = parse_rate_limit_reset(err, now)
    if reset is not None:
        wait = (reset - now).total_seconds() + RATE_LIMIT_RESET_BUFFER_SECONDS
        if wait <= 0:
            return RATE_LIMIT_RESET_BUFFER_SECONDS
        if wait > RATE_LIMIT_MAX_WAIT_SECONDS:
            return None
        return int(wait)
    if waits_used < len(RATE_LIMIT_BACKOFF_SECONDS):
        return RATE_LIMIT_BACKOFF_SECONDS[waits_used]
    return None


# ---------------------------------------------------------------------------
# Process-group timeout runner
# ---------------------------------------------------------------------------

@dataclass
class _ProcResult:
    returncode: int
    stdout: str
    stderr: str
    timed_out: bool = False


def _run_with_timeout(cmd: list[str], cwd, timeout: int) -> _ProcResult:
    """Run *cmd* in its own process group, killing the whole group on timeout.

    claude -p spawns MCP-server children that hold the output pipes open, so a
    plain subprocess.run(timeout=...) can block in the post-kill read. Killing
    the process group avoids that.
    """
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=str(cwd) if cwd else None,
        start_new_session=True,
    )
    try:
        stdout, stderr = proc.communicate(timeout=timeout)
        return _ProcResult(proc.returncode, stdout or "", stderr or "")
    except subprocess.TimeoutExpired:
        try:
            os.killpg(proc.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        try:
            stdout, stderr = proc.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            stdout, stderr = "", ""
        return _ProcResult(-9, stdout or "", stderr or "", timed_out=True)


# ---------------------------------------------------------------------------
# Research phase sizing
#
# The research stage runs one `claude -p --agent orchestrator` process that
# researches every remaining finding sequentially, so its wall-clock cost
# scales with the finding count. A fixed timeout therefore fails
# deterministically past a certain size: run 2026-07-25T18-29-52 had 37
# approved findings and was SIGKILLed at exactly 5400s with 20 done and no
# slowdown.
#
# Measured per-finding durations: ~264s on that run (87 min / 20), ~354s on
# the slowest historical run. 420s gives headroom over both.
# ---------------------------------------------------------------------------

RESEARCH_SECONDS_PER_FINDING = 420
RESEARCH_TIMEOUT_OVERHEAD = 600      # agent startup, marker write, slack
RESEARCH_LEG_MAX_SECONDS = 5400      # per-leg ceiling: bounds a genuine hang
RESEARCH_MAX_LEGS = 6                # ~120 findings at the ceiling


def research_timeout(remaining: int) -> int:
    """Wall-clock budget for one research leg covering *remaining* findings.

    Scales with the workload but stays capped, so a hung agent is still killed
    within RESEARCH_LEG_MAX_SECONDS. Work beyond one leg is picked up by the
    next leg -- researcher outputs are written per finding and skipped on
    resume, so continuing is idempotent.
    """
    if remaining <= 0:
        return RESEARCH_TIMEOUT_OVERHEAD
    return min(
        RESEARCH_LEG_MAX_SECONDS,
        RESEARCH_TIMEOUT_OVERHEAD + remaining * RESEARCH_SECONDS_PER_FINDING,
    )


# The review stage has the same shape: run-reviewer.sh walks every report
# sequentially, up to 3 reviewer+researcher rounds each, so its wall-clock cost
# scales with the report count. Measured on run 2026-07-25T18-29-52: 17.2
# min/report (2026-07-26 session) and 12.4 min/report (2026-07-25 session).
# 1200s gives headroom over both.
#
# Unlike research, an over-run here is no longer destructive: run-reviewer.sh
# checkpoints reviewer-output.json after every finding, so re-running /review
# resumes from the last completed report instead of restarting.
REVIEW_SECONDS_PER_REPORT = 1200
REVIEW_TIMEOUT_OVERHEAD = 600
REVIEW_MAX_SECONDS = 21600  # 6h ceiling; resume covers anything beyond it
REVIEW_MAX_LEGS = 4         # 4 x 6h covers any realistic batch


def review_timeout(reports: int) -> int:
    """Wall-clock budget for the review stage over *reports* reports."""
    if reports <= 0:
        return REVIEW_TIMEOUT_OVERHEAD
    return min(
        REVIEW_MAX_SECONDS,
        REVIEW_TIMEOUT_OVERHEAD + reports * REVIEW_SECONDS_PER_REPORT,
    )


def count_reviewable_reports(run_dir: Path) -> int:
    """How many reports run-reviewer.sh will actually review in *run_dir*.

    Mirrors the script's own collection loop: researcher-revision-* files are
    per-round artifacts, not reports; a researcher output contributes its
    .data.reports[] entries, or itself when .data is a flat object carrying a
    finding_id.

    This is NOT the same as the number of researcher-*.json files. A finding
    the researcher skipped as a duplicate still writes an output, but with
    reports: [] -- on run 2026-07-25T18-29-52, 37 files yielded only 29
    reports. Using the file count as the target makes a resume loop chase 8
    reports that can never appear.
    """
    total = 0
    for path in sorted(run_dir.glob("researcher-*.json")):
        if path.name.startswith("researcher-revision-"):
            continue
        try:
            data = json.loads(path.read_text()).get("data")
        except (json.JSONDecodeError, OSError, UnicodeDecodeError):
            continue
        if not isinstance(data, dict):
            continue
        reports = data.get("reports")
        if isinstance(reports, list):
            total += len(reports)
        elif data.get("finding_id"):
            total += 1
    return total


_TIMEOUT_MARKER = "timed out after"


def looks_timed_out(err: str) -> bool:
    """True if *err* came from a stage killed by its wall-clock timeout.

    Callers need to distinguish "ran out of clock while making progress"
    (resumable) from a hard failure like a rate limit (not resumable). Both
    the message producers below and this predicate use _TIMEOUT_MARKER so the
    two cannot drift apart.
    """
    return _TIMEOUT_MARKER in (err or "")


def next_leg_action(
    ok: bool,
    timed_out: bool,
    done_before: int,
    done_after: int,
    marker_exists: bool,
    legs_used: int,
    max_legs: int = RESEARCH_MAX_LEGS,
) -> tuple[str, str]:
    """Decide what to do after one leg of a resumable, per-item stage.

    Used by both research (findings) and review (reports): each writes a
    durable per-item artifact and skips completed items on resume, so a leg cut
    short by the clock can simply be continued.

    Returns (action, reason) where action is one of:
      "complete" -- the stage's completion marker is present, nothing left
      "continue" -- the leg made progress and was cut short; resume
      "stop"     -- hard error, no progress (hang), or leg budget exhausted
    """
    if marker_exists:
        return "complete", "all items have a terminal result"

    progressed = done_after > done_before

    # A non-timeout failure (rate limit, crash) will not fix itself by running
    # the same command again inside this loop.
    if not ok and not timed_out:
        return "stop", "stage failed with a hard error"

    if not progressed:
        return "stop", "leg produced no new researcher output"

    if legs_used >= max_legs:
        return "stop", f"leg budget exhausted after {legs_used} legs"

    return "continue", f"{done_after - done_before} findings done this leg, more remain"


# ---------------------------------------------------------------------------
# Error persistence
# ---------------------------------------------------------------------------

def _persist_stage_error(run_id: str, stage: str, returncode: int, stdout: str, stderr: str) -> Path | None:
    """Write the full stdout/stderr of a failed claude run to
    pipeline/runs/<run_id>/<stage>-error.log so failures can be diagnosed after
    the fact (the Discord message only carries a truncated tail). Best effort —
    returns the path on success, None on failure, never raises."""
    try:
        run_dir = RUNS_DIR / run_id
        if not run_dir.exists():
            return None
        log_path = run_dir / f"{stage}-error.log"
        ts = datetime.now(timezone.utc).isoformat()
        log_path.write_text(
            f"# {stage} failed for run {run_id}\n"
            f"# timestamp: {ts}\n"
            f"# exit code: {returncode}\n\n"
            f"===== STDERR =====\n{stderr or '(empty)'}\n\n"
            f"===== STDOUT =====\n{stdout or '(empty)'}\n"
        )
        return log_path
    except Exception as e:
        logger.debug("Could not persist %s error log for %s: %s", stage, run_id, e)
        return None


# ---------------------------------------------------------------------------
# Subprocess runners
# ---------------------------------------------------------------------------

def run_subprocess_checked(
    cmd: list[str],
    cwd: Path | None = None,
    capture: bool = True,
    timeout: int = 1800,
) -> tuple[bool, str]:
    """Run a subprocess and check its return code.

    Returns (ok, stderr_tail). On success, stderr_tail is empty. On failure,
    contains the last ~500 chars of stderr (or stdout if stderr is empty) for
    user-facing error messages.
    """
    try:
        result = _run_with_timeout(cmd, cwd, timeout)
    except (FileNotFoundError, OSError) as e:
        return False, f"Failed to launch {cmd[0]}: {e}"

    if result.timed_out:
        return False, f"{_TIMEOUT_MARKER} {timeout}s"

    if result.returncode != 0:
        tail = (result.stderr or result.stdout or "").strip()
        if len(tail) > 500:
            tail = "..." + tail[-500:]
        return False, f"exit code {result.returncode}: {tail or '(no output)'}"
    return True, ""


def run_claude_and_log_cost(
    cmd: list[str],
    run_id: str,
    stage: str,
    cwd: Path | None = None,
    timeout: int = 3600,
) -> tuple[bool, str, float]:
    """Run a `claude -p --output-format json ...` invocation, parse the
    structured result for `total_cost_usd`, and append the entry to
    pipeline/runs/<run_id>/cost.json.

    Returns (ok, error_tail, cost_usd). cost_usd is 0.0 if parsing fails.
    """
    try:
        result = _run_with_timeout(cmd, cwd, timeout)
    except (FileNotFoundError, OSError) as e:
        return False, f"Failed to launch {cmd[0]}: {e}", 0.0

    cost_usd = 0.0
    parsed = None
    if result.stdout:
        try:
            parsed = json.loads(result.stdout)
            cost_usd = float(parsed.get("total_cost_usd") or 0.0)
        except (json.JSONDecodeError, ValueError, TypeError) as e:
            logger.debug("Could not parse claude JSON output for cost (%s)", e)

    # Append cost entry regardless of success/failure so partial costs are logged
    _append_cost_entry(run_id, stage, cost_usd, parsed)

    if result.timed_out:
        log_path = _persist_stage_error(run_id, stage, -9, result.stdout, result.stderr)
        log_hint = f" Partial output saved to `{log_path.name}`." if log_path else ""
        return False, f"{stage} {_TIMEOUT_MARKER} {timeout}s and was killed.{log_hint}", cost_usd

    if result.returncode != 0:
        # Claude CLI sometimes exits non-zero even though the session itself
        # finished cleanly (terminal_reason == "completed", no permission
        # denials). Trust the parsed JSON over the exit code in that case.
        if (
            parsed
            and parsed.get("terminal_reason") == "completed"
            and not parsed.get("permission_denials")
            and not parsed.get("is_error")
        ):
            logger.warning(
                "claude exit=%d but terminal_reason=completed for stage=%s run_id=%s; treating as success",
                result.returncode, stage, run_id,
            )
            return True, "", cost_usd

        # Genuine failure: persist the full output for post-mortem and detect
        # the common usage/rate-limit case so the user gets an actionable message
        # instead of a raw JSON dump.
        log_path = _persist_stage_error(
            run_id, stage, result.returncode, result.stdout or "", result.stderr or ""
        )
        log_hint = f" Full output saved to `{log_path.name}`." if log_path else ""
        combined = (result.stderr or "") + "\n" + (result.stdout or "")

        if looks_rate_limited(combined, parsed):
            logger.warning(
                "claude hit a usage/rate limit during stage=%s run_id=%s (exit=%d)",
                stage, run_id, result.returncode,
            )
            # Embed the reset time in machine-readable ISO form so callers can
            # rate_limit_wait_seconds() on this message and auto-resume.
            reset = parse_rate_limit_reset(combined)
            reset_hint = f" Limit resets at {reset.isoformat()}." if reset else ""
            return (
                False,
                f"{_RATE_LIMIT_ERR_MARKER} during {stage} (exit {result.returncode})."
                f"{reset_hint} "
                f"Nothing was corrupted — re-run `/{stage}` once the limit resets."
                f"{log_hint}",
                cost_usd,
            )

        tail = (result.stderr or result.stdout or "").strip()
        if len(tail) > 500:
            tail = "..." + tail[-500:]
        return False, f"exit code {result.returncode}: {tail or '(no output)'}{log_hint}", cost_usd
    return True, "", cost_usd


# ---------------------------------------------------------------------------
# Cost logging
# ---------------------------------------------------------------------------

def _append_cost_entry(run_id: str, stage: str, cost_usd: float, parsed: dict | None) -> None:
    """Append a cost entry to pipeline/runs/<run_id>/cost.json. Best effort —
    never raises."""
    try:
        run_dir = RUNS_DIR / run_id
        if not run_dir.exists():
            return
        cost_path = run_dir / "cost.json"
        if cost_path.exists():
            try:
                data = json.loads(cost_path.read_text())
            except json.JSONDecodeError:
                data = {"run_id": run_id, "total_usd": 0.0, "stages": []}
        else:
            data = {"run_id": run_id, "total_usd": 0.0, "stages": []}

        entry = {
            "stage": stage,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "cost_usd": round(cost_usd, 6),
        }
        if parsed:
            entry["duration_ms"] = parsed.get("duration_ms")
            entry["num_turns"] = parsed.get("num_turns")
            usage = parsed.get("usage") or {}
            entry["input_tokens"] = usage.get("input_tokens")
            entry["output_tokens"] = usage.get("output_tokens")
            entry["cache_read_tokens"] = usage.get("cache_read_input_tokens")
            entry["cache_creation_tokens"] = usage.get("cache_creation_input_tokens")

        data.setdefault("stages", []).append(entry)
        data["total_usd"] = round(data.get("total_usd", 0.0) + cost_usd, 6)
        _atomic_write_json(cost_path, data)
    except Exception as e:
        logger.debug("Cost log write failed for %s: %s", run_id, e)
