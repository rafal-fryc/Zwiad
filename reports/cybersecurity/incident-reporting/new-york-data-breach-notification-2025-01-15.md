---
title: "New York Amends Data Breach Notification Law: 30-Day Timeline, Expanded Medical Data Coverage, and DFS Reporting Requirements"
date: 2025-01-15
jurisdiction: "New York"
category: "cybersecurity"
development_type: "legislation"
finding_id: "SCAN-20250115-028"
topic_key: "new-york-47007880-2025"
topic_type: "state_bill"
first_reported: 2025-01-15
last_updated: 2026-04-16
status_history:
  - "2026-04-16: Corrected S2376B hyperlink; added HIPAA carve-out from 30-day individual notification deadline; corrected bill attribution (A8872A/S2659B for 30-day and NYDFS changes; S2376B/A4737B for medical data expansion)."
cluster: "New York GBL § 899-aa Data Breach Notification Amendments (2024–2025)"
cluster_slug: "new-york-gbl-899aa-data-breach-notification-amendments"
---

# New York Amends Data Breach Notification Law: 30-Day Timeline, Expanded Medical Data Coverage, and DFS Reporting Requirements

**Jurisdiction:** New York | **Category:** Cybersecurity | **Date:** 2025-01-15

## Executive Summary [HIGH confidence]

In December 2024, New York Governor Kathy Hochul signed two bills into law amending New York General Business Law § 899-aa, the state's data breach notification statute. [A8872A](https://www.nysenate.gov/legislation/bills/2023/A8872/amendment/A) (companion Senate bill: [S2659B](https://www.nysenate.gov/legislation/bills/2023/S2659/amendment/B)) imposed a hard 30-day deadline for notifying affected New York residents of a breach and added a new obligation for NYDFS-regulated entities to report breaches to the New York Department of Financial Services. [S2376B](https://www.nysenate.gov/legislation/bills/2023/S2376/amendment/B) (companion Assembly bill: A4737B) expanded the definition of "private information" to include medical and health insurance information, effective March 21, 2025. A clarifying amendment signed February 14, 2025 narrowed the NYDFS reporting requirement to apply only to NYDFS-regulated covered entities. Importantly, GBL § 899-aa as amended contains a HIPAA carve-out: HIPAA-covered entities are exempt from the 30-day individual notification deadline and continue to be governed by HIPAA's 60-day window for individual notice; their parallel compliance burden under the amended statute is regulatory reporting to state agencies. Life sciences companies, consumer health care organizations, and any entity that processes New York residents' medical data face materially increased exposure under the amended law.

## Background [HIGH confidence]

New York's data breach notification framework has its roots in GBL § 899-aa, originally enacted in 2005 and significantly overhauled by the [Stop Hacks and Improve Electronic Data Security (SHIELD) Act](https://legislation.nysenate.gov/pdf/bills/2019/s5575b) in 2019. The SHIELD Act broadened the definition of "private information," imposed data security program requirements, and extended the statute's reach to any entity holding data on New York residents regardless of where that entity is located.

Prior to the December 2024 amendments, GBL § 899-aa required notification of affected individuals "in the most expedient time possible and without unreasonable delay." No statutory outer bound on timing existed. This standard drew criticism for allowing companies to delay notifications without clear accountability. Additionally, health-related data — including medical history and health insurance identifiers — was not expressly listed as a category of "private information" triggering the notification obligation, creating a gap relative to federal frameworks like HIPAA and to other state laws that had begun covering such data.

The New York State Legislature passed two bill pairs in the 2023-2024 legislative session to address these gaps:

- **[A8872A](https://www.nysenate.gov/legislation/bills/2023/A8872/amendment/A) / [S2659B](https://www.nysenate.gov/legislation/bills/2023/S2659/amendment/B)**: enacted the 30-day individual notification deadline and the NYDFS regulatory reporting obligation.
- **[S2376B](https://www.nysenate.gov/legislation/bills/2023/S2376/amendment/B) / A4737B**: enacted the expanded definition of "private information" to include medical and health insurance data, with a delayed effective date.

[Governor Hochul signed both bill pairs on December 21, 2024](https://www.governor.ny.gov/news/governor-hochul-signs-online-safety-legislation-strengthen-protections-personal-data-consumers), calling them part of a legislative package designed to strengthen consumer data protections. The December 2024 amendments were followed on February 14, 2025 by a technical correction addressing an unintended overbreadth in the NYDFS reporting provision.

The [current text of GBL § 899-aa](https://www.nysenate.gov/legislation/laws/GBS/899-AA) reflects all amendments as of early 2025.

## Detailed Analysis [HIGH confidence]

### 1. Thirty-Day Notification Deadline (Enacted by A8872A/S2659B, Effective December 21, 2024)

A8872A/S2659B amend GBL § 899-aa to require that any person or business that experiences a breach of the security of their computerized data containing New York residents' private information must notify affected residents within thirty days of discovering the breach. This replaces the prior open-ended "without unreasonable delay" standard and brings New York closer to the notification windows already in place in states such as Florida (30 days) and Colorado (30 days).

The 30-day clock runs from discovery of the breach, not from a determination that harm is likely or that the breach is confirmed. Organizations that typically use a preliminary investigation phase before initiating notification must compress that process to meet the new deadline.

**HIPAA Carve-Out:** GBL § 899-aa as amended contains an explicit HIPAA exception to the individual notification requirement. HIPAA-covered entities and business associates are **exempt** from the 30-day individual notification deadline; HIPAA's 60-day window continues to govern their individual notice obligations for breaches of unsecured protected health information. As [reported by HIPAA Journal](https://www.hipaajournal.com/new-york-data-breach-notification-requirements/) and multiple law firm analyses, this carve-out means the December 2024 amendment has limited direct impact on HIPAA-regulated entities' individual notification timeline. However, HIPAA-covered entities are **not** exempt from the statute's regulatory reporting obligations: a qualifying breach still requires notification to the New York Attorney General, the New York Department of State (NYSDOS), the New York Division of State Police (NYSDSP), and — if the entity is also NYDFS-regulated — NYDFS.

### 2. NYDFS Regulatory Reporting (Enacted by A8872A/S2659B, Effective December 21, 2024, Clarified February 14, 2025)

The December 2024 amendments added NYDFS to the list of regulators that must receive breach notification. GBL § 899-aa already required that businesses notify the New York Attorney General, NYSDOS, and the New York Division of State Police. A8872A/S2659B, as originally enacted, read as if all businesses were required to also notify NYDFS when notifying affected residents.

However, [a technical correction signed on February 14, 2025](https://www.dataprotectionreport.com/2025/02/new-york-changes-data-breach-law-in-december-and-february/) clarified that the NYDFS notification obligation applies only to "covered entities" as defined under [23 NYCRR 500.1](https://www.dfs.ny.gov/industry_guidance/cybersecurity) — NYDFS's cybersecurity regulation — and that such notice must be provided in compliance with [23 NYCRR 500.17](https://www.dfs.ny.gov/industry_guidance/cybersecurity) (the NYDFS incident notification rule). Entities that are not NYDFS-regulated — including most non-financial businesses — are not required to notify NYDFS.

For NYDFS-regulated covered entities (banks, insurance companies, mortgage servicers, and other licensed financial services firms), the December/February amendment package creates an additional parallel reporting track: they must now comply with both 23 NYCRR 500.17's cyber event notification timeline and GBL § 899-aa's broader multi-agency regulatory reporting requirements.

### 3. Expanded Definition of "Private Information" — Medical and Health Insurance Data (Enacted by S2376B/A4737B, Effective March 21, 2025)

[S2376B](https://www.nysenate.gov/legislation/bills/2023/S2376/amendment/B) adds two new categories of data to the definition of "private information" under GBL § 899-aa, effective March 21, 2025:

- **Medical information**: "any information regarding an individual's medical history, mental or physical condition, or medical treatment or diagnosis by a health care professional."
- **Health insurance information**: "an individual's health insurance policy number or subscriber identification number, any unique identifier used by a health insurer to identify the individual, or any information in an individual's application and claims history."

Prior to this amendment, a breach of such health-related information held by non-HIPAA-covered entities — for example, a consumer wellness app, a pharmaceutical company's patient-reported outcome database, or a medical device company's customer registry — would not trigger New York's breach notification statute. The March 21, 2025 effective date gave entities approximately 90 days from the December signing to assess their data inventories and update incident response plans.

The [Ropes & Gray analysis](https://www.ropesgray.com/en/insights/alerts/2025/01/new-year-new-data-breach-notification-requirements-in-new-york) emphasizes that these new categories are particularly consequential for life sciences and consumer health care companies — entities that routinely handle medical data in clinical trial databases, adverse event systems, connected device platforms, and digital health applications but may not qualify as HIPAA-covered entities or business associates. Such companies previously operated in a notification gap; they now face the same breach obligations under state law as HIPAA-regulated organizations.

For HIPAA-covered entities, the expanded definition means that a HIPAA breach involving New York residents now triggers state regulatory reporting obligations (to NYSAG, NYSDOS, NYSDSP, and if DFS-regulated, NYDFS) even though the HIPAA carve-out preserves the federal 60-day window for individual notification. [The Morrison Foerster analysis](https://www.mofo.com/resources/insights/250314-a-mofo-privacy-minute-new-york-data-breach-notification) notes this distinction: HIPAA-covered entities' primary new compliance burden under the amended law is multi-agency regulatory reporting, not accelerated individual notification.

## Impact Assessment [HIGH confidence]

### Affected Entities

The amendments create compliance obligations across a broad range of industries:

- **Life sciences companies** (pharmaceutical, biotech, medical devices): entities handling patient recruitment, adverse event systems, post-market surveillance databases, or connected device data that includes New York residents' medical information now face breach notification obligations that did not previously apply under state law.
- **Consumer health care companies** (wellness apps, digital health platforms, telehealth): companies that collect health-related data from consumers but are not HIPAA-covered entities or business associates are newly subject to GBL § 899-aa following the March 21, 2025 definitional expansion. These entities — unlike HIPAA-covered entities — are not exempt from the 30-day individual notification deadline.
- **HIPAA-covered entities and business associates** (hospitals, health systems, health plans, medical groups): these organizations retain HIPAA's 60-day individual notification window under the GBL § 899-aa HIPAA carve-out, but must now ensure compliance with state regulatory reporting obligations (NYSAG, NYSDOS, NYSDSP, and NYDFS if regulated).
- **NYDFS-regulated financial institutions**: banks, insurers, and licensed financial services firms that hold employee health insurance information or customer medical data (e.g., through underwriting or claims processing) face the dual burden of 23 NYCRR 500 incident reporting and GBL § 899-aa regulatory notification.
- **Employers and HR technology vendors**: entities that maintain employee health records, benefits enrollment data, or self-insured health plan information that could include New York employees' medical or health insurance identifiers.

### Compliance Requirements and Timelines

| Requirement | Enacted By | Effective Date | Applicable Entities |
|---|---|---|---|
| 30-day notification to NY residents | A8872A/S2659B | December 21, 2024 | All entities subject to GBL § 899-aa (HIPAA-covered entities exempt for individual notice; 60-day HIPAA window applies to them) |
| NYDFS breach reporting | A8872A/S2659B | December 21, 2024 (clarified Feb. 14, 2025) | NYDFS-covered entities under 23 NYCRR 500 only |
| Medical and health insurance data triggers notification | S2376B/A4737B | March 21, 2025 | All entities subject to GBL § 899-aa |

Practically, organizations must:

1. **Update incident response plans and playbooks** to reflect the 30-day notification deadline, replacing any procedures tied to the prior "without unreasonable delay" standard. Investigation, legal review, and notification preparation timelines must be compressed accordingly. (Note: HIPAA-covered entities should confirm their carve-out status under amended GBL § 899-aa but must ensure their regulatory reporting workflows to state agencies are operational.)

2. **Audit data inventories** to identify whether medical information or health insurance information relating to New York residents is held anywhere in company systems — including cloud storage, CRMs, EHRs, data warehouses, and third-party processors.

3. **Revise vendor and data processing agreements** to ensure third-party processors holding covered data are contractually obligated to notify within timeframes compatible with applicable deadlines.

4. **Assess NYDFS applicability**: organizations that hold New York financial services licenses should verify whether they qualify as "covered entities" under 23 NYCRR 500 and, if so, integrate GBL § 899-aa reporting into their existing NYDFS incident notification procedures.

5. **Confirm HIPAA carve-out scope**: HIPAA-covered entities should verify that their GBL § 899-aa individual notification obligations are governed by HIPAA's 60-day window, and focus their New York compliance investment on building robust multi-agency regulatory reporting workflows (NYSAG, NYSDOS, NYSDSP, NYDFS if applicable).

### Enforcement Outlook

The [New York Attorney General](https://ag.ny.gov/) has historically been active in enforcing GBL § 899-aa, bringing enforcement actions for delayed or inadequate breach notifications. The shift from a flexible "without unreasonable delay" standard to a hard 30-day deadline creates a clear, objective benchmark for enforcement. Late notification now carries less ambiguity; any notification beyond 30 days is presumptively a violation for non-HIPAA-covered entities, absent an exception. Companies should anticipate increased scrutiny.

## Action Items

- **Immediate (by end of Q1 2025)**: Update incident response plans and breach notification procedures to reflect the 30-day notification deadline applicable to all non-HIPAA-covered entities that suffer breaches of New York residents' private information.
- **Immediate**: If your organization is a NYDFS-regulated covered entity under 23 NYCRR 500, integrate GBL § 899-aa multi-agency notification requirements (NYSAG, NYSDOS, NYSDSP, NYDFS) into existing 23 NYCRR 500.17 incident response procedures.
- **Before March 21, 2025** (past, but remediation still required if incomplete): Conduct a data mapping exercise to identify all systems holding medical information or health insurance information relating to New York residents, including legacy systems, cloud environments, and third-party processors.
- **Before March 21, 2025**: Update vendor/data processor agreements to include obligations that enable compliance with applicable notification deadlines.
- **Ongoing**: Review employee health and benefits data practices, particularly for self-insured plans and wellness programs, to confirm whether they involve GBL § 899-aa-covered medical information.
- **Monitor**: Watch for New York AG enforcement guidance or litigation interpreting the 30-day deadline and the new medical/health insurance information categories, as these will shape practical compliance expectations.
- **HIPAA-covered entities**: Confirm that the GBL § 899-aa HIPAA carve-out preserves the 60-day federal window for individual notification, and build multi-agency state regulatory reporting workflows (NYSAG, NYSDOS, NYSDSP, and NYDFS if regulated) into your incident command structure. Do not conflate individual notification timing with regulatory reporting obligations.

## Related Reports

- [reports/cybersecurity/incident-reporting/new-york-nysdoh-hospital-cybersecurity-2024-06-10.md](../new-york-nysdoh-hospital-cybersecurity-2024-06-10.md) — Companion New York cybersecurity development: NYSDOH's proposed hospital cybersecurity program and incident reporting requirements share jurisdictional and healthcare-sector context with the amended GBL § 899-aa.
- [reports/cybersecurity/standards-guidance/new-york-dfs-ai-cybersecurity-guidance-2024-10-16.md](../../standards-guidance/new-york-dfs-ai-cybersecurity-guidance-2024-10-16.md) — NYDFS AI cybersecurity guidance is directly relevant to DFS-regulated entities now also subject to the amended breach notification law's NYDFS reporting provision.
- [reports/cybersecurity/incident-reporting/utah-sb98-data-breach-notification-amendment-2024-05-14.md](utah-sb98-data-breach-notification-amendment-2024-05-14.md) — Utah's 2024 data breach notification amendment reflects the broader national trend of states tightening breach timelines and expanding reporting requirements, providing comparative context.
- [reports/cybersecurity/incident-reporting/pennsylvania-breach-notification-amendment-2024-06.md](pennsylvania-breach-notification-amendment-2024-06.md) — Pennsylvania's 2024 breach notification amendment similarly expands covered categories and regulatory reporting, directly paralleling New York's December 2024 changes.

## Sources

1. [NY State Assembly Bill 2023-A8872A — NYSenate.gov](https://www.nysenate.gov/legislation/bills/2023/A8872/amendment/A) — Official text of Assembly Bill A8872A (enacted 30-day deadline and NYDFS reporting).
2. [NY Senate Bill 2023-S2659B — NYSenate.gov](https://www.nysenate.gov/legislation/bills/2023/S2659/amendment/B) — Official text of Senate companion bill S2659B to A8872A.
3. [NY Senate Bill 2023-S2376B — NYSenate.gov](https://www.nysenate.gov/legislation/bills/2023/S2376/amendment/B) — Official text of Senate Bill S2376B (enacted medical and health insurance data definition expansion, effective March 21, 2025).
4. [NY General Business Law § 899-aa — NYSenate.gov](https://www.nysenate.gov/legislation/laws/GBS/899-AA) — Current consolidated statutory text of the New York data breach notification law reflecting all amendments.
5. [Governor Hochul Signs Online Safety Legislation — NY Governor's Office](https://www.governor.ny.gov/news/governor-hochul-signs-online-safety-legislation-strengthen-protections-personal-data-consumers) — Official press release confirming December 21, 2024 signing of both bill pairs.
6. [New Year, New Data Breach Notification Requirements in New York — Ropes & Gray LLP](https://www.ropesgray.com/en/insights/alerts/2025/01/new-year-new-data-breach-notification-requirements-in-new-york) — Primary law firm analysis focusing on impacts for life sciences and consumer health care companies.
7. [New York Changes Data Breach Law — in December and February — Norton Rose Fulbright Data Protection Report](https://www.dataprotectionreport.com/2025/02/new-york-changes-data-breach-law-in-december-and-february/) — Analysis of both the December 2024 original amendments and the February 14, 2025 clarifying amendment narrowing the NYDFS reporting requirement.
8. [New York Enacts Immediate Updates to Breach Notification Law — Workplace Privacy, Data Management & Security Report](https://www.workplaceprivacyreport.com/2025/01/articles/data-breach-notification/new-york-enacts-immediate-updates-to-breach-notification-law/) — Analysis of HIPAA interaction and implications for healthcare-regulated entities.
9. [A MoFo Privacy Minute: New York Data Breach Notification — Morrison Foerster](https://www.mofo.com/resources/insights/250314-a-mofo-privacy-minute-new-york-data-breach-notification) — Law firm analysis including February 2025 amendment and HIPAA-covered entity reporting obligations.
10. [New York Modifies Data Breach Law Heading Into 2025 — Eye on Privacy (Kelley Drye)](https://www.eyeonprivacy.com/2025/01/new-york-modifies-data-breach-law-heading-into-2025/) — Additional law firm analysis summarizing all three key changes.
11. [New York Data Breach Notification Requirements Updated — HIPAA Journal](https://www.hipaajournal.com/new-york-data-breach-notification-requirements/) — Analysis confirming the HIPAA carve-out from the 30-day individual notification deadline.
12. [New York Updates Data Breach Notification Law — National Law Review](https://natlawreview.com/article/new-york-data-breach-notification-law-updated) — Summary of the amendments and effective dates.
13. [NYDFS Cybersecurity Resource Center — 23 NYCRR 500](https://www.dfs.ny.gov/industry_guidance/cybersecurity) — Official NYDFS guidance on 23 NYCRR 500 covered entity definitions and incident notification requirements (23 NYCRR 500.17) relevant to the breach reporting provision.
