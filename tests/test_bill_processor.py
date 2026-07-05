"""Unit tests for bill_processor pure-logic helpers."""
import sys
import os

# Ensure project root is on sys.path for direct module import
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.bill_processor import should_append_history


class TestShouldAppendHistory:
    def test_empty_history_returns_true(self):
        new_hist = {"date": "2026-01-01", "status": "introduced", "detail": ""}
        assert should_append_history([], new_hist) is True

    def test_identical_last_entry_returns_false(self):
        hist = [{"date": "2026-01-01", "status": "introduced", "detail": "", "source_run_id": "r1"}]
        new_hist = {"date": "2026-01-01", "status": "introduced", "detail": "", "source_run_id": "r2"}
        assert should_append_history(hist, new_hist) is False

    def test_different_status_returns_true(self):
        hist = [{"date": "2026-01-01", "status": "introduced", "detail": ""}]
        new_hist = {"date": "2026-01-15", "status": "passed", "detail": ""}
        assert should_append_history(hist, new_hist) is True
