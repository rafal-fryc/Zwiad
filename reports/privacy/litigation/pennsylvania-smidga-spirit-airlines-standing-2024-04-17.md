---
title: "W.D. Pa. Dismisses Session Replay Wiretap Class Action Against Spirit Airlines for Lack of Article III Standing"
date: 2024-04-17
jurisdiction: "Pennsylvania"
category: "privacy"
development_type: "court-decision"
finding_id: "SCAN-20240417-020"
topic_key: "pa-spirit-airlines-standing-2024"
topic_type: "litigation"
first_reported: 2024-04-17
last_updated: 2026-04-15
status_history:
  - date: 2026-04-15
    note: "Corrected plaintiff names (Malinda S. Smidga, Frances Curd, Kayla Mandeng); added CIPA claims for Mandeng; corrected credit card allegation attribution to Mandeng; fixed Third/Ninth Circuit case attribution (Cook v. GameStop = 3d Cir.; Popa v. Microsoft = 9th Cir.)."
cluster: "CIPA Website Wiretapping Class Actions"
cluster_slug: "cipa-website-wiretapping-litigation"
---

# W.D. Pa. Dismisses Session Replay Wiretap Class Action Against Spirit Airlines for Lack of Article III Standing

**Jurisdiction:** Pennsylvania, Federal | **Category:** Privacy | **Date:** 2024-04-17

## Executive Summary [HIGH confidence]

On April 5, 2024, Judge Marilyn J. Horan of the U.S. District Court for the Western District of Pennsylvania dismissed a putative class action alleging that Spirit Airlines violated state wiretapping and privacy laws by deploying session replay software on its website. In [*Smidga v. Spirit Airlines, Inc.*, No. 2:22-cv-01578-MJH (W.D. Pa. Apr. 5, 2024)](https://law.justia.com/cases/federal/district-courts/pennsylvania/pawdce/2:2022cv01578/293758/80/), the court granted Spirit Airlines' Rule 12(b)(1) motion to dismiss, holding that none of the three named plaintiffs -- Malinda S. Smidga, Frances Curd, and Kayla Mandeng -- alleged a concrete injury sufficient to establish Article III standing. After plaintiffs declined to amend their complaint, the court dismissed the action for lack of subject matter jurisdiction. The decision is significant as part of a growing body of federal court rulings holding that the mere collection of anonymized browsing data through session replay technology does not constitute a cognizable injury under Article III, even where state wiretapping statutes may have been violated.

## Background [HIGH confidence]

### Session Replay Technology

Session replay software is a category of web analytics tools that tracks and records website visitors' browsing behavior, including mouse movements, clicks, keystrokes, scroll patterns, and page navigation. Companies deploy these tools -- typically implemented as JavaScript code snippets embedded in website pages -- to analyze user experience, optimize website design, and create personalized marketing content. The technology has become widespread across the e-commerce industry, generating significant privacy litigation.

### The Smidga Litigation

The putative class action was filed in November 2022 by plaintiffs Malinda S. Smidga, Frances Curd, and Kayla Mandeng against Spirit Airlines in the Western District of Pennsylvania. The plaintiffs alleged that Spirit Airlines procured third-party vendors to embed JavaScript code on its website, which deployed on each visitor's internet browser for the purpose of intercepting and recording electronic communications in real time. According to the complaint, website visitors did not realize Spirit was viewing and recording their mouse movements, clicks, keystrokes, and other browsing activity to create full session replays of their visits. See [Top Class Actions, Spirit class action claims airline wiretaps electronic communications](https://topclassactions.com/lawsuit-settlements/privacy/spirit-class-action-claims-airline-wiretaps-electronic-communications-of-website-visitors/).

The case involved a consolidation of related actions: Mandeng had originally filed a separate action in the Southern District of California (No. 3:23-cv-00233) before the matters were consolidated in the Western District of Pennsylvania.

### Statutory Framework

Each named plaintiff brought claims under statutes corresponding to her state of residence:

- **Malinda S. Smidga (Pennsylvania):** Claims under the **Pennsylvania Wiretapping and Electronic Surveillance Control Act (WESCA)**, [18 Pa. C.S. sections 5701-5782](https://www.legis.state.pa.us/WU01/LI/LI/CT/HTM/18/00.057..HTM) -- Pennsylvania's all-party consent wiretapping statute -- and invasion of privacy under Pennsylvania common law (intrusion upon seclusion).
- **Frances Curd (Maryland):** Claims under the **Maryland Wiretapping and Electronic Surveillance Act (MESA)** -- Maryland's analogous all-party consent wiretap statute -- and invasion of privacy under Maryland common law.
- **Kayla Mandeng (California):** Claims under the **California Invasion of Privacy Act (CIPA)**, Cal. Penal Code §§ 630-638.55 -- California's broad electronic privacy statute covering wiretapping and eavesdropping.

The choice of multiple state wiretapping statutes reflected the residency of the named plaintiffs across different jurisdictions. All three statutes prohibit the interception of electronic communications without the consent of all parties.

### Post-TransUnion Standing Landscape

The Supreme Court's 2021 decision in [*TransUnion LLC v. Ramirez*, 594 U.S. 413 (2021)](https://www.supremecourt.gov/opinions/20pdf/20-297_4g25.pdf) fundamentally reshaped Article III standing doctrine for statutory violations. The Court held that a plaintiff must demonstrate a concrete injury to have standing to pursue damages in federal court, even where a statute has been violated. Critically, the Court ruled that for intangible harms, the alleged injury must bear a "close relationship to a harm traditionally recognized" in American legal history. This framework has proven particularly consequential in privacy litigation involving session replay technology, where the question of whether data collection without tangible consequences constitutes a concrete harm has divided federal courts.

## Detailed Analysis [HIGH confidence]

### Spirit Airlines' Motion to Dismiss

Spirit Airlines filed a Rule 12(b)(1) motion attacking the plaintiffs' Article III standing on both facial and factual grounds. Spirit argued that: (1) the plaintiffs failed to allege any concrete harm from Spirit's use of session replay software; and (2) no concrete harm actually occurred because the website did not collect personal identifying information from visitors and any data collected was anonymized. See [Duane Morris, Pennsylvania Federal Court Dismisses Data Privacy Class Action Based On Lack Of Standing](https://blogs.duanemorris.com/classactiondefense/2024/04/15/pennsylvania-federal-court-dismisses-data-privacy-class-action-based-on-lack-of-standing/).

### The Court's Standing Analysis

Judge Horan analyzed each plaintiff's allegations individually, applying both facial and factual attacks on jurisdiction:

**Plaintiffs Smidga and Curd** alleged only the collection of basic contact information during their visits to Spirit's website, using only disjunctive "or" statements that did not specifically identify what personal data they actually entered. Critically, neither Smidga nor Curd alleged that she entered credit card information, and neither ultimately completed a purchase during her session. The court found that these allegations did not establish a concrete injury because the plaintiffs did not identify any tangible consequences flowing from the data collection -- no identity theft, no financial loss, no misuse of their information.

**Plaintiff Mandeng** presented a marginally stronger case: she specifically alleged that she "input[ed] the names, addresses and ages of herself and her four (4) children, the departure and arrival locations for her potential trip, and her credit card and billing information" during her visit to Spirit's website. However, the court subjected this claim to a factual attack on standing. Spirit Airlines submitted sworn declarations asserting that its session replay software did not collect or record personalized data, including credit card information, from website visitors. Because Mandeng did not dispute these sworn assertions with contrary evidence, the court found that she too could not survive a factual challenge to Article III standing, even though she had alleged the most specific and sensitive data inputs of the three plaintiffs. See [ClassAction.org -- Order Granting Motion to Dismiss](https://www.classaction.org/media/smidga-et-al-v-spirit-airlines-order-granting-motion-to-dimiss.pdf).

### Precedential Analysis

Judge Horan cited over fifteen recent federal court decisions where courts denied standing in similar session replay and website tracking circumstances. This extensive citation of precedent demonstrated a growing judicial consensus that the mere recording of anonymized browsing data does not satisfy the constitutional standing requirement, particularly in the wake of *TransUnion*. The court's analysis reinforced the principle that a bare statutory violation, without a showing of concrete harm, is insufficient to confer standing in federal court. See [Kilpatrick Townsend, Spirit Airlines defeats wiretapping and invasion of privacy class action](https://ktslaw.com/en/Blog/classaction/2024/4/Spirit-Airlines-defeats-wiretapping-and-invasion-of-privacy).

### Leave to Amend and Final Dismissal

The court granted plaintiffs limited leave to amend their complaint to cure the standing deficiencies. When plaintiffs declined to file an amended complaint, the court entered final dismissal for lack of subject matter jurisdiction.

### Third Circuit Appeal

Plaintiffs noticed an appeal to the Third Circuit on April 23, 2024. This appeal is significant because the Third Circuit had not yet addressed the standing question in the session replay context at the time of the district court's ruling. The outcome could provide binding precedent for the Third Circuit on whether wiretap statute violations arising from session replay technology give rise to Article III standing.

## Impact Assessment [MEDIUM confidence]

### Implications for Session Replay Litigation

This decision is part of a clear trend in federal courts toward dismissing session replay wiretap class actions on standing grounds. The ruling has practical implications for companies that deploy session replay and similar analytics tools on their websites:

1. **Anonymization as a defense:** Spirit Airlines' successful use of sworn declarations establishing that its session replay software collected only anonymized data proved decisive, particularly against plaintiff Mandeng -- who had made the most concrete data-input allegations (including credit card and billing information) among the three plaintiffs. Companies that can demonstrate data anonymization in their session replay implementations have a strong standing defense.

2. **Factual attack strategy:** The court's willingness to evaluate Spirit's factual challenge to standing under Rule 12(b)(1) -- crediting the defendant's sworn assertions about its data practices in the absence of contrary evidence from plaintiffs -- provides a roadmap for defendants to defeat standing at an early stage.

3. **Pleading burden on plaintiffs:** The decision underscores that plaintiffs in session replay cases must allege specific, concrete harms beyond the mere fact that browsing data was collected. General allegations of "interception" of "electronic communications" may not suffice without tying the collection to a tangible injury. Even Mandeng's relatively detailed allegations of entering sensitive data (names, ages of children, credit card information) did not survive Spirit's factual challenge to standing.

4. **Multi-statute strategy limited by standing:** The case illustrates that plaintiffs' strategy of invoking multiple state wiretap statutes (WESCA, MESA, CIPA) based on each named plaintiff's home state residency does not, by itself, resolve the federal constitutional standing problem that applies across all claims brought in federal court.

### Broader Standing Landscape [MEDIUM confidence]

The *Smidga* ruling aligns with subsequent decisions from other circuits addressing session replay standing. The Third Circuit reached a similar conclusion in [*Cook v. GameStop, Inc.*, No. 23-2574 (3d Cir. Aug. 7, 2025)](https://law.justia.com/cases/federal/appellate-courts/ca3/23-2574/23-2574-2025-08-07.html), affirming dismissal of a WESCA session replay class action for lack of Article III standing and holding that mouse clicks and non-sensitive browsing data do not establish a concrete harm analogous to recognized common-law privacy torts. See [Kilpatrick Townsend, Third Circuit affirms the dismissal of session replay class action for lack of Article III standing](https://ktslaw.com/en/Blog/classaction/2025/8/Third-Circuit-affirms-the-dismissal-of-session-replay-class-action-for-lack-of-Article-III-standing); [Duane Morris, Third Circuit Clarifies Standing Requirements for Session Replay Privacy Claims](https://www.duanemorris.com/alerts/third_circuit_clarifies_standing_requirements_session_replay_privacy_claims_0825.html).

Separately, the Ninth Circuit issued a significant parallel ruling in [*Popa v. Microsoft Corp.*, No. 24-14 (9th Cir. Aug. 26, 2025)](https://law.justia.com/cases/federal/appellate-courts/ca9/24-14/24-14-2025-08-26.html), dismissing a WESCA-based session replay class action and holding that a plaintiff must allege a harm "that has traditionally been actionable in our nation's legal system" -- a bare statutory violation does not suffice. The [Hunton Andrews Kurth analysis](https://www.hunton.com/hunton-retail-law-resource/just-browsing-courts-differ-on-whether-website-users-lack-article-iii-standing-for-wiretapping-claims) notes that while courts remain split, the trend since *TransUnion* has favored defendants. However, some courts -- particularly in cases where personally identifiable information or sensitive data was collected -- have found standing, meaning the issue is far from settled.

### State Court Alternative

Critically, Article III standing requirements apply only in federal court. Plaintiffs who cannot establish standing in federal court may refile in state court, where the standing threshold may be lower. This creates a strategic consideration for both plaintiffs' counsel (who may prefer state court) and defendants (who may prefer removal to federal court to invoke the standing defense). CIPA claims are particularly susceptible to this dynamic: a California plaintiff like Mandeng who cannot establish federal Article III standing may pursue CIPA claims in California state court, where standing requirements differ.

## Action Items

- **Companies using session replay software** should document that their implementations anonymize visitor data and do not capture personally identifiable information (PII), sensitive data, or payment card information, as this factual record proved decisive in the *Smidga* motion practice -- even against the plaintiff who specifically alleged entering credit card and billing information.
- **Defense counsel** should evaluate early Rule 12(b)(1) motions in session replay cases, leveraging the growing body of precedent -- including *Smidga*, *Cook v. GameStop* (3d Cir. 2025), and *Popa v. Microsoft* (9th Cir. 2025) -- to challenge standing before discovery.
- **Plaintiffs' counsel** should consider filing session replay wiretap claims in state court where Article III standing requirements do not apply, or ensure complaints include specific, concrete allegations of harm beyond mere data collection. CIPA claims may be particularly viable in California state court.
- **Monitor the Third Circuit appeal** in *Smidga* for potential binding precedent on whether session replay wiretap claims satisfy Article III standing in the Third Circuit, in addition to the Third Circuit's 2025 ruling in *Cook v. GameStop*.
- **Track CIPA developments** given the Ninth Circuit's ruling in *Popa v. Microsoft* and its stated implications for CIPA class actions involving session replay and web-tracking tools.

## Related Reports

- [reports/privacy/illinois-bipa-7th-circuit-retroactivity-2026-04-12.md](reports/privacy/illinois-bipa-7th-circuit-retroactivity-2026-04-12.md) -- Related privacy litigation involving standing and damages issues in state privacy statute enforcement (Illinois BIPA).
- [reports/privacy/enforcement-actions/texas-allstate-arity-tdpsa-enforcement-2026-04-14.md](reports/privacy/enforcement-actions/texas-allstate-arity-tdpsa-enforcement-2026-04-14.md) -- Related enforcement action involving data collection practices and state privacy law enforcement.
- [reports/privacy/doj-vppa-first-circuit-brief-2026-04-12.md](reports/privacy/doj-vppa-first-circuit-brief-2026-04-12.md) -- Related federal appellate privacy litigation involving statutory standing and concrete injury analysis under a federal privacy statute.

## Sources

1. [Justia - Smidga v. Spirit Airlines, Inc., No. 2:2022cv01578, Document 80 (W.D. Pa. 2024)](https://law.justia.com/cases/federal/district-courts/pennsylvania/pawdce/2:2022cv01578/293758/80/) -- Court opinion text from the Western District of Pennsylvania.
2. [Duane Morris - Pennsylvania Federal Court Dismisses Data Privacy Class Action Based On Lack Of Standing](https://blogs.duanemorris.com/classactiondefense/2024/04/15/pennsylvania-federal-court-dismisses-data-privacy-class-action-based-on-lack-of-standing/) -- Primary law firm analysis of the decision (source of the original finding).
3. [Kilpatrick Townsend - Spirit Airlines defeats wiretapping and invasion of privacy class action](https://ktslaw.com/en/Blog/classaction/2024/4/Spirit-Airlines-defeats-wiretapping-and-invasion-of-privacy) -- Detailed law firm analysis covering claims, standing analysis, and leave to amend.
4. [ClassAction.org - Order Granting Motion to Dismiss (PDF)](https://www.classaction.org/media/smidga-et-al-v-spirit-airlines-order-granting-motion-to-dimiss.pdf) -- Full text of the court's order granting the motion to dismiss; primary source for plaintiff-specific standing analysis.
5. [Top Class Actions - Spirit class action claims airline wiretaps electronic communications](https://topclassactions.com/lawsuit-settlements/privacy/spirit-class-action-claims-airline-wiretaps-electronic-communications-of-website-visitors/) -- Background on the original complaint and allegations.
6. [Pennsylvania General Assembly - 18 Pa. C.S. Chapter 57, Wiretapping and Electronic Surveillance](https://www.legis.state.pa.us/WU01/LI/LI/CT/HTM/18/00.057..HTM) -- Official text of the Pennsylvania Wiretapping and Electronic Surveillance Control Act.
7. [Supreme Court - TransUnion LLC v. Ramirez, 594 U.S. 413 (2021)](https://www.supremecourt.gov/opinions/20pdf/20-297_4g25.pdf) -- The foundational Supreme Court decision on Article III standing and concrete injury for statutory violations.
8. [Hunton Andrews Kurth - Courts Differ on Whether Website Users Lack Article III Standing for Wiretapping Claims](https://www.hunton.com/hunton-retail-law-resource/just-browsing-courts-differ-on-whether-website-users-lack-article-iii-standing-for-wiretapping-claims) -- Analysis of the circuit split on standing in session replay cases.
9. [Kilpatrick Townsend - Third Circuit affirms the dismissal of session replay class action (Cook v. GameStop)](https://ktslaw.com/en/Blog/classaction/2025/8/Third-Circuit-affirms-the-dismissal-of-session-replay-class-action-for-lack-of-Article-III-standing) -- Coverage of the Third Circuit's August 7, 2025 ruling in Cook v. GameStop, Inc., No. 23-2574.
10. [Justia - Cook v. GameStop, Inc., No. 23-2574 (3d Cir. Aug. 7, 2025)](https://law.justia.com/cases/federal/appellate-courts/ca3/23-2574/23-2574-2025-08-07.html) -- Third Circuit opinion text affirming dismissal of WESCA session replay class action.
11. [Duane Morris - Third Circuit Clarifies Standing Requirements for Session Replay Privacy Claims](https://www.duanemorris.com/alerts/third_circuit_clarifies_standing_requirements_session_replay_privacy_claims_0825.html) -- Additional law firm analysis of Cook v. GameStop (3d Cir. 2025).
12. [Justia - Popa v. Microsoft Corp., No. 24-14 (9th Cir. Aug. 26, 2025)](https://law.justia.com/cases/federal/appellate-courts/ca9/24-14/24-14-2025-08-26.html) -- Ninth Circuit opinion text dismissing session replay class action (distinct from Cook v. GameStop).
13. [National Law Review - Ninth Circuit Rejects Session Replay Wiretap Class Action (Popa v. Microsoft)](https://natlawreview.com/article/ninth-circuit-dismisses-session-replay-wiretap-case) -- Analysis of the Ninth Circuit's August 26, 2025 ruling in Popa v. Microsoft.
14. [Troutman Pepper - The Intangible Concrete Injury: A 2024 Update of Post-TransUnion Decisions](https://www.troutman.com/insights/the-intangible-concrete-injury-a-2024-update-of-post-transunion-decisions-on-standing-for-data-breach-class-actions/) -- Comprehensive analysis of post-TransUnion standing decisions in data privacy class actions.
