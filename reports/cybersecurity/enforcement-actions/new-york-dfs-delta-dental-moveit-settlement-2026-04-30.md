---
title: "New York DFS Secures $2.25 Million Settlement with Delta Dental Over MOVEit Data Breach"
date: 2026-04-30
jurisdiction: "New York"
category: "cybersecurity"
development_type: "enforcement"
finding_id: "SCAN-20260504-012"
topic_key: "new-york-9d005a5e-2026"
topic_type: "enforcement"
first_reported: 2026-05-04
last_updated: 2026-05-19
status_history:
  - "2026-05-19: Merged finding SCAN-20260519-008 — added clarification that approximately 6,000 New York policyholders were specifically affected by the breach; the 7 million figure reflects the total nationwide exposure across all Delta Dental entities."
  - "2026-05-19: Revised per reviewer feedback (round 1) — removed unverifiable '6,000 New York policyholders' figure (traced only to generic IAPP homepage); corrected breach window from May 27–30 to May 28–30 per consent order; added 60,000 files exfiltrated figure from consent order; added § 500.17(a) notification delay timeline (detected June 2023, confirmed July 2023, notified NYDFS December 15, 2023)."
cluster: "NYDFS Cybersecurity Regulation (23 NYCRR Part 500): AI Guidance and Enforcement"
cluster_slug: "nydfs-cybersecurity-regulation-23-nycrr-500"
---

# New York DFS Secures $2.25 Million Settlement with Delta Dental Over MOVEit Data Breach

**Jurisdiction:** New York | **Category:** Cybersecurity | **Date:** 2026-04-30

## Summary [HIGH confidence]

The New York Department of Financial Services (NYDFS) announced on April 30, 2026, a [$2.25 million settlement](https://www.dfs.ny.gov/reports_and_publications/press_releases/pr20260430) with Delta Dental Insurance Company (DDIC) and Delta Dental of New York, Inc. (DDNY) arising from a 2023 MOVEit Transfer server breach. The breach exposed personal information of approximately **7 million individuals** nationwide, with threat actors exfiltrating approximately **60,000 files** from Delta Dental's MOVEit server between May 28 and May 30, 2023. The settlement resolves violations of [23 NYCRR Part 500](https://www.dfs.ny.gov/system/files/documents/2023/03/23NYCRR500_0.pdf) — the DFS Cybersecurity Regulation — specifically inadequate incident response policies and improper data retention practices that left large volumes of nonpublic information unnecessarily exposed when threat actors exploited the MOVEit zero-day vulnerability. This is among NYDFS's largest cybersecurity enforcement penalties under Part 500 and reinforces the regulator's focus on data minimization and timely incident notification as core compliance obligations.

## Key Facts [HIGH confidence]

- NYDFS Acting Superintendent Kaitlin Asrow announced the settlement on April 30, 2026, via [official press release](https://www.dfs.ny.gov/reports_and_publications/press_releases/pr20260430).
- The penalty amount is **$2.25 million**, to be paid jointly by DDIC and DDNY; the consent order bars the companies from seeking reimbursement or indemnification for the penalty.
- Threat actors exploited a zero-day vulnerability in [MOVEit Transfer](https://www.bleepingcomputer.com/news/security/delta-dental-of-california-data-breach-exposed-info-of-7-million-people/) between **May 28 and May 30, 2023** — the specific exfiltration window for Delta Dental as identified in the consent order (the broader Cl0p ransomware group campaign against MOVEit installations began May 27, 2023). A [forensic review confirmed](https://databreaches.net/2026/05/01/nysdfs-secures-2-25-million-cybersecurity-settlement-with-delta-dental/) that approximately **60,000 files** were exfiltrated from the server during this window.
- Exposed data included names, addresses, Social Security numbers, driver's license numbers, financial account information, tax identification numbers, and patient health information. Approximately **7 million individuals** were affected across all Delta Dental entities nationally, per [SecurityWeek reporting](https://www.securityweek.com/delta-dental-of-california-discloses-data-breach-impacting-6-9-million-people/).
- DFS investigation found violations of the following specific regulatory sections:
  - **23 NYCRR § 500.3(n)** — failure to implement and maintain a written policy addressing incident response;
  - **23 NYCRR § 500.13** — failure to implement retention settings and secure disposal of NPI no longer necessary for business operations;
  - **23 NYCRR § 500.16(b)(6)** — failure to establish a written incident response plan addressing reporting of Cybersecurity Events;
  - **23 NYCRR § 500.17(a)** — failure to provide timely 72-hour notice to DFS following determination of a Cybersecurity Event. Delta Dental became aware of suspicious activity in **June 2023** and confirmed on **July 6, 2023** that consumer data had been exfiltrated, yet did not notify NYDFS until **December 15, 2023** — nearly six months after detection and well beyond the 72-hour window required by the regulation.
- The companies notified all affected consumers by **March 2024**, per [DataBreaches.net coverage](https://databreaches.net/2026/05/01/nysdfs-secures-2-25-million-cybersecurity-settlement-with-delta-dental/).
- NYDFS issued an [Industry Letter on the MOVEit vulnerability on June 2, 2023](https://www.dfs.ny.gov/industry_guidance/industry_letters/il20230602_moveit_vulnerability), directing covered entities to assess their exposure — signaling early regulatory awareness of the risk.
- [Paul Hastings analysis](https://www.paulhastings.com/insights/ph-privacy/youve-got-mail-nydfs-enforcement-action-highlights-cybersecurity-risk-of-over-retention-and-other-risks) characterizes this enforcement action as highlighting dual cybersecurity risks from both inadequate incident response and data **over-retention** — retaining NPI beyond operational necessity creates a larger attack surface.

## Regulatory Context [HIGH confidence]

The DFS Cybersecurity Regulation, [23 NYCRR Part 500](https://www.law.cornell.edu/regulations/new-york/title-23/chapter-I/part-500), first took effect in March 2017 and was substantially amended in November 2023 to add phased-in requirements on multi-factor authentication, asset management, and enhanced governance. The amendments became fully effective November 1, 2025.

Section 500.13 requires covered entities to implement "policies and procedures for the secure disposal on a periodic basis of any Nonpublic Information that is no longer necessary for business operations or for other legitimate business purposes." The Delta Dental consent order found that the companies lengthened their IT systems' default retention settings, storing the ultimately exfiltrated files for longer than 30 days — a direct data minimization failure. This illustrates how retaining excess data, even if originally collected for legitimate purposes, can constitute an independent Part 500 violation when that data is later exfiltrated.

Section 500.17(a) requires prompt notification to DFS "in the most expedient time possible and without unreasonable delay but in no event later than 72 hours" after determining a reportable Cybersecurity Event occurred. The Delta Dental timeline — awareness in June 2023, confirmed exfiltration July 6, 2023, NYDFS notification December 15, 2023 — represents a delay of approximately five months from confirmed knowledge of the event. The [Debevoise analysis](https://www.debevoisedatablog.com/2026/05/06/nydfss-first-2026-cyber-enforcement-action-highlights-imperative-of-early-notification-robust-ir-plans-and-data-minimization/) of this enforcement action specifically highlights that the obligation to notify attaches upon "determination" of the event, not upon completion of a full forensic investigation.

This action is the second significant Part 500 enforcement penalty within the past year. In August 2025, NYDFS imposed a [$2 million penalty on Healthplex, Inc.](https://www.hunton.com/privacy-and-information-security-law/nydfs-settles-with-healthplex-for-2-million-over-inadequate-cybersecurity-measures) for similar violations including failure to implement MFA, absence of a data retention policy, and delayed incident notification. Taken together, these actions reveal an NYDFS enforcement pattern focused on:

1. Data minimization and retention policy compliance under § 500.13;
2. Timely incident reporting under § 500.17(a); and
3. Documented, operational (not merely paper) incident response under §§ 500.3(n) and 500.16.

## Action Items

- **Audit data retention schedules immediately.** Review whether your organization retains NPI beyond operational necessity. Implement secure disposal procedures per § 500.13. Over-retention of data that is later breached constitutes an independent regulatory violation — not just a breach consequence.
- **Verify incident response plan documentation.** Confirm your written incident response plan satisfies § 500.16(b)(6), specifically including procedures for reporting Cybersecurity Events to DFS within 72 hours. A plan that exists on paper but is not operationally implemented will not satisfy the regulation.
- **Test your 72-hour notification trigger.** Establish internal processes to determine promptly when a cybersecurity incident rises to a "Cybersecurity Event" requiring DFS notification under § 500.17(a). The Delta Dental enforcement makes clear: waiting five months from detection — even while a forensic investigation is ongoing — will not be treated as a mitigating factor. The clock runs from "determination" of the event.
- **Assess third-party file-transfer tool exposure.** Review the use of managed file-transfer software (including MOVEit and alternatives) in light of known supply-chain vulnerabilities. Ensure vendor risk management processes under § 500.11 include patching and monitoring requirements for these tools.
- **Review annual certification accuracy.** Annual Part 500 compliance certifications are due by April 15. The Healthplex enforcement action separately found that certifying compliance while not in compliance is itself a violation. Ensure certifications are substantively accurate.

## Related Reports

- [reports/cybersecurity/standards-guidance/new-york-nydfs-ai-cybersecurity-guidance-2024-10-16.md](../standards-guidance/new-york-nydfs-ai-cybersecurity-guidance-2024-10-16.md) — Same NYDFS regulatory framework (23 NYCRR Part 500); that report covers DFS guidance on AI-related cybersecurity risks under the same regulation governing this enforcement action.
- [reports/cybersecurity/enforcement-actions/multistate-enzo-biochem-data-breach-settlement-2024-08-13.md](multistate-enzo-biochem-data-breach-settlement-2024-08-13.md) — Parallel multistate AG enforcement arising from a 2023 ransomware data breach; similar pattern of inadequate cybersecurity practices leading to consumer NPI exposure and multi-million-dollar settlement.
- [reports/cybersecurity/enforcement-actions/hhs-ocr-hipaa-ransomware-settlements-2026-04-24.md](hhs-ocr-hipaa-ransomware-settlements-2026-04-24.md) — HHS OCR HIPAA enforcement against healthcare entities for similar failures to protect patient health information; parallel federal enforcement trend reinforcing data security compliance obligations.
- [reports/cybersecurity/incident-reporting/new-york-data-breach-notification-2025-01-15.md](../incident-reporting/new-york-data-breach-notification-2025-01-15.md) — New York's 2025 amendments to GBL § 899-aa breach notification law; DFS-licensed entities subject to both that statute and Part 500 notification requirements.

## Sources

1. [NYDFS Press Release: Acting Superintendent Kaitlin Asrow Secures $2.25 Million Cybersecurity Settlement with Delta Dental (Apr. 30, 2026)](https://www.dfs.ny.gov/reports_and_publications/press_releases/pr20260430) — Official government announcement; primary source for settlement amount, parties, and regulatory framing.
2. [23 NYCRR Part 500 — Cybersecurity Requirements for Financial Services Companies (DFS)](https://www.dfs.ny.gov/system/files/documents/2023/03/23NYCRR500_0.pdf) — Official regulatory text; basis for specific section citations.
3. [23 NYCRR Part 500 — Cornell LII](https://www.law.cornell.edu/regulations/new-york/title-23/chapter-I/part-500) — Secondary source for regulatory text; used for section reference verification.
4. [NYDFS Industry Letter: MOVEit Transfer Vulnerability (June 2, 2023)](https://www.dfs.ny.gov/industry_guidance/industry_letters/il20230602_moveit_vulnerability) — Official DFS guidance issued at the time of the MOVEit zero-day discovery; establishes that DFS was aware and directed covered entity action.
5. [DataBreaches.net: NYSDFS Secures $2.25 Million Cybersecurity Settlement with Delta Dental (May 1, 2026)](https://databreaches.net/2026/05/01/nysdfs-secures-2-25-million-cybersecurity-settlement-with-delta-dental/) — Secondary coverage with consent order details including specific Part 500 sections violated, 60,000 files exfiltrated, and breach window May 28–30.
6. [BleepingComputer: Delta Dental of California data breach exposed info of 7 million people](https://www.bleepingcomputer.com/news/security/delta-dental-of-california-data-breach-exposed-info-of-7-million-people/) — Contemporaneous breach reporting covering scope of MOVEit exposure.
7. [SecurityWeek: Delta Dental Says Data Breach Exposed 7 Million Customers](https://www.securityweek.com/delta-dental-of-california-discloses-data-breach-impacting-6-9-million-people/) — Independent verification of breach scope and data types exposed.
8. [Paul Hastings LLP: You've Got Mail — NYDFS Enforcement Action Highlights Cybersecurity Risk of Over-Retention and Other Risks](https://www.paulhastings.com/insights/ph-privacy/youve-got-mail-nydfs-enforcement-action-highlights-cybersecurity-risk-of-over-retention-and-other-risks) — Law firm client alert with substantive analysis of enforcement action and compliance implications.
9. [Debevoise & Plimpton: NYDFS's First 2026 Cyber Enforcement Action Highlights Imperative of Early Notification, Robust IR Plans and Data Minimization (May 6, 2026)](https://www.debevoisedatablog.com/2026/05/06/nydfss-first-2026-cyber-enforcement-action-highlights-imperative-of-early-notification-robust-ir-plans-and-data-minimization/) — Law firm analysis; confirms notification delay timeline and that § 500.17(a) notification clock begins at determination of event, not completion of forensic review.
10. [Hunton Andrews Kurth: NYDFS Settles With Healthplex for $2 Million Over Inadequate Cybersecurity Measures](https://www.hunton.com/privacy-and-information-security-law/nydfs-settles-with-healthplex-for-2-million-over-inadequate-cybersecurity-measures) — Prior Part 500 enforcement context; establishes enforcement pattern for data retention and notification violations.
11. [InsuranceNewsNet: Acting Superintendent Kaitlin Asrow Secures $2.25 Million Cybersecurity Settlement with Delta Dental](https://insurancenewsnet.com/oarticle/acting-superintendent-kaitlin-asrow-secures-2-25-million-cybersecurity-settlement-with-delta-dental) — Additional coverage of the official announcement.
