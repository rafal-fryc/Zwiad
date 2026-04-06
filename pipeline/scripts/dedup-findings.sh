#!/bin/bash
set -euo pipefail

# Dedup scanner findings against existing reports
# Usage: dedup-findings.sh <run-id>
# Reads: pipeline/runs/<run-id>/scanner-output.json
# Writes: pipeline/runs/<run-id>/scanner-deduped.json (findings with duplicates removed)
# Also writes: pipeline/runs/<run-id>/scanner-duplicates.json (removed items for audit)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

RUN_ID="${1:?ERROR: Must provide run-id as first argument}"
RUN_DIR="$PROJECT_ROOT/pipeline/runs/$RUN_ID"
INPUT="$RUN_DIR/scanner-output.json"
OUTPUT="$RUN_DIR/scanner-deduped.json"
DUPES="$RUN_DIR/scanner-duplicates.json"

if [ ! -f "$INPUT" ]; then
  echo "ERROR: Scanner output not found: $INPUT" >&2
  exit 1
fi

# URL normalization: strip UTM params, Lexology tracking, trailing slash, force https
normalize_url() {
  local url="$1"
  echo "$url" \
    | sed 's|^http://|https://|' \
    | sed 's|[?&]utm_[^&]*||g' \
    | sed 's|[?&]g=[^&]*||g' \
    | sed 's|?$||' \
    | sed 's|/$||'
}

# --- Pass 1: Collect existing report URLs ---
echo "Pass 1: URL match dedup..."
EXISTING_URLS=$(mktemp)
PASS1_KEEP=$(mktemp)
PASS1_DUPES=$(mktemp)
EXISTING_TITLES=$(mktemp)
PASS2_KEEP=$(mktemp)
PASS2_DUPES=$(mktemp)
trap 'rm -f "$EXISTING_URLS" "$PASS1_KEEP" "$PASS1_DUPES" "$EXISTING_TITLES" "$PASS2_KEEP" "$PASS2_DUPES"' EXIT

# Extract URLs from existing reports (grep for markdown links and source_url fields)
if [ -d "$PROJECT_ROOT/reports" ]; then
  find "$PROJECT_ROOT/reports" -name "*.md" -type f 2>/dev/null | while read -r report; do
    grep -oP 'https?://[^\s\)\]>"]+' "$report" 2>/dev/null || true
  done | while read -r url; do
    normalize_url "$url"
  done | sort -u > "$EXISTING_URLS"
fi

# --- Pass 1: Filter by URL match ---
# Touch files to ensure they exist even if no findings
touch "$PASS1_KEEP" "$PASS1_DUPES"

jq -c '.data.findings[]' "$INPUT" | while IFS= read -r finding; do
  raw_url=$(echo "$finding" | jq -r '.source_url')
  norm_url=$(normalize_url "$raw_url")
  if grep -qF "$norm_url" "$EXISTING_URLS" 2>/dev/null; then
    echo "$finding" >> "$PASS1_DUPES"
  else
    echo "$finding" >> "$PASS1_KEEP"
  fi
done

URL_DUPES=$(wc -l < "$PASS1_DUPES" 2>/dev/null | tr -d ' ')
echo "  URL matches removed: $URL_DUPES"

# --- Pass 2: Title similarity ---
echo "Pass 2: Title similarity dedup..."

# Extract titles from existing reports (first H1 or title in frontmatter)
if [ -d "$PROJECT_ROOT/reports" ]; then
  find "$PROJECT_ROOT/reports" -name "*.md" -type f 2>/dev/null | while read -r report; do
    # Try frontmatter title first, then first H1
    grep -m1 '^title:' "$report" 2>/dev/null | sed 's/^title:\s*//' || \
    grep -m1 '^# ' "$report" 2>/dev/null | sed 's/^# //' || true
  done | tr '[:upper:]' '[:lower:]' | sort -u > "$EXISTING_TITLES"
fi

# Touch to ensure files exist
touch "$PASS2_KEEP" "$PASS2_DUPES"

if [ -s "$PASS1_KEEP" ]; then
  while IFS= read -r finding; do
    title=$(echo "$finding" | jq -r '.title' | tr '[:upper:]' '[:lower:]')
    # Check if any existing title contains this title as substring or vice versa (>20 chars overlap)
    is_dupe=false
    if [ -s "$EXISTING_TITLES" ]; then
      while IFS= read -r existing_title; do
        if [ ${#existing_title} -gt 20 ] && [ ${#title} -gt 20 ]; then
          if echo "$existing_title" | grep -qiF "$title" 2>/dev/null || \
             echo "$title" | grep -qiF "$existing_title" 2>/dev/null; then
            is_dupe=true
            break
          fi
        fi
      done < "$EXISTING_TITLES"
    fi
    if [ "$is_dupe" = true ]; then
      echo "$finding" >> "$PASS2_DUPES"
    else
      echo "$finding" >> "$PASS2_KEEP"
    fi
  done < "$PASS1_KEEP"
fi

TITLE_DUPES=$(wc -l < "$PASS2_DUPES" 2>/dev/null | tr -d ' ')
echo "  Title matches removed: $TITLE_DUPES"

# Note: Pass 3 (semantic comparison via Claude) is deferred per RESEARCH open question 4.
# Implement if passes 1+2 prove insufficient for catching duplicates.

# --- Build output ---
echo "Building deduped output..."

# Collect remaining findings into array
KEPT_FINDINGS="[]"
if [ -s "$PASS2_KEEP" ]; then
  KEPT_FINDINGS=$(jq -s '.' "$PASS2_KEEP")
fi

# Build deduped envelope (same envelope, filtered findings)
jq --argjson findings "$KEPT_FINDINGS" \
  '.data.findings = $findings' "$INPUT" > "$OUTPUT"

# Build duplicates log for audit
ALL_DUPES="[]"
for f in "$PASS1_DUPES" "$PASS2_DUPES"; do
  if [ -s "$f" ]; then
    FILE_DUPES=$(jq -s '.' "$f")
    ALL_DUPES=$(echo "$ALL_DUPES" | jq --argjson d "$FILE_DUPES" '. + $d')
  fi
done
echo "$ALL_DUPES" | jq '.' > "$DUPES"

KEPT=$(echo "$KEPT_FINDINGS" | jq 'length')
REMOVED=$(echo "$ALL_DUPES" | jq 'length')
echo ""
echo "Dedup complete."
echo "  Kept: $KEPT findings"
echo "  Removed: $REMOVED duplicates"
echo "  Output: $OUTPUT"
echo "  Duplicates log: $DUPES"
