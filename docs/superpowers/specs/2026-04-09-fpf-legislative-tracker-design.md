# FPF Legislative Bill Tracking System — Design Spec

**Date:** 2026-04-09
**Status:** Approved

## Context

Zwiad monitors regulatory developments via a multi-agent pipeline (scanner → researcher → reviewer → categorizer). It currently processes Lexology law firm digest emails and web sources.

FPF (Future of Privacy Forum) sends weekly legislative tracking emails in two flavors: "U.S. AI Legislation Update" and "U.S. Privacy Legislation Updates." These emails contain structured bill-by-bill tracking across US states: bill identifiers, sponsors, status, summaries, and links to bill text on state legislature websites.

The goal is to add a parallel processing path that extracts bill data from FPF emails, downloads bill text PDFs from state sites, converts them to markdown via docling, and maintains a persistent bill library with status tracking over time.

## Architecture Overview

**Approach:** New parallel pipeline integrated with existing infrastructure. FPF emails are detected and routed to a dedicated `fpf-scanner` agent. Bill downloads and conversion are handled by a Python tool (`bill_processor.py`). A persistent `tracker.json` maintains bill state across runs.

**Key decisions:**
- Unified bill library (AI + Privacy bills in one tracker, tagged by category)
- Auto-processing without approval gate (FPF is a trusted source)
- Chronological email processing to build tracker history
- Three-tier bill download: FPF link → state config pattern → agent fallback
- Docling for PDF-to-markdown conversion (installed successfully on aarch64)

## Directory Structure

### Bill Library

```
bills/
  tracker.json                    # Master bill index
  {state_lowercase}/              # e.g., bills/oregon/
    {BILL_TYPE}-{NUMBER}/         # e.g., bills/oregon/SB-1546/
      metadata.json               # Full bill metadata + status history
      current.md                  # Symlink → latest version markdown
      versions/
        v1-introduced.pdf         # Original PDF
        v1-introduced.md          # Docling-converted markdown
        v2-amended.pdf            # Amended version
        v2-amended.md
```

### Pipeline Artifacts (per run)

```
pipeline/runs/{run_id}/
  emails/
    {subject}-{N}.html            # Email body (existing)
    {subject}-{N}.meta.json       # NEW: sender, subject, date sidecar
  fpf-scanner-output.json         # FPF scanner extracted bills
  fpf-bills-processed.json        # Download/conversion results
```

### New Config Files

```
pipeline/config/
  states.json                     # Per-state bill download strategies
```

### New Agent

```
.claude/agents/
  fpf-scanner.md                  # FPF email parser agent
```

### New Python Tools

```
tools/
  bill_processor.py               # Bill download + docling convert + tracker update
```

## Data Model

### tracker.json

```json
{
  "schema_version": "1.0",
  "last_updated": "2026-04-09T12:00:00Z",
  "bills": {
    "OR-SB-1546-2026": {
      "bill_identifier": "SB 1546",
      "state": "Oregon",
      "state_abbrev": "OR",
      "session": "2026",
      "title": "AI Companion Chatbot Regulation",
      "category": ["ai-law"],
      "topics": ["chatbots", "minors-protection"],
      "sponsors": ["Sen. Floyd Prozanski (D)"],
      "current_status": "signed",
      "bill_dir": "bills/oregon/SB-1546",
      "current_version": "v2-enrolled",
      "download_status": "success",
      "bill_text_url": "https://olis.oregonlegislature.gov/...",
      "status_history": [
        {
          "date": "2026-01-15",
          "status": "introduced",
          "detail": "Introduced by Sen. Prozanski",
          "source_email_date": "2026-01-22",
          "source_run_id": "2026-04-09T12-00-00"
        }
      ],
      "versions": [
        {
          "version_id": "v1-introduced",
          "date": "2026-01-15",
          "pdf_path": "bills/oregon/SB-1546/versions/v1-introduced.pdf",
          "md_path": "bills/oregon/SB-1546/versions/v1-introduced.md"
        }
      ],
      "first_seen_run": "2026-04-09T12-00-00",
      "last_updated_run": "2026-04-09T15-00-00"
    }
  }
}
```

**Bill key format:** `{STATE_ABBREV}-{BILL_TYPE}-{NUMBER}-{SESSION}`

### Status Vocabulary

`introduced` | `in-committee` | `passed-committee` | `passed-first-chamber` | `passed-second-chamber` | `enrolled` | `signed` | `vetoed` | `dead` | `tabled` | `amended`

### Per-Bill metadata.json

Same structure as the tracker entry for the bill. Serves as a self-contained record alongside the bill text files.

## Agent: fpf-scanner

**File:** `.claude/agents/fpf-scanner.md`
**Model:** sonnet
**Tools:** WebSearch, WebFetch, Read, Write, Glob, Grep

**Input:** Paths to FPF email HTML files in `pipeline/runs/{run_id}/emails/`

**Behavior:**
1. Read each FPF email HTML file
2. Identify the email type (AI Legislation or Privacy Legislation) from subject/content
3. Parse the email structure — FPF uses HTML tables with state-organized sections:
   - "Highlights" section with key movements
   - "Stuff from the States" section with alphabetical state-by-state bill listings
   - "Federal" section for congressional bills
4. For each bill entry, extract:
   - Bill identifier (e.g., "SB 1546", "HB 2225")
   - State name
   - Session year
   - Title/summary
   - Current status (from description text: "introduced", "passed", "signed", etc.)
   - Status detail (e.g., "Passed Senate 26-1 on March 5")
   - Sponsor(s) with party affiliation
   - Category: ai-law, privacy, or both
   - Topic tags (chatbots, health, liability, employment, etc.)
   - FPF link to bill text (the informz.net redirect URL)
5. Read `bills/tracker.json` to determine which bills are new vs. status updates
6. Output `fpf-scanner-output.json`

**Output Schema** (`fpf-scanner-output.json`):
```json
{
  "schema_version": "1.0",
  "pipeline_run_id": "{run_id}",
  "timestamp": "ISO 8601",
  "stage": "fpf-scanner",
  "status": "complete",
  "data": {
    "email_files_processed": ["path1.html", "path2.html"],
    "email_dates": ["2026-01-22", "2026-01-23"],
    "bills": [
      {
        "id": "FPF-YYYYMMDD-NNN",
        "bill_identifier": "SB 1546",
        "state": "Oregon",
        "state_abbrev": "OR",
        "session": "2026",
        "title": "AI Companion Chatbot Regulation",
        "summary": "...",
        "status": "introduced",
        "status_detail": "Introduced by Sen. Prozanski (D)",
        "last_action_date": "2026-01-15",
        "bill_text_url": "https://FPF.informz.net/z/...",
        "category": ["ai-law"],
        "topics": ["chatbots"],
        "sponsors": ["Sen. Prozanski (D)"],
        "is_new": true,
        "previous_status": null
      }
    ],
    "source_failures": []
  }
}
```

## Email Classification

**Location:** `discord_bot.py` (inline, not a separate tool)

After `fetch_new_emails()` saves HTML files with `.meta.json` sidecars, classify by:

1. Check sender address — FPF emails come from addresses containing "fpf.org" or "informz.net"
2. Check subject line — FPF subjects match: "FPF U.S. AI Legislation" or "FPF U.S. Privacy Legislation"
3. Lexology emails: sender contains "lexology"
4. Unknown: log and skip

**`.meta.json` sidecar format** (saved alongside each email HTML):
```json
{
  "subject": "FPF U.S. AI Legislation Update (January 22)",
  "from": "FPF <noreply@informz.net>",
  "date": "Wed, 22 Jan 2026 10:00:00 -0500"
}
```

## Bill Download System

### Three-Tier Strategy

**Tier 1 — Follow FPF link:** Resolve the `FPF.informz.net/z/...` redirect URL via HTTP HEAD/GET to get the actual state legislature page URL. If the resolved page is a PDF, download directly. If it's an HTML page, look for a PDF download link.

**Tier 2 — State config pattern:** Look up the state in `pipeline/config/states.json`. Apply the configured URL pattern to construct the bill page or PDF URL. **Important:** Ask the user for each state's correct bill text location during development — they have prior experience navigating these sites.

**Tier 3 — Agent fallback:** Spawn a Claude agent with WebFetch that navigates the state legislature site to find and download the bill text. Log the successful approach for future config addition.

### State Config Format (`pipeline/config/states.json`)

```json
{
  "schema_version": "1.0",
  "states": {
    "OR": {
      "name": "Oregon",
      "strategy": "direct_pdf",
      "bill_page_pattern": "https://olis.oregonlegislature.gov/liz/{session}/Measures/Overview/{bill_type}{bill_number}",
      "pdf_pattern": "https://olis.oregonlegislature.gov/liz/{session}/Downloads/MeasureDocument/{bill_type}{bill_number}/Enrolled",
      "notes": "bill_type is SB/HB. bill_number digits only. Session format: 2025R1"
    }
  }
}
```

**Strategy types:**
- `direct_pdf` — URL pattern resolves directly to a PDF file
- `page_with_pdf_link` — Page contains a download link to the PDF
- `html_bill_text` — Bill text rendered as HTML (e.g., California leginfo)
- `agent_navigate` — Complex site, let agent figure it out

### Failed Downloads

If all tiers fail, the bill is still tracked in `tracker.json` with `"download_status": "failed"`. The status history and metadata are preserved. Downloads can be retried or resolved manually later.

## PDF Conversion

**Tool:** `tools/bill_processor.py` (includes docling integration)

```python
from docling.document_converter import DocumentConverter

converter = DocumentConverter()
result = converter.convert("path/to/bill.pdf")
markdown = result.document.export_to_markdown()
```

Docling v2.85.0 is installed and working on aarch64/Tegra. It handles:
- Complex PDF layouts common in legislative documents
- Document structure preservation (sections, lists, tables)
- Export to clean markdown

If a bill text is HTML (e.g., California), use WebFetch to extract the text and save as markdown directly (no docling needed).

## Version Management

When processing an FPF email that mentions a bill we already track:

1. Compare the bill's status in the email to `current_status` in tracker
2. If status has changed, append to `status_history`
3. If the bill has been amended/enrolled/engrossed (new text version):
   - Download the new version PDF
   - Convert to markdown
   - Save as `v{N}-{label}.pdf/.md` in the bill's `versions/` directory
   - Update `current.md` symlink to point to the new version
   - Update `current_version` in tracker and metadata

**Version labels:** `introduced`, `amended`, `substitute`, `engrossed`, `enrolled`, `chaptered`

## Processing Flow (End-to-End)

```
/scan Discord command
  ↓
fetch_new_emails() — save HTML + .meta.json sidecars
  ↓
classify_emails() — group into 'lexology', 'fpf', 'unknown'
  ↓
┌─────────────────────────┐  ┌──────────────────────────┐
│ Lexology emails         │  │ FPF emails               │
│ → existing scanner      │  │ → fpf-scanner agent      │
│ → existing pipeline     │  │ → fpf-scanner-output.json│
│ (unchanged)             │  │                          │
└─────────────────────────┘  └──────────┬───────────────┘
                                        ↓
                             bill_processor.py
                               ↓ for each bill:
                             ┌─ new bill? create dir, download, convert
                             └─ existing? update status, check for new version
                                        ↓
                             Update tracker.json + metadata.json
                                        ↓
                             Post bill status summary to Discord
```

## Discord Integration

### Modified `/scan` Command

After FPF processing completes, post a summary embed:
- Count of new bills discovered
- Count of status updates
- Count of bill texts downloaded
- Any download failures
- Per-bill status cards for new/changed bills

### New Commands

**`/bills [state]`** — List tracked bills, optionally filtered by state. Shows: bill ID, state, title, status, category.

**`/bill <identifier>`** — Detail view for one bill. Shows: full status history, current version, sponsor, links, download status.

## Implementation Phases

### Phase 1: Foundation
- Save email metadata sidecars in `fetch_new_emails()`
- Add email classification function
- Create `fpf-scanner` agent definition
- Create `fpf-scanner-output.json` schema
- Create `bills/` directory and empty `tracker.json`
- Create `pipeline/config/states.json` skeleton

### Phase 2: FPF Scanner Testing
- Download FPF emails from GitHub repo to local directory
- Process the earliest FPF emails (Jan 22-23) through fpf-scanner manually
- Validate extracted bill data against the emails

### Phase 3: Bill Downloads + Docling
- Implement `tools/bill_processor.py` with three-tier download
- Configure `states.json` for states appearing in early emails (ask user for each state)
- Test docling conversion on downloaded PDFs
- Verify tracker.json updates

### Phase 4: Orchestrator Integration
- Add FPF processing mode to orchestrator.md
- Wire email classification → fpf-scanner → bill_processor in orchestrator flow
- Update `discord_bot.py` `/scan` to handle FPF results
- End-to-end test with Jan 22-23 emails

### Phase 5: Chronological Build-Up
- Process remaining emails chronologically (Jan 29, Feb 5, ..., Mar 26)
- Verify status tracking across multiple emails for the same bills
- Add state configs as new states appear

### Phase 6: Discord Commands + Polish
- Implement `/bills` and `/bill` commands
- Bill status summary embeds after scans
- Handle edge cases: dead bills, session carryover, substitute bills

## Testing Strategy

- **Unit:** Process individual FPF emails, verify extracted bill count and metadata
- **Integration:** Full pipeline from email fetch → scanner → bill_processor → tracker update
- **Regression:** Process emails chronologically, verify status history accuracy for bills that appear in multiple emails
- **Validation set:** April 2-3 emails (held back) used to test tracker updates on established bills
