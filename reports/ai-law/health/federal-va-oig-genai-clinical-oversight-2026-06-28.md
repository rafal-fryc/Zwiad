---
title: "VA OIG: Clinicians Using Generative AI Chat Tools in Clinical Settings Without Required Oversight"
date: 2026-06-28
jurisdiction: "Federal"
category: "ai-law"
development_type: "guidance"
finding_id: "SCAN-20260628-015"
topic_key: "federal-f882c94e-2026"
topic_type: "guidance"
first_reported: 2026-06-15
last_updated: 2026-06-28
status_history: []
cluster: "Federal AI Procurement and Governance: OMB M-25-21, M-25-22, and M-26-04"
cluster_slug: "federal-ai-procurement-omb-memoranda"
---

# VA OIG: Clinicians Using Generative AI Chat Tools in Clinical Settings Without Required Oversight

**Jurisdiction:** Federal | **Category:** AI Law | **Date:** June 2026

## Executive Summary [HIGH confidence]

The Department of Veterans Affairs Office of Inspector General (VA OIG) released a national healthcare review — Report 26-00182-140 — in June 2026, finding that Veterans Health Administration (VHA) clinicians are using two general-purpose generative AI chat tools, [VA GPT and Microsoft 365 Copilot Chat](https://www.vaoig.gov/reports/national-healthcare-review/review-generative-artificial-intelligence-chat-tools-clinical), for clinical care and documentation without adequate governance, risk management, or patient safety oversight. An analysis of 135 prompts shared by VA staff found 79 were clinical in nature — including drafting clinical notes and patient care summarization — yet neither tool had been designated a "high-impact" AI system, a classification that would have triggered mandatory federal safeguards under [OMB Memorandum M-25-21](https://digitalgovernmenthub.org/examples/omb-m-25-21-accelerating-federal-use-of-ai-through-innovation-governance-and-public-trust/). The OIG issued three recommendations to the Under Secretary for Health requiring formal governance policies, high-impact AI designation evaluation, and integration of AI risk monitoring into existing patient safety programs. The VA concurred with all three recommendations and provided initial action plans.

## Background [HIGH confidence]

### Veterans Health Administration AI Adoption

The VHA is the largest integrated healthcare system in the United States, serving over 9 million enrolled veterans across more than 1,200 care sites. As generative AI tools rapidly entered the commercial market, VA employees — including clinical staff — began using enterprise-licensed AI chat tools for daily work. By late 2025, [more than 15,000 VA staff members](https://www.hipaajournal.com/va-oig-lack-oversight-va-genai-chat-tools/) were using general-purpose generative AI chat tools, with clinical uses including drafting medical record notes and summarizing patient care.

The VA authorized two general-purpose chat tools for use with patient health information: [VA GPT](https://www.hipaajournal.com/va-oig-lack-oversight-va-genai-chat-tools/), an internally developed chat tool, and Microsoft 365 Copilot Chat, deployed through VA's enterprise Microsoft licensing. Neither tool was designed specifically for clinical use; both are general-purpose large language model interfaces that VA employees adapted for clinical tasks on their own initiative.

Separately, VHA piloted a purpose-built clinical tool, [Ambient AI Scribe](https://www.soapnoteai.com/soap-note-guides-and-example/va-ai-scribe-2026/), which listens to clinical encounters and drafts medical record notes. Unlike the general-purpose chat tools, Ambient AI Scribe was correctly designated as "high-impact" — triggering required pre-deployment testing, ongoing performance monitoring, and mandatory human review before notes entered the medical record. The OIG's report treats the Ambient AI Scribe governance structure as the standard the general-purpose tools failed to meet.

### Federal AI Governance Framework

Federal AI oversight for executive branch agencies is governed primarily by [OMB Memorandum M-25-21](https://digitalgovernmenthub.org/examples/omb-m-25-21-accelerating-federal-use-of-ai-through-innovation-governance-and-public-trust/) (April 3, 2025), "Accelerating Federal Use of AI through Innovation, Governance, and Public Trust," issued under Executive Order 14179. M-25-21 requires agencies to:

- Designate a Chief AI Officer (CAIO) and maintain a public AI use-case inventory
- Classify AI systems with significant consequences for rights, safety, or mission outcomes as "high-impact"
- Apply minimum risk management practices to high-impact AI, including pre-deployment testing and continuous monitoring
- Coordinate AI governance across internal agency bodies

For the VA specifically, AI governance was formally divided between the VHA's [National Artificial Intelligence Institute (NAII)](https://department.va.gov/ai/chief-ai-officer/) and the Office of Information and Technology's Chief AI Officer team. The OIG found that as of the review period, these two bodies were coordinating AI efforts without a formalized governance relationship, and critically, neither had engaged VHA's National Center for Patient Safety when AI tools were authorized for clinical use.

### Preliminary Advisory Memorandum (January 2026)

The OIG had already signaled these concerns earlier in the review. On January 15, 2026, the OIG published a [Preliminary Result Advisory Memorandum (Report 26-00182-42)](https://www.vaoig.gov/reports/preliminary-result-advisory-memorandum/review-vhas-use-generative-artificial-intelligence) identifying VHA's lack of a formal mechanism to identify, track, or resolve risks from generative AI as a potential patient safety risk. The preliminary memo prompted limited initial actions from VA, including adding a National Center for Patient Safety representative to the VHA AI Assessment Subcommittee. The June 2026 final report reflects the outcome of the full review conducted October 2025 through February 2026.

## Detailed Analysis [HIGH confidence]

### Findings: Governance Gaps

The OIG's central finding is that VA AI leadership failed to coordinate with VHA's National Center for Patient Safety when authorizing generative AI chat tools for clinical use. This failure had cascading consequences:

**No high-impact designation.** Despite clinical use of VA GPT and Copilot Chat at scale — including for drafting clinical notes that become part of official medical records — VA AI leaders did not classify either tool as "high-impact" under M-25-21. [During interviews, VA leaders characterized the tools as analogous to search engines](https://www.nextgov.com/artificial-intelligence/2026/06/vas-ai-chatbots-not-designated-high-impact-despite-clinical-use-watchdog-says/414158/) and emphasized user-level responsibility for outputs, a framing the OIG rejected as inadequate given the clinical stakes.

**No formal risk-reporting mechanism.** [VHA did not have a formal mechanism to identify, track, or resolve risks associated with generative AI](https://www.fedagent.com/news/va-watchdog-flags-patient-safety-risks-from-ai-use-in-veterans-health-care/). When AI tools produced inaccurate or incomplete outputs — including omissions that could affect diagnoses or treatment decisions — there was no structured channel for clinicians to report these errors, no systematic tracking, and no integration with existing patient safety reporting systems.

**No AI-specific safety reporting.** Unlike medication errors or surgical complications, which have established reporting protocols under VHA patient safety programs, AI-related clinical errors had no defined reporting category. The OIG found [limited coordination between the CAIO/NAII and the National Center for Patient Safety](https://www.techtarget.com/healthtechanalytics/news/366644951/OIG-found-limited-coordination-oversight-of-VAs-genAI-tools/), meaning AI-related adverse events would not reliably surface through existing safety infrastructure.

**Known technical limitations unmitigated.** Both VA GPT and Copilot Chat lack real-time web access, meaning their knowledge bases are not current. [Generative AI systems can produce inaccurate or incomplete outputs](https://www.govinfosecurity.com/va-health-ai-chat-tools-lack-oversight-agency-warns-a-31958), including "hallucinations" — fabricated facts stated with apparent confidence — that, when incorporated into clinical notes, could affect diagnoses, treatment plans, or medication decisions without the clinician or patient being aware.

### Findings: Scope of Clinical Use

Of 135 prompts shared with the OIG by VA staff:
- [56 prompts were for drafting clinical notes](https://www.hipaajournal.com/va-oig-lack-oversight-va-genai-chat-tools/)
- 17 prompts were for patient care summarization
- 6 prompts were for other clinical purposes
- The remaining 56 prompts were non-clinical

This distribution — with over 58% of reviewed prompts being clinical in nature — directly contradicts the framing of the tools as search-engine analogues. Clinical note drafting in particular carries elevated risk: notes drafted by AI that are reviewed but not critically edited by a clinician may perpetuate errors into the permanent medical record.

### The Ambient AI Scribe Contrast

The OIG's analysis uses Ambient AI Scribe as an implicit standard of care. That tool, a purpose-built clinical AI, was correctly classified as high-impact and subjected to: pre-deployment testing, ongoing performance monitoring, feedback loops for error detection, and mandatory human review before notes entered the medical record. The OIG's second recommendation asks whether the safeguards applied to Ambient AI Scribe should be adapted for the general-purpose chat tools — implicitly arguing they should.

### OIG Recommendations

The OIG issued three recommendations to the Under Secretary for Health:

1. **Define permissible clinical uses and governance.** The Under Secretary for Health should review VHA's current use of generative AI chat tools, define permissible clinical uses for general-purpose AI chat tools, clarify oversight responsibilities and risk mitigation requirements, and outline an implementation plan.

2. **Evaluate high-impact designation.** The Under Secretary for Health should evaluate whether safeguards applied to high-impact AI tools like Ambient AI Scribe should be adapted for VA GPT and Copilot Chat when used for clinical care and documentation.

3. **Integrate AI risk into patient safety programs.** The Under Secretary for Health should oversee integration of AI-related risk monitoring into existing patient safety programs and ensure staff are trained to identify and report AI-related safety events.

### VA Response

The VA [concurred with all three recommendations](https://www.vaoig.gov/reports/national-healthcare-review/review-generative-artificial-intelligence-chat-tools-clinical) and provided action plans. Initial steps included increased communication between AI governance bodies and health agencies and reporting systems. The VA committed to developing clinical AI governance policies and corresponding quality assurance processes — though as of the report's publication, no concrete deadline for full implementation was specified. The VHA concurred "in principle" with Recommendation 1 and concurred fully with Recommendations 2 and 3.

## Impact Assessment [MEDIUM confidence]

### Veterans and Patient Safety

The most direct impact of the governance gap is on the 9 million enrolled veterans receiving VHA care. Clinical notes drafted by AI that contain errors — omissions, hallucinations, outdated information — can affect diagnoses, medications, referrals, and insurance determinations. Because neither VA GPT nor Copilot Chat has real-time knowledge access, clinical notes drafted using these tools may rely on outdated clinical guidance.

The risk is compounded by the scale of adoption: with [over 15,000 staff using these tools](https://www.hipaajournal.com/va-oig-lack-oversight-va-genai-chat-tools/), even a small error rate could translate to a significant number of affected patients. The absence of AI-specific error reporting means baseline error rates are unknown.

### Federal AI Governance Implications

This report is significant beyond the VA context. It is among the first OIG reviews to assess whether a major federal agency's AI governance practices comply with M-25-21's "high-impact" designation requirements in a clinical setting. The finding that VA leaders characterized general-purpose AI chat tools as search engines — thereby sidestepping high-impact classification — is a pattern likely replicated across other federal agencies using enterprise Microsoft 365 Copilot licenses.

The OIG's analysis provides a roadmap for how oversight bodies should evaluate M-25-21 compliance: assess actual use patterns (not just authorized use cases), examine whether clinical or safety-adjacent uses trigger high-impact obligations, and test whether AI governance bodies coordinate with safety programs.

### Healthcare Organizations Beyond the VA

While the VA OIG's jurisdiction is limited to the Department of Veterans Affairs, the report's findings reflect governance challenges common to all large healthcare systems deploying general-purpose AI tools. Private health systems, academic medical centers, and community hospitals face the same pattern: enterprise AI licenses (Microsoft Copilot, Google Workspace AI, etc.) adopted at scale, with clinical use following organically and governance lagging behind. Compliance officers and health system legal teams should treat this report as a governance benchmark.

### Regulatory and Privacy Dimensions

VHA is subject to the Privacy Act of 1974 and VA-specific privacy regulations, which require Privacy Impact Assessments (PIAs) for systems that collect or process personally identifiable information. The OIG report does not directly address whether PIAs were completed for the AI chat tools' clinical uses, but [VA regulations require PIAs for new or substantially changed IT systems](https://department.va.gov/privacy/privacy-program-plan/) — a category that plausibly includes authorizing a general-purpose tool for clinical PHI processing. This is a potential compliance gap the report does not fully resolve.

## Action Items

- **Healthcare organizations using enterprise AI tools**: Audit current clinical use of general-purpose AI chat tools (Microsoft Copilot, Google AI, etc.) against your jurisdiction's AI governance requirements; where clinical use is occurring without governance oversight, classify the activity and apply appropriate safeguards before expanding access.
- **Federal agencies subject to M-25-21**: Reassess AI use-case inventories to capture de facto clinical or safety-adjacent uses of general-purpose AI tools, not just intended uses; evaluate whether any such uses warrant high-impact designation regardless of the tool's original classification.
- **VHA compliance staff**: Monitor VA's implementation of the three OIG recommendations; the VA's "in principle" concurrence with Recommendation 1 leaves room for a narrower response than the OIG intended, and the absence of specific implementation deadlines warrants follow-up.
- **Health system legal and compliance teams**: Cross-reference this OIG report against your organization's AI governance policies, privacy impact assessment processes, and patient safety reporting protocols; update AI-related incident reporting categories to capture AI-related adverse events specifically.
- **Monitor**: Watch for VA's publication of formal clinical AI use policies and its M-25-21 compliance report to OMB (due September 22, 2026, for high-impact AI practices) as indicators of follow-through on OIG recommendations.

## Related Reports

- [reports/ai-law/health/state-ai-health-insurance-prior-auth-bills-2026-04-23.md](reports/ai-law/health/state-ai-health-insurance-prior-auth-bills-2026-04-23.md) — Covers parallel AI governance issues in health insurance prior authorization at the state level, reflecting a broader pattern of AI adoption in healthcare outpacing regulatory frameworks.
- [reports/ai-law/enforcement-actions/federal-fda-ai-overreliance-cgmp-warning-2026-04-02.md](reports/ai-law/enforcement-actions/federal-fda-ai-overreliance-cgmp-warning-2026-04-02.md) — FDA's warning letter citing AI overreliance in pharmaceutical manufacturing reflects a similar pattern of AI deployment in regulated health contexts without adequate safeguards.
- [reports/ai-law/frameworks-guidance/federal-wh-ostp-ai-safety-procurement-2026-05-18.md](reports/ai-law/frameworks-guidance/federal-wh-ostp-ai-safety-procurement-2026-05-18.md) — Covers the M-25-21 and related federal AI procurement and safety framework that the VA OIG applied in assessing VA's governance failures.
- [reports/ai-law/frameworks-guidance/nist-ai-rmf-critical-infrastructure-profile-2026-04-13.md](reports/ai-law/frameworks-guidance/nist-ai-rmf-critical-infrastructure-profile-2026-04-13.md) — NIST AI Risk Management Framework critical infrastructure profile provides the risk management standards referenced in both M-25-21 and the OIG's governance gap analysis.

## Sources

1. [Review of Generative Artificial Intelligence Chat Tools for Clinical Use — VA OIG (Report 26-00182-140)](https://www.vaoig.gov/reports/national-healthcare-review/review-generative-artificial-intelligence-chat-tools-clinical) — Official OIG report page; primary source for findings, recommendations, and VA response.
2. [VA OIG Report 26-00182-140 Full PDF](https://www.vaoig.gov/sites/default/files/reports/2026-06/vaoig-26-00182-140_-_final.pdf) — Full text of the June 2026 final report.
3. [Review of VHA's Use of Generative AI — Preliminary Advisory Memorandum (January 2026)](https://www.vaoig.gov/reports/preliminary-result-advisory-memorandum/review-vhas-use-generative-artificial-intelligence) — OIG preliminary advisory memo (Report 26-00182-42) published January 15, 2026.
4. [VA Clinical Staff Rushed to Use Generative AI Without Oversight — FedScoop](https://fedscoop.com/va-ai-use-clinical-staff-watchdog-report/) — Detailed news coverage of the final report's findings and context.
5. [VA's AI Chatbots Not Designated High-Impact, Despite Clinical Use — Nextgov/FCW](https://www.nextgov.com/artificial-intelligence/2026/06/vas-ai-chatbots-not-designated-high-impact-despite-clinical-use-watchdog-says/414158/) — Analysis of the high-impact designation failure and M-25-21 implications.
6. [OIG Found Limited Coordination, Oversight of VA's GenAI Tools — TechTarget Health Tech Analytics](https://www.techtarget.com/healthtechanalytics/news/366644951/OIG-found-limited-coordination-oversight-of-VAs-genAI-tools) — Technical analysis of governance coordination failures between CAIO/NAII and National Center for Patient Safety.
7. [VA OIG Identifies Lack of Oversight of VA GenAI Chat Tools — HIPAA Journal](https://www.hipaajournal.com/va-oig-lack-oversight-va-genai-chat-tools/) — Summary of findings with patient safety focus, including prompt analysis statistics.
8. [VA OIG Expresses Concerns About Clinical Use of AI, Patient Safety — U.S. Medicine](https://www.usmedicine.com/non-clinical-topics/technology/va-oig-expresses-concerns-about-clinical-use-of-artificial-intelligence-patient-safety/) — Clinical practitioner-focused coverage.
9. [VA Watchdog Flags Patient Safety Risks from AI Use in Veterans Health Care — FEDagent](https://www.fedagent.com/news/va-watchdog-flags-patient-safety-risks-from-ai-use-in-veterans-health-care) — Additional coverage with focus on patient safety risk framing.
10. [VA Health AI Chat Tools Lack Oversight — GovInfoSecurity](https://www.govinfosecurity.com/va-health-ai-chat-tools-lack-oversight-agency-warns-a-31958) — Cybersecurity and information security perspective on the governance failures.
11. [VHA Lacks 'Formal Mechanism' for Mitigating Clinical AI Chatbot Risks — Nextgov/FCW (January 2026)](https://www.nextgov.com/artificial-intelligence/2026/01/vha-lacks-formal-mechanism-mitigating-clinical-ai-chatbot-risks-watchdog-says/410734/) — Coverage of the preliminary advisory memo and initial VA response.
12. [OMB Memorandum M-25-21: Accelerating Federal Use of AI Through Innovation, Governance, and Public Trust](https://digitalgovernmenthub.org/examples/omb-m-25-21-accelerating-federal-use-of-ai-through-innovation-governance-and-public-trust/) — The federal AI governance framework under which the VA OIG assessed VA's compliance.
13. [VA Artificial Intelligence — Guidance for Generative AI Use at VA](https://department.va.gov/ai/guidance-for-generative-ai-use-at-va/) — VA's internal AI guidance page (internal access), referenced in OIG as background.
14. [VA Chief AI Officer](https://department.va.gov/ai/chief-ai-officer/) — VA's CAIO office structure and hub-and-spoke governance model description.
15. [VA AI Scribe 2026: Nationwide Expansion — SOAP Note AI](https://www.soapnoteai.com/soap-note-guides-and-example/va-ai-scribe-2026/) — Background on Ambient AI Scribe program and its governance safeguards as the high-impact benchmark.
16. [VA Privacy Program Plan](https://department.va.gov/privacy/privacy-program-plan/) — VA privacy impact assessment requirements and Privacy Act obligations relevant to clinical AI deployment.
