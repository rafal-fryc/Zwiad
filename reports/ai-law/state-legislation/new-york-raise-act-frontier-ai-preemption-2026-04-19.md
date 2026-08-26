---
title: "New York RAISE Act and Federal Preemption: Frontier AI Developer Compliance in a Contested Regulatory Landscape"
date: 2026-04-19
jurisdiction: "New York"
category: "ai-law"
development_type: "legislation"
finding_id: "SCAN-20260419-030"
topic_key: "NY-RAISE-ACT-FEDERAL-PREEMPTION-2026"
topic_type: "state_bill"
first_reported: 2026-04-19
last_updated: 2026-04-19
status_history: []
cluster: "New York RAISE Act: Frontier AI Safety and Federal Preemption"
cluster_slug: "new-york-raise-act-frontier-ai-safety"
---

# New York RAISE Act and Federal Preemption: Frontier AI Developer Compliance in a Contested Regulatory Landscape

**Jurisdiction:** New York / Federal | **Category:** ai-law | **Date:** 2026-04-19

## Executive Summary [HIGH confidence]

New York's [Responsible AI Safety and Education (RAISE) Act](https://www.nysenate.gov/legislation/bills/2025/S8828) — signed December 19, 2025 and finalized through chapter amendments signed March 27, 2026 — is now the most substantive enacted frontier AI safety law in the United States, imposing safety protocol publication, 72-hour incident reporting, and annual review requirements on large frontier model developers operating in New York. Full compliance is required by January 1, 2027. The RAISE Act arrives simultaneously with an aggressive federal preemption campaign: President Trump's December 11, 2025 executive order directed the Department of Justice to establish an AI Litigation Task Force (operational as of January 9, 2026) to challenge state AI laws deemed inconsistent with federal policy, and the March 20, 2026 National Policy Framework for AI formally recommended that Congress preempt state laws imposing "undue burdens" on AI development. Whether the RAISE Act falls within the scope of federal preemption efforts remains legally uncertain, as the RAISE Act's focus on transparency and catastrophic-risk safety protocols may not clearly conflict with any existing federal statute — but its regulatory footprint is broad enough that affected developers should prepare for both compliance and potential litigation-driven disruption.

## Background [HIGH confidence]

### State AI Regulation Accelerates Nationally

The landscape of state AI legislation has expanded dramatically in 2025–2026. More than 1,000 AI-related bills were introduced across US states and territories in 2025 alone, with over 600 new bills with private-sector requirements introduced in Q1 2026 according to [Alston & Bird's April 2026 AI Quarterly](https://www.alston.com/en/insights/publications/2026/04/ai-quarterly-april-2026). States have focused particularly on: (1) transparency and disclosure requirements for AI-generated content; (2) safety and accountability frameworks for large or "frontier" AI models; and (3) consumer protection in specific contexts such as companion chatbots, healthcare, and employment.

New York's RAISE Act is the flagship of the frontier-model safety category. It was signed just eight days after President Trump issued his December 11, 2025 executive order specifically targeting state AI laws — making the RAISE Act a live test of how the federal-state tension will resolve in practice.

### Federal Response: The December 2025 Executive Order

On December 11, 2025, President Trump signed an executive order titled ["Ensuring a National Policy Framework for Artificial Intelligence"](https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/) (also styled "Eliminating State Law Obstruction of National Artificial Intelligence Policy"). The order declared US policy to pursue "global AI dominance through a minimally burdensome national policy framework" and directed a sequenced set of federal agency actions:

- **DOJ AI Litigation Task Force:** The Attorney General was directed to establish a task force to challenge state AI laws on grounds of unconstitutional regulation of interstate commerce, federal preemption, or other unlawfulness.
- **Commerce/BEAD conditions:** Within 90 days, the Secretary of Commerce was to identify conditions for BEAD broadband funding eligibility, potentially disqualifying states with "onerous" AI laws.
- **FTC policy statement:** By March 11, 2026, the FTC was directed to issue a policy statement explaining when state laws requiring alterations to the "truthful outputs of AI models" are preempted by the FTC Act.
- **FCC proceeding:** The FCC was directed to consider a federal reporting and disclosure standard for AI models.

As [Sidley Austin analyzed](https://datamatters.sidley.com/2025/12/23/unpacking-the-december-11-2025-executive-order-ensuring-a-national-policy-framework-for-artificial-intelligence/), the DOJ AI Litigation Task Force became operational on January 9, 2026, when Attorney General Pam Bondi issued an internal memorandum formally establishing it. The task force will challenge state laws on the grounds that they are illegal, unconstitutionally regulate interstate commerce, or are overridden by existing federal regulations, per the [DOJ memorandum](https://www.justice.gov/ag/media/1422986/dl?inline=).

### March 2026 National Policy Framework

On March 20, 2026, the White House released the [National Policy Framework for Artificial Intelligence legislative recommendations](https://www.whitehouse.gov/wp-content/uploads/2026/03/03.20.26-National-Policy-Framework-for-Artificial-Intelligence-Legislative-Recommendations.pdf) — the deliverable required by the December 2025 executive order. The Framework calls for Congress to preempt state laws that: (1) regulate AI model development; or (2) impose liability on AI developers for unlawful conduct by third parties using their systems. Preserved state authorities include generally applicable consumer-protection and fraud laws, child-safety laws (including AI-generated CSAM prohibitions), state procurement, and zoning. The Framework is non-binding and does not alter existing legal obligations without congressional action.

## Detailed Analysis [HIGH confidence]

### New York RAISE Act: Statutory Structure

The RAISE Act ([NY Senate Bill S8828 / Assembly Bill A9449](https://www.nysenate.gov/legislation/bills/2025/S8828)) was signed by Governor Hochul on December 19, 2025, with chapter amendments signed on March 27, 2026. The chapter amendments align the law more closely with California's [SB 53 (Trusted Frontier AI Accountability Act)](https://www.mofo.com/resources/insights/260403-new-york-amends-the-raise-act-to-align-more-closely). Full compliance obligations are effective January 1, 2027, giving covered developers approximately nine months to build compliance programs. The New York Department of Financial Services (DFS) receives broad rulemaking and enforcement authority under the amended law.

**Scope — Who is Covered:**

The RAISE Act applies to "large frontier developers," defined as entities that:
- Have trained at least one "frontier model" — a foundation model trained using computing power greater than 10²⁶ integer or floating-point operations (FLOPs); and
- Have annual revenues exceeding $500 million.

The law applies to frontier developers that develop, deploy, or operate frontier models "in whole or in part" in New York. As [Wiley Rein analyzed](https://www.wiley.law/alert-New-York-Finalizes-RAISE-Act-for-Frontier-AI-Models-Law-Takes-Effect-January-1-2027), the nexus requirement's breadth means any developer whose models are accessible to New York users may be covered — a significant jurisdictional reach.

**Core Obligations:**

1. **Written Safety and Security Protocols:** Large frontier developers must implement written safety and security protocols, publish a redacted copy, transmit the unredacted version to the New York Attorney General and Division of Homeland Security and Emergency Services (DHSES), and retain unredacted copies for regulatory inspection.

2. **Pre-Deployment Transparency Reports:** Before deploying any new frontier model, developers must publish a transparency report including the developer's contact information, model release date, supported languages and output modalities, intended uses, and usage restrictions.

3. **72-Hour Incident Reporting:** Developers must disclose any "safety incident" involving a frontier model to both the New York Attorney General and DHSES within 72 hours of discovering the incident. The RAISE Act focuses specifically on incidents that could constitute "catastrophic risk" — defined as risk of death or serious injury to more than 50 people or more than $1 billion in damage.

4. **Annual Protocol Reviews:** Developers must conduct annual reviews of their safety and security protocols and make necessary modifications.

5. **DFS Assessment Fees:** The amended law grants DFS authority to assess fees for regulatory oversight of covered developers.

**Enforcement:**

The Attorney General may bring civil actions for failure to submit required reporting or for making false statements. Penalties reach $1 million for a first violation and $3 million for subsequent violations, per [Norton Rose Fulbright's analysis](https://www.nortonrosefulbright.com/en/knowledge/publications/5b5742f4/the-new-york-responsible-ai-safety-and-education-raise-act-what-you-need-to-know). Independent audit requirements may apply through DFS rulemaking.

### DOJ AI Litigation Task Force: Mandate and Likely Targets [MEDIUM confidence]

The DOJ AI Litigation Task Force operates under the January 9, 2026 [internal AG memorandum](https://www.justice.gov/ag/media/1422986/dl?inline=), which states that "United States AI companies must be free to innovate without cumbersome regulation" and that state-by-state regulation creates a compliance patchwork particularly burdensome for startups. The task force coordinates with White House AI czar David Sacks and is directed to challenge state laws on the following legal theories:

- **Dormant Commerce Clause:** State laws imposing extraterritorial regulation of AI model development burden interstate commerce because AI models are trained and deployed nationally, not on a state-by-state basis.
- **Express and Conflict Preemption:** Where federal statutes (FTC Act, Communications Act, etc.) directly regulate the same conduct as state AI laws, federal law may preempt state requirements.
- **First Amendment:** Regulations compelling developers to alter "truthful outputs" of AI models may compel speech in violation of the First Amendment.

As [BakerHostetler analyzed](https://www.bakerlaw.com/insights/navigating-the-emerging-federal-state-ai-showdown-doj-establishes-ai-litigation-task-force/), Colorado's AI Act (SB 24-205) is the most-cited likely target: it requires "reasonable care" from high-risk AI deployers to prevent algorithmic discrimination and imposes developer liability for third-party deployer conduct — precisely the provisions the Framework recommends preempting. California's suite of laws (TFAIA, AB 2013, SB 942) is also frequently cited.

**Is the RAISE Act a Target?**

The picture for New York's RAISE Act is less clear, as [Alston & Bird's April 2026 Quarterly](https://www.alston.com/en/insights/publications/2026/04/ai-quarterly-april-2026) and [Davis Wright Tremaine](https://www.dwt.com/blogs/artificial-intelligence-law-advisor/2025/12/new-york-raise-act-ai-safety-rules-developers) both note. The RAISE Act differs from Colorado's law in key ways:

- It targets only the largest frontier developers ($500M+ revenue, 10²⁶+ FLOP models), not all AI deployers.
- Its requirements are primarily transparency and safety reporting — not restrictions on what outputs models can produce or what conduct third parties may engage in.
- It does not impose liability on developers for third-party misuse of their models.

These distinctions may make the RAISE Act harder to challenge under the Framework's primary preemption theories. However, the RAISE Act's 72-hour incident-reporting requirement and mandatory protocol submission to the AG could still be challenged as: (1) imposing a compliance burden that varies from any future federal disclosure standard; or (2) compelled disclosure that, if the disclosed information is deemed proprietary, could implicate trade secret or First Amendment concerns.

As [Davis Wright Tremaine further analyzed in April 2026](https://www.dwt.com/blogs/artificial-intelligence-law-advisor/2026/04/ny-overhauls-frontier-ai-transparency-law), the chapter amendments specifically re-aligned the RAISE Act with California's SB 53 framework — potentially creating a coordinated state resistance to federal preemption by presenting a bicoastal legislative template that developers in both markets must satisfy regardless of federal guidance.

### FTC Policy Statement and BEAD Conditions [MEDIUM confidence]

The March 11, 2026 FTC deadline for a policy statement on state bias-mitigation preemption has passed. As of the date of this report, no public FTC policy statement specifically addressing preemption of state AI output-alteration requirements has been located. Similarly, the Commerce Department's BEAD Policy Notice identifying "burdensome" state AI laws has not been publicly confirmed as issued. The absence of these enforcement instruments — combined with congressional inaction on comprehensive federal AI legislation — significantly weakens the immediate practical force of the federal preemption campaign. Until Congress acts or a federal court rules on a DOJ challenge, state AI laws remain fully enforceable.

## Impact Assessment [HIGH confidence]

### Who Is Affected by the RAISE Act

The RAISE Act's threshold (frontier models trained at 10²⁶+ FLOPs, $500M+ developer revenue) is designed to target only the largest AI developers — primarily companies like OpenAI, Anthropic, Google DeepMind, Meta, and xAI as of early 2026. Startups, mid-market AI companies, and enterprise deployers that do not train frontier-scale models are not directly covered. However:

- **Deployers of covered models** must understand their vendor's RAISE Act compliance status, since downstream deployment of non-compliant frontier models could create contractual and reputational risk.
- **Any developer with New York operations or users** should assess whether their models meet the 10²⁶ FLOP threshold as compute costs decline and training scales increase over the coming years.

### Compliance Burden and Timeline

With a January 1, 2027 effective date, covered developers have approximately eight months from the chapter amendment signing (March 27, 2026) to:

1. Implement and document written safety and security protocols.
2. Draft transparency reports for all current and planned frontier model releases.
3. Establish 72-hour incident detection and reporting workflows connecting to the NY AG and DHSES.
4. Await and incorporate DFS regulations (which may impose additional audit requirements).
5. Assess the unredacted protocol submission obligation and establish appropriate confidentiality protections.

DFS is expected to issue implementing regulations before the January 1, 2027 effective date. The scope and content of those regulations — particularly regarding independent audit requirements and assessment fees — will materially affect the total compliance burden.

### Federal Preemption Risk to Compliance Investments

Organizations that build RAISE Act compliance programs face an inherent uncertainty: if DOJ challenges the RAISE Act and a federal court issues a preliminary injunction, compliance investments may be stranded. However, given the RAISE Act's structural differences from the laws the Framework most directly targets, the risk of a successful preemption challenge is assessed as lower for the RAISE Act than for Colorado's AI Act. Developers should build compliance programs while monitoring DOJ litigation activity.

### Multi-State AI Compliance Patchwork

The RAISE Act's alignment with California's SB 53 is a deliberate legislative strategy by states to create a coherent bicoastal framework that developers cannot avoid without forgoing two of the three largest US markets. As [Carnegie Endowment for International Peace analyzed](https://carnegieendowment.org/emissary/2026/02/ai-state-law-new-york-raise-act-california-sb53), this convergence strategy may make federal preemption politically and legally harder to accomplish: Congress would need to preempt not just one outlier state but a coordinated multi-state standard with significant democratic legitimacy.

The practical compliance picture for frontier AI developers as of April 2026 includes:
- **New York RAISE Act:** Effective January 1, 2027 — safety protocols, incident reporting, transparency reports.
- **California TFAIA:** Pending potential enforcement — similar frontier model safety obligations.
- **California AB 2013 / SB 942:** Already in effect — training data transparency and content labeling.
- **Colorado AI Act (SB 24-205):** Effective June 30, 2026 — high-risk AI deployer obligations.
- **Texas TRAIGA:** In effect since January 1, 2026 — disclosure and bias audit obligations.

## Action Items

- **Large frontier AI developers (>$500M revenue, >10²⁶ FLOP models):** Begin RAISE Act compliance immediately. Prioritize: (a) safety protocol documentation; (b) incident response workflows with 72-hour notification capability to NY AG and DHSES; (c) transparency report templates for current model lineup; and (d) counsel review of protocol submission confidentiality obligations before transmitting unredacted materials.
- **All AI developers:** Audit model training compute costs and revenue thresholds annually — the RAISE Act's 10²⁶ FLOP threshold will capture more developers as training scales increase.
- **Deployers of third-party frontier models:** Include RAISE Act compliance representations in vendor agreements. Confirm vendor status before deploying in New York-facing applications.
- **Compliance and legal teams:** Track DFS rulemaking on RAISE Act implementation (expected before January 1, 2027) and adjust compliance programs when regulations are finalized.
- **Government affairs and litigation monitoring:** Track DOJ AI Litigation Task Force activity for any challenge to the RAISE Act. If DOJ files suit, assess whether to seek amicus or intervenor status in the litigation.
- **Multi-state compliance programs:** Align RAISE Act safety protocol and incident reporting obligations with California TFAIA requirements to minimize duplicative compliance work — the two frameworks are now substantially aligned after the March 2026 chapter amendment.
- **FTC and Commerce monitoring:** Confirm whether the March 11, 2026 FTC bias-alteration preemption statement and BEAD Policy Notice were issued and assess their implications for any ongoing state disclosure-compliance programs.

## Related Reports

- [Trump Executive Order and National AI Policy Framework: Federal Push to Preempt State AI Laws](../trump-ai-executive-order-state-preemption-2026-04-12.md) — Covers the December 11, 2025 executive order that established the DOJ AI Litigation Task Force and the federal preemption campaign that creates uncertainty for RAISE Act compliance.
- [White House Releases National Policy Framework for AI, Urging Congress to Preempt State AI Laws](../federal-regulation/federal-national-policy-framework-ai-preemption-2026-04-14.md) — Covers the March 20, 2026 legislative recommendations that formally proposed preemption of state laws like the RAISE Act.
- [Colorado AI Act Enforcement Delayed](colorado-ai-act-enforcement-delayed-2026-04-13.md) — The Colorado AI Act (SB 24-205) is the DOJ task force's most-cited likely litigation target and illustrates the enforcement uncertainty facing state AI laws under federal preemption pressure.

## Sources

1. [NY State Senate Bill 2025-S8828 — RAISE Act Chapter Amendment](https://www.nysenate.gov/legislation/bills/2025/S8828) — Official bill text of the chapter amendment signed March 27, 2026.
2. [NY State Assembly Bill 2025-A9449 — RAISE Act Assembly Companion](https://www.nysenate.gov/legislation/bills/2025/A9449) — Assembly bill text for the chapter amendment.
3. [Governor Hochul — Signs Nation-Leading Legislation for Frontier AI](https://www.governor.ny.gov/news/governor-hochul-signs-nation-leading-legislation-require-ai-frameworks-ai-frontier-models) — Official signing announcement and overview of the RAISE Act's requirements.
4. [DOJ — Artificial Intelligence Litigation Task Force Memo (January 9, 2026)](https://www.justice.gov/ag/media/1422986/dl?inline=) — Internal AG memorandum formally establishing the AI Litigation Task Force.
5. [White House — Ensuring a National Policy Framework for Artificial Intelligence (December 11, 2025 EO)](https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/) — Executive order directing DOJ task force, BEAD conditions, FTC statement, and FCC proceeding.
6. [White House — National Policy Framework for AI Legislative Recommendations (March 20, 2026, PDF)](https://www.whitehouse.gov/wp-content/uploads/2026/03/03.20.26-National-Policy-Framework-for-Artificial-Intelligence-Legislative-Recommendations.pdf) — Full text of the Framework's legislative recommendations to Congress.
7. [Alston & Bird — AI Quarterly April 2026](https://www.alston.com/en/insights/publications/2026/04/ai-quarterly-april-2026) — Primary finding source; synthesizes RAISE Act, DOJ task force, and federal preemption as of Q1 2026.
8. [Alston & Bird Privacy Blog — New York Regulates Large AI Models](https://www.alstonprivacy.com/new-york-regulates-large-artificial-intelligence-models/) — Alston's detailed analysis of the original RAISE Act provisions.
9. [Wiley Rein — New York Finalizes RAISE Act; Law Takes Effect January 1, 2027](https://www.wiley.law/alert-New-York-Finalizes-RAISE-Act-for-Frontier-AI-Models-Law-Takes-Effect-January-1-2027) — Post-amendment analysis confirming final scope, thresholds, and effective date.
10. [Norton Rose Fulbright — RAISE Act: What You Need to Know](https://www.nortonrosefulbright.com/en/knowledge/publications/5b5742f4/the-new-york-responsible-ai-safety-and-education-raise-act-what-you-need-to-know) — Detailed compliance obligations and penalty structure.
11. [Morrison Foerster — New York Amends RAISE Act to Align with California](https://www.mofo.com/resources/insights/260403-new-york-amends-the-raise-act-to-align-more-closely) — Analysis of the chapter amendment's convergence with California SB 53.
12. [Davis Wright Tremaine — NY Enacts RAISE Act Amid Federal Preemption Debate](https://www.dwt.com/blogs/artificial-intelligence-law-advisor/2025/12/new-york-raise-act-ai-safety-rules-developers) — Analysis of RAISE Act in context of federal preemption debate.
13. [Davis Wright Tremaine — NY Overhauls Frontier AI Transparency Requirements (April 2026)](https://www.dwt.com/blogs/artificial-intelligence-law-advisor/2026/04/ny-overhauls-frontier-ai-transparency-law) — Post-amendment update on revised requirements.
14. [BakerHostetler — DOJ Establishes AI Litigation Task Force](https://www.bakerlaw.com/insights/navigating-the-emerging-federal-state-ai-showdown-doj-establishes-ai-litigation-task-force/) — Analysis of task force mandate and likely state law targets.
15. [Baker Botts — Inside the DOJ's New AI Litigation Task Force](https://www.bakerbotts.com/thought-leadership/publications/2026/january/inside-the-dojs-new-ai-litigation-task-force) — Detailed breakdown of the January 9, 2026 AG memorandum.
16. [Sidley Austin — Unpacking the December 11, 2025 Executive Order](https://datamatters.sidley.com/2025/12/23/unpacking-the-december-11-2025-executive-order-ensuring-a-national-policy-framework-for-artificial-intelligence/) — Agency directive breakdown including FTC and BEAD timelines.
17. [Carnegie Endowment — New York Aligns with California on Frontier AI Laws](https://carnegieendowment.org/emissary/2026/02/ai-state-law-new-york-raise-act-california-sb53) — Policy analysis of NY-CA convergence strategy as resistance to federal preemption.
18. [Jones Walker — RAISE Act: What Frontier Model Developers Need to Know](https://www.joneswalker.com/en/insights/blogs/ai-law-blog/new-yorks-raise-act-what-frontier-model-developers-need-to-know.html) — Compliance overview including compute thresholds and covered entities.
19. [Fisher Phillips — New York Governor Signs Sweeping AI Safety Law](https://www.fisherphillips.com/en/news-insights/new-york-governor-signs-sweeping-ai-safety-law.html) — Business preparation guide for the RAISE Act.
20. [CBS News — DOJ Creates Task Force to Challenge State AI Regulations](https://www.cbsnews.com/news/doj-creates-task-force-to-challenge-state-ai-regulations/) — News reporting on task force establishment.
