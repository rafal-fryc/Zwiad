# Pitfalls Research

**Domain:** Multi-agent CLI pipeline for regulatory monitoring (privacy/cybersecurity/AI law)
**Researched:** 2026-04-06
**Confidence:** HIGH (critical pitfalls) / MEDIUM (some edge cases based on limited production data for Claude CLI orchestration)

## Critical Pitfalls

### Pitfall 1: LLM Hallucination in Legal Reports — Fabricated Citations and Incorrect Statutes

**What goes wrong:**
LLMs fabricate case citations, invent statute numbers, misattribute legal provisions to the wrong jurisdiction, or conflate similar-but-distinct laws. Stanford research (2025) found general-purpose LLMs fabricate case citations in 30-45% of legal research responses. Claude is better than average but not immune — especially for niche state-level privacy statutes where training data is thin.

**Why it happens:**
LLMs generate plausible-sounding legal references by pattern-matching, not by looking them up. State-level regulatory developments (e.g., a new amendment to the Texas Data Privacy and Security Act) have sparse training representation. The model confidently generates a citation that "looks right" but is wrong in the details — wrong section number, wrong effective date, wrong jurisdiction.

**How to avoid:**
- The reviewer agent must perform source fidelity checks: every claim in a report must trace back to a specific URL or document the researcher cited.
- Implement a "claim-source pair" format in report templates: each factual assertion has an inline citation. The reviewer verifies the citation actually says what the report claims.
- Never let the researcher agent generate statute numbers from memory. The researcher must extract them from scraped source material and quote verbatim.
- Use the 3-round researcher-reviewer loop specifically to catch this: Round 1 catches gross hallucinations, Round 2 catches subtle misattributions, Round 3 is the final sanity check.

**Warning signs:**
- Reports cite statutes with suspiciously "round" section numbers (e.g., "Section 100" instead of "Section 541.083").
- Effective dates that fall on January 1 or July 1 without source confirmation (these are common defaults the model guesses).
- Reports mention laws that sound plausible but return no results when searched.
- Reviewer consistently passes reports without flagging anything — suggests the reviewer prompt is too lenient.

**Phase to address:**
Phase 1 (report template design) and Phase 2 (reviewer agent implementation). The claim-source pair format must be baked into the report template from day one. The reviewer agent's system prompt must explicitly instruct it to verify each citation against the cited source URL.

---

### Pitfall 2: Agent Error Cascade — One Subprocess Failure Silently Corrupts the Pipeline

**What goes wrong:**
In a multi-agent CLI pipeline, Agent B receives garbled or incomplete output from Agent A and proceeds to work with it rather than failing. The scanner finds 5 developments but the JSON is malformed; the researcher picks up 3 of them and silently drops 2. Or the researcher produces a report but exits with a non-zero code; the reviewer never runs and the pipeline "completes" with an unreviewed report sitting in the output folder.

Research on multi-agent LLM systems shows error amplification of up to 17.2x compared to single-agent baselines when agents are connected without structured validation.

**Why it happens:**
- Claude CLI `--print` mode returns text to stdout. If the orchestrator does not validate the output structure before passing it to the next agent, garbage propagates.
- Subprocess exit codes are not always checked. A Claude CLI call that hits a context limit or internal error may still exit 0 with partial output.
- File-based IPC (agent A writes a file, agent B reads it) has no built-in contract enforcement — agent B reads whatever is there, even if it is incomplete.

**How to avoid:**
- Define explicit JSON schemas for inter-agent communication. Use `--output-format json` with `--json-schema` for structured output from each agent.
- Validate every agent's output against its schema before passing to the next agent. The orchestrator script (not the agents themselves) owns this validation.
- Check both exit code AND output validity. A zero exit code with empty or malformed output is still a failure.
- Implement a "pipeline manifest" — a simple JSON file that tracks which agents ran, their exit codes, output file paths, and validation status. If any step is missing or failed, the pipeline halts and reports where it broke.

**Warning signs:**
- Reports appear in the output folder that were never reviewed (missing reviewer metadata).
- Scanner identifies developments but the researcher's report covers fewer items than expected.
- Pipeline "succeeds" but output files are empty or truncated.

**Phase to address:**
Phase 1 (orchestrator design). The orchestrator must be designed with validation gates between every agent handoff from the very beginning. Retrofitting validation into an existing pipeline is painful.

---

### Pitfall 3: LinkedIn Scraping — Legal Risk and Technical Infeasibility

**What goes wrong:**
The project lists LinkedIn feeds as a desired source. Teams spend significant effort building LinkedIn scraping infrastructure, only to find: (a) accounts get banned within days, (b) LinkedIn sends a cease-and-desist, or (c) the scraper breaks every time LinkedIn updates their anti-bot measures. Even if it works briefly, it creates ongoing legal exposure.

**Why it happens:**
Despite the hiQ v. LinkedIn ruling (publicly accessible data scraping does not violate CFAA), LinkedIn's Terms of Service explicitly prohibit automated access. LinkedIn actively detects and bans scraping accounts. Logged-in scraping (needed for feed access) is more legally risky than public profile scraping. LinkedIn has sued companies that created fake accounts for scraping.

**How to avoid:**
- Do NOT build programmatic LinkedIn scraping. The legal risk is real and the technical maintenance burden is unsustainable.
- Instead, use LinkedIn as a manual discovery channel: the user reads their LinkedIn feed and forwards interesting posts/links to the scanner's input (same pattern as the email digest — save as file or copy URL).
- If LinkedIn content is crucial, consider: (a) LinkedIn's official API (very limited, requires partner approval), (b) RSS feeds from LinkedIn newsletters (some LinkedIn newsletters have RSS), (c) monitoring the same authors' content on their law firm websites instead (most law firm partners cross-post).
- The real value from LinkedIn is discovering who posted, not the LinkedIn page itself. Track the law firms and authors, and scrape their actual websites.

**Warning signs:**
- Anyone on the team starts building a LinkedIn login flow or session management.
- Project planning includes "LinkedIn API integration" as a phase deliverable.
- Test accounts getting CAPTCHAs or temporary bans during development.

**Phase to address:**
Phase 0 (project scoping). Make the explicit decision NOW to exclude programmatic LinkedIn access. Document the alternative approach (manual forwarding + scraping the actual source websites) in the project plan.

---

### Pitfall 4: Context Window Exhaustion on Long Legal Documents

**What goes wrong:**
A state legislature publishes a 200-page omnibus privacy bill. The researcher agent tries to analyze it by feeding the full text into the Claude CLI prompt. The context window fills up, the model's attention degrades on the middle sections (the "lost in the middle" phenomenon), and the resulting report misses critical provisions buried in Sections 45-60 of the bill.

Research confirms LLMs preferentially attend to the beginning and end of long contexts, ignoring the middle — exactly where substantive legal provisions often reside.

**Why it happens:**
- Legal documents are long. A single state privacy bill can be 20,000-50,000 tokens. A federal rulemaking notice can be 100,000+ tokens.
- The Claude CLI subprocess has its own context window. The system prompt, agent instructions, and the document all compete for space.
- Developers assume "Claude has a large context window so it can handle anything" without understanding attention degradation.

**How to avoid:**
- Implement document chunking in the researcher agent: break long documents into logical sections (by article, section, or topic) and analyze each chunk separately.
- For legal documents specifically, chunk by structural boundaries (Title > Chapter > Section) rather than by token count. Legal cross-references depend on structural context.
- Use a two-pass approach: Pass 1 scans the full document for a table of contents / section summary. Pass 2 deep-dives into relevant sections identified in Pass 1.
- Set a hard token budget for source documents per agent call. If a document exceeds the budget, the orchestrator must chunk it before passing to the agent.

**Warning signs:**
- Reports that cover only the "highlights" or "key provisions" of long documents without mentioning specific section numbers from the middle of the document.
- Researcher agent calls that take unusually long (context-heavy calls are slower).
- Reports that accurately describe the first and last sections of a bill but are vague about the middle.

**Phase to address:**
Phase 2 (researcher agent). The chunking strategy must be part of the researcher agent's design, not an afterthought. Test with real long documents (grab a real state privacy bill) during development.

---

### Pitfall 5: Rate Limiting and Blocking on Government and Law Firm Sites

**What goes wrong:**
The scanner agent aggressively scrapes state legislature websites, federal register pages, and law firm blogs. Government sites have aggressive rate limits and primitive anti-bot defenses that block by IP. Law firm sites use Cloudflare or similar CDNs. The scanner gets IP-banned from key sources, and the pipeline goes blind to new developments from those sources — silently, because the scanner does not distinguish "no new content" from "blocked."

**Why it happens:**
- Government websites are often hosted on underpowered infrastructure with low rate-limit thresholds.
- Law firm websites increasingly use bot protection (Cloudflare, Akamai) that blocks automated access.
- Developers test with one or two requests and assume the pattern scales.
- The scanner does not track HTTP response codes, so a 403 or 429 looks the same as "nothing new."

**How to avoid:**
- Respect robots.txt. Check it for every source domain and honor Crawl-delay directives.
- Implement conservative rate limiting: minimum 10-15 seconds between requests to the same domain.
- Track and log HTTP response codes for every request. Distinguish "200 with no new content" from "403 blocked" from "429 rate limited."
- Build a source health dashboard (even if it is just a JSON status file): for each source, track last successful scrape, last error, consecutive error count. Alert if a source has been failing for more than 24 hours.
- Use the WebFetch/WebSearch MCP tools available in Claude Code rather than raw HTTP requests — they handle some anti-bot challenges.

**Warning signs:**
- Scanner reports "no new developments" for an extended period from a previously active source.
- HTTP 403 or 429 errors appearing in logs.
- Source websites loading fine in a browser but failing in the scanner.

**Phase to address:**
Phase 1 (scanner agent). Rate limiting and response code tracking must be built into the scanner from the first implementation, not added after the first ban.

---

### Pitfall 6: Over-Engineered Taxonomy Killing the Categorizer Agent

**What goes wrong:**
The categorizer agent is designed to maintain a complex, multi-level taxonomy with precise subcategories (e.g., `/privacy/biometric/state-laws/illinois/bipa-amendments/2026`). The taxonomy becomes so specific that: (a) most categories contain 1-2 reports, (b) finding anything requires knowing the exact path, (c) the categorizer agent spends most of its tokens debating where to file things, and (d) reports that span multiple topics get arbitrarily assigned to one category, losing discoverability.

**Why it happens:**
- Librarian instinct: the natural impulse is to create a perfect classification system upfront.
- The PROJECT.md wisely says "subcategories emerge organically" but without guardrails, the categorizer will create increasingly granular subcategories with each new report.
- Folder-based organization forces single-dimension classification. A report about "AI-generated deepfakes in political advertising" could be /ai-law, /privacy, or /cybersecurity.

**How to avoid:**
- Enforce a maximum depth of 2 levels: `/topic/subtopic/report.md`. Never deeper.
- Use frontmatter tags for cross-cutting concerns rather than trying to encode everything in the folder path. A report can be filed in `/privacy/biometric-data/` and tagged with `jurisdictions: [illinois, texas]`, `related-topics: [ai-law, employment]`.
- Set a minimum threshold for subcategory creation: a new subcategory is only justified when 3+ reports would belong there. Until then, reports stay in the parent category.
- The categorizer should maintain a simple `taxonomy.json` that lists all current categories and their report counts. Review it periodically to merge low-count categories.

**Warning signs:**
- More than 50% of subcategories contain only 1 report.
- The categorizer agent's output frequently mentions "this could go in X or Y" without a clear decision.
- Folder tree depth exceeds 3 levels.
- You cannot find a report you know exists without searching.

**Phase to address:**
Phase 3 (categorizer agent). But the taxonomy rules (max depth, minimum threshold) should be defined in Phase 1 as part of the file structure design.

---

### Pitfall 7: Reviewer Agent Rubber-Stamping Reports

**What goes wrong:**
The reviewer agent is supposed to independently verify source fidelity and legal accuracy. In practice, it reads the researcher's report, finds it "well-written and comprehensive," and approves it without actually checking sources. The 3-round iteration loop becomes 1 round of rubber-stamping. Every report passes review, and hallucinations go undetected until a human reads one and finds a fabricated statute.

**Why it happens:**
- LLMs are cooperative by default. Without adversarial prompting, the reviewer will find reasons to approve rather than reject.
- The reviewer does not have independent access to the source material — it is reviewing the researcher's summary of the sources, not the sources themselves.
- The reviewer's system prompt says "check for accuracy" but does not define specific, falsifiable checks to perform.

**How to avoid:**
- Give the reviewer agent independent web access to verify source URLs. The reviewer must fetch at least the key cited sources and confirm the claims match.
- Structure the reviewer's prompt as a checklist of specific verifications: (1) Does each cited URL exist and return content? (2) Does the cited source actually say what the report claims? (3) Are statute numbers, effective dates, and jurisdiction names correct? (4) Are there claims without citations?
- Include adversarial framing: "Your job is to find errors. A report that passes your review with zero corrections reflects poorly on your thoroughness. Assume the report contains at least one error and find it."
- Track reviewer metrics: if the reviewer approves 100% of reports in Round 1, the reviewer prompt needs tightening.

**Warning signs:**
- Reviewer consistently approves in Round 1 with no corrections.
- Reviewer feedback is generic ("well-researched, accurate") rather than specific ("verified Section 5(a) citation against source URL, confirmed").
- Human spot-checks find errors that the reviewer should have caught.

**Phase to address:**
Phase 2 (reviewer agent). The reviewer must be designed as an adversarial checker from the start. This is the single most important quality gate in the pipeline.

---

## Technical Debt Patterns

| Shortcut | Immediate Benefit | Long-term Cost | When Acceptable |
|----------|-------------------|----------------|-----------------|
| Passing full report text between agents via CLI args instead of files | Simpler orchestration, no file I/O | CLI argument length limits (128KB-2MB depending on OS), breaks with long reports | Never — use file-based handoff from day one |
| Skipping structured output schemas for agent responses | Faster initial development | Every downstream agent needs custom parsing; silent failures when format drifts | First prototype only; add schemas before second agent is built |
| Hardcoding source URLs in the scanner | Quick to get first scan working | Adding/removing sources requires code changes; no visibility into source health | First week of development; move to config file immediately after |
| Using `claude -p` without `--output-format json` | Simpler to read raw text output | Cannot reliably parse agent output programmatically; breaks on multi-line responses | Never for inter-agent communication; acceptable for human-facing final output |
| Storing reports without metadata/frontmatter | Reports are just markdown, easy to write | Cannot search, filter, or generate digests without parsing file content; categorization becomes guesswork | Never — frontmatter is trivial to add and essential for any future querying |

## Integration Gotchas

| Integration | Common Mistake | Correct Approach |
|-------------|----------------|------------------|
| Claude CLI subprocess | Assuming stdout is always clean JSON — Claude may emit warnings, progress messages, or MCP tool output mixed with the response | Use `--output-format json` and parse only the final JSON object. Capture stderr separately. |
| Claude CLI subprocess | Not setting `--max-turns` — agent runs indefinitely, burning tokens on tangents | Set explicit `--max-turns` per agent role. Scanner: 3-5 turns. Researcher: 10-15 turns. Reviewer: 5-8 turns. |
| Government websites (congress.gov, state legislatures) | Scraping HTML that changes structure frequently (session-specific URLs, dynamic rendering) | Target stable endpoints: RSS feeds, API endpoints where available (congress.gov has an API), PDF versions of bills. Prefer structured data over HTML scraping. |
| Law firm blogs | Scraping content that requires JavaScript rendering | Use MCP WebFetch or similar tools that handle JS rendering. Many law firm sites are React/Next.js SPAs. Test each source to confirm content is accessible without a full browser. |
| Email digest input | Parsing forwarded emails with inconsistent formatting (different email clients, quoted text, signatures) | Define a simple extraction format: the user saves the email body as a plain text or markdown file. Do not try to parse raw email headers, MIME boundaries, or HTML email. |

## Performance Traps

| Trap | Symptoms | Prevention | When It Breaks |
|------|----------|------------|----------------|
| Running all agent subprocesses sequentially when some could be parallel | Full pipeline takes 15-30 minutes for a single run | Scanner is sequential (one pass). But multiple researcher agents for different findings can run in parallel. Reviewer must wait for researcher. | When tracking 10+ sources with 5+ findings per run |
| No caching of scraped content | Same law firm blog post gets fetched 3 times (scanner reads it, researcher reads it, reviewer verifies it) | Cache scraped content by URL with a TTL (24 hours for news, 7 days for legislation). Store in a `/cache` directory. | Immediately — every pipeline run wastes tokens and risks rate limits |
| Loading full report history into categorizer context | Categorizer needs to know existing categories but loading all past reports fills the context window | Maintain a lightweight `taxonomy.json` with category names and report counts. Categorizer reads only this index, not all past reports. | After 50+ reports accumulated |
| Agent spawning overhead | Each `claude` CLI invocation has startup time (loading MCP servers, reading CLAUDE.md, initializing tools) | Minimize the number of agent invocations. Batch similar work. Do not spawn a new agent per source URL — have the scanner process all URLs in one invocation. | From day one — each agent spawn adds 5-15 seconds |

## Security Mistakes

| Mistake | Risk | Prevention |
|---------|------|------------|
| Storing scraped personal data (LinkedIn profiles, author bios) without data minimization | GDPR/CCPA exposure if reports contain personal data scraped without consent | Reports should cite sources by URL and organization, not by scraping personal profiles. If an author is mentioned, use publicly available professional attribution only. |
| Not sanitizing URLs before passing to agent subprocesses | Command injection via crafted URLs in source lists | Validate all URLs against an allowlist of domains. Never pass user-provided URLs directly to shell commands without sanitization. |
| Storing API keys or session tokens in CLAUDE.md or agent prompts | Credentials leak into Claude's context and potentially into output | Use environment variables for any credentials. Never embed secrets in prompts or configuration files that agents read. |
| Running all agents with `--dangerously-skip-permissions` | Agents can execute arbitrary shell commands, modify system files | Use permission profiles appropriate to each agent role. Scanner needs web access. Researcher needs web access and file write. Categorizer needs file read/write only. |

## UX Pitfalls

| Pitfall | User Impact | Better Approach |
|---------|-------------|-----------------|
| Pipeline runs silently for 20+ minutes with no progress indication | User assumes it is broken, kills the process, or starts a second run | Write progress to a status file or stdout: "Scanning source 3/12...", "Researching finding 2/5...", "Review round 1/3..." |
| Human confirmation step blocks the entire pipeline indefinitely | User forgets to confirm, pipeline sits idle for hours | Write pending confirmations to a file. If running in scheduled mode later, auto-proceed after a timeout with a "human review needed" flag on the output. |
| Reports use inconsistent formatting across different runs | Hard to scan, compare, or build a coherent knowledge base | Enforce a strict report template with required frontmatter fields. The researcher agent receives the template as part of its prompt, not as a suggestion. |
| No summary of what the pipeline did after completion | User must manually check output folders to see what happened | Generate a run summary: sources scanned, findings identified, reports produced, reports that needed human review, any errors. |

## "Looks Done But Isn't" Checklist

- [ ] **Scanner agent:** Does it actually detect NEW developments, or does it re-report known items every run? Verify it tracks "already seen" items between runs.
- [ ] **Researcher report:** Does every factual claim have a citation? Check for "general knowledge" statements that snuck in without sources.
- [ ] **Reviewer verification:** Did the reviewer actually fetch and check cited URLs, or just read the report and say "looks good"? Check reviewer logs for HTTP requests.
- [ ] **Categorizer filing:** Are reports discoverable? Try to find a specific report knowing only its topic, not its filename. If you cannot, the categorization is not working.
- [ ] **Pipeline idempotency:** Run the pipeline twice on the same inputs. Does it produce duplicate reports? It should not.
- [ ] **Error recovery:** Kill the pipeline mid-run. Can it resume or at least report what was completed? Orphaned partial reports are worse than no reports.
- [ ] **Source coverage:** Are all configured sources actually being scanned? Check that each source URL returns 200, not 403/404/timeout.

## Recovery Strategies

| Pitfall | Recovery Cost | Recovery Steps |
|---------|---------------|----------------|
| Hallucinated legal citations in published reports | MEDIUM | Audit all existing reports against their cited sources. Flag and quarantine reports with unverifiable claims. Re-run the researcher-reviewer loop on flagged reports with tightened prompts. |
| IP banned from a government source | LOW | Wait 24-48 hours (most bans are temporary). Reduce request rate. If permanent, use a different network path or find an alternative source (RSS feed, API). |
| Over-engineered taxonomy with 100+ subcategories | MEDIUM | Flatten: merge all subcategories with fewer than 3 reports into their parent. Update report frontmatter tags to preserve the lost categorization metadata. |
| Pipeline produced duplicate reports across runs | LOW | Deduplicate by comparing report topics/sources. Implement a "seen developments" index that persists between runs. |
| Agent error cascade produced corrupt reports | MEDIUM | Check pipeline manifest for which steps failed. Delete reports produced after the first failure. Re-run from the failed step with validated inputs. |
| Context window exhaustion on long document | LOW | Re-chunk the document with smaller sections. Re-run the researcher on just the missed sections. Merge results into the existing report. |

## Pitfall-to-Phase Mapping

| Pitfall | Prevention Phase | Verification |
|---------|------------------|--------------|
| LLM hallucination in legal reports | Phase 1 (report template) + Phase 2 (reviewer agent) | Human spot-check of 5 reports; verify every citation resolves and matches claims |
| Agent error cascade | Phase 1 (orchestrator design) | Intentionally feed malformed input to each agent; confirm pipeline halts with clear error |
| LinkedIn scraping trap | Phase 0 (project scoping) | Confirm no LinkedIn login/scraping code exists; verify alternative source strategy documented |
| Context window exhaustion | Phase 2 (researcher agent) | Test with a 50+ page legal document; verify report covers middle sections |
| Rate limiting / IP bans | Phase 1 (scanner agent) | Run scanner 3x consecutively; verify no 429/403 errors; check rate limiting delays in logs |
| Over-engineered taxonomy | Phase 1 (file structure) + Phase 3 (categorizer agent) | After 20 reports, verify max folder depth is 2 and no single-report subcategories exist |
| Reviewer rubber-stamping | Phase 2 (reviewer agent) | Intentionally introduce 3 errors into a report; verify reviewer catches at least 2 of 3 |

## Sources

- [Stanford Legal RAG Hallucinations Study (2025)](https://dho.stanford.edu/wp-content/uploads/Legal_RAG_Hallucinations.pdf) — hallucination rates in legal LLM output
- [Large Legal Fictions: Profiling Legal Hallucinations in LLMs](https://academic.oup.com/jla/article/16/1/64/7699227) — taxonomy of legal hallucination types
- [Why Multi-Agent LLM Systems Fail (arXiv 2025)](https://arxiv.org/html/2503.13657v1) — 17.2x error amplification, inter-agent misalignment
- [Claude Code Agent Teams Documentation](https://code.claude.com/docs/en/agent-teams) — official patterns for multi-agent Claude orchestration
- [Claude Code CLI Reference](https://code.claude.com/docs/en/cli-reference) — `--print`, `--output-format json`, `--max-turns`
- [hiQ v. LinkedIn Ruling Analysis](https://www.fbm.com/publications/what-recent-rulings-in-hiq-v-linkedin-and-other-cases-say-about-the-legality-of-data-scraping/) — LinkedIn scraping legality
- [LinkedIn Scraping Legal Guide 2026](https://sociavault.com/blog/linkedin-scraping-legal-guide-2026) — current enforcement landscape
- [Context Window Limitations in LLMs (2026)](https://atlan.com/know/llm-context-window-limitations/) — lost-in-the-middle phenomenon
- [AI Hallucinations in Legal Work (2026)](https://thelegalprompts.com/blog/ai-hallucinations-legal-work-avoid-sanctions-2026) — verification best practices
- [Knowledge Base Taxonomy Best Practices](https://www.matrixflows.com/blog/knowledge-base-taxonomy-best-practices) — taxonomy design principles

---
*Pitfalls research for: Multi-agent CLI regulatory monitoring pipeline (Zwiad)*
*Researched: 2026-04-06*
