# Architecture Research

**Domain:** Multi-agent CLI pipeline for regulatory monitoring
**Researched:** 2026-04-06
**Confidence:** HIGH

## Standard Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                        ORCHESTRATOR (Bash script)                    │
│  Runs pipeline stages sequentially, passes file paths between them  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐   ┌────────────┐   ┌──────────┐   ┌──────────────┐  │
│  │ SCANNER  │──>│ RESEARCHER │──>│ REVIEWER │──>│ CATEGORIZER  │  │
│  │ (agent)  │   │  (agent)   │<──│ (agent)  │   │   (agent)    │  │
│  └────┬─────┘   └─────┬──────┘   └────┬─────┘   └──────┬───────┘  │
│       │               │               │                │           │
│       v               v               v                v           │
│  scan_results/   drafts/         reviews/          reports/        │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                     HUMAN CONFIRMATION GATE                          │
│         (Terminal prompt between scanner and researcher)             │
├─────────────────────────────────────────────────────────────────────┤
│                        FILESYSTEM (data layer)                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌───────────────────┐  │
│  │  inbox/  │  │pipeline/ │  │ reports/ │  │  .claude/agents/  │  │
│  │ (email   │  │ (working │  │ (final   │  │  (agent configs)  │  │
│  │  files)  │  │  state)  │  │ output)  │  │                   │  │
│  └──────────┘  └──────────┘  └──────────┘  └───────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

### Component Responsibilities

| Component | Responsibility | Implementation |
|-----------|----------------|----------------|
| Orchestrator | Sequencing agents, file routing, iteration control, error handling, human gates | Bash script (`zwiad.sh`) invoking `claude -p` |
| Scanner Agent | Ingest email digests and source lists, identify new regulatory developments | Claude Code subagent with web search tools |
| Researcher Agent | Deep-dive confirmed findings, produce markdown report drafts | Claude Code subagent with web search and file write |
| Reviewer Agent | Verify source fidelity, legal accuracy, flag hallucinations | Claude Code subagent, read-only on drafts, writes review feedback |
| Categorizer Agent | File finalized reports into topic/subtopic folders, maintain taxonomy | Claude Code subagent with file read/write/move |
| Human Gate | Present scanner findings for confirmation before research begins | Bash `select` or `read` prompt in orchestrator |
| Filesystem | All inter-agent communication, working state, final output | Structured directories with JSON metadata + markdown content |

## Recommended Project Structure

```
zwiad/
├── zwiad.sh                    # Main orchestrator script
├── lib/
│   ├── run-agent.sh            # Wrapper: invokes claude -p with standard flags
│   ├── iterate.sh              # Researcher-reviewer iteration loop (max 3 rounds)
│   └── confirm.sh              # Human confirmation gate logic
├── .claude/
│   └── agents/                 # Subagent definitions (markdown + frontmatter)
│       ├── scanner.md
│       ├── researcher.md
│       ├── reviewer.md
│       └── categorizer.md
├── inbox/                      # Input: email digests, source lists
│   └── 2026-04-06-digest.txt
├── pipeline/                   # Working state (per-run, ephemeral)
│   └── runs/
│       └── 2026-04-06T08-00/
│           ├── scan-results.json       # Scanner output
│           ├── confirmed.json          # Post-human-gate filtered list
│           ├── drafts/                 # Researcher output
│           │   ├── finding-001.md
│           │   └── finding-002.md
│           ├── reviews/                # Reviewer feedback
│           │   ├── finding-001-review-1.md
│           │   └── finding-001-review-2.md
│           └── run-log.json            # Pipeline execution metadata
├── reports/                    # Final output: categorized reports
│   ├── privacy/
│   │   ├── state-laws/
│   │   └── federal/
│   ├── cybersecurity/
│   │   ├── incident-response/
│   │   └── frameworks/
│   ├── ai-law/
│   │   └── executive-orders/
│   └── taxonomy.json           # Categorizer-maintained topic structure
└── CLAUDE.md                   # Project context for all agents
```

### Structure Rationale

- **`inbox/`:** Decouples input ingestion from pipeline execution. User drops files here manually; future automation writes here too.
- **`pipeline/runs/`:** Each run gets a timestamped directory. Working state is isolated per run so concurrent or failed runs do not corrupt each other. This is the inter-agent communication channel.
- **`reports/`:** The durable output. Organized by topic with subcategories that the categorizer evolves over time. This is the knowledge base.
- **`.claude/agents/`:** Project-scoped subagent definitions checked into version control. Each agent's system prompt, tool restrictions, and model are defined here.
- **`lib/`:** Shell functions factored out of the main orchestrator for testability and readability.

## Architectural Patterns

### Pattern 1: Bash Orchestrator with `claude -p` Subprocesses

**What:** A bash script drives the pipeline. Each agent is a `claude -p` invocation that reads input from a file, writes output to a file, and exits. The orchestrator controls sequencing, error handling, and data routing.

**When to use:** When agents are sequential (not parallel), communication is file-based, and you want zero dependencies beyond bash and the `claude` CLI.

**Trade-offs:**
- Pro: No runtime dependencies, trivially debuggable, each agent run is logged
- Pro: Natural fit for Claude Code's `--print` mode which exits after completion
- Pro: Shell script is easy to schedule via cron or Claude Code scheduled tasks
- Con: No real-time inter-agent communication (file-based only)
- Con: Bash error handling is primitive compared to Python/Node

**Example:**
```bash
#!/usr/bin/env bash
set -euo pipefail

RUN_DIR="pipeline/runs/$(date +%Y-%m-%dT%H-%M)"
mkdir -p "$RUN_DIR/drafts" "$RUN_DIR/reviews"

# Scanner agent
cat inbox/*.txt | claude -p \
  --agent scanner \
  --output-format json \
  --json-schema "$(cat schemas/scan-results.json)" \
  --max-turns 15 \
  --max-budget-usd 2.00 \
  --allowedTools "Read,Bash(curl *),WebSearch,WebFetch" \
  > "$RUN_DIR/scan-results.json"

# Human confirmation gate
source lib/confirm.sh
confirm_findings "$RUN_DIR/scan-results.json" "$RUN_DIR/confirmed.json"

# Researcher + Reviewer iteration loop
source lib/iterate.sh
iterate_research "$RUN_DIR"
```

### Pattern 2: Structured JSON Handoffs Between Agents

**What:** Agents communicate via JSON files with defined schemas. The scanner outputs a `scan-results.json` with a list of findings. The researcher reads that and writes markdown drafts plus a `draft-metadata.json`. The reviewer reads both and writes structured feedback. Schemas enforce contracts between agents.

**When to use:** Always. File-based handoffs need structure to prevent drift and enable the orchestrator to make routing decisions.

**Trade-offs:**
- Pro: `--json-schema` flag enforces output shape at the Claude API level
- Pro: Orchestrator can parse JSON to decide next steps (e.g., which findings need more research)
- Con: JSON schemas need maintenance as pipeline evolves

**Example schema for scanner output:**
```json
{
  "type": "object",
  "properties": {
    "findings": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string" },
          "title": { "type": "string" },
          "summary": { "type": "string" },
          "sources": { "type": "array", "items": { "type": "string" } },
          "jurisdiction": { "type": "string" },
          "category": { "enum": ["privacy", "cybersecurity", "ai-law"] },
          "urgency": { "enum": ["breaking", "notable", "background"] }
        },
        "required": ["id", "title", "summary", "sources", "category"]
      }
    },
    "scan_metadata": {
      "type": "object",
      "properties": {
        "sources_checked": { "type": "integer" },
        "scan_date": { "type": "string" }
      }
    }
  },
  "required": ["findings"]
}
```

### Pattern 3: Capped Iteration Loop (Researcher-Reviewer)

**What:** The researcher and reviewer agents iterate: researcher writes a draft, reviewer checks it, researcher revises based on feedback. Maximum 3 rounds. If unresolved after 3, the finding is flagged for human review.

**When to use:** For the researcher-reviewer pair specifically. This is the only multi-turn interaction in the pipeline.

**Trade-offs:**
- Pro: Catches hallucinations and factual errors before they reach final output
- Pro: Hard cap prevents token waste on fundamentally problematic findings
- Con: Each iteration round is a full `claude -p` invocation (token cost scales linearly with rounds)
- Con: Reviewer may be overly conservative, burning rounds on style rather than substance

**Example:**
```bash
iterate_research() {
  local run_dir="$1"
  local max_rounds=3

  for finding in $(jq -r '.findings[].id' "$run_dir/confirmed.json"); do
    local round=0
    local status="needs_revision"

    while [[ "$status" == "needs_revision" && $round -lt $max_rounds ]]; do
      round=$((round + 1))

      # Researcher writes/revises draft
      claude -p \
        --agent researcher \
        --output-format text \
        --max-turns 20 \
        --max-budget-usd 3.00 \
        --allowedTools "Read,Write,WebSearch,WebFetch,Bash(curl *)" \
        "Research finding $finding. Round $round. $(cat_context $run_dir $finding $round)" \
        > "$run_dir/drafts/${finding}-r${round}.md"

      # Reviewer checks draft
      claude -p \
        --agent reviewer \
        --output-format json \
        --json-schema "$(cat schemas/review-result.json)" \
        --max-turns 10 \
        --max-budget-usd 1.50 \
        --allowedTools "Read,WebSearch,WebFetch" \
        "Review draft for $finding. $(cat "$run_dir/drafts/${finding}-r${round}.md")" \
        > "$run_dir/reviews/${finding}-review-${round}.json"

      status=$(jq -r '.verdict' "$run_dir/reviews/${finding}-review-${round}.json")
    done

    if [[ "$status" == "needs_revision" ]]; then
      echo "FLAGGED: $finding unresolved after $max_rounds rounds" >> "$run_dir/human-review.log"
    fi
  done
}
```

### Pattern 4: Subagent Definitions as Configuration

**What:** Each agent is defined as a `.claude/agents/*.md` file with YAML frontmatter specifying tools, model, and system prompt. The orchestrator references them via `--agent <name>`. This separates agent behavior (prompt engineering) from pipeline logic (bash orchestration).

**When to use:** Always. This is how Claude Code natively supports multi-agent setups.

**Trade-offs:**
- Pro: Agent prompts are version-controlled, reviewable, iterable
- Pro: Tool restrictions enforced per-agent (reviewer cannot write files, scanner cannot edit reports)
- Pro: Model selection per agent (use Sonnet for scanner/categorizer, Opus for researcher/reviewer)
- Con: Subagent definitions are loaded at session start; changes require new session

**Example subagent definition (`.claude/agents/reviewer.md`):**
```markdown
---
name: reviewer
description: Independently verifies report drafts for source fidelity and legal accuracy
tools: Read, Grep, Glob, WebSearch, WebFetch
model: opus
maxTurns: 10
---

You are a regulatory law reviewer. Your job is to independently verify
report drafts for:

1. **Source fidelity**: Every factual claim must be supported by a cited
   source. Check that citations exist and actually support the claims made.
2. **Legal accuracy**: Statute numbers, effective dates, jurisdiction names,
   and regulatory body names must be correct.
3. **No hallucinations**: Flag any claims that appear fabricated or that you
   cannot verify from the cited sources.

Output a structured review with:
- verdict: "approved" | "needs_revision"
- issues: array of {type, description, location, severity}
- suggestions: array of improvement recommendations

Be rigorous. A false positive (flagging correct content) is far less costly
than a false negative (approving incorrect content).
```

## Data Flow

### Pipeline Flow (Happy Path)

```
inbox/*.txt (email digests)
    |
    v
[SCANNER AGENT] --json-schema--> pipeline/runs/{ts}/scan-results.json
    |
    v
[HUMAN GATE] --select/confirm--> pipeline/runs/{ts}/confirmed.json
    |
    v
[RESEARCHER AGENT] ------------> pipeline/runs/{ts}/drafts/{id}.md
    |                                     ^
    v                                     |
[REVIEWER AGENT] --verdict json---------->|  (loop up to 3x)
    |                                     |
    | approved                    needs_revision
    v
[CATEGORIZER AGENT] -----------> reports/{category}/{subcategory}/{id}.md
                                  reports/taxonomy.json (updated)
```

### Data Contracts Between Agents

| From | To | Format | Schema | Content |
|------|----|--------|--------|---------|
| Email digest | Scanner | Plain text (piped via stdin) | None | Raw email text |
| Scanner | Human Gate | JSON | `scan-results.json` schema | Array of findings with sources, category, urgency |
| Human Gate | Researcher | JSON | `confirmed.json` (subset of scan results) | Filtered findings the user approved |
| Researcher | Reviewer | Markdown + JSON sidecar | Report template + `draft-metadata.json` | Full report draft with citations |
| Reviewer | Researcher | JSON | `review-result.json` schema | Verdict, issues array, suggestions |
| Reviewer | Categorizer | Markdown (approved draft) | Report template | Finalized report |
| Categorizer | Filesystem | Markdown + JSON | Report + `taxonomy.json` | Filed report + updated taxonomy |

### Key Data Flows

1. **Scanner ingest flow:** Email text piped to `claude -p` via stdin. Scanner uses web search tools to verify and expand on items mentioned in the digest. Outputs structured JSON with findings.
2. **Research-review loop:** The orchestrator bash script manages iteration. Each round, the researcher gets the previous draft plus reviewer feedback as input context (piped or via `--append-system-prompt`). The reviewer gets only the latest draft and original finding context (no access to previous review rounds, to prevent anchoring).
3. **Categorization flow:** Categorizer reads finalized report markdown and the current `taxonomy.json`. It decides the appropriate category/subcategory, creates directories if needed, moves the report, and updates `taxonomy.json`. The taxonomy evolves organically.

## Scaling Considerations

| Scale | Architecture Adjustments |
|-------|--------------------------|
| 1-5 findings/day | Current sequential pipeline is fine. Each run takes 10-30 minutes. |
| 5-20 findings/day | Parallelize researcher-reviewer loops per finding (background jobs in bash, `wait` for completion). Scanner and categorizer remain sequential. |
| 20+ findings/day | Consider moving orchestrator to Python/Node for better job management. Add batching: scanner groups related findings. Consider Agent Teams for parallel research. |

### Scaling Priorities

1. **First bottleneck:** Researcher-reviewer iteration time. Each finding takes 3-6 `claude -p` invocations. With 10 findings, that is 30-60 invocations sequentially. Mitigation: parallelize per finding with `&` and `wait` in bash.
2. **Second bottleneck:** Token budget per run. At 20+ findings with Opus, daily costs become significant. Mitigation: use Sonnet for scanner/categorizer, reserve Opus for researcher/reviewer. Use `--max-budget-usd` to cap per-agent spend.
3. **Third bottleneck:** Context window limits. Very complex regulatory developments with many sources may exceed a single agent's context. Mitigation: chunk large findings into sub-topics before research.

## Anti-Patterns

### Anti-Pattern 1: Python/Node Orchestrator for a 4-Stage Pipeline

**What people do:** Build a sophisticated orchestrator in Python or Node.js with async/await, queue management, and process pools for what is fundamentally a 4-step sequential pipeline.
**Why it's wrong:** Adds dependency management, packaging, and debugging complexity for no benefit at this scale. The pipeline is inherently sequential (scanner before researcher before reviewer before categorizer). Bash handles this natively.
**Do this instead:** Start with bash. Move to Python/Node only when you need parallel per-finding research (scale consideration #1) and bash `&`/`wait` becomes unwieldy.

### Anti-Pattern 2: Session Continuation Instead of Fresh Invocations

**What people do:** Use `claude -c` (continue session) to chain agents, keeping all context in one growing conversation.
**Why it's wrong:** Context window fills up fast. Agent prompts bleed into each other. No isolation between agents. A hallucination in round 1 infects all subsequent rounds.
**Do this instead:** Each `claude -p` invocation is a fresh session. Pass only the relevant files as input. The `--no-session-persistence` flag prevents disk clutter.

### Anti-Pattern 3: Giving All Agents All Tools

**What people do:** Every agent gets full tool access because it is simpler to configure.
**Why it's wrong:** The reviewer should never be able to edit report files (it should only read and provide feedback). The scanner should not be able to write to the reports directory. Unrestricted tools undermine the pipeline's checks and balances.
**Do this instead:** Use the `tools` frontmatter field in each subagent definition. Scanner: `Read, WebSearch, WebFetch, Bash(curl *)`. Researcher: `Read, Write, WebSearch, WebFetch`. Reviewer: `Read, Grep, WebSearch, WebFetch` (no Write/Edit). Categorizer: `Read, Write, Bash(mv *), Bash(mkdir *)`.

### Anti-Pattern 4: Unstructured Agent Output

**What people do:** Let agents output free-form text and parse it with regex in the orchestrator.
**Why it's wrong:** LLM output format drifts. Regex parsing is fragile. The orchestrator cannot make routing decisions (e.g., "is this finding approved?") without structured data.
**Do this instead:** Use `--output-format json` with `--json-schema` for every agent that feeds into orchestrator logic. Only the final report output is free-form markdown.

### Anti-Pattern 5: Reviewer Sees Previous Reviews

**What people do:** Pass all previous review rounds to the reviewer so it has "full context."
**Why it's wrong:** Creates anchoring bias. If the reviewer flagged issue X in round 1, it will look for issue X in round 2 even if it was fixed. The reviewer should evaluate each draft independently.
**Do this instead:** Reviewer gets only the current draft and the original finding context. The researcher gets reviewer feedback (to know what to fix), but the reviewer starts fresh each round.

## Integration Points

### External Services

| Service | Integration Pattern | Notes |
|---------|---------------------|-------|
| Web sources (gov sites, law firms) | `WebSearch` and `WebFetch` tools via Claude Code | No API keys needed; uses Claude Code's built-in web access |
| Email digests | File drop into `inbox/` | User forwards/saves email as `.txt` or `.eml` file. Future: automate via mail rule |
| LinkedIn | `WebFetch` on public posts | Feasibility uncertain for feeds; individual post URLs work. Investigate during implementation |

### Internal Boundaries

| Boundary | Communication | Notes |
|----------|---------------|-------|
| Orchestrator to Agents | `claude -p` subprocess with stdin pipe and file arguments | Orchestrator waits for exit code, reads output file |
| Agent to Agent | Filesystem (JSON + Markdown in `pipeline/runs/`) | No direct communication; orchestrator mediates all handoffs |
| Human Gate | Terminal `read`/`select` prompt in orchestrator script | Blocks pipeline until user confirms. Timeout option for future automation |
| Pipeline to Reports | File move/copy by categorizer agent | Reports directory is the durable output; pipeline directory is ephemeral |

## Build Order (Dependencies)

The following build order reflects component dependencies. Each phase produces something testable.

1. **Filesystem structure + orchestrator skeleton** - Create directory layout, `zwiad.sh` with placeholder agent calls, `run-agent.sh` wrapper. Testable: script runs, creates run directory, exits cleanly.

2. **Scanner agent** - Define `.claude/agents/scanner.md`, implement scan-results JSON schema, wire into orchestrator. Testable: feed an email digest, get structured findings JSON.

3. **Human confirmation gate** - Implement `confirm.sh` with terminal prompts. Testable: present scan results, user selects/rejects findings, writes `confirmed.json`.

4. **Researcher agent** - Define `.claude/agents/researcher.md`, implement report template, wire single-pass research into orchestrator. Testable: take a confirmed finding, produce a draft report.

5. **Reviewer agent** - Define `.claude/agents/reviewer.md`, implement review-result JSON schema. Testable: take a draft, produce structured review feedback.

6. **Iteration loop** - Implement `iterate.sh` with max-3-round logic, human-review flagging. Testable: researcher and reviewer iterate on a finding, loop terminates correctly.

7. **Categorizer agent** - Define `.claude/agents/categorizer.md`, implement taxonomy management. Testable: take an approved report, file it in the correct category, update taxonomy.

8. **End-to-end pipeline** - Wire all components together, add error handling, logging, budget caps. Testable: full pipeline from email digest to categorized report.

## Sources

- [Claude Code CLI Reference](https://code.claude.com/docs/en/cli-reference) - Official docs for all CLI flags including `-p`, `--output-format`, `--json-schema`, `--max-turns`, `--max-budget-usd`
- [Claude Code Agent Teams](https://code.claude.com/docs/en/agent-teams) - Official docs for multi-agent orchestration patterns
- [Claude Code Subagents](https://code.claude.com/docs/en/sub-agents) - Official docs for subagent definitions, frontmatter fields, tool restrictions
- [Claude Code Headless/Print Mode](https://code.claude.com/docs/en/headless) - Official docs for running Claude Code programmatically
- [Multi-Agent Orchestration with Claude Code](https://dev.to/bredmond1019/multi-agent-orchestration-running-10-claude-instances-in-parallel-part-3-29da) - Community patterns for parallel Claude instances
- [Terminal-Based Agent Engineering](https://www.sitepoint.com/terminal-based-agent-engineering-the--claude-code--workflow/) - Patterns for CLI-based agent workflows

---
*Architecture research for: Zwiad regulatory monitoring pipeline*
*Researched: 2026-04-06*
