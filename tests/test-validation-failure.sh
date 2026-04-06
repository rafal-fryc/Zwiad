#!/bin/bash
set -euo pipefail
PASS=0
FAIL=0

echo "=== Test: Validation Failures (expected rejections) ==="

# Test 1: Invalid JSON is caught
if bash pipeline/scripts/validate-handoff.sh envelope tests/fixtures/invalid-json.txt > /dev/null 2>&1; then
  echo "FAIL: Invalid JSON should be rejected"
  FAIL=$((FAIL + 1))
else
  echo "PASS: Invalid JSON correctly rejected"
  PASS=$((PASS + 1))
fi

# Test 2: Missing required field is caught
if bash pipeline/scripts/validate-handoff.sh envelope tests/fixtures/missing-field.json > /dev/null 2>&1; then
  echo "FAIL: Missing field should be rejected"
  FAIL=$((FAIL + 1))
else
  echo "PASS: Missing field correctly rejected"
  PASS=$((PASS + 1))
fi

# Test 3: Wrong schema version is caught
if bash pipeline/scripts/validate-handoff.sh envelope tests/fixtures/wrong-version.json > /dev/null 2>&1; then
  echo "FAIL: Wrong version should be rejected"
  FAIL=$((FAIL + 1))
else
  echo "PASS: Wrong version correctly rejected"
  PASS=$((PASS + 1))
fi

# Test 4: Invalid scanner data is caught at stage level
if bash pipeline/scripts/validate-handoff.sh scanner tests/fixtures/invalid-scanner-data.json > /dev/null 2>&1; then
  echo "FAIL: Invalid scanner data should be rejected"
  FAIL=$((FAIL + 1))
else
  echo "PASS: Invalid scanner data correctly rejected"
  PASS=$((PASS + 1))
fi

# Test 5: Nonexistent file is caught
if bash pipeline/scripts/validate-handoff.sh envelope tests/fixtures/does-not-exist.json > /dev/null 2>&1; then
  echo "FAIL: Nonexistent file should be rejected"
  FAIL=$((FAIL + 1))
else
  echo "PASS: Nonexistent file correctly rejected"
  PASS=$((PASS + 1))
fi

echo ""
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] && exit 0 || exit 1
