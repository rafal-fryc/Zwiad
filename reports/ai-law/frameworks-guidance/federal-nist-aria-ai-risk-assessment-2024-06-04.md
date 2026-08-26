---
title: "NIST Launches ARIA Program: Voluntary AI Risk and Impact Assessment Testing Opens to Developers Worldwide"
date: 2024-06-04
jurisdiction: "Federal"
category: "ai-law"
development_type: "guidance"
finding_id: "SCAN-20240604-025"
topic_key: "NIST-INVITES-AI-DEVELOPERS-TO-SUBMI-2024"
topic_type: "guidance"
first_reported: 2024-06-04
last_updated: 2024-06-04
status_history: []
cluster: "NIST ARIA Program: AI Risk and Impact Assessment"
cluster_slug: "nist-aria-ai-risk-assessment"
---

# NIST Launches ARIA Program: Voluntary AI Risk and Impact Assessment Testing Opens to Developers Worldwide

**Jurisdiction:** Federal | **Category:** AI Law | **Date:** 2024-06-04

## Executive Summary [HIGH confidence]

In May 2024, the National Institute of Standards and Technology (NIST) officially launched the Assessing Risks and Impacts of AI (ARIA) program, a voluntary initiative that invites AI developers worldwide to submit their large language models for multi-level sociotechnical evaluation. ARIA extends NIST's established AI Risk Management Framework (AI RMF 1.0) into an operational testing environment, applying three evaluation layers — model testing, red-teaming, and field testing — to measure how AI systems perform and affect users in realistic scenarios. The inaugural pilot (ARIA 0.1), which accepted seven AI applications from five organizations, introduces the Contextual Robustness Index (CoRIx) as a novel measurement instrument. While voluntary and non-binding, ARIA has significant long-term compliance implications: NIST frameworks historically migrate into federal procurement requirements and form the foundation of binding state and sector-specific AI rules. AI developers and deployers should monitor ARIA outputs, which will produce publicly available evaluation results and industry-usable guidelines, tools, and metrics.

## Background [HIGH confidence]

NIST has a long history of publishing voluntary frameworks that become mandatory in practice. The [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) (first published 2014) is now woven into federal contractor requirements, FTC expectations, and state cybersecurity laws. The [NIST AI Risk Management Framework 1.0](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf) (AI RMF), released in January 2023 under the [National Artificial Intelligence Initiative Act of 2020 (Pub. L. 116-283)](https://www.congress.gov/bill/116th-congress/house-bill/6216/text), directed NIST to publish a voluntary risk management framework for trustworthy AI. Section 5501 of that statute specifically charged NIST with developing "voluntary, consensus-based, sector-neutral" AI standards in collaboration with the private sector.

President Biden's [Executive Order 14110 on Safe, Secure, and Trustworthy Artificial Intelligence](https://www.federalregister.gov/documents/2023/11/01/2023-24283/safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence) (October 2023) elevated NIST's role substantially, assigning NIST and the newly created U.S. AI Safety Institute (USAISI) responsibility for developing AI safety guidelines, evaluation methodologies, and testing infrastructure. ARIA is a direct downstream product of those EO mandates — it represents NIST operationalizing the AI RMF's "Measure" function through a concrete, replicable testing program.

Prior to ARIA, AI evaluation in the United States was fragmented: model cards, system cards, and pre-deployment testing occurred primarily within developer organizations using proprietary methods. Third-party evaluation was largely limited to academic red-teaming exercises or competitions without standardized measurement instruments. ARIA fills this gap by establishing a government-run, third-party sociotechnical evaluation infrastructure.

In April 2024, NIST's Information Technology Laboratory (ITL) launched ARIA's pilot phase. On May 28, 2024, NIST formally [announced ARIA](https://www.nist.gov/news-events/news/2024/05/nist-launches-aria-new-program-advance-sociotechnical-testing-and), inviting developers globally to submit applications for evaluation in the program's inaugural round.

## Detailed Analysis [HIGH confidence]

### Program Design and Structure

ARIA is structured around a three-tier evaluation model, progressing from technical assessment to real-world field interaction:

1. **Model Testing** — Automated processes using scripted prompt sessions to confirm claimed capabilities. Trained assessors evaluate and annotate AI application outputs against "Test Packets" (TPs), which define permitted and prohibited model behaviors. TPs function analogously to model guardrails, establishing redlines for acceptable outputs at both application and scenario levels. Per the [ARIA Pilot Evaluation Plan](https://ai-challenges.nist.gov/uassets/7), model testing confirms whether systems "perform as advertised."

2. **Red-Teaming** — Adversarial probing to surface vulnerabilities, biases, inaccuracies, and harmful outputs. Between December 2024 and January 2025, 51 red teamers participated in ARIA 0.1, submitting structured adversarial queries across defined evaluation scenarios. Red-teaming stress-tests AI systems beyond normal operating conditions.

3. **Field Testing** — The broadest evaluation layer, pairing human testers with AI applications in scenario-based interactions to measure both application behavior and the positive and negative impacts on users. Field testing examines what NIST describes as "what happens when people interact with AI regularly in realistic settings."

The three evaluation scenarios used in ARIA 0.1 were: **TV Spoilers** (testing AI handling of user preferences and content sensitivity), **Meal Planner** (dietary guidance and contextual personalization), and **Pathfinder** (general assistive navigation). These seemingly mundane domains were deliberately chosen to test AI behavior in representative everyday consumer contexts rather than high-stakes or specialized use cases.

### Measurement: The Contextual Robustness Index (CoRIx)

ARIA introduces a novel measurement framework, the [Contextual Robustness Index (CoRIx)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.700-2.pdf), as its primary evaluation instrument. CoRIx combines data from expert annotators and human testers to produce quantitative scores for how well an AI system "maintains safe functionality within societal contexts." Unlike traditional accuracy-only benchmarks, CoRIx explicitly measures contextual robustness — the ability of a system to behave appropriately across varied user populations and interaction contexts.

The ARIA 0.1 pilot generated 508 total testing sessions across seven submitted applications. [NIST AI 700-2](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.700-2.pdf), the formal technical report for the ARIA pilot, documents the methodology, pilot design, and evaluation instrument in full.

### Submission Requirements

Participation in ARIA is open globally to AI developers. Each submitting organization must provide:
- A **system description** (analogous to a model card or system card), documenting datasets, architecture, design choices, and contextual information about the AI application
- Execution of a **transfer agreement** with NIST governing the handling of submitted software, access credentials, and AI-generated data

The [ARIA program website](https://ai-challenges.nist.gov/aria) specifies eligibility based on application type (large language models in ARIA 0.1) rather than geographic restriction. Evaluation results are published publicly, with the specific level of disclosure pre-negotiated with each submitting organization.

### Relationship to the AI RMF and Broader Standards Architecture

ARIA operationalizes the AI RMF's "Measure" function — the function that recommends quantitative and qualitative techniques for analyzing and monitoring AI risk and impacts. The [CSRC presentation on ARIA](https://csrc.nist.gov/Presentations/2024/assessing-risk-and-impacts-of-ai-aria-program) situates ARIA within NIST's broader trustworthy AI standards architecture. ARIA's outputs — guidelines, tools, methodologies, metrics — are intended to give organizations concrete instruments to self-evaluate their AI systems using the same approaches NIST applies in its own evaluations.

This architecture matters because it signals the direction of future mandatory standards. NIST frameworks, while voluntary at the federal level, become incorporated into sector-specific requirements (e.g., OCC, SEC, HHS guidance), Federal Acquisition Regulation (FAR) clauses for government contractors, and state AI statutes.

### Current Status and Future Development (as of 2025-2026)

The ARIA 0.1 pilot testing period ran from December 2024 through January 2025, with pilot analysis in February–May 2025 and a summary report expected in Summer/Fall 2025. The [NIST technical report NIST.AI.700-2](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.700-2.pdf) documents the pilot methodology and evaluation design in full.

Under the Trump administration's [2025 AI Action Plan](https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf), NIST's Center for AI Standards and Innovation (CAISI) has been directed to evaluate frontier AI systems for national security risks, indicating continued federal investment in AI evaluation infrastructure. However, the Action Plan also directs NIST to revise the AI RMF to remove certain content, and there is ongoing uncertainty about ARIA's future programmatic scope under a prioritization-of-innovation policy stance.

The [U.S. AI Safety Institute](https://www.nist.gov/artificial-intelligence/executive-order-safe-secure-and-trustworthy-artificial-intelligence) remains in an uncertain position — while operating within NIST, proposals for statutory authority have been introduced in Congress but not yet enacted. ARIA's continuation is tied to this institutional stability.

## Impact Assessment [MEDIUM confidence]

### Affected Organizations

ARIA is directly relevant to:

- **AI developers and foundation model providers**: Voluntary participation in ARIA offers early insight into how government evaluators assess AI safety and impact, allowing organizations to benchmark against NIST's emerging evaluation standards before they become mandatory.
- **AI deployers**: Organizations integrating third-party AI systems need to monitor ARIA results, which will be publicly available, as they may become due diligence benchmarks in procurement and regulatory contexts.
- **Federal contractors**: NIST frameworks routinely migrate into FAR requirements. Organizations with federal contracts involving AI should anticipate that ARIA's metrics could appear in procurement clauses.
- **Regulated industries (healthcare, finance, education)**: AI governance regulations in these sectors frequently incorporate or reference NIST frameworks. ARIA's CoRIx methodology may be adopted by sector regulators (e.g., OCC, FDA, SEC) as an evaluation standard.
- **Global AI developers**: ARIA is explicitly open to non-US submitters, making its methodology relevant to multinational technology companies operating in US markets.

### Compliance Considerations

ARIA itself creates no legal obligations. However, several compliance dynamics warrant attention:

- **NIST-as-de-facto-standard**: FTC guidance, state AI legislation, and sector regulators increasingly cite NIST AI RMF compliance as evidence of responsible AI governance. ARIA's outputs will extend this nexus.
- **Procurement implications**: Executive Order 14110 directed federal agencies to use NIST AI evaluation standards in procurement. ARIA's methodologies and CoRIx could become required evaluation instruments for government-procured AI systems.
- **Litigation posture**: Published ARIA results could be used in litigation — plaintiffs challenging AI harms may cite poor ARIA scores as evidence of inadequate pre-deployment testing. Developers with strong ARIA results have a potential defense artifact.
- **Voluntary participation as risk disclosure**: Submitting to ARIA carries the benefit of public credibility but also the risk of publicly disclosed evaluation findings that reveal limitations. Organizations should assess disclosure risk before submitting.

### Enforcement Outlook

ARIA is a measurement and standards development program, not an enforcement action. No regulatory penalties attach to low scores or non-participation. The enforcement implications are indirect: NIST evaluation results, once public, will inform FTC assessments of AI marketing claims, state AG investigations of AI harm, and private litigation under consumer protection statutes.

## Action Items

- Monitor the ARIA program website at [ai-challenges.nist.gov/aria](https://ai-challenges.nist.gov/aria) for announcements of future evaluation rounds (ARIA 0.2 and beyond).
- Review the [NIST AI 700-2 technical report](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.700-2.pdf) to understand CoRIx methodology and how NIST measures contextual robustness — assess whether your AI systems would perform adequately under this evaluation approach.
- AI developers offering LLMs should assess the voluntary participation calculus: early ARIA participation builds credibility and regulatory familiarity before potential mandatory programs arise, but requires review of the transfer agreement and disclosure arrangements.
- Incorporate ARIA's three-tier evaluation model (model testing, red-teaming, field testing) into internal AI governance frameworks, whether or not you participate in the federal program — this structure reflects emerging best practice.
- Track the legislative status of bills proposing statutory authority for the U.S. AI Safety Institute, which would affect ARIA's institutional permanence and scope.
- Assess federal contracting exposure: if your organization supplies AI systems to the federal government, monitor FAR and agency-specific acquisition regulations for ARIA-related evaluation requirements.

## Related Reports

- [reports/ai-law/frameworks-guidance/federal-nist-ai-agent-standards-initiative-2026-04-07.md](reports/ai-law/frameworks-guidance/federal-nist-ai-agent-standards-initiative-2026-04-07.md) — NIST's CAISI AI Agent Standards Initiative extends the same NIST AI RMF lineage that ARIA builds on, targeting AI agent interoperability and security standards.
- [reports/ai-law/frameworks-guidance/nist-ai-rmf-critical-infrastructure-profile-2026-04-13.md](reports/ai-law/frameworks-guidance/nist-ai-rmf-critical-infrastructure-profile-2026-04-13.md) — NIST's critical infrastructure AI RMF profile expands the same evaluation framework that ARIA operationalizes, tailored to high-consequence sectors.
- [reports/ai-law/state-legislation/colorado-benesch-sb205-state-patchwork-2024-06-04.md](reports/ai-law/state-legislation/colorado-benesch-sb205-state-patchwork-2024-06-04.md) — Colorado's SB 24-205 AI Act, signed the same week ARIA launched, exemplifies how NIST-aligned risk evaluation approaches migrate into binding state legislation.

## Sources

1. [NIST Launches ARIA, a New Program to Advance Sociotechnical Testing and Evaluation for AI — NIST.gov](https://www.nist.gov/news-events/news/2024/05/nist-launches-aria-new-program-advance-sociotechnical-testing-and) — Official NIST press release announcing the ARIA program launch, May 2024
2. [ARIA — Assessing Risks and Impacts of AI — NIST AI Challenges](https://ai-challenges.nist.gov/aria) — Official ARIA program portal, submission information, and program documentation
3. [The NIST Assessing Risks and Impacts of AI (ARIA) Pilot Evaluation Plan](https://ai-challenges.nist.gov/uassets/7) — Formal evaluation plan document detailing the three-tier testing structure and test packet methodology
4. [NIST Trustworthy and Responsible AI — NIST AI 700-2](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.700-2.pdf) — Official NIST technical report on ARIA pilot methodology, CoRIx measurement instrument, and evaluation design
5. [NIST Invites AI Developers to Submit Models for Risk Assessment Testing — National Law Review (Mintz)](https://natlawreview.com/article/nist-invites-ai-developers-submit-models-risk-assessment-testing-ai-washington) — Law firm analysis of ARIA implications for AI developers
6. [NIST Invites AI Developers to Submit Models for Risk Assessment Testing — Mintz.com](https://www.mintz.com/insights-center/viewpoints/54731/2024-05-30-nist-invites-ai-developers-submit-models-risk) — Primary law firm source (Mintz) covering AI developer submission requirements and legal context
7. [Assessing Risks and Impacts of AI (ARIA) — CSRC NIST Presentation](https://csrc.nist.gov/Presentations/2024/assessing-risk-and-impacts-of-ai-aria-program) — NIST Computer Security Resource Center presentation situating ARIA within the broader NIST AI standards architecture
8. [National Artificial Intelligence Initiative Act of 2020 — Congress.gov](https://www.congress.gov/bill/116th-congress/house-bill/6216/text) — Statutory authority for NIST AI framework development; Pub. L. 116-283
9. [Executive Order 14110 on Safe, Secure, and Trustworthy AI — Federal Register](https://www.federalregister.gov/documents/2023/11/01/2023-24283/safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence) — Biden EO that directed NIST/USAISI to develop AI evaluation methodologies; backdrop for ARIA
10. [NIST AI Risk Management Framework 1.0 — nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf) — The foundational NIST AI RMF that ARIA operationalizes; January 2023
11. [NIST ARIA Program: Ensuring AI Safety & Evaluation — TestPros](https://testpros.com/artificial-intelligence/nist-aria-program-implications/) — Industry analysis of ARIA's compliance implications for AI developers and procurers
12. [The New Dawn of AI Evaluation: NIST's ARIA — Northwestern University CASMI](https://casmi.northwestern.edu/news/articles/2024/the-new-dawn-of-ai-evaluation-nists-aria.html) — Academic analysis of ARIA's significance for AI evaluation methodology
13. [Understanding AI's Capabilities: NIST Launches ARIA — ANSI](https://www.ansi.org/standards-news/all-news/5-31-24-understanding-ai-capabilities-nist-launches-program-to-advance-sociotechnical-testing) — American National Standards Institute coverage confirming program scope and testing approach
14. [America's AI Action Plan — White House, July 2025](https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf) — Trump administration AI policy framework directing NIST CAISI to evaluate frontier AI systems and potentially revising the AI RMF
