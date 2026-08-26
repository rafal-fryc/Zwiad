---
title: "Maryland 2024 Legislative Session: Key New Laws Affecting Financial Services Providers"
date: 2024-07-24
jurisdiction: "Maryland"
category: "privacy"
development_type: "legislation"
finding_id: "SCAN-20240724-016"
topic_key: "maryland-a317b78b-2024"
topic_type: "guidance"
first_reported: 2024-07-24
last_updated: 2026-04-16
status_history:
  - "2026-04-16: Revised per reviewer feedback (round 1) — fixed MODPA applicability (added targeting prong, removed unconfirmed payment-transaction carveout), updated MODPA penalties to $10,000/$25,000 first/subsequent, corrected SB 760 dual effective dates (June 1 / October 1, 2025), corrected HB 622 inline citation URL, softened unverified '18 states' count."
cluster: "Maryland MODPA and Kids Code (HB 567 / HB 603)"
cluster_slug: "maryland-modpa-kids-code-2024"
---

# Maryland 2024 Legislative Session: Key New Laws Affecting Financial Services Providers

**Jurisdiction:** Maryland | **Category:** Privacy / Financial Services | **Date:** 2024-07-24

## Executive Summary [MEDIUM confidence]

The Maryland General Assembly's 2024 regular session produced several significant laws affecting financial services providers, with implications for data privacy, consumer reporting, third-party oversight, and consumer fraud. The centerpiece is the [Maryland Online Data Privacy Act (MODPA)](https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/sb0541?ys=2024RS) (SB 541/HB 567), signed by Governor Wes Moore on May 9, 2024, which establishes Maryland as home to one of the nation's most stringent state privacy frameworks — effective October 1, 2025. Alongside MODPA, the legislature enacted laws restricting consumer reporting of certain criminal records, authorizing expanded examination of third-party service providers by the Commissioner of Financial Regulation, and establishing the first-in-the-nation Gift Card Scams Prevention Act. Financial institutions should note that MODPA's GLBA exemption provides substantial but not unlimited relief from the new privacy requirements. All four laws carry compliance deadlines in 2024 or 2025.

## Background [MEDIUM confidence]

Maryland's 2024 legislative session represented one of the most active years in the state's history for financial services and data privacy regulation. The session ran through early April 2024, with Governor Moore signing the principal bills in May 2024.

The MODPA was the flagship privacy bill of the session. Maryland was following more than a dozen other states that had already enacted comprehensive data privacy legislation in the years following California's CCPA. Maryland's version, however, introduced several provisions — particularly around data minimization and the outright prohibition on selling sensitive personal data — that were more restrictive than most peer state laws.

Three companion measures addressed narrower but operationally significant concerns: the regulation of consumer reporting agencies' access to criminal records, a new supervisory tool allowing Maryland's banking regulator to examine technology vendors directly, and a consumer fraud law targeting gift card draining scams. Gordon Feinblatt LLC, a Maryland-based law firm, published a comprehensive update on these laws in July 2024 as part of their [Maryland Laws Update 2024](https://www.gfrlaw.com/what-we-do/insights/maryland-laws-update-2024), which served as the primary practitioner-facing synthesis of the session's impact on financial services.

## Detailed Analysis [MEDIUM confidence]

### Maryland Online Data Privacy Act (MODPA) — SB 541 / HB 567

Governor Moore [signed SB 541](https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/sb0541?ys=2024RS) into law on May 9, 2024. The Act takes effect October 1, 2025, though enforcement does not begin against personal data processed before April 1, 2026.

**Applicability thresholds.** MODPA applies to for-profit entities that (a) conduct business in Maryland *or* target products or services to Maryland residents, and that also meet one of the following thresholds: (i) process or control personal data of at least 35,000 consumers during a calendar year, or (ii) process or control personal data of at least 10,000 consumers and derive more than 20% of gross revenue from selling personal data. The "targeting" prong is significant — an entity with no physical presence in Maryland may be subject to MODPA if it directs its products or services toward Maryland residents. These thresholds are notably lower than those in Virginia and other model states, expanding MODPA's practical reach.

**Consumer rights.** Controllers must: confirm whether they are processing a consumer's personal data; provide access to that data; correct inaccuracies; delete personal data upon request (unless retention is legally required); provide data portability; disclose categories of third parties receiving personal data; and honor opt-out requests for targeted advertising, sale of personal data, and profiling decisions with legal or significant effects. Consumers may designate authorized agents to exercise opt-out rights on their behalf.

**Data minimization — the defining feature.** MODPA's data minimization mandate is stricter than most state peers. Controllers must [limit collection to what is "reasonably necessary and proportionate"](https://www.cyberlawmonitor.com/2024/08/26/marylands-new-approach-to-data-minimization-creates-unique-compliance-issues/) to provide the specific product or service requested. For sensitive personal data — which includes biometric data, precise geolocation, race, health, sexual orientation, and immigration status — controllers may only process it when "strictly necessary" to deliver a requested product or service. Crucially, MODPA prohibits the *sale* of sensitive personal data entirely, rather than merely requiring opt-in consent (as most other state laws do). This absolute prohibition is a significant departure from the prevailing state law model, as analyzed by [WilmerHale](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20240521-maryland-and-nebraska-adopt-comprehensive-privacy-laws).

**GLBA exemption — scope and limits.** MODPA exempts financial institutions and their affiliates governed by Title V of the [Gramm-Leach-Bliley Act](https://www.ftc.gov/legal-library/browse/statutes/gramm-leach-bliley-act), as well as data controlled by those entities under GLBA. This provides meaningful relief for banks, credit unions, insurance companies, and other licensed financial institutions. However, fintech companies that do not hold a banking license but partner with covered GLBA entities — and companies that process both GLBA-covered and non-GLBA data — face more nuanced analysis. The exemption is entity-level and data-level; it is not a blanket shield for all operations of a company that touches financial services.

**Enforcement.** The Maryland Attorney General's Consumer Protection Division has exclusive enforcement authority. There is no private right of action. Violations are treated as unfair, abusive, or deceptive trade practices under the [Maryland Consumer Protection Act](https://www.marylandattorneygeneral.gov/Pages/CPD/default.aspx), which carries civil penalties of up to $10,000 per violation for a first violation and up to $25,000 per violation for subsequent violations.

**Official legislative text.** The enrolled text is available at [SB 541 — Maryland General Assembly](https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/sb0541?ys=2024RS) and [HB 567 — Maryland General Assembly](https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/hb0567?ys=2024RS).

---

### HB 622 — Criminal Records in Consumer Reports

Governor Moore signed [HB 622](https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/HB0622?ys=2024RS) into law, effective October 1, 2024. The law imposes new restrictions on what consumer reporting agencies (CRAs) may include in consumer reports:

- **Prohibited entries.** CRAs may not include any charge in which the consumer was falsely accused, acquitted, exonerated, received a nolle prosequi, was not found guilty, did not plead guilty, or which was later expunged.
- **Downstream prohibition.** CRAs also may not rely on prohibited records to make creditworthiness determinations, even indirectly.
- **Penalties.** Violations constitute unfair, abusive, or deceptive trade practices under the Maryland Consumer Protection Act. Fines reach $10,000 for a first violation and $25,000 for subsequent violations.

The [Maryland Commissioner of Financial Regulation issued a Consumer Advisory](https://www.dllr.state.md.us/finance////advisories/advisory-con-criminalrecordsexpiredinfo.pdf) on August 27, 2024 providing regulatory guidance to covered entities, as reported by [Gordon Feinblatt](https://www.gfrlaw.com/what-we-do/insights/maryland-commissioner-financial-regulation-issues-advisory-concerning-new-laws). Financial institutions that use CRA data in underwriting, employment decisions, or vendor risk management should verify that their CRA partners have updated their reporting practices by October 1, 2024.

---

### HB 250 — Third-Party Service Provider Examination Authority

[HB 250](https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/HB0250?ys=2024rs) (Chapter 422), effective October 1, 2024, grants the Commissioner of Financial Regulation new supervisory authority to examine third-party service providers that perform services on behalf of entities licensed or chartered by the Office of Financial Regulation (OFR). Key features:

- The Commissioner may examine a third-party service provider "to the same extent" as the regulated entity itself.
- The Commissioner must notify the licensed entity of any examination involving its third-party service provider.
- Financial institutions bear responsibility for ensuring their vendors cooperate with OFR examination requests.

This authority brings Maryland into alignment with federal banking regulators (OCC, FDIC, Federal Reserve) that have long asserted examination rights over bank third-party service providers. For financial technology companies providing core banking, payment processing, or compliance services to Maryland-licensed institutions, this creates direct regulatory exposure to the OFR.

---

### SB 760 — Gift Card Scams Prevention Act

Maryland became the first state in the nation to enact legislation specifically targeting [gift card draining scams](https://www.reedsmith.com/en/perspectives/2024/10/gift-card-draining-no-more-marylands-new-law-in-focus) when Governor Moore signed SB 760 (Chapter 463) in May 2024. The law has two operative effective dates:

- **Open-loop gift card provisions: effective June 1, 2025.** Open-loop cards (those bearing a network brand such as Visa or Mastercard and usable at any merchant) are subject to the Act's security packaging and tamper-evident warning requirements beginning June 1, 2025.
- **Closed-loop gift card provisions: effective October 1, 2025.** Closed-loop cards (retailer-specific cards redeemable only at the issuing merchant's stores) become subject to the Act's requirements on October 1, 2025. This is the operative date for most retail gift card programs.

Both categories of covered cards are subject to the following requirements:

- Merchants and retailers must use secure packaging with visible tamper-evident warnings for gift cards.
- Third-party gift card resellers face record-keeping and inspection requirements.
- Companies must maintain detailed transaction records for at least three years, subject to law enforcement inspection.
- Violations are treated as unfair, abusive, or deceptive trade practices under the Maryland Consumer Protection Act.

While this law primarily affects retail and commerce, financial institutions that issue, distribute, or accept gift cards — including prepaid cards — should review compliance obligations. Banks that partner with gift card program managers should ensure their contractual agreements address SB 760's security and record-keeping requirements, with timelines keyed to whether their programs involve open-loop or closed-loop cards.

## Impact Assessment [MEDIUM confidence]

**MODPA's primary impact on financial services.** Most Maryland-chartered banks, credit unions, insurance companies, and their affiliates will qualify for the GLBA exemption and face minimal direct compliance burden under MODPA for their core financial services data. However, financial holding companies with non-bank subsidiaries (wealth management apps, insurance technology platforms, or consumer-facing analytics businesses) must conduct entity-by-entity and data-type-by-data-type assessments to identify where the GLBA exemption does not apply.

**Fintech and technology companies.** Companies that partner with banks but do not themselves hold banking licenses occupy uncertain ground under MODPA's GLBA exemption. The exemption covers "financial institutions" as defined by GLBA and their affiliates — but a third-party software vendor, data analytics firm, or payment processor without a banking license may not qualify. These entities should assume MODPA applies unless they obtain a legal opinion confirming exemption status. Note also that the targeting prong of MODPA's applicability test means that out-of-state fintechs marketing to Maryland consumers are within scope even without a Maryland physical presence.

**Consumer reporting and credit underwriting.** Maryland lenders, mortgage companies, and background screening consumers must verify that their CRA providers have updated practices to comply with HB 622 by October 1, 2024. Using prohibited criminal record data — even inadvertently — creates unfair trade practices liability.

**Vendor management.** HB 250's third-party examination authority creates new considerations for vendor contracts. OFR-licensed institutions should notify existing service providers of the new examination authority and ensure vendor agreements include cooperation obligations. New vendor agreements executed after October 1, 2024 should include express OFR examination cooperation clauses.

**Effective dates summary:**

| Law | Effective Date | Notes |
|---|---|---|
| MODPA (SB 541/HB 567) | October 1, 2025 | Enforcement applies to data processed on/after April 1, 2026 |
| HB 622 (Criminal Records / CRAs) | October 1, 2024 | Already in effect |
| HB 250 (Third-Party Exam Authority) | October 1, 2024 | Already in effect |
| SB 760 (Gift Card Scams) — open-loop | June 1, 2025 | Network-branded gift cards (Visa, Mastercard, etc.) |
| SB 760 (Gift Card Scams) — closed-loop | October 1, 2025 | Retailer-specific gift cards |

## Action Items

- Conduct a MODPA applicability assessment for each legal entity in the enterprise — including out-of-state entities that target products or services to Maryland residents — specifically addressing whether each entity qualifies for the GLBA exemption and whether any non-banking operations fall outside that exemption.
- Audit CRA vendor agreements and reporting practices to confirm compliance with HB 622 criminal record prohibitions (effective October 1, 2024). Request written certification from CRA partners.
- Review and update vendor contracts to include Maryland OFR examination cooperation obligations consistent with HB 250 (effective October 1, 2024).
- For institutions that issue, distribute, or accept gift cards or prepaid cards, assess SB 760 compliance obligations and update program manager agreements: open-loop card programs must comply by June 1, 2025; closed-loop programs by October 1, 2025.
- If MODPA applies to any enterprise entity: begin data inventory and mapping to identify sensitive personal data processing; implement data minimization policies; update privacy notices; and establish processes for honoring consumer rights requests before October 1, 2025.
- Monitor Maryland AG Consumer Protection Division for MODPA implementation guidance, rulemaking, and any FAQs published in 2024–2025.

## Related Reports

- [reports/privacy/state-comprehensive-laws/maryland-sb541-modpa-2024-04-17.md](reports/privacy/state-comprehensive-laws/maryland-sb541-modpa-2024-04-17.md) — In-depth analysis of MODPA as standalone legislation; this report provides financial-services-specific context and discusses the GLBA exemption, companion laws, and vendor implications not covered in the MODPA-focused report.
- [reports/privacy/financial-privacy/glba-reform-huizenga-discussion-draft-2026-04-12.md](reports/privacy/financial-privacy/glba-reform-huizenga-discussion-draft-2026-04-12.md) — Federal GLBA modernization discussion draft that, if enacted, would broadly preempt state financial privacy laws including Maryland's; relevant to assessing the long-term durability of MODPA's GLBA exemption.
- [reports/privacy/state-comprehensive-laws/maryland-modpa-kids-code-2024-05-16.md](reports/privacy/state-comprehensive-laws/maryland-modpa-kids-code-2024-05-16.md) — Maryland's children's data privacy provisions enacted alongside MODPA; financial services companies offering products to minors should review both laws together.

## Sources

1. [Maryland Laws Update 2024 — Gordon Feinblatt LLC](https://www.gfrlaw.com/what-we-do/insights/maryland-laws-update-2024) — Primary practitioner synthesis of 2024 Maryland laws affecting financial services providers; basis for the finding.
2. [SB 541 — Maryland General Assembly (Official Legislative Text)](https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/sb0541?ys=2024RS) — Official text and status of MODPA Senate companion bill.
3. [HB 567 — Maryland General Assembly (Official Legislative Text)](https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/hb0567?ys=2024RS) — Official text and status of MODPA House companion bill.
4. [HB 622 — Maryland General Assembly (Official Legislative Text)](https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/HB0622?ys=2024RS) — Official text of criminal records in consumer reports bill.
5. [HB 250 — Maryland General Assembly](https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/HB0250?ys=2024rs) — Official text of third-party service provider examination authority bill.
6. [Maryland and Nebraska Adopt Comprehensive Privacy Laws — WilmerHale](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20240521-maryland-and-nebraska-adopt-comprehensive-privacy-laws) — Law firm analysis comparing MODPA to peer state laws, including analysis of data minimization and sensitive data sale prohibition.
7. [Maryland Creates a New Paradigm for Data Privacy — Davis Wright Tremaine](https://www.dwt.com/blogs/privacy--security-law-blog/2024/05/maryland-online-data-privacy-act-signed) — Law firm analysis of MODPA's distinctive provisions.
8. [Maryland's New Approach to Data Minimization Creates Unique Compliance Issues — Cyber Law Monitor](https://www.cyberlawmonitor.com/2024/08/26/marylands-new-approach-to-data-minimization-creates-unique-compliance-issues/) — Analysis of MODPA's data minimization obligations and how they differ from other state privacy laws.
9. [Maryland Enacts Comprehensive Data Privacy Law — White & Case LLP](https://www.whitecase.com/insight-alert/maryland-enacts-comprehensive-data-privacy-law) — Law firm summary of MODPA's key requirements, exemptions, and effective dates.
10. [Maryland Commissioner of Financial Regulation Issues Advisory Concerning New Laws — Lexology / Gordon Feinblatt](https://www.lexology.com/library/detail.aspx?g=34462376-8668-4268-99ea-a860c041c964) — OFR regulatory advisory summarizing HB 622 criminal records restrictions.
11. [Maryland Commissioner of Financial Regulation — Consumer Advisory (PDF)](https://www.dllr.state.md.us/finance////advisories/advisory-con-criminalrecordsexpiredinfo.pdf) — Official OFR consumer advisory on HB 622 criminal record and credit information restrictions.
12. [Gift Card Draining No More: Maryland's New Law in Focus — Reed Smith LLP](https://www.reedsmith.com/en/perspectives/2024/10/gift-card-draining-no-more-marylands-new-law-in-focus) — Detailed analysis of SB 760 Gift Card Scams Prevention Act, including security requirements, record-keeping obligations, and the open-loop/closed-loop distinction.
13. [Maryland Online Data Privacy Act Now in Effect — Koley Jessen](https://www.koleyjessen.com/insights/publications/maryland-online-data-privacy-act) — Updated summary confirming MODPA's October 1, 2025 effective date and enforcement application to data processed on/after April 1, 2026.
14. [Maryland Enacts Expansive Comprehensive Consumer Data Privacy Law — CFS Blog](https://consumerfsblog.com/2024/05/maryland-enacts-expansive-comprehensive-consumer-data-privacy-law/) — Financial services-focused analysis of MODPA, including GLBA exemption scope.
15. [2024 Regulatory Highlights — Maryland Department of Labor](https://labor.maryland.gov/finance/finregreghl2024.pdf) — Official state regulatory highlights publication covering new laws affecting Maryland-regulated financial institutions.
