---
finding_id: "SCAN-20260407-007"
format: "client-alert"
date: "2026-04-07"
jurisdiction: "California"
category: "privacy"
development_type: "enforcement"
---

# California Privacy Protection Agency Issues $1.1 Million Fine Against PlayOn Sports for CCPA Student Privacy Violations

**Jurisdiction:** California | **Category:** Privacy | **Date:** 2026-04-07

## Summary [HIGH confidence]

On March 3, 2026, the California Privacy Protection Agency (CPPA) Board issued its first enforcement decision involving student privacy, fining PlayOn Sports $1.1 million for multiple CCPA violations related to its GoFan ticketing platform used by approximately 1,400 California schools. <!-- verified --> The decision establishes critical precedent that directing consumers to third-party industry opt-out tools (such as the Network Advertising Initiative or Digital Advertising Alliance) does not satisfy CCPA opt-out requirements, and that "agree-to-enter" consent walls for tracking technologies violate the statute. <!-- verified -->

## Key Facts [HIGH confidence]

- PlayOn Sports operates the GoFan platform, which provides digital ticketing, streaming, and fundraising services to approximately 1,400 California schools for high school sporting events, theater performances, and dances ([CPPA Press Release](https://privacy.ca.gov/2026/03/youth-sports-media-company-to-pay-1-1-million-fine-change-practices-over-privacy-violations/)) <!-- verified -->

- During January 1, 2023 through December 31, 2024, PlayOn collected personal information using first- and third-party cookies, persistent trackers, and technologies such as MetaPixel for targeted advertising, constituting "sale" and "sharing" of personal information under the CCPA ([Holland & Knight Analysis](https://www.hklaw.com/en/insights/publications/2026/03/calprivacy-fines-playon-sports-1-1m-for-ccpa-opt-out-and-notice)) <!-- verified -->

- PlayOn deployed consent banners offering only an "Agree" option; on mobile devices, the banner covered the screen area needed to redeem tickets, effectively forcing consumers to consent to tracking to use tickets they had already purchased ([CPPA Press Release](https://privacy.ca.gov/2026/03/youth-sports-media-company-to-pay-1-1-million-fine-change-practices-over-privacy-violations/)) <!-- verified -->

- PlayOn directed consumers to opt out through the NAI and DAA rather than providing its own compliant opt-out mechanism; the CPPA ruled this does not satisfy CCPA requirements under [Cal. Civ. Code Section 1798.120](https://codes.findlaw.com/ca/civil-code/civ-sect-1798-120/) (consumer right to opt out of sale/sharing) and [Section 1798.135](https://codes.findlaw.com/ca/civil-code/civ-sect-1798-135/) (business obligation to provide opt-out mechanisms) ([Hunton Andrews Kurth Analysis](https://www.hunton.com/privacy-and-cybersecurity-law-blog/calprivacy-issues-1-1-million-fine-for-ccpa-violations-involving-student-privacy)) <!-- verified: corrected per reviewer feedback; now references both relevant sections with correct URLs -->

- PlayOn failed to honor opt-out preference signals such as Global Privacy Control, violating [Cal. Civ. Code Section 1798.135](https://codes.findlaw.com/ca/civil-code/civ-sect-1798-135/) and [11 CCR Section 7025](https://www.law.cornell.edu/regulations/california/11-CCR-7025) ([Inside Privacy / Covington Analysis](https://www.insideprivacy.com/state-privacy/calprivacy-fines-playon-sports-for-insufficient-opt-out-process/)) <!-- verified -->

- The settlement requires PlayOn to comply with the CCPA's prohibition on selling or sharing personal information of consumers aged 13-16 without affirmative opt-in consent, though the decision did not make a specific finding that PlayOn violated these minor-specific protections ([CPPA Press Release](https://privacy.ca.gov/2026/03/youth-sports-media-company-to-pay-1-1-million-fine-change-practices-over-privacy-violations/); [Loeb & Loeb Analysis](https://www.loeb.com/en/insights/publications/2026/03/calprivacy-playon-sports-enforcement)) <!-- verified: corrected per reviewer feedback; multiple law firm analyses confirm the decision did not find a minor-specific violation -->

- PlayOn's privacy notice had not been updated since July 2022 — over two and a half years — failing to meet the CCPA requirement to update privacy policies at least annually. The notice also failed to inform consumers of their right to opt out of "sharing" and incorrectly stated that PlayOn did not "sell" personal information ([WilmerHale Analysis](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20260319-youth-sports-media-company-to-pay-1-10-million-fine-in-cppa-enforcement-action)) <!-- verified: corrected per reviewer feedback; duration now accurately reflects sources -->

## Settlement Terms [HIGH confidence] [VERIFIED]

- **$1.1 million monetary penalty** payable to the state ([CPPA Press Release](https://privacy.ca.gov/2026/03/youth-sports-media-company-to-pay-1-1-million-fine-change-practices-over-privacy-violations/)) <!-- verified -->

- Deploy **company-operated opt-out mechanisms** on all digital properties ([CPPA Press Release](https://privacy.ca.gov/2026/03/youth-sports-media-company-to-pay-1-1-million-fine-change-practices-over-privacy-violations/)) <!-- verified -->

- **Recognize and honor opt-out preference signals** (e.g., Global Privacy Control) ([CPPA Press Release](https://privacy.ca.gov/2026/03/youth-sports-media-company-to-pay-1-1-million-fine-change-practices-over-privacy-violations/)) <!-- verified -->

- **Revise privacy notices and consent banners** to accurately reflect data practices ([CPPA Press Release](https://privacy.ca.gov/2026/03/youth-sports-media-company-to-pay-1-1-million-fine-change-practices-over-privacy-violations/)) <!-- verified -->

- Conduct **quarterly scans** of digital properties to maintain a current inventory of tracking technologies ([Holland & Knight Analysis](https://www.hklaw.com/en/insights/publications/2026/03/calprivacy-fines-playon-sports-1-1m-for-ccpa-opt-out-and-notice)) <!-- verified -->

- Complete a **privacy risk assessment** within one year, reviewed by the board of directors, with updates required before any material change in processing for a three-year period ([CPPA Press Release](https://privacy.ca.gov/2026/03/youth-sports-media-company-to-pay-1-1-million-fine-change-practices-over-privacy-violations/)) <!-- verified -->

## Action Items

- **Audit opt-out mechanisms immediately.** Any business relying on NAI, DAA, or similar third-party industry opt-out tools as its primary opt-out method for sale/sharing of personal information must implement its own company-operated opt-out mechanism. The CPPA has now explicitly rejected this practice.

- **Eliminate consent walls for tracking.** "Agree-to-enter" banners that condition access to services on consent to tracking technologies violate the CCPA. Review all cookie/consent banners to ensure consumers can decline non-essential tracking without losing access to purchased services or core functionality.

- **Honor Global Privacy Control and other opt-out preference signals.** Ensure all digital properties are configured to detect and process opt-out preference signals in a frictionless manner per [11 CCR Section 7025](https://www.law.cornell.edu/regulations/california/11-CCR-7025).

- **Review minor-specific obligations.** Businesses serving K-12 schools or platforms likely accessed by users aged 13-16 must obtain affirmative opt-in consent before selling or sharing their personal information. Implement age-gating or default opt-out protections as appropriate.

- **Update privacy notices.** Ensure notices accurately describe all data sale/sharing activities, consumer opt-out rights (including the right to opt out of "sharing"), and how the business processes opt-out preference signals.

## Related Reports

No related reports found in the knowledge base.

## Sources

1. [CPPA Press Release -- Youth Sports Media Company to Pay $1.10 Million Fine](https://privacy.ca.gov/2026/03/youth-sports-media-company-to-pay-1-1-million-fine-change-practices-over-privacy-violations/) -- Official CPPA announcement with enforcement details and required remedies
2. [CPPA Order of Decision -- PlayOn Sports](https://privacy.ca.gov/wp-content/uploads/sites/357/2026/03/Order-of-Decision_PlayOn_Enforcement.pdf) -- Official enforcement order (PDF)
3. [Holland & Knight -- CalPrivacy Fines PlayOn Sports $1.1M](https://www.hklaw.com/en/insights/publications/2026/03/calprivacy-fines-playon-sports-1-1m-for-ccpa-opt-out-and-notice) -- Law firm analysis of opt-out and notice violations
4. [Hunton Andrews Kurth -- CalPrivacy Issues $1.1 Million Fine](https://www.hunton.com/privacy-and-cybersecurity-law-blog/calprivacy-issues-1-1-million-fine-for-ccpa-violations-involving-student-privacy) -- Law firm analysis of student privacy implications
5. [Covington Inside Privacy -- CalPrivacy Fines PlayOn Sports](https://www.insideprivacy.com/state-privacy/calprivacy-fines-playon-sports-for-insufficient-opt-out-process/) -- Law firm analysis of opt-out process insufficiency
6. [WilmerHale -- Youth Sports Media Company to Pay $1.10 Million Fine](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20260319-youth-sports-media-company-to-pay-1-10-million-fine-in-cppa-enforcement-action) -- Law firm analysis of enforcement action details
7. [Cal. Civ. Code Section 1798.120 -- FindLaw](https://codes.findlaw.com/ca/civil-code/civ-sect-1798-120/) -- Official statutory text for consumer right to opt out of sale/sharing
8. [Cal. Civ. Code Section 1798.135 -- FindLaw](https://codes.findlaw.com/ca/civil-code/civ-sect-1798-135/) -- Official statutory text for business opt-out mechanism obligations
9. [11 CCR Section 7025 -- Opt-Out Preference Signals](https://www.law.cornell.edu/regulations/california/11-CCR-7025) -- CCPA implementing regulation on opt-out preference signals
10. [Loeb & Loeb -- CalPrivacy PlayOn Sports Enforcement](https://www.loeb.com/en/insights/publications/2026/03/calprivacy-playon-sports-enforcement) -- Law firm analysis noting the decision did not find minor-specific violations
