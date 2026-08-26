---
title: "Colorado SB 24-205: A Comprehensive Analysis of the Nation's First State AI Act"
date: 2024-07-23
jurisdiction: "Colorado"
category: "ai-law"
development_type: "guidance"
finding_id: "SCAN-20240723-034"
topic_key: "colorado-1565052a-2024"
topic_type: "guidance"
topic_key_confidence: "low"
first_reported: 2024-07-23
last_updated: 2026-04-15
status_history:
  - "2026-04-15: Initial report created, synthesizing legislative text, Senator Rodriguez interview (Mayer Brown podcast, July 2024), and subsequent implementation developments including June 30, 2026 effective date delay and 2026 ADMT replacement framework proposal."
  - "2026-04-15: Revision r1 — corrected cure period from 10 business days to 60 days (section 6-1-1706); expanded small business exemption to include all three conditions; added Representative Duran to House co-sponsors."
---

# Colorado SB 24-205: A Comprehensive Analysis of the Nation's First State AI Act

**Jurisdiction:** Colorado | **Category:** AI Law | **Date:** July 23, 2024

## Executive Summary [HIGH confidence]

Colorado became the first US state to enact comprehensive artificial intelligence regulation when Governor Jared Polis signed [Senate Bill 24-205](https://leg.colorado.gov/bills/sb24-205) on May 17, 2024. The [Colorado Artificial Intelligence Act (CAIA)](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf) imposes a duty of reasonable care on both developers and deployers of "high-risk" AI systems to protect consumers from algorithmic discrimination in consequential decisions affecting employment, education, healthcare, housing, financial services, insurance, legal services, and essential government services. Senator Robert Rodriguez — the bill's primary sponsor and Colorado Senate Majority Leader — described the legislation as "a framework for accountability, for biases and discrimination," focused on ensuring transparency when AI makes life-altering decisions. Governor Polis signed with reservations, calling for federal preemption and legislative improvements; those concerns, combined with industry opposition, led to a special session delay and a proposed 2026 replacement framework. The law's effective date was subsequently moved from February 1, 2026 to June 30, 2026 by SB 25B-004, and as of March 2026, a governor-backed working group has proposed an "ADMT Framework" to replace the Act entirely.

## Background [HIGH confidence]

### The Federal Vacuum and Colorado's Impetus

By the time Senator Rodriguez introduced SB 24-205 in April 2024, the United States had no comprehensive federal AI law. The Biden administration had issued a sweeping AI Executive Order in October 2023 and the [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/artificial-intelligence) was published in January 2023, but neither imposed binding legal duties on private-sector AI developers or deployers. Congress had conducted hearings but failed to advance comprehensive legislation. State legislatures — particularly those with existing privacy law infrastructure — began filling this gap.

Colorado was positioned to lead. It had enacted the [Colorado Privacy Act (CPA)](https://leg.colorado.gov/bills/sb21-190) in 2021, and legislative staff had experience processing complex data-protection frameworks. Senator Rodriguez, who chairs the Senate Business, Labor, & Technology committee, built on that foundation to craft a focused AI bill targeting algorithmic discrimination specifically — the intersection of AI decision-making and civil rights.

### Legislative History and Connecticut Parallel

Senator Rodriguez filed SB 24-205 on April 10, 2024. The bill largely tracked [Connecticut's SB 2](https://www.cga.ct.gov/2024/TOB/S/PDF/2024SB-00002-R00-SB.PDF), a nearly identical bill that failed passage in Connecticut that same session. The Colorado bill added several Colorado-specific provisions, including authority for the Colorado Attorney General to conduct rulemaking — a feature absent from the Connecticut draft.

The bill passed the Colorado Senate and House and was transmitted to Governor Polis's desk in May 2024. Co-sponsors included Senator Cutter and House Representatives Manny Rutinel, Brianna Titone, and Duran.

### Governor Polis's Conditional Signing

On May 17, 2024, Governor Polis signed SB 24-205 into law but simultaneously published a letter expressing substantive reservations. He criticized the Act for "creat[ing] a complex compliance regime" and expressed "concern[] about [its] impact on an industry that is fueling critical technological advancements." The Governor called on the bill's sponsors to "significantly improve" the approach before the law took effect and urged Congress to enact federal legislation that would preempt the state measure — the only governor to sign a bill while publicly calling for its federal replacement.

## Detailed Analysis [HIGH confidence]

### Scope and Core Architecture

SB 24-205 establishes a [risk-tiered regulatory framework](https://www.naag.org/attorney-general-journal/a-deep-dive-into-colorados-artificial-intelligence-act/) applicable to any "person doing business in Colorado" that develops or deploys AI systems. The law creates two distinct obligation tracks: one for **developers** (those who build or substantially modify AI systems) and one for **deployers** (those who use AI systems to make decisions about consumers). Both are subject to the overarching duty: to "use reasonable care to protect consumers from any known or reasonably foreseeable risks of algorithmic discrimination."

### Key Definitions

**Artificial Intelligence System:** Any machine-based system that, for any explicit or implicit objective, infers from inputs it receives how to generate outputs including content, decisions, predictions, or recommendations that can influence physical or virtual environments.

**High-Risk AI System:** An AI system that, when deployed, makes or is a "substantial factor" in making a **consequential decision**. This is the central scope-triggering definition. A system is high-risk only when deployed in a consequential context — meaning the same model could be high-risk in one use case and not in another. [See the enrolled bill text at section 6-1-1702](https://content.leg.colorado.gov/sites/default/files/documents/2024A/bills/2024a_205_enr.pdf).

**Consequential Decision:** A decision with "material legal or similarly significant effect" on a consumer's access to, or conditions of:
- Education enrollment or opportunities
- Employment or employment opportunities
- Financial or lending services
- Essential government services
- Healthcare services
- Housing
- Insurance
- Legal services

**Substantial Factor:** A factor that assists in making a consequential decision or is capable of altering the outcome of a consequential decision, excluding factors providing only information or data or performing narrow procedural or preparatory tasks. This distinction is practically significant: a chatbot that gathers information without influencing the decision is arguably not a "substantial factor."

**Algorithmic Discrimination:** Any condition in which the use of an AI system results in an unlawful differential treatment or impact that disfavors an individual or group of individuals on the basis of their actual or perceived race, color, ethnicity, sex, religion, age, national origin, limited English proficiency, disability, veteran status, genetic information, reproductive health, or similar protected characteristic.

**Developer:** Any person doing business in Colorado that develops or intentionally and substantially modifies a high-risk AI system that is offered, sold, leased, given, or otherwise made available to deployers.

**Deployer:** Any person doing business in Colorado that deploys a high-risk AI system to make, or be a substantial factor in making, consequential decisions about consumers.

### Developer Obligations [HIGH confidence]

Under [Section 6-1-1703 of the Colorado Revised Statutes](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf) (as enacted by SB 24-205), developers must:

1. **Maintain documentation:** Create and maintain documentation sufficient to allow deployers to complete impact assessments.
2. **Disclose to deployers:** Make available to each deployer a statement disclosing (a) the intended uses of the high-risk system; (b) the types of data processed; (c) data governance practices; (d) known limitations; (e) performance metrics; and (f) measures taken to mitigate known risks of algorithmic discrimination.
3. **Publish a public statement:** Post a publicly available summary describing the types of high-risk systems the developer has developed or intentionally and substantially modified.
4. **Report discrimination:** Within 90 days of discovering — or receiving a credible report — that a high-risk system has caused or is reasonably likely to have caused algorithmic discrimination, disclose this to (a) the Colorado Attorney General and (b) all known deployers of the system.
5. **Notify of modifications:** Inform known deployers of any subsequent modifications that materially change a prior disclosure.

Developers are entitled to a **rebuttable presumption** of having satisfied the reasonable care standard if they comply with the documentation and disclosure provisions and have adopted a conforming AI risk management framework (see Safe Harbors below).

### Deployer Obligations [HIGH confidence]

Under [Section 6-1-1704](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf), deployers must:

1. **Implement a risk management policy:** Adopt and implement a written risk management policy and program for the high-risk system, covering identification and mitigation of discrimination risks. The policy may incorporate NIST AI RMF, ISO/IEC 42001, or another recognized framework.
2. **Complete impact assessments:** Conduct and document an impact assessment (a) before deploying each high-risk system, (b) within 90 days of any significant modification, and (c) at least annually. Impact assessments must cover: (i) the intended purpose, (ii) a summary of training data, (iii) known performance limitations, (iv) discrimination risks by demographic group, and (v) mitigation measures.
3. **Notify consumers:** Before a high-risk AI system makes or substantially contributes to a consequential decision about a consumer, notify that consumer of (a) the fact that a high-risk AI system is being used; (b) a description of the system and its purpose; and (c) the type of data used and data governance practices.
4. **Provide adverse action notice:** If a high-risk system makes — or is a substantial factor in making — an adverse consequential decision, the deployer must (a) notify the consumer; (b) provide the principal reasons for the decision; (c) disclose what data was processed; and (d) describe what role AI played in the outcome.
5. **Provide a right to correct:** Give consumers the opportunity to correct any inaccurate personal data used in the decision.
6. **Provide a right to appeal:** Give consumers the opportunity to appeal the adverse decision via human review, if technically feasible.
7. **Annual review:** Review deployment at least annually to ensure no algorithmic discrimination has resulted.
8. **Report discrimination:** Within 90 days of discovering that a deployed high-risk system has caused or is likely to have caused algorithmic discrimination, notify the Colorado Attorney General and the relevant developer.

Deployers also receive a **rebuttable presumption** of reasonable care if they comply with the above requirements.

### Consumer Rights [HIGH confidence]

The CAIA grants consumers targeted procedural rights when they are subject to high-risk AI decision-making. Per [Sections 6-1-1703 and 6-1-1704](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf), consumers have the right to:

- **Pre-decision disclosure:** Know that a high-risk AI system is being used before or at the time of a consequential decision.
- **Adverse action explanation:** Receive a plain-English explanation of the principal reasons for an adverse decision and how AI contributed.
- **Data correction:** Correct inaccurate personal data that was processed in making the decision.
- **Human review appeal:** Appeal an adverse consequential decision for human review, if technically feasible.
- **Interaction disclosure:** Be told when interacting with any AI system (not just high-risk systems) — a broader disclosure requirement covering all consumer-facing AI deployments.

The last right — disclosure of AI interaction — applies to any business that deploys an AI system intended to interact with consumers, regardless of whether the system is "high-risk." This means customer service chatbots, virtual assistants, and similar tools all require consumer disclosure under the CAIA.

Additionally, consumers who receive adverse decisions are also entitled to information about opt-out rights under the [Colorado Privacy Act (CPA)](https://leg.colorado.gov/bills/sb21-190).

### Safe Harbors and Exemptions [HIGH confidence]

**Risk Framework Safe Harbor:** Developers and deployers that comply with a recognized AI risk management framework — specifically the [NIST AI RMF](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf), ISO/IEC 42001, or another framework recognized by the Colorado Attorney General — and take specified measures to discover and correct violations have an **affirmative defense** to enforcement actions under the CAIA.

**Small Business Exemption:** Organizations with fewer than 50 full-time employees may qualify for reduced obligations, but only if all three of the following conditions are met: (1) the deployer does not train the AI system using its own proprietary data; (2) the deployer limits use of the system to uses previously disclosed by the developer; and (3) the deployer provides consumers access to the impact assessment completed by the developer. This carve-out is narrower than it appears: condition (1) excludes many smaller companies that fine-tune vendor models on internal data, while conditions (2) and (3) require active compliance steps — not mere passivity — even for qualifying small businesses.

**Federally Regulated AI Systems:** AI systems approved or certified by federal agencies — including the FDA, FAA, and Federal Housing Finance Agency (FHFA) — are fully exempt from the CAIA. Systems complying with equivalent or stricter federal standards (such as those from the HHS Office of the National Coordinator for Health Information Technology) are similarly exempt.

**Financial Institution Exemption:** Banks, out-of-state banks, credit unions chartered by Colorado or federal authorities, and their affiliates are exempt from the CAIA's requirements.

**Insurer Exemption:** Insurers and fraternal benefit societies subject to Colorado insurance regulation are exempt.

**Open-Source Model Carve-Out:** Developers of open-source AI components that are not themselves deploying the AI are not treated as deployers under the Act.

### Enforcement Mechanism [HIGH confidence]

The Colorado Attorney General has **exclusive authority** to enforce SB 24-205. There is **no private right of action** under the statute. Violations are treated as unfair trade practices under the [Colorado Consumer Protection Act (CCPA)](https://coag.gov/consumer-protection/), with maximum civil penalties of **$20,000 per violation**, with each consumer or transaction counted separately.

The Attorney General is also granted **rulemaking authority** to implement the CAIA — a provision included at the request of Senator Rodriguez and not present in the Connecticut parallel bill. The [Colorado Attorney General's office has initiated AI-related rulemaking](https://coag.gov/ai/) under the Anti-Discrimination in AI (ADAI) rulemaking proceeding.

A **60-day cure period** applies for violations where cure is possible under [Section 6-1-1706](https://content.leg.colorado.gov/sites/default/files/documents/2024A/bills/2024a_205_enr.pdf), but the cure provision does not apply to violations that have caused actual harm, violations of a prior notice, or patterns of violations.

## Senator Rodriguez's Legislative Intent [MEDIUM confidence]

In the [Mayer Brown AI Legislative Update podcast published July 2024](https://www.mayerbrown.com/en/insights/podcasts/2024/07/a-conversation-with-senator-rodriguez-about-colorados-landmark-ai-law), Senator Rodriguez described SB 24-205 as "a framework for accountability, for biases and discrimination and just making sure that people know when they're interacting with" high-risk AI systems. He explained that Colorado's work on the Consumer Privacy Act provided foundational infrastructure and legislative staff familiarity with complex data-protection concepts that made the AI bill tractable.

In a [January 2026 episode of the Regulatory Oversight podcast](https://www.regulatoryoversight.com/2026/01/ai-algorithms-and-accountability-unpacking-the-colorado-ai-act-with-senator-rodriguez/) with Troutman Pepper Locke privacy attorney David Stauss, Senator Rodriguez elaborated on the intent behind the law's "substantial factor" standard and impact assessment requirements, emphasizing that the goal was to impose meaningful accountability for AI-driven outcomes in high-stakes domains without prohibiting AI development or deployment.

Key legislative goals as stated by Senator Rodriguez:
- Focus on **algorithmic discrimination** rather than prohibiting specific AI technologies outright
- Require **transparency and documentation** as the primary compliance mechanism
- Empower consumers to understand and contest AI-driven decisions affecting their lives
- Create a framework flexible enough to accommodate future technological development through Attorney General rulemaking
- Build on existing Colorado consumer protection infrastructure rather than creating a separate regulatory body

## Industry Opposition and Lobbying [MEDIUM confidence]

The week before Governor Polis signed SB 24-205, technology industry groups launched a concerted veto campaign. The [US Chamber of Commerce](https://www.uschamber.com/) warned that the law may hamper small business AI adoption and argued a gap-filling approach targeting specific discrimination would be preferable to the CAIA's broad framework. The [Chamber of Progress](https://progress.org/) and [Consumer Technology Association (CTA)](https://www.cta.tech/) both urged Governor Polis to veto the bill and instead strengthen existing anti-discrimination laws.

Governor Polis's signing statement incorporated several of these criticisms — an unusual posture for a governor signing major legislation — and noted that the bill's compliance regime could burden smaller businesses disproportionately. His letter encouraged the legislature to work with developers, deployers, and consumer advocates to produce a revised approach.

These pressures ultimately produced results: following a failed August 2025 special session that was intended to replace the CAIA wholesale, the legislature used SB 25B-004 to simply delay the effective date, buying time for broader legislative revision.

## Comparison: Colorado vs. EU AI Act [MEDIUM confidence]

Colorado's CAIA and the [EU Artificial Intelligence Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) (which received final Council approval in May 2024, concurrent with SB 24-205's enactment) share a risk-based architecture and comparable transparency obligations. Both:

- Define risk tiers based on the use context of AI systems (high-risk in specific application domains)
- Require documentation, conformity assessments, and disclosure
- Mandate human oversight mechanisms for high-risk applications
- Focus on algorithmic discrimination as a primary harm to prevent

However, significant differences exist:

| Feature | Colorado CAIA | EU AI Act |
|---|---|---|
| Geographic scope | Colorado consumers | EU market (global extraterritorial reach) |
| Prohibited AI uses | None | Multiple (social scoring, real-time biometric surveillance, etc.) |
| Regulator | State Attorney General (rulemaking + enforcement) | AI Office + national competent authorities |
| Enforcement | Consumer Protection Act, $20,000/violation | Market surveillance, fines up to €30M or 6% of global turnover |
| Private right of action | No | Yes (for certain violations) |
| Developer vs. deployer | Dual-track obligation | Duty chain across providers, deployers, importers, distributors |
| Conformity assessment | Rebuttable safe harbor (NIST AI RMF, ISO 42001) | Mandatory third-party certification for some high-risk systems |
| Open-source | Carve-out for non-deploying developers | Partial carve-outs with conditions |

Baker McKenzie observed that the Colorado Act resembles a "Brussels to Boulder" transatlantic convergence — not because Colorado copied the EU Act (the drafting processes were concurrent), but because both frameworks were responding to similar perceived harms using a risk-tiered, transparency-focused approach. Key differences are that the EU Act goes considerably further in establishing prohibited uses and mandatory third-party conformity assessments for certain high-risk categories, while Colorado relies more heavily on private-sector self-governance via recognized risk frameworks.

## Implementation Timeline and Status [HIGH confidence]

| Date | Event |
|---|---|
| April 10, 2024 | SB 24-205 introduced by Senator Rodriguez |
| May 17, 2024 | Governor Polis signs SB 24-205 with reservations |
| July 2024 | Mayer Brown podcast with Senator Rodriguez on legislative intent |
| August 2025 | Colorado special session; SB 25B-004 delays effective date to June 30, 2026 |
| March 17, 2026 | Governor's AI Policy Working Group proposes ADMT Framework to replace CAIA |
| June 30, 2026 | Current CAIA effective date (subject to further legislative action) |
| January 1, 2027 | Proposed ADMT replacement framework effective date (if enacted) |

### The August 2025 Special Session and Effective Date Delay

Governor Polis called a special legislative session in August 2025 in part to address SB 24-205. Senator Rodriguez introduced [SB 25B-004](https://leg.colorado.gov/bills/sb25b-004) (Increase Transparency for Algorithmic Systems), which was initially designed to repeal and replace the CAIA with a broader "algorithmic decision systems" regulatory framework. The replacement deal collapsed, and SB 25B-004 was narrowed to solely delay the CAIA's effective date from February 1, 2026, to **June 30, 2026**. Governor Polis signed SB 25B-004 on August 28, 2025.

### The 2026 ADMT Framework Proposal

On March 17, 2026, the Colorado AI Policy Work Group — established by Governor Polis and representing small businesses, hospitals, schools, consumer groups, venture capitalists, and technology advocates — reached consensus on a proposed bill to replace SB 24-205. The proposal, known as the "KILO draft," shifts from the CAIA's prescriptive governance requirements (impact assessments, risk management policies, annual reviews) to a disclosure-and-transparency model focused on:

- Consumer notice in plain language
- Human review rights
- Recordkeeping requirements
- Elimination of proactive bias audit mandates
- Removal of AG discrimination reporting duties

If enacted, the Automated Decision-Making Technology (ADMT) Framework would take effect January 1, 2027, and SB 24-205 would be repealed. As of April 2026, the bill had not yet been formally introduced in the Colorado legislature.

## Practical Compliance Implications [MEDIUM confidence]

Until the CAIA is repealed or superseded, the following compliance posture is recommended for organizations doing business in Colorado:

**For Developers:**
- Inventory all AI systems that could qualify as "high-risk" when deployed by downstream customers
- Prepare and maintain technical documentation sufficient for deployers to complete impact assessments
- Establish a disclosure template covering required data elements (intended use, data types, performance metrics, known limitations)
- Implement a 90-day incident notification workflow for discovered algorithmic discrimination
- Assess whether existing systems align with NIST AI RMF or ISO 42001 to take advantage of the safe harbor

**For Deployers:**
- Map all AI systems against the CAIA's consequential decision categories; identify which systems are "high-risk" as deployed
- Build or adapt impact assessment procedures — these must be completed before deployment and annually thereafter
- Update consumer-facing notices to include AI disclosure (required for all consumer-facing AI, not just high-risk)
- Design adverse action notification workflows with plain-language AI explanation capability
- Implement data correction and human review appeal mechanisms in decision-making workflows
- Document the risk management policy in writing and review it annually

**For All Organizations:**
- Monitor the Colorado legislature for ADMT Framework introduction and potential SB 24-205 repeal
- Track Colorado AG rulemaking at [coag.gov/ai](https://coag.gov/ai/) — the AG's guidance will materially define compliance scope
- Maintain contingency plans for a June 30, 2026 enforcement date if the replacement bill stalls

## Action Items

- **Immediate:** Identify all AI systems deployed in Colorado consequential decision contexts; classify each as "high-risk" or not under CAIA definitions.
- **Before June 30, 2026 (current effective date):** Complete impact assessments for all high-risk AI systems; implement consumer notification workflows; document risk management policies.
- **Ongoing:** Monitor Colorado AG rulemaking proceedings at coag.gov/ai for implementing guidance that will define key compliance scope questions.
- **Legislative watch:** Track the ADMT Framework bill introduction in the 2026 Colorado regular session — if enacted, compliance obligations will change materially before the current June 30, 2026 effective date.
- **Federal preemption monitor:** Track federal AI preemption proposals; Governor Polis has explicitly called for federal law to supersede SB 24-205.

## Related Reports

- [reports/ai-law/state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md](reports/ai-law/state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md) — Comprehensive primary report on SB 24-205's passage, statutory analysis, and immediate industry implications.
- [reports/ai-law/state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md](reports/ai-law/state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md) — Covers the August 2025 special session and SB 25B-004 effective date delay to June 30, 2026.
- [reports/ai-law/state-legislation/colorado-polis-ai-signing-squire-patton-boggs-2024-05-23.md](reports/ai-law/state-legislation/colorado-polis-ai-signing-squire-patton-boggs-2024-05-23.md) — Analysis of Governor Polis's signing letter and its implications for legislative revision.
- [reports/ai-law/employment-ai/colorado-sb205-employer-ai-employment-2024-05-20.md](reports/ai-law/employment-ai/colorado-sb205-employer-ai-employment-2024-05-20.md) — Deep dive into CAIA's implications for employers using AI in hiring, performance evaluation, and workforce management.
- [reports/ai-law/health/colorado-sb205-healthcare-ai-implications-2024-05-28.md](reports/ai-law/health/colorado-sb205-healthcare-ai-implications-2024-05-28.md) — Analysis of CAIA's implications for healthcare AI systems, including FDA-regulated device exemptions.
- [reports/ai-law/frameworks-guidance/nist-ai-rmf-critical-infrastructure-profile-2026-04-13.md](reports/ai-law/frameworks-guidance/nist-ai-rmf-critical-infrastructure-profile-2026-04-13.md) — The NIST AI RMF profile that forms the basis for CAIA's primary safe harbor defense.
- [reports/ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md](reports/ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md) — Federal preemption context directly relevant to Governor Polis's call for a federal alternative to SB 24-205.

## Sources

1. [SB24-205 Consumer Protections for Artificial Intelligence — Colorado General Assembly](https://leg.colorado.gov/bills/sb24-205) — Official bill page with sponsors, status, and enrolled text links.
2. [Colorado SB 24-205 Enrolled Bill Text (PDF)](https://content.leg.colorado.gov/sites/default/files/documents/2024A/bills/2024a_205_enr.pdf) — Official enrolled text as passed by the legislature; authoritative for statutory language including section 6-1-1706 (60-day cure period).
3. [Colorado SB 24-205 Signed Act (PDF)](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf) — Governor-signed version; official legal text.
4. [A Conversation With Senator Rodriguez About Colorado's Landmark AI Law — Mayer Brown Podcast](https://www.mayerbrown.com/en/insights/podcasts/2024/07/a-conversation-with-senator-rodriguez-about-colorados-landmark-ai-law) — Primary source for Senator Rodriguez's legislative intent; published July 2024.
5. [A Conversation With Senator Rodriguez — Lexology](https://www.lexology.com/library/detail.aspx?g=a4a7c3b2-6656-44af-a88f-2030a39363cc) — Lexology republication of the Mayer Brown podcast entry; original source for this finding.
6. [AI, Algorithms, and Accountability: Unpacking the Colorado AI Act with Senator Rodriguez — Troutman Pepper Locke / Regulatory Oversight](https://www.regulatoryoversight.com/2026/01/ai-algorithms-and-accountability-unpacking-the-colorado-ai-act-with-senator-rodriguez/) — January 2026 podcast episode with Senator Rodriguez and David Stauss on implementation developments.
7. [A Deep Dive into Colorado's Artificial Intelligence Act — National Association of Attorneys General](https://www.naag.org/attorney-general-journal/a-deep-dive-into-colorados-artificial-intelligence-act/) — Detailed statutory analysis from NAAG; HIGH confidence source.
8. [Colorado's Landmark AI Act: What Companies Need to Know — Skadden](https://www.skadden.com/insights/publications/2024/06/colorados-landmark-ai-act) — Major law firm analysis of CAIA's key provisions and compliance implications.
9. [Colorado Passes First-in-Nation Artificial Intelligence Act — Wilson Sonsini](https://www.wsgr.com/en/insights/colorado-passes-first-in-nation-artificial-intelligence-act.html) — Law firm analysis emphasizing developer/deployer framework and comparison to EU AI Act.
10. [Colorado Governor Signs Broad AI Bill Regulating Employment Decisions — Seyfarth Shaw](https://www.seyfarth.com/news-insights/colorado-governor-signs-broad-ai-bill-regulating-employment-decisions.html) — Analysis of Governor Polis's signing and employment law implications.
11. [Colorado's Landmark AI Law Coming Online: What Developers and Deployers Should Know — Brownstein Hyatt](https://www.bhfs.com/insight/colorados-landmark-ai-law-coming-online-what-developers-and-deployers-should-know/) — Comprehensive compliance guidance from Colorado-based law firm.
12. [FAQ on Colorado's Consumer Artificial Intelligence Act (SB 24-205) — Center for Democracy and Technology](https://cdt.org/insights/faq-on-colorados-consumer-artificial-intelligence-act-sb-24-205/) — Consumer advocacy perspective on consumer rights provisions; also addresses CDT's views on what should be strengthened.
13. [Colorado's Artificial Intelligence Act is a Step in the Right Direction. It Must be Strengthened, Not Weakened. — Center for Democracy and Technology](https://cdt.org/insights/colorados-artificial-intelligence-act-is-a-step-in-the-right-direction-it-must-be-strengthened-not-weakened/) — CDT's position on industry opposition and calls for reform.
14. [North America: From Brussels to Boulder — Baker McKenzie InsightPlus](https://insightplus.bakermckenzie.com/bm/data-technology/north-america-from-brussels-to-boulder-colorado-enacts-comprehensive-ai-law-on-the-heels-of-eus-ai-act-with-significant-obligations-for-business-and-employers) — EU AI Act vs. Colorado CAIA comparative analysis.
15. [Colorado's Artificial Intelligence Law Could Be on the Chopping Block — Littler Mendelson](https://www.littler.com/news-analysis/asap/colorados-artificial-intelligence-law-could-be-chopping-block) — Analysis of industry opposition and legislative risk to SB 24-205.
16. [SB25B-004 Increase Transparency for Algorithmic Systems — Colorado General Assembly](https://leg.colorado.gov/bills/sb25b-004) — Official page for the August 2025 special session bill that delayed CAIA's effective date.
17. [Colorado Postpones Implementation of Colorado AI Act, SB 24-205 — Akin Gump](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/colorado-postpones-implementation-of-colorado-ai-act-sb-24-205) — Analysis of SB 25B-004 and implications of the delay to June 30, 2026.
18. [Artificial Intelligence Working Group Agrees on Framework to Replace Colorado Law — Colorado Politics](https://www.coloradopolitics.com/2026/03/17/artificial-intelligence-working-group-agrees-on-framework-to-replace-colorado-law/) — March 17, 2026 reporting on the ADMT Framework consensus.
19. [The Colorado AI Policy Work Group Proposes an Updated Framework to Replace the Colorado AI Act — Mayer Brown](https://www.mayerbrown.com/en/insights/publications/2026/03/the-colorado-ai-policy-work-group-proposes-an-updated-framework-to-replace-the-colorado-ai-act) — Mayer Brown analysis of the KILO/ADMT replacement framework.
20. [Colorado Anti-Discrimination in AI Law (ADAI) Rulemaking — Colorado Attorney General](https://coag.gov/ai/) — Official AG rulemaking page for CAIA implementation guidance.
21. [Colorado AI Act — Wikipedia](https://en.wikipedia.org/wiki/Colorado_AI_Act) — Background context and legislative history.
22. [Colorado Moves to Overhaul Its AI Act: Understanding the ADMT Framework — DCI Consulting](https://www.jdsupra.com/legalnews/colorado-moves-to-overhaul-its-ai-act-7446094/) — Analysis of the proposed ADMT replacement framework's key changes from SB 24-205.
