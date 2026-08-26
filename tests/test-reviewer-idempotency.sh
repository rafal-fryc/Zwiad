#!/bin/bash
set -euo pipefail

# Idempotency regression test for run-reviewer.sh (run 2026-07-17T13-54-18).
#
# A re-run must REUSE reports that already reached a terminal outcome (verified,
# or escalated with an escalation-<id>.json gate file) and only re-review those
# left non-terminal by a prior partial/rate-limited run. This test stubs the
# `claude` CLI so we can assert exactly which findings get re-reviewed without
# spending money or needing network access.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

PASS=0
FAIL=0
run_test() {
  if [ "$2" -eq 0 ]; then echo "PASS: $1"; PASS=$((PASS + 1)); else echo "FAIL: $1"; FAIL=$((FAIL + 1)); fi
}

echo "=== Reviewer Idempotency Tests ==="
echo ""

RUN_ID="TEST-IDEMPOTENCY-$$"
RUN_DIR="$PROJECT_ROOT/pipeline/runs/$RUN_ID"
STUB_BIN="$(mktemp -d)"
CALL_LOG="$RUN_DIR/.claude-calls"

cleanup() { rm -rf "$RUN_DIR" "$STUB_BIN"; }
trap cleanup EXIT

mkdir -p "$RUN_DIR"

# --- researcher outputs: A (reuse-verified), B (reuse-escalated), C (re-review) ---
for pair in "A:test-a" "B:test-b" "C:test-c"; do
  fid="FIND-${pair%%:*}"; slug="${pair##*:}"
  cat > "$RUN_DIR/researcher-$fid.json" <<EOF
{"schema_version":"1.0","pipeline_run_id":"$RUN_ID","timestamp":"2026-07-18T00:00:00Z","stage":"researcher","status":"complete",
 "data":{"reports":[{"finding_id":"$fid","report_path":"reports/privacy/$slug.md","format":"client-alert","jurisdiction_tags":["Federal"],"topic_key":"k-$fid","topic_type":"guidance","confidence_summary":{"high":1,"medium":0,"low":0}}]}}
EOF
done

# --- prior reviewer-output.json: A verified, B + C needs-human-review ---
cat > "$RUN_DIR/reviewer-output.json" <<EOF
{"schema_version":"1.0","pipeline_run_id":"$RUN_ID","timestamp":"2026-07-18T00:00:00Z","stage":"reviewer","status":"pending-review",
 "data":{"reviews":[
   {"finding_id":"FIND-A","report_path":"reports/privacy/test-a.md","status":"verified","iteration_count":1,"claims_checked":5,"issues_found":[]},
   {"finding_id":"FIND-B","report_path":"reports/privacy/test-b.md","status":"needs-human-review","iteration_count":3,"claims_checked":8,"issues_found":[{"claim":"c","issue":"i","severity":"major"}]},
   {"finding_id":"FIND-C","report_path":"reports/privacy/test-c.md","status":"needs-human-review","iteration_count":1,"claims_checked":0,"issues_found":[]}
 ]}}
EOF

# B has a genuine escalation gate file → terminal; C does NOT → must be re-reviewed
echo '{"run_id":"'"$RUN_ID"'","finding_id":"FIND-B","report_path":"reports/privacy/test-b.md","escalation_md":"","rounds_completed":3,"unresolved_issues":[],"resolved":false}' > "$RUN_DIR/escalation-FIND-B.json"

# --- stub claude: log the finding it was called for, write valid feedback ---
cat > "$STUB_BIN/claude" <<'STUB'
#!/bin/bash
for a; do prompt="$a"; done   # last arg is the prompt
fid=$(printf '%s' "$prompt" | sed -n 's/.*for finding \([A-Za-z0-9-]*\).*/\1/p')
fb=$(printf '%s' "$prompt" | sed -n 's/.*feedback to: \([^ ]*\.json\).*/\1/p')
[ -n "$fid" ] && echo "$fid" >> "$CALL_LOG"
if [ -n "$fb" ]; then
  cat > "$fb" <<FB
{"finding_id":"$fid","report_path":"reports/privacy/x.md","round":1,"claims_checked":4,"issues":[],"resolution_status":"resolved"}
FB
fi
echo '{"total_cost_usd":0,"is_error":false,"terminal_reason":"completed"}'
exit 0
STUB
chmod +x "$STUB_BIN/claude"
export CALL_LOG

# --- run the reviewer with the stub claude in front of PATH ---
OUT=$(PATH="$STUB_BIN:$PATH" bash "$PROJECT_ROOT/pipeline/scripts/run-reviewer.sh" "$RUN_ID" 2>&1) || true

# Test 1: script completed and wrote a valid reviewer-output.json
bash "$PROJECT_ROOT/pipeline/scripts/validate-handoff.sh" reviewer "$RUN_DIR/reviewer-output.json" > /dev/null 2>&1
run_test "Re-run produces a schema-valid reviewer-output.json" $?

# Test 2: claude was invoked for C only (A and B reused, never re-reviewed)
CALLS=$(cat "$CALL_LOG" 2>/dev/null | sort -u | tr '\n' ' ')
if [ "$(printf '%s' "$CALLS" | tr -d ' ')" = "FIND-C" ]; then
  run_test "claude re-reviewed only the non-terminal report (C); reused A + B" 0
else
  run_test "claude re-reviewed only the non-terminal report (got: '$CALLS')" 1
fi

# Test 3: reused count is exactly 2
if printf '%s' "$OUT" | grep -q "Reused from prior run (not re-reviewed): 2"; then
  run_test "Summary reports 2 reused reports" 0
else
  run_test "Summary reports 2 reused reports" 1
fi

# Test 4: A stays verified, B stays needs-human-review (reused verbatim), C now verified
A_ST=$(jq -r '.data.reviews[] | select(.finding_id=="FIND-A") | .status' "$RUN_DIR/reviewer-output.json")
B_ST=$(jq -r '.data.reviews[] | select(.finding_id=="FIND-B") | .status' "$RUN_DIR/reviewer-output.json")
C_ST=$(jq -r '.data.reviews[] | select(.finding_id=="FIND-C") | .status' "$RUN_DIR/reviewer-output.json")
if [ "$A_ST" = "verified" ] && [ "$B_ST" = "needs-human-review" ] && [ "$C_ST" = "verified" ]; then
  run_test "Reused A=verified, B=needs-human-review; re-reviewed C=verified" 0
else
  run_test "Statuses (A=$A_ST B=$B_ST C=$C_ST)" 1
fi

echo ""
echo "=== Results: Passed $PASS / Total $((PASS + FAIL)) ==="
[ "$FAIL" -eq 0 ] && exit 0 || exit 1
