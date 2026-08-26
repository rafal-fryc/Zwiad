---
title: "Washington State Court Issues First-of-Its-Kind Ruling Excluding AI-Enhanced Video Evidence (State v. Puloka)"
date: 2024-06-10
jurisdiction: "Washington"
category: "privacy"
development_type: "court-decision"
finding_id: "SCAN-20240610-010"
topic_key: "washington-7b03183d-2024"
topic_type: "enforcement"
first_reported: 2024-06-10
last_updated: 2026-04-15
status_history: []
cluster: "AI-Enhanced Evidence Admissibility: State v. Puloka and Frye/Daubert Standards"
cluster_slug: "ai-enhanced-evidence-admissibility-litigation"
---

# Washington State Court Issues First-of-Its-Kind Ruling Excluding AI-Enhanced Video Evidence (State v. Puloka)

**Jurisdiction:** Washington | **Category:** Privacy / Litigation | **Date:** June 2024

> **Note on source summary:** The scanner finding summary described this ruling as holding that "AI-generated images were admissible as evidence subject to authentication." This characterization is inaccurate. The ruling in *State v. Puloka* **excluded** AI-enhanced video evidence. The error appears to originate from a misreading of the Duane Morris article. The report below reflects the verified record from the court decision and multiple independent legal analyses.

## Executive Summary [HIGH confidence]

In March 2024, a King County Superior Court judge in *State of Washington v. Puloka*, No. 21-1-04851-2, excluded AI-enhanced video evidence in what legal experts widely describe as the first-of-its-kind evidentiary ruling on AI-generated content in a United States criminal trial. The defense had sought to introduce a version of a shooting video that had been processed through Topaz Labs AI Video enhancement software to improve resolution and clarity. Applying Washington's Frye admissibility standard, the court held that AI video enhancement tools have not achieved general acceptance in the relevant scientific community — identified as the forensic video analysis community — and that the technology's opacity posed unacceptable risks of jury confusion. The ruling establishes a significant benchmark for how courts may scrutinize AI-enhanced or AI-generated evidence, and signals that proponents will face a substantial burden before such evidence clears Frye or Daubert hurdles.

## Background [HIGH confidence]

### The Underlying Case

The State of Washington charged Joshua Puloka with three counts of murder arising from a 2021 shooting captured on a bystander's smartphone. The unaltered, 10-second source video had already been admitted into evidence by both parties. The defense sought to additionally admit an AI-enhanced version of that same footage to improve its legibility for the jury.

### Washington's Evidentiary Framework

Washington state courts apply the [Frye standard](https://www.expertinstitute.com/resources/insights/washington-expert-witness-admissibility-rules/), derived from *Frye v. United States*, 293 F. 1013 (D.C. Cir. 1923), rather than the federal Daubert standard used in federal courts and a majority of other states. Under Frye, evidence derived from a novel scientific method is admissible only if that method has gained "general acceptance" in the relevant scientific community. The proponent of novel scientific evidence bears the burden of establishing this acceptance. Washington's evidentiary framework is codified in the [Washington Rules of Evidence](https://www.courts.wa.gov/court_rules/?fa=court_rules.list&group=ga&set=ER), including [ER 702](https://www.courts.wa.gov/court_rules/?fa=court_rules.display&group=ga&set=er&ruleid=gaer0702) (expert testimony) and [ER 403](https://www.courts.wa.gov/court_rules/?fa=court_rules.display&group=ga&set=ER&ruleid=gaer0403) (exclusion of relevant evidence on grounds of prejudice or confusion).

The Frye standard's community-acceptance gatekeeping function is distinct from the judge-centered reliability inquiry under Daubert. In Frye jurisdictions, if the scientific community endorses a methodology, courts must generally admit evidence derived from it; if the community has not accepted the methodology, courts must exclude it regardless of the trial judge's independent assessment of reliability.

## Detailed Analysis [HIGH confidence]

### The Frye Hearing

On March 29, 2024, the court conducted a Frye hearing to determine whether the AI-enhanced video met Washington's admissibility standards. The defense expert testified that he had used [Topaz Labs AI Video](https://www.topazlabs.com/topaz-video-ai) — a commercially available machine-learning enhancement tool widely used in the cinematography and film industry — to increase the video's resolution, sharpen edges, reduce motion blur, and add clarity to indistinct features.

The state's expert countered with several technical objections. The AI enhancement software had multiplied the original pixel count by a factor of sixteen. More critically, the algorithm's process was opaque: the underlying model could not be peer-reviewed or independently replicated by forensic video analysts using standard methods. Traditional video enhancement techniques — such as "nearest neighbor," "bi-cubic," and "bi-linear" interpolation — can be reproduced by other practitioners and are understood within the forensic community. Topaz AI, by contrast, draws on training data and learned weights to "hallucinate" pixels that were never in the original footage, representing what the model "thinks" should be there rather than what was actually captured.

The state's expert also cited a warning from a relevant scientific working group that machine learning techniques "can be challenging to identify what process[es] were applied to the imagery and replicate those steps with accuracy."

### The Court's Conclusions of Law

The court ruled against admitting both the AI-enhanced video and the expert witness testimony supporting it. Its analysis proceeded on multiple grounds, each independently fatal to the defense proffer. The [official court ruling](https://www.nacdl.org/getattachment/89dee8b2-c47d-49c0-89d4-e187efe76551/Washington-v-Puloka-(No-21-1-04851-2-KNT)-(Sup-Ct-WA-2024).pdf?lang=en-US) (available via NACDL) contains the full findings of fact and conclusions of law.

**Frye / ER 702 — General Acceptance Not Established.** The court held that the use of AI tools to enhance video in a criminal trial is a "novel technique." Because the technique was novel, the defendant bore the burden of showing general acceptance in the relevant scientific community. The court identified the "forensic video analysis community" — not the broader cinematography or film industry — as the relevant community for this analysis. Topaz Video AI enhancement tools had not been peer-reviewed by that community, were not reproducible by practitioners in that community, and were not generally accepted within it. The defense therefore failed to meet its burden under the Frye standard and ER 702.

**ER 403 — Risk of Misleading the Jury.** Independently, the court found that the probative value of the AI-enhanced video was substantially outweighed by the risk of unfair prejudice, confusion, and waste of time under ER 403. The enhanced video did not capture with integrity what actually happened; instead, it used opaque methods to represent what the AI model believed should be shown. Admitting it risked creating "a time-consuming trial within a trial" focused on the non-peer-reviewed, non-reproducible process the AI model employed.

**No Integrity Guarantee.** A central concern was that AI-enhanced imagery cannot be treated as a faithful magnification of original footage. Unlike optical zoom or traditional interpolation, machine-learning video enhancement introduces a probabilistic inference layer: pixels are synthesized based on what the model was trained to expect, not drawn directly from source data. The court found this distinction legally and factually dispositive.

### The Frye vs. Daubert Divide

The Puloka ruling is particularly significant in the context of the broader national divide between evidentiary standards. Federal courts and approximately 30 states apply the [Daubert standard](https://www.law.cornell.edu/wex/daubert_standard), under which the trial judge independently evaluates reliability factors (testability, error rates, peer review, general acceptance). In Daubert jurisdictions, the outcome in a case like Puloka would not be predetermined by community acceptance alone — a judge could theoretically admit AI-enhanced evidence if satisfied it was reliable even absent forensic community endorsement.

Washington's continued application of [Frye](https://www.law.cornell.edu/wex/frye_standard) means that AI proponents in Washington must specifically win acceptance within the forensic video analysis community, not merely demonstrate commercial use or general technical reliability. This creates a heightened and more community-specific standard compared to many other jurisdictions.

### Implications for AI Evidence Broadly

The Puloka ruling signals broader judicial skepticism toward AI-generated or AI-enhanced content. As the [American Bar Association](https://www.americanbar.org/groups/litigation/resources/litigation-news/2024/fall/court-excludes-aienhanced-videos-trial-evidence/) analysis notes, the case shows how courts may impose an "unduly onerous burden of proof" on AI-generated evidence by applying multiple evidentiary hurdles simultaneously. Without a uniform standard governing AI-generated evidence, courts must improvise on an ad hoc basis, creating risk of inconsistent outcomes across jurisdictions.

The [Greenberg Traurig analysis](https://www.gtlaw.com/en/insights/2024/5/washington-court-rejects-novel-use-of-ai-enhanced-video-in-trial) observes that the Puloka court's reasoning — emphasizing opaqueness, lack of peer review, and non-reproducibility — may well apply beyond video enhancement to other categories of AI-generated content: synthetic images, AI-generated audio, generative AI text outputs, and predictive analytics. Any AI tool that cannot be independently replicated or peer-reviewed within the relevant scientific community faces a substantial Frye obstacle in Washington.

The [Center for Democracy and Technology](https://cdt.org/insights/inadmissible-ai-evidence-in-court/) has further noted that AI-generated evidence raising authenticity concerns implicates both the admissibility inquiry and the jury's ability to evaluate credibility — concerns that the Puloka court's ER 403 analysis addresses directly.

## Impact Assessment [MEDIUM confidence]

### Criminal Defense and Prosecution

Defense counsel in Washington state who seek to use AI-enhanced or AI-generated visual evidence now face a two-part burden: (1) establishing general acceptance of the AI methodology in the relevant forensic scientific community under the Frye standard, and (2) demonstrating that probative value outweighs prejudice under ER 403. The same burden applies to the prosecution. Attorneys presenting AI-enhanced surveillance footage, AI-reconstructed crime scenes, or AI-generated demonstratives must anticipate Frye challenges and prepare expert witnesses who can speak to community acceptance within forensic — not commercial — contexts.

### Civil Litigation

While Puloka arose in a criminal context, Washington's Frye standard applies in civil proceedings as well. Parties relying on AI-enhanced images, AI-reconstructed accident scenes, or AI-generated medical visualizations in Washington civil litigation should expect analogous challenges. The forensic community acceptance requirement will differ by context (e.g., accident reconstruction, forensic engineering), but the analytical framework transfers.

### Technology Vendors

Providers of AI video enhancement and generative imaging tools who seek legal or forensic applications face a gap between their commercial ecosystems and the forensic video analysis community. [Topaz Labs AI Video](https://www.topazlabs.com/topaz-video-ai) is widely used in post-production but has not undergone the peer-review process required by the forensic community. Vendors seeking to establish their tools' admissibility in Frye jurisdictions should invest in peer review through recognized forensic scientific bodies and publication in forensic science journals.

### Other Jurisdictions

Daubert states retain flexibility to admit AI-enhanced evidence on a case-by-case reliability inquiry, but the Puloka reasoning — particularly regarding opacity, non-reproducibility, and the risk of jury confusion — may be persuasive even in Daubert jurisdictions. The National Law Review [notes](https://natlawreview.com/article/washington-court-rejects-novel-use-ai-enhanced-video-trial) that courts nationwide will likely continue to err on the side of exclusion until more information is available about AI model inputs and methods. As the [Quinn Emanuel analysis](https://www.quinnemanuel.com/the-firm/publications/adapting-the-rules-of-evidence-for-the-age-of-ai/) observes, adapting the rules of evidence for the age of AI is a work in progress across both state and federal systems.

The [U.S. Courts Advisory Committee on Evidence Rules](https://www.uscourts.gov/sites/default/files/2024-04_agenda_book_for_evidence_rules_meeting_final.pdf) has been actively examining how AI evidence interacts with the Federal Rules of Evidence, suggesting that federal guidance — and potentially amended rules — may be forthcoming.

## Action Items

- **Washington litigators (criminal and civil):** For any AI-enhanced or AI-generated evidence intended for trial use, conduct a pre-filing Frye analysis focused specifically on acceptance within the relevant forensic community, not commercial or broader technology communities.
- **Defense counsel:** Retain expert witnesses capable of testifying about forensic community standards for the specific AI tool at issue. Absence of peer review in forensic literature is presumptively fatal under Puloka.
- **Prosecutors:** The same framework applies to government-proffered AI evidence — confirm that any AI-enhanced surveillance footage or digital exhibits has been processed using methods accepted in the forensic video analysis community.
- **Civil litigators in Washington:** Review AI-generated demonstratives and AI-enhanced visual evidence against the Puloka standard before trial; engage forensic experts early to assess community acceptance.
- **Technology vendors:** Seek peer review and publication in recognized forensic science journals for any AI video or image enhancement tools being marketed for evidentiary use; engage with organizations such as the Scientific Working Group for Digital Evidence (SWGDE).
- **Monitor:** Watch for appellate review of Puloka, developments in the U.S. Advisory Committee on Evidence Rules AI workstream, and any legislative proposals in Washington for AI evidence authentication standards.

## Related Reports

- [reports/privacy/take-it-down-act-strahler-conviction-2026-04-12.md](/home/rafal/projecty/Zwiad/reports/privacy/take-it-down-act-strahler-conviction-2026-04-12.md) — First federal conviction involving AI deepfake imagery under the TAKE IT DOWN Act; directly related to AI-generated content evidentiary and enforcement landscape.
- [reports/privacy/litigation/california-cipa-chat-wiretapping-cody-v-boscov-2024-05-23.md](/home/rafal/projecty/Zwiad/reports/privacy/litigation/california-cipa-chat-wiretapping-cody-v-boscov-2024-05-23.md) — Court decision analyzing evidentiary and procedural standards in digital privacy litigation; shares "court-decision" development type in privacy category.
- [reports/privacy/illinois-bipa-7th-circuit-retroactivity-2026-04-12.md](/home/rafal/projecty/Zwiad/reports/privacy/illinois-bipa-7th-circuit-retroactivity-2026-04-12.md) — Seventh Circuit decision on biometric data evidence and litigation standards; related as court-decision precedent in privacy-adjacent technology law.

## Sources

1. [Duane Morris TechLaw Blog — Artificial Intelligence in the Courtroom (June 7, 2024)](https://blogs.duanemorris.com/techlaw/2024/06/07/artificial-intelligence-in-the-courtroom/) — Original Lexology/Duane Morris article that prompted this finding; analysis of the Puloka ruling and its implications.
2. [State v. Puloka, No. 21-1-04851-2 (Super. Ct. King Co. Wash. 2024) — Official Court Ruling (via NACDL)](https://www.nacdl.org/getattachment/89dee8b2-c47d-49c0-89d4-e187efe76551/Washington-v-Puloka-(No-21-1-04851-2-KNT)-(Sup-Ct-WA-2024).pdf?lang=en-US) — Official court document containing findings of fact and conclusions of law.
3. [Greenberg Traurig — Washington Court Rejects Novel Use of AI-Enhanced Video in Trial (May 2024)](https://www.gtlaw.com/en/insights/2024/5/washington-court-rejects-novel-use-of-ai-enhanced-video-in-trial) — Law firm alert with detailed case analysis and practitioner implications.
4. [NBC News — Washington state judge blocks use of AI-enhanced video as evidence in possible first-of-its-kind ruling](https://www.nbcnews.com/news/us-news/washington-state-judge-blocks-use-ai-enhanced-video-evidence-rcna141932) — Primary news coverage confirming first-of-its-kind characterization.
5. [American Bar Association — Court Excludes AI-Enhanced Videos from Trial Evidence (Fall 2024)](https://www.americanbar.org/groups/litigation/resources/litigation-news/2024/fall/court-excludes-aienhanced-videos-trial-evidence/) — ABA Litigation News analysis with practitioner commentary on the ruling.
6. [National Law Review — Washington State Court Rejects Admissibility of AI Enhanced Video](https://natlawreview.com/article/washington-court-rejects-novel-use-ai-enhanced-video-trial) — Legal analysis noting broader implications for courts' treatment of opaque AI methods.
7. [Quinn Emanuel — Adapting the Rules of Evidence for the Age of AI](https://www.quinnemanuel.com/the-firm/publications/adapting-the-rules-of-evidence-for-the-age-of-ai/) — Comprehensive law firm analysis of how Frye, Daubert, and authentication rules apply to AI evidence.
8. [Center for Democracy and Technology — Inadmissible? AI Evidence in Court](https://cdt.org/insights/inadmissible-ai-evidence-in-court/) — Policy analysis of AI evidence challenges including authenticity and jury evaluation concerns.
9. [Washington Rules of Evidence — ER 702 (Expert Testimony)](https://www.courts.wa.gov/court_rules/?fa=court_rules.display&group=ga&set=er&ruleid=gaer0702) — Official text of Washington's expert testimony rule applied in Puloka.
10. [Washington Rules of Evidence — ER 403 (Exclusion on Grounds of Prejudice)](https://www.courts.wa.gov/court_rules/?fa=court_rules.display&group=ga&set=ER&ruleid=gaer0403) — Official text of Washington's prejudice/confusion exclusion rule applied in Puloka.
11. [Cornell LII — Frye Standard](https://www.law.cornell.edu/wex/frye_standard) — Reference definition of the Frye general acceptance standard applied by Washington courts.
12. [Cornell LII — Daubert Standard](https://www.law.cornell.edu/wex/daubert_standard) — Reference definition of the contrasting Daubert standard used in federal courts and most states.
13. [U.S. Courts Advisory Committee on Evidence Rules — April 2024 Agenda Book](https://www.uscourts.gov/sites/default/files/2024-04_agenda_book_for_evidence_rules_meeting_final.pdf) — Federal rules committee materials on AI evidence, showing federal-level attention to same issues.
14. [Maryland State Bar Association — Applying Daubert and Frye to AI Evidence](https://www.msba.org/site/site/content/News-and-Publications/News/General-News/Applying_Daubert_and_Frye_to_AI_Evidence.aspx) — Analysis of how both evidentiary standards apply to AI-generated evidence across states.

Sources:
- [Duane Morris TechLaw Blog — Artificial Intelligence in the Courtroom](https://blogs.duanemorris.com/techlaw/2024/06/07/artificial-intelligence-in-the-courtroom/)
- [Washington Court Rejects Novel Use of AI-Enhanced Video in Trial | Greenberg Traurig LLP](https://www.gtlaw.com/en/insights/2024/5/washington-court-rejects-novel-use-of-ai-enhanced-video-in-trial)
- [Washington state judge blocks use of AI-enhanced video as evidence | NBC News](https://www.nbcnews.com/news/us-news/washington-state-judge-blocks-use-ai-enhanced-video-evidence-rcna141932)
- [Court Excludes AI-Enhanced Videos from Trial Evidence | American Bar Association](https://www.americanbar.org/groups/litigation/resources/litigation-news/2024/fall/court-excludes-aienhanced-videos-trial-evidence/)
- [Washington State Court Rejects Admissibility of AI Enhanced Video | National Law Review](https://natlawreview.com/article/washington-court-rejects-novel-use-ai-enhanced-video-trial)
- [Adapting the Rules of Evidence for the Age of AI | Quinn Emanuel](https://www.quinnemanuel.com/the-firm/publications/adapting-the-rules-of-evidence-for-the-age-of-ai/)
- [Inadmissible? AI Evidence in Court | CDT](https://cdt.org/insights/inadmissible-ai-evidence-in-court/)
- [ER 702 — Washington State Courts](https://www.courts.wa.gov/court_rules/?fa=court_rules.display&group=ga&set=er&ruleid=gaer0702)
- [ER 403 — Washington State Courts](https://www.courts.wa.gov/court_rules/?fa=court_rules.display&group=ga&set=ER&ruleid=gaer0403)
- [Frye Standard | Cornell LII](https://www.law.cornell.edu/wex/frye_standard)
- [Daubert Standard | Cornell LII](https://www.law.cornell.edu/wex/daubert_standard)
- [U.S. Courts Advisory Committee on Evidence Rules — April 2024 Agenda](https://www.uscourts.gov/sites/default/files/2024-04_agenda_book_for_evidence_rules_meeting_final.pdf)
- [Applying Daubert and Frye to AI Evidence | Maryland State Bar Association](https://www.msba.org/site/site/content/News-and-Publications/News/General-News/Applying_Daubert_and_Frye_to_AI_Evidence.aspx)
