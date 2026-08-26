---
title: "California State Courts Hold CIPA Pen Register Provision Does Not Prohibit IP Address Collection"
date: 2025-01-15
jurisdiction: "California"
category: "privacy"
development_type: "court-decision"
finding_id: "SCAN-20250115-026"
topic_key: "california-d6a3b96b-2025"
topic_type: "enforcement"
first_reported: 2025-01-15
last_updated: 2026-04-16
status_history:
  - "2026-04-16: R1 revision — corrected Aviles court to Los Angeles County Superior Court (Stanley Mosk Courthouse); removed misdated Inside Class Actions Jan. 10 2025 citation from Sanchez analysis; corrected Popa description to reference Pennsylvania WESCA; replaced unverifiable '1,500+' figure with figures actually stated in K&L Gates article."
  - "2026-04-16: R2 revision -- corrected Ninth Circuit Popa citation from 'Popa v. Harriet Carter Gifts, Inc.' (Third Circuit/Pennsylvania WESCA, 2022) to 'Popa v. Microsoft Corporation, No. 24-14 (9th Cir. Aug. 26, 2025)'; updated parenthetical to reflect session-replay/wiretapping law context; updated Sources entry 13 accordingly."
cluster: "CIPA Website Wiretapping Class Actions"
cluster_slug: "cipa-website-wiretapping-litigation"
---

# California State Courts Hold CIPA Pen Register Provision Does Not Prohibit IP Address Collection

**Jurisdiction:** California | **Category:** Privacy | **Date:** 2025-01-15

## Executive Summary [HIGH confidence]

In January 2025, two California superior courts issued back-to-back decisions rejecting the application of the California Invasion of Privacy Act's (CIPA) pen register provision — [Penal Code § 638.51](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=638.51.) — to the collection of IP addresses by website tracking technologies. In *Sanchez v. Cars.com Inc.*, 2025 WL 487194 (Cal. Super. Ct. Jan. 27, 2025), Judge Tiana J. Murillo sustained the defendant's demurrer without leave to amend, concluding that § 638.51 applies only to telephone-number-tracing technology, not internet communications. One day later, in *Aviles v. LiveRamp, Inc.*, 2025 WL 487196 (Cal. Super. Ct. Jan. 28, 2025), Judge Joseph Lipner reached a similar result, dismissing claims because the plaintiff failed to allege the website tool collected "outgoing addressing information from visitors' devices." These rulings are particularly significant because they add to a growing body of California state court decisions rejecting CIPA § 638.51 claims — creating a sharp divergence from federal district courts, which have largely upheld the same claims at the pleading stage. The decisions provide meaningful, if still incomplete, relief for businesses facing dozens of copycat CIPA lawsuits challenging routine website tracking practices.

## Background [HIGH confidence]

### CIPA's Pen Register Provision

California enacted the California Invasion of Privacy Act in 1967 to prohibit law enforcement eavesdropping on telephone communications. The pen register provisions, codified at [California Penal Code §§ 638.50–638.55](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=638.51.), were added effective January 1, 2016, through Assembly Bill 929, tracking the federal Pen Register Act almost verbatim. Under [§ 638.51(a)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=638.51.), "a person may not install or use a pen register or a trap and trace device without first obtaining a court order." The statute defines "pen register" under [§ 638.50(b)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=638.50.) as "a device or process that records or decodes dialing, routing, addressing, or signaling information transmitted by an instrument or facility from which a wire or electronic communication is transmitted, but not the contents of a communication." CIPA authorizes private plaintiffs and provides for statutory damages of $5,000 per violation under [§ 638.55](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=638.55.).

### The CIPA Pen Register Litigation Wave

Beginning around 2023, plaintiff's firms began asserting novel theories applying CIPA's pen register provisions to ordinary website tracking tools — including advertising pixels (e.g., Meta Pixel, TikTok Pixel), JavaScript tags, analytics beacons, and audience segmentation software. The theory: when a user visits a website, these tools collect the visitor's IP address and transmit it to third parties, which plaintiffs argue qualifies as recording "routing" or "addressing" information under § 638.50(b). As analyzed by [K&L Gates (March 2024)](https://www.klgates.com/Pen-Register-and-Trap-and-Trace-Claims-The-Latest-Wave-of-CIPA-Litigation-3-4-2024), "scores of class action and individual lawsuits" were filed on this theory, with one firm alone filing over 120 such actions in the months following *Greenley*. Statutory damages of $5,000 per website visitor create potential class-wide exposure in the billions of dollars for large-traffic websites.

The litigation wave was ignited by *Greenley v. Kochava, Inc.* (S.D. Cal. 2023), the first federal decision to uphold a CIPA § 638.51 claim, where the court held that software "that identifies consumers, gathers data, and correlates that data through unique 'fingerprinting'" qualifies as a pen register. Subsequent federal district court decisions in California largely followed *Greenley*, applying the statute's "plain language" broadly to internet technologies. However, California state courts — where CIPA's statutory damages and procedural rules make plaintiff forum selection attractive — began reaching markedly different conclusions.

### The State Court vs. Federal Court Interpretive Split

By late 2024 and into 2025, a sharp interpretive divergence had formed. As documented by [Holland & Knight (February 2026)](https://www.hklaw.com/en/insights/publications/2026/02/uncertainty-continues-in-california-on-cipa-section-63851-claims):

- **California state courts** have generally adopted a narrower interpretation, focusing on CIPA's legislative history to conclude that § 638.51's pen register provisions are confined to telephone-number-tracing technology and do not extend to internet communications or IP address collection by websites.
- **Federal district courts** (applying California law) have largely held the opposite — that the statute's plain text is broad enough to encompass website tracking tools that collect IP addresses or other routing/addressing information.

This divergence created a strategic forum-selection incentive: plaintiffs preferred state court for substantive law advantages (or, from a defendant's perspective, federal court was more favorable on the merits). Related CIPA litigation on wiretapping theories under §§ 631 and 632.7 has followed a similar pattern, as detailed in companion reports.

## Detailed Analysis [HIGH confidence]

### Sanchez v. Cars.com Inc. (Cal. Super. Ct. Jan. 27, 2025)

The plaintiff Monica Sanchez — described in commentary as a "tester" plaintiff — alleged that Cars.com unlawfully installed a pen register on its website by embedding a tracking beacon that sent website visitors' IP addresses to the beacon's software provider. She asserted that the beacon constituted a pen register under § 638.51.

Judge Murillo of the Los Angeles County Superior Court sustained Cars.com's demurrer **without leave to amend** — the most adverse outcome possible for a plaintiff, meaning the court found no viable amended pleading could cure the defect. The court analyzed the "plain language and legislative intent" of CIPA to determine whether internet communications constitute pen registers. Key holdings:

1. **Telephone technology, not internet technology**: Drawing on legislative history, Judge Murillo concluded that, like the federal Pen Register Act upon which California's provision was modeled, the statute "applied only to mechanical, telephone number-tracing technology, not technology used to collect the IP address from a desktop computer." Because the California legislature adopted the federal authorization provision verbatim, the court held it intended the same limited scope.

2. **No reasonable expectation of privacy in IP addresses**: The court rejected the premise underlying the plaintiffs' theory, finding that website visitors have no reasonable expectation of privacy in their computers' IP addresses because sharing an IP address is "a basic function of accessing the internet."

3. **No leave to amend**: By sustaining without leave to amend, the court signaled that the defect was legal — not factual — and that no set of additional allegations could convert Cars.com's use of routine website tracking into a pen register violation. As analyzed by [Inside Class Actions (March 12, 2025)](https://www.insideclassactions.com/2025/03/12/courts-hold-cipas-pen-register-provision-does-not-apply-to-internet-communications-or-to-alleged-data-collection-about-visitors-devices-from-visitors-devices/), the full decision is publicly available at [fkks.com/uploads/news/Sanchez_v._Cars_.com_.pdf](https://fkks.com/uploads/news/Sanchez_v._Cars_.com_.pdf).

### Aviles v. LiveRamp, Inc. (Cal. Super. Ct. Jan. 28, 2025)

The plaintiff similarly alleged that LiveRamp — an audience segmentation and data connectivity company — unlawfully installed a pen register by embedding a beacon on websites that sent visitors' IP addresses to LiveRamp's servers.

Judge Lipner of the Los Angeles County Superior Court (Stanley Mosk Courthouse) sustained LiveRamp's demurrer **with leave to amend**, meaning the plaintiff was permitted to try again. The court's analysis focused on pleading adequacy rather than a categorical ruling that IP address collection can never violate § 638.51:

1. **Pen register prong**: Judge Lipner held the plaintiff failed to adequately allege use of a pen register because he did not plead that the website technology "collect[ed] the outgoing addressing information from visitors' devices or browsers." The court's framing — focusing on "outgoing" information from the user's device — signals that a properly pleaded claim would need to allege collection of information leaving the visitor's device, not merely information about the visitor's device that the server receives.

2. **Trap and trace prong**: The court separately found the plaintiff failed to plead a trap and trace device claim because he did not allege "that Defendant installed software on Plaintiff's device or browser that collected incoming contact information to Plaintiff's device."

3. **Distinction from Sanchez**: The *Aviles* dismissal is narrower than *Sanchez*. Because leave to amend was granted, the *Aviles* court left open the possibility that a more precisely drawn complaint — one that alleges a beacon actually installed on the visitor's device and collecting outgoing addressing data — could survive demurrer.

### Broader State Court Pattern

The *Sanchez* and *Aviles* decisions are part of an accelerating trend in California state courts. As detailed by [Inside Class Actions (March 12, 2025)](https://www.insideclassactions.com/2025/03/12/courts-hold-cipas-pen-register-provision-does-not-apply-to-internet-communications-or-to-alleged-data-collection-about-visitors-devices-from-visitors-devices/), subsequent California state court rulings in early 2025 further entrenched the view that CIPA's pen register provision does not apply to internet communications or to alleged data collection "about visitors' devices, from visitors' devices."

At the same time, federal decisions have continued to cut the other way. In *Carol Lesh v. Cable News Network, Inc.*, No. 24 CIV. 03132 (S.D.N.Y. Feb. 20, 2025), a federal court denied CNN's motion to dismiss CIPA § 638.51 claims, recognizing that online tracking technologies collecting IP addresses may fall under California's pen register law. This geographic split — California state courts dismissing, federal courts allowing — is now the defining feature of the litigation landscape as analyzed by [Holland & Knight (February 2026)](https://www.hklaw.com/en/insights/publications/2026/02/uncertainty-continues-in-california-on-cipa-section-63851-claims).

### Ninth Circuit Popa Decision and Standing Overlay

An additional layer was added in August 2025, when the Ninth Circuit issued its decision in *[Popa v. Microsoft Corporation, No. 24-14 (9th Cir. Aug. 26, 2025)](https://law.justia.com/cases/federal/appellate-courts/ca9/24-14/24-14-2025-08-26.html)*, holding that plaintiffs asserting privacy violations under state wiretapping and privacy statutes must demonstrate a concrete injury-in-fact for Article III standing — mere statutory violation is insufficient. *Popa v. Microsoft Corporation* involved session-replay claims on a third-party website under Washington state and federal wiretapping law (not California law), but the Ninth Circuit's Article III standing analysis has been applied to CIPA § 638.51 claims in federal proceedings. As reported by [Inside Class Actions (October 23, 2025)](https://www.insideclassactions.com/2025/10/23/court-applies-popa-to-dismiss-cipa-pen-register-claim-for-lack-of-article-iii-standing/), courts began applying *Popa* to dismiss CIPA pen register claims for lack of standing, adding another defense ground for federal court defendants even where substantive law favored plaintiffs.

### Legislative Response: California SB 690

Amid the litigation surge, the California Legislature introduced [Senate Bill 690](https://www.beneschlaw.com/resources/updates-on-cipa-reform-ca-sb-690-progresses-to-the-assembly-without-a-private-right-of-action.html), which would amend CIPA to exempt the use of website tracking technologies serving a "commercial business purpose," provided they comply with existing privacy laws such as the CCPA. The Senate passed SB 690 unanimously in June 2025. However, as reported by [Duane Morris (July 2025)](https://www.duanemorris.com/alerts/california_sb690_stalls_assembly_cipa_liability_remains_least_through_2026_0725.html), the bill stalled in the Assembly after its sponsor paused it due to "outstanding concerns around consumer privacy." SB 690 is now a two-year bill, meaning CIPA § 638.51 liability remains fully intact at least through 2026.

## Impact Assessment [MEDIUM confidence]

### For Website Operators

The *Sanchez* and *Aviles* decisions are favorable for website operators facing CIPA pen register demands or litigation, but the relief is partial and jurisdiction-dependent:

- **State court advantage**: Where CIPA pen register actions are filed and remain in California state court, the growing line of state trial court decisions holding the statute inapplicable to IP address collection provides a strong demurrer basis. The *Sanchez* demurrer sustained without leave to amend is the strongest precedent for a categorical defense.
- **Federal court risk persists**: Operators removed to federal court (or sued in federal court) face substantially greater risk, as the overwhelming majority of federal judges apply § 638.51 broadly to website tracking tools. The *Popa* standing doctrine provides an additional potential defense, but does not eliminate substantive exposure.
- **Forum uncertainty**: The state/federal split means the outcome of CIPA pen register litigation remains highly forum-dependent, and defendants cannot rely on the state court decisions to insulate them from all exposure.

### Industries Most Affected

The following industries face heightened exposure given typical reliance on third-party tracking tools:

- **Media and publishing**: Advertising-supported websites with high California traffic (illustrated by the *Mirmalek v. Los Angeles Times* settlement of $3.85 million).
- **E-commerce and auto**: *Sanchez v. Cars.com* demonstrates that lead-generation and marketplace platforms with embedded tracking beacons are targeted.
- **Ad tech and data connectivity**: Companies like LiveRamp that provide audience segmentation and data connectivity services are directly in the crosshairs as the alleged installer of the pen register.
- **Healthcare**: Dozens of health system and pharmacy websites have faced CIPA pixel claims; the pen register theory is a secondary theory in many of these cases.

### Compliance Implications

Website operators cannot confidently rely solely on the state court decisions given the federal court divergence. Best practice compliance steps remain the same as before *Sanchez* and *Aviles*:

- Implement a consent management platform (CMP) that blocks third-party tracking tags absent user consent.
- Conduct a full third-party tag audit to identify any pixel, beacon, or SDK that captures and transmits IP addresses or device identifiers to external parties.
- Review privacy notices to ensure disclosures align with actual data flows.
- Monitor the SB 690 legislative track in 2026 for potential statutory safe harbor.

### Litigation Risk Outlook

Despite favorable state court decisions, the structural litigation risk remains significant:

- Statutory damages of $5,000 per violation mean large-traffic websites face theoretically enormous class exposure even with low success rates at trial.
- The *Popa* standing requirement adds a litigation hurdle but is more relevant in federal court than state court.
- Plaintiff firms continue filing new CIPA pen register complaints; the volume of new filings shows no sign of abating despite adverse state court decisions, as plaintiffs can seek federal court venues or attempt to replead under the *Aviles* framework (which left the door open for adequately pleaded complaints).

## Action Items

- **Audit third-party tags**: Identify every pixel, beacon, JavaScript tag, and SDK on California-facing websites that captures visitors' IP addresses or device identifiers and transmits them to third parties. Determine whether any tag could be characterized as a "pen register" under either the broad federal interpretation or the narrower state court test.
- **Implement consent gating**: Configure consent management platforms to block advertising, analytics, and data management tags for California users absent affirmative consent. This provides the most robust defense against § 638.51 claims regardless of how the state/federal split resolves.
- **Evaluate forum strategy**: If a CIPA pen register complaint is received, promptly assess removal eligibility under CAFA (28 U.S.C. § 1332(d)). Federal forum carries greater substantive legal risk but may have procedural advantages; state forum now offers stronger precedent for dismissal but requires CAFA analysis.
- **Preserve litigation documents**: Retain server logs, analytics data, and third-party tag configuration records. This evidence is relevant both to CAPA jurisdiction disputes and to substantive pen register analysis.
- **Monitor SB 690 in 2026**: Track the two-year bill's progress. If enacted, SB 690 would create a commercial-purpose exemption that would substantially reduce CIPA § 638.51 exposure for standard website analytics and advertising.
- **Watch for Ninth Circuit guidance**: The Circuit has not directly ruled on whether § 638.51 applies to website IP address collection. A published Ninth Circuit decision would be highly persuasive — and potentially controlling in federal court — and could either entrench or unify the current split.

## Related Reports

- [reports/privacy/litigation/california-cipa-pen-register-mirmalek-la-times-2024-06-10.md](/home/rafal/projecty/Zwiad/reports/privacy/litigation/california-cipa-pen-register-mirmalek-la-times-2024-06-10.md) — Companion report covering CAFA removal strategy in CIPA § 638.51 pen register class actions; includes the $3.85M LA Times settlement and analysis of the state/federal interpretive split.
- [reports/privacy/litigation/california-cipa-punitive-damages-attorney-fees-2024-07-24.md](/home/rafal/projecty/Zwiad/reports/privacy/litigation/california-cipa-punitive-damages-attorney-fees-2024-07-24.md) — Earlier California court ruling addressing punitive damages and attorney fees in CIPA pen register cases; directly related statute and litigation context.
- [reports/privacy/litigation/california-cipa-chat-wiretapping-garcia-v-buildcom-2024-04-17.md](/home/rafal/projecty/Zwiad/reports/privacy/litigation/california-cipa-chat-wiretapping-garcia-v-buildcom-2024-04-17.md) — Federal dismissal of CIPA § 631 wiretapping claims over website chat technology; companion litigation wave under same statute.

## Sources

1. [California Court Holds CIPA's Pen Register Provision Does Not Prohibit Collection of IP Addresses (Rodriguez v. Plivo Inc.) — Inside Class Actions (Jan. 10, 2025)](https://www.insideclassactions.com/2025/01/10/another-california-court-holds-cipas-pen-register-provision-does-not-prohibit-the-collection-of-ip-addresses/) — Covers an October 2024 California state court ruling in Rodriguez v. Plivo Inc., a predecessor decision in the same line of CIPA pen register cases. Published 17 days before the Sanchez ruling and does not cover that case.
2. [Courts Hold CIPA's Pen Register Provision Does Not Apply to Internet Communications — Inside Class Actions (Mar. 12, 2025)](https://www.insideclassactions.com/2025/03/12/courts-hold-cipas-pen-register-provision-does-not-apply-to-internet-communications-or-to-alleged-data-collection-about-visitors-devices-from-visitors-devices/) — Primary post-decision analysis covering Sanchez v. Cars.com, Aviles v. LiveRamp, and subsequent state court rulings through early 2025.
3. [Sanchez v. Cars.com — Full Superior Court Decision (PDF)](https://fkks.com/uploads/news/Sanchez_v._Cars_.com_.pdf) — Official superior court order in Sanchez v. Cars.com (Cal. Super. Ct. Los Angeles Co. Jan. 27, 2025).
4. [Uncertainty Continues in California on CIPA Section 638.51 Claims — Holland & Knight (Feb. 2026)](https://www.hklaw.com/en/insights/publications/2026/02/uncertainty-continues-in-california-on-cipa-section-63851-claims) — Comprehensive overview of the state vs. federal court interpretive split on CIPA pen registers through early 2026.
5. [California Penal Code § 638.51 — California Legislative Information (official text)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=638.51.) — Official statutory text of the pen register prohibition.
6. [California Penal Code § 638.50 — California Legislative Information (official text)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=638.50.) — Official statutory definition of "pen register" under CIPA.
7. [Pen Register and Trap and Trace Claims: The Latest Wave of CIPA Litigation — K&L Gates (March 2024)](https://www.klgates.com/Pen-Register-and-Trap-and-Trace-Claims-The-Latest-Wave-of-CIPA-Litigation-3-4-2024) — Industry analysis of the CIPA pen register litigation surge; notes "scores of class action and individual lawsuits" and one firm filing over 120 actions.
8. [Recent California State Court Wins for Defendants in Website Tracking Cases — FKKS (Lexology)](https://www.lexology.com/library/detail.aspx?g=cd76ca22-a61b-46e2-a619-9c25a2e109a4) — Analysis of Sanchez, Aviles, and related California state court defense victories.
9. [Collecting IP Addresses? "Not An Invasion of Privacy," Says New York Federal Court in CIPA Pen-Register Action — Mayer Brown (Feb. 2025)](https://www.mayerbrown.com/en/insights/publications/2025/02/collecting-ip-addresses-not-an-invasion-of-privacy-says-new-york-federal-court-in-cipa-pen-register-action) — Covers the Gabrielli v. Insider federal dismissal for lack of standing; provides contrast with the Lesh/CNN ruling.
10. [Old Law, New World: CIPA's Pen Register Provision and the Internet in Federal Court — American Bar Association](https://www.americanbar.org/groups/litigation/resources/newsletters/class-actions-derivative-suits/old-law-new-world-california-invasion-of-privacy-act-pen-register-provision/) — Legal analysis of federal court application of CIPA to internet tracking technologies; surveys the interpretive divergence.
11. [California SB 690 Stalls in Assembly — Duane Morris (July 2025)](https://www.duanemorris.com/alerts/california_sb690_stalls_assembly_cipa_liability_remains_least_through_2026_0725.html) — Documents SB 690's failure to advance in the Assembly; confirms CIPA § 638.51 liability through at least 2026.
12. [Updates on CIPA Reform: CA SB 690 Progresses to the Assembly — Benesch Friedlander (2025)](https://www.beneschlaw.com/resources/updates-on-cipa-reform-ca-sb-690-progresses-to-the-assembly-without-a-private-right-of-action.html) — Details of SB 690's commercial business purpose exemption and legislative history.
13. [Court Applies Popa to Dismiss CIPA Pen Register Claim for Lack of Article III Standing — Inside Class Actions (Oct. 23, 2025)](https://www.insideclassactions.com/2025/10/23/court-applies-popa-to-dismiss-cipa-pen-register-claim-for-lack-of-article-iii-standing/) — Documents courts applying the Ninth Circuit's *Popa v. Microsoft Corporation, No. 24-14 (9th Cir. Aug. 26, 2025)* Article III standing analysis to CIPA § 638.51 pen register claims; standing overlay for federal court defendants.
14. [2025 California Code, Penal Code § 638.51 — Justia](https://law.justia.com/codes/california/code-pen/part-1/title-15/chapter-1-5/section-638-51/) — Secondary statutory text source (Justia annotated version with case citations).
15. [Developments in Digital Privacy Litigation in 2024–2025: CIPA, VPPA, and California's SB 690 — Coblentz Law](https://www.coblentzlaw.com/news/developments-in-digital-privacy-litigation-in-2024-2025-cipa-vppa-and-californias-sb-690/) — Comprehensive 2024–2025 litigation survey including CIPA pen register trends and SB 690 background.
