#!/bin/bash
set -euo pipefail

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

echo "=== Researcher Validation Tests ==="
echo ""

# ---------------------------------------------------------------------------
# REPT-01: Schema validation
# ---------------------------------------------------------------------------
echo "--- REPT-01: Schema validation ---"

# Test 1: Researcher output validates against schema
bash "$PROJECT_ROOT/pipeline/scripts/validate-handoff.sh" researcher "$PROJECT_ROOT/tests/fixtures/sample-researcher-output.json" > /dev/null 2>&1
run_test "Researcher output validates against schema" $?

# Test 2: Researcher output has report_path field
jq -e '.data.reports[0].report_path' "$PROJECT_ROOT/tests/fixtures/sample-researcher-output.json" > /dev/null 2>&1
run_test "Researcher output has report_path field" $?

# Test 3: Researcher output has jurisdiction_tags array
jq -e '.data.reports[0].jurisdiction_tags | length > 0' "$PROJECT_ROOT/tests/fixtures/sample-researcher-output.json" > /dev/null 2>&1
run_test "Researcher output has jurisdiction_tags array" $?

echo ""

# ---------------------------------------------------------------------------
# REPT-02: Format selection
# ---------------------------------------------------------------------------
echo "--- REPT-02: Format selection ---"

# Test 4: High relevance finding maps to client-alert format
RELEVANCE_0=$(jq -r '.data.findings[0].relevance' "$PROJECT_ROOT/tests/fixtures/sample-approved-findings.json")
FORMAT_0=$(jq -r '.data.reports[0].format' "$PROJECT_ROOT/tests/fixtures/sample-researcher-output.json")
if [ "$RELEVANCE_0" = "high" ] && [ "$FORMAT_0" = "client-alert" ]; then
  run_test "High relevance finding maps to client-alert format" 0
else
  run_test "High relevance finding maps to client-alert format (got relevance=$RELEVANCE_0, format=$FORMAT_0)" 1
fi

# Test 5: Medium relevance finding maps to research-memo format
RELEVANCE_1=$(jq -r '.data.findings[1].relevance' "$PROJECT_ROOT/tests/fixtures/sample-approved-findings.json")
FORMAT_1=$(jq -r '.data.reports[1].format' "$PROJECT_ROOT/tests/fixtures/sample-researcher-output.json")
if [ "$RELEVANCE_1" = "medium" ] && [ "$FORMAT_1" = "research-memo" ]; then
  run_test "Medium relevance finding maps to research-memo format" 0
else
  run_test "Medium relevance finding maps to research-memo format (got relevance=$RELEVANCE_1, format=$FORMAT_1)" 1
fi

# Test 6: Format enum is valid
VALID_FORMATS=$(jq -e '[.data.reports[] | select(.format | IN("client-alert","research-memo"))] | length' "$PROJECT_ROOT/tests/fixtures/sample-researcher-output.json")
TOTAL_REPORTS=$(jq '.data.reports | length' "$PROJECT_ROOT/tests/fixtures/sample-researcher-output.json")
if [ "$VALID_FORMATS" = "$TOTAL_REPORTS" ]; then
  run_test "Format enum is valid for all reports" 0
else
  run_test "Format enum is valid for all reports (valid=$VALID_FORMATS, total=$TOTAL_REPORTS)" 1
fi

echo ""

# ---------------------------------------------------------------------------
# REPT-03: Confidence summary
# ---------------------------------------------------------------------------
echo "--- REPT-03: Confidence summary ---"

# Test 7: Confidence summary has high/medium/low counts
jq -e '.data.reports[0].confidence_summary | (.high >= 0) and (.medium >= 0) and (.low >= 0)' "$PROJECT_ROOT/tests/fixtures/sample-researcher-output.json" > /dev/null 2>&1
run_test "Confidence summary has high/medium/low counts" $?

# Test 8: Client-alert sample has confidence tags in headings
ALERT_CONF_COUNT=$(grep -c '\[.*confidence\]' "$PROJECT_ROOT/tests/fixtures/sample-reports/client-alert-sample.md" || true)
if [ "$ALERT_CONF_COUNT" -ge 2 ]; then
  run_test "Client-alert sample has confidence tags in headings (found $ALERT_CONF_COUNT)" 0
else
  run_test "Client-alert sample has confidence tags in headings (found $ALERT_CONF_COUNT, need >= 2)" 1
fi

# Test 9: Research-memo sample has confidence tags in headings
MEMO_CONF_COUNT=$(grep -c '\[.*confidence\]' "$PROJECT_ROOT/tests/fixtures/sample-reports/research-memo-sample.md" || true)
if [ "$MEMO_CONF_COUNT" -ge 3 ]; then
  run_test "Research-memo sample has confidence tags in headings (found $MEMO_CONF_COUNT)" 0
else
  run_test "Research-memo sample has confidence tags in headings (found $MEMO_CONF_COUNT, need >= 3)" 1
fi

echo ""

# ---------------------------------------------------------------------------
# REPT-04: Related Reports section
# ---------------------------------------------------------------------------
echo "--- REPT-04: Related Reports ---"

# Test 10: Client-alert sample has Related Reports section
grep -q '## Related Reports' "$PROJECT_ROOT/tests/fixtures/sample-reports/client-alert-sample.md"
run_test "Client-alert sample has Related Reports section" $?

# Test 11: Research-memo sample has Related Reports section
grep -q '## Related Reports' "$PROJECT_ROOT/tests/fixtures/sample-reports/research-memo-sample.md"
run_test "Research-memo sample has Related Reports section" $?

echo ""

# ---------------------------------------------------------------------------
# Report content validation
# ---------------------------------------------------------------------------
echo "--- Report content validation ---"

# Test 12: Client-alert has all required sections
ALERT_PASS=true
for section in "## Summary" "## Key Facts" "## Action Items" "## Sources"; do
  if ! grep -q "$section" "$PROJECT_ROOT/tests/fixtures/sample-reports/client-alert-sample.md"; then
    ALERT_PASS=false
    break
  fi
done
if [ "$ALERT_PASS" = true ]; then
  run_test "Client-alert has all required sections" 0
else
  run_test "Client-alert has all required sections" 1
fi

# Test 13: Research-memo has all required sections
MEMO_PASS=true
for section in "## Executive Summary" "## Background" "## Detailed Analysis" "## Impact Assessment" "## Action Items" "## Sources"; do
  if ! grep -q "$section" "$PROJECT_ROOT/tests/fixtures/sample-reports/research-memo-sample.md"; then
    MEMO_PASS=false
    break
  fi
done
if [ "$MEMO_PASS" = true ]; then
  run_test "Research-memo has all required sections" 0
else
  run_test "Research-memo has all required sections" 1
fi

# Test 14: Both reports have Sources section
grep -q "## Sources" "$PROJECT_ROOT/tests/fixtures/sample-reports/client-alert-sample.md" && \
grep -q "## Sources" "$PROJECT_ROOT/tests/fixtures/sample-reports/research-memo-sample.md"
run_test "Both reports have Sources section" $?

# Test 15: Report paths start with reports/
VALID_PATHS=$(jq -e '[.data.reports[] | select(.report_path | startswith("reports/"))] | length' "$PROJECT_ROOT/tests/fixtures/sample-researcher-output.json")
if [ "$VALID_PATHS" = "$TOTAL_REPORTS" ]; then
  run_test "Report paths start with reports/" 0
else
  run_test "Report paths start with reports/ (valid=$VALID_PATHS, total=$TOTAL_REPORTS)" 1
fi

echo ""
echo "=== Results: Passed $PASS / Total $((PASS + FAIL)) ==="
[ "$FAIL" -eq 0 ] && exit 0 || exit 1
