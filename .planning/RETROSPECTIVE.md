# Project Retrospective

*A living document updated after each milestone. Lessons feed forward into future planning.*

## Milestone: v1.0 — MVP

**Shipped:** 2026-04-07
**Phases:** 5 | **Plans:** 14

### What Was Built
- Multi-agent regulatory monitoring pipeline with 5 Claude Code subagents (scanner, researcher, reviewer, categorizer, orchestrator)
- JSON state handoff contracts with jq schema validation at every stage boundary
- Scanner with Lexology digest parsing, government source scanning, two-pass dedup, and human approval gate
- Researcher with dual report formats (client-alert/research-memo), confidence tagging, and official legal text mandate
- Reviewer with source re-fetch + independent verification, 3-round iteration, and human escalation
- Categorizer with seed+emergent subcategory strategy and human review for new subcategories
- Python CLI entry point with run/resume subcommands, audit logging, and desktop notifications
- Cron scheduling with Tegra-specific environment detection

### What Worked
- Phase-by-phase planning with context gathering before each phase produced focused, implementable plans
- JSON schema-first approach meant agent contracts were clear before agent prompts were written
- Reusing the APPROVED marker pattern across scanner approval and reviewer escalation kept the UX consistent
- Existing bash scripts (validate-handoff.sh, approve-findings.sh) stayed useful through all phases

### What Was Inefficient
- Worktree merges lost commits during Phase 5 execution — continuation agents started from wrong base, requiring re-execution of plan 05-02
- Requirements traceability table was never updated during execution — all 19 requirements still show "Pending" despite being implemented
- No live pipeline runs during development — all testing was component-level, no end-to-end validation with real data

### Patterns Established
- Agent definitions in `.claude/agents/*.md` with frontmatter (model, tools, permissionMode)
- JSON state files with common envelope (schema_version, pipeline_run_id, timestamp, stage, status, data)
- Timestamped pipeline run directories: `pipeline/runs/YYYY-MM-DDTHH-MM-SS/`
- Human approval via markdown file + `## APPROVED` marker
- Config files in `pipeline/config/` for source lists and category registries
- Python entry point calling `claude -p --agent` via subprocess

### Key Lessons
1. Worktree-based parallel execution needs careful branch base verification — agents can silently start from the wrong commit
2. Requirements status should be updated atomically when phases complete, not deferred to milestone
3. Component tests are necessary but insufficient — an end-to-end smoke test with real data should be the first post-milestone activity

### Cost Observations
- Model mix: ~60% opus (researcher, planner, executor), ~40% sonnet (checker, verifier, scanner)
- Notable: Single-agent-per-wave execution meant no real parallelism benefit from worktrees in Phase 5

---

## Cross-Milestone Trends

### Process Evolution

| Milestone | Phases | Plans | Key Change |
|-----------|--------|-------|------------|
| v1.0 | 5 | 14 | Initial establishment of agent pipeline patterns |

### Cumulative Quality

| Milestone | Tests | Key Validation |
|-----------|-------|----------------|
| v1.0 | 55+ assertions | Component-level (jq validation, dedup, approval gate, reviewer iteration) |

### Top Lessons (Verified Across Milestones)

1. Schema-first design pays off — clear contracts between agents prevent integration surprises
2. Human approval gates should follow one consistent pattern (markdown + marker) across all pipeline stages
