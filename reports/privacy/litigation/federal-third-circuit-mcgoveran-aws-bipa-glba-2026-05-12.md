---
title: "Third Circuit Limits BIPA's Reach: AWS Wins on Extraterritoriality, Pindrop Wins on GLBA Financial Institution Exemption (McGoveran v. Amazon Web Services, No. 24-3215)"
date: 2026-05-12
jurisdiction: "Federal"
category: "privacy"
development_type: "court-decision"
finding_id: "SCAN-20260601-046"
topic_key: "federal-0727c239-2026"
topic_type: "enforcement"
first_reported: 2026-05-20
last_updated: 2026-06-01
status_history:
  - "2026-06-01: Corrected Background section to reflect original Illinois state court filing (Madison County Circuit Court, December 17, 2019) and AWS removal to S.D. Ill. federal court; corrected litigation origin year from 2020 to December 2019 (reviewer round 1 correction; confirmed via Madison-St. Clair Record and S.D. Ill. case No. 3:20-CV-31)"
cluster: "Illinois BIPA Litigation and Amendments"
cluster_slug: "illinois-bipa-litigation"
---

# Third Circuit Limits BIPA's Reach: AWS Wins on Extraterritoriality, Pindrop Wins on GLBA Financial Institution Exemption

**Case:** *McGoveran v. Amazon Web Services, Inc.*, No. 24-3215 (3d Cir. May 12, 2026)

**Jurisdiction:** Federal (Third Circuit) | **Category:** Privacy / Biometric Data | **Date:** May 12, 2026

## Executive Summary [HIGH confidence]

On May 12, 2026, the U.S. Court of Appeals for the Third Circuit affirmed dismissal of a biometric privacy class action brought by Illinois residents who called John Hancock Financial Services, a Massachusetts-based insurance and retirement services company. The case, *McGoveran v. Amazon Web Services, Inc.*, No. 24-3215, produced two significant and distinct holdings. First, the Third Circuit held that Pindrop Security, Inc. — a voice authentication and fraud detection vendor — independently qualifies as a "financial institution" under the Gramm-Leach-Bliley Act (GLBA) and therefore is wholly exempt from Illinois's Biometric Information Privacy Act (BIPA), 740 ILCS 14/1 et seq., by virtue of BIPA's incorporated financial-institution exemption. Second, as to Amazon Web Services (AWS), the court affirmed summary judgment on the surviving BIPA Section 15(b) claim on extraterritoriality grounds, joining a growing consensus that BIPA only applies when the alleged violations occurred "primarily and substantially" in Illinois — not merely because the plaintiff placed a call from within the state. The decision reinforces two powerful defense tools for cloud service providers, authentication vendors, and financial technology companies facing BIPA exposure: (1) the GLBA financial-institution exemption can attach to technology vendors based on their own service activities, independent of their financial-sector clients; and (2) the location of servers and data processing — not the plaintiff's physical location — governs BIPA's territorial scope.

## Background [HIGH confidence]

Illinois enacted the Biometric Information Privacy Act in 2008, establishing the first comprehensive state biometric data law in the United States. BIPA imposes strict notice, consent, and data retention requirements on private entities that collect, capture, purchase, receive, or otherwise obtain "biometric identifiers" — including retina or iris scans, fingerprints, voiceprints, and scans of hand or face geometry — from Illinois consumers. BIPA carries a private right of action with statutory damages ranging from \$1,000 per negligent violation to \$5,000 per intentional or reckless violation, making it a magnet for class action litigation.

BIPA contains an important exemption for financial institutions regulated by and in compliance with the privacy and data security provisions of Title V of GLBA. The GLBA financial institution exemption is codified at BIPA Section 25(c), which provides that the Act does not apply to a "financial institution or an affiliate of a financial institution that is subject to Title V, Subtitle A of the federal Gramm-Leach-Bliley Act." The Federal Reserve Board's Regulation Y, at [12 C.F.R. § 225.86(a)(2)(iii)](https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-225/subpart-I/section-225.86), enumerates financial activities that technology companies may conduct to qualify as financial institutions under GLBA, specifically including "authenticating the identity of persons conducting financial and nonfinancial transactions."

The case has a notably long history tracing back to December 2019. On December 17, 2019, Illinois residents Christine McGoveran, Joseph Valentine, and Amelia Rodriguez (plaintiffs) filed a putative class action complaint against AWS and Pindrop Security in the Circuit Court for the Third Judicial Circuit, Madison County, Illinois — the state court of general jurisdiction for Madison County. Plaintiffs alleged five counts of BIPA violations after calling John Hancock's customer service center. John Hancock is a Massachusetts-based financial services company. John Hancock routed its inbound customer service calls through Amazon Connect, a cloud-based contact center platform operated by AWS. Pindrop Security, a voice authentication and fraud-detection company, then analyzed callers' voices in real time using its biometric technology to verify caller identities and detect fraud — creating voiceprints of the callers without their explicit written informed consent, plaintiffs alleged.

AWS and Pindrop removed the case from Madison County Circuit Court to the U.S. District Court for the Southern District of Illinois (Case No. 3:20-CV-31), which dismissed for lack of personal jurisdiction over both defendants — finding neither AWS nor Pindrop specifically targeted Illinois residents. Plaintiffs refiled in the U.S. District Court for the District of Delaware, adding Pindrop and repleading. The Delaware district court dismissed all claims against Pindrop under BIPA's financial-institution exemption and dismissed most claims against AWS, sustaining only the Section 15(b) claim (collection without written consent) for further proceedings. Ultimately the district court granted summary judgment to AWS on the Section 15(b) claim on extraterritoriality grounds. Both rulings were appealed to the Third Circuit.

## Detailed Analysis [HIGH confidence]

### The GLBA Financial Institution Exemption: Pindrop's Independent Status

The more novel and commercially significant holding concerns Pindrop. The Third Circuit affirmed that Pindrop independently qualifies as a "financial institution" under GLBA by virtue of its own service activities — not derivatively through its financial-sector client John Hancock. The panel held that Pindrop's voice authentication and fraud-detection services for financial institutions fall squarely within "authenticating the identity of persons conducting financial and nonfinancial transactions," as enumerated in [12 C.F.R. § 225.86(a)(2)(iii)](https://www.ecfr.gov/current/title-12/chapter-II/subpart-I/section-225.86) of the Federal Reserve's Regulation Y, which lists permissible financial activities for bank holding companies and their affiliates.

This holding is doctrinally significant in two respects. First, it confirms that the GLBA financial institution exemption is not limited to the ultimate financial-institution client (here, John Hancock). A technology vendor that provides authentication services as its core business can itself qualify as a financial institution if those services constitute "activities closely related to banking" under the relevant federal regulation. Second, the exemption is self-contained: Pindrop's GLBA status is determined by what Pindrop does, not by who its customers are. Other courts — including district courts applying the exemption to Nuance Communications (a voice AI vendor) — had reached similar conclusions, but this Third Circuit affirmance adds appellate authority outside the Seventh Circuit to the principle.

The practical consequence is that voice authentication vendors, fraud detection platforms, and similar companies whose services are used by financial institutions may now more reliably invoke the GLBA exemption as an early dispositive defense to BIPA class actions, without needing to prove they derive their exemption from their clients' regulated status.

### The Extraterritoriality Doctrine: AWS's Location-of-Processing Defense

The second major holding addresses BIPA's geographic reach. Illinois courts and federal courts applying Illinois law have consistently held that BIPA does not apply extraterritorially — that is, BIPA only governs conduct that occurred "primarily and substantially" within Illinois. This doctrine derives from a presumption against extraterritorial application of Illinois statutes and has been adopted by courts in multiple circuits.

As to AWS, the key facts were dispositive: no AWS employee in Illinois had access to any biometric data; AWS did not store biometric identifiers in Illinois; and the AWS servers processing the voiceprints were physically located in Virginia. The Third Circuit held that plaintiffs could not establish the required nexus to Illinois simply because the callers were in Illinois when they placed calls. The court joined the growing body of case law — including earlier rulings in which Amazon and Microsoft both prevailed on extraterritoriality grounds in BIPA suits — standing for the proposition that BIPA cannot be triggered by an Illinois plaintiff's physical presence in Illinois alone when the underlying data collection, processing, and storage occur entirely outside the state.

This holding reinforces the geographic defense for cloud service providers: where servers are located matters more for BIPA compliance purposes than where customers are located. Cloud providers whose infrastructure is outside Illinois can argue that BIPA's substantive protections do not attach even if large portions of their user bases are Illinois residents.

### Five Issues Resolved

The Third Circuit resolved five issues on appeal, including: (1) dismissal of Pindrop under the GLBA financial institution exemption; (2) summary judgment for AWS on the extraterritoriality grounds; (3) whether the district court abused its discretion in denying plaintiffs' motions to extend discovery; (4) whether the district court abused its discretion in denying plaintiffs' motion for voluntary dismissal without prejudice; and (5) whether the plaintiffs' claims were otherwise cognizable under BIPA. The panel affirmed the district court in all respects.

### Litigation History and Procedural Posture

The case has a notably long history tracing back to December 2019 — underscoring the attrition value of procedural defense strategies in BIPA class actions. Plaintiffs originally filed in Illinois state court (Madison County Circuit Court) in December 2019; AWS and Pindrop removed to the Southern District of Illinois, which dismissed for lack of personal jurisdiction (affirmed on appeal). Plaintiffs then refiled in the District of Delaware, which disposed of the case entirely on the merits. The multi-year litigation history, across an Illinois state court, two federal district courts, and two rounds of appellate review, illustrates the friction that forum selection and jurisdiction challenges can impose on biometric privacy plaintiffs even before any substantive adjudication.

## Impact Assessment [MEDIUM confidence]

### Cloud Service Providers and Authentication Vendors

The ruling provides meaningful practical guidance for cloud-based call center platforms, customer authentication tools, and voice-enabled AI systems:

- **Infrastructure-based defense**: AWS's success on extraterritoriality confirms that the location of servers and data processing facilities is determinative of BIPA's application to cloud providers. AWS's servers in Virginia — not the callers' locations in Illinois — governed the territorial analysis. Cloud providers with infrastructure outside Illinois should audit the physical location of data processing for any voice or biometric applications serving Illinois customers.

- **Vendor-level GLBA status**: Pindrop's exemption demonstrates that technology vendors should evaluate whether their own services independently qualify them as GLBA-regulated financial institutions under 12 C.F.R. § 225.86, rather than assuming they must rely on a downstream financial institution's regulated status.

- **Multi-party arrangements**: Many modern biometric data processing arrangements involve a chain of vendors — an enterprise client, a cloud platform, and one or more AI/ML service providers. This decision confirms that each layer of the vendor stack may have independent legal defenses to BIPA exposure, reducing the risk of strict joint liability running from the enterprise client to all upstream vendors.

### Financial Services Companies

Financial institutions using third-party biometric authentication vendors in their customer-facing operations should:

- Confirm that their authentication and fraud-detection vendors independently satisfy GLBA financial institution status, rather than assuming the financial institution's own exempt status flows through to its technology vendors under a joint-enterprise theory.
- Review cloud infrastructure contracts to understand the physical location of biometric data processing — particularly whether voiceprints, behavioral biometrics, or other biometric identifiers are processed on servers in Virginia, Oregon, or other non-Illinois AWS regions.
- Retain the GLBA exemption analysis in vendor due diligence documentation as a litigation-readiness measure.

### BIPA Litigation Plaintiffs Bar

For BIPA plaintiffs, the decision reduces the available pool of financially significant defendants in multi-party biometric data cases. If an authentication vendor qualifies for the GLBA exemption and the cloud infrastructure is outside Illinois, plaintiffs may be effectively limited to pursuing the enterprise-level client — typically a financial institution that itself benefits from the GLBA exemption. The net effect may be to further funnel BIPA liability toward mid-size employers in non-financial sectors who use on-premises biometric time-and-attendance systems, where the extraterritoriality and GLBA defenses are unavailable.

### Broader State Law Implications

While the decision addresses BIPA specifically, its extraterritoriality reasoning is broadly applicable. Other states that have enacted biometric privacy laws — including Texas (CUBI), Washington (WA BIPA), and, increasingly, states enacting comprehensive privacy laws with biometric data provisions — have analogous territorial-application questions. Defense counsel in non-BIPA biometric privacy litigation will likely cite *McGoveran* for the general proposition that plaintiff presence in a state is an insufficient hook for applying that state's biometric law to out-of-state data processing.

## What To Watch

- **Cert petition**: No petition for certiorari has been announced as of the date of this report. Given that the Third Circuit is expressly "joining" other courts rather than creating a circuit split, the extraterritoriality holding does not create the circuit conflict typically needed to attract Supreme Court review. The GLBA-exemption-for-vendors question is also unlikely to draw cert interest given the strong consensus across district courts.
- **Illinois legislative response**: BIPA's exemptions have previously attracted legislative attention. Following this decision, Illinois privacy advocates may seek to clarify BIPA's extraterritorial scope or narrow the GLBA exemption's application to downstream technology vendors. Monitor the Illinois General Assembly for proposed BIPA amendments in the 2026-2027 legislative cycle.
- **Impact on voice AI products**: The ruling arrives as voice AI and large language model-based customer service agents proliferate in financial services. Vendors deploying voice biometric authentication as part of AI-powered call center platforms — including AWS Connect, Google CCAI, and Microsoft Azure Communication Services — now have clearer precedent supporting both the extraterritoriality defense and the GLBA vendor exemption.
- **Other circuits**: The Third Circuit's affirmance of the extraterritoriality doctrine adds to precedent from the Seventh Circuit (which governs Illinois directly) and from out-of-circuit district courts that have applied the "primarily and substantially" test. Defendants in the First, Second, and Ninth Circuits may cite *McGoveran* as persuasive authority in analogous BIPA class actions filed in those jurisdictions.
- **Morgan Lewis representation**: Morgan Lewis & Bockius LLP represented AWS in the Third Circuit and publicized the result as a precedential victory.

## Related Reports

- [reports/privacy/illinois-bipa-7th-circuit-retroactivity-2026-04-12.md](reports/privacy/illinois-bipa-7th-circuit-retroactivity-2026-04-12.md) — Seventh Circuit decision on BIPA damages amendment retroactivity; addresses the same statute in the circuit that governs Illinois directly, and sits alongside *McGoveran* as the current appellate-level BIPA landscape.
- [reports/privacy/litigation/illinois-thermoflex-bipa-insurance-coverage-2024-06-06.md](reports/privacy/litigation/illinois-thermoflex-bipa-insurance-coverage-2024-06-06.md) — Seventh Circuit ruling on CGL insurance coverage for BIPA claims; relevant to the downstream financial consequences of BIPA exposure that *McGoveran* helps defendants avoid.
- [reports/privacy/financial-privacy/glba-reform-huizenga-discussion-draft-2026-04-12.md](reports/privacy/financial-privacy/glba-reform-huizenga-discussion-draft-2026-04-12.md) — Congressional discussion draft to modernize GLBA Title V, directly relevant to the statutory framework at the center of the Pindrop exemption holding.

## Sources

1. [*McGoveran v. Amazon Web Services, Inc.*, No. 24-3215 (3d Cir. May 12, 2026) — CourtListener PDF](https://storage.courtlistener.com/pdf/2026/05/12/christine_mcgoveran_v._amazon_web_services_inc.pdf) — Official Third Circuit slip opinion; primary source for all holdings.
2. [Justia case page — McGoveran v. AWS, No. 24-3215 (3d Cir. 2026)](https://law.justia.com/cases/federal/appellate-courts/ca3/24-3215/24-3215-2026-05-12.html) — Docket metadata and opinion text; confirms decision date May 12, 2026.
3. [Verdict News — Third Circuit Affirms Dismissal of BIPA Voiceprint Suit vs. AWS, Pindrop](https://verdict.news/circuit/third-circuit-affirms-dismissal-of-bipa-voiceprint-019e1e2d) — Summary of all five issues resolved on appeal; confirms GLBA exemption and extraterritoriality holdings.
4. [Bloomberg Law — Amazon Defeats Biometric Suit Over John Hancock Customer Calls](https://news.bloomberglaw.com/litigation/amazon-defeats-biometric-suit-over-john-hancock-customer-calls) — News coverage confirming case facts and outcome.
5. [Law360 — 3rd Circ. Says Financial Services Rule Thwarts Privacy Suit](https://www.law360.com/articles/2476581/3rd-circ-says-financial-services-rule-thwarts-privacy-suit) — Legal trade reporting on the financial services rule holding.
6. [Morgan Lewis & Bockius LLP — 3rd Circ. Says Financial Services Rule Thwarts Privacy Suit (Law360 news reprint)](https://www.morganlewis.com/news/2026/05/3rd-circ-says-financial-services-rule-thwarts-privacy-suit) — AWS counsel's publication noting precedential significance.
7. [Blank Rome LLP — Recent Amazon Biometric Privacy Ruling Shows Power of Successful Personal Jurisdiction Challenges in BIPA Class Actions](https://www.blankrome.com/publications/recent-amazon-biometric-privacy-ruling-shows-power-successful-personal-jurisdiction) — Defense counsel analysis of personal jurisdiction and extraterritoriality implications for cloud providers.
8. [JD Supra — Blank Rome analysis (full text)](https://www.jdsupra.com/legalnews/recent-amazon-biometric-privacy-ruling-14435/) — Full Blank Rome client alert with detailed procedural history and implications.
9. [Just The News — Federal appeals court narrows reach of Illinois' biometrics privacy law, handing Amazon a win](https://justthenews.com/nation/states/center-square/biometrics-privacy-laws-territorial-reach-limited-appeals-court-says) — News account confirming Third Circuit's statement that it is joining other courts in limiting BIPA's territorial reach.
10. [Perkins Coie — Amazon and Microsoft Win Summary Judgment in Illinois BIPA Lawsuits Based on Extraterritoriality](https://perkinscoie.com/insights/update/amazon-and-microsoft-win-summary-judgment-illinois-bipa-lawsuits-based) — Prior district court rulings on BIPA extraterritoriality affirmed by the Third Circuit; provides litigation context.
11. [Pindrop — Authentication Is Financial Infrastructure](https://www.pindrop.com/article/authentication-is-financial-infrastructure/) — Pindrop's own description of its authentication services as GLBA-qualifying financial infrastructure; corroborates the statutory analysis underlying the court's GLBA holding.
12. [eCFR — 12 C.F.R. § 225.86 (Federal Reserve Regulation Y — Permissible Financial Activities)](https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-225/subpart-I/section-225.86) — Official regulatory text of the provision the court applied to qualify Pindrop as a financial institution under GLBA.
13. [Madison-St. Clair Record — Amazon's cloud services arm, security company, sued over claims of biometric data violations](https://madisonrecord.com/stories/522621245-amazon-s-cloud-services-arm-security-company-sued-over-claims-of-biometric-data-violations) — Local legal news source confirming December 17, 2019 original filing in Madison County Circuit Court; confirms state court origin of case.
