---
title: "Colorado Passes Artificial Intelligence Regulatory Bill: Taft Law Analysis of SB 24-205"
date: 2024-05-31
jurisdiction: "Colorado"
category: "ai-law"
development_type: "legislation"
finding_id: "SCAN-20240531-007"
topic_key: "colorado-a6785cd5-2024"
topic_type: "state_bill"
first_reported: 2024-05-31
last_updated: 2024-05-31
status_history: []
cluster: "Colorado AI Act (SB 24-205): Enforcement and Amendments"
cluster_slug: "colorado-ai-act-sb-24-205-enforcement"
---

# Colorado Passes Artificial Intelligence Regulatory Bill: Taft Law Analysis of SB 24-205

**Jurisdiction:** Colorado | **Category:** AI Law | **Date:** May 31, 2024

> **Note:** This report covers the Taft Stettinius & Hollister LLP analysis of Colorado SB 24-205, published via Lexology on May 31, 2024. For the primary enactment analysis, see [reports/ai-law/state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md](reports/ai-law/state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md). For subsequent enforcement delays, see [reports/ai-law/state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md](reports/ai-law/state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md).

## Executive Summary [HIGH confidence]

On May 17, 2024, Colorado Governor Jared Polis signed [Senate Bill 24-205](https://leg.colorado.gov/bills/sb24-205) — the Colorado Artificial Intelligence Act — into law, making Colorado the first U.S. state to enact comprehensive artificial intelligence regulation. Modeled in part on the EU AI Act's risk-based approach, the law imposes a duty of reasonable care on both **developers** and **deployers** of "high-risk" AI systems to protect consumers from algorithmic discrimination in consequential decisions affecting eight designated sectors. Enforcement rests exclusively with the Colorado Attorney General, with civil penalties of up to $20,000 per violation available under the Colorado Consumer Protection Act. Governor Polis signed with reservations, calling on legislators and stakeholders to improve the law before its effective date — a concern that ultimately contributed to a delay moving enforcement to June 30, 2026.

## Background [HIGH confidence]

### The Federal Policy Vacuum

By early 2024, Congress had not enacted comprehensive AI legislation despite multiple legislative proposals. Existing federal AI activity — including the Biden administration's October 2023 Executive Order on AI, the NIST AI Risk Management Framework (AI RMF 1.0) published in January 2023, and FTC guidance on AI practices — imposed no binding duties on private-sector AI developers or deployers. In the absence of federal action, states began filling the gap. Most early state AI laws addressed narrow topics: chatbot disclosure, employment AI, or deepfake prohibitions. No state had enacted a cross-sector framework imposing a general duty of care.

### Legislative Origins

SB 24-205 was introduced in the Colorado General Assembly and moved rapidly through both chambers. The bill's sponsors drew heavily on the structure of the [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689), which the European Parliament passed in March 2024. The timing was notable: Colorado's signing and the EU Act's entry into force occurred within months of each other, reflecting a convergent international movement toward risk-based AI regulation. The [official signed bill text](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf) is publicly available from the Colorado General Assembly.

As analyzed by [Taft Stettinius & Hollister LLP](https://www.taftlaw.com/news-events/law-bulletins/colorado-passes-artificial-intelligence-ai-regulatory-bill/), SB 24-205 borrows the EU AI Act's tiered, risk-based structure: by identifying eight specific high-risk use cases rather than regulating all AI systems uniformly, the Colorado legislature recognized that not all AI applications carry equivalent risk.

## Detailed Analysis [HIGH confidence]

### Core Obligation: Duty of Reasonable Care

The law's central requirement is a general duty of reasonable care imposed on both developers and deployers of high-risk AI systems. Per [Colorado General Assembly SB 24-205](https://leg.colorado.gov/bills/sb24-205), "developer of a high-risk artificial intelligence system" must "use reasonable care to protect consumers from any known or reasonably foreseeable risks of algorithmic discrimination in the high-risk system."

This obligation flows down the AI supply chain: developers must make available to deployers the information and documentation needed to complete impact assessments, and deployers must implement the safeguards described below.

### Key Definitions

**High-Risk AI System:** Any AI system that, when deployed, "makes, or is a substantial factor in making, a consequential decision." Critically, the law does not require that the AI system be the sole decision-maker — systems that are a "substantial factor" in a decision qualify even when a human makes the final call.

**Consequential Decision:** A decision that has a "material legal or similarly significant effect" on an individual's life in one of eight designated sectors:
1. Education opportunities (admissions, scholarships)
2. Employment (hiring, promotion, termination)
3. Financial services (credit, lending)
4. Healthcare (diagnosis, treatment)
5. Housing (rentals, mortgages)
6. Insurance (coverage, pricing)
7. Essential government services
8. Legal services

**Algorithmic Discrimination:** Any condition in which a high-risk AI system results in "unlawful differential treatment or impact" based on protected characteristics including age, race, color, ethnicity, sex, religion, disability, national origin, sexual orientation, or veteran status. Notably excluded from this definition: use of high-risk AI systems solely for self-testing or to increase diversity and address historical discrimination.

### Developer Obligations

Developers of high-risk AI systems must:

- Use reasonable care to protect consumers from known or reasonably foreseeable risks of algorithmic discrimination
- Make available to deployers the information and documentation necessary to complete an impact assessment
- Publish a publicly available statement summarizing the types of high-risk systems developed or modified and how the developer manages foreseeable risks of algorithmic discrimination
- Notify the Colorado Attorney General within 90 days of discovering a known or reasonably foreseeable risk of algorithmic discrimination, or within 90 days of receiving a credible report of such discrimination

### Deployer Obligations

Entities that deploy high-risk AI systems to make consequential decisions concerning Colorado consumers must:

- Implement a risk management policy and program for each high-risk system, calibrated to be reasonable given the [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence/ai-risk-management-framework), the deployer's size, the nature of the system, and the sensitivity of data processed
- Annually complete an impact assessment for each high-risk system covering: purpose and intended use, risk of algorithmic discrimination, steps to mitigate risk, description of training data and output data, performance metrics, transparency measures, and post-deployment monitoring
- Notify consumers if a high-risk system makes or substantially contributes to a consequential decision concerning them
- Provide consumers an opportunity to correct incorrect personal data the system processed
- Provide consumers an opportunity to appeal adverse consequential decisions via human review, if technically feasible
- Annually review each deployed high-risk system to ensure it is not causing algorithmic discrimination

### Small Business Deployer Exemption

A deployer with 50 or fewer full-time employees is exempt from the risk management program, impact assessment, and public statement requirements, provided all three of the following conditions are met:
1. The deployer does not train the AI system on its own proprietary data
2. The system does not continue to learn from the deployer's data after deployment
3. The deployer uses the system only for its intended purpose as specified by the developer, and provides consumers with any impact assessment furnished by the developer

Small business deployers remain subject to the general duty of care and consumer notification obligations.

### Sector-Specific Exemptions

The law provides full or partial compliance pathways for entities regulated by sector-specific AI governance:

- **Financial institutions:** Banks, credit unions, and their affiliates are in full compliance if subject to examination by a state or federal prudential regulator under any published guidance or regulations that apply to the use of high-risk systems
- **Insurers:** An insurer subject to Colorado's insurance statutes governing external consumer data and algorithms, and rules adopted by the Commissioner of Insurance, is in full compliance
- **HIPAA-regulated entities:** Healthcare entities subject to comparable federal requirements may qualify for analogous treatment

### AI Labeling Requirements

Separately from the high-risk AI provisions, SB 24-205 imposes broader **AI disclosure and labeling requirements** applicable to any deployer using an AI system to interact with consumers — not limited to high-risk systems. Deployers must disclose to consumers when they are interacting with an AI system rather than a human, upon request. These requirements represent a broader compliance footprint than the high-risk framework alone.

## Impact Assessment [HIGH confidence]

### Affected Organizations

The law applies to any person "doing business in" Colorado that develops or deploys high-risk AI systems — not only Colorado-domiciled entities. The eight designated sectors create broad coverage across industries typically relying on algorithmic decision-making: financial services (credit scoring, loan underwriting), healthcare (diagnostic tools, treatment recommendation engines), employment (applicant screening, performance management), insurance (underwriting, claims), and real estate (lending, tenant screening).

Organizations operating nationally with AI tools that touch Colorado consumers — even without a physical Colorado presence — must assess whether those tools meet the "consequential decision" threshold.

### Compliance Timeline

| Milestone | Date |
|-----------|------|
| Bill signed | May 17, 2024 |
| Original effective date | February 1, 2026 |
| Enforcement delayed (SB 25B-004) | August 2025 special session |
| Current effective date | June 30, 2026 |

The delay followed Governor Polis's expressed reservations and significant industry opposition. Organizations should treat June 30, 2026 as the operative compliance deadline absent further legislative action.

### Enforcement Outlook

The [Colorado Attorney General](https://www.naag.org/attorney-general-journal/a-deep-dive-into-colorados-artificial-intelligence-act/) holds exclusive enforcement authority — there is no private right of action. Before initiating enforcement, the AG must provide written notice of a violation and allow a 60-day cure period. Violations constitute deceptive trade practices under the Colorado Consumer Protection Act, exposing violators to civil penalties of up to $20,000 per violation. Because each affected consumer or transaction counts separately, penalties can accumulate rapidly: a system discriminating against 100 consumers could produce up to $2 million in theoretical exposure.

The AG also holds rulemaking authority to implement the act's requirements, which may produce additional compliance obligations before the effective date.

### Industry and Stakeholder Reactions

The law generated significant opposition from industry groups. The U.S. Chamber of Commerce argued the law could hamper small business adoption of AI. The Chamber of Progress and the Consumer Technology Association urged Governor Polis to veto SB 24-205 entirely, arguing that strengthening existing consumer protection and civil rights laws would be a more appropriate approach than sector-agnostic AI regulation. Governor Polis signed with reservations, calling on the legislature and stakeholders to "significantly improve" the law before it takes effect and expressing hope that Congress would enact federal legislation to preempt it with "a needed cohesive federal approach." These concerns reflected a broader industry view that Colorado's framework — by imposing obligations on developers and deployers who may not know each other's practices — creates compliance challenges unique to AI supply chains.

## Action Items

- Map your AI systems to the eight high-risk categories and determine whether any systems make or substantially contribute to "consequential decisions" affecting Colorado consumers
- Establish documentation protocols for AI system risk assessments, even before the June 30, 2026 effective date, to ensure sufficient lead time
- Developers: prepare publicly available statements summarizing high-risk AI systems and risk management practices
- Deployers: evaluate applicability of small business exemption (50-or-fewer-employee threshold with the three additional conditions)
- Assess applicability of sector-specific compliance pathways (financial, insurance, HIPAA)
- Implement consumer disclosure, correction, and appeal mechanisms for high-risk AI decisions
- Monitor Colorado AG rulemaking for implementing regulations that may impose additional obligations
- Track federal preemption developments — the White House has indicated support for federal legislation that would supersede state AI laws

## Related Reports

- [Colorado Becomes the First State to Pass Comprehensive AI Legislation (SB 24-205)](reports/ai-law/state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md) — Primary enactment report with full legislative history and statutory analysis
- [Colorado Legislature Approves AI Bill Targeting "High-Risk" Systems and AI Labeling (SB 24-205)](reports/ai-law/state-legislation/colorado-sb205-ai-act-2024-05-20.md) — Holland & Knight analysis emphasizing AI labeling provisions
- [The Colorado AI Act: America's First Comprehensive AI Law (SB 24-205)](reports/ai-law/state-legislation/colorado-sb205-ai-act-2024-05-29.md) — Comparative EU AI Act analysis by Herzog Fox & Neeman
- [Colorado AI Act Enforcement Delayed](reports/ai-law/state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md) — Post-2024 developments including the August 2025 special session delay to June 30, 2026
- [Trump Executive Order Establishes National AI Policy Framework Preempting State Laws](reports/ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md) — Federal preemption threat directly affecting Colorado AI Act's survival

## Sources

1. [SB24-205 Consumer Protections for Artificial Intelligence — Colorado General Assembly](https://leg.colorado.gov/bills/sb24-205) — Official legislative page with bill status, sponsors, and version history
2. [Colorado's SB 24-205 (The AI Act) — Official Signed Text](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf) — Official enrolled and signed bill text from the Colorado General Assembly
3. [Colorado Passes Artificial Intelligence (AI) Regulatory Bill — Taft Law](https://www.taftlaw.com/news-events/law-bulletins/colorado-passes-artificial-intelligence-ai-regulatory-bill/) — Primary source analysis from Taft Stettinius & Hollister LLP, the source of this finding
4. [A Deep Dive into Colorado's Artificial Intelligence Act — NAAG](https://www.naag.org/attorney-general-journal/a-deep-dive-into-colorados-artificial-intelligence-act/) — Detailed statutory analysis from the National Association of Attorneys General covering enforcement and definitions
5. [Colorado Governor Signs Broad AI Bill Regulating Employment Decisions — Seyfarth Shaw LLP](https://www.seyfarth.com/news-insights/colorado-governor-signs-broad-ai-bill-regulating-employment-decisions.html) — Law firm analysis covering employment context and Governor Polis's signing statement
6. [Colorado's Historic SB 24-205 Signed Into Law — Epstein Becker Green / Workforce Bulletin](https://www.workforcebulletin.com/colorados-historic-sb-24-205-concerning-consumer-protections-in-interactions-with-ai-signed-into-law-after-passing-state-senate-and-house) — Analysis of legislative passage and industry opposition
7. [Mile-High Risk: Colorado Enacts Risk-Based AI Regulation — Davis Wright Tremaine](https://www.dwt.com/blogs/artificial-intelligence-law-advisor/2024/05/colorado-enacts-first-risk-based-ai-regulation-law) — Risk-based framework analysis with NIST AI RMF context
8. [Colorado Postpones Implementation of Colorado AI Act, SB 24-205 — Akin Gump](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/colorado-postpones-implementation-of-colorado-ai-act-sb-24-205) — Analysis of enforcement delay to June 30, 2026 following 2025 special session
9. [FAQ on Colorado's Consumer Artificial Intelligence Act — Center for Democracy and Technology](https://cdt.org/insights/faq-on-colorados-consumer-artificial-intelligence-act-sb-24-205/) — Civil society perspective on consumer protection provisions
10. [Colorado SB24-205 — Regulations.AI](https://regulations.ai/regulations/colorado-sb-205-consumer-protections-ai-2024) — Secondary compliance reference with key definitions and exemptions
