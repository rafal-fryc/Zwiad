---
title: "Anthropic Introduces Government ID Verification for Claude via Persona; EU AI Office Excluded from Claude Mythos Access"
date: 2026-04-19
jurisdiction: "Federal"
category: "ai-law"
development_type: "other"
finding_id: "SCAN-20260419-025"
topic_key: "federal-anthropic-id-verification-persona-2026"
topic_type: "guidance"
first_reported: 2026-04-17
last_updated: 2026-04-19
status_history: []
cluster: "Anthropic Claude Mythos: AI-Driven Vulnerability Research"
cluster_slug: "anthropic-claude-mythos-cybersecurity"
---

# Anthropic Introduces Government ID Verification for Claude via Persona; EU AI Office Excluded from Claude Mythos Access

**Jurisdiction:** Federal, International | **Category:** ai-law | **Date:** 2026-04-19

## Executive Summary [MEDIUM confidence]

During the week of April 14–16, 2026, Anthropic quietly published a [help center article](https://support.claude.com/en/articles/14328960-identity-verification-on-claude) disclosing that it has introduced government-issued ID verification for access to "certain capabilities" of its Claude AI models, partnering with San Francisco-based identity verification firm Persona Identities. The verification process requires users to submit a physical government ID document and complete a live selfie biometric match; Anthropic states that neither images nor identity data will be used to train Claude models. Simultaneously, critics and AI safety organizations have raised concerns about the European Union AI Office's exclusion from testing access to Claude Mythos — Anthropic's most capable frontier model, restricted under Project Glasswing — highlighting a growing governance gap between the EU and UK regulatory bodies. These two developments together signal a significant evolution in how Anthropic is managing access to its most powerful capabilities: identity-gating at the user level, and selective institutional access at the frontier model level.

## Background [MEDIUM confidence]

### Frontier Model Access Controls: Project Glasswing and Claude Mythos

In early April 2026, Anthropic announced [Project Glasswing](https://www.anthropic.com/glasswing), a restricted-access cybersecurity initiative built around Claude Mythos Preview — a model that Anthropic determined was too dangerous to release publicly after internal testing demonstrated autonomous discovery and exploitation of zero-day vulnerabilities across every major operating system and browser. Access was extended only to a named consortium of 12 large technology and finance firms and approximately 40 additional critical-software maintainers. (Full analysis is available in this knowledge base's companion report on Project Glasswing and Claude Mythos.)

The UK AI Security Institute received pre-deployment testing access and published technical analysis within a week of the announcement. By contrast, EU agencies were largely excluded from direct model access, with only Germany's Federal Office for Information Security (BSI) confirming it had opened talks with Anthropic — without direct access to the model itself.

### Regulatory Backdrop: EU GPAI Code of Practice

Anthropic is a signatory to the EU's [General-Purpose AI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai), which entered its application phase on August 2, 2025. Signatories to the Code who provide models classified as carrying systemic risk — a category Claude Mythos almost certainly falls within — are required to draw up a Safety and Security Framework and to provide the EU AI Office with unredacted access within prescribed timeframes following a qualifying safety event. Full Commission enforcement powers over Code signatories take effect on August 2, 2026, per [EU AI Act timelines](https://axis-intelligence.com/eu-ai-act-news-2026/).

### Anthropic's Existing Usage Policy Framework

Prior to the ID verification rollout, Anthropic enforced its Acceptable Use Policy through behavioral monitoring and account enforcement. The introduction of biometric identity verification represents a structural shift: from post-hoc policy enforcement to pre-access identity confirmation for designated capabilities or risk signals.

## Detailed Analysis [MEDIUM confidence]

### The ID Verification Policy

Anthropic's [help center disclosure](https://support.claude.com/en/articles/14328960-identity-verification-on-claude) states that users "might see a verification prompt when accessing certain capabilities, as part of our routine platform integrity checks, or other safety and compliance measures." Anthropic has not published a comprehensive list of which capabilities are gated or what specific behavioral signals trigger verification. An Anthropic spokesperson told [Engadget](https://www.engadget.com/ai/anthropic-will-ask-claude-users-to-verify-their-identities-for-a-few-use-cases-115754092.html) that checks are triggered "in situations where we see activity that indicates potentially fraudulent or abusive behaviour, which violates our usage policy."

The stated rationale encompasses three distinct goals:

1. **Abuse prevention** — detecting and blocking policy violators, underage users, and accounts in unsupported regions.
2. **Platform integrity** — proactive verification during routine checks, not merely reactive enforcement.
3. **Legal compliance** — meeting unspecified "legal and safety obligations," language that may signal anticipated regulatory requirements.

Anthropic's statement that "being responsible with powerful technology starts with knowing who is using it" aligns with broader industry trends toward Know Your Customer (KYC) approaches for high-risk AI capabilities, as [Help Net Security](https://www.helpnetsecurity.com/2026/04/16/anthropic-claude-identity-verification-government-id/) notes this makes Claude the first major AI chatbot to implement such checks.

### The Persona Identities Partnership

Anthropic selected [Persona Identities, Inc.](https://withpersona.com/) as its verification partner — a San Francisco-based KYC/AML infrastructure provider that also supplies age verification for ChatGPT and facial age estimation for Roblox, per [Biometric Update](https://www.biometricupdate.com/202604/anthropic-adds-limited-biometric-id-verification-from-persona-to-claude). Accepted documents include passports, national identity cards, driver's licenses, and state/provincial ID cards. The process involves submitting a physical, undamaged document alongside a live selfie for biometric liveness detection; verification typically completes in under five minutes.

Under the data handling arrangement disclosed by Anthropic:

- Identity documents and selfie images are collected and held by Persona, not stored on Anthropic's own systems.
- Anthropic may access Persona's verification records for purposes such as reviewing user appeals.
- Anthropic states it does not copy or store ID images itself.
- Identity data will not be used to train Claude models.
- Data is encrypted in transit and at rest.
- Data sharing is limited to Persona and Anthropic, except where legally required.

Persona's own [privacy policy](https://withpersona.com/legal/privacy-policy) notes that the firm uses subprocessors including AWS, Google Cloud, and MongoDB for biometric data processing. Persona's default is to delete personal data immediately upon completing verification, though clients may direct longer retention for fraud investigation purposes.

### Privacy Concerns and Criticism

The rollout has drawn criticism on several grounds, as documented by [Decrypt](https://decrypt.co/364509/claude-anthropic-government-id-kyc-privacy) and [WinBuzzer](https://winbuzzer.com/2026/04/16/anthropic-claude-id-verification-backlash-xcxwbn/):

- **Prior Persona security incident:** In February 2026, a security researcher reported exposure of Persona's front end on a government server, prompting speculation about potential government surveillance links, per [Malwarebytes](https://www.malwarebytes.com/blog/news/2026/02/age-verification-vendor-persona-left-frontend-exposed). Persona's CEO responded on Hacker News disputing the characterization.
- **User migration irony:** Some users had migrated to Claude specifically due to privacy concerns about other AI providers, and now find themselves subject to biometric verification requirements they sought to avoid.
- **Opacity of triggers:** Anthropic's refusal to disclose which capabilities or behaviors trigger verification creates compliance uncertainty for users who cannot anticipate when they will be required to submit identity documents.
- **Subprocessor chain:** Persona's subprocessors include OpenAI among others, raising questions about data flows across competing AI companies' infrastructure.

### The Claude Mythos–EU AI Office Access Controversy

A distinct but related controversy involves Anthropic's decision not to share direct access to Claude Mythos with EU regulatory bodies. According to [The Decoder](https://the-decoder.com/claude-mythos-is-a-wake-up-call-for-europes-ai-safety-apparatus/) and [ResultSense](https://www.resultsense.com/news/2026-04-17-eu-ai-office-mythos-access-gap), the EU AI Office — despite being an Anthropic GPAI Code of Practice counterparty — did not receive testing access to Claude Mythos Preview when Project Glasswing launched.

Critics attribute this access gap to structural weaknesses in the EU AI Office:

- The EU AI Office has approximately 140 staff, with 36 in the safety unit responsible for evaluating the most capable models — a unit that eight AI safety groups have demanded be quadrupled to 160 staff by 2030.
- The AI Office lacks the technical depth and seniority to engage at parity with a company releasing a model capable of autonomously exploiting zero-days across all major operating systems.
- Yoshua Bengio, quoted by POLITICO, described it as "deeply concerning" that technology companies rather than regulators are determining how to handle these risks.

The European Commission confirmed on April 15, 2026 that it had opened formal talks with Anthropic on Claude Mythos, covering both the model's cyber-defense potential and systemic threat implications, per [Startup News](https://startupnews.fyi/2026/04/16/eu-in-talks-with-anthropic-over-risks-of-ai-model-mythos/) and the [EC Audiovisual Service midday briefing of April 17, 2026](https://audiovisual.ec.europa.eu/en/media/video/I-287781). However, these talks were initiated after the Project Glasswing announcement — not before — suggesting the EU was responding reactively rather than engaging as a peer in the pre-deployment safety review that the UK AISI conducted.

### Connection Between the Two Developments

While Anthropic has not publicly stated that the ID verification rollout is specifically designed to gate access to Mythos-class capabilities, the timing is notable. As [CodeRoasis](https://coderoasis.com/anthropic-claude-kyc-identity-verification-2026/) and [PiuNikaWeb](https://piunikaweb.com/2026/04/16/anthropic-claude-identity-verification-persona/) observe, the timing of the ID verification policy aligns with the Mythos Preview release. It is plausible that Anthropic anticipates that its most dangerous capabilities — including any eventual broader rollout of Mythos-class functionality — will require identity-verified access as a harm reduction measure. This interpretation is consistent with Anthropic's stated rationale of "knowing who is using" powerful technology.

## Impact Assessment [MEDIUM confidence]

### Affected Users and Organizations

- **Individual Claude users** who engage in activities that Anthropic's systems flag as potentially abusive or who attempt to access designated high-capability features will be required to complete biometric ID verification through Persona before proceeding.
- **Privacy-sensitive individuals and organizations** — journalists, activists, researchers in sensitive domains — who cannot or prefer not to submit government identification to a third-party KYC provider may find certain Claude capabilities inaccessible.
- **EU-regulated AI deployers** will encounter a parallel track of risk: as GPAI Code of Practice enforcement matures, Anthropic's selective access decisions for frontier models like Mythos will come under increasing regulatory scrutiny.
- **EU government and regulatory bodies** face an institutional capability gap in evaluating frontier AI systems, as illustrated by the Mythos access disparity — a gap that has direct implications for EU AI Act enforcement credibility.

### Compliance Requirements and Timelines

There are currently no mandatory regulatory requirements in the United States compelling AI companies to implement KYC identity verification. Anthropic's rollout appears to be a voluntary safety measure, though the language about meeting "legal and safety obligations" may foreshadow anticipated requirements under child safety legislation (e.g., statutes analogous to COPPA enforcement or pending age-appropriate-design laws) or future AI safety regulations.

For EU regulatory compliance, the August 2, 2026 deadline for full GPAI Code of Practice enforcement is the critical date. Anthropic's compliance posture with the Code's AI Office access obligations — particularly regarding Mythos and its classification as a systemic-risk model — remains publicly unresolved.

### Enforcement Outlook

No enforcement actions related to either the ID verification rollout or the EU AI Office access controversy have been announced as of this writing. The EU Commission's confirmation of talks with Anthropic suggests diplomacy is the current mode, but the August 2026 enforcement window narrows the timeline for resolving formal compliance questions.

## Action Items

- **Compliance counsel for AI-deploying organizations:** Review whether any of your Claude-based applications or API integrations trigger Anthropic's ID verification conditions and assess downstream impacts on user experience and data processing obligations.
- **Privacy officers:** Evaluate data flow implications of the Persona verification pipeline — particularly Persona's subprocessors and data retention practices — against GDPR, CCPA, and sector-specific privacy obligations if your organization has users who may be asked to verify.
- **EU-regulated AI providers:** Monitor the European Commission's talks with Anthropic for any formal guidance on GPAI Code of Practice compliance regarding Mythos-class models. The August 2, 2026 enforcement date is a hard deadline for compliance documentation.
- **AI governance teams:** Track whether other frontier AI labs (OpenAI, Google DeepMind) follow Anthropic's KYC-for-capabilities pattern; this could become an emerging industry norm that regulatory guidance formalizes.
- **Legal and policy teams in EU institutions:** Assess whether current EU AI Office staffing and technical capacity is sufficient to exercise meaningful oversight over models that frontier labs may restrict to private partners, as the Mythos access gap has illustrated.

## Related Reports

- [reports/ai-law/frontier-models/federal-anthropic-project-glasswing-claude-mythos-2026-04-14.md](reports/ai-law/frontier-models/federal-anthropic-project-glasswing-claude-mythos-2026-04-14.md) — Companion report covering Project Glasswing, Claude Mythos capabilities, and the initial EU regulatory exclusion from pre-deployment testing.

## Sources

1. [Claude Help Center — Identity Verification on Claude](https://support.claude.com/en/articles/14328960-identity-verification-on-claude) — Anthropic's official help center disclosure of the ID verification program; process details, data handling, and privacy assurances.
2. [The Register — Anthropic starts checking ID for some Claude users](https://www.theregister.com/2026/04/16/anthropic_claude_id_verification_persona/) — Contemporaneous reporting on the rollout, Persona partnership, and initial reaction.
3. [Engadget — Anthropic will ask Claude users to verify their identities 'for a few use cases'](https://www.engadget.com/ai/anthropic-will-ask-claude-users-to-verify-their-identities-for-a-few-use-cases-115754092.html) — Source of Anthropic spokesperson quote on trigger conditions.
4. [Help Net Security — Anthropic tests user trust with ID and selfie checks for Claude](https://www.helpnetsecurity.com/2026/04/16/anthropic-claude-identity-verification-government-id/) — Detailed technical overview of the verification process and Persona partnership.
5. [Biometric Update — Anthropic adds limited biometric ID verification from Persona to Claude](https://www.biometricupdate.com/202604/anthropic-adds-limited-biometric-id-verification-from-persona-to-claude) — Industry coverage noting Persona also supplies verification for ChatGPT and Roblox.
6. [Decrypt — You Switched to Claude Over Surveillance Fears. Now It Wants Your Passport](https://decrypt.co/364509/claude-anthropic-government-id-kyc-privacy) — Privacy criticism and user backlash reporting.
7. [Malwarebytes — Age verification vendor Persona left frontend exposed](https://www.malwarebytes.com/blog/news/2026/02/age-verification-vendor-persona-left-frontend-exposed) — February 2026 security incident involving Persona's platform.
8. [Persona Identities — Privacy Policy](https://withpersona.com/legal/privacy-policy) — Persona's data handling, subprocessors, and retention practices.
9. [PiuNikaWeb — Anthropic adds Persona-based ID checks to Claude for select use cases](https://piunikaweb.com/2026/04/16/anthropic-claude-identity-verification-persona/) — Additional reporting on implementation and Mythos timing connection.
10. [The Decoder — Claude Mythos is a wake-up call for Europe's AI safety apparatus](https://the-decoder.com/claude-mythos-is-a-wake-up-call-for-europes-ai-safety-apparatus/) — Analysis of EU AI Office staffing and structural gaps in frontier model oversight.
11. [ResultSense — EU AI Office shut out of Mythos as UK AISI leads](https://www.resultsense.com/news/2026-04-17-eu-ai-office-mythos-access-gap) — Reporting on EU exclusion and comparative UK advantage.
12. [Startup News — EU in talks with Anthropic over risks of AI model Mythos](https://startupnews.fyi/2026/04/16/eu-in-talks-with-anthropic-over-risks-of-ai-model-mythos/) — EC formal talks confirmation.
13. [Courthouse News Service — EU in talks with Anthropic over risks of AI model Mythos](https://www.courthousenews.com/eu-in-talks-with-anthropic-over-risks-of-ai-model-mythos/) — Additional reporting on EU-Anthropic dialogue.
14. [EC Audiovisual Service — EC Midday press briefing of 17/04/2026](https://audiovisual.ec.europa.eu/en/media/video/I-287781) — Commission's public statement on Mythos talks and dual-strand engagement with Anthropic.
15. [Anthropic — Signing the EU Code of Practice](https://www.anthropic.com/news/eu-code-practice) — Anthropic's commitment to the GPAI Code of Practice and systemic-risk model obligations.
16. [EU GPAI Code of Practice (official)](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) — Official Code text including Safety and Security Framework obligations for systemic-risk GPAI models.
17. [IAPP — Claude Mythos: Rethinking cybersecurity and AI governance](https://iapp.org/news/a/claude-mythos-rethinking-cybersecurity-and-ai-governance) — IAPP analysis connecting Mythos to broader AI governance frameworks.
18. [WinBuzzer — Claude Now Requires ID Checks, Locking Out Some Users](https://winbuzzer.com/2026/04/16/anthropic-claude-id-verification-backlash-xcxwbn/) — User backlash and access restriction reporting.
