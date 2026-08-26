---
title: "Colorado Enacts Groundbreaking AI Consumer Protection Legislation (SB 24-205)"
date: 2024-06-03
jurisdiction: "Colorado"
category: "ai-law"
development_type: "legislation"
finding_id: "SCAN-20240603-003"
topic_key: "colorado-042c573c-2024"
topic_type: "state_bill"
first_reported: 2024-06-03
last_updated: 2024-06-03
status_history: []
cluster: "Colorado AI Act (SB 24-205): Enforcement and Amendments"
cluster_slug: "colorado-ai-act-sb-24-205-enforcement"
---

# Colorado Enacts Groundbreaking AI Consumer Protection Legislation (SB 24-205)

**Jurisdiction:** Colorado | **Category:** AI Law | **Date:** June 3, 2024

> **Note:** This report is based on Akin Gump Strauss Hauer & Feld LLP's blog post "Colorado Enacts Groundbreaking AI Consumer Protection Legislation" (AG Data Dive, June 2024), which provides a practical compliance-oriented analysis of Colorado SB 24-205 aimed at business practitioners. The knowledge base also contains a comprehensive primary enactment analysis at [reports/ai-law/state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md](reports/ai-law/state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md) and a focused developer/deployer framework memo at [reports/ai-law/state-legislation/colorado-sb205-akin-gump-developer-deployer-2024-05-30.md](reports/ai-law/state-legislation/colorado-sb205-akin-gump-developer-deployer-2024-05-30.md). Readers seeking the deepest doctrinal analysis should consult those reports alongside this one.

## Executive Summary [HIGH confidence]

Colorado Governor Jared Polis signed [Senate Bill 24-205](https://leg.colorado.gov/bills/sb24-205) — formally titled the Consumer Protections for Artificial Intelligence Act — on May 17, 2024, making Colorado the first state to enact a comprehensive risk-based AI regulatory framework in the United States. The law imposes a duty of reasonable care on both **developers** and **deployers** of high-risk AI systems to protect Colorado consumers from algorithmic discrimination in consequential decisions affecting employment, education, health care, housing, financial services, insurance, legal services, and essential government services. Enforcement rests exclusively with the Colorado Attorney General, with civil penalties up to $20,000 per violation under the Colorado Consumer Protection Act. The original February 1, 2026 effective date was subsequently delayed to June 30, 2026 by SB 25B-004 signed August 28, 2025; as of April 2026, Governor Polis's AI Policy Working Group has unanimously endorsed a proposed ADMT replacement framework that — if enacted — would supersede SB 24-205 with a January 1, 2027 effective date.

## Background [HIGH confidence]

### Federal Vacuum and State Action

At the time of SB 24-205's enactment, no comprehensive federal AI legislation existed. Federal regulatory activity had produced voluntary guidance: the [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/artificial-intelligence/ai-risk-management-framework) in January 2023, and the Biden administration's [Executive Order on Safe, Secure, and Trustworthy Artificial Intelligence](https://www.federalregister.gov/documents/2023/11/01/2023-24283/safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence) in October 2023 — neither imposing binding private-sector mandates. This vacuum left states to act.

Colorado's approach followed a narrowly-scoped [Utah AI Policy Act (SB 149)](https://le.utah.gov/~2024/bills/static/SB0149.html) enacted in March 2024 (AI disclosure requirements), but was far more comprehensive in scope, modeling its risk-based tier structure on the then-recently passed [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689), which the European Parliament approved in March 2024.

### Legislative History

Senator Robert Rodriguez introduced SB 24-205 on April 10, 2024. Additional Senate sponsors included Senators Cutter, Michaelson Jenet, Priola, and Winter F.; House sponsors were Representatives Titone, Rutinel, and Duran. The Senate passed the bill on May 3, 2024; the House on May 8, 2024. Governor Polis signed on May 17, 2024, with a formal letter urging the legislature to "significantly improve" the law before the original February 1, 2026 effective date and calling on Congress to enact preemptive federal AI legislation.

The [official enrolled and signed statute text](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf) is available from the Colorado General Assembly. The bill's full history and all versions are on the [Colorado General Assembly SB 24-205 bill page](https://leg.colorado.gov/bills/sb24-205).

### Context: Why "Groundbreaking"

[Akin Gump characterizes the law](https://www.akingump.com/en/insights/blogs/ag-data-dive/colorado-enacts-groundbreaking-ai-consumer-protection-legislation) as "groundbreaking" for three reasons: (1) it is the first US state comprehensive AI law imposing affirmative duties on both the development and deployment sides of the AI supply chain; (2) it adopts a consequential-decision scope that captures the highest-risk practical applications of AI without attempting to regulate AI broadly; and (3) it creates a shared liability framework between AI vendors (developers) and enterprise customers (deployers) that has no prior state-law precedent.

## Detailed Analysis [HIGH confidence]

### Scope: What Is a "High-Risk AI System"?

The law applies to **high-risk artificial intelligence systems** — defined as any AI system that, when deployed, makes or is a "substantial factor" in making a **consequential decision**. A consequential decision is one with a material legal or similarly significant effect on a consumer's access to, cost of, or terms of:

- Employment or employment opportunities
- Education enrollment or educational opportunities
- Financial or lending services
- Essential government services
- Health care services
- Housing
- Insurance
- Legal services

This outcome-based definition means the law's scope is determined by what decisions the AI influences, not by the technical characteristics of the AI system itself — a deliberate structural choice that distinguishes Colorado's approach from the EU AI Act's category-based classification.

### Key Definition: "Algorithmic Discrimination"

The law defines algorithmic discrimination as any condition in which an AI system results in unlawful differential treatment or impact that disfavors a consumer based on: race, color, ethnicity, sex, religion, age, national origin, limited English proficiency, disability, veteran status, genetic information, or reproductive health. The duty of reasonable care is specifically directed at preventing this outcome.

### Developer Obligations [HIGH confidence]

Under [SB 24-205](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf), a **developer** is any person doing business in Colorado who develops, or intentionally and substantially modifies, a high-risk AI system that is made available commercially. Core developer obligations include:

1. **Deployer documentation:** Provide deployers with a statement disclosing the intended uses, known harmful uses, training data bias evaluation methodology, and risk mitigation measures for each high-risk AI system.
2. **Technical artifacts:** Make available (to the extent feasible) model cards, dataset cards, or other impact assessment materials that enable deployers to complete their own statutory impact assessments.
3. **Public disclosure:** Maintain a publicly accessible website summarizing the types of high-risk AI systems developed and how the developer manages foreseeable algorithmic discrimination risks.
4. **Incident notification:** Within 90 days of discovering, or receiving a credible report from a deployer, that a system has caused or is reasonably likely to cause algorithmic discrimination, notify both the Colorado AG and all known Colorado deployers.

A developer obtains a **rebuttable presumption of reasonable care** if it makes available to deployers the required statement disclosing system information and the documentation needed for impact assessments.

The "intentionally and substantially modifies" language creates a notable compliance risk for enterprises that fine-tune, adapt, or retrain foundation models: such activity may constitute development — not merely deployment — triggering the full developer obligation set.

### Deployer Obligations [HIGH confidence]

A **deployer** is any person doing business in Colorado who uses a high-risk AI system in a product or service to make, or be a substantial factor in making, consequential decisions about Colorado consumers. "Deploy" equals "use" — meaning any enterprise using a covered AI system in the enumerated decision categories is a deployer regardless of whether it built or sells the system.

Core deployer obligations include:

1. **Risk management program:** Implement a written risk management policy and program for each high-risk AI system, incorporating the [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence/ai-risk-management-framework), [ISO/IEC 42001](https://www.iso.org/standard/81230.html), or a substantially equivalent framework designated by the Colorado AG.
2. **Impact assessments:** Conduct documented impact assessments (a) prior to deployment, (b) annually thereafter, and (c) within 90 days of any intentional and substantial modification. Assessments must cover data processed, performance metrics across demographic groups, known limitations, and transparency measures.
3. **Annual review:** Review each deployed high-risk AI system annually to confirm it is not causing algorithmic discrimination.
4. **Consumer notice:** When a high-risk AI system makes or substantially influences a consequential decision affecting a specific consumer, notify the consumer in plain language, in the consumer's language and accessible formats, explaining the decision and how inaccurate data may be corrected.
5. **Human review and appeal:** Provide consumers a meaningful opportunity to appeal adverse consequential decisions and, where technically feasible, to obtain human review of the AI-influenced outcome.
6. **General AI disclosure:** Ensure consumers interacting with any AI system (not just high-risk systems) are informed they are interacting with an AI — a broader, standalone disclosure requirement.
7. **Website summary:** Publish a summary of all high-risk AI systems the deployer has deployed.

Deployers that satisfy all of these obligations obtain a **rebuttable presumption of reasonable care** — the central safe harbor. A separate **voluntary safe harbor** protects entities that discover and remediate violations through their own internal review before any AG complaint is filed.

### Consumer Rights [HIGH confidence]

Colorado consumers subject to consequential decisions influenced by a high-risk AI system have three affirmative rights:

- **Notice:** The right to be informed, in advance or contemporaneously, that an AI system is making or substantially influencing a consequential decision affecting them, along with a plain-language description of the decision and the role of AI.
- **Data correction:** The right to correct inaccurate personal data processed by the AI system in reaching a consequential decision.
- **Appeal with human review:** The right to appeal an adverse consequential decision and — where technically feasible — to have a human review the AI-influenced outcome.

### Exemptions [HIGH confidence]

The statute contains several targeted exemptions from the high-risk AI requirements:

- **Federally regulated AI:** Systems approved or cleared by FDA, FAA, or FHFA; systems deployed under DoD, DoC, or NASA contracts (unless used in employment or housing decisions).
- **Financial institutions:** Banks, credit unions, and affiliates subject to AI examination by state or federal prudential regulators under published guidance meeting statutory criteria.
- **Insurers:** Insurance companies and AI developers serving insurers under Colorado's algorithmic-insurance statutes.
- **HIPAA-covered entities:** Health care AI systems compliant with qualifying HHS/ONC guidance.
- **Small-business deployers:** Deployers with fewer than 50 full-time employees who (a) do not train the system using their own data, (b) restrict use to disclosed developer uses, and (c) provide consumers access to the developer's impact assessment materials.
- **Self-testing/diversity programs:** AI systems used solely for self-testing or to increase workforce diversity and address historical discrimination are excluded from the algorithmic discrimination definition.

### Enforcement [HIGH confidence]

The Colorado Attorney General has **exclusive** enforcement authority — there is no private right of action. The [Colorado AG's AI enforcement page](https://coag.gov/ai/) serves as the official hub for rulemaking and guidance. Violations constitute unfair or deceptive trade practices under the [Colorado Consumer Protection Act](https://coag.gov/resources/consumer-protection/), subjecting violators to civil penalties of up to **$20,000 per violation**. Each affected consumer may constitute a separate violation, creating potential for substantial aggregate penalties in systemic algorithmic discrimination scenarios.

Before filing suit, the AG must provide written notice and allow a 60-day cure period for identified deficiencies.

## Comparison with EU AI Act [MEDIUM confidence]

Colorado's law shares a risk-based architecture with the [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) but reflects distinctly American regulatory philosophy:

| Feature | Colorado SB 24-205 | EU AI Act |
|---|---|---|
| High-risk definition | Consequential-decision outcomes (8 enumerated categories) | Tiered by use case + technical criteria; prohibited uses category |
| Compliance standard | Reasonable care + rebuttable presumption via recognized framework | Prescriptive conformity assessment + technical documentation |
| Prohibited AI uses | None | Yes (unacceptable-risk category, e.g., social scoring, real-time remote biometric ID) |
| Enforcement | State AG exclusive; no private right of action | National competent authorities + EU AI Office; variable state-level penalties |
| Pre-market authorization | None | Required for highest-risk systems |
| Small-business relief | Conditional exemption for deployers < 50 FTE | Proportionality principle; no blanket exemption |
| Effective date | June 30, 2026 (delayed from Feb 1, 2026) | Phased Aug 2024 – Aug 2026 |

Colorado adopts a negligence-standard framework rooted in outcomes ("did this AI cause discrimination?") rather than the EU Act's product-safety model focused on technical characteristics and pre-deployment conformity assessments.

### Comparison with Other State AI Laws (2024)

As of mid-2024, Colorado's law was the most comprehensive state AI statute in the United States. Comparable laws enacted in 2024 included:

- **Utah AI Policy Act (SB 149):** Focused on AI disclosure (operators must disclose AI use on request); no developer/deployer obligation framework.
- **Tennessee ELVIS Act:** Addresses AI voice and likeness cloning; narrow entertainment-sector focus.
- **Connecticut SB 2:** Passed the Senate in 2024 but stalled in the House; would have enacted a developer/deployer framework modeled on Colorado's.

Bills in [California](https://leginfo.legislature.ca.gov/), New York, Illinois, and Rhode Island introduced in 2024 signal multi-state regulatory fragmentation ahead, as [Akin Gump predicted](https://www.akingump.com/en/insights/blogs/ag-data-dive/colorado-enacts-groundbreaking-ai-consumer-protection-legislation) using the GDPR/US privacy law proliferation analogy.

## Effective Dates and Compliance Timeline [HIGH confidence]

| Milestone | Date |
|---|---|
| SB 24-205 signed by Governor Polis | May 17, 2024 |
| Original effective date | February 1, 2026 |
| SB 25B-004 signed (delay bill) | August 28, 2025 |
| Revised effective date | June 30, 2026 |
| Governor's AI Policy Working Group proposes ADMT replacement | March 17, 2026 |
| Proposed ADMT Framework effective date (if enacted) | January 1, 2027 |

All developer and deployer obligations — including risk management programs, impact assessments, consumer notices, and human review procedures — must be operational by **June 30, 2026** if SB 24-205 remains in force. Organizations tracking the proposed ADMT replacement framework should monitor the 2026 Colorado legislative session for a repeal-and-replace bill.

## Impact Assessment [MEDIUM confidence]

### Broad Deployer Coverage

The "deploy = use" definition sweeps in any enterprise using a covered AI tool in employment, lending, health care, housing, insurance, education, government services, or legal services — regardless of whether the organization built or sells the AI. Most large enterprises deploying AI in HR, underwriting, credit, admissions, or care management are deployers and cannot avoid SB 24-205's requirements by outsourcing AI development to vendors.

### Supply Chain Compliance Pressure

Because deployers depend on developer documentation to complete their own impact assessments and qualify for the rebuttable presumption, AI vendor contracts need to incorporate:
- Developer documentation obligations (model cards, dataset cards, bias evaluation disclosures)
- 90-day incident notification provisions
- Representations about training data bias evaluation and risk mitigation measures
- Indemnification for documentation failures that undermine deployer compliance

### Multi-State Proliferation Risk

If SB 24-205 survives legal challenge and the ADMT replacement framework retains a comparable developer/deployer structure, Colorado may catalyze similar laws in additional states — mirroring the post-CCPA proliferation of comprehensive state privacy laws. Organizations investing now in compliant impact assessment processes, NIST AI RMF governance, and vendor documentation requirements position themselves for a lower-cost multi-state compliance posture.

### Federal Preemption Risk

The Trump administration's December 2025 [Executive Order on Eliminating State Law Obstruction of National AI Policy](https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy) explicitly targets "onerous" state AI laws. A DOJ legal challenge to SB 24-205 — or the ADMT replacement — could delay or eliminate enforcement before the June 30, 2026 effective date. Organizations should monitor Commerce Department guidance and any resulting litigation.

## Action Items

- **Determine deployer status now:** Audit all AI tools in use for employment, lending, health care, housing, insurance, education, and legal services decisions affecting Colorado consumers. Any such tool makes the organization a deployer subject to SB 24-205 obligations.
- **Assess developer status for AI customizers:** Organizations fine-tuning, adapting, or substantially retraining third-party AI models should obtain a legal opinion on whether their activity crosses the "intentionally and substantially modifies" threshold.
- **Implement NIST AI RMF or ISO 42001 governance:** Begin building the risk management program infrastructure required for the deployer rebuttable presumption — this investment will also serve future state AI compliance requirements.
- **Negotiate AI vendor contracts now:** Update AI procurement agreements to require developer documentation supply, incident notification within 90 days, and training data bias evaluation representations.
- **Prepare consumer notice workflows:** Draft and test the plain-language consumer notices required for consequential decisions; build appeal and human review procedures for adverse outcomes.
- **Monitor the 2026 Colorado legislative session:** Track the proposed ADMT replacement bill; if enacted, it will supersede SB 24-205 with a January 1, 2027 effective date and a substantially revised obligation structure.
- **Track federal preemption developments:** Monitor DOJ AI Litigation Task Force activity and Commerce Department AI guidance for signals about federal preemption of state AI laws.

## Related Reports

- [reports/ai-law/state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md](reports/ai-law/state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md) — Comprehensive primary analysis of SB 24-205 enactment with full statutory text analysis, legislative history, industry opposition, and exemptions.
- [reports/ai-law/state-legislation/colorado-sb205-akin-gump-developer-deployer-2024-05-30.md](reports/ai-law/state-legislation/colorado-sb205-akin-gump-developer-deployer-2024-05-30.md) — Companion Akin Gump analysis focused on the "intentionally and substantially modifies" developer definition, supply chain liability dynamics, and GDPR proliferation analogy.
- [reports/ai-law/state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md](reports/ai-law/state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md) — Covers SB 25B-004 delay to June 30, 2026, the failed 2025 special session, and the March 2026 ADMT replacement proposal.
- [reports/ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md](reports/ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md) — Trump December 2025 executive order targeting "onerous" state AI laws; Colorado SB 24-205 is a named target.
- [reports/ai-law/frameworks-guidance/nist-ai-rmf-critical-infrastructure-profile-2026-04-13.md](reports/ai-law/frameworks-guidance/nist-ai-rmf-critical-infrastructure-profile-2026-04-13.md) — NIST AI RMF guidance; the SB 24-205 deployer rebuttable presumption expressly references NIST AI RMF compliance as the primary recognized framework.
- [reports/ai-law/state-legislation/utah-uaipa-sb149-ai-disclosure-2024-05-15.md](reports/ai-law/state-legislation/utah-uaipa-sb149-ai-disclosure-2024-05-15.md) — Utah AI Policy Act enacted March 2024; the narrow disclosure-only predecessor against which Colorado's comprehensive approach is often benchmarked.

## Sources

1. [Akin Gump — Colorado Enacts Groundbreaking AI Consumer Protection Legislation (AG Data Dive)](https://www.akingump.com/en/insights/blogs/ag-data-dive/colorado-enacts-groundbreaking-ai-consumer-protection-legislation) — Primary source; Akin Gump blog post providing compliance-oriented analysis of SB 24-205
2. [Colorado General Assembly — SB 24-205 Bill Page](https://leg.colorado.gov/bills/sb24-205) — Official bill page with full text, legislative history, sponsors, and all versions
3. [Colorado SB 24-205 Signed Text (PDF)](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf) — Official enrolled and signed statute text; authoritative source for statutory definitions and obligations
4. [Akin Gump — Colorado Passes New Watershed AI Consumer Protection Bill](https://www.akingump.com/en/insights/alerts/colorado-passes-new-watershed-ai-consumer-protection-bill) — Akin Gump client alert on SB 24-205 signing; GDPR proliferation analogy framing
5. [JD Supra — Colorado Enacts Groundbreaking AI Consumer Protection Legislation (Akin Gump)](https://www.jdsupra.com/legalnews/colorado-enacts-groundbreaking-ai-7259153/) — JD Supra republication of the Akin Gump analysis with full text
6. [Mondaq — Colorado Enacts Groundbreaking AI Consumer Protection Legislation](https://mondaq.com/unitedstates/new-technology/1474668/colorado-enacts-groundbreaking-ai-consumer-protection-legislation) — Mondaq republication of the Akin Gump article
7. [National Association of Attorneys General — A Deep Dive into Colorado's Artificial Intelligence Act](https://www.naag.org/attorney-general-journal/a-deep-dive-into-colorados-artificial-intelligence-act/) — Independent statutory analysis covering exemptions, legislative history, and multi-state significance
8. [American Bar Association — Colorado Enacts Law Regulating High-Risk Artificial Intelligence Systems](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-july/colorado-enacts-law-regulating-high-risk-artificial-intelligence-systems/) — ABA analysis with legal definitions and compliance requirements
9. [Skadden — Colorado's Landmark AI Act: What Companies Need To Know](https://www.skadden.com/insights/publications/2024/06/colorados-landmark-ai-act) — Independent law firm analysis covering rebuttable presumption and impact assessment obligations
10. [Gibson Dunn — Colorado's Mile High AI Act: 6 Key Takeaways](https://www.gibsondunn.com/colorado-mile-high-ai-act-6-key-takeaways/) — Key takeaways analysis from Gibson Dunn covering compliance priorities
11. [Baker McKenzie — From Brussels to Boulder: Colorado AI Act vs. EU AI Act](https://insightplus.bakermckenzie.com/bm/data-technology/north-america-from-brussels-to-boulder-colorado-enacts-comprehensive-ai-law-on-the-heels-of-eus-ai-act-with-significant-obligations-for-business-and-employers) — Comparative EU AI Act / Colorado analysis
12. [Akin Gump — Colorado Postpones Implementation of Colorado AI Act, SB 24-205](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/colorado-postpones-implementation-of-colorado-ai-act-sb-24-205) — Akin Gump tracker entry on SB 25B-004 delay to June 30, 2026
13. [Baker Botts — Colorado AI Act Implementation Delayed (Sept 2025)](https://www.bakerbotts.com/thought-leadership/publications/2025/september/colorado-ai-act-implementation-delayed) — Analysis of SB 25B-004 delay legislation and its implications
14. [Mayer Brown — Colorado AI Policy Work Group Proposes Framework to Replace Colorado AI Act](https://www.mayerbrown.com/en/insights/publications/2026/03/the-colorado-ai-policy-work-group-proposes-an-updated-framework-to-replace-the-colorado-ai-act) — March 2026 ADMT replacement proposal analysis
15. [Colorado Governor's Office — AI Policy Workgroup Delivers Unanimous Support for Revised Policy Framework](https://governorsoffice.colorado.gov/governor/news/colorado-artificial-intelligence-policy-workgroup-delivers-unanimous-support-revised-policy) — Official press release on Governor Polis's endorsement of the ADMT replacement framework
16. [EU AI Act — Official Text (EUR-Lex)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) — Official EU AI Act text; comparison reference
17. [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence/ai-risk-management-framework) — NIST AI RMF; referenced in SB 24-205 as the primary recognized framework for deployer reasonable care presumption
18. [Colorado Attorney General — AI Enforcement and Rulemaking Page](https://coag.gov/ai/) — Official AG enforcement and rulemaking hub for SB 24-205
19. [Colorado General Assembly — SB 25B-004 (Delay Bill)](https://leg.colorado.gov/bills/sb25b-004) — Official bill page for the 2025 enforcement delay legislation extending the effective date to June 30, 2026
20. [Jones Day — Colorado Enacts AI Consumer Protection Legislation](https://www.jonesday.com/en/insights/2024/06/colorado-enacts-ai-consumer-protection-legislation) — Jones Day independent analysis of SB 24-205 obligations and compliance implications
