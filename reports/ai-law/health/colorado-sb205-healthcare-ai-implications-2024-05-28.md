---
title: "Colorado AI Act (SB 24-205): Healthcare Sector Compliance Guide"
date: 2024-05-28
jurisdiction: "Colorado"
category: "ai-law"
development_type: "legislation"
finding_id: "SCAN-20240528-027"
topic_key: "colorado-dcdba04f-2024"
topic_type: "state_bill"
first_reported: 2024-05-28
last_updated: 2026-04-15
status_history: []
cluster: "Colorado AI Act (SB 24-205): Enforcement and Amendments"
cluster_slug: "colorado-ai-act-sb-24-205-enforcement"
---

# Colorado AI Act (SB 24-205): Healthcare Sector Compliance Guide

**Jurisdiction:** Colorado | **Category:** AI Law | **Date:** May 28, 2024

> **Scope note:** This report focuses exclusively on healthcare-sector implications of Colorado SB 24-205, including the HIPAA, ONC/HTI-1, and FDA exemptions; clinical decision support boundaries; utilization review requirements under HB26-1139; and mental health AI regulations. For the primary statutory analysis of SB 24-205, see [reports/ai-law/state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md](../state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md).

## Executive Summary [HIGH confidence]

Colorado [Senate Bill 24-205](https://leg.colorado.gov/bills/sb24-205), signed into law on May 17, 2024, makes Colorado the first US state to enact comprehensive AI regulation — and explicitly identifies "health care services" as a high-risk application area subject to the law's consumer-protection framework. Healthcare organizations — hospitals, health systems, payers, digital health companies, and certified health IT vendors — are within the law's scope as both "deployers" and "developers" of high-risk AI systems unless a specific statutory exemption applies. Three distinct exemptions protect qualifying healthcare AI uses from the law's full obligations: a HIPAA-covered-entity exemption, an ONC/HTI-1 federal-standards exemption, and an FDA-authorized device exemption. Each exemption is narrow, conditional, and requires affirmative documentation. Entities that do not satisfy an exemption face the law's full developer or deployer obligations — including annual AI impact assessments, consumer disclosures, human-review rights, and 90-day incident reporting — before the law's effective date of June 30, 2026. A companion bill, [HB26-1139](https://leg.colorado.gov/bills/HB26-1139), currently advancing in the 2026 session, would layer additional AI-specific requirements on health insurance utilization review and mental health AI chatbots.

## Background [HIGH confidence]

### Why Healthcare AI Is Specifically Named

[SB 24-205](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf) defines a "high-risk artificial intelligence system" as any AI system that makes, or is a "substantial factor" in making, a **consequential decision**. The statute lists "health care services" as one of eight named consequential-decision categories — alongside employment, education, financial services, essential government services, housing, insurance, and legal services. Healthcare AI therefore triggers the full compliance framework whenever it functions as a substantial factor in decisions affecting a Colorado consumer's access to, cost of, or terms of health care services.

The statutory focus on healthcare AI reflects the legislature's recognition that AI diagnostic tools, clinical decision support systems, and prior authorization algorithms can directly affect patient health outcomes. As analyzed by [Mintz Levin](https://natlawreview.com/article/colorado-ai-systems-regulation-what-health-care-deployers-and-developers-need-know), health care stakeholders — hospitals, payers, and digital health companies — are among the most directly affected categories of deployer under the law.

### The Federal Context: AI in Healthcare Already Regulated

Healthcare AI operates within an existing federal regulatory ecosystem that SB 24-205 had to navigate carefully:

- **FDA oversight:** By May 2024, the FDA had authorized [882 AI/ML-enabled medical devices](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices), applying its established 510(k) and De Novo pathways to software that functions as a medical device.
- **ONC/HTI-1 Final Rule:** The Office of the National Coordinator for Health Information Technology's [HTI-1 Final Rule](https://www.healthit.gov/topic/laws-regulation-and-policy/health-data-technology-and-interoperability-certification-program) (published January 9, 2024; effective March 11, 2024 after Congressional Review Act correction) introduced algorithmic transparency requirements for certified health IT, including requirements for health IT developers to disclose predictive decision support interventions to providers and patients.
- **HIPAA:** The Health Insurance Portability and Accountability Act already imposes privacy, security, and breach notification requirements on covered entities and business associates, creating a compliance framework that overlaps with SB 24-205's data-governance obligations.

Colorado's legislature built exemptions keyed to each of these federal frameworks to avoid requiring healthcare organizations to comply with duplicative state obligations where equivalent federal oversight already exists — while ensuring that the most consequential, uncovered AI uses remain subject to state consumer protections.

## Detailed Analysis [HIGH confidence]

### Three Statutory Exemptions for Healthcare AI

#### 1. HIPAA Covered Entity Exemption

[SB 24-205 section 6-1-1706(2)(k)](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf) exempts deployers, developers, or others that are **covered entities under HIPAA** when providing AI-generated recommendations that satisfy all three of the following conditions:

1. The recommendation is **generated by an AI system**;
2. The recommendation **requires a health care provider to take action to implement** it; and
3. The recommendation is **not otherwise considered high-risk** under the Act.

The critical operative element is condition 2: the AI system must produce a recommendation, not an autonomous determination. If the system automatically executes a consequential health care decision — denying a claim, ordering a medication, restricting access — without requiring affirmative clinician action, the HIPAA exemption does not apply. As [Manatt, Phelps & Phillips](https://www.manatt.com/insights/newsletters/health-highlights/colorado-regulating-high-risk-ai-deployment-and-d) analyzed, administrative AI functions such as billing, appointment scheduling, and clinical documentation may qualify because they are not "high-risk" consequential decisions; but prior-authorization denial systems, autonomous treatment-selection tools, and coverage-determination algorithms must be evaluated under conditions 2 and 3 before reliance on the exemption.

**Not covered:** The HIPAA exemption does not protect AI systems used by health insurers for coverage determinations where those determinations constitute consequential decisions about a patient's access to health care services. Utilization management AI — a core focus of payer operations — requires separate analysis.

#### 2. ONC/HTI-1 Federal Standards Exemption

[SB 24-205 section 6-1-1706(2)(j)](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf) exempts deployers, developers, or others that deploy, develop, or modify a high-risk AI system **in compliance with standards established by a federal agency** where those federal standards are equivalent to or stricter than SB 24-205's requirements.

The most significant application is to the ONC HTI-1 Final Rule, which covers certified health IT developers and health care providers using certified EHR technology. As identified by [Mintz Levin](https://natlawreview.com/article/colorado-ai-systems-regulation-what-health-care-deployers-and-developers-need-know), health IT developers operating under ONC certification requirements — and health care providers using certified systems in compliance with HTI-1 — may qualify for this exemption. To invoke it, an organization must document: (a) the applicable federal standard; (b) that their AI system operates in compliance with that standard; and (c) that the federal standard's requirements are equivalent to or more rigorous than SB 24-205's transparency, impact-assessment, and consumer-disclosure obligations.

The ONC/HTI-1 exemption helps reduce compliance duplication for a large segment of the hospital and health system market, which by definition uses certified EHR technology to participate in Medicare and Medicaid.

#### 3. FDA-Authorized Device Exemption

[SB 24-205 section 6-1-1706(2)(i)](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf) exempts deployers and developers of AI systems that have been **approved, authorized, certified, cleared, or granted by a federal agency** — including the FDA. This exemption covers FDA-cleared or -authorized AI/ML-enabled medical devices, which by May 2024 numbered [882 devices](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices).

The exemption is scoped to the AI system as authorized: if a hospital deployer uses an FDA-cleared diagnostic AI system for a use consistent with its authorized indication, it is exempt. Using the same system for an off-label purpose that constitutes a consequential decision — for example, using a diagnostic imaging AI as the sole basis for an insurance coverage determination — may fall outside the exemption's scope and require SB 24-205 compliance analysis. Organizations should retain documentation of each system's FDA authorization status and confine use to authorized indications.

### The Non-Exempt Zone: Where Healthcare Organizations Are Fully Covered

The three exemptions leave significant areas of healthcare AI fully subject to SB 24-205. Organizations should presume coverage unless a specific exemption is documented:

**Prior authorization and utilization management AI:** AI systems used by health insurers or managed care organizations to make or substantially influence decisions to approve, deny, or delay coverage for health care services are paradigmatic "high-risk" systems making consequential decisions about a consumer's access to health care services. The HIPAA exemption does not apply unless a licensed clinician must affirmatively act to implement the AI's recommendation. Many automated prior authorization systems — which generate automatic denials without required clinician review — are unlikely to qualify.

**Population health management and risk stratification:** AI systems that identify high-risk patients for care management, flag patients for intervention, or exclude patients from outreach may make or substantially contribute to consequential decisions about the terms of health care services. Depending on design, these may not fall within the HIPAA exemption (they affect the terms of care access rather than merely providing a clinical recommendation).

**Revenue cycle management AI:** AI tools used in billing, coding, and revenue cycle management that can affect a patient's financial obligations for health care are potentially within scope.

**Hiring and staffing AI in healthcare:** Hospitals and health systems that use AI to screen clinician candidates, determine staffing assignments, or evaluate employee performance face the same employer-deployer obligations as any other Colorado employer.

### Deployer Obligations That Apply to Non-Exempt Healthcare AI [HIGH confidence]

Healthcare entities that cannot invoke an exemption must satisfy the deployer compliance framework:

1. **Risk management program:** Implement a formal AI risk management policy and program for each high-risk AI system, aligned with the [NIST AI Risk Management Framework](https://www.nist.gov/artificial-intelligence/ai-risk-management-framework), [ISO 42001](https://www.iso.org/standard/81230.html), or an equivalent framework.

2. **Pre-deployment and annual impact assessments:** Conduct impact assessments before deploying each high-risk AI system; repeat annually; and conduct a new assessment within 90 days of any intentional and substantial system modification. Assessments must cover the types of data processed, performance metrics on protected-class groups, known limitations, mitigation measures, and consumer transparency provisions.

3. **Consumer notice:** When a high-risk AI system makes or substantially influences a consequential health care decision affecting a Colorado consumer, the deployer must notify that consumer — in plain language, in the consumer's preferred language — explaining the decision and how to correct inaccurate personal data used in the decision.

4. **Human review and appeal:** Provide an opportunity for meaningful appeal of adverse consequential decisions and, where technically feasible, human review of the AI-influenced decision. As analyzed by [Foley & Lardner](https://natlawreview.com/article/colorado-ai-act-implications-health-care-providers), this requirement has particular significance for health care providers using AI in clinical decision support where patients receive adverse clinical recommendations.

5. **Website summary:** Publish on the deployer's website a clear summary of all high-risk AI systems deployed, including their types and purposes.

### Incident Reporting Obligations for Developers [HIGH confidence]

Healthcare AI **developers** — including health IT vendors and digital health companies selling AI products for use in consequential decisions — face a 90-day incident reporting obligation. Within 90 days of discovering or receiving a credible report that a high-risk AI system has caused or is reasonably likely to have caused algorithmic discrimination, the developer must:

- Notify the Colorado Attorney General; and
- Notify all known Colorado deployers of the system.

This obligation applies regardless of exemption status for the deployer — a health IT developer whose product is deployed by a HIPAA-covered entity that claims the HIPAA exemption still bears incident-reporting duties if the AI system itself does not qualify for an exemption. Organizations should audit whether their contracts with health IT vendors appropriately address this developer obligation and what notification workflows exist.

## HB26-1139: Healthcare-Specific AI Bill Advancing in 2026 [MEDIUM confidence]

A companion bill, [HB26-1139 "Use of Artificial Intelligence in Health Care"](https://leg.colorado.gov/bills/HB26-1139), passed the Colorado House on third reading (47-15) on March 16, 2026, and has been transmitted to the Senate. While SB 24-205 applies broadly to all high-risk AI sectors, HB26-1139 addresses healthcare AI specifically with requirements that both supplement and partially overlap with SB 24-205's framework.

**Utilization review and insurance coverage AI:** HB26-1139 would prohibit health insurers from using AI systems as the **sole basis** for denying coverage. Any denial or delay based even partly on medical necessity must be reviewed by a licensed clinician or physician competent to evaluate the specific clinical issues. Insurers deploying AI in utilization management must disclose to the relevant state division: (a) which utilization review functions use AI; (b) where in the review process AI is applied; (c) the human oversight process for adverse coverage determinations; and (d) audit information demonstrating AI use compliance.

**Mental health AI chatbots:** HB26-1139 would establish specific rules for AI systems used in psychotherapy:
- Prohibited from stating or implying they are a human mental health provider or authorized to practice psychotherapy;
- Required to implement crisis protocols for suicidal ideation or self-harm, including referral to a crisis hotline;
- Regulated professionals must disclose to clients when AI systems are used in their practice;
- Billing a public or private payer for psychotherapy services **conducted directly by an AI system** would be prohibited.

As reported by [Colorado Public Radio](https://www.cpr.org/2026/03/09/colorado-ai-health-care-guardrails-bills/), the bill passed the Colorado House floor (47-15) on March 16, 2026, and has been transmitted to the Senate. Final passage and interaction with the SB 24-205 replacement framework under development by the Governor's ADMT Working Group remains pending.

## Impact Assessment [MEDIUM confidence]

### Entities Most Affected

**Health insurers and managed care organizations** face the highest compliance exposure under SB 24-205 for their prior authorization and utilization management AI — systems that make consequential decisions about health care access that are unlikely to qualify for the HIPAA exemption. HB26-1139 would add explicit utilization review requirements on top.

**Hospitals and health systems** using AI for clinical decision support, care management, or patient risk stratification need to map each system against the three exemptions. Systems that fail the exemption tests require impact assessments, consumer disclosures, and human-review rights before June 30, 2026.

**Health IT developers and digital health companies** face developer obligations — documentation, incident reporting to the AG, and deployer notifications — for any AI products deployed in Colorado for consequential health care decisions. Vendor contracts should be reviewed and updated to address these obligations.

**Mental health providers and telehealth platforms** face specific exposure under HB26-1139's chatbot requirements, which are distinct from SB 24-205's framework and impose affirmative disclosure, crisis protocol, and billing restrictions.

### Key Compliance Deadlines

- **June 30, 2026:** SB 24-205 effective date for the existing law (delayed from February 1, 2026 by [SB 25B-004](https://leg.colorado.gov/bills/sb25b-004)).
- **2026 legislative session:** Ongoing deliberation on a replacement ADMT framework proposed by the Governor's AI Policy Working Group; if enacted, would take effect January 1, 2027. If this bill passes, the June 30, 2026 SB 24-205 effective date may be superseded.
- **HB26-1139:** Effective date pending final passage and governor signature.

### Enforcement

The Colorado Attorney General has exclusive enforcement authority. Violations are unfair or deceptive trade practices under the [Colorado Consumer Protection Act](https://coag.gov/resources/consumer-protection/), with civil penalties reaching $20,000 per violation. There is no private right of action. The [Colorado AG's AI rulemaking page](https://coag.gov/ai/) is the official hub for enforcement guidance development.

## Action Items

- **Audit all AI systems against the three exemptions:** For each AI system deployed or developed by the organization, document the basis for any exemption claim (HIPAA, ONC/HTI-1, or FDA authorization). Do not assume an exemption applies without affirmative documentation.
- **Map utilization management AI for HIPAA exemption eligibility:** Identify which prior authorization, coverage determination, and utilization review AI systems automatically execute decisions versus generate recommendations requiring licensed clinician action. Systems that auto-deny without required clinician review are likely non-exempt.
- **Prepare developer documentation packages now:** Health IT vendors selling AI products deployed in Colorado for high-risk health care decisions must compile and deliver to deployer customers: intended uses, known harmful uses, training data bias evaluation, and risk mitigation measures.
- **Establish 90-day incident reporting workflows:** Create internal processes for monitoring AI system performance for algorithmic discrimination. Ensure discovery triggers a 90-day clock for AG notification and deployer notification.
- **Draft impact assessments for non-exempt systems:** For systems not covered by an exemption, begin pre-deployment impact assessments now to document data types, performance metrics by protected class, limitations, and mitigation measures.
- **Implement consumer notice and appeal processes:** Design patient-facing notification workflows for adverse health care AI decisions, including how to correct inaccurate data and request human review.
- **Monitor HB26-1139:** Track this bill's progress in the 2026 Colorado Senate; if enacted, it imposes standalone requirements on utilization management AI and mental health chatbots independent of SB 24-205.
- **Track the ADMT replacement framework:** If the Governor's proposed replacement bill passes in the 2026 session, the core compliance obligations may shift and the compliance deadline may move to January 1, 2027.

## Related Reports

- [reports/ai-law/state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md](../state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md) — Primary comprehensive statutory analysis of SB 24-205: full developer-deployer framework, legislative history, all eight consequential-decision categories, and industry opposition.
- [reports/ai-law/state-legislation/colorado-sb205-ai-act-2024-05-29.md](../state-legislation/colorado-sb205-ai-act-2024-05-29.md) — Comparative analysis placing SB 24-205 alongside the EU AI Act; covers all exemptions including the HIPAA exemption at a high level.
- [reports/ai-law/state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md](../state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md) — Covers SB 25B-004 enforcement delay to June 30, 2026, HB26-1263 chatbot safety bill, and federal preemption pressure from the Trump administration.
- [reports/ai-law/frameworks-guidance/nist-ai-rmf-critical-infrastructure-profile-2026-04-13.md](../frameworks-guidance/nist-ai-rmf-critical-infrastructure-profile-2026-04-13.md) — NIST AI RMF guidance referenced in SB 24-205's deployer safe harbor; relevant for healthcare organizations structuring their risk management programs.
- [reports/ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md](../trump-ai-executive-order-state-preemption-2026-04-12.md) — Trump executive order targeting "onerous" state AI laws; Colorado's SB 24-205 is a primary target and federal preemption could affect the June 30, 2026 compliance deadline.

## Sources

1. [Colorado General Assembly — SB 24-205 Bill Page](https://leg.colorado.gov/bills/sb24-205) — Official bill page, sponsors, vote history, and current status
2. [Colorado SB 24-205 Signed Text (PDF)](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf) — Official enrolled statute text; primary authority for all statutory citations
3. [Mintz Levin — Colorado AI Systems Regulation: What Health Care Deployers and Developers Need to Know](https://natlawreview.com/article/colorado-ai-systems-regulation-what-health-care-deployers-and-developers-need-know) — Healthcare-specific analysis of exemptions, ONC/HTI-1 pathway, and deployer obligations; published June 27, 2024
4. [Manatt, Phelps & Phillips — CO Enacts "High-Risk" AI Law Regulating Deployers and Developers, Including Health Care Stakeholders](https://www.manatt.com/insights/newsletters/health-highlights/colorado-regulating-high-risk-ai-deployment-and-d) — Health Highlights analysis covering HIPAA exemption scope, payer exposure, and preparation steps
5. [Foley & Lardner — The Colorado AI Act: Implications for Health Care Providers](https://natlawreview.com/article/colorado-ai-act-implications-health-care-providers) — Healthcare provider-focused analysis covering human review requirements, algorithmic discrimination, and February 2025 updated guidance
6. [Colorado General Assembly — HB26-1139 Use of Artificial Intelligence in Health Care](https://leg.colorado.gov/bills/HB26-1139) — Official bill page for 2026 healthcare AI companion legislation covering utilization review and mental health AI
7. [Colorado Public Radio — Two proposals on artificial intelligence in the medical system advance at the statehouse](https://www.cpr.org/2026/03/09/colorado-ai-health-care-guardrails-bills/) — Coverage of HB26-1139 advancing through House committee in March 2026; bill subsequently passed full House 47-15 on March 16, 2026
8. [FDA — Artificial Intelligence and Machine Learning (AI/ML)-Enabled Medical Devices](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices) — Official FDA list of 882 authorized AI/ML medical devices; basis for FDA exemption analysis
9. [ONC — Health Data, Technology, and Interoperability (HTI-1) Final Rule](https://www.healthit.gov/topic/laws-regulation-and-policy/health-data-technology-and-interoperability-certification-program) — ONC's HTI-1 rule establishing algorithmic transparency requirements for certified health IT; published January 9, 2024; effective March 11, 2024 per Federal Register correction notice 2024-02519
10. [Colorado AG — AI Anti-Discrimination Rulemaking Page](https://coag.gov/ai/) — Official AG enforcement and rulemaking hub for SB 24-205
11. [Colorado General Assembly — SB 25B-004](https://leg.colorado.gov/bills/sb25b-004) — Special session bill delaying SB 24-205 effective date to June 30, 2026
12. [Epstein Becker Green / Health Law Advisor — Colorado's SB 24-205: Addressing AI Risk with Sweeping Consumer Protection Law](https://www.healthlawadvisor.com/colorado-sb-24-205-on-the-verge-of-addressing-ai-risk-with-sweeping-consumer-protection-law) — Healthcare sector overview of SB 24-205's consumer protection framework
