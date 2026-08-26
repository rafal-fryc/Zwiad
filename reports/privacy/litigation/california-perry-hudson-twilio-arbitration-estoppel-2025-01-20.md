---
title: "California Federal Court Allows Software Vendor to Enforce Website Operator's Arbitration Agreement in Privacy Lawsuit"
date: 2025-01-20
decision_date: 2024-12-02
jurisdiction: "California"
category: "privacy"
development_type: "court-decision"
finding_id: "SCAN-20250120-030"
topic_key: "california-d23675d9-2025"
topic_type: "enforcement"
first_reported: 2025-01-20
last_updated: 2026-04-22
status_history:
  - "2026-04-22: Corrected Kramer v. Toyota docket URL (12-55050), corrected WSHB Law firm name to Wood Smith Henning & Berman LLP, updated SB 690 status framing, added decision_date frontmatter field."
cluster: "CIPA Website Wiretapping Class Actions"
cluster_slug: "cipa-website-wiretapping-litigation"
---

# California Federal Court Allows Software Vendor to Enforce Website Operator's Arbitration Agreement in Privacy Lawsuit

**Jurisdiction:** California (N.D. Cal.) | **Category:** Privacy / Litigation | **Date:** January 20, 2025

## Executive Summary [HIGH confidence]

In *Perry-Hudson v. Twilio, Inc.*, No. 3:24-cv-03741-VC (N.D. Cal. Dec. 2, 2024), Judge Vince Chhabria granted Twilio's motion to compel individual arbitration, holding that a software vendor not party to the underlying arbitration agreement could nonetheless enforce that agreement under the equitable estoppel doctrine. The plaintiff, a customer of hair-loss treatment retailer Keeps, attempted to sidestep his arbitration agreement with Keeps by suing only Twilio — the analytics/communications software vendor whose tools Keeps embedded on its website. The court rejected this tactic, finding two independent grounds for equitable estoppel: (1) the plaintiff's claims were "intimately founded in and intertwined with" his agreement with Keeps, and (2) the plaintiff alleged interdependent and coordinated misconduct by both Twilio and Keeps that was intimately connected to contractual obligations. The case was stayed pending arbitration. This decision is significant for software vendors embedded across website ecosystems and for companies that rely on arbitration clauses as a defense against privacy class actions under California's Invasion of Privacy Act and similar wiretapping statutes.

## Background [HIGH confidence]

### The Website Wiretapping Litigation Wave

Since 2022, plaintiffs' counsel have filed hundreds — and by some estimates thousands — of putative class actions alleging that website analytics tools, advertising pixels, session-replay scripts, and customer engagement software constitute illegal "wiretapping" under the [California Invasion of Privacy Act ("CIPA"), Penal Code §§ 631 and 632.7](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=631). These cases assert that third-party technology vendors embedded on websites intercept communications in real time without user consent.

CIPA section 631 prohibits unauthorized interception of "telegraphic or telephone" wire communications and has been extended by plaintiffs to cover internet-based communications. The statute provides a private right of action with statutory damages of $5,000 per violation — a structure that has fueled large-scale class action filings even absent actual monetary harm to individual plaintiffs.

A recurring defense deployed by website operators has been to invoke arbitration clauses embedded in their terms of service or privacy policies, which frequently contain class action waivers. The strategic complication arises when plaintiffs name only the third-party technology vendor — not the website operator — as a defendant. In that posture, the non-party vendor cannot directly invoke an arbitration agreement to which it was not a signatory.

### The Equitable Estoppel Doctrine in the Ninth Circuit

Federal courts apply state contract law to determine whether a non-signatory can compel arbitration under the equitable estoppel doctrine. Under California law, as articulated by the Ninth Circuit in [*Kramer v. Toyota Motor Corp.*, 705 F.3d 1122 (9th Cir. 2013)](https://law.justia.com/cases/federal/appellate-courts/ca9/12-55050/12-55050-2013-01-30.html), a non-signatory defendant may invoke an arbitration clause via equitable estoppel in two circumstances:

1. **Intertwining:** When the signatory plaintiff's claims against the non-signatory are "intimately founded in and intertwined with" the underlying contract containing the arbitration clause.
2. **Concerted misconduct:** When the signatory plaintiff alleges interdependent and coordinated misconduct by both the non-signatory and a signatory party, and that misconduct is intimately connected with the obligations of the underlying agreement.

The Ninth Circuit reinforced this standard in [*Herrera v. Cathay Pacific Airways Ltd.*, 104 F.4th 702 (9th Cir. Mar. 11, 2024)](https://law.justia.com/cases/federal/appellate-courts/ca9/21-16083/21-16083-2024-03-11.html), reversing a district court denial of a motion to compel arbitration and holding that the proper focus is whether it would be unfair to allow a plaintiff to circumvent a valid arbitration clause by strategic party selection.

## Detailed Analysis [HIGH confidence]

### Facts of *Perry-Hudson v. Twilio*

Plaintiff Jonathon Perry-Hudson was a customer of Keeps, an online retailer selling hair-loss treatments. When Perry-Hudson used Keeps' website and provided health information to receive a treatment recommendation, Keeps had embedded Twilio's software tools on the site — tools that allegedly collected and transmitted Perry-Hudson's data, including sensitive health information, to facilitate targeted advertising.

Rather than suing Keeps — the party with whom he had directly contracted and whose Terms & Conditions he had agreed to — Perry-Hudson filed a putative class action against Twilio only. His claims alleged that Twilio's role in capturing his website communications constituted illegal "wiretapping" under [CIPA § 631](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=631). By naming only Twilio, Perry-Hudson sought to avoid the arbitration clause in the Keeps Terms & Conditions, which covered disputes arising from his use of the Keeps website.

Twilio moved to compel arbitration of plaintiff's claims, invoking the arbitration clause in Keeps' Terms & Conditions under the equitable estoppel doctrine. The motion was filed in the United States District Court for the Northern District of California, where the case is docketed as [Case No. 3:24-cv-03741](https://dockets.justia.com/docket/california/candce/3:2024cv03741/431380).

### The Court's Two-Pronged Equitable Estoppel Analysis

Judge Chhabria applied the *Kramer* two-part framework and found both prongs satisfied.

**First prong — Intertwining:** The court found that Perry-Hudson's privacy claims were "intimately founded in and intertwined with" his agreement with Keeps. Specifically, the court noted that consent is an element of each CIPA claim, and whether Perry-Hudson consented to sharing his data with Twilio turns directly on the Keeps Terms & Conditions and Privacy Policy — documents Perry-Hudson agreed to when using the Keeps website. Because the arbitration agreement "speaks directly to Keeps's obligations with respect to [plaintiff's] data and his consent to sharing that data," Perry-Hudson's claims against Twilio could not be resolved without reference to that contract.

**Second prong — Concerted misconduct:** The court also found that Perry-Hudson alleged interdependent and coordinated misconduct between Twilio and Keeps, both in deploying the data-collection tools and in how Perry-Hudson's health data flowed between the two entities. The court held that this alleged "concerted misconduct" was "intimately connected" to the contractual relationship between Perry-Hudson and Keeps, satisfying the second *Kramer* prong independently.

Judge Chhabria granted Twilio's motion to compel individual arbitration and denied Twilio's motion to dismiss as moot. The case was stayed pending completion of arbitration proceedings. The official court order is available on [Justia Dockets](https://docs.justia.com/cases/federal/district-courts/california/candce/3:2024cv03741/431380/35).

### The Strategic Pleading Tactic and Its Limits

The decision explicitly addresses a litigation tactic that has gained prominence in the website wiretapping arena: plaintiffs deliberately omit the website operator from the complaint to avoid triggering an arbitration clause and class action waiver that the operator could enforce. By suing only the third-party vendor, plaintiffs gamble that the vendor — lacking privity with the plaintiff — cannot invoke a contract to which it was not a party.

The court rejected this tactic, reasoning that a plaintiff who agreed to an arbitration clause cannot "skirt its agreement with Keeps by suing only Twilio." This reasoning draws on the principle embedded in equitable estoppel: a party should not be permitted to use inconsistent positions — claiming rights under a contract (by relying on it to establish the breach of a duty) while simultaneously disavowing the contract's dispute-resolution mechanism.

### Covington & Burling Analysis

The decision was analyzed by [Covington & Burling LLP on Inside Class Actions](https://www.insideclassactions.com/2025/01/13/california-federal-court-allows-software-vendor-to-enforce-website-operators-arbitration-agreement-in-privacy-lawsuit/), which characterized the ruling as reinforcing "that equitable estoppel principles may provide avenues of relief against plaintiffs seeking to avoid arbitration clauses covering the claims at issue." Similarly, [Wood Smith Henning & Berman LLP (WSHB Law) noted](https://www.wshblaw.com/publication-software-vendor-granted-right-to-enforce-websites-arbitration-agreement-in-california-privacy-dispute) that the ruling underscores the importance of arbitration agreements in defending against wiretapping-based privacy class actions.

## Impact Assessment [MEDIUM confidence]

### Who Is Affected

This decision has direct implications for several categories of actors:

**Software vendors and analytics providers:** Companies like Twilio, marketing pixels, customer data platforms, session-replay providers, and similar third-party vendors embedded on consumer websites gain a meaningful defense in privacy class actions. If the website operator whose site embeds the vendor's tool has a valid arbitration agreement with the user, the vendor can potentially invoke that agreement even as a non-signatory.

**Website operators:** The ruling incentivizes website operators to maintain robust, enforceable arbitration clauses in their terms of service. An arbitration agreement that a website operator secures from users may not only protect the operator itself but may also protect downstream vendors from class action exposure.

**Privacy plaintiffs' counsel:** The decision limits the effectiveness of the selective-defendant litigation strategy. Plaintiffs who sign up for an operator's service and agree to arbitration may be unable to evade arbitration simply by naming only the operator's technology vendors as defendants.

### Compliance Implications

The decision does not impose new affirmative legal requirements on businesses, but it carries important strategic implications:

1. **For website operators:** Ensure that terms of service contain well-drafted, enforceable arbitration clauses with class action waivers that expressly cover claims arising from data sharing with third-party vendors. The Keeps arbitration clause's reference to data obligations was a critical factor in the court's analysis.

2. **For software vendors:** Audit the terms of service of major website operator customers. Where those terms include arbitration clauses, preserve those agreements as a potential defense in any privacy litigation brought by website users.

3. **For both:** The court's analysis turned significantly on whether the plaintiff's claims were consent-dependent and thus intertwined with the underlying contract. Vendors and operators should structure consent flows and data-sharing disclosures in terms of service so that user consent to data sharing is clearly documented.

### Broader Context: CIPA and California Senate Bill 690

The decision arrives during a period of significant uncertainty in California website-tracking litigation. [California Senate Bill 690](https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260SB690), which would exclude routine commercial tracking from CIPA's scope, passed the California Senate unanimously in June 2025 but was voluntarily held in the Assembly by its sponsor pending resolution of outstanding privacy concerns; it advanced as a two-year bill eligible for reconsideration in the 2026 session. In the absence of legislative clarification, courts continue to issue divergent rulings on the scope of CIPA's wiretapping provisions, making arbitration clause defenses particularly valuable to defendants.

The Ninth Circuit's 2024 decision in *Herrera v. Cathay Pacific* and the Northern District's ruling in *Perry-Hudson* suggest that courts in the circuit are willing to apply equitable estoppel robustly when a plaintiff's strategic party selection appears designed to circumvent a valid arbitration agreement.

## Action Items

- **Website operators:** Review and update arbitration clauses in terms of service to ensure they expressly address data sharing with third-party vendors and cover all claims that could arise from that sharing.
- **Software vendors:** Identify website operator customers with user-facing arbitration agreements and class action waivers; assess whether those clauses could support an equitable estoppel argument if vendor-only privacy litigation is filed.
- **Litigants facing CIPA class actions:** Evaluate at the earliest stage whether the plaintiff agreed to an arbitration clause with a co-party or upstream partner; the *Perry-Hudson* two-prong *Kramer* test provides a viable motion-to-compel framework even for non-signatories.
- **Monitor the *Perry-Hudson* docket** ([Case 3:24-cv-03741](https://dockets.justia.com/docket/california/candce/3:2024cv03741/431380)) for any appeal of the arbitration order, which could affect the strength of this precedent in the Ninth Circuit.
- **Track California SB 690** in the 2026 legislative session; enactment would alter the underlying substantive exposure driving these cases and reduce the practical value of arbitration defenses in the CIPA context.

## Related Reports

- [reports/privacy/litigation/california-cipa-chat-wiretapping-cody-v-boscov-2024-05-23.md](reports/privacy/litigation/california-cipa-chat-wiretapping-cody-v-boscov-2024-05-23.md) — Covers CIPA wiretapping claims against a website operator over embedded live chat software, directly in the same litigation cluster.
- [reports/privacy/litigation/california-cipa-pen-register-ip-address-2025-01-15.md](reports/privacy/litigation/california-cipa-pen-register-ip-address-2025-01-15.md) — Addresses CIPA pen register provision and limits on its scope in website-tracking cases; companion precedent context.
- [reports/privacy/litigation/california-cipa-ddr-media-jornaya-hashing-2025-01-20.md](reports/privacy/litigation/california-cipa-ddr-media-jornaya-hashing-2025-01-20.md) — Decided on the same date, addresses CIPA claims against a data analytics vendor, illustrating the parallel wave of vendor-targeted CIPA litigation.
- [reports/privacy/litigation/california-shah-v-fandom-cipa-tracking-consent-2024-11-06.md](reports/privacy/litigation/california-shah-v-fandom-cipa-tracking-consent-2024-11-06.md) — Addresses consent as a defense to CIPA tracking claims; consent analysis is central to the intertwining prong applied in *Perry-Hudson*.

## Sources

1. [*Perry-Hudson v. Twilio, Inc.*, Case No. 3:24-cv-03741-VC (N.D. Cal.) — Justia Docket](https://dockets.justia.com/docket/california/candce/3:2024cv03741/431380) — Official docket for the case, including filing date and case number.
2. [Order Granting Motion to Compel Individual Arbitration — Justia Dockets & Filings](https://docs.justia.com/cases/federal/district-courts/california/candce/3:2024cv03741/431380/35) — Official court order (Dec. 2, 2024) granting Twilio's motion to compel arbitration.
3. [CourtListener — *Perry-Hudson v. Twilio, Inc.*, 3:24-cv-03741](https://www.courtlistener.com/docket/68877244/perry-hudson-v-twilio-inc/) — PACER-linked docket with case filings.
4. [Covington & Burling / Inside Class Actions — "California Federal Court Allows Software Vendor to Enforce Website Operator's Arbitration Agreement in Privacy Lawsuit" (Jan. 13, 2025)](https://www.insideclassactions.com/2025/01/13/california-federal-court-allows-software-vendor-to-enforce-website-operators-arbitration-agreement-in-privacy-lawsuit/) — Primary law firm analysis of the decision; key source for court's reasoning.
5. [Covington & Burling / Lexology — same article](https://www.lexology.com/library/detail.aspx?g=ee87e210-4cd2-4736-984d-0afd8cac080a) — Lexology syndication of the Covington & Burling analysis.
6. [Wood Smith Henning & Berman LLP (WSHB Law) — "Software Vendor Granted Right to Enforce Website's Arbitration Agreement in California Privacy Dispute"](https://www.wshblaw.com/publication-software-vendor-granted-right-to-enforce-websites-arbitration-agreement-in-california-privacy-dispute) — Independent law firm analysis confirming key facts and legal reasoning.
7. [Covington & Burling / Inside Class Actions — "Website Wiretapping Litigation: Recent Decisions and Developments" (Feb. 26, 2025)](https://www.insideclassactions.com/2025/02/26/website-wiretapping-litigation-recent-decisions-and-developments/) — Broader survey placing *Perry-Hudson* in the context of 2024–2025 CIPA litigation trends.
8. [Inside Privacy — "Website Wiretapping Litigation: Recent Decisions and Developments"](https://www.insideprivacy.com/data-privacy/website-wiretapping-litigation-recent-decisions-and-developments/) — Additional Covington analysis noting arbitration developments in website wiretapping cases.
9. [*Herrera v. Cathay Pacific Airways Ltd.*, 104 F.4th 702 (9th Cir. 2024) — Justia](https://law.justia.com/cases/federal/appellate-courts/ca9/21-16083/21-16083-2024-03-11.html) — Ninth Circuit precedent applying equitable estoppel standard for non-signatory arbitration enforcement.
10. [California Penal Code § 631 — California Legislative Information](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=631) — Official text of CIPA's wiretapping provision underlying the plaintiff's claims.
11. [Proskauer / National Law Review — "Ninth Circuit Clears Airline's Arbitration by Estoppel Argument for Takeoff" (2024)](https://natlawreview.com/article/ninth-circuit-clears-airlines-arbitration-estoppel-argument-takeoff) — Analysis of *Herrera v. Cathay Pacific*, the governing Ninth Circuit equitable estoppel standard.
12. [Global Policy Watch / Covington — "Website Wiretapping Litigation: Recent Decisions and Developments"](https://www.globalpolicywatch.com/2025/02/website-wiretapping-litigation-recent-decisions-and-developments/) — Supplementary coverage of CIPA litigation trends and the role of arbitration defenses.
