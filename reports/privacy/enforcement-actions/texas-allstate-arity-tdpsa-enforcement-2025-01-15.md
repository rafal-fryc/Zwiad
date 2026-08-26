---
title: "Texas AG Sues Allstate and Arity for Covert Mobile Data Collection: First TDPSA Enforcement Action"
date: 2025-01-15
jurisdiction: "Texas"
category: "privacy"
development_type: "enforcement"
finding_id: "SCAN-20250115-001"
topic_key: "texas-e853212b-2025"
topic_type: "enforcement_action"
first_reported: 2025-01-15
last_updated: 2026-04-16
status_history:
  - "2026-04-16: Revised per reviewer round 1 — corrected § 541.001 subsection from (18) to (29); corrected Data Broker Law penalty structure ($10,000 is 12-month cap, not per-violation floor); added April 10, 2025 partial personal jurisdiction dismissal of Allstate Corporation and Arity 875 LLC; clarified FCRA ruling as partial (consent-related CRA claims dismissed; misleading-reporting theory survived)."
cluster: "Texas AG v. Allstate/Arity: TDPSA Enforcement Action"
cluster_slug: "texas-ag-allstate-arity-tdpsa-enforcement"
---

# Texas AG Sues Allstate and Arity for Covert Mobile Data Collection: First TDPSA Enforcement Action

**Jurisdiction:** Texas | **Category:** privacy | **Date:** 2025-01-15

## Executive Summary [HIGH confidence]

On January 13, 2025, Texas Attorney General Ken Paxton filed suit against Allstate Corporation and five of its subsidiaries — including three entities operating under the Arity brand — for secretly collecting, processing, and selling the precise geolocation and driving behavior data of more than 45 million Americans without their knowledge or consent. The [complaint](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-allstate-and-arity-unlawfully-collecting-using-and-selling-over-45), filed in the District Court of Montgomery County, Texas, marks the first enforcement action brought by any state attorney general under a U.S. state comprehensive consumer data privacy law. The State alleges violations of three separate Texas statutes: the [Texas Data Privacy and Security Act (TDPSA)](https://statutes.capitol.texas.gov/Docs/BC/htm/BC.541.htm) (Tex. Bus. & Com. Code Ch. 541), the [Texas Data Broker Law](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/consumer-privacy-rights/texas-data-broker-act) (Tex. Bus. & Com. Code Ch. 509), and the Texas Insurance Code's prohibition on unfair and deceptive acts and practices. The State seeks more than $1 million in civil penalties plus injunctive relief requiring deletion of unlawfully collected data. This case is widely regarded as a landmark that will shape how comprehensive state privacy statutes are enforced across the 20+ U.S. states that have enacted them.

**Case Status Update (April 10, 2025):** Judge Vince Santini of the 457th District Court in Montgomery County dismissed The Allstate Corporation and Arity 875 LLC from the Texas state action for lack of personal jurisdiction, finding those entities lack sufficient ties to Texas to be haled into its courts. Per [Bloomberg Law](https://news.bloomberglaw.com/litigation/allstate-ends-texas-data-collection-claims-in-latest-paxton-blow), the remaining defendants are Arity LLC, Arity Services LLC, Allstate Insurance Company, and Allstate Vehicle and Property Insurance Company.

## Background [HIGH confidence]

### The Texas Data Privacy and Security Act

The TDPSA was enacted as [House Bill 4 (88th Regular Session)](https://capitol.texas.gov/tlodocs/88R/billtext/html/HB00004F.htm) and became effective on July 1, 2024, codified at [Chapter 541 of the Texas Business and Commerce Code](https://statutes.capitol.texas.gov/Docs/BC/htm/BC.541.htm). The statute follows the Virginia-model framework, creating rights for Texas consumers to access, correct, delete, and opt out of the processing of their personal data. The TDPSA specifically categorizes "precise geolocation data" as **sensitive data**, requiring a controller to obtain affirmative, informed consumer consent before processing it — a heightened obligation that goes beyond baseline notice requirements. The Texas AG holds exclusive enforcement authority; the TDPSA does not create a private right of action. Penalties reach up to $7,500 per violation following a 30-day cure period.

### The Texas Data Broker Law

Texas separately regulates data brokers under [Chapter 509 of the Texas Business and Commerce Code](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/consumer-privacy-rights/texas-data-broker-act). A "data broker" is a business entity that sells, licenses, trades, or otherwise provides personal data about individuals to third parties that it did not collect directly from those individuals. Data brokers must register annually with the Texas Secretary of State by March 1 of each year, pay a $300 registration fee, and maintain a written information security program. The civil penalty for a data broker that fails to register is computed as $100 per day in violation plus unpaid registration fees, and may not exceed $10,000 assessed against the same data broker in any 12-month period ([Tex. Bus. & Com. Code § 509.008](https://law.justia.com/codes/texas/2023/business-and-commerce-code/title-11/subtitle-a/chapter-509/section-509-008/)).

### Texas AG Privacy Enforcement Build-Up

The filing of this lawsuit was preceded by a substantial institutional build-up. In [June 2024](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/consumer-privacy-rights/texas-data-privacy-and-security-act), the Texas AG announced the formation of a dedicated Privacy and Technology enforcement team within the Consumer Protection Division, reportedly exceeding ten attorneys at launch, timed to the TDPSA's July 1, 2024 effective date. The Allstate/Arity action is the unit's inaugural enforcement filing.

### Allstate and Arity

Allstate is one of the United States' largest personal lines insurance carriers. Arity is a data analytics subsidiary Allstate formed to operate its telematics and driving behavior data business. Arity developed and licensed a software development kit (SDK) designed to be embedded in third-party mobile applications, enabling persistent collection of location, movement, and driving behavior signals from app users' phones. Arity in turn sold processed driving behavior scores and raw data to insurance carriers — including Allstate itself — for use in underwriting and pricing.

## Detailed Analysis [HIGH confidence]

### The SDK-Based Data Collection Scheme

The complaint alleges that Arity developed an SDK it licensed to third-party app publishers, paying those publishers millions of dollars in exchange for embedding the SDK in their applications. The SDK was specifically targeted at apps that already incorporated location-based features — such as navigation, fuel rewards, or family safety tools — so that the additional location polling by the SDK would not be apparent to end users. Named apps include [Life360](https://www.carriermanagement.com/news/2025/01/27/271086.htm), GasBuddy, Fuel Rewards, and Routely.

Once integrated, the SDK allegedly captured latitude, longitude, speed, GPS time, bearing, and altitude at intervals of 15 seconds or less. From approximately 40 million active connections, the defendants built what the State describes as "the world's largest driving behavior database," comprising trillions of miles of location data from over 45 million Americans, according to the [Texas AG press release](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-allstate-and-arity-unlawfully-collecting-using-and-selling-over-45). Consumers who downloaded the third-party apps were wholly unaware that Arity's software was embedded within them or that their geolocation and driving data was being harvested and monetized.

### Alleged TDPSA Violations

The complaint asserts three TDPSA violation theories against the Arity defendants as detailed by [Hunton Andrews Kurth](https://www.hunton.com/privacy-and-information-security-law/texas-ag-sues-allstate-for-violations-of-texas-privacy-law-in-first-enforcement-action-under-a-state-comprehensive-data-privacy-law) and [WilmerHale](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20250121-texas-ag-brings-first-ever-lawsuit-under-a-state-comprehensive-privacy-law):

1. **Failure to provide a privacy notice.** The TDPSA requires controllers to provide consumers with a clear, accessible privacy notice describing categories of personal data collected and the purposes for which it is processed. Consumers were "wholly unaware" that the Arity defendants were collecting their sensitive data, and no adequate notice was provided.

2. **Failure to obtain affirmative consent for sensitive data.** Precise geolocation data constitutes "sensitive data" under [Tex. Bus. & Com. Code § 541.001(29)](https://statutes.capitol.texas.gov/Docs/BC/htm/BC.541.htm), which the TDPSA defines to include precise geolocation information. A controller must obtain affirmative, opt-in consent — defined as a "clear affirmative act signifying a freely given, specific, informed, and unambiguous agreement" — before processing sensitive data. The Act expressly provides that consent cannot be established by "acceptance of a general or broad terms of use" or by dark patterns. The complaint alleges that burying data collection terms in app EULAs that consumers never associated with Arity did not satisfy this standard.

3. **Failure to provide opt-out mechanism and required sales notice.** The TDPSA requires a controller selling sensitive personal data to post a conspicuous notice stating: "NOTICE: We may sell your sensitive personal data." The Arity defendants posted no such notice and provided no mechanism for consumers to opt out of the sale of their data for purposes of targeted advertising or profiling.

### Alleged Texas Data Broker Law Violation

Arity derived revenue from selling personal data of Texas consumers it had not collected directly from those individuals — the precise definition of a regulated "data broker" under [Tex. Bus. & Com. Code Ch. 509](https://www.sos.state.tx.us/statdoc/data-brokers.shtml). The State alleges that Arity failed to register with the Texas Secretary of State by the March 1, 2024 statutory deadline and continued operating unregistered. Under [Tex. Bus. & Com. Code § 509.008](https://law.justia.com/codes/texas/2023/business-and-commerce-code/title-11/subtitle-a/chapter-509/section-509-008/), the civil penalty is $100 per day in violation plus unpaid registration fees, not to exceed $10,000 assessed against the same data broker in any 12-month period. The State claims entitlement to more than $1,000,000 in total monetary relief across all violation theories, as noted by [National Law Review](https://natlawreview.com/article/texas-ag-sues-allstate-violations-texas-privacy-law-first-enforcement-action-under).

### Alleged Texas Insurance Code Violations

The complaint adds a third statutory track under the Texas Insurance Code's prohibition on unfair and deceptive acts and practices in the business of insurance. The [Vinson & Elkins analysis](https://www.velaw.com/insights/texas-ag-targets-allstate-in-first-enforcement-of-texas-data-privacy-and-security-act/) explains that the State targets Allstate's insurance operations directly, alleging: (1) failure to verify consumer consent before purchasing driving-related data from app publishers; (2) "turning a blind eye" to the strong likelihood that consumers had not consented to the collection and sale of their data; and (3) using unlawfully obtained data in its own underwriting and pricing processes while marketing the same data to other carriers. This count opens an additional penalty track and signals that data-driven underwriting is now a privacy enforcement target.

### Remedies Sought

The State seeks: (1) a permanent injunction prohibiting continued violations; (2) an order requiring deletion of all unlawfully processed data; (3) restitution to affected consumers; and (4) civil penalties exceeding $1,000,000, comprising up to $7,500 per TDPSA violation and Data Broker Law penalties computed per § 509.008 (capped at $10,000 per 12-month period), per the [Texas AG press release](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-allstate-and-arity-unlawfully-collecting-using-and-selling-over-45) and [Securiti overview](https://securiti.ai/texas-ag-complaint-v-allstate-corporation/).

### Texas State Action — Personal Jurisdiction Dismissal (April 10, 2025) [HIGH confidence]

On April 10, 2025, Judge Vince Santini of the 457th District Court in Montgomery County entered an order dismissing two of the original six defendants — The Allstate Corporation and Arity 875 LLC — for lack of personal jurisdiction. According to [Bloomberg Law](https://news.bloomberglaw.com/litigation/allstate-ends-texas-data-collection-claims-in-latest-paxton-blow) and [MLex](https://www.mlex.com/mlex/articles/2326565/texas-court-lacks-jurisdiction-over-allstate-subsidiary-judge-says-in-location-privacy-suit), the court found that those entities lacked sufficient contacts with Texas to support personal jurisdiction; Allstate Corporation is headquartered in Illinois and Arity 875 LLC likewise demonstrated inadequate Texas presence. The ruling does not affect the claims against the remaining defendants: Arity LLC, Arity Services LLC, Allstate Insurance Company, and Allstate Vehicle and Property Insurance Company. The Texas AG's case against those four entities proceeds on all three statutory tracks.

### Parallel Federal Class Action Litigation [HIGH confidence]

The Texas AG filing triggered a wave of private class action lawsuits, which were consolidated in the Northern District of Illinois as *In re Allstate & Arity Consumer Privacy Litigation*, No. 25 CV 407 (N.D. Ill.). On March 3, 2026, Judge Jeremy C. Daniel issued a ruling on defendants' motions to dismiss. The court denied dismissal of claims under the [Federal Wiretap Act](https://natlawreview.com/article/massive-win-plaintiffs-federal-court-keeps-wiretap-and-fcra-claims-alive) and various state consumer protection and privacy tort claims, while dismissing computer hacking claims. On the Wiretap Act, the court held that even though the third-party app developers consented to the SDK's data interception, the plaintiffs' invocation of the "crime-tort exemption" — which nullifies party consent when interception is conducted for the purpose of committing an independent tortious act — was sufficient to survive dismissal.

On the FCRA, the court issued a **partial ruling**. Judge Daniel dismissed the consent-related FCRA claims against Arity in its capacity as a consumer reporting agency (CRA) — those claims turned on whether plaintiffs had consented to furnishing certain information and did not survive. However, the separate FCRA theory that Arity willfully reported misleading driving behavior information survived dismissal. Per [Repairer Driven News](https://www.repairerdrivennews.com/2026/03/19/court-allows-suit-alleging-allstate-collected-and-sold-consumer-data-to-move-forward-dismisses-portion/), the court found the allegation that Arity's reports "purported to reflect individuals' driving behavior — but omitted the important context that they were not driving" squarely within the FCRA's definition of "misleading" information. The FCRA preemption argument was also rejected for state law claims not predicated on Arity's CRA status. The net result is a partial victory for plaintiffs: the misleading-reporting FCRA theory and Wiretap Act claims proceed; the consent-based CRA claims do not.

## Impact Assessment [HIGH confidence]

### Who Is Affected

The enforcement action implicates any entity that:
- Operates or licenses SDKs that collect location, telematics, or behavioral data from third-party mobile apps;
- Processes, sells, or licenses precise geolocation data of Texas consumers without affirmative opt-in consent;
- Derives revenue from personal data of more than 50,000 Texas consumers it did not collect directly (triggering data broker registration obligations);
- Uses third-party behavioral or telematics data in insurance underwriting, pricing, or claims processing.

The data-driven insurance sector faces the sharpest exposure. Carriers and analytics vendors that purchase telematics scores, driving behavior data, or mobility data from third parties have almost certainly acquired data processed through SDK pipelines similar to the one alleged here.

### Compliance Implications

**SDK operators and publishers.** The complaint establishes that an SDK vendor is a "controller" under the TDPSA with independent notice-and-consent obligations, separate from the app publisher in which the SDK is embedded. App publishers that receive financial consideration for embedding third-party SDKs share exposure. Companies on either side of an SDK licensing relationship must confirm: (a) what categories of personal data the SDK collects; (b) whether precise geolocation or other sensitive data categories are involved; (c) what privacy notices and consent flows have been implemented; and (d) whether the data-flow is disclosed in the apps' own privacy policies with appropriate specificity.

**Data brokers.** Texas's Data Broker Law registration requirement is a strict-liability regime with no cure period defense. Any entity that meets the statutory definition — selling personal data it did not collect directly from consumers — must register by March 1 of each year. The Arity count demonstrates the AG will use registration failures as a stand-alone enforcement hook even when layered onto other privacy claims. Note that the § 509.008 penalty cap of $10,000 per 12-month period does not reduce the importance of compliance: the AG may file separate penalty actions for each 12-month period of non-registration, and registration failures also give rise to attorney's fees exposure.

**Downstream data users.** Insurance carriers, marketing platforms, and analytics firms that purchase or license driving behavior, mobility, or behavioral scoring data should scrutinize contractual representations about consent provenance. The Insurance Code count puts carriers on notice that purchasing data without verifying consent is itself an unfair practice.

**The cure period.** The TDPSA provides a 30-day cure period before the AG may assess penalties. However, as [Hunton Andrews Kurth](https://www.hunton.com/privacy-and-information-security-law/texas-ag-sues-allstate-for-violations-of-texas-privacy-law-in-first-enforcement-action-under-a-state-comprehensive-data-privacy-law) notes, the AG's approach in this case suggests the State will still pursue penalties for widespread, systemic violations that cannot be meaningfully cured after the fact — particularly where the underlying conduct involved covert collection of sensitive data at scale.

### National Enforcement Implications

The [White & Case analysis](https://www.whitecase.com/insight-alert/texas-attorney-generals-landmark-privacy-lawsuit-signals-new-era-data-privacy) identifies this case as the template other state AGs will study when deploying their own comprehensive privacy statutes. The theory of joint-controller liability for SDK ecosystems, the aggressive use of a data broker registration statute as a parallel penalty track, and the pairing of privacy claims with industry-specific code violations (here, insurance) are all replicable in states including California (CCPA/CPRA), Connecticut (CTDPA), Colorado (CPA), Virginia (VCDPA), and Oregon (OCPA). As of April 2026, the class action wiretap and FCRA misleading-reporting claims surviving the Northern District of Illinois motion to dismiss add private litigation as a parallel risk vector for similar SDK-based collection schemes nationwide. The April 2025 personal jurisdiction dismissal also signals that out-of-state parent companies may be able to escape state court proceedings if their Texas nexus is insufficiently direct — a structural consideration for multi-entity corporate families.

## Action Items

- **Inventory SDKs immediately.** Any company that publishes mobile apps or licenses SDKs to third parties should produce a complete list of every SDK deployed, the data it collects, and whether that data includes precise geolocation or other TDPSA-sensitive categories.
- **Audit consent flows for sensitive data.** Confirm that collection of precise geolocation, health, biometric, genetic, or similar sensitive data is gated by an affirmative, opt-in consent mechanism that is distinct from general terms of service acceptance — and that the consent flow identifies the specific collector.
- **Confirm data broker registration in Texas.** Any entity deriving revenue from personal data of Texas consumers it did not collect directly from those individuals must be registered with the Texas Secretary of State under Tex. Bus. & Com. Code Ch. 509. Unregistered entities should register without delay and assess historical penalty exposure under § 509.008 ($100 per day plus unpaid fees, capped at $10,000 per 12-month period, with separate potential liability for each registration year missed).
- **Review downstream data purchase contracts.** Carriers, analytics firms, and marketers purchasing telematics, driving behavior, or location data should obtain contractual representations that the data was collected with consent meeting TDPSA standards, and should conduct due diligence on the consent provenance of incumbent data sets.
- **Post required sensitive data sales notice.** Any TDPSA-covered controller that sells or may sell sensitive personal data must post the statutory notice: "NOTICE: We may sell your sensitive personal data." This applies even when data is sold indirectly through data brokers or aggregators.
- **Monitor the Montgomery County docket and the Northern District of Illinois class action.** The Texas AG complaint is the precedent-setting filing; any consent decree, settlement, or ruling on the merits will set the compliance floor. The parallel federal class action (wiretap and FCRA misleading-reporting theories) creates independent exposure and may produce an earlier settlement signal.
- **Evaluate Insurance Code UDAP risk.** Insurers using third-party behavioral or telematics data for underwriting should document the consent provenance of each data source and assess whether their practices could be characterized as purchasing unlawfully obtained data, which this complaint frames as a per se unfair and deceptive practice.

## Related Reports

- [reports/privacy/enforcement-actions/texas-allstate-arity-tdpsa-enforcement-2026-04-14.md](reports/privacy/enforcement-actions/texas-allstate-arity-tdpsa-enforcement-2026-04-14.md) — Client-alert companion covering the same enforcement action with a focus on immediate compliance action items.
- [reports/privacy/enforcement-actions/nj-tx-ag-privacy-enforcement-team-2024-05-28.md](reports/privacy/enforcement-actions/nj-tx-ag-privacy-enforcement-team-2024-05-28.md) — Background on the Texas AG Privacy and Technology enforcement team whose first filed action is the Allstate/Arity case.
- [reports/privacy/enforcement-actions/texas-tdpsa-ag-enforcement-initiative-2024-06-10.md](reports/privacy/enforcement-actions/texas-tdpsa-ag-enforcement-initiative-2024-06-10.md) — Earlier report on the Texas AG's announced TDPSA enforcement initiative, providing immediate pre-suit context.
- [reports/privacy/state-comprehensive-laws/florida-oregon-texas-privacy-laws-july-2024-2024-05-15.md](reports/privacy/state-comprehensive-laws/florida-oregon-texas-privacy-laws-july-2024-2024-05-15.md) — Comparative analysis of state privacy laws effective July 2024, including the TDPSA framework underlying this enforcement action.

## Sources

1. [Texas OAG — Press Release: AG Paxton Sues Allstate and Arity (Jan. 13, 2025)](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-allstate-and-arity-unlawfully-collecting-using-and-selling-over-45) — Primary official announcement with full allegations, statutes cited, and penalty demand.
2. [Texas OAG — Allstate and Arity Petition Filed (PDF)](https://www.texasattorneygeneral.gov/sites/default/files/images/press/Allstate%20and%20Arity%20Petition%20Filed.pdf) — Official complaint filed in Montgomery County District Court; primary legal text of the allegations.
3. [Texas Business and Commerce Code Chapter 541 (TDPSA)](https://statutes.capitol.texas.gov/Docs/BC/htm/BC.541.htm) — Official text of the statute; key provisions include sensitive data definition (§ 541.001(29)) and consent requirements.
4. [Texas Business and Commerce Code § 509.008 — Civil Penalty (Justia)](https://law.justia.com/codes/texas/2023/business-and-commerce-code/title-11/subtitle-a/chapter-509/section-509-008/) — Official statutory text of the Data Broker Law civil penalty provision; confirms $100/day plus unpaid fees, capped at $10,000 per 12-month period.
5. [Texas Data Broker Act — Texas AG Overview](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/consumer-privacy-rights/texas-data-broker-act) — Official AG summary of data broker registration obligations and penalties.
6. [Texas Secretary of State — Data Broker Registration](https://www.sos.state.tx.us/statdoc/data-brokers.shtml) — Official registration portal and procedural requirements for data brokers.
7. [WilmerHale — Texas AG Brings First Ever Lawsuit Under a State Comprehensive Privacy Law (Jan. 21, 2025)](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20250121-texas-ag-brings-first-ever-lawsuit-under-a-state-comprehensive-privacy-law) — Detailed factual and statutory breakdown of the complaint, including SDK technical details.
8. [Vinson & Elkins — Texas AG Targets Allstate in First Enforcement of TDPSA](https://www.velaw.com/insights/texas-ag-targets-allstate-in-first-enforcement-of-texas-data-privacy-and-security-act/) — Analysis of Insurance Code and TDPSA interplay; downstream data purchaser liability discussion.
9. [Hunton Andrews Kurth — Texas AG Sues Allstate for Violations of Texas Privacy Law](https://www.hunton.com/privacy-and-information-security-law/texas-ag-sues-allstate-for-violations-of-texas-privacy-law-in-first-enforcement-action-under-a-state-comprehensive-data-privacy-law) — TDPSA provision-by-provision mapping, cure period analysis, and compliance takeaways.
10. [White & Case — Texas Attorney General's Landmark Privacy Lawsuit Signals New Era in Data Privacy Enforcement](https://www.whitecase.com/insight-alert/texas-attorney-generals-landmark-privacy-lawsuit-signals-new-era-data-privacy) — National enforcement implications and comparison to other state comprehensive privacy statutes.
11. [National Law Review — MASSIVE WIN FOR PLAINTIFFS: Federal Court Keeps Wiretap and FCRA Claims Alive](https://natlawreview.com/article/massive-win-plaintiffs-federal-court-keeps-wiretap-and-fcra-claims-alive) — Analysis of the Northern District of Illinois March 3, 2026 partial ruling in *In re Allstate & Arity Consumer Privacy Litigation*, No. 25 CV 407; wiretap and FCRA misleading-reporting claims survive.
12. [Repairer Driven News — Court allows suit alleging Allstate collected and sold consumer data to move forward, dismisses portion (Mar. 19, 2026)](https://www.repairerdrivennews.com/2026/03/19/court-allows-suit-alleging-allstate-collected-and-sold-consumer-data-to-move-forward-dismisses-portion/) — Detailed breakdown of the partial FCRA dismissal; confirms consent-related CRA claims dismissed, misleading-reporting theory survived.
13. [Securiti — Overview of Texas AG Complaint v. Allstate Corporation](https://securiti.ai/texas-ag-complaint-v-allstate-corporation/) — Summary of civil penalties sought and specific TDPSA violation theories from the complaint.
14. [National Law Review — Texas AG Sues Allstate for Violations of Texas Privacy Law (First Enforcement Action)](https://natlawreview.com/article/texas-ag-sues-allstate-violations-texas-privacy-law-first-enforcement-action-under) — Summary of the Data Broker Law count and penalty structure.
15. [Carrier Management — Allstate, Arity Legal Troubles Mount; Class Action Filings Allege Privacy Violations](https://www.carriermanagement.com/news/2025/01/27/271086.htm) — Coverage of parallel class actions and named third-party apps including Life360.
16. [Bloomberg Law — Allstate Ends Texas Data Collection Claims in Latest Paxton Blow](https://news.bloomberglaw.com/litigation/allstate-ends-texas-data-collection-claims-in-latest-paxton-blow) — Reports April 10, 2025 dismissal of Allstate Corporation and Arity 875 LLC for lack of personal jurisdiction; identifies remaining defendants.
17. [MLex — Texas court lacks jurisdiction over Allstate, subsidiary, judge says in location privacy suit](https://www.mlex.com/mlex/articles/2326565/texas-court-lacks-jurisdiction-over-allstate-subsidiary-judge-says-in-location-privacy-suit) — Corroborating coverage of Judge Santini's April 10, 2025 personal jurisdiction ruling.
