---
title: "ICE Domestic Surveillance Expansion: Social Media Tracking, Spyware, and Data Broker Contracts Draw Congressional and Civil Liberties Scrutiny"
date: 2026-05-04
jurisdiction: "Federal"
category: "privacy"
development_type: "other"
finding_id: "SCAN-20260504-039"
topic_key: "federal-e719f438-2026"
topic_type: "guidance"
first_reported: 2026-05-01
last_updated: 2026-05-04
status_history: []
cluster: "ICE Domestic Surveillance Expansion: Data Broker Contracts, Spyware, and Congressional Scrutiny (2026)"
cluster_slug: "ice-domestic-surveillance-expansion-2026"
---

# ICE Domestic Surveillance Expansion: Social Media Tracking, Spyware, and Data Broker Contracts Draw Congressional and Civil Liberties Scrutiny

**Jurisdiction:** Federal | **Category:** Privacy | **Date:** 2026-05-04

## Executive Summary [MEDIUM confidence]

The U.S. Immigration and Customs Enforcement has substantially expanded its domestic surveillance capabilities through a network of vendor contracts covering facial recognition, commercial location data, social media monitoring, phone forensics, and military-grade spyware. The tools in aggregate enable ICE agents to determine individuals' social media accounts, home addresses, and employment information without judicial warrants in most cases. In April 2026, ICE's acting director formally acknowledged the agency's use of Graphite — an Israeli-made "zero-click" spyware — to intercept encrypted communications, the first official confirmation of the tool's deployment inside the United States. Congress has demanded answers, the DHS Inspector General has launched a formal audit of ICE biometric and data collection practices, and civil liberties organizations argue the surveillance apparatus now extends well beyond immigration enforcement to monitor U.S. citizens and constitutionally protected activities. DHS has declined to disclose specific operational methods, asserting its practices comply with the U.S. Constitution.

## Background [MEDIUM confidence]

ICE's surveillance mandate derives primarily from the [Homeland Security Act of 2002](https://www.dhs.gov/sites/default/files/publications/hr_5005_enr.pdf) and the [Immigration and Nationality Act](https://www.uscis.gov/laws-and-policy/legislation/immigration-and-nationality-act), which authorize immigration enforcement and border security operations. For decades, ICE conducted enforcement primarily through traditional investigative techniques. Beginning in the mid-2010s, the agency began acquiring commercial surveillance tools; the pace accelerated sharply following the Trump administration's mass deportation initiative launched in January 2025.

The reconciliation legislation enacted in July 2025 allocated DHS approximately $169 billion across six components — and roughly $191 billion including Secretary-directed funds — per [Congressional Research Service Report R48704](https://www.congress.gov/crs-product/R48704). ICE alone received approximately [$75 billion](https://www.kaine.senate.gov/press-releases/warner-kaine-demand-investigation-into-dhs-use-of-surveillance-technology) — more than the FBI's total budget. This funding surge enabled a rapid expansion of commercial vendor contracts for surveillance technology.

The legal framework governing government use of commercially acquired location data and surveillance tools remains unsettled. The Supreme Court's [Carpenter v. United States (2018)](https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf) held that warrantless collection of seven or more days of historical cell-site location information violates the Fourth Amendment. However, the government has taken the position that purchase of commercial location data from brokers — as distinct from direct compulsion of carriers — falls outside Carpenter's scope. This interpretation is contested by privacy advocates and a growing number of lawmakers.

Prior DHS Inspector General investigations found that [CBP, ICE, and the Secret Service all violated federal law through warrantless purchase and use of location data](https://cyberscoop.com/dhs-ig-audit-ice-obim-biometric-data-privacy-facial-recognition/), including employees sharing account credentials for phone-tracking databases and supervisors failing to maintain audit logs.

## Detailed Analysis [MEDIUM confidence]

### The Surveillance Tool Ecosystem

ICE's surveillance capabilities are deployed through a constellation of vendor relationships, each covering distinct data categories:

**Palantir — ImmigrationOS ($30 million contract):** [Palantir Technologies was awarded a $30 million contract](https://immpolicytracking.org/policies/reported-palantir-awarded-30-million-to-build-immigrationos-surveillance-platform-for-ice/) to build "ImmigrationOS," an integrated enforcement platform designed to: (1) identify and locate individuals prioritized for removal; (2) track self-deportations with near-real-time visibility; and (3) optimize deportation logistics. Palantir's ELITE tool, which integrates with ImmigrationOS, creates maps of potential enforcement targets and assigns "confidence scores" to addresses. The platform draws on data from Thomson Reuters' CLEAR database, government agency records, and other sources to construct individual profiles.

**Thomson Reuters — CLEAR Platform ($22.8 million contract):** ICE relies heavily on Thomson Reuters' Consolidated Lead Evaluation and Reporting (CLEAR) database. Per a [statement of work document reviewed by reporters](https://www.404media.co/how-thomson-reuters-powers-ice-and-palantir/), CLEAR provides ICE with "any information that identifies the possible location of the target and changes in the target's identifiers, such as addresses, phone numbers, email addresses, user names, new aliases, date of birth changes, SSN changes, utility changes, arrests, credit checks, death registry information, employment changes, insurance changes and affiliated organizations." The $22.8 million contract is scheduled to expire May 31, 2026. [Over 200 Thomson Reuters employees signed an internal letter](https://www.npr.org/2026/04/21/nx-s1-5786915/ice-immigration-enforcement-data-thomson-reuters) opposing the contract.

**Penlink — Webloc and Tangles ($5 million):** [ICE paid approximately $5 million](https://www.eff.org/deeplinks/2026/01/ice-going-surveillance-shopping-spree) for Penlink's Webloc (commercial location data aggregation) and Tangles (social media surveillance combining web scraping with API access). According to an internal ICE legal analysis, commercial location data acquired through Webloc can be queried without a warrant — a legal interpretation that Senator Ron Wyden and ACLU attorneys have publicly disputed.

**Clearview AI ($10 million contract):** ICE holds a [contract valued at approximately $10 million with Clearview AI](https://www.eff.org/deeplinks/2026/01/ice-going-surveillance-shopping-spree) for facial recognition services. Clearview's database contains billions of facial images scraped from the public internet.

**Mobile Fortify (Biometric Field App):** [ICE agents have used Mobile Fortify more than 100,000 times](https://www.npr.org/2026/03/04/nx-s1-5717031/ice-dhs-immigrants-surveillance-confrontation-deportation-mobile-fortify), according to a lawsuit filed by Illinois and Chicago in January 2026. The app enables field agents to upload face scans and fingerprints matched against a database of over 200 million images from DHS, FBI, and State Department records.

**Flock Safety (License Plate Readers):** [ICE has persuaded local law enforcement to run queries on its behalf](https://www.eff.org/deeplinks/2026/01/ice-going-surveillance-shopping-spree) through Flock Safety's network of over 40,000 automated license plate recognition (ALPR) scanners across the United States.

### Paragon Graphite Spyware: A Critical Disclosure

The most significant recent development is ICE's acknowledgment of Graphite deployment. In an [April 1, 2026 letter to congressional oversight members](https://www.npr.org/2026/04/07/nx-s1-5776799/ice-spyware-privacy), ICE Acting Director Todd Lyons confirmed the agency is using Graphite — created by Israeli company Paragon Solutions — to intercept encrypted communications as part of fentanyl trafficking investigations.

Graphite employs "zero-click" technology, meaning it can compromise a target device and access encrypted messages without the user clicking any link. The agency initially signed a [$2 million contract with Paragon Solutions](https://immpolicytracking.org/policies/ice-to-gain-access-to-sophisticated-foreign-made-spyware/) at the end of the Biden administration, which was paused and subsequently revived by the Trump administration.

Lyons' letter, described as a belated response to an October 2025 congressional inquiry, did not answer basic questions about who is being targeted, what legal authority ICE relies upon, or whether the spyware has been deployed against persons inside the United States. [WhatsApp disclosed in early 2025](https://www.npr.org/2026/04/07/nx-s1-5776799/ice-spyware-privacy) that approximately 90 journalists and civil society members in multiple countries had been targeted with Graphite.

Representative Summer Lee (D-PA), one of the October inquiry's authors, stated: "The response I received from ICE makes one thing clear. They are moving forward with invasive spyware technology inside the United States." The Electronic Frontier Foundation's Cooper Quintin noted that Lyons' response "doesn't rule out ICE using an administrative subpoena to deploy this malware against people living in the United States."

### Mission Creep: Surveillance Beyond Immigration Targets

[A March 2026 NPR investigation](https://www.npr.org/2026/03/04/nx-s1-5717031/ice-dhs-immigrants-surveillance-confrontation-deportation-mobile-fortify) documented DHS using facial recognition, biometric scanning, and social media monitoring to identify and investigate U.S. citizens — not merely immigration enforcement targets. The [American Immigration Council reported](https://www.americanimmigrationcouncil.org/blog/ice-ai-surveillance-tracking-americans/) that AI-powered enforcement originally confined to the southern border has expanded to target individuals across American cities.

Furthermore, ICE has [explicitly stated it intends to use surveillance capabilities against anti-ICE protesters](https://www.brennancenter.org/our-work/research-reports/ice-wants-go-after-dissenters-well-immigrants), labeling them "domestic terrorists." Minnesota contracts for Penlink tools [explicitly marketed the products for use at protests](https://www.americanimmigrationcouncil.org/blog/ice-ai-surveillance-tracking-americans/) and other First Amendment-protected gatherings.

ICE has also accessed [Medicaid records to obtain home addresses](https://www.npr.org/2026/03/04/nx-s1-5717031/ice-dhs-immigrants-surveillance-confrontation-deportation-mobile-fortify) for enforcement purposes — data shared under interagency agreements — raising questions about the scope of authorized data sharing between health agencies and immigration enforcement.

## Impact Assessment [MEDIUM confidence]

### U.S. Citizens and Lawful Residents

The most significant impact is on non-immigration-related individuals whose data is swept into ICE databases. Commercial location data, facial recognition records, and social media monitoring tools do not distinguish between U.S. citizens and undocumented individuals. Any person whose face appears in a publicly accessible image, whose phone emits location signals, or whose social media posts are publicly visible may be profiled by ICE systems without a warrant, notification, or recourse.

### Civil Society and First Amendment Activities

ICE's stated intent to monitor anti-immigration protesters — and its procurement of tools marketed for protest surveillance — creates a documented chilling effect on constitutionally protected speech and assembly. Organizations involved in advocacy, journalism, legal aid, and community organizing should assume their members and activities may be subject to surveillance.

### Data Broker Industry

ICE contracts validate a business model in which commercial data brokers aggregate sensitive personal information and sell it to government agencies, effectively enabling warrantless surveillance at scale. This model faces increasing scrutiny from Congress and state attorneys general. California's 2025 investigation into the location data industry ([SCAN-20250313-014](reports/privacy/enforcement-actions/california-ag-location-data-sweep-2025-03-13.md)) reflects growing state-level pushback. Federal legislation to close the commercial data purchase loophole remains stalled.

### Congressional and Oversight Response

Senators Warner and Kaine sent a letter in January 2026 demanding a DHS IG investigation. [Following that pressure](https://www.kaine.senate.gov/press-releases/following-warner-kaine-pressure-dhs-inspector-general-launches-audit-of-dhs-data-privacy-abuses), Inspector General Joseph Cuffari launched a formal audit of ICE and the Office of Biometric Identity Management (OBIM) focusing on: how DHS collects and retains biometric and personally identifiable information; whether sharing and security practices comply with law; and whether privacy policies adequately protect individuals. The IG separately reported that [DHS has "systematically obstructed"](https://cyberscoop.com/dhs-ig-audit-ice-obim-biometric-data-privacy-facial-recognition/) the office's audit work by blocking access to records and systems.

In March 2026, Senator Wyden [sent a separate letter to the DHS IG](https://www.wyden.senate.gov/imo/media/doc/wyden_letter_to_dhs_oig_on_ice_purchasing_location_datapdf.pdf) specifically requesting examination of ICE's warrantless purchase of location data through Penlink. A bipartisan group of [70 lawmakers demanded a probe into ICE's data purchases](https://www.theregister.com/2026/03/03/us_lawmakers_ice_data_purchases).

## Action Items

- **Conduct employee data-use audits:** Organizations operating in sectors with ICE data sharing agreements (healthcare, social services, financial institutions) should audit whether their data is flowing to ICE through Medicaid records or other interagency channels and assess exposure under applicable privacy laws.
- **Review protest and advocacy security posture:** Organizations engaged in immigration-related advocacy, legal representation, or journalism should evaluate whether their communications security practices are adequate given confirmed use of zero-click spyware domestically.
- **Monitor DHS IG audit outcomes:** The DHS Inspector General audit of ICE and OBIM is ongoing. Publication of findings — if the audit is completed and released — will provide the most authoritative assessment of legal compliance and may trigger legislative or regulatory responses.
- **Track Thomson Reuters CLEAR contract renewal:** The $22.8 million CLEAR contract expires May 31, 2026. Contract renewal or non-renewal will signal the administration's direction on commercial data broker reliance and may affect other vendor relationships.
- **Track Fourth Amendment litigation:** Civil liberties organizations including the ACLU and EFF have signaled litigation interest. Court challenges to warrantless commercial data purchases and Graphite deployment inside the U.S. may produce controlling precedent on government-broker surveillance arrangements.
- **Follow federal privacy legislation:** Bills to close the commercial data purchase loophole — including proposals modeled on Senator Wyden's prior legislative efforts — remain the most likely vehicle for structural reform. Track markup schedules in Senate Commerce and House Judiciary.

## Related Reports

- [reports/privacy/federal-legislation/fisa-section-702-renewal-2026-04-13.md](reports/privacy/federal-legislation/fisa-section-702-renewal-2026-04-13.md) — FISA Section 702 covers foreign intelligence surveillance authority; the Fourth Amendment warrant debate there parallels ICE's arguments for warrantless commercial data purchases domestically.
- [reports/privacy/enforcement-actions/california-ag-location-data-sweep-2025-03-13.md](reports/privacy/enforcement-actions/california-ag-location-data-sweep-2025-03-13.md) — California's CCPA investigative sweep into the location data industry directly implicates the same data broker vendors (including Penlink competitors) that supply ICE.
- [reports/privacy/federal-meta-smart-glasses-facial-recognition-coalition-2026-04-14.md](reports/privacy/federal-meta-smart-glasses-facial-recognition-coalition-2026-04-14.md) — Federal facial recognition policy debate; ICE's use of Clearview AI and Mobile Fortify is part of the same broader facial recognition expansion that the civil society coalition addressed.
- [reports/privacy/federal-legislation/federal-wyden-fisa702-reform-democrats-2026-04-19.md](reports/privacy/federal-legislation/federal-wyden-fisa702-reform-democrats-2026-04-19.md) — Senator Wyden's FISA reform effort is led by the same legislator demanding investigation of ICE's location data purchases; the warrantless surveillance concerns overlap substantively.

## Sources

1. [ICE acknowledges it is using powerful spyware — NPR (April 7, 2026)](https://www.npr.org/2026/04/07/nx-s1-5776799/ice-spyware-privacy) — Primary reporting on ICE's formal confirmation of Graphite spyware deployment; includes congressional responses and EFF analysis.
2. [ICE has spun a massive surveillance web — NPR (March 4, 2026)](https://www.npr.org/2026/03/04/nx-s1-5717031/ice-dhs-immigrants-surveillance-confrontation-deportation-mobile-fortify) — Investigative piece on Mobile Fortify, biometric surveillance, and tracking of U.S. citizens.
3. [ICE Is Going on a Surveillance Shopping Spree — EFF (January 2026)](https://www.eff.org/deeplinks/2026/01/ice-going-surveillance-shopping-spree) — Detailed breakdown of ICE vendor contracts: Penlink, Clearview AI, Flock Safety, and others.
4. [Warner, Kaine Demand Investigation into DHS Use of Surveillance Technology — Sen. Kaine (January 2026)](https://www.kaine.senate.gov/press-releases/warner-kaine-demand-investigation-into-dhs-use-of-surveillance-technology) — Official Senate press release with details on DHS surveillance technology contracts and Fourth Amendment concerns.
5. [Following Warner, Kaine Pressure, DHS IG Launches Audit — Sen. Kaine (February 2026)](https://www.kaine.senate.gov/press-releases/following-warner-kaine-pressure-dhs-inspector-general-launches-audit-of-dhs-data-privacy-abuses) — Official announcement of DHS Inspector General audit scope and objectives.
6. [Palantir granted $30 million to build ImmigrationOS — Immigration Policy Tracking Project](https://immpolicytracking.org/policies/reported-palantir-awarded-30-million-to-build-immigrationos-surveillance-platform-for-ice/) — Contract details and platform functionality for Palantir's ImmigrationOS.
7. [ICE contracts with Paragon to gain access to sophisticated spyware — Immigration Policy Tracking Project](https://immpolicytracking.org/policies/ice-to-gain-access-to-sophisticated-foreign-made-spyware/) — Contract details for Paragon Graphite spyware.
8. [How Thomson Reuters Powers ICE and Palantir — 404 Media](https://www.404media.co/how-thomson-reuters-powers-ice-and-palantir/) — Analysis of CLEAR platform capabilities and integration with Palantir's enforcement tools; includes statement of work excerpts.
9. [She raised concerns about her company's contracts with ICE. Then she lost her job — NPR (April 21, 2026)](https://www.npr.org/2026/04/21/nx-s1-5786915/ice-immigration-enforcement-data-thomson-reuters) — Reporting on Thomson Reuters employee opposition and contract renewal status.
10. [Mission Creep: AI Surveillance at DHS Crosses Dangerous Line Into Tracking Americans — American Immigration Council](https://www.americanimmigrationcouncil.org/blog/ice-ai-surveillance-tracking-americans/) — Analysis of AI surveillance expansion beyond immigration targets to U.S. citizens.
11. [ICE Wants to Go After Dissenters as well as Immigrants — Brennan Center for Justice](https://www.brennancenter.org/our-work/research-reports/ice-wants-go-after-dissenters-well-immigrants) — Analysis of ICE's stated intent to use surveillance against anti-deportation protesters.
12. [DHS privacy probe will focus on biometric tracking by ICE, OBIM — CyberScoop](https://cyberscoop.com/dhs-ig-audit-ice-obim-biometric-data-privacy-facial-recognition/) — Details on DHS IG audit scope, obstruction findings, and prior privacy violations.
13. [70 US lawmakers demand probe into ICE's data purchases — The Register (March 3, 2026)](https://www.theregister.com/2026/03/03/us_lawmakers_ice_data_purchases) — Bipartisan congressional demand for investigation into commercial data purchases.
14. [Sen. Wyden letter to DHS IG on ICE purchasing location data (March 3, 2026)](https://www.wyden.senate.gov/imo/media/doc/wyden_letter_to_dhs_oig_on_ice_purchasing_location_datapdf.pdf) — Official letter demanding IG examine ICE's warrantless commercial location data purchases.
15. [DHS is buying access to real-time location data — Prism Reports (April 29, 2026)](https://prismreports.org/2026/04/29/dhs-surveillance-location-data-penlink-plx/) — Most recent reporting on DHS real-time location data acquisition via Penlink.
16. [Reps. Lee, Brown, Ansari Demand Answers from DHS on Use of Foreign Spyware — Congresswoman Summer Lee](https://summerlee.house.gov/newsroom/press-releases/reps-lee-brown-ansari-demand-answers-from-dhs-on-use-of-foreign-spyware-by-ice) — Congressional response to Graphite acknowledgment; quotes from Rep. Lee.
