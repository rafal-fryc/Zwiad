---
phase: 02-scanner
plan: 01
subsystem: pipeline
tags: [scanner, bash, json-schema, jq, claude-cli, subagent]

# Dependency graph
requires:
  - phase: 01-agent-framework
    provides: directory structure, envelope schema, validate-handoff.sh, scanner.md stub
provides:
  - source config file with government URLs and search queries
  - full scanner agent prompt with Lexology parsing and web scanning logic
  - EML to HTML conversion wrapper script
  - scanner orchestration entry point (run-scanner.sh)
  - extended scanner schema with category and source_failures
affects: [02-scanner remaining plans, researcher agent, pipeline orchestration]

# Tech tracking
tech-stack:
  added: [eml-to-html (Python CLI dependency)]
  patterns: [source config externalization, scanner envelope output, run directory per pipeline execution]

key-files:
  created:
    - pipeline/config/sources.json
    - pipeline/scripts/convert-eml.sh
    - pipeline/scripts/run-scanner.sh
  modified:
    - .claude/agents/scanner.md
    - pipeline/schemas/scanner.schema.json
    - pipeline/schemas/scanner.jq

key-decisions:
  - "Source config uses direct_fetch + search_queries split for different scanning strategies"
  - "Scanner agent processes Lexology links sequentially to avoid rate limiting"
  - "Run directories use UTC timestamps for unique pipeline run isolation"

patterns-established:
  - "Source externalization: scanner reads sources from JSON config, not hardcoded in prompt"
  - "Run directory pattern: pipeline/runs/<timestamp>/ for per-execution state isolation"
  - "Script orchestration: bash script builds prompt, invokes claude -p --agent, validates output"

requirements-completed: [SCAN-01, SCAN-02, SCAN-03]

# Metrics
duration: 3min
completed: 2026-04-06
---

# Phase 02 Plan 01: Scanner Core Summary

**Source config with 3 government sites and 5 search queries, full scanner agent prompt with Lexology digest parsing and web source scanning, EML conversion wrapper, and run-scanner.sh orchestration script**

## Performance

- **Duration:** 3 min
- **Started:** 2026-04-06T23:04:51Z
- **Completed:** 2026-04-06T23:08:02Z
- **Tasks:** 3
- **Files modified:** 6

## Accomplishments
- Created externalized source config with 3 direct_fetch government sites (FTC, NIST CSRC, Congress.gov) and 5 search queries covering privacy, cybersecurity, and AI law
- Replaced scanner agent stub with 93-line prompt covering Lexology HTML digest parsing, source config scanning, URL normalization, error handling, and structured JSON output
- Built run-scanner.sh orchestration script supporting --eml, --html, and --sources-only modes with full pipeline flow: EML conversion, agent invocation, output validation, result reporting
- Extended scanner schema with category enum and source_failures array; updated jq validation

## Task Commits

Each task was committed atomically:

1. **Task 1: Create source config and extend scanner schema** - `e309978` (feat)
2. **Task 2: Write full scanner agent prompt and EML conversion script** - `ba5c03f` (feat)
3. **Task 3: Create run-scanner.sh orchestration script** - `909bdca` (feat)

## Files Created/Modified
- `pipeline/config/sources.json` - Externalized source definitions (3 direct_fetch, 5 search_queries)
- `pipeline/schemas/scanner.schema.json` - Extended with category enum and source_failures array
- `pipeline/schemas/scanner.jq` - Updated jq validation with category check
- `.claude/agents/scanner.md` - Full scanner agent prompt (93 lines)
- `pipeline/scripts/convert-eml.sh` - EML to HTML conversion wrapper using eml-to-html
- `pipeline/scripts/run-scanner.sh` - Scanner orchestration entry point

## Decisions Made
- Source config splits sources into direct_fetch (WebFetch) and search_queries (WebSearch) for different scanning strategies
- Scanner processes Lexology article links sequentially to avoid rate limiting
- Run directories use UTC timestamps under pipeline/runs/ for per-execution isolation
- Added Glob and Grep tools to scanner agent frontmatter for reading source config and checking existing reports

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered
None

## User Setup Required
None - no external service configuration required. Note: eml-to-html Python CLI must be installed for EML conversion to work (referenced in convert-eml.sh).

## Next Phase Readiness
- Scanner core is complete: source config, agent prompt, EML conversion, orchestration script
- Ready for remaining 02-scanner plans: dedup logic, human review generation, integration testing
- run-scanner.sh references dedup-findings.sh in its output message (to be created in future plan)

## Self-Check: PASSED

All 7 files found. All 3 commit hashes verified.

---
*Phase: 02-scanner*
*Completed: 2026-04-06*
