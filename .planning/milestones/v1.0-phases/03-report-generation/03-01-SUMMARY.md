---
phase: 03-report-generation
plan: 01
subsystem: agents
tags: [markdown-templates, agent-prompts, researcher, confidence-tagging, citations]

requires:
  - phase: 01-agent-framework
    provides: "Researcher agent stub, pipeline schemas (researcher.schema.json, scanner.schema.json, envelope.schema.json), directory structure"
  - phase: 02-scanner
    provides: "Scanner finding fields (id, title, relevance, category, jurisdiction) that serve as researcher input"
provides:
  - "Client-alert report template (pipeline/templates/client-alert.md)"
  - "Research-memo report template (pipeline/templates/research-memo.md)"
  - "Complete researcher agent system prompt encoding D-01 through D-10"
affects: [03-report-generation, 04-review-cycle, 05-categorization]

tech-stack:
  added: []
  patterns:
    - "Report templates as separate files with YAML frontmatter and placeholder syntax"
    - "Agent system prompts structured with critical rules first (official legal text, confidence definitions)"
    - "Section-level confidence tagging in report headings"

key-files:
  created:
    - "pipeline/templates/client-alert.md"
    - "pipeline/templates/research-memo.md"
  modified:
    - ".claude/agents/researcher.md"

key-decisions:
  - "Templates stored as separate files rather than inline in system prompt -- allows template changes without prompt changes"
  - "Official legal text mandate (D-06) placed early in prompt for maximum agent attention"
  - "Confidence tagging at section level, not claim level, for clean readability"

patterns-established:
  - "Report template pattern: YAML frontmatter + H1 title + metadata line + H2 sections with confidence placeholders"
  - "Agent prompt structure: critical rules first, process steps middle, error handling last"

requirements-completed: [REPT-01, REPT-02, REPT-03, REPT-04]

duration: 4min
completed: 2026-04-07
---

# Phase 3 Plan 1: Report Templates and Researcher Prompt Summary

**Two report templates (client-alert, research-memo) and full researcher agent prompt encoding format selection, confidence tagging, citation rules, official legal text mandate, and related-reports discovery**

## Performance

- **Duration:** 4 min
- **Started:** 2026-04-07T00:31:59Z
- **Completed:** 2026-04-07T00:36:46Z
- **Tasks:** 2
- **Files modified:** 3

## Accomplishments
- Created client-alert template with Summary, Key Facts, Action Items, Related Reports, Sources sections and YAML frontmatter
- Created research-memo template with Executive Summary, Background, Detailed Analysis, Impact Assessment, Action Items, Related Reports, Sources sections
- Wrote 178-line researcher agent system prompt encoding all 10 user decisions (D-01 through D-10)
- Prompt places critical rules (official legal text mandate, confidence definitions) in the first half for maximum agent attention

## Task Commits

Each task was committed atomically:

1. **Task 1: Create report templates** - `8e51cab` (feat)
2. **Task 2: Write full researcher agent system prompt** - `a557093` (feat)

## Files Created/Modified
- `pipeline/templates/client-alert.md` - Client-alert report template with 7 sections, YAML frontmatter, confidence placeholders, HTML guidance comments
- `pipeline/templates/research-memo.md` - Research-memo report template with 9 sections, YAML frontmatter, confidence placeholders, HTML guidance comments
- `.claude/agents/researcher.md` - Complete researcher agent definition with 11 sections covering format selection, research depth, confidence tagging, citation format, related reports, output JSON, and error handling

## Decisions Made
- Templates stored as separate files in `pipeline/templates/` rather than inline in the system prompt, allowing template updates without modifying the agent prompt
- Official legal text requirement (D-06) placed as second section in prompt (after role intro) to ensure maximum agent attention on this critical non-negotiable rule
- Confidence definitions placed immediately after D-06 section, keeping the two most important quality rules in the prompt's first half

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered
None

## User Setup Required
None - no external service configuration required.

## Next Phase Readiness
- Report templates ready for researcher agent to read during report generation
- Researcher agent prompt complete and ready for orchestration script (Plan 02) to invoke via `claude -p --agent researcher`
- Templates are referenced by path in the researcher prompt (`pipeline/templates/client-alert.md`, `pipeline/templates/research-memo.md`)

## Self-Check: PASSED

All files exist, all commits verified.

---
*Phase: 03-report-generation*
*Completed: 2026-04-07*
