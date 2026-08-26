#!/bin/bash
set -euo pipefail

# Test reviewer iteration logic and escalation
# Covers: VERF-03 (3-round iteration, human escalation)

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

echo "=== Reviewer Iteration Tests ==="
echo ""

# ---------------------------------------------------------------------------
# VERF-03: Iteration protocol
# ---------------------------------------------------------------------------
echo "--- VERF-03: Iteration protocol ---"

# Test 1: Feedback round field is integer 1-3
ROUND_VAL=$(jq '.round' "$PROJECT_ROOT/tests/fixtures/sample-reviewer-feedback.json")
if [ "$ROUND_VAL" -ge 1 ] && [ "$ROUND_VAL" -le 3 ]; then
  run_test "Feedback round field is integer 1-3 (got $ROUND_VAL)" 0
else
  run_test "Feedback round field is integer 1-3 (got $ROUND_VAL)" 1
fi

# Test 2: Issue status supports dispute flow values
# Construct test JSON with all allowed status values
DISPUTE_TEST='{"finding_id":"TEST-001","report_path":"reports/privacy/test.md","round":2,"claims_checked":5,"issues":[
  {"claim":"c1","section":"s","source_url":"http://x","issue":"i","severity":"critical","suggested_fix":"f","status":"open"},
  {"claim":"c2","section":"s","source_url":"http://x","issue":"i","severity":"major","suggested_fix":"f","status":"fixed"},
  {"claim":"c3","section":"s","source_url":"http://x","issue":"i","severity":"minor","suggested_fix":"f","status":"disputed"},
  {"claim":"c4","section":"s","source_url":"http://x","issue":"i","severity":"critical","suggested_fix":"f","status":"upheld"},
  {"claim":"c5","section":"s","source_url":"http://x","issue":"i","severity":"minor","suggested_fix":"f","status":"withdrawn"}
],"resolution_status":"issues-found"}'
echo "$DISPUTE_TEST" | jq -e -f "$PROJECT_ROOT/pipeline/schemas/reviewer-feedback.jq" > /dev/null 2>&1
run_test "Issue status supports all dispute flow values (open/fixed/disputed/upheld/withdrawn)" $?

# Test 3: Resolution status 'resolved' with only minor issues passes schema
RESOLVED_TEST='{"finding_id":"TEST-002","report_path":"reports/privacy/test.md","round":2,"claims_checked":5,"issues":[
  {"claim":"c1","section":"s","source_url":"http://x","issue":"minor style","severity":"minor","suggested_fix":"f","status":"open"}
],"resolution_status":"resolved"}'
echo "$RESOLVED_TEST" | jq -e -f "$PROJECT_ROOT/pipeline/schemas/reviewer-feedback.jq" > /dev/null 2>&1
run_test "Resolution status 'resolved' passes schema with minor-only issues" $?

# Test 4: Resolution status 'escalate' valid for round 3
ESCALATE_TEST='{"finding_id":"TEST-003","report_path":"reports/cybersecurity/test.md","round":3,"claims_checked":10,"issues":[
  {"claim":"c1","section":"s","source_url":"http://x","issue":"unresolved","severity":"critical","suggested_fix":"f","status":"upheld"}
],"resolution_status":"escalate"}'
echo "$ESCALATE_TEST" | jq -e -f "$PROJECT_ROOT/pipeline/schemas/reviewer-feedback.jq" > /dev/null 2>&1
run_test "Resolution status 'escalate' valid for round 3" $?

# Test 5: Escalation fixture has APPROVED marker
grep -q '## APPROVED' "$PROJECT_ROOT/tests/fixtures/sample-escalation.md"
run_test "Escalation fixture has APPROVED marker" $?

# Test 6: Escalation fixture has unresolved issues section
grep -q '## Unresolved Issues' "$PROJECT_ROOT/tests/fixtures/sample-escalation.md"
run_test "Escalation fixture has unresolved issues section" $?

# Test 7: Escalation fixture has round history
if grep -q 'Round 1:' "$PROJECT_ROOT/tests/fixtures/sample-escalation.md" && \
   grep -q 'Round 3:' "$PROJECT_ROOT/tests/fixtures/sample-escalation.md"; then
  run_test "Escalation fixture has round history (Round 1 and Round 3)" 0
else
  run_test "Escalation fixture has round history (Round 1 and Round 3)" 1
fi

# Test 8: run-reviewer.sh exists and is executable
test -x "$PROJECT_ROOT/pipeline/scripts/run-reviewer.sh"
run_test "run-reviewer.sh exists and is executable" $?

# Test 9: generate-escalation.sh exists and is executable
test -x "$PROJECT_ROOT/pipeline/scripts/generate-escalation.sh"
run_test "generate-escalation.sh exists and is executable" $?

# Test 10: approve-escalation.sh exists and is executable
test -x "$PROJECT_ROOT/pipeline/scripts/approve-escalation.sh"
run_test "approve-escalation.sh exists and is executable" $?

# Test 11: run-reviewer.sh contains 3-round iteration limit
grep -q '\-le 3' "$PROJECT_ROOT/pipeline/scripts/run-reviewer.sh"
run_test "run-reviewer.sh contains 3-round iteration limit" $?

# Test 12: run-reviewer.sh invokes researcher for revision
grep -q 'claude -p --agent researcher' "$PROJECT_ROOT/pipeline/scripts/run-reviewer.sh"
run_test "run-reviewer.sh invokes researcher for revision" $?

# Test 13: Reviewer output iteration_count is 1-3 for all reviews
INVALID_IC=$(jq '[.data.reviews[] | select(.iteration_count < 1 or .iteration_count > 3)] | length' "$PROJECT_ROOT/tests/fixtures/sample-reviewer-output.json")
if [ "$INVALID_IC" -eq 0 ]; then
  run_test "Reviewer output iteration_count is 1-3 for all reviews" 0
else
  run_test "Reviewer output iteration_count is 1-3 for all reviews (invalid: $INVALID_IC)" 1
fi

# ---------------------------------------------------------------------------
# VERF-04: Escalation counts UNRESOLVED issues only (run 2026-07-17 bug)
# A report whose critical/major issues are all status=fixed/resolved must
# verify, not escalate. run-reviewer.sh must count only status open/upheld.
# ---------------------------------------------------------------------------
echo ""
echo "--- VERF-04: Unresolved-only escalation counting ---"

ALL_FIXED='{"issues":[
  {"severity":"critical","status":"fixed"},
  {"severity":"major","status":"fixed"}
]}'
CM_FIXED=$(echo "$ALL_FIXED" | jq '[.issues[] | select((.severity=="critical" or .severity=="major") and (.status=="open" or .status=="upheld"))] | length')
run_test "All-fixed critical/major issues count as 0 blocking (report verifies)" $([ "$CM_FIXED" -eq 0 ] && echo 0 || echo 1)

OPEN_MIX='{"issues":[
  {"severity":"critical","status":"open"},
  {"severity":"major","status":"fixed"},
  {"severity":"minor","status":"open"}
]}'
CM_OPEN=$(echo "$OPEN_MIX" | jq '[.issues[] | select((.severity=="critical" or .severity=="major") and (.status=="open" or .status=="upheld"))] | length')
run_test "One open critical issue counts as 1 blocking (report escalates)" $([ "$CM_OPEN" -eq 1 ] && echo 0 || echo 1)

# run-reviewer.sh must use the status-filtered count, not severity-only
if grep -qE 'select\(\(\.severity == "critical" or \.severity == "major"\) and \(\.status == "open" or \.status == "upheld"\)\)' "$PROJECT_ROOT/pipeline/scripts/run-reviewer.sh"; then
  run_test "run-reviewer.sh counts only unresolved (open/upheld) critical/major" 0
else
  run_test "run-reviewer.sh counts only unresolved (open/upheld) critical/major" 1
fi

# every needs-human-review outcome must be backed by an escalation gate file
if grep -q 'Guarantee an escalation gate file' "$PROJECT_ROOT/pipeline/scripts/run-reviewer.sh"; then
  run_test "run-reviewer.sh guarantees a gate file for needs-human-review outcomes" 0
else
  run_test "run-reviewer.sh guarantees a gate file for needs-human-review outcomes" 1
fi

echo ""
echo "=== Results: Passed $PASS / Total $((PASS + FAIL)) ==="
[ "$FAIL" -eq 0 ] && exit 0 || exit 1
