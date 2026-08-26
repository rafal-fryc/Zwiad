---
title: "Brantley v. Prisma Labs: Court Dismisses BIPA Class Action Against Lensa AI Magic Avatar App for Lack of Standing"
date: 2024-08-06
jurisdiction: "Illinois"
category: "privacy"
development_type: "court-decision"
finding_id: "SCAN-20240815-019"
topic_key: "illinois-9643bbf8-2024"
topic_type: "litigation"
first_reported: 2024-08-15
last_updated: 2024-08-15
status_history: []
cluster: "Illinois BIPA Litigation and Amendments"
cluster_slug: "illinois-bipa-litigation"
---

# Brantley v. Prisma Labs: Court Dismisses BIPA Class Action Against Lensa AI Magic Avatar App for Lack of Standing

**Jurisdiction:** Illinois (N.D. Ill.) | **Category:** Privacy | **Date:** August 6, 2024

## Executive Summary [MEDIUM confidence]

On August 6, 2024, Judge Jorge L. Alonso of the U.S. District Court for the Northern District of Illinois dismissed *Brantley v. Prisma Labs, Inc.*, No. 1:23-cv-01566, a proposed class action brought under the [Illinois Biometric Information Privacy Act (BIPA), 740 ILCS 14/](https://www.ilga.gov/Legislation/ILCS/Articles?ActID=3004&ChapterID=57&Print=True) against the maker of the Lensa "Magic Avatar" AI photo application. The plaintiff alleged that Prisma Labs scraped biometric data — specifically facial geometry scans — from a publicly available AI training dataset called LAION-5B without Illinois residents' knowledge or consent. Judge Alonso dismissed the complaint for two independent reasons: (1) lack of Article III standing because the plaintiff could not plausibly allege that his own biometric data was actually scraped, and (2) lack of personal jurisdiction over the California-incorporated defendant. The court granted leave to file an amended complaint by September 9, 2024. The decision is notable as an early judicial test of whether BIPA's consent and collection requirements reach AI companies that train on scraped internet images, and it sets a meaningful pleading hurdle for plaintiffs who cannot directly demonstrate their data was collected.

## Background [HIGH confidence]

### BIPA: Illinois's Biometric Privacy Framework

Illinois enacted the [Biometric Information Privacy Act (BIPA), 740 ILCS 14/](https://www.ilga.gov/Legislation/ILCS/Articles?ActID=3004&ChapterID=57&Print=True) in 2008 as the first US state biometric privacy statute to include a private right of action. BIPA imposes strict obligations on private entities before they may collect, use, or disclose biometric identifiers — defined to include fingerprints, retinal and iris scans, voiceprints, handprints, and scans of face geometry — from Illinois residents.

Section 15(a) requires private entities to adopt a publicly available written retention and destruction schedule. Section 15(b) requires informed written consent and notice before collection. Section 15(c) prohibits profiting from biometric data. Section 15(d) bars disclosure to third parties without consent. Statutory damages under Section 20 are $1,000 per negligent violation and $5,000 per intentional or reckless violation, plus attorneys' fees and costs. In August 2024 — the same month as the Brantley ruling — [Governor Pritzker signed Senate Bill 2979](https://www.gtlaw.com/en/insights/2024/8/bipa-update-illinois-limits-liability-and-clarifies-electronic-consent-for-biometric-data-collection) amending BIPA to cap recovery at a single violation per person regardless of the number of collection or disclosure events, directly responding to the Illinois Supreme Court's explosive *Cothron v. White Castle* decision.

### Lensa and the Magic Avatar Feature

Lensa is a mobile AI photo-editing application developed and operated by Prisma Labs, Inc., a California corporation. Among its most prominent features is "Magic Avatars," which transforms user-uploaded selfies into stylized AI-generated portraits in various artistic styles. Magic Avatars is powered by a generative AI model trained on the [LAION-5B dataset](https://laion.ai/blog/laion-5b/), an open large-scale collection of approximately 5.85 billion image-text pairs compiled by the non-profit Large-scale Artificial Intelligence Open Network (LAION). LAION-5B was assembled by crawling URLs from the Common Crawl web archive — a snapshot of a substantial portion of the publicly accessible internet.

When Lensa launched Magic Avatars in late 2022, it attracted tens of millions of users but simultaneously drew scrutiny from biometric privacy advocates who questioned whether training on scraped internet images — many of which depict identifiable human faces — constituted unlawful biometric data collection under BIPA.

### The Lawsuit

On March 14, 2023, Tyrone Brantley filed a putative class action in the Northern District of Illinois against Prisma Labs. Brantley alleged that Prisma Labs violated BIPA by using LAION-5B to extract scans of face geometry from publicly available photographs — including photographs of Illinois residents — without their written consent or notice, and without a publicly available biometric data retention and destruction policy. The proposed class was sweeping: Brantley sought to represent every Illinois resident who had ever had a photograph of themselves posted anywhere online at any point in time, on the theory that LAION-5B crawled those images and that Prisma Labs performed facial geometry scans on them during AI model training.

## Detailed Analysis [MEDIUM confidence]

### The Standing Problem: Speculative Injury in the Age of Web-Scale Datasets

The central legal failure in *Brantley* was the plaintiff's inability to establish Article III standing — the constitutional minimum threshold requiring that a plaintiff show a concrete, particularized, and actual or imminent injury-in-fact caused by the defendant's conduct.

Brantley acknowledged that he had never personally uploaded any images to the LAION-5B dataset. Instead, he argued that because LAION-5B purports to index images from nearly every corner of the internet, and because he had been active on social media and other websites where photographs of him were posted, it was "virtually certain" that images of himself — and images of all proposed Illinois class members — were captured in LAION-5B, and therefore that Prisma Labs necessarily collected his biometric data when training its AI model.

Judge Alonso rejected this theory. The court applied the well-established federal pleading standard: while a plaintiff may rely on reasonable inferences, those inferences must be plausible rather than merely possible or speculative. The court found Brantley's "virtual certainty" argument insufficient because:

1. **No direct allegation that his images were in the dataset.** Although Brantley alleged that LAION-5B contains images drawn from "almost every website," he did not specifically allege that photographs of him from those websites were actually crawled and included in the dataset during the relevant period. The gap between "LAION-5B crawled most of the internet" and "LAION-5B includes images of me" was too wide to bridge through inference alone.

2. **No allegation of actual biometric extraction.** Even assuming his images were somewhere in LAION-5B, Brantley did not adequately allege that Prisma Labs actually performed facial geometry scans specifically on images depicting him, as opposed to training on text-image pairs or non-facial images in the dataset.

3. **Class definition was impossibly broad.** The proposed class — every Illinois resident ever photographed anywhere online — reflected an implausibly speculative theory of injury. Accepting it would mean that any company using LAION-5B for any purpose had necessarily violated BIPA with respect to every Illinois resident, a result the court found implausible on the alleged facts.

The court accordingly dismissed under [Rule 12(b)(1)](https://www.law.cornell.edu/rules/frcp/rule_12) for lack of subject matter jurisdiction, holding that without standing, the court lacked constitutional authority to adjudicate the claims.

### Personal Jurisdiction: The California Defendant Problem

As an independent basis for dismissal, the court also found that it lacked personal jurisdiction over Prisma Labs under [Rule 12(b)(2)](https://www.law.cornell.edu/rules/frcp/rule_12). Prisma Labs is incorporated and headquartered in California. The court found that Brantley had not adequately alleged that Prisma Labs purposefully directed conduct at Illinois — a requirement for specific personal jurisdiction under the constitutional *minimum contacts* standard established in *International Shoe Co. v. Washington* — or that the claims arose from Prisma Labs's contacts with Illinois specifically, as distinguished from its nationwide provision of a consumer application.

The personal jurisdiction defect is analytically significant beyond *Brantley*. AI companies developing foundation models on national or global datasets are frequently headquartered in California or other non-Illinois states. BIPA plaintiffs seeking to sue such companies in Illinois federal court must plead specific facts showing the defendant purposefully targeted Illinois or its residents, rather than simply offering a product available in all 50 states.

### Leave to Amend

Consistent with standard federal practice favoring opportunity to cure pleading defects, Judge Alonso granted Brantley leave to file an amended complaint by September 9, 2024. The court's analysis suggests that an amended complaint would need to allege, with factual specificity, that: (a) images depicting the plaintiff were actually included in LAION-5B; (b) Prisma Labs specifically processed those images in a manner that extracted facial geometry or other BIPA-protected biometric identifiers; and (c) sufficient minimum contacts exist to support personal jurisdiction in Illinois.

### Significance: The "AI Training Data" Theory of BIPA Liability

*Brantley* represents one of the early federal court rulings on whether BIPA's collection-and-consent requirements extend to AI model training on scraped internet images. The theory advanced by Brantley — that training on a public dataset that includes someone's photograph constitutes an unlawful "collection" of that person's biometric data — is novel and potentially vast in scope. If accepted, it would expose virtually every AI company training generative image or facial recognition models on internet-sourced data to BIPA liability for every Illinois resident depicted in that training set.

Judge Alonso did not rule that this theory is legally incorrect. He ruled only that Brantley failed to adequately plead the factual predicate: he could not plausibly allege that his specific biometric data was collected. This distinction matters: the court's ruling is a pleading sufficiency holding, not a merits determination that AI training on public datasets falls outside BIPA's reach. Future plaintiffs with more direct evidence — for example, plaintiffs who can affirmatively identify their image in the training dataset, or plaintiffs who uploaded selfies to Lensa and can allege the app extracted facial geometry as part of its processing pipeline — may fare differently.

The contrast with [*Clearview AI BIPA litigation*](https://natlawreview.com/article/first-bipa-litigation-class-members-receive-equity-clearview-ai) is instructive. Clearview built a dedicated facial recognition database by scraping and indexing images, and plaintiffs could plausibly allege that Clearview extracted their biometric data and stored it in a searchable form. That case ultimately settled for an estimated [$51.75 million in March 2025](https://www.regulatoryoversight.com/2025/04/51-75m-settlement-in-clearview-ai-biometric-privacy-litigation-illustrates-creative-resolution-for-startups-facing-parallel-litigation-and-enforcement-action/), with class members receiving a 23% equity stake in the company. The Clearview fact pattern — a company explicitly building a biometric identification system from scraped images — presents a cleaner theory of BIPA liability than the *Brantley* theory, where the AI company's purpose was artistic image generation rather than biometric identification.

## Impact Assessment [MEDIUM confidence]

### AI Companies Using Public Training Datasets

The *Brantley* dismissal gives AI companies a meaningful defense against speculative BIPA class actions premised solely on the use of publicly available datasets like LAION-5B. A plaintiff who cannot affirmatively allege — based on actual facts, not probabilistic reasoning — that a defendant extracted their specific biometric data cannot maintain a BIPA suit in federal court. This sets a non-trivial pleading bar that screens out the broadest, most speculative theories of AI training data liability.

However, the ruling does not immunize AI companies. Companies that:

- Store or process user-uploaded photographs in a manner that involves facial geometry extraction (such as through real-time AI avatar generation based on selfies)
- Build databases that index or catalog facial recognition data extracted from scraped images
- Operate biometric data systems in connection with Illinois-based users

remain squarely within BIPA's reach and must satisfy its consent, notice, and retention policy requirements.

### Compliance Implications for Consumer-Facing AI Apps

Consumer-facing AI applications that process user photographs — including avatar generators, photo editors, face filters, and similar tools — face distinct BIPA exposure compared to back-end model training. When a user in Illinois uploads a selfie to an AI app and the app processes that image to extract facial geometry (even as a step in generating stylized output rather than storing a biometric record), the better-reasoned view is that BIPA's collection requirements are implicated. The standing hurdle the *Brantley* court identified does not arise in that context because the user can directly allege that the company processed their image.

### BIPA Amendments Coincide with Brantley Ruling

The timing of the ruling — August 6, 2024 — coincided with the Illinois legislature's passage of [Senate Bill 2979](https://ogletree.com/insights-resources/blog-posts/illinois-legislature-passes-bill-to-clarify-per-scan-damages-for-privacy-act-violations-awaits-governors-signature/), signed by Governor Pritzker on August 2, 2024. SB 2979 caps BIPA damages at a single recovery per person regardless of the number of collection or disclosure events, dramatically reducing the annihilative liability exposure that had previously deterred settlement and driven plaintiffs to seek staggering class-wide damages. In April 2026, the Seventh Circuit held in *Clay v. Union Pacific* that the SB 2979 damages cap applies retroactively to pending cases, further reducing the value of open BIPA lawsuits.

### Geographic and Jurisdictional Risk for Non-Illinois Companies

The dismissal for lack of personal jurisdiction highlights a structural challenge for plaintiffs seeking to bring BIPA claims in Illinois federal court against technology companies headquartered elsewhere. A California-based AI company that offers an app nationally may lack sufficient Illinois-specific contacts to support specific personal jurisdiction unless it specifically targeted the Illinois market. Plaintiffs may increasingly need to file in the defendant's home jurisdiction (California, etc.) or develop stronger facts connecting the defendant's conduct to Illinois specifically.

## Action Items

- **AI companies using scraped image datasets for model training**: Conduct a legal assessment of whether training data processing involves BIPA-protected biometric identifiers (facial geometry scans). LAION-5B and similar large-scale datasets are likely to be the subject of continued litigation; document the technical steps of the training pipeline that may or may not constitute "collection" of biometric identifiers under 740 ILCS 14/10.
- **Consumer-facing AI photo apps with Illinois users**: Ensure full BIPA compliance for in-app image processing: (a) adopt and publish a written biometric data retention and destruction policy per 740 ILCS 14/15(a); (b) obtain informed written (or electronic, post-SB2979) consent before collecting biometric identifiers per 740 ILCS 14/15(b); (c) limit disclosure per 740 ILCS 14/15(d).
- **Litigation defense counsel**: Track whether Brantley files an amended complaint by September 9, 2024. Monitor for future cases where plaintiffs develop more targeted evidence of their specific image's presence in AI training datasets — the *Brantley* dismissal is a procedural win, not a merits ruling.
- **Policy and compliance teams**: Note that the BIPA SB 2979 damages cap (single recovery per person) reduces aggregate class exposure significantly for existing and future BIPA defendants, including AI companies. Retroactive application confirmed by the Seventh Circuit in *Clay v. Union Pacific* (April 2026).
- **In-house counsel at AI companies**: Review terms of service, privacy notices, and consent mechanisms for any feature that processes user photographs. Ensure these comply with BIPA's heightened consent standard, not merely standard CCPA or GDPR consent frameworks.

## Related Reports

- [reports/privacy/litigation/illinois-thermoflex-bipa-insurance-coverage-2024-06-06.md](/home/rafal/projecty/Zwiad/reports/privacy/litigation/illinois-thermoflex-bipa-insurance-coverage-2024-06-06.md) -- Addresses BIPA insurance coverage exclusions in the Seventh Circuit; directly relevant to companies assessing coverage for BIPA AI training data claims.
- [reports/privacy/illinois-bipa-7th-circuit-retroactivity-2026-04-12.md](/home/rafal/projecty/Zwiad/reports/privacy/illinois-bipa-7th-circuit-retroactivity-2026-04-12.md) -- Seventh Circuit's 2026 ruling holding that the 2024 BIPA SB 2979 damages cap applies retroactively to pending cases, directly affecting the remedy landscape for cases like *Brantley*.
- [reports/privacy/illinois-bipa-sb2979-damages-amendment-2024-04-17.md](/home/rafal/projecty/Zwiad/reports/privacy/illinois-bipa-sb2979-damages-amendment-2024-04-17.md) -- Legislative analysis of the SB 2979 BIPA damages reform enacted the same month as the Brantley dismissal.
- [reports/privacy/litigation/california-x-corp-bright-data-web-scraping-2024-05-09.md](/home/rafal/projecty/Zwiad/reports/privacy/litigation/california-x-corp-bright-data-web-scraping-2024-05-09.md) -- Related web-scraping litigation in California addressing legality of scraping public data for AI training purposes.

## Sources

1. [Brantley v. Prisma Labs, Inc., No. 1:2023cv01566, Document 44 (N.D. Ill. Aug. 6, 2024) — Justia](https://law.justia.com/cases/federal/district-courts/illinois/ilndce/1:2023cv01566/431303/44/) -- Primary source: court docket entry for the dismissal order.
2. [Judge Makes Class Action Claims Against "Magic Avatar" AI App Disappear — Inside Class Actions / Covington & Burling](https://www.insideclassactions.com/2024/08/12/judge-makes-class-action-claims-against-magic-avatar-ai-app-disappear/) -- Law firm analysis summarizing grounds for dismissal and legal significance.
3. [Dechert Obtains Landmark Win for AI Leader Prisma Labs — Dechert LLP](https://www.dechert.com/knowledge/news/2024/8/dechert-obtains-landmark-win-for-ai-leader-prisma-labs.html) -- Defense counsel announcement detailing the standing and personal jurisdiction holdings.
4. [Prisma Labs Skirts BIPA Suit Over Training of Its AI Photo App — Bloomberg Law](https://news.bloomberglaw.com/privacy-and-data-security/prisma-labs-skirts-bipa-suit-over-training-of-its-ai-photo-app) -- News coverage of the dismissal with legal analysis.
5. [Brantley v. Prisma Labs — WordsByWes Case Tracker](https://www.wordsbywes.ink/casetracker/case/brantley-v-prisma-labs/) -- Case tracker with procedural history, including the September 9, 2024 amended complaint deadline.
6. [Brantley v. Prisma Labs, 1:23-cv-01566 — CourtListener.com](https://www.courtlistener.com/docket/67004686/brantley-v-prisma-labs-inc/) -- Full docket listing for the case in the Northern District of Illinois.
7. [AI Avatar App is the Latest Target of BIPA Class Action Litigation — National Law Review / Privacy World](https://natlawreview.com/article/ai-avatar-app-latest-target-bipa-class-action-litigation) -- Early 2023 analysis of the original complaint and the novel BIPA theory at issue.
8. [Biometric Information Privacy Act, 740 ILCS 14/ — Illinois General Assembly (official text)](https://www.ilga.gov/Legislation/ILCS/Articles?ActID=3004&ChapterID=57&Print=True) -- Official statutory text of BIPA as enacted and amended.
9. [BIPA Update: Illinois Limits Liability and Clarifies Electronic Consent — Greenberg Traurig LLP](https://www.gtlaw.com/en/insights/2024/8/bipa-update-illinois-limits-liability-and-clarifies-electronic-consent-for-biometric-data-collection) -- Analysis of the August 2024 BIPA SB 2979 amendments signed contemporaneously with the Brantley ruling.
10. [Illinois Legislature Passes Bill to Clarify Per-Scan Damages — Ogletree Deakins](https://ogletree.com/insights-resources/blog-posts/illinois-legislature-passes-bill-to-clarify-per-scan-damages-for-privacy-act-violations-awaits-governors-signature/) -- Legislative history and analysis of SB 2979 damages reform.
11. [A First in BIPA Litigation: Class Members Receive Equity in Clearview AI — National Law Review](https://natlawreview.com/article/first-bipa-litigation-class-members-receive-equity-clearview-ai) -- Clearview AI BIPA settlement providing contrast to the Brantley AI training data theory.
12. [$51.75M Settlement in Clearview AI Biometric Privacy Litigation — Regulatory Oversight](https://www.regulatoryoversight.com/2025/04/51-75m-settlement-in-clearview-ai-biometric-privacy-litigation-illustrates-creative-resolution-for-startups-facing-parallel-litigation-and-enforcement-action/) -- 2025 final settlement approval in Clearview BIPA class action: $51.75 million, 23% equity stake.
13. [LAION-5B: A New Era of Open Large-Scale Multi-Modal Datasets — LAION.ai](https://laion.ai/blog/laion-5b/) -- Official description of the LAION-5B dataset central to the plaintiff's factual allegations.
