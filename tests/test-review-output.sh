#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

PASS=0
FAIL=0

echo "=== Review Output Tests ==="

# Setup: create a temporary pipeline run with deduped fixture data
TEST_RUN_ID="test-review-$(date +%s)"
TEST_RUN_DIR="$PROJECT_ROOT/pipeline/runs/$TEST_RUN_ID"
mkdir -p "$TEST_RUN_DIR"
trap 'rm -rf "$TEST_RUN_DIR"' EXIT

# Use scanner output directly as deduped (for simplicity in this test)
cp "$SCRIPT_DIR/fixtures/sample-scanner-output.json" "$TEST_RUN_DIR/scanner-deduped.json"

# Run review generation
"$PROJECT_ROOT/pipeline/scripts/generate-review.sh" "$TEST_RUN_ID"

REVIEW="$TEST_RUN_DIR/scanner-review.md"

# Test 1: Review file exists
if [ -f "$REVIEW" ]; then
  echo "PASS: scanner-review.md created"
  PASS=$((PASS + 1))
else
  echo "FAIL: scanner-review.md not created"
  FAIL=$((FAIL + 1))
fi

# Test 2: Contains checkboxes
CHECKBOX_COUNT=$(grep -c '\- \[ \] Approve' "$REVIEW" || true)
if [ "$CHECKBOX_COUNT" -eq 3 ]; then
  echo "PASS: Contains 3 approval checkboxes"
  PASS=$((PASS + 1))
else
  echo "FAIL: Expected 3 checkboxes, found $CHECKBOX_COUNT"
  FAIL=$((FAIL + 1))
fi

# Test 3: Contains finding IDs
if grep -q "SCAN-20260406-001" "$REVIEW" && grep -q "SCAN-20260406-002" "$REVIEW" && grep -q "SCAN-20260406-003" "$REVIEW"; then
  echo "PASS: All finding IDs present"
  PASS=$((PASS + 1))
else
  echo "FAIL: Missing finding IDs"
  FAIL=$((FAIL + 1))
fi

# Test 4: Contains source failure section
if grep -q "Source Failures" "$REVIEW"; then
  echo "PASS: Source failures section present"
  PASS=$((PASS + 1))
else
  echo "FAIL: Source failures section missing"
  FAIL=$((FAIL + 1))
fi

# Test 5: Contains APPROVED marker hint (commented out)
if grep -q "## APPROVED" "$REVIEW"; then
  echo "PASS: APPROVED marker hint present"
  PASS=$((PASS + 1))
else
  echo "FAIL: APPROVED marker hint missing"
  FAIL=$((FAIL + 1))
fi

# Test 6: Contains pipeline run ID
if grep -q "$TEST_RUN_ID" "$REVIEW"; then
  echo "PASS: Pipeline run ID present in review"
  PASS=$((PASS + 1))
else
  echo "FAIL: Pipeline run ID missing from review"
  FAIL=$((FAIL + 1))
fi

echo ""
echo "Review output tests: $PASS passed, $FAIL failed"

if [ "$FAIL" -gt 0 ]; then
  exit 1
fi
