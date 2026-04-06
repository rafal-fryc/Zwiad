#!/bin/bash
set -euo pipefail
PASS=0
FAIL=0

echo "=== Test: Schema Validation (success cases) ==="

# Test 1: Valid scanner output passes envelope validation
if bash pipeline/scripts/validate-handoff.sh envelope tests/fixtures/valid-scanner-output.json > /dev/null 2>&1; then
  echo "PASS: Valid scanner output passes envelope validation"
  PASS=$((PASS + 1))
else
  echo "FAIL: Valid scanner output should pass envelope validation"
  FAIL=$((FAIL + 1))
fi

# Test 2: Valid scanner output passes scanner-specific validation
if bash pipeline/scripts/validate-handoff.sh scanner tests/fixtures/valid-scanner-output.json > /dev/null 2>&1; then
  echo "PASS: Valid scanner output passes scanner validation"
  PASS=$((PASS + 1))
else
  echo "FAIL: Valid scanner output should pass scanner validation"
  FAIL=$((FAIL + 1))
fi

# Test 3: Valid envelope-only passes envelope validation
if bash pipeline/scripts/validate-handoff.sh envelope tests/fixtures/valid-envelope-only.json > /dev/null 2>&1; then
  echo "PASS: Valid envelope-only passes envelope validation"
  PASS=$((PASS + 1))
else
  echo "FAIL: Valid envelope-only should pass envelope validation"
  FAIL=$((FAIL + 1))
fi

# Test 4: Empty findings array passes scanner validation
if bash pipeline/scripts/validate-handoff.sh scanner tests/fixtures/valid-envelope-only.json > /dev/null 2>&1; then
  echo "PASS: Empty findings array passes scanner validation"
  PASS=$((PASS + 1))
else
  echo "FAIL: Empty findings array should pass scanner validation"
  FAIL=$((FAIL + 1))
fi

echo ""
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] && exit 0 || exit 1
