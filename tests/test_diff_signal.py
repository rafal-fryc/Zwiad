import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tools.diff_signal import classify


def test_bill_progress_beats_penalty_mention():
    finding = {
        "title": "SB 123 passed the Senate",
        "summary": "The bill passed the Senate; violations carry civil penalties up to $7,500.",
    }
    result = classify(finding, {"current_status": "introduced"})
    assert result["diff_signal"] == "status_change"
    assert result["status_after"] == "passed-first-chamber"


def test_pure_enforcement_still_penalty():
    finding = {
        "title": "AG announces $2M fine against DataCo",
        "summary": "Civil penalties imposed for privacy violations.",
    }
    result = classify(finding, {"current_status": ""})
    assert result["diff_signal"] == "new_penalty"


def test_signed_beats_everything():
    finding = {"title": "HB 5 signed into law", "summary": "Includes penalty provisions."}
    result = classify(finding, {"current_status": "passed-second-chamber"})
    assert result["diff_signal"] == "signed"


def test_restated_status_is_noise():
    finding = {"title": "SB 9 was signed into law last month", "summary": ""}
    result = classify(finding, {"current_status": "signed"})
    assert result["diff_signal"] == "noise"
