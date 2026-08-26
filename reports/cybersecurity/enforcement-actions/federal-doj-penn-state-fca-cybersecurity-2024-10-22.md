---
title: "Penn State Pays $1.25 Million to Resolve DOJ False Claims Act Cybersecurity Allegations"
date: 2024-10-22
jurisdiction: "Federal"
category: "cybersecurity"
development_type: "enforcement"
finding_id: "SCAN-20241106-007"
topic_key: "DOJ-UPDATE-PENN-STATE-2024"
topic_type: "enforcement_action"
first_reported: 2024-11-06
last_updated: 2026-04-22
status_history: []
cluster: "DOJ Civil Cyber-Fraud Initiative (CCFI): False Claims Act Cybersecurity Enforcement"
cluster_slug: "doj-civil-cyber-fraud-initiative-fca-enforcement"
---

# Penn State Pays $1.25 Million to Resolve DOJ False Claims Act Cybersecurity Allegations

**Jurisdiction:** Federal, Pennsylvania | **Category:** Cybersecurity | **Date:** 2024-10-22

## Executive Summary [HIGH confidence]

On October 22, 2024, the [U.S. Department of Justice](https://www.justice.gov/usao-edpa/pr/penn-state-agrees-pay-125-million-resolve-false-claims-act-allegations-relating-non) announced that Pennsylvania State University (Penn State) agreed to pay $1,250,000 to resolve allegations that it failed to comply with contractual cybersecurity requirements on fifteen Department of Defense (DoD) and NASA contracts and subcontracts, in violation of the False Claims Act (FCA). The case was initiated by a then-serving Chief Information Officer at Penn State's Applied Research Laboratory who filed a qui tam whistleblower complaint in October 2022 while still employed at ARL. The settlement represents the latest enforcement action under the [DOJ's Civil Cyber-Fraud Initiative (CCFI)](https://www.justice.gov/archives/opa/pr/pennsylvania-state-university-agrees-pay-125m-resolve-false-claims-act-allegations-relating), which launched in October 2021, and signals sustained DOJ intent to use FCA liability as a lever for cybersecurity compliance among federal contractors and research universities. The Penn State resolution is noteworthy for extending enforcement scrutiny to two previously underemphasized compliance dimensions: adequacy of Plans of Action and Milestones (POA&Ms) and cloud service provider (CSP) compliance with FedRAMP Moderate baseline requirements.

## Background [HIGH confidence]

### The False Claims Act as a Cybersecurity Enforcement Tool

The FCA, 31 U.S.C. §§ 3729–3733, imposes civil liability on any person who knowingly submits false or fraudulent claims for payment to the federal government. The statute's qui tam provisions allow private relators — often current or former employees — to sue on the government's behalf and share in any recovery. In October 2021, the DOJ [formally launched the Civil Cyber-Fraud Initiative](https://www.fcacounsel.com/blog/doj-civil-cyber-fraud-initiative/), directing the Civil Fraud Section's Commercial Litigation Branch to prioritize cybersecurity non-compliance by contractors and grantees as actionable FCA violations. The initiative targets entities that "knowingly provide deficient cybersecurity products or services, knowingly misrepresent their cybersecurity practices or protocols, or knowingly violate their obligations to monitor and report cybersecurity incidents."

Since its launch, the CCFI has yielded recoveries exceeding $28 million across multiple settlements. Prior notable actions included a $930,000 settlement with Comprehensive Health Services in March 2022 for failure to secure medical data at overseas government facilities; a $4.09 million settlement with Verizon Business Network Services in 2023 for deficient controls in a managed federal network service; and, in 2024, a $2.7 million settlement with a staffing firm over COVID-19 contact tracing data and an $11.3 million combined resolution against two consulting firms over deficient cybersecurity in a federal rental assistance platform. By year-end 2024, the CCFI had [recovered approximately $14 million in the calendar year alone](https://www.globalinvestigations.blog/uncategorized/dojs-false-claims-act-based-civil-cyber-fraud-initiative-in-2024/), making it the initiative's most productive year to date.

### Regulatory Framework: DFARS and NIST SP 800-171

The specific cybersecurity requirements at issue in the Penn State case derive from the Defense Federal Acquisition Regulation Supplement (DFARS) and corresponding NASA regulations:

- **DFARS 252.204-7012** — "Safeguarding Covered Defense Information and Cyber Incident Reporting." This clause, incorporated into DoD contracts since 2016, requires contractors to implement the [110 security controls in NIST Special Publication 800-171](https://www.acquisition.gov/dfars/252.204-7012-safeguarding-covered-defense-information-and-cyber-incident-reporting.) to protect Controlled Unclassified Information (CUI) on covered contractor information systems. It also mandates that cloud services used to process CUI must meet [FedRAMP Moderate baseline requirements](https://www.acquisition.gov/dfars/252.204-7012-safeguarding-covered-defense-information-and-cyber-incident-reporting.) or equivalent.
- **DFARS 252.204-7019** — "Notice of NIST SP 800-171 DoD Assessment Requirements." This clause [required contractors to conduct self-assessments](https://www.acquisition.gov/dfars/252.204-7019-notice-nistsp-800-171-dod-assessment-requirements.) of their NIST SP 800-171 compliance and submit scores to the DoD Supplier Performance Risk System (SPRS).
- **DFARS 252.204-7020** — "NIST SP 800-171 DoD Assessment Requirements." This clause [required higher-level assessment and reporting](https://www.acquisition.gov/dfars/252.204-7020-nist-sp-800-171dod-assessment-requirements.) to SPRS, including submission of a current assessment score, prior to contract award and periodically thereafter.
- **NASA FAR Supplement (FARS) 1852.204-76** — NASA's parallel clause requiring contractors to secure unclassified IT resources handling NASA-sensitive information.

NIST SP 800-171 itself organizes 110 security requirements across 14 control families covering areas such as access control, audit and accountability, incident response, maintenance, risk assessment, and system and communications protection. Compliance has been contractually mandated across DoD acquisitions (except COTS items) since the DFARS clauses took effect. Contractors that identify gaps are required to document them in POA&Ms with concrete timelines for remediation.

### Universities Under DOJ's Crosshairs

Research universities occupy a structurally exposed position in the CCFI enforcement landscape: they hold billions of dollars in federal research contracts and grants, maintain large, decentralized IT environments, and handle substantial volumes of CUI generated in defense and NASA-sponsored research programs. The Penn State case was not the first to target a university. In February 2024, the DOJ intervened in a qui tam case against the [Georgia Tech Research Corporation (GTRC)](https://www.justice.gov/opa/pr/georgia-tech-research-corporation-agrees-pay-875000-resolve-civil-cyber-fraud-litigation) — its first CCFI litigation intervention — alleging that Georgia Tech failed to deploy required security controls on DoD contract systems, including operating an unreviewed system security plan and failing to install antivirus software on certain laboratory computers. The DOJ filed a complaint-in-intervention in the Georgia Tech matter in August 2024, meaning both university cases were active simultaneously in late 2024 when Penn State settled. Georgia Tech ultimately settled for $875,000 in September 2025 — approximately 11 months after the Penn State resolution — reinforcing that research universities remain a sustained CCFI priority.

## Detailed Analysis [HIGH confidence]

### The Qui Tam Complaint and Timeline

On October 5, 2022, Matthew Decker, then-serving Chief Information Officer for Penn State's Applied Research Laboratory (ARL), filed a qui tam complaint in the U.S. District Court for the Eastern District of Pennsylvania under seal. Decker was still actively employed as ARL CIO at the time of filing — he served in that role from November 2015 through March 2023 — making this an insider whistleblower action brought by a current employee with direct visibility into ARL's compliance posture. The complaint alleged that Penn State had failed to implement required NIST SP 800-171 controls across a multi-year period spanning at least January 2018 through November 2023. The DOJ investigated the allegations and reached a settlement agreement with Penn State on October 22, 2024 — approximately two years after the complaint was filed. Decker received $250,000, representing 20% of the $1.25 million settlement, as his relator's share under the FCA's qui tam provisions.

### Scope of the Alleged Violations

The settlement encompasses [fifteen contracts and subcontracts](https://www.insidegovernmentcontracts.com/2024/11/penn-state-agrees-to-pay-1-25m-in-settlement-for-cybersecurity-non-compliance-false-claims-act-allegations/) with DoD and NASA. The government's allegations against Penn State break down into three distinct categories:

**1. Failure to Implement Required NIST SP 800-171 Controls**

Penn State allegedly failed to implement a subset of the 110 NIST SP 800-171 security controls required under DFARS 252.204-7008 and 252.204-7012 across covered systems handling CUI. This is the foundational violation common to most CCFI enforcement actions: contractors are required to achieve full implementation of these controls, and gaps must be remediated per documented timelines.

**2. Misrepresentation of Assessment Scores and POA&M Timelines**

This element distinguishes the Penn State case from prior CCFI settlements. Under DFARS 252.204-7019(d) and 252.204-7020(d), contractors submit self-assessment scores to DoD's SPRS database. Penn State submitted scores that reflected existing implementation gaps — which is permitted — but the settlement alleges that Penn State [misrepresented the timelines by which it expected to implement required controls](https://www.governmentcontractslegalforum.com/2024/11/articles/government-contracts/allegations-of-a-litany-of-lyin-penn-state-settles-claims-of-cybersecurity-noncompliance/) and failed to adequately document and actively pursue POA&Ms to achieve compliance. In other words, Penn State disclosed gaps but then did not follow through with credible remediation plans, and allegedly misrepresented its implementation progress. DOJ analysts noted this is the [first CCFI settlement to focus explicitly on POA&M adequacy](https://www.wiley.law/alert-DOJ-Continues-Crackdown-on-Cybersecurity-Compliance-with-FCA-Settlement) — establishing that the government regards inaccurate or dormant POA&Ms as independently actionable FCA fraud.

**3. Failure to Use FedRAMP-Compliant Cloud Service Providers**

For some contracts, Penn State allegedly failed to route CUI through external Cloud Service Providers (CSPs) that meet FedRAMP Moderate baseline requirements, as mandated by DFARS 252.204-7012. This is another first for CCFI: the DOJ had not previously included CSP non-compliance as a standalone element in an FCA cybersecurity settlement. Law firm analyses [noted that the CSP allegation signals the government's intent](https://www.crowell.com/en/insights/client-alerts/allegations-of-a-litany-of-lyin-penn-state-settles-claims-of-cybersecurity-noncompliance) to scrutinize cloud infrastructure choices — not merely the implementation of security controls — as part of its enforcement posture.

### Significance Within the CCFI Enforcement Trajectory

The Penn State settlement arrived contemporaneously with two other significant CCFI-adjacent developments in late 2024:

- **CMMC Final Rule (October 2024):** The DoD published the final rule for the [Cybersecurity Maturity Model Certification (CMMC) program](https://www.feldesman.com/penn-state-settlement-demonstrates-governments-continued-focus-on-cybersecurity-compliance/) under 32 C.F.R. Part 170, effective December 16, 2024. CMMC formalizes third-party assessment and certification of NIST SP 800-171 compliance as a condition for DoD contract eligibility. Because CMMC requires written affirmations and certifications of compliance, any false affirmation creates a cleaner pathway to FCA liability than existed under the self-assessment regime. The Penn State settlement's focus on POA&M misrepresentation directly anticipates this heightened certification environment.
- **Georgia Tech Active Litigation (2024):** Unlike Penn State, the Georgia Tech case was litigated — the DOJ filed a complaint-in-intervention in August 2024 — before reaching a settlement. The parallel trajectories of the two university cases illustrate that the DOJ is willing to both settle and litigate CCFI matters depending on the strength of the record.

### The Role of Internal Whistleblowers

Both the Penn State and Georgia Tech cases were originated by insiders with detailed technical knowledge — a CIO and cybersecurity team members, respectively. The [Harvard Law School Corporate Governance analysis](https://corpgov.law.harvard.edu/2024/11/21/cyber-whistleblower-leads-to-doj-civil-settlement/) of the Penn State settlement emphasized that insider cybersecurity knowledge creates potent qui tam cases: relators who held compliance-facing roles possess documentary evidence, contemporaneous communications, and technical understanding that are difficult for defendants to rebut. The fact that Decker filed while still employed underscores that qui tam exposure is not limited to disgruntled former employees — active insiders with unresolved compliance concerns are equally capable of initiating FCA actions. Organizations that maintain internal compliance friction — where employees raise cybersecurity concerns and are overruled or ignored — face elevated whistleblower risk under the FCA.

## Impact Assessment [MEDIUM confidence]

### Universities with Federal Research Contracts

The Penn State and Georgia Tech cases, which were active simultaneously in late 2024 and both resulted in settlements (Penn State in October 2024, Georgia Tech in September 2025), establish a clear enforcement pattern targeting research universities. Academic institutions holding DoD or NASA research contracts must treat their cybersecurity compliance programs with the same rigor they apply to research compliance (IRB, export controls, financial conflicts of interest). Key exposure areas include:

- **Applied research laboratories** that handle CUI from DoD and intelligence community sponsors are structurally high-risk: they process sensitive data, employ large technical staffs with varying security awareness, and typically operate outside central university IT governance.
- **SPRS self-assessment scores** that reflect unimplemented controls must be accompanied by credible, actively-pursued POA&Ms with accurate remediation timelines. Submitting a low score without a genuine POA&M is now explicitly an FCA risk.
- **Cloud migrations** for research computing environments must verify that any CSP processing CUI holds a FedRAMP Moderate (or higher) authorization. Use of commercial cloud services (e.g., AWS, Azure, Google Cloud) for CUI workloads requires verification that the government-authorized version of the service — not the commercial offering — is being used.

### Defense Industrial Base (DIB) Broadly

The Penn State settlement has implications far beyond universities. Any defense contractor or subcontractor subject to DFARS 252.204-7012, 7019, or 7020 faces the same exposure. The DOJ's [Arnold & Porter analysis](https://www.arnoldporter.com/en/perspectives/blogs/fca-qui-notes/posts/2025/01/doj-civil-cyber-fraud-initiative) underscored that the CCFI remains active under any administration because it generates recoveries — it is self-funding via settlement proceeds and whistleblower incentives — and because former employees with access to compliance systems are structurally positioned to file qui tam complaints with minimal barriers.

### CMMC Acceleration

The CMMC final rule's requirement for written affirmations of compliance — mandatory beginning with DoD contracts issued after the rule's phased implementation — will expand the universe of FCA-actionable statements. As [noted by Wiley](https://www.wiley.law/alert-DOJ-Continues-Crackdown-on-Cybersecurity-Compliance-with-FCA-Settlement), every CMMC affirmation that a contractor signs while knowingly out of compliance becomes a potential false claim. Organizations that have been tolerating known gaps under the self-assessment regime should treat the CMMC timeline as a remediation deadline, not merely a certification deadline.

### Whistleblower Risk Profile

The $250,000 relator's share paid to Matthew Decker illustrates the financial incentive structure. Under 31 U.S.C. § 3730(d), qui tam relators receive between 15% and 25% (or up to 30% if the government declines to intervene) of the settlement or judgment. In a sector where cybersecurity professionals are well-compensated but may hold grievances about understaffed compliance programs or unheeded warnings, the FCA's qui tam incentives create a standing invitation to potential whistleblowers.

## Action Items

- **Audit SPRS submissions now.** Verify that all active NIST SP 800-171 self-assessment scores submitted to SPRS accurately reflect current implementation status and are supported by live, actively-pursued POA&Ms with honest remediation timelines. A low score accompanied by a credible POA&M is defensible; a misrepresented timeline is an FCA risk.
- **Audit cloud service providers.** For every covered system that stores, processes, or transmits CUI, confirm that the CSP holds a FedRAMP Moderate (or equivalent) authorization. Distinguish between authorized government offerings and commercial equivalents that may share brand names but lack authorization.
- **Prepare for CMMC affirmations.** DoD contractors at Level 2 (which maps to all 110 NIST SP 800-171 controls) will be required to affirm compliance when the CMMC contractual requirements propagate through DFARS. Begin third-party assessment preparation now; do not wait until solicitations begin requiring CMMC status.
- **Inventory CUI flows in research environments.** Universities should map which research programs generate or handle CUI, confirm which systems are in-scope for DFARS clauses, and ensure those systems are under centralized security governance — not delegated entirely to individual department or laboratory IT staff.
- **Establish internal cybersecurity compliance reporting channels.** The insider whistleblower pattern in both Penn State and Georgia Tech cases indicates that compliance friction — employees who raise concerns without resolution — creates qui tam exposure. Establish formal mechanisms for security staff to escalate compliance concerns, with documented management responses.
- **Monitor Georgia Tech litigation outcome.** The Georgia Tech case (which was litigated before settling for $875,000 in September 2025) may yield additional judicial guidance on the FCA's materiality standard as applied to cybersecurity certifications. Track developments in United States ex rel. [Craig and others] v. Georgia Tech Research Corp.

## Related Reports

- [reports/cybersecurity/enforcement-actions/federal-sec-solarwinds-ciso-personal-liability-2024-07-18.md](reports/cybersecurity/enforcement-actions/federal-sec-solarwinds-ciso-personal-liability-2024-07-18.md) — Parallel federal enforcement action holding a senior security officer personally liable for cybersecurity misrepresentations, illustrating the SEC's analogous use of securities fraud statutes to pursue cybersecurity non-disclosure; shares the theme of personal and institutional liability for false cybersecurity certifications.
- [reports/cybersecurity/enforcement-actions/federal-sec-cyber-enforcement-authority-solarwinds-2024-07-26.md](reports/cybersecurity/enforcement-actions/federal-sec-cyber-enforcement-authority-solarwinds-2024-07-26.md) — Related examination of federal enforcement authority in cybersecurity contexts; relevant to the DOJ CCFI's companion enforcement landscape alongside SEC disclosure requirements.
- [reports/cybersecurity/enforcement-actions/multistate-enzo-biochem-data-breach-settlement-2024-08-13.md](reports/cybersecurity/enforcement-actions/multistate-enzo-biochem-data-breach-settlement-2024-08-13.md) — Multistate enforcement settlement arising from data breach; illustrates the parallel state enforcement track that federal contractors may face in addition to DOJ FCA exposure.

## Sources

1. [DOJ USAO-EDPA Press Release: Penn State Agrees to Pay $1.25 Million (Oct. 22, 2024)](https://www.justice.gov/usao-edpa/pr/penn-state-agrees-pay-125-million-resolve-false-claims-act-allegations-relating-non) — Official DOJ announcement; primary source for settlement terms, contract scope, and allegations.
2. [DOJ OPA Press Release: Pennsylvania State University Agrees to Pay $1.25M (Oct. 22, 2024)](https://www.justice.gov/archives/opa/pr/pennsylvania-state-university-agrees-pay-125m-resolve-false-claims-act-allegations-relating) — DOJ Office of Public Affairs version of the same announcement; corroborates USAO-EDPA release.
3. [Crowell & Moring: "Allegations of a Litany of Lyin': Penn State Settles Claims of Cybersecurity Noncompliance"](https://www.crowell.com/en/insights/client-alerts/allegations-of-a-litany-of-lyin-penn-state-settles-claims-of-cybersecurity-noncompliance) — Law firm client alert; provides detailed legal analysis of POA&M and CSP allegations and their novelty in CCFI enforcement.
4. [Wiley: "DOJ Continues Crackdown on Cybersecurity Compliance with $1.25M FCA Settlement"](https://www.wiley.law/alert-DOJ-Continues-Crackdown-on-Cybersecurity-Compliance-with-FCA-Settlement) — Government contracts law firm analysis; discusses CMMC implications and first-of-kind POA&M enforcement.
5. [Inside Government Contracts: "Penn State Agrees to Pay $1.25M in Settlement"](https://www.insidegovernmentcontracts.com/2024/11/penn-state-agrees-to-pay-1-25m-in-settlement-for-cybersecurity-non-compliance-false-claims-act-allegations/) — Crowell & Moring government contracts blog; details on fifteen contracts, SPRS submissions, and whistleblower identity.
6. [Feldesman Tucker: "Penn State Settlement Follows DOJ's Enforcement Trends in 2024"](https://www.feldesman.com/penn-state-settlement-demonstrates-governments-continued-focus-on-cybersecurity-compliance/) — Analysis situating Penn State within the 2024 CCFI trend; CMMC final rule implications for universities.
7. [Harvard Law School Corporate Governance Forum: "Cyber Whistleblower Leads to DOJ Civil Settlement"](https://corpgov.law.harvard.edu/2024/11/21/cyber-whistleblower-leads-to-doj-civil-settlement/) — Academic analysis of the whistleblower mechanism and insider knowledge dynamics in cybersecurity FCA cases.
8. [Arnold & Porter FCA Qui Notes: "An Update on DOJ's Civil Cyber Fraud Initiative" (Jan. 2025)](https://www.arnoldporter.com/en/perspectives/blogs/fca-qui-notes/posts/2025/01/doj-civil-cyber-fraud-initiative) — Year-in-review analysis of CCFI enforcement through 2024; universities specifically identified as a continuing DOJ priority.
9. [Womble Bond Dickinson: "Recent FCA Investigations at Universities: A Closer Look"](https://www.womblebonddickinson.com/us/insights/alerts/recent-fca-investigations-universities-closer-look-cybersecurity-compliance) — University-specific compliance analysis comparing Penn State and Georgia Tech cases.
10. [DOJ OPA: Georgia Tech Research Corporation Agrees to Pay $875,000 (Sept. 30, 2025)](https://www.justice.gov/opa/pr/georgia-tech-research-corporation-agrees-pay-875000-resolve-civil-cyber-fraud-litigation) — Official DOJ press release on the companion university enforcement action; settlement announced approximately 11 months after Penn State's resolution.
11. [Global Investigations Blog: "DOJ's FCA-Based Civil Cyber-Fraud Initiative in 2024"](https://www.globalinvestigations.blog/uncategorized/dojs-false-claims-act-based-civil-cyber-fraud-initiative-in-2024/) — Aggregate CCFI enforcement statistics and 2024 recovery figures.
12. [Acquisition.gov: DFARS 252.204-7012 — Safeguarding Covered Defense Information and Cyber Incident Reporting](https://www.acquisition.gov/dfars/252.204-7012-safeguarding-covered-defense-information-and-cyber-incident-reporting.) — Official regulatory text of the primary DFARS clause at issue.
13. [Acquisition.gov: DFARS 252.204-7019 — Notice of NIST SP 800-171 DoD Assessment Requirements](https://www.acquisition.gov/dfars/252.204-7019-notice-nistsp-800-171-dod-assessment-requirements.) — Official text of SPRS self-assessment submission clause.
14. [Acquisition.gov: DFARS 252.204-7020 — NIST SP 800-171 DoD Assessment Requirements](https://www.acquisition.gov/dfars/252.204-7020-nist-sp-800-171dod-assessment-requirements.) — Official text of higher-level DoD assessment requirements clause.
15. [Debevoise Data Blog: "Cyber Whistleblower Leads to DOJ Civil Settlement"](https://www.debevoisedatablog.com/2024/11/04/cyber-whistleblower-leads-to-doj-civil-settlement/) — Additional law firm analysis of the whistleblower dynamics and CCFI enforcement priorities.
