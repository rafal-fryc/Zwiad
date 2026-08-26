---
title: "Google Accused of Collecting Disability Data from California DMV Website Visitors: Wilson v. Google LLC (N.D. Cal. 2024)"
date: 2024-05-29
jurisdiction: "California"
category: "privacy"
development_type: "litigation"
finding_id: "SCAN-20240529-002"
topic_key: "california-49d3d85c-2024"
topic_type: "enforcement_action"
first_reported: 2024-05-29
last_updated: 2026-04-15
status_history: []
cluster: "CIPA Website Wiretapping Class Actions"
cluster_slug: "cipa-website-wiretapping-litigation"
---

# Google Accused of Collecting Disability Data from California DMV Website Visitors: Wilson v. Google LLC (N.D. Cal. 2024)

**Jurisdiction:** California, Federal | **Category:** Privacy | **Date:** 2024-05-29

## Executive Summary [HIGH confidence]

A proposed class action filed in May 2024 alleges that Google LLC secretly embedded tracking tools — Google Analytics and DoubleClick — on the California Department of Motor Vehicles (DMV) website to intercept and monetize the disability status and personal information of visitors applying for or renewing disability parking placards. The plaintiff, Katherine Wilson, asserts that Google collected her information without consent when she used the California MyDMV portal and used it for its own advertising business. The case, *Wilson v. Google LLC*, No. 24-cv-03176-EKL (N.D. Cal.), invokes the federal [Driver's Privacy Protection Act (DPPA), 18 U.S.C. § 2721 et seq.](https://www.law.cornell.edu/uscode/text/18/2721), and the [California Invasion of Privacy Act (CIPA), Cal. Penal Code §§ 630–638](https://www.leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=PEN&division=&title=15.&part=1.&chapter=1.5.&article=). In a March 2025 ruling, Judge Eumi K. Lee dismissed the DPPA claim with leave to amend but allowed the CIPA wiretapping claim to proceed, finding the plaintiff had adequately alleged Google intercepted her communications for its own advertising benefit.

---

## Background and Factual Allegations [HIGH confidence]

### The MyDMV Portal and Disability Placard Renewals

The California DMV offers an online portal — MyDMV — through which residents can apply for, renew, or check the status of disability parking placards. These services require visitors to submit personal information including name, address, and disability status. The plaintiff Katherine Wilson used this portal in or around June 2023 to renew her disability parking placard.

### Alleged Google Tracking

According to the complaint, Google had embedded [Google Analytics and DoubleClick](https://exportcompliancedaily.com/article/2024/05/29/google-ad-tools-illegally-collect-disability-data-from-calif-dmv-class-action-2405280027?BC=bc_674b1056d531b) tags on the DMV website. Through these tools, Google allegedly:

- Intercepted and collected visitors' email addresses, disability information, disability placard details, and other personal identifying information as that data was submitted by users;
- Transmitted this information from the DMV's web infrastructure to Google's servers;
- Used the collected data to generate revenue for Google's advertising and marketing business — without users' knowledge or consent.

The complaint describes Google's conduct as "secretly" using these tools to intercept communications "in transit," characterizing Google as operating for its own commercial benefit rather than as a contractor acting solely on behalf of the DMV.

### Class Definition

The complaint was filed on behalf of all individuals who used the California DMV website to apply for, renew, or check the status of a disability parking placard, and whose personal information Google allegedly collected without consent.

---

## Legal Claims [HIGH confidence]

### Count 1: Driver's Privacy Protection Act (DPPA), 18 U.S.C. § 2721

The [DPPA](https://en.wikipedia.org/wiki/Driver%27s_Privacy_Protection_Act) is a 1994 federal statute enacted as part of the Violent Crime Control and Law Enforcement Act. It prohibits any person from knowingly obtaining or disclosing personal information from a motor vehicle record for any purpose not specifically permitted by the statute. Permissible purposes include government functions, motor vehicle safety, litigation, insurance, and licensed investigative work.

The plaintiff alleged that Google "obtained" her personal information from a "motor vehicle record" for an impermissible purpose — namely, commercial advertising — by intercepting data transmitted through the DMV's website.

**DPPA Outcome (March 2025):** Judge Lee dismissed this claim with leave to amend. The court reasoned that because the personal information Google allegedly intercepted "came from Plaintiff herself when she entered it into the DMV's website," it did not constitute information obtained "from a motor vehicle record" within the meaning of the DPPA. The plaintiff was granted until April 15, 2025 to amend her DPPA allegations.

### Count 2: California Invasion of Privacy Act (CIPA), Cal. Penal Code § 631

[CIPA § 631](https://codes.findlaw.com/ca/penal-code/pen-sect-631/) prohibits the unauthorized interception of communications without the consent of all parties. Applied to digital contexts, courts have increasingly considered whether third-party analytics and tracking tools embedded in websites constitute unlawful "wiretapping" of user communications.

The plaintiff alleged that Google, by secretly intercepting communications between users and the DMV as those communications were "in transit" (i.e., as the user entered and submitted data), violated CIPA's prohibition on interception without consent.

**CIPA Outcome (March 2025):** Judge Lee denied Google's motion to dismiss. The court held that Wilson had adequately alleged that:

1. Google intercepted her communications while they were in transit, satisfying CIPA's "in transit" requirement;
2. Google acted for its own benefit — not merely as an extension or agent of the DMV — by collecting the data for its own advertising purposes;
3. Google's conduct was distinguishable from cases where a vendor was explicitly contracted to provide advertising, because here Wilson alleged Google uses its tools to encourage website operators, including government agencies, to share user data that Google then monetizes.

The court declined to dismiss the CIPA claim, and it will proceed.

---

## March 2025 Court Ruling in Detail [HIGH confidence]

*Wilson v. Google LLC*, No. 24-cv-03176-EKL, 2025 U.S. Dist. LEXIS 55629 (N.D. Cal. Mar. 25, 2025), was decided by [U.S. District Judge Eumi K. Lee](https://cand.uscourts.gov/judges/ekl/lee-eumi-k) of the Northern District of California.

**CIPA claim survives:** Judge Lee found it sufficient that the complaint alleged Google operated independently — collecting data for its own advertising revenue — rather than functioning solely as the DMV's technical contractor. This is a critical legal distinction under CIPA litigation: the "extension" defense (arguing that a vendor is merely carrying out the website operator's instructions) failed here at the motion to dismiss stage because the plaintiff alleged Google obtained a concrete commercial benefit from the data independent of any direction by the DMV.

**DPPA claim dismissed:** The judge parsed the word "from" in the statutory phrase "personal information from a motor vehicle record" and found that data entered by a user into a web form is not the same as data disclosed from a stored government record. This textual reasoning may limit DPPA's applicability to "real-time" interception of online form submissions. The plaintiff was given leave to amend to cure this deficiency.

**Broader significance:** The ruling adds to a growing body of federal district court decisions on CIPA's application to third-party website analytics tools. The "extension" vs. independent benefit analysis used by Judge Lee aligns with other CIPA cases but applies the doctrine in a novel government-website context.

---

## Broader CIPA Litigation Landscape [MEDIUM confidence]

The *Wilson v. Google* case sits at the intersection of two active areas of privacy litigation: CIPA website wiretapping cases and tracking technology suits against both private companies and government agencies.

### Surge in CIPA Claims

As of mid-2025, [approximately 1,500 CIPA lawsuits had been filed in an 18-month period](https://www.bytebacklaw.com/2025/11/2025-update-website-tracking-litigation-and-enforcement/), reflecting an explosive growth in claims targeting website operators' use of cookies, pixels, session replay software, and analytics platforms including Google Analytics and Meta Pixel. Potential statutory damages under CIPA are up to $5,000 per violation or three times actual damages — whichever is greater — plus attorney's fees, making even small-scale violations financially significant at class scale.

### Related CIPA Cases on Google Analytics

Courts have divided on whether using Google Analytics constitutes "wiretapping" under state law. For example, in a separate context, a Massachusetts high court ruled that use of Google Analytics and Meta Pixel does not violate the Massachusetts Wiretap Act — a contrast to the California approach in *Wilson*.

The [National Law Review has analyzed](https://natlawreview.com/article/when-google-follows-you-dmv-where-consent-gets-lost-traffic) the *Wilson* ruling as highlighting a potential gap in privacy protection: data stored in a government database is federally protected by the DPPA, but the same data loses that protection while the user is actively transmitting it to the government agency.

### California SB 690 — Stalled CIPA Reform

California's legislature considered [Senate Bill 690](https://www.duanemorris.com/alerts/california_sb690_stalls_assembly_cipa_liability_remains_least_through_2026_0725.html), which would have created a safe harbor for routine commercial tracking tools subject to CCPA opt-out rights, potentially limiting CIPA exposure for businesses using tools like Google Analytics. However, SB 690 failed to clear the Assembly before the 2025 session adjourned and is a two-year bill eligible for reconsideration in the 2026 legislative session (beginning January 5, 2026). Privacy advocates including the EFF, ACLU California Action, and Privacy Rights Clearinghouse opposed the bill, and its retroactivity provision was removed before final passage through the Senate.

---

## Implications for Website Operators [MEDIUM confidence]

### Government Agencies

The case raises significant questions for government agencies that use commercial analytics platforms. An agency embedding Google Analytics or similar tools on a site that processes sensitive personal information — including disability data, health records, or financial information — may unwittingly expose itself and its analytics vendors to CIPA liability if users are not clearly notified and given consent mechanisms.

### Private-Sector Businesses

The ruling reinforces the compliance risk for any California-facing website using third-party analytics. Key considerations:

1. **Consent mechanisms:** Businesses should ensure cookie consent banners clearly disclose the specific types of data collected and the third parties receiving that data, including Google Analytics and advertising platforms.
2. **Vendor contracts:** Pass-down contractual provisions should specify permissible data uses and prohibit analytics vendors from using collected data for their own commercial purposes.
3. **Sensitive categories:** Platforms collecting disability, health, or financial data carry heightened risk under both CIPA and the DPPA — even if the platform is an intermediary rather than the primary data holder.
4. **"Extension" defense:** At the motion-to-dismiss stage, the *Wilson* ruling demonstrates that alleging a vendor acts for its own benefit (not just the operator's) is sufficient to survive dismissal. Organizations that use Google Analytics for advertising optimization rather than pure internal analytics face greater CIPA exposure.

---

## Official Legal Text [HIGH confidence]

- **Driver's Privacy Protection Act:** [18 U.S.C. § 2721](https://www.law.cornell.edu/uscode/text/18/2721) (Cornell LII); [18 U.S.C. § 2721 (House.gov)](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title18-section2721&num=0&edition=prelim)
- **California Invasion of Privacy Act:** [Cal. Penal Code §§ 630–638 (leginfo.legislature.ca.gov)](https://www.leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=PEN&division=&title=15.&part=1.&chapter=1.5.&article=); [Cal. Penal Code § 631 (FindLaw)](https://codes.findlaw.com/ca/penal-code/pen-sect-631/)
- **Case complaint (PDF):** [Wilson v. Google, Complaint, No. 5:24-cv-03176 (N.D. Cal. May 24, 2024)](https://cdn.arstechnica.net/wp-content/uploads/2024/05/Wilson-v-Google-Complaint-5-24-2024.pdf)

---

## Sources

1. [Class Action Complaint, Wilson v. Google LLC, No. 5:24-cv-03176 (PDF via Ars Technica)](https://cdn.arstechnica.net/wp-content/uploads/2024/05/Wilson-v-Google-Complaint-5-24-2024.pdf) — Official court filing; primary source for factual allegations.
2. [Class Action Hits Google Over Collecting Disability Data From California Drivers — Law.com / The Recorder (May 30, 2024)](https://www.law.com/therecorder/2024/05/30/class-action-hits-google-over-collecting-disability-data-from-california-drivers/)
3. [Google Ad Tools Illegally Collect Disability Data From Calif. DMV: Class Action — Export Compliance Daily (May 29, 2024)](https://exportcompliancedaily.com/article/2024/05/29/google-ad-tools-illegally-collect-disability-data-from-calif-dmv-class-action-2405280027?BC=bc_674b1056d531b)
4. [Google Sued Over Data Collection From DMV — MediaPost (May 29, 2024)](https://www.mediapost.com/publications/article/396383/google-sued-over-data-collection-from-dmv.html)
5. [Disabled Driver Advances Google Suit Over Collection of DMV Data — Bloomberg Law (Mar. 2025)](https://news.bloomberglaw.com/privacy-and-data-security/disabled-driver-advances-google-suit-over-collection-of-dmv-data)
6. [Google Must Face Privacy Claim Over Data Collection From DMV — MediaPost (Mar. 28, 2025)](https://www.mediapost.com/publications/article/404592/google-must-face-privacy-claim-over-data-collectio.html)
7. [WHEN GOOGLE FOLLOWS YOU TO THE DMV: Where Consent Gets Lost in the Traffic — National Law Review (Mar. 30, 2025)](https://natlawreview.com/article/when-google-follows-you-dmv-where-consent-gets-lost-traffic)
8. [WHEN GOOGLE FOLLOWS YOU TO THE DMV: Where Consent Gets Lost in the Traffic — CIPAWorld (Mar. 30, 2025)](https://cipaworld.com/2025/03/30/when-google-follows-you-to-the-dmv-where-consent-gets-lost-in-the-traffic/)
9. [Wilson v. Google LLC (5:24-cv-03176) — PACER Monitor (Public Docket)](https://www.pacermonitor.com/public/case/53679786/Wilson_v_Google_LLC_)
10. [18 U.S.C. § 2721 — Driver's Privacy Protection Act (Cornell LII)](https://www.law.cornell.edu/uscode/text/18/2721)
11. [Cal. Penal Code §§ 630–638, California Invasion of Privacy Act (leginfo.legislature.ca.gov)](https://www.leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=PEN&division=&title=15.&part=1.&chapter=1.5.&article=)
12. [2025 Update: Website Tracking Litigation and Enforcement — ByteBack Law (2025)](https://www.bytebacklaw.com/2025/11/2025-update-website-tracking-litigation-and-enforcement/)
13. [California SB 690 Stalls in Assembly — Duane Morris LLP (Jul. 2025)](https://www.duanemorris.com/alerts/california_sb690_stalls_assembly_cipa_liability_remains_least_through_2026_0725.html)
14. [Driver's Privacy Protection Act — Wikipedia](https://en.wikipedia.org/wiki/Driver%27s_Privacy_Protection_Act)
15. [Plaintiff Alleges Tech Giant's Illegal Data Collection on Government Site — Northern California Record](https://norcalrecord.com/stories/671017981-plaintiff-alleges-tech-giant-s-illegal-data-collection-on-government-site)
