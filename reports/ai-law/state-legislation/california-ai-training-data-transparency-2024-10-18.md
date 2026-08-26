---
title: "California's September 2024 AI Legislative Package: Training Data Disclosure and Content Transparency"
date: 2024-10-18
jurisdiction: "California"
category: "ai-law"
development_type: "legislation"
finding_id: "SCAN-20241018-024"
topic_key: "california-5716e04d-2024"
topic_type: "state_bill"
topic_key_confidence: "low"
first_reported: 2024-10-18
last_updated: 2026-04-16
status_history: []
cluster: "California September 2024 AI Legislative Package (AB 2013, SB 942, and Related Bills)"
cluster_slug: "california-sep-2024-ai-legislative-package"
---

# California's September 2024 AI Legislative Package: Training Data Disclosure and Content Transparency

**Jurisdiction:** California | **Category:** AI Law | **Date:** October 18, 2024

## Executive Summary [HIGH confidence]

In September 2024, California Governor Gavin Newsom signed 17 AI-related bills into law while vetoing the controversial SB 1047, collectively representing the most comprehensive state-level AI legislative effort in the United States. The two centerpiece laws — [AB 2013](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2013) (Generative AI Training Data Transparency Act) and [SB 942](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240SB942) (California AI Transparency Act) — require generative AI developers to publicly disclose training data characteristics and embed detectable provenance markers in AI-generated content, effective January 1, 2026. Both laws apply to developers whose systems serve California users. The package also includes bills addressing deepfakes in elections, digital replica protections, AI definitions, healthcare AI disclosures, and AI in education. The veto of SB 1047 — which would have imposed sweeping safety requirements on frontier model developers — signals California's preference for targeted, transparency-focused regulation over broad liability frameworks. As of early 2026, AB 2013 faces a constitutional challenge filed by Elon Musk's xAI, which a federal district court declined to enjoin in March 2026.

## Background [HIGH confidence]

California's legislature advanced more than 50 AI-related bills during the 2023–2024 legislative session, reflecting the state's dual role as home to most major AI developers and the source of significant consumer protection law. The September 2024 bill signings came amid an intense national debate about whether AI regulation should be handled at the state or federal level, with California positioned as the de facto standard-setter given the size of its economy and its consumer protection track record.

The centerpiece of the legislative debate was [SB 1047](https://www.gov.ca.gov/wp-content/uploads/2024/09/SB-1047-Veto-Message.pdf), the Safe and Secure Innovation for Frontier Artificial Intelligence Models Act, which passed both chambers of the legislature with bipartisan support. SB 1047 would have required developers of AI models costing more than $100 million to train to implement full shutdown capabilities, submit written safety-and-security protocols to the state Attorney General, retain annual third-party auditors, and avoid uses creating "unreasonable risk" of "critical harm." The bill drew a rare coalition of supporters including the Center for AI Safety, Elon Musk, Anthropic, and the SAG-AFTRA union, while drawing opposition from Meta, OpenAI, and former House Speaker Nancy Pelosi.

Governor Newsom vetoed SB 1047 on September 29, 2024, characterizing it as "a solution that is not informed by an empirical trajectory analysis of AI systems and capabilities." His [veto message](https://www.gov.ca.gov/wp-content/uploads/2024/09/SB-1047-Veto-Message.pdf) argued the bill "could give the public a false sense of security about controlling this fast-moving technology" by focusing on model cost and size rather than deployment context, and warned that smaller specialized models might pose comparable or greater risks than those the bill targeted. Newsom simultaneously signed 17 other AI bills, framing the package as targeted, evidence-based regulation.

Prior to this package, California had enacted the California Consumer Privacy Act (CCPA) and its 2020 amendment CPRA, giving it the most robust consumer data protection framework in the US. The 2024 AI package extended this regulatory posture into AI governance specifically.

## Detailed Analysis [HIGH confidence]

### AB 2013 — Generative AI Training Data Transparency Act

[AB 2013](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2013), signed September 28, 2024, requires developers of generative AI systems or services publicly available to Californians to post documentation on their websites describing the data used to train their models. The law applies retroactively to systems released or substantially modified on or after January 1, 2022. Key required disclosures include:

- The types of data used (text, images, audio, video, etc.)
- Intellectual property status — whether datasets include copyrighted, trademarked, or patented material
- Whether datasets were purchased or licensed under commercial arrangements
- Whether personal information or aggregate consumer data was included
- Data processing methods applied
- The volume of data (number of data points)
- Whether synthetic data was used
- The time period during which data was collected

The law exempts AI systems whose sole purpose is to ensure data security, physical safety, or operation of aircraft, and systems provided exclusively to federal agencies for national security, military, or defense purposes.

**Enforcement and Penalties:** AB 2013's enforcement structure is notably thin. The text establishes no dedicated enforcement agency or civil penalty schedule. As analyzed by [Crowell & Moring](https://www.crowell.com/en/insights/client-alerts/californias-ab-2013-requires-generative-ai-data-disclosure-by-january-1-2026), enforcement would most likely proceed through California's Unfair Competition Law (UCL), which authorizes action by the Attorney General, district attorneys, and plaintiffs who can demonstrate injury and loss of money or property. Penalty ranges under the UCL — potentially up to $1 million per violation — create significant uncertainty.

**Constitutional Challenge:** On December 29, 2025, xAI (the developer of Grok) filed a federal lawsuit in the US District Court for the Central District of California seeking to block AB 2013 before its January 1, 2026 effective date. xAI alleged violations of the Fifth Amendment (per se takings and regulatory takings by compelling disclosure of trade secrets) and First Amendment (compelled commercial speech), as well as unconstitutional vagueness under the Fourteenth Amendment's Due Process Clause. On March 4, 2026, the [district court denied xAI's motion for a preliminary injunction](https://www.nortonrosefulbright.com/en-us/knowledge/publications/c1df8419/california-district-court-upholds-transparency-requirements-for-generative-ai-training-data), finding xAI failed to demonstrate a likelihood of success on the merits of its Takings Clause claim and concluding the law's commercial speech regulation warranted only intermediate scrutiny — a standard the legislature's transparency interest likely satisfies. OpenAI and Anthropic had already posted AB 2013 disclosures on their websites prior to the ruling.

### SB 942 — California AI Transparency Act

[SB 942](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240SB942), signed September 19, 2024 and effective January 1, 2026, applies to "covered providers" — defined as entities that create, code, or produce a generative AI system with over 1,000,000 monthly visitors or users publicly accessible in California. The law imposes a two-part disclosure regime:

1. **Manifest Disclosures:** Covered providers must offer users an option to include a visible disclosure in AI-generated image, video, or audio content identifying it as AI-generated. The disclosure must be clear, conspicuous, appropriate for the medium, and understandable to a reasonable person.

2. **Latent Disclosures:** AI-generated content must contain embedded provenance data including the provider's name, AI system details, creation timestamp, and a unique identifier. These "watermarks" must meet technical standards capable of detection by a publicly available tool.

3. **Free AI Detection Tool:** Covered providers must make publicly available, at no cost, an AI detection tool enabling users to verify whether image, video, or audio content was generated or altered by their system. The tool must return available provenance data (excluding personal data) and support multiple content formats. Providers must collect user feedback on the tool and implement improvements.

### Other Significant Bills in the Package

**AB 1008 — CCPA Extension to AI Systems:** [AB 1008](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB1008), signed September 28, 2024, amends the CCPA to clarify that "personal information" exists in "abstract digital formats," expressly defined to include AI systems capable of outputting personal information. This extends California's existing privacy law to cover generative AI systems that store or can reproduce personal data.

**AB 2885 — AI Definition:** [AB 2885](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB2885) establishes a uniform statutory definition of "artificial intelligence" across California law, providing a consistent foundation for other AI-specific legislation and reducing definitional inconsistency between statutes.

**AB 1836 — Digital Replica of Deceased Persons:** [AB 1836](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB1836), signed September 17, 2024, prohibits producing, distributing, or making available a digital replica of a deceased personality's voice or likeness in an expressive audiovisual work or sound recording without prior consent from authorized representatives.

**Election Integrity Deepfake Bills:** California enacted multiple bills targeting AI-generated election content:
- **AB 2839**: Bans distribution of materially deceptive AI-generated election content within 120 days before and 60 days after an election. Enforcement was preliminarily enjoined on First Amendment grounds by a federal district court on October 2, 2024.
- **AB 2655 (Defending Democracy from Deepfake Deception Act)**: Requires large online platforms (1M+ California users) to label or remove digitally manipulated content falsely appearing authentic in election contexts.
- **AB 2355**: Requires political advertisements using AI-generated or substantially altered content to include a conspicuous disclosure, effective January 1, 2025.

**SB 926 — AI-Generated CSAM and Intimate Images:** [SB 926](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB926) criminalizes the creation and distribution of AI-generated sexually explicit deepfake content where the distributor knows or should know it will cause serious emotional distress.

**SB 1120 — Healthcare AI:** Regulates use of AI, algorithms, or other software tools in utilization review and management functions by healthcare service plans and disability insurers, effective September 28, 2024.

**AB 3030 — Healthcare AI Disclosures:** Requires health clinics, hospitals, and physicians' offices to provide patients with a disclaimer when written or verbal communications pertaining to patient clinical information were generated using generative AI.

**SB 896 — Emergency AI Risk Assessment:** Requires the California Office of Emergency Services to conduct risk analyses on potential threats posed by generative AI to critical state infrastructure, working with frontier model developers.

**AB 2876 — AI Literacy in Education:** Requires the State Board of Education to consider AI literacy in curriculum frameworks and instructional materials for math, science, and history.

## Impact Assessment [HIGH confidence]

**Who Is Directly Covered**

AB 2013 covers any developer of a publicly available generative AI system or service accessible to Californians — there is no user-volume threshold for application, and the retroactive reach to systems released on or after January 1, 2022, means legacy models are included. SB 942 applies only to providers with 1 million or more monthly users, which as a practical matter targets the largest commercial AI platforms (Google, Meta, OpenAI, Anthropic, xAI, Midjourney, and similar scale operators).

**Compliance Obligations by January 1, 2026**

Organizations in scope for AB 2013 must publish a publicly accessible webpage documenting training data characteristics across each required category. There is no prescribed format for this disclosure — the law calls for a "high-level summary," leaving developers discretion over granularity. Given the Attorney General has not issued implementing guidance, the practical standard for adequate compliance is not fully settled.

SB 942 compliance requires engineering investment: implementing content provenance metadata at generation time (latent disclosures), UI changes to offer manifest disclosure options to users, and deployment of a public-facing AI detection tool. Organizations using third-party AI APIs to generate content should determine whether their upstream provider (if a "covered provider") has discharged these obligations or whether downstream disclosure obligations attach.

**Enforcement Outlook**

The California Attorney General has not announced a formal enforcement initiative tied to January 1, 2026. The UCL enforcement model for AB 2013 creates meaningful plaintiff litigation risk — private plaintiffs who can allege economic injury may bring suits. The xAI constitutional challenge, now past the preliminary injunction stage, is a signal that the litigation landscape remains active. AB 2013's lack of a detailed penalty structure increases unpredictability.

**Federal Preemption Risk**

President Trump signed an executive order in December 2025 establishing a national AI policy framework oriented toward preempting state AI laws. The [federal national AI policy framework](reports/ai-law/federal-regulation/federal-national-policy-framework-ai-preemption-2026-04-14.md) and the DOJ AI Litigation Task Force (established January 9, 2026) create a sustained threat to state laws including California's 2024 package. However, as of the writing of this report, no federal preemption statute has been enacted and California's laws remain in effect.

**Industry Response**

Major AI developers including OpenAI and Anthropic have proactively posted AB 2013 disclosures. The xAI lawsuit represents a dissenting posture. No company has publicly announced SB 942 detection tool non-compliance. The practical sophistication required for robust latent disclosures (consistent with emerging C2PA technical standards) is significant.

## Action Items

- Audit all generative AI systems or services offered to California consumers to determine whether they fall within AB 2013's scope (systems released or substantially modified since January 1, 2022). Assess whether disclosures are already posted; if not, develop compliant training data summaries.
- For covered providers under SB 942, verify that image, video, and audio generation workflows embed latent provenance metadata and that user-facing disclosure options are available. Confirm that a free public AI detection tool is deployed or that contractual arrangements with upstream providers obligate them to provide one.
- Review terms of service and vendor contracts with AI API providers to clarify which party bears disclosure obligations under both AB 2013 and SB 942.
- Monitor the xAI v. California litigation (Central District of California) for appellate developments that could affect the constitutionality or scope of AB 2013 obligations.
- Track California Attorney General guidance on AB 2013 implementation; no guidance has been issued as of April 2026, and any guidance will materially clarify the depth of disclosure required.
- Assess exposure under the election deepfake bills (AB 2839, AB 2655, AB 2355) if your organization operates a large online platform or distributes AI-generated political content in California.
- Monitor federal preemption developments: Congress is considering AI preemption legislation that could supersede parts of California's 2024 package; subscribe to relevant federal rulemaking dockets.

## Related Reports

- [Trump Executive Order and National AI Policy Framework: Federal Push to Preempt State AI Laws](../trump-ai-executive-order-state-preemption-2026-04-12.md) — The December 2025 executive order establishes a national AI policy framework that may preempt California's training data and transparency laws through DOJ enforcement.
- [Colorado AI Act Enforcement Delayed to June 30, 2026](../state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md) — Colorado's AI Act parallels California's approach to algorithmic accountability and faces similar federal preemption headwinds.
- [Colorado Passes Artificial Intelligence Regulatory Bill: Taft Law Analysis of SB 24-205](../state-legislation/colorado-sb24-205-taft-2024-05-31.md) — Colorado's SB 24-205, passed in May 2024, represents the other major state AI regulatory effort of 2024, focusing on high-risk AI system obligations rather than transparency.

## Sources

1. [AB 2013 — Generative Artificial Intelligence: Training Data Transparency Act (Official Bill Text, leginfo.legislature.ca.gov)](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2013) — Official enrolled bill text for AB 2013.
2. [SB 942 — California AI Transparency Act (Official Bill Text, leginfo.legislature.ca.gov)](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240SB942) — Official enrolled bill text for SB 942.
3. [SB 1047 Veto Message, Office of Governor Gavin Newsom](https://www.gov.ca.gov/wp-content/uploads/2024/09/SB-1047-Veto-Message.pdf) — Official veto message articulating Newsom's rationale for rejecting SB 1047.
4. [California's New AI Laws Focus on Training Data, Content Transparency — Cooley LLP](https://www.cooley.com/news/insight/2024/2024-10-16-californias-new-ai-laws-focus-on-training-data-content-transparency) — Primary source alert covering both AB 2013 and SB 942, published October 2024.
5. [California Governor Vetoes AI Safety Bill SB 1047, Signs AB 2013 Requiring Generative AI Transparency — Morgan Lewis](https://www.morganlewis.com/pubs/2024/10/california-governor-vetoes-ai-safety-bill-sb-1047-signs-ab-2013-requiring-generative-ai-transparency) — Law firm analysis of the SB 1047 veto and AB 2013 signing.
6. [Governor Newsom Signs (and Vetoes) Major California AI Legislation — Wilson Sonsini](https://www.wsgr.com/en/insights/governor-newsom-signs-and-vetoes-major-california-ai-legislation.html) — Summary of all 17 signed bills and the SB 1047 veto.
7. [18 AI-Related Laws Governor Newsom Did Not Veto — Winston & Strawn](https://www.winston.com/en/insights-news/18-ai-related-laws-governor-newsom-did-not-veto) — Comprehensive breakdown of each enacted AI bill from the 2024 session.
8. [California's AB 2013 Requires Generative AI Data Disclosure by January 1, 2026 — Crowell & Moring](https://www.crowell.com/en/insights/client-alerts/californias-ab-2013-requires-generative-ai-data-disclosure-by-january-1-2026) — Analysis of enforcement mechanism and compliance requirements.
9. [California Enacts Sweeping New AI Regulation — DLA Piper](https://www.dlapiper.com/en-us/insights/publications/2024/10/california-enacts-sweeping-new-ai-regulation) — Overview of all 18 enacted AI laws including sector-specific bills (insurance, healthcare).
10. [In a Single Day, California Enacts Five Bills Tackling Digital Replicas and Deepfakes — Perkins Coie](https://perkinscoie.com/insights/update/single-day-california-enacts-five-bills-tackling-digital-replicas-and-deepfakes) — Detailed analysis of AB 1836, AB 2839, AB 2655, AB 2355, and SB 926.
11. [California District Court Upholds Transparency Requirements for Generative AI Training Data — Norton Rose Fulbright](https://www.nortonrosefulbright.com/en-us/knowledge/publications/c1df8419/california-district-court-upholds-transparency-requirements-for-generative-ai-training-data) — Report on the March 4, 2026 district court decision denying xAI's preliminary injunction.
12. [xAI's Challenge to California's AI Training Data Transparency Law (AB2013) — Institute for Law & AI](https://law-ai.org/xais-challenge-to-californias-ai-training-data-transparency-law-ab2013/) — Analysis of xAI's constitutional claims under the Fifth and First Amendments.
13. [Here is What's Illegal Under California's 18 (and Counting) New AI Laws — TechCrunch](https://techcrunch.com/2024/09/29/here-is-whats-illegal-under-californias-18-and-counting-new-ai-laws/) — Consumer-accessible summary of the full package with specific prohibitions per law.
14. [AB 2013: Generative Artificial Intelligence: Training Data — CalMatters Digital Democracy](https://calmatters.digitaldemocracy.org/bills/ca_202320240ab2013) — Legislative tracking page with vote history and timeline.
