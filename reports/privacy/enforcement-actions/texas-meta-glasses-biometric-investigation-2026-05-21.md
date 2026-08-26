---
title: "Texas AG Opens Privacy Investigation into Meta AI Smart Glasses"
date: 2026-05-21
jurisdiction: "Texas"
category: "privacy"
development_type: "enforcement"
finding_id: "SCAN-20260601-017"
topic_key: "texas-02aa4d98-2026"
topic_type: "enforcement_action"
first_reported: 2026-05-21
last_updated: 2026-06-01
status_history: []
cluster: "Texas AG Biometric Data Enforcement: CUBI and Facebook Facial Recognition"
cluster_slug: "texas-ag-biometric-cubi-enforcement"
---

# Texas AG Opens Privacy Investigation into Meta AI Smart Glasses

**Jurisdiction:** Texas | **Category:** privacy | **Date:** 2026-05-21

## Summary [HIGH confidence]

On May 20, 2026, Texas Attorney General Ken Paxton [announced](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-launches-investigation-meta-glasses-protect-texans-privacy-unlawful) the launch of a formal investigation into Meta Platforms, Inc. over privacy concerns surrounding its AI-powered Ray-Ban Meta smart glasses. The AG's office has issued a Civil Investigative Demand (CID) to determine whether Meta deceptively misrepresents its use of consumer data in violation of Texas law, with the investigation targeting alleged unlawful collection of facial geometry, always-on audio/video recording, and subcontractor access to intimate footage. This is the second major enforcement action the Texas AG has directed at Meta over biometric data in under two years, following the record $1.4 billion CUBI settlement reached in July 2024.

## Key Facts [HIGH confidence]

- Attorney General Paxton issued a [Civil Investigative Demand](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-launches-investigation-meta-glasses-protect-texans-privacy-unlawful) (CID) to Meta to examine whether the company "deceptively misrepresents" its use of private consumer data in violation of Texas law, focusing on the Meta AI Glasses (Ray-Ban Meta smart glasses).
- The glasses feature an **"always enabled" mode** that continuously processes video data for Meta AI products. The device's LED recording indicator is not activated during this mode and can be physically obscured, meaning bystanders receive no practical notice that they are being recorded, per the [AG's press release](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-launches-investigation-meta-glasses-protect-texans-privacy-unlawful).
- **Subcontractor access:** Data annotators at [Sama](https://www.biometricupdate.com/202605/texas-ag-opens-investigation-into-meta-glasses-over-privacy-biometric-concerns), a Kenya-based AI training subcontractor working for Meta, reviewed footage captured through the glasses — including videos showing bathroom visits, intimate moments, bank cards, and personal documents. Swedish journalists tracked the data pipeline from glasses worn in Western homes to Sama's Nairobi office; one employee noted that faces are not always automatically blurred despite Meta's representations to that effect, per [CBS Texas](https://www.cbsnews.com/texas/news/meta-glasses-texas-investigation-5-20-2026/).
- **Facial recognition "Name Tag" feature:** Meta's internal roadmap, reported by the [New York Times in February 2026](https://www.macrumors.com/2026/02/13/meta-facial-recognition-smart-glasses/), describes a feature internally codenamed "Name Tag" that would enable real-time identification of individuals captured by the glasses' cameras by collecting and processing their facial geometry — without the knowledge or consent of those individuals.
- The investigation probes potential violations of the [Texas Capture or Use of Biometric Identifier Act (CUBI)](https://statutes.capitol.texas.gov/docs/bc/htm/bc.503.htm), Tex. Bus. & Com. Code Ann. § 503.001 *et seq.*, which prohibits capturing biometric identifiers (including "record of hand or face geometry") for a commercial purpose without prior notice and consent, and the [Texas Deceptive Trade Practices Act (DTPA)](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/consumer-privacy-rights/biometric-identifier-act).
- The [Texas Data Privacy and Security Act (TDPSA)](https://statutes.capitol.texas.gov/Docs/BC/htm/BC.541.htm), Tex. Bus. & Com. Code Ann. § 541.001 *et seq.* (effective July 1, 2024), independently classifies biometric data as "sensitive data," requires explicit consent for its processing, and authorizes penalties of up to $7,500 per violation, per [AG enforcement guidance](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/consumer-privacy-rights/texas-data-privacy-and-security-act).
- In July 2024, Paxton secured a [$1.4 billion settlement](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-secures-14-billion-settlement-meta-over-its-unauthorized-capture) with Meta over Facebook's "tag suggestions" facial recognition feature — the largest settlement ever obtained by a single state and the first enforcement action under CUBI, which was enacted in 2009.
- Other jurisdictions are applying parallel pressure: the UK's Information Commissioner's Office [wrote to Meta](https://www.theregister.com/2026/03/05/ico_meta_glasses/) in March 2026 requesting information about data protection compliance, and a [civil class action](https://techcrunch.com/2026/03/05/meta-sued-over-ai-smartglasses-privacy-concerns-after-workers-reviewed-nudity-sex-and-other-footage/) was filed March 5, 2026 alleging false advertising and privacy violations based on the same Sama subcontractor disclosures.

## Legal Framework [HIGH confidence]

**Texas Capture or Use of Biometric Identifier Act (CUBI), Tex. Bus. & Com. Code Ann. § 503.001 *et seq.***

CUBI defines "biometric identifier" to include a "record of hand or face geometry" — directly implicating the facial geometry data Meta's glasses capture and the Name Tag feature would process. The statute prohibits capturing such identifiers for a commercial purpose unless the company: (1) informs the individual before capture, and (2) obtains written consent. It also prohibits selling, leasing, or disclosing biometric identifiers without consent, subject to narrow exceptions. Violations are subject to a civil penalty of up to $25,000 per violation, and the AG may bring an enforcement action to recover those penalties. The [official statute text is available from the Texas Legislature](https://statutes.capitol.texas.gov/docs/bc/htm/bc.503.htm).

**Texas Data Privacy and Security Act (TDPSA), Tex. Bus. & Com. Code Ann. § 541.001 *et seq.***

The TDPSA, effective July 1, 2024, classifies biometric data as "sensitive data" and requires that a controller obtain consent before processing sensitive data. Meta, as a controller, must obtain explicit consent before collecting biometric data from Texas consumers. Violations following a failed 30-day cure period carry civil penalties up to $7,500 per violation. The AG has exclusive enforcement authority. [Official TDPSA statute text is available from the Texas Legislature](https://statutes.capitol.texas.gov/Docs/BC/htm/BC.541.htm).

**Texas Deceptive Trade Practices Act (DTPA)**

The CID issued to Meta appears to target potential false or misleading representations about how user data is handled — including representations that recorded faces are automatically blurred before review by contractors. If Meta's privacy representations were misleading, the DTPA provides an independent enforcement basis. The 2024 settlement established that the AG will pursue large monetary recoveries under DTPA in conjunction with CUBI.

## Action Items

- **Operators of AI-enabled wearables and ambient recording devices** in Texas must obtain informed, prior written consent before capturing facial geometry data of any individual — including bystanders — for commercial purposes. Reliance on passive indicators (such as an LED) is insufficient if those indicators are not active during data-processing modes.
- **Companies using AI training subcontractors** should audit their data annotation pipelines for compliance with CUBI and TDPSA: subcontractor access to raw footage containing identifiable individuals' biometric data likely constitutes a "disclosure" under CUBI requiring consent or qualifying exception.
- **Review privacy representations**: Meta's investigation is partly premised on alleged misrepresentations (automatic face blurring). Companies should audit public-facing privacy policies, product disclosures, and user agreements for accuracy against actual data handling practices.
- **Monitor Name Tag and similar planned features**: The CID probes not only existing functionality but also internal product roadmaps. Companies should treat pre-launch biometric feature design as subject to CUBI and TDPSA compliance review — not just post-launch audits.
- **Assess TDPSA obligations independently of CUBI**: Unlike CUBI's commercial-purpose focus, TDPSA applies whenever biometric data is "processed for the purpose of uniquely identifying an individual." Companies should confirm whether their use of facial data or voice/geometry measurements triggers TDPSA's sensitive data consent requirement.
- **Watch for escalation to litigation**: The AG's CID is investigative, not a lawsuit. However, the 2022-to-2024 Meta trajectory (CID/investigation → lawsuit → $1.4B settlement) establishes a clear enforcement playbook; companies under investigation should prepare for formal litigation if CID responses are unsatisfactory.

## Related Reports

- [reports/privacy/federal-meta-smart-glasses-facial-recognition-coalition-2026-04-14.md](reports/privacy/federal-meta-smart-glasses-facial-recognition-coalition-2026-04-14.md) — ACLU-led 75-organization letter demanding Meta halt the same "Name Tag" facial recognition feature that is central to the Texas AG investigation.
- [reports/privacy/enforcement-actions/texas-allstate-arity-tdpsa-enforcement-2026-04-14.md](reports/privacy/enforcement-actions/texas-allstate-arity-tdpsa-enforcement-2026-04-14.md) — Texas AG's first-ever TDPSA enforcement action (Allstate/Arity), establishing the enforcement model and penalty framework under the same statute implicated here.

## Sources

1. [Texas AG Press Release: Paxton Launches Investigation Into Meta Glasses](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-launches-investigation-meta-glasses-protect-texans-privacy-unlawful) — Official announcement from the Texas Office of the Attorney General, May 20, 2026; primary source for investigation details, CID issuance, and privacy concerns cited.
2. [Texas Business and Commerce Code Chapter 503 (CUBI) — Official Statute Text](https://statutes.capitol.texas.gov/docs/bc/htm/bc.503.htm) — Official Texas Legislature source; text of the Capture or Use of Biometric Identifier Act including definitions, consent requirements, and penalty provisions.
3. [Texas Business and Commerce Code Chapter 541 (TDPSA) — Official Statute Text](https://statutes.capitol.texas.gov/Docs/BC/htm/BC.541.htm) — Official Texas Legislature source; text of the Texas Data Privacy and Security Act including sensitive data definition, consent requirements, and AG enforcement authority.
4. [Texas AG: TDPSA Consumer Protection Page](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/consumer-privacy-rights/texas-data-privacy-and-security-act) — AG's official consumer guidance on TDPSA scope and enforcement process.
5. [Texas AG: CUBI Consumer Protection Page](https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/consumer-privacy-rights/biometric-identifier-act) — AG's official consumer guidance on CUBI scope, definitions, and filing complaints.
6. [Texas AG Press Release: $1.4 Billion Settlement with Meta (July 2024)](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-secures-14-billion-settlement-meta-over-its-unauthorized-capture) — Official AG announcement of the prior CUBI settlement establishing enforcement precedent; key for contextualizing new investigation.
7. [Biometric Update: Texas AG Opens Investigation into Meta Glasses](https://www.biometricupdate.com/202605/texas-ag-opens-investigation-into-meta-glasses-over-privacy-biometric-concerns) — Specialist biometrics publication; reporting on Sama subcontractor data pipeline and investigation details.
8. [CBS Texas: Texas AG Investigates Meta Over AI Glasses](https://www.cbsnews.com/texas/news/meta-glasses-texas-investigation-5-20-2026/) — Local reporting with additional detail on subcontractor face-blurring discrepancies.
9. [National Law Review: Texas AG Opens Investigation Into Meta Glasses](https://natlawreview.com/article/texas-ag-opens-investigation-meta-glasses-reviving-biometric-privacy-pressure-meta) — Legal analysis of enforcement context, CID scope, and implications for pre-launch product features.
10. [MacRumors: Meta Plans "Name Tag" Facial Recognition for Ray-Ban Smart Glasses](https://www.macrumors.com/2026/02/13/meta-facial-recognition-smart-glasses/) — Reporting on the internal "Name Tag" feature and the internal Meta document describing planned rollout.
11. [TechCrunch: Meta Sued Over AI Smart Glasses Privacy Concerns](https://techcrunch.com/2026/03/05/meta-sued-over-ai-smartglasses-privacy-concerns-after-workers-reviewed-nudity-sex-and-other-footage/) — Coverage of the March 5, 2026 class action filed over Sama subcontractor access to sensitive footage.
12. [The Register: Meta Smart Glasses Face UK Privacy Probe](https://www.theregister.com/2026/03/05/ico_meta_glasses/) — UK ICO's parallel investigation launched March 2026, providing international regulatory context.
13. [Crowell & Moring: Texas Targets Big Tech With Wave of Suits and Investigations](https://www.crowell.com/en/insights/client-alerts/texas-targets-big-tech-with-wave-of-suits-and-investigations-part-of-nationwide-trend) — Law firm client alert contextualizing Texas AG enforcement trends against large technology companies.
14. [WFAA: Texas AG Ken Paxton Launches Investigation Into Meta AI Glasses](https://www.wfaa.com/article/news/local/texas/texas-ken-paxton-investigation-into-meta-ai-glasses-over-privacy-concerns/287-92a8d11d-49f9-42a5-b840-32d8a061863d) — Local news coverage with additional background on the investigation announcement.
