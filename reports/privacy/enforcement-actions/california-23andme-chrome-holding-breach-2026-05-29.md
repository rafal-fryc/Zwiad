---
title: "California AG Sues Chrome Holding (Formerly 23andMe) Over 2023 Genetic Data Breach Affecting 7 Million Customers"
date: 2026-05-29
jurisdiction: "California"
category: "privacy"
development_type: "enforcement"
finding_id: "SCAN-20260601-026"
topic_key: "CAAG-CHROME-HOLDING-CO-2026"
topic_type: "enforcement"
first_reported: 2026-05-29
last_updated: 2026-06-01
status_history: []
cluster: "23andMe 2023 Genetic Data Breach: State AG Enforcement Actions"
cluster_slug: "23andme-genetic-data-breach-ag-enforcement"
---

# California AG Sues Chrome Holding (Formerly 23andMe) Over 2023 Genetic Data Breach Affecting 7 Million Customers

**Jurisdiction:** California | **Category:** Privacy | **Date:** May 29, 2026

## Summary [HIGH confidence]

California Attorney General Rob Bonta filed suit on May 27, 2026 against Chrome Holding Co. and ChromeCo, Inc. — the entities that emerged from 23andMe's March 2025 bankruptcy — in San Francisco Superior Court, alleging systematic security failures that allowed a threat actor to operate undetected within 23andMe's systems for over five months in 2023 and exfiltrate sensitive genetic data belonging to nearly 7 million customers, including 855,541 Californians. The complaint invokes three California statutes — the Genetic Information Privacy Act (GIPA), the California Consumer Privacy Act (CCPA), and the Reasonable Data Security Law — each of which imposes heightened obligations on companies that collect and maintain genetic data. This is the first state AG enforcement action arising from the 23andMe breach and represents a significant escalation of state accountability for direct-to-consumer (DTC) genetic testing companies following the company's collapse into bankruptcy.

## Key Facts [HIGH confidence]

- On May 27, 2026, AG Bonta filed *People v. Chrome Holding Co., fka 23andMe et al.* in San Francisco Superior Court, targeting Chrome Holding Co. and ChromeCo, Inc. — the post-bankruptcy corporate successors to 23andMe — [official complaint (PDF)](https://oag.ca.gov/system/files/attachments/press-docs/People%20v%20Chrome%20Holding%20fka%2023andMe%20et%20al.%20-%20Stamped%20Complaint.pdf).
- The breach began in approximately April 2023 via a **credential stuffing attack**, exploiting username and password combinations stolen from prior breaches at other companies — most notably a [2017 breach at MyHeritage](https://www.bleepingcomputer.com/news/security/california-ag-sues-23andme-over-2023-breach-exposing-health-data/), a former 23andMe partner.
- Through credential stuffing, the threat actor gained initial access to approximately **14,000 individual 23andMe accounts**, then exploited a coding error in 23andMe's **"DNA Relatives" feature** — which allowed doctored database queries — to laterally expand unauthorized access to the data of nearly **7 million customers**, per [California DOJ press release](https://oag.ca.gov/news/press-releases/attorney-general-bonta-sues-chrome-holding-co-formerly-known-23andme-over-2023).
- The threat actor operated undetected within 23andMe's systems for **over five months** — from approximately April through October 2023 — before the company publicly acknowledged the breach on October 6, 2023, per the [California AG complaint](https://oag.ca.gov/news/press-releases/attorney-general-bonta-sues-chrome-holding-co-formerly-known-23andme-over-2023).
- The complaint alleges that **23andMe paid an undisclosed $400,000 cryptocurrency ransom** to the threat actor in exchange for the removal of breach-related information posted online and disclosure of additional system vulnerabilities, while simultaneously denying publicly that a security incident had occurred, per [The Register's reporting](https://www.theregister.com/legal/2026/05/29/rob-bonta-sues-23andmes-new-owners-over-2023-breach/).
- Specific security failures alleged in the complaint include: (1) failure to implement multi-factor authentication (MFA) required by 23andMe's own internal Information Security Policy for access to the most sensitive consumer data; (2) failure to prevent or detect the well-known credential stuffing threat vector; (3) failure to detect the internal DNA Relatives coding error that enabled lateral data exfiltration; and (4) making false and misleading public statements about security practices and the breach's severity, per the [California DOJ press release](https://oag.ca.gov/news/press-releases/attorney-general-bonta-sues-chrome-holding-co-formerly-known-23andme-over-2023).
- A prior **multistate coalition investigation** by California and other state AGs found that 23andMe's pre-breach security procedures fell below industry standards in multiple respects, per [Hogan Lovells analysis](https://www.hoganlovells.com/en/publications/state-attorneys-general-data-breach-investigations-23andme-in-2023-more-in-2024).
- **23andMe filed for Chapter 11 bankruptcy in March 2025**, citing falling demand and legal liabilities from the breach. The company's assets were subsequently acquired by the TTAM Research Institute, a nonprofit founded by 23andMe's original CEO Anne Wojcicki, with the sale completed on July 14, 2025, per [Lawfare](https://www.lawfaremedia.org/article/privacy--consent--and-national-security-after-the-23andme-bankruptcy).
- A separate private **class action settlement of $30 million** received final court approval on January 30, 2026, covering approximately 6.4 million US residents whose data was compromised, per [HIPAA Journal](https://www.hipaajournal.com/23andme-class-action-data-breach-settlement/). This civil AG enforcement action is independent of that settlement.
- Twenty-seven other states and Washington D.C. challenged the transfer of genetic data during the 23andMe bankruptcy sale process, with Michigan AG Dana Nessel announcing participation in a bipartisan coalition objecting to the data sale, per [Michigan AG press release](https://www.michigan.gov/ag/news/press-releases/2025/06/10/ag-nessel-enters-multistate-legal-fight-to-protect-genetic-information-in-23andme-bankruptcy-case).

## Legal Framework [HIGH confidence]

The complaint relies on three California statutes that collectively impose the strictest DTC genetic data obligations in the United States:

**California Genetic Information Privacy Act (GIPA), Cal. Civ. Code §§ 56.17–56.18** (effective January 1, 2022): GIPA applies specifically to DTC genetic testing companies and requires: (1) affirmative and separate consumer consent for each distinct use category of genetic data; (2) reasonable security procedures to protect genetic data against unauthorized access, destruction, use, modification, or disclosure; (3) the ability for consumers to access and destroy their genetic data; and (4) complete notice of data collection, use, and disclosure practices. Civil penalties: $1,000 per negligent violation; $1,000–$10,000 per intentional violation, per [National Law Review](https://natlawreview.com/article/california-enacts-new-privacy-law-genetic-data) and [Hinshaw & Culbertson analysis](https://www.hinshawlaw.com/en/insights/privacy-cyber-and-ai-decoded-alert/privacy-law-essentials-californias-genetic-information-privacy-act).

**California Consumer Privacy Act (CCPA)**: The complaint invokes the CCPA's data security requirements and its prohibition on false or misleading statements material to consumers' decisions to use a company's products. Penalties: $2,500 per violation; $7,500 per intentional violation or violation involving minor consumers, per [ppc.land reporting on the complaint](https://ppc.land/california-sues-23andme-over-7-million-genetic-profiles-exposed-in-2023-breach/).

**California Reasonable Data Security Law (Cal. Civ. Code § 1798.100 et seq.)**: Requires businesses to implement and maintain reasonable security procedures and practices appropriate to the nature and sensitivity of personal information maintained.

The AG's theory is that genetic data — encoding health predispositions, biological relatives, ethnicity, and ancestry — sits at the apex of sensitivity under all three statutes, requiring the highest possible security posture. 23andMe's failure to require MFA, its failure to detect credential stuffing, and its exploitation of the DNA Relatives coding error collectively violated this heightened obligation.

## Why It Matters [HIGH confidence]

**Genetic data is uniquely irreplaceable.** Unlike passwords or payment card numbers, an individual's genetic profile cannot be changed after exposure. It encodes immutable family relationships, disease predispositions, and ethnic heritage — information with lifelong consequences. The AG complaint explicitly argues this immutability justifies heightened legal obligation.

**The ransom payment and public denial are the most legally explosive allegations.** If proven, paying $400,000 in cryptocurrency while publicly denying a security incident occurred would constitute affirmative deception of California consumers, opening intentional violation penalties under both CCPA and GIPA — potentially $7,500 and $10,000 per incident, respectively, applied across 855,541 California victims.

**Successor liability doctrine is directly at issue.** Chrome Holding Co. and ChromeCo, Inc. are post-bankruptcy corporate successors, not the original 23andMe entity. The AG's choice to sue these entities tests whether state consumer protection liability survives bankruptcy restructuring in the genetic data context — a question with broad implications for DTC genetic testing companies generally.

**The bankruptcy sale raised unresolved genetic data governance questions.** Twenty-eight states challenged the bankruptcy sale process, arguing that genetic data cannot be commodified through bankruptcy proceedings under existing privacy frameworks. The AG enforcement action compounds legal exposure for the successor entities who now hold the original breach liability along with the underlying genetic database, per [Villanova Law analysis](https://www.villanova.edu/university/media/press-releases/2026/genetic-testing-bankruptcy.html) and [Loeb & Loeb analysis](https://www.loeb.com/en/insights/publications/2025/07/23andme-bankruptcy-sparks-data-privacy-concerns-should-it).

**It signals expanded state AG appetite for genetic privacy enforcement.** California's action follows a multistate coalition investigation and comes after 28 states intervened in the bankruptcy. State AGs across the country are actively developing genetic data enforcement programs. Companies operating DTC genetic testing services should expect coordinated multistate enforcement as the next phase.

**Industry-wide MFA and credential stuffing controls are now AG enforcement priorities.** The complaint is explicit that failing to implement MFA for high-sensitivity data violates a company's own stated security policies and applicable law. This is now an express enforcement position of the California AG.

## Action Items

- **DTC genetic testing companies** should immediately audit whether current security controls — including MFA, anomaly detection for bulk data queries, and API rate limiting — match the heightened standard required for genetic data under GIPA, the CCPA, and the Reasonable Data Security Law. Gaps should be remediated before a breach, not after.
- **Privacy and compliance counsel** should review the *People v. Chrome Holding* complaint (linked in Sources) for a detailed list of the specific failures alleged; use it as a checklist against current security programs.
- **Incident response teams** should revise breach communication protocols to ensure no public statements are issued that could be characterized as downplaying a breach's severity while ransom negotiations are occurring; the alleged 23andMe public denial while paying ransom is now a litigation-proven risk.
- **Bankruptcy practitioners and M&A counsel** advising acquirers of genetic data companies should assess successor liability exposure for pre-acquisition breaches, as this action makes clear that the California AG will pursue the surviving entity regardless of corporate restructuring.
- **Customers of Chrome Holding/23andMe** who are California residents and have not yet filed a claim under the $30 million class action settlement should note that the February 17, 2026 claim deadline has passed; the AG action seeks separate civil penalties and injunctive relief but does not replace the class settlement.
- **Companies with multistate DTC genetic testing operations** should engage specialized privacy counsel to assess exposure under analogous genetic privacy statutes in other states (e.g., Alabama's Genetic Data Privacy Act, Texas and Montana biometric/genetic data provisions).

## Related Reports

- [Alabama Enacts Genetic Data Privacy Act (HB 21): Consumer Protections for DTC Genetic Testing Companies](reports/privacy/alabama-genetic-data-privacy-act-hb21-2024-05-22.md) — Alabama's 2024 genetic data statute closely mirrors GIPA's framework and is the next most likely basis for a state AG action against DTC genetic testing companies following California's enforcement template.
- [California AG Launches CCPA Investigative Sweep Targeting Location Data Industry](reports/privacy/enforcement-actions/california-ag-location-data-sweep-2025-03-10.md) — Demonstrates the California AG's established pattern of using CCPA investigative sweeps as a precursor to enforcement litigation, the same trajectory followed in the 23andMe/Chrome Holding action.
- [CPPA Launches Data Broker Enforcement Era: Growbots Settlement and the Delete Act Compliance Imperative](reports/privacy/enforcement-actions/california-cppa-data-broker-delete-act-growbots-2025-03-13.md) — California's broader data broker and sensitive data enforcement environment within which the 23andMe AG action sits.

## Sources

1. [California AG Press Release: Bonta Sues Chrome Holding Co. (formerly 23andMe)](https://oag.ca.gov/news/press-releases/attorney-general-bonta-sues-chrome-holding-co-formerly-known-23andme-over-2023) — Official California DOJ announcement; primary source for complaint allegations, legal theories, and AG statement.
2. [People v. Chrome Holding Co. fka 23andMe — Stamped Complaint (PDF)](https://oag.ca.gov/system/files/attachments/press-docs/People%20v%20Chrome%20Holding%20fka%2023andMe%20et%20al.%20-%20Stamped%20Complaint.pdf) — Official complaint filed in San Francisco Superior Court; primary source for specific allegations, statutory violations, and remedies sought.
3. [BleepingComputer: California AG sues 23andMe over 2023 breach exposing health data](https://www.bleepingcomputer.com/news/security/california-ag-sues-23andme-over-2023-breach-exposing-health-data/) — Technical breach details including credential stuffing mechanism, MyHeritage connection, and DNA Relatives feature exploitation.
4. [The Register: Rob Bonta sues 23andMe's new owners over 2023 breach](https://www.theregister.com/legal/2026/05/29/rob-bonta-sues-23andmes-new-owners-over-2023-breach/) — Ransom payment allegations and successor liability framing.
5. [HIPAA Journal: California AG Files Lawsuit Over 23andMe Data Breach](https://www.hipaajournal.com/california-ag-23andme-data-breach-lawsuit/) — Overview of complaint allegations, settlement status, and class action context.
6. [HIPAA Journal: 23andMe Requests Bankruptcy Judge Approve Revised $50 Million Data Breach Settlement](https://www.hipaajournal.com/23andme-class-action-data-breach-settlement/) — Class action settlement background, bankruptcy court approval, and final approval on January 30, 2026.
7. [Lawfare: Privacy, Consent, and National Security After the 23andMe Bankruptcy](https://www.lawfaremedia.org/article/privacy--consent--and-national-security-after-the-23andme-bankruptcy) — Analysis of genetic data governance failures exposed by the bankruptcy, TTAM acquisition context.
8. [Loeb & Loeb: 23andMe Bankruptcy Sparks Data Privacy Concerns](https://www.loeb.com/en/insights/publications/2025/07/23andme-bankruptcy-sparks-data-privacy-concerns-should-it) — Law firm analysis of the genetic data sale in bankruptcy and successor liability issues.
9. [Villanova University: 23andMe Bankruptcy Exposes Fragility of Genetic Data Frameworks](https://www.villanova.edu/university/media/press-releases/2026/genetic-testing-bankruptcy.html) — Academic analysis of bioethics and policy gaps in genetic data bankruptcy proceedings.
10. [Michigan AG: Nessel Enters Multistate Legal Fight to Protect Genetic Information in 23andMe Bankruptcy](https://www.michigan.gov/ag/news/press-releases/2025/06/10/ag-nessel-enters-multistate-legal-fight-to-protect-genetic-information-in-23andme-bankruptcy-case) — Confirms 28-state coalition challenging genetic data transfer in bankruptcy.
11. [Hogan Lovells: State Attorneys General Data Breach Investigations: 23andMe in 2023, more in 2024](https://www.hoganlovells.com/en/publications/state-attorneys-general-data-breach-investigations-23andme-in-2023-more-in-2024) — Law firm analysis of the multistate AG coalition's pre-litigation investigation findings.
12. [National Law Review: California Enacts the Genetic Information Privacy Act](https://natlawreview.com/article/california-enacts-new-privacy-law-genetic-data) — Legislative history and requirements of GIPA (SB 41, effective January 1, 2022).
13. [Hinshaw & Culbertson: Privacy Law Essentials — California's Genetic Information Privacy Act](https://www.hinshawlaw.com/en/insights/privacy-cyber-and-ai-decoded-alert/privacy-law-essentials-californias-genetic-information-privacy-act) — Detailed GIPA requirements, consent framework, and penalty structure.
14. [ppc.land: California Sues 23andMe Over 7 Million Genetic Profiles Exposed in 2023 Breach](https://ppc.land/california-sues-23andme-over-7-million-genetic-profiles-exposed-in-2023-breach/) — CCPA and GIPA penalty ranges as alleged in the complaint.
15. [Engadget: California sues 23andMe over 2023 data breach that affected 7 million users](https://www.engadget.com/2183454/california-ag-sues-23andme-data-breach/) — Consumer-accessible summary confirming scope and breach timeline.
16. [23andMe Data Settlement Official Site](https://www.23andmedatasettlement.com/) — Official site for the $30 million class action settlement; confirms February 17, 2026 claim deadline.
