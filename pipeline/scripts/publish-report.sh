#!/usr/bin/env bash
#
# publish-report.sh <path-to-memo.md>
#
# Copies a finalized research report into the local zwiad-reports clone,
# regenerates index.json, commits, and pushes. The push triggers a GitHub
# Action in zwiad-reports which fires the Vercel Deploy Hook, rebuilding
# the sitehome site and publishing the report at /reports/<slug>.
#
# Prerequisites:
#   - ~/projecty/zwiad-reports cloned with SSH remote and push access
#   - Report file has YAML frontmatter with: title, date (YYYY-MM-DD), topic, summary
#   - Filename MUST be <YYYY-MM-DD>-<slug>.md; the full filename minus .md is the slug
#
set -euo pipefail

REPORTS_REPO="${REPORTS_REPO:-$HOME/projecty/zwiad-reports}"

if [ $# -ne 1 ]; then
  echo "Usage: $0 <path-to-memo.md>" >&2
  exit 2
fi

MEMO_PATH="$1"
if [ ! -f "$MEMO_PATH" ]; then
  echo "Error: report file not found: $MEMO_PATH" >&2
  exit 2
fi

if [ ! -d "$REPORTS_REPO/.git" ]; then
  echo "Error: $REPORTS_REPO is not a git checkout" >&2
  exit 2
fi

FILENAME="$(basename "$MEMO_PATH")"
SLUG="${FILENAME%.md}"

if ! [[ "$FILENAME" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}-[a-z0-9-]+\.md$ ]]; then
  echo "Error: filename must match <YYYY-MM-DD>-<slug>.md (lowercase, hyphens): $FILENAME" >&2
  exit 2
fi

# Validate frontmatter via python (title/date/topic/summary required; no yaml dep needed)
python3 - "$MEMO_PATH" <<'PY'
import re, sys, pathlib
path = pathlib.Path(sys.argv[1])
text = path.read_text()
m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.DOTALL)
if not m:
    print(f"Error: {path} missing YAML frontmatter (--- ... ---)", file=sys.stderr)
    sys.exit(1)
required = {"title", "date", "topic", "summary"}
found = set()
for line in m.group(1).splitlines():
    key = line.split(":", 1)[0].strip()
    if key:
        found.add(key)
missing = required - found
if missing:
    print(f"Error: {path} missing frontmatter keys: {sorted(missing)}", file=sys.stderr)
    sys.exit(1)
PY

DEST="$REPORTS_REPO/memos/$FILENAME"
if [ -e "$DEST" ] && ! cmp -s "$MEMO_PATH" "$DEST"; then
  echo "Note: overwriting existing report $DEST"
fi

mkdir -p "$REPORTS_REPO/memos"
cp "$MEMO_PATH" "$DEST"

# Regenerate index.json from all memos
python3 - "$REPORTS_REPO" <<'PY'
import json, re, pathlib, datetime
root = pathlib.Path(__import__("sys").argv[1])
memos_dir = root / "memos"
entries = []
for f in sorted(memos_dir.glob("*.md")):
    text = f.read_text()
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.DOTALL)
    if not m:
        raise SystemExit(f"Memo missing frontmatter: {f}")
    meta = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"').strip("'")
    entries.append({
        "slug": f.stem,
        "file": f"memos/{f.name}",
        "title": meta.get("title", ""),
        "date": meta.get("date", ""),
        "topic": meta.get("topic", ""),
        "summary": meta.get("summary", ""),
    })
entries.sort(key=lambda e: e["date"], reverse=True)
out = {"generated": datetime.date.today().isoformat(), "memos": entries}
(root / "index.json").write_text(json.dumps(out, indent=2) + "\n")
print(f"Regenerated index.json with {len(entries)} memo(s)")
PY

cd "$REPORTS_REPO"
if git diff --quiet && git diff --cached --quiet; then
  echo "No changes to publish."
  exit 0
fi

git add memos/ index.json
git commit -m "Publish: $SLUG"
git push
echo "Published $SLUG — Vercel rebuild should begin within seconds."
