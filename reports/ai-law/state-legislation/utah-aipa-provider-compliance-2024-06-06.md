---
title: "Utah Artificial Intelligence Policy Act: Practical Compliance Guide for Providers and Businesses"
date: 2024-06-06
jurisdiction: "Utah"
category: "ai-law"
development_type: "legislation"
finding_id: "SCAN-20240606-010"
topic_key: "utah-3670c8f6-2024"
topic_type: "state_bill"
first_reported: 2024-06-06
last_updated: 2026-04-21
status_history:
  - "2026-04-21: Added HB 452 (2025) mental health chatbot coverage; clarified SB 332 as source of sunset extension; added Utah Dept of Commerce Dec 2 2024 press release citation for first mitigation agreement."
cluster: "Utah AI Policy Act (SB 149): Disclosure Framework and Compliance"
cluster_slug: "utah-uaipa-sb149-ai-disclosure"
---

# Utah Artificial Intelligence Policy Act: Practical Compliance Guide for Providers and Businesses

**Jurisdiction:** Utah | **Category:** AI Law | **Date:** June 6, 2024

## Executive Summary [HIGH confidence]

Utah's [Artificial Intelligence Policy Act (UAIPA), enacted as SB 149](https://le.utah.gov/~2024/bills/static/SB0149.html) and signed March 13, 2024, became effective May 1, 2024 — making Utah the first US state to impose binding disclosure obligations specifically targeting generative AI in the private sector. The law creates a two-tier compliance framework: licensed professionals in regulated occupations (including more than 30 healthcare professions, attorneys, accountants, and engineers) must proactively disclose AI use at the outset of consumer interactions, while all businesses engaged in consumer-protection-regulated activities must disclose AI use on request. The Utah Division of Consumer Protection (UDCP) enforces the law with fines up to $2,500 per violation; no private right of action exists. Utah simultaneously established an Office of Artificial Intelligence Policy and a regulatory sandbox (the AI Learning Laboratory) to allow businesses to test AI systems under partial regulatory protection. In 2025, the legislature significantly narrowed the law's disclosure triggers — but the core framework remains in force through at least July 1, 2027. Organizations that have not yet audited their consumer-facing AI tools and implemented required disclosures should treat that gap as an active compliance risk.

## Background [HIGH confidence]

### Utah's First-Mover Position

Utah enacted the UAIPA in the absence of any federal AI disclosure statute and ahead of all other US states. The law amends Utah's existing [Consumer Sales Practices Act](https://le.utah.gov/~2024/bills/static/SB0149.html) — it does not create a standalone AI code. By grafting AI disclosure obligations onto proven consumer-protection enforcement infrastructure, the legislature avoided the need to build new regulatory machinery while gaining access to the UDCP's existing tools: administrative fines, injunctions, and disgorgement.

The brief compliance window was notable: the governor signed SB 149 on March 13, 2024, and the law took effect May 1, 2024 — a window of fewer than seven weeks. Businesses using generative AI in consumer-facing applications were required to implement disclosure mechanisms, audit their tools, and train staff with minimal lead time. [Sheppard Mullin's Healthcare Law Blog](https://www.sheppardhealthlaw.com/2024/06/articles/artificial-intelligence/utah-providers-are-you-complying-with-the-ai-policy-act/) noted in June 2024 that many Utah providers remained out of compliance more than a month after the law took effect.

### The Regulatory Context

Prior to the UAIPA, Utah had enacted the [Utah Consumer Privacy Act](https://le.utah.gov/xcode/Title13/Chapter61/13-61.html) (effective December 31, 2023) as part of the national wave of state comprehensive privacy laws. The UAIPA builds on that foundation. The professional licensing infrastructure referenced in the UAIPA — the "regulated occupation" category — is administered by Utah's Division of Professional Licensing under the Department of Commerce, which regulates more than 60 professions.

## Detailed Analysis [HIGH confidence]

### Scope: Generative AI Covered by the UAIPA

The UAIPA defines "generative AI" as an artificial system that: (a) is trained on data; (b) interacts with a person using text, audio, or visual communication; and (c) generates non-scripted outputs similar to outputs created by a human, with limited or no human oversight. This definition intentionally excludes scripted decision trees and traditional chatbots that deliver pre-authored responses. It squarely targets large-language-model-style systems deployed in consumer-facing settings.

[Orrick confirmed](https://www.orrick.com/en/Insights/2024/04/Utah-AI-Laws-Require-Consumer-Facing-Disclosures-Starting-May-1) that the definition covers AI systems interacting with persons in Utah regardless of where the deploying business is headquartered — a Utah consumer-protective framing that applies geographically.

### Tier 1: Regulated Occupation Disclosure (Proactive)

Providers in "regulated occupations" face the most demanding disclosure tier. A regulated occupation is one regulated by the Utah Department of Commerce that requires a license or state certification. The category is expansive and includes:

- **Healthcare:** Physicians and surgeons, dentists, nurses (RN and LPN), pharmacists, midwives, physical therapists, occupational therapists, genetic counselors, radiology technologists, health facility administrators, social workers, mental health therapists
- **Legal and financial:** Attorneys, CPAs and public accountants
- **Technical:** Architects, engineers, contractors
- **Other:** Over 30 total professions regulated by the Department of Commerce

When a person in a regulated occupation uses generative AI to provide regulated services to a consumer, they must **prominently** disclose that the consumer is interacting with generative AI:

- **Oral/audible interactions:** Verbal disclosure at the start of the conversation, before substantive exchange begins.
- **Electronic/text interactions:** Written disclosure before the written exchange begins.

The disclosure must be proactive and unprompted. Silence — even if the consumer does not ask — is a violation.

### Tier 2: General Consumer Activity Disclosure (On-Request)

Any business that "uses, prompts, or otherwise causes" generative AI to interact with a consumer in connection with activities regulated by the UDCP (consumer sales, telemarketing, charitable solicitations, etc.) must:

- Disclose "clearly and conspicuously" that the consumer is interacting with generative AI and not a human, **when asked or prompted by the consumer**.

The AI system itself must be capable of making this disclosure. Configuring an LLM-based customer service tool to deny being AI, or to deflect the question, would constitute a violation. [Skadden noted](https://www.skadden.com/insights/publications/2024/04/utah-becomes-first-state) that businesses should view AI-generated statements no differently than statements made by their own employees — accountability runs to the deployer.

### The "No AI Defense" Provision

A legally significant provision eliminates a potential litigation defense. Under the UAIPA, it is expressly **not a defense** to a consumer protection violation that generative AI:
- Made the violative statement;
- Undertook the violative act; or
- Was used in furtherance of the violation.

A business cannot escape enforcement by arguing the AI autonomously generated the problematic content. This provision makes deployers strictly accountable for their AI tools' consumer-facing outputs. Compliance programs must treat AI-generated statements as corporate statements.

### Enforcement Structure [HIGH confidence]

Enforcement authority rests exclusively with the **Utah Division of Consumer Protection (UDCP)** and, in limited circumstances, the Utah Attorney General:

- **UDCP administrative fines:** Up to **$2,500 per violation**. Each deceptive act or practice constitutes a separate violation, meaning fines can accumulate rapidly across large-scale consumer interactions.
- **AG civil penalties:** Up to **$5,000 per violation** of an existing administrative or court order.
- **Injunctive relief:** Courts may enjoin continuing violations in UDCP-initiated proceedings.
- **Disgorgement:** Courts may order return of funds obtained through violative AI interactions.
- **No private right of action:** Individual consumers cannot sue under the UAIPA. Enforcement is exclusively governmental.

[Hunton Andrews Kurth confirmed](https://www.hunton.com/privacy-and-cybersecurity-law-blog/utahs-ai-policy-act-now-effective) that UDCP's ordinary enforcement powers under the Consumer Sales Practices Act also apply — meaning the UAIPA's penalties layer on top of existing consumer protection remedies rather than replacing them.

As of mid-2024, no significant public UDCP enforcement actions under the UAIPA had been publicly announced. The enforcement program remains nascent. The absence of a private right of action limits immediate litigation exposure to governmental enforcement, but reputational risk and injunctive relief — which can require operational changes to AI systems — represent the more meaningful near-term compliance drivers.

### Office of Artificial Intelligence Policy and the AI Learning Laboratory [HIGH confidence]

Alongside the disclosure obligations, the UAIPA creates the **Office of Artificial Intelligence Policy** within Utah's Department of Commerce. The Office's director is appointed by the executive director of the Department of Commerce. Its responsibilities include:

- Monitoring AI technological developments and reporting to the legislature and governor.
- Recommending statutory and regulatory changes.
- Coordinating with federal agencies and other states on AI policy.
- Supporting state agencies in AI adoption and governance.
- Providing compliance guidance to businesses.

The Office administers the **AI Learning Laboratory Program** — a regulatory sandbox mechanism. Participants may apply for **regulatory mitigation agreements** lasting up to 12 months, with a single 12-month extension available. Regulatory mitigation may include:

- Reduced fines during the testing period.
- Cure periods before fines are imposed.
- Partial exemptions from specific disclosure requirements while testing novel AI applications.

[GovTech reported](https://www.govtech.com/artificial-intelligence/utah-launches-office-of-artificial-intelligence-policy) that the Office opened in July 2024, with its first subject area focused on AI use in healthcare — specifically mental health applications. The state's first regulatory mitigation agreement was entered with an organization deploying a student-focused mental health chatbot, as confirmed by the [Utah Department of Commerce's December 2, 2024 press release](https://commerce.utah.gov/2024/12/02/news-release-utah-department-of-commerces-office-of-artificial-intelligence-announces-first-regulatory-mitigation-agreement/). Separately, the OAIP partnered with Dentacor to explore AI in dental care.

For organizations developing or deploying novel AI applications in regulated sectors, the Learning Laboratory represents a meaningful compliance risk-mitigation tool during the early enforcement period.

### 2025 Amendments: Narrowed Disclosure Scope [HIGH confidence]

In March 2025, Utah enacted [SB 226](https://le.utah.gov/~2025/bills/static/SB0226.html), [SB 332](https://le.utah.gov/~2025/bills/static/SB0332.html), and [HB 452](https://le.utah.gov/~2025/bills/static/HB0452.html), all effective May 7, 2025, making significant modifications to the UAIPA framework and adding a new layer of sector-specific AI regulation:

1. **High-Risk Threshold for Proactive Disclosure:** Proactive disclosure at the outset of an interaction (previously required for all regulated occupation interactions) is now required only when the AI interaction is **"high-risk"** — defined as one involving: (i) collection of sensitive personal information (health, financial, or biometric data), AND (ii) provision of personalized recommendations or advice that could reasonably be relied upon to make significant personal decisions (medical, mental health, financial, or legal advice).

2. **Clarified Request Standard:** The on-request disclosure trigger requires a **"clear and unambiguous request"** to determine whether an interaction involves AI, narrowing from the original "asked or prompted" standard.

3. **Safe Harbor:** A person is not subject to enforcement if the generative AI system itself "clearly and conspicuously" discloses it is nonhuman at the outset and throughout any consumer interaction.

4. **Sunset Extension (SB 332):** [SB 332](https://le.utah.gov/~2025/bills/static/SB0332.html) specifically extended the UAIPA's sunset date from May 7, 2025 to **July 1, 2027**, preserving the core framework for two additional years.

5. **HB 452 — AI Mental Health Chatbot Obligations:** Enacted alongside the UAIPA amendments, [HB 452](https://le.utah.gov/~2025/bills/static/HB0452.html) creates a new standalone code section titled "Artificial Intelligence Applications Relating to Mental Health." This bill was directly informed by Utah's experience as the first state to enter a regulatory mitigation agreement involving a student-focused AI mental health chatbot. HB 452 applies to any "mental health chatbot" — defined as AI technology using generative AI to engage in conversations with a user "similar to the confidential communications that an individual would have with a licensed mental health therapist," where a supplier represents, or a reasonable person would believe, it can provide mental health therapy or help manage or treat mental health conditions. Key obligations include:

   - **Layered disclosure:** Suppliers must clearly and conspicuously disclose AI identity (a) before the user can access the chatbot, (b) after any gap of more than seven days since the user's last session, and (c) whenever asked by the user. This is a more demanding cadence than the general UAIPA on-request standard.
   - **Advertising transparency:** Any advertisements delivered through the chatbot must be disclosed, and user input may not be used to decide whether to serve advertisements or to customize them.
   - **Data protection:** Suppliers may not sell or share individually identifiable health information or user input with any third party, subject to limited exceptions for health care providers acting with user consent, health plans on user request, and HIPAA-compliant business associate arrangements.
   - **Affirmative defense:** Suppliers can establish an affirmative defense by creating, maintaining, and implementing a qualifying written policy for the chatbot and filing that policy with the UDCP.
   - **Enforcement:** Violations carry administrative fines up to $2,500 per violation under HB 452, layered on top of existing Consumer Sales Practices Act penalties.

   For licensed mental health therapists and healthcare organizations deploying AI-powered therapeutic or wellness chatbots, HB 452 imposes compliance obligations that operate independently of — and in some respects more strictly than — the general UAIPA disclosure tiers. The seven-day re-disclosure cadence and data-sharing prohibition have no equivalent in SB 149 or SB 226. [Perkins Coie](https://perkinscoie.com/insights/update/new-utah-ai-laws-change-disclosure-requirements-and-identity-protections-target), [Sheppard Mullin](https://www.sheppardhealthlaw.com/2025/05/articles/artificial-intelligence/utah-enacts-ai-amendments-targeted-at-mental-health-chatbots-and-generative-ai/), and [Wilson Sonsini](https://www.wsgr.com/en/insights/utah-enacts-mental-health-chatbot-law.html) all identify HB 452 as a material addition to the 2025 Utah AI regulatory package warranting independent compliance assessment.

For healthcare providers, the high-risk definition's two-part test is likely to cover most clinical AI interactions — tools collecting health data and providing patient-specific recommendations remain in the mandatory disclosure zone. [Perkins Coie noted](https://perkinscoie.com/insights/update/new-utah-ai-laws-change-disclosure-requirements-and-identity-protections-target) that the changes represent a meaningful narrowing for non-clinical AI deployments, but regulated healthcare providers still face substantial obligations for core clinical AI tools, and those operating therapeutic chatbot products now face the additional layer of HB 452 requirements.

## Impact Assessment [MEDIUM confidence]

### Who Must Comply

**Regulated occupation providers (Tier 1 — proactive disclosure for high-risk interactions):**
- Healthcare organizations: hospital systems, physician practices, telehealth platforms, digital health apps deploying LLM-based tools that collect health data and provide personalized clinical recommendations.
- Legal professionals: law firms using AI-assisted client communication tools.
- Financial professionals: accountants and financial advisors using AI in client-facing service delivery.
- Engineers, architects, contractors regulated by the Utah Department of Commerce.

**All consumer-facing businesses using generative AI (Tier 2 — on-request disclosure):**
- E-commerce companies with AI customer service chatbots serving Utah consumers.
- Telemarketing firms using AI-voice or AI-text tools.
- Any business deploying LLM-based tools in consumer interactions regardless of jurisdiction of incorporation.

**Mental health chatbot suppliers (HB 452 — independent obligations):**
- Any supplier of an AI-powered chatbot that engages in therapeutic-style conversations with Utah users, or that a reasonable person would believe can provide mental health therapy or manage mental health conditions. This category extends beyond licensed providers to commercial wellness apps, school-based AI tools, and employer-sponsored mental health platforms serving Utah users.

The law's geographic scope reaches any entity using AI to interact with Utah consumers, not just Utah-based businesses.

### Key Compliance Gaps Identified by Practitioners

Multiple law firm analyses identified implementation gaps that remain relevant:

- **Disclosure frequency ambiguity:** The statute does not specify whether disclosure must occur before each individual AI interaction, once per customer session, or once per relationship. Organizations must adopt internal policies on cadence and document the legal rationale.
- **Operator vs. practitioner liability:** When a hospital system deploys AI used by physicians, it is unclear whether the institution, the individual practitioner, or both bear the disclosure obligation. Conservative practice is to ensure both layers of disclosure exist.
- **Vendor configuration:** AI vendors may not have configured their tools to identify as AI in response to consumer requests by default. Vendor agreements should require UAIPA-compliant configuration and include representations about AI disclosure capability.
- **Scope of "provision of regulated services":** Administrative, operational, and back-office AI tools at healthcare organizations may or may not constitute "provision of regulated services" — the line is unresolved pending UDCP guidance.
- **HB 452 scope ambiguity:** The definition of "mental health chatbot" does not require a clinical license. General-purpose wellness or emotional-support AI applications may fall within scope if they present as capable of providing mental health support. Suppliers of such products should assess whether HB 452's data-sharing prohibitions and layered disclosure cadence apply.

## Action Items

- **Immediate audit:** Inventory all generative AI tools deployed in consumer-facing contexts. Classify each tool against the UAIPA "generative AI" definition (trained on data; generates non-scripted human-like outputs via text/audio/visual communication; limited human oversight). Scripted decision trees likely fall outside scope; LLM-based systems do not.
- **Regulated occupation providers:** For any AI tool that interacts with patients, clients, or customers and qualifies as high-risk (collecting sensitive personal data + providing personalized significant-decision advice): implement proactive verbal disclosure for phone/voice interactions and written disclosure banners for digital/chat interfaces before the interaction begins.
- **All covered businesses:** Confirm that all AI chatbots and virtual assistants deployed for Utah consumers are configured to affirmatively identify as AI in response to any clear consumer inquiry. Test this functionality.
- **Mental health chatbot operators (HB 452):** Assess whether any AI-powered therapeutic or wellness chatbot products meet the HB 452 "mental health chatbot" definition. If so: (i) implement pre-access and seven-day re-disclosure flows; (ii) audit data-sharing arrangements for compliance with the IIHI prohibition; (iii) confirm that no user input feeds advertising targeting systems; (iv) draft and file a qualifying written policy with the UDCP to preserve the affirmative defense.
- **No AI defense elimination:** Remove from all consumer protection defense playbooks any argument that shifts liability to the AI system itself for violative statements. Update legal hold procedures to treat AI outputs as corporate statements.
- **Vendor agreements:** Amend AI vendor contracts to include UAIPA compliance representations, require AI self-disclosure configuration, and allocate indemnification responsibility for non-compliant AI outputs.
- **Disclosure frequency policy:** Adopt and document an internal policy on AI disclosure cadence (per-encounter, per-session, or per-relationship) pending UDCP regulatory guidance on adequacy standards.
- **Learning Laboratory assessment:** Evaluate eligibility for the Utah AI Learning Laboratory Program for novel or ambiguous AI use cases. Regulatory mitigation agreements can reduce fine exposure and provide a safe harbor during early enforcement.
- **Monitor UDCP enforcement:** Track enforcement actions as the UDCP's AI compliance program matures. Given the nascent enforcement environment, early enforcement cases will define adequacy standards for disclosures.
- **Track the July 1, 2027 sunset:** Plan for potential additional legislative action or renewal proceedings as the UAIPA approaches its sunset date.

## Related Reports

- [reports/ai-law/state-legislation/utah-uaipa-sb149-ai-disclosure-2024-05-15.md](reports/ai-law/state-legislation/utah-uaipa-sb149-ai-disclosure-2024-05-15.md) -- Comprehensive primary report on the full UAIPA legislative framework, all provisions, and 2025 amendments; this compliance guide extends that analysis with practical implementation steps for providers.
- [reports/ai-law/state-legislation/utah-uaipa-ai-disclosure-cozen-2024-05-15.md](reports/ai-law/state-legislation/utah-uaipa-ai-disclosure-cozen-2024-05-15.md) -- Supplementary healthcare-sector analysis covering implementation ambiguities for licensed clinical providers, disclosure frequency gaps, and vendor liability questions.
- [reports/ai-law/state-legislation/utah-colorado-ai-pioneering-state-laws-2024-06-06.md](reports/ai-law/state-legislation/utah-colorado-ai-pioneering-state-laws-2024-06-06.md) -- Comparative analysis of Utah's disclosure-first model against Colorado's risk-based framework; essential context for multi-state AI compliance programs.
- [reports/ai-law/state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md](reports/ai-law/state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md) -- Colorado's SB 24-205 enforcement delay; organizations operating in both states should coordinate Utah UAIPA compliance with Colorado SB 24-205 preparation.

## Sources

1. [S.B. 149 Artificial Intelligence Amendments — Utah Legislature (Official Text)](https://le.utah.gov/~2024/bills/static/SB0149.html) -- Enrolled bill text; primary source for all statutory definitions, disclosure tiers, and penalty structure
2. [Utah Providers – Are You Complying with the AI Policy Act? — Sheppard Mullin Healthcare Law Blog](https://www.sheppardhealthlaw.com/2024/06/articles/artificial-intelligence/utah-providers-are-you-complying-with-the-ai-policy-act/) -- Primary source for this finding; June 2024 practitioner-oriented compliance analysis from Sheppard Mullin
3. [Utah Becomes First State To Enact AI-Centric Consumer Protection Law — Skadden](https://www.skadden.com/insights/publications/2024/04/utah-becomes-first-state) -- Skadden analysis of "no AI defense" provision and scope of deployer accountability
4. [Utah AI Laws Require Consumer-Facing Disclosures Starting May 1 — Orrick](https://www.orrick.com/en/Insights/2024/04/Utah-AI-Laws-Require-Consumer-Facing-Disclosures-Starting-May-1) -- Orrick analysis of geographic scope and disclosure requirements for both tiers
5. [How the Utah AI Policy Act Impacts Health Professionals — McDermott Will & Emery](https://www.mcdermottlaw.com/insights/how-the-utah-artificial-intelligence-policy-act-impacts-health-professionals/) -- Healthcare-sector analysis; source for list of 30+ regulated health professions and "provision of regulated services" ambiguity
6. [Utah's AI Policy Act Now Effective — Hunton Andrews Kurth](https://www.hunton.com/privacy-and-cybersecurity-law-blog/utahs-ai-policy-act-now-effective) -- Enforcement authority analysis; layered remedies under UAIPA and Consumer Sales Practices Act
7. [Utah Launches Office of Artificial Intelligence Policy — GovTech](https://www.govtech.com/artificial-intelligence/utah-launches-office-of-artificial-intelligence-policy) -- July 2024 office launch; healthcare focus, Dentacor partnership details
8. [First Regulatory Mitigation Agreement — Utah Department of Commerce Press Release (Dec. 2, 2024)](https://commerce.utah.gov/2024/12/02/news-release-utah-department-of-commerces-office-of-artificial-intelligence-announces-first-regulatory-mitigation-agreement/) -- Official announcement of Utah's first regulatory mitigation agreement for a student-focused mental health chatbot
9. [SB 226 — Utah Legislature (2025 Official Text)](https://le.utah.gov/~2025/bills/static/SB0226.html) -- Official enrolled text of 2025 amendment bill; primary source for "high-risk" definition, clarified request standard, and safe harbor provision
10. [SB 332 — Utah Legislature (2025 Official Text)](https://le.utah.gov/~2025/bills/static/SB0332.html) -- Official enrolled text of SB 332; source for sunset extension from May 7, 2025 to July 1, 2027
11. [HB 452 Artificial Intelligence Amendments — Utah Legislature (2025 Official Text)](https://le.utah.gov/~2025/bills/static/HB0452.html) -- Official enrolled text of HB 452; primary source for mental health chatbot definitions, layered disclosure cadence, data-sharing prohibitions, and affirmative defense
12. [New Utah AI Laws Change Disclosure Requirements — Perkins Coie](https://perkinscoie.com/insights/update/new-utah-ai-laws-change-disclosure-requirements-and-identity-protections-target) -- 2025 amendments analysis; covers SB 226, SB 332, and HB 452 as a package; source for narrowed disclosure scope and mental health chatbot provisions
13. [Utah Enacts AI Amendments Targeted at Mental Health Chatbots — Sheppard Mullin Healthcare Law Blog](https://www.sheppardhealthlaw.com/2025/05/articles/artificial-intelligence/utah-enacts-ai-amendments-targeted-at-mental-health-chatbots-and-generative-ai/) -- May 2025 healthcare-focused analysis of HB 452 requirements and compliance implications
14. [Utah Enacts Mental Health Chatbot Law — Wilson Sonsini](https://www.wsgr.com/en/insights/utah-enacts-mental-health-chatbot-law.html) -- Wilson Sonsini analysis of HB 452 scope, obligations, and affirmative defense mechanism
15. [Utah scales back reach of generative AI consumer protection law — Davis Polk](https://www.davispolk.com/insights/client-update/utah-scales-back-reach-generative-ai-consumer-protection-law) -- Davis Polk analysis of SB 226 and SB 332 scope changes; context for sunset extension
