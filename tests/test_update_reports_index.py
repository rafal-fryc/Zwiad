"""Tests for update_reports_index: index_lock reentrance and add_entry URL normalization."""

import json
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from tools.update_reports_index import (  # noqa: E402
    add_entry,
    index_lock,
    load_index,
    save_index,
)


# ---------------------------------------------------------------------------
# index_lock — sequential acquire/release
# ---------------------------------------------------------------------------

def test_index_lock_sequential_acquire(tmp_path, monkeypatch):
    """index_lock can be acquired, released, and acquired again sequentially."""
    import tools.update_reports_index as mod

    monkeypatch.setattr(mod, "LOCK_PATH", tmp_path / "index.json.lock")

    # First acquire + release
    with index_lock():
        pass  # released on exit

    # Second acquire + release — must not deadlock
    with index_lock():
        pass


# ---------------------------------------------------------------------------
# add_entry — normalizes stored legacy URLs on merge
# ---------------------------------------------------------------------------

def _make_index(key: str, raw_url: str) -> dict:
    """Build a minimal index with one existing entry containing a non-normalized URL."""
    return {
        "schema_version": "1.0",
        "last_updated": None,
        "reports": {
            key: {
                "topic_key": key,
                "topic_type": "other",
                "topic_key_confidence": "medium",
                "report_path": "reports/privacy/foo.md",
                "title": "Foo",
                "jurisdiction": "US",
                "category": "privacy",
                "subcategory": None,
                "source_urls": [raw_url],  # intentionally not normalized
                "first_reported": "2026-01-01",
                "last_updated": "2026-01-01",
                "current_status": None,
                "status_history": [],
                "finding_ids": [],
                "update_count": 0,
            }
        },
        "url_index": {raw_url: key},
    }


def test_add_entry_normalizes_existing_urls_on_merge():
    """add_entry normalizes stored legacy source_urls when merging into an existing entry."""
    from tools.url_norm import normalize_url

    key = "FTC-TEST-2026"
    raw_url = "HTTP://Example.com/page?utm_source=email&utm_medium=newsletter"
    expected_normalized = normalize_url(raw_url)
    assert expected_normalized is not None, "normalize_url must return something for this input"

    index = _make_index(key, raw_url)

    # Merge a new URL via add_entry
    new_url = "https://ftc.gov/news/press/2026"
    new_normalized = normalize_url(new_url)
    assert new_normalized is not None

    new_entry = {
        "topic_key": key,
        "report_path": "reports/privacy/foo.md",
        "category": "privacy",
        "source_urls": [new_url],
    }

    add_entry(index, new_entry)

    existing = index["reports"][key]
    stored_urls = existing["source_urls"]

    # All stored URLs must be normalized
    for u in stored_urls:
        assert u == normalize_url(u) or normalize_url(u) is None, (
            f"Stored URL {u!r} is not normalized"
        )

    # The old non-normalized form must no longer appear
    assert raw_url not in stored_urls, (
        f"Raw (un-normalized) URL {raw_url!r} still in source_urls after merge"
    )

    # The normalized form of the old URL must be present
    assert expected_normalized in stored_urls, (
        f"Expected normalized URL {expected_normalized!r} missing from source_urls"
    )

    # The new URL must be present (normalized)
    assert new_normalized in stored_urls, (
        f"New URL {new_normalized!r} missing from source_urls"
    )

    # url_index must map normalized URL to the key
    assert index["url_index"].get(expected_normalized) == key
    assert index["url_index"].get(new_normalized) == key
