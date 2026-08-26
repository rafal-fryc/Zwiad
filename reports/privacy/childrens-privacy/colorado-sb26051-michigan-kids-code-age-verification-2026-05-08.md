---
title: "Colorado Passes OS-Level Age Attestation Law; Michigan Kids Code Advances to House"
date: 2026-05-08
jurisdiction: "Colorado"
category: "privacy"
development_type: "legislation"
finding_id: "SCAN-20260508-032"
topic_key: "colorado-c8bdb7a2-2026"
topic_type: "state_bill"
first_reported: 2026-05-05
last_updated: 2026-05-08
status_history:
  - "2026-05-08: Reviewer r1 corrections applied — Michigan vote date fixed (Apr 30 -> Apr 29), Polis veto clarified (SB 25-086, not age verification), COPPA dates corrected (compliance deadline Apr 22 2026 / effective Jun 23 2025), Colorado vote sequence corrected, Republican crossovers (Huizenga, McBroom) noted."
  - "2026-05-08: Reviewer r2 correction applied — SB 25-201 fate corrected: passed Senate H&HS committee 8-1 but stalled on Senate floor (sponsors postponed pending Supreme Court ruling on Texas age verification law); did not fail in committee."
cluster: "State OS-Level Age Verification Laws: Colorado SB 26-051 and Related Bills (2026)"
cluster_slug: "state-os-level-age-verification-laws-2026"
---

# Colorado Passes OS-Level Age Attestation Law; Michigan Kids Code Advances to House

**Jurisdiction:** Colorado, Michigan (multi-state) | **Category:** Privacy — Children's Online Safety | **Date:** 2026-05-08

## Summary [HIGH confidence]

Colorado's legislature passed [SB26-051](https://leg.colorado.gov/bills/SB26-051), the Age Attestation on Computing Devices Act, on May 1, 2026, becoming the first state to mandate operating-system-level age verification rather than placing that burden on individual websites or apps. The bill — cleared by the Senate on May 1, 2026 — voting 33-0 to concur with House amendments and 26-9 to repass the enrolled bill — now awaits Governor Jared Polis's signature; if signed, it takes effect January 1, 2028. Simultaneously, Michigan's Senate passed the four-bill "Kids Over Clicks" package (SB 757-760) on April 29, 2026, by a 20-17 vote, including the [Michigan Kids Code Act](https://www.michiganvotes.org/legislation/2025/senate/bill-758) (SB 758-759), which now moves to the Republican-controlled House. Together, these actions mark a significant escalation in state-level children's online safety legislation during the 2026 legislative season.

## Key Facts [HIGH confidence]

- Colorado SB26-051 requires operating system providers (Apple, Google, Microsoft, and Linux distributions) to collect users' date of birth or age at account setup and generate a standardized age-bracket signal — under 13, 13-16, 16-18, or 18 and above — made available to app developers through a real-time API, according to the [Colorado General Assembly bill text](https://leg.colorado.gov/bills/SB26-051).
- App developers accessing covered application stores (i.e., major app stores) must query and rely on that age signal as the primary proof of a user's age, and are prohibited from collecting age data separately or passing the signal to third parties for unrelated purposes, per the [official bill language](https://leg.colorado.gov/bill_files/110990/download).
- Civil penalties under SB26-051 are up to **$2,500 per minor** for negligent violations and up to **$7,500 per minor** for intentional violations, effective January 1, 2028, per [legislative analysis](https://leg.colorado.gov/bills/SB26-051).
- The approach is novel: prior age verification statutes in Texas and Utah placed obligations directly on websites, raising First Amendment concerns and prompting litigation; Colorado's OS-level model attempts to move compliance to the infrastructure layer, as noted by [Biometric Update](https://www.biometricupdate.com/202602/colorado-moves-age-checks-from-websites-to-operating-systems).
- Governor Polis vetoed [SB 25-086](https://leg.colorado.gov/bills/SB25-086) in 2025 — a social media accountability and moderation bill requiring platforms to remove flagged accounts — not an age verification measure; the separate 2025 age verification bill (SB 25-201) stalled on the Senate floor — sponsors postponed it pending a Supreme Court ruling on a similar Texas law — and did not reach his desk. SB26-051's enrollment status as of May 8, 2026 is not yet confirmed by an official governor's office press release. Official text could not be confirmed as signed at time of writing; the expected status page for manual verification is: [leg.colorado.gov/bills/SB26-051](https://leg.colorado.gov/bills/SB26-051).
- Michigan's Kids Over Clicks package comprises four bills: **SB 757** (SAFE for Kids Act — prohibits algorithmically driven, personal-data-based social media feeds to minors without parental consent), **SB 758-759** (Michigan Kids Code — bans targeted advertising to children, mandates privacy-by-default settings, expands parental controls, restricts push notifications during school hours and overnight; effective July 1, 2026 if enacted), and **SB 760** (LEAD for Kids Act — restricts AI companion chatbots accessible to children), according to the [Kids Code Coalition announcement](https://kidscodecoalition.org/2026/04/michigan-senate-passes-kids-over-clicks-youth-online-safety-package/) and [Michigan Senate Democrats](https://senatedems.com/kids-over-clicks/).
- The Michigan Senate vote of 20-17 was primarily along party lines (Dems control the Senate), though two Republican senators — Huizenga and McBroom — crossed party lines to vote in favor of the package; the bills now face a Republican-controlled House, where prospects are uncertain, per [Michigan Advance](https://michiganadvance.com/2026/05/01/logging-off-how-michigan-is-prioritizing-kids-over-clicks/).
- The Troutman Pepper Locke state privacy roundup (May 4, 2026, 16th installment) also noted a Minnesota lawmaker introduced **SF 5221** to regulate processing of geolocation data, per [JDSupra](https://www.jdsupra.com/legalnews/proposed-state-privacy-law-update-may-4-5954451/).

## Key Provisions Comparison [HIGH confidence]

| Feature | Colorado SB26-051 | Michigan Kids Code (SB 758-759) |
|---|---|---|
| Mechanism | OS-level age-bracket API signal | Platform-side safety requirements |
| Minimum age protected | Under 13 (strictest tier) / under 18 | Under 18 |
| Advertising to minors | Prohibited (app cannot receive minor signal and serve targeted ads) | Explicitly banned |
| Parental controls | Parental account linkage at OS level | Expanded parental account controls required |
| Notifications | App must comply with child-safety laws once it receives signal | Prohibited overnight and during school hours |
| Penalties | $2,500-$7,500 per minor per violation | Codified under Michigan Consumer Protection Act (SB 759) |
| Effective date | January 1, 2028 (if signed) | July 1, 2026 (if enacted) |
| Legislative status (May 8, 2026) | Passed both chambers; awaiting governor | Passed Senate; in House committee |

## Legal and Constitutional Context [MEDIUM confidence]

Colorado's OS-layer architecture was deliberately designed to sidestep the First Amendment vulnerabilities identified when states (Texas, Utah) tried to mandate age verification at the point of content access. By placing the obligation on device OS providers rather than content publishers, the bill's sponsors argue it does not restrict access to lawful speech. Critics, however, note that the bill still creates a comprehensive age-profiling infrastructure that could chill anonymous internet use; moreover, the constitutional question for OS-level mandates remains untested in federal courts. The [Complete Colorado editorial board](https://completecolorado.com/2026/02/17/colorado-senate-bill-51-online-age-verification-illusion-of-safety/) argued the measure creates "the illusion of safety" because minors can bypass app-store controls via web browsers, a vector SB26-051 does not address. Related federal litigation paused the Colorado AI Act (SB 24-205) on April 27, 2026 — a reminder that state digital regulation continues to attract constitutional challenge.

Michigan's Kids Over Clicks package follows a design-standard model closer to the UK Age-Appropriate Design Code, which has survived legal challenge more successfully than access-restriction models. The Michigan approach places obligations on platform operators rather than OS providers or users, aligning with [state children's online safety frameworks](https://www.multistate.us/insider/2026/4/30/state-childrens-online-safety-laws-expand-beyond-social-media-in-2026) enacted by Maryland, California, Nebraska, and Vermont in prior years.

## Action Items

- **App store operators and OS developers (Apple, Google, Microsoft):** If Colorado SB26-051 is signed, begin technical design work for age-bracket API infrastructure immediately — January 1, 2028 is the compliance deadline but OS-level changes require multi-year integration lead times.
- **App developers distributing via covered application stores in Colorado:** Review app store distribution agreements; plan to implement calls to the new age-signal API and update data minimization practices to prohibit collection of independent age data once the law takes effect.
- **Digital platforms with Michigan users (social media, advertising, AI chatbot services):** Track Michigan HB progress; if enacted, SB 758-759 would impose July 1, 2026 compliance deadlines for default privacy settings, targeted advertising prohibitions, and parental consent mechanisms — no grace period.
- **Counsel and compliance teams:** Monitor Governor Polis's action on SB26-051; his 2025 veto of a prior age verification bill creates uncertainty. Engage state-specific tracking on the Colorado General Assembly bill status page.
- **All covered entities:** Note that the FTC's updated COPPA Rule (compliance deadline April 22, 2026; rule legally effective June 23, 2025) layers federal obligations on top of state laws. Colorado and Michigan measures do not preempt COPPA; compliance with both will be required.
- **Policy teams:** The Troutman Pepper Locke roundup (16th installment) tracks over 20 active state children's privacy bills in 2026; a unified tracking system is advisable given the volume and pace of enactment.

## Related Reports

- [reports/privacy/childrens-privacy/coppa-amendments-compliance-deadline-2026-04-13.md](../coppa-amendments-compliance-deadline-2026-04-13.md) -- FTC's updated COPPA Rule took effect April 22, 2026; creates federal baseline obligations that Colorado and Michigan measures supplement.
- [reports/privacy/childrens-privacy/federal-coppa-enforcement-begins-2026-05-04.md](../federal-coppa-enforcement-begins-2026-05-04.md) -- FTC begins enforcing the 2025 COPPA amendments, directly relevant to the same class of platforms targeted by Colorado and Michigan bills.
- [reports/privacy/childrens-privacy/arkansas-act900-addictive-design-injunction-2026-04-22.md](../arkansas-act900-addictive-design-injunction-2026-04-22.md) -- Federal court blocked Arkansas's social media safety law targeting addictive design; illustrates constitutional risk for design-mandate statutes like Michigan's.
- [reports/privacy/childrens-privacy/maryland-aadc-kids-code-modpa-2024-05-15.md](../maryland-aadc-kids-code-modpa-2024-05-15.md) -- Maryland's Age-Appropriate Design Code and Kids Code, the model that Michigan's Kids Code builds on.
- [reports/privacy/childrens-privacy/new-york-age-signals-cdpa-safe-kids-2024-11-04.md](../new-york-age-signals-cdpa-safe-kids-2024-11-04.md) -- New York's approach to age signals under its children's privacy laws, providing comparative context for Colorado's OS-level signal model.
- [reports/privacy/state-comprehensive-laws/colorado-cpa-rules-biometric-minors-opinion-letters-2025-01.md](../../state-comprehensive-laws/colorado-cpa-rules-biometric-minors-opinion-letters-2025-01.md) -- Colorado CPA rules on biometric data and minors, directly relevant to SB26-051's data minimization requirements.

## Sources

1. [SB26-051 Age Attestation on Computing Devices — Colorado General Assembly](https://leg.colorado.gov/bills/SB26-051) -- Official bill page with legislative history and vote records; primary source for SB26-051 status and provisions.
2. [SB26-051 Official Bill Text — Colorado General Assembly](https://leg.colorado.gov/bill_files/110990/download) -- Full enrolled bill text with operative provisions and penalty structure.
3. [Colorado Moves Age Checks From Websites to Operating Systems — Biometric Update](https://www.biometricupdate.com/202602/colorado-moves-age-checks-from-websites-to-operating-systems) -- Technical and policy analysis of SB26-051's OS-layer approach and comparison to prior state models.
4. [SB051 Legislative Tracking — Legiscan](https://legiscan.com/CO/bill/SB051/2026) -- Third-party tracking confirming Senate concurrence on May 1, 2026.
5. [Senate Bill 51: Online Age Verification and the Illusion of Safety — Complete Colorado](https://completecolorado.com/2026/02/17/colorado-senate-bill-51-online-age-verification-illusion-of-safety/) -- Critical analysis of enforcement gaps (web browser bypass) and constitutional concerns.
6. [Michigan Senate Passes Kids Over Clicks Youth Online Safety Package — Kids Code Coalition](https://kidscodecoalition.org/2026/04/michigan-senate-passes-kids-over-clicks-youth-online-safety-package/) -- Advocacy group summary of Senate passage, bill-by-bill breakdown, and vote counts.
7. [Logging Off: How Michigan Is Prioritizing 'Kids Over Clicks' — Michigan Advance](https://michiganadvance.com/2026/05/01/logging-off-how-michigan-is-prioritizing-kids-over-clicks/) -- Detailed reporting on legislative dynamics, House prospects, and Democratic-Republican dynamics.
8. [Kids Over Clicks — Michigan Senate Democrats](https://senatedems.com/kids-over-clicks/) -- Sponsor-facing summary of the four-bill package, provisions, and legislative intent.
9. [SB 758 — MichiganVotes](https://www.michiganvotes.org/legislation/2025/senate/bill-758) -- Official Michigan Legislature bill tracking for the Kids Code (SB 758).
10. [Proposed State Privacy Law Update: May 4, 2026 — Troutman Pepper Locke via JDSupra](https://www.jdsupra.com/legalnews/proposed-state-privacy-law-update-may-4-5954451/) -- Primary source digest confirming Colorado passage, Michigan Senate passage, and Minnesota SF 5221 introduction; 16th roundup installment.
11. [State Children's Online Safety Laws Expand to AI Chatbots — MultiState](https://www.multistate.us/insider/2026/4/30/state-childrens-online-safety-laws-expand-beyond-social-media-in-2026) -- Broad survey of 2026 state legislative activity in children's online safety, providing national context.
12. [Senate Bills 757-760 Analysis — Michigan Legislature (PDF)](https://www.legislature.mi.gov/documents/2025-2026/billanalysis/Senate/pdf/2025-SFA-0757-G.pdf) -- Official Michigan Senate Fiscal Agency analysis of the full Kids Over Clicks package.
