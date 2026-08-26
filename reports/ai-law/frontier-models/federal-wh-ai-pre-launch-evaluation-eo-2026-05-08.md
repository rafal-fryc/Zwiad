---
title: "White House Weighs Executive Order on Pre-Launch AI Model Evaluation Following Claude Mythos Developments"
date: 2026-05-08
jurisdiction: "Federal"
category: "ai-law"
development_type: "guidance"
finding_id: "SCAN-20260508-022"
topic_key: "WH-CONSIDERING-PRE-LAUNCH-AI-MODE-2026"
topic_type: "guidance"
first_reported: 2026-05-08
last_updated: 2026-05-08
status_history: []
cluster: "Anthropic Claude Mythos: AI-Driven Vulnerability Research"
cluster_slug: "anthropic-claude-mythos-cybersecurity"
---

# White House Weighs Executive Order on Pre-Launch AI Model Evaluation Following Claude Mythos Developments

**Jurisdiction:** Federal | **Category:** AI Law | **Date:** 2026-05-08

## Summary [HIGH confidence]

The Trump administration is considering an executive order that would require advanced AI models to undergo mandatory government vetting before public release, a significant departure from the deregulatory posture it adopted on taking office. The policy reversal is driven directly by concerns over Anthropic's Claude Mythos model — a frontier system capable of autonomously discovering and exploiting zero-day software vulnerabilities at scale — which prompted senior White House officials, the Office of the National Cyber Director (ONCD), and Vice President JD Vance to engage AI developers on security and safety protocols. National Economic Council Director Kevin Hassett described the administration as studying a process modeled on [FDA drug approval](https://thehill.com/policy/technology/5866292-white-house-ai-evaluation-process/), where AI models would have to be "proven safe" before release.

## Key Facts [HIGH confidence]

- National Economic Council Director Kevin Hassett confirmed on May 6, 2026, that the White House is [studying an executive order](https://www.bloomberg.com/news/articles/2026-05-06/white-house-preps-order-to-boost-ai-security-hassett-says) that would create a mandatory pre-release vetting process for high-risk AI models, analogizing the framework to FDA drug-approval requirements.
- The White House's [Office of the National Cyber Director](https://www.axios.com/2026/05/04/trump-white-house-ai-safety-tests-mythos) hosted two meetings in late April 2026 — one with tech and cybersecurity companies, and a separate session with major tech trade groups — to address security risks raised by advanced AI, including Anthropic's Mythos Preview.
- The proposed oversight structure [would grant agencies such as the NSA, ONCD, and the Office of the Director of National Intelligence early access](https://www.cnbc.com/2026/05/05/ai-oversight-trump-google-microsoft-xai.html) to frontier models without necessarily blocking their release, with classified testing environments available.
- White House staff [briefed senior leaders from Anthropic, Google, and OpenAI](https://fortune.com/2026/05/06/trump-administration-embraces-ai-oversight-policies-it-once-rejected-anthropic-mythos-caisi/) on the emerging oversight plans in the week of April 28, 2026.
- White House Chief of Staff Susie Wiles and Treasury Secretary Scott Bessent [met with Anthropic CEO Dario Amodei on April 17, 2026](https://www.axios.com/2026/04/17/anthropic-white-house-wiles-bessent-amodei), with Amodei also meeting National Cyber Director Sean Cairncross — the sessions described as "productive and constructive" by the White House.
- The administration's pivot follows its [January 2025 revocation of the Biden AI executive order](https://www.theregister.com/ai-and-ml/2026/05/08/trump-jumps-from-anything-goes-to-strict-regulation-ai-policy/5234687) that had established AI risk-management requirements — making the current discussions a notable policy reversal.
- A White House official told The New York Times that talk of a formal executive order is ["speculation"](https://www.tomshardware.com/tech-industry/artificial-intelligence/white-house-considers-mandatory-government-vetting-of-ai-models-before-release) and that any announcement would come directly from President Trump.
- NIST's Center for AI Standards and Innovation (CAISI) simultaneously announced on May 5, 2026, that it [signed pre-deployment evaluation agreements with Google DeepMind, Microsoft, and xAI](https://www.hpcwire.com/off-the-wire/nists-caisi-announces-new-frontier-ai-testing-agreements-with-google-deepmind-microsoft-xai/), expanding the program to all five major US AI laboratories and completing more than 40 model evaluations to date.

## The Catalyst: Claude Mythos and Project Glasswing [HIGH confidence]

Anthropic's Claude Mythos Preview — released on a restricted basis via [Project Glasswing](https://www.anthropic.com/glasswing) on April 7, 2026 — is the proximate cause of the administration's shift. The model [autonomously discovered thousands of high-severity zero-day vulnerabilities](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html) across major operating systems, web browsers, and other critical infrastructure, including flaws more than 27 years old. Because of its offensive-cyber potential, Anthropic declined general availability and instead limited access to roughly 50 organizations — major technology firms, banks, and critical-infrastructure operators — under contractual obligations to use the model for defensive vulnerability remediation.

The [Glasswing structure](https://www.anthropic.com/glasswing) is essentially a private pre-deployment review: Anthropic acts as gatekeeper, deciding who may use the capability and for what purpose. The White House is now considering whether the federal government should play a similar or superior gatekeeping role for frontier AI models going forward — one that is institutionalized rather than left to individual developers.

Vice President JD Vance — who in February 2025 stated at the Paris AI Action Summit that he was ["not here to talk about AI safety"](https://www.presidency.ucsb.edu/documents/remarks-the-vice-president-the-artificial-intelligence-action-summit-paris-france) — reportedly urged major AI developers to collaborate with the government on the safety and security concerns raised by Mythos' cybersecurity capabilities, marking a shift in his public posture.

## Proposed Framework and UK Comparison [MEDIUM confidence]

The administration is considering adopting elements of the [UK AI Security Institute (AISI) model](https://www.gov.uk/government/publications/ai-safety-institute-approach-to-evaluations/ai-safety-institute-approach-to-evaluations), under which the UK government conducts structured pre-deployment capability assessments against safety benchmarks before frontier models are released commercially. The AISI focuses on cybersecurity, biosecurity, chemical threats, and AI autonomy in its evaluations.

The US equivalent under consideration would expand CAISI's existing voluntary pre-deployment program into a mandatory framework with defined timelines and criteria. The CAISI program already includes [classified evaluation environments and interagency participation via the TRAINS Taskforce](https://www.ciodive.com/news/Google-Microsoft-xAI-to-face-security-testing/819375/), drawing evaluators from the Departments of Defense, Energy, and Homeland Security. If codified by executive order, participation would shift from voluntary to mandatory for models above a capability threshold.

Kevin Hassett's FDA-drug analogy is instructive: FDA pre-market approval requires affirmative demonstration of safety and efficacy before commercial sale. Applied to AI, this would represent a presumption against release pending government clearance — the inverse of the current approach, where models may be released unless the government intervenes.

## Action Items

- **Monitor White House communications closely.** The executive order remains in study phase as of May 8, 2026. Any formal announcement would come from President Trump directly, per White House officials. Organizations deploying or building frontier AI models should track this space weekly.
- **Assess CAISI agreement implications.** The voluntary CAISI pre-deployment evaluation program now covers all five major US AI labs. If an executive order formalizes and expands this program, organizations outside the existing agreements may face new obligations. Review your organization's frontier model development roadmap against potential new pre-release review timelines.
- **Evaluate compliance posture for cybersecurity-capable AI.** The Mythos precedent suggests the administration's threshold for "high-risk" AI centers on cybersecurity and national security capabilities. Organizations developing or deploying AI with significant vulnerability-detection, penetration-testing, or code-exploitation capabilities should prepare for heightened scrutiny.
- **Review UK AISI framework as a reference model.** The administration has explicitly cited the UK approach as a template. Legal and compliance teams should familiarize themselves with the [AISI evaluation methodology](https://www.gov.uk/government/publications/ai-safety-institute-approach-to-evaluations/ai-safety-institute-approach-to-evaluations) as a likely basis for any US counterpart.
- **Engage trade associations.** The ONCD has convened industry working sessions. Participation through trade groups is an early avenue for shaping implementation details before any order is finalized.

## Related Reports

- [reports/ai-law/frontier-models/federal-caisi-uk-aisi-pre-deployment-model-evaluations-2026-05-06.md](../frontier-models/federal-caisi-uk-aisi-pre-deployment-model-evaluations-2026-05-06.md) — Covers the May 5, 2026 CAISI agreements with Google DeepMind, Microsoft, and xAI that form the voluntary framework the executive order would potentially codify and expand.
- [reports/ai-law/frontier-models/federal-anthropic-project-glasswing-claude-mythos-2026-04-14.md](../frontier-models/federal-anthropic-project-glasswing-claude-mythos-2026-04-14.md) — Covers Project Glasswing and Claude Mythos Preview in detail — the proximate catalyst for the White House's policy reversal described in this report.
- [reports/ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md](../trump-ai-executive-order-state-preemption-2026-04-12.md) — Covers the December 2025 Trump AI executive order establishing national AI policy; a new executive order on pre-deployment review would amend or supplement that framework.

## Sources

1. [Axios: Trump administration considering safety review for new AI models after Mythos](https://www.axios.com/2026/05/04/trump-white-house-ai-safety-tests-mythos) — Primary source reporting on ONCD meetings and White House deliberations, dated May 4, 2026.
2. [Bloomberg: White House Prepares Order to Boost AI Security, Hassett Says](https://www.bloomberg.com/news/articles/2026-05-06/white-house-preps-order-to-boost-ai-security-hassett-says) — Reports Kevin Hassett's confirmation of executive order study; May 6, 2026.
3. [The Hill: Hassett says White House may review AI models "like an FDA drug"](https://thehill.com/policy/technology/5866292-white-house-ai-evaluation-process/) — Quotes Hassett's FDA analogy in detail.
4. [CNBC: Trump admin moves further into AI oversight, will test Google, Microsoft and xAI models](https://www.cnbc.com/2026/05/05/ai-oversight-trump-google-microsoft-xai.html) — Reports on CAISI agreements and oversight expansion; May 5, 2026.
5. [Fortune: Trump administration suddenly embraces AI oversight ideas it once rejected](https://fortune.com/2026/05/06/trump-administration-embraces-ai-oversight-policies-it-once-rejected-anthropic-mythos-caisi/) — Analysis of administration policy reversal and CAISI context.
6. [Tom's Hardware: Trump administration considers mandatory pre-release vetting of AI models](https://www.tomshardware.com/tech-industry/artificial-intelligence/trump-administration-considers-mandatory-pre-release-vetting-of-ai-models) — Covers White House official's "speculation" statement and NYT sourcing.
7. [Tom's Hardware: White House reportedly considers mandatory government vetting of AI models before release](https://www.tomshardware.com/tech-industry/artificial-intelligence/white-house-considers-mandatory-government-vetting-of-ai-models-before-release) — Additional detail on proposed framework and agency roles.
8. [The Register: Trump jumps from 'anything goes' to 'strict regulation' AI policy](https://www.theregister.com/ai-and-ml/2026/05/08/trump-jumps-from-anything-goes-to-strict-regulation-ai-policy/5234687) — Covers the policy shift in context of the January 2025 Biden EO revocation.
9. [HPCwire: NIST's CAISI Announces New Frontier AI Testing Agreements with Google DeepMind, Microsoft, xAI](https://www.hpcwire.com/off-the-wire/nists-caisi-announces-new-frontier-ai-testing-agreements-with-google-deepmind-microsoft-xai/) — Official CAISI program announcement and evaluation statistics.
10. [CIO Dive: Google, Microsoft and xAI's frontier AI to face national security testing](https://www.ciodive.com/news/Google-Microsoft-xAI-to-face-security-testing/819375/) — Details on classified evaluation environments and TRAINS Taskforce.
11. [Anthropic: Project Glasswing](https://www.anthropic.com/glasswing) — Official Anthropic announcement of the restricted access program.
12. [The Hacker News: Anthropic's Claude Mythos Finds Thousands of Zero-Day Flaws Across Major Systems](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html) — Technical details on Mythos vulnerability discovery capabilities.
13. [Axios: Scoop: Bessent and Wiles met Anthropic's Amodei in sign of thaw](https://www.axios.com/2026/04/17/anthropic-white-house-wiles-bessent-amodei) — Details of April 17, 2026 White House meeting with Anthropic CEO.
14. [UK Government: AI Safety Institute approach to evaluations](https://www.gov.uk/government/publications/ai-safety-institute-approach-to-evaluations/ai-safety-institute-approach-to-evaluations) — Official UK AISI evaluation methodology, cited as a template for the proposed US framework.
15. [American Presidency Project: Vance AI Action Summit Remarks](https://www.presidency.ucsb.edu/documents/remarks-the-vice-president-the-artificial-intelligence-action-summit-paris-france) — Official transcript of Vance's February 2025 Paris speech, providing baseline for comparing his prior AI safety posture.
16. [Just Security: Too Dangerous to Deploy: Anthropic's Mythos and What Comes Next](https://www.justsecurity.org/138011/too-dangerous-anthropic-mythos/) — Legal and national security analysis of the Mythos deployment implications.
