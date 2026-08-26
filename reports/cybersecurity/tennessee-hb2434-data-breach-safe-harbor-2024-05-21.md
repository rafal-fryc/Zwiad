---
title: "Tennessee HB 2434: Data Breach Class Action Safe Harbor (Public Chapter 991)"
date: 2024-05-30
jurisdiction: "Tennessee"
category: "cybersecurity"
development_type: "legislation"
finding_id: "SCAN-20240530-003"
topic_key: "tennessee-ed9d585a-2024"
topic_type: "state_bill"
first_reported: 2024-05-30
last_updated: 2026-04-15
status_history:
  - "2026-04-15: Corrected TIPA effective date from 'July 2024' to 'July 1, 2025'; added full sponsor names (Bryan Terry, Shane Reeves); confirmed Title 47 amendment reference against enrolled bill title (Round 1 reviewer feedback)."
cluster: "Tennessee HB 2434: Data Breach Class Action Safe Harbor"
cluster_slug: "tennessee-hb-2434-data-breach-safe-harbor"
---

# Tennessee HB 2434: Data Breach Class Action Safe Harbor (Public Chapter 991)

**Jurisdiction:** Tennessee | **Category:** Cybersecurity | **Date:** May 21, 2024

## Executive Summary [HIGH confidence]

On May 21, 2024, Tennessee Governor Bill Lee signed [House Bill 2434](https://www.capitol.tn.gov/Bills/113/Bill/HB2434.pdf) into law as [Public Chapter 991](https://publications.tnsosfiles.com/acts/113/pub/pc0991.pdf), creating a sweeping class action safe harbor for private entities that suffer cybersecurity incidents. The law amends Tennessee Code Annotated (TCA) Titles 29 and 47 to prohibit class action lawsuits against private entities arising from a "cybersecurity event" unless plaintiffs can prove the entity acted with willful and wanton misconduct or gross negligence — a standard significantly more demanding than the ordinary negligence benchmark previously applicable. Unlike comparable safe harbor statutes in Ohio and Utah, Tennessee's law imposes no affirmative cybersecurity program requirements: businesses need not adopt a specific framework, maintain a written security policy, or demonstrate compliance with any standard to invoke the protection. Analysts widely regard this as the most business-protective data breach class action statute in the nation, though consumer advocates argue it leaves breach victims with a practically insurmountable litigation hurdle.

## Background [HIGH confidence]

### Legislative Context and Catalyst

Tennessee's HB 2434 emerged against the backdrop of two devastating ransomware attacks on Nashville-area healthcare providers in early 2024. Change Healthcare — a subsidiary of UnitedHealth Group with operations tied to Nashville — suffered a major ransomware attack in February 2024 that disrupted prescription processing across the United States, exposing the data of tens of millions of patients. Ascension Saint Thomas, a major Nashville hospital system, was struck by a ransomware attack in May 2024 that forced ambulance diversions and suspended access to electronic health records. Both entities faced numerous class action lawsuits, directly motivating the legislature to act.

State Representative Bryan Terry (House) and Senator Shane Reeves (Senate) introduced companion bills HB 2434 and [SB 2018](https://legiscan.com/TN/bill/SB2018/2023), respectively, during the 113th General Assembly (2023–2024). The bills moved quickly through committee. The House passed HB 2434 on April 22, 2024, with a 76–18 vote; the Senate conformed to HB 2434 and passed it on April 24, 2024, with a 25–5 vote. Governor Lee signed the bill into law on May 21, 2024, effective immediately upon signing. The [Tennessee General Assembly's bill information page](https://wapp.capitol.tn.gov/apps/Billinfo/default.aspx?BillNumber=HB2434&ga=113) confirms assignment of Public Chapter Number 991.

### Existing State Safe Harbor Landscape

Before HB 2434, a small but growing set of states had enacted cybersecurity safe harbor laws — all framed as affirmative defenses conditioned on maintaining a qualifying security program:

- **Ohio** (2018, [ORC § 1354.02](https://codes.ohio.gov/ohio-revised-code/section-1354.02)): Affirmative defense for entities that create, maintain, and comply with a written cybersecurity program conforming to a recognized framework (NIST CSF, ISO 27001, PCI-DSS, HIPAA, etc.). Framework updates must be incorporated within six months.
- **Utah** (2021): Similar affirmative defense requiring "reasonable compliance" with a cybersecurity program conforming to a recognized framework; uses "reasonably complies" rather than Ohio's stricter "complies" formulation.
- **Connecticut** (2021): Affirmative defense in tort actions conditioned on maintaining a cybersecurity program meeting certain framework standards.

Tennessee's law breaks from this pattern entirely: it provides a class-action immunity rather than an affirmative defense, and it imposes no cybersecurity program requirement whatsoever.

## Detailed Analysis [HIGH confidence]

### Statutory Text and New Code Sections

HB 2434 amends TCA Title 29 (Civil Procedure and Courts) and Title 47 (Commercial Instruments and Transactions) by adding a new section codified at **T.C.A. § 29-34-215**. The enrolled bill is formally titled "AN ACT to amend Tennessee Code Annotated, Title 29 and Title 47, relative to civil liability," confirming both titles are within scope. The operative provisions are:

- **§ 29-34-215(b):** "A private entity is not liable in a class action lawsuit resulting from a cybersecurity event unless the cybersecurity event was caused by willful and wanton misconduct or gross negligence on the part of the private entity."

Key definitions (§ 29-34-215(a)):

- **"Cybersecurity event"** (§ 29-34-215(a)(1)): "An event resulting in unauthorized access to, or disruption or misuse of, an information system or nonpublic information stored on an information system." This is deliberately broad, covering ransomware, unauthorized access, exfiltration, and system disruption — regardless of how the breach occurred.
- **"Private entity"** (§ 29-34-215(a)(4)): "A corporation, religious or charitable organization, association, partnership, limited liability company, limited liability partnership, or other private business entity, whether organized for-profit or not-for-profit." The law extends its protection to non-profits, including hospitals and health systems.
- **"Information system"** and **"nonpublic information"**: Defined broadly to encompass electronic records containing personally identifiable information, financial data, and other sensitive categories.

The [official bill text](https://www.capitol.tn.gov/Bills/113/Bill/HB2434.pdf) (Tennessee General Assembly) and the [enrolled Public Chapter 991](https://publications.tnsosfiles.com/acts/113/pub/pc0991.pdf) (Tennessee Secretary of State) are the authoritative sources.

### The Gross Negligence Standard: Legal Significance

The elevation from ordinary negligence to willful and wanton misconduct or gross negligence is the law's central innovation. Under Tennessee common law, **gross negligence** requires proof of a defendant's subjective mental state — conscious indifference to the probability of harm — going well beyond a failure to exercise reasonable care. As the [Pierson Ferdinand analysis](https://pierferd.com/insights/it-takes-more-than-negligence-to-file-a-class-action-after-a-cybersecurity-event-in-tennessee) explains, a class action plaintiff would need to show not merely that the defendant lacked adequate security controls, but that it was subjectively aware of a serious gap and consciously disregarded the resulting risk.

**Practical illustration:** To survive dismissal, a plaintiff's attorney would need to demonstrate, for example, that a company knew its multi-factor authentication (MFA) was disabled, understood that the absence of MFA created a high probability of breach, and consciously declined to re-enable it. Mere evidence that the company lacked MFA — even if industry-standard — would be insufficient under the new standard.

The [Holland & Knight analysis](https://www.hklaw.com/en/insights/publications/2024/06/new-tennessee-law-creates-heightened-liability-requirement) notes that this is a class-action-specific rule: individual tort claims (not brought as class actions) continue to be governed by ordinary negligence standards. The law therefore does not eliminate data breach liability altogether; it specifically raises the bar for class certification and class-wide recovery.

### No Affirmative Cybersecurity Program Requirement

Unlike every comparable state safe harbor law, HB 2434 contains no affirmative security program requirement. A private entity need not:

- Maintain a written cybersecurity policy
- Adopt or conform to any recognized framework (NIST CSF, ISO 27001, SOC 2, etc.)
- Employ any particular technical safeguard
- Document a security incident response plan

This distinguishes Tennessee's approach from Ohio's (which requires a documented, compliant cybersecurity program as a predicate to the affirmative defense) and has drawn both praise and criticism. From a business defense perspective, it simplifies the protection — there is no compliance program to audit or certify. From a policy perspective, critics note it provides no incentive for companies to invest in cybersecurity practices. The [Troutman Pepper Locke analysis](https://www.troutman.com/insights/cybersecurity-safe-harbors-one-step-forward-and-two-steps-back/) describes this as "one step forward and two steps back" for the broader safe harbor model.

### Relationship to Tennessee Information Protection Act

Tennessee separately enacted the [Tennessee Information Protection Act (TIPA)](https://www.mintz.com/insights-center/viewpoints/2826/2023-05-11-mintz-may-madness-tennessees-information-protection-act-gets-us-thinking-about-nist-y-safe-harbors) (effective July 1, 2025), which contains its own separate affirmative defense for companies maintaining a written privacy program conforming to the NIST Privacy Framework. Note that while TIPA became fully effective July 1, 2025, data protection assessment requirements under TIPA apply to processing activities created on or after July 1, 2024 — an earlier applicability trigger for that specific obligation. TIPA's affirmative defense applies only to claims brought under TIPA itself — not to general tort claims. HB 2434's class action shield operates independently and more broadly, applying to all class action claims arising from cybersecurity events regardless of the underlying legal theory.

### Immediate Effective Date and Retroactive Application

The law took effect immediately upon Governor Lee's signature on May 21, 2024. This immediate effective date was significant: as [Ritter Gallagher notes](https://www.rittergallagher.com/insights/1xjuyl4bgbwzk21oi4vq1dl6bd9myg) and reporting from [WKRN](https://www.wkrn.com/news/tennessee-news/new-tn-law-to-protect-entities-under-cyber-attack-from-class-action-suits/) confirms, the safe harbor could apply directly to then-pending class actions related to the Ascension and Change Healthcare incidents, depending on the dates of filing and applicable choice-of-law analysis. Whether the law applies retroactively to class actions filed before the signing date is a question courts will need to resolve.

## Impact Assessment [MEDIUM confidence]

### Affected Entities

The law applies to all "private entities" operating in Tennessee, covering:

- **Healthcare organizations:** Hospitals, health systems, insurers, medical practices — the primary sector motivating the legislation
- **Financial services:** Banks, insurers, fintech companies
- **Retailers and hospitality:** Any business collecting consumer data
- **Technology companies:** SaaS providers, data processors, managed service providers
- **Non-profits:** Including religious organizations and charities that handle member or donor data

The broad definition of "private entity" ensures virtually every private-sector organization that stores electronic data is eligible for the protection, regardless of size or industry.

### Plaintiffs' Bar Impact

The law substantially narrows viable class action theories for data breach victims in Tennessee. The [Robinson+Cole analysis on JDSupra](https://www.jdsupra.com/legalnews/tennessee-passes-law-restricting-data-1695886/) and the [DataBreaches.Net assessment](https://databreaches.net/2024/06/26/impact-of-tennessees-cybersecurity-class-action-safe-harbor/) note that this raises the question of whether other states may follow Tennessee's model. For plaintiffs' attorneys, the path to class certification in Tennessee state court now requires substantially more factual investigation into a defendant's specific subjective awareness of security gaps — a pre-filing inquiry that raises costs and reduces the economic viability of bringing smaller class actions.

Individual tort claims remain governed by ordinary negligence and are not directly affected by the statute; the impact is confined to class proceedings.

### Consumer Advocates' Criticism

Consumer advocates and plaintiff-side attorneys have argued that the heightened standard is practically insurmountable in most breach cases, effectively insulating negligent companies from meaningful accountability. [DataBreaches.Net](https://databreaches.net/2024/06/26/impact-of-tennessees-cybersecurity-class-action-safe-harbor/) details the criticism that the previous reasonable care standard was already an appropriate and calibrated check on corporate behavior. Critics also highlight that Tennessee's approach diverges from federal cybersecurity policy guidance from the Cybersecurity and Infrastructure Security Agency (CISA), which urges companies to strengthen baseline security practices — a goal the law arguably undermines by removing litigation incentive.

### Enforcement Outlook and Judicial Application

Because the law is structured as a class action immunity (rather than an affirmative defense to be raised and proven by defendant), courts may interpret it as a threshold barrier to class certification itself. The [Quinn Emanuel analysis](https://www.quinnemanuel.com/the-firm/publications/new-state-level-safe-harbor-statutes-attempt-to-curb-data-breach-litigation-risks/) discusses how courts in states with similar (though less protective) safe harbor statutes have generally construed such provisions strictly. Future Tennessee appellate decisions will be critical in defining what evidence suffices to demonstrate "gross negligence" or "willful and wanton misconduct" in the cybersecurity context.

### National Replication Risk

The [Winston & Strawn analysis](https://www.winston.com/en/blogs-and-podcasts/class-action-insider/tennessee-law-restricts-data-breach-class-action-suits-will-other-states-follow) raises the question of whether other states will follow Tennessee's model. If other states adopt comparable class action bars — without requiring affirmative cybersecurity programs — the aggregate effect on data breach litigation nationally could be significant.

## Action Items

- Businesses with Tennessee operations should document that they are aware of HB 2434's protection and brief litigation counsel on the new gross negligence standard applicable to any data breach class actions filed in Tennessee state court.
- Organizations facing existing Tennessee data breach class actions should consult counsel immediately regarding whether HB 2434 applies to pending cases and how to raise the new standard in motions practice.
- Companies should not assume the law eliminates data breach liability exposure: individual (non-class) tort claims remain governed by ordinary negligence; HIPAA, FTC Act, and state notification obligations are unaffected; and federal class actions may not be subject to Tennessee's bar.
- Compliance teams should continue investing in recognized cybersecurity frameworks (NIST CSF, ISO 27001) not because HB 2434 requires them, but because regulatory scrutiny from the FTC, HHS OCR, and SEC continues to intensify at the federal level, and because the law's protection is contingent on the absence of gross negligence — a standard more easily met by organizations with documented security programs.
- Monitor whether other states introduce comparable legislation, particularly in the wake of major ransomware incidents affecting healthcare.
- Track Tennessee appellate decisions interpreting "gross negligence" and "willful and wanton misconduct" in the cybersecurity context as the first wave of cases under HB 2434 proceeds.

## Related Reports

- [Utah SB 98 (2024): Expanded Data Breach Notification Requirements](reports/cybersecurity/incident-reporting/utah-sb98-data-breach-notification-amendment-2024-05-14.md) -- Utah's 2024 data breach legislation addresses notification obligations in the same legislative cycle, offering a useful contrast with Tennessee's liability-side approach.
- [California's CCPA Cybersecurity Audit Rule: Class-Action Litigation and Discovery Risks](reports/cybersecurity/enforcement-actions/california-ccpa-cybersecurity-audit-class-litigation-2026-04-14.md) -- California moves in the opposite direction, creating class action exposure tied to cybersecurity audit failures, underscoring the divergent state-law landscape.
- [Federal CIRCIA Final Rule Delay](reports/cybersecurity/incident-reporting/federal-circia-final-rule-delay-2026-04-07.md) -- Federal cyber incident reporting obligations remain unaffected by Tennessee's class action bar and continue to evolve; organizations must track both tracks.

## Sources

1. [Tennessee HB 2434 Official Bill Text (capitol.tn.gov)](https://www.capitol.tn.gov/Bills/113/Bill/HB2434.pdf) -- Official enrolled bill text; titled "AN ACT to amend Tennessee Code Annotated, Title 29 and Title 47, relative to civil liability" (Tennessee General Assembly)
2. [Public Chapter 991 (Tennessee Secretary of State)](https://publications.tnsosfiles.com/acts/113/pub/pc0991.pdf) -- Official enacted law as signed by Governor Lee on May 21, 2024
3. [Tennessee General Assembly HB 2434 Bill Information Page](https://wapp.capitol.tn.gov/apps/Billinfo/default.aspx?BillNumber=HB2434&ga=113) -- Official legislative status, vote tallies, and companion bill information
4. [LegiScan: Tennessee HB 2434 (113th General Assembly)](https://legiscan.com/TN/bill/HB2434/2023) -- Legislative tracking with vote history and chaptered bill text
5. [Thompson Hine LLP: Tennessee Enacts Data Breach Class Action Safe Harbor](https://www.thompsonhine.com/insights/tennessee-enacts-data-breach-class-action-safe-harbor/) -- Primary law firm analysis; source for the original Lexology finding
6. [Lexology: Tennessee Enacts Data Breach Class Action Safe Harbor (Thompson Hine)](https://www.lexology.com/library/detail.aspx?g=f8980278-3f3d-4547-90ad-2145b146516b) -- Lexology repost of Thompson Hine client alert
7. [Holland & Knight: New Tennessee Law Creates Heightened Liability Requirement](https://www.hklaw.com/en/insights/publications/2024/06/new-tennessee-law-creates-heightened-liability-requirement) -- Detailed analysis of the gross negligence standard and its legal significance
8. [Pierson Ferdinand LLP: It Takes More Than Negligence To File A Class Action After A Cybersecurity Event In Tennessee](https://pierferd.com/insights/it-takes-more-than-negligence-to-file-a-class-action-after-a-cybersecurity-event-in-tennessee) -- Practical analysis with example of gross negligence burden in MFA context
9. [Ritter Gallagher: Tennessee Enacts Cybersecurity Safe Harbor Against Class Action Lawsuits](https://www.rittergallagher.com/insights/1xjuyl4bgbwzk21oi4vq1dl6bd9myg) -- Analysis covering immediate effective date and Ascension/Change Healthcare implications
10. [Robinson+Cole Data Privacy + Security Insider (JDSupra): Tennessee Passes Law Restricting Data Breach Class Action Suits](https://www.jdsupra.com/legalnews/tennessee-passes-law-restricting-data-1695886/) -- Analysis of impact on plaintiffs' bar and national replication risk
11. [DataBreaches.Net: Impact of Tennessee's Cybersecurity Class Action Safe Harbor](https://databreaches.net/2024/06/26/impact-of-tennessees-cybersecurity-class-action-safe-harbor/) -- Consumer-side analysis with criticism of the heightened standard
12. [Troutman Pepper Locke: Cybersecurity Safe Harbors — One Step Forward and Two Steps Back](https://www.troutman.com/insights/cybersecurity-safe-harbors-one-step-forward-and-two-steps-back/) -- Comparative analysis of state safe harbor models; Ohio, Utah, Connecticut, and Tennessee
13. [Quinn Emanuel: New State-Level Safe Harbor Statutes Attempt to Curb Data Breach Litigation Risks](https://www.quinnemanuel.com/the-firm/publications/new-state-level-safe-harbor-statutes-attempt-to-curb-data-breach-litigation-risks/) -- Detailed national survey of safe harbor approaches and judicial interpretation
14. [Winston & Strawn: Tennessee Law Restricts Data Breach Class Action Suits; Will Other States Follow?](https://www.winston.com/en/blogs-and-podcasts/class-action-insider/tennessee-law-restricts-data-breach-class-action-suits-will-other-states-follow) -- Analysis of interstate policy implications
15. [Ohio Revised Code § 1354.02 (Ohio Laws)](https://codes.ohio.gov/ohio-revised-code/section-1354.02) -- Official text of Ohio's cybersecurity safe harbor for comparison
16. [WKRN: New State Law to Protect Entities Under Cyber Attack from Class Action Suits](https://www.wkrn.com/news/tennessee-news/new-tn-law-to-protect-entities-under-cyber-attack-from-class-action-suits/) -- Nashville news coverage of the law's context amid Ascension health hack
17. [Mintz: Tennessee's Information Protection Act Gets Us Thinking About NIST-y Safe Harbors](https://www.mintz.com/insights-center/viewpoints/2826/2023-05-11-mintz-may-madness-tennessees-information-protection-act-gets-us-thinking-about-nist-y-safe-harbors) -- Analysis of TIPA's separate privacy framework affirmative defense and its relationship to HB 2434
18. [Vensure: Reminder — The Tennessee Information Protection Act (TIPA), Effective July 1, 2025](https://vensure.com/employment-law-updates/tennessee/reminder-the-tennessee-information-protection-act-tipa-effective-july-1-2025/) -- Confirms TIPA's full effective date as July 1, 2025 and the earlier July 1, 2024 data protection assessment applicability trigger
19. [Tennessee Attorney General Press Release (April 30, 2025): TIPA Tips and Guidelines](https://www.tn.gov/attorneygeneral/news/2025/4/30/pr25-25.html) -- Official AG office confirmation of TIPA's effective date and compliance guidance
