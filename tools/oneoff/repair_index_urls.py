#!/usr/bin/env python3
"""One-time repair: re-normalize every URL in reports/index.json.

Fixes legacy keys written before normalize_url handled scheme/www/param-order
(review 2026-07-05, issues: malformed &-joined URLs, http:// keys).
Idempotent; prints a summary. Run from the project root:
    python3 tools/oneoff/repair_index_urls.py
"""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
from tools.url_norm import normalize_url
from tools.update_reports_index import load_index, save_index


def main() -> int:
    index = load_index()
    changed = 0
    new_url_index: dict[str, str] = {}
    for key, entry in index.get("reports", {}).items():
        urls = entry.get("source_urls", []) or []
        normalized: list[str] = []
        for u in urls:
            n = normalize_url(u)
            if n and n not in normalized:
                normalized.append(n)
            if n != u:
                changed += 1
        entry["source_urls"] = normalized
        for n in normalized:
            new_url_index.setdefault(n, key)
    old_count = len(index.get("url_index", {}))
    index["url_index"] = new_url_index
    save_index(index)
    print(f"URLs rewritten: {changed}; url_index {old_count} -> {len(new_url_index)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
