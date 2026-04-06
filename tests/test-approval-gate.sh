#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

PASS=0
FAIL=0

echo "=== Approval Gate Tests ==="

# Setup
TEST_RUN_ID="test-approval-$(date +%s)"
TEST_RUN_DIR="$PROJECT_ROOT/pipeline/runs/$TEST_RUN_ID"
mkdir -p "$TEST_RUN_DIR"
trap 'rm -rf "$TEST_RUN_DIR"' EXIT

# Copy fixtures
cp "$SCRIPT_DIR/fixtures/sample-scanner-output.json" "$TEST_RUN_DIR/scanner-deduped.json"

# Test 1: Pending review (no APPROVED marker) should be rejected
cp "$SCRIPT_DIR/fixtures/sample-review-pending.md" "$TEST_RUN_DIR/scanner-review.md"
if ! "$PROJECT_ROOT/pipeline/scripts/approve-findings.sh" "$TEST_RUN_ID" 2>/dev/null; then
  echo "PASS: Pending review correctly rejected"
  PASS=$((PASS + 1))
else
  echo "FAIL: Pending review should have been rejected"
  FAIL=$((FAIL + 1))
fi

# Test 2: Approved review should succeed
cp "$SCRIPT_DIR/fixtures/sample-review-approved.md" "$TEST_RUN_DIR/scanner-review.md"
if "$PROJECT_ROOT/pipeline/scripts/approve-findings.sh" "$TEST_RUN_ID" 2>/dev/null; then
  echo "PASS: Approved review accepted"
  PASS=$((PASS + 1))
else
  echo "FAIL: Approved review should have been accepted"
  FAIL=$((FAIL + 1))
fi

# Test 3: Approved output file created
if [ -f "$TEST_RUN_DIR/scanner-approved.json" ]; then
  echo "PASS: scanner-approved.json created"
  PASS=$((PASS + 1))
else
  echo "FAIL: scanner-approved.json not created"
  FAIL=$((FAIL + 1))
fi

# Test 4: Only checked findings are in approved output
# The fixture has finding 001 checked and 003 unchecked
APPROVED_COUNT=$(jq '.data.findings | length' "$TEST_RUN_DIR/scanner-approved.json")
if [ "$APPROVED_COUNT" -eq 1 ]; then
  echo "PASS: Only 1 approved finding (001 checked, 003 unchecked)"
  PASS=$((PASS + 1))
else
  echo "FAIL: Expected 1 approved finding, got $APPROVED_COUNT"
  FAIL=$((FAIL + 1))
fi

# Test 5: Correct finding approved (SCAN-20260406-001)
APPROVED_ID=$(jq -r '.data.findings[0].id' "$TEST_RUN_DIR/scanner-approved.json")
if [ "$APPROVED_ID" = "SCAN-20260406-001" ]; then
  echo "PASS: Correct finding (001) approved"
  PASS=$((PASS + 1))
else
  echo "FAIL: Expected SCAN-20260406-001, got $APPROVED_ID"
  FAIL=$((FAIL + 1))
fi

# Test 6: Approved output has human-review stage
STAGE=$(jq -r '.stage' "$TEST_RUN_DIR/scanner-approved.json")
if [ "$STAGE" = "human-review" ]; then
  echo "PASS: Approved output has stage 'human-review'"
  PASS=$((PASS + 1))
else
  echo "FAIL: Expected stage 'human-review', got '$STAGE'"
  FAIL=$((FAIL + 1))
fi

echo ""
echo "Approval gate tests: $PASS passed, $FAIL failed"

if [ "$FAIL" -gt 0 ]; then
  exit 1
fi
