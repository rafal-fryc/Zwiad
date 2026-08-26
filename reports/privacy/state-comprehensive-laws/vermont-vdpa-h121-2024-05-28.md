---
title: "Vermont Data Privacy Act (H.121): One of the Most Stringent State Privacy Laws Passed, Then Vetoed"
date: 2024-05-28
jurisdiction: "Vermont"
category: "privacy"
development_type: "legislation"
finding_id: "SCAN-20240528-006"
topic_key: "vermont-a3af5bfe-2024"
topic_type: "state_bill"
first_reported: 2024-05-28
last_updated: 2026-04-15
status_history:
  - "2026-04-15: Corrected data broker non-registration penalty from '$10,000 per day' to '$50 per day, not to exceed $10,000 per year' per 9 V.S.A. § 2446; clarified that the $25,000 materially-incorrect-filing penalty is proposed (H.211, 2025-2026) not enacted law."
cluster: "Vermont H.121: Data Privacy Act (Passed and Vetoed, 2024)"
cluster_slug: "vermont-h121-data-privacy-act-2024"
---

# Vermont Data Privacy Act (H.121): One of the Most Stringent State Privacy Laws Passed, Then Vetoed

**Jurisdiction:** Vermont | **Category:** Privacy | **Date:** 2024-05-28

## Executive Summary [HIGH confidence]

Just past midnight on May 11, 2024, the Vermont legislature passed H.121, "An act relating to enhancing consumer privacy and the age-appropriate design code," creating what would have been the most stringent comprehensive consumer privacy law in the United States. Vermont's bill combined a Connecticut-style privacy framework with Maryland-inspired data minimization, Washington-modeled consumer health data protections, an Age-Appropriate Design Code for minors, and — most controversially — a private right of action for consumers to sue data brokers and large data holders directly. Governor Phil Scott vetoed the bill on June 13, 2024, citing the private right of action as an undue burden on Vermont businesses. The House voted 128-17 to override, but the Senate sustained the veto 14-15, falling six votes short. H.121 is dead. Vermont remains the only New England state with a significant data privacy statute — its 2018 data broker registration law — but no enacted comprehensive consumer privacy framework.

## Background [HIGH confidence]

Vermont has a longer data privacy history than is often acknowledged. In 2018, Vermont enacted [9 V.S.A. § 2430](https://legislature.vermont.gov/statutes/section/09/062/02430), one of the first state data broker registration statutes in the country, requiring any business that knowingly collects and sells or licenses the brokered personal information of consumers with whom it has no direct relationship to register annually with the Vermont Attorney General and pay a registration fee. That 2018 law imposed no consumer-facing rights and no general controller obligations, but it established Vermont as an active participant in data privacy regulation from an early date.

Beginning in the 2022-2023 legislative biennium, Vermont lawmakers launched efforts to build a comprehensive consumer privacy statute on top of the data broker registration foundation. H.121 was introduced in the 2023-2024 session and moved through committee hearings over roughly 18 months, incorporating testimony from consumer advocacy groups, technology industry representatives, small business organizations, and the Vermont Attorney General's office. The [Electronic Privacy Information Center (EPIC)](https://epic.org/vermont-house-unanimously-passes-vermont-data-privacy-act/) reported that the House passed H.121 unanimously — a remarkable degree of consensus for such broad privacy legislation. The Senate passed a final version immediately prior to the close of the legislative session in the early morning hours of May 11, 2024.

Vermont's bill was introduced during a period of heightened state privacy activity nationwide. In 2024 alone, [Maryland's Online Data Privacy Act (MODPA)](https://legiscan.com/MD/bill/SB0541/2024) was signed into law, widely described as the strictest enacted comprehensive privacy statute in the country. [Kentucky enacted its Consumer Data Protection Act](https://apps.legislature.ky.gov/record/24rs/hb15.html), [Nebraska passed the Nebraska Data Privacy Act](https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=54479), and [Minnesota enacted the Minnesota Consumer Data Privacy Act](https://www.revisor.mn.gov/bills/bill.php?f=HF4757&y=2024&ssn=0&b=house). Vermont's H.121 was drafted with awareness of all these parallel efforts and was designed to establish a new ceiling for state privacy protection.

## Detailed Analysis [HIGH confidence]

### Applicability Thresholds

The [full text of H.121 as passed by both chambers](https://legislature.vermont.gov/Documents/2024/Docs/BILLS/H-0121/H-0121%20As%20Passed%20by%20Both%20House%20and%20Senate%20Unofficial.pdf) sets out a tiered applicability framework keyed to the number of Vermont consumers whose data is controlled or processed per calendar year:

| Effective Date | Consumer Threshold (standalone) | Consumer Threshold + Revenue Trigger |
|---|---|---|
| July 1, 2025 | 100,000 consumers | 25,000 consumers + >25% gross revenue from data sales |
| July 1, 2026 | 50,000 consumers | 12,500 consumers + >20% gross revenue from data sales |
| July 1, 2027 | 25,000 consumers | 6,250 consumers + >20% gross revenue from data sales |

Notably, the tiered threshold structure was designed to gradually pull in more businesses over time while giving smaller entities runway to prepare. Vermont's population of approximately 650,000 means the initial 100,000-consumer threshold would have applied almost exclusively to large national actors processing data of a significant fraction of Vermont residents.

Several provisions of H.121 carried **no applicability threshold at all**: provisions governing consumer health data, minors' personal data, and data broker obligations applied to any person conducting business in Vermont or targeting products or services at Vermont residents regardless of the volume of data processed. This no-threshold approach for health and children's data was among the most aggressive aspects of the bill.

### Consumer Rights

H.121 granted Vermont consumers the following rights, modeled on the Connecticut Data Privacy Act framework but with significant additions ([Hall Booth Smith analysis](https://hallboothsmith.com/vermont-data-privacy-act-vdpa/)):

- **Right to confirm and access** personal data being processed about them
- **Right to correct** inaccurate personal data
- **Right to delete** personal data provided by or obtained about the consumer
- **Right to data portability** in a portable and readily usable format
- **Right to opt out** of targeted advertising, sale of personal data, and profiling in furtherance of automated decisions with legal or similarly significant effects
- **Right to obtain a list of third parties** to which the controller has disclosed their personal data — a provision not present in most state laws
- **Right to opt out via universal opt-out mechanisms**, including the [Global Privacy Control (GPC)](https://globalprivacycontrol.org/) browser signal — controllers would have been required to honor GPC preferences

Controllers would have had 45 days to respond to requests, extendable by 45 additional days when reasonably necessary. They would also have been required to establish an appeal mechanism for denied requests. These timelines mirror the Connecticut model.

### Data Minimization [HIGH confidence]

Among H.121's most significant departures from the Virginia-model state privacy law template was its robust data minimization requirement. Rather than permitting collection and processing of personal data for any purpose disclosed in a privacy notice, H.121 required controllers to limit collection of personal data to what is "reasonably necessary and proportionate to provide or maintain a specific product or service requested by the consumer" — meaning that collecting data in anticipation of possible future products or services, or for internal research unrelated to the consumer's requested service, would have been prohibited.

This formulation tracks Maryland's MODPA, which uses similar language, and is significantly more restrictive than the minimization language in Virginia, Colorado, or Connecticut privacy laws, which generally prohibit processing for purposes "incompatible" with the disclosed purpose but do not restrict the scope of initial collection. [McDermott Will & Emery's analysis](https://www.mcdermottlaw.com/insights/mixing-things-up-like-a-certain-ice-cream-maker-vermont-passes-consumer-data-privacy-law/) described this as making H.121 one of the most data-minimization-intensive laws in the United States.

### Sensitive Data [HIGH confidence]

H.121 defined sensitive data to include:
- Racial or ethnic origin
- Religious or philosophical beliefs
- Mental or physical health diagnosis
- Sexual orientation or gender identity
- Citizenship or immigration status
- Genetic data or biometric data processed to uniquely identify an individual
- Precise geolocation data (within 1,750 feet)
- Financial information beyond general income/salary
- Personal data of known children

For most sensitive data categories, H.121 required affirmative **opt-in consent** before processing — consistent with other states. However, H.121 took the additional step of **prohibiting the sale of sensitive data entirely**, even where the consumer had consented. This outright prohibition on selling sensitive data, regardless of consent, had no direct precedent in other enacted comprehensive state privacy laws and was among the provisions drawing the strongest business opposition.

### Consumer Health Data Protections [HIGH confidence]

H.121 included a dedicated subchapter on consumer health data, tracking the approach of Washington's [My Health My Data Act (MHMDA)](https://app.leg.wa.gov/RCW/default.aspx?cite=19.373). Key provisions included:

- Prohibition on disclosing consumer health data to third parties except with affirmative authorization from the consumer
- Prohibition on geofencing within 1,850 feet of health care facilities to serve health-related advertising to consumers who are or were physically present in that location
- Confidentiality obligations for entities that receive consumer health data from another covered entity
- No applicability threshold — these provisions applied to any person doing business in Vermont or targeting Vermont residents, regardless of data processing volume

### Private Right of Action [HIGH confidence]

The most contested feature of H.121 was a limited [private right of action](https://www.hunton.com/privacy-and-information-security-law/vermont-legislature-passes-state-privacy-bill-with-right-to-sue-for-consumers) allowing consumers to sue in Vermont state court for:

- Processing sensitive data without the required consent
- Violating COPPA with respect to a child's sensitive personal data
- Violating consumer health data confidentiality obligations

The private right of action was limited to data brokers and "large data holders" — entities that process personal data of at least 100,000 Vermont residents per year. Consumers could recover **actual damages only** (not statutory or punitive damages). The right of action would have taken effect on January 1, 2027, and would have **automatically sunset on January 1, 2029**, unless the legislature voted to extend it — a built-in sunset designed to give the legislature the opportunity to evaluate real-world effects before making the mechanism permanent.

As of 2024, no other enacted comprehensive state privacy law in the Virginia-model tradition provided consumers with a direct right to sue; Washington's MHMDA provided a private right of action for health data only. Vermont's H.121 would have been the first general comprehensive privacy law with such a mechanism.

### Age-Appropriate Design Code [HIGH confidence]

H.121 incorporated a Vermont Age-Appropriate Design Code (VAADC) applicable to online services, products, or features likely to be accessed by minors. Covered businesses would have been prohibited from:

- Using "dark patterns" — defined broadly as user interface designs that undermine user autonomy, deceive users, or impair their ability to exercise privacy rights
- Using design features that "encourage excessive and compulsive use" by minors
- Permitting unknown adults to contact minors through the platform
- Permitting adults to monitor or track a minor's online activity

The VAADC required covered businesses to apply the highest available default privacy settings for minors and to treat children's privacy as a design priority rather than an afterthought. Governor Scott noted in his veto letter that California's similar [Age-Appropriate Design Code](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202120220AB2273) had been enjoined by a federal district court on First Amendment grounds — a concern that influenced his decision to veto H.121.

### Data Broker Provisions [HIGH confidence]

Vermont's existing [data broker registration statute](https://legislature.vermont.gov/statutes/section/09/062/02430) defined a data broker as a business that knowingly collects and sells or licenses the personal information of consumers with whom it has no direct relationship. H.121 would have expanded data broker obligations by requiring:

- Annual security assessments
- Limitations on data collection to specific, disclosed purposes
- Direct applicability of the private right of action for data broker violations involving sensitive data

### Enforcement and Penalties [HIGH confidence]

Primary enforcement authority rested with the Vermont Attorney General, who would have had authority to:
- Issue civil investigative demands
- Bring civil enforcement actions
- Seek civil penalties of up to $7,500 per violation (consistent with other Virginia-model states)

Controllers and processors would have received a **60-day cure period** before the AG could initiate an enforcement action for most violations. In addition to the AG's general enforcement authority, violations of H.121 constituted unfair and deceptive acts and practices under Vermont's Consumer Protection Act (9 V.S.A. § 2453), providing an additional enforcement basis.

Data broker-specific penalties under [existing Vermont data broker law (9 V.S.A. § 2446)](https://legislature.vermont.gov/statutes/section/09/062/02446) include a civil penalty of $50 per day for non-registration, not to exceed $10,000 per year in total. (Note: A $25,000 penalty for filing materially incorrect information has been proposed under H.211 in the 2025-2026 legislative session but is not currently enacted law under 9 V.S.A. § 2446.)

## The Veto and Aftermath [HIGH confidence]

Governor Phil Scott vetoed H.121 on [June 13, 2024](https://governor.vermont.gov/press-release/action-taken-governor-phil-scott-legislation-june-13-2024). In his veto letter, he cited three primary concerns:

1. **Private right of action**: Scott wrote that allowing consumers to sue companies directly "would make Vermont a national outlier, and more hostile than any other state to many businesses and non-profits." He expressed concern about "an unnecessary and avoidable level of risk" for Vermont businesses from increased litigation exposure.

2. **Accumulated regulatory burden**: Scott argued that Vermont businesses were simultaneously absorbing new costs from a payroll tax, a Clean Heat Standard, property tax increases, and Act 250 land-use changes, making H.121's compliance costs ill-timed for the state's economy.

3. **Age-Appropriate Design Code**: Scott cited the California AADC's constitutional troubles — a federal court had enjoined California's version — as reason to doubt Vermont's version would withstand First Amendment scrutiny.

The governor explicitly stated his preference that Vermont adopt Connecticut's comprehensive privacy framework, noting that New Hampshire had also modeled its law on Connecticut and that regional consistency would benefit Vermont businesses.

Vermont Attorney General Charity Clark [issued a sharp rebuke](https://ago.vermont.gov/blog/2024/06/14/statement-attorney-general-clark-governors-veto-h121-vermont-data-privacy-act) of the veto, calling it "extremely disappointing" and stating that without a private right of action, "enforcement would fall solely to taxpayers through the Attorney General's Office." Clark argued that H.121 "represents a paradigm shift" and that Vermont's data should belong to its consumers, not to corporations.

### Veto Override Outcome

At the [June 17, 2024 veto session](https://therecord.media/vermont-landmark-privacy-bill-killed), the outcomes were:

- **House**: 128-17 in favor of override — far exceeding the two-thirds threshold
- **Senate**: 14-15 in favor of override — six votes short of the required 20 for a two-thirds supermajority

The veto was sustained. H.121 did not become law. Vermont remains the only state where a comprehensive consumer privacy bill achieved overwhelming House support only to die on a Senate veto override vote.

### 2025-2026 Legislative Follow-On

Vermont lawmakers have not abandoned the effort. In the 2025-2026 legislative session, the Senate passed S.71, a [pared-down data privacy bill](https://vtdigger.org/2025/03/27/final-reading-vermont-senate-passes-pared-down-data-privacy-bill/) that strips the private right of action and adopts a more Connecticut-aligned model, on March 27, 2025. S.71 was referred to the House Commerce and Economic Development Committee. A competing House bill, H.208, retains a private right of action. As of April 2025, no successor bill has been enacted.

Separately, the Age-Appropriate Design Code provisions of H.121 were reintroduced as a standalone bill (S.69), which Governor Scott signed into law on June 12, 2025, effective January 1, 2027 — demonstrating that the governor was willing to accept the children's safety provisions when they were not bundled with adult consumer privacy rights and a private right of action.

## Impact Assessment [MEDIUM confidence]

### Who Would Have Been Affected

Had H.121 become law, immediate compliance obligations would have fallen primarily on:

- **Large national technology companies** processing data of more than 100,000 Vermont consumers — effectively, most major consumer-facing digital platforms
- **Data brokers** operating nationally, which faced both the expanded H.121 requirements and Vermont's existing registration statute
- **Healthcare-adjacent businesses** of any size, due to the no-threshold consumer health data provisions
- **Online platforms serving minors**, subject to the VAADC regardless of data processing volume

Vermont's small population (approximately 650,000 residents) limited the compliance population at the 100,000-consumer threshold to large national actors. The governor's concern about small Vermont businesses was somewhat at odds with the thresholds' evident design, though the no-threshold health and children's provisions would have touched smaller entities.

### Significance for National Privacy Policy

Vermont's H.121 experiment has direct implications for the national privacy law debate on two axes:

**Private right of action**: Vermont's experience demonstrates that a private right of action commands strong legislative support (128-17 House override) but meets organized business resistance in upper chambers. This pattern may inform future battles in other states and in the ongoing federal comprehensive privacy debate, where the private right of action remains one of the most contested provisions in any proposed American Privacy Rights Act (APRA).

**State divergence vs. convergence**: The governor's recommendation that Vermont adopt Connecticut's law rather than legislate a unique framework reflects a business preference for interstate harmonization. As more states adopt Connecticut-modeled laws (New Hampshire, New Jersey), pressure on outlier states grows — but so does the evidence that a more protective model is politically achievable.

### Market Consequences of the Veto

Ironically, the veto may have increased uncertainty for businesses with Vermont operations rather than reduced it. Vermont's 2025-2026 legislative activity means businesses face the prospect of compliance obligations under a new law within the near term. The removal of the private right of action in S.71 would reduce litigation risk but would not eliminate the compliance cost of meeting Vermont's consumer rights framework.

## Action Items

- Monitor Vermont's 2025-2026 privacy legislation (S.71 and H.208) for resolution; as of April 2025 the fate of these bills remains uncertain.
- Data brokers operating nationally must maintain compliance with Vermont's existing data broker registration statute (9 V.S.A. § 2430), which was not affected by H.121's failure.
- Organizations preparing multi-state privacy programs should treat Vermont as a jurisdiction where comprehensive adult consumer privacy law may arrive soon, potentially modeled on Connecticut's framework.
- Prepare for the Vermont Age-Appropriate Design Code (S.69), signed into law June 2025, effective January 1, 2027 — this is enacted law applicable to platforms serving Vermont minors.
- Review private right of action exposure analysis: if a future Vermont law includes a private right of action even in limited form, organizations processing sensitive data of Vermont consumers or operating as large data holders face litigation risk that does not exist under any current comprehensive state privacy law.

## Related Reports

- [reports/privacy/state-comprehensive-laws/vermont-vdpa-h121-vetoed-2024-05-22.md](reports/privacy/state-comprehensive-laws/vermont-vdpa-h121-vetoed-2024-05-22.md) -- Comprehensive prior report on the same H.121 legislation covering the veto and aftermath in detail; this report covers the same development and readers should consult both.
- [reports/privacy/state-comprehensive-laws/maryland-sb541-modpa-2024-04-17.md](reports/privacy/state-comprehensive-laws/maryland-sb541-modpa-2024-04-17.md) -- Maryland's MODPA, which provided the data minimization model that Vermont's H.121 adopted; enacted successfully at the same time Vermont's bill was proceeding.
- [reports/privacy/state-comprehensive-laws/minnesota-mcdpa-hf4757-2024-05-30.md](reports/privacy/state-comprehensive-laws/minnesota-mcdpa-hf4757-2024-05-30.md) -- Minnesota's MCDPA passed in the same 2024 legislative wave; contrast its enactment with Vermont's veto outcome.
- [reports/privacy/maine-ld1822-privacy-bill-failed-2026-04-12.md](reports/privacy/maine-ld1822-privacy-bill-failed-2026-04-12.md) -- Maine's LD 1822 failed in 2026; another New England state example of difficulties enacting comprehensive adult privacy law.

## Sources

1. [H.121 As Passed by Both House and Senate (Full Text) -- Vermont Legislature](https://legislature.vermont.gov/Documents/2024/Docs/BILLS/H-0121/H-0121%20As%20Passed%20by%20Both%20House%20and%20Senate%20Unofficial.pdf) -- Official 105-page bill text as passed by both chambers; primary source for all provision descriptions and effective dates.
2. [Bill Status H.121 -- Vermont Legislature](https://legislature.vermont.gov/bill/status/2024/H.121) -- Official bill status with action history, vote records, and committee referrals.
3. [Vermont Legislature Passes State Privacy Bill with Right to Sue for Consumers -- Hunton Andrews Kurth](https://www.hunton.com/privacy-and-information-security-law/vermont-legislature-passes-state-privacy-bill-with-right-to-sue-for-consumers) -- Detailed law firm analysis of key provisions, consumer rights, and private right of action structure.
4. [Vermont Data Privacy Act (VDPA) H.121: Key Implications -- Hall Booth Smith](https://hallboothsmith.com/vermont-data-privacy-act-vdpa/) -- Analysis of applicability thresholds, tiered timeline, and compliance obligations.
5. [Vermont Passes Consumer Data Privacy Law -- McDermott Will & Emery](https://www.mcdermottlaw.com/insights/mixing-things-up-like-a-certain-ice-cream-maker-vermont-passes-consumer-data-privacy-law/) -- Law firm analysis with comparison to other state laws; source for data minimization characterization.
6. [While You Were Sleeping, Vermont Passed One of the Most Stringent State Consumer Privacy Laws Yet -- Taft Privacy & Data Security Insights](https://www.privacyanddatasecurityinsight.com/2024/05/while-you-were-sleeping-vermont-passed-one-of-the-most-stringent-state-consumer-privacy-laws-yet/) -- Original law firm alert from the finding's source; provides initial characterization and timing.
7. [Not So Fast: Vermont Governor VETOES Private Right of Action -- Taft Privacy & Data Security Insights](https://www.privacyanddatasecurityinsight.com/2024/06/not-so-fast-vermont-governor-vetoes-private-right-of-action-for-consumer-privacy-violations/) -- Taft follow-up on the governor's veto.
8. [Action Taken by Governor Phil Scott on Legislation -- June 13, 2024](https://governor.vermont.gov/press-release/action-taken-governor-phil-scott-legislation-june-13-2024) -- Official governor's office press release announcing the veto of H.121.
9. [Statement From Attorney General Clark on Governor's Veto of H.121 -- Vermont AG Office](https://ago.vermont.gov/blog/2024/06/14/statement-attorney-general-clark-governors-veto-h121-vermont-data-privacy-act) -- Official statement from AG Charity Clark criticizing the veto and urging override.
10. [Vermont's Landmark Privacy Bill Killed as Legislature Fails to Override Veto -- The Record / Recorded Future News](https://therecord.media/vermont-landmark-privacy-bill-killed) -- News coverage of the final Senate vote and veto sustain.
11. [Vermont Senate Fails to Override Vermont Data Privacy Act Veto -- EPIC](https://epic.org/vermont-senate-sustains-governors-veto-of-vermont-privacy-act/) -- EPIC analysis of the failed veto override, including Senate vote count of 14-15.
12. [Vermont Governor Vetoes Data Privacy Act -- Foley & Lardner](https://www.foley.com/insights/publications/2024/06/vermont-governor-vetoes-data-privacy-act/) -- Law firm analysis of the veto and its implications for businesses.
13. [Final Reading: Vermont Senate Passes Pared-Down Data Privacy Bill -- VTDigger](https://vtdigger.org/2025/03/27/final-reading-vermont-senate-passes-pared-down-data-privacy-bill/) -- News coverage of S.71's passage in the Vermont Senate on March 27, 2025.
14. [Vermont House Unanimously Passes Vermont Data Privacy Act -- EPIC](https://epic.org/vermont-house-unanimously-passes-vermont-data-privacy-act/) -- EPIC coverage of the House's unanimous passage; source for legislative history.
15. [Vermont Governor Vetoes Comprehensive Data Privacy Bill -- TechPolicy.Press](https://www.techpolicy.press/vermont-governor-vetoes-comprehensive-data-privacy-bill/) -- Independent policy journalism on the veto and its implications.
16. [9 V.S.A. § 2446 -- Vermont Data Broker Civil Penalties (Official Statute)](https://legislature.vermont.gov/statutes/section/09/062/02446) -- Official Vermont statutory text specifying the $50/day non-registration penalty capped at $10,000/year; cited to correct the penalty figures in the Enforcement section.
