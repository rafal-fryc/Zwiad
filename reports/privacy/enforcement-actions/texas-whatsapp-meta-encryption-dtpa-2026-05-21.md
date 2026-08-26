---
title: "Texas AG Sues WhatsApp and Meta Over Encrypted Messaging Deception Under DTPA"
date: 2026-05-21
jurisdiction: "Texas"
category: "privacy"
development_type: "enforcement"
finding_id: "SCAN-20260601-023"
topic_key: "TXAG-WHATSAPP-AND-META-2026"
topic_type: "enforcement"
first_reported: 2026-05-22
last_updated: 2026-06-01
status_history: []
cluster: "Texas AG v. Meta/WhatsApp: DTPA Encrypted Messaging Enforcement"
cluster_slug: "texas-ag-meta-whatsapp-dtpa-encryption-enforcement"
---

# Texas AG Sues WhatsApp and Meta Over Encrypted Messaging Deception Under DTPA

**Jurisdiction:** Texas | **Category:** Privacy — Enforcement Actions | **Date:** May 21, 2026

## Summary [HIGH confidence]

Texas Attorney General Ken Paxton filed suit on May 21, 2026 against Meta Platforms, Inc. and WhatsApp LLC in a Harrison County district court, alleging that the companies violated the [Texas Deceptive Trade Practices Act (DTPA)](https://statutes.capitol.texas.gov/SOTWDocs/BC/htm/BC.17.htm) by falsely marketing WhatsApp as end-to-end encrypted while maintaining an internal system that allowed employees and contractors to access users' private message content on demand. The lawsuit, if successful, could expose Meta to $10,000 fines per DTPA violation and injunctive relief barring unauthorized message access. The action arrives weeks after a federal Commerce Department investigator closed a parallel probe that had concluded Meta stores and can view WhatsApp messages — a finding that Paxton's complaint now weaponizes at the state level.

## Key Facts [HIGH confidence]

- **Filing date and forum:** The petition was filed May 21, 2026, in the 71st Judicial District Court of Harrison County, Texas, against Meta Platforms, Inc. and WhatsApp LLC, as confirmed by the [Texas AG press release](https://www.texasattorneygeneral.gov/news/releases/attorney-general-paxton-files-landmark-lawsuit-against-meta-and-whatsapp-lying-about-privacy) and the [court petition PDF](https://www.texasattorneygeneral.gov/sites/default/files/images/press/WhatsApp%20Petition.pdf).

- **Core allegation — the internal "task" system:** The petition alleges Meta operated a tiered internal "task" system through which employees and contractors could submit requests to access the content of WhatsApp messages. Requests were allegedly sometimes processed without meaningful scrutiny, according to [Bloomberg Law](https://news.bloomberglaw.com/litigation/meta-whatsapp-sued-over-privacy-protections-by-texas) and the [Texas Tribune](https://www.texastribune.org/2026/05/21/texas-whatsapp-meta-privacy-encryption-lawsuit/).

- **Contested marketing claim:** WhatsApp publicly assures users that messages are protected by end-to-end encryption and that "not even WhatsApp" can read private communications. The company's [Privacy Policy](https://www.whatsapp.com/legal/privacy-policy) states messages are encrypted to protect against access by the company and third parties. Paxton argues this representation is materially false given the internal access mechanism.

- **Federal investigation backdrop:** A Commerce Department investigator with the Office of Export Enforcement spent ten months gathering documents and conducting interviews before concluding: "There is no limit to the type of WhatsApp message that can be viewed by Meta." The investigator also stated the misconduct "involve[s] civil and criminal violations that span several federal jurisdictions." The probe was abruptly closed after the investigator sought to coordinate findings with other federal agencies, per [Bloomberg](https://www.bloomberg.com/news/articles/2026-04-28/us-ends-investigation-into-claims-whatsapp-chats-aren-t-private) and [Gizmodo](https://gizmodo.com/trump-admin-closes-investigation-into-alleged-backdoor-for-whatsapp-report-2000751760).

- **Relief sought:** The state is requesting a permanent injunction barring Meta from accessing Texans' messages without consent, civil penalties of up to **$10,000 per DTPA violation**, attorneys' fees, and other consumer protection remedies, per [KSAT](https://www.ksat.com/news/texas/2026/05/21/whatsapp-meta-can-access-texans-private-messages-ag-ken-paxton-says-in-lawsuit/) and [Route Fifty](https://www.route-fifty.com/management/2026/05/whatsapp-meta-can-access-texans-private-messages-ag-ken-paxton-claims-lawsuit/413723/).

- **Meta's denial:** Meta spokesperson Rachel Holland stated: "WhatsApp cannot access people's encrypted communications and any suggestion to the contrary is false." Meta maintains that WhatsApp uses the Signal Protocol, where message encryption keys never leave users' devices and are never accessible to the company.

- **Parallel class action:** A separate federal class action — *Dawson et al. v. Meta Platforms, Inc. et al.* — was filed in the U.S. District Court for the Northern District of California in January 2026 raising substantively similar allegations based on whistleblower disclosures about internal employee access to message content. No settlement has been reached; the case remains in early stages, per [classaction.org](https://www.classaction.org/blog/despite-privacy-promises-meta-third-parties-read-and-store-whatsapp-messages-class-action-lawsuit-alleges).

- **Scale of alleged harm:** The Texas Tribune and Tech Times report the complaint frames the deception as affecting 3.3 billion global WhatsApp users, with millions of Texas residents among them, per [TechTimes](https://www.techtimes.com/articles/317065/20260523/whatsapp-encryption-claims-under-fire-texas-sues-meta-saying-33-billion-users-were-misled.htm).

## Legal Analysis [MEDIUM confidence]

**DTPA Framework.** The Texas Deceptive Trade Practices-Consumer Protection Act, Tex. Bus. & Com. Code § 17.01 et seq., prohibits false, misleading, or deceptive acts or practices in the conduct of any trade or commerce. The state can seek civil penalties up to $10,000 per violation and may request injunctions, consumer restitution, and attorneys' fees. Penalties escalate to $250,000 per violation when the deception targeted consumers aged 65 or older.

**Theory of Liability.** Paxton's theory is straightforward: WhatsApp's encryption marketing — specifically the "not even WhatsApp can read your messages" representation — constitutes a material misrepresentation to consumers who chose the platform based on that privacy promise. If Meta maintained an operational capability to access decrypted message content regardless of the Signal Protocol's cryptographic guarantees in transit, the marketing claim was false at the point of sale. A law firm analysis by [Shumaker, Loop & Kendrick (via JDSupra)](https://www.jdsupra.com/legalnews/client-alert-texas-v-meta-and-whatsapp-2979500/) notes that neither the complaint nor Meta disputes the underlying Signal Protocol; the dispute is whether Meta built a separate capability layered on top of or around that protocol that defeated the privacy promise in practice.

**Precedent from Prior Texas-Meta Litigation.** Paxton previously sued Meta in February 2022 under the Texas Capture or Use of Biometric Identifier Act (CUBI) and the DTPA over Facebook's "tag suggestions" facial recognition feature. That case settled in July 2024 for [$1.4 billion — the largest settlement ever obtained by a single state](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-secures-14-billion-settlement-meta-over-its-unauthorized-capture) — demonstrating Paxton's willingness to litigate tech-privacy cases to resolution and Meta's exposure to substantial state-level liability.

**Business-Context Carveout.** WhatsApp's own Privacy Policy acknowledges a nuance: when users message businesses on WhatsApp, the content may be visible to the business and to third-party service providers (potentially including Meta) acting on behalf of those businesses. Whether the complaint distinguishes consumer-to-consumer from business-to-consumer messaging is not yet clear from public filings.

## Why It Matters [HIGH confidence]

**Encryption marketing as consumer protection liability.** This is one of the first state enforcement actions to treat an encryption marketing claim as actionable consumer fraud rather than merely a technical or security disclosure issue. If Texas prevails, companies making absolute privacy representations — "we can never read your messages" — will need to ensure those claims are operationally accurate end-to-end, not just cryptographically accurate in transit.

**Abandoned federal probe becomes state ammunition.** The Trump administration's Commerce Department closed its own investigation into the same underlying conduct. That closure did not end the legal risk; it created an evidentiary record that Paxton is now leveraging. State enforcement is increasingly serving as the backstop when federal agencies stand down, a pattern documented in [Bloomberg Law's 2026 enforcement tracker](https://news.bloomberglaw.com/legal-exchange-insights-and-commentary/california-texas-are-leading-2026-privacy-enforcement-efforts) and [WilmerHale's 2026 State AG Enforcement outlook](https://www.wilmerhale.com/en/insights/client-alerts/20260109-state-ag-enforcement-action-priorities-for-2026).

**Coordinated multi-front exposure.** Meta now faces the Texas AG action, the federal *Dawson* class action in California, and continued reputational scrutiny from the Commerce Department investigator's published conclusions. Each proceeding can amplify the others through discovery and public record.

**Scale of potential penalties.** With millions of Texas WhatsApp users, even a modest per-violation count could produce a penalty figure that rivals or exceeds the $1.4 billion biometric settlement. The DTPA's $10,000-per-violation cap applies per deceptive act — courts have found each individual consumer transaction can be a separate violation in analogous cases.

## Action Items

- **Platform operators making encryption or privacy-by-design marketing claims** should immediately audit whether those claims are operationally accurate — not just technically accurate at the protocol level. If internal tools, moderation pipelines, or contractor access mechanisms can reach plaintext message content, claims of absolute end-to-end encryption are legally vulnerable under DTPA-style consumer protection theories.

- **Legal and compliance teams** should review all public-facing privacy disclosures — website copy, app store listings, help center articles, and terms of service — for unqualified encryption or "no-access" claims and add operational carveouts or caveats where internal access mechanisms exist.

- **Businesses using WhatsApp for customer communications** should note that WhatsApp's own Privacy Policy already acknowledges third-party access in the business-messaging context. This may create disclosure obligations under applicable state privacy laws.

- **Privacy counsel** should monitor the *State of Texas v. Meta Platforms, Inc. et al.* docket in the 71st District Court of Harrison County for any preliminary injunction proceedings, Meta's responsive pleadings, and the state's discovery demands — each will clarify the legal theory's viability and scope.

- **Monitor the *Dawson* class action** in N.D. Cal. for discovery that may surface internal Meta documents relevant to the task-access system. Findings in the federal case could accelerate Texas proceedings.

## Related Reports

- [Texas AG Opens Privacy Investigation into Meta AI Smart Glasses](/home/rafal/projecty/Zwiad/reports/privacy/enforcement-actions/texas-meta-glasses-biometric-investigation-2026-05-21.md) — Concurrent Texas AG action against Meta on a separate privacy theory (facial recognition via smart glasses), illustrating Paxton's sustained multi-front strategy against Meta.
- [Meta Settles Texas Biometric Data Lawsuit for Record $1.4 Billion Under CUBI](/home/rafal/projecty/Zwiad/reports/privacy/enforcement-actions/texas-meta-biometric-cubi-settlement-2024-07-30.md) — The 2024 precedent settlement that established Paxton's track record against Meta and demonstrated the DTPA's financial teeth.
- [Texas AG: Allstate and Arity TDPSA Enforcement](/home/rafal/projecty/Zwiad/reports/privacy/enforcement-actions/texas-allstate-arity-tdpsa-enforcement-2026-04-14.md) — Shows the Texas AG's broader pattern of aggressive state-level privacy enforcement using consumer protection statutes.
- [Massachusetts SJC: Meta and Minors](/home/rafal/projecty/Zwiad/reports/privacy/enforcement-actions/massachusetts-sjc-meta-minors-2026-04-13.md) — Parallel state-level enforcement action against Meta by another state AG, reinforcing the multi-state enforcement trend.

## Sources

1. [Texas AG Press Release: Attorney General Paxton Files Landmark Lawsuit Against Meta and WhatsApp](https://www.texasattorneygeneral.gov/news/releases/attorney-general-paxton-files-landmark-lawsuit-against-meta-and-whatsapp-lying-about-privacy) — Official Texas OAG announcement; primary source for filing date, forum, and core allegations.
2. [State of Texas v. Meta Platforms, Inc. — Original Petition (PDF)](https://www.texasattorneygeneral.gov/sites/default/files/images/press/WhatsApp%20Petition.pdf) — Official court petition filed in 71st District Court, Harrison County.
3. [Texas Deceptive Trade Practices Act, Tex. Bus. & Com. Code § 17.01 et seq.](https://statutes.capitol.texas.gov/SOTWDocs/BC/htm/BC.17.htm) — Full statutory text of the DTPA, the legal basis for the suit.
4. [Texas Tribune: Texas sues WhatsApp, Meta over alleged privacy violations (May 21, 2026)](https://www.texastribune.org/2026/05/21/texas-whatsapp-meta-privacy-encryption-lawsuit/) — Detailed reporting on the filing, core allegations, and Meta's response.
5. [Bloomberg Law: Meta, WhatsApp Sued by Texas Over Secure Message Protections](https://news.bloomberglaw.com/litigation/meta-whatsapp-sued-over-privacy-protections-by-texas) — Legal press reporting on the Harrison County filing and allegations.
6. [Bloomberg: US Closes Probe Into Claims Meta Can Access Encrypted WhatsApp Messages (April 28, 2026)](https://www.bloomberg.com/news/articles/2026-04-28/us-ends-investigation-into-claims-whatsapp-chats-aren-t-private) — Reports the Commerce Department's abrupt closure of its WhatsApp investigation and the investigator's memo.
7. [Bloomberg: US Has Investigated Claims That WhatsApp Chats Aren't Private (January 29, 2026)](https://www.bloomberg.com/news/articles/2026-01-29/us-has-investigated-claims-that-whatsapp-chats-aren-t-private) — Original Bloomberg report revealing the Commerce Department investigation.
8. [Gizmodo: Trump Admin Closes Investigation Into Alleged Backdoor for WhatsApp](https://gizmodo.com/trump-admin-closes-investigation-into-alleged-backdoor-for-whatsapp-report-2000751760) — Secondary coverage of the federal probe closure.
9. [KSAT: WhatsApp, Meta can access Texans' private messages, AG Ken Paxton says in lawsuit](https://www.ksat.com/news/texas/2026/05/21/whatsapp-meta-can-access-texans-private-messages-ag-ken-paxton-says-in-lawsuit/) — Local Texas reporting on relief sought and key allegations.
10. [Route Fifty: WhatsApp, Meta Can Access Texans' Private Messages, AG Ken Paxton Claims in Lawsuit](https://www.route-fifty.com/management/2026/05/whatsapp-meta-can-access-texans-private-messages-ag-ken-paxton-claims-lawsuit/413723/) — Coverage of relief sought including $10,000 per violation.
11. [TechTimes: WhatsApp Encryption Claims Under Fire: Texas Sues Meta, Saying 3.3 Billion Users Were Misled](https://www.techtimes.com/articles/317065/20260523/whatsapp-encryption-claims-under-fire-texas-sues-meta-saying-33-billion-users-were-misled.htm) — Scale-of-harm framing and global user count context.
12. [Shumaker, Loop & Kendrick via JDSupra: Texas v. Meta and WhatsApp — A New Front in the Battle Over Encryption, Privacy Marketing, and Consumer Protection](https://www.jdsupra.com/legalnews/client-alert-texas-v-meta-and-whatsapp-2979500/) — Law firm analysis of the DTPA theory and its distinction between cryptographic protocol and operational access.
13. [classaction.org: Despite Privacy Promises, Meta, Third Parties Read and Store WhatsApp Messages, Class Action Lawsuit Alleges](https://www.classaction.org/blog/despite-privacy-promises-meta-third-parties-read-and-store-whatsapp-messages-class-action-lawsuit-alleges) — Details on the parallel federal class action in N.D. California (*Dawson et al.*).
14. [Texas AG: Attorney General Paxton Secures $1.4 Billion Settlement with Meta Over Biometric Data](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-secures-14-billion-settlement-meta-over-its-unauthorized-capture) — Official release on the 2024 CUBI/DTPA biometric settlement establishing Paxton's track record.
15. [Texas Tribune: Meta to pay Texas $1.4 billion for using facial recognition technology without users' permission (July 30, 2024)](https://www.texastribune.org/2024/07/30/texas-meta-facebook-biometric-data-settlement/) — Settlement details and context on the prior Texas-Meta litigation.
16. [WhatsApp Privacy Policy](https://www.whatsapp.com/legal/privacy-policy) — Official WhatsApp privacy disclosures, including encryption representations and business-messaging carveouts.
17. [WilmerHale: State AG Enforcement Action Priorities for 2026](https://www.wilmerhale.com/en/insights/client-alerts/20260109-state-ag-enforcement-action-priorities-for-2026) — Context on state AG enforcement trends and California/Texas leadership in privacy enforcement.
18. [Bloomberg Law: California, Texas Lead 2026 Privacy Enforcement Efforts](https://news.bloomberglaw.com/legal-exchange-insights-and-commentary/california-texas-are-leading-2026-privacy-enforcement-efforts) — 2026 enforcement landscape analysis.
19. [Courthouse News Service: Texas Accuses WhatsApp of Lying About Message Privacy](https://www.courthousenews.com/texas-accuses-whatsapp-of-lying-about-message-privacy/) — Court reporter coverage of the filing.
20. [Security Boulevard: Conflicting Messages on Messages: TX AG Sues Meta About WhatsApp Encryption Claims](https://securityboulevard.com/2026/05/conflicting-messages-on-messages-tx-ag-sues-meta-about-whatsapp-encryption-claims/) — Cybersecurity-focused analysis of the encryption technical claims.
