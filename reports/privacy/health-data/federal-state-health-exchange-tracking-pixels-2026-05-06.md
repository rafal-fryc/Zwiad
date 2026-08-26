---
title: "State Health Insurance Exchanges Sharing Sensitive User Data with Big Tech via Ad Trackers"
date: 2026-05-06
jurisdiction: "Federal"
category: "privacy"
development_type: "other"
finding_id: "SCAN-20260508-014"
topic_key: "federal-0f440ca5-2026"
topic_type: "guidance"
first_reported: 2026-05-06
last_updated: 2026-05-08
status_history: []
cluster: "State Health Insurance Exchange Ad Tracker Data Sharing (Bloomberg Investigation)"
cluster_slug: "state-aca-exchange-tracking-pixel-data-sharing"
---

# State Health Insurance Exchanges Sharing Sensitive User Data with Big Tech via Ad Trackers

**Jurisdiction:** Federal / Multi-state | **Category:** Privacy | **Date:** 2026-05-06

## Executive Summary [HIGH confidence]

A [Bloomberg investigation published May 4, 2026](https://www.bloomberg.com/features/2026-healthcare-advertising-trackers-privacy/) found that nearly all of the 20 U.S. state-run health insurance exchanges plus the Washington, D.C. exchange were transmitting sensitive user data to major technology companies — including Meta, TikTok, Google, Snap, and Microsoft's LinkedIn — through advertising tracking pixels embedded in their websites. The data shared includes highly sensitive categories: race and citizenship status, immigration information, ZIP codes, names of prescription drugs and dosages, names of physicians and hospitals previously visited, and disclosures about incarcerated family members. More than 7 million Americans used these exchanges to purchase health insurance for 2026, meaning a substantial population was exposed to undisclosed data sharing during a sensitive enrollment process. The investigation exposes a significant regulatory gap: state health insurance exchanges are not themselves HIPAA-covered entities, leaving users without robust federal privacy protections despite the sensitive nature of data collected on enrollment sites. Several states removed specific trackers after Bloomberg contacted them for comment, but no federal enforcement action or legislative response has been announced.

## Background [HIGH confidence]

State health insurance exchanges were established under the Affordable Care Act (ACA) to allow individuals and families to shop for and purchase health insurance plans. As of 2026, approximately 20 states operate their own state-based exchanges (SBEs) rather than using the federal HealthCare.gov platform. These exchanges collect detailed personal and health-related information from applicants during the enrollment process, including demographic information, household composition, income, immigration status, and health needs.

Advertising tracking pixels — small snippets of JavaScript code embedded in websites — are a standard tool used across the internet to measure advertising campaign effectiveness, track site visitors, and enable retargeted advertising. Exchanges embedded these technologies purportedly to measure marketing campaigns and recruit uninsured individuals to enroll in coverage.

The use of tracking pixels in healthcare contexts has been a recurring regulatory concern since at least 2021. In June 2022, [The Markup first reported](https://themarkup.org/pixel-hunt/2022/06/16/facebook-is-receiving-sensitive-medical-information-from-hospital-websites) widespread use of the Meta pixel on hospital websites, triggering congressional inquiries and prompting multiple health systems to remove the trackers. In July 2023, the [FTC and HHS jointly warned approximately 130 hospital systems and telehealth providers](https://www.ftc.gov/news-events/news/press-releases/2023/07/ftc-hhs-warn-hospital-systems-telehealth-providers-about-privacy-security-risks-online-tracking) that pixel-based tracking technologies on patient-facing pages risked HIPAA and consumer protection violations. A separate investigation by [The Markup in 2025 found 4 additional states sharing personal health data](https://themarkup.org/pixel-hunt/2025/06/17/we-caught-4-more-states-sharing-personal-health-data-with-big-tech) through similar mechanisms, demonstrating a persistent and previously underaddressed sector gap.

The regulatory landscape governing tracking pixels in healthcare underwent significant change in June 2024. In [*American Hospital Association v. Becerra*](https://www.aha.org/legal-documents/2024-06-29-opinion-order-american-hospital-association-et-al-v-xavier-becerra-et-al), a federal district court in the Northern District of Texas struck down the portion of HHS Office for Civil Rights' December 2022 HIPAA tracking technology bulletin that had extended HIPAA obligations to data collected on unauthenticated public webpages. HHS [declined to appeal](https://www.aha.org/news/headline/2024-08-29-hhs-will-not-appeal-aha-court-victory-online-tracking-case) the ruling, leaving a significant gap in the federal framework. Bloomberg's investigation notes that hospital tracker prevalence dropped from approximately 98% in 2021 to 30% in 2025 — driven by litigation threat, not regulatory action — while state exchange adoption of trackers remained largely unaddressed.

## Detailed Analysis [HIGH confidence]

### Scope and Nature of Data Shared

Bloomberg reviewed thousands of enrollment and informational webpages across 20 state exchanges plus D.C. and found personal data being transmitted to advertising platforms on many of them. The investigation identified the following specific examples, as reported by [TechCrunch](https://techcrunch.com/2026/05/04/us-healthcare-marketplaces-shared-citizenship-and-race-data-with-ad-tech-giants/) and corroborated by [CyberNews](https://cybernews.com/news/states-healthcare-user-data-big-tech/) and [SC Media](https://www.scworld.com/brief/u-s-state-health-insurance-marketplaces-shared-user-data-with-tech-giants/):

- **Washington State:** The exchange sent applicants' sex and citizenship responses to TikTok, along with race data the tracker failed to filter out.
- **Virginia:** The premium estimation tool sent ZIP codes to Meta.
- **New York:** The marketplace shared pages visited during enrollment — including pages where applicants disclosed incarcerated family members — with TikTok, Meta, Snap, and LinkedIn.
- **Nevada:** Nevada Health Link transmitted the names and dosages of medications (e.g., Fluoxetine/Prozac) entered by applicants to LinkedIn and Snapchat.
- **Maine:** CoverME.gov sent names of prescription drugs and dosages to Google Analytics, along with names of doctors and hospitals applicants had previously visited.

Bloomberg confirmed that visits to at least ten exchange sites were linkable to a journalist's Facebook account, meaning Meta was receiving and retargeting specific individuals based on their insurance enrollment activity — without those individuals' knowledge.

### The Regulatory Gap: Why Exchanges Are Not HIPAA-Covered Entities

A critical and underappreciated aspect of this story is that state health insurance exchanges are generally not considered [HIPAA covered entities](https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html) under the current regulatory framework. HIPAA applies to health plans, healthcare clearinghouses, and healthcare providers — categories that describe the insurers selling coverage through the exchanges, not the exchanges themselves. As [Fierce Healthcare has reported](https://www.fiercehealthcare.com/payer/does-hipaa-apply-to-health-insurance-exchanges), the ACA exchange rule established privacy protections separate from HIPAA, but with smaller penalties and without mandatory breach notification to regulators.

This gap means data flowing from exchange websites to third-party ad platforms falls outside HHS enforcement jurisdiction. Moreover, the June 2024 ruling in *AHA v. Becerra* reinforced that even the partial HIPAA extension HHS attempted to impose via guidance on unauthenticated public webpages was unlawful.

### FTC's Health Breach Notification Rule: Partial Coverage

The FTC's [Health Breach Notification Rule](https://www.ftc.gov/legal-library/browse/rules/health-breach-notification-rule) (16 C.F.R. Part 318), amended in [April 2024](https://www.ftc.gov/news-events/news/press-releases/2024/04/ftc-finalizes-changes-health-breach-notification-rule) and [effective July 29, 2024](https://www.federalregister.gov/documents/2024/05/30/2024-10855/health-breach-notification-rule), provides a potential hook for FTC jurisdiction. The 2024 amendments broadened the Rule to cover vendors of personal health records and PHR-related entities, and clarified that unauthorized disclosures — not just data breaches — trigger notification obligations. The Rule targets non-HIPAA covered entities collecting individually identifiable health information. Whether state-operated exchanges or the ad-tech vendors receiving pixel data qualify as "vendors of personal health records" or "PHR-related entities" under the Rule's definitions is unsettled, but the FTC has shown willingness to pursue pixel-related enforcement against health-adjacent entities in other contexts.

### Prior Enforcement Precedents

The FTC has pursued several enforcement actions relating to health data sharing with third-party advertising platforms:
- **GoodRx (2023):** The FTC settled with GoodRx for sharing health data with advertising platforms, imposing a $1.5 million penalty — the first action under the Health Breach Notification Rule.
- **BetterHelp (2023):** The FTC ordered BetterHelp to pay $7.8 million and prohibited sharing health data with advertising platforms.
- **Kochava (2026):** The FTC settled with Kochava, prohibiting it from selling sensitive consumer location data without affirmative express consumer consent, demonstrating continued agency focus on data broker practices involving sensitive personal information.

These precedents signal that the FTC views the unauthorized sharing of health-adjacent data with advertisers as an unfair trade practice under Section 5 of the FTC Act, regardless of HIPAA applicability.

### State Law Applicability

Multiple states have enacted health data privacy statutes that may apply independently of HIPAA. Washington State's [My Health My Data Act](https://app.leg.wa.gov/RCW/default.aspx?cite=19.373) (effective March 2024) applies broadly to consumer health data collected by entities without HIPAA coverage, with a private right of action. California's [Confidentiality of Medical Information Act (CMIA)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=56.10.) and the CCPA may impose additional obligations on health data handling for California residents. These state laws could provide bases for state AG enforcement or private litigation against exchanges that shared covered health data.

## Impact Assessment [MEDIUM confidence]

### Affected Entities

The primary subjects of concern are the state-operated health insurance exchanges found to have embedded tracking technologies that transmitted user data. Secondarily, the ad-tech companies — Meta, TikTok, Google, Snap, LinkedIn — that received this data face reputational scrutiny. Neither category has yet faced formal enforcement action in connection with this specific investigation.

The 7 million Americans who purchased health insurance through state exchanges in 2026 are the affected population. The sensitivity of the data involved — including immigration status, medication information, and family composition — creates meaningful risks of discriminatory targeting, government surveillance concerns in the current immigration enforcement climate, and insurance-related discrimination.

### Immediate State Responses

Several states removed specific trackers after Bloomberg contacted them for comment, including:
- **Washington State:** Paused its rollout of the TikTok tracker.
- **Virginia:** Removed the Meta pixel after Bloomberg identified ZIP code sharing.

These remediation steps are reactive rather than systemic. No state has yet announced a formal audit, rulemaking, or enforcement investigation in response to the Bloomberg report, based on available information at time of writing.

### Potential Regulatory and Legislative Consequences

The findings are likely to draw attention from congressional privacy advocates, though there is no confirmed congressional response as of this writing. Prior investigations into hospital pixel tracking prompted inquiry letters from senators including Sen. Mark Warner (D-VA) in 2022, and senators launched inquiries into telehealth companies in 2023, setting a precedent for legislative follow-up to investigative journalism in this space. Whether the current political environment will generate similar responses is uncertain.

At the state level, state attorneys general with broad consumer protection authority — particularly in states with health data statutes such as Washington, California, Connecticut, and Nevada — may investigate whether exchange operators or their technology vendors violated existing law. Washington's My Health My Data Act's private right of action also creates exposure to class action litigation.

The AHA v. Becerra ruling has significantly reduced OCR's enforcement options against exchanges directly, as they are not HIPAA covered entities to begin with and the broader principle of limiting HIPAA guidance expansion applies to the sector.

## Action Items

- **For state exchange operators:** Audit all third-party tracking technologies currently embedded in exchange websites and enrollment tools. Conduct a data inventory mapping which data elements are accessible to each tracker, and remove or reconfigure trackers that transmit health-adjacent, demographic, or immigration status data to advertising platforms. Review consent disclosures and privacy notices for accuracy.
- **For state attorneys general:** Assess whether exchange-based pixel tracking implicates state consumer protection, health data privacy, or unfair and deceptive practices statutes. States with MHMDA-style laws (Washington) or broad health privacy statutes (California, Nevada) have the strongest enforcement hooks.
- **For legal and compliance professionals:** Monitor for FTC enforcement activity under the 2024 Health Breach Notification Rule amendments — the unauthorized disclosure prong is newly actionable and the exchanges' sharing of health-adjacent data to ad platforms may meet the Rule's definitional thresholds. Advise non-HIPAA health data handlers accordingly.
- **For privacy advocates and policymakers:** The absence of a comprehensive federal consumer privacy law (APRA has not passed) continues to leave sensitive health data collected outside HIPAA-covered contexts without uniform protection. This investigation may revive momentum for targeted health data privacy legislation or FTC rulemaking.
- **Monitoring:** Watch for state legislative responses in session states, FTC investigation announcements, congressional inquiry letters, and class action filings in states with private rights of action over health data or consumer protection violations.

## Related Reports

- [reports/privacy/health-data/federal-health-data-security-overlay-2026-04-27.md](reports/privacy/health-data/federal-health-data-security-overlay-2026-04-27.md) — Covers new federal health data security rules layered over existing HIPAA obligations for health entities, directly relevant to the regulatory framework gap this investigation exposes.
- [reports/privacy/health-data/federal-ocr-hipaa-self-funded-plan-enforcement-2026-04-23.md](reports/privacy/health-data/federal-ocr-hipaa-self-funded-plan-enforcement-2026-04-23.md) — OCR HIPAA enforcement activity, relevant to understanding the limits of OCR's jurisdictional reach over exchange-adjacent entities post-AHA v. Becerra.
- [reports/privacy/litigation/massachusetts-doe-v-tenet-healthcare-pixel-tracking-2024-05-20.md](reports/privacy/litigation/massachusetts-doe-v-tenet-healthcare-pixel-tracking-2024-05-20.md) — Massachusetts federal court case allowing tracking pixel claims to proceed under wiretapping and other statutes, illustrating the litigation exposure for health entities using ad trackers.
- [reports/privacy/hhs-ocr-hipaa-risk-management-video-2026-04-12.md](reports/privacy/hhs-ocr-hipaa-risk-management-video-2026-04-12.md) — HHS OCR HIPAA security guidance, providing context for the HIPAA framework's current scope and limitations relative to exchange-site tracking.

## Sources

1. [Bloomberg: State Health Sites Send Race, Location, Immigration Data to Meta, TikTok (2026)](https://www.bloomberg.com/features/2026-healthcare-advertising-trackers-privacy/) — Primary investigation; key findings on data types, affected states, and state responses.
2. [TechCrunch: US healthcare marketplaces shared citizenship and race data with ad tech giants (May 4, 2026)](https://techcrunch.com/2026/05/04/us-healthcare-marketplaces-shared-citizenship-and-race-data-with-ad-tech-giants/) — Independent corroborating coverage of Bloomberg findings with additional detail on specific state examples.
3. [Bloomberg Law: TikTok, Meta Were Sent Personal Data From State Health Sites](https://news.bloomberglaw.com/insurance/tiktok-meta-were-sent-personal-data-from-state-health-sites) — Bloomberg Law coverage with insurance-sector framing and regulatory analysis.
4. [Gizmodo: Meta and TikTok Are Getting Your Data From State Healthcare Sites (2026)](https://gizmodo.com/meta-and-tiktok-are-getting-your-data-from-state-healthcare-sites-report-2000754335) — Secondary reporting confirming scope and state-specific findings.
5. [SC Media: U.S. state health insurance marketplaces reportedly shared user data with tech giants](https://www.scworld.com/brief/u-s-state-health-insurance-marketplaces-shared-user-data-with-tech-giants) — Cybersecurity-oriented coverage with additional detail on data categories.
6. [CyberNews: US states share your health data with Big Tech](https://cybernews.com/news/states-healthcare-user-data-big-tech/) — Independent corroborating report.
7. [The Markup: We caught 4 more states sharing personal health data with Big Tech (2025)](https://themarkup.org/pixel-hunt/2025/06/17/we-caught-4-more-states-sharing-personal-health-data-with-big-tech) — 2025 predecessor investigation documenting the same pattern in additional states.
8. [HHS: Use of Online Tracking Technologies by HIPAA Covered Entities and Business Associates](https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/hipaa-online-tracking/index.html) — Official HHS OCR guidance on tracking technologies and HIPAA applicability.
9. [AHA: Opinion & Order, American Hospital Association v. Becerra (N.D. Tex. June 20, 2024)](https://www.aha.org/legal-documents/2024-06-29-opinion-order-american-hospital-association-et-al-v-xavier-becerra-et-al) — Court order vacating HHS OCR's expansion of HIPAA to unauthenticated webpage tracking.
10. [Quarles Law: HHS Tracking Technology Guidance Vacated by Federal Court](https://www.quarles.com/newsroom/publications/hhs-tracking-technology-guidance-vacated-by-federal-court) — Law firm analysis of the AHA v. Becerra ruling and its implications.
11. [AHA News: HHS will not appeal AHA court victory in online tracking case (August 2024)](https://www.aha.org/news/headline/2024-08-29-hhs-will-not-appeal-aha-court-victory-online-tracking-case) — Confirmation that HHS declined to appeal, finalizing the regulatory rollback.
12. [FTC: FTC and HHS Warn Hospital Systems and Telehealth Providers about Privacy and Security Risks from Online Tracking Technologies (July 2023)](https://www.ftc.gov/news-events/news/press-releases/2023/07/ftc-hhs-warn-hospital-systems-telehealth-providers-about-privacy-security-risks-online-tracking) — Prior joint enforcement signal relevant to the regulatory posture toward pixel tracking in health contexts.
13. [FTC: FTC Finalizes Changes to the Health Breach Notification Rule (April 2024)](https://www.ftc.gov/news-events/news/press-releases/2024/04/ftc-finalizes-changes-health-breach-notification-rule) — 2024 HBNR amendments broadening coverage to unauthorized disclosures by non-HIPAA health entities.
14. [Federal Register: Health Breach Notification Rule Final Rule (May 30, 2024)](https://www.federalregister.gov/documents/2024/05/30/2024-10855/health-breach-notification-rule) — Official regulatory text of the 2024 HBNR amendments.
15. [Fierce Healthcare: Does HIPAA apply to health insurance exchanges?](https://www.fiercehealthcare.com/payer/does-hipaa-apply-to-health-insurance-exchanges) — Industry reporting on the exchange-HIPAA coverage gap.
16. [Holland & Knight: American Hospital Assn. v. Becerra — Are Tracking Tools OK Again?](https://www.hklaw.com/en/insights/publications/2024/06/american-hospital-assn-v-becerra-are-tracking-tools-ok-again) — Law firm analysis of AHA v. Becerra and post-ruling compliance landscape.
