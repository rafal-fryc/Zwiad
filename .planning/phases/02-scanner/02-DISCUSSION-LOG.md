# Phase 2: Scanner - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-04-06
**Phase:** 02-scanner
**Areas discussed:** Email Digest Parsing, Source Scanning Strategy, Duplicate Detection, Human Approval Flow

---

## Email Digest Parsing

| Option | Description | Selected |
|--------|-------------|----------|
| Plain text (.txt) | Copy-paste email body into text file | |
| Raw email (.eml) | Save as .eml, needs MIME parsing | |
| HTML (.html) | Save rendered email as HTML | |
| Multiple formats | Support all three, auto-detect | |

**User's choice:** .eml files converted to HTML using `eml-to-html` npm package (https://github.com/dunnkers/eml-to-html)
**Notes:** User has .eml files from Lexology; wants a conversion step, then scanner works with HTML.

| Option | Description | Selected |
|--------|-------------|----------|
| Links + short summaries | Headlines with URLs to full articles | |
| Full article text inline | Complete alert text in email | |
| Mix of both | Some full text, some links | |

**User's choice:** User provided screenshot — Lexology digest contains titles linked to full articles, law firm names, and truncated summaries. Links + short summaries pattern.

| Option | Description | Selected |
|--------|-------------|----------|
| Follow links (Recommended) | Fetch full article from each URL | ✓ |
| Digest only | Extract only what's in the digest HTML | |
| Follow selectively | Only follow high-relevance links | |

**User's choice:** Follow links — scanner fetches full article text from each Lexology URL.

| Option | Description | Selected |
|--------|-------------|----------|
| Lexology only | Single digest, tailored parser | |
| Multiple digests | Multiple aggregators, generic parser | |
| Lexology now, others later | Start Lexology-specific, design for extensibility | ✓ |

**User's choice:** Lexology now, others later.

| Option | Description | Selected |
|--------|-------------|----------|
| Capture all, score later | Extract everything, use relevance scoring | |
| Filter by topic section | Only extract from relevant sections | ✓ |
| Configurable filter list | Maintain editable keyword/section list | |

**User's choice:** Filter by topic section, mapped to the project's three categories (privacy, cybersecurity, ai-law).

---

## Source Scanning Strategy

| Option | Description | Selected |
|--------|-------------|----------|
| WebSearch queries | Targeted web searches for government sources | |
| Direct site queries | Fetch specific known pages and parse | |
| Both approaches | Direct fetch + web search for broader discovery | ✓ |

**User's choice:** Both approaches — direct fetch for known high-value pages, web search for broader discovery.

| Option | Description | Selected |
|--------|-------------|----------|
| Digest is primary | Lexology only, don't scrape law firm sites | |
| Supplement with search | Lexology first, then WebSearch for gaps | ✓ |
| Both independently | Scan sites AND digest independently | |

**User's choice:** Supplement with search — Lexology digest primary, WebSearch fills gaps.

| Option | Description | Selected |
|--------|-------------|----------|
| Log and continue (Recommended) | Note failure, continue scanning other sources | ✓ |
| Retry once then continue | One retry with delay, then log and move on | |
| Fail the whole scan | Any source failure stops scanner | |

**User's choice:** Log and continue.

| Option | Description | Selected |
|--------|-------------|----------|
| Config file (Recommended) | JSON/YAML file listing sources and queries | ✓ |
| Hardcoded in agent prompt | Sources in scanner.md directly | |
| Both — defaults + overrides | Hardcoded defaults with config overrides | |

**User's choice:** Config file.

---

## Duplicate Detection

| Option | Description | Selected |
|--------|-------------|----------|
| URL + title matching | Compare URLs and normalized titles | |
| Semantic similarity | Claude compares summaries | |
| Layered approach (Recommended) | URL match → title similarity → Claude semantic comparison | ✓ |

**User's choice:** Layered approach.

| Option | Description | Selected |
|--------|-------------|----------|
| Flag but include | Mark as possible duplicate, user decides | |
| Auto-skip | Exclude duplicates automatically | ✓ |
| Separate section | Show in separate "Already Covered" section | |

**User's choice:** Auto-skip — duplicates removed from findings list.

---

## Human Approval Flow

| Option | Description | Selected |
|--------|-------------|----------|
| Markdown with checkboxes | Checkboxes for approve/reject | |
| JSON with approve field | Machine-readable approve/reject | |
| Both — markdown + JSON | Markdown for review, script converts to JSON | ✓ |

**User's choice:** Both — human-friendly markdown for review, script converts back to JSON.

| Option | Description | Selected |
|--------|-------------|----------|
| Approve/reject only (Recommended) | Simple check/uncheck | |
| Light edits allowed | Fix titles, adjust relevance, add notes | ✓ |
| Full editing | Rewrite summaries, add context | |

**User's choice:** Light edits allowed.

| Option | Description | Selected |
|--------|-------------|----------|
| Re-run command | User runs resume command after editing | |
| Watch for file change | Auto-resume on file change | |
| Approval marker | User adds `## APPROVED` marker when done | ✓ |

**User's choice:** Approval marker — user adds `## APPROVED` to signal completion.

---

## Claude's Discretion

- Lexology HTML parsing implementation (selectors, patterns)
- URL normalization for dedup
- Config file format and schema
- Search query design for government sources
- Review markdown layout
- Finding ID generation

## Deferred Ideas

- Additional digest format support (JD Supra, Mondaq, Law360) — future phase
- LinkedIn feed monitoring — v2 (SOCL-01)
