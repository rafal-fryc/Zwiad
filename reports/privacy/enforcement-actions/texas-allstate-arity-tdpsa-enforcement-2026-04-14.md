---
finding_id: "SCAN-20260414-014"
format: "client-alert"
title: "Texas AG Sues Allstate and Arity in First-Ever State Comprehensive Privacy Law Enforcement Action"
date: "2026-04-14"
jurisdiction: "Texas"
category: "privacy"
development_type: "enforcement"
topic_key: "TXAG-ALLSTATE-2026"
topic_type: "enforcement"
first_reported: "2026-04-14"
last_updated: "2026-04-14"
status_history: []
cluster: "Texas AG v. Allstate/Arity: TDPSA Enforcement Action"
cluster_slug: "texas-ag-allstate-arity-tdpsa-enforcement"
---

# Texas AG Sues Allstate and Arity in First-Ever State Comprehensive Privacy Law Enforcement Action

**Jurisdiction:** Texas | **Category:** privacy | **Date:** 2026-04-14

## Summary [HIGH confidence]

Texas Attorney General Ken Paxton has filed the first-ever enforcement action under a U.S. state comprehensive data privacy law, [suing Allstate and its subsidiary Arity](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-allstate-and-arity-unlawfully-collecting-using-and-selling-over-45) for unlawfully collecting, using, and selling precise geolocation and driving behavior data from more than 45 million Americans. The complaint, filed January 13, 2025 in the District Court of Montgomery County, Texas, alleges that the defendants embedded a software development kit (SDK) in popular third-party mobile apps — including Life360, GasBuddy, Fuel Rewards, and Routely — to secretly harvest consumer data without notice or consent, then used it to underwrite policies and sold it to other insurers to adjust premiums and deny coverage. The case is widely regarded as a landmark precedent that will shape Texas Data Privacy and Security Act (TDPSA) enforcement and SDK-based data collection practices nationwide.

## Key Facts [HIGH confidence]

- The lawsuit was filed on January 13, 2025 by Texas AG Ken Paxton in the District Court of Montgomery County, Texas, asserting claims under the TDPSA, the Texas Data Broker Law, and the Texas Insurance Code's prohibition on unfair and deceptive acts in the business of insurance ([V&E analysis](https://www.velaw.com/insights/texas-ag-targets-allstate-in-first-enforcement-of-texas-data-privacy-and-security-act/); [Texas OAG press release](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-allstate-and-arity-unlawfully-collecting-using-and-selling-over-45)).
- Defendants allegedly paid third-party app developers millions of dollars to embed Arity's SDK into Life360, GasBuddy, Fuel Rewards, and Routely, with bonus incentives tied to expanding the "driving behavior" database ([Texas OAG press release](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-allstate-and-arity-unlawfully-collecting-using-and-selling-over-45)).
- The SDK allegedly captured latitude, longitude, speed, GPS time, bearing, and altitude at intervals of 15 seconds or less from approximately 40 million active connections, compiling what the State describes as "the world's largest driving behavior database" covering over 45 million Americans ([WilmerHale analysis](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20250121-texas-ag-brings-first-ever-lawsuit-under-a-state-comprehensive-privacy-law)).
- The complaint alleges three TDPSA violation theories: (1) failure to provide a clear and accessible privacy notice of geolocation collection; (2) failure to obtain affirmative consent for processing precise geolocation, a category of "sensitive data" under the statute; and (3) failure to provide a consumer opt-out mechanism for data sales and targeted advertising ([Hunton Andrews Kurth analysis](https://www.hunton.com/privacy-and-information-security-law/texas-ag-sues-allstate-for-violations-of-texas-privacy-law-in-first-enforcement-action-under-a-state-comprehensive-data-privacy-law)).
- Arity is separately alleged to have violated the Texas Data Broker Law (Tex. Bus. & Com. Code Ch. 509) by failing to register with the Texas Secretary of State by the March 1, 2024 deadline, despite deriving revenue from processing personal data of more than 50,000 individuals it did not collect directly ([Texas OAG press release](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-allstate-and-arity-unlawfully-collecting-using-and-selling-over-45)).
- The State is seeking more than $1,000,000 in civil penalties, including up to $7,500 per TDPSA violation and up to $10,000 per Texas Data Broker Law violation, plus injunctive relief ([Texas OAG press release](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-allstate-and-arity-unlawfully-collecting-using-and-selling-over-45); [WilmerHale analysis](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20250121-texas-ag-brings-first-ever-lawsuit-under-a-state-comprehensive-privacy-law)).
- The data was allegedly used to underwrite Allstate policies and resold to other insurance carriers who used it to assess driver risk, adjust premiums, and in some cases deny or drop coverage ([V&E analysis](https://www.velaw.com/insights/texas-ag-targets-allstate-in-first-enforcement-of-texas-data-privacy-and-security-act/)).
- The official complaint (petition) is publicly available from the Texas AG ([Allstate and Arity Petition Filed.pdf](https://www.texasattorneygeneral.gov/sites/default/files/images/press/Allstate%20and%20Arity%20Petition%20Filed.pdf)).

## Why It Matters [HIGH confidence]

This is the first public enforcement action brought by any state attorney general under a comprehensive consumer data privacy law, and it establishes several patterns likely to be replicated across the 19+ U.S. states with similar statutes ([White & Case analysis](https://www.whitecase.com/insight-alert/texas-attorney-generals-landmark-privacy-lawsuit-signals-new-era-data-privacy)):

- **SDK supply-chain liability.** The theory of the case treats the SDK operator (Arity) and the app publishers as joint data collectors, exposing both to notice-and-consent obligations. Companies that embed or license SDKs for analytics, advertising, or behavioral scoring face direct attention from regulators.
- **Precise geolocation as sensitive data.** The TDPSA (Tex. Bus. & Com. Code Ch. 541) classifies precise geolocation data as "sensitive data" requiring opt-in consent before processing. Texas is signaling that burying consent in app EULAs or general privacy policies will not satisfy that standard.
- **Data broker registration is not optional.** Texas's willingness to pursue a stand-alone Data Broker Law count alongside the TDPSA claims demonstrates the State will use registration failures as an independent enforcement hook with meaningful per-violation penalties.
- **No cure period defense for pre-cure conduct.** Although the TDPSA contains a 30-day cure period, the AG's approach suggests the State will still seek penalties for conduct that continued without cure or that was too pervasive to cure meaningfully ([Hunton Andrews Kurth analysis](https://www.hunton.com/privacy-and-information-security-law/texas-ag-sues-allstate-for-violations-of-texas-privacy-law-in-first-enforcement-action-under-a-state-comprehensive-data-privacy-law)).
- **Insurance-law overlay.** Pairing TDPSA counts with an Insurance Code unfair-practices count gives the State an additional statutory penalty track and signals that data-driven underwriting practices are now a privacy enforcement target.

## Action Items

- **Inventory SDKs.** Companies that publish or embed SDKs collecting location, telematics, or behavioral data should immediately inventory every SDK deployed across their apps, identify what data leaves the device, and confirm whether precise geolocation is captured.
- **Re-paper consent flows.** Verify that any collection of precise geolocation, health, biometric, or other "sensitive data" under the TDPSA is gated by affirmative, opt-in consent presented clearly outside of boilerplate terms of service.
- **Confirm data broker registration.** Any entity deriving revenue from personal data of 50,000+ Texans it did not collect directly must register with the Texas Secretary of State under Tex. Bus. & Com. Code Ch. 509; unregistered entities should register immediately and assess historical exposure.
- **Review downstream sales contracts.** Companies selling or licensing consumer data to insurers, advertisers, or analytics partners should confirm that contracts mirror the TDPSA's controller/processor obligations and that opt-out rights flow through.
- **Monitor the docket.** The Montgomery County filing is the template other AGs will study. Track motion practice, any settlement or consent order, and watch for follow-on actions from California, Connecticut, Oregon, and Colorado regulators.
- **Assess insurance-underwriting practices.** Carriers using third-party telematics or behavioral data for pricing should document the provenance and consent basis of that data and evaluate Insurance Code UDAP exposure.

## Related Reports

No related reports found in the knowledge base.

## Sources

1. [Texas Office of the Attorney General — Press Release (Jan. 13, 2025)](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-allstate-and-arity-unlawfully-collecting-using-and-selling-over-45) — Primary official announcement with allegations, statutes cited, and penalty demand.
2. [Texas OAG — Allstate and Arity Petition Filed (PDF)](https://www.texasattorneygeneral.gov/sites/default/files/images/press/Allstate%20and%20Arity%20Petition%20Filed.pdf) — Official complaint filed in Montgomery County District Court.
3. [White & Case — Texas Attorney General's Landmark Privacy Lawsuit Signals New Era in Data Privacy Enforcement](https://www.whitecase.com/insight-alert/texas-attorney-generals-landmark-privacy-lawsuit-signals-new-era-data-privacy) — Law firm analysis of national enforcement implications.
4. [WilmerHale — Texas AG Brings First Ever Lawsuit Under a State Comprehensive Privacy Law](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20250121-texas-ag-brings-first-ever-lawsuit-under-a-state-comprehensive-privacy-law) — Detailed factual and statutory breakdown of the complaint.
5. [Vinson & Elkins — Texas AG Targets Allstate in First Enforcement of Texas Data Privacy and Security Act](https://www.velaw.com/insights/texas-ag-targets-allstate-in-first-enforcement-of-texas-data-privacy-and-security-act/) — Analysis of Insurance Code and TDPSA interplay.
6. [Hunton Andrews Kurth — Texas AG Sues Allstate for Violations of Texas Privacy Law](https://www.hunton.com/privacy-and-information-security-law/texas-ag-sues-allstate-for-violations-of-texas-privacy-law-in-first-enforcement-action-under-a-state-comprehensive-data-privacy-law) — TDPSA statutory-provision mapping and compliance takeaways.
