---
title: "NIST Plans Summer 2026 Release of AI Cybersecurity Framework Profile (NISTIR 8596)"
date: 2026-05-19
jurisdiction: "Federal"
category: "cybersecurity"
development_type: "guidance"
finding_id: "SCAN-20260519-046"
topic_key: "NIST-PLANS-SUMMER-2026-RELEASE-OF-A-2026"
topic_type: "guidance"
first_reported: 2026-05-19
last_updated: 2026-05-20
status_history:
  - "2026-05-20: Corrected misattribution in Impact Assessment — 'de facto benchmark' quote reassigned from Goodwin Law to Crowell & Moring (reviewer round 1 fix)."
cluster: "NIST Cybersecurity Framework Profile for AI (NISTIR 8596 / Cyber AI Profile)"
cluster_slug: "nist-csf-cyber-ai-profile-nistir8596"
---

# NIST Plans Summer 2026 Release of AI Cybersecurity Framework Profile (NISTIR 8596)

**Jurisdiction:** Federal | **Category:** Cybersecurity | **Date:** May 19, 2026

## Executive Summary [MEDIUM confidence]

NIST announced in May 2026 that it expects to release the initial public draft of the Cybersecurity Framework Profile for Artificial Intelligence (NISTIR 8596), known as the Cyber AI Profile, in summer 2026, pending internal agency approval. The profile layers AI-specific cybersecurity priorities onto the existing NIST Cybersecurity Framework 2.0 (CSF 2.0) and covers three focus areas: securing AI systems, using AI for cyber defense, and thwarting AI-enabled attacks. A companion document — overlay guidance for predictive AI systems — is also expected in summer 2026, while overlay guidance for agentic AI systems is targeted for late summer or early fall 2026. NIST aims to finalize all related guidance by 2027. For organizations deploying AI systems, this framework is likely to become a de facto benchmark for assessing cybersecurity diligence, particularly among federal agencies, contractors, and regulated industries.

## Background [HIGH confidence]

The Cyber AI Profile originates from a recognition that the NIST Cybersecurity Framework 2.0 — [published February 2024](https://www.nist.gov/cyberframework) — does not directly address the specific cybersecurity risks and opportunities associated with AI systems. NIST and the National Cybersecurity Center of Excellence (NCCoE) undertook a collaborative effort, drawing a community of interest of more than 6,500 participants, to develop tailored cybersecurity guidance for AI.

The development timeline proceeded as follows:

- **February 2025**: NIST released an initial concept paper outlining the scope of the profile.
- **April 2025**: NIST conducted a public workshop on the concept paper.
- **Summer 2025**: A series of community of interest meetings refined the approach.
- **December 16, 2025**: NIST published the [preliminary draft NIST IR 8596](https://csrc.nist.gov/pubs/ir/8596/iprd), opening a 45-day public comment period through January 30, 2026.
- **January 14, 2026**: NIST held a hybrid workshop to discuss the preliminary draft alongside updates on the companion COSAiS control overlays.
- **April–May 2026**: NIST held Spring Virtual Working Sessions (April 28, May 5, and May 12, 2026) to process comment responses.
- **Summer 2026**: Initial public draft expected, pending internal approval.
- **2027**: Final publication targeted.

The Cyber AI Profile is a companion product to two broader NIST AI frameworks: the [AI Risk Management Framework (AI RMF)](https://www.nist.gov/itl/ai-risk-management-framework) and the [Secure Software Development Framework](https://csrc.nist.gov/Projects/ssdf). Where those documents address AI governance broadly, NISTIR 8596 focuses specifically on cybersecurity risk management for AI.

## Detailed Analysis [MEDIUM confidence]

### Scope and Three Focus Areas

NISTIR 8596 organizes guidance around three overlapping focus areas, reflecting AI's dual role as both a target and a tool:

1. **Securing AI Systems ("Secure")**: Addresses cybersecurity risks that arise from integrating AI components into an organization's environment — including adversarial attacks on model inputs (prompt injection, evasion attacks), supply chain risks from third-party AI models, and vulnerabilities in AI pipelines. The preliminary draft notes that AI systems exhibit unique failure modes that conventional cybersecurity controls do not fully address.

2. **Conducting AI-Enabled Cyber Defense ("Defend")**: Encourages organizations to leverage AI for cybersecurity — for example, automating threat intelligence analysis, deploying AI-assisted incident response, and using agentic AI to accelerate vulnerability management.

3. **Thwarting AI-Enabled Cyberattacks ("Thwart")**: Prepares organizations for adversaries who use AI to amplify attacks — including deepfakes targeting personnel, generative AI-assisted phishing and fraud, and autonomous agent-driven vulnerability exploitation.

The profile is organized using the CSF 2.0 structure of Functions, Categories, and Subcategories, which allows organizations already operating under CSF 2.0 programs to layer AI-specific controls without reconstructing their security architecture.

### Agentic AI: A Central Concern

A notable feature of the draft is its treatment of agentic AI systems — AI that can take sequences of actions with limited human intervention, interact with other AI agents, and operate at machine speed. The [preliminary draft text](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8596.iprd.pdf) describes agentic AI as introducing identity and authorization challenges that static access reviews cannot address, calling for real-time identity controls that treat AI agents as distinct principals in an enterprise's security architecture.

This theme is reinforced by a companion [NCCoE concept paper on AI agent identity and authorization](https://www.nccoe.nist.gov/sites/default/files/2026-02/accelerating-the-adoption-of-software-and-ai-agent-identity-and-authorization-concept-paper.pdf) published February 5, 2026, which addresses the gap where AI agents are commonly treated as generic service accounts with no dedicated identity, authorization, or accountability controls.

### COSAiS Control Overlays

Alongside the Cyber AI Profile, NIST is developing the [Control Overlays for Securing AI Systems (COSAiS)](https://csrc.nist.gov/projects/cosais) — a series of SP 800-53 control overlays that provide implementation-level guidance. The COSAiS project covers five AI deployment categories, including single-agent and multi-agent systems. These overlays are designed to help organizations map existing NIST 800-53 controls to specific AI deployment patterns.

As of January 8, 2026, NIST published an annotated outline (discussion draft) of the overlay for predictive AI — "Using and Fine-Tuning Predictive AI" — with an initial public draft expected in summer 2026. The overlay for agentic AI systems is expected in late summer or early fall 2026, per the [Nextgov/FCW reporting](https://www.nextgov.com/artificial-intelligence/2026/05/nist-aims-summer-release-ai-cyber-guidelines/413559/).

### Relationship to Other Frameworks

The Cyber AI Profile is explicitly positioned as additive to, not a replacement for, existing frameworks. As [Crowell & Moring's analysis](https://www.crowell.com/en/insights/client-alerts/nist-releases-draft-framework-for-ai-cybersecurity-solicits-public-comment-what-organizations-using-or-deploying-ai-should-know) notes, the profile "layers AI-specific priorities and considerations onto the CSF 2.0" and provides mappings to NIST AI RMF, NIST SP 800-53, and other resources. FedRAMP-related standards and FISMA-implementing controls reference NIST CSF, making the Cyber AI Profile a likely indirect input into federal procurement and authorization processes.

The Department of Defense's CMMC framework has also begun incorporating AI security requirements, and [Crowell & Moring separately notes](https://www.crowell.com/en/insights/client-alerts/cmmc-for-ai-defense-policy-law-imposes-ai-security-framework-and-requirements-on-contractors) that defense policy law now imposes AI security framework requirements on contractors — a path that the Cyber AI Profile may inform.

## Impact Assessment [MEDIUM confidence]

### Who Is Affected

The profile is explicitly voluntary for most organizations. However, the following categories face heightened relevance:

- **Federal agencies and their contractors**: FISMA requires agencies to implement NIST security standards. Agencies deploying AI systems — an increasingly common occurrence — will be expected to incorporate the Cyber AI Profile guidance into their risk management programs. Contractors subject to CMMC or NIST SP 800-171 requirements should monitor whether the AI-specific controls from COSAiS become mandatory for federal contract work.
- **FedRAMP-authorized cloud service providers**: As NIST standards inform FedRAMP baselines, providers deploying AI components in their offerings should anticipate future FedRAMP guidance incorporating Cyber AI Profile concepts.
- **Regulated industries**: Sectors subject to sector-specific cybersecurity requirements (healthcare under HIPAA, financial services under NYDFS Cybersecurity Regulation or FTC Safeguards Rule) should monitor how their regulators incorporate NIST AI guidance, as NIST frameworks frequently become benchmarks for what constitutes "reasonable" security.
- **AI developers and deployers broadly**: As [Crowell & Moring observes](https://www.crowell.com/en/insights/client-alerts/nist-releases-draft-framework-for-ai-cybersecurity-solicits-public-comment-what-organizations-using-or-deploying-ai-should-know), the profile has "the potential to become a de facto benchmark for regulators, auditors, plaintiffs, and counterparties" assessing cybersecurity diligence for AI-enabled systems. [Goodwin Law's analysis](https://www.goodwinlaw.com/en/insights/publications/2026/01/alerts-otherindustries-ai-risk-meets-cyber-governance) similarly highlights the profile's implications for litigation and regulatory risk.

### Compliance Timeline

No mandatory compliance deadline exists at this time. The framework is voluntary. The relevant milestones are:

| Milestone | Expected Date |
|---|---|
| Initial public draft of NISTIR 8596 | Summer 2026 (pending agency approval) |
| Predictive AI COSAiS overlay (initial public draft) | Summer 2026 |
| Agentic AI COSAiS overlay (initial public draft) | Late summer / early fall 2026 |
| Final publication of NISTIR 8596 | 2027 (target) |

### Enforcement Outlook

NIST guidance is non-binding for private-sector organizations but carries significant soft-law weight. The pattern with CSF 2.0 and NIST AI RMF has been that private litigation, regulatory enforcement, and procurement requirements increasingly incorporate NIST standards as the baseline for "reasonable" security practices. Organizations that cannot demonstrate alignment with the Cyber AI Profile face reputational and legal risk as the standard gains adoption.

## Action Items

- Review the [preliminary draft NIST IR 8596](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8596.iprd.pdf) to understand the current direction of the Cyber AI Profile before the initial public draft is released.
- Monitor the [NCCoE Cyber AI Profile project page](https://www.nccoe.nist.gov/projects/cyber-ai-profile) for the summer 2026 release announcement of the initial public draft.
- Conduct a gap assessment against the three focus areas (Secure, Defend, Thwart) to identify which CSF 2.0 subcategories are implicated by your AI deployments.
- For organizations using or planning to use agentic AI systems: review the NCCoE concept paper on AI agent identity and authorization as a preview of what the agentic AI COSAiS overlay will likely require.
- Federal contractors and agencies: assess exposure under CMMC and any AI security-related contract requirements that may incorporate Cyber AI Profile or COSAiS controls.
- Engage in the public comment process on the initial public draft when it is released (comment period details to be announced with the summer 2026 release).
- Track the COSAiS overlay releases for predictive and agentic AI, as these provide implementation-level detail that the higher-level profile does not.
- Update AI-related incident response plans to address adversarial AI attack scenarios identified in the Thwart focus area.

## Related Reports

- [reports/cybersecurity/standards-guidance/federal-five-eyes-agentic-ai-guidance-2026-05-01.md](reports/cybersecurity/standards-guidance/federal-five-eyes-agentic-ai-guidance-2026-05-01.md) -- Five Eyes joint guidance on agentic AI cybersecurity issued May 2026 addresses overlapping agentic AI security concerns that NISTIR 8596 also targets.
- [reports/cybersecurity/standards-guidance/federal-oncd-ai-cyber-defense-industry-outreach-2026-05-01.md](reports/cybersecurity/standards-guidance/federal-oncd-ai-cyber-defense-industry-outreach-2026-05-01.md) -- White House ONCD outreach on AI-enhanced cyber defenses overlaps with the Cyber AI Profile's "Defend" focus area and represents a parallel federal initiative.
- [reports/cybersecurity/standards-guidance/federal-ai-cyberattack-agency-response-2026-04-15.md](reports/cybersecurity/standards-guidance/federal-ai-cyberattack-agency-response-2026-04-15.md) -- Government response to AI-enabled cyberattacks frames the threat landscape that the NIST Cyber AI Profile's "Thwart" focus area directly addresses.
- [reports/cybersecurity/standards-guidance/new-york-nydfs-ai-cybersecurity-guidance-2024-10-16.md](reports/cybersecurity/standards-guidance/new-york-nydfs-ai-cybersecurity-guidance-2024-10-16.md) -- NYDFS AI cybersecurity guidance represents how a sector regulator has already translated NIST-adjacent AI security concepts into binding requirements for financial services firms.

## Sources

1. [Nextgov/FCW: NIST aims for summer release of AI cyber guidelines](https://www.nextgov.com/artificial-intelligence/2026/05/nist-aims-summer-release-ai-cyber-guidelines/413559/) -- Primary source reporting NIST's announced summer 2026 release timeline for the initial public draft and overlay guidance schedule.
2. [CSRC: NISTIR 8596 (Preliminary Draft) — Cybersecurity Framework Profile for Artificial Intelligence](https://csrc.nist.gov/pubs/ir/8596/iprd) -- Official NIST/CSRC landing page for the preliminary draft of NISTIR 8596.
3. [NIST.gov: Draft NIST Guidelines Rethink Cybersecurity for the AI Era](https://www.nist.gov/news-events/news/2025/12/draft-nist-guidelines-rethink-cybersecurity-ai-era) -- Official NIST press release announcing the December 16, 2025 preliminary draft release.
4. [CSRC: NIST releases prelim draft of Cyber AI profile](https://csrc.nist.gov/News/2025/nist-releases-prelim-draft-cyber-ai-profile) -- CSRC news item announcing the preliminary draft with community of interest statistics.
5. [NCCoE: Cyber AI Profile project page](https://www.nccoe.nist.gov/projects/cyber-ai-profile) -- NCCoE landing page tracking project milestones, workshops, and publication status.
6. [NCCoE: NIST IR 8596 ipd — Initial Public Draft page](https://www.nccoe.nist.gov/publications/csf-profile/nist-ir-8596-ipd-cybersecurity-framework-profile-artificial-intelligence) -- NCCoE publication page for the initial public draft (listing Spring 2026 working sessions and current status).
7. [NIST: Preliminary draft PDF (NIST.IR.8596.iprd)](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8596.iprd.pdf) -- Full text of the preliminary draft, directly available from NIST servers.
8. [CSRC: Control Overlays for Securing AI Systems (COSAiS)](https://csrc.nist.gov/projects/cosais) -- Official NIST project page for the SP 800-53 control overlays for AI systems.
9. [NCCoE: Concept paper — Accelerating the Adoption of Software and AI Agent Identity and Authorization](https://www.nccoe.nist.gov/sites/default/files/2026-02/accelerating-the-adoption-of-software-and-ai-agent-identity-and-authorization-concept-paper.pdf) -- NCCoE companion paper on AI agent identity, directly relevant to the agentic AI overlay.
10. [Crowell & Moring: NIST Releases Draft Framework for AI Cybersecurity](https://www.crowell.com/en/insights/client-alerts/nist-releases-draft-framework-for-ai-cybersecurity-solicits-public-comment-what-organizations-using-or-deploying-ai-should-know) -- Law firm analysis of practical compliance implications; source for "de facto benchmark" characterization.
11. [Goodwin Law: AI Risk Meets Cyber Governance — NIST's Draft Cyber AI Profile](https://www.goodwinlaw.com/en/insights/publications/2026/01/alerts-otherindustries-ai-risk-meets-cyber-governance) -- Independent law firm analysis of litigation and regulatory risk implications.
12. [National Law Review: NIST Issues Preliminary Draft of Cyber AI Profile](https://natlawreview.com/article/nist-issues-preliminary-draft-cyber-ai-profile-framework-poised-alter-security) -- Analysis framing the profile as poised to alter security operations.
13. [Crowell & Moring: CMMC for AI — Defense Policy Law Imposes AI Security Requirements on Contractors](https://www.crowell.com/en/insights/client-alerts/cmmc-for-ai-defense-policy-law-imposes-ai-security-framework-and-requirements-on-contractors) -- Analysis of how defense contractor AI security requirements intersect with NIST guidance.
14. [CSA Lab Space: NIST AI Agent Standards Initiative](https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-ai-agent-standards-initiative-2026040/) -- Cloud Security Alliance analysis of the broader NIST AI agent standards effort and its enterprise security implications.
