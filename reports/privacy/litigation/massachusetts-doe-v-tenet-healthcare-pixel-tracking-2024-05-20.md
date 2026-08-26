---
title: "Healthcare Provider Beware: Massachusetts Federal Court Largely Permits Tracking Technology and Wiretapping Claims to Proceed in Doe v. Tenet Healthcare"
date: 2024-05-20
jurisdiction: "Massachusetts"
category: "privacy"
development_type: "court-decision"
finding_id: "SCAN-20240520-003"
topic_key: "massachusetts-32112c77-2024"
topic_type: "enforcement"
first_reported: 2024-05-20
last_updated: 2024-05-20
status_history: []
cluster: "Healthcare Provider Tracking Pixel Litigation (Meta Pixel & HIPAA-Adjacent Claims)"
cluster_slug: "healthcare-tracking-pixel-litigation"
---

# Healthcare Provider Beware: Massachusetts Federal Court Largely Permits Tracking Technology and Wiretapping Claims to Proceed in Doe v. Tenet Healthcare

**Jurisdiction:** Massachusetts, Federal | **Category:** Privacy | **Date:** 2024-05-20

## Executive Summary [HIGH confidence]

On April 23, 2024, U.S. District Judge Patti B. Saris of the District of Massachusetts issued a significant ruling in *[Jane Doe v. Tenet Healthcare Corporation](https://caselaw.findlaw.com/court/us-dis-crt-d-mas/116091358.html)* (Civil Action No. 1:23-cv-12978-PBS), allowing seven of nine privacy-related claims to proceed against a hospital operator that deployed Meta Pixel and other third-party tracking technologies on its patient-facing website. Only two claims — negligence per se and invasion of privacy — were dismissed as unrecognized causes of action under Massachusetts law. The surviving claims include negligence, breach of implied contract, unjust enrichment, breach of fiduciary duty, the Massachusetts Right to Privacy Law (M.G.L. c. 214, § 1B), the Massachusetts Consumer Protection Act (M.G.L. c. 93A), and the Massachusetts Wiretap Act (M.G.L. c. 272, § 99) — the last of which was preserved pending a ruling from the Massachusetts Supreme Judicial Court (SJC). The decision is a significant warning for healthcare providers using analytics tools: courts in the First Circuit are receptive to a wide spectrum of state-law theories targeting digital tracking of patient health information, even absent a HIPAA private right of action.

## Background [HIGH confidence]

### The Rise of Pixel Litigation in Healthcare

Between 2022 and 2024, plaintiffs' counsel filed hundreds of class actions against healthcare providers for deploying third-party tracking pixels — chiefly [Meta Pixel](https://www.facebook.com/business/tools/meta-pixel) and Google Analytics — on websites that collect or display patient health information. These tools embed JavaScript code that captures user interactions (pages visited, buttons clicked, form inputs) and transmits data bundles to Facebook, Google, and other third-party advertising platforms.

The regulatory backdrop intensified pressure. On December 1, 2022, HHS Office for Civil Rights (OCR) issued a [Bulletin on Online Tracking Technologies](https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/hipaa-online-tracking/index.html), asserting that many deployments of third-party trackers on authenticated patient portals and certain unauthenticated pages triggered HIPAA obligations. OCR followed by sending letters to approximately 130 hospital systems and telehealth providers urging compliance review. While HIPAA has no private right of action, the bulletin accelerated the filing of state-law class actions premised on tracking practices that OCR had labeled non-compliant.

HHS updated its bulletin on March 18, 2024, but that guidance was subsequently challenged. On June 20, 2024, the U.S. District Court for the Northern District of Texas [vacated key portions](https://www.nixonpeabody.com/insights/alerts/2024/07/03/portions-of-ocrs-bulletin-on-online-tracking-technologies-deemed-unlawful) of the bulletin in *American Hospital Association v. Becerra*, finding that HHS exceeded its statutory authority by treating an IP address combined with a visit to certain unauthenticated public webpages as HIPAA-protected individually identifiable health information. OCR subsequently withdrew its appeal. The April 2024 *Doe v. Tenet* ruling predates this vacatur, but is notable precisely because it demonstrates that state-law claims can proceed independent of the HIPAA regulatory framework.

### The Massachusetts Wiretap Act

The Massachusetts Wiretap Act, [M.G.L. c. 272, § 99](https://malegislature.gov/laws/generallaws/partiv/titlei/chapter272/section99), was enacted in 1968 to criminalize the interception of wire and oral communications, particularly telephone wiretapping. Section 99(C)(1) makes it a crime to "willfully commit an interception" of a "wire communication" or "oral communication." The statute provides a private right of action, which plaintiffs have deployed to challenge website analytics tools as unlawful interceptions of their online communications. Unlike California's two-party consent wiretapping law ([Cal. Penal Code § 631](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=631.&lawCode=PEN)), the Massachusetts statute's application to web browsing remained unsettled as of the *Doe v. Tenet* ruling, with the central question pending before the SJC in *Vita v. New England Baptist Hospital*.

### Tenet Healthcare and MetroWest Medical Center

Tenet Healthcare Corporation is a for-profit hospital chain. Its Massachusetts-based subsidiary operates MetroWest Medical Center in Framingham, Massachusetts. The plaintiff, a Framingham resident and patient, alleged that Tenet's patient-facing website deployed Meta Pixel and other tracking scripts that captured and transmitted to Facebook information including: her identity, patient status, health conditions, requested treatments, appointment time, and location. This data was then used to optimize Facebook advertising targeting — including health-related ads directed back at the plaintiff.

## Detailed Analysis [HIGH confidence]

### Case Overview and Procedural History

The complaint, filed in late 2023, asserted nine causes of action. Tenet moved to dismiss all counts. [Judge Saris's April 23, 2024 opinion](https://scholar.google.com/scholar_case?case=15238052607098824653) granted the motion as to two counts and denied it as to seven:

| Count | Claim | Outcome |
|-------|-------|---------|
| I | Negligence | Survived |
| II | Negligence per se | Dismissed — not a recognized independent claim under Massachusetts law |
| III | Invasion of privacy (common law) | Dismissed — not a recognized tort under Massachusetts law |
| IV | Breach of Implied Contract | Survived |
| V | Unjust Enrichment | Survived |
| VI | Breach of Fiduciary Duty | Survived |
| VII | Massachusetts Right to Privacy (M.G.L. c. 214, § 1B) | Survived |
| VIII | Massachusetts Consumer Protection Act (M.G.L. c. 93A) | Survived |
| IX | Massachusetts Wiretap Act (M.G.L. c. 272, § 99) | Survived (denied without prejudice, pending SJC ruling in *Vita*) |

### Negligence (Count I)

The court found the plaintiff had adequately pled a duty of care, breach, causation, and damages. Healthcare providers owe patients a duty of care in handling their medical information. The allegation that Tenet knowingly deployed a tracking pixel that transmitted health-related data to Facebook without patient consent plausibly stated a breach of that duty. The court found that whether the plaintiff suffered cognizable damages — particularly reputational harm or loss of privacy — presented a factual question not resolvable on a motion to dismiss.

### Breach of Implied Contract (Count IV)

The plaintiff alleged that Tenet's privacy notices and patient intake materials created an implied promise to maintain the confidentiality of patient health information. The court agreed that these representations — combined with the common understanding in the patient-provider relationship that sensitive health information will not be shared with advertisers — could constitute an implied contractual term. The alleged disclosure to Facebook breached that implied term.

### Breach of Fiduciary Duty (Count VI)

This count is particularly significant. The court acknowledged that under Massachusetts law, a fiduciary relationship exists between a healthcare provider and a patient. Fiduciaries owe duties of loyalty and confidentiality to their beneficiaries. The court found that the plaintiff stated a plausible claim that Tenet breached its fiduciary duty of confidentiality by intentionally sharing patient information with Facebook for Tenet's own commercial benefit (improved advertising targeting) without patient consent or knowledge.

### Massachusetts Right to Privacy (Count VII) — M.G.L. c. 214, § 1B

[Section 1B](https://malegislature.gov/Laws/GeneralLaws/PartIII/TitleI/Chapter214/Section1b) provides: "A person shall have a right against unreasonable, substantial or serious interference with his privacy." The court found that the alleged disclosure of highly personal healthcare information — including health conditions and treatment details — to a social media company for advertising purposes plausibly constituted an unreasonable, substantial, or serious interference with privacy. Whether the interference met the statutory threshold presented a factual question.

### Massachusetts Consumer Protection Act (Count VIII) — M.G.L. c. 93A

[Chapter 93A](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXV/Chapter93A/Section2) prohibits unfair or deceptive acts in trade or commerce. The court found that disclosing patient health information to Facebook in a manner allegedly inconsistent with Tenet's own privacy notices and patients' reasonable expectations could constitute a deceptive practice. Chapter 93A is significant because it allows for double or treble damages and attorney's fees for willful violations — making it a potent vehicle for class litigation.

### Massachusetts Wiretap Act (Count IX) — M.G.L. c. 272, § 99

Rather than ruling on the merits of the wiretap claim, Judge Saris deferred and denied Tenet's motion without prejudice, because the identical legal question — whether the Massachusetts Wiretap Act applies to the interception of website browsing data by third-party analytics tools — was then pending before the SJC in *Vita v. New England Baptist Hospital*. The court determined it would be inappropriate to resolve a novel question of state statutory interpretation while the state's highest court was actively considering the same issue.

### The SJC's Subsequent Resolution in *Vita v. New England Baptist Hospital*

The SJC's decision in [*Vita v. New England Baptist Hospital*](https://law.justia.com/cases/massachusetts/supreme-court/2024/sjc-13542.html) (SJC-13542), issued on October 24, 2024, substantially altered the wiretap landscape that *Doe v. Tenet* left open. In a 5-1 decision, the SJC ruled that the Massachusetts Wiretap Act does not apply to the interception of website browsing activities by third-party tracking tools.

The SJC grounded its reasoning in the rule of lenity: because the term "communication" in the 1968 statute is ambiguous with respect to web browsing interactions — the Legislature could not have anticipated the internet — any ambiguity must be resolved in favor of the defendants. The court stated: "If the Legislature intends for the wiretap act's criminal and civil penalties to prohibit the tracking of a person's browsing of, and interaction with, published information on websites, it must say so expressly."

The dissenting justice argued that the hospitals' privacy disclosures were misleading and that the legislature intended the statute to protect against evolving surveillance techniques. The *Vita* ruling directly affects the viability of Count IX in *Doe v. Tenet*: following the SJC's decision, the Wiretap Act claim will be vulnerable to renewed dismissal in the district court.

## Impact Assessment [MEDIUM confidence]

### Implications for Healthcare Providers

The *Doe v. Tenet* ruling confirms that healthcare providers face substantial exposure under Massachusetts state law for deploying third-party tracking technologies on patient-facing websites, even where HIPAA offers no private right of action. The survival of claims grounded in:
- Common law negligence
- Implied contract
- Fiduciary duty
- Statutory consumer protection (M.G.L. c. 93A)
- Statutory privacy (M.G.L. c. 214, § 1B)

...creates a multi-vector litigation risk that is difficult to eliminate through technical compliance measures alone. The fiduciary duty theory is particularly notable because it is grounded in the inherent nature of the patient-provider relationship, not in any contractual provision or regulatory standard.

### The Narrowing of Wiretap Exposure

The subsequent *Vita* decision substantially limits the wiretap avenue for future plaintiffs in Massachusetts. Third-party trackers on public, unauthenticated webpages are now clearly outside the scope of M.G.L. c. 272, § 99 under the SJC's ruling. This is a meaningful defense victory, though [commentators at the Boston Bar Association](https://bostonbar.org/journal/slc-web-tracking-does-not-violate-wiretap-act-but-businesses-may-not-be-totally-in-the-clear/) have noted that the *Vita* court may have left open claims involving authenticated patient portals where communications are more clearly person-to-person in character.

### Contrast with Other Jurisdictions

Massachusetts now sits at an interesting crossroads. Its state wiretap law has been narrowed for website tracking purposes, but its common law and consumer protection frameworks remain robust plaintiff-side tools in the healthcare context. California presents the opposite dynamic: CIPA (Cal. Penal Code § 631) has been applied inconsistently to website tracking tools in different federal district courts, [with some courts dismissing those claims](https://www.insideclassactions.com/2024/11/12/massachusetts-supreme-judicial-court-holds-that-third-party-technologies-relating-to-web-browsing-do-not-violate-massachusetts-wiretap-act/) and others allowing them to proceed.

### Scope of Potential Class

The complaint seeks class certification. If the remaining claims survive, the potential class could include all patients who visited Tenet's Massachusetts websites while the Meta Pixel was operational — potentially tens or hundreds of thousands of individuals. Chapter 93A's treble damages and attorney's fees provisions make a certified class extremely costly.

### HHS OCR Regulatory Context

While the *Doe v. Tenet* ruling is independent of HIPAA, the broader HHS OCR tracking technology bulletin — now partially vacated — continues to shape how healthcare providers configure website analytics. The 2024 Texas district court ruling vacating the "proscribed combination" portion of the OCR bulletin provides some regulatory relief, particularly for unauthenticated public pages. But OCR's position on authenticated pages (patient portals, online scheduling forms) remains in force. Healthcare providers operating in Massachusetts face both state-court private litigation risk and continued OCR enforcement exposure for authenticated-page tracking.

## Action Items

- Conduct an immediate audit of all first-party and third-party tracking scripts deployed on patient-facing websites, distinguishing between authenticated patient portal pages and unauthenticated public pages.
- Remove or disable Meta Pixel, Google Analytics, and similar advertising-oriented trackers from any page where patients can submit health information, access medical records, or schedule appointments, unless robust consent mechanisms compliant with HIPAA and state privacy law are implemented.
- Review all patient-facing privacy notices and website terms of service to ensure they accurately describe any third-party data sharing — any gap between stated policy and actual practice heightens Chapter 93A exposure.
- Evaluate the scope of past pixel deployment to assess potential litigation exposure, including whether a HIPAA breach notification analysis is warranted for any period when protected health information may have been transmitted to third parties.
- Work with legal counsel to assess whether the *Vita* ruling reduces exposure specifically on Wiretap Act theories, and what effect it has on any pending litigation or demand letters received.
- Monitor the *Doe v. Tenet* docket for any post-*Vita* ruling on Count IX, and for updates on class certification proceedings — those proceedings will further define the litigation landscape for Massachusetts healthcare operators.
- Consider healthcare-specific analytics platforms (e.g., those with HIPAA Business Associate Agreements) as replacements for advertising-linked tracking tools.

## Related Reports

- [reports/privacy/litigation/california-cipa-chat-wiretapping-garcia-v-buildcom-2024-04-17.md](reports/privacy/litigation/california-cipa-chat-wiretapping-garcia-v-buildcom-2024-04-17.md) -- Parallel wiretap class action litigation under California's CIPA arising from website tracking tools, illustrating the national scope of the pixel tracking litigation wave.
- [reports/privacy/hhs-ocr-hipaa-risk-management-video-2026-04-12.md](reports/privacy/hhs-ocr-hipaa-risk-management-video-2026-04-12.md) -- HHS OCR HIPAA enforcement guidance directly relevant to the regulatory framework surrounding healthcare provider data handling obligations.
- [reports/privacy/enforcement-actions/massachusetts-sjc-meta-minors-2026-04-13.md](reports/privacy/enforcement-actions/massachusetts-sjc-meta-minors-2026-04-13.md) -- Massachusetts SJC ruling on Meta's liability for design features, demonstrating the Massachusetts courts' willingness to allow state-law privacy claims against technology companies to proceed.

## Sources

1. [Jane Doe v. Tenet Healthcare Corp., No. 1:23-cv-12978-PBS (D. Mass. Apr. 23, 2024) — FindLaw](https://caselaw.findlaw.com/court/us-dis-crt-d-mas/116091358.html) -- Official case text of the April 23, 2024 district court ruling, including all nine counts and the court's disposition
2. [Doe v. Tenet Healthcare Corp. — Google Scholar](https://scholar.google.com/scholar_case?case=15238052607098824653) -- Full text of the district court opinion
3. [USCOURTS-mad-1_23-cv-12978 — GovInfo](https://www.govinfo.gov/app/details/USCOURTS-mad-1_23-cv-12978) -- Official federal court docket entry via GovInfo
4. [Doe v. Tenet Healthcare Corporation — Justia Docket](https://dockets.justia.com/docket/massachusetts/madce/1:2023cv12978/264409) -- Complete case docket
5. [Healthcare Provider Beware: Massachusetts Federal Court Largely Permits Tracking Technologies and Wiretapping Claims To Proceed — Mintz (May 16, 2024)](https://www.mintz.com/insights-center/viewpoints/2166/2024-05-16-healthcare-provider-beware-massachusetts-federal-court) -- Primary law firm analysis from Mintz (the finding's source), covering all surviving claims and their significance for healthcare providers
6. [Healthcare Provider Beware — National Law Review](https://natlawreview.com/article/healthcare-provider-beware-massachusetts-federal-court-largely-permits-tracking) -- Republication of Mintz analysis, providing additional context on the First Circuit privacy litigation environment
7. [Vita v. New England Baptist Hospital, SJC-13542 (Mass. Oct. 24, 2024) — Justia](https://law.justia.com/cases/massachusetts/supreme-court/2024/sjc-13542.html) -- Full text of the SJC decision resolving the wiretap question left open in *Doe v. Tenet*
8. [Massachusetts Supreme Court Narrows Scope of State's Wiretapping Law — WilmerHale (Nov. 5, 2024)](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20241105-massachusetts-supreme-court-narrows-scope-of-states-wiretapping-law) -- Law firm analysis of the *Vita* ruling and its effect on website wiretap litigation
9. [Massachusetts General Laws c. 272, § 99 — Massachusetts Legislature](https://malegislature.gov/laws/generallaws/partiv/titlei/chapter272/section99) -- Official text of the Massachusetts Wiretap Act
10. [Massachusetts General Laws c. 214, § 1B — Massachusetts Legislature](https://malegislature.gov/Laws/GeneralLaws/PartIII/TitleI/Chapter214/Section1b) -- Official text of the Massachusetts Right to Privacy statute
11. [HHS OCR Bulletin: Use of Online Tracking Technologies by HIPAA Covered Entities](https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/hipaa-online-tracking/index.html) -- Official HHS OCR guidance on HIPAA obligations triggered by third-party tracking tools, providing regulatory backdrop for the litigation
12. [Portions of OCR's Bulletin on Online Tracking Technologies Deemed Unlawful — Nixon Peabody (July 3, 2024)](https://www.nixonpeabody.com/insights/alerts/2024/07/03/portions-of-ocrs-bulletin-on-online-tracking-technologies-deemed-unlawful) -- Analysis of the Texas court's vacatur of key OCR bulletin provisions, relevant to regulatory risk assessment
13. [Federal Courts in the First Circuit Continue to Grapple with Privacy Class Action Claims — National Law Review](https://natlawreview.com/article/federal-courts-first-circuit-continue-grapple-privacy-class-action-claims) -- Survey of First Circuit pixel and wiretap litigation trends providing comparative context for *Doe v. Tenet*
14. [Patient Advances Tenet Lawsuit Over Info Sharing with Facebook — Bloomberg Law](https://news.bloomberglaw.com/litigation/patient-advances-tenet-lawsuit-over-info-sharing-with-facebook) -- News coverage of the district court ruling
15. [Web Tracking Does Not Violate Wiretap Act, But Businesses May Not Be Totally in the Clear — Boston Bar Association](https://bostonbar.org/journal/slc-web-tracking-does-not-violate-wiretap-act-but-businesses-may-not-be-totally-in-the-clear/) -- Nuanced analysis of open questions remaining after *Vita*, including potential exposure for authenticated patient portal interactions
