"""Tests for the rate-limit auto-wait-and-resume helpers in tools/claude_stage.py."""
from datetime import datetime, timezone
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tools.claude_stage import (
    RATE_LIMIT_BACKOFF_SECONDS,
    RATE_LIMIT_MAX_WAITS,
    RATE_LIMIT_RESET_BUFFER_SECONDS,
    looks_rate_limited_err,
    parse_rate_limit_reset,
    rate_limit_wait_seconds,
)

# 9:00am EDT / 13:00 UTC on a summer day
NOW = datetime(2026, 6, 29, 13, 0, tzinfo=timezone.utc)


def test_parse_cli_human_form():
    # The exact phrasing the claude CLI emitted on run 2026-06-28T19-28-09
    r = parse_rate_limit_reset(
        "You've hit your session limit · resets 12:30pm (America/New_York)", NOW
    )
    assert r is not None
    assert (r.hour, r.minute) == (12, 30)
    assert r.astimezone(timezone.utc).hour == 16  # 12:30 EDT == 16:30 UTC


def test_parse_iso_form_with_trailing_period():
    r = parse_rate_limit_reset("Limit resets at 2026-06-29T12:30:00-04:00.", NOW)
    assert r is not None
    assert r.isoformat() == "2026-06-29T12:30:00-04:00"


def test_parse_requires_minutes_or_ampm():
    # A bare number after "resets" must not be mistaken for a time
    assert parse_rate_limit_reset("resets 42 widgets", NOW) is None


def test_parse_unknown_timezone_returns_none():
    assert parse_rate_limit_reset("resets 12:30pm (Not/AZone)", NOW) is None


def test_wait_until_reset_plus_buffer():
    w = rate_limit_wait_seconds("resets 12:30pm (America/New_York)", 0, NOW)
    assert w == int(3.5 * 3600) + RATE_LIMIT_RESET_BUFFER_SECONDS


def test_wait_gives_up_when_reset_too_far_out():
    # 8:00am EDT is already past at NOW, so the parse rolls to tomorrow (>6h)
    assert rate_limit_wait_seconds("resets 8:00am (America/New_York)", 0, NOW) is None


def test_backoff_schedule_when_no_reset_parses():
    waits = [rate_limit_wait_seconds("no reset info here", i, NOW) for i in range(5)]
    assert waits == list(RATE_LIMIT_BACKOFF_SECONDS) + [None, None]


def test_wait_budget_exhausted():
    assert (
        rate_limit_wait_seconds("resets 12:30pm (America/New_York)", RATE_LIMIT_MAX_WAITS, NOW)
        is None
    )


def test_error_marker_roundtrip():
    # The message run_claude_and_log_cost emits must satisfy the predicate
    # callers use to decide whether to wait.
    msg = "hit an Anthropic usage/rate limit during research (exit 1). Limit resets at 2026-06-29T12:30:00-04:00."
    assert looks_rate_limited_err(msg)
    assert parse_rate_limit_reset(msg, NOW) is not None
    assert not looks_rate_limited_err("exit code 1: something else broke")
