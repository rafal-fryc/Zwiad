---
title: "Colorado AI Act: Kilpatrick Townsend Analysis of Algorithmic Discrimination Obligations (SB 24-205)"
date: 2024-06-07
jurisdiction: "Colorado"
category: "ai-law"
development_type: "legislation"
finding_id: "SCAN-20240607-014"
topic_key: "colorado-4147b0e5-2024"
topic_type: "state_bill"
topic_key_confidence: "low"
first_reported: 2024-06-07
last_updated: 2024-06-07
status_history: []
cluster: "Colorado AI Act (SB 24-205): Enforcement and Amendments"
cluster_slug: "colorado-ai-act-sb-24-205-enforcement"
---

# Colorado AI Act: Kilpatrick Townsend Analysis of Algorithmic Discrimination Obligations (SB 24-205)

**Jurisdiction:** Colorado | **Category:** AI Law | **Date:** June 7, 2024

> **Note:** The knowledge base contains extensive coverage of Colorado SB 24-205. This memo synthesizes the [Kilpatrick Townsend & Stockton LLP analysis](https://ktslaw.com/en/Insights/Alert/2024/6/Byte-sized-Justice-Colorados-New-AI-Bill-Seeks-to-Address-Algorithmic-Discrimination) published June 2024, which offers several notable critiques not widely emphasized elsewhere — including the structural weakness of the HIPAA exemption and unresolved scope questions for ad tech. For the primary comprehensive statutory analysis, see [reports/ai-law/state-legislation/colorado-ai-act-sb205-2024.md](reports/ai-law/state-legislation/colorado-ai-act-sb205-2024.md). For enforcement delay developments through 2025, see [reports/ai-law/state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md](reports/ai-law/state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md).

## Executive Summary [HIGH confidence]

On May 17, 2024, Colorado Governor Jared Polis signed [Senate Bill 24-205](https://leg.colorado.gov/bills/sb24-205) — the Colorado Artificial Intelligence Act (CAIA) — into law, making Colorado the first US state to enact comprehensive cross-sectoral artificial intelligence regulation. As analyzed by [Kilpatrick Townsend & Stockton LLP](https://ktslaw.com/en/Insights/Alert/2024/6/Byte-sized-Justice-Colorados-New-AI-Bill-Seeks-to-Address-Algorithmic-Discrimination), the law focuses primarily on preventing **algorithmic discrimination** — unlawful differential treatment of consumers based on protected characteristics — in eight designated high-stakes sectors. The law creates distinct but interrelated obligations for AI **developers** and **deployers**, with the Attorney General holding exclusive enforcement authority and no private right of action. The Kilpatrick analysis is notable for raising two issues that received less attention in contemporaneous law firm coverage: (1) the HIPAA exemption is structurally ineffective because it exempts only non-high-risk healthcare decisions, yet the law only regulates high-risk systems in the first place; and (2) the law's scope may extend to ad tech systems that deliver targeted advertising for high-risk service categories. The original effective date of February 1, 2026 was subsequently delayed to June 30, 2026 by [SB 25B-004](https://leg.colorado.gov/bills/sb25b-004), signed August 28, 2025.

## Background [HIGH confidence]

### Colorado as First Mover

Colorado's enactment of SB 24-205 followed a period of fragmented state AI regulation. Prior state AI laws addressed narrow categories: chatbot disclosure requirements in California, employment screening audits in New York City, and deepfake prohibitions in several states. No US state had previously enacted a cross-sector framework imposing substantive obligations on both AI developers and the businesses that deploy their systems. Colorado's bill drew structural inspiration from the [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689), which the European Parliament approved in March 2024, adopting the EU's risk-tiered approach — regulating only high-risk applications rather than all AI systems.

The bill's primary Senate sponsor, Senate Majority Leader Robert Rodriguez, described the legislation as a "chassis" — an initial framework focused first on bias, intended to be built upon as legislative understanding of AI matures. This framing was significant: it acknowledged the law's limitations while signaling legislative intent to expand regulation over time. The [official signed bill text](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf) is publicly available from the Colorado General Assembly.

Governor Polis signed the bill with reservations, expressing hope that Congress would enact federal legislation establishing "a needed cohesive federal approach" that would supersede state AI laws. Despite these reservations, the law was enacted and has survived — though it has been delayed.

### Regulatory and Legislative Context

The [Colorado Attorney General's office](https://coag.gov/ai/) has been granted rulemaking authority to implement the CAIA, including authority over developer documentation requirements, impact assessment standards, notice and disclosure formats, risk management standards, and the conditions for affirmative defenses. This rulemaking authority — absent from comparable legislation that failed in Connecticut's 2024 session — gave Colorado's enforcement architecture considerably more flexibility than a purely statutory scheme.

## Detailed Analysis [HIGH confidence]

### Scope: Who and What Is Covered

The CAIA applies to any person "doing business in" Colorado that develops or deploys a **high-risk artificial intelligence system**. Physical presence in Colorado is not required; national businesses whose AI tools affect Colorado consumers must assess applicability.

A **high-risk AI system** is defined as any AI system that, when deployed, "makes, or is a substantial factor in making, a consequential decision." The "substantial factor" language is deliberately broad: a system need not be the sole or primary driver of a decision to qualify. Human oversight or final review does not automatically remove a system from the high-risk category.

A **consequential decision** is one with "a material legal or similarly significant effect" on an individual's access to, or the terms of, services in eight sectors:

1. Education enrollment and opportunities (admissions, scholarships)
2. Employment and employment opportunities (hiring, promotion, termination)
3. Financial and lending services (credit, loans)
4. Essential government services
5. Healthcare services (diagnosis, treatment)
6. Housing (rentals, mortgages)
7. Insurance (coverage, underwriting, pricing)
8. Legal services

### The Ad Tech Scope Question [MEDIUM confidence]

A notable interpretive question raised by [Kilpatrick Townsend](https://ktslaw.com/en/Insights/Alert/2024/6/Byte-sized-Justice-Colorados-New-AI-Bill-Seeks-to-Address-Algorithmic-Discrimination) concerns the potential reach of the "consequential decision" definition into advertising technology. The question: could an AI system that decides which ads to show a consumer — for example, deciding which consumers see a housing offer, a job posting, or a financial product — constitute "making or substantially contributing to a consequential decision" within the CAIA's scope?

The law's eight sectors include employment, housing, and financial services — precisely the categories where targeted advertising frequently occurs. If a digital ad delivery algorithm determines that certain consumers do not see a mortgage product advertisement, has that system "made" a consequential decision affecting their access to financial or lending services? This question has not been resolved by the Colorado Attorney General through rulemaking, and the statutory text does not expressly address advertising. The ad tech industry should monitor the AG's rulemaking process, as clarification in implementing regulations could significantly expand or contract the law's practical coverage.

### Developer Obligations

Per the [official bill text](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf), developers of high-risk AI systems must:

- Exercise reasonable care to protect consumers from **known or reasonably foreseeable** risks of algorithmic discrimination
- Make available to deployers the information and documentation necessary to complete impact assessments
- Publish a publicly available statement summarizing high-risk AI types developed or modified and the developer's risk management practices
- Notify the Colorado Attorney General within 90 days of discovering a known or reasonably foreseeable risk of algorithmic discrimination, or receiving a credible discrimination report

Developer obligations focus on the supply chain: they must equip deployers with the information needed to run the deployed system responsibly.

### Deployer Obligations

Businesses that deploy high-risk AI systems to make or contribute to consequential decisions affecting Colorado consumers bear the more extensive compliance obligations:

- Implement a risk management policy and program calibrated to the [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence/ai-risk-management-framework), organizational size, system nature, and data sensitivity
- Complete annual impact assessments for each high-risk system — covering purpose, discrimination risks, mitigation steps, training data, performance metrics, transparency measures, and post-deployment monitoring
- Notify consumers when a high-risk system makes or substantially contributes to a consequential decision about them
- Provide consumers the right to correct inaccurate personal data the system processed
- Provide consumers a right to appeal adverse consequential decisions through human review, where technically feasible
- Conduct annual reviews of deployed systems to verify they are not producing algorithmic discrimination

### Small Business Deployer Exemption

Deployers with 50 or fewer full-time employees are exempt from the risk management program, annual impact assessment, and public statement requirements — but only if all three of the following conditions are met:

1. The deployer does not train the system on proprietary data
2. The system does not continue learning from the deployer's data post-deployment
3. The deployer uses the system only for its intended purpose as specified by the developer, and provides consumers any impact assessment furnished by the developer

Small business deployers remain subject to the duty of care and consumer notification obligations regardless of size.

### Sector-Specific Compliance Pathways

**Financial institutions:** Banks, credit unions, and their affiliates are in full compliance if subject to examination by a state or federal prudential regulator under guidance or regulations that apply to high-risk system use.

**Insurers:** An insurer subject to [Colorado's insurance statute Section 10-3-1104.9](https://leg.colorado.gov/bills/sb24-205), which addresses external consumer data and algorithmic discrimination, and implementing rules adopted by the Commissioner of Insurance, is in full compliance.

### The HIPAA Exemption Problem [MEDIUM confidence]

One of the Kilpatrick Townsend analysis's most pointed observations concerns the law's HIPAA exemption. The CAIA provides that entities subject to HIPAA and making "non-high-risk" healthcare AI decisions may qualify for an exemption. However, Kilpatrick Townsend identified a critical structural weakness: the CAIA only applies to **high-risk** AI systems in the first place. An exemption covering only non-high-risk healthcare decisions therefore exempts precisely the systems and decisions that were never subject to the law — making the exemption practically ineffective.

This stands in contrast to the insurer exemption, which maps directly onto the regulated conduct: an insurer already subject to state algorithmic discrimination requirements is fully compliant with the overlapping CAIA requirements because the underlying regulatory obligation is satisfied. The HIPAA exemption's failure to achieve the same result reflects a drafting flaw that the Attorney General's rulemaking authority may attempt to cure, but absent regulatory clarification, healthcare entities should not assume the HIPAA exemption provides meaningful relief.

### Enforcement Architecture

Enforcement rests exclusively with the [Colorado Attorney General](https://coag.gov/ai/). There is no private right of action, which limits litigation risk compared to laws with citizen suit provisions. Before initiating enforcement, the AG must provide written notice and allow a 60-day cure period for violations. Violations constitute deceptive trade practices under the Colorado Consumer Protection Act, subject to civil penalties of up to **$20,000 per violation**. Because each affected consumer or transaction counts separately, penalties can aggregate rapidly at scale.

The AG also holds broad rulemaking authority, which may produce additional compliance obligations before the June 30, 2026 effective date. Organizations should monitor rulemaking activity through the [Colorado AG's AI rulemaking page](https://coag.gov/ai/).

## Impact Assessment [HIGH confidence]

### National Significance

Colorado's CAIA established the US state-level template for algorithmic accountability regulation. Its risk-based, cross-sectoral structure — targeting consequential decisions affecting individuals in eight high-stakes domains — has been studied and partially replicated in legislative proposals in other states. As analyzed by the [American Bar Association](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-july/colorado-enacts-law-regulating-high-risk-artificial-intelligence-systems/), Colorado became the first state to impose substantive obligations on both developers and deployers, creating a supply-chain compliance model with no clear US precedent at the time of enactment.

The law's national significance is tempered by uncertainty about its survival. Governor Polis expressed reservations at signing, the [Trump administration's January 2025 executive order on AI](https://www.whitehouse.gov/presidential-actions/2025/01/removing-barriers-to-american-leadership-in-artificial-intelligence/) directed agencies to preempt "inconsistent" state AI laws, and the [TAKE IT DOWN Act](https://www.congress.gov/bill/119th-congress/senate-bill/146) debate has renewed attention to federal AI preemption. The June 30, 2026 effective date remains operative as of this writing, but further delays or amendments remain possible.

### Compliance Timeline

| Milestone | Date |
|-----------|------|
| SB 24-205 signed by Governor Polis | May 17, 2024 |
| Original effective date | February 1, 2026 |
| SB 25B-004 signed (enforcement delay) | August 28, 2025 |
| Current operative effective date | June 30, 2026 |

### Affected Industries

The eight-sector scope creates broad coverage across industries that commonly use algorithmic or AI-assisted decision-making:

- **Financial services:** Credit scoring, underwriting, loan decisioning systems
- **Employment:** Applicant tracking and screening tools, performance management AI, workforce analytics
- **Healthcare:** Diagnostic tools, treatment recommendation engines, patient triage systems
- **Insurance:** Claims processing AI, underwriting algorithms, pricing models
- **Housing:** Tenant screening AI, mortgage underwriting algorithms
- **Ad tech:** Systems that deliver targeted advertising for high-risk-sector services (scope question unresolved)

Organizations operating nationally with AI tools that touch Colorado consumers must assess whether those tools meet the "substantial factor in making a consequential decision" threshold — even without a physical Colorado presence.

## Action Items

- Audit AI systems used in employment, lending, healthcare, housing, insurance, and government services for the Colorado AI Act's "high-risk" footprint; document whether each system makes or substantially contributes to consequential decisions
- Do not assume the HIPAA exemption provides coverage: consult with counsel on whether healthcare AI tools qualify given the structural drafting issue identified in the Kilpatrick analysis
- For financial services: verify that applicable federal or state prudential regulatory oversight covers your AI system use before relying on the financial institution compliance pathway
- For ad tech and marketing technology: assess whether AI-driven ad delivery for housing, employment, financial products, or healthcare services could constitute a consequential decision; monitor Colorado AG rulemaking for clarification
- Deployers: implement or document annual impact assessment procedures for each high-risk system, with sufficient lead time before June 30, 2026
- Developers: prepare publicly available statements on high-risk AI types and risk management practices
- Small businesses (50 or fewer employees): confirm all three conditions for the small-business deployer exemption are satisfied; partial satisfaction does not qualify
- Monitor Colorado AG rulemaking at coag.gov/ai for implementing regulations that may expand compliance obligations

## Related Reports

- [Colorado Becomes the First State to Pass Comprehensive AI Legislation (SB 24-205)](reports/ai-law/state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md) — Primary enactment report with full legislative history and statutory analysis
- [Colorado AI Act Enforcement Delayed](reports/ai-law/state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md) — Post-2024 developments including the August 2025 special session delay to June 30, 2026
- [Colorado SB 24-205: Landmark AI Act — Essential Business Compliance Insights (Venable LLP Analysis)](reports/ai-law/state-legislation/colorado-sb24-205-venable-compliance-2024-06-06.md) — Contemporaneous compliance-focused analysis covering similar obligations
- [Colorado AI Act: Hogan Lovells Data Chronicles Practitioner Analysis (SB 24-205)](reports/ai-law/state-legislation/colorado-hogan-lovells-data-chronicles-ai-act-2024-06-06.md) — Practitioner roundtable analysis of the same legislation
- [NYC Local Law 144: Automated Employment Decision Tool (AEDT) Bias Audit Requirements](reports/ai-law/employment-ai/nyc-local-law-144-aedt-bias-audit-2024-05-23.md) — Comparative employment-AI regulation from the same period; contrast with Colorado's broader sector approach

## Sources

1. [SB24-205 Consumer Protections for Artificial Intelligence — Colorado General Assembly](https://leg.colorado.gov/bills/sb24-205) — Official legislative page with bill status, sponsors, and version history
2. [Colorado's SB 24-205 (The AI Act) — Official Signed Text](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf) — Official enrolled and signed bill text from the Colorado General Assembly
3. [Byte-sized Justice: Colorado's New AI Bill Seeks to Address Algorithmic Discrimination — Kilpatrick Townsend & Stockton LLP](https://ktslaw.com/en/Insights/Alert/2024/6/Byte-sized-Justice-Colorados-New-AI-Bill-Seeks-to-Address-Algorithmic-Discrimination) — Primary source for this report: the Kilpatrick Townsend analysis cited by the finding, including HIPAA exemption critique and ad tech scope questions
4. [Colorado Postpones Implementation of Colorado AI Act, SB 24-205 — Akin Gump](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/colorado-postpones-implementation-of-colorado-ai-act-sb-24-205) — Analysis of enforcement delay to June 30, 2026 following August 2025 special session
5. [Colorado Anti-Discrimination in AI Law (ADAI) Rulemaking — Colorado Attorney General](https://coag.gov/ai/) — Official Colorado AG page on ADAI rulemaking and enforcement authority
6. [Colorado Enacts Law Regulating High-Risk Artificial Intelligence Systems — American Bar Association](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-july/colorado-enacts-law-regulating-high-risk-artificial-intelligence-systems/) — ABA analysis of the law's national significance and scope; confirms Colorado as first state with cross-sector AI obligations on developers and deployers
7. [A Deep Dive into Colorado's Artificial Intelligence Act — National Association of Attorneys General](https://www.naag.org/attorney-general-journal/a-deep-dive-into-colorados-artificial-intelligence-act/) — Statutory analysis from NAAG covering enforcement architecture, definitions, and AG rulemaking authority
8. [AI Regulation: Colorado Artificial Intelligence Act (CAIA) — KPMG](https://kpmg.com/us/en/articles/2024/ai-regulation-colorado-artificial-intelligence-act-caia-reg-alert.html) — Compliance-focused analysis of CAIA developer and deployer obligations
9. [Colorado's AI law delayed until June 2026: What the latest setback means for businesses — Clark Hill PLC](https://www.clarkhill.com/news-events/news/colorados-ai-law-delayed-until-june-2026-what-the-latest-setback-means-for-businesses/) — Analysis of the August 2025 delay and remaining compliance window
10. [Byte-sized Justice: Colorado's New AI Bill (Japanese/English mirror) — Kilpatrick Townsend](https://kilpatricktownsend.jp/en/colorados-new-ai-bill_english/) — Mirror copy of the Kilpatrick analysis on the firm's Japan site, confirming publication authenticity
