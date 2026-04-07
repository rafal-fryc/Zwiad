# Zwiad

## What This Is

A regulatory monitoring platform that tracks privacy, cybersecurity, and AI law developments across US state and federal jurisdictions. A multi-agent pipeline — triggered manually for now, daily later — scans sources, identifies noteworthy developments, researches them in depth, produces verified markdown reports, and organizes them by topic. Built as CLI-driven agents running in Claude Code using the `claude` CLI (no API).

## Core Value

Reliable, source-verified regulatory intelligence reports that can serve as both a queryable knowledge base and standalone client alerts.

## Requirements

### Validated

- ✓ Scanner agent scans web sources (law firm alerts, government sites) and identifies new regulatory developments — v1.0
- ✓ Scanner presents initial findings with links for human confirmation before proceeding — v1.0
- ✓ Daily email digest (forwarded/saved as file) serves as an input source for the scanner — v1.0
- ✓ Researcher agent takes confirmed findings and gathers detailed information from law firm client alerts, government websites, and other sources — v1.0
- ✓ Researcher agent writes an initial markdown report (format adapts: client alert style for breaking news, research memo style for complex analysis) — v1.0
- ✓ Reviewer agent independently checks report for source fidelity and legal accuracy — v1.0
- ✓ Researcher and reviewer iterate up to 3 rounds; if still disagreeing after 3, flag for human review — v1.0
- ✓ Categorizer agent files finalized reports into topic folders with emergent subcategories — v1.0
- ✓ All reports stored as local markdown files — v1.0
- ✓ Pipeline runs on manual trigger (CLI command); architecture supports daily scheduled runs via cron — v1.0
- ✓ Each agent is a separate Claude Code subprocess orchestrated via the `claude` CLI — v1.0

### Active

(Cleared for next milestone — define with `/gsd-new-milestone`)

### Out of Scope

- Knowledge base / vector store / search index — separate future project
- API-based agent orchestration (Agent SDK) — using CLI instead
- Autonomous operation without human confirmation — future milestone after trust is established
- Real-time monitoring / streaming — batch processing is sufficient
- Web UI or dashboard — CLI-only for now

## Context

Shipped v1.0 with ~3,800 LOC across Python, Bash, JSON, and Agent markdown.
Tech stack: Claude Code CLI (v2.1.92), Python 3.10, Bash, jq, system cron.
Architecture: 5 Claude Code subagents (scanner, researcher, reviewer, categorizer, orchestrator) with JSON state handoffs and jq schema validation.

- Lexology daily digest is the primary email input source — EML converted to HTML via `eml-to-html` npm package
- LinkedIn deferred to v2 (legal/scraping risks)
- Reports serve dual purpose: knowledge base entries AND standalone client alerts
- 16 seed subcategories across 3 topics with human-reviewed emergent growth
- Pipeline: scanner → human approval → researcher → reviewer (3-round iteration) → categorizer → audit log

## Constraints

- **Runtime**: Claude Code CLI (`claude` command) — no Anthropic API keys, no Agent SDK
- **Storage**: Local filesystem only — markdown files in structured directories
- **Execution**: Manual trigger for v1; designed so daily scheduling can be added later via Claude Code scheduled tasks
- **Review cap**: Max 3 iteration rounds between researcher and reviewer before escalating to human
- **Sources**: Web-accessible sources only — no paywalled databases unless the user provides access

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Claude Code CLI over Agent SDK | User wants to use regular Claude Code usage, no API costs | ✓ Good — all 5 agents run as subprocesses via `claude -p --agent` |
| File-based email input over Gmail MCP | Simpler, no auth complexity, user forwards/saves email | ✓ Good — EML/HTML conversion works, no auth needed |
| Flexible report format (alert vs memo) | Different developments warrant different treatment | ✓ Good — relevance-based format selection implemented |
| 3-round review cap | Balance thoroughness with token usage; escalate if unresolved | ✓ Good — iteration + escalation with APPROVED marker pattern |
| Topic-first folder hierarchy with emergent subcategories | Avoids premature taxonomy; lets structure grow with content | ✓ Good — seed list + emergent with human review for new subcategories |
| Python pipeline entry point over bash | User preference for Python | ✓ Good — run_pipeline.py with argparse CLI |
| Symlinks for multi-topic reports | Discoverable from multiple topic paths without duplication | — Pending live validation |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-04-07 after v1.0 milestone*
