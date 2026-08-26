---
title: "Minnesota Consumer Data Privacy Act (MCDPA): White & Case Analysis of Key Provisions"
date: 2024-06-06
jurisdiction: "Minnesota"
category: "privacy"
development_type: "legislation"
finding_id: "SCAN-20240606-002"
topic_key: "minnesota-d802386e-2024"
topic_type: "state_bill"
first_reported: 2024-06-06
last_updated: 2026-04-21
status_history:
  - "2026-04-21: Corrected geolocation definition to MCDPA's three-decimal-degree standard (~360 ft); corrected two instances of §325M.17 to §325M.16 (data inventory section); added July 31, 2026 threshold reduction (100,000 → 35,000 consumers) to applicability section."
cluster: "Minnesota Consumer Data Privacy Act (MCDPA / HF 4757)"
cluster_slug: "minnesota-mcdpa-hf4757-comprehensive-privacy"
---

# Minnesota Consumer Data Privacy Act (MCDPA): White & Case Analysis of Key Provisions

**Jurisdiction:** Minnesota | **Category:** Privacy | **Date:** 2024-06-06

## Executive Summary [HIGH confidence]

On May 24, 2024, Minnesota Governor Tim Walz signed [HF 4757](https://www.revisor.mn.gov/bills/bill.php?b=House&f=HF4757&y=2024&ssn=0) into law, enacting the Minnesota Consumer Data Privacy Act (MCDPA), codified at [Minnesota Statutes, chapter 325M, sections 325M.10 through 325M.21](https://www.revisor.mn.gov/statutes/cite/325M). Minnesota became one of the latest states to adopt comprehensive consumer data privacy legislation, with the law taking effect on July 31, 2025. The MCDPA broadly follows the Virginia-model framework but introduces distinctive provisions, including the first-in-the-nation mandatory data inventory requirement, an expanded consumer right to challenge profiling decisions, a right to obtain a list of specific third-party data recipients, and a mechanism allowing consumers to designate authorized agents via browser settings. Enforcement rests exclusively with the Minnesota Attorney General, who may seek civil penalties of up to $7,500 per violation. Note: A more comprehensive analysis of this same legislation appears in this knowledge base — see the Related Reports section.

## Background [HIGH confidence]

Minnesota joined a growing number of states enacting comprehensive data privacy legislation after Congress failed to pass federal privacy legislation in the form of the [American Data Privacy and Protection Act (ADPPA)](https://www.congress.gov/bill/117th-congress/house-bill/8152). As of mid-2024, nineteen states had enacted such laws, with Minnesota's MCDPA often described as the nation's 18th or 19th, depending on counting methodology.

The MCDPA was introduced as part of the broader HF 4757 omnibus bill during the 93rd Minnesota Legislative Session (2023–2024). The legislature passed it on May 19, 2024, and Governor Walz signed it into law five days later on May 24, 2024. The law takes effect on July 31, 2025 — a deliberate delay intended to allow businesses time to achieve compliance. Postsecondary institutions regulated by the Minnesota Office of Higher Education receive an extended compliance deadline of July 31, 2029.

The MCDPA builds on the Virginia Consumer Data Protection Act (VCDPA) framework but incorporates consumer-friendly elements drawn from Oregon's and Connecticut's privacy statutes, creating a statute that compliance professionals have characterized as among the stronger state data privacy laws enacted to date.

## Detailed Analysis [HIGH confidence]

### Applicability Thresholds

The MCDPA applies to entities operating in Minnesota or that target Minnesota residents with goods or services, and that during a calendar year either:

1. Control or process the personal data of at least **100,000 Minnesota consumers** (excluding data processed solely to complete a payment transaction), or
2. Derive more than **25% of gross revenue from the sale of personal data** and process the personal data of at least **25,000 Minnesota consumers**.

**Note:** Effective July 31, 2026, the first threshold decreases from 100,000 to **35,000 Minnesota consumers**, significantly expanding the law's reach to businesses that were previously below the initial threshold. The second threshold (25,000 consumers + 25% revenue from data sales) is not affected by this reduction.

The law exempts small businesses as defined by [U.S. Small Business Administration size standards](https://www.sba.gov/document/support-table-size-standards), making Minnesota (along with Texas and Nebraska) one of the few states to carve out SBA-defined small businesses. However, the small-business exemption does not extend to the sale of sensitive data: even exempt small businesses may not sell a consumer's sensitive data without prior consent.

### Entity and Data Exemptions

The MCDPA follows a data-level (rather than entity-level) exemption model for several regulated sectors. Exempt data categories include:

- Data governed by [HIPAA](https://www.hhs.gov/hipaa/index.html) and the [HITECH Act](https://www.hhs.gov/hipaa/for-professionals/special-topics/hitech-act-enforcement-interim-final-rule/index.html)
- Financial data subject to the [Gramm-Leach-Bliley Act (GLBA)](https://www.ftc.gov/business-guidance/privacy-security/gramm-leach-bliley-act)
- Consumer credit data subject to the [Fair Credit Reporting Act (FCRA)](https://www.ftc.gov/legal-library/browse/statutes/fair-credit-reporting-act)
- Educational data covered by [FERPA](https://www2.ed.gov/policy/gen/guid/fpco/ferpa/index.html)
- Children's data governed by [COPPA](https://www.ftc.gov/legal-library/browse/statutes/childrens-online-privacy-protection-rule-coppa)
- Nonprofit organizations established to detect and prevent insurance fraud receive a narrow entity-level exemption

Critically, entities subject to HIPAA or GLBA are not fully exempt at the entity level — only the specific data classes regulated by those statutes are carved out. An organization's other personal data processing activities remain subject to the MCDPA.

### Consumer Rights

The MCDPA grants Minnesota consumers the following rights:

- **Right to access**: Consumers may confirm whether a controller is processing their personal data and obtain a copy of that data.
- **Right to correct**: Consumers may request correction of inaccurate personal data.
- **Right to delete**: Consumers may request deletion of personal data the controller has collected about them.
- **Right to data portability**: Consumers may request their personal data in a portable, readily usable format.
- **Right to opt out**: Consumers may opt out of (a) targeted advertising, (b) the sale of personal data, and (c) profiling that produces significant legal or similarly significant effects.
- **Right to list of specific third parties**: Following the Oregon OCPA model, the MCDPA grants consumers a right to request a list of specific third parties to whom the controller has disclosed or sold their personal data — not merely categories of third parties.
- **Right to question profiling decisions**: Consumers may challenge automated profiling decisions and receive an explanation of the reason for the decision, the data used, and actions the consumer may take to obtain a different outcome.

### Controller Obligations

Controllers must provide consumers with a privacy notice disclosing categories of personal data processed, purposes of processing, retention periods, and a description of consumer rights. Material changes to the privacy policy require electronic notification with a meaningful opportunity for consumers to withdraw consent to materially different processing.

**Data Privacy and Protection Assessments (DPIAs)** are required before processing data for targeted advertising, profiling with significant effects, selling personal data, or processing sensitive data.

**Data inventory** (first-in-the-nation requirement): Under [Minn. Stat. § 325M.16](https://www.revisor.mn.gov/statutes/cite/325M.16), controllers must maintain an inventory of personal data as part of their data security program — an explicit obligation found in no prior US state comprehensive privacy law.

**Policy documentation**: Uniquely, the MCDPA requires controllers to maintain written documentation of the policies and procedures adopted to comply with the statute, including the name and contact information for the individual responsible for those policies.

**Authorized agents via browser settings**: Consumers may designate an authorized agent to exercise opt-out rights on their behalf via an internet link, browser setting, browser extension, or global device setting. This explicitly validates universal opt-out mechanisms (UOOMs) and extends beyond the approach taken in most other Virginia-model laws.

### Sensitive Data

The MCDPA defines sensitive data to include:
- Racial or ethnic origin
- Religious beliefs
- Mental or physical health diagnosis
- Sexual orientation or gender identity
- Citizenship or immigration status
- Genetic or biometric data used for unique identification
- Specific geolocation data: information that identifies a consumer's geographic coordinates with an accuracy of more than three decimal degrees of latitude and longitude (approximately 360 feet / ~110 meters), or a street address derived from such coordinates — as defined in [Minn. Stat. § 325M.11](https://www.revisor.mn.gov/statutes/cite/325M.11)
- Known children's data

Controllers must obtain **consent** before processing sensitive data.

### Enforcement

The Minnesota Attorney General has exclusive enforcement authority. There is no private right of action. The AG may bring civil actions for penalties of up to **$7,500 per violation** plus reasonable attorney's fees. The AG does not have rulemaking authority under the MCDPA.

A **30-day cure period** applied from the effective date (July 31, 2025) through January 31, 2026: during this window, the AG was required to provide written notice of alleged violations and allow businesses 30 days to cure before commencing enforcement. As of February 1, 2026, the cure period expired. The [AG's February 2026 update](https://www.ag.state.mn.us/Office/Communications/2026/02/05_MCDPA.asp) confirmed that hundreds of educational letters and dozens of formal warning letters were sent during the initial enforcement window, with most companies voluntarily correcting identified issues.

## Impact Assessment [HIGH confidence]

### Affected Entities

The MCDPA affects businesses of all sizes operating in or targeting Minnesota residents, subject to the applicability thresholds above. Because Minnesota's economy is substantial — home to 18 Fortune 500 companies — and because the law contains no general nonprofit exemption (aside from insurance-fraud-detection nonprofits), compliance obligations are broadly distributed across commercial and nonprofit sectors alike.

### Compliance Timeline

As of the date of this report (June 2024), businesses had approximately 14 months to achieve compliance by the July 31, 2025 effective date. That deadline has now passed. The AG's cure period expired January 31, 2026, meaning full enforcement is now in effect.

Key compliance milestones:
- **July 31, 2025**: Law became effective; general business compliance required.
- **January 31, 2026**: 30-day cure period expired; AG may now bring enforcement without prior notice.
- **July 31, 2026**: First applicability threshold drops from 100,000 to 35,000 Minnesota consumers — businesses in the 35,000–99,999 range must be compliant by this date.
- **July 31, 2029**: Extended deadline for postsecondary institutions regulated by the Minnesota Office of Higher Education.

### Industry Implications

The mandatory data inventory requirement has particular compliance significance: unlike data mapping (a best practice widely followed under GDPR), an explicit statutory requirement to maintain a data inventory creates a discoverable compliance artifact and a potential enforcement touchpoint. Businesses without mature data governance programs face structural compliance work independent of the consumer rights framework.

The MCDPA's profiling challenge right is among the most consumer-protective in any US state privacy law and is expected to generate compliance questions in the automated decision-making space, particularly for entities using AI-driven scoring, recommendation systems, or decisioning processes with consequential outputs.

## Action Items

- Confirm whether your organization meets the applicability thresholds (100,000 consumers or 25,000 consumers + 25% revenue from data sales). Note that as of July 31, 2026, the primary threshold drops to 35,000 consumers — organizations currently below 100,000 should assess exposure now.
- If the SBA small-business exemption potentially applies, document the basis for that determination — but note the exemption does not cover selling sensitive data.
- Establish a data inventory if one is not already maintained; this is a statutory requirement under [Minn. Stat. § 325M.16](https://www.revisor.mn.gov/statutes/cite/325M.16), not merely a best practice.
- Conduct required Data Privacy and Protection Assessments (DPIAs) for covered processing activities (targeted advertising, profiling, sensitive data processing, data sales).
- Update privacy notices to include retention periods and consumer rights disclosures consistent with MCDPA requirements.
- Implement a mechanism for consumers to designate authorized agents through browser-level opt-out signals (universal opt-out mechanisms).
- Prepare processes to handle the expanded consumer rights, including the right to a list of specific third-party data recipients and the right to question profiling decisions.
- Document policies and procedures with a named compliance contact, as required by statute.
- Monitor AG enforcement actions as the cure period has now expired; enforcement risk is active.

## Related Reports

- [reports/privacy/state-comprehensive-laws/minnesota-mcdpa-hf4757-2024-05-30.md](reports/privacy/state-comprehensive-laws/minnesota-mcdpa-hf4757-2024-05-30.md) — Comprehensive deep-dive analysis of the same MCDPA legislation covering legislative history, full provision analysis, and enforcement outlook; should be read as the primary reference for this law.
- [reports/privacy/state-comprehensive-laws/five-states-q2-2024-privacy-laws-comparative-2024-07-26.md](reports/privacy/state-comprehensive-laws/five-states-q2-2024-privacy-laws-comparative-2024-07-26.md) — Comparative analysis of multiple Q2 2024 state privacy laws including MCDPA in context of the national state privacy law wave.
- [reports/privacy/state-comprehensive-laws/colorado-hb1130-biometric-data-2024-06-04.md](reports/privacy/state-comprehensive-laws/colorado-hb1130-biometric-data-2024-06-04.md) — Colorado's concurrent biometric data expansion to the Colorado Privacy Act, illustrating the parallel state legislative activity during the same period.

## Sources

1. [Minnesota HF 4757 Bill Status — MN Revisor of Statutes](https://www.revisor.mn.gov/bills/bill.php?b=House&f=HF4757&y=2024&ssn=0) — Official bill status page for the legislation that became the MCDPA; 93rd Legislature.
2. [Minnesota Statutes, Chapter 325M — MN Revisor of Statutes](https://www.revisor.mn.gov/statutes/cite/325M) — Official codified text of the MCDPA (§§ 325M.10–325M.21, effective July 31, 2025).
3. [Minnesota Statutes § 325M.11 — MN Revisor of Statutes](https://www.revisor.mn.gov/statutes/cite/325M.11) — Definitions section; authoritative source for the "specific geolocation data" definition (three decimal degrees standard).
4. [Minnesota Statutes § 325M.16 — MN Revisor of Statutes](https://www.revisor.mn.gov/statutes/cite/325M.16) — Controller responsibilities section; authoritative source for the data inventory and data security requirements.
5. [Minnesota Consumer Data Privacy Act — Minnesota AG Office](https://ag.state.mn.us/Data-Privacy/) — Official AG resource hub for the MCDPA, including consumer and business guidance.
6. [Minnesota Attorney General MCDPA Enforcement Page](https://www.ag.state.mn.us/Data-Privacy/Business/Controller/Enforcement.asp) — AG enforcement policies and cure period information.
7. [Minnesota AG February 2026 Enforcement Update](https://www.ag.state.mn.us/Office/Communications/2026/02/05_MCDPA.asp) — AG announcement that cure period expired January 31, 2026; summary of early enforcement activity.
8. [Minnesota AG July 2025 Launch Statement](https://www.ag.state.mn.us/Office/Communications/2025/07/28_MCDPA.asp) — Official AG statement on MCDPA taking effect July 31, 2025.
9. [Minnesota Enacts Comprehensive Consumer Data Privacy Law — White & Case LLP](https://www.whitecase.com/insight-alert/minnesota-enacts-comprehensive-consumer-data-privacy-law) — Primary finding source; White & Case analysis of the MCDPA's key provisions.
10. [Minnesota Enacts the Latest State Privacy Law (HF 4757 / SF 4782) — Troutman Pepper Locke](https://www.troutman.com/insights/minnesota-enacts-the-latest-state-privacy-law-hf-4757-sf-4782/) — Law firm analysis highlighting distinctive provisions and compliance implications.
11. [Minnesota's Unique Spin on Consumer Data Privacy — Perkins Coie](https://perkinscoie.com/insights/blog/minnesotas-unique-spin-consumer-data-privacy) — Analysis focused on MCDPA provisions that differ from other Virginia-model states, particularly data inventory and profiling rights.
12. [Minnesota Consumer Data Privacy Act Takes Effect July 31 — Koley Jessen](https://www.koleyjessen.com/insights/publications/minnesota-consumer-data-privacy-act-takes-effect-july-31) — Compliance-focused update confirming effective date and cure period details.
13. [Minnesota Enacts Comprehensive Privacy Legislation — Fredrikson & Byron](https://www.fredlaw.com/alert-minnesota-enacts-comprehensive-privacy-legislation) — Law firm client alert on applicability thresholds and exemption structure.
14. [What is Specific Geolocation Data in the MCDPA? — CLIClaw](https://www.cliclaw.com/faqs/what-specific-geolocation-data-minnesota-consumer-data-privacy-act-mcdpa/) — Analysis confirming the three-decimal-degree latitude/longitude standard for specific geolocation data under § 325M.11.
