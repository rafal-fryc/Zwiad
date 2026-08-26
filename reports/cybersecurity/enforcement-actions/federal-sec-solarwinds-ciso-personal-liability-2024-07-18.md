---
title: "SEC v. SolarWinds: CISO Personal Liability — What Survived, What Was Dismissed, and What It Means for Security Officers"
date: 2024-07-26
jurisdiction: "Federal"
category: "cybersecurity"
development_type: "enforcement"
finding_id: "SCAN-20240726-032"
topic_key: "SEC-SOLARWINDS-AND-ITS-CISO-2024"
topic_type: "enforcement_action"
first_reported: 2024-07-26
last_updated: 2026-04-15
status_history: []
cluster: "SEC v. SolarWinds: Cybersecurity Disclosure Enforcement Limits"
cluster_slug: "sec-solarwinds-cybersecurity-enforcement"
---

# SEC v. SolarWinds: CISO Personal Liability — What Survived, What Was Dismissed, and What It Means for Security Officers

**Jurisdiction:** Federal (S.D.N.Y.) | **Category:** Cybersecurity / Securities Enforcement | **Date:** July 18, 2024

## Executive Summary [HIGH confidence]

On July 18, 2024, U.S. District Judge Paul A. Engelmayer of the Southern District of New York dismissed the bulk of the SEC's landmark complaint in *SEC v. SolarWinds Corp. and Timothy G. Brown* (Case No. 1:23-cv-09518-PAE), but allowed fraud claims tied to a corporate website "Security Statement" to proceed against both the company and its CISO individually. This was the first time the SEC had charged an individual Chief Information Security Officer with securities fraud. The [107-page opinion](https://www.nysd.uscourts.gov/sites/default/files/2024-07/SolarWinds%20Opinion%20(Dkt.%20125).pdf) rejected the SEC's attempt to hold Brown personally liable for statements in formal SEC filings, for conduct disclosed under a voluntary NIST Cybersecurity Framework scoring methodology, and for post-incident disclosures made during an unfolding investigation. What survived — and ultimately drove the case until the SEC's November 2025 voluntary dismissal — were narrow but meaningful fraud claims resting on Brown's documented personal knowledge that the public-facing Security Statement contradicted internal cybersecurity assessments he had seen and managed. The ruling's lasting significance for security practitioners is the specific liability pathway it confirmed: a CISO who knows of a gap between a public security representation and internal reality, and who personally disseminates or approves the public statement anyway, is exposed to individual securities fraud liability.

## Background [HIGH confidence]

### The SUNBURST Attack and SEC's Enforcement Theory

In October 2019, threat actors later attributed to Russia's SVR inserted malicious code ("SUNBURST") into SolarWinds' Orion software update pipeline. The malware reached approximately 18,000 organizations, including multiple U.S. federal agencies, before SolarWinds disclosed the breach on December 14, 2020. The resulting stock decline of approximately 25–35 percent drew SEC attention.

On October 30, 2023, the [SEC filed suit](https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26423) against SolarWinds and Timothy G. Brown, then serving as Vice President of Cyber Security and Architecture and the company's de facto CISO. Brown's individual role made the action unprecedented: it was the first SEC enforcement action to charge a CISO personally with securities fraud in connection with a company's cybersecurity disclosures. The SEC sought permanent injunctive relief, civil penalties, disgorgement, and — critically for Brown personally — an officer-and-director bar that would have prohibited him from serving as an officer or director of any public company.

### The Six Claims Against Brown

The original [SEC complaint](https://www.sec.gov/files/litigation/complaints/2023/comp-pr2023-227.pdf) (and its February 2024 amended version) charged Brown personally with conduct spanning six liability theories:

1. Fraud based on SolarWinds' pre-breach website "Security Statement" (access controls and password policy misrepresentations)
2. Fraud based on risk factor disclosures in annual and quarterly SEC filings
3. Fraud based on post-SUNBURST Form 8-K and related disclosures
4. Fraud based on marketing communications (press releases, blog posts, podcasts)
5. Aiding and abetting SolarWinds' failure to maintain internal accounting controls under Section 13(b)(2)(B) of the Exchange Act
6. Aiding and abetting SolarWinds' failure to maintain disclosure controls under Rule 13a-15(a)

The SEC further alleged "scheme liability" under Rule 10b-5(a) and (c) — that Brown had participated in a scheme to defraud investors through his personal role in creating, approving, and disseminating the Security Statement.

### Brown's Role and Internal Documentation

Central to the surviving claims was evidence of Brown's day-to-day role. The complaint alleged that Brown managed the Security Statement directly, approved it, and disseminated it to employees and partners. It also alleged that he was personally presented with — and participated in creating — internal assessments showing that SolarWinds scored poorly on specific NIST Cybersecurity Framework categories directly corresponding to the Security Statement's representations, and that internal SOX audits documented longstanding failures on password policy compliance that were reported to management. As [Greenberg Traurig analyzed](https://www.gtlaw.com/en/insights/2024/7/sec-v-solarwinds-update-us-federal-district-court-dismisses-most-of-the-secs-case-but-some-fraud-claims-and-ciso-liability-remain), these internal presentations, communications, and cybersecurity assessments formed the evidentiary backbone of the claims that ultimately survived.

## Detailed Analysis [HIGH confidence]

### What Was Dismissed Against Brown Personally

**Risk Factor Filings (Annual and Quarterly Reports)**

The court dismissed all claims that Brown aided and abetted fraud in SolarWinds' risk factor disclosures in Exchange Act filings (Forms 10-K and 10-Q). The SEC had argued that the risk factors describing cybersecurity threats as hypothetical future risks were misleading because the company already faced known vulnerabilities. Judge Engelmayer found these arguments unpersuasive: risk factor language is inherently general and forward-looking, and the SEC's theory improperly held the company to disclosing specific operational weaknesses in the risk factor section — a use of that disclosure vehicle not supported by precedent.

**Post-SUNBURST Form 8-K and Subsequent Disclosures**

The court dismissed all claims arising from SolarWinds' December 14, 2020, Form 8-K and subsequent post-incident disclosures. The SEC had alleged these were misleading because they did not disclose all known indicators of the attack's scope. The court held that the SEC's theory "impermissibly relies on hindsight and speculation" — SolarWinds was disclosing an unfolding, novel nation-state attack in real time, and faulting the company for not knowing at disclosure what only post-facto forensic investigation revealed. This protection extends to Brown personally.

**Marketing Communications as Puffery**

All claims tied to press releases, blog posts, and podcast appearances by SolarWinds and Brown were dismissed as non-actionable "corporate puffery" — general, aspirational statements that a reasonable investor would not rely on as specific factual representations. The court drew a clear line between promotional marketing content and the kind of specific, investor-facing representations that can ground securities fraud.

**NIST Framework Voluntary Scoring**

The SEC argued that it was materially misleading to claim adherence to the NIST Cybersecurity Framework without disclosing poor scores on specific framework components. The court was skeptical, observing this was "not [the SEC's] strongest" argument. Voluntary self-assessment scores under a flexible risk management framework are not representations of compliance; they are internal management tools. Holding companies and their security officers liable for not publicly disclosing the granular outputs of voluntary internal risk assessments would create perverse incentives against conducting and documenting such assessments.

**Internal Accounting Controls (Section 13(b)(2)(B))**

The court fully rejected the SEC's theory that Exchange Act Section 13(b)(2)(B) — requiring "internal accounting controls" — extends to cybersecurity systems. The court conducted a textual and historical analysis concluding the provision is limited to financial accounting integrity. Brown could not be liable for aiding and abetting a violation that the statute does not cover.

**Disclosure Controls (Rule 13a-15(a))**

The court dismissed claims that Brown aided and abetted inadequate disclosure controls. The court held that establishing a disclosure controls violation requires pleading "systemic deficiencies" in the overall disclosure framework, not isolated mishandling of specific incidents. Two misclassified cybersecurity incidents did not make out a claim that the company lacked a functioning disclosure controls system.

### What Survived Against Brown Personally

**Security Statement Fraud: Section 10(b) and Rule 10b-5(b)**

The sole surviving misrepresentation claim centered on SolarWinds' corporate website "Security Statement" — a document Brown managed, approved, and promoted. The court found the SEC had adequately pled that two specific representations in the Security Statement were materially false:

- **Access controls**: The Security Statement stated SolarWinds maintained role-based, least-privilege access controls. Internal evidence showed "largely indiscriminate provision of administrative access to employees" — a state the court found "blatantly contradicts" the public claim.
- **Password protection policies**: The Security Statement described robust password standards, but internal SOX audits documented that these standards were not enforced in practice.

The court held the Security Statement was investor-facing because it was publicly accessible on the corporate website, and because cybersecurity practices were material to SolarWinds' business as an IT infrastructure software vendor. On Brown personally, the court found the SEC had "easily ple[d]" scienter: Brown had been the direct manager and approver of the Security Statement, had received and presented internal assessments documenting poor NIST scores and access control deficiencies, and had seen the SOX audit findings showing password non-compliance. His personal knowledge of the internal-versus-public gap, combined with his role in approving and disseminating the statement, established the scienter element for individual liability.

As [Skadden noted](https://www.skadden.com/insights/publications/2024/08/takeaways-from-the-dismissal-of-sec-claims), the court imputed Brown's scienter to SolarWinds as well — his knowledge as the senior security official responsible for the Security Statement was attributed to the company.

**Scheme Liability: Rule 10b-5(a) and (c)**

The court also allowed the scheme liability theory to survive as to Brown. Because Brown had personally disseminated and promoted the Security Statement — not merely helped craft it — he was alleged to have participated in a "scheme" to defraud investors within the meaning of Rule 10b-5(a) and (c). [Freshfields' analysis](https://blog.freshfields.us/post/102jeyk/court-quashes-substantial-number-of-secs-novel-liability-theories-in-sec-v-sola) noted that scheme liability surviving alongside misrepresentation liability is significant: it provides the SEC a second doctrinal basis for individual liability whenever a CISO takes affirmative steps to disseminate a false security representation.

### The Final Chapter: November 2025 Voluntary Dismissal

After the July 2024 partial dismissal, the surviving Security Statement claims proceeded to discovery. On November 20, 2025, the [SEC jointly stipulated to dismiss its remaining claims](https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26423) against both SolarWinds and Brown with prejudice, without any penalty, consent order, or remediation requirement. Brown remained in his CISO role throughout the litigation.

The SEC offered no public legal rationale, citing only "exercise of discretion." As [Parker Poe analyzed](https://www.parkerpoe.com/news/2025/12/key-takeaways-for-companies-after-sec-voluntarily-dismisses), multiple factors likely contributed: the Trump-era SEC's recalibrated enforcement philosophy pivoting toward outright fraudulent disclosure rather than disclosure-deficiency cases; the age and complexity of the underlying conduct; and the difficulty of proving the narrow surviving theory at trial in a sympathetic fact pattern (a nation-state attack that victimized thousands of organizations).

The final dismissal provides procedural relief, but as [Perkins Coie emphasized](https://perkinscoie.com/insights/update/sec-dismisses-cyber-disclosure-case-against-solarwinds-and-ciso), it does not alter the legal framework established by the July 2024 opinion: the liability theory that survived to discovery — specific false public statement, CISO personal knowledge of its falsity, CISO approval and dissemination — remains good law.

## Impact Assessment [HIGH confidence]

### The CISO Personal Liability Framework After SolarWinds

The SolarWinds litigation created a legally tested template for individual CISO liability under federal securities law. The ruling confirms that CISOs of public companies can face personal fraud liability when all of the following are present:

1. A specific, publicly accessible document describes the company's cybersecurity practices in concrete terms (not puffery).
2. The CISO has personal knowledge — documented in internal assessments, audits, or communications — that the document's representations are inaccurate or misleading.
3. The CISO personally approves, disseminates, or otherwise adopts responsibility for the document.

What the ruling equally confirms as insufficient to establish personal CISO liability:
- Generic cybersecurity risk factors in SEC filings (dismissed)
- Voluntary NIST or similar framework self-assessments (dismissed)
- Post-incident disclosures made in real time without full information (dismissed)
- Marketing and promotional communications (dismissed as puffery)
- Inadequate cybersecurity program design or implementation, standing alone (dismissed — Section 13(b)(2)(B) does not extend to cybersecurity)

### The Deterrence-Communication Tension

The case exposed a structural tension for security executives. CISOs are expected to document cybersecurity weaknesses in internal assessments, gap analyses, and audit findings — good security governance requires candid internal communication. But the SolarWinds ruling demonstrated that those same internal documents become evidence of scienter in a securities fraud case if there is a gap between what they say and what the company represents publicly. As [Perkins Coie noted](https://perkinscoie.com/insights/update/sec-dismisses-cyber-disclosure-case-against-solarwinds-and-ciso), the final dismissal may ease some concern that internal candor creates personal legal risk, but the liability framework itself remains in place.

### D&O Insurance and Indemnification

The SolarWinds case triggered industry-wide reassessment of whether CISO positions are adequately covered by directors and officers insurance. [Hunton Williams analyzed](https://www.hunton.com/privacy-and-information-security-law/judge-dismisses-most-of-sec-case-against-solarwinds-and-its-ciso) that most public company D&O policies cover "insured persons" for securities claims regardless of whether the CISO holds a formal Section 16 officer title — the relevant question is whether the SEC action constitutes a "securities claim" under the policy definition, which the SolarWinds-type fact pattern typically would. However, the answer depends on specific policy language, exclusions for intentional misconduct, and whether the CISO's defense costs deplete limits available to the board and C-suite. Companies should confirm explicitly that their CISO is an "insured person" under the D&O policy and review applicable exclusions.

A separate concern: even where insurance covers defense costs, personal indemnification agreements may not fully protect a CISO if the company itself is simultaneously defending and faces financial pressure. CISOs should negotiate individual indemnification agreements separate from reliance on the corporate D&O program.

### Board Oversight Implications

The ruling confirms that board-level cybersecurity governance is not merely a best practice — it is a legal risk management imperative. If the board receives internal assessments showing a gap between public cybersecurity representations and operational reality, and does not direct correction of the public statement, individual directors could face exposure under the same legal theory. [Skadden's pre-ruling analysis](https://www.skadden.com/insights/publications/2023/11/what-does-the-secs-complaint-against-solarwinds-mean) flagged that the SEC's charge against Brown rested on his role as the individual "primarily responsible for creating and approving" the Security Statement — a role boards should ensure is assigned with appropriate legal oversight, not delegated entirely to the security team without legal or compliance review.

### Industry Impact: CISO Recruitment and Retention

A [BlackFog survey](https://www.csoonline.com/article/4109992/what-cisos-should-know-about-the-solarwinds-lawsuit-dismissal.html) found that 70 percent of CISOs reported that the threat of personal liability negatively affected their perception of the CISO role, with potential chilling effects on recruitment and retention of experienced security executives. The November 2025 dismissal tempered some of that concern, but the legal framework remains available for future enforcement action under different administrations.

## Action Items

- **Audit all public-facing cybersecurity representations with legal review.** Every document accessible to investors that describes the company's cybersecurity practices — corporate website security pages, trust portals, partner-facing security statements, product documentation with security claims — should be reviewed by legal counsel against current internal assessments and audit findings. Any gap between public representation and internal reality should be corrected before it is documented in internal communications.

- **Establish a formal "Security Statement" lifecycle process.** Public-facing security representations should be treated as investor disclosures subject to the same review, approval, and update disciplines applied to formal SEC filings. Assign clear responsibility for who owns each statement, schedule periodic accuracy reviews tied to internal assessment cycles, and document the review and sign-off process.

- **Never use voluntary framework scores as the basis for public compliance claims.** NIST CSF, ISO 27001, and similar frameworks are risk management tools, not compliance certifications. Public representations that the company "follows NIST" or achieves a specific maturity level in a specific domain are representations that can be tested against internal assessment data. Either avoid such representations or ensure they are strictly accurate and hedged appropriately.

- **Segregate internal assessment records from marketing and external communications review.** Internal NIST assessments, gap analyses, SOX audit findings, and similar documents should remain in a controlled legal review channel. They should not be cross-referenced in external communications without express legal sign-off confirming that the public statement accurately reflects (and does not materially overstate) the internal findings.

- **Confirm CISO D&O coverage explicitly.** Boards and general counsel should confirm that the CISO is named as an "insured person" under the company's D&O policy, review the policy's definition of "securities claims" to confirm it covers SEC enforcement actions, and check whether any exclusions (intentional misconduct, conduct not in officer capacity) could create coverage gaps. Supplement with a standalone CISO indemnification agreement if coverage is uncertain.

- **Document the board's cybersecurity oversight role.** Board materials, meeting minutes, and oversight committee charters should reflect that the board is receiving and reviewing material cybersecurity risk information, directing management to address identified gaps, and overseeing the accuracy of public cybersecurity representations. This documentation supports a defense against claims that board oversight was inadequate and demonstrates governance that may be relevant under [17 CFR § 229.106 (Item 106)](https://www.ecfr.gov/current/title-17/chapter-II/part-229/subpart-229.100/section-229.106) annual disclosure obligations.

- **Train CISOs on when internal findings trigger disclosure obligations.** Security executives should understand — with legal counsel's guidance — when an internal assessment finding is material enough to require public disclosure or correction of an existing public statement. This includes understanding the nexus between internal audit findings, board reporting obligations, and investor-facing representations.

- **Monitor the SEC's cybersecurity enforcement posture under current leadership.** The Trump-era SEC has signaled a shift toward "back to basics" fraudulent disclosure enforcement rather than novel disclosure-deficiency theories. This does not eliminate the risk framework; a future administration may reinvigorate it. Companies should track enforcement posture and build durable processes, not point-in-time compliance designed around the current enforcement climate.

## Related Reports

- [reports/cybersecurity/enforcement-actions/federal-sec-cyber-enforcement-authority-solarwinds-2024-07-26.md](reports/cybersecurity/enforcement-actions/federal-sec-cyber-enforcement-authority-solarwinds-2024-07-26.md) — Companion report covering the same SDNY ruling from the perspective of SEC enforcement authority limits; covers the internal accounting controls and disclosure controls dismissed claims in depth from a compliance team perspective.
- [reports/cybersecurity/enforcement-actions/federal-sec-coinbase-sdny-ruling-2024-03-27.md](reports/cybersecurity/enforcement-actions/federal-sec-coinbase-sdny-ruling-2024-03-27.md) — Related SDNY ruling addressing limits of SEC enforcement authority against a technology company in a different regulatory context.
- [reports/cybersecurity/incident-reporting/federal-circia-final-rule-delay-2026-04-07.md](reports/cybersecurity/incident-reporting/federal-circia-final-rule-delay-2026-04-07.md) — Federal cybersecurity incident reporting rule, relevant regulatory backdrop for the environment in which CISOs now operate.

## Sources

1. [SDNY Opinion: SEC v. SolarWinds Corp. and Timothy G. Brown (Dkt. 125, July 18, 2024)](https://www.nysd.uscourts.gov/sites/default/files/2024-07/SolarWinds%20Opinion%20(Dkt.%20125).pdf) — Official 107-page court opinion; primary authority for all holdings discussed in this report.
2. [SEC Enforcement Page: SolarWinds Corp. and Timothy G. Brown (LR-26423)](https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26423) — Official SEC enforcement docket including original complaint, amended complaint, and November 2025 joint stipulation to dismiss.
3. [SEC Original Complaint: SolarWinds Corporation and Timothy G. Brown (Oct. 30, 2023)](https://www.sec.gov/files/litigation/complaints/2023/comp-pr2023-227.pdf) — Official complaint text; source for the six liability theories charged against Brown and the remedies sought.
4. [Davis Wright Tremaine: District Court Dismisses Majority of SEC Complaint Against SolarWinds and Its CISO (July 2024)](https://www.dwt.com/blogs/privacy--security-law-blog/2024/07/sec-solarwinds-case-mostly-dismissed-by-sdny-court) — Primary source law firm analysis (finding source); focused on implications for CISOs and public companies.
5. [Davis Wright Tremaine: SEC's Charges Against SolarWinds and Its CISO Highlight Emerging Risks (Nov. 2023)](https://www.dwt.com/blogs/privacy--security-law-blog/2023/11/sec-solarwinds-ciso-fraud-charges) — DWT pre-ruling analysis of what the charges meant for security professionals when first filed.
6. [Greenberg Traurig: SEC v. SolarWinds Update — CISO Liability Remains (July 2024)](https://www.gtlaw.com/en/insights/2024/7/sec-v-solarwinds-update-us-federal-district-court-dismisses-most-of-the-secs-case-but-some-fraud-claims-and-ciso-liability-remain) — Detailed analysis of surviving CISO liability claims and the internal documentation evidence.
7. [Skadden: Takeaways From the Dismissal of SEC Claims Against SolarWinds and Its CISO (Aug. 2024)](https://www.skadden.com/insights/publications/2024/08/takeaways-from-the-dismissal-of-sec-claims) — Leading securities litigation firm analysis; CISO liability framework and imputed scienter analysis.
8. [Skadden: What Does the SEC's Complaint Against SolarWinds Mean for CISOs and Boards? (Nov. 2023)](https://www.skadden.com/insights/publications/2023/11/what-does-the-secs-complaint-against-solarwinds-mean) — Pre-ruling analysis of board and CISO governance implications.
9. [Freshfields: Court Quashes Substantial Number of SEC's Novel Liability Theories in SEC v. SolarWinds](https://blog.freshfields.us/post/102jeyk/court-quashes-substantial-number-of-secs-novel-liability-theories-in-sec-v-sola) — Analysis of the scheme liability surviving claim and Rule 10b-5(a)/(c) implications.
10. [Perkins Coie: SEC Dismisses Cyber Disclosure Case Against SolarWinds and CISO (2025)](https://perkinscoie.com/insights/update/sec-dismisses-cyber-disclosure-case-against-solarwinds-and-ciso) — Analysis of the November 2025 final dismissal and what persists for CISO liability.
11. [Parker Poe: Key Takeaways for Companies After SEC Voluntarily Dismisses Landmark SolarWinds Enforcement Action (Dec. 2025)](https://www.parkerpoe.com/news/2025/12/key-takeaways-for-companies-after-sec-voluntarily-dismisses) — Post-dismissal analysis of enforcement posture shift and compliance implications.
12. [Harvard Law Corporate Governance Blog: SEC Dismisses SolarWinds Lawsuit — What CISOs Need to Know (Dec. 2025)](https://corpgov.law.harvard.edu/2025/12/10/sec-dismisses-solarwinds-lawsuit-what-cisos-need-to-know/) — Academic and practitioner analysis specifically for the CISO audience on what the final dismissal means.
13. [Harvard Law Corporate Governance Blog: SolarWinds Dismissed — What the SEC's U-turn Signals for Cyber Enforcement (Dec. 2025)](https://corpgov.law.harvard.edu/2025/12/07/solarwinds-dismissed-what-the-secs-u-turn-signals-for-cyber-enforcement/) — Broader enforcement signal analysis following final dismissal.
14. [Hunton Williams: Judge Dismisses Most of SEC Case Against SolarWinds and Its CISO](https://www.hunton.com/privacy-and-information-security-law/judge-dismisses-most-of-sec-case-against-solarwinds-and-its-ciso) — D&O insurance coverage analysis for CISOs post-ruling.
15. [CSO Online: What CISOs Should Know About the SolarWinds Lawsuit Dismissal](https://www.csoonline.com/article/4109992/what-cisos-should-know-about-the-solarwinds-lawsuit-dismissal.html) — Practitioner-oriented analysis including BlackFog survey data on CISO liability concerns.
16. [eCFR: 17 CFR § 229.106 — Cybersecurity (Item 106)](https://www.ecfr.gov/current/title-17/chapter-II/part-229/subpart-229.100/section-229.106) — Official text of the SEC's 2023 cybersecurity disclosure rule governing annual governance and risk management disclosures.
17. [Akin Gump: Cybersecurity After SolarWinds — Practical Guidance for CISOs Under the New Rules](https://www.akingump.com/en/insights/alerts/cybersecurity-after-solarwinds-practical-guidance-for-cisos-under-the-new-rules) — Forward-looking practical guidance for CISOs navigating the post-SolarWinds regulatory environment.
