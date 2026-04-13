#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

PASS=0
FAIL=0

echo "=== Dedup Tests ==="

# Setup: temporary pipeline run + isolated fixture index
TEST_RUN_ID="test-dedup-$(date +%s)"
TEST_RUN_DIR="$PROJECT_ROOT/pipeline/runs/$TEST_RUN_ID"
mkdir -p "$TEST_RUN_DIR"

TEST_INDEX=$(mktemp --suffix=.json)
trap 'rm -rf "$TEST_RUN_DIR" "$TEST_INDEX"' EXIT

# Copy scanner output fixture to the test run directory
cp "$SCRIPT_DIR/fixtures/sample-scanner-output.json" "$TEST_RUN_DIR/scanner-output.json"

# Build an isolated reports/index.json with only the FTC finding's URL.
# This simulates "this URL has already been filed in a prior report" without
# touching the real reports/index.json or the reports/ tree.
cat > "$TEST_INDEX" <<'EOF'
{
  "schema_version": "1.0",
  "last_updated": "2026-04-06T00:00:00Z",
  "reports": {
    "ftc-data-broker-rules-2026": {
      "topic_key": "ftc-data-broker-rules-2026",
      "topic_type": "rulemaking",
      "topic_key_confidence": "high",
      "report_path": "reports/privacy/ftc-data-broker-rules-2026-04-01.md",
      "title": "FTC Proposes New Data Broker Rules",
      "category": "privacy",
      "first_reported": "2026-04-01",
      "last_updated": "2026-04-01",
      "source_urls": [
        "https://www.ftc.gov/news-events/news/press-releases/2026/04/ftc-data-broker-rules"
      ],
      "status_history": [],
      "finding_ids": []
    }
  },
  "url_index": {
    "https://www.ftc.gov/news-events/news/press-releases/2026/04/ftc-data-broker-rules": "ftc-data-broker-rules-2026"
  }
}
EOF

# Run dedup against the isolated index
INDEX_PATH="$TEST_INDEX" "$PROJECT_ROOT/pipeline/scripts/dedup-findings.sh" "$TEST_RUN_ID"

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

# Test 3: Total count dropped from 3 to 2
DEDUPED_COUNT=$(jq '.data.findings | length' "$TEST_RUN_DIR/scanner-deduped.json")
if [ "$DEDUPED_COUNT" -eq 2 ]; then
  echo "PASS: Dedup removed 1 duplicate (3 -> 2 findings)"
  PASS=$((PASS + 1))
else
  echo "FAIL: Expected 2 findings after dedup, got $DEDUPED_COUNT"
  FAIL=$((FAIL + 1))
fi

# Test 4: FTC finding (URL match against the isolated index) was removed
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

# Test 6: Duplicates log contains the removed finding with a dedup_reason
DUPE_COUNT=$(jq 'length' "$TEST_RUN_DIR/scanner-duplicates.json")
if [ "$DUPE_COUNT" -ge 1 ]; then
  echo "PASS: Duplicates log has entries"
  PASS=$((PASS + 1))
else
  echo "FAIL: Duplicates log is empty"
  FAIL=$((FAIL + 1))
fi

# Test 7: Dedup reason is recorded (url_match, noise, or topic_key_match)
REASON=$(jq -r '.[0].dedup_reason // empty' "$TEST_RUN_DIR/scanner-duplicates.json")
case "$REASON" in
  url_match|topic_key_match|noise)
    echo "PASS: Dedup reason recorded ($REASON)"
    PASS=$((PASS + 1))
    ;;
  *)
    echo "FAIL: Expected url_match, topic_key_match, or noise; got '$REASON'"
    FAIL=$((FAIL + 1))
    ;;
esac

# Test 8: Phase 2 — candidate_updates key exists in deduped output (may be empty)
HAS_UPDATES_KEY=$(jq '.data | has("candidate_updates")' "$TEST_RUN_DIR/scanner-deduped.json")
if [ "$HAS_UPDATES_KEY" = "true" ]; then
  echo "PASS: candidate_updates key present in deduped output"
  PASS=$((PASS + 1))
else
  echo "FAIL: candidate_updates key missing from deduped output"
  FAIL=$((FAIL + 1))
fi

echo ""
echo "Dedup tests: $PASS passed, $FAIL failed"

if [ "$FAIL" -gt 0 ]; then
  exit 1
fi
