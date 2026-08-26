---
title: "N.D. Cal. Dismisses X Corp.'s Breach of Contract and Tort Claims Against Bright Data in Landmark Web Scraping Ruling"
date: 2024-05-09
jurisdiction: "California"
category: "privacy"
development_type: "court-decision"
finding_id: "SCAN-20240520-024"
topic_key: "california-X-corp-web-scraping-2024"
topic_type: "enforcement"
topic_key_confidence: "medium"
first_reported: 2024-05-20
last_updated: 2024-05-20
status_history: []
cluster: "X Corp. v. Bright Data: Web Scraping Terms-of-Service Litigation"
cluster_slug: "x-corp-bright-data-web-scraping-litigation"
---

# N.D. Cal. Dismisses X Corp.'s Breach of Contract and Tort Claims Against Bright Data in Landmark Web Scraping Ruling

**Jurisdiction:** California (Federal — N.D. Cal.) | **Category:** Privacy / Data Law | **Date:** May 9, 2024

## Executive Summary [HIGH confidence]

On May 9, 2024, U.S. District Judge William Alsup of the Northern District of California dismissed, with leave to amend, all claims brought by X Corp. (formerly Twitter) against Bright Data Ltd., an Israeli data-intelligence company, in *X Corp. v. Bright Data Ltd.*, No. C 23-03698 WHA (N.D. Cal.). The court held that X's state-law breach of contract and tort claims were preempted by the federal Copyright Act to the extent they targeted Bright Data's scraping and resale of publicly available X content, and that X had failed to plead cognizable server-damage sufficient to support access-based claims such as trespass to chattels. The decision is widely regarded as the first district court ruling to apply copyright conflict preemption to dismiss a contract claim in a data-scraping dispute, significantly narrowing the toolkit available to online platforms seeking to use terms-of-service restrictions to block commercial data collection. Following a November 2024 ruling on a second amended complaint, a trespass-to-chattels claim premised on abnormal server load from bot traffic was allowed to proceed, and the case is set for jury trial in March 2026.

## Background [HIGH confidence]

### The Parties and the Lawsuit

X Corp. is the operator of the X (formerly Twitter) social media platform. [Bright Data Ltd.](https://brightdata.com/) is an Israeli company that provides commercial web-scraping infrastructure — proxy networks, data collection APIs, and pre-scraped datasets — to enterprise customers. X filed suit against Bright Data in the N.D. Cal. on July 26, 2023, alleging that Bright Data both scraped publicly accessible X content without authorization and circumvented X's technical anti-scraping measures to enable its customers to do the same.

The case is one of several aggressive legal actions by X against data scrapers following Elon Musk's acquisition of the company in late 2022 and the subsequent imposition of strict API rate limits and Terms of Service updates designed to limit automated access. A parallel action, *X Corp. v. Center for Countering Digital Hate* (N.D. Cal., No. 23-cv-03836), was dismissed in March 2024 on anti-SLAPP grounds after the court found that CCDH's research activities constituted protected First Amendment expression — a separate but contextually related defeat for X's anti-scraping campaign.

### The CFAA and Web Scraping: The hiQ v. LinkedIn Backdrop

The legal framework governing web scraping in the Ninth Circuit was substantially shaped by [*hiQ Labs, Inc. v. LinkedIn Corp.*](https://calawyers.org/privacy-law/ninth-circuit-holds-data-scraping-is-legal-in-hiq-v-linkedin/). In 2019, the Ninth Circuit held that scraping publicly accessible data from LinkedIn's platform did not violate the Computer Fraud and Abuse Act (CFAA) because the CFAA's prohibition on access "without authorization" cannot apply where a website imposes no authorization requirement — i.e., where access to the data requires no login. The Ninth Circuit reaffirmed this position on remand after the Supreme Court's decision in *Van Buren v. United States* (2021), which narrowed the CFAA by holding that users with legitimate access to a system do not violate the statute merely by misusing that access. Together, *hiQ* and *Van Buren* established that the CFAA is generally unavailable against scrapers of public-facing websites.

The *hiQ* dispute ended in a private settlement around December 2022, with hiQ agreeing to a permanent injunction, but the Ninth Circuit's CFAA analysis — that there are simply no "gates" to open or close on a public website — has remained controlling. Confronting this precedent, X Corp. deliberately chose *not* to bring CFAA claims in *X Corp. v. Bright Data*. Instead, X pursued an exclusively contract- and tort-based strategy, which set the stage for Judge Alsup's copyright preemption ruling.

### Meta v. Bright Data: An Immediately Preceding Decision

One month before the May 2024 ruling in *X Corp. v. Bright Data*, a different N.D. Cal. judge dismissed Meta Platforms' similar lawsuit against Bright Data ([*Meta Platforms, Inc. v. Bright Data Ltd.*, No. 3:23-cv-00077-EMC](https://www.mofo.com/resources/insights/240604-california-federal-court-holds-x-s-claims)). Judge Chen ruled in January 2024 that Bright Data could only be bound by Meta's terms of service to the extent it scraped while authenticated (i.e., logged in), and that the unauthenticated scraping of public data could not give rise to breach of contract liability because Bright Data had never agreed to Meta's ToS in that context. The *Meta* ruling reinforced the principle that terms-of-service restrictions are difficult to enforce against scrapers who never accept those terms.

## Detailed Analysis [HIGH confidence]

### X's Claims: Two Categories of Alleged Wrongdoing

Judge Alsup organized X's complaint into [two operative grievances](https://www.skadden.com/insights/publications/2024/05/district-court-adopts-broad-view):

1. **Access-based claims**: Bright Data allegedly entered X's technological infrastructure without authorization, circumventing anti-scraping controls and using X's servers beyond the scope of any license.
2. **Data-based claims**: Bright Data allegedly scraped, packaged, and resold X's publicly available content for profit, thereby misappropriating X's data assets.

Specific counts included: breach of contract, tortious interference with contract, unjust enrichment, misappropriation, trespass to chattels, and violations of California's Unfair Competition Law (UCL), California Business and Professions Code § 17200. X notably did not assert a claim under the CFAA or the California Computer Data Access and Fraud Act (CDAFA), apparently conceding the weakness of those theories post-*hiQ*.

### Dismissal of Data-Based Claims: Copyright Conflict Preemption

The court's most consequential holding concerned the data-based claims — specifically, whether a platform can use state-law contract or tort theories to prohibit the scraping and resale of its publicly posted content.

Judge Alsup applied the doctrine of **conflict preemption** under the Supremacy Clause, holding that X's state-law claims impermissibly conflicted with the federal Copyright Act in two ways:

**First**, enforcing X's terms of service to prohibit Bright Data from copying and reselling X content would prevent Bright Data and its customers from exercising statutory fair use rights under 17 U.S.C. § 107. Fair use is a federally guaranteed right, and state-law enforcement mechanisms cannot be used to nullify it.

**Second**, permitting X to assert proprietary rights over platform content through contract law would effectively grant X de facto copyright protection over material that may not qualify for copyright at all — such as short user-generated comments or factual posts that fail the originality threshold. The court observed that allowing this would [risk "the possible creation of information monopolies that would disserve the public interest."](https://blog.ericgoldman.org/archives/2024/05/x-corp-v-bright-data-is-the-decision-weve-been-waiting-for-guest-blog-post.htm)

Legal commentators, including [Skadden](https://www.skadden.com/insights/publications/2024/05/district-court-adopts-broad-view) and [Morrison Foerster](https://www.mofo.com/resources/insights/240604-california-federal-court-holds-x-s-claims), noted that this was the **first time a district court had applied the conflict preemption test to dismiss a contract claim** in a data-scraping case — a significant extension of conflict preemption doctrine beyond its prior use in copyright contexts.

Dismissed on this basis: breach of contract (data-scraping component), misappropriation, and unjust enrichment.

### Dismissal of Access-Based Claims: Failure to Plead Harm

The trespass to chattels, UCL, and tortious interference claims premised on Bright Data's allegedly unauthorized access to X's servers were dismissed on a distinct ground: failure to adequately allege damage. Under California law, trespass to chattels requires that the plaintiff plead actual dispossession of or damage to the chattel — mere unauthorized access is insufficient. The court found that X's complaint did not plausibly allege that Bright Data's scraping activity caused measurable harm to X's server infrastructure or business operations. Without that pleading, the access-based claims were legally deficient regardless of any preemption analysis.

### Leave to Amend: What Survived

The dismissal was granted **with leave to amend**, meaning X could attempt to cure the deficiencies. Significantly, Judge Alsup left open the possibility that:
- A properly pled trespass to chattels claim — showing actual, quantifiable server damage or degradation — could survive.
- Access-based claims tied to authenticated scraping (i.e., Bright Data accessing X while logged into accounts) might be cognizable under contract or CDAFA theories if adequately pled.

### Post-Dismissal: Second Amended Complaint (November 2024)

X filed a second amended complaint, and in [November 2024 Judge Alsup issued a further ruling](https://docs.justia.com/cases/federal/district-courts/california/candce/3:2023cv03698/415869/156) that allowed a narrowed version of the trespass-to-chattels claim to proceed. The court found that X now plausibly alleged that "scrapers traverse the X service in patterns markedly different from humans or authorized machines, resulting in abnormal use of server capacity." The judge described this amended pleading as a significant improvement over the prior complaint, finding the trespass claim viable on these new facts. Misappropriation and unjust enrichment — previously dismissed under copyright preemption — were not revived. The case proceeded to discovery and is scheduled for jury trial before Judge Alsup on **March 2, 2026**, in San Francisco.

## Impact Assessment [MEDIUM confidence]

### Significance for the Web Scraping Legal Landscape

The May 2024 ruling in *X Corp. v. Bright Data* materially reshaped the strategic calculus for online platforms seeking to stop commercial data collection:

**Copyright preemption as scraper defense**: The decision establishes that conflict preemption under the Copyright Act can extinguish state-law contract and misappropriation claims premised on copying publicly accessible content. This is a powerful and novel defense that scrapers and data brokers can raise in any jurisdiction subject to the Ninth Circuit or persuasive authority from N.D. Cal.

**Terms of service limitations**: Courts in the Ninth Circuit have now twice in 2024 rejected ToS-based enforcement against scrapers of public content (Meta and X). The emerging principle is that ToS cannot bind parties who never affirmatively accepted them (logged-in accounts), and even where accepted, enforcement that conflicts with federal law is preempted.

**Trespass to chattels as the surviving theory**: The November 2024 ruling on the second amended complaint signals that platforms *can* plausibly plead trespass claims — but only if they allege specific, measurable server degradation caused by bot traffic patterns. This is a higher bar than X initially attempted to clear. The March 2026 trial will test whether X can prove this theory to a jury.

**AI training data implications**: The ruling has immediate relevance to the wave of AI copyright litigation, as AI model developers frequently scrape public websites for training data. The court's recognition that contract-based restrictions on copying publicly available content may be preempted by the Copyright Act supports arguments that platforms cannot use ToS alone to prohibit AI training data collection, at least in the Ninth Circuit.

### Who Is Affected

- **Online platforms and publishers**: Companies relying on ToS restrictions and state-law claims to stop commercial scraping must reexamine their enforcement strategies. Copyright infringement claims (for content actually owned by the platform) and technical countermeasures remain more viable than contract or misappropriation claims.
- **Data brokers and alternative data providers**: Commercial scrapers of public data in the Ninth Circuit now have a strengthened preemption defense against state-law contract claims.
- **AI developers**: Training data scrapers can cite *X Corp. v. Bright Data* for the proposition that platforms' ToS restrictions on copying are subject to copyright conflict preemption.
- **Legal practitioners**: The decision signals that multi-theory "kitchen sink" complaints against scrapers are vulnerable; each theory must be independently viable and adequately pled.

## Action Items

- Online platforms and publishers operating in the Ninth Circuit should audit their anti-scraping enforcement strategy, shifting focus away from contract/tort claims toward (a) copyright infringement for platform-owned content, (b) CDAFA or CFAA claims for authenticated scraping or circumvention of technical controls, and (c) well-pled trespass to chattels claims tied to documented server-load evidence.
- Legal teams handling ToS drafts should ensure ToS explicitly conditions access on user authentication, and should collect server-load metrics that could support future trespass claims if scraping becomes litigated.
- Data brokers and AI developers should document that their scraping operations target only publicly accessible (unauthenticated) pages and monitor the March 2026 trial outcome for guidance on what constitutes actionable trespass to chattels harm.
- Track any Ninth Circuit appeal that follows the 2026 trial verdict — the appellate court's treatment of copyright conflict preemption in this context will be authoritative across the circuit.
- Companies in jurisdictions outside the Ninth Circuit should note that this ruling is persuasive but not binding; CFAA and state tort theories may remain more viable in other circuits.

## Related Reports

- [reports/privacy/litigation/california-cipa-chat-wiretapping-garcia-v-buildcom-2024-04-17.md](../litigation/california-cipa-chat-wiretapping-garcia-v-buildcom-2024-04-17.md) -- California federal court litigation on technology-based privacy claims, illustrating the broader pattern of N.D. Cal. dismissing novel digital privacy tort theories on pleading grounds.
- [reports/privacy/litigation/massachusetts-doe-v-tenet-healthcare-pixel-tracking-2024-05-20.md](../litigation/massachusetts-doe-v-tenet-healthcare-pixel-tracking-2024-05-20.md) -- Related litigation examining unauthorized data collection from web properties and the boundaries of platform liability for third-party data access.

## Sources

1. [Proskauer Rose — "California Court Issues Another Noteworthy Decision Dismissing Breach of Contract and Tort Claims in Web Scraping Dispute" (May 14, 2024)](https://newmedialaw.proskauer.com/2024/05/14/california-court-issues-another-noteworthy-decision-dismissing-breach-of-contract-and-tort-claims-in-web-scraping-dispute/) — Primary law firm analysis from Bright Data's counsel summarizing the May 9 ruling and its significance.
2. [Skadden — "District Court Adopts Broad View of Copyright Preemption in Data Scraping Case" (May 2024)](https://www.skadden.com/insights/publications/2024/05/district-court-adopts-broad-view) -- In-depth analysis of the conflict preemption holding and its novelty in the data-scraping context.
3. [Morrison Foerster / Socially Aware Blog — "California Federal Court Holds X's Claims Against Scraper Preempted by Federal Law" (June 4, 2024)](https://www.mofo.com/resources/insights/240604-california-federal-court-holds-x-s-claims) -- Additional law firm analysis covering preemption doctrine and AI training data implications.
4. [CourtListener — X Corp. v. Bright Data Ltd., 3:23-cv-03698 Docket](https://www.courtlistener.com/docket/67637345/x-corp-v-bright-data-ltd/) -- Official court docket for the N.D. Cal. case, including all filed documents.
5. [Justia — Order Re Second Amended Complaint (Nov. 26, 2024)](https://docs.justia.com/cases/federal/district-courts/california/candce/3:2023cv03698/415869/156) -- Court order allowing the trespass-to-chattels claim to proceed on amended pleading.
6. [Leagle — X Corp. v. Bright Data Ltd., No. C 23-03698 WHA (May 10, 2024)](https://www.leagle.com/decision/infdco20240510c40) -- Text of the original May 9, 2024 dismissal order.
7. [Skadden / CLS Blue Sky Blog — "Skadden Discusses Court's Broad View of Copyright Preemption" (May 23, 2024)](https://clsbluesky.law.columbia.edu/2024/05/23/skadden-discusses-courts-broad-view-of-copyright-preemption-in-data-scraping-case/) -- Columbia Law School repost of Skadden analysis, providing additional academic context.
8. [Eric Goldman Technology & Marketing Law Blog — "X Corp. v. Bright Data is the Decision We've Been Waiting For" (May 2024)](https://blog.ericgoldman.org/archives/2024/05/x-corp-v-bright-data-is-the-decision-weve-been-waiting-for-guest-blog-post.htm) -- Expert commentary on policy implications, including the "information monopolies" risk articulated by Judge Alsup.
9. [FKKS IP & Media Law Blog — "BLOCKBUSTER RULING: Federal Court Holds That Copyright Act Preempts X's Web Scraping Claims"](https://ipandmedialaw.fkks.com/post/102j7d0/blockbuster-ruling-federal-court-holds-that-copyright-act-preempts-xs-web-scrap) -- Law firm commentary characterizing the ruling's significance for the AI copyright litigation ecosystem.
10. [Courthouse News Service — "Judge tosses X's contract claims against data scraping company"](https://www.courthousenews.com/judge-tosses-xs-contract-claims-against-data-scraping-company/) -- News coverage of the dismissal, including procedural details.
11. [California Lawyers Association — "Ninth Circuit Holds Data Scraping is Legal in hiQ v. LinkedIn"](https://calawyers.org/privacy-law/ninth-circuit-holds-data-scraping-is-legal-in-hiq-v-linkedin/) -- Background on the foundational *hiQ* CFAA ruling that X's complaint was designed to work around.
12. [Fenwick — "HiQ Labs Scrapes by Again: The Ninth Circuit Reaffirms that Data Scraping Does Not Violate the CFAA"](https://www.fenwick.com/insights/publications/hiq-labs-scrapes-by-again-the-ninth-circuit-reaffirms-that-data-scraping-does-not-violate-the-cfaa-1) -- Analysis of the Ninth Circuit's reaffirmation of *hiQ* post-*Van Buren*, the immediate precedential backdrop.
13. [ZwillGen — "hiQ v. LinkedIn Wrapped Up: Web Scraping Lessons Learned"](https://www.zwillgen.com/alternative-data/hiq-v-linkedin-wrapped-up-web-scraping-lessons-learned/) -- Summary of *hiQ* settlement and remaining lessons for ToS enforcement.
14. [Attorney Evan Brown — "X can claim trespass to chattel in data scraping case" (Dec. 1, 2024)](https://evan.law/2024/12/01/x-gets-chance-to-plead-trespass-to-chattel-claim-in-data-scraping-case/) -- Analysis of the November 2024 second amended complaint ruling allowing trespass claim to proceed.
15. [Digital Policy Alert — "Issued ruling in lawsuit alleging copyright violations concerning data scraping (X Corp v Bright Data Ltd)"](https://digitalpolicyalert.org/event/19822-issued-ruling-in-lawsuit-alleging-copyright-violations-concerning-data-scrapping-x-corp-v-bright-data-ltd) -- Policy tracker entry for the ruling, with procedural history.
