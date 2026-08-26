---
title: "California AI Transparency Act (SB 942): Watermarking and Disclosure Requirements for Large Generative AI Providers"
date: 2024-10-18
jurisdiction: "California"
category: "privacy"
development_type: "legislation"
finding_id: "SCAN-20241018-009"
topic_key: "california-08ffd21f-2024"
topic_type: "state_bill"
first_reported: 2024-10-18
last_updated: 2026-04-16
status_history:
  - "2026-04-16: Round 2 revision — corrected section numbering: disclosure requirements moved from Section 22757.1 to Section 22757.3 (a)/(b); licensee obligations clarified as Section 22757.3(c); Section 22757.1 correctly identified as Definitions section."
cluster: "California September 2024 AI Legislative Package (AB 2013, SB 942, and Related Bills)"
cluster_slug: "california-sep-2024-ai-legislative-package"
---

# California AI Transparency Act (SB 942): Watermarking and Disclosure Requirements for Large Generative AI Providers

**Jurisdiction:** California | **Category:** Privacy / AI Law | **Date:** October 18, 2024

## Executive Summary [HIGH confidence]

On September 19, 2024, Governor Gavin Newsom signed [SB 942](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB942), the California AI Transparency Act (CAITA), into law. The Act requires large generative AI (GenAI) system providers — defined as those with more than one million monthly users or visitors in California — to offer a free AI content detection tool, embed latent provenance metadata in AI-generated audio, image, and video content, and offer users the option to include a visible manifest disclosure. Penalties reach $5,000 per violation per day, enforceable exclusively by the California Attorney General and local attorneys — there is no private right of action. The Act was originally scheduled to take effect January 1, 2026, but October 2025 amendments via [AB 853](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB853) delayed the operative date for existing provisions to August 2, 2026, and added phased obligations through January 1, 2028. The Act is currently subject to federal preemption pressure under President Trump's December 2025 executive order, though state laws remain enforceable pending Congressional action or court rulings.

## Background [HIGH confidence]

California's SB 942 emerged from a growing national concern about AI-generated deepfakes, synthetic media manipulation, and the inability of consumers to distinguish authentic content from AI-generated material. The legislation follows a wave of state activity on AI transparency and disclosure, including Utah's AI Policy Act (2024) and Colorado's SB 24-205 (2024), and sits alongside California's companion measure [AB 2013](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2013), the Generative AI Training Data Transparency Act, which requires GenAI developers to post documentation about training data.

SB 942 was authored by Senator Josh Becker and is codified as Chapter 25 of Division 8 of the California Business and Professions Code (commencing with Section 22757). The bill passed the legislature with bipartisan support and was signed on September 19, 2024 — the same day Newsom signed several other AI-related measures, while vetoing several others including the high-profile SB 1047 AI safety bill.

The law targets a specific and growing harm: undetectable AI-generated synthetic media. It does not regulate AI systems broadly but rather focuses on large consumer-facing GenAI platforms — those with sufficient reach to create significant societal risk from unattributed synthetic content. Notably, the Act applies only to audio, image, and video content; text-only AI output is explicitly excluded from the disclosure requirements.

In October 2025, California enacted [AB 853](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB853), which amended CAITA in two significant ways: it delayed the operative date of the original SB 942 provisions from January 1, 2026 to August 2, 2026, and it added new requirements on large online platforms (distinct from covered providers) to retain provenance metadata, detect and label provenance data, provide authenticity warnings, and maintain compliant metadata. Those additional platform obligations phase in on January 1, 2027, and January 1, 2028.

## Detailed Analysis [HIGH confidence]

### Covered Provider Definition

A "Covered Provider" is defined as a person that creates, codes, or otherwise produces a generative AI system that: (1) has over 1,000,000 monthly visitors or users, and (2) is publicly accessible within the geographic boundaries of California. This threshold-based definition — keyed to monthly active users rather than to computing power or model capability — is broader than thresholds used in some other AI regulatory frameworks and reaches a significant number of consumer-facing GenAI platforms currently operating at scale.

Critically, a covered provider does not need to be headquartered in California. Any entity whose GenAI system is accessible to and used by California residents at the applicable scale falls within the definition, consistent with California's longstanding extraterritorial approach to consumer protection regulation.

### Disclosure Requirements (Section 22757.3)

Section 22757.3 of the Business and Professions Code contains both the manifest disclosure option and the mandatory latent disclosure requirement within its subdivisions (a) and (b), with licensee obligations in subdivision (c). Note that Section 22757.1 is the definitions section of Chapter 25, providing the statutory definitions for terms including "artificial intelligence," "covered provider," "generative AI system," and "capture device."

**Section 22757.3(a) — Manifest Disclosure (User-Optional)**

Section 22757.3(a) requires covered providers to offer each user the **option** to include a manifest disclosure — a visible, human-readable label — in AI-generated or AI-altered audio, image, or video content. The manifest disclosure must:

- Identify the content as AI-generated or AI-altered;
- Be clear, conspicuous, and appropriate for the medium;
- Be understandable to a reasonable person;
- Be permanent or extraordinarily difficult to remove, to the extent technically feasible.

Unlike the latent disclosure (which is mandatory for covered providers to embed), the manifest disclosure is user-initiated — providers must offer the option, but users may choose not to apply it. This structure preserves user autonomy while ensuring that providers build the capability into their systems.

**Section 22757.3(b) — Latent Disclosure (Mandatory)**

Section 22757.3(b) requires covered providers to include a **latent disclosure** in AI-generated image, video, or audio content (or any combination). The latent disclosure must:

- Be embedded directly within the content (not merely accompanying it);
- Be detectable by the provider's free detection tool;
- Be permanent or extraordinarily difficult to remove, to the extent technically feasible;
- Convey, either directly or via a link to a permanent internet website: (a) the name of the covered provider; (b) information about the specific AI system used; (c) the time and date the content was created; and (d) a unique identifier for the content.

These requirements are consistent with standards promoted by the [Coalition for Content Provenance and Authenticity (C2PA)](https://c2pa.org/) and the IPTC Photo Metadata Standard. Industry analysts and law firm commentators have noted that compliance-grade implementation will likely need to conform to C2PA or equivalent open interoperability standards to meet the detectability requirement across platforms. Covered providers are not expressly required to use C2PA, but the technical specifications for permanence and detectability strongly favor open-standard watermarking approaches over proprietary methods.

### Free AI Detection Tool (Section 22757.2)

Section 22757.2 requires covered providers to make available — at no cost and accessible to the public — an AI content detection tool that allows users to assess whether image, video, or audio content was created or altered by the covered provider's GenAI system. The tool must be capable of detecting the latent disclosures embedded in content the provider's system generated. This requirement effectively forces providers to build and maintain detection infrastructure in parallel with their generative systems — a meaningful technical and operational commitment.

### Third-Party Licensee Obligations (Section 22757.3(c))

Section 22757.3(c) governs contractual obligations when a covered provider licenses its GenAI system to a third party. For context, Sections 22757.3(a) and (b) establish the manifest and latent disclosure requirements directly; Section 22757.3(c) extends compliance responsibility into the provider's downstream distribution chain. The provider must require by contract that the licensee maintain the system's capability to include the required disclosures. A covered provider must revoke the license within 96 hours of discovering that the licensee has altered the system to disable the disclosure capability. Upon revocation, the licensee must cease using the system. These contractual flow-down obligations are novel in state AI law and create a compliance monitoring responsibility for providers throughout their distribution chain, as [analyzed by Orrick](https://www.orrick.com/en/Insights/2025/01/Navigating-the-California-AI-Transparency-Act-New-Contract-Requirements).

### Penalties and Enforcement

A covered provider that violates CAITA is liable for a civil penalty of **$5,000 per violation**, with each day of non-compliance constituting a separate violation. Actions may be filed by the California Attorney General, a city attorney, or a county counsel. There is no private right of action. A prevailing plaintiff is entitled to reasonable attorneys' fees and costs, as documented in analysis by [Kilpatrick Townsend & Stockton LLP](https://ktslaw.com/en/Insights/Alert/2024/10/AI-Transparency-and-Compliance-Key-Takeaways-from-Californias-AI-Transparency-Act).

### AB 853 Amendments and Phased Implementation (October 2025)

[AB 853](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB853), signed by Governor Newsom on October 13, 2025, made the following changes to CAITA:

- **Delayed operative date**: Original SB 942 provisions moved from January 1, 2026 to August 2, 2026;
- **New platform obligations**: Large online platforms (not just GenAI providers) must retain available provenance data in content posted on their platforms, detect and label provenance data, provide authenticity warnings, and maintain compliant metadata. These obligations phase in January 1, 2027 and January 1, 2028.

As noted by [Troutman Pepper](https://www.troutmanprivacy.com/2025/10/california-ai-transparency-act-amendments-signed-into-law/) and [Infobytes by Orrick](https://infobytes.orrick.com/2025-10-17/california-delays-its-ai-transparency-act-and-passes-new-content-laws/), the delay was attributed in part to industry implementation challenges and the need for technical standards to mature.

### Federal Preemption Dynamics

On December 11, 2025, President Trump signed an executive order titled "[Ensuring a National Policy Framework for Artificial Intelligence](https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/)," directing the Department of Justice to establish an AI Litigation Task Force to challenge state AI laws deemed inconsistent with a federal policy framework. The order conditions certain federal funding on states refraining from enforcing conflicting AI laws. While California's AI laws were not individually named in the final order — Colorado's AI Act was explicitly singled out — the order creates broad legal uncertainty. Multiple law firms, including [Gibson Dunn](https://www.gibsondunn.com/president-trump-latest-executive-order-on-ai-seeks-to-preempt-state-laws/) and [Goodwin](https://www.goodwinlaw.com/en/insights/publications/2025/12/alerts-otherindustries-trumps-ai-preemption-executive-order), have noted that the executive order itself cannot overturn existing state law — that requires Congressional action or a judicial ruling. California AG Rob Bonta signaled that his office would examine the legality of the preemption order. As of April 2026, no federal court has enjoined CAITA enforcement.

## Impact Assessment [HIGH confidence]

### Affected Entities

The Act directly targets large consumer-facing GenAI platforms. As of the time of writing, the most likely covered providers include major AI image, video, and audio generation platforms exceeding 1,000,000 monthly California users. Providers that license their models to third parties — including API-based B2B licensors — have additional contractual compliance obligations regardless of whether their own consumer-facing products cross the threshold. Smaller startups and enterprise-focused providers below the 1,000,000-user threshold are not covered providers under the original SB 942 provisions, though they may become subject to the AB 853 platform obligations if they operate large content platforms.

The law does not apply to text-only AI outputs, meaning large-language-model chat interfaces (without image/audio/video generation) are not currently within scope.

### Compliance Timeline

| Obligation | Deadline |
|---|---|
| Original SB 942 provisions (latent disclosure, manifest disclosure option, free detection tool, licensee contracts) | **August 2, 2026** |
| AB 853 large online platform obligations (Phase 1) | **January 1, 2027** |
| AB 853 large online platform obligations (Phase 2) | **January 1, 2028** |

### Technical Compliance Considerations

Compliance requires: (1) building or integrating C2PA-compatible or equivalent watermarking into content generation pipelines; (2) deploying a public-facing detection tool capable of reading embedded provenance metadata; (3) updating API licensing agreements with flow-down disclosure obligations and a 96-hour license revocation mechanism; and (4) building user interface features offering the manifest disclosure option at the point of content generation.

Law firm analyses from [TrustArc](https://trustarc.com/resource/california-ai-transparency-laws-sb942-ab2013/) and [Fairnow](https://fairnow.ai/guide/california-ai-transparency-act/) recommend that covered providers begin technical implementation well in advance of the August 2, 2026 operative date given the non-trivial engineering requirements for durable, interoperable metadata embedding.

### Enforcement Outlook

Enforcement is limited to public actions by the California AG and local attorneys — no private plaintiffs can file suit. The $5,000 per violation per day structure can accrue rapidly against a large provider with widespread non-compliance; a single non-compliant content type sustained over one month could generate six-figure liability. The California AG's office has recently demonstrated willingness to pursue tech sector enforcement (see CPPA enforcement activity and concurrent AI-related enforcement monitoring), making public enforcement a realistic near-term risk once the law becomes operative.

The federal preemption dynamic introduces uncertainty but does not suspend enforcement obligations. Until a court enjoins CAITA or Congress passes preemptive federal AI legislation, covered providers should treat the August 2, 2026 operative date as controlling.

## Action Items

- **Audit current systems**: Identify whether your GenAI audio, image, or video systems exceed 1,000,000 monthly California users; document the threshold analysis for each product line.
- **Assess licensee relationships**: Review all agreements under which your GenAI system is licensed to third parties; begin drafting contractual amendments to include flow-down disclosure obligations and the 96-hour revocation mechanism required by Section 22757.3(c).
- **Initiate technical implementation**: Evaluate C2PA-compatible watermarking libraries and provenance metadata solutions; engage your engineering team on integration into content generation pipelines before Q1 2026 to allow adequate testing before the August 2, 2026 deadline.
- **Build user-facing disclosure UX**: Design and implement the manifest disclosure option in content creation user interfaces per Section 22757.3(a); the option must be clear, conspicuous, and offered at the moment of content creation or export.
- **Deploy detection tool**: Plan and test the free, publicly accessible AI content detection tool required by Section 22757.2; coordinate with your trust-and-safety or product teams on hosting and availability requirements.
- **Monitor AB 853 platform obligations**: If you operate a large online content platform (separate from the GenAI provider role), track the phased January 1, 2027 and January 1, 2028 implementation deadlines and begin compliance planning now.
- **Track federal preemption**: Monitor DOJ AI Litigation Task Force activity, any federal preemption legislation introduced in Congress, and any court challenges to CAITA; adjust compliance timelines only upon a court order or enacted federal statute — do not treat the executive order alone as suspending state obligations.
- **Coordinate with AB 2013 compliance**: If you are also a GenAI developer subject to AB 2013 training data disclosure requirements (operative January 1, 2026), align compliance programs to reduce duplicative effort.

## Related Reports

- [reports/ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md](../ai-law/trump-ai-executive-order-state-preemption-2026-04-12.md) — The December 2025 Trump executive order directly targets state AI laws including CAITA, creating federal preemption pressure on California's AI transparency enforcement.
- [reports/ai-law/state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md](../ai-law/state-legislation/colorado-ai-act-enforcement-delayed-2026-04-13.md) — Colorado's AI Act faces the same federal preemption dynamics and delayed enforcement timeline, providing a comparative state AI regulatory context.
- [reports/ai-law/state-legislation/utah-uaipa-ai-disclosure-cozen-2024-05-15.md](../ai-law/state-legislation/utah-uaipa-ai-disclosure-cozen-2024-05-15.md) — Utah's AI Policy Act (2024) established an earlier state-level AI disclosure framework applicable to regulated occupations and healthcare, making it a precursor to California's broader content disclosure approach.
- [reports/privacy/california-cppa-opposes-apra-federal-preemption-2024-05-14.md](california-cppa-opposes-apra-federal-preemption-2024-05-14.md) — The California Privacy Protection Agency's opposition to federal privacy preemption parallels California's likely posture on federal AI preemption efforts targeting CAITA.

## Sources

1. [Bill Text - SB-942 California AI Transparency Act (California Legislature)](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB942) — Official enrolled bill text and legislative history for SB 942.
2. [AB 853 - California Legislative Information](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB853) — Official text of the 2025 amendments delaying CAITA operative date and adding platform obligations.
3. [AB 2013 - Generative Artificial Intelligence: Training Data (California Legislature)](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB2013) — Companion California AI transparency law on training data disclosure.
4. [AI Transparency and Compliance – Key Takeaways from California's AI Transparency Act (Kilpatrick Townsend & Stockton LLP)](https://ktslaw.com/en/Insights/Alert/2024/10/AI-Transparency-and-Compliance-Key-Takeaways-from-Californias-AI-Transparency-Act) — Primary source law firm analysis of SB 942 provisions, definitions, and penalties (October 2024).
5. [California Enacts AI Transparency Law Requiring Disclosures for AI Content (Jones Day)](https://www.jonesday.com/en/insights/2024/10/california-enacts-ai-transparency-law-requiring-disclosures-for-ai-content) — Independent law firm analysis of SB 942 requirements and scope.
6. [California AI Transparency Act Amendments Signed Into Law (Troutman Pepper)](https://www.troutmanprivacy.com/2025/10/california-ai-transparency-act-amendments-signed-into-law/) — Analysis of AB 853 amendments, operative date delay, and new platform obligations.
7. [California delays its AI Transparency Act and passes new content laws (Infobytes by Orrick)](https://infobytes.orrick.com/2025-10-17/california-delays-its-ai-transparency-act-and-passes-new-content-laws/) — Orrick analysis of AB 853 and the broader California AI legislative landscape.
8. [Navigating the California AI Transparency Act: New Contract Requirements (Orrick)](https://www.orrick.com/en/Insights/2025/01/Navigating-the-California-AI-Transparency-Act-New-Contract-Requirements) — Detailed analysis of third-party licensee contract obligations and 96-hour revocation requirement.
9. [California SB 942 & AB 2013: AI transparency compliance guide (TrustArc)](https://trustarc.com/resource/california-ai-transparency-laws-sb942-ab2013/) — Compliance-focused overview comparing SB 942 and AB 2013 requirements.
10. [California AI Transparency Act: SB-942 Compliance Guide (Fairnow)](https://fairnow.ai/guide/california-ai-transparency-act/) — Practical compliance guidance including C2PA watermarking implementation recommendations.
11. [Ensuring a National Policy Framework for Artificial Intelligence (White House)](https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/) — Official text of the December 11, 2025 executive order directing DOJ AI Litigation Task Force and establishing federal preemption framework.
12. [President Trump's Latest Executive Order on AI Seeks to Preempt State Laws (Gibson Dunn)](https://www.gibsondunn.com/president-trump-latest-executive-order-on-ai-seeks-to-preempt-state-laws/) — Legal analysis of the executive order's scope and limitations with respect to state AI law preemption.
13. [Trump's AI Preemption Executive Order Unlikely to Put a Lid on State AI Laws (Goodwin)](https://www.goodwinlaw.com/en/insights/publications/2025/12/alerts-otherindustries-trumps-ai-preemption-executive-order) — Assessment of the executive order's legal constraints and enforceability against existing state laws.
14. [New State AI Laws are Effective on January 1, 2026, But a New Executive Order Signals Disruption (King & Spalding)](https://www.kslaw.com/news-and-insights/new-state-ai-laws-are-effective-on-january-1-2026-but-a-new-executive-order-signals-disruption) — Broader analysis of the state AI law landscape entering 2026 and federal preemption dynamics.
15. [California's New AI Laws Focus on Training Data, Content Transparency (Cooley)](https://www.cooley.com/news/insight/2024/2024-10-16-californias-new-ai-laws-focus-on-training-data-content-transparency) — Analysis placing SB 942 and AB 2013 in the context of California's broader 2024 AI legislative package.
