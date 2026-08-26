---
title: "US Lawmakers Flag Critical Loopholes in DOJ Data Security Program: White House, CIA, and Nuclear Labs Left Unprotected"
date: 2026-05-22
jurisdiction: "Federal"
category: "privacy"
development_type: "legislation"
finding_id: "SCAN-20260601-024"
topic_key: "federal-d66a9272-2026"
topic_type: "federal_bill"
first_reported: 2026-05-22
last_updated: 2026-06-01
status_history: []
cluster: "DOJ Data Security Program (EO 14117): Cross-Border Data Transfer Restrictions"
cluster_slug: "doj-data-security-program-eo14117"
---

# US Lawmakers Flag Critical Loopholes in DOJ Data Security Program: White House, CIA, and Nuclear Labs Left Unprotected

**Jurisdiction:** Federal | **Category:** Privacy | **Date:** May 22, 2026

## Executive Summary [HIGH confidence]

Three Democratic lawmakers — Senator Ron Wyden (D-OR), Senator Martin Heinrich (D-NM), and Representative Sara Jacobs (D-CA) — sent a letter to the Trump administration warning that the Department of Justice's Data Security Program (DSP) contains critical geographic gaps that leave federal government employees at the White House, CIA headquarters, the National Reconnaissance Office, the National Geospatial-Intelligence Agency, Congress, the Supreme Court, and nuclear weapons laboratories vulnerable to foreign surveillance through commercial location data. The DSP's Government-Related Location Data List (GRLD List) — which defines the 736 geofenced locations where location data triggers heightened restrictions on transfers to adversary nations — omits many of the most sensitive national security facilities in the country. The lawmakers urged the Trump administration to replace the piecemeal location list with a comprehensive "protection zone" covering the entire Washington, D.C. National Capital Region. The DSP itself took effect April 8, 2025, implementing [Executive Order 14117](https://www.federalregister.gov/documents/2024/03/01/2024-04573/preventing-access-to-americans-bulk-sensitive-personal-data-and-united-states-government-related) signed by President Biden in February 2024, and represents the most significant US federal restriction on cross-border transfers of sensitive personal and government data to adversary nations.

## Background [HIGH confidence]

### Executive Order 14117 and the DSP's Origins

On February 28, 2024, President Biden signed [Executive Order 14117](https://www.federalregister.gov/documents/2024/03/01/2024-04573/preventing-access-to-americans-bulk-sensitive-personal-data-and-united-states-government-related), "Preventing Access to Americans' Bulk Sensitive Personal Data and United States Government-Related Data by Countries of Concern." The order directed the DOJ to establish a new regulatory framework to restrict the ability of six designated "countries of concern" — China (including Hong Kong and Macau), Cuba, Iran, North Korea, Russia, and Venezuela — to access bulk sensitive personal data and US government-related data through commercial transactions that would otherwise be legal under existing law.

The DOJ's National Security Division (NSD) issued the [final rule at 28 C.F.R. Part 202](https://www.ecfr.gov/current/title-28/chapter-I/part-202) on January 8, 2025, with the [Federal Register publication](https://www.federalregister.gov/documents/2025/01/08/2024-31486/preventing-access-to-us-sensitive-personal-data-and-government-related-data-by-countries-of-concern) providing the complete regulatory text. The core provisions took effect on April 8, 2025, with additional compliance requirements for audits and annual reporting phased in through October 5, 2025. The DOJ issued its [Compliance Guide](https://www.justice.gov/opa/media/1396356/dl) on April 11, 2025, and established a good-faith enforcement grace period through July 8, 2025.

### What the DSP Restricts

The DSP establishes what are effectively export controls over two broad categories of data:

**Bulk Sensitive Personal Data:** The DSP restricts transactions involving large volumes of genomic, geolocation, biometric, health, financial, and certain other categories of personal data. "Bulk" thresholds vary by data type — for example, geolocation data covering more than 1,000 US persons triggers bulk restrictions. Prohibited transactions (complete bans) include data brokerage transactions with countries of concern or covered persons. Restricted transactions (allowed with compliance obligations) include vendor agreements, employment agreements, and investment agreements, which must satisfy CISA Security Requirements, data compliance programs, audit obligations, and recordkeeping requirements, per the [DOJ compliance documentation](https://www.justice.gov/nsd/data-security).

**Government-Related Data:** This category is treated with heightened restriction and carries no bulk threshold — even a single data point qualifies if it falls within the definition. Government-related data encompasses: (1) precise geolocation data originating from within any location on the GRLD List; and (2) sensitive personal data that is marketed as linked or linkable to US federal employees or contractors. The absence of a bulk threshold for government-related location data reflects the recognition that even granular, individual-level data about a federal official's location can be operationally useful to a foreign intelligence service, per [Mayer Brown's analysis of the GRLD List](https://www.mayerbrown.com/en/insights/publications/2025/06/doj-data-security-program-insights-on-the-government-related-location-data-list).

## Detailed Analysis [HIGH confidence]

### The Government-Related Location Data List and Its Gaps

The GRLD List designates [736 geofenced locations](https://www.mayerbrown.com/en/insights/publications/2025/06/doj-data-security-program-insights-on-the-government-related-location-data-list) — each defined by precise latitude and longitude coordinates — as areas where any geolocation data collected is automatically treated as government-related data and subject to heightened DSP restrictions regardless of whether it can be linked to a specific individual. The list was designed to include military installations, intelligence community facilities, and other national security assets where geolocation data could expose the movements of government personnel to foreign adversaries.

However, analysis of the GRLD List has revealed significant omissions. The full list was largely composed of Department of Defense installations — Air Force, Army, and Navy bases, national guard installations, and ammunition plants. Within the Washington, D.C. area, [the list identifies only two sites: the Naval Observatory and the Washington Navy Yard](https://www.mayerbrown.com/en/insights/publications/2025/06/doj-data-security-program-insights-on-the-government-related-location-data-list). This means that geolocation data collected within the boundaries of the following facilities is **not** treated as restricted government-related data under the current GRLD List:

- The White House
- CIA Headquarters (Langley, Virginia)
- The National Reconnaissance Office (NRO)
- The National Geospatial-Intelligence Agency (NGA)
- Congress (Capitol Hill)
- The Supreme Court
- Continuity-of-government facilities
- Federal laboratories involved in nuclear weapons design

The [Wyden-Heinrich-Jacobs letter](https://www.wyden.senate.gov/news/press-releases/wyden-heinrich-jacobs-justice-department-failed-to-protect-white-house-cia-hq-and-other-sensitive-us-government-locations-from-ai-enabled-foreign-spy-threats) was addressed to Director of National Intelligence Tulsi Gabbard and Acting Attorney General Todd Blanche and was released publicly on approximately May 22, 2026. DOJ has acknowledged to outside observers that the current list is not comprehensive and that additional locations may be added.

### The AI-Enabled Surveillance Threat Vector

The lawmakers' letter placed particular emphasis on how AI systems amplify the threat posed by unregulated commercial location data. The letter warned that AI-enabled analysis of raw location data streams from within and around Washington, D.C. can allow foreign intelligence services to infer the patterns, routines, and movements of identified government officials even without naming specific individuals in the dataset. Commercial data brokers aggregate and sell this precise location data — derived from mobile apps and device sensors — to any buyer, including intermediaries acting on behalf of foreign governments. When the location originates at an unprotected facility like CIA headquarters, the DSP's protections do not apply, and there is no federal bar on a data broker selling that data to a Chinese or Russian buyer.

The [Lawfare analysis of data brokers and government employees](https://www.lawfaremedia.org/article/data-brokers-and-threats-to-government-employees) and the [Brennan Center's report on closing the data broker loophole](https://www.brennancenter.org/our-work/research-reports/closing-data-broker-loophole) have both documented how the intersection of commercial data markets and federal employee movements creates intelligence vulnerabilities. The DSP was specifically designed to address this threat, but the omission of key facilities undermines its effectiveness at the most sensitive level.

### The Proposed "Protection Zone" Solution

Rather than continuing to add individual buildings to the GRLD List one at a time — a process that is reactive and inherently incomplete — the three lawmakers proposed creating a geographically defined "protection zone" covering the entire National Capital Region around Washington, D.C. Under this approach, any geolocation data originating anywhere within the zone would automatically be treated as government-related data and subject to DSP restrictions, regardless of whether the specific building or facility is individually named. This approach mirrors the concept used for Presidential Emergency Operations Centers and other broadly defined security perimeters in national security law.

The practical effect would be to close the coverage gap for CIA headquarters, the White House, the Capitol, and the dozens of other federal facilities that are within D.C. but currently excluded from the GRLD List. It would also future-proof the program against the addition of new facilities to the D.C. area that might otherwise go unprotected due to administrative lag.

### Trump Administration Response

The letter was directed to the Trump administration, which has continued to operate the DSP — a program initiated under a Biden executive order — without publicly announcing changes to the GRLD List. The DSP's structure under 28 C.F.R. Part 202 remains in place. DOJ NSD acknowledged informally that the list is "not comprehensive," but has not announced a formal update timeline as of this writing. The current administration has not publicly responded to the specific congressional letter as of the date of this report.

## Impact Assessment [MEDIUM confidence]

### Data Brokers and Commercial Location Services

Data brokers and commercial location analytics companies that sell or provide access to precise geolocation data derived from mobile devices are the primary industry immediately affected by this coverage gap. As long as CIA headquarters, the White House, and similar facilities remain off the GRLD List, commercial brokers face no DSP-based restrictions on selling location data from those areas to countries of concern or their agents. If the protection zone proposal is adopted, brokers would need to geo-filter all data against a broader geographic exclusion zone — potentially impacting billions of data records derived from the D.C. metropolitan area.

### Federal Employee Vulnerability

The more immediate impact is on federal employees themselves, who have no DSP protection for location data generated during their work at unprotected facilities. A CIA officer's daily commute pattern, parking habits, or time-in-building data derived from their personal mobile device or vehicle is freely available to data brokers and, through them, to foreign adversaries. This is the precise vulnerability that EO 14117 was designed to address — but the incomplete GRLD List leaves it open for the most sensitive national security workforce.

### Compliance Landscape for Affected Entities

Organizations subject to the DSP — including technology companies, financial institutions, healthcare providers, and universities — must maintain compliance with the current GRLD List as implemented. If DOJ updates the list to add the White House, CIA headquarters, or adopts a National Capital Region zone, affected organizations will need to update their data compliance programs and systems accordingly. The DSP's compliance framework includes mandatory data security requirements under [CISA Security Requirements for Restricted Transactions](https://www.cisa.gov/resources-tools/resources/EO-14117-security-requirements), annual certification, audit obligations, and recordkeeping requirements that would extend to any newly designated locations.

### Legislative and Regulatory Outlook

The lawmakers' letter is formally directed at the executive branch, not Congress, framing the request as an administrative fix the Trump administration can make without new legislation. DOJ NSD has authority under the existing final rule to update the GRLD List. However, the current administration has given no public indication it intends to expand the list — and the letter's Democratic authorship may complicate bipartisan momentum for the fix. Broader legislative action to reform the data broker industry remains pending in other contexts, including the SECURE Data Act (HR 8413), though that bill does not specifically address the GRLD List gap.

## Action Items

- **Data brokers and location data vendors:** Review current transaction screening systems against the GRLD List. Monitor DOJ NSD for any formal updates to the list, which could require rapid reconfiguration of geo-filtering systems.
- **Federal contractors with mobile workforce:** Assess whether employee location data collected through corporate apps or fleet tracking systems falls within any existing GRLD geofences, and prepare for potential expansion of protected zones.
- **DSP-regulated organizations (general):** Maintain current compliance posture under 28 C.F.R. Part 202 and CISA Security Requirements. Designate a compliance officer to track NSD updates to the GRLD List, which can change by administrative action without notice-and-comment rulemaking.
- **Government affairs teams:** Monitor DOJ NSD and DNI responses to the Wyden-Heinrich-Jacobs letter. A DOJ response or formal list update may trigger compliance obligations quickly if your organization operates in or aggregates data from the Washington, D.C. metropolitan area.
- **Technology and security teams:** Evaluate whether systems that collect or aggregate precise geolocation data have the technical capability to implement geofence-based filtering at the scale a National Capital Region protection zone would require.

## Related Reports

- [reports/privacy/federal-legislation/federal-wyden-fisa702-reform-democrats-2026-04-19.md](../federal-wyden-fisa702-reform-democrats-2026-04-19.md) — Senator Wyden is lead author of both the FISA 702 reform letter and this DSP loophole letter; both address AI-enabled foreign surveillance of US persons by adversary nations.
- [reports/privacy/federal-legislation/federal-secure-data-act-hr8413-2026-04-22.md](../federal-secure-data-act-hr8413-2026-04-22.md) — The SECURE Data Act includes a data broker registry and cross-border data flow provisions that intersect with the DSP's commercial data restrictions.
- [reports/privacy/enforcement-actions/california-ag-location-data-sweep-2025-03-10.md](../../enforcement-actions/california-ag-location-data-sweep-2025-03-10.md) — California AG's location data enforcement sweep addresses the same commercial location data industry that the DSP's GRLD List is designed to regulate at the federal level.

## Sources

1. [Wyden, Heinrich, Jacobs Senate Press Release — May 2026](https://www.wyden.senate.gov/news/press-releases/wyden-heinrich-jacobs-justice-department-failed-to-protect-white-house-cia-hq-and-other-sensitive-us-government-locations-from-ai-enabled-foreign-spy-threats) — Official Senate press release detailing the letter, signatories, specific omitted locations, and the National Capital Region protection zone proposal.
2. [PBS NewsHour — Lawmakers warn data protection rules don't protect key sites](https://www.pbs.org/newshour/politics/lawmakers-warn-data-protection-rules-dont-protect-key-sites-including-white-house-and-cia) — News coverage identifying the letter date (Thursday, approximately May 22, 2026) and summarizing the lawmakers' key arguments.
3. [ProKerala — Data loophole exposed near White House](https://www.prokerala.com/news/articles/a1765847.html) — Secondary coverage identifying which specific legislators signed the letter and the protection zone proposal.
4. [DOJ National Security Division — Data Security Program](https://www.justice.gov/nsd/data-security) — Official DOJ landing page for the Data Security Program with links to the final rule, compliance guides, and GRLD List.
5. [Federal Register — Final Rule, 28 C.F.R. Part 202 (Jan. 8, 2025)](https://www.federalregister.gov/documents/2025/01/08/2024-31486/preventing-access-to-us-sensitive-personal-data-and-government-related-data-by-countries-of-concern) — The complete final regulatory text implementing Executive Order 14117, effective April 8, 2025.
6. [eCFR — 28 C.F.R. Part 202](https://www.ecfr.gov/current/title-28/chapter-I/part-202) — Current codified version of the DSP regulations, including definitions, prohibited and restricted transaction categories, and compliance requirements.
7. [Federal Register — Executive Order 14117 (Feb. 28, 2024)](https://www.federalregister.gov/documents/2024/03/01/2024-04573/preventing-access-to-americans-bulk-sensitive-personal-data-and-united-states-government-related) — The Biden executive order that created the legal authority for the DSP.
8. [Mayer Brown — Insights on the Government-Related Location Data List](https://www.mayerbrown.com/en/insights/publications/2025/06/doj-data-security-program-insights-on-the-government-related-location-data-list) — Law firm analysis identifying specific omissions from the GRLD List, including CIA headquarters and the two-site Washington D.C. representation (Naval Observatory and Washington Navy Yard).
9. [DOJ Compliance Guide (April 11, 2025)](https://www.justice.gov/opa/media/1396356/dl) — Official DOJ compliance guide issued alongside program launch; describes data compliance program, audit, and recordkeeping requirements.
10. [CISA Security Requirements for Restricted Transactions](https://www.cisa.gov/resources-tools/resources/EO-14117-security-requirements) — CISA's technical security requirements that DSP-regulated entities must implement for restricted transactions.
11. [Lawfare — Data Brokers and Threats to Government Employees](https://www.lawfaremedia.org/article/data-brokers-and-threats-to-government-employees) — Policy analysis of how the commercial data broker industry creates national security risks for federal employees and government facilities.
12. [Brennan Center — Closing the Data Broker Loophole](https://www.brennancenter.org/our-work/research-reports/closing-data-broker-loophole) — Policy research documenting the structural gap between commercial data broker practices and existing federal protections for government personnel.
13. [DOJ Office of Public Affairs — DSP Implementation Announcement](https://www.justice.gov/opa/pr/justice-department-implements-critical-national-security-program-protect-americans-sensitive) — Official DOJ press release announcing program implementation and describing its national security rationale.
