---
title: "FTC COPPA Rule Amendments (2025): Compliance Deadline April 22, 2026"
date: "2026-04-13"
jurisdiction: "Federal"
category: "privacy"
development_type: "regulation"
cluster: "FTC COPPA Rule Amendments (2025)"
cluster_slug: "ftc-coppa-2025-amendments"
first_reported: "2026-04-07"
last_updated: 2026-04-13
status_history:
  - date: "2026-04-07"
    status: "Initial report — compliance deadline imminent alert"
  - date: "2026-04-13"
    status: "Updated with expanded compliance checklist, risk outlook, and timeline"
---

# FTC COPPA Rule Amendments (2025): Compliance Deadline April 22, 2026

## Summary [HIGH confidence]

The FTC's amended Children's Online Privacy Protection Rule (16 CFR Part 312), finalized by a [unanimous 5-0 Commission vote on January 16, 2025](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-changes-childrens-privacy-rule-limiting-companies-ability-monetize-kids-data) and [published in the Federal Register on April 22, 2025](https://www.federalregister.gov/documents/2025/04/22/2025-05904/childrens-online-privacy-protection-rule), has a general compliance deadline of **April 22, 2026**. These are the most significant changes to COPPA in over a decade — COPPA's first major update since 2013 — expanding the definition of children's personal information to include biometric identifiers, requiring separate verifiable parental consent before disclosing children's data for advertising or AI model training, mandating a written information security program, and prohibiting indefinite data retention.

## Key Requirements [HIGH confidence]

### 1. Expanded Definition of "Personal Information"
16 CFR 312.2 is expanded to include:
- **Biometric identifiers** usable for automated or semi-automated recognition: fingerprints, voiceprints, retina/iris patterns, genetic data (including DNA sequences), gait patterns, facial templates, and faceprints.
- **Government-issued identifiers** beyond SSN — state ID and passport numbers.
- Phone numbers and certain geolocation data are also newly covered.

([Federal Register, 90 FR 20498](https://www.federalregister.gov/documents/2025/04/22/2025-05904/childrens-online-privacy-protection-rule))

### 2. Separate Verifiable Parental Consent for Third-Party Disclosures
Operators must obtain a **separate, specific opt-in verifiable parental consent (VPC)** before disclosing a child's personal information to third parties for any purpose not "integral" to the website or online service. This includes advertising partnerships and data-sharing arrangements. A blanket consent checkbox no longer suffices; marketing/disclosure consent cannot be bundled into a general consent to collection and use.

### 3. AI Training Classified as Never "Integral"
The FTC explicitly stated in the rule's commentary that disclosures of children's personal information to **train or develop AI technologies** are not integral to a website or online service and **always require separate verifiable parental consent**. Organizations using children's data for AI/ML purposes must implement consent gates or cease such use by the compliance deadline.

([Akin Gump analysis](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/new-coppa-obligations-for-ai-technologies-collecting-data-from-children); [Data Protection Report](https://www.dataprotectionreport.com/2025/06/ftcs-coppa-rule-changes-include-ai-training-consent-requirement/))

### 4. Written Information Security Program (WISP)
The amendments replace COPPA's prior general "reasonable security" obligation with a prescriptive requirement to establish, implement, and maintain a **written information security program** with safeguards appropriate to the sensitivity of the data and the operator's size. Operators must designate a program coordinator, perform annual risk assessments, implement safeguards, and obtain written assurances from service providers.

### 5. Data Retention Policy and Public Retention Schedule
Operators may retain children's personal information only **for as long as reasonably necessary** for the specific collection purpose. Requirements include:
- A written data retention policy with defined retention periods.
- **Public disclosure** of the retention schedule (business purpose, timeframe, deletion process) in the online notice.
- Indefinite retention is prohibited.

([Fenwick analysis](https://www.fenwick.com/insights/publications/what-the-amended-coppa-rule-means-for-data-retention-practices))

### 6. Narrowed "Support for Internal Operations" Exemption
Operators relying on the internal-operations exemption must now **publicly list the specific internal operations** for which persistent identifiers are used, and cannot use the data to contact individuals, build profiles, or serve targeted ads.

### 7. Ed-Tech: Codification Deferred
The FTC declined to codify its existing informal guidance permitting schools to authorize data collection on behalf of parents for ed-tech services, citing potential conflicts with anticipated FERPA regulation changes. Existing guidance remains in effect but has not been given regulatory force.

([Loeb & Loeb analysis](https://www.loeb.com/en/insights/publications/2025/05/childrens-online-privacy-in-2025-the-amended-coppa-rule))

### 8. Safe Harbor Program Transparency
FTC-approved Safe Harbor programs face heightened transparency and membership-disclosure obligations, with **earlier compliance deadlines** (90 days–6 months after publication).

## Enforcement and Penalties [MEDIUM confidence]

Courts can impose civil penalties up to **$53,088 per violation**, with factors including the egregiousness of violations, number of children affected, type of information collected, and company size. ([FTC COPPA FAQ](https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions))

The FTC has historically prioritized COPPA enforcement, with settlements against YouTube, TikTok, Epic Games, Amazon, and Microsoft ranging from tens to hundreds of millions of dollars. The new WISP and retention requirements provide concrete, documentable checkpoints that will streamline post-April 2026 enforcement. State attorneys general, who share COPPA enforcement authority, are also expected to act under the amended rule.

## Compliance Checklist [HIGH confidence]

Before **April 22, 2026**, operators of child-directed services (or general-audience services with actual knowledge of under-13 users) should:

- [ ] Update privacy notices for the expanded PI definition, public retention schedule, and internal-operations disclosures.
- [ ] Re-paper parental consent flows with a **separate, unbundled VPC** for third-party disclosures (especially targeted ads and data-sharing arrangements).
- [ ] **Cease or gate AI training on children's data** — implement separate consent gates or cease use by the compliance deadline.
- [ ] Adopt a WISP with designated coordinator, annual risk assessment, documented safeguards, and service-provider assurances.
- [ ] Adopt a written data retention policy and purge data no longer necessary.
- [ ] Inventory biometric and government-ID data flows; confirm VPC coverage.
- [ ] Review K-12 ed-tech arrangements against FTC's existing (non-codified) school-authorization guidance.
- [ ] Update vendor/service-provider agreements for written data-protection assurances and downstream-use restrictions.
- [ ] Train product, engineering, and marketing teams on new consent and disclosure rules.

## Timeline [HIGH confidence]

| Date | Event |
|------|-------|
| January 16, 2025 | FTC announces final COPPA Rule amendments (unanimous 5-0 vote) |
| April 22, 2025 | Final rule published in the Federal Register (90 FR 20498) |
| June 23, 2025 | Rule effective date |
| July–October 2025 | Safe Harbor program compliance deadlines |
| **April 22, 2026** | **General operator compliance deadline** |

## Sources

1. [FTC Press Release: FTC Finalizes Changes to Children's Privacy Rule](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-changes-childrens-privacy-rule-limiting-companies-ability-monetize-kids-data) — Official FTC announcement of the January 2025 unanimous vote finalizing COPPA amendments
2. [Federal Register: Children's Online Privacy Protection Rule (90 FR 20498)](https://www.federalregister.gov/documents/2025/04/22/2025-05904/childrens-online-privacy-protection-rule) — Official Federal Register publication of the final rule, April 22, 2025
3. [eCFR: 16 CFR Part 312](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-312) — Current text of the Children's Online Privacy Protection Rule as codified
4. [FTC — COPPA Rule landing page](https://www.ftc.gov/legal-library/browse/rules/childrens-online-privacy-protection-rule-coppa)
5. [FTC: Complying with COPPA FAQ](https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions) — Official FTC compliance guidance and penalty information
6. [Akin Gump: New COPPA Obligations for AI Technologies](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/new-coppa-obligations-for-ai-technologies-collecting-data-from-children) — Law firm analysis of AI-specific COPPA obligations
7. [Data Protection Report: FTC's COPPA Rule Changes Include AI Training Consent Requirement](https://www.dataprotectionreport.com/2025/06/ftcs-coppa-rule-changes-include-ai-training-consent-requirement/) — Norton Rose Fulbright analysis of AI training consent requirements
8. [White & Case: Unpacking the FTC's COPPA Amendments](https://www.whitecase.com/insight-alert/unpacking-ftcs-coppa-amendments-what-you-need-know) — Comprehensive law firm compliance guidance
9. [Mayer Brown: FTC Announces Significant Amendments to COPPA](https://www.mayerbrown.com/en/insights/publications/2025/04/ftc-announces-significant-amendments-to-coppa)
10. [Latham & Watkins: FTC Publishes Updates to COPPA Rule](https://www.lw.com/en/insights/ftc-publishes-updates-to-coppa-rule)
11. [Alston & Bird: FTC Publishes Amendments to COPPA Rule](https://www.alstonprivacy.com/ftc-publishes-amendments-to-coppa-rule/)
12. [Jones Day: FTC Finalizes Amendments to COPPA Rule](https://www.jonesday.com/en/insights/2025/05/ftc-finalizes-amendments-to-coppa--rule)
13. [Loeb & Loeb: Children's Online Privacy in 2025](https://www.loeb.com/en/insights/publications/2025/05/childrens-online-privacy-in-2025-the-amended-coppa-rule) — Law firm analysis including ed-tech implications
14. [Fenwick: What the Amended COPPA Rule Means for Data Retention](https://www.fenwick.com/insights/publications/what-the-amended-coppa-rule-means-for-data-retention-practices) — Law firm analysis of data retention requirements
15. [Davis Wright Tremaine: FTC Amends COPPA Rule](https://www.dwt.com/blogs/privacy--security-law-blog/2025/05/coppa-rule-ftc-amended-childrens-privacy)
16. [Hunton: FTC Publishes Final COPPA Rule Amendments](https://www.hunton.com/privacy-and-cybersecurity-law-blog/ftc-publishes-final-coppa-rule-amendments)
17. [Securiti: FTC's 2025 COPPA Final Rule Amendments](https://securiti.ai/ftc-coppa-final-rule-amendments/)
