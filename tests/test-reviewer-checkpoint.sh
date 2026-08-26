#!/bin/bash
# Test: reviewer progress survives an interrupted run
#
# Covers the two halves of the fix for run 2026-07-25T18-29-52, where the review
# stage was killed by its wall-clock timeout and wrote no reviewer-output.json,
# so the next run re-reviewed all 37 reports from scratch:
#
#   1. write_reviewer_output's merge -- a mid-loop checkpoint must never shrink
#      the file by dropping prior terminal results the loop has not reached yet.
#   2. salvage-reviewer-output.sh -- rebuild reviewer-output.json from the
#      per-finding artifacts an interrupted run left on disk.

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PASS=0
FAIL=0

pass() { echo "PASS: $1"; PASS=$((PASS + 1)); }
fail() { echo "FAIL: $1"; FAIL=$((FAIL + 1)); }

echo "=== Test: Reviewer checkpoint + salvage ==="

# ---------------------------------------------------------------------------
# 1. Checkpoint merge semantics
# ---------------------------------------------------------------------------

merge() {
  jq -n --argjson prior "$1" --argjson cur "$2" \
    '($prior + $cur) | group_by(.finding_id) | map(.[-1])'
}

PRIOR='[{"finding_id":"A","status":"verified"},{"finding_id":"B","status":"verified"},{"finding_id":"C","status":"needs-human-review"}]'

# Mid-loop: only A has been re-reviewed this run.
MERGED=$(merge "$PRIOR" '[{"finding_id":"A","status":"needs-human-review"}]')

COUNT=$(echo "$MERGED" | jq 'length')
if [ "$COUNT" -eq 3 ]; then
  pass "Mid-loop checkpoint keeps all 3 prior entries (no shrink)"
else
  fail "Mid-loop checkpoint dropped entries: expected 3, got $COUNT"
fi

A_STATUS=$(echo "$MERGED" | jq -r '.[] | select(.finding_id=="A") | .status')
if [ "$A_STATUS" = "needs-human-review" ]; then
  pass "Current-run entry wins over the prior entry for the same finding"
else
  fail "Current entry did not win: A is '$A_STATUS'"
fi

DUPES=$(echo "$MERGED" | jq '[.[].finding_id] | length as $n | unique | length as $u | $n - $u')
if [ "$DUPES" -eq 0 ]; then
  pass "Merged output has no duplicate finding_ids"
else
  fail "Merged output has $DUPES duplicate finding_id(s)"
fi

# Empty prior (first run) must still produce the current entries verbatim.
MERGED_EMPTY=$(merge '[]' '[{"finding_id":"A","status":"verified"}]')
if [ "$(echo "$MERGED_EMPTY" | jq 'length')" -eq 1 ]; then
  pass "Empty prior merges to just the current entries"
else
  fail "Empty prior merge produced unexpected length"
fi

# ---------------------------------------------------------------------------
# 2. Salvage from on-disk artifacts
# ---------------------------------------------------------------------------

RUN_ID="test-checkpoint-$$"
RUN_DIR="$PROJECT_ROOT/pipeline/runs/$RUN_ID"
mkdir -p "$RUN_DIR"
trap 'rm -rf "$RUN_DIR"' EXIT

mk_report() {   # finding_id
  jq -n --arg fid "$1" \
    '{schema_version:"1.0", stage:"researcher", status:"complete",
      data:{reports:[{finding_id:$fid, report_path:("reports/privacy/x-" + $fid + ".md")}]}}' \
    > "$RUN_DIR/researcher-$1.json"
}

mk_feedback() { # finding_id round severity status
  jq -n --arg fid "$1" --argjson r "$2" --arg sev "$3" --arg st "$4" \
    '{finding_id:$fid, report_path:("reports/privacy/x-" + $fid + ".md"), round:$r,
      claims_checked:(10 + $r), resolution_status:"issues-found",
      issues:[{claim:"c", section:"s", source_url:null, issue:"i", severity:$sev,
               suggested_fix:"f", status:$st}]}' \
    > "$RUN_DIR/reviewer-feedback-r$2-$1.json"
}

# VERIFIED-A: round 1, minor only -> terminal "verified"
mk_report "SCAN-A"; mk_feedback "SCAN-A" 1 "minor" "open"

# ESCALATED-B: three rounds of critical + escalation gate -> "needs-human-review"
mk_report "SCAN-B"
mk_feedback "SCAN-B" 1 "critical" "open"
mk_feedback "SCAN-B" 2 "critical" "upheld"
mk_feedback "SCAN-B" 3 "critical" "upheld"
echo '{}' > "$RUN_DIR/researcher-revision-r1-SCAN-B.json"
echo '{}' > "$RUN_DIR/researcher-revision-r2-SCAN-B.json"
jq -n '{run_id:"x", finding_id:"SCAN-B", resolved:false}' > "$RUN_DIR/escalation-SCAN-B.json"

# PARTIAL-C: round 1 critical, no revision -> interrupted, NOT terminal
mk_report "SCAN-C"; mk_feedback "SCAN-C" 1 "critical" "open"

# UNTOUCHED-D: report only, never reviewed -> NOT terminal
mk_report "SCAN-D"

OUT=$(bash "$PROJECT_ROOT/pipeline/scripts/salvage-reviewer-output.sh" "$RUN_ID" --stdout 2>/dev/null)

got_status() { echo "$OUT" | jq -r --arg f "$1" '.data.reviews[] | select(.finding_id==$f) | .status'; }

if [ "$(echo "$OUT" | jq '.data.reviews | length')" -eq 2 ]; then
  pass "Salvage keeps only the 2 terminal findings"
else
  fail "Salvage entry count wrong: got $(echo "$OUT" | jq '.data.reviews | length'), want 2"
fi

[ "$(got_status SCAN-A)" = "verified" ] \
  && pass "Round-1 minor-only salvages as verified" \
  || fail "SCAN-A status: '$(got_status SCAN-A)'"

[ "$(got_status SCAN-B)" = "needs-human-review" ] \
  && pass "Round-3 critical with gate salvages as needs-human-review" \
  || fail "SCAN-B status: '$(got_status SCAN-B)'"

[ -z "$(got_status SCAN-C)" ] \
  && pass "Interrupted mid-iteration finding is omitted (gets re-reviewed)" \
  || fail "SCAN-C should be omitted, got '$(got_status SCAN-C)'"

[ -z "$(got_status SCAN-D)" ] \
  && pass "Never-reviewed finding is omitted" \
  || fail "SCAN-D should be omitted"

# claims_checked must be the max across rounds, matching run-reviewer.sh.
B_CLAIMS=$(echo "$OUT" | jq -r '.data.reviews[] | select(.finding_id=="SCAN-B") | .claims_checked')
[ "$B_CLAIMS" = "13" ] \
  && pass "claims_checked takes the max across rounds (13)" \
  || fail "claims_checked for SCAN-B: got '$B_CLAIMS', want 13"

# An escalated finding whose gate file is missing is not reusable by
# run-reviewer.sh, so salvage must not claim it is terminal.
rm -f "$RUN_DIR/escalation-SCAN-B.json"
OUT2=$(bash "$PROJECT_ROOT/pipeline/scripts/salvage-reviewer-output.sh" "$RUN_ID" --stdout 2>/dev/null)
[ "$(echo "$OUT2" | jq '.data.reviews | length')" -eq 1 ] \
  && pass "Escalation without a gate file is not treated as terminal" \
  || fail "Missing gate file still salvaged as terminal"

# Envelope shape must match what the reviewer stage normally emits.
SHAPE=$(echo "$OUT" | jq -r '[.schema_version, .stage, (.data.reviews|type)] | join(",")')
[ "$SHAPE" = "1.0,reviewer,array" ] \
  && pass "Envelope shape matches the reviewer handoff contract" \
  || fail "Envelope shape wrong: $SHAPE"

echo ""
echo "Reviewer checkpoint tests: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ]
