# Phase 01: Agent Framework - Research

**Researched:** 2026-04-06
**Domain:** Claude Code subagent definitions, JSON state validation, pipeline orchestration
**Confidence:** HIGH

## Summary

Phase 1 builds the subprocess agent infrastructure: five agent definition files in `.claude/agents/`, a JSON state contract with envelope validation, a bash+jq validation script, and the directory structure for pipeline runs, reports, and input. The core technology is Claude Code's native subagent system (`.claude/agents/*.md` with YAML frontmatter), which is well-documented and verified working on this system (Claude Code v2.1.92).

The main technical challenge is JSON Schema validation using only bash+jq (per decision D-05). jq does NOT support JSON Schema natively -- it validates JSON syntax and can check structural properties (field existence, types) via jq expressions. This is sufficient for envelope validation but means schemas will be expressed as both JSON Schema files (documentation/contract) and parallel jq validation expressions (runtime enforcement). This is a deliberate tradeoff to avoid Node/Python dependencies.

**Primary recommendation:** Define agent stubs with real frontmatter (model, tools, permissionMode) and placeholder prompts. Build the validation layer as a single `validate-handoff.sh` script that takes a schema name and JSON file path, using jq expressions derived from the JSON Schema files.

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions
- **D-01:** Model assignment: opus for researcher/reviewer, sonnet for scanner/categorizer/orchestrator
- **D-02:** Per-agent tool allowlists in frontmatter. Scanner: WebSearch+WebFetch+Read+Write. Researcher: WebSearch+WebFetch+Read+Write. Reviewer: Read+WebFetch only. Categorizer: Read+Write+Glob only.
- **D-03:** No budget caps or turn limits initially
- **D-04:** Phase 1 creates all 5 agent stubs with real frontmatter but placeholder prompts
- **D-05:** Schemas as JSON Schema files in pipeline/schemas/. Bash+jq validation script. No Node/Python dependency.
- **D-06:** Hard fail on validation failure with error message. Pipeline stops. No retries.
- **D-07:** One JSON file per stage with common envelope: `{pipeline_run_id, timestamp, stage, status, data: {...}}`
- **D-08:** Simple schema_version field. Fail on mismatch.
- **D-09:** Orchestrator agent spawns subagents via Agent tool (not bash script orchestration)
- **D-10:** Human approval gate: orchestrator writes scanner findings to review file, pipeline pauses
- **D-11:** Fail fast on agent errors. No retries.
- **D-12:** Batch processing: all findings through each stage together
- **D-13:** Pipeline runs in timestamped directories: pipeline/runs/YYYY-MM-DDTHH-MM-SS/
- **D-14:** Reports in reports/privacy/, reports/cybersecurity/, reports/ai-law/
- **D-15:** Email input in input/ at repo root
- **D-16:** JSON schemas in pipeline/schemas/

### Claude's Discretion
- Exact JSON schema field names and types for each stage's data payload
- Validation script implementation details (jq patterns, error formatting)
- Agent stub system prompt placeholder content
- Pipeline run ID format (UUID, timestamp, sequential)

### Deferred Ideas (OUT OF SCOPE)
None
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| PIPE-05 | Each agent runs as a separate Claude Code subprocess via `claude -p --agent` | Verified: `claude -p --agent <name> --output-format json` works. Agent definitions in `.claude/agents/*.md`. Frontmatter supports model, tools, permissionMode, maxTurns. |
| PIPE-06 | Agents communicate via JSON state files with schema validation at each handoff | Validated: jq structural validation works (field existence + type checks). JSON Schema files serve as contracts; jq expressions enforce at runtime. |
</phase_requirements>

## Project Constraints (from CLAUDE.md)

- **Runtime**: Claude Code CLI only -- no Anthropic API keys, no Agent SDK
- **Storage**: Local filesystem only -- markdown files in structured directories
- **Execution**: Manual trigger for v1
- **Review cap**: Max 3 iteration rounds between researcher and reviewer
- **Sources**: Web-accessible only
- No npm install, no pip install -- pure Claude Code CLI project
- Agent definitions in `.claude/agents/*.md` (Claude Code convention)
- Pipeline state as JSON in `pipeline/state/` (per CLAUDE.md; decisions refined to `pipeline/runs/`)

## Standard Stack

### Core
| Component | Version | Purpose | Why Standard |
|-----------|---------|---------|--------------|
| Claude Code CLI | 2.1.92 (installed) | Agent runtime, subprocess invocation | Project constraint. `--agent` flag for main agent, Agent tool for subagent spawning. [VERIFIED: `claude --version` returns 2.1.92] |
| Claude Code Subagents | Built-in (v2.1.63+) | Agent definition format | `.claude/agents/*.md` with YAML frontmatter. Native feature, no setup needed. [VERIFIED: official docs at code.claude.com/docs/en/sub-agents] |
| jq | 1.6 (installed) | JSON validation and processing | Structural validation of handoff files. No external dependencies. [VERIFIED: `jq --version` returns jq-1.6] |
| bash | System default | Pipeline scripts, validation glue | Entry point, orchestration glue. [VERIFIED: available] |

### Supporting
| Component | Version | Purpose | When to Use |
|-----------|---------|---------|-------------|
| Fetch MCP Server | Latest via uvx | Enhanced URL fetching | When built-in WebFetch hits limitations on large government docs |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| jq structural validation | Python jsonschema | Full JSON Schema support but adds Python dependency (violates D-05) |
| jq structural validation | ajv-cli (Node) | Full JSON Schema support but adds Node dependency (violates D-05) |
| Subagent orchestration | Bash script calling `claude -p` in sequence | Works but loses Agent tool's native context management. Decision D-09 chose subagent approach. |

## Architecture Patterns

### Recommended Project Structure
```
.claude/
  agents/
    orchestrator.md       # Main agent (--agent orchestrator)
    scanner.md            # Subagent: scan sources
    researcher.md         # Subagent: deep research + report
    reviewer.md           # Subagent: fact-check reports
    categorizer.md        # Subagent: file reports by topic
pipeline/
  schemas/
    envelope.schema.json  # Common envelope schema
    scanner.schema.json   # Scanner output data schema
    researcher.schema.json
    reviewer.schema.json
    categorizer.schema.json
  scripts/
    validate-handoff.sh   # Bash+jq validation script
  runs/
    2026-04-06T14-30-00/  # Per-run state directory
      scanner-output.json
      human-approved.json
      researcher-output.json
      reviewer-output.json
      categorizer-output.json
reports/
  privacy/
  cybersecurity/
  ai-law/
input/
  digest-2026-04-06.txt   # Email digest files
```

### Pattern 1: Subagent Definition with Frontmatter
**What:** Each agent is a `.claude/agents/*.md` file with YAML frontmatter controlling model, tools, and permissions
**When to use:** Always -- this is the native Claude Code pattern
**Example:**
```yaml
# Source: https://code.claude.com/docs/en/sub-agents
---
name: scanner
description: Scans regulatory sources and email digests for new developments. Use when the orchestrator needs to identify new regulatory items.
tools: WebSearch, WebFetch, Read, Write
model: sonnet
---

[Placeholder: Scanner system prompt will be defined in Phase 2]
```
[VERIFIED: official docs at code.claude.com/docs/en/sub-agents]

### Pattern 2: Orchestrator Agent with Agent Tool Restrictions
**What:** The orchestrator agent uses `tools: Agent(scanner, researcher, reviewer, categorizer), Read, Write, Bash, Glob` to restrict which subagents it can spawn
**When to use:** For the main orchestrator that coordinates the pipeline
**Example:**
```yaml
# Source: https://code.claude.com/docs/en/sub-agents
---
name: orchestrator
description: Coordinates the regulatory monitoring pipeline. Spawns scanner, researcher, reviewer, and categorizer subagents.
tools: Agent(scanner, researcher, reviewer, categorizer), Read, Write, Bash, Glob, Grep
model: sonnet
---

[Placeholder: Orchestrator system prompt will be defined in Phase 5]
```
[VERIFIED: `Agent(agent_type)` syntax confirmed in official docs -- restricts which subagents can be spawned]

### Pattern 3: JSON Envelope Contract
**What:** Every inter-agent JSON file follows a common envelope structure
**When to use:** All pipeline handoff files
**Example:**
```json
{
  "schema_version": "1.0",
  "pipeline_run_id": "2026-04-06T14-30-00",
  "timestamp": "2026-04-06T14:30:00Z",
  "stage": "scanner",
  "status": "complete",
  "data": {
    "findings": []
  }
}
```
[ASSUMED -- field names are Claude's discretion per CONTEXT.md]

### Pattern 4: jq Structural Validation
**What:** A bash script that validates JSON files against expected structure using jq expressions
**When to use:** Before each agent reads a handoff file from the previous stage
**Example:**
```bash
#!/bin/bash
# validate-handoff.sh <schema-name> <json-file>
# Source: jq structural validation pattern [VERIFIED: jq -e works for boolean assertions]

SCHEMA="$1"
FILE="$2"

# Validate JSON syntax
if ! jq empty "$FILE" 2>/dev/null; then
  echo "ERROR: Invalid JSON in $FILE" >&2
  exit 1
fi

# Validate envelope fields
if ! jq -e '
  (.schema_version | type == "string") and
  (.pipeline_run_id | type == "string") and
  (.timestamp | type == "string") and
  (.stage | type == "string") and
  (.status | type == "string") and
  (.data | type == "object")
' "$FILE" > /dev/null 2>&1; then
  echo "ERROR: Envelope validation failed for $FILE" >&2
  echo "Required fields: schema_version, pipeline_run_id, timestamp, stage, status, data" >&2
  exit 1
fi

# Validate schema version
EXPECTED_VERSION="1.0"
ACTUAL_VERSION=$(jq -r '.schema_version' "$FILE")
if [ "$ACTUAL_VERSION" != "$EXPECTED_VERSION" ]; then
  echo "ERROR: Schema version mismatch in $FILE: expected $EXPECTED_VERSION, got $ACTUAL_VERSION" >&2
  exit 1
fi

# Stage-specific validation (load from schema-specific jq expression file)
STAGE_VALIDATOR="pipeline/schemas/${SCHEMA}.jq"
if [ -f "$STAGE_VALIDATOR" ]; then
  if ! jq -e -f "$STAGE_VALIDATOR" "$FILE" > /dev/null 2>&1; then
    echo "ERROR: Stage-specific validation failed for $FILE against $SCHEMA" >&2
    exit 1
  fi
fi

echo "OK: $FILE validates against $SCHEMA"
exit 0
```
[VERIFIED: jq -e exits with code 1 on false, jq -f loads expressions from file]

### Anti-Patterns to Avoid
- **Using Agent Teams instead of subagents:** Agent Teams are for parallel inter-agent discussion. This pipeline is sequential with file handoffs -- subagents are the correct pattern. [VERIFIED: official docs distinguish these clearly]
- **Spawning subagents from subagents:** Subagents cannot spawn other subagents. Only the main thread agent (orchestrator via `--agent`) can use the Agent tool to spawn subagents. [VERIFIED: official docs state this explicitly]
- **Omitting `tools` field to inherit all tools:** Each agent should have explicit tool restrictions per D-02. Omitting `tools` gives the subagent ALL tools from the parent. [VERIFIED: official docs confirm inheritance behavior]
- **Using `--agent` with a nonexistent agent name:** Claude Code does NOT error on a missing agent name -- it silently runs without the agent definition. Always verify agent files exist. [VERIFIED: tested locally, `--agent nonexistent` returned success]

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Agent subprocess invocation | Custom process management | `claude -p --agent <name> --output-format json` | Native CLI handles context windows, model selection, tool restrictions |
| Agent definition format | Custom config files | `.claude/agents/*.md` with YAML frontmatter | Native Claude Code convention, auto-discovered, version-controllable |
| Subagent spawning from orchestrator | Bash script calling `claude -p` in loop | Agent tool (native to Claude Code) | Orchestrator agent natively has Agent tool access; handles context passing |
| JSON syntax validation | Custom parser | `jq empty` | jq handles all edge cases, installed on system |
| Pipeline run IDs | UUID generator | Timestamp-based ID (e.g., `2026-04-06T14-30-00`) | Human-readable, naturally sortable, no external dependency |

## Common Pitfalls

### Pitfall 1: Silent Agent Missing
**What goes wrong:** `claude -p --agent scanner` runs successfully even if `.claude/agents/scanner.md` doesn't exist. The agent runs without the custom system prompt, tools, or model.
**Why it happens:** Claude Code treats `--agent` as a hint, not a hard requirement. If the agent file is not found, it falls back to default behavior.
**How to avoid:** Add a pre-flight check in scripts: verify the agent file exists before invoking `claude -p --agent`.
**Warning signs:** Agent behaves generically, uses wrong model, has tools it shouldn't have.
[VERIFIED: tested locally -- `--agent nonexistent` returned success with no error]

### Pitfall 2: jq Does Not Do JSON Schema Validation
**What goes wrong:** Assuming `jq` can validate against a JSON Schema file. It cannot. jq validates JSON syntax and can check structural properties, but has no built-in JSON Schema support.
**Why it happens:** Conflating "JSON validation" with "JSON Schema validation."
**How to avoid:** Write JSON Schema files as contracts/documentation, and write parallel jq expressions for runtime validation. Keep them in sync manually.
**Warning signs:** Schemas exist but are never actually enforced at runtime.
[VERIFIED: jq 1.6 has no schema validation command]

### Pitfall 3: Subagent Context is Isolated
**What goes wrong:** Expecting subagents to see the parent's conversation history or CLAUDE.md context.
**Why it happens:** Subagents get only their own system prompt plus basic environment details (working directory). They do NOT receive the parent's conversation context or the full Claude Code system prompt.
**How to avoid:** Pass all needed context via the Agent tool prompt or via files. Subagents CAN read CLAUDE.md from the working directory if they have the Read tool.
**Warning signs:** Subagent doesn't know about project structure or conventions.
[VERIFIED: official docs state "Subagents receive only this system prompt (plus basic environment details like working directory), not the full Claude Code system prompt."]

### Pitfall 4: Timestamp Directory Names on Windows/Linux Portability
**What goes wrong:** Using colons in directory names (e.g., `2026-04-06T14:30:00`) fails on some filesystems.
**Why it happens:** ISO 8601 timestamps contain colons.
**How to avoid:** Replace colons with hyphens: `2026-04-06T14-30-00`. Decision D-13 already specifies this format.
**Warning signs:** Directory creation fails silently.
[ASSUMED -- standard filesystem best practice]

### Pitfall 5: Agent Tool Output Truncation
**What goes wrong:** When a subagent produces very long output, only the final message is returned to the parent agent. Intermediate reasoning is lost.
**Why it happens:** Subagents return only their final response to the parent.
**How to avoid:** Have agents write their full output to JSON files, and return only a summary/status to the parent. This is already the plan (file-based handoffs).
**Warning signs:** Orchestrator sees truncated results from subagents.
[VERIFIED: official docs state subagents return final message to parent]

## Code Examples

### Agent Definition: Orchestrator (main agent)
```yaml
# .claude/agents/orchestrator.md
# Source: https://code.claude.com/docs/en/sub-agents [VERIFIED]
---
name: orchestrator
description: Coordinates the Zwiad regulatory monitoring pipeline. Spawns scanner, researcher, reviewer, and categorizer subagents in sequence.
tools: Agent(scanner, researcher, reviewer, categorizer), Read, Write, Bash, Glob, Grep
model: sonnet
---

You are the Zwiad pipeline orchestrator. Your job is to coordinate the regulatory monitoring pipeline by spawning subagents in sequence and managing file-based handoffs between them.

[Placeholder: Full orchestration logic will be defined in Phase 5]
```

### Agent Definition: Scanner (subagent stub)
```yaml
# .claude/agents/scanner.md
# Source: https://code.claude.com/docs/en/sub-agents [VERIFIED]
---
name: scanner
description: Scans regulatory sources and email digests for new privacy, cybersecurity, and AI law developments. Use when the pipeline needs to identify new items.
tools: WebSearch, WebFetch, Read, Write
model: sonnet
---

You are the Zwiad scanner agent. Your job is to identify new regulatory developments from provided sources.

[Placeholder: Full scanning logic will be defined in Phase 2]
```

### Agent Definition: Reviewer (restricted tools)
```yaml
# .claude/agents/reviewer.md
---
name: reviewer
description: Independently fact-checks research reports by verifying claims against cited sources. Use after researcher produces a report.
tools: Read, WebFetch
model: opus
---

You are the Zwiad reviewer agent. Your job is to verify factual claims in research reports.

[Placeholder: Full review logic will be defined in Phase 4]
```

### CLI Invocation Pattern
```bash
# Launch the orchestrator as main agent [VERIFIED: --agent flag works]
claude -p --agent orchestrator \
  --output-format json \
  "Run the pipeline for input/digest-2026-04-06.txt"

# Parse result from JSON output [VERIFIED: jq .result extraction works]
RESULT=$(claude -p --agent orchestrator --output-format json "..." | jq -r '.result')
```

### JSON Envelope Schema
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Pipeline Handoff Envelope",
  "description": "Common envelope for all inter-agent JSON state files",
  "type": "object",
  "required": ["schema_version", "pipeline_run_id", "timestamp", "stage", "status", "data"],
  "properties": {
    "schema_version": {
      "type": "string",
      "const": "1.0"
    },
    "pipeline_run_id": {
      "type": "string",
      "description": "Timestamp-based run identifier, e.g. 2026-04-06T14-30-00"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "ISO 8601 timestamp of when this file was written"
    },
    "stage": {
      "type": "string",
      "enum": ["scanner", "human-review", "researcher", "reviewer", "categorizer"]
    },
    "status": {
      "type": "string",
      "enum": ["complete", "error", "pending-review"]
    },
    "data": {
      "type": "object",
      "description": "Stage-specific payload, validated by per-stage schema"
    }
  },
  "additionalProperties": false
}
```
[ASSUMED -- field names/values are Claude's discretion per CONTEXT.md]

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| `Task` tool name | `Agent` tool name | Claude Code v2.1.63 | `Task(...)` still works as alias but `Agent(...)` is canonical [VERIFIED: official docs note] |
| Bash script orchestration | Subagent definitions + Agent tool | v2.1.63 | Native context management, tool restrictions, model selection per agent |
| `/loop` for scheduling | System cron + `claude -p` | v2.1.72+ | `/loop` expires after 7 days; cron is durable (v2 concern, not Phase 1) |

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | Pipeline run ID format as timestamp (e.g., `2026-04-06T14-30-00`) | Architecture Patterns | Low -- easily changed, format is Claude's discretion |
| A2 | JSON envelope field names (schema_version, pipeline_run_id, timestamp, stage, status, data) | Code Examples | Low -- field names are Claude's discretion, easily adjusted |
| A3 | Stage enum values: scanner, human-review, researcher, reviewer, categorizer | Code Examples | Low -- can be adjusted during implementation |
| A4 | Status enum values: complete, error, pending-review | Code Examples | Low -- can be adjusted during implementation |
| A5 | Using `.jq` files for per-stage validation expressions | Architecture Patterns | Medium -- alternative is inline jq in the validation script. `.jq` files are more maintainable. |

## Open Questions

1. **Orchestrator's permissionMode**
   - What we know: The orchestrator needs to spawn subagents and write files. `auto` or `acceptEdits` would reduce prompts.
   - What's unclear: Whether `bypassPermissions` is appropriate for the orchestrator in `-p` (print) mode.
   - Recommendation: Use no explicit permissionMode for now (inherits from session). The `--dangerously-skip-permissions` flag on the CLI invocation handles this for `-p` mode.

2. **Reviewer tool list completeness**
   - What we know: D-02 says Reviewer gets Read+WebFetch only.
   - What's unclear: Reviewer may need Grep/Glob to search the codebase for existing reports (for REPT-04 cross-referencing).
   - Recommendation: Stick with D-02 for Phase 1 stubs. Expand in Phase 4 if needed.

3. **How subagents discover project context**
   - What we know: Subagents don't receive parent's system prompt. They DO read CLAUDE.md if they have Read tool access.
   - What's unclear: Whether subagents automatically discover and read CLAUDE.md or need explicit instruction.
   - Recommendation: Include "Read CLAUDE.md for project context" in each agent's system prompt placeholder.

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| Claude Code CLI | All agent invocations | Yes | 2.1.92 | -- |
| jq | JSON validation script | Yes | 1.6 | -- |
| bash | Pipeline scripts | Yes | System default | -- |
| Python 3 | Not required (D-05) | Yes (3.10.12) | 3.10.12 | N/A |
| Node.js | Not required (D-05) | Yes (v24.14.1) | v24.14.1 | N/A |

**Missing dependencies with no fallback:** None

**Missing dependencies with fallback:** None

All required dependencies are available. Python and Node are present but intentionally not used for validation (per D-05).

## Validation Architecture

### Test Framework
| Property | Value |
|----------|-------|
| Framework | bash + manual verification |
| Config file | none -- bash scripts are self-contained |
| Quick run command | `bash pipeline/scripts/validate-handoff.sh envelope pipeline/runs/test/scanner-output.json` |
| Full suite command | `bash pipeline/scripts/test-validation.sh` (to be created in Wave 0) |

### Phase Requirements to Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| PIPE-05 | Agent can be launched via `claude -p --agent` and exits cleanly | smoke | `claude -p --agent scanner --output-format json "Echo test" && echo PASS` | No -- Wave 0 |
| PIPE-06a | Valid JSON handoff passes validation | unit | `bash pipeline/scripts/validate-handoff.sh envelope test-fixtures/valid-envelope.json` | No -- Wave 0 |
| PIPE-06b | Malformed JSON is caught and reported | unit | `bash pipeline/scripts/validate-handoff.sh envelope test-fixtures/invalid-json.txt` | No -- Wave 0 |
| PIPE-06c | Schema-violating JSON is caught (missing required field) | unit | `bash pipeline/scripts/validate-handoff.sh envelope test-fixtures/missing-field.json` | No -- Wave 0 |
| PIPE-06d | Schema version mismatch is caught | unit | `bash pipeline/scripts/validate-handoff.sh envelope test-fixtures/wrong-version.json` | No -- Wave 0 |

### Sampling Rate
- **Per task commit:** Quick run command on modified validation scripts
- **Per wave merge:** Full test suite
- **Phase gate:** All validation tests pass + successful agent smoke test

### Wave 0 Gaps
- [ ] `pipeline/scripts/test-validation.sh` -- test runner for all validation scenarios
- [ ] `pipeline/scripts/test-fixtures/` -- directory with valid and invalid JSON test files
- [ ] Smoke test script for PIPE-05 agent invocation

## Security Domain

### Applicable ASVS Categories

| ASVS Category | Applies | Standard Control |
|---------------|---------|-----------------|
| V2 Authentication | No | N/A -- local CLI tool, no auth |
| V3 Session Management | No | N/A -- stateless CLI invocations |
| V4 Access Control | Yes (minimal) | Tool allowlists in agent frontmatter (D-02) |
| V5 Input Validation | Yes | jq structural validation of JSON handoffs (D-05) |
| V6 Cryptography | No | N/A -- no encryption in this phase |

### Known Threat Patterns

| Pattern | STRIDE | Standard Mitigation |
|---------|--------|---------------------|
| Malformed JSON injection between agents | Tampering | Structural validation with jq before each handoff (D-05, D-06) |
| Agent using unauthorized tools | Elevation of Privilege | Explicit tool allowlists in frontmatter (D-02) |
| Schema version mismatch causing silent data loss | Information Disclosure | Hard fail on version mismatch (D-08) |

## Sources

### Primary (HIGH confidence)
- [Claude Code CLI](https://code.claude.com/docs/en/sub-agents) -- Subagent definition format, frontmatter fields, Agent tool syntax, tool restrictions, permission modes. Fetched and verified 2026-04-06.
- Local system verification -- `claude --version` (2.1.92), `jq --version` (1.6), `--agent` flag behavior tested locally.

### Secondary (MEDIUM confidence)
- [Claude Code CLI Reference](https://code.claude.com/docs/en/cli-reference) -- Referenced in CLAUDE.md, verified flags via `claude --help`.

### Tertiary (LOW confidence)
- None -- all critical claims verified against official docs or local testing.

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH -- all tools verified locally, official docs confirm patterns
- Architecture: HIGH -- subagent definitions are well-documented native feature
- Pitfalls: HIGH -- key pitfalls verified through testing (silent agent missing) and official docs (subagent isolation)
- Validation: MEDIUM -- jq structural validation approach is sound but per-stage validation expressions need implementation

**Research date:** 2026-04-06
**Valid until:** 2026-05-06 (stable -- Claude Code subagent API is established)
