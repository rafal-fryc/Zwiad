---
title: "NYDFS Issues Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence"
date: 2024-10-16
jurisdiction: "New York"
category: "cybersecurity"
development_type: "guidance"
finding_id: "SCAN-20241021-018"
topic_key: "new-york-fa5f9db6-2024"
topic_type: "rulemaking"
first_reported: 2024-10-21
last_updated: 2026-04-16
status_history:
  - date: 2026-04-16
    change: "Corrected Class A company definition in Background and Impact Assessment sections to include the $20M gross annual revenue prerequisite per 23 NYCRR § 500.1 (reviewer round 1 fix)."
cluster: "NYDFS Cybersecurity Regulation (23 NYCRR Part 500): AI Guidance and Enforcement"
cluster_slug: "nydfs-cybersecurity-regulation-23-nycrr-500"
---

# NYDFS Issues Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence

**Jurisdiction:** New York | **Category:** Cybersecurity | **Date:** 2024-10-16

## Executive Summary [HIGH confidence]

On October 16, 2024, New York State Department of Financial Services (NYDFS) Superintendent Adrienne A. Harris issued an [Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence and Strategies to Combat Related Risks](https://www.dfs.ny.gov/industry-guidance/industry-letters/il20241016-cyber-risks-ai-and-strategies-combat-related-risks). The guidance does not create new requirements but clarifies how all entities covered by the existing NYDFS Cybersecurity Regulation, 23 NYCRR Part 500, must apply that regulation's existing risk assessment, access control, vendor management, and training requirements to AI-related cybersecurity threats. The letter identifies four primary AI-driven cybersecurity risks — AI-enabled social engineering (deepfakes), AI-enhanced cyberattacks, exposure of large volumes of nonpublic information (NPI), and supply chain vulnerabilities introduced by AI vendors — and provides specific mitigation strategies for each. As a practical matter, the guidance will shape how NYDFS examines covered entities' cybersecurity programs for AI readiness going forward and may foreshadow formal regulatory action.

## Background [HIGH confidence]

### NYDFS Cybersecurity Regulation: 23 NYCRR Part 500

NYDFS first enacted 23 NYCRR Part 500 in March 2017, establishing baseline cybersecurity requirements for banks, insurance companies, money transmitters, mortgage lenders and brokers, and other financial services companies licensed or chartered under New York Banking, Insurance, or Financial Services Law. The regulation requires covered entities to maintain a cybersecurity program, designate a Chief Information Security Officer (CISO), conduct periodic risk assessments, implement access controls and multi-factor authentication (MFA), and notify NYDFS within 72 hours of a qualifying cybersecurity incident.

In November 2023, NYDFS finalized the [Second Amendment to Part 500](https://www.dfs.ny.gov/system/files/documents/2023/12/rf23_nycrr_part_500_amend02_20231101.pdf), the most significant revision since the regulation's initial enactment. The Second Amendment introduced a phased compliance timeline extending through November 1, 2025, added new requirements for Class A companies — defined under [23 NYCRR § 500.1](https://www.law.cornell.edu/regulations/new-york/23-NYCRR-500.1) as covered entities with at least $20 million in gross annual revenue in each of the last two fiscal years AND either more than 2,000 employees averaged over the last two fiscal years or over $1 billion in gross annual revenue in each of the last two fiscal years — and expanded MFA obligations, endpoint detection and response (EDR) requirements, and independent audit duties. At the time the October 2024 AI guidance was issued, covered entities were mid-stream in the Second Amendment's compliance rollout.

### Regulatory Context for AI Guidance

The October 2024 letter is part of a broader trend of regulators supplementing existing cybersecurity frameworks with AI-specific interpretation guidance rather than immediately promulgating new AI-specific rules. NYDFS issued the letter under its existing supervisory authority, signaling that it considers the AI-related risks described to be within the scope of what covered entities must already address under Part 500 — and that non-compliance with AI-related cyber hygiene can constitute a regulatory violation under the existing regulation.

Superintendent Harris stated at the time of issuance: "AI has improved the ability for businesses to enhance threat detection and incident response strategies, while concurrently creating new opportunities for cybercriminals to commit crimes at greater scale and speed." The [NYDFS press release](https://www.dfs.ny.gov/reports_and_publications/press_releases/pr20241016) characterized the guidance as intended to help the regulated sector address evolving threats within the existing regulatory framework.

## Detailed Analysis [HIGH confidence]

### Four Primary AI-Related Cybersecurity Risks

The Industry Letter identifies four "concerning threats" associated with AI, organized into two categories: risks arising from threat actors' use of AI, and risks arising from covered entities' own use of AI.

**1. AI-Enabled Social Engineering (Threat Actor Risk)**

AI tools enable threat actors to generate highly convincing deepfakes — synthetic audio, video, and text — that can impersonate executives, employees, or customers. These deepfakes are deployed through phishing (email), vishing (telephone), smishing (SMS/text), videoconferencing impersonation, and fraudulent online postings. When successful, such attacks result in credential theft, unauthorized access to information systems, and unauthorized financial transfers. The guidance notes that these attacks are increasingly personalized and harder to distinguish from authentic communications.

**2. AI-Enhanced Cyberattacks (Threat Actor Risk)**

Threat actors leverage AI tools to accelerate and scale existing attack methods: automated vulnerability scanning and exploitation, faster malware and ransomware development and deployment, and more effective evasion of detection controls. AI can be used to conduct reconnaissance at scale, identify targets, and launch attacks that outpace manual defensive responses.

**3. Exposure or Theft of Nonpublic Information (Covered Entity Risk)**

Developing or deploying AI products requires covered entities to collect and process large volumes of data, often including customer NPI. Aggregating NPI at scale creates a more attractive target and a larger attack surface. NYDFS expressed concern that entities' AI adoption programs may be inadvertently expanding the sensitivity and volume of data that must be protected under Part 500.

**4. Supply Chain Vulnerabilities (Covered Entity Risk)**

AI model development and deployment often involves third-party vendors and service providers (TPSPs) who collect and process large volumes of data on behalf of covered entities. Each TPSP relationship introduces potential attack vectors. A compromised vendor can serve as a gateway for broader attacks on the covered entity's network and on other entities in the same supply chain.

### Mitigation Strategies and Required Actions Under Part 500

The guidance maps each risk category to specific obligations already contained in Part 500 and provides practical recommendations for how covered entities should fulfill those obligations in the AI context.

**Risk Assessments (§ 500.9)**

Covered entities must ensure their risk assessments expressly address: (i) the organization's own use of AI; (ii) AI technologies used by TPSPs and vendors; and (iii) vulnerabilities arising from AI applications that could affect the confidentiality, integrity, or availability of information systems or NPI. The guidance emphasizes that risk assessments must be updated to reflect the rapidly evolving AI threat landscape.

**Access Controls and Authentication (§ 500.12)**

NYDFS strongly recommends that covered entities move away from authentication methods that AI deepfakes can defeat — specifically, SMS text, voice-based verification, and video-based verification. Recommended alternatives include digital-based certificates, physical security keys, and biometric methods employing "liveness detection" or texture analysis to verify that a biometric input comes from a live person rather than a spoofed image or video. Entities may also combine multiple biometric modalities simultaneously (e.g., fingerprint combined with iris recognition or keystroke dynamics). Note that the Second Amendment already mandated expanded MFA obligations phasing in through 2025; the AI guidance layers AI-specific authentication recommendations on top of those baseline requirements.

**Third-Party Service Provider Management (§ 500.11)**

The guidance directs covered entities to update TPSP policies and procedures to account for AI-related risks. Due diligence conducted before engaging a TPSP that will access information systems or NPI should now specifically assess: (i) the AI-related threats facing that TPSP; (ii) how those threats, if realized, could affect the covered entity; and (iii) how the TPSP defends against such threats. Contractual protections should require timely TPSP notification of any cybersecurity event affecting the covered entity's systems or NPI held by the TPSP.

**Cybersecurity Training (§ 500.14)**

Annual cybersecurity training required under Part 500 must be updated to include AI-related content, including: the nature of AI-related cybersecurity risks; the entity's procedures for mitigating those risks; and how to recognize and respond to AI-enabled social engineering attacks, including deepfake-based phishing and vishing attempts.

**Board and Senior Leadership Oversight (§ 500.4)**

The Senior Governing Body — typically the board of directors — must be provided with regular reports covering cybersecurity matters that include AI-related threats. The guidance expects the board to have sufficient understanding of AI cybersecurity risks to exercise meaningful oversight and to have delegated authority for risk management appropriately within the organization.

**Data Management**

While not mapped to a single Part 500 section, the guidance emphasizes that covered entities should evaluate whether their AI adoption programs are creating unnecessarily large data stores of NPI, and should implement data minimization and retention practices appropriate to the risk profile.

### Scope: Who Is Covered

The October 2024 guidance applies to all "Covered Entities" under 23 NYCRR Part 500: any person or entity operating under, or required to operate under, a license, registration, charter, certificate, permit, accreditation, or similar authorization under the Banking Law, Insurance Law, or Financial Services Law of New York. This includes banks, credit unions, insurance companies, insurance agents and brokers, money transmitters, mortgage lenders and brokers, check cashers, and other DFS-licensed financial services firms. Entities that are licensed solely in other states and do not hold a New York license are not directly covered, though other states' regulators may adopt similar positions.

### No New Requirements — But Significant Practical Implications

NYDFS was explicit that the guidance does not impose requirements beyond those already in Part 500. However, as [Mayer Brown](https://www.mayerbrown.com/en/insights/publications/2024/10/new-york-state-department-of-financial-services-issues-industry-letter-on-cybersecurity-risks-arising-from-artificial-intelligence) and [Hunton Andrews Kurth](https://www.hunton.com/privacy-and-information-security-law/nydfs-tells-companies-to-address-ai-security-threats) both noted in their analyses, the guidance effectively defines NYDFS's examination expectations. Covered entities that have not addressed AI-specific risks in their risk assessments, training programs, and TPSP policies may find themselves cited for Part 500 non-compliance during regulatory examinations — even absent any separate AI-specific rulemaking.

The guidance also signals NYDFS's view that AI-related cyber risk is already a live regulatory issue, not a future concern. [White & Case](https://www.whitecase.com/insight-alert/nydfs-releases-artificial-intelligence-cybersecurity-guidance-covered-entities) observed that the letter will likely influence how other state and federal regulators approach AI-cybersecurity risk management, potentially serving as a template for future guidance or rulemaking by other sector regulators.

## Impact Assessment [HIGH confidence]

### Affected Entities

All NYDFS-licensed financial services firms are directly subject to the guidance. The broadest impact falls on:

- **Banks and credit unions** holding significant customer financial data and NPI
- **Insurance companies and agents** operating under New York Insurance Law
- **Money transmitters and fintech firms** that process high volumes of transactions involving NPI
- **Mortgage lenders, brokers, and servicers** licensed under New York Banking Law

Class A companies — defined under [23 NYCRR § 500.1](https://www.law.cornell.edu/regulations/new-york/23-NYCRR-500.1) as those with at least $20 million in gross annual revenue in each of the last two fiscal years AND either more than 2,000 employees averaged over the last two fiscal years or over $1 billion in gross annual revenue in each of the last two fiscal years — face the highest compliance burden because they are simultaneously managing Second Amendment compliance timelines while being expected to integrate AI-risk considerations into all required cybersecurity program elements.

### Compliance Requirements and Timelines

The guidance does not establish new deadlines separate from those already in Part 500 and the Second Amendment. However, covered entities should treat the guidance as signaling that the following program elements must promptly reflect AI-specific considerations:

- **Risk assessments** (already required; must now expressly cover AI-related risks)
- **Annual cybersecurity training** (must now include AI/deepfake content)
- **TPSP due diligence and contracts** (must now address AI-related vendor risks)
- **Authentication mechanisms** (entities should begin evaluating AI-resistant MFA methods ahead of the Second Amendment's expanded MFA requirements becoming fully effective in November 2025)
- **Board reporting** (senior governing body briefings must cover AI-related threats)

### Enforcement Outlook

NYDFS has demonstrated an active enforcement posture under Part 500, including consent orders and civil monetary penalties against covered entities for cybersecurity program deficiencies. Now that NYDFS has published guidance explicitly identifying AI-related cyber risks as within scope, future enforcement actions could cite failure to address AI risks as evidence of an inadequate risk assessment or deficient cybersecurity program. Covered entities should treat the guidance as creating de facto compliance obligations even in the absence of new regulatory text.

The guidance may also foreshadow future formal rulemaking. NYDFS's broader cybersecurity regulatory trajectory — from the original 2017 regulation through the 2023 Second Amendment — suggests that interpretive guidance often precedes more prescriptive rule amendments.

## Action Items

- **Immediately** review existing risk assessments to determine whether they expressly address AI-related threat vectors, including threat actors' use of AI, the entity's own AI deployments, and AI used by TPSPs. Update assessments if they are silent on these topics.
- **Within 90 days**, assess current MFA mechanisms against the guidance's recommendation to avoid SMS, voice, or video-based authentication factors; begin evaluating or piloting AI-resistant alternatives (hardware security keys, digital certificates, multi-modal biometrics with liveness detection).
- **Before next annual training cycle**, update cybersecurity training curricula to include content on AI-enabled social engineering (deepfakes, vishing, spear phishing), the entity's procedures for mitigating AI risks, and incident response protocols for AI-enhanced attacks.
- **On a rolling basis**, update TPSP due diligence questionnaires and contractual templates to require AI-risk disclosures, assess TPSP AI cyber hygiene, and ensure timely breach notification obligations are clearly specified.
- **At next board/senior leadership briefing**, include a segment on AI-related cybersecurity threats and the entity's current program response, ensuring the board record reflects adequate oversight of this risk category.
- **Monitor** NYDFS examination activity and enforcement actions for any citations related to AI cybersecurity program gaps; note that citations under existing Part 500 provisions citing AI-risk deficiencies would confirm the de facto compliance expectations created by this guidance.
- **Watch** for any NYDFS follow-on rulemaking that may formalize AI-specific cybersecurity requirements as distinct obligations within Part 500.

## Related Reports

- [reports/cybersecurity/incident-reporting/new-york-nysdoh-hospital-cybersecurity-2024-06-10.md](reports/cybersecurity/incident-reporting/new-york-nysdoh-hospital-cybersecurity-2024-06-10.md) -- Both reports address New York cybersecurity regulatory requirements from 2024, with the NYSDOH report covering healthcare-sector-specific incident reporting obligations analogous to the DFS-sector obligations discussed here.

## Sources

1. [Industry Letter — October 16, 2024: Cybersecurity Risks Arising from Artificial Intelligence and Strategies to Combat Related Risks (NYDFS)](https://www.dfs.ny.gov/industry-guidance/industry-letters/il20241016-cyber-risks-ai-and-strategies-combat-related-risks) -- Official NYDFS industry letter; primary source for all guidance requirements and risk categories described in this report.
2. [NYDFS Press Release — October 16, 2024 (DFS)](https://www.dfs.ny.gov/reports_and_publications/press_releases/pr20241016) -- Official NYDFS press release announcing issuance of the guidance letter, with Superintendent Harris's statement.
3. [23 NYCRR Part 500 — Second Amendment Text (DFS, November 2023)](https://www.dfs.ny.gov/system/files/documents/2023/12/rf23_nycrr_part_500_amend02_20231101.pdf) -- Official text of the Second Amendment to the NYDFS Cybersecurity Regulation; provides the regulatory baseline to which the October 2024 guidance applies.
4. [23 NYCRR § 500.1 — Definitions (Cornell LII)](https://www.law.cornell.edu/regulations/new-york/23-NYCRR-500.1) -- Official regulatory text of the Class A company definition, including the conjunctive $20M gross annual revenue prerequisite.
5. [NYDFS Cybersecurity Resource Center (DFS)](https://www.dfs.ny.gov/industry_guidance/cybersecurity) -- NYDFS landing page for all Part 500 guidance, resources, and industry letters.
6. [New York State Department of Financial Services Issues Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence (Mayer Brown, October 2024)](https://www.mayerbrown.com/en/insights/publications/2024/10/new-york-state-department-of-financial-services-issues-industry-letter-on-cybersecurity-risks-arising-from-artificial-intelligence) -- Law firm analysis noting practical examination implications and likely influence on other regulators.
7. [NYDFS Tells Companies to Address AI Security Threats (Hunton Andrews Kurth)](https://www.hunton.com/privacy-and-information-security-law/nydfs-tells-companies-to-address-ai-security-threats) -- Law firm analysis of compliance implications and authentication recommendations.
8. [NYDFS Releases Artificial Intelligence Cybersecurity Guidance For Covered Entities (White & Case)](https://www.whitecase.com/insight-alert/nydfs-releases-artificial-intelligence-cybersecurity-guidance-covered-entities) -- Law firm analysis identifying four primary risk categories and noting potential influence on other regulators.
9. [NYDFS Issues Guidance on Artificial Intelligence-related Cybersecurity Risks (Alston & Bird)](https://www.alstonprivacy.com/nydfs-issues-guidance-on-artificial-intelligence-related-cybersecurity-risks/) -- Additional law firm analysis of the guidance with compliance recommendations.
10. [New York Department of Financial Services Issues New Guidance on Cybersecurity Risks Arising from Artificial Intelligence (Consumer Financial Services Law Monitor)](https://www.consumerfinancialserviceslawmonitor.com/2024/10/new-york-department-of-financial-services-issues-new-guidance-on-cybersecurity-risks-arising-from-artificial-intelligence/) -- Trade press analysis with third-party service provider management detail.
11. [NYDFS Issues Industry Guidance on Risks Arising from Artificial Intelligence (Inside Privacy / Covington)](https://www.insideprivacy.com/artificial-intelligence/nydfs-issues-industry-guidance-on-risks-arising-from-artificial-intelligence/) -- Additional practitioner analysis of the guidance structure and scope.
12. [New York Department of Financial Services Addresses Cybersecurity Risks from Artificial Intelligence (Data Protection Report / Norton Rose Fulbright)](https://www.dataprotectionreport.com/2024/10/new-york-department-of-financial-services-addresses-cybersecurity-risks-from-artificial-intelligence/) -- Supplemental law firm analysis covering vendor management and NPI data risk.
13. [NYDFS Part 500, One Year Later — New Requirements Effective November 1, 2024 (Debevoise Data Blog)](https://www.debevoisedatablog.com/2024/10/30/nydfs-part-500-one-year-later-part-one-new-requirements-effective-november-1-2024/) -- Analysis of Second Amendment compliance milestones running concurrently with the AI guidance, useful for compliance timeline context.
