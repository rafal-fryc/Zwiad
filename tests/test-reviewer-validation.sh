#!/bin/bash
set -euo pipefail

# Test reviewer feedback schema validation and content structure
# Covers: VERF-01 (claims supported by sources), VERF-02 (legal accuracy fields)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

PASS=0
FAIL=0

run_test() {
  local description="$1"
  local result="$2"
  if [ "$result" -eq 0 ]; then
    echo "PASS: $description"
    PASS=$((PASS + 1))
  else
    echo "FAIL: $description"
    FAIL=$((FAIL + 1))
  fi
}

echo "=== Reviewer Validation Tests ==="
echo ""

# ---------------------------------------------------------------------------
# VERF-01: Source-backed claims (feedback schema)
# ---------------------------------------------------------------------------
echo "--- VERF-01: Source verification structure ---"

# Test 1: Feedback fixture passes jq schema validation
jq -e -f "$PROJECT_ROOT/pipeline/schemas/reviewer-feedback.jq" "$PROJECT_ROOT/tests/fixtures/sample-reviewer-feedback.json" > /dev/null 2>&1
run_test "Feedback fixture passes jq schema validation" $?

# Test 2: Feedback has required fields
jq -e '
  .finding_id and .report_path and (.round | type == "number") and
  (.claims_checked | type == "number") and (.issues | type == "array") and
  .resolution_status
' "$PROJECT_ROOT/tests/fixtures/sample-reviewer-feedback.json" > /dev/null 2>&1
run_test "Feedback has all required fields" $?

# Test 3: Each issue has source_url field (string type)
MISSING_URL=$(jq '[.issues[] | select(.source_url | type != "string")] | length' "$PROJECT_ROOT/tests/fixtures/sample-reviewer-feedback.json")
if [ "$MISSING_URL" -eq 0 ]; then
  run_test "Each issue has source_url field" 0
else
  run_test "Each issue has source_url field (missing: $MISSING_URL)" 1
fi

# Test 4: Each issue has claim and issue description (non-empty strings)
MISSING_CLAIM=$(jq '[.issues[] | select((.claim | length) == 0 or (.issue | length) == 0)] | length' "$PROJECT_ROOT/tests/fixtures/sample-reviewer-feedback.json")
if [ "$MISSING_CLAIM" -eq 0 ]; then
  run_test "Each issue has claim and issue description" 0
else
  run_test "Each issue has claim and issue description (missing: $MISSING_CLAIM)" 1
fi

# Test 5: Reviewer output envelope passes schema validation
bash "$PROJECT_ROOT/pipeline/scripts/validate-handoff.sh" reviewer "$PROJECT_ROOT/tests/fixtures/sample-reviewer-output.json" > /dev/null 2>&1
run_test "Reviewer output envelope passes schema validation" $?

echo ""

# ---------------------------------------------------------------------------
# VERF-02: Legal accuracy fields
# ---------------------------------------------------------------------------
echo "--- VERF-02: Legal accuracy fields ---"

# Test 6: Feedback severity includes critical for factual errors
HAS_CRITICAL=$(jq '[.issues[] | select(.severity == "critical")] | length > 0' "$PROJECT_ROOT/tests/fixtures/sample-reviewer-feedback.json")
if [ "$HAS_CRITICAL" = "true" ]; then
  run_test "Feedback severity includes critical for factual errors" 0
else
  run_test "Feedback severity includes critical for factual errors" 1
fi

# Test 7: Feedback has suggested_fix for each issue (non-empty)
MISSING_FIX=$(jq '[.issues[] | select((.suggested_fix | length) == 0)] | length' "$PROJECT_ROOT/tests/fixtures/sample-reviewer-feedback.json")
if [ "$MISSING_FIX" -eq 0 ]; then
  run_test "Each issue has suggested_fix" 0
else
  run_test "Each issue has suggested_fix (missing: $MISSING_FIX)" 1
fi

# Test 8: Issues have section field for traceability
MISSING_SECTION=$(jq '[.issues[] | select((.section | length) == 0)] | length' "$PROJECT_ROOT/tests/fixtures/sample-reviewer-feedback.json")
if [ "$MISSING_SECTION" -eq 0 ]; then
  run_test "Issues have section field for traceability" 0
else
  run_test "Issues have section field for traceability (missing: $MISSING_SECTION)" 1
fi

# Test 9: Reviewer output has claims_checked count >= 0
INVALID_CC=$(jq '[.data.reviews[] | select(.claims_checked < 0)] | length' "$PROJECT_ROOT/tests/fixtures/sample-reviewer-output.json")
if [ "$INVALID_CC" -eq 0 ]; then
  run_test "Reviewer output has valid claims_checked counts" 0
else
  run_test "Reviewer output has valid claims_checked counts (invalid: $INVALID_CC)" 1
fi

# Test 10: Reviewer output status enum is valid
INVALID_STATUS=$(jq '[.data.reviews[] | select(.status | IN("verified", "disputed", "needs-human-review") | not)] | length' "$PROJECT_ROOT/tests/fixtures/sample-reviewer-output.json")
if [ "$INVALID_STATUS" -eq 0 ]; then
  run_test "Reviewer output status enum is valid" 0
else
  run_test "Reviewer output status enum is valid (invalid: $INVALID_STATUS)" 1
fi

echo ""

# ---------------------------------------------------------------------------
# VERF-05: Robustness regressions from run 2026-07-17T13-54-18
# ---------------------------------------------------------------------------
echo "--- VERF-05: Reviewer robustness ---"

# Test: feedback whose issue has source_url=null (a genuinely UNSOURCED claim)
# must validate. A reviewer legitimately reports null source_url when the issue
# IS that the claim lacks a source; the old schema required a string and
# silently dropped these valid reviews (finding SCAN-20260717-007).
jq -e -f "$PROJECT_ROOT/pipeline/schemas/reviewer-feedback.jq" "$PROJECT_ROOT/tests/fixtures/sample-reviewer-feedback-null-source.json" > /dev/null 2>&1
run_test "Feedback with null source_url (unsourced-claim issue) validates" $?

# Test: run-reviewer.sh must guard its nested `claude -p` calls so a single
# nonzero exit (incl. claude's benign 'completed-but-nonzero' quirk) cannot
# abort the whole batch under 'set -e' (what killed the run at finding 009).
CLAUDE_CALLS=$(grep -cE '^\s*claude -p --agent (reviewer|researcher)' "$PROJECT_ROOT/pipeline/scripts/run-reviewer.sh")
GUARDED_CALLS=$(grep -cE '\|\| true' "$PROJECT_ROOT/pipeline/scripts/run-reviewer.sh")
if [ "$CLAUDE_CALLS" -ge 1 ] && [ "$GUARDED_CALLS" -ge "$CLAUDE_CALLS" ]; then
  run_test "run-reviewer.sh guards its claude calls against set -e abort" 0
else
  run_test "run-reviewer.sh guards its claude calls against set -e abort (claude=$CLAUDE_CALLS guarded=$GUARDED_CALLS)" 1
fi

echo ""
echo "=== Results: Passed $PASS / Total $((PASS + FAIL)) ==="
[ "$FAIL" -eq 0 ] && exit 0 || exit 1
