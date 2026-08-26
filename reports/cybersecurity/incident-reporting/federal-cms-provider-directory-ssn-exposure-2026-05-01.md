---
title: "CMS National Provider Directory Exposed Healthcare Providers' Social Security Numbers for Weeks"
date: 2026-05-01
jurisdiction: "Federal"
category: "cybersecurity"
development_type: "other"
finding_id: "SCAN-20260504-031"
topic_key: "federal-0e5209bf-2026"
topic_type: "guidance"
first_reported: 2026-05-01
last_updated: 2026-05-04
status_history: []
cluster: "CMS National Provider Directory SSN Exposure (2026)"
cluster_slug: "cms-npd-ssn-data-breach-2026"
---

# CMS National Provider Directory Exposed Healthcare Providers' Social Security Numbers for Weeks

**Jurisdiction:** Federal | **Category:** Cybersecurity / Healthcare Data | **Date:** May 1, 2026

## Summary [HIGH confidence]

The Centers for Medicare and Medicaid Services (CMS) inadvertently exposed the Social Security numbers of at least 102 healthcare providers through a publicly downloadable database powering its new National Provider Directory — a flagship Medicare modernization initiative overseen by CMS Administrator Dr. Mehmet Oz and built partly with U.S. Digital Service (USDS) support. The [Washington Post](https://www.washingtonpost.com/health/2026/04/30/medicare-portal-social-security-numbers-exposed/) discovered the exposure and flagged it to CMS on April 28, 2026; the agency took the directory offline thereafter. CMS attributed the breach to providers inadvertently entering Social Security numbers in incorrect database fields, and has not disclosed the full count of affected individuals or whether it has notified any affected providers.

## Key Facts [HIGH confidence]

- CMS made the National Provider Directory database publicly downloadable as part of its data transparency initiative; the files are not immediately visible to users visiting the directory portal but were accessible for download for at least several weeks prior to April 28, 2026, according to [The Washington Post](https://www.washingtonpost.com/health/2026/04/30/medicare-portal-social-security-numbers-exposed/).
- Politico and the Post independently examined downloadable files and found full, unredacted Social Security numbers for at least 102 providers, linked to their names and other identifying information, per [SC World](https://www.scworld.com/brief/medicare-directory-exposes-social-security-numbers-of-us-healthcare-providers) and [The Hill](https://thehill.com/policy/healthcare/5860959-cms-publishes-social-security-data/).
- The directory covers more than 7 million providers and was created to help seniors identify which doctors and facilities accept which insurance plans, according to [The Hill](https://thehill.com/policy/healthcare/5860959-cms-publishes-social-security-data/).
- CMS stated the error "stems from incorrect entries of provider or provider-representative-supplied information in the wrong places" — framing the root cause as a data validation failure rather than a cyberattack, per [The Washington Post](https://www.washingtonpost.com/health/2026/04/30/medicare-portal-social-security-numbers-exposed/).
- CMS did not respond to questions about the total number of SSNs exposed, whether affected providers have been notified, or the date on which the exposure began, according to [The Washington Post](https://www.washingtonpost.com/health/2026/04/30/medicare-portal-social-security-numbers-exposed/) and [SC World](https://www.scworld.com/brief/medicare-directory-exposes-social-security-numbers-of-us-healthcare-providers).
- CMS took the directory offline after being notified and stated it "has taken steps to address it promptly and reinforce safeguards around data submission and validation," per [The Hill](https://thehill.com/policy/healthcare/5860959-cms-publishes-social-security-data/).
- The directory is a component of CMS's three-phase National Provider Directory initiative; Phase 1 launched in fall 2025 for Medicare Advantage open enrollment, with a beta launch for the full directory planned for later in 2026, per [STAT News](https://www.statnews.com/2026/02/19/cms-national-provider-directory-launch-beta-test/).
- The U.S. DOGE Service is actively involved in the CMS healthcare modernization initiative, including the provider directory project, under Acting USDS Administrator Amy Gleason, per [USDS](https://www.usds.gov/projects/cms).
- CMS Administrator Dr. Mehmet Oz has oversight responsibility for the agency and the directory initiative, per [The New Republic](https://newrepublic.com/post/209849/dr-oz-medicare-portal-leak-social-security-numbers).
- Rep. Richard E. Neal (D-MA), ranking member of the Ways and Means Committee, called on House Republicans to launch an investigation, stating the incident reflects the Trump Administration's "incompetence" in handling sensitive data, per [The Washington Post](https://www.washingtonpost.com/health/2026/04/30/medicare-portal-social-security-numbers-exposed/).
- Rep. John B. Larson (D-CT) called on DOGE and the administration to provide a detailed account of how the breach occurred, per [Rep. Larson's press release](https://larson.house.gov/media-center/in-the-news/trump-administration-inadvertently-exposed-healthcare-providers-social).
- Democratic Senators Jeff Merkley and Ron Wyden (both D-OR) had previously raised concerns in a letter to CMS Administrator Oz about the rushed directory implementation, warning of "erroneous, conflicting, and duplicative information" in the database, per [Healthcare Finance News](https://www.healthcarefinancenews.com/news/democrats-press-cms-rushing-medicare-provider-directory).
- This incident is described as the latest in a series of quality and accuracy problems with the directory since its launch, including prior issues with misidentified insurance plan coverage, per [TechRadar](https://www.techradar.com/pro/security/cms-error-exposes-us-healthcare-providers-social-security-numbers-trump-administration-directory-designed-to-modernize-medicare-encounters-another-setback).

## Regulatory and Legal Framework [MEDIUM confidence]

### HIPAA Breach Notification Rule

CMS is a covered entity under the Health Insurance Portability and Accountability Act (HIPAA). The HIPAA Breach Notification Rule, codified at [45 C.F.R. §§ 164.400–414](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-D), requires covered entities to:

1. **Notify affected individuals** without unreasonable delay and no later than 60 calendar days after discovering a breach of unsecured protected health information (PHI), under [45 C.F.R. § 164.404](https://www.law.cornell.edu/cfr/text/45/164.404).
2. **Notify the Secretary of HHS** of the breach, under [45 C.F.R. § 164.408](https://www.law.cornell.edu/cfr/text/45/164.408). For breaches affecting 500 or more individuals, notification is due within 60 days of discovery and must be reported to the HHS Office for Civil Rights (OCR) simultaneously.
3. **Notify prominent media outlets** in each state where the breach affects 500 or more residents, under [45 C.F.R. § 164.406](https://www.law.cornell.edu/cfr/text/45/164.406).

A critical legal question is whether the exposed data constitutes PHI subject to HIPAA protections. SSNs are not inherently PHI; however, if the exposed SSNs are linked to individuals' Medicare enrollment status or other health-related data fields in the National Provider Directory, they may constitute PHI of those providers in their capacity as Medicare-enrolled individuals. This analysis is complicated because the exposed individuals are providers (not patients) and HIPAA's breach notification provisions principally address PHI of patients. The [HHS OCR Breach Portal](https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf) had not, as of publication date, listed a CMS National Provider Directory incident, which may indicate either that CMS does not consider HIPAA's breach notification rule applicable to this exposure or that notification is pending.

### Privacy Act of 1974

Social Security numbers held by a federal agency about identifiable individuals are covered by the [Privacy Act of 1974, 5 U.S.C. § 552a](https://www.govinfo.gov/content/pkg/USCODE-2022-title5/pdf/USCODE-2022-title5-partI-chap5-subchapII-sec552a.pdf). Federal agencies are required to implement safeguards to protect records from unauthorized disclosure. CMS's unintentional public exposure of SSNs in a downloadable database could constitute a disclosure not covered by any routine use under the applicable Systems of Records Notice (SORN), triggering Privacy Act obligations. To date, CMS has not publicly acknowledged whether it has assessed the exposure under the Privacy Act or notified the Office of Management and Budget (OMB) as required for major computer matching programs.

### E-Government Act / Federal Information Security

The Federal Information Security Modernization Act (FISMA) and the E-Government Act require federal agencies to secure systems and data. While FISMA violations do not create private rights of action, congressional oversight committees — including the House Ways and Means Committee — have investigative authority over CMS's data security practices, per [Congressional Research Service summaries](https://crsreports.congress.gov/).

## Action Items

- **Healthcare providers enrolled in Medicare:** If you submitted NPI enrollment data to CMS within the past 12–18 months, verify whether your Social Security number was inadvertently included in any CMS data fields. Contact CMS at 1-800-MEDICARE or through the PECOS enrollment portal to confirm your data has been corrected.
- **Healthcare organizations and practice administrators:** Audit any NPI or PECOS enrollment submissions made on behalf of employed or affiliated providers to confirm no SSNs were entered in incorrect fields.
- **Compliance officers:** Monitor the HHS OCR Breach Portal for any formal breach notification from CMS, which would trigger secondary notification obligations if your organization's providers are affected. The 60-day clock under 45 C.F.R. § 164.404 runs from the date of discovery (April 28, 2026), meaning formal notifications — if CMS determines HIPAA applies — are due by June 27, 2026.
- **Legal counsel:** Evaluate whether affected providers have independent state-law remedies. Multiple states have identity theft protection statutes that may apply to SSN exposures, regardless of federal HIPAA applicability. Assess whether CMS's framing of this as a provider data-entry error rather than an agency security failure is legally adequate.
- **Policy and government affairs teams:** Track congressional oversight requests from Rep. Neal (Ways and Means) and Rep. Larson; any formal investigation could yield document productions that shed light on the full scope of the exposure and CMS data handling practices.
- **All stakeholders:** Await CMS's planned data submission safeguard enhancements before relying on the National Provider Directory as a source of validated provider data; the directory has a documented pattern of accuracy and integrity problems.

## Related Reports

- [reports/cybersecurity/enforcement-actions/hhs-ocr-hipaa-ransomware-settlements-2026-04-24.md](../enforcement-actions/hhs-ocr-hipaa-ransomware-settlements-2026-04-24.md) — HHS OCR's active HIPAA enforcement initiative and corrective action plans are directly relevant to CMS's breach notification obligations and OCR's likely scrutiny of this incident.
- [reports/cybersecurity/standards-guidance/federal-five-eyes-agentic-ai-guidance-2026-05-01.md](../standards-guidance/federal-five-eyes-agentic-ai-guidance-2026-05-01.md) — USDS/DOGE involvement in CMS modernization intersects with federal AI and data security guidance frameworks relevant to agentic system deployments.

## Sources

1. [Medicare portal exposed health providers' Social Security numbers — The Washington Post](https://www.washingtonpost.com/health/2026/04/30/medicare-portal-social-security-numbers-exposed/) — Primary investigative report; first to identify and report the exposure to CMS on April 28, 2026.
2. [Medicare directory exposes Social Security numbers of US healthcare providers — SC World](https://www.scworld.com/brief/medicare-directory-exposes-social-security-numbers-of-us-healthcare-providers) — Security industry brief confirming at least 102 exposed SSNs; corroboration source.
3. [CMS accidentally reveals Social Security data of providers — The Hill](https://thehill.com/policy/healthcare/5860959-cms-publishes-social-security-data/) — Congressional reaction and CMS statement summarizing the exposure and agency response.
4. [Error in Medicare database exposes US healthcare providers Social Security numbers — TechRadar](https://www.techradar.com/pro/security/cms-error-exposes-us-healthcare-providers-social-security-numbers-trump-administration-directory-designed-to-modernize-medicare-encounters-another-setback) — Technical analysis of the breach and broader pattern of directory quality problems.
5. [Trump's Big Medicare Project Leaked Tons of Social Security Numbers — The New Republic](https://newrepublic.com/post/209849/dr-oz-medicare-portal-leak-social-security-numbers) — Dr. Oz / CMS Administrator context; details on root cause (provider data entry error vs. system failure).
6. [Trump Administration Inadvertently Exposed Healthcare Providers' Social Security Numbers — Rep. John Larson press release](https://larson.house.gov/media-center/in-the-news/trump-administration-inadvertently-exposed-healthcare-providers-social) — Congressional oversight demand; Rep. Larson's call for DOGE accountability.
7. [National Provider Directory set to launch this year with beta test — STAT News](https://www.statnews.com/2026/02/19/cms-national-provider-directory-launch-beta-test/) — Background on the three-phase NPD initiative and planned 2026 beta launch.
8. [Modernizing Critical Healthcare Systems with CMS — U.S. DOGE Service (USDS)](https://www.usds.gov/projects/cms) — Official description of USDS/DOGE involvement in CMS healthcare modernization and provider directory.
9. [National Provider Directory — CMS](https://directory.cms.gov/) — Official CMS portal for the National Provider Directory (offline at time of reporting).
10. [Democrats press CMS on 'rushing' Medicare provider directory — Healthcare Finance News](https://www.healthcarefinancenews.com/news/democrats-press-cms-rushing-medicare-provider-directory) — Background on prior Democratic concerns about directory accuracy and rushed rollout.
11. [eCFR 45 CFR Part 164 Subpart D — Breach Notification Rule](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-D) — Official regulatory text of HIPAA Breach Notification Rule (45 C.F.R. §§ 164.400–414).
12. [45 C.F.R. § 164.404 — Notification to Individuals](https://www.law.cornell.edu/cfr/text/45/164.404) — Specific individual notification requirement: 60-day deadline, written form requirements.
13. [45 C.F.R. § 164.408 — Notification to the Secretary](https://www.law.cornell.edu/cfr/text/45/164.408) — HHS Secretary notification requirement for breaches of unsecured PHI.
14. [HHS OCR Breach Portal](https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf) — Official breach reporting portal; no CMS National Provider Directory incident listed as of publication date.
15. [Breach Notification Rule Overview — HHS.gov](https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html) — HHS summary of HIPAA Breach Notification Rule obligations and enforcement.
16. [Will DOGE Access to CMS Data Lead to HIPAA Breaches? — GovInfoSecurity](https://www.govinfosecurity.com/will-doge-access-to-cms-data-lead-to-hipaa-breaches-a-27463) — Prior expert analysis of DOGE access to CMS systems and HIPAA breach risk.
