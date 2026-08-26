---
title: "California SB 1047: Safe and Secure Innovation for Frontier Artificial Intelligence Models Act — Full Legislative Arc, Veto, and Follow-On Regulation"
date: 2024-08-15
jurisdiction: "California"
category: "ai-law"
development_type: "legislation"
finding_id: "SCAN-20240815-011"
topic_key: "california-b3fd1bb9-2024"
topic_type: "state_bill"
topic_key_confidence: "low"
first_reported: 2024-08-15
last_updated: 2026-04-21
status_history: []
---

# California SB 1047: Safe and Secure Innovation for Frontier Artificial Intelligence Models Act — Full Legislative Arc, Veto, and Follow-On Regulation

**Jurisdiction:** California | **Category:** AI Law | **Date:** August 15, 2024

## Executive Summary [HIGH confidence]

California Senate Bill 1047, the [Safe and Secure Innovation for Frontier Artificial Intelligence Models Act](https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202320240SB1047), was the most ambitious U.S. state AI safety bill to reach a governor's desk in 2024. Authored by Senator Scott Wiener (D-San Francisco), SB 1047 would have imposed product safety, auditing, and kill-switch obligations on developers of AI models costing more than $100 million to train. The bill passed both chambers of the California legislature with strong margins before Governor Gavin Newsom vetoed it on September 29, 2024. Newsom's [veto message](https://www.gov.ca.gov/wp-content/uploads/2024/09/SB-1047-Veto-Message.pdf) criticized the bill for focusing on model size rather than real-world deployment context, arguing the approach could create a false sense of security while stifling innovation. Although the bill did not become law, its provisions set the template for subsequent California and federal AI safety discussions, and a narrower successor statute — SB 53 — was signed by Newsom on September 29, 2025.

## Background [HIGH confidence]

### The AI Safety Debate in California

By early 2024, California was home to the majority of the world's leading AI model developers — including OpenAI, Anthropic, Google DeepMind, Meta AI, and xAI — making the state a natural regulatory focal point. The national debate over AI safety had intensified following the release of GPT-4 (March 2023), Claude 2 (July 2023), and Gemini (December 2023), along with the publication of model capability evaluation research suggesting that frontier models posed novel and hard-to-predict risks.

Senator Wiener introduced SB 1047 in the 2023–2024 legislative session as a direct response to the absence of federal AI safety legislation. With Congress deadlocked and the Biden Administration's October 2023 executive order on AI safety limited to federal agencies, state-level action appeared to be the most viable near-term avenue for imposing pre-deployment safety requirements on model developers.

### Legislative History

SB 1047 was introduced on February 8, 2024, and underwent substantial amendment between February and August 2024 in response to industry feedback and committee concerns. Key amendments narrowed the definition of "covered model," adjusted penalty structures, and added whistleblower protections. As amended, the bill passed the California State Senate by a [32–1 vote](https://legiscan.com/CA/votes/SB1047/2023) and cleared the State Assembly on August 28, 2024, before being transmitted to the Governor.

The bill attracted unusually sharp divisions within the AI industry itself. [Google, Meta, and OpenAI opposed the bill](https://en.wikipedia.org/wiki/Safe_and_Secure_Innovation_for_Frontier_Artificial_Intelligence_Models_Act), arguing it would harm innovation and create regulatory uncertainty. OpenAI stated that AI regulation should be handled federally. By contrast, Anthropic CEO Dario Amodei wrote that the bill's benefits likely outweighed its costs in its amended form. Elon Musk's xAI supported the bill. In a notable development, at least 113 current and former employees of OpenAI, Google DeepMind, Anthropic, Meta, and xAI signed an open letter to Governor Newsom urging him to sign the bill.

The legislative debate surfaced a fundamental disagreement: whether frontier AI safety requirements should be scoped by computational scale (the SB 1047 approach) or by the context in which a model is deployed (Newsom's stated preference).

## Detailed Analysis [HIGH confidence]

### Scope: What Was a "Covered Model"

Under SB 1047, a "covered model" was defined as an AI model trained:
- Using computing power greater than **10^26 integer or floating-point operations (FLOP)**, and
- At a cost exceeding **$100 million**.

A "covered model derivative" — a fine-tuned version of a covered model — was also subject to the Act if the fine-tuning itself cost more than **$10 million**. This dual threshold was designed to capture only frontier-scale models, excluding the vast majority of commercial and open-source models. At the time of introduction, a small number of models from a handful of developers met or approached these thresholds.

### Developer Obligations

The bill imposed a layered set of pre-training, pre-deployment, and ongoing obligations on developers of covered models, as analyzed by [Gibson Dunn](https://www.gibsondunn.com/regulating-the-future-eight-key-takeaways-from-californias-sb-1047-vetoed-by-governor-newsom/) and [Morgan Lewis](https://www.morganlewis.com/pubs/2024/08/californias-sb-1047-would-impose-new-safety-requirements-for-developers-of-large-scale-ai-models):

**1. Safety and Security Protocol.** Before initiating training of a covered model, a developer would be required to create a written safety and security protocol with guidance from the Government Operations Agency. This document would need to cover the developer's approach to assessing and mitigating potential critical harms.

**2. Pre-Deployment Assessment.** Before making a covered model publicly available, a developer would be required to assess whether the model could cause critical harm, record and retain all test results, and submit a compliance statement to the California Attorney General confirming that reasonable care was taken to prevent critical harms.

**3. Kill Switch / Shutdown Capability.** Developers would be required to maintain the technical capability to fully shut down any covered model — a provision widely described as a "kill switch" or "circuit breaker." This requirement also extended to compute providers, who would need to implement policies enabling shutdown of compute resources used to train covered models.

**4. Annual Third-Party Audits.** Beginning January 1, 2026, developers would be required to retain a third-party auditor annually to assess compliance with the Act. Redacted versions of audit reports would be published; unredacted versions would be provided to the Attorney General on request.

**5. Incident Reporting.** Developers would be required to report each AI safety incident involving a covered model to the Attorney General within 72 hours of discovery. The bill also included provisions for reporting to the Government Operations Agency.

**6. Whistleblower Protections.** The bill created protections for employees who disclosed information about AI safety risks, including protections against retaliation.

### Critical Harms Definition

The bill defined "critical harms" with respect to four categories:
- Creation or use of a chemical, biological, radiological, or nuclear (CBRN) weapon with potential for mass casualties
- Cyberattacks on critical infrastructure causing mass casualties or at least **$500 million** in damage
- Autonomous crimes (i.e., AI acting without human direction) causing mass casualties or at least **$500 million** in damage
- Other attacks on critical safety systems

### Enforcement and Penalties

The California Attorney General would be authorized to seek civil penalties of up to **10% of the initial cost of model development** for a first violation, and up to **30% of development costs** for subsequent violations. For a model costing $100 million to train, this would imply potential first-violation penalties of $10 million and repeat-violation penalties of $30 million.

### CalCompute Initiative

SB 1047 also contained a provision establishing **CalCompute**, a public cloud computing cluster administered through the University of California system, intended to provide AI compute access for startups, academic researchers, and community groups who cannot afford commercial compute at scale.

### Open Source Implications

A significant concern raised by critics — including [Andreessen Horowitz](https://a16z.com/sb-1047-what-you-need-to-know-with-anjney-midha/) — was that SB 1047 would apply to open-source model releases meeting the compute threshold. Open-source developers would face the same pre-deployment compliance requirements as commercial developers, a significant burden given that open-source projects typically lack the legal and compliance infrastructure of large corporations.

## Governor's Veto Analysis [HIGH confidence]

Governor Newsom vetoed SB 1047 on September 29, 2024, returning the bill to the legislature without his signature. His [official veto message](https://www.gov.ca.gov/wp-content/uploads/2024/09/SB-1047-Veto-Message.pdf) articulated three principal objections:

**1. Compute-Scale Regulation Is Insufficiently Targeted.** Newsom argued that SB 1047's framework — which triggered obligations based solely on training compute and cost — was "not informed by an empirical trajectory analysis of AI systems and capabilities." He stated that the bill "applies stringent standards to even the most basic functions" performed by large models, regardless of how dangerous those functions actually are.

**2. Risk of False Security.** The Governor warned that by focusing only on large, expensive models, the bill "could give the public a false sense of security about controlling this fast-moving technology." He noted that "[s]maller, specialized models may emerge as equally or even more dangerous than the models targeted by SB 1047."

**3. Deployment Context Matters More Than Model Size.** Newsom expressed a clear preference for a risk-tiering framework based on how models are deployed — "whether an AI system is deployed in high-risk environments, involves critical decision-making or the use of sensitive data" — rather than their raw computational scale.

Despite the veto, Newsom endorsed the underlying regulatory goal: "Safety protocols must be adopted. Proactive guardrails should be implemented, and severe consequences for bad actors must be clear and enforceable." He indicated that a California-specific approach might be warranted absent federal action, but that it must be based on "empirical evidence and science."

The [Perkins Coie analysis](https://perkinscoie.com/insights/update/implications-california-governor-newsoms-veto-ai-safety-bill-sb-1047) of the veto noted that Newsom's reasoning implies future regulation may be broader in scope (covering smaller models) but more targeted in application (filtering by deployment risk rather than training scale).

## Impact Assessment [MEDIUM confidence]

### Immediate Impact: AI Developers Relieved of Obligations

Because SB 1047 was vetoed, no compliance obligations under the Act ever took effect. Developers of large frontier models — OpenAI, Anthropic, Google DeepMind, Meta, Microsoft — faced no legal exposure under California law solely on account of training compute scale.

### Signal for Regulatory Direction

The bill's passage through the legislature — even without the Governor's signature — sent a clear signal to the AI industry that state-level product safety legislation for frontier models had political viability. The near-miss prompted many large developers to accelerate voluntary safety commitments and internal auditing processes in anticipation of eventual regulation.

### Simultaneous Legislation: AB 2013 Signed

On September 28, 2024 — one day before vetoing SB 1047 — Newsom signed [AB 2013, the Generative AI Training Data Transparency Act](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2013). Unlike SB 1047, AB 2013 received unanimous legislative support (38–0 in the Senate, 75–0 in the Assembly). AB 2013 requires developers of generative AI systems to publicly disclose on their websites a high-level summary of training data sources by January 1, 2026, and applies retroactively to any AI system made publicly available in California from January 1, 2022 onward. This simultaneous signing-and-veto pattern illustrated Newsom's preference for transparency obligations over pre-deployment safety mandates.

### Follow-On Legislation: SB 53 (2025)

California ultimately enacted a narrower frontier AI statute in 2025. On September 29, 2025, Newsom signed [SB 53, the Transparency in Frontier Artificial Intelligence Act (TFAIA)](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB53), also authored by Senator Wiener. As analyzed by [Future of Privacy Forum](https://fpf.org/blog/californias-sb-53-the-first-frontier-ai-law-explained/) and [Mayer Brown](https://www.mayerbrown.com/en/insights/publications/2025/10/california-enacts-sb-53-creating-new-requirements-for-developers-of-frontier-artificial-intelligence-models-and-related-whistleblower-provisions), SB 53:

- Requires frontier AI developers to publish safety frameworks (governance documentation and transparency reports)
- Mandates reporting of critical safety incidents to the California Office of Emergency Services within 15 days of discovery (24 hours for incidents posing imminent risk of death or serious injury)
- Applies to large developers with revenues over $500 million whose models meet certain computational thresholds
- Extends whistleblower protections for employees reporting AI safety concerns
- Makes California the first state to enact a statute specifically targeting frontier AI safety

Approximately five to eight companies fall within SB 53's scope, including OpenAI, Anthropic, Google DeepMind, Meta, and Microsoft. The law represents a more modest approach than SB 1047 — focused on transparency and reporting rather than pre-deployment safety mandates and kill switches — but is consistent with the deployment-context rationale articulated in Newsom's SB 1047 veto.

### Federal Landscape

The SB 1047 debate occurred against the backdrop of federal inaction on frontier AI. Congress did not pass comprehensive AI legislation in 2024. The Biden Administration's October 2023 AI executive order was revoked by President Trump's January 2025 executive order, which instead directed federal agencies to promote AI adoption and instructed the Department of Justice to challenge state AI laws that conflicted with federal AI policy.

## Action Items

- **Developers of frontier AI models** with California nexus should assess applicability of SB 53 (TFAIA), signed September 29, 2025, which imposes transparency reporting and incident notification obligations on large developers (revenue over $500 million) training models above applicable compute thresholds.
- **All developers of generative AI systems** available to California consumers should verify compliance with AB 2013, which required public training data disclosure on websites by January 1, 2026, and applies retroactively to systems made available from January 1, 2022 onward.
- **Legislative monitoring**: Track further AI safety legislation from Senator Wiener and other California legislators. The SB 1047 veto did not end California's ambition to regulate frontier AI — it shifted the approach toward deployment-context risk-tiering.
- **Federal developments**: Monitor federal preemption arguments. The Trump Administration's January 2025 AI executive order and the DOJ AI Litigation Task Force have targeted state AI laws as potential obstacles to federal AI policy. California's AI laws may face constitutional challenges.
- **Open-source developers** should review whether their models approach the compute or revenue thresholds in SB 53 and whether any incident reporting obligations may be triggered.

## Related Reports

- [reports/ai-law/california/california-ab-2013-genai-training-data-transparency-2024.md](reports/ai-law/california/california-ab-2013-genai-training-data-transparency-2024.md) — AB 2013 was signed the day before Newsom vetoed SB 1047; both address California AI developer obligations and the same legislative session.
- [reports/ai-law/state-legislation/new-york-raise-act-frontier-ai-preemption-2026-04-19.md](reports/ai-law/state-legislation/new-york-raise-act-frontier-ai-preemption-2026-04-19.md) — New York's RAISE Act follows the same frontier-model safety framework as SB 1047 and directly references the California experience.
- [reports/ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md](reports/ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md) — The Trump AI executive order and federal preemption framework directly affects the viability of state-level AI safety laws like SB 1047's successors.
- [reports/ai-law/federal-regulation/federal-national-policy-framework-ai-preemption-2026-04-14.md](reports/ai-law/federal-regulation/federal-national-policy-framework-ai-preemption-2026-04-14.md) — Federal preemption analysis relevant to California's AI regulatory authority post-SB 1047.

## Sources

1. [California SB 1047 — Official Bill Status, California Legislative Information](https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202320240SB1047) — Official bill status and legislative history from the California Legislature
2. [California SB 1047 — Official Bill Text, California Legislative Information](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240SB1047) — Full text of the bill as amended
3. [SB 1047 Veto Message — Governor Gavin Newsom (PDF)](https://www.gov.ca.gov/wp-content/uploads/2024/09/SB-1047-Veto-Message.pdf) — Official veto message from the Governor's office, September 29, 2024
4. [Safe and Secure Innovation for Frontier Artificial Intelligence Models Act — Wikipedia](https://en.wikipedia.org/wiki/Safe_and_Secure_Innovation_for_Frontier_Artificial_Intelligence_Models_Act) — Comprehensive overview of the bill including legislative history, stakeholder positions, and key provisions
5. [Regulating the Future: Eight Key Takeaways from California's SB 1047, Vetoed by Governor Newsom — Gibson Dunn](https://www.gibsondunn.com/regulating-the-future-eight-key-takeaways-from-californias-sb-1047-vetoed-by-governor-newsom/) — Detailed legal analysis of SB 1047's provisions and implications
6. [Implications of California Governor Newsom's Veto of AI Safety Bill SB 1047 — Perkins Coie](https://perkinscoie.com/insights/update/implications-california-governor-newsoms-veto-ai-safety-bill-sb-1047) — Analysis of veto rationale and future regulatory direction
7. [California Governor Vetoes AI Safety Bill SB 1047, Signs AB 2013 — Morgan Lewis](https://www.morganlewis.com/pubs/2024/10/california-governor-vetoes-ai-safety-bill-sb-1047-signs-ab-2013-requiring-generative-ai-transparency) — Analysis of the veto and the simultaneously signed AB 2013
8. [Gov. Newsom Vetoes AI Bill but Leaves the Door Open to Future CA Regulation — Crowell & Moring](https://www.crowell.com/en/insights/client-alerts/gov-newsom-vetoes-ai-bill-but-leaves-the-door-open-to-future-ca-regulation) — Law firm client alert analyzing veto implications
9. [California's SB 1047: Understanding the Safe and Secure Innovation for Frontier Artificial Intelligence Act — DLA Piper](https://www.dlapiper.com/en/insights/publications/2024/02/californias-sb-1047) — Early analysis of the bill's scope and developer obligations
10. [California's SB 1047: What You Need to Know — A16Z / Andreessen Horowitz](https://a16z.com/sb-1047-what-you-need-to-know-with-anjney-midha/) — Venture capital perspective on the bill's impact on open-source AI and startups
11. [Gov. Newsom Vetoes California's Controversial AI Bill SB 1047 — TechCrunch](https://techcrunch.com/2024/09/29/gov-newsom-vetoes-californias-controversial-ai-bill-sb-1047/) — News coverage of the veto
12. [Newsom Vetoes Major California Artificial Intelligence Bill — CalMatters](https://calmatters.org/economy/2024/09/california-artificial-intelligence-bill-veto/) — California-focused news coverage including key stakeholder reactions
13. [California Votes: SB 1047 — LegiScan](https://legiscan.com/CA/votes/SB1047/2023) — Official vote counts for the bill
14. [California AB 2013 — Official Bill Text, California Legislative Information](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2013) — Official text of the Generative AI Training Data Transparency Act
15. [California SB 53 — Official Bill Text, California Legislative Information](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB53) — Official text of the Transparency in Frontier Artificial Intelligence Act, SB 53 (2025)
16. [Governor Newsom Signs SB 53 — Governor of California Press Release](https://www.gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/) — Official Governor's office announcement of SB 53 signing
17. [California's SB 53: The First Frontier AI Law, Explained — Future of Privacy Forum](https://fpf.org/blog/californias-sb-53-the-first-frontier-ai-law-explained/) — Policy analysis of SB 53 as successor to SB 1047
18. [California Enacts SB 53 — Mayer Brown](https://www.mayerbrown.com/en/insights/publications/2025/10/california-enacts-sb-53-creating-new-requirements-for-developers-of-frontier-artificial-intelligence-models-and-related-whistleblower-provisions) — Legal analysis of SB 53's compliance requirements
19. [All Eyes on Sacramento: SB 1047 and the AI Safety Debate — Carnegie Endowment for International Peace](https://carnegieendowment.org/posts/2024/09/california-sb1047-ai-safety-regulation?lang=en) — Policy analysis of the broader AI safety debate and SB 1047's significance
