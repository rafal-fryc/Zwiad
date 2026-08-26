---
title: "Beware of the Spy Pixel: Arizona TUCSR Act Class Action Wave Targeting Email Tracking"
date: 2024-05-30
jurisdiction: "Arizona"
category: "privacy"
development_type: "litigation"
finding_id: "SCAN-20240530-018"
topic_key: "arizona-dbd2f837-2024"
topic_type: "enforcement_action"
first_reported: 2024-05-30
last_updated: 2026-04-15
status_history: []
cluster: "Arizona TUCSR Act: Email Tracking Pixel Class Action Wave"
cluster_slug: "arizona-tucsr-spy-pixel-litigation"
---

# Beware of the Spy Pixel: Arizona TUCSR Act Class Action Wave Targeting Email Tracking

**Jurisdiction:** Arizona | **Category:** Privacy | **Date:** 2024-05-30

## Executive Summary [HIGH confidence]

Beginning in late 2023 and accelerating through early 2024, plaintiffs' attorneys filed a wave of class action lawsuits in Arizona courts alleging that retailers' use of email tracking pixels — so-called "spy pixels" — violated Arizona's [Telephone, Utility and Communication Service Records Act (TUCSR Act)](https://www.azleg.gov/ars/44/01376.htm), A.R.S. § 44-1376 et seq. Named defendants include major retailers such as Target, Gap, Home Depot, Lowe's, Patagonia, PacSun, H&M, and Sephora, along with marketing technology vendors. Plaintiffs alleged that the metadata collected by tracking pixels — including when and where an email was opened, device type, read duration, and forwarding activity — constitutes a "communication service record" that the statute bars from being obtained without customer authorization, and sought $1,000 per violation in statutory damages. Within less than one year, at least five trial courts dismissed these claims, finding that ordinary marketing email senders are not "communication service providers" regulated by the statute. In November 2025, the Arizona Court of Appeals definitively affirmed that the TUCSR Act does not apply to tracking pixels in marketing emails, effectively ending the litigation wave. Companies that received demand letters or are party to pending litigation should monitor the fallout; the remaining live risk is legislative amendment rather than continued judicial exposure.

## Background [HIGH confidence]

### The Arizona TUCSR Act

Arizona enacted its Telephone, Utility and Communication Service Records Act as part of a 2007 legislative response to the federal Telephone Records and Privacy Protection Act of 2006, which criminalized the practice of "pretexting" — fraudulently obtaining telephone records to track or surveil individuals. The Arizona legislature subsequently expanded the prohibition from telephone records alone to encompass "communication service records" and "public utility records," reflecting the shift of consumer communications to internet-based services.

The operative statutory provisions are codified at [A.R.S. § 44-1376 (Definitions)](https://www.azleg.gov/ars/44/01376.htm), [§ 44-1376.01 (Unauthorized or Fraudulent Procurement)](https://www.azleg.gov/ars/44/01376-01.htm), [§ 44-1376.02 (Application)](https://www.azleg.gov/ars/44/01376-02.htm), and [§ 44-1376.04 (Civil Causes of Action)](https://www.azleg.gov/ars/44/01376-04.htm). The statute defines "communication service record" to include subscriber information — such as name, billing address, length of service, payment method, telephone number, electronic account identification, associated screen names, toll bills or access logs, and records of the path of an electronic communication between the point of origin and the point of delivery. The statute expressly excludes the content of any stored oral, wire, or electronic communication.

Section 44-1376.01 prohibits any person from knowingly obtaining a "communication service record" of any Arizona resident (i) without the authorization of the person to whom the record pertains, or (ii) by fraudulent, deceptive, or false means. It also requires entities that maintain such records to establish reasonable procedures protecting against unauthorized or fraudulent disclosure.

The civil remedies provision at [A.R.S. § 44-1376.04](https://law.justia.com/codes/arizona/title-44/section-44-1376-04/) provides that an aggrieved person may recover the sum of actual damages plus any profits made by the violator, with a minimum recovery of $1,000 per violation. The statute also authorizes equitable relief and attorneys' fees.

### The Broader Context: Privacy Class Action Proliferation

The Arizona spy pixel litigation wave emerged against a backdrop of proliferating privacy class actions targeting digital tracking technologies. California's Invasion of Privacy Act (CIPA) had generated substantial class action volume over website chat features and session replay tools. In the healthcare sector, plaintiffs successfully leveraged state wiretap and privacy statutes to challenge hospitals' use of Meta Pixel on patient-facing websites. The Arizona TUCSR Act presented an analogous opportunity: a state statute with a private right of action, per-violation statutory damages, and no prior civil enforcement history, applied to the ubiquitous practice of email marketing analytics.

Before 2024, there was no judicial precedent interpreting the TUCSR Act in a civil context. This gap created both the opportunity plaintiffs sought to exploit and the doctrinal uncertainty that ultimately made mass filings attractive before any adverse ruling foreclosed the theory.

## Detailed Analysis [HIGH confidence]

### The Plaintiffs' Legal Theory

Plaintiffs' complaints alleged that companies deploying email marketing analytics platforms embedded hidden tracking pixels — typically single-pixel transparent images referenced via a unique URL — in marketing emails sent to Arizona residents. When a recipient opened the email, the pixel loaded automatically, transmitting a range of behavioral metadata to the sender's marketing technology vendor. The metadata collected typically included:

- Date, time, and geographic location where the email was opened
- Device type and email client used
- Number of times the email was opened
- Whether the email was forwarded or printed
- Average read duration

Plaintiffs argued that these metadata fall within the statutory definition of "communication service record," specifically citing the phrase "access logs" in the definition and the reference to "records of the path of an electronic communication between the point of origin and the point of delivery." Under this theory, every time an Arizona recipient opened a marketing email, the retailer and its vendor "obtained" a communication service record without the recipient's consent, triggering $1,000 in statutory damages per instance.

Class definitions typically sought to cover "all persons in the State of Arizona who have opened a marketing email containing a tracking pixel from Defendants" within the applicable statute of limitations — a class that could encompass potentially hundreds of thousands of individuals and aggregate liability in the hundreds of millions of dollars.

### Named Defendants and Key Cases

The litigation wave targeted a broad cross-section of national retailers and their email marketing technology vendors. Key cases filed through mid-2024 include:

**Carbajal v. Home Depot U.S.A., Inc.** — Filed in the District of Arizona (Case No. CV-24-00730-PHX-DGC), this case accused [Home Depot](https://natlawreview.com/article/email-spy-home-depot-sued-putative-class-action-alleged-use-spy-tracking-pixels) and its email analytics vendor Validity, Inc. of embedding spy pixels that tracked when, where, and how recipients engaged with marketing emails. The district court dismissed the complaint, holding that the TUCSR Act applies to "communication service providers" — businesses such as internet service providers that deliver actual communication services to subscribers — rather than retailers who communicate with customers by email for marketing purposes. The court further held that tracking pixel metadata does not constitute a "communication service record" as defined in the statute.

**Carbajal v. Gap, Inc.** — Filed in the District of Arizona (Case No. 2:24-cv-01056), this suit accused [The Gap](https://communicationslitigationtoday.com/article/2024/05/10/class-action-seeks-to-halt-the-gaps-use-of-tracking-pixels-to-spy-on-email-recipients-2405090013) and its email analytics vendor PaeDae (d/b/a Gimbal, operating as Infillion) of the same conduct. Unlike the Home Depot case, plaintiff Ivonne Carbajal and The Gap filed a notice of settlement on November 29, 2024, making it one of the few cases in this wave to resolve without a merits dismissal.

**Smith v. Target Corporation** — Filed in Arizona state superior court, this case became the vehicle for the definitive appellate ruling. The Superior Court dismissed the complaint with prejudice, finding persuasive the federal court analysis in *Carbajal v. Home Depot*. Plaintiff Kiloh Smith appealed to the [Arizona Court of Appeals, Division One](https://coa1.azcourts.gov/Portals/0/OpinionFiles/Div1/2025/CV25-0120%20Smith%20v.%20Target%20OP%20Final%20(11112025).pdf).

Additional defendants in the wave included Lowe's and its vendor Salesforce, Patagonia, PacSun, H&M, and Sephora. [Lowe's plaintiffs](https://communicationslitigationtoday.com/article/2024/05/08/lowes-salesforce-spy-on-consumers-when-they-open-marketing-emails-class-action-2405070067) sought actual damages or $1,000 per violation, injunctive relief, and attorneys' fees.

### Court Decisions: Consistent Rejection

Arizona trial courts and federal courts sitting in the District of Arizona were remarkably consistent in dismissing these claims in 2024. [Proskauer Rose](https://privacylaw.proskauer.com/2024/09/articles/privacy-law/privacy-class-action-spotlight-surge-of-privacy-class-actions-in-arizona-targeting-email-pixel-tracking/) reported that at least five courts ruled that the TUCSR Act does not apply to marketing emails with tracking pixels, advancing two independent grounds:

1. **Scope of regulated entities**: The TUCSR Act was designed to regulate "communication service providers" — entities like internet service providers and telephone companies that actually provide communication services to subscribers. Retailers that send marketing emails are not communication service providers within the statute's intended scope. As the *Home Depot* court put it, the statute covers "businesses such as internet service providers that deliver actual communication services to subscribers, rather than retailers engaged in selling goods and services who communicate with customers by email."

2. **Definition of "communication service record"**: The metadata collected by tracking pixels — email open timestamps, device type, geographic location, read duration — does not constitute a "communication service record" as defined by the statute. The term "access logs" in the definition refers to records of when a subscriber accesses communication services provided to them by their service provider, not marketing analytics collected by a retailer about how its recipients engage with email campaigns. Plaintiffs' reading would stretch the statutory definition beyond any plausible legislative intent.

### The Arizona Court of Appeals Ruling (November 2025)

The Arizona Court of Appeals, Division One, issued its opinion in [*Smith v. Target Corporation*, No. 1-CA-CV-25-0210](https://law.justia.com/cases/arizona/court-of-appeals-division-one-published/2025/1-ca-cv-25-0210.html) on November 13, 2025, definitively resolving the statutory interpretation question. The court affirmed dismissal with prejudice, holding that the TUCSR Act "simply does not apply to tracking pixels in marketing emails."

The court's analysis focused on the statute's historical origins. The TUCSR Act emerged from two prior state laws enacted in 2000 and 2006, and all three laws were clearly intended to regulate "public utility records, telephone records, [and] communication service records" controlled by service providers that "send or receive oral, wire or electronic communications or computer services." The court confirmed that an email sender is not the kind of person or entity that the TUCSR Act seeks to regulate. The court further held that "access logs" within the "communication service record" definition refers only to records of when a subscriber accesses communication services — "not marketing metrics collected by retailers about email engagement."

Following the appellate decision, [federal district courts began dismissing pending similar claims](https://natlawreview.com/article/arizona-court-appeals-affirms-dismissal-arizona-spy-pixel-class-action), effectively mopping up the remaining docket.

### Defendants' Principal Arguments

Based on the judicial outcomes, the most successful defenses for businesses named in the TUCSR Act pixel cases were:

- **Not a "communication service provider"**: Retailers using email for marketing are not regulated entities under the statute. The statute was enacted to protect telephone customers from having their call records obtained through pretexting, not to impose consent obligations on retailers who send promotional emails.
- **Pixels do not create "communication service records"**: Email engagement analytics are not subscriber records maintained by a communication services provider. They are marketing performance metrics generated and held by the email sender, not records of a subscriber's use of a communication service.
- **Legislative intent**: The statutory history demonstrates no legislative intent to reach commercial email analytics. If the legislature wanted to extend privacy obligations to email marketing, it would need to amend the statute explicitly.

### Damages Exposure and Litigation Economics

The litigation wave presented significant asymmetric risk: plaintiffs seeking $1,000 per "violation" (per email open) against email lists potentially reaching millions of Arizona residents could theoretically generate nine-figure aggregate exposure, even with weak legal theories. This dynamic incentivized some defendants to settle rather than litigate (e.g., The Gap), while those that fought the merits prevailed. The [Perkins Coie](https://perkinscoie.com/insights/update/class-action-lawsuit-over-marketing-email-tracking-pixels-dismissed-federal-court) analysis of the federal court dismissal emphasized that defendants who promptly challenged the legal theory on a motion to dismiss successfully avoided class certification proceedings entirely.

## Impact Assessment [MEDIUM confidence]

### Current Risk Landscape

With the Arizona Court of Appeals having ruled definitively that the TUCSR Act does not apply to marketing email tracking pixels, the immediate litigation risk from this theory is substantially diminished. Federal courts sitting in Arizona have already begun applying the appellate court's reasoning to dismiss pending cases. Defendants in active cases should seek dismissal based on *Smith v. Target* as controlling authority on Arizona law.

The one significant exception is the [Gap settlement](https://www.pacermonitor.com/public/case/53459210/Carbajal_v_Gap_Incorporated_et_al), which resolved before a merits ruling. Defendants who have not yet received a favorable dismissal should evaluate their exposure in light of the appellate ruling.

### Legislative Amendment Risk

The more significant residual risk is legislative. The *Smith v. Target* court expressly noted that the Arizona legislature could expand the TUCSR Act to cover information gathered by marketing emails and pixel technology, but it has not done so. The litigation wave has drawn significant public and legislative attention to email tracking practices. Arizona legislators could introduce amendments that would explicitly extend the statute's scope to commercial email senders and marketing analytics, creating a statutory basis for future litigation that courts could not dismiss on the current grounds.

Companies should monitor the Arizona legislature for any proposed amendments to A.R.S. § 44-1376 that would broaden the definition of "communication service record" or expand the category of regulated entities.

### Industry-Wide Implications

The Arizona spy pixel cases are part of a broader pattern of plaintiffs' counsel identifying state privacy statutes with private rights of action and per-violation statutory damages, then testing novel theories in the civil context before courts have interpreted the statute. Similar waves have emerged under California's CIPA (for website chat and session replay tools) and under state wiretap statutes. Even when courts ultimately reject the theory — as happened here — the litigation wave imposes substantial defense costs and creates reputational exposure.

The [WilmerHale 2024 year-in-review](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20250225-year-in-review-2024-web-tracking-litigation-and-enforcement) on web tracking litigation documented the Arizona pixel wave alongside other tracking-related class action activity, placing it within a national trend that shows no sign of abating despite individual state-level setbacks.

### Affected Businesses

Any business that:
- Operates email marketing programs targeting Arizona residents
- Uses third-party email analytics vendors (e.g., Salesforce Marketing Cloud, Validity, Gimbal/Infillion, Klaviyo, Mailchimp)
- Embeds tracking pixels or uses pixel-based open-rate or engagement analytics

was potentially within scope of the plaintiff's theory, even though courts have now rejected that theory. Businesses in this position may still face:
- Pending demand letters from plaintiffs' counsel that predate the appellate ruling
- Remaining unappealed state court cases
- Future legislative amendments if Arizona lawmakers respond to the litigation wave

## Action Items

- Monitor active TUCSR Act pixel litigation dockets for final dispositions following *Smith v. Target*; file dispositive motions citing the Arizona Court of Appeals ruling if any cases remain pending
- Track Arizona legislative session for any bills proposing to amend A.R.S. § 44-1376 to expressly cover email marketing analytics or expand the definition of "communication service record"
- Audit email marketing practices to document consent and disclosure practices, even though current law does not require them, as a hedge against potential legislative amendment
- Consult with outside counsel before modifying email analytics or consent disclosures in response to demand letters — changes made reactively may affect litigation posture in pending matters
- Review email marketing vendor agreements (e.g., data processing addenda) to understand the vendor's role and indemnification obligations in tracking-related litigation
- Consider whether existing email marketing disclosures adequately describe tracking practices for purposes of other applicable state laws (e.g., California's CCPA/CPRA, which imposes separate notice and opt-out obligations for data collected through email interactions)

## Related Reports

- [reports/privacy/litigation/massachusetts-doe-v-tenet-healthcare-pixel-tracking-2024-05-20.md](reports/privacy/litigation/massachusetts-doe-v-tenet-healthcare-pixel-tracking-2024-05-20.md) — Covers parallel pixel tracking litigation in the healthcare context under Massachusetts state law, illustrating the broader national wave of class actions targeting tracking technologies
- [reports/privacy/litigation/california-cipa-chat-wiretapping-garcia-v-buildcom-2024-04-17.md](reports/privacy/litigation/california-cipa-chat-wiretapping-garcia-v-buildcom-2024-04-17.md) — Documents California CIPA wiretapping class actions targeting web analytics, the template for the Arizona TUCSR litigation strategy
- [reports/privacy/litigation/california-cipa-chat-wiretapping-cody-v-boscov-2024-05-23.md](reports/privacy/litigation/california-cipa-chat-wiretapping-cody-v-boscov-2024-05-23.md) — Additional CIPA class action against a retailer, showing how retail companies face parallel tracking liability theories in multiple states simultaneously

## Sources

1. [A.R.S. § 44-1376 — Definitions (Arizona Legislature)](https://www.azleg.gov/ars/44/01376.htm) — Official text of the TUCSR Act definitions section, including the definition of "communication service record"
2. [A.R.S. § 44-1376.01 — Unauthorized or Fraudulent Procurement (Arizona Legislature)](https://www.azleg.gov/ars/44/01376-01.htm) — Official text of the core prohibition and protection requirements
3. [A.R.S. § 44-1376.04 — Civil Causes of Action (Justia)](https://law.justia.com/codes/arizona/title-44/section-44-1376-04/) — Civil remedies provision: $1,000 minimum per-violation damages plus actual damages and attorneys' fees
4. [Smith v. Target Corporation, No. 1-CA-CV-25-0210 (Ariz. Ct. App. Nov. 13, 2025) (Justia)](https://law.justia.com/cases/arizona/court-of-appeals-division-one-published/2025/1-ca-cv-25-0210.html) — Definitive Arizona appellate ruling holding TUCSR Act does not apply to marketing email tracking pixels
5. [Smith v. Target Corporation — Court of Appeals Opinion PDF](https://coa1.azcourts.gov/Portals/0/OpinionFiles/Div1/2025/CV25-0120%20Smith%20v.%20Target%20OP%20Final%20(11112025).pdf) — Official appellate court opinion from the Arizona Court of Appeals website
6. [Arizona Court of Appeals Affirms Dismissal of Arizona "Spy Pixel" Class Action (Womble Bond Dickinson)](https://www.womblebonddickinson.com/us/insights/alerts/arizona-court-appeals-affirms-dismissal-arizona-spy-pixel-class-action) — Law firm analysis of the *Smith v. Target* appellate ruling and its implications
7. [Arizona Court of Appeals Affirms Dismissal of Arizona "Spy Pixel" Class Action (National Law Review)](https://natlawreview.com/article/arizona-court-appeals-affirms-dismissal-arizona-spy-pixel-class-action) — Secondary coverage of the appellate ruling with analysis
8. [Beware of the Spy Pixel: Arizona Faces New Class Action Trend Under Privacy Law (Benesch Friedlander / JDSupra)](https://www.jdsupra.com/legalnews/beware-of-the-spy-pixel-arizona-faces-9332676/) — Original May 2024 Benesch law firm analysis identifying the emerging litigation wave; the primary source for this finding
9. [Beware of the Spy Pixel (Benesch Law firm website)](https://www.beneschlaw.com/insight/beware-of-the-spy-pixel-arizona-faces-new-class-action-trend-under-privacy-law/) — Benesch's original client-facing alert on the Arizona litigation trend
10. [Privacy Class Action Spotlight: Surge of Privacy Class Actions in Arizona Targeting Email Pixel Tracking (Proskauer Rose)](https://privacylaw.proskauer.com/2024/09/articles/privacy-law/privacy-class-action-spotlight-surge-of-privacy-class-actions-in-arizona-targeting-email-pixel-tracking/) — September 2024 Proskauer analysis documenting five favorable court rulings and identifying companies targeted
11. [Arizona Spy Pixel Class Action Litigation Update (Bryan Cave Leighton Paisner)](https://www.bclplaw.com/en-US/events-insights-news/spy-pixel-class-action-litigation.html) — BCLP litigation update on the Arizona spy pixel wave
12. [Email Spy: Home Depot Sued in Putative Class Action For Alleged Use of Spy Tracking Pixels (National Law Review)](https://natlawreview.com/article/email-spy-home-depot-sued-putative-class-action-alleged-use-spy-tracking-pixels) — Coverage of the Carbajal v. Home Depot case and TUCSR Act claims
13. [Lowe's, Salesforce Spy on Consumers When They Open Marketing Emails: Class Action (Communications Litigation Today)](https://communicationslitigationtoday.com/article/2024/05/08/lowes-salesforce-spy-on-consumers-when-they-open-marketing-emails-class-action-2405070067) — Coverage of the Lowe's/Salesforce class action filing
14. [Class Action Seeks to Halt The Gap's Use of Tracking Pixels (Communications Litigation Today)](https://communicationslitigationtoday.com/article/2024/05/10/class-action-seeks-to-halt-the-gaps-use-of-tracking-pixels-to-spy-on-email-recipients-2405090013) — Coverage of the Carbajal v. Gap filing
15. [Class Action Lawsuit Over Marketing Email Tracking Pixels Dismissed by Federal Court (Perkins Coie)](https://perkinscoie.com/insights/update/class-action-lawsuit-over-marketing-email-tracking-pixels-dismissed-federal-court) — Perkins Coie analysis of the federal court dismissal in *Carbajal v. Home Depot*
16. [Year in Review: 2024 Web Tracking Litigation and Enforcement (WilmerHale)](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20250225-year-in-review-2024-web-tracking-litigation-and-enforcement) — Comprehensive 2024 review placing Arizona pixel litigation within the broader national tracking litigation landscape
17. [A New Privacy Nuisance Suit Wave Gathers Strength In Arizona (Reed Smith)](https://www.reedsmith.com/en/perspectives/2025/02/a-new-privacy-nuisance-suit-wave-gathers-strength-in-arizona) — Reed Smith 2025 analysis of ongoing Arizona privacy litigation trends
18. [Carbajal v. Gap — PACER Monitor Docket](https://www.pacermonitor.com/public/case/53459210/Carbajal_v_Gap_Incorporated_et_al) — Docket for the Gap case showing November 2024 settlement notice
