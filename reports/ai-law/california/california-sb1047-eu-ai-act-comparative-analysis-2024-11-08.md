---
title: "California SB 1047 vs. EU AI Act: Comparative Analysis of Cross-Continental AI Regulatory Frameworks"
date: 2024-11-08
jurisdiction: "California"
category: "ai-law"
development_type: "regulation"
finding_id: "SCAN-20241108-002"
topic_key: "california-b0b3d04e-2024"
topic_type: "rulemaking"
topic_key_confidence: "low"
first_reported: 2024-11-08
last_updated: 2024-11-08
status_history: []
cluster: "California SB 1047 vs. EU AI Act: Cross-Continental AI Regulatory Comparison"
cluster_slug: "california-sb1047-eu-ai-act-comparative-analysis"
---

# California SB 1047 vs. EU AI Act: Comparative Analysis of Cross-Continental AI Regulatory Frameworks

**Jurisdiction:** California / EU | **Category:** AI Law | **Date:** November 8, 2024

## Executive Summary [MEDIUM confidence]

Two major AI regulatory frameworks dominated global policy discussions in 2024: California Senate Bill 1047 (SB 1047), the [Safe and Secure Innovation for Frontier Artificial Intelligence Models Act](https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202320240SB1047), and the European Union's [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng), commonly known as the EU AI Act. Though SB 1047 was vetoed by Governor Gavin Newsom on September 29, 2024, its legislative arc — and its comparison with the EU's comprehensive framework — reveals divergent philosophies about how to regulate frontier AI. SB 1047 adopted a model-centric, catastrophic-harm-focused approach targeting developers of the largest foundation models, while the EU AI Act takes a use-case-based, risk-tiered approach covering the entire AI value chain. The [Bird & Bird comparative analysis](https://www.twobirds.com/en/insights/2024/global/californias-ai-bill-vs-the-eu-ai-act-a-cross-continental-analysis-of-ai-regulations) published November 2024 highlights that these differences reflect not only regulatory philosophy but also distinct assumptions about where AI risk actually originates.

## Background [HIGH confidence]

### The California Legislative Context

By early 2024, California hosted the majority of the world's leading AI developers — including OpenAI, Anthropic, Google DeepMind, Meta AI, and xAI — making it the natural focal point for US state-level AI regulation. Senator Scott Wiener (D-San Francisco) introduced SB 1047 as a direct response to the absence of federal legislation, proposing to impose pre-deployment safety obligations on developers of frontier AI models whose training costs exceeded $100 million in computing resources.

SB 1047 passed both chambers of the California legislature with strong margins. On September 29, 2024, Governor Newsom vetoed it, citing the bill's focus on model size rather than real-world deployment context. In his [veto message](https://www.gov.ca.gov/wp-content/uploads/2024/09/SB-1047-Veto-Message.pdf), Newsom stated the bill "regulates models based only on their cost and size" rather than function, arguing it would create a "false sense of security" while stifling innovation. He simultaneously announced a California AI Policy Working Group co-led by AI pioneer Fei-Fei Li to develop evidence-based regulatory recommendations.

### The EU Regulatory Context

The EU AI Act — [Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) — is the world's first comprehensive legal framework for AI. It entered into force on August 1, 2024, following publication in the Official Journal on July 12, 2024. The regulation applies in phased tranches: prohibited AI practices and AI literacy obligations took effect February 2, 2025; governance rules and obligations for general-purpose AI (GPAI) models became applicable August 2, 2025; and full application for high-risk AI systems commences August 2, 2026.

The EU AI Act emerged from a multi-year legislative process initiated by the European Commission's April 2021 proposal and was driven by the EU's goal of harmonizing internal market rules while protecting fundamental rights, democratic institutions, and the rule of law from AI-related harms.

## Detailed Analysis [MEDIUM confidence]

### Philosophical Divergence: Model-Centric vs. Use-Case-Centric Regulation

The most fundamental difference between the two frameworks is their regulatory anchor. SB 1047 used a **model-centric** approach: obligations attached to AI models based on training cost thresholds ($100 million in computing resources), making the underlying model — rather than its deployment context — the regulatory trigger. The EU AI Act uses a **use-case-centric** approach: obligations are determined primarily by how an AI system is deployed and whether it poses risks to health, safety, or fundamental rights in specific high-risk application domains.

As the [Bird & Bird analysis](https://www.twobirds.com/en/insights/2024/global/californias-ai-bill-vs-the-eu-ai-act-a-cross-continental-analysis-of-ai-regulations) explains, this distinction carries major practical implications. Under SB 1047, a $100 million foundation model used only for creative writing would have faced the same obligations as one deployed in critical infrastructure. Under the EU AI Act, those two uses would be treated entirely differently — the latter potentially classified as high-risk, the former as minimal risk.

### Risk Classification Frameworks

**EU AI Act — Four-Tier Risk Pyramid**

The EU AI Act establishes four risk categories for AI systems:

1. **Unacceptable Risk (Prohibited):** Eight categories of AI applications are outright banned, including social scoring systems, subliminal manipulation techniques, real-time biometric surveillance in public spaces (with narrow law enforcement exceptions), and AI used to exploit vulnerabilities of specific groups. These prohibitions applied from February 2, 2025.

2. **High Risk:** Defined in [Article 6](https://artificialintelligenceact.eu/article/6/) and [Annex III](https://artificialintelligenceact.eu/annex/3/), high-risk systems include AI used in biometric identification, critical infrastructure, education, employment, essential services (credit scoring, insurance), law enforcement, border control, and administration of justice. These systems must undergo conformity assessments, be registered in an EU database, implement risk management systems, and maintain robust human oversight.

3. **Limited Risk:** AI systems such as chatbots subject to transparency obligations — users must be informed they are interacting with AI.

4. **Minimal/No Risk:** The vast majority of AI applications fall here. No specific obligations are imposed.

**SB 1047 — Harm-Based Threshold Approach**

SB 1047 defined regulatory obligations based on a "covered model" concept — any AI model trained using computing power costing more than $100 million. Covered model developers would have been required to:
- Implement reasonable safeguards to prevent "critical harms" — defined as harms involving weapons of mass destruction, attacks on critical infrastructure, or autonomous AI-enabled crimes causing mass casualties or $500 million in damage;
- Maintain the ability to shut down or limit the model's capabilities (a "kill switch" obligation);
- Conduct pre-deployment safety testing and annual third-party audits;
- Preserve records and submit compliance documentation to the California Attorney General.

The [Stanford FSI comparative analysis](https://fsi.stanford.edu/publication/californias-sb1047-vs-eu-ai-act-comparative-analysis-ai-regulation) notes that SB 1047's harm taxonomy was narrower and more catastrophic in focus than the EU AI Act — designed to guard against existential or society-altering harms, while the EU Act addresses a broader conception of everyday harms affecting individuals in specific application contexts.

### General-Purpose AI (GPAI) Model Coverage

Both frameworks address foundation models — large pre-trained models capable of being deployed across many use cases — but take different approaches.

The EU AI Act's Title VIII (Articles 51-56) regulates GPAI models, defined as models trained using more than 10²³ floating-point operations (FLOPs) capable of generating text, image, or audio outputs. GPAI obligations include maintaining technical documentation, publishing training data summaries, and complying with EU copyright law. Models presenting **systemic risk** — those exceeding 10²⁵ FLOPs — face additional obligations including notifying the European Commission, conducting adversarial testing, and implementing security protocols. These GPAI obligations became applicable on [August 2, 2025](https://www.steptoe.com/en/news-publications/steptechtoe-blog/eu-ai-act-obligations-for-gpai-models-now-applicable.html).

SB 1047's "covered model" concept was arguably broader than the EU's GPAI systemic-risk tier in some respects (the $100 million compute cost threshold captures a wide range of large models), but narrower in others (it did not address the full range of transparency obligations or supply-chain relationships that the EU GPAI framework imposes on model providers and downstream deployers).

### Scope: Developers vs. Full Value Chain

SB 1047 focused primarily on model **developers** — those who train covered models — and secondarily on those who fine-tune them. It imposed minimal obligations on **deployers** (the businesses or individuals who build applications using covered models). The EU AI Act covers the entire AI value chain: providers (developers), deployers (users in the EU context), importers, and distributors, each with differentiated obligations depending on their role and the risk category of the system.

This scope difference has significant compliance implications for multinational companies. A California company deploying an EU-developed GPAI model in a high-risk application faces both frameworks' requirements from different directions: the EU AI Act's deployer obligations and (had SB 1047 become law) potential developer obligations.

### Kill Switch Requirement

One of SB 1047's most controversial provisions was the requirement that developers maintain a capability to shut down or halt covered models — colloquially called a "kill switch." This had no direct parallel in the EU AI Act, which does require human oversight mechanisms and the ability to correct or discontinue high-risk AI systems, but stops short of mandating a dedicated shutdown capability at the model level.

Governor Newsom cited this provision among his objections, and when Senator Wiener introduced the successor statute — [SB 53 (Transparency in Frontier Artificial Intelligence Act)](https://www.gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/), signed September 29, 2025 — the kill switch requirement was dropped.

### Enforcement Mechanisms

The EU AI Act establishes a multi-tier enforcement architecture. National competent authorities in each EU member state oversee compliance, with the [European AI Office](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) responsible for GPAI model enforcement at the EU level. Fines for noncompliance reach up to:
- €35 million or 7% of worldwide annual turnover for prohibited AI practices;
- €15 million or 3% of turnover for other violations by GPAI providers;
- €7.5 million or 1.5% for providing incorrect information.

SB 1047 would have empowered the California Attorney General to bring civil enforcement actions, with fines up to 10% of a model's compute cost for willful violations and disgorgement of profits. The [Gibson Dunn analysis](https://www.gibsondunn.com/regulating-the-future-eight-key-takeaways-from-californias-sb-1047-vetoed-by-governor-newsom/) noted this represented a novel enforcement mechanism — tying penalty amounts to the model's training cost rather than to revenue or harm magnitude.

## Impact Assessment [MEDIUM confidence]

### For AI Developers Globally

The two frameworks impose distinct compliance burdens on developers. EU AI Act obligations for GPAI models are now in force (since August 2025), requiring providers of large foundation models to maintain technical documentation, publish training data summaries, and comply with copyright requirements. Providers of systemic-risk models face additional notification and adversarial testing requirements.

California, following SB 1047's veto, enacted a narrower framework through SB 53. That law — the [Transparency in Frontier Artificial Intelligence Act](https://fpf.org/blog/californias-sb-53-the-first-frontier-ai-law-explained/) — imposes transparency and adverse incident reporting requirements on frontier AI developers but does not include SB 1047's pre-deployment safety mandates, kill switch requirement, or independent audit obligations.

### Comparative Lessons for US Federal Regulation

The comparative analysis is directly relevant to US federal AI policy debates. The EU Act's risk-tiered, use-case-based approach has informed proposals in Congress, and the Biden Administration's October 2023 executive order on AI safety cited similar principles (though that executive order was revoked by President Trump in January 2025). Under the current Trump administration, the federal posture has shifted toward preempting state AI laws rather than establishing a comprehensive federal framework comparable to the EU AI Act.

### Jurisdictional Arbitrage Risk

The EU AI Act's extraterritorial reach — it applies to providers placing AI systems on the EU market or whose systems affect EU residents — means that US developers building products for EU customers must comply regardless of their home jurisdiction. California's SB 1047 would have created a similar dynamic for California-based developers. The mismatch between these frameworks creates potential for compliance friction and regulatory arbitrage, as companies must navigate rules with different triggers, obligations, and enforcement mechanisms simultaneously.

## Action Items

- Monitor EU AI Act enforcement milestones: GPAI model obligations are now in force (August 2025); full high-risk AI system obligations apply from August 2026.
- Assess whether products qualify as GPAI or high-risk systems under EU criteria; consult [Annex III](https://artificialintelligenceact.eu/annex/3/) of the regulation for the definitive high-risk category list.
- Track California SB 53 implementing regulations — the California Department of Technology is required to issue annual regulatory recommendations beginning in 2026.
- Monitor US federal AI legislation developments; the Trump administration's preemption posture may affect which state AI laws survive legal challenge.
- Organizations operating in both California and the EU should conduct a gap analysis comparing EU AI Act obligations (particularly GPAI provisions) with California's SB 53 transparency requirements.

## Related Reports

- [reports/ai-law/california/california-sb1047-frontier-ai-safety-veto-2024.md](reports/ai-law/california/california-sb1047-frontier-ai-safety-veto-2024.md) -- Comprehensive report on the full legislative arc of SB 1047, including Newsom's veto rationale and the successor SB 53.
- [reports/ai-law/california/california-ab-2013-genai-training-data-transparency-2024.md](reports/ai-law/california/california-ab-2013-genai-training-data-transparency-2024.md) -- Related California AI transparency legislation signed the same day Newsom vetoed SB 1047.
- [reports/ai-law/state-legislation/colorado-sb205-eu-ai-act-comparison.md](reports/ai-law/state-legislation/) -- Colorado's AI Act also drew comparisons to EU framework; see Colorado AI Act state-legislation reports.

## Sources

1. [Regulation (EU) 2024/1689 -- Official Text, EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) -- Official text of the EU AI Act, entered into force August 1, 2024.
2. [California SB 1047 -- Legislative Text, leginfo.legislature.ca.gov](https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202320240SB1047) -- Official California legislative text for the Safe and Secure Innovation for Frontier Artificial Intelligence Models Act.
3. [Governor Newsom SB 1047 Veto Message (PDF)](https://www.gov.ca.gov/wp-content/uploads/2024/09/SB-1047-Veto-Message.pdf) -- Official veto message from Governor Newsom explaining objections to SB 1047.
4. [Bird & Bird: California's AI Bill vs. the EU AI Act: A Cross-Continental Analysis](https://www.twobirds.com/en/insights/2024/global/californias-ai-bill-vs-the-eu-ai-act-a-cross-continental-analysis-of-ai-regulations) -- Primary source for the finding; law firm comparative analysis published November 2024.
5. [Stanford FSI: California's SB1047 vs EU AI Act: A Comparative Analysis](https://fsi.stanford.edu/publication/californias-sb1047-vs-eu-ai-act-comparative-analysis-ai-regulation) -- Stanford Freeman Spogli Institute comparative academic analysis.
6. [EU Artificial Intelligence Act -- High-Level Summary](https://artificialintelligenceact.eu/high-level-summary/) -- Comprehensive annotated summary of EU AI Act provisions.
7. [EU AI Act Article 6: Classification Rules for High-Risk AI Systems](https://artificialintelligenceact.eu/article/6/) -- Official classification criteria for high-risk AI systems.
8. [EU AI Act Annex III: High-Risk AI Systems](https://artificialintelligenceact.eu/annex/3/) -- Complete list of high-risk AI application categories.
9. [Gibson Dunn: Eight Key Takeaways from California's SB 1047](https://www.gibsondunn.com/regulating-the-future-eight-key-takeaways-from-californias-sb-1047-vetoed-by-governor-newsom/) -- Law firm analysis of SB 1047's key provisions and enforcement mechanisms.
10. [Governor Newsom Signs SB 53 -- Official Press Release](https://www.gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/) -- Official announcement of SB 53 (Transparency in Frontier Artificial Intelligence Act), September 29, 2025.
11. [Future of Privacy Forum: California's SB 53 Explained](https://fpf.org/blog/californias-sb-53-the-first-frontier-ai-law-explained/) -- Analysis of SB 53's provisions and relationship to SB 1047.
12. [Steptoe: EU AI Act Obligations for GPAI Models Now Applicable](https://www.steptoe.com/en/news-publications/steptechtoe-blog/eu-ai-act-obligations-for-gpai-models-now-applicable.html) -- Coverage of GPAI obligations entering into force August 2025.
13. [European Commission: Guidelines for GPAI Model Providers](https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers) -- European Commission official guidelines for GPAI providers under the AI Act.
14. [Euronews: How California's AI Legislation Compares to the EU AI Act](https://www.euronews.com/next/2024/09/11/a-big-win-for-the-eu-how-californias-ai-legislation-compares-to-the-eu-ai-act) -- News coverage of SB 1047 / EU AI Act comparison, September 2024.
15. [Perkins Coie: Implications of Newsom's Veto of SB 1047](https://perkinscoie.com/insights/update/implications-california-governor-newsoms-veto-ai-safety-bill-sb-1047) -- Law firm analysis of the regulatory implications of the veto.
