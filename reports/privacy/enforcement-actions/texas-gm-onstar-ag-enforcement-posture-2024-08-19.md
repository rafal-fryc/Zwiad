---
title: "Texas AG's GM/OnStar Lawsuit Signals Aggressive Privacy Enforcement Posture Across Connected Industries"
date: 2024-08-19
jurisdiction: "Texas"
category: "privacy"
development_type: "enforcement"
finding_id: "SCAN-20240819-016"
topic_key: "TXAG-POSTURE-2024"
topic_type: "enforcement"
first_reported: 2024-08-19
last_updated: 2026-04-21
status_history: []
cluster: "Connected Car Telematics Data Sharing: State AG Enforcement Actions"
cluster_slug: "connected-car-telematics-data-broker-enforcement"
---

# Texas AG's GM/OnStar Lawsuit Signals Aggressive Privacy Enforcement Posture Across Connected Industries

**Jurisdiction:** Texas | **Category:** privacy | **Date:** 2024-08-19

## Executive Summary [HIGH confidence]

On August 13, 2024, the Texas Attorney General's office filed suit against [General Motors LLC and OnStar LLC](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-general-motors-unlawfully-collecting-drivers-private-data-and) in the District Court of Montgomery County, Texas (Case No. 24-08-12392), alleging that GM deployed deceptive enrollment tactics to harvest driving behavior data from more than 1.8 million Texas consumers and sold it to insurance data brokers without meaningful consent. Critically, the AG chose to bring suit under the long-standing [Texas Deceptive Trade Practices — Consumer Protection Act (DTPA)](https://statutes.capitol.texas.gov/Docs/BC/htm/BC.17.htm) rather than the newly effective Texas Data Privacy and Security Act (TDPSA) — a strategic choice that bypassed the TDPSA's mandatory 30-day cure period and enabled broader damages. The lawsuit is the fourth major privacy enforcement action by AG Ken Paxton in 2024 and, read alongside the AG's June 2024 Privacy and Technology enforcement initiative and July 2024 Meta biometric settlement, represents a sustained, multi-statute enforcement posture targeting the full spectrum of data-monetization industries. Compliance officers and in-house counsel across automotive, technology, healthcare AI, and data-broker sectors should treat this lawsuit as a direct signal of continued enforcement intensity, not an isolated matter.

## Background [HIGH confidence]

### The Texas Privacy Enforcement Landscape Prior to August 2024

Texas entered 2024 with an unusually robust set of privacy enforcement tools. Three statutes form the core enforcement arsenal:

1. **Texas Deceptive Trade Practices — Consumer Protection Act (DTPA), Tex. Bus. & Com. Code § 17.46 et seq.** This "mini-FTC act" — operative since the 1970s — prohibits false, misleading, or deceptive acts or practices in the conduct of any trade or commerce. It provides the AG with civil penalty authority of up to $10,000 per violation and $250,000 per violation against victims aged 65 or older, plus injunctive relief and restitution. Critically, it imposes no right-to-cure requirement before the AG can file suit. The [official statute is accessible on the Texas Legislature Online](https://statutes.capitol.texas.gov/Docs/BC/htm/BC.17.htm).

2. **Texas Capture or Use of Biometric Identifier Act (CUBI), Tex. Bus. & Com. Code § 503A.** Enacted in 2009, CUBI restricts the collection, use, storage, and sale of biometric identifiers — including facial geometry — without prior informed consent. The AG is the sole enforcer.

3. **Texas Data Privacy and Security Act (TDPSA), Tex. Bus. & Com. Code Ch. 541.** Signed by Governor Abbott in June 2023 and [effective July 1, 2024](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/consumer-privacy-rights/texas-data-privacy-and-security-act), the TDPSA is Texas's comprehensive consumer privacy law, extending rights including access, correction, deletion, portability, and opt-out of targeted advertising. It authorizes civil penalties of up to $7,500 per violation but requires a 30-day right-to-cure notice before suit. Exclusive enforcement authority rests with the AG.

On **June 4, 2024** — weeks before the TDPSA took effect — AG Paxton [formally announced a Privacy and Technology enforcement initiative](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-launches-data-privacy-and-security-initiative-protect-texans-sensitive), establishing a dedicated enforcement team within the Consumer Protection Division. The initiative's stated mandate spans DTPA, CUBI, the TDPSA, the Data Broker Law (Tex. Bus. & Com. Code Ch. 503B), the Identity Theft Enforcement and Protection Act, and applicable federal statutes including COPPA and HIPAA. The formation of a specialized unit — rather than assigning privacy matters to generalist ADA staff — signals institutional commitment to sustained enforcement.

### Key Enforcement Actions Preceding the GM Lawsuit

| Date | Action | Statute(s) | Result |
|------|--------|-----------|--------|
| June 2022 (filed) | *Texas v. Meta* (facial recognition / tag suggestions) | CUBI | Settled July 2024 for $1.4B — largest single-state privacy settlement in US history |
| June 4, 2024 | Privacy and Technology Enforcement Initiative launched | Multiple | Dedicated enforcement team formed |
| June 6, 2024 | Investigations opened into multiple car manufacturers re: telematics data practices | DTPA | Civil investigative demands; GM subsequently sued |
| June 2024 | Letters to 100+ companies re: Texas Data Broker Law registration | Data Broker Law | Over 200 data brokers eventually registered |
| July 30, 2024 | [Meta $1.4B biometric settlement announced](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-secures-14-billion-settlement-meta-over-its-unauthorized-capture-personal-biometric-data) | CUBI | Record-setting settlement paid over five years |
| August 13, 2024 | *Texas v. GM and OnStar* filed | DTPA, Data Broker Law | Active litigation (pending as of April 2026) |

The Meta settlement — the first enforcement action and first settlement under CUBI — validated the AG's litigation approach: file early, accept a high-value settlement, and use it as a deterrent signal for the next target category. The GM lawsuit followed this template by escalating from automotive industry investigations to a formal complaint within two months.

## Detailed Analysis [HIGH confidence]

### The GM/OnStar Complaint: Allegations and Legal Theory

The [official complaint — State of Texas v. General Motors LLC and OnStar LLC (original petition, PDF)](https://www.texasattorneygeneral.gov/sites/default/files/images/press/General%20Motors%20Data%20Privacy%20Petition%20Filed.pdf) — sets out a layered enforcement theory:

**Scope of data collection.** Since approximately 2015, GM equipped vehicles with OnStar-connected hardware that collected data across 36 behavioral categories, including: current speed; trip start/end times; distance driven; hard-braking events; sharp turns; hard acceleration; seatbelt status for driver and passengers; and late-night driving. The complaint alleges 14+ million GM vehicles were so equipped, with 1.8+ million in Texas.

**Deceptive enrollment.** The AG's core deception theory rests on two prongs. First, GM embedded OnStar Smart Driver enrollment into the vehicle onboarding process at dealerships in a way that appeared mandatory. Second, and critically, GM or its dealers informed customers that declining enrollment would cause their vehicle's safety features to be deactivated — a statement the AG characterizes as a material misrepresentation. Dealership employees were incentivized with commissions for Smart Driver enrollments, creating a financial incentive to pressure consumers.

**Data monetization.** From approximately 2015 to March 2024, GM sold or transferred aggregated driving data to third parties including [LexisNexis Risk Solutions and Verisk Analytics](https://www.cbsnews.com/news/gm-selling-driver-data-car-insurers-texas-lawsuit/) — both consumer reporting agencies — which compiled behavioral risk profiles and "Driving Scores" sold to auto insurers. Factors deemed adverse included: late-night trips; sharp turns; hard braking; seat belt non-use; and speeds above 80 mph. GM ceased data sharing with LexisNexis and Verisk in March 2024 following New York Times investigative reporting, but the Texas AG alleges the harm to current policyholders had already materialized in premium increases and coverage denials.

**Statutes invoked.** The primary statutory vehicle is the DTPA (§ 17.46), charging GM with false and deceptive business representations regarding: (1) the nature and effects of the Smart Driver enrollment; (2) the consequences of declining enrollment; (3) what data was being collected; and (4) how collected data would be used. The complaint also invokes the Texas Data Broker Law (§ 503B) on the theory that GM and OnStar operated as, or facilitated, unregistered data brokers.

### Why DTPA Rather than TDPSA?

The AG's decision to invoke the DTPA — rather than the TDPSA, which became effective July 1, 2024, just six weeks before the lawsuit — is analytically significant. As [CPO Magazine reported](https://www.cpomagazine.com/data-protection/texas-attorney-general-sues-general-motors-over-consumer-privacy-violations-sale-of-driver-data-to-insurance-companies/), the TDPSA requires the AG to issue a 30-day notice of violation and allow cure before filing suit. The DTPA imposes no such precondition.

This choice reveals a strategic doctrine: Texas will use existing consumer protection law to circumvent procedural protections embedded in the comprehensive privacy statute when conduct is sufficiently egregious or when the AG wants to move quickly. The implication for industry is significant — TDPSA compliance alone does not insulate entities from DTPA liability for the same data practices, if those practices are characterized as deceptive under the broader consumer protection framework.

[White & Case characterized the approach as "landmark"](https://www.whitecase.com/insight-alert/texas-attorney-generals-landmark-privacy-lawsuit-signals-new-era-data-privacy), noting that it demonstrates consumer protection statutes can independently reach data monetization practices without reference to a comprehensive privacy law.

### Damages Exposure

The DTPA authorizes the AG to seek:
- Civil penalties of up to **$10,000 per violation**, where each deceptive act toward each consumer may constitute a separate violation;
- An additional penalty of up to **$250,000 per victim aged 65 or older**;
- Injunctive relief prohibiting continuation of unlawful practices;
- Restitution to affected consumers;
- Destruction of unlawfully collected data.

With 1.8 million Texas consumers identified, potential civil exposure on a per-violation theory exceeds **$18 billion** before senior-victim enhancements, as [Property Casualty 360 reported](https://www.propertycasualty360.com/2024/08/20/texas-puts-general-motors-onstar-at-head-of-line-in-data-privacy-lawsuit-414-258559/). This quantum of theoretical exposure — even if the AG ultimately settles for far less — functions as leverage comparable to the $1.4B Meta settlement.

### Enforcement Posture Signals

Several features of the GM lawsuit illuminate the AG's broader enforcement philosophy:

**Pattern from investigation to lawsuit in weeks.** The June 2024 automotive industry investigation produced a formal complaint against GM in only eight weeks. This acceleration suggests the AG's team had pre-existing intelligence on GM's practices from prior reporting and was using the investigation process to assemble a filing-ready complaint, not to deliberate.

**Targeting the data pipeline, not just the data collector.** The complaint names OnStar LLC separately from GM, and identifies LexisNexis and Verisk as recipients. The AG's stated enforcement mandate covers data brokers directly, suggesting downstream actors — not only the OEM that collected data — face scrutiny.

**Use of DTPA for technology-sector conduct.** The DTPA was historically deployed in consumer transactions involving tangible goods or traditional services. By applying it to connected-vehicle telematics and data monetization, the AG's office is establishing that digital-era data practices are "trade or commerce" for DTPA purposes — a precedent directly applicable to mobile apps, streaming platforms, and health-tech.

**Parallel federal coordination.** On January 14, 2026, the [FTC finalized a consent order against GM and OnStar](https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-finalizes-order-settling-allegations-gm-onstar-collected-sold-geolocation-data-without-consumers), banning GM from sharing geolocation and driving behavior data with consumer reporting agencies for five years and requiring affirmative consent for any connected vehicle data collection. The parallel federal proceeding — on essentially the same facts — suggests coordination between state and federal enforcers and indicates the GM conduct will be scrutinized under the most aggressive theory available in each forum simultaneously.

### Subsequent Enforcement Actions Reinforcing the Pattern

The AG's office has continued its enforcement trajectory since the GM filing:

- **September 2024:** Settlement with [Pieces Technologies](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-leads-nation-protecting-americans-data-privacy-and-security-big-tech), a Dallas-based healthcare AI company, for false and misleading statements about accuracy and safety of AI products — first AI-sector enforcement using the DTPA.
- **October 2024:** [Lawsuit against TikTok](https://www.hunton.com/privacy-and-information-security-law/texas-attorney-general-files-lawsuit-against-tiktok-under-scope-act) under the Texas Securing Children Online through Parental Empowerment (SCOPE) Act for allegedly sharing minors' personal data with third parties.
- **December 2024:** Investigations opened into 15 technology companies regarding privacy and safety practices for minors under SCOPE and TDPSA.
- **Early 2025:** Four additional automotive manufacturers — Ford, Hyundai, Toyota, and Fiat Chrysler — [received civil investigative demands](https://therecord.media/gm-lawsuit-texas-data-privacy) expanding the connected-vehicle investigation beyond GM.
- **January 2025:** First TDPSA enforcement action filed (against Allstate and Arity for SDK-based telematics data collection), demonstrating the AG's willingness to now use the comprehensive privacy statute in addition to DTPA when the cure period has been exhausted.

## Impact Assessment [MEDIUM confidence]

### Industries at Elevated Risk

The AG's stated enforcement mandate and pattern of actions since June 2024 put several industries in the high-risk category for enforcement under DTPA, TDPSA, or both:

- **Connected vehicle and telematics:** GM was first, but four other OEMs already face civil investigative demands. Any connected-vehicle program collecting behavioral data and transmitting it to insurers, data brokers, or other third parties faces DTPA exposure under the GM theory.
- **Mobile SDK and app-based telematics:** The Allstate/Arity enforcement (filed January 2025) confirms the AG is pursuing the entire data pipeline — SDK operators who harvest location data through embedded code in third-party apps face direct TDPSA and DTPA exposure.
- **Healthcare AI:** The Pieces Technologies settlement signals the AG's DTPA theory extends to AI product representations, specifically false claims about accuracy or safety. Healthcare AI vendors operating in Texas should audit product-level accuracy statements for DTPA compliance.
- **Data brokers (all sectors):** 100+ companies received non-compliance letters under the Data Broker Law in 2024. The AG treats Data Broker Law violations as an aggravating factor in broader DTPA/TDPSA enforcement actions.
- **Platforms with minors' data:** The SCOPE Act enforcement trajectory — investigation to TikTok lawsuit — mirrors the automotive pattern. Any platform accessible to minors in Texas is a prospective SCOPE/TDPSA target.

### Compliance Considerations

The intersection of DTPA and TDPSA enforcement requires a two-track analysis for Texas-facing companies:

**TDPSA compliance is necessary but not sufficient.** Meeting the TDPSA's consent, disclosure, and data rights obligations does not eliminate DTPA exposure if the manner in which enrollment or consent was obtained could be characterized as deceptive. The GM case illustrates this vividly: GM's disclosures may have technically disclosed data-sharing in buried terms-of-service language, but the AG's DTPA theory focuses on the deceptive *framing* of enrollment — not whether a disclosure existed at all.

**Onboarding and enrollment UX is an enforcement risk surface.** The most specific and concrete allegation in the GM complaint — that consumers were told safety features would be deactivated if they declined enrollment — is a UI/UX design decision, not a policy one. Compliance programs that focus only on privacy notices and data mapping without auditing enrollment flows and consent pathways will miss this category of risk.

**Third-party data recipients face independent exposure.** The AG's mandate covers data brokers. If your organization purchases telematics, behavioral, or biometric data that was originally collected without adequate consent, you inherit the enforcement risk profile of the original collector. Chain-of-consent documentation from data vendors is a basic due-diligence requirement.

## Action Items

- Audit all Texas-consumer-facing data collection programs — particularly any connected-device, telematics, or behavioral-scoring features — against both DTPA (deception standard) and TDPSA (consent and disclosure standard). Treat these as two independent assessments, not a single compliance exercise.
- Review all enrollment and onboarding flows for consumer-facing representations that could be characterized as coercive or materially misleading, including statements about consequences of declining optional features or services.
- If your organization sells data to consumer reporting agencies, insurance companies, or data brokers, verify that the consent chain for that data is affirmative, granular, and accurately disclosed — DTPA does not require "lack of any disclosure"; it requires that the disclosure not be deceptive in context.
- Confirm Texas Data Broker Law registration compliance (Tex. Bus. & Com. Code Ch. 503B) if your organization meets the statutory definition of a data broker operating in Texas.
- Obtain chain-of-consent documentation from telematics data vendors (particularly those providing driving scores or behavioral risk profiles) and assess whether that data was originally collected under practices now challenged by the Texas AG.
- Monitor the docket in *Texas v. General Motors LLC and OnStar LLC*, Montgomery County District Court, Case No. 24-08-12392, for settlement terms that will set an industry benchmark for remediation obligations.
- For automotive OEMs and connected-vehicle operators: assess the parallel FTC consent order against GM (finalized January 14, 2026) as a baseline compliance framework for connected vehicle data practices, even if your company is not yet under a federal or Texas enforcement action.

## Related Reports

- [reports/privacy/enforcement-actions/texas-ag-gm-onstar-driver-data-2024-08-15.md](reports/privacy/enforcement-actions/texas-ag-gm-onstar-driver-data-2024-08-15.md) — Companion report covering the GM/OnStar lawsuit itself in detail, including complaint allegations, damages theory, bankruptcy court complications, and FTC consent order terms.
- [reports/privacy/enforcement-actions/texas-tdpsa-ag-enforcement-initiative-2024-06-10.md](reports/privacy/enforcement-actions/texas-tdpsa-ag-enforcement-initiative-2024-06-10.md) — Background on the June 2024 launch of the Texas AG Privacy and Technology enforcement initiative, the statutory foundation for the broader posture analyzed here.
- [reports/privacy/enforcement-actions/texas-allstate-arity-tdpsa-enforcement-2026-04-14.md](reports/privacy/enforcement-actions/texas-allstate-arity-tdpsa-enforcement-2026-04-14.md) — Texas AG's first TDPSA enforcement action against Allstate and Arity, demonstrating the AG's willingness to use the comprehensive privacy statute alongside DTPA for SDK-based telematics data collection.
- [reports/privacy/enforcement-actions/texas-meta-biometric-cubi-settlement-2024-07-30.md](reports/privacy/enforcement-actions/texas-meta-biometric-cubi-settlement-2024-07-30.md) — The $1.4B Meta biometric settlement that immediately preceded and contextualized the GM enforcement action as part of a broader AG enforcement campaign.
- [reports/privacy/enforcement-actions/montana-ford-stellantis-auto-data-cid-2026-04-19.md](reports/privacy/enforcement-actions/montana-ford-stellantis-auto-data-cid-2026-04-19.md) — Montana AG's civil investigative demands against Ford and Stellantis on connected-car data theories, demonstrating the multi-state spread of the enforcement pattern the Texas GM case initiated.

## Sources

1. [Texas OAG Press Release: Paxton Sues General Motors for Unlawfully Collecting and Selling Driver Data](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-general-motors-unlawfully-collecting-drivers-private-data-and) — Official August 13, 2024 announcement with key allegations and relief sought.
2. [State of Texas v. General Motors LLC and OnStar LLC — Original Petition (PDF)](https://www.texasattorneygeneral.gov/sites/default/files/images/press/General%20Motors%20Data%20Privacy%20Petition%20Filed.pdf) — Official complaint filed in Montgomery County District Court; primary legal text for claims and statute citations.
3. [Texas AG Privacy and Technology Enforcement Initiative Announcement (June 4, 2024)](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-launches-data-privacy-and-security-initiative-protect-texans-sensitive) — Official announcement establishing the dedicated enforcement team.
4. [Texas AG: Investigation into Car Manufacturers' Data Practices (June 2024)](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-opens-investigation-car-manufacturers-collection-and-sale-drivers-data) — Precursor investigation announcement establishing the automotive-sector inquiry.
5. [Texas AG: Meta $1.4B CUBI Settlement Announcement (July 30, 2024)](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-secures-14-billion-settlement-meta-over-its-unauthorized-capture-personal-biometric-data) — Official announcement of record biometric data settlement that preceded the GM lawsuit.
6. [Texas AG: 100+ Data Broker Non-Compliance Letters](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-notifies-over-100-companies-their-apparent-failure-comply-texas-data) — Official announcement of Data Broker Law enforcement sweep.
7. [Texas Deceptive Trade Practices Act, Tex. Bus. & Com. Code Ch. 17 (official text)](https://statutes.capitol.texas.gov/Docs/BC/htm/BC.17.htm) — Official statutory text of the DTPA including Section 17.46 prohibitions and penalty provisions.
8. [Texas Data Privacy and Security Act, Tex. Bus. & Com. Code Ch. 541 (official AG page)](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/consumer-privacy-rights/texas-data-privacy-and-security-act) — Official OAG guidance on TDPSA including enforcement authority and process.
9. [Texas Data Broker Law, Tex. Bus. & Com. Code Ch. 503B (official AG page)](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/consumer-privacy-rights/texas-data-broker-act) — Official OAG guidance on data broker registration and compliance.
10. [FTC Finalizes Order Against GM and OnStar (January 14, 2026)](https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-finalizes-order-settling-allegations-gm-onstar-collected-sold-geolocation-data-without-consumers) — Official FTC press release on the consent order; authoritative source for federal remedies.
11. [Federal Register: General Motors and OnStar LLC, Analysis of Proposed Consent Order (January 30, 2025)](https://www.federalregister.gov/documents/2025/01/30/2025-01940/general-motors-and-onstar-llc-analysis-of-proposed-consent-order-to-aid-public-comment) — Official Federal Register entry for the FTC consent order proceeding.
12. [Frankfurt Kurnit Klein & Selz: "Don't Mess with Texas" (August 2024)](https://technologylaw.fkks.com/post/102jgqm/dont-mess-with-texas-lone-star-state-ags-latest-lawsuit-signals-continued-aggr) — Primary law firm analysis underlying the approved finding; situates the GM case within broader Texas enforcement posture.
13. [White & Case: Texas AG's Landmark Privacy Lawsuit Signals New Era](https://www.whitecase.com/insight-alert/texas-attorney-generals-landmark-privacy-lawsuit-signals-new-era-data-privacy) — Law firm analysis characterizing DTPA strategy as landmark enforcement approach.
14. [CPO Magazine: Texas AG Sues GM Over Consumer Privacy Violations](https://www.cpomagazine.com/data-protection/texas-attorney-general-sues-general-motors-over-consumer-privacy-violations-sale-of-driver-data-to-insurance-companies/) — Analysis of DTPA vs. TDPSA enforcement choice and right-to-cure rationale.
15. [CBS News: GM Selling Driver Data to Car Insurers (2024)](https://www.cbsnews.com/news/gm-selling-driver-data-car-insurers-texas-lawsuit/) — Details on LexisNexis and Verisk as data recipients; GM's March 2024 cessation of data sharing.
16. [Property Casualty 360: GM and OnStar at Head of Line in Data Privacy Lawsuit](https://www.propertycasualty360.com/2024/08/20/texas-puts-general-motors-onstar-at-head-of-line-in-data-privacy-lawsuit-414-258559/) — Analysis of damages theory and $18 billion exposure estimate.
17. [The Record (Recorded Future News): GM Lawsuit is Texas AG's First Shot in Privacy Initiative](https://therecord.media/gm-lawsuit-texas-data-privacy) — Coverage situating the GM lawsuit within the AG's broader enforcement strategy.
18. [Hunton Andrews Kurth: Texas AG Files Lawsuit Against TikTok Under SCOPE Act (October 2024)](https://www.hunton.com/privacy-and-information-security-law/texas-attorney-general-files-lawsuit-against-tiktok-under-scope-act) — Confirms AG's extension of enforcement to children's privacy platform sector.
19. [Morrison Foerster: Texas Privacy Enforcement Heats Up (November 2024)](https://www.mofo.com/resources/insights/241112-texas-privacy-enforcement-heats-up) — Law firm roundup of 2024 Texas privacy enforcement actions and outlook.
20. [White and Williams: Bankruptcy Court Orders Texas to Strike GM Allegations](https://www.whiteandwilliams.com/restructuring-perspectives/bankruptcy-court-orders-texas-to-strike-allegations-in-state-data-privacy-suit-against-general-motors) — Analysis of October 2025 bankruptcy court ruling limiting scope of Texas's GM complaint.
