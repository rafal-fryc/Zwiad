---
title: "FTC v. Kochava: Settlement Bars Sale of Sensitive Location Data Without Consent"
date: 2026-05-08
jurisdiction: "Federal"
category: "privacy"
development_type: "enforcement"
finding_id: "SCAN-20260519-010"
topic_key: "FTC-OVER-LOCATION-DATA-BROKER-PRAC-2026"
topic_type: "enforcement"
topic_key_confidence: "high"
first_reported: 2026-05-08
last_updated: 2026-05-19
status_history: []
---

# FTC v. Kochava: Settlement Bars Sale of Sensitive Location Data Without Consent

**Jurisdiction:** Federal | **Category:** Privacy | **Date:** 2026-05-08

## Summary [HIGH confidence]

The Federal Trade Commission has obtained a stipulated final order prohibiting data broker Kochava Inc. and its subsidiary Collective Data Solutions (CDS) from selling, sharing, or disclosing consumers' precise geolocation data associated with sensitive locations — including medical facilities, places of worship, domestic violence shelters, and schools — unless they first secure affirmative express consent. Filed May 4, 2026 in the U.S. District Court for the District of Idaho (Case No. 2:22-cv-00377-BLW), the order resolves an FTC lawsuit originally filed in August 2022 and represents the agency's most detailed consent order to date on location data broker practices. No monetary civil penalty was assessed; Kochava reportedly disclosed that its financial condition precluded a monetary settlement.

## Key Facts [HIGH confidence]

- **Order filed May 4, 2026:** The FTC filed a proposed stipulated order in the District of Idaho on May 4, 2026; Kochava signed on March 2, 2026. The Commission approved the order 2-0. The order terminates in ten years ([FTC press release](https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-ban-kochava-subsidiary-selling-sensitive-location-data-settle-charges-they-sold-location-data); [FTC case page](https://www.ftc.gov/legal-library/browse/cases-proceedings/ftc-v-kochava-inc)).

- **Original complaint:** The FTC's August 2022 complaint alleged Kochava sold customized geolocation data feeds derived from more than 61 million unique mobile device IDs in a single week, enabling purchasers to track individuals to reproductive health clinics, houses of worship, homeless shelters, domestic violence shelters, and addiction recovery facilities ([FTC 2022 press release](https://www.ftc.gov/news-events/news/press-releases/2022/08/ftc-sues-kochava-selling-data-tracks-people-reproductive-health-clinics-places-worship-other)).

- **Legal basis:** The FTC alleged violations of Section 5(a) of the FTC Act, 15 U.S.C. § 45(a), characterizing the sale of sensitive location data without consumer consent as an unfair trade practice. No HIPAA or sector-specific statute was relied upon — the agency proceeded entirely on general unfairness authority.

- **Prohibited practices under the order:** Kochava and CDS are barred from selling, licensing, transferring, sharing, or disclosing "sensitive location data" — defined as precise location data associated with medical facilities, religious organizations, sites predominantly providing education or childcare to minors, homeless shelters, domestic violence shelters, and military or federal law enforcement installations — without affirmative express consumer consent ([proposed stipulated order, p. 2–5](https://www.ftc.gov/system/files/ftc_gov/pdf/ftc_v._kochava_-_proposed_stipulated_order.pdf)).

- **Required compliance programs:** The order mandates: (1) a written Sensitive Location Data Program including quarterly accuracy assessments; (2) a Supplier Assessment Program verifying upstream data sources obtained valid consumer consent; (3) a data retention schedule with mandatory deletion or de-identification of historical sensitive location data collected without consent; (4) a consumer-facing mechanism allowing individuals to request the identity of data recipients and to withdraw consent and request deletion ([White & Case client alert](https://www.whitecase.com/insight-alert/ftc-settles-data-broker-kochava-over-sale-sensitive-location-data-key-takeaways)).

- **No monetary penalty:** Kochava indicated that its financial condition precluded a monetary settlement. Critics at the Citizens Lab Policy blog have characterized the settlement as inadequate, noting it does not restrict Kochava's sale of other sensitive consumer data (e.g., app usage profiles and personal characteristics) ([CLP Blog](https://clpblog.citizen.org/the-ftcs-inadequate-kochava-proposed-privacy-settlement/)).

- **Case timeline:** Original complaint filed August 29, 2022; amended complaint filed June 5, 2023; second amended complaint filed July 15, 2024; settlement announced March 2026 and filed May 4, 2026 ([FTC case page](https://www.ftc.gov/legal-library/browse/cases-proceedings/ftc-v-kochava-inc)).

## Regulatory Context [HIGH confidence]

The Kochava settlement is the latest in a sustained FTC enforcement campaign against location data brokers:

- **X-Mode Social / Outlogic (January 2024):** First-ever FTC prohibition on the sale of sensitive location data against a data broker; order required deletion of historical sensitive data and implementation of supplier vetting requirements ([FTC press release, Jan. 9, 2024](https://www.ftc.gov/news-events/news/press-releases/2024/01/ftc-order-prohibits-data-broker-x-mode-social-outlogic-selling-sensitive-location-data)).

- **InMarket Media (January 2024):** Ban on selling or licensing precise location data; order finalized April 2024 ([FTC press release, Jan. 2024](https://www.ftc.gov/news-events/news/press-releases/2024/01/ftc-order-will-ban-inmarket-selling-precise-consumer-location-data)).

- **Gravy Analytics / Venntel and Mobilewalla:** Additional orders in the same campaign. The FTC's March 2024 Tech at FTC blog post confirmed the agency views mass location data collection — even absent a specific statutory hook — as presumptively unfair when tied to sensitive locations ([FTC Tech at FTC Blog, March 2024](https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/2024/03/ftc-cracks-down-mass-data-collectors-closer-look-avast-x-mode-inmarket)).

The Kochava order adds a significant doctrinal refinement: the requirement that consent be linked to a service "directly requested by the consumer" forecloses consent obtained through opaque third-party SDKs or bundled app permissions.

## Critical Analysis [MEDIUM confidence]

**Scope limitations:** The order's definition of "sensitive location data" is narrower than the FTC originally signaled. Commentators at MLex reported that the final settlement narrowed the sensitive location categories compared to earlier proposed definitions, and the CLP Blog noted the order leaves Kochava free to continue selling behavioral, demographic, and app-level data without the same consent constraints.

**Absence of monetary relief:** The lack of a civil penalty distinguishes this action from contemporaneous FTC enforcement (e.g., Avast, fined $16.5 million in 2024). Without a financial deterrent, the order's deterrence value is primarily reputational and structural.

**Political context:** The 2-0 vote reflects the current two-member Commission operating without a full quorum following the removal of two Democratic commissioners in early 2025. The Kochava order and its narrow consent framework may reflect the compromises needed to achieve consensus in this environment.

## Action Items

- **Location data brokers:** Audit all data products for coverage of the six sensitive location categories defined in the order. Implement supplier assessment programs to verify upstream consent validity. Establish deletion schedules for historical sensitive location data lacking documented consent.

- **App publishers and SDK users:** Review data-sharing agreements with downstream brokers. If SDK-level consent was used to authorize third-party location data sales, assess whether that consent qualifies as "affirmative express consent" for a service "directly requested by the consumer" under the Kochava framework.

- **Buyers of location data:** Require contractual representations from data suppliers that sensitive location data has been filtered and that upstream consent complies with the Kochava standard. Implement due-diligence review of supplier consent mechanisms.

- **All companies with ad-tech location data pipelines:** Monitor the 60-day public comment period on the proposed order (opened May 4, 2026) for any FTC modifications before the order is finalized.

## Related Reports

- [reports/privacy/enforcement-actions/federal-ftc-kochava-location-data-2026-05-08.md](reports/privacy/enforcement-actions/federal-ftc-kochava-location-data-2026-05-08.md) -- Prior report on the same FTC v. Kochava settlement filed under finding SCAN-20260508-005; contains overlapping analysis of the order's terms.
- [reports/privacy/enforcement-actions/california-ag-location-data-sweep-2025-03-10.md](reports/privacy/enforcement-actions/california-ag-location-data-sweep-2025-03-10.md) -- California AG's parallel CCPA investigative sweep targeting location data brokers, showing concurrent state-level enforcement pressure on the same industry.
- [reports/privacy/enforcement-actions/ftc-match-okcupid-clarifai-enforcement-2026-04-07.md](reports/privacy/enforcement-actions/ftc-match-okcupid-clarifai-enforcement-2026-04-07.md) -- Recent FTC enforcement action against Match Group and OkCupid for sharing user data without consent, illustrating the FTC's broader data-without-consent enforcement posture.
- [reports/privacy/state-comprehensive-laws/virginia-sb338-vcdpa-geolocation-ban-2026-04-19.md](reports/privacy/state-comprehensive-laws/virginia-sb338-vcdpa-geolocation-ban-2026-04-19.md) -- Virginia VCDPA amendment imposing new restrictions on geolocation data collection, reflecting convergent legislative and regulatory action on location privacy.

## Sources

1. [FTC Press Release: FTC to Ban Kochava and Subsidiary from Selling Sensitive Location Data (May 4, 2026)](https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-ban-kochava-subsidiary-selling-sensitive-location-data-settle-charges-they-sold-location-data) -- Official FTC announcement of the settlement; primary source for order terms, timeline, and vote count.
2. [FTC Case Page: FTC v. Kochava, Inc.](https://www.ftc.gov/legal-library/browse/cases-proceedings/ftc-v-kochava-inc) -- Complete case docket with all filings and timeline items; primary official source for case history.
3. [Proposed Stipulated Order (PDF) — Case 2:22-cv-00377-BLW (May 4, 2026)](https://www.ftc.gov/system/files/ftc_gov/pdf/ftc_v._kochava_-_proposed_stipulated_order.pdf) -- Full text of the proposed order; authoritative source for prohibited practices, sensitive location definitions, and compliance program requirements.
4. [FTC Press Release: FTC Sues Kochava (August 2022)](https://www.ftc.gov/news-events/news/press-releases/2022/08/ftc-sues-kochava-selling-data-tracks-people-reproductive-health-clinics-places-worship-other) -- Original 2022 complaint announcement; source for factual allegations regarding 61 million device IDs and sensitive location types.
5. [White & Case Client Alert: FTC Settles with Data Broker Kochava — Key Takeaways for Businesses](https://www.whitecase.com/insight-alert/ftc-settles-data-broker-kochava-over-sale-sensitive-location-data-key-takeaways) -- Law firm analysis of business implications, compliance program requirements, and supplier assessment obligations.
6. [Citizens Lab Policy Blog: The FTC's Inadequate Kochava Proposed Privacy Settlement](https://clpblog.citizen.org/the-ftcs-inadequate-kochava-proposed-privacy-settlement/) -- Critical analysis of settlement scope limitations; source for claim that order excludes non-location sensitive data and for Kochava's stated financial inability to pay civil penalties.
7. [FTC Press Release: FTC Order Prohibits X-Mode Social / Outlogic from Selling Sensitive Location Data (January 2024)](https://www.ftc.gov/news-events/news/press-releases/2024/01/ftc-order-prohibits-data-broker-x-mode-social-outlogic-selling-sensitive-location-data) -- Predecessor enforcement action; establishes regulatory context for Kochava settlement.
8. [FTC Press Release: FTC Order Bans InMarket from Selling Precise Consumer Location Data (January 2024)](https://www.ftc.gov/news-events/news/press-releases/2024/01/ftc-order-will-ban-inmarket-selling-precise-consumer-location-data) -- Second parallel enforcement action in January 2024 location data broker campaign.
9. [FTC Tech at FTC Blog: FTC Cracks Down on Mass Data Collectors — Avast, X-Mode, InMarket (March 2024)](https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/2024/03/ftc-cracks-down-mass-data-collectors-closer-look-avast-x-mode-inmarket) -- FTC policy blog confirming unfairness theory for mass location data collection; background on the enforcement campaign.
10. [MLex: Kochava Settlement With US FTC Narrows Definition of Sensitive Locations](https://www.mlex.com/mlex/articles/2473969/kochava-settlement-with-us-ftc-narrows-definition-of-sensitive-locations) -- Specialist regulatory reporting on the narrowing of sensitive location definitions in the final order compared to earlier proposals.
11. [National Law Review: FTC Bars Kochava From Selling Sensitive Location Data](https://natlawreview.com/article/ftc-bars-kochava-selling-sensitive-location-data) -- Legal news summary confirming order terms and consent requirements.
12. [AdExchanger: The FTC Bars Kochava From Selling Sensitive Data Without Consent](https://www.adexchanger.com/privacy/the-ftc-bars-kochava-from-selling-sensitive-data-without-consent/) -- Industry publication coverage of ad-tech implications; confirms no monetary penalty.
