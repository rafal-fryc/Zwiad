#!/usr/bin/env python3
"""Append an 'Update {date}' section to an existing report markdown file.

Phase 2 of the Zwiad pipeline: when the scanner encounters a finding whose
topic_key matches an already-indexed report AND the diff_signal classifier
marks it as a real update (not noise), this module performs the atomic
append.

Design: strict APPEND-ONLY. This never rewrites prior sections — it only:
  1. Rewrites two lines in the frontmatter: `last_updated` and appends one
     entry to `status_history`. Leaves all other frontmatter keys untouched.
  2. Appends the update block at the end of the body.
  3. Writes atomically via tempfile + rename in the same directory.
  4. After the markdown write succeeds, calls `update_reports_index.append_status`
     in-process so the index stays in sync.

CLI:
    python3 tools/report_updater.py append \\
        --report-path reports/privacy/alabama-hb351-2026-04-07.md \\
        --update-markdown "Governor Ivey signed HB 351 on May 1, 2026..." \\
        --status signed \\
        --date 2026-05-01 \\
        --finding-id SCAN-20260501-042 \\
        --run-id 2026-05-01T09-00-00 \\
        [--status-before introduced] \\
        [--source-url https://example.com/news] \\
        [--topic-key AL-HB-351-2026]

Library:
    from tools.report_updater import append_update
    ok, err = append_update(
        report_path=Path("reports/privacy/alabama-hb351-2026-04-07.md"),
        update_markdown="Governor Ivey signed HB 351 on May 1, 2026...",
        status="signed",
        date="2026-05-01",
        finding_id="SCAN-20260501-042",
        run_id="2026-05-01T09-00-00",
    )
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

PROJECT_ROOT = Path(__file__).resolve().parent.parent

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def _split_frontmatter(text: str) -> tuple[str | None, str]:
    """Return (frontmatter_text_including_delimiters, body). If no frontmatter, (None, text)."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    return m.group(0), text[m.end():]


def _rewrite_frontmatter(
    frontmatter_block: str,
    last_updated: str,
    status_entry: dict[str, str],
) -> str:
    """Update `last_updated` and append one `status_history` entry.

    Line-based rewrite — never touches keys we don't own. Keeps the delimiter
    lines (`---`) intact. If `last_updated` is absent, inserts it before the
    closing delimiter. If `status_history` is absent, initializes it.
    """
    lines = frontmatter_block.splitlines()
    # Find opening + closing '---' delimiter indices
    assert lines[0] == "---", f"expected opening ---, got {lines[0]!r}"
    closing_idx = None
    for i in range(1, len(lines)):
        if lines[i] == "---":
            closing_idx = i
            break
    if closing_idx is None:
        # Malformed frontmatter — return as-is; caller will skip frontmatter update
        return frontmatter_block

    # Work with the interior (between the --- delimiters)
    interior = lines[1:closing_idx]

    # 1. Update or insert `last_updated`
    last_updated_line = f'last_updated: "{last_updated}"'
    found_last_updated = False
    for i, ln in enumerate(interior):
        if re.match(r"^last_updated\s*:", ln):
            interior[i] = last_updated_line
            found_last_updated = True
            break
    if not found_last_updated:
        interior.append(last_updated_line)

    # 2. Append status_history entry
    # Format: status_history: [...]  (flow-style list of flow-mapping entries)
    # Or:    status_history:\n  - {...}  (block-style)
    # We'll use block-style for readability + reserve flow for the inline entry dict.
    status_entry_flow = (
        "{"
        + ", ".join(f'{k}: "{v}"' for k, v in status_entry.items() if v)
        + "}"
    )

    status_history_idx = None
    for i, ln in enumerate(interior):
        if re.match(r"^status_history\s*:", ln):
            status_history_idx = i
            break

    if status_history_idx is None:
        # Create fresh status_history block
        interior.append("status_history:")
        interior.append(f"  - {status_entry_flow}")
    else:
        header = interior[status_history_idx]
        rest = header.split(":", 1)[1].strip() if ":" in header else ""
        if rest == "[]" or rest == "":
            # Convert to block form and append one entry
            interior[status_history_idx] = "status_history:"
            # Insert the new entry right after the header
            interior.insert(status_history_idx + 1, f"  - {status_entry_flow}")
        elif rest.startswith("["):
            # Inline flow list — append inside the brackets
            # Parse out the interior between [ and ]
            m = re.match(r"^\[(.*)\]\s*$", rest)
            if m:
                items_str = m.group(1).strip()
                sep = ", " if items_str else ""
                interior[status_history_idx] = (
                    f"status_history: [{items_str}{sep}{status_entry_flow}]"
                )
            else:
                # Can't parse; fall back to appending as block entry below existing
                interior.insert(status_history_idx + 1, f"  - {status_entry_flow}")
        else:
            # Already block-style (header:"status_history:" with entries following at col 2).
            # Append after the existing block. Find last '  - ' line.
            insert_at = status_history_idx + 1
            while insert_at < len(interior) and interior[insert_at].startswith("  "):
                insert_at += 1
            interior.insert(insert_at, f"  - {status_entry_flow}")

    return "\n".join(["---"] + interior + ["---", ""])


def _append_update_block(
    body: str,
    update_markdown: str,
    status_before: str,
    status_after: str,
    date: str,
    finding_id: str,
    run_id: str,
    source_url: Optional[str] = None,
) -> str:
    """Append the strict update block to the end of the body."""
    parts = [
        "",
        f"## Update {date}",
        "",
        f"**Change:** {status_before or '(unspecified)'} → {status_after}",
    ]
    if source_url:
        parts.append(f"**Source:** {source_url}")
    parts.append(f"**Summary:** {update_markdown}")
    parts.append(f"**Finding ID:** {finding_id}")
    parts.append(f"**Run ID:** {run_id}")
    parts.append("")
    appendix = "\n".join(parts)

    # Normalize trailing whitespace on body so we don't stack blank lines
    body_trimmed = body.rstrip() + "\n"
    return body_trimmed + appendix


def append_update(
    report_path: Path,
    update_markdown: str,
    status: str,
    date: str,
    finding_id: str,
    run_id: str,
    status_before: str = "",
    source_url: Optional[str] = None,
    topic_key: Optional[str] = None,
    update_index: bool = True,
) -> tuple[bool, str]:
    """Perform the atomic append. Returns (ok, err_message)."""
    if not report_path.exists():
        return False, f"report not found: {report_path}"

    original = report_path.read_text(encoding="utf-8")
    fm_block, body = _split_frontmatter(original)

    if fm_block is not None:
        try:
            new_fm = _rewrite_frontmatter(
                fm_block,
                last_updated=date,
                status_entry={
                    "date": date,
                    "status": status,
                    "finding_id": finding_id,
                    "run_id": run_id,
                },
            )
        except Exception as e:
            return False, f"frontmatter rewrite failed: {e}"
    else:
        # No frontmatter — leave the body unchanged on that front
        new_fm = ""

    new_body = _append_update_block(
        body,
        update_markdown=update_markdown,
        status_before=status_before,
        status_after=status,
        date=date,
        finding_id=finding_id,
        run_id=run_id,
        source_url=source_url,
    )

    new_content = (new_fm if new_fm else "") + new_body

    # Atomic write in same directory
    target_dir = report_path.parent
    target_dir.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(prefix=".ru-", suffix=".md.tmp", dir=str(target_dir))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(new_content)
        os.replace(tmp_path, report_path)
    except Exception as e:
        try:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
        except OSError:
            pass
        return False, f"write failed: {e}"

    # Update the reports index in-sync (best-effort; failure here is reported but
    # the markdown append already succeeded)
    if update_index and topic_key:
        try:
            # Support both package and direct-script invocation
            if __package__ in (None, ""):
                sys.path.insert(0, str(PROJECT_ROOT))
                from tools.update_reports_index import load_index, save_index, append_status
            else:
                from .update_reports_index import load_index, save_index, append_status  # type: ignore
            index = load_index()
            append_status(
                index,
                key=topic_key,
                status=status,
                date=date,
                finding_id=finding_id,
                run_id=run_id,
            )
            save_index(index)
        except KeyError as e:
            return True, f"markdown appended, but index append_status failed: {e}"
        except Exception as e:
            return True, f"markdown appended, but index update failed: {e}"

    return True, ""


def main() -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)

    ap = sub.add_parser("append", help="Append an update section to an existing report")
    ap.add_argument("--report-path", required=True)
    ap.add_argument("--update-markdown", required=True)
    ap.add_argument("--status", required=True, help="New status after the update")
    ap.add_argument("--date", required=True, help="YYYY-MM-DD")
    ap.add_argument("--finding-id", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--status-before", default="")
    ap.add_argument("--source-url", default=None)
    ap.add_argument("--topic-key", default=None,
                    help="If set, also calls update_reports_index.append_status to sync the index")
    ap.add_argument("--no-index-update", action="store_true",
                    help="Skip the in-process index update (use for testing)")

    args = p.parse_args()

    if args.cmd == "append":
        ok, err = append_update(
            report_path=Path(args.report_path),
            update_markdown=args.update_markdown,
            status=args.status,
            date=args.date,
            finding_id=args.finding_id,
            run_id=args.run_id,
            status_before=args.status_before,
            source_url=args.source_url,
            topic_key=args.topic_key,
            update_index=not args.no_index_update,
        )
        if ok:
            print(json.dumps({"ok": True, "warning": err or None}))
            return 0
        else:
            print(json.dumps({"ok": False, "error": err}), file=sys.stderr)
            return 1
    return 2


if __name__ == "__main__":
    sys.exit(main())
