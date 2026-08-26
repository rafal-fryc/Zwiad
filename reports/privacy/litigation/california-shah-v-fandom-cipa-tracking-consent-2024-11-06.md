---
title: "Shah v. Fandom: Online Consent to Third-Party Tracking Under California's CIPA Pen Register Provision"
date: 2024-11-06
jurisdiction: "California"
category: "privacy"
development_type: "litigation"
finding_id: "SCAN-20241106-002"
topic_key: "california-9206cc83-2024"
topic_type: "guidance"
first_reported: 2024-11-06
last_updated: 2026-04-22
status_history:
  - "2026-04-22: Corrected § 638.51(c) characterization in Background section — replaced erroneous 'statutory damages of up to $2,500' with accurate distinction between criminal penalty (§ 638.51(c): up to $2,500 fine and/or county jail) and civil remedy (§ 637.2: $5,000 per violation or treble damages)."
cluster: "CIPA Website Wiretapping Class Actions"
cluster_slug: "cipa-website-wiretapping-litigation"
---

# Shah v. Fandom: Online Consent to Third-Party Tracking Under California's CIPA Pen Register Provision

**Jurisdiction:** California | **Category:** Privacy | **Date:** 2024-11-06

## Executive Summary [MEDIUM confidence]

In *Shah v. Fandom, Inc.*, No. 3:24-cv-01062 (N.D. Cal. 2024), the Northern District of California denied Fandom's motion to dismiss a class action alleging that the gaming website GameSpot.com installed third-party advertising trackers — operated by GumGum, Audiencerate, and TripleLift — on visitors' browsers without their consent, in violation of [California Penal Code § 638.51](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=638.51.) (the California Invasion of Privacy Act's pen register provision). The court held that a user who consents to transmit their IP address to a website operator does not necessarily consent to transmitting that address to unknown third-party trackers, rejecting the argument that mere website visits constitute implied consent to all downstream data flows. The case subsequently settled in December 2025 for $1.2 million, covering California users who visited GameSpot between January 5, 2023 and December 16, 2025. The ruling adds a significant data point to the rapidly evolving body of CIPA pen register case law, in which federal and state courts have reached sharply divergent conclusions about whether routine web tracking technologies violate a 2015 statute originally designed to address telephone surveillance.

## Background [HIGH confidence]

### California's CIPA Pen Register Provision

The California Invasion of Privacy Act (CIPA) has long prohibited wiretapping and eavesdropping on communications. In 2015, the California Legislature added [Penal Code § 638.51](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=638.51.) through [AB 929](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=201520160AB929), effective January 1, 2016. Section 638.51(a) prohibits any person from installing or using a "pen register" or "trap and trace device" without a court order, subject to specified exceptions for communications service providers. [California Penal Code § 638.50](https://law.justia.com/codes/california/code-pen/part-1/title-15/chapter-1-5/section-638-50/) defines "pen register" as "a device or process that records or decodes dialing, routing, addressing, or signaling information transmitted by an instrument or facility from which a wire or electronic communication is transmitted," and "trap and trace device" as "a device or process that captures the incoming electronic or other impulses that identify the originating number or other dialing, routing, addressing, or signaling information reasonably likely to identify the source of a wire or electronic communication."

The pen register provision was enacted in the telephone context and contains no specific provisions addressing online tracking technologies, cookie-based identifiers, or IP address transmission — an omission that has produced widespread litigation uncertainty as plaintiffs have applied the statute to modern web analytics tools.

### The CIPA Litigation Wave

Beginning around 2022 and accelerating through 2024, plaintiffs' firms filed hundreds of putative class actions against websites operating with third-party advertising, analytics, and session-replay tools, alleging those tools function as unauthorized pen registers or trap-and-trace devices under § 638.51. Violations of § 638.51 carry criminal penalties of up to $2,500 per violation under § 638.51(c); in civil class actions, plaintiffs have sought $5,000 per violation (or treble damages, whichever is greater) under § 637.2, which provides a private right of action for CIPA violations. Because class actions can aggregate thousands of individual web sessions, civil exposure amounts can be enormous even for routine website operation.

Federal district courts in California have largely declined to dismiss CIPA § 638.51 claims at the pleading stage, finding that third-party pixels and tracking technologies can plausibly constitute pen registers or trap-and-trace devices within the statute's broad definitional text. California state courts, by contrast, began pushing back in late 2024 and early 2025, with several superior court judges holding that the statute applies only to telephone-number-tracing technology, not internet communications. This state-federal court divergence remained unresolved as of the time of the Shah v. Fandom ruling.

## Detailed Analysis [MEDIUM confidence]

### Factual Background

Plaintiffs Vishal Shah and Jayden Kim filed suit in February 2024 alleging that Fandom, through its website GameSpot.com, caused visitors' browsers to download three third-party tracking programs: the [GumGum Tracker](https://gumgum.com/), the [Audiencerate Tracker](https://audiencerate.com/), and the [TripleLift Tracker](https://www.triplelift.com/). Once installed in a user's browser cache via cookies, each tracker instructed the browser to transmit the user's IP address to the respective third-party company. According to the plaintiffs, the trackers also stored cookies so that repeat visitors to Fandom's site could be identified and tracked over time. The plaintiffs alleged these trackers constituted unauthorized pen registers under CIPA § 638.51(a) and that Fandom was liable for installing them without user consent.

### The Consent Question

Fandom moved to dismiss, arguing primarily that users impliedly consented to the IP address transmissions by voluntarily visiting GameSpot.com, because IP address sharing is a standard and widely understood feature of internet browsing. The court rejected this argument.

Applying the principle that "consent is generally limited to the specific conduct authorized," the court distinguished between two distinct disclosures: (1) a user's transmission of their IP address to Fandom's own servers as a necessary consequence of accessing the website, and (2) the subsequent transmission of that IP address to GumGum, Audiencerate, and TripleLift — third parties with whom the user had no direct relationship. The court held that consenting to the first disclosure does not necessarily encompass consent to the second. As the opinion states: "A user who consents to disclose their IP address…as part of accessing [a] website does not necessarily consent to disclose their IP address to the third parties operating the Trackers." ([Bloomberg Law reporting](https://news.bloomberglaw.com/litigation/users-advance-fandom-pen-register-suit-over-ip-address-sharing))

On the question of implied consent through Fandom's privacy policy or terms of service, the court found the allegations sufficient to proceed: plaintiff Vishal Shah plausibly alleged that he did not anticipate or agree to the disclosure of his IP address to the third-party tracker companies when he visited GameSpot.com. The court found this consistent with the principle that online consent must be specific to the conduct being authorized, not a blanket acceptance of undisclosed downstream data practices.

### The Statutory Scope Holding

The court's opinion also addressed Fandom's policy argument that applying CIPA to standard web tracking imposes unreasonable burdens on ordinary internet operation. The court acknowledged the concern but declined to limit the statute judicially: "To the extent that Fandom believes the statute may impose too many burdens when applied to the realities of modern technologies…the question of whether the statute's scope should be narrowed ultimately rests with the Legislature, not the courts." ([National Law Review](https://natlawreview.com/article/invisible-data-real-consequences-navigating-ip-consent-dilemma))

This passage is significant because it explicitly invites legislative correction rather than judicial narrowing — and the California Legislature subsequently attempted exactly that through SB 690.

### IP Addresses as "Addressing Information"

The court affirmed that IP addresses constitute "addressing information" within CIPA § 638.50's definition of pen register, consistent with how other federal courts in the Northern District of California had previously reasoned. The court found the trackers' function of recording and forwarding IP addresses to third parties was sufficient to survive a motion to dismiss as a plausible pen register use. This holding aligns with the broader federal court trend acknowledging that online tracking technologies collecting addressing information fall within § 638.51's scope.

### Settlement

The case ultimately settled on December 16, 2025, when the court granted preliminary approval of a $1.2 million class settlement. ([Top Class Actions](https://topclassactions.com/lawsuit-settlements/open-lawsuit-settlements/1-2m-gamespot-privacy-class-action-settlement/); [Class Action.org](https://www.classaction.org/news/1.2m-gamespot-cipa-settlement-ends-class-action-lawsuit-over-alleged-use-of-third-party-data-trackers)). The settlement class consists of California residents who visited GameSpot.com between January 5, 2023 and December 16, 2025. A final approval hearing is scheduled for May 19, 2026. Individual class members who submitted timely claims are entitled to a proportionate share of the fund, not to exceed $5,000 per claimant.

## Impact Assessment [MEDIUM confidence]

### Consent Standards for Third-Party Tracking

The central takeaway from *Shah v. Fandom* is that website operators cannot rely on users' general awareness of internet IP transmission to establish consent to third-party tracking. The ruling makes clear that for consent to be legally operative under CIPA, it must be specific to the conduct in question — including identification of which third parties will receive the user's addressing information and for what purposes. A privacy policy that discloses broad data-sharing practices without specifically identifying the tracking technologies involved and their operators may be insufficient to establish CIPA consent.

### Federal-Court Risk Remains Elevated

The *Shah v. Fandom* ruling issued from a federal district court, which denied dismissal. Federal courts in the Northern District have largely maintained this approach through 2024. Companies facing CIPA § 638.51 class actions in federal court face a more hostile environment at the motion-to-dismiss stage than in California state court, where recent decisions in *Sanchez v. Cars.com* and *Aviles v. LiveRamp* have been more defendant-friendly. Companies served with federal CIPA class actions should evaluate removal strategy carefully and monitor the developing state-versus-federal court split. ([Holland & Knight analysis](https://www.hklaw.com/en/insights/publications/2026/02/uncertainty-continues-in-california-on-cipa-section-63851-claims))

### Industry Categories at Elevated Risk

Websites using third-party advertising technology stacks — particularly those embedding pixels from social media platforms (Meta, TikTok), identity resolution vendors (LiveRamp, Oracle), or programmatic advertising intermediaries (GumGum, TripleLift) — face the highest litigation exposure. The settlement in *Shah v. Fandom* demonstrates that even a single defendant's settlement cost can reach seven figures before accounting for legal fees. Companies operating content-rich websites with high California user traffic and advertising-based business models are especially exposed.

### Legislative Landscape: SB 690

The California Legislature introduced [SB 690](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB690) in 2025 as a direct response to CIPA § 638.51 class action proliferation. As introduced, SB 690 would amend CIPA's pen register and trap-and-trace definitions to exclude devices or processes used for a "commercial business purpose" as defined by reference to the California Consumer Privacy Act (CCPA). The California Senate unanimously passed SB 690 in June 2025; however, the bill stalled in the Assembly and did not advance into law before the end of the 2025 legislative session. ([Duane Morris analysis](https://www.duanemorris.com/alerts/california_sb690_stalls_assembly_cipa_liability_remains_least_through_2026_0725.html)). As of April 2026, the bill has not been enacted, and CIPA § 638.51 liability for online tracking remains unchanged. Companies should not assume legislative relief is imminent when making compliance decisions.

### Statutory Damages Exposure

CIPA § 638.51(c) provides for criminal penalties of up to $2,500 per violation. Plaintiffs in civil class actions have also sought $5,000 in statutory damages per violation under CIPA § 637.2, which provides a private right of action for CIPA violations. The *Shah v. Fandom* settlement — $1.2 million for a website-scale class covering more than two years of California user visits — illustrates the settlement leverage available to plaintiffs even when the underlying legal theory faces genuine uncertainty.

## Action Items

- Conduct an inventory of all third-party scripts, pixels, and tracking tags deployed on California-facing web properties, with particular attention to advertising technology vendors and identity resolution services.
- Review existing privacy policies and cookie consent mechanisms to evaluate whether disclosures are specific enough to identify the third parties receiving user IP addresses and the purposes for which those addresses are used.
- For companies relying on a cookie consent banner or pop-up as the primary consent mechanism, assess whether the banner provides specific enough notice about third-party IP transmission to support a CIPA consent defense in federal court.
- Evaluate whether pending CIPA class action matters are better defended in California state court (where recent rulings have been more defendant-friendly) or federal court, and assess removal or remand strategy accordingly.
- Monitor the California Legislature's handling of SB 690 in the 2026 session; track whether the Assembly advances the bill with or without the retroactivity provision that was removed before Senate passage.
- Monitor the final approval hearing in *Shah v. Fandom* scheduled for May 19, 2026, for any judicial commentary on the merits that could affect related pending litigation.

## Related Reports

- [reports/privacy/litigation/california-cipa-pen-register-ip-address-2025-01-15.md](reports/privacy/litigation/california-cipa-pen-register-ip-address-2025-01-15.md) — Companion ruling from California state courts (*Sanchez v. Cars.com* and *Aviles v. LiveRamp*) reaching the opposite result from *Shah v. Fandom* on whether § 638.51 applies to IP address collection, illustrating the state-federal court divergence.
- [reports/privacy/litigation/california-cipa-pen-register-mirmalek-la-times-2024-06-10.md](reports/privacy/litigation/california-cipa-pen-register-mirmalek-la-times-2024-06-10.md) — Earlier N.D. Cal. ruling declining to remand a CIPA pen register class action, part of the same CIPA Website Wiretapping Class Actions cluster.
- [reports/privacy/litigation/california-cipa-chat-wiretapping-cody-v-boscov-2024-05-23.md](reports/privacy/litigation/california-cipa-chat-wiretapping-cody-v-boscov-2024-05-23.md) — Related CIPA wiretapping litigation targeting website chat features under CIPA's eavesdropping provisions rather than § 638.51, showing parallel litigation theories applied to similar tracking contexts.

## Sources

1. [California Penal Code § 638.51 (leginfo.legislature.ca.gov)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=638.51.) — Official text of the pen register prohibition at issue in Shah v. Fandom
2. [California Penal Code § 638.50 (Justia)](https://law.justia.com/codes/california/code-pen/part-1/title-15/chapter-1-5/section-638-50/) — Official definitions of "pen register" and "trap and trace device"
3. [AB 929 (2015) — Pen registers: authorized use (leginfo.legislature.ca.gov)](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=201520160AB929) — Enacting legislation adding § 638.51 to the California Penal Code
4. [Online Consent to Tracking Software Under California Law: Shah v. Fandom — Loeb & Loeb LLP (Lexology)](https://www.lexology.com/library/detail.aspx?g=82fbfa9c-ad69-4a01-941e-023f15d471bd) — Primary law firm analysis of the N.D. Cal. ruling and its consent analysis
5. [Online Consent to Tracking Software Under California Law: Shah v. Fandom — Loeb & Loeb LLP (QuickTakes)](https://quicktakes.loeb.com/post/102jnfa/online-consent-to-tracking-software-under-california-law-a-dive-into-the-shah-v) — Same article, direct publisher URL
6. [Users Advance Fandom 'Pen Register' Suit Over IP Address Sharing (Bloomberg Law)](https://news.bloomberglaw.com/litigation/users-advance-fandom-pen-register-suit-over-ip-address-sharing) — Bloomberg Law reporting on the motion-to-dismiss denial
7. [Shah v. Fandom, Inc., 754 F.Supp.3d 924 (N.D. Cal. 2024) — vLex](https://case-law.vlex.com/vid/shah-v-fandom-inc-1081886503) — Case law database entry for the published opinion
8. [Shah v. Fandom Docket, No. 3:24-cv-01062 (filed Feb. 21, 2024)](https://sunsteinwebdocs.s3.amazonaws.com/documents/Shah-v.-Fandom-Inc.-Docket-No.-3_24-cv-01062-N.D.-Cal.-Feb-21-2024-Court-Docket-1.pdf) — Court docket showing filing details
9. [How Shah v. Fandom, Inc. Could Reshape Consent Online (East West GC)](https://www.eastwestgc.com/post/how-shah-v-fandom-inc-could-reshape-consent-online) — Analysis of consent implications for online businesses
10. [$1.2M GameSpot CIPA Settlement — Class Action.org](https://www.classaction.org/news/1.2m-gamespot-cipa-settlement-ends-class-action-lawsuit-over-alleged-use-of-third-party-data-trackers) — Settlement reporting with class definition and timeline
11. [GameSpot CIPA Settlement — Top Class Actions](https://topclassactions.com/lawsuit-settlements/open-lawsuit-settlements/1-2m-gamespot-privacy-class-action-settlement/) — Settlement details, eligibility, and claim filing information
12. [GameSpot Settlement Website FAQ (gamespotsettlement.com)](https://www.gamespotsettlement.com/Home/FAQ) — Official settlement website with court-approved claim information
13. [INVISIBLE DATA, REAL CONSEQUENCES: Navigating the IP Consent Dilemma (National Law Review)](https://natlawreview.com/article/invisible-data-real-consequences-navigating-ip-consent-dilemma) — Analysis of the CIPA consent framework including Shah v. Fandom statutory scope holding
14. [Uncertainty Continues in California on CIPA Section 638.51 Claims (Holland & Knight)](https://www.hklaw.com/en/insights/publications/2026/02/uncertainty-continues-in-california-on-cipa-section-63851-claims) — 2026 analysis of the state-federal court divergence and outstanding legal uncertainty
15. [Developments in Digital Privacy Litigation in 2024–2025: CIPA, VPPA, and SB 690 (Coblentz Law)](https://www.coblentzlaw.com/news/developments-in-digital-privacy-litigation-in-2024-2025-cipa-vppa-and-californias-sb-690/) — Comprehensive survey of CIPA litigation landscape and SB 690 legislative background
16. [California SB 690 Stalls in Assembly — CIPA Liability Remains Through 2026 (Duane Morris)](https://www.duanemorris.com/alerts/california_sb690_stalls_assembly_cipa_liability_remains_least_through_2026_0725.html) — Status of SB 690 and compliance implications of its failure to advance
17. [SB 690 — California Legislative Information (leginfo.legislature.ca.gov)](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB690) — Official California Legislature bill page for SB 690
18. [California's Invasion of Privacy Act: A New Frontier for Website Tracking Litigation (ABA Business Law Today)](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-august/californias-invasion-privacy-act/) — ABA overview of CIPA pen register litigation wave and legal background
19. [Pen Register and Trap and Trace Claims: The Latest Wave of CIPA Litigation (K&L Gates)](https://www.klgates.com/Pen-Register-and-Trap-and-Trace-Claims-The-Latest-Wave-of-CIPA-Litigation-3-4-2024) — Law firm analysis of the early litigation wave and statutory interpretation debates
20. [Court Holds CIPA's Pen Register Provision Does Not Impose Liability for "What Makes the Internet Possible" (Global Policy Watch)](https://www.globalpolicywatch.com/2024/12/court-holds-cipas-pen-register-provision-does-not-impose-liability-for-what-makes-the-internet-possible/) — Analysis of contrasting state court rulings limiting § 638.51 scope
