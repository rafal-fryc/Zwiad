---
title: "ELSAG SignalTrace: License Plate Readers Expanded to Harvest Bluetooth, Wi-Fi, and RFID Device Identifiers, Creating Mass Surveillance Infrastructure Gap"
date: 2026-06-24
jurisdiction: "Federal"
category: "privacy"
development_type: "other"
finding_id: "SCAN-20260628-021"
topic_key: "federal-990ad112-2026"
topic_type: "guidance"
first_reported: 2026-06-24
last_updated: 2026-06-29
status_history: []
cluster: "ELSAG SignalTrace: ALPR Multi-Modal Device Identifier Surveillance Infrastructure"
cluster_slug: "elsag-signaltrace-alpr-device-identifier-surveillance"
---

# ELSAG SignalTrace: License Plate Readers Expanded to Harvest Bluetooth, Wi-Fi, and RFID Device Identifiers, Creating Mass Surveillance Infrastructure Gap

**Jurisdiction:** Federal | **Category:** Privacy | **Date:** 2026-06-24

## Executive Summary [MEDIUM confidence]

Leonardo US Cyber and Security Solutions has launched ELSAG SignalTrace, a software and sensor system that transforms existing automated license plate reader (ALPR) deployments into multi-modal surveillance nodes capable of harvesting Bluetooth, Wi-Fi, and RFID identifiers from smartphones, wearables, pet microchips, and other consumer electronics in passing vehicles. By correlating device identifiers repeatedly appearing alongside the same plate number, the system generates persistent electronic profiles linking specific individuals to vehicle movements across time and space — without a warrant, without consent, and without any existing federal regulatory framework expressly governing this capability. The development has drawn immediate scrutiny from the Electronic Frontier Foundation (EFF) and the American Civil Liberties Union (ACLU), which argue the technology enables warrantless population-scale surveillance. No federal statute specifically addresses commercial ALPR-plus-device-fingerprinting systems; Congress has debated but not passed legislation that would close the relevant regulatory gap.

## Background [HIGH confidence]

### Automated License Plate Readers: Established Infrastructure

Automated license plate readers are optical camera systems that capture vehicle registration plates and match them against databases of plates of interest. As described in the [Congressional Research Service report on ALPR technology (R48160)](https://www.congress.gov/crs-product/R48160), ALPR systems work by automatically capturing images of passing vehicles, running an algorithm to read the plate, and logging the result with a time-stamped GPS location. ALPRs have been deployed by law enforcement agencies for two decades for applications including stolen vehicle recovery, Amber Alert searches, and warrant enforcement.

The ALPR market has grown substantially through commercial deployments by companies such as Flock Safety and Leonardo's ELSAG division. As of 2025, ALPRs had been deployed at traffic intersections, highway on-ramps, parking facilities, and private communities across the United States, with some networks covering hundreds of thousands of cameras. The ACLU documented that plate readers alone already "create permanent records of virtually everywhere any of us has driven," with data retained for months or years.

### Legal Landscape Prior to SignalTrace

The Fourth Amendment legal framework for ALPRs remains unsettled. As noted in the [CRS ALPR background report (IF13068)](https://www.congress.gov/crs-product/IF13068), no federal appellate court has decided whether law enforcement queries of ALPR databases constitute a Fourth Amendment search. Federal trial courts have generally upheld law enforcement access to ALPR databases while acknowledging that extended surveillance could raise constitutional concerns under the mosaic theory articulated in *United States v. Jones*, 565 U.S. 400 (2012), where five justices in concurrence suggested that prolonged GPS tracking may require a warrant even if individual observations do not.

No comprehensive federal statute governs ALPR data collection, retention, or commercial sale. State statutes addressing ALPRs were drafted narrowly to cover photographic plate capture; none anticipated the harvesting of electronic device identifiers from vehicle occupants. As reported by [Stateline](https://stateline.org/2025/10/10/despite-widespread-interest-only-3-states-passed-license-plate-reader-laws-this-year/), despite substantial legislative interest in 2025, only three states enacted ALPR laws. Washington State's Governor [signed SB 6002 (the Driver Privacy Act) on March 30, 2026](https://www.aclu-wa.org/press-releases/gov-ferguson-signs-sb-6002-the-driver-privacy-act-into-law/); California and Virginia enacted retention limitation provisions effective January 2026. None of these laws address Bluetooth or Wi-Fi harvesting by ALPR-adjacent sensors.

### The "Data Broker Loophole" and Commercial Surveillance Context

SignalTrace's commercial availability intersects with a separately documented concern: federal and state agencies have purchased commercial location data without obtaining warrants. The FTC finalized enforcement orders against [Gravy Analytics and Venntel](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-order-prohibiting-gravy-analytics-venntel-selling-sensitive-location-data) in January 2025, and against [Mobilewalla](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-order-banning-mobilewalla-selling-sensitive-location-data) for collecting and selling sensitive location data without proper consumer consent. The FTC also sent warning letters to 13 data brokers in February 2026 regarding their obligations under the [Protecting Americans' Data from Foreign Adversaries Act (PADFA)](https://www.ftc.gov/news-events/news/press-releases/2026/02/ftc-reminds-data-brokers-their-obligations-comply-padfaa), which carries civil penalties of up to $53,088 per violation. These actions target location data brokers operating through mobile advertising ecosystems; no comparable enforcement framework presently reaches ALPR-derived device fingerprint data.

## Detailed Analysis [MEDIUM confidence]

### What SignalTrace Does

[Leonardo US Cyber and Security Solutions](https://www.leonardocompany-us.com/lpr/elsag-signaltrace) markets ELSAG SignalTrace as "a groundbreaking software system for law enforcement, designed to identify suspect people or vehicles, even when a license plate number is not known." The system adds sensors to existing ALPR camera installations — or deploys standalone sensors in "off-road and non-traffic environments such as rail stations, event venues, and shopping centers" — that passively sweep for signals broadcast by consumer electronics. According to [Leonardo's product materials](https://www.leonardocompany-us.com/lpr/signaltrace-product-sheet) and [a documentary product sheet archived by DocumentCloud](https://s3.documentcloud.org/documents/28215440/signaltrace-us.pdf), the identifiers captured include:

- Bluetooth device identifiers from smartphones, wireless headphones, fitness trackers, and smartwatches (including Apple AirPods and Apple Watch)
- Wi-Fi probe requests from mobile phones and tablets
- RFID tags from key fobs, key cards, and asset trackers
- Pet microchip signals (passive RFID)
- Vehicle-native signals including tire pressure sensor IDs, infotainment system identifiers, and vehicle hotspot SSIDs

The system processes these identifiers by identifying device signatures that repeatedly appear alongside the same plate number across multiple capture events. Repeated co-occurrence links the device to the vehicle, and the vehicle's plate is then linked to a registered owner. The combined record — plate, owner, device identifiers, time-stamped locations — is stored in Leonardo's Enterprise Operations Center for retrospective querying and prospective alerting. As [404 Media first reported](https://www.404media.co/this-company-will-add-phone-airpod-and-smartwatch-trackers-to-license-plate-readers/), law enforcement could use the resulting database to identify a suspect's device fingerprint from a prior incident and then receive real-time alerts when that fingerprint is detected at a new location.

### Novel Legal and Technical Issues

This capability creates at least three categories of novel legal issues not addressed by existing ALPR jurisprudence or statute.

**First, device fingerprinting is categorically different from plate reading.** ALPRs read information the state itself assigned and requires to be publicly displayed: a vehicle registration plate. Device Bluetooth and Wi-Fi identifiers are not publicly required disclosures; they are emitted incidentally by privately owned consumer electronics. The expectation-of-privacy analysis that permits plate reading — reading what the government mandates be displayed — does not straightforwardly extend to harvesting identifiers from phones in drivers' pockets, as noted by [Tech Republic](https://www.techrepublic.com/article/news-leonardo-signaltrace-alpr-device-tracking/) and other technology analysts.

**Second, device identifiers enable person-tracking, not vehicle-tracking.** A license plate identifies a registered vehicle owner. A smartphone Bluetooth MAC address identifies an individual who may be a driver, passenger, or bystander. Once correlated, the system can track an individual across vehicle changes — if a person switches cars but carries the same phone, their device fingerprint persists in the database. Bruce Schneier noted in his [security analysis](https://www.schneier.com/blog/archives/2026/06/enhanced-license-plate-tracking.html) that "what once tracked vehicles now tracks the people inside them," a qualitative expansion that the existing constitutional mosaic-theory cases have not addressed in the ALPR context.

**Third, the regulatory vacuum is structural, not incidental.** As the [Deep Dive Canada analysis](https://thedeepdive.ca/leonardo-signaltrace-alpr-device-tracking/) summarized, "no federal law explicitly prohibits law enforcement from collecting Bluetooth identifiers via roadside surveillance, nor is there clear guidance on how long such data can be retained or who can access it." State ALPR statutes were drafted around photographic plate capture; none contain retention or access provisions that would apply to Wi-Fi or RFID sweeping. The Stored Communications Act does not reach passively broadcast device identifiers. The Electronic Communications Privacy Act's interception provisions were not designed for passive radio signal harvesting.

### Company Background and Federal Procurement Reach

Leonardo S.p.A. is a large, publicly traded Italian defense and aerospace company. Its U.S. subsidiary, Leonardo US Cyber and Security Solutions, holds existing contracts with [U.S. Special Operations Command and the General Services Administration](https://www.404media.co/this-company-will-add-phone-airpod-and-smartwatch-trackers-to-license-plate-readers/), meaning SignalTrace has a direct pathway to federal law enforcement procurement without new contracting infrastructure. Leonardo already operates the ELSAG ALPR platform across numerous U.S. jurisdictions; SignalTrace is positioned as a software upgrade deployable on existing hardware.

### Privacy Advocacy Response

The EFF, monitoring ALPR capability expansion, applied the term "mission creep" to SignalTrace — citing its practice of infrastructure approved for one stated purpose acquiring new capabilities without fresh democratic approval. The [ACLU has called for a moratorium](https://protonprivacy.substack.com/p/forget-flock-now-the-cameras-can) on SignalTrace deployment until privacy safeguards are established, noting that the ALPR layer already "create[s] permanent records of virtually everywhere any of us has driven" and that adding device fingerprints generates "home addresses, workplaces, medical visits, and social associations — without a warrant."

Critics have raised particular concerns about the commercial availability dimension: even if law enforcement deployment is subject to some internal policy constraints (however minimal), the same data could be licensed or sold to private investigators, insurance companies, employers, or stalkers through data broker intermediaries. Existing federal data broker regulation under the FTC's Section 5 authority has targeted location data from mobile advertising ecosystems; no enforcement action has addressed ALPR-derived device fingerprint data.

### Congressional Activity

Congress has debated but not enacted legislation that would directly constrain SignalTrace-type commercial surveillance.

The [Fourth Amendment Is Not For Sale Act](https://www.wyden.senate.gov/news/press-releases/wyden-paul-and-bipartisan-senators-reintroduce-the-fourth-amendment-is-not-for-sale-act) passed the House in April 2024 with bipartisan support (219–199) but died in the Senate. The bill would prohibit law enforcement and intelligence agencies from purchasing personal data — including geolocation data — from third-party sellers without a warrant. As of June 2026 the bill has not advanced in the 119th Congress.

The House Republican [SECURE Data Act (HR 8413)](https://www.hunton.com/privacy-and-cybersecurity-law-blog/house-republicans-introduce-comprehensive-federal-privacy-bill-secure-data-act), introduced in April 2026, establishes a data broker definition and registry regime but does not specifically address law enforcement purchase of ALPR-adjacent data or impose restrictions on commercial surveillance sensor networks. A [June 3, 2026 House subcommittee hearing](https://energycommerce.house.gov/posts/committees-on-energy-and-commerce-and-financial-services-introduce-pair-of-privacy-bills-to-establish-comprehensive-data-protections-for-all-americans) on the SECURE Data Act and a companion financial privacy bill did not surface ALPR-specific provisions.

The [American Data Privacy and Protection Act (ADPPA)](https://en.wikipedia.org/wiki/American_Data_Privacy_and_Protection_Act), which stalled in the prior Congress, would have specifically limited transfer of precise geolocation data; it has not been reintroduced in the 119th Congress.

## Impact Assessment [MEDIUM confidence]

### Affected Entities

**Individuals:** Any person driving, riding in, or walking near a vehicle in range of a SignalTrace sensor — estimated to ultimately include any American navigating public roads if deployment scales as Leonardo envisions. Populations with heightened vulnerability include domestic violence survivors, journalists' sources, undocumented immigrants, protesters, patients traveling to sensitive medical appointments, and individuals targeted by stalkers or abusers with access to commercial data brokers.

**Law enforcement agencies:** Agencies that adopt SignalTrace gain substantially expanded investigative capability but also inherit legal risk. Courts applying an expanded mosaic theory could suppress evidence collected without a warrant under *Carpenter v. United States*, 585 U.S. 296 (2018), which held that the third-party doctrine does not apply to prolonged CSLI collection. Whether *Carpenter* extends to ALPR-plus-device-fingerprint collection is not settled.

**Data brokers and private surveillance firms:** The commercial availability framing in Leonardo's marketing — the product is not limited to law enforcement — creates potential for the database to be queried by private parties. Commercial availability without robust access controls or audit mechanisms would replicate the patterns the FTC targeted in the Gravy Analytics and Mobilewalla enforcement actions.

**State and local governments:** Jurisdictions that have enacted ALPR data retention limits (California, Washington, Virginia) may face ambiguity about whether those limits extend to Bluetooth/RFID identifiers collected by SignalTrace sensors co-located with ALPR cameras.

### Compliance and Regulatory Outlook

There is no existing federal compliance regime that directly applies to SignalTrace as a product or to the data it collects. Agencies deploying the system operate in a legal gray zone. The most plausible near-term regulatory intervention vectors are:

1. **FTC enforcement** under Section 5 unfair or deceptive acts or practices authority, following the Gravy Analytics/Mobilewalla precedent, if the SignalTrace database is made commercially available without adequate consent or access controls.
2. **Congressional action** through the Fourth Amendment Is Not For Sale Act (if revived) or a SignalTrace-specific amendment to a comprehensive privacy bill.
3. **State legislation** extending existing ALPR statutes to cover co-located device harvesting sensors; the California ALPR retention bills (SB 274, SB 1013) currently in the 2025–2026 session could potentially be amended to this effect.
4. **Constitutional litigation** under *Carpenter* or state constitutional privacy provisions, which may result in evidence suppression and agency policy changes even absent legislation.

## Action Items

- Monitor Leonardo's GSA and federal agency contracting filings for SignalTrace procurement awards, which would signal deployment scale and potential federal procurement questions.
- Track California SB 274 and SB 1013 (ALPR retention bills) for any amendment activity that extends their scope to device identifier harvesting.
- Track the Fourth Amendment Is Not For Sale Act for reintroduction or attachment as an amendment to the SECURE Data Act during House floor consideration.
- Advise clients operating in sensitive sectors (domestic violence services, reproductive health, immigration legal services, journalism) to assess whether their clients' travel patterns could be exposed through ALPR-adjacent device fingerprinting.
- Organizations with supply-chain or vendor relationships with data broker intermediaries should review whether those intermediaries could acquire SignalTrace-derived data and whether existing vendor contracts address the obligation not to purchase surveillance-derived personal data.
- Review existing state ALPR compliance policies to determine whether existing retention and access controls are scoped to cover non-photographic signal collection; if not, policies should be updated proactively in anticipation of regulatory clarification.

## Related Reports

- [reports/privacy/federal-ice-domestic-surveillance-tools-2026-05-04.md](reports/privacy/federal-ice-domestic-surveillance-tools-2026-05-04.md) — Covers ICE's expanded commercial data broker and surveillance tool contracts, directly relevant to potential government procurement of SignalTrace-derived data.
- [reports/privacy/federal-meta-smart-glasses-facial-recognition-coalition-2026-04-14.md](reports/privacy/federal-meta-smart-glasses-facial-recognition-coalition-2026-04-14.md) — Addresses the same mission-creep pattern of consumer electronics being repurposed for ambient surveillance without consent; the ACLU and EFF coalition response parallels their SignalTrace positions.
- [reports/privacy/federal-legislation/federal-secure-data-act-hr8413-june-hearing-2026-06-01.md](reports/privacy/federal-legislation/federal-secure-data-act-hr8413-june-hearing-2026-06-01.md) — Covers the SECURE Data Act, the most active comprehensive federal privacy bill as of June 2026, which could be amended to address commercial surveillance aggregation.

## Sources

1. [ELSAG SignalTrace Product Page — Leonardo US](https://www.leonardocompany-us.com/lpr/elsag-signaltrace) — Official Leonardo US product description of SignalTrace capabilities and deployment scope.
2. [SignalTrace Product Sheet — Leonardo US](https://www.leonardocompany-us.com/lpr/signaltrace-product-sheet) — Official Leonardo marketing sheet listing device types captured (phones, wearables, RFID, pet microchips).
3. [SignalTrace Product Sheet PDF — DocumentCloud](https://s3.documentcloud.org/documents/28215440/signaltrace-us.pdf) — Archived Leonardo product sheet with technical capability details.
4. [This Company Will Add Phone, AirPod, and Smartwatch Trackers to License Plate Readers — 404 Media](https://www.404media.co/this-company-will-add-phone-airpod-and-smartwatch-trackers-to-license-plate-readers/) — Primary investigative report breaking the SignalTrace story; details on operational use cases and federal procurement pathways.
5. [Enhanced License Plate Tracking — Schneier on Security](https://www.schneier.com/blog/archives/2026/06/enhanced-license-plate-tracking.html) — Bruce Schneier's security analysis of the person-versus-vehicle tracking distinction.
6. [Leonardo's SignalTrace Could Let Police Plate Readers Track Your Devices — The Deep Dive](https://thedeepdive.ca/leonardo-signaltrace-alpr-device-tracking/) — Analysis of the regulatory vacuum and absence of federal law governing Bluetooth identifier collection.
7. [License Plate Readers Gain Eyes on Your Phone, AirPods and Watch — Tech Republic](https://www.techrepublic.com/article/news-leonardo-signaltrace-alpr-device-tracking/) — Technical analysis of device identifier types and privacy implications.
8. [Don't Like Car License Plate Readers Invading Your Privacy? It's About To Get A Lot Worse — Car Buzz](https://carbuzz.com/license-plate-readers-detect-electronic-devices-privacy-concerns/) — Summary of ACLU moratorium call and privacy advocacy context.
9. [Forget Flock. Now the Cameras Can Read Your Pockets Too — Proton Privacy (Substack)](https://protonprivacy.substack.com/p/forget-flock-now-the-cameras-can) — EFF "mission creep" framing and ACLU moratorium call; analysis of commercial availability risks.
10. [Law Enforcement and Technology: Use of Automated License Plate Readers — Congressional Research Service (R48160)](https://www.congress.gov/crs-product/R48160) — Official CRS report on ALPR background, legal framework, and Fourth Amendment case law.
11. [Automated License Plate Readers: Background and Legal Issues — Congressional Research Service (IF13068)](https://www.congress.gov/crs-product/IF13068) — CRS brief on ALPR Fourth Amendment issues and absence of federal appellate precedent.
12. [Despite Widespread Interest, Only 3 States Passed License Plate Reader Laws This Year — Stateline](https://stateline.org/2025/10/10/despite-widespread-interest-only-3-states-passed-license-plate-reader-laws-this-year/) — Documents limited state legislative progress on ALPR regulation in 2025.
13. [Growing Privacy Regulation of Automatic License Plate Readers — Winston & Strawn](https://www.winston.com/en/blogs-and-podcasts/privacy-law-corner/growing-privacy-regulation-of-automatic-license-plate-readers) — Law firm analysis of state ALPR legislation trends.
14. [FTC Finalizes Order Prohibiting Gravy Analytics and Venntel from Selling Sensitive Location Data — FTC Press Release](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-order-prohibiting-gravy-analytics-venntel-selling-sensitive-location-data) — January 14, 2025 final FTC order prohibiting Gravy Analytics and Venntel from selling sensitive location data; establishes Section 5 precedent applicable to ALPR-adjacent surveillance data.
15. [FTC Finalizes Order Banning Mobilewalla — FTC Press Release](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-order-banning-mobilewalla-selling-sensitive-location-data) — Final FTC order in Mobilewalla case banning sale of sensitive location data.
16. [FTC Reminds Data Brokers of Obligations Under PADFA — FTC Press Release](https://www.ftc.gov/news-events/news/press-releases/2026/02/ftc-reminds-data-brokers-their-obligations-comply-padfaa) — FTC February 2026 warning letters on PADFA compliance; civil penalty exposure for data broker violations.
17. [Wyden, Paul Reintroduce the Fourth Amendment Is Not For Sale Act — Senator Wyden Press Release](https://www.wyden.senate.gov/news/press-releases/wyden-paul-and-bipartisan-senators-reintroduce-the-fourth-amendment-is-not-for-sale-act) — Official Senate press release on the bill prohibiting warrantless government purchase of location data.
18. [House Passes Fourth Amendment Is Not For Sale Act — CyberScoop](https://cyberscoop.com/house-passes-4th-amendment-is-not-for-sale-act/) — Reports House passage in April 2024 and Senate inaction.
19. [House Republicans Introduce SECURE Data Act — Hunton](https://www.hunton.com/privacy-and-cybersecurity-law-blog/house-republicans-introduce-comprehensive-federal-privacy-bill-secure-data-act) — Law firm analysis of the SECURE Data Act introduced April 2026; data broker registry provisions.
20. [Carpenter v. United States, 585 U.S. 296 (2018)](https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf) — Supreme Court ruling that prolonged CSLI collection requires a warrant; most likely constitutional precedent to govern SignalTrace disputes.
21. [IAPP News: New Tracking Tool Connects License Plates, Smart Device Data](https://iapp.org/news/a/new-tracking-tool-connects-license-plates-smart-device-data) — Original IAPP Daily Dashboard report that identified this development for monitoring.
22. [Gov. Ferguson Signs SB 6002, the Driver Privacy Act, into Law — ACLU of Washington](https://www.aclu-wa.org/press-releases/gov-ferguson-signs-sb-6002-the-driver-privacy-act-into-law/) — ACLU-WA press release confirming Governor Ferguson signed SB 6002 on March 30, 2026; primary source for the signing date.
