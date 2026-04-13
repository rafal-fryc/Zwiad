#!/usr/bin/env python3
"""Backfill reports/index.json from existing reports in reports/.

Walks reports/**/*.md, parses frontmatter + first H1 + URLs, assigns topic_keys
via tools/topic_keys.py, writes to reports/index.json.backfill (NOT the live
file). Also emits backfill-report.json listing low-confidence entries for human
review before promotion.

Idempotent — safe to run multiple times; produces identical output for the same
input set.

Usage:
    python3 tools/backfill_reports_index.py [--promote]

    --promote    After writing .backfill file, rename it to reports/index.json.
                 Only use if you've reviewed backfill-report.json and are happy
                 with the keys.

Output files:
    reports/index.json.backfill    Draft index, safe to discard
    reports/backfill-report.json   Human-review summary
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = PROJECT_ROOT / "reports"
BACKFILL_PATH = REPORTS_DIR / "index.json.backfill"
LIVE_INDEX_PATH = REPORTS_DIR / "index.json"
REPORT_PATH = REPORTS_DIR / "backfill-report.json"

# Sibling-module imports. Support both direct invocation (`python3 tools/backfill_reports_index.py`)
# and package-style invocation (`python3 -m tools.backfill_reports_index`).
if __package__ in (None, ""):
    sys.path.insert(0, str(PROJECT_ROOT))
    from tools.topic_keys import topic_key, load_rules  # noqa: E402
    from tools.url_norm import normalize_url  # noqa: E402
else:
    from .topic_keys import topic_key, load_rules  # noqa: E402
    from .url_norm import normalize_url  # noqa: E402


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
URL_RE = re.compile(r"https?://[^\s\)\]>\"'<]+")
H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)


def parse_frontmatter(content: str) -> dict:
    """Minimal YAML frontmatter parser — handles key: \"value\" pairs only."""
    m = FRONTMATTER_RE.match(content)
    if not m:
        return {}
    meta: dict = {}
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        k = k.strip()
        v = v.strip()
        if v.startswith('"') and v.endswith('"'):
            v = v[1:-1]
        elif v.startswith("'") and v.endswith("'"):
            v = v[1:-1]
        meta[k] = v
    return meta


def extract_first_h1(content: str) -> str:
    m = H1_RE.search(content)
    if m:
        return m.group(1).strip()
    return ""


def extract_urls(content: str) -> list[str]:
    urls = set()
    for m in URL_RE.finditer(content):
        raw = m.group(0).rstrip(".,);:]")
        normalized = normalize_url(raw)
        if normalized:
            urls.add(normalized)
    return sorted(urls)


def derive_subcategory_from_path(report_path: Path) -> str | None:
    """reports/privacy/enforcement-actions/foo.md -> enforcement-actions.
    reports/privacy/foo.md -> None."""
    try:
        rel = report_path.relative_to(REPORTS_DIR)
    except ValueError:
        return None
    parts = rel.parts
    if len(parts) >= 3:
        return parts[1]
    return None


def build_finding_from_report(report_path: Path, content: str, meta: dict) -> dict:
    """Construct a finding-like dict that topic_keys.py can consume."""
    title = extract_first_h1(content) or meta.get("finding_id", "")
    urls = extract_urls(content)
    return {
        "title": title,
        "summary": content[:2000],
        "source": meta.get("source", ""),
        "source_url": urls[0] if urls else "",
        "jurisdiction": meta.get("jurisdiction", ""),
        "category": meta.get("category", ""),
        "development_type": meta.get("development_type", ""),
        "date": meta.get("date", ""),
    }


def infer_category(meta: dict, report_path: Path) -> str:
    cat = meta.get("category", "")
    if cat:
        return cat
    try:
        rel = report_path.relative_to(REPORTS_DIR)
        if rel.parts:
            return rel.parts[0]
    except ValueError:
        pass
    return "privacy"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--promote",
        action="store_true",
        help="After writing .backfill file, promote it to the live reports/index.json",
    )
    args = p.parse_args()

    if not REPORTS_DIR.exists():
        print(f"No reports directory at {REPORTS_DIR}; writing empty index.")
        empty_index = {
            "schema_version": "1.0",
            "last_updated": datetime.now(timezone.utc).isoformat(),
            "reports": {},
            "url_index": {},
        }
        BACKFILL_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(BACKFILL_PATH, "w") as f:
            json.dump(empty_index, f, indent=2)
        print(f"  Wrote {BACKFILL_PATH}")
        return 0

    rules = load_rules()

    index: dict = {
        "schema_version": "1.0",
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "reports": {},
        "url_index": {},
    }

    report_files = sorted(REPORTS_DIR.rglob("*.md"))
    audit: list[dict] = []
    duplicates: list[dict] = []
    low_confidence: list[dict] = []

    for report_path in report_files:
        if report_path.is_symlink():
            continue

        content = report_path.read_text(encoding="utf-8", errors="replace")
        meta = parse_frontmatter(content)
        finding = build_finding_from_report(report_path, content, meta)

        key, confidence, topic_type = topic_key(finding, rules)

        category = infer_category(meta, report_path)
        subcategory = derive_subcategory_from_path(report_path)
        source_urls = extract_urls(content)
        rel_path = str(report_path.relative_to(PROJECT_ROOT))
        date = meta.get("date") or ""

        entry = {
            "topic_key": key,
            "topic_type": topic_type,
            "topic_key_confidence": confidence,
            "report_path": rel_path,
            "title": finding["title"],
            "jurisdiction": meta.get("jurisdiction"),
            "category": category,
            "subcategory": subcategory,
            "source_urls": source_urls,
            "first_reported": date or datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "last_updated": date or datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "current_status": None,
            "status_history": [],
            "finding_ids": [meta["finding_id"]] if meta.get("finding_id") else [],
            "update_count": 0,
        }

        if key in index["reports"]:
            duplicates.append({
                "topic_key": key,
                "existing_path": index["reports"][key]["report_path"],
                "conflicting_path": rel_path,
                "action": "keep_first",
            })
        else:
            index["reports"][key] = entry
            for url in source_urls:
                if url and url not in index["url_index"]:
                    index["url_index"][url] = key

        audit.append({
            "report_path": rel_path,
            "topic_key": key,
            "topic_type": topic_type,
            "confidence": confidence,
        })

        if confidence == "low":
            low_confidence.append({
                "report_path": rel_path,
                "topic_key": key,
                "title": finding["title"][:100],
                "reason": "Fallback hash key used — no rule matched",
            })

    BACKFILL_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(BACKFILL_PATH, "w") as f:
        json.dump(index, f, indent=2)

    report = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_reports_scanned": len(report_files),
        "total_indexed": len(index["reports"]),
        "total_urls_indexed": len(index["url_index"]),
        "duplicates": duplicates,
        "low_confidence_entries": low_confidence,
        "all_entries_audit": audit,
    }
    with open(REPORT_PATH, "w") as f:
        json.dump(report, f, indent=2)

    print(f"Scanned: {len(report_files)} reports")
    print(f"Indexed: {len(index['reports'])} unique topic_keys")
    print(f"URLs indexed: {len(index['url_index'])}")
    if duplicates:
        print(f"  Duplicate keys (kept first): {len(duplicates)}")
    if low_confidence:
        print(f"  Low-confidence keys: {len(low_confidence)} (review required)")
    print(f"\nBackfill written: {BACKFILL_PATH}")
    print(f"Review report:    {REPORT_PATH}")

    if args.promote:
        if low_confidence and not args.promote:
            print("\nRefusing to auto-promote with low-confidence entries present.")
            return 1
        import shutil
        shutil.copy2(BACKFILL_PATH, LIVE_INDEX_PATH)
        print(f"\nPromoted to {LIVE_INDEX_PATH}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
