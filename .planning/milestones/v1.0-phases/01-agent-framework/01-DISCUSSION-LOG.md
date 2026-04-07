# Phase 1: Agent Framework - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-04-06
**Phase:** 01-agent-framework
**Areas discussed:** Agent definitions, JSON state contracts, Pipeline orchestration, Directory structure

---

## Agent Definitions

| Option | Description | Selected |
|--------|-------------|----------|
| Opus for deep work, Sonnet for coordination | Researcher + Reviewer get opus. Scanner, Categorizer, Orchestrator get sonnet. | ✓ |
| All sonnet to start | Cheaper iteration during development. Upgrade later. | |
| All opus | Maximum quality everywhere. Higher cost. | |

**User's choice:** Opus for deep work, Sonnet for coordination
**Notes:** Matches CLAUDE.md recommendations.

| Option | Description | Selected |
|--------|-------------|----------|
| Strict per-agent allowlists | Scanner: WebSearch+WebFetch+Read+Write. Reviewer: Read+WebFetch only. Etc. | ✓ |
| All agents get all tools | Simpler setup, rely on prompts. | |
| Minimal tools, add as needed | Start with Read only, add incrementally. | |

**User's choice:** Strict per-agent allowlists
**Notes:** None

| Option | Description | Selected |
|--------|-------------|----------|
| Yes, per-agent caps | Scanner: 20 turns. Researcher: $3/finding. Etc. | |
| Turn limits only | No dollar caps, rely on turn counts. | |
| No limits initially | Let agents run freely during development. | ✓ |

**User's choice:** No limits initially
**Notes:** Will add limits once usage patterns are understood.

| Option | Description | Selected |
|--------|-------------|----------|
| All 5 agents as stubs | Real frontmatter, placeholder system prompts. | ✓ |
| Only orchestrator + one test agent | Minimal to prove the framework. | |
| All 5 agents fully specified | Complete system prompts now. | |

**User's choice:** All 5 agents as stubs
**Notes:** Later phases fill in the prompts.

---

## JSON State Contracts

| Option | Description | Selected |
|--------|-------------|----------|
| JSON Schema files + bash validation script | .json schemas in pipeline/schemas/. Bash+jq validates. No Node/Python. | ✓ |
| Schema in agent prompts only | Describe structure in prompts. Trust LLM output. | |
| TypeScript/Zod schemas with Node validation | Formal typed schemas. Adds Node dependency. | |

**User's choice:** JSON Schema files + bash validation script
**Notes:** None

| Option | Description | Selected |
|--------|-------------|----------|
| Hard fail with error message | Pipeline stops. Error shows which field failed. | ✓ |
| Retry the producing agent once | Feed error back to agent, retry once, then stop. | |
| Log warning and continue | Record violation, let next agent try. | |

**User's choice:** Hard fail with error message
**Notes:** None

| Option | Description | Selected |
|--------|-------------|----------|
| One file per stage with common envelope | {pipeline_run_id, timestamp, stage, status, data: {...}} | ✓ |
| Single accumulating state file | One file, each agent appends. | |
| Separate input/output files per stage | Dedicated input/output per agent. | |

**User's choice:** One file per stage with common envelope
**Notes:** None

| Option | Description | Selected |
|--------|-------------|----------|
| Simple version field, no migration | schema_version: "1.0". Fail on mismatch. | ✓ |
| No versioning for v1 | Skip entirely. Add later. | |
| Full semver with migration scripts | Formal versioning with migration. | |

**User's choice:** Simple version field, no migration
**Notes:** None

---

## Pipeline Orchestration

| Option | Description | Selected |
|--------|-------------|----------|
| Bash script calling claude -p sequentially | run-pipeline.sh invokes each agent. Simple, debuggable. | |
| Orchestrator agent spawning subagents | Main agent uses Agent tool to spawn scanner, researcher, etc. | ✓ |
| Hybrid: bash for flow, orchestrator for decisions | Bash handles stage flow, orchestrator handles decisions. | |

**User's choice:** Orchestrator agent spawning subagents
**Notes:** User prefers the agentic approach over bash scripting.

| Option | Description | Selected |
|--------|-------------|----------|
| Write findings to file, pause, user re-runs | Orchestrator writes review file. Pipeline pauses. User re-runs after review. | ✓ |
| Interactive prompt during pipeline run | Present findings inline, wait for y/n. | |
| Approval via file editing | User edits JSON to set approved: true. | |

**User's choice:** Write findings to file, pause, user re-runs
**Notes:** None

| Option | Description | Selected |
|--------|-------------|----------|
| Fail fast, log error, stop pipeline | Non-zero exit or invalid output stops everything. | ✓ |
| Retry once, then fail | One retry on failure. | |
| Skip failed findings, continue others | Partial results on failure. | |

**User's choice:** Fail fast, log error, stop pipeline
**Notes:** None

| Option | Description | Selected |
|--------|-------------|----------|
| One finding at a time | Each finding goes through full pipeline before next. | |
| Batch all findings per stage | All findings to researcher, then all to reviewer, etc. | ✓ |
| Parallel processing | Multiple findings simultaneously. | |

**User's choice:** Batch all findings per stage
**Notes:** None

---

## Directory Structure

| Option | Description | Selected |
|--------|-------------|----------|
| Timestamped run directories | pipeline/runs/2026-04-06T14-30-00/ | ✓ |
| Stage-based directories | pipeline/scanner/, pipeline/researcher/, etc. | |
| Flat with naming convention | All files in pipeline/ with prefixed names. | |

**User's choice:** Timestamped run directories
**Notes:** None

| Option | Description | Selected |
|--------|-------------|----------|
| Top-level /reports with topic subdirs | reports/privacy/, reports/cybersecurity/, reports/ai-law/ | ✓ |
| Under /output | output/reports/privacy/ etc. | |
| Top-level topic folders | privacy/, cybersecurity/, ai-law/ at repo root. | |

**User's choice:** Top-level /reports with topic subdirs
**Notes:** None

| Option | Description | Selected |
|--------|-------------|----------|
| /input directory | input/ at repo root. | ✓ |
| Passed as CLI argument | User provides path when triggering. | |
| Both: default + CLI override | Check input/ by default, CLI overrides. | |

**User's choice:** /input directory
**Notes:** None

| Option | Description | Selected |
|--------|-------------|----------|
| pipeline/schemas/ | Schemas live next to pipeline code. | ✓ |
| Top-level /schemas | schemas/ at repo root. | |
| You decide | Claude picks during implementation. | |

**User's choice:** pipeline/schemas/
**Notes:** User initially asked what schemas are for — explained they define inter-agent handoff data structure for PIPE-06 validation.

---

## Claude's Discretion

- Exact JSON schema field names and types
- Validation script implementation details
- Agent stub placeholder content
- Pipeline run ID format

## Deferred Ideas

None — discussion stayed within phase scope
