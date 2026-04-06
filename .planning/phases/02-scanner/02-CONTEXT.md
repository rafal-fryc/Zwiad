# Phase 2: Scanner - Context

**Gathered:** 2026-04-06
**Status:** Ready for planning

<domain>
## Phase Boundary

The scanner agent can ingest an email digest file, query government and law firm websites, detect duplicates against existing reports, and present a structured findings list requiring human approval before any research proceeds.

</domain>

<decisions>
## Implementation Decisions

### Email Digest Parsing
- **D-01:** Input format is HTML, converted from .eml using the `eml-to-html` npm package (https://github.com/dunnkers/eml-to-html). The scanner does not parse .eml directly.
- **D-02:** The primary digest source is Lexology daily newsfeed. Each item has: title (linked to full article), law firm name, summary snippet, optional tags (jurisdiction, content type like "Video"). Items are organized by region/topic sections.
- **D-03:** Scanner follows every Lexology link to fetch the full article text via WebFetch — the digest only contains truncated snippets.
- **D-04:** Scanner filters items by topic section, only extracting items from sections that map to the project's three categories (privacy, cybersecurity, ai-law). Irrelevant sections are skipped.
- **D-05:** Design the digest parser so adding new digest formats (JD Supra, Mondaq, etc.) is straightforward in a future phase. Lexology-specific parsing for now.

### Source Scanning Strategy
- **D-06:** Government sources use both approaches: direct fetch for known high-value pages (FTC press releases, congress.gov bill search, NIST) AND WebSearch queries for broader discovery of new developments.
- **D-07:** Law firm alerts: Lexology digest is the primary source. Supplement with WebSearch for firms/alerts not in the Lexology feed to catch what the digest misses.
- **D-08:** On source failure (timeout, blocked, down): log the failure in the output and continue scanning other sources. User sees which sources failed in the findings report.
- **D-09:** Source list (government sites, search queries, direct URLs) maintained in a config file (JSON or YAML), not hardcoded in the agent prompt. Easy to add/remove sources without modifying agent code.

### Duplicate Detection
- **D-10:** Layered dedup approach — First pass: exact URL match against existing reports. Second pass: title similarity. Third pass: Claude semantic comparison of remaining candidates against recent reports. Progressive cost.
- **D-11:** Detected duplicates are auto-skipped from the findings list. User does not see them in the approval file.

### Human Approval Flow
- **D-12:** Scanner outputs both a human-readable markdown file (with checkboxes per finding) and a JSON state file. User reviews/edits the markdown; a script converts checkbox edits back to JSON for the pipeline.
- **D-13:** User can make light edits during review — fix titles, adjust relevance, add a note. Not full rewriting (that's the researcher's job).
- **D-14:** Pipeline resumes when the user adds an `## APPROVED` marker to the review markdown file. Pipeline checks for this marker before proceeding to the next stage.

### Claude's Discretion
- Lexology HTML parsing implementation details (CSS selectors, link extraction patterns)
- URL normalization strategy for dedup (stripping UTM params, etc.)
- Exact config file format (JSON vs YAML) and schema for source list
- Search query design for government source discovery
- Review markdown formatting and layout
- Finding ID generation scheme

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project context
- `.planning/PROJECT.md` — Project vision, constraints (CLI-only, local filesystem, no API keys)
- `.planning/REQUIREMENTS.md` — SCAN-01 through SCAN-05, PIPE-03 (human confirmation gate)
- `CLAUDE.md` — Technology stack, CLI invocation patterns, model assignments, web scraping tool recommendations

### Phase 1 infrastructure
- `.planning/phases/01-agent-framework/01-CONTEXT.md` — Agent definitions, JSON state contracts, directory structure, pipeline orchestration decisions
- `.claude/agents/scanner.md` — Scanner agent stub (sonnet model, WebSearch+WebFetch+Read+Write tools)
- `pipeline/schemas/scanner.schema.json` — Scanner output schema (findings array with required fields)
- `pipeline/schemas/envelope.schema.json` — Pipeline handoff envelope (schema_version, pipeline_run_id, timestamp, stage, status, data)
- `pipeline/scripts/validate-handoff.sh` — Schema validation script

### External tools
- `eml-to-html` npm package: https://github.com/dunnkers/eml-to-html — .eml to HTML conversion dependency

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `.claude/agents/scanner.md` — Agent stub with correct frontmatter (sonnet, tools: WebSearch+WebFetch+Read+Write). Needs full system prompt.
- `pipeline/schemas/scanner.schema.json` — Output schema already defines finding fields (id, title, source, source_url, summary, relevance, jurisdiction, development_type)
- `pipeline/schemas/envelope.schema.json` — Envelope with `pending-review` status ready for human approval gate
- `pipeline/scripts/validate-handoff.sh` — jq-based validation for schema checking

### Established Patterns
- Agent definitions in `.claude/agents/*.md` with frontmatter (model, tools, permissionMode)
- JSON state files with common envelope wrapping stage-specific data
- Timestamped pipeline run directories: `pipeline/runs/YYYY-MM-DDTHH-MM-SS/`
- Bash+jq for validation — no Node/Python dependency in pipeline scripts

### Integration Points
- `input/` directory — scanner reads email digest HTML files from here
- `pipeline/runs/<run-id>/` — scanner writes output JSON here
- `reports/` with `privacy/`, `cybersecurity/`, `ai-law/` subdirectories — scanner checks these for duplicate detection
- Orchestrator agent spawns scanner via Agent tool (D-09 from Phase 1)

</code_context>

<specifics>
## Specific Ideas

- Lexology URLs contain UTM tracking parameters that should be stripped for cleaner storage and dedup matching (e.g., `?g=3b2f0dcb-...&utm_source=...` — the `g` param is the article ID)
- User will provide an example HTML email for parser development — build parsing against actual Lexology format
- Digest has geographic sections (USA, North America, Global, Europe) and topic sections (IT & Data Protection) — use topic sections for filtering, geographic sections for jurisdiction hints
- Tags on individual items (e.g., "Iowa" badge) provide jurisdiction signals that should map to the `jurisdiction` field in the schema

</specifics>

<deferred>
## Deferred Ideas

- Support for additional digest formats (JD Supra, Mondaq, Law360) — future phase, but D-05 ensures extensible design
- LinkedIn feed monitoring — v2 requirement (SOCL-01), explicitly out of scope for v1

None — discussion stayed within phase scope

</deferred>

---

*Phase: 02-scanner*
*Context gathered: 2026-04-06*
