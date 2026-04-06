# Requirements: Zwiad

**Defined:** 2026-04-06
**Core Value:** Reliable, source-verified regulatory intelligence reports that can serve as both a queryable knowledge base and standalone client alerts.

## v1 Requirements

Requirements for initial release. Each maps to roadmap phases.

### Scanning & Input

- [ ] **SCAN-01**: Scanner agent parses forwarded email digest file to extract law firm alert links and development summaries
- [ ] **SCAN-02**: Scanner agent searches government websites (congress.gov, FTC, NIST, state legislature sites) for new developments
- [ ] **SCAN-03**: Scanner agent searches law firm alert websites for new client alerts
- [ ] **SCAN-04**: Scanner agent detects duplicate developments already covered by existing reports
- [ ] **SCAN-05**: Scanner presents structured findings (title, source, summary, relevance) with links for human review

### Report Generation

- [ ] **REPT-01**: Researcher agent produces structured markdown reports with source citations and jurisdiction tags
- [ ] **REPT-02**: Researcher agent selects format based on development type (client alert for breaking news, research memo for complex analysis)
- [ ] **REPT-03**: Each factual claim in report is tagged with confidence level (HIGH/MEDIUM/LOW) based on source quality
- [ ] **REPT-04**: Finalized reports include a "Related Reports" section linking similar developments in the knowledge base

### Verification

- [ ] **VERF-01**: Reviewer agent independently checks that all claims are supported by cited sources (no hallucinations)
- [ ] **VERF-02**: Reviewer agent verifies legal accuracy (correct statute citations, effective dates, jurisdiction attribution)
- [ ] **VERF-03**: Researcher and reviewer iterate up to 3 rounds; unresolved disagreements escalate to human review
- [ ] **VERF-04**: Reviewer annotates each claim with verification status in the final report

### Pipeline & Organization

- [ ] **PIPE-01**: Finalized reports filed into topic folders (/privacy, /cybersecurity, /ai-law) with emergent subcategories
- [ ] **PIPE-02**: Each pipeline run produces an audit trail log (what was scanned, approved, researched, verified)
- [ ] **PIPE-03**: Human confirmation gate — scanner findings require approval before research proceeds
- [ ] **PIPE-04**: Pipeline supports scheduled daily execution via cron
- [ ] **PIPE-05**: Each agent runs as a separate Claude Code subprocess via `claude -p --agent`
- [ ] **PIPE-06**: Agents communicate via JSON state files with schema validation at each handoff

## v2 Requirements

Deferred to future release. Tracked but not in current roadmap.

### Social & Extended Sources

- **SOCL-01**: Scanner agent integrates LinkedIn feed monitoring for designated accounts
- **SOCL-02**: Scanner agent monitors additional social platforms for regulatory commentary

### Advanced Analysis

- **ANAL-01**: Multi-jurisdictional comparison tables auto-generated when multiple states pass similar laws
- **ANAL-02**: Natural language query interface for searching the report knowledge base
- **ANAL-03**: Trend detection across accumulated reports (emerging regulatory patterns)

### Automation

- **AUTO-01**: Fully autonomous operation — scanner findings auto-approved for trusted development types
- **AUTO-02**: Configurable approval thresholds based on source reliability and topic sensitivity

## Out of Scope

Explicitly excluded. Documented to prevent scope creep.

| Feature | Reason |
|---------|--------|
| Web UI / dashboard | Massive scope expansion; markdown files + existing tools (VS Code, Obsidian) sufficient for target user |
| Paywalled databases (Westlaw, LexisNexis, Bloomberg Law) | Expensive subscriptions ($10K+/yr), ToS violations for scraping; law firm alerts synthesize this content |
| Global jurisdiction coverage | Scope explosion; each jurisdiction has different structures and languages; nail US first |
| Real-time monitoring / streaming | Regulatory changes happen on days/weeks timescale; daily batch is sufficient |
| Automated legal advice / action items | Context-dependent; generic AI-generated legal advice creates liability exposure |
| Agent SDK / API-based orchestration | Using Claude Code CLI for zero API cost; included in subscription |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
|-------------|-------|--------|
| SCAN-01 | Pending | Pending |
| SCAN-02 | Pending | Pending |
| SCAN-03 | Pending | Pending |
| SCAN-04 | Pending | Pending |
| SCAN-05 | Pending | Pending |
| REPT-01 | Pending | Pending |
| REPT-02 | Pending | Pending |
| REPT-03 | Pending | Pending |
| REPT-04 | Pending | Pending |
| VERF-01 | Pending | Pending |
| VERF-02 | Pending | Pending |
| VERF-03 | Pending | Pending |
| VERF-04 | Pending | Pending |
| PIPE-01 | Pending | Pending |
| PIPE-02 | Pending | Pending |
| PIPE-03 | Pending | Pending |
| PIPE-04 | Pending | Pending |
| PIPE-05 | Pending | Pending |
| PIPE-06 | Pending | Pending |

**Coverage:**
- v1 requirements: 19 total
- Mapped to phases: 0
- Unmapped: 19 ⚠️

---
*Requirements defined: 2026-04-06*
*Last updated: 2026-04-06 after initial definition*
