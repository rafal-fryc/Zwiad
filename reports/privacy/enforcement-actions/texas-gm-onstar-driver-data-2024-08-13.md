---
title: "Texas AG Sues General Motors and OnStar for Selling 1.8 Million Texans' Driving Data Without Consent"
date: 2024-08-13
jurisdiction: "Texas"
category: "privacy"
development_type: "enforcement"
finding_id: "SCAN-20240820-002"
topic_key: "texas-bb866101-2024"
topic_type: "enforcement"
first_reported: 2024-08-20
last_updated: 2024-08-20
status_history: []
cluster: "Connected Car Telematics Data Sharing: State AG Enforcement Actions"
cluster_slug: "connected-car-telematics-data-broker-enforcement"
---

# Texas AG Sues General Motors and OnStar for Selling 1.8 Million Texans' Driving Data Without Consent

**Jurisdiction:** Texas | **Category:** privacy | **Date:** 2024-08-13

## Executive Summary [HIGH confidence]

On August 13, 2024, Texas Attorney General Ken Paxton filed suit against General Motors LLC and its OnStar LLC subsidiary in the District Court of Montgomery County, Texas (Case No. 24-08-12392), alleging the companies unlawfully collected and sold detailed driving behavior data from more than 1.8 million Texas drivers to third-party data brokers without meaningful consent. The complaint asserts violations of the [Texas Deceptive Trade Practices-Consumer Protection Act (DTPA), Texas Business & Commerce Code Chapter 17](https://statutes.capitol.texas.gov/Docs/BC/htm/BC.17.htm). GM and OnStar allegedly enrolled drivers in data-harvesting programs under false pretenses — including telling customers that declining enrollment would disable vehicle safety features — and then sold granular trip-by-trip driving records to companies such as LexisNexis and Verisk, which packaged the data into consumer risk scores sold to insurance carriers. Insurers used those scores to raise premiums or deny coverage, often without the driver's knowledge. The case represents the opening salvo in a broader Texas AG enforcement initiative targeting connected-vehicle data practices.

## Background [HIGH confidence]

### Connected-Vehicle Telematics and the Insurance Data Economy

Modern vehicles are equipped with telematics systems that continuously collect operational data: trip start and end times, vehicle speed, hard-braking events, hard-acceleration events, seatbelt status, miles driven, geolocation, and late-night driving patterns. Automakers transmit this data off-vehicle via embedded cellular connections to cloud platforms where it can be processed, stored, and monetized.

A parallel industry of automotive data brokers — principally [LexisNexis Risk Solutions](https://risk.lexisnexis.com/products/telematics) and [Verisk Analytics](https://www.verisk.com/insurance/products/telematics/) — emerged to aggregate telematics feeds from multiple automakers, compute behavioral risk scores ("Driving Scores"), and license those scores to property and casualty insurers. Insurers then factored the scores into underwriting decisions, often without disclosing to policyholders the data source. A [March 2024 New York Times investigation](https://www.nytimes.com/2024/03/11/technology/carmakers-driver-tracking-insurance.html) first surfaced the scope of this data-sharing arrangement, documenting cases where drivers received premium increases traceable to OnStar Smart Driver enrollment they did not recall making.

### Texas's Investigation and Prior Enforcement Posture

In [June 2024, AG Paxton announced](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-general-motors-unlawfully-collecting-drivers-private-data-and) he had opened formal investigations into several major automakers regarding unlawful data collection and sale practices. The GM lawsuit, filed approximately six weeks later, was the first enforcement action to emerge from that initiative. Texas framed the action as a consumer-protection matter under the DTPA rather than as a privacy enforcement action under the [Texas Data Privacy and Security Act (TDPSA)](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/consumer-privacy-rights/texas-data-privacy-and-security-act), which had only become effective July 1, 2024.

The choice of the DTPA was deliberate. The DTPA has decades of established case law and precedent, provides for civil penalties of up to [$20,000 per violation](https://statutes.capitol.texas.gov/Docs/BC/htm/BC.17.htm) (compared to the TDPSA's $7,500 per violation cap), and had already been used by the FTC in analogous federal actions.

## Detailed Analysis [HIGH confidence]

### Defendants and Scope

The defendants are **General Motors LLC** (the vehicle manufacturer and owner of the OnStar platform) and **OnStar LLC** (its wholly owned connected-services subsidiary). The petition covers GM's data-collection program from **2015 through March 2024**, during which the company collected driving data from more than **14 million GM vehicles nationwide**, including more than **1.8 million Texas drivers**.

### The Data Collection Mechanism

GM installed telematics hardware in vehicles beginning with 2015 model-year cars and later. The hardware was activated through OnStar's connected-services platform. The data collected per trip included:

- Trip start date, start time, and end time
- Vehicle speed data (including events above 80 mph)
- Hard-braking and hard-acceleration frequency
- Seatbelt engagement status for driver and passengers
- Distance driven
- Geolocation (precise GPS coordinates)
- Time-of-day and late-night driving patterns

This data was transmitted in near-real time to GM/OnStar cloud systems and then streamed to data broker partners pursuant to licensing agreements.

### The Data Broker Agreements

GM entered licensing agreements with at minimum the following entities to sell or license driving data:

- **[Verisk Analytics / DrivingData](https://www.verisk.com/insurance/)**: Agreement initiated in 2015. Verisk created a "Driving Score" based on GM telematics feeds and licensed that score to auto insurers. Verisk ceased selling car-company-provided driver behavior patterns to insurers following public backlash in 2024.
- **[LexisNexis Risk Solutions](https://risk.lexisnexis.com/)**: LexisNexis built consumer disclosure reports incorporating GM OnStar data that auto insurers could access through standard underwriting queries. LexisNexis continued operating its driver-behavior data product as of mid-2024 despite the mounting regulatory scrutiny.
- **Wejo Limited**: A UK-based automotive data broker also identified as a recipient in GM's data-sharing agreements.
- **Jacobs Engineering**: Also identified in the petition as a recipient, though the petition's characterization of this relationship has not been publicly detailed.

Per the [Texas AG's press release](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-general-motors-unlawfully-collecting-drivers-private-data-and), GM "profited handsomely" from these licensing arrangements, though the petition does not specify the total revenue received.

### Deceptive Enrollment Allegations

The DTPA claims rest heavily on GM's alleged misrepresentations during vehicle onboarding. The petition alleges GM:

1. **Compelled enrollment through safety feature threats**: During the vehicle onboarding process, customers who initially declined OnStar Smart Driver enrollment were allegedly told that refusing would result in deactivation of their vehicle's safety features (e.g., automatic crash notification, emergency services). This statement was allegedly false or misleading.

2. **Omitted material disclosures**: Despite lengthy privacy policies and terms of service, GM allegedly never clearly disclosed that enrollment in OnStar programs would result in the systematic sale of granular driving data to insurance-focused data brokers.

3. **Used confusing and vague language**: The consumer-facing disclosures used language that obscured the commercial nature and insurance-industry destination of the data sharing.

4. **Insurance rate impacts undisclosed**: Consumers were not told that their data would be used by insurers to calculate risk scores that could result in premium increases or coverage denials.

### Legal Basis

The petition asserts claims under the [Texas Deceptive Trade Practices-Consumer Protection Act, Texas Business & Commerce Code § 17.46](https://law.justia.com/codes/texas/2024/business-and-commerce-code/title-2/chapter-17/subchapter-e/), which prohibits "false, misleading, or deceptive acts or practices in the conduct of any trade or commerce." Under § 17.47, the AG may obtain injunctive relief and civil penalties. Penalties under § 17.47(c) can reach **$20,000 per violation per day** for violations after notice and a cease and desist. Given that 1.8 million Texas drivers are implicated, potential aggregate penalties could be substantial.

The petition was also accompanied by an application for a temporary restraining order and preliminary injunction.

### GM's Program Termination

General Motors had already terminated its data-broker sharing arrangements prior to the lawsuit's filing. [In March 2024](https://www.kbb.com/car-news/gm-stops-selling-driving-data-to-insurance-companies/), GM announced it was ending its partnerships with LexisNexis and Verisk and discontinuing the OnStar Smart Driver product. The termination was announced following the New York Times investigation and congressional inquiries from Senators Ron Wyden and Ed Markey. The Texas petition covers the period before that termination.

### Bankruptcy Court Complications

A subsequent litigation development complicated the Texas case. After Texas filed a **First Amended Petition on May 20, 2025**, which added allegations about "Old GM" conduct predating GM's 2009 bankruptcy restructuring, GM and OnStar filed an emergency motion in the [United States Bankruptcy Court for the Southern District of New York](https://www.nysb.uscourts.gov/sites/default/files/opinions/233396_14841_opinion.pdf) — the court overseeing GM's legacy 2009 bankruptcy — seeking to block Texas from using pre-bankruptcy conduct to calculate civil penalties against "New GM."

On **October 14, 2025**, the Bankruptcy Court [ruled in GM's favor](https://www.whiteandwilliams.com/restructuring-perspectives/bankruptcy-court-orders-texas-to-strike-allegations-in-state-data-privacy-suit-against-general-motors), finding that (1) it retains "core" jurisdiction over the 2009 Sale Order, and (2) Texas's attempt to use Old GM's pre-bankruptcy conduct to establish civil penalty liability against New GM constitutes impermissible successor liability barred by the Sale Order. Texas was ordered to strike the relevant allegations from its pending state-court complaint. The underlying case in Montgomery County, Texas remains pending as of early 2026.

## Impact Assessment [HIGH confidence]

### Affected Entities

**Automakers with telematics programs**: Any manufacturer using embedded cellular telematics and monetizing that data through third-party agreements faces similar exposure. Beyond GM, [LexisNexis's own disclosures](https://risk.lexisnexis.com/) identified Kia, Mitsubishi, Subaru, Honda, Hyundai, and Ford as additional automotive data sources. All are potentially exposed to analogous state AG actions.

**Insurance data brokers**: LexisNexis Risk Solutions and Verisk Analytics were the primary downstream recipients. Both operated in a largely unregulated space that assumed automaker consent flows were adequate. Texas's subsequent [January 2025 suit against Allstate's Arity subsidiary](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-allstate-insurance-privacy-law-violations) — the first action under the TDPSA — targeted the insurer-side data collection operation, extending the theory to insurers themselves.

**Property and casualty insurers**: Carriers that purchased and used driving scores in underwriting, premium-setting, or coverage-denial decisions without disclosing the data source to applicants face potential consumer protection exposure in Texas and other states.

### Multi-Jurisdictional Cascade

The Texas action catalyzed enforcement in other states:

- **[Arkansas](https://arkansasag.gov/news-release/attorney-general-griffin-sues-general-motors-and-onstar-for-deceiving-arkansans-and-unlawfully-selling-data/)**: AG Tim Griffin sued GM and OnStar on February 26, 2025, under the Arkansas Deceptive Trade Practices Act, alleging the same conduct pattern.
- **[Nebraska](https://ago.nebraska.gov/attorney-general-mike-hilgers-files-lawsuit-against-general-motors-deceptive-collection-and-sale)**: AG Mike Hilgers filed suit in July 2025, alleging deceptive collection and sale of Nebraskans' driving data since at least 2015.
- **[Montana](reports/privacy/enforcement-actions/montana-ford-stellantis-auto-data-cid-2026-04-19.md)**: The Montana AG subsequently issued civil investigative demands against Ford and Stellantis for similar connected-vehicle data practices (2026).

### Federal Parallel: FTC Action and Final Order

The [Federal Trade Commission filed a complaint against General Motors and OnStar](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-takes-action-against-general-motors-sharing-drivers-precise-location-driving-behavior-data) in January 2025, alleging violations of the FTC Act (Section 5) for the same underlying conduct. Under the [FTC's final order, finalized in January 2026](https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-finalizes-order-settling-allegations-gm-onstar-collected-sold-geolocation-data-without-consumers), GM and OnStar are:

- Banned for **five years** from sharing consumers' precise geolocation and driver behavior data with consumer reporting agencies
- Required to obtain **affirmative express consent** before collecting connected-vehicle data
- Required to create a mechanism for consumers to request and delete their data
- Required to give consumers the ability to disable precise geolocation collection

The FTC order does not include a monetary penalty but imposes significant behavioral remedies. The Texas state-court case and the FTC order run in parallel; the FTC order does not moot or preclude the Texas AG's damages and penalty claims.

### Compliance Implications for the Automotive Sector

The GM enforcement chain establishes that:

1. **Telematics consent flows must be granular and specific**: Bundled consent covering data sharing with insurance-focused brokers does not satisfy state DTPA or privacy law standards, particularly where the commercial purpose (insurer risk scoring) is not clearly disclosed.
2. **Safety feature conditioning is impermissible**: Telling consumers that declining data-collection enrollment will disable safety features is a material misrepresentation likely to constitute deception under state DTPA and UDAP statutes.
3. **Pre-existing broker agreements must be audited**: Even where an automaker has since terminated data-sharing arrangements, historical data flows remain subject to enforcement covering the period of active sharing.

## Action Items

- **Audit existing connected-vehicle data programs**: Identify all telematics data streams, downstream data-sharing agreements, and the commercial purposes for which partner entities use the data (especially insurance underwriting applications).
- **Review consent capture language**: Evaluate whether consumer-facing enrollment flows clearly disclose that driving data will be shared with third-party data brokers for insurance-related purposes. Vague or buried terms do not satisfy DTPA or privacy law standards.
- **Eliminate safety-feature conditioning**: Remove any language or flow logic that suggests declining data-collection enrollment will disable vehicle safety or emergency features. This framing has been specifically called out as deceptive in the GM petition.
- **Monitor the Montgomery County, Texas docket** (Case No. 24-08-12392): The underlying state court case remains pending; any ruling on DTPA liability or penalty calculation will create precedent for future auto-industry data enforcement.
- **Assess exposure in Arkansas and Nebraska**: If the entity collects and monetizes driving data from residents in those states, conduct a parallel exposure assessment given the subsequent AG actions filed in 2025.
- **Review FTC order compliance obligations**: Any entity that either (a) is in the automotive telematics supply chain or (b) handles consumer driving data as a downstream licensee should assess compliance with the January 2026 FTC final order's requirements regarding affirmative express consent and deletion rights.

## Related Reports

- [reports/privacy/enforcement-actions/texas-allstate-arity-tdpsa-enforcement-2026-04-14.md](reports/privacy/enforcement-actions/texas-allstate-arity-tdpsa-enforcement-2026-04-14.md) -- The first enforcement action under the TDPSA, filed by the same Texas AG against Allstate's Arity subsidiary for analogous location-data-to-insurer sharing; directly extends the enforcement theory from this GM DTPA case.
- [reports/privacy/enforcement-actions/montana-ford-stellantis-auto-data-cid-2026-04-19.md](reports/privacy/enforcement-actions/montana-ford-stellantis-auto-data-cid-2026-04-19.md) -- Montana AG civil investigative demands targeting Ford and Stellantis for connected-vehicle data practices; part of the same multi-state enforcement wave initiated by the Texas GM action.
- [reports/privacy/enforcement-actions/texas-allstate-arity-tdpsa-enforcement-2025-01-15.md](reports/privacy/enforcement-actions/texas-allstate-arity-tdpsa-enforcement-2025-01-15.md) -- Earlier research memo on the same Allstate/Arity action; provides additional TDPSA technical analysis.

## Sources

1. [Texas AG Press Release — Paxton Sues General Motors](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-general-motors-unlawfully-collecting-drivers-private-data-and) — Official AG announcement with filing date, defendants, and key allegations.
2. [State of Texas v. General Motors LLC and OnStar LLC — Filed Petition (PDF)](https://www.texasattorneygeneral.gov/sites/default/files/images/press/General%20Motors%20Data%20Privacy%20Petition%20Filed.pdf) — Official court petition; primary source for legal claims, statute citations, and data scope.
3. [Texas Business & Commerce Code Chapter 17 — DTPA](https://statutes.capitol.texas.gov/Docs/BC/htm/BC.17.htm) — Official statutory text of the Texas Deceptive Trade Practices-Consumer Protection Act.
4. [Justia: Texas BCC § 17.46 Subchapter E (2024)](https://law.justia.com/codes/texas/2024/business-and-commerce-code/title-2/chapter-17/subchapter-e/) — Searchable 2024 version of the DTPA unlawful practices provision.
5. [Texas Data Privacy and Security Act — AG Overview](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/consumer-privacy-rights/texas-data-privacy-and-security-act) — Official AG page describing TDPSA enforcement authority and penalty structure (for comparison with DTPA).
6. [FTC Press Release — FTC Takes Action Against GM, January 2025](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-takes-action-against-general-motors-sharing-drivers-precise-location-driving-behavior-data) — Federal complaint announcement; confirms overlapping federal enforcement theory.
7. [FTC Final Order Against GM/OnStar, January 2026](https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-finalizes-order-settling-allegations-gm-onstar-collected-sold-geolocation-data-without-consumers) — Finalized behavioral remedies; 5-year data-sharing ban and consent requirements.
8. [White & Williams — Bankruptcy Court Orders Texas to Strike Allegations](https://www.whiteandwilliams.com/restructuring-perspectives/bankruptcy-court-orders-texas-to-strike-allegations-in-state-data-privacy-suit-against-general-motors) — Law firm analysis of October 2025 Bankruptcy Court ruling barring use of pre-2009 Old GM conduct.
9. [SDNY Bankruptcy Court Opinion — Motors Liquidation Company](https://www.nysb.uscourts.gov/sites/default/files/opinions/233396_14841_opinion.pdf) — Official court opinion from the Bankruptcy Court ruling.
10. [Arkansas AG — Lawsuit Against GM and OnStar](https://arkansasag.gov/news-release/attorney-general-griffin-sues-general-motors-and-onstar-for-deceiving-arkansans-and-unlawfully-selling-data/) — Official Arkansas AG announcement; February 2025 parallel state enforcement.
11. [Nebraska AG — Lawsuit Against General Motors](https://ago.nebraska.gov/attorney-general-mike-hilgers-files-lawsuit-against-general-motors-deceptive-collection-and-sale) -- Official Nebraska AG announcement; July 2025 parallel state enforcement.
12. [Kelley Blue Book — GM Stops Selling Driving Data](https://www.kbb.com/car-news/gm-stops-selling-driving-data-to-insurance-companies/) — Contemporaneous reporting on GM's March 2024 termination of broker agreements.
13. [The Record — GM Lawsuit Is Texas AG's First Privacy Initiative Shot](https://therecord.media/gm-lawsuit-texas-data-privacy) -- News analysis contextualizing the GM case within Texas's broader privacy enforcement strategy.
14. [White & Case — Texas AG Landmark Privacy Lawsuit Analysis](https://www.whitecase.com/insight-alert/texas-attorney-generals-landmark-privacy-lawsuit-signals-new-era-data-privacy) — Law firm analysis of the enforcement significance and legal strategy.
15. [Trellis — Case No. 24-08-12392 Docket](https://trellis.law/case/48339/24-08-12392/state-texas-vs-general-motors-llc-onstar-llc) — Court docket for the Montgomery County, Texas state-court proceeding.
