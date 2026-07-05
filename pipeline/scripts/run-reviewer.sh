#!/bin/bash
set -euo pipefail

# Reviewer pipeline orchestration script
# Usage: run-reviewer.sh <run-id>
# Reads researcher output files from pipeline/runs/<run-id>/
# Invokes reviewer agent for each report, iterates up to 3 rounds
# Escalates unresolved issues after 3 rounds

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

RUN_ID="${1:?ERROR: Must provide run-id as first argument}"
RUN_DIR="$PROJECT_ROOT/pipeline/runs/$RUN_ID"

# Validate run directory exists
if [ ! -d "$RUN_DIR" ]; then
  echo "ERROR: Run directory not found: $RUN_DIR" >&2
  exit 1
fi

# Collect reports to review from researcher output files
REPORTS_JSON="[]"
REPORT_COUNT=0

for RESEARCHER_FILE in "$RUN_DIR"/researcher-*.json; do
  # Skip if no matching files (glob returns literal pattern)
  [ -f "$RESEARCHER_FILE" ] || continue

  # Skip revision files (researcher-revision-r*)
  BASENAME=$(basename "$RESEARCHER_FILE")
  if [[ "$BASENAME" =~ ^researcher-revision- ]]; then
    continue
  fi

  # Extract reports from each researcher output
  # Handle both formats: .data.reports[] (array) and .data (flat object with finding_id)
  FILE_REPORTS=$(jq -c 'if .data.reports then .data.reports[] else .data | select(.finding_id) end' "$RESEARCHER_FILE" 2>/dev/null || true)
  while IFS= read -r report; do
    [ -z "$report" ] && continue
    REPORTS_JSON=$(echo "$REPORTS_JSON" | jq --argjson r "$report" '. + [$r]')
    REPORT_COUNT=$((REPORT_COUNT + 1))
  done <<< "$FILE_REPORTS"
done

if [ "$REPORT_COUNT" -eq 0 ]; then
  echo "ERROR: No researcher output files found in $RUN_DIR" >&2
  echo "Run run-researcher.sh first." >&2
  exit 1
fi

echo "Reviewing $REPORT_COUNT reports..."
echo ""

VERIFIED=0
ESCALATED=0
FAILED=0
REVIEWS_JSON="[]"

for i in $(seq 0 $((REPORT_COUNT - 1))); do
  FINDING_ID=$(echo "$REPORTS_JSON" | jq -r ".[$i].finding_id")
  REPORT_PATH=$(echo "$REPORTS_JSON" | jq -r ".[$i].report_path")

  # T-04-05: Validate finding_id matches strict pattern
  if [[ ! "$FINDING_ID" =~ ^[A-Za-z]+-[0-9A-Za-z-]+$ ]]; then
    echo "ERROR: Invalid finding_id: $FINDING_ID" >&2
    FAILED=$((FAILED + 1))
    continue
  fi

  # T-04-02: Validate report_path starts with reports/(privacy|cybersecurity|ai-law)/
  if [[ ! "$REPORT_PATH" =~ ^reports/(privacy|cybersecurity|ai-law)/ ]]; then
    echo "ERROR: Invalid report path: $REPORT_PATH" >&2
    FAILED=$((FAILED + 1))
    continue
  fi

  echo "Reviewing finding $((i+1))/$REPORT_COUNT: $FINDING_ID"
  echo "  Report: $REPORT_PATH"

  ROUND=1
  IS_VERIFIED=false
  TOTAL_CLAIMS=0
  REMAINING_ISSUES="[]"

  while [ "$ROUND" -le 3 ]; do
    FEEDBACK_FILE="$RUN_DIR/reviewer-feedback-r${ROUND}-${FINDING_ID}.json"

    # Build reviewer prompt
    PROMPT="Review the report at $REPORT_PATH for finding $FINDING_ID."
    PROMPT="$PROMPT Pipeline run: $RUN_ID. Round: $ROUND."
    PROMPT="$PROMPT Write your feedback to: $FEEDBACK_FILE."

    if [ "$ROUND" -gt 1 ]; then
      PREV_REVISION="$RUN_DIR/researcher-revision-r$((ROUND-1))-${FINDING_ID}.json"
      if [ -f "$PREV_REVISION" ]; then
        PROMPT="$PROMPT Previous revision response at: $PREV_REVISION."
      fi
    fi

    # Invoke reviewer agent
    claude -p --agent reviewer \
      --output-format json \
      --permission-mode acceptEdits \
      --max-turns 25 \
      "$PROMPT"

    # Check feedback file exists
    if [ ! -f "$FEEDBACK_FILE" ]; then
      echo "  WARNING: Reviewer did not produce feedback for $FINDING_ID round $ROUND" >&2
      break
    fi

    # T-04-01: Validate feedback against schema
    if ! jq -e -f "$PROJECT_ROOT/pipeline/schemas/reviewer-feedback.jq" "$FEEDBACK_FILE" >/dev/null 2>&1; then
      echo "  WARNING: Feedback validation failed for $FINDING_ID round $ROUND" >&2
      break
    fi

    # Track claims checked
    ROUND_CLAIMS=$(jq '.claims_checked' "$FEEDBACK_FILE")
    if [ "$ROUND_CLAIMS" -gt "$TOTAL_CLAIMS" ]; then
      TOTAL_CLAIMS=$ROUND_CLAIMS
    fi

    # D-06: Check for critical/major issues
    CRITICAL_MAJOR=$(jq '[.issues[] | select(.severity == "critical" or .severity == "major")] | length' "$FEEDBACK_FILE")

    if [ "$CRITICAL_MAJOR" -eq 0 ]; then
      echo "  Round $ROUND: Resolved for $FINDING_ID (minor issues only)"
      IS_VERIFIED=true
      REMAINING_ISSUES=$(jq '[.issues[] | select(.severity == "minor")]' "$FEEDBACK_FILE")
      break
    fi

    echo "  Round $ROUND: $CRITICAL_MAJOR critical/major issues for $FINDING_ID"

    # D-09: If round 3, escalate
    if [ "$ROUND" -eq 3 ]; then
      echo "  Escalating $FINDING_ID after 3 rounds"
      "$SCRIPT_DIR/generate-escalation.sh" "$RUN_ID" "$FINDING_ID" "$REPORT_PATH"
      REMAINING_ISSUES=$(jq '[.issues[] | select(.status == "open" or .status == "upheld")]' "$FEEDBACK_FILE")
      break
    fi

    # Invoke researcher for revision
    REVISION_FILE="$RUN_DIR/researcher-revision-r${ROUND}-${FINDING_ID}.json"
    REVISION_PROMPT="Revise the report at $REPORT_PATH based on reviewer feedback."
    REVISION_PROMPT="$REVISION_PROMPT Read feedback at: $FEEDBACK_FILE."
    REVISION_PROMPT="$REVISION_PROMPT Address each issue. Write revision response to: $REVISION_FILE."
    REVISION_PROMPT="$REVISION_PROMPT Pipeline run: $RUN_ID. Round: $ROUND."

    claude -p --agent researcher \
      --output-format json \
      --permission-mode acceptEdits \
      --max-turns 20 \
      "$REVISION_PROMPT"

    if [ ! -f "$REVISION_FILE" ]; then
      echo "  WARNING: Researcher did not produce revision response for $FINDING_ID round $ROUND" >&2
      break
    fi

    ROUND=$((ROUND + 1))
  done

  # Build per-finding review result
  if [ "$IS_VERIFIED" = true ]; then
    STATUS="verified"
    VERIFIED=$((VERIFIED + 1))
  elif [ "$ROUND" -ge 3 ]; then
    STATUS="needs-human-review"
    ESCALATED=$((ESCALATED + 1))
  else
    STATUS="disputed"
    FAILED=$((FAILED + 1))
  fi

  # Build issues_found array for the envelope (simplified format)
  ISSUES_FOUND=$(echo "$REMAINING_ISSUES" | jq '[.[] | {claim: .claim, issue: .issue, severity: .severity}]')

  REVIEW_ENTRY=$(jq -n \
    --arg fid "$FINDING_ID" \
    --arg rp "$REPORT_PATH" \
    --arg st "$STATUS" \
    --argjson ic "$ROUND" \
    --argjson cc "$TOTAL_CLAIMS" \
    --argjson iss "$ISSUES_FOUND" \
    '{
      finding_id: $fid,
      report_path: $rp,
      status: $st,
      iteration_count: $ic,
      claims_checked: $cc,
      issues_found: $iss
    }')

  REVIEWS_JSON=$(echo "$REVIEWS_JSON" | jq --argjson entry "$REVIEW_ENTRY" '. + [$entry]')
  echo ""
done

# Determine overall status
# D-11: If all verified, auto-pass to categorizer
if [ "$ESCALATED" -eq 0 ] && [ "$FAILED" -eq 0 ]; then
  OVERALL_STATUS="complete"
else
  OVERALL_STATUS="pending-review"
fi

# Build final reviewer output envelope
jq -n \
  --arg run_id "$RUN_ID" \
  --arg status "$OVERALL_STATUS" \
  --argjson reviews "$REVIEWS_JSON" \
  '{
    schema_version: "1.0",
    pipeline_run_id: $run_id,
    timestamp: (now | todate),
    stage: "reviewer",
    status: $status,
    data: { reviews: $reviews }
  }' > "$RUN_DIR/reviewer-output.json"

# Validate output envelope
"$PROJECT_ROOT/pipeline/scripts/validate-handoff.sh" reviewer "$RUN_DIR/reviewer-output.json"

# Print summary
echo "Review complete."
echo "  Verified: $VERIFIED / $REPORT_COUNT"
if [ "$ESCALATED" -gt 0 ]; then
  echo "  Escalated: $ESCALATED (needs human review)"
fi
if [ "$FAILED" -gt 0 ]; then
  echo "  Failed: $FAILED"
fi

echo ""
if [ "$OVERALL_STATUS" = "complete" ]; then
  echo "Next: Run categorizer agent."
else
  echo "Next: Resolve escalations in $RUN_DIR/reviewer-escalation-*.md (JSON gate files: escalation-*.json)"
  echo "Then run: approve-escalation.sh $RUN_ID <finding-id>"
fi
