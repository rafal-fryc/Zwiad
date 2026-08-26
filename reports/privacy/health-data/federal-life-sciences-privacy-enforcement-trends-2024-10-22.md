---
title: "Life Sciences Privacy and Cybersecurity Enforcement Trends: Key Risks for Pharma and Biotech (2024)"
date: 2024-10-22
jurisdiction: "Federal"
category: "privacy"
development_type: "guidance"
finding_id: "SCAN-20241022-016"
topic_key: "life-sciences-enforcement-trends-2024"
topic_type: "guidance"
first_reported: 2024-10-22
last_updated: 2026-04-16
status_history: []
cluster: "Life Sciences Privacy and Cybersecurity Enforcement Trends (2024)"
cluster_slug: "life-sciences-privacy-cybersecurity-enforcement-2024"
---

# Life Sciences Privacy and Cybersecurity Enforcement Trends: Key Risks for Pharma and Biotech (2024)

**Jurisdiction:** Federal, Massachusetts | **Category:** Privacy | **Date:** 2024-10-22

> **Note on Source:** This report was triggered by Morrison & Foerster's podcast series "When Your Life Sciences Are on the Line," which is primarily a law firm marketing and thought-leadership vehicle. The podcast episodes themselves do not constitute new regulatory developments. This memo synthesizes the underlying enforcement landscape the series addresses, sourcing primary and secondary authorities directly.

## Executive Summary [MEDIUM confidence]

Life sciences companies — pharmaceutical manufacturers, biotech firms, medical device makers, and digital health platforms — face a convergent set of privacy and cybersecurity enforcement pressures from multiple federal regulators and state attorneys general. The FTC's active enforcement under the [Health Breach Notification Rule (HBNR)](https://www.ftc.gov/legal-library/browse/rules/health-breach-notification-rule), HHS OCR's tracking-technology guidance (now partially vacated), a proposed overhaul of the HIPAA Security Rule, and DOJ's Civil Cyber-Fraud Initiative each represent distinct enforcement vectors that collectively raise the stakes for life sciences companies' data practices. These trends were the subject of a Morrison & Foerster podcast episode published October 22, 2024, hosted by former Acting U.S. Attorney for the District of Massachusetts Nate Mendell — but the underlying regulatory actions are documented in primary government sources and summarized here.

## Background [HIGH confidence]

Life sciences companies occupy an unusual position in health-data regulation. Many are not HIPAA "covered entities" (health plans, clearinghouses, healthcare providers) but nonetheless handle sensitive health and biometric data through clinical trials, patient support programs, direct-to-consumer health applications, and co-pay assistance portals. This gap between HIPAA coverage and the actual data practices of the industry has driven regulatory creativity: the FTC, state attorneys general, and the SEC have each asserted jurisdiction over health-data practices using authorities independent of HIPAA.

The regulatory landscape accelerated markedly in 2022–2024:

- **FTC health data enforcement** — In 2023, the FTC pursued three landmark enforcement actions against companies that disclosed consumer health information to advertising platforms via tracking technologies. GoodRx ($1.5 million) and Premom ($100,000 FTC civil penalty, plus $100,000 to state AGs in D.C., Connecticut, and Oregon) were charged under the Health Breach Notification Rule (HBNR) for unauthorized disclosure of health information. BetterHelp ($7.8 million in consumer refunds) was charged separately under FTC Act Section 5 for unfair and deceptive practices — it was not an HBNR action. Together, these cases signaled that the FTC would aggressively pursue pixel-driven health data sharing across multiple legal theories. Final amendments to the HBNR, effective [July 29, 2024](https://www.federalregister.gov/documents/2024/05/30/2024-10855/health-breach-notification-rule), codified this interpretation and extended coverage explicitly to health apps and connected devices.

- **HHS OCR tracking-technology guidance** — In December 2022, OCR issued a bulletin on [HIPAA obligations when using online tracking technologies](https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/hipaa-online-tracking/index.html) (pixels, cookies, analytics). OCR updated the guidance on March 18, 2024, but a [June 20, 2024 ruling](https://www.nixonpeabody.com/insights/alerts/2024/07/03/portions-of-ocrs-bulletin-on-online-tracking-technologies-deemed-unlawful) by the U.S. District Court for the Northern District of Texas vacated the guidance to the extent it covered unauthenticated public webpages, narrowing OCR's reach for non-patient-portal contexts.

- **State-level consumer health data laws** — Washington's [My Health My Data Act](https://app.leg.wa.gov/RCW/default.aspx?cite=19.373&full=true) (effective March 31, 2024; June 30, 2024 for small businesses) and Nevada's similar statute imposed broad consumer health data protections beyond HIPAA's scope, directly affecting life sciences companies with consumer-facing digital products in those states.

## Detailed Analysis [MEDIUM confidence]

### FTC Health Breach Notification Rule (HBNR) Enforcement

The FTC's HBNR enforcement posture is the most direct threat to non-HIPAA-covered life sciences companies. The [GoodRx](https://www.ftc.gov/news-events/news/press-releases/2023/02/ftc-enforcement-action-bar-goodrx-sharing-consumers-sensitive-health-info-advertising) and [Premom](https://www.ftc.gov/news-events/news/press-releases/2023/05/ovulation-tracking-app-premom-will-be-barred-sharing-health-data-advertising-under-proposed-ftc) enforcement actions — the FTC's first-ever HBNR cases — established that:

1. Disclosing identifiable health information to advertising platforms (Meta Pixel, Google Analytics, etc.) without consumer authorization constitutes a "breach of security" under the HBNR, regardless of whether there was a data breach in the traditional sense.
2. The FTC views third-party tracking pixels embedded in health-related digital properties as a per se data-sharing mechanism requiring scrutiny.
3. The [2024 HBNR final rule amendments](https://www.dwt.com/blogs/privacy--security-law-blog/2024/05/ftc-finalizes-hbnr-to-cover-health-app-breaches) broadened coverage to health apps, connected devices, and similar technologies, making clear that pharma and biotech companies with patient-facing digital products are within scope.

The FTC also pursued [BetterHelp](https://www.ftc.gov/news-events/news/press-releases/2023/03/ftc-takes-action-against-betterhelp-sharing-consumers-sensitive-mental-health-information) under a distinct legal theory: FTC Act Section 5 (unfair and deceptive practices), not the HBNR. BetterHelp agreed to $7.8 million in consumer refunds for sharing mental health data with advertising platforms contrary to its privacy promises. The BetterHelp action is significant because it demonstrates that the FTC does not need to invoke the HBNR to pursue health data misuse — Section 5 provides an independent basis, particularly where companies make specific privacy representations to consumers.

For life sciences companies, this dual-track enforcement (HBNR for qualifying health vendors; Section 5 for any company making privacy representations) translates to risk at patient assistance portals, condition-specific websites, clinical trial recruitment pages, and any consumer-facing health application that integrates advertising or analytics technology.

### HHS OCR Tracking Technology Guidance and Litigation

OCR's [March 2024 updated bulletin](https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/hipaa-online-tracking/index.html) maintained that HIPAA-covered entities and their business associates must apply Security Rule safeguards to any ePHI potentially collected by tracking technologies. The guidance remained highly consequential for covered healthcare providers and health plans in the life sciences supply chain.

However, the [June 2024 federal court decision](https://hhhealthlawblog.com/court-vacates-hipaa-online-tracking-guidance/) vacating part of the bulletin introduced uncertainty: OCR's guidance no longer applies to unauthenticated public webpages. For authenticated patient portals and health applications requiring login, HIPAA obligations remain fully in force. This creates a bifurcated compliance landscape that life sciences companies must navigate carefully.

OCR also announced that HIPAA Security Rule compliance is an [enforcement priority for investigations](https://www.mofo.com/resources/insights/240329-ocr-updates-guidance-on-use-of-online-tracking-technologies) involving tracking technologies, even post-litigation.

### HIPAA Security Rule NPRM (December 2024)

On December 27, 2024, HHS OCR published a [Notice of Proposed Rulemaking (NPRM)](https://www.federalregister.gov/documents/2025/01/06/2024-30983/hipaa-security-rule-to-strengthen-the-cybersecurity-of-electronic-protected-health-information) proposing the first major overhaul of the HIPAA Security Rule since 2013. Key proposed changes include:

- Elimination of the "addressable" vs. "required" implementation specification distinction — all specifications would become required with limited exceptions
- Mandatory encryption of ePHI at rest and in transit
- Mandatory multi-factor authentication (MFA)
- Vulnerability scanning at least every six months
- Penetration testing at least annually
- Written, tested, and regularly updated policies and procedures

The public comment period closed March 7, 2025. Life sciences companies that are HIPAA business associates — including contract research organizations (CROs), data analytics vendors, and technology providers to health systems — face significantly heightened technical requirements if finalized.

### DOJ Civil Cyber-Fraud Initiative

DOJ's [Civil Cyber-Fraud Initiative](https://www.foley.com/insights/publications/2024/08/doj-cybersecurity-enforcement-false-claims-act/), launched in 2021, uses the False Claims Act (FCA) to pursue cybersecurity violations by federal contractors and grantees. In 2024, several significant settlements underscore the initiative's scope:

- A **$2.7 million settlement with Insight Global LLC** (May 2024) for failing to implement sufficient cybersecurity measures to protect health information in COVID-19 contact tracing work.
- An **$11.3 million settlement** with consulting firms for FCA violations tied to cybersecurity failures in a federally-funded rental assistance program.

For life sciences companies that receive federal grants (NIH, BARDA, ARPA-H) or hold federal contracts (VA, DOD drug procurement, government clinical trials), cybersecurity failures can now generate FCA liability, dramatically expanding the potential financial consequences beyond HIPAA civil monetary penalties.

### SEC Cybersecurity Rules and Life Sciences

The SEC's cybersecurity disclosure rules, effective December 2023, require public companies to disclose material cybersecurity incidents within four business days and provide annual disclosures on cybersecurity risk management, strategy, and governance. For publicly traded life sciences companies, an October 2024 [Morrison & Foerster podcast episode](https://podcasts.apple.com/ca/podcast/when-your-life-sciences-are-on-the-line-cybersecurity/id1519312958?i=1000673344778) specifically addressed how these rules interact with life sciences sector vulnerabilities. The rules are not unique to life sciences but carry outsized risk in the sector given the sensitivity of clinical and patient data.

## Impact Assessment [MEDIUM confidence]

**Affected entities:** Pharmaceutical manufacturers, biotech companies, medical device makers, digital health platform operators, contract research organizations (CROs), and any life sciences company operating consumer-facing digital properties or holding federal contracts. Companies with patient support programs, co-pay portals, or disease-awareness websites are specifically at risk for FTC/HBNR exposure.

**Compliance requirements and timelines:**
- FTC HBNR amended rule: effective July 29, 2024 — compliance required now
- HIPAA tracking technology guidance: apply to authenticated portals now; unauthenticated public pages governed by updated (post-litigation) OCR interpretation
- HIPAA Security Rule NPRM: proposed, not final; comment period closed March 7, 2025; watch for final rule
- SEC cybersecurity disclosure rules: in effect since December 2023 for public companies

**Enforcement outlook:** Enforcement is active and converging. The FTC has signaled continued HBNR enforcement with the 2024 rule expansion, and pursues health data misuse under FTC Act Section 5 where HBNR does not apply. OCR has committed to making tracking-technology compliance an enforcement priority. DOJ's Civil Cyber-Fraud Initiative is expanding FCA liability into cybersecurity. The Massachusetts U.S. Attorney's Office — where former Acting U.S. Attorney Mendell served — has historically been among the most active in healthcare fraud enforcement, including False Claims Act actions.

## Action Items

- Audit all consumer-facing digital properties (patient portals, disease awareness sites, co-pay portals, clinical trial recruitment pages) for pixel and SDK integrations that may transmit health-related signals to advertising platforms.
- Assess applicability of the FTC Health Breach Notification Rule: if the company operates a health app, connected device, or consumer health platform, the amended HBNR applies. Separately assess FTC Act Section 5 exposure for any company making privacy representations to consumers about health data handling.
- For HIPAA business associates (CROs, data vendors, technology providers to health plans): review the HIPAA Security Rule NPRM and assess gap against proposed mandatory technical safeguards (encryption, MFA, pen testing).
- Review federal contract and grant portfolio for cybersecurity compliance certifications; assess FCA exposure under DOJ's Civil Cyber-Fraud Initiative.
- Public companies: confirm SEC cybersecurity incident reporting procedures are in place; verify board-level cybersecurity oversight documentation is ready for annual reporting.
- Monitor OCR's revised tracking technology guidance and any further litigation affecting its scope.
- Monitor the HIPAA Security Rule NPRM for a final rule (expected 2025–2026).

## Related Reports

- [reports/privacy/health-data/federal-washington-healthcare-update-may22-2024.md](../health-data/federal-washington-healthcare-update-may22-2024.md) — Covers related federal and Washington state healthcare privacy developments.
- [reports/privacy/health-data/federal-cms-healthcare-privacy-2024-04-17.md](../health-data/federal-cms-healthcare-privacy-2024-04-17.md) — Federal CMS healthcare privacy update with overlapping HIPAA enforcement context.
- [reports/privacy/enforcement-actions/ftc-match-okcupid-clarifai-enforcement-2026-04-07.md](../enforcement-actions/ftc-match-okcupid-clarifai-enforcement-2026-04-07.md) — FTC enforcement actions involving health and sensitive data sharing with advertising platforms.

## Sources

1. [When Your Life Sciences Are on the Line: Privacy and Security Enforcement Trends | Morrison Foerster](https://www.mofo.com/resources/podcasts/240603-when-your-life-sciences-are) — Primary MoFo podcast page covering privacy and security enforcement trends for life sciences companies.
2. [When Your Life Sciences Are on the Line: Cybersecurity (Apple Podcasts)](https://podcasts.apple.com/ca/podcast/when-your-life-sciences-are-on-the-line-cybersecurity/id1519312958?i=1000673344778) — October 2024 episode on SEC cybersecurity rules and life sciences governance.
3. [Health Breach Notification Rule | FTC](https://www.ftc.gov/legal-library/browse/rules/health-breach-notification-rule) — Official FTC page for the Health Breach Notification Rule, including 2024 amendments.
4. [Updated FTC Health Breach Notification Rule (FTC Blog, April 2024)](https://www.ftc.gov/business-guidance/blog/2024/04/updated-ftc-health-breach-notification-rule-puts-new-provisions-place-protect-users-health-apps) — FTC explanation of the 2024 HBNR amendments covering health apps and devices.
5. [Health Breach Notification Rule Final Rule, Federal Register](https://www.federalregister.gov/documents/2024/05/30/2024-10855/health-breach-notification-rule) — Official Federal Register publication of the 2024 HBNR final rule, effective July 29, 2024.
6. [FTC Enforcement Action to Bar GoodRx from Sharing Consumers' Sensitive Health Info](https://www.ftc.gov/news-events/news/press-releases/2023/02/ftc-enforcement-action-bar-goodrx-sharing-consumers-sensitive-health-info-advertising) — Official FTC press release on the GoodRx HBNR enforcement action.
7. [Ovulation Tracking App Premom Will be Barred from Sharing Health Data for Advertising | FTC](https://www.ftc.gov/news-events/news/press-releases/2023/05/ovulation-tracking-app-premom-will-be-barred-sharing-health-data-advertising-under-proposed-ftc) — Official FTC press release on the Premom HBNR enforcement action ($100,000 FTC civil penalty; $100,000 additional to state AGs).
8. [FTC Takes Action Against BetterHelp for Sharing Consumers' Sensitive Mental Health Information | FTC](https://www.ftc.gov/news-events/news/press-releases/2023/03/ftc-takes-action-against-betterhelp-sharing-consumers-sensitive-mental-health-information) — Official FTC press release on the BetterHelp Section 5 enforcement action (not HBNR).
9. [FTC and HHS Warn Hospital Systems and Telehealth Providers about Tracking Technologies | FTC](https://www.ftc.gov/news-events/news/press-releases/2023/07/ftc-hhs-warn-hospital-systems-telehealth-providers-about-privacy-security-risks-online-tracking) — Joint FTC/HHS advisory on tracking technology privacy risks.
10. [Use of Online Tracking Technologies by HIPAA Covered Entities and Business Associates | HHS.gov](https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/hipaa-online-tracking/index.html) — Official HHS OCR tracking technology guidance bulletin (updated March 2024).
11. [Portions of OCR's Bulletin on Online Tracking Technologies Deemed Unlawful | Nixon Peabody](https://www.nixonpeabody.com/insights/alerts/2024/07/03/portions-of-ocrs-bulletin-on-online-tracking-technologies-deemed-unlawful) — Analysis of the June 2024 federal court decision vacating portions of the OCR tracking guidance.
12. [Court Vacates HIPAA Online Tracking Guidance | Holland & Hart](https://hhhealthlawblog.com/court-vacates-hipaa-online-tracking-guidance/) — Summary of the Northern District of Texas ruling vacating OCR's unauthenticated webpage guidance.
13. [HIPAA Security Rule NPRM | HHS.gov](https://www.hhs.gov/hipaa/for-professionals/security/hipaa-security-rule-nprm/index.html) — Official HHS page for the December 2024 HIPAA Security Rule NPRM.
14. [HIPAA Security Rule NPRM, Federal Register (Jan. 6, 2025)](https://www.federalregister.gov/documents/2025/01/06/2024-30983/hipaa-security-rule-to-strengthen-the-cybersecurity-of-electronic-protected-health-information) — Official Federal Register publication of the proposed HIPAA Security Rule update.
15. [DOJ Shows its Commitment to Cybersecurity Enforcement Through the False Claims Act | Foley & Lardner](https://www.foley.com/insights/publications/2024/08/doj-cybersecurity-enforcement-false-claims-act/) — Analysis of DOJ Civil Cyber-Fraud Initiative enforcement activity through 2024.
16. [DOJ's FCA Recoveries Top $2.9 Billion in FY 2024 | Epstein Becker Green](https://www.healthlawadvisor.com/dojs-false-claims-act-recoveries-top-2-9-billion-in-fy-2024-but-health-care-numbers-dip-what-could-fy-2025-hold-for-health-care-enforcement) — Overview of FY 2024 DOJ FCA healthcare enforcement statistics.
17. [OCR Updates Guidance on Use of Online Tracking Technologies | Morrison Foerster](https://www.mofo.com/resources/insights/240329-ocr-updates-guidance-on-use-of-online-tracking-technologies) — MoFo client alert on the March 2024 OCR tracking technology guidance update.
18. [FTC Targets Tracking Pixels Amid Data Sharing Settlements with GoodRx, BetterHelp | Davis Wright Tremaine](https://www.dwt.com/blogs/privacy--security-law-blog/2023/03/ftc-pixel-tracking-health-goodrx-betterhelp) — Law firm analysis of FTC pixel tracking enforcement pattern.
19. [FTC Finalizes Expansion of Health Breach Notification Rule | Davis Wright Tremaine](https://www.dwt.com/blogs/privacy--security-law-blog/2024/05/ftc-finalizes-hbnr-to-cover-health-app-breaches) — Analysis of the final 2024 HBNR amendments.
20. [Washington My Health My Data Act, RCW Chapter 19.373](https://app.leg.wa.gov/RCW/default.aspx?cite=19.373&full=true) — Official Washington State RCW text for the My Health My Data Act (HB 1155, 2023 session).
