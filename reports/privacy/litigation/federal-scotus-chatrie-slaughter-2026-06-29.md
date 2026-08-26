---
title: "Supreme Court Rules Geofence Warrants Are Fourth Amendment Searches and Upholds Trump's Removal of FTC Commissioner Slaughter"
date: 2026-06-29
jurisdiction: "Federal"
category: "privacy"
development_type: "litigation"
finding_id: "SCAN-20260717-001"
topic_key: "FTC-ACCESS-TO-LOCATION-DATA-AND-2026"
topic_type: "enforcement"
first_reported: 2026-06-29
last_updated: "2026-07-17"
status_history:
  - {date: "2026-07-17", status: "unsettled_commentary", finding_id: "SCAN-20260717-021", run_id: "2026-07-17T13-54-18"}
cluster: "Geofence Warrants and the Fourth Amendment: Chatrie v. United States"
cluster_slug: "geofence-warrant-fourth-amendment-scotus"
---

# Supreme Court Rules Geofence Warrants Are Fourth Amendment Searches and Upholds Trump's Removal of FTC Commissioner Slaughter

**Jurisdiction:** Federal | **Category:** Privacy | **Date:** 2026-06-29

## Summary [HIGH confidence]

On June 29, 2026, the U.S. Supreme Court issued two decisions with major implications for privacy law and administrative law. In [*Chatrie v. United States*](https://www.supremecourt.gov/opinions/25pdf/25-112_0am4.pdf), No. 25-112, the Court held 6-3, in an opinion by Justice Kagan, that police conducted a Fourth Amendment "search" when they obtained a geofence warrant compelling Google to disclose location data for devices near a Virginia credit union robbery — holding that individuals retain a reasonable expectation of privacy in digital location data even when a third party (Google) holds it ([SCOTUSblog](https://www.scotusblog.com/2026/06/court-rules-that-law-enforcements-use-of-geofence-warrant-was-a-search/); [Justia](https://supreme.justia.com/cases/federal/us/609/25-112/)). In [*Trump v. Slaughter*](https://www.supremecourt.gov/opinions/25pdf/25-332_qn12.pdf), No. 25-332, the Court held 6-3, in an opinion by Chief Justice Roberts, that statutory "for-cause" removal protections for Federal Trade Commission commissioners are unconstitutional, overruling the 91-year-old precedent *Humphrey's Executor v. United States* (1935) and upholding President Trump's removal of Commissioner Rebecca Slaughter ([SCOTUSblog](https://www.scotusblog.com/2026/06/court-allows-trump-to-fire-ftc-commissioner-and-overturns-major-restraint-on-presidential-power/); [Wikipedia case summary](https://en.wikipedia.org/wiki/Trump_v._Slaughter)). Together, the rulings reshape both the Fourth Amendment framework governing law-enforcement access to location data and the independence of the FTC as a regulator — the latter with immediate knock-on effects for the EU-U.S. Data Privacy Framework.

## Key Facts: Chatrie v. United States [HIGH confidence]

- The case arose from a 2019 armed robbery of a credit union in Midlothian, Virginia, where investigators obtained a geofence warrant directing Google to disclose location data for all devices within a 150-meter radius of the bank during a 30-minute window, narrowing an initial 19 accounts down to identifying information for 3 accounts, including Chatrie's ([SCOTUSblog case page](https://www.scotusblog.com/cases/chatrie-v-united-states/)).
- The Court held that the police conducted a Fourth Amendment search when obtaining Chatrie's location information from Google, extending the reasoning of *Carpenter v. United States* (2018) to hold that individuals have a reasonable expectation of privacy in location data even for short time periods and even when a third party stores that data ([SCOTUSblog](https://www.scotusblog.com/2026/06/court-rules-that-law-enforcements-use-of-geofence-warrant-was-a-search/)).
- The judgment was vacated and remanded, 6-3, in an opinion authored by Justice Kagan. Justice Jackson wrote a concurrence joined by Justice Sotomayor; Justice Gorsuch concurred in the judgment; Justice Alito dissented (joined by Justice Thomas as to Part I and by Justice Barrett as to portions of Part II) ([Justia](https://supreme.justia.com/cases/federal/us/609/25-112/)).
- The Court did **not** hold that geofence warrants are categorically unconstitutional, and it stopped short of specifying what a valid geofence warrant must contain — leaving the particularity and scope questions for further development on remand and in lower courts ([Just Security analysis](https://www.justsecurity.org/145214/chatrie-fourth-amendment-supreme-court/)).
- This decision resolves the case previously covered in [Zwiad's report on the April 27, 2026 oral arguments](federal-chatrie-geofence-warrant-2026-04-28.md), which detailed the underlying facts, circuit split, and argument dynamics in depth.

## Key Facts: Trump v. Slaughter [HIGH confidence]

- President Trump removed FTC Commissioners Rebecca Slaughter and Alvaro Bedoya early in his second term without invoking the statutory for-cause standard. Slaughter sued, and the U.S. District Court for the District of Columbia granted summary judgment restoring her to office; the Supreme Court reversed ([Congressional Research Service, LSB11448](https://www.congress.gov/crs-product/LSB11448)).
- The Court held 6-3 that the FTC Act's "for-cause" removal restriction violates separation-of-powers principles because FTC commissioners exercise executive power and therefore "must be removable by the President at will." Chief Justice Roberts wrote the majority opinion, joined by Alito, Gorsuch, Kavanaugh, and Barrett, with Thomas joining all but Part III-B ([SCOTUSblog](https://www.scotusblog.com/2026/06/court-allows-trump-to-fire-ftc-commissioner-and-overturns-major-restraint-on-presidential-power/)).
- The decision expressly overrules *Humphrey's Executor v. United States*, 295 U.S. 602 (1935), which for 91 years had permitted Congress to shield multi-member independent agency heads from at-will presidential removal ([Ogletree Deakins](https://ogletree.com/insights-resources/blog-posts/supreme-court-holds-ftcs-for-cause-removal-protections-violate-separation-of-powers/)).
- Justice Gorsuch wrote a 16-page concurrence urging Congress and the courts to "recover" legislative and judicial powers he says have been ceded to the executive branch. Justice Sotomayor dissented, joined by Justices Kagan and Jackson, warning that Congress created multi-member agencies like the FTC to operate with independence from "absolute partisan control" ([SCOTUSblog](https://www.scotusblog.com/2026/06/court-allows-trump-to-fire-ftc-commissioner-and-overturns-major-restraint-on-presidential-power/)).
- The ruling's reasoning extends beyond the FTC to other multi-member, commission-style agencies exercising executive power — including rulemaking, litigation, and adjudicatory authority — raising questions about removal protections at agencies such as the SEC, NLRB, and CPSC ([Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/07/what-the-trump-v-slaughter-decision-means-for-independent)).

## EU-U.S. Data Privacy Framework Impact [HIGH confidence]

- The European Commission's adequacy decision for the EU-U.S. Data Privacy Framework (DPF) cited the FTC's independence as a structural safeguard underpinning U.S. commitments on data protection oversight; reporting indicates the FTC's independence was referenced roughly 259 times in the Commission's adequacy determination ([IAPP — "After Slaughter: FTC independence and EU-US DPF face potential challenges"](https://iapp.org/news/a/after-slaughter-ftc-independence-and-eu-us-dpf-face-potential-challenges)).
- Privacy advocacy group noyb (led by Max Schrems) sent a letter to the European Commission dated June 30, 2026, arguing that no other U.S. authority can remedy the loss of FTC independence, and announced it will file a legal challenge to the DPF before the Court of Justice of the European Union (CJEU), urging the Commission to withdraw the adequacy decision immediately — a step commentators are calling a potential "Schrems III" case ([noyb](https://noyb.eu/en/us-supreme-court-just-blew-eu-us-data-transfers); [Captain Compliance](https://captaincompliance.com/news/max-schrems-preps-schrems-iii-why-the-eu-us-data-privacy-framework-faces-its-biggest-threat-yet/)).
- IAPP has published a countervailing view cautioning that *Trump v. Slaughter* "does not undo" the DPF's separate individual-redress mechanism (the Data Protection Review Court), suggesting the practical legal impact on the adequacy decision remains contested and will likely be tested in EU courts rather than resolved immediately ([IAPP — "No, Trump v. Slaughter does not undo the EU-US data-transfer redress mechanism"](https://iapp.org/news/a/no-trump-v-slaughter-does-not-undo-the-eu-us-data-transfer-redress-mechanism)).
- Because the CJEU challenge had not been filed as of this writing, this section reflects analyst commentary and advocacy-group statements rather than an adjudicated outcome; readers should treat DPF-survival predictions as unsettled pending formal EU Commission or CJEU action.

## Action Items

- **Companies responding to geofence warrants (technology, telecom, app developers):** Update warrant-response protocols to reflect that geofence requests are now presumptively subject to Fourth Amendment scrutiny. Legal teams should require particularity analysis before complying and consult counsel on narrowing overbroad requests, since *Chatrie* leaves open what constitutes a constitutionally sufficient geofence warrant.
- **Law enforcement agencies:** Consult counsel before issuing new geofence warrants; build in narrower, more particularized requests pending further guidance from lower courts on remand.
- **Companies relying on the EU-U.S. Data Privacy Framework for cross-border transfers:** Monitor the European Commission's response and any noyb/CJEU challenge closely. Consider layering supplementary transfer safeguards (e.g., standard contractual clauses) as a contingency in case the adequacy decision is suspended or annulled.
- **Compliance and government-affairs teams:** Track FTC leadership and enforcement-priority changes now that commissioners serve at the President's pleasure; expect greater volatility in FTC enforcement posture across administrations.

## Related Reports

- [Supreme Court Hears Arguments in Chatrie v. United States on Constitutionality of Geofence Warrants](federal-chatrie-geofence-warrant-2026-04-28.md) -- This report is the direct sequel: it covers the April 27, 2026 oral arguments in the same case now resolved by the June 29, 2026 decision summarized above.
- [Virginia Bans Sale of Precise Geolocation Data: VCDPA Amendment SB 338 Signed Into Law](../state-comprehensive-laws/virginia-sb338-vcdpa-geolocation-ban-2026-04-19.md) -- Virginia's statutory restriction on commercial sale of precise geolocation data complements the constitutional protection against law-enforcement access recognized in *Chatrie*.
- [FTC Strategic Plan FY2026-2030](../enforcement-actions/ftc-strategic-plan-fy2026-2030-2026-04-13.md) -- Directly relevant to understanding how FTC enforcement priorities may shift given the agency's newly confirmed lack of independence from presidential control under *Trump v. Slaughter*.
- [FTC Ferguson Privacy Enforcement Surge](../enforcement-actions/federal-ftc-ferguson-privacy-enforcement-surge-2026-06-28.md) -- Documents the FTC's recent enforcement trajectory under Chairman Ferguson, relevant context for assessing how at-will removal authority may affect future enforcement direction.

## Sources

1. [Supreme Court of the United States — Chatrie v. United States opinion, No. 25-112 (June 29, 2026)](https://www.supremecourt.gov/opinions/25pdf/25-112_0am4.pdf) -- Official slip opinion.
2. [SCOTUSblog — "Court rules that law enforcement's use of 'geofence warrant' was a 'search'"](https://www.scotusblog.com/2026/06/court-rules-that-law-enforcements-use-of-geofence-warrant-was-a-search/) -- Primary case analysis of the Chatrie decision, vote count, and opinion authorship.
3. [Justia — Chatrie v. United States, 609 U.S. ___ (2026)](https://supreme.justia.com/cases/federal/us/609/25-112/) -- Case summary including concurrence/dissent breakdown.
4. [Just Security — "Fencing with Fourth Amendment: Unpacking the Supreme Court's Chatrie Decision"](https://www.justsecurity.org/145214/chatrie-fourth-amendment-supreme-court/) -- Legal analysis of the decision's scope and limitations.
5. [SCOTUSblog — Chatrie v. United States case page (25-112)](https://www.scotusblog.com/cases/chatrie-v-united-states/) -- Case docket and background facts.
6. [Supreme Court of the United States — Trump v. Slaughter opinion, No. 25-332 (June 29, 2026)](https://www.supremecourt.gov/opinions/25pdf/25-332_qn12.pdf) -- Official slip opinion.
7. [SCOTUSblog — "Supreme Court allows Trump to fire FTC commissioner and overturns major restraint on presidential power"](https://www.scotusblog.com/2026/06/court-allows-trump-to-fire-ftc-commissioner-and-overturns-major-restraint-on-presidential-power/) -- Primary case analysis of the Slaughter decision, vote count, and opinion authorship.
8. [Congress.gov CRS Legal Sidebar LSB11448 — "Trump v. Slaughter and the Future of For-Cause Removal Protections"](https://www.congress.gov/crs-product/LSB11448) -- Congressional Research Service background and procedural history.
9. [Wikipedia — Trump v. Slaughter](https://en.wikipedia.org/wiki/Trump_v._Slaughter) -- General case summary corroborating holding and reasoning.
10. [Ogletree Deakins — "Supreme Court Holds FTC's 'For-Cause' Removal Protections Violate Separation of Powers"](https://ogletree.com/insights-resources/blog-posts/supreme-court-holds-ftcs-for-cause-removal-protections-violate-separation-of-powers/) -- Law firm analysis of holding and practical implications.
11. [Holland & Knight — "What the Trump v. Slaughter Decision Means for Independent Agency-Regulated Companies"](https://www.hklaw.com/en/insights/publications/2026/07/what-the-trump-v-slaughter-decision-means-for-independent) -- Law firm analysis of implications for other independent agencies.
12. [IAPP — "After Slaughter: FTC independence and EU-US DPF face potential challenges"](https://iapp.org/news/a/after-slaughter-ftc-independence-and-eu-us-dpf-face-potential-challenges) -- Analysis of DPF adequacy risk following the decision.
13. [IAPP — "No, Trump v. Slaughter does not undo the EU-US data-transfer redress mechanism"](https://iapp.org/news/a/no-trump-v-slaughter-does-not-undo-the-eu-us-data-transfer-redress-mechanism) -- Countervailing analysis on the scope of DPF impact.
14. [noyb — "US Supreme Court just blew up EU-US Data Transfers"](https://noyb.eu/en/us-supreme-court-just-blew-eu-us-data-transfers) -- Advocacy group statement and letter to the European Commission announcing planned CJEU challenge.
15. [Captain Compliance — "Max Schrems Preps 'Schrems III'"](https://captaincompliance.com/news/max-schrems-preps-schrems-iii-why-the-eu-us-data-privacy-framework-faces-its-biggest-threat-yet/) -- Secondary reporting on the anticipated CJEU challenge to the DPF.
16. [Zwiad report — Supreme Court Hears Arguments in Chatrie v. United States (April 28, 2026)](federal-chatrie-geofence-warrant-2026-04-28.md) -- Internal prior report on the oral-argument stage of the same case.

## Update 2026-07-17

**Change:** unsettled_commentary → unsettled_commentary
**Source:** http://info.iapp.org/MTM4LUVaTS0wNDIAAAGi3IrxjmpAxHGlVfHnfsJHzhgg3M-9j6CstrXwfJvWbVE6vYSzRWI1uTxnDhEVPXdeTUsgIH0=
**Summary:** At an IAPP LinkedIn Live panel on 6 July 2026 hosted by IAPP Managing Director Cobun Zweifel-Keegan with Wilson Sonsini Goodrich & Rosati partner and former FTC Division of Privacy and Identity Protection head Maneesha Mithal, panelists discussed downstream effects of Trump v. Slaughter on FTC independence and the EU-U.S. Data Privacy Framework. One panelist noted the FTC now has a strong incentive to fast-track pending investigations and settlement negotiations to closure before the end of the current administration, given uncertainty over how a future administration might handle unresolved settlement discussions. The panel otherwise reinforced the DPF-adequacy concerns already reflected in this report's EU-U.S. Data Privacy Framework Impact section, without altering the substantive legal analysis.
**Finding ID:** SCAN-20260717-021
**Run ID:** 2026-07-17T13-54-18
