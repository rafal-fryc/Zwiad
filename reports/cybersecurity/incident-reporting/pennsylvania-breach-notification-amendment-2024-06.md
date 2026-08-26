---
title: "Pennsylvania Act 33 of 2024: Significant Amendments to the Breach of Personal Information Notification Act"
date: 2024-07-23
jurisdiction: "Pennsylvania"
category: "cybersecurity"
development_type: "legislation"
finding_id: "SCAN-20240723-030"
topic_key: "pennsylvania-75debb06-2024"
topic_type: "state_bill"
first_reported: 2024-07-23
last_updated: 2026-04-15
status_history:
  - "2026-04-15: Revised per reviewer feedback (round 1) — corrected Expanded Definition section to accurately attribute health insurance and online credentials to the 2023 amendment (SB 696) rather than Act 33 of 2024; added 2023 amendment paragraph to Background; clarified UTPCPL § 201-8 as the penalty-amount source in Enforcement section."
  - "2026-04-15: Revised per reviewer feedback (round 2) — corrected act number from 'No. 15' to 'No. 151' (Act 151 of 2022) in all occurrences; corrected Sources #3 URL and session from 2023-2024 to 2021-2022 Regular Session."
---

# Pennsylvania Act 33 of 2024: Significant Amendments to the Breach of Personal Information Notification Act

**Jurisdiction:** Pennsylvania | **Category:** Cybersecurity | **Date:** 2024-07-23

## Executive Summary [HIGH confidence]

On June 28, 2024, Pennsylvania Governor Josh Shapiro signed [Senate Bill 824 into law as Act 33 of 2024](https://www.legis.state.pa.us/cfdocs/legis/li/uconsCheck.cfm?yr=2024&sessInd=0&act=33), further strengthening Pennsylvania's [Breach of Personal Information Notification Act (BPINA)](https://www.attorneygeneral.gov/bpina/), originally enacted as Act 94 of 2005 and substantially expanded by a 2023 amendment (SB 696, P.L. 2139, No. 151). The 2024 amendments took effect on September 26, 2024. Three changes introduced by Act 33 stand out as particularly significant: (1) entities experiencing a breach affecting more than 500 Pennsylvania residents must now notify the Office of Attorney General concurrently with notifying affected individuals; (2) entities whose breaches expose Social Security numbers, driver's license numbers, state ID numbers, or financial account numbers must provide affected individuals with a free independent credit report and 12 months of credit monitoring services; and (3) the definition of "medical information" — which the 2023 amendment had added broadly — is narrowed so that it applies only to state agencies and state agency contractors. Health insurance information and online credentials, which the 2023 amendment (SB 696) added to the covered-data definition, are retained unchanged by Act 33. The law aligns Pennsylvania — previously an outlier on regulator notification — with the majority of states, and places Pennsylvania among the small group of states that mandate credit monitoring remedies.

## Background [HIGH confidence]

Pennsylvania enacted its original Breach of Personal Information Notification Act in 2005 (Act 94, codified at 73 P.S. §§ 2301–2329). The law required notification to affected Pennsylvania residents when their unencrypted personal information was accessed or acquired by an unauthorized person. The original statute was notable for having no government notification requirement: entities notified consumers but did not report to any state regulator, placing Pennsylvania in an increasingly small minority of states that lacked regulatory-reporting obligations.

In 2006, 2008, and 2014 Pennsylvania made modest refinements but did not require AG notification or credit monitoring.

In 2023, Pennsylvania enacted its most substantial pre-Act 33 overhaul of BPINA. Senate Bill 696, signed into law as [P.L. 2139, No. 151](https://www.palegis.us/legislation/bills/2021/sb696) and effective May 2, 2023, significantly expanded the personal information definition and imposed enhanced security obligations. Specifically, the 2023 amendment added three new categories of covered data: (1) **medical information** (individually identifiable information in an individual's current or historical medical record created by a health care professional); (2) **health insurance information** (a health insurance policy number or subscriber identification number combined with an access code or other information permitting misuse of health insurance benefits); and (3) **online credentials** (a username or email address combined with a password or security question and answer that would permit access to an online account). The 2023 amendment also imposed enhanced security requirements on entities that maintain personal information on behalf of the Commonwealth — requiring use of encryption or other adequate security measures and maintenance of written security and data-retention policies — and imposed a stricter notification timeline on state agencies and state agency contractors (7 business days from breach determination). The 2023 amendment expanded covered-entity scope to expressly include municipalities, financial institutions, healthcare providers not subject to HIPAA, and contractors.

Over this same period, the majority of states enacted or updated their own breach notification laws to require concurrent regulator notification — typically to the attorney general, a consumer protection agency, or a specialized cybersecurity body. By the time Act 33 was signed, approximately 35 states required entities to notify a state regulator when a breach exceeded a threshold number of affected residents. Pennsylvania's absence of such a requirement had been a gap in its legal framework for nearly two decades.

The [Pennsylvania Attorney General's BPINA page](https://www.attorneygeneral.gov/bpina/) reflects the prior framework's limitations: prior to Act 33, the AG had no structured inbound reporting mechanism and relied on affected individuals and press reporting to learn of major breaches. Senate Bill 824 was passed by the Pennsylvania General Assembly and sent to the Governor in June 2024 to close this structural gap.

## Detailed Analysis [HIGH confidence]

### Statutory Authority and Legislative Vehicle

Act 33 of 2024 is codified at [P.L. 427, No. 33 (June 28, 2024)](https://www.legis.state.pa.us/WU01/LI/LI/US/HTM/2024/0/0033..HTM), amending 73 P.S. §§ 2301–2329 (the BPINA). The official enrolled bill text is available directly from the [Pennsylvania General Assembly](https://www.palegis.us/legislation/bills/2023/sb824). The effective date is September 26, 2024, 90 days after signing.

### Revised Definition of Personal Information

Act 33 of 2024 does not add new categories to the definition of "personal information" — those expansions were accomplished by the 2023 amendment (SB 696). Rather, Act 33 **narrows** one category that the 2023 amendment added broadly, and retains the others without change.

**What the 2023 amendment (SB 696) added — retained by Act 33:**

- **Health insurance information** — a policy number or subscriber identification number in combination with any access code or other information permitting misuse of the individual's health insurance benefits. Added by SB 696, effective May 2, 2023; unchanged by Act 33.
- **Online credentials** — a username or email address combined with a password or security question and answer permitting access to an online account. Added by SB 696, effective May 2, 2023; unchanged by Act 33.

**What Act 33 changed:**

- **Medical information (narrowed scope)** — The 2023 amendment had added medical information broadly, covering any individually identifiable information in a current or historical medical record created by a health care professional. Act 33 restricts this prong so that it applies **only to medical information in the possession of a state agency or state agency contractor**. This is a significant restriction: private-sector organizations — hospitals, clinics, health systems, insurers acting in a commercial capacity — are no longer obligated to notify under BPINA for breaches of medical records. HIPAA's Breach Notification Rule remains applicable to HIPAA-covered entities and their business associates, but BPINA's own medical-information trigger now applies exclusively to public-sector holders.

The pre-existing covered data elements — Social Security numbers, driver's license/state ID numbers, financial account numbers combined with required security codes — remain unchanged from the original 2005 statute.

Compliance programs should reflect both the 2023 addition of health insurance information and online credentials (already in force since May 2, 2023) and the 2024 narrowing of the medical information trigger.

### Attorney General Notification Requirement

Act 33 of 2024 creates a new mandatory notification obligation to the Pennsylvania Attorney General whenever a breach affects more than 500 Pennsylvania residents. Key parameters:

- **Threshold:** More than 500 Pennsylvania residents affected
- **Timing:** The AG notification must be made concurrently with notification to affected individuals (i.e., simultaneously, not after)
- **Method:** The Pennsylvania AG launched a dedicated [online BPINA reporting portal](https://www.attorneygeneral.gov/bpina/) on September 26, 2024, the amendment's effective date. Entities may use this portal to submit required notifications
- **Content:** The portal requires specific reporting content, details of which are built into the submission form

This brings Pennsylvania into alignment with the approximately 35 states that already had attorney general or regulator notification requirements. Per [Ropes & Gray's analysis](https://www.ropesdataphiles.com/2024/09/pennsylvania-strengthens-data-breach-notification-law/), Pennsylvania is one of the last major states to adopt this requirement.

### Credit Monitoring and Credit Report Requirement

One of the most operationally demanding changes in Act 33 is the mandatory credit monitoring obligation. When a breach involves a Social Security number, driver's license number, state identification card number, or financial account number (individually or in combination), the breached entity must:

1. Provide affected individuals with **access to an independent credit report from a consumer reporting agency**, free of charge
2. Provide **12 months of credit monitoring services**, free of charge

This obligation applies regardless of whether the breach also triggers the AG notification requirement. Pennsylvania joins Connecticut, Delaware, Massachusetts, and the District of Columbia as the only jurisdictions imposing a statutory credit monitoring mandate as of the law's effective date, per [Regulatory Oversight's analysis](https://www.regulatoryoversight.com/2024/09/amendments-align-pennsylvanias-breach-notification-law-with-majority-of-states/).

The credit monitoring requirement is operationally significant: it requires advance contracting with a credit monitoring vendor or establishing a mechanism to provide individual access codes, as well as updated breach response protocols and potentially higher breach-remediation cost estimates in risk assessments.

### Notification Timeline: Unchanged "Without Unreasonable Delay" Standard

Act 33 does not alter the notification timing standard for private entities. The law retains the longstanding "without unreasonable delay" standard for notifying affected individuals. Regulatory practice generally treats this as approximately 30–60 days following confirmation of the breach, though no statutory ceiling is specified. Entities may delay notification if law enforcement requests a delay to protect a criminal investigation.

**Public entities face a stricter timeline established by the 2023 amendment:** state agencies and state agency contractors must notify affected individuals within 7 business days of determining that a breach occurred. Act 33 did not alter this timeline.

### Enforcement Mechanism

BPINA does not create a private right of action for affected individuals. Enforcement is through the Pennsylvania Attorney General. Under [73 P.S. § 2329](https://law.justia.com/codes/pennsylvania/act-33/), a violation of BPINA constitutes an unfair or deceptive act or practice in violation of the [Pennsylvania Unfair Trade Practices and Consumer Protection Law (UTPCPL)](https://www.legis.state.pa.us/WU01/LI/LI/US/HTM/1968/0/0387..HTM). This means the AG may bring civil enforcement actions seeking injunctive relief, restitution for affected consumers, and civil penalties. The penalty amounts — up to $1,000 per violation and up to $3,000 for violations affecting individuals 60 years of age or older — derive from **UTPCPL § 201-8** (73 P.S. § 201-8), which is the UTPCPL's civil penalty provision. Section 2329 of BPINA is the enforcement hook that designates BPINA violations as UTPCPL violations; the penalty schedule itself is set by the UTPCPL.

The availability of the AG's new online portal — which creates a structured data inflow — signals increased capacity for the AG to monitor and pursue non-compliant entities, particularly those that fail to report despite meeting the 500-resident threshold.

### Comparison to Other State Breach Notification Laws

| Feature | Pennsylvania (Act 33, 2024) | Utah (SB 98, 2024) | California (CCPA/Civ. Code 1798.82) | Texas (BC § 521) |
|---|---|---|---|---|
| Regulator notification threshold | 500 residents | 500 residents | N/A (no specific threshold) | No regulator notification |
| Notification timing (private) | Without unreasonable delay | Expedient / reasonable time | Most expedient time (within 30 days recommended) | Without unreasonable delay |
| Credit monitoring mandate | Yes (12 months, SSN/DL/financial) | No | No | No |
| Online credential coverage | Yes (since 2023) | No | Yes | No |
| Health insurance info | Yes (since 2023) | No | Yes | Partial |
| Enforcement body | AG (UTPCPL) | AG | AG (CCPA) | AG |

Pennsylvania's Act 33, taken as a whole, leapfrogs several peer states in remediation obligations while aligning on regulator-notification requirements that most states already had in place.

## Impact Assessment [HIGH confidence]

### Entities Subject to Act 33

BPINA applies to any entity — private sector, nonprofit, or government — that **maintains, stores, or manages computerized data that includes personal information of Pennsylvania residents**. There is no size or revenue threshold. Covered entities include:

- Pennsylvania businesses and organizations of all sizes
- Out-of-state businesses that hold personal information of Pennsylvania residents
- Service providers and vendors handling data on behalf of covered entities
- State agencies and state agency contractors (subject to the stricter 7-business-day timeline, established by the 2023 amendment)

Industries with the highest exposure due to breach frequency — healthcare (particularly for health insurance information, added by the 2023 amendment), financial services, retail (for financial account numbers), and technology (for online credentials, added by the 2023 amendment) — face the greatest compliance burden.

### New Compliance Obligations Effective September 26, 2024

Organizations that have not yet done so must urgently complete the following obligations introduced by Act 33 (noting that health insurance information and online credentials as triggering data elements have been in effect since May 2, 2023 under the prior amendment):

1. **AG Notification Protocol:** Update incident response playbooks to include concurrent AG notification for any breach affecting more than 500 Pennsylvania residents. Register and test the AG's online BPINA reporting portal.
2. **Credit Monitoring Vendor Contract:** Execute agreements with credit monitoring service providers capable of delivering 12 months of monitoring at scale. Establish a mechanism for generating and distributing access codes or links to affected individuals.
3. **Definition Updates:** Confirm that breach assessment and classification procedures already reflect the 2023 addition of health insurance information and online credentials as triggering data elements, and account for the 2024 narrowing of the medical information trigger to state agencies only.
4. **Cost Modeling:** Update breach cost estimates and cyber insurance coverage assessments to reflect the credit monitoring mandate, which can add meaningful per-record costs.
5. **Consumer Notification Templates:** Revise notification letters to describe credit monitoring access, including instructions for individuals to enroll.

### Enforcement Outlook

The AG's online reporting portal significantly increases the regulatory visibility of breaches. Prior to Act 33, the AG had no direct pipeline for breach data; now, large breaches must be proactively reported. This infrastructure is consistent with increased enforcement activity: entities that experience breaches involving 500+ Pennsylvania residents but fail to notify the AG are now affirmatively non-compliant, not merely undetected.

No public enforcement actions under Act 33 have been reported as of the date of this report (April 2026). The newness of the law and the recency of the portal suggest enforcement is in an early stage; firms should expect increasing scrutiny as the AG's office accumulates breach-report data and identifies non-reporters.

## Action Items

- **Overdue (effective May 2, 2023):** Confirm that incident response plans and data classification frameworks already treat health insurance information and online credentials as BPINA-covered data elements, as required by the 2023 amendment (SB 696, P.L. 2139, No. 151).
- **Overdue (effective September 26, 2024):** Audit your incident response plan and playbooks to ensure simultaneous AG notification is triggered for any breach affecting more than 500 Pennsylvania residents. Use the PA AG's BPINA online portal at [https://www.attorneygeneral.gov/bpina/](https://www.attorneygeneral.gov/bpina/).
- **Overdue:** Execute a credit monitoring vendor contract capable of providing 12 months of free credit monitoring to affected individuals when Social Security numbers, driver's license numbers, state ID numbers, or financial account numbers are involved.
- **Overdue:** Update breach response notification letter templates to include credit monitoring enrollment instructions.
- **Overdue (if a state agency or contractor):** Ensure your notification procedures reflect the 7-business-day deadline for state entities (established by the 2023 amendment).
- **Governance:** Ensure general counsel and privacy/security teams are briefed on the narrowed medical information trigger: for private-sector entities, medical information is no longer a BPINA-covered data element as of Act 33, though HIPAA obligations remain unaffected.
- **Risk modeling:** Revise cyber insurance coverage assessments and breach cost models to account for 12-month credit monitoring costs, which are now a legal obligation (not a voluntary remediation choice) for qualifying breaches.
- **Ongoing:** Monitor the PA AG's BPINA portal for any published guidance, reporting statistics, or enforcement actions. Monitor the PA General Assembly for further amendments — [the legislature has already tagged amending legislation for Act 33](https://www.legis.state.pa.us/cfdocs/BillInfo/AmendingLegis.cfm?Act=0033.&ActSessYear=2024&ActSessInd=0&SessYear=2023).

## Related Reports

- [reports/cybersecurity/incident-reporting/utah-sb98-data-breach-notification-amendment-2024-05-14.md](reports/cybersecurity/incident-reporting/utah-sb98-data-breach-notification-amendment-2024-05-14.md) — Utah enacted a parallel expansion of AG and Cyber Center breach notification requirements in the same 2024 legislative cycle, making a direct state-law comparison useful for multi-state compliance programs.
- [reports/cybersecurity/incident-reporting/federal-circia-final-rule-delay-2026-04-07.md](reports/cybersecurity/incident-reporting/federal-circia-final-rule-delay-2026-04-07.md) — Federal CIRCIA imposes mandatory cyber incident reporting for critical infrastructure operators; Pennsylvania entities in covered sectors must navigate both CIRCIA and BPINA obligations.
- [reports/cybersecurity/enforcement-actions/california-ccpa-cybersecurity-audit-class-litigation-2026-04-14.md](reports/cybersecurity/enforcement-actions/california-ccpa-cybersecurity-audit-class-litigation-2026-04-14.md) — California's cybersecurity audit rule creates a comparable multi-state compliance challenge for organizations holding personal information across Pennsylvania and California.

## Sources

1. [Act No. 33 of 2024 — Pennsylvania General Assembly (official act page)](https://www.legis.state.pa.us/cfdocs/legis/li/uconsCheck.cfm?yr=2024&sessInd=0&act=33) — Official landing page for Act 33, with links to the enrolled bill text
2. [P.L. 427, No. 33 — Full Text of Act 33 of 2024 (PA General Assembly)](https://www.legis.state.pa.us/WU01/LI/LI/US/HTM/2024/0/0033..HTM) — Enrolled and signed statutory text of the amending act
3. [Senate Bill 696 (2021-2022 Regular Session) — Pennsylvania General Assembly](https://www.palegis.us/legislation/bills/2021/sb696) — Official bill page for SB 696 (P.L. 2139, No. 151), the 2023 BPINA amendment effective May 2, 2023
4. [Pennsylvania Consolidated Statutes § 33 (2024) — Justia](https://law.justia.com/codes/pennsylvania/act-33/) — Codified text of BPINA as amended by Act 33
5. [2023-2024 Legislation Amending Act 33 of 2024 — PA General Assembly](https://www.legis.state.pa.us/cfdocs/BillInfo/AmendingLegis.cfm?Act=0033.&ActSessYear=2024&ActSessInd=0&SessYear=2023) — Legislative history and subsequent amending bills
6. [Breach of Personal Information Notification Act (BPINA) — Pennsylvania Office of Attorney General](https://www.attorneygeneral.gov/bpina/) — Official AG page describing requirements and hosting the reporting portal
7. [Pennsylvania's Updated Data Breach Notification Law — Buchanan Ingersoll & Rooney PC](https://www.bipc.com/pennsylvania%E2%80%99s-updated-cybersecurity-breach-notification-law) — Comprehensive law firm analysis of Act 33 provisions
8. [Pennsylvania Amends Its Breach Notification Law — Buchanan Ingersoll & Rooney PC](https://www.bipc.com/pennsylvania-amends-its-breach-notification-law) — Analysis of the 2023 BPINA amendment (SB 696)
9. [Pennsylvania Strengthens Data Breach Notification Law — Ropes & Gray (RopesDataPhiles)](https://www.ropesdataphiles.com/2024/09/pennsylvania-strengthens-data-breach-notification-law/) — Analysis with comparative context on AG notification requirement
10. [Amendments Align Pennsylvania's Breach Notification Law With Majority of States — Regulatory Oversight](https://www.regulatoryoversight.com/2024/09/amendments-align-pennsylvanias-breach-notification-law-with-majority-of-states/) — Multi-state comparative analysis including credit monitoring peer states
11. [Pennsylvania's Updated Breach Notification Law Requires Credit Monitoring — HIPAA Journal](https://www.hipaajournal.com/pennsylvanias-updated-breach-notification-law-2024/) — Healthcare-sector focused analysis of credit monitoring and health insurance information provisions
12. [Updated Pennsylvania Breach of Personal Information Notification Act Now in Effect — HIPAA Journal](https://www.hipaajournal.com/updated-pennsylvania-breach-of-personal-information-notification-act-now-in-effect/) — Coverage of the 2023 BPINA amendment (SB 696) effective date
13. [Pennsylvania Amends Data Breach Notification Law — Alston & Bird Privacy, Cyber & Data Strategy Blog](https://www.alstonprivacy.com/pennsylvania-amends-data-breach-notification-law/) — Independent law firm analysis of key changes
14. [New Data Breach Notification Obligations for PA and a New Reporting Portal — Eye On Privacy (Sheppard Mullin)](https://www.eyeonprivacy.com/2024/09/new-data-breach-notification-obligations-for-pa-and-a-new-reporting-portal/) — Originating source firm's analysis; covers AG portal launch timing
15. [Pennsylvania Launches Data Breach Reporting Portal — National Law Review](https://natlawreview.com/article/new-data-breach-notification-obligations-pa-and-new-reporting-portal) — Covers the September 26, 2024 portal launch
16. [Pennsylvania Amends Breach of Personal Information Notification Act — National Law Review](https://natlawreview.com/article/client-update-pennsylvania-breach-personal-information-notification-act-bpina) — Coverage of the 2023 BPINA amendment (SB 696)
17. [Pennsylvania Updates Breach of Personal Information Notification — National Law Review](https://natlawreview.com/article/pennsylvania-amends-data-protection-requirements-revised-breach-notification-act) — Summary of Act 33 changes with compliance focus
18. [Pennsylvania amends the Breach of Personal Information Notification Act — JDSupra (Orrick)](https://www.jdsupra.com/legalnews/pennsylvania-amends-the-breach-of-3820092/) — Additional independent law firm analysis
19. [Amendments Expand Pennsylvania's Data Breach Notification Law — Cozen O'Connor](https://www.cozen.com/news-resources/publications/2024/amendments-expand-pennsylvania-s-data-breach-notification-law) — Covers expanded personal information definitions and AG notification in detail
20. [Security Breach Notification Chart: Pennsylvania — Perkins Coie](https://perkinscoie.com/insights/publication/security-breach-notification-chart-pennsylvania) — Comprehensive multi-factor chart for Pennsylvania breach notification law
21. [Pennsylvania's Amended Data Breach Law Upends Standard Framework — Shook, Hardy & Bacon](https://www.shb.com/intelligence/newsletters/pds/hansen-pennsylvania-data-breach-law) — Analysis highlighting credit monitoring as a novel departure from standard breach notification frameworks
22. [Pennsylvania Unfair Trade Practices and Consumer Protection Law — PA General Assembly](https://www.legis.state.pa.us/WU01/LI/LI/US/HTM/1968/0/0387..HTM) — Official text of the enforcement statute under which BPINA violations are prosecuted; § 201-8 sets the civil penalty amounts
23. [Client Update: Pennsylvania BPINA — Norris McLaughlin](https://norrismclaughlin.com/news/client-update-pennsylvania-breach-of-personal-information-notification-act-bpina/) — Law firm analysis covering the 2023 amendment's expanded personal information definition and security requirements
24. [Pennsylvania Data Breach Notification Act Amendment — Vorys](https://www.vorys.com/publication-pennsylvania-data-breach-notification-act-amendment-what-businesses-need-to-know-for-may-2-2023) — Detailed compliance guidance on the 2023 BPINA amendment effective May 2, 2023
