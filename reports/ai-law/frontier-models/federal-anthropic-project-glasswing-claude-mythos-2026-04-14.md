---
title: "Anthropic Restricts Claude Mythos Access via Project Glasswing Amid Frontier Cyber-Offensive Capability Concerns"
date: 2026-04-14
jurisdiction: "Federal"
category: "ai-law"
development_type: "guidance"
finding_id: "SCAN-20260414-015"
topic_key: "federal-33d2a8f0-2026"
topic_type: "guidance"
first_reported: 2026-04-14
last_updated: 2026-04-14
status_history: []
cluster: "Anthropic Claude Mythos: AI-Driven Vulnerability Research"
cluster_slug: "anthropic-claude-mythos-cybersecurity"
---

# Anthropic Restricts Claude Mythos Access via Project Glasswing Amid Frontier Cyber-Offensive Capability Concerns

## Executive Summary [HIGH confidence]

On April 7, 2026, Anthropic announced [Project Glasswing](https://www.anthropic.com/glasswing), a limited-access cybersecurity initiative built around a preview of its most advanced frontier model, Claude Mythos. According to Anthropic's [Mythos Preview technical note](https://red.anthropic.com/2026/mythos-preview/), internal testing showed the model can autonomously discover and weaponize zero-day vulnerabilities across every major operating system and web browser, including flaws as old as 27 years. Citing "unprecedented cybersecurity risks," Anthropic declined to make Mythos generally available and instead granted access to a consortium of 12 named US-based technology and finance firms and roughly 40 additional critical-software maintainers, per [Fortune](https://fortune.com/2026/04/07/anthropic-claude-mythos-model-project-glasswing-cybersecurity/) and [VentureBeat](https://venturebeat.com/technology/anthropic-says-its-most-powerful-ai-cyber-model-is-too-dangerous-to-release).

The release has immediate regulatory implications: the UK AI Security Institute (AISI) received testing access and has already triggered a financial-sector risk review, while EU cybersecurity agencies were largely excluded — raising questions about compliance with the EU AI Code of Practice and equitable frontier-model governance.

## Project Glasswing: Structure and Partners [HIGH confidence]

Per [Anthropic's announcement](https://www.anthropic.com/glasswing), the named launch partners are: Amazon Web Services, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorgan Chase, the Linux Foundation, Microsoft, Nvidia, and Palo Alto Networks. Anthropic extended access to "more than 40 additional organizations that build or maintain critical software," whose names have not been publicly disclosed. [CrowdStrike confirmed its founding-member status](https://www.crowdstrike.com/en-us/blog/crowdstrike-founding-member-anthropic-mythos-frontier-model-to-secure-ai/) in a coordinated blog post.

The program's stated goal is defensive: allow a curated set of vendors and infrastructure operators to find and patch vulnerabilities in their own code bases before the underlying capability proliferates. Anthropic has stated it does not plan to make Mythos Preview generally available.

## Demonstrated Capabilities [HIGH confidence]

Anthropic's red-team writeup and contemporaneous reporting document the following capabilities:

- **Thousands of zero-days discovered.** Per [The Hacker News](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html) and [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-latest-ai-model-identifies-thousands-of-zero-day-vulnerabilities-in-every-major-operating-system-and-every-major-web-browser-claude-mythos-preview-sparks-race-to-fix-critical-bugs-some-unpatched-for-decades), Mythos identified thousands of high-severity zero-days across every major OS and browser.
- **Autonomous exploitation of long-dormant flaws.** The model autonomously found and exploited a 17-year-old FreeBSD NFS remote-code-execution vulnerability (tracked as CVE-2026-4747) granting unauthenticated root, and a 27-year-old flaw in OpenBSD — an OS widely used for firewalls and hardened infrastructure — per [Help Net Security](https://www.helpnetsecurity.com/2026/04/08/anthropic-claude-mythos-preview-identify-vulnerabilities/) and [The Register](https://www.theregister.com/2026/04/07/anthropic_all_your_zerodays_are_belong_to_us/).
- **Multi-stage exploit chaining.** In one test, Mythos wrote a browser exploit chaining four vulnerabilities with a JIT heap spray to escape both renderer and OS sandboxes, per the [red team preview](https://red.anthropic.com/2026/mythos-preview/).
- **AISI benchmark results.** The UK AISI reported a 73% success rate on expert-level capture-the-flag tasks and full completion of its 32-step enterprise-network attack range on three of ten attempts, per [GovInfoSecurity](https://www.govinfosecurity.com/europe-ponders-claude-mythos-from-afar-a-31395).

## UK Regulatory Response [HIGH confidence]

The UK has been the most active jurisdiction to date. The [UK AI Security Institute](https://red.anthropic.com/2026/mythos-preview/) received pre-deployment testing access under its voluntary evaluations framework. Following AISI's findings:

- The UK AI Minister publicly confirmed AISI testing and said action had "already been taken" based on the results, per [Gizmodo](https://gizmodo.com/claude-mythos-preview-has-officially-frightened-the-british-2000745462).
- The Bank of England, the Financial Conduct Authority (FCA), and HM Treasury have reportedly opened high-level talks with the National Cyber Security Centre (NCSC) to assess critical financial infrastructure exposure, per [Tekedia](https://www.tekedia.com/uk-regulators-launch-urgent-review-of-anthropic-ai-model-claude-mythos-over-financial-system-cyber-risks/) and [BusinessToday](https://www.businesstoday.in/technology/story/anthropics-latest-ai-model-mythos-triggers-urgent-risk-review-by-uk-regulators-525315-2026-04-13).

## EU Exclusion and Governance Gap [MEDIUM confidence]

According to [The Decoder](https://the-decoder.com/claude-mythos-is-a-wake-up-call-for-europes-ai-safety-apparatus/) and [GovInfoSecurity](https://www.govinfosecurity.com/europe-ponders-claude-mythos-from-afar-a-31395), EU agencies have been largely sidelined:

- Only Germany's Federal Office for Information Security (BSI) has confirmed opening talks with Anthropic, and reportedly without direct test access.
- The EU AI Code of Practice obliges signatories to draw up a safety and security framework and to grant the European AI Office unredacted access within five working days of a qualifying event; the Commission has not publicly detailed Anthropic's compliance posture for Mythos.
- No EU cybersecurity agency appears on the Project Glasswing partner list.

This asymmetry — UK AISI and US private partners inside, EU regulators outside — is the most concrete governance signal from the release and is likely to feature in EU AI Act / Code of Practice enforcement discussions in Q2 2026.

## US Federal Posture [LOW confidence]

As of this writing, no US federal agency (CISA, NIST AISI, White House OSTP) has issued a public statement specifically addressing Mythos or Glasswing. The absence of a named US government partner on the Glasswing roster is notable given ongoing debate over the Trump administration's AI executive order and state preemption. Official US federal guidance could not be retrieved at time of writing; readers should monitor [CISA advisories](https://www.cisa.gov/news-events/cybersecurity-advisories) and the NIST AI Safety Institute for forthcoming statements.

## Regulatory and Compliance Implications [MEDIUM confidence]

1. **Frontier-model access governance is moving to bilateral, firm-by-firm arrangements.** Glasswing is a voluntary, access-gated structure — not a statutory regime. Expect regulators (especially in the EU) to push for mandatory pre-deployment testing parity.
2. **EU AI Code of Practice pressure.** The Commission is likely to seek public clarification of Anthropic's Article-level obligations (safety/security framework, AI Office access) given the model's demonstrated systemic-risk capability.
3. **Critical-infrastructure disclosure.** Financial-sector operators outside the named consortium may face regulator inquiries about their exposure to the classes of vulnerabilities Mythos has surfaced, particularly under NIS2 (EU) and FCA operational-resilience rules (UK).
4. **Coordinated vulnerability disclosure strain.** Thousands of zero-days moving through a 50-entity consortium places unprecedented load on CVD processes; expect ENISA, CISA, and CERT-EU guidance on handling AI-discovered vulnerability tranches.
5. **Dual-use export controls.** Expect renewed debate over whether offensive-capable frontier models fall within existing US export-control regimes (EAR) or require a dedicated framework.

## Action Items

- **Technology vendors:** If you are not a Glasswing partner, accelerate internal fuzzing and dependency audits of OS, browser, and legacy daemon code. The 17- and 27-year-old exploited vulnerabilities suggest deep codebase review is warranted.
- **Financial institutions (UK):** Anticipate FCA/PRA outreach on AI-cyber risk; prepare operational-resilience documentation.
- **EU-regulated providers:** Monitor European AI Office communications regarding Mythos and Code-of-Practice compliance; document your own frontier-model access posture.
- **In-house counsel for frontier AI labs:** Review pre-deployment testing commitments to UK AISI and US AISI for parity with EU obligations to reduce governance-asymmetry exposure.
- **CISOs generally:** Treat the Glasswing patch cycle as a high-priority reason to enable rapid patching across OS and browser fleets over the next 60–90 days.

## Sources

1. [Anthropic — Project Glasswing announcement](https://www.anthropic.com/glasswing) — Primary source; program structure, partner list, safety rationale.
2. [Anthropic Red — Claude Mythos Preview technical note](https://red.anthropic.com/2026/mythos-preview/) — Primary source; capability evaluations, exploit examples, AISI access.
3. [Fortune — "Anthropic is giving some firms early access to Claude Mythos"](https://fortune.com/2026/04/07/anthropic-claude-mythos-model-project-glasswing-cybersecurity/) — Partner list verification and business context.
4. [VentureBeat — "Anthropic says its most powerful AI cyber model is too dangerous to release publicly"](https://venturebeat.com/technology/anthropic-says-its-most-powerful-ai-cyber-model-is-too-dangerous-to-release) — Safety rationale.
5. [InfoQ — Anthropic Releases Claude Mythos Preview with Cybersecurity Capabilities](https://www.infoq.com/news/2026/04/anthropic-claude-mythos/) — Technical community coverage.
6. [CrowdStrike — Founding-member blog post](https://www.crowdstrike.com/en-us/blog/crowdstrike-founding-member-anthropic-mythos-frontier-model-to-secure-ai/) — Independent partner confirmation.
7. [The Hacker News — Mythos finds thousands of zero-days](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html) — Vulnerability-scale reporting.
8. [Tom's Hardware — Mythos Preview sparks race to fix critical bugs](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-latest-ai-model-identifies-thousands-of-zero-day-vulnerabilities-in-every-major-operating-system-and-every-major-web-browser-claude-mythos-preview-sparks-race-to-fix-critical-bugs-some-unpatched-for-decades) — Age and breadth of vulnerabilities.
9. [Help Net Security — Mythos finds and exploits zero-days across every major OS and browser](https://www.helpnetsecurity.com/2026/04/08/anthropic-claude-mythos-preview-identify-vulnerabilities/) — FreeBSD CVE and OpenBSD flaw details.
10. [The Register — Anthropic Mythos model can find and exploit 0-days](https://www.theregister.com/2026/04/07/anthropic_all_your_zerodays_are_belong_to_us/) — Independent corroboration.
11. [Gizmodo — "Claude Mythos Preview Has Officially Frightened the British"](https://gizmodo.com/claude-mythos-preview-has-officially-frightened-the-british-2000745462) — UK AI Minister statement.
12. [Tekedia — UK Regulators Launch Urgent Review](https://www.tekedia.com/uk-regulators-launch-urgent-review-of-anthropic-ai-model-claude-mythos-over-financial-system-cyber-risks/) — BoE/FCA/HMT/NCSC engagement.
13. [BusinessToday — UK regulators risk review](https://www.businesstoday.in/technology/story/anthropics-latest-ai-model-mythos-triggers-urgent-risk-review-by-uk-regulators-525315-2026-04-13) — UK regulatory coordination.
14. [The Decoder — "Claude Mythos is a wake-up call for Europe's AI safety apparatus"](https://the-decoder.com/claude-mythos-is-a-wake-up-call-for-europes-ai-safety-apparatus/) — EU exclusion analysis.
15. [GovInfoSecurity — "Europe Ponders Claude Mythos From Afar"](https://www.govinfosecurity.com/europe-ponders-claude-mythos-from-afar-a-31395) — EU AI Code of Practice context; AISI benchmark figures.
16. [NBC News — Anthropic Project Glasswing limited release](https://www.nbcnews.com/tech/security/anthropic-project-glasswing-mythos-preview-claude-gets-limited-release-rcna267234) — Mainstream corroboration.
17. [CyberScoop — US and UK cyber heavyweights on Mythos](https://cyberscoop.com/claude-mythos-ai-cybersecurity-threat-report/) — Transatlantic response framing.

## Related Reports

- [reports/ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md](../ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md) — Federal AI governance posture relevant to the US-side absence from Glasswing's public partner structure.
