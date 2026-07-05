import subprocess
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tools.claude_stage import looks_rate_limited, _run_with_timeout, run_subprocess_checked


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
