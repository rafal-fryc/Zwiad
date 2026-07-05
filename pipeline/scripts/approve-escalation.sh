#!/bin/bash
set -euo pipefail

# LEGACY: This script is the standalone CLI alternative for resolving
# escalations. The production runtime handles escalations via Discord +
# orchestrator Mode 2. Kept for ad-hoc CLI use and pytest fixtures.
#
# Approve escalated reviewer findings after human resolution
# Usage: approve-escalation.sh <run-id> <finding-id>
# Reads: pipeline/runs/<run-id>/reviewer-escalation-<finding-id>.md
# Updates: pipeline/runs/<run-id>/reviewer-output.json

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

RUN_ID="${1:?ERROR: Must provide run-id as first argument}"
FINDING_ID="${2:?ERROR: Must provide finding-id as second argument}"

# T-04-05: Validate finding_id matches strict pattern
if [[ ! "$FINDING_ID" =~ ^[A-Za-z]+-[0-9A-Za-z-]+$ ]]; then
  echo "ERROR: Invalid finding_id: $FINDING_ID" >&2
  exit 1
fi

RUN_DIR="$PROJECT_ROOT/pipeline/runs/$RUN_ID"
ESCALATION="$RUN_DIR/reviewer-escalation-${FINDING_ID}.md"
OUTPUT="$RUN_DIR/reviewer-output.json"

# Validate escalation file exists
if [ ! -f "$ESCALATION" ]; then
  echo "ERROR: Escalation file not found: $ESCALATION" >&2
  exit 1
fi

# Validate reviewer output exists
if [ ! -f "$OUTPUT" ]; then
  echo "ERROR: Reviewer output not found: $OUTPUT" >&2
  echo "Run run-reviewer.sh first." >&2
  exit 1
fi

# T-04-06: Check for APPROVED marker (line-start anchored)
if ! grep -q "^## APPROVED" "$ESCALATION"; then
  echo "ERROR: Escalation file has not been approved." >&2
  echo "To approve, uncomment the '## APPROVED' marker in:" >&2
  echo "  $ESCALATION" >&2
  echo "" >&2
  echo "Edit the file and change:" >&2
  echo "  <!-- ## APPROVED -->" >&2
  echo "to:" >&2
  echo "  ## APPROVED" >&2
  exit 1
fi

# Update the finding's review status in reviewer-output.json
# Change status from "needs-human-review" to "verified"
UPDATED=$(jq --arg fid "$FINDING_ID" '
  .data.reviews = [
    .data.reviews[] |
    if .finding_id == $fid then
      .status = "verified" | .issues_found = []
    else
      .
    end
  ]
' "$OUTPUT")

echo "$UPDATED" > "$OUTPUT"

# Check if all reviews are now verified
ALL_VERIFIED=$(jq '[.data.reviews[] | select(.status != "verified")] | length == 0' "$OUTPUT")

if [ "$ALL_VERIFIED" = "true" ]; then
  # Update envelope status to complete
  jq '.status = "complete"' "$OUTPUT" > "$OUTPUT.tmp" && mv "$OUTPUT.tmp" "$OUTPUT"
  echo "All reviews now verified."
  echo "Ready for categorizer agent."
else
  REMAINING=$(jq '[.data.reviews[] | select(.status != "verified")] | length' "$OUTPUT")
  echo "Approved: $FINDING_ID"
  echo "Remaining reviews needing approval: $REMAINING"
fi

# Clear the machine-readable escalation gate for this finding.
# The human-readable reviewer-escalation-*.md file is kept as an artifact.
GATE_FILE="$RUN_DIR/escalation-${FINDING_ID}.json"
if [ -f "$GATE_FILE" ]; then
  rm -f "$GATE_FILE"
  echo "Escalation gate cleared: $GATE_FILE"
fi

# If no escalation-*.json files remain, clear the has-escalations marker.
REMAINING_GATES=$(find "$RUN_DIR" -maxdepth 1 -name "escalation-*.json" | wc -l)
if [ "$REMAINING_GATES" -eq 0 ]; then
  rm -f "$RUN_DIR/has-escalations.marker"
  echo "All escalations resolved — has-escalations.marker removed."
fi

# Re-validate updated output
"$PROJECT_ROOT/pipeline/scripts/validate-handoff.sh" reviewer "$OUTPUT"
