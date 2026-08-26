---
title: "California Federal Court Rejects 'Trap and Trace' Cookie Theory in Rounds v. Development Dimensions International"
date: 2026-04-28
jurisdiction: "California"
category: "privacy"
development_type: "court-decision"
finding_id: "SCAN-20260504-043"
topic_key: "california-58c0d093-2026"
topic_type: "enforcement"
topic_key_confidence: "low"
first_reported: 2026-04-28
last_updated: 2026-05-04
status_history: []
cluster: "CIPA Website Wiretapping Class Actions"
cluster_slug: "cipa-website-wiretapping-litigation"
---

# California Federal Court Rejects 'Trap and Trace' Cookie Theory in Rounds v. Development Dimensions International

**Jurisdiction:** California, Federal | **Category:** Privacy | **Date:** 2026-04-28

## Executive Summary [HIGH confidence]

On March 11, 2026, Judge David O. Carter of the U.S. District Court for the Central District of California dismissed without leave to amend the putative class action *Travis Rounds v. Development Dimensions International, Inc.*, No. 2:25-cv-08145 (C.D. Cal. Mar. 11, 2026), rejecting the plaintiff's attempt to characterize website advertising cookies and a third-party data-broker SDK as "trap and trace devices" under [California Penal Code § 638.51](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=638.51.) — the pen register and trap and trace provision of the California Invasion of Privacy Act (CIPA). The court found persuasive the defendant's argument that allegations of cookie use alone do not plausibly constitute a statutory violation of § 638.51, and further held that the insufficiency of those allegations independently defeated the personal jurisdiction analysis. The ruling extends a growing body of defendant-favorable decisions under § 638.51, adding a particularly significant wrinkle: the plaintiff had attempted to distinguish earlier dismissals by pointing to a third-party data-broker software development kit (6Sense) that the defendant had embedded on its website to de-anonymize and profile visitors. The court rejected that incremental theory, suggesting that even advertising-adjacent profiling technology does not clear the "trap and trace device" threshold when the mechanism alleged is cookie-based data transmission. The decision reinforces a litigation landscape in which California state and federal courts are narrowing the § 638.51 claim space, even as the state legislative fix — [SB 690](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB690) — stalled in 2025 and remains pending for the 2026 session.

## Background [HIGH confidence]

### California Penal Code § 638.51 and the CIPA Pen Register Framework

California added pen register and trap and trace provisions to CIPA effective January 1, 2016, through Assembly Bill 929 (Cal. Stats. 2015, ch. 204). The provision is codified at [California Penal Code §§ 638.50–638.55](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=638.51.), modeled closely on the federal Pen Register Act, 18 U.S.C. §§ 3121–3127. [Section 638.51(a)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=638.51.) provides that "a person may not install or use a pen register or a trap and trace device without first obtaining a court order pursuant to Section 638.52 or 638.53." The statute defines terms in [§ 638.50](https://codes.findlaw.com/ca/penal-code/pen-sect-638-50/):

- **"Pen register"** (§ 638.50(b)): "a device or process that records or decodes dialing, routing, addressing, or signaling information transmitted by an instrument or facility from which a wire or electronic communication is transmitted, but not the contents of a communication."
- **"Trap and trace device"** (§ 638.50(d)): "a device or process that captures the incoming electronic or other impulses that identify the originating number or other dialing, routing, addressing, or signaling information reasonably likely to identify the source of a wire or electronic communication, but not the contents of a communication."

[Section 638.55](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=638.55.) authorizes private civil suits and imposes statutory damages of $5,000 per violation. This damages structure — with no required showing of actual harm — makes the statute a frequent vehicle for class actions asserting aggregate damages potentially in the billions on large-traffic websites.

### The CIPA § 638.51 Litigation Wave

Beginning around 2023, plaintiffs' firms began pressing novel theories that common website tracking technologies — advertising pixels, JavaScript tags, analytics beacons, audience-segmentation SDKs, and browser cookies — constitute pen registers or trap and trace devices under § 638.51. The central theory: when a user visits a website, these tools collect the visitor's IP address or behavioral data and transmit it to third parties, which plaintiffs argue qualifies as recording "routing" or "addressing" information under the statute.

The litigation wave was ignited by *Greenley v. Kochava, Inc.*, 684 F. Supp. 3d 1024 (S.D. Cal. 2023), which held that software that "identifies consumers, gathers data, and correlates that data through unique 'fingerprinting'" can qualify as a pen register. As documented by [K&L Gates (March 2024)](https://www.klgates.com/Pen-Register-and-Trap-and-Trace-Claims-The-Latest-Wave-of-CIPA-Litigation-3-4-2024), scores of class actions followed, with one plaintiffs' firm alone filing over 120 such actions in the months after *Greenley*. By 2025, more than 1,000 new CIPA lawsuits per year were being filed, according to [Shumaker, Loop & Kendrick (2026)](https://www.shumaker.com/insight/client-alert-website-tracking-and-privacy-lawsuits-predicted-to-surge-in-2026-practical-steps-to-mitigate-risk/).

### The Interpretive Split: State vs. Federal Courts

A significant divergence in interpretation emerged between 2024 and 2025. As analyzed by [Holland & Knight (February 2026)](https://www.hklaw.com/en/insights/publications/2026/02/uncertainty-continues-in-california-on-cipa-section-63851-claims):

- **California state courts** have generally adopted a narrower reading, holding that § 638.51's pen register provisions are confined to telephone-number-tracing technology and do not extend to internet communications or IP address collection.
- **Federal district courts** applying California law have largely held that the statute's plain text is broad enough to encompass website tracking tools that collect IP addresses or other routing/addressing information.

Key state court dismissals included *Sanchez v. Cars.com, Inc.*, 2025 WL 487194 (Cal. Super. Ct. Jan. 27, 2025) (sustained demurrer without leave to amend, holding § 638.51 "applied only to mechanical, telephone number-tracing technology, not technology used to collect the IP address from a desktop computer"), and *Aviles v. LiveRamp, Inc.*, 2025 WL 487196 (Cal. Super. Ct. Jan. 28, 2025) (dismissed for failure to allege collection of outgoing addressing information). See the companion report on [California CIPA Pen Register IP Address State Court Rulings](../litigation/california-cipa-pen-register-ip-address-2025-01-15.md) for a detailed analysis of those decisions.

Federal courts simultaneously entertained the theory. In *Camplisson v. Adidas America* (S.D. Cal. Jan. 2025), the court denied a motion to dismiss a § 638.51 pen register claim, allowing the case to proceed. *Green Light for CIPA*, as [Baker Donelson characterized it](https://www.bakerdonelson.com/green-light-for-cipa-new-federal-court-ruling-fuels-digital-tracking-class-actions), multiple federal decisions continued to allow § 638.51 claims to survive the pleadings stage in 2025 and into 2026.

### The Plaintiffs' Escalation: Data-Broker SDK Theory

Against this backdrop, *Rounds v. DDI* represented a plaintiff-side attempt to thread the needle between the narrowing IP-address-only dismissals and the broader profiling conducted by modern ad-tech stacks. Rather than simply alleging that a tracking pixel transmitted IP addresses, the plaintiff in *Rounds* alleged that defendant Development Dimensions International ("DDI") had embedded a software development kit from [6Sense](https://6sense.com/) — a B2B revenue intelligence and account engagement platform — on its website. According to the plaintiff's theory, 6Sense's SDK did more than collect an IP address; it allegedly de-anonymized the visitor, correlated the visit against 6Sense's commercial database, and constructed or enriched a behavioral profile. The plaintiff framed this as "capturing routing and signaling data to de-anonymize users," squarely invoking the § 638.50(d) trap and trace language.

### Legislative Reform Efforts

California Senate Bill 690 (2025), authored by Sen. Anna Caballero, would have amended CIPA to create a safe harbor for routine commercial website tracking, shielding businesses from § 638.51 liability for use of common technologies like cookies, pixels, and session replay software. Despite unanimous passage in the state Senate, the bill [stalled in the Assembly in July 2025](https://www.duanemorris.com/alerts/california_sb690_stalls_assembly_cipa_liability_remains_least_through_2026_0725.html) after consumer privacy advocates — including the Electronic Frontier Foundation, ACLU California Action, and Privacy Rights Clearinghouse — raised objections. SB 690 is now a "two-year bill" eligible to be taken up again in the 2026 legislative session, but its prospects remain uncertain. As [Duane Morris noted](https://www.duanemorris.com/alerts/california_sb690_stalls_assembly_cipa_liability_remains_least_through_2026_0725.html), CIPA liability for common tracking technologies remains unresolved through legislative action at least through 2026.

## Detailed Analysis [MEDIUM confidence]

### Case Facts: *Rounds v. Development Dimensions International, Inc.*

- **Court:** U.S. District Court for the Central District of California
- **Case number:** 2:25-cv-08145 (filed August 28, 2025; per [Justia docket](https://dockets.justia.com/docket/california/cacdce/2:2025cv08145/984908))
- **Judge:** David O. Carter
- **Ruling date:** March 11, 2026
- **Outcome:** Dismissed without leave to amend

Travis Rounds, the plaintiff, alleged that DDI — a talent management and leadership development company — had installed 6Sense's data-broker SDK on its website. 6Sense is a B2B audience intelligence platform that correlates web visitor signals (geolocation, device type, browser data, cookies) against a commercial database to identify corporate visitors and enrich their profiles. Rounds alleged that when he visited DDI's website, his geolocation, device information, browser cookies, and other browser data were transmitted to 6Sense, which added the information to an existing profile and shared additional commercially derived data back to DDI.

Rounds characterized the 6Sense SDK as a "trap and trace device" on the theory that it captured "routing and signaling" information to identify the source of his communication with DDI's web server — language tracking § 638.50(d)'s definition. The complaint alleged a CIPA § 638.51 violation and also relied on the alleged statutory violation as the basis for personal jurisdiction over DDI.

### The Court's Ruling

Judge Carter dismissed the complaint without leave to amend on two interlocking grounds:

**First, the statutory violation ground.** The court found "persuasive Defendant's argument that allegations of the use of cookies does not suffice as a statutory violation of § 638.51 and the alleged use of a trap and trace device," as reported by [Inside Class Actions (March 26, 2026)](https://www.insideclassactions.com/2026/03/26/federal-court-rejects-claim-that-cookies-are-illegal-trap-and-trace-devices/) and [Loeb & Loeb (April 2026)](https://www.loeb.com/en/insights/passle/2026/04/privacy-litigation-update-california-court-rejects-trap-and-trace-cookie-claims). Although the court did not issue a categorical holding that § 638.51 can never apply to web technologies, it concluded that Rounds's specific pleading — centered on cookie-based data transmission — did not plausibly allege the statutory elements. The court declined to extend the "trap and trace" label to a commercial profiling SDK merely because that SDK ingests cookie data as part of its de-anonymization process.

**Second, the personal jurisdiction ground.** Unusually, Judge Carter connected the statutory pleading insufficiency to the court's jurisdiction: because Rounds failed to allege a plausible § 638.51 violation, the alleged statutory violation could not support the exercise of personal jurisdiction over DDI. This "jurisdictional hook" analysis — where the statutory claim is necessary to establish the court's authority to hear the case — makes the dismissal without leave to amend more final than typical Rule 12(b)(6) dismissals. Courts generally grant leave to amend at least once at the pleadings stage; the "without leave" disposition signals that no amended pleading could cure the jurisdictional defect flowing from the substantive statutory shortfall.

**Significance of the "without leave to amend" disposition.** The decision was without leave to amend on both grounds. This indicates the court concluded no set of additional facts could convert DDI's cookie-reliant ad-tech implementation into a trap and trace device violation. As analyzed by [CDF Labor Law (2026)](https://www.cdflaborlaw.com/blog/court-provides-new-road-to-early-victory-defeating-cipa-complaint), the ruling provides defendants with a procedural roadmap: early motions challenging the sufficiency of cookie-based trap and trace allegations — particularly where the challenged technology relies on standard browser cookies rather than surreptitiously installed device software — may succeed in obtaining full dismissal at the pleadings stage.

### The 6Sense SDK Distinction

The *Rounds* plaintiff's use of the 6Sense SDK theory was noteworthy as a deliberate attempt to differentiate from the earlier IP-address-only dismissals. *Sanchez* and *Aviles* had been dismissed partly on the ground that IP address collection alone — something every web server does — cannot constitute a pen register or trap and trace violation. The *Rounds* plaintiff argued that 6Sense's SDK did something qualitatively different: it actively cross-referenced browser signals against 6Sense's data graph to de-anonymize users rather than merely noting their IP address.

Judge Carter's rejection of this incremental theory is significant. The court appears to have focused on the mechanism — cookie-based data transmission — rather than the downstream use (de-anonymization and profiling). This suggests that even where a third-party tool uses cookies as input to a more sophisticated profiling operation, the operative question is whether the data collection mechanism itself satisfies the statutory definitions. Cookie transmission, in the court's view, does not, because cookies are a basic and consensual feature of web browsing rather than a device covertly "capturing" communications.

### Contrast with Pro-Plaintiff Rulings

The *Rounds* result stands in tension with decisions in which federal courts have allowed § 638.51 claims to proceed based on comparable ad-tech allegations. The [Baker Donelson analysis (2026)](https://www.bakerdonelson.com/green-light-for-cipa-new-federal-court-ruling-fuels-digital-tracking-class-actions) catalogs a class of federal decisions — including *Camplisson v. Adidas America* (S.D. Cal.) — in which plaintiffs survived motions to dismiss on similar or weaker allegations. The divergence may be explained, in part, by differences in the sophistication of the pleadings, the specific tracking technology alleged, and how individual judges analyze the line between "routing addressing information" and "contents of a communication" under § 638.50.

[Fisher Phillips (2026)](https://www.fisherphillips.com/en/insights/insights/california-courts-create-confusion-in-digital-tracking-cases) has characterized the current landscape as one of "confusion," with contradictory rulings leaving both plaintiffs and defendants uncertain about litigation strategy. The *Rounds* dismissal adds weight to the defendant-favorable side of the ledger but does not resolve the underlying interpretive split.

### Appellate Outlook

No appellate court — state or federal — has yet issued a definitive ruling on whether § 638.51 applies to website tracking technologies. As analyzed by [ZwillGen (2025)](https://www.zwillgen.com/litigation/appeals-court-cases-may-finally-provide-cipa-section-638-51-guidance/):

- **California Court of Appeal:** *Variety Media LLC v. Superior Court* is pending and is expected to address whether § 638.51 extends to common website tracking technologies. This will be the first state appellate authority on the issue, though a decision may be a year or more away.
- **Ninth Circuit:** *Drummer v. CoStar Group, Inc.* involves a certified question on whether sharing IP addresses and similar data constitutes a cognizable privacy injury sufficient to confer Article III standing (2026 WL 712922, Feb. 13, 2026). A Ninth Circuit ruling narrowing standing requirements could curtail federal § 638.51 litigation broadly.
- **Ninth Circuit standing precedent:** The court's August 2025 decision in *Popa v. Microsoft Corp.* reaffirmed that plaintiffs must show collection of "embarrassing, invasive or otherwise private information" — not just a statutory violation — to establish Article III standing. As documented by [Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/02/uncertainty-continues-in-california-on-cipa-section-63851-claims), this standing bar has become a significant threshold defense in federal § 638.51 cases.

## Impact Assessment [MEDIUM confidence]

### For Website Operators and Businesses

The *Rounds* ruling provides meaningful, if jurisdiction-specific, relief for businesses defending CIPA § 638.51 trap and trace claims. The dismissal without leave to amend represents the most favorable possible outcome at the pleadings stage. However, because the decision is from a single district court judge and the underlying law remains contested, it does not constitute binding authority across the Central District or elsewhere.

Businesses that have embedded third-party ad-tech SDKs — particularly those from data-broker or audience intelligence vendors like 6Sense, Clearbit, Demandbase, or similar platforms — should note that the *Rounds* ruling declined to treat cookie-based data ingestion by such tools as a trap and trace violation. However, these tools may still face CIPA exposure under § 631 (wiretapping) or other theories, and the absence of leave to amend in *Rounds* reflects specific pleading deficiencies rather than a categorical rule.

The practical litigation landscape remains challenging:

- The state/federal interpretive split means that plaintiffs' forum-selection choices heavily influence the viability of § 638.51 claims.
- SB 690's stall in the 2025 legislative session means no statutory safe harbor is available for the foreseeable future.
- The $5,000 per-violation statutory damages provision continues to produce bet-the-company exposure for large-traffic websites without any showing of actual harm.

### For Plaintiffs and the Class Action Bar

The *Rounds* dismissal without leave to amend raises the pleading bar for cookie-based trap and trace theories, even where plaintiffs attempt to frame the technology as a de-anonymizing data-broker tool. The ruling suggests that plaintiffs advancing § 638.51 claims must do more than allege that a website uses cookies feeding into a commercial profiling engine: the complaint must plausibly allege that the specific device or process at issue functionally constitutes a trap and trace device, likely meaning a tool that captures incoming addressing information in a way analogous to its telephone-era counterpart.

The [Inside Class Actions 2025 Roundup (January 2026)](https://www.insideclassactions.com/2026/01/27/2025-website-wiretapping-roundup/) and [Crowell & Moring's analysis](https://www.crowell.com/en/insights/client-alerts/new-year-same-cipa-uncertainty-when-will-the-appellate-courts-enter-the-chat) document that the plaintiffs' bar is actively litigating multiple competing theories in anticipation of eventual appellate guidance. The *Rounds* loss is unlikely to end § 638.51 cookie litigation broadly, but it may cause plaintiffs to refine their factual allegations or shift toward tools that involve more direct device-level software installation rather than third-party cookie ingestion.

### For Ad-Tech and Data Intelligence Vendors

Vendors whose SDKs appear as co-defendants or unnamed tools in CIPA § 638.51 suits — including data-broker platforms, audience intelligence providers, and customer data platforms that correlate web-visit signals against commercial identity graphs — should treat *Rounds* as a partial, fact-specific win. The court's focus on the cookie mechanism as insufficient, rather than on the downstream de-anonymization purpose, provides some protection for SDK vendors. However, the ruling does not immunize vendors whose tools install software on user devices, intercept communications in transit, or operate through mechanisms other than standard browser cookie transmission.

## Action Items

- **Audit third-party tracking vendors:** Identify all SDKs, pixels, and analytics tools embedded on company websites, with particular attention to audience-intelligence and data-broker platforms (e.g., 6Sense, Clearbit, Demandbase) that correlate browser signals against commercial databases. Even where *Rounds* limits CIPA § 638.51 trap and trace exposure for cookie-based ingestion, those tools may create wiretapping exposure under § 631 or CCPA data-sharing obligations.
- **Monitor SB 690 in the 2026 legislative session:** California SB 690, which would create a statutory safe harbor for common website tracking tools, is eligible for reconsideration in the 2026 session. Organizations should track its progress, engage in stakeholder comment processes, and prepare compliance contingencies for both passage and continued failure.
- **Assess forum-selection risk:** The persistent state/federal interpretive split means that companies facing CIPA § 638.51 claims should work with counsel to evaluate whether removal to federal court (or resistance to remand) is advantageous given the plaintiff's specific allegations and the technology at issue.
- **Watch for appellate guidance:** *Variety Media LLC v. Superior Court* (California Court of Appeal) and *Drummer v. CoStar Group* (Ninth Circuit) are expected to issue opinions that will provide the first binding authority on the scope of § 638.51. Companies should monitor these dockets and reassess litigation posture when decisions issue.
- **Review consent and disclosure practices:** Regardless of the § 638.51 litigation outcome, robust consent management and cookie disclosure practices under the CCPA/CPRA and applicable guidelines reduce overall cookie-related litigation risk and may be relevant to any future "good faith" defense under § 638.53.
- **Preserve CIPA § 638.51 motion practice:** The *Rounds* ruling, combined with *Sanchez* and *Aviles*, provides a strong record for early dispositive motions in § 638.51 trap and trace cases where the plaintiff's theory depends on cookie-based data collection. Coordinate with litigation counsel to deploy these precedents at the earliest practicable stage.

## Related Reports

- [California State Courts Hold CIPA Pen Register Provision Does Not Prohibit IP Address Collection](../litigation/california-cipa-pen-register-ip-address-2025-01-15.md) — The January 2025 *Sanchez* and *Aviles* state court decisions that rejected the same § 638.51 trap and trace theory *Rounds* extended; together these cases define the defendant-favorable line of authority.
- [Central District of California Dismisses CIPA Wiretapping and Eavesdropping Claims Against Boscov's](../litigation/california-cipa-chat-wiretapping-cody-v-boscov-2024-05-23.md) — Parallel CIPA wiretapping (§ 631) dismissal in the same Central District of California court, relevant to the broader pattern of CIPA litigation narrowing.
- [California Federal Court Grants Summary Judgment to CIPA Defendants: Hashing Technology Defeats Wiretapping Claims](../litigation/california-cipa-ddr-media-jornaya-hashing-2025-01-20.md) — Companion decision under CIPA § 631 where a federal court granted summary judgment to defendants, narrowing the wiretapping theory for session-replay and data-collection technology.

## Sources

1. [*Travis Rounds v. Development Dimensions International, Inc.*, No. 2:25-cv-08145 (Justia Docket)](https://dockets.justia.com/docket/california/cacdce/2:2025cv08145/984908) — Docket for the Central District of California case; confirms filing date (August 28, 2025) and case number.
2. [Loeb & Loeb LLP, "Privacy Litigation Update: California Court Rejects 'Trap and Trace' Cookie Claims" (April 2026)](https://www.loeb.com/en/insights/passle/2026/04/privacy-litigation-update-california-court-rejects-trap-and-trace-cookie-claims) — Primary law firm analysis of the *Rounds* ruling; reports judge, outcome, and statutory reasoning.
3. [Inside Class Actions (Covington & Burling), "Federal Court Rejects Claim that Cookies Are Illegal Trap and Trace Devices" (March 26, 2026)](https://www.insideclassactions.com/2026/03/26/federal-court-rejects-claim-that-cookies-are-illegal-trap-and-trace-devices/) — Detailed contemporaneous coverage of the *Rounds* March 11, 2026 ruling with direct quotation from the court's order.
4. [California Penal Code § 638.51 (Justia, 2025 Code)](https://law.justia.com/codes/california/code-pen/part-1/title-15/chapter-1-5/section-638-51/) — Official text of the prohibition on pen registers and trap and trace devices.
5. [California Penal Code § 638.50 (FindLaw)](https://codes.findlaw.com/ca/penal-code/pen-sect-638-50/) — Official definitions including "pen register" (§ 638.50(b)) and "trap and trace device" (§ 638.50(d)).
6. [Holland & Knight, "Uncertainty Continues in California on CIPA Section 638.51 Claims" (February 2026)](https://www.hklaw.com/en/insights/publications/2026/02/uncertainty-continues-in-california-on-cipa-section-63851-claims) — Comprehensive analysis of the state/federal interpretive split, standing requirements, and the *Popa v. Microsoft* Ninth Circuit decision.
7. [Baker Donelson, "Green Light for CIPA: New Federal Court Ruling Fuels Digital Tracking Class Actions" (2026)](https://www.bakerdonelson.com/green-light-for-cipa-new-federal-court-ruling-fuels-digital-tracking-class-actions) — Analysis of pro-plaintiff federal decisions including *Camplisson v. Adidas America*, providing context for the split with *Rounds*.
8. [Fisher Phillips, "California Courts Create Confusion in Digital Tracking Cases" (2026)](https://www.fisherphillips.com/en/insights/insights/california-courts-create-confusion-in-digital-tracking-cases) — Detailed survey of contradictory state and federal rulings on CIPA § 638.51, characterizing the landscape as one of "confusion."
9. [K&L Gates, "Pen Register and Trap and Trace Claims: The Latest Wave of CIPA Litigation" (March 2024)](https://www.klgates.com/Pen-Register-and-Trap-and-Trace-Claims-The-Latest-Wave-of-CIPA-Litigation-3-4-2024) — Historical background on the litigation wave post-*Greenley*, including volume and damages exposure data.
10. [Duane Morris, "California SB 690 Stalls in Assembly — CIPA Liability Remains at Least Through 2026" (July 2025)](https://www.duanemorris.com/alerts/california_sb690_stalls_assembly_cipa_liability_remains_least_through_2026_0725.html) — Analysis of SB 690's failure to advance in the 2025 session and its status as a two-year bill.
11. [ZwillGen, "Appeals Court Cases May Finally Provide CIPA Section 638.51 Guidance" (2025)](https://www.zwillgen.com/litigation/appeals-court-cases-may-finally-provide-cipa-section-638-51-guidance/) — Analysis of pending appellate cases including *Variety Media LLC v. Superior Court* (California Court of Appeal) and *Drummer v. CoStar Group* (Ninth Circuit).
12. [CDF Labor Law, "Court Provides New Road to Early Victory Defeating CIPA Complaint" (2026)](https://www.cdflaborlaw.com/blog/court-provides-new-road-to-early-victory-defeating-cipa-complaint) — Analysis of the *Rounds* dismissal as a procedural roadmap for defendants in § 638.51 cases.
13. [Inside Class Actions, "Website Wiretapping Roundup: 2025 Decisions and Developments" (January 27, 2026)](https://www.insideclassactions.com/2026/01/27/2025-website-wiretapping-roundup/) — Comprehensive roundup of all 2025 CIPA decisions, providing the full context within which *Rounds* was decided.
14. [Shumaker Loop & Kendrick, "Website Tracking and Privacy Lawsuits Predicted to Surge in 2026" (2026)](https://www.shumaker.com/insight/client-alert-website-tracking-and-privacy-lawsuits-predicted-to-surge-in-2026-practical-steps-to-mitigate-risk/) — Quantifies CIPA lawsuit volume (1,000+ per year) and provides compliance recommendations.
15. [Fisher Phillips, "California Proposal to Curb Website Cookie Litigation Stalls" (2025)](https://www.fisherphillips.com/en/news-insights/california-proposal-to-curb-website-cookie-litigation-stalls.html) — Analysis of SB 690's stalling and three recommended compliance steps for businesses.
16. [Crowell & Moring, "New Year, Same CIPA Uncertainty — When Will the Appellate Courts Enter the Chat?" (2026)](https://www.crowell.com/en/insights/client-alerts/new-year-same-cipa-uncertainty-when-will-the-appellate-courts-enter-the-chat) — Forward-looking analysis of appellate timing and its impact on CIPA § 638.51 litigation strategy.
