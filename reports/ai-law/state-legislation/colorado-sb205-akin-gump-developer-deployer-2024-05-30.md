---
title: "Colorado SB 205: Akin Gump Analysis of the Developer/Deployer Obligation Framework"
date: 2024-05-30
jurisdiction: "Colorado"
category: "ai-law"
development_type: "legislation"
finding_id: "SCAN-20240530-011"
topic_key: "colorado-03c99124-2024"
topic_type: "state_bill"
first_reported: 2024-05-30
last_updated: 2024-05-30
status_history: []
cluster: "Colorado AI Act (SB 24-205): Enforcement and Amendments"
cluster_slug: "colorado-ai-act-sb-24-205-enforcement"
---

# Colorado SB 205: Akin Gump Analysis of the Developer/Deployer Obligation Framework

**Jurisdiction:** Colorado | **Category:** AI Law | **Date:** May 30, 2024

> **Note:** This report covers Colorado SB 24-205 from the perspective of Akin Gump Strauss Hauer & Feld LLP's "Colorado Passes New Watershed AI Consumer Protection Bill" client alert (May 2024). It is a focused companion to the comprehensive enactment analysis at [reports/ai-law/state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md](reports/ai-law/state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md). This memo emphasizes the distinctive analytical angles in Akin Gump's treatment: the "intentional and substantial modification" trigger for developer status, the broad "deploy = use" definition, the supply chain liability structure, and the GDPR-era state privacy law analogy as a predictor of regulatory spread.

## Executive Summary [HIGH confidence]

Colorado Governor Jared Polis signed [Senate Bill 24-205](https://leg.colorado.gov/bills/sb24-205) on May 17, 2024, creating the first comprehensive state AI regulatory framework in the United States. Akin Gump characterizes the law as a potential "watershed" moment — drawing an explicit analogy to the GDPR's catalytic effect on US state privacy legislation — and focuses its analysis on the dual-obligation structure imposed on **developers** and **deployers** of high-risk AI systems. Three definitional features of the law's scope are particularly significant in Akin Gump's reading: (1) a person who "intentionally and substantially modifies" a third-party AI system qualifies as a developer, capturing fine-tuning and customization activity; (2) the definition of "deploy" means "use," so any company using a high-risk AI system — not just those that built or resell it — is a deployer subject to compliance; and (3) the law's consequential-decision framework creates a shared liability chain between developers and deployers in which a developer's documentation failures flow directly into deployer liability exposure. Enforcement rests exclusively with the Colorado Attorney General under the Colorado Consumer Protection Act; civil penalties may reach $20,000 per violation. The effective date has since been extended to June 30, 2026, after a failed 2025 special session.

## Background [HIGH confidence]

### The GDPR Precedent and Predicted Regulatory Spread

Akin Gump's framing of SB 24-205 as a "watershed" development is analytically important: it echoes the firm's prior coverage of the GDPR's effect on US state privacy legislation — where California's CCPA in 2018 triggered a multi-state legislative wave that by 2024 had produced comprehensive privacy laws in more than nineteen states. The GDPR/privacy law analogy predicts that Colorado's AI Act, if it survives legal challenge, will similarly catalyze comprehensive AI legislation across additional states, particularly in jurisdictions that have already modeled privacy legislation on California's framework.

This framing was borne out in subsequent legislative activity: following Colorado's enactment of SB 24-205, [Connecticut](https://www.cga.ct.gov/), [Georgia, and Illinois introduced companion AI bills](https://www.naag.org/attorney-general-journal/a-deep-dive-into-colorados-artificial-intelligence-act/) modeled on the developer-deployer framework. While none of those bills were enacted in 2024, the legislative pattern mirrored what occurred in the years following California's CCPA.

### Federal Vacuum

At the time of enactment, Congress had not passed comprehensive AI legislation. Federal activity consisted of voluntary guidance — the [NIST AI Risk Management Framework (AI RMF 1.0)](https://www.nist.gov/artificial-intelligence/executive-order-safe-secure-and-trustworthy-artificial-intelligence), published January 2023 — and the Biden administration's [October 2023 AI Executive Order](https://www.federalregister.gov/documents/2023/11/01/2023-24283/safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence), which directed agency action but imposed no private-sector mandates. The absence of binding federal AI law left a regulatory vacuum that Colorado, following a multi-state legislative working group coordinated through the Future of Privacy Forum, moved to fill.

### Legislative History

Senator Robert Rodriguez introduced [SB 24-205](https://leg.colorado.gov/bills/sb24-205) on April 10, 2024. The Senate passed it on May 3, 2024; the House on May 8, 2024. Governor Polis signed on May 17, 2024 — the same month the European Parliament gave its final vote to the [EU AI Act](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689), which formally entered into force in August 2024. The [official enrolled text](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf) is available from the Colorado General Assembly.

## Detailed Analysis [HIGH confidence]

### Core Framework: Duty of Reasonable Care on Both Ends of the AI Supply Chain

SB 24-205's central mechanism is a **duty of reasonable care** imposed separately on developers and deployers of high-risk AI systems to protect Colorado consumers from algorithmic discrimination. Akin Gump characterizes this as a "supply chain" obligation: the law simultaneously regulates AI model builders (developers) and the enterprises that use those models in decision-making (deployers), creating interlocking compliance obligations that travel along the AI vendor-customer relationship.

The [official statute](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf) defines:

- **High-risk AI system:** A system that makes, or is a "substantial factor" in making, a **consequential decision** — one with a material legal or similarly significant effect on a consumer's access to, cost of, or terms of employment, education, financial services, essential government services, health care, housing, insurance, or legal services.
- **Algorithmic discrimination:** Any condition in which an AI system results in unlawful differential treatment or impact that disfavors an individual or group based on race, color, ethnicity, sex, religion, age, national origin, limited English proficiency, disability, veteran status, genetic information, or reproductive health.

### The Developer Definition: "Intentionally and Substantially Modifies" [HIGH confidence]

A feature that Akin Gump highlights as analytically significant is the breadth of the **developer** definition. Under the statute, a developer is not limited to the entity that originally trains or builds an AI system. Rather, the definition covers any person doing business in Colorado who **develops or intentionally and substantially modifies** a high-risk AI system that is commercially available.

This means:
- A company that fine-tunes a foundation model (e.g., adapts a general-purpose LLM for a specific employment screening use case) may qualify as a developer, even if the underlying model was built by a third party.
- A company that retrains a vendor-supplied AI tool using its own proprietary data may qualify as a developer.
- Customization at the prompt level or through RLHF (reinforcement learning from human feedback) could, depending on the scope, trigger developer status.

Critically, changes resulting from AI **self-learning after deployment** are excluded from the definition of intentional and substantial modification — but only if those changes were predetermined in the initial impact assessment and properly documented. This carve-out places a compliance premium on thorough pre-deployment documentation: deployers who fail to document anticipated model drift lose the self-learning exclusion.

### The Deployer Definition: "Deploy" Means "Use" [HIGH confidence]

Equally significant in Akin Gump's analysis is the deployer definition. The statute defines "deploy" as **"use"** — and accordingly, a deployer is any person doing business in Colorado who **uses** a high-risk AI system in a product or service to make or substantially factor into consequential decisions about Colorado consumers. This is a notably broad reading:

- A company that purchases an AI hiring tool from a vendor and uses it to screen job applicants is a deployer.
- A hospital that subscribes to an AI diagnostic platform is a deployer.
- A bank that licenses a credit-scoring model from a fintech vendor is a deployer.
- Any enterprise that integrates a third-party AI API into a decision workflow affecting the enumerated consequential-decision categories is a deployer.

The practical implication, as Akin Gump notes, is that the compliance burden falls on **all enterprises that use AI in consequential decisions** — not only those that build or commercialize AI systems. This significantly broadens the regulated universe beyond what a casual reader of "AI developer regulation" might expect.

### Developer Obligations [HIGH confidence]

Under the [signed statute](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf), developers must:

1. **Supply deployer documentation:** Provide deployers with a statement describing the AI system's intended uses, known harmful or inappropriate uses, how training data was evaluated for bias, and what risk mitigation measures were taken.
2. **Maintain a public disclosure:** Publish a publicly accessible statement summarizing the types of high-risk AI systems they have developed or made commercially available and how they manage foreseeable algorithmic discrimination risks.
3. **Incident notification:** Within 90 days of discovering or receiving a credible report that a system has caused or is reasonably likely to have caused algorithmic discrimination, notify the Colorado Attorney General and all known Colorado deployers.

### Deployer Obligations and the Rebuttable Presumption [HIGH confidence]

Deployers obtain a **rebuttable presumption of reasonable care** — the statute's central compliance safe harbor — if they satisfy all of the following:

1. **Risk management policy:** Implement a written risk management policy and program for each high-risk AI system, incorporating the [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence/executive-order-safe-secure-and-trustworthy-artificial-intelligence), [ISO 42001](https://www.iso.org/standard/81230.html), or a substantially equivalent framework.
2. **Impact assessments:** Conduct documented impact assessments (a) prior to deployment, (b) annually thereafter, and (c) within 90 days of any intentional and substantial modification. Assessments must cover the types of data processed, performance metrics across demographic groups, known limitations, and transparency measures.
3. **Annual deployment review:** Review each deployed high-risk AI system annually to confirm it is not causing algorithmic discrimination.
4. **Consumer notice:** When a high-risk AI system makes or substantially influences a consequential decision affecting a specific consumer, notify that consumer in plain language (in the consumer's language, in accessible formats), explain the decision, and describe how the consumer may correct inaccurate data.
5. **Human review and appeal:** Provide consumers a meaningful opportunity to appeal adverse consequential decisions and, where technically feasible, to obtain human review of the AI-influenced outcome.
6. **Website summary:** Publish a summary of all high-risk AI systems deployed by the entity.

A separate **voluntary safe harbor** protects organizations that discover violations through their own internal review and remediate before any complaint is filed with the Attorney General.

### Supply Chain Liability Dynamics [HIGH confidence]

Akin Gump's analysis emphasizes the operational interdependency created by the dual-obligation structure. Because deployers depend on developer documentation to conduct their own impact assessments and satisfy the rebuttable presumption, a developer's failure to supply adequate documentation — or to disclose known discrimination risks — flows downstream into deployer compliance failures. Key dynamics include:

- **Documentation dependency:** A deployer cannot complete a compliant impact assessment without the developer-supplied information about training data bias evaluation and risk mitigation. If the developer's documentation is inadequate, the deployer's presumption of reasonable care is undermined regardless of the deployer's own efforts.
- **Incident reporting cascade:** When a developer discovers or receives notice of algorithmic discrimination within 90 days, they must notify all known deployers. This notification triggers deployer obligations: the deployer must in turn investigate, remediate, and may need to notify affected consumers.
- **Vendor contract implications:** Enterprise customers (deployers) should seek contractual representations from AI vendors (developers) regarding documentation completeness, bias evaluation methodology, and timely incident notification. The statute creates legal exposure that flows from developer non-compliance to deployer liability.

### EU AI Act Comparison [MEDIUM confidence]

Akin Gump situates Colorado's approach alongside the EU AI Act framework, noting shared architecture but fundamental differences in regulatory philosophy:

| Feature | Colorado SB 24-205 | EU AI Act |
|---|---|---|
| High-risk definition | Consequential decision outcomes (enumerated categories) | Tiered classification by use case + technical characteristics |
| Compliance standard | Reasonable care + framework-based safe harbor | Prescriptive conformity assessment + CE-marking equivalent |
| Prohibited AI uses | None | Yes (unacceptable-risk category) |
| Enforcement | State AG exclusive; no private right of action | National competent authorities + EU AI Office; member states set penalties |
| Pre-market authorization | None | Required for highest-risk categories |
| Small-business relief | Conditional exemption for deployers <50 employees | Proportionality principle; no blanket exemption |

Colorado's "reasonable care" standard is distinctly American: it creates negligence-style liability rooted in outcomes rather than the EU Act's prescriptive product-safety model. Companies subject to both regimes — EU-based AI developers selling to US enterprise customers in Colorado, or Colorado developers whose products serve EU users — face a dual compliance challenge with non-overlapping documentation formats and different enforcement architectures.

### Exemptions [HIGH confidence]

Several categories are partially or fully exempt from SB 24-205's high-risk AI requirements:

- **Federally regulated AI:** Systems approved or cleared by the FDA, FAA, or Federal Housing Finance Agency; systems deployed under contracts with the Department of Commerce, Department of Defense, or NASA (unless affecting employment or housing).
- **Financial institutions:** Banks, credit unions, and their affiliates subject to AI examination by a state or federal prudential regulator under published guidance meeting the statutory criteria.
- **Insurers:** Insurance companies and AI developers for insurers operating under Colorado's algorithmic-insurance statutes.
- **HIPAA-covered entities:** Certain health care entities compliant with qualifying HHS AI guidance.
- **Small-business deployers:** Deployers with fewer than 50 full-time employees who (a) do not train the AI system using their own data, (b) limit use to uses disclosed by the developer, and (c) provide consumers access to the developer's impact assessment.

### Enforcement [HIGH confidence]

The Colorado Attorney General has **exclusive** enforcement authority; there is no private right of action. Under the [Colorado Consumer Protection Act](https://coag.gov/resources/consumer-protection/), violations constitute unfair or deceptive trade practices, subject to civil penalties of up to **$20,000 per violation**. The AG may also pursue injunctive relief and restitution. The [Colorado AG's official AI rulemaking page](https://coag.gov/ai/) is the hub for enforcement guidance.

Akin Gump tracks Colorado's AI Act through its [AI Law and Regulation Tracker](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/Colorado-Governor-Signs-Senate-Bill-205-Into-Law,-Adopting-a-Risk-based-Approach-to-Algorithmic-Consumer-Discrimination), which logged the signing event as "Adopting a Risk-based Approach to Algorithmic Consumer Discrimination" — framing consistent with the firm's characterization of the law as primarily a consumer discrimination measure, not a general AI safety statute.

### Post-Enactment Status [HIGH confidence]

The law's original effective date of February 1, 2026 was delayed to **June 30, 2026** by [SB 25B-004](https://leg.colorado.gov/bills/sb25b-004), signed by Governor Polis on August 28, 2025, following a failed special legislative session. As of April 2026, a proposed ADMT (Automated Decision-Making Technology) replacement framework reached unanimous consensus in Governor Polis's AI Policy Working Group; a repeal-and-replace bill targeting a January 1, 2027 effective date is expected in the 2026 legislative session. If the replacement bill is enacted before June 30, 2026, SB 24-205 may be superseded before it takes effect. See [Colorado AI Act Enforcement Delayed to June 30, 2026](reports/ai-law/state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md) for full details.

## Impact Assessment [MEDIUM confidence]

### Who Qualifies as a Deployer (Broader than Expected)

The "deploy = use" definition creates a compliance obligation for virtually any enterprise that integrates AI into the enumerated consequential-decision categories. Companies that assume they are not "AI companies" — because they license third-party AI tools rather than build them — are deployers and bear the full suite of risk management, impact assessment, consumer notice, and human review obligations.

### The Fine-Tuner Problem

Companies that customize foundation models — a common enterprise practice — face uncertainty about whether their customization activity crosses the "intentional and substantial modification" threshold that would make them developers rather than (or in addition to) deployers. If classified as developers, they bear the additional burdens of deployer documentation supply, public disclosure maintenance, and 90-day incident reporting to the AG. Organizations engaged in prompt engineering, fine-tuning, or RLHF adaptation of third-party AI models should seek legal counsel on whether their activity triggers developer status under the statute.

### Vendor Contract Restructuring

Given the documentation dependency between developers and deployers, enterprise procurement contracts for AI tools should be updated to require vendors to:
- Supply compliant developer documentation at the time of deployment and following any intentional and substantial modification.
- Notify the customer (as a Colorado deployer) within 90 days of any discovered or reported algorithmic discrimination.
- Represent that training data was evaluated for bias and that risk mitigation measures were applied.
- Provide access to impact assessment materials needed for the deployer's own annual compliance review.

### Patchwork Risk

The GDPR analogy cuts both ways: GDPR triggered state privacy laws that are substantially harmonized in structure but diverge in specific requirements. If Colorado's developer-deployer framework spreads to additional states — with jurisdiction-specific definitional variations — companies selling AI tools into multiple state markets will face a compliance matrix analogous to the multi-state privacy law landscape. Proactive compliance investment in documentation, impact assessment processes, and vendor management infrastructure now reduces that future compliance burden.

## Action Items

- **Assess developer status for AI fine-tuners:** Any organization that customizes, fine-tunes, or substantially modifies third-party AI systems for consequential-decision use cases in Colorado should conduct a legal analysis of whether they qualify as developers under SB 24-205, given the "intentionally and substantially modifies" definition.
- **Audit all AI tool usage for deployer status:** Do not limit analysis to in-house AI development. Any AI tool used (deployed = used) in employment, lending, healthcare, education, housing, insurance, or legal services decisions affecting Colorado consumers triggers deployer obligations.
- **Restructure AI vendor contracts:** Add representations and warranties from AI vendors covering: documentation supply obligations, training data bias evaluation, 90-day incident notification, and indemnification for documentation failures that cause deployer liability.
- **Implement NIST AI RMF or ISO 42001 governance:** Deployers that want to qualify for the rebuttable presumption of reasonable care must adopt a recognized risk management framework. Building this infrastructure now serves Colorado compliance and is likely to satisfy analogous requirements in future state AI laws.
- **Document self-learning exclusion:** Deployers whose AI systems update post-deployment through learning must document anticipated model behavior changes in their initial impact assessments to preserve the self-learning exclusion from the "intentional and substantial modification" definition.
- **Monitor the 2026 legislative session:** A repeal-and-replace ADMT bill is expected; if enacted, it would supersede SB 24-205 with a January 1, 2027 effective date and potentially different developer/deployer definitions.
- **Track federal preemption:** The Trump administration's December 2025 executive order signals a potential DOJ challenge to state AI laws; monitor Commerce Department guidance and any resulting litigation that could affect Colorado enforcement before June 30, 2026.

## Related Reports

- [reports/ai-law/state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md](reports/ai-law/state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md) — Comprehensive primary analysis of SB 24-205 enactment: full statutory text analysis, legislative history, industry opposition, and exemptions in depth.
- [reports/ai-law/state-legislation/colorado-sb205-ai-act-2024-05-20.md](reports/ai-law/state-legislation/colorado-sb205-ai-act-2024-05-20.md) — Holland & Knight analysis perspective, focusing on the general AI labeling requirement applicable to all consumer-facing AI deployments beyond the high-risk framework.
- [reports/ai-law/state-legislation/colorado-sb205-ai-act-2024-05-29.md](reports/ai-law/state-legislation/colorado-sb205-ai-act-2024-05-29.md) — Herzog Fox & Neeman analysis placing Colorado SB 24-205 in direct comparative context with the EU AI Act using a side-by-side framework.
- [reports/ai-law/employment-ai/colorado-sb205-spb-employer-liability-2024-05-30.md](reports/ai-law/employment-ai/colorado-sb205-spb-employer-liability-2024-05-30.md) — Squire Patton Boggs analysis of employer liability and algorithmic discrimination in employment AI under SB 24-205.
- [reports/ai-law/state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md](reports/ai-law/state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md) — Covers SB 25B-004 enforcement delay to June 30, 2026, the failed 2025 special session, and the proposed ADMT replacement framework.
- [reports/ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md](reports/ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md) — Trump December 2025 executive order targeting "onerous" state AI laws; Colorado's SB 24-205 is a primary named target.
- [reports/ai-law/frameworks-guidance/nist-ai-rmf-critical-infrastructure-profile-2026-04-13.md](reports/ai-law/frameworks-guidance/nist-ai-rmf-critical-infrastructure-profile-2026-04-13.md) — NIST AI RMF guidance; SB 24-205 deployer safe harbor references NIST AI RMF compliance as the primary recognized framework.

## Sources

1. [Akin Gump — Colorado Passes New Watershed AI Consumer Protection Bill](https://www.akingump.com/en/insights/alerts/colorado-passes-new-watershed-ai-consumer-protection-bill) — Primary source; Akin Gump's client alert characterizing the law as a watershed event analogous to GDPR's effect on US privacy law
2. [Akin Gump — Colorado Enacts Groundbreaking AI Consumer Protection Legislation (AG Data Dive Blog)](https://www.akingump.com/en/insights/blogs/ag-data-dive/colorado-enacts-groundbreaking-ai-consumer-protection-legislation) — Akin Gump blog post with additional compliance analysis and practical implications
3. [Akin Gump AI Law and Regulation Tracker — Colorado Governor Signs SB 205](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/Colorado-Governor-Signs-Senate-Bill-205-Into-Law,-Adopting-a-Risk-based-Approach-to-Algorithmic-Consumer-Discrimination) — Akin Gump's regulatory tracker entry documenting signing event and risk-based framework characterization
4. [Lexology — Colorado Passes New Watershed AI Consumer Protection Bill (Akin Gump)](https://www.lexology.com/library/detail.aspx?g=59474bda-a3b6-45d1-8f1e-6a09db7654cd) — Lexology republication of the Akin Gump client alert (original finding source)
5. [JD Supra — Colorado Passes New Watershed AI Consumer Protection Bill (Akin Gump)](https://www.jdsupra.com/legalnews/colorado-passes-new-watershed-ai-9571309/) — JD Supra republication of the Akin Gump client alert with full text
6. [Colorado General Assembly — SB 24-205 Bill Page](https://leg.colorado.gov/bills/sb24-205) — Official bill page with full text, legislative history, sponsors, and votes
7. [Colorado SB 24-205 Signed Text (PDF)](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf) — Official enrolled and signed statute text; primary source for statutory definitions and obligations
8. [EU AI Act — Official Text (EUR-Lex)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) — Official EU AI Act text used for developer/deployer framework comparison
9. [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence/executive-order-safe-secure-and-trustworthy-artificial-intelligence) — NIST AI RMF referenced in SB 24-205 as the primary recognized framework for deployer reasonable care presumption
10. [National Association of Attorneys General — A Deep Dive into Colorado's Artificial Intelligence Act](https://www.naag.org/attorney-general-journal/a-deep-dive-into-colorados-artificial-intelligence-act/) — Independent statutory analysis covering exemptions, legislative history, and multi-state influence
11. [Colorado Attorney General — AI Enforcement and Rulemaking Page](https://coag.gov/ai/) — Official AG rulemaking hub; enforcement authority and guidance for SB 24-205
12. [Akin Gump — Colorado Postpones Implementation of Colorado AI Act, SB 24-205](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/colorado-postpones-implementation-of-colorado-ai-act-sb-24-205) — Akin Gump tracker entry on SB 25B-004 enforcement delay to June 30, 2026
