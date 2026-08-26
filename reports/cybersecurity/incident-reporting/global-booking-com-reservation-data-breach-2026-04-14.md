---
title: "Booking.com Confirms Reservation Data Breach; Forces PIN Resets Amid Phishing Wave"
finding_id: "SCAN-20260414-009"
format: "client-alert"
date: 2026-04-14
jurisdiction: "Global"
category: "cybersecurity"
development_type: "enforcement"
topic_key: "global-a11b9dc1-2026"
topic_type: "guidance"
first_reported: 2026-04-14
last_updated: 2026-04-14
status_history: []
cluster: "Booking.com 2026 Reservation Data Breach"
cluster_slug: "booking-com-2026-data-breach"
---

# Booking.com Confirms Reservation Data Breach; Forces PIN Resets Amid Phishing Wave

**Jurisdiction:** Global, EU, Netherlands | **Category:** cybersecurity | **Date:** 2026-04-14

## Summary [HIGH confidence]

Amsterdam-based Booking.com confirmed on April 13, 2026 that unauthorized parties accessed customer reservation data — including names, email and postal addresses, phone numbers, and booking details — though the company says no financial data was taken. Booking.com has forced PIN resets across existing and past reservations and is individually notifying affected users, while security researchers report the stolen data is already fueling hyper-targeted phishing campaigns against travelers via email and WhatsApp. The incident echoes a 2018 partner-credential compromise for which the Dutch Data Protection Authority (AP) fined Booking.com €475,000 in 2021 for missing the GDPR's 72-hour notification deadline.

## Key Facts [HIGH confidence]

- Booking.com confirmed the breach publicly on April 13, 2026 and began emailing impacted customers from `noreply@booking.com`, per [TechCrunch](https://techcrunch.com/2026/04/13/booking-com-confirms-hackers-accessed-customers-data/) and [The Register](https://www.theregister.com/2026/04/13/bookingcom_breach/).
- Exposed data categories include customer names, email addresses, postal addresses, phone numbers, reservation details, and messages exchanged with accommodations; the company states financial information was not accessed, according to [BleepingComputer](https://www.bleepingcomputer.com/news/security/new-bookingcom-data-breach-forces-reservation-pin-resets/) and [SecurityWeek](https://www.securityweek.com/booking-com-says-hackers-accessed-user-information/).
- Booking.com has not disclosed the number of affected users but stated "the issue has been fully contained" and is forcing reservation PIN resets across past and current bookings to prevent unauthorized trip modifications or cancellations, per [Skift](https://skift.com/2026/04/13/booking-com-hacked-data-breach-reservations/).
- The incident appears to follow the industry's well-documented supply-chain pattern: attackers compromise hotel partner credentials (often via infostealer malware) and then mine reservation systems linked to Booking.com, rather than breaching Booking.com's core systems directly — as analyzed by [Cyber News Centre](https://www.cybernewscentre.com/14th-april-2026-cyber-update-booking-com-data-breach-exposes-supply-chain-vulnerabilities-as-customers-face-targeted-phishing/).
- Security researchers and national press are tracking an active wave of targeted phishing against travelers using the leaked reservation specifics, including WhatsApp-based "pay now or lose your booking" scams, per [Cybernews](https://cybernews.com/news/booking-com-breach-phishing-travel-data-exposed/) and [DutchNews.nl](https://www.dutchnews.nl/2026/04/booking-com-warns-customers-after-reservation-data-breach/).
- The Dutch Data Protection Authority (Autoriteit Persoonsgegevens) is aware of the incident; because Booking.com's lead supervisory authority is the AP, GDPR Article 33's 72-hour notification obligation and Article 34 affected-individual notification apply, per [DutchNews.nl](https://www.dutchnews.nl/2026/04/booking-com-warns-customers-after-reservation-data-breach/).
- In 2021, the AP fined Booking.com €475,000 for reporting a 2018 partner-credential breach 22 days late — 19 days past the GDPR deadline — establishing precedent relevant to the current incident, per the [European Data Protection Board](https://www.edpb.europa.eu/news/national-news/2020/dutch-sa-fines-bookingcom-delay-reporting-data-breach_en) and [Hunton Privacy Blog](https://www.hunton.com/privacy-and-cybersecurity-law-blog/dutch-regulator-fines-booking-com-475000-euros-for-late-breach-reporting).

## Action Items

- **Travelers with Booking.com reservations:** Treat any unexpected message referencing your booking (email, SMS, WhatsApp, or in-app chat) as suspect, even if it cites accurate reservation details. Never pay or re-enter card data via links in such messages — log in directly through the Booking.com app or website.
- **Hotel and accommodation partners:** Immediately review extranet access logs, rotate credentials, enable MFA on Booking.com partner accounts, and scan staff endpoints for infostealer malware, which remains the dominant initial access vector in travel-sector supply-chain compromises.
- **Privacy and security teams at travel-adjacent companies:** Re-examine third-party and partner-channel risk controls. Confirm breach-notification runbooks can meet the GDPR 72-hour clock when the triggering event is a partner-side compromise rather than a direct intrusion.
- **EU/EEA data subjects:** If you do not receive an individual notification but suspect your booking data was exposed, you may lodge a complaint with your national DPA or the Dutch AP under GDPR Article 77.
- **Monitor** for forthcoming statements from the Dutch AP, potential enforcement activity, and any follow-on class actions in EU Member States or the UK under UK GDPR.

## Related Reports

- [Anthropic Claude "Mythos" Cyberattack](reports/cybersecurity/anthropic-claude-mythos-cyberattack-2026-04-12.md) — Another high-profile 2026 incident illustrating how modern threat actors weaponize leaked operational data for downstream targeted attacks.
- [California CCPA Cybersecurity Audit Class Litigation](reports/cybersecurity/california-ccpa-cybersecurity-audit-class-litigation-2026-04-14.md) — Tangential: same regulatory theme (post-breach accountability), but California/CCPA rather than GDPR; included for comparative cybersecurity-governance context.

## Sources

1. [TechCrunch — Booking.com confirms hackers accessed customers' data](https://techcrunch.com/2026/04/13/booking-com-confirms-hackers-accessed-customers-data/) — Primary confirmation of the breach and data categories.
2. [BleepingComputer — New Booking.com data breach forces reservation PIN resets](https://www.bleepingcomputer.com/news/security/new-bookingcom-data-breach-forces-reservation-pin-resets/) — Technical details on PIN reset scope and exposed fields.
3. [The Register — Booking.com warns of possible reservation data exposure](https://www.theregister.com/2026/04/13/bookingcom_breach/) — Independent corroboration and company statement analysis.
4. [SecurityWeek — Booking.com Says Hackers Accessed User Information](https://www.securityweek.com/booking-com-says-hackers-accessed-user-information/) — Security-industry coverage confirming data categories and containment claim.
5. [Skift — Booking.com Warns Travelers of Reservation Data Breach](https://skift.com/2026/04/13/booking-com-hacked-data-breach-reservations/) — Travel-industry perspective and PIN-reset rationale.
6. [Cybernews — Booking.com breach sparks scam wave targeting travelers' bookings](https://cybernews.com/news/booking-com-breach-phishing-travel-data-exposed/) — Reporting on downstream phishing activity.
7. [Cyber News Centre — 14 April 2026 Cyber Update](https://www.cybernewscentre.com/14th-april-2026-cyber-update-booking-com-data-breach-exposes-supply-chain-vulnerabilities-as-customers-face-targeted-phishing/) — Supply-chain attack-vector analysis.
8. [DutchNews.nl — Booking.com warns customers after reservation data breach](https://www.dutchnews.nl/2026/04/booking-com-warns-customers-after-reservation-data-breach/) — Confirms Dutch AP awareness and Netherlands-angle reporting.
9. [European Data Protection Board — Dutch SA fines Booking.com for delay in reporting data breach](https://www.edpb.europa.eu/news/national-news/2020/dutch-sa-fines-bookingcom-delay-reporting-data-breach_en) — Official EDPB record of the €475,000 2021 fine precedent.
10. [Hunton Privacy & Cybersecurity Law Blog — Dutch Regulator Fines Booking.com 475,000 Euros for Late Breach Reporting](https://www.hunton.com/privacy-and-cybersecurity-law-blog/dutch-regulator-fines-booking-com-475000-euros-for-late-breach-reporting) — Law-firm analysis of the GDPR Article 33 precedent.
