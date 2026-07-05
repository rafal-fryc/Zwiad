#!/bin/bash
set -euo pipefail

# Generate escalation markdown for unresolved reviewer issues
# Usage: generate-escalation.sh <run-id> <finding-id> <report-path>
# Reads: reviewer-feedback-r*-<finding-id>.json and researcher-revision-r*-<finding-id>.json
# Writes: reviewer-escalation-<finding-id>.md

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

RUN_ID="${1:?ERROR: Must provide run-id as first argument}"
FINDING_ID="${2:?ERROR: Must provide finding-id as second argument}"
REPORT_PATH="${3:?ERROR: Must provide report-path as third argument}"

# T-04-05: Validate finding_id matches strict pattern
if [[ ! "$FINDING_ID" =~ ^[A-Za-z]+-[0-9A-Za-z-]+$ ]]; then
  echo "ERROR: Invalid finding_id: $FINDING_ID" >&2
  exit 1
fi

RUN_DIR="$PROJECT_ROOT/pipeline/runs/$RUN_ID"
OUTPUT="$RUN_DIR/reviewer-escalation-${FINDING_ID}.md"

# Find the latest feedback file (round 3)
LATEST_FEEDBACK="$RUN_DIR/reviewer-feedback-r3-${FINDING_ID}.json"
if [ ! -f "$LATEST_FEEDBACK" ]; then
  echo "ERROR: Round 3 feedback not found: $LATEST_FEEDBACK" >&2
  exit 1
fi

# Extract unresolved issues (open or upheld) from latest feedback
UNRESOLVED=$(jq -c '[.issues[] | select(.status == "open" or .status == "upheld")]' "$LATEST_FEEDBACK")
UNRESOLVED_COUNT=$(echo "$UNRESOLVED" | jq 'length')

if [ "$UNRESOLVED_COUNT" -eq 0 ]; then
  echo "WARNING: No unresolved issues found in round 3 feedback for $FINDING_ID"
  exit 0
fi

# Start building the escalation markdown
{
  echo "# Verification Escalation"
  echo ""
  echo "**Pipeline Run:** $RUN_ID"
  echo "**Finding:** $FINDING_ID"
  echo "**Report:** $REPORT_PATH"
  echo "**Rounds Completed:** 3"
  echo ""
  echo "## Unresolved Issues"

  # Process each unresolved issue
  for idx in $(seq 0 $((UNRESOLVED_COUNT - 1))); do
    ISSUE=$(echo "$UNRESOLVED" | jq -c ".[$idx]")
    SEVERITY=$(echo "$ISSUE" | jq -r '.severity')
    CLAIM=$(echo "$ISSUE" | jq -r '.claim')
    CONCERN=$(echo "$ISSUE" | jq -r '.issue')
    SUGGESTED_FIX=$(echo "$ISSUE" | jq -r '.suggested_fix')

    echo ""
    echo "### Issue $((idx + 1)): $SEVERITY -- $(echo "$CLAIM" | head -c 60)"
    echo ""
    echo "**Claim:** \"$CLAIM\""
    echo ""
    echo "**Reviewer's Concern:** $CONCERN"
    echo ""

    # Try to find researcher's response from revision files
    RESEARCHER_RESPONSE="No response"
    for ROUND in 1 2; do
      REVISION_FILE="$RUN_DIR/researcher-revision-r${ROUND}-${FINDING_ID}.json"
      if [ -f "$REVISION_FILE" ]; then
        # Look for a response addressing this claim
        RESPONSE=$(jq -r --arg claim "$CLAIM" '
          if .revisions then
            (.revisions[] | select(.claim == $claim) | .justification) // "No specific response"
          elif .issues_addressed then
            (.issues_addressed[] | select(.claim == $claim) | .response) // "No specific response"
          else
            "No specific response"
          end
        ' "$REVISION_FILE" 2>/dev/null || echo "No specific response")
        if [ "$RESPONSE" != "No specific response" ] && [ -n "$RESPONSE" ]; then
          RESEARCHER_RESPONSE="$RESPONSE"
        fi
      fi
    done

    echo "**Researcher's Response:** $RESEARCHER_RESPONSE"
    echo ""

    # Build round history from all feedback files
    echo "**Round History:**"
    for ROUND in 1 2 3; do
      FEEDBACK_FILE="$RUN_DIR/reviewer-feedback-r${ROUND}-${FINDING_ID}.json"
      if [ -f "$FEEDBACK_FILE" ]; then
        # Check if this issue appears in this round's feedback
        ROUND_STATUS=$(jq -r --arg claim "$CLAIM" '
          (.issues[] | select(.claim == $claim) | .status) // empty
        ' "$FEEDBACK_FILE" 2>/dev/null || true)

        if [ -n "$ROUND_STATUS" ]; then
          case "$ROUND_STATUS" in
            open)
              echo "- Round $ROUND: Raised by reviewer"
              ;;
            fixed)
              echo "- Round $ROUND: Fixed by researcher"
              ;;
            disputed)
              echo "- Round $ROUND: Disputed by researcher"
              ;;
            upheld)
              echo "- Round $ROUND: Upheld by reviewer"
              ;;
            withdrawn)
              echo "- Round $ROUND: Withdrawn by reviewer"
              ;;
            *)
              echo "- Round $ROUND: $ROUND_STATUS"
              ;;
          esac
        fi
      fi
    done
  done

  echo ""
  echo "## Current Report"
  echo ""
  echo "The current version of the report is at: \`$REPORT_PATH\`"
  echo ""
  echo "Please review the report directly and resolve the issues listed above."
  echo ""
  echo "## Instructions"
  echo ""
  echo "1. Read the report at the path above."
  echo "2. For each unresolved issue, either:"
  echo "   - Edit the report to address the reviewer's concern, OR"
  echo "   - Add a note explaining why the current text is acceptable."
  echo "3. When all issues are resolved, uncomment the APPROVED marker below to resume the pipeline."
  echo ""
  echo "<!-- ## APPROVED -->"

} > "$OUTPUT"

# Machine-readable companion — the orchestrator/bot escalation gates glob
# escalation-*.json, so this file is what actually pauses the pipeline.
JSON_OUTPUT="$RUN_DIR/escalation-${FINDING_ID}.json"
jq -n \
  --arg run_id "$RUN_ID" \
  --arg finding_id "$FINDING_ID" \
  --arg report_path "$REPORT_PATH" \
  --arg md_path "$(basename "$OUTPUT")" \
  --argjson unresolved "$UNRESOLVED" \
  '{
    run_id: $run_id,
    finding_id: $finding_id,
    report_path: $report_path,
    escalation_md: $md_path,
    rounds_completed: 3,
    unresolved_issues: $unresolved,
    resolved: false
  }' > "$JSON_OUTPUT"
echo "Escalation JSON written to: $JSON_OUTPUT"

echo "Escalation written to: $OUTPUT"
echo "  Unresolved issues: $UNRESOLVED_COUNT"
