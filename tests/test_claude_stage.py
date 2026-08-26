import subprocess
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tools.claude_stage import (
    looks_rate_limited,
    _run_with_timeout,
    run_subprocess_checked,
    research_timeout,
    next_leg_action,
    looks_timed_out,
    review_timeout,
    count_reviewable_reports,
    RESEARCH_LEG_MAX_SECONDS,
    RESEARCH_MAX_LEGS,
    REVIEW_MAX_SECONDS,
)


def test_rate_limit_detection_positive():
    assert looks_rate_limited("Error: Claude usage limit reached", None)
    assert looks_rate_limited("", {"result": "429 too many requests"})


def test_rate_limit_detection_negative():
    assert not looks_rate_limited("normal output", {"result": "done"})


def test_timeout_kills_process_tree():
    # A shell that spawns a child sleeping forever; must return within ~2s
    proc = _run_with_timeout(["bash", "-c", "sleep 300"], cwd=None, timeout=1)
    assert proc.timed_out


def test_run_subprocess_checked_timeout_reports_failure():
    ok, err = run_subprocess_checked(["bash", "-c", "sleep 300"], timeout=1)
    assert not ok
    assert "timed out" in err


def test_looks_timed_out_recognises_real_timeout_message():
    # Guards against the predicate drifting from the message producers.
    _, err = run_subprocess_checked(["bash", "-c", "sleep 300"], timeout=1)
    assert looks_timed_out(err)


def test_looks_timed_out_rejects_other_failures():
    assert not looks_timed_out("hit an Anthropic usage/rate limit during research")
    assert not looks_timed_out("exit code 1: boom")
    assert not looks_timed_out("")
    assert not looks_timed_out(None)


# ---------------------------------------------------------------------------
# Research timeout sizing
#
# Regression: run 2026-07-25T18-29-52 had 37 approved findings and was killed
# (SIGKILL, exit -9) at exactly 5400s with 20 findings done and no slowdown.
# The timeout was a fixed constant while the work it bounds scales with the
# finding count.
# ---------------------------------------------------------------------------

def test_research_timeout_scales_with_finding_count():
    assert research_timeout(10) > research_timeout(1)
    assert research_timeout(20) > research_timeout(10)


def test_research_timeout_covers_worst_observed_per_finding_rate():
    # Slowest historical run measured ~354s/finding; a leg sized for N findings
    # must budget at least that much per finding, or it gets killed mid-stride.
    for n in (1, 5, 10):
        assert research_timeout(n) >= n * 354


def test_research_timeout_is_capped_so_a_hang_is_still_caught():
    # A genuine hang must not be allowed to burn hours.
    assert research_timeout(1000) == RESEARCH_LEG_MAX_SECONDS
    assert research_timeout(37) <= RESEARCH_LEG_MAX_SECONDS


def test_research_timeout_handles_zero_and_negative():
    assert research_timeout(0) > 0
    assert research_timeout(-1) > 0


# ---------------------------------------------------------------------------
# Research leg continuation logic
# ---------------------------------------------------------------------------

def test_marker_present_means_complete():
    action, _ = next_leg_action(
        ok=True, timed_out=False, done_before=37, done_after=37,
        marker_exists=True, legs_used=1,
    )
    assert action == "complete"


def test_timeout_with_progress_continues():
    # The exact 2026-07-25 failure: killed at 5400s having done 20 of 37.
    action, reason = next_leg_action(
        ok=False, timed_out=True, done_before=0, done_after=20,
        marker_exists=False, legs_used=1,
    )
    assert action == "continue", reason


def test_timeout_without_progress_stops():
    # Nothing produced in a full leg is a genuine hang, not a capacity problem.
    action, _ = next_leg_action(
        ok=False, timed_out=True, done_before=20, done_after=20,
        marker_exists=False, legs_used=2,
    )
    assert action == "stop"


def test_hard_error_stops_immediately_even_with_progress():
    # e.g. rate limit — retrying just burns another leg.
    action, _ = next_leg_action(
        ok=False, timed_out=False, done_before=0, done_after=5,
        marker_exists=False, legs_used=1,
    )
    assert action == "stop"


def test_clean_exit_without_marker_continues_if_progressing():
    # Orchestrator hit --max-turns but did useful work; resume is idempotent.
    action, _ = next_leg_action(
        ok=True, timed_out=False, done_before=0, done_after=12,
        marker_exists=False, legs_used=1,
    )
    assert action == "continue"


def test_leg_budget_is_bounded():
    action, _ = next_leg_action(
        ok=False, timed_out=True, done_before=0, done_after=20,
        marker_exists=False, legs_used=RESEARCH_MAX_LEGS,
    )
    assert action == "stop"


# ---------------------------------------------------------------------------
# Review timeout sizing
#
# Regression: the same run's review stage got a fixed 10800s for 37 reports
# while measuring 17.2 min/report -- it could only ever reach ~11 of them.
# ---------------------------------------------------------------------------

def test_review_timeout_scales_with_report_count():
    assert review_timeout(20) > review_timeout(5)


def test_review_timeout_covers_worst_observed_per_report_rate():
    # 17.2 min/report measured; the budget must not undercut it.
    for n in (1, 5, 10):
        assert review_timeout(n) >= n * 17.2 * 60


def test_review_timeout_beats_the_fixed_value_that_failed():
    # 37 reports previously got 10800s and died at ~11.
    assert review_timeout(37) > 10800


def test_review_timeout_is_capped():
    assert review_timeout(10_000) == REVIEW_MAX_SECONDS


def test_review_timeout_handles_zero():
    assert review_timeout(0) > 0


# ---------------------------------------------------------------------------
# Reviewable report counting
#
# Regression: 37 researcher-*.json files on run 2026-07-25T18-29-52 yielded
# only 29 reviewable reports -- 8 were skipped duplicates with reports: [].
# A resume loop targeting the file count chases reports that never appear.
# ---------------------------------------------------------------------------

def _mk_run(tmp_path, files: dict):
    import json as _json
    for name, payload in files.items():
        (tmp_path / name).write_text(_json.dumps(payload))
    return tmp_path


def test_count_reports_ignores_skipped_duplicates(tmp_path):
    _mk_run(tmp_path, {
        "researcher-SCAN-1.json": {"data": {"reports": [{"finding_id": "SCAN-1"}]}},
        "researcher-SCAN-2.json": {"data": {"reports": [], "skipped_duplicate": {"x": 1}}},
    })
    assert count_reviewable_reports(tmp_path) == 1


def test_count_reports_ignores_revision_artifacts(tmp_path):
    _mk_run(tmp_path, {
        "researcher-SCAN-1.json": {"data": {"reports": [{"finding_id": "SCAN-1"}]}},
        "researcher-revision-r1-SCAN-1.json": {"data": {"reports": [{"finding_id": "SCAN-1"}]}},
    })
    assert count_reviewable_reports(tmp_path) == 1


def test_count_reports_handles_flat_data_object(tmp_path):
    _mk_run(tmp_path, {
        "researcher-SCAN-1.json": {"data": {"finding_id": "SCAN-1", "report_path": "p.md"}},
    })
    assert count_reviewable_reports(tmp_path) == 1


def test_count_reports_survives_corrupt_files(tmp_path):
    _mk_run(tmp_path, {
        "researcher-SCAN-1.json": {"data": {"reports": [{"finding_id": "SCAN-1"}]}},
    })
    (tmp_path / "researcher-SCAN-bad.json").write_text("{not json")
    assert count_reviewable_reports(tmp_path) == 1


def test_count_reports_empty_dir(tmp_path):
    assert count_reviewable_reports(tmp_path) == 0


def test_full_37_finding_run_completes_within_leg_budget():
    """End-to-end sizing check for the run that failed: simulate legs at the
    worst observed rate and confirm the loop drains 37 findings."""
    total, done, legs = 37, 0, 0
    while done < total and legs < RESEARCH_MAX_LEGS:
        budget = research_timeout(total - done)
        done_before = done
        done = min(total, done + budget // 354)  # worst-case per-finding rate
        legs += 1
        marker = done >= total
        action, _ = next_leg_action(
            ok=marker, timed_out=not marker, done_before=done_before,
            done_after=done, marker_exists=marker, legs_used=legs,
        )
        if action != "continue":
            break
    assert done == total, f"only {done}/{total} findings after {legs} legs"
