#!/bin/bash
# Test: a defensive escalation gate must not be permanently terminal
#
# run-reviewer.sh writes an escalation gate for EVERY needs-human-review
# outcome, including the case where the reviewer produced no usable feedback at
# all (rate limit, crash). Because the resume path treats "gate file exists" as
# terminal, a transient rate limit was permanently recorded as an escalation and
# the report was never fact-checked.
#
# Run 2026-07-25T18-29-52: 11 gates written in 31 seconds when every reviewer
# call failed instantly. A real review takes ~15 minutes.
#
# The fix marks those gates review_failed:true so resume retries them, while
# genuine three-round escalations stay terminal.

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
REVIEWER="$PROJECT_ROOT/pipeline/scripts/run-reviewer.sh"
PASS=0
FAIL=0

pass() { echo "PASS: $1"; PASS=$((PASS + 1)); }
fail() { echo "FAIL: $1"; FAIL=$((FAIL + 1)); }

echo "=== Test: Escalation gate retry semantics ==="

TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

# The predicate the script uses to decide whether a gate is terminal.
is_terminal() {
  [ -f "$1" ] || return 1
  [ "$(jq -r '.review_failed // false' "$1" 2>/dev/null)" != "true" ]
}

jq -n '{finding_id:"A", unresolved_issues:[{severity:"critical"}], rounds_completed:3,
        escalation_md:"# real", resolved:false}' > "$TMP/genuine.json"
jq -n '{finding_id:"B", unresolved_issues:[], rounds_completed:1, escalation_md:"",
        review_failed:true, resolved:false}' > "$TMP/failed.json"
jq -n '{finding_id:"C", unresolved_issues:[], rounds_completed:3, escalation_md:"",
        review_failed:false, resolved:false}' > "$TMP/explicit-false.json"

is_terminal "$TMP/genuine.json" \
  && pass "Genuine 3-round escalation stays terminal (skipped on resume)" \
  || fail "Genuine escalation was treated as retryable"

is_terminal "$TMP/failed.json" \
  && fail "review_failed gate was treated as terminal (would never be reviewed)" \
  || pass "review_failed gate is retryable on resume"

is_terminal "$TMP/explicit-false.json" \
  && pass "review_failed:false behaves as terminal" \
  || fail "review_failed:false was treated as retryable"

is_terminal "$TMP/nonexistent.json" \
  && fail "Missing gate reported as terminal" \
  || pass "Missing gate is not terminal"

# Legacy gates written before this fix have no review_failed field. They must
# default to terminal so genuine escalations are not silently re-reviewed.
jq -n '{finding_id:"D", unresolved_issues:[{severity:"major"}], rounds_completed:3}' \
  > "$TMP/legacy.json"
is_terminal "$TMP/legacy.json" \
  && pass "Legacy gate with no review_failed field defaults to terminal" \
  || fail "Legacy gate changed meaning"

# ---------------------------------------------------------------------------
# Structural: the script must actually consult the flag, and stamp it.
# ---------------------------------------------------------------------------

if grep -q "review_failed" "$REVIEWER"; then
  pass "run-reviewer.sh references review_failed"
else
  fail "run-reviewer.sh does not reference review_failed"
fi

# The reuse branch (the one that skips a prior escalation) must consult it.
if sed -n '/reusing prior escalation/,-8p' "$REVIEWER" 2>/dev/null | grep -q "review_failed" \
   || grep -B8 "reusing prior escalation" "$REVIEWER" | grep -q "review_failed"; then
  pass "Escalation-reuse branch consults review_failed"
else
  fail "Escalation-reuse branch still skips on gate existence alone"
fi

# The floor gate must record the real round count, not a hardcoded 3 -- a
# reviewer that died in round 1 did not complete three rounds.
if grep -A12 "Guarantee an escalation gate file" "$REVIEWER" | grep -q "rounds_completed: 3"; then
  fail "Floor gate still hardcodes rounds_completed: 3"
else
  pass "Floor gate records the actual round reached"
fi

echo ""
echo "Escalation retry tests: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ]
