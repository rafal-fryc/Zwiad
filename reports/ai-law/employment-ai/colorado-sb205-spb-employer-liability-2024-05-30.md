---
title: "Colorado SB 24-205: Algorithmic Discrimination Liability for Private-Sector Employers — Squire Patton Boggs Analysis"
date: 2024-05-30
jurisdiction: "Colorado"
category: "ai-law"
development_type: "legislation"
finding_id: "SCAN-20240530-007"
topic_key: "colorado-6c568e83-2024"
topic_type: "state_bill"
first_reported: 2024-05-30
last_updated: 2026-04-15
status_history:
  - "2026-04-15: Revised per reviewer round 1 — corrected Illinois HB 3773 signing month from September to August 2024; fixed Executive Summary enforcement language to include district attorneys; corrected comparison table IHRC→IDHR/IHRC and added Illinois $5,000 vs. Colorado $20,000 penalty note."
cluster: "Colorado AI Act (SB 24-205): Enforcement and Amendments"
cluster_slug: "colorado-ai-act-sb-24-205-enforcement"
---

# Colorado SB 24-205: Algorithmic Discrimination Liability for Private-Sector Employers — Squire Patton Boggs Analysis

**Jurisdiction:** Colorado | **Category:** AI Law — Employment AI | **Date:** May 30, 2024

> **Source perspective note:** This research memo is based primarily on the analysis published by Squire Patton Boggs on the *Employment Law Worldview* blog, which frames Colorado SB 24-205 specifically from the angle of private-sector employer liability and HR risk management. For a broader statutory overview and full legislative history of SB 24-205, see [reports/ai-law/state-legislation/colorado-sb205-ai-act-2024-05-20.md](../state-legislation/colorado-sb205-ai-act-2024-05-20.md). For the dedicated Littler Mendelson employer analysis, see [reports/ai-law/employment-ai/colorado-sb205-employer-ai-employment-2024-05-20.md](colorado-sb205-employer-ai-employment-2024-05-20.md).

## Executive Summary [HIGH confidence]

On May 17, 2024, Colorado became the first U.S. state to enact a law directly imposing liability on private-sector employers for algorithmic discrimination caused by the use of AI in employment decisions. [Senate Bill 24-205](https://leg.colorado.gov/bills/sb24-205), signed by Governor Jared Polis, applies to any employer that uses an AI system as a "substantial factor" in a "consequential decision" touching employment — including hiring, firing, promotions, compensation, benefits, and other material employment actions. Employers acting as AI "deployers" must exercise "reasonable care" to prevent algorithmic discrimination, implement risk management programs aligned with frameworks such as the NIST AI Risk Management Framework, conduct periodic impact assessments, provide individualized adverse-action notices, and enable human review of adverse AI-driven employment decisions. Enforcement rests exclusively with government actors (Colorado Attorney General and district attorneys); there is no private right of action. The [Squire Patton Boggs Employment Law Worldview](https://www.employmentlawworldview.com/could-artificial-intelligence-create-real-liability-for-employers-colorado-just-passed-the-first-u-s-law-addressing-algorithmic-discrimination-in-private-sector-use-of-ai-systems-us/) analysis emphasizes that the "reasonable care" negligence standard creates real, actionable employer liability independent of any showing of intentional discrimination — a significant departure from traditional employment discrimination law. The effective date, after a legislative delay, is June 30, 2026.

## Background [HIGH confidence]

### Colorado as National First Mover

Prior to SB 24-205, no U.S. state had enacted legislation directly imposing a duty of care on private-sector employers in connection with AI-assisted employment decisions. Existing federal and state frameworks addressed employer discrimination through intentional-conduct standards (Title VII) or narrow, sector-specific rules (Illinois's Artificial Intelligence Video Interview Act of 2019 covering AI analysis of video interviews, Maryland's 2020 requirement for candidate disclosure in AI-assisted hiring, and New York City's Local Law 144 requiring bias audits for automated employment decision tools in hiring). None of those laws imposed a general negligence-style standard applicable across the full employment lifecycle.

[Squire Patton Boggs](https://www.employmentlawworldview.com/could-artificial-intelligence-create-real-liability-for-employers-colorado-just-passed-the-first-u-s-law-addressing-algorithmic-discrimination-in-private-sector-use-of-ai-systems-us/) characterizes SB 24-205 as the first U.S. law specifically aimed at "algorithmic discrimination in private sector use of AI systems" — and notes its reach extends well beyond hiring to include performance evaluations, compensation decisions, benefits eligibility, promotions, and termination. The law also covers staffing agencies and any other private-sector entity using AI to make or substantially influence employment decisions affecting Colorado consumers.

### Legislative Path and Governor's Concerns

SB 24-205 was introduced by Senator Robert Rodriguez in the 2024 Colorado legislative session. It passed the Senate on May 3, 2024, the House on May 8, 2024, and was signed on May 17, 2024. Governor Polis signed the law with explicit reservations, [stating in his signing letter](https://www.dwt.com/-/media/files/blogs/artificial-intelligence-law-advisor/2024/05/sb24205-signing-statement.pdf) that the negligence standard "deviates from the traditional method of addressing discrimination" — which historically requires proof of intentional conduct — and called on the Colorado legislature to improve the law before its effective date. Polis also raised concern about regulatory fragmentation, urging federal AI legislation that would supersede SB 24-205. The [signed enrolled bill text](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf) is available from the Colorado General Assembly.

On August 28, 2025, Colorado Governor Polis signed [SB 25B-004](https://leg.colorado.gov/bills/sb25b-004), delaying the effective date from February 1, 2026 to June 30, 2026, following pressure from the business community and a failed special legislative session that did not produce substantive amendments. As analyzed by [Seyfarth Shaw](https://www.seyfarth.com/news-insights/artificial-intelligence-legal-roundup-colorado-postpones-implementation-of-ai-law-as-california-finalizes-new-employment-discrimination-regulations-and-illinois-disclosure-law-set-to-take-effect.html), the postponement gives employers additional runway but does not change the substantive compliance obligations.

### Comparative Employment Law Context

When Colorado enacted SB 24-205, Colorado and Illinois were the only U.S. jurisdictions specifically regulating employers' use of AI in private-sector employment decisions. Illinois's approach — amending the Human Rights Act via [HB 3773](https://regulations.ai/regulations/illinois-hb-3773-ai-employment-discrimination-2024) — makes algorithmic discrimination an actionable civil rights violation under the state's Human Rights Act, allowing employees to bring private claims. Colorado's CAIA, by contrast, imposes a proactive compliance regime with AG-only enforcement. As [Squire Patton Boggs subsequently noted](https://www.employmentlawworldview.com/illinois-enacts-new-ai-legislation-joining-colorado-as-the-only-states-regulating-algorithmic-discrimination-in-private-sector-use-of-ai-systems-us/), Illinois joined Colorado in August 2024 (Governor Pritzker signed HB 3773 on August 9, 2024) as the second state to regulate algorithmic discrimination in private sector AI use, but took a materially different enforcement approach.

## Detailed Analysis [HIGH confidence]

### Statutory Architecture: How Employment AI Becomes "High-Risk"

Under [SB 24-205 Section 6-1-1702](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf), an AI system is "high-risk" when, upon deployment, it "makes, or is a substantial factor in making, a consequential decision." A "consequential decision" includes any determination with a "material legal or similarly significant effect" on a consumer's access to or the cost or terms of **employment or employment opportunities** — expressly listed among the statute's covered domains (alongside education, financial services, healthcare, housing, insurance, and legal services).

This definition captures a broad range of commercial AI products in the HR technology market:

- **Applicant tracking and resume screening systems** that rank, filter, or score job candidates
- **Structured interview analysis tools** that evaluate candidate responses via audio, video, or behavioral analysis
- **AI-powered performance management platforms** that rate, rank, or flag employee productivity or conduct
- **Workforce analytics and succession planning tools** that surface or suppress candidates for advancement
- **Compensation benchmarking and pay equity AI** that determines or recommends salary ranges
- **Termination risk and workforce reduction tools** that identify employees for separation

The law does not set any minimum percentage threshold for when AI becomes a "substantial factor." Squire Patton Boggs and other employment law analysts flag this as a key definitional ambiguity: an ATS or scoring tool that is one of several inputs into a hiring decision may qualify, even if a human manager ultimately decides.

### The Developer-Deployer Framework: Employer Role

SB 24-205 distinguishes between AI **developers** (those who build or substantially modify a high-risk AI system) and AI **deployers** (those who use a high-risk AI system to make consequential decisions about consumers). For the vast majority of employers, the relevant role is that of deployer — using off-the-shelf or lightly customized HR technology from third-party vendors.

As a deployer, an employer's core statutory obligations under Section 6-1-1706 include:

**1. Implement a Risk Management Policy and Program**
A written program governing the full lifecycle of each high-risk AI system in use, aligned with a recognized framework — the statute specifically names the [NIST AI Risk Management Framework](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf), [ISO/IEC 42001](https://www.iso.org/standard/81230.html), or a substantially equivalent framework. The program must document how the employer identifies, monitors, and mitigates algorithmic discrimination risks.

**2. Conduct Impact Assessments**
Written impact assessments are required:
- Before initial deployment of any covered system
- Annually for each covered system in active use
- Within 90 days of any intentional and substantial modification to the system

Each assessment must evaluate discrimination risk, describe the categories of data processed, document performance metrics and known limitations, and describe mitigation measures planned or taken.

**3. Provide Consumer (Applicant/Employee) Notices**
Employers must disclose to affected individuals:
- Prior to or at the time of any consequential decision: the purpose of the AI system, the nature of the decision it informs, and a plain-language description of the system
- Following an adverse consequential decision: the principal reasons for the decision, information about the individual's right to correct inaccurate personal data used by the system, and information about the right to appeal

**4. Enable Human Review on Appeal**
Individuals adversely affected by a high-risk AI employment decision must have a meaningful right to appeal, including the right to human review "if technically feasible." Employers must maintain documented appeal procedures and honor them.

**5. Publish a Public Website Notice**
Deployers must post a publicly accessible disclosure identifying each high-risk AI system in use and the types of consequential decisions it informs.

**6. Report Discrimination Incidents to the AG**
If an employer discovers or receives a credible report that a high-risk AI system has caused algorithmic discrimination, it must notify the Colorado Attorney General within 90 days.

### The "Reasonable Care" Negligence Standard

The central employer liability mechanism is the duty to "use reasonable care to protect consumers from any known or reasonably foreseeable risks of algorithmic discrimination." As [Squire Patton Boggs](https://www.employmentlawworldview.com/could-artificial-intelligence-create-real-liability-for-employers-colorado-just-passed-the-first-u-s-law-addressing-algorithmic-discrimination-in-private-sector-use-of-ai-systems-us/) highlights — and as Governor Polis's [signing statement](https://www.dwt.com/-/media/files/blogs/artificial-intelligence-law-advisor/2024/05/sb24205-signing-statement.pdf) underscores — this standard diverges fundamentally from traditional employment discrimination doctrine:

- **Title VII (federal)** requires either proof of discriminatory intent (disparate treatment) or statistical proof that a specific employment practice causes a racially or otherwise protected-class disparate impact, which the employer can then rebut with a business necessity defense
- **SB 24-205** requires neither proof of intent nor statistical disparity in a specific challenged decision; it asks only whether the employer exercised "reasonable care" to prevent foreseeable discrimination risks — a tort negligence standard applied to an employment compliance obligation

The practical consequence is that employers who cannot show they followed the compliance steps — risk management program, impact assessments, adverse-action notices, appeal procedures — are potentially liable even if no actual discrimination ever occurred. Conversely, the statute creates a **rebuttable presumption of reasonable care** for employers who implement a recognized risk management framework. Following the prescribed compliance steps creates a litigation-ready evidentiary record.

### Algorithmic Discrimination Defined

The statute defines "algorithmic discrimination" to mean any condition in which use of an AI system "results in an unlawful differential treatment or impact that disfavors an individual or group of individuals on the basis of their actual or perceived age, color, disability, ethnicity, genetic information, limited proficiency in the English language, national origin, race, religion, reproductive health, sex, veteran status, or other classification protected under the laws of Colorado or federal law." The definition is outcome-oriented — it focuses on discriminatory results rather than discriminatory intent, aligning with disparate-impact doctrine rather than disparate-treatment doctrine.

### Small Employer Partial Exemption

Employers with fewer than 50 full-time equivalent employees are partially exempt from the most burdensome deployer obligations (specifically the risk management program, impact assessment, and website notice requirements) **only if all three conditions are simultaneously met**:

1. The employer does not use its own data to train or substantially customize the AI system
2. The employer uses the system only for purposes previously disclosed by the developer
3. The employer makes available to employees and applicants any impact assessment completed by the developer

Even qualifying small employers must still: exercise the duty of reasonable care, provide pre-decision and adverse-action notices, maintain appeal procedures, and report discrimination incidents to the AG. There is no size threshold exemption for AI developers; a small startup that builds employment AI for others bears full developer obligations regardless of headcount. Employers who fine-tune or customize AI tools using their own workforce data lose the exemption entirely.

### Safe Harbor for Self-Reporting and Cure

A deployer employer that discovers a violation through:
- Internal review or voluntary testing
- Adversarial testing or red-teaming
- User feedback mechanisms

...and that discloses and remediates the violation before a formal enforcement action is filed, may assert an **affirmative defense** in any subsequent AG proceeding. This safe harbor provision incentivizes employers to maintain ongoing monitoring programs and document their testing activities as part of the risk management program. A 60-day cure period is also available once the AG initiates an enforcement inquiry, for employers that cure the violation in good faith.

### Enforcement Architecture: AG-Only, No Private Right of Action

The [Colorado Attorney General](https://coag.gov/ai/) and district attorneys have exclusive enforcement authority. There is no private right of action under SB 24-205, which is a significant limitation on employee and applicant recourse under the statute itself. However, as [Seyfarth Shaw](https://www.seyfarth.com/news-insights/colorado-governor-signs-broad-ai-bill-regulating-employment-decisions.html) notes, the absence of a private right of action does not fully insulate employers: AG findings of algorithmic discrimination can seed follow-on litigation under Title VII, the Colorado Anti-Discrimination Act (CADA), or other existing anti-discrimination frameworks. Civil penalties under the [Colorado Consumer Protection Act](https://coag.gov/resources/consumer-protection/) may reach **$20,000 per violation** — a standard that accumulates per individual affected by a non-compliant decision, making systemic AI failures in high-volume hiring processes potentially catastrophic in cost.

## Impact Assessment [MEDIUM confidence]

### Scope of Affected Employers

Squire Patton Boggs and [Ogletree Deakins](https://ogletree.com/insights-resources/blog-posts/colorados-artificial-intelligence-act-what-employers-need-to-know/) both note that the broad definition of "consequential decision" in the employment context means virtually any employer using modern commercial HR software with AI features is potentially a covered deployer. This includes:

- Enterprises using Workday, SAP SuccessFactors, Oracle HCM, or similar platforms, which increasingly include AI-driven recommendations and scoring
- Mid-market employers using major ATS products (Greenhouse, Lever, iCIMS, Pinpoint, and similar)
- Employers using AI for performance management, workforce analytics, or compensation benchmarking
- Staffing and temporary staffing agencies placing workers in Colorado

Out-of-state employers with Colorado-resident employees or applicants are within scope. The law's protection extends to "Colorado consumers," which the AG is expected to interpret as including remote workers and applicants who are Colorado residents even if the employer operates no physical facility in the state.

### Comparison with Illinois Approach

As of August 2024, Colorado and Illinois stood as the only U.S. states directly regulating private-sector employer AI use. The contrast is instructive:

| Dimension | Colorado CAIA (SB 24-205) | Illinois HB 3773 |
|-----------|--------------------------|-------------------|
| Legal theory | Negligence (reasonable care) | Civil rights (anti-discrimination) |
| Private right of action | No — AG only | Yes — through Illinois Human Rights Act |
| Affirmative compliance program required | Yes (risk program, impact assessments, notices) | No affirmative program requirement |
| Protected bases | Broad (Colorado + federal protected classes) | Illinois protected classes |
| Enforcement | AG civil penalties up to $20,000/violation | IDHR complaint (IHRC adjudication or circuit court election), damages, attorneys' fees |

> **Penalty differential note:** Illinois HB 3773 caps civil penalties at $5,000 per violation, compared to Colorado's $20,000 per violation under the Consumer Protection Act. Colorado's higher per-violation exposure is especially significant for employers making AI-driven decisions at scale (e.g., high-volume resume screening), where individual violations aggregate rapidly.

The result is that employers in both states must manage different risk profiles: in Colorado, the compliance risk is regulatory (AG enforcement); in Illinois, the litigation risk is direct employee/applicant claims.

### Federal-State Tension

The Trump administration's executive order posture adds complexity. [Executive Order 14281](https://www.whitehouse.gov/presidential-actions/2025/04/restoring-equality-of-opportunity-and-meritocracy/) (April 2025) directed federal agencies to abandon disparate impact analysis. Colorado's CAIA runs directly counter to this approach — it ties employer liability to discriminatory outcomes rather than intent. Employers operating nationally must simultaneously satisfy Colorado's outcome-focused framework and federal guidance that deprioritizes disparate impact enforcement. Federal preemption of CAIA through legislation or executive action remains possible but has not materialized as of the reporting date.

### Vendor Contract and Procurement Implications

Because SB 24-205 places parallel obligations on AI developers — including documentation of bias testing, intended uses, and risk mitigation — employers should review vendor contracts for:

- Representations and warranties concerning bias evaluation during training and testing
- Indemnification provisions if the vendor's system causes algorithmic discrimination
- Contractual commitments to provide developer impact assessments (which qualifying small employers may rely upon in lieu of their own)
- Data sharing provisions relevant to employer impact assessment requirements

[Foley & Lardner](https://www.foley.com/insights/publications/2024/05/colorado-artificial-intelligence-act-human-resources-employers/) recommends negotiating for robust vendor documentation as a precondition to AI system deployment, not as an afterthought.

## Action Items

- **Inventory all employment AI:** Conduct a complete audit of AI systems used in hiring, performance management, compensation, promotion, discipline, and termination — for any tool used in decisions affecting Colorado workers. Determine whether each qualifies as a high-risk AI system under the consequential-decisions definition.
- **Pre-deploy impact assessments by June 30, 2026:** For each identified high-risk AI system not yet assessed, complete a written impact assessment before the effective date. Assessments must describe data inputs/outputs, performance metrics, known limitations, and discrimination mitigation steps.
- **Build a risk management program:** Adopt a written AI governance program aligned with NIST AI RMF or ISO 42001. The program must assign accountability, document monitoring frequency, and cover how the employer identifies, evaluates, and mitigates algorithmic discrimination risks.
- **Design adverse-action notice workflows:** For each high-risk AI system, build pre-decision and post-adverse-decision notice templates. Ensure the process provides: the decision basis in plain language, the right to correct personal data, the right to appeal to human review.
- **Review and amend vendor contracts:** Request developer documentation packages (bias testing data, intended uses, risk assessments) from all HR AI vendors before or at the time of renewal. Negotiate indemnification appropriate to SB 24-205 liability exposure.
- **Evaluate small employer exemption:** If the employer has fewer than 50 FTEs, confirm whether all three exemption conditions are met — particularly the prohibition on training or fine-tuning the AI system with proprietary employee data.
- **Institute ongoing monitoring:** Establish an annual review cycle for each covered AI system. Document monitoring results to support the rebuttable-presumption-of-reasonable-care safe harbor. Maintain records of any self-identified violations and remediation steps taken.
- **Monitor Colorado AG rulemaking:** The [AG's ADAI rulemaking page](https://coag.gov/ai/) will publish guidance interpreting covered AI systems, impact assessment standards, and safe harbor conditions before June 30, 2026.
- **Track multi-state AI employment legislation:** Follow Illinois enforcement under HB 3773 (effective January 1, 2026) and monitor proposed legislation in California, New York, and other states for additional employer AI compliance obligations.

## Related Reports

- [reports/ai-law/employment-ai/colorado-sb205-employer-ai-employment-2024-05-20.md](colorado-sb205-employer-ai-employment-2024-05-20.md) — Comprehensive Littler Mendelson-focused employer analysis of SB 24-205, covering the same provisions in depth with additional case law context and federal-state tension analysis; read together with this memo for a complete picture.
- [reports/ai-law/state-legislation/colorado-sb205-ai-act-2024-05-20.md](../state-legislation/colorado-sb205-ai-act-2024-05-20.md) — General framework overview of SB 24-205, covering both developer and deployer obligations and the full statutory structure.
- [reports/ai-law/state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md](../state-legislation/colorado-ai-act-sb24-205-passage-2024-05-14.md) — Passage-day report on SB 24-205 with legislative history, key exemptions, and enforcement timeline.
- [reports/ai-law/state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md](../state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md) — Covers the August 2025 special session enforcement delay to June 30, 2026; directly relevant to employer compliance planning.
- [reports/ai-law/employment-ai/nyc-local-law-144-aedt-bias-audit-2024-05-23.md](nyc-local-law-144-aedt-bias-audit-2024-05-23.md) — New York City Local Law 144 requiring bias audits for automated employment decision tools in hiring; the predecessor law to which Colorado's CAIA is frequently compared.
- [reports/ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md](../trump-ai-executive-order-state-preemption-2026-04-12.md) — Trump EO targeting "onerous" state AI laws; critical for assessing whether federal preemption could relieve employer compliance obligations under CAIA before June 30, 2026.

## Sources

1. [Squire Patton Boggs / Employment Law Worldview — Could Artificial Intelligence Create Real Liability for Employers? Colorado Just Passed the First U.S. Law Addressing Algorithmic Discrimination in Private Sector Use of AI Systems (US)](https://www.employmentlawworldview.com/could-artificial-intelligence-create-real-liability-for-employers-colorado-just-passed-the-first-u-s-law-addressing-algorithmic-discrimination-in-private-sector-use-of-ai-systems-us/) — Primary source for this finding; Squire Patton Boggs employment law analysis emphasizing employer liability framing and HR risk management angle
2. [Squire Patton Boggs / Employment Law Worldview — Illinois Enacts New AI Legislation, Joining Colorado as the Only States Regulating Algorithmic Discrimination in Private Sector Use of AI Systems (US)](https://www.employmentlawworldview.com/illinois-enacts-new-ai-legislation-joining-colorado-as-the-only-states-regulating-algorithmic-discrimination-in-private-sector-use-of-ai-systems-us/) — Squire Patton Boggs comparative analysis of Colorado CAIA and Illinois HB 3773
3. [National Law Review — Could Artificial Intelligence Create Real Liability for Employers?](https://natlawreview.com/article/could-artificial-intelligence-create-real-liability-employers-colorado-just-passed) — Republication of Squire Patton Boggs Employment Law Worldview article for broader industry access
4. [Colorado General Assembly — SB 24-205 Bill Page](https://leg.colorado.gov/bills/sb24-205) — Official bill page; legislative history, committee votes, enrolled bill links
5. [Colorado SB 24-205 Signed Enrolled Text (PDF)](https://content.leg.colorado.gov/sites/default/files/2024a_205_signed.pdf) — Official enrolled and signed statute; primary source for all statutory definitions and requirements cited
6. [Governor Polis Signing Statement (hosted by DWT)](https://www.dwt.com/-/media/files/blogs/artificial-intelligence-law-advisor/2024/05/sb24205-signing-statement.pdf) — Official Governor Polis signing statement expressing reservations about the negligence standard and patchwork regulation
7. [Seyfarth Shaw — Colorado Governor Signs Broad AI Bill Regulating Employment Decisions](https://www.seyfarth.com/news-insights/colorado-governor-signs-broad-ai-bill-regulating-employment-decisions.html) — Employment law firm analysis of employer obligations, enforcement mechanism, and HR impact
8. [Seyfarth Shaw — AI Legal Roundup: Colorado Postpones Implementation of AI Law](https://www.seyfarth.com/news-insights/artificial-intelligence-legal-roundup-colorado-postpones-implementation-of-ai-law-as-california-finalizes-new-employment-discrimination-regulations-and-illinois-disclosure-law-set-to-take-effect.html) — Covers August 2025 delay to June 30, 2026 and comparative state employment AI landscape
9. [Ogletree Deakins — Colorado's Artificial Intelligence Act: What Employers Need to Know](https://ogletree.com/insights-resources/blog-posts/colorados-artificial-intelligence-act-what-employers-need-to-know/) — Employment law firm analysis with focus on deployer obligations, small employer exemption conditions, and covered AI tools in HR technology
10. [Foley & Lardner — Proceed with Caution When Taking the Human Out of Human Resources](https://www.foley.com/insights/publications/2024/05/colorado-artificial-intelligence-act-human-resources-employers/) — HR-focused analysis of SB 24-205 employer obligations, vendor contract implications, and procurement recommendations
11. [Illinois HB 3773 — Regulations.AI](https://regulations.ai/regulations/illinois-hb-3773-ai-employment-discrimination-2024) — Overview of Illinois HB 3773 amending the Human Rights Act to cover algorithmic discrimination, used for Colorado-Illinois comparison
12. [McGuireWoods — Employers Beware: The Rise of AI Regulation in Illinois, Colorado and California](https://www.mcguirewoods.com/client-resources/alerts/2024/10/employers-beware-the-rise-of-ai-regulation-in-illinois-colorado-and-california/) — Multi-state employer AI compliance overview contrasting the three regulatory approaches
13. [Colorado Attorney General — ADAI Rulemaking and Enforcement](https://coag.gov/ai/) — Official AG rulemaking hub for SB 24-205; source for penalty ranges and enforcement authority
14. [NIST AI Risk Management Framework 1.0](https://www.nist.gov/system/files/documents/2023/01/26/AI%20RMF%201.0.pdf) — The federal framework that Colorado CAIA expressly designates as a qualifying risk management standard for the deployer safe harbor
15. [White House — Executive Order 14281 on Restoring Equality of Opportunity and Meritocracy](https://www.whitehouse.gov/presidential-actions/2025/04/restoring-equality-of-opportunity-and-meritocracy/) — Trump April 2025 EO directing federal agencies to abandon disparate impact analysis; creates federal-state tension with Colorado's outcome-focused employer liability standard
