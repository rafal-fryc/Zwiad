# Phase 5: Pipeline Integration - Context

**Gathered:** 2026-04-07
**Status:** Ready for planning

<domain>
## Phase Boundary

Finalized reports are automatically filed into the correct topic folders with emergent subcategories, every pipeline run produces a complete audit log, and the pipeline can be triggered on a schedule. This phase delivers: categorizer agent logic, audit trail logging, scheduled execution support, orchestrator system prompt, and the Python pipeline entry point that ties everything together.

</domain>

<decisions>
## Implementation Decisions

### Subcategory Strategy
- **D-01:** Seed list + emergent approach — start with predefined subcategories per topic, but allow the categorizer to propose new ones when content doesn't fit existing categories.
- **D-02:** Subcategory registry lives in a JSON config file in `pipeline/config/` (e.g., `categories.json`). Lists known subcategories per topic. Categorizer reads it and can propose additions. Human-editable, version-controlled.
- **D-03:** New subcategory creation requires human confirmation — categorizer proposes the new subcategory and files the report in a `/pending/` folder. User confirms before the subcategory is added to the registry and the report is moved to its final location.
- **D-04:** Multi-topic reports use symlinks — report is filed in the primary topic folder, with symlinks created in secondary topic folders. Discoverable from multiple paths without content duplication.

### Audit Trail Design
- **D-05:** Audit trail is a human-readable markdown file per pipeline run, written to the run's timestamped directory (e.g., `pipeline/runs/2026-04-07T06-00-00/audit-log.md`).
- **D-06:** Detail level is stage summaries — per-stage section recording: what ran, items processed, outcomes (pass/fail/escalate), duration. Lists finding titles but not full content. Compact and scannable.
- **D-07:** Per-run logs only, no cumulative index. To see run history, list the `pipeline/runs/` directory.

### Scheduling & Automation
- **D-08:** Scheduled runs pause at the human approval gate — scanner completes, writes the review file, then pipeline stops. Desktop notification (notify-send) alerts that findings await approval.
- **D-09:** Desktop notification via `notify-send` for both approval-pending and pipeline-failure events. Works on the Tegra system's desktop environment.
- **D-10:** Resume after approval via manual command — user runs a resume script (e.g., `python run_pipeline.py resume <run-id>`) that picks up from the approved state and runs researcher → reviewer → categorizer.
- **D-11:** On pipeline failure: log error details to audit log, send desktop notification, no automatic retry. Consistent with Phase 1's fail-fast approach (D-11). Next scheduled run proceeds normally.

### Orchestrator End-to-End Flow
- **D-12:** Pipeline entry point is a Python script (`run_pipeline.py`), not bash. Invokes `claude -p --agent orchestrator` via subprocess. Handles: run directory setup, resume logic, cron integration, notifications, audit log finalization.
- **D-13:** Existing bash utility scripts (`validate-handoff.sh`, `approve-findings.sh`, etc.) remain as-is. Only the main pipeline entry point and orchestration glue moves to Python.
- **D-14:** Orchestrator agent manages the full pipeline flow internally — spawns scanner, researcher, reviewer, categorizer as subagents via Agent tool. Matches Phase 1 design (D-09). Python script handles pre/post concerns (run directory setup, audit log, notifications).
- **D-15:** Two input modes supported: (1) email digest file — `python run_pipeline.py run --input path/to/digest.html`, (2) web-only scan — `python run_pipeline.py run --web-only` which skips email parsing and only searches government/law firm sites.

### Claude's Discretion
- Seed subcategory list contents (initial subcategories per topic)
- Audit log markdown template layout and exact sections
- Orchestrator system prompt structure and subagent coordination logic
- Python script argument parsing library (argparse vs click)
- Notification message content and formatting
- How the categorizer determines primary vs secondary topics
- Pipeline run ID generation format

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project context
- `.planning/PROJECT.md` — Project vision, constraints (CLI-only, local filesystem, no API keys), emergent subcategory strategy
- `.planning/REQUIREMENTS.md` — PIPE-01 (categorized filing), PIPE-02 (audit trail), PIPE-04 (scheduled execution)
- `CLAUDE.md` — Technology stack, CLI invocation patterns, model assignments, scheduling recommendations (system cron + `claude -p`), token cost considerations

### Phase 1 infrastructure
- `.planning/phases/01-agent-framework/01-CONTEXT.md` — Agent definitions (D-04), JSON state contracts (D-05-D-08), orchestrator pattern (D-09), batch processing (D-12), directory structure (D-13-D-16)
- `.claude/agents/orchestrator.md` — Orchestrator agent stub (sonnet, Agent+Read+Write+Bash+Glob+Grep tools). Needs full system prompt.
- `.claude/agents/categorizer.md` — Categorizer agent stub (sonnet, Read+Write+Glob tools). Needs full system prompt.
- `pipeline/schemas/categorizer.schema.json` — Categorizer output schema (filed_reports with finding_id, source_path, destination_path, topic enum, subcategory)
- `pipeline/schemas/envelope.schema.json` — Pipeline handoff envelope (schema_version, pipeline_run_id, timestamp, stage enum, status enum, data)
- `pipeline/scripts/validate-handoff.sh` — jq-based schema validation

### Phase 2 scanner (approval gate pattern)
- `.planning/phases/02-scanner/02-CONTEXT.md` — Human approval flow (D-12, D-14): markdown review file + APPROVED marker pattern
- `pipeline/scripts/approve-findings.sh` — Approval script to reuse/reference for resume flow
- `pipeline/scripts/generate-review.sh` — Review markdown generation
- `pipeline/scripts/run-scanner.sh` — Scanner orchestration script

### Phase 3 researcher
- `.planning/phases/03-report-generation/03-CONTEXT.md` — Report format decisions, confidence tagging, source citations
- `pipeline/scripts/run-researcher.sh` — Researcher orchestration script

### Phase 4 reviewer
- `.planning/phases/04-verification/04-CONTEXT.md` — Verification methodology, iteration protocol, escalation flow
- `pipeline/scripts/run-reviewer.sh` — Reviewer orchestration script
- `pipeline/scripts/approve-escalation.sh` — Escalation approval script
- `pipeline/scripts/generate-escalation.sh` — Escalation file generation

### Existing pipeline config
- `pipeline/config/sources.json` — Source configuration (pattern for categories.json)

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `.claude/agents/categorizer.md` — Agent stub with correct frontmatter (sonnet, Read+Write+Glob). Needs full system prompt with categorization logic.
- `.claude/agents/orchestrator.md` — Agent stub with correct frontmatter (sonnet, Agent+Read+Write+Bash+Glob+Grep). Needs full system prompt with pipeline flow logic.
- `pipeline/schemas/categorizer.schema.json` — Output schema already defines filed_reports with topic enum and subcategory field. May need extension for pending/symlink status.
- `pipeline/scripts/validate-handoff.sh` — Schema validation reusable for categorizer output.
- `pipeline/scripts/approve-findings.sh` — APPROVED marker pattern reusable for subcategory confirmation flow.
- `pipeline/config/sources.json` — Config file pattern reusable for categories.json registry.

### Established Patterns
- Agent definitions in `.claude/agents/*.md` with frontmatter (model, tools, permissionMode)
- JSON state files with common envelope wrapping stage-specific data
- Timestamped pipeline run directories: `pipeline/runs/YYYY-MM-DDTHH-MM-SS/`
- Bash orchestration scripts invoking `claude -p --agent`
- Human approval via markdown file + `## APPROVED` marker
- jq-based JSON schema validation via `validate-handoff.sh`

### Integration Points
- Input: `reviewer-output.json` from Phase 4 (verified reports with status)
- Input: Markdown reports in `reports/{category}/` directories (categorizer reads these)
- Output: Reports moved/symlinked to `reports/{topic}/{subcategory}/` directories
- Output: `categorizer-output.json` with filing decisions (filed_reports array)
- Output: `audit-log.md` per pipeline run directory
- Entry: `run_pipeline.py` Python script as single pipeline entry point
- Scheduling: System cron calls `run_pipeline.py` for daily execution

</code_context>

<specifics>
## Specific Ideas

- User prefers Python over bash for the main pipeline script — use Python subprocess to call `claude -p --agent orchestrator`
- Desktop notification via `notify-send` — user wants immediate visibility on the Tegra system for both approval-pending and failure events
- Subcategory confirmation flow should follow the same pattern as scanner approval (markdown file + APPROVED marker) for consistency
- Web-only mode enables scanning without an email digest — useful for days when no digest arrives or for ad-hoc checks

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope

</deferred>

---

*Phase: 05-pipeline-integration*
*Context gathered: 2026-04-07*
