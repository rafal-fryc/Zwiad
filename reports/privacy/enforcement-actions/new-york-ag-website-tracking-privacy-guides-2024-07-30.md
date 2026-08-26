---
title: "New York AG Publishes Privacy Guides on Website Tracking Technologies"
date: 2024-07-30
jurisdiction: "New York"
category: "privacy"
development_type: "guidance"
finding_id: "SCAN-20240819-002"
topic_key: "new-york-edbb8500-2024"
topic_type: "guidance"
first_reported: 2024-08-19
last_updated: 2026-04-21
status_history: []
cluster: "New York AG Website Privacy Controls: Tracking Technology Enforcement (GBL §§ 349-350)"
cluster_slug: "new-york-ag-website-privacy-controls-enforcement"
---

# New York AG Publishes Privacy Guides on Website Tracking Technologies

**Jurisdiction:** New York | **Category:** Privacy | **Date:** July 30, 2024

## Executive Summary [HIGH confidence]

On July 30, 2024, New York Attorney General Letitia James [announced](https://ag.ny.gov/press-release/2024/attorney-general-james-launches-website-privacy-guides-new-york-consumers-and) the publication of two privacy guides — the [Business Guide to Website Privacy Controls](https://ag.ny.gov/resources/organizations/business-guidance/website-privacy-controls) and the [Consumer Guide to Web Tracking](https://ag.ny.gov/publications/consumer-guide-web-tracking) — following an Office of the Attorney General (OAG) investigation that found 13 high-traffic websites serving over 75 million consumers per month had broken or deceptive privacy controls. The guides signal an enforcement posture under New York's existing consumer protection law, [General Business Law (GBL) § 349](https://law.justia.com/codes/new-york/gbs/article-22-a/349/), even in the absence of a comprehensive state privacy statute. Companies operating websites that serve New York consumers should treat these guides as de facto compliance benchmarks given the OAG's explicit warning that inaccurate privacy representations and non-functioning opt-out tools can constitute unlawful deceptive acts. All 13 websites identified as non-compliant resolved their issues after being notified by the OAG, suggesting the guidance is intended to create a compliance floor before the agency proceeds to formal enforcement.

## Background [HIGH confidence]

New York lacks a comprehensive consumer privacy statute comparable to the California Consumer Privacy Act (CCPA) or Virginia's CDPA. Legislative efforts to enact a comprehensive privacy law — most notably the New York Privacy Act — have stalled repeatedly in the legislature. In this regulatory gap, the OAG has relied on [GBL § 349](https://law.justia.com/codes/new-york/gbs/article-22-a/349/), which prohibits deceptive acts or practices in the conduct of any business, trade, or commerce in New York State. That provision authorizes the AG to seek injunctive relief, restitution, and civil penalties of up to $5,000 per violation.

The OAG has a track record of using GBL § 349 as a basis for privacy and cybersecurity enforcement. Prior actions include investigations of companies under the [SHIELD Act](https://ag.ny.gov/resources/organizations/data-breach-reporting/shield-act) (New York's data security and breach notification law, enacted July 25, 2019), which imposed affirmative obligations to implement reasonable data security safeguards. Enforcement highlights include a $650,000 settlement with Dunkin Donuts over a credential-stuffing data breach and an [October 2025 settlement](https://ag.ny.gov/press-release/2025/attorney-general-james-secures-142-million-car-insurance-companies-over-data) of $14.2 million against car insurance companies over data breaches.

Website tracking technologies — including HTTP cookies, tracking pixels, web beacons, and JavaScript tags placed by third-party advertising and analytics platforms — have attracted increasing regulatory scrutiny nationwide. In the healthcare context, the use of tracking pixels on hospital websites led to the OAG investigating New York-Presbyterian Hospital over potential HIPAA and GBL violations. The July 2024 guidance broadens this scrutiny to general commercial e-commerce websites, marking the first time the OAG published a sector-agnostic compliance guide specifically addressing online tracking technology deployment.

## Detailed Analysis [HIGH confidence]

### The OAG Investigation

Over several months preceding the announcement, the OAG analyzed third-party tags and privacy controls on a cross-section of high-traffic websites. The [official press release](https://ag.ny.gov/press-release/2024/attorney-general-james-launches-website-privacy-guides-new-york-consumers-and) confirms that 13 websites were found non-compliant, collectively receiving an estimated 75 million visitors in March 2024. The websites were predominantly well-known e-commerce sites selling consumer goods such as apparel, books, and event tickets. The OAG contacted each company, requested remediation, and all 13 resolved the issues before the guides were published. The OAG did not publicly name the 13 companies.

The central finding was that certain marketing or advertising tags remained active even after users attempted to opt out of tracking via the websites' own privacy controls. This gap between disclosed behavior (opt-out is honored) and actual behavior (tracking continues) directly implicates GBL § 349's prohibition on deceptive practices.

### The Business Guide to Website Privacy Controls [HIGH confidence]

The [Business Guide](https://ag.ny.gov/resources/organizations/business-guidance/website-privacy-controls) identifies six categories of common mistakes found during the OAG investigation:

1. **Uncategorized or miscategorized tags and cookies.** Consent management platforms (CMPs) categorize tags as "necessary," "analytics," or "marketing." If a tag is uncategorized, the CMP cannot determine whether to fire it when a user opts out of a category. Seven of the 13 websites had at least one tag that was not properly categorized, making this the leading cause of broken privacy controls among the investigated websites.

2. **Misconfigured tools.** Tag management systems (TMS) must be properly integrated with CMPs so that opt-out signals are passed through the TMS to individual tags. At some of the investigated websites, the CMP failed to pass opt-out signals through to the TMS, resulting in tracking continuing after a user opted out.

3. **Hardcoded tags.** Some third-party tags are embedded directly into website code rather than managed through a TMS. Because they bypass the TMS entirely, CMPs cannot suppress hardcoded tags based on user consent preferences.

4. **Tag-level privacy settings applied only in states with comprehensive privacy laws.** Some third-party tags (e.g., Google's "restricted data processing" or Meta's "limited data use" flags) have configurable privacy-protective settings that businesses had enabled only for states with enacted privacy statutes, leaving New York users unprotected.

5. **Incomplete understanding of tag data collection.** Companies often deploy third-party tags without fully understanding what data those tags collect, transmit, or share with the tag provider. The guide recommends periodic audits of each tag's data practices.

6. **Cookieless tracking.** Beyond HTTP cookies, websites increasingly use fingerprinting, local storage objects, and other persistent identifiers that are not cookie-based and therefore evade standard cookie-blocking controls. Privacy representations that omit cookieless tracking methods may be inaccurate.

The Business Guide recommends that companies: (a) designate a qualified individual with training on tracking technologies and privacy policies; (b) establish an intake process for adding new tags; (c) maintain a complete inventory of all tags deployed on each page; (d) configure and categorize all tags within the CMP; (e) test privacy controls before and after any tag changes; and (f) ensure that opt-out signals are properly passed from the CMP through the TMS to each individual tag.

### The Consumer Guide to Web Tracking [HIGH confidence]

The [Consumer Guide](https://ag.ny.gov/publications/consumer-guide-web-tracking) is a plain-language document explaining to New York consumers: (a) how websites track activity using cookies, pixels, and other technologies; (b) how to use a website's opt-out controls; (c) how to use browser-level privacy settings; and (d) limitations of opt-out controls (for instance, opting out may stop new cookies from being set but will not delete existing cookies). The guide does not create affirmative legal rights for consumers beyond what GBL § 349 already provides.

### Legal Authority and Enforcement Framework [HIGH confidence]

The OAG's stated position, as reflected in the Business Guide and [confirmed by multiple law firm analyses](https://www.alstonprivacy.com/new-york-attorney-general-investigates-companies-for-website-tags-publishes-guidelines-on-online-tracking-technologies/), is that:

> "Statements about when and how website visitors are tracked should be accurate, and privacy controls should work as described."

This is grounded in [GBL § 349](https://law.justia.com/codes/new-york/gbs/article-22-a/349/), which makes unlawful "deceptive acts or practices in the conduct of any business, trade or commerce." The AG does not require proof of consumer harm to bring an enforcement action; the deceptive nature of the practice itself is the violation. Civil penalties can reach $5,000 per violation, and the OAG may seek injunctive relief and restitution.

As noted by [Alston & Bird](https://www.alstonprivacy.com/new-york-attorney-general-investigates-companies-for-website-tags-publishes-guidelines-on-online-tracking-technologies/), the Business Guide "effectively creates a compliance standard that, if not followed, could subject companies to enforcement action under New York's consumer protection laws." The [Sidley Austin Data Matters blog](https://datamatters.sidley.com/2024/08/13/new-york-attorney-general-publishes-guide-to-avoid-key-mistakes-regarding-online-tracking-technologies/) similarly characterizes the guides as conveying that the OAG "intends to enforce online cookie practices even absent a comprehensive state privacy law."

[McDermott Will & Emery](https://www.mcdermottlaw.com/insights/new-york-attorney-general-issues-cookie-guidance-and-enforcement-warnings/) characterized the guides as "cookie guidance and enforcement warnings," underscoring that the publication serves a dual purpose: providing compliance clarity while signaling enforcement intent to the regulated community.

## Impact Assessment [MEDIUM confidence]

### Affected Entities

The guidance applies to any company that: (a) operates a website serving New York consumers; (b) deploys third-party cookies, pixels, tags, or other tracking technologies on that website; and (c) makes privacy representations to users (e.g., through a privacy policy, cookie notice, or consent banner) regarding those technologies. Given New York's status as a major commercial market, practically any substantial US or multinational consumer-facing business is within scope.

The investigation targeted e-commerce sites in apparel, publishing, and live events. However, the legal theory — deceptive representations about privacy controls — applies across sectors including retail, media, finance, healthcare, and software-as-a-service.

### Compliance Requirements

The Business Guide does not establish binding regulations, but the OAG's characterization of the identified practices as potentially violating GBL § 349 creates a de facto compliance standard. Key compliance requirements implied by the guide:

- **Tag inventory and governance:** Maintain a comprehensive, up-to-date inventory of all tracking technologies deployed across the website, including their categorization, data flows, and third-party recipients.
- **CMP and TMS integration:** Ensure that consent management and tag management systems are properly configured so that user opt-out choices are honored end-to-end. Test this integration regularly.
- **Hardcoded tag audit:** Identify and remove or CMP-gate any hardcoded tags that bypass the TMS.
- **Tag-level privacy settings:** Enable privacy-protective settings (e.g., "restricted data processing") for all third-party tags, not just in states with comprehensive privacy laws.
- **Accurate privacy disclosures:** Ensure that the website's privacy policy and cookie notice accurately describe all tracking technologies in use, including cookieless tracking methods.
- **Responsible person designation:** Assign a knowledgeable individual with accountability for tracking technology compliance.

There are no statutory deadlines imposed by this guidance. The compliance expectation, based on the OAG's enforcement posture, is immediate.

### Enforcement Outlook

The publication of guidance prior to enforcement is consistent with the OAG's approach in other contexts (e.g., SHIELD Act compliance guidance was published well before enforcement actions). The New York AG has demonstrated willingness to pursue privacy and cybersecurity enforcement under existing consumer protection laws. The fact that the OAG investigated 13 websites and obtained voluntary remediation before publishing the guides suggests that the primary enforcement mechanism at this stage is informal (investigation followed by demand letters), with formal enforcement reserved for egregious or unresponsive cases.

As noted by [Koley Jessen](https://www.koleyjessen.com/insights/publications/new-york-attorney-general-releases-website-privacy-guidance-for-companies-tracking-users-online/), the broader national context — including state privacy law patchwork considerations, California Invasion of Privacy Act (CIPA) litigation, and international GDPR/ePrivacy obligations — means that companies addressing these guides should do so as part of an integrated tracking technology compliance program rather than as a New York-specific exercise.

## Action Items

- **Audit tracking technologies now.** Conduct an end-to-end audit of all cookies, pixels, tags, and other tracking technologies deployed on any consumer-facing website, with particular attention to third-party tags managed via a TMS.
- **Test CMP/TMS integration.** Simulate a user opting out via the consent banner and verify through network traffic analysis that marketing/advertising tags cease firing. Confirm that opt-out signals pass from the CMP through to each individual tag.
- **Inventory and categorize all tags.** Ensure every tag in the TMS is assigned to a category (e.g., necessary, analytics, marketing). Remove or quarantine uncategorized tags.
- **Audit for hardcoded tags.** Review page source code and third-party script loading for any tags not managed through the TMS. Bring them under CMP control or remove them.
- **Enable tag-level privacy settings universally.** For tags from providers such as Google or Meta that offer privacy-protective processing modes, enable those settings for all users globally, not only those in states with comprehensive privacy laws.
- **Update privacy disclosures.** Confirm that the privacy policy and cookie notice accurately describe all tracking technologies in use, including any cookieless or fingerprinting-based tracking.
- **Designate a compliance owner.** Identify a qualified person responsible for tracking technology governance. Document policies for the intake, categorization, testing, and retirement of website tags.
- **Monitor for OAG enforcement developments.** The New York AG has signaled ongoing scrutiny of website tracking. Monitor for any subsequent enforcement actions or additional guidance that refines the compliance standard.

## Related Reports

- [reports/privacy/enforcement-actions/nj-tx-ag-privacy-enforcement-team-2024-05-28.md](reports/privacy/enforcement-actions/nj-tx-ag-privacy-enforcement-team-2024-05-28.md) — Covers the concurrent build-out of dedicated privacy enforcement teams at the New Jersey and Texas AG offices, illustrating the multi-state AG enforcement trend that contextualizes the New York OAG's proactive website-tracking investigation.
- [reports/privacy/litigation/arizona-tucsr-spy-pixel-class-action-2024-05-30.md](reports/privacy/litigation/arizona-tucsr-spy-pixel-class-action-2024-05-30.md) — Details the Arizona tracking pixel class action wave under the TUCSR Act, which demonstrates parallel private litigation risk arising from the same cookie and pixel tracking practices addressed by the New York AG guidance.
- [reports/privacy/litigation/washington-overlake-hospital-pixel-privacy-2024-06-07.md](reports/privacy/litigation/washington-overlake-hospital-pixel-privacy-2024-06-07.md) — Covers a federal court dismissal of pixel tracking privacy claims in the healthcare context, relevant to understanding the legal treatment of the same tracking technologies addressed in the New York guides.
- [reports/privacy/enforcement-actions/california-cppa-enforcement-advisory-data-minimization-2024-04-02.md](reports/privacy/enforcement-actions/california-cppa-enforcement-advisory-data-minimization-2024-04-02.md) — The California CPPA's enforcement advisory on data minimization addresses the same category of third-party tag and analytics data collection practices that the New York guides target.

## Sources

1. [Attorney General James Launches Website Privacy Guides for New York Consumers and Businesses](https://ag.ny.gov/press-release/2024/attorney-general-james-launches-website-privacy-guides-new-york-consumers-and) — Official OAG press release announcing the guides and summarizing the investigation findings.
2. [Business Guide to Website Privacy Controls](https://ag.ny.gov/resources/organizations/business-guidance/website-privacy-controls) — Official OAG business-facing guide identifying six categories of common mistakes and compliance recommendations.
3. [A Consumer Guide to Web Tracking](https://ag.ny.gov/publications/consumer-guide-web-tracking) — Official OAG consumer-facing guide explaining how website tracking works and how to limit it.
4. [New York General Business Law § 349 (Justia)](https://law.justia.com/codes/new-york/gbs/article-22-a/349/) — Statutory text of the consumer protection provision underlying the OAG's enforcement authority.
5. [NY AG Publishes Privacy Guides on Website Tracking — Hunton Andrews Kurth](https://www.hunton.com/privacy-and-cybersecurity-law-blog/ny-ag-publishes-privacy-guides-on-website-tracking) — Law firm client alert summarizing the guides and their compliance implications.
6. [New York AG Investigates Companies for Website Tags, Publishes Guidelines on Online Tracking Technologies — Alston & Bird](https://www.alstonprivacy.com/new-york-attorney-general-investigates-companies-for-website-tags-publishes-guidelines-on-online-tracking-technologies/) — Detailed law firm analysis of the investigation scope, key findings, and enforcement framing.
7. [New York AG Publishes Guide to Avoid "Key Mistakes" Regarding Online Tracking Technologies — Sidley Austin Data Matters](https://datamatters.sidley.com/2024/08/13/new-york-attorney-general-publishes-guide-to-avoid-key-mistakes-regarding-online-tracking-technologies/) — Sidley analysis highlighting the six key mistake categories and the GBL § 349 enforcement theory.
8. [New York AG Issues Cookie Guidance and Enforcement Warnings — McDermott Will & Emery](https://www.mcdermottlaw.com/insights/new-york-attorney-general-issues-cookie-guidance-and-enforcement-warnings/) — Law firm analysis framing the guides as both guidance and enforcement signals.
9. [New York AG Releases Website Privacy Guidance for Companies Tracking Users Online — Koley Jessen](https://www.koleyjessen.com/insights/publications/new-york-attorney-general-releases-website-privacy-guidance-for-companies-tracking-users-online/) — Analysis contextualizing the guides within the broader national privacy compliance landscape.
10. [Businesses Beware: New York Eyeing Privacy Regulation and Enforcement Even Absent Omnibus State Privacy Law — Privacy World (Troutman Pepper)](https://www.privacyworld.blog/2024/08/businesses-beware-new-york-eyeing-privacy-regulation-and-enforcement-even-absent-omnibus-state-privacy-law/) — Commentary on the OAG's enforcement posture in the absence of comprehensive state privacy legislation.
11. [SHIELD Act — New York State Attorney General](https://ag.ny.gov/resources/organizations/data-breach-reporting/shield-act) — Official OAG page on New York's data security law, providing background on the OAG's existing privacy enforcement framework.
12. [Attorney General James Secures $14.2 Million from Car Insurance Companies Over Data Breaches](https://ag.ny.gov/press-release/2025/attorney-general-james-secures-142-million-car-insurance-companies-over-data) — Example of OAG enforcement action under GBL § 349 and SHIELD Act demonstrating the agency's active enforcement posture.
