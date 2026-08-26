---
title: "Washington Federal Court Dismisses Privacy Claims Involving Hospital Website Pixel Tracking"
date: 2024-06-07
jurisdiction: "Washington"
category: "privacy"
development_type: "court-decision"
finding_id: "SCAN-20240607-011"
topic_key: "washington-5d1ca6ad-2024"
topic_type: "enforcement"
first_reported: 2024-06-07
last_updated: 2024-06-07
status_history: []
cluster: "Healthcare Provider Tracking Pixel Litigation (Meta Pixel & HIPAA-Adjacent Claims)"
cluster_slug: "healthcare-tracking-pixel-litigation"
---

# Washington Federal Court Dismisses Privacy Claims Involving Hospital Website Pixel Tracking

**Jurisdiction:** Washington, Federal | **Category:** Privacy | **Date:** 2024-06-07

## Executive Summary [HIGH confidence]

On May 13, 2024, U.S. District Judge Tana Lin of the Western District of Washington dismissed in full a class action complaint in *[Nienaber v. Overlake Hospital Medical Center](https://law.justia.com/cases/federal/district-courts/washington/wawdce/2:2023cv01159/324912/32/)* (Case No. 2:23-cv-01159-TL), granting the hospital's Rule 12(b)(6) motion with leave to amend most claims. Plaintiff Jacq Nienaber alleged that Overlake Hospital installed Facebook Pixel, Meta's Conversions API, and Google Tag Manager on its public website and patient portal, causing her protected health information (PHI) to be shared with Meta and Google without consent. The court found that Nienaber's complaint offered only two sentences describing her actual website activity — supported by hypothetical examples of potential data disclosure — which was insufficient to plausibly allege that any PHI or personally identifiable information (PII) was actually transmitted. Because the threshold pleading failure infected all claims, the court dismissed every cause of action, with the breach of confidence claim dismissed with prejudice (not a recognized cause of action under Washington law) and all others dismissed with leave to amend. The case continued through amended complaints before the plaintiff filed a voluntary dismissal in March 2025.

## Background [HIGH confidence]

### The Rise of Healthcare Pixel Litigation

Beginning around 2022 and accelerating through 2024, plaintiffs' counsel filed hundreds of class actions against healthcare providers for deploying third-party tracking pixels — primarily [Meta Pixel](https://www.facebook.com/business/tools/meta-pixel) and Google Analytics — on websites and patient portals that handle health-related information. These tools embed JavaScript that captures user interactions (pages visited, buttons clicked, form inputs) and transmits data bundles to Facebook, Google, and other advertising platforms. The central allegation in these cases is that when a patient browses a healthcare provider's website or logs into a patient portal, their health-related activity is covertly shared with advertising technology companies in violation of federal wiretapping law, state consumer protection statutes, and common-law privacy doctrines.

The [HHS Office for Civil Rights issued guidance in December 2022](https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/hipaa-online-tracking/index.html) confirming that tracking technologies on HIPAA-regulated entities' websites that capture individually identifiable health information constitute disclosures of PHI requiring authorization. This guidance intensified litigation, though a Texas federal court later held in June 2024 that the HHS guidance exceeded the agency's statutory authority under HIPAA's definition of individually identifiable health information.

### Overlake Hospital and the Complaint

Overlake Hospital Medical Center is a nonprofit healthcare organization headquartered in Bellevue, Washington. Plaintiff Jacq Nienaber is a Washington State resident and patient of Overlake who alleged she used Overlake's public website and private patient portal to search for healthcare information and manage her care.

Nienaber alleged that Overlake deployed three third-party tracking tools: (1) the Facebook Tracking Pixel; (2) Meta's Conversions Application Programming Interface (Conversions API); and (3) Google Tag Manager. She further alleged that "shortly after using Defendant's Website, Plaintiff has seen numerous targeted advertisements on Facebook related to her medical conditions and treatments sought through Overlake" — pointing to this as circumstantial evidence that her health data had been transmitted to Meta.

The complaint asserted eight causes of action: violation of the Electronic Communications Privacy Act (ECPA); violation of the Computer Fraud and Abuse Act (CFAA); intrusion upon seclusion; public disclosure of private facts; negligence; breach of confidence; unjust enrichment; and violation of the Washington Consumer Protection Act (CPA).

## Detailed Analysis [HIGH confidence]

### Threshold Failure: Insufficient Pleading of PHI Disclosure

Judge Lin identified a threshold pleading deficiency that pervaded all claims: the complaint did not plausibly allege that Overlake actually transmitted Nienaber's PHI or PII to any third party. The complaint's description of Nienaber's website activity consisted of just two sentences, and the remaining allegations were hypothetical examples of how patient data *could* be captured and transmitted — not specific facts about what actually occurred.

As the [Duane Morris class action defense blog noted](https://blogs.duanemorris.com/classactiondefense/2024/06/19/district-court-dismisses-data-privacy-class-action-against-health-care-system-for-failure-to-sufficiently-allege-disclosure-of-phi/), the court concluded that "Plaintiff's failure to sufficiently allege PHI was reason alone for dismissal," and that "for adtech plaintiffs to plausibly plead claims for ECPA violations, negligence, or invasion of privacy, they need to identify what allegedly private information was disclosed via the adtech."

The court also found Nienaber failed to plausibly allege that any information disclosed from the patient portal — as opposed to the public website — could be attributed to the tracking tools. This distinction is significant because patient portals, unlike public-facing pages, involve authenticated sessions where users input sensitive health information.

### ECPA Claims: One-Party Consent Exemption

The court dismissed Nienaber's Electronic Communications Privacy Act (ECPA) claim on two grounds. First, adopting the threshold finding, Nienaber failed to allege that any communication disclosing PHI had actually been intercepted. Second, and independently, the ECPA claim was barred by the statute's one-party consent exemption. Under 18 U.S.C. § 2511(2)(d), interception of a communication is not unlawful when one of the parties to the communication consents. Because Overlake, as the owner and operator of its own website, was a party to each communication between itself and Nienaber's browser, it could not be held liable for intercepting communications to which it was already a party. The court reasoned that Overlake consented to its own website's operation, including any tracking tools it chose to deploy.

This ECPA one-party consent holding aligns with decisions from other circuits in the pixel litigation wave. Courts have split on whether the service provider exemption or one-party consent applies to healthcare pixel cases, but the Western District of Washington firmly adopted the consent rationale here.

### CFAA Claims: Unauthorized Access

The Computer Fraud and Abuse Act (CFAA) claim was dismissed because Nienaber could not establish that Overlake exceeded authorized access to her computer. The CFAA prohibits unauthorized access to protected computers. Because the tracking pixels were installed by Overlake on Overlake's own website — which Nienaber voluntarily visited — the court found no basis to conclude that Overlake accessed Nienaber's computer without authorization. The access to her browser that resulted from visiting the website was by definition authorized.

### Invasion of Privacy Claims

The court dismissed both invasion-of-privacy theories. On the intrusion-upon-seclusion theory, the court found that any alleged intrusion was carried out by Meta and Google as third parties, not by Overlake directly. Overlake's role was to install the pixels; the actual data collection and transmission was performed by the third parties. Washington's intrusion tort requires that the defendant commit the intrusion, not merely enable a third party to do so.

On the public disclosure of private facts theory, Nienaber failed to allege that her data was disclosed to "the public at large" — a required element of the tort — or that any disclosure was "highly offensive to a reasonable person."

### Negligence, Unjust Enrichment, and Washington CPA

The negligence claim failed because, even assuming Overlake owed a duty to safeguard patient data, Nienaber did not plausibly allege a breach of that duty. The complaint's hypothetical framing meant there were no specific facts demonstrating that Overlake's deployment of the tracking tools fell below the applicable standard of care.

The unjust enrichment claim was dismissed for failure to allege a concrete detriment to Nienaber. Unjust enrichment requires that the plaintiff suffered some loss corresponding to the defendant's unjust gain; general allegations about data being "worth something" were insufficient without concrete injury.

The Washington Consumer Protection Act (CPA) claim fell because Nienaber failed to adequately allege an injury to her "business or property," which is a required element distinct from personal injury. Data privacy violations, standing alone, do not automatically satisfy this element under Washington law.

### Breach of Confidence: Dismissed with Prejudice

The breach of confidence claim was the only one dismissed with prejudice, as the court held it is not a recognized cause of action under Washington law. Unlike some states (including California), Washington does not recognize an independent tort of breach of confidence, making this theory unavailable regardless of how well the facts were pleaded.

### Leave to Amend and Subsequent Proceedings

All claims except breach of confidence were dismissed with leave to amend. Nienaber filed an amended complaint, and the litigation continued. In March 2025, Judge Lin ruled on the second amended complaint, largely maintaining prior dismissals of ECPA and invasion of privacy claims without leave to amend, while other claims — including negligence, breach of implied contract, unjust enrichment, and Washington CPA claims — were dismissed with leave to amend. The plaintiff ultimately filed a [voluntary dismissal in March 2025](https://www.courtlistener.com/docket/67662188/nienaber-v-overlake-hospital-medical-center/), ending the litigation after approximately 20 months.

## Impact Assessment [HIGH confidence]

### Pleading Standards as a Defense Tool

The Overlake decision reinforces a significant defense-side tool in healthcare pixel litigation: stringent application of the Rule 12(b)(6) plausibility standard to data transmission allegations. Courts in this wave of litigation have increasingly required plaintiffs to plead specific facts about what data was transmitted, to whom, and how — rather than relying on general allegations about how tracking pixels *could* work. This decision demonstrates that anecdotal evidence (seeing targeted ads) combined with general allegations about pixel capabilities is insufficient at the pleading stage.

Healthcare organizations, insurers, and their legal advisors have pointed to the Overlake ruling and similar decisions as evidence that the wave of pixel litigation is not uniformly plaintiff-friendly. [Fisher Phillips has noted](https://www.fisherphillips.com/en/news-insights/court-tosses-most-claims-in-healthcare-pixel-privacy-suit.html) that courts ruling that website visits don't reveal PHI absent specific pleading of what health data was captured represent a meaningful constraint on these class actions.

### ECPA One-Party Consent in Healthcare Context

The ECPA one-party consent ruling has important implications for healthcare providers. It means that a hospital or health system that deploys tracking technology on its own website cannot be held liable under the ECPA for intercepting communications to which it is a party — even if those communications are simultaneously shared with Meta or Google. This is a meaningful procedural barrier for plaintiffs. However, the exemption does not necessarily shield the third-party tracking vendors themselves (Meta, Google) from ECPA liability under a different theory, and it does not address HIPAA compliance obligations, which are regulatory in nature and enforced by HHS OCR, not through private litigation.

### Contrast with Other Jurisdictions

The Overlake dismissal stands in contrast to decisions in other jurisdictions during the same period. In *[Doe v. Tenet Healthcare](https://caselaw.findlaw.com/court/us-dis-crt-d-mas/116091358.html)* (D. Mass., April 2024), Judge Patti Saris allowed seven of nine claims to proceed, including breach of fiduciary duty, breach of implied contract, and the Massachusetts Consumer Protection Act (93A), finding the pleading adequate. The divergence between First and Ninth Circuit district courts on pixel privacy cases reflects unsettled law about both the merits of ECPA claims and the applicable pleading standard for alleging PHI disclosure. [WilmerHale's 2024 Web Tracking Year in Review](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20250225-year-in-review-2024-web-tracking-litigation-and-enforcement) describes this as a "mixed bag" period for healthcare website operators, with outcomes highly dependent on jurisdiction, the specific tracking tools deployed, and how plaintiffs frame their factual allegations.

### Industry Compliance Implications

Despite the dismissal, the Overlake case does not signal that healthcare providers may freely deploy tracking pixels. HIPAA's regulatory framework remains fully operative, and HHS OCR continues to investigate and take enforcement action against healthcare providers for impermissible disclosures of PHI via tracking technologies. The case's outcome was driven by pleading deficiencies, not by a ruling that the conduct was lawful. Healthcare organizations should:

- Conduct audits of tracking technologies deployed on public websites, patient portals, and mobile applications
- Assess whether any tracking tools capture user-entered health information or information that, combined with a healthcare provider's domain, could constitute PHI
- Evaluate consent mechanisms and privacy notice accuracy
- Monitor OCR enforcement activity in this area, which operates independently of private litigation outcomes

## Action Items

- Audit all third-party tracking scripts (pixels, tag managers, analytics tools) deployed on public-facing and authenticated healthcare websites; confirm whether they capture health-related search terms, page visits, or form inputs that could constitute PHI under HIPAA
- Review existing privacy notices and terms of service to ensure accurate disclosure of any data sharing with advertising platforms; inaccurate notices may support breach of contract or CPA claims even when ECPA claims fail
- Assess whether patient portal environments are technically isolated from third-party advertising tags; courts have given separate consideration to patient-portal tracking as involving more sensitive authenticated health data
- Monitor the broader healthcare pixel litigation landscape; the voluntary dismissal in *Nienaber* should not be read as resolution of the legal questions raised — similar claims continue in other districts with varying outcomes
- Consult with privacy counsel before deploying or retaining analytics tools from Meta, Google, or similar platforms on any healthcare-related digital property, particularly in light of continuing HHS OCR enforcement activity

## Related Reports

- [reports/privacy/litigation/massachusetts-doe-v-tenet-healthcare-pixel-tracking-2024-05-20.md](../litigation/massachusetts-doe-v-tenet-healthcare-pixel-tracking-2024-05-20.md) — Direct counterpart case decided six weeks earlier in the District of Massachusetts, where tracking pixel claims survived dismissal on stronger pleading, highlighting inter-circuit divergence in healthcare pixel litigation outcomes.
- [reports/privacy/litigation/arizona-tucsr-spy-pixel-class-action-2024-05-30.md](../litigation/arizona-tucsr-spy-pixel-class-action-2024-05-30.md) — Related pixel-based class action against a hospital system in Arizona, providing additional comparative context for how tracking pixel claims are pleaded and litigated across different courts.

## Sources

1. [Nienaber v. Overlake Hospital Medical Center, No. 2:2023cv01159, Document 32 (W.D. Wash. 2024) — Justia](https://law.justia.com/cases/federal/district-courts/washington/wawdce/2:2023cv01159/324912/32/) — Primary court order granting the first motion to dismiss, dated May 13, 2024
2. [Nienaber v. Overlake Hospital Medical Center — FindLaw Case Text](https://caselaw.findlaw.com/court/us-dis-crt-w-d-was-at-sea/116173924.html) — Published case text for the 2024 dismissal ruling
3. [Nienaber v. Overlake Hospital Medical Center — Docket, Justia](https://dockets.justia.com/docket/washington/wawdce/2:2023cv01159/324912) — Full case docket showing procedural history from filing through voluntary dismissal
4. [Nienaber v. Overlake Hospital Medical Center — CourtListener Docket](https://www.courtlistener.com/docket/67662188/nienaber-v-overlake-hospital-medical-center/) — Docket and filings including the March 2025 voluntary dismissal
5. [Washington Federal Court Dismisses Privacy Claims Involving Hospital Website — Inside Class Actions](https://www.insideclassactions.com/2024/06/04/washington-federal-court-dismisses-privacy-claims-involving-hospital-website/) — Law firm analysis summarizing the May 2024 ruling and its grounds
6. [Washington Federal Court Dismisses Privacy Claims Involving Hospital Website — Lexology / Covington & Burling](https://www.lexology.com/library/detail.aspx?g=bd2d6a98-3227-415e-ae13-d613c2860bbf) — Covington & Burling client alert summarizing the dismissal
7. [District Court Dismisses Data Privacy Class Action Against Health Care System For Failure To Sufficiently Allege Disclosure of PHI — Duane Morris Class Action Defense Blog](https://blogs.duanemorris.com/classactiondefense/2024/06/19/district-court-dismisses-data-privacy-class-action-against-health-care-system-for-failure-to-sufficiently-allege-disclosure-of-phi/) — In-depth analysis of PHI pleading standard and implications for future pixel litigation
8. [Court Tosses Most Claims in Healthcare Pixel Privacy Suit — Fisher Phillips LLP](https://www.fisherphillips.com/en/news-insights/court-tosses-most-claims-in-healthcare-pixel-privacy-suit.html) — Employer-focused law firm analysis on what the ruling means for healthcare website operators
9. [Order on Motion to Dismiss Second Amended Class Action Complaint — Horty Springer (PDF)](https://www.hortyspringer.com/wp-content/uploads/2025/03/Nienaber-v.-Overlake-Hospital-Medical-Center.pdf) — Official court order on the second amended complaint, March 2025, showing claims dismissed with and without leave to amend
10. [Year in Review: 2024 Web Tracking Litigation and Enforcement — WilmerHale](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20250225-year-in-review-2024-web-tracking-litigation-and-enforcement) — Comprehensive review of 2024 healthcare and other pixel tracking litigation trends across jurisdictions
11. [Overlake Hospital Beats Suit Over Data Sharing With Meta, Google — Bloomberg Law](https://news.bloomberglaw.com/litigation/overlake-hospital-beats-suit-over-data-sharing-with-meta-google) — News coverage of the May 2024 dismissal ruling
12. [Nienaber v. Overlake Hospital Medical Center — Original Complaint (ClassAction.org PDF)](https://www.classaction.org/media/nienaber-v-overlake-hospital-medical-center.pdf) — Filed class action complaint providing factual allegations and claims as originally pleaded
