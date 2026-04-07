# Phase 1: Agent Framework - Context

**Gathered:** 2026-04-06
**Status:** Ready for planning

<domain>
## Phase Boundary

Establish the subprocess agent infrastructure and shared JSON state contracts that all subsequent agents (scanner, researcher, reviewer, categorizer) build on. This phase delivers the skeleton — agent definitions, JSON schemas, validation, orchestrator, and directory structure — not the agent-specific logic.

</domain>

<decisions>
## Implementation Decisions

### Agent Definitions
- **D-01:** Model assignment follows role complexity: opus for deep work (researcher, reviewer), sonnet for coordination (scanner, categorizer, orchestrator)
- **D-02:** Each agent gets strict per-agent tool allowlists in frontmatter. Scanner: WebSearch+WebFetch+Read+Write. Researcher: WebSearch+WebFetch+Read+Write. Reviewer: Read+WebFetch only. Categorizer: Read+Write+Glob only.
- **D-03:** No budget caps or turn limits initially. Add limits once actual usage patterns are understood.
- **D-04:** Phase 1 creates all 5 agent definition files (.claude/agents/) as stubs — real frontmatter (model, tools, permissionMode) but placeholder system prompts. Later phases fill in the domain-specific prompts.

### JSON State Contracts
- **D-05:** Schemas defined as JSON Schema files in pipeline/schemas/. A bash+jq validation script checks handoff files against schemas before the next agent reads them. No Node/Python dependency for validation.
- **D-06:** On validation failure: hard fail with error message showing which field failed and why. Pipeline stops. No automatic retries.
- **D-07:** One JSON file per stage with common envelope: `{pipeline_run_id, timestamp, stage, status, data: {...}}`. The `data` field is stage-specific.
- **D-08:** Simple version field in schemas (schema_version: "1.0"). Bump on breaking changes. No automated migration — fail loudly on mismatch.

### Pipeline Orchestration
- **D-09:** Orchestrator agent (via --agent flag) spawns subagents using the Agent tool. This is the "agentic" approach — the orchestrator manages the pipeline flow, not a bash script.
- **D-10:** Human approval gate: orchestrator writes scanner findings to a review file, pipeline pauses. User reviews/edits, then re-runs the pipeline pointing at the approved file.
- **D-11:** Fail fast on agent errors: if an agent exits with non-zero or produces invalid output, log the error and stop. No automatic retries.
- **D-12:** Batch processing: all approved findings go through each stage together (all to researcher, then all to reviewer, then all to categorizer) rather than one-at-a-time through the full pipeline.

### Directory Structure
- **D-13:** Pipeline run artifacts in timestamped directories: pipeline/runs/2026-04-06T14-30-00/ with all stage outputs for that run.
- **D-14:** Final reports in top-level reports/ with topic subdirectories: reports/privacy/, reports/cybersecurity/, reports/ai-law/. Subcategories created by categorizer as topics emerge.
- **D-15:** Email digest input files go in input/ at repo root. Scanner reads from this directory.
- **D-16:** JSON schema files live in pipeline/schemas/ alongside pipeline infrastructure code.

### Claude's Discretion
- Exact JSON schema field names and types for each stage's `data` payload
- Validation script implementation details (jq patterns, error formatting)
- Agent stub system prompt placeholder content
- Pipeline run ID format (UUID, timestamp, sequential)

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

No external specs — requirements fully captured in decisions above. Key project docs:

### Project context
- `.planning/PROJECT.md` — Project vision, constraints (CLI-only, local filesystem, no API keys)
- `.planning/REQUIREMENTS.md` — PIPE-05 (subprocess agents via `claude -p --agent`), PIPE-06 (JSON state files with schema validation)
- `CLAUDE.md` — Technology stack recommendations, CLI invocation patterns, subagent definition examples, model assignments per role

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- None — greenfield project, only CLAUDE.md exists in repo

### Established Patterns
- Claude Code subagent pattern: `.claude/agents/*.md` files with frontmatter (model, tools, maxTurns, permissionMode)
- CLI invocation: `claude -p --agent <name> --output-format json`
- Documented in CLAUDE.md with examples

### Integration Points
- `.claude/agents/` directory for agent definitions (Claude Code convention)
- `pipeline/` directory for orchestration infrastructure (new)
- `reports/` directory for output (new)
- `input/` directory for email digest files (new)

</code_context>

<specifics>
## Specific Ideas

No specific requirements — open to standard approaches

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope

</deferred>

---

*Phase: 01-agent-framework*
*Context gathered: 2026-04-06*
