---
title: "Oregon AG Rosenblum Issues AI Guidance Mapping Existing Consumer Protection Laws to AI Systems"
date: 2025-01-14
jurisdiction: "Oregon"
category: "privacy"
development_type: "guidance"
finding_id: "SCAN-20250114-010"
topic_key: "oregon-2c0dd995-2025"
topic_type: "guidance"
first_reported: 2025-01-14
last_updated: 2026-04-16
status_history:
  - "2026-04-16: Revised (r1) — added OCIPA as fourth statute covered by guidance; corrected SB 1546 to reflect Governor Kotek's April 1, 2026 signature; updated UTPA legislative lineage to reference FTC's proposed Unfair Trade Practices and Consumer Protection Law."
cluster: "Oregon AG AI Guidance: Existing Consumer Protection Laws Applied to AI"
cluster_slug: "oregon-ag-ai-guidance-consumer-protection"
---

# Oregon AG Rosenblum Issues AI Guidance Mapping Existing Consumer Protection Laws to AI Systems

**Jurisdiction:** Oregon | **Category:** Privacy | **Date:** December 24, 2024

## Executive Summary [MEDIUM confidence]

On December 24, 2024, Oregon Attorney General Ellen Rosenblum issued [formal guidance titled "What You Should Know About How Oregon's Laws May Affect Your Company's Use of Artificial Intelligence"](https://www.doj.state.or.us/wp-content/uploads/2024/12/AI-Guidance-12-24-24.pdf) as one of her final acts before leaving office. The guidance does not create new law but clarifies that four existing Oregon statutes — the Unlawful Trade Practices Act (UTPA), the Oregon Consumer Privacy Act (OCPA), the Oregon Consumer Information Protection Act (OCIPA), and the Oregon Equality Act — already apply to AI developers and deployers. Businesses that develop, sell, or integrate AI systems in Oregon face meaningful compliance obligations under these laws today, and non-compliance carries potential enforcement risk by the new AG and private plaintiffs. The guidance expressly acknowledges it may require updating depending on Oregon's 2025 legislative session and any changes in federal AI law — a caveat that has proven prescient, as Oregon's legislature subsequently passed SB 1546, a chatbot safety bill, which Governor Kotek signed into law on April 1, 2026.

## Background [HIGH confidence]

Oregon enacted the Oregon Consumer Privacy Act (OCPA) in 2023, with the law taking effect July 1, 2024. The OCPA is modeled on Virginia's CDPA framework and grants Oregon consumers rights including access, deletion, correction, and opt-out of targeted advertising and profiling for consequential decisions. The OCPA defines "sensitive data" more broadly than many peer state laws, encompassing national origin, transgender or nonbinary status, and victim-of-crime status, in addition to more commonly protected categories such as racial and ethnic origin, religious beliefs, health data, sexual orientation, and precise geolocation.

Oregon's Unlawful Trade Practices Act (UTPA), codified at [ORS Chapter 646](https://www.oregonlegislature.gov/bills_laws/ors/ors646.html), has been on the books since 1971. Enacted as an amended version of the [Federal Trade Commission's proposed Unfair Trade Practices and Consumer Protection Law](https://www.oregonlegislature.gov/lpro/Publications/BB2016TheUnlawfulTradePracticesAct.pdf) — a model statute recommended by the Council of State Governments and adopted in various forms across roughly 25 states — the UTPA prohibits deceptive and unfair business practices and grants both the AG and private individuals the right to bring enforcement actions. The Oregon Consumer Information Protection Act (OCIPA), codified at ORS 646A.600–646A.628, requires businesses that possess consumers' personal information to implement reasonable cybersecurity safeguards and to notify consumers and the AG in the event of a data breach. The Oregon Equality Act prohibits discrimination in housing, public accommodations, and employment based on protected characteristics including race, color, religion, sex, sexual orientation, gender identity, national origin, marital status, age, and disability.

The December 2024 guidance was issued against a backdrop of rapid AI adoption and the absence of any Oregon statute specifically regulating AI. AG Rosenblum — who had been a national leader in privacy enforcement during her tenure — used the guidance to signal that her office viewed AI-related misconduct as squarely within its existing authority, while also placing businesses on notice before her successor took office.

## Detailed Analysis [MEDIUM confidence]

### Unlawful Trade Practices Act (UTPA)

The guidance states unambiguously that the "marketing, sale, or use" of AI systems is not exempt from Oregon's UTPA. [Troutman Pepper Locke's analysis](https://www.jdsupra.com/legalnews/oregon-issues-ai-guidance-for-businesses-1957884/) summarizes the key UTPA obligations: a business may violate the UTPA if it fails to disclose a material defect or material nonconformity in an AI product, including when the AI regularly generates false or misleading information and the business does not disclose these limitations to purchasers and end users. The guidance extends this liability upstream: an AI developer may be held "liable to downstream consumers for the harm its products cause," even where the developer is not the direct deployer.

Specific UTPA-triggering conduct identified in the guidance includes: AI-generated fake reviews or deceptive celebrity endorsements; AI-facilitated false price reductions or "flash sales"; AI-powered robocalls that misrepresent caller identity; and any AI system that makes material misrepresentations to consumers, whether directly or through an intermediary. The guidance emphasizes that [complexity does not create exemption](https://www.constangy.com/constangy-cyber-advisor/oregon-attorney-general-issues-ai-guidance-for-businesses) — unpredictability or opacity in AI outputs does not relieve a business of its UTPA duties.

### Oregon Consumer Privacy Act (OCPA)

The guidance applies the OCPA's existing framework directly to AI development and deployment. [Hunton Andrews Kurth's analysis](https://www.hunton.com/privacy-and-information-security-law/or-ag-issues-guidance-regarding-or-state-laws-and-ai) identifies the following obligations the guidance imposes on AI actors:

- **Training data disclosure:** Developers that use personal data to train AI models must clearly disclose that practice in an accessible privacy notice. General-purpose privacy notices that do not specifically reference AI training are insufficient.
- **Sensitive data consent:** If any training data includes OCPA "sensitive data" categories, developers must obtain explicit consumer consent before using that data. This applies regardless of when the data was originally collected.
- **No retroactive notice amendments:** The guidance expressly prohibits "retroactively or passively" altering privacy notices or terms of use to legitimize previously collected data for AI training purposes — a direct warning against the practice some platforms have adopted.
- **Data protection assessments:** The guidance notes that "feeding consumer data into AI models and processing it in connection with these models likely poses heightened risks to consumers," triggering the OCPA's requirement to conduct data protection assessments prior to such processing.
- **Profiling opt-out:** The OCPA already grants consumers the right to opt out of profiling for consequential decisions; the guidance confirms this right applies to AI-driven profiling.

### Oregon Consumer Information Protection Act (OCIPA)

The guidance also addresses AI actors' obligations under the OCIPA (ORS 646A.600–646A.628), Oregon's data security and breach notification law. According to [Securiti's compliance analysis](https://securiti.ai/oregon-ai-guidance/) and [Regulatory Oversight's coverage](https://www.regulatoryoversight.com/2025/01/oregon-ag-rosenblum-issues-ai-guidance-for-businesses/), the guidance requires AI developers who possess consumers' personal information to implement reasonable cybersecurity safeguards for that data. Notably, OCIPA violations are themselves enforceable under the UTPA, linking the two statutes. In the AI context, this means an AI developer whose systems inadequately protect training data or consumer inputs may face dual exposure: a UTPA deceptive practices claim and a standalone OCIPA cybersecurity obligation. The guidance signals that the AG's office intends to read OCIPA as applying to AI pipelines where personal data flows into or through model training and inference processes.

### Oregon Equality Act

The guidance addresses algorithmic bias and its intersection with anti-discrimination law. AI systems that "utilize discretionary inputs or produce biased outcomes that harm individuals based on protected characteristics" may violate the Oregon Equality Act. The guidance offers a concrete example: a rental management company using an AI mortgage approval system that consistently denies qualified applicants based on neighborhood or ethnic-background proxies — because the model was trained on historically biased data — may violate the law regardless of the company's intent.

The practical implication is that businesses cannot escape Equality Act liability by attributing discriminatory outcomes to the AI system rather than to human decision-making. The guidance frames AI developers and deployers as jointly responsible for identifying and mitigating bias during the development process, not after discriminatory outcomes occur.

## Impact Assessment [MEDIUM confidence]

**Who is affected.** The guidance has broad scope. It applies to any Oregon-nexus business that develops AI tools, resells AI-powered products, or integrates third-party AI into its operations. Industries with the most immediate exposure include retail, fintech, real estate, employment platforms, and consumer-facing software vendors — sectors where AI-driven consumer interactions and consequential decisions are already commonplace.

**Compliance requirements and timelines.** There are no new compliance deadlines created by the guidance itself; the underlying statutes are already in effect. Businesses face immediate obligations to: (1) audit privacy notices for OCPA-compliant AI training disclosures; (2) assess whether any sensitive data is used in AI training and obtain required consents; (3) review AI-generated consumer communications for UTPA accuracy and disclosure compliance; (4) conduct or update data protection assessments where AI processing creates heightened consumer risk; and (5) assess whether AI pipelines that handle personal data satisfy OCIPA's reasonable cybersecurity standard.

**Enforcement outlook.** The guidance does not announce any pending investigations, but it puts businesses on constructive notice of the AG's enforcement theory. Oregon's UTPA permits both AG enforcement and private rights of action, meaning non-compliance is not solely dependent on AG priority-setting. The guidance's emphasis on developer liability downstream from deployment is notable — it expands the potential universe of respondents in future enforcement actions beyond the deploying business to the AI vendor.

**2025-2026 legislative context.** As the guidance anticipated, Oregon's legislature moved on AI-specific legislation. In March 2026, the Oregon legislature passed [SB 1546](https://www.troutmanprivacy.com/2026/03/oregon-legislature-passes-bill-regulating-consumer-facing-interactive-ai-with-private-right-of-action/), which regulates consumer-facing interactive AI systems (including AI companions), mandates safety disclosures, and creates a private right of action with statutory damages of $1,000 per violation. [Governor Kotek signed SB 1546 into law on April 1, 2026](https://www.transparencycoalition.ai/news/oregon-lawmakers-pass-major-chatbot-bill-in-significant-win-for-kids-and-ai-safety); it takes effect January 1, 2027. The AG guidance therefore represents the floor of Oregon's regulatory posture, not the ceiling.

## Action Items

- Review all consumer-facing privacy notices to ensure they specifically and clearly disclose any use of consumer personal data in AI model training — generic notice language is likely insufficient under the guidance's standard.
- Audit whether any OCPA "sensitive data" categories are present in AI training datasets; if so, verify explicit consumer consent exists or halt use pending consent collection.
- Document that no retroactive or passive privacy notice amendments have been made to legitimize prior data collection for AI training.
- Conduct or refresh data protection assessments for AI processing activities that involve personal data, particularly where outputs affect consequential consumer decisions.
- Evaluate AI system outputs for potential discriminatory patterns under the Oregon Equality Act, especially in housing, employment, and lending contexts.
- Review AI-generated consumer communications (including automated chat, recommendations, and pricing) for UTPA compliance — accuracy, disclosure of AI involvement, and absence of material omissions.
- Assess whether AI pipelines that process consumer personal information satisfy OCIPA's reasonable cybersecurity standard; implement or document safeguards and breach-notification procedures accordingly.
- Review SB 1546 (signed April 1, 2026, effective January 1, 2027) and assess whether consumer-facing AI systems qualify as "interactive AI" or "AI companions" under the bill's definitions.

## Related Reports

- [reports/privacy/state-comprehensive-laws/florida-oregon-texas-privacy-laws-july-2024-2024-05-15.md](reports/privacy/state-comprehensive-laws/florida-oregon-texas-privacy-laws-july-2024-2024-05-15.md) -- Covers the Oregon Consumer Privacy Act's effective date (July 1, 2024) and core requirements, which form the legal foundation for the AG's AI guidance.
- [reports/privacy/enforcement-actions/texas-tdpsa-ag-enforcement-initiative-2024-06-10.md](reports/privacy/enforcement-actions/texas-tdpsa-ag-enforcement-initiative-2024-06-10.md) -- Parallel state AG enforcement initiative using existing privacy statute authority against digital platforms, illustrating the AG-guidance-to-enforcement pipeline that Oregon may follow.
- [reports/privacy/state-comprehensive-laws/colorado-hb1058-biological-neural-data-2024-05-14.md](reports/privacy/state-comprehensive-laws/colorado-hb1058-biological-neural-data-2024-05-14.md) -- Another state using existing data privacy frameworks to address AI-specific data processing concerns, providing comparative context.

## Sources

1. [Oregon AG AI Guidance (Official PDF) -- doj.state.or.us](https://www.doj.state.or.us/wp-content/uploads/2024/12/AI-Guidance-12-24-24.pdf) -- Official guidance document issued December 24, 2024 by AG Rosenblum; primary source for all substantive provisions including OCIPA obligations.
2. [Oregon Issues AI Guidance for Businesses -- Troutman Pepper Locke / JDSupra](https://www.jdsupra.com/legalnews/oregon-issues-ai-guidance-for-businesses-1957884/) -- Troutman Pepper Locke client analysis of the guidance; source for UTPA and downstream developer liability discussion.
3. [OR AG Issues Guidance Regarding OR State Laws and AI -- Hunton Andrews Kurth](https://www.hunton.com/privacy-and-information-security-law/or-ag-issues-guidance-regarding-or-state-laws-and-ai) -- Law firm analysis covering OCPA training data disclosure and sensitive data consent requirements.
4. [Oregon AG Issues AI Guidance for Businesses -- Constangy Brooks](https://www.constangy.com/constangy-cyber-advisor/oregon-attorney-general-issues-ai-guidance-for-businesses) -- Analysis covering UTPA complexity-does-not-exempt principle and accountability framework.
5. [Oregon attorney general issues advice to businesses on use of AI -- Oregon Capital Chronicle](https://oregoncapitalchronicle.com/2024/12/30/oregon-attorney-general-issues-advice-to-businesses-on-use-of-ai/) -- News coverage providing context on the guidance's issuance and AG Rosenblum's commentary.
6. [Oregon's AI Guidance: What Businesses Need To Know -- Securiti](https://securiti.ai/oregon-ai-guidance/) -- Comprehensive compliance-focused analysis covering all four statutes including OCIPA cybersecurity obligations.
7. [State Attorneys General Issue Guidance On Privacy & AI -- Inside Privacy (Covington)](https://www.insideprivacy.com/state-privacy/state-attorneys-general-issue-guidance-on-privacy-artificial-intelligence/) -- Multi-state context; situates Oregon's guidance within broader state AG AI enforcement trend.
8. [Oregon Legislature Passes SB 1546 -- Troutman Privacy Blog](https://www.troutmanprivacy.com/2026/03/oregon-legislature-passes-bill-regulating-consumer-facing-interactive-ai-with-private-right-of-action/) -- Covers Oregon's subsequent AI-specific legislation (SB 1546, passed March 2026).
9. [ORS Chapter 646 -- Oregon Revised Statutes](https://www.oregonlegislature.gov/bills_laws/ors/ors646.html) -- Official text of Oregon's Unlawful Trade Practices Act; legal basis for UTPA enforcement.
10. [Oregon AG Issues AI Guidance for Businesses -- Regulatory Oversight](https://www.regulatoryoversight.com/2025/01/oregon-ag-rosenblum-issues-ai-guidance-for-businesses/) -- Analysis confirming the guidance covers four statutes including OCIPA and describing OCIPA's AI application.
11. [The Unlawful Trade Practices Act Background Brief -- Oregon Legislature](https://www.oregonlegislature.gov/lpro/Publications/BB2016TheUnlawfulTradePracticesAct.pdf) -- Official Oregon Legislature Research Office brief describing the UTPA's 1971 legislative origins as an amended version of the FTC's proposed Unfair Trade Practices and Consumer Protection Law.
12. [Oregon Governor Signs SB 1546 Chatbot Safety Bill -- Transparency Coalition](https://www.transparencycoalition.ai/news/oregon-lawmakers-pass-major-chatbot-bill-in-significant-win-for-kids-and-ai-safety) -- Confirms Governor Kotek's April 1, 2026 signature on SB 1546.
