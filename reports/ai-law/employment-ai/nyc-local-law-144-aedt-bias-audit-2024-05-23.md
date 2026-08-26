---
title: "NYC Local Law 144: AI Bias Audit Mandates for Automated Employment Decision Tools and the Emerging National Landscape"
date: 2024-05-23
jurisdiction: "New York"
category: "ai-law"
development_type: "other"
finding_id: "SCAN-20240523-027"
topic_key: "new-york-601113b3-2024"
topic_type: "guidance"
first_reported: 2024-05-23
last_updated: 2024-05-23
status_history: []
cluster: "NYC Local Law 144: AEDT Bias Audit Mandate"
cluster_slug: "nyc-local-law-144-aedt-bias-audits"
---

# NYC Local Law 144: AI Bias Audit Mandates for Automated Employment Decision Tools and the Emerging National Landscape

**Jurisdiction:** New York (New York City) | **Category:** AI Law — Employment AI | **Date:** May 23, 2024

## Executive Summary [HIGH confidence]

New York City [Local Law 144 of 2021](https://legistar.council.nyc.gov/LegislationDetail.aspx?ID=4344524&GUID=B051915D-A9AC-451E-81F8-6596032FA3F9) became the world's first law to mandate annual independent bias audits for automated employment decision tools (AEDTs) used in hiring and promotion. Enacted December 11, 2021, and in force with enforcement beginning July 5, 2023, the law requires covered employers to: (1) obtain an annual bias audit from an independent auditor; (2) publicly post audit results; and (3) provide advance notice to job candidates and employees. As of mid-2024, compliance research presented at the ACM FAccT 2024 conference revealed widespread non-compliance — of 391 employers studied, only 18 posted audit reports and 13 posted transparency notices — a phenomenon the researchers termed "null compliance." The NYC Department of Consumer and Worker Protection (DCWP), charged with enforcement, has issued only minimal enforcement actions and identified a single non-compliance issue in its own review of 32 companies. The law has nonetheless generated a national ripple effect: Maryland, New Jersey, Illinois, and Colorado have all introduced or enacted related legislation by mid-2024, and the EEOC issued Title VII guidance in May 2023 reinforcing that federal anti-discrimination law applies to AI-driven hiring tools.

## Background [HIGH confidence]

### The Problem: AI in Hiring and Algorithmic Discrimination

Automated tools — including applicant tracking systems with AI scoring, video interview analysis software, resume-parsing algorithms, and personality assessment platforms — have become standard infrastructure in large-scale hiring. These tools are often purchased from third-party vendors and deployed across thousands of candidate applications. Research consistently demonstrates that such tools can perpetuate or amplify historical labor market discrimination, producing lower selection rates for women, racial minorities, and people with disabilities without human reviewers perceiving or intending the discrimination.

Prior to Local Law 144, no jurisdiction in the United States or globally required employers to subject these tools to independent auditing or public reporting. Federal anti-discrimination law (Title VII of the Civil Rights Act, the ADA, the ADEA) prohibits discriminatory employment practices but does not require affirmative pre-deployment testing, audit reporting, or candidate notification when AI tools are used.

### Legislative History

The bill that became Local Law 144, introduced as [Int 1894-2020](https://legistar.council.nyc.gov/LegislationDetail.aspx?ID=4344524&GUID=B051915D-A9AC-451E-81F8-6596032FA3F9) in the New York City Council, was sponsored by Council Member Laurie Cumbo. It passed the Council and was signed into law by Mayor Bill de Blasio on December 11, 2021, becoming [Local Law 144 of 2021](https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page). The law became effective January 1, 2023.

The law's implementation was delayed repeatedly due to complexity of the implementing rules. The NYC Department of Consumer and Worker Protection (DCWP, formerly the Department of Consumer Affairs or DCA) was designated as the enforcement agency. DCWP issued a first proposed rule, revised proposed rule, and ultimately adopted [Final Rules](https://rules.cityofnewyork.us/rule/automated-employment-decision-tools-2/) effective April 6, 2023, with enforcement commencing July 5, 2023. An [Updated Final Rule](https://rules.cityofnewyork.us/rule/automated-employment-decision-tools-updated/) was subsequently issued to address outstanding questions.

### Federal Context: EEOC 2023 AI Guidance

Simultaneous with NYC enforcement beginning, the U.S. Equal Employment Opportunity Commission issued [technical assistance guidance on May 18, 2023](https://www.eeoc.gov/sites/default/files/2024-04/20240429_What%20is%20the%20EEOCs%20role%20in%20AI.pdf) clarifying that Title VII's disparate impact doctrine applies to employer use of AI in selection processes. The EEOC's guidance reinforced that employers remain liable for discriminatory outcomes from AI tools even when those tools are supplied by third-party vendors, and that the four-fifths (80%) rule applies to assess adverse impact from algorithmic selection. This established a parallel federal pathway for enforcement that does not require a bias audit mandate — but creates employer liability for disparate impact outcomes regardless of intent. The EEOC also published [guidance for workers](https://www.eeoc.gov/sites/default/files/2024-04/20240429_Employment%20Discrimination%20and%20AI%20for%20Workers.pdf) in April 2024 explaining their rights when employers use AI.

## Detailed Analysis [HIGH confidence]

### Scope: What Counts as an AEDT

Under Local Law 144, an "automated employment decision tool" is defined as any computational process derived from machine learning, statistical modeling, data analytics, or artificial intelligence that issues a simplified output — including a score, classification, or recommendation — that is used to substantially assist or replace discretionary decision-making by an employer or employment agency in connection with hiring or promotion decisions in New York City.

The [DCWP Final Rules](https://rules.cityofnewyork.us/rule/automated-employment-decision-tools-2/) clarify that the law covers tools that "substantially assist or replace" human decision-making. A tool "substantially assists" if: the employer relies on it as one of the primary sources in its decision; the employer uses it to overrule human decision-making; or the employer uses it in a way that constrains human discretion to a set of candidates identified by the tool. Purely rules-based systems (e.g., keyword filtering that does not involve machine learning or statistical modeling) are not AEDTs. Tools used only after a final hiring decision has been made are also excluded.

Key tools likely covered include: AI-based resume scoring and ranking systems, chatbot or video interview AI tools that score candidate responses, personality or cognitive assessment tools that use AI to generate hiring recommendations, and predictive analytics used to flag or advance candidates.

### Bias Audit Requirements

The centerpiece of the law is the annual bias audit requirement. Key requirements per the [Final Rules](https://rules.cityofnewyork.us/rule/automated-employment-decision-tools-2/) include:

**Independent Auditor:** The audit must be conducted by an independent auditor — defined as one who is not employed by the employer or the AEDT vendor; has no involvement in use, development, or distribution of the AEDT; and has no direct or material indirect financial interest in the employer, employment agency, or vendor.

**Data Requirements:** The audit must be conducted using historical data from the employer's own use of the AEDT, if available and statistically significant. If insufficient historical data exists, the auditor may use test data, but the audit summary must explain the reason and describe the test data source.

**Metrics Required:** Audit summaries must include: the date of the most recent bias audit; the AEDT's distribution date; the source and description of the data used; the number of individuals assessed in "unknown" categories; the number of applicants or candidates; and selection rates and impact ratios by sex, race, and ethnicity. The impact ratio is calculated as the selection rate for a category divided by the selection rate for the most-selected category.

**Publication:** Audit results must be published on the employer's website in the "Employment" or "Jobs" section. They must remain accessible for at least three years after the date of the most recent audit.

**Annual Recurrence:** A new bias audit must be obtained no more than one year prior to each use of the AEDT.

**Important Limitation:** The law does not require employers to take any action based on audit results. An employer may use an AEDT with documented bias and remain technically compliant, so long as the audit was conducted and published. This design choice was deliberate — lawmakers opted for transparency over mandated outcome thresholds.

### Notice Requirements

Employers must provide at least 10 business days' advance notice to candidates or employees residing in New York City before using an AEDT. The [DCWP FAQ](https://www.nyc.gov/assets/dca/downloads/pdf/about/DCWP-AEDT-FAQ.pdf) clarifies that notice may be provided via job posting or by mail or email. The notice must include: the fact that an AEDT will be used; how and what data will be collected; and the type of AEDT being used. Candidates may request that the employer instead use an alternative selection process or have the position kept open during the notice period. Employers are not required to accommodate such requests but must have a policy on how they respond.

### Penalties

Civil penalties run from $500 per violation on the first day to between $500 and $1,500 per day for each subsequent day of violation. Each day of use without a compliant bias audit is a separate violation; each failure to provide notice to an individual applicant or employee is also a separate violation. High-volume hiring scenarios can generate substantial aggregate liability.

### Compliance Reality: The "Null Compliance" Finding

Research published at the [2024 ACM Conference on Fairness, Accountability, and Transparency (FAccT 2024)](https://dl.acm.org/doi/10.1145/3630106.3658998) by researchers at the Center for Technology and Society studied 391 employers and found that only 18 had posted bias audit reports and only 13 had posted transparency notices. A companion [preprint on arXiv](https://arxiv.org/abs/2406.01399) describes the structural problem: because the law gives employers substantial self-assessment discretion over whether their system is "in scope," the absence of a posted audit cannot be conclusively identified as non-compliance — the employer may have determined its tool is not an AEDT. The researchers termed this "null compliance": a compliance regime where violations are structurally invisible.

Of the 18 bias audit reports that were published, 96% showed impact ratios above the 0.8 threshold — suggesting either genuinely low disparate impact or a selection effect in which employers only publish favorable audits. Interviews with audit industry professionals conducted by the same team suggested many AEDTs on the market would fail the four-fifths rule if audited without self-selection bias.

### DCWP Enforcement: A Structural Challenge

The [New York State Comptroller's audit of DCWP's LL 144 enforcement](https://www.osc.ny.gov/state-agencies/audits/2025/12/02/enforcement-local-law-144-automated-employment-decision-tools) (published December 2025, covering the enforcement period) found critical weaknesses:

- DCWP received only two AEDT-related complaints during the period reviewed, but did not investigate whether the complaint intake process was functioning.
- Of test calls placed to the NYC 311 hotline about AEDT issues, 75% were misrouted and never reached DCWP.
- DCWP reviewed 32 companies' websites and bias audits and identified one compliance issue. When the Comptroller reviewed the same 32 companies, at least 17 potential non-compliance issues were identified.
- DCWP's enforcement strategy relies primarily on complaint-based enforcement with insufficient proactive monitoring.

The State Comptroller recommended that DCWP improve its complaint routing, expand proactive compliance reviews, and conduct renewed stakeholder education.

## Impact Assessment [MEDIUM confidence]

### Who Is Affected

The law applies to any employer or employment agency that uses an AEDT in the screening of candidates for employment at a job, position, or category of jobs in New York City, or in the evaluation of employees for promotion. Covered entities include: private employers with operations in New York City; staffing agencies placing workers in NYC; remote-hire employers evaluating NYC-based candidates; and employment agencies operating in NYC regardless of headquarters location.

The law is notable for extraterritorial reach: a company headquartered in California that uses an AI résumé screener to evaluate applicants for a New York City position must comply if the applicant is a New York City resident. Given New York City's labor market size, this effectively applies to the national and international applicant pools of any employer with significant NYC operations.

### Industry Impact

Sectors most materially affected include: financial services (major banks and insurance companies use AI in hiring at scale); technology companies (large engineering and product hiring funnels); consulting and professional services; healthcare and life sciences (high-volume clinical and administrative hiring); and any company relying on commercial ATS platforms with embedded AI scoring features (e.g., Workday, SAP SuccessFactors, iCIMS, Greenhouse).

Vendors of covered AEDT tools also face operational impact: employers seeking compliance expect vendor-provided or vendor-supported audit capabilities, creating a market for certified independent auditors.

### Compliance Costs and Market Response

A market for bias audit services has emerged. Firms including Holistic AI, Warden AI, BABL AI, and others offer LL 144-compliant audit services. The cost of a compliant bias audit ranges widely based on data availability, tool complexity, and auditor. Independent auditors must be formally independent of both employer and vendor per the final rules.

### The Disclosure Gap

A structural compliance challenge — identified both by the FAccT 2024 researchers and the NYC Comptroller's audit — is that the law's self-scoping creates a disclosure gap: employers who simply decide their tools are not "AEDTs" face no obligation and generate no paper trail indicating non-compliance. DCWP cannot proactively identify non-compliant employers because the only visible compliance signal is a published audit — and an employer that has concluded its tool is out of scope will not publish one.

## Emerging National Landscape [MEDIUM confidence]

As of May 2024, NYC Local Law 144 remained the only enacted and enforced mandatory bias audit law for employment AI in the United States, but parallel developments were advancing in multiple jurisdictions:

**Illinois (enacted August 2024):** The Illinois Human Rights Act was amended by [H.B. 3773](https://www.jonesday.com/en/insights/2024/10/illinois-becomes-second-state-to-pass-broad-legislation-on-the-use-of-ai-in-employment-decisions), signed August 9, 2024, effective January 1, 2026. Illinois prohibits use of AI in employment decisions that causes discrimination based on protected characteristics. Unlike NYC LL 144, it does not require bias audits but requires notice to employees that AI is used. It is broader in scope (covering promotion, renewal, training, discipline, and termination, not just initial hiring) but lacks the audit transparency mechanism.

**Colorado (signed May 2024):** [SB 24-205](https://leg.colorado.gov/bills/sb24-205), signed May 17, 2024, covers AI in "consequential decisions" including employment, requires pre-deployment and annual impact assessments, adverse-action notices, and appeals for AI-influenced employment decisions. Effective June 30, 2026. Requires independent assessments but does not require public posting of audit results — a key difference from NYC LL 144.

**Maryland (proposed 2024):** [HB 1255](https://www.multistate.us/insider/2023/6/15/as-artificial-intelligence-proliferates-states-and-localities-enact-laws-regulating-its-use-in-hiring) (February 2024) would restrict automated employment decision tools in hiring to cases where an impact assessment confirms no unlawful discrimination. As of mid-2024, the bill was in proposal stage.

**New Jersey (proposed 2024):** [A3854](https://www.multistate.us/insider/2023/6/15/as-artificial-intelligence-proliferates-states-and-localities-enact-laws-regulating-its-use-in-hiring) (February 2024) substantially mirrors NYC Local Law 144. As of mid-2024, it was in proposal stage.

**Federal (EEOC guidance):** The EEOC's May 2023 [Title VII technical assistance](https://www.eeoc.gov/sites/default/files/2024-04/20240429_What%20is%20the%20EEOCs%20role%20in%20AI.pdf) and April 2024 worker guidance confirmed that existing federal law applies to AI in hiring but did not impose affirmative audit or publication requirements. Note: the Trump administration withdrew this EEOC AI guidance in January 2025.

## Action Items

- **Inventory AEDT use:** Identify all AI-enabled tools used in NYC hiring or promotion decisions. For each tool, obtain a legal assessment of whether it qualifies as an AEDT under the Final Rules' "substantially assist or replace" standard.
- **Commission bias audits immediately:** Any employer currently using a covered AEDT in NYC without a current (within 12 months) independent bias audit is in violation. Commission audits from a qualified independent auditor before next use.
- **Publish audit summaries:** Publish the bias audit summary — including all required metrics (selection rates, impact ratios by sex/race/ethnicity, dataset description) — on the company's public employment/careers website page.
- **Implement candidate notice process:** Establish a documented process to provide 10-business-day advance notice to NYC-based candidates before any AEDT is used in their evaluation. Include the notice in job postings or confirmation emails.
- **Review vendor contracts:** Evaluate whether AI tool vendors provide documentation sufficient to support an independent audit. Negotiate for data access, methodology documentation, and audit cooperation clauses.
- **Track annual renewal deadlines:** Bias audits must be renewed annually. Implement calendar reminders and compliance tracking for each covered tool's audit expiration date.
- **Monitor state legislative activity:** Track Illinois (effective Jan 1, 2026), Colorado (effective June 30, 2026), and pending New Jersey and Maryland bills for overlapping compliance obligations that will require separate program responses.
- **Retain EEOC federal compliance review:** Even where state/local laws do not mandate audits, Title VII disparate impact doctrine applies. Maintain internal disparate impact monitoring for AI hiring tools regardless of jurisdiction.

## Related Reports

- [reports/ai-law/employment-ai/colorado-sb205-employer-ai-employment-2024-05-20.md](colorado-sb205-employer-ai-employment-2024-05-20.md) — Colorado's SB 24-205 employer AI employment obligations, the other landmark US employment AI compliance regime enacted in the same period; shares focus on bias assessment and adverse-action notice requirements for employers.
- [reports/ai-law/state-legislation/colorado-sb205-ai-act-2024-05-20.md](../state-legislation/colorado-sb205-ai-act-2024-05-20.md) — General framework overview of Colorado AI Act (SB 24-205), which directly references NYC LL 144 as a predecessor regulatory model.
- [reports/ai-law/enforcement-actions/massachusetts-ag-ai-advisory-2024-04-22.md](../enforcement-actions/massachusetts-ag-ai-advisory-2024-04-22.md) — Massachusetts AG advisory on AI use in consumer and employment contexts — illustrates state-level enforcement appetite for AI accountability outside of formal statutory regimes.

## Sources

1. [NYC Council Legistar — Int 1894-2020 / Local Law 144 of 2021](https://legistar.council.nyc.gov/LegislationDetail.aspx?ID=4344524&GUID=B051915D-A9AC-451E-81F8-6596032FA3F9) — Official NYC Council legislative record and bill text for Local Law 144
2. [NYC.gov DCWP — Automated Employment Decision Tools (AEDT) Official Page](https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page) — Official DCWP enforcement and compliance page; primary agency guidance
3. [NYC Rules — Automated Employment Decision Tools Final Rule](https://rules.cityofnewyork.us/rule/automated-employment-decision-tools-2/) — Final implementing rules adopted April 6, 2023, effective July 5, 2023
4. [NYC Rules — Automated Employment Decision Tools (Updated)](https://rules.cityofnewyork.us/rule/automated-employment-decision-tools-updated/) — Updated final rule addressing additional compliance questions
5. [DCWP AEDT FAQ (PDF)](https://www.nyc.gov/assets/dca/downloads/pdf/about/DCWP-AEDT-FAQ.pdf) — Official DCWP frequently asked questions covering bias audit, data, notice, and complaints
6. [NY State Comptroller — Enforcement of Local Law 144 Audit Report](https://www.osc.ny.gov/state-agencies/audits/2025/12/02/enforcement-local-law-144-automated-employment-decision-tools) — December 2025 audit of DCWP's LL 144 enforcement effectiveness; source for complaint statistics, DCWP review findings, and 311 misrouting data
7. [ACM FAccT 2024 — "Null Compliance: NYC Local Law 144 and the Challenges of Algorithm Accountability"](https://dl.acm.org/doi/10.1145/3630106.3658998) — Peer-reviewed study of 391 employers' compliance with LL 144; source for compliance rate statistics
8. [arXiv preprint — Null Compliance (full paper)](https://arxiv.org/abs/2406.01399) — Full version of the FAccT 2024 paper with extended methodology and findings
9. [EEOC — "What is the EEOC's Role in AI?" (PDF)](https://www.eeoc.gov/sites/default/files/2024-04/20240429_What%20is%20the%20EEOCs%20role%20in%20AI.pdf) — Official EEOC guidance on AI in employment; April 2024 publication
10. [EEOC — Employment Discrimination and AI for Workers (PDF)](https://www.eeoc.gov/sites/default/files/2024-04/20240429_Employment%20Discrimination%20and%20AI%20for%20Workers.pdf) — EEOC worker-facing AI discrimination guidance, April 2024
11. [Greenberg Traurig — NYC's Law Governing Automated Employment Decision Tools Takes Effect July 5](https://www.gtlaw.com/en/insights/2023/6/nycs-law-governing-automated-employment-decision-tools-takes-effect-july-5) — Law firm analysis of enforcement-start requirements for employers
12. [Gibson Dunn — NYC's Artificial Intelligence Law: Key Takeaways From Newly Released FAQs](https://www.gibsondunn.com/nyc-artificial-intelligence-law-key-takeaways-from-newly-released-faqs/) — Law firm analysis of DCWP FAQ guidance
13. [MultiState — As Artificial Intelligence Proliferates, States and Localities Enact Laws Regulating Its Use in Hiring](https://www.multistate.us/insider/2023/6/15/as-artificial-intelligence-proliferates-states-and-localities-enact-laws-regulating-its-use-in-hiring) — Legislative tracking of Maryland HB 1255 and New Jersey A3854 alongside NYC LL 144
14. [Jones Day — Illinois Becomes Second State to Pass Broad Legislation on the Use of AI in Employment Decisions](https://www.jonesday.com/en/insights/2024/10/illinois-becomes-second-state-to-pass-broad-legislation-on-the-use-of-ai-in-employment-decisions) — Analysis of Illinois HB 3773 as the second major state law in this space
15. [Epstein Becker Green — Taking Stock of New York City's Automated Employment Decision Tools Law](https://www.workforcebulletin.com/taking-stock-of-new-york-citys-automated-employment-decision-tools-law) — Practice-oriented analysis of compliance status and employer obligations
