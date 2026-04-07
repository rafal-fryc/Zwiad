# Phase 3: Report Generation - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-04-06
**Phase:** 03-report-generation
**Areas discussed:** Report Structure & Format, Source Research Depth, Confidence Tagging, Related Reports Linking

---

## Report Structure & Format

| Option | Description | Selected |
|--------|-------------|----------|
| Length and depth | Alert: 1-2 pages. Memo: 3-5+ pages | |
| Audience and tone | Alert: executive. Memo: legal professional | |
| Both length and audience | Distinct templates for each format | ✓ |

**User's choice:** Both length and audience — client-alerts short and executive-friendly, research-memos long and technical.

| Option | Description | Selected |
|--------|-------------|----------|
| Minimal sections | Title, Summary, Key Facts, Sources, Tags | |
| Full structured report | All sections for both formats | |
| Format-dependent sections | Alert: compact. Memo: full structure | ✓ |

**User's choice:** Format-dependent sections.

| Option | Description | Selected |
|--------|-------------|----------|
| Auto-detect from finding type | development_type determines format | |
| Relevance-based | HIGH = alert, MEDIUM/LOW = memo | ✓ |
| Scanner metadata + researcher judgment | Default from metadata, researcher can override | |

**User's choice:** Relevance-based format selection.

| Option | Description | Selected |
|--------|-------------|----------|
| Inline links | Citations as markdown links in text | |
| Footnote-style | Numbered footnotes + Sources section | |
| Both inline + sources list | Inline links plus deduplicated Sources section | ✓ |

**User's choice:** Both inline links and a Sources section.

---

## Source Research Depth

| Option | Description | Selected |
|--------|-------------|----------|
| Primary source + context | Full article + 2-3 related sources | |
| Deep research | 5-10+ sources, legislative history, precedents | |
| Format-dependent depth | Alert: fast (1-2 sources). Memo: deep (5-10 sources) | ✓ |

**User's choice:** Format-dependent depth.

| Option | Description | Selected |
|--------|-------------|----------|
| Always cite official text | Locate and cite statute/regulation text | ✓ |
| Cite if easily found | Try, but don't spend excessive effort | |
| Cite law firm analysis | Rely on firm's summary of legal text | |

**User's choice:** Always cite official legal text — non-negotiable for legal accuracy.

---

## Confidence Tagging

| Option | Description | Selected |
|--------|-------------|----------|
| Source quality hierarchy | Government = HIGH, firm = MEDIUM, secondary = LOW | |
| Verification count | 2+ sources = HIGH, 1 authoritative = MEDIUM, 1 weak = LOW | |
| Both source quality + verification | Combined criteria for each level | ✓ |

**User's choice:** Both source quality and verification combined.

| Option | Description | Selected |
|--------|-------------|----------|
| Per-claim inline tags | Tag each factual claim inline | |
| Per-section tags | Tag at section/paragraph level | ✓ |
| Per-claim with clean format | Precise but non-intrusive format | |

**User's choice:** Per-section tags — clean reading without cluttering prose.

---

## Related Reports Linking

| Option | Description | Selected |
|--------|-------------|----------|
| Jurisdiction + topic match | File glob + frontmatter matching | |
| Claude semantic search | Read and assess thematic similarity | ✓ |
| Layered approach | Glob → tag match → Claude comparison | |

**User's choice:** Claude semantic search.

| Option | Description | Selected |
|--------|-------------|----------|
| Simple list | Bulleted titles with file paths | |
| Annotated list | Links with one-line relationship note | |
| You decide | Claude's discretion on format | ✓ |

**User's choice:** Claude's discretion.

---

## Claude's Discretion

- Report markdown template styling
- Related Reports section format
- WebSearch query design for official legal texts
- Report filename convention
- Orchestration script details

## Deferred Ideas

None.
