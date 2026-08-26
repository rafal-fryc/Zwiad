---
title: "FTC Invokes TAKE IT DOWN Act Authority Against Platforms as Notice-and-Removal Obligations Take Effect"
date: 2026-05-19
jurisdiction: "Federal"
category: "privacy"
development_type: "enforcement"
finding_id: "SCAN-20260519-007"
topic_key: "FTC-PLATFORMS-2026"
topic_type: "enforcement"
first_reported: 2026-05-12
last_updated: 2026-06-01
status_history:
  - "2026-06-01: Added compliance guidance section (finding SCAN-20260601-047) covering deletion mechanism requirements, request validation, safe harbor provisions, and updated action items based on IAPP/McNees analysis and FTC business guidance."
cluster: "TAKE IT DOWN Act: Federal NCII Enforcement"
cluster_slug: "take-it-down-act-enforcement"
---

# FTC Invokes TAKE IT DOWN Act Authority Against Platforms as Notice-and-Removal Obligations Take Effect

**Jurisdiction:** Federal | **Category:** Privacy | **Date:** 2026-05-19

## Summary [HIGH confidence]

On May 19, 2026 — exactly one year after President Trump signed the TAKE IT DOWN Act — the Federal Trade Commission's civil enforcement authority over covered online platforms became active. [FTC Chairman Andrew Ferguson sent letters to more than a dozen prominent online platforms](https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-chairman-ferguson-advises-companies-comply-take-it-down-act), including Amazon, Alphabet, Apple, Meta, Microsoft, TikTok, and X, warning that platforms that fail to comply with the statute's 48-hour notice-and-removal obligations face civil penalties of up to $53,088 per violation. The FTC's actions constitute the first federal enforcement signal covering AI-generated nonconsensual intimate imagery, marking a significant expansion of federal content-removal obligations into the deepfake context.

Subsequent analysis from [IAPP](https://iapp.org/news/a/take-it-down-act-how-to-comply-as-the-ftc-begins-enforcement) and law firm practitioners — including McNees Wallace & Nurick — has clarified the practical compliance obligations: platforms must build a validated, clearly accessible deletion mechanism, honor incoming requests within 48 hours (including proactive removal of identical copies), and document good-faith efforts to qualify for the statute's limited safe harbor.

## Key Facts [HIGH confidence]

- The TAKE IT DOWN Act ([S. 146, 119th Congress, Public Law 119–12](https://www.congress.gov/bill/119th-congress/senate-bill/146/text)) was signed on May 19, 2025. Its criminal provisions (codified at **47 U.S.C. § 223(h)**) took effect immediately; Section 3's platform notice-and-removal obligations (codified at **47 U.S.C. § 223a**) allowed a one-year implementation window ending May 19, 2026. The full statutory text is available as [COMPS-18158 from GovInfo](https://www.govinfo.gov/content/pkg/COMPS-18158/pdf/COMPS-18158.pdf).
- FTC Chairman Ferguson sent pre-deadline warning letters to at least 15 companies: Amazon, Alphabet, Apple, Automattic, Bumble, Discord, Match Group, Meta, Microsoft, Pinterest, Reddit, SmugMug, Snapchat, TikTok, and X. ([FTC Press Release, May 2026](https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-chairman-ferguson-advises-companies-comply-take-it-down-act))
- Covered platforms must establish a clearly accessible process for victims to request removal of nonconsensual intimate images (NCII) and AI-generated deepfakes. Upon receipt of a valid request, platforms must remove the reported content **and all known identical copies** within **48 hours**. ([FTC Compliance Guidance](https://www.ftc.gov/business-guidance/resources/complying-take-it-down-act))
- A "covered platform" is defined as a website, online service, online application, or mobile application that serves the public and either (1) primarily provides a forum for user-generated content, or (2) publishes, curates, hosts, or makes available NCII in the regular course of trade or business. Excluded: broadband ISPs, email providers, and sites that primarily host pre-selected content where interactive features are incidental. ([Congress.gov CRS Analysis LSB11314](https://www.congress.gov/crs-product/LSB11314))
- Noncompliance is treated as a violation of a rule defining an unfair or deceptive act or practice under **Section 18(a)(1)(B) of the FTC Act (15 U.S.C. § 57a(a)(1)(B))**, with civil penalties enforceable under **Sections 5(l) and 5(m)**, exposing platforms to civil penalties of **$53,088 per violation**. ([National Law Review analysis](https://natlawreview.com/article/ftcs-take-it-down-act-stakeholder-letter-signals-heightened-compliance-priority); [CRS Analysis LSB11314](https://www.congress.gov/crs-product/LSB11314))
- The Act partially displaces Section 230 immunity for covered platforms: FTC enforcement under Section 3 is not blocked by Section 230 because the obligation runs to the removal process itself, not content moderation decisions. The interplay between Section 230 and potential private claims remains legally unsettled. ([Troutman Pepper Locke analysis](https://www.troutman.com/insights/platforms-face-section-230-shift-from-take-it-down-act/))
- Chairman Ferguson encouraged platforms to implement content-hashing technologies to proactively prevent reappearance of previously removed content and to share hash databases with the [National Center for Missing and Exploited Children (NCMEC)](https://www.missingkids.org/) and [StopNCII.org](https://stopncii.org/). ([CyberScoop](https://cyberscoop.com/ftc-take-it-down-act-enforcement-deepfakes/))
- No formal administrative complaints or named investigations against specific platforms had been publicly filed as of May 19, 2026. The FTC described its enforcement posture as one of active monitoring, with formal actions expected to follow in coming months against non-compliant platforms. ([SC Media](https://www.scworld.com/brief/ftc-begins-enforcing-take-it-down-act-for-nonconsensual-deepfakes))
- At the IAPP Global Privacy Summit 2026, FTC officials confirmed the TAKE IT DOWN Act is a top enforcement priority for the agency in 2026. ([National Law Review](https://natlawreview.com/article/what-platforms-need-know-about-compliance-ftc-take-it-down-act))

## Compliance Guidance: Building a Compliant Deletion Mechanism [HIGH confidence]

This section incorporates analysis published after the May 19 enforcement launch, including guidance from [IAPP](https://iapp.org/news/a/take-it-down-act-how-to-comply-as-the-ftc-begins-enforcement) and [National Law Review](https://natlawreview.com/article/what-platforms-need-know-about-compliance-ftc-take-it-down-act), as well as the [FTC's own business guidance](https://www.ftc.gov/business-guidance/resources/complying-take-it-down-act).

### The 48-Hour Removal Window

The statute requires removal "as soon as possible" and no later than **48 hours** after receipt of a valid request. The clock begins when a valid notification is received — not when the platform routes the request internally. Platforms must therefore front-load intake processing so that triage, validation, and escalation all occur within a window that leaves time for actual content removal. Key operational requirements:

- Remove the specifically identified intimate visual depiction within 48 hours.
- **Make reasonable efforts to find and remove all known identical copies** within the same 48-hour window. The phrase "known identical copies" encompasses both on-platform duplicates (re-uploads, cross-posted content) and, where technically feasible, copies the platform is able to identify through its own systems. ([FTC Compliance Guidance](https://www.ftc.gov/business-guidance/resources/complying-take-it-down-act))
- Assign each request a confirmation or report number and provide status updates to the requestor — both a best practice recommended by the FTC and a practical defense against allegations of bad faith. ([FTC Business Blog, May 2026](https://www.ftc.gov/business-guidance/blog/2026/05/take-it-down-act-enforcement-starts-now-what-know-about-ftc-tida))

### Accessibility and Visibility of the Mechanism

The statute requires the removal process to be **clearly and conspicuously disclosed**. The FTC has elaborated that "clearly accessible" means:

- A plain-language description of the notice-and-removal process must be displayed prominently — on the home page and wherever intimate content can appear on the platform.
- The submission mechanism should be reachable directly from the content itself (e.g., a "report this" link on each image or video), not merely buried in a help center or terms of service page.
- The process must accommodate **non-account holders**: individuals who are depicted but are not registered users of the platform must have a pathway to submit a removal request without creating an account. ([FTC Compliance Guidance](https://www.ftc.gov/business-guidance/resources/complying-take-it-down-act); [National Law Review](https://natlawreview.com/article/what-platforms-need-know-about-compliance-ftc-take-it-down-act))

## Compliance Guidance: Validating Takedown Requests [HIGH confidence]

A platform's obligation is triggered by receipt of a **valid notification**. The statute specifies what a valid notification must contain, drawn from [47 U.S.C. § 223a](https://www.law.cornell.edu/uscode/text/47/223a):

1. **Physical or electronic signature** of the identifiable individual (i.e., the depicted person) or an authorized representative acting on their behalf.
2. **Identification of the specific depiction** — sufficient description or URL for the platform to locate the content.
3. **Information sufficient to locate the depiction** on the platform.
4. **A good-faith statement** asserting that the depicted individual believes the content was distributed without their consent, along with any information relevant to the platform's verification of that assertion.
5. **Contact information** sufficient for the platform to communicate with the requestor about the outcome.

**Identity verification:** The statute does not prescribe a specific identity verification methodology, but compliance practitioners have recommended that platforms accept government-ID verification for non-account-holders and use account-credential confirmation for registered users. Platforms should not impose overly burdensome verification requirements that effectively block legitimate requests — the FTC's enforcement lens focuses on whether platforms are facilitating removal, not erecting barriers to it. ([Skadden analysis](https://www.skadden.com/insights/publications/2025/06/take-it-down-act))

**Request tracking and recordkeeping:** Platforms should maintain logs of each incoming request, the date and time of receipt, the validation determination (valid or invalid, with reasoning), the date of content removal, and any communications with the requestor. These records form the documentary basis for a good-faith defense in any FTC investigation. ([National Law Review](https://natlawreview.com/article/ftc-begins-enforcement-take-it-down-act-new-risks-and-tools-businesses))

**Duplicate detection — hashing:** To satisfy the "known identical copies" obligation, platforms should implement or contract for digital hash-matching technology (e.g., PhotoDNA or equivalent). When content is flagged and removed, the platform generates a cryptographic fingerprint (hash) of the file; subsequent uploads matching that hash are auto-flagged or blocked. The FTC strongly encourages — though does not formally require as a statutory element — sharing of hashes with [NCMEC's Take It Down service](https://www.missingkids.org/) and [StopNCII.org](https://stopncii.org/). ([CyberScoop](https://cyberscoop.com/ftc-take-it-down-act-enforcement-deepfakes/))

## Compliance Guidance: Safe Harbor Provisions [HIGH confidence]

The TAKE IT DOWN Act builds a statutory safe harbor into [47 U.S.C. § 223a](https://www.law.cornell.edu/uscode/text/47/223a) for platforms that act in good faith:

> A covered platform shall not be liable for any claim based on the covered platform's good faith disabling of access to, or removal of, material claimed to be a nonconsensual intimate visual depiction based on facts or circumstances from which the unlawful publishing of an intimate visual depiction is apparent, **regardless of whether the intimate visual depiction is ultimately determined to be unlawful or not.**

**Scope of protection:** The safe harbor insulates a platform from civil claims by content posters who argue the removal was wrongful — for instance, a poster who claims the content was consensually shared. As long as the platform acted in good faith on the apparent facts of the request, it is shielded even if that determination later proves incorrect. ([Proskauer Rose analysis](https://www.proskauer.com/blog/take-it-down-act-signed-into-law-offering-tools-to-fight-non-consensual-intimate-images-and-creating-a-new-image-takedown-mechanism/))

**Critical limitation — no safe harbor for inaction:** The safe harbor does not extend to a platform's decision to reject or refuse to honor a removal request. A platform that receives a valid request and takes no action, or that imposes conditions beyond the statutory requirements to delay removal, cannot claim good-faith protection. ([47 U.S.C. § 223a; Troutman Pepper Locke](https://www.troutman.com/insights/platforms-face-section-230-shift-from-take-it-down-act/))

**Relationship to Section 230:** The Act adds its own good-faith safe harbor that operates alongside — and in some cases supplements — the Good Samaritan provision of Section 230 of the Communications Decency Act. The TAKE IT DOWN Act safe harbor is narrower in scope (limited to NCII removal actions) but provides a cleaner statutory basis for removing NCII content without triggering Section 230 debates about whether removal constitutes "editorial discretion." ([University of Baltimore Law Review](https://ubaltlawreview.com/2025/11/03/the-take-it-down-acts-48-hour-deadline-what-does-it-mean-when-section-230-still-shields-platforms/))

**Documenting good faith:** To maximize protection, platforms should:
- Maintain written internal policies governing NCII removal processes.
- Document each removal decision and the facts that supported it.
- Retain records for a period consistent with applicable litigation hold standards (minimum 3 years recommended by practitioners).
- Train content moderation and legal staff on the distinction between valid TIDA requests and other takedown regimes (DMCA, CSAM). ([National Law Review](https://natlawreview.com/article/ftc-begins-enforcement-take-it-down-act-new-risks-and-tools-businesses))

## Action Items

- **Audit notice-and-removal infrastructure immediately.** Confirm your platform has a clearly and conspicuously displayed NCII removal request mechanism that meets the Act's requirements. Platforms that lacked a compliant process as of May 19, 2026 are already in a potential violation posture.
- **Verify 48-hour removal SLA end-to-end.** Internal workflows must ensure content and all known identical copies are removed within 48 hours of valid notice. Map every handoff — intake, validation, moderation, technical removal, duplicate scan — and set internal targets that leave buffer before the statutory deadline. Document timestamps for compliance defensibility.
- **Ensure accessibility for non-account-holders.** The removal mechanism must permit individuals who do not have an account on your platform to submit requests. A gate that requires account creation to report NCII content is a compliance gap.
- **Implement per-request confirmation numbers and status updates.** The FTC explicitly recommends this as evidence of a functioning, good-faith process. Build it into your intake system before the first formal complaint arrives.
- **Deploy content-hashing for duplicate detection.** The "known identical copies" obligation is not satisfied by manual review alone. Implement hash-based fingerprinting (PhotoDNA or equivalent) and integrate with NCMEC and StopNCII hash databases to proactively block re-uploads.
- **Assess whether your platform is "covered."** Apply the statutory definition carefully. Platforms primarily providing user-generated content forums are squarely covered. Platforms with incidental interactive features may qualify for the exclusion — obtain counsel analysis if coverage is unclear.
- **Review Section 230 reliance.** Do not assume Section 230 immunity shields non-compliance with the notice-and-removal obligation. The criminal provision (47 U.S.C. § 223(h)) is already outside Section 230's scope; the civil enforcement mechanism under Section 3 appears to follow suit.
- **Build and document your good-faith record.** Establish written internal policies, train moderation staff, and retain decision records to support a good-faith defense in any FTC investigation. The statutory safe harbor only protects platforms that can demonstrate they acted in good faith on the apparent facts.
- **Create a dedicated TIDA escalation path.** TAKE IT DOWN Act requests have distinct requirements and a shorter response window than DMCA or CSAM workflows. Do not route TIDA requests through general content moderation queues.
- **Monitor for formal FTC complaints.** The first wave of enforcement actions is expected within months. Platforms should assess their litigation readiness and consider proactive engagement with the FTC if compliance gaps exist.

## Related Reports

- [reports/privacy/take-it-down-act-strahler-conviction-2026-04-12.md](../take-it-down-act-strahler-conviction-2026-04-12.md) — Covers the first criminal conviction under the Act's criminal provisions (47 U.S.C. § 223(h)), providing background on the statute's scope and the DOJ's parallel criminal enforcement track.
- [reports/privacy/enforcement-actions/ftc-match-okcupid-clarifai-enforcement-2026-04-07.md](ftc-match-okcupid-clarifai-enforcement-2026-04-07.md) — FTC's March 2026 enforcement against Match Group/OkCupid for unauthorized AI data sharing demonstrates the Commission's active enforcement posture on platform data practices.
- [reports/privacy/childrens-privacy/coppa-amendments-compliance-deadline-2026-04-13.md](../childrens-privacy/coppa-amendments-compliance-deadline-2026-04-13.md) — COPPA amendments create overlapping compliance obligations for platforms serving minors, including platforms covered by the TAKE IT DOWN Act.

## Sources

1. [Text - S.146 - TAKE IT DOWN Act (Congress.gov)](https://www.congress.gov/bill/119th-congress/senate-bill/146/text) — Official enrolled statutory text from Congress.gov.
2. [TAKE IT DOWN Act - GovInfo (COMPS-18158)](https://www.govinfo.gov/content/pkg/COMPS-18158/pdf/COMPS-18158.pdf) — Official unamended text of Public Law 119–12.
3. [47 U.S.C. § 223a — Notice and removal of nonconsensual intimate visual depictions (LII/Cornell)](https://www.law.cornell.edu/uscode/text/47/223a) — Codified statutory text of Section 3, including safe harbor provision.
4. [FTC Chairman Ferguson Advises Companies to Comply with the Take It Down Act (FTC Press Release, May 2026)](https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-chairman-ferguson-advises-companies-comply-take-it-down-act) — Primary FTC announcement of enforcement signal and warning letters.
5. [FTC Begins Enforcing the TAKE IT DOWN Act (FTC Press Release, May 2026)](https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-begins-enforcing-take-it-down-act) — FTC announcement of formal enforcement launch.
6. [FTC Sends Warning Letters to Companies About Compliance with the TAKE IT DOWN Act (FTC)](https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-sends-warning-letters-companies-about-compliance-take-it-down-act) — Detail on warning letters issued to specific platforms.
7. [Complying With the Take It Down Act (FTC Business Guidance)](https://www.ftc.gov/business-guidance/resources/complying-take-it-down-act) — Official FTC compliance resource for covered platforms; primary source for deletion mechanism and accessibility requirements.
8. [Take It Down Act Enforcement Starts Now: What to Know About the FTC and TIDA (FTC Business Blog)](https://www.ftc.gov/business-guidance/blog/2026/05/take-it-down-act-enforcement-starts-now-what-know-about-ftc-tida) — FTC blog post clarifying operational requirements including confirmation numbers and status updates.
9. [TAKE IT DOWN Act statute page (FTC Legal Library)](https://www.ftc.gov/legal-library/browse/statutes/tools-address-known-exploitation-immobilizing-technological-deepfakes-websites-networks-act-take-it) — FTC's statutory reference page.
10. [CRS Analysis LSB11314 — The TAKE IT DOWN Act (Congress.gov)](https://www.congress.gov/crs-product/LSB11314) — Congressional Research Service analysis of the statute's scope and definitions.
11. [TAKE IT DOWN Act: How to Comply as the FTC Begins Enforcement (IAPP)](https://iapp.org/news/a/take-it-down-act-how-to-comply-as-the-ftc-begins-enforcement) — Detailed compliance guidance from the International Association of Privacy Professionals, including McNees Wallace & Nurick analysis.
12. [What Platforms Need to Know About Compliance with the FTC Take It Down Act (National Law Review)](https://natlawreview.com/article/what-platforms-need-know-about-compliance-ftc-take-it-down-act) — Practitioner compliance checklist covering intake, validation, duplicate detection, and recordkeeping.
13. [FTC Begins Enforcement of the TAKE IT DOWN Act: New Risks and Tools for Businesses (National Law Review)](https://natlawreview.com/article/ftc-begins-enforcement-take-it-down-act-new-risks-and-tools-businesses) — Analysis of enforcement risk and documentation best practices for good-faith defense.
14. [FTC's TAKE IT DOWN Act Stakeholder Letter Signals Heightened Compliance Priority (National Law Review)](https://natlawreview.com/article/ftcs-take-it-down-act-stakeholder-letter-signals-heightened-compliance-priority) — Law firm analysis of FTC letter significance and penalty exposure.
15. [Here's How the FTC Plans to Enforce the Take It Down Act (CyberScoop)](https://cyberscoop.com/ftc-take-it-down-act-enforcement-deepfakes/) — Reporting on FTC enforcement posture, platform-specific letters, and hashing recommendations.
16. [FTC Begins Enforcing Take It Down Act for Nonconsensual Deepfakes (SC Media)](https://www.scworld.com/brief/ftc-begins-enforcing-take-it-down-act-for-nonconsensual-deepfakes) — Brief on enforcement launch and status as of May 19, 2026.
17. ['Take It Down Act' Requires Online Platforms To Remove Unauthorized Intimate Images and Deepfakes When Notified (Skadden)](https://www.skadden.com/insights/publications/2025/06/take-it-down-act) — Detailed statutory analysis including valid notification elements and identity verification considerations.
18. [Platforms Face Section 230 Shift From Take It Down Act (Troutman Pepper Locke)](https://www.troutman.com/insights/platforms-face-section-230-shift-from-take-it-down-act/) — Analysis of Section 230 interaction and safe harbor scope.
19. [Take it Down Act Signed into Law (Proskauer Rose)](https://www.proskauer.com/blog/take-it-down-act-signed-into-law-offering-tools-to-fight-non-consensual-intimate-images-and-creating-a-new-image-takedown-mechanism/) — Analysis of safe harbor scope including wrongful removal protection.
20. [The TAKE IT DOWN Act's 48-Hour Deadline: What Does It Mean When Section 230 Still Shields Platforms? (University of Baltimore Law Review)](https://ubaltlawreview.com/2025/11/03/the-take-it-down-acts-48-hour-deadline-what-does-it-mean-when-section-230-still-shields-platforms/) — Academic analysis of Section 230 and TIDA safe harbor interaction.
21. [May 19 Deadline for TAKE IT DOWN Act Compliance: Is Your Company Prepared? (Wiley Law)](https://www.wiley.law/alert-May-19-Deadline-for-TAKE-IT-DOWN-Act-Compliance-Is-Your-Company-Prepared) — Pre-deadline compliance checklist from Wiley Rein.
22. [TAKE IT DOWN Act Targets Deepfakes: Are Online Platforms Caught in the Crosshairs? (Morgan Lewis)](https://www.morganlewis.com/pubs/2025/06/take-it-down-act-targets-deepfakes-are-online-platforms-caught-in-the-crosshairs) — Law firm analysis of covered platform scope and compliance risk.
23. [President Trump Signs Take It Down Act Into Law (Latham & Watkins)](https://www.lw.com/en/insights/president-trump-signs-take-it-down-act-into-law) — Summary of Act's provisions at signing.
