---
title: "Court Limits SEC Cybersecurity Enforcement Authority: SolarWinds SDNY Ruling July 2024"
date: 2024-07-26
jurisdiction: "Federal"
category: "cybersecurity"
development_type: "enforcement"
finding_id: "SCAN-20240726-016"
topic_key: "SEC-AUTHORITY-2024"
topic_type: "enforcement_action"
first_reported: 2024-07-26
last_updated: 2024-07-26
status_history: []
cluster: "SEC v. SolarWinds: Cybersecurity Disclosure Enforcement Limits"
cluster_slug: "sec-solarwinds-cybersecurity-enforcement"
---

# Court Limits SEC Cybersecurity Enforcement Authority: SolarWinds SDNY Ruling July 2024

**Jurisdiction:** Federal (S.D.N.Y.) | **Category:** Cybersecurity / Securities Enforcement | **Date:** July 18, 2024

## Executive Summary [HIGH confidence]

On July 18, 2024, U.S. District Judge Paul A. Engelmayer of the Southern District of New York issued a 107-page opinion in *SEC v. SolarWinds Corp. and Timothy G. Brown* (Case No. 1:23-cv-09518-PAE) that dramatically curtailed the SEC's cybersecurity enforcement authority. The [court dismissed the bulk of the SEC's claims](https://www.nysd.uscourts.gov/sites/default/files/2024-07/SolarWinds%20Opinion%20(Dkt.%20125).pdf), including the agency's novel attempt to apply the Exchange Act's "internal accounting controls" provision to cybersecurity systems, its post-incident disclosure claims (which the court found impermissibly relied on hindsight), and its securities fraud claims based on marketing communications characterized as non-actionable corporate puffery. Only claims tied to SolarWinds' corporate website "Security Statement" survived. The ruling established significant constraints on the SEC's use of pre-existing enforcement tools against cybersecurity disclosures and set a high bar for cybersecurity-based securities fraud actions. The case ultimately ended in complete defeat for the SEC when, on November 20, 2025, the agency voluntarily dismissed its remaining claims with prejudice, without any penalty or consent order.

## Background [HIGH confidence]

### The SUNBURST Supply-Chain Attack

SolarWinds Corporation, an Austin, Texas-based provider of IT infrastructure management software, became the target of one of the most consequential cyberattacks in U.S. history. Beginning as early as October 2019, threat actors — later attributed to the Russian Foreign Intelligence Service (SVR) — inserted malicious code known as "SUNBURST" into SolarWinds' Orion software update mechanism. When customers applied updates, the malware was distributed to approximately 18,000 organizations, including multiple U.S. federal agencies such as the Treasury, Commerce, and Homeland Security departments.

SolarWinds publicly disclosed the breach on December 14, 2020, in a Form 8-K filing. Its stock price dropped approximately 25 percent over the following two days and approximately 35 percent by month's end. The scale of the breach drew congressional scrutiny, intelligence community reviews, and ultimately the attention of the SEC.

### The SEC's Enforcement Theory

On October 30, 2023, the [SEC filed a landmark complaint](https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26423) against SolarWinds and its Chief Information Security Officer, Timothy G. Brown, in the Southern District of New York. The action was notable for several firsts: it was the SEC's first-ever litigated enforcement action against a public company specifically for its cybersecurity disclosures, and the first time the agency had brought individual securities fraud charges against a CISO.

The complaint advanced an expansive enforcement theory targeting six categories of alleged misconduct:

1. **Pre-incident Security Statement fraud**: Misrepresentations in SolarWinds' corporate website "Security Statement" about access controls and password policies (2017–2020).
2. **Risk factor filing fraud**: False or misleading cybersecurity risk disclosures in annual and quarterly SEC filings.
3. **Post-breach Form 8-K fraud**: Misleading disclosures in December 2020 and subsequent filings about the nature and scope of the SUNBURST attack.
4. **Marketing communications fraud**: False cybersecurity capability claims in press releases, blog posts, and podcasts.
5. **Internal accounting controls failures**: Violations of Section 13(b)(2)(B) of the Securities Exchange Act of 1934 by allegedly failing to maintain adequate "internal accounting controls" — which the SEC interpreted to cover cybersecurity systems.
6. **Disclosure controls failures**: Violations of Exchange Act Rule 13a-15(a) for failing to maintain adequate disclosure controls and procedures.

The SEC sought permanent injunctive relief, disgorgement, civil monetary penalties, and a bar preventing Brown from serving as an officer or director of any public company — remedies that, if obtained, would have had industry-wide chilling effects on CISO recruitment and retention.

### The SEC's 2023 Cybersecurity Disclosure Rule

The enforcement action was filed contemporaneously with the SEC's [July 26, 2023 Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure Final Rule](https://www.sec.gov/newsroom/press-releases/2023-139), which codified disclosure obligations at [17 CFR § 229.106 (Regulation S-K, Item 106)](https://www.ecfr.gov/current/title-17/chapter-II/part-229/subpart-229.100/section-229.106). Item 106 requires public companies to describe their processes for assessing, identifying, and managing material cybersecurity risks, as well as board oversight and management's role in cybersecurity governance. The rule took effect September 5, 2023, with reporting obligations for annual filings covering fiscal years ending on or after December 15, 2023. The SEC had publicly presented the SolarWinds action as consistent with and a preview of enforcement under the new rule framework.

## Detailed Analysis [HIGH confidence]

### Claims Dismissed: Internal Accounting Controls — Section 13(b)(2)(B)

The ruling's most consequential holding rejected the SEC's expansion of the Exchange Act's internal accounting controls provision to cybersecurity systems. Section 13(b)(2)(B) of the Securities Exchange Act of 1934 requires public companies to "devise and maintain a system of internal accounting controls sufficient to provide reasonable assurances" that certain financial objectives are met — including that transactions are properly recorded, assets are safeguarded, and financial statements are prepared in accordance with GAAP.

Judge Engelmayer conducted a textual, historical, and purposive analysis of Section 13(b)(2)(B) and concluded that the provision's scope is limited to accounting and financial controls. The court held that the statute "cannot govern 'every internal system a public company uses to guard against unauthorized access to its assets.'" The court found that the legislative history of the Foreign Corrupt Practices Act of 1977 — which enacted Section 13(b)(2)(B) in response to slush fund and foreign bribery concerns — confirms that "internal accounting controls" refers exclusively to financial accounting integrity, not to information security or cybersecurity program adequacy.

As [Debevoise & Plimpton analyzed](https://www.debevoise.com/insights/publications/2024/07/internal-accounting-controls-claim-rejected-in), this was a definitive rejection of a theory the SEC had been advancing with increasing frequency in enforcement contexts well beyond cybersecurity. The court's holding forecloses the SEC from using Section 13(b)(2)(B) as a hook to police the sufficiency of a company's cybersecurity defenses.

### Claims Dismissed: Disclosure Controls and Procedures — Rule 13a-15(a)

Exchange Act Rule 13a-15(a) requires issuers to maintain "disclosure controls and procedures" designed to ensure that material information is captured and communicated to those responsible for SEC filings. The SEC alleged that SolarWinds violated this rule by having deficient disclosure controls that failed to flag two cybersecurity incidents for proper classification and reporting.

Judge Engelmayer dismissed these claims, holding that a disclosure controls claim requires the pleading of "systemic deficiencies" across the company's disclosure apparatus — not isolated or incident-specific errors. The two misclassified incidents the SEC pointed to did not plausibly allege that SolarWinds lacked a functioning disclosure controls system; rather, they showed at most that individual incidents were mishandled. As [Holland & Knight noted](https://www.hklaw.com/en/insights/publications/2024/07/court-in-solarwinds-case-blows-down-secs-cyber-enforcement-authority), the court made clear that "innocent errors are an inadequate basis" on which to plead deficient disclosure controls.

### Claims Dismissed: Post-SUNBURST Disclosures

All SEC claims arising from SolarWinds' post-December 2020 disclosures — including the Form 8-K filings, related press statements, and communications issued as the investigation unfolded — were dismissed. Engelmayer held that the SEC's fraud theory for these claims improperly relied on hindsight, faulting SolarWinds for not knowing in real time the full scope, attribution, and impact of the attack.

The court reasoned that novel, sophisticated nation-state attacks rarely yield immediate complete information. The SEC's pleadings assumed that SolarWinds should have known facts that only became apparent through subsequent forensic investigation. This aspect of the ruling, as [Harvard Law's Corporate Governance Blog observed](https://corpgov.law.harvard.edu/2024/08/03/court-dismisses-most-of-secs-claims-against-solarwinds/), establishes a meaningful protection for companies disclosing cyber incidents in good faith with contemporaneously available information.

### Claims Dismissed: Marketing Communications as Corporate Puffery

The SEC had alleged that SolarWinds' public marketing — press releases, blog posts, podcast appearances, and similar communications — made materially false statements about its cybersecurity capabilities. Judge Engelmayer dismissed these claims, characterizing the statements as "non-actionable corporate puffery": general, aspirational, or vague language that a reasonable investor would not rely upon as specific factual representations.

[White & Case noted](https://www.whitecase.com/insight-alert/judge-rejects-secs-aggressive-approach-cybersecurity-enforcement) that this holding limits the SEC's ability to treat routine cybersecurity marketing language as the basis for securities fraud, drawing a clear line between investor-facing material disclosures and promotional communications.

### Claims Survived: The Website "Security Statement"

The sole category of claims to survive the motion to dismiss involved SolarWinds' corporate website "Security Statement" — a document published around 2017 and maintained through the breach period that described SolarWinds' cybersecurity practices for customers, partners, and investors. The court held that the SEC adequately pled that this document contained materially false representations in two specific areas:

1. **Access controls**: The Security Statement represented that SolarWinds maintained role-based, least-privilege access controls. Internal evidence alleged in the complaint showed "largely indiscriminate provision of administrative access to employees," which the court found "blatantly contradicts" the Security Statement's claims.
2. **Password protection policies**: The Security Statement represented robust password standards that internal audits reportedly showed were not being enforced in practice.

The court further held that the Security Statement was part of the "total mix of information" available to investors because it was publicly accessible on the corporate website. Cybersecurity was central to SolarWinds' business proposition as an IT management software vendor, making the representations material to a reasonable investor. [Fenwick & West analyzed](https://www.fenwick.com/insights/publications/sec-v-solarwinds-court-dismisses-the-majority-of-the-secs-securities-fraud-claims) that this holding turns on the specificity and public accessibility of the document, not on its location (corporate website vs. SEC filing).

Critically, the surviving claims against CISO Timothy Brown personally rested on allegations that Brown had specific, documented knowledge — captured in internal communications — of the gap between the Security Statement's representations and the company's actual practices. His alleged awareness of unfavorable NIST Cybersecurity Framework assessments and SOX audit findings that were never reflected in the public Security Statement formed the core of the surviving individual liability theory.

### The Role of 17 CFR § 229.106 (Item 106)

The court did not directly adjudicate claims under the SEC's 2023 Cybersecurity Disclosure Rule (17 CFR § 229.106) because those rules were not yet in effect during the relevant conduct period (pre-2021). However, the ruling's reasoning informs how Item 106 enforcement should be understood. Item 106 requires annual descriptions of cybersecurity risk management processes, governance, and board oversight. The court's analysis suggests that:

- Liability under Item 106 annual disclosures would require the SEC to plead material falsity with scienter, not merely program inadequacy.
- Companies with documented, functioning cybersecurity programs — even imperfect ones — are in a stronger position than those with none.
- Aspirational language in Item 106 disclosures should be avoided in favor of accurate, specific descriptions tied to actual internal practices.

## Impact Assessment [HIGH confidence]

### Effect on SEC Cybersecurity Enforcement Authority

The July 2024 ruling — and its November 2025 completion — define a substantially narrower zone of SEC enforcement authority in cybersecurity than the agency had asserted:

- **Internal accounting controls theory is closed for cybersecurity**: Section 13(b)(2)(B) does not reach cybersecurity program failures. The SEC cannot use this provision to attack inadequate security controls, no matter how severe.
- **Post-incident hindsight claims face high bar**: Contemporaneous incident disclosures made in good faith with available information are protected. The SEC must prove the company knew more than it said, at the time of disclosure.
- **Marketing puffery provides limited enforcement basis**: Generic cybersecurity capability claims in promotional contexts are not actionable unless they cross into specific, investor-material representations.
- **Website and public statements are within enforcement reach**: Specific, publicly accessible statements describing security practices in concrete terms — whether on a corporate website, trust portal, or similar public document — constitute investor-facing representations and are subject to fraud claims if materially false.

### CISO Personal Liability Framework

The ruling recalibrates the CISO personal liability risk profile:

- **Broad enterprise-risk theories failed**: The SEC's attempt to hold Brown personally liable for enterprise-wide cybersecurity failures was mostly rejected. Individual liability requires a specific public statement, personal responsibility for that statement, and documented personal knowledge of its falsity.
- **Internal documentation creates exposure**: The danger to Brown arose from internal communications showing he knew of the gap between public claims and internal reality. Security executives should be aware that internal audit findings, gap analysis memos, and assessment reports may be discoverable and consequential.
- **Personal liability remains real where the elements exist**: The narrower theory that survived — specific false public statement + personal knowledge of falsity — is a viable and legally sound theory. It did not disappear; it was merely confined.

### Implications for Public Companies

The ruling establishes practical guidance for companies managing cybersecurity disclosure risk:

- Public-facing cybersecurity statements on corporate websites, trust portals, and marketing materials are within the SEC's fraud enforcement reach if materially inconsistent with internal assessments.
- Companies should maintain accurate alignment between public cybersecurity representations and internal program reality, particularly with respect to access controls, authentication standards, and framework compliance claims.
- Incident disclosure decisions should be documented contemporaneously, capturing what was known and when, to defeat hindsight-based fraud claims.

### The Complete Dismissal: November 2025

The final chapter of the case underscored the limits of the SEC's enforcement theory. After partial dismissal in July 2024, the case proceeded to discovery on the surviving Security Statement claims. Settlement discussions did not produce an agreement. On November 20, 2025, the [SEC filed a Joint Stipulation to Dismiss](https://corpgov.law.harvard.edu/2025/12/07/solarwinds-dismissed-what-the-secs-u-turn-signals-for-cyber-enforcement/) with prejudice, ending the case entirely with no penalty, consent order, or remediation requirement.

The SEC offered no substantive explanation, citing "exercise of discretion." Multiple law firms attributed the outcome to the Trump-era SEC's recalibrated enforcement philosophy — pivoting away from novel disclosure-deficiency theories toward cases involving outright fraudulent disclosure — combined with the age of the underlying conduct and the difficulty of proving the surviving narrow theory at trial.

As [A&O Shearman analyzed](https://www.aoshearman.com/en/insights/ao-shearman-on-tech/solarwinds-dismissed-what-the-secs-u-turn-signals-for-cyber-enforcement), the complete dismissal signals a significant contraction of the SEC's cybersecurity enforcement ambitions. The agency's [announcement](https://blog.freshfields.us/post/102lvrf/sec-seeks-dismissal-of-cybersecurity-disclosure-case-against-solarwinds-and-its-c) that it will focus on "fraudulent disclosure" relating to cybersecurity going forward confirms the pivot away from the broad theories tested in SolarWinds.

## Action Items

- **Audit public-facing cybersecurity representations**: Review all corporate website security statements, trust portals, product security pages, and marketing materials for accuracy against actual internal practices, assessments, and audit findings. The Security Statement theory that survived the court's motion to dismiss remains a valid enforcement basis — and the gap between public claim and internal reality is the key risk factor.
- **Document contemporaneous incident disclosure decisions**: For any material or potentially material cybersecurity incident, document in real time what was known, when it was known, what additional investigation was underway, and the basis for the materiality determination. This contemporaneous record defeats hindsight-based fraud claims.
- **Calibrate Item 106 annual disclosures**: Under [17 CFR § 229.106](https://www.ecfr.gov/current/title-17/chapter-II/part-229/subpart-229.100/section-229.106), annual governance and risk management disclosures must accurately describe actual board oversight and management processes. Aspirational or generalized descriptions that do not reflect reality create the same exposure as the Security Statement.
- **Brief CISOs on personal liability risk**: The SolarWinds ruling confirms that individual liability attaches where a CISO has personal knowledge of a gap between a specific public statement and internal reality. Legal counsel should ensure CISOs understand when internal findings trigger disclosure obligations and when to escalate to legal and investor-relations teams.
- **Avoid internal accounting controls reliance as a sword or shield**: The court's dismissal of Section 13(b)(2)(B) as a cybersecurity enforcement tool is specific to the SEC's use of that provision. It does not affect other federal or state cybersecurity requirements. Companies should not infer from this ruling that cybersecurity controls are exempt from legal requirements generally.
- **Monitor SEC enforcement posture under current leadership**: The SEC has signaled a focus on outright fraudulent cybersecurity disclosure rather than disclosure-deficiency cases. Companies facing SEC inquiry should track whether the agency's theory sounds in fraud (and thus must plead scienter) versus a regulatory compliance theory.

## Related Reports

- [reports/cybersecurity/enforcement-actions/federal-sec-solarwinds-dismissal-2024-07-18.md](reports/cybersecurity/enforcement-actions/federal-sec-solarwinds-dismissal-2024-07-18.md) — Companion report covering the same SDNY ruling from the perspective of the CISO liability question and the complete November 2025 final dismissal.
- [reports/cybersecurity/enforcement-actions/federal-sec-coinbase-sdny-ruling-2024-03-27.md](reports/cybersecurity/enforcement-actions/federal-sec-coinbase-sdny-ruling-2024-03-27.md) — Related SDNY ruling addressing limits of SEC enforcement authority against a technology company in a different context.
- [reports/cybersecurity/incident-reporting/federal-circia-final-rule-delay-2026-04-07.md](reports/cybersecurity/incident-reporting/federal-circia-final-rule-delay-2026-04-07.md) — Federal cybersecurity incident reporting rule development, relevant context for the regulatory landscape in which SEC disclosure enforcement operates.

## Sources

1. [SDNY Opinion: SEC v. SolarWinds Corp. and Timothy G. Brown (Dkt. 125, July 18, 2024)](https://www.nysd.uscourts.gov/sites/default/files/2024-07/SolarWinds%20Opinion%20(Dkt.%20125).pdf) — Official 107-page court opinion dismissing most SEC claims; primary legal authority for the ruling.
2. [SEC Litigation Release LR-26423: SolarWinds Corp. and Timothy G. Brown](https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26423) — Official SEC page for the enforcement action including links to the original complaint.
3. [SEC Press Release: SEC Charges SolarWinds and CISO with Fraud, Internal Control Failures (Oct. 30, 2023)](https://www.sec.gov/newsroom/press-releases/2023-227) — Original SEC announcement of charges describing the enforcement theory.
4. [eCFR: 17 CFR § 229.106 — Cybersecurity (Item 106)](https://www.ecfr.gov/current/title-17/chapter-II/part-229/subpart-229.100/section-229.106) — Official regulatory text of the 2023 cybersecurity disclosure rule requirement for annual reports.
5. [SEC Press Release: SEC Adopts Rules on Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure (July 26, 2023)](https://www.sec.gov/newsroom/press-releases/2023-139) — Official announcement of the July 2023 cybersecurity disclosure rule adoption.
6. [Holland & Knight: Court in SolarWinds Case Blows Down SEC's Cyber Enforcement Authority (July 2024)](https://www.hklaw.com/en/insights/publications/2024/07/court-in-solarwinds-case-blows-down-secs-cyber-enforcement-authority) — Primary source law firm analysis (finding source); detailed breakdown of dismissed claims and enforcement authority implications.
7. [Harvard Law Corporate Governance Blog: Court Dismisses Most of SEC's Claims Against SolarWinds (Aug. 3, 2024)](https://corpgov.law.harvard.edu/2024/08/03/court-dismisses-most-of-secs-claims-against-solarwinds/) — Detailed academic and practitioner analysis of the ruling's legal significance.
8. [Harvard Law Corporate Governance Blog: SolarWinds Dismissed — What the SEC's U-turn Signals for Cyber Enforcement (Dec. 7, 2025)](https://corpgov.law.harvard.edu/2025/12/07/solarwinds-dismissed-what-the-secs-u-turn-signals-for-cyber-enforcement/) — Post-final dismissal analysis of the complete arc of the case and enforcement implications.
9. [Gibson Dunn: Dismissal of Much of SEC's SolarWinds Complaint Has Potentially Broad Implications for SEC Cybersecurity Enforcement (July 2024)](https://www.gibsondunn.com/dismissal-of-much-of-secs-solarwinds-complaint-has-potentially-broad-implications-for-sec-cybersecurity-enforcement/) — Major securities enforcement firm analysis with broad enforcement implications focus.
10. [White & Case: Judge Rejects SEC's Aggressive Approach to Cybersecurity Enforcement](https://www.whitecase.com/insight-alert/judge-rejects-secs-aggressive-approach-cybersecurity-enforcement) — Analysis of the puffery holding and general enforcement posture implications.
11. [Debevoise & Plimpton: Internal Accounting Controls Claim Rejected in SolarWinds Case (July 2024)](https://www.debevoise.com/insights/publications/2024/07/internal-accounting-controls-claim-rejected-in) — Specialized analysis of the Section 13(b)(2)(B) statutory interpretation holding.
12. [Fenwick & West: SEC v. SolarWinds: Court Dismisses the Majority of the SEC's Securities Fraud Claims](https://www.fenwick.com/insights/publications/sec-v-solarwinds-court-dismisses-the-majority-of-the-secs-securities-fraud-claims) — Technology-sector focused analysis of the ruling including Security Statement analysis.
13. [Skadden: Takeaways from the Dismissal of SEC Claims Against SolarWinds and Its CISO (Aug. 2024)](https://www.skadden.com/insights/publications/2024/08/takeaways-from-the-dismissal-of-sec-claims) — Major securities litigation firm analysis with CISO liability focus.
14. [A&O Shearman: SolarWinds Dismissed — What the SEC's U-turn Signals for Cyber Enforcement](https://www.aoshearman.com/en/insights/ao-shearman-on-tech/solarwinds-dismissed-what-the-secs-u-turn-signals-for-cyber-enforcement) — Post-final dismissal analysis of shifting enforcement priorities.
15. [Freshfields: SEC Seeks Dismissal of Cybersecurity Disclosure Case Against SolarWinds and CISO](https://blog.freshfields.us/post/102lvrf/sec-seeks-dismissal-of-cybersecurity-disclosure-case-against-solarwinds-and-its-c) — Coverage of the SEC's November 2025 voluntary dismissal motion and stated rationale.
16. [Crowell & Moring: U.S. Federal District Court Judge Dismisses Much of SEC's Claims Against SolarWinds](https://www.crowell.com/en/insights/client-alerts/us-federal-district-court-judge-dismisses-much-of-secs-claims-against-solarwinds-and-its-ciso-relating-to-sunburst-cybersecurity-attack) — Analysis covering the SUNBURST attack background and claims analysis.
17. [Alston & Bird: First of Its Kind: Federal Court Dismisses Majority of SEC's SolarWinds Action](https://www.alston.com/en/insights/publications/2024/07/federal-court-dismisses-majority-of-sec-solarwinds) — "First of its kind" framing and analysis of novel enforcement theories dismissed.
