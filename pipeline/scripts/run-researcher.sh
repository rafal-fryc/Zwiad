#!/bin/bash
set -euo pipefail

# LEGACY: This script is the standalone CLI alternative to invoking the
# researcher via Discord. The production runtime (discord_bot.py /research +
# orchestrator Mode 2) bypasses this script entirely. Kept for ad-hoc CLI use
# and legacy pytest fixtures (tests/test-approval-gate.sh).
#
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

  # Invoke researcher agent (T-03-06: --max-turns 30 limits execution).
  # Guard against `set -e`: the claude CLI sometimes exits nonzero even when
  # the session completed cleanly — the output-file check below is the real
  # success signal (same guard as run-reviewer.sh). timeout(1) bounds a hang.
  timeout 3600 claude -p --agent researcher --output-format json \
    --max-turns 30 \
    "$PROMPT" || true

  OUTPUT="$RUN_DIR/researcher-$FINDING_ID.json"

  # Check output file exists
  if [ ! -f "$OUTPUT" ]; then
    echo "WARNING: Researcher did not produce output for $FINDING_ID at $OUTPUT" >&2
    FAILED=$((FAILED + 1))
    continue
  fi

  # Validate against schema. Per-finding isolation: quarantine the bad output
  # (so a re-run retries it) and continue — one invalid envelope must not
  # abort the rest of the batch.
  if ! "$PROJECT_ROOT/pipeline/scripts/validate-handoff.sh" researcher "$OUTPUT"; then
    echo "WARNING: Validation failed for $FINDING_ID — quarantining output, continuing" >&2
    mv "$OUTPUT" "$OUTPUT.rejected"
    FAILED=$((FAILED + 1))
    continue
  fi

  # T-03-03 mitigation: validate report_path. Full reports must live under
  # reports/{privacy,cybersecurity,ai-law}/; append_update entries may also
  # target tracked-bill files under bills/ (same rule as run-reviewer.sh).
  REPORT_PATH=$(jq -r '.data.reports[0].report_path // ""' "$OUTPUT")
  OPERATION=$(jq -r '.data.reports[0].operation // ""' "$OUTPUT")
  if [ "$OPERATION" = "append_update" ]; then
    PATH_RE='^(reports/(privacy|cybersecurity|ai-law)|bills)/'
  else
    PATH_RE='^reports/(privacy|cybersecurity|ai-law)/'
  fi
  if [ -n "$REPORT_PATH" ] && [[ ! "$REPORT_PATH" =~ $PATH_RE ]]; then
    echo "WARNING: Invalid report path for $FINDING_ID: $REPORT_PATH — quarantining, continuing" >&2
    mv "$OUTPUT" "$OUTPUT.rejected"
    FAILED=$((FAILED + 1))
    continue
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
