# Zwiad

## What This Is

A regulatory monitoring platform that tracks privacy, cybersecurity, and AI law developments across US state and federal jurisdictions. A multi-agent pipeline — triggered manually for now, daily later — scans sources, identifies noteworthy developments, researches them in depth, produces verified markdown reports, and organizes them by topic. Built as CLI-driven agents running in Claude Code using the `claude` CLI (no API).

## Core Value

Reliable, source-verified regulatory intelligence reports that can serve as both a queryable knowledge base and standalone client alerts.

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] Scanner agent scans web sources (law firm alerts, government sites, LinkedIn feeds) and identifies new regulatory developments worth reporting
- [ ] Scanner presents initial findings with links for human confirmation before proceeding
- [ ] Daily email digest (forwarded/saved as file) serves as an input source for the scanner
- [ ] Researcher agent takes confirmed findings and gathers detailed information from law firm client alerts, government websites, LinkedIn posts, and other sources
- [ ] Researcher agent writes an initial markdown report (format adapts: client alert style for breaking news, research memo style for complex analysis)
- [ ] Reviewer agent independently checks report for source fidelity (claims supported by cited sources, no hallucinations) and legal accuracy (correct statutes, dates, jurisdictions)
- [ ] Researcher and reviewer iterate up to 3 rounds; if still disagreeing after 3, flag for human review
- [ ] Categorizer agent files finalized reports into topic folders: `/privacy`, `/cybersecurity`, `/ai-law`, each with subcategories determined as topics emerge
- [ ] All reports stored as local markdown files
- [ ] Pipeline runs on manual trigger (CLI command); architecture supports future daily scheduled runs
- [ ] Each agent is a separate Claude Code subprocess orchestrated via the `claude` CLI

### Out of Scope

- Knowledge base / vector store / search index — separate future project
- API-based agent orchestration (Agent SDK) — using CLI instead
- Autonomous operation without human confirmation — future milestone after trust is established
- Real-time monitoring / streaming — batch processing is sufficient
- Web UI or dashboard — CLI-only for now

## Context

- The user receives a daily email digest of law firm client alerts relevant to privacy/cyber/AI law — this will be forwarded or saved as a file for the scanner to ingest
- LinkedIn is a desired source; feasibility of programmatic LinkedIn feed access needs investigation during research
- Reports serve dual purpose: building a knowledge base for future LLM querying AND serving as individual client alerts when developments warrant it
- Three top-level topic categories (privacy, cybersecurity, ai-law) with subcategories that emerge organically as reports accumulate
- The categorizer agent defines and refines subcategories over time rather than using a fixed taxonomy

## Constraints

- **Runtime**: Claude Code CLI (`claude` command) — no Anthropic API keys, no Agent SDK
- **Storage**: Local filesystem only — markdown files in structured directories
- **Execution**: Manual trigger for v1; designed so daily scheduling can be added later via Claude Code scheduled tasks
- **Review cap**: Max 3 iteration rounds between researcher and reviewer before escalating to human
- **Sources**: Web-accessible sources only — no paywalled databases unless the user provides access

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Claude Code CLI over Agent SDK | User wants to use regular Claude Code usage, no API costs | — Pending |
| File-based email input over Gmail MCP | Simpler, no auth complexity, user forwards/saves email | — Pending |
| Flexible report format (alert vs memo) | Different developments warrant different treatment | — Pending |
| 3-round review cap | Balance thoroughness with token usage; escalate if unresolved | — Pending |
| Topic-first folder hierarchy with emergent subcategories | Avoids premature taxonomy; lets structure grow with content | — Pending |

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
*Last updated: 2026-04-06 after initialization*
