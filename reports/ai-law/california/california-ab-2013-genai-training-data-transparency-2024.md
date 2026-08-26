---
title: "California AB 2013: Generative AI Training Data Transparency Act — Compliance Obligations and Operational Impact"
date: 2024-10-22
jurisdiction: "California"
category: "ai-law"
development_type: "legislation"
finding_id: "SCAN-20241022-008"
topic_key: "california-ab-2013-genai-2024"
topic_type: "legislation"
topic_key_confidence: "high"
first_reported: 2024-10-22
last_updated: 2026-04-16
status_history:
  - "2026-04-16: Corrected bill author from Rebecca Bauer-Kahan to Jacqui Irwin (District 42) per reviewer verification against official legislative record."
---

# California AB 2013: Generative AI Training Data Transparency Act — Compliance Obligations and Operational Impact

**Jurisdiction:** California | **Category:** AI Law | **Date:** October 22, 2024

## Executive Summary [HIGH confidence]

California's [Assembly Bill 2013](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2013), the Generative Artificial Intelligence Training Data Transparency Act (TDTA), was signed by Governor Gavin Newsom on September 28, 2024, and took effect January 1, 2026. The law requires any entity that designs, codes, produces, or substantially modifies a generative AI system or service made publicly available to Californians to post a publicly accessible "high-level summary" of the datasets used to train that system, addressing twelve statutory disclosure categories that span data types, intellectual property status, use of personal information, synthetic data, data processing methods, and collection timeframes. The law applies retroactively to systems released or substantially modified on or after January 1, 2022. There is no user-volume threshold — the statute covers developers of all sizes. AB 2013 contains no dedicated enforcement mechanism or civil penalty schedule, creating reliance on California's Unfair Competition Law for enforcement. On December 29, 2025, xAI filed a federal lawsuit seeking to enjoin the law on First Amendment and Takings Clause grounds; the US District Court for the Central District of California denied the preliminary injunction on March 4, 2026. OpenAI, Anthropic, and Google each posted compliant disclosures by the January 1, 2026 effective date.

## Background [HIGH confidence]

The TDTA emerged from California's 2023–2024 legislative session during which the California legislature advanced more than 50 AI-related bills, positioning the state as the de facto national standard-setter for AI governance. AB 2013 was authored by Assembly Member Jacqui Irwin (District 42) and passed both chambers of the California legislature with bipartisan support during the summer of 2024.

The legislation responds to a recognized gap in AI governance: while AI systems increasingly affect consequential decisions about consumers, third parties, and content consumers encounter, the training data used to develop those systems has historically been treated as proprietary. Policymakers, academic researchers, and civil society advocates had for several years argued that the opacity of training data posed risks to accountability, copyright enforcement, privacy compliance, and fair competition. AB 2013 represents California's targeted legislative response to this accountability gap — distinct from the much broader [SB 1047](https://www.gov.ca.gov/wp-content/uploads/2024/09/SB-1047-Veto-Message.pdf), which Governor Newsom vetoed on September 29, 2024 on grounds that it was not informed by empirical trajectory analysis and might provide a false sense of security.

The legislative context includes California's existing consumer protection infrastructure: the California Consumer Privacy Act (CCPA) and its 2020 amendment (CPRA) already impose data collection and use transparency obligations. AB 2013 extends this transparency posture specifically to the AI training data pipeline rather than the collection of consumer data for AI applications, though it expressly cross-references the CCPA's definition of "personal information."

AB 2013 was part of a package of 17 AI bills signed in September 2024. The companion transparency law, SB 942 (California AI Transparency Act), applies to providers with 1 million or more monthly users and requires content provenance watermarking and a public AI detection tool. AB 2013 has no such user-volume floor and is accordingly broader in reach.

## Detailed Analysis [HIGH confidence]

### Covered Entities

AB 2013 defines a "developer" as "a person, partnership, state or local government agency, or corporation that designs, codes, produces, or substantially modifies an artificial intelligence system or service for use by members of the public." This definition is intentionally broad:

- It captures the full chain of GenAI development — foundation model builders, fine-tuners, and organizations that substantially modify commercially licensed or open-source models.
- There is no revenue threshold, employee count limit, or minimum user-volume trigger.
- The law covers AI systems or services "publicly available to Californians," which as a practical matter means any system accessible via the internet from a California IP address.
- Government agencies are expressly included, though federal entities are carved out by the exemptions (see below).

The law does **not** cover companies that merely integrate or access third-party AI systems via API without substantially modifying the underlying model. Whether "fine-tuning" (a common enterprise adaptation technique) constitutes "substantial modification" is addressed in the statute's definition: substantial modification includes "any new versions or releases or any other material changes to an AI system's functionality or performance, including updates incorporating the results of retraining or fine-tuning of the model." This means that companies deploying customized or fine-tuned versions of open-source or commercial foundation models are likely covered and must publish disclosures about the data used in their fine-tuning.

### The Twelve Disclosure Categories

The statute calls for a "high-level summary" of datasets used in development but then specifies twelve discrete categories of information that must be addressed, per [Goodwin Procter's analysis](https://www.goodwinlaw.com/en/insights/publications/2025/06/alerts-ai-californias-ab-2013-generative-ai-developers-show-their-data). Each covered system or service requires a publicly accessible webpage containing:

1. A description of how the datasets further the intended purpose of the AI system or service.
2. The number of data points included in the datasets (expressed as general ranges if precise counts are impractical).
3. A clear definition of each category associated with data points, including the format of data points and sample values.
4. Whether the datasets include any data protected by copyright, trademark, or patent, or whether they are entirely in the public domain.
5. Whether the datasets were purchased or licensed by the developer.
6. Whether the datasets include personal information as defined by the [CCPA (Cal. Civ. Code § 1798.140)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.140).
7. Whether the datasets include aggregate consumer information.
8. Whether there was any cleaning, processing, or other modification to the datasets by the developer, including the intended purpose of those efforts.
9. The time period during which the data in the datasets were collected, and a notice if data collection is ongoing.
10. The dates the datasets were first used during development.
11. Whether synthetic data generation was used or is continuously used in development.
12. Whether the datasets were used for additional purpose beyond the AI system's development.

While labeled a "high-level summary," categories 2 through 4 in particular — requiring data volume, specific category definitions, and IP status assessments — impose significant investigation obligations on developers. For large-scale models trained on heterogeneous datasets assembled over years, assembling this documentation can require substantial internal audit work.

### Retroactive Application

The TDTA applies to generative AI systems or services released or substantially modified on or after January 1, 2022. This retroactive reach covers the generational cohort of large language models and image generation systems (GPT-3.5, GPT-4, Llama, Stable Diffusion, DALL-E, Gemini, and their successors) that have driven widespread GenAI adoption. Developers must post disclosures for legacy models still in public availability, not just newly released systems.

### Exemptions

AB 2013 exempts:
- Generative AI systems used solely to ensure the security and integrity of information or systems (cybersecurity-only use cases).
- Systems used solely to operate aircraft in the national airspace.
- Systems developed for national security, military, or defense purposes and made available exclusively to a federal agency.

These exemptions are narrow and targeted. There is no general B2B exemption, enterprise-only use exemption, or small developer exception.

### Enforcement Architecture

AB 2013 contains no dedicated enforcement agency, no express civil penalty schedule, and no private right of action. The California legislature's [committee analysis](https://calmatters.digitaldemocracy.org/bills/ca_202320240ab2013) stated that enforcement would likely flow through California's Unfair Competition Law (UCL, Bus. & Prof. Code § 17200 et seq.), which authorizes suits by:
- The California Attorney General
- District attorneys and city attorneys in their jurisdictions
- Private plaintiffs who can demonstrate economic injury and loss of money or property under the UCL's § 17204 standing provision

UCL penalties can reach $2,500 per violation (when brought by government actors), with restitution and injunctive relief also available. The absence of an express penalty schedule creates unpredictability in compliance planning. As of April 2026, the California Attorney General has not announced a formal enforcement initiative specifically targeting AB 2013 compliance.

### Constitutional Litigation: xAI v. Bonta

On December 29, 2025 — two days before the TDTA's effective date — [xAI LLC filed suit](https://natlawreview.com/article/unmaking-grok-elon-musks-xai-sues-california-attorney-general-over-ai-training) in the US District Court for the Central District of California against California Attorney General Rob Bonta, seeking to block enforcement of AB 2013. xAI's constitutional claims include:

- **Fifth Amendment Takings Clause**: AB 2013 effects a per se taking and a regulatory taking by compelling disclosure of trade secrets — specifically, the training data composition of xAI's Grok model — without just compensation.
- **First Amendment**: Compelled disclosure of commercial information regulates speech. xAI argued that the statute's vagueness also fails to give fair notice of what must be disclosed.
- **Fourteenth Amendment Due Process (Vagueness)**: The statute's undefined terms — including "high-level summary" and the scope of required detail for some categories — allegedly fail to provide fair notice of what conduct is proscribed.

On March 4, 2026, [US District Judge Jesus G. Bernal denied xAI's motion for a preliminary injunction](https://www.nortonrosefulbright.com/en-us/knowledge/publications/c1df8419/california-district-court-upholds-transparency-requirements-for-generative-ai-training-data), finding that xAI failed to demonstrate a likelihood of success on the merits of any of its three constitutional claims. On the Takings Clause claim, the court found that compelled disclosure of information — as distinct from physical property or regulatory elimination of economic value — is not a per se taking under established precedent. On the First Amendment claim, the court applied intermediate scrutiny (appropriate for commercial speech regulations) and concluded the statute's transparency interest was substantial. The case remains pending on the merits as of April 2026.

Notably, [OpenAI and Anthropic](https://www.pymnts.com/cpi-posts/ai-developers-avoid-details-in-initial-training-data-disclosures-under-california-statute/) did not file suit and posted disclosures by January 1, 2026. Both addressed all twelve statutory categories but did so at a general level — describing data as broad categories (web content, licensed material, user contributions, AI-generated data) without naming specific datasets. Anthropic disclosed that personal information appears in its training data as a byproduct of publicly available web content and described technical measures to reduce its presence. This early market practice — high-level categorical disclosure rather than dataset-level enumeration — is likely to inform the compliance standard, absent Attorney General guidance.

## Impact Assessment [HIGH confidence]

### Who Is Directly Covered

Because AB 2013 has no user-volume floor, it is far broader in scope than its companion law SB 942:

- **Foundation model developers** (OpenAI, Anthropic, Google, Meta, Mistral, Cohere, etc.) are clearly within scope regardless of size.
- **Fine-tuners and substantially modifying users** — enterprises that retrain or fine-tune open-source or commercial base models on proprietary data — fall within scope if their modified system serves California users.
- **AI-native startups** offering specialized GenAI applications (image generation, code assistants, document summarization) that train custom models are covered.
- **Enterprise internal tools** that are not made "publicly available to Californians" are likely excluded, though the line between enterprise software and publicly available systems can be contested.

### Key Compliance Challenges

**Dataset documentation at scale.** The central operational challenge is assembling provenance documentation for training datasets that may span years, incorporate thousands of heterogeneous source datasets, include web-scraped content with unclear licensing, and have passed through multiple preprocessing pipelines. This requires investment in training data governance infrastructure — data catalogs, provenance tracking systems, and audit processes — that many organizations historically have not maintained.

**Intellectual property assessment.** Category 4 requires a determination of whether datasets contain data protected by copyright, trademark, or patent. For models trained on broad internet scrapes, this is not a trivial determination. Current copyright litigation (ongoing cases against several major AI companies regarding training data) makes this assessment legally fraught: acknowledging copyrighted material in a public AB 2013 disclosure could be used in parallel copyright infringement litigation.

**CCPA personal information nexus.** Category 6 ties directly to CCPA's definition of "personal information" (Cal. Civ. Code § 1798.140(v)), which covers any information that identifies, relates to, or is reasonably capable of being associated with a particular consumer or household. For models trained on public internet content, personal information is almost certainly present. The [Brooks Kushman analysis](https://www.brookskushman.com/insights/navigating-ai-compliance-how-californias-ab-2013-reshapes-genai-operations/) flags that this CCPA cross-reference means compliance counsel must evaluate privacy issues related to training data, not just the disclosure structure.

**Trade secret tension.** Unlike California's trade secret protections under the California Uniform Trade Secrets Act (CUTSA), AB 2013 contains no carve-out allowing developers to withhold information from disclosures on grounds that it constitutes a trade secret. [Baker Botts' November 2024 analysis](https://www.bakerbotts.com/thought-leadership/publications/2024/november/ca-ab-2013_gen-ai-compliance) identifies this as a central strategic tension: disclosures must comply with the statute while minimizing revelation of competitive intelligence about training data composition. The xAI lawsuit's Takings Clause theory elevates this tension to a constitutional question.

**Third-party model liability gap.** Companies that use third-party APIs without fine-tuning (and thus are not "developers" under the statute) are not directly covered. However, those that build on top of open-source models and fine-tune them — a very common enterprise pattern — need to trace disclosure obligations through their own modification of the model plus any datasets added during fine-tuning.

**No prescribed format.** AB 2013 specifies content categories but not format, length, or technical vocabulary for disclosures. The absence of implementing regulations means organizations must make judgment calls about granularity. Early disclosure practices by OpenAI and Anthropic — categorical rather than dataset-specific — suggest the market is converging on a conservative interpretation of "high-level summary," but this has not been validated by the Attorney General.

### Enforcement Exposure

The UCL enforcement model creates meaningful exposure on three tracks:

1. **Attorney General enforcement action**: Although no formal program has been announced, the California AG's office has historically pursued both privacy and consumer protection enforcement aggressively. A wave of non-compliance or a high-profile disclosure inadequacy could trigger AG action.

2. **Private plaintiff litigation**: Private UCL plaintiffs need only allege economic injury — a threshold that can be met by competitors, consumers, or public interest organizations. The breadth of potential plaintiffs increases litigation risk.

3. **Copyright plaintiff discovery use**: AB 2013 disclosures, once public, can be cited in copyright infringement cases as admissions of training data composition.

### Federal Preemption Risk

President Trump signed an executive order in December 2025 establishing a national AI policy framework directed at preempting conflicting state AI laws. The Trump administration has expressed explicit interest in limiting state-level AI regulation. However, as of April 2026, no federal statute has been enacted that would expressly preempt AB 2013. [King & Spalding's January 2026 analysis](https://www.kslaw.com/news-and-insights/new-state-ai-laws-are-effective-on-january-1-2026-but-a-new-executive-order-signals-disruption) notes that state AI transparency laws face meaningful preemption risk if Congress acts, but AB 2013 remains fully operative absent legislative action.

## Action Items

- Audit all generative AI systems or services currently offered (publicly) that could be accessible to California residents, including systems released or substantially modified since January 1, 2022. Confirm whether each falls within AB 2013's "developer" definition — focus on whether the organization designed, coded, produced, or substantially modified the underlying model.
- If fine-tuning or retraining of a third-party or open-source model is part of the deployment architecture, treat the fine-tuning organization as a covered developer for purposes of the fine-tuned model's training data disclosures.
- Develop and publish a compliant training data disclosure webpage for each covered system. Address all twelve statutory categories. Initial industry practice (OpenAI, Anthropic, Google) uses high-level categorical language rather than dataset-specific enumeration — document the rationale for the level of granularity chosen in case of a later enforcement inquiry.
- Conduct an IP assessment of training datasets for copyright, trademark, and patent status, in coordination with IP counsel. If copyright infringement litigation is active or anticipated, coordinate disclosure strategy with litigation counsel to avoid inconsistent statements.
- Evaluate training data sets for CCPA-covered personal information; document what categories of personal information are present and what technical measures (e.g., data cleaning, differential privacy) were applied.
- Establish an ongoing disclosure update process: AB 2013 requires updated disclosures each time a covered system is substantially modified, including updates incorporating fine-tuning results. Build this trigger into model release workflows.
- Monitor xAI v. Bonta (C.D. Cal.) for appellate developments. A Ninth Circuit decision on the First Amendment or Takings Clause theories could materially alter the scope of disclosure obligations or provide a basis for withholding trade-secret-sensitive training data information.
- Track California Attorney General guidance on AB 2013 implementation; no guidance has been issued as of April 2026, and formal guidance would clarify acceptable disclosure granularity.
- Monitor federal AI preemption legislation; if Congress enacts a preemption provision, assess whether AB 2013 disclosures must still be maintained.

## Related Reports

- [California's September 2024 AI Legislative Package: Training Data Disclosure and Content Transparency](../state-legislation/california-ai-training-data-transparency-2024-10-18.md) — Provides the broader context of all 17 California AI bills signed in September 2024, including SB 942's companion content provenance requirements and the SB 1047 veto.
- [Trump Executive Order and National AI Policy Framework: Federal Push to Preempt State AI Laws](../trump-ai-executive-order-state-preemption-2026-04-12.md) — The December 2025 executive order signals federal intent to preempt state AI laws including California's training data transparency requirements.
- [Colorado AI Act Enforcement Delayed to June 30, 2026](../state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md) — Colorado's AI Act presents a parallel state-level AI accountability regime with comparable federal preemption exposure.

## Sources

1. [AB 2013 — Generative Artificial Intelligence: Training Data Transparency (Official Bill Text, leginfo.legislature.ca.gov)](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2013) — Official enrolled bill text; primary statutory authority for all requirement descriptions.
2. [Navigating AI Compliance: How California's AB 2013 Reshapes GenAI Operations — Brooks Kushman PC (via Lexology)](https://www.lexology.com/library/detail.aspx?g=04ad117a-98be-4e35-9b7e-73f3ce6e6e8d) — Original source for this finding; analysis of compliance obligations and CCPA nexus.
3. [How AB 2013 Reshapes GenAI Operations in California — Brooks Kushman PC](https://www.brookskushman.com/insights/navigating-ai-compliance-how-californias-ab-2013-reshapes-genai-operations/) — Primary law firm analysis of compliance challenges and CCPA cross-reference issues.
4. [California's AB 2013: Challenges and Opportunities in Generative AI Compliance — Baker Botts LLP (November 2024)](https://www.bakerbotts.com/thought-leadership/publications/2024/november/ca-ab-2013_gen-ai-compliance) — Analysis of trade secret tensions, compliance strategy, and strategic disclosure framing.
5. [California's AB 2013: Challenges and Opportunities in Generative AI Compliance — Baker Botts/Mondaq](https://www.mondaq.com/unitedstates/new-technology/1550664/californias-ab-2013-challenges-and-opportunities-in-generative-ai-compliance) — Syndicated version of Baker Botts analysis.
6. [California's AB 2013 Requires Generative AI Data Disclosure by January 1, 2026 — Crowell & Moring LLP](https://www.crowell.com/en/insights/client-alerts/californias-ab-2013-requires-generative-ai-data-disclosure-by-january-1-2026) — Analysis of enforcement mechanism via UCL and compliance requirements.
7. [AB 2013: New California AI Law Mandates Disclosure of GenAI Training Data — Perkins Coie](https://perkinscoie.com/insights/update/ab-2013-new-california-ai-law-mandates-disclosure-genai-training-data) — Detailed analysis of scope, definitions, and all required disclosure categories.
8. [California's AB 2013: Generative AI Developers Must Show Their Data — Goodwin Procter (June 2025)](https://www.goodwinlaw.com/en/insights/publications/2025/06/alerts-ai-californias-ab-2013-generative-ai-developers-show-their-data) — Enumerates all 12 statutory disclosure categories; covers scope of "substantial modification."
9. [California's AB 2013 Takes Effect: Navigating AI Training Data Transparency and Trade Secret Risk — Goodwin Procter (January 2026)](https://www.goodwinlaw.com/en/insights/publications/2026/01/alerts-otherindustries-californias-ab-2013-takes-effect) — Post-effective-date analysis of trade secret risks and early disclosure practices.
10. [California's GenAI Data Training Compliance Law AB 2013: Challenges and Practical Next Steps — Mintz (January 2026)](https://www.mintz.com/insights-center/viewpoints/54731/2026-01-15-californias-genai-data-training-compliance-law-ab-2013) — Practical guidance on IP protection strategies within AB 2013 compliance framework.
11. [xAI Files Lawsuit Challenging California AB 2013 — National Law Review](https://natlawreview.com/article/unmaking-grok-elon-musks-xai-sues-california-attorney-general-over-ai-training) — Detailed reporting on xAI's December 2025 constitutional challenge against the TDTA.
12. [xAI's Challenge to California's AI Training Data Transparency Law (AB 2013) — Institute for Law & AI](https://law-ai.org/xais-challenge-to-californias-ai-training-data-transparency-law-ab2013/) — Legal analysis of xAI's Fifth Amendment and First Amendment claims.
13. [xAI v. Bonta: A Constitutional Clash for Training Data Transparency — IAPP](https://iapp.org/news/a/xai-v-bonta-a-constitutional-clash-for-training-data-transparency) — Privacy professional analysis of constitutional dimensions of xAI lawsuit.
14. [California District Court Upholds Transparency Requirements for Generative AI Training Data — Norton Rose Fulbright (March 2026)](https://www.nortonrosefulbright.com/en-us/knowledge/publications/c1df8419/california-district-court-upholds-transparency-requirements-for-generative-ai-training-data) — Report on the March 4, 2026 denial of xAI's preliminary injunction by Judge Bernal.
15. [AI Developers Avoid Details in Initial Training Data Disclosures Under California Statute — PYMNTS](https://www.pymnts.com/cpi-posts/ai-developers-avoid-details-in-initial-training-data-disclosures-under-california-statute/) — Reporting on OpenAI, Anthropic, and Google's compliance approach — high-level categorical disclosures.
16. [AI Legal Updates: California's AI Training Data Transparency Law Takes Effect — Davis+Gilbert LLP](https://www.dglaw.com/ai-legal-updates-californias-ai-training-data-transparency-law-takes-effect/) — Post-effective-date compliance update covering scope and enforcement landscape.
17. [Countdown to Jan. 1, 2026: Preparing for California's New AI Training Data Transparency Obligations — FKKS Technology Law](https://technologylaw.fkks.com/post/102lx5o/countdown-to-jan-1-2026-preparing-for-californias-new-ai-training-data-transp) — Pre-effective-date guidance on building compliance programs for AB 2013.
18. [New State AI Laws Effective January 1, 2026, But a New Executive Order Signals Disruption — King & Spalding](https://www.kslaw.com/news-and-insights/new-state-ai-laws-are-effective-on-january-1-2026-but-a-new-executive-order-signals-disruption) — Federal preemption risk analysis for state AI laws including AB 2013.
19. [AB 2013: Generative Artificial Intelligence: Training Data — CalMatters Digital Democracy](https://calmatters.digitaldemocracy.org/bills/ca_202320240ab2013) — Legislative tracking page with vote history and timeline.
20. [California AI Model Training Disclosure Law Likely Doesn't Violate First Amendment — Reason/Volokh Conspiracy (March 2026)](https://reason.com/volokh/2026/03/10/california-ai-model-training-disclosure-law-likely-doesnt-violate-first-amendment/) — Academic legal analysis supporting the district court's First Amendment reasoning.
21. [SB 1047 Veto Message, Office of Governor Gavin Newsom](https://www.gov.ca.gov/wp-content/uploads/2024/09/SB-1047-Veto-Message.pdf) — Governor's veto message establishing the policy rationale for targeted transparency over broad safety mandates.
