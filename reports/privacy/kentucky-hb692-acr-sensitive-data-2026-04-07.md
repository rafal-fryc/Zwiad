---
finding_id: "SCAN-20260407-009"
format: "research-memo"
date: "2026-04-07"
jurisdiction: "Kentucky"
category: "privacy"
development_type: "legislation"
cluster: "Kentucky HB 692: ACR Data Under KCDPA"
cluster_slug: "kentucky-hb-692-acr-kcdpa"
---

# Kentucky HB 692: Automatic Content Recognition Data Classified as Sensitive Under KCDPA

**Jurisdiction:** Kentucky | **Category:** Privacy | **Date:** 2026-04-07

## Executive Summary [HIGH confidence]

Kentucky enacted HB 692 on March 31, 2026, amending the Kentucky Consumer Data Protection Act (KCDPA, KRS 367.3611 et seq.) to classify automatic content recognition (ACR) data as sensitive personal data. The amendment requires smart TV and smart monitor manufacturers to obtain explicit consumer consent before collecting ACR data, which tracks what content users view by analyzing audio and video fingerprints. Kentucky is the first state to specifically target ACR technology in its comprehensive privacy law. The law takes effect [July 1, 2027](https://apps.legislature.ky.gov/record/26rs/hb692.html).

## Background [MEDIUM confidence]

### Automatic Content Recognition Technology

Automatic content recognition (ACR) is a technology embedded in smart TVs and monitors that periodically captures frames and audio from the display, builds a digital fingerprint, and matches it against a database of known content to identify what is being watched. According to [research published in 2024](https://arxiv.org/abs/2409.06203), smart TVs can capture screenshots as frequently as every 10 milliseconds and transmit viewing data to manufacturer servers every 15 to 60 seconds. Critically, ACR operates across every input source -- it tracks not only content streamed through built-in apps but also content from gaming consoles, laptops, and external streaming devices connected via HDMI. [TV manufacturers have built significant revenue streams from ACR data](https://www.securityweek.com/smart-tv-surveillance-how-samsung-and-lgs-acr-technology-tracks-what-you-watch/), using it to power targeted advertising, audience measurement, and content recommendations.

### Kentucky Consumer Data Protection Act (KCDPA)

Kentucky enacted its comprehensive consumer data privacy law (HB 15) in 2024, joining the wave of state-level privacy legislation modeled broadly on the Virginia Consumer Data Protection Act. The KCDPA [took effect January 1, 2026](https://www.akingump.com/en/insights/blogs/ag-data-dive/kentucky-data-protection-act-what-businesses-need-to-know). Under the existing law, "sensitive data" includes personal data revealing racial or ethnic origin, religious beliefs, mental or physical health diagnoses, sexual orientation, citizenship or immigration status, genetic or biometric data processed for unique identification, data collected from a known child, and [precise geolocation data](https://apps.legislature.ky.gov/law/Statutes/statute.aspx?id=55836). Controllers may not process sensitive data without first obtaining the consumer's consent -- an opt-in requirement that contrasts with the general opt-out framework governing other personal data under the KCDPA.

## Detailed Analysis [HIGH confidence]

### Key Provisions of HB 692

HB 692, sponsored by Representative Josh Branscum (R-Russell Springs) with co-sponsors Steve Bratcher and William Lawrence, amends [KRS 367.3611](https://apps.legislature.ky.gov/law/Statutes/statute.aspx?id=55836) in three material ways:

1. **Defines "automatic content recognition data"** as information collected by technology embedded in internet-connected smart televisions or smart monitors that identifies content being displayed by analyzing audio or video fingerprints, including content from streaming services and broadcasts ([HB 692 bill text](https://apps.legislature.ky.gov/recorddocuments/bill/26RS/hb692/bill.pdf)).

2. **Defines "smart monitor"** as a new term in the statute, expanding coverage beyond smart TVs to include internet-connected display devices with ACR capability.

3. **Adds ACR data to the "sensitive data" definition**, thereby triggering the KCDPA's opt-in consent requirement for any processing of ACR data.

### Legislative History

The bill was [introduced on February 23, 2026](https://fastdemocracy.com/bill-search/ky/2026RS/bills/KYB00019872/) and passed the House unanimously on March 13, 2026, with a vote of [92-0](https://apps.legislature.ky.gov/record/26RS/hb692/vote_history.pdf). It subsequently passed the Senate by consent on March 31, 2026, and was [enrolled into law](https://legiscan.com/KY/bill/HB692/2026). The unanimous passage suggests broad bipartisan support for ACR-specific privacy protections.

### First-in-Nation Status

Kentucky is the [first state to specifically target ACR surveillance technology](https://www.gblock.app/articles/kentucky-smart-tv-acr-consent-law) built into modern smart TVs within its comprehensive privacy law framework. While ACR data collection could arguably fall under existing KCDPA categories or FTC enforcement actions (such as the [2017 Vizio settlement](https://www.consumerreports.org/electronics/privacy/how-to-turn-off-smart-tv-snooping-features-a4840102036/)), HB 692 removes any ambiguity by creating an explicit statutory definition and classification.

## Impact Assessment [MEDIUM confidence]

### Affected Entities

The amendment directly impacts smart TV manufacturers (Samsung, LG, Vizio, TCL, and others), streaming device makers whose products connect to smart monitors, and the advertising technology companies that purchase ACR-derived viewing data. [The ACR data market is a significant revenue source for TV manufacturers](https://stateofsurveillance.org/articles/surveillance/smart-tv-surveillance-acr/), with some companies generating more revenue from data than from hardware sales.

### Compliance Requirements

Beginning July 1, 2027, any entity collecting ACR data from Kentucky consumers must obtain affirmative opt-in consent before processing. This aligns with how the KCDPA already treats other categories of sensitive data. Companies that currently rely on pre-checked boxes, buried settings, or default-on ACR must implement clear consent mechanisms for Kentucky consumers.

### Enforcement

The KCDPA is enforced exclusively by the [Kentucky Attorney General](https://www.ag.ky.gov/about/Office-Divisions/ODP/KCDPA/Pages/default.aspx), with no private right of action. Companies have a 30-day cure period before enforcement action. Violations are treated as unfair or deceptive trade practices under KRS Chapter 367.

## Action Items

- **Smart TV and monitor manufacturers** should audit current ACR consent flows for Kentucky consumers and implement opt-in mechanisms before July 1, 2027.
- **Ad-tech companies** receiving ACR data should verify that upstream data providers have obtained valid Kentucky consumer consent for ACR data processed after the effective date.
- **Privacy and compliance teams** should monitor whether other states introduce similar ACR-specific amendments to their privacy laws, as Kentucky's unanimous passage may encourage copycat legislation.
- **Legal teams** should review the full enrolled text of [HB 692](https://apps.legislature.ky.gov/recorddocuments/bill/26RS/hb692/bill.pdf) to assess whether the "smart monitor" definition captures any of their non-TV products.

## Related Reports

No related reports found in the knowledge base.

## Sources

1. [Kentucky Legislature -- 26RS HB 692](https://apps.legislature.ky.gov/record/26rs/hb692.html) -- Official bill record page with status and history
2. [HB 692 Bill Text (PDF)](https://apps.legislature.ky.gov/recorddocuments/bill/26RS/hb692/bill.pdf) -- Full enrolled text of the legislation
3. [KRS 367.3611 -- Definitions](https://apps.legislature.ky.gov/law/Statutes/statute.aspx?id=55836) -- Current statutory text of the KCDPA definitions section
4. [HB 692 Vote History (PDF)](https://apps.legislature.ky.gov/record/26RS/hb692/vote_history.pdf) -- House vote record showing 92-0 passage
5. [FastDemocracy -- KY HB 692 Tracking](https://fastdemocracy.com/bill-search/ky/2026RS/bills/KYB00019872/) -- Bill tracking with timeline and summary
6. [LegiScan -- Kentucky HB692](https://legiscan.com/KY/bill/HB692/2026) -- Bill tracking confirming enrollment
7. [Frankfort Today -- Kentucky House Passes Bill to Protect Smart TV Data Privacy](https://nationaltoday.com/us/ky/frankfort/news/2026/03/17/kentucky-house-passes-bill-to-protect-smart-tv-data-privacy/) -- News coverage of House passage
8. [GBlock -- Kentucky Just Made It Illegal for Your Smart TV to Spy on You Without Asking](https://www.gblock.app/articles/kentucky-smart-tv-acr-consent-law) -- Analysis of the law's first-in-nation status
9. [SecurityWeek -- Smart TV Surveillance: ACR Technology](https://www.securityweek.com/smart-tv-surveillance-how-samsung-and-lgs-acr-technology-tracks-what-you-watch/) -- Technical background on ACR data collection
10. [arXiv -- Automatic Content Recognition Tracking in Smart TVs](https://arxiv.org/abs/2409.06203) -- Academic research on ACR tracking frequency and scope
11. [State of Surveillance -- Smart TV Surveillance 2025](https://stateofsurveillance.org/articles/surveillance/smart-tv-surveillance-acr/) -- Analysis of ACR data collection practices
12. [Consumer Reports -- How to Turn Off Smart TV Snooping](https://www.consumerreports.org/electronics/privacy/how-to-turn-off-smart-tv-snooping-features-a4840102036/) -- Consumer guidance on ACR opt-out
13. [Akin Gump -- Kentucky Data Protection Act](https://www.akingump.com/en/insights/blogs/ag-data-dive/kentucky-data-protection-act-what-businesses-need-to-know) -- Law firm analysis of the KCDPA
14. [Kentucky Attorney General -- KCDPA Page](https://www.ag.ky.gov/about/Office-Divisions/ODP/KCDPA/Pages/default.aspx) -- Official enforcement authority information
