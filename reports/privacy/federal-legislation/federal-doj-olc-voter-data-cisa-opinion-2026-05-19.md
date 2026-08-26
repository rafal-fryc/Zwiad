---
title: "DOJ OLC Opinion Claims Broad Federal Authority to Obtain State Voter Registration Data; States and Courts Push Back"
date: 2026-05-14
jurisdiction: "Federal"
category: "privacy"
development_type: "guidance"
finding_id: "SCAN-20260519-033"
topic_key: "CISA-DOJ-ISSUES-OPINION-ON-GOVERNME-2026"
topic_type: "guidance"
first_reported: 2026-05-14
last_updated: 2026-05-19
status_history: []
cluster: "DOJ OLC Voter Roll Data Opinion: Federal Authority vs. State Privacy Laws"
cluster_slug: "doj-olc-voter-roll-data-federal-authority"
---

# DOJ OLC Opinion Claims Broad Federal Authority to Obtain State Voter Registration Data; States and Courts Push Back

**Jurisdiction:** Federal | **Category:** Privacy | **Date:** 2026-05-14

## Summary [HIGH confidence]

On May 12, 2026, the Department of Justice Office of Legal Counsel (OLC) issued a slip opinion titled "Authority to Obtain and Share Statewide Voter Roll Data," providing formal legal justification for the federal government's nationwide demands that states hand over unredacted voter registration files — including partial Social Security numbers, driver's license numbers, and birthdates. The opinion concludes that the Civil Rights Act of 1960, reinforced by HAVA, the NVRA, and the Voting Rights Act, authorizes the DOJ to compel state production of these records and to share them with DHS's immigration enforcement apparatus. Privacy professionals must understand that the opinion directly disputes that the Privacy Act, Driver's Privacy Protection Act, or any state privacy law can block federal access to voter rolls. Multiple federal courts have already rejected this theory, and more than 30 states are currently engaged in active litigation resisting the demands.

## Key Facts [HIGH confidence]

- The OLC opinion, dated May 12, 2026 and publicly released shortly thereafter, memorialized legal advice the office had already provided to the DOJ Civil Rights Division in September 2025, according to [CyberScoop](https://cyberscoop.com/federal-voter-data-collection-doj-legal-memo/).
- The opinion grounds DOJ's compulsion authority in two interlocking provisions of the [Civil Rights Act of 1960](https://www.justice.gov/olc/media/1440346/dl): Section 301 (52 U.S.C. § 20701), which requires election officials to retain voter records for 22 months after a federal election; and Section 303 (52 U.S.C. § 20703), which grants the Attorney General the authority to inspect and copy those retained records upon written demand. The opinion reads Section 303's demand-and-inspect authority as permitting DOJ to obtain full copies of the retained rolls. It supplements that basis with citations to the Help America Vote Act (HAVA), the National Voter Registration Act (NVRA), and the Voting Rights Act of 1965.
- The opinion expressly concludes that the Privacy Act of 1974, the Driver's Privacy Protection Act, and the E-Government Act do not restrict DOJ's authority to collect or share voter roll data, and that "[n]o state is entitled to withhold responsive materials based on privacy or confidentiality provisions found in state law," per [CyberScoop's reporting on the memo](https://cyberscoop.com/federal-voter-data-collection-doj-legal-memo/).
- The OLC opinion authorizes DOJ to share collected voter data with DHS, specifically to run it through DHS's SAVE (Systematic Alien Verification for Entitlements) program to check for noncitizens on voter rolls, according to [NPR](https://www.npr.org/2026/04/03/nx-s1-5768455/privacy-doj-dhs-voter-data).
- At least 48 states and Washington, D.C. have received DOJ demands for complete voter registration lists. At least 15 states — predominantly Republican-led — have provided full unredacted rolls, while the majority have resisted, per the [Brennan Center's tracker](https://www.brennancenter.org/our-work/research-reports/tracker-justice-department-requests-voter-information).
- The DOJ has filed federal lawsuits against 30 states and D.C. seeking to compel production, per the [University of Wisconsin Law School's State Democracy Research Initiative tracker](https://statedemocracy.law.wisc.edu/our-work/tracker-doj-lawsuits-seeking-states-sensitive-voter-data).
- Federal courts have dismissed DOJ lawsuits on the merits in California, Michigan, Oregon, Massachusetts, Rhode Island, and Arizona. The DOJ has appealed dismissals in California, Oregon, and Michigan, according to [Democracy Docket](https://www.democracydocket.com/news-alerts/doj-voter-roll-grab-court-sounds-skeptical-of-trump-bid-for-michigan-data/). A separate DOJ suit against Georgia was dismissed solely on venue grounds — the case was filed in the Middle District of Georgia when it should have been filed in the Northern District — and does not reflect a ruling on the merits; DOJ immediately refiled in the correct district and the Georgia litigation is ongoing, per [Democracy Docket](https://www.democracydocket.com/news-alerts/after-filing-in-wrong-court-doj-refiles-lawsuit-seeking-georgia-voter-rolls/) and the [Georgia Recorder](https://georgiarecorder.com/2026/01/23/federal-judge-tosses-out-doj-lawsuit-seeking-sensitive-voter-data-in-georgia/).
- Kilian Kagle, the chief FOIA officer and senior privacy official for DOJ's Civil Rights Division, resigned amid the data collection effort. DOJ has not issued the public notices or Privacy Impact Assessments that federal law requires before collecting or disseminating personal data for a new purpose, per [NPR](https://www.npr.org/2026/04/03/nx-s1-5768455/privacy-doj-dhs-voter-data).
- The Brennan Center has identified serious security deficiencies in DOJ's proposed data transfer agreements: password-only (no multifactor) authentication, inadequate encryption, no data minimization requirements, and a DOJ plan to "archive" rather than destroy collected data, creating a permanent federal voter registry, per the [Brennan Center's security analysis](https://www.brennancenter.org/our-work/analysis-opinion/justice-departments-security-measures-collecting-voter-rolls-are).
- Election law scholar Justin Levitt, writing at the [Election Law Blog](https://electionlawblog.org/?p=156170), disputes the opinion's conclusion that a non-citizen finding gives the Civil Rights Division authority to remove individual voter records, arguing the proper authority is referral for prosecution — not unilateral record removal.

## Action Items

- **Assess state-specific exposure immediately.** Organizations in states that have provided or are likely to provide voter rolls should map what personal data was shared and consider notifying affected individuals where applicable under state breach notification or privacy laws.
- **Monitor litigation outcomes closely.** Six federal courts have dismissed DOJ's compulsion suits on the merits. If appellate courts affirm those dismissals, the OLC opinion's legal basis will be significantly eroded. Track appeals in the Ninth and Sixth Circuits and watch the Georgia case now proceeding in the Northern District.
- **Do not treat the OLC opinion as binding on states.** OLC opinions bind executive branch agencies but are not binding on states, courts, or Congress. Organizations advising state election agencies should note that courts have not accepted this legal theory.
- **Evaluate Privacy Impact Assessment gaps.** The DOJ has not issued required Privacy Act notices or PIAs for this data collection. If your organization has contracts or data-sharing arrangements with DOJ, assess whether the collection triggers your own privacy obligations under applicable laws.
- **Assess re-identification and downstream sharing risks.** The OLC opinion explicitly permits DOJ to share voter data with DHS for immigration enforcement. Organizations handling voter data should anticipate that any data provided to DOJ may be disclosed to other federal agencies without further notice.
- **Prepare for a permanent federal voter registry risk scenario.** DOJ's stated intent to archive rather than delete collected data means sensitive voter PII may persist indefinitely in federal systems with documented security weaknesses. Consider whether your organization should file amicus briefs or join advocacy efforts in pending litigation.

## Related Reports

- [reports/privacy/federal-ice-domestic-surveillance-tools-2026-05-04.md](reports/privacy/federal-ice-domestic-surveillance-tools-2026-05-04.md) -- ICE's expansion of domestic surveillance tools, including data broker contracts, directly parallels the DOJ effort to aggregate voter PII for immigration enforcement cross-referencing.
- [reports/privacy/financial-privacy/federal-bank-citizenship-data-eo-2026-04-19.md](reports/privacy/financial-privacy/federal-bank-citizenship-data-eo-2026-04-19.md) -- Treasury's parallel initiative to collect bank customer citizenship data reflects the same broad federal drive to aggregate citizenship-related personal data across government databases.
- [reports/privacy/federal-legislation/fisa-section-702-renewal-2026-04-13.md](reports/privacy/federal-legislation/fisa-section-702-renewal-2026-04-13.md) -- FISA 702 reauthorization debates raise related questions about federal government access to personal data and oversight mechanisms for mass data collection programs.

## Sources

1. [DOJ OLC Slip Opinion: Authority to Obtain and Share Statewide Voter Roll Data (justice.gov)](https://www.justice.gov/olc/media/1440346/dl) -- Official OLC slip opinion; primary legal text for this development.
2. [DOJ releases legal rationale for nationwide voter data collection (CyberScoop)](https://cyberscoop.com/federal-voter-data-collection-doj-legal-memo/) -- Detailed reporting on the OLC memo's content, legal reasoning, and implications.
3. [US Justice Department Drafts Legal Opinion Backing Demands for State Voter Rolls (US News/Reuters)](https://www.usnews.com/news/politics/articles/2026-05-13/us-justice-department-drafts-legal-opinion-backing-demands-for-state-voter-rolls) -- Wire report on the opinion's May 12, 2026 release and non-binding nature.
4. [The OLC opinion on the voter file demands (Election Law Blog)](https://electionlawblog.org/?p=156170) -- Analysis by Justin Levitt disputing key OLC legal conclusions regarding voter record removal authority.
5. [As DOJ prepares to share state voter data with DHS, a key privacy officer resigns (NPR)](https://www.npr.org/2026/04/03/nx-s1-5768455/privacy-doj-dhs-voter-data) -- Reports on the Civil Rights Division privacy officer's resignation and missing Privacy Act notices.
6. [Tracker of Justice Department Requests for Voter Information (Brennan Center for Justice)](https://www.brennancenter.org/our-work/research-reports/tracker-justice-department-requests-voter-information) -- Interactive tracker showing state-by-state compliance and resistance status.
7. [The Justice Department's Security Measures for Collecting Voter Rolls Are Inadequate (Brennan Center for Justice)](https://www.brennancenter.org/our-work/analysis-opinion/justice-departments-security-measures-collecting-voter-rolls-are) -- Security analysis identifying encryption, access control, and data retention deficiencies.
8. [DOJ voter roll grab: Court sounds skeptical of Trump bid for Michigan data (Democracy Docket)](https://www.democracydocket.com/news-alerts/doj-voter-roll-grab-court-sounds-skeptical-of-trump-bid-for-michigan-data/) -- Reports on judicial skepticism and dismissals in multiple states.
9. [Tracker: DOJ Lawsuits Seeking States' Sensitive Voter Data (University of Wisconsin Law School)](https://statedemocracy.law.wisc.edu/our-work/tracker-doj-lawsuits-seeking-states-sensitive-voter-data) -- Comprehensive tracker of all DOJ voter data lawsuits filed against states.
10. [Trump Administration Has Sued More than 20 States for Refusing to Turn Over Voter Files (Brennan Center for Justice)](https://www.brennancenter.org/our-work/analysis-opinion/trump-administration-has-sued-more-20-states-refusing-turn-over-voter) -- Overview of DOJ litigation posture and scope of federal demands.
11. [States are right to push back on the DOJ's pursuit of voter data (StateScoop)](https://statescoop.com/states-doj-voter-data/) -- State-level technology and policy analysis of the legal and cybersecurity concerns.
12. [Court dismisses DOJ's Georgia voter roll lawsuit because it filed in the wrong district (Democracy Docket)](https://www.democracydocket.com/news-alerts/court-dismisses-dojs-georgia-voter-roll-lawsuit-because-it-filed-in-the-wrong-district/) -- Reports Judge Royal's venue-only dismissal of the Middle District of Georgia suit.
13. [After filing in wrong court, DOJ refiles lawsuit seeking Georgia voter rolls (Democracy Docket)](https://www.democracydocket.com/news-alerts/after-filing-in-wrong-court-doj-refiles-lawsuit-seeking-georgia-voter-rolls/) -- Confirms DOJ refiling in the Northern District of Georgia; Georgia litigation continues.
14. [Federal judge tosses out DOJ lawsuit seeking Georgia voter rolls (Georgia Recorder)](https://georgiarecorder.com/2026/01/23/federal-judge-tosses-out-doj-lawsuit-seeking-sensitive-voter-data-in-georgia/) -- Georgia Recorder reporting on the venue dismissal and DOJ's prompt refiling.
