# Phase 3: Report Generation - Research

**Researched:** 2026-04-06
**Domain:** Claude Code agent system prompts, markdown report templates, bash orchestration
**Confidence:** HIGH

## Summary

Phase 3 fills the researcher agent stub (`.claude/agents/researcher.md`) with a complete system prompt, creates two markdown report templates (client-alert and research-memo), builds the orchestration script (`run-researcher.sh`) that invokes the researcher on each approved finding, and adds test fixtures and validation scripts for the researcher output schema. The infrastructure is already in place from Phase 1 -- schemas, validation, envelope format, and directory structure all exist. This phase is primarily about content: what the researcher agent should do, how reports should look, and how to wire the approved findings into the researcher invocation.

The technical risk is low. The patterns are established by Phase 2's scanner implementation: a bash script reads approved findings JSON, constructs a prompt, invokes `claude -p --agent researcher`, validates the output. The novel parts are (1) the researcher's system prompt which must encode complex research instructions including source hierarchy, confidence tagging, and format selection logic, and (2) the report templates which define the markdown structure for both formats.

**Primary recommendation:** Follow the scanner pattern exactly for orchestration. Focus implementation effort on the researcher system prompt quality and report template design -- these are the value-bearing artifacts.

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions
- **D-01:** Two distinct report formats -- client-alert (short, executive-friendly, action-oriented, 1-2 pages) and research-memo (long, technical, analytical, 3-5+ pages). Each has a different template with different sections.
- **D-02:** Format-dependent sections:
  - **Client-alert:** Title, Summary, Key Facts, Action Items, Source Citations, Related Reports, Jurisdiction Tags
  - **Research-memo:** Title, Executive Summary, Background, Detailed Analysis, Impact Assessment, Action Items, Source Citations, Related Reports, Jurisdiction Tags
- **D-03:** Format selection is relevance-based: HIGH relevance findings produce client-alerts (urgent, notify now). MEDIUM/LOW relevance findings produce research-memos (deeper background analysis).
- **D-04:** Source citations use both inline markdown links for readability AND a deduplicated Sources section at the bottom listing all URLs used.
- **D-05:** Research depth is format-dependent: client-alerts get primary source + 1-2 verification sources (fast). Research-memos get deep research with 5-10 sources (thorough: official text, legislative history, enforcement precedents, affected industry analysis).
- **D-06:** Researcher MUST always locate and cite official legal text (statute, regulation, rule from congress.gov, state legislature, CFR) when a finding references legislation. This is non-negotiable for legal accuracy.
- **D-07:** Confidence levels determined by source quality + verification combined:
  - **HIGH:** Official government source, court filing, statute text -- OR any claim corroborated by 2+ independent authoritative sources
  - **MEDIUM:** Single reputable law firm analysis or major news outlet
  - **LOW:** Secondary reporting, opinion pieces, unverified social media, uncorroborated non-authoritative source
- **D-08:** Confidence tags applied at the section/paragraph level (e.g., "### Key Facts [HIGH confidence]"), not per individual claim. Clean reading without cluttering the prose.
- **D-09:** Researcher reads recent reports in the same category using Claude semantic search to assess thematic similarity. Picks the truly related ones -- not just keyword matches.
- **D-10:** Related Reports section format is at Claude's discretion. Must link related reports with clear connection explanation.

### Claude's Discretion
- Exact report markdown template styling and formatting details
- Related Reports section format (simple list, annotated list, or other)
- WebSearch query design for finding official legal texts
- How many reports to compare for Related Reports (3-5 in same category is reasonable)
- Report filename convention (e.g., `jurisdiction-topic-date.md`)
- Orchestration script details for running researcher on batches of approved findings

### Deferred Ideas (OUT OF SCOPE)
None -- discussion stayed within phase scope
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| REPT-01 | Researcher agent produces structured markdown reports with source citations and jurisdiction tags | Researcher system prompt with citation rules (D-04, D-06), report templates with Jurisdiction Tags section (D-02), researcher.schema.json already has jurisdiction_tags array |
| REPT-02 | Researcher agent selects format based on development type (client alert for breaking news, research memo for complex analysis) | Format selection logic in system prompt keyed on scanner finding `relevance` field (D-03): high=client-alert, medium/low=research-memo |
| REPT-03 | Each factual claim in report is tagged with confidence level (HIGH/MEDIUM/LOW) based on source quality | Confidence tagging rules in system prompt (D-07, D-08), section-level tags, confidence_summary in researcher output schema |
| REPT-04 | Finalized reports include a "Related Reports" section linking similar developments in the knowledge base | Related Reports logic using Glob+Read to scan existing reports in same category directory (D-09, D-10) |
</phase_requirements>

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| Claude Code CLI (`claude`) | 2.1.92 | Agent runtime for researcher subprocess | Project constraint. Already installed. [VERIFIED: `claude --version` on system] |
| Bash | System default | Orchestration script (`run-researcher.sh`) | Matches Phase 2 scanner pattern. No external dependencies. [VERIFIED: existing `run-scanner.sh`] |
| jq | System default | JSON parsing in orchestration script, output validation | Already used by `validate-handoff.sh` and `approve-findings.sh`. [VERIFIED: existing scripts] |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| Built-in WebSearch | Claude Code built-in | Researcher discovers sources during report writing | Always available, no config needed. [VERIFIED: scanner agent uses it] |
| Built-in WebFetch | Claude Code built-in | Researcher fetches full content from URLs | For reading official legal texts, law firm analyses. [VERIFIED: scanner agent uses it] |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| Markdown templates as inline system prompt | Separate template files read by agent | Templates inline in system prompt are simpler, avoid extra Read calls. Separate files only needed if templates change frequently without system prompt changes. Recommend inline. |
| Per-finding researcher invocation | Batch all findings in one researcher call | Per-finding gives better isolation (one failure doesn't lose all reports) and matches D-12 from Phase 1 (batch processing means all through researcher stage, but individual invocations). Recommend per-finding. |

**Installation:**
```bash
# No installation needed -- all tools already available
```

## Architecture Patterns

### Recommended Project Structure (new files this phase creates)
```
.claude/agents/
  researcher.md          # Full system prompt (UPDATE existing stub)
pipeline/scripts/
  run-researcher.sh      # Orchestration script (NEW)
pipeline/templates/
  client-alert.md        # Report template (NEW directory + file)
  research-memo.md       # Report template (NEW file)
reports/
  privacy/               # Researcher writes reports here (EXISTS)
  cybersecurity/          # (EXISTS)
  ai-law/                # (EXISTS)
tests/
  fixtures/
    sample-approved-findings.json  # Test fixture (NEW)
    sample-researcher-output.json  # Test fixture (NEW)
    sample-reports/
      client-alert-sample.md       # Expected output sample (NEW)
      research-memo-sample.md      # Expected output sample (NEW)
  test-researcher-validation.sh    # Test script (NEW)
```

### Pattern 1: Per-Finding Researcher Invocation
**What:** The orchestration script iterates over approved findings and invokes `claude -p --agent researcher` once per finding, writing one report per call. [VERIFIED: matches `run-scanner.sh` pattern]
**When to use:** Always -- this is the standard pipeline pattern.
**Example:**
```bash
# Source: existing run-scanner.sh pattern adapted for researcher
FINDING_COUNT=$(jq '.data.findings | length' "$APPROVED_FILE")
for i in $(seq 0 $((FINDING_COUNT - 1))); do
  FINDING_JSON=$(jq -c ".data.findings[$i]" "$APPROVED_FILE")
  FINDING_ID=$(echo "$FINDING_JSON" | jq -r '.id')
  
  RESEARCHER_PROMPT="Research this finding and write a report."
  RESEARCHER_PROMPT="$RESEARCHER_PROMPT Pipeline run ID: $RUN_ID."
  RESEARCHER_PROMPT="$RESEARCHER_PROMPT Finding data: $FINDING_JSON"
  RESEARCHER_PROMPT="$RESEARCHER_PROMPT Write the report to: reports/{category}/{filename}.md"
  RESEARCHER_PROMPT="$RESEARCHER_PROMPT Write your output metadata to: $RUN_DIR/researcher-$FINDING_ID.json"
  
  claude -p --agent researcher --output-format json \
    --max-turns 30 \
    "$RESEARCHER_PROMPT"
done
```

### Pattern 2: Format Selection from Scanner Finding
**What:** The researcher reads the `relevance` field from the scanner finding to choose format. No separate decision logic needed -- it's a direct mapping. [VERIFIED: D-03 from CONTEXT.md, scanner schema has relevance enum]
**When to use:** Every report generation.
**Example:**
```bash
# In system prompt instructions:
# If finding.relevance == "high" -> use client-alert format
# If finding.relevance == "medium" or "low" -> use research-memo format
```

### Pattern 3: Report Filename Convention
**What:** Reports named `{jurisdiction}-{topic-slug}-{date}.md` in the category directory.
**When to use:** Every report. Provides sortable, scannable filenames.
**Example:**
```
reports/privacy/federal-apra-privacy-act-2026-04-06.md
reports/cybersecurity/california-ccpa-enforcement-2026-04-06.md
reports/ai-law/colorado-ai-act-2026-04-06.md
```

### Pattern 4: Confidence Summary Counting
**What:** After writing the report, researcher counts section-level confidence tags to produce the `confidence_summary` object in JSON output. [VERIFIED: researcher.schema.json requires high/medium/low integer counts]
**When to use:** Every researcher output JSON.

### Pattern 5: Related Reports Discovery
**What:** Researcher uses Glob to list existing `.md` files in `reports/{category}/`, reads their titles and summaries, and identifies thematically related ones. The agent's built-in semantic understanding handles relevance better than keyword matching. [VERIFIED: D-09 specifies "Claude semantic search"]
**When to use:** Every report, after the main content is written.

### Anti-Patterns to Avoid
- **Batching all findings into one researcher call:** One failure loses all reports. Per-finding isolation is safer and matches the per-finding report output pattern.
- **Hardcoding report templates in the orchestration script:** Templates belong in the system prompt or template files, not the bash script. The bash script only handles invocation mechanics.
- **Using grep for Related Reports:** Keyword matching misses semantic connections. The researcher agent (opus model) should read existing report summaries and use its understanding to find related content.
- **Skipping official legal text lookup:** D-06 is non-negotiable. The system prompt must make this a hard requirement, not a suggestion.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| JSON validation | Custom jq logic per schema | Existing `validate-handoff.sh` + `researcher.jq` | Already built in Phase 1, validates envelope + stage-specific data [VERIFIED: researcher.jq exists] |
| Pipeline run tracking | Custom state management | Timestamped run directories (`pipeline/runs/`) | Pattern established in Phase 1, used by scanner [VERIFIED: run-scanner.sh creates these] |
| Report deduplication | Custom dedup logic | Scanner dedup already handles this upstream | Researcher receives pre-deduped approved findings [VERIFIED: dedup-findings.sh runs before approval] |
| Web content extraction | Custom HTML parsing | Claude Code built-in WebFetch | Handles HTML-to-markdown conversion server-side [VERIFIED: CLAUDE.md documents this] |

## Common Pitfalls

### Pitfall 1: Researcher Agent Prompt Too Long
**What goes wrong:** System prompt exceeds effective attention window, agent ignores later instructions.
**Why it happens:** Report templates, confidence rules, citation rules, related-reports logic, format selection -- all in one prompt.
**How to avoid:** Structure the system prompt with clear sections and use markdown headers. Put the most critical rules (D-06 official legal text, D-07 confidence levels) early. Put template structures as reference sections at the end. The researcher reads templates from files if they're too large for inline.
**Warning signs:** Agent produces reports missing required sections or ignoring confidence tagging.

### Pitfall 2: WebSearch/WebFetch Failures During Research
**What goes wrong:** Government sites are slow or block automated requests. Researcher can't find official legal text.
**Why it happens:** WebFetch has 15-minute cache but some sites have anti-bot measures or are intermittently unavailable.
**How to avoid:** System prompt must instruct: if official text can't be fetched, note it explicitly in the report with LOW confidence tag and include the URL for manual verification. Never fabricate a citation.
**Warning signs:** Reports with inline links that 404 or lead to wrong pages.

### Pitfall 3: Confidence Summary Mismatch
**What goes wrong:** The JSON `confidence_summary` counts don't match the actual confidence tags in the markdown report.
**Why it happens:** Researcher writes the report, then separately writes JSON output, and miscounts.
**How to avoid:** System prompt instructs researcher to re-read the report and count tags before writing JSON. Or: write JSON last, after the report is final.
**Warning signs:** Validation passes (schema is valid) but counts are wrong (semantic error, not structural).

### Pitfall 4: Related Reports Section Empty on First Run
**What goes wrong:** First pipeline run has no existing reports, so Related Reports is always "None."
**Why it happens:** Knowledge base starts empty.
**How to avoid:** System prompt handles this gracefully: "If no related reports exist in the knowledge base, state 'No related reports found -- this is among the first reports in the knowledge base.'"
**Warning signs:** Not a real problem -- just ensure the template handles the empty case.

### Pitfall 5: Finding JSON Too Large for CLI Argument
**What goes wrong:** Bash argument length limit exceeded when passing finding JSON inline.
**Why it happens:** Scanner summary fields can be 2-4 sentences each, finding JSON can be 500+ characters.
**How to avoid:** Write finding data to a temporary file and tell the researcher to read it, rather than passing inline. Or reference the approved findings file with an index. The scanner script passes a file path, not inline data.
**Warning signs:** Bash "Argument list too long" error.

## Code Examples

### Orchestration Script Structure (following run-scanner.sh pattern)
```bash
# Source: existing run-scanner.sh adapted for researcher
#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

RUN_ID="${1:?ERROR: Must provide run-id as first argument}"
RUN_DIR="$PROJECT_ROOT/pipeline/runs/$RUN_ID"
APPROVED_FILE="$RUN_DIR/scanner-approved.json"

# Validate input exists
if [ ! -f "$APPROVED_FILE" ]; then
  echo "ERROR: Approved findings not found: $APPROVED_FILE" >&2
  exit 1
fi

# Count findings
FINDING_COUNT=$(jq '.data.findings | length' "$APPROVED_FILE")
echo "Processing $FINDING_COUNT approved findings..."

# Process each finding
REPORTS=()
for i in $(seq 0 $((FINDING_COUNT - 1))); do
  FINDING_ID=$(jq -r ".data.findings[$i].id" "$APPROVED_FILE")
  echo "Researching: $FINDING_ID"
  
  # Build prompt referencing the file, not inline data
  PROMPT="Research finding index $i from $APPROVED_FILE"
  PROMPT="$PROMPT Pipeline run ID: $RUN_ID."
  PROMPT="$PROMPT Write output metadata to: $RUN_DIR/researcher-$FINDING_ID.json"
  
  claude -p --agent researcher --output-format json \
    --max-turns 30 \
    "$PROMPT"
  
  # Validate output
  OUTPUT="$RUN_DIR/researcher-$FINDING_ID.json"
  "$PROJECT_ROOT/pipeline/scripts/validate-handoff.sh" researcher "$OUTPUT"
done
```

### Report Template: Client-Alert Format (D-02)
```markdown
---
finding_id: {finding_id}
format: client-alert
date: {date}
jurisdiction: {jurisdiction}
category: {category}
development_type: {development_type}
---

# {Title}

**Jurisdiction:** {jurisdiction_tags}  |  **Category:** {category}  |  **Date:** {date}

## Summary [confidence level]

{2-3 sentence executive summary of the development and its significance}

## Key Facts [confidence level]

- {Fact 1 with [inline source link](url)}
- {Fact 2 with [inline source link](url)}
- {Fact 3}

## Action Items

- {What affected organizations should do}
- {Deadlines or timelines to note}

## Related Reports

- [{Related report title}](relative/path/to/report.md) -- {connection explanation}

## Sources

1. [{Source name}]({url}) -- {what this source provides}
2. [{Source name}]({url}) -- {what this source provides}
```

### Report Template: Research-Memo Format (D-02)
```markdown
---
finding_id: {finding_id}
format: research-memo
date: {date}
jurisdiction: {jurisdiction}
category: {category}
development_type: {development_type}
---

# {Title}

**Jurisdiction:** {jurisdiction_tags}  |  **Category:** {category}  |  **Date:** {date}

## Executive Summary [confidence level]

{3-5 sentence overview for busy readers}

## Background [confidence level]

{Context: what led to this development, legislative/regulatory history}

## Detailed Analysis [confidence level]

{In-depth examination of the development, key provisions, legal basis}
{Multiple paragraphs with [inline citations](url)}

## Impact Assessment [confidence level]

{Who is affected, how, and when}
{Industry implications, compliance requirements}

## Action Items

- {Recommended actions}
- {Compliance deadlines}
- {Monitoring points}

## Related Reports

- [{Related report title}](relative/path/to/report.md) -- {connection explanation}

## Sources

1. [{Source name}]({url}) -- {what this source provides}
2. [{Source name}]({url}) -- {what this source provides}
```

### Researcher Output JSON (matching existing schema)
```json
{
  "schema_version": "1.0",
  "pipeline_run_id": "2026-04-06T14-30-00",
  "timestamp": "2026-04-06T15:00:00Z",
  "stage": "researcher",
  "status": "complete",
  "data": {
    "reports": [
      {
        "finding_id": "SCAN-20260406-001",
        "report_path": "reports/privacy/federal-apra-privacy-act-2026-04-06.md",
        "format": "client-alert",
        "jurisdiction_tags": ["Federal"],
        "confidence_summary": {
          "high": 2,
          "medium": 1,
          "low": 0
        }
      }
    ]
  }
}
```

## Validation Architecture

### Test Framework
| Property | Value |
|----------|-------|
| Framework | Bash test scripts (custom, matching Phase 1/2 pattern) |
| Config file | `tests/run-all.sh` (existing test runner) |
| Quick run command | `bash tests/test-researcher-validation.sh` |
| Full suite command | `bash tests/run-all.sh` |

### Phase Requirements to Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| REPT-01 | Researcher output JSON validates against researcher.schema.json with report_path and jurisdiction_tags | unit | `bash tests/test-researcher-validation.sh` | No -- Wave 0 |
| REPT-02 | Format field matches relevance-based selection (high->client-alert, medium/low->research-memo) | unit | `bash tests/test-researcher-validation.sh` (format check section) | No -- Wave 0 |
| REPT-03 | Confidence summary counts are non-negative integers and present in output | unit | `bash tests/test-researcher-validation.sh` (confidence section) | No -- Wave 0 |
| REPT-04 | Report markdown contains "## Related Reports" section header | unit | `bash tests/test-researcher-validation.sh` (report content check) | No -- Wave 0 |

### Sampling Rate
- **Per task commit:** `bash tests/test-researcher-validation.sh`
- **Per wave merge:** `bash tests/run-all.sh`
- **Phase gate:** Full suite green before `/gsd-verify-work`

### Wave 0 Gaps
- [ ] `tests/fixtures/sample-approved-findings.json` -- approved findings input fixture
- [ ] `tests/fixtures/sample-researcher-output.json` -- valid researcher output fixture
- [ ] `tests/fixtures/sample-reports/client-alert-sample.md` -- sample client-alert report
- [ ] `tests/fixtures/sample-reports/research-memo-sample.md` -- sample research-memo report
- [ ] `tests/test-researcher-validation.sh` -- covers REPT-01 through REPT-04

## Security Domain

### Applicable ASVS Categories

| ASVS Category | Applies | Standard Control |
|---------------|---------|-----------------|
| V2 Authentication | No | N/A -- local CLI, no auth |
| V3 Session Management | No | N/A -- stateless CLI invocations |
| V4 Access Control | No | N/A -- single-user local filesystem |
| V5 Input Validation | Yes | jq-based schema validation via `validate-handoff.sh` at every stage boundary [VERIFIED: existing pattern] |
| V6 Cryptography | No | N/A -- no secrets handled |

### Known Threat Patterns

| Pattern | STRIDE | Standard Mitigation |
|---------|--------|---------------------|
| Prompt injection via scanner finding data | Tampering | Researcher reads finding data from validated JSON file, not user-controlled free text. Scanner findings are pre-validated against schema. [VERIFIED: approve-findings.sh validates IDs against source data] |
| Hallucinated citations | Information Disclosure | Confidence tagging (D-07) + reviewer verification (Phase 4) catch fabricated sources. System prompt explicitly forbids fabricating URLs. |
| Path traversal in report_path | Tampering | Orchestration script validates report_path starts with `reports/` and category is one of the three known values. |

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | YAML frontmatter in report markdown files will be useful for downstream processing (categorizer, search) | Code Examples (templates) | LOW -- frontmatter is optional metadata, can be removed if not needed. Categorizer phase (5) may prefer different metadata format. |
| A2 | `claude -p --agent researcher` with `--max-turns 30` is sufficient for deep research + report writing | Architecture Patterns | MEDIUM -- opus model doing WebSearch + WebFetch + report writing may need more turns for research-memo format. Monitor and adjust. |
| A3 | Passing finding index + file path to researcher is better than inline JSON | Pitfall 5 | LOW -- both approaches work, but file reference avoids argument length limits. |

## Open Questions

1. **Researcher budget cap**
   - What we know: D-03 from Phase 1 says "no budget caps initially." CLAUDE.md suggests `--max-budget-usd 3.00` per finding.
   - What's unclear: Whether to add budget caps now or wait until actual usage is observed.
   - Recommendation: Skip budget caps for now per D-03. Add monitoring (log token usage from `--output-format json` response) so caps can be set later with data.

2. **Report frontmatter format**
   - What we know: YAML frontmatter is conventional for markdown files used as knowledge bases (Obsidian, Jekyll, Hugo).
   - What's unclear: Whether downstream phases (categorizer, search) will use frontmatter.
   - Recommendation: Include frontmatter -- it's low cost and high future value. The categorizer can read it in Phase 5.

3. **Multiple reports per researcher call vs. one-at-a-time**
   - What we know: D-12 says "batch processing" meaning all findings go through researcher stage, but the invocation pattern (per-finding vs. all-at-once) is a Claude's Discretion item.
   - What's unclear: Whether opus can handle multiple findings in one context window effectively.
   - Recommendation: One finding per researcher invocation. Better isolation, clearer error handling, matches the per-report output pattern.

## Sources

### Primary (HIGH confidence)
- Existing codebase: `.claude/agents/researcher.md`, `pipeline/schemas/researcher.schema.json`, `pipeline/schemas/researcher.jq` -- verified current state of researcher infrastructure
- Existing codebase: `pipeline/scripts/run-scanner.sh`, `pipeline/scripts/approve-findings.sh` -- verified orchestration and data flow patterns
- Existing codebase: `pipeline/schemas/scanner.schema.json` -- verified scanner finding fields that serve as researcher input
- `.planning/phases/03-report-generation/03-CONTEXT.md` -- all implementation decisions (D-01 through D-10)
- `.planning/phases/01-agent-framework/01-CONTEXT.md` -- pipeline architecture decisions
- `CLAUDE.md` -- technology stack, model assignments, CLI patterns

### Secondary (MEDIUM confidence)
- Claude Code CLI reference (documented in CLAUDE.md) -- `--agent`, `--output-format json`, `--max-turns` flags

### Tertiary (LOW confidence)
- None -- all research based on verified codebase artifacts and locked decisions

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH -- all tools are already in use by Phase 2 scanner, verified on system
- Architecture: HIGH -- following established patterns from Phase 1/2 with minor adaptations
- Pitfalls: MEDIUM -- based on general LLM agent experience, not project-specific incidents yet

**Research date:** 2026-04-06
**Valid until:** 2026-05-06 (stable -- infrastructure patterns unlikely to change)
