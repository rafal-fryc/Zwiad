---
title: "Federal Courts Dismiss Website Privacy Suits for Lack of Article III Standing Following Popa v. Microsoft"
date: 2026-04-21
jurisdiction: "Federal"
category: "privacy"
development_type: "court-decision"
finding_id: "SCAN-20260422-011"
topic_key: "federal-popa-cipa-article-iii-standing-2026"
topic_type: "enforcement"
first_reported: 2026-04-21
last_updated: 2026-04-22
status_history: []
cluster: "CIPA Website Wiretapping Class Actions"
cluster_slug: "cipa-website-wiretapping-litigation"
---

# Federal Courts Dismiss Website Privacy Suits for Lack of Article III Standing Following Popa v. Microsoft

**Jurisdiction:** Federal, California | **Category:** Privacy | **Date:** 2026-04-21

## Executive Summary [MEDIUM confidence]

A growing wave of California federal court decisions is dismissing website privacy class actions for lack of Article III standing, applying the Ninth Circuit's August 2025 ruling in [Popa v. Microsoft Corporation](https://cdn.ca9.uscourts.gov/datastore/opinions/2025/08/26/24-14.pdf). Under the Popa framework, plaintiffs alleging violations of the California Invasion of Privacy Act (CIPA) through website tracking technologies must plead that the defendant actually collected "embarrassing, invasive, or otherwise private information" — bare statutory violations or generic metadata collection are insufficient to confer standing. Recent decisions applying this standard include the Northern District of California's April 2026 dismissal in *In re USA Today Co. Internet Tracking Litigation* and the Southern District of California's February 2026 dismissal in *Maghoney v. Dotdash Media, Inc.* The trend represents a significant defense-side development in CIPA litigation, though a judicial split persists: some courts are distinguishing Popa and permitting standing where tracking data is more granular or aggregated into user profiles.

## Background [HIGH confidence]

### Article III Standing Doctrine in Privacy Cases

Article III of the U.S. Constitution limits federal court jurisdiction to "Cases" and "Controversies," requiring plaintiffs to demonstrate, among other things, a concrete and particularized injury-in-fact. In [TransUnion LLC v. Ramirez](https://www.supremecourt.gov/opinions/20pdf/20-297_4g25.pdf) (2021), the Supreme Court reaffirmed that "no concrete harm, no standing" — a plaintiff cannot establish Article III standing through a statutory violation alone, absent actual harm bearing a close relationship to a traditional common-law analogue. This holding had immediate implications for mass privacy litigation premised on technical statutory violations without demonstrable injury.

Following TransUnion, federal courts faced the question of how to evaluate standing in consumer privacy cases, particularly those alleging invasion of privacy through automated tracking technologies. The key inquiry became whether the alleged privacy harm was sufficiently "concrete" under common-law tort analogues — principally intrusion upon seclusion and public disclosure of private facts.

### CIPA Website Tracking Litigation Wave

The California Invasion of Privacy Act (Cal. Penal Code §§ 630–638.55) has been the vehicle for a surge in website tracking class actions. Plaintiffs' firms began filing hundreds — eventually thousands — of lawsuits alleging that websites' use of third-party pixels, session-replay tools, pen registers, and trap-and-trace devices violated CIPA's wiretapping (§ 631) and pen register (§ 638.51) provisions without user consent. These cases targeted companies across industries including media, e-commerce, healthcare, and financial services.

By 2025, [federal courts were grappling with inconsistent rulings](https://www.hklaw.com/en/insights/publications/2026/02/uncertainty-continues-in-california-on-cipa-section-63851-claims) on CIPA standing. Some courts found that tracking metadata — IP addresses, browser type, operating system — was insufficient to establish a concrete privacy injury. Others found that more granular data aggregated into user profiles could survive standing analysis. The circuit-level framework was unsettled until the Ninth Circuit's Popa decision in August 2025.

## Detailed Analysis [HIGH confidence]

### Popa v. Microsoft Corporation (9th Cir. Aug. 26, 2025)

The foundation of the current trend is the [Ninth Circuit's published opinion in *Popa v. Microsoft Corporation*](https://cdn.ca9.uscourts.gov/datastore/opinions/2025/08/26/24-14.pdf), No. 24-14 (9th Cir. Aug. 26, 2025). The plaintiff brought a putative class action alleging that Microsoft's "Clarity" session-replay tool — deployed on petsuppliesplus.com — intercepted her browsing activity in violation of Pennsylvania's Wiretapping and Electronic Surveillance Control Act (WESCA). The district court dismissed for lack of standing, and the Ninth Circuit affirmed.

The Ninth Circuit articulated a demanding standard for concrete privacy injury:

1. **Common-law tort analogy required**: Courts must "assess whether an individual plaintiff has suffered a harm that has traditionally been actionable in our nation's legal system" by comparing the specific harm to a specific common-law tort. A free-roaming statutory "right to privacy" is not sufficient.

2. **"Embarrassing, invasive, or otherwise private information" threshold**: To plead a concrete injury analogous to intrusion upon seclusion or public disclosure of private facts, the plaintiff must allege that the technology collected information of a genuinely private character — not merely browsing metadata or store-clerk-level observation.

3. **Statutory violation is not concrete injury**: An alleged violation of a privacy statute, on its own, does not establish Article III standing absent facts showing harm that "has traditionally been actionable."

The Ninth Circuit analogized Popa's browsing data — browser type, operating system, pages visited on a pet-supplies site — to a store clerk observing which aisles a shopper visits, which has never been actionable at common law. The court stressed that the plaintiff alleged "over 30 different categories of information" without identifying any that was embarrassing or sensitive.

[Wiley Law](https://www.wiley.law/pressrelease-Wiley-Represented-Amicus-Coalition-Helps-Strengthen-Limits-on-Privacy-Lawsuits-with-Ninth-Circuit-Win-for-Microsoft), whose amicus coalition participated in the Popa case, characterized the ruling as "reinfor[cing] strict limits on privacy lawsuits brought by plaintiffs trying to capitalize on businesses' use of commonplace internet technologies without suffering any legitimate harm."

### In re USA Today Co. Internet Tracking Litigation (N.D. Cal. Apr. 6, 2026)

The primary decision reported by Covington & Burling is [*In re USA Today Co. Internet Tracking Litigation*](https://www.insideclassactions.com/2026/04/13/another-court-dismisses-website-privacy-suit-for-lack-of-article-iii-standing/), 2026 WL 932655, at *3 (N.D. Cal. Apr. 6, 2026). Plaintiffs sued USA Today's publisher alleging violations of CIPA's trap-and-trace provision, asserting that third-party tracking technologies installed on the news site collected IP addresses, location, browser type, and similar data.

The Northern District of California dismissed for lack of subject matter jurisdiction under Rule 12(b)(1), holding:

- The data allegedly collected — IP addresses, browser type, device type, location metadata — "would [not] be highly offensive to a reasonable person" and courts have "repeatedly found no reasonable expectation of privacy" in such disclosures.
- Citing Popa directly, the court reiterated that a bare CIPA statutory violation is insufficient for Article III standing absent a concrete injury — plaintiffs must plead facts showing embarrassing, invasive, or otherwise private information was collected.
- The court granted leave to amend, leaving open the possibility that more specific allegations could establish standing.

### Maghoney v. Dotdash Media, Inc. (S.D. Cal. Feb. 23, 2026)

A parallel development occurred in the Southern District of California. In [*Maghoney v. Dotdash Media, Inc.*](https://law.justia.com/cases/federal/district-courts/california/casdce/3:2024cv02394/800642/34/), No. 3:2024-cv-02394 (S.D. Cal. Feb. 23, 2026), the plaintiff visited Verywell Health (a Dotdash property) and entered search terms relating to sexually transmitted infections. The plaintiff alleged the site's advertising platform intercepted and transmitted these search queries to third parties.

The court nonetheless dismissed for lack of Article III standing under Rule 12(b)(1), applying Popa to hold:

- Alleging that a defendant disclosed "sensitive health related" search terms, without indication that the search terms "were tied to his personal medical history," cannot establish a concrete injury.
- Merely searching for sensitive health terms — as opposed to disclosing one's actual medical history or diagnosis — does not establish a legally protectable privacy interest.
- The plaintiff's "unadorned allegation of anxiety" was "conclusory at best" and insufficient to show an injury that is "concrete, particularized, and actual."
- All four of the plaintiff's theories of harm failed to rise to the level of "highly offensive" conduct.
- Dismissal was with leave to amend.

The Maghoney ruling attracted significant attention from the compliance bar. [Fisher Phillips](https://www.fisherphillips.com/en/insights/insights/major-win-in-cipa-case-signals-higher-hurdles-for-privacy-plaintiffs) characterized the decision as "signals higher hurdles for privacy plaintiffs" and noted it establishes that even sensitive health search terms, without tying those terms to a specific individual's medical history, are insufficient to establish Article III standing.

### Sensitive Search Terms Not Sufficient: April 2026 Decision

A separate April 2026 decision followed the same pattern. According to [Covington & Burling's Inside Class Actions blog](https://www.insideclassactions.com/2026/04/09/sensitive-search-terms-not-enough-to-establish-article-iii-standing-under-popa/), another federal court granted a defendant's motion to dismiss for lack of Article III standing under Popa even where the plaintiff alleged that health-related search terms were shared with third parties, holding that the plaintiff "merely searched sensitive health related terms" without evidence the terms "were tied to his personal medical history" — insufficient to show a concrete privacy injury.

### The Judicial Split: Courts That Have Found Standing

Not all courts have followed the Popa framework to dismissal. [Holland & Knight's February 2026 analysis](https://www.hklaw.com/en/insights/publications/2026/02/uncertainty-continues-in-california-on-cipa-section-63851-claims) documents a continuing split among Northern District of California judges:

- Some judges dismiss CIPA § 638.51 pen register claims under Popa where the alleged data is generic metadata (IP addresses, browser type, device identifiers).
- Other judges find standing where tracking data is aggregated into "comprehensive, non-anonymous user profiles" that bear a closer relationship to the intrusion upon seclusion tort, citing the Ninth Circuit's 2020 decision in *In re Facebook, Inc. Internet Tracking Litigation*.

In *Gabrielli v. Haleon US Inc.*, for example, a district court found standing where the defendant used third-party cookies to collect browsing history, website interactions, and user input data — a more granular form of tracking than metadata alone. This confirms that the Popa standard, while demanding, does not categorically bar all CIPA website-tracking claims; it turns on the character of the specific data collected.

### CIPA Standing Roundup: Post-Popa Landscape

The [Tyz Law Group's CIPA Standing Roundup](https://www.tyzlaw.com/insights-archive/cipa-standing-roundup) catalogues the divergence across cases since Popa, noting that California federal district courts have reached "opposite results" applying the Popa standing analysis to substantially similar CIPA § 638.51 pen register allegations. Key variables that influence outcomes include:

- **Type of data**: IP addresses and browser metadata → typically insufficient; health information, browsing history with user-input data, or data tied to individual identity → more likely to survive.
- **Aggregation**: Single data points collected in isolation → weaker standing; data combined into a comprehensive user profile → stronger argument for concrete injury.
- **Specificity of pleading**: Courts repeatedly dismiss where plaintiffs rely on boilerplate allegations; plaintiffs who tailor their pleadings to identify the specific sensitive nature of the collected information fare better.

## Impact Assessment [MEDIUM confidence]

### Implications for CIPA Class Action Defendants

The Popa framework provides defendants in CIPA website-tracking class actions with a powerful early-stage defense that can resolve cases before discovery. Defendants facing § 631 wiretapping or § 638.51 pen register claims should evaluate whether the plaintiff has specifically alleged that "embarrassing, invasive, or otherwise private information" was collected — generic metadata allegations will frequently fail this test in the post-Popa landscape.

The Covington & Burling team — whose [Inside Class Actions](https://www.insideclassactions.com/2026/04/13/another-court-dismisses-website-privacy-suit-for-lack-of-article-iii-standing/) blog tracks these decisions — has highlighted the importance of 12(b)(1) motions over 12(b)(6) motions: dismissal for lack of subject matter jurisdiction is typically not a pleading defect that can be cured by better drafting, and courts frequently dismiss without prejudice subject to amendment.

### Implications for Website Operators

For companies operating websites with third-party analytics, advertising pixels, session-replay tools, and similar technologies:

- **Reduced litigation risk for metadata-only collection**: Where tracking is limited to IP addresses, browser type, device identifiers, and basic behavioral metadata, the Popa framework substantially reduces Article III standing exposure in federal court.
- **Heightened risk for health, financial, or sensitive data contexts**: Websites that collect or transmit data tied to a user's health status, specific identity, or sensitive personal characteristics face harder-to-dismiss standing arguments. Healthcare, financial services, and other sensitive-sector operators should maintain heightened caution.
- **State court remains an avenue**: The Popa standing analysis is an Article III federal court doctrine. California state court is not bound by it. As noted above, an Orange County Superior Court sustained a demurrer on narrower statutory grounds, but the state law landscape for CIPA remains contested. Plaintiffs may strategically file in state court to avoid the Popa framework.

### Implications for Plaintiffs and the Class Action Bar

The wave of Popa dismissals has raised the pleading bar substantially for plaintiffs. To survive a standing challenge, plaintiffs' counsel must:

- Specifically identify what sensitive, embarrassing, or invasive information was collected — not merely the categories of metadata.
- Plead facts connecting the collected data to the plaintiff's individual identity and privacy interest.
- Demonstrate that the collection was analogous to a recognized common-law privacy tort, not merely a technical statutory violation.

CIPA litigation volume is not expected to decline materially: [Shumaker, Loop & Kendrick's January 2026 analysis](https://www.shumaker.com/insight/client-alert-website-tracking-and-privacy-lawsuits-predicted-to-surge-in-2026-practical-steps-to-mitigate-risk/) projects continued surge in CIPA claims through 2026. However, the Popa framework is expected to shift the battleground toward state court filings and to encourage more granular, tailored pleading in federal cases.

## Action Items

- Audit website tracking technologies to identify what categories of data are being collected by third-party tools (pixels, session replay, analytics); document whether any data collected could be characterized as "embarrassing, invasive, or otherwise private" under the Popa standard.
- For companies defending CIPA class actions in federal court, assess the viability of a Rule 12(b)(1) motion to dismiss for lack of Article III standing under Popa — this may be the most efficient path to early dismissal where plaintiff's tracking allegations involve only generic metadata.
- Monitor the evolving judicial split: courts within the Northern District of California continue to reach conflicting results on near-identical CIPA § 638.51 allegations; revisit standing strategy as additional opinions issue.
- Evaluate California state court exposure separately — the Article III Popa framework does not govern CIPA claims litigated in state court, and state court plaintiffs' bar is increasingly sophisticated about this distinction.
- For healthcare, pharmaceutical, and financial services websites, apply heightened scrutiny to third-party tracking practices — data touching health status, financial condition, or sexual health is more likely to satisfy the Popa concrete-injury threshold.
- Watch for a Ninth Circuit clarification on the aggregation theory: the split between courts that credit "comprehensive user profile" arguments and those that do not may eventually require circuit-level resolution.

## Related Reports

- [reports/privacy/litigation/california-cipa-pen-register-ip-address-2025-01-15.md](../litigation/california-cipa-pen-register-ip-address-2025-01-15.md) -- Covers the California state court split on CIPA § 638.51 pen register claims and the threshold question of whether IP address collection qualifies; directly related to the Popa standing analysis.
- [reports/privacy/litigation/california-cipa-pen-register-mirmalek-la-times-2024-06-10.md](../litigation/california-cipa-pen-register-mirmalek-la-times-2024-06-10.md) -- Prior N.D. Cal. ruling on CIPA pen register claims against a news website; same defendant class and legal theory as USA Today litigation.
- [reports/privacy/litigation/california-cipa-chat-wiretapping-garcia-v-buildcom-2024-04-17.md](../litigation/california-cipa-chat-wiretapping-garcia-v-buildcom-2024-04-17.md) -- California CIPA § 631 wiretapping claims in the chat context; standing doctrine issues closely related to Popa.
- [reports/privacy/litigation/california-pharma-pixel-class-certification-2025-03-13.md](../litigation/california-pharma-pixel-class-certification-2025-03-13.md) -- Pharma-sector pixel tracking class certification; illustrates the sensitive-data context where standing arguments are harder for defendants.

## Sources

1. [Popa v. Microsoft Corporation, No. 24-14 (9th Cir. Aug. 26, 2025) — Official Opinion](https://cdn.ca9.uscourts.gov/datastore/opinions/2025/08/26/24-14.pdf) -- Full published Ninth Circuit opinion establishing the "embarrassing, invasive, or otherwise private information" standard for Article III standing in CIPA cases
2. [Another Court Dismisses Website Privacy Suit for Lack of Article III Standing — Inside Class Actions / Covington & Burling (Apr. 13, 2026)](https://www.insideclassactions.com/2026/04/13/another-court-dismisses-website-privacy-suit-for-lack-of-article-iii-standing/) -- Covington blog post covering the *In re USA Today* N.D. Cal. April 6, 2026 dismissal applying Popa; primary source for the triggering finding
3. [Court Applies Popa to Dismiss CIPA Pen Register Claim for Lack of Article III Standing — Inside Privacy / Covington & Burling](https://www.insideprivacy.com/data-privacy/court-applies-popa-to-dismiss-cipa-pen-register-claim-for-lack-of-article-iii-standing/) -- Covington analysis of an October 2025 district court dismissal applying Popa to CIPA § 638.51 pen register claims
4. [Sensitive Search Terms Not Enough To Establish Article III Standing Under Popa — Inside Class Actions (Apr. 9, 2026)](https://www.insideclassactions.com/2026/04/09/sensitive-search-terms-not-enough-to-establish-article-iii-standing-under-popa/) -- Covington blog post on the April 2026 dismissal of health search term claims under Popa
5. [Maghoney v. Dotdash Media, Inc., No. 3:24-cv-02394 (S.D. Cal. Feb. 23, 2026) — Justia](https://law.justia.com/cases/federal/district-courts/california/casdce/3:2024cv02394/800642/34/) -- Justia docket entry and opinion for Dotdash dismissal; provides case number, court, date, and holding
6. [Popa v. Microsoft Corporation — Ninth Circuit Clarifies Article III Standing Requirements — Vedder Price / JDSupra](https://www.jdsupra.com/legalnews/popa-v-microsoft-corporation-et-al-4416253/) -- Law firm analysis of Popa's holdings and implications for CIPA and internet privacy litigation
7. [Popa v. Microsoft: Pivotal Ninth Circuit Ruling Narrows Wiretap Suits over Web Analytics — Washington Legal Foundation (Oct. 6, 2025)](https://www.wlf.org/2025/10/06/publishing/popa-v-microsoft-pivotal-ninth-circuit-ruling-narrows-wiretap-suits-over-web-analytics/) -- WLF amicus analysis of Popa's significance; explains session-replay technology and standing doctrine interaction
8. [CIPA Standing Roundup: Article III Standing in Pen Register and Trap and Trace Cases Following Popa v. Microsoft — Tyz Law Group](https://www.tyzlaw.com/insights-archive/cipa-standing-roundup) -- Comprehensive roundup of post-Popa district court decisions on CIPA § 638.51 standing; documents the judicial split
9. [Uncertainty Continues in California on CIPA Section 638.51 Claims — Holland & Knight (Feb. 2026)](https://www.hklaw.com/en/insights/publications/2026/02/uncertainty-continues-in-california-on-cipa-section-63851-claims) -- Law firm analysis of the split among N.D. Cal. judges on CIPA standing post-Popa
10. [Website Wiretapping Roundup: 2025 Decisions and Developments — Inside Class Actions (Jan. 27, 2026)](https://www.insideclassactions.com/2026/01/27/2025-website-wiretapping-roundup/) -- Annual roundup of CIPA/wiretapping decisions across 2025; context for the evolving landscape
11. [Major Win in CIPA Case Signals Higher Hurdles for Privacy Plaintiffs — Fisher Phillips](https://www.fisherphillips.com/en/insights/insights/major-win-in-cipa-case-signals-higher-hurdles-for-privacy-plaintiffs) -- Employer-side analysis of Maghoney and its implications for CIPA class action defense strategy
12. [TransUnion LLC v. Ramirez, 594 U.S. 413 (2021) — Supreme Court Opinion](https://www.supremecourt.gov/opinions/20pdf/20-297_4g25.pdf) -- Supreme Court foundational precedent establishing "no concrete harm, no standing" in the class action context
13. [Courts Still Divided on Whether California Privacy Law Applies to Website Tracking — Fisher Phillips](https://www.fisherphillips.com/en/insights/insights/courts-still-divided-on-whether-california-privacy-law-applies-to-website-tracking) -- Summary of four conflicting rulings issued within a 10-day period; illustrates ongoing judicial uncertainty
14. [Website Tracking and Privacy Lawsuits Predicted to Surge in 2026 — Shumaker Loop & Kendrick (Jan. 2026)](https://www.shumaker.com/insight/client-alert-website-tracking-and-privacy-lawsuits-predicted-to-surge-in-2026-practical-steps-to-mitigate-risk/) -- Client alert forecasting continued CIPA litigation volume in 2026 notwithstanding standing barriers
15. [Ninth Circuit Takes Cautious Approach to Privacy and Data Security Standing — IAPP](https://iapp.org/news/a/ninth-circuit-takes-cautious-approach-to-privacy-and-data-security-standing) -- IAPP analysis of the Ninth Circuit's broader post-TransUnion standing jurisprudence in data privacy contexts
