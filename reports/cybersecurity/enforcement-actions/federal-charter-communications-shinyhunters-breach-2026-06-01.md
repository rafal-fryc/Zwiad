---
title: "Cyberattack on Charter Communications Breaches Data on 4.9 Million Accounts"
date: 2026-06-01
jurisdiction: "Federal"
category: "cybersecurity"
development_type: "enforcement"
finding_id: "SCAN-20260615-002"
topic_key: "federal-b4be979c-2026"
topic_type: "enforcement"
first_reported: 2026-06-01
last_updated: 2026-06-15
status_history: []
cluster: "Charter Communications (Spectrum) ShinyHunters Data Breach (2026)"
cluster_slug: "charter-communications-spectrum-shinyhunters-breach-2026"
---

# Cyberattack on Charter Communications Breaches Data on 4.9 Million Accounts

**Jurisdiction:** Federal | **Category:** Cybersecurity | **Date:** 2026-06-01

## Summary [MEDIUM confidence]

Charter Communications, the telecom and cable company operating the Spectrum brand, suffered a significant data breach originating on April 1, 2026 when the ShinyHunters threat group executed a voice phishing (vishing) attack that compromised an employee's Microsoft Entra credentials and enabled unauthorized access to Charter's Salesforce CRM environment. After Charter refused to pay a ransom, ShinyHunters leaked the stolen data publicly on May 27, 2026. Have I Been Pwned has confirmed that 4.9 million unique accounts were exposed; ShinyHunters claims the actual theft reached 42 million records. The breach triggers FCC CPNI notification obligations, multi-state breach notification laws, and SEC cybersecurity disclosure rules, and Charter now faces at least four federal class-action suits in Connecticut.

## Key Facts [MEDIUM confidence]

- **Attack vector — vishing and credential hijacking:** On April 1, 2026, threat actors used a voice phishing call to trick a Charter employee into surrendering Microsoft Entra (Azure AD) account credentials; no software vulnerability was exploited. The compromised identity account was then used to authenticate into Charter's Salesforce CRM instance, from which customer records were exported. ([BleepingComputer](https://www.bleepingcomputer.com/news/security/charter-confirms-data-breach-after-shinyhunters-extortion-threat/); [TechJack Solutions](https://techjacksolutions.com/scc-intel/shinyhunters-breaches-charter-communications-via-vishing-and-salesforce-exfiltration-exposing-4-9m-accounts/))

- **Attacker identity — ShinyHunters:** ShinyHunters, a prolific financially-motivated cybercrime group previously associated with major breaches including Ticketmaster and Snowflake-linked victims, claimed credit for the Charter intrusion. ([TechRepublic](https://www.techrepublic.com/article/news-charter-shinyhunters-cyber-incident/); [CyberInsider](https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/))

- **Ransom demand and leak:** ShinyHunters posted a May 27, 2026 deadline for Charter to open ransom negotiations or see the data published publicly. Charter declined to pay, and the data was subsequently published on the group's dark web leak site. ([BleepingComputer](https://www.bleepingcomputer.com/news/security/charter-communications-data-breach-affects-49-million-accounts/))

- **Confirmed scope — 4.9 million accounts:** Have I Been Pwned analyzed the leaked dataset and confirmed 4.9 million unique email addresses, along with associated names, phone numbers, and physical addresses were exposed. Approximately 85,000 records from an internal employee directory also included job titles. ([Have I Been Pwned](https://haveibeenpwned.com/Breach/Charter); [SecurityWeek](https://www.securityweek.com/charter-communications-data-breach-could-impact-nearly-5-million/))

- **Disputed total scale — ShinyHunters claims 42 million:** ShinyHunters asserted the full exfiltration reached 42 million records from Charter's Salesforce environment, including consumer and business customer names, email addresses, physical addresses, phone numbers, plan information, customer support ticket data, and some Customer Proprietary Network Information (CPNI). Cybernews independently estimated at least 13 million individuals may have been exposed. ([Techlicious](https://www.techlicious.com/blog/spectrum-charter-data-breach-shinyhunters-2026/); [SafeState](https://www.safestate.com/post/charter-communications-data-breach-exposes-42-million-records))

- **Charter's position — no CPNI or sensitive PI exfiltrated:** Charter confirmed the incident but stated: "No sensitive personal information (PI) or customer proprietary network information (CPNI) data was exfiltrated by the threat actor as a result of recent activity." Charter stated only sales tools used to manage current, past, and prospective business customers were impacted. ([BleepingComputer](https://www.bleepingcomputer.com/news/security/charter-communications-data-breach-affects-49-million-accounts/))

- **Public disclosure date:** The breach originated April 1, 2026 but was not publicly disclosed until May 27, 2026 — approximately eight weeks after the intrusion began. ([BreachSense](https://www.breachsense.com/breaches/charter-communications-data-breach/))

- **SEC 8-K filing:** Charter Communications filed a Form 8-K with the SEC disclosing the cyber incident. ([SEC EDGAR](https://www.sec.gov/Archives/edgar/data/0001091667/000109166726000024/chtr-20260421.htm))

- **Class-action litigation:** At least four federal class-action complaints were filed in Connecticut federal court following public disclosure, including a complaint filed June 1, 2026 by plaintiff Mariah Kent. The suits allege Charter failed to implement reasonable data security measures. ([Scott+Scott](https://scott-scott.com/consumer-cases/charter-communications-data-breach/); [Chimicles Schwartz](https://chimicles.com/charter-communications-data-breach/); [Rosen Law](https://rosenlegal.com/case/charter-communications-inc/))

## Regulatory Exposure [HIGH confidence]

### FCC CPNI Notification Obligations

As a telecommunications carrier, Charter is subject to the FCC's data breach reporting rules under [47 CFR § 64.2011](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-U/section-64.2011) and the [2024 Data Breach Reporting Requirements Order](https://www.federalregister.gov/documents/2024/02/12/2024-01667/data-breach-reporting-requirements) (effective March 13, 2024, as upheld by the [Sixth Circuit on August 13, 2025](https://www.mondaq.com/unitedstates/telecoms-mobile-cable-communications/1670614/sixth-circuit-upholds-fccs-2024-breach-notification-rules)):

- **Law enforcement notification:** Carriers must notify the FBI and U.S. Secret Service within seven (7) business days of reasonable determination of a breach. Given the confirmed scope of 4.9 million accounts, this threshold is unambiguously met.
- **Customer notification:** Carriers must notify affected customers promptly, with a maximum 30-day delay from determination of the breach. The FCC must also be notified under the 2024 rules.
- **CPNI vs. PII distinction:** Charter's denial that CPNI was exfiltrated is legally significant. FCC enforcement exposure under CPNI-specific rules is reduced if Charter's forensic conclusion holds. However, the 2024 rules expanded FCC jurisdiction to cover PII breaches more broadly. The data confirmed exposed (names, email addresses, phone numbers, physical addresses) constitutes PII regardless of CPNI status.

Charter's eight-week gap between intrusion (April 1) and public disclosure (May 27) raises FCC notification timeline compliance questions that regulators and class-action plaintiffs are likely to scrutinize.

### Multi-State Breach Notification Laws

The 4.9 million affected accounts span Charter's nationwide Spectrum subscriber base across all 50 states and Washington DC. Every US state has enacted a data breach notification statute. Key obligations include:

- **California:** California Customer Records Act (Cal. Civ. Code § 1798.80 et seq.) and CCPA. California requires notification in the most expedient time possible without unreasonable delay.
- **New York:** SHIELD Act (Gen. Bus. Law § 899-aa). New York requires notification in the most expedient time possible.
- **Multistate enforcement precedent:** The [Enzo Biochem multistate settlement](../multistate-enzo-biochem-data-breach-settlement-2024-08-13.md) — a $7.5 million resolution involving multiple state AGs — illustrates the enforcement pathway for multi-jurisdiction breach notification failures.

### SEC Cybersecurity Incident Disclosure

Charter's Form 8-K filing reflects the SEC's cybersecurity incident disclosure requirements under the SEC's 2023 cybersecurity disclosure rules (17 CFR Parts 229 and 249), which require material cybersecurity incident disclosure within four business days of determination of materiality. The eight-week internal discovery-to-public-disclosure gap will be examined for compliance.

## Action Items

- **Assess FCC notification compliance now:** Any organization that is a telecommunications carrier should confirm whether its CPNI breach notification procedures under 47 CFR § 64.2011 include the FBI/USSS seven-day law enforcement notification, updated FCC notification, and the 30-day customer notification maximum. The Charter breach timeline is a live illustration of the FCC's enforcement trigger.

- **Audit identity and access management for SaaS platforms:** The ShinyHunters vishing attack that compromised a Microsoft Entra account without exploiting any software vulnerability is a textbook illustration of the risk from absent or bypassable phishing-resistant MFA. Organizations should implement FIDO2/WebAuthn or hardware security key MFA on all identity provider (IdP) accounts that gate access to CRM and customer data environments.

- **Evaluate Salesforce CRM data minimization:** Charter's Salesforce instance held the customer records that were exfiltrated. Organizations should audit what customer PII and CPNI is retained in CRM instances, apply least-privilege access controls, and enable Salesforce audit trail logging and anomaly detection.

- **Review vishing/social engineering response playbooks:** The attack vector here was human — a fraudulent phone call. Organizations should implement call-back verification procedures for any request to provide or reset credentials, and run tabletop exercises simulating vishing scenarios targeting help desk and IT staff.

- **Monitor the CPNI dispute's regulatory resolution:** If regulators or forensic investigators find that CPNI was exfiltrated contrary to Charter's denial, enforcement under FCC CPNI rules would follow. Track developments in the Connecticut class-action docket and any FCC inquiry for authoritative resolution of the disputed scope.

- **Telecom operators should confirm 2024 FCC rule compliance:** The Sixth Circuit's August 2025 ruling upholding the 2024 data breach notification rules removed the last major legal challenge. All telecom carriers should confirm their notification procedures comply with the expanded 2024 requirements, including the new FCC notification obligation.

## Related Reports

- [Federal CIRCIA Final Rule Delay](../incident-reporting/federal-circia-final-rule-delay-2026-04-07.md) — CIRCIA's federal cyber incident reporting framework is the parallel regulatory regime to the FCC's CPNI breach rules; the delay context is relevant to understanding the current federal breach notification landscape.
- [Multistate Enzo Biochem Data Breach Settlement](../enforcement-actions/multistate-enzo-biochem-data-breach-settlement-2024-08-13.md) — This $7.5 million multistate AG settlement provides direct precedent for multi-jurisdiction enforcement exposure Charter may face.
- [New York DFS Delta Dental MOVEit Settlement](../enforcement-actions/new-york-dfs-delta-dental-moveit-settlement-2026-04-30.md) — Illustrates state-level enforcement action against an organization breached via a third-party supply chain attack; comparable enforcement trajectory to Charter.

## Sources

1. [BleepingComputer — Charter Communications data breach affects 4.9 million accounts](https://www.bleepingcomputer.com/news/security/charter-communications-data-breach-affects-49-million-accounts/) — Primary incident coverage; confirmed scope of 4.9M accounts and Charter's official statement.
2. [BleepingComputer — Charter confirms data breach after ShinyHunters extortion threat](https://www.bleepingcomputer.com/news/security/charter-confirms-data-breach-after-shinyhunters-extortion-threat/) — Details on ShinyHunters ransom deadline and data leak publication.
3. [SecurityWeek — Charter Communications Data Breach Could Impact Nearly 5 Million](https://www.securityweek.com/charter-communications-data-breach-could-impact-nearly-5-million/) — Technical analysis and breach impact scope.
4. [TechRepublic — ShinyHunters Alleges 42M Records Stolen from Charter Communications](https://www.techrepublic.com/article/news-charter-shinyhunters-cyber-incident/) — ShinyHunters' claims and 42M record assertion.
5. [CyberInsider — Charter Communications confirms data breach as hackers threaten leak of 42 million records](https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/) — Charter's confirmation and threat actor background.
6. [Techlicious — Charter confirms Spectrum data breach: 13 million customers exposed](https://www.techlicious.com/blog/spectrum-charter-data-breach-shinyhunters-2026/) — Independent estimate of 13M exposed customers.
7. [TechJack Solutions — ShinyHunters Breaches Charter Communications via Vishing and Salesforce Exfiltration](https://techjacksolutions.com/scc-intel/shinyhunters-breaches-charter-communications-via-vishing-and-salesforce-exfiltration-exposing-4-9m-accounts/) — Technical breakdown of attack chain: vishing → Entra compromise → Salesforce exfiltration.
8. [Have I Been Pwned — Charter Data Breach](https://haveibeenpwned.com/Breach/Charter) — Independent breach data verification confirming 4.9M unique email addresses.
9. [SafeState — Charter Communications Data Breach Exposes 42 Million Records](https://www.safestate.com/post/charter-communications-data-breach-exposes-42-million-records) — Analysis of full ShinyHunters claim regarding 42M records.
10. [BreachSense — Charter Communications Data Breach in 2026](https://www.breachsense.com/breaches/charter-communications-data-breach/) — Timeline and breach database entry confirming April 1 intrusion, May 27 public disclosure.
11. [SEC EDGAR — Charter Communications Form 8-K FY2026](https://www.sec.gov/Archives/edgar/data/0001091667/000109166726000024/chtr-20260421.htm) — Official SEC cybersecurity incident disclosure filing by Charter Communications.
12. [Scott+Scott — Charter Communications Data Breach](https://scott-scott.com/consumer-cases/charter-communications-data-breach/) — Class-action filing tracking; at least four suits in Connecticut federal court.
13. [Chimicles Schwartz — Charter Communications Data Breach Investigation](https://chimicles.com/charter-communications-data-breach/) — Class-action investigation; security failure allegations.
14. [Rosen Law — Charter Communications, Inc. Class Action Lawsuit](https://rosenlegal.com/case/charter-communications-inc/) — Additional class-action filing against Charter.
15. [ComplianceHub.Wiki — Charter Spectrum Breach: ShinyHunters, ISP Regulatory Obligations](https://compliancehub.wiki/charter-spectrum-shinyhunters-salesforce-breach-isp-regulatory-2026/) — Regulatory analysis of FCC CPNI obligations and Charter's denial strategy.
16. [ComplianceHub.Wiki — Spectrum Class Action: CPNI Question Charter Faces](https://compliancehub.wiki/spectrum-charter-data-breach-class-action-40-million/) — CPNI regulatory exposure analysis in class-action context.
17. [eCFR — 47 CFR § 64.2011, Notification of CPNI Security Breaches](https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-U/section-64.2011) — Official FCC rule text governing CPNI breach notification requirements for telecommunications carriers.
18. [Federal Register — FCC Data Breach Reporting Requirements (2024)](https://www.federalregister.gov/documents/2024/02/12/2024-01667/data-breach-reporting-requirements) — Official text of 2024 FCC rule expanding breach reporting to cover PII beyond CPNI, effective March 13, 2024.
19. [Mondaq — Sixth Circuit Upholds FCC's 2024 Breach Notification Rules](https://www.mondaq.com/unitedstates/telecoms-mobile-cable-communications/1670614/sixth-circuit-upholds-fccs-2024-breach-notification-rules) — August 2025 Sixth Circuit ruling confirming validity of 2024 FCC notification requirements.
20. [Captain Compliance — Charter Cyberattack Exposes 4.9 Million Accounts](https://captaincompliance.com/education/charter-cyberattack-exposes-4-9-million-accounts-as-employee-credential-attacks-hit-major-companies/) — Broader analysis of credential-based attacks on major companies in 2026.
