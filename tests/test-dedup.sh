#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

PASS=0
FAIL=0

echo "=== Dedup Tests ==="

# Setup: create a temporary pipeline run with fixture data
TEST_RUN_ID="test-dedup-$(date +%s)"
TEST_RUN_DIR="$PROJECT_ROOT/pipeline/runs/$TEST_RUN_ID"
mkdir -p "$TEST_RUN_DIR"
trap 'rm -rf "$TEST_RUN_DIR"' EXIT

# Copy scanner output fixture to test run directory
cp "$SCRIPT_DIR/fixtures/sample-scanner-output.json" "$TEST_RUN_DIR/scanner-output.json"

# Setup: create temporary reports directory with fixture report
# The dedup script reads from $PROJECT_ROOT/reports/
# We need the fixture report in place for the test
FIXTURE_REPORT_DIR="$PROJECT_ROOT/reports/privacy"
mkdir -p "$FIXTURE_REPORT_DIR"
# Only copy if not already there (don't clobber real reports)
FIXTURE_REPORT="$FIXTURE_REPORT_DIR/sample-existing-report.md"
COPIED_FIXTURE=false
if [ ! -f "$FIXTURE_REPORT" ]; then
  cp "$SCRIPT_DIR/fixtures/sample-reports/privacy/sample-existing-report.md" "$FIXTURE_REPORT"
  COPIED_FIXTURE=true
fi
trap 'rm -rf "$TEST_RUN_DIR"; if [ "$COPIED_FIXTURE" = true ]; then rm -f "$FIXTURE_REPORT"; fi' EXIT

# Run dedup
"$PROJECT_ROOT/pipeline/scripts/dedup-findings.sh" "$TEST_RUN_ID"

# Test 1: Deduped output file exists
if [ -f "$TEST_RUN_DIR/scanner-deduped.json" ]; then
  echo "PASS: scanner-deduped.json created"
  PASS=$((PASS + 1))
else
  echo "FAIL: scanner-deduped.json not created"
  FAIL=$((FAIL + 1))
fi

# Test 2: Duplicates log exists
if [ -f "$TEST_RUN_DIR/scanner-duplicates.json" ]; then
  echo "PASS: scanner-duplicates.json created"
  PASS=$((PASS + 1))
else
  echo "FAIL: scanner-duplicates.json not created"
  FAIL=$((FAIL + 1))
fi

# Test 3: FTC finding (URL match) was removed -- finding 002 URL matches existing report
DEDUPED_COUNT=$(jq '.data.findings | length' "$TEST_RUN_DIR/scanner-deduped.json")
if [ "$DEDUPED_COUNT" -eq 2 ]; then
  echo "PASS: Dedup removed 1 duplicate (3 -> 2 findings)"
  PASS=$((PASS + 1))
else
  echo "FAIL: Expected 2 findings after dedup, got $DEDUPED_COUNT"
  FAIL=$((FAIL + 1))
fi

# Test 4: The removed finding was the FTC one (URL match)
FTC_PRESENT=$(jq '[.data.findings[] | select(.id == "SCAN-20260406-002")] | length' "$TEST_RUN_DIR/scanner-deduped.json")
if [ "$FTC_PRESENT" -eq 0 ]; then
  echo "PASS: FTC duplicate correctly removed"
  PASS=$((PASS + 1))
else
  echo "FAIL: FTC duplicate should have been removed but is still present"
  FAIL=$((FAIL + 1))
fi

# Test 5: Non-duplicate findings preserved
IOWA_PRESENT=$(jq '[.data.findings[] | select(.id == "SCAN-20260406-001")] | length' "$TEST_RUN_DIR/scanner-deduped.json")
CO_PRESENT=$(jq '[.data.findings[] | select(.id == "SCAN-20260406-003")] | length' "$TEST_RUN_DIR/scanner-deduped.json")
if [ "$IOWA_PRESENT" -eq 1 ] && [ "$CO_PRESENT" -eq 1 ]; then
  echo "PASS: Non-duplicate findings preserved"
  PASS=$((PASS + 1))
else
  echo "FAIL: Non-duplicate findings missing (Iowa=$IOWA_PRESENT, Colorado=$CO_PRESENT)"
  FAIL=$((FAIL + 1))
fi

# Test 6: Duplicates log contains the removed finding
DUPE_COUNT=$(jq 'length' "$TEST_RUN_DIR/scanner-duplicates.json")
if [ "$DUPE_COUNT" -ge 1 ]; then
  echo "PASS: Duplicates log has entries"
  PASS=$((PASS + 1))
else
  echo "FAIL: Duplicates log is empty"
  FAIL=$((FAIL + 1))
fi

echo ""
echo "Dedup tests: $PASS passed, $FAIL failed"

if [ "$FAIL" -gt 0 ]; then
  exit 1
fi
