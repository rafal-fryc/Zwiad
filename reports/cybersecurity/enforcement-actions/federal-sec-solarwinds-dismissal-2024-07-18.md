---
title: "SDNY Dismisses Bulk of SEC's Case Against SolarWinds and CISO Tim Brown"
date: 2024-07-18
jurisdiction: "Federal"
category: "cybersecurity"
development_type: "court-decision"
finding_id: "SCAN-20240723-023"
topic_key: "new-york-05f0f359-2024"
topic_type: "enforcement"
first_reported: 2024-07-23
last_updated: 2024-07-23
status_history: []
cluster: "SEC v. SolarWinds: Cybersecurity Disclosure Enforcement Limits"
cluster_slug: "sec-solarwinds-cybersecurity-enforcement"
---

# SDNY Dismisses Bulk of SEC's Case Against SolarWinds and CISO Tim Brown

**Jurisdiction:** Federal (S.D.N.Y.) | **Category:** Cybersecurity / Securities Enforcement | **Date:** July 18, 2024

## Executive Summary [HIGH confidence]

On July 18, 2024, U.S. District Judge Paul A. Engelmayer of the Southern District of New York issued a 107-page opinion in *SEC v. SolarWinds Corp. and Timothy G. Brown* dismissing the bulk of the SEC's securities fraud and internal controls charges arising from the December 2020 SUNBURST cyberattack. The court rejected the SEC's attempt to apply the Exchange Act's "internal accounting controls" provision to cybersecurity systems, held that post-SUNBURST disclosure claims impermissibly relied on hindsight, and dismissed statements in press releases and blog posts as non-actionable corporate puffery. A single set of claims survived — those tied to SolarWinds' corporate website "Security Statement," which the court found contained materially false representations about access controls and password protections. Both SolarWinds and its CISO, Timothy Brown, remained defendants on those surviving claims. The case ultimately ended in November 2025 when the SEC voluntarily dismissed the remaining claims with prejudice, cementing a near-total defeat for the agency's most ambitious cybersecurity enforcement action.

## Background [HIGH confidence]

### The SUNBURST Attack and Original Complaint

In December 2020, SolarWinds disclosed that threat actors — later attributed to the Russian SVR intelligence service — had injected malicious code ("SUNBURST") into the company's Orion software update mechanism, compromising approximately 18,000 customers including multiple U.S. federal agencies. The breach became one of the most significant supply-chain attacks in recorded history.

On October 30, 2023, the [SEC filed a complaint](https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26423) in the Southern District of New York charging SolarWinds and its Chief Information Security Officer, Timothy G. Brown, with fraud and internal controls violations. The complaint was sweeping in scope, targeting:

- Misrepresentations in SolarWinds' website "Security Statement" (2017–2020)
- Risk factor disclosures in annual and quarterly SEC filings
- Post-breach Form 8-K disclosures (December 2020 onward)
- Press releases, blog posts, and podcasts about the company's cybersecurity posture
- Alleged failures of "internal accounting controls" under Section 13(b)(2)(B) of the Securities Exchange Act of 1934
- Alleged failures of "disclosure controls and procedures" under Exchange Act Rule 13a-15

The charges against Brown personally marked the first time the SEC had brought a securities fraud action directly against a sitting CISO, injecting significant uncertainty into the industry about individual executive exposure under the federal securities laws.

### The SEC's 2023 Cybersecurity Disclosure Rule

The enforcement action was brought alongside — and was publicly presented as consistent with — the SEC's [July 2023 Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure rules](https://www.sec.gov/rules-regulations/2023/07/s7-09-22) (effective September 5, 2023; reporting requirements beginning December 18, 2023). Those rules require public companies to disclose material cybersecurity incidents on Form 8-K within four business days of materiality determination, and to provide annual disclosures about cybersecurity risk management, strategy, and board governance. The SEC had signaled that the SolarWinds action would serve as an enforcement template for those new obligations.

## Detailed Analysis [HIGH confidence]

### Claims Dismissed: Internal Accounting Controls (Section 13(b)(2)(B))

Judge Engelmayer's most consequential ruling rejected the SEC's effort to use Section 13(b)(2)(B) of the Exchange Act — the "internal accounting controls" provision — as a basis for cybersecurity enforcement. The court held that the word "accounting" in the statute restricts its reach to controls over financial accounting and business transactions, not to cybersecurity or information-technology systems generally.

Engelmayer conducted a detailed analysis of the statutory text, legislative history, and purpose of the provision, concluding that "the history and purpose of the statute confirm that cybersecurity controls are outside the scope of" internal controls over financial reporting. He found that Section 13(b)(2)(B) "cannot govern 'every internal system a public company uses to guard against unauthorized access to its assets'" and can only regulate systems that qualify as "internal accounting controls" in the financial sense. As [Jones Day noted](https://www.jonesday.com/en/insights/2024/07/court-rejects-sec-authority-over-cybersecurity-controls), this was a rare instance where a defendant successfully challenged the SEC's expansive reading of that provision.

### Claims Dismissed: Disclosure Controls and Procedures

The court also narrowed the SEC's use of Exchange Act Rule 13a-15's "disclosure controls and procedures" provision. Engelmayer held that the SEC could not sustain those claims where the company had disclosure controls in place and the pleading did not allege systematic, company-wide failures — only isolated or incident-specific deficiencies. The court's reading significantly constrains the SEC's ability to use disclosure control failures as a proxy for ordinary cybersecurity inadequacies.

### Claims Dismissed: Post-SUNBURST Disclosures

The court dismissed all SEC claims relating to SolarWinds' post-December 2020 disclosures — including Form 8-K filings, press releases, and communications made after the breach became public. Engelmayer held that these claims did not plausibly allege actionable deficiencies in SolarWinds' reporting. He reasoned that the pleadings impermissibly relied on hindsight and speculation: the SEC was faulting the company for not immediately knowing the full scope and attribution of the attack, which was reasonable given its novel nature and the government's own delayed attribution. According to [Harvard Law's Corporate Governance Blog](https://corpgov.law.harvard.edu/2024/08/03/court-dismisses-most-of-secs-claims-against-solarwinds/), this aspect of the ruling sets a meaningful barrier against "Monday-morning quarterbacking" of incident disclosures.

### Claims Dismissed: Press Releases, Blog Posts, and Podcasts

The court rejected SEC claims premised on SolarWinds' general marketing communications about its cybersecurity capabilities — press releases, blog posts, and podcast statements. Engelmayer characterized these as "non-actionable corporate puffery": vague, aspirational statements that a reasonable investor would not rely on as material factual representations. [White & Case observed](https://www.whitecase.com/insight-alert/judge-rejects-secs-aggressive-approach-cybersecurity-enforcement) that this holding limits the SEC's ability to treat routine cybersecurity marketing language as a basis for securities fraud.

### Claims Dismissed: Most Pre-SUNBURST Filing Disclosures

The court dismissed the SEC's pre-SUNBURST fraud and false-filing claims based on risk factor language and other statements in SolarWinds' 10-K, 10-Q, and S-1 filings, finding that the alleged misrepresentations were not plausibly pled as materially false or misleading at the time they were made.

### Claims That Survived: The Website "Security Statement"

The sole category of claims that survived the motion to dismiss involved SolarWinds' corporate website "Security Statement" — a document published in 2017 and maintained throughout the relevant period that described the company's cybersecurity practices to prospective customers and investors. The court held that the SEC adequately pleaded that this document contained materially false representations specifically regarding:

1. **Access controls**: The Security Statement claimed SolarWinds maintained robust, role-based access controls. Internal evidence alleged in the complaint showed "largely indiscriminate provision of administrative access to employees," which the court found "blatantly contradicts the Security Statement's representations."
2. **Password protection policies**: The Security Statement described strong password standards that internal audits reportedly showed were not being met.

The court further found that SolarWinds' overall cybersecurity portrayal in the Security Statement was "misleading if not outright false" given Brown's alleged awareness — documented in internal communications — that the company's NIST Cybersecurity Framework assessments and SOX audits had given poor ratings to its actual access control practices. The court found Brown personally liable on these surviving claims because he was alleged to have known of the gap between the public statement and internal reality, and had authority over the Security Statement. [Greenberg Traurig summarized](https://www.gtlaw.com/en/insights/2024/7/sec-v-solarwinds-update-us-federal-district-court-dismisses-most-of-the-secs-case-but-some-fraud-claims-and-ciso-liability-remain) the court's reasoning as: materiality was satisfied because cybersecurity was "central" to SolarWinds' core business of selling software to security-sensitive enterprise customers.

The court declined to dismiss the claims regarding compliance with the NIST Cybersecurity Framework, network monitoring practices, and secure software development lifecycle representations that the SEC had also challenged in the Security Statement, finding the pleading insufficiently specific on those sub-points.

### The CISO Personal Liability Question

The surviving claim against Brown is significant for the CISO community: Engelmayer held that, at the pleading stage, the SEC had stated a viable claim that Brown personally made — or was responsible for making — materially false representations in a public document while knowing those representations were inaccurate. As [Greenberg Traurig noted](https://www.gtlaw.com/en/insights/2024/7/sec-v-solarwinds-update-us-federal-district-court-dismisses-most-of-the-secs-case-but-some-fraud-claims-and-ciso-liability-remain), this was a narrower theory than the SEC's original sweeping theory of CISO accountability, but it left the door open to individual liability where the executive had specific knowledge of a material discrepancy.

[SolarWinds CISO Tim Brown subsequently commented](https://cyberscoop.com/tim-brown-solarwinds-liability-cyberlawcon/) that security executives were "nervous" about individual liability exposure, even as the surviving claims were narrow.

## Impact Assessment [HIGH confidence]

### Implications for SEC Cybersecurity Enforcement Authority

The July 2024 ruling substantially curtailed the SEC's cybersecurity enforcement toolkit as constructed in the SolarWinds complaint:

- **Internal accounting controls theory is foreclosed for cybersecurity**: The Exchange Act Section 13(b)(2)(B) theory cannot be used to police cybersecurity program adequacy. The SEC must rely on the securities fraud provisions (Section 10(b) and Rule 10b-5) or the new 2023 Disclosure Rule, not internal controls law.
- **Disclosure controls theory is narrowed**: Disclosure control failures must be systemic and well-pleaded; the SEC cannot use this provision to second-guess individual incident responses.
- **Post-incident hindsight claims face high pleading bar**: Companies disclosing cyber incidents in real time are protected from fraud claims based on facts that emerged only later, as long as contemporaneous disclosures were reasonable given then-available information.
- **Marketing puffery is off-limits**: Generic cybersecurity marketing language, even if aspirational and potentially misleading to lay readers, does not support securities fraud.

### Implications for the SEC's 2023 Cybersecurity Disclosure Rule

The court's ruling does not directly invalidate the [2023 Cybersecurity Disclosure Rule](https://www.sec.gov/rules-regulations/2023/07/s7-09-22), which was adopted on July 26, 2023, and took effect in December 2023. The rule's Form 8-K incident disclosure obligation (Item 1.05) and annual Form 10-K governance disclosures (Item 1C) remain in force. However, the ruling does:

- Confirm that the "material incident" standard requires the SEC to prove the company knew — and failed to disclose — material facts, not simply that, in hindsight, more could have been said
- Reinforce that the SEC's enforcement of the rule must satisfy Rule 10b-5's scienter requirement for fraud claims, rather than relying on strict-liability internal controls theories
- Suggest that companies with documented internal cybersecurity frameworks (even imperfect ones) are in a stronger position than those with no program at all

### Implications for CISO Individual Liability

The ruling sends mixed signals to CISOs:

- **The broad "CISO as enterprise risk owner" theory failed**: The SEC's attempt to hold Brown liable for enterprise-wide cybersecurity failures that manifested in investor disclosures was mostly rejected.
- **Specific false statements with personal knowledge remain a risk**: CISOs who sign off on or are responsible for specific public statements they know to be false remain exposed to individual SEC enforcement. The Security Statement theory illustrates that internal awareness of a gap between public representation and reality is the critical fact.
- **Documentation of internal findings matters**: Brown's personal exposure derived largely from internal communications showing he knew the NIST assessments showed gaps that the public Security Statement did not acknowledge.

### The Final Outcome: Complete Dismissal (November 2025)

The case's ultimate resolution further underscored the limits of the SEC's SolarWinds theory. After the court's July 2024 partial dismissal, discovery proceeded on the surviving Security Statement claims. On July 2, 2025, the parties announced a settlement in principle; the court stayed the case. The anticipated settlement did not materialize. On November 20, 2025, the SEC filed a [Joint Stipulation to Dismiss](https://corpgov.law.harvard.edu/2025/12/07/solarwinds-dismissed-what-the-secs-u-turn-signals-for-cyber-enforcement/) with prejudice, ending the case entirely without any penalty, consent order, or remediation requirement against SolarWinds or Brown.

[The SEC offered no substantive explanation](https://www.alstonprivacy.com/sec-dismisses-remaining-claims-against-solarwinds/), stating only that the dismissal was an "exercise of discretion" that "does not necessarily reflect its position on any other case." Analysts at multiple law firms attributed the outcome to a combination of: the narrowed surviving theory being difficult to prove at trial; the Trump-era SEC's recalibration of enforcement priorities toward "fraudulent disclosure" rather than disclosure-deficiency cases; and the age of the underlying conduct.

As [Jones Day observed](https://www.jonesday.com/en/insights/2025/12/sec-dismisses-remaining-solarwinds-claims), the complete dismissal is a landmark outcome signaling a significant contraction of the SEC's ambitions in cybersecurity enforcement.

## Action Items

- **Review public-facing cybersecurity statements**: Companies should audit all website security statements, trust portals, and marketing materials describing their cybersecurity practices against their actual internal assessments, audits, and gap analyses. The Security Statement theory that survived the SolarWinds motion remains a viable basis for future SEC enforcement — the specific gap between public claims and internal findings is the key risk.
- **Maintain records showing good-faith disclosure decisions**: Following the court's hindight-bar ruling, document your contemporaneous decision-making process for cyber incident disclosures. Notes showing what was known, when, and why the materiality determination was made protect against after-the-fact second-guessing.
- **Calibrate Form 10-K Item 1C disclosures to actual program maturity**: The 2023 SEC Cybersecurity Disclosure Rule's annual governance disclosure remains in force. Companies should ensure that board oversight and risk management descriptions reflect actual organizational reality, not aspirational descriptions.
- **Train CISOs on securities disclosure obligations**: The SolarWinds ruling confirms that CISOs with personal knowledge of gaps between public representations and internal reality face individual exposure. Legal counsel should brief CISOs on when awareness of cybersecurity deficiencies triggers disclosure obligations.
- **Monitor SEC enforcement posture under current leadership**: The final dismissal of SolarWinds reflects a shift in SEC enforcement philosophy under the Trump administration, but the 2023 Cybersecurity Disclosure Rule remains in force and the agency has signaled continued interest in outright fraudulent disclosure cases.
- **Do not rely on the internal accounting controls dismissal as a complete shield**: While the court foreclosed Section 13(b)(2)(B) as a standalone cybersecurity enforcement theory, the SEC can still pursue securities fraud claims under Section 10(b) where specific material false statements about cybersecurity are alleged.

## Related Reports

- [reports/cybersecurity/enforcement-actions/federal-sec-coinbase-sdny-ruling-2024-03-27.md](reports/cybersecurity/enforcement-actions/federal-sec-coinbase-sdny-ruling-2024-03-27.md) — Both cases involve SDNY court rulings on the scope of SEC enforcement authority in technology-adjacent contexts; the Coinbase ruling also addressed the limits of SEC jurisdictional claims against a technology company.

## Sources

1. [SEC Litigation Release LR-26423: SolarWinds Corp. and Timothy G. Brown](https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26423) — Official SEC announcement of the original October 2023 enforcement action against SolarWinds and Brown.
2. [SEC Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure — Final Rule (S7-09-22)](https://www.sec.gov/rules-regulations/2023/07/s7-09-22) — Official text of the July 2023 SEC cybersecurity disclosure rule, effective September 2023.
3. [SEC Press Release: SEC Adopts Rules on Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure](https://www.sec.gov/newsroom/press-releases/2023-139) — Official agency announcement of the 2023 rule adoption.
4. [Court Dismisses Most of SEC's Claims Against SolarWinds (Harvard Law Corporate Governance Blog, Aug. 3, 2024)](https://corpgov.law.harvard.edu/2024/08/03/court-dismisses-most-of-secs-claims-against-solarwinds/) — Detailed academic analysis of the July 2024 ruling including analysis of surviving and dismissed claims.
5. [SolarWinds Dismissed: What the SEC's U-turn Signals for Cyber Enforcement (Harvard Law Corporate Governance Blog, Dec. 7, 2025)](https://corpgov.law.harvard.edu/2025/12/07/solarwinds-dismissed-what-the-secs-u-turn-signals-for-cyber-enforcement/) — Post-final dismissal analysis of the full arc of the case and enforcement implications.
6. [Paul, Weiss: SDNY Court Deals Blow to SEC Cyber Enforcement, Dismisses Most Charges Against SolarWinds and Its CISO](https://www.paulweiss.com/practices/litigation/cybersecurity-data-protection/publications/sdny-court-deals-blow-to-sec-cyber-enforcement-dismisses-most-charges-against-solarwinds-and-its-ciso?id=52318) — Comprehensive client alert analyzing all dismissed and surviving claims with detailed legal analysis.
7. [Skadden: Takeaways from the Dismissal of SEC Claims Against SolarWinds and Its CISO](https://www.skadden.com/insights/publications/2024/08/takeaways-from-the-dismissal-of-sec-claims) — Law firm analysis of the ruling's key takeaways for public companies.
8. [Jones Day: Court Rejects SEC Authority Over Cybersecurity Controls and Most Alleged Disclosure Violations](https://www.jonesday.com/en/insights/2024/07/court-rejects-sec-authority-over-cybersecurity-controls) — Analysis of the internal accounting controls ruling and statutory interpretation.
9. [Jones Day: SEC Dismisses Remaining SolarWinds Claims (Dec. 2025)](https://www.jonesday.com/en/insights/2025/12/sec-dismisses-remaining-solarwinds-claims) — Analysis of the final November 2025 joint stipulation dismissal.
10. [Greenberg Traurig: SEC v. SolarWinds Update — Dismisses Most of SEC's Case, But Some Fraud Claims and CISO Liability Remain](https://www.gtlaw.com/en/insights/2024/7/sec-v-solarwinds-update-us-federal-district-court-dismisses-most-of-the-secs-case-but-some-fraud-claims-and-ciso-liability-remain) — Analysis of CISO personal liability implications and surviving Security Statement claims.
11. [Cleary Gottlieb: SDNY Court Dismisses Several SEC Claims Against SolarWinds and its CISO](https://www.clearygottlieb.com/news-and-insights/publication-listing/sdny-court-dismisses-several-sec-claims-against-solarwinds-and-its-ciso) — Substantive legal analysis of the ruling from a leading securities litigation firm.
12. [White & Case: Judge Rejects SEC's Aggressive Approach to Cybersecurity Enforcement](https://www.whitecase.com/insight-alert/judge-rejects-secs-aggressive-approach-cybersecurity-enforcement) — Analysis of the puffery holding and broader enforcement posture implications.
13. [Holland & Knight: Court in SolarWinds Case Blows Down SEC's Cyber Enforcement Authority](https://www.hklaw.com/en/insights/publications/2024/07/court-in-solarwinds-case-blows-down-secs-cyber-enforcement-authority) — Analysis of the ruling's impact on SEC enforcement authority.
14. [Alston & Bird: SEC Dismisses Remaining Claims Against SolarWinds](https://www.alstonprivacy.com/sec-dismisses-remaining-claims-against-solarwinds/) — Coverage of the final November 2025 dismissal and SEC's stated rationale.
15. [Fenwick: SEC v. SolarWinds: Court Dismisses the Majority of the SEC's Securities Fraud Claims](https://www.fenwick.com/insights/publications/sec-v-solarwinds-court-dismisses-the-majority-of-the-secs-securities-fraud-claims) — Technology-sector focused analysis of the ruling.
16. [Cooley: Federal Court Dismisses Bulk of SEC's Complaint Against SolarWinds in Cyberattack Case](https://www.cooley.com/news/insight/2024/2024-07-23-federal-court-dismisses-bulk-of-secs-complaint-against-solarwinds-in-cyberattack-case) — Law firm analysis with focus on compliance implications.
17. [Debevoise & Plimpton: Internal Accounting Controls Claim Rejected in SolarWinds Case](https://www.debevoise.com/insights/publications/2024/07/internal-accounting-controls-claim-rejected-in) — Specialized analysis of the Section 13(b)(2)(B) statutory interpretation holding.
18. [CyberScoop: SolarWinds CISO says security execs are 'nervous' about individual liability for data breaches](https://cyberscoop.com/tim-brown-solarwinds-liability-cyberlawcon/) — Coverage of Tim Brown's public remarks on CISO liability concerns following the ruling.
19. [Hunton Andrews Kurth: Judge Dismisses Most of SEC Case Against SolarWinds and Its CISO](https://www.hunton.com/privacy-and-information-security-law/judge-dismisses-most-of-sec-case-against-solarwinds-and-its-ciso) — Privacy and cybersecurity practice group analysis.
