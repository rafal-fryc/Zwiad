---
title: "Utah SB 98 (2024): Expanded Data Breach Notification Requirements to Attorney General and Cyber Center"
date: 2024-05-14
jurisdiction: "Utah"
category: "cybersecurity"
development_type: "legislation"
finding_id: "SCAN-20240514-007"
topic_key: "utah-34c31aa2-2024"
topic_type: "state_bill"
first_reported: 2024-05-14
last_updated: 2026-04-14
status_history: []
cluster: "Utah SB 98 (2024): Data Breach Notification Amendments"
cluster_slug: "utah-sb-98-2024-data-breach-notification"
---

# Utah SB 98 (2024): Expanded Data Breach Notification Requirements to Attorney General and Cyber Center

**Jurisdiction:** Utah | **Category:** Cybersecurity | **Date:** 2024-05-14

## Executive Summary [HIGH confidence]

On March 19, 2024, Utah Governor Spencer J. Cox signed [Senate Bill 98 (SB 98)](https://le.utah.gov/~2024/bills/static/SB0098.html) — "Online Data Security and Privacy Amendments" — into law, with an effective date of May 1, 2024. The bill amends two existing statutes: the [Protection of Personal Information Act (Utah Code § 13-44-101 et seq.)](https://law.justia.com/codes/utah/title-13/chapter-44/part-2/section-202/) and the Utah Technology Governance Act in the Utah Government Operations Code (§ 63A-16-1101 et seq.). The key change requires that when a data breach affects 500 or more Utah residents, the notifying entity must now include specific enumerated information in its notification to both the Utah Attorney General and the newly established Utah Cyber Center. A companion confidentiality provision allows submitters to seek protected-record status for breach reports by including a written claim of business confidentiality. Organizations operating in Utah or handling data on Utah residents must update their incident-response procedures to satisfy the expanded notification content requirements that took effect May 1, 2024.

## Background [HIGH confidence]

Utah first enacted its data breach notification law in 2006 (S.B. 69) and has amended it several times since. For most of its history, the law primarily required notification to affected Utah residents but did not mandate reporting to any government agency. That framework changed significantly in 2023.

In March 2023, Utah's legislature passed [S.B. 127 — Cybersecurity Amendments](https://le.utah.gov/~2023/bills/static/SB0127.html), signed into law March 23, 2023 and effective May 3, 2023. S.B. 127 made two foundational changes that set the stage for the 2024 amendments:

1. It created the **Utah Cyber Center** — a new governmental entity tasked with developing a statewide strategic cybersecurity plan for executive branch agencies and other governmental organizations, identifying and mitigating cyber threats, and providing incident response coordination across state and federal partners.
2. It imposed a new requirement: when an investigation into a breach reveals that misuse of personal information of 500 or more Utah residents has occurred or is reasonably likely to occur, the entity must notify both the Office of the Attorney General and the newly created Utah Cyber Center. Prior to S.B. 127, no such government-agency notification was required.

The 2023 S.B. 127 framework established the obligation to notify, but did not prescribe the specific content of those government notifications. SB 98 in 2024 closes that gap.

The legislative history of Utah's broader data privacy framework also includes S.B. 208 (2009), S.B. 193 (2019), and the [Utah Consumer Privacy Act (S.B. 227, 2022)](https://le.utah.gov/~2022/bills/static/SB0227.html) — demonstrating consistent legislative attention to data protection across more than a decade. SB 98 fits within this pattern of incremental refinement.

## Detailed Analysis [HIGH confidence]

### Statutes Amended

SB 98, titled "Online Data Security and Privacy Amendments," amends:

- **Utah Code § 13-44** — Protection of Personal Information Act (commercial entities)
- **Utah Code § 63A-16** — Utah Technology Governance Act (government entities)
- **Utah Code § 63D-2-105** — Use of authorized domain extensions for government websites (a separate, minor provision)

### New Required Content for AG and Cyber Center Notifications

For breaches affecting 500 or more Utah residents, SB 98 requires the notification sent to the Attorney General and the Utah Cyber Center to include all of the following, effective May 1, 2024:

1. **Date the breach occurred** (or best estimate if exact date is unknown)
2. **Date the breach was discovered** by the entity
3. **Total number of people affected** by the breach of system security, including a **specific breakout of the total number of Utah residents** affected
4. **Type of personal information** involved in the breach
5. **A short description** of the breach of system security that occurred

For **governmental entities**, SB 98 goes further and requires additional detail in reports to the Utah Cyber Center, including: the path or means of access used by the unauthorized party; perpetrator information if known; and response steps taken by the entity.

### 500-Resident Threshold and Notification Triggers

The 500-resident threshold was established by S.B. 127 in 2023 and is carried forward unchanged by SB 98. The trigger for all governmental notifications remains: an investigation reveals that **misuse of personal information of 500 or more Utah residents has occurred or is reasonably likely to occur**. Entities not meeting this threshold still must notify affected individuals but have no government-reporting obligation under state law.

For breaches involving **1,000 or more** state residents, entities must also notify major consumer reporting agencies — a separate requirement carried forward from earlier law.

### Confidentiality Provision

SB 98 adds a new confidentiality mechanism for breach notifications submitted to the Attorney General or the Cyber Center. A submitted document may be classified as a **protected record** under Utah's Government Records Access and Management Act (GRAMA) if the submitting entity includes:

- A **written claim of business confidentiality**, and
- A **concise statement of reasons** supporting the claim.

This provision addresses a legitimate concern for organizations that feared detailed breach disclosures to government agencies could become publicly accessible through GRAMA requests. The protected-record classification, if granted, shields the submission from routine public disclosure, though it remains accessible to the agencies for enforcement and coordination purposes.

### Government-Entity Reporting Separately Codified

SB 98 makes a structural distinction between private-sector and public-sector breach reporting. Government entities now have codified, independent reporting obligations to the Cyber Center under § 63A-16, with more granular required content (including perpetrator information and response steps) than private-sector filers under § 13-44.

### What Did Not Change

SB 98 does not alter:
- The resident-notification obligation for **all** affected Utah residents (applicable regardless of the 500-person threshold)
- The "most expedient time possible" standard for notification timing
- The definition of "personal information" that triggers the law
- The existing exemptions for HIPAA-covered entities and other federally regulated sectors

## Impact Assessment [MEDIUM confidence]

### Affected Entities

The amended requirements apply to any **person or business entity that owns or licenses computerized data containing personal information of Utah residents** — with no revenue or size threshold. This includes companies headquartered outside Utah if they hold data on Utah residents. Governmental entities operating in Utah are subject to the parallel requirements under § 63A-16.

Industries with large Utah resident datasets — healthcare, financial services, retail, technology, and higher education — face the greatest exposure given volume-driven breach frequency.

### Compliance Requirements and Timelines

All requirements are effective **May 1, 2024** (already in effect). Organizations should verify that:

1. Incident response plans and playbooks have been updated to capture and transmit the five required data fields (occurrence date, discovery date, total affected including breakout of Utah residents affected, type of data, and description) in government notifications.
2. Template notification letters to the AG and Cyber Center reflect the new content requirements.
3. Procedures exist to route government notifications via email to **cybercenter@utah.gov** (the Cyber Center's designated reporting channel) concurrently with AG notification.
4. A mechanism exists to assert business-confidentiality claims on breach reports when warranted, including drafting the required written justification.

### Enforcement Outlook

Utah's enforcement of data breach notification violations can result in civil actions by the Attorney General. Under [Utah Code § 13-44-301](https://le.utah.gov/xcode/Title13/Chapter44/13-44-P3_1800010118000101.pdf), violations may result in civil penalties of **up to $2,500 per violation** (or per series of violations concerning a specific consumer), with an **aggregate cap of $100,000** for related violations concerning more than one consumer. Repeat violations may attract heightened enforcement scrutiny. The Attorney General is empowered to bring civil actions for non-compliance.

The creation of the Utah Cyber Center as a dedicated breach-intake body — rather than the AG receiving reports alone — signals Utah's intent to use breach data for statewide cybersecurity intelligence and resilience planning. Organizations that fail to notify may find themselves identified through Cyber Center incident intelligence, not solely through AG investigations.

No enforcement actions specifically targeting SB 98 non-compliance have been publicly reported as of the time of writing.

## Action Items

- **Immediate (already past deadline):** Review and update all incident response plans and breach notification templates to include the five SB 98-required data elements in AG and Cyber Center notifications.
- **Immediate:** Confirm that notification routing addresses include both the Utah AG and cybercenter@utah.gov for all breaches meeting the 500-resident threshold.
- **For counsel drafting notifications:** Add a step to assess whether a business-confidentiality claim under GRAMA is warranted and, if so, prepare the required written claim and reasons statement as part of the breach filing package.
- **For government entities in Utah:** Review the expanded Cyber Center reporting requirements under § 63A-16, which include additional fields (perpetrator information, access vector, response steps) beyond what private-sector filers must provide.
- **Ongoing:** Monitor the Utah Cyber Center (cybercenter.utah.gov) and Attorney General for any interpretive guidance on the content requirements or confidentiality-claim procedures.
- **Ongoing:** Track any future Utah legislative sessions for further amendments — Utah has amended its breach notification law in four of the last six years, reflecting continued legislative attention to the topic.

## Related Reports

- [reports/cybersecurity/incident-reporting/federal-circia-final-rule-delay-2026-04-07.md](reports/cybersecurity/incident-reporting/federal-circia-final-rule-delay-2026-04-07.md) — Federal parallel: CIRCIA imposes similar mandatory incident-reporting obligations for critical infrastructure operators at the federal level, and harmonization with state reporting frameworks (including Utah's) is an active policy issue.
- [reports/cybersecurity/enforcement-actions/california-ccpa-cybersecurity-audit-class-litigation-2026-04-14.md](reports/cybersecurity/enforcement-actions/california-ccpa-cybersecurity-audit-class-litigation-2026-04-14.md) — State-level cybersecurity compliance risk: California's CPPA cybersecurity audit rule creates a parallel compliance burden for organizations operating in multiple states alongside Utah's breach reporting updates.

## Sources

1. [SB0098 — Utah Legislature (2024 Session)](https://le.utah.gov/~2024/bills/static/SB0098.html) — Official bill page for SB 98, "Online Data Security and Privacy Amendments," 2024 Utah General Session
2. [SB0098S03 — 3rd Substitute (enrolled version)](https://le.utah.gov/~2024/bills/sbillamd/SB0098S03.htm) — Amended text of SB 98 as signed into law
3. [Understanding Utah's Updated Data Breach Reporting Requirements — Constangy Brooks Smith & Prophete LLP](https://www.constangy.com/constangy-cyber-advisor/utah-amends-data-breach-reporting-requirements) — Primary source law firm analysis (originating firm for this finding)
4. [Utah Enacts Amendments to State Breach Notification Law — Hunton Andrews Kurth](https://www.hunton.com/privacy-and-information-security-law/utah-enacts-amendments-to-state-breach-notification-law) — Independent law firm analysis of SB 98 provisions
5. [Utah Amends Cybersecurity and Data Breach Notification Law — National Law Review](https://natlawreview.com/article/utah-updates-breach-notification-requirements-take-effect) — Legal news coverage of SB 98 effective date
6. [Utah Updates to Breach Notification Requirements Take Effect — Workplace Privacy Report (Hinshaw & Culbertson)](https://www.workplaceprivacyreport.com/2024/05/articles/data-breach-notification/utah-updates-to-breach-notification-requirements-take-effect/) — Analysis of May 1, 2024 effective date and compliance implications
7. [Utah amends data breach reporting requirements — Lexology (Constangy)](https://www.lexology.com/library/detail.aspx?g=d47290c0-8bc7-4f26-b653-4d012af67849) — Original Lexology posting of Constangy analysis
8. [Utah Code § 13-44-202 — Personal Information: Disclosure of System Security Breach (2025)](https://law.justia.com/codes/utah/title-13/chapter-44/part-2/section-202/) — Official statutory text as currently codified
9. [Data Breach Notification Law Update: Utah and Pennsylvania — Davis Wright Tremaine](https://www.dwt.com/blogs/privacy--security-law-blog/2023/03/data-breach-laws-utah-pennsylvania) — Analysis of the 2023 S.B. 127 amendment that created the Cyber Center and AG notification obligation
10. [Utah Amends Data Breach Law, Creates Cyber Center — National Law Review](https://natlawreview.com/article/utah-amends-data-breach-law-creates-cyber-center) — Background on the 2023 S.B. 127 legislation establishing the foundational AG/Cyber Center notification requirement
11. [Need to Report a Breach? — Utah Cyber Center](https://cybercenter.utah.gov/Report-a-Breach/) — Official Utah Cyber Center breach reporting portal and contact information
12. [Security Breach Notification Chart: Utah — Perkins Coie](https://perkinscoie.com/insights/publication/security-breach-notification-chart-utah) — Comprehensive multi-law-firm reference chart for Utah breach notification law
