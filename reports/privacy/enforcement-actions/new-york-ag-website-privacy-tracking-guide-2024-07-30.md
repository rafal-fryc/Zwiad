---
title: "New York AG Publishes Business Guide to Website Privacy Controls, Identifies Key Mistakes in Online Tracking (July 2024)"
date: 2024-08-15
jurisdiction: "New York"
category: "privacy"
development_type: "guidance"
finding_id: "SCAN-20240815-024"
topic_key: "new-york-ef29840c-2024"
topic_type: "guidance"
first_reported: 2024-08-15
last_updated: 2024-08-15
status_history: []
cluster: "New York AG Website Privacy Controls: Tracking Technology Enforcement (GBL §§ 349-350)"
cluster_slug: "new-york-ag-website-privacy-controls-enforcement"
---

# New York AG Publishes Business Guide to Website Privacy Controls, Identifies Key Mistakes in Online Tracking (July 2024)

**Jurisdiction:** New York | **Category:** Privacy | **Date:** July 30, 2024

## Executive Summary [HIGH confidence]

On July 30, 2024, New York Attorney General Letitia James [announced two privacy guides](https://ag.ny.gov/press-release/2024/attorney-general-james-launches-website-privacy-guides-new-york-consumers-and) — one for businesses and one for consumers — focused on the use of online tracking technologies. The Business Guide to Website Privacy Controls was issued following an OAG investigation into 13 high-traffic websites that together served more than 75 million New York visitors per month and were found to have non-functional or misleading privacy controls. The guide identifies six categories of "key mistakes" businesses make when deploying cookies, pixels, and other tracking tags, and frames these mistakes as potential violations of New York's consumer protection laws prohibiting deceptive acts and practices under [General Business Law (GBL) §§ 349 and 350](https://ag.ny.gov/resources/organizations/business-guidance/website-privacy-controls). All 13 investigated companies resolved the identified issues after receiving OAG notification. The publication signals that the AG's office will continue to use deceptive-practices authority as its primary enforcement lever for tracking technology violations in the absence of a comprehensive New York state privacy law.

## Background [HIGH confidence]

### No Comprehensive New York Privacy Law — But Robust Enforcement Authority

Unlike California, Virginia, or Colorado, New York has not enacted a comprehensive consumer data privacy statute. The New York Privacy Act (NYPA) and the Stop Online Promotion of Addiction Act (SOPA) have been proposed in successive legislative sessions but have not passed as of mid-2024. However, the absence of a dedicated privacy law has not precluded active AG enforcement.

The OAG exercises its privacy enforcement authority primarily under [GBL § 349](https://ag.ny.gov/resources/organizations/business-guidance/website-privacy-controls), which broadly prohibits "deceptive acts or practices in the conduct of any business, trade or commerce," and GBL § 350, which prohibits false advertising. Under this framework, a business that tells consumers its privacy controls restrict tracking — but whose technical implementation does not deliver on that promise — may be engaged in a deceptive act or practice even if no specific privacy statute applies.

The OAG also enforces the [SHIELD Act](https://lawyersalliance.org/userFiles/uploads/legal_alerts/SHIELD_Act_Legal_Alert.pdf) (Stop Hacks and Improve Electronic Data Security Act, signed 2019), which imposes data security program requirements on any person or business that owns or licenses computerized data containing the private information of New York residents. The SHIELD Act is a security/breach-notification statute, not a broad privacy law, but it establishes the OAG's posture as an active regulator of data practices affecting New York consumers.

### Prior Enforcement: The New York-Presbyterian Hospital Pixel Settlement (2023)

The July 2024 guidance did not emerge in a vacuum. In 2023, the OAG secured a [$300,000 settlement with New York-Presbyterian Hospital](https://ag.ny.gov/press-release/2023/attorney-general-james-secures-300000-newyork-presbyterian-hospital-failing) for use of third-party tracking pixels on its website. Between June 2016 and June 2022, NYP deployed pixels and tags that transmitted sensitive health information — including users' IP addresses, health conditions searched, and appointment scheduling activity — to third-party advertising platforms, without adequate policies, vetting procedures, or business associate agreements. The settlement required the hospital to audit and remediate its tracking technology deployment, implement a written tracking technology policy, and conduct employee training.

The NYP settlement established the OAG's willingness to pursue pixel-based enforcement through both HIPAA-adjacent theories and GBL deceptive practices claims, and previewed the investigation methodology the OAG would apply in the 2024 sweep of e-commerce and consumer websites.

### The 2024 Investigation

In the months preceding the July 30 announcement, the OAG conducted a targeted investigation into tracking technology practices across a sample of high-traffic websites — primarily [well-known e-commerce operators](https://www.alstonprivacy.com/new-york-attorney-general-investigates-companies-for-website-tags-publishes-guidelines-on-online-tracking-technologies/) selling apparel, books, and tickets to live events. The investigation found that 13 websites, collectively serving an estimated 75 million consumers per month in March 2024, had privacy controls that did not function as represented. On each site, marketing or advertising tags continued to fire even after visitors opted out of tracking through the site's own cookie consent interface.

The OAG notified all 13 companies; all resolved the identified deficiencies without formal enforcement action. The OAG then converted its investigative findings into the two public-facing guides released on July 30.

## Detailed Analysis [HIGH confidence]

### The Business Guide to Website Privacy Controls

The AG's [Business Guide to Website Privacy Controls](https://ag.ny.gov/resources/organizations/business-guidance/website-privacy-controls) is directed to "companies providing services to New York consumers" and is structured around two themes: (1) identifying and preventing technical implementation problems, and (2) ensuring that privacy disclosures and interfaces are truthful and non-deceptive. The guide covers three broad categories of tracking technology: cookies, web pixels (also called tracking pixels or web beacons), and cookieless tracking methods such as digital fingerprinting and server-to-server tracking.

#### Key Mistake 1: Uncategorized or Miscategorized Tags and Cookies

Many websites deploy consent management platforms (CMPs) that allow visitors to accept or reject categories of cookies (e.g., "Essential," "Analytics," "Marketing"). The guide finds that businesses frequently fail to correctly categorize their tags and cookies within the CMP. When cookies are miscategorized — for example, a marketing pixel labeled as "Essential" — the user's opt-out preference is not honored because the CMP treats the tag as exempt from opt-out controls. Similarly, tags that are never categorized at all remain active regardless of consumer choice.

#### Key Mistake 2: Misconfigured Consent Management and Tag Management Tools

A significant technical error category involves the interaction between consent management platforms and tag management systems (TMS). When both tools are in use, they must be properly integrated so that the TMS receives and acts on opt-out signals generated by the CMP. The investigation found instances where this integration was broken: the TMS did not receive the CMP signal, and tags continued to fire. The guide notes that businesses often lack visibility into their full tag inventory and the downstream data flows each tag initiates.

#### Key Mistake 3: Hardcoded Tags

The guide gives particular emphasis to "hardcoded" tags — tracking code inserted directly into a website's HTML source rather than managed through a TMS. Because hardcoded tags are outside the TMS, the CMP has no mechanism to block them. They fire every time a web page loads, regardless of the consumer's consent choice. The OAG's investigation found hardcoded tags on multiple websites and treats their presence as a per se technical failure of privacy controls.

#### Key Mistake 4: Tag Privacy Settings Not Applied Nationally

Some third-party tag vendors offer a "restricted data processing" or "limited data use" mode that limits the scope of data collection when activated. The guide found that businesses often enable these privacy modes only in states with comprehensive privacy laws (e.g., California, Colorado, Virginia) and do not apply them to New York visitors. The OAG treats this as a problem: if a business's privacy policy implies that all users have the ability to limit tracking, applying restrictions only in certain states makes the representation misleading.

#### Key Mistake 5: Incomplete Understanding of Tag Data Collection

Businesses frequently cannot describe what data each third-party tag collects or how that data is used. The guide stresses that businesses should conduct vendor due diligence, review data processing agreements, and maintain a comprehensive tag inventory. An inability to account for data flows creates both technical compliance risk (tags may collect and transmit more than intended) and legal risk (privacy policy representations may be inaccurate).

#### Key Mistake 6: Cookieless Tracking Not Addressed

The guide expressly addresses cookieless tracking technologies — including device fingerprinting, pixel-based tracking, and server-to-server data matching — which persist even after a user opts out of cookies. Many CMPs are designed to control cookie-based tracking only and have no effect on fingerprinting or server-side tracking. The OAG's position is that if a website represents to users that declining cookies will limit tracking, but cookieless tracking continues regardless, the representation is misleading.

### The Consumer Guide

The companion [Consumer Guide to Tracking on the Web](https://ag.ny.gov/publications/consumer-guide-web-tracking) explains to New York residents how tracking works, what cookie pop-ups do and do not accomplish, and how to use browser-level privacy tools to limit tracking beyond what website-level controls offer. The guide acknowledges that website opt-outs do not delete cookies already stored on a user's device and that tracking can resume based on previously stored identifiers.

### Legal Framework: GBL §§ 349 and 350 as Privacy Enforcement Tools

The OAG's Business Guide states explicitly that the basis for its authority is New York consumer protection law — specifically the prohibition on deceptive acts and practices — rather than a dedicated privacy statute. [GBL § 349](https://ag.ny.gov/resources/organizations/business-guidance/website-privacy-controls) grants the AG broad investigative and enforcement authority when a business engages in consumer-facing deception. The key legal theory is straightforward: if a business tells consumers "you can opt out of tracking" but its technical implementation does not honor that choice, the representation is false and actionable.

This approach does not require proving that a specific data category was mishandled or that a consumer suffered a concrete harm in the tort sense. The deceptive act itself — the false or misleading privacy representation — is the violation. Legal analysts at [Alston & Bird](https://www.alstonprivacy.com/new-york-attorney-general-investigates-companies-for-website-tags-publishes-guidelines-on-online-tracking-technologies/) and [McDermott Will & Emery](https://www.mcdermottlaw.com/insights/new-york-attorney-general-issues-cookie-guidance-and-enforcement-warnings/) have noted that this theory is particularly powerful because it encompasses any business with a privacy policy or cookie consent interface — essentially every website that serves New York consumers.

The OAG's approach also mirrors enforcement theories used by state attorneys general who have brought actions against companies for deceptive cookie consent practices under their own UDAP statutes, and aligns with FTC enforcement precedents under Section 5 of the FTC Act.

## Impact Assessment [HIGH confidence]

### Who Is Affected

The Business Guide applies to any business that (a) operates a website accessible to New York consumers and (b) deploys cookies, pixels, or other tracking technologies and makes any representation — express or implied — about tracking or privacy. This encompasses virtually every commercial website operating in the United States. The guide does not limit its scope to New York-incorporated entities or businesses that specifically target New York consumers; the OAG's jurisdictional reach extends to any business whose website is accessible to and used by New York residents.

Sectors at heightened risk include:
- E-commerce retailers, ticketing platforms, and subscription services (primary subjects of the 2024 investigation)
- Healthcare providers and health-related websites (given the 2023 NYP enforcement precedent)
- Financial services firms with consumer-facing websites
- Any website using third-party advertising technology (Meta Pixel, Google Ads, LinkedIn Insight Tag, etc.)

### Compliance Requirements

The guide does not create new statutory obligations. It articulates how existing GBL deceptive practices law applies to tracking technology deployments. Practically, the guidance creates the following compliance expectations:

1. **Accurate tag inventory:** Businesses must know what tracking technologies are deployed, by whom, and what data each collects.
2. **Correct CMP configuration:** CMPs must be configured so that opt-out signals reach all relevant tags, including those managed by third-party tag management systems.
3. **No hardcoded tracking tags:** All tracking tags should be managed through a TMS that is integrated with the CMP.
4. **Vendor privacy mode applied to all users:** Restricted data processing modes should not be limited to states with comprehensive privacy laws.
5. **Cookieless tracking addressed:** Privacy controls must address non-cookie tracking methods, or the privacy policy must accurately disclose their continued operation post-opt-out.
6. **Interface design:** Cookie consent pop-ups must give "Accept" and "Decline" options equal visual weight and prominence; dark patterns (smaller decline buttons, de-emphasized opt-out options) may constitute deceptive design.

### Enforcement Outlook

The guide functions simultaneously as a compliance resource and as an enforcement roadmap — publishing criteria the OAG will use to evaluate tracking technology deployments going forward. [Privacy World](https://www.privacyworld.blog/2024/08/businesses-beware-new-york-eyeing-privacy-regulation-and-enforcement-even-absent-omnibus-state-privacy-law/) and [McDermott Will & Emery](https://www.mcdermottlaw.com/insights/new-york-attorney-general-issues-cookie-guidance-and-enforcement-warnings/) have noted that the publication of detailed guidance typically precedes a second wave of enforcement in which the AG can point to the guide as notice that businesses were on notice of the requirements. Companies that have now read the guide and failed to remediate are in a weaker position if later investigated.

The OAG has not disclosed the identities of the 13 websites investigated, and all resolved their issues informally. This suggests the AG's office used the 2024 sweep primarily to gather factual findings to inform the guide rather than to generate enforcement headlines. Future enforcement actions involving tracking technology are likely to be more formal and to involve monetary penalties, building on the $300,000 NYP precedent.

## Action Items

- **Conduct a full tracking technology audit** — inventory every cookie, pixel, tag, and script deployed on all consumer-facing web properties. Include third-party and hardcoded tags, not just those managed through the primary CMP or TMS.
- **Verify CMP-TMS integration** — confirm that opt-out signals from the CMP successfully suppress all relevant tags within the TMS. Test this with a technical audit (e.g., using browser network inspection tools or a third-party tag auditing service) from a New York IP address.
- **Eliminate hardcoded tracking tags** — migrate all tracking technology to TMS-controlled deployment so the CMP can suppress them on opt-out.
- **Apply vendor privacy modes universally** — if a third-party tag vendor offers a "restricted data processing" or "limited data use" flag, activate it for all users, not just residents of states with comprehensive privacy laws.
- **Audit cookieless tracking** — identify whether device fingerprinting, server-to-server matching, or pixel-only tracking operates independently of cookie consent. Update the privacy policy to accurately describe these technologies, or extend opt-out controls to cover them.
- **Review consent interface design** — ensure that "Accept" and "Decline" (or equivalent) buttons are presented with equal prominence, size, and color. Remove any design elements that de-emphasize the opt-out path.
- **Review and update your privacy policy** — ensure that all representations about what tracking occurs, when, and how consumers can opt out, accurately reflect actual technical implementation.
- **Monitor for OAG enforcement follow-up** — the July 2024 guide signals active regulatory attention. Subscribe to AG press releases and maintain a compliance calendar to re-audit tracking technology configurations at least annually.

## Related Reports

- [reports/privacy/enforcement-actions/nj-tx-ag-privacy-enforcement-team-2024-05-28.md](reports/privacy/enforcement-actions/nj-tx-ag-privacy-enforcement-team-2024-05-28.md) — State AG offices building dedicated privacy enforcement capacity, directly relevant to understanding the enforcement environment in which the NY AG guide was issued.
- [reports/privacy/litigation/massachusetts-doe-v-tenet-healthcare-pixel-tracking-2024-05-20.md](reports/privacy/litigation/massachusetts-doe-v-tenet-healthcare-pixel-tracking-2024-05-20.md) — Parallel private litigation arising from healthcare website pixel tracking, the same technology category addressed by the NY AG's business guide.
- [reports/privacy/litigation/washington-overlake-hospital-pixel-privacy-2024-06-07.md](reports/privacy/litigation/washington-overlake-hospital-pixel-privacy-2024-06-07.md) — Healthcare pixel tracking litigation in another jurisdiction, providing broader enforcement context for the tracking technology issues the NY AG guide addresses.

## Sources

1. [Attorney General James Launches Website Privacy Guides for New York Consumers and Businesses — NY AG Press Release, July 30, 2024](https://ag.ny.gov/press-release/2024/attorney-general-james-launches-website-privacy-guides-new-york-consumers-and) — Official OAG announcement with investigation findings and guide summary.
2. [Business Guide to Website Privacy Controls — NY AG Official Guide](https://ag.ny.gov/resources/organizations/business-guidance/website-privacy-controls) — The official business-facing guide; primary source for the six key mistakes and compliance framework.
3. [Consumer Guide to Tracking on the Web — NY AG](https://ag.ny.gov/publications/consumer-guide-web-tracking) — Companion consumer-facing guide explaining tracking mechanisms and consumer opt-out tools.
4. [New York Attorney General Investigates Companies for Website Tags, Publishes Guidelines on Online Tracking Technologies — Alston & Bird Privacy Blog](https://www.alstonprivacy.com/new-york-attorney-general-investigates-companies-for-website-tags-publishes-guidelines-on-online-tracking-technologies/) — Law firm analysis of the guide's legal framework and enforcement theory under GBL §§ 349 and 350.
5. [New York Attorney General Publishes Guide to Avoid "Key Mistakes" Regarding Online Tracking Technologies — Sidley Austin / Data Matters Blog](https://datamatters.sidley.com/2024/08/13/new-york-attorney-general-publishes-guide-to-avoid-key-mistakes-regarding-online-tracking-technologies/) — Detailed law firm analysis of each key mistake identified in the business guide.
6. [New York AG Issues Cookie Guidance and Enforcement Warnings — McDermott Will & Emery](https://www.mcdermottlaw.com/insights/new-york-attorney-general-issues-cookie-guidance-and-enforcement-warnings/) — Analysis emphasizing the enforcement signal embedded in the guide's publication.
7. [NY AG Publishes Privacy Guides on Website Tracking — Hunton Andrews Kurth](https://www.hunton.com/privacy-and-information-security-law/ny-ag-publishes-privacy-guides-on-website-tracking) — Law firm summary with compliance implications for businesses.
8. [Businesses Beware: New York Eyeing Privacy Regulation and Enforcement Even Absent Omnibus State Privacy Law — Privacy World Blog](https://www.privacyworld.blog/2024/08/businesses-beware-new-york-eyeing-privacy-regulation-and-enforcement-even-absent-omnibus-state-privacy-law/) — Analysis of the NY AG's use of UDAP authority as a substitute for comprehensive privacy law.
9. [Cookie Cutter: NY AG Announces Cookie Scrutiny with Business Guide to Website Privacy Controls — Wyrick Robbins Practical Privacy Blog](https://practicalprivacy.wyrick.com/blog/cookie-cutter-ny-ag-announces-cookie-scrutiny-with-business-guide-to-website-privacy-controls) — Analysis of dark pattern / deceptive design concerns raised by the guide.
10. [Attorney General James Secures $300,000 from NewYork-Presbyterian Hospital for Failing to Protect Patient Privacy — NY AG Press Release, 2023](https://ag.ny.gov/press-release/2023/attorney-general-james-secures-300000-newyork-presbyterian-hospital-failing) — Prior OAG enforcement action establishing pixel tracking enforcement precedent.
11. [New York Attorney General Releases Website Privacy Guidance for Companies Tracking Users Online — Koley Jessen](https://www.koleyjessen.com/insights/publications/new-york-attorney-general-releases-website-privacy-guidance-for-companies-tracking-users-online) — Additional law firm analysis covering CMP configuration and vendor privacy mode issues.
12. [SHIELD Act Legal Alert — Lawyers Alliance for New York](https://lawyersalliance.org/userFiles/uploads/legal_alerts/SHIELD_Act_Legal_Alert.pdf) — Background on New York's SHIELD Act data security requirements and their relationship to the AG's broader privacy enforcement authority.
