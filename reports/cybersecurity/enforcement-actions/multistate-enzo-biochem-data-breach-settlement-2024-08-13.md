---
title: "Multistate AG Settlement: Enzo Biochem Pays $4.5M Over 2023 Ransomware Data Breach"
date: 2024-08-13
jurisdiction: "New York"
category: "cybersecurity"
development_type: "enforcement"
finding_id: "SCAN-20240819-043"
topic_key: "new-york-b838c136-2024"
topic_type: "enforcement_action"
first_reported: 2024-08-19
last_updated: 2026-04-21
status_history: []
cluster: "Multistate AG Healthcare Data Breach Settlements and Enforcement"
cluster_slug: "multistate-ag-healthcare-data-breach-enforcement"
---

# Multistate AG Settlement: Enzo Biochem Pays $4.5M Over 2023 Ransomware Data Breach

**Jurisdiction:** New York, New Jersey, Connecticut | **Category:** Cybersecurity | **Date:** August 13, 2024

## Executive Summary [HIGH confidence]

On August 13, 2024, the attorneys general of New York, New Jersey, and Connecticut announced a coordinated $4.5 million settlement with biotechnology company Enzo Biochem, Inc. and its subsidiary Enzo Clinical Labs, Inc. over a 2023 ransomware attack that exposed the protected health information of approximately 2.4 million patients. The settlement — the largest state AG data security penalty of 2024 — resolves alleged violations of the HIPAA Security Rule, the HIPAA Breach Notification Rule, and state consumer protection and data security laws, including New York General Business Law (GBL) § 899-bb (the NY SHIELD Act). In addition to the financial penalty, Enzo agreed to implement a comprehensive corrective action plan covering multi-factor authentication, password governance, encryption at rest and in transit, annual risk assessments, and a formal incident response program. The action illustrates the willingness of state AGs to enforce HIPAA obligations under parallel state law authority — a trend with direct compliance significance for any covered entity or business associate operating in these jurisdictions.

## Background [HIGH confidence]

Enzo Biochem, Inc. is a New York-based life sciences and biotechnology company. Its subsidiary, Enzo Clinical Labs, Inc., operated diagnostic and clinical testing laboratories across New York until August 2023, when it sold its laboratory testing assets and exited the clinical laboratory business. At the time of the breach, Enzo Clinical Labs handled clinical test data for millions of patients, making it a covered entity subject to HIPAA's privacy and security requirements.

State attorneys general have held independent authority to bring civil actions under HIPAA since the Health Information Technology for Economic and Clinical Health (HITECH) Act of 2009 (Pub. L. 111-5, § 13410(e)), which allows state AGs to seek injunctive relief and civil monetary penalties on behalf of state residents. In New York specifically, the NY SHIELD Act (effective March 21, 2020) codified at [GBL § 899-bb](https://www.nysenate.gov/legislation/laws/GBL/899-BB) requires businesses that own or license computerized data including private information of New York residents to implement and maintain reasonable administrative, technical, and physical safeguards. Violations can be pursued by the NY AG under [GBL § 899-aa](https://www.nysenate.gov/legislation/laws/GBL/899-AA) and § 899-bb.

The multistate enforcement coalition reflects an established pattern of state AG coordination in large data security cases. New York typically leads investigations involving large numbers of resident victims, with other affected states joining under their own statutory authority.

## Detailed Analysis [HIGH confidence]

### The April 2023 Ransomware Attack

Between April 4 and April 6, 2023, threat actors accessed Enzo's network using two stolen employee login credentials. According to the [New York AG press release](https://ag.ny.gov/press-release/2024/attorney-general-james-secures-45-million-biotech-company-failing-protect-new), those credentials were shared among five Enzo employees, and one had not been changed in over ten years. The attackers accessed an Enzo database server used for analytics and reporting, exfiltrated approximately 1.4 terabytes of patient data relating to testing conducted between October 2012 and April 2023, and then deployed ransomware to encrypt Enzo's files.

Enzo did not detect the intrusion in real time. The company lacked automated systems for monitoring network traffic for anomalous behavior, meaning the breach was not discovered until several days after the initial compromise. Enzo disclosed the incident to the SEC via an 8-K filing on May 30, 2023. The total affected population reached approximately 2.47 million patients, including more than 1.4 million New York residents, approximately 193,000 Connecticut residents, and residents from other states as well.

The stolen data included patient names, addresses, dates of birth, phone numbers, Social Security numbers, and medical treatment and diagnosis information — categories that constitute both HIPAA-protected health information (PHI) and "private information" under state breach notification statutes.

### Security Deficiencies Identified

The multistate investigation, led by the New York OAG, identified a pattern of sustained security neglect. Key deficiencies included:

- **Credential sharing and stale passwords**: Two login credentials were shared among five employees; one had not been rotated in ten years. No multi-factor authentication (MFA) was in place for user accounts.
- **Failure to act on prior risk assessments**: A third-party HIPAA risk assessment conducted in 2021 — and an earlier assessment in 2017 — identified specific risks and recommended remediation steps that Enzo failed to implement. The 2021 assessment specifically recommended encrypting PHI at rest on servers and desktops, deploying automated anomaly detection, documenting policies and procedures, and formalizing risk management.
- **Inadequate encryption**: PHI on Enzo servers was not encrypted at rest, contrary to both HIPAA Security Rule standards (45 C.F.R. § 164.312(a)(2)(iv)) and the 2021 assessment's recommendations.
- **Absence of monitoring**: Enzo had no system for detecting suspicious network activity, delaying discovery of the breach by several days and allowing the exfiltration to proceed undetected.
- **Insufficient breach notification**: The AGs alleged that Enzo's breach notification letters failed to disclose all categories of compromised data, in violation of the HIPAA Breach Notification Rule (45 C.F.R. §§ 164.400-414).

According to [Norton Rose Fulbright's analysis](https://www.insidetechlaw.com/blog/2024/08/violation-of-hipaa-security-rule-violation-of-ny-shield-act), the AGs alleged violations of twelve specific provisions of the HIPAA Privacy, Security, and Breach Notification Rules.

### Legal Basis and Settlement Terms

**New York**: The NY AG entered an Assurance of Discontinuance (AOD) with Enzo Biochem, available at [ag.ny.gov](https://ag.ny.gov/sites/default/files/settlements-agreements/enzo-biochem-aod-2024.pdf). The AOD is premised on violations of HIPAA (enforced through HITECH state AG authority) and GBL § 899-bb (the NY SHIELD Act). New York receives $2,826,889.24 of the total settlement.

**New Jersey**: The NJ AG entered a Consent Order (formally executed August 8, 2024), available at [nj.gov](https://www.nj.gov/oag/newsreleases24/2024-0813_Enzo-NJ-Consent-Order-DCA-Executed.pdf). The NJ settlement is premised on violations of HIPAA and the New Jersey Consumer Fraud Act (N.J.S.A. 56:8-1 et seq.). New Jersey receives approximately $930,000.

**Connecticut**: Connecticut AG William Tong, per the [CT AG press release](https://portal.ct.gov/ag/press-releases/2024-press-releases/attorney-general-tong-joins-multistate-coalition-to-secure-4-5-million), participated as part of the multistate coalition. Connecticut receives $743,110.76.

### Corrective Action Plan

Beyond the financial penalty, Enzo agreed to implement the following security measures going forward:

1. Maintain a comprehensive information security program protecting the confidentiality, integrity, and availability of personal and health information.
2. Implement and maintain policies limiting access to personal information on a need-to-know basis.
3. Implement and maintain multi-factor authentication for all user accounts.
4. Establish and maintain password policies requiring strong, complex passwords and periodic rotation.
5. Encrypt all personal information, whether stored at rest or transmitted in transit.
6. Conduct and document annual risk assessments.
7. Develop, implement, and maintain a written incident response plan.

These requirements mirror HIPAA Security Rule administrative, physical, and technical safeguards (45 C.F.R. Part 164, Subpart C) and align with the NY SHIELD Act's "reasonable safeguards" standard under GBL § 899-bb(2)(b).

## Impact Assessment [MEDIUM confidence]

### Affected Industries

The settlement is directly relevant to any entity that:
- Qualifies as a HIPAA covered entity (healthcare providers, health plans, healthcare clearinghouses) or business associate;
- Holds personal health or biometric information of New York, New Jersey, or Connecticut residents; or
- Is subject to the NY SHIELD Act (any business that owns or licenses private information of New York residents, regardless of where the business is located).

Clinical laboratories, reference labs, genomic testing companies, and health IT vendors face heightened exposure given the combination of large patient data volumes and the AGs' demonstrated willingness to enforce HIPAA directly.

### The NY SHIELD Act as HIPAA Parallel

A significant doctrinal feature of this settlement is the NY OAG's use of GBL § 899-bb as a parallel enforcement vehicle for HIPAA Security Rule violations. As [Norton Rose Fulbright observed](https://www.insidetechlaw.com/blog/2024/08/violation-of-hipaa-security-rule-violation-of-ny-shield-act), the NY AG treated Enzo's HIPAA violations as per se violations of the SHIELD Act's "reasonable safeguards" obligation. This approach means that HIPAA-covered entities operating in New York face state AG enforcement independently of any federal HHS/OCR action. The $2.8 million New York share — far larger than OCR's typical resolution for comparable cases — signals that state AG enforcement can impose materially greater financial risk than federal HIPAA enforcement alone.

### Enforcement Outlook

This action is part of a broader multi-year trend of state AG enforcement in the healthcare data security space. The $4.5 million combined penalty was described by analysts at [HIPAA Journal](https://www.hipaajournal.com/enzo-biochem-hipaa-settlement-ny-nj-ct/) as the largest state AG data security penalty imposed in 2024. Separately, Enzo also faced a private class action that settled for $7.5 million in January 2025, demonstrating the layered liability exposure — federal regulatory, multistate AG, and private class action — that follows large health data breaches.

The Enzo settlement follows other high-profile state AG healthcare enforcement actions, including the NY AG's earlier actions involving 23andMe and various hospital network breaches, as well as the [Blackbaud data breach litigation](reports/cybersecurity/enforcement-actions/south-carolina-blackbaud-data-breach-class-cert-denied-2024-06-04.md) involving similar vendor-side failures.

## Action Items

- Audit credential management practices immediately: eliminate shared login credentials, enforce MFA for all user accounts, and mandate password rotation policies consistent with NIST SP 800-63B guidelines.
- Implement or review encryption-at-rest for all PHI and private information held on organizational servers, workstations, and portable media; document compliance with HIPAA 45 C.F.R. § 164.312(a)(2)(iv).
- Review outstanding findings from the most recent HIPAA risk assessment and prioritize remediation of open items — regulators treat unaddressed assessment findings as aggravating evidence of willful neglect.
- Deploy automated network monitoring and anomaly detection systems to reduce dwell time and support timely breach detection obligations under HIPAA 45 C.F.R. § 164.308(a)(1)(ii)(D).
- Ensure breach notification letters disclose all categories of compromised data as required by HIPAA 45 C.F.R. § 164.410(c) and applicable state statutes.
- Assess NY SHIELD Act exposure: any business holding private information of New York residents should confirm its information security program meets GBL § 899-bb's "reasonable safeguards" standard, particularly if already subject to HIPAA.
- Review New Jersey Consumer Fraud Act and Connecticut data security obligations if operating in those states or holding resident data.

## Related Reports

- [reports/cybersecurity/enforcement-actions/south-carolina-blackbaud-data-breach-class-cert-denied-2024-06-04.md](reports/cybersecurity/enforcement-actions/south-carolina-blackbaud-data-breach-class-cert-denied-2024-06-04.md) — Both actions involve vendor-side healthcare data breaches and examine the intersection of HIPAA obligations and state-law enforcement theories.
- [reports/cybersecurity/standards-guidance/new-york-dfs-ai-cybersecurity-guidance-2024-10-16.md](reports/cybersecurity/standards-guidance/new-york-dfs-ai-cybersecurity-guidance-2024-10-16.md) — New York DFS cybersecurity guidance issued in the same enforcement cycle, relevant to covered entities operating under New York regulatory frameworks.
- [reports/cybersecurity/incident-reporting/new-york-data-breach-notification-2025-01-15.md](reports/cybersecurity/incident-reporting/new-york-data-breach-notification-2025-01-15.md) — New York's breach notification requirements, the state-law framework alongside which GBL § 899-bb security obligations operate.

## Sources

1. [NY AG Press Release — AG James Secures $4.5 Million from Enzo Biochem (Aug. 13, 2024)](https://ag.ny.gov/press-release/2024/attorney-general-james-secures-45-million-biotech-company-failing-protect-new) — Official announcement from the New York Office of the Attorney General; primary source for settlement terms, penalty allocation, and security failure findings.
2. [NY AG Assurance of Discontinuance — Enzo Biochem (2024)](https://ag.ny.gov/sites/default/files/settlements-agreements/enzo-biochem-aod-2024.pdf) — Official settlement document from the New York AG; source for legal basis and AOD terms. Note: PDF retrieval was not attempted at time of writing; this URL is provided for manual verification.
3. [NJ AG Consent Order — In the Matter of Enzo Biochem, Inc. (Aug. 8, 2024)](https://www.nj.gov/oag/newsreleases24/2024-0813_Enzo-NJ-Consent-Order-DCA-Executed.pdf) — Official NJ consent order; source for NJ-specific penalty and legal basis. Note: PDF retrieval was not attempted at time of writing; URL provided for manual verification.
4. [NJ AG Press Release — Attorney General Platkin Secures $4.5 Million from Enzo Biochem (Aug. 13, 2024)](https://www.njoag.gov/attorney-general-platkin-and-multistate-coalition-secure-4-5-million-from-enzo-biochem-for-failing-to-protect-health-data/) — Official NJ AG announcement; confirms NJ penalty share and corrective action requirements.
5. [CT AG Press Release — AG Tong Joins Multistate Coalition to Secure $4.5 Million (Aug. 13, 2024)](https://portal.ct.gov/ag/press-releases/2024-press-releases/attorney-general-tong-joins-multistate-coalition-to-secure-4-5-million) — Official CT AG announcement; confirms CT penalty share ($743,110.76) and affected CT residents (193,000+).
6. [HIPAA Journal — Enzo Biochem Settles HIPAA Violations with State AGs for $4.5 Million](https://www.hipaajournal.com/enzo-biochem-hipaa-settlement-ny-nj-ct/) — Detailed secondary analysis of HIPAA violations alleged, corrective action plan, and enforcement context; characterizes the penalty as the largest state AG data security penalty of 2024.
7. [Norton Rose Fulbright / Inside Tech Law — Violation of HIPAA Security Rule = Violation of NY SHIELD Act](https://www.insidetechlaw.com/blog/2024/08/violation-of-hipaa-security-rule-violation-of-ny-shield-act) — Law firm client alert analyzing the NY AG's doctrinal approach of treating HIPAA violations as per se NY SHIELD Act violations; key secondary source for legal theory section.
8. [Brach Eichler — NJ, NY and CT Attorneys General Settle Biotech Company Data Breach for $4.5M](https://www.bracheichler.com/insights/nj-ny-and-ct-attorneys-general-settle-biotech-company-data-breach-for-4-5m/) — NJ law firm analysis with NJ-specific compliance context and state statutory background.
9. [Recorded Future News (The Record) — Biotech company hacked in 2023 pays states $4.5 million over breached data](https://therecord.media/enzo-biotech-company-pays-states-over-2023-breach) — News coverage confirming breach timeline and scale; corroboration of 2.4 million patient figure.
10. [TechTarget HealthTech Security — Enzo Biochem pays $4.5M for health data security failures](https://www.techtarget.com/healthtechsecurity/news/366605474/Enzo-Biochem-pays-45M-for-health-data-security-failures) — Technical news analysis of security deficiencies identified in the investigation.
11. [National Law Review — Biotech Company Settles with Three State AGs Over Security Practices](https://natlawreview.com/article/biotech-company-settles-three-state-ags-over-security-practices) — Law review summary with HIPAA regulatory framework context.
12. [HIPAA Journal — Enzo Biochem Settles Ransomware Class Action for $7.5 Million](https://www.hipaajournal.com/enzo-biochem-class-action-data-breach-settlement/) — Source for the parallel class action settlement ($7.5 million, January 2025), illustrating layered liability exposure.
13. [NY GBL § 899-bb (NY SHIELD Act)](https://www.nysenate.gov/legislation/laws/GBL/899-BB) — Official statutory text of the New York Stop Hacks and Improve Electronic Data Security Act.
