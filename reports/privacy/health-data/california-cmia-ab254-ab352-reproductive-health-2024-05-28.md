---
title: "California CMIA Amendments (AB 254 & AB 352): New Requirements for Reproductive and Sexual Health Data"
date: 2024-05-28
jurisdiction: "California"
category: "privacy"
development_type: "legislation"
finding_id: "SCAN-20240528-004"
topic_key: "california-772bda97-2024"
topic_type: "state_bill"
first_reported: 2024-05-28
last_updated: 2026-04-15
status_history:
  - "2026-04-15: Revised per reviewer round-1 feedback — corrected HIPAA reproductive health rule status (vacated June 2025, Purl v. HHS); corrected Civil Code § 56.36 penalty tiers for licensed health care professionals (added $10,000 intermediate tier; clarified $2,500 negligent-disclosure floor applies to any person/entity)."
cluster: "California CMIA Amendments (AB 254 & AB 352): Reproductive and Sexual Health Data"
cluster_slug: "california-cmia-ab254-ab352-reproductive-health"
---

# California CMIA Amendments (AB 254 & AB 352): New Requirements for Reproductive and Sexual Health Data

**Jurisdiction:** California | **Category:** Privacy | **Date:** 2024-05-28

## Executive Summary [HIGH confidence]

Two bills signed by Governor Gavin Newsom on September 27, 2023 substantially expand California's Confidentiality of Medical Information Act (CMIA) to protect reproductive and sexual health data. [Assembly Bill 254](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB254) (AB 254) brings consumer-facing reproductive health apps within the CMIA framework for the first time, treating app operators as "providers of health care" subject to the same restrictions as hospitals and clinicians. [Assembly Bill 352](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB352) (AB 352) imposes strict data segregation, access-control, and out-of-state disclosure prohibitions on electronic health record (EHR) developers and other businesses storing sensitive service information for California patients. Both statutes became partially effective January 1, 2024, with EHR-developer technical compliance required by July 1, 2024, and provider liability for AB 352 violations deferred to January 31, 2027 following a 2025 extension. Organizations operating reproductive health apps, EHR systems, or health data platforms that touch California residents must act now to audit their data practices.

## Background [HIGH confidence]

The CMIA, codified at [California Civil Code § 56 et seq.](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=56.10.&lawCode=CIV), is California's primary health data privacy statute and predates the federal Health Insurance Portability and Accountability Act of 1996 (HIPAA). It has historically applied to providers of health care, health plans, contractors, and employers. A key gap in its coverage emerged post-Dobbs: consumer-facing fertility and menstrual tracking apps — collectively holding sensitive inferential data about pregnancy status, contraception use, and sexual activity — were not regulated entities under HIPAA and, prior to AB 254, sat in a legal grey zone under the CMIA.

The Dobbs decision in June 2022 heightened urgency around this gap. States with abortion restrictions were increasingly seeking medical records through out-of-state subpoenas and law enforcement requests. California responded with a package of reproductive-health privacy legislation in 2023 that included AB 254, AB 352, and related measures. The two bills targeted different segments of the health data ecosystem: AB 254 captured the consumer app sector; AB 352 addressed the enterprise EHR infrastructure layer.

Prior to these amendments, the California Attorney General had already taken interpretive positions that CMIA applied to some digital health services, but AB 254 codified that stance explicitly, resolving legal ambiguity for app operators. AB 352 was specifically motivated by the risk that EHR systems could be compelled to produce records tied to abortion or gender-affirming care through out-of-state legal process — a risk the legislature addressed with mandatory technical and operational controls at the infrastructure level.

## Detailed Analysis [HIGH confidence]

### AB 254 — Reproductive or Sexual Health Digital Services

AB 254 amends the CMIA to introduce two new defined terms and a corresponding coverage expansion. A "[reproductive or sexual health digital service](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB254)" is defined as a mobile application or website that (a) collects reproductive or sexual health application information from a consumer, (b) markets itself as facilitating reproductive or sexual health services, and (c) uses that information to facilitate such services. "Reproductive or sexual health application information" covers information about a consumer's reproductive health, menstrual cycle, fertility, pregnancy, pregnancy outcome, plans to conceive, or type of sexual activity, including inferred information about pregnancy status, hormone levels, birth control use, sexual activity, or gender identity.

Any business offering such a service for the purpose of allowing an individual to manage their health information, or for diagnosis, treatment, or management of a medical condition, is deemed a "provider of health care" under the CMIA. This creates full CMIA obligations: the prohibition on selling medical information, the bar on using it for marketing without specific authorization, the requirement for prior written authorization before disclosure, and exposure to the CMIA's civil and criminal penalty regime.

The practical significance is substantial. Many period-tracking and fertility apps were not HIPAA-covered entities, meaning they previously faced only the California Consumer Privacy Act (CCPA) — a general-purpose privacy statute with weaker health-specific restrictions. AB 254 closes this gap by imposing sector-specific health privacy obligations directly on app operators. [ArentFox Schiff](https://www.afslaw.com/perspectives/health-care-counsel-blog/california-adopts-privacy-protections-digital-reproductive) notes that AB 254 is designed to ensure reproductive health apps are subject to CMIA in the same way clinicians and hospitals are, with CMIA serving as California's analogue to HIPAA for this sector.

### AB 352 — Sensitive Services: Data Segregation and Out-of-State Disclosure Prohibition

AB 352 targets entities further upstream in the health data infrastructure: EHR developers, digital health companies, and other businesses that electronically store or maintain "medical information on the provision of sensitive services" on behalf of California health care providers, health plans, pharmaceutical companies, contractors, or employers. The statute defines "sensitive services" to include health care services related to mental or behavioral health, sexual and reproductive health, sexually transmitted infections, substance use disorder, gender-affirming care, and intimate partner violence.

The core obligations, which required implementing capabilities, policies, and procedures by July 1, 2024, are:

1. **Access controls**: Limit user access privileges to information systems containing medical information related to gender-affirming care, abortion, abortion-related services, and contraception only to authorized persons.
2. **Out-of-state disclosure prohibition**: Prevent the disclosure, access, transfer, transmission, or processing of such information to any person or entity outside of California.
3. **Record segregation**: Segregate medical information related to these specified services from the rest of a patient's medical record.

Health care providers themselves face a parallel obligation: they must not release medical information related to an individual seeking or obtaining an abortion in response to a subpoena or request based on another state's laws that interfere with rights under California's Reproductive Privacy Act, or based on a foreign penal civil action. This applies to inquiries by out-of-state agencies and federal law enforcement as well. [McDermott Will & Emery](https://www.mcdermottlaw.com/insights/californias-new-reproductive-privacy-laws-ab-352-and-ab-254-create-complexities-for-health-information-sharing/) notes that these restrictions create meaningful complexity for health information exchanges and data-sharing networks that span state lines, particularly where systems must dynamically identify and segregate sensitive records.

### Relationship to HIPAA [MEDIUM confidence]

The CMIA has historically been more restrictive than HIPAA in several respects. At the time AB 352 was enacted, the U.S. Department of Health and Human Services issued a 2024 rulemaking — the HIPAA Privacy Rule to Support Reproductive Health Care Privacy, 89 Fed. Reg. 32,976 (Apr. 26, 2024) — that similarly limited disclosures of reproductive health information by HIPAA-covered entities. AB 352's framework paralleled and in some respects exceeded those federal protections.

**That federal rule is no longer operative.** On June 18, 2025, the U.S. District Court for the Northern District of Texas vacated the 2024 HIPAA reproductive health rule nationwide in [*Purl v. U.S. Department of Health and Human Services*, No. 2:24-CV-228-Z (N.D. Tex. June 18, 2025)](https://www.hklaw.com/en/insights/publications/2025/06/hipaas-reproductive-health-rule-is-vacated-nationally). The court held that the rule exceeded HHS's statutory authority and unlawfully restricted state-mandated reporting obligations. HHS declined to appeal by the August 18, 2025 deadline, and the Fifth Circuit subsequently dismissed a related intervenor appeal on September 10, 2025, [confirming the rule's demise](https://www.americanbar.org/groups/health_law/news/2025/signaling-end-purl-case/). As of mid-2025, no direct federal HIPAA analog to AB 352's reproductive health disclosure protections remains in effect.

The practical consequence is significant: **California's CMIA now provides substantially stronger protection for reproductive health data than the current federal HIPAA baseline**, which reverted to pre-2024 standards for this category of data. Where HIPAA applies, California providers must comply with the more protective state statute. For non-HIPAA entities (including most consumer app operators), AB 254's CMIA coverage fills the regulatory gap independently, entirely without federal support.

### Enforcement and Penalties [HIGH confidence]

CMIA enforcement runs through [Civil Code §§ 56.35–56.36](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=56.36.&lawCode=CIV). Under that framework:

- **Negligent disclosures**: Any person or entity that negligently discloses medical information in violation of the CMIA is liable for an administrative fine or civil penalty not to exceed $2,500 per violation (§ 56.36(b)).
- **Knowing and willful violations — licensed health care professionals**: A licensed health care professional who knowingly and willfully obtains, discloses, or uses medical information in violation of the CMIA faces a tiered penalty structure: up to $2,500 on a first violation; up to $10,000 on a second violation; and up to $25,000 on a third and subsequent violation (§ 56.36(c)).
- **Knowing and willful violations — all other persons and entities**: Any person or entity that is not a licensed health care professional and knowingly and willfully obtains, discloses, or uses medical information in violation of the CMIA is liable for a civil penalty not to exceed $25,000 per violation (§ 56.36(c)).
- **Violations for financial gain**: A person or entity that knowingly or willfully obtains or uses medical information for the purpose of financial gain may face an administrative fine or civil penalty not to exceed $250,000 per violation, plus disgorgement of proceeds (§ 56.36(c)).
- **Criminal liability**: Knowing and willful acquisition, disclosure, or use of medical information in violation of the CMIA may be charged as a criminal misdemeanor.

The California Attorney General enforces these provisions, and private right of action is available for violations resulting in economic loss or personal injury. AB 352's liability provisions carry a phased timeline: the technical compliance deadline for EHR developers was July 1, 2024, but health care providers received a safe harbor from enforcement liability until January 31, 2026 in the original statutory text. That deadline was subsequently extended to January 31, 2027 by [Assembly Bill 260 (2025)](https://connectingforbetterhealth.com/wp-content/uploads/2025/10/Final-AB-352-FAQ-October-2025.pdf) for providers working diligently and in good faith toward compliance.

## Impact Assessment [MEDIUM confidence]

**Affected entities — AB 254:** Any developer or operator of a mobile app or website that markets reproductive or sexual health services, collects menstrual cycle, fertility, pregnancy, or related data, and serves California residents. This includes standalone period-tracking apps, ovulation and fertility platforms, pregnancy journaling tools, and digital sexual health services. These operators were previously unregulated under CMIA; they are now full health care providers for CMIA purposes and must implement the statute's consent, access, use, and disclosure restrictions.

**Affected entities — AB 352:** EHR developers, health information exchanges, health care interoperability vendors, digital health platforms, and any business that operates data infrastructure storing California patient records for covered health care entities. The segregation and access-control requirements are technically demanding for systems built on unified patient record architectures where sensitive-service data is not already isolated.

**Compliance timeline:** The July 1, 2024 deadline for EHR technical capabilities under AB 352 has passed. Providers themselves have until January 31, 2027 under AB 260 to reach full compliance without incurring liability, provided good-faith effort is demonstrated. AB 254's obligations for app operators have been in effect since January 1, 2024 with no corresponding safe harbor.

**Interstate tension:** AB 352's out-of-state disclosure prohibition directly conflicts with legal process served by states with restrictive abortion laws seeking California records. Health systems and EHR vendors may face conflicting legal demands — a subpoena from a Texas court versus a California statute prohibiting compliance. [Troutman Pepper Locke](https://www.troutman.com/insights/New-California-Law-Imposes-Significant-Data-Management-Requirements-for-Sensitive-Health-Data/) has flagged that navigating this conflict may require proactive legal guidance and operational protocols for responding to out-of-state requests. The vacatur of the 2024 HIPAA reproductive health rule removes a federal backstop that would have provided some parallel protection and may intensify the importance of California's state-law regime.

**Enforcement outlook:** No public enforcement actions specifically under the AB 254 or AB 352 amendments have been identified as of the date of this report. The California AG's [privacy enforcement page](https://oag.ca.gov/privacy/privacy-enforcement-actions) does not yet reflect actions under these specific provisions. Given the July 2024 technical deadline and the approaching January 2027 provider compliance date, enforcement activity is expected to increase through 2026.

## Action Items

- **App operators**: Audit all consumer-facing reproductive and sexual health digital services to determine whether AB 254's "provider of health care" definition applies. If so, implement CMIA-compliant authorization workflows, data use restrictions, and prohibition on sale or marketing use of reproductive health information.
- **EHR developers and health data vendors**: If the July 1, 2024 technical compliance deadline has passed, assess current state of access controls, out-of-state disclosure prevention capabilities, and record segregation for sensitive services. Document good-faith compliance efforts to preserve the AB 260 safe harbor through January 31, 2027.
- **Health care providers**: Establish policies for responding to out-of-state subpoenas, law enforcement requests, and cross-border data sharing requests involving reproductive health, gender-affirming care, and other sensitive service records. Do not release such records in response to legal process based on other states' laws restricting reproductive rights. Note that the federal HIPAA reproductive health rule vacated in *Purl* (June 2025) no longer provides parallel federal protection — California CMIA compliance is now the operative framework.
- **Health information exchanges and interoperability networks**: Review data-sharing agreements and technical architectures to ensure sensitive-service record flows are blocked from routing to entities outside California consistent with AB 352.
- **All covered entities**: Monitor for enforcement guidance from the California AG and any further legislative amendments, including follow-on legislation to AB 260 that may affect the 2027 provider deadline. Track any Congressional or HHS rulemaking activity that might restore federal reproductive health privacy protections in the wake of *Purl*.

## Related Reports

- [reports/privacy/health-data/federal-cms-healthcare-privacy-2024-04-17.md](../health-data/federal-cms-healthcare-privacy-2024-04-17.md) — Federal regulatory context: CMS and Senate HELP Committee developments affecting health data privacy at the federal level, relevant background for California's complementary state-level approach.
- [reports/privacy/hhs-ocr-hipaa-risk-management-video-2026-04-12.md](../hhs-ocr-hipaa-risk-management-video-2026-04-12.md) — HIPAA Security Rule guidance from HHS OCR; intersects with the HIPAA/CMIA interaction analyzed in this report.
- [reports/privacy/state-comprehensive-laws/california-cppa-opposes-apra-federal-preemption-2024-05-14.md](../california-cppa-opposes-apra-federal-preemption-2024-05-14.md) — CPPA's opposition to federal preemption; the CMIA is among the California statutes that could be affected by federal privacy preemption proposals.

## Sources

1. [AB 254 Official Bill Text — California Legislative Information](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB254) — Official enrolled text of AB 254 amending CMIA to cover reproductive or sexual health digital services.
2. [AB 352 Official Bill Text — California Legislative Information](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB352) — Official enrolled text of AB 352 amending CMIA to require sensitive-services segregation and out-of-state disclosure prohibitions.
3. [California Civil Code § 56.10 — CMIA Disclosure Provisions](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=56.10.&lawCode=CIV) — Official statutory text of existing CMIA disclosure provisions amended by AB 254 and AB 352.
4. [California Civil Code § 56.36 — CMIA Penalties (California Legislative Information)](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=56.36.&lawCode=CIV) — Official text of CMIA penalty provisions, including the tiered structure for licensed health care professionals.
5. [Baker McKenzie — "Amendments to California's CMIA Bring Health Data New Requirements"](https://connectontech.bakermckenzie.com/amendments-to-californias-cmia-bring-health-data-new-requirements/) — Primary law firm alert and source of the underlying finding; comprehensive overview of AB 254 and AB 352 provisions.
6. [ArentFox Schiff — "California Adopts Privacy Protections for Digital Reproductive and Sexual Health Information"](https://www.afslaw.com/perspectives/health-care-counsel-blog/california-adopts-privacy-protections-digital-reproductive) — Analysis of AB 254's app-sector coverage expansion and relationship to HIPAA.
7. [McDermott Will & Emery — "California's New Reproductive Privacy Laws AB 352 and AB 254 Create Complexities for Health Information Sharing"](https://www.mcdermottlaw.com/insights/californias-new-reproductive-privacy-laws-ab-352-and-ab-254-create-complexities-for-health-information-sharing/) — Detailed analysis of interstate health information exchange complications arising from AB 352.
8. [National Law Review — "California's New Reproductive Privacy Laws AB 352 and AB 254 Create Complexities for Health Information Sharing"](https://natlawreview.com/article/californias-new-reproductive-privacy-laws-ab-352-and-ab-254-create-complexities) — Syndicated version of McDermott analysis with additional context.
9. [Covington Digital Health — "California Enacts Amendments to the CMIA"](https://www.covingtondigitalhealth.com/2023/10/california-enacts-amendments-to-the-cmia/) — Law firm analysis covering both AB 254 and AB 352 effective dates and scope.
10. [Troutman Pepper Locke — "New California Law Imposes Significant Data Management Requirements for Sensitive Health Data"](https://www.troutman.com/insights/New-California-Law-Imposes-Significant-Data-Management-Requirements-for-Sensitive-Health-Data/) — Analysis of AB 352 EHR developer obligations and interstate legal conflict risk.
11. [AB 352 FAQ — Connecting for Better Health (October 2025)](https://connectingforbetterhealth.com/wp-content/uploads/2025/10/Final-AB-352-FAQ-October-2025.pdf) — Industry FAQ on AB 352 compliance including the AB 260 extension to January 31, 2027.
12. [California AG — Privacy Enforcement Actions](https://oag.ca.gov/privacy/privacy-enforcement-actions) — Official California Attorney General enforcement page; no AB 254/352-specific enforcement actions identified as of date of report.
13. [Manatt, Phelps & Phillips — "California Enacts Laws to Further Protect Reproductive Health Data"](https://www.manatt.com/insights/newsletters/health-highlights/california-enacts-laws-to-further-protect-reproduc/) — Overview of the broader 2023 California reproductive health legislative package context.
14. [Holland & Knight — "HIPAA's Reproductive Health Rule Is Vacated Nationally" (June 2025)](https://www.hklaw.com/en/insights/publications/2025/06/hipaas-reproductive-health-rule-is-vacated-nationally) — Analysis of the *Purl v. HHS* district court decision vacating the 2024 HIPAA reproductive health rule nationwide.
15. [American Bar Association Health Law Section — "Fifth Circuit Dismisses Appeal of Decision Vacating HIPAA Reproductive Health Privacy Rule" (September 2025)](https://www.americanbar.org/groups/health_law/news/2025/signaling-end-purl-case/) — Confirms the end of *Purl* litigation and the finality of the vacatur following dismissal of the Fifth Circuit appeal.
