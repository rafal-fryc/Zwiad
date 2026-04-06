# Feature Research

**Domain:** Regulatory monitoring platform for privacy, cybersecurity, and AI law
**Researched:** 2026-04-06
**Confidence:** MEDIUM-HIGH

## Feature Landscape

### Table Stakes (Users Expect These)

Features users assume exist. Missing these = product feels incomplete.

| Feature | Why Expected | Complexity | Notes |
|---------|--------------|------------|-------|
| Multi-source scanning | Every regulatory intelligence platform (Regology, Compliance.ai, NAVEX) monitors multiple source types. A scanner that only reads one input is useless. | MEDIUM | Start with email digests (already available) + government sites (congress.gov, state legislature sites). Law firm client alert websites are high-value, low-friction sources. |
| Source citation and linking | Regulatory intelligence is worthless without provenance. Users must verify claims against originals. Regology provides paragraph-level citations. | LOW | Every report must link back to the source URL. Non-negotiable for legal credibility. |
| Structured markdown reports | The core deliverable. Law firm client alerts follow a consistent structure: headline, key takeaway, background, analysis, action items. Users expect scannable, well-organized output. | MEDIUM | Two formats per PROJECT.md: client alert style (breaking news) and research memo style (complex analysis). Use subheadings, bullet lists, avoid legalese walls. |
| Topic-based categorization | Regology organizes by topic, jurisdiction, and industry. At minimum, filing reports into `/privacy`, `/cybersecurity`, `/ai-law` is expected baseline organization. | LOW | PROJECT.md already specifies this. Emergent subcategories are the right call -- avoid over-engineering taxonomy upfront. |
| Jurisdiction tagging | Privacy/cyber/AI law is inherently jurisdictional. A report about California CCPA amendments vs. a federal FTC action must be distinguishable. | LOW | Tag in frontmatter metadata. US federal + 50 states is the initial scope per PROJECT.md. |
| Human confirmation gate before research | Users do not trust fully autonomous AI pipelines for legal content. The EU AI Act and industry practice both mandate human oversight for high-risk AI outputs. Scanner presents findings, human approves before research proceeds. | LOW | Already in PROJECT.md requirements. This is table stakes for trust, not a nice-to-have. |
| Source fidelity verification | Independent review that claims are supported by cited sources. This is the #1 differentiator between useful and dangerous AI-generated legal content. Hallucinated statute numbers or misattributed holdings destroy credibility. | HIGH | Reviewer agent checks: correct statute citations, accurate dates, proper jurisdiction attribution, claims match source content. The 3-round cap with human escalation is sound. |
| Deduplication / novelty detection | Multiple sources often cover the same development (e.g., 15 law firms write about the same FTC enforcement action). Users expect the system to recognize "this is the same event" and consolidate. | MEDIUM | Compare new findings against recent reports in the filesystem. Hash or fuzzy-match on key entities (statute, jurisdiction, date, parties). |
| Pipeline status and audit trail | Users need to know what happened: what was scanned, what was approved, what was researched, what passed/failed review. Basic operational transparency. | LOW | Write a pipeline run log (JSON or markdown) for each execution. Record timestamps, agent outputs, human decisions, review iterations. |

### Differentiators (Competitive Advantage)

Features that set Zwiad apart from commercial platforms (Regology at $50K+/yr, Compliance.ai enterprise pricing) and from manual monitoring.

| Feature | Value Proposition | Complexity | Notes |
|---------|-------------------|------------|-------|
| Adaptive report format | Commercial platforms produce uniform output. Zwiad adapts: client alert style for breaking news (short, actionable), research memo style for complex analysis (deep, multi-source). The categorizer/researcher chooses format based on development type. | MEDIUM | Define 2-3 report templates. Let the researcher agent select based on criteria: urgency, complexity, number of affected jurisdictions. |
| Iterative researcher-reviewer loop | Most AI writing tools do single-pass generation. The multi-round adversarial review (researcher writes, reviewer challenges, up to 3 rounds) produces significantly more reliable output. This mimics law firm editorial process. | HIGH | Core architectural differentiator. Reviewer must be genuinely independent -- different system prompt, different evaluation criteria. Not just "does this read well" but "are the legal claims accurate." |
| Emergent taxonomy / organic subcategories | Commercial platforms use rigid pre-defined taxonomies. Zwiad lets subcategories emerge as content accumulates (e.g., `/privacy/state-comprehensive-laws`, `/ai-law/employment-decisions`). Adapts to the actual regulatory landscape rather than predicting it. | MEDIUM | Categorizer agent examines existing folder structure + report content to decide placement. Periodically suggest reorganization when subcategories grow unwieldy. |
| Cross-development linking | When a new state privacy law passes, link to related reports (other states' similar laws, federal proposals, enforcement actions). Builds a knowledge web, not just a file dump. | MEDIUM | Markdown cross-references between reports. Categorizer agent adds "Related reports" section based on shared entities (statute type, jurisdiction, topic). |
| Email digest as input source | Unique to this use case: user already receives curated daily law firm digests. Instead of building complex web scrapers for every source, leverage the human-curated email as primary input. Dramatically reduces the cold-start source problem. | LOW | Parse forwarded email (plain text or HTML). Extract law firm alert links, development summaries. This is the highest-ROI input source because it is already curated by domain experts. |
| Cost structure (zero API cost) | Commercial platforms cost $20K-100K+/year. Zwiad runs on Claude Code CLI usage (included in subscription). For a solo practitioner or small team, this is transformative. | LOW | Not a feature per se, but a structural advantage that shapes every design decision. |
| LinkedIn feed integration | LinkedIn is where privacy/cyber lawyers share commentary and early signals about regulatory developments. No commercial platform integrates LinkedIn well. | HIGH | Feasibility uncertain per PROJECT.md. Likely requires manual copy-paste or browser extension rather than API access. Defer to v1.x -- email digests provide sufficient initial coverage. |
| Confidence scoring per claim | Go beyond binary "verified/not verified." Rate each factual claim in a report: HIGH (confirmed against primary source), MEDIUM (confirmed against secondary source), LOW (single source, unverified). | MEDIUM | Reviewer agent annotates claims. Visible in report metadata or inline. Helps human reader calibrate trust. |
| Multi-jurisdictional comparison tables | When multiple states pass similar laws (e.g., comprehensive privacy statutes), auto-generate comparison tables showing key differences: scope, rights granted, enforcement mechanisms, effective dates. | HIGH | High value for practitioners tracking the patchwork. Requires structured extraction from multiple reports. Good v2 feature after knowledge base exists. |

### Anti-Features (Commonly Requested, Often Problematic)

| Feature | Why Requested | Why Problematic | Alternative |
|---------|---------------|-----------------|-------------|
| Real-time monitoring / streaming | "I want to know the instant something happens." | Regulatory changes don't happen in real-time. Bills are introduced, go through committee, get amended -- on timescales of days/weeks. Real-time adds massive complexity (webhooks, persistent processes, rate limiting) for zero practical benefit. Daily/manual batch is sufficient. | Daily batch processing with manual trigger. If something is truly urgent, the email digest will surface it same-day. |
| Web UI / dashboard | "I want pretty charts and a search bar." | Massive scope expansion. Frontend framework, hosting, auth, state management. Delays core value delivery by months. The target user is a lawyer who reads markdown -- they do not need a React app. | Well-organized markdown files in a structured directory. Use existing tools (VS Code, Obsidian, grep) for search and navigation. Knowledge base / search index is explicitly out of scope per PROJECT.md. |
| Fully autonomous operation (no human gate) | "Just run it and send me the reports." | AI-generated legal content without human review is a liability risk. Hallucinated statute citations, mischaracterized holdings, or incorrect jurisdiction assignments could lead to malpractice if relied upon. Trust must be earned incrementally. | Human confirmation before research (v1). Gradually reduce oversight as track record builds. PROJECT.md correctly identifies this as future milestone "after trust is established." |
| Paywalled database integration (Westlaw, LexisNexis, Bloomberg Law) | "Get the authoritative source from legal databases." | Requires expensive subscriptions ($10K+/yr per database), complex authentication, and terms-of-service compliance. Scraping these services violates ToS. | Use freely available government primary sources (legislature sites, federal register, court filings) supplemented by law firm client alerts that synthesize paywalled content. |
| Comprehensive global jurisdiction coverage | "Track EU, UK, APAC, LATAM regulations too." | Scope explosion. Each jurisdiction has different legislative structures, languages, source websites. Going global before nailing US coverage means doing everything poorly. | US federal + state only for v1. Architecture should not preclude international expansion, but do not build for it now. |
| Natural language query interface | "Ask questions about the knowledge base." | Requires vector store, embeddings, RAG pipeline -- all explicitly out of scope. Premature optimization before the knowledge base has sufficient content to query meaningfully. | Build the report corpus first. Query interface is a separate future project per PROJECT.md (knowledge base / vector store). |
| Automated action item generation | "Tell me what my clients need to do." | Legal advice is context-dependent. Generic "action items" from AI could be dangerously wrong for specific client situations. Creates liability exposure. | Reports describe the regulatory development and its implications. Leave specific client advice to the human lawyer reading the report. |

## Feature Dependencies

```
[Email Digest Parsing]
    +--requires--> [Source Citation/Linking]
    +--feeds-----> [Scanner Agent: Development Identification]
                       +--requires--> [Deduplication / Novelty Detection]
                       +--requires--> [Human Confirmation Gate]
                                          +--feeds--> [Researcher Agent: Report Writing]
                                                          +--requires--> [Structured Report Templates]
                                                          +--requires--> [Jurisdiction Tagging]
                                                          +--feeds--> [Reviewer Agent: Verification Loop]
                                                                          +--requires--> [Source Fidelity Checking]
                                                                          +--feeds--> [Categorizer Agent: Filing]
                                                                                          +--requires--> [Topic Categorization]
                                                                                          +--enhances--> [Cross-Development Linking]

[Pipeline Audit Trail] --enhances--> [All Pipeline Stages]

[Adaptive Report Format] --enhances--> [Researcher Agent]

[Confidence Scoring] --enhances--> [Reviewer Agent]

[Emergent Taxonomy] --enhances--> [Categorizer Agent]

[LinkedIn Integration] --conflicts--> [v1 Scope] (defer)
[Multi-Jurisdictional Comparison] --requires--> [Sufficient Report Corpus]
```

### Dependency Notes

- **Human Confirmation Gate requires Scanner output:** Scanner must present structured findings (title, source, summary, relevance score) for human to make informed approve/reject decisions.
- **Reviewer requires Source Fidelity Checking:** The reviewer agent's primary job is verification. Without the ability to check claims against sources, it is just a style editor -- that is not the point.
- **Cross-Development Linking requires Topic Categorization:** Cannot link related reports without a categorization system to identify relationships.
- **Deduplication requires some prior report history:** First run has nothing to deduplicate against. This feature becomes critical by run 3-4 as source overlap becomes apparent.
- **Emergent Taxonomy enhances but does not block Categorizer:** v1 categorizer can use fixed top-level categories. Emergent subcategories layer on top.

## MVP Definition

### Launch With (v1)

Minimum viable product -- what is needed to validate the concept.

- [ ] Email digest parser -- extract law firm alert links and development summaries from forwarded email file
- [ ] Scanner agent -- identify noteworthy developments from parsed input, present structured findings
- [ ] Human confirmation gate -- CLI prompt showing findings, user approves/rejects each before proceeding
- [ ] Researcher agent -- produce markdown report from confirmed finding using web sources, with source citations
- [ ] Two report templates -- client alert format and research memo format
- [ ] Reviewer agent -- independently verify source fidelity, legal accuracy; iterate up to 3 rounds
- [ ] Human escalation -- flag unresolved researcher-reviewer disagreements after 3 rounds
- [ ] Categorizer agent -- file reports into `/privacy`, `/cybersecurity`, `/ai-law` with jurisdiction metadata
- [ ] Pipeline run log -- record what was scanned, approved, researched, reviewed, filed
- [ ] Basic deduplication -- check if a development was already reported (title/entity similarity against existing reports)

### Add After Validation (v1.x)

Features to add once core pipeline is working reliably.

- [ ] Emergent subcategories -- categorizer proposes and creates subcategories based on content patterns
- [ ] Cross-development linking -- "Related reports" section with markdown links between related developments
- [ ] Confidence scoring -- reviewer annotates claims with HIGH/MEDIUM/LOW verification confidence
- [ ] Adaptive format selection -- researcher auto-selects alert vs memo format based on development characteristics
- [ ] Government source scanning -- direct monitoring of congress.gov, state legislature sites, Federal Register
- [ ] LinkedIn integration -- if feasible, parse LinkedIn posts shared by followed privacy/cyber lawyers
- [ ] Daily scheduled execution -- move from manual trigger to Claude Code scheduled tasks

### Future Consideration (v2+)

Features to defer until report corpus is substantial and pipeline is trusted.

- [ ] Multi-jurisdictional comparison tables -- requires sufficient corpus of state-level reports to compare
- [ ] Knowledge base / vector store / search -- explicitly out of scope per PROJECT.md, separate project
- [ ] Natural language querying over report corpus
- [ ] Reduced human oversight (autonomous mode) -- only after trust is established through consistent accuracy
- [ ] International jurisdiction expansion -- after US coverage is solid
- [ ] Report distribution (email/Slack alerts to team members)

## Feature Prioritization Matrix

| Feature | User Value | Implementation Cost | Priority |
|---------|------------|---------------------|----------|
| Email digest parsing | HIGH | LOW | P1 |
| Scanner agent (development identification) | HIGH | MEDIUM | P1 |
| Human confirmation gate | HIGH | LOW | P1 |
| Researcher agent (report writing) | HIGH | HIGH | P1 |
| Structured report templates | HIGH | LOW | P1 |
| Source citation and linking | HIGH | LOW | P1 |
| Reviewer agent (verification loop) | HIGH | HIGH | P1 |
| Jurisdiction tagging (frontmatter metadata) | MEDIUM | LOW | P1 |
| Topic categorization (3 top-level folders) | MEDIUM | LOW | P1 |
| Pipeline run log / audit trail | MEDIUM | LOW | P1 |
| Basic deduplication | MEDIUM | MEDIUM | P1 |
| Human escalation (3-round cap) | HIGH | LOW | P1 |
| Emergent subcategories | MEDIUM | MEDIUM | P2 |
| Cross-development linking | MEDIUM | MEDIUM | P2 |
| Confidence scoring per claim | MEDIUM | MEDIUM | P2 |
| Adaptive format selection | LOW | LOW | P2 |
| Government source scanning | HIGH | HIGH | P2 |
| Scheduled daily execution | MEDIUM | LOW | P2 |
| LinkedIn integration | MEDIUM | HIGH | P3 |
| Multi-jurisdictional comparison tables | HIGH | HIGH | P3 |
| Knowledge base / search | HIGH | HIGH | P3 (separate project) |

**Priority key:**
- P1: Must have for launch
- P2: Should have, add when pipeline is validated
- P3: Nice to have, future consideration

## Competitor Feature Analysis

| Feature | Regology ($50K+/yr) | Compliance.ai (Enterprise) | NAVEX | Zwiad (CLI/local) |
|---------|---------------------|---------------------------|-------|-------------------|
| Source monitoring | 6,200+ vetted sources, 246+ jurisdictions | Unlimited regulatory sources, ML-filtered | Daily alerts filtered by jurisdiction/topic | Email digests + web sources (focused, not comprehensive) |
| Categorization | Topic, jurisdiction, industry, compliance object mapping | User-configurable preferences by agency/topic | Jurisdiction + topic + stage filtering | Topic folders + jurisdiction tags, emergent subcategories |
| Report types | 50+ pre-built dashboards, custom reports | Real-time dashboards, custom alerts | Filtered alert feed | Client alerts + research memos (markdown) |
| Verification | Human compliance team curation | ML models + human review | Editorial review | Adversarial researcher-reviewer agent loop |
| Change visualization | Redlined amendment tracking | Before/after comparisons | Change summaries | Full report per development (not diff-based) |
| Human oversight | Workflow task assignment | Team-based review | Owner assignment | Human gate before research + escalation after review |
| Cost | $50K-100K+/year | Enterprise pricing (undisclosed) | Enterprise pricing | Claude Code subscription only |
| Deployment | Cloud SaaS | Cloud SaaS | Cloud SaaS | Local CLI, local filesystem |

**Zwiad's competitive position:** Not competing with enterprise platforms on coverage or polish. Competing on: (1) cost (orders of magnitude cheaper), (2) verification rigor (adversarial agent review vs. single-pass ML), (3) adaptability (user controls the pipeline, can modify agent prompts), (4) privacy (everything runs locally, no data leaves the machine except web searches).

## Sources

- [Regology Platform](https://www.regology.com/platform) -- Feature set, Smart Law Library, categorization approach
- [Compliance.ai Regulatory Intelligence](https://www.compliance.ai/solution/regulatory-intelligence/) -- Source monitoring, alerting capabilities
- [NAVEX Regulatory Change Management](https://www.navex.com/en-us/platform/regulatory-change-management/) -- Alert filtering, jurisdiction/topic organization
- [Visualping Regulatory Intelligence](https://visualping.io/regulatory-intelligence) -- Web change monitoring approach
- [Reputation Ink: Client Alert Best Practices](https://www.rep-ink.com/inksights/how-to-write-better-client-alerts-10-of-the-best-tips/) -- Report structure and format standards
- [Kiteworks: Human in the Loop for AI Compliance](https://www.kiteworks.com/regulatory-compliance/human-in-the-loop-ai-compliance/) -- HITL requirements in regulated domains
- [Zapier: Human-in-the-Loop AI Workflows](https://zapier.com/blog/human-in-the-loop/) -- HITL vs HOTL patterns
- [Fast.io: Agent-to-Agent File Communication](https://fast.io/resources/agent-to-agent-file-communication-protocols/) -- File-based inter-agent communication patterns
- [Addy Osmani: Code Agent Orchestra](https://addyosmani.com/blog/code-agent-orchestra/) -- Multi-agent CLI orchestration patterns
- [White & Case: AI Watch Global Regulatory Tracker](https://www.whitecase.com/insight-our-thinking/ai-watch-global-regulatory-tracker-united-states) -- Example of regulatory tracking taxonomy
- [Centraleyes: Best Regulatory Change Management Software 2026](https://www.centraleyes.com/best-regulatory-change-management-software/) -- Market landscape overview

---
*Feature research for: Regulatory monitoring platform (privacy/cybersecurity/AI law)*
*Researched: 2026-04-06*
