---
title: "Maryland Enacts Comprehensive Privacy Law and Kids Code (MODPA + HB 603)"
date: 2024-05-16
jurisdiction: "Maryland"
category: "privacy"
development_type: "legislation"
finding_id: "SCAN-20240516-010"
topic_key: "maryland-82551d75-2024"
topic_type: "state_bill"
first_reported: 2024-05-16
last_updated: 2026-04-15
status_history:
  - "2026-04-15 (r1): Corrected state-count figure from 'approximately 19' to 'approximately 17' per contemporaneous law firm sources (DWT, Mintz); fixed source 12 description — Hunton article is a 2025 litigation piece, not a 2024 drafting-history source; replaced unsupported 'constitutional experts' claim with FPF-sourced account of structural drafting choices."
  - "2026-04-15 (r2): Corrected judge name from Robert Bennett to Richard D. Bennett in Ongoing Legal Challenges section; case number RDB-25-0322 initials confirm Richard D. Bennett as the presiding judge."
cluster: "Maryland MODPA and Kids Code (HB 567 / HB 603)"
cluster_slug: "maryland-modpa-kids-code-2024"
---

# Maryland Enacts Comprehensive Privacy Law and Kids Code (MODPA + HB 603)

**Jurisdiction:** Maryland | **Category:** Privacy | **Date:** 2024-05-16

> **Knowledge-Base Note:** This report covers the May 9, 2024 signing event. Three companion reports in this knowledge base provide deeper analysis of individual provisions and compliance workstreams. See [Related Reports](#related-reports) below. This memo focuses on the signing context, law firm alert landscape, and cross-references that were not captured in the earlier filings.

## Executive Summary [HIGH confidence]

On May 9, 2024, Maryland Governor Wes Moore signed two landmark privacy statutes on the same day: [House Bill 567 / Senate Bill 541 (the Maryland Online Data Privacy Act, "MODPA")](https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/hb0567?ys=2024RS) and [House Bill 603 (the Maryland Age-Appropriate Design Code Act, "Maryland Kids Code")](https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/hb0603?ys=2024RS). MODPA is widely regarded as the most stringent comprehensive state consumer privacy law in the United States, introducing an outright prohibition on the sale of sensitive data (with no consent carve-out), a service-tethered data minimization standard, and enforcement teeth via the Maryland Attorney General under the Consumer Protection Act. The Kids Code, modeled on the United Kingdom's Children's Code and California's AADC, requires privacy-by-design for online services likely to be accessed by children under 18 and imposes per-child penalties of up to $7,500 for intentional violations. MODPA took effect October 1, 2025, with AG enforcement commencing April 1, 2026. The Kids Code took effect October 1, 2024. Both laws are now subject to ongoing legal and compliance scrutiny.

## Background [HIGH confidence]

### Legislative Progression

Both bills passed the Maryland General Assembly on April 6–8, 2024, during the 2024 Regular Session:

- [House Bill 567 / Senate Bill 541 (MODPA)](https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/sb0541?ys=2024RS) — The enrolled bill text is available from the [Maryland General Assembly as a PDF](https://mgaleg.maryland.gov/2024RS/chapters_noln/ch_454_hb0567e.pdf).
- [House Bill 603 (Maryland Kids Code)](https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/hb0603?ys=2024RS) — The enrolled bill text is available [here](https://mgaleg.maryland.gov/2024RS/Chapters_noln/CH_461_hb0603t.pdf).

Governor Moore signed both bills on May 9, 2024, completing Maryland's dual-track approach to comprehensive privacy legislation. The simultaneous enactment was intentional: MODPA's heightened protections for minors under 18 and the Kids Code's design-based obligations were designed as complementary layers, with the Kids Code providing a standalone design-obligation framework and MODPA providing the underlying data-rights architecture.

### State Privacy Law Context

By May 2024, Maryland's enactment brought the total number of US states with comprehensive consumer privacy laws to approximately 17, making Maryland the seventeenth state, per contemporaneous analysis by [Davis Wright Tremaine](https://www.dwt.com/blogs/privacy--security-law-blog/2024/05/maryland-online-data-privacy-act-signed) and [Mintz](https://www.mintz.com/insights-center/viewpoints/2826/2024-05-16-maryland-enacts-sweeping-privacy-reform) (some sources count 18 depending on the sequencing of concurrent 2024 enactments, but no contemporaneous source places the count at 19). Maryland is notable within this cohort because it departed from the Virginia Consumer Data Protection Act (VCDPA) model that most states had adopted. The [Future of Privacy Forum described](https://fpf.org/blog/the-old-line-state-does-something-new-on-privacy/) the MODPA legislation as doing "something new on privacy" for its departure from the standard VCDPA template.

MODPA's thresholds — covering controllers that process data of 35,000 or more Maryland consumers annually, or 10,000 or more consumers while deriving over 20% of gross revenue from data sales — are among the lowest in any US state comprehensive privacy law. As [Davis Wright Tremaine observed](https://www.dwt.com/blogs/privacy--security-law-blog/2024/05/maryland-online-data-privacy-act-signed), the 35,000-consumer floor represents approximately 0.56% of Maryland's population, compared to Oregon's threshold of 2.35% and Colorado's of 1.72%, meaning MODPA covers a broader set of businesses than most analogous state laws.

## Detailed Analysis [HIGH confidence]

### MODPA: Key Structural Provisions

**Applicability.** MODPA applies to persons that conduct business in Maryland or provide products or services targeted to Maryland residents and that, during a calendar year: (1) control or process personal data of at least 35,000 Maryland consumers, excluding payment-only data; or (2) control or process data of at least 10,000 Maryland consumers and derive over 20% of gross revenue from selling personal data. Entity-level exemptions include financial institutions subject to [GLBA](https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/sb0541?ys=2024RS), and data-level exemptions include HIPAA-protected health information and FCRA-regulated data. Notably, MODPA does not categorically exempt non-profits or higher education institutions — only a narrow nonprofit exemption applies to organizations processing data solely to assist law enforcement investigations of insurance fraud or first responders in catastrophic events.

**Data Minimization — A New Paradigm.** MODPA's data minimization standard is its most structurally distinct provision. Controllers must limit data collection to what is "reasonably necessary and proportionate to provide or maintain a specific product or service requested by the consumer." This is stricter than the VCDPA and GDPR-inspired "adequate, relevant, and reasonably necessary in relation to disclosed purposes" standard. As [DWT noted](https://www.dwt.com/blogs/privacy--security-law-blog/2024/05/maryland-online-data-privacy-act-signed), it effectively ties permissible collection to what the consumer actively requested, foreclosing the common practice of collecting data for broadly stated business purposes.

**Sensitive Data — Absolute Sale Prohibition.** MODPA is the first US state law to impose an outright ban on selling sensitive personal data. Sensitive data includes biometric and genetic data, health data (including gender-affirming care and reproductive health), precise geolocation, data concerning children, racial or ethnic origin, citizenship and immigration status, national origin, religious beliefs, sex life or sexual orientation, and status as transgender or nonbinary. As [Perkins Coie analyzed](https://perkinscoie.com/insights/blog/new-privacy-paradigm-understanding-marylands-trailblazing-approach-online-privacy), consent does not override this prohibition — even an explicit opt-in from a consumer cannot authorize the sale of their sensitive data.

**Minor-Specific Protections.** MODPA prohibits businesses from selling personal data or engaging in targeted advertising when they know or should have known the consumer is under 18. Unlike other states that limit such protections to children under 13 or under 16, Maryland extends this to all individuals under 18, and it eliminates the opt-in consent exception that other states permit.

**Anti-Discrimination.** MODPA is among the first state privacy laws to include an explicit anti-discrimination provision, prohibiting data processing in ways that unlawfully discriminate on the basis of race, religion, national origin, sex, sexual orientation, or disability.

**Controller Obligations.** Controllers must: publish transparent privacy notices; perform data protection impact assessments (DPIAs) for high-risk activities (targeted advertising, profiling, sale of personal data, and processing of sensitive data); enter into processor contracts; honor consumer rights requests (access, correction, deletion, portability, opt-out); and recognize universal opt-out mechanisms.

**Enforcement and Penalties.** Exclusive enforcement authority rests with the Maryland Attorney General under the Maryland Consumer Protection Act. Violations are treated as unfair, deceptive, or abusive trade practices. Penalties reach up to $10,000 for first violations and $25,000 for subsequent violations. The AG has discretion to provide a 60-day cure notice for violations occurring on or before April 1, 2027, after which the cure period sunsets. There is no private right of action.

### Maryland Kids Code (HB 603): Key Structural Provisions

**Applicability.** The Kids Code applies to online service providers offering products "reasonably likely to be accessed by children" under 18. Rather than requiring age verification, providers must assess — using a variety of indicators — whether their service is likely to be accessed by children. This design-based, "likely to be accessed" standard differs from COPPA's actual-knowledge standard.

**Core Requirements.** Covered services must: (1) complete a data protection impact assessment (DPIA) identifying whether the service is reasonably likely to be accessed by children; (2) implement privacy by design and default; (3) configure the highest available privacy settings for children by default; (4) not use personal data of children in ways contrary to their best interests; and (5) not use dark patterns to induce children to provide more personal data than necessary.

**Comparison to California AADC.** The Kids Code is modeled on the United Kingdom's Age-Appropriate Design Code and California's 2022 AADC. California's AADC was preliminarily enjoined by a federal district court in September 2023 on First Amendment grounds in *NetChoice v. Bonta*. Maryland's HB 603 was drafted as an "AADC 2.0" framework with structural modifications intended to reduce that constitutional exposure: most significantly, the bill omits any obligation for businesses to verify or estimate user ages, relying solely on the "likely to be accessed by children" audience standard; and the Kids Code's obligations are tied to consumer protection statutes rather than content-regulation mechanisms. As the [Future of Privacy Forum analyzed](https://fpf.org/blog/new-age-appropriate-design-code-framework-takes-hold-in-maryland/), Maryland is the first state to enact an AADC 2.0 bill, though whether the First Amendment vulnerabilities have been cured remained an open question at the time of enactment. According to [TechPolicy.Press](https://www.techpolicy.press/maryland-kids-code-becomes-law/), experts noted the First Amendment risk remained and predicted litigation.

**Enforcement and Penalties.** The Maryland Attorney General enforces the Kids Code as UDAP violations. Penalties are up to $2,500 per child for negligent violations and $7,500 per child for intentional violations. Because penalties are assessed per-child, they can accumulate substantially for large-scale violations against services with many child users.

**Effective Date.** The Kids Code took effect October 1, 2024. DPIAs were required to be completed by April 1, 2026.

### Ongoing Legal Challenges to the Kids Code [MEDIUM confidence]

Notwithstanding Maryland's constitutional modifications, NetChoice (whose members include Google, Meta, and TikTok) filed a First Amendment lawsuit on February 3, 2025. In November 2025, [U.S. District Judge Richard D. Bennett denied Maryland's motion to dismiss](https://thedailyrecord.com/2025/12/01/maryland-kids-code-lawsuit-netchoice-first-amendment/) on November 24, 2025, finding that NetChoice had standing and had stated plausible First Amendment claims. The case — *NetChoice v. Brown* — is pending in the U.S. District Court for the District of Maryland. The [Hunton Andrews Kurth analysis](https://www.hunton.com/privacy-and-information-security-law/new-lawsuit-challenges-marylands-age-appropriate-design-code-act) of the lawsuit filing provides background on the claims asserted. The outcome will have national implications given parallel proceedings involving similar age-appropriate design codes in other states.

## Impact Assessment [HIGH confidence]

### Businesses Subject to MODPA

The combination of MODPA's low applicability thresholds (35,000 consumers), aggressive data minimization standard, and absolute sensitive data sale prohibition creates a materially higher compliance burden than any other US state privacy law except California's CCPA/CPRA. Organizations that have built compliance programs around the VCDPA model will need to:

- Audit existing data collection practices for alignment with the "reasonably necessary and proportionate to a requested product or service" standard (not merely disclosed purposes)
- Cease any sale of sensitive data, regardless of whether consent has been or could be obtained
- Expand minors' data protections to cover all individuals under 18
- Implement universal opt-out signal recognition

MODPA became enforceable on April 1, 2026. The 60-day cure period remains available through April 1, 2027.

### Businesses Subject to the Kids Code

Any online service — from social media to gaming to productivity apps — that may be accessed by users under 18 must assess its obligations under the Kids Code. The "likely to be accessed by children" standard is broader than COPPA's actual-knowledge standard and requires an affirmative assessment rather than simple age-gate implementation. The per-child penalty structure makes Kids Code exposure material for any service with a significant youth user base.

However, the Kids Code's constitutionality remains unresolved pending *NetChoice v. Brown*. Businesses facing compliance costs may wish to monitor that litigation closely while still preparing for compliance obligations.

### Compounding Obligations

Organizations subject to both MODPA and the Kids Code face overlapping and sometimes stricter obligations: both laws require DPIAs, both prohibit using data of minors for targeted advertising, and MODPA's absolute ban on selling sensitive data (including children's data) dovetails with the Kids Code's prohibitions on processing children's data contrary to their interests. The [Manatt analysis](https://www.manatt.com/insights/newsletters/privacy-and-data-security/now-in-effect-maryland-law-raises-bar-on-sensitive-data-data-minimization-and-children-s-privacy) confirms that a single violation can trigger penalties under both statutes simultaneously.

## Action Items

- Determine whether your organization meets MODPA's applicability thresholds (35,000 Maryland consumer data points annually, or 10,000 with 20%+ revenue from data sales). The thresholds are intentionally low.
- Audit data collection practices against MODPA's service-tethered data minimization standard — "reasonably necessary and proportionate to a requested product or service" is stricter than most existing US state privacy law standards.
- Immediately cease any commercial activity that involves selling sensitive data as MODPA defines it (including health data, precise geolocation, biometric data, and data concerning minors). No consent exception applies.
- Expand minor-data protections to cover all individuals under 18, not just those under 13 (COPPA threshold) or under 16.
- Assess whether any online products are "reasonably likely to be accessed by children" under the Kids Code standard and complete required DPIAs (the April 1, 2026 deadline has now passed; DPIAs should be completed immediately if not done).
- Implement universal opt-out mechanism recognition (e.g., GPC signal) for targeted advertising and data sales.
- Monitor *NetChoice v. Brown* (D. Md. No. RDB-25-0322) for rulings on Kids Code constitutionality.
- Engage privacy counsel to assess MODPA's anti-discrimination provision, which adds a dimension absent from most state privacy laws.

## Related Reports

- [reports/privacy/state-comprehensive-laws/maryland-sb541-modpa-2024-04-17.md](reports/privacy/state-comprehensive-laws/maryland-sb541-modpa-2024-04-17.md) -- In-depth analysis of MODPA's provisions, enforcement structure, and comparison to other state privacy laws; treats this as the nation's most stringent state privacy law.
- [reports/privacy/childrens-privacy/maryland-hb603-aadc-kids-code-2024-04-22.md](reports/privacy/childrens-privacy/maryland-hb603-aadc-kids-code-2024-04-22.md) -- Comprehensive analysis of the dual MODPA + Kids Code enactment package and its disruption of the VCDPA-model patchwork.
- [reports/privacy/childrens-privacy/maryland-aadc-kids-code-modpa-2024-05-15.md](reports/privacy/childrens-privacy/maryland-aadc-kids-code-modpa-2024-05-15.md) -- Focus on the UDAP penalty overlap between the Kids Code and MODPA, plus the November 2025 *NetChoice v. Brown* motion-to-dismiss ruling.
- [reports/privacy/state-comprehensive-laws/kentucky-hb692-acr-sensitive-data-2026-04-13.md](reports/privacy/state-comprehensive-laws/kentucky-hb692-acr-sensitive-data-2026-04-13.md) -- Kentucky's 2026 amendments to the KCDPA address sensitive data handling; comparison to MODPA's absolute sensitive data sale prohibition is relevant.

## Sources

1. [Maryland General Assembly — HB 0567 (MODPA) Legislation Page](https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/hb0567?ys=2024RS) -- Official Maryland legislative record for House Bill 567 (companion to SB 541); confirms passage and chapter assignment.
2. [Maryland General Assembly — HB 0567 Enrolled Bill Text (PDF)](https://mgaleg.maryland.gov/2024RS/chapters_noln/ch_454_hb0567e.pdf) -- Official enrolled bill text of MODPA.
3. [Maryland General Assembly — SB 0541 Legislation Page](https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/sb0541?ys=2024RS) -- Senate Bill 541, the MODPA companion; official legislative record.
4. [Maryland General Assembly — HB 0603 (Kids Code) Legislation Page](https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/hb0603?ys=2024RS) -- Official Maryland legislative record for House Bill 603 (Kids Code).
5. [Maryland General Assembly — HB 0603 Enrolled Bill Text (PDF)](https://mgaleg.maryland.gov/2024RS/Chapters_noln/CH_461_hb0603t.pdf) -- Official enrolled text of the Maryland Age-Appropriate Design Code Act.
6. [Davis Wright Tremaine — "Maryland Creates a New Paradigm for Data Privacy"](https://www.dwt.com/blogs/privacy--security-law-blog/2024/05/maryland-online-data-privacy-act-signed) -- Law firm analysis of MODPA's signing; identifies Maryland as the seventeenth state; covers applicability thresholds and data minimization standard.
7. [Future of Privacy Forum — "The Old Line State Does Something New on Privacy"](https://fpf.org/blog/the-old-line-state-does-something-new-on-privacy/) -- Non-profit policy analysis confirming Maryland's departure from the VCDPA model.
8. [Future of Privacy Forum — "New Age-Appropriate Design Code Framework Takes Hold in Maryland"](https://fpf.org/blog/new-age-appropriate-design-code-framework-takes-hold-in-maryland/) -- FPF analysis of HB 603 as an "AADC 2.0" framework; explains structural drafting choices made in response to California AADC First Amendment vulnerability.
9. [Perkins Coie — "A New Privacy Paradigm: Understanding Maryland's Trailblazing Approach to Online Privacy"](https://perkinscoie.com/insights/blog/new-privacy-paradigm-understanding-marylands-trailblazing-approach-online-privacy) -- Law firm analysis emphasizing the sensitive data sale prohibition and its non-waivable nature.
10. [Perkins Coie — "Are You Ready for October 1? Maryland's Data Privacy Law Sets New Standards For Compliance"](https://perkinscoie.com/insights/blog/are-you-ready-october-1-marylands-data-privacy-law-sets-new-standards-compliance) -- Pre-enforcement compliance guidance; confirms cure period structure and April 2026 enforcement start.
11. [Manatt, Phelps & Phillips — "Now in Effect: Maryland Law Raises Bar on Sensitive Data, Data Minimization and Children's Privacy"](https://www.manatt.com/insights/newsletters/privacy-and-data-security/now-in-effect-maryland-law-raises-bar-on-sensitive-data-data-minimization-and-children-s-privacy) -- Post-effective-date analysis confirming dual penalty exposure under both MODPA and Kids Code.
12. [Hunton Andrews Kurth — "New Lawsuit Challenges Maryland's Age-Appropriate Design Code Act"](https://www.hunton.com/privacy-and-information-security-law/new-lawsuit-challenges-marylands-age-appropriate-design-code-act) -- February 2025 coverage of the NetChoice v. Brown lawsuit filing; background on the First Amendment claims asserted against the Kids Code.
13. [TechPolicy.Press — "Maryland Kids Code Becomes Law"](https://www.techpolicy.press/maryland-kids-code-becomes-law/) -- News coverage noting the residual constitutional risks despite Maryland's modifications.
14. [The Daily Record — "Big Tech Lawsuit Over MD 'Kids Code' Can Move Forward"](https://thedailyrecord.com/2025/12/01/maryland-kids-code-lawsuit-netchoice-first-amendment/) -- Reports on U.S. District Court denial of Maryland's motion to dismiss in *NetChoice v. Brown* (Nov. 24, 2025).
15. [Troutman Pepper — "District Court Denies Motion to Dismiss Challenge to Maryland's Kids Code"](https://www.troutmanprivacy.com/2025/11/district-court-denies-motion-to-dismiss-challenge-to-marylands-kids-code/) -- Law firm analysis of the *NetChoice v. Brown* motion-to-dismiss ruling.
16. [OneTrust — "Maryland's Online Data Privacy Act (MODPA) Key Rules & Requirements"](https://www.onetrust.com/blog/marylands-online-data-privacy-act-modpa-key-rules-and-requirements/) -- Compliance platform analysis; used for applicability threshold comparisons across states.
17. [DLA Piper — "US: Maryland Online Data Privacy Act Summary and Comparative Analysis"](https://www.dlapiper.com/en-us/insights/publications/2024/07/us-maryland-online-data-privacy-act-summary-and-comparative-analysis) -- Law firm summary and cross-state comparison; used for GLBA and nonprofit exemption analysis.
18. [Mintz — "Maryland Enacts Sweeping Privacy Reform"](https://www.mintz.com/insights-center/viewpoints/2826/2024-05-16-maryland-enacts-sweeping-privacy-reform) -- Law firm alert dated same day as the finding; identifies Maryland as the seventeenth state; independent confirmation of signing date and key provisions.
