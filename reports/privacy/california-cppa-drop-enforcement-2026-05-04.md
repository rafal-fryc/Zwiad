---
title: "CalPrivacy Accelerates Data Broker Enforcement as DROP Compliance Deadline Nears"
date: 2026-05-04
jurisdiction: "California"
category: "privacy"
development_type: "enforcement"
finding_id: "SCAN-20260504-014"
topic_key: "CPPA-DROP-REQUIREMENTS-SET-2026"
topic_type: "enforcement"
first_reported: 2026-05-04
last_updated: 2026-05-04
status_history: []
cluster: "CalPrivacy DROP Program: Data Broker Audit Regulations"
cluster_slug: "cppa-data-broker-drop-audits"
---

# CalPrivacy Accelerates Data Broker Enforcement as DROP Compliance Deadline Nears

**Jurisdiction:** California | **Category:** Privacy | **Date:** 2026-05-04

## Summary [HIGH confidence]

On August 1, 2026, California's Delete Request and Opt-Out Platform (DROP) shifts from a passive consumer-facing service into an active compliance obligation for every data broker doing business in California. Beginning that date, data brokers must access DROP at least every 45 days, process consumer deletion requests, and complete deletions within 90 days — or face fines of $200 per request per day. At its April 30–May 1, 2026 board meeting, the [California Privacy Protection Agency (CalPrivacy)](https://cppa.ca.gov) signaled accelerating enforcement, discussed the federal SECURED Act's threat to the DELETE Act's consumer rights, and explored California's potential for an EU adequacy decision.

## Key Facts [HIGH confidence]

- **August 1, 2026 deadline is firm.** Starting that date, all data brokers doing business in California must access DROP at least every 45 days to retrieve and process consumer deletion requests, per the [California Delete Act (SB 362)](https://cppa.ca.gov/regulations/pdf/data_broker_reg_delete_act_statute_eff_20260101.pdf) and the [DROP regulations adopted November 6, 2025](https://cppa.ca.gov/regulations/drop.html).
- **90-day deletion window.** Once a data broker downloads a consumer's deletion request from DROP, it must delete the consumer's non-exempt personal information and report status back to CalPrivacy within 90 days ([CPPA DROP requirements page](https://cppa.ca.gov/regulations/drop.html)).
- **DROP launched January 1, 2026.** The platform went live accepting consumer requests from day one; as of early 2026 more than 285,000 California residents had already submitted requests, far exceeding agency projections ([IAPP coverage](https://iapp.org/news/a/calprivacy-unpacks-drop-updates-on-consumer-participation-upcoming-enforcement)).
- **Data broker registration has surged under enforcement pressure.** Registered data brokers grew from 459 in June 2025 to more than 575 by February 2026, which CalPrivacy attributed directly to its enforcement actions ([IAPP, CalPrivacy explores enforcement uptick](https://iapp.org/news/a/calprivacy-explores-data-broker-enforcement-uptick-eu-adequacy-prospects)).
- **Penalties are steep.** Failure to process a deletion request carries a $200-per-request, per-day fine. Perkins Coie estimated a theoretical single-cycle miss could expose one data broker to [$1.5 billion in aggregate penalty liability](https://perkinscoie.com/insights/blog/california-drop-mechanism-15-billion-exposure-and-clock-ticking-key-takeaways-2026).
- **Strike Force is active.** CalPrivacy formed a [Data Broker Enforcement Strike Force](https://cppa.ca.gov/announcements/2025/20251119.html) in November 2025 to investigate both registration failures and CCPA violations; enforcement actions are already in double digits.
- **SECURED Act threat.** At the board meeting, CalPrivacy discussed the federal [SECURE Data Act](https://privacy.ca.gov/2026/04/california-privacy-protection-agency-releases-letter-opposing-the-secure-data-act/), which would preempt both the CCPA and the Delete Act, eliminating DROP. CalPrivacy Chairperson Jennifer Urban stated the agency "cannot support any law that has a broad preemption provision in it."
- **EU adequacy exploration.** The April 30–May 1 board also reviewed whether California could pursue an adequacy determination with the EU under the GDPR, a move that could protect cross-border data flows if the EU-U.S. Data Privacy Framework were invalidated. Agency staff noted such a determination may not currently benefit the state ([IAPP](https://iapp.org/news/a/calprivacy-explores-data-broker-enforcement-uptick-eu-adequacy-prospects)).

## Legal Basis [HIGH confidence]

The DROP system is built on two layers of California law:

1. **California Delete Act — Cal. Civ. Code § 1798.99.80 et seq. (SB 362, Ch. 709, Stats. 2023).** Requires CalPrivacy to create a centralized accessible deletion mechanism. Mandates data broker registration, annual fees ($6,000 per year for 2026), and DROP participation. Effective compliance requirement (DROP access and processing) begins August 1, 2026. Statute text available at the [CPPA statutory PDF](https://cppa.ca.gov/regulations/pdf/data_broker_reg_delete_act_statute_eff_20260101.pdf).

2. **DROP Regulations (Cal. Code Regs.).** Adopted September 26, 2025; approved by the Office of Administrative Law November 6, 2025; effective January 1, 2026. The [final text of regulations (PDF)](https://cppa.ca.gov/regulations/pdf/drop_ftr.pdf) specifies mechanics of DROP access, data matching obligations, deletion procedures, suppression list requirements, breach notification, and compliance reporting. The [Final Statement of Reasons (PDF)](https://cppa.ca.gov/regulations/pdf/drop_fosr.pdf) explains the Agency's policy rationale.

CalPrivacy has exclusive enforcement authority under the Delete Act; there is no private right of action. Penalties are administrative, assessed by the Enforcement Division.

## What Data Brokers Must Do by August 1, 2026 [HIGH confidence]

The [CPPA's Information for Data Brokers page](https://cppa.ca.gov/data_brokers/) and the DROP regulations require the following concrete steps:

- **Establish a DROP account** and pay the one-time access integration fee before August 1, 2026.
- **Connect technical systems** to retrieve deletion request lists from the DROP portal at minimum every 45 days.
- **Run matching logic** against internal databases using identifiers provided by CalPrivacy; delete all non-exempt personal information associated with any matched identifier.
- **Maintain a suppression list** to prevent re-collection, re-purchase, or re-sale of deleted consumer data.
- **Report deletion status** back to CalPrivacy within the 90-day window.
- **Ensure registration is current** and complete — including all trade names (DBAs), public-facing websites, and separately registered subsidiaries/affiliates (see [Enforcement Advisory 2025-01](https://cppa.ca.gov/pdf/enfadvisory202501.pdf)).

Independent compliance audits begin **January 1, 2028**, adding a second enforcement layer starting that year.

## Enforcement Context [HIGH confidence]

CalPrivacy has been progressively escalating Delete Act enforcement since mid-2025:

- **Accurate Append, Inc.** (Washington): $55,400 fine for failure to register (July 2025).
- **Jerico Pictures, Inc. (National Public Data)** (Florida): $46,000 fine for same violation.
- **KMA** (Connecticut): $55,800 settlement for failure to register.
- Additional enforcement actions have followed in a continuing campaign the agency itself characterized as an "enforcement uptick."

The Nelson Mullins [DROP Enforcement Advisory FAQ](https://www.nelsonmullins.com/insights/alerts/privacy_and_data_security_alert/all/calprivacy-drops-latest-drop-enforcement-advisory-faqs-and-another-clear-warning-to-data-brokers) describes the agency's most recent enforcement advisory as "another clear warning to data brokers" with detailed FAQs on compliance expectations.

## Action Items

- **Immediately audit DROP account status.** Any data broker doing business in California that has not yet created and funded a DROP account should do so now — the August 1 hard deadline leaves minimal time to complete technical integration and testing.
- **Map all affiliated entities.** Subsidiaries and affiliates cannot rely on a parent's DROP registration; confirm each distinct legal entity has its own account and current registration.
- **Test deletion pipeline end-to-end.** Validate that the 45-day retrieval cycle, matching logic, deletion workflows, suppression list writes, and status reporting back to CalPrivacy all function correctly before August 1.
- **Monitor the SECURED Act.** If the federal SECURE Data Act advances in Congress and passes with its current preemption language, it would eliminate DROP obligations — but compliance planning should proceed on the assumption that California law remains in effect.
- **Prepare for DROP audits (2028).** CalPrivacy is in active pre-rulemaking on third-party audit standards (public comment period closed May 7, 2026); audit documentation and records management practices should be built into DROP workflows now.
- **Review suppression list architecture.** The obligation to prevent re-collection of deleted data is technical and ongoing; ensure downstream data purchases and partnerships honor suppression flags.

## Related Reports

- [reports/privacy/cppa-drop-audit-rulemaking-2026-04-12.md](reports/privacy/cppa-drop-audit-rulemaking-2026-04-12.md) -- CalPrivacy's April 2026 pre-rulemaking invitation for comments on DROP audit standards is the next compliance layer after August 2026 enforcement, directly tied to this development.
- [reports/privacy/enforcement-actions/california-cppa-data-broker-delete-act-growbots-2025-03-13.md](reports/privacy/enforcement-actions/california-cppa-data-broker-delete-act-growbots-2025-03-13.md) -- CPPA's first Delete Act enforcement settlement (Growbots, March 2025) established the enforcement pattern now being accelerated toward the August 2026 deadline.
- [reports/privacy/california-cppa-opposes-apra-federal-preemption-2024-05-14.md](reports/privacy/california-cppa-opposes-apra-federal-preemption-2024-05-14.md) -- CPPA's opposition to the American Privacy Rights Act's preemption provisions directly parallels its current opposition to the SECURED Act's effort to preempt the Delete Act and DROP.
- [reports/privacy/cppa-playon-sports-ccpa-enforcement-2026-04-07.md](reports/privacy/cppa-playon-sports-ccpa-enforcement-2026-04-07.md) -- Documents the broader CPPA enforcement trajectory (CCPA fines reaching $2.75M) that provides institutional context for the DROP enforcement ramp-up.

## Sources

1. [Accessible Deletion Mechanism – DROP System Requirements (CPPA)](https://cppa.ca.gov/regulations/drop.html) -- Official CPPA page describing DROP requirements, timelines, and data broker obligations.
2. [California Delete Act Statute (SB 362, effective 2026-01-01) (PDF)](https://cppa.ca.gov/regulations/pdf/data_broker_reg_delete_act_statute_eff_20260101.pdf) -- Official statutory text of the Delete Act (Cal. Civ. Code § 1798.99.80 et seq.).
3. [DROP Regulations Final Text (PDF)](https://cppa.ca.gov/regulations/pdf/drop_ftr.pdf) -- Official text of the DROP regulations adopted November 6, 2025, effective January 1, 2026.
4. [DROP Final Statement of Reasons (PDF)](https://cppa.ca.gov/regulations/pdf/drop_fosr.pdf) -- CalPrivacy's regulatory rationale for the DROP rules.
5. [Information for Data Brokers (CPPA)](https://cppa.ca.gov/data_brokers/) -- Official CPPA guidance on data broker registration and compliance obligations under DROP.
6. [CPPA Meeting Materials April 30–May 1, 2026](https://cppa.ca.gov/meetings/materials/20260430_0501.html) -- Official board meeting materials covering DROP updates, SECURED Act, and EU adequacy discussion.
7. [CalPrivacy Launches Data Broker Enforcement Strike Force (CPPA, Nov. 2025)](https://cppa.ca.gov/announcements/2025/20251119.html) -- Official announcement of the Strike Force formation.
8. [Enforcement Advisory 2025-01: Data Broker Registration (PDF)](https://cppa.ca.gov/pdf/enfadvisory202501.pdf) -- CPPA formal enforcement advisory on registration requirements and common deficiencies.
9. [California Privacy Protection Agency Releases Letter Opposing the SECURE Data Act](https://privacy.ca.gov/2026/04/california-privacy-protection-agency-releases-letter-opposing-the-secure-data-act/) -- Official CPPA opposition letter to federal SECURE Data Act.
10. [IAPP: CalPrivacy explores data broker enforcement uptick, EU adequacy prospects](https://iapp.org/news/a/calprivacy-explores-data-broker-enforcement-uptick-eu-adequacy-prospects) -- IAPP coverage of the April 30–May 1 board meeting including enforcement statistics and EU adequacy discussion.
11. [IAPP: CalPrivacy unpacks DROP updates on consumer participation, upcoming enforcement](https://iapp.org/news/a/calprivacy-unpacks-drop-updates-on-consumer-participation-upcoming-enforcement) -- IAPP coverage of the February 2026 board meeting DROP update with consumer participation figures.
12. [Perkins Coie: The California DROP Mechanism — $1.5 Billion in Exposure](https://perkinscoie.com/insights/blog/california-drop-mechanism-15-billion-exposure-and-clock-ticking-key-takeaways-2026) -- Law firm analysis estimating penalty exposure from a single missed deletion cycle, from 2026 IAPP Global Summit.
13. [Pillsbury: A New Era of Data Deletion: Inside California's DROP System](https://consumer-protection-dispatch.pillsburylaw.com/data-deletion-california-drop-system/) -- Law firm overview of DROP compliance requirements and data broker obligations.
14. [Nelson Mullins: CalPrivacy Drops Latest DROP Enforcement Advisory: FAQs](https://www.nelsonmullins.com/insights/alerts/privacy_and_data_security_alert/all/calprivacy-drops-latest-drop-enforcement-advisory-faqs-and-another-clear-warning-to-data-brokers) -- Law firm FAQ on most recent enforcement advisory and compliance expectations.
15. [Crowell & Moring: California Privacy Agency Launches Data Broker Strike Force](https://www.crowell.com/en/insights/client-alerts/california-privacy-agency-launches-data-broker-strike-force-amid-delete-act-crackdown) -- Law firm client alert on Strike Force formation and Delete Act enforcement.
16. [Hunton Andrews Kurth: CalPrivacy Announces Agenda for April 30–May 1 Board Meeting](https://www.hunton.com/privacy-and-cybersecurity-law-blog/calprivacy-announces-the-agenda-for-its-april-30-may-1-board-meeting) -- Law firm summary of board meeting agenda items including DROP, SECURED Act, and EU adequacy.
