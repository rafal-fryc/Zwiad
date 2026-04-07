# Phase 4: Verification - Context

**Gathered:** 2026-04-07
**Status:** Ready for planning

<domain>
## Phase Boundary

The reviewer agent independently audits every researcher-produced report for hallucinations and legal accuracy, iterates with the researcher to resolve disagreements (up to 3 rounds), and escalates to human review when iteration is exhausted. The final verified report includes per-claim verification status annotations. This phase fills in the reviewer agent's system prompt, creates the review orchestration script, and builds the iteration/escalation machinery.

</domain>

<decisions>
## Implementation Decisions

### Verification Methodology
- **D-01:** Reviewer uses a two-pronged approach: re-fetch all cited source URLs via WebFetch to check claims match source content, PLUS independent WebSearch for key facts to catch missing context or uncited information.
- **D-02:** Reviewer tools must be updated from Read+WebFetch to Read+WebFetch+WebSearch to enable independent fact-checking and legislative status lookups.
- **D-03:** Legal accuracy verification covers: statute citation correctness, effective dates, jurisdiction attribution, AND current legislative status (enacted, pending, vetoed, amended).
- **D-04:** When a cited source URL is inaccessible (down, paywalled, etc.), the claim is flagged as "unverifiable — source unavailable" in the review output. The review continues; the whole review does not fail.

### Iteration Protocol
- **D-05:** Reviewer communicates issues via structured JSON feedback files. Each issue includes: claim text, issue description, severity (critical/major/minor), and suggested fix. Fits existing schema patterns.
- **D-06:** A round resolves (iteration stops) when the reviewer finds zero critical or major issues. Minor issues are noted in the final report but do not trigger another round.
- **D-07:** Researcher can push back on reviewer findings by marking an issue as "disputed" with evidence/justification. Reviewer re-evaluates the dispute in the next round.
- **D-08:** Iteration state tracked via versioned files per round in the pipeline run directory: `reviewer-feedback-r{N}.json`, `researcher-revision-r{N}.json`. Full audit trail preserved.

### Human Escalation Flow
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

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project context
- `.planning/PROJECT.md` — Project vision, constraints (CLI-only, local filesystem, no API keys), 3-round review cap
- `.planning/REQUIREMENTS.md` — VERF-01 (source-backed claims), VERF-02 (legal accuracy), VERF-03 (3-round iteration + escalation), VERF-04 (per-claim verification annotation)
- `CLAUDE.md` — Technology stack, CLI invocation patterns, model assignments (opus for reviewer)

### Phase 1 infrastructure
- `.planning/phases/01-agent-framework/01-CONTEXT.md` — Agent definitions, JSON state contracts, batch processing (D-12), fail fast (D-11), pipeline orchestration (D-09)
- `.claude/agents/reviewer.md` — Reviewer agent stub (opus model, currently Read+WebFetch — needs WebSearch added per D-02)
- `pipeline/schemas/reviewer.schema.json` — Reviewer output schema (reviews array with status, iteration_count, claims_checked, issues_found)
- `pipeline/schemas/researcher.schema.json` — Researcher output schema (reports with finding_id, report_path, format, confidence_summary)
- `pipeline/schemas/envelope.schema.json` — Pipeline handoff envelope format
- `pipeline/scripts/validate-handoff.sh` — jq-based schema validation

### Phase 2 scanner (approval gate pattern)
- `.planning/phases/02-scanner/02-CONTEXT.md` — Human approval flow (D-12, D-14): markdown review file + APPROVED marker pattern to reuse for escalation
- `pipeline/scripts/approve-findings.sh` — Approval script pattern to reference for escalation resume

### Phase 3 researcher (reviewer's input)
- `.planning/phases/03-report-generation/03-CONTEXT.md` — Report format decisions, confidence tagging (D-08), source citations (D-04), official legal text requirement (D-06)
- `pipeline/scripts/run-researcher.sh` — Researcher orchestration script (iteration will invoke this for revisions)

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `.claude/agents/reviewer.md` — Agent stub with correct frontmatter (opus). Needs WebSearch added to tools and full system prompt.
- `pipeline/schemas/reviewer.schema.json` — Output schema already defines reviews array with status enum (verified/disputed/needs-human-review), iteration_count (1-3), claims_checked, issues_found (with claim/issue/severity)
- `pipeline/scripts/validate-handoff.sh` — Schema validation reusable for reviewer output validation
- `pipeline/scripts/approve-findings.sh` — APPROVED marker pattern reusable for escalation resume flow
- `pipeline/scripts/generate-review.sh` — Markdown review generation pattern reusable for escalation file

### Established Patterns
- Agent definitions in `.claude/agents/*.md` with frontmatter (model, tools, permissionMode)
- JSON state files with common envelope wrapping stage-specific data
- Timestamped pipeline run directories: `pipeline/runs/YYYY-MM-DDTHH-MM-SS/`
- Bash orchestration scripts invoking `claude -p --agent`
- Human approval via markdown file + `## APPROVED` marker (Phase 2)

### Integration Points
- Input: `researcher-output.json` from Phase 3 (contains report paths and metadata)
- Input: Markdown reports in `reports/{category}/` directories
- Output: `reviewer-output.json` with verification status per report
- Output: Versioned feedback/revision files per iteration round
- Output: Escalation markdown file for human review (when needed)
- Orchestration: Script invokes `claude -p --agent reviewer` and manages iteration loop

</code_context>

<specifics>
## Specific Ideas

- Escalation file should follow the same human-review pattern as scanner approval: user gets a readable markdown document, makes edits, adds APPROVED marker to resume
- Versioned round files (reviewer-feedback-r1.json, researcher-revision-r1.json) provide a natural audit trail that the escalation summary can compile from
- The reviewer's independent WebSearch should focus on verifying KEY claims (statute numbers, dates, enforcement actions) rather than re-researching the entire topic

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope

</deferred>

---

*Phase: 04-verification*
*Context gathered: 2026-04-07*
