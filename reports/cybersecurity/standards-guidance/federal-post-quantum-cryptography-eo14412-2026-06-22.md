---
title: "White House Signs Two Executive Orders on Quantum Computing and Post-Quantum Cryptography Migration"
date: 2026-06-22
jurisdiction: "Federal"
category: "cybersecurity"
development_type: "regulation"
finding_id: "SCAN-20260628-005"
topic_key: "federal-2699df3a-2026"
topic_type: "rulemaking"
first_reported: 2026-06-24
last_updated: 2026-06-28
status_history: []
cluster: "Trump EOs 14412/14413: Federal Post-Quantum Cryptography Migration Mandate"
cluster_slug: "trump-eo-post-quantum-cryptography-migration"
---

# White House Signs Two Executive Orders on Quantum Computing and Post-Quantum Cryptography Migration

**Jurisdiction:** Federal | **Category:** Cybersecurity | **Date:** June 22, 2026

## Summary [HIGH confidence]

On June 22, 2026, President Trump signed two companion executive orders establishing a comprehensive federal framework for quantum technologies: [EO 14412, "Securing the Nation Against Advanced Cryptographic Attacks"](https://www.whitehouse.gov/presidential-actions/2026/06/securing-the-nation-against-advanced-cryptographic-attacks/), and [EO 14413, "Ushering in the Next Frontier of Quantum Innovation"](https://www.whitehouse.gov/presidential-actions/2026/06/ushering-in-the-next-frontier-of-quantum-innovation/). Together, the orders mandate that federal agencies migrate their highest-priority systems to post-quantum cryptography (PQC) on legally binding deadlines — December 31, 2030 for key establishment and December 31, 2031 for digital signatures — while simultaneously launching a national initiative to develop a fault-tolerant quantum computer by 2028. Federal contractors face parallel FIPS compliance deadlines, and the orders create cascading pressure on critical infrastructure operators and the broader vendor ecosystem.

## Key Facts [HIGH confidence]

- President Trump signed both EOs on June 22, 2026; they were published in the Federal Register on June 25, 2026 (Vol. 91, No. 121): [EO 14412 at pp. 38483–38486](https://www.federalregister.gov/documents/2026/06/25/2026-12909/securing-the-nation-against-advanced-cryptographic-attacks) and [EO 14413 at pp. 38487–38491](https://www.federalregister.gov/documents/2026/06/25/2026-12910/ushering-in-the-next-frontier-of-quantum-innovation), each published as a separate document.
- **EO 14412** directs federal agencies to migrate all [high-value assets (HVAs) and high-impact systems](https://www.whitehouse.gov/presidential-actions/2026/06/securing-the-nation-against-advanced-cryptographic-attacks/) to NIST-approved PQC for key establishment by **December 31, 2030**, and for digital signatures by **December 31, 2031**.
- Agency heads must designate a PQC migration lead within **30 days** of the order; the Office of Management and Budget must issue updated PQC guidance to agencies within **90 days** per [Cybersecurity Dive's reporting](https://www.cybersecuritydive.com/news/quantum-cryptography-white-house-executive-order/823530/).
- The Secretary of Commerce, through NIST, must initiate a pilot PQC migration project within **180 days**, to be completed no later than December 31, 2027, per [EO 14412 text](https://www.whitehouse.gov/presidential-actions/2026/06/securing-the-nation-against-advanced-cryptographic-attacks/).
- NSA must report to the President on the status of PQC migration across National Security Systems within **180 days** and annually thereafter; NSS remain subject to [CNSA 2.0](https://www.whitehouse.gov/presidential-actions/2026/06/securing-the-nation-against-advanced-cryptographic-attacks/) rather than EO 14412 directly.
- The Federal Acquisition Regulatory (FAR) Council must publish a proposed rule within **180 days** requiring covered contractors to comply with NIST FIPS (including PQC algorithms) by December 31, 2030, per [Jenner & Block's analysis](https://www.jenner.com/en/news-insights/client-alerts/two-new-executive-orders-on-quantum-computing-key-takeaways-for-companies-operating-in-quantum-information-science-and-critical-infrastructure).
- A second FAR proposed rule, due within **270 days**, will require contractors to implement vulnerability disclosure policies incorporating cryptographic vulnerability reporting, including testing for non-FIPS-approved algorithms.
- CISA and NIST must publish guidance on minimum elements of a **cryptographic bill of materials (CBOM)** within **270 days** to enable automated inventory of cryptographic assets used across hardware and software.
- The underlying NIST PQC standards are already final: [FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), and FIPS 205 (SLH-DSA)](https://www.federalregister.gov/documents/2024/08/14/2024-17956/announcing-issuance-of-federal-information-processing-standards-fips-fips-203-module-lattice-based) were finalized by NIST on August 13, 2024 and published jointly in the Federal Register on August 14, 2024 (all three announced in a single FR document), after an eight-year global standardization effort.
- The EO explicitly cites the **"harvest now, decrypt later"** threat: adversaries are collecting encrypted US government data today with the intent to decrypt it once fault-tolerant quantum computers become operational, per [NSA, CISA, and NIST warnings](https://www.whitehouse.gov/presidential-actions/2026/06/securing-the-nation-against-advanced-cryptographic-attacks/).
- **EO 14413** directs the Department of Energy to develop and deploy at least one fault-tolerant, scientifically relevant quantum computer (the QC-ADDS initiative) by **2028**, per [DOE's announcement](https://www.energy.gov/science/articles/energy-department-announces-initiative-create-and-deploy-worlds-first).
- EO 14413 also requires: a new national quantum strategy, a plan to strengthen domestic QIST supply chains (within 120 days), a government-wide quantum workforce recruitment strategy (within 90 days), and identification of next-generation quantum sensor projects to field by September 30, 2028.
- Neither EO creates hard migration deadlines for **critical infrastructure** operators (energy, finance, water, transportation, telecommunications, healthcare); however, the orders direct federal agencies to "assist" critical infrastructure owners with their PQC migration plans, per [Jenner & Block](https://www.jenner.com/en/news-insights/client-alerts/two-new-executive-orders-on-quantum-computing-key-takeaways-for-companies-operating-in-quantum-information-science-and-critical-infrastructure).

## Impact Assessment [MEDIUM confidence]

**Federal agencies** face a hard legal obligation under EO 14412, with binding deadlines that supersede prior CISA and OMB guidance. The 30-day agency lead designation requirement is the most immediate compliance action. Agencies that have not begun cryptographic inventory should treat the orders as the starting gun: [Cloudflare's analysis](https://blog.cloudflare.com/post-quantum-eo-2026/) characterizes the EO as converting years of NIST guidance into enforceable directives.

**Federal contractors** will face binding FAR requirements once proposed rules are finalized, which means the practical rulemaking timeline extends into 2027. However, contractors that supply encryption-handling products or services — particularly those supporting HVAs or high-impact systems — should begin PQC readiness assessments immediately, as FAR rulemaking can accelerate, and agency procurement preferences for PQC-capable vendors may precede the formal rule.

**Critical infrastructure operators** are not directly bound, but the EOs create significant indirect pressure. [Jenner & Block warns](https://www.jenner.com/en/news-insights/client-alerts/two-new-executive-orders-on-quantum-computing-key-takeaways-for-companies-operating-in-quantum-information-science-and-critical-infrastructure) that because contractors must be FIPS-PQC-compliant by 2030, "products that vendors build to federal requirements end up used by hospitals, banks, universities, and small businesses" — creating de facto standards across regulated sectors. Additionally, sector-specific regulators (e.g., FFIEC for financial institutions, HHS for healthcare) are likely to follow with complementary guidance.

**The CBOM requirement** is notable for its supply-chain implications: the 270-day CISA/NIST guidance will establish a standardized way to inventory cryptographic dependencies at the component level, analogous to SBOMs for software. Organizations that are already developing CBOM practices will be better positioned for both federal procurement and eventual sector-specific requirements.

[NIST IR 8547](https://csrc.nist.gov/news/2024/postquantum-cryptography-fips-approved) sets the RSA and ECC deprecation schedule: deprecated for new federal systems after 2030, fully disallowed (including for legacy interoperability) after 2035 — making the 2030 PQC transition deadline a de facto sunset for classical public-key cryptography in federal environments.

## Action Items

- **Designate a PQC Migration Lead** (due within 30 days of June 22, 2026 — by July 22, 2026): Federal agency heads must name a senior official responsible for PQC migration planning. Contractors should appoint an internal PQC lead in parallel.
- **Conduct a cryptographic inventory now**: Identify all systems using RSA, ECC, and classical Diffie-Hellman for key exchange or digital signatures. Prioritize HVAs and high-impact systems for the 2030 deadline; inventory all others for the 2031 deadline. Organizations without a CBOM process should begin developing one ahead of the CISA/NIST guidance.
- **Monitor the OMB PQC guidance** (due within 90 days of June 22 — by September 19, 2026): The updated OMB memo will set agency-specific implementation milestones and is expected to be the primary operational compliance document. Track for publication via the Federal Register and OMB website.
- **Assess vendor and supply-chain readiness**: Evaluate whether existing hardware security modules, TLS libraries, VPN products, and PKI infrastructure support FIPS 203/204/205. Begin vendor conversations about PQC upgrade roadmaps, especially for long-lead hardware refresh cycles.
- **Track the FAR proposed rule** (due within 180 days of June 22 — by December 19, 2026): Contractors should prepare comments and begin internal gap assessments against NIST FIPS 203/204/205 requirements. The proposed rule comment period will be the primary opportunity to shape contractor compliance timelines.
- **Critical infrastructure operators**: Request early engagement with sector-specific agency liaisons on PQC migration assistance. Even without direct legal obligation, beginning PQC planning now avoids being compressed between future regulatory mandates and vendor lead times.
- **Review CNSA 2.0 compliance if operating National Security Systems**: NSS are carved out of EO 14412 and remain subject to NSA's [CNSA 2.0](https://www.whitehouse.gov/presidential-actions/2026/06/securing-the-nation-against-advanced-cryptographic-attacks/) framework. NSA's 180-day presidential report may produce updated CNSA 2.0 guidance.

## Related Reports

- [NIST Plans Summer 2026 Release of AI Cybersecurity Framework Profile (NISTIR 8596)](reports/cybersecurity/standards-guidance/federal-nistir-8596-cyber-ai-profile-2026-05-19.md) — Both involve NIST-led federal cybersecurity standard-setting that directly affects federal agency procurement and contractor obligations.
- [NERC Explores CIP 100-Series Framework for Cloud and Emerging Technologies in Critical Infrastructure](reports/cybersecurity/critical-infrastructure/federal-nerc-cip-cloud-emerging-tech-framework-2026-04-28.md) — Parallel critical infrastructure cybersecurity rulemaking that may intersect with PQC migration obligations for bulk power system operators under NERC CIP standards.
- [White House AI Cybersecurity Executive Order: Draft Provisions and Postponement](reports/cybersecurity/standards-guidance/federal-ai-cybersecurity-eo-frontier-model-postponed-2026-05-20.md) — Related White House executive action on federal cybersecurity posture; the postponed AI cybersecurity EO may be revived alongside EO 14412 implementation.

## Sources

1. [EO 14412 — Securing the Nation Against Advanced Cryptographic Attacks (White House)](https://www.whitehouse.gov/presidential-actions/2026/06/securing-the-nation-against-advanced-cryptographic-attacks/) — Official text of the primary post-quantum cryptography executive order.
2. [EO 14413 — Ushering in the Next Frontier of Quantum Innovation (White House)](https://www.whitehouse.gov/presidential-actions/2026/06/ushering-in-the-next-frontier-of-quantum-innovation/) — Official text of the companion quantum innovation executive order.
3. [Federal Register: EO 14412, Vol. 91 No. 121, pp. 38483–38486 (June 25, 2026)](https://www.federalregister.gov/documents/2026/06/25/2026-12909/securing-the-nation-against-advanced-cryptographic-attacks) — Official Federal Register publication of EO 14412, document 2026-12909.
4. [Federal Register: EO 14413, Vol. 91 No. 121, pp. 38487–38491 (June 25, 2026)](https://www.federalregister.gov/documents/2026/06/25/2026-12910/ushering-in-the-next-frontier-of-quantum-innovation) — Official Federal Register publication of EO 14413, document 2026-12910.
5. [White House Fact Sheet: Securing the Nation Against Advanced Cryptographic Attacks](https://www.whitehouse.gov/fact-sheets/2026/06/fact-sheet-president-donald-j-trump-secures-the-nation-against-advanced-cryptographic-attacks/) — White House summary of EO 14412 key provisions.
6. [White House Fact Sheet: Ushering in the Next Frontier of Quantum Innovation](https://www.whitehouse.gov/fact-sheets/2026/06/fact-sheet-president-donald-j-trump-ushers-in-the-next-frontier-of-quantum-innovation/) — White House summary of EO 14413 key provisions.
7. [Jenner & Block: Two New Executive Orders on Quantum Computing — Key Takeaways](https://www.jenner.com/en/news-insights/client-alerts/two-new-executive-orders-on-quantum-computing-key-takeaways-for-companies-operating-in-quantum-information-science-and-critical-infrastructure) — Law firm analysis of implications for companies in quantum information science and critical infrastructure.
8. [Cybersecurity Dive: Trump sets new deadlines for agencies and contractors to adopt post-quantum cryptography](https://www.cybersecuritydive.com/news/quantum-cryptography-white-house-executive-order/823530/) — News reporting on the agency and contractor timelines, including the 30- and 90-day near-term actions.
9. [Cloudflare Blog: The post-quantum EO is an important milestone. Now it's time to get to work](https://blog.cloudflare.com/post-quantum-eo-2026/) — Technical industry analysis from a major internet security company, focusing on implementation implications.
10. [Inside Privacy: Trump Administration Releases Two Executive Orders on Quantum](https://www.insideprivacy.com/cybersecurity-2/trump-administration-releases-two-executive-orders-on-quantum/) — Covington & Burling analysis of both EOs.
11. [Federal Register: NIST FIPS 203, 204, and 205 — August 14, 2024](https://www.federalregister.gov/documents/2024/08/14/2024-17956/announcing-issuance-of-federal-information-processing-standards-fips-fips-203-module-lattice-based) — Official publication announcing all three finalized NIST post-quantum cryptography standards jointly (FIPS 203, 204, and 205 are all announced in this single document, despite the title naming only FIPS 203).
12. [NIST CSRC: Post-Quantum Cryptography FIPS Approved](https://csrc.nist.gov/news/2024/postquantum-cryptography-fips-approved) — NIST's official announcement of FIPS 203/204/205 finalization, including NIST IR 8547 classical algorithm deprecation timeline.
13. [DOE: Energy Department Announces Quantum Genesis Initiative](https://www.energy.gov/science/articles/energy-department-announces-initiative-create-and-deploy-worlds-first) — Department of Energy announcement of the QC-ADDS initiative to deliver a fault-tolerant quantum computer by 2028 under EO 14413.
14. [Crowell & Moring: Twin Executive Orders Seek to Spur Quantum Leap in Technology and Cybersecurity](https://www.crowell.com/en/insights/client-alerts/twin-executive-orders-seek-to-spur-quantum-leap-in-technology-and-cybersecurity) — Law firm analysis covering both EOs with focus on technology and cybersecurity implications.
15. [Holland & Knight: President Trump Signs 2 Quantum Executive Orders](https://www.hklaw.com/en/insights/publications/2026/06/president-trump-signs-two-quantum-executive-orders) — Additional law firm analysis of both EOs.
16. [AppViewX: EO 14412 and the Post-Quantum Imperative for Machine Identity](https://www.appviewx.com/blogs/executive-order-14412-post-quantum-imperative-for-machine-identity/) — Technical analysis focusing on certificate management and machine identity implications of EO 14412.
17. [Justia Regulation Tracker: EO 14412, 38483–38486 (2026-12909)](https://regulations.justia.com/regulations/fedreg/2026/06/25/2026-12909.html) — Confirms EO 14412 page range 38483–38486.
18. [Justia Regulation Tracker: EO 14413, 38487–38491 (2026-12910)](https://regulations.justia.com/regulations/fedreg/2026/06/25/2026-12910.html) — Confirms EO 14413 page range 38487–38491.
