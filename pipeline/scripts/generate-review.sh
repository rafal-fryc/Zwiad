#!/bin/bash
set -euo pipefail

# Generate human-readable review markdown from deduped scanner output
# Usage: generate-review.sh <run-id>
# Reads: pipeline/runs/<run-id>/scanner-deduped.json
# Writes: pipeline/runs/<run-id>/scanner-review.md

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

RUN_ID="${1:?ERROR: Must provide run-id as first argument}"
RUN_DIR="$PROJECT_ROOT/pipeline/runs/$RUN_ID"
INPUT="$RUN_DIR/scanner-deduped.json"
OUTPUT="$RUN_DIR/scanner-review.md"

if [ ! -f "$INPUT" ]; then
  echo "ERROR: Deduped scanner output not found: $INPUT" >&2
  echo "Run dedup-findings.sh first." >&2
  exit 1
fi

SCAN_DATE=$(jq -r '.timestamp' "$INPUT" | cut -d'T' -f1)
FINDING_COUNT=$(jq '.data.findings | length' "$INPUT")
FAILURE_COUNT=$(jq '.data.source_failures // [] | length' "$INPUT")
# Count successful sources (total unique sources in findings)
SUCCESS_COUNT=$(jq '[.data.findings[].source] | unique | length' "$INPUT")

# Generate review markdown
{
  echo "# Scanner Findings Review"
  echo ""
  echo "**Pipeline Run:** $RUN_ID"
  echo "**Scan Date:** $SCAN_DATE"
  echo "**Total Findings:** $FINDING_COUNT"
  echo "**Sources Scanned:** $SUCCESS_COUNT successful, $FAILURE_COUNT failed"
  echo ""

  # Source failures section (D-08)
  if [ "$FAILURE_COUNT" -gt 0 ]; then
    echo "## Source Failures"
    echo ""
    jq -r '.data.source_failures[] | "- \(.source_name // .source_id): \(.error)"' "$INPUT"
    echo ""
  fi

  echo "## Findings"
  echo ""

  # Generate finding entries with checkboxes (D-12)
  SEQ=0
  jq -c '.data.findings[]' "$INPUT" | while IFS= read -r finding; do
    SEQ=$((SEQ + 1))
    id=$(echo "$finding" | jq -r '.id')
    title=$(echo "$finding" | jq -r '.title')
    source=$(echo "$finding" | jq -r '.source')
    url=$(echo "$finding" | jq -r '.source_url')
    category=$(echo "$finding" | jq -r '.category // "uncategorized"')
    relevance=$(echo "$finding" | jq -r '.relevance')
    jurisdiction=$(echo "$finding" | jq -r '.jurisdiction')
    dev_type=$(echo "$finding" | jq -r '.development_type')
    summary=$(echo "$finding" | jq -r '.summary')

    echo "### $SEQ. [$id] $title"
    echo "- [ ] Approve"
    echo "- **Source:** $source"
    echo "- **URL:** $url"
    echo "- **Category:** $category"
    echo "- **Relevance:** $relevance"
    echo "- **Jurisdiction:** $jurisdiction"
    echo "- **Type:** $dev_type"
    echo "- **Summary:** $summary"
    echo "- **Notes:** _(add notes here)_"
    echo ""
    echo "---"
    echo ""
  done

  echo "<!-- Review each finding above. Check the box to approve. -->"
  echo "<!-- Edit titles, relevance, or add notes as needed (D-13). -->"
  echo "<!-- When review is complete, add the marker below: -->"
  echo ""
  echo "<!-- ## APPROVED -->"

} > "$OUTPUT"

echo "Review file generated: $OUTPUT"
echo "  Findings: $FINDING_COUNT"
echo "  Edit the file, check boxes to approve, then add '## APPROVED' marker."
