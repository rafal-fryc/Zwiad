#!/usr/bin/env python3
"""Append a new source bullet to an existing report's ## Sources section.

Usage:
  append-source.py <target-report-path> <title> <url> [gist]

- If the report has no "## Sources" section, creates one at the end.
- Updates `last_updated:` in the YAML frontmatter to today.
- Idempotent: if the same URL already appears under Sources, it's not added again.
"""
from __future__ import annotations

import datetime
import re
import sys
from pathlib import Path


FM_RE = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
SOURCES_H2_RE = re.compile(r"^##\s+Sources\s*$", re.MULTILINE | re.IGNORECASE)


def ensure_last_updated(fm_block: str, today: str) -> str:
    lines = fm_block.splitlines()
    found = False
    new_lines = []
    for ln in lines:
        if ":" in ln:
            k = ln.split(":", 1)[0].strip()
            if k == "last_updated":
                new_lines.append(f"last_updated: {today}")
                found = True
                continue
        new_lines.append(ln)
    if not found:
        new_lines.append(f"last_updated: {today}")
    return "\n".join(new_lines)


def main():
    if len(sys.argv) < 4:
        print("Usage: append-source.py <path> <title> <url> [gist]", file=sys.stderr)
        sys.exit(2)
    path = Path(sys.argv[1])
    title = sys.argv[2]
    url = sys.argv[3]
    gist = sys.argv[4] if len(sys.argv) >= 5 else ""

    if not path.exists():
        print(f"Error: {path} not found", file=sys.stderr)
        sys.exit(2)

    text = path.read_text()
    today = datetime.date.today().isoformat()

    # Update frontmatter last_updated
    m = FM_RE.match(text)
    if m:
        new_fm = ensure_last_updated(m.group(1), today)
        text = f"---\n{new_fm}\n---\n" + text[m.end():]

    # Is the URL already present anywhere? Then skip.
    if url in text:
        print(f"URL already present in {path}; not appending")
        path.write_text(text)
        return

    # Append bullet under Sources
    bullet = f"- [{title}]({url})"
    if gist:
        bullet += f" — {gist}"
    bullet += "\n"

    m2 = SOURCES_H2_RE.search(text)
    if m2:
        # Find end of Sources section (next ## heading or EOF)
        after = text[m2.end():]
        next_h2 = re.search(r"^##\s+", after, re.MULTILINE)
        insert_at = m2.end() + (next_h2.start() if next_h2 else len(after))
        # Trim trailing blank line before next heading/EOF
        while insert_at > 0 and text[insert_at - 1] == "\n":
            insert_at -= 1
        text = text[:insert_at] + "\n" + bullet + text[insert_at:]
    else:
        if not text.endswith("\n"):
            text += "\n"
        text += "\n## Sources\n\n" + bullet

    path.write_text(text)
    print(f"Appended source to {path}")


if __name__ == "__main__":
    main()
