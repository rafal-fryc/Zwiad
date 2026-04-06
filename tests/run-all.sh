#!/bin/bash
set -uo pipefail
TOTAL_PASS=0
TOTAL_FAIL=0

echo "==============================="
echo "  Zwiad Test Suite"
echo "==============================="
echo ""

# Run each test script and track results
for test_script in tests/test-*.sh; do
  echo "--- Running: $test_script ---"
  if bash "$test_script"; then
    TOTAL_PASS=$((TOTAL_PASS + 1))
  else
    TOTAL_FAIL=$((TOTAL_FAIL + 1))
  fi
  echo ""
done

echo "==============================="
echo "  Suite Results: $TOTAL_PASS scripts passed, $TOTAL_FAIL failed"
echo "==============================="
[ "$TOTAL_FAIL" -eq 0 ] && exit 0 || exit 1
