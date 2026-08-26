---
title: "Indiana Amends Breach Notification Law to Cover Age Verification Data Collected by Adult Websites"
date: 2024-07-25
jurisdiction: "Indiana"
category: "cybersecurity"
development_type: "legislation"
finding_id: "SCAN-20240725-010"
topic_key: "indiana-4a2230fe-2024"
topic_type: "state_bill"
first_reported: 2024-07-25
last_updated: 2026-04-15
status_history: []
cluster: "Indiana SB 17: Age Verification Mandate and Breach Notification Amendments"
cluster_slug: "indiana-sb17-age-verification-breach-notification"
---

# Indiana Amends Breach Notification Law to Cover Age Verification Data Collected by Adult Websites

**Jurisdiction:** Indiana | **Category:** Cybersecurity | **Date:** July 25, 2024

## Executive Summary [MEDIUM confidence]

Indiana Senate Bill 17 (2024), enacted as [P.L. 98-2024](https://iga.in.gov/legislative/2024/bills/senate/17/details) and signed March 13, 2024, simultaneously establishes a new age verification mandate for adult-oriented websites and amends Indiana's breach notification statute ([IC 24-4.9](https://law.justia.com/codes/indiana/title-24/article-4-9/)) to treat age verification information collected under the new law as "personal information." Adult-oriented websites — defined as those where at least one-third of content qualifies as material harmful to minors — must implement a reasonable age verification method before permitting user access. Any operator that suffers a breach of age verification data collected under [IC 24-4-23](https://law.justia.com/codes/indiana/title-24/article-4/chapter-23/) must comply with Indiana's existing 45-day breach notification framework. The law was originally set to take effect July 1, 2024, was briefly enjoined, and became enforceable on August 16, 2024, when the Seventh Circuit lifted the preliminary injunction. The Indiana Attorney General subsequently filed enforcement actions against major adult content operators including PornHub.

## Background [MEDIUM confidence]

Indiana's preexisting breach notification law, codified at [IC 24-4.9](https://law.justia.com/codes/indiana/title-24/article-4-9/), imposes disclosure obligations on data owners whose systems experience a breach of "personal information." The statute was strengthened by HEA 1341 in 2022, which added a firm 45-day notification deadline — previously, the standard was only "without unreasonable delay" — and required concurrent notice to the Indiana Attorney General whenever consumer notification was sent. That framework covered classic data categories such as Social Security numbers, financial account information, and biometric identifiers.

The 2024 legislative session added a new dimension: age verification data. The impetus was growing legislative concern across the country about minors accessing sexually explicit content online. Indiana joined a wave of states — including Texas (whose law was at the center of the U.S. Supreme Court's June 2025 decision in *Free Speech Coalition v. Paxton*) — in requiring adult content platforms to verify user ages before allowing access. Because the age verification process necessarily involves collecting sensitive identifying documents, the legislature recognized that a data breach involving such information could inflict distinct harms on affected individuals.

## Detailed Analysis [MEDIUM confidence]

### Two Interrelated Laws in One Bill

[SB 17](https://iga.in.gov/legislative/2024/bills/senate/17/details) enacted two complementary regulatory regimes. First, it created [IC 24-4-23](https://law.justia.com/codes/indiana/title-24/article-4/chapter-23/), an entirely new chapter governing age verification for adult-oriented websites. Second, it amended [IC 24-4.9-2-10](https://law.justia.com/codes/indiana/title-24/article-4-9/chapter-2/section-24-4-9-2-10/) — the definition of "personal information" in the breach notification statute — to explicitly incorporate data collected under IC 24-4-23.

### Age Verification Mandate (IC 24-4-23)

Under the new chapter, an "adult oriented website operator" whose content is at least one-third material harmful to minors must use a [reasonable age verification method](https://law.justia.com/codes/indiana/title-24/article-4/chapter-23/section-24-4-23-7/) before permitting access. Qualifying methods include:

- A **mobile credential** (e.g., a mobile driver's license compliant with state and federal standards);
- An **independent third-party age verification service** that cross-references identifying information against commercially available databases used by government agencies and businesses for age and identity verification; or
- Any **commercially reasonable method** that relies on public or private transactional data, such as mortgage, education, or employment records.

Critically, the law prohibits any person conducting age verification from retaining identifying information of an individual seeking access. This data-minimization requirement is central to the privacy architecture: the statute assumes verification data will be collected temporarily but must not be retained. Despite this prohibition, the legislature was sufficiently concerned about the period of collection and transmission to include such data within the breach notification framework.

### Amendment to "Personal Information" Definition (IC 24-4.9-2-10)

The amendment adds, as a new category of personal information, information collected by an adult-oriented website operator — or its designee — under IC 24-4-23. This means that if an operator or its third-party verification vendor suffers an unauthorized acquisition of age verification records, the operator must:

1. Determine whether the breach creates a reasonable likelihood of harm to affected individuals;
2. Provide notice to each Indiana resident whose personal information was compromised;
3. Submit notification to the Indiana Attorney General no later than **45 days** after discovery of the breach; and
4. If over 1,000 Indiana residents are affected, also notify consumer reporting agencies.

The standard notification triggers and safe harbors under [IC 24-4.9-3-1](https://law.justia.com/codes/indiana/title-24/article-4-9/chapter-3/section-24-4-9-3-1/) apply equally to age verification data breaches.

### Enforcement Framework

The law creates two enforcement pathways. The **Indiana Attorney General** may seek an injunction and civil penalties up to $250,000, plus investigative costs. Separately, a **private right of action** exists: parents or guardians of a minor harmed by a violation of the age verification requirement may seek monetary damages, injunctive relief, and reasonable attorney's fees. Any other person may pursue injunctive relief and attorney's fees.

Violations of IC 24-4-23 are also treated as deceptive acts under Indiana's consumer protection framework, expanding the AG's enforcement toolkit.

### Effective Date and Litigation History [MEDIUM confidence]

- **Signed:** March 13, 2024.
- **Original effective date:** July 1, 2024.
- **Preliminary injunction issued:** June 30, 2024 (Southern District of Indiana), halting enforcement on First Amendment grounds.
- **Seventh Circuit stay of injunction:** August 16, 2024 — the law became enforceable on this date, pending the U.S. Supreme Court's resolution of the analogous Texas case.
- **U.S. Supreme Court ruling:** June 27, 2025 — the Court ruled 6-3 in *Free Speech Coalition v. Paxton* that Texas's age verification law is constitutional, as it imposes only an incidental burden on adults' protected speech while advancing the state's interest in shielding children from harmful content. The Seventh Circuit subsequently reversed the preliminary injunction against Indiana's law.
- **AG enforcement:** In December 2025, Indiana AG Todd Rokita filed suit in Marion Superior Court against the operators of PornHub and approximately 50 other adult websites for alleged violations of the age verification law.

## Impact Assessment [MEDIUM confidence]

### Affected Entities

The law has layered impacts across several categories of organizations:

**Adult-oriented website operators** — whether domestic or foreign — that make material harmful to minors available to Indiana residents must implement compliant age verification systems and assess whether they, or any third-party vendors they use, are capable of triggering breach notification obligations under IC 24-4.9.

**Third-party age verification vendors** — companies that provide age verification services to adult content platforms now handle data that constitutes "personal information" under Indiana law. These vendors should review their data security practices, contractual obligations with operator clients, and incident response procedures specifically for Indiana breach notification timelines.

**Data security and compliance counsel** — practitioners advising any entity in the digital identity, age verification, or adult content verticals should treat age verification data as a regulated data category in Indiana, equivalent in breach-notification weight to financial account numbers or biometric identifiers.

### Compliance Requirements

Organizations within scope should ensure:

- **Data security controls** meet reasonable standards for protecting age verification information during the collection and transmission window, even though retention is prohibited.
- **Breach response plans** are updated to include age verification data as a covered data category triggering the 45-day notification clock.
- **Vendor contracts** with age verification service providers include breach notification obligations, indemnification provisions, and data security standards consistent with IC 24-4.9.
- **Notice templates** and AG notification procedures address age verification data breaches, including use of the Indiana AG's [breach notification form](https://www.in.gov/attorneygeneral/consumer-protection-division/id-theft-prevention/security-breaches/security-breach-faqs-and-notification-form-for-businesses/).

### Enforcement Outlook

With the Supreme Court's 2025 ruling affirming age verification laws' constitutionality, Indiana's law now stands on solid legal footing. The AG's December 2025 enforcement actions against Aylo/PornHub signal an active enforcement posture. Organizations that have not yet implemented compliant age verification systems — or that have not assessed their breach notification obligations for this new data category — face material enforcement risk.

## Action Items

- Determine whether your platform or any platform you operate falls within Indiana's "adult oriented website operator" definition (one-third or more content is material harmful to minors).
- If within scope, implement a compliant reasonable age verification method before permitting Indiana user access; confirm that your chosen method does not retain identifying information post-verification.
- Update your data breach response plan and incident response runbook to include age verification data (collected under IC 24-4-23) as a personal information category subject to Indiana's 45-day notification requirement.
- Review contracts with third-party age verification vendors to ensure they include data security obligations, breach notification pass-through requirements, and appropriate indemnification.
- Confirm that breach notification procedures include concurrent AG notification to DataBreach@atg.in.gov within 45 days of breach discovery.
- Monitor ongoing enforcement actions by Indiana AG Rokita against adult content operators for guidance on how the AG interprets compliance obligations.
- If you provide age verification services to operators, assess whether your security controls are sufficient to protect regulated personal information and whether your breach response procedures meet the 45-day window.

## Related Reports

- [reports/cybersecurity/incident-reporting/utah-sb98-data-breach-notification-amendment-2024-05-14.md](reports/cybersecurity/incident-reporting/utah-sb98-data-breach-notification-amendment-2024-05-14.md) — Utah similarly amended its breach notification law in 2024 to expand covered personal information categories.
- [reports/cybersecurity/incident-reporting/pennsylvania-breach-notification-amendment-2024-06.md](reports/cybersecurity/incident-reporting/pennsylvania-breach-notification-amendment-2024-06.md) — Pennsylvania's 2024 breach notification amendments similarly expanded the personal information definition.

## Sources

1. [Indiana SB 17 (2024) — Indiana General Assembly](https://iga.in.gov/legislative/2024/bills/senate/17/details) — Official bill page for SB 17 (P.L. 98-2024), including signing history and text.
2. [IC 24-4-23 — Age Verification for Adult Oriented Websites (Justia 2024)](https://law.justia.com/codes/indiana/title-24/article-4/chapter-23/section-24-4-23-16/) — Official Indiana Code text for the new age verification chapter.
3. [IC 24-4.9-2-10 — "Personal Information" Definition (Justia 2025)](https://law.justia.com/codes/indiana/title-24/article-4-9/chapter-2/section-24-4-9-2-10/) — Statutory definition of personal information including the 2024 age verification amendment.
4. [IC 24-4.9-3-1 — Disclosure of Breach (Justia 2025)](https://law.justia.com/codes/indiana/title-24/article-4-9/chapter-3/section-24-4-9-3-1/) — Indiana's breach disclosure requirement and 45-day notification deadline.
5. [IC 24-4-23-7 — Reasonable Age Verification Method (Justia 2025)](https://law.justia.com/codes/indiana/title-24/article-4/chapter-23/section-24-4-23-7/) — Statutory definition of qualifying age verification methods.
6. [Indiana Amends Breach Notification Law Along with New Adult Website Verification Requirement — National Law Review](https://natlawreview.com/article/indiana-amends-breach-notification-law-along-new-adult-website-verification) — Sheppard Mullin law firm analysis summarizing the dual-component legislation.
7. [Indiana Amends Breach Notification Law Along with New Adult Website Verification Requirement — JD Supra (Sheppard Mullin)](https://www.jdsupra.com/legalnews/indiana-amends-breach-notification-law-4339887/) — Full Sheppard Mullin client alert with statute citations.
8. [Indiana Amends Breach Notification Law Along with New Adult Website Verification Requirement — Mondaq](https://www.mondaq.com/unitedstates/privacy-protection/1496906/indiana-amends-breach-notification-law-along-with-new-adult-website-verification-requirement) — Secondary law firm summary providing additional detail on the legislation's scope.
9. [Indiana Law Requiring Stricter Age Verification for Adult Websites Now in Effect — LPM (WFYI)](https://www.lpm.org/news/2024-08-16/indiana-law-requiring-stricter-age-verification-for-adult-websites-now-in-effect) — News coverage confirming August 16, 2024 enforcement commencement after Seventh Circuit lifted injunction.
10. [Porn Companies Sued for Alleged Violations of Indiana's Age Verification Law — The Indiana Lawyer](https://www.theindianalawyer.com/articles/ag-rokita-sues-porn-companies-for-alleged-violations-of-indianas-age-verification-law) — Coverage of AG Rokita's December 2025 enforcement action against Aylo/PornHub and approximately 50 other operators.
11. [Indiana Age Verification Law (SB 17): Key Impacts & Debate — Ondato](https://ondato.com/blog/indiana-age-verification/) — Industry perspective on the law's practical requirements for age verification service providers.
12. [Age Verification for Material Harmful to Minors — Indiana Courts Legislative Update](https://legislativeupdate.courts.in.gov/2024/03/28/age-verification-for-material-harmful-to-minors-3/) — Indiana judiciary's legislative summary of SB 17's requirements.
13. [Security Breach Notification Chart — Indiana, Perkins Coie](https://perkinscoie.com/insights/publication/security-breach-notification-chart-indiana) — Comprehensive summary of Indiana's IC 24-4.9 breach notification requirements including post-2024 amendments.
14. [Indiana AG Security Breach FAQ and Notification Form](https://www.in.gov/attorneygeneral/consumer-protection-division/id-theft-prevention/security-breaches/security-breach-faqs-and-notification-form-for-businesses/) — Official Indiana AG guidance and breach notification submission process.
15. [Indiana SB0017 — LegiScan](https://legiscan.com/IN/bill/SB0017/2024) — Legislative tracking page with bill text, amendment history, and vote records.
