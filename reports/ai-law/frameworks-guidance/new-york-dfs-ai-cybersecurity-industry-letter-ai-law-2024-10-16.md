---
title: "NY DFS Issues AI Cybersecurity Industry Letter Mapping 23 NYCRR Part 500 to Artificial Intelligence Risks"
date: 2024-10-16
jurisdiction: "New York"
category: "ai-law"
development_type: "guidance"
finding_id: "SCAN-20241104-002"
topic_key: "new-york-136539ef-2024"
topic_type: "guidance"
topic_key_confidence: "low"
first_reported: 2024-11-04
last_updated: 2026-04-21
status_history:
  - "2026-04-21: Corrected Class A company definition (logical connector AND vs OR; gross annual revenue vs total assets per 23 NYCRR § 500.1); updated CFTC TAC citation to specific press release URL (r1 reviewer feedback)"
cluster: "NYDFS Cybersecurity Regulation (23 NYCRR Part 500): AI Guidance and Enforcement"
cluster_slug: "nydfs-cybersecurity-regulation-23-nycrr-500"
---

# NY DFS Issues AI Cybersecurity Industry Letter Mapping 23 NYCRR Part 500 to Artificial Intelligence Risks

**Jurisdiction:** New York | **Category:** AI Law | **Date:** 2024-10-16

> **Note:** A companion report on this same industry letter, filed under the cybersecurity category and focusing on the cybersecurity compliance obligations, exists at `reports/cybersecurity/standards-guidance/new-york-dfs-ai-cybersecurity-guidance-2024-10-16.md` (finding SCAN-20241021-018). This report focuses on the AI governance and AI-law implications of the letter.

## Executive Summary [HIGH confidence]

On October 16, 2024, New York State Department of Financial Services (NYDFS) Superintendent Adrienne A. Harris issued an [Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence and Strategies to Combat Related Risks](https://www.dfs.ny.gov/industry-guidance/industry-letters/il20241016-cyber-risks-ai-and-strategies-combat-related-risks). The letter is notable from an AI law perspective because it represents one of the first major US financial-services regulator actions to explicitly address how existing regulatory frameworks apply when covered entities deploy or are threatened by artificial intelligence. The guidance does not create new legal obligations but establishes NYDFS's interpretive position that the existing [23 NYCRR Part 500](https://www.dfs.ny.gov/system/files/documents/2023/03/23NYCRR500_0.pdf) cybersecurity regulation already requires AI-specific risk assessments, AI-aware vendor due diligence, and AI-adapted employee training. This interpretive approach — applying existing regulation to AI rather than enacting new AI-specific rules — is likely to influence how other state regulators address AI in the near term.

## Background [HIGH confidence]

### NYDFS and the 23 NYCRR Part 500 Regulatory Framework

The New York Department of Financial Services is the primary regulator for banks, insurers, and other financial services companies chartered or licensed in New York. Its cybersecurity regulation, [23 NYCRR Part 500](https://www.dfs.ny.gov/system/files/documents/2023/03/23NYCRR500_0.pdf), was first enacted on March 1, 2017 — the first comprehensive cybersecurity regulation in the United States applicable to financial services entities. Under Part 500, "covered entities" are defined in 23 NYCRR § 500.1(e) as any person operating under or required to operate under a license, registration, charter, certificate, permit, accreditation, or similar authorization under the Banking Law, the Insurance Law, or the Financial Services Law.

The regulation was [substantially amended in November 2023](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20231128-nydfs-finalizes-amendments-to-cybersecurity-regulations) — the most significant revision since the original 2017 rule — with a phased implementation schedule running from December 2023 through November 2025. The amendment process began in July 2022 and went through multiple public comment rounds. Key amendment deadlines include:

- **December 1, 2023**: Cybersecurity event notice requirements (ransomware and events reported to other authorities)
- **November 1, 2024**: New governance requirements (§ 500.4), encryption (§ 500.15), and incident response/business continuity (§ 500.16)
- **May 1, 2025**: Vulnerability scanning updates, access privilege changes, and monitoring/training provisions
- **November 1, 2025**: Multi-factor authentication (§ 500.12) and asset management/data retention (§ 500.13(a)) requirements take full effect

The October 2024 industry letter was issued precisely as the November 1, 2024 amendment tranche became effective, making it particularly timely for entities integrating the new governance and incident response requirements.

### Context: AI and Financial Services Regulation

The NYDFS guidance fits within a broader pattern of US financial regulators grappling with AI's implications. The CFTC's [Technology Advisory Committee AI subcommittee report (May 2024)](https://www.cftc.gov/PressRoom/PressReleases/8905-24) and federal interagency statements on AI in banking have all addressed AI risk without imposing new statutory requirements. NYDFS's approach — issuing an interpretive industry letter rather than proposing new rules — is consistent with this emerging pattern of regulators mapping AI risk to existing frameworks rather than waiting for new legislation.

## Detailed Analysis [HIGH confidence]

### Four AI-Driven Cybersecurity Risk Categories

The NYDFS industry letter identifies four primary categories of AI-related cybersecurity risk facing covered entities. Two arise from threat actors using AI against entities; two arise from entities' own deployment of AI:

**1. AI-Enabled Social Engineering**
This is characterized in the guidance as among the most significant threats facing financial services. AI dramatically improves threat actors' ability to create personalized, convincing phishing emails and [deepfakes](https://www.dfs.ny.gov/industry-guidance/industry-letters/il20241016-cyber-risks-ai-and-strategies-combat-related-risks) — realistic synthetic audio, video, and text — that impersonate executives, customers, or regulators. NYDFS expressly identifies deepfakes as a primary vehicle for fraudulent wire transfer instructions and credential theft.

**2. AI-Enhanced Cyberattacks**
Threat actors can leverage AI tools to scan for and exploit vulnerabilities at greater speed and scale, accelerate malware and ransomware deployment, conduct automated reconnaissance, and evade detection systems. The guidance notes that AI can compress the attack lifecycle from weeks to hours.

**3. Risks from Maintaining Large Volumes of Nonpublic Information (NPI)**
Covered entities deploying AI frequently aggregate large quantities of NPI — including biometric data — to train or operate AI systems. The guidance warns that "maintaining non-public information in large quantities poses additional risks for Covered Entities that develop or deploy AI because they need to protect substantially more data, and threat actors have a greater incentive to target these entities."

**4. Third-Party, Vendor, and Supply Chain Dependencies**
AI systems frequently depend on external vendors for training data, model APIs, and infrastructure. The guidance flags the supply chain risk: a compromise of an AI vendor can propagate to all entities using that vendor's models or data pipelines.

### Interpretive Mapping: Existing Part 500 Requirements to AI Risks

The guidance's AI-law significance lies in its explicit mapping of existing regulatory requirements to AI scenarios — effectively announcing how NYDFS examiners will evaluate AI readiness under existing authority:

**Risk Assessments (§ 500.9)**: The Cybersecurity Regulation requires annual risk assessments. The guidance states these must now specifically address AI-related risks — both threats from AI-weaponized attackers and risks from the entity's own AI use. A generic risk assessment that does not address AI will not satisfy this requirement as a practical matter.

**Access Controls and Authentication (§ 500.7, § 500.12)**: NYDFS takes a notable interpretive position on authentication: covered entities should avoid authentication methods that AI deepfakes can defeat — specifically SMS text, voice calls, and video authentication. The guidance recommends physical security keys and digital certificate-based authentication as deepfake-resistant alternatives. Given that MFA compliance under the amended § 500.12 takes full effect November 1, 2025, entities must design their MFA solutions with this interpretive guidance in mind.

**Third-Party Service Provider Management (§ 500.11)**: The guidance "strongly" recommends that due diligence on third-party service providers include evaluation of AI-specific risks. Vendor contracts should require notification to the covered entity of any AI-related cybersecurity event. The guidance signals that NYDFS will scrutinize vendor management programs for AI-specific provisions.

**Cybersecurity Training (§ 500.14)**: Annual training must be adapted to address AI-fueled social engineering, including deepfakes. Personnel who develop or deploy AI systems should receive additional training on secure AI system design. Personnel using AI-powered applications should be trained to avoid disclosing NPI in AI queries.

**Incident Response and Business Continuity (§ 500.16)**: Plans must be "reasonably designed to address all types of Cybersecurity Events," explicitly including AI-driven incidents. This amendment tranche became effective November 1, 2024 — the same month as the guidance.

### Enforcement Signal

Several law firms analyzing the guidance have flagged it as a likely enforcement signal. [Ogletree Deakins](https://ogletree.com/insights-resources/blog-posts/new-york-department-of-financial-services-industry-letter-foreshadowing-enforcement-of-vendor-management/) characterized the vendor management section as "foreshadowing enforcement" of third-party AI risk management requirements. [Debevoise & Plimpton](https://www.debevoisedatablog.com/2024/10/20/managing-cybersecurity-risks-arising-from-ai-new-guidance-from-the-nydfs/) noted that the guidance establishes the interpretive baseline examiners will use when assessing whether covered entities' cybersecurity programs adequately address AI risk.

## Impact Assessment [MEDIUM confidence]

### Covered Entities Affected

All entities regulated by NYDFS under the Banking Law, Insurance Law, or Financial Services Law are subject to the guidance. This encompasses banks chartered in New York, insurance companies, money transmitters, mortgage servicers, and other licensed financial services entities — collectively thousands of institutions ranging from large global banks to small community lenders.

Class A companies — defined under [23 NYCRR § 500.1](https://www.law.cornell.edu/regulations/new-york/23-NYCRR-500.1) as covered entities with at least $20 million in gross annual revenue in each of the last two fiscal years from all business operations AND either more than 2,000 employees averaged over the last two fiscal years or over $1 billion in gross annual revenue from all business operations — face the most stringent obligations under the 2023 amendments, but the AI guidance's interpretive positions apply to all covered entities regardless of size.

### Compliance Implications

The guidance creates de facto compliance requirements for AI readiness even without new rulemaking. Covered entities that have not updated their risk assessments, vendor contracts, and training programs to address AI by the time of their next NYDFS examination face potential examination findings. The November 2024 guidance was issued as the governance and incident response amendment tranche took effect, signaling that NYDFS examiners will begin evaluating AI readiness immediately.

Practical compliance steps the guidance implies:
- Risk assessments updated to include AI threat scenarios and entity AI deployments
- Vendor contracts revised to require AI cybersecurity event notification
- MFA implementations designed to resist deepfake attacks (avoid SMS/voice/video auth)
- Employee training curricula updated for deepfake social engineering scenarios
- Incident response plans revised to address AI-specific attack vectors

### Broader AI Governance Significance

From an AI-law perspective, the NYDFS approach represents a significant regulatory template. Rather than waiting for comprehensive AI legislation or proposing new AI-specific rules, NYDFS announced its interpretive position that existing cybersecurity regulation already covers AI risk — and will be enforced accordingly. This "existing law applies" approach may be replicated by other state financial regulators and could influence how federal bank regulators (OCC, Fed, FDIC) address AI cybersecurity risk through existing safety-and-soundness supervisory authority.

## Action Items

- Update the annual cybersecurity risk assessment to include an explicit AI risk section covering both external AI-enabled threats and internal AI deployments before the next examination cycle.
- Audit third-party service provider contracts to add AI cybersecurity event notification obligations and AI-specific due diligence criteria.
- Review MFA implementations to assess whether SMS, voice, or video authentication factors are used in contexts that could be defeated by deepfakes; develop a remediation plan aligned with the November 1, 2025 MFA amendment deadline.
- Revise cybersecurity awareness training to include deepfake scenarios and NPI-handling protocols for AI tool use.
- Update incident response and business continuity plans to address AI-specific attack vectors and threat scenarios (effective November 1, 2024).
- Monitor NYDFS examination findings and enforcement actions for AI-related deficiency citations as the examination cycle progresses through 2025.

## Related Reports

- [reports/cybersecurity/standards-guidance/new-york-dfs-ai-cybersecurity-guidance-2024-10-16.md](../../../cybersecurity/standards-guidance/new-york-dfs-ai-cybersecurity-guidance-2024-10-16.md) — Companion report on the same NYDFS industry letter, filed under cybersecurity, with detailed treatment of the Part 500 compliance obligations for cybersecurity practitioners.
- [reports/ai-law/frameworks-guidance/nist-ai-rmf-critical-infrastructure-profile-2026-04-13.md](../frameworks-guidance/nist-ai-rmf-critical-infrastructure-profile-2026-04-13.md) — NIST AI RMF profile development for critical infrastructure, which overlaps with AI risk management frameworks for financial services.
- [reports/ai-law/state-legislation/new-york-raise-act-frontier-ai-preemption-2026-04-19.md](../state-legislation/new-york-raise-act-frontier-ai-preemption-2026-04-19.md) — New York's RAISE Act on frontier AI safety, representing the legislative complement to NYDFS's regulatory approach to AI governance in New York.
- [reports/ai-law/federal-regulation/federal-cftc-tac-ai-report-2024-05-02.md](../federal-regulation/federal-cftc-tac-ai-report-2024-05-02.md) — CFTC Technology Advisory Committee AI report, representing a parallel federal financial regulator's approach to AI risk under existing regulatory authority.

## Sources

1. [Industry Letter - October 16, 2024: Cybersecurity Risks Arising from Artificial Intelligence and Strategies to Combat Related Risks (NY DFS)](https://www.dfs.ny.gov/industry-guidance/industry-letters/il20241016-cyber-risks-ai-and-strategies-combat-related-risks) -- Official primary source: the full text of the NYDFS industry letter
2. [DFS Superintendent Adrienne A. Harris Issues New Guidance to Address Cybersecurity Risks Arising from Artificial Intelligence (NY DFS Press Release)](https://www.dfs.ny.gov/reports_and_publications/press_releases/pr20241016) -- Official NYDFS press release accompanying the guidance
3. [23 NYCRR Part 500: Cybersecurity Requirements for Financial Services Companies (NY DFS)](https://www.dfs.ny.gov/system/files/documents/2023/03/23NYCRR500_0.pdf) -- Official text of the NYDFS cybersecurity regulation (2023 amended version)
4. [NYDFS Finalizes Amendments to Cybersecurity Regulations (WilmerHale)](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20231128-nydfs-finalizes-amendments-to-cybersecurity-regulations) -- Analysis of the November 2023 Part 500 amendments and implementation timeline
5. [Managing Cybersecurity Risks Arising from AI - New Guidance from the NYDFS (Debevoise Data Blog)](https://www.debevoisedatablog.com/2024/10/20/managing-cybersecurity-risks-arising-from-ai-new-guidance-from-the-nydfs/) -- Law firm analysis characterizing the guidance's enforcement implications
6. [NYDFS Issues Industry Guidance on Risks Arising from Artificial Intelligence (Inside Privacy / Covington)](https://www.insideprivacy.com/artificial-intelligence/nydfs-issues-industry-guidance-on-risks-arising-from-artificial-intelligence/) -- Law firm analysis of the four risk categories and mitigation measures
7. [New York Department of Financial Services' Industry Letter: Foreshadowing Enforcement of Vendor Management? (Ogletree Deakins)](https://ogletree.com/insights-resources/blog-posts/new-york-department-of-financial-services-industry-letter-foreshadowing-enforcement-of-vendor-management/) -- Analysis flagging the vendor management section as an enforcement signal
8. [NYDFS Releases Artificial Intelligence Cybersecurity Guidance For Covered Entities (White & Case)](https://www.whitecase.com/insight-alert/nydfs-releases-artificial-intelligence-cybersecurity-guidance-covered-entities) -- Additional law firm analysis on access controls and MFA guidance
9. [New York Department of Financial Services Issues New Guidance on Cybersecurity Risks Arising from Artificial Intelligence (Consumer Financial Services Law Monitor / Troutman Pepper)](https://www.consumerfinancialserviceslawmonitor.com/2024/10/new-york-department-of-financial-services-issues-new-guidance-on-cybersecurity-risks-arising-from-artificial-intelligence/) -- Source law firm analysis from the original finding source
10. [NYDFS: Final set of cybersecurity requirements under amended Part 500 take effect November 1, 2025 (Hogan Lovells)](https://www.hoganlovells.com/en/publications/nydfs-final-set-of-cybersecurity-requirements-under-amended-part-500-take-effect-november-1-2025) -- Analysis of the November 2025 amendment compliance deadlines
11. [23 NYCRR § 500.1 - Definitions (LII / Cornell Law)](https://www.law.cornell.edu/regulations/new-york/23-NYCRR-500.1) -- Official regulatory text of the Part 500 definitions section, including the exact Class A covered entity definition
12. [CFTC Technology Advisory Committee Advances Report on Responsible AI in Financial Markets (CFTC Press Release 8905-24)](https://www.cftc.gov/PressRoom/PressReleases/8905-24) -- CFTC press release announcing the TAC AI subcommittee report (May 2024)

