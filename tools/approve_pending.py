#!/usr/bin/env python3
"""Approve or reject pending-subcategory proposals from the categorizer.

The categorizer routes reports whose subcategory is not in
pipeline/config/categories.json to pipeline/pending/<finding_id>-pending.{md,json}
for human confirmation. This is the (previously missing) consumer of that queue.

Real pending-JSON shape (inspected 2026-07-05):
  finding_id          str   e.g. "SCAN-20240606-022"
  original_path       str   e.g. "reports/privacy/litigation/file.md"
  proposed_topic      str   e.g. "privacy"
  proposed_subcategory str  e.g. "litigation"
  reason              str   human-readable explanation

categories.json shape:
  { "schema_version": "1.0", "topics": { "<topic>": { "subcategories": [...] } } }

Usage:
    python3 tools/approve_pending.py list
    python3 tools/approve_pending.py approve SCAN-20240606-022 [--subcategory other-name]
    python3 tools/approve_pending.py reject SCAN-20240606-022
"""
import argparse
import json
import shutil
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PENDING_DIR = PROJECT_ROOT / "pipeline" / "pending"
CATEGORIES_PATH = PROJECT_ROOT / "pipeline" / "config" / "categories.json"

sys.path.insert(0, str(PROJECT_ROOT))
from tools.update_reports_index import load_index, save_index, index_lock  # noqa: E402


def _pending_items() -> list[dict]:
    items = []
    for jf in sorted(PENDING_DIR.glob("*-pending.json")):
        try:
            data = json.loads(jf.read_text())
        except json.JSONDecodeError:
            print(f"WARN: unreadable {jf.name}", file=sys.stderr)
            continue
        data["_json_path"] = str(jf)
        items.append(data)
    return items


def cmd_list(args) -> int:
    items = _pending_items()
    if not items:
        print("No pending subcategory proposals.")
        return 0
    for it in items:
        fid = it.get("finding_id", "?")
        topic = it.get("proposed_topic", "?")
        sub = it.get("proposed_subcategory", "?")
        path = it.get("original_path", "")
        print(f"{fid:28s} {topic:15s} -> {sub:30s} {path}")
    print(f"\n{len(items)} pending. approve/reject with tools/approve_pending.py")
    return 0


def _find(finding_id: str) -> dict | None:
    for it in _pending_items():
        if it.get("finding_id") == finding_id:
            return it
    return None


def cmd_approve(args) -> int:
    it = _find(args.finding_id)
    if not it:
        print(f"ERROR: no pending item for {args.finding_id}", file=sys.stderr)
        return 2
    topic = it["proposed_topic"]
    sub = args.subcategory or it["proposed_subcategory"]
    report_path = PROJECT_ROOT / it["original_path"]

    # Add subcategory to categories.json if missing
    cats = json.loads(CATEGORIES_PATH.read_text())
    topic_entry = cats.setdefault("topics", {}).setdefault(topic, {})
    subs = topic_entry.setdefault("subcategories", [])
    if sub not in subs:
        subs.append(sub)
        subs.sort()
        CATEGORIES_PATH.write_text(json.dumps(cats, indent=2) + "\n")
        print(f"Added subcategory {topic}/{sub} to categories.json")

    # Move report to the subcategory directory
    dest_dir = PROJECT_ROOT / "reports" / topic / sub
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / report_path.name
    if report_path.exists() and report_path.resolve() != dest.resolve():
        shutil.move(str(report_path), str(dest))
        print(f"Moved {report_path.name} -> {dest.relative_to(PROJECT_ROOT)}")

    # Update index entries
    new_rel = str(dest.relative_to(PROJECT_ROOT))
    old_rel = it["original_path"]
    with index_lock():
        index = load_index()
        for key, entry in index.get("reports", {}).items():
            fids = entry.get("finding_ids") or []
            if args.finding_id in fids or entry.get("finding_id") == args.finding_id:
                entry["subcategory"] = sub
                entry["report_path"] = new_rel
            elif entry.get("report_path") == old_rel:
                entry["subcategory"] = sub
                entry["report_path"] = new_rel
        save_index(index)

    _cleanup(it)
    print(f"Approved {args.finding_id} -> {topic}/{sub}")
    return 0


def cmd_reject(args) -> int:
    it = _find(args.finding_id)
    if not it:
        print(f"ERROR: no pending item for {args.finding_id}", file=sys.stderr)
        return 2
    _cleanup(it)
    print(f"Rejected {args.finding_id}; report stays at {it.get('original_path', '')}")
    return 0


def _cleanup(it: dict) -> None:
    jf = Path(it["_json_path"])
    md = jf.with_name(jf.name.replace("-pending.json", "-pending.md"))
    for p in (jf, md):
        if p.exists():
            p.unlink()


def main() -> int:
    p = argparse.ArgumentParser(
        description="Approve or reject pending subcategory proposals."
    )
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list").set_defaults(func=cmd_list)
    ap = sub.add_parser("approve")
    ap.add_argument("finding_id")
    ap.add_argument("--subcategory", help="Override the proposed subcategory name")
    ap.set_defaults(func=cmd_approve)
    rj = sub.add_parser("reject")
    rj.add_argument("finding_id")
    rj.set_defaults(func=cmd_reject)
    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
