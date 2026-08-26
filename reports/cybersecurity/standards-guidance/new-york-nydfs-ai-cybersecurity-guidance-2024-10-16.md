---
title: "NYDFS Issues Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence"
date: 2024-10-16
jurisdiction: "New York"
category: "cybersecurity"
development_type: "guidance"
finding_id: "SCAN-20241105-025"
topic_key: "new-york-nydfs-ai-cybersecurity-guidance-2024"
topic_type: "guidance"
first_reported: 2024-11-05
last_updated: 2024-11-05
status_history: []
cluster: "NYDFS Cybersecurity Regulation (23 NYCRR Part 500): AI Guidance and Enforcement"
cluster_slug: "nydfs-cybersecurity-regulation-23-nycrr-500"
---

# NYDFS Issues Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence

**Jurisdiction:** New York | **Category:** Privacy / Financial Services Cybersecurity | **Date:** October 16, 2024

## Executive Summary [HIGH confidence]

On October 16, 2024, the New York Department of Financial Services (NYDFS) issued an industry letter titled "Cybersecurity Risks Arising from Artificial Intelligence and Strategies to Combat Related Risks," signed by Superintendent Adrienne A. Harris. The letter applies to all NYDFS-regulated financial institutions — including banks, insurance companies, mortgage servicers, and other licensed financial services entities — that are already subject to the agency's landmark cybersecurity regulation, [23 NYCRR Part 500](https://www.dfs.ny.gov/system/files/documents/2023/03/23NYCRR500_0.pdf). Although NYDFS states the letter creates no new legal obligations, it provides a detailed roadmap for how the agency expects covered entities to address four categories of AI-driven cybersecurity risk and signals enforcement priorities that regulators will apply in examinations. Regulated entities that have not updated their risk assessments, third-party vendor programs, access controls, and training protocols to account for AI-specific threats should do so promptly.

## Background [HIGH confidence]

### NYDFS's Cybersecurity Regulation: 23 NYCRR Part 500

The [NYDFS Cybersecurity Regulation, 23 NYCRR Part 500](https://www.dfs.ny.gov/system/files/documents/2023/03/23NYCRR500_0.pdf), was first adopted in 2017 as the first comprehensive state-level cybersecurity rule for financial institutions. It established baseline requirements for covered entities, including mandatory risk assessments, multi-factor authentication (MFA), encryption, cybersecurity training, third-party service provider (TPSP) management, and incident reporting to the DFS.

In November 2023, NYDFS finalized its [second amendment to Part 500](https://www.dfs.ny.gov/system/files/documents/2023/10/rf_fs_2amend23NYCRR500_text_20231101.pdf), the most sweeping set of changes since the regulation's enactment. Key changes include:

- Creation of a "Class A Company" tier for larger entities subject to enhanced controls, mandatory independent audits, and advanced technical requirements.
- Expanded MFA requirements now covering all users attempting to access information systems (not just privileged accounts), phased in with a final compliance deadline of November 1, 2025.
- A 72-hour incident notification obligation to DFS under Section 500.17(a), covering ransomware payments and events reported to other regulators.
- New requirements for complete asset inventory documentation.

These 2023 amendments established the foundation upon which the October 2024 AI guidance is layered. The AI guidance does not amend Part 500 but instructs covered entities on how existing Part 500 requirements — particularly risk assessments (§ 500.9), TPSP management (§ 500.11), access controls (§ 500.7), training (§ 500.14), and incident response (§ 500.16) — apply to the AI threat landscape.

### NYDFS's Broader AI Regulatory Agenda

The October 2024 cybersecurity letter is part of a broader NYDFS engagement with AI governance. In January 2024, [Superintendent Harris proposed guidance on the discriminatory use of AI and external consumer data in insurance underwriting](https://www.dfs.ny.gov/reports_and_publications/press_releases/pr202401171). In August 2024, NYDFS issued a [final circular letter on AI use in insurance underwriting and pricing](https://www.alstonprivacy.com/nydfs-issues-final-circular-letter-guidance-on-use-of-ai-in-insurance-underwriting-and-ratings/), focused on fairness and bias. The October 2024 industry letter pivots from bias concerns to cybersecurity risks — addressing both the risks that threat actors' use of AI creates for covered entities, and the risks that covered entities themselves introduce when deploying AI systems.

## Detailed Analysis [HIGH confidence]

### Scope and Covered Entities

The October 16, 2024 industry letter, available in full on the [NYDFS website](https://www.dfs.ny.gov/industry-guidance/industry-letters/il20241016-cyber-risks-ai-and-strategies-combat-related-risks), applies to all "Covered Entities" under Part 500 — defined as any person operating under a license, registration, charter, certificate, permit, accreditation, or similar authorization under the New York Banking Law, Insurance Law, or Financial Services Law. This encompasses:

- State-chartered banks, credit unions, and savings institutions
- Licensed mortgage companies, servicers, and originators
- Licensed money transmitters and check cashers
- Insurance companies and agencies licensed in New York
- Registered investment advisers and broker-dealers regulated by DFS
- New York branches and agencies of foreign banks

The guidance explicitly reaches covered entities' third-party service providers (TPSPs) to the extent those providers access the covered entity's information systems or nonpublic information (NPI) — meaning AI vendors and cloud platforms used by regulated firms are indirectly within scope.

### The Four Primary AI Cybersecurity Risk Categories

NYDFS organizes its analysis around four principal risk categories — two arising from threat actors' use of AI against covered entities, and two arising from covered entities' own deployment of AI systems.

**Risk 1 — AI-Enabled Social Engineering.** NYDFS identifies this as "one of the most significant threats to the financial services sector." Generative AI enables bad actors to create highly realistic deepfake audio, video, and text that can convincingly impersonate executives, employees, regulators, and customers. AI-powered phishing and voice-cloning attacks dramatically lower the skill threshold for social engineering attacks and increase the scale at which they can be conducted. Scenarios include synthetic voice calls impersonating a CFO to authorize wire transfers, AI-generated video calls impersonating clients for account takeovers, and adaptive phishing emails that evade traditional detection.

**Risk 2 — AI-Enhanced Cyberattacks.** AI tools accelerate traditional attack techniques by enabling threat actors to scan for vulnerabilities at scale, generate novel malware and ransomware variants, and evade detection systems more effectively than legacy methods allow. AI-assisted coding dramatically compresses the development time for exploit tools. NYDFS notes that AI can facilitate faster exfiltration of NPI once a network is compromised.

**Risk 3 — Exposure or Theft of Nonpublic Information.** When covered entities deploy AI systems, those systems typically require large volumes of training data, input data, or query data — much of which may constitute NPI under Part 500 or sensitive personal information under other statutes. Concentration of NPI within AI infrastructure (e.g., large language models fine-tuned on customer data, AI-powered fraud detection trained on transaction records) makes those systems high-value targets. NYDFS warns of risks including model inversion attacks, data poisoning, prompt injection, and unauthorized data extraction.

**Risk 4 — Increased Vulnerabilities from Third-Party AI Dependencies.** Covered entities frequently rely on third-party vendors to deliver AI capabilities, including cloud AI services, model APIs, AI-augmented security tools, and data analytics platforms. Each third-party dependency introduces potential failure points: supply chain compromises of the AI vendor, misconfiguration of AI infrastructure, and propagation of breaches from vendor networks into the covered entity's systems. A compromised AI provider can become a gateway for lateral movement into covered entity networks.

### Guidance on Controls and Compliance Measures

NYDFS maps each risk category to existing Part 500 control requirements and provides operational specificity on how those controls should be adapted for the AI threat environment.

**Risk Assessments (§ 500.9).** Covered entities must update their cybersecurity risk assessments to explicitly account for AI-related risks — both those introduced by the entity's own AI use and those arising from threat actors deploying AI against the entity. NYDFS specifies that risk assessments should address: (a) the entity's AI use, including AI embedded in products, operations, and back-office systems; (b) AI used by TPSPs and vendors that have access to the entity's systems or NPI; and (c) specific AI attack vectors including deepfakes, AI-enhanced phishing, automated vulnerability exploitation, and supply chain compromise.

**Third-Party Service Provider Management (§ 500.11).** The letter "strongly recommends" that pre-engagement due diligence on TPSPs include specific diligence on AI-related risks — both risks the TPSP's AI use poses to itself and risks it poses to the covered entity. Required TPSP policies and procedures should address minimum access control and encryption standards, contractual protections, and ongoing monitoring. Given the pace of AI vendor development, NYDFS's emphasis on AI-specific diligence signals that generic TPSP questionnaires will be insufficient; examiners are likely to look for AI-specific due diligence artifacts.

**Access Controls and Multi-Factor Authentication (§ 500.7).** The letter addresses a specific vulnerability: AI-generated deepfakes can defeat some common MFA implementations, particularly those relying on SMS text, voice calls, or video verification. NYDFS recommends that covered entities:

- Avoid SMS text-based, voice-based, or video-based authentication factors where deepfake impersonation is a plausible threat.
- Migrate toward authentication methods resistant to deepfake attacks: hardware security keys (FIDO2/WebAuthn compliant), digital certificates, and device-bound passkeys.
- Implement out-of-band verification protocols for high-risk actions (large wire transfers, account changes, executive approvals).

This recommendation intersects with the 2023 amendment's expanded MFA mandate — covered entities still phasing in MFA compliance under the November 2025 deadline should ensure new MFA implementations use deepfake-resistant factors.

**Cybersecurity Training (§ 500.14).** Part 500 requires annual cybersecurity awareness training for all personnel. The AI letter instructs that this training should now specifically cover: (a) AI-specific attack vectors including deepfake social engineering; (b) the entity's internal policies and procedures for mitigating AI-related risks; and (c) for entities that deploy AI directly, training on how to protect their own AI systems (e.g., secure AI development practices, prompt injection risks, model access controls).

**Monitoring and Vulnerability Management (§ 500.5).** Covered entities should implement continuous monitoring processes capable of detecting AI-specific threats, including anomalous behavior patterns that may indicate AI-assisted attacks, AI-generated communications, and unauthorized access to AI systems or training data.

**Incident Response and Business Continuity (§§ 500.16, 500.17).** Existing incident response plans must be updated to address AI-specific disruptions — including scenarios where a covered entity's AI systems are poisoned, compromised, or taken offline. Business continuity plans should account for reliance on AI-dependent services and the potential unavailability of AI-assisted systems during a cyber incident.

**Data Management and NPI Protection.** NYDFS instructs covered entities to implement strong data governance controls over AI systems that process NPI, including data minimization, encryption, access logging, and restrictions on use of NPI as AI training data unless appropriately authorized.

### Enforcement Signal

Multiple law firm analyses emphasize that while the letter states it creates no new obligations, it functions as a de facto enforcement roadmap. As [Cozen O'Connor](https://www.cozen.com/news-resources/publications/2024/nydfs-issues-guidance-on-cybersecurity-risks-arising-from-artificial-intelligence) observed, the letter "presents a clear signal of NYDFS' interpretation of existing regulations and insight into enforcement priorities." Similarly, [White & Case](https://www.whitecase.com/insight-alert/nydfs-releases-artificial-intelligence-cybersecurity-guidance-covered-entities) noted that the guidance "provides a roadmap of issues the NYDFS might focus on in enforcement proceedings." Covered entities that fail to address the specific risk categories and control gaps identified in the letter should expect those gaps to be highlighted in DFS examinations and used as a basis for findings of Part 500 non-compliance.

## Impact Assessment [HIGH confidence]

### Affected Industries and Entities

All NYDFS-licensed financial institutions are within scope. The practical impact is highest for:

- **Banking institutions** — particular exposure to AI-assisted fraud, synthetic identity theft, and account takeover via deepfake social engineering.
- **Insurance companies** — exposed to AI-enhanced fraud in claims processing and underwriting, plus NPI exposure through AI-driven actuarial and customer data systems.
- **Mortgage servicers and originators** — targeted by AI-assisted synthetic identity and wire transfer fraud.
- **Money transmitters** — high-value targets for AI-assisted social engineering to misdirect transfers.
- **Fintechs licensed by DFS** — often rely heavily on AI and third-party AI infrastructure, increasing supply chain exposure.

### Compliance Timelines and Interaction with 2023 Amendment Deadlines

The October 2024 letter is effective immediately as interpretive guidance. Its interaction with the 2023 amendment's implementation schedule is significant:

- The November 1, 2025 deadline for the 2023 amendment's remaining provisions — including expanded MFA and comprehensive asset inventory — provides a practical compliance window. Covered entities finalizing MFA implementation should incorporate deepfake-resistant authentication factors in that design.
- Entities in the Class A tier face enhanced obligations and should ensure AI-specific controls are embedded in their independent audit programs.
- Ongoing annual TPSP due diligence renewals should be updated to include AI-specific questionnaire elements.

### Consequences of Non-Compliance

Part 500 carries significant enforcement teeth. NYDFS has brought enforcement actions resulting in multi-million dollar penalties, including a $30 million penalty against Robinhood Crypto in 2022, a $50 million civil penalty against Coinbase (plus $50 million compliance investment commitment), and ongoing examinations of other regulated entities for Part 500 deficiencies. The AI guidance will likely be incorporated into NYDFS examination protocols, and gaps in AI risk assessment, TPSP diligence, and training documentation will be citable as Part 500 violations.

## Action Items

- **Update risk assessments immediately.** Amend your 23 NYCRR § 500.9 cybersecurity risk assessment to explicitly address the four AI risk categories identified in the October 2024 letter: AI-enabled social engineering, AI-enhanced attacks, NPI exposure through AI systems, and TPSP AI dependencies.

- **Audit TPSP AI diligence.** Review existing TPSP due diligence questionnaires and contractual provisions to determine whether they capture AI-specific risks. Update questionnaires for all upcoming TPSP renewals and new engagements to include AI risk assessment elements consistent with § 500.11.

- **Review MFA implementations for deepfake resistance.** Audit existing and planned MFA deployments. Where SMS, voice, or video-based authentication is in use for high-risk functions, develop a migration plan toward hardware security keys or digital certificates before the November 1, 2025 expanded MFA deadline.

- **Update annual cybersecurity training curricula.** Before the next required training cycle, add modules covering AI-enabled social engineering (deepfakes, AI phishing), the entity's specific AI-related policies, and — if the entity deploys AI — secure AI usage practices.

- **Update incident response and BCP plans.** Revise your § 500.16 incident response plan to address AI-related scenarios: deepfake-facilitated breaches, compromised AI systems, and AI vendor outages. Update business continuity plans for AI-dependent services.

- **Implement data governance controls for AI systems.** Map all AI systems that process NPI. Ensure data minimization, access logging, encryption, and authorization controls are in place consistent with Part 500 data management requirements.

- **Monitor NYDFS examination activity.** Track NYDFS examination findings and enforcement actions in the AI space as signals of how the agency is applying the October 2024 letter in practice.

## Related Reports

- [reports/privacy/financial-privacy/federal-bank-fintech-tprm-guidance-2024-06-07.md](reports/privacy/financial-privacy/federal-bank-fintech-tprm-guidance-2024-06-07.md) — Covers federal third-party risk management guidance for bank-fintech partnerships, directly relevant to the TPSP AI diligence requirements in the NYDFS letter.
- [reports/privacy/enforcement-actions/federal-ftc-ai-risk-consumer-harm-blog-2025-01.md](reports/privacy/enforcement-actions/federal-ftc-ai-risk-consumer-harm-blog-2025-01.md) — FTC analysis of AI-related consumer harm risks, showing parallel federal regulatory focus on AI as a risk factor under existing statutory frameworks.
- [reports/privacy/financial-privacy/glba-reform-huizenga-discussion-draft-2026-04-12.md](reports/privacy/financial-privacy/glba-reform-huizenga-discussion-draft-2026-04-12.md) — GLBA reform proposal with relevance to financial services data protection obligations that interact with NYDFS Part 500 requirements.

## Sources

1. [NYDFS Industry Letter, October 16, 2024: Cybersecurity Risks Arising from Artificial Intelligence and Strategies to Combat Related Risks](https://www.dfs.ny.gov/industry-guidance/industry-letters/il20241016-cyber-risks-ai-and-strategies-combat-related-risks) — Official text of the primary guidance document from NYDFS.
2. [NYDFS Press Release, October 16, 2024: Superintendent Adrienne A. Harris Issues New Guidance](https://www.dfs.ny.gov/reports_and_publications/press_releases/pr20241016) — Official NYDFS press release announcing the industry letter.
3. [23 NYCRR Part 500 — Cybersecurity Requirements for Financial Services Companies (2023 amended text)](https://www.dfs.ny.gov/system/files/documents/2023/03/23NYCRR500_0.pdf) — Full regulatory text of the NYDFS Cybersecurity Regulation as amended.
4. [NYDFS Second Amendment to 23 NYCRR Part 500 (November 2023)](https://www.dfs.ny.gov/system/files/documents/2023/10/rf_fs_2amend23NYCRR500_text_20231101.pdf) — Text of the November 2023 amendment introducing Class A requirements and expanded MFA obligations.
5. [Debevoise Data Blog: Managing Cybersecurity Risks Arising from AI — New Guidance from the NYDFS (October 20, 2024)](https://www.debevoisedatablog.com/2024/10/20/managing-cybersecurity-risks-arising-from-ai-new-guidance-from-the-nydfs/) — Debevoise & Plimpton analysis of the four risk categories and control expectations.
6. [NYU Compliance and Enforcement: Managing Cybersecurity Risks Arising from AI — New Guidance from the NYDFS (November 11, 2024)](https://wp.nyu.edu/compliance_enforcement/2024/11/11/managing-cybersecurity-risks-arising-from-ai-new-guidance-from-the-nydfs/) — Academic summary of the guidance with focus on compliance implications.
7. [White & Case: NYDFS Releases Artificial Intelligence Cybersecurity Guidance for Covered Entities](https://www.whitecase.com/insight-alert/nydfs-releases-artificial-intelligence-cybersecurity-guidance-covered-entities) — White & Case analysis; notes the guidance as an enforcement roadmap.
8. [Alston & Bird: NYDFS Issues Guidance on Artificial Intelligence-related Cybersecurity Risks](https://www.alstonprivacy.com/nydfs-issues-guidance-on-artificial-intelligence-related-cybersecurity-risks/) — Alston & Bird analysis covering scope, risks, and recommended controls.
9. [Mayer Brown: New York State Department of Financial Services Issues Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence](https://www.mayerbrown.com/en/insights/publications/2024/10/new-york-state-department-of-financial-services-issues-industry-letter-on-cybersecurity-risks-arising-from-artificial-intelligence) — Mayer Brown analysis.
10. [Cozen O'Connor: NYDFS Issues Guidance on Cybersecurity Risks Arising from Artificial Intelligence](https://www.cozen.com/news-resources/publications/2024/nydfs-issues-guidance-on-cybersecurity-risks-arising-from-artificial-intelligence) — Cozen analysis highlighting enforcement signal.
11. [Willkie Farr: NYDFS Issues Industry Guidance Letter on Artificial Intelligence Cybersecurity Risks](https://www.willkie.com/publications/2024/11/nydfs-issues-industry-guidance-letter-on-artificial-intelligence-cybersecurity-risks) — Willkie analysis.
12. [Goodwin: NYDFS Publishes Guidance on AI-Related Cybersecurity Risks](https://www.goodwinlaw.com/en/insights/publications/2024/10/alerts-finance-aiml-nydfs-publishes-guidance-on-the-import) — Goodwin analysis.
13. [Hunton Andrews Kurth: NYDFS Tells Companies to Address AI Security Threats](https://www.hunton.com/privacy-and-information-security-law/nydfs-tells-companies-to-address-ai-security-threats) — Hunton analysis focused on MFA and deepfake authentication risks.
14. [Consumer Financial Services Law Monitor: New York Department of Financial Services Issues New Guidance on Cybersecurity Risks Arising from Artificial Intelligence](https://www.consumerfinancialserviceslawmonitor.com/2024/10/new-york-department-of-financial-services-issues-new-guidance-on-cybersecurity-risks-arising-from-artificial-intelligence/) — Overview and analysis of the guidance.
15. [Inside Privacy (Covington & Burling): NYDFS Issues Industry Guidance on Risks Arising from Artificial Intelligence](https://www.insideprivacy.com/artificial-intelligence/nydfs-issues-industry-guidance-on-risks-arising-from-artificial-intelligence/) — Covington analysis of the guidance and its implications.
16. [Paul Hastings: NYDFS Issues AI Industry Letter](https://www.paulhastings.com/insights/ph-privacy/nydfs-issues-ai-industry-letter) — Analysis from Paul Hastings (original source of the finding).
17. [Hogan Lovells: NYDFS Final Set of Cybersecurity Requirements Under Amended Part 500 Take Effect November 1, 2025](https://www.hoganlovells.com/en/publications/nydfs-final-set-of-cybersecurity-requirements-under-amended-part-500-take-effect-november-1-2025) — Context on November 2025 compliance deadlines for amended Part 500.
18. [NYDFS Press Release, January 2024: Superintendent Harris Proposes Artificial Intelligence Guidance to Combat Discrimination](https://www.dfs.ny.gov/reports_and_publications/press_releases/pr202401171) — Background on NYDFS's earlier AI guidance on insurance underwriting discrimination.
