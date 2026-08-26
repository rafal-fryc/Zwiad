---
title: "Age Signals Under New York's Children's Privacy Laws: How Platforms Must Detect Minors"
date: 2024-11-04
jurisdiction: "New York"
category: "privacy"
development_type: "guidance"
finding_id: "SCAN-20241104-024"
topic_key: "new-york-a7ae8cb1-2024"
topic_type: "guidance"
first_reported: 2024-11-04
last_updated: 2026-04-22
status_history:
  - "2026-04-22: Corrected covered operator definition (removed erroneous 1M account-holder threshold); clarified Governor Hochul signing date as June 20, 2024."
cluster: "New York SAFE for Kids Act and Child Data Protection Act (S7694-A / S7695-A)"
cluster_slug: "new-york-safe-kids-act-child-data-protection-act"
---

# Age Signals Under New York's Children's Privacy Laws: How Platforms Must Detect Minors

**Jurisdiction:** New York | **Category:** Privacy | **Date:** November 4, 2024

## Executive Summary [HIGH confidence]

New York's two landmark children's privacy statutes — the [Stop Addictive Feeds Exploitation (SAFE) for Kids Act](https://www.nysenate.gov/legislation/bills/2023/S7694/amendment/A) (S7694-A) and the [New York Child Data Protection Act](https://www.nysenate.gov/legislation/bills/2023/S7695/amendment/A) (S7695-A), both signed by Governor Kathy Hochul on June 20, 2024 — impose distinct but overlapping obligations on online platforms to determine whether a user is under 18. The SAFE for Kids Act requires social media platforms to use "commercially reasonable and technically feasible methods" to confirm users are adults before delivering algorithmic content feeds or nighttime push notifications to them. The Child Data Protection Act introduces a novel "age flag" mechanism that obligates any online service to treat a user as a minor whenever the user's device or browser transmits a signal indicating minor status. Together, these two provisions create a layered age-detection framework that extends well beyond the federal Children's Online Privacy Protection Act (COPPA), which covers only under-13 users. Platforms serving New York users must assess which law applies to their service, understand the different age-determination triggers under each statute, and prepare for ongoing rulemaking by the New York Attorney General (OAG) that will specify approved methods and technical standards.

## Background [HIGH confidence]

### The Two Statutes and Their Structure

New York's pair of children's privacy laws represent two distinct regulatory philosophies operating in tandem. The SAFE for Kids Act targets the mechanism of harm — algorithmic amplification to minors — and places the obligation primarily on social media platforms. The Child Data Protection Act targets the data collection relationship more broadly, applying to any operator that has "actual knowledge" of a minor user or runs a service primarily directed to minors.

Both bills passed the New York Assembly on June 7, 2024, and Governor Hochul signed both into law on June 20, 2024. The [New York State Senate Bill S7694-A](https://www.nysenate.gov/legislation/bills/2023/S7694/amendment/A) (SAFE for Kids Act) and [Senate Bill S7695-A](https://www.nysenate.gov/legislation/bills/2023/S7695/amendment/A) (Child Data Protection Act) delegated broad rulemaking authority to the OAG to specify the technical and procedural details — including permissible age-determination methods — before regulated obligations become fully enforceable.

### Federal Baseline and State Departure

At the federal level, [COPPA](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/childrens-online-privacy-protection-rule) covers only children under 13 and triggers primarily from an operator's actual knowledge or from operating a service directed to children. New York's laws break from this model in two ways: first, by extending protection to all users under 18 (not just under 13); and second, by creating affirmative age-detection obligations rather than waiting for operators to acquire knowledge passively. The result is a far more demanding compliance posture for any platform serving New York residents.

### Rulemaking Timeline

The OAG issued two [Advanced Notices of Proposed Rulemaking (ANPRMs)](https://ag.ny.gov/resources/individuals/consumer-issues/technology/protecting-children-online) on August 1, 2024 — one for each statute — soliciting input on age-determination methods, verifiable parental consent mechanisms, and related technical questions. The public comment period closed September 30, 2024. Following that comment period, the OAG issued a formal Notice of Proposed Rulemaking (NPRM) for the SAFE for Kids Act in [September 2025](https://ag.ny.gov/press-release/2025/attorney-general-james-releases-proposed-rules-safe-kids-act-restrict-addictive), with a 60-day comment period closing December 1, 2025. The SAFE for Kids Act will take effect 180 days after the OAG finalizes those regulations, making the earliest possible effective date for the SAFE for Kids Act's age-verification requirements late 2026 or early 2027. The Child Data Protection Act became effective June 20, 2025.

## Detailed Analysis [HIGH confidence]

### How the SAFE for Kids Act Triggers Age-Determination Obligations

The [SAFE for Kids Act](https://www.nysenate.gov/legislation/bills/2023/S7694/amendment/A) prohibits a "covered operator" — defined as any operator of an "addictive social media platform," meaning a service that offers an algorithmic feed as a significant part of its services — from providing an "addictive feed" to any user the operator knows or reasonably should know is a minor, unless the operator has either:

1. Applied "commercially reasonable and technically feasible methods" to determine the user is not a minor; or
2. Obtained verifiable parental consent.

An "addictive feed" is defined broadly as a service or feature where media generated or shared by users is recommended, selected, or prioritized for display based on information associated with the user or their device — capturing essentially all social media algorithmic recommendation systems. There is no numeric account-holder floor in the statute; any operator of such a platform is subject to the law.

The age-determination obligation is therefore triggered by the decision to serve an algorithmic feed at all. A platform that delivers personalized feeds must have a defensible basis for concluding each recipient is an adult, or must have parental consent on file. The statute does not prescribe specific methods; that is left to OAG rulemaking.

The proposed rules released by the OAG in September 2025 indicate that platforms will have significant flexibility in choosing age-verification methods — including image/video upload, cross-referencing email or phone data against age-predictive databases, or government ID — provided the chosen method meets an effectiveness floor. According to [analysis by City & State New York](https://www.cityandstateny.com/policy/2025/09/heres-how-ny-plans-regulate-kids-use-social-media/408108/), the proposed rules would require platforms to implement methods that detect circumvention attempts with a minimum 98% success rate. The OAG has also indicated that at least one approved method must not require government ID and must allow users to remain anonymous to the platform.

### The Child Data Protection Act's "Age Flag" Mechanism [HIGH confidence]

The [Child Data Protection Act](https://www.nysenate.gov/legislation/bills/2023/S7695/amendment/A) takes a different approach to age signaling. The statute applies to operators who collect, maintain, or allow the collection of personal data from New York users under 18 — either because the service is primarily directed to minors or because the operator has "actual knowledge" that a specific user is a minor. Critically, the CDPA adds a third trigger: operators must treat a user as a covered minor if the user's "device or browser sends a signal — such as a privacy setting or plug-in — indicating that the user is (or should be treated as) a minor."

This "age flag" provision is conceptually novel in US children's privacy law. Age flags may take the form of:

- A browser plug-in installed by a parent or the minor;
- A privacy setting on the operating system or browser;
- A device-level setting; or
- Any other mechanism that complies with OAG regulations to be promulgated.

As [Loeb & Loeb noted](https://www.loeb.com/en/insights/publications/2024/07/new-york-governor-signs-legislation-to-protect-minors-online) upon the law's signing, this requirement "is likely to spur new technical compliance innovations and challenges for platforms and publishers." Even a general-audience platform that does not primarily target children becomes obligated under the CDPA once it receives an age flag from any user's device — it cannot simply ignore the signal.

The OAG has acknowledged the implementation complexity of the age-flag provision. In its implementation guidance, the OAG stated it will exercise discretion on age-flag enforcement "until the OAG promulgates rules clarifying operators' responsibilities with respect to age flags, so long as operators otherwise exhibit good-faith efforts to comply with all other provisions of [the Act]." This is an important safe harbor for platforms attempting good-faith compliance in advance of final rules.

### Contrast: The Two Statutes' Age-Detection Frameworks [MEDIUM confidence]

The two laws differ in meaningful ways that create distinct compliance tracks:

| Dimension | SAFE for Kids Act | Child Data Protection Act |
|---|---|---|
| **Covered entities** | Any operator of an addictive social media platform (algorithmic feed as a significant part of services) | Any online service; primarily directed to minors or actual knowledge of minor |
| **Age threshold** | Under 18 | Under 18 (parental consent for under 13; teen consent for 13-17) |
| **Age-detection trigger** | Serving an addictive feed | Actual knowledge OR age flag from device/browser |
| **Methods prescribed** | OAG rulemaking (98% circumvention-detection floor proposed) | OAG rulemaking pending; age flags described by statute |
| **Consent mechanism** | Verifiable parental consent as alternative to age determination | Informed consent from teen (13-17); verifiable parental consent for under 13 |
| **Effective date** | 180 days after OAG finalizes rules (est. late 2026 / early 2027) | June 20, 2025 |

The divergence in consent models is especially challenging: under the SAFE for Kids Act, a parent grants consent; under the CDPA, a teen aged 13-17 provides their own informed consent. As [Holland & Knight observed](https://www.hklaw.com/en/insights/publications/2024/10/new-york-new-laws-with-strict-data-requirements-for), platforms subject to both laws will need to build consent workflows that satisfy both regimes simultaneously.

### Age-Determination Methods: A Technical Taxonomy [MEDIUM confidence]

The OAG's ANPRM and subsequent stakeholder commentary identified three broad categories of age assurance:

1. **Age declaration** — the user self-reports their age. Low friction but easily circumvented; unlikely to satisfy the SAFE for Kids Act's "commercially reasonable" standard on its own.

2. **Age estimation** — algorithms infer age from behavioral signals, facial analysis, or device/account metadata without requiring the user to supply identity documents. Privacy-protective but variable in accuracy; biometric-based methods raise separate regulatory concerns.

3. **Age verification** — the user supplies authoritative proof of age, such as a government ID, credit card attestation, or third-party identity check. Most reliable but creates significant data collection and privacy risks.

The OAG's ANPRM explicitly invited comment on each category's "commercially reasonable and technically feasible" characteristics. [EPIC's submission](https://epic.org/epic-urges-ny-attorney-general-to-center-data-minimization-and-age-determination-best-practices-in-rulemaking-for-ny-safe-for-kids-act/) recommended that OAG prioritize data minimization — for example, where a government ID is used, only the birth year should be extracted, not the full document. EPIC also recommended that age determination not be a mandatory gatekeeping step: a platform that eliminates addictive feeds and nighttime notifications entirely would have no need to verify ages at all.

The [Future of Privacy Forum's comments](https://fpf.org/blog/fpf-submits-comments-to-inform-new-york-childrens-privacy-rulemaking-processes/) similarly warned that each method "has its own challenges and risks that should be carefully balanced across the state interest in protecting minors online and the state of current technologies, and end-user realities." The FPF comments highlighted that some forms of age estimation — particularly behavioral analysis — could themselves constitute the very kind of data profiling the CDPA seeks to restrict.

### First Amendment and Civil Liberties Considerations [MEDIUM confidence]

The [Center for Democracy and Technology (CDT)](https://cdt.org/insights/cdt-urges-ny-state-to-mitigate-risks-of-safe-for-kids-act/) filed comments urging the OAG to include safeguards to protect New York residents' free expression and privacy rights. CDT noted that mandatory age verification systems collect sensitive personal data and may deter constitutionally protected speech by users who decline to provide identity documents. CDT recommended that any approved age-determination method be accompanied by: strict data minimization requirements; prohibition on secondary use of age-determination data; anonymous verification alternatives; and independent audits of verification vendors.

These concerns mirror First Amendment challenges being litigated against similar state laws in other jurisdictions (e.g., the [Ninth Circuit's analysis](https://reports/privacy/childrens-privacy/california-caadca-ninth-circuit-dpia-2024-08-20.md) of California's Age-Appropriate Design Code).

## Impact Assessment [HIGH confidence]

### Entities Affected

The two statutes collectively affect a wide range of online services operating in New York:

- **Social media platforms offering algorithmic feeds** (SAFE for Kids Act): Any operator of an addictive social media platform must implement age-determination systems before delivering personalized feeds to any user whose minor status cannot be ruled out with "commercially reasonable" certainty.
- **General-audience web services** (CDPA age flag): Must monitor for and honor device-level age flags, even if the service is not primarily directed to children.
- **Children's services** (CDPA primarily directed to minors): Face the full data minimization, consent, and data-sale restriction requirements under the CDPA regardless of age signals.
- **Third-party age-verification vendors**: Will face scrutiny under OAG regulations governing data minimization and secondary use of verification data.

### Compliance Requirements and Timelines

The CDPA has been in effect since June 20, 2025. Operators of services primarily directed to minors must currently comply with data minimization obligations, the prohibition on selling minors' data without consent, and the actual-knowledge arm of the coverage trigger. The age-flag enforcement discretion period means platforms can defer engineering age-flag detection infrastructure until OAG issues clarifying rules, but good-faith compliance efforts should be documented.

The SAFE for Kids Act's age-verification requirements await OAG finalization of regulations (comment period closed December 1, 2025). Platforms should use the rulemaking period to inventory their algorithmic feed products, assess current age-detection capabilities, and evaluate vendor solutions against the proposed 98% circumvention-detection floor.

### Enforcement Outlook

Both statutes vest sole enforcement authority in the OAG. The OAG has [actively engaged](https://ag.ny.gov/resources/individuals/consumer-issues/technology/protecting-children-online) on children's privacy as a signature priority of Attorney General Letitia James's tenure. No private right of action exists under either statute. Civil penalties under the CDPA can reach $5,000 per violation. The SAFE for Kids Act's penalty structure will be confirmed in final rules.

## Action Items

- Classify your service: determine whether it is a "covered operator" under the SAFE for Kids Act (any operator of an addictive social media platform — a service offering an algorithmic feed as a significant part of its services), "primarily directed to minors" under the CDPA, or subject to the CDPA due to actual knowledge of or age flags from specific users.
- Audit existing age-detection and age-gating mechanisms against the SAFE for Kids Act's "commercially reasonable" standard and begin vendor evaluation for compliant age-assurance solutions.
- Implement monitoring for device-level age flag signals (browser plug-ins, OS privacy settings) as a precaution even before OAG finalizes age-flag regulations; document good-faith efforts.
- Map parental and teen consent workflows separately for the two statutes: the SAFE for Kids Act requires verifiable parental consent; the CDPA requires teen informed consent for 13-17 year olds and parental consent for under-13.
- Review data minimization obligations under the CDPA for any data currently collected from users who may be minors; establish retention limits and prohibitions on sale.
- Monitor OAG rulemaking: track the SAFE for Kids Act NPRM for final rule publication, which will set the 180-day countdown to that law's effective date.
- Brief product and engineering teams on the 98% circumvention-detection floor in the proposed SAFE for Kids Act rules; begin scoping technical architecture changes now.

## Related Reports

- [New York Attorney General Opens Public Consultation on Child Online Safety Laws](reports/privacy/childrens-privacy/new-york-safe-kids-child-data-anprm-2024-08-19.md) — Covers the August 2024 ANPRMs that launched the rulemaking process underpinning this analysis; essential prior reading for understanding the age-determination regulatory framework.
- [Maryland Age-Appropriate Design Code and MODPA](reports/privacy/childrens-privacy/maryland-aadc-kids-code-modpa-2024-05-15.md) — Maryland's comparable age-appropriate design code and its data protection impact assessment requirements; useful comparative reference for platform compliance teams.
- [California CAADCA Ninth Circuit DPIA Decision](reports/privacy/childrens-privacy/california-caadca-ninth-circuit-dpia-2024-08-20.md) — Ninth Circuit analysis of California's AADC raises First Amendment considerations directly relevant to New York's age-verification mandates.
- [COPPA Amendments Compliance Deadline](reports/privacy/childrens-privacy/coppa-amendments-compliance-deadline-2026-04-13.md) — Federal COPPA rulemaking context that forms the baseline from which both New York statutes depart.

## Sources

1. [NY State Senate Bill S7694-A — SAFE for Kids Act (official text)](https://www.nysenate.gov/legislation/bills/2023/S7694/amendment/A) — Full text of the Stop Addictive Feeds Exploitation for Kids Act as enacted.
2. [NY State Senate Bill S7695-A — Child Data Protection Act (official text)](https://www.nysenate.gov/legislation/bills/2023/S7695/amendment/A) — Full text of the New York Child Data Protection Act as enacted.
3. [Child Data Protection Act — NY AG PDF (official)](https://ag.ny.gov/sites/default/files/2024-08/child-data-protection-act.pdf) — OAG publication of the enacted CDPA statute text.
4. [SAFE for Kids Act ANPRM — NY AG PDF (official)](https://ag.ny.gov/sites/default/files/2024-08/safe-forkidsact.pdf) — OAG's August 2024 ANPRM soliciting comment on age-determination methods.
5. [NY AG — Protecting Children Online (official resource page)](https://ag.ny.gov/resources/individuals/consumer-issues/technology/protecting-children-online) — OAG portal for both children's privacy statutes and rulemaking.
6. [NY AG Press Release — SAFE for Kids Act NPRM (September 2025)](https://ag.ny.gov/press-release/2025/attorney-general-james-releases-proposed-rules-safe-kids-act-restrict-addictive) — Formal NPRM announcement with proposed rules and public comment period.
7. [NY AG — Child Data Protection Act Implementation Guidance](https://ag.ny.gov/child-data-protection-act-guidance) — OAG guidance issued ahead of the CDPA's June 20, 2025 effective date.
8. [Davis Wright Tremaine — Empire State of Minding the Minors](https://www.dwt.com/blogs/privacy--security-law-blog/2024/06/child-online-safety-and-data-privacy-in-new-york) — Law firm analysis of both statutes published at signing; detailed on age flag provisions.
9. [Loeb & Loeb — New York Governor Signs Legislation to Protect Minors Online](https://www.loeb.com/en/insights/publications/2024/07/new-york-governor-signs-legislation-to-protect-minors-online) — Law firm alert covering age flag compliance challenges.
10. [Holland & Knight — New York New Laws with Strict Data Requirements for Children](https://www.hklaw.com/en/insights/publications/2024/10/new-york-new-laws-with-strict-data-requirements-for) — Analysis of diverging consent frameworks under the two statutes.
11. [FPF — Submits Comments to Inform New York Children's Privacy Rulemaking](https://fpf.org/blog/fpf-submits-comments-to-inform-new-york-childrens-privacy-rulemaking-processes/) — Future of Privacy Forum rulemaking comments discussing risks and tradeoffs of age-assurance methods.
12. [EPIC — Urges NY AG to Center Data Minimization and Age Determination Best Practices](https://epic.org/epic-urges-ny-attorney-general-to-center-data-minimization-and-age-determination-best-practices-in-rulemaking-for-ny-safe-for-kids-act/) — EPIC rulemaking comments with technical recommendations on age-determination data minimization.
13. [CDT — Urges NY State to Mitigate Risks of SAFE for Kids Act](https://cdt.org/insights/cdt-urges-ny-state-to-mitigate-risks-of-safe-for-kids-act/) — Civil liberties critique of mandatory age-verification requirements and recommended safeguards.
14. [Inside Privacy — New York Begins Rulemaking for Two Children's Data Privacy Laws](https://www.insideprivacy.com/childrens-privacy/new-york-begins-rulemaking-for-two-childrens-data-privacy-laws/) — Covington law firm coverage of the ANPRM process.
15. [City & State New York — How NY Plans to Regulate Kids' Use of Social Media](https://www.cityandstateny.com/policy/2025/09/heres-how-ny-plans-regulate-kids-use-social-media/408108/) — Reporting on the proposed SAFE for Kids Act rules including the 98% circumvention-detection standard.
16. [Goodwin — New York's Child Data Protection Act Is Now In Effect](https://www.goodwinlaw.com/en/insights/publications/2025/06/alerts-practices-dpc-new-yorks-child-data-protection-act-now-effect) — Law firm alert on CDPA compliance obligations as of June 20, 2025.
