# Technology Stack

**Project:** Zwiad - Regulatory Monitoring Platform
**Researched:** 2026-04-06

## Recommended Stack

### Core Runtime & Orchestration

| Technology | Version | Purpose | Why | Confidence |
|------------|---------|---------|-----|------------|
| Claude Code CLI (`claude`) | 2.1.92+ | Agent runtime for all subprocesses | Project constraint: no API keys, no Agent SDK. Already installed on the system. The `-p` (print) flag enables non-interactive invocation with `--output-format json` for structured output parsing. | HIGH |
| Claude Code Subagents | Built-in (v2.1.63+) | Define scanner, researcher, reviewer, categorizer as reusable agent definitions | Native Claude Code feature. Each subagent gets its own context window, custom system prompt, tool restrictions, and model selection. Defined as markdown files in `.claude/agents/`. Avoids building custom orchestration. | HIGH |
| Bash (shell scripts) | System default | Pipeline orchestration, glue between agents, manual trigger entry point | The project is CLI-driven. A bash script serves as the pipeline entry point, invoking `claude -p` for each stage or using the `--agent` flag to run the orchestrator agent. Minimal dependencies, maximum compatibility. | HIGH |

### Agent Architecture

| Technology | Version | Purpose | Why | Confidence |
|------------|---------|---------|-----|------------|
| Claude Code `--agent` flag | v2.1.63+ | Run orchestrator agent as the main session agent | The `--agent` flag lets you specify a custom agent definition as the session's main agent. The orchestrator agent can then spawn subagents (scanner, researcher, reviewer, categorizer) via the Agent tool. This is the intended pattern per official docs. | HIGH |
| Subagent markdown definitions | v2.1.63+ | Define each pipeline stage as a `.claude/agents/*.md` file | Each agent (scanner, researcher, reviewer, categorizer) gets a dedicated markdown file with frontmatter controlling `tools`, `model`, `maxTurns`, and `permissionMode`. These are version-controlled and reusable. | HIGH |
| `--agents` CLI flag (JSON) | v2.1.63+ | Dynamic agent definitions for testing/iteration | Allows passing agent definitions as JSON inline, useful during development before committing to `.claude/agents/` files. | MEDIUM |

### Web Scraping & Search

| Technology | Version | Purpose | Why | Confidence |
|------------|---------|---------|-----|------------|
| Built-in WebSearch | Built into Claude Code | Discover new regulatory developments, find law firm alerts | Always available to Claude Code agents. Uses Anthropic's server-side search. No configuration needed. Sufficient for finding published regulatory content. | HIGH |
| Built-in WebFetch | Built into Claude Code | Fetch and extract content from specific URLs (law firm sites, government pages) | Uses Axios locally with content conversion to markdown via Haiku. 15-minute cache. Handles most text-heavy regulatory content well. No setup required. | HIGH |
| Fetch MCP Server (`mcp-server-fetch`) | Latest via uvx | Enhanced URL fetching with chunked reading and proxy support | Fallback for when built-in WebFetch hits limitations. Supports `start_index` for reading large pages in chunks. Install with `claude mcp add fetch -- uvx mcp-server-fetch`. Use for government sites that return large documents. | MEDIUM |
| Playwright MCP Server (`@playwright/mcp`) | Latest via npx | JavaScript-rendered pages, dynamic content, sites requiring interaction | Only needed if government sites or LinkedIn require JS rendering. Register with `claude mcp add playwright -- npx @playwright/mcp@latest`. Single browser session limitation means sequential use only. Reserve for sites that fail with WebFetch. | LOW (contingent) |

### File-Based Communication & Storage

| Technology | Version | Purpose | Why | Confidence |
|------------|---------|---------|-----|------------|
| Local filesystem (markdown) | N/A | All reports, inter-agent state, pipeline artifacts | Project constraint: local filesystem only. Markdown is human-readable, version-controllable, and the native output format of Claude Code agents. | HIGH |
| Structured directory hierarchy | N/A | Organize reports by topic, manage pipeline state | Directories: `/reports/{privacy,cybersecurity,ai-law}/`, `/pipeline/` for inter-agent state files, `/input/` for email digest files. | HIGH |
| JSON state files | N/A | Machine-readable inter-agent communication | Pipeline state (what scanner found, what human confirmed, what researcher produced) stored as JSON in `/pipeline/state/`. Each pipeline run gets a timestamped directory. | HIGH |
| CLAUDE.md (per-directory) | N/A | Provide agents with context about directory structure and conventions | Root CLAUDE.md describes project. Subdirectory CLAUDE.md files in `/reports/` guide the categorizer. This is how Claude Code naturally discovers project context. | HIGH |

### Scheduling

| Technology | Version | Purpose | Why | Confidence |
|------------|---------|---------|-----|------------|
| Manual trigger (bash script) | N/A | v1: Human runs `./run-pipeline.sh` | Project requirement for v1. Simple, no infrastructure needed. | HIGH |
| Claude Code Desktop Scheduled Tasks | v2.1.72+ | v2: Daily automated runs | Native Claude Code feature. Persistent across restarts, accesses local files, configurable schedule. Minimum 1-minute interval. Requires Claude Code desktop app running. | MEDIUM |
| System cron + `claude -p` | System | v2 alternative: Daily scheduled runs via OS cron | More reliable than session-scoped `/loop` (which expires after 7 days). Cron calls a bash script that invokes `claude -p --agent orchestrator`. Works on headless Linux (like the Tegra system). | HIGH |
| GitHub Actions schedule trigger | N/A | v3: Cloud-based daily runs | Future option if the project moves to cloud execution. Not needed for v1/v2. | LOW |

### Input Processing

| Technology | Version | Purpose | Why | Confidence |
|------------|---------|---------|-----|------------|
| Email-to-file (manual save) | N/A | Convert daily email digest to scanner input | Project decision: user forwards/saves email as a file. Avoids Gmail API/MCP auth complexity. Save as `.eml`, `.txt`, or `.html` in `/input/` directory. | HIGH |
| Cat/pipe to claude | N/A | Feed email content to scanner agent | `cat input/digest-2026-04-06.txt \| claude -p --agent scanner "Analyze this digest..."` — native Unix pattern. | HIGH |

### Models (per agent role)

| Agent | Recommended Model | Why | Confidence |
|-------|-------------------|-----|------------|
| Orchestrator | `sonnet` | Coordination logic, not deep analysis. Cost-efficient. | HIGH |
| Scanner | `sonnet` | Web search + initial triage. Good balance of capability and speed. | HIGH |
| Researcher | `opus` | Deep analysis, report writing, source verification. Needs highest capability. | MEDIUM |
| Reviewer | `opus` | Independent fact-checking requires strong reasoning. | MEDIUM |
| Categorizer | `sonnet` | File organization is straightforward. Haiku could work but sonnet is safer for taxonomy decisions. | HIGH |

## Architecture Pattern: Subagent Pipeline

The recommended pattern uses Claude Code's native subagent system rather than custom bash orchestration:

```
User runs: claude --agent orchestrator "Run daily scan"

Orchestrator agent (sonnet):
  1. Reads /input/ for new email digests
  2. Spawns Scanner subagent → writes findings to /pipeline/state/{date}/scan-results.json
  3. Presents findings for human confirmation (interactive pause)
  4. For each confirmed finding:
     a. Spawns Researcher subagent → writes draft report to /pipeline/state/{date}/drafts/
     b. Spawns Reviewer subagent → reads draft, writes review to /pipeline/state/{date}/reviews/
     c. If disagreement, iterates (up to 3 rounds)
     d. Spawns Categorizer subagent → files final report to /reports/{topic}/{subtopic}/
```

### Key CLI Invocation Patterns

```bash
# Manual trigger (v1)
claude --agent orchestrator "Run daily pipeline scan"

# Non-interactive with JSON output
claude -p --agent scanner --output-format json "Scan these sources..."

# Pipe email content
cat input/digest.txt | claude -p --agent scanner "Analyze this email digest for regulatory developments"

# With tool restrictions (scanner only needs web + read)
# Defined in .claude/agents/scanner.md frontmatter:
# tools: Read, Glob, Grep, WebSearch, WebFetch

# With max turns to prevent runaway
claude -p --agent researcher --max-turns 25 "Research this development..."

# With budget cap
claude -p --agent researcher --max-budget-usd 2.00 "Research this development..."
```

### Subagent Definition Example

```markdown
# .claude/agents/scanner.md
---
name: scanner
description: Scans web sources for new regulatory developments in privacy, cybersecurity, and AI law
tools: Read, Glob, Grep, WebSearch, WebFetch, Write
model: sonnet
maxTurns: 20
---

You are a regulatory development scanner. Your job is to identify new noteworthy
developments in US privacy, cybersecurity, and AI law.

## Sources to scan
- Law firm client alerts (search for recent publications)
- State legislature websites for new bills
- Federal Register for new rules and proposed rules
- NIST, FTC, state AG offices for enforcement actions

## Output format
Write findings as JSON to the pipeline state directory...
```

## Alternatives Considered

| Category | Recommended | Alternative | Why Not |
|----------|-------------|-------------|---------|
| Agent orchestration | Claude Code subagents (`.claude/agents/`) | Custom bash script calling `claude -p` in sequence | Subagents are native, handle context windows automatically, support tool restrictions and model selection per agent. Bash scripts require manual JSON parsing and state management. |
| Agent orchestration | Subagents | Agent Teams (experimental) | Agent teams are experimental, add coordination overhead, use significantly more tokens, and are designed for inter-agent discussion — not sequential pipeline stages. Our pipeline is sequential with file handoffs, which is the subagent sweet spot. |
| Agent orchestration | Subagents | Claude Agent SDK (Python) | Project constraint: no API keys. SDK requires Anthropic API access. |
| Web scraping | Built-in WebSearch + WebFetch | Playwright MCP | Playwright adds complexity, requires headless browser, single-session limitation. Most regulatory sources are text-heavy static pages where WebFetch works fine. Add Playwright only if specific sources require JS rendering. |
| Web scraping | Built-in WebSearch + WebFetch | Bright Data / ScrapIn / external scraping APIs | Adds cost, external dependency, API key management. Overkill for reading public government sites and law firm blogs. |
| LinkedIn access | Skip for v1; revisit later | Proxycurl / scraping services | Proxycurl shut down (Jan 2026 lawsuit, July 2026 closure). LinkedIn actively sues scrapers. Legal risk not worth it for a monitoring tool. Use LinkedIn's native "Download Your Data" export or RSS-to-email services as workaround. |
| Inter-agent communication | JSON files in pipeline state directory | Redis message broker | Massive overkill. Agents run sequentially. File-based state is debuggable, version-controllable, and requires zero infrastructure. |
| Inter-agent communication | JSON state files | Agent Teams shared task list | Task list is for parallel coordination. Our pipeline is sequential. File-based state is simpler and more transparent. |
| Scheduling (v2) | System cron + `claude -p` | Claude Code `/loop` skill | `/loop` is session-scoped, expires after 7 days, requires an open session. System cron is durable and works on headless Linux. |
| Scheduling (v2) | System cron | Desktop Scheduled Tasks | Desktop tasks require the Claude Code desktop app running. This system is headless Linux (Tegra). Cron is more appropriate. |
| Report format | Markdown | HTML / PDF | Markdown is human-readable, git-friendly, Claude's native output format, and trivially convertible to other formats later. |
| State management | Flat JSON files per pipeline run | SQLite database | JSON files are simpler, debuggable with any text editor, and sufficient for batch processing. No query requirements yet. Consider SQLite if/when a knowledge base feature is added. |

## Installation & Setup

```bash
# Claude Code is already installed (v2.1.92)
# Verify:
claude --version

# Add Fetch MCP server (enhanced URL fetching, optional)
claude mcp add fetch -- uvx mcp-server-fetch

# Add Playwright MCP server (only if JS-rendered sites are needed)
# claude mcp add playwright -- npx @playwright/mcp@latest

# Create project directory structure
mkdir -p .claude/agents
mkdir -p reports/{privacy,cybersecurity,ai-law}
mkdir -p pipeline/state
mkdir -p input

# No npm install needed — this is a pure Claude Code CLI project
# No Python dependencies — agents use Claude Code's built-in tools
# No external services — everything runs locally
```

## Runtime Environment

| Component | Current | Required | Notes |
|-----------|---------|----------|-------|
| Claude Code | v2.1.92 | v2.1.63+ (subagents), v2.1.72+ (scheduled tasks) | Already exceeds requirements |
| Node.js | v24.14.1 | Any recent LTS | Only needed if Playwright MCP is used (npx) |
| Python | 3.10.12 | 3.8+ | Only needed if Fetch MCP server is used (uvx) |
| Platform | Linux aarch64 (Tegra) | Any | Headless Linux means Desktop scheduled tasks won't work; use cron |
| Shell | bash | bash | Pipeline entry point |

## Token Cost Considerations

| Agent | Expected Usage | Cost Strategy |
|-------|---------------|---------------|
| Scanner | Medium (web searches + initial analysis) | Use sonnet, set `--max-turns 20` |
| Researcher | High (deep web research + report writing) | Use opus for quality, set `--max-budget-usd 3.00` per finding |
| Reviewer | Medium (read report + verify sources) | Use opus, set `--max-turns 15` |
| Categorizer | Low (read report + file organization) | Use sonnet, set `--max-turns 5` |
| Orchestrator | Low (coordination only) | Use sonnet, set `--max-turns 30` for full pipeline |

Use `--max-budget-usd` on the researcher agent to prevent runaway costs on complex topics. The reviewer's 3-round iteration cap (project requirement) naturally limits spend.

## Sources

- [Claude Code CLI Reference](https://code.claude.com/docs/en/cli-reference) — Official docs, verified 2026-04-06 (HIGH confidence)
- [Claude Code Subagents](https://code.claude.com/docs/en/sub-agents) — Official docs, verified 2026-04-06 (HIGH confidence)
- [Claude Code Agent Teams](https://code.claude.com/docs/en/agent-teams) — Official docs, verified 2026-04-06 (HIGH confidence)
- [Claude Code Scheduled Tasks](https://code.claude.com/docs/en/scheduled-tasks) — Official docs, verified 2026-04-06 (HIGH confidence)
- [Agent Pipeline With Claude Code](https://iamjeremie.me/post/2026-03/agent-pipeline-with-claude-code/) — Community pattern, file-based agent communication (MEDIUM confidence)
- [Multi-Agent Orchestration: Running 10+ Claude Instances in Parallel](https://dev.to/bredmond1019/multi-agent-orchestration-running-10-claude-instances-in-parallel-part-3-29da) — Community pattern (MEDIUM confidence)
- [Claude Code Web Search and MCP Guide](https://help.apiyi.com/en/claude-code-web-search-websearch-mcp-guide-en.html) — WebSearch vs MCP comparison (MEDIUM confidence)
- [Playwright MCP Server](https://github.com/microsoft/playwright-mcp) — Official Microsoft repo (HIGH confidence)
- [Fetch MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) — Official MCP reference server (HIGH confidence)
- [LinkedIn Scraping Legal Guide 2026](https://sociavault.com/blog/linkedin-scraping-legal-guide-2026) — LinkedIn scraping risks (MEDIUM confidence)
