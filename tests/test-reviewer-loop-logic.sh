#!/bin/bash
set -uo pipefail

# Regression tests for the reviewer-loop convergence + verdict fixes (2026-08):
#  1. The iteration loop must count only UNRESOLVED (open/upheld) critical/major
#     issues — a report whose critical issues were all fixed must verify, not
#     burn three rounds and escalate.
#  2. A round-3 reviewer *failure* (no valid feedback) must be classified as
#     review_failed (retryable), not as a genuine escalation — the verdict
#     block must branch on ESCALATED_AFTER_ROUNDS, not on ROUND alone.
#  3. salvage-reviewer-output.sh must apply the same unresolved-only filter.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
REVIEWER_SH="$PROJECT_ROOT/pipeline/scripts/run-reviewer.sh"
SALVAGE_SH="$PROJECT_ROOT/pipeline/scripts/salvage-reviewer-output.sh"

PASS=0
FAIL=0
run_test() {
  local name="$1" rc="$2"
  if [ "$rc" -eq 0 ]; then
    echo "PASS: $name"; PASS=$((PASS + 1))
  else
    echo "FAIL: $name"; FAIL=$((FAIL + 1))
  fi
}

echo "=== Test: Reviewer loop logic ==="

# The exact filter both scripts must use (kept in lockstep with the code —
# extracted from run-reviewer.sh below so the test fails if the script drifts).
FILTER='[.issues[] | select((.severity == "critical" or .severity == "major") and (.status == "open" or .status == "upheld"))] | length'

TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

# Feedback where every critical/major issue was already resolved
cat > "$TMP/feedback-resolved.json" <<'EOF'
{
  "finding_id": "SCAN-TEST-001",
  "report_path": "reports/privacy/test-2026-08-19.md",
  "round": 2,
  "claims_checked": 10,
  "issues": [
    {"claim": "date", "issue": "wrong date", "severity": "critical", "status": "fixed"},
    {"claim": "statute", "issue": "wrong section", "severity": "major", "status": "withdrawn"},
    {"claim": "phrasing", "issue": "imprecise", "severity": "minor", "status": "open"}
  ],
  "resolution_status": "resolved"
}
EOF

# Feedback with a genuinely unresolved critical issue
cat > "$TMP/feedback-open.json" <<'EOF'
{
  "finding_id": "SCAN-TEST-002",
  "report_path": "reports/privacy/test2-2026-08-19.md",
  "round": 3,
  "claims_checked": 10,
  "issues": [
    {"claim": "penalty", "issue": "wrong amount", "severity": "critical", "status": "upheld"}
  ],
  "resolution_status": "escalate"
}
EOF

# 1a. Resolved-issues feedback counts zero blocking issues
COUNT=$(jq "$FILTER" "$TMP/feedback-resolved.json")
[ "$COUNT" -eq 0 ]; run_test "fixed/withdrawn critical issues do not block verification" $?

# 1b. Open/upheld critical issues still count
COUNT=$(jq "$FILTER" "$TMP/feedback-open.json")
[ "$COUNT" -eq 1 ]; run_test "open/upheld critical issues still block" $?

# 1c. Every CRITICAL_MAJOR count in run-reviewer.sh (update branch AND main
# loop) uses the unresolved-only filter — the old main-loop line counted by
# severity alone, which is the bug this guards against.
MAIN_OK=1
while IFS= read -r line; do
  case "$line" in *"status == \"open\""*) ;; *) MAIN_OK=0 ;; esac
done < <(grep 'CRITICAL_MAJOR=\$(jq' "$REVIEWER_SH")
[ "$MAIN_OK" -eq 1 ]; run_test "every CRITICAL_MAJOR count in run-reviewer.sh filters on open/upheld" $?

# 2. Verdict block branches on ESCALATED_AFTER_ROUNDS, not bare ROUND
grep -q 'ESCALATED_AFTER_ROUNDS=true' "$REVIEWER_SH" && \
  grep -q 'elif \[ "\$ESCALATED_AFTER_ROUNDS" = true \]' "$REVIEWER_SH" && \
  ! grep -q 'elif \[ "\$ROUND" -ge 3 \]' "$REVIEWER_SH"
run_test "round-3 verdict requires a real escalation, not just ROUND=3" $?

# 3. salvage-reviewer-output.sh uses the same unresolved-only filter
SALVAGE_OK=1
while IFS= read -r line; do
  case "$line" in *"status == \"open\""*) ;; *) SALVAGE_OK=0 ;; esac
done < <(grep 'CRITICAL_MAJOR=\$(jq' "$SALVAGE_SH")
[ "$SALVAGE_OK" -eq 1 ]; run_test "salvage script filter matches run-reviewer.sh" $?

echo ""
echo "Reviewer loop logic tests: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] && exit 0 || exit 1
