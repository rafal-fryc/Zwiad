---
title: "Financial Services AI Risk Management: Expanded Controls Across OCC, FDIC, Federal Reserve, CFPB, and Treasury"
date: 2026-06-02
jurisdiction: "Federal"
category: "ai-law"
development_type: "guidance"
finding_id: "SCAN-20260615-056"
topic_key: "federal-d1f93d6b-2026"
topic_type: "guidance"
first_reported: 2026-06-02
last_updated: 2026-06-15
status_history: []
cluster: "Federal Financial Services AI Risk Management: SR 26-2, FS AI RMF, and Interagency Guidance (2026)"
cluster_slug: "federal-financial-ai-risk-management-2026"
---

# Financial Services AI Risk Management: Expanded Controls Across OCC, FDIC, Federal Reserve, CFPB, and Treasury

**Jurisdiction:** Federal | **Category:** AI Law | **Date:** June 2, 2026

## Executive Summary [HIGH confidence]

A convergence of regulatory actions in early 2026 has materially expanded AI risk management obligations for US financial institutions. The most significant development is the [joint interagency issuance of revised Model Risk Management guidance (SR 26-2 / OCC Bulletin 2026-13 / FDIC FIL-15-2026)](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm) by the Federal Reserve, OCC, and FDIC on April 17, 2026, replacing the 15-year-old SR 11-7 framework. Separately, the US Treasury in partnership with the Cyber Risk Institute released the [Financial Services AI Risk Management Framework (FS AI RMF)](https://home.treasury.gov/news/press-releases/sb0395) in late February and March 2026 — a voluntary, sector-specific complement to the NIST AI RMF encompassing 230 control objectives. Critically, the revised model risk management guidance explicitly excludes generative AI and agentic AI from scope, creating a well-documented governance gap that regulators say they plan to address through a forthcoming Request for Information (RFI). Financial institutions must now navigate intersecting and partially incomplete guidance from at least five federal regulators while managing rapidly evolving AI deployments in lending, fraud detection, customer service, and AML compliance.

## Background [HIGH confidence]

### Prior Regulatory Foundation

US banking regulators first addressed model risk management in [OCC Bulletin 2011-12 and Federal Reserve SR 11-7](https://www.occ.treas.gov/news-issuances/bulletins/2026/bulletin-2026-13.html), issued jointly in April 2011. That guidance established foundational principles for model development, validation, and governance — disciplines that applied to statistical credit scoring models, stress testing, and similar quantitative tools of the era. A supplemental statement followed in April 2021 (SR 21-8 / FDIC FIL-22-2021) extending model risk discipline to Bank Secrecy Act and AML compliance models.

The 2011 framework predated modern machine learning and has been widely criticized as insufficient for AI systems that operate through opaque neural networks, generate language, or take autonomous actions. For over a decade, regulated institutions applied SR 11-7's principles as best they could to ML models, but with minimal explicit supervisory guidance on how to handle AI-specific characteristics such as hallucination risk, distributional shift, prompt injection, and emergent behavior.

### Treasury's Early 2026 AI Risk Framework Push

In February–March 2026, the US Treasury Department released a suite of six resources developed in coordination with more than 100 financial institutions, the [Financial Services Sector Coordinating Council (FSSCC)](https://home.treasury.gov/news/press-releases/sb0395), and the Cyber Risk Institute. These resources included the FS AI RMF itself and an AI Lexicon designed to standardize terminology across institutions, regulators, and vendors. Treasury's release signaled federal recognition that the financial sector needed sector-specific AI governance guidance beyond the cross-industry NIST AI RMF 1.0 (January 2023).

### Federal Reserve Vice Chair Bowman's May 2026 Remarks

Complementing the formal guidance issuances, Federal Reserve Vice Chair for Supervision Michelle Bowman delivered substantive remarks on AI at the [Financial Stability Oversight Council AI Series Roundtable on Cybersecurity and Risk Management](https://www.federalreserve.gov/newsevents/speech/bowman20260501a.htm) on May 1, 2026. Bowman acknowledged the rapid proliferation of AI in banking and urged a "flexible supervisory response," noting that the same AI tools helping firms defend themselves can also be weaponized against them. She emphasized that supervisory expectations must be scaled to institutional size and complexity, and that the Federal Reserve engages with banks at all levels of the system on AI principles.

## Detailed Analysis [HIGH confidence]

### The Revised Model Risk Management Guidance (SR 26-2)

The joint interagency guidance issued April 17, 2026, supersedes SR 11-7 (2011) and SR 21-8 (2021) in their entirety. [OCC Bulletin 2026-13](https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html) and [FDIC FIL-15-2026](https://www.fdic.gov/news/financial-institution-letters/2026/agencies-revise-interagency-model-risk-management-guidance) are the companion issuances. Key changes include:

**Principles-based, risk-proportionate approach.** The revised guidance reinforces that model risk management should be tailored to each institution's size, complexity, and model risk profile. Practices appropriate for large, complex institutions are not required of smaller or less complex banks. This explicitly addresses longstanding industry criticism that SR 11-7 imposed disproportionate burdens.

**Full model lifecycle coverage.** The guidance details supervisory expectations across the entire model lifecycle — from initial development and data acquisition through implementation, ongoing monitoring, and eventual retirement. This reflects recognition that models deployed years ago may present risks not evident at initial validation.

**"Effective challenge" emphasis.** The guidance reinforces expectations for robust independent validation through a meaningful "effective challenge" process, where qualified validators can credibly question a model's conceptual soundness, ongoing performance, and limitations.

**Explicit exclusion of generative and agentic AI.** The agencies explicitly excluded generative AI and agentic AI models from SR 26-2's scope on the basis that these technologies are "novel and rapidly evolving." The agencies announced a forthcoming RFI that will address model risk management for AI generally, including generative AI and agentic AI, but no timeline was given. This exclusion means banks' most aggressively deployed AI technologies — large language models used in customer service, code generation, and internal operations — currently operate outside the formal model validation framework.

According to [reporting on the governance gap](https://www.techtimes.com/articles/318340/20260613/bank-ai-oversight-expands-every-exam-generative-ai-bypasses-sr-26-2-kill-switch-gap-grows.htm), nearly three in four banks cannot confirm with confidence that they can shut down a malfunctioning AI model or report an AI failure to regulators, even as generative and agentic AI bypass the validation requirements that apply to traditional models.

### The Treasury FS AI RMF

Released by Treasury on [March 1, 2026](https://home.treasury.gov/news/press-releases/sb0395), the Financial Services AI Risk Management Framework (FS AI RMF) translates the voluntary NIST AI RMF into 230 banking-specific control objectives mapped across the AI lifecycle. The framework is organized around NIST's four functions — Govern, Map, Measure, and Manage — and addresses key risk themes including:

- AI lifecycle governance (design, development, deployment, retirement)
- Data quality and provenance controls
- Third-party and vendor AI risk oversight
- Cybersecurity and adversarial threat management (including prompt injection and model extraction)
- Human oversight of automated systems
- Fairness, bias, and explainability controls aligned with fair lending obligations

The FS AI RMF is voluntary and does not create new legal obligations. However, [law firm analyses](https://www.mondaq.com/unitedstates/fintech/1751798/financial-services-ai-risk-management-framework-operationalizing-the-230-control-objectives-before-the-market-wakes-up) note that these materials are likely to become a reference standard in examinations, internal audit programs, third-party oversight protocols, and contract negotiations with AI vendors. Regulators are already referencing the framework in examination contexts.

### CFPB: Consumer Protection and Fair Lending in AI Contexts

The CFPB has not issued comprehensive AI-specific rules but has accumulated a body of guidance and enforcement signals relevant to AI-driven consumer finance:

**Chatbot guidance.** The CFPB issued a report on AI chatbot use in consumer finance, identifying risks including inaccurate information, failure to recognize consumer invocations of rights under Regulation E and Regulation Z, and privacy and data security concerns. The Bureau stated it would actively police chatbot deployments that fail to provide accurate, helpful information or that deny consumers access to human representatives.

**Adverse action on AI credit denials.** The CFPB previously issued guidance clarifying that lenders using AI or algorithmic models to make credit decisions must provide specific, accurate reasons for adverse actions — they cannot use generic adverse action codes if those codes do not reflect the actual model output. [This guidance](https://uk.practicallaw.thomsonreuters.com/w-040-8758) remains operative and continues to create compliance challenges for institutions using black-box AI in underwriting.

**Fair lending recalibration.** On April 22, 2026, the CFPB issued a [final rule amending Regulation B](https://www.consumerfinancemonitor.com/2026/05/04/cfpbs-final-rule-recalibrates-fair-lending-enforcement-a-return-to-clarity-and-core-statutory-principles/) to remove disparate-impact provisions, limiting ECOA enforcement to intentional discrimination. Disparate-treatment theories, including proxy-based discrimination claims, remain intact. This rule affects AI lending models by narrowing the theory of liability — but does not eliminate fair lending risk for AI systems that operate through correlations with protected characteristics.

### Third-Party / Vendor Risk Management

The three banking agencies (OCC, Federal Reserve, FDIC) issued interagency guidance on third-party risk management in 2023, which applies broadly to AI vendors and technology providers. The FS AI RMF explicitly extends its 230 control objectives to AI risks introduced by vendors, partners, and affiliates. Financial institutions that rely on third-party AI models for lending decisions, fraud detection, or AML compliance are expected to apply due diligence, ongoing monitoring, and contractual protections equivalent to what they would apply to internally developed models.

### FINRA: Broker-Dealer AI Governance

The [Financial Industry Regulatory Authority's 2026 Annual Regulatory Oversight Report](https://www.finra.org/media-center/newsreleases/2025/finra-publishes-2026-regulatory-oversight-report-empower-member-firm) dedicates a standalone section to generative AI for the first time — a clear signal that examiners will scrutinize AI governance in 2026 broker-dealer examinations. FINRA expects firms to:

- Assess regulatory compliance obligations before deploying generative AI
- Establish written policies and procedures governing AI use
- Ensure AI-generated communications with customers meet suitability and supervision standards
- Maintain human oversight of AI agents acting autonomously

FINRA identified AI agents acting autonomously without "human in the loop" controls as an emerging risk of greatest concern.

## Impact Assessment [MEDIUM confidence]

### Who Is Affected

- **Large banking organizations** (>$30 billion in assets) regulated by the Federal Reserve face the most direct SR 26-2 applicability, but the guidance is principles-based and regulators will apply it proportionately.
- **OCC-chartered banks and federal savings associations** are governed by OCC Bulletin 2026-13.
- **FDIC-supervised state nonmember banks** are governed by FDIC FIL-15-2026.
- **CFPB-supervised lenders** (banks and nonbanks in consumer credit) face ongoing adverse action and fair lending requirements from CFPB guidance on AI.
- **Broker-dealers** regulated by FINRA face new AI governance examination expectations.
- **All financial institutions using third-party AI vendors** must apply third-party risk management disciplines to those vendors under existing interagency guidance.

### The Generative AI Governance Gap

The most significant near-term compliance challenge for financial institutions is the explicit exclusion of generative and agentic AI from SR 26-2. This creates a regulatory gray zone:

- Traditional quantitative models (credit scorecards, stress testing models, fraud detection ML models) are covered by SR 26-2 and must be developed, validated, and monitored under the revised framework.
- Generative AI tools (LLM-powered chatbots, code assistants, document summarization, autonomous agents) are excluded from SR 26-2 but remain subject to general safety and soundness expectations, existing consumer protection laws, and the CFPB's chatbot guidance.
- The forthcoming RFI on generative and agentic AI model risk may eventually create binding expectations, but institutions that have already deployed these tools with minimal governance frameworks will face remediation challenges.

### Compliance Timeline and Deadlines

The revised interagency guidance (SR 26-2 / OCC Bulletin 2026-13 / FDIC FIL-15-2026) became effective on [April 17, 2026](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm), the date of issuance. The guidance is not transitional — it does not include a formal implementation deadline. Examiners are expected to begin applying it during routine examinations, though enforcement of new expectations typically involves supervisory discussions before formal actions.

The FS AI RMF carries no compliance deadline because it is voluntary. However, institutions that benchmark their AI governance programs against the FS AI RMF will be better positioned in examinations as regulators increasingly reference it.

The CFPB's Regulation B amendment removing disparate impact takes effect July 21, 2026.

### Consequences of Non-Compliance

Failure to maintain adequate model risk management practices can result in:

- Supervisory criticisms and matters requiring attention (MRAs) during examination
- Formal enforcement actions including consent orders and civil money penalties
- Consumer protection violations under CFPB authority (adverse action deficiencies, chatbot-related UDAAP violations)
- Fair lending liability for AI lending models producing discriminatory outcomes

## Action Items

- **Assess existing model inventory against SR 26-2.** Categorize all models by type, complexity, and materiality; confirm which models fall under the revised guidance and which (generative/agentic AI) currently fall outside scope.
- **Develop interim governance for generative and agentic AI.** Do not wait for the forthcoming RFI. Establish policies, risk assessments, and human-oversight controls for LLM-based tools deployed now, using the FS AI RMF's 230 control objectives as a voluntary benchmark.
- **Audit adverse action notification processes.** Confirm that AI-driven credit decisions are producing specific, model-grounded adverse action reasons consistent with CFPB guidance — not generic codes.
- **Map third-party AI vendors to existing third-party risk management programs.** Apply due diligence, contract protections, and ongoing monitoring to AI technology vendors as required under 2023 interagency third-party guidance.
- **Align FINRA compliance programs.** Broker-dealers should update written supervisory procedures to address generative AI use in customer communications and internal operations before 2026 examinations.
- **Monitor the forthcoming RFI on generative and agentic AI.** Comment deadlines, once published, will be the primary opportunity to shape how banking regulators extend model risk management to excluded AI technologies.
- **Review fair lending model risk in light of CFPB Regulation B amendment.** While disparate impact liability has been narrowed, proxy-based disparate-treatment theories remain — audit AI lending models for correlations with protected characteristics that could support intentional discrimination claims.

## Related Reports

- [Federal NIST AI RMF Critical Infrastructure Profile (April 2026)](../frameworks-guidance/nist-ai-rmf-critical-infrastructure-profile-2026-04-13.md) — The NIST AI RMF is the upstream framework the Treasury FS AI RMF is built upon; financial institutions governing AI risk under the FS AI RMF should understand the broader NIST framework from which it derives.
- [New York DFS AI Cybersecurity Guidance](../frameworks-guidance/new-york-dfs-ai-cybersecurity-guidance-2024-10-16.md) — NYDFS-regulated financial entities face an additional layer of AI-specific cybersecurity obligations under 23 NYCRR 500 alongside the federal model risk management guidance.
- [Federal CFTC TAC AI Report (May 2024)](../frameworks-guidance/federal-cftc-tac-ai-report-2024-05-02.md) — The CFTC's Technology Advisory Committee addressed AI risk in derivatives markets; relevant to financial institutions with commodity or derivatives exposures.
- [FTC Staff Blog on AI Risk Factors](../frameworks-guidance/federal-ftc-ai-risk-consumer-harm-blog-2025-01.md) — FTC consumer harm framework for AI overlaps with CFPB's approach to chatbot and AI lending risks in consumer finance.

## Sources

1. [Federal Reserve SR 26-2: Revised Guidance on Model Risk Management (April 17, 2026)](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm) — Primary source; full text of the revised interagency model risk management guidance and Federal Reserve supervisory letter.
2. [OCC Bulletin 2026-13: Model Risk Management Revised Guidance](https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html) — OCC companion issuance to SR 26-2; applies to OCC-chartered banks and federal savings associations.
3. [FDIC FIL-15-2026: Agencies Revise Interagency Model Risk Management Guidance](https://www.fdic.gov/news/financial-institution-letters/2026/agencies-revise-interagency-model-risk-management-guidance) — FDIC companion issuance; applies to FDIC-supervised state nonmember banks.
4. [US Treasury FS AI RMF Press Release (March 1, 2026)](https://home.treasury.gov/news/press-releases/sb0395) — Official Treasury announcement of the Financial Services AI Risk Management Framework and associated resources.
5. [Taft Stettinius & Hollister: Financial Services AI Risk Management Framework — Expanded Controls](https://www.tafttechlaw.com/2026/05/financial-services-ai-risk-management-framework-expanded-controls-for-the-financial-services-industry/) — Law firm analysis synthesizing the FS AI RMF and intersecting regulatory guidance; the primary source identified in the finding.
6. [Federal Reserve Vice Chair Bowman: AI in the Financial System (May 1, 2026)](https://www.federalreserve.gov/newsevents/speech/bowman20260501a.htm) — Federal Reserve supervisory policy speech on AI risk management and the need for flexible oversight.
7. [Sullivan & Cromwell: Federal Banking Agencies Issue Revised Guidance on Model Risk Management](https://www.sullcrom.com/insights/memo/2026/April/OCC-Fed-FDIC-Issue-Revised-Guidance-Model-Risk-Management) — Law firm client alert analyzing SR 26-2, OCC Bulletin 2026-13, and FDIC FIL-15-2026.
8. [Mondaq / Lowenstein Sandler: Operationalizing the 230 Control Objectives Before the Market Wakes Up](https://www.mondaq.com/unitedstates/fintech/1751798/financial-services-ai-risk-management-framework-operationalizing-the-230-control-objectives-before-the-market-wakes-up) — Law firm analysis of the FS AI RMF's 230 control objectives and their practical compliance implications.
9. [Consumer Finance Monitor: CFPB Final Rule Recalibrates Fair Lending Enforcement (April 22, 2026)](https://www.consumerfinancemonitor.com/2026/05/04/cfpbs-final-rule-recalibrates-fair-lending-enforcement-a-return-to-clarity-and-core-statutory-principles/) — Analysis of CFPB's Regulation B amendment removing disparate-impact provisions; effective July 21, 2026.
10. [Practical Law / Thomson Reuters: CFPB Guidance on Adverse Action Notifications and AI](https://uk.practicallaw.thomsonreuters.com/w-040-8758) — Summary of CFPB guidance on adverse action notification requirements for AI-driven credit decisions.
11. [FINRA: 2026 Annual Regulatory Oversight Report](https://www.finra.org/media-center/newsreleases/2025/finra-publishes-2026-regulatory-oversight-report-empower-member-firm) — Official FINRA report establishing AI governance examination priorities for 2026 broker-dealer exams.
12. [TechTimes: Bank AI Oversight Expands to Every Exam — Generative AI Bypasses SR 26-2 as Kill-Switch Gap Grows (June 13, 2026)](https://www.techtimes.com/articles/318340/20260613/bank-ai-oversight-expands-every-exam-generative-ai-bypasses-sr-26-2-kill-switch-gap-grows.htm) — Reporting on the governance gap created by SR 26-2's exclusion of generative and agentic AI.
13. [GAO-25-107197: Artificial Intelligence — Use and Oversight in Financial Services](https://files.gao.gov/reports/GAO-25-107197/index.html) — GAO report providing context on AI use across the financial sector and existing regulatory oversight frameworks.
