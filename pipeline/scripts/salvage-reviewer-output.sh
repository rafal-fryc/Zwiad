#!/bin/bash
# Reconstruct reviewer-output.json from the per-finding artifacts already on
# disk (reviewer-feedback-r*.json + escalation-*.json).
#
# Why this exists: run-reviewer.sh writes reviewer-output.json only after its
# whole loop finishes, and its resume path reads terminal outcomes ONLY from
# that file. A run killed part-way (e.g. by the stage timeout) therefore leaves
# hours of completed reviews on disk that the next run cannot see, so it
# re-reviews everything from scratch. This rebuilds the file so a re-run skips
# what is already terminal.
#
# Terminal-state rules mirror run-reviewer.sh exactly:
#   - highest round whose feedback validates, with 0 critical/major issues
#       -> "verified", issues_found = the minor issues
#   - round 3 reached with critical/major issues still open
#       -> "needs-human-review", issues_found = issues with status open|upheld
#   - anything else (mid-iteration, missing/invalid feedback)
#       -> omitted, so the next run re-reviews it
#
# Usage: salvage-reviewer-output.sh <run_id> [--stdout] [--force]

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

RUN_ID="${1:-}"
if [ -z "$RUN_ID" ]; then
  echo "Usage: $0 <run_id> [--stdout] [--force]" >&2
  exit 1
fi
shift

TO_STDOUT=false
FORCE=false
for arg in "$@"; do
  case "$arg" in
    --stdout) TO_STDOUT=true ;;
    --force)  FORCE=true ;;
    *) echo "Unknown option: $arg" >&2; exit 1 ;;
  esac
done

RUN_DIR="$PROJECT_ROOT/pipeline/runs/$RUN_ID"
if [ ! -d "$RUN_DIR" ]; then
  echo "ERROR: run directory not found: $RUN_DIR" >&2
  exit 1
fi

# Refuse to clobber the output while a reviewer run is live -- it would race
# with that run's own end-of-loop write.
if [ "$TO_STDOUT" = false ] && [ "$FORCE" = false ]; then
  if pgrep -f "run-reviewer.sh $RUN_ID" >/dev/null 2>&1; then
    echo "ERROR: run-reviewer.sh is still running for $RUN_ID." >&2
    echo "Wait for it to exit, or pass --stdout to preview, or --force to override." >&2
    exit 1
  fi
fi

REVIEWS_JSON="[]"
VERIFIED=0
ESCALATED=0
SKIPPED=0

for RESEARCHER_FILE in "$RUN_DIR"/researcher-*.json; do
  [ -f "$RESEARCHER_FILE" ] || continue
  BASENAME=$(basename "$RESEARCHER_FILE")
  # Revision files are per-round artifacts, not report definitions.
  if [[ "$BASENAME" =~ ^researcher-revision- ]]; then
    continue
  fi

  FILE_REPORTS=$(jq -c 'if .data.reports then .data.reports[] else .data | select(.finding_id) end' \
    "$RESEARCHER_FILE" 2>/dev/null || true)

  while IFS= read -r report; do
    [ -z "$report" ] && continue
    FINDING_ID=$(echo "$report" | jq -r '.finding_id')
    REPORT_PATH=$(echo "$report" | jq -r '.report_path')
    [ -z "$FINDING_ID" ] || [ "$FINDING_ID" = "null" ] && continue

    # Walk rounds ascending; the script breaks out of its loop at the first
    # terminal round, so the first terminal round we find is the outcome.
    STATUS=""
    ITERATION=0
    TOTAL_CLAIMS=0
    ISSUES="[]"

    for ROUND in 1 2 3; do
      FB="$RUN_DIR/reviewer-feedback-r${ROUND}-${FINDING_ID}.json"
      [ -f "$FB" ] || break
      # Same schema gate the reviewer script applies before trusting feedback.
      if ! jq -e -f "$PROJECT_ROOT/pipeline/schemas/reviewer-feedback.jq" "$FB" >/dev/null 2>&1; then
        break
      fi

      ROUND_CLAIMS=$(jq '.claims_checked // 0' "$FB" 2>/dev/null || echo 0)
      if [ "$ROUND_CLAIMS" -gt "$TOTAL_CLAIMS" ]; then
        TOTAL_CLAIMS=$ROUND_CLAIMS
      fi
      ITERATION=$ROUND

      # Count only UNRESOLVED critical/major issues (status open/upheld) — must
      # stay in lockstep with the same expression in run-reviewer.sh.
      CRITICAL_MAJOR=$(jq '[.issues[] | select((.severity == "critical" or .severity == "major") and (.status == "open" or .status == "upheld"))] | length' "$FB")
      if [ "$CRITICAL_MAJOR" -eq 0 ]; then
        STATUS="verified"
        ISSUES=$(jq '[.issues[] | select(.severity == "minor") | {claim, issue, severity}]' "$FB")
        break
      fi

      if [ "$ROUND" -eq 3 ]; then
        STATUS="needs-human-review"
        ISSUES=$(jq '[.issues[] | select(.status == "open" or .status == "upheld") | {claim, issue, severity}]' "$FB")
        break
      fi

      # Not terminal: the script only advances to round N+1 after the
      # researcher produced a revision response. Without it, the run stopped
      # here and this finding is not terminal.
      if [ ! -f "$RUN_DIR/researcher-revision-r${ROUND}-${FINDING_ID}.json" ]; then
        STATUS=""
        break
      fi
    done

    # A needs-human-review entry is only reusable by run-reviewer.sh when its
    # escalation gate file exists -- that is the condition its skip path tests.
    if [ "$STATUS" = "needs-human-review" ] && [ ! -f "$RUN_DIR/escalation-${FINDING_ID}.json" ]; then
      STATUS=""
    fi

    if [ -z "$STATUS" ]; then
      SKIPPED=$((SKIPPED + 1))
      continue
    fi

    if [ "$STATUS" = "verified" ]; then
      VERIFIED=$((VERIFIED + 1))
    else
      ESCALATED=$((ESCALATED + 1))
    fi

    ENTRY=$(jq -n \
      --arg fid "$FINDING_ID" --arg rp "$REPORT_PATH" --arg st "$STATUS" \
      --argjson ic "$ITERATION" --argjson cc "$TOTAL_CLAIMS" --argjson iss "$ISSUES" \
      '{finding_id: $fid, report_path: $rp, status: $st,
        iteration_count: $ic, claims_checked: $cc, issues_found: $iss}')
    REVIEWS_JSON=$(echo "$REVIEWS_JSON" | jq --argjson e "$ENTRY" '. + [$e]')
  done <<< "$FILE_REPORTS"
done

# Salvage always reflects an incomplete run (that is why it is being salvaged),
# so the envelope stays pending-review unless everything terminal is verified
# and nothing was left unreviewed.
if [ "$ESCALATED" -eq 0 ] && [ "$SKIPPED" -eq 0 ]; then
  OVERALL_STATUS="complete"
else
  OVERALL_STATUS="pending-review"
fi

ENVELOPE=$(jq -n \
  --arg run_id "$RUN_ID" --arg status "$OVERALL_STATUS" --argjson reviews "$REVIEWS_JSON" \
  '{schema_version: "1.0", pipeline_run_id: $run_id, timestamp: (now | todate),
    stage: "reviewer", status: $status, data: {reviews: $reviews}}')

if [ "$TO_STDOUT" = true ]; then
  echo "$ENVELOPE"
  echo "Salvaged: $VERIFIED verified, $ESCALATED escalated, $SKIPPED not terminal (will be re-reviewed)." >&2
  exit 0
fi

OUT="$RUN_DIR/reviewer-output.json"
TMP=$(mktemp "$RUN_DIR/.reviewer-output.XXXXXX")
echo "$ENVELOPE" > "$TMP"

if ! "$PROJECT_ROOT/pipeline/scripts/validate-handoff.sh" reviewer "$TMP"; then
  echo "ERROR: salvaged envelope failed validation; leaving $OUT untouched." >&2
  echo "       Rejected envelope kept at $TMP for inspection." >&2
  exit 1
fi

mv "$TMP" "$OUT"
echo "Wrote $OUT"
echo "  Verified:                 $VERIFIED"
echo "  Escalated:                $ESCALATED"
echo "  Not terminal (re-review): $SKIPPED"
