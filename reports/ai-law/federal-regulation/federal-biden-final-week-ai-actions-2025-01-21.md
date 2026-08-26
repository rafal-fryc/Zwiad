---
title: "Biden's Final Week: Three Federal AI Actions — Export Controls, Infrastructure, and Cybersecurity"
date: 2025-01-21
jurisdiction: "Federal"
category: "ai-law"
development_type: "guidance"
finding_id: "SCAN-20250121-027"
topic_key: "washington-932b9225-2025"
topic_type: "guidance"
first_reported: 2025-01-21
last_updated: 2026-04-22
status_history:
  - "2026-04-22: Revised per reviewer round 1 — corrected Tier 2 NVEU GPU cap attribution, corrected TLS 1.3 deadline sourcing in Detailed Analysis (original EO uses 'within 180 days'; December 1, 2025 date introduced by Trump June 2025 amendment), corrected BIS rescission date to May 12, 2025 (three days before compliance deadline), added January 15, 2026 delayed compliance note for certain AI Diffusion Rule provisions."
cluster: "Biden Final Week: AI Export Controls, Infrastructure, and Cybersecurity EOs (January 2025)"
cluster_slug: "biden-final-week-ai-actions-jan-2025"
---

# Biden's Final Week: Three Federal AI Actions — Export Controls, Infrastructure, and Cybersecurity

**Jurisdiction:** Federal | **Category:** ai-law | **Date:** 2025-01-21

## Executive Summary [HIGH confidence]

In his final six days in office, President Biden issued three significant AI-related regulatory actions that collectively represented the most sweeping federal AI governance push of his administration. On January 13, 2025, the Bureau of Industry and Security (BIS) published a final rule — the "Framework for Artificial Intelligence Diffusion" — establishing worldwide export controls on advanced computing chips and AI model weights, dividing the world into three access tiers. On January 14, 2025, Biden signed Executive Order 14141, directing the Departments of Defense and Energy to lease federal lands for gigawatt-scale AI data centers powered by clean energy. On January 16, 2025, he signed Executive Order 14144, a sweeping cybersecurity order requiring software attestation reform, post-quantum cryptography adoption, and AI-assisted federal cyber defenses. All three actions were subsequently targeted by the incoming Trump administration: the AI Diffusion Rule was rescinded on May 12, 2025; EO 14141 was revoked on July 23, 2025; and EO 14144 was substantially amended in June 2025, though not fully revoked.

## Background [HIGH confidence]

Biden's three January 2025 AI actions built on a multi-year federal AI governance architecture. The foundation was the October 2023 Executive Order 14110 on "Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence," which directed dozens of federal agency actions on AI safety, red-team testing, and standards development. That order was revoked by President Trump on January 20, 2025 — his first day in office — as part of a broader rollback of Biden-era AI policy.

On export controls, the Biden administration had been tightening chip restrictions since October 2022, with successive rounds of export control rules targeting advanced semiconductors destined for China and other adversaries. The January 2025 AI Diffusion Rule represented the most ambitious expansion of that framework, extending controls beyond China to create a tiered global system.

On AI infrastructure, the context was a surge in private-sector demand for electricity and land to build AI data centers. The Biden administration was concerned that the U.S. risked dependence on foreign AI infrastructure and sought to mobilize federal land and permitting authority before the transition.

On cybersecurity, EO 14144 directly succeeded the May 2021 Executive Order 14028 on "Improving the Nation's Cybersecurity," which had introduced software supply chain security reforms following the SolarWinds breach. EO 14144 formalized and deepened many of the commitments from the 2021 order.

## Detailed Analysis [HIGH confidence]

### Action 1: Framework for Artificial Intelligence Diffusion (AI Diffusion Rule)

The [Framework for Artificial Intelligence Diffusion](https://www.federalregister.gov/documents/2025/01/15/2025-00636/framework-for-artificial-intelligence-diffusion) was published in the Federal Register on January 15, 2025, as FR Doc. 2025-00636. The rule became effective January 13, 2025, with a delayed compliance deadline of May 15, 2025. Certain provisions — specifically paragraphs 14, 15, and 18 of Supplement No. 10 to Part 748 — had a further delayed compliance date of January 15, 2026.

The rule imposed worldwide export controls on two categories of items: (1) advanced computing integrated circuits (ICs), including H100, H200, and Blackwell-generation Nvidia GPUs; and (2) AI model weights, designated under the new Export Control Classification Number (ECCN) 4E091. The model weight controls were novel — never before had the U.S. applied export controls to trained AI model parameters.

The rule established a **three-tier country classification framework**:

- **Tier 1 (Unrestricted):** The United States and 18 close allies including the United Kingdom, Canada, Germany, Japan, South Korea, Taiwan, Australia, and New Zealand. Entities headquartered in Tier 1 countries had unlimited access to advanced GPUs for datacenter buildouts.

- **Tier 2 (Capped Access):** Countries including Singapore, Israel, Portugal, Switzerland, Poland, the United Arab Emirates, Saudi Arabia, and India. Tier 2 entities that obtained **National Validated End-User (NVEU) authorization** could deploy up to 100,000 H100-equivalent GPUs by end of 2025, 270,000 by end of 2026, and 320,000 by end of 2027. Tier 2 entities that did not obtain NVEU status faced a significantly lower standard national cap of approximately 49,901 H100-equivalents through 2027. A license-free threshold of 1,700 H100-equivalents also applied to Tier 2 imports without counting toward national limits.

- **Tier 3 (Restricted):** Adversaries including China, Russia, and North Korea, which were already subject to existing export controls and sanctions and would have faced an outright ban under the new rule.

The rule also introduced new controls on AI model weights, defining them as "numerical parameter[s] within an AI model" that "help determine the model's outputs in response to inputs." This extended U.S. export controls into the domain of software and intangible technology at an unprecedented scale.

The [Semiconductor Industry Association criticized the rule](https://www.semiconductors.org/sia-statement-on-biden-administration-action-imposing-new-export-controls-on-ai-chips/) for potentially harming U.S. competitiveness by complicating chip sales to allied nations. RAND Corporation analysis noted the framework's ambition to create a "U.S.-led global AI ecosystem" through export controls.

### Action 2: Executive Order 14141 — AI Infrastructure

On January 14, 2025, President Biden signed [Executive Order 14141, "Advancing United States Leadership in Artificial Intelligence Infrastructure."](https://bidenwhitehouse.archives.gov/briefing-room/presidential-actions/2025/01/14/executive-order-on-advancing-united-states-leadership-in-artificial-intelligence-infrastructure/) This EO established a framework for leasing federal lands managed by the Department of Defense (DOD) and Department of Energy (DOE) to private-sector entities for the construction of "frontier AI data centers" at gigawatt scale.

**Key Provisions:**
- By **February 28, 2025**: The Secretary of Defense and Secretary of Energy were each required to identify a minimum of three sites on federal land suitable for AI data center development.
- By **March 31, 2025**: DOD and DOE were required to launch competitive 30-day public solicitations for private-sector proposals.
- By **June 30, 2025**: Winning proposals were to be announced.
- By **end of 2025**: All permits and approvals for selected AI infrastructure projects were to be issued, or as soon as possible under applicable law.
- By **end of 2027**: Construction and operation of frontier AI data centers and associated clean energy facilities was targeted.

EO 14141 obligated private-sector developers to: procure clean energy resources matching data center demand; bear all costs for data center construction; adhere to high labor standards; and purchase "an appropriate share" of U.S.-manufactured semiconductors.

The EO established five guiding principles for AI infrastructure development, centered on national security, economic competitiveness, clean energy integration, minimizing environmental and community impacts, and preserving U.S. global AI leadership.

### Action 3: Executive Order 14144 — Cybersecurity

On January 16, 2025, Biden signed [Executive Order 14144, "Strengthening and Promoting Innovation in the Nation's Cybersecurity."](https://public-inspection.federalregister.gov/2025-01470.pdf) Published in the Federal Register on January 17, this EO built extensively on EO 14028 (2021).

**Software Supply Chain Security:** EO 14144 directed software developers supplying the federal government to submit to CISA machine-readable attestations of secure development practices, high-level validation artifacts, and a list of federal customers. It directed CISA to develop an audit process to verify attestation completeness and to regularly validate sample attestations.

**Post-Quantum Cryptography (PQC):** Within 180 days of signing, CISA was required to publish a list of product categories where PQC-capable solutions are "widely available." Agencies then had 90 days to make PQC support a mandatory requirement for new solicitations in those product categories. Within 180 days, the NSA Director and OMB Director were also required to issue mandates for agencies to support TLS 1.3 or a successor by January 2, 2030. (Note: the Trump administration's June 6, 2025 amending order converted these rolling "within 180 days" deadlines to fixed calendar dates, including a December 1, 2025 compliance date for the TLS 1.3 mandate issuance — see Impact Assessment below.)

**AI for Cyber Defense:** EO 14144 directed DOD to adopt advanced AI models for cyber defense operations and established a pilot program to explore AI applications in securing critical infrastructure in the energy sector.

**Digital Identity:** The EO directed initiatives to drive adoption of digital identity verification for federal programs.

## Impact Assessment [HIGH confidence]

### AI Diffusion Rule — Rescinded May 2025

The AI Diffusion Rule never entered into force. On May 12, 2025 — three days before the compliance deadline — the Trump administration [announced its rescission](https://www.bis.gov/press-release/department-commerce-announces-rescission-biden-era-artificial-intelligence-diffusion-rule-strengthens), citing "burdensome new regulatory requirements" that allegedly stifled American technological innovation and damaged diplomatic relationships with strategic partners. Nvidia, whose GPU sales to Tier 2 markets would have been subject to caps, [celebrated the reversal](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-celebrates-dumping-of-biden-era-ai-chip-export-rules-simpler-new-policy-promised).

BIS stated it would issue a replacement rule but provided no timeline. Alongside the rescission, BIS issued three guidance documents effective May 13, 2025: (1) a policy statement on controls for advanced ICs used to train Chinese AI models; (2) guidance on General Prohibition 10 applicable to Chinese-manufactured 3A090 ICs; and (3) guidance on preventing diversion of AI supply chains.

The practical effect is that export controls on AI chips revert to the pre-Diffusion-Rule framework, while the administration develops a new approach.

### EO 14141 — Revoked July 2025

EO 14141 survived the initial Trump transition. The incoming administration did not include it on its January 20, 2025 revocation list. However, on July 23, 2025, President Trump [revoked EO 14141 and replaced it](https://www.whitehouse.gov/presidential-actions/2025/07/accelerating-federal-permitting-of-data-center-infrastructure/) with a new executive order, "Accelerating Federal Permitting of Data Center Infrastructure." Trump's replacement order retained the concept of leasing federal lands for data centers but removed the clean energy mandates and high labor standards that Biden's EO had required. The replacement also expanded the list of agencies directed to identify sites beyond DOD and DOE to include EPA and the Department of the Interior.

For organizations that had submitted proposals or begun the competitive solicitation process under Biden's framework, the revocation required reassessment under the new order.

### EO 14144 — Amended but Largely Preserved

Unlike the other two actions, EO 14144 largely survived. Trump did not revoke it on January 20, 2025, and on June 6, 2025, [issued an amending order](https://www.whitehouse.gov/presidential-actions/2025/06/sustaining-select-efforts-to-strengthen-the-nations-cybersecurity-and-amending-executive-order-13694-and-executive-order-14144/) titled "Sustaining Select Efforts to Strengthen the Nation's Cybersecurity and Amending Executive Order 13694 and Executive Order 14144." This reflected bipartisan consensus on core cybersecurity measures.

The Trump amendments rescinded several Section 6 provisions covering AI-cyber initiatives — including the DOD AI cyber defense mandate and the critical infrastructure AI pilot — on the stated grounds of "refocusing AI cybersecurity efforts towards identifying and managing vulnerabilities, rather than censorship." The software attestation framework, post-quantum cryptography requirements, and network security mandates in other sections were substantially preserved with modifications toward simpler, more decentralized compliance.

The June 6, 2025 amending order also converted the original Biden EO's rolling "within 180 days" deadlines to fixed calendar dates. Specifically, the December 1, 2025 deadline for the NSA Director and OMB Director to issue TLS 1.3 mandate guidance was introduced by the Trump amendment — not by the original Biden EO. The Biden EO's original language required this action within 180 days of signing (i.e., by approximately mid-July 2025).

**Current obligations under EO 14144 (post-Trump amendments):** Federal software suppliers continue to face CISA attestation requirements. PQC transition timelines remain in force. TLS 1.3 mandate (by January 2, 2030) remains in effect.

## Action Items

- **Federal contractors and software suppliers:** Monitor CISA for updates to the secure software development attestation form and audit procedures, which remain operative under amended EO 14144.
- **AI chip manufacturers and exporters:** The AI Diffusion Rule has been rescinded; await BIS guidance on replacement export control framework. Apply pre-Diffusion-Rule EAR requirements in the interim. Monitor for a new BIS rulemaking.
- **Data center and energy developers:** Biden's EO 14141 has been replaced by Trump's July 2025 "Accelerating Federal Permitting of Data Center Infrastructure" EO. Evaluate new site leasing opportunities under the replacement framework, which removes clean energy mandates.
- **Federal agencies:** PQC support mandates and TLS 1.3 transition deadlines under EO 14144 remain operative. The December 1, 2025 deadline for NSA/OMB to issue TLS 1.3 mandate guidance (introduced by the June 6, 2025 Trump amending order) has passed; confirm agency compliance posture with the January 2, 2030 implementation deadline.
- **AI model developers:** The model weight controls in the rescinded AI Diffusion Rule are no longer in effect, but monitor BIS for any replacement rule that may reimpose controls on closed-source AI model weights (ECCN 4E091 remains on the books).

## Related Reports

- [reports/ai-law/federal-regulation/federal-biden-nsm-ai-national-security-2024-11-05.md](reports/ai-law/federal-regulation/federal-biden-nsm-ai-national-security-2024-11-05.md) — Biden's November 2024 National Security Memorandum on AI, which preceded the final-week actions and established the policy foundation for AI and national security, including the same DOD/DOE agencies directed by EO 14141.
- [reports/ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md](reports/ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md) — Trump's December 2025 EO on national AI policy framework, which represents the subsequent chapter in the federal AI executive order sequence that began with the Biden actions described here.
- [reports/ai-law/federal-regulation/federal-national-policy-framework-ai-preemption-2026-04-14.md](reports/ai-law/federal-regulation/federal-national-policy-framework-ai-preemption-2026-04-14.md) — Trump administration's federal AI preemption framework, the downstream policy consequence of the Trump-era reversal of Biden's AI architecture.

## Sources

1. [Framework for Artificial Intelligence Diffusion — Federal Register](https://www.federalregister.gov/documents/2025/01/15/2025-00636/framework-for-artificial-intelligence-diffusion) — Official Federal Register publication of the AI Diffusion Rule (FR Doc. 2025-00636), January 15, 2025.
2. [Executive Order 14141 — Biden White House Archives](https://bidenwhitehouse.archives.gov/briefing-room/presidential-actions/2025/01/14/executive-order-on-advancing-united-states-leadership-in-artificial-intelligence-infrastructure/) — Official text of EO 14141, "Advancing United States Leadership in Artificial Intelligence Infrastructure," January 14, 2025.
3. [Executive Order 14144 — Federal Register Public Inspection](https://public-inspection.federalregister.gov/2025-01470.pdf) — Official text of EO 14144, "Strengthening and Promoting Innovation in the Nation's Cybersecurity," January 16, 2025.
4. [BIS Press Release: Rescission of AI Diffusion Rule](https://www.bis.gov/press-release/department-commerce-announces-rescission-biden-era-artificial-intelligence-diffusion-rule-strengthens) — Official BIS announcement of the May 12, 2025 rescission, with rationale and interim measures.
5. [National Law Review: Out with a Bang — Biden's Three AI Actions](https://natlawreview.com/article/out-bang-president-biden-ends-final-week-office-three-ai-actions-ai-washington) — Mintz law firm analysis summarizing all three actions contemporaneously (January 21, 2025).
6. [EO 14141 — American Presidency Project](https://www.presidency.ucsb.edu/documents/executive-order-14141-advancing-united-states-leadership-artificial-intelligence) — Archival record of EO 14141 including revocation date (July 23, 2025).
7. [EO 14144 — American Presidency Project](https://www.presidency.ucsb.edu/documents/executive-order-14144-strengthening-and-promoting-innovation-the-nations-cybersecurity) — Archival record of EO 14144 with full text.
8. [Trump "Accelerating Federal Permitting of Data Center Infrastructure" EO](https://www.whitehouse.gov/presidential-actions/2025/07/accelerating-federal-permitting-of-data-center-infrastructure/) — Trump's July 2025 executive order revoking and replacing Biden's EO 14141.
9. [Trump Cyber EO amending EO 14144](https://www.whitehouse.gov/presidential-actions/2025/06/sustaining-select-efforts-to-strengthen-the-nations-cybersecurity-and-amending-executive-order-13694-and-executive-order-14144/) — June 6, 2025 Trump order amending EO 14144, preserving core cybersecurity requirements while rescinding AI-specific provisions; introduced December 1, 2025 fixed deadlines in place of original "within 180 days" language.
10. [RAND: Understanding the AI Diffusion Framework](https://www.rand.org/pubs/perspectives/PEA3776-1.html) — Independent analysis of the three-tier country system and strategic implications.
11. [SIA Statement on Biden AI Chip Export Controls](https://www.semiconductors.org/sia-statement-on-biden-administration-action-imposing-new-export-controls-on-ai-chips/) — Semiconductor Industry Association's contemporaneous critique of the Diffusion Rule.
12. [Davis Wright Tremaine: Analyzing Biden's Cybersecurity EO](https://www.dwt.com/blogs/privacy--security-law-blog/2025/02/biden-cybersecurity-executive-order-cisa) — Detailed section-by-section analysis of EO 14144.
13. [Davis Wright Tremaine: Trump Reverses Biden Cyber EO](https://www.dwt.com/blogs/privacy--security-law-blog/2025/06/trump-cyber-order-changes-biden-eo-14144) — Analysis of June 2025 Trump amendments to EO 14144, identifying what was preserved vs. rescinded.
14. [Morgan Lewis: Biden EO on AI Infrastructure and Federal Lands](https://www.morganlewis.com/blogs/powerandpipes/2025/01/biden-executive-order-to-fast-track-ai-data-centers-and-energy-infrastructure-on-federal-lands) — Energy law analysis of EO 14141's clean energy and federal land leasing provisions.
15. [Inside Government Contracts: January 2025 AI Developments](https://www.insidegovernmentcontracts.com/2025/02/january-2025-ai-developments-transitioning-to-the-trump-administration/) — Government contracts law analysis of all three Biden AI actions and their status at the Trump transition.
16. [Hogan Lovells: BIS Announces Rescission of Biden-Era AI Diffusion Rule](https://www.hoganlovells.com/en/publications/bis-announces-rescission-of-bidenera-ai-diffusion-rule-and-issues-new-ai-policy-and-guidance) — Law firm analysis confirming May 12, 2025 rescission announcement date and issuing guidance on interim compliance posture.
17. [Baker McKenzie: BIS Begins Rescinding AI Diffusion Rule](https://sanctionsnews.bakermckenzie.com/bis-begins-rescinding-ai-diffusion-rule-and-issues-guidance-on-huawei-ics-and-on-ics-and-commodities-used-to-train-ai-models/) — Confirms May 12, 2025 rescission announcement; notes May 13 issuance of accompanying guidance documents.
