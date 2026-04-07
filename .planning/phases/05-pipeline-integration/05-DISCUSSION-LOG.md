# Phase 5: Pipeline Integration - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-04-07
**Phase:** 05-pipeline-integration
**Areas discussed:** Subcategory strategy, Audit trail design, Scheduling & automation, Orchestrator end-to-end flow

---

## Subcategory Strategy

| Option | Description | Selected |
|--------|-------------|----------|
| Fully emergent | Categorizer reads existing subfolder names, assigns or creates. No seed list. | |
| Seed list + emergent | Start with predefined list, allow categorizer to create new ones when content doesn't fit. | ✓ |
| You decide | Claude picks during planning. | |

**User's choice:** Seed list + emergent
**Notes:** None

---

| Option | Description | Selected |
|--------|-------------|----------|
| Config file | JSON/YAML in pipeline/config/ listing known subcategories per topic. Human-editable, version-controlled. | ✓ |
| Filesystem only | No registry file — read existing subfolder names. Seed subcategories as empty dirs. | |
| You decide | Claude picks storage approach. | |

**User's choice:** Config file
**Notes:** None

---

| Option | Description | Selected |
|--------|-------------|----------|
| Auto-create, log it | Creates subfolder and adds to config automatically. Appears in audit log. | |
| Flag for review | Suggests new subcategory but doesn't create until human confirms. Report filed in /pending/. | ✓ |
| You decide | Claude picks based on pipeline flow. | |

**User's choice:** Flag for review
**Notes:** None

---

| Option | Description | Selected |
|--------|-------------|----------|
| Primary topic only | Each report in one topic folder based on best fit. Simpler, avoids duplication. | |
| Symlinks for secondary topics | Filed in primary topic folder, symlinks from secondary. Discoverable from multiple paths. | ✓ |
| You decide | Claude picks during planning. | |

**User's choice:** Symlinks for secondary topics
**Notes:** None

---

## Audit Trail Design

| Option | Description | Selected |
|--------|-------------|----------|
| Markdown summary | Human-readable markdown in each run directory. Easy to review in VS Code/Obsidian. | ✓ |
| JSON log | Machine-readable JSON. Better for programmatic analysis. Less pleasant to read. | |
| Both | JSON for data, markdown for readability. Two files per run. | |

**User's choice:** Markdown summary
**Notes:** None

---

| Option | Description | Selected |
|--------|-------------|----------|
| Stage summaries | Per-stage section: what ran, items processed, outcomes, duration. Compact and scannable. | ✓ |
| Full detail | Includes per-finding breakdown, reviewer feedback summaries, all source URLs. | |
| You decide | Claude picks right level of detail. | |

**User's choice:** Stage summaries
**Notes:** None

---

| Option | Description | Selected |
|--------|-------------|----------|
| Per-run logs only | Each run directory gets its own audit log. List runs directory for history. | ✓ |
| Cumulative index | Top-level pipeline/RUNS.md appending summary per run. Quick overview. | |
| You decide | Claude picks simplest approach. | |

**User's choice:** Per-run logs only
**Notes:** None

---

## Scheduling & Automation

| Option | Description | Selected |
|--------|-------------|----------|
| Pause and notify | Completes scanning, writes review file, stops. Sends notification. User approves then re-runs. | ✓ |
| Auto-approve for scheduled runs | Skip approval gate entirely. All findings go to research. Risky. | |
| Two-phase cron | First cron runs scanner, second runs rest later on approved items. | |

**User's choice:** Pause and notify
**Notes:** None

---

| Option | Description | Selected |
|--------|-------------|----------|
| Log file + stdout | Write status to pipeline/PENDING.md and log to stdout. Check manually. | |
| Desktop notification | Use notify-send for immediate visibility on Tegra system. | ✓ |
| You decide | Claude picks simplest for headless Linux. | |

**User's choice:** Desktop notification
**Notes:** None

---

| Option | Description | Selected |
|--------|-------------|----------|
| Manual re-run command | Run resume script with run-id. Picks up from approved state. | ✓ |
| Watch for APPROVED marker | Background watcher auto-resumes. More automated but complex. | |
| You decide | Claude picks during planning. | |

**User's choice:** Manual re-run command
**Notes:** None

---

| Option | Description | Selected |
|--------|-------------|----------|
| Log error, continue next day | Record in audit log. No retry. Next run proceeds normally. | |
| Retry once after delay | Wait 30 minutes and retry once. | |
| You decide | Claude picks based on fail-fast pattern. | |

**User's choice:** Log error + desktop notification, no retry (free-text)
**Notes:** User wants notification on failure too, not just logging. Consistent with fail-fast approach.

---

## Orchestrator End-to-End Flow

| Option | Description | Selected |
|--------|-------------|----------|
| Single bash script | ./run-pipeline.sh calling `claude -p --agent orchestrator`. Cron calls same script. | |
| Orchestrator agent directly | User runs `claude -p --agent orchestrator` directly. No wrapper. | |
| You decide | Claude picks entry point approach. | |

**User's choice:** Python script (free-text: "i am a bigger fan of python rather than bash scripts")
**Notes:** User prefers Python for the main entry point. Existing bash utility scripts stay.

---

| Option | Description | Selected |
|--------|-------------|----------|
| Keep bash utilities | Existing bash scripts are small jq wrappers. Only main entry point moves to Python. | ✓ |
| Rewrite all in Python | Replace all bash with Python using json module. Consistent but more work. | |
| You decide | Claude picks per script. | |

**User's choice:** Keep bash utilities
**Notes:** Pragmatic migration — only main orchestration logic in Python.

---

| Option | Description | Selected |
|--------|-------------|----------|
| Orchestrator agent manages flow | Python launches orchestrator once. Orchestrator spawns subagents. Python handles pre/post. | ✓ |
| Python drives each stage | Python calls each agent directly via subprocess. Bypasses orchestrator pattern. | |
| You decide | Claude picks during planning. | |

**User's choice:** Orchestrator agent manages flow
**Notes:** Matches Phase 1 design (D-09).

---

| Option | Description | Selected |
|--------|-------------|----------|
| Email digest file only | Core use case from Phase 2. Web-only scanning added later. | |
| Email digest + web-only mode | Two modes: email digest input or web-only scan (search sites without email). | ✓ |
| You decide | Claude picks simplest for v1. | |

**User's choice:** Email digest + web-only mode
**Notes:** More flexible from day one.

---

## Claude's Discretion

- Seed subcategory list contents
- Audit log markdown template layout
- Orchestrator system prompt structure
- Python argument parsing library
- Notification message formatting
- Primary vs secondary topic determination logic
- Pipeline run ID generation format

## Deferred Ideas

None — discussion stayed within phase scope
