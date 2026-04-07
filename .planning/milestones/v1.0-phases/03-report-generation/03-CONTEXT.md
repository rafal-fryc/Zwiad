# Phase 3: Report Generation - Context

**Gathered:** 2026-04-06
**Status:** Ready for planning

<domain>
## Phase Boundary

The researcher agent takes a set of approved findings and produces complete, publication-quality markdown reports with citations, jurisdiction tags, adaptive format selection, and confidence-scored claims. This phase fills in the researcher agent's system prompt, creates report templates, and builds the orchestration script that runs the researcher on approved findings.

</domain>

<decisions>
## Implementation Decisions

### Report Structure & Format
- **D-01:** Two distinct report formats — client-alert (short, executive-friendly, action-oriented, 1-2 pages) and research-memo (long, technical, analytical, 3-5+ pages). Each has a different template with different sections.
- **D-02:** Format-dependent sections:
  - **Client-alert:** Title, Summary, Key Facts, Action Items, Source Citations, Related Reports, Jurisdiction Tags
  - **Research-memo:** Title, Executive Summary, Background, Detailed Analysis, Impact Assessment, Action Items, Source Citations, Related Reports, Jurisdiction Tags
- **D-03:** Format selection is relevance-based: HIGH relevance findings produce client-alerts (urgent, notify now). MEDIUM/LOW relevance findings produce research-memos (deeper background analysis).
- **D-04:** Source citations use both inline markdown links for readability AND a deduplicated Sources section at the bottom listing all URLs used.

### Source Research Depth
- **D-05:** Research depth is format-dependent: client-alerts get primary source + 1-2 verification sources (fast). Research-memos get deep research with 5-10 sources (thorough: official text, legislative history, enforcement precedents, affected industry analysis).
- **D-06:** Researcher MUST always locate and cite official legal text (statute, regulation, rule from congress.gov, state legislature, CFR) when a finding references legislation. This is non-negotiable for legal accuracy.

### Confidence Tagging
- **D-07:** Confidence levels determined by source quality + verification combined:
  - **HIGH:** Official government source, court filing, statute text — OR any claim corroborated by 2+ independent authoritative sources
  - **MEDIUM:** Single reputable law firm analysis or major news outlet
  - **LOW:** Secondary reporting, opinion pieces, unverified social media, uncorroborated non-authoritative source
- **D-08:** Confidence tags applied at the section/paragraph level (e.g., "### Key Facts [HIGH confidence]"), not per individual claim. Clean reading without cluttering the prose.

### Related Reports Linking
- **D-09:** Researcher reads recent reports in the same category using Claude semantic search to assess thematic similarity. Picks the truly related ones — not just keyword matches.
- **D-10:** Related Reports section format is at Claude's discretion. Must link related reports with clear connection explanation.

### Claude's Discretion
- Exact report markdown template styling and formatting details
- Related Reports section format (simple list, annotated list, or other)
- WebSearch query design for finding official legal texts
- How many reports to compare for Related Reports (3-5 in same category is reasonable)
- Report filename convention (e.g., `jurisdiction-topic-date.md`)
- Orchestration script details for running researcher on batches of approved findings

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project context
- `.planning/PROJECT.md` — Project vision, constraints (CLI-only, local filesystem), flexible report format decision
- `.planning/REQUIREMENTS.md` — REPT-01 (structured markdown reports), REPT-02 (format selection), REPT-03 (confidence tagging), REPT-04 (Related Reports section)
- `CLAUDE.md` — Technology stack, CLI invocation patterns, model assignments (opus for researcher)

### Phase 1 infrastructure
- `.planning/phases/01-agent-framework/01-CONTEXT.md` — Agent definitions, JSON state contracts, batch processing model, directory structure
- `.claude/agents/researcher.md` — Researcher agent stub (opus model, WebSearch+WebFetch+Read+Write tools)
- `pipeline/schemas/researcher.schema.json` — Researcher output schema (finding_id, report_path, format, jurisdiction_tags, confidence_summary)
- `pipeline/schemas/envelope.schema.json` — Pipeline handoff envelope format

### Phase 2 scanner output (researcher input)
- `.planning/phases/02-scanner/02-CONTEXT.md` — Scanner decisions, approval flow, finding structure
- `pipeline/schemas/scanner.schema.json` — Scanner finding fields (id, title, source, source_url, summary, relevance, jurisdiction, development_type, category)
- `pipeline/scripts/approve-findings.sh` — Produces scanner-approved.json (researcher's input)

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `.claude/agents/researcher.md` — Agent stub with correct frontmatter (opus, tools: WebSearch+WebFetch+Read+Write). Needs full system prompt.
- `pipeline/schemas/researcher.schema.json` — Output schema already defines format enum (client-alert/research-memo), jurisdiction_tags array, confidence_summary (high/medium/low counts)
- `pipeline/scripts/validate-handoff.sh` — jq-based validation for schema checking
- `pipeline/schemas/envelope.schema.json` — Common envelope with `researcher` stage

### Established Patterns
- Agent definitions in `.claude/agents/*.md` with frontmatter
- JSON state files with common envelope wrapping stage-specific data
- Timestamped pipeline run directories: `pipeline/runs/YYYY-MM-DDTHH-MM-SS/`
- Bash orchestration scripts (e.g., `run-scanner.sh`) that invoke `claude -p --agent`
- Source config in `pipeline/config/sources.json` — similar config pattern available for report templates

### Integration Points
- Input: `scanner-approved.json` from Phase 2 approval gate (contains approved finding IDs + metadata)
- Output: Markdown reports written to `reports/{category}/` directories
- Output: `researcher-output.json` with report metadata for downstream reviewer agent
- Orchestration: Script invokes `claude -p --agent researcher` per finding (or batched)

</code_context>

<specifics>
## Specific Ideas

- Scanner findings include `relevance` (high/medium/low) which maps directly to format selection (D-03)
- Scanner findings include `development_type` which can inform research depth (e.g., enforcement actions may need court filing lookups)
- Reports serve dual purpose: standalone client alerts AND knowledge base entries (from PROJECT.md context)
- The `category` field from scanner maps to report output directory (privacy/cybersecurity/ai-law)

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within phase scope

</deferred>

---

*Phase: 03-report-generation*
*Context gathered: 2026-04-06*
