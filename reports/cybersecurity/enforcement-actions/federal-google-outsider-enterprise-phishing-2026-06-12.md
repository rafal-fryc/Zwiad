---
title: "Google Sues Outsider Enterprise: First Federal Lawsuit Targeting AI-Enabled Phishing-as-a-Service Network"
date: 2026-06-12
jurisdiction: "Federal"
category: "cybersecurity"
development_type: "enforcement"
finding_id: "SCAN-20260615-055"
topic_key: "federal-f31f08d0-2026"
topic_type: "enforcement"
first_reported: 2026-06-12
last_updated: 2026-06-15
status_history: []
cluster: "Google v. Outsider Enterprise: Operation Ghost Hook AI-Enabled Phishing Lawsuit"
cluster_slug: "google-operation-ghost-hook-phishing-as-a-service-lawsuit"
---

# Google Sues Outsider Enterprise: First Federal Lawsuit Targeting AI-Enabled Phishing-as-a-Service Network

**Jurisdiction:** Federal (S.D.N.Y.) | **Category:** Cybersecurity | **Date:** June 12, 2026

## Summary [HIGH confidence]

Google filed a civil lawsuit on June 12, 2026 against a China-based phishing-as-a-service operation known as the "Outsider Enterprise" — marking the first time Google has legally pursued bad actors for misusing its Gemini AI tools. Filed in the U.S. District Court for the Southern District of New York (Case No. 1:26-cv-04982), the complaint alleges that defendants (named as Does 1–25) sold subscription-based phishing kits that leveraged Gemini to auto-generate fraudulent websites and smishing campaigns at industrial scale. The coordinated action, dubbed **Operation Ghost Hook**, simultaneously brought in the FBI, which seized core infrastructure, a Shopify storefront, and approximately $100,000 in cryptocurrency from the network's payment wallets.

## Key Facts [HIGH confidence]

- **Case docket:** *Google LLC v. Does 1-25*, No. 1:26-cv-04982 (S.D.N.Y., filed June 12, 2026), per [CourtListener](https://www.courtlistener.com/docket/73476270/google-llc-v-does-125/).
- **Legal claims:** The complaint asserts RICO/racketeering, wire fraud, trademark infringement, copyright infringement, and false advertising, according to [TechCrunch](https://techcrunch.com/2026/06/12/chinese-cybercrime-operation-that-used-ai-to-scam-hundreds-of-thousands-of-victims-sued-by-google/) and [Cybersecurity News](https://cybersecuritynews.com/google-sues-chinese-cybercrime-network/).
- **AI abuse mechanism:** Outsider Enterprise sold "phishing kits" for as low as $88/week or $200/month that instructed buyers to use Gemini to generate custom phishing landing pages mimicking trusted brands including Google, YouTube, E-ZPass, and the U.S. Postal Service, per [Help Net Security](https://www.helpnetsecurity.com/2026/06/12/google-china-based-cybercrime-network-lawsuit/).
- **Scale of harm:** Between November 2025 and April 2026, the network was linked to more than 9,000 fake websites and over 1.5 million fraudulent URLs; in a single two-week period in May 2026, it sent approximately 2.5 million smishing messages generating 55,000 spam complaints, per [9to5Google](https://9to5google.com/2026/06/12/google-sues-cybercrime-network-that-used-gemini-for-financial-scams/).
- **Cumulative losses:** The FBI estimates that since July 2023, Outsider Enterprise's platform enabled theft of at least 3.87 million credit card numbers and approximately $1.9 billion in consumer losses, per [CyberScoop](https://cyberscoop.com/outsider-cybercrime-network-takedown-china-fbi-google-lumen/).
- **Law enforcement action:** Operation Ghost Hook resulted in FBI seizure of core admin domains, thousands of domains registered through U.S. registrars, a Shopify storefront, and roughly $100,000 from Outsider payment wallets, per [Cryptopolitan](https://www.cryptopolitan.com/google-sues-chinese-ai-phishing-ring-outsider-enterprise/).
- **Carrier cooperation:** Google coordinated with AT&T, T-Mobile, and Verizon to block Outsider-linked smishing messages before delivery, per [SecurityWeek](https://www.securityweek.com/fbi-google-dismantle-outsider-enterprise-phishing-service/).
- **Official announcement:** Google published a detailed account of the operation on its safety blog: [blog.google/innovation-and-ai/technology/safety-security/combatting-ai-scams/](https://blog.google/innovation-and-ai/technology/safety-security/combatting-ai-scams/).

> **Note on official legal text:** The full complaint was filed under seal or as a restricted electronic filing in PACER; the official docket is accessible via [CourtListener](https://www.courtlistener.com/docket/73476270/google-llc-v-does-125/) but the complaint document itself could not be retrieved at time of writing. Key factual claims above are drawn from Google's official blog post and corroborated by multiple independent outlets.

## Action Items

- **Review AI acceptable-use policies:** If your organization uses Google Gemini (or any foundation model) via API or consumer accounts, audit your usage logs and acceptable-use acknowledgments. The Outsider Enterprise case establishes that abusive use of AI platforms to generate fraudulent content is actionable under RICO and trademark law — creating potential secondary liability exposure for organizations that fail to monitor misuse within their networks.
- **Assess smishing exposure:** Organizations impersonated in Outsider campaigns (financial institutions, toll agencies, logistics providers, utilities) should check whether their brand appeared in the network's known 9,000+ fraudulent domains, coordinate with Google's Safe Browsing team if needed, and issue consumer-facing alerts.
- **Coordinate with carrier fraud teams:** The Google-AT&T-T-Mobile-Verizon cooperation model demonstrates that proactive carrier-level filtering is a viable mitigation pathway. Organizations experiencing brand-impersonation smishing should formally engage carrier fraud units.
- **Watch for RICO precedent:** This is the first application of RICO to an AI-enabled phishing-as-a-service network. A favorable ruling for Google could materially expand the legal toolkit for pursuing AI-augmented cybercrime — worth tracking for litigation strategy and cyber insurance underwriting.
- **Monitor Operation Ghost Hook follow-ons:** FBI seizures do not guarantee criminal charges. Watch the DOJ press releases and the SDNY civil docket (1:26-cv-04982) for default judgments, injunctions, or criminal referrals that could produce enforceable precedent.

## Related Reports

- [Federal: Charter Communications / ShinyHunters Breach (June 2026)](../enforcement-actions/federal-charter-communications-shinyhunters-breach-2026-06-01.md) — Both reports address large-scale cybercrime enforcement actions at the federal level involving the SDNY and coordinated government response.
- [Federal: SEC / SolarWinds CISO Personal Liability (July 2024)](../enforcement-actions/federal-sec-solarwinds-ciso-personal-liability-2024-07-18.md) — Establishes the broader trend of using civil litigation (SEC enforcement, private suits) to impose accountability on cybersecurity threat actors and negligent insiders.
- [Tennessee HB 2434: Data Breach Safe Harbor (May 2024)](../tennessee-hb2434-data-breach-safe-harbor-2024-05-21.md) — Related through the intersection of cybersecurity liability frameworks; organizations impersonated in phishing campaigns may benefit from breach-response safe harbor statutes.

## Sources

1. [Google LLC v. Does 1-25, 1:26-cv-04982 — CourtListener](https://www.courtlistener.com/docket/73476270/google-llc-v-does-125/) — Official PACER docket for the civil complaint filed in S.D.N.Y.
2. [How Google is combatting AI scams and dismantling the "Outsider Enterprise" — Google Blog](https://blog.google/innovation-and-ai/technology/safety-security/combatting-ai-scams/) — Google's official account of the lawsuit and Operation Ghost Hook
3. [Chinese cybercrime operation that used AI to scam 'hundreds of thousands of victims' sued by Google — TechCrunch](https://techcrunch.com/2026/06/12/chinese-cybercrime-operation-that-used-ai-to-scam-hundreds-of-thousands-of-victims-sued-by-google/) — Detailed reporting on legal claims, scale, and FBI coordination
4. [Google sues China-based scammers over Gemini AI abuse — Help Net Security](https://www.helpnetsecurity.com/2026/06/12/google-china-based-cybercrime-network-lawsuit/) — Technical details on phishing kit mechanics and Gemini misuse
5. [Google Sues Chinese Cybercrime Network — Cybersecurity News](https://cybersecuritynews.com/google-sues-chinese-cybercrime-network/) — Summary of defendants and legal counts
6. [FBI takes down massive China-based cybercrime network that caused $1.9B in losses — CyberScoop](https://cyberscoop.com/outsider-cybercrime-network-takedown-china-fbi-google-lumen/) — FBI Operation Ghost Hook details and financial loss estimates
7. [Google sues Chinese AI phishing ring as FBI seizes domains and $100,000 in Operation Ghost Hook — Cryptopolitan](https://www.cryptopolitan.com/google-sues-chinese-ai-phishing-ring-outsider-enterprise/) — Infrastructure seizure details and Shopify storefront takedown
8. [FBI, Google Dismantle 'Outsider Enterprise' Phishing Service — SecurityWeek](https://www.securityweek.com/fbi-google-dismantle-outsider-enterprise-phishing-service/) — Carrier cooperation and infrastructure disruption details
9. [Google sues cybercrime network that used Gemini for financial scams — 9to5Google](https://9to5google.com/2026/06/12/google-sues-cybercrime-network-that-used-gemini-for-financial-scams/) — Smishing message volume and spam complaint statistics
10. [AI Scam Surge Prompts Google to File Lawsuit — PYMNTS](https://www.pymnts.com/cybersecurity/fraud-attack/2026/ai-scam-surge-prompts-google-to-file-lawsuit/) — Consumer impact framing and subscription pricing details
11. [Google Sues Chinese Smishing Network — The Hacker News](https://thehackernews.com/2026/06/google-sues-chinese-smishing-network.html) — Technical analysis of smishing delivery mechanism
12. [FBI disrupts massive AI-powered phishing service — BleepingComputer](https://www.bleepingcomputer.com/news/security/fbi-disrupts-massive-ai-powered-phishing-service-using-a-million-urls/) — URL count and FBI takedown mechanics
