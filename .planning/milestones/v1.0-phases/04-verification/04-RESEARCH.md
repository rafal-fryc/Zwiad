# Phase 4: Verification - Research

**Researched:** 2026-04-07
**Domain:** Reviewer agent implementation, iteration protocol, human escalation
**Confidence:** HIGH

## Summary

Phase 4 implements the reviewer agent that independently fact-checks researcher-produced reports, manages an iterative dispute resolution protocol (up to 3 rounds), and escalates unresolved disagreements to human review. The core deliverables are: (1) a fully populated reviewer agent system prompt in `.claude/agents/reviewer.md`, (2) a `run-reviewer.sh` orchestration script that manages the review-iterate-escalate loop, (3) JSON feedback/revision schemas for inter-round communication, and (4) an escalation markdown generator and resume script.

The project's existing patterns provide a strong foundation. The envelope schema, jq-based validation, APPROVED marker pattern, and bash orchestration scripts from Phases 1-3 directly translate to this phase. The reviewer agent stub already exists with the correct model (opus) and needs its tools expanded (add WebSearch) and system prompt filled in. The reviewer output schema already defines the reviews array with status enums, iteration counts, and issues structure.

**Primary recommendation:** Build the iteration loop in bash (matching `run-researcher.sh` style), use the reviewer agent for claim extraction and verification, and keep all state in versioned JSON files per round. The reviewer agent prompt is the most critical piece -- it must be prescriptive about claim identification, source re-fetching, and independent verification.

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions
- **D-01:** Reviewer uses a two-pronged approach: re-fetch all cited source URLs via WebFetch to check claims match source content, PLUS independent WebSearch for key facts to catch missing context or uncited information.
- **D-02:** Reviewer tools must be updated from Read+WebFetch to Read+WebFetch+WebSearch to enable independent fact-checking and legislative status lookups.
- **D-03:** Legal accuracy verification covers: statute citation correctness, effective dates, jurisdiction attribution, AND current legislative status (enacted, pending, vetoed, amended).
- **D-04:** When a cited source URL is inaccessible (down, paywalled, etc.), the claim is flagged as "unverifiable -- source unavailable" in the review output. The review continues; the whole review does not fail.
- **D-05:** Reviewer communicates issues via structured JSON feedback files. Each issue includes: claim text, issue description, severity (critical/major/minor), and suggested fix. Fits existing schema patterns.
- **D-06:** A round resolves (iteration stops) when the reviewer finds zero critical or major issues. Minor issues are noted in the final report but do not trigger another round.
- **D-07:** Researcher can push back on reviewer findings by marking an issue as "disputed" with evidence/justification. Reviewer re-evaluates the dispute in the next round.
- **D-08:** Iteration state tracked via versioned files per round in the pipeline run directory: `reviewer-feedback-r{N}.json`, `researcher-revision-r{N}.json`. Full audit trail preserved.
- **D-09:** When 3 rounds are exhausted without resolution, the pipeline generates a markdown escalation file showing: the current report, each unresolved dispute (reviewer's concern vs researcher's justification), and round-by-round history.
- **D-10:** Human resolves escalation by editing the report directly, then adding an `## APPROVED` marker (same pattern as scanner approval gate from Phase 2). Pipeline resumes with the edited report.
- **D-11:** Reports that pass verification (reviewer status = "verified", zero critical/major issues) auto-pass to the categorizer without human sign-off. Only escalated reports require human intervention.

### Claude's Discretion
- Reviewer system prompt structure and claim extraction logic
- Exact JSON feedback file schema (fields beyond the required claim/issue/severity/suggested-fix)
- Escalation markdown file formatting and layout
- How reviewer identifies and extracts individual claims from report sections
- WebSearch query design for independent fact verification
- How minor issues are annotated in the final report

### Deferred Ideas (OUT OF SCOPE)
None -- discussion stayed within phase scope
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| VERF-01 | Reviewer agent independently checks that all claims are supported by cited sources (no hallucinations) | D-01 two-pronged approach (re-fetch sources + independent WebSearch), reviewer agent prompt with claim extraction logic, WebFetch for source re-verification |
| VERF-02 | Reviewer agent verifies legal accuracy (correct statute citations, effective dates, jurisdiction attribution) | D-03 legal accuracy scope, reviewer prompt sections on statute verification, WebSearch for legislative status lookups |
| VERF-03 | Researcher and reviewer iterate up to 3 rounds; unresolved disagreements escalate to human review | D-05 through D-10 iteration protocol, versioned feedback files, escalation markdown generator, APPROVED marker resume pattern |
| VERF-04 | Reviewer annotates each claim with verification status in the final report | Per-claim annotation format in reviewer prompt, annotation insertion into report markdown, final verified report output |
</phase_requirements>

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| Claude Code CLI (`claude`) | 2.1.92+ | Invoke reviewer agent via `claude -p --agent reviewer` | Project constraint: all agents run as CLI subprocesses [VERIFIED: CLAUDE.md] |
| bash | System | Orchestration script for review-iterate-escalate loop | Matches existing `run-researcher.sh` pattern [VERIFIED: codebase] |
| jq | System | JSON manipulation for feedback files, schema validation, iteration state | Already used throughout pipeline scripts [VERIFIED: codebase] |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| `validate-handoff.sh` | Existing | Schema validation for reviewer output | After each reviewer invocation to validate output [VERIFIED: codebase] |

No new dependencies are needed. This phase uses only existing tools and patterns. [VERIFIED: codebase audit]

## Architecture Patterns

### Recommended Project Structure

New files this phase creates:

```
.claude/agents/
  reviewer.md              # UPDATE: expand tools + full system prompt
pipeline/scripts/
  run-reviewer.sh          # NEW: review orchestration with iteration loop
  generate-escalation.sh   # NEW: generate escalation markdown from round history
  approve-escalation.sh    # NEW: parse APPROVED escalation, resume pipeline
pipeline/schemas/
  reviewer-feedback.schema.json  # NEW: per-round feedback schema
  reviewer-feedback.jq           # NEW: jq validation for feedback
pipeline/runs/<run-id>/
  reviewer-feedback-r1.json      # Generated per round (D-08)
  researcher-revision-r1.json   # Generated per round (D-08)
  reviewer-escalation.md        # Generated on escalation (D-09)
  reviewer-output.json          # Final reviewer envelope
tests/
  test-reviewer-validation.sh   # NEW: validation tests
  fixtures/
    sample-reviewer-feedback.json
    sample-reviewer-output.json
    sample-escalation.md
```

### Pattern 1: Iteration Loop in Bash

**What:** The `run-reviewer.sh` script manages the review-iterate-escalate cycle entirely in bash, invoking the reviewer and researcher agents as subprocesses per round. [ASSUMED]

**When to use:** Every reviewer invocation for every report.

**Design:**

```bash
# Pseudocode for run-reviewer.sh iteration loop
for FINDING in researcher_outputs:
  ROUND=1
  while ROUND <= 3:
    # Invoke reviewer agent
    claude -p --agent reviewer \
      --output-format json \
      --max-turns 25 \
      "Review report at $REPORT_PATH. Round $ROUND. ..."
    
    # Check feedback: any critical/major issues?
    CRITICAL_MAJOR=$(jq '[.issues[] | select(.severity == "critical" or .severity == "major")] | length' feedback.json)
    
    if CRITICAL_MAJOR == 0:
      # D-06: resolved -- minor issues noted but no more rounds
      mark_verified
      break
    
    if ROUND == 3:
      # D-09: escalate
      generate_escalation_markdown
      mark_needs_human_review
      break
    
    # Invoke researcher agent for revision
    claude -p --agent researcher \
      --output-format json \
      --max-turns 20 \
      "Revise report based on reviewer feedback at $FEEDBACK_PATH. Round $ROUND. ..."
    
    ROUND=$((ROUND + 1))
  done
done
```

### Pattern 2: Reviewer Agent Two-Pronged Verification (D-01)

**What:** The reviewer agent system prompt instructs it to perform two distinct verification passes per report. [VERIFIED: D-01 from CONTEXT.md]

**Pass 1 -- Source Re-fetch:** For each cited source URL in the report, use WebFetch to retrieve the page and check that the claim attributed to that source actually appears in (or is supported by) the source content.

**Pass 2 -- Independent Verification:** For key facts (statute numbers, effective dates, enforcement actions, jurisdiction claims), use WebSearch to independently verify them against authoritative sources.

### Pattern 3: Structured Feedback JSON (D-05, D-07)

**What:** Each review round produces a feedback JSON file with per-issue structure. [VERIFIED: D-05, D-07 from CONTEXT.md]

**Schema design (Claude's discretion area):**

```json
{
  "finding_id": "SCAN-20260406-001",
  "report_path": "reports/privacy/federal-apra-2026-04-06.md",
  "round": 1,
  "claims_checked": 12,
  "issues": [
    {
      "claim": "The bill was introduced on April 4, 2026",
      "section": "Key Facts",
      "source_url": "https://www.congress.gov/...",
      "issue": "Source page shows introduction date as April 7, not April 4",
      "severity": "critical",
      "suggested_fix": "Update date to April 7, 2026",
      "status": "open"
    }
  ],
  "resolution_status": "issues-found"
}
```

The `status` field on each issue supports the dispute flow (D-07):
- `"open"` -- new issue from reviewer
- `"fixed"` -- researcher addressed it in revision
- `"disputed"` -- researcher disagrees, provides justification
- `"upheld"` -- reviewer re-evaluated dispute, maintains position
- `"withdrawn"` -- reviewer accepts researcher's dispute justification

### Pattern 4: Researcher Revision Response (D-07)

**What:** When the researcher revises a report based on feedback, it produces a revision JSON documenting what was changed. [ASSUMED]

```json
{
  "finding_id": "SCAN-20260406-001",
  "round": 1,
  "report_path": "reports/privacy/federal-apra-2026-04-06.md",
  "responses": [
    {
      "issue_index": 0,
      "action": "fixed",
      "explanation": "Updated date to April 7 per congress.gov"
    },
    {
      "issue_index": 1,
      "action": "disputed",
      "evidence": "The FTC press release at [url] confirms enforcement action",
      "justification": "Source confirms the claim; reviewer may have checked a different page"
    }
  ]
}
```

### Pattern 5: Escalation Markdown (D-09, D-10)

**What:** When 3 rounds exhaust without resolution, a markdown file is generated for human review. Follows the APPROVED marker pattern from Phase 2. [VERIFIED: D-09, D-10 from CONTEXT.md, approve-findings.sh pattern]

```markdown
# Verification Escalation

**Pipeline Run:** 2026-04-06T14-30-00
**Finding:** SCAN-20260406-001
**Report:** reports/privacy/federal-apra-2026-04-06.md
**Rounds Completed:** 3

## Unresolved Issues

### Issue 1: [severity] -- [claim summary]

**Reviewer's Concern:** [description]
**Researcher's Response:** [justification]

**Round History:**
- Round 1: Raised by reviewer
- Round 2: Disputed by researcher -- [evidence]
- Round 3: Upheld by reviewer -- [reasoning]

## Current Report

[Full report content embedded or linked]

## Instructions

Edit the report file directly to resolve issues.
When complete, add the marker below:

<!-- ## APPROVED -->
```

### Pattern 6: Per-Claim Verification Annotation (VERF-04)

**What:** The final verified report includes inline annotations showing verification status per claim. [VERIFIED: VERF-04 from REQUIREMENTS.md]

**Recommended annotation format (Claude's discretion area):**

The reviewer agent, after completing verification (or after human approval), inserts verification status markers into the report. Two options:

**Option A -- Inline markers (recommended):** Add verification tags after confidence tags in section headings and as inline markers on individual claims.

```markdown
## Key Facts [HIGH confidence] [VERIFIED]

- The bill was introduced on April 7, 2026 [source](url) <!-- verified -->
- The private right of action allows $100-$750 per incident [source](url) <!-- verified -->
- The bill preempts state privacy laws [source](url) <!-- disputed: scope unclear -->
```

**Option B -- Verification summary section:** Add a `## Verification Status` section at the end listing each checked claim and its status.

Recommendation: Use Option A (inline markers as HTML comments) because it keeps verification context next to the claim it applies to, is non-disruptive to report readability, and is parseable by downstream tools if needed.

### Anti-Patterns to Avoid

- **Running all rounds in one agent invocation:** Each round must be a separate `claude -p` call so the orchestration script can inspect results and make decisions. Do not try to have the reviewer self-loop. [ASSUMED]
- **Reviewer modifying the report directly:** The reviewer only produces feedback JSON. The researcher makes changes. This separation ensures independent verification. [VERIFIED: D-05, D-07]
- **Failing the entire review on one inaccessible source:** Per D-04, mark as "unverifiable" and continue. [VERIFIED: D-04]

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| JSON schema validation | Custom validation logic | Existing `validate-handoff.sh` + jq filters | Already proven pattern, consistent with pipeline [VERIFIED: codebase] |
| Human approval gate | Custom approval flow | Existing APPROVED marker pattern from Phase 2 | Reuse `approve-findings.sh` logic for escalation [VERIFIED: codebase] |
| Pipeline envelope format | Custom JSON structure | Existing `envelope.schema.json` wrapper | All stages use the same envelope [VERIFIED: codebase] |
| Iteration file naming | Ad hoc naming | `reviewer-feedback-r{N}.json` / `researcher-revision-r{N}.json` per D-08 | Locked decision [VERIFIED: D-08] |

## Common Pitfalls

### Pitfall 1: Reviewer Agent Context Window Exhaustion

**What goes wrong:** The reviewer agent is invoked with opus model and given a full report to analyze plus multiple WebFetch results. Long reports with many sources can exhaust the context window or hit max-turns before completing verification.
**Why it happens:** Each WebFetch call returns substantial content. A research-memo with 10 sources could generate enormous context.
**How to avoid:** Set `--max-turns 25` for the reviewer (enough for claim extraction + source re-fetching + independent search). In the system prompt, instruct the reviewer to prioritize: check critical/legal claims first, then work through remaining claims. If turns run low, output partial results. [ASSUMED]
**Warning signs:** Reviewer output has very few `claims_checked` relative to report size.

### Pitfall 2: WebFetch Failures Breaking Verification Flow

**What goes wrong:** Source URLs from the report are stale, paywalled, or return errors. The reviewer gets stuck trying to re-fetch inaccessible sources.
**Why it happens:** Reports cite URLs that worked at research time but may be unavailable hours/days later.
**How to avoid:** D-04 already addresses this: flag as "unverifiable -- source unavailable" and continue. The reviewer prompt must explicitly instruct: do not retry failed fetches more than once, do not halt review. [VERIFIED: D-04]
**Warning signs:** High proportion of "unverifiable" claims in output.

### Pitfall 3: Infinite Dispute Loops

**What goes wrong:** Researcher disputes every finding, reviewer upholds every dispute, creating unproductive iteration that always hits the 3-round cap.
**Why it happens:** Neither agent has clear criteria for when a dispute is valid vs. when to accept feedback.
**How to avoid:** The reviewer prompt should specify dispute evaluation criteria: a dispute is valid if the researcher provides a specific URL or quote that directly supports the contested claim. The researcher prompt (for revision) should specify: disputes must include a verifiable source or direct quote. [ASSUMED]
**Warning signs:** Every round has the same number of issues with all status "disputed" then "upheld."

### Pitfall 4: Researcher Not Receiving Feedback Context

**What goes wrong:** When invoking the researcher for revision, the prompt does not clearly point to the feedback file, or the researcher agent cannot read the feedback format.
**Why it happens:** The researcher agent's system prompt is designed for initial report writing, not revision.
**How to avoid:** The `run-reviewer.sh` script must provide a clear prompt to the researcher that includes: (1) path to the feedback file, (2) instruction to read it and address each issue, (3) path to write the revision response JSON. The researcher agent already has Read+Write tools. [ASSUMED]
**Warning signs:** Researcher produces a new report instead of revising the existing one.

### Pitfall 5: Escalation File Not Being Self-Contained

**What goes wrong:** The escalation markdown references files or round data that the human cannot easily access or understand.
**Why it happens:** The escalation generator script only links to JSON files instead of embedding the relevant content.
**How to avoid:** The escalation markdown must be fully self-contained: embed the current report content (or clear path to it), inline the dispute text from each round, and include clear instructions. [VERIFIED: D-09]
**Warning signs:** Human needs to read 6+ JSON files to understand the dispute.

## Code Examples

### Example 1: Reviewer Agent Invocation

```bash
# Source: run-researcher.sh pattern from Phase 3 [VERIFIED: codebase]
claude -p --agent reviewer \
  --output-format json \
  --max-turns 25 \
  "Review the report at $REPORT_PATH for finding $FINDING_ID. \
   Pipeline run: $RUN_ID. Round: $ROUND. \
   Write your feedback to: $RUN_DIR/reviewer-feedback-r${ROUND}.json. \
   $([ "$ROUND" -gt 1 ] && echo "Previous revision response at: $RUN_DIR/researcher-revision-r$((ROUND-1)).json")"
```

### Example 2: Check Round Resolution (D-06)

```bash
# Source: D-06 decision -- zero critical/major means resolved [VERIFIED: CONTEXT.md]
CRITICAL_MAJOR=$(jq '[.issues[] | select(.severity == "critical" or .severity == "major")] | length' \
  "$RUN_DIR/reviewer-feedback-r${ROUND}.json")

if [ "$CRITICAL_MAJOR" -eq 0 ]; then
  echo "Round $ROUND: Resolved (minor issues only)"
  # Proceed to finalize
else
  echo "Round $ROUND: $CRITICAL_MAJOR critical/major issues remain"
  # Proceed to researcher revision or escalation
fi
```

### Example 3: Build Reviewer Output Envelope

```bash
# Source: envelope.schema.json pattern [VERIFIED: codebase]
jq -n \
  --arg run_id "$RUN_ID" \
  --arg status "$FINAL_STATUS" \
  --argjson reviews "$REVIEWS_JSON" \
  '{
    schema_version: "1.0",
    pipeline_run_id: $run_id,
    timestamp: (now | todate),
    stage: "reviewer",
    status: $status,
    data: { reviews: $reviews }
  }' > "$RUN_DIR/reviewer-output.json"
```

## Validation Architecture

### Test Framework

| Property | Value |
|----------|-------|
| Framework | bash + jq (test scripts) |
| Config file | `tests/run-all.sh` |
| Quick run command | `bash tests/test-reviewer-validation.sh` |
| Full suite command | `bash tests/run-all.sh` |

### Phase Requirements to Test Map

| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| VERF-01 | Reviewer feedback JSON has issues for unsupported claims | unit (schema validation) | `bash tests/test-reviewer-validation.sh` | No -- Wave 0 |
| VERF-02 | Legal accuracy fields present in feedback (statute, date, jurisdiction) | unit (fixture validation) | `bash tests/test-reviewer-validation.sh` | No -- Wave 0 |
| VERF-03 | Iteration loop respects 3-round cap and escalates | unit (script logic) | `bash tests/test-reviewer-iteration.sh` | No -- Wave 0 |
| VERF-04 | Final report contains per-claim verification annotations | unit (grep for markers) | `bash tests/test-reviewer-annotation.sh` | No -- Wave 0 |

### Sampling Rate
- **Per task commit:** `bash tests/test-reviewer-validation.sh`
- **Per wave merge:** `bash tests/run-all.sh`
- **Phase gate:** Full suite green before `/gsd-verify-work`

### Wave 0 Gaps
- [ ] `tests/test-reviewer-validation.sh` -- covers VERF-01, VERF-02 (schema and feedback structure)
- [ ] `tests/test-reviewer-iteration.sh` -- covers VERF-03 (iteration logic, escalation trigger)
- [ ] `tests/test-reviewer-annotation.sh` -- covers VERF-04 (per-claim annotation presence)
- [ ] `tests/fixtures/sample-reviewer-feedback.json` -- valid feedback fixture
- [ ] `tests/fixtures/sample-reviewer-output.json` -- complete reviewer envelope fixture
- [ ] `tests/fixtures/sample-escalation.md` -- escalation markdown fixture
- [ ] `pipeline/schemas/reviewer-feedback.schema.json` -- feedback schema
- [ ] `pipeline/schemas/reviewer-feedback.jq` -- jq validation for feedback

## Security Domain

### Applicable ASVS Categories

| ASVS Category | Applies | Standard Control |
|---------------|---------|-----------------|
| V2 Authentication | No | N/A -- CLI-only, no auth |
| V3 Session Management | No | N/A -- stateless pipeline runs |
| V4 Access Control | No | N/A -- local filesystem only |
| V5 Input Validation | Yes | jq schema validation on all JSON inputs; strict pattern matching on file paths and finding IDs (matching approve-findings.sh pattern) |
| V6 Cryptography | No | N/A -- no secrets handled |

### Known Threat Patterns

| Pattern | STRIDE | Standard Mitigation |
|---------|--------|---------------------|
| Malformed JSON injection via agent output | Tampering | jq schema validation via validate-handoff.sh [VERIFIED: codebase] |
| Path traversal in report_path | Tampering | Validate report_path starts with `reports/` and category is valid (existing pattern from run-researcher.sh) [VERIFIED: codebase] |
| Finding ID injection in escalation approval | Tampering | Strict pattern matching on finding IDs (existing pattern from approve-findings.sh) [VERIFIED: codebase] |

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | Each review round should be a separate `claude -p` invocation (not self-looping within one agent call) | Architecture Patterns / Anti-Patterns | LOW -- if self-looping works better, the bash script is simpler but less controllable |
| A2 | Researcher revision prompt can reuse the existing researcher agent with a modified prompt (not a separate agent definition) | Architecture Patterns / Pattern 4 | LOW -- if a separate revision agent is needed, it is a small addition |
| A3 | `--max-turns 25` is sufficient for reviewer to check a typical report (5-15 claims, 3-10 sources) | Common Pitfalls / Pitfall 1 | MEDIUM -- if insufficient, claims may go unchecked; increase to 30 or instruct prioritization |
| A4 | Dispute evaluation criteria (reviewer accepts dispute if researcher provides verifiable source) will prevent infinite dispute loops | Common Pitfalls / Pitfall 3 | MEDIUM -- if both agents argue in circles, all reviews will escalate to human |
| A5 | HTML comments (`<!-- verified -->`) are a non-disruptive annotation format for per-claim verification status | Architecture Patterns / Pattern 6 | LOW -- alternative formats exist; any inline annotation works |

## Open Questions

1. **Researcher revision mode**
   - What we know: The researcher agent's system prompt is designed for initial report writing from a finding. It needs to also handle revisions based on reviewer feedback.
   - What's unclear: Should the revision instruction go in the researcher agent prompt permanently (as a "Revision Mode" section), or should the orchestration script pass all context via the `-p` prompt argument?
   - Recommendation: Add a "Revision Mode" section to the researcher agent prompt. This keeps the agent self-contained and avoids extremely long inline prompts. The orchestration script passes the feedback file path and round number; the agent prompt explains how to process them.

2. **Per-claim annotation granularity**
   - What we know: VERF-04 requires per-claim verification status. Reports have section-level confidence tags but individual claims are inline text with source links.
   - What's unclear: Should every inline citation get an annotation, or only claims where issues were found/disputed?
   - Recommendation: Annotate ALL checked claims (verified/disputed/needs-human-review). This provides positive confirmation that claims were checked, not just flagging problems.

## Sources

### Primary (HIGH confidence)
- `.claude/agents/reviewer.md` -- Current reviewer agent stub, tools, model assignment
- `pipeline/schemas/reviewer.schema.json` -- Existing reviewer output schema
- `pipeline/schemas/reviewer.jq` -- Existing jq validation rules
- `pipeline/schemas/envelope.schema.json` -- Pipeline envelope format
- `pipeline/scripts/run-researcher.sh` -- Researcher orchestration pattern to replicate
- `pipeline/scripts/approve-findings.sh` -- APPROVED marker pattern to reuse
- `pipeline/scripts/generate-review.sh` -- Markdown generation pattern to reuse
- `pipeline/templates/client-alert.md` -- Report structure reviewer must parse
- `pipeline/templates/research-memo.md` -- Report structure reviewer must parse
- `.planning/phases/04-verification/04-CONTEXT.md` -- All locked decisions D-01 through D-11

### Secondary (MEDIUM confidence)
- `CLAUDE.md` -- Technology stack, CLI patterns, model assignments, token cost strategy

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH -- no new dependencies, all patterns verified in codebase
- Architecture: HIGH -- iteration protocol fully specified by locked decisions, patterns match existing codebase
- Pitfalls: MEDIUM -- context window and dispute loop concerns are reasonable extrapolations but not empirically tested

**Research date:** 2026-04-07
**Valid until:** 2026-05-07 (stable -- no external library dependencies, all internal patterns)
