# Scanner Findings Review

**Pipeline Run:** 2026-04-13T16-53-44
**Scan Date:** 2026-04-13
**Total Findings:** 6
**Sources Scanned:** 5 successful, 5 failed

## Source Failures

- Lexology practical know-how digest (Lexology---practical-know-how-1.html): HTML file is single-line with 25,000+ tokens; cannot be read via Read tool (line-based chunking ineffective). WebFetch is not permitted in this environment. Article URLs were identified in the file via grep but content was inaccessible for direct extraction. Search-based supplementation was used to cover the same topics.
- Lexology PRO Quick Tip #1 email (Quick-tip-1-Save-hours-of-legal-research-time-with-0.html): Not a regulatory digest — email is a Lexology PRO welcome/marketing campaign about research tools. No regulatory content to extract. Intentionally skipped.
- FTC Press Releases: WebFetch not permitted. FTC press release page not directly accessible. Recent FTC enforcement developments captured via WebSearch supplementation.
- NIST CSRC News: WebFetch not permitted. NIST CSRC page not directly accessible. Recent NIST publications captured via WebSearch supplementation.
- Congress.gov Privacy/Data Bills: WebFetch not permitted. Congress.gov search page not directly accessible. State and federal legislative developments captured via WebSearch supplementation.

## Findings

### 1. [SCAN-20260413-002] Proposed State Privacy Law Update: April 13, 2026 — Kentucky ACR Bill Delivered to Governor, Maine Bill Stalled
- [ ] Approve
- **Source:** Troutman Pepper Locke / Privacy + Cyber + AI
- **URL:** https://www.troutmanprivacy.com/2026/04/proposed-state-privacy-law-update-april-13-2026/
- **Category:** privacy
- **Relevance:** high
- **Jurisdiction:** Federal
- **Type:** legislation
- **Summary:** The April 13, 2026 weekly state privacy law update reports that Kentucky's HB 692 — which adds automatic content recognition (ACR) data from smart TVs to the definition of sensitive data under Kentucky's consumer data privacy law — passed the legislature and was delivered to the governor. Maine's consumer data privacy bill stalled in the House on a procedural vote. A New York Senate Committee advanced the Stop Online Predators Act. Legislatures in Georgia and South Dakota closed without passing comprehensive privacy bills, while Alabama, Kansas, Kentucky, Maine, Nebraska, and Tennessee face imminent end-of-session deadlines.
- **Notes:** _(add notes here)_

---

### 2. [SCAN-20260413-004] Proposed State AI Law Update: April 13, 2026 — Nebraska Chatbot Bill, Maryland Pricing Bill Passed
- [ ] Approve
- **Source:** Troutman Pepper Locke / Privacy + Cyber + AI
- **URL:** https://www.troutmanprivacy.com/2026/04/proposed-state-ai-law-update-april-13-2026/
- **Category:** ai-law
- **Relevance:** high
- **Jurisdiction:** Federal
- **Type:** legislation
- **Summary:** The April 13, 2026 weekly state AI law update reports that Nebraska's unicameral legislature passed LB 525, which includes the Conversational AI Safety Act, requiring AI chatbot services to disclose to users (particularly minors) that they are interacting with AI and prohibiting AI services from representing they can provide professional mental health care. Maryland's legislature passed HB 895 (the Protection From Predatory Pricing Act), prohibiting food retailers and third-party delivery services from using consumer personal data for dynamic pricing, effective October 1, 2026. Maine passed a bill prohibiting AI from offering therapy or psychotherapy services unless provided by a licensed professional.
- **Notes:** _(add notes here)_

---

### 3. [SCAN-20260413-010] FTC COPPA Rule Amendments Take Effect April 22, 2026 — Enforcement Begins on Expanded Biometric and Government ID Provisions
- [ ] Approve
- **Source:** Federal Trade Commission / Taft Privacy & Data Security Insights
- **URL:** https://www.privacyanddatasecurityinsight.com/2026/04/enforcement-begins-soon-for-significant-coppa-rule-amendments/
- **Category:** privacy
- **Relevance:** high
- **Jurisdiction:** Federal
- **Type:** regulation
- **Summary:** The FTC will begin enforcing significant amendments to the Children's Online Privacy Protection Rule (COPPA Rule) on April 22, 2026, one year after the finalized amendments were published in the Federal Register on April 22, 2025. The updated COPPA Rule expands the definition of 'personal information' to include biometric identifiers (fingerprints, retina patterns, facial templates, voiceprints), government-issued identifiers (state ID card numbers, birth certificate numbers, passport numbers), and other new categories. FTC Chairman Andrew Ferguson has publicly committed to aggressive COPPA enforcement as a priority. Civil penalties for violations can exceed $50,000 per violation.
- **Notes:** _(add notes here)_

---

### 4. [SCAN-20260413-012] NIST Releases AI RMF Profile Concept Note on Trustworthy AI in Critical Infrastructure
- [ ] Approve
- **Source:** NIST
- **URL:** https://www.nist.gov/programs-projects/concept-note-ai-rmf-profile-trustworthy-ai-critical-infrastructure
- **Category:** ai-law
- **Relevance:** medium
- **Jurisdiction:** Federal
- **Type:** guidance
- **Summary:** On April 7, 2026, NIST released a concept note for an AI Risk Management Framework (AI RMF) Profile focused on Trustworthy AI in Critical Infrastructure. The profile is intended to guide critical infrastructure operators toward specific risk management practices when deploying AI-enabled capabilities. This follows NIST's broader AI RMF initiative and the February 2026 launch of the AI Agent Standards Initiative by NIST's Center for AI Standards and Innovation (CAISI), which addresses autonomous AI agents. The concept note is part of an ongoing effort to develop sector-specific AI governance profiles.
- **Notes:** _(add notes here)_

---

### 5. [SCAN-20260413-014] Indiana, Kentucky, and Rhode Island Comprehensive Privacy Laws Take Effect January 1, 2026
- [ ] Approve
- **Source:** Koley Jessen / MultiState
- **URL:** https://www.koleyjessen.com/insights/publications/new-state-privacy-laws-effective-january-1-2026-indiana-kentucky-and-rhode-island
- **Category:** privacy
- **Relevance:** high
- **Jurisdiction:** Federal
- **Type:** legislation
- **Summary:** Comprehensive consumer data privacy laws in Indiana (IN SB 5), Kentucky (KY HB 15), and Rhode Island (RI HB 7787/SB 2500) took effect January 1, 2026. All three laws largely follow the Virginia CDPA template. Rhode Island's law has notably low applicability thresholds, covering entities processing data of at least 35,000 consumers or 10,000 consumers when more than 20% of revenue derives from personal data sales. These new laws bring the total number of states with active comprehensive privacy laws to approximately 20, covering more than half the U.S. population.
- **Notes:** _(add notes here)_

---

### 6. [SCAN-20260413-015] California CPPA Imposes $1.35 Million Fine Against Tractor Supply Co. for CCPA Violations
- [ ] Approve
- **Source:** California Privacy Protection Agency
- **URL:** https://cppa.ca.gov/announcements/
- **Category:** privacy
- **Relevance:** high
- **Jurisdiction:** California
- **Type:** enforcement
- **Summary:** The California Privacy Protection Agency imposed a $1.35 million fine against Tractor Supply Company for violations of the California Consumer Privacy Act. The enforcement action is part of a series of CPPA enforcement actions in 2026 targeting businesses failing to implement adequate opt-out mechanisms and privacy notices required under the CCPA. Additional 2026 CPPA enforcement actions include a $632,500 fine against American Honda Motor Co. and a $345,178 fine against Todd Snyder, Inc. California's CPPA and AG are conducting an active enforcement campaign targeting CCPA compliance failures.
- **Notes:** _(add notes here)_

---

<!-- Review each finding above. Check the box to approve. -->
<!-- Edit titles, relevance, or add notes as needed (D-13). -->
<!-- When review is complete, add the marker below: -->

<!-- ## APPROVED -->
