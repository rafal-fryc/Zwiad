---
finding_id: "SCAN-20260407-006"
format: "client-alert"
date: "2026-04-07"
jurisdiction: "California"
category: "privacy"
development_type: "enforcement"
cluster: "CPPA CCPA Enforcement Actions"
cluster_slug: "cppa-ccpa-enforcement-actions"
---

# California AG Announces Record $2.75 Million CCPA Settlement With Disney for Opt-Out Violations Across Streaming Services

**Jurisdiction:** California | **Category:** Privacy | **Date:** 2026-04-07

## Summary [HIGH confidence] [VERIFIED]

On February 11, 2026, California Attorney General Rob Bonta announced a [$2.75 million settlement with The Walt Disney Company](https://oag.ca.gov/news/press-releases/california-wont-let-it-go-attorney-general-bonta-announces-275-million) <!-- verified --> -- the largest CCPA settlement in California history -- for failing to honor consumers' opt-out requests across Disney's streaming platforms and devices. <!-- verified --> The enforcement action signals that partial compliance with opt-out obligations -- honoring requests on one service or device but not others linked to the same account -- constitutes a CCPA violation, with significant implications for any business operating multi-platform digital ecosystems.

## Key Facts [HIGH confidence] [VERIFIED]

- The AG's investigation originated from a [January 2024 sweep of streaming services](https://oag.ca.gov/news/press-releases/california-wont-let-it-go-attorney-general-bonta-announces-275-million) <!-- verified -->, which identified systemic failures in how Disney processed opt-out requests under Cal. Civ. Code [Section 1798.120](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.120.) <!-- verified --> (right to opt out of sale or sharing) and [Section 1798.135](https://california-ccpa.org/section-1798-135-methods-of-limiting-sale-sharing-and-use-of-personal-information-and-use-of-sensitive-personal-information/) <!-- verified --> (methods for limiting sale and sharing).

- Disney's opt-out toggles within streaming apps applied only to the specific service and device where the consumer clicked them. <!-- verified --> A consumer who opted out on Disney+ could still have their data sold via Hulu, ESPN+, or other Disney platforms on different devices -- even when logged into the [same Disney account](https://www.dataprotectionreport.com/2026/02/partial-compliance-is-noncompliance-lessons-from-californias-2-75-million-settlement-with-disney/). <!-- verified -->

- Disney processed Global Privacy Control (GPC) signals only at the device level, not the account level, meaning a GPC opt-out on one browser did not carry over to other devices or browsers linked to the same account <!-- verified --> -- a violation of CCPA's requirement to honor GPC as a valid [opt-out signal](https://www.hklaw.com/en/insights/publications/2026/02/caught-in-a-mousetrap-disney-to-pay-for-consumer-opt-out-missteps). <!-- verified -->

- Under the settlement, Disney must implement a frictionless, account-wide opt-out that applies across all streaming services and devices when a logged-in user submits a request, add a clear "Do Not Sell or Share" link inside every streaming app, and provide users with confirmation that their opt-out was processed. <!-- verified --> Disney must also provide [compliance updates every 60 days](https://oag.ca.gov/news/press-releases/california-wont-let-it-go-attorney-general-bonta-announces-275-million) until full compliance is achieved. <!-- verified -->

- The $2.75 million penalty is the [largest CCPA settlement to date](https://www.hunton.com/privacy-and-cybersecurity-law-blog/california-ag-reaches-record-2-75-million-settlement-with-disney-for-violating-ccpas-opt-out-rights) <!-- verified -->, surpassing the AG's prior CCPA enforcement actions and reflecting the AG office's escalating posture on opt-out compliance. <!-- verified -->

## Action Items

- **Audit cross-platform opt-out propagation:** Businesses operating multiple services, apps, or device platforms under a single user account must verify that opt-out requests propagate to all services and devices linked to that account -- not just the service or device where the request originated.

- **Verify GPC signal handling at the account level:** Ensure that Global Privacy Control signals received while a user is logged in are applied account-wide, not limited to the specific browser or device transmitting the signal.

- **Confirm "Do Not Sell or Share" link placement:** Review all consumer-facing applications -- including mobile apps, smart TV apps, and web interfaces -- to ensure a clear and conspicuous opt-out link is present in each, consistent with Cal. Civ. Code Section 1798.135.

- **Document and confirm opt-out processing:** Implement mechanisms to provide consumers with confirmation that their opt-out request has been received and effectuated across the full platform ecosystem.

## Related Reports

No related reports found in the knowledge base.

## Sources

1. [California AG Press Release: $2.75 Million Settlement with Disney](https://oag.ca.gov/news/press-releases/california-wont-let-it-go-attorney-general-bonta-announces-275-million) -- Primary source; official announcement with settlement details, violation descriptions, and injunctive terms.
2. [Holland & Knight: Caught in a Mousetrap](https://www.hklaw.com/en/insights/publications/2026/02/caught-in-a-mousetrap-disney-to-pay-for-consumer-opt-out-missteps) -- Law firm analysis of GPC and opt-out toggle failures.
3. [Hunton Andrews Kurth: Record $2.75 Million Settlement](https://www.hunton.com/privacy-and-cybersecurity-law-blog/california-ag-reaches-record-2-75-million-settlement-with-disney-for-violating-ccpas-opt-out-rights) -- Law firm analysis confirming record-setting nature of the penalty.
4. [Norton Rose Fulbright / Data Protection Report: Partial Compliance Is Noncompliance](https://www.dataprotectionreport.com/2026/02/partial-compliance-is-noncompliance-lessons-from-californias-2-75-million-settlement-with-disney/) -- Analysis of cross-device opt-out failures and compliance lessons.
5. [Cal. Civ. Code Section 1798.120 -- Right to Opt Out](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.120.) -- Official statutory text of CCPA opt-out right.
6. [Cal. Civ. Code Section 1798.135 -- Methods of Limiting Sale and Sharing](https://california-ccpa.org/section-1798-135-methods-of-limiting-sale-sharing-and-use-of-personal-information-and-use-of-sensitive-personal-information/) -- Statutory requirements for opt-out mechanisms and "Do Not Sell or Share" links.
