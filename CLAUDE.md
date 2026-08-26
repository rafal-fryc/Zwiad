<!-- GSD:project-start source:PROJECT.md -->
## Project

**Zwiad**

A regulatory monitoring platform that tracks privacy, cybersecurity, and AI law developments across US state and federal jurisdictions. A multi-agent pipeline — triggered manually for now, daily later — scans sources, identifies noteworthy developments, researches them in depth, produces verified markdown reports, and organizes them by topic. Built as CLI-driven agents running in Claude Code using the `claude` CLI (no API).

**Core Value:** Reliable, source-verified regulatory intelligence reports that can serve as both a queryable knowledge base and standalone client alerts.

### Constraints

- **Runtime**: Claude Code CLI (`claude` command) — no Anthropic API keys, no Agent SDK
- **Storage**: Local filesystem only — markdown files in structured directories
- **Execution**: Manual trigger for v1; designed so daily scheduling can be added later via Claude Code scheduled tasks
- **Review cap**: Max 3 iteration rounds between researcher and reviewer before escalating to human
- **Sources**: Web-accessible sources only — no paywalled databases unless the user provides access
<!-- GSD:project-end -->

<!-- GSD:stack-start source:research/STACK.md -->
## Technology Stack

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
| Researcher | `sonnet` | Deep analysis, report writing, source verification. Downgraded from opus 2026-07: cost/rate-limit tradeoff; revisit if verification quality drops. | MEDIUM |
| Reviewer | `opus` | Independent fact-checking is the pipeline's quality gate and the main escalation source. Re-upgraded to opus (Opus 5) 2026-08 after rate-limit handling gained auto-wait-and-resume; Opus 5 review has high precision AND recall. Other stages stay on sonnet to conserve usage limits. | MEDIUM |
| Categorizer | `sonnet` | File organization is straightforward. Haiku could work but sonnet is safer for taxonomy decisions. | HIGH |
## Architecture Pattern: Subagent Pipeline
### Key CLI Invocation Patterns
# Manual trigger (v1)
# Non-interactive with JSON output
# Pipe email content
# With tool restrictions (scanner only needs web + read)
# Defined in .claude/agents/scanner.md frontmatter:
# tools: Read, Glob, Grep, WebSearch, WebFetch
# With max turns to prevent runaway
# With budget cap
### Subagent Definition Example
# .claude/agents/scanner.md
## Sources to scan
- Law firm client alerts (search for recent publications)
- State legislature websites for new bills
- Federal Register for new rules and proposed rules
- NIST, FTC, state AG offices for enforcement actions
## Output format
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
# 1. Claude Code CLI (already installed; verify with `claude --version`)
claude --version  # expect v2.1.92+

# 2. Python deps (the project uses real packages despite the early "no deps" goal)
pip install --user discord.py python-dotenv docling

# 3. Optional MCP servers
claude mcp add fetch -- uvx mcp-server-fetch                  # enhanced URL fetching
claude mcp add playwright -- npx @playwright/mcp@latest       # JS-rendered scraping (used by tools/bill_processor.py)

# 4. Secrets — create .env at the project root
cat > .env <<'EOF'
DISCORD_TOKEN=...
DISCORD_GUILD_ID=...
DISCORD_CHANNEL_ID=...
IMAP_EMAIL=zwiad@example.com
IMAP_PASSWORD=...                # Gmail App Password (NOT your account password)
EOF
chmod 600 .env

# 5. Run the Discord bot
python3 discord_bot.py
```

## Runtime Environment
| Component | Current | Required | Notes |
|-----------|---------|----------|-------|
| Claude Code CLI | v2.1.92 | v2.1.63+ (subagents), v2.1.72+ (scheduled tasks) | Already exceeds requirements |
| Python | 3.10.12 | 3.10+ | discord.py, python-dotenv, docling required (see below) |
| Node.js | v24.14.1 | Any recent LTS | Only needed if Playwright MCP is used |
| Platform | Linux aarch64 (Tegra) | Any | Headless Linux: Desktop scheduled tasks unavailable; use cron |
| Shell | bash | bash | Pipeline orchestration scripts |

## Python Dependencies

The "no Python dependencies" claim from the original PROJECT.md is no longer accurate. Current required packages:

| Package | Used by | Purpose |
|---------|---------|---------|
| `discord.py` | `discord_bot.py` | Discord slash commands and bot integration |
| `python-dotenv` | `discord_bot.py`, `tools/topic_keys.py` (via .env) | Loads `.env` config |
| `docling` | `tools/bill_processor.py` | Converts downloaded bill PDFs to markdown (CPU-only on Tegra; set `CUDA_VISIBLE_DEVICES=""`) |
| `imaplib`, `email`, `socket` | `discord_bot.py` (stdlib) | Gmail IMAP fetch for `/scan` |

## Secrets

Stored in `.env` (gitignored). Required keys: `DISCORD_TOKEN`, `DISCORD_GUILD_ID`, `DISCORD_CHANNEL_ID`, `IMAP_EMAIL`, `IMAP_PASSWORD`. The IMAP password must be a Gmail **App Password** (not the account login) — generate one at https://myaccount.google.com/apppasswords with 2FA enabled.

The `.env` file lives in the project root with `chmod 600`. Do NOT commit it.

## External Services in Use

Despite the original "everything runs locally" goal, the following external services are now in play:

- **Anthropic API (indirect)**: Scanner agent's WebSearch and WebFetch tools call Anthropic's hosted endpoints. No API key needed (auth is via the Claude Code CLI session).
- **Gmail IMAP** (`imap.gmail.com:993`): Email digest ingestion for Lexology / FPF / IAPP.
- **Discord API**: Slash commands + channel messages.
- **GitHub API** (read-only, anonymous): `tools/fetch_fpf_emails.py` pulls `.eml` files from a public FileTransfer repo.
- **Playwright** (if installed): JS rendering for state legislature bill text downloads in `bill_processor.py`.
## Token Cost Considerations
Actual values as wired in the code (keep this table in sync with the call sites named below):
| Agent | Expected Usage | Cost Strategy (actual) |
|-------|---------------|---------------|
| Scanner | Medium (web searches + initial analysis) | sonnet; legacy `run-scanner.sh` uses `--max-turns 25`; production scan runs via orchestrator (`--max-turns 60`, `discord_bot.py`) |
| Researcher | High (deep web research + report writing) | sonnet; research legs use `--max-turns 200` + `--max-budget-usd max(5, todo*3)` (`discord_bot.py`); revision calls `--max-turns 20` (`run-reviewer.sh`) |
| Reviewer | High (source re-fetch + independent search, on opus) | opus; `--max-turns 15` for update reviews, `--max-turns 40` for full reviews (`run-reviewer.sh`) |
| Categorizer | Medium (index updates + file organization) | sonnet; `--max-turns 80`, `--max-budget-usd 10.00` (`discord_bot.py`) |
| Orchestrator | Coordination + validation | sonnet; `--max-turns 60` scan / `--max-turns 200` research (`discord_bot.py`, `run_pipeline.py`) |
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
<!-- GSD:stack-end -->

<!-- GSD:conventions-start source:CONVENTIONS.md -->
## Conventions

Conventions not yet established. Will populate as patterns emerge during development.
<!-- GSD:conventions-end -->

<!-- GSD:architecture-start source:ARCHITECTURE.md -->
## Architecture

Architecture not yet mapped. Follow existing patterns found in the codebase.
<!-- GSD:architecture-end -->

<!-- GSD:skills-start source:skills/ -->
## Project Skills

No project skills found. Add skills to any of: `.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, or `.github/skills/` with a `SKILL.md` index file.
<!-- GSD:skills-end -->

<!-- GSD:workflow-start source:GSD defaults -->
## GSD Workflow Enforcement

Before using Edit, Write, or other file-changing tools, start work through a GSD command so planning artifacts and execution context stay in sync.

Use these entry points:
- `/gsd-quick` for small fixes, doc updates, and ad-hoc tasks
- `/gsd-debug` for investigation and bug fixing
- `/gsd-execute-phase` for planned phase work

Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.

**Exemption — pipeline agents:** this rule applies to development work on the repo, not to pipeline execution. The scanner, researcher, reviewer, categorizer, fpf-scanner, and orchestrator agents Write/Edit reports, run artifacts, and state files as their core job — they do not need a GSD command to do so.
<!-- GSD:workflow-end -->



<!-- GSD:profile-start -->
## Developer Profile

> Profile not yet configured. Run `/gsd-profile-user` to generate your developer profile.
> This section is managed by `generate-claude-profile` -- do not edit manually.
<!-- GSD:profile-end -->
