---
title: "Texas AG Sues General Motors and OnStar for Unlawful Collection and Sale of Driver Data to Insurers"
date: 2024-08-15
jurisdiction: "Texas"
category: "privacy"
development_type: "enforcement"
finding_id: "SCAN-20240815-001"
topic_key: "texas-3eae2b28-2024"
topic_type: "enforcement_action"
first_reported: 2024-08-15
last_updated: 2026-04-21
status_history: []
cluster: "Connected Car Telematics Data Sharing: State AG Enforcement Actions"
cluster_slug: "connected-car-telematics-data-broker-enforcement"
---

# Texas AG Sues General Motors and OnStar for Unlawful Collection and Sale of Driver Data to Insurers

**Jurisdiction:** Texas | **Category:** privacy | **Date:** 2024-08-15

## Executive Summary [HIGH confidence]

On August 13, 2024, Texas Attorney General Ken Paxton filed suit against [General Motors LLC and OnStar LLC](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-general-motors-unlawfully-collecting-drivers-private-data-and) in the District Court of Montgomery County, Texas, alleging the companies systematically collected detailed driving behavior data from more than 14 million vehicles and sold it to data brokers — including [LexisNexis Risk Solutions and Verisk Analytics](https://www.cbsnews.com/news/gm-selling-driver-data-car-insurers-texas-lawsuit/) — without meaningful consumer consent. The case directly affected more than 1.8 million Texas drivers. GM leveraged its OnStar Smart Driver enrollment process to capture speed, braking, seatbelt use, trip distance, and other behavioral metrics, which were used to generate insurance "Driving Scores" that insurers then used to raise premiums or deny coverage. Texas seeks up to $10,000 per violation plus enhanced penalties for victims aged 65 or older, putting total potential exposure at or above $18 billion. The lawsuit — filed just weeks after the [Texas Data Privacy and Security Act (TDPSA)](https://statutes.capitol.texas.gov/Docs/BC/htm/BC.541.htm) took effect on July 1, 2024 — is part of a broader AG initiative targeting connected-vehicle telematics practices across the automotive industry. A parallel [FTC consent order finalized in January 2026](https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-finalizes-order-settling-allegations-gm-onstar-collected-sold-geolocation-data-without-consumers) adds federal enforcement weight to the same underlying conduct.

## Background [HIGH confidence]

### Texas Privacy Enforcement Context

Texas enacted the [Texas Data Privacy and Security Act (HB 4, 88th Regular Session)](https://capitol.texas.gov/tlodocs/88R/billtext/html/HB00004F.htm), signed by Governor Greg Abbott in June 2023 and effective July 1, 2024, codified at [Chapter 541 of the Texas Business and Commerce Code](https://statutes.capitol.texas.gov/Docs/BC/htm/BC.541.htm). Weeks before the TDPSA took effect, AG Paxton [announced a dedicated Privacy and Technology enforcement team](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-launches-data-privacy-and-security-initiative-protect-texans-sensitive) within the Consumer Protection Division, signaling aggressive posture. The team's mandate explicitly encompasses the TDPSA, the [Texas Data Broker Law](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/consumer-privacy-rights/texas-data-broker-act), the Biometric Identifier Act, the Identity Theft Enforcement and Protection Act, the Deceptive Trade Practices Act (DTPA), and federal statutes including COPPA and HIPAA.

In June 2024 — before filing against GM — Paxton [opened investigations into multiple car manufacturers](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-opens-investigation-car-manufacturers-collection-and-sale-drivers-data), citing widespread media reporting that automakers were covertly harvesting telematics data and selling it to insurers. GM was named as the first defendant to face a formal lawsuit; [four additional manufacturers (Ford, Hyundai, Toyota, and Fiat Chrysler) were subjected to civil investigative demands in early 2025](https://therecord.media/texas-probes-four-more-car-companies-data-collection-sharing).

### GM's OnStar Smart Driver Program

GM began installing connected-vehicle technology in vehicles from the 2015 model year onward. Vehicles equipped with OnStar could transmit trip-level data including start and end times, speed, distance, hard-braking events, sharp turns, seatbelt status, and late-night driving patterns. The [OnStar Smart Driver program](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-general-motors-unlawfully-collecting-drivers-private-data-and) was presented to consumers as a personalized driving feedback feature. GM allegedly embedded enrollment prompts into the vehicle onboarding process and, according to the complaint, warned consumers that failing to enroll would result in the deactivation of safety features — a representation the AG characterizes as materially misleading.

Data collected via Smart Driver was sold to [LexisNexis Risk Solutions and Verisk Analytics](https://www.cbsnews.com/news/gm-selling-driver-data-car-insurers-texas-lawsuit/), major consumer reporting agencies that aggregate behavioral data for underwriting purposes. These firms compiled the data into "Driving Scores" sold to auto insurers, which used them to adjust premiums or refuse coverage. [GM announced in March 2024 that it had ceased sharing data with LexisNexis and Verisk](https://www.cbsnews.com/news/gm-selling-driver-data-car-insurers-texas-lawsuit/), following a New York Times investigation, but the Texas AG alleges the harm to existing policyholders had already materialized.

## Detailed Analysis [HIGH confidence]

### Legal Claims

The [official complaint — State of Texas v. General Motors LLC and OnStar LLC](https://www.texasattorneygeneral.gov/sites/default/files/images/press/General%20Motors%20Data%20Privacy%20Petition%20Filed.pdf) — is filed in the District Court of Montgomery County and advances claims under multiple Texas statutes:

- **Texas Deceptive Trade Practices — Consumer Protection Act (DTPA):** The AG alleges GM's enrollment practices constituted false, deceptive, and misleading business representations. The DTPA is the primary enforcement vehicle, permitting the OAG to sue on behalf of consumers without individual plaintiff standing. Notably, Texas chose the DTPA over the TDPSA, [likely because the TDPSA requires a 30-day right-to-cure notice before suit](https://www.cpomagazine.com/data-protection/texas-attorney-general-sues-general-motors-over-consumer-privacy-violations-sale-of-driver-data-to-insurance-companies/) — a procedural constraint the DTPA does not impose.
- **Texas Data Broker Law:** GM and OnStar allegedly operated as or facilitated unregistered data brokers in violation of the [Texas Business and Commerce Code § 503B](https://statutes.capitol.texas.gov/Docs/BC/htm/BC.503B.htm).
- **Identity Theft Enforcement and Protection Act and Biometric Identifier Act:** The complaint references these as additional bases, depending on how driving behavioral data is classified.

### Damages Theory

The DTPA authorizes civil penalties of up to **$10,000 per violation**, with an additional penalty of up to **$250,000 per victim aged 65 or older**. With 1.8 million identified Texas victims, the [total potential civil exposure exceeds $18 billion](https://www.propertycasualty360.com/2024/08/20/texas-puts-general-motors-onstar-at-head-of-line-in-data-privacy-lawsuit-414-258559/) before senior-citizen enhancements. Texas also seeks: injunctive relief prohibiting deceptive data collection practices without informed consent; restitution to affected consumers; and destruction of all driving data held by GM, OnStar, or third-party recipients.

### Bankruptcy Court Complication

A notable procedural development arose in the context of GM's 2009 bankruptcy reorganization. [White and Williams reported in October 2025](https://www.whiteandwilliams.com/restructuring-perspectives/bankruptcy-court-orders-texas-to-strike-allegations-in-state-data-privacy-suit-against-general-motors) that the U.S. Bankruptcy Court for the Southern District of New York ordered Texas to strike allegations suggesting an ongoing pattern of deception extending to pre-reorganization conduct — including references to ignition switch and fuel tank matters — because such claims implicate the 2009 sale order transferring assets from "Old GM" to "New GM." The ruling limits the temporal scope of Texas's deception narrative but does not extinguish the core data-collection claims, which post-date the 2009 sale.

### Federal Parallel: FTC Consent Order (January 2026)

The FTC pursued parallel federal enforcement. On January 14, 2026, the [FTC finalized a consent order against GM and OnStar](https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-finalizes-order-settling-allegations-gm-onstar-collected-sold-geolocation-data-without-consumers), requiring:

- A **five-year ban** on sharing geolocation and driving behavior data with consumer reporting agencies;
- **Affirmative express consent** required before any future collection, use, or sharing of connected vehicle data;
- Systems enabling all U.S. consumers to **request, view, and delete** their data;
- Option to **disable precise geolocation tracking** at the vehicle level;
- **Destruction of all previously collected driver data** within 180 days, with parallel instructions to third parties.

The FTC order does not include a monetary penalty but imposes a 20-year compliance and reporting obligation. The absence of a fine reflects the FTC's current consent-order model for novel data practices.

### Significance of the DTPA Strategy

Legal analysts at [White & Case characterized the lawsuit as a "landmark" action](https://www.whitecase.com/insight-alert/texas-attorney-generals-landmark-privacy-lawsuit-signals-new-era-data-privacy) signaling a new era in data privacy enforcement. Three features stand out. First, Texas deployed the long-established DTPA rather than the new TDPSA — demonstrating that comprehensive privacy statutes are not the only route to enforcement; consumer protection laws can reach covert data monetization directly. Second, the AG framed the harm in terms of downstream insurance consequences, giving affected consumers a concrete, easily communicable injury (premium increases, coverage denials). Third, the sheer scale of potential penalties — anchored to a per-violation DTPA theory across millions of consumers — elevates the financial exposure well beyond what most OEM compliance programs were designed to contemplate.

## Impact Assessment [HIGH confidence]

### Affected Industries

- **Automotive OEMs and connected-vehicle platform operators**: Any telematics or connected-services program collecting trip-level behavioral data is now within scope for AG scrutiny under state DTPA or consumer protection statutes, regardless of whether a comprehensive privacy law applies.
- **Telematics data brokers and consumer reporting agencies** (e.g., LexisNexis Risk Solutions, Verisk): Named indirectly in the complaint and subject to parallel enforcement as recipients of unlawfully collected data. The FTC order requires data destruction by third parties.
- **Auto insurers using telematics underwriting data**: Insurers relying on third-party behavioral scores must audit the provenance of data sourced from OEM telematics programs.
- **SDK and app ecosystem participants**: The overlapping Allstate/Arity enforcement (filed January 2025) extends the same theory to mobile SDK-based telematics collection — signaling the AG is pursuing the entire data pipeline, not just the OEM layer.

### Compliance Requirements

The FTC order creates immediate baseline obligations for GM and OnStar that can serve as a reference point for industry self-assessment:

1. Affirmative opt-in consent before any telematics data collection begins;
2. Clear, plain-language disclosure of what data is collected, how it is used, and who receives it;
3. Consumer rights to access, delete, and disable geolocation collection;
4. Prohibition on sharing behavioral data with consumer reporting agencies absent specific consent;
5. Third-party data destruction obligations upon termination of data-sharing arrangements.

The Texas state case remains pending as of April 2026. Any settlement or judgment will add additional state-law compliance obligations on top of the FTC order.

### Broader Enforcement Trajectory

Texas expanded its automotive data investigation to [Ford, Hyundai, Toyota, and Fiat Chrysler in early 2025](https://therecord.media/texas-probes-four-more-car-companies-data-collection-sharing). Montana's AG issued civil investigative demands against Ford and Stellantis in April 2026 on analogous theories. The multi-state pattern is consistent with coordinated AG enforcement, and additional states with DTPA-analogues or comprehensive privacy laws are likely to follow.

## Action Items

- Audit all telematics and connected-vehicle programs to identify what behavioral or location data is collected, how it is disclosed to consumers, and to whom it is transmitted or sold — particularly any linkage to consumer reporting agencies.
- Review enrollment and onboarding flows for deceptive dark patterns; specifically, evaluate whether consumers are meaningfully informed that enrolling in optional features triggers data monetization to third parties.
- If your organization operates as a data broker or sells data to consumer reporting agencies, verify Texas Data Broker Law registration compliance and assess whether consent obtained from OEM data sources meets Texas's affirmative-consent standard.
- If you are an insurer using OEM telematics-derived scores for underwriting, request chain-of-consent documentation from data vendors (LexisNexis, Verisk, or OEM direct) and assess exposure under both DTPA and state insurance unfair-practices statutes.
- Monitor the Texas v. GM state court docket for any settlement terms, which will set a benchmark for remediation obligations beyond the FTC's January 2026 consent order.
- Assess whether similar exposure exists under other states' consumer protection statutes; do not assume that compliance with the TDPSA or a similar comprehensive privacy law provides full insulation where underlying conduct is separately actionable as deceptive trade practice.

## Related Reports

- [reports/privacy/enforcement-actions/texas-allstate-arity-tdpsa-enforcement-2026-04-14.md](reports/privacy/enforcement-actions/texas-allstate-arity-tdpsa-enforcement-2026-04-14.md) — Texas AG's first TDPSA enforcement action against Allstate and Arity for SDK-based telematics data collection, directly parallel to the GM theory of liability.
- [reports/privacy/enforcement-actions/texas-tdpsa-ag-enforcement-initiative-2024-06-10.md](reports/privacy/enforcement-actions/texas-tdpsa-ag-enforcement-initiative-2024-06-10.md) — Background on the Texas OAG privacy enforcement team launch and its statutory mandate, which provides the institutional context for the GM lawsuit.
- [reports/privacy/enforcement-actions/montana-ford-stellantis-auto-data-cid-2026-04-19.md](reports/privacy/enforcement-actions/montana-ford-stellantis-auto-data-cid-2026-04-19.md) — Montana AG's civil investigative demands against Ford and Stellantis, showing the GM case spawning multi-state connected-car enforcement.

## Sources

1. [Texas OAG Press Release: Paxton Sues General Motors](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-general-motors-unlawfully-collecting-drivers-private-data-and) — Official announcement of the August 13, 2024 lawsuit with key allegations and relief sought.
2. [State of Texas v. General Motors LLC and OnStar LLC — Original Petition (PDF)](https://www.texasattorneygeneral.gov/sites/default/files/images/press/General%20Motors%20Data%20Privacy%20Petition%20Filed.pdf) — Official complaint filed in Montgomery County District Court; primary legal text for claims and statute citations.
3. [Texas OAG: Investigation into Car Manufacturers' Data Practices (June 2024)](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-opens-investigation-car-manufacturers-collection-and-sale-drivers-data) — Precursor investigation announcement establishing the broader automotive data enforcement initiative.
4. [FTC Finalizes Order Against GM and OnStar (January 14, 2026)](https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-finalizes-order-settling-allegations-gm-onstar-collected-sold-geolocation-data-without-consumers) — Official FTC press release on the consent order; authoritative source for federal remedies and compliance obligations.
5. [FTC Case Docket: General Motors LLC, et al.](https://www.ftc.gov/legal-library/browse/cases-proceedings/2423052-general-motors-llc-et-al-matter) — Official FTC legal library entry for the enforcement proceeding.
6. [CBS News: GM Selling Driver Data to Car Insurers (2024)](https://www.cbsnews.com/news/gm-selling-driver-data-car-insurers-texas-lawsuit/) — Details on LexisNexis and Verisk as data recipients; GM's March 2024 cessation of data sharing.
7. [CPO Magazine: Texas AG Sues GM Over Consumer Privacy Violations](https://www.cpomagazine.com/data-protection/texas-attorney-general-sues-general-motors-over-consumer-privacy-violations-sale-of-driver-data-to-insurance-companies/) — Legal analysis including explanation of DTPA vs. TDPSA enforcement choice and right-to-cure rationale.
8. [White & Case: Texas AG's Landmark Privacy Lawsuit Signals New Era](https://www.whitecase.com/insight-alert/texas-attorney-generals-landmark-privacy-lawsuit-signals-new-era-data-privacy) — Law firm analysis characterizing the enforcement approach and industry implications.
9. [White and Williams: Bankruptcy Court Orders Texas to Strike Allegations](https://www.whiteandwilliams.com/restructuring-perspectives/bankruptcy-court-orders-texas-to-strike-allegations-in-state-data-privacy-suit-against-general-motors) — Analysis of October 2025 bankruptcy court ruling limiting scope of Texas allegations.
10. [The Record (Recorded Future News): GM Lawsuit is Texas AG's First Shot in Privacy Initiative](https://therecord.media/gm-lawsuit-texas-data-privacy) — Coverage situating the GM lawsuit within the AG's broader enforcement strategy.
11. [The Record: Texas Probes Four More Car Companies on Data Collection](https://therecord.media/texas-probes-four-more-car-companies-data-collection-sharing) — Reports on 2025 expansion to Ford, Hyundai, Toyota, and Fiat Chrysler.
12. [Property Casualty 360: GM and OnStar at Head of Line in Data Trafficking Suit](https://www.propertycasualty360.com/2024/08/20/texas-puts-general-motors-onstar-at-head-of-line-in-data-privacy-lawsuit-414-258559/) — Analysis of damages theory and $18 billion exposure estimate.
13. [Texas Data Privacy and Security Act, Tex. Bus. & Com. Code Ch. 541](https://statutes.capitol.texas.gov/Docs/BC/htm/BC.541.htm) — Official statutory text of the TDPSA.
14. [Texas Data Broker Law, Tex. Bus. & Com. Code Ch. 503B](https://statutes.capitol.texas.gov/Docs/BC/htm/BC.503B.htm) — Official text of the Data Broker registration and compliance requirements.
15. [Captain Compliance: FTC Finalizes Settlement with GM Over Unauthorized Driver Data Sales](https://captaincompliance.com/news/ftc-finalizes-settlement-with-gm-over-unauthorized-driver-data-sales-as-texas-ag-targets-connected-car-privacy-violations/) — Summary of FTC order terms alongside Texas enforcement context.
