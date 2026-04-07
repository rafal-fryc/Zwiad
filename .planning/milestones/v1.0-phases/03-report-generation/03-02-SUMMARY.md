---
phase: 03-report-generation
plan: 02
subsystem: pipeline-orchestration
tags: [researcher, orchestration, test-fixtures, validation, schema-compliance]

requires:
  - phase: 03-report-generation
    plan: 01
    provides: "Researcher agent definition, report templates, researcher schema and jq rules"
  - phase: 02-scanner
    provides: "run-scanner.sh pattern, validate-handoff.sh, approve-findings.sh, scanner-approved.json format"

provides:
  - "run-researcher.sh orchestration script for invoking researcher agent per finding"
  - "Test fixtures: approved findings, researcher output, sample client-alert and research-memo reports"
  - "test-researcher-validation.sh covering REPT-01 through REPT-04"

affects:
  - "tests/run-all.sh (auto-discovers new test script)"

tech_stack:
  added: []
  patterns:
    - "Per-finding agent invocation with validation after each call"
    - "Report path validation regex for category enforcement (T-03-03)"
    - "Warn-and-continue pattern for non-blocking failures (T-03-06)"

key_files:
  created:
    - pipeline/scripts/run-researcher.sh
    - tests/fixtures/sample-approved-findings.json
    - tests/fixtures/sample-researcher-output.json
    - tests/fixtures/sample-reports/client-alert-sample.md
    - tests/fixtures/sample-reports/research-memo-sample.md
    - tests/test-researcher-validation.sh
  modified: []

decisions:
  - "Followed run-scanner.sh pattern for orchestration script structure (SCRIPT_DIR/PROJECT_ROOT resolution, argument parsing, loop with validation)"
  - "Used warn-and-continue for missing researcher output files to allow partial pipeline success"

metrics:
  duration: "159s"
  completed: "2026-04-07T00:41:58Z"
  tasks_completed: 2
  tasks_total: 2
  files_created: 6
  files_modified: 0
  test_count: 15
  test_pass: 15
---

# Phase 03 Plan 02: Researcher Orchestration and Test Fixtures Summary

Orchestration script wires researcher agent into pipeline with per-finding invocation, schema validation, and path traversal mitigation; 15 fixture-based tests validate all REPT requirements.

## What Was Built

### Task 1: Orchestration Script and Test Fixtures

**pipeline/scripts/run-researcher.sh** -- Follows the established run-scanner.sh pattern:
- Accepts RUN_ID argument, reads scanner-approved.json from the run directory
- Iterates approved findings, invoking `claude -p --agent researcher --output-format json --max-turns 30` per finding
- Validates each output via `validate-handoff.sh researcher`
- Validates report_path matches `^reports/(privacy|cybersecurity|ai-law)/` regex (T-03-03 mitigation)
- Warn-and-continue on missing output files (T-03-06 mitigation)
- Prints summary with success/failure counts

**Test Fixtures:**
- `sample-approved-findings.json` -- 2 findings (high-relevance privacy/legislation, medium-relevance cybersecurity/enforcement)
- `sample-researcher-output.json` -- Valid researcher envelope with 2 reports matching schema
- `client-alert-sample.md` -- Realistic client-alert with all D-02 sections and confidence tags
- `research-memo-sample.md` -- Realistic research-memo with all D-02 sections and confidence tags

### Task 2: Researcher Validation Test Script

**tests/test-researcher-validation.sh** -- 15 tests organized by requirement:
- REPT-01 (3 tests): Schema validation via validate-handoff.sh, report_path field, jurisdiction_tags array
- REPT-02 (3 tests): Format selection mapping (high->client-alert, medium->research-memo), enum validation
- REPT-03 (3 tests): Confidence summary counts, confidence tags in headings for both report formats
- REPT-04 (2 tests): Related Reports section exists in both sample reports
- Content validation (4 tests): All required sections present per D-02 templates, Sources section, report paths prefix

Auto-discovered by `tests/run-all.sh` via the `test-*.sh` glob pattern.

## Verification Results

- `bash tests/test-researcher-validation.sh` -- 15/15 passed
- `bash tests/run-all.sh` -- 7/7 test scripts passed, 0 failed
- `pipeline/scripts/run-researcher.sh` is executable with path validation
- All fixture JSON files pass `jq empty`
- Sample reports contain all required D-02 sections

## Deviations from Plan

None -- plan executed exactly as written.

## Commits

| Task | Commit | Description |
|------|--------|-------------|
| 1 | 81a4bd3 | feat(03-02): add researcher orchestration script and test fixtures |
| 2 | 3a9a10a | test(03-02): add researcher validation test script covering REPT-01 through REPT-04 |

## Self-Check: PASSED
