---
title: "Iowa Enacts AI Chatbot Regulations Protecting Minors (SF 2417)"
date: 2026-05-05
jurisdiction: "Iowa"
category: "ai-law"
development_type: "legislation"
finding_id: "SCAN-20260508-004"
topic_key: "IA-SF-2417-2026"
topic_type: "state_bill"
first_reported: 2026-05-05
last_updated: 2026-05-08
status_history:
  - "2026-05-08: Revised Key Facts and Summary to distinguish statutory effective date (July 1, 2026) from operator applicability/compliance date (July 1, 2027); corrected Action Items and Sources note to use accurate terminology."
  - "2026-05-08 (r2): Corrected inaccurate 'one of the first states' framing in Summary; expanded Key Facts legislative context to include California, Washington, and Oregon as predecessor states; updated Action Items to reference the full 2026 state chatbot law wave."
cluster: "State Chatbot Disclosure and AI Mental Health Practice Laws: 2026 Legislative Wave"
cluster_slug: "state-chatbot-disclosure-laws-2026"
---

# Iowa Enacts AI Chatbot Regulations Protecting Minors (SF 2417)

**Jurisdiction:** Iowa | **Category:** AI Law | **Date:** 2026-05-05

## Summary [HIGH confidence]

Iowa Governor Kim Reynolds signed [Senate File 2417](https://www.legis.iowa.gov/docs/publications/LGE/91/SF2417.pdf) on May 2, 2026, joining a growing cohort of states — including California (January 2026), Washington (March 2026), Oregon (April 2026), Maine (April 2026), and Nebraska (April 2026) — that enacted conversational AI regulations for minors in 2026. The law mandates AI disclosure, parental controls, self-harm intervention protocols, and prohibitions on presenting chatbots as licensed mental health providers. The statute carries two distinct operative dates: it takes legal effect on Iowa's books on **July 1, 2026**, while the operator compliance obligations (the applicability date) do not begin until **July 1, 2027**. Operators face civil penalties of up to $1,000 per violation with a $500,000 per-operator cap under Iowa Attorney General enforcement.

## Key Facts [HIGH confidence]

- **Signed into law:** May 2, 2026, by Governor Kim Reynolds; **statutory effective date: July 1, 2026** (the date the law enters Iowa's code); **operator compliance required by: July 1, 2027** (the separate applicability date per the enrolled text), per [Iowa Legislature enrolled text](https://www.legis.iowa.gov/docs/publications/LGE/91/SF2417.pdf) and confirmed by [LegiScan bill tracking](https://legiscan.com/IA/bill/SF2417/2025) (recording "Effective: 07/01/2026 / Applicability: 07/01/2027"). The distinction matters: AG rulemaking authority and the law's formal legal status attach from July 1, 2026, even though operators have until July 1, 2027 to achieve full compliance.
- **Unanimous passage:** The Iowa House passed SF 2417 unanimously; the Iowa Senate cleared it without any opposing votes, per [The Gazette](https://www.thegazette.com/news/state/bill-restricting-ai-chatbots-goes-to-iowa-governor/article_3926f04e-ed32-41c1-b21c-0115973d32ac.html).
- **Covered services:** A "conversational AI service" is defined as AI software accessible to the general public with the primary purpose of simulating human conversation. The definition explicitly excludes: business-to-customer customer service bots, voice command/virtual assistant interfaces for consumer devices, and AI used solely for internal business purposes, per the [enrolled bill text](https://www.legis.iowa.gov/docs/publications/LGE/91/SF2417.pdf).
- **Disclosure requirement:** Operators must display a persistent, visible disclaimer at the beginning of each interaction with a minor and at least once every three hours of continuous interaction, per [Government Technology](https://www.govtech.com/artificial-intelligence/iowa-bill-restricting-ai-chatbots-heads-to-governors-desk).
- **Parental controls:** For users under age 13, operators must allow parents or guardians to control privacy and account settings, per [Troutman Pepper analysis](https://www.troutmanprivacy.com/2026/04/proposed-state-ai-law-update-april-20-2026/).
- **Content restrictions:** Operators may not program AI to generate sexually explicit content, make sexualized statements, or simulate adult-minor romantic interactions involving a minor, per the [enrolled bill text](https://www.legis.iowa.gov/docs/publications/LGE/91/SF2417.pdf).
- **Anti-manipulation:** Operators are prohibited from awarding points or similar rewards at unpredictable intervals to minors with the intent of encouraging increased engagement — a direct anti-addiction measure, per [legiscan.com bill tracking](https://legiscan.com/IA/bill/SF2417/2025).
- **Self-harm protocols:** Operators must adopt protocols responding to user prompts regarding suicidal ideation or self-harm, including making reasonable efforts to refer users to crisis service providers such as suicide hotlines or crisis text lines, per the [enrolled bill text](https://www.legis.iowa.gov/docs/publications/LGE/91/SF2417.pdf).
- **Mental health prohibition:** An operator shall not knowingly cause or program a conversational AI service to represent or imply that it is designed to provide professional psychology or behavioral health services, per the [enrolled bill text](https://www.legis.iowa.gov/docs/publications/LGE/91/SF2417.pdf).
- **Civil penalties:** $1,000 per violation, up to $500,000 per operator maximum; the Iowa Attorney General has exclusive enforcement authority and rulemaking power under Iowa Code chapter 17A, per [legiscan.com](https://legiscan.com/IA/bill/SF2417/2025).
- **No private right of action:** Enforcement is vested solely in the Attorney General; the statute does not create a private cause of action, per [SF 2417 bill text analysis](https://www.legis.iowa.gov/docs/publications/LGE/91/SF2417.pdf).
- **State AI legislative context:** Iowa's enactment follows a 2026 wave of state chatbot laws beginning with California (January 2026), Washington (March 2026), Oregon (April 2026), Maine (April 2026), and Nebraska (April 2026), and parallels pending federal legislation including the CHATBOT Act (S.4407) and the GUARD Act (S.3062), per [Troutman Pepper state AI update](https://www.troutmanprivacy.com/2026/04/proposed-state-ai-law-update-april-20-2026/).

## Action Items

- **Map your product portfolio (now):** Determine whether any consumer-facing AI products qualify as a "conversational AI service" under the Iowa definition — the public accessibility and primary-purpose-of-conversation tests are the threshold inquiries. Internal tools, narrow-topic customer service bots, and voice assistants are excluded.
- **Implement age-detection mechanisms (by July 1, 2027):** The disclosure and parental control requirements turn on whether a user is a "minor account holder." Develop or enhance age-verification or age-estimation processes to identify users under 18 (and specifically under 13 for parental control requirements).
- **Build disclosure into the UX (by July 1, 2027):** Engineer persistent, visible AI-identity disclaimers that appear at session start and reset every three hours of continuous interaction. Document that disclaimer placement satisfies the "conspicuous" standard.
- **Audit content filtering (by July 1, 2027):** Review content moderation systems to confirm that AI outputs cannot generate sexually explicit content, sexualized statements, or romantic simulations involving minors.
- **Remove reward/gamification features for minors (by July 1, 2027):** Audit any points, badges, streaks, or unpredictable-interval reward systems and either remove them for minor users or redesign so they do not function as variable-ratio reinforcement schedules.
- **Deploy crisis protocols (by July 1, 2027):** Establish documented self-harm and suicidal ideation detection and referral protocols. Referral to at least one recognized crisis resource (988 Suicide & Crisis Lifeline, Crisis Text Line) should be the minimum standard.
- **Remove mental-health-provider framing (immediately):** Review all marketing copy, in-product messaging, and AI persona configurations to ensure the service is not presented as a psychology, counseling, or behavioral health provider.
- **Monitor AG rulemaking (starting July 1, 2026):** The Iowa Attorney General's rulemaking authority under chapter 17A is active from the statutory effective date of July 1, 2026 — not July 1, 2027. Monitor the AG's docket beginning mid-2026 for rules that may define key terms or expand compliance obligations ahead of the July 1, 2027 applicability date.
- **Track parallel state legislation:** Iowa joins California, Washington, Oregon, Maine, and Nebraska in enacting chatbot-specific minor-protection laws in 2026. A multi-state compliance framework is advisable given the divergent enforcement models (AG-only in Iowa and Nebraska; private right of action in Oregon) and varying compliance deadlines across jurisdictions.

## Related Reports

- [reports/ai-law/state-legislation/nebraska-maine-ai-chatbot-health-enacted-2026-04-22.md](../state-legislation/nebraska-maine-ai-chatbot-health-enacted-2026-04-22.md) — Nebraska's LB 525 and Maine's LD 2082, enacted weeks earlier, impose overlapping chatbot disclosure and AI mental health practice restrictions, forming part of the same 2026 state legislative wave.
- [reports/ai-law/chatbots/federal-chatbot-act-s4407-children-ai-2026-04-29.md](federal-chatbot-act-s4407-children-ai-2026-04-29.md) — The federal CHATBOT Act (S.4407) would require family account controls for children's AI chatbot use, directly paralleling Iowa SF 2417's parental control mandates for users under 13.
- [reports/ai-law/chatbots/federal-guard-act-s3062-minors-2026-05-01.md](federal-guard-act-s3062-minors-2026-05-01.md) — The GUARD Act (S.3062), unanimously advanced by the Senate Judiciary Committee, would ban AI companion services for minors at the federal level — complementing Iowa's disclosure and content-restriction approach.
- [reports/ai-law/oregon-ai-companion-chatbot-sb1546-2026-04-07.md](../oregon-ai-companion-chatbot-sb1546-2026-04-07.md) — Oregon SB 1546 enacted AI companion chatbot safety requirements including a private right of action; contrasts with Iowa's AG-only enforcement model.
- [reports/ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md](../trump-ai-executive-order-state-preemption-2026-04-12.md) — The Trump AI Executive Order established a national AI policy framework with preemption implications for state AI laws; Iowa SF 2417 may face federal preemption scrutiny given DOJ's active AI litigation posture.

## Sources

1. [Iowa Senate File 2417 — Enrolled Text (Iowa Legislature)](https://www.legis.iowa.gov/docs/publications/LGE/91/SF2417.pdf) — Official enrolled statute text; primary source for definitions, requirements, penalties, statutory effective date (July 1, 2026), and applicability date (July 1, 2027).
2. [Iowa Senate File 2417 — Introduced Text (Iowa Legislature)](https://www.legis.iowa.gov/docs/publications/LGI/91/SF2417.pdf) — Introduced version for legislative history comparison.
3. [Iowa Bill Restricting AI Chatbots Heads to Governor's Desk (Government Technology)](https://www.govtech.com/artificial-intelligence/iowa-bill-restricting-ai-chatbots-heads-to-governors-desk) — Pre-signature coverage with disclosure requirement details.
4. [Bill Restricting AI Chatbots Goes to Iowa Governor (The Gazette)](https://www.thegazette.com/news/state/bill-restricting-ai-chatbots-goes-to-iowa-governor/article_3926f04e-ed32-41c1-b21c-0115973d32ac.html) — Legislative history; confirms unanimous passage in both chambers.
5. [Iowa Sets New Standards for AI: Governor Signs SF 2417 (Dubuque In Pursuit News)](https://dubuqueinpursuitnews.com/2026/05/03/iowa-sets-new-standards-for-ai-governor-signs-sf-2417-into-law/) — Post-signature reporting confirming May 2, 2026 signing date.
6. [Iowa Governor Signs Chatbots Bill (Privacy Daily)](https://privacy-daily.com/article/2026/05/05/iowa-governor-signs-chatbots-bill-2605050045?BC=bc_69fb165e75f9f) — IAPP Daily Dashboard coverage confirming key provisions.
7. [Iowa SF2417 — 91st General Assembly (LegiScan)](https://legiscan.com/IA/bill/SF2417/2025) — Legislative tracking; records "Effective: 07/01/2026 / Applicability: 07/01/2027" and civil penalty cap details ($500,000 per operator).
8. [Proposed State AI Law Update: April 20, 2026 (Troutman Pepper)](https://www.troutmanprivacy.com/2026/04/proposed-state-ai-law-update-april-20-2026/) — Law firm analysis of pre-enactment bill; parental controls and compliance framing; reference point for predecessor state chatbot laws.
9. [SF 2417 — Iowa (AI Policy Map)](https://www.aipolicymap.com/ai-bills/2593872) — Regulatory tracking aggregator with bill status and summary.
10. [AI Safeguards for Minors Bill Awaits Governor's Signature (Iowa Public Radio)](https://www.iowapublicradio.org/state-government-news/2026-04-16/ai-safeguards-for-minors-bill-awaits-governors-signature) — Pre-signature legislative context and background on self-harm impetus.
