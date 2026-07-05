"""Shared stage-runner module for Zwiad pipeline agents.

Provides subprocess execution helpers with process-group timeouts, rate-limit
detection, error persistence, and cost logging. Used by both discord_bot.py
and run_pipeline.py.
"""

from __future__ import annotations

import json
import os
import signal
import subprocess
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

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
        return False, f"timed out after {timeout}s"

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
        return False, f"{stage} timed out after {timeout}s and was killed.{log_hint}", cost_usd

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
            return (
                False,
                f"hit an Anthropic usage/rate limit during {stage} (exit {result.returncode}). "
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
