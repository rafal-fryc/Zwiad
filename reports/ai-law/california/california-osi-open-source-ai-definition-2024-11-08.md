---
title: "OSI Open Source AI Definition v1.0: Criteria, Industry Impact, and Regulatory Implications"
date: 2024-11-08
jurisdiction: "California"
category: "ai-law"
development_type: "guidance"
finding_id: "SCAN-20241108-007"
topic_key: "california-3dcfe7bc-2024"
topic_type: "guidance"
topic_key_confidence: "low"
first_reported: 2024-11-08
last_updated: 2026-04-22
status_history: []
cluster: "OSI Open Source AI Definition (OSAID v1.0): Criteria and Regulatory Impact"
cluster_slug: "osi-open-source-ai-definition-osaid"
---

# OSI Open Source AI Definition v1.0: Criteria, Industry Impact, and Regulatory Implications

**Jurisdiction:** California (Federal / International Implications) | **Category:** AI Law | **Date:** November 8, 2024

## Executive Summary [HIGH confidence]

The [Open Source Initiative (OSI)](https://opensource.org/), a California public benefit corporation, published [Open Source AI Definition (OSAID) v1.0](https://opensource.org/ai/open-source-ai-definition) on October 28, 2024, establishing the first formal definition of "open source AI." The definition requires that any AI system qualifying as open source must grant four essential freedoms — to use, study, modify, and share — and mandates disclosure of model weights, training code, and detailed information about training data. The definition has immediate practical consequences: major models including Meta's Llama 2, Microsoft's Phi-2, and Mistral's Mixtral fail to meet the standard, despite being widely marketed as "open source." OSAID v1.0 carries significant regulatory weight because the EU AI Act (Regulation 2024/1689) grants meaningful compliance exemptions to genuinely open source AI systems, and US federal policymakers are increasingly referencing the definition in public consultations. Organizations deploying or procuring AI systems should understand whether the systems they rely on actually qualify under OSAID — because incorrectly assuming open source status can create legal exposure where regulatory exemptions do not apply.

## Background [HIGH confidence]

### OSI's Role and Corporate Structure

The Open Source Initiative was founded in 1998 and is incorporated as a California public benefit corporation. It is widely regarded as the authoritative body for defining what constitutes "open source" software, having maintained the [Open Source Definition (OSD)](https://opensource.org/osd) for over two decades. The OSD established the baseline criteria — including free redistribution, access to source code, and non-discriminatory licensing — that underpin the open source software ecosystem.

The transition from software to AI systems introduced substantial complexity. Unlike traditional software, AI systems include not only code but also trained model parameters (weights), training datasets, and the computational processes that produce those parameters. The OSD does not map cleanly onto these components, creating definitional ambiguity that OSI sought to resolve through the OSAID project.

### Development Process

OSI began the OSAID development process in 2022. The final v1.0 release followed:

- An international roadshow of community workshops
- A year-long co-design process involving more than 25 organizations
- Input from commercial entities including Microsoft, Google, Amazon, Meta, Intel, and Samsung
- Participation from nonprofit organizations including the Mozilla Foundation, Linux Foundation, Apache Software Foundation, and the United Nations International Telecommunications Union
- Endorsements from more than 20 organizations including the Eleuther AI institute, CommonCrawl Foundation, and the Eclipse Foundation, alongside support from more than 100 individuals

Version 1.0 was announced on [October 28, 2024 at the All Things Open conference](https://opensource.org/blog/the-open-source-initiative-announces-the-release-of-the-industrys-first-open-source-ai-definition).

## Detailed Analysis [HIGH confidence]

### The Four Essential Freedoms

OSAID v1.0 mirrors the traditional software four-freedoms framework but adapts it for AI systems. To qualify as open source AI, a system must be made available under terms that grant:

1. **Freedom to use** — for any purpose, without having to ask for permission
2. **Freedom to study** — how the system works and inspect its components
3. **Freedom to modify** — for any purpose, including to change its output
4. **Freedom to share** — with or without modifications, for any purpose

These freedoms are not merely aspirational; the definition requires that the technical components necessary to exercise each freedom actually be made available to the public.

### Required Disclosures: The Three-Part Stack

For the four freedoms to be meaningful in the AI context, OSAID requires that the following three categories of components be made publicly available under appropriate terms:

**1. Data information:** The complete list of training data, including provenance (where the data came from), how data was processed, and instructions for obtaining or licensing it. Where legally permissible, the actual training dataset must be made available. This requirement is the most contentious: many commercial AI providers use proprietary or licensed datasets that cannot be publicly released.

**2. Code:** The source code used to train the system, create the dataset, and run inferences. This encompasses the model architecture definition and preprocessing code.

**3. Model parameters:** The trained weights and all parameters necessary to run the system. These must be available without conditions that would restrict use, modification, or redistribution.

The OSAID does not mandate a specific license instrument for parameters — they may be free "by their nature" — but any legal mechanism used must preserve all four essential freedoms.

### Models That Qualify vs. Models That Fail

Based on OSI's own assessments, the following AI models meet OSAID requirements:
- **OLMo** (Allen Institute for AI / AI2)
- **Pythia** (Eleuther AI)
- **CrystalCoder** (LLM360)
- **T5** (Google)

The following widely-used models fail to meet OSAID requirements despite being marketed as "open source":
- **Llama 2 and Llama 3** (Meta) — [OSI has explicitly stated](https://opensource.org/blog/metas-llama-license-is-still-not-open-source) that Meta's Llama license is not open source. Meta's license restricts commercial use for applications with over 700 million users, does not release training data, and the data cannot be substantially reconstructed.
- **Phi-2** (Microsoft) — fails training data disclosure requirements
- **Mixtral** (Mistral) — fails full compliance
- **Grok** (X/Twitter) — fails compliance

Meta publicly [rejected the OSI definition](https://www.axios.com/2024/10/29/meta-osi-definition-open-source-ai-llama), stating there "is no single open source AI definition" and that "previous open source definitions do not encompass the complexities of today's rapidly advancing AI models." Some technology companies have begun using the term "open weights" — a more limited descriptor — as an alternative to "open source" for models that release parameters but not training data.

### OSI's "Open Washing" Critique

OSI Executive Director Stefano Maffulli publicly stated that Meta's labeling of the Llama foundation model as open source "confuses users and pollutes the open-source concept." This tension between commercial "open weights" releases and true open source is at the core of why OSI developed the OSAID: to prevent what critics call "open washing" — using open source branding without meeting its substantive requirements.

## Impact Assessment [MEDIUM confidence]

### EU AI Act Regulatory Exemptions

The stakes of the OSAID classification extend to legal compliance. The EU AI Act ([Regulation 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng), in force August 1, 2024) provides significant exemptions for genuinely open source AI:

- Providers of general-purpose AI (GPAI) models released under free and open source licenses are **exempt from obligations** to provide technical documentation to downstream AI system integrators
- Open source GPAI providers established outside the EU are **exempt from the obligation to appoint an authorized EU representative**
- For non-GPAI systems, the AI Act does not apply to third parties making open-source AI publicly available — provided they are not monetizing the product (no paid support, no targeted advertising)

**Critical limitation:** The open source exemptions do **not** apply to:
- GPAI models with "systemic risk" (as defined in Article 51 of the AI Act)
- High-risk AI systems (Annex III categories)
- AI systems used for prohibited purposes (Article 5)
- Even exempt open-source providers must publish a summary of training content and adopt a copyright policy

The consequence is that organizations believing their AI deployments qualify as open source (and thus exempt from certain EU AI Act requirements) must verify that claim against OSAID, not simply against how a vendor markets their product. A system marketed as "open source" by its developer but failing OSAID criteria may not qualify for AI Act exemptions.

### US Federal Policy Landscape

At the US federal level, OSAID v1.0 has been well-received across agency and legislative contexts:

- The [Federal Trade Commission](https://www.ftc.gov/) and the [National Telecommunications and Information Administration](https://www.ntia.doc.gov/) have both supported open source AI models as beneficial for competition, innovation, and security
- A December 2024 House Bipartisan AI Task Force report called for federal investments in open-source AI research and advocated a risk-based approach to monitoring harms
- OSI has participated in roundtables with federal agencies and responded to public calls for comments on AI security and sustainability

However, OSAID remains a private-sector, non-binding standard in the US context. No federal statute currently incorporates it by reference, and Congress has not enacted legislation that would tie regulatory treatment to OSAID compliance.

### Industry Compliance Implications

Organizations that develop, deploy, or procure AI systems should evaluate their models against OSAID for several practical reasons:

1. **EU AI Act compliance planning:** Organizations operating in the EU or serving EU users must determine whether their AI systems qualify for open source exemptions. Assuming a model is exempt based solely on vendor marketing can result in unmet compliance obligations.

2. **Procurement and third-party risk:** Enterprises procuring open source AI for internal use should verify OSAID compliance before relying on open source status for any compliance purpose.

3. **Reputational and labeling risk:** As OSAID becomes the recognized industry standard, mislabeling a model as "open source" when it does not qualify creates reputational and potentially legal risk under consumer protection frameworks.

4. **Model reproducibility:** OSAID's training data disclosure requirements serve a practical function: they enable independent safety evaluations and audits. Organizations that cannot reproduce or audit a model's training data face heightened unknown risk.

## Action Items

- **AI procurement teams:** Before procuring or deploying any AI system described by its vendor as "open source," verify the system's compliance with OSAID criteria — specifically whether model weights, training code, and training data information are all publicly available under open terms.
- **EU compliance programs:** Organizations subject to the EU AI Act should not assume open source exemptions apply to systems marketed as "open source" without verifying OSAID compliance. Engage legal counsel to assess whether specific GPAI models used in your stack qualify for documentation and representation exemptions under Articles 53 and 54 of the AI Act.
- **AI governance policies:** Update AI governance and vendor management policies to incorporate a definition of "open source AI" aligned with OSAID v1.0. Distinguish between "open weights" (parameters only) and fully open source AI.
- **Monitor OSAID evolution:** OSI has indicated it will update the OSAID as the field evolves. Track OSI's published OSAID updates and any federal regulatory guidance that incorporates the definition.
- **Regulatory engagement:** Organizations with positions on open source AI policy should engage with OSI's public consultations and respond to any NIST or NTIA requests for comment that address open source AI frameworks.

## Related Reports

- [reports/ai-law/california/california-sb1047-eu-ai-act-comparative-analysis-2024-11-08.md](reports/ai-law/california/california-sb1047-eu-ai-act-comparative-analysis-2024-11-08.md) — Directly relevant: analyzes the EU AI Act's treatment of open source AI exemptions alongside California SB 1047's model-centric approach, providing the regulatory framework within which OSAID operates.
- [reports/ai-law/california/california-ab-2013-genai-training-data-transparency-2024.md](reports/ai-law/california/california-ab-2013-genai-training-data-transparency-2024.md) — Related: California AB 2013 imposes training data transparency requirements on generative AI developers — parallel to OSAID's training data disclosure criteria.
- [reports/ai-law/california/california-sb1047-frontier-ai-safety-veto-2024.md](reports/ai-law/california/california-sb1047-frontier-ai-safety-veto-2024.md) — Related: California's vetoed frontier AI safety bill was directed at the same large AI model developers whose products are now evaluated against OSAID v1.0.
- [reports/ai-law/state-legislation/california-ai-training-data-transparency-2024-10-18.md](reports/ai-law/state-legislation/california-ai-training-data-transparency-2024-10-18.md) — Related: overlapping subject matter on training data disclosure obligations under California law.

## Sources

1. [OSI: The Open Source Initiative Announces the Release of the Industry's First Open Source AI Definition](https://opensource.org/blog/the-open-source-initiative-announces-the-release-of-the-industrys-first-open-source-ai-definition) — Official OSI press release announcing OSAID v1.0, October 28, 2024
2. [Open Source AI Definition — Open Source Initiative](https://opensource.org/ai) — Official OSI landing page for OSAID with links to the definition text and FAQs
3. [OSI: 2024 End-of-Year Review: Open Source AI Definition v1.0](https://opensource.org/blog/2024-end-of-year-review-open-source-ai-definition-v1-0) — OSI retrospective on OSAID development process, participating organizations, and endorsements
4. [InfoWorld: OSI unveils Open Source AI Definition 1.0](https://www.infoworld.com/article/3593266/osi-unveils-open-source-ai-definition-1-0.html) — Third-party technical analysis of OSAID criteria and which models qualify
5. [TechCrunch: We finally have an 'official' definition for open source AI](https://techcrunch.com/2024/10/28/we-finally-have-an-official-definition-for-open-source-ai/) — News coverage of the OSAID v1.0 release and industry reception
6. [Axios: Meta, OSI tussle over definition of open source AI](https://www.axios.com/2024/10/29/meta-osi-definition-open-source-ai-llama) — Reports on Meta's public rejection of OSAID and the "open washing" dispute
7. [OSI: Meta's LLaMa license is still not Open Source](https://opensource.org/blog/metas-llama-license-is-still-not-open-source) — Official OSI analysis explaining why Meta's Llama license fails OSAID criteria
8. [HPCwire: OSI Open AI Definition Stops Short of Requiring Open Data for LLMs](https://www.hpcwire.com/2024/11/06/osi-open-ai-definition-stops-short-of-requiring-open-data-for-llms/) — Technical analysis of OSAID's training data requirements and industry response
9. [SiliconANGLE: OSI clarifies what makes AI systems open-source, but most 'open' models fall short](https://siliconangle.com/2024/10/28/osi-clarifies-makes-ai-systems-open-source-open-models-fall-short/) — Assessment of which models meet OSAID criteria
10. [Eversheds Sutherland: Opening up about AI: OSI defines open source AI (JDSupra)](https://www.jdsupra.com/legalnews/opening-up-about-ai-osi-defines-open-9549359/) — Law firm client alert on OSAID v1.0 and compliance implications
11. [Orrick: The EU AI Act: Application to Open-Source Projects](https://www.orrick.com/en/Insights/2024/09/The-EU-AI-Act-Application-to-Open-Source-Projects) — Law firm analysis of EU AI Act open source exemptions (Recital 102, Articles 53–54)
12. [Orrick: The EU AI Act: Open-Source Exceptions and Considerations for Your AI Strategy](https://www.orrick.com/en/Insights/2024/05/The-EU-AI-Act-Open-Source-Exceptions-and-Considerations-for-Your-AI-Strategy) — Detailed analysis of exemption scope, limitations, and systemic risk carve-outs
13. [Linux Foundation EU: What Open Source Developers Need to Know about the EU AI Act](https://linuxfoundation.eu/newsroom/ai-act-explainer) — Technical explainer on EU AI Act treatment of open source AI systems
14. [OSI: Ensuring Open Source AI thrives under the EU's new AI rules](https://opensource.org/blog/ensuring-open-source-ai-thrives-under-the-eus-new-ai-rules) — OSI's own analysis of how OSAID interacts with EU AI Act exemptions
15. [InfoQ: OSI Releases New Definition for Open Source AI, Setting Standards for Transparency and Accessibility](https://www.infoq.com/news/2024/11/open-source-ai-definition/) — Technical audience coverage of OSAID requirements and ecosystem implications
