#!/bin/bash
set -euo pipefail

# Phase 5 Pipeline Integration Tests
# Validates all pipeline components without running the actual pipeline (no claude CLI invocations).
# Usage: bash pipeline/scripts/test-pipeline.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

PASS=0
FAIL=0
TOTAL=0

check() {
  TOTAL=$((TOTAL + 1))
  local desc="$1"
  shift
  if "$@" >/dev/null 2>&1; then
    echo "  PASS: $desc"
    PASS=$((PASS + 1))
  else
    echo "  FAIL: $desc"
    FAIL=$((FAIL + 1))
  fi
}

echo "=== Phase 5 Pipeline Integration Tests ==="
echo ""

# --- 1. Categories.json ---
echo "1. Categories Registry"
check "categories.json is valid JSON" jq empty "$PROJECT_ROOT/pipeline/config/categories.json"
check "has 3 topics" test "$(jq '.topics | keys | length' "$PROJECT_ROOT/pipeline/config/categories.json")" -eq 3
check "privacy has subcategories" test "$(jq '.topics.privacy.subcategories | length' "$PROJECT_ROOT/pipeline/config/categories.json")" -gt 0
check "cybersecurity has subcategories" test "$(jq '.topics.cybersecurity.subcategories | length' "$PROJECT_ROOT/pipeline/config/categories.json")" -gt 0
check "ai-law has subcategories" test "$(jq '.topics["ai-law"].subcategories | length' "$PROJECT_ROOT/pipeline/config/categories.json")" -gt 0
echo ""

# --- 2. Categorizer Schema (extended) ---
echo "2. Categorizer Schema Validation"
TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT

# Test basic categorizer output
cat > "$TMPDIR/basic.json" << 'FIXTURE'
{
  "schema_version": "1.0",
  "pipeline_run_id": "test-run",
  "timestamp": "2026-04-07T00:00:00Z",
  "stage": "categorizer",
  "status": "complete",
  "data": {
    "filed_reports": [{
      "finding_id": "SCAN-20260407-001",
      "source_path": "reports/privacy/test-report.md",
      "destination_path": "reports/privacy/data-breach/test-report.md",
      "topic": "privacy",
      "subcategory": "data-breach"
    }]
  }
}
FIXTURE
check "basic categorizer output validates" "$PROJECT_ROOT/pipeline/scripts/validate-handoff.sh" categorizer "$TMPDIR/basic.json"

# Test extended categorizer output (with is_pending and symlinks)
cat > "$TMPDIR/extended.json" << 'FIXTURE'
{
  "schema_version": "1.0",
  "pipeline_run_id": "test-run",
  "timestamp": "2026-04-07T00:00:00Z",
  "stage": "categorizer",
  "status": "complete",
  "data": {
    "filed_reports": [{
      "finding_id": "SCAN-20260407-002",
      "source_path": "reports/privacy/new-report.md",
      "destination_path": "pipeline/pending/SCAN-20260407-002-pending.md",
      "topic": "privacy",
      "subcategory": "biometric-data",
      "is_pending": true,
      "proposed_subcategory": "biometric-data",
      "symlinks": []
    }]
  }
}
FIXTURE
check "extended categorizer output (pending) validates" jq -e -f "$PROJECT_ROOT/pipeline/schemas/categorizer.jq" "$TMPDIR/extended.json"

# Test with symlinks
cat > "$TMPDIR/symlinks.json" << 'FIXTURE'
{
  "schema_version": "1.0",
  "pipeline_run_id": "test-run",
  "timestamp": "2026-04-07T00:00:00Z",
  "stage": "categorizer",
  "status": "complete",
  "data": {
    "filed_reports": [{
      "finding_id": "SCAN-20260407-003",
      "source_path": "reports/privacy/cross-report.md",
      "destination_path": "reports/privacy/enforcement-actions/cross-report.md",
      "topic": "privacy",
      "subcategory": "enforcement-actions",
      "is_pending": false,
      "symlinks": ["reports/cybersecurity/enforcement-actions/cross-report.md"]
    }]
  }
}
FIXTURE
check "extended categorizer output (symlinks) validates" jq -e -f "$PROJECT_ROOT/pipeline/schemas/categorizer.jq" "$TMPDIR/symlinks.json"
echo ""

# --- 3. Agent Definitions ---
echo "3. Agent Definitions"
check "categorizer.md exists" test -f "$PROJECT_ROOT/.claude/agents/categorizer.md"
check "categorizer.md references categories.json" grep -q "categories.json" "$PROJECT_ROOT/.claude/agents/categorizer.md"
check "categorizer.md references pending flow" grep -q "pending" "$PROJECT_ROOT/.claude/agents/categorizer.md"
check "orchestrator.md exists" test -f "$PROJECT_ROOT/.claude/agents/orchestrator.md"
check "orchestrator.md has scan phase" grep -q "Scan phase\|scan phase\|scan-complete" "$PROJECT_ROOT/.claude/agents/orchestrator.md"
check "orchestrator.md has research phase" grep -q "Research phase\|research phase\|pipeline-complete" "$PROJECT_ROOT/.claude/agents/orchestrator.md"
echo ""

# --- 4. Python Entry Point ---
echo "4. Python Entry Point"
check "run_pipeline.py exists" test -f "$PROJECT_ROOT/run_pipeline.py"
check "run_pipeline.py is valid Python" python3 -c "import ast; ast.parse(open('$PROJECT_ROOT/run_pipeline.py').read())"
check "run_pipeline.py --help works" python3 "$PROJECT_ROOT/run_pipeline.py" --help
check "run_pipeline.py run --help works" python3 "$PROJECT_ROOT/run_pipeline.py" run --help
check "run_pipeline.py resume --help works" python3 "$PROJECT_ROOT/run_pipeline.py" resume --help
echo ""

# --- 5. Cron Setup ---
echo "5. Cron Setup"
check "crontab.example exists" test -f "$PROJECT_ROOT/pipeline/cron/crontab.example"
check "install-cron.sh exists" test -f "$PROJECT_ROOT/pipeline/cron/install-cron.sh"
check "install-cron.sh is valid bash" bash -n "$PROJECT_ROOT/pipeline/cron/install-cron.sh"
check "pending directory exists" test -d "$PROJECT_ROOT/pipeline/pending"
echo ""

# --- 6. Directory Structure ---
echo "6. Directory Structure"
check "reports/privacy/ exists" test -d "$PROJECT_ROOT/reports/privacy"
check "reports/cybersecurity/ exists" test -d "$PROJECT_ROOT/reports/cybersecurity"
check "reports/ai-law/ exists" test -d "$PROJECT_ROOT/reports/ai-law"
echo ""

# --- Summary ---
echo "==========================="
echo "Results: $PASS/$TOTAL passed, $FAIL failed"
if [ "$FAIL" -gt 0 ]; then
  echo "SOME TESTS FAILED"
  exit 1
else
  echo "ALL TESTS PASSED"
  exit 0
fi
