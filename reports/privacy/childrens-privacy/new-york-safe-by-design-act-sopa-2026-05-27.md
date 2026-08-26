---
title: "New York Governor Signs Safe by Design Act (Stop Online Predators Act) into Law as Part of FY2027 Budget"
date: 2026-05-28
jurisdiction: "New York"
category: "privacy"
development_type: "legislation"
finding_id: "SCAN-20260628-028"
topic_key: "new-york-c375a464-2026"
topic_type: "state_bill"
first_reported: 2026-06-01
last_updated: 2026-06-29
status_history:
  - "2026-06-29: Revised per reviewer feedback (R1): corrected signing date to May 28; removed erroneous A10008-C budget bill citation (that bill covers transportation); corrected age coverage from 'under 17' to 'under 18'; updated California AADC section to reflect March 12, 2026 Ninth Circuit partial-injunction ruling."
cluster: "New York Safe by Design Act (Stop Online Predators Act): Minor Protection Platform Design Obligations"
cluster_slug: "new-york-safe-by-design-act-sopa-minors"
---

# New York Governor Signs Safe by Design Act (Stop Online Predators Act) into Law as Part of FY2027 Budget

**Jurisdiction:** New York | **Category:** Privacy — Children's Online Safety | **Date:** 2026-05-28

## Summary [HIGH confidence]

Governor Kathy Hochul signed the New York FY2027 budget on May 28, 2026, enacting the [Safe by Design Act](https://www.nysenate.gov/newsroom/press-releases/2026/andrew-gounardes/sen-gounardes-proposal-protect-kids-online-included) — also known as the Stop Online Predators Act (SOPA) — as part of the budget package. The law imposes affirmative platform-design obligations on social media, gaming, and user-generated content services to protect minors under 18, requiring privacy-protective defaults, parental consent flows by age tier, restrictions on AI companion features, and limits on financial transactions involving minors. Compliance obligations are triggered 180 days after the New York Attorney General promulgates implementing regulations; as of June 2026, those regulations have not been finalized, putting the operative effective date in or around early 2027.

## Key Facts [MEDIUM confidence]

- The Safe by Design Act was included in the New York FY2027 budget package signed by Governor Hochul on May 28, 2026, according to [Senator Andrew Gounardes' press release](https://www.nysenate.gov/newsroom/press-releases/2026/andrew-gounardes/sen-gounardes-proposal-protect-kids-online-included) and [Governor Hochul's budget announcement](https://www.governor.ny.gov/news/governor-hochul-secures-investments-keep-our-kids-safe-online-and-bolster-youth-mental-health).
- **Note on budget bill number:** The specific article-VII budget bill that contains SOPA could not be independently confirmed at the time of writing. An earlier draft of this report erroneously cited A10008-C; independent sources confirm A10008-C is the transportation, economic development and environmental conservation budget bill — it does not contain SOPA. The correct budget bill is likely within the Education, Labor and Family Assistance (ELFA) bill series (A10006-C/S9006-C) or another article-VII vehicle, but this has not been verified against enrolled bill text. The enrolled budget bills are available at [nyassembly.gov/2026budget](https://www.assembly.state.ny.us/2026budget/?sec=enacted) for manual verification. This section is tagged MEDIUM confidence until the correct bill number is confirmed.
- The underlying standalone bill, [S4609-A / A6549-A](https://www.nysenate.gov/legislation/bills/2025/S4609/amendment/A) (sponsored by Senator Gounardes and Assemblymember Nily Rozic), provides the substantive text for SOPA and was incorporated into the budget as budget language.

**Covered Platforms:**

- The law applies to social networks, gaming platforms with chat functions (e.g., Roblox, Discord), and user-generated content services where minors are likely to be present, per [Common Sense Media's fact sheet](https://www.commonsensemedia.org/sites/default/files/featured-content/files/safe-by-design-factsheet-updated-5.26.2026.pdf).
- Platforms must utilize a "commercially reasonable" form of age assurance to determine whether a user is a covered minor. Self-declaration (entering a birthday) is explicitly insufficient; the Attorney General's rulemaking will define qualifying methods, per [ChatForest's compliance analysis](https://chatforest.com/builders-log/ny-safe-by-design-act-sopa-children-platform-privacy-compliance-builder-guide/).

**Age Tiers and Parental Consent:**

- **Under 13:** Parental approval required for new connections; parents may view list of approved friends; parental consent required for financial transactions.
- **13–17:** Profiles set to private by default; unknown adults cannot initiate private messages with minors unless the minor accepts a friend/follow request.
- **All minors (under 18):** Non-connected adults above age 18 cannot privately communicate with minors, view full profiles, or tag minors in content; geolocation set off by default.
- Sources: [NYSenate.gov press release](https://www.nysenate.gov/newsroom/press-releases/2026/andrew-gounardes/sen-gounardes-proposal-protect-kids-online-included); [Brooklyn Paper](https://www.brooklynpaper.com/hochul-stop-online-predators-act/).

**AI Companion Restrictions:**

- AI companion systems — defined as chatbots that simulate sustained relationships, ask emotion-based questions, or maintain personal dialogue history — must be disabled by default for all minor accounts, per [ChatForest](https://chatforest.com/builders-log/ny-safe-by-design-act-sopa-children-platform-privacy-compliance-builder-guide/).
- Parents may re-enable AI companions for their children's accounts.

**Financial Safeguards:**

- Parents must approve in-platform financial transactions connected to a child's account; for users under 13, parents may also view the account's transaction history, per [Brooklyn Paper](https://www.brooklynpaper.com/hochul-stop-online-predators-act/).

**Dark Patterns and Non-Degradation:**

- Platforms may not degrade service quality or raise prices for users who choose stronger privacy protections — the privacy path must be functionally equivalent to the non-privacy path, per [ChatForest's analysis](https://chatforest.com/builders-log/ny-safe-by-design-act-sopa-children-platform-privacy-compliance-builder-guide/).
- Platforms must actively detect and prevent circumvention of age controls and parental consent mechanisms.

## Enforcement and Penalties [MEDIUM confidence]

- The New York Attorney General is the sole enforcement authority. There is no private right of action — individual users cannot sue platforms directly, per [ChatForest](https://chatforest.com/builders-log/ny-safe-by-design-act-sopa-children-platform-privacy-compliance-builder-guide/) and [IAPP](https://iapp.org/news/a/notable-ai-privacy-bills-hit-finish-line-in-illinois-connecticut-and-new-york).
- Civil penalties: up to $5,000 per violation. The AG may also seek injunctive relief.
- Penalty figures are sourced from secondary analysis (ChatForest, Brooklyn Paper) and have not been independently confirmed against official bill text at time of writing.

## Effective Date [MEDIUM confidence]

- The law takes effect 180 days after the New York Attorney General promulgates implementing regulations on age assurance methods. The AG has not finalized those regulations as of June 2026, per [ChatForest](https://chatforest.com/builders-log/ny-safe-by-design-act-sopa-children-platform-privacy-compliance-builder-guide/). Industry estimates point to early 2027, but the date is not locked.
- For comparison, the NY Attorney General released proposed rules for the related SAFE for Kids Act in 2025; that rulemaking docket — at [ag.ny.gov](https://ag.ny.gov/resources/individuals/consumer-issues/technology/protecting-children-online) — offers a reference point for how the AG approaches age assurance rulemaking under New York's children's online safety framework.

## Regulatory Context [HIGH confidence]

New York now has a layered children's online safety regulatory stack:

1. **NY SAFE for Kids Act (S7694-A, signed June 2024)** — Prohibits "addictive feeds" and nighttime push notifications for minors without parental consent. AG proposed rules issued in 2025; final rules pending. See existing reports: [New York SAFE for Kids Act — Age Signals](reports/privacy/childrens-privacy/new-york-age-signals-cdpa-safe-kids-2024-11-04.md); [NY SAFE for Kids Act ANPRM](reports/privacy/childrens-privacy/new-york-safe-kids-child-data-anprm-2024-08-19.md).
2. **NY Child Data Protection Act (S7695-A, signed June 2024)** — Limits collection and use of children's data by covered operators.
3. **NY Safe by Design Act / SOPA (FY2027 budget, signed May 28, 2026)** — This law. Adds design-default obligations, stranger-danger restrictions, AI companion controls, and parental financial oversight.

This layered framework makes New York one of the most restrictive states for platform design vis-à-vis minors, comparable to [California's Age-Appropriate Design Code Act (AB 2273)](https://kidscodecoalition.org/age-appropriate-design-codes/). The California AADC's litigation history is directly relevant to SOPA's constitutional risk: on March 12, 2026, the Ninth Circuit issued a mixed ruling on the California AADC, [partially lifting the district court's preliminary injunction](https://www.hklaw.com/en/insights/publications/2026/03/ninth-circuit-issues-mixed-ruling-on-california-age-appropriate-design). The court allowed several major provisions to take immediate effect — including the age estimation requirement, default high-privacy settings for minors, age-appropriate disclosures, and parental/child privacy tools — while sustaining the injunction as to the AADC's data-use restrictions and dark-patterns provision on constitutional vagueness grounds (finding that terms such as "materially detrimental," "best interests," and "well-being" were insufficiently definite). The partial Ninth Circuit ruling means California AADC compliance obligations are now active for a significant subset of provisions, even as litigation continues over the vagueness-enjoined provisions. This split outcome is a key data point for assessing the constitutional profile of SOPA's own design-default requirements. Other states with design-code laws enacted as of 2026 include Maryland (2024), Nebraska and Vermont (2025), and South Carolina (2026), per [Kids Code Coalition](https://kidscodecoalition.org/age-appropriate-design-codes/).

At the federal level, [KOSA (S.1748, 119th Congress)](https://www.congress.gov/bill/119th-congress/senate-bill/1748) remains pending, meaning state-by-state obligations continue to diverge. The NY Safe by Design Act is explicitly design-obligation legislation — it does not rely solely on notice-and-consent — placing it in the more demanding tier of children's privacy law.

## Action Items

- **Conduct a platform-scope assessment now.** Determine whether your service qualifies as a "covered platform" under SOPA — social networks, chat-enabled gaming services, and user-generated content services with likely minor users are all in scope. Even platforms that do not market to minors may be covered if minors are "reasonably likely" to be present.
- **Audit current age assurance mechanisms.** Self-declared birthdates are insufficient. Begin evaluating commercially reasonable alternatives (e.g., device-based signals, email verification, parental consent flows). Monitor the NY AG's rulemaking docket at [ag.ny.gov](https://ag.ny.gov/resources/individuals/consumer-issues/technology/protecting-children-online) for defined acceptable methods.
- **Review and remediate default settings.** Map all platform defaults against SOPA's requirements: private profiles for minors under 18, restricted DMs, location off, AI companions off, financial transaction limits on. Identify gaps and begin product planning for remediation.
- **Engage product and engineering teams on parental control flows by age tier.** Under-13 approval flows are distinct from 13–17 default-private and DM restriction requirements. Build age-tiered account types if not already in place.
- **Watch the AG rulemaking docket closely.** The compliance clock starts when final regulations are issued. Once rules drop, covered platforms have 180 days. Given the AG's pace on SAFE for Kids Act rules, final SOPA regulations are plausible in late 2026, triggering a mid-2027 effective date.
- **Reconcile with other NY children's privacy obligations.** SOPA operates alongside the NY SAFE for Kids Act and the Child Data Protection Act. Compliance programs should integrate all three rather than treating each in isolation.
- **Assess constitutional risk in light of the California AADC ruling.** The Ninth Circuit's March 2026 mixed ruling on the California AADC is the most current precedent: design defaults and age estimation survived First Amendment challenge, but data-use and dark-patterns restrictions were enjoined on vagueness grounds. SOPA's non-degradation and dark-patterns prohibition may face analogous challenges. Track further developments in *NetChoice v. Bonta* before finalizing remediation architecture.
- **Verify the correct FY2027 budget bill number.** The specific article-VII budget bill vehicle for SOPA has not been confirmed in this report. Before citing the enacted bill in external communications or filings, verify the correct bill number at [nyassembly.gov/2026budget](https://www.assembly.state.ny.us/2026budget/?sec=enacted).

## Related Reports

- [reports/privacy/childrens-privacy/new-york-age-signals-cdpa-safe-kids-2024-11-04.md](reports/privacy/childrens-privacy/new-york-age-signals-cdpa-safe-kids-2024-11-04.md) — Covers the earlier NY SAFE for Kids Act and Child Data Protection Act, which form the first layer of New York's children's privacy stack that SOPA now expands.
- [reports/privacy/childrens-privacy/new-york-safe-kids-child-data-anprm-2024-08-19.md](reports/privacy/childrens-privacy/new-york-safe-kids-child-data-anprm-2024-08-19.md) — NY AG's advance notice of proposed rulemaking for SAFE for Kids Act age assurance; the same rulemaking framework governs SOPA's pending regulations.
- [reports/privacy/childrens-privacy/california-sb976-social-media-addiction-rulemaking-2026-06-01.md](reports/privacy/childrens-privacy/california-sb976-social-media-addiction-rulemaking-2026-06-01.md) — California's parallel children's social media addiction law and its active rulemaking, relevant for organizations managing multi-state children's privacy compliance.
- [reports/privacy/childrens-privacy/colorado-sb26051-michigan-kids-code-age-verification-2026-05-08.md](reports/privacy/childrens-privacy/colorado-sb26051-michigan-kids-code-age-verification-2026-05-08.md) — Colorado and Michigan age-verification bills; comparable state-level design-obligation legislation advancing in parallel.
- [reports/privacy/state-comprehensive-laws/illinois-ct-ny-ai-privacy-bills-2026-05-28.md](reports/privacy/state-comprehensive-laws/illinois-ct-ny-ai-privacy-bills-2026-05-28.md) — The multi-state wave report that briefly covers NY Safe by Design alongside Illinois and Connecticut AI/privacy laws passed in the same legislative sprint.

## Sources

1. [Sen. Gounardes' Proposal to Protect Kids Online Included in State Budget — NYSenate.gov](https://www.nysenate.gov/newsroom/press-releases/2026/andrew-gounardes/sen-gounardes-proposal-protect-kids-online-included) — Official NY Senate press release confirming SOPA's inclusion in the FY2027 budget; primary legislative source.
2. [Governor Hochul Secures Investments to Keep Our Kids Safe Online — Governor.ny.gov](https://www.governor.ny.gov/news/governor-hochul-secures-investments-keep-our-kids-safe-online-and-bolster-youth-mental-health) — Governor's office announcement of SOPA inclusion in the FY2027 budget; confirms signing and scope.
3. [2026-2027 Enacted Budget — New York State Assembly](https://www.assembly.state.ny.us/2026budget/?sec=enacted) — Landing page for all enrolled FY2027 budget bill texts; provided for manual verification of the correct article-VII bill number containing SOPA.
4. [NY State Senate Bill 2025-S4609A — nysenate.gov](https://www.nysenate.gov/legislation/bills/2025/S4609/amendment/A) — Standalone Senate bill (Stop Online Predators Act) incorporated into the budget; substantive bill text.
5. [Common Sense Media — New York Safe by Design Act Fact Sheet (PDF)](https://www.commonsensemedia.org/sites/default/files/featured-content/files/safe-by-design-factsheet-updated-5.26.2026.pdf) — Updated May 26, 2026 fact sheet summarizing key SOPA provisions; used as corroboration for coverage and default-settings requirements.
6. [Common Sense Media Applauds New Kids' Online Safety Victory in New York](https://www.commonsensemedia.org/press-releases/common-sense-media-applauds-new-kids-online-safety-victory-in-new-york) — Advocacy organization press release confirming SOPA signing and welcoming the law.
7. [NY Safe by Design Act (SOPA): What Platform Builders Must Do Before the ~Early 2027 Effective Date — ChatForest](https://chatforest.com/builders-log/ny-safe-by-design-act-sopa-children-platform-privacy-compliance-builder-guide/) — Detailed compliance guide covering effective date, age-tier requirements, AI companion rules, enforcement, and dark patterns prohibition. Secondary/analysis source.
8. [Notable AI, Privacy Bills Hit Finish Line in Illinois, Connecticut and New York — IAPP](https://iapp.org/news/a/notable-ai-privacy-bills-hit-finish-line-in-illinois-connecticut-and-new-york) — IAPP overview of the 2026 state legislative sprint including NY Safe by Design; authoritative trade publication.
9. [Hochul Backs Stop Online Predators Act in 2026 Budget — Brooklyn Paper](https://www.brooklynpaper.com/hochul-stop-online-predators-act/) — Local coverage confirming age tiers, parental financial controls, and Governor's backing.
10. [Sen. Gounardes' Proposal to Protect Kids Online — State of the State Preview](https://www.nysenate.gov/newsroom/press-releases/2026/andrew-gounardes/sen-gounardes-bill-protect-kids-online-will-be) — Earlier press release confirming Governor Hochul's State of the State support for SOPA.
11. [Governor Hochul Announces New York Received Highest Ranking for Technology Laws Keeping Kids Safe Online](https://www.governor.ny.gov/news/governor-hochul-announces-new-york-state-received-highest-nation-ranking-technology-laws) — Governor's office press release situating SOPA within NY's broader children's safety law posture.
12. [Kids Code Coalition — New York](https://kidscodecoalition.org/new-york/) — Coalition tracker covering New York's children's online design obligations including SOPA.
13. [Age-Appropriate Design Codes — Kids Code Coalition](https://kidscodecoalition.org/age-appropriate-design-codes/) — State-by-state tracker of AADC-model laws; used for comparative state context.
14. [Protecting Children Online — New York State Attorney General](https://ag.ny.gov/resources/individuals/consumer-issues/technology/protecting-children-online) — AG's consumer resource page; relevant for monitoring SOPA rulemaking.
15. [KOSA S.1748 — 119th Congress — Congress.gov](https://www.congress.gov/bill/119th-congress/senate-bill/1748) — Federal KOSA bill status; cited for federal/state landscape context.
16. [Proposed State Privacy and AI Law Update: June 1, 2026 — Troutman Privacy](https://www.troutmanprivacy.com/2026/05/proposed-state-privacy-and-ai-law-update-june-1-2026/) — Primary finding source; law firm blog post confirming NY Safe by Design Act enactment.
17. [Ninth Circuit Issues Mixed Ruling on California Age-Appropriate Design Code Act — Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/03/ninth-circuit-issues-mixed-ruling-on-california-age-appropriate-design) — Analysis of the March 12, 2026 Ninth Circuit ruling partially lifting the AADC injunction; cited for constitutional context.
18. [Ninth Circuit Partially Lifts Injunction Against California Age-Appropriate Design Code Act — Alston & Bird](https://www.alstonprivacy.com/ninth-circuit-partially-lifts-injunction-against-california-age-appropriate-design-code-act/) — Additional analysis of the March 2026 Ninth Circuit ruling; corroborates Holland & Knight account.
