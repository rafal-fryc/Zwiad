---
title: "Texas AG Ken Paxton Sues Allstate and Arity for Unlawful Telematics Data Collection: First TDPSA Enforcement Action"
date: 2025-01-20
jurisdiction: "Texas"
category: "privacy"
development_type: "enforcement"
finding_id: "SCAN-20250120-007"
topic_key: "TXAG-ALLSTATE-2025"
topic_type: "enforcement"
first_reported: 2025-01-20
last_updated: 2026-04-22
status_history:
  - "2026-04-22: Corrected TDPSA § 541.001 sensitive data subsection from (29) to (23) per enrolled bill; corrected data broker penalty to $100/day plus unpaid fees capped at $10,000, citing § 509.008; corrected data broker applicability description to reflect 'principal source of revenue' definition without erroneous 50,000-person threshold; replaced regulatoryoversight.com source with Goodwin law firm alert."
cluster: "Texas AG v. Allstate/Arity: TDPSA Enforcement Action"
cluster_slug: "texas-ag-allstate-arity-tdpsa-enforcement"
---

# Texas AG Ken Paxton Sues Allstate and Arity for Unlawful Telematics Data Collection: First TDPSA Enforcement Action

**Jurisdiction:** Texas | **Category:** privacy | **Date:** 2025-01-20

> **Editorial Note:** This report covers the initial filing and legal framework of this enforcement action. A more comprehensive and updated report — including case developments through April 2026 — exists at [reports/privacy/enforcement-actions/texas-allstate-arity-tdpsa-enforcement-2025-01-15.md](../../../reports/privacy/enforcement-actions/texas-allstate-arity-tdpsa-enforcement-2025-01-15.md). That report should be treated as the authoritative source for ongoing developments. This report is retained as a companion memo focused on the original legal framework and industry context.

## Executive Summary [HIGH confidence]

On January 13, 2025, Texas Attorney General Ken Paxton filed the first-ever enforcement action under a U.S. state comprehensive consumer data privacy law, suing Allstate Corporation and five related entities — including three Arity-branded data analytics subsidiaries — for unlawfully collecting, using, and selling precise geolocation and driving behavior data from more than 45 million Americans without their knowledge or consent. The [complaint](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-allstate-and-arity-unlawfully-collecting-using-and-selling-over-45), filed in the District Court of Montgomery County, Texas, alleges violations of the [Texas Data Privacy and Security Act (TDPSA)](https://capitol.texas.gov/tlodocs/88R/billtext/html/HB00004F.htm) (Tex. Bus. & Com. Code Ch. 541), the Texas Data Broker Law (Tex. Bus. & Com. Code Ch. 509), and the Texas Insurance Code's prohibition on unfair and deceptive trade practices. The State alleges that Allstate's subsidiary Arity secretly embedded software development kits (SDKs) in popular consumer apps — including Life360, GasBuddy, Fuel Rewards, and Routely — to continuously harvest location and driving data, then sold that data to insurers to adjust policy rates. Texas seeks more than $1 million in civil penalties plus injunctive relief and data deletion.

## Background [HIGH confidence]

### The Texas Data Privacy and Security Act

Texas enacted HB 4, the Texas Data Privacy and Security Act, in the 88th Legislative Session. The statute became effective July 1, 2024, establishing comprehensive privacy obligations for businesses that process personal data of Texas residents. Key provisions include requirements to provide a clear and accessible privacy notice, obtain affirmative consent before processing sensitive data (including precise geolocation), honor consumer opt-out rights, and observe data minimization principles. Enforcement authority rests exclusively with the [Texas Attorney General](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/consumer-privacy-rights/texas-data-privacy-and-security-act); there is no private right of action under the TDPSA.

Before filing suit, the TDPSA requires the AG to provide a 30-day written notice of violation and an opportunity to cure. Companies that fail to cure, or that breach a written cure commitment, are liable for civil penalties of up to $7,500 per violation. The [full text of HB 4](https://capitol.texas.gov/tlodocs/88R/billtext/html/HB00004F.htm) is available via the Texas Legislature Online.

### The Texas Data Broker Law

Texas Business & Commerce Code Chapter 509 — commonly called the Texas Data Broker Law — requires business entities whose principal source of revenue derives from collecting, processing, or transferring personal data that the entity did not collect directly from the individual to register with the Texas Secretary of State by March 1 of each year and pay a $300 annual registration fee. The [Texas Secretary of State's data broker portal](https://www.sos.state.tx.us/statdoc/data-brokers.shtml) maintains the registry. Failure to register is a standalone violation subject to civil penalties. The civil penalty for non-compliance is $100 per day in violation plus the amount of any unpaid registration fees, capped at $10,000 assessed against the same data broker in any 12-month period (Tex. Bus. & Com. Code [§ 509.008](https://texas.public.law/statutes/tex._bus._and_com._code_section_509.008)).

> **Note on applicability thresholds:** At the time of the Allstate filing (January 2025), the statute (enacted as SB 2105, 88th Legislature) applied to entities meeting the "principal source of revenue" definition — there was no standalone numerical headcount threshold in the definition itself. A subsequent 2025 amendment (SB 2121, 89th Legislature, eff. September 1, 2025) added explicit applicability thresholds including a 50,000-individual prong and revised the "principal source" language. The Allstate enforcement is governed by the pre-amendment version.

### Texas AG Enforcement Posture

The AG's Office began preparing for TDPSA enforcement well before the Allstate suit. In June 2024, the AG [announced a dedicated Tech and Privacy enforcement team](https://www.goodwinlaw.com/en/insights/publications/2024/06/alerts-practices-dpc-texas-new-privacy-law-goes-into-effect-enforcement) within the Consumer Protection Division — a team of roughly 20 staff, making it one of the largest state-level privacy enforcement operations in the country — signaling intent to bring enforcement actions promptly after the law took effect. AG Paxton also [notified over 100 companies](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-notifies-over-100-companies-their-apparent-failure-comply-texas-data) of apparent failure to register under the Texas Data Broker Law, establishing a track record of proactive enforcement across multiple statutes.

### The Telematics Data Ecosystem

Telematics — the collection of vehicle and driving behavior data using GPS, accelerometers, and mobile sensors — has become a major data economy in the insurance industry. Insurers use driving data to offer usage-based insurance (UBI) programs, price policies, and assess risk. When telematics data is gathered through dedicated opt-in programs (e.g., Progressive Snapshot), consumer consent is typically clear. The Allstate/Arity model, by contrast, involved paying third-party app developers to embed an Arity SDK that collected data from users of unrelated consumer apps, without those users' knowledge that their driving behavior was being captured for insurance purposes.

## Detailed Analysis [HIGH confidence]

### The Alleged Data Collection Scheme

According to the [Texas AG press release](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-allstate-and-arity-unlawfully-collecting-using-and-selling-over-45) and the filed petition, Allstate established Arity as a telematics data subsidiary beginning around 2016. Arity developed an SDK that, when embedded in a third-party app, continuously harvested the mobile device user's latitude, longitude, speed, GPS timestamp, bearing, and altitude — typically at intervals of 15 seconds or less. Arity paid app developers millions of dollars to integrate the SDK and offered bonus incentives tied to growing the data set, creating what Allstate marketed as "the world's largest driving behavior database" covering trillions of miles of travel by over 45 million consumers.

The third-party apps involved — including [Life360](https://www.life360.com), GasBuddy, Fuel Rewards, and Routely — did not primarily market themselves as driving-behavior or insurance products. Users who downloaded these apps for family location sharing, finding cheap gas prices, or navigation had no reasonable basis to understand that their precise geolocation data was being simultaneously harvested, analyzed by an insurance company, and sold to other insurers to adjust their premiums or deny their coverage.

### TDPSA Violations Alleged

The complaint alleges the following TDPSA violations, each as assessed by [WilmerHale](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20250121-texas-ag-brings-first-ever-lawsuit-under-a-state-comprehensive-privacy-law) and [Vinson & Elkins](https://www.velaw.com/insights/texas-ag-targets-allstate-in-first-enforcement-of-texas-data-privacy-and-security-act/):

- **Failure to provide privacy notice.** The TDPSA requires controllers to provide a clear and accessible privacy notice that includes the categories of personal data processed, the purposes of processing, and information about consumer rights. The AG alleges that neither Allstate nor Arity disclosed in any accessible notice that data from third-party apps was being collected, aggregated into a driving behavior database, and sold to insurers.

- **Failure to obtain affirmative consent for sensitive data.** Precise geolocation data is classified as "sensitive data" under TDPSA § 541.001(23) of the enrolled bill. Processing sensitive data requires obtaining the consumer's affirmative, informed consent. The AG alleges that users of the third-party apps never consented — explicitly or implicitly — to their geolocation data being used for insurance risk assessment.

  > **Subsection numbering note:** The enrolled bill (HB 4, 88th Legislature) defines "sensitive data" at § 541.001(23). Some secondary sources cite § 541.001(29). The discrepancy likely reflects renumbering between the enrolled bill and the codified version in the Texas Business & Commerce Code. The official enrolled bill text at [capitol.texas.gov](https://capitol.texas.gov/tlodocs/88R/billtext/html/HB00004F.htm) controls as the authoritative enactment; practitioners should verify the current codified subsection number against the Texas statutes portal.

- **Lack of opt-out mechanism.** The TDPSA requires controllers to provide a clear and accessible means for consumers to opt out of the processing of their personal data for targeted advertising, sale, or profiling in furtherance of decisions that produce legal or similarly significant effects. Selling driving data to insurers who used it to price policies falls within this category, yet no opt-out mechanism was offered to app users.

### Data Broker Law Violation

The complaint separately alleges that Arity violated Texas Business & Commerce Code Chapter 509 by failing to register as a data broker before the March 1, 2024 deadline despite qualifying as one — Arity collected data from more than 45 million individuals through third-party app integrations rather than direct collection, and derived revenue by licensing that data to insurers. According to [CompliancePoint](https://www.compliancepoint.com/privacy/texas-ag-sues-allstate-insurance-for-privacy-law-violations/), Arity had still not registered at the time the lawsuit was filed. The civil penalty for data broker law violations is $100 per day in violation plus unpaid registration fees, capped at $10,000 assessed against the same data broker in any 12-month period ([Tex. Bus. & Com. Code § 509.008](https://texas.public.law/statutes/tex._bus._and_com._code_section_509.008)).

### Texas Insurance Code Claims

In addition to data privacy statutes, the complaint invokes the Texas Insurance Code's prohibitions on unfair and deceptive acts and practices in the business of insurance. This claim is significant because it connects the data collection scheme directly to harm in a regulated market — namely, consumers being subjected to higher premiums or coverage denials based on data they did not know was being collected. The [White & Case analysis](https://www.whitecase.com/insight-alert/texas-attorney-generals-landmark-privacy-lawsuit-signals-new-era-data-privacy) characterizes this as a novel theory that links data privacy violations to insurance market harm under a separate regulatory framework, potentially expanding the AG's enforcement tools and damages base.

### Penalties Sought

Per [Securiti's overview of the complaint](https://securiti.ai/texas-ag-complaint-v-allstate-corporation/), the State seeks:
- Civil penalties of up to **$7,500 per TDPSA violation** (post-cure-period)
- Civil penalties structured as **$100 per day plus unpaid registration fees, capped at $10,000 per 12-month period** of data broker registration non-compliance (§ 509.008)
- Penalties under the Texas Insurance Code (at least $17,000 per insurer misconduct violation according to some reports, though the exact Insurance Code penalty schedule varies by provision)
- Total penalties exceeding **$1 million**
- Injunctive relief requiring Allstate and Arity to cease the alleged practices and **delete unlawfully collected data**

### Wider Litigation Context

The Texas AG action was accompanied by a wave of private class action lawsuits. According to [Repairer Driven News](https://www.repairerdrivennews.com/2025/01/23/class-action-lawsuit-filed-against-allstate-for-allegedly-collecting-and-selling-data-without-consumer-consent/), a class action was filed in the Northern District of Illinois in January 2025, consolidating at least 15 separate suits. A court subsequently allowed drivers to proceed with claims under the laws of 20 states. BFA Law was appointed to the Plaintiffs' Executive Committee in April 2025. The parallel private litigation further amplifies compliance and financial risk for Allstate.

## Impact Assessment [MEDIUM confidence]

### Immediate Industry Implications

The Allstate/Arity case is the first time a state AG has invoked a state comprehensive consumer data privacy law to bring an enforcement action, according to [WilmerHale](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20250121-texas-ag-brings-first-ever-lawsuit-under-a-state-comprehensive-privacy-law). The precedent is particularly significant for industries that rely on embedded SDKs in third-party apps for data acquisition — including insurance (telematics), advertising technology, retail analytics, and financial services. The core allegation — that paying a third-party app developer to embed a data-collection SDK does not constitute obtaining consent from app users — is a broadly applicable theory that other AGs are likely to adopt.

### SDK and Third-Party Data Procurement Practices

The lawsuit specifically targets the practice of paying third-party app developers to collect data on behalf of a data buyer, without the end user having any awareness of or relationship with the ultimate data recipient. This is a widespread business model across adtech and data brokerage. Organizations that rely on this model — regardless of industry — should reassess whether their SDK deployment practices satisfy the consent and notice requirements of the 20+ comprehensive state privacy laws now in effect.

### Data Broker Registration Compliance

The data broker registration failure alleged here is striking given Arity's scale of 45 million data subjects. At the time of the filing (January 2025), Texas's data broker registration requirement applied to entities whose principal source of revenue derived from processing or transferring personal data not collected directly from individuals — a definition Arity plainly met. Companies operating in data brokerage or whose business models derive substantial revenue from third-party-sourced personal data should verify their registration status with the [Texas Secretary of State](https://www.sos.state.tx.us/statdoc/data-brokers.shtml) and monitor the revised 2025 applicability thresholds under SB 2121.

### Insurance Sector Telematics Programs

The Insurance Code claims put all insurers using telematics data on notice that covert data acquisition — even data acquired from a subsidiary or vendor rather than directly from policyholders — can constitute an unfair or deceptive act in the business of insurance. Insurers should audit the data sources feeding their underwriting models to verify that all data was collected with appropriate consumer notice and consent.

### Enforcement Outlook

The [Holland & Knight 2025 Texas privacy recap](https://www.hklaw.com/en/insights/publications/2026/02/privacy-and-cybersecurity-legislation-in-texas) confirms that the Allstate suit opened a broader enforcement campaign: in 2025, the Texas AG brought additional suits and launched investigations under the TDPSA and the SCOPE Act (children's online privacy), focusing on geolocation data, AI, and automated content recognition. The AG's pattern suggests sustained, multi-statute enforcement rather than a one-time action.

## Action Items

- **SDK-reliant data programs**: Conduct an immediate audit of any SDK integrations in third-party apps that capture consumer location, movement, or behavioral data on your behalf. Verify that end users of those apps receive conspicuous notice and provide affirmative consent to the data collection before it is used for your business purposes.
- **Sensitive data consent**: Review whether your organization processes precise geolocation data of Texas residents. Under the TDPSA, this is sensitive data (§ 541.001(23) of the enrolled bill) requiring opt-in affirmative consent — not merely a privacy notice or a general terms-of-service disclosure.
- **Texas data broker registration**: If your business derives revenue from processing or transferring personal data that you did not collect directly from the individuals involved — and this constitutes a principal source of your revenue — confirm registration with the Texas Secretary of State by March 1 each year. Review the [data broker registration FAQ](https://www.sos.state.tx.us/statdoc/faqs4000.shtml). Also verify applicability under the revised 2025 thresholds (SB 2121) if your business was formed or restructured after September 1, 2025.
- **Insurance sector telematics review**: If you are an insurer or insurer-affiliated entity using driving behavior or telematics data in underwriting, audit the data provenance chain to confirm that consumer notice and consent requirements were met at every step, including third-party vendor data acquisition.
- **Multi-state privacy law review**: Given that similar state comprehensive privacy laws are now effective in 20+ states, assess whether SDK-based or third-party-acquired data collection practices comply with the consent and notice requirements of all applicable state laws, not just Texas.
- **Monitor litigation**: Track the private class action (In re Allstate & Arity Consumer Privacy Litigation, N.D. Ill.) and the state AG case in Montgomery County, Texas for settlement terms, injunctive orders, and jury instructions that may establish liability standards for SDK-based data collection.

## Related Reports

- [Texas AG Sues Allstate and Arity for Covert Mobile Data Collection: First TDPSA Enforcement Action](reports/privacy/enforcement-actions/texas-allstate-arity-tdpsa-enforcement-2025-01-15.md) — Authoritative, updated report on the same enforcement action with case developments through April 2026, including the partial personal jurisdiction dismissal ruling.
- [Texas AG Sues Allstate and Arity in First-Ever State Comprehensive Privacy Law Enforcement Action](reports/privacy/enforcement-actions/texas-allstate-arity-tdpsa-enforcement-2026-04-14.md) — Client alert version of the same matter summarizing key facts and immediate compliance actions.
- [Texas AG Gearing Up for Aggressive Enforcement as TDPSA Takes Effect July 1, 2024](reports/privacy/enforcement-actions/texas-tdpsa-ag-enforcement-initiative-2024-06-10.md) — Background on the AG's enforcement posture and dedicated Data Privacy team before the first TDPSA action was filed.
- [Montana AG Launches Civil Investigative Demands Against Ford and Stellantis Over Connected-Car Data Sharing](reports/privacy/enforcement-actions/montana-ford-stellantis-auto-data-cid-2026-04-19.md) — A parallel AG enforcement action targeting connected-vehicle telematics data practices, illustrating the spread of this theory beyond Texas.
- [New Jersey and Texas AG Offices Build Out Dedicated Privacy Enforcement Teams (2024)](reports/privacy/enforcement-actions/nj-tx-ag-privacy-enforcement-team-2024-05-28.md) — Context on Texas AG's institutional preparation for privacy enforcement including the launch of a dedicated privacy team.

## Sources

1. [Texas AG Press Release: Ken Paxton Sues Allstate and Arity](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-allstate-and-arity-unlawfully-collecting-using-and-selling-over-45) — Official announcement of the enforcement action with allegations summary and penalty amounts.
2. [Allstate and Arity Petition (PDF)](https://www.texasattorneygeneral.gov/sites/default/files/images/press/Allstate%20and%20Arity%20Petition%20Filed.pdf) — Official court petition filed by the Texas AG in the District Court of Montgomery County, Texas.
3. [Texas HB 4 — TDPSA Enrolled Text](https://capitol.texas.gov/tlodocs/88R/billtext/html/HB00004F.htm) — Full text of the Texas Data Privacy and Security Act as enacted (88th Legislature); authoritative source for enrolled bill subsection numbering.
4. [Texas AG TDPSA Overview](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/consumer-privacy-rights/texas-data-privacy-and-security-act) — Official AG guide to the TDPSA including enforcement process and consumer rights.
5. [Texas Secretary of State — Data Broker Registry](https://www.sos.state.tx.us/statdoc/data-brokers.shtml) — Official data broker registration portal under Texas Business & Commerce Code Ch. 509.
6. [Texas SOS — Data Broker FAQ](https://www.sos.state.tx.us/statdoc/faqs4000.shtml) — Frequently asked questions on data broker registration requirements.
7. [Texas Business & Commerce Code § 509.008 — Civil Penalty](https://texas.public.law/statutes/tex._bus._and_com._code_section_509.008) — Statutory text of the data broker civil penalty provision: $100/day plus unpaid fees, capped at $10,000 per 12-month period.
8. [WilmerHale: Texas AG Brings First Ever Lawsuit Under a State Comprehensive Privacy Law](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20250121-texas-ag-brings-first-ever-lawsuit-under-a-state-comprehensive-privacy-law) — Law firm analysis confirming this is the first state comprehensive privacy law enforcement action and identifying key legal theories.
9. [Vinson & Elkins: Texas AG Targets Allstate in First Enforcement of TDPSA](https://www.velaw.com/insights/texas-ag-targets-allstate-in-first-enforcement-of-texas-data-privacy-and-security-act/) — Law firm analysis of TDPSA violations alleged and compliance implications.
10. [White & Case: Texas AG Landmark Privacy Lawsuit Signals New Era](https://www.whitecase.com/insight-alert/texas-attorney-generals-landmark-privacy-lawsuit-signals-new-era-data-privacy) — Analysis connecting Insurance Code claims to data privacy violations and broader industry implications.
11. [Securiti: Overview of Texas AG Complaint v. Allstate Corporation](https://securiti.ai/texas-ag-complaint-v-allstate-corporation/) — Detailed walkthrough of the complaint's factual allegations and legal counts.
12. [CompliancePoint: Texas AG Sues Allstate Insurance for Privacy Law Violations](https://www.compliancepoint.com/privacy/texas-ag-sues-allstate-insurance-for-privacy-law-violations/) — Secondary analysis confirming Arity's data broker registration failure and SDK details.
13. [Repairer Driven News: Class Action Lawsuit Filed Against Allstate](https://www.repairerdrivennews.com/2025/01/23/class-action-lawsuit-filed-against-allstate-for-allegedly-collecting-and-selling-data-without-consumer-consent/) — Coverage of the parallel federal class action litigation.
14. [Holland & Knight: Privacy Legislation in Texas — What Happened in 2025 and What's Next](https://www.hklaw.com/en/insights/publications/2026/02/privacy-and-cybersecurity-legislation-in-texas) — 2025 enforcement recap confirming ongoing AG enforcement campaign under TDPSA and SCOPE Act.
15. [Texas AG: Notice to Over 100 Companies Failing to Register as Data Brokers](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-notifies-over-100-companies-their-apparent-failure-comply-texas-data) — Prior AG enforcement activity establishing data broker registration enforcement posture.
16. [Goodwin: Texas' New Privacy Law Goes Into Effect — and AG Builds Enforcement Team](https://www.goodwinlaw.com/en/insights/publications/2024/06/alerts-practices-dpc-texas-new-privacy-law-goes-into-effect-enforcement) — Law firm alert documenting the AG's June 2024 announcement of the dedicated Tech and Privacy enforcement team.
