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

# Idempotency: load the prior run's reviewer-output.json (if any) so we can
# reuse reports that already reached a terminal outcome and only re-review those
# that did not. A report is "terminal" if it was verified, or if it produced a
# genuine escalation gate file (escalation-<id>.json). Reports left as
# needs-human-review WITHOUT an escalation file are the ones a prior run failed
# to actually review (e.g. rate-limited reviewers that emitted no feedback) —
# those get re-reviewed. This lets a re-run after a partial failure re-review
# only the gap instead of redoing every report (and re-incurring the cost / rate
# limit that caused the gap).
PRIOR_REVIEWS="[]"
if [ -f "$RUN_DIR/reviewer-output.json" ]; then
  PRIOR_REVIEWS=$(jq -c '.data.reviews // []' "$RUN_DIR/reviewer-output.json" 2>/dev/null || echo "[]")
fi

# Clear the aggregate escalation marker up front; it is re-touched below for each
# reused-or-freshly escalated report so it reflects only the current run's state.
rm -f "$RUN_DIR/has-escalations.marker"

# Remove checkpoint temp files left behind by a prior run that was SIGKILLed
# mid-write (the stage timeout kills the whole process group, so no trap runs).
rm -f "$RUN_DIR"/.reviewer-output.*

# Write the reviewer output envelope atomically.
#
# Called after EVERY finding as a checkpoint, not just once at the end. A run
# killed part-way (stage timeout, rate limit, reboot) previously left its
# completed reviews invisible to the next run -- the resume path reads terminal
# outcomes only from this file -- so everything was re-reviewed from scratch.
#
# Entries are merged with PRIOR_REVIEWS so a mid-loop checkpoint cannot shrink
# the file: reports the loop has not reached yet keep their prior terminal
# result. Current-run entries win on conflict.
write_reviewer_output() {
  local status="$1"
  local tmp merged
  tmp=$(mktemp "$RUN_DIR/.reviewer-output.XXXXXX") || return 0
  merged=$(jq -n --argjson prior "$PRIOR_REVIEWS" --argjson cur "$REVIEWS_JSON" \
    '($prior + $cur) | group_by(.finding_id) | map(.[-1])' 2>/dev/null) || merged=""
  if [ -z "$merged" ]; then
    rm -f "$tmp"
    echo "  WARNING: could not merge reviewer-output.json checkpoint" >&2
    return 0
  fi
  if jq -n \
      --arg run_id "$RUN_ID" \
      --arg status "$status" \
      --argjson reviews "$merged" \
      '{
        schema_version: "1.0",
        pipeline_run_id: $run_id,
        timestamp: (now | todate),
        stage: "reviewer",
        status: $status,
        data: { reviews: $reviews }
      }' > "$tmp" 2>/dev/null; then
    mv -f "$tmp" "$RUN_DIR/reviewer-output.json"
  else
    rm -f "$tmp"
    echo "  WARNING: could not checkpoint reviewer-output.json" >&2
  fi
  return 0
}

VERIFIED=0
ESCALATED=0
FAILED=0
REUSED=0
REVIEWS_JSON="[]"

for i in $(seq 0 $((REPORT_COUNT - 1))); do
  FINDING_ID=$(echo "$REPORTS_JSON" | jq -r ".[$i].finding_id")
  REPORT_PATH=$(echo "$REPORTS_JSON" | jq -r ".[$i].report_path")
  OPERATION=$(echo "$REPORTS_JSON" | jq -r ".[$i].operation // \"\"")

  # T-04-05: Validate finding_id matches strict pattern
  if [[ ! "$FINDING_ID" =~ ^[A-Za-z]+-[0-9A-Za-z-]+$ ]]; then
    echo "ERROR: Invalid finding_id: $FINDING_ID" >&2
    FAILED=$((FAILED + 1))
    continue
  fi

  # T-04-02: full reports must live under reports/{privacy,cybersecurity,ai-law}/.
  # Update entries (append_update) may also target tracked-bill files under bills/.
  if [ "$OPERATION" = "append_update" ]; then
    if [[ ! "$REPORT_PATH" =~ ^(reports/(privacy|cybersecurity|ai-law)|bills)/ ]]; then
      echo "ERROR: Invalid update report path: $REPORT_PATH" >&2
      FAILED=$((FAILED + 1))
      continue
    fi
  elif [[ ! "$REPORT_PATH" =~ ^reports/(privacy|cybersecurity|ai-law)/ ]]; then
    echo "ERROR: Invalid report path: $REPORT_PATH" >&2
    FAILED=$((FAILED + 1))
    continue
  fi

  # Idempotency skip: reuse a prior terminal result verbatim (no claude call).
  PRIOR_ENTRY=$(echo "$PRIOR_REVIEWS" | jq -c --arg fid "$FINDING_ID" 'map(select(.finding_id == $fid)) | .[0] // empty')
  if [ -n "$PRIOR_ENTRY" ]; then
    PRIOR_STATUS=$(echo "$PRIOR_ENTRY" | jq -r '.status // ""')
    if [ "$PRIOR_STATUS" = "verified" ]; then
      echo "Skipping $((i+1))/$REPORT_COUNT: $FINDING_ID — reusing prior verified result"
      REVIEWS_JSON=$(echo "$REVIEWS_JSON" | jq --argjson e "$PRIOR_ENTRY" '. + [$e]')
      VERIFIED=$((VERIFIED + 1)); REUSED=$((REUSED + 1))
      continue
    elif [ -f "$RUN_DIR/escalation-${FINDING_ID}.json" ] && \
         [ "$(jq -r '.review_failed // false' "$RUN_DIR/escalation-${FINDING_ID}.json" 2>/dev/null)" != "true" ]; then
      # Genuine escalation: a reviewer reached a verdict it could not resolve.
      # A gate marked review_failed:true is NOT terminal -- the reviewer never
      # returned a verdict there, so it falls through and gets re-reviewed.
      echo "Skipping $((i+1))/$REPORT_COUNT: $FINDING_ID — reusing prior escalation"
      REVIEWS_JSON=$(echo "$REVIEWS_JSON" | jq --argjson e "$PRIOR_ENTRY" '. + [$e]')
      ESCALATED=$((ESCALATED + 1)); REUSED=$((REUSED + 1))
      touch "$RUN_DIR/has-escalations.marker"
      continue
    fi
    # else: prior was non-terminal (e.g. rate-limited, no feedback/escalation) —
    # fall through and re-review it.
  fi

  if [ "$OPERATION" = "append_update" ]; then
    echo "Reviewing UPDATE $((i+1))/$REPORT_COUNT: $FINDING_ID (single-pass)"
    # A fresh verdict supersedes any stale escalation gate from a prior run
    rm -f "$RUN_DIR/escalation-${FINDING_ID}.json"
    FEEDBACK_FILE="$RUN_DIR/reviewer-feedback-r1-${FINDING_ID}.json"
    PROMPT="Single-pass update review for finding $FINDING_ID (operation append_update)."
    PROMPT="$PROMPT Review the appended update in $REPORT_PATH."
    PROMPT="$PROMPT Pipeline run: $RUN_ID. Round: 1. This is an append_update entry:"
    PROMPT="$PROMPT do NOT iterate; apply pipeline/config/update-review-policy.json once."
    PROMPT="$PROMPT Write your feedback to: $FEEDBACK_FILE."

    # Guard against `set -e`: the claude CLI sometimes exits nonzero even when
    # the session completed cleanly. The feedback-file existence + schema check
    # below is the real success signal, so a nonzero exit here must NOT abort
    # the whole batch (this is what killed the run at finding 009).
    claude -p --agent reviewer \
      --output-format json \
      --permission-mode acceptEdits \
      --max-turns 15 \
      "$PROMPT" || true

    VERDICT="needs-human-review"
    VERDICT_REASON="Reviewer produced no valid feedback"
    UPDATE_ISSUES="[]"
    UPDATE_CLAIMS=0
    if [ -f "$FEEDBACK_FILE" ] && jq -e -f "$PROJECT_ROOT/pipeline/schemas/reviewer-feedback.jq" "$FEEDBACK_FILE" >/dev/null 2>&1; then
      UPDATE_CLAIMS=$(jq '.claims_checked' "$FEEDBACK_FILE")
      # Count only UNRESOLVED critical/major issues (status open/upheld). Issues
      # the researcher already fixed ("fixed"/"disputed"/"withdrawn") must not
      # block verification or trigger an escalation — otherwise a report whose
      # issues were all resolved still escalates, and generate-escalation.sh
      # (which filters on open/upheld) then finds nothing to write, orphaning it.
      CRITICAL_MAJOR=$(jq '[.issues[] | select((.severity == "critical" or .severity == "major") and (.status == "open" or .status == "upheld"))] | length' "$FEEDBACK_FILE")
      if [ "$CRITICAL_MAJOR" -eq 0 ]; then
        VERDICT="auto_approved"
        VERDICT_REASON="No critical/major issues in single-pass update review"
        STATUS="verified"
        VERIFIED=$((VERIFIED + 1))
      else
        VERDICT_REASON="$CRITICAL_MAJOR critical/major issue(s) in update review"
        STATUS="needs-human-review"
        ESCALATED=$((ESCALATED + 1))
        UPDATE_ISSUES=$(jq '[.issues[] | {claim: .claim, issue: .issue, severity: .severity}]' "$FEEDBACK_FILE")
        jq -n \
          --arg run_id "$RUN_ID" \
          --arg finding_id "$FINDING_ID" \
          --arg report_path "$REPORT_PATH" \
          --argjson unresolved "$UPDATE_ISSUES" \
          '{
            run_id: $run_id,
            finding_id: $finding_id,
            report_path: $report_path,
            escalation_md: "",
            rounds_completed: 1,
            unresolved_issues: $unresolved,
            resolved: false
          }' > "$RUN_DIR/escalation-${FINDING_ID}.json"
        touch "$RUN_DIR/has-escalations.marker"
      fi
      UPDATE_ISSUES=$(jq '[.issues[] | {claim: .claim, issue: .issue, severity: .severity}]' "$FEEDBACK_FILE")
    else
      STATUS="needs-human-review"
      ESCALATED=$((ESCALATED + 1))
      jq -n \
        --arg run_id "$RUN_ID" \
        --arg finding_id "$FINDING_ID" \
        --arg report_path "$REPORT_PATH" \
        '{
          run_id: $run_id,
          finding_id: $finding_id,
          report_path: $report_path,
          escalation_md: "",
          rounds_completed: 1,
          unresolved_issues: [],
          resolved: false
        }' > "$RUN_DIR/escalation-${FINDING_ID}.json"
      touch "$RUN_DIR/has-escalations.marker"
    fi

    REVIEW_ENTRY=$(jq -n \
      --arg fid "$FINDING_ID" --arg rp "$REPORT_PATH" --arg st "$STATUS" \
      --arg v "$VERDICT" --arg vr "$VERDICT_REASON" \
      --argjson cc "$UPDATE_CLAIMS" --argjson iss "$UPDATE_ISSUES" \
      '{
        finding_id: $fid, report_path: $rp, status: $st,
        operation: "append_update", verdict: $v, verdict_reason: $vr,
        iteration_count: 1, claims_checked: $cc, issues_found: $iss
      }')
    REVIEWS_JSON=$(echo "$REVIEWS_JSON" | jq --argjson entry "$REVIEW_ENTRY" '. + [$entry]')
    echo ""
    continue
  fi

  echo "Reviewing finding $((i+1))/$REPORT_COUNT: $FINDING_ID"
  # A fresh verdict supersedes any stale escalation gate from a prior run
  rm -f "$RUN_DIR/escalation-${FINDING_ID}.json"
  echo "  Report: $REPORT_PATH"

  ROUND=1
  IS_VERIFIED=false
  TOTAL_CLAIMS=0
  REMAINING_ISSUES="[]"
  # True when the round loop ended because the reviewer produced nothing usable
  # (no feedback file, or feedback that failed schema validation) rather than
  # because it reached a verdict. Such a report was never actually fact-checked.
  REVIEW_FAILED=false
  # True only when the round-3 escalation branch ran on VALID reviewer feedback.
  # The verdict block below must not infer this from ROUND alone: a reviewer
  # that produced no/invalid feedback in round 3 leaves ROUND=3 too, and that
  # case is a review FAILURE (retryable), not a genuine escalation.
  ESCALATED_AFTER_ROUNDS=false

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

    # Invoke reviewer agent. Guard against `set -e`: claude may exit nonzero
    # despite a clean session; the feedback-file check below is the real signal.
    # max-turns 40: the reviewer runs on opus (Opus 5) whose turns are more
    # deliberate; 25 was tuned for sonnet and truncated full reviews.
    claude -p --agent reviewer \
      --output-format json \
      --permission-mode acceptEdits \
      --max-turns 40 \
      "$PROMPT" || true

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

    # D-06: Check for critical/major issues.
    # Count only UNRESOLVED ones (status open/upheld) — same rule as the
    # append_update branch above. Issues the researcher already addressed
    # ("fixed"/"disputed"/"withdrawn") must not force another round or an
    # escalation; otherwise a report whose issues were all resolved still
    # burns three rounds and escalates with nothing actionable in the gate.
    CRITICAL_MAJOR=$(jq '[.issues[] | select((.severity == "critical" or .severity == "major") and (.status == "open" or .status == "upheld"))] | length' "$FEEDBACK_FILE")

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
      ESCALATED_AFTER_ROUNDS=true
      "$SCRIPT_DIR/generate-escalation.sh" "$RUN_ID" "$FINDING_ID" "$REPORT_PATH" \
        || echo "  WARNING: generate-escalation.sh failed for $FINDING_ID" >&2
      touch "$RUN_DIR/has-escalations.marker"
      REMAINING_ISSUES=$(jq '[.issues[] | select(.status == "open" or .status == "upheld")]' "$FEEDBACK_FILE")
      break
    fi

    # Invoke researcher for revision
    REVISION_FILE="$RUN_DIR/researcher-revision-r${ROUND}-${FINDING_ID}.json"
    REVISION_PROMPT="Revise the report at $REPORT_PATH based on reviewer feedback."
    REVISION_PROMPT="$REVISION_PROMPT Read feedback at: $FEEDBACK_FILE."
    REVISION_PROMPT="$REVISION_PROMPT Address each issue. Write revision response to: $REVISION_FILE."
    REVISION_PROMPT="$REVISION_PROMPT Pipeline run: $RUN_ID. Round: $ROUND."

    # Guard against `set -e`: the revision-file check below is the real signal.
    claude -p --agent researcher \
      --output-format json \
      --permission-mode acceptEdits \
      --max-turns 20 \
      "$REVISION_PROMPT" || true

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
  elif [ "$ESCALATED_AFTER_ROUNDS" = true ]; then
    # Genuine three-round escalation: the round-3 reviewer returned valid
    # feedback with unresolved critical/major issues. (Checking ROUND >= 3
    # here was wrong — a reviewer that failed to produce feedback in round 3
    # also leaves ROUND=3, and that case must fall through to REVIEW_FAILED
    # so the resume path retries it instead of treating it as terminal.)
    STATUS="needs-human-review"
    ESCALATED=$((ESCALATED + 1))
  else
    # Reviewer produced no usable feedback (missing/invalid, or claude failed).
    # Surface it as an escalation so the categorizer does not silently drop the
    # report — the pipeline must never lose a report without human sign-off.
    # But mark it as a review FAILURE, not a verdict: the report was never
    # fact-checked, so a later run must retry it rather than treat it as done.
    STATUS="needs-human-review"
    REVIEW_FAILED=true
    FAILED=$((FAILED + 1))
    touch "$RUN_DIR/has-escalations.marker"
  fi

  # Guarantee an escalation gate file for any needs-human-review outcome so the
  # human resolution flow always has a gate to act on. generate-escalation.sh
  # writes a richer one when it can; this is the floor.
  #
  # The gate records review_failed and the round actually reached. A gate with
  # review_failed:true means the reviewer never returned a verdict, so the
  # resume path retries it instead of treating it as terminal. Without that
  # distinction a transient rate limit is indistinguishable from a genuine
  # three-round escalation and the report is never fact-checked at all --
  # exactly what happened to 11 reports on run 2026-07-25T18-29-52.
  if [ "$STATUS" = "needs-human-review" ] && [ ! -f "$RUN_DIR/escalation-${FINDING_ID}.json" ]; then
    GATE_ISSUES=$(echo "$REMAINING_ISSUES" | jq '[.[] | {claim: .claim, issue: .issue, severity: .severity}]' 2>/dev/null || echo "[]")
    jq -n --arg run_id "$RUN_ID" --arg fid "$FINDING_ID" --arg rp "$REPORT_PATH" \
      --argjson unresolved "$GATE_ISSUES" --argjson rounds "$ROUND" \
      --argjson failed "$REVIEW_FAILED" \
      '{run_id: $run_id, finding_id: $fid, report_path: $rp, escalation_md: "",
        rounds_completed: $rounds, unresolved_issues: $unresolved,
        review_failed: $failed, resolved: false}' \
      > "$RUN_DIR/escalation-${FINDING_ID}.json"
    touch "$RUN_DIR/has-escalations.marker"
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

  # Checkpoint: make this finding's outcome durable before starting the next
  # one, so an interrupted run resumes instead of restarting.
  write_reviewer_output "pending-review"

  echo ""
done

# Determine overall status
# D-11: If all verified, auto-pass to categorizer
if [ "$ESCALATED" -eq 0 ] && [ "$FAILED" -eq 0 ]; then
  OVERALL_STATUS="complete"
else
  OVERALL_STATUS="pending-review"
fi

# Final envelope: same writer, now with the run's real overall status.
write_reviewer_output "$OVERALL_STATUS"

# Validate output envelope
"$PROJECT_ROOT/pipeline/scripts/validate-handoff.sh" reviewer "$RUN_DIR/reviewer-output.json"

# Print summary
echo "Review complete."
echo "  Verified: $VERIFIED / $REPORT_COUNT"
if [ "$REUSED" -gt 0 ]; then
  echo "  Reused from prior run (not re-reviewed): $REUSED"
fi
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
