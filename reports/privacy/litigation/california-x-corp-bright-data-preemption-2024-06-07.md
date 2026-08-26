---
title: "California Federal Court Holds X's Claims Against Scraper Preempted by Federal Law"
date: 2024-06-07
jurisdiction: "California"
category: "privacy"
development_type: "court-decision"
finding_id: "SCAN-20240607-016"
topic_key: "california-c2b9a7e4-2024"
topic_type: "enforcement"
topic_key_confidence: "low"
first_reported: 2024-06-07
last_updated: 2024-06-07
status_history: []
cluster: "X Corp. v. Bright Data: Web Scraping Terms-of-Service Litigation"
cluster_slug: "x-corp-bright-data-web-scraping-litigation"
---

# California Federal Court Holds X's Claims Against Scraper Preempted by Federal Law

**Jurisdiction:** California (Federal — N.D. Cal.) | **Category:** Privacy / Data Law | **Date:** May 9, 2024 (Morrison & Foerster analysis, June 4, 2024)

> **Note on Related Reports:** Two comprehensive primary analyses of *X Corp. v. Bright Data Ltd.* are already in this knowledge base. This report synthesizes the [Morrison & Foerster](https://www.mofo.com/resources/insights/240604-california-federal-court-holds-x-s-claims) and [Socially Aware Blog](https://www.sociallyawareblog.com/topics/california-federal-court-holds-x-s-claims-against-scraper-preempted-by-federal-law) perspectives and should be read alongside:
> - [reports/privacy/litigation/california-x-corp-bright-data-web-scraping-2024-05-09.md](california-x-corp-bright-data-web-scraping-2024-05-09.md) — Full background, procedural history, and extended legal analysis (SCAN-20240520-024).
> - [reports/privacy/litigation/california-x-corp-bright-data-scraping-2024-06-05.md](california-x-corp-bright-data-scraping-2024-06-05.md) — Pearl Cohen perspective and Israeli/cross-border practitioner focus (SCAN-20240605-024).

## Executive Summary [HIGH confidence]

On May 9, 2024, U.S. District Judge William Alsup of the Northern District of California issued a landmark ruling in *X Corp. v. Bright Data Ltd.*, No. C 23-03698 WHA (N.D. Cal.), granting Bright Data's motion to dismiss all of X Corp.'s claims. As [Morrison Foerster's Socially Aware Blog](https://www.sociallyawareblog.com/topics/california-federal-court-holds-x-s-claims-against-scraper-preempted-by-federal-law) analyzed, the court dismissed X's breach of contract and related state-law claims targeting Bright Data's scraping and resale of publicly available X content on copyright conflict preemption grounds, and dismissed access-based claims — trespass to chattels and California UCL violations — for failure to plead cognizable harm. The decision is the first district court ruling to apply copyright conflict preemption to extinguish a contract claim in a web-scraping dispute, establishing a powerful new structural defense for commercial data scrapers against state-law enforcement theories.

## Background [HIGH confidence]

### Parties and Case History

[X Corp.](https://x.com) (formerly Twitter) filed suit on July 26, 2023 in the N.D. Cal. against [Bright Data Ltd.](https://brightdata.com/), an Israeli commercial web-scraping infrastructure company, alleging that Bright Data scraped publicly accessible X content, circumvented X's anti-scraping technology, and sold the resulting data to third parties — all in violation of X's Terms of Service (ToS) and Developer Agreement.

The lawsuit was part of X's aggressive post-acquisition anti-scraping campaign under Elon Musk. X imposed strict API rate limits and revised its ToS to prohibit scraping, then brought litigation to enforce those restrictions.

### The CFAA Backdrop: Why X Avoided Federal Law

When X filed its complaint, Ninth Circuit precedent already made CFAA claims against public-data scrapers untenable. In [*hiQ Labs, Inc. v. LinkedIn Corp.*](https://calawyers.org/privacy-law/ninth-circuit-holds-data-scraping-is-legal-in-hiq-v-linkedin/), the Ninth Circuit held in 2019 — and reaffirmed in 2022 after the Supreme Court's *Van Buren v. United States* (2021) decision — that scraping publicly accessible data does not violate the CFAA because a website with no access restrictions imposes no "authorization" that could be exceeded. Confronting this binding precedent, X deliberately chose not to plead CFAA claims, pursuing exclusively state-law contract and tort theories. This strategic choice proved critical to the court's preemption analysis.

### The Meta v. Bright Data Parallel

One month before the *X Corp.* ruling, [Judge Chen of the same court dismissed Meta Platforms' similar lawsuit against Bright Data](https://newmedialaw.proskauer.com/2024/05/14/california-court-issues-another-noteworthy-decision-dismissing-breach-of-contract-and-tort-claims-in-web-scraping-dispute/) on contract interpretation grounds, finding that Bright Data did not "use" Facebook or Instagram within the meaning of Meta's ToS when it scraped while logged off. The *X Corp.* ruling extended further, applying copyright preemption to eliminate contract claims even where ToS might otherwise apply.

## Detailed Analysis [HIGH confidence]

### Claims Structure: Two Theories of Wrongdoing

As analyzed by [Morrison Foerster](https://www.mofo.com/resources/insights/240604-california-federal-court-holds-x-s-claims), Judge Alsup organized X's complaint into two operative groups:

**Data-based claims** (targeting scraping and resale of X's publicly posted content):
- Breach of contract — scraping violated X's ToS and Developer Agreement;
- Misappropriation — commercial exploitation of X's data assets;
- Unjust enrichment — profiting from X's platform without compensation;
- Tortious interference — inducing X users to violate their own ToS obligations.

**Access-based claims** (targeting Bright Data's server access):
- Trespass to chattels — scraping bots burdened X's server infrastructure;
- California UCL violations (Bus. & Prof. Code § 17200) — using IP proxy technology to disguise scraping activity as ordinary user traffic.

### Dismissal of Data-Based Claims: Copyright Conflict Preemption [HIGH confidence]

The court's most novel holding applied **copyright conflict preemption** under the Supremacy Clause — the doctrine that state law must yield when it stands as an obstacle to the full purposes of a federal statute. [Skadden](https://www.skadden.com/insights/publications/2024/05/district-court-adopts-broad-view) noted that while "conflict preemption has played second fiddle to express preemption in the caselaw as of late," Judge Alsup held it was "the more appropriate consideration when the question presented is not whether rights created by state law are equivalent to rights created by federal copyright law but whether enforcement of state law conflicts with federal law."

The court found X's state-law claims in irreconcilable conflict with the Copyright Act in two independent ways:

**First — Nullification of statutory fair use rights.** Under 17 U.S.C. § 107, fair use is a federally guaranteed right. Allowing X to use contract law to prohibit all copying of its platform content — regardless of whether any specific copying would qualify as fair use — would permit a private party to effectively abolish a federal statutory right for everyone who might be covered by X's ToS. The court refused to permit state-law enforcement mechanisms to accomplish that result.

**Second — Improper extension of copyright-like exclusion rights.** X is a non-exclusive licensee of most content posted to its platform (users retain their copyright; X receives only a limited license). Non-exclusive licensees have no right under the Copyright Act to exclude third parties from copying the licensed work. As [Morrison Foerster](https://www.mofo.com/resources/insights/240604-california-federal-court-holds-x-s-claims) observed, X was attempting to "entrench its own private copyright system that rivals, even conflicts with, the actual copyright system enacted by Congress" by using contract law to assert an exclusionary power the Copyright Act explicitly declines to give it. The court further noted this approach risked creating ["information monopolies that would disserve the public interest"](https://blog.ericgoldman.org/archives/2024/05/x-corp-v-bright-data-is-the-decision-weve-been-waiting-for-guest-blog-post.htm) — allowing platforms to exercise control over factual, publicly available data that may not even meet copyright's originality threshold under *Feist Publications, Inc. v. Rural Telephone Service Co.*, 499 U.S. 340 (1991).

**Doctrinal significance.** As [Skadden](https://www.skadden.com/insights/publications/2024/05/district-court-adopts-broad-view) and [Morrison Foerster](https://www.mofo.com/resources/insights/240604-california-federal-court-holds-x-s-claims) both emphasized, this was **the first district court decision to dismiss a contract claim under copyright conflict preemption** in a web-scraping context. Prior decisions applying preemption to data-scraping disputes had relied on Section 301 express preemption — a narrower doctrine applicable only when a state right is "equivalent" to a copyright right. Conflict preemption is broader: it applies whenever state-law enforcement would frustrate federal copyright objectives, even if the state right is formally different from copyright.

Claims dismissed under this holding: breach of contract (data-scraping component), misappropriation, unjust enrichment, and the tortious interference count to the extent it rested on inducing ToS violations related to data copying.

### Dismissal of Access-Based Claims: Failure to Plead Cognizable Harm [HIGH confidence]

The trespass to chattels and UCL claims were dismissed on a wholly separate ground: failure to plead actual harm.

**Trespass to chattels.** California law requires a plaintiff to allege actual dispossession of or physical damage to the chattel. Mere unauthorized access is legally insufficient. The court found X had not plausibly alleged that Bright Data's scraping caused measurable harm to its servers, noting that "sending requests to X Corp.'s servers with a scraper is [not] inherently burdensome, or inherently more burdensome than an X user sending requests to X Corp.'s servers with a browser." X's pleadings contained only conclusory references to server capacity concerns and reputational harm — insufficient to support a cognizable injury.

**UCL unfair competition (§ 17200).** The court rejected X's argument that Bright Data "deceived" X by disguising scrapers as legitimate users through IP proxy technology. The court held that there is no "affirmative duty to identify oneself with a given IP address" and that the sale of IP proxy services is not "inherently deceptive." Without a predicate fraudulent act, the UCL claim failed.

### Dismissal with Leave to Amend

The dismissal was granted **with leave to amend**, preserving the theoretical possibility that:
- A properly pled trespass-to-chattels claim with specific, quantified server-degradation evidence could survive;
- Access-based claims tied to authenticated scraping (Bright Data operating while logged into X accounts) might be cognizable under contract or the California Computer Data Access and Fraud Act (CDAFA).

### Subsequent Developments: November 2024 Ruling and March 2026 Trial [MEDIUM confidence]

X filed a second amended complaint. In [November 2024, Judge Alsup allowed a narrowed trespass-to-chattels claim to proceed](https://docs.justia.com/cases/federal/district-courts/california/candce/3:2023cv03698/415869/156), finding that X now plausibly alleged that "scrapers traverse the X service in patterns markedly different from humans or authorized machines, resulting in abnormal use of server capacity." The copyright preemption holdings were not disturbed. The case proceeded to discovery with a jury trial scheduled for March 2, 2026 before Judge Alsup in San Francisco — where X will need to prove its trespass theory to a factfinder.

## Impact Assessment [MEDIUM confidence]

### Platform Enforcement Strategies

The ruling fundamentally disrupts the ToS-based enforcement model that social media platforms have relied upon to restrict commercial data collection. As [Morrison Foerster](https://www.mofo.com/resources/insights/240604-california-federal-court-holds-x-s-claims) observed, the decision confirms that:

1. **State-law contract claims against public-data scrapers are preempted in the Ninth Circuit.** Any breach of contract, misappropriation, or unjust enrichment theory premised on copying publicly posted content faces copyright conflict preemption when brought in the Ninth Circuit.

2. **Trespass to chattels survives — but requires hard evidence.** Platforms can bring trespass claims but must document actual, measurable server load differentials between scraper traffic and ordinary user traffic. The November 2024 ruling shows this bar can be cleared with adequate pleading, but it requires forensic infrastructure.

3. **The contractual toolkit is narrowed, not eliminated.** Claims predicated on authenticated scraping (logged-in access) — or on non-copyright harms such as database misappropriation under a valid sui generis theory — may remain viable outside the preemption holding's scope.

### AI Training Data Implications

[FKKS IP & Media Law Blog](https://ipandmedialaw.fkks.com/post/102j7d0/blockbuster-ruling-federal-court-holds-that-copyright-act-preempts-xs-web-scrap) characterized the ruling as having immediate relevance to AI model developers who scrape public websites for training data. If platforms cannot use ToS to prohibit copying that would qualify as fair use — and training data collection has colorable fair use arguments — then ToS-based restrictions on AI scraping are subject to the same preemption analysis. The decision does not resolve AI training data disputes, but it weakens one of platforms' primary legal theories.

### Broader Web Scraping Landscape

The *X Corp. v. Bright Data* ruling completes a trajectory in Ninth Circuit law:

| Case | Year | Holding |
|---|---|---|
| *hiQ Labs v. LinkedIn* (9th Cir.) | 2019/2022 | CFAA does not apply to scraping publicly accessible data |
| *Van Buren v. United States* (SCOTUS) | 2021 | CFAA "exceeds authorized access" requires a technical access barrier, not just policy prohibition |
| *Meta v. Bright Data* (N.D. Cal.) | Jan. 2024 | ToS cannot bind parties who scrape while logged off and never "use" the service |
| *X Corp. v. Bright Data* (N.D. Cal.) | May 2024 | State-law contract/misappropriation claims against public-data scrapers preempted by Copyright Act |

Together, these decisions establish that public-data scraping in the Ninth Circuit is substantially insulated from CFAA, contract, and misappropriation liability. The only surviving theories are copyright infringement (for content the platform actually owns), trespass to chattels premised on documented server harm, and CDAFA/CFAA claims for authenticated access violations.

Outside the Ninth Circuit, the ruling is persuasive but not binding. Courts in the Second, Fifth, or Eleventh Circuits may apply different preemption analyses, and CFAA theories may face less restrictive interpretations.

## Action Items

- Platforms enforcing ToS-based anti-scraping policies in the Ninth Circuit should immediately evaluate exposure to copyright conflict preemption challenges; shift enforcement focus toward copyright infringement, CDAFA claims for authenticated scraping, and trespass to chattels backed by forensic server-load evidence.
- Data brokers, alternative data providers, and AI developers scraping public-facing websites should document that operations target only unauthenticated pages, and preserve server-traffic comparison data demonstrating that scraping patterns do not impose abnormal server burdens.
- Track the March 2026 jury trial outcome in *X Corp. v. Bright Data* — the jury's verdict on the trespass-to-chattels claim will be the first post-*hiQ* assessment of what quantum of server impact constitutes actionable harm.
- Companies outside the Ninth Circuit should monitor whether other circuits adopt or reject conflict preemption in the web-scraping context; no circuit court has yet ruled on this specific issue.
- AI developers relying on public-website scraping for training data should note that this decision strengthens arguments that ToS restrictions on copying are subject to fair-use-based preemption, though that issue remains unsettled.

## Related Reports

- [reports/privacy/litigation/california-x-corp-bright-data-web-scraping-2024-05-09.md](california-x-corp-bright-data-web-scraping-2024-05-09.md) — Primary comprehensive analysis of the same *X Corp. v. Bright Data* case from the initial ruling date, with full procedural history and extended legal analysis.
- [reports/privacy/litigation/california-x-corp-bright-data-scraping-2024-06-05.md](california-x-corp-bright-data-scraping-2024-06-05.md) — Pearl Cohen perspective on the same case, providing Israeli/cross-border data intelligence company focus.
- [reports/privacy/litigation/california-cipa-chat-wiretapping-garcia-v-buildcom-2024-04-17.md](california-cipa-chat-wiretapping-garcia-v-buildcom-2024-04-17.md) — Related N.D. Cal. litigation illustrating the broader pattern of California federal courts scrutinizing novel digital privacy tort theories.
- [reports/privacy/litigation/federal-dc-circuit-thaler-ai-copyright-2025-03-18.md](federal-dc-circuit-thaler-ai-copyright-2025-03-18.md) — Related AI copyright litigation; the copyright framework underlying this ruling directly intersects with emerging AI training data disputes.

## Sources

1. [Morrison Foerster — "California Federal Court Holds X's Claims Against Scraper Preempted by Federal Law" (June 4, 2024)](https://www.mofo.com/resources/insights/240604-california-federal-court-holds-x-s-claims) — Primary source for this finding; Morrison Foerster analysis of the preemption holding and its implications.
2. [Morrison Foerster / Socially Aware Blog — Same article (alternate URL)](https://www.sociallyawareblog.com/topics/california-federal-court-holds-x-s-claims-against-scraper-preempted-by-federal-law) — Morrison Foerster's Socially Aware Blog version with extended commentary on terms-of-service and AI training data implications.
3. [Skadden — "District Court Adopts Broad View of Copyright Preemption in Data Scraping Case" (May 2024)](https://www.skadden.com/insights/publications/2024/05/district-court-adopts-broad-view) — In-depth analysis of the conflict preemption holding, its novelty, and comparison to prior express preemption cases; documents this as the first contract-claim dismissal under conflict preemption.
4. [Columbia Law School / CLS Blue Sky Blog — "Skadden Discusses Court's Broad View of Copyright Preemption" (May 23, 2024)](https://clsbluesky.law.columbia.edu/2024/05/23/skadden-discusses-courts-broad-view-of-copyright-preemption-in-data-scraping-case/) — Academic repost of Skadden analysis with additional context.
5. [Proskauer Rose New Media Law Blog — "California Court Issues Another Noteworthy Decision Dismissing Breach of Contract and Tort Claims in Web Scraping Dispute" (May 14, 2024)](https://newmedialaw.proskauer.com/2024/05/14/california-court-issues-another-noteworthy-decision-dismissing-breach-of-contract-and-tort-claims-in-web-scraping-dispute/) — Analysis from Bright Data's counsel; covers both the X Corp. and Meta rulings and their joint significance.
6. [Proskauer Rose — "Proskauer Secures Dismissal of Scraping Claims Against Bright Data"](https://www.proskauer.com/release/proskauer-secures-dismissal-of-scraping-claims-against-bright-data) — Firm announcement summarizing the May 9 ruling; documents Proskauer as Bright Data's counsel.
7. [FKKS IP & Media Law Blog — "BLOCKBUSTER RULING: Federal Court Holds That Copyright Act Preempts X's Web Scraping Claims"](https://ipandmedialaw.fkks.com/post/102j7d0/blockbuster-ruling-federal-court-holds-that-copyright-act-preempts-xs-web-scrap) — Law firm commentary on AI training data implications of the ruling.
8. [Eric Goldman Technology & Marketing Law Blog — "X Corp. v. Bright Data is the Decision We've Been Waiting For" (May 2024)](https://blog.ericgoldman.org/archives/2024/05/x-corp-v-bright-data-is-the-decision-weve-been-waiting-for-guest-blog-post.htm) — Expert commentary on the "information monopolies" risk articulated by Judge Alsup and broader policy implications.
9. [CourtListener — X Corp. v. Bright Data Ltd., Docket No. 3:23-cv-03698](https://www.courtlistener.com/docket/67637345/x-corp-v-bright-data-ltd/) — Official court docket for the N.D. Cal. case including all filed documents and orders.
10. [Justia — Order Re Second Amended Complaint (Nov. 26, 2024)](https://docs.justia.com/cases/federal/district-courts/california/candce/3:2023cv03698/415869/156) — Court order allowing the narrowed trespass-to-chattels claim to proceed on X's second amended complaint.
11. [Leagle — X Corp. v. Bright Data Ltd., No. C 23-03698 WHA (May 10, 2024)](https://www.leagle.com/decision/infdco20240510c40) — Published text of the original May 9, 2024 dismissal order.
12. [California Lawyers Association — "Ninth Circuit Holds Data Scraping is Legal in hiQ v. LinkedIn"](https://calawyers.org/privacy-law/ninth-circuit-holds-data-scraping-is-legal-in-hiq-v-linkedin/) — Background on the foundational CFAA ruling that made contract/tort theories X's only viable path.
13. [Digital Policy Alert — "Issued ruling in lawsuit alleging copyright violations concerning data scraping (X Corp v Bright Data Ltd)"](https://digitalpolicyalert.org/event/19822-issued-ruling-in-lawsuit-alleging-copyright-violations-concerning-data-scrapping-x-corp-v-bright-data-ltd) — Regulatory policy tracker entry with procedural history.
