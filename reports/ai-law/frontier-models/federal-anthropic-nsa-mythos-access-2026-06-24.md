---
title: "Export Control Order Severs Anthropic's NSA Mythos Arrangement, Exposing AI Governance Paradox"
date: 2026-06-24
jurisdiction: "Federal"
category: "ai-law"
development_type: "regulation"
finding_id: "SCAN-20260628-031"
topic_key: "federal-04a9d25d-2026"
topic_type: "rulemaking"
first_reported: 2026-06-24
last_updated: 2026-06-29
status_history:
  - "2026-06-29: Revision r1 — corrected AP attribution for official clarification (was incorrectly attributed to the Economist); clarified DoD supply chain designation timeline (Trump directive Feb 27, formal notification letters March 3, 2026) and replaced stateofsurveillance.org citation with Mayer Brown primary legal source; added red.anthropic.com as primary source for $2,000/24-hour exploit capability figures; rephrased Project Glasswing characterization to distinguish commercial consortium from offensive operations vehicle."
cluster: "BIS Export Controls on Frontier AI Model Access: Anthropic Fable 5 and Mythos 5"
cluster_slug: "bis-export-controls-frontier-ai-models"
---

# Export Control Order Severs Anthropic's NSA Mythos Arrangement, Exposing AI Governance Paradox

**Jurisdiction:** Federal | **Category:** AI Law | **Date:** June 24, 2026

## Summary [HIGH confidence]

The Commerce Department's June 12, 2026 export control directive ordering Anthropic to suspend foreign national access to its Fable 5 and Mythos 5 models collaterally severed an active operational arrangement between Anthropic and the National Security Agency. The NSA had been using Mythos — including the Mythos Preview model — for cybersecurity red-teaming and offensive cyber operations, with access authorized under the Project Glasswing framework and roughly six Anthropic engineers embedded inside the agency as forward-deployed staff. When the export control order hit, NSA analysts working under that arrangement lost access because their authorization had derived from the Glasswing program. This outcome illustrates a structural governance paradox at the intersection of AI export controls and national security AI programs: the same administration that invoked national security as the basis for restricting Anthropic's models was simultaneously operating classified AI programs that depended on access to those same models.

## Key Facts [HIGH confidence]

- The NSA had been using Anthropic's Mythos model for cybersecurity operations before the export ban, with [roughly six Anthropic forward-deployed engineers embedded at the agency](https://techcrunch.com/2026/06/05/nsa-said-to-be-readying-anthropics-mythos-for-use-in-cyber-operations/) to help deploy and adapt the model. This arrangement was an extension of Project Glasswing, Anthropic's controlled-access cybersecurity program launched in April 2026. ([Axios](https://www.axios.com/2026/04/19/nsa-anthropic-mythos-pentagon))
- The NSA's use of Mythos had proceeded despite the DoD's [supply chain risk designation of Anthropic](https://www.mayerbrown.com/en/insights/publications/2026/03/pentagon-designates-anthropic-a-supply-chain-risk-what-government-contractors-need-to-know) — the first such designation ever applied to an American company. President Trump directed agencies to cease using Anthropic technology on February 27, 2026; the formal DoD notification letters designating Anthropic a supply chain risk were dated March 3, 2026. The designation barred Anthropic from Pentagon contracts and directed contractors to cease commercial activity with the firm, yet the NSA, which operates under DoD, continued its Glasswing arrangement. ([CNBC](https://www.cnbc.com/2026/05/01/pentagon-anthropic-blacklist-mythos-michael.html))
- On June 12, 2026, the Bureau of Industry and Security issued an "Is Informed" export control letter ordering Anthropic to suspend all Fable 5 and Mythos 5 access for any foreign national anywhere in the world. Anthropic, unable to reliably segment its users by nationality, took both models fully offline. ([Anthropic official statement](https://www.anthropic.com/news/fable-mythos-access))
- Following the export control order, [parts of the NSA lost access to Mythos 5](https://www.nextgov.com/artificial-intelligence/2026/06/parts-nsa-lose-mythos-5-access-amid-anthropic-supply-chain-dispute/414366/) because NSA analysts' authorization to use the model had flowed through the Project Glasswing program, which Anthropic suspended to comply with the directive. Some NSA analysts were notified they would lose access on the Friday following the order. ([Defense One](https://www.defenseone.com/policy/2026/06/nsa-mythos-anthropic-supply-chain/414371/))
- The agency may still retain access to earlier versions of Mythos under prior arrangements that predate Project Glasswing, though access to current model versions, Anthropic engineering support, and updates is more limited. ([Nextgov/FCW](https://www.nextgov.com/artificial-intelligence/2026/06/parts-nsa-lose-mythos-5-access-amid-anthropic-supply-chain-dispute/414366/))
- NSA Director Gen. Joshua Rudd had briefed Sen. Mark Warner (D-VA) that during authorized internal red-team testing, Mythos "broke into almost all of our classified systems, not in weeks, but in hours." A U.S. official later clarified to the Associated Press that the model identified vulnerabilities but did not necessarily exploit them, and that the testing was a sanctioned defensive exercise, not a security breach. ([Security Affairs](https://securityaffairs.com/194016/ai/anthropics-mythos-ai-broke-into-almost-all-nsa-classified-systems-in-hours.html); [CNBC/AP](https://www.cnbc.com/2026/06/23/anthropics-mythos-model-found-vulnerabilities-in-classified-us-government-systems-official-says.html))
- On June 27, Commerce Secretary Lutnick partially reversed course, restoring Mythos 5 access for approximately 100 approved US organizations through Project Glasswing. It is not publicly confirmed whether the NSA's arrangement was among those specifically restored. ([NPR](https://www.npr.org/2026/06/27/nx-s1-5871245/trump-administration-imposes-restrictions-for-anthropic-to-halt-access-to-2-ai-models))

## Background: The NSA–Anthropic Arrangement [MEDIUM confidence]

The NSA's integration of Anthropic's Mythos model was distinct from standard government procurement in two respects. First, it proceeded through Project Glasswing — a commercial cybersecurity research consortium — rather than a formal DoD procurement contract, allowing the intelligence agency to sidestep the supply chain risk designation that formally prohibited defense-sector engagement with Anthropic. Second, the arrangement included [Anthropic embedding its own engineers inside the NSA](https://socfortress.medium.com/anthropic-engineers-embedded-at-nsa-for-mythos-cyber-operations-4a73a99cd551) — a model more commonly associated with forward-deployed commercial software support than with classified intelligence operations.

Mythos's value to the NSA stemmed from its capability to autonomously identify and exploit zero-day vulnerabilities. According to [Anthropic's published cybersecurity capability assessment](https://red.anthropic.com/2026/mythos-preview/), Mythos can produce a complete exploit chain for a complex target for under $2,000 in compute cost and in under 24 hours — capabilities that one source described as useful for operations targeting the networks of adversaries such as China or Iran. ([Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/nsa-using-clause-mythos-for-offensive-cyber-operations-report-claims-says-half-a-dozen-anthropic-engineers-embedded-inside-the-agency))

The existence of this arrangement surfaced in an April 19, 2026 [Axios scoop](https://www.axios.com/2026/04/19/nsa-anthropic-mythos-pentagon) that characterized the situation as a paradox: the military was simultaneously arguing in court that using Anthropic's tools threatened US national security while the intelligence community was actively using those tools in classified cyber operations. The Pentagon's tech chief subsequently [stated](https://www.cnbc.com/2026/05/01/pentagon-anthropic-blacklist-mythos-michael.html) that the Mythos Glasswing arrangement was a separate issue from the DoD blacklisting — an acknowledgment that different parts of the executive branch were operating under different and conflicting policy frameworks.

## Governance Paradox and Policy Implications [MEDIUM confidence]

The export control directive's disruption of the NSA arrangement illustrates a structural gap in the US government's approach to governing frontier AI. Three distinct and conflicting policy tracks ran simultaneously:

**Track 1 — Restriction (DoD):** The Pentagon's late February/early March 2026 supply chain designation effectively barred formal Anthropic contracting across the defense sector.

**Track 2 — Integration (NSA/Intelligence Community):** Through Project Glasswing, the NSA actively embedded Anthropic engineers and used Mythos for classified operations, operating under a different procurement channel that was not technically covered by the DoD designation.

**Track 3 — Emergency Control (Commerce/BIS):** The June 12 BIS export control directive invoked national security to impose emergency restrictions on the same models the intelligence community was relying on for national security operations — without apparent coordination with the NSA's operational use.

The result is that export control authorities designed to prevent adversaries from accessing advanced AI capabilities simultaneously denied those capabilities to US intelligence agencies. [CSIS analysts](https://www.csis.org/analysis/department-commerce-restricted-access-anthropics-latest-models-what-comes-next) have noted that this uncoordinated overlap reflects the absence of any interagency framework for managing the lifecycle of commercially developed frontier AI models that have both national security value and national security risk.

The June 2, 2026 executive order "Promoting Advanced Artificial Intelligence Innovation and Security" does not resolve this tension. While it assigns NSA the authority to set the capability thresholds that designate a model as a "covered frontier model," it does not address how emergency export control authorities should interact with NSA's own operational use of covered models — leaving the conflict that materialized on June 12 structurally unresolved. ([White House EO](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/))

## What Is Not Known [LOW confidence]

The following material facts are not publicly confirmed and could not be verified at time of writing:

- Whether the June 27 partial restoration of Mythos 5 access through Project Glasswing has specifically restored NSA analysts' access, or whether the NSA's arrangement remains severed.
- The specific terms of any separate classified agreement between Anthropic and the NSA, beyond the Glasswing commercial program framework.
- Whether the Anthropic engineers previously embedded at the NSA have been removed, continue in a limited capacity, or whether a revised arrangement is under negotiation.
- The identity of the "prior arrangements" under which the NSA may retain access to earlier Mythos versions.

## Action Items

- **AI developers working with government agencies** should audit whether their operational government arrangements flow through commercial programs (like Project Glasswing) that could be disrupted by export control actions directed at the company — and map the distinction between commercial-channel government access and formal procurement contracts.
- **National security agencies and defense contractors** using commercially developed frontier AI models should assess whether their access to those models is legally insulated from general-purpose export control directives, or whether access could be suspended unilaterally if the model's developer faces an emergency BIS action.
- **Compliance counsel** for AI developers with intelligence community clients should review whether the "Is Informed" mechanism can reach models delivered under classified government contracts or only those offered through commercial channels.
- **Policy teams** should monitor whether the White House-Anthropic cybersecurity framework negotiations currently underway result in an interagency coordination mechanism that reconciles BIS export control authorities with intelligence community AI operational access — this gap is the most significant unresolved governance question surfaced by the June 12 order.
- **General counsel at frontier AI companies** should note that the DoD supply chain designation and BIS export controls are distinct legal instruments administered by different agencies with different trigger criteria — a company can be simultaneously restricted by both and yet operationally depended upon by the same executive branch through a third channel.

## Related Reports

- [reports/ai-law/frontier-models/federal-anthropic-fable5-mythos5-export-control-2026-06-15.md](reports/ai-law/frontier-models/federal-anthropic-fable5-mythos5-export-control-2026-06-15.md) — Primary report on the June 12 BIS export control directive that directly caused NSA analysts to lose Mythos access.
- [reports/ai-law/frontier-models/federal-anthropic-cybersecurity-framework-negotiations-2026-06-22.md](reports/ai-law/frontier-models/federal-anthropic-cybersecurity-framework-negotiations-2026-06-22.md) — Reports the White House-Anthropic negotiations over a cybersecurity compliance framework — the policy process most likely to resolve the interagency coordination gap this report identifies.
- [reports/ai-law/frontier-models/federal-anthropic-project-glasswing-claude-mythos-2026-04-14.md](reports/ai-law/frontier-models/federal-anthropic-project-glasswing-claude-mythos-2026-04-14.md) — Background on Project Glasswing, the commercial cybersecurity program through which the NSA arrangement was established.
- [reports/ai-law/federal-regulation/federal-congress-ai-export-controls-anthropic-2026-06-17.md](reports/ai-law/federal-regulation/federal-congress-ai-export-controls-anthropic-2026-06-17.md) — Congressional response to the export control order, including bipartisan demands for legal and procedural transparency and advancing AI governance legislation.
- [reports/ai-law/frontier-models/federal-trump-ai-innovation-security-eo-2026-06-02.md](reports/ai-law/frontier-models/federal-trump-ai-innovation-security-eo-2026-06-02.md) — The June 2 executive order that establishes voluntary frontier model review and assigns NSA classification authority — the framework that did not prevent the June 12 interagency conflict.

## Sources

1. [Nextgov/FCW: Parts of NSA lose Mythos 5 access amid Anthropic supply chain dispute](https://www.nextgov.com/artificial-intelligence/2026/06/parts-nsa-lose-mythos-5-access-amid-anthropic-supply-chain-dispute/414366/) — Primary federal IT reporting on NSA analysts losing Mythos 5 access, Glasswing as the authorization mechanism, and potential retention of older model versions.
2. [Defense One: Parts of NSA lose Mythos 5 access after White House imposes limits](https://www.defenseone.com/policy/2026/06/nsa-mythos-anthropic-supply-chain/414371/) — Defense-focused coverage confirming NSA access disruption and supply chain dispute framing.
3. [Axios: NSA using Anthropic's Mythos despite Defense Department blacklist](https://www.axios.com/2026/04/19/nsa-anthropic-mythos-pentagon) — April 2026 scoop revealing NSA's use of Mythos through Glasswing notwithstanding the DoD supply chain designation.
4. [TechCrunch: NSA said to be readying Anthropic's Mythos for use in cyber operations](https://techcrunch.com/2026/06/05/nsa-said-to-be-readying-anthropics-mythos-for-use-in-cyber-operations/) — June 5, 2026 reporting on Anthropic's half-dozen forward-deployed engineers embedded at NSA, based on Financial Times reporting.
5. [Tom's Hardware: NSA using Claude Mythos for 'offensive cyber operations'](https://www.tomshardware.com/tech-industry/artificial-intelligence/nsa-using-clause-mythos-for-offensive-cyber-operations-report-claims-says-half-a-dozen-anthropic-engineers-embedded-inside-the-agency) — Details on the six Anthropic engineers embedded at NSA and Mythos exploit cost/time capabilities (secondary source).
6. [Anthropic: Assessing Claude Mythos Preview's cybersecurity capabilities](https://red.anthropic.com/2026/mythos-preview/) — Anthropic's primary published capability assessment, providing the $2,000/exploit-chain and under-24-hour timing figures.
7. [Anthropic: Statement on the US government directive to suspend access to Fable 5 and Mythos 5](https://www.anthropic.com/news/fable-mythos-access) — Official Anthropic statement on the June 12 BIS directive and resulting global access suspension.
8. [Security Affairs: Anthropic's Mythos AI broke into almost all NSA classified systems in hours](https://securityaffairs.com/194016/ai/anthropics-mythos-ai-broke-into-almost-all-nsa-classified-systems-in-hours.html) — Reporting on NSA Director Rudd's Senate Intelligence Committee briefing on Mythos red-team results and the subsequent AP official clarification.
9. [CNBC/AP: Anthropic's Mythos model found vulnerabilities in classified US government systems, official says](https://www.cnbc.com/2026/06/23/anthropics-mythos-model-found-vulnerabilities-in-classified-us-government-systems-official-says.html) — AP wire report via CNBC; authoritative sourcing for the U.S. official clarification distinguishing vulnerability identification from exploitation.
10. [CNBC: Pentagon tech chief says Anthropic is still blacklisted, but Mythos is a separate issue](https://www.cnbc.com/2026/05/01/pentagon-anthropic-blacklist-mythos-michael.html) — Pentagon official statement distinguishing the DoD supply chain designation from the NSA's Glasswing arrangement.
11. [Mayer Brown: Pentagon Designates Anthropic a Supply Chain Risk — What Government Contractors Need to Know](https://www.mayerbrown.com/en/insights/publications/2026/03/pentagon-designates-anthropic-a-supply-chain-risk-what-government-contractors-need-to-know) — Primary legal analysis of the DoD supply chain designation, confirming the February 27 Trump directive and March 3, 2026 formal notification letter dates.
12. [NPR: Trump administration partially lifts export ban on Anthropic's most advanced AI model](https://www.npr.org/2026/06/27/nx-s1-5871245/trump-administration-imposes-restrictions-for-anthropic-to-halt-access-to-2-ai-models) — Reports the June 27 partial restoration of Mythos 5 for ~100 approved US organizations.
13. [CSIS: The Department of Commerce Restricted Access to Anthropic's Latest Models. What Comes Next?](https://www.csis.org/analysis/department-commerce-restricted-access-anthropics-latest-models-what-comes-next) — Policy analysis of the legal authority and coordination gaps exposed by the export control action.
14. [White House: Promoting Advanced Artificial Intelligence Innovation and Security (Executive Order)](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/) — June 2, 2026 EO assigning NSA authority over frontier model classification thresholds — the framework that did not address interagency coordination of emergency export controls.
15. [SOCFortress / Medium: Anthropic Engineers Embedded at NSA for Mythos Cyber Operations](https://socfortress.medium.com/anthropic-engineers-embedded-at-nsa-for-mythos-cyber-operations-4a73a99cd551) — Secondary reporting on the forward-deployed engineer arrangement.
