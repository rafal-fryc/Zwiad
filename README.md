# Zwiad

A regulatory monitoring platform that tracks US privacy, cybersecurity, and AI law developments. A multi-agent pipeline — powered entirely by Claude Code CLI — scans sources, identifies noteworthy developments, researches them in depth, produces verified markdown reports, and organizes them by topic.

## How It Works

Five agents run sequentially, communicating via JSON files on the local filesystem:

| Agent | Role | Model |
|-------|------|-------|
| **Scanner** | Finds new regulatory developments from web sources and email digests | Sonnet |
| **Researcher** | Produces publication-quality reports with verified legal citations | Opus |
| **Reviewer** | Independent fact-checker; iterates up to 3 rounds with researcher | Opus |
| **Categorizer** | Files verified reports into `reports/{privacy,cybersecurity,ai-law}/` | Sonnet |
| **Orchestrator** | Coordinates the pipeline and spawns the other agents | Sonnet |

Agent definitions live in `.claude/agents/` as markdown files with frontmatter controlling tools, model, and turn limits.

## Quick Start

### Prerequisites

- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) v2.1.63+ (subagent support)
- Bash
- Python 3.8+

No API keys, no external services, no npm install required.

### Usage

**1. Scan** — finds new developments and pauses for your review:

```bash
# With an email digest (e.g., Lexology newsfeed saved as HTML)
python3 run_pipeline.py run --input path/to/digest.html

# Web sources only (no email input)
python3 run_pipeline.py run --web-only
```

This creates a timestamped run in `pipeline/runs/`, scans sources, deduplicates against existing reports, and generates `scanner-review.md` for you to approve.

**2. Approve** — review the findings in `scanner-review.md` and mark the ones you want researched.

**3. Resume** — researches, fact-checks, and files approved findings:

```bash
python3 run_pipeline.py resume <run-id>
```

## Pipeline Flow

```
run_pipeline.py run --input digest.html
  |
  v
Orchestrator (scan phase)
  |-> Scanner: ingests digest + web sources -> scanner-output.json
  |-> Deduplication: filters against existing reports
  |-> Generates scanner-review.md
  |
  [HUMAN APPROVAL GATE]
  |
run_pipeline.py resume <run-id>
  |
  v
Orchestrator (research phase)
  |-> Researcher: writes reports with verified citations
  |-> Reviewer: fact-checks, iterates up to 3 rounds
  |-> Categorizer: files reports into topic hierarchy
  |
  v
Done -> pipeline-complete.marker + audit-log.md
```

## Report Output

Reports are generated in two formats:

- **Client Alerts** (1-2 pages) — breaking news, executive-friendly, with action items
- **Research Memos** (3-5+ pages) — deep technical analysis with comprehensive sourcing

All reports include YAML frontmatter, inline citations with URLs, and confidence tags (`HIGH`/`MEDIUM`/`LOW`).

### Report Directory Structure

```
reports/
├── privacy/
│   ├── state-comprehensive-laws/
│   ├── federal-legislation/
│   ├── enforcement-actions/
│   ├── data-breach/
│   ├── childrens-privacy/
│   └── health-data/
├── cybersecurity/
│   ├── federal-frameworks/
│   ├── incident-reporting/
│   ├── enforcement-actions/
│   ├── critical-infrastructure/
│   └── standards-guidance/
└── ai-law/
    ├── federal-regulation/
    ├── state-legislation/
    ├── executive-orders/
    ├── enforcement-actions/
    └── frameworks-guidance/
```

## Data Sources

Configured in `pipeline/config/sources.json`:

- **Direct fetch**: FTC press releases, NIST CSRC news, Congress.gov bill tracking
- **Search queries**: State privacy legislation, FTC enforcement, AI regulation, NIST AI framework, state AG enforcement, law firm alerts
- **Email digests**: Lexology daily newsfeed (saved as HTML/EML to `input/`)

## Testing

```bash
tests/run-all.sh
```

11 test scripts covering schema validation, deduplication, approval gates, researcher validation, reviewer iteration, and more.

## Design Decisions

- **Human-in-the-loop**: Findings must be approved before expensive research runs
- **3-round review cap**: Reviewer iterates with researcher max 3 times, then escalates
- **File-based state**: All inter-agent communication is JSON in `pipeline/runs/` — fully debuggable and version-controllable
- **No external dependencies**: Runs entirely on Claude Code CLI built-in tools (WebSearch, WebFetch, Agent)
- **Schema validation**: JSON Schema validation at every agent handoff point

## Project Structure

```
.claude/agents/       # Agent definitions (scanner, researcher, reviewer, categorizer, orchestrator)
pipeline/
  config/             # sources.json, categories.json
  runs/               # Timestamped pipeline run directories
  schemas/            # JSON Schema definitions for agent handoffs
  scripts/            # Shell scripts for dedup, approval, validation, etc.
reports/              # Generated reports organized by topic
tests/                # Test suite
run_pipeline.py       # Main entry point
```

## License

Private repository.
