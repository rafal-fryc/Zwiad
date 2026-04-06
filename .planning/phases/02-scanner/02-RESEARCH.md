# Phase 02: Scanner - Research

**Researched:** 2026-04-06
**Domain:** Email digest parsing, web scraping for regulatory sources, duplicate detection, human approval workflow
**Confidence:** MEDIUM-HIGH

## Summary

Phase 02 implements the scanner agent -- the first real pipeline stage. The scanner must (1) parse Lexology HTML email digests to extract law firm alerts, (2) query government websites and search the web for new regulatory developments, (3) detect duplicates against existing reports, and (4) present a structured findings list for human approval before research proceeds.

The core technical challenge is in three areas: reliably parsing Lexology HTML digests (no public spec exists -- must reverse-engineer from actual emails), designing a source configuration system that separates scanning logic from source definitions, and implementing a layered dedup approach that balances cost with accuracy. The human approval gate is architecturally simpler since Phase 1 already established the `pending-review` envelope status and the scanner JSON schema.

**Primary recommendation:** Build the scanner as a multi-step bash orchestration script that (1) converts .eml to HTML via `eml-to-html` Python CLI, (2) invokes the scanner Claude agent with the HTML content and source config, (3) runs dedup against existing reports, and (4) generates both the JSON state file and human-readable review markdown. The scanner agent prompt does the heavy lifting (HTML parsing, web searching, structuring findings), while bash handles file I/O and the approval gate.

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions
- **D-01:** Input format is HTML, converted from .eml using the `eml-to-html` Python package (https://github.com/dunnkers/eml-to-html). The scanner does not parse .eml directly.
- **D-02:** The primary digest source is Lexology daily newsfeed. Each item has: title (linked to full article), law firm name, summary snippet, optional tags (jurisdiction, content type like "Video"). Items are organized by region/topic sections.
- **D-03:** Scanner follows every Lexology link to fetch the full article text via WebFetch -- the digest only contains truncated snippets.
- **D-04:** Scanner filters items by topic section, only extracting items from sections that map to the project's three categories (privacy, cybersecurity, ai-law). Irrelevant sections are skipped.
- **D-05:** Design the digest parser so adding new digest formats (JD Supra, Mondaq, etc.) is straightforward in a future phase. Lexology-specific parsing for now.
- **D-06:** Government sources use both approaches: direct fetch for known high-value pages (FTC press releases, congress.gov bill search, NIST) AND WebSearch queries for broader discovery of new developments.
- **D-07:** Law firm alerts: Lexology digest is the primary source. Supplement with WebSearch for firms/alerts not in the Lexology feed to catch what the digest misses.
- **D-08:** On source failure (timeout, blocked, down): log the failure in the output and continue scanning other sources. User sees which sources failed in the findings report.
- **D-09:** Source list (government sites, search queries, direct URLs) maintained in a config file (JSON or YAML), not hardcoded in the agent prompt. Easy to add/remove sources without modifying agent code.
- **D-10:** Layered dedup approach -- First pass: exact URL match against existing reports. Second pass: title similarity. Third pass: Claude semantic comparison of remaining candidates against recent reports. Progressive cost.
- **D-11:** Detected duplicates are auto-skipped from the findings list. User does not see them in the approval file.
- **D-12:** Scanner outputs both a human-readable markdown file (with checkboxes per finding) and a JSON state file. User reviews/edits the markdown; a script converts checkbox edits back to JSON for the pipeline.
- **D-13:** User can make light edits during review -- fix titles, adjust relevance, add a note. Not full rewriting (that's the researcher's job).
- **D-14:** Pipeline resumes when the user adds an `## APPROVED` marker to the review markdown file. Pipeline checks for this marker before proceeding to the next stage.

### Claude's Discretion
- Lexology HTML parsing implementation details (CSS selectors, link extraction patterns)
- URL normalization strategy for dedup (stripping UTM params, etc.)
- Exact config file format (JSON vs YAML) and schema for source list
- Search query design for government source discovery
- Review markdown formatting and layout
- Finding ID generation scheme

### Deferred Ideas (OUT OF SCOPE)
- Support for additional digest formats (JD Supra, Mondaq, Law360) -- future phase, but D-05 ensures extensible design
- LinkedIn feed monitoring -- v2 requirement (SOCL-01), explicitly out of scope for v1
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| SCAN-01 | Scanner agent parses forwarded email digest file to extract law firm alert links and development summaries | Lexology HTML parsing via Claude agent with WebFetch for full article retrieval; eml-to-html for .eml conversion |
| SCAN-02 | Scanner agent searches government websites (congress.gov, FTC, NIST, state legislature sites) for new developments | Source config file with direct URLs and WebSearch queries; government source URLs documented below |
| SCAN-03 | Scanner agent searches law firm alert websites for new client alerts | Lexology digest as primary source + supplemental WebSearch queries |
| SCAN-04 | Scanner agent detects duplicate developments already covered by existing reports | Layered dedup: URL match, title similarity, semantic comparison against reports/ directory |
| SCAN-05 | Scanner presents structured findings (title, source, summary, relevance) with links for human review | Review markdown with checkboxes + JSON state file; approval marker workflow |
| PIPE-03 | Human confirmation gate -- scanner findings require approval before research proceeds | Markdown review file with `## APPROVED` marker; conversion script back to JSON |
</phase_requirements>

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| eml-to-html | 0.0.2 (Python/pip) | Convert .eml email files to .html | Locked decision D-01. Python CLI tool, NOT an npm package despite CONTEXT.md label. [VERIFIED: pip dry-run install succeeded, PyPI package exists] |
| jq | 1.6 | JSON processing for dedup URL matching, schema validation, review-to-JSON conversion | Already installed on system, used by Phase 1 validation scripts. [VERIFIED: system check] |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| Claude Code WebSearch | Built-in | Discover new regulatory developments via web search | Government source discovery, supplemental law firm alerts |
| Claude Code WebFetch | Built-in | Fetch full article content from Lexology links and government pages | Following Lexology article links (D-03), direct government page fetches |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| eml-to-html (Python) | eml-parser (npm, v2.1.1) | eml-parser is Node.js and could avoid Python dependency, but user locked decision to use eml-to-html. Could revisit if eml-to-html proves insufficient. [VERIFIED: npm view eml-parser version = 2.1.1] |
| JSON source config | YAML source config | YAML is more human-readable for complex configs but adds a parsing dependency. JSON is native to jq and requires no extra tooling. Recommend JSON. [ASSUMED] |

**Installation:**
```bash
pip install --user eml-to-html
# Verify:
eml-to-html --help
```

**Version verification:**
- eml-to-html: 0.0.2 [VERIFIED: pip dry-run against PyPI on 2026-04-06]
- jq: 1.6 [VERIFIED: system `jq --version`]
- Node.js: v24.14.1 [VERIFIED: system `node --version`]

## Architecture Patterns

### Recommended Project Structure
```
pipeline/
  config/
    sources.json          # Government URLs, search queries, direct fetches (D-09)
  scripts/
    validate-handoff.sh   # Already exists from Phase 1
    convert-eml.sh        # Wrapper: eml-to-html -> output HTML
    run-scanner.sh        # Scanner orchestration entry point
    approve-findings.sh   # Convert reviewed markdown back to JSON
  runs/
    <run-id>/
      scanner-output.json       # Envelope with findings array
      scanner-review.md         # Human-readable review file
      scanner-approved.json     # Post-approval JSON (approved items only)
      scanner-errors.json       # Source failures log (D-08)
input/
  *.eml                  # Raw email digest files
  *.html                 # Pre-converted HTML (optional)
reports/
  privacy/               # Existing reports for dedup checking
  cybersecurity/
  ai-law/
.claude/agents/
  scanner.md             # Full scanner agent prompt (update stub)
```

### Pattern 1: Scanner Agent Prompt as HTML Parser
**What:** The scanner Claude agent receives the full HTML content of the Lexology digest inline (piped or as a file reference) and uses its language understanding to extract structured items -- no CSS selector library needed.
**When to use:** For Lexology digest parsing where the HTML structure is semi-structured email HTML (tables, divs) that Claude can understand natively.
**Rationale:** Claude is extremely capable at extracting structured data from HTML. Writing a brittle CSS selector parser for email HTML that changes format is worse than letting the agent parse it. The agent prompt specifies what to extract (title, link, firm name, summary, tags, section) and the output schema enforces the structure. [ASSUMED -- based on Claude's HTML understanding capability]

**Example agent invocation:**
```bash
# Convert .eml to HTML first
eml-to-html input/digest-2026-04-06.eml
# Resulting HTML is input/digest-2026-04-06.html

# Pipe to scanner agent
cat input/digest-2026-04-06.html | claude -p \
  --agent scanner \
  --output-format json \
  "Parse this Lexology digest HTML. Extract items from privacy, cybersecurity, and AI law sections only. For each item, fetch the full article via the linked URL. Output findings as JSON."
```

### Pattern 2: Source Config File
**What:** A JSON config file defines all sources the scanner should check, categorized by type (direct-fetch, search-query).
**When to use:** For all non-digest scanning (government sites, supplemental law firm searches).
**Example:**
```json
{
  "schema_version": "1.0",
  "sources": {
    "direct_fetch": [
      {
        "id": "ftc-press",
        "name": "FTC Press Releases",
        "url": "https://www.ftc.gov/news-events/news/press-releases",
        "category": ["privacy", "cybersecurity"],
        "extract": "List of recent press release titles and links"
      },
      {
        "id": "nist-news",
        "name": "NIST CSRC News",
        "url": "https://csrc.nist.gov/news",
        "category": ["cybersecurity", "ai-law"],
        "extract": "Recent publications and announcements"
      },
      {
        "id": "congress-privacy",
        "name": "Congress.gov Privacy Bills",
        "url": "https://www.congress.gov/search?q=%7B%22source%22%3A%22legislation%22%2C%22congress%22%3A%22119%22%2C%22type%22%3A%22bills%22%7D&searchResultViewType=expanded",
        "category": ["privacy"],
        "extract": "New bills related to privacy and data protection"
      }
    ],
    "search_queries": [
      {
        "id": "state-privacy-2026",
        "query": "state privacy law legislation 2026 new bill",
        "category": ["privacy"],
        "description": "State-level comprehensive privacy legislation"
      },
      {
        "id": "ftc-enforcement-2026",
        "query": "FTC enforcement action data privacy cybersecurity 2026",
        "category": ["privacy", "cybersecurity"],
        "description": "FTC enforcement actions"
      },
      {
        "id": "ai-regulation-2026",
        "query": "artificial intelligence regulation law executive order 2026 US",
        "category": ["ai-law"],
        "description": "Federal and state AI regulation"
      },
      {
        "id": "nist-ai-2026",
        "query": "NIST AI framework guidance publication 2026",
        "category": ["ai-law", "cybersecurity"],
        "description": "NIST AI-related publications"
      },
      {
        "id": "state-ag-privacy",
        "query": "state attorney general privacy enforcement settlement 2026",
        "category": ["privacy"],
        "description": "State AG enforcement actions"
      }
    ]
  }
}
```

### Pattern 3: Layered Dedup Pipeline
**What:** Three-pass deduplication: URL match -> title similarity -> semantic comparison.
**When to use:** After all findings are collected, before generating the review file.
**Implementation approach:**
1. **Pass 1 (URL match):** Extract URLs from existing reports via grep/jq. Normalize URLs (strip UTM params, trailing slashes, protocol). Exact match = duplicate. Cost: zero (bash/jq). [ASSUMED]
2. **Pass 2 (Title similarity):** Extract titles from existing report frontmatter or first H1. Simple substring/fuzzy match in jq or bash. Flag high-similarity titles. Cost: zero (local). [ASSUMED]
3. **Pass 3 (Semantic):** For remaining candidates, ask Claude to compare each finding summary against recent report summaries. Only invoked for items that pass the first two filters. Cost: token usage per comparison. [ASSUMED]

### Pattern 4: Human Review File Format
**What:** Markdown file with checkboxes that the user edits to approve/reject findings.
**Example:**
```markdown
# Scanner Findings Review

**Pipeline Run:** 2026-04-06T14-30-00
**Scan Date:** 2026-04-06
**Total Findings:** 12
**Sources Scanned:** 8 successful, 1 failed

## Source Failures
- congress.gov bill search: timeout after 30s

## Findings

### 1. [SCAN-20260406-001] FTC Issues New Data Broker Guidance
- [x] Approve
- **Source:** FTC Press Release
- **URL:** https://www.ftc.gov/news-events/...
- **Category:** privacy
- **Relevance:** high
- **Jurisdiction:** Federal
- **Type:** guidance
- **Summary:** The FTC released new guidance on data broker obligations...
- **Notes:** _(user can add notes here)_

---

### 2. [SCAN-20260406-002] Iowa Passes Comprehensive Privacy Law
- [x] Approve
- **Source:** Lexology / Smith & Jones LLP
- **URL:** https://www.lexology.com/library/...
- **Category:** privacy
- **Relevance:** high
- **Jurisdiction:** Iowa
- **Type:** legislation
- **Summary:** Iowa legislature passed HB 1234...
- **Notes:**

---

## APPROVED
<!-- Add this section header when review is complete -->
<!-- Pipeline will not proceed without this marker -->
```

### Anti-Patterns to Avoid
- **Hardcoding source URLs in agent prompt:** Source list changes frequently. Config file (D-09) keeps agent prompt stable.
- **Parsing HTML with regex in bash:** Let the Claude agent parse HTML. It understands document structure better than any regex.
- **Running dedup inside the Claude agent:** Dedup passes 1 and 2 should be done in bash/jq for zero token cost. Only pass 3 needs Claude.
- **Single monolithic scanner invocation:** Break into stages: (1) digest parse, (2) source scan, (3) dedup, (4) review generation. Easier to debug and test.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| .eml to HTML conversion | Custom MIME parser | eml-to-html CLI (Python) | MIME parsing has edge cases (multipart, encoding, attachments). Locked decision D-01. |
| JSON schema validation | Custom bash field checkers | Existing validate-handoff.sh + jq filters | Already built in Phase 1 with envelope.jq and scanner.jq |
| HTML content extraction | BeautifulSoup/cheerio parser | Claude agent with WebFetch | Claude understands HTML structure natively; avoids adding parsing library dependency |
| URL normalization | Custom regex | Simple jq/bash function stripping known params | UTM params, trailing slashes, protocol normalization. Small, well-defined problem. |

**Key insight:** The scanner agent IS the parser. Claude's language understanding replaces traditional HTML parsing libraries. The bash scripts handle orchestration, file I/O, and cost-free dedup passes.

## Common Pitfalls

### Pitfall 1: Lexology Rate Limiting / Blocking
**What goes wrong:** Scanner follows many Lexology links (D-03) in rapid succession, gets rate-limited or blocked.
**Why it happens:** Lexology may have anti-scraping measures. WebFetch has a 15-minute cache but first requests still hit the server.
**How to avoid:** The scanner agent should process links sequentially (not parallel). If a fetch fails, log it and continue (D-08). Consider adding the Fetch MCP server as fallback for chunked reading of large pages.
**Warning signs:** HTTP 429 responses, empty page content, CAPTCHA pages.

### Pitfall 2: Lexology HTML Format Changes
**What goes wrong:** Lexology updates their email template, breaking extraction.
**Why it happens:** Email HTML is not a stable API. Templates change without notice.
**How to avoid:** Use Claude's semantic understanding rather than brittle CSS selectors. The agent prompt should describe WHAT to extract (titles, links, firm names, summaries) not HOW (specific CSS classes). Test with real email samples. [ASSUMED]
**Warning signs:** Scanner returns zero findings from a digest that clearly has content.

### Pitfall 3: Government Site Fetch Failures
**What goes wrong:** WebFetch returns incomplete or no content from government sites (JS-rendered pages, anti-bot measures).
**Why it happens:** Some government sites use JavaScript rendering that WebFetch cannot handle.
**How to avoid:** Start with WebFetch. If specific sites consistently fail, add Playwright MCP server for those sources only. Document which sources need JS rendering in the source config. D-08 ensures graceful degradation.
**Warning signs:** Empty or boilerplate-only content from fetched pages.

### Pitfall 4: Overly Aggressive Dedup
**What goes wrong:** Legitimate new developments get incorrectly flagged as duplicates (D-11 means user never sees them).
**Why it happens:** Title similarity too aggressive; different articles about the same topic but different developments.
**How to avoid:** Set title similarity threshold conservatively (err on the side of showing duplicates). For semantic pass, instruct Claude to distinguish "same development, different coverage" (duplicate) from "same topic, different development" (not duplicate). Consider adding a "potential duplicates" section in the review file for borderline cases. [ASSUMED]
**Warning signs:** User notices gaps in coverage compared to what they see in their email.

### Pitfall 5: Scanner Token Budget Explosion
**What goes wrong:** Scanner agent uses excessive tokens fetching full articles from every Lexology link.
**Why it happens:** D-03 says follow every link. A typical digest might have 20-30 items. Each WebFetch adds significant context.
**How to avoid:** Filter by relevant sections FIRST (D-04), then fetch only relevant articles. This reduces fetches from ~30 to ~5-10. Consider extracting just the first few paragraphs of each article rather than the full text -- the researcher will do deep reading later.
**Warning signs:** Scanner runs taking >5 minutes or costing >$1 per run.

### Pitfall 6: Review Markdown Parsing Fragility
**What goes wrong:** The approve-findings.sh script fails to correctly parse the edited markdown back to JSON.
**Why it happens:** User edits markdown in unexpected ways (changes formatting, adds sections, removes markers).
**How to avoid:** Use a simple, robust parsing approach: each finding has a unique ID (e.g., SCAN-20260406-001). The script looks for `- [x] Approve` or `- [ ] Approve` next to each ID. Everything else is ignored. Test with various edit scenarios. [ASSUMED]
**Warning signs:** Approved items not matching between markdown and JSON.

## Code Examples

### EML Conversion Wrapper Script
```bash
#!/bin/bash
# pipeline/scripts/convert-eml.sh
# Converts .eml file to HTML using eml-to-html Python CLI
set -euo pipefail

INPUT_FILE="$1"
if [ ! -f "$INPUT_FILE" ]; then
  echo "ERROR: File not found: $INPUT_FILE" >&2
  exit 1
fi

# eml-to-html creates .html file alongside the .eml file
eml-to-html "$INPUT_FILE"

# Output the path to the generated HTML
HTML_FILE="${INPUT_FILE%.eml}.html"
if [ -f "$HTML_FILE" ]; then
  echo "$HTML_FILE"
else
  echo "ERROR: Conversion failed, no HTML output" >&2
  exit 1
fi
```
*Source: eml-to-html CLI behavior [VERIFIED: GitHub README]*

### URL Normalization for Dedup
```bash
# Normalize URL: strip UTM params, trailing slash, force https
normalize_url() {
  local url="$1"
  echo "$url" \
    | sed 's|^http://|https://|' \
    | sed 's|[?&]utm_[^&]*||g' \
    | sed 's|[?&]g=[^&]*||g' \
    | sed 's|?$||' \
    | sed 's|/$||'
}
```
*Source: Custom pattern based on D-10 and Lexology URL structure (CONTEXT specifics section) [ASSUMED]*

### Finding ID Generation
```bash
# Generate finding ID: SCAN-YYYYMMDD-NNN
generate_finding_id() {
  local date_part=$(date +%Y%m%d)
  local seq="$1"  # sequence number, zero-padded
  printf "SCAN-%s-%03d" "$date_part" "$seq"
}
```
*Source: Custom pattern [ASSUMED]*

### Approval Marker Check
```bash
#!/bin/bash
# Check if review file has been approved
check_approval() {
  local review_file="$1"
  if grep -q "^## APPROVED" "$review_file"; then
    return 0  # approved
  else
    return 1  # not yet approved
  fi
}
```
*Source: Based on D-14 [ASSUMED]*

## Government Source URLs (Verified)

| Source | URL | Content Type | Notes |
|--------|-----|-------------|-------|
| FTC Press Releases | https://www.ftc.gov/news-events/news/press-releases | Enforcement, guidance | Static HTML, WebFetch should work [VERIFIED: WebSearch confirmed URL] |
| NIST CSRC News | https://csrc.nist.gov/news | Publications, frameworks | Static HTML [VERIFIED: WebSearch confirmed URL] |
| Congress.gov Browse | https://www.congress.gov/browse | Legislation | 119th Congress (2025-2026). Has API but API key required. WebFetch for browse page. [VERIFIED: WebSearch] |
| IAPP State Privacy Tracker | https://iapp.org/resources/article/us-state-privacy-legislation-tracker | State legislation tracker | May require login for full access [VERIFIED: WebSearch] |
| State legislature sites | Various per state | Bills, votes | No single URL; use WebSearch queries per state [ASSUMED] |

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| RSS feeds for regulatory monitoring | Email digests + web scraping | ~2023 | Many government RSS feeds are abandoned; email digests more reliable |
| Dedicated scraping frameworks (Scrapy) | LLM-based extraction from HTML | ~2024-2025 | Claude can parse semi-structured HTML without brittle selectors |
| API-based congress tracking | Congress.gov API v3 (key required) | Current | API exists but requires registration; WebSearch/WebFetch sufficient for scanning |

**Deprecated/outdated:**
- Sunlight Congress API: deprecated, replaced by congress.gov API v3 [VERIFIED: WebSearch results show old Sunlight Labs API]
- Proxycurl for LinkedIn: shut down (Jan 2026 lawsuit, July 2026 closure) [CITED: CLAUDE.md]

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | Claude agent can reliably parse Lexology HTML email format without CSS selectors | Architecture Pattern 1 | Would need to add cheerio/jsdom dependency for programmatic HTML parsing |
| A2 | URL normalization via sed is sufficient for dedup pass 1 | Code Examples | Edge cases in URL formats could cause false negatives in dedup |
| A3 | Title similarity via substring matching in bash is adequate for dedup pass 2 | Architecture Pattern 3 | May need fuzzy matching library if titles vary significantly between sources |
| A4 | Conservative dedup thresholds will prevent false positives in auto-skip (D-11) | Pitfall 4 | Could silently drop legitimate findings the user should see |
| A5 | JSON is better than YAML for source config since jq is already a dependency | Alternatives Considered | YAML would be more readable for non-technical users editing source lists |
| A6 | WebFetch can reliably fetch FTC, NIST, and Congress.gov pages | Government Sources | May need Playwright MCP for JS-rendered pages |
| A7 | Review markdown parsing via grep for checkbox + ID is robust enough | Pitfall 6 | Users might edit markdown in unexpected ways that break parsing |

## Open Questions

1. **Lexology HTML structure**
   - What we know: Items have title (linked), firm name, summary snippet, tags. Organized by sections.
   - What's unclear: Exact HTML element structure, CSS classes, whether format is consistent across digests.
   - Recommendation: User provides a sample .eml file before implementation. Build and test against real data.

2. **Congress.gov API key vs WebFetch**
   - What we know: Congress.gov has a free API (v3) requiring registration. Rate limit: 5000/hr. [VERIFIED: WebSearch]
   - What's unclear: Whether WebFetch on the browse page provides enough information, or if API access would be significantly better.
   - Recommendation: Start with WebFetch/WebSearch. If insufficient, register for API key as enhancement.

3. **eml-to-html output quality**
   - What we know: Package exists on PyPI, version 0.0.2, MIT license, 36 GitHub stars. [VERIFIED: pip + GitHub]
   - What's unclear: How well it handles Lexology's specific .eml format (multipart MIME, embedded images, encoding).
   - Recommendation: Test with a real Lexology .eml file early. If conversion is poor, user can manually save the email as HTML from their email client as a workaround.

4. **Dedup semantic pass token cost**
   - What we know: Pass 3 requires Claude to compare findings against existing reports.
   - What's unclear: How many comparisons will be needed in practice (depends on report volume and pass 1+2 effectiveness).
   - Recommendation: Initially skip pass 3. Implement passes 1 and 2 first. Add semantic pass only if duplicates slip through.

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| Python 3 | eml-to-html | Yes | 3.10.12 | User manually saves email as HTML |
| pip | eml-to-html install | Yes | (system) | pipx or manual download |
| jq | Dedup, JSON processing, validation | Yes | 1.6 | -- (critical dependency) |
| Node.js | Potential MCP servers | Yes | v24.14.1 | -- |
| Claude Code CLI | Scanner agent invocation | Yes | v2.1.92 | -- (core dependency) |
| eml-to-html | .eml conversion (D-01) | No (not installed) | 0.0.2 available | pip install --user eml-to-html |

**Missing dependencies with no fallback:**
- None -- all critical dependencies are available or installable.

**Missing dependencies with fallback:**
- eml-to-html: not yet installed, but pip install is straightforward. Fallback: user saves email as HTML directly.

## Validation Architecture

### Test Framework
| Property | Value |
|----------|-------|
| Framework | Bash test scripts (established in Phase 1) |
| Config file | tests/run-all.sh (test runner) |
| Quick run command | `bash tests/run-all.sh` |
| Full suite command | `bash tests/run-all.sh` |

### Phase Requirements to Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| SCAN-01 | Parse Lexology HTML digest, extract findings | integration | `bash tests/test-digest-parse.sh` | No -- Wave 0 |
| SCAN-02 | Query government sources, return developments | manual-only | Manual: requires live web access | N/A |
| SCAN-03 | Query law firm alert sources | manual-only | Manual: requires live web access | N/A |
| SCAN-04 | Detect duplicates against existing reports | unit | `bash tests/test-dedup.sh` | No -- Wave 0 |
| SCAN-05 | Output structured findings for review | unit | `bash tests/test-review-output.sh` | No -- Wave 0 |
| PIPE-03 | Human approval gate blocks pipeline | unit | `bash tests/test-approval-gate.sh` | No -- Wave 0 |

### Sampling Rate
- **Per task commit:** `bash tests/run-all.sh`
- **Per wave merge:** `bash tests/run-all.sh`
- **Phase gate:** Full suite green before `/gsd-verify-work`

### Wave 0 Gaps
- [ ] `tests/test-digest-parse.sh` -- test HTML parsing with sample Lexology HTML fixture
- [ ] `tests/test-dedup.sh` -- test URL match, title similarity against fixture reports
- [ ] `tests/test-review-output.sh` -- test review markdown generation and JSON output
- [ ] `tests/test-approval-gate.sh` -- test approval marker detection and JSON conversion
- [ ] `tests/fixtures/sample-lexology-digest.html` -- real or synthetic Lexology HTML for testing
- [ ] `tests/fixtures/sample-reports/` -- fixture reports directory for dedup testing
- [ ] `tests/fixtures/sample-review-approved.md` -- review file with approval marker
- [ ] `tests/fixtures/sample-review-pending.md` -- review file without approval marker

## Security Domain

### Applicable ASVS Categories

| ASVS Category | Applies | Standard Control |
|---------------|---------|-----------------|
| V2 Authentication | No | N/A -- local CLI tool, no user auth |
| V3 Session Management | No | N/A |
| V4 Access Control | No | N/A -- single user, local filesystem |
| V5 Input Validation | Yes | jq schema validation on all JSON; scanner schema enforces field types and enums |
| V6 Cryptography | No | N/A |

### Known Threat Patterns for CLI + Web Scraping Stack

| Pattern | STRIDE | Standard Mitigation |
|---------|--------|---------------------|
| Malicious content in fetched web pages | Tampering | Claude processes content in sandboxed context; no code execution from fetched content |
| URL injection via crafted email digest | Tampering | Scanner validates URLs before fetching; normalize and sanitize |
| Large page denial (memory exhaustion) | Denial of Service | WebFetch has built-in limits; Fetch MCP supports chunked reading |

## Sources

### Primary (HIGH confidence)
- Phase 1 artifacts: `.claude/agents/scanner.md`, `pipeline/schemas/scanner.schema.json`, `pipeline/schemas/envelope.schema.json`, `pipeline/scripts/validate-handoff.sh` -- established infrastructure
- npm registry: verified eml-parser v2.1.1, eml-format v0.6.1 exist as alternatives
- PyPI: verified eml-to-html v0.0.2 installable via pip
- GitHub dunnkers/eml-to-html: confirmed Python CLI tool, MIT license

### Secondary (MEDIUM confidence)
- [FTC Press Releases URL](https://www.ftc.gov/news-events/news/press-releases) -- confirmed via WebSearch
- [NIST CSRC News](https://csrc.nist.gov/news) -- confirmed via WebSearch
- [Congress.gov API](https://github.com/LibraryOfCongress/api.congress.gov) -- API v3, key required, 5000 req/hr
- [IAPP State Privacy Tracker](https://iapp.org/resources/article/us-state-privacy-legislation-tracker) -- comprehensive tracker

### Tertiary (LOW confidence)
- Lexology email HTML structure -- no public documentation; must reverse-engineer from samples
- State legislature site accessibility via WebFetch -- varies by state, untested

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH -- minimal dependencies, all verified installable
- Architecture: MEDIUM-HIGH -- patterns are sound but Lexology HTML parsing is untested
- Pitfalls: MEDIUM -- based on common web scraping patterns and Claude Code experience
- Government sources: MEDIUM -- URLs verified but actual fetchability not tested

**Research date:** 2026-04-06
**Valid until:** 2026-05-06 (30 days -- government URLs stable, Lexology format could change)
