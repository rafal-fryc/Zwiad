---
title: "Supreme Court Hears FCC Location Data Fines Case — Court Appears Likely to Uphold Agency Enforcement Authority"
date: 2026-04-22
jurisdiction: "Federal"
category: "privacy"
development_type: "litigation"
finding_id: "SCAN-20260422-027"
topic_key: "FCC-SCOTUS-CPNI-25-406-567"
topic_type: "enforcement_action"
first_reported: 2026-04-22
last_updated: 2026-04-22
status_history: []
cluster: "FCC Location Data Fines: AT&T and Verizon Carrier Enforcement"
cluster_slug: "fcc-location-data-fines-carrier-enforcement"
---

# Supreme Court Hears FCC Location Data Fines Case — Court Appears Likely to Uphold Agency Enforcement Authority

**Jurisdiction:** Federal | **Category:** Privacy | **Date:** April 22, 2026

## Summary [HIGH confidence]

On April 21, 2026, the US Supreme Court heard consolidated oral arguments in *Federal Communications Commission v. AT&T, Inc.* (No. 25-406) and *Verizon Communications Inc. v. Federal Communications Commission* (No. 25-567), cases challenging over $103 million in FCC fines imposed in 2024 for the carriers' sale of customer location data to third-party aggregators without adequate consent. A majority of justices appeared skeptical of the telecoms' Seventh Amendment jury trial arguments, with several suggesting the FCC's two-stage forfeiture process — which culminates in a DOJ-filed civil suit where defendants receive a jury trial — is constitutionally distinguishable from the SEC structure struck down in *SEC v. Jarkesy* (2024). A decision is expected by late June 2026.

## Background [HIGH confidence]

### The Underlying FCC Enforcement Action

In April 2024, the FCC fined AT&T $57,265,625 and Verizon $46,901,250 — part of nearly $200 million in total fines also levied against T-Mobile and Sprint — for violations of [Section 222 of the Communications Act of 1934](https://www.fcc.gov/document/fcc-fines-largest-wireless-carriers-sharing-location-data), which requires telecommunications carriers to protect the confidentiality of customer proprietary network information (CPNI), including precise location data.

The [FCC's investigation](https://krebsonsecurity.com/2024/04/fcc-fines-major-u-s-wireless-carriers-for-selling-customer-location-data/) found that each carrier had sold access to customer location data to "aggregators" — intermediary companies that then resold it to third-party location-based service (LBS) providers. In several documented instances, that data reached a Missouri sheriff through prison phone company Securus, which obtained location data through aggregator LocationSmart, without customer consent. The carriers attempted to delegate their consent obligations to downstream recipients, resulting in widespread unauthorized disclosure.

The FCC rejected the carriers' argument that location data does not constitute CPNI, and found that each unauthorized LBS provider with data access for more than 30 days after public disclosure of the practice constituted a separate continuing violation — driving up the penalty amounts. The original [FCC press release and forfeiture orders](https://docs.fcc.gov/public/attachments/DOC-402213A1.pdf) are publicly available.

### The Two-Stage FCC Forfeiture Process

The FCC's enforcement structure operates in two stages. First, the agency issues a Notice of Apparent Liability (NAL), proposing a penalty and inviting the carrier to respond. The FCC may then issue a binding Forfeiture Order. Critically, the FCC cannot collect that order on its own: only the Department of Justice can enforce it by filing a civil collection suit in federal district court, where the carrier has the right to a jury trial. Companies may alternatively pay the forfeiture and seek review in a federal court of appeals under the Hobbs Act within 60 days.

## The Circuit Split [HIGH confidence]

The constitutional challenge turned on whether this structure violated the Seventh Amendment's guarantee of jury trials in suits at common law. Two circuits reached opposite conclusions:

- **Fifth Circuit** (*FCC v. AT&T*): Applying *SEC v. Jarkesy*, 603 U.S. 109 (2024), the court [vacated the $57 million AT&T forfeiture order](https://perkinscoie.com/insights/update/fifth-circuit-rules-fcc-enforcement-action-unconstitutional), finding the FCC's in-house proceedings — in which the agency acted as prosecutor, judge, and jury — violated AT&T's Article III and Seventh Amendment rights. The Fifth Circuit found the CPNI enforcement action analogous to a common-law fraud action that would have been tried by a jury in 1791.

- **Second Circuit** (*Verizon v. FCC*): The court [upheld the Verizon forfeiture](https://epic.org/second-circuit-affirms-fcc-privacy-authorities-over-subscriber-location-data-similar-to-recent-dc-circuit-decision/), finding nothing in the FCC's proceedings "transgressed the Seventh Amendment's jury trial guarantee." The Second Circuit reasoned that because collection requires a DOJ-filed civil suit, the Seventh Amendment right is preserved at the enforcement stage.

The [DC Circuit had similarly upheld](https://epic.org/dc-circuit-affirms-fcc-privacy-authorities-in-location-data-action-against-sprint-t-mobile/) the FCC's authority in the consolidated Sprint/T-Mobile appeals. On January 9, 2026, the Supreme Court granted certiorari to resolve the split.

## April 21 Oral Arguments [HIGH confidence]

### The Carriers' Position

Jeffrey B. Wall, arguing for AT&T and Verizon, contended that the Forfeiture Order itself is binding and coercive — that companies, faced with millions of dollars in FCC-assessed penalties, face enormous pressure to pay rather than wait indefinitely for a DOJ civil suit that may never come. Wall argued this practical reality strips companies of a meaningful jury trial right. AT&T and Verizon's position was bolstered by *Loper Bright Enterprises v. Raimondo*, 603 U.S. 369 (2024), which eliminated judicial deference to agency interpretations and, along with *Jarkesy*, has emboldened challenges to agency adjudicatory authority.

### The Government's Position

Vivek Suri, arguing for the Trump administration and the FCC, urged the Court to distinguish *Jarkesy*: unlike the SEC, which could collect its own penalties through in-house proceedings, the FCC must go to federal district court to collect any forfeiture order. At that point, the carrier gets a full jury trial. Suri argued the Forfeiture Order is therefore not self-executing and does not deprive the carriers of Seventh Amendment rights.

### How the Justices Responded

According to [SCOTUSblog's reporting](https://www.scotusblog.com/2026/04/court-appears-skeptical-of-right-to-jury-trial-in-fcc-proceedings/) and [Roll Call coverage](https://rollcall.com/2026/04/21/supreme-court-sounds-ready-to-back-agency-authority-over-violations/), the Court appeared broadly skeptical of the carriers' position:

- **Chief Justice John Roberts** suggested the FCC Forfeiture Order might amount to no more than a public finding that the company "did something bad" — a reputational sanction rather than a legally binding obligation — and characterized the carriers' resistance to FCC proceedings as driven by "bad PR" concerns.

- **Justice Brett Kavanaugh** acknowledged the "government's in retreat" on its characterization of the orders, but questioned whether the Seventh Amendment is even implicated when a full de novo jury trial is available in the DOJ enforcement suit: "When the government seeks a penalty, it would seem that, so long as you get a de novo jury trial, that the Seventh Amendment and Article III would be satisfied."

- **Justice Samuel Alito** noted the FCC's civil forfeiture process, in place since 1960, appears "quite different" from a common-law lawsuit that would have required a jury at the founding.

- **Justice Amy Coney Barrett** compared the carriers' situation to a plea bargain in a criminal case — the company can pay and avoid trial, but the option for a jury trial remains.

- **Justice Ketanji Brown Jackson** challenged Wall's framing that the Forfeiture Order is "binding," telling him the agency's order looks more like a "charge" the companies could pay or contest — not a final judgment.

No justice appeared ready to embrace the carriers' broadest argument. [Newsweek](https://www.newsweek.com/verizon-att-lawsuit-fcc-supreme-court-john-roberts-11860787) and [US News & World Report](https://www.usnews.com/news/top-news/articles/2026-04-21/us-supreme-court-to-assess-fcc-power-to-fine-in-clash-with-wireless-carriers) also reported the Court "leans toward FCC" based on the argument dynamics.

## Key Legal Issues [HIGH confidence]

### Distinguishing *Jarkesy*

The pivotal distinction from *Jarkesy* is the FCC's lack of independent collection authority. In *Jarkesy*, the SEC could obtain disgorgement and civil penalties through its own administrative tribunals without going to federal court. The FCC, by contrast, requires DOJ to file a civil enforcement suit — giving defendants a jury trial at the enforcement stage. The constitutional question is whether the Forfeiture Order itself, issued before any jury trial, constitutes the actionable deprivation of a Seventh Amendment right.

### Article III and Agency Adjudication

AT&T and Verizon also raised an Article III claim that the FCC's in-house adjudicators — not life-tenured federal judges — are constitutionally prohibited from making binding factual determinations regarding civil liability. The argument echoes the broader assault on the administrative state accelerated by *Loper Bright*, *Jarkesy*, and related decisions since 2022.

### The "Binding" Orders Question

A subsidiary question — whether the Forfeiture Order is legally "binding" before DOJ enforcement — may determine the outcome. If the Court holds the order is merely precatory (advisory), the Seventh Amendment is not triggered until DOJ files suit. If binding, it must be accompanied by jury trial rights. Oral argument suggests several justices lean toward the former view.

## Broader Implications [MEDIUM confidence]

### For FCC Enforcement Authority

A ruling for the FCC would preserve the agency's current enforcement architecture across all its substantive mandates — CPNI privacy, equal employment, indecency, spectrum rules, and broadband policy. If the carriers prevail, the FCC could be forced to route all monetary penalty cases through DOJ, dramatically slowing enforcement timelines and reducing deterrence. [Davis Wright Tremaine](https://www.dwt.com/blogs/broadband-advisor/2026/02/supreme-court-review-fcc-penalty-authority) notes a pro-carrier ruling could also chill pending enforcement actions across all four wireless carriers (T-Mobile and Sprint have separate pending challenges in the DC Circuit).

### For the Administrative State Broadly

Other agencies that use similar two-stage enforcement models — notice of violation followed by DOJ-enforced collection — may be affected. However, the FCC's structure is meaningfully distinct from the SEC model invalidated in *Jarkesy*, and oral argument suggests the Court is unlikely to extend *Jarkesy* to agencies that lack independent collection authority.

### For Telecom Privacy Compliance

The carriers' underlying conduct — delegating consent obligations to aggregators and failing to audit downstream data use — remains a compliance risk regardless of the constitutional outcome. The [FCC's enforcement advisory framework](https://www.fcc.gov/general/enforcement-primer) for CPNI has not been rescinded, and state attorneys general (including California, whose [2025 location data sweep](https://www.globalpolicywatch.com/2026/01/fcc-privacy-enforcement-may-face-more-constitutional-scrutiny-supreme-court-review-of-fcc-cpni-fines-sought-amid-circuit-split/) targeted the same data flows) retain independent authority to act.

## Action Items

- **Monitor for decision by late June 2026.** A ruling upholding FCC enforcement authority would validate the $103 million in fines and confirm the FCC's CPNI enforcement model going forward.
- **Telecoms and data aggregators:** Review current location data sharing arrangements against Section 222 CPNI consent requirements regardless of the constitutional outcome. The FCC's substantive findings on carrier liability have not been challenged on the merits.
- **Companies in other regulated sectors:** Assess whether your regulatory agency uses a *Jarkesy*-style self-executing penalty system (SEC/FTC model) or a *FCC*-style DOJ-enforcement model, as the constitutional risk profile differs significantly.
- **Compliance officers:** Prepare for potential enforcement expansion. If the Court upholds the FCC, the Commission may reinvigorate CPNI enforcement stalled since the Fifth Circuit's 2025 ruling. Commissioner Simington's dissents from all FCC penalty actions (arguing *Jarkesy* rendered them unconstitutional) would be invalidated.
- **Track T-Mobile/Sprint DC Circuit appeals**, which remain pending and may be resolved in light of the Supreme Court's forthcoming ruling.

## Related Reports

- [FCC 2024 Net Neutrality Order Extends Section 222 Privacy Protections to Broadband -- Then Gets Vacated](../federal-fcc-net-neutrality-cpni-broadband-2024-05-23.md) — Covers the FCC's 2024 attempt to extend Section 222 CPNI protections to broadband providers, the same statutory framework at issue in the AT&T/Verizon forfeiture orders.
- [California AG Launches CCPA Investigative Sweep Targeting Location Data Industry](california-ag-location-data-sweep-2025-03-10.md) — State enforcement targeting the same location data aggregator ecosystem examined in the FCC's 2024 forfeiture orders; illustrates parallel enforcement risk even if FCC authority is curtailed.
- [DOJ Urges First Circuit to Uphold VPPA Against First Amendment Challenge in Hearst Appeal](../doj-vppa-first-circuit-brief-2026-04-12.md) — Related DOJ litigation posture defending federal privacy enforcement mechanisms in circuit courts.

## Sources

1. [SCOTUSblog — "Court appears skeptical of right to jury trial in FCC proceedings" (April 2026)](https://www.scotusblog.com/2026/04/court-appears-skeptical-of-right-to-jury-trial-in-fcc-proceedings/) — Primary oral argument recap with justice-by-justice analysis
2. [SCOTUSblog — "Justices to hear argument on right to jury trial in FCC proceedings"](https://www.scotusblog.com/2026/04/justices-to-hear-argument-on-right-to-jury-trial-in-fcc-proceedings/) — Pre-argument case preview with constitutional framing
3. [SCOTUSblog — Case page: *Verizon Communications Inc. v. FCC* (No. 25-567)](https://www.scotusblog.com/cases/verizon-communications-inc-v-federal-communications-commission/) — Official docket and case tracking
4. [SCOTUSblog — Case page: *FCC v. AT&T, Inc.* (No. 25-406)](https://www.scotusblog.com/cases/federal-communications-commission-v-att-inc-2/) — Official docket and case tracking
5. [Supreme Court — Combined Reply Brief, Nos. 25-406 and 25-567 (April 10, 2026)](https://www.supremecourt.gov/DocketPDF/25/25-406/404083/20260410070726142_ATT%20Verizon%20-%20Combined%20Reply%20Brief%20-%20for%20efiling.pdf) — Official AT&T/Verizon reply brief
6. [Supreme Court — Docket for No. 25-406 (*FCC v. AT&T, Inc.*)](https://www.supremecourt.gov/docket/docketfiles/html/public/25-406.html) — Official Supreme Court docket
7. [Verizon Cert Petition, No. 25-567 (Nov. 6, 2025)](https://www.supremecourt.gov/DocketPDF/25/25-567/383709/20251106103552667_Verizon%20-%20Cert%20Petition%20and%20Appendix%20-%20To%20E-file.pdf) — Verizon's petition for certiorari setting out constitutional arguments
8. [FCC — "FCC Fines Largest Wireless Carriers for Sharing Location Data" (April 29, 2024)](https://www.fcc.gov/document/fcc-fines-largest-wireless-carriers-sharing-location-data) — Official FCC press release on the 2024 forfeiture orders
9. [FCC — Forfeiture Order press release document (DOC-402213A1)](https://docs.fcc.gov/public/attachments/DOC-402213A1.pdf) — Official FCC document summarizing all four carrier fines
10. [Krebs on Security — "FCC Fines Major U.S. Wireless Carriers for Selling Customer Location Data" (April 2024)](https://krebsonsecurity.com/2024/04/fcc-fines-major-u-s-wireless-carriers-for-selling-customer-location-data/) — Technical background on aggregator scheme and Securus/LocationSmart origins
11. [Davis Wright Tremaine — "5th Circuit Holds That Jarkesy Invalidates FCC Forfeiture Order Against AT&T" (May 2025)](https://www.dwt.com/blogs/broadband-advisor/2025/05/5th-circuit-invalidates-fcc-forfeiture-jarkesy) — Law firm analysis of the Fifth Circuit ruling
12. [Davis Wright Tremaine — "Supreme Court Schedules Argument in FCC CPNI Civil Forfeiture Cases" (Feb. 2026)](https://www.dwt.com/blogs/broadband-advisor/2026/02/supreme-court-review-fcc-penalty-authority) — Pre-argument analysis of constitutional stakes and enforcement implications
13. [Perkins Coie — "Fifth Circuit Rules FCC Enforcement Action Unconstitutional"](https://perkinscoie.com/insights/update/fifth-circuit-rules-fcc-enforcement-action-unconstitutional) — Law firm analysis of Fifth Circuit decision on Jarkesy extension to FCC
14. [Perkins Coie — "Post-Jarkesy, Circuits Diverge on Whether the FCC's Enforcement Process Is Constitutional"](https://perkinscoie.com/insights/update/post-jarkesy-circuits-diverge-whether-fccs-enforcement-process-constitutional) — Circuit split analysis (Fifth vs. Second vs. DC Circuits)
15. [Roll Call — "Supreme Court sounds ready to back agency authority over violations" (April 21, 2026)](https://rollcall.com/2026/04/21/supreme-court-sounds-ready-to-back-agency-authority-over-violations/) — Post-argument news coverage
16. [Newsweek — "John Roberts calls FCC fines case against Verizon, AT&T a 'PR problem'" (April 2026)](https://www.newsweek.com/verizon-att-lawsuit-fcc-supreme-court-john-roberts-11860787) — Roberts quote and post-argument analysis
17. [US News & World Report — "US Supreme Court Leans Toward FCC in Clash With Wireless Carriers Over Fines" (April 21, 2026)](https://www.usnews.com/news/top-news/articles/2026-04-21/us-supreme-court-to-assess-fcc-power-to-fine-in-clash-with-wireless-carriers) — Post-argument coverage
18. [JURIST — "US Supreme Court weighs whether FCC can impose massive penalties without a jury trial" (April 21, 2026)](https://www.jurist.org/news/2026/04/us-supreme-court-weighs-whether-fcc-can-impose-massive-penalties-without-a-jury-trial-scotus-dispatch/) — Post-argument analysis and SCOTUS dispatch
19. [Global Policy Watch — "FCC Privacy Enforcement May Face More Constitutional Scrutiny" (Jan. 2026)](https://www.globalpolicywatch.com/2026/01/fcc-privacy-enforcement-may-face-more-constitutional-scrutiny-supreme-court-review-of-fcc-cpni-fines-sought-amid-circuit-split/) — Pre-certiorari analysis of the circuit split and FCC enforcement risk
20. [EPIC — "Second Circuit Affirms FCC Privacy Authorities Over Subscriber Location Data"](https://epic.org/second-circuit-affirms-fcc-privacy-authorities-over-subscriber-location-data-similar-to-recent-dc-circuit-decision/) — Second Circuit ruling upholding Verizon fine
21. [EPIC — "DC Circuit Affirms FCC Privacy Authorities in Location Data Action Against Sprint/T-Mobile"](https://epic.org/dc-circuit-affirms-fcc-privacy-authorities-in-location-data-action-against-sprint-t-mobile/) — DC Circuit ruling consistent with Second Circuit
22. [Constitutional Accountability Center — Case overview page](https://www.theusconstitution.org/litigation/federal-communications-commission-v-att-and-verizon-v-federal-communications-commission/) — Advocacy organization case tracking
23. [FCC — Enforcement Primer (general enforcement process)](https://www.fcc.gov/general/enforcement-primer) — Official description of FCC's two-stage forfeiture process
