---
title: "Massachusetts SJC Holds Website Tracking Does Not Violate State Wiretap Act (Vita v. New England Baptist Hospital)"
date: 2024-11-08
jurisdiction: "Massachusetts"
category: "privacy"
development_type: "court-decision"
finding_id: "SCAN-20241108-011"
topic_key: "massachusetts-2490bba8-2024"
topic_type: "enforcement"
first_reported: 2024-11-08
last_updated: 2024-11-08
status_history: []
cluster: "Massachusetts Wiretap Act (M.G.L. c. 272 § 99): Website Tracking Litigation"
cluster_slug: "massachusetts-wiretap-act-website-tracking-litigation"
---

# Massachusetts SJC Holds Website Tracking Does Not Violate State Wiretap Act (Vita v. New England Baptist Hospital)

**Jurisdiction:** Massachusetts | **Category:** Privacy | **Date:** 2024-11-08

## Executive Summary [HIGH confidence]

On October 24, 2024, the Massachusetts Supreme Judicial Court (SJC) issued a landmark 5-1 decision in [*Vita v. New England Baptist Hospital*](https://law.justia.com/cases/massachusetts/supreme-court/2024/sjc-13542.html) (SJC-13542), holding that the Massachusetts Wiretap Act, [M.G.L. c. 272, § 99](https://malegislature.gov/Laws/GeneralLaws/PartIV/TitleI/Chapter272/Section99), does not apply to the interception of website browsing activities by third-party tracking technologies such as session replay software, pixel trackers, and analytics tools. The court applied the rule of lenity to resolve statutory ambiguity in defendants' favor, reasoning that the 1968 statute's reference to "communication" cannot be read to encompass interactions between a user and a website — as opposed to person-to-person communications. This is the first state supreme court ruling to directly address whether analog-era wiretap statutes reach modern website tracking tools, and it substantially curtails one of the primary legal theories driving a wave of class action litigation against companies using analytics and advertising technology. Although defendants prevailed on the wiretap theory, the SJC expressly acknowledged the serious privacy concerns raised by the proliferation of tracking technologies and directed aggrieved parties to the Legislature for a remedy — leaving open the possibility of statutory reform.

## Background [HIGH confidence]

### The Wave of Website Wiretap Litigation

Between 2022 and 2024, plaintiffs' counsel filed hundreds of class actions in state and federal courts across the United States, alleging that the deployment of third-party tracking tools on websites violated state wiretap statutes. The primary targets were session replay tools, Meta Pixel (formerly Facebook Pixel), Google Analytics, and similar software that captures user interactions — including pages visited, mouse movements, keystrokes, and browsing behavior — and transmits that data to third parties. Plaintiffs argued that these transmissions constituted unlawful "interceptions" of protected "communications" under statutes originally designed to prohibit telephone wiretapping.

The Massachusetts Wiretap Act, [M.G.L. c. 272, § 99](https://malegislature.gov/Laws/GeneralLaws/PartIV/TitleI/Chapter272/Section99), enacted in 1968, was a frequent target. The statute makes it a crime to "willfully commit an interception" of a "wire communication" or "oral communication," and provides a private civil right of action. Unlike federal wiretap law, the Massachusetts statute is an all-party consent law, meaning that interception without the consent of all parties is unlawful. Plaintiffs argued that website operators who embed third-party trackers cause those trackers to "intercept" users' browsing "communications" without user consent.

Healthcare providers became the epicenter of this litigation. In 2022, HHS Office for Civil Rights issued a [bulletin asserting that certain deployments of tracking technology on healthcare websites triggered HIPAA obligations](https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/hipaa-online-tracking/index.html). This regulatory pressure — combined with the availability of state-law private rights of action — produced a surge of class actions against hospital systems and other healthcare entities in Massachusetts and nationally. By late 2024, [hundreds of such suits were pending](https://www.insideclassactions.com/2024/11/12/massachusetts-supreme-judicial-court-holds-that-third-party-technologies-relating-to-web-browsing-do-not-violate-massachusetts-wiretap-act/) in courts nationwide.

### Procedural History of Vita

Plaintiff Kathleen Vita filed two consolidated class action complaints against New England Baptist Hospital (NEBH) and Beth Israel Deaconess Medical Center (BIDMC), two major Boston-area healthcare institutions. Vita alleged that both hospitals had embedded Meta Pixel and Google Analytics on their public-facing websites, causing those tools to capture and transmit her browsing activity — including information about the doctors she searched and the medical conditions she researched — to Facebook and Google for advertising purposes, without her knowledge or consent. Vita did not allege that any messages she sent to a healthcare provider, or any information from an authenticated patient portal, was intercepted; the claim was confined to her browsing of publicly accessible website pages.

The trial court denied the hospitals' motions to dismiss, allowing the wiretap claims to proceed. The SJC granted direct appellate review on the threshold question: does the term "communication" in the Massachusetts Wiretap Act extend to a user's web browsing interactions with a website?

### Role of Amicus Parties

The case attracted significant amicus attention reflecting its national importance. The [Electronic Privacy Information Center (EPIC) and National Consumer Law Center filed a brief](https://epic.org/wp-content/uploads/2024/03/Vita-v-New-England-Baptist-Amicus-NCLC-EPIC.pdf) in support of the plaintiff, arguing that the wiretap law's intent to protect privacy should be read broadly to reach modern surveillance techniques and that failure to do so would leave patients without meaningful recourse. The [U.S. Chamber of Commerce](https://www.uschamber.com/cases/privacy-and-cybersecurity/vita-v-new-england-baptist-hospital) and the [Greater Boston Chamber of Commerce and Massachusetts Nonprofit Network](https://bostonchamber.com/press-release/chamber-and-massachusetts-nonprofit-network-file-amicus-brief-in-vita-v-new-england-baptist-hospital/) filed briefs on behalf of the defendants, arguing that extending the wiretap statute to website analytics would impose sweeping and unforeseeable liability on organizations that rely on standard digital tools.

## Detailed Analysis [HIGH confidence]

### The Statutory Framework

The Massachusetts Wiretap Act, codified at [M.G.L. c. 272, § 99](https://malegislature.gov/Laws/GeneralLaws/PartIV/TitleI/Chapter272/Section99), defines "wire communication" and "oral communication" and prohibits their interception. The critical interpretive question was whether a user's web browsing activity — browsing publicly accessible informational pages on a hospital website, with no exchange of messages with another person — constitutes a "communication" within the statute's meaning.

The statute's legislative declaration states that its purpose is to protect against secret surveillance by "public and private agencies and individuals" and to ensure the "privacy of persons and to define clearly the circumstances under which the interception of wire and oral communications may be permitted." Critically, the Legislature enacted the statute in 1968, decades before the internet existed.

### The Court's Majority Opinion

Writing for a 5-1 majority, the SJC applied the rule of lenity — the principle that ambiguity in a criminal statute must be resolved in favor of the defendant — to hold that web browsing does not constitute a "communication" within the Massachusetts Wiretap Act.

The court reasoned that the statute's plain language and historical context both indicated that "communication" was intended to cover person-to-person transmissions of information — telephone calls, telegrams, messages exchanged between individuals. The statutory examples of covered communications — "private conversations in person or over the telephone or private person-to-person messages communicated through the use of wire or cables" — describe bilateral exchanges, not unilateral user interactions with a published website.

The majority stated directly: "we cannot conclude with any confidence that the Legislature intended 'communication' to extend so broadly as to criminalize the interception of web browsing and other such interactions." Applying the rule of lenity to resolve this ambiguity in favor of defendants, the court reversed the trial court's denial of the motions to dismiss and dismissed the wiretap claims. The majority also declared that "[i]f the Legislature intends for the Wiretap Act's criminal and civil penalties to prohibit the tracking of a person's browsing of, and interaction with, published information on websites, it must say so expressly."

### The Dissent

Justice Dalila Argaez Wendlandt dissented. She argued that the hospitals' privacy disclosures were misleading because they did not adequately disclose the extent of third-party tracking, and that the Legislature's express statement of purpose — protecting citizens against evolving surveillance — was broad enough to reach the tracking technologies at issue. The dissent contended that the majority's narrow construction left patients without effective protection against a practice the statute's drafters would have prohibited had they foreseen it. The dissent notably characterized the hospitals' conduct as effectively monetizing patients' health interests for advertising revenue without meaningful disclosure.

### The Rule of Lenity as the Decisive Tool

The SJC's heavy reliance on the rule of lenity is analytically notable. Courts typically apply lenity only as a last resort, after exhausting conventional textual, structural, and purposive analysis. By invoking lenity here, the court effectively acknowledged that the case was genuinely close on the merits — a point significant for both legislative reform efforts and future litigation in other jurisdictions interpreting analogous statutes. The rule of lenity is typically available only in the context of ambiguous criminal statutes; because the Massachusetts Wiretap Act is a criminal statute with civil remedies, the rule applied.

### First-State-Supreme-Court Ruling on Point

Legal commentators have noted that *Vita* is the [first decision by any state supreme court](https://www.insideclassactions.com/2024/11/12/massachusetts-supreme-judicial-court-holds-that-third-party-technologies-relating-to-web-browsing-do-not-violate-massachusetts-wiretap-act/) addressing whether state-analog wiretap statutes reach website tracking technology. While the ruling is binding only in Massachusetts, it is influential persuasive authority for courts in other states construing analogous provisions. States with similar all-party consent wiretap statutes — including California (CIPA, Cal. Penal Code § 631), Pennsylvania, and others — have seen parallel pixel tracking class actions. The *Vita* court's reasoning, while grounded in Massachusetts law, articulates a framework that other courts can adopt or distinguish.

## Impact Assessment [HIGH confidence]

### Effect on Massachusetts Wiretap Class Actions

The *Vita* ruling directly forecloses future claims under the Massachusetts Wiretap Act for website browsing tracking in the absence of legislative amendment. For cases pending at the time of the decision, defendants gained a strong basis to seek dismissal of wiretap counts. In *Doe v. Tenet Healthcare Corporation* (No. 1:23-cv-12978-PBS, D. Mass.), Judge Saris had previously preserved the wiretap count without prejudice pending the SJC's resolution of *Vita*; following the October 24, 2024 ruling, that count became vulnerable to renewed dismissal.

Plaintiffs in Massachusetts are not without recourse. Multiple alternative theories survived in parallel cases: negligence, breach of fiduciary duty (particularly significant in the healthcare context), breach of implied contract, the [Massachusetts Right to Privacy, M.G.L. c. 214, § 1B](https://malegislature.gov/Laws/GeneralLaws/PartIII/TitleI/Chapter214/Section1b), and the [Massachusetts Consumer Protection Act, M.G.L. c. 93A](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXV/Chapter93A) remain available. The *Vita* ruling does not affect any of these alternative theories.

### Significance for Healthcare Organizations

Healthcare providers deploying tracking pixels on public-facing websites in Massachusetts face substantially reduced wiretap liability exposure following *Vita*. However, as the [Boston Bar Association has noted](https://bostonbar.org/journal/slc-web-tracking-does-not-violate-wiretap-act-but-businesses-may-not-be-totally-in-the-clear/), the *Vita* court's reasoning distinguishes between public website pages (where the user interacts with published content) and authenticated patient portals (where users may be sending messages to healthcare providers). The latter may still implicate person-to-person communication in ways the statute was designed to protect, and the *Vita* holding may not extend to those scenarios.

### Persuasive Authority for Other Jurisdictions

[Law firm analyses](https://www.thompsoncoburn.com/insights/the-recent-massachusetts-court-holding-in-vita-is-a-win-for-businesses-and-a-look-at-trends-in-novel-u-s-wiretapping-litigation/) have emphasized *Vita*'s value as persuasive authority in other states. California, which has seen the highest volume of CIPA-based website tracking class actions, does not have an analogous rule of lenity argument available in the same form, but defendants can cite *Vita*'s reasoning about the nature of web browsing as a "communication." Courts in Pennsylvania, Illinois, and Maryland — other jurisdictions with active wiretap class action dockets — may similarly look to *Vita* when construing their own statutes.

[Sidley Austin's analysis](https://datamatters.sidley.com/2024/10/30/massachusetts-highest-court-signals-willingness-to-scrutinize-state-wiretapping-laws-and-knock-out-claims-at-the-pleading-stage/) notes that *Vita* signals state supreme courts' willingness to scrutinize wiretap claims at the pleading stage — a procedural posture favorable to defendants in these suits, which are frequently brought to extract settlements based on the cost of class-wide litigation rather than the merits.

### Legislative Reform Pathway

The SJC majority's explicit directive — that if the Legislature wants to prohibit website tracking under the wiretap statute, "it must say so expressly" — is an unusual judicial invitation to legislative action. Privacy advocates, including [EPIC](https://epic.org/massachusetts-top-court-rejects-privacy-arguments-holds-that-hospital-website-tracking-is-not-a-wiretap/), responded to the ruling with calls for the Massachusetts Legislature to amend the Wiretap Act or enact a comprehensive state privacy law to address the gap. As of the date of the original finding (November 2024), Massachusetts had not yet enacted a comprehensive consumer privacy law — one of a small number of states without such legislation. The *Vita* decision adds urgency to these legislative discussions in the Commonwealth.

### National Context: Tracking Pixel Litigation Landscape

The [National Law Review's state-by-state guide to tracking pixel wiretapping risk](https://natlawreview.com/article/tracking-pixel-litigation-expands-state-state-guide-wiretapping-risk) illustrates the patchwork nature of the legal landscape nationally. In some states, district courts have dismissed pixel tracking wiretap claims; in others, courts have permitted them to proceed. *Vita* now provides a definitive state-law anchor on the defense side for Massachusetts, distinguishing it from states where the law remains unsettled.

## Action Items

- Companies operating websites accessible to Massachusetts residents should conduct an inventory of all third-party tracking technologies deployed, distinguishing between public pages and authenticated portals where person-to-person communications occur.
- Businesses defending pending Massachusetts wiretap class actions based on website tracking should file or renew motions to dismiss the wiretap counts in light of *Vita*, citing the SJC's holding directly.
- For authenticated patient portals and other authenticated interactive environments, wiretap exposure analysis should proceed independently — the *Vita* holding is limited to public-facing, non-communicative website browsing.
- Do not assume *Vita* disposes of other state-law theories: negligence, breach of fiduciary duty (especially in healthcare), M.G.L. c. 93A consumer protection, and M.G.L. c. 214, § 1B right to privacy claims remain viable in Massachusetts.
- Businesses operating nationally should consult state-specific counsel for jurisdictions with active pixel tracking litigation (California, Pennsylvania, Illinois) — *Vita* is persuasive but not binding authority outside Massachusetts.
- Monitor Massachusetts legislative activity for any proposed amendment to the Wiretap Act or enactment of a comprehensive state privacy law, both of which could reverse or narrow the *Vita* defense.
- Review third-party tracking technology configurations, particularly on healthcare websites, to assess ongoing risk under HIPAA and alternative state-law theories regardless of wiretap exposure.

## Related Reports

- [reports/privacy/litigation/massachusetts-doe-v-tenet-healthcare-pixel-tracking-2024-05-20.md](reports/privacy/litigation/massachusetts-doe-v-tenet-healthcare-pixel-tracking-2024-05-20.md) -- The federal district court companion case that preserved the wiretap count pending the SJC's resolution in *Vita*; provides full analysis of the non-wiretap claims that survived dismissal.
- [reports/privacy/litigation/california-cipa-chat-wiretapping-garcia-v-buildcom-2024-04-17.md](reports/privacy/litigation/california-cipa-chat-wiretapping-garcia-v-buildcom-2024-04-17.md) -- Parallel wiretap class action litigation under California's CIPA statute arising from website tracking tools, illustrating the multi-state scope of pixel tracking litigation and the varying outcomes under different state wiretap laws.
- [reports/privacy/litigation/california-cipa-chat-wiretapping-cody-v-boscov-2024-05-23.md](reports/privacy/litigation/california-cipa-chat-wiretapping-cody-v-boscov-2024-05-23.md) -- Additional California CIPA website wiretapping decision providing comparative context on how different courts are resolving the same technology-statute interface question.
- [reports/privacy/enforcement-actions/massachusetts-sjc-meta-minors-2026-04-13.md](reports/privacy/enforcement-actions/massachusetts-sjc-meta-minors-2026-04-13.md) -- Massachusetts SJC ruling on technology company liability under state law, illustrating the broader context of Massachusetts courts' treatment of digital privacy claims.

## Sources

1. [Vita v. New England Baptist Hospital, SJC-13542 (Mass. Oct. 24, 2024) — Justia](https://law.justia.com/cases/massachusetts/supreme-court/2024/sjc-13542.html) -- Official case text of the SJC's October 24, 2024 ruling; primary source for all holdings and quotes from the majority opinion
2. [Massachusetts General Laws c. 272, § 99 — Massachusetts Legislature](https://malegislature.gov/Laws/GeneralLaws/PartIV/TitleI/Chapter272/Section99) -- Official text of the Massachusetts Wiretap Act; foundation for the statutory interpretation analysis
3. [Vita v. New England Baptist Hospital — FindLaw](https://caselaw.findlaw.com/court/ma-supreme-judicial-court/116650802.html) -- Alternative official case text with procedural history and full opinion
4. [Massachusetts Supreme Court Narrows Scope of State's Wiretapping Law — WilmerHale (Nov. 5, 2024)](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20241105-massachusetts-supreme-court-narrows-scope-of-states-wiretapping-law) -- Detailed law firm analysis of the holding, rule of lenity rationale, and multi-jurisdictional implications
5. [Massachusetts Supreme Judicial Court Holds That Third-Party Technologies Relating to Web Browsing Do Not Violate Massachusetts Wiretap Act — Inside Class Actions (Nov. 12, 2024)](https://www.insideclassactions.com/2024/11/12/massachusetts-supreme-judicial-court-holds-that-third-party-technologies-relating-to-web-browsing-do-not-violate-massachusetts-wiretap-act/) -- Analysis confirming *Vita* as the first state supreme court ruling on this issue and its effect on pending class action dockets
6. [Massachusetts Supreme Judicial Court Rejects Use of Wiretap Statute in Data Privacy Class Action Lawsuits — Saul Ewing LLP](https://www.saul.com/insights/alert/massachusetts-supreme-judicial-court-rejects-use-wiretap-statute-data-privacy-class) -- Law firm client alert covering business implications and remaining exposure under alternative theories
7. [The Recent Massachusetts Court Holding in Vita is a Win for Businesses — Thompson Coburn LLP](https://www.thompsoncoburn.com/insights/the-recent-massachusetts-court-holding-in-vita-is-a-win-for-businesses-and-a-look-at-trends-in-novel-u-s-wiretapping-litigation/) -- Analysis of *Vita*'s value as persuasive authority in other states and trends in wiretap litigation nationally
8. [Massachusetts' Highest Court Signals Willingness to Scrutinize State Wiretapping Laws — Sidley Austin Data Matters (Oct. 30, 2024)](https://datamatters.sidley.com/2024/10/30/massachusetts-highest-court-signals-willingness-to-scrutinize-state-wiretapping-laws-and-knock-out-claims-at-the-pleading-stage/) -- Analysis of procedural significance — SJC's willingness to dismiss at pleading stage — and implications for multi-state litigation strategy
9. [Web Tracking Does Not Violate Wiretap Act, But Businesses May Not Be Totally in the Clear — Boston Bar Association](https://bostonbar.org/journal/slc-web-tracking-does-not-violate-wiretap-act-but-businesses-may-not-be-totally-in-the-clear/) -- Nuanced practitioner analysis of open questions post-*Vita*, particularly re: authenticated portals and alternative theories
10. [Massachusetts Supreme Judicial Court Rejects Wiretap Claims Based on Website Tracking — Pierce Atwood](https://www.pierceatwood.com/alerts/massachusetts-supreme-judicial-court-rejects-wiretap-claims-based-website-tracking) -- Additional law firm analysis covering implications for healthcare sector specifically
11. [Vita v. New England Baptist — EPIC](https://epic.org/documents/vita-v-new-england-baptist/) -- EPIC's case page including links to amicus brief and post-decision commentary calling for legislative action
12. [EPIC/NCLC Amicus Brief in Vita v. New England Baptist Hospital](https://epic.org/wp-content/uploads/2024/03/Vita-v-New-England-Baptist-Amicus-NCLC-EPIC.pdf) -- Full text of privacy advocacy amicus brief supporting plaintiff's broad reading of the wiretap statute
13. [Massachusetts' Top Court Rejects Privacy Arguments — EPIC (Oct. 24, 2024)](https://epic.org/massachusetts-top-court-rejects-privacy-arguments-holds-that-hospital-website-tracking-is-not-a-wiretap/) -- EPIC's post-decision statement and advocacy for legislative response
14. [Vita v. New England Baptist Hospital — U.S. Chamber of Commerce](https://www.uschamber.com/cases/privacy-and-cybersecurity/vita-v-new-england-baptist-hospital) -- Chamber's case page and summary of its amicus argument in support of defendants
15. [Greater Boston Chamber and Massachusetts Nonprofit Network Amicus Brief in Vita — Boston Chamber](https://bostonchamber.com/press-release/chamber-and-massachusetts-nonprofit-network-file-amicus-brief-in-vita-v-new-england-baptist-hospital/) -- Business community amicus participation supporting defendants
16. [Tracking Pixel Litigation Expands: A State-by-State Guide to Wiretapping Risk — National Law Review](https://natlawreview.com/article/tracking-pixel-litigation-expands-state-state-guide-wiretapping-risk) -- National survey of pixel tracking wiretap litigation risk across jurisdictions providing comparative context for the *Vita* ruling
17. [Rule of Lenity as a Shield Against Statutory Damages — National Law Review](https://natlawreview.com/article/rule-lenity-shield-against-statutory-damages-massachusetts-supreme-judicial-court) -- Analysis of the rule of lenity as the decisive analytical tool in *Vita* and its implications for other criminal-civil wiretap statutes
18. [Massachusetts General Laws c. 214, § 1B — Massachusetts Legislature](https://malegislature.gov/Laws/GeneralLaws/PartIII/TitleI/Chapter214/Section1b) -- Official text of the Massachusetts Right to Privacy statute, which remains a viable theory for plaintiffs following *Vita*
