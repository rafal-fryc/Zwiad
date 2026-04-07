#!/bin/bash
set -euo pipefail

# Test per-claim verification annotations in reports
# Covers: VERF-04 (verification status annotation)

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

echo "=== Reviewer Annotation Tests ==="
echo ""

# ---------------------------------------------------------------------------
# VERF-04: Per-claim verification annotation
# ---------------------------------------------------------------------------
echo "--- VERF-04: Verification annotations ---"

REPORT="$PROJECT_ROOT/tests/fixtures/sample-verified-report.md"

# Test 1: Verified report has <!-- verified --> annotations
VERIFIED_COUNT=$(grep -c '<!-- verified -->' "$REPORT" || true)
if [ "$VERIFIED_COUNT" -gt 0 ]; then
  run_test "Verified report has <!-- verified --> annotations (found $VERIFIED_COUNT)" 0
else
  run_test "Verified report has <!-- verified --> annotations (found 0)" 1
fi

# Test 2: Verified report has <!-- disputed: ... --> annotation
grep -q '<!-- disputed:' "$REPORT"
run_test "Verified report has <!-- disputed: ... --> annotation" $?

# Test 3: Verified report has <!-- unverifiable: source unavailable --> annotation (D-04)
grep -q '<!-- unverifiable: source unavailable -->' "$REPORT"
run_test "Verified report has <!-- unverifiable: source unavailable --> annotation" $?

# Test 4: Section headings include verification status
if grep -q '\[VERIFIED\]' "$REPORT"; then
  run_test "Section headings include [VERIFIED] status" 0
else
  run_test "Section headings include [VERIFIED] status" 1
fi

# Test 5: Verified report retains confidence tags
if grep -qE '\[(HIGH|MEDIUM|LOW) confidence\]' "$REPORT"; then
  run_test "Verified report retains confidence tags" 0
else
  run_test "Verified report retains confidence tags" 1
fi

# Test 6: Reviewer agent prompt includes annotation instructions
grep -q '<!-- verified -->' "$PROJECT_ROOT/.claude/agents/reviewer.md"
run_test "Reviewer agent prompt includes verified annotation instruction" $?

# Test 7: Reviewer agent prompt includes disputed annotation
grep -q '<!-- disputed:' "$PROJECT_ROOT/.claude/agents/reviewer.md"
run_test "Reviewer agent prompt includes disputed annotation instruction" $?

# Test 8: Annotation format uses HTML comments (non-disruptive)
# All annotations in the verified report should use <!-- ... --> format
# Check that no non-HTML annotation patterns are used (e.g., [verified], {verified})
ANNOTATIONS=$(grep -oE '<!-- [a-z]+[^>]*-->' "$REPORT" | wc -l)
NON_HTML=$(grep -cE '\{verified\}|\{disputed\}|\{unverifiable\}' "$REPORT" || true)
if [ "$ANNOTATIONS" -gt 0 ] && [ "$NON_HTML" -eq 0 ]; then
  run_test "Annotations use HTML comment format exclusively (found $ANNOTATIONS)" 0
else
  run_test "Annotations use HTML comment format exclusively (html=$ANNOTATIONS, non-html=$NON_HTML)" 1
fi

echo ""
echo "=== Results: Passed $PASS / Total $((PASS + FAIL)) ==="
[ "$FAIL" -eq 0 ] && exit 0 || exit 1
