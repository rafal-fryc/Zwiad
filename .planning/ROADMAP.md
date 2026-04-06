# Roadmap: Zwiad

## Overview

Zwiad is built in five phases. Phase 1 establishes the subprocess agent framework and JSON handoff contracts that every other phase depends on. Phase 2 delivers the scanner -- parsing email digests, querying government and law firm sites, deduplicating, and presenting findings for human approval. Phase 3 delivers the researcher agent that turns approved findings into structured markdown reports with source citations and confidence tagging. Phase 4 adds the reviewer agent and the researcher-reviewer iteration loop with human escalation. Phase 5 closes the pipeline: categorized output folders, audit trail logs, and scheduled execution support.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Agent Framework** - Establish subprocess agent infrastructure and JSON state contracts
- [ ] **Phase 2: Scanner** - Scan sources, deduplicate, present findings, require human approval before proceeding
- [ ] **Phase 3: Report Generation** - Researcher agent produces structured, source-cited, confidence-tagged markdown reports
- [ ] **Phase 4: Verification** - Reviewer agent checks claims, iterates with researcher up to 3 rounds, escalates unresolved
- [ ] **Phase 5: Pipeline Integration** - Categorized output filing, audit trail, scheduled execution support

## Phase Details

### Phase 1: Agent Framework
**Goal**: The subprocess agent infrastructure and shared JSON state contracts exist and work, enabling all subsequent agents to be built against a stable foundation
**Depends on**: Nothing (first phase)
**Requirements**: PIPE-05, PIPE-06
**Success Criteria** (what must be TRUE):
  1. A claude subprocess agent can be launched via `claude -p --agent` and exits cleanly with a result
  2. Agents read and write JSON state files that are validated against a schema at each handoff
  3. A malformed or schema-violating JSON handoff is caught and reported as an error rather than silently passed through
**Plans:** 3 plans
Plans:
- [x] 01-01-PLAN.md -- Directory structure + agent definition stubs
- [x] 01-02-PLAN.md -- JSON schemas + jq validation script
- [x] 01-03-PLAN.md -- Test fixtures, test scripts, and smoke test

### Phase 2: Scanner
**Goal**: The scanner agent can ingest an email digest file, query government and law firm websites, detect duplicates against existing reports, and present a structured findings list requiring human approval before any research proceeds
**Depends on**: Phase 1
**Requirements**: SCAN-01, SCAN-02, SCAN-03, SCAN-04, SCAN-05, PIPE-03
**Success Criteria** (what must be TRUE):
  1. User can point the scanner at a saved email digest file and receive extracted alert links and summaries
  2. Scanner queries at least congress.gov, FTC, NIST, and state legislature sites and returns new developments not yet in the report folder
  3. Scanner queries law firm alert websites and returns new client alerts
  4. Scanner flags any finding that duplicates a development already covered by an existing report
  5. Scanner outputs a structured list (title, source, summary, relevance, link) and the pipeline halts until the user approves or rejects each finding
**Plans:** 4 plans
Plans:
- [x] 02-01-PLAN.md -- Scanner core: source config, EML conversion, agent prompt, orchestration
- [x] 02-02-PLAN.md -- Dedup pipeline, review markdown generator, approval gate
- [x] 02-03-PLAN.md -- Test fixtures and test scripts for scanner components
- [x] 02-04-PLAN.md -- Gap closure: law firm alert search queries, test fixture fix

### Phase 3: Report Generation
**Goal**: The researcher agent takes a set of approved findings and produces complete, publication-quality markdown reports with citations, jurisdiction tags, adaptive format selection, and confidence-scored claims
**Depends on**: Phase 2
**Requirements**: REPT-01, REPT-02, REPT-03, REPT-04
**Success Criteria** (what must be TRUE):
  1. User can run the researcher agent on an approved finding and receive a markdown report with source citations and jurisdiction tags
  2. Breaking news findings produce client-alert format reports; complex analysis findings produce research memo format reports
  3. Every factual claim in the report carries a HIGH, MEDIUM, or LOW confidence tag reflecting source quality
  4. Each finalized report contains a "Related Reports" section that links thematically similar reports already in the knowledge base
**Plans**: TBD
**UI hint**: no

### Phase 4: Verification
**Goal**: The reviewer agent independently audits every report for hallucinations and legal accuracy, iterates with the researcher to resolve disagreements, and escalates to human review when iteration is exhausted
**Depends on**: Phase 3
**Requirements**: VERF-01, VERF-02, VERF-03, VERF-04
**Success Criteria** (what must be TRUE):
  1. Reviewer agent reads a researcher-produced report and identifies any claims not supported by cited sources
  2. Reviewer agent flags incorrect statute citations, wrong effective dates, or misattributed jurisdictions
  3. Researcher and reviewer automatically iterate to resolve disagreements; after 3 unsuccessful rounds the report is flagged for human review and the pipeline pauses
  4. The final verified report includes a per-claim verification status annotation (verified / disputed / needs human review)
**Plans**: TBD

### Phase 5: Pipeline Integration
**Goal**: Finalized reports are automatically filed into the correct topic folders with emergent subcategories, every pipeline run produces a complete audit log, and the pipeline can be triggered on a schedule
**Depends on**: Phase 4
**Requirements**: PIPE-01, PIPE-02, PIPE-04
**Success Criteria** (what must be TRUE):
  1. After verification, each report is filed into /privacy, /cybersecurity, or /ai-law with a subcategory subfolder determined by the categorizer agent
  2. Each pipeline run produces a log file recording what was scanned, which findings were approved, which reports were produced, and whether verification passed
  3. The pipeline can be triggered by a cron job (or equivalent scheduler) for daily automated execution without manual intervention
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 -> 2 -> 3 -> 4 -> 5

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Agent Framework | 0/3 | Planning complete | - |
| 2. Scanner | 0/4 | Gap closure planned | - |
| 3. Report Generation | 0/TBD | Not started | - |
| 4. Verification | 0/TBD | Not started | - |
| 5. Pipeline Integration | 0/TBD | Not started | - |
