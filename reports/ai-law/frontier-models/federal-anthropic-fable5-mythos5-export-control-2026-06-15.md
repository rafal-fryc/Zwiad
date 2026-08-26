---
title: "US Orders Anthropic to Halt Foreign National Access to Frontier AI Models Fable 5 and Mythos 5"
date: 2026-06-15
jurisdiction: "Federal"
category: "ai-law"
development_type: "regulation"
finding_id: "SCAN-20260628-003"
topic_key: "federal-bb7a435d-2026"
topic_type: "rulemaking"
first_reported: 2026-06-15
last_updated: 2026-06-29
status_history:
  - "2026-06-29: Revision r1 — corrected Summary citation for ~100 Glasswing organizations (added Axios/Semafor inline); clarified CNBC/NPR date attribution for Lutnick letter vs. reporting date; confirmed Legal Analysis MCTL language already matched reviewer suggested fix."
cluster: "BIS Export Controls on Frontier AI Model Access: Anthropic Fable 5 and Mythos 5"
cluster_slug: "bis-export-controls-frontier-ai-models"
---

# US Orders Anthropic to Halt Foreign National Access to Frontier AI Models Fable 5 and Mythos 5

**Jurisdiction:** Federal | **Category:** AI Law | **Date:** June 15, 2026

## Summary [HIGH confidence]

On June 12, 2026, the US Department of Commerce Bureau of Industry and Security (BIS) issued an unprecedented "Is Informed" letter to Anthropic ordering it to suspend all access to its two most advanced AI models — Fable 5 and Mythos 5 — by any foreign national anywhere in the world, including foreign national employees at Anthropic itself. Anthropic, disputing the government's rationale but unable to comply selectively, disabled both models globally for all customers. As of June 27, Commerce Secretary Howard Lutnick partially reversed course, restoring Mythos 5 access for approximately 100 approved companies and government agencies listed in Annex A of Lutnick's June 26 letter — entities participating in Anthropic's Project Glasswing cybersecurity program — while Fable 5 remains suspended for general use. ([Axios](https://www.axios.com/2026/06/27/commerce-anthropic-mythos-restrictions-lift), [Semafor](https://www.semafor.com/article/06/27/2026/us-releases-powerful-anthropic-model-mythos-to-some-us-companies)) This is the first time the US government has applied export controls directly to AI model access rather than to the underlying hardware.

## Key Facts [HIGH confidence]

- Anthropic launched Fable 5 and Mythos 5 on June 9, 2026; BIS issued an "Is Informed" directive just three days later on June 12 at 5:21 PM ET, citing national security authorities under the [Export Control Reform Act of 2018 (ECRA), 50 U.S.C. § 4817(b)(1)](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title50-section4817&num=0&edition=prelim) and 15 C.F.R. § 744.22(b) of the [Export Administration Regulations (EAR)](https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-744). ([Cybersecurity News](https://cybersecuritynews.com/claude-mythos-5-and-fable-5-export/amp/))
- The directive was triggered by a reported jailbreak path allowing potential bypass of Mythos 5's safety guardrails. [Anthropic's official statement](https://www.anthropic.com/news/fable-mythos-access) noted that the government provided only verbal evidence of a "potential narrow, non-universal jailbreak" — one that Anthropic contended also applied to publicly available models such as OpenAI's GPT-5.5 not subject to similar controls. ([Fortune](https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/))
- The jailbreak concern originated from Amazon's research team, whose CEO Andy Jassy reportedly shared the finding with the government. ([Fortune](https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/))
- Mythos 5 is particularly capable of detecting previously undiscovered software vulnerabilities across major operating systems and web browsers. Fable 5, released the same week, is built on Mythos technology but launched with cybersecurity and biotechnology capabilities restricted. ([Al Jazeera](https://www.aljazeera.com/news/2026/6/13/us-orders-anthropic-to-disable-ai-models-for-all-foreign-nationals))
- The "Is Informed" mechanism allows Commerce to impose export license requirements on specific parties or items without going through formal rulemaking — its use at this breadth and applied directly to AI model access (rather than hardware or software code) is legally unprecedented. ([Just Security](https://www.justsecurity.org/142745/law-anthropic-export-controls/))
- On June 18, four bipartisan House members — Reps. Sam Liccardo (D-CA), Jay Obernolte (R-CA), Ted Lieu (D-CA), and Scott Franklin (R-FL) — sent a letter to Commerce Secretary Lutnick demanding the legal and technical basis for the directive, setting a June 26 deadline for a response. ([Congressman Sam Liccardo press release](https://liccardo.house.gov/media/press-releases/bipartisan-members-congress-seek-transparency-frontier-ai-export-controls))
- Lutnick's letter, dated June 26, authorized Mythos 5 access for approximately 100 trusted companies, federal agencies, research institutions, and critical infrastructure operators listed in Annex A; reporting of the restoration appeared widely on June 27. ([NPR](https://www.npr.org/2026/06/27/nx-s1-5871245/trump-administration-imposes-restrictions-for-anthropic-to-halt-access-to-2-ai-models), [Axios](https://www.axios.com/2026/06/27/commerce-anthropic-mythos-restrictions-lift), [Semafor](https://www.semafor.com/article/06/27/2026/us-releases-powerful-anthropic-model-mythos-to-some-us-companies), [CNBC](https://www.cnbc.com/2026/06/26/us-government-anthropic-claude-mythos5-ai.html)) The authorized entities are participants in [Project Glasswing](https://www.anthropic.com/news/expanding-project-glasswing), Anthropic's vetted cybersecurity program, which had already expanded to 150 organizations in a June 2 announcement prior to the export control order. Fable 5 remains suspended for general users.
- Over 100 cybersecurity executives — including Alex Stamos, Chris Wysopal, and Joe Levy — signed an open letter at freefable.org arguing the ban removes frontier defensive AI from security professionals without justified risk. ([TechPolicy.Press](https://www.techpolicy.press/did-the-us-government-just-set-an-ai-export-precedent-by-blocking-mythos/))

## Legal Analysis [MEDIUM confidence]

The BIS order invokes two distinct authorities:

1. **ECRA § 4817(b)(1)** — empowers BIS to establish interim controls on "emerging and foundational technologies" essential to national security without completing formal rulemaking. This provision was designed to fill gaps in the Export Administration Regulations for technologies not yet formally listed as controlled items under existing law, while longer-term regulations are developed.

2. **EAR § 744.22(b)** — permits BIS to require export licenses when there is an unacceptable risk of use in or diversion to a "military-intelligence end use" or "military-intelligence end user."

The "Is Informed" mechanism is not itself novel — BIS has used it in the semiconductor context — but applying it to restrict access to an AI model (rather than hardware or software code) raises unresolved questions about what constitutes an "export" in a cloud-accessed, API-delivered service context. The [Harvard Law Review](https://harvardlawreview.org/blog/2026/06/is-access-to-fable-an-export/) and [CSIS](https://www.csis.org/analysis/department-commerce-restricted-access-anthropics-latest-models-what-comes-next) both note that Commerce has not promulgated a formal rule classifying frontier AI model access as an export-controlled item, making the legal underpinning of this order contested. [Just Security's legal analysis](https://www.justsecurity.org/142745/law-anthropic-export-controls/) questions the statutory authority's application to inference-as-a-service: the statute's language is brief and nonspecific, and the agency is operating at the outermost edge of its delegated authority.

The partial restoration via Project Glasswing establishes a de facto licensing regime: only parties on an approved list may access the controlled model. This mirrors export license exception frameworks used for hardware but has no established regulatory analogue for AI.

## Action Items

- **Frontier AI developers** should immediately audit whether their most capable models could face similar "Is Informed" classification under EAR § 744.22(b) — particularly models with advanced cybersecurity, biotechnology, or dual-use capabilities — and engage BIS proactively about licensing pathway options.
- **Enterprises with foreign national employees or contractors** that rely on frontier AI model access (especially Anthropic's Claude suite) should review workforce access policies and assess exposure to disruption if additional models are brought under export control.
- **Organizations seeking Mythos 5 access** should apply through [Project Glasswing](https://www.anthropic.com/glasswing), which currently covers approximately 100 organizations; Anthropic has signaled plans for further expansion.
- **Compliance officers** should monitor CSIS, Just Security, and Congressional press releases for any formal rulemaking by BIS to codify AI model export controls, which would establish clearer compliance obligations and classification criteria.
- **Policy and government affairs teams** should track proposed congressional AI export control legislation that may formalize — or limit — BIS authority to unilaterally restrict AI model access.

## Related Reports

- [reports/ai-law/frontier-models/federal-anthropic-project-glasswing-claude-mythos-2026-04-14.md](reports/ai-law/frontier-models/federal-anthropic-project-glasswing-claude-mythos-2026-04-14.md) -- The prior Glasswing/Mythos report details the cybersecurity vetting program that became the vehicle for the partial export control reversal.
- [reports/ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md](reports/ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md) -- Trump's December 2025 AI Executive Order established the national AI policy and security framework that provides political context for the Commerce Department's aggressive use of export controls.
- [reports/ai-law/federal-regulation/federal-trump-ai-cabinet-divisions-2026-06-01.md](reports/ai-law/federal-regulation/federal-trump-ai-cabinet-divisions-2026-06-01.md) -- Reports intra-administration conflict over AI policy, directly relevant to understanding the policy environment in which the Fable/Mythos export directive was issued.

## Sources

1. [Anthropic Official Statement on Fable 5 and Mythos 5 Suspension](https://www.anthropic.com/news/fable-mythos-access) -- Primary source: Anthropic's public statement disputing the government's rationale and describing model suspension.
2. [Al Jazeera: US orders Anthropic to disable AI models for all foreign nationals](https://www.aljazeera.com/news/2026/6/13/us-orders-anthropic-to-disable-ai-models-for-all-foreign-nationals) -- Primary news coverage of the June 12 directive and scope.
3. [Fortune: Anthropic disables Fable and Mythos AI models following U.S. government export ban](https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/) -- Details on Amazon/Jassy jailbreak report and Anthropic's objections.
4. [Time: Anthropic Pulls Its Most Powerful AI Models After U.S. Bars Foreign Access](https://time.com/article/2026/06/13/anthropic-fable-mythos-ban-US-security/) -- News coverage of the suspension.
5. [Anthropic on X (@AnthropicAI)](https://x.com/AnthropicAI/status/2065597531644743999) -- Official Anthropic statement thread on the government directive scope.
6. [Nextgov/FCW: Anthropic suspends top AI models after U.S. export control order](https://www.nextgov.com/artificial-intelligence/2026/06/anthropic-suspends-top-ai-models-after-us-export-control-order/414173/) -- Federal IT coverage; dates and legal structure.
7. [CSIS: The Department of Commerce Restricted Access to Anthropic's Latest Models. What Comes Next?](https://www.csis.org/analysis/department-commerce-restricted-access-anthropics-latest-models-what-comes-next) -- Independent think-tank Q&A analysis of regulatory authority and precedent.
8. [Just Security: Legal Considerations Related to the Anthropic "Export Controls Directive"](https://www.justsecurity.org/142745/law-anthropic-export-controls/) -- Legal analysis of statutory authority and "Is Informed" mechanism limits.
9. [Harvard Law Review: Is Access to Fable an Export?](https://harvardlawreview.org/blog/2026/06/is-access-to-fable-an-export/) -- Scholarly analysis of whether cloud-based AI model access constitutes an "export" under EAR.
10. [Congressman Sam Liccardo: Bipartisan Members of Congress Seek Transparency on Frontier AI Export Controls](https://liccardo.house.gov/media/press-releases/bipartisan-members-congress-seek-transparency-frontier-ai-export-controls) -- Official press release: bipartisan House letter to Commerce Secretary.
11. [CNBC: Trump admin allows Anthropic to release Mythos AI model to some companies, government agencies](https://www.cnbc.com/2026/06/26/us-government-anthropic-claude-mythos5-ai.html) -- Reports partial reversal; Lutnick letter dated June 26 authorizing Mythos 5 for approved entities.
12. [NPR: Trump administration partially lifts export ban on Anthropic's most advanced AI model](https://www.npr.org/2026/06/27/nx-s1-5871245/trump-administration-imposes-restrictions-for-anthropic-to-halt-access-to-2-ai-models) -- Confirms Lutnick letter and scope of the partial restoration; widely reported June 27.
13. [Anthropic: Expanding Project Glasswing](https://www.anthropic.com/news/expanding-project-glasswing) -- Anthropic's official announcement of the June 2 Glasswing expansion to 150 organizations (pre-ban event; cited for the Glasswing program background, not for post-ban restoration figures).
14. [TechPolicy.Press: Did the US Government Just Set An AI Export Precedent by Blocking Mythos?](https://www.techpolicy.press/did-the-us-government-just-set-an-ai-export-precedent-by-blocking-mythos/) -- Analysis of precedent-setting nature and open letter from cybersecurity executives.
15. [Cybersecurity News: U.S. Commerce Dept Imposes Export Controls on Anthropic's Claude Mythos 5 and Fable 5](https://cybersecuritynews.com/claude-mythos-5-and-fable-5-export/amp/) -- Detailed reporting on the EAR legal authorities invoked.
16. [Axios: Anthropic's Mythos is coming back for a select group of entities approved by the U.S. government](https://www.axios.com/2026/06/27/commerce-anthropic-mythos-restrictions-lift) -- Confirms the post-ban Annex A restoration to approximately 100 approved entities and Lutnick letter terms.
17. [Semafor: US releases powerful Anthropic model Mythos to some US companies](https://www.semafor.com/article/06/27/2026/us-releases-powerful-anthropic-model-mythos-to-some-us-companies) -- Exclusive reporting confirming the Annex A restoration count and scope of the partial reversal.
