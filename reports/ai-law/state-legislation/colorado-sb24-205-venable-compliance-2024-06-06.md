---
title: "Colorado SB 24-205: Landmark AI Act — Essential Business Compliance Insights (Venable LLP Analysis)"
date: 2024-06-06
jurisdiction: "Colorado"
category: "ai-law"
development_type: "legislation"
finding_id: "SCAN-20240606-013"
topic_key: "colorado-375c832a-2024"
topic_type: "state_bill"
topic_key_confidence: "low"
first_reported: 2024-06-06
last_updated: 2026-04-21
status_history: []
cluster: "Colorado AI Act (SB 24-205): Enforcement and Amendments"
cluster_slug: "colorado-ai-act-sb-24-205-enforcement"
---

# Colorado SB 24-205: Landmark AI Act — Essential Business Compliance Insights (Venable LLP Analysis)

**Jurisdiction:** Colorado | **Category:** AI Law | **Date:** June 6, 2024

> **Note:** The knowledge base contains extensive coverage of Colorado SB 24-205 from multiple law firm perspectives. This memo synthesizes the [Venable LLP compliance-focused analysis](https://www.venable.com/insights/publications/2024/05/colorados-landmark-ai-law-essential-insights) published in May 2024 and incorporates material updates through April 2026, including the implementation delay and ongoing legislative uncertainty. Readers seeking the most comprehensive statutory analysis should consult [reports/ai-law/state-legislation/colorado-ai-act-sb205-2024.md](reports/ai-law/state-legislation/colorado-ai-act-sb205-2024.md).

## Executive Summary [HIGH confidence]

On May 17, 2024, Colorado Governor Jared Polis signed [Senate Bill 24-205](https://leg.colorado.gov/bills/sb24-205) — the first comprehensive US state law imposing substantive obligations on developers and deployers of high-risk artificial intelligence systems. The law creates a duty of reasonable care to prevent algorithmic discrimination in consequential decisions affecting employment, education, housing, healthcare, financial services, insurance, legal services, and essential government services. [Venable LLP's analysis](https://www.venable.com/insights/publications/2024/05/colorados-landmark-ai-law-essential-insights) emphasizes the compliance burden for businesses already using or planning to deploy AI tools in these sectors, noting that obligations extend beyond AI vendors to any business that uses AI in high-stakes decision-making contexts. The Colorado Attorney General holds exclusive enforcement authority with penalties up to $20,000 per violation under the Colorado Consumer Protection Act. The original February 1, 2026 effective date was subsequently delayed to June 30, 2026 by [SB 25B-004](https://leg.colorado.gov/bills/sb25b-004), signed August 28, 2025, amid ongoing legislative uncertainty about whether the law will be substantially amended or replaced before that deadline.

## Background [HIGH confidence]

### Colorado's Regulatory Leadership

Colorado became the first US state to enact comprehensive AI legislation targeting high-risk systems when Governor Polis signed SB 24-205 on May 17, 2024. The bill was sponsored by Senate Majority Leader Robert Rodriguez and largely tracked an analogous bill (SB 2) that failed in Connecticut's 2024 legislative session. Colorado's version added an important feature absent from the Connecticut draft: explicit rulemaking authority for the state Attorney General.

The bill built on Colorado's existing data protection infrastructure. Colorado enacted the [Colorado Privacy Act (CPA)](https://leg.colorado.gov/bills/sb21-190) in 2021, giving its legislature experience with complex data-protection frameworks. SB 24-205 extends that foundation into the domain of AI-assisted decision-making, targeting the specific risk of algorithmic discrimination rather than data privacy generally.

Governor Polis signed the bill while simultaneously publishing a letter expressing substantive reservations — the first governor to approve a bill while publicly calling for its federal replacement. He criticized the legislation for creating a "complex compliance regime" and expressed concern about its impact on technological innovation, calling on sponsors to "significantly improve" the law before its effective date and urging Congress to enact preemptive federal legislation.

### The Federal Landscape at Signing

At the time SB 24-205 was signed, no comprehensive federal AI law existed. The Biden administration had issued a sweeping [Executive Order on Safe, Secure, and Trustworthy AI](https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/) in October 2023, and the [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/artificial-intelligence) had been published in January 2023. Neither imposed binding legal duties on private-sector entities. Colorado's action reflected a broader wave of state AI legislation, with Utah, Tennessee, and other states also passing AI-related statutes in 2024.

## Detailed Analysis [HIGH confidence]

### Statutory Structure and Core Duty

SB 24-205 is codified at [Colorado Revised Statutes §§ 6-1-1701 through 6-1-1709](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf). Its central obligation is a duty of "reasonable care" imposed on both developers and deployers of high-risk AI systems "to protect consumers from any known or reasonably foreseeable risks of algorithmic discrimination." The statute creates parallel but distinct obligation tracks for each actor type.

### Key Definitions

The statute's scope depends critically on several cascading definitions:

**High-Risk AI System:** Any AI system that, when deployed, makes or is a "substantial factor" in making a **consequential decision**. The same model can be high-risk in one deployment context but not in another — risk is assessed at the deployment level, not the system level.

**Consequential Decision:** A decision with "material legal or similarly significant effect" on a consumer's access to, or conditions of: education enrollment, employment, financial or lending services, essential government services, healthcare, housing, insurance, or legal services.

**Substantial Factor:** A factor that "assists in making a consequential decision or is capable of altering the outcome" of such a decision. The statute expressly excludes factors that only provide information or data, or perform "narrow procedural or preparatory tasks" — an important limiting principle for businesses using AI for preliminary data gathering rather than decision-making.

**Algorithmic Discrimination:** Any condition where use of an AI system results in "unlawful differential treatment or impact" disfavoring an individual or group based on protected characteristics. Colorado's protected characteristics include: age, color, disability, ethnicity, genetic information, limited English proficiency, national origin, race, religion, reproductive health, sex, veteran status, and any other protected classification under Colorado or federal law.

**Developer:** Any person doing business in Colorado that develops or "intentionally and substantially modifies" a high-risk AI system offered to deployers. Notably, a developer need not be the original creator — entities that substantially modify third-party AI systems are captured.

**Deployer:** Any person doing business in Colorado that deploys a high-risk AI system to make or substantially factor into consequential decisions about consumers.

### Developer Obligations [HIGH confidence]

Developers must, per [Section 6-1-1703](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf):

1. **Maintain documentation** sufficient for deployers to complete impact assessments, including model cards, dataset cards, or other technical artifacts.
2. **Disclose to deployers** the intended uses, types of data processed, data governance practices, known limitations, performance metrics, and mitigation measures for algorithmic discrimination risks.
3. **Publish a public statement** on a website (or in a public use-case inventory) summarizing their risk management approach for each type of high-risk AI system they develop or modify.
4. **Report algorithmic discrimination** to the Colorado Attorney General within 90 days of discovering any known or reasonably foreseeable algorithmic discrimination in a deployed system.
5. **Notify deployers** when they discover algorithmic discrimination in a system deployed by those deployers.

### Deployer Obligations [HIGH confidence]

Deployers face the most operationally intensive obligations. Under [Section 6-1-1704](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf), deployers must:

1. **Implement a risk management program** that governs the deployment and use of high-risk AI systems, aligned with a recognized framework (NIST AI RMF, ISO/IEC 42001, or another framework designated by the Attorney General).
2. **Complete impact assessments** before initial deployment, annually thereafter, and within 90 days of any intentional and substantial modification. The assessment must document: the system's purpose and intended use cases, analysis of algorithmic discrimination risks, data categories processed, outputs generated, post-deployment monitoring measures, and data governance practices.
3. **Provide consumer notices** when a high-risk AI system makes or substantially factors into a consequential decision about a consumer. Notices must describe: the purpose of the system, the data categories processed, how consumers can access and correct their data, and how consumers can appeal a consequential decision.
4. **Publish a public statement** on a website describing the types of high-risk AI systems deployed and general risk management practices.
5. **Report algorithmic discrimination** to the Colorado Attorney General within 90 days of discovery.

### Small Business Exemptions [MEDIUM confidence]

[Venable LLP notes](https://www.venable.com/insights/publications/2024/05/colorados-landmark-ai-law-essential-insights) that SB 24-205 includes a conditional exemption for small deployers (fewer than 50 full-time employees). The exemption removes the obligation to maintain a risk management program, complete impact assessments, and publish public statements — but only if all three conditions are satisfied:

1. The deployer does not use its own data to train or substantially customize the AI system.
2. The deployer limits its use to purposes previously disclosed by the developer.
3. The deployer provides consumers with the developer's impact assessment in lieu of its own.

Small deployers retain the obligation to provide consumer notices and to exercise reasonable care to prevent algorithmic discrimination. Businesses near the 50-employee threshold should assess their headcount carefully, as the exemption is binary.

### Affirmative Defense [HIGH confidence]

An affirmative defense is available to any developer or deployer that: (a) complies with the latest version of the [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence), ISO/IEC 42001, or another recognized framework designated by the Attorney General; and (b) discovers and cures a violation through internal testing or red-teaming before an enforcement action is brought. This provision makes NIST AI RMF adoption directly legally significant rather than merely aspirational for Colorado-regulated entities.

### Enforcement Architecture [HIGH confidence]

The [Colorado Attorney General](https://coag.gov/ai/) holds exclusive enforcement authority — there is no private right of action under SB 24-205. Violations are treated as unfair trade practices under the [Colorado Consumer Protection Act (CRS Title 6, Article 1)](https://law.justia.com/codes/colorado/title-6/fair-trade-and-restraint-of-trade/article-1/), exposing violators to civil penalties of $20,000 or more per violation. Each affected consumer, each high-risk AI system, and each incident can constitute a separate violation, creating substantial aggregated exposure for large-scale deployers.

The Attorney General also has rulemaking authority to implement and enforce the Act — a feature that distinguishes Colorado's approach from other state AI efforts. Attorney General rulemaking guidance is expected ahead of the June 30, 2026 effective date, though as of April 2026 no final rules have been issued.

## Implementation Timeline and Legislative Uncertainty [HIGH confidence]

### The August 2025 Special Session Failure

Industry opposition to SB 24-205 intensified through 2024 and into 2025. In August 2025, the Colorado legislature held a six-day special session at which four competing amendment bills were introduced. The session ultimately collapsed after technology companies objected to proposed liability provisions in Senate Majority Leader Rodriguez's "AI Sunshine Act" (SB 4), which would have narrowed the law while maintaining core consumer protections.

### Implementation Delay via SB 25B-004

Following the special session collapse, Governor Polis on August 28, 2025 signed [SB 25B-004](https://leg.colorado.gov/bills/sb25b-004), the "Increase Transparency for Algorithmic Systems Act." This bill did nothing more than delay the effective date from February 1, 2026 to June 30, 2026 — all substantive obligations, exemptions, rebuttable presumptions, and affirmative defenses remain unchanged. The [Akin Gump analysis](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/colorado-postpones-implementation-of-colorado-ai-act-sb-24-205) of this delay confirmed that the five-month extension was intended to give the 2026 regular legislative session time to consider substantive amendments.

### 2026 Legislative Session

Governor Polis convened an AI Policy Workgroup in October 2025 — before the 2026 regular session opened in January — to develop a potential legislative replacement for the original Act. The workgroup released a proposed "ADMT Framework" in March 2026. As of April 2026, the law's ultimate scope remains uncertain. Possible outcomes include: narrowing the definition of "high-risk AI system," reducing deployer obligations, expanding exemptions, or shifting liability more heavily toward developers. Any significant changes would need to be enacted and signed before the June 30, 2026 effective date to affect that compliance deadline.

## Impact Assessment [HIGH confidence]

### Affected Industries

The law's scope — focused on consequential decisions in employment, housing, healthcare, financial services, education, insurance, and legal services — captures a broad swath of the economy. [Venable LLP's analysis](https://www.venable.com/insights/publications/2024/05/colorados-landmark-ai-law-essential-insights) emphasizes that the law extends to any business *using* AI tools in these contexts, not merely AI vendors. A hospital using a vendor's AI triage system, a bank using an AI credit scoring model, or a staffing agency using an AI resume screener each falls within the deployer definition.

### Compliance Burden

The impact assessment requirement is the most operationally intensive obligation. Businesses must complete assessments before initial deployment, annually, and within 90 days of substantial modifications. For enterprises managing multiple AI systems across multiple business units, this creates significant ongoing administrative burden.

The consumer notice requirements will require businesses to redesign workflows at consequential-decision touchpoints, building disclosure mechanisms and appeal processes into existing systems.

### Developer vs. Deployer Tension

SB 24-205 creates a structural tension in AI vendor-customer relationships. Developers are required to provide documentation sufficient for deployer impact assessments, but developers may lack visibility into all the deployment contexts their tools are used in. Vendors and customers will need to negotiate documentation obligations in AI procurement contracts — a compliance coordination challenge that Venable's analysis flags as particularly important for enterprise AI deployments.

## Action Items

- Audit all AI systems currently deployed or under evaluation to determine whether any qualify as high-risk AI systems under the Colorado definition (consequential decisions about Colorado consumers).
- Identify whether your organization is a "developer," a "deployer," or both under the statute; a single business may qualify as both if it modifies and deploys AI systems.
- Assess applicability of the small-business exemption (fewer than 50 full-time employees) and confirm all three qualifying conditions can be satisfied.
- Review and update AI procurement contracts to include developer documentation obligations sufficient for deployer impact assessments.
- Begin preparing impact assessment templates aligned with the statute's requirements and NIST AI RMF; NIST compliance provides an affirmative defense.
- Implement (or evaluate) a risk management program for any high-risk AI system aligned with NIST AI RMF 1.0 or ISO/IEC 42001.
- Design consumer notice workflows and appeal processes for consequential-decision touchpoints.
- Monitor the 2026 Colorado legislative session closely — the law's substance may change materially before the June 30, 2026 effective date; compliance planning should be modular to accommodate possible amendments.
- Watch for Colorado Attorney General rulemaking guidance expected ahead of June 30, 2026.

## Related Reports

- [reports/ai-law/state-legislation/colorado-ai-act-sb205-2024.md](reports/ai-law/state-legislation/colorado-ai-act-sb205-2024.md) — Comprehensive statutory analysis of SB 24-205, the most detailed coverage of the law in this knowledge base.
- [reports/ai-law/state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md](reports/ai-law/state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md) — Covers the SB 25B-004 implementation delay to June 30, 2026 and the ongoing 2026 legislative uncertainty.
- [reports/ai-law/state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md](reports/ai-law/state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md) — Initial report on the bill's passage and Governor Polis's signing.
- [reports/ai-law/state-legislation/colorado-sb205-akin-gump-developer-deployer-2024-05-30.md](reports/ai-law/state-legislation/colorado-sb205-akin-gump-developer-deployer-2024-05-30.md) — Akin Gump's developer/deployer obligation analysis, covering the same dual-obligation framework.
- [reports/ai-law/state-legislation/utah-colorado-ai-pioneering-state-laws-2024-06-06.md](reports/ai-law/state-legislation/utah-colorado-ai-pioneering-state-laws-2024-06-06.md) — Places Colorado SB 24-205 in the context of the broader state AI law wave alongside Utah's AI disclosure act.

## Sources

1. [SB24-205 Consumer Protections for Artificial Intelligence — Colorado General Assembly](https://leg.colorado.gov/bills/sb24-205) — Official legislative page for SB 24-205, including bill history, sponsors, and links to enrolled and signed text.
2. [Colorado SB 24-205 Signed Text (PDF) — Colorado General Assembly](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf) — Official signed text of SB 24-205 as enacted, the primary statutory authority.
3. [Colorado's Landmark AI Law: Essential Insights for Businesses — Venable LLP](https://www.venable.com/insights/publications/2024/05/colorados-landmark-ai-law-essential-insights) — Law firm client alert providing the primary compliance-focused analysis underlying this report.
4. [SB25B-004 Increase Transparency for Algorithmic Systems — Colorado General Assembly](https://leg.colorado.gov/bills/sb25b-004) — Official legislative page for the 2025 special-session bill that delayed the effective date to June 30, 2026.
5. [Colorado Postpones Implementation of Colorado AI Act, SB 24-205 — Akin Gump](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/colorado-postpones-implementation-of-colorado-ai-act-sb-24-205) — Law firm analysis of SB 25B-004's effect on compliance timelines.
6. [Colorado AI Act Implementation Delayed — Baker Botts (September 2025)](https://www.bakerbotts.com/thought-leadership/publications/2025/september/colorado-ai-act-implementation-delayed) — Confirming the August 28, 2025 signing of SB 25B-004 and implementation of the June 30, 2026 effective date.
7. [Colorado Delays Comprehensive AI Law With Further Changes Anticipated — Greenberg Traurig](https://www.gtlaw.com/en/insights/2025/9/colorado-delays-comprehensive-ai-law-with-further-changes-anticipated) — Law firm analysis of the special session collapse and expected 2026 legislative activity.
8. [A Deep Dive into Colorado's Artificial Intelligence Act — National Association of Attorneys General](https://www.naag.org/attorney-general-journal/a-deep-dive-into-colorados-artificial-intelligence-act/) — In-depth NAAG analysis of the Act's structure, definitions, and enforcement mechanisms.
9. [Colorado Anti-Discrimination in AI Law (ADAI) Rulemaking — Colorado Attorney General](https://coag.gov/ai/) — Official Colorado AG page tracking rulemaking activity under SB 24-205.
10. [NIST AI Risk Management Framework — NIST](https://www.nist.gov/artificial-intelligence) — The NIST AI RMF that serves as an affirmative defense basis under SB 24-205.
11. [Colorado Consumer Protection Act (CRS Title 6, Article 1) — Justia](https://law.justia.com/codes/colorado/title-6/fair-trade-and-restraint-of-trade/article-1/) — Full text of the Colorado Consumer Protection Act, the pre-existing statute under which SB 24-205 violations are enforced as unfair trade practices.
