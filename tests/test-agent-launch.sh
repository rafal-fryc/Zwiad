#!/bin/bash
set -euo pipefail
# Test: Agent subprocess can be launched and exits cleanly
PASS=0
FAIL=0

echo "=== Test: Agent Launch ==="

# Preflight: verify agent files exist (pitfall #1 from research)
for agent in orchestrator scanner researcher reviewer categorizer; do
  if [ ! -f ".claude/agents/${agent}.md" ]; then
    echo "FAIL: Agent file missing: .claude/agents/${agent}.md"
    FAIL=$((FAIL + 1))
  else
    echo "PASS: Agent file exists: .claude/agents/${agent}.md"
    PASS=$((PASS + 1))
  fi
done

# Smoke test: launch scanner agent with a trivial prompt
# Uses --output-format json to get structured output
# Note: This test requires claude CLI to be available and may use tokens
echo ""
echo "--- Smoke test: launch scanner agent ---"
RESULT=$(claude -p --agent scanner --output-format json "Respond with exactly: AGENT_SMOKE_TEST_OK" 2>/dev/null) || {
  echo "FAIL: Scanner agent launch failed with non-zero exit"
  FAIL=$((FAIL + 1))
  echo ""
  echo "Results: $PASS passed, $FAIL failed"
  exit 1
}

if echo "$RESULT" | jq -e '.result' > /dev/null 2>&1; then
  echo "PASS: Scanner agent returned valid JSON with result field"
  PASS=$((PASS + 1))
else
  echo "FAIL: Scanner agent did not return valid JSON with result field"
  FAIL=$((FAIL + 1))
fi

echo ""
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] && exit 0 || exit 1
