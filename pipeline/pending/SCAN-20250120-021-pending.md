---
title: "California Federal Court Grants Summary Judgment to CIPA Defendants: Hashing Technology Defeats Wiretapping Claims"
date: 2025-01-20
jurisdiction: "California"
category: "privacy"
development_type: "court-decision"
finding_id: "SCAN-20250120-021"
topic_key: "california-0fa28010-2025"
topic_type: "enforcement"
topic_key_confidence: "low"
first_reported: 2025-01-20
last_updated: 2026-04-22
status_history:
  - "2026-04-22: Revised per reviewer round 1 — corrected Chhabria quote ('borderline impossible'), updated Thomas v. Papa John's characterization, added temporal disclosure note to Executive Summary."
cluster: "CIPA Website Wiretapping Class Actions"
cluster_slug: "cipa-website-wiretapping-litigation"
---

# California Federal Court Grants Summary Judgment to CIPA Defendants: Hashing Technology Defeats Wiretapping Claims

**Jurisdiction:** California, Federal | **Category:** Privacy | **Date:** 2025-01-20

## Executive Summary [HIGH confidence]

In *Williams v. DDR Media, LLC*, No. 22-cv-03789-SI, 757 F. Supp. 3d 989 (N.D. Cal. Nov. 20, 2024), Judge Susan Illston of the United States District Court for the Northern District of California granted summary judgment to defendants DDR Media LLC and Jornaya in a putative class action brought under [California Penal Code § 631(a)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=631.&lawCode=PEN) — the wiretapping provision of the California Invasion of Privacy Act (CIPA). The plaintiff, Loretta Williams, alleged that Jornaya's TCPA Guardian software intercepted her keystrokes, clicks, and personal data submitted on DDR Media's website in violation of CIPA's prohibition against "reading" communications in transit. The court rejected this theory on the merits, holding that CIPA's prohibition on "read[ing], or attempt[ing] to read, or to learn the contents or meaning" of a communication requires some effort at understanding the substantive meaning of the data — and that Jornaya's automated hashing process, which instantaneously converts inputs into incomprehensible alphanumeric strings, does not satisfy that standard. The decision provides a significant affirmative defense for technology vendors relying on one-way hashing to protect personal data, and places the Northern District of California among courts narrowing CIPA's scope in the face of a wave of website wiretapping class actions.

**Temporal note:** The core decision in *Williams v. DDR Media* was issued November 20, 2024. This report was prepared in April 2026 and incorporates subsequent developments through early 2026, including the October 2025 Chhabria ruling, the June 2025 *Thomas v. Papa John's* Ninth Circuit decision, and the January 2026 CIPA litigation roundup. Citations from these later periods are expressly noted as post-decision context.

## Background [HIGH confidence]

### California's Invasion of Privacy Act — Section 631

[California Penal Code § 631](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=631.&lawCode=PEN), enacted in 1967 as part of the California Invasion of Privacy Act, penalizes willful wiretapping and interception of communications without the consent of all parties. Subsection (a) creates civil and criminal liability for any person who intentionally "reads, or attempts to read, or to learn the contents or meaning of any message, report, or communication while the same is in transit" over a telephone or telegraph wire, or any other wire or cable — absent the consent of all parties to the communication.

Since 2021, plaintiffs' attorneys have deployed § 631 at scale against website operators and technology vendors. The prevailing theory characterizes third-party analytics pixels, session replay tools, tracking pixels, and compliance-technology SDKs as third-party "eavesdroppers" intercepting real-time user keystrokes and form submissions, placing them within the statute's wiretapping prohibition. This litigation wave has generated thousands of demand letters and hundreds of putative class actions in California state and federal courts. The [California Privacy Protection Agency](https://cppa.ca.gov/) and the California Legislature have acknowledged the volume of CIPA litigation and considered legislative clarification, including [Senate Bill 690 (2025)](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB690), which would exempt commercial business-purpose tracking from liability.

### DDR Media, Jornaya, and TCPA Guardian

Defendant DDR Media LLC operates a consumer finance and insurance lead-generation website. Defendant Jornaya — a Philadelphia-based data technology company — markets TCPA Guardian, software designed to help lead buyers and sellers comply with the [Telephone Consumer Protection Act (TCPA)](https://www.fcc.gov/consumers/guides/stop-unwanted-robocalls-and-texts) by verifying whether a consumer provided prior express written consent before being contacted by telemarketers. TCPA Guardian records the circumstances of consent on a website (URL, timestamp, form data) and compares hashed representations of lead data between lead sellers and buyers to confirm identity without sharing raw personal data.

Loretta Williams visited snappyrent2own.com — a DDR Media site — on December 10, 2021, and submitted a form containing her name, email address, and phone number. She subsequently filed suit alleging that Jornaya's TCPA Guardian had intercepted and "read" those inputs in violation of CIPA § 631(a), and that DDR Media was liable under an aiding-and-abetting theory for enabling Jornaya's conduct on its website. Following a prior dismissal and amendment, her Second Amended Complaint asserted a single CIPA § 631(a) claim. The court allowed the claim to proceed past the pleading stage, and the parties then engaged in discovery. Jornaya thereafter moved for summary judgment.

## Detailed Analysis [HIGH confidence]

### The Hashing Defense: Automated Processing as Non-"Reading"

The central question before the court was whether Jornaya's TCPA Guardian "reads, or attempts to read, or to learn the contents or meaning" of Williams's data within the meaning of § 631(a).

Jornaya submitted evidence establishing that TCPA Guardian subjects every piece of user-submitted data to a one-way cryptographic hash immediately upon transmission from the website to Jornaya's servers. The original, unhashed data is never stored or retained. The hashing algorithm transforms inputs into incomprehensible alphanumeric strings (hashes) that cannot be reversed to recover the original information. The hashed values serve only as identity tokens for comparing whether two lead records correspond to the same person — TCPA Guardian does not process, analyze, or "read" the names, email addresses, or phone numbers that were originally submitted.

Judge Illston held that the statute's verb phrase — "reads, or attempts to read, or to learn the contents or meaning" — requires "some effort at understanding the substantive meaning" of the communication at issue. Because Jornaya's hashing is automatic, instantaneous, and produces only an opaque representation, the court found no such effort was present. Williams argued that even the initial formatting step preceding the hash (in which data is prepared for the hashing algorithm) constituted "reading." The court was "not persuaded," finding this step to be an automatic, technologically unremarkable precursor that did not involve any attempt to understand the data's meaning.

Because Jornaya did not commit a predicate CIPA § 631(a) violation, the court also dismissed the aiding-and-abetting claim against DDR Media, as such a theory requires an underlying violation by the aided party. [*See* National Law Review analysis of the ruling](https://natlawreview.com/article/hashing-it-out-jornayas-data-tech-victory-over-cipa-claims).

### "In-Transit" and Consent Dimensions

While the court's primary rationale rested on the "reads or learns" analysis, the ruling touched on themes also prominent in related CIPA § 631 cases decided in 2024–2025. Courts in the Northern District, Central District, and Ninth Circuit have variously addressed whether third-party software captures data "while in transit" (as opposed to after receipt), and whether website privacy policies or cookie banners establish consent sufficient to defeat CIPA claims. The *Williams* court reached the defendants' favor without needing to fully resolve the in-transit timing question, because the hashing defense established a more fundamental threshold: Jornaya was not "reading" the data at any point in the process.

The Covington & Burling attorneys of record for defendants (Matthew Q. Verdin, Kathryn Cahoy, and Libbie Canter) had previously argued in earlier proceedings that the plaintiff had consented to Jornaya's data collection through the website's privacy disclosures; this consent argument was part of the evidentiary record at summary judgment even if the court's stated rationale focused on the "reads" element. [*See* Lexology / Covington coverage](https://www.lexology.com/library/detail.aspx?g=7c592f71-d2eb-4f65-bc2d-dd395efd2c0e).

### Position in the Broader CIPA Landscape

*Williams v. DDR Media* fits within a broader 2024–2025 judicial trend of defendants prevailing on CIPA § 631 claims through multiple doctrinal routes:

- **In-transit timing:** In *Torres v. Prudential Financial* (2025), a California federal court held that session replay software data becomes readable only after transmission and storage, not "while in transit," defeating the CIPA claim. In *Thomas v. Papa John's* (Ninth Circuit, June 18, 2025), the Ninth Circuit affirmed dismissal, holding that the plaintiff had not alleged Papa John's aided a third party in eavesdropping and that she lacked a reasonable expectation of privacy in the submitted form data.
- **Consent:** In *Lakes v. Ubisoft, Inc.* (N.D. Cal. Apr. 2, 2025), the court concluded that consent defeated all CIPA § 631 claims.
- **Statutory scope and rule of lenity:** In a notable October 2025 decision, Judge Vince Chhabria described CIPA as "a total mess" and invoked the rule of lenity to grant summary judgment for a defendant facing Meta Pixel claims, noting it was "borderline impossible" to determine how the 1967 statute applied to modern internet communications.

Despite this defense-favorable trend, the litigation wave has not abated: courts remain divided on the in-transit element, aiding-and-abetting exposure for website operators, and the applicability of § 638.51 (pen register) to web tracking. [*See* 2025 CIPA litigation roundup, Inside Class Actions](https://www.insideclassactions.com/2026/01/27/2025-website-wiretapping-roundup/).

## Impact Assessment [MEDIUM confidence]

### Technology Vendors Using One-Way Hashing

*Williams v. DDR Media* is particularly significant for technology vendors in the lead-generation, identity-matching, and consent-verification space that rely on cryptographic hashing to process user data without retaining raw personal information. The decision suggests that courts applying CIPA § 631(a) will examine whether a vendor actually comprehended the substantive meaning of user data — not merely whether the vendor's software made contact with the data stream. Vendors that hash all inputs immediately upon receipt, and never store or analyze unhashed data, have strong grounds to defeat "reads or learns" claims under § 631(a) in the Northern District of California.

However, this ruling does not eliminate CIPA exposure for all tracking technologies. Session replay tools that buffer and reassemble keystroke data for later human viewing present a different technical profile. Pixel-based advertising tools (e.g., Meta Pixel, TikTok Pixel) that transmit user data to third parties in readable form without immediate hashing remain vulnerable under multiple theories. The ruling also does not address CIPA § 638.51 (pen register) claims, which have been litigated on separate grounds.

### Website Operators and Lead-Generation Platforms

For website operators that embed third-party compliance tools or lead-qualification technology:

- The DDR Media ruling demonstrates that the aiding-and-abetting theory depends entirely on whether the underlying third-party vendor committed a predicate CIPA violation. If the vendor's technology design defeats primary liability, the website operator's exposure also falls away.
- Operators should nonetheless ensure that website privacy policies and consent notices adequately disclose third-party data collection, as consent remains an independent and frequently litigated defense.

### Legislative Pressure

[California SB 690 (2025)](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB690), introduced by Senator Caballero, would amend CIPA to exempt commercial business-purpose tracking technologies from § 631 liability, targeting the wave of litigation the *Williams* decision emerged from. If enacted, SB 690 would render the *Williams* hashing analysis largely moot for compliant commercial uses, but would not resolve pending cases or the broader debate about CIPA's application to non-commercial or non-disclosed tracking.

## Action Items

- Technology vendors using one-way cryptographic hashing should document their data flow architectures to demonstrate that inputs are hashed immediately upon receipt and that original data is never stored — this technical evidence is the core of the *Williams* affirmative defense.
- Website operators embedding compliance or lead-qualification tools (Jornaya TCPA Guardian or similar) should request written confirmation from vendors describing their hashing or data-minimization practices, to support aiding-and-abetting defense arguments if sued under CIPA.
- Review and update website privacy policies and cookie/consent banners to ensure clear, conspicuous disclosure of all third-party data collection technologies — consent remains an independent CIPA defense regardless of the hashing analysis.
- Monitor [California SB 690](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB690) as it moves through the legislature; enactment would substantially affect existing CIPA exposure for commercial website tracking practices.
- Do not assume *Williams* resolves all CIPA § 631 exposure: session replay tools, advertising pixels, and pen register (§ 638.51) theories remain active litigation risks requiring independent technical and legal analysis.

## Related Reports

- [reports/privacy/litigation/california-cipa-chat-wiretapping-cody-v-boscov-2024-05-23.md](../litigation/california-cipa-chat-wiretapping-cody-v-boscov-2024-05-23.md) — Companion CIPA § 631 wiretapping ruling in the same cluster, addressing website live-chat technology and the in-transit interception element.
- [reports/privacy/litigation/california-cipa-pen-register-ip-address-2025-01-15.md](../litigation/california-cipa-pen-register-ip-address-2025-01-15.md) — Related California state court decisions rejecting CIPA § 638.51 pen register claims against website IP-address collection, decided contemporaneously with *Williams*.
- [reports/privacy/litigation/california-cipa-chat-wiretapping-garcia-v-buildcom-2024-04-17.md](../litigation/california-cipa-chat-wiretapping-garcia-v-buildcom-2024-04-17.md) — Earlier CIPA § 631 wiretapping case addressing session replay and live chat under the same in-transit framework contested in *Williams*.

## Sources

1. [Williams v. DDR Media, LLC — CaseMine (N.D. Cal. Nov. 20, 2024)](https://www.casemine.com/judgement/us/674009205b2f8e66a0a8771c) — Primary case record and judgment text for Williams v. DDR Media, LLC, No. 22-cv-03789-SI, 757 F. Supp. 3d 989.
2. [California Federal Court Grants Summary Judgment to CIPA Defendants — Inside Class Actions (Covington & Burling LLP, Jan. 14, 2025)](https://www.insideclassactions.com/2025/01/14/california-federal-court-grants-summary-judgment-to-cipa-defendants/) — Primary law firm analysis by Covington & Burling attorneys; provides detailed factual and legal summary of the ruling.
3. [HASHING IT OUT!: Jornaya's Data Tech Victory Over CIPA Claims — National Law Review (Nov. 22, 2024)](https://natlawreview.com/article/hashing-it-out-jornayas-data-tech-victory-over-cipa-claims) — Independent analysis of the Williams decision from the TCPA/lead-gen litigation perspective; confirms case citation and legal reasoning.
4. [California Federal Court Grants Summary Judgment to CIPA Defendants — Lexology (Covington & Burling LLP)](https://www.lexology.com/library/detail.aspx?g=7c592f71-d2eb-4f65-bc2d-dd395efd2c0e) — Covington & Burling client alert on the ruling; confirms lead defense attorneys and legal analysis.
5. [California Penal Code § 631 — California Legislative Information (official text)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=631.&lawCode=PEN) — Official California Legislature text of CIPA § 631(a), the wiretapping provision at issue.
6. [California Penal Code § 631 (2025) — Justia](https://law.justia.com/codes/california/code-pen/part-1/title-15/chapter-1-5/section-631/) — Secondary statutory reference for CIPA § 631; useful for version history.
7. [Website Wiretapping Roundup: 2025 Decisions and Developments — Inside Class Actions (Jan. 27, 2026)](https://www.insideclassactions.com/2026/01/27/2025-website-wiretapping-roundup/) — Comprehensive roundup of 2025 CIPA § 631 decisions; contextualizes Williams within the broader litigation landscape.
8. [Developments in Digital Privacy Litigation in 2024-2025: CIPA, VPPA, and California's SB 690 — Coblentz Law](https://www.coblentzlaw.com/news/developments-in-digital-privacy-litigation-in-2024-2025-cipa-vppa-and-californias-sb-690/) — Law firm analysis covering Williams and peer decisions, plus SB 690 legislative context.
9. [U.S. Privacy Litigation Update: Holiday Edition (October–December 2024) — Byte Back Law](https://www.bytebacklaw.com/2025/01/u-s-privacy-litigation-update-holiday-edition-october-november-december-2024/) — Litigation update confirming Williams in broader Q4 2024 privacy litigation context.
10. [California Senate Bill 690 — California Legislative Information (official text)](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB690) — Official legislative text of SB 690, the 2025 bill proposing to amend CIPA to exempt commercial tracking technologies.
11. [Williams v. DDR Media, LLC — PACER Monitor docket, 3:22-cv-03789](https://www.pacermonitor.com/public/case/45051004/Williams_v_DDR_Media,_LLC_et_al) — Public docket for the case; provides procedural history and filing dates.
