#!/bin/bash
set -euo pipefail

# LEGACY: This script is the standalone CLI alternative to the Discord
# approval flow (/approve_all, /approve, /reject). The production runtime
# bypasses this script. Kept for ad-hoc CLI use and pytest fixtures.
#
# Parse approved review markdown back to JSON for pipeline
# Usage: approve-findings.sh <run-id>
# Reads: pipeline/runs/<run-id>/scanner-review.md
# Reads: pipeline/runs/<run-id>/scanner-deduped.json (for finding data)
# Writes: pipeline/runs/<run-id>/scanner-approved.json (approved findings only)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

RUN_ID="${1:?ERROR: Must provide run-id as first argument}"
RUN_DIR="$PROJECT_ROOT/pipeline/runs/$RUN_ID"
REVIEW="$RUN_DIR/scanner-review.md"
SOURCE="$RUN_DIR/scanner-deduped.json"
OUTPUT="$RUN_DIR/scanner-approved.json"

if [ ! -f "$REVIEW" ]; then
  echo "ERROR: Review file not found: $REVIEW" >&2
  exit 1
fi

if [ ! -f "$SOURCE" ]; then
  echo "ERROR: Deduped scanner output not found: $SOURCE" >&2
  exit 1
fi

# Check for approval marker (D-14)
if ! grep -q "^## APPROVED" "$REVIEW"; then
  echo "ERROR: Review file has not been approved." >&2
  echo "Add '## APPROVED' marker to $REVIEW when review is complete." >&2
  exit 1
fi

# Extract approved finding IDs (D-12: checkbox pattern)
# Pattern: "- [x] Approve" preceded by "### N. [FINDING-ID]"
# We look for checked boxes and extract the finding ID from the preceding heading
# T-02-07 mitigation: strict pattern matching on finding IDs
APPROVED_IDS=$(mktemp)
trap 'rm -f "$APPROVED_IDS"' EXIT

# Parse: find lines with checked approve boxes, extract the finding ID from context
# Support both SCAN-YYYYMMDD-NNN and other ID formats (e.g., finding-NNN)
grep -B2 '^\- \[x\] Approve' "$REVIEW" | grep -oP '(?<=\[)[A-Za-z]+-[\w-]+(?=\])' | sort -u > "$APPROVED_IDS"

APPROVED_COUNT=$(wc -l < "$APPROVED_IDS" | tr -d ' ')
echo "Approved findings: $APPROVED_COUNT"

if [ "$APPROVED_COUNT" -eq 0 ]; then
  echo "WARNING: No findings were approved. Output will have empty findings array."
fi

# T-02-07 mitigation: Only finding IDs present in the original scanner output can be approved
# Filter deduped findings to only those with approved IDs
APPROVED_FINDINGS=$(jq --slurpfile ids <(jq -R '.' "$APPROVED_IDS" | jq -s '.') \
  '[.data.findings[] | select(.id as $fid | $ids[0] | index($fid))]' "$SOURCE")

# Verify no injected IDs (IDs in review but not in source data)
VALID_COUNT=$(echo "$APPROVED_FINDINGS" | jq 'length')
if [ "$VALID_COUNT" -ne "$APPROVED_COUNT" ]; then
  INJECTED=$((APPROVED_COUNT - VALID_COUNT))
  echo "WARNING: $INJECTED approved ID(s) not found in scanner output (ignored)."
  APPROVED_COUNT="$VALID_COUNT"
fi

# Build approved envelope (T-02-08: preserve audit trail)
jq --argjson findings "$APPROVED_FINDINGS" '{
  schema_version: .schema_version,
  pipeline_run_id: .pipeline_run_id,
  timestamp: (now | todate),
  stage: "human-review",
  status: "complete",
  data: {
    findings: $findings
  }
}' "$SOURCE" > "$OUTPUT"

echo "Approved output: $OUTPUT"
echo "  Approved: $APPROVED_COUNT findings"
echo "  Ready for researcher agent."
