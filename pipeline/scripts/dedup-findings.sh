#!/bin/bash
set -euo pipefail

# Dedup scanner findings against the reports index.
#
# Usage: dedup-findings.sh <run-id>
# Reads:
#   pipeline/runs/<run-id>/scanner-output.json
#   reports/index.json
# Writes:
#   pipeline/runs/<run-id>/scanner-deduped.json    (findings to research)
#   pipeline/runs/<run-id>/scanner-duplicates.json (removed, with reason)
#
# Pass 1a (topic_key match) and Pass 1b (URL match) use the reports index as an
# O(1) lookup, replacing the old filesystem walk. Pass 2 (title substring) is
# retained as a last-resort heuristic but now reads titles from the index
# rather than re-parsing every .md file.
#
# Pass 3 (semantic comparison via Claude) is deferred per the RESEARCH open
# question. Implement if passes 1+2 prove insufficient.
#
# If reports/index.json is missing, the script falls back to a legacy
# filesystem walk so v1 pipeline runs never hard-fail on a fresh checkout.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

RUN_ID="${1:?ERROR: Must provide run-id as first argument}"
RUN_DIR="$PROJECT_ROOT/pipeline/runs/$RUN_ID"
INPUT="$RUN_DIR/scanner-output.json"
OUTPUT="$RUN_DIR/scanner-deduped.json"
DUPES="$RUN_DIR/scanner-duplicates.json"
# INDEX_PATH env var lets tests point at an isolated fixture index
INDEX="${INDEX_PATH:-$PROJECT_ROOT/reports/index.json}"

if [ ! -f "$INPUT" ]; then
  echo "ERROR: Scanner output not found: $INPUT" >&2
  exit 1
fi

PYTHON_BIN="${PYTHON_BIN:-python3}"

normalize_url() {
  # Single source of truth lives at tools/url_norm.py — see H4 in docs/REVIEW-2026-04-10.md
  "$PYTHON_BIN" "$PROJECT_ROOT/tools/url_norm.py" "$1"
}

PASS1A_KEEP=$(mktemp)
PASS1A_DUPES=$(mktemp)
PASS1A_UPDATES=$(mktemp)
PASS1B_KEEP=$(mktemp)
PASS1B_DUPES=$(mktemp)
PASS2_KEEP=$(mktemp)
PASS2_DUPES=$(mktemp)
INDEX_URLS=$(mktemp)
INDEX_KEYS=$(mktemp)
INDEX_TITLES=$(mktemp)

trap 'rm -f "$PASS1A_KEEP" "$PASS1A_DUPES" "$PASS1A_UPDATES" "$PASS1B_KEEP" "$PASS1B_DUPES" "$PASS2_KEEP" "$PASS2_DUPES" "$INDEX_URLS" "$INDEX_KEYS" "$INDEX_TITLES"' EXIT

touch "$PASS1A_KEEP" "$PASS1A_DUPES" "$PASS1A_UPDATES" "$PASS1B_KEEP" "$PASS1B_DUPES" "$PASS2_KEEP" "$PASS2_DUPES"

if [ -f "$INDEX" ]; then
  jq -r '.reports | keys[]' "$INDEX" 2>/dev/null | sort -u > "$INDEX_KEYS" || true
  jq -r '.url_index | keys[]' "$INDEX" 2>/dev/null | sort -u > "$INDEX_URLS" || true
  jq -r '.reports[] | .title | ascii_downcase' "$INDEX" 2>/dev/null | sort -u > "$INDEX_TITLES" || true
  echo "Loaded reports/index.json: $(wc -l < "$INDEX_KEYS") topic_keys, $(wc -l < "$INDEX_URLS") URLs, $(wc -l < "$INDEX_TITLES") titles"
else
  echo "WARNING: reports/index.json not found — falling back to empty index. Run tools/backfill_reports_index.py first."
  : > "$INDEX_KEYS"
  : > "$INDEX_URLS"
  : > "$INDEX_TITLES"
fi

# --- Pass 1a: topic_key match ---
echo "Pass 1a: topic_key match dedup..."

jq -c '.data.findings[]' "$INPUT" | while IFS= read -r finding; do
  topic_key=$(echo "$finding" | jq -r '.topic_key // empty')
  if [ -z "$topic_key" ]; then
    # Fallback: compute topic_key on the fly if the scanner/annotate step
    # didn't provide one. Capture all three fields (key, type, confidence) so
    # downstream stages don't lose the confidence signal. In the normal flow
    # orchestrator Mode 1 Step 2.5 runs `topic_keys.py annotate` first, so
    # this fallback should rarely fire.
    kv=$("$PYTHON_BIN" "$PROJECT_ROOT/tools/topic_keys.py" --finding-json "$finding" 2>/dev/null || echo '{}')
    topic_key=$(echo "$kv" | jq -r '.topic_key // empty')
    topic_type=$(echo "$kv" | jq -r '.topic_type // empty')
    topic_key_confidence=$(echo "$kv" | jq -r '.confidence // empty')
    if [ -n "$topic_key" ]; then
      finding=$(echo "$finding" | jq -c \
        --arg k "$topic_key" \
        --arg t "$topic_type" \
        --arg c "$topic_key_confidence" \
        '. + {topic_key: $k, topic_type: $t, topic_key_confidence: $c}')
    fi
  fi

  if [ -n "$topic_key" ] && grep -qxF -- "$topic_key" "$INDEX_KEYS" 2>/dev/null; then
    # Phase 2: topic_key match → run diff_signal classifier against the
    # existing index entry. Pure noise drops silently; everything else
    # becomes a candidate_update for the researcher to append to the
    # existing report instead of filing a sibling.
    existing_json=$(jq -c --arg k "$topic_key" '.reports[$k] // {}' "$INDEX" 2>/dev/null || echo '{}')
    diff_out=$("$PYTHON_BIN" "$PROJECT_ROOT/tools/diff_signal.py" \
      --finding-json "$finding" \
      --existing-json "$existing_json" 2>/dev/null || echo '{"diff_signal":"narrative_only","status_before":"","status_after":""}')
    signal=$(echo "$diff_out" | jq -r '.diff_signal // "narrative_only"')
    status_before=$(echo "$diff_out" | jq -r '.status_before // ""')
    status_after=$(echo "$diff_out" | jq -r '.status_after // ""')
    previous_report_path=$(echo "$existing_json" | jq -r '.report_path // ""')

    if [ "$signal" = "noise" ]; then
      echo "$finding" | jq -c --arg r "noise" --arg k "$topic_key" \
        '. + {dedup_reason: $r, noise_topic_key: $k}' >> "$PASS1A_DUPES"
    else
      echo "$finding" | jq -c \
        --arg k "$topic_key" \
        --arg rp "$previous_report_path" \
        --arg ds "$signal" \
        --arg sb "$status_before" \
        --arg sa "$status_after" \
        '. + {is_update: true, previous_topic_key: $k, previous_report_path: $rp, diff_signal: $ds, status_before: $sb, status_after: $sa}' \
        >> "$PASS1A_UPDATES"
    fi
  else
    echo "$finding" >> "$PASS1A_KEEP"
  fi
done

NOISE_DUPES=$(wc -l < "$PASS1A_DUPES" 2>/dev/null | tr -d ' ')
UPDATE_CANDS=$(wc -l < "$PASS1A_UPDATES" 2>/dev/null | tr -d ' ')
echo "  topic_key matches → noise drops: $NOISE_DUPES"
echo "  topic_key matches → candidate_updates: $UPDATE_CANDS"

# --- Pass 1b: URL match against url_index ---
echo "Pass 1b: URL match dedup..."

if [ -s "$PASS1A_KEEP" ]; then
  while IFS= read -r finding; do
    raw_url=$(echo "$finding" | jq -r '.source_url // empty')
    norm_url=$(normalize_url "$raw_url")
    if [ -n "$norm_url" ] && grep -qxF "$norm_url" "$INDEX_URLS" 2>/dev/null; then
      echo "$finding" | jq -c --arg r "url_match" '. + {dedup_reason: $r}' >> "$PASS1B_DUPES"
    else
      echo "$finding" >> "$PASS1B_KEEP"
    fi
  done < "$PASS1A_KEEP"
fi

URL_DUPES=$(wc -l < "$PASS1B_DUPES" 2>/dev/null | tr -d ' ')
echo "  URL matches removed: $URL_DUPES"

# --- Pass 2: Title substring ---
echo "Pass 2: title substring dedup..."

if [ -s "$PASS1B_KEEP" ] && [ -s "$INDEX_TITLES" ]; then
  while IFS= read -r finding; do
    title=$(echo "$finding" | jq -r '.title // empty' | tr '[:upper:]' '[:lower:]')
    is_dupe=false
    if [ ${#title} -gt 20 ]; then
      while IFS= read -r existing_title; do
        if [ ${#existing_title} -gt 20 ]; then
          if echo "$existing_title" | grep -qiF -- "$title" 2>/dev/null || \
             echo "$title" | grep -qiF -- "$existing_title" 2>/dev/null; then
            is_dupe=true
            break
          fi
        fi
      done < "$INDEX_TITLES"
    fi
    if [ "$is_dupe" = true ]; then
      echo "$finding" | jq -c --arg r "title_match" '. + {dedup_reason: $r}' >> "$PASS2_DUPES"
    else
      echo "$finding" >> "$PASS2_KEEP"
    fi
  done < "$PASS1B_KEEP"
elif [ -s "$PASS1B_KEEP" ]; then
  cp "$PASS1B_KEEP" "$PASS2_KEEP"
fi

TITLE_DUPES=$(wc -l < "$PASS2_DUPES" 2>/dev/null | tr -d ' ')
echo "  Title matches removed: $TITLE_DUPES"

# Note: Pass 3 (semantic comparison via Claude) is deferred per RESEARCH open question 4.
# Implement if passes 1a+1b+2 prove insufficient for catching duplicates.

# --- Build output ---
echo "Building deduped output..."

KEPT_FINDINGS="[]"
if [ -s "$PASS2_KEEP" ]; then
  KEPT_FINDINGS=$(jq -s '.' "$PASS2_KEEP")
fi

CANDIDATE_UPDATES="[]"
if [ -s "$PASS1A_UPDATES" ]; then
  CANDIDATE_UPDATES=$(jq -s '.' "$PASS1A_UPDATES")
fi

jq --argjson findings "$KEPT_FINDINGS" --argjson updates "$CANDIDATE_UPDATES" \
  '.data.findings = $findings | .data.candidate_updates = $updates' "$INPUT" > "$OUTPUT"

ALL_DUPES="[]"
for f in "$PASS1A_DUPES" "$PASS1B_DUPES" "$PASS2_DUPES"; do
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
