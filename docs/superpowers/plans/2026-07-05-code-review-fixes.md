# Code Review Remediation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix all Critical and Important findings from the 2026-07-05 full code review of the Zwiad pipeline, in the review's recommended order.

**Architecture:** Five phases: (1) agent/validator contract fixes so the next pipeline run doesn't halt; (2) cron-readiness for the bot and CLI runner (timeouts, concurrency, shared stage-runner module); (3) data-quality fixes to URL normalization, bill keys, bill versioning, and index safety; (4) a pytest suite for the pure helper modules plus a validator round-trip check; (5) the remaining Important/Minor items.

**Tech Stack:** Python 3.10 (stdlib + discord.py), bash, jq schemas, Claude Code agent markdown.

## Global Constraints

- Runtime is Claude Code CLI (`claude -p`) — no Anthropic API keys, no SDK.
- All state is local filesystem JSON/markdown; writes to shared state files must be atomic (`mkstemp` + `os.replace`).
- Max 3 researcher/reviewer iteration rounds before human escalation (unchanged).
- The repo working tree has many unrelated uncommitted changes (reports, pipeline state). **Every commit must `git add` only the files named in its task** — never `git add -A`.
- Tests live in `tests/` at the project root; run with `python3 -m pytest tests/ -v`. Create `tests/__init__.py` empty file in the first task that adds a test.
- Decision taken for the uncommitted opus→sonnet model downgrade: **keep sonnet** (matches current working-tree intent, likely a cost/rate-limit decision) and update CLAUDE.md's model table to match. Flag in the final summary so the user can revert.

---

## Phase 1 — Contract fixes (before the next pipeline run)

### Task 1: `append_update` branch in researcher validator

**Files:**
- Modify: `pipeline/schemas/researcher.jq`
- Modify: `pipeline/schemas/researcher.schema.json`

**Interfaces:**
- Produces: validator accepts `reports[]` entries with `operation: "append_update"` requiring only `finding_id`, `report_path`, `topic_key`, `topic_type` (+ optional delta fields), while non-update entries keep the full requirement set. This matches `researcher.md:162`.

- [ ] **Step 1: Write a failing round-trip check.** Create two fixture files in `/tmp/claude-1000/-home-rafal-projecty-Zwiad/8daa7afe-b6a7-4fad-8ad4-4f3b97ec0453/scratchpad/` (or a temp dir):

`fixture-update.json`:
```json
{
  "schema_version": "1.0",
  "pipeline_run_id": "2026-07-05T00-00-00",
  "timestamp": "2026-07-05T00:00:00Z",
  "stage": "researcher",
  "status": "complete",
  "data": {
    "reports": [
      {
        "finding_id": "SCAN-20260705-001",
        "report_path": "bills/virginia/SB-338/current.md",
        "topic_key": "VA-SB-338-2026",
        "topic_type": "state_bill",
        "operation": "append_update",
        "update_markdown": "## Update 2026-07-05\nPassed the Senate.",
        "status_after": "passed-first-chamber"
      }
    ]
  }
}
```

`fixture-full.json`: same envelope but the report entry has `format: "client-alert"`, `jurisdiction_tags: ["VA"]`, `confidence_summary: {"high": 3, "medium": 1, "low": 0}`, `topic_key`, `topic_type`, and NO `operation` field.

Run: `jq -e -f pipeline/schemas/researcher.jq fixture-update.json`
Expected: **exit 1** (currently fails — `format` is unconditionally required).

- [ ] **Step 2: Replace `pipeline/schemas/researcher.jq`** with:

```jq
(.data.reports | type == "array") and
(.data.reports | all(
  (.finding_id | type == "string") and
  (.report_path | type == "string") and
  (if (.operation // "") == "append_update" then
    (.topic_key | type == "string") and
    (.topic_type | type == "string")
  else
    (.format | type == "string") and
    (.format | IN("client-alert", "research-memo")) and
    (.jurisdiction_tags | type == "array") and
    (.confidence_summary | type == "object") and
    (.confidence_summary.high | type == "number") and
    (.confidence_summary.medium | type == "number") and
    (.confidence_summary.low | type == "number")
  end)
))
```

- [ ] **Step 3: Update `pipeline/schemas/researcher.schema.json`** — replace the single `items` object with a `oneOf`. The first branch is the existing object unchanged. The second branch (update entries):

```json
{
  "type": "object",
  "required": ["finding_id", "report_path", "topic_key", "topic_type", "operation"],
  "properties": {
    "finding_id": { "type": "string" },
    "report_path": { "type": "string" },
    "topic_key": { "type": "string" },
    "topic_type": { "type": "string", "enum": ["state_bill", "federal_bill", "enforcement", "rulemaking", "guidance", "other"] },
    "operation": { "const": "append_update" },
    "update_markdown": { "type": "string" },
    "status_after": { "type": "string" },
    "diff_signal": { "type": "string" },
    "source_url": { "type": "string" }
  },
  "additionalProperties": true
}
```

Also add `"operation": false` is NOT expressible in the first branch — instead add `"not": { "required": ["operation"] }` to the first branch so the two branches are disjoint.

- [ ] **Step 4: Verify both fixtures pass.**
Run: `jq -e -f pipeline/schemas/researcher.jq fixture-update.json && jq -e -f pipeline/schemas/researcher.jq fixture-full.json && bash pipeline/scripts/validate-handoff.sh researcher fixture-update.json`
Expected: all succeed. Also verify a broken fixture (full entry missing `format`) still fails.

- [ ] **Step 5: Commit**
```bash
git add pipeline/schemas/researcher.jq pipeline/schemas/researcher.schema.json
git commit -m "schemas: accept append_update researcher entries per researcher.md contract"
```

### Task 2: Unify escalation artifact naming on `escalation-<finding_id>.json`

**Files:**
- Modify: `pipeline/scripts/generate-escalation.sh`
- Modify: `pipeline/scripts/run-reviewer.sh` (line ~241, the "Next:" hint)

**Interfaces:**
- Produces: every escalation now creates BOTH `reviewer-escalation-<id>.md` (human-readable, unchanged) and `escalation-<id>.json` (machine-readable). The `.json` name matches the gate globs in `orchestrator.md:213`, `run_pipeline.py`, and `discord_bot.py:1411`.

- [ ] **Step 1: Add JSON emission to `generate-escalation.sh`.** After the existing `} > "$OUTPUT"` block (line 145), add:

```bash
# Machine-readable companion — the orchestrator/bot escalation gates glob
# escalation-*.json, so this file is what actually pauses the pipeline.
JSON_OUTPUT="$RUN_DIR/escalation-${FINDING_ID}.json"
jq -n \
  --arg run_id "$RUN_ID" \
  --arg finding_id "$FINDING_ID" \
  --arg report_path "$REPORT_PATH" \
  --arg md_path "$(basename "$OUTPUT")" \
  --argjson unresolved "$UNRESOLVED" \
  '{
    run_id: $run_id,
    finding_id: $finding_id,
    report_path: $report_path,
    escalation_md: $md_path,
    rounds_completed: 3,
    unresolved_issues: $unresolved,
    resolved: false
  }' > "$JSON_OUTPUT"
echo "Escalation JSON written to: $JSON_OUTPUT"
```

- [ ] **Step 2: Update the hint in `run-reviewer.sh`** — change line 241 from `echo "Next: Resolve escalations in $RUN_DIR/reviewer-escalation-*.md"` to mention both files: `echo "Next: Resolve escalations in $RUN_DIR/reviewer-escalation-*.md (JSON gate files: escalation-*.json)"`.

- [ ] **Step 3: Verify.** Create a fake run dir with a `reviewer-feedback-r3-SCAN-TEST-001.json` containing one open critical issue (shape: `{"issues":[{"claim":"c","issue":"i","severity":"critical","status":"open","suggested_fix":"f"}],"claims_checked":1}`), run `bash pipeline/scripts/generate-escalation.sh <fake-run-id> SCAN-TEST-001 reports/privacy/test.md`, and confirm both `reviewer-escalation-SCAN-TEST-001.md` and `escalation-SCAN-TEST-001.json` exist and the JSON parses with `jq .`. Delete the fake run dir afterward.

- [ ] **Step 4: Commit**
```bash
git add pipeline/scripts/generate-escalation.sh pipeline/scripts/run-reviewer.sh
git commit -m "pipeline: emit escalation-<id>.json so orchestrator/bot gates actually fire"
```

### Task 3: Implement the `append_update` branch in `run-reviewer.sh` + extend `reviewer.jq`

**Files:**
- Modify: `pipeline/scripts/run-reviewer.sh`
- Modify: `pipeline/schemas/reviewer.jq`
- Modify: `.claude/agents/reviewer.md` (remove the batch framing at line ~40)

**Interfaces:**
- Consumes: researcher outputs where update entries carry `operation: "append_update"` (Task 1's contract).
- Produces: `reviewer-output.json` review entries for updates carry `operation: "append_update"`, `verdict` (`auto_approved` | `needs-human-review`), `verdict_reason`; `iteration_count` is 1; the researcher is never re-invoked for updates; `bills/` report paths are accepted for update entries only.

- [ ] **Step 1: Capture `operation` when collecting reports.** In `run-reviewer.sh` the per-report loop reads fields at lines 61-62. Add after line 62:

```bash
  OPERATION=$(echo "$REPORTS_JSON" | jq -r ".[$i].operation // \"\"")
```

- [ ] **Step 2: Relax the path guard for update entries.** Replace the guard at lines 72-76 with:

```bash
  # T-04-02: full reports must live under reports/{privacy,cybersecurity,ai-law}/.
  # Update entries (append_update) may also target tracked-bill files under bills/.
  if [ "$OPERATION" = "append_update" ]; then
    if [[ ! "$REPORT_PATH" =~ ^(reports/(privacy|cybersecurity|ai-law)|bills)/ ]]; then
      echo "ERROR: Invalid update report path: $REPORT_PATH" >&2
      FAILED=$((FAILED + 1))
      continue
    fi
  elif [[ ! "$REPORT_PATH" =~ ^reports/(privacy|cybersecurity|ai-law)/ ]]; then
    echo "ERROR: Invalid report path: $REPORT_PATH" >&2
    FAILED=$((FAILED + 1))
    continue
  fi
```

- [ ] **Step 3: Single-pass update review.** Immediately after the path guard (before `ROUND=1`), insert the update branch. It invokes the reviewer once, never loops, never calls the researcher, and derives the verdict from the feedback file:

```bash
  if [ "$OPERATION" = "append_update" ]; then
    echo "Reviewing UPDATE $((i+1))/$REPORT_COUNT: $FINDING_ID (single-pass)"
    FEEDBACK_FILE="$RUN_DIR/reviewer-feedback-r1-${FINDING_ID}.json"
    PROMPT="Single-pass update review for finding $FINDING_ID (operation append_update)."
    PROMPT="$PROMPT Review the appended update in $REPORT_PATH."
    PROMPT="$PROMPT Pipeline run: $RUN_ID. Round: 1. This is an append_update entry:"
    PROMPT="$PROMPT do NOT iterate; apply pipeline/config/update-review-policy.json once."
    PROMPT="$PROMPT Write your feedback to: $FEEDBACK_FILE."

    claude -p --agent reviewer \
      --output-format json \
      --permission-mode acceptEdits \
      --max-turns 15 \
      "$PROMPT"

    VERDICT="needs-human-review"
    VERDICT_REASON="Reviewer produced no valid feedback"
    UPDATE_ISSUES="[]"
    UPDATE_CLAIMS=0
    if [ -f "$FEEDBACK_FILE" ] && jq -e -f "$PROJECT_ROOT/pipeline/schemas/reviewer-feedback.jq" "$FEEDBACK_FILE" >/dev/null 2>&1; then
      UPDATE_CLAIMS=$(jq '.claims_checked' "$FEEDBACK_FILE")
      CRITICAL_MAJOR=$(jq '[.issues[] | select(.severity == "critical" or .severity == "major")] | length' "$FEEDBACK_FILE")
      if [ "$CRITICAL_MAJOR" -eq 0 ]; then
        VERDICT="auto_approved"
        VERDICT_REASON="No critical/major issues in single-pass update review"
        STATUS="verified"
        VERIFIED=$((VERIFIED + 1))
      else
        VERDICT_REASON="$CRITICAL_MAJOR critical/major issue(s) in update review"
        STATUS="needs-human-review"
        ESCALATED=$((ESCALATED + 1))
      fi
      UPDATE_ISSUES=$(jq '[.issues[] | {claim: .claim, issue: .issue, severity: .severity}]' "$FEEDBACK_FILE")
    else
      STATUS="needs-human-review"
      ESCALATED=$((ESCALATED + 1))
    fi

    REVIEW_ENTRY=$(jq -n \
      --arg fid "$FINDING_ID" --arg rp "$REPORT_PATH" --arg st "$STATUS" \
      --arg v "$VERDICT" --arg vr "$VERDICT_REASON" \
      --argjson cc "$UPDATE_CLAIMS" --argjson iss "$UPDATE_ISSUES" \
      '{
        finding_id: $fid, report_path: $rp, status: $st,
        operation: "append_update", verdict: $v, verdict_reason: $vr,
        iteration_count: 1, claims_checked: $cc, issues_found: $iss
      }')
    REVIEWS_JSON=$(echo "$REVIEWS_JSON" | jq --argjson entry "$REVIEW_ENTRY" '. + [$entry]')
    echo ""
    continue
  fi
```

- [ ] **Step 4: Extend `pipeline/schemas/reviewer.jq`** so entries may optionally carry the update fields. Replace the file with:

```jq
(.data.reviews | type == "array") and
(.data.reviews | all(
  (.finding_id | type == "string") and
  (.report_path | type == "string") and
  (.status | type == "string") and
  (.status | IN("verified", "disputed", "needs-human-review")) and
  (.iteration_count | type == "number") and
  (.iteration_count >= 1) and
  (.iteration_count <= 3) and
  (.claims_checked | type == "number") and
  (.issues_found | type == "array") and
  (.issues_found | all(
    (.claim | type == "string") and
    (.issue | type == "string") and
    (.severity | type == "string") and
    (.severity | IN("critical", "major", "minor"))
  )) and
  (if has("operation") then
    (.operation == "append_update") and
    (.verdict | type == "string") and
    (.verdict | IN("auto_approved", "needs-human-review"))
  else true end)
))
```

- [ ] **Step 5: Fix `reviewer.md` batch framing.** In `.claude/agents/reviewer.md`, replace the line `After processing all \`append_update\` entries, move on to any entries whose \`operation\` is NOT \`append_update\` and apply the normal verification flow below.` with: `You are invoked once per report. If the prompt says the entry is an append_update, apply only the single-pass flow above; otherwise apply the normal verification flow below.`

- [ ] **Step 6: Verify.** `bash -n pipeline/scripts/run-reviewer.sh` (syntax). Then build a fixture `reviewer-output.json` containing one normal entry and one update entry (with `operation`/`verdict`) and run `jq -e -f pipeline/schemas/reviewer.jq` on it — expect success. An update entry with `verdict: "bogus"` must fail.

- [ ] **Step 7: Commit**
```bash
git add pipeline/scripts/run-reviewer.sh pipeline/schemas/reviewer.jq .claude/agents/reviewer.md
git commit -m "pipeline: implement single-pass append_update review branch in run-reviewer.sh"
```

### Task 4: Add `fpf-scanner` to envelope stage enum; fix reviewer toolset

**Files:**
- Modify: `pipeline/schemas/envelope.jq` (line 5)
- Modify: `pipeline/schemas/envelope.schema.json` (matching enum)
- Modify: `.claude/agents/reviewer.md` (frontmatter line 4)

- [ ] **Step 1:** In `envelope.jq` line 5 change the enum to `IN("scanner", "human-review", "researcher", "reviewer", "categorizer", "fpf-scanner")`. Make the same enum addition in `envelope.schema.json` (find the `stage` enum array and append `"fpf-scanner"`).
- [ ] **Step 2:** In `.claude/agents/reviewer.md` frontmatter change `tools: Read, WebFetch, WebSearch` to `tools: Read, Write, Edit, WebFetch, WebSearch` — the prompt requires writing feedback JSON files and inserting `<!-- verified -->` annotations, so the declared list was false documentation.
- [ ] **Step 3: Verify:** run `jq -e -f pipeline/schemas/envelope.jq` against a minimal fpf-scanner envelope fixture (stage `fpf-scanner`, status `complete`, string schema_version/pipeline_run_id/timestamp, object data) — expect success.
- [ ] **Step 4: Commit**
```bash
git add pipeline/schemas/envelope.jq pipeline/schemas/envelope.schema.json .claude/agents/reviewer.md
git commit -m "schemas: allow fpf-scanner stage; reviewer.md declares the tools it actually needs"
```

### Task 5: Commit the model decision + CLAUDE.md alignment

**Files:**
- Modify: `CLAUDE.md` (Models table + Token Cost Considerations)
- Commit (already modified): `.claude/agents/researcher.md`, `.claude/agents/reviewer.md` model lines

- [ ] **Step 1:** In `CLAUDE.md`, in the "Models (per agent role)" table change Researcher and Reviewer rows from `opus` to `sonnet` and update the Why cells to note: "Downgraded from opus 2026-07: cost/rate-limit tradeoff; revisit if verification quality drops." Make the same change in the "Token Cost Considerations" table rows.
- [ ] **Step 2: Commit** (this intentionally picks up the pre-existing uncommitted `model: sonnet` frontmatter edits):
```bash
git add CLAUDE.md .claude/agents/researcher.md .claude/agents/reviewer.md
git commit -m "agents: record researcher/reviewer opus->sonnet downgrade in CLAUDE.md"
```

---

## Phase 2 — Cron-readiness (bot + CLI runner)

### Task 6: Shared stage-runner module with timeouts and rate-limit detection

**Files:**
- Create: `tools/claude_stage.py`
- Modify: `discord_bot.py` (delete moved functions, import from module)
- Test: `tests/test_claude_stage.py`

**Interfaces:**
- Produces: `tools/claude_stage.py` exporting:
  - `run_claude_and_log_cost(cmd: list[str], run_id: str, stage: str, cwd: Path | None = None, timeout: int = 3600) -> tuple[bool, str, float]`
  - `run_subprocess_checked(cmd: list[str], cwd: Path | None = None, capture: bool = True, timeout: int = 1800) -> tuple[bool, str]`
  - `looks_rate_limited(text: str, parsed: dict | None) -> bool`
  - `RUNS_DIR: Path` module constant (`PROJECT_ROOT / "pipeline" / "runs"`)
- Both entry points (`discord_bot.py`, `run_pipeline.py`) import from this module. Behavior is the bot's current implementation (`discord_bot.py:228-420`) plus timeouts.

- [ ] **Step 1: Write failing tests** in `tests/test_claude_stage.py` (create `tests/__init__.py` too):

```python
import subprocess
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tools.claude_stage import looks_rate_limited, _run_with_timeout, run_subprocess_checked


def test_rate_limit_detection_positive():
    assert looks_rate_limited("Error: Claude usage limit reached", None)
    assert looks_rate_limited("", {"result": "429 too many requests"})


def test_rate_limit_detection_negative():
    assert not looks_rate_limited("normal output", {"result": "done"})


def test_timeout_kills_process_tree():
    # A shell that spawns a child sleeping forever; must return within ~2s
    proc = _run_with_timeout(["bash", "-c", "sleep 300"], cwd=None, timeout=1)
    assert proc.timed_out


def test_run_subprocess_checked_timeout_reports_failure():
    ok, err = run_subprocess_checked(["bash", "-c", "sleep 300"], timeout=1)
    assert not ok
    assert "timed out" in err
```

Run: `python3 -m pytest tests/test_claude_stage.py -v` — Expected: FAIL (module doesn't exist).

- [ ] **Step 2: Create `tools/claude_stage.py`.** Move these verbatim from `discord_bot.py`, renaming `_looks_rate_limited` → `looks_rate_limited`: `_RATE_LIMIT_MARKERS`, `_looks_rate_limited` (:228-255), `_persist_stage_error` (:258-279), `run_subprocess_checked` (:282-304), `run_claude_and_log_cost` (:307-383), `_append_cost_entry` (:386-420). Use `get_logger("zwiad.stage")` from `tools.logging_setup`. Then add the timeout core and route both runners through it:

```python
from dataclasses import dataclass
import os
import signal
import subprocess


@dataclass
class _ProcResult:
    returncode: int
    stdout: str
    stderr: str
    timed_out: bool = False


def _run_with_timeout(cmd: list[str], cwd, timeout: int) -> _ProcResult:
    """Run *cmd* in its own process group, killing the whole group on timeout.

    claude -p spawns MCP-server children that hold the output pipes open, so a
    plain subprocess.run(timeout=...) can block in the post-kill read. Killing
    the process group avoids that.
    """
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=str(cwd) if cwd else None,
        start_new_session=True,
    )
    try:
        stdout, stderr = proc.communicate(timeout=timeout)
        return _ProcResult(proc.returncode, stdout or "", stderr or "")
    except subprocess.TimeoutExpired:
        try:
            os.killpg(proc.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        try:
            stdout, stderr = proc.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            stdout, stderr = "", ""
        return _ProcResult(-9, stdout or "", stderr or "", timed_out=True)
```

In `run_claude_and_log_cost`, replace the `subprocess.run(...)` call with `result = _run_with_timeout(cmd, cwd, timeout)`; add a `timeout: int = 3600` parameter; and right after cost logging, before the returncode check, add:

```python
    if result.timed_out:
        log_path = _persist_stage_error(run_id, stage, -9, result.stdout, result.stderr)
        log_hint = f" Partial output saved to `{log_path.name}`." if log_path else ""
        return False, f"{stage} timed out after {timeout}s and was killed.{log_hint}", cost_usd
```

In `run_subprocess_checked`, likewise replace `subprocess.run` with `_run_with_timeout(cmd, cwd, timeout)` (add `timeout: int = 1800` param) and return `(False, f"timed out after {timeout}s")` when `result.timed_out`.

- [ ] **Step 3:** In `discord_bot.py` delete the moved code and add near the other tool imports (after line 41):

```python
from tools.claude_stage import run_claude_and_log_cost, run_subprocess_checked  # noqa: E402
```

Call sites need no changes (same signatures; timeout defaults apply). Pass explicit timeouts at the long stages: `run_claude_and_log_cost(cmd, run_id, "research", cwd=PROJECT_ROOT, timeout=5400)` in `_run_research_phase` and the same in `_run_review_phase`.

- [ ] **Step 4: Run tests + compile check.**
Run: `python3 -m pytest tests/test_claude_stage.py -v && python3 -m py_compile discord_bot.py tools/claude_stage.py`
Expected: PASS, no compile errors.

- [ ] **Step 5: Commit**
```bash
git add tools/claude_stage.py discord_bot.py tests/__init__.py tests/test_claude_stage.py
git commit -m "bot: extract shared claude stage runner with process-group timeouts"
```

### Task 7: `run_pipeline.py` — use shared runner + phase-split resume

**Files:**
- Modify: `run_pipeline.py`

**Interfaces:**
- Consumes: `tools.claude_stage.run_claude_and_log_cost` (Task 6).
- Produces: `resume` now runs Mode 2 (research) then Mode 4 (review/categorize) as two stages, checking `research-complete.marker` between them — matching what `discord_bot.py` `/research` + `/review` do and what `orchestrator.md:98-222` specifies.

- [ ] **Step 1: Route stages through the shared runner.** In `run_stage` (`run_pipeline.py:65-110`) replace the `subprocess.run(...)` line with:

```python
    from tools.claude_stage import run_claude_and_log_cost
    ok, err, cost = run_claude_and_log_cost(cmd[:-1] + [cmd[-1]], run_id, name, cwd=PROJECT_ROOT, timeout=timeout)
```

Concretely: change `run_stage`'s signature to `run_stage(name, cmd, run_id, run_dir, audit_entries, timeout=3600)`, call `ok, err, cost = run_claude_and_log_cost(cmd, run_id, name, cwd=PROJECT_ROOT, timeout=timeout)`, and adapt the error path: on `not ok`, write `error.log` with `err`, append the audit error entry (`"error": err[:500]`), `notify(...)`, and `raise RuntimeError(f"Stage {name} failed: {err[:200]}")`. On success append the audit entry with `{"name": name, "duration_seconds": duration, "status": "complete", "cost_usd": cost}` (drop the dead `stdout_tail` field — review Minor 17). Keep the duration timing with `time.monotonic()` around the call. Remove the now-unused `import subprocess` if nothing else uses it (`notify` still does — keep it).

- [ ] **Step 2: Split `run_research_phase` into two stages.** Replace the body after the guards (`run_pipeline.py:191-223`) with:

```python
    research_prompt = (
        f"Research phase for run {run_id}. Process approved findings from "
        f"pipeline/runs/{run_id}/scanner-approved.json. "
        f"Follow Mode 2 (research-only): researcher per finding (skip findings whose "
        f"researcher-{{id}}.json already exists), then write research-complete.marker. "
        f"Do NOT invoke reviewer or categorizer."
    )
    cmd = [
        "claude", "-p", "--agent", "orchestrator",
        "--output-format", "json", "--permission-mode", "acceptEdits",
        "--max-turns", "200", research_prompt,
    ]
    run_stage("orchestrator-research", cmd, run_id, run_dir, audit_entries, timeout=5400)

    if not (run_dir / "research-complete.marker").exists():
        audit_entries.append({
            "name": "research-marker-check", "duration_seconds": 0, "status": "warning",
            "error": "research-complete.marker not found -- re-run resume to retry (idempotent)",
        })
        print("[WARN] research-complete.marker not found; stopping before review phase")
        return audit_entries

    review_prompt = (
        f"Review phase for run {run_id}. Mode 4 of the orchestrator instructions: "
        f"verify research-complete.marker exists, run reviewer, check escalations, "
        f"run categorizer if no escalations, and write pipeline-complete.marker. "
        f"Do NOT re-invoke researcher."
    )
    cmd = [
        "claude", "-p", "--agent", "orchestrator",
        "--output-format", "json", "--permission-mode", "acceptEdits",
        "--max-turns", "200", review_prompt,
    ]
    run_stage("orchestrator-review", cmd, run_id, run_dir, audit_entries, timeout=5400)

    complete_marker = run_dir / "pipeline-complete.marker"
    escalation_marker = run_dir / "has-escalations.marker"
    if escalation_marker.exists() or any(run_dir.glob("escalation-*.json")):
        notify("Escalations Pending", f"Run {run_id}: Review escalations")
    elif complete_marker.exists():
        notify("Pipeline Complete", f"Run {run_id}: Reports filed")
    else:
        audit_entries.append({
            "name": "review-marker-check", "duration_seconds": 0, "status": "warning",
            "error": "Neither pipeline-complete.marker nor escalations found",
        })
        print("[WARN] No completion marker found in run directory")
    return audit_entries
```

- [ ] **Step 3: Verify:** `python3 -m py_compile run_pipeline.py && python3 run_pipeline.py --help && python3 run_pipeline.py resume 1999-01-01T00-00-00; test $? -eq 1` (missing run dir must exit 1, not crash).

- [ ] **Step 4: Commit**
```bash
git add run_pipeline.py
git commit -m "pipeline: resume now runs split research+review phases via shared stage runner"
```

### Task 8: Bot concurrency guard, `cmd_scan` fall-through fix, run_id validation

**Files:**
- Modify: `discord_bot.py`

**Interfaces:**
- Produces: module-level `_active_runs: set[str]` + `_acquire_run(run_id) -> bool` / `_release_run(run_id)`; `_valid_run_id(run_id) -> bool` used by every command taking a `run_id` parameter.

- [ ] **Step 1: Add the guard helpers** after `latest_run_id` (line ~50):

```python
# In-flight pipeline stages: run_ids with a claude subprocess currently running.
# Prevents overlapping /scan//research//review invocations from corrupting a run.
_active_runs: set[str] = set()

_RUN_ID_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}$")


def _valid_run_id(run_id: str) -> bool:
    """run_id is used as a path component — accept only the timestamp shape."""
    return bool(_RUN_ID_RE.match(run_id or ""))


def _acquire_run(run_id: str) -> bool:
    if run_id in _active_runs:
        return False
    _active_runs.add(run_id)
    return True


def _release_run(run_id: str) -> None:
    _active_runs.discard(run_id)
```

- [ ] **Step 2: Validate user-supplied run_ids.** In each of `cmd_findings`, `cmd_approve`, `cmd_research`, `cmd_review`, `cmd_status`, `cmd_results`, immediately after the `run_id = run_id or ...` resolution and the `if not run_id` check, add:

```python
    if not _valid_run_id(run_id):
        await interaction.response.send_message(f"Invalid run id: `{run_id}`")
        return
```

(For commands that already responded, use `channel.send`; only `cmd_research`/`cmd_review` respond later — in all six the check goes before the first `interaction.response.send_message`, so `interaction.response` is correct.)

- [ ] **Step 3: Guard the three long-running commands.** In `cmd_scan` right after `run_id = datetime...` (line 863), in `cmd_research` and `cmd_review` right after run_id validation, add:

```python
    if not _acquire_run(run_id):
        await interaction.response.send_message(
            f"Run `{run_id}` already has a stage in progress — wait for it to finish."
        )
        return
```

(In `cmd_scan` the interaction is already answered, so place the `_acquire_run` before `interaction.response.send_message` — reorder so acquisition happens first.) Wrap the remainder of each command body in `try: ... finally: _release_run(run_id)`.

- [ ] **Step 4: Fix the `cmd_scan` fall-through.** At `discord_bot.py:1027-1028`, change:

```python
        if not scan_ok:
            await channel.send(f"Scan FAILED for `{run_id}` — {scan_err}")
```

to:

```python
        if not scan_ok:
            await channel.send(f"Scan FAILED for `{run_id}` — {scan_err}")
            detach_handler(audit_handler)
            return
```

(after Step 3's try/finally wrap, the `return` also releases the run guard; `latest_run_id = run_id` at :1032 is then never reached for failed scans — intended.)

- [ ] **Step 5: `get_latest_run_id` directory filter** (`discord_bot.py:510-515`): change the sort to name-based over directories only:

```python
def get_latest_run_id() -> str | None:
    """Return the most recent run_id by name (run ids are sortable timestamps)."""
    if not RUNS_DIR.exists():
        return None
    runs = sorted(
        (p for p in RUNS_DIR.iterdir() if p.is_dir() and _valid_run_id(p.name)),
        key=lambda p: p.name,
        reverse=True,
    )
    return runs[0].name if runs else None
```

- [ ] **Step 6: Verify:** `python3 -m py_compile discord_bot.py`. Also grep-check every `try:` added has a matching `finally: _release_run`.

- [ ] **Step 7: Commit**
```bash
git add discord_bot.py
git commit -m "bot: per-run concurrency guard, run_id validation, stop after scan failure"
```

### Task 9: Safe JSON reads + atomic writes + handler leak fixes in the bot

**Files:**
- Modify: `discord_bot.py`

- [ ] **Step 1: Add a safe reader** near the other helpers:

```python
def _read_run_json(path: Path) -> dict | None:
    """Read agent-produced JSON defensively. Agents drift; malformed JSON is a
    routine failure mode, not an exception. Returns None on any read error."""
    try:
        with open(path) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError) as e:
        logger.warning("Unreadable run JSON %s: %s", path, e)
        return None
```

- [ ] **Step 2: Use it at every agent-produced-JSON read.** Replace the bare `json.load(...)` at these sites, handling `None` by messaging the user (in command handlers) or returning empty (in helpers):
  - `load_findings` (:568) → `data = _read_run_json(path)`; `if data is None: continue` (fall through to next candidate file).
  - `load_candidate_updates` (:592) → return `[]` on None.
  - `find_run_reports` categorizer read (:699) and researcher fallback loop (:729) → on None, skip that file (`continue`) / return `[]`.
  - `write_approved_json` source read (:755-756) → on None, `raise RuntimeError(f"Cannot read {source_path.name}")`; in `cmd_approve` wrap the `write_approved_json` call in `try/except RuntimeError` and send the error to the user.
  - fpf results read (:937), approved read in `cmd_research` (:1264), approved read in `cmd_status` (:1503) → on None, send a warning message and skip that section.
  Also fix `write_approved_json`'s `f["id"]` / `u["id"]` (:761, :770) to `f.get("id")` / `u.get("id")` with a `if not ...: continue` skip.

- [ ] **Step 3: Atomic writes.** Add a helper and use it for `write_approved_json` (:784-786) and `_append_cost_entry`'s `cost_path.write_text` (now in `tools/claude_stage.py`):

```python
def _atomic_write_json(path: Path, data) -> None:
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=f".{path.stem}-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        os.replace(tmp, path)
    except Exception:
        if os.path.exists(tmp):
            os.remove(tmp)
        raise
```

Put one copy in `tools/claude_stage.py` (exported) and import it in `discord_bot.py` rather than duplicating.

- [ ] **Step 4: Handler-leak fix.** In `cmd_scan`, `cmd_research`, `cmd_review`: immediately after `audit_handler = attach_run_file_handler(logger, run_id)`, open a `try:` block ending in `finally: detach_handler(audit_handler)`, and delete all the scattered mid-body `detach_handler(audit_handler)` calls. This composes with Task 8's `_release_run` try/finally (one combined `finally: detach_handler(...); _release_run(run_id)` is fine).

- [ ] **Step 5: Fix the `load_findings` double-read** in `cmd_scan` (:1034-1035): change `load_findings` to compute both counts in one pass is invasive; simpler — keep the two calls but they now share `_read_run_json`; OR replace with:

```python
    all_findings = load_findings(run_id, us_only=False)
    findings = [f for f in all_findings if is_us_jurisdiction(f.get("jurisdiction"))]
    non_us_rejected = len(all_findings) - len(findings)
```

Use this replacement (single file read).

- [ ] **Step 6: Verify:** `python3 -m py_compile discord_bot.py`; grep for remaining bare `json.load(` in `discord_bot.py` — the only acceptable remaining sites are config reads with existing try/except (`_load_email_source_rules`, `classify_emails`, `_classify_updates`, `cmd_health`) and `load_tracker` (fix that one too with `_read_run_json`).

- [ ] **Step 7: Commit**
```bash
git add discord_bot.py tools/claude_stage.py
git commit -m "bot: defensive JSON reads, atomic writes, try/finally log handler cleanup"
```

---

## Phase 3 — Data quality

### Task 10: Rewrite `normalize_url` correctly + tests

**Files:**
- Modify: `tools/url_norm.py`
- Test: `tests/test_url_norm.py`

**Interfaces:**
- Produces: `normalize_url(url: str) -> str` — same name/signature, now: forces https, lowercases host, strips `www.`, drops fragments, removes `utm_*` and `g` query params, drops empty `?`, drops trailing `/` on the path, and is order-insensitive for the params it keeps (preserves original order of kept params).

- [ ] **Step 1: Write the failing tests** in `tests/test_url_norm.py`:

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tools.url_norm import normalize_url


def test_utm_first_param_does_not_mangle_url():
    assert normalize_url("https://x.com/a?utm_source=n&id=5") == "https://x.com/a?id=5"


def test_param_order_insensitive_for_stripping():
    a = normalize_url("https://x.com/a?utm_source=n&id=5")
    b = normalize_url("https://x.com/a?id=5&utm_source=n")
    assert a == b == "https://x.com/a?id=5"


def test_forces_https_and_strips_trailing_slash():
    assert normalize_url("http://example.com/foo/") == "https://example.com/foo"


def test_lexology_g_param_stripped():
    assert normalize_url("https://www.lexology.com/library/detail.aspx?g=abc123") == \
        "https://lexology.com/library/detail.aspx"


def test_host_lowercased_www_stripped_fragment_dropped():
    assert normalize_url("https://WWW.Example.com/Path#frag") == "https://example.com/Path"


def test_empty_and_whitespace():
    assert normalize_url("") == ""
    assert normalize_url("  https://a.com  ") == "https://a.com"


def test_non_http_garbage_passthrough():
    # No scheme: returned trimmed but untouched otherwise
    assert normalize_url("not a url") == "not a url"
```

Run: `python3 -m pytest tests/test_url_norm.py -v` — Expected: FAIL (`utm` first-param case).

- [ ] **Step 2: Replace `normalize_url`** in `tools/url_norm.py`:

```python
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

_STRIP_PARAMS_PREFIXES = ("utm_",)
_STRIP_PARAMS_EXACT = {"g"}  # Lexology tracking param


def normalize_url(url: str) -> str:
    """Strip tracking params and canonicalize a URL.

    Rules:
    - http:// -> https:// (force scheme)
    - lowercase host, strip leading www.
    - drop utm_* params and the Lexology g= param (order-insensitive)
    - drop fragments, empty query strings, and trailing / on the path
    - whitespace trim
    """
    if not url:
        return ""
    url = url.strip()
    parts = urlsplit(url)
    if parts.scheme not in ("http", "https"):
        return url  # not a web URL; leave untouched
    host = parts.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    kept = [
        (k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True)
        if not k.lower().startswith(_STRIP_PARAMS_PREFIXES)
        and k.lower() not in _STRIP_PARAMS_EXACT
    ]
    path = parts.path.rstrip("/") if parts.path != "/" else ""
    return urlunsplit(("https", host, path, urlencode(kept), ""))
```

(Remove the now-unused `import re` if nothing else in the file uses it.)

- [ ] **Step 3: Run tests:** `python3 -m pytest tests/test_url_norm.py -v` — Expected: PASS.

- [ ] **Step 4: One-time index repair.** Create `tools/oneoff/repair_index_urls.py`:

```python
#!/usr/bin/env python3
"""One-time repair: re-normalize every URL in reports/index.json.

Fixes legacy keys written before normalize_url handled scheme/www/param-order
(review 2026-07-05, issues: malformed &-joined URLs, http:// keys).
Idempotent; prints a summary. Run from the project root:
    python3 tools/oneoff/repair_index_urls.py
"""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
from tools.url_norm import normalize_url
from tools.update_reports_index import load_index, save_index


def main() -> int:
    index = load_index()
    changed = 0
    new_url_index: dict[str, str] = {}
    for key, entry in index.get("reports", {}).items():
        urls = entry.get("source_urls", []) or []
        normalized: list[str] = []
        for u in urls:
            n = normalize_url(u)
            if n and n not in normalized:
                normalized.append(n)
            if n != u:
                changed += 1
        entry["source_urls"] = normalized
        for n in normalized:
            new_url_index.setdefault(n, key)
    old_count = len(index.get("url_index", {}))
    index["url_index"] = new_url_index
    save_index(index)
    print(f"URLs rewritten: {changed}; url_index {old_count} -> {len(new_url_index)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

Run it once: `python3 tools/oneoff/repair_index_urls.py`. Then verify: `python3 tools/update_reports_index.py lookup-url --url "http://leg.colorado.gov/"` style checks — specifically `python3 -c "import json; ix=json.load(open('reports/index.json')); assert not [u for u in ix['url_index'] if u.startswith('http://')], 'http keys remain'"`.

- [ ] **Step 5: Commit**
```bash
git add tools/url_norm.py tests/test_url_norm.py tools/oneoff/repair_index_urls.py reports/index.json
git commit -m "tools: rewrite normalize_url with proper URL parsing; repair live index"
```

### Task 11: Unified bill key builder (federal + shared between tools)

**Files:**
- Modify: `tools/topic_keys.py`
- Modify: `tools/bill_processor.py` (delegate `bill_key`)
- Test: `tests/test_topic_keys.py`

**Interfaces:**
- Produces: `topic_keys.make_bill_key(state_abbrev: str, bill_type: str, bill_number: str, session_year: str) -> str` returning `"{STATE}-{TYPE}-{NUM}-{YEAR}"`; `topic_keys.session_to_year(session: str) -> str` (takes `"2026"` or `"2025-2026"` → `"2026"`, i.e. last 4-digit year found, empty string if none); `_state_bill_key` maps federal jurisdictions to `"US"`; `bill_processor.bill_key` delegates to `make_bill_key` + `session_to_year`.

- [ ] **Step 1: Failing tests** in `tests/test_topic_keys.py`:

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tools.topic_keys import topic_key, make_bill_key, session_to_year
from tools.bill_processor import bill_key


def test_federal_bill_gets_us_key():
    finding = {
        "title": "Congress passes HB 1234 on AI safety",
        "jurisdiction": "Federal",
        "development_type": "legislation",
        "date": "2026-03-01",
    }
    key, confidence, topic_type = topic_key(finding, {"regulator_aliases": {}, "agency_aliases": {}})
    assert topic_type == "federal_bill"
    assert key == "US-HB-1234-2026"
    assert confidence == "high"


def test_state_bill_key_unchanged():
    finding = {
        "title": "Virginia SB 338 advances",
        "jurisdiction": "Virginia",
        "development_type": "legislation",
        "date": "2026-02-01",
    }
    key, _, _ = topic_key(finding, {"regulator_aliases": {}, "agency_aliases": {}})
    assert key == "VA-SB-338-2026"


def test_session_to_year():
    assert session_to_year("2026") == "2026"
    assert session_to_year("2025-2026") == "2026"
    assert session_to_year("") == ""


def test_bill_processor_and_topic_keys_agree():
    assert bill_key("VA", "SB 338", "2026") == "VA-SB-338-2026"
    assert bill_key("US", "HB 1234", "2025-2026") == "US-HB-1234-2026"
    assert make_bill_key("VA", "S.B.", "338", "2026") == "VA-SB-338-2026"
```

Run: `python3 -m pytest tests/test_topic_keys.py -v` — Expected: FAIL (`make_bill_key` undefined; federal finding gets hash-fallback key).

- [ ] **Step 2: Implement in `tools/topic_keys.py`.** Add after `_hash8`:

```python
FEDERAL_JURISDICTIONS = {"federal", "us federal", "united states", "us", "u.s.", "usa"}


def make_bill_key(state_abbrev: str, bill_type: str, bill_number: str, session_year: str) -> str:
    """Single source of truth for bill topic keys, shared with bill_processor.

    The cross-index dedup design (bill_processor <-> scanner findings) hinges
    on both producing byte-identical keys.
    """
    bill_type = re.sub(r"[.\s]", "", (bill_type or "")).upper()
    bill_number = re.sub(r"[.\s]", "", (bill_number or "")).upper()
    return f"{state_abbrev.upper()}-{bill_type}-{bill_number}-{session_year}"


def session_to_year(session: str) -> str:
    """Extract the closing 4-digit year from a session string ('2025-2026' -> '2026')."""
    years = re.findall(r"\d{4}", session or "")
    return years[-1] if years else ""
```

In `_state_bill_key` (:132-156), replace the state-abbrev resolution block with:

```python
    state_abbrev = None
    low = jurisdiction.lower()
    if low in FEDERAL_JURISDICTIONS:
        state_abbrev = "US"
    elif len(jurisdiction) == 2 and jurisdiction.isupper():
        state_abbrev = jurisdiction
    elif low in US_STATE_ABBREV:
        state_abbrev = US_STATE_ABBREV[low]
```

and build the key via `key = make_bill_key(state_abbrev, bill_type, bill_number, session)`.

- [ ] **Step 3: Delegate in `tools/bill_processor.py`.** Replace `bill_key` (:53-62) with:

```python
def bill_key(state_abbrev: str, bill_identifier: str, session: str) -> str:
    """Generate a tracker key like OR-SB-1546-2026 (shared with topic_keys)."""
    if __package__ in (None, ""):
        sys.path.insert(0, str(PROJECT_ROOT))
        from tools.topic_keys import make_bill_key, session_to_year
    else:
        from .topic_keys import make_bill_key, session_to_year  # type: ignore
    parts = bill_identifier.strip().split()
    if len(parts) >= 2:
        bill_type, bill_number = parts[0], parts[1]
    else:
        bill_type, bill_number = bill_identifier.replace(" ", "-"), ""
    return make_bill_key(state_abbrev, bill_type, bill_number,
                         session_to_year(session) or session)
```

- [ ] **Step 4: Run tests:** `python3 -m pytest tests/test_topic_keys.py -v` — Expected: PASS. Also run `python3 -c "import json; t=json.load(open('bills/tracker.json')); from tools.bill_processor import bill_key; mismatches=[k for k,v in t['bills'].items() if bill_key(v['state_abbrev'], v['bill_identifier'], v.get('session','2026')) != k]; print('key mismatches:', len(mismatches))"` — must print `key mismatches: 0` (all current sessions are plain `"2026"`, so keys are unchanged).

- [ ] **Step 5: Commit**
```bash
git add tools/topic_keys.py tools/bill_processor.py tests/test_topic_keys.py
git commit -m "tools: unify bill key generation; federal bills key as US-*"
```

### Task 12: Fix bill versioning, status-history duplication, redirects, results dir

**Files:**
- Modify: `tools/bill_processor.py`

- [ ] **Step 1: Tracker-driven version numbering.** `download_bill` (:353-369) currently derives `version_num` from a directory glob (`len(existing_versions) // 2 + 1`) — broken (converter writes `.md`, not `.html`; v2 overwrites v1). Change the signature to accept the version number: `def download_bill(state_abbrev, state_name, bill_identifier, session, fpf_url, states_config, bill_directory, version_num: int = 1) -> dict:` and delete the glob lines (:361-362), using the parameter directly. Keep `version_label = "introduced" if version_num == 1 else f"version-{version_num}"`.

- [ ] **Step 2: Re-download on status change.** In `process_bills`, replace the download gate (:680) — currently `if entry["download_status"] in ("pending", "failed"):` — with:

```python
        status_changed = (not is_new) and bill.get("status") \
            and bill["status"] != prev_status
        needs_download = entry["download_status"] in ("pending", "failed") or status_changed
        if needs_download:
            version_num = len(entry.get("versions", [])) + 1
            dl_result = download_bill(
                state_abbrev, state, bill_id, session,
                bill.get("bill_text_url"),
                states_config, bill_dir,
                version_num=version_num,
            )
```

To make `prev_status` available, capture it in the existing-bill branch (:657-667): change `if bill.get("status") and bill["status"] != existing["current_status"]:` to first do `prev_status = existing["current_status"]` before updating, and set `prev_status = None` in the `is_new` branch.

- [ ] **Step 3: Deduplicate status_history.** Wrap the unconditional append (:669-676) in a guard:

```python
        new_hist = {
            "date": bill.get("last_action_date") or datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "status": bill.get("status", "introduced"),
            "detail": bill.get("status_detail", ""),
            "source_email_date": fpf_output.get("data", {}).get("email_dates", [""])[0] if fpf_output.get("data", {}).get("email_dates") else "",
            "source_run_id": run_id,
        }
        hist = tracker["bills"][key]["status_history"]
        last = hist[-1] if hist else {}
        if not (last.get("date") == new_hist["date"]
                and last.get("status") == new_hist["status"]
                and last.get("detail") == new_hist["detail"]):
            hist.append(new_hist)
```

- [ ] **Step 4: Relative redirect fix.** In `resolve_redirect` (:81-96), change the redirect branch to:

```python
            if e.code in (301, 302, 303, 307, 308) and e.headers.get("Location"):
                from urllib.parse import urljoin
                url = urljoin(url, e.headers["Location"])
```

- [ ] **Step 5: Results dir + misc.** In `process_bills` before the results write (:757), add `results_path.parent.mkdir(parents=True, exist_ok=True)`. In `try_state_config` (:323) fix the duplicate literal: `is_senate = bill_type.upper() in ("S", "SB", "SF", "SJR", "SR")`. In `_cross_index_bill_to_reports` (:539-546), hoist the `normalize_url` import out of the per-URL loop to the top of the function.

- [ ] **Step 6: Verify:** `python3 -m py_compile tools/bill_processor.py`, then a dry version-number check: `python3 -c "
import json
t = json.load(open('bills/tracker.json'))
e = next(iter(t['bills'].values()))
print('versions:', len(e.get('versions', [])), '-> next would be', len(e.get('versions', [])) + 1)"`.

- [ ] **Step 7: Commit**
```bash
git add tools/bill_processor.py
git commit -m "tools: tracker-driven bill versions, re-download on status change, dedupe history"
```

### Task 13: `diff_signal` pattern ordering fix + tests

**Files:**
- Modify: `tools/diff_signal.py`
- Test: `tests/test_diff_signal.py`

- [ ] **Step 1: Failing tests** in `tests/test_diff_signal.py`:

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tools.diff_signal import classify


def test_bill_progress_beats_penalty_mention():
    finding = {
        "title": "SB 123 passed the Senate",
        "summary": "The bill passed the Senate; violations carry civil penalties up to $7,500.",
    }
    result = classify(finding, {"current_status": "introduced"})
    assert result["diff_signal"] == "status_change"
    assert result["status_after"] == "passed-first-chamber"


def test_pure_enforcement_still_penalty():
    finding = {
        "title": "AG announces $2M fine against DataCo",
        "summary": "Civil penalties imposed for privacy violations.",
    }
    result = classify(finding, {"current_status": ""})
    assert result["diff_signal"] == "new_penalty"


def test_signed_beats_everything():
    finding = {"title": "HB 5 signed into law", "summary": "Includes penalty provisions."}
    result = classify(finding, {"current_status": "passed-second-chamber"})
    assert result["diff_signal"] == "signed"


def test_restated_status_is_noise():
    finding = {"title": "SB 9 was signed into law last month", "summary": ""}
    result = classify(finding, {"current_status": "signed"})
    assert result["diff_signal"] == "noise"
```

Run: `python3 -m pytest tests/test_diff_signal.py -v` — Expected: first test FAILS (`new_penalty` wins today).

- [ ] **Step 2: Reorder `PATTERNS`** in `tools/diff_signal.py` (:32-57): move the five bill-progress entries (`passed the house/senate/committee/chamber`, `passed both chambers`, `cleared committee`, `reported favorably`, `advanced from committee`) to ABOVE the penalty block (`penalt…`, `consent order`, `settlement`, `enforcement action`, `fine…`). Keep vetoed/signed/amendment first, and `died|failed|stalled` / `tabled` after the penalty block (unchanged relative order otherwise). Update the comment: `# Order matters — first match wins. Bill-progress verbs outrank penalty nouns because bill summaries routinely mention penalty provisions.`

- [ ] **Step 3: Run tests:** `python3 -m pytest tests/test_diff_signal.py -v` — Expected: PASS.

- [ ] **Step 4: Commit**
```bash
git add tools/diff_signal.py tests/test_diff_signal.py
git commit -m "tools: bill-progress patterns outrank penalty mentions in diff_signal"
```

### Task 14: Backfill safety guard + CLAUDE.md exclusion; index lock

**Files:**
- Modify: `tools/backfill_reports_index.py`
- Modify: `tools/update_reports_index.py`

- [ ] **Step 1: Fix the dead promote guard.** In `backfill_reports_index.py`, add a `--force` flag to the argparser (`parser.add_argument("--force", action="store_true", help="Promote even with low-confidence entries")` — locate the existing parser near the top of `main`). Replace lines 261-267 with:

```python
    if args.promote:
        if low_confidence and not args.force:
            print("\nRefusing to auto-promote with low-confidence entries present."
                  " Re-run with --force to override.")
            return 1
        os.replace(BACKFILL_PATH, LIVE_INDEX_PATH)
        print(f"\nPromoted to {LIVE_INDEX_PATH}")
```

(add `import os` at the top if missing; remove the `import shutil`).

- [ ] **Step 2: Exclude non-report markdown.** Change line 167 from `report_files = sorted(REPORTS_DIR.rglob("*.md"))` to:

```python
    report_files = sorted(
        p for p in REPORTS_DIR.rglob("*.md")
        if p.name not in ("CLAUDE.md", "README.md")
    )
```

- [ ] **Step 3: Advisory lock for index writers.** In `tools/update_reports_index.py`, add:

```python
import fcntl
from contextlib import contextmanager

LOCK_PATH = INDEX_PATH.with_suffix(".json.lock")


@contextmanager
def index_lock():
    """Advisory lock around load->mutate->save of reports/index.json.

    Atomic replace prevents corruption but not lost updates; the bot,
    pipeline stages, and bill_processor all read-modify-write this file.
    """
    LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LOCK_PATH, "w") as lf:
        fcntl.flock(lf, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(lf, fcntl.LOCK_UN)
```

Wrap the load→save pairs in `cmd_add` and `cmd_append_status` with `with index_lock():`. In `tools/bill_processor.py`'s cross-index block (:737-754), import and wrap the `load_index()`…`save_index(reports_index)` span in `with index_lock():` (import via the same `_load_cross_index_helpers` pattern — simplest: extend `_load_cross_index_helpers` to also return `index_lock`).

- [ ] **Step 4: Normalize membership test in `add_entry`.** In `update_reports_index.py:91`, the existing-entry check compares the normalized URL against possibly un-normalized stored values. After Task 10's index repair the stored values are normalized, so the current code is correct going forward — but make it robust: change the merge loop to:

```python
        existing["source_urls"] = [normalize_url(u) or u for u in existing["source_urls"]]
        for url in entry.get("source_urls", []):
            normalized = normalize_url(url)
            if normalized and normalized not in existing["source_urls"]:
                existing["source_urls"].append(normalized)
                index["url_index"][normalized] = key
```

- [ ] **Step 5: Verify:** `python3 -m py_compile tools/backfill_reports_index.py tools/update_reports_index.py tools/bill_processor.py` and `python3 tools/update_reports_index.py stats` (must still print stats).

- [ ] **Step 6: Commit**
```bash
git add tools/backfill_reports_index.py tools/update_reports_index.py tools/bill_processor.py
git commit -m "tools: fix backfill promote guard, exclude CLAUDE.md, add index write lock"
```

---

## Phase 4 — Test harness & validator round-trip

### Task 15: Validator round-trip check for agent-documented examples

**Files:**
- Create: `pipeline/scripts/check-schema-examples.sh`
- Create: `pipeline/schemas/examples/researcher-full.json`, `pipeline/schemas/examples/researcher-update.json`, `pipeline/schemas/examples/reviewer-output.json`, `pipeline/schemas/examples/fpf-scanner.json`

**Interfaces:**
- Produces: `bash pipeline/scripts/check-schema-examples.sh` exits 0 iff every example file under `pipeline/schemas/examples/` passes `validate-handoff.sh` for the stage encoded in its filename prefix. This is the CI-style check that would have caught review issues 1, 2, 9, 12 of the agent layer.

- [ ] **Step 1: Create the example files.** Each is a full envelope matching what the corresponding agent prompt documents. `researcher-update.json` = Task 1's `fixture-update.json`. `researcher-full.json` = Task 1's `fixture-full.json`. `reviewer-output.json` = an envelope with `stage: "reviewer"`, one verified normal entry and one `append_update` entry with `verdict: "auto_approved"` (shape from Task 3 Step 3). `fpf-scanner.json` = minimal envelope with `stage: "fpf-scanner"`, `data: {"bills": []}`.

- [ ] **Step 2: Create the check script:**

```bash
#!/bin/bash
set -euo pipefail
# Round-trip every documented example envelope through validate-handoff.sh.
# Filename convention: <stage>-<variant>.json -> stage is the part before the first '-'
# except 'fpf-scanner' which contains a dash; handle it explicitly.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXAMPLES_DIR="$SCRIPT_DIR/../schemas/examples"
FAIL=0
for f in "$EXAMPLES_DIR"/*.json; do
  base=$(basename "$f" .json)
  case "$base" in
    fpf-scanner*) stage="fpf-scanner" ;;
    *) stage="${base%%-*}" ;;
  esac
  if "$SCRIPT_DIR/validate-handoff.sh" "$stage" "$f" >/dev/null 2>&1; then
    echo "OK   $base ($stage)"
  else
    echo "FAIL $base ($stage)"
    FAIL=1
  fi
done
exit $FAIL
```

`chmod +x pipeline/scripts/check-schema-examples.sh`. Note: check how `validate-handoff.sh` maps stage→schema for `fpf-scanner` (it uses `${SCHEMA}.jq`; there is no `fpf-scanner.jq`, only `.schema.json` — per `validate-handoff.sh:58` a missing `.jq` skips stage-specific validation, which is acceptable; envelope validation still runs).

- [ ] **Step 3: Run it:** `bash pipeline/scripts/check-schema-examples.sh` — Expected: all OK, exit 0. If any FAIL, the schema or the example is wrong — fix the mismatch (that's the point of the check).

- [ ] **Step 4: Run the whole test suite:** `python3 -m pytest tests/ -v` — all green.

- [ ] **Step 5: Commit**
```bash
git add pipeline/scripts/check-schema-examples.sh pipeline/schemas/examples/
git commit -m "pipeline: schema example round-trip check catching prompt/validator drift"
```

---

## Phase 5 — Remaining Important/Minor fixes

### Task 16: Persist Discord approval state + restart-surviving buttons

**Files:**
- Modify: `discord_bot.py`

**Interfaces:**
- Produces: approvals persisted to `pipeline/runs/<run_id>/approval-state.json` on every click; `FindingView` buttons use deterministic `custom_id`s (`zwiad:<run_id>:<finding_id>:approve|reject`); a dynamic-item handler restores button function after bot restarts; `cmd_approve` reads the persisted file when in-memory state is empty.

- [ ] **Step 1: Persistence helpers:**

```python
def _approval_path(run_id: str) -> Path:
    return RUNS_DIR / run_id / "approval-state.json"


def _load_approval_state(run_id: str) -> dict[str, bool]:
    data = _read_run_json(_approval_path(run_id))
    return data.get("approvals", {}) if isinstance(data, dict) else {}


def _save_approval_state(run_id: str) -> None:
    state = approval_state.get(run_id, {})
    _atomic_write_json(_approval_path(run_id), {
        "run_id": run_id,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "approvals": state,
    })
```

- [ ] **Step 2: Wire clicks to disk.** In `FindingView.approve`/`.reject` (:804-818), after mutating `approval_state`, call `_save_approval_state(self.run_id)`. Give the buttons deterministic ids by constructing them in `__init__` instead of decorators:

```python
class FindingView(discord.ui.View):
    """Approve/Reject buttons for a single finding. custom_ids are deterministic
    so clicks still resolve after a bot restart (see on_interaction fallback)."""

    def __init__(self, run_id: str, finding_id: str):
        super().__init__(timeout=None)
        self.run_id = run_id
        self.finding_id = finding_id
        approve = discord.ui.Button(
            label="Approve", style=discord.ButtonStyle.green,
            custom_id=f"zwiad:{run_id}:{finding_id}:approve")
        reject = discord.ui.Button(
            label="Reject", style=discord.ButtonStyle.red,
            custom_id=f"zwiad:{run_id}:{finding_id}:reject")
        approve.callback = self._make_cb(True, approve, reject)
        reject.callback = self._make_cb(False, reject, approve)
        self.add_item(approve)
        self.add_item(reject)

    def _make_cb(self, approved: bool, this_btn, other_btn):
        async def cb(interaction: discord.Interaction):
            approval_state.setdefault(self.run_id, {})[self.finding_id] = approved
            _save_approval_state(self.run_id)
            this_btn.label = "Approved" if approved else "Rejected"
            this_btn.disabled = True
            other_btn.disabled = True
            await interaction.response.edit_message(view=self)
        return cb
```

- [ ] **Step 3: Restart survival.** Add an `on_interaction` fallback in `ZwiadBot` (component interactions whose view is gone after restart):

```python
    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.type != discord.InteractionType.component:
            return
        cid = (interaction.data or {}).get("custom_id", "")
        if not cid.startswith("zwiad:") or interaction.response.is_done():
            return
        try:
            _, run_id, finding_id, action = cid.split(":", 3)
        except ValueError:
            return
        approved = action == "approve"
        approval_state.setdefault(run_id, {})[finding_id] = approved
        _save_approval_state(run_id)
        await interaction.response.send_message(
            f"`{finding_id}` {'approved' if approved else 'rejected'} (recorded after restart).",
            ephemeral=True,
        )
```

(Note: `discord.Client` dispatches `on_interaction` before view callbacks only for unknown views; when the live view exists, its callback answers first and `interaction.response.is_done()` guards double-handling. Verify against discord.py 2.x behavior — if the live view's callback runs after `on_interaction`, invert the guard by checking `self._connection._view_store.is_message_tracked(interaction.message.id)` or simply accept the ephemeral duplicate.)

- [ ] **Step 4: Read persisted state in `cmd_approve`** (:1226-1227): change to:

```python
        state = approval_state.get(run_id) or _load_approval_state(run_id)
```

- [ ] **Step 5: Verify:** `python3 -m py_compile discord_bot.py`.

- [ ] **Step 6: Commit**
```bash
git add discord_bot.py
git commit -m "bot: persist approvals to run dir; buttons survive restarts via custom_id fallback"
```

### Task 17: Cost caps, no-body email handling, optional owner gate

**Files:**
- Modify: `discord_bot.py`

- [ ] **Step 1: Budget caps.** In `_run_research_phase` (:1300-1307) and `_run_review_phase` (:1391-1398), add to the `cmd` list after the `--max-turns` pair: `"--max-budget-usd", f"{max(5.0, remaining * 3.0):.2f}"` for research (uses the `remaining` count already computed; the CLAUDE.md per-finding cap is $3.00) and `"--max-budget-usd", f"{max(5.0, len(researcher_files) * 2.0):.2f}"` for review. First verify the flag exists: run `claude -p --help 2>&1 | grep -i budget`; if the flag is absent in the installed CLI version, instead add a post-hoc overrun alert after each phase: `if actual_cost > estimated_cost * 2: await channel.send(f"⚠️ {stage} cost ${actual_cost:.2f} — more than 2x the estimate.")` and note the flag's absence in a code comment.

- [ ] **Step 2: No-body emails.** In `fetch_new_emails`, the `if html_body:` block (:174-197) silently drops bodyless emails while still marking them read (:199). Add an `else` branch before `mail.store`:

```python
                else:
                    logger.warning("Email has no extractable body; recording as skipped: %r",
                                   msg.get("Subject", ""))
                    processed_data["processed"][mid] = {
                        "first_seen_run": run_id,
                        "subject": msg.get("Subject", ""),
                        "from": msg.get("From", ""),
                        "processed_at": datetime.now(timezone.utc).isoformat(),
                        "skipped": "no-body",
                    }
                    processed_dirty = True
```

- [ ] **Step 3: Optional owner gate.** After the env loading (:29-33), add `OWNER_ID = int(os.environ.get("DISCORD_OWNER_ID", "0"))`. Add a helper:

```python
def _authorized(interaction: discord.Interaction) -> bool:
    """If DISCORD_OWNER_ID is set, only that user may run cost-incurring commands."""
    return not OWNER_ID or interaction.user.id == OWNER_ID
```

At the top of `cmd_scan`, `cmd_research`, `cmd_review`, `cmd_approve`:

```python
    if not _authorized(interaction):
        await interaction.response.send_message("Not authorized.", ephemeral=True)
        return
```

(Unset env var = current permissive behavior; no .env change required.)

- [ ] **Step 4: Verify:** `python3 -m py_compile discord_bot.py`.
- [ ] **Step 5: Commit**
```bash
git add discord_bot.py
git commit -m "bot: research/review budget caps, no-body email audit trail, optional owner gate"
```

### Task 18: Agent-markdown hygiene sweep

**Files:**
- Modify: `.claude/agents/orchestrator.md`, `.claude/agents/researcher.md`, `.claude/agents/scanner-archive.md`
- Modify: `reports/privacy/CLAUDE.md`, `reports/cybersecurity/CLAUDE.md`, `reports/ai-law/CLAUDE.md`

- [ ] **Step 1: Orchestrator mode/step renumbering.** In `orchestrator.md`: reorder sections to Mode 1, Mode 2, Mode 3 (FPF), Mode 4; renumber Mode 4's internal steps starting at "Step 1: Mode 4 Gate" and fix every cross-reference ("Steps 4–7 below" → "the steps below"; the `/review` prompt in `discord_bot.py:1385-1389` references "Step 4/5/6/7" — update that prompt string in the same commit to name the steps by title instead: "run reviewer, check escalations, run categorizer if no escalations, write pipeline-complete.marker"). Fix the Mode 2 progress-log template (~:274-293) so it stops listing "Running reviewer… Running categorizer… Pipeline complete" — Mode 2's template ends at "Research complete".
- [ ] **Step 2: researcher.md example fix.** Line ~25: change the frontmatter example `topic_type` values `federal_rule | enforcement_action` to the real vocabulary `state_bill | federal_bill | enforcement | rulemaking | guidance | other`.
- [ ] **Step 3: Scanner ID convention.** In `scanner-archive.md` near line 48, extend the ID note: "Archive digests use the digest date in the SCAN id (SCAN-YYYYMMDD from the email date), unlike live scans which use the scan date. Dedup is topic-key based, so the difference is informational only."
- [ ] **Step 4: reports/*/CLAUDE.md.** In each of the three files: delete the stale hand-maintained "Reports Index (pipeline run …)" table; reconcile the subcategory list with `pipeline/config/categories.json` AND the directories that exist on disk (`ls reports/<topic>/`) — list every real directory; add one line: "This file lists directory structure only. The authoritative report index is reports/index.json; do not maintain report tables here."
- [ ] **Step 5: Verify:** `grep -n "Steps 4" .claude/agents/orchestrator.md` returns nothing; `grep -n "federal_rule" .claude/agents/researcher.md` returns nothing.
- [ ] **Step 6: Commit**
```bash
git add .claude/agents/orchestrator.md .claude/agents/researcher.md .claude/agents/scanner-archive.md reports/privacy/CLAUDE.md reports/cybersecurity/CLAUDE.md reports/ai-law/CLAUDE.md discord_bot.py
git commit -m "agents: renumber orchestrator modes, fix stale examples and reports CLAUDE.md tables"
```

### Task 19: Pending-subcategory approval script + categories reconciliation

**Files:**
- Create: `tools/approve_pending.py`
- Modify: `pipeline/config/categories.json`

**Interfaces:**
- Produces: `python3 tools/approve_pending.py list` (show pending items), `python3 tools/approve_pending.py approve <finding_id> [--subcategory NAME]` (adds subcategory to categories.json if new, moves the report from the category root into the subcategory dir, updates reports/index.json entry's `subcategory` + `report_path`, deletes the two pending files), `python3 tools/approve_pending.py reject <finding_id>` (deletes the pending files, leaves the report at the category root).

- [ ] **Step 1: Inspect the pending JSON shape first**: `cat pipeline/pending/SCAN-20260628-025-pending.json` — expected fields include `finding_id`, `proposed_subcategory`, `category`/`topic`, `report_path`. Write the script against the actual fields found.

- [ ] **Step 2: Implement `tools/approve_pending.py`:**

```python
#!/usr/bin/env python3
"""Approve or reject pending-subcategory proposals from the categorizer.

The categorizer routes reports whose subcategory is not in
pipeline/config/categories.json to pipeline/pending/<finding_id>-pending.{md,json}
for human confirmation. This is the (previously missing) consumer of that queue.

Usage:
    python3 tools/approve_pending.py list
    python3 tools/approve_pending.py approve SCAN-20260628-025 [--subcategory other-name]
    python3 tools/approve_pending.py reject SCAN-20260628-025
"""
import argparse
import json
import shutil
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PENDING_DIR = PROJECT_ROOT / "pipeline" / "pending"
CATEGORIES_PATH = PROJECT_ROOT / "pipeline" / "config" / "categories.json"

sys.path.insert(0, str(PROJECT_ROOT))
from tools.update_reports_index import load_index, save_index, index_lock  # noqa: E402


def _pending_items() -> list[dict]:
    items = []
    for jf in sorted(PENDING_DIR.glob("*-pending.json")):
        try:
            data = json.loads(jf.read_text())
        except json.JSONDecodeError:
            print(f"WARN: unreadable {jf.name}", file=sys.stderr)
            continue
        data["_json_path"] = str(jf)
        items.append(data)
    return items


def cmd_list(args) -> int:
    items = _pending_items()
    if not items:
        print("No pending subcategory proposals.")
        return 0
    for it in items:
        print(f"{it.get('finding_id','?'):28s} {it.get('category','?'):15s} "
              f"-> {it.get('proposed_subcategory','?'):25s} {it.get('report_path','')}")
    print(f"\n{len(items)} pending. approve/reject with tools/approve_pending.py")
    return 0


def _find(finding_id: str) -> dict | None:
    for it in _pending_items():
        if it.get("finding_id") == finding_id:
            return it
    return None


def cmd_approve(args) -> int:
    it = _find(args.finding_id)
    if not it:
        print(f"ERROR: no pending item for {args.finding_id}", file=sys.stderr)
        return 2
    category = it["category"]
    sub = args.subcategory or it["proposed_subcategory"]
    report_path = PROJECT_ROOT / it["report_path"]

    cats = json.loads(CATEGORIES_PATH.read_text())
    subs = cats.setdefault("categories", {}).setdefault(category, {}).setdefault("subcategories", [])
    if sub not in subs:
        subs.append(sub)
        subs.sort()
        CATEGORIES_PATH.write_text(json.dumps(cats, indent=2) + "\n")
        print(f"Added subcategory {category}/{sub} to categories.json")

    dest_dir = PROJECT_ROOT / "reports" / category / sub
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / report_path.name
    if report_path.exists() and report_path.resolve() != dest.resolve():
        shutil.move(str(report_path), str(dest))
        print(f"Moved {report_path.name} -> {dest.relative_to(PROJECT_ROOT)}")

    with index_lock():
        index = load_index()
        for key, entry in index.get("reports", {}).items():
            if args.finding_id in (entry.get("finding_ids") or []):
                entry["subcategory"] = sub
                entry["report_path"] = str(dest.relative_to(PROJECT_ROOT))
        save_index(index)

    _cleanup(it)
    print(f"Approved {args.finding_id} -> {category}/{sub}")
    return 0


def cmd_reject(args) -> int:
    it = _find(args.finding_id)
    if not it:
        print(f"ERROR: no pending item for {args.finding_id}", file=sys.stderr)
        return 2
    _cleanup(it)
    print(f"Rejected {args.finding_id}; report stays at {it.get('report_path','')}")
    return 0


def _cleanup(it: dict) -> None:
    jf = Path(it["_json_path"])
    md = jf.with_name(jf.name.replace("-pending.json", "-pending.md"))
    for p in (jf, md):
        if p.exists():
            p.unlink()


def main() -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list").set_defaults(func=cmd_list)
    ap = sub.add_parser("approve")
    ap.add_argument("finding_id")
    ap.add_argument("--subcategory")
    ap.set_defaults(func=cmd_approve)
    rj = sub.add_parser("reject")
    rj.add_argument("finding_id")
    rj.set_defaults(func=cmd_reject)
    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
```

Adjust field names (`category` vs `topic`, `proposed_subcategory` vs `subcategory`) to match the actual pending-JSON shape found in Step 1.

- [ ] **Step 3: Reconcile `categories.json` with disk.** For each directory under `reports/{privacy,cybersecurity,ai-law}/` that is not in categories.json (review found: `ai-law/employment-ai`, `privacy/litigation`, `cybersecurity/ai-threat-response`, plus `state/`/`california/` dirs), add it to the registry (they exist and contain filed reports; retroactively legitimizing beats orphaning). Verify with: `python3 - <<'EOF'
import json
from pathlib import Path
cats = json.load(open('pipeline/config/categories.json'))
for topic in ('privacy', 'cybersecurity', 'ai-law'):
    disk = {p.name for p in Path(f'reports/{topic}').iterdir() if p.is_dir()}
    reg = set(cats['categories'].get(topic, {}).get('subcategories', []))
    print(topic, 'on disk but unregistered:', sorted(disk - reg))
EOF` — after the fix, all three lines print `[]`. (Adapt key names to the real categories.json structure.)

- [ ] **Step 4: Run `python3 tools/approve_pending.py list`** — must print the ~16 pending findings.

- [ ] **Step 5: Commit**
```bash
git add tools/approve_pending.py pipeline/config/categories.json
git commit -m "tools: approve_pending consumer for the pending-subcategory queue"
```

### Task 20: Tools minor batch

**Files:**
- Modify: `tools/process_fpf_chronological.py`, `tools/report_updater.py`, `tools/fetch_fpf_emails.py`
- Move: `tools/add_2024_index_entries.py` → `tools/oneoff/add_2024_index_entries.py`, `tools/process_fpf_chronological.py` stays (it's parameterizable) but note below.

- [ ] **Step 1: `process_fpf_chronological.py` stale-output fix** (:132-145): before the `subprocess.run(cmd, ...)` call, add `output_path = RUNS_DIR / run_id / "fpf-scanner-output.json"` and `output_path.unlink(missing_ok=True)`; after the run, check `if result.returncode != 0: print(f"  Scanner: FAILED — exit {result.returncode}"); return False` BEFORE the `output_path.exists()` check (keep that check as the second gate).
- [ ] **Step 2: `report_updater.py` idempotency + YAML escaping.** In the `append` flow, before writing, check whether the finding_id already appears: read the file, and if `re.search(rf"finding_id: \"?{re.escape(finding_id)}\"?", content)` or the finding_id appears in an existing `status_history` line, print `"SKIP: {finding_id} already applied to {path}"` and exit 0. In the flow-entry builder (:107-111), escape quotes: `f'{k}: "{str(v).replace(chr(34), chr(39))}"'` (replace double quotes with single quotes inside values — YAML-safe for this simple flow style).
- [ ] **Step 3: `fetch_fpf_emails.py` docstring** (:4): change `--output-dir DIR` in the docstring to describe the actual positional argument.
- [ ] **Step 4: Move one-off script:** `mkdir -p tools/oneoff && git mv tools/add_2024_index_entries.py tools/oneoff/`. Fix its internal `PROJECT_ROOT` if it derives from `__file__` (one more `.parent`).
- [ ] **Step 5: Verify:** `python3 -m py_compile tools/process_fpf_chronological.py tools/report_updater.py tools/fetch_fpf_emails.py tools/oneoff/add_2024_index_entries.py` and run the full suite: `python3 -m pytest tests/ -v`.
- [ ] **Step 6: Commit**
```bash
git add -A tools/oneoff/ tools/process_fpf_chronological.py tools/report_updater.py tools/fetch_fpf_emails.py
git commit -m "tools: stale-output guard, idempotent report updates, one-off script quarantine"
```

### Task 21: Final verification sweep

- [ ] **Step 1:** `python3 -m pytest tests/ -v` — all pass.
- [ ] **Step 2:** `python3 -m py_compile discord_bot.py run_pipeline.py tools/*.py tools/oneoff/*.py` — clean.
- [ ] **Step 3:** `bash -n pipeline/scripts/*.sh` — clean.
- [ ] **Step 4:** `bash pipeline/scripts/check-schema-examples.sh` — all OK.
- [ ] **Step 5:** `python3 tools/update_reports_index.py stats` — sane counts (≈662 reports).
- [ ] **Step 6:** Report to the user: what was fixed, the model-downgrade decision taken (kept sonnet — reversible), and the two behavior notes (failed scans no longer become `latest_run_id`; federal bill keys now `US-*` — only affects future findings, no existing keys changed).
