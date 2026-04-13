---
title: "Ohio Man Pleads Guilty in First-Ever Conviction Under the TAKE IT DOWN Act"
jurisdiction: Federal
category: privacy
development_type: enforcement
date: 2026-04-08
first_reported: 2026-04-08
last_updated: 2026-04-12
topic_key: federal-take-it-down-act-strahler-conviction
topic_type: enforcement
status_history: []
deprecated: true
superseded_by: SCAN-20260412-028
cluster: "TAKE IT DOWN Act: Federal NCII Enforcement"
cluster_slug: "take-it-down-act-enforcement"
---

> **DEPRECATED — This report (SCAN-20260412-009) has been superseded by a more fully verified version.**
> See the authoritative report: [reports/privacy/take-it-down-act-strahler-conviction-2026-04-12.md](take-it-down-act-strahler-conviction-2026-04-12.md) (SCAN-20260412-028).
> Do not cite this report in client materials. Use SCAN-20260412-028 instead.

# Ohio Man Pleads Guilty in First-Ever Conviction Under the TAKE IT DOWN Act

**Jurisdiction:** Federal (U.S. District Court for the Southern District of Ohio)  
**Date:** April 8, 2026  
**Category:** AI Law / Enforcement

## Executive Summary [HIGH confidence]

James Strahler II, 37, of Columbus, Ohio, pleaded guilty on April 8, 2026 in the U.S. District Court for the Southern District of Ohio to a multi-count federal indictment that includes the first-ever criminal conviction (conviction via guilty plea; sentencing pending) under the [TAKE IT DOWN Act](https://www.congress.gov/bill/119th-congress/senate-bill/146/text). U.S. Attorney Dominick S. Gerace II [confirmed](https://www.justice.gov/usao-sdoh/pr/columbus-man-pleads-guilty-cyberstalking-exes-creating-ai-generated-obscene-material) that Strahler is "the first person in the United States to be convicted" under the Act, which was signed into law by President Trump on May 19, 2025. Sentencing is scheduled for a later date.

## The TAKE IT DOWN Act [HIGH confidence]

The TAKE IT DOWN Act (S. 146, 119th Congress) passed the House on April 28, 2025 (after Senate passage on February 13, 2025) and was [signed into law on May 19, 2025](https://en.wikipedia.org/wiki/TAKE_IT_DOWN_Act). The statute has two main operative components:

1. **Criminal prohibition (effective immediately):** Makes it a federal crime to knowingly publish, or threaten to publish, nonconsensual intimate visual depictions of identifiable individuals, including AI-generated "digital forgeries" (deepfakes), as described in the [Congressional Research Service analysis](https://www.congress.gov/crs-product/LSB11314).
2. **Platform notice-and-removal obligation:** Covered online platforms must implement a notice-and-removal process and take down reported imagery (and known identical copies) within 48 hours of a compliant request. Platforms have until **May 19, 2026** to comply, with FTC enforcement authority under Section 5 of the [Federal Trade Commission Act](https://www.law.cornell.edu/uscode/text/15/45).

The Act's criminal prohibition is codified at [47 U.S.C. § 223(h)](https://www.law.cornell.edu/uscode/text/47/223) (added by the Act to the Communications Act), and the platform notice-and-removal obligation is codified at [47 U.S.C. § 223a](https://www.law.cornell.edu/uscode/text/47/223a). The Act supplements — but does not reside in — existing Title 18 offenses targeting nonconsensual intimate imagery and cyberstalking.

## The Strahler Case [HIGH confidence]

According to the [DOJ press release](https://www.justice.gov/usao-sdoh/pr/columbus-man-pleads-guilty-cyberstalking-exes-creating-ai-generated-obscene-material) from the U.S. Attorney's Office for the Southern District of Ohio and [contemporaneous reporting](https://www.10tv.com/article/news/local/columbus-man-first-convicted-take-it-down-act-pleads-guilty-cybercrimes/530-fff42eac-4089-49ce-847b-0597c8a8fe39) from local news, Strahler pleaded guilty to three federal counts:

- **Cyberstalking** (18 U.S.C. § 2261A)
- **Producing obscene visual representations of the sexual abuse of children** (18 U.S.C. § 1466A)
- **Publication of digital forgeries** under the TAKE IT DOWN Act

### Underlying conduct

Between December 2024 and June 2025, Strahler:

- Sent harassing messages, including real and AI-generated nude images, to at least six women (former intimate partners and acquaintances), and in at least one case distributed the material to the victim's coworkers and family members.
- Used AI tools to morph children's faces onto the bodies of adults or other minors to create sexually explicit videos, including depictions of boys with their own family members.
- Created more than 700 images of real victims and animated persons and posted them to a website dedicated to child sexual abuse material.
- Installed more than 24 AI applications and over 100 web-based AI models on his phone, reflecting a sustained pattern of generative-AI abuse, per [Spectrum News](https://spectrumnews1.com/oh/columbus/news/2026/04/08/take-it-down-act-conviction) and [NBC News](https://www.nbcnews.com/tech/security/first-person-convicted-law-criminalizing-intimate-deepfakes-rcna267236).

### Prosecutorial significance

U.S. Attorney Gerace publicly framed the plea as the first conviction under the TAKE IT DOWN Act. The charging structure — pairing the new TAKE IT DOWN Act count with established cyberstalking and CSAM statutes — suggests DOJ's early enforcement model will use the new statute as an **additive** charge layered on top of existing conduct-based offenses rather than as a standalone prosecution. Because Strahler pleaded guilty, there will be no adjudicated ruling on constitutional challenges (e.g., First Amendment overbreadth) to the TAKE IT DOWN Act's criminal provisions in this case.

## Analysis and Implications

### For prosecutors and law enforcement

- The TAKE IT DOWN Act provides a **dedicated federal hook** for AI-generated nonconsensual intimate imagery of adults, which previously sat in an uncomfortable gap between state revenge-porn statutes and federal CSAM/cyberstalking law.
- Expect continued charge-stacking where the conduct spans adults and minors, since Title 18 CSAM penalties remain significantly higher than the TAKE IT DOWN Act's criminal penalties.

### For covered platforms

- The criminal conviction does not change platform obligations, but it underscores FTC and DOJ seriousness as the **May 19, 2026 notice-and-removal compliance deadline** approaches. Platforms should have their designated reporting channel, 48-hour takedown workflow, and hash-matching for known identical copies operational by that date.
- Per [Skadden's analysis](https://www.skadden.com/insights/publications/2025/06/take-it-down-act) and [Proskauer's client alert](https://www.proskauer.com/blog/take-it-down-act-signed-into-law-offering-tools-to-fight-non-consensual-intimate-images-and-creating-a-new-image-takedown-mechanism), covered platforms should document good-faith compliance given the Act's FTC Act §5 enforcement backstop.

### For AI developers

- Strahler's use of 24+ AI apps and 100+ web-based models highlights the role of **undermoderated or open-source generative image tools** in image-based abuse. Developers of face-swap, undress, and image-morph tools should expect downstream pressure (contractual, reputational, regulatory) even though the Act does not directly impose liability on model providers.

### Litigation outlook

- Because this case resolved by plea, the first **contested** constitutional challenge to the TAKE IT DOWN Act's criminal provisions remains pending future prosecutions. First Amendment challenges (vagueness, overbreadth of "digital forgeries") are widely anticipated by commentators including the [National Association of Attorneys General](https://www.naag.org/attorney-general-journal/congresss-attempt-to-criminalize-nonconsensual-intimate-imagery-the-benefits-and-potential-shortcomings-of-the-take-it-down-act/) and [Dynamis LLP](https://www.dynamisllp.com/knowledge/navigating-take-it-down-act-in-litigation).

## Action Items

- **Covered platforms:** Verify notice-and-removal infrastructure is live and auditable by May 19, 2026. Confirm designated contact is published and the 48-hour SLA is tracked.
- **Counsel advising generative AI developers:** Review product safety tooling, especially face-swap and nudification workflows; document abuse-prevention measures.
- **Enforcement teams / state AGs:** Track DOJ charging patterns from this case as template for future referrals; preserve coordination channels with USAO cybercrime units.
- **Monitor:** Watch for Strahler's sentencing memo, which may be the first judicial articulation of TAKE IT DOWN Act sentencing considerations.

## Sources

1. [DOJ / U.S. Attorney's Office, Southern District of Ohio — Press release on Strahler guilty plea](https://www.justice.gov/usao-sdoh/pr/columbus-man-pleads-guilty-cyberstalking-exes-creating-ai-generated-obscene-material) — Primary source: charges, plea, U.S. Attorney statement confirming first-ever conviction.
2. [S. 146 (119th Congress) — TAKE IT DOWN Act bill text](https://www.congress.gov/bill/119th-congress/senate-bill/146/text) — Official statutory text.
3. [Congressional Research Service — LSB11314: The TAKE IT DOWN Act](https://www.congress.gov/crs-product/LSB11314) — Authoritative legal overview of criminal and platform provisions.
4. [47 U.S.C. § 223 — Obscene or harassing telephone calls; includes subsection (h) criminal prohibition added by the TAKE IT DOWN Act](https://www.law.cornell.edu/uscode/text/47/223) — Codified criminal provision.
5. [47 U.S.C. § 223a — Notice and removal of nonconsensual intimate visual depictions](https://www.law.cornell.edu/uscode/text/47/223a) — Codified platform obligation.
6. [15 U.S.C. § 45 — Federal Trade Commission Act Section 5 (unfair or deceptive acts or practices)](https://www.law.cornell.edu/uscode/text/15/45) — FTC enforcement authority for platform violations.
7. [10TV (Columbus) — Columbus man first convicted in nation under Take It Down Act](https://www.10tv.com/article/news/local/columbus-man-first-convicted-take-it-down-act-pleads-guilty-cybercrimes/530-fff42eac-4089-49ce-847b-0597c8a8fe39) — Local reporting with case details.
8. [Spectrum News 1 Ohio — Take It Down Act conviction](https://spectrumnews1.com/oh/columbus/news/2026/04/08/take-it-down-act-conviction) — Corroborating reporting.
9. [NBC News — First person convicted under law criminalizing intimate deepfakes](https://www.nbcnews.com/tech/security/first-person-convicted-law-criminalizing-intimate-deepfakes-rcna267236) — National coverage.
10. [Wikipedia — TAKE IT DOWN Act](https://en.wikipedia.org/wiki/TAKE_IT_DOWN_Act) — Background on passage and signing dates.
11. [Skadden — 'Take It Down Act' Requires Online Platforms To Remove Unauthorized Intimate Images and Deepfakes When Notified](https://www.skadden.com/insights/publications/2025/06/take-it-down-act) — Law firm compliance analysis.
12. [Proskauer Rose — Take It Down Act Signed into Law](https://www.proskauer.com/blog/take-it-down-act-signed-into-law-offering-tools-to-fight-non-consensual-intimate-images-and-creating-a-new-image-takedown-mechanism) — Platform obligations analysis.
13. [NAAG — Congress's Attempt to Criminalize Nonconsensual Intimate Imagery: Benefits and Potential Shortcomings of the TAKE IT DOWN Act](https://www.naag.org/attorney-general-journal/congresss-attempt-to-criminalize-nonconsensual-intimate-imagery-the-benefits-and-potential-shortcomings-of-the-take-it-down-act/) — Anticipated constitutional issues.
14. [Dynamis LLP — Navigating the TAKE IT DOWN Act in Litigation](https://www.dynamisllp.com/knowledge/navigating-take-it-down-act-in-litigation) — Litigation outlook.

## Related Reports

**SUPERSEDED:** This report has been superseded by SCAN-20260412-028. See [take-it-down-act-strahler-conviction-2026-04-12.md](take-it-down-act-strahler-conviction-2026-04-12.md) for the authoritative version with additional source verification.
