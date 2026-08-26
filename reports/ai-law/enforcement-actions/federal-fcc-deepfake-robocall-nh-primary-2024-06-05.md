---
title: "FCC Proposes Fines for AI-Based Deepfake Robocalls Before New Hampshire Primary"
date: 2024-06-05
jurisdiction: "Federal"
category: "ai-law"
development_type: "enforcement"
finding_id: "SCAN-20240605-013"
topic_key: "FCC-PROPOSES-FINES-FOR-AI-BASED-DE-2024"
topic_type: "enforcement_action"
first_reported: 2024-06-05
last_updated: 2026-04-15
status_history:
  - "2026-04-15: Updated criminal proceedings section to reflect June 13, 2025 acquittal of Steve Kramer on all charges by NH jury; clarified Executive Summary and Background to distinguish FCC's 3,000-call verified subset (used for forfeiture math) from broader campaign scope of 5,000+ calls."
cluster: "FCC Deepfake Robocall Enforcement: AI-Generated Political Calls (TCPA/STIR-SHAKEN)"
cluster_slug: "fcc-deepfake-robocall-enforcement"
---

# FCC Proposes Fines for AI-Based Deepfake Robocalls Before New Hampshire Primary

**Jurisdiction:** Federal | **Category:** ai-law | **Date:** 2024-06-05

## Executive Summary [HIGH confidence]

In May 2024, the Federal Communications Commission (FCC) adopted two Notices of Apparent Liability (NALs) targeting the perpetrators of an AI-generated deepfake robocall scheme that distributed a fabricated recording of President Biden's voice to at least 5,000 New Hampshire voters — and by some estimates as many as 5,000–10,000 — two days before the state's January 2024 presidential primary. The FCC proposed a $6 million fine against political consultant Steve Kramer — who admitted to orchestrating the scheme — and a separate $2 million fine against Lingo Telecom, the voice service provider that transmitted the spoofed calls in apparent violation of STIR/SHAKEN caller ID authentication rules. The actions represent the FCC's first enforcement proceedings targeting deepfake content distributed via robocall, and followed the agency's February 2024 declaratory ruling confirming that AI-generated voices constitute "artificial or prerecorded voice" under the Telephone Consumer Protection Act (TCPA). By September 2024, Kramer received a final $6 million forfeiture order and Lingo Telecom settled for $1 million with a binding compliance program — establishing the federal enforcement baseline for AI-assisted election interference via telecommunications. (Note: the FCC calculated the $6 million forfeiture based on a verified subset of 3,000 calls for which it could confirm spoofed caller ID violations, not the full campaign volume.) On the criminal side, a New Hampshire jury acquitted Kramer on all charges on June 13, 2025; the FCC civil forfeiture order remains separately outstanding.

## Background [HIGH confidence]

### The Deepfake Robocall Incident

On January 21, 2024 — two days before New Hampshire's first-in-the-nation Democratic presidential primary — thousands of registered Democrats in the state received an unsolicited robocall. The call featured a cloned AI voice impersonating President Biden, using his recognizable phrase "What a bunch of malarkey" and delivering a message urging recipients not to vote in the primary, falsely suggesting that casting a ballot in the primary would prevent them from voting in the November general election. The message told voters to "save your vote" for November instead.

The [New Hampshire Attorney General's office](https://www.doj.nh.gov/news-and-media/steven-kramer-charged-voter-suppression-over-ai-generated-president-biden-robocalls) announced an investigation on January 22, 2024, the day after the calls went out. Independent estimates from anti-robocall monitoring services placed total call volume at 5,000 or more, with some estimates ranging as high as 5,000–25,000; anti-robocall application Nomorobo reported that approximately 76% of detected calls targeted New Hampshire voters specifically. The FCC's enforcement proceedings were based on a verified subset of 3,000 calls for which it could confirm spoofed caller ID violations — that 3,000-call figure drove the forfeiture calculation but does not represent the full scope of the campaign. The calls used a spoofed caller ID that displayed the phone number of a prominent, uninvolved New Hampshire political operative — not the actual originator's number.

### The Actors

Steve Kramer, a 54-year-old political consultant from New Orleans, Louisiana, admitted to drafting the robocall script and hiring Paul Carpenter — a Louisiana-based street magician and world-record holder in straitjacket escapes — to use generative AI tools to clone President Biden's voice and produce the deepfake audio. Kramer also selected the spoofed caller ID number: that of a well-known local political operative who had no connection to the scheme.

### FCC's February 2024 Declaratory Ruling on AI Robocalls

Even before the May 2024 NALs, the FCC acted swiftly in response to the New Hampshire incident. On February 2, 2024, the Commission unanimously adopted [Declaratory Ruling FCC 24-17](https://docs.fcc.gov/public/attachments/FCC-24-17A1.pdf), which clarified that calls made using AI-generated voices are subject to the TCPA's prohibition on "artificial or prerecorded voice" robocalls without the called party's prior express consent. The ruling took immediate effect upon release on February 8, 2024.

As stated by the FCC, the ruling confirmed that "AI technologies that generate human voices, such as voice cloning" fall within the TCPA's existing definition of "artificial or prerecorded voice," triggering the full suite of TCPA consent, disclosure, and opt-out requirements. The ruling also enhanced the FCC's civil enforcement authority, empowering the agency to fine robocallers using AI-generated voices up to $23,000 per violation.

### Truth in Caller ID Act and STIR/SHAKEN Framework

Two statutory and regulatory frameworks were central to the FCC's enforcement actions:

1. **Truth in Caller ID Act (47 U.S.C. § 227(e))**: Prohibits caller ID spoofing conducted with the intent to defraud, cause harm, or wrongfully obtain anything of value. The Act provides the FCC authority to impose forfeitures of up to $10,000 per violation, with a $1 million cap per unlawful campaign.

2. **STIR/SHAKEN caller ID authentication rules**: FCC regulations require voice service providers to digitally sign and authenticate calls using public key cryptography, reducing the ability of bad actors to spoof caller ID. Providers must also implement "Know Your Customer" (KYC) protocols to verify their customers' legitimacy and the accuracy of caller ID information they transmit.

## Detailed Analysis [HIGH confidence]

### NAL Against Steve Kramer (FCC 24-59, May 2024)

The FCC adopted [NAL FCC 24-59](https://docs.fcc.gov/public/attachments/FCC-24-59A1.pdf) on May 23, 2024, proposing a $6 million fine against Steve Kramer for apparent willful violations of the Truth in Caller ID Act. The Commission calculated the proposed forfeiture as follows:

- **Base forfeiture**: $1,000 per spoofed call × 3,000 verified calls = $3,000,000
- **Upward adjustment**: 100% increase for egregiousness of the conduct
- **Total proposed**: $6,000,000

The 3,000-call figure represents the FCC's verified count of spoofed calls for forfeiture computation purposes, not the total number of calls distributed. The FCC cited the egregiousness of the violation because: (1) the calls targeted voters immediately before an election with false information designed to suppress participation; (2) the deepfake technology was used to impersonate a sitting president; and (3) the spoofed caller ID falsely implicated an uninvolved third party.

The [FCC press release](https://docs.fcc.gov/public/attachments/DOC-402762A1.pdf) announcing the NAL stated the calls "apparently violated the Truth in Caller ID Act by maliciously spoofing the number of a prominent local political consultant" — emphasizing that the harm extended not only to recipients but to the individual whose number was impersonated.

On September 26, 2024, the FCC voted to convert the NAL into a final [forfeiture order of $6 million](https://docs.fcc.gov/public/attachments/DOC-405811A1.pdf) against Kramer, making it a binding monetary penalty subject to collection. Kramer has publicly stated he does not intend to pay the forfeiture.

### NAL Against Lingo Telecom (May 2024) and Settlement

Simultaneously, the FCC adopted a second NAL proposing a $2 million fine against [Lingo Telecom](https://www.fcc.gov/document/fcc-settles-spoofed-ai-generated-robocalls-case), the voice service provider that transmitted Kramer's calls. The FCC alleged Lingo violated the FCC's STIR/SHAKEN rules by:

1. Failing to implement reasonable KYC protocols that would have identified the calls as potentially fraudulent before transmission;
2. Incorrectly labeling the calls with the highest level of attestation ("A-level attestation") — signaling to downstream carriers that the caller ID was verified — when in fact the caller ID was spoofed.

On August 21, 2024, Lingo Telecom agreed to settle the proceeding for a reduced [$1 million civil penalty](https://docs.fcc.gov/public/attachments/DOC-404951A1.pdf) plus a compliance program described by the FCC as the "first-of-its-kind" for STIR/SHAKEN. The compliance plan requires Lingo to:

- Strictly adhere to FCC STIR/SHAKEN authentication standards
- Implement robust KYC and "Know Your Upstream Provider" (KYUP) protocols
- Submit to compliance monitoring and auditing

### Criminal Charges in New Hampshire — Outcome: Acquittal

Parallel to the FCC proceedings, New Hampshire state prosecutors brought criminal charges against Kramer. He was [indicted](https://www.nbcnews.com/politics/politics-news/steve-kramer-admitted-deepfaking-bidens-voice-new-hampshire-primary-rcna153626) on felony counts of voter suppression and misdemeanor counts of impersonating a candidate — charges distributed across four New Hampshire counties based on the residences of identified call recipients: Rockingham County, Belknap County, Grafton County, and Merrimack County.

On June 13, 2025, a New Hampshire jury [acquitted Kramer on all charges](https://www.nhpr.org/nh-news/2025-06-13/political-operative-fake-biden-robocalls-nh-primary-found-not-guilty), including 11 felony voter suppression counts (each carrying up to seven years in prison) and the accompanying candidate impersonation counts. The defense successfully argued that Kramer's message did not name Biden as a declared candidate and that the intent element required for voter suppression had not been proven beyond a reasonable doubt. The acquittal does not affect the FCC's civil forfeiture order — the $6 million civil penalty is a separate administrative proceeding that does not require a criminal conviction, and it remains outstanding.

### FCC Rulemaking on AI in Political Advertising

On a related but distinct track, the FCC separately launched a [Notice of Proposed Rulemaking (NPRM)](https://www.dwt.com/blogs/artificial-intelligence-law-advisor/2024/06/fcc-targets-biden-robo-deepfakes-and-political-ai) in June 2024 addressing the broader use of AI-generated content in political advertising via telecommunications — signaling that the Kramer/Lingo enforcement actions were part of a wider regulatory initiative, not isolated responses.

## Impact Assessment [MEDIUM confidence]

### Enforcement Signal for AI-Assisted Election Interference

The twin NALs represent the FCC's most consequential enforcement action targeting AI-generated content in a political context to date. The $6 million forfeiture against Kramer is notable for its per-violation structure and the 100% egregiousness multiplier — signaling the FCC's willingness to maximize available penalty authority when AI is weaponized for voter suppression.

Enforcement observers, including [Davis Wright Tremaine](https://www.dwt.com/blogs/artificial-intelligence-law-advisor/2024/06/fcc-targets-biden-robo-deepfakes-and-political-ai), characterized the actions as "a clear signal that the FCC is likely to continue zeroing in on illegal robocalls" and as an indicator of the agency's expanding focus on AI-related enforcement in the telecommunications space.

### Voice Service Provider Obligations

The Lingo Telecom settlement establishes meaningful precedent for voice service providers. The case demonstrates that providers cannot rely on customer representations alone to satisfy STIR/SHAKEN attestation requirements — they must implement proactive KYC and KYUP protocols capable of catching fraudulent campaigns before transmission. The "first-of-its-kind" compliance plan imposed on Lingo sets a template that the FCC may impose on future violators.

### TCPA Compliance for AI Voice Technologies

The February 2024 declaratory ruling, applied in the context of the Kramer NAL, means all callers using AI-generated or voice-cloned audio in outbound calls must now obtain prior express consent from recipients (absent an emergency purpose or applicable exemption), provide caller identification and disclosure information, and offer opt-out mechanisms in calls that constitute telemarketing. Failure to comply exposes callers to FCC civil penalties of up to $23,000 per call, plus potential private TCPA litigation where consumers can recover $500–$1,500 per unauthorized call.

### Intersection with State Law

The New Hampshire criminal prosecution illustrates both the potential and limits of using existing state voter suppression and candidate impersonation statutes against AI-generated deepfake robocall schemes. Kramer's June 2025 acquittal demonstrates that state criminal statutes drafted before the advent of AI voice cloning may not map cleanly onto these new fact patterns — specifically, the jury was not persuaded that the requisite criminal intent for voter suppression had been proven, or that Biden qualified as an "impersonated candidate" under the applicable statute. The acquittal may prompt states to draft AI-specific election interference statutes with clearer intent elements and broader definitions of candidate impersonation. Importantly, however, the FCC civil enforcement track proceeded entirely independently and produced a final $6 million forfeiture order — underscoring that federal telecommunications enforcement does not depend on the outcome of parallel state criminal proceedings.

## Action Items

- **Voice service providers**: Audit STIR/SHAKEN attestation workflows and KYC/KYUP protocols immediately. The Lingo Telecom settlement establishes that highest-level attestation applied to unverified customer traffic constitutes an apparent violation and that the FCC will impose compliance programs as part of settlements.
- **Political campaigns and consultants**: Any use of AI-generated or voice-cloned audio in outbound calls — including robocalls — now requires prior express consent under the TCPA as clarified by FCC Declaratory Ruling FCC 24-17. Obtain legal counsel before deploying such technologies in political communications.
- **AI voice technology vendors**: Assess whether customers' use of voice-cloning or generative AI audio products for robocalls or telephony campaigns could expose the vendor to secondary liability or regulatory scrutiny; consider implementing contractual prohibitions and monitoring for misuse.
- **Monitor FCC AI political ad NPRM**: The FCC's June 2024 NPRM on AI in political advertising is expected to produce rules that could impose additional disclosure and consent requirements for AI-generated content across broadcast, cable, and telephone platforms. Track for comment deadlines and final rulemaking timelines.
- **State election law tracking**: The NH acquittal signals a gap between existing state voter suppression statutes and novel AI deepfake fact patterns. Other states should examine whether existing statutes are adequate or whether new AI-specific election interference legislation is needed. Monitor state AG offices and legislatures for parallel enforcement or new legislation.

## Related Reports

- [reports/ai-law/federal-regulation/federal-senate-ai-election-bills-committee-2024-06-10.md](reports/ai-law/federal-regulation/federal-senate-ai-election-bills-committee-2024-06-10.md) — Senate legislation targeting AI use in elections, directly relevant as federal legislative counterpart to the FCC's enforcement approach.
- [reports/ai-law/enforcement-actions/massachusetts-ag-ai-advisory-2024-04-22.md](reports/ai-law/enforcement-actions/massachusetts-ag-ai-advisory-2024-04-22.md) — State AG AI enforcement action illustrating the parallel state enforcement track alongside federal FCC actions.

## Sources

1. [FCC Proposes $6 Million Fine for Illegal Robocalls (DOC-402762A1)](https://docs.fcc.gov/public/attachments/DOC-402762A1.pdf) — Official FCC press release announcing NAL against Steve Kramer, May 2024
2. [FCC NAL Against Steve Kramer (FCC 24-59)](https://docs.fcc.gov/public/attachments/FCC-24-59A1.pdf) — Full text of the Notice of Apparent Liability against Kramer
3. [FCC Forfeiture Order Against Kramer (DOC-405811A1)](https://docs.fcc.gov/public/attachments/DOC-405811A1.pdf) — Final $6 million forfeiture order adopted September 26, 2024
4. [Lingo Telecom $1 Million Settlement (DOC-404951A1)](https://docs.fcc.gov/public/attachments/DOC-404951A1.pdf) — Official FCC announcement of Lingo Telecom consent decree
5. [FCC Issues $6M Fine for NH Robocalls](https://www.fcc.gov/document/fcc-issues-6m-fine-nh-robocalls) — FCC official document page for the Kramer forfeiture order
6. [FCC Settles Spoofed AI-Generated Robocalls Case](https://www.fcc.gov/document/fcc-settles-spoofed-ai-generated-robocalls-case) — FCC official document page for the Lingo Telecom settlement
7. [FCC Declaratory Ruling FCC 24-17 (AI Robocalls)](https://docs.fcc.gov/public/attachments/FCC-24-17A1.pdf) — Full text of February 2024 declaratory ruling that AI voice cloning is subject to TCPA
8. [FCC Makes AI-Generated Voices in Robocalls Illegal](https://www.fcc.gov/document/fcc-makes-ai-generated-voices-robocalls-illegal) — FCC official announcement of FCC 24-17 declaratory ruling
9. [NH DOJ: Steven Kramer Charged with Voter Suppression](https://www.doj.nh.gov/news-and-media/steven-kramer-charged-voter-suppression-over-ai-generated-president-biden-robocalls) — New Hampshire Department of Justice press release on criminal indictment
10. [NH DOJ: Kramer NAL Document](https://www.doj.nh.gov/sites/g/files/ehbemt721/files/inline-documents/sonh/item-2-kramer-robocall-nal.pdf) — Copy of the FCC NAL hosted by the NH DOJ
11. [NPR: Criminal Charges and FCC Fines for Deepfake Biden Robocalls](https://www.npr.org/2024/05/23/nx-s1-4977582/fcc-ai-deepfake-robocall-biden-new-hampshire-political-operative) — NPR reporting on the dual FCC/criminal enforcement actions
12. [NBC News: Steve Kramer Indicted](https://www.nbcnews.com/politics/politics-news/steve-kramer-admitted-deepfaking-bidens-voice-new-hampshire-primary-rcna153626) — NBC News reporting on the criminal indictment details and Paul Carpenter's role
13. [CyberScoop: FCC Hits Operative with $6 Million Fine](https://cyberscoop.com/fcc-fine-joe-biden-deepfake-new-hampshire-robocall-steve-kramer/) — CyberScoop reporting on the September 2024 forfeiture order
14. [Davis Wright Tremaine: Two FCC Actions on AI](https://www.dwt.com/blogs/artificial-intelligence-law-advisor/2024/06/fcc-targets-biden-robo-deepfakes-and-political-ai) — Law firm analysis of both NALs and the broader FCC AI enforcement/rulemaking trajectory
15. [Perkins Coie: FCC Fines Telecom for Deepfake Robocalls](https://perkinscoie.com/insights/update/fcc-fines-telecom-transmitted-ai-generated-deepfake-robocalls-impersonating) — Law firm analysis of the Lingo Telecom action and STIR/SHAKEN compliance implications
16. [Comm Law Group: Lingo Telecom $1 Million Settlement](https://commlawgroup.com/2024/lingo-telecom-to-pay-1-million-in-fcc-settlement-over-deepfake-robocalls/) — Detailed analysis of the Lingo Telecom consent decree and compliance program
17. [Wilson Sonsini: FCC Rules AI-Generated Voices Are "Artificial"](https://www.wsgr.com/en/insights/fcc-rules-ai-generated-voices-are-artificial-under-the-tcpa.html) — Law firm analysis of the February 2024 TCPA declaratory ruling
18. [PBS NewsHour: Political Consultant Faces $6 Million Fine and Criminal Charges](https://www.pbs.org/newshour/politics/political-consultant-behind-ai-generated-biden-robocalls-faces-6-million-fine-and-criminal-charges) — PBS reporting on the dual regulatory and criminal exposure
19. [NHPR: Political Operative Found Not Guilty (June 13, 2025)](https://www.nhpr.org/nh-news/2025-06-13/political-operative-fake-biden-robocalls-nh-primary-found-not-guilty) — New Hampshire Public Radio reporting on the jury acquittal of Kramer on all criminal charges
20. [WBUR: NH Jury Acquits Consultant Behind AI Robocalls on All Charges (June 16, 2025)](https://www.wbur.org/news/2025/06/16/biden-ai-robocall-new-hampshire-steven-kramer-not-guilty) — Additional reporting on the acquittal outcome and remaining FCC civil forfeiture
