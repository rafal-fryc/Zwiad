---
title: "Clarifai Deletes 3 Million OkCupid User Photos and AI Models Following FTC Settlement"
date: 2026-04-22
jurisdiction: "Federal"
category: "privacy"
development_type: "enforcement"
finding_id: "SCAN-20260422-016"
topic_key: "FTC-CLARIFAI-DELETES-OKCUPID-USER-2026"
topic_type: "enforcement_action"
first_reported: 2026-04-21
last_updated: 2026-04-22
status_history: []
cluster: "FTC Enforcement: Match Group/OkCupid Data Sharing with Clarifai"
cluster_slug: "ftc-match-group-okcupid-clarifai-enforcement"
---

# Clarifai Deletes 3 Million OkCupid User Photos and AI Models Following FTC Settlement

**Jurisdiction:** Federal | **Category:** Privacy | **Date:** 2026-04-22

## Summary [HIGH confidence]

AI company Clarifai certified to the FTC on April 7, 2026, that it had deleted approximately three million OkCupid user photos and all facial recognition models trained on that data, completing the remediation phase of the FTC's March 30, 2026 enforcement action against Match Group and OkCupid. Clarifai also confirmed to Congress on April 16, 2026, that it had not shared the data with third parties. The deletion — spanning not just the raw photos but every AI model derived from them — marks a concrete application of the FTC's "algorithmic disgorgement" approach to AI enforcement and illustrates the agency's willingness to reach non-party AI companies as part of privacy settlements.

## Key Facts [HIGH confidence]

- **Settlement context:** On March 30, 2026, the FTC filed a complaint and stipulated final order against Match Group Americas and OkCupid (Humor Rainbow, Inc.) in Case No. 3:26-cv-00996-K (N.D. Tex.) for sharing nearly three million user photos plus location and demographic data with Clarifai in 2014, in violation of OkCupid's own privacy policy. The FTC alleged deceptive acts or practices under Section 5 of the FTC Act, 15 U.S.C. § 45 ([FTC Press Release](https://www.ftc.gov/news-events/news/press-releases/2026/03/ftc-takes-action-against-match-okcupid-deceiving-users-sharing-personal-data-third-party)).

- **Clarifai's deletion certification:** Clarifai — which was not a named defendant in the FTC action — voluntarily certified to the FTC on April 7, 2026, that it had deleted all approximately three million OkCupid user photos it received in 2014 ([TechCrunch](https://techcrunch.com/2026/04/21/clarifai-okcupid-facial-recognition-ai-ftc-settlement/)).

- **AI model destruction included:** Clarifai confirmed it also deleted any facial recognition AI models trained on the OkCupid data, going beyond the raw dataset to destroy derivative AI work product ([Engadget](https://www.engadget.com/ai/ai-company-deletes-the-3-million-okcupid-photos-it-used-for-facial-recognition-training-195223996.html)).

- **Congressional notification:** On April 16, 2026, Clarifai notified the office of Representative Lori Trahan (D-MA) that it had deleted the data and models and had not shared the data with third parties. Representative Trahan described the deletion as "a step in the right direction," while criticizing the FTC for settling without financial penalties ([The Next Web](https://thenextweb.com/news/clarifai-okcupid-photos-deleted-ftc-settlement)).

- **No monetary penalty:** The FTC settlement does not include a financial penalty against OkCupid or Match Group. The FTC lacks statutory authority to impose civil monetary penalties for first-time Section 5 violations of this type. The consent order permanently prohibits the companies from misrepresenting their data practices and requires ten years of compliance reporting ([Venable LLP](https://www.venable.com/insights/publications/2026/04/ftc-okcupid-settlement-deceptive-data-sharing)).

- **Origin of the data transfer:** OkCupid's founders were personal financial investors in Clarifai. In 2014, Clarifai founder Matthew Zeiler contacted OkCupid co-founder Maxwell Krohn requesting data. OkCupid provided the photos with no written agreement, no use restrictions, and no user notification, directly contrary to its published privacy policy ([Engadget](https://www.engadget.com/ai/ai-company-deletes-the-3-million-okcupid-photos-it-used-for-facial-recognition-training-195223996.html)).

- **Obstruction during investigation:** OkCupid publicly denied involvement with Clarifai when media reports surfaced, and the companies obstructed the FTC's Civil Investigative Demand, requiring court enforcement. The complaint treats this obstruction as an aggravating factor ([Biometric Update](https://www.biometricupdate.com/202603/ftc-order-bars-okcupid-from-misleading-users-about-biometric-data-sharing)).

- **Retroactive reach:** The FTC investigation traced data-sharing conduct from September 2014 — approximately twelve years before the settlement — illustrating the agency's willingness to investigate and pursue historical data practices even absent any current statutory framework governing AI training data.

- **First Section 5 privacy action under current FTC Chair:** This is the first Section 5 privacy enforcement action under FTC Chair Andrew Ferguson, signaling continuity of FTC privacy enforcement into the new administration ([ComplexDiscovery](https://complexdiscovery.com/ftcs-okcupid-action-reframes-ai-training-data-as-a-consumer-protection-issue/)).

## Enforcement Pattern: Algorithmic Disgorgement [HIGH confidence]

The Clarifai deletion illustrates a recurring FTC enforcement mechanism — requiring destruction not only of improperly obtained personal data but also of AI models built on that data. The FTC has applied this "algorithmic disgorgement" remedy in prior settlements:

- **Everalbum (2021):** FTC required deletion of facial recognition models trained on photos collected without proper consent. Users who had deactivated accounts had their data and derived models destroyed ([FTC Policy Statement on Biometric Information](https://www.ftc.gov/legal-library/browse/policy-statement-federal-trade-commission-biometric-information-section-5-federal-trade-commission)).

- **Rite Aid (2023):** FTC banned the retailer from using AI facial recognition systems for five years following allegations it deployed the technology without reasonable safeguards under Section 5 ([FTC Rite Aid Action](https://www.ftc.gov/news-events/news/press-releases/2023/12/rite-aid-banned-using-ai-facial-recognition-after-ftc-says-retailer-deployed-technology-without)).

- **Operation AI Comply (2024):** On September 25, 2024, the FTC announced enforcement actions against five companies for deceptive AI practices, applying similar disgorgement and prohibition frameworks ([FTC Operation AI Comply](https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes)).

The OkCupid/Clarifai case adds a new dimension: a non-party AI vendor (Clarifai) independently certifying deletion to both the regulator and Congress, without being a named defendant. This voluntary cooperation model may set an informal standard for how AI companies receiving third-party datasets should respond when those datasets become the subject of enforcement.

## Significance: Consent as an AI Training Prerequisite [MEDIUM confidence]

Multiple industry analysts characterize the settlement as marking a shift in how the FTC frames AI training data — treating privacy policy representations as legally binding constraints on training data collection, not merely aspirational commitments. Key observations from law firm analysis:

- **Privacy policy as hard constraint:** Venable LLP notes that the settlement reaffirms that privacy policies create enforceable obligations; a company cannot share data with an AI training vendor if that sharing falls outside the policy's described categories, even absent a specific "AI training" prohibition ([Venable LLP](https://www.venable.com/insights/publications/2026/04/ftc-okcupid-settlement-deceptive-data-sharing)).

- **Conflict-of-interest data sharing:** The FTC's complaint specifically emphasized that OkCupid's founders held financial interests in Clarifai and that no formal business relationship existed. This framing signals that investor-relationship data sharing receives heightened FTC scrutiny.

- **No compliance program obligations:** Unlike many prior FTC consent orders, the OkCupid order does not require the companies to implement a formal privacy program or undergo third-party assessments. Venable characterizes this as "minimal affirmative obligations" compared to prior FTC privacy orders, consistent with the current administration's more limited regulatory approach ([Venable LLP](https://www.venable.com/insights/publications/2026/04/ftc-okcupid-settlement-deceptive-data-sharing)).

- **Criticism of penalty-free settlement:** Critics, including Representative Trahan and privacy advocacy groups, argue the lack of monetary penalties and user compensation leaves affected users without meaningful redress for a decade-old biometric privacy violation. The settlement's absence of financial penalties has renewed calls for federal comprehensive privacy legislation with private rights of action ([State of Surveillance](https://stateofsurveillance.org/news/okcupid-ftc-settlement-clarifai-facial-recognition-3-million-photos-2026/)).

## Action Items

- **Audit AI training data pipelines for third-party sourcing.** If your organization received training data from a platform company — particularly under informal or investor-relationship arrangements — verify that the source had legal authority to transfer the data under its privacy policy and applicable law at the time of transfer. Historical transfers with inadequate documentation now carry retroactive enforcement risk.

- **Review third-party AI vendor agreements for deletion obligations.** Contracts with AI vendors that received your users' personal data should include enforceable data deletion requirements covering both raw data and derivative models. The Clarifai deletion demonstrates regulators expect model destruction, not just dataset deletion.

- **Align privacy policies with all current data-sharing arrangements.** Confirm every active data-sharing relationship falls within the categories described in your published privacy policy. The FTC's core legal theory here — deception through policy non-compliance — requires no special AI statute; it applies to any gap between stated and actual practices.

- **Establish conflict-of-interest controls for data access decisions.** Implement internal review and approval requirements for data sharing with entities in which officers, founders, directors, or significant shareholders hold financial interests. Document the business justification independently of any personal investment relationship.

- **Preserve documentation of data-sharing decisions.** Given the FTC's twelve-year retrospective reach in this case, organizations should maintain contemporaneous records of what data was shared, with whom, under what legal authority, and what restrictions applied. These records are critical for demonstrating compliance in the event of a future investigation.

## Related Reports

- [reports/privacy/enforcement-actions/ftc-match-okcupid-clarifai-enforcement-2026-04-07.md](../enforcement-actions/ftc-match-okcupid-clarifai-enforcement-2026-04-07.md) — Primary report on the March 30, 2026 FTC complaint and consent order against Match Group and OkCupid; this report covers the subsequent Clarifai data deletion development.
- [reports/privacy/enforcement-actions/ftc-strategic-plan-fy2026-2030-2026-04-13.md](../enforcement-actions/ftc-strategic-plan-fy2026-2030-2026-04-13.md) — FTC's FY 2026-2030 Strategic Plan, providing context for continued privacy and AI enforcement priorities under the new administration.

## Sources

1. [FTC Press Release — FTC Takes Action Against Match and OkCupid](https://www.ftc.gov/news-events/news/press-releases/2026/03/ftc-takes-action-against-match-okcupid-deceiving-users-sharing-personal-data-third-party) — Official FTC announcement of the March 30, 2026 enforcement action and settlement terms
2. [FTC Case Page — OkCupid/Match](https://www.ftc.gov/legal-library/browse/cases-proceedings/okcupidmatch) — Official case proceedings page with links to complaint, stipulated order, and timeline
3. [TechCrunch — Clarifai deletes 3 million photos that OkCupid provided to train facial recognition AI](https://techcrunch.com/2026/04/21/clarifai-okcupid-facial-recognition-ai-ftc-settlement/) — Primary reporting on Clarifai's April 7, 2026 deletion certification to FTC
4. [Engadget — AI company deletes the 3 million OKCupid photos it used for facial recognition training](https://www.engadget.com/ai/ai-company-deletes-the-3-million-okcupid-photos-it-used-for-facial-recognition-training-195223996.html) — Additional details on Clarifai's model and data deletion
5. [The Next Web — FTC settles OkCupid data scandal with no fine](https://thenextweb.com/news/clarifai-okcupid-photos-deleted-ftc-settlement) — Coverage of Representative Trahan's response and congressional engagement
6. [Venable LLP — FTC OkCupid Settlement: Deceptive Data Sharing, Privacy Policy Compliance, and Section 5 Takeaways](https://www.venable.com/insights/publications/2026/04/ftc-okcupid-settlement-deceptive-data-sharing) — Law firm analysis of settlement terms, legal theory, and compliance implications
7. [Inside Privacy (Covington) — FTC Alleges OkCupid Data Sharing Amounted to a Deceptive Practice](https://www.insideprivacy.com/united-states/federal-trade-commission/ftc-alleges-okcupid-data-sharing-amounted-to-a-deceptive-practice/) — Law firm analysis of the deceptive practice theory under Section 5
8. [Biometric Update — FTC order bars OkCupid from misleading users about biometric data sharing](https://www.biometricupdate.com/202603/ftc-order-bars-okcupid-from-misleading-users-about-biometric-data-sharing) — Coverage of obstruction allegations and biometric data aspects
9. [ComplexDiscovery — FTC's OkCupid Action Reframes AI Training Data as a Consumer Protection Issue](https://complexdiscovery.com/ftcs-okcupid-action-reframes-ai-training-data-as-a-consumer-protection-issue/) — Analysis of enforcement pattern and first-action-under-Ferguson significance
10. [FTC — Rite Aid Banned from Using AI Facial Recognition (December 2023)](https://www.ftc.gov/news-events/news/press-releases/2023/12/rite-aid-banned-using-ai-facial-recognition-after-ftc-says-retailer-deployed-technology-without) — Prior biometric AI enforcement action for comparison to algorithmic disgorgement pattern
11. [FTC — Operation AI Comply Announcement (September 2024)](https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes) — FTC's 2024 AI enforcement sweep context
12. [FTC Policy Statement on Biometric Information and Section 5](https://www.ftc.gov/legal-library/browse/policy-statement-federal-trade-commission-biometric-information-section-5-federal-trade-commission) — FTC's biometric enforcement policy framework underlying the consent theory
13. [State of Surveillance — OkCupid Gave 3 Million Photos to a Facial Recognition Company. The FTC's Punishment? Nothing.](https://stateofsurveillance.org/news/okcupid-ftc-settlement-clarifai-facial-recognition-3-million-photos-2026/) — Critical perspective on absence of monetary penalties and user redress
