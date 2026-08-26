---
title: "webXray Audit Finds Widespread CCPA Global Privacy Control Noncompliance by Google, Meta, and Microsoft"
date: 2026-04-22
jurisdiction: "California"
category: "privacy"
development_type: "enforcement"
finding_id: "SCAN-20260422-014"
topic_key: "CA-CCPA-GPC-WEBXRAY-AUDIT-2026"
topic_type: "enforcement_action"
first_reported: 2026-04-21
last_updated: 2026-04-22
status_history: []
cluster: "CPPA CCPA Global Privacy Control (GPC) Opt-Out Enforcement"
cluster_slug: "cppa-ccpa-gpc-opt-out-enforcement"
---

# webXray Audit Finds Widespread CCPA Global Privacy Control Noncompliance by Google, Meta, and Microsoft

**Jurisdiction:** California | **Category:** Privacy | **Date:** 2026-04-22

## Summary [HIGH confidence]

A March 2026 audit by privacy technology firm webXray found that 55 percent of California's most popular websites continued setting advertising cookies even after consumers sent a Global Privacy Control (GPC) opt-out signal, with [Google failing to honor GPC in 86 percent of observed cases, Meta in 69 percent, and Microsoft in 50 percent](https://globalprivacyaudit.org/2026/california). The audit — published on [globalprivacyaudit.org](https://globalprivacyaudit.org/2026/california) and covering 7,634 websites scanned from a California residential IP address — estimates $5.8 billion in aggregate potential liability if regulators apply the average fine from recent CCPA enforcement actions across the 4,170 noncompliant sites identified. The findings materially increase enforcement risk for any organization relying on third-party ad-tech vendors to honor GPC, coming as the California Privacy Protection Agency (CPPA) actively builds its Audits Division and has already secured five opt-out enforcement settlements in the past 14 months.

## Key Facts [HIGH confidence]

- The [webXray audit](https://globalprivacyaudit.org/2026/california) scanned 7,634 of California's most popular websites twice each — once with GPC enabled and once without — from a California residential IP address, using an unmodified Chrome browser downloaded from Google's own servers.
- [55 percent of sites tested](https://www.darkreading.com/cyber-risk/audit-big-tech-ignores-data-collection-requests) set advertising cookies despite the GPC opt-out signal being present; 194 distinct online advertising services were found ignoring GPC signals.
- **Google** failed to honor GPC in [86 percent of observed interactions](https://globalprivacyaudit.org/2026/california): upon receiving the GPC signal, Google's ad servers respond by setting a two-year `IDE` advertising cookie. Cookie Consent banners certified by Google showed opt-out failure rates of 77 to 91 percent across three major Google-certified consent management platform (CMP) vendors tested.
- **Meta** exhibited GPC noncompliance in [69 percent of cases](https://globalprivacyaudit.org/2026/california): the Meta tracking pixel contains no code to check for GPC at all and fires unconditionally regardless of opt-out settings.
- **Microsoft** failed in [50 percent of cases](https://globalprivacyaudit.org/2026/california): its ad network unconditionally returns a one-year `MUID` tracking cookie when a GPC signal is received. Microsoft stated publicly that it honors GPC for personalized advertising but that certain cookies are necessary for operational purposes.
- The audit was led by Timothy Libert, who previously led cookie policy and compliance at Google's Sunnyvale offices from 2021 to 2023, per [KQED reporting](https://www.kqed.org/news/12079887/what-is-the-point-of-californias-privacy-laws-if-big-tech-ignores-them).
- The potential $5.8 billion aggregate liability estimate is derived by applying the [average CCPA opt-out enforcement fine of $1,387,617](https://globalprivacyaudit.org/2026/california) across the 4,170 noncompliant sites — calculated from six enforcement actions: Sephora ($1.2M, 2022), Healthline Media ($1.55M, 2025), Tractor Supply ($1.35M, 2025), PlayOn Sports ($1.1M, 2026), Ford Motor Co. ($375,703, 2026), and Walt Disney ($2.75M, 2026).

## Legal Basis [HIGH confidence]

Under [California Civil Code Section 1798.135](https://california-ccpa.org/section-1798-135-methods-of-limiting-sale-sharing-and-use-of-personal-information-and-use-of-sensitive-personal-information), as amended by the California Privacy Rights Act of 2020 (CPRA), a business that sells or shares consumers' personal information must honor opt-out preference signals transmitted by a platform, technology, or mechanism meeting technical specifications adopted by the CPPA under Section 1798.185. The Global Privacy Control is a W3C-recognized technical standard that California regulators have expressly endorsed as satisfying this requirement. Under [Section 1798.120](https://california-ccpa.org/section-1798-120-consumers-right-to-opt-out-of-sale-or-sharing-of-personal-information/), businesses that receive a GPC signal must treat it as a valid opt-out of sale and sharing of personal information — there is no opt-out-of-opt-out provision for advertising cookies that the business characterizes as "operational."

Revised [CCPA regulations effective January 1, 2026](https://cppa.ca.gov/regulations/pdf/ccpa_statute_eff_20260101.pdf) added a requirement that businesses provide consumers confirmation that their GPC-triggered opt-out has been processed. CPPA enforcement guidance issued in September 2025 announced a [joint investigative sweep with Colorado and Connecticut attorneys general](https://cppa.ca.gov/announcements/2025/20250923.html) specifically targeting GPC noncompliance — signaling that regulators view the issue as industry-wide rather than firm-specific.

## Enforcement Context [HIGH confidence]

The CPPA and California Attorney General have built a consistent GPC enforcement record across six settlements, escalating in penalty size:

| Settlement | Year | Amount | GPC Issue |
|---|---|---|---|
| Sephora | 2022 | $1.2M | Ignoring GPC signals entirely; failure to disclose data sales |
| Healthline Media | 2025 | $1.55M | Opt-out failures including GPC |
| Tractor Supply | 2025 | $1.35M | Opt-out noncompliance |
| PlayOn Sports | 2026 | $1.1M | Failed to configure digital properties to recognize GPC signals ([CPPA enforcement action](https://privacymatters.dlapiper.com/2026/03/californias-playon-enforcement-a-new-chapter-in-childrens-data-privacy/)) |
| Ford Motor Co. | 2026 | $375,703 | Improperly processing opt-out requests; adding unnecessary friction to GPC |
| Walt Disney Co. | 2026 | $2.75M | Limiting GPC opt-out to a single device rather than honoring across all linked streaming services ([CA AG press release](https://oag.ca.gov/news/press-releases/california-wont-let-it-go-attorney-general-bonta-announces-275-million)) |

The [Disney settlement](https://oag.ca.gov/news/press-releases/california-wont-let-it-go-attorney-general-bonta-announces-275-million) — the largest CCPA settlement in history — is particularly instructive: Disney did have a GPC mechanism, but it scoped the opt-out to only the device and browser where the GPC signal was detected. The AG found that a logged-in consumer's opt-out must propagate across all streaming services associated with that account. This "partial compliance is noncompliance" principle applies directly to organizations whose ad-tech vendors honor GPC on some touchpoints but not others.

The CPPA is [building out a dedicated Audits Division](https://www.hunton.com/privacy-and-cybersecurity-law-blog/calprivacy-director-expects-ccpa-compliance-audits-in-2026) in 2026 authorized to conduct both announced and unannounced proactive compliance audits. CPPA Deputy Director of Enforcement Michael Macko has stated the agency's strategy is to [establish precedents across different CCPA elements and industries](https://www.hudsoncook.com/article/california-privacy-protection-agency-heralds-a-new-era-of-privacy-enforcement/) rather than concentrate on any single sector — signaling that enforcement will not be limited to the media and retail sectors that have dominated past actions.

## Industry Implications [MEDIUM confidence]

The webXray findings expose a structural gap in how most organizations implement GPC compliance: they rely on their CMP or ad-tech vendors to handle the GPC signal, but those vendors — including Google-certified CMPs — are themselves found to be noncompliant in the majority of tested cases. Key implications:

- **CMP Vendor Reliance Is Not a Defense.** CPPA enforcement consistently holds the business (not its vendor) liable for opt-out failures. Vendor contractual representations are not a shield if the actual technical implementation does not honor GPC.
- **Logged-In State Propagation.** Per the Disney settlement, a GPC opt-out by an authenticated user must propagate to all services associated with the consumer's account — not just the current browser session.
- **Operational Cookie Exception Is Narrow.** Microsoft's position — that certain cookies remain necessary for operational purposes — has not been tested in California enforcement. The CPPA's general posture, as reflected in enforcement actions and advisories, is that the opt-out exemption for strictly operational processing is narrow and cannot be used to maintain advertising tracking infrastructure.
- **Advertising Networks as Vector.** 194 third-party advertising services were found ignoring GPC. Any site that loads these networks (e.g., Google Ads, Meta Pixel, Microsoft Clarity) is exposed even if its own first-party code honors GPC correctly.

[CalMatters reporting](https://calmatters.org/economy/technology/2026/04/data-privacy-opt-outs/) characterized the scale as violations occurring at "industrial scale," and [multiple law firm analyses](https://www.potomaclaw.com/news-California-Ramps-Up-Enforcement-of-Consumer-Privacy-Opt-Out-Rights-in-2026) confirm that opt-out compliance is the CPPA's most active enforcement area heading into the second half of 2026.

## Action Items

1. **Audit your GPC implementation end-to-end now.** Do not rely on your CMP vendor's self-certification. Replicate the webXray methodology: scan your domains with GPC enabled and verify in network traffic that no advertising cookies are set by first-party or third-party scripts.

2. **Test all ad-tech vendors individually.** Identify every third-party script loading on your properties. If Google Ads, Meta Pixel, or Microsoft Advertising are present, test specifically whether those networks honor GPC — the audit found they do not in a majority of cases.

3. **Address logged-in user propagation.** If you operate multiple products, apps, or streaming services under a single account, a GPC opt-out from any device or browser must cascade to all associated services. This is the Disney lesson.

4. **Review your "operational cookies" carve-out.** If your compliance program exempts certain cookies from GPC on the grounds they are operationally necessary, obtain written legal analysis confirming those cookies do not constitute "sale or sharing" under CCPA. The CPPA does not recognize a general advertising-network-as-operational-infrastructure argument.

5. **Update vendor contracts.** Add explicit GPC-compliance warranties and audit rights to all CMP, CDN, and ad-tech vendor agreements. Negotiate indemnification for CCPA fines resulting from vendor-side GPC failures.

6. **Monitor CPPA audit notices.** The CPPA's new Audits Division can conduct unannounced audits. Organizations with significant California traffic should treat proactive GPC audit readiness — documented testing records, vendor compliance certifications, and opt-out signal logs — as a compliance control that must be maintained continuously.

7. **Multi-state exposure check.** Colorado and Connecticut regulators joined California in a joint GPC sweep in September 2025. Colorado's CPA and Connecticut's CTDPA also require honoring opt-out preference signals. A single unified GPC compliance program covering all three states is more efficient than jurisdiction-by-jurisdiction fixes.

## Related Reports

- [reports/privacy/cppa-playon-sports-ccpa-enforcement-2026-04-07.md](../../cppa-playon-sports-ccpa-enforcement-2026-04-07.md) -- Covers the $1.1M PlayOn Sports CPPA enforcement action for GPC noncompliance, one of six baseline enforcement actions cited in the webXray audit.
- [reports/privacy/enforcement-actions/california-cppa-enforcement-advisory-data-minimization-2024-04-02.md](california-cppa-enforcement-advisory-data-minimization-2024-04-02.md) -- CPPA's first enforcement advisory signals the agency's proactive enforcement posture that underlies the risk identified in the webXray audit.
- [reports/privacy/state-comprehensive-laws/cppa-ccpa-new-regulations-public-comment-2024-07.md](../state-comprehensive-laws/cppa-ccpa-new-regulations-public-comment-2024-07.md) -- Background on the CPPA's 2024 rulemaking that expanded GPC recognition obligations effective January 1, 2026.
- [reports/privacy/cppa-drop-audit-rulemaking-2026-04-12.md](../cppa-drop-audit-rulemaking-2026-04-12.md) -- The CPPA's new Audits Division infrastructure — the same division expected to conduct proactive GPC compliance audits following the webXray report.

## Sources

1. [webXray California Privacy Audit 2026](https://globalprivacyaudit.org/2026/california) -- Primary source: the full webXray audit report with methodology, per-company noncompliance rates, and aggregate liability estimate
2. [Dark Reading: Audit: Big Tech Often Ignores CA Law Opt-Out Requests](https://www.darkreading.com/cyber-risk/audit-big-tech-ignores-data-collection-requests) -- News coverage of the webXray audit with summary of findings
3. [The Record: Big tech fails to opt-out users requesting not to be tracked](https://therecord.media/big-tech-fails-to-opt-out-users-requesting-not-to-be-tracked) -- Recorded Future News coverage with company-specific details
4. [KQED: What Is the Point of California's Privacy Laws if Big Tech Ignores Them?](https://www.kqed.org/news/12079887/what-is-the-point-of-californias-privacy-laws-if-big-tech-ignores-them) -- KQED investigative coverage including background on webXray founder Timothy Libert
5. [CalMatters: Websites break California privacy law at 'industrial scale,' survey finds](https://calmatters.org/economy/technology/2026/04/data-privacy-opt-outs/) -- CalMatters reporting contextualizing scale of noncompliance; published April 21, 2026
6. [California Civil Code Section 1798.135 -- CCPA/CPRA GPC opt-out requirement](https://california-ccpa.org/section-1798-135-methods-of-limiting-sale-sharing-and-use-of-personal-information-and-use-of-sensitive-personal-information) -- Official statutory text providing the legal basis for GPC compliance obligations
7. [California Civil Code Section 1798.120 -- Consumers' Right to Opt Out](https://california-ccpa.org/section-1798-120-consumers-right-to-opt-out-of-sale-or-sharing-of-personal-information/) -- Statutory right underpinning GPC enforcement
8. [CPPA CCPA Statute (effective January 1, 2026)](https://cppa.ca.gov/regulations/pdf/ccpa_statute_eff_20260101.pdf) -- Current CCPA/CPRA statutory text with 2026 amendments including GPC confirmation requirements
9. [California AG Press Release: Disney $2.75M Settlement](https://oag.ca.gov/news/press-releases/california-wont-let-it-go-attorney-general-bonta-announces-275-million) -- Official announcement of largest CCPA settlement, establishing the "logged-in state propagation" requirement
10. [Holland & Knight: Caught in a Mousetrap: Disney to Pay $2.75M](https://www.hklaw.com/en/insights/publications/2026/02/caught-in-a-mousetrap-disney-to-pay-for-consumer-opt-out-missteps) -- Law firm analysis of Disney settlement compliance lessons
11. [DLA Piper Privacy Matters: PlayOn Enforcement -- New Chapter in Children's Data Privacy](https://privacymatters.dlapiper.com/2026/03/californias-playon-enforcement-a-new-chapter-in-childrens-data-privacy/) -- Law firm analysis of CPPA's $1.1M PlayOn Sports GPC enforcement action
12. [Hunton Andrews Kurth: CalPrivacy Director Expects CCPA Compliance Audits in 2026](https://www.hunton.com/privacy-and-cybersecurity-law-blog/calprivacy-director-expects-ccpa-compliance-audits-in-2026) -- Analysis of CPPA Audits Division plans and enforcement priorities
13. [Hudson Cook: California Privacy Protection Agency Heralds a "New Era of Privacy Enforcement"](https://www.hudsoncook.com/article/california-privacy-protection-agency-heralds-a-new-era-of-privacy-enforcement/) -- Deputy Director Macko's enforcement strategy statement
14. [Potomac Law: California Ramps Up Enforcement of Consumer Privacy Opt-Out Rights in 2026](https://www.potomaclaw.com/news-California-Ramps-Up-Enforcement-of-Consumer-Privacy-Opt-Out-Rights-in-2026) -- Law firm analysis of CPPA 2026 enforcement patterns and GPC focus
15. [CPPA September 2025 Announcement: Joint GPC Sweep](https://cppa.ca.gov/announcements/2025/20250923.html) -- Official CPPA announcement of multistate GPC enforcement sweep with Colorado and Connecticut
16. [Uniconsent: US CCPA: Disney to Pay $2.75M for Failed Consumer Opt-Out via Global Privacy Control](https://www.uniconsent.com/blog/disney-ccpa-fine-global-privacy-control) -- Technical analysis of Disney's GPC failure mode
