#!/bin/bash
set -euo pipefail

# Researcher pipeline orchestration script
# Usage: run-researcher.sh <run-id>
# Reads approved findings from pipeline/runs/<run-id>/scanner-approved.json
# Invokes researcher agent for each finding, validates output

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

RUN_ID="${1:?ERROR: Must provide run-id as first argument}"
RUN_DIR="$PROJECT_ROOT/pipeline/runs/$RUN_ID"
APPROVED_FILE="$RUN_DIR/scanner-approved.json"

# Validate approved findings file exists (T-03-05)
if [ ! -f "$APPROVED_FILE" ]; then
  echo "ERROR: Approved findings not found: $APPROVED_FILE" >&2
  echo "Run approve-findings.sh first." >&2
  exit 1
fi

# Count findings to process
FINDING_COUNT=$(jq '.data.findings | length' "$APPROVED_FILE")

if [ "$FINDING_COUNT" -eq 0 ]; then
  echo "WARNING: No approved findings to research."
  exit 0
fi

echo "Processing $FINDING_COUNT approved findings..."
echo ""

SUCCESS=0
FAILED=0

for i in $(seq 0 $((FINDING_COUNT - 1))); do
  FINDING_ID=$(jq -r ".data.findings[$i].id" "$APPROVED_FILE")
  echo "Researching finding $((i+1))/$FINDING_COUNT: $FINDING_ID"

  # Build prompt for researcher agent
  PROMPT="Research finding index $i from $APPROVED_FILE."
  PROMPT="$PROMPT Pipeline run ID: $RUN_ID."
  PROMPT="$PROMPT Write your output metadata to: $RUN_DIR/researcher-$FINDING_ID.json."
  PROMPT="$PROMPT Write the report to the appropriate reports/{category}/ directory."

  # Invoke researcher agent (T-03-06: --max-turns 30 limits execution)
  claude -p --agent researcher --output-format json \
    --max-turns 30 \
    "$PROMPT"

  OUTPUT="$RUN_DIR/researcher-$FINDING_ID.json"

  # Check output file exists
  if [ ! -f "$OUTPUT" ]; then
    echo "WARNING: Researcher did not produce output for $FINDING_ID at $OUTPUT" >&2
    FAILED=$((FAILED + 1))
    continue
  fi

  # Validate against schema
  "$PROJECT_ROOT/pipeline/scripts/validate-handoff.sh" researcher "$OUTPUT"

  # T-03-03 mitigation: Validate report_path starts with reports/ and category is valid
  REPORT_PATH=$(jq -r '.data.reports[0].report_path' "$OUTPUT")
  if [[ ! "$REPORT_PATH" =~ ^reports/(privacy|cybersecurity|ai-law)/ ]]; then
    echo "ERROR: Invalid report path: $REPORT_PATH" >&2
    echo "Report path must start with reports/(privacy|cybersecurity|ai-law)/" >&2
    exit 1
  fi

  SUCCESS=$((SUCCESS + 1))
  echo "  Completed: $FINDING_ID"
  echo ""
done

echo "Research complete."
echo "  Successful: $SUCCESS / $FINDING_COUNT"
if [ "$FAILED" -gt 0 ]; then
  echo "  Failed: $FAILED"
fi

echo ""
echo "Next: Run reviewer agent."
