---
title: "Privacy and Data Security Implications of California's 2024 AI Legislative Package"
date: 2024-11-04
jurisdiction: "California"
category: "privacy"
development_type: "legislation"
finding_id: "SCAN-20241104-033"
topic_key: "california-36070f2b-2024"
topic_type: "state_bill"
topic_key_confidence: "low"
first_reported: 2024-11-04
last_updated: 2026-04-22
status_history:
  - "2026-04-21: Round 1 revision — corrected AB 1836 effective date to January 1, 2025; corrected xAI Corp v. Bonta district to Central District of California and noted preliminary injunction denial (March 4, 2026); corrected SB 1047 compute threshold conjunction from 'or' to 'and'; corrected vetoed bills count to two vetoed (SB 1047, SB 1252) plus AB 3211 to inactive file; updated SB 942 effective date to August 2, 2026 per AB 853 (signed October 2025)."
  - "2026-04-22: Round 2 revision — corrected AB 1836 effective date from January 1, 2025 to January 1, 2026 in narrative section and compliance timeline table."
cluster: "California September 2024 AI Legislative Package (AB 2013, SB 942, and Related Bills)"
cluster_slug: "california-sep-2024-ai-legislative-package"
---

# Privacy and Data Security Implications of California's 2024 AI Legislative Package

**Jurisdiction:** California | **Category:** Privacy | **Date:** 2024-11-04

## Executive Summary [HIGH confidence]

Governor Gavin Newsom signed 18 AI-related bills into law between September 17 and September 28, 2024, after vetoing the high-profile [SB 1047](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB1047) frontier-model safety bill as overly broad. The signed package constitutes the most comprehensive state AI legislative action in the nation to date, covering training data transparency, AI content watermarking and detection, CCPA expansion to cover AI systems and neural data, healthcare AI disclosures, deepfakes, and digital replicas. Four bills — [AB 2013](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2013), [SB 942](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240SB942), [AB 1008](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB1008), and [SB 1223](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240SB1223) — carry the most direct privacy and data security compliance obligations for businesses operating AI systems in or directed at California consumers. Most major provisions take effect January 1, 2025 or later, giving affected organizations limited runway to adapt data governance, vendor contracts, and privacy programs.

## Background [HIGH confidence]

California's 2024 legislative session was dominated by AI regulation, producing an unusually large and diverse body of AI-specific statutes. The session's centerpiece was SB 1047, the "Safe and Secure Innovation for Frontier Artificial Intelligence Models Act," authored by Sen. Scott Wiener. SB 1047 would have required developers of frontier AI models — defined by compute thresholds above $100 million in training costs and 10^26 floating-point operations — to conduct pre-deployment safety assessments, maintain kill-switch capabilities, and implement whistleblower protections. The bill passed the legislature but was [vetoed by Governor Newsom on September 29, 2024](https://www.gov.ca.gov/wp-content/uploads/2024/09/SB-1047-Veto-Message.pdf). In his veto message, Newsom stated that the compute-threshold approach created a "false sense of security" by focusing on model size rather than actual deployment risk, and that smaller models deployed in high-risk contexts could pose equivalent or greater dangers without falling under the bill's scope.

Despite the SB 1047 veto, Newsom simultaneously [announced a comprehensive set of AI initiatives](https://www.gov.ca.gov/2024/09/29/governor-newsom-announces-new-initiatives-to-advance-safe-and-responsible-ai-protect-californians/) and signed the remaining package of AI bills into law. The governor framed the signings as a calibrated, targeted approach that addresses "actual risks" AI poses to Californians — including privacy violations, disinformation, exploitation of likenesses, and threats to children — while preserving conditions for responsible AI innovation.

Prior to 2024, California's primary AI-adjacent legal framework consisted of the California Consumer Privacy Act (CCPA) / California Privacy Rights Act (CPRA) — which did not explicitly address AI systems or neural data — and a patchwork of sector-specific statutes. The CCPA's implementing regulations from the California Privacy Protection Agency (CPPA) had been under development on automated decision-making technology (ADMT), but no comprehensive AI-specific statute had cleared the legislature until this 2024 package. Colorado passed SB 24-205 (the Colorado AI Act) earlier in 2024, but California's breadth and number of bills surpassed that effort significantly.

## Detailed Analysis [HIGH confidence]

### CCPA-Related Bills: AB 1008 and SB 1223

The two bills with the most immediate privacy compliance implications directly amend the CCPA.

**AB 1008 — AI Systems as Personal Information Holders**

[AB 1008](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB1008), signed September 28, 2024 and effective January 1, 2025, amends California Civil Code Section 1798.140(v) to specify that "personal information" exists in various formats, including "abstract digital formats" such as "compressed or encrypted files, metadata, or artificial intelligence systems that are capable of outputting personal information." The bill resolves a previously ambiguous question: whether a generative AI model that has ingested personal information retains that information in a legally cognizable sense, and whether consumers can exercise CCPA rights (deletion, access, opt-out) against the AI system itself.

The bill's author, Rep. Rebecca Bauer-Kahan, drew the analogy to data compression — an AI model that can reproduce a consumer's personal information when prompted is, functionally, storing that information. Without AB 1008, a business could potentially transfer a language model trained on personal data to a buyer and characterize the transaction as outside the CCPA's sale/share rules. The amendment closes that gap. Businesses that develop, procure, or substantially deploy generative AI systems capable of outputting consumer personal information must now evaluate whether CCPA rights attach to those systems and build mechanisms to honor deletion and access requests in the AI context.

**SB 1223 — Neural Data as Sensitive Personal Information**

[SB 1223](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240SB1223), also signed September 28, 2024 and effective January 1, 2025, adds "neural data" as a category of sensitive personal information under CCPA. The bill defines neural data as "information that is generated by measuring the activity of a consumer's central or peripheral nervous system, and that is not inferred from nonneural information." By categorizing neural data as sensitive under Civil Code Section 1798.140, consumers gain the full suite of CCPA sensitive-data rights: the right to limit use and disclosure of neural data, heightened opt-in requirements for minors, and the right to access, delete, and correct.

The practical scope extends to any business collecting electroencephalogram (EEG) data, brain-computer interface data, or related neurotechnology outputs. As the neurotechnology industry expands — including consumer wearables with biometric sensing capabilities — SB 1223 places California at the vanguard of "neurorights" regulation alongside Colorado, which passed similar neural data protections in HB 24-1058. Businesses operating neurotechnology products directed at California consumers must update their CCPA privacy notices, consent mechanisms, and data governance frameworks to treat neural data equivalently to Social Security numbers or genetic data.

### Training Data Transparency: AB 2013

[AB 2013](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2013), signed September 28, 2024 and effective January 1, 2026, requires "developers" of generative AI systems to publicly post documentation about the datasets used to train their systems before making those systems available to California consumers. The bill applies to any generative AI system released on or after January 1, 2022 — creating retroactive disclosure obligations for systems already in the market.

"Developer" is defined broadly to include not only companies that design or produce AI systems, but also companies that "substantially modify" an existing AI system for use by members of the public. Required disclosures must include:

- A high-level summary of training datasets, including sources or owners and the purpose the data serves in training
- Whether datasets contain copyright-protected, trademarked, or patented material
- Whether datasets include personal information as defined under the CCPA, or aggregate consumer information
- Whether datasets were purchased or licensed
- Processing steps applied to the data (cleaning, modification, enhancement) and the purpose of each step
- The timeframe during which data was collected and whether collection is ongoing

AB 2013 is enforced through California's Unfair Competition Law (Business & Professions Code Section 17200), enabling both Attorney General enforcement and private UCL actions. Because the UCL requires a plaintiff to show injury in fact and lost money or property, direct private litigation risk may be moderate — but UCL class actions remain a viable enforcement vector. [Leading AI companies including OpenAI, Anthropic, and Google have published required disclosures](https://www.dglaw.com/ai-legal-updates-californias-ai-training-data-transparency-law-takes-effect/) on their websites in advance of the January 1, 2026 effective date.

### AI Content Transparency: SB 942

[SB 942](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240SB942), the California AI Transparency Act, was signed September 19, 2024 and takes effect August 2, 2026. The original effective date of January 1, 2026 was extended by [AB 853](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB853), signed by Governor Newsom on October 13, 2025, which also imposed new transparency requirements on additional categories of entities effective January 1, 2027 and January 1, 2028. SB 942 applies to "covered providers" — defined as businesses that create, code, or produce generative AI systems averaging over 1 million monthly users or visitors and that are publicly accessible in California.

Covered providers must:
1. Embed an invisible, difficult-to-remove watermark (latent disclosure) in all AI-generated or AI-altered image, video, or audio content produced by their systems
2. Provide users the option to add a visible watermark (manifest disclosure) to such content
3. Make available a free, publicly accessible AI detection tool that allows users to determine whether specific image, video, or audio content was created or altered by the provider's system

SB 942's scope is limited to image, video, and audio — text-only AI outputs are excluded. The civil penalty is $5,000 per violation per day under an action brought by the Attorney General, a city attorney, or county counsel. The million-monthly-user threshold limits the immediate scope of compliance obligations to the largest generative AI platforms, but downstream deployers who substantially modify covered systems may need to assess whether they independently qualify.

### AI Definition Standardization: AB 2885

[AB 2885](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2885), signed September 28, 2024 and effective January 1, 2025, establishes a uniform statutory definition of "artificial intelligence" across California law: "an engineered or machine-based system that varies in its level of autonomy and that can, for explicit or implicit objectives, infer from the input it receives how to generate outputs that can influence physical or virtual environments." The definition tracks the OECD's definition of AI with minor modifications.

While AB 2885 is primarily a conforming definition bill, its significance is substantial: it determines the scope of AI-specific obligations under all California statutes that incorporate or reference this definition. Businesses must assess which of their systems qualify as "AI" under AB 2885 and which obligations in the 2024 package consequently apply.

### Healthcare AI: AB 3030 and SB 1120

Two bills address AI use in healthcare delivery with distinct compliance structures.

[AB 3030](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB3030), effective January 1, 2025, requires health care providers (hospitals, clinics, physician offices) that use generative AI to generate patient communications containing clinical information to include a clear disclaimer indicating AI involvement and directing patients to a human health care provider. The disclaimer format requirements vary: for written communications, it must appear prominently at the beginning; for chat, throughout; for audio, verbally at start and end; for video, displayed throughout. The requirement does not apply when a licensed human health care provider reviews and edits the AI-generated content before it is sent.

[SB 1120](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB1120), effective January 1, 2025, requires AI used for utilization review (UR) or utilization management (UM) functions — coverage determination, prior authorization — to comply with substantive requirements ensuring the AI applies criteria fairly and equitably. Insurers and managed care plans must ensure AI-assisted UR decisions are based on specified clinical information and cannot substitute for physician medical judgment.

### Deepfakes and Digital Replicas

California's 2024 package included a cluster of bills targeting harmful AI-generated synthetic content:

- **[SB 926](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB926)** (signed September 19, 2024): Criminalizes creation and distribution of sexually explicit deepfakes that appear convincingly real and cause the depicted individual "serious emotional distress"
- **[SB 981](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB981)** (signed September 19, 2024): Requires social media platforms to establish reporting mechanisms for deepfake nude content
- **[AB 1836](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB1836)** (signed September 17, 2024, effective January 1, 2026): Prohibits creation of digital replicas of deceased performers in advertising or audiovisual works without estate consent; establishes damages of $10,000 per violation or actual damages
- **[AB 2655](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB2655)** (signed September 17, 2024): Requires large online platforms to identify and remove election-related deepfake content during election periods
- **[AB 2839](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB2839)** (signed September 17, 2024): Prohibits distribution of AI-generated or digitally altered election-related content that falsely depicts a candidate

### Additional Provisions

- **[SB 896](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB896)** (Generative AI Accountability Act): Requires California's Office of Emergency Services to conduct annual risk assessments of generative AI threats to critical infrastructure, with reports to the Legislature. State agencies using AI must disclose AI-generated communications and provide human contact options.
- **[SB 1288](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB1288)**: Establishes an AI in Education working group to develop guidance and model policies addressing academic integrity, data privacy, and equity by 2026.
- **[AB 2876](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB2876)**: Requires the State Board of Education to incorporate AI literacy into curriculum frameworks.
- **[AB 1831](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB1831)**: Extends existing child exploitation material prohibitions to AI-generated depictions.
- **[AB 2905](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB2905)**: Requires robocalls using AI-generated voices to include a disclosure at the start of the call.

### Vetoed Bills

Two AI bills were vetoed by Governor Newsom. SB 1047 (frontier model safety, discussed above) was the highest profile. Newsom also vetoed SB 1252 (social media AI transparency). A third bill, AB 3211 (digital provenance, authenticity, and watermarking standards — partly overlapping with SB 942), was ordered to the inactive file in the Senate before reaching the governor and was therefore not formally vetoed.

## Impact Assessment [HIGH confidence]

**Who Is Directly Affected**

The 2024 package creates tiered obligations across multiple industry verticals:

- **Generative AI developers and providers**: AB 2013 (training data disclosure), SB 942 (watermarking and detection tools), AB 1008 (CCPA liability for AI-held personal data), and AB 2885 (definition scope) all apply. Large-scale consumer-facing GenAI providers face the most immediate compliance burden.
- **Healthcare entities**: Hospitals, clinics, physician practices, health insurers, and managed care plans must comply with AB 3030 (patient communication disclosures) and SB 1120 (UR/UM AI fairness requirements) by January 1, 2025.
- **Neurotechnology businesses**: Any company collecting EEG, BCI, or other neural activity data from California consumers must treat that data as sensitive personal information under CCPA from January 1, 2025.
- **Social media platforms**: SB 981 (deepfake nude reporting mechanisms) and AB 2655 (election deepfake removal) create platform-level content governance obligations.
- **Entertainment and media companies**: AB 1836 creates estate consent requirements for digital replicas of deceased performers in all commercial and expressive works.
- **Political campaigns and advertisers**: AB 2839 and AB 2655 restrict AI-generated political content during election periods.

**Compliance Timelines**

| Bill | Subject | Effective Date |
|------|---------|---------------|
| AB 1008 | CCPA — AI personal information | January 1, 2025 |
| SB 1223 | CCPA — neural data as sensitive PI | January 1, 2025 |
| AB 2885 | AI statutory definition | January 1, 2025 |
| AB 3030 | Healthcare AI patient disclosures | January 1, 2025 |
| SB 1120 | Healthcare UR/UM AI fairness | January 1, 2025 |
| AB 1836 | Digital replicas — deceased performers | January 1, 2026 |
| SB 926 | Deepfake sexual content | January 1, 2025 |
| AB 2013 | GenAI training data transparency | January 1, 2026 |
| SB 942 | AI content watermarking/detection | August 2, 2026 (extended from January 1, 2026 by AB 853, signed Oct. 2025) |

**Enforcement Outlook**

SB 926, AB 1836, AB 2655, and AB 2839 each include a private right of action, creating immediate litigation risk for entertainment companies and political actors. AB 2013 is enforceable through the UCL (both AG and private plaintiffs). SB 942 authorizes civil penalties collectible by the AG, city attorneys, and county counsel. AB 1008 and SB 1223 amendments are enforced through the existing CCPA/CPRA framework, including CPPA administrative enforcement and private claims under the CCPA's limited private right of action for data security breaches.

The CPPA's concurrent development of ADMT rulemaking (addressing automated decision-making profiling) creates a layered regulatory environment where statutory AI obligations and forthcoming agency regulations may interact. Businesses should monitor CPPA rulemaking developments closely.

**Pending Litigation**

AB 2013 has already attracted legal challenge. xAI Corp (Elon Musk's AI company) filed suit in federal court challenging AB 2013 as an unconstitutional compelled disclosure under the First Amendment. The case, [xAI Corp v. Bonta](https://www.courtlistener.com/docket/72086154/xai-llc-v-bonta/) (Case No. 2:25-cv-12295), is pending in the Central District of California. On March 4, 2026, United States District Judge Jesus G. Bernal [denied xAI's motion for a preliminary injunction](https://cdn.arstechnica.net/wp-content/uploads/2026/03/xAI-v-Bonta-Order-Denying-Preliminary-Injunction-3-4-26.pdf), finding that xAI had failed to demonstrate a likelihood of success on its First Amendment, Takings Clause, or vagueness claims. The case remains pending on the merits, but the injunction denial is a significant early setback for xAI and a marker that AB 2013 remains in effect while litigation continues.

## Action Items

- **Assess AI system inventory against AB 2885 definition**: Map all enterprise AI systems to the statutory definition as of January 1, 2025 to determine scope of compliance obligations across the 2024 package.
- **Update CCPA data mapping for AI systems (AB 1008)**: Identify all generative AI systems deployed or procured by your organization capable of outputting personal information; update privacy notices, data subject request procedures, and vendor contracts to address CCPA rights with respect to AI-held data. Deadline: January 1, 2025.
- **Add neural data to CCPA sensitive-data program (SB 1223)**: If your organization processes neural data (EEG, BCI, brain wave data), update privacy notices, consent mechanisms, and data minimization policies to reflect sensitive-data treatment. Deadline: January 1, 2025.
- **Healthcare entities: deploy AB 3030 disclosures**: Health care providers using GenAI for patient communications must add compliant disclaimers before sending any AI-generated clinical messages. Implement review workflows where licensed providers can edit AI outputs to qualify for the exception. Deadline: January 1, 2025.
- **Healthcare payers: audit UR/UM AI tools (SB 1120)**: Insurers and managed care plans must verify that AI-assisted coverage determination tools meet SB 1120's substantive fairness requirements. Deadline: January 1, 2025.
- **Prepare AB 2013 training data disclosures**: GenAI developers and companies that have substantially modified GenAI systems must audit training datasets and prepare website-published documentation meeting AB 2013's content requirements for any system released after January 1, 2022. Deadline: January 1, 2026.
- **Assess SB 942 watermarking obligations**: Determine whether your GenAI system meets the 1-million-monthly-user threshold. If so, implement latent watermarking, manifest watermarking options, and an AI detection tool before August 2, 2026. Note that AB 853 (signed October 2025) also imposed new obligations on large online platforms, source code distributors, and capture device manufacturers taking effect January 1, 2027 and January 1, 2028.
- **Review deepfake and digital replica exposure**: Audit marketing, advertising, and content production practices for AI-generated synthetic content involving real individuals or deceased performers. Ensure estate consent processes are in place for digital replica use under AB 1836.
- **Monitor xAI v. Bonta litigation**: The Central District of California denied xAI's preliminary injunction on March 4, 2026; the merits of the First Amendment challenge remain pending. Track the case for any developments that could affect AB 2013 enforceability.
- **Track CPPA ADMT rulemaking**: The California Privacy Protection Agency's forthcoming automated decision-making technology regulations will layer additional obligations on top of the 2024 statutory package. Engage in comment proceedings as they develop.

## Related Reports

- [reports/ai-law/california/california-ab-2013-genai-training-data-transparency-2024.md](/home/rafal/projecty/Zwiad/reports/ai-law/california/california-ab-2013-genai-training-data-transparency-2024.md) — Detailed compliance analysis of AB 2013's training data transparency requirements for generative AI developers.
- [reports/ai-law/california/california-sb1047-frontier-ai-safety-veto-2024.md](/home/rafal/projecty/Zwiad/reports/ai-law/california/california-sb1047-frontier-ai-safety-veto-2024.md) — Full legislative arc and veto analysis of SB 1047, the frontier AI safety bill Newsom vetoed alongside signing this package.
- [reports/ai-law/state-legislation/california-sb942-ai-transparency-act-2024-10-18.md](/home/rafal/projecty/Zwiad/reports/ai-law/state-legislation/california-sb942-ai-transparency-act-2024-10-18.md) — Focused analysis of SB 942 watermarking and disclosure requirements.
- [reports/privacy/state-comprehensive-laws/colorado-california-neural-data-privacy-laws-2024-10-21.md](/home/rafal/projecty/Zwiad/reports/privacy/state-comprehensive-laws/colorado-california-neural-data-privacy-laws-2024-10-21.md) — Comparative analysis of California SB 1223 and Colorado's parallel neural data privacy protections.
- [reports/ai-law/enforcement-actions/california-xai-v-bonta-ab2013-litigation-2026-04-19.md](/home/rafal/projecty/Zwiad/reports/ai-law/enforcement-actions/california-xai-v-bonta-ab2013-litigation-2026-04-19.md) — First Amendment litigation challenging AB 2013's constitutionality as compelled commercial speech.
- [reports/privacy/state-comprehensive-laws/california-cppa-admt-public-comment-2025-01.md](/home/rafal/projecty/Zwiad/reports/privacy/state-comprehensive-laws/california-cppa-admt-public-comment-2025-01.md) — CPPA's parallel automated decision-making technology rulemaking, which interacts with the 2024 statutory AI package.

## Sources

1. [The Privacy and Data Security Impact of California's Recent AI Bills — Eye on Privacy (Sheppard Mullin)](https://www.eyeonprivacy.com/2024/10/the-privacy-and-data-security-impact-of-californias-recent-ai-bills/) — Primary analysis by Sheppard Mullin attorneys Liisa M. Thomas and Kathryn Smith on privacy/data security implications of the 2024 AI package
2. [The Privacy and Data Security Impact of California's Recent AI Bills — JDSupra](https://www.jdsupra.com/legalnews/the-privacy-and-data-security-impact-of-4063060/) — JDSupra republication of Sheppard Mullin analysis
3. [California Governor Signs AI Governance Measures into Law — Davis Wright Tremaine](https://www.dwt.com/blogs/artificial-intelligence-law-advisor/2024/10/california-governor-signs-ai-laws-vetoes-sb-1047) — Law firm overview of signed bills and SB 1047 veto
4. [California Enacts 17 AI Bills in 2024 — Willkie Compliance Concourse](https://complianceconcourse.willkie.com/articles/california-enacts-17-ai-bills-in-2024/) — Comprehensive list of enacted AI bills
5. [18 AI-Related Laws Governor Newsom Did Not Veto — Winston & Strawn](https://www.winston.com/en/insights-news/18-ai-related-laws-governor-newsom-did-not-veto) — Full enumeration of signed AI legislation
6. [Governor Newsom Announces New Initiatives to Advance Safe and Responsible AI — Governor's Office](https://www.gov.ca.gov/2024/09/29/governor-newsom-announces-new-initiatives-to-advance-safe-and-responsible-ai-protect-californians/) — Official government press release accompanying SB 1047 veto and package signing
7. [SB 1047 Veto Message — Governor's Office](https://www.gov.ca.gov/wp-content/uploads/2024/09/SB-1047-Veto-Message.pdf) — Official veto message with Newsom's reasoning
8. [AB 2013 Official Bill Text — California Legislature](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2013) — Official text of AB 2013 (Generative AI Training Data Transparency)
9. [SB 942 Official Bill Text — California Legislature](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240SB942) — Official text of SB 942 (California AI Transparency Act)
10. [AB 1008 Official Bill Text — California Legislature](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB1008) — Official text of AB 1008 (CCPA and AI personal information)
11. [SB 1223 Official Bill Text — California Legislature](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240SB1223) — Official text of SB 1223 (neural data as sensitive personal information)
12. [AB 2885 Official Bill Text — California Legislature](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2885) — Official text of AB 2885 (statutory AI definition)
13. [Raft of California AI Legislation Adds to Growing Patchwork of US Regulation — White & Case](https://www.whitecase.com/insight-alert/raft-california-ai-legislation-adds-growing-patchwork-us-regulation) — Law firm analysis covering full scope of 2024 AI package
14. [California Governor Signs 18 AI Bills Into Law — ArentFox Schiff](https://www.afslaw.com/perspectives/ai-law-blog/california-governor-signs-18-ai-bills-law) — Overview of all 18 signed bills with enforcement provisions
15. [California's AB 2013 Requires Generative AI Data Disclosure by January 1, 2026 — Crowell & Moring](https://www.crowell.com/en/insights/client-alerts/californias-ab-2013-requires-generative-ai-data-disclosure-by-january-1-2026) — Detailed compliance guidance on AB 2013 obligations
16. [California SB 942 & AB 2013: AI Transparency Compliance Guide — TrustArc](https://trustarc.com/resource/california-ai-transparency-laws-sb942-ab2013/) — Practical compliance guidance for SB 942 and AB 2013
17. [Neural Data as Sensitive Information: Unpacking SB 1223's New Protections — california-ccpa.org](https://california-ccpa.org/blog/neural-data-as-sensitive-information-unpacking-sb-1223s-new-protections/) — Analysis of SB 1223 neural data provisions
18. [California Amends CCPA to Cover Neural Data and Clarify Scope of Personal Information — Hunton Andrews Kurth](https://www.hunton.com/privacy-and-information-security-law/california-amends-ccpa-to-cover-neural-data-and-clarify-scope-of-personal-information) — Law firm analysis of AB 1008 and SB 1223 CCPA amendments
19. [In a Single Day, California Enacts Five Bills Tackling Digital Replicas and Deepfakes — Perkins Coie](https://perkinscoie.com/insights/update/single-day-california-enacts-five-bills-tackling-digital-replicas-and-deepfakes) — Analysis of deepfake and digital replica legislation
20. [California AI Training Data Transparency Law Takes Effect — Davis+Gilbert LLP](https://www.dglaw.com/ai-legal-updates-californias-ai-training-data-transparency-law-takes-effect/) — Report on major AI companies' compliance with AB 2013 by effective date
21. [California SB 1223 — Consumer Privacy: Sensitive Personal Information: Neural Data — CPPA](https://cppa.ca.gov/meetings/materials/20240716_item7_sb_1223.pdf) — CPPA staff analysis of SB 1223 submitted to CPPA Board
22. [California AB 1008 — CCPA Memorandum — CPPA](https://cppa.ca.gov/meetings/materials/20240716_item7_ab_1008_memo.pdf) — CPPA staff memo on AB 1008's interaction with CCPA regulatory framework
23. [AB 853 Official Bill Text — California Legislature](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB853) — Official text of AB 853, which extended SB 942's effective date to August 2, 2026 and added new transparency obligations for additional entity categories
24. [California AI Transparency Act Amendments Signed Into Law — Troutman Pepper](https://www.troutmanprivacy.com/2025/10/california-ai-transparency-act-amendments-signed-into-law/) — Analysis of AB 853's amendments to SB 942, including the effective date extension and new obligations
25. [xAI-v-Bonta Order Denying Preliminary Injunction (March 4, 2026) — Ars Technica / Court Document](https://cdn.arstechnica.net/wp-content/uploads/2026/03/xAI-v-Bonta-Order-Denying-Preliminary-Injunction-3-4-26.pdf) — Official court order by Judge Jesus G. Bernal (C.D. Cal.) denying xAI's motion for preliminary injunction against AB 2013
26. [X.AI LLC v. Rob Bonta, 2:25-cv-12295 — CourtListener](https://www.courtlistener.com/docket/72086154/xai-llc-v-bonta/) — Full docket for xAI Corp v. Bonta in the Central District of California
27. [xAI v. Bonta: A Constitutional Clash for Training Data Transparency — IAPP](https://iapp.org/news/a/xai-v-bonta-a-constitutional-clash-for-training-data-transparency) — Privacy professional analysis of the constitutional issues raised in the xAI litigation
