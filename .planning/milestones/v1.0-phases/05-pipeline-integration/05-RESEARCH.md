# Phase 5: Pipeline Integration - Research

**Researched:** 2026-04-07
**Domain:** Pipeline orchestration, report categorization, audit logging, cron scheduling
**Confidence:** HIGH

## Summary

Phase 5 integrates all four prior pipeline stages (scanner, researcher, reviewer, categorizer) into a single end-to-end pipeline with a Python entry point, adds the categorizer agent logic for filing reports with emergent subcategories, produces audit trail logs per run, and enables cron-based scheduled execution. The codebase already has fully implemented agent definitions (scanner, researcher, reviewer) and bash orchestration scripts for each stage, plus stub agent definitions for orchestrator and categorizer that need full system prompts.

The primary technical work is: (1) writing the categorizer agent system prompt with subcategory registry logic, (2) writing the orchestrator agent system prompt that coordinates all subagents, (3) building the Python `run_pipeline.py` entry point with run/resume/cron modes, (4) creating the audit log generation, and (5) setting up cron scheduling with desktop notifications. All components use existing patterns -- JSON envelope handoffs, `validate-handoff.sh` validation, `claude -p --agent` invocation, and markdown-based human approval gates.

**Primary recommendation:** Follow established codebase patterns exactly. The categorizer agent and orchestrator agent are the two creative deliverables; everything else is glue code assembling existing pieces.

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions
- **D-01:** Seed list + emergent approach -- start with predefined subcategories per topic, but allow the categorizer to propose new ones when content doesn't fit existing categories.
- **D-02:** Subcategory registry lives in a JSON config file in `pipeline/config/` (e.g., `categories.json`). Lists known subcategories per topic. Categorizer reads it and can propose additions. Human-editable, version-controlled.
- **D-03:** New subcategory creation requires human confirmation -- categorizer proposes the new subcategory and files the report in a `/pending/` folder. User confirms before the subcategory is added to the registry and the report is moved to its final location.
- **D-04:** Multi-topic reports use symlinks -- report is filed in the primary topic folder, with symlinks created in secondary topic folders. Discoverable from multiple paths without content duplication.
- **D-05:** Audit trail is a human-readable markdown file per pipeline run, written to the run's timestamped directory (e.g., `pipeline/runs/2026-04-07T06-00-00/audit-log.md`).
- **D-06:** Detail level is stage summaries -- per-stage section recording: what ran, items processed, outcomes (pass/fail/escalate), duration. Lists finding titles but not full content. Compact and scannable.
- **D-07:** Per-run logs only, no cumulative index. To see run history, list the `pipeline/runs/` directory.
- **D-08:** Scheduled runs pause at the human approval gate -- scanner completes, writes the review file, then pipeline stops. Desktop notification (notify-send) alerts that findings await approval.
- **D-09:** Desktop notification via `notify-send` for both approval-pending and pipeline-failure events. Works on the Tegra system's desktop environment.
- **D-10:** Resume after approval via manual command -- user runs a resume script (e.g., `python run_pipeline.py resume <run-id>`) that picks up from the approved state and runs researcher -> reviewer -> categorizer.
- **D-11:** On pipeline failure: log error details to audit log, send desktop notification, no automatic retry. Consistent with Phase 1's fail-fast approach (D-11). Next scheduled run proceeds normally.
- **D-12:** Pipeline entry point is a Python script (`run_pipeline.py`), not bash. Invokes `claude -p --agent orchestrator` via subprocess. Handles: run directory setup, resume logic, cron integration, notifications, audit log finalization.
- **D-13:** Existing bash utility scripts (`validate-handoff.sh`, `approve-findings.sh`, etc.) remain as-is. Only the main pipeline entry point and orchestration glue moves to Python.
- **D-14:** Orchestrator agent manages the full pipeline flow internally -- spawns scanner, researcher, reviewer, categorizer as subagents via Agent tool. Matches Phase 1 design (D-09). Python script handles pre/post concerns (run directory setup, audit log, notifications).
- **D-15:** Two input modes supported: (1) email digest file -- `python run_pipeline.py run --input path/to/digest.html`, (2) web-only scan -- `python run_pipeline.py run --web-only` which skips email parsing and only searches government/law firm sites.

### Claude's Discretion
- Seed subcategory list contents (initial subcategories per topic)
- Audit log markdown template layout and exact sections
- Orchestrator system prompt structure and subagent coordination logic
- Python script argument parsing library (argparse vs click)
- Notification message content and formatting
- How the categorizer determines primary vs secondary topics
- Pipeline run ID generation format

### Deferred Ideas (OUT OF SCOPE)
None -- discussion stayed within phase scope
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| PIPE-01 | Finalized reports filed into topic folders (/privacy, /cybersecurity, /ai-law) with emergent subcategories | Categorizer agent system prompt, categories.json registry, subcategory confirmation flow, symlink pattern for multi-topic reports |
| PIPE-02 | Each pipeline run produces an audit trail log (what was scanned, approved, researched, verified) | Audit log markdown template, Python script audit collection, per-stage summary format |
| PIPE-04 | Pipeline supports scheduled daily execution via cron | Python entry point with run/resume modes, crontab entry, notify-send integration, pause-at-approval-gate pattern |
</phase_requirements>

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| Python 3 stdlib | 3.10.12 | Pipeline entry point script | Already installed on system. argparse, subprocess, json, pathlib, datetime, os, sys all available. No external dependencies needed. [VERIFIED: checked on system] |
| Claude Code CLI | 2.1.92 | Agent runtime | Already installed, exceeds minimum 2.1.63. [VERIFIED: `claude --version`] |
| jq | System | JSON validation, schema checking | Already used by all existing pipeline scripts. [VERIFIED: validate-handoff.sh uses jq] |
| notify-send | 0.7.9 | Desktop notifications | Already installed on Tegra system. [VERIFIED: `notify-send --version`] |
| cron | System | Scheduled execution | Standard Linux scheduler. System has crontab available (currently empty). [VERIFIED: `crontab -l`] |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| argparse | stdlib | CLI argument parsing for run_pipeline.py | Use for the Python entry point. Zero dependencies, built into Python. Sufficient for run/resume subcommands. [ASSUMED] |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| argparse | click | click is nicer API but requires pip install; argparse is stdlib and sufficient for 2 subcommands |
| Python subprocess | Direct bash | D-12 locks Python as entry point; subprocess calls existing bash scripts and claude CLI |
| notify-send | Python dbus bindings | notify-send is simpler, already installed, no additional Python packages needed |

**Installation:**
```bash
# No installation needed -- all stdlib and system tools
# Verify:
python3 --version   # 3.10.12
claude --version     # 2.1.92
jq --version         # system
notify-send --version  # 0.7.9
```

## Architecture Patterns

### Recommended Project Structure
```
run_pipeline.py                          # Python entry point (NEW)
pipeline/
  config/
    sources.json                         # Existing source config
    categories.json                      # NEW: subcategory registry
  scripts/
    run-scanner.sh                       # Existing
    run-researcher.sh                    # Existing
    run-reviewer.sh                      # Existing
    approve-findings.sh                  # Existing
    validate-handoff.sh                  # Existing
    ...                                  # Other existing scripts
  schemas/
    categorizer.schema.json              # Existing (may need extension)
    categorizer.jq                       # Existing
    ...                                  # Other existing schemas
  runs/
    2026-04-07T06-00-00/                 # Timestamped run directory
      scanner-output.json
      scanner-review.md
      scanner-approved.json
      researcher-*.json
      reviewer-output.json
      categorizer-output.json            # NEW
      audit-log.md                       # NEW
  pending/                               # NEW: reports awaiting subcategory confirmation
    {finding-id}-pending.json            # Metadata for pending categorization
reports/
  privacy/
    {subcategory}/                       # Subcategory subdirectories
      {report}.md
  cybersecurity/
    {subcategory}/
      {report}.md
  ai-law/
    {subcategory}/
      {report}.md
.claude/agents/
  orchestrator.md                        # Existing stub -> full system prompt
  categorizer.md                         # Existing stub -> full system prompt
```

### Pattern 1: Two-Layer Orchestration (Python outer + Agent inner)
**What:** Python script handles infrastructure (run directory, notifications, audit log, resume logic). Orchestrator agent handles pipeline flow (spawn subagents, manage handoffs). [VERIFIED: established by D-12 and D-14]
**When to use:** Always -- this is the locked architecture.
**Example:**
```python
# Source: D-12, D-14 from CONTEXT.md
# Python outer layer
def run_pipeline(run_id, input_file=None, web_only=False):
    run_dir = setup_run_directory(run_id)
    try:
        result = subprocess.run(
            ["claude", "-p", "--agent", "orchestrator",
             "--output-format", "json", "--max-turns", "30",
             build_prompt(run_id, input_file, web_only)],
            capture_output=True, text=True
        )
        # Orchestrator handles scanner -> approval gate -> stop
        # Or: researcher -> reviewer -> categorizer (resume mode)
    except Exception as e:
        log_error(run_dir, e)
        notify("Pipeline failure", str(e))
```

### Pattern 2: Subcategory Registry with Pending Flow
**What:** categories.json defines known subcategories. Categorizer reads it, files reports in known subcategories directly, proposes new ones by filing in `/pending/`. [VERIFIED: D-01, D-02, D-03]
**When to use:** Every categorization decision.
**Example:**
```json
// Source: D-02 from CONTEXT.md, modeled on sources.json pattern
// pipeline/config/categories.json
{
  "schema_version": "1.0",
  "topics": {
    "privacy": {
      "subcategories": [
        "state-comprehensive-laws",
        "federal-legislation",
        "enforcement-actions",
        "data-breach",
        "childrens-privacy",
        "health-data"
      ]
    },
    "cybersecurity": {
      "subcategories": [
        "federal-frameworks",
        "incident-reporting",
        "enforcement-actions",
        "critical-infrastructure",
        "standards-guidance"
      ]
    },
    "ai-law": {
      "subcategories": [
        "federal-regulation",
        "state-legislation",
        "executive-orders",
        "enforcement-actions",
        "frameworks-guidance"
      ]
    }
  }
}
```

### Pattern 3: Audit Log as Markdown
**What:** Each pipeline run produces `audit-log.md` in the run directory with per-stage summaries. [VERIFIED: D-05, D-06, D-07]
**When to use:** Every pipeline run (both initial and resume).

### Pattern 4: Resume-from-Approval
**What:** Pipeline run has two modes -- initial (scanner -> pause at approval) and resume (pick up after approval -> researcher -> reviewer -> categorizer). [VERIFIED: D-08, D-10]
**When to use:** Scheduled cron runs trigger initial mode; user triggers resume mode after reviewing scanner output.

### Pattern 5: Symlinks for Multi-Topic Reports
**What:** Report filed in primary topic folder; symlinks created in secondary topic folders. [VERIFIED: D-04, symlinks tested on this system]
**When to use:** When categorizer determines a report is relevant to multiple topics.

### Anti-Patterns to Avoid
- **Running orchestrator for the full pipeline in one shot:** The pipeline MUST pause at the human approval gate (D-08). The orchestrator invocation is split into two phases: scan phase and research phase. The Python script manages this split.
- **Building custom JSON parsing in Python:** Reuse existing `validate-handoff.sh` and `jq` validation. Python script calls these via subprocess, does not duplicate validation logic.
- **Creating subcategory directories without confirmation:** New subcategories go to `/pending/` first (D-03). Never auto-create unregistered subcategory directories.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| JSON schema validation | Python JSON validation | Existing `validate-handoff.sh` + jq | Already handles envelope + stage-specific validation for all stages. Proven pattern. [VERIFIED: codebase] |
| Human approval gate | New approval mechanism | Existing `approve-findings.sh` + `## APPROVED` marker pattern | Scanner approval flow already works. Subcategory confirmation can follow the same pattern. [VERIFIED: codebase] |
| Desktop notifications | Python dbus/gi | `notify-send` CLI via subprocess | Already installed, works on Tegra. One-liner subprocess call. [VERIFIED: system] |
| Run ID generation | Custom format | `date -u +"%Y-%m-%dT%H-%M-%S"` (existing pattern) | Already used by `run-scanner.sh`. Consistent with existing run directories. [VERIFIED: run-scanner.sh line 13] |
| Deduplication | Custom dedup | Existing `dedup-findings.sh` | Already implemented in Phase 2. [VERIFIED: codebase] |

**Key insight:** This phase is primarily glue code. Nearly every component either exists or follows an established codebase pattern. The creative work is in the categorizer system prompt and orchestrator system prompt.

## Common Pitfalls

### Pitfall 1: Orchestrator Context Window Exhaustion
**What goes wrong:** The orchestrator agent spawns subagents that do heavy web research. If the orchestrator tries to run the full pipeline (scanner + researcher + reviewer + categorizer) in one invocation, it may exhaust its context window.
**Why it happens:** Each subagent invocation returns output to the orchestrator's context. Multiple findings multiplied by multiple stages can fill the window.
**How to avoid:** Split the pipeline into two orchestrator invocations: (1) scan phase (scanner only), (2) research phase (researcher + reviewer + categorizer for each approved finding). The Python script manages this split with separate `claude -p --agent orchestrator` calls. Set `--max-turns` appropriately.
**Warning signs:** Orchestrator starting to repeat itself, losing track of which findings have been processed.

### Pitfall 2: Symlink Relative Path Issues
**What goes wrong:** Symlinks created with absolute paths break when the repo is moved. Symlinks with wrong relative paths point to nothing.
**Why it happens:** `ln -s` target path interpretation depends on whether it is relative to the symlink location or the current directory.
**How to avoid:** Use relative paths from the symlink location. For a symlink at `reports/cybersecurity/subcategory/report.md` pointing to `reports/privacy/subcategory/report.md`, the target should be `../../privacy/subcategory/report.md`. The categorizer should compute relative paths.
**Warning signs:** `ls -la` shows broken symlinks (red in most terminals), `file` reports "broken symbolic link".

### Pitfall 3: Cron Environment Differences
**What goes wrong:** Pipeline works when run manually but fails from cron because PATH, HOME, or DISPLAY are different.
**Why it happens:** Cron runs with a minimal environment. `claude` CLI may not be in PATH. `notify-send` requires DISPLAY/DBUS_SESSION_BUS_ADDRESS for desktop notifications.
**How to avoid:** In the crontab entry: (1) set full PATH, (2) set DISPLAY=:0 for notify-send, (3) set DBUS_SESSION_BUS_ADDRESS for notify-send, (4) use absolute paths for the Python script and all tools. The Python script should also log environment info at startup for debugging.
**Warning signs:** Cron job runs but no notifications appear; cron mail shows "command not found" errors.

### Pitfall 4: Resume Logic State Confusion
**What goes wrong:** User runs `resume` on a run that hasn't been approved yet, or runs it on an already-completed run, leading to duplicate reports or errors.
**Why it happens:** No state tracking beyond file existence.
**How to avoid:** Check for `scanner-approved.json` existence before resuming. Check for `categorizer-output.json` to detect already-completed runs. The Python script should validate state before proceeding.
**Warning signs:** Duplicate reports in reports/ directory, error messages about missing files.

### Pitfall 5: Categorizer Schema Mismatch with Pending Flow
**What goes wrong:** The existing `categorizer.schema.json` does not account for pending subcategory proposals or symlink information.
**Why it happens:** Schema was created in Phase 1 as a minimal stub matching original requirements.
**How to avoid:** Extend the categorizer schema to include `is_pending`, `proposed_subcategory`, `symlinks` fields, or handle pending items outside the main categorizer output (separate pending metadata files).
**Warning signs:** Schema validation fails after categorizer produces output with new fields.

## Code Examples

### Python Entry Point Structure
```python
# Source: D-12, D-15 from CONTEXT.md [ASSUMED structure]
#!/usr/bin/env python3
"""Zwiad pipeline entry point."""
import argparse
import subprocess
import json
import os
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

def create_run_id():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%S")

def setup_run_dir(run_id):
    run_dir = PROJECT_ROOT / "pipeline" / "runs" / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir

def notify(title, message):
    """Send desktop notification via notify-send."""
    try:
        subprocess.run(
            ["notify-send", "--urgency=normal", f"Zwiad: {title}", message],
            timeout=5
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass  # Non-critical

def run_scan_phase(run_id, run_dir, input_file=None, web_only=False):
    """Run scanner -> dedup -> generate review -> pause for approval."""
    # ... invoke scanner, dedup, generate-review scripts
    notify("Findings Ready", f"Run {run_id}: Review scanner findings")

def run_research_phase(run_id, run_dir):
    """Resume: approved findings -> researcher -> reviewer -> categorizer."""
    # ... invoke remaining pipeline stages
    notify("Pipeline Complete", f"Run {run_id}: Reports filed")
```

### Crontab Entry
```bash
# Source: CLAUDE.md scheduling section [VERIFIED: cron recommended for headless Tegra]
# Daily at 6 AM UTC
DISPLAY=:0
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
PATH=/home/rafal/.local/bin:/usr/local/bin:/usr/bin:/bin

0 6 * * * cd /home/rafal/projecty/Zwiad && /usr/bin/python3 run_pipeline.py run --web-only >> pipeline/logs/cron.log 2>&1
```

### Audit Log Template
```markdown
# Pipeline Audit Log

**Run ID:** 2026-04-07T06-00-00
**Started:** 2026-04-07T06:00:00Z
**Completed:** 2026-04-07T06:15:23Z
**Status:** complete | partial | error

## Scanner
- **Duration:** 3m 12s
- **Sources scanned:** 8
- **Findings produced:** 5
- **Source failures:** 1 (FTC website timeout)

## Human Review
- **Approved:** 3 of 5 findings
- **Rejected:** 2
- **Approved findings:** SCAN-20260407-001, SCAN-20260407-003, SCAN-20260407-005

## Researcher
- **Reports produced:** 3
- **Format breakdown:** 2 client-alerts, 1 research-memo
- **Failures:** 0

## Reviewer
- **Verified:** 2
- **Escalated:** 1 (SCAN-20260407-005)
- **Total rounds:** 5

## Categorizer
- **Filed:** 2 reports
- **Pending subcategory:** 1 (proposed "biometric-data" under privacy)
- **Symlinks created:** 1

## Errors
None
```

### Categorizer Agent Prompt Pattern
```markdown
# Source: D-01, D-02, D-03, D-04 from CONTEXT.md [ASSUMED prompt structure]
## Categorization Process
1. Read pipeline/config/categories.json for known subcategories
2. Read reviewer-output.json for verified reports
3. For each verified report:
   a. Read the report markdown
   b. Determine primary topic (privacy / cybersecurity / ai-law)
   c. Determine subcategory from known list OR propose new one
   d. If subcategory is known: file report to reports/{topic}/{subcategory}/
   e. If subcategory is new: file to pipeline/pending/, write proposal
   f. Determine secondary topics, create symlinks
4. Write categorizer-output.json
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Bash-only orchestration | Python entry + Claude agent orchestration | This phase | Python handles infra concerns; agent handles pipeline logic |
| Flat topic directories | Topic/subcategory hierarchy | This phase | More organized report filing as volume grows |
| Manual pipeline invocation | Cron-triggered with notifications | This phase | Daily automated scanning with human-in-the-loop approval |

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | argparse is sufficient for run/resume subcommands (vs click) | Standard Stack | Low -- argparse is stdlib, adequate for 2 subcommands. If inadequate, easy to refactor. |
| A2 | Seed subcategory list contents are reasonable for privacy/cybersecurity/ai-law domains | Architecture Patterns | Medium -- wrong seeds just mean more pending proposals initially. Registry is human-editable. |
| A3 | DISPLAY=:0 and DBUS_SESSION_BUS_ADDRESS will work for notify-send from cron on Tegra | Common Pitfalls | Medium -- may need to discover actual DBUS address at runtime. Test required. |
| A4 | Orchestrator can manage researcher->reviewer->categorizer for 3-5 findings within context window with max-turns 30 | Common Pitfalls | High -- if context overflows, need to split into per-finding orchestrator calls or use bash script for outer loop. |

## Open Questions

1. **Orchestrator invocation strategy: single vs split**
   - What we know: D-14 says orchestrator manages full flow via Agent tool. D-08 says pipeline pauses at approval gate.
   - What's unclear: Whether one orchestrator invocation handles scan+pause, or the Python script calls the orchestrator twice (once for scan, once for research). Existing bash scripts (run-scanner.sh, run-researcher.sh, run-reviewer.sh) each invoke agents directly -- the orchestrator has not been used yet.
   - Recommendation: Python script calls individual bash scripts (or claude CLI directly) for each stage, rather than relying on one orchestrator agent invocation for everything. This is more reliable, debuggable, and avoids context window concerns. The orchestrator agent prompt can still define the logical flow but the Python script drives execution. This aligns with how the codebase actually works (individual stage scripts) while satisfying D-12 (Python entry point) and D-14 (orchestrator manages flow).

2. **Categorizer schema extension for pending/symlink status**
   - What we know: Existing schema has `filed_reports` with `finding_id, source_path, destination_path, topic, subcategory`. D-03 requires pending flow. D-04 requires symlinks.
   - What's unclear: Whether to extend the existing schema or use a separate data structure for pending items.
   - Recommendation: Extend categorizer schema to add optional `is_pending` boolean and `symlinks` array. Pending items still appear in `filed_reports` but with `is_pending: true` and `destination_path` pointing to `pipeline/pending/`.

3. **DBUS_SESSION_BUS_ADDRESS for cron notifications**
   - What we know: notify-send 0.7.9 is installed and works from terminal.
   - What's unclear: Exact DBUS address needed for cron on this Tegra system.
   - Recommendation: Test with `echo $DBUS_SESSION_BUS_ADDRESS` in an interactive session, hardcode in crontab. Add fallback (log to file) if notification fails.

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| Python 3 | Pipeline entry point (D-12) | Yes | 3.10.12 | -- |
| Claude Code CLI | Agent execution | Yes | 2.1.92 | -- |
| jq | Schema validation | Yes | System | -- |
| notify-send | Desktop notifications (D-09) | Yes | 0.7.9 | Log to file |
| cron | Scheduled execution (PIPE-04) | Yes | System | -- |
| Symlink support | Multi-topic reports (D-04) | Yes | Linux native | -- |
| bash | Existing scripts | Yes | System | -- |

**Missing dependencies with no fallback:** None

**Missing dependencies with fallback:** None -- all dependencies available.

## Validation Architecture

### Test Framework
| Property | Value |
|----------|-------|
| Framework | bash + manual testing (no formal test framework in project) |
| Config file | None -- project uses ad-hoc validation scripts |
| Quick run command | `bash pipeline/scripts/validate-handoff.sh categorizer <file>` |
| Full suite command | Manual end-to-end pipeline run |

### Phase Requirements to Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| PIPE-01 | Reports filed into topic/subcategory folders | smoke | `ls -la reports/{topic}/{subcategory}/` after categorizer run | No -- Wave 0 |
| PIPE-01 | Symlinks created for multi-topic reports | smoke | `find reports/ -type l` after categorizer run | No -- Wave 0 |
| PIPE-01 | Pending subcategory proposals filed correctly | smoke | `ls pipeline/pending/` after categorizer proposes new subcategory | No -- Wave 0 |
| PIPE-02 | Audit log produced per run | smoke | `test -f pipeline/runs/<run-id>/audit-log.md` | No -- Wave 0 |
| PIPE-02 | Audit log contains all stage sections | smoke | `grep -c "^## " pipeline/runs/<run-id>/audit-log.md` (expect 5+) | No -- Wave 0 |
| PIPE-04 | Pipeline runs from cron | manual | Install crontab, verify next morning | No -- manual only |
| PIPE-04 | Notifications fire on approval-pending | manual | Check desktop after cron scanner run | No -- manual only |
| PIPE-04 | Resume mode picks up from approved state | smoke | `python3 run_pipeline.py resume <run-id>` after approval | No -- Wave 0 |

### Sampling Rate
- **Per task commit:** `bash pipeline/scripts/validate-handoff.sh categorizer <test-file>`
- **Per wave merge:** Manual end-to-end pipeline run with test data
- **Phase gate:** Full pipeline run: scan -> approve -> resume -> verify reports filed

### Wave 0 Gaps
- [ ] Test categorizer output validation: create a mock categorizer-output.json and validate with `validate-handoff.sh categorizer`
- [ ] Test `run_pipeline.py` argument parsing: `python3 run_pipeline.py --help`, `python3 run_pipeline.py run --web-only` (dry-run mode)
- [ ] Test notify-send from cron environment: `env -i DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus notify-send "test" "test"`

## Security Domain

### Applicable ASVS Categories

| ASVS Category | Applies | Standard Control |
|---------------|---------|-----------------|
| V2 Authentication | No | N/A -- local CLI tool, no auth |
| V3 Session Management | No | N/A -- stateless pipeline runs |
| V4 Access Control | No | N/A -- single-user local system |
| V5 Input Validation | Yes | jq schema validation via validate-handoff.sh; Python argparse for CLI args |
| V6 Cryptography | No | N/A -- no secrets or encryption in this phase |

### Known Threat Patterns

| Pattern | STRIDE | Standard Mitigation |
|---------|--------|---------------------|
| Path traversal in report filing | Tampering | Validate destination_path starts with `reports/` prefix. Existing pattern from run-researcher.sh line 66-69. [VERIFIED: codebase] |
| Symlink escape | Tampering | Validate symlink targets stay within reports/ directory tree |
| Cron command injection | Tampering | Hardcode crontab entry; no user-controlled input in cron line |
| Finding ID injection in approval | Tampering | Already mitigated in approve-findings.sh (T-02-07: strict pattern matching, validation against source data). [VERIFIED: codebase] |

## Sources

### Primary (HIGH confidence)
- Codebase inspection: all `.claude/agents/*.md` files, all `pipeline/scripts/*.sh` files, all `pipeline/schemas/*` files
- System verification: Python 3.10.12, Claude CLI 2.1.92, notify-send 0.7.9, symlink support, cron availability
- Phase 1-4 CONTEXT.md files for architectural decisions

### Secondary (MEDIUM confidence)
- CLAUDE.md technology stack recommendations (scheduling, model assignments, CLI patterns)

### Tertiary (LOW confidence)
- None

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH -- all tools verified on system, all stdlib
- Architecture: HIGH -- follows established codebase patterns, locked decisions are clear
- Pitfalls: MEDIUM -- cron environment and orchestrator context window concerns need runtime testing

**Research date:** 2026-04-07
**Valid until:** 2026-05-07 (stable -- no fast-moving dependencies)
