---
title: "FTC Finalizes Order Against Illuminate Education Over Data Breach Affecting 10 Million Students"
date: 2026-06-08
jurisdiction: "Federal"
category: "privacy"
development_type: "enforcement"
finding_id: "SCAN-20260615-035"
topic_key: "FTC-ILLUMINATE-EDUCATION-2026"
topic_type: "enforcement"
first_reported: 2026-06-08
last_updated: "2026-06-28"
status_history:
  - {date: "2026-06-28", status: "consent-order", finding_id: "SCAN-20260628-007", run_id: "2026-06-28T19-28-09"}
cluster: "FTC EdTech Student Data Privacy Enforcement (Illuminate Education and Related Actions)"
cluster_slug: "ftc-edtech-student-data-breach-enforcement"
---

# FTC Finalizes Order Against Illuminate Education Over Data Breach Affecting 10 Million Students

**Jurisdiction:** Federal | **Category:** Privacy — Enforcement | **Date:** June 5, 2026

## Summary [HIGH confidence]

The Federal Trade Commission voted 2-0 on June 5, 2026 to give [final approval to a modified consent order](https://www.ftc.gov/news-events/news/press-releases/2026/06/ftc-gives-final-approval-order-against-illuminate-settling-allegations-it-failed-secure-students) against Illuminate Education, Inc., a K-12 education software vendor, settling allegations that the company's security failures led to a data breach exposing personal information of approximately 10.1 million current and former students. The finalized order — modified from the December 2025 proposed version in response to public comments — requires Illuminate to implement a comprehensive data security program, adopt strict data minimization practices, delete unnecessary student data, and publish a data retention schedule. The action signals sustained FTC attention to educational technology vendors and the protection of children's personal data, arriving alongside a parallel $5.1 million multistate settlement by California, Connecticut, and New York attorneys general.

## Key Facts [HIGH confidence]

- The FTC voted 2-0 to finalize the modified consent order on June 5, 2026, per the [FTC press release](https://www.ftc.gov/news-events/news/press-releases/2026/06/ftc-gives-final-approval-order-against-illuminate-settling-allegations-it-failed-secure-students). The order runs for 10 years, a departure from the FTC's longstanding 20-year default for administrative orders.
- Illuminate Education is a Wisconsin-based provider of student information systems and assessment tools used by school districts nationwide, including the New York City and Los Angeles Unified School Districts — the two largest in the country, per [StateScoop](https://statescoop.com/ftc-orders-illuminate-education-to-bolster-data-security-after-breach-impacting-10m-students/).
- The breach occurred between December 28, 2021, and January 8, 2022. A threat actor exploited login credentials of a former Illuminate employee who had departed the company three and a half years earlier, per [K-12 Dive](https://www.k12dive.com/news/illuminate-education-reaches-settlement-with-ftc-over-2021-data-breach/806814/).
- Compromised data included email and mailing addresses, dates of birth, student records, health-related information, academic and behavioral data, disciplinary records, and special education status for approximately 10.1 million students, per the [FTC case record](https://www.ftc.gov/legal-library/browse/cases-proceedings/222-3105-illuminate-education-inc-matter).
- The FTC's complaint alleged that Illuminate was warned about security vulnerabilities on its network by a third-party vendor as early as 2020 — nearly two years before the breach — but failed to remediate them, per [National Law Review](https://natlawreview.com/article/when-we-take-security-seriously-isnt-enough-lessons-ftcs-illuminate-order).
- The final order incorporates one substantive change from the December 2025 proposed version: an explicit data minimization requirement — prohibiting Illuminate from collecting, processing, or maintaining personal data beyond what is necessary to provide requested services — added in response to EPIC's public comment, per [EPIC](https://epic.org/ftc-finalizes-settlement-with-illuminate-education-heeding-epics-call-to-strengthen-data-minimization-requirements/).
- Separately, California, Connecticut, and New York reached a $5.1 million settlement with Illuminate on November 6, 2025, resolving state law violations for approximately 5 million students in those three states, per the [New York AG press release](https://ag.ny.gov/press-release/2025/attorney-general-james-and-multistate-coalition-secure-51-million-education). The Connecticut action was the first enforcement brought under Connecticut's Student Data Privacy Law.

## Order Requirements [HIGH confidence]

The final consent order, enforceable for 10 years, imposes the following obligations on Illuminate:

**Data Security Program.** Illuminate must establish and implement a comprehensive information security program covering access controls, encryption, logging, vulnerability management, vendor risk assessments, cloud configuration review, secure software development, incident response procedures, and regular penetration testing, per [Inside Privacy](https://www.insideprivacy.com/united-states/federal-trade-commission/ftc-announces-10-year-information-security-consent-orders-with-illuminate-education-and-illusory-systems/).

**Data Minimization.** Illuminate is prohibited from collecting, processing, or maintaining personal data that is not reasonably necessary to provide the products or services requested. This provision was strengthened in the final order following EPIC's comment, per [EPIC](https://epic.org/ftc-finalizes-settlement-with-illuminate-education-heeding-epics-call-to-strengthen-data-minimization-requirements/).

**Data Retention and Deletion.** Illuminate must delete personal information that is no longer needed and publish a publicly available data retention schedule detailing what data is collected, why it is collected, and the timeframe for its deletion, per [ComplianceHub.Wiki](https://compliancehub.wiki/ftc-illuminate-education-final-order-student-data-security-edtech-2026/).

**Breach Notification Reporting.** Within 14 days of notifying any federal, state, or local government entity about a covered security incident, Illuminate must submit a corresponding report to the FTC, per [Inside Privacy](https://www.insideprivacy.com/united-states/federal-trade-commission/ftc-announces-10-year-information-security-consent-orders-with-illuminate-education-and-illusory-systems/).

**Misrepresentation Ban.** Illuminate is permanently prohibited from misrepresenting its data security and privacy practices, or the timeline within which it will notify school districts and students about a breach, per the [FTC press release](https://www.ftc.gov/news-events/news/press-releases/2026/06/ftc-gives-final-approval-order-against-illuminate-settling-allegations-it-failed-secure-students).

**Third-Party Assessments and Certifications.** Illuminate must undergo biennial third-party security assessments for the 10-year order period, with full disclosure to assessors, and its Chief Information Security Officer must provide annual certifications of compliance to the FTC, per [Captain Compliance](https://captaincompliance.com/education/ftc-finalizes-order-against-illuminate-education-over-student-data-security-failures/).

## Significance for EdTech Vendors [MEDIUM confidence]

The Illuminate enforcement action is the FTC's most significant action targeting a K-12 education technology vendor and sets a clear baseline for what "reasonable" data security means in the sector. Three aspects are especially notable for compliance planning:

**Credential lifecycle management.** The breach was enabled by unrevoked credentials belonging to an employee who had left the company 3.5 years earlier. The California AG's portion of the multistate settlement explicitly requires immediate termination of departing employee credentials, per [Wilson Sonsini](https://www.wsgr.com/en/insights/edtech-provider-agrees-to-dollar51-million-settlement-with-three-state-attorneys-general-over-student-data-breach.html). This will become a de facto standard for FTC Section 5 compliance in the edtech space.

**Vendor warning ignored.** The FTC's complaint specifically identified Illuminate's failure to act on its own third-party vendor's 2020 security vulnerability report. Documenting and actioning vendor security findings will now be essential to demonstrating reasonable care.

**Data minimization in consent orders.** EPIC's successful advocacy to strengthen the data minimization provision in the final order marks an evolution in FTC edtech enforcement — consent orders now include affirmative data minimization obligations beyond what the original proposed orders contained. This is notable given concurrent FTC enforcement priorities under the updated COPPA Rule (effective April 22, 2026), per [IAPP](https://iapp.org).

## Action Items

- **Audit credential lifecycle processes immediately.** Revoke all access credentials — including to third-party cloud systems and backup databases — upon employee departure. The Illuminate breach used credentials from an employee who left 3.5 years prior.
- **Review and act on outstanding vendor security reports.** Unresolved third-party security findings are now a documented FTC enforcement theory. Maintain a remediation log for all vendor assessments, and treat unaddressed findings as a material risk.
- **Inventory student/minors personal data and implement data minimization.** Map all personal data collected from K-12 students. Assess whether each data element is strictly necessary to provide the contracted service. Purge data that cannot be justified under a data minimization standard.
- **Publish a data retention schedule.** The FTC now requires Illuminate to maintain a public retention schedule. EdTech vendors contracting with school districts should proactively adopt the same transparency standard.
- **Prepare for dual federal-state exposure.** Illuminate faced simultaneous FTC and multistate AG enforcement. Vendors operating in California, Connecticut, and New York face heightened scrutiny; the Connecticut settlement was the first action under Connecticut's Student Data Privacy Law.
- **Review backup database architecture.** The Illuminate breach reached backup databases that were not isolated from live environments. Isolate backup systems per network segmentation best practices.

## Related Reports

- [reports/privacy/childrens-privacy/coppa-amendments-compliance-deadline-2026-04-13.md](../childrens-privacy/coppa-amendments-compliance-deadline-2026-04-13.md) — Updated COPPA Rule (effective April 22, 2026) imposes new obligations on operators handling children's data, directly reinforcing the FTC's regulatory posture evidenced by the Illuminate action.
- [reports/privacy/childrens-privacy/federal-coppa-enforcement-begins-2026-05-04.md](../childrens-privacy/federal-coppa-enforcement-begins-2026-05-04.md) — FTC's activation of updated COPPA enforcement (May 2026) provides the regulatory backdrop for the Illuminate action's emphasis on children's data protection.
- [reports/privacy/enforcement-actions/ftc-strategic-plan-fy2026-2030-2026-04-13.md](ftc-strategic-plan-fy2026-2030-2026-04-13.md) — FTC's FY 2026-2030 Strategic Plan identifies children's online safety as "one of the most important consumer protection issues of our time," providing the strategic context for the Illuminate enforcement priority.
- [reports/privacy/enforcement-actions/federal-x-corp-ftc-consent-order-petition-2026-06-04.md](federal-x-corp-ftc-consent-order-petition-2026-06-04.md) — A contemporaneous FTC consent order case (X Corp.) illustrates the Commission's continued active use of consent orders as an enforcement mechanism under the current 2-0 composition.

## Sources

1. [FTC Press Release: Final Approval of Order Against Illuminate Education (June 5, 2026)](https://www.ftc.gov/news-events/news/press-releases/2026/06/ftc-gives-final-approval-order-against-illuminate-settling-allegations-it-failed-secure-students) — Official FTC announcement of the finalized order, vote count, and order requirements.
2. [FTC Case Record: In the Matter of Illuminate Education, Inc. (222-3105)](https://www.ftc.gov/legal-library/browse/cases-proceedings/222-3105-illuminate-education-inc-matter) — Official FTC docket page with complaint, proposed order, and final order documents.
3. [FTC Initial Action Press Release (December 2025)](https://www.ftc.gov/news-events/news/press-releases/2025/12/ftc-takes-action-against-education-technology-provider-failing-secure-students-personal-data) — FTC announcement of the proposed consent order and original allegations.
4. [EPIC: FTC Finalizes Settlement with Illuminate Education, Heeding EPIC's Call to Strengthen Data Minimization Requirements](https://epic.org/ftc-finalizes-settlement-with-illuminate-education-heeding-epics-call-to-strengthen-data-minimization-requirements/) — Analysis of the data minimization change added in the final order following EPIC's public comment.
5. [New York AG Press Release: $5.1 Million Multistate Settlement (November 2025)](https://ag.ny.gov/press-release/2025/attorney-general-james-and-multistate-coalition-secure-51-million-education) — Official NY AG announcement of the California/Connecticut/New York settlement.
6. [Inside Privacy (Covington): FTC Announces 10-Year Information Security Consent Orders](https://www.insideprivacy.com/united-states/federal-trade-commission/ftc-announces-10-year-information-security-consent-orders-with-illuminate-education-and-illusory-systems/) — Law firm analysis of both FTC consent orders (Illuminate and Illusory Systems), order requirements and compliance obligations.
7. [Wilson Sonsini: EdTech Provider Agrees to $5.1 Million Settlement with Three State Attorneys General](https://www.wsgr.com/en/insights/edtech-provider-agrees-to-dollar51-million-settlement-with-three-state-attorneys-general-over-student-data-breach.html) — Law firm analysis of the multistate settlement, specific state-level security requirements.
8. [National Law Review: When 'We Take Security Seriously' Isn't Enough](https://natlawreview.com/article/when-we-take-security-seriously-isnt-enough-lessons-ftcs-illuminate-order) — Analysis of FTC's enforcement theory and compliance lessons for the broader industry.
9. [StateScoop: FTC Orders Illuminate Education to Bolster Data Security After Breach Impacting 10M Students](https://statescoop.com/ftc-orders-illuminate-education-to-bolster-data-security-after-breach-impacting-10m-students/) — Coverage including geographic scope of affected school districts.
10. [K-12 Dive: Illuminate Education Reaches Settlement with FTC](https://www.k12dive.com/news/illuminate-education-reaches-settlement-with-ftc-over-2021-data-breach/806814/) — Education sector coverage with breach timeline details.
11. [Captain Compliance: FTC Finalizes Order Against Illuminate Education](https://captaincompliance.com/education/ftc-finalizes-order-against-illuminate-education-over-student-data-security-failures/) — Summary of third-party assessment and CISO certification requirements.
12. [ComplianceHub.Wiki: The FTC's Final Illuminate Order and What It Means for Every Data-Handling Company](https://compliancehub.wiki/ftc-illuminate-education-final-order-student-data-security-edtech-2026/) — Detailed breakdown of order provisions including retention schedule requirements.
13. [Connecticut AG Press Release: First Action Under Student Data Privacy Law](https://portal.ct.gov/ag/press-releases/2025-press-releases/attorney-general-tong-enters-into-settlement-in-first-action-under-student-data-privacy-law) — Connecticut AG announcement confirming this was the first enforcement under the Connecticut Student Data Privacy Law.

## Update 2026-06-28

**Change:** (unspecified) → consent-order
**Source:** https://www.ftc.gov/news-events/news/press-releases/2026/06/ftc-gives-final-approval-order-against-illuminate-settling-allegations-it-failed-secure-students
**Summary:** A subsequent pipeline scan (SCAN-20260628-007) confirmed the June 5, 2026 final consent order approval via the [FTC press release](https://www.ftc.gov/news-events/news/press-releases/2026/06/ftc-gives-final-approval-order-against-illuminate-settling-allegations-it-failed-secure-students). No new material facts emerged beyond what is documented above — the 2-0 Commission vote, the 10-year order term, and all order requirements including the data minimization provision added in response to EPIC's public comment were fully reported at the time of this report's initial publication on June 8, 2026. The companion consent order against Illusory Systems, Inc. (a separate FTC enforcement matter concerning a crypto platform, docketed separately from the Illuminate matter) similarly remains as proposed; its final approval status has not been separately confirmed in public sources as of this update.
**Finding ID:** SCAN-20260628-007
**Run ID:** 2026-06-28T19-28-09
