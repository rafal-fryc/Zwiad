#!/usr/bin/env python3
"""Atomic reader/writer for reports/index.json.

Owned by the categorizer stage. Used as a CLI from agent markdown so the
sonnet-class categorizer agent does not need to implement JSON merge logic.

Usage:
    # Insert or refresh a report entry after filing
    python3 tools/update_reports_index.py add \\
        --entry-json '{"topic_key":"...", "topic_type":"...", ...}'

    # Append a status history entry (Phase 2 — used when report is updated)
    python3 tools/update_reports_index.py append-status \\
        --topic-key FTC-DISNEY-2026 \\
        --status signed \\
        --date 2026-05-01 \\
        --finding-id SCAN-20260501-012 \\
        --run-id 2026-05-01T09-00-00

    # Lookup (returns JSON of the entry, or empty if not found)
    python3 tools/update_reports_index.py lookup --topic-key FTC-DISNEY-2026

    # Lookup by URL
    python3 tools/update_reports_index.py lookup-url --url https://example.com/foo

    # Stats
    python3 tools/update_reports_index.py stats
"""

import argparse
import json
import os
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = PROJECT_ROOT / "reports" / "index.json"

# Single source of truth for URL normalization — see tools/url_norm.py
if __package__ in (None, ""):
    sys.path.insert(0, str(PROJECT_ROOT))
    from tools.url_norm import normalize_url  # noqa: E402
else:
    from .url_norm import normalize_url  # noqa: E402


def load_index(path: Path = INDEX_PATH) -> dict:
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return {
        "schema_version": "1.0",
        "last_updated": None,
        "reports": {},
        "url_index": {},
    }


def save_index(index: dict, path: Path = INDEX_PATH) -> None:
    index["last_updated"] = datetime.now(timezone.utc).isoformat()
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(
        prefix=".index-",
        suffix=".json.tmp",
        dir=str(path.parent),
    )
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(index, f, indent=2)
        os.replace(tmp_path, path)
    except Exception:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        raise


def add_entry(index: dict, entry: dict) -> dict:
    """Insert or refresh a report entry. If the key already exists,
    refreshes last_updated + merges source_urls + preserves first_reported + status_history."""
    key = entry["topic_key"]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    existing = index["reports"].get(key)
    if existing:
        existing.setdefault("source_urls", [])
        for url in entry.get("source_urls", []):
            normalized = normalize_url(url)
            if normalized and normalized not in existing["source_urls"]:
                existing["source_urls"].append(normalized)
                index["url_index"][normalized] = key
        existing["last_updated"] = entry.get("last_updated") or now
        for k in ("title", "jurisdiction", "category", "subcategory", "current_status", "report_path"):
            v = entry.get(k)
            if v:
                existing[k] = v
        finding_id = entry.get("finding_id")
        if finding_id:
            existing.setdefault("finding_ids", [])
            if finding_id not in existing["finding_ids"]:
                existing["finding_ids"].append(finding_id)
    else:
        source_urls = sorted({normalize_url(u) for u in entry.get("source_urls", []) if u})
        new_entry = {
            "topic_key": key,
            "topic_type": entry.get("topic_type", "other"),
            "topic_key_confidence": entry.get("topic_key_confidence", "medium"),
            "report_path": entry["report_path"],
            "title": entry.get("title", ""),
            "jurisdiction": entry.get("jurisdiction"),
            "category": entry["category"],
            "subcategory": entry.get("subcategory"),
            "source_urls": source_urls,
            "first_reported": entry.get("first_reported") or now,
            "last_updated": entry.get("last_updated") or now,
            "current_status": entry.get("current_status"),
            "status_history": entry.get("status_history", []),
            "finding_ids": [entry["finding_id"]] if entry.get("finding_id") else [],
            "update_count": 0,
        }
        index["reports"][key] = new_entry
        for url in source_urls:
            if url:
                index["url_index"][url] = key

    return index


def append_status(
    index: dict,
    key: str,
    status: str,
    date: str,
    finding_id: str | None = None,
    run_id: str | None = None,
    detail: str | None = None,
) -> dict:
    entry = index["reports"].get(key)
    if not entry:
        raise KeyError(f"topic_key not found: {key}")
    entry.setdefault("status_history", [])
    entry["status_history"].append({
        "date": date,
        "status": status,
        "finding_id": finding_id,
        "run_id": run_id,
        "detail": detail,
    })
    entry["current_status"] = status
    entry["last_updated"] = date
    entry["update_count"] = entry.get("update_count", 0) + 1
    if finding_id:
        entry.setdefault("finding_ids", [])
        if finding_id not in entry["finding_ids"]:
            entry["finding_ids"].append(finding_id)
    return index


def cmd_add(args) -> int:
    try:
        entry = json.loads(args.entry_json)
    except json.JSONDecodeError as e:
        print(f"ERROR: invalid entry JSON: {e}", file=sys.stderr)
        return 2
    if "topic_key" not in entry or "report_path" not in entry or "category" not in entry:
        print("ERROR: entry must contain topic_key, report_path, category", file=sys.stderr)
        return 2
    index = load_index()
    add_entry(index, entry)
    save_index(index)
    print(json.dumps({"ok": True, "topic_key": entry["topic_key"]}))
    return 0


def cmd_append_status(args) -> int:
    index = load_index()
    try:
        append_status(
            index,
            key=args.topic_key,
            status=args.status,
            date=args.date,
            finding_id=args.finding_id,
            run_id=args.run_id,
            detail=args.detail,
        )
    except KeyError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    save_index(index)
    print(json.dumps({"ok": True, "topic_key": args.topic_key}))
    return 0


def cmd_lookup(args) -> int:
    index = load_index()
    entry = index["reports"].get(args.topic_key)
    print(json.dumps(entry or {}, indent=2))
    return 0 if entry else 1


def cmd_lookup_url(args) -> int:
    index = load_index()
    normalized = normalize_url(args.url)
    topic_key = index.get("url_index", {}).get(normalized)
    if topic_key:
        entry = index["reports"].get(topic_key, {})
        print(json.dumps({"topic_key": topic_key, "entry": entry}, indent=2))
        return 0
    print(json.dumps({"topic_key": None}))
    return 1


def cmd_stats(args) -> int:
    index = load_index()
    reports = index.get("reports", {})
    by_type: dict[str, int] = {}
    by_confidence: dict[str, int] = {}
    for r in reports.values():
        by_type[r.get("topic_type", "other")] = by_type.get(r.get("topic_type", "other"), 0) + 1
        by_confidence[r.get("topic_key_confidence", "medium")] = (
            by_confidence.get(r.get("topic_key_confidence", "medium"), 0) + 1
        )
    print(json.dumps({
        "total_reports": len(reports),
        "total_urls": len(index.get("url_index", {})),
        "by_topic_type": by_type,
        "by_confidence": by_confidence,
    }, indent=2))
    return 0


def main() -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)

    add = sub.add_parser("add", help="Insert or refresh a report entry")
    add.add_argument("--entry-json", required=True)
    add.set_defaults(func=cmd_add)

    app = sub.add_parser("append-status", help="Append a status_history entry")
    app.add_argument("--topic-key", required=True)
    app.add_argument("--status", required=True)
    app.add_argument("--date", required=True)
    app.add_argument("--finding-id")
    app.add_argument("--run-id")
    app.add_argument("--detail")
    app.set_defaults(func=cmd_append_status)

    lk = sub.add_parser("lookup", help="Look up an entry by topic_key")
    lk.add_argument("--topic-key", required=True)
    lk.set_defaults(func=cmd_lookup)

    lku = sub.add_parser("lookup-url", help="Look up an entry by URL")
    lku.add_argument("--url", required=True)
    lku.set_defaults(func=cmd_lookup_url)

    st = sub.add_parser("stats", help="Print index statistics")
    st.set_defaults(func=cmd_stats)

    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
