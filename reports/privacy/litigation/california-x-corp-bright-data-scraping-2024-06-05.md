---
title: "Federal Court Dismisses X's Data Scraping Claims Against Bright Data: Copyright Preemption Shields Commercial Scrapers"
date: 2024-06-05
jurisdiction: "California"
category: "privacy"
development_type: "court-decision"
finding_id: "SCAN-20240605-024"
topic_key: "california-2fde1700-2024"
topic_type: "enforcement"
topic_key_confidence: "low"
first_reported: 2024-06-05
last_updated: 2026-04-15
status_history:
  - "2026-04-15: Corrected erroneous claim that Bright Data settled a 2022 Meta lawsuit; replaced with accurate account that Bright Data prevailed via summary judgment in Meta Platforms, Inc. v. Bright Data Ltd., No. 3:23-cv-00077-EMC (N.D. Cal. Jan. 23, 2024), filed January 2023, with Meta voluntarily dismissing the remaining claim in February 2024. Also corrected 'dismissed Meta's similar suit' to 'granted summary judgment to Bright Data in Meta's similar suit'."
cluster: "X Corp. v. Bright Data: Web Scraping Terms-of-Service Litigation"
cluster_slug: "x-corp-bright-data-web-scraping-litigation"
---

# Federal Court Dismisses X's Data Scraping Claims Against Bright Data: Copyright Preemption Shields Commercial Scrapers

**Jurisdiction:** California (Federal — N.D. Cal.) | **Category:** Privacy / Data Law | **Date:** May 9, 2024 (reported June 5, 2024)

> **Note:** A comprehensive primary report on this case — *X Corp. v. Bright Data Ltd.*, No. C 23-03698 WHA — is available at [reports/privacy/litigation/california-x-corp-bright-data-web-scraping-2024-05-09.md](california-x-corp-bright-data-web-scraping-2024-05-09.md). This report supplements that analysis with the [Pearl Cohen Zedek Latzer Baratz law firm perspective](https://www.pearlcohen.com/federal-court-dismisses-xs-data-scraping-claims/) and provides a practitioner-focused synthesis for Israeli/cross-border data intelligence companies.

## Executive Summary [HIGH confidence]

On May 9, 2024, U.S. District Judge William Alsup of the Northern District of California issued a landmark ruling in *X Corp. v. Bright Data Ltd.*, No. C 23-03698 WHA (N.D. Cal.), dismissing all of X Corp.'s claims against Israeli data-intelligence company Bright Data Ltd. The court held that X's state-law claims for breach of contract, trespass to chattels, misappropriation, unjust enrichment, tortious interference, and violations of California's Unfair Competition Law (UCL) either were preempted by the federal Copyright Act or failed to plead cognizable harm. The ruling is the [first district court decision to apply copyright conflict preemption to dismiss a contract claim](https://www.skadden.com/insights/publications/2024/05/district-court-adopts-broad-view) in a web-scraping dispute. As [Pearl Cohen Zedek Latzer Baratz](https://www.pearlcohen.com/federal-court-dismisses-xs-data-scraping-claims/) — an Israeli-founded law firm with expertise in this area — observed, the decision "affirms Bright Data's right to scrape public data posted on social media platforms" and creates significant precedent that social media companies cannot unilaterally restrict public access to data they do not own but have made publicly available.

## Background [HIGH confidence]

### The Parties

[X Corp.](https://x.com) (formerly Twitter) is the operator of the X social media platform. [Bright Data Ltd.](https://brightdata.com/) is an Israeli company providing commercial web-scraping infrastructure: proxy networks, data collection APIs, and curated datasets sold to enterprise clients. Bright Data is headquartered in Tel Aviv and is one of the world's largest commercial data-scraping service providers. The case thus pits a major US social media platform against a significant Israeli data intelligence firm in a dispute with cross-border technology industry significance.

### Lawsuit History

X filed suit against Bright Data in the U.S. District Court for the Northern District of California on July 26, 2023, alleging that Bright Data:

1. Scraped publicly accessible content from X's platform for commercial resale;
2. Circumvented X's anti-scraping technology;
3. Enabled and encouraged its customers to do the same — all in violation of X's Terms of Service (ToS) and Developer Agreement.

The lawsuit was part of a broader campaign by X under Elon Musk's ownership to restrict automated data collection. Following the April 2022 Twitter acquisition, X imposed aggressive API rate limits and updated its ToS to prohibit scraping. In a closely related prior litigation, Bright Data had prevailed against Meta: Judge Chen of the N.D. Cal. granted summary judgment to Bright Data in [*Meta Platforms, Inc. v. Bright Data Ltd.*, No. 3:23-cv-00077-EMC (N.D. Cal. Jan. 23, 2024)](https://newmedialaw.proskauer.com/2024/05/14/california-court-issues-another-noteworthy-decision-dismissing-breach-of-contract-and-tort-claims-in-web-scraping-dispute/), a case filed in January 2023. Meta subsequently voluntarily dismissed the remaining tortious interference claim in February 2024; Bright Data publicly denied any settlement had occurred. Bright Data continued operating its scraping services throughout.

### Legal Landscape at Filing

When X filed its complaint, the web-scraping legal landscape had already been substantially shaped by [*hiQ Labs, Inc. v. LinkedIn Corp.*](https://calawyers.org/privacy-law/ninth-circuit-holds-data-scraping-is-legal-in-hiq-v-linkedin/), in which the Ninth Circuit held that automated collection of publicly accessible data does not violate the Computer Fraud and Abuse Act (CFAA) because a public website imposes no authorization requirement. Confronting this binding precedent, X deliberately chose not to bring CFAA claims, instead pursuing an exclusively contract- and tort-based theory. This strategic choice proved fatal when the court applied copyright conflict preemption to those state-law claims.

One month before the X ruling, Judge Chen of the same N.D. Cal. court granted summary judgment to Bright Data in Meta's similar suit ([*Meta Platforms, Inc. v. Bright Data Ltd.*, No. 3:23-cv-00077-EMC](https://www.mofo.com/resources/insights/240604-california-federal-court-holds-x-s-claims)), finding that Bright Data could only be bound by Meta's ToS to the extent it scraped while authenticated (logged in) and that unauthenticated public-data scraping could not give rise to breach of contract liability. The *X Corp.* ruling extended and deepened these principles.

## Detailed Analysis [HIGH confidence]

### Claims Brought by X Corp.

X Corp. advanced six categories of claims against Bright Data, which Judge Alsup organized into two operative theories of wrongdoing:

**Data-based claims** (targeting scraping and resale of X content):
- **Breach of contract** — Bright Data violated X's ToS and Developer Agreement by scraping and selling X data;
- **Misappropriation** — Bright Data misappropriated the commercial value of X's data assets;
- **Unjust enrichment** — Bright Data was unjustly enriched by profiting from X's platform without compensation;
- **Tortious interference** — Bright Data interfered with X's contracts with its users by inducing ToS violations.

**Access-based claims** (targeting unauthorized server access):
- **Trespass to chattels** — Bright Data's scraping bots unlawfully accessed and burdened X's server infrastructure;
- **California UCL violations** (Cal. Bus. & Prof. Code § 17200) — Bright Data's proxy-network operations constituted unfair or fraudulent business practices.

### Dismissal of Data-Based Claims: Copyright Conflict Preemption

The court's most consequential and novel holding concerned the data-based claims. Judge Alsup applied [**copyright conflict preemption**](https://clsbluesky.law.columbia.edu/2024/05/23/skadden-discusses-courts-broad-view-of-copyright-preemption-in-data-scraping-case/) under the Supremacy Clause — distinct from the "express" preemption codified in Section 301 of the Copyright Act (17 U.S.C. § 301) — holding that X's state-law claims impermissibly conflicted with the federal Copyright Act in two fundamental ways:

**First**, enforcing X's ToS to prohibit Bright Data from copying and reselling X content would prevent Bright Data and its customers from exercising **statutory fair use rights** under 17 U.S.C. § 107. Fair use is a federally guaranteed right, and state-law enforcement mechanisms cannot be used to nullify it. Allowing X to use contract law to ban all copying — regardless of whether it would qualify as fair use — would create a private contract right more expansive than federal copyright law allows.

**Second**, permitting X to assert proprietary rights over platform content through contract law would grant X de facto copyright protection over material that may not qualify for copyright at all — such as short user-generated tweets or factual posts failing the originality threshold under *Feist Publications, Inc. v. Rural Telephone Service Co.*, 499 U.S. 340 (1991). The court observed that allowing such claims would risk ["the possible creation of information monopolies that would disserve the public interest."](https://blog.ericgoldman.org/archives/2024/05/x-corp-v-bright-data-is-the-decision-weve-been-waiting-for-guest-blog-post.htm)

As [Skadden noted](https://www.skadden.com/insights/publications/2024/05/district-court-adopts-broad-view), this was the **first time a district court had applied conflict preemption to dismiss a contract claim** in a data-scraping dispute — a significant doctrinal extension. Prior conflict preemption cases in the IP context arose in different settings; applying it to extinguish ToS-based restrictions on data access is novel and potentially far-reaching.

**Claims dismissed on preemption grounds:** Breach of contract (data-scraping component), misappropriation, unjust enrichment, and the tortious interference count to the extent it rested on inducing ToS violations related to data copying.

### Dismissal of Access-Based Claims: Failure to Allege Harm

The access-based claims — trespass to chattels and UCL — were dismissed on a distinct, non-preemption ground: failure to adequately plead cognizable harm.

**Trespass to chattels**: Under California law, trespass to chattels requires pleading actual dispossession of or physical damage to the chattel. Mere unauthorized access is legally insufficient. [As Pearl Cohen analyzed](https://www.pearlcohen.com/federal-court-dismisses-xs-data-scraping-claims/), the court held that X "did not adequately allege that Bright Data's access caused damage" and that "using a scraper was deemed no more burdensome than a user accessing X's servers with a browser." X's pleadings contained only conclusory references to server capacity and reputational harm, which were insufficient.

**UCL unfair competition**: X's Section 17200 claim was dismissed because the court found no fraudulent business act by Bright Data. The court held that "the sale of IP proxies is not 'inherently deceptive'" since there is no "affirmative duty to identify oneself with a given IP address." The use and sale of scraping tools and services is not inherently fraudulent absent allegations that an actual misrepresentation occurred.

### Tortious Interference

The tortious interference claim was dismissed both because it rested on the preempted contract theory and because X failed to plead the specific third-party contracts that Bright Data allegedly caused users to breach.

### Leave to Amend

The dismissal was granted with leave to amend, leaving open the possibility that:
- A properly pled trespass to chattels claim showing actual, measurable server damage could survive;
- Access-based claims tied to authenticated scraping (Bright Data logging into accounts to scrape) might be cognizable under contract or CDAFA theories if adequately pled.

### Subsequent Developments: November 2024 Second Amended Complaint Ruling

X filed a second amended complaint. In [November 2024, Judge Alsup allowed a narrowed trespass-to-chattels claim to proceed](https://docs.justia.com/cases/federal/district-courts/california/candce/3:2023cv03698/415869/156), finding that X now plausibly alleged "scrapers traverse the X service in patterns markedly different from humans or authorized machines, resulting in abnormal use of server capacity." The core copyright-preemption holdings, however, remained intact — misappropriation and unjust enrichment were not revived. The case was set for jury trial before Judge Alsup on March 2, 2026.

## Impact Assessment [MEDIUM confidence]

### Significance for the Web Scraping Legal Landscape

[Pearl Cohen](https://www.pearlcohen.com/federal-court-dismisses-xs-data-scraping-claims/) characterized the ruling as creating "a significant precedent that social media companies cannot unilaterally restrict public access to information they do not own but have made publicly available." The ruling's broader implications include:

**1. Copyright conflict preemption as a structural scraper defense.** Any state-law claim — breach of contract, misappropriation, unjust enrichment — that effectively restricts the copying of publicly posted content faces preemption challenges under this ruling. This is the most powerful and novel aspect of the decision. Scrapers in the Ninth Circuit can now raise preemption as a threshold defense, potentially disposing of cases before merits discovery.

**2. Terms of service cannot create private copyright regimes.** The court explicitly refused to allow X to build a "private copyright system that rivals and conflicts with the actual copyright system enacted by Congress." This principle has broad applicability: any platform using ToS to restrict public data access faces the same argument.

**3. Trespass to chattels survives — but requires proof of actual server harm.** The November 2024 ruling shows that trespass claims *can* succeed if scrapers cause demonstrable, abnormal server load distinct from ordinary user traffic. Platforms must instrument their infrastructure to capture such evidence before litigation.

**4. The hiQ-to-Bright Data trajectory.** Together with [*hiQ v. LinkedIn*](https://calawyers.org/privacy-law/ninth-circuit-holds-data-scraping-is-legal-in-hiq-v-linkedin/), this ruling completes a picture: CFAA claims fail against public-data scrapers (hiQ), and now contract/misappropriation claims fail too (Bright Data). The Ninth Circuit is the most scraper-friendly circuit in the US.

**5. AI training data implications.** As [FKKS observed](https://ipandmedialaw.fkks.com/post/102j7d0/blockbuster-ruling-federal-court-holds-that-copyright-act-preempts-xs-web-scrap), the ruling has immediate relevance to AI developers who scrape public websites for training data. Platforms cannot use ToS alone to prohibit AI training data collection, at least in the Ninth Circuit, if that collection would qualify as fair use or involves non-copyrightable factual content.

### Affected Parties

- **Israeli and international data companies**: Bright Data's victory directly benefits commercial data-scraping services operating in the US market. The ruling provides legal clarity that public data collection from major social media platforms is permissible under US law, strengthening the position of data intelligence firms headquartered outside the US.
- **US social media platforms**: Must reassess enforcement strategies. Contract and misappropriation claims against scrapers of public content are substantially weakened. Copyright infringement claims (for platform-owned content) and technical access controls remain the more viable paths.
- **AI developers and model trainers**: Training data collection from public websites receives indirect protection — ToS restrictions cannot block fair use scraping.
- **Data brokers and alternative data providers**: Commercial scrapers gain a preemption defense they can deploy against any state-law claim targeting public-data collection.

## Action Items

- Platforms relying on ToS-based anti-scraping enforcement should immediately audit their claims strategy: contract and misappropriation claims against public-data scrapers are vulnerable to copyright conflict preemption in the Ninth Circuit.
- Shift enforcement focus to: (a) copyright infringement claims for content the platform actually owns; (b) CDAFA or CFAA claims for authenticated access violations; and (c) trespass to chattels supported by server-instrumentation evidence showing abnormal load patterns distinct from ordinary user traffic.
- Data brokers and AI developers scraping public-facing websites should document that their operations target only unauthenticated pages and preserve records that scraping patterns do not impose abnormal server burdens.
- Monitor the March 2026 trial outcome in *X Corp. v. Bright Data* — a jury verdict on the surviving trespass-to-chattels claim will provide the first post-*hiQ* assessment of what level of server impact constitutes actionable harm.
- Companies outside the Ninth Circuit should note that this ruling is persuasive but not binding; CFAA and state tort theories may remain more viable in other circuits, and no circuit court has yet addressed copyright conflict preemption in this context.

## Related Reports

- [reports/privacy/litigation/california-x-corp-bright-data-web-scraping-2024-05-09.md](california-x-corp-bright-data-web-scraping-2024-05-09.md) — Primary comprehensive analysis of this same case (filed under SCAN-20240520-024); readers should consult that report for full background, procedural history, and extended legal analysis.
- [reports/privacy/litigation/california-cipa-chat-wiretapping-garcia-v-buildcom-2024-04-17.md](california-cipa-chat-wiretapping-garcia-v-buildcom-2024-04-17.md) — Related N.D. Cal. litigation on technology-based privacy claims; illustrates the broader pattern of California federal courts scrutinizing novel digital privacy theories on pleading grounds.
- [reports/privacy/litigation/massachusetts-doe-v-tenet-healthcare-pixel-tracking-2024-05-20.md](massachusetts-doe-v-tenet-healthcare-pixel-tracking-2024-05-20.md) — Related litigation on unauthorized data collection from web properties and the limits of platform liability for third-party data access.

## Sources

1. [Pearl Cohen Zedek Latzer Baratz — "Federal Court Dismisses X's Data Scraping Claims" (June 2024)](https://www.pearlcohen.com/federal-court-dismisses-xs-data-scraping-claims/) — Primary source for this finding; Israeli-founded law firm analysis of the ruling and its cross-border significance for data companies.
2. [Skadden — "District Court Adopts Broad View of Copyright Preemption in Data Scraping Case" (May 2024)](https://www.skadden.com/insights/publications/2024/05/district-court-adopts-broad-view) — In-depth analysis of the conflict preemption holding and its novelty in the data-scraping context.
3. [Morrison Foerster — "California Federal Court Holds X's Claims Against Scraper Preempted by Federal Law" (June 4, 2024)](https://www.mofo.com/resources/insights/240604-california-federal-court-holds-x-s-claims) — Additional law firm analysis covering preemption doctrine and AI training data implications.
4. [Proskauer Rose — "Proskauer Secures Dismissal of Scraping Claims Against Bright Data"](https://www.proskauer.com/release/proskauer-secures-dismissal-of-scraping-claims-against-bright-data) — Announcement by Bright Data's counsel summarizing the May 9 ruling.
5. [FKKS IP & Media Law Blog — "BLOCKBUSTER RULING: Federal Court Holds That Copyright Act Preempts X's Web Scraping Claims"](https://ipandmedialaw.fkks.com/post/102j7d0/blockbuster-ruling-federal-court-holds-that-copyright-act-preempts-xs-web-scrap) — Law firm commentary on the AI training data implications and the ruling's significance for the broader IP ecosystem.
6. [Skadden / CLS Blue Sky Blog — "Skadden Discusses Court's Broad View of Copyright Preemption" (May 23, 2024)](https://clsbluesky.law.columbia.edu/2024/05/23/skadden-discusses-courts-broad-view-of-copyright-preemption-in-data-scraping-case/) — Columbia Law School repost with additional academic context.
7. [Eric Goldman Technology & Marketing Law Blog — "X Corp. v. Bright Data is the Decision We've Been Waiting For" (May 2024)](https://blog.ericgoldman.org/archives/2024/05/x-corp-v-bright-data-is-the-decision-weve-been-waiting-for-guest-blog-post.htm) — Expert commentary on the "information monopolies" risk articulated by Judge Alsup and policy implications.
8. [CourtListener — X Corp. v. Bright Data Ltd., 3:23-cv-03698 Docket](https://www.courtlistener.com/docket/67637345/x-corp-v-bright-data-ltd/) — Official court docket for the N.D. Cal. case, including all filed documents and orders.
9. [Justia — Order Re Second Amended Complaint (Nov. 26, 2024)](https://docs.justia.com/cases/federal/district-courts/california/candce/3:2023cv03698/415869/156) — Court order allowing the narrowed trespass-to-chattels claim to proceed; establishes the surviving theory.
10. [California Lawyers Association — "Ninth Circuit Holds Data Scraping is Legal in hiQ v. LinkedIn"](https://calawyers.org/privacy-law/ninth-circuit-holds-data-scraping-is-legal-in-hiq-v-linkedin/) — Background on the foundational CFAA ruling that shaped X's litigation strategy.
11. [Courthouse News Service — "Judge tosses X's contract claims against data scraping company"](https://www.courthousenews.com/judge-tosses-xs-contract-claims-against-data-scraping-company/) — News coverage including procedural details and Judge Alsup's direct quotes.
12. [Digital Policy Alert — "Issued ruling in lawsuit alleging copyright violations concerning data scraping (X Corp v Bright Data Ltd)"](https://digitalpolicyalert.org/event/19822-issued-ruling-in-lawsuit-alleging-copyright-violations-concerning-data-scrapping-x-corp-v-bright-data-ltd) — Regulatory policy tracker entry with procedural history.
