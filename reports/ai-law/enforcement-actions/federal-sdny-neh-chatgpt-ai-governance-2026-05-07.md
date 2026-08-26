---
title: "SDNY Rules DOGE's ChatGPT-Assisted NEH Grant Terminations Unconstitutional: Lessons for Corporate AI Governance"
date: 2026-05-07
jurisdiction: "Federal"
category: "ai-law"
development_type: "court-decision"
finding_id: "SCAN-20260519-048"
topic_key: "federal-8d108957-2026"
topic_type: "enforcement"
topic_key_confidence: "low"
first_reported: 2026-05-13
last_updated: 2026-05-20
status_history:
  - "2026-05-20: Corrected case name from 'v. National Endowment for the Humanities' to 'v. McDonald' (Michael McDonald, NEH Acting Chairman) throughout; updated citation to include docket number No. 1:25-cv-03657; added note that Westlaw citation 2026 WL 1256545 could not be independently verified; updated all formal shorthand references from 'ACLS v. NEH' to 'ACLS v. McDonald'; added CourtListener and Civil Rights Litigation Clearinghouse to Sources."
cluster: "DOGE ChatGPT-Assisted Federal Grant Terminations: AI Decision-Making Litigation"
cluster_slug: "doge-chatgpt-ai-decision-making-litigation"
---

# SDNY Rules DOGE's ChatGPT-Assisted NEH Grant Terminations Unconstitutional: Lessons for Corporate AI Governance

**Jurisdiction:** Federal | **Category:** AI Law | **Date:** May 7, 2026

## Executive Summary [HIGH confidence]

On May 7, 2026, U.S. District Judge Colleen McMahon of the Southern District of New York issued a 143-page opinion in [*American Council of Learned Societies v. McDonald*](https://www.courtlistener.com/docket/70035052/american-council-of-learned-societies-v-mcdonald/), No. 1:25-cv-03657 (S.D.N.Y. May 7, 2026) (Michael McDonald, NEH Acting Chairman), ruling that the mass termination of more than 1,400 federal humanities grants was "unlawful, unconstitutional, ultra vires, and without legal effect." A Westlaw citation of 2026 WL 1256545 appears in secondary commentary but could not be independently verified through available sources at time of writing; practitioners should verify this citation against the official Westlaw entry or the NYSD court's docket before citing it in filings. The terminations were driven by the Department of Government Efficiency's (DOGE) use of OpenAI's ChatGPT to classify grants as DEI-related without human expert review or any defined standard for the AI. The court rejected the government's argument that responsibility for unconstitutional outputs could be deflected onto the AI tool, holding that "ChatGPT was the Government's chosen instrument for purposes of this project" and that the "Government cannot escape liability ... by scapegoating ChatGPT." While the case arose under constitutional doctrine applicable to government actors, legal practitioners and compliance professionals have identified the decision as carrying broad implications for any private organization that embeds generative AI in consequential decision-making processes.

## Background [HIGH confidence]

The National Endowment for the Humanities (NEH) is an independent federal agency created by the [National Foundation on the Arts and the Humanities Act of 1965](https://www.neh.gov/about/history/legislation) to support scholarship, education, and public programs in the humanities. For decades it funded universities, archives, libraries, museums, and individual scholars through a peer-reviewed competitive grant process.

Following the January 2025 presidential executive orders directing agencies to eliminate programs with diversity, equity, and inclusion (DEI) components, DOGE personnel were embedded at the NEH. In April 2025, the NEH carried out the largest mass grant termination in its history, cancelling approximately 1,400 previously awarded grants and withholding more than $100 million in committed funding. The stated basis was that the terminated grants implicated DEI.

Discovery obtained during litigation revealed the mechanism behind the terminations: [DOGE employees fed grant descriptions into ChatGPT](https://www.prnewswire.com/news-releases/discovery-released-in-lawsuit-by-humanities-groups-reveals-chatgpt-powered-process-by-doge-in-cancelling-grants-for-schools-libraries-and-community-organizations-302707495.html) using a single prompt — "Does the following relate at all to DEI? Respond factually in less than 120 characters" — and then entered the chatbot's yes/no responses and brief rationales into a spreadsheet. No subject-matter experts reviewed the AI outputs, no standard definition of "DEI" was provided to the AI, and no human adjudicator confirmed whether the chatbot's reasoning made sense in any individual case. The AI flagged grants containing terms such as "history," "culture," and "identity" as DEI-related.

The plaintiffs — the American Council of Learned Societies (ACLS), the American Historical Association (AHA), and the Modern Language Association (MLA) — filed suit and moved for summary judgment. Judge McMahon granted the motion on all counts.

## Detailed Analysis [HIGH confidence]

### Constitutional Holdings

Judge McMahon's 143-page opinion rested on three distinct grounds:

**First Amendment violation.** The court held that the grant terminations constituted viewpoint discrimination — a per se violation of the First Amendment. The government selected grants for termination based on perceived ideological content, a textbook example of viewpoint-based restriction on speech. The AI-mediated classification process did not cure this constitutional deficiency; it operationalized it. McMahon noted that grants including an anthology titled *In the Shadow of the Holocaust: Short Fiction by Jewish Writers from the Soviet Union* were flagged by ChatGPT as DEI-related — illustrating the unreliability of the AI classification and the lack of meaningful human review.

**Fifth Amendment equal protection violation.** The court found the terminations violated the equal protection component of the Fifth Amendment because grants were targeted based on race, sex, religion, national origin, and other constitutionally sensitive characteristics embedded in the subjects studied. Using AI to aggregate and act upon those characteristics without individualized review did not insulate the government from equal protection scrutiny.

**Ultra vires action.** The terminations were made without statutory authority. The NEH's enabling legislation requires that grants be made and cancelled through specific procedural channels; wholesale cancellation by DOGE personnel embedded at the agency was not authorized by Congress.

### The "Scapegoating the AI" Doctrine

The most consequential holding for AI governance practitioners is the court's rejection of the government's attempt to displace liability onto the AI tool. The government argued that any viewpoint classification was ChatGPT's doing rather than the government's. Judge McMahon rejected this reasoning categorically: ["ChatGPT was the Government's chosen instrument for purposes of this project, and DOGE's use of AI to identify DEI-related material neither excuses presumptively unconstitutional conduct nor gives the Government carte blanche to engage in it."](https://www.feldesman.com/federal-court-orders-reinstatement-of-more-than-1400-neh-grants-terminated-through-ai-assisted-review/)

The court's analysis establishes that the entity that deploys an AI system owns its outputs for legal accountability purposes. Outsourcing a decision to an AI model does not transfer legal responsibility to the model's developer or to the model itself.

### Deficiencies in Human Oversight Identified by the Court

The opinion identified several specific oversight failures that contributed to the constitutional violation:

- No defined standard for the AI. ChatGPT was given no definition of "DEI" and produced inconsistent, unreliable classifications.
- No expert review of AI outputs. DOGE employees with no subject-matter expertise in the humanities accepted ChatGPT's outputs without verification.
- No individualized adjudication. Grants were terminated en masse based on the chatbot's binary yes/no responses without any case-by-case human judgment.
- No audit or validation step. The process included no mechanism to catch errors before adverse action was taken.

Sidley Austin's analysis of the decision [summarizes these failures as the absence of "sufficient human involvement, oversight, and validation"](https://www.sidley.com/en/insights/newsupdates/2026/05/when-the-devil-made-me-do-it-is-not-a-defense-lessons-in-ai-governance) in an AI-assisted process that produced consequential, irreversible outcomes.

### Remedies

Judge McMahon ordered the NEH to [reinstate more than 1,400 terminated grants and prohibited the government from reallocating the more than $100 million](https://www.feldesman.com/federal-court-orders-reinstatement-of-more-than-1400-neh-grants-terminated-through-ai-assisted-review/) associated with the terminated grants.

## Impact Assessment [MEDIUM confidence]

### Immediate Impact on Government AI Deployment

Every federal agency using or considering AI tools for consequential decisions received a direct warning from this opinion. The ruling establishes judicial willingness to scrutinize AI-assisted government decision-making under constitutional standards, looking past technological framing to examine the actual impact on individual rights. [Courts are now confronting the question of how much human oversight is legally required when AI helps shape government decisions](https://www.nbcnews.com/politics/doge/judge-rules-trump-administrations-cancellation-humanities-grants-was-u-rcna344162), and *ACLS v. McDonald* provides a concrete answer: substantially more than DOGE provided.

### Implications for Private Sector AI Governance

Although constitutional rights provisions do not bind private actors directly, the court's reasoning about AI accountability carries significant persuasive weight in other legal contexts. [Sidley Austin's client alert](https://www.sidley.com/en/insights/newsupdates/2026/05/when-the-devil-made-me-do-it-is-not-a-defense-lessons-in-ai-governance) observes that "similar issues could arise from a company's use of any large language model (LLM), including internally developed models, or even industry-specific AI systems integrated into operational workflows." Private organizations face parallel exposure under:

- **Employment discrimination law.** Companies using AI to make adverse employment decisions — terminations, performance reviews, hiring — face Title VII and state anti-discrimination law claims if the AI produces disparate impact without adequate human review and oversight.
- **Financial services regulation.** Regulators including the SEC, CFTC, and banking agencies have issued guidance requiring firms to maintain oversight and accountability for algorithmic systems. The *ACLS v. McDonald* reasoning reinforces the principle that firms cannot deflect regulatory responsibility onto AI vendors.
- **Consumer protection and UDAP liability.** State attorneys general have invoked consumer protection statutes against companies whose automated decision systems produce harmful outcomes without adequate safeguards. Courts applying *ACLS v. McDonald*'s reasoning could find that deploying an AI tool without meaningful oversight is itself the organization's actionable conduct.
- **Tort liability.** As AI systems are deployed in higher-stakes domains — financial advice, medical triage, insurance underwriting — tort plaintiffs may draw on *ACLS v. McDonald* to argue that defendants cannot escape negligence liability by attributing adverse outcomes to the AI rather than to the organization's decision to deploy it without adequate governance.

### Regulatory Context: Automated Decision-Making Rules

The court's analysis aligns with emerging regulatory requirements on automated decision-making technology (ADMT). Several state privacy laws that take effect in 2026-2027 require businesses using ADMT for significant decisions to conduct risk assessments, report those assessments to senior management, and provide individuals with notice and opt-out rights. The *ACLS v. McDonald* decision provides courts with a framework for evaluating whether an organization's ADMT governance meets a legally adequate standard of human oversight and validation.

### Note on Scanner Finding Discrepancy

The initial scanner finding described this case as arising from "financial harm caused by an algorithmic trading system." This characterization does not match the verified facts. The case arose from DOGE's use of ChatGPT to classify federal humanities grants at the NEH, not from algorithmic trading. The core governance principle — that organizations cannot shift legal responsibility for AI outputs onto AI systems — is the same, but practitioners should use the correct case context when citing this decision.

## Action Items

- Review all AI-assisted decision-making workflows to identify processes where consequential adverse actions (terminations, denials, classifications) are taken based on AI output without meaningful human review and validation.
- Establish and document the standard or criteria provided to any AI system used in decisions affecting individuals, and ensure those standards are auditable and defensible under applicable legal frameworks.
- Implement individualized human adjudication checkpoints for high-stakes AI outputs, particularly where AI is used to classify, score, or triage individuals in contexts subject to anti-discrimination, consumer protection, or regulatory oversight.
- Brief senior management and boards on the *ACLS v. McDonald* decision and its implications for organizational AI governance programs; document that briefing as part of the governance record.
- Coordinate with outside counsel to assess whether existing ADMT risk assessments and disclosures satisfy requirements under state privacy laws taking effect in 2026-2027.
- Monitor for government appeal of the *ACLS v. McDonald* ruling; the constitutional holdings could be narrowed or affirmed at the circuit level, affecting the decision's precedential weight.

## Related Reports

- [reports/ai-law/federal-regulation/federal-national-policy-framework-ai-preemption-2026-04-14.md](../../federal-regulation/federal-national-policy-framework-ai-preemption-2026-04-14.md) -- White House National Policy Framework for AI, March 2026, which called for federal preemption of state AI laws and shapes the regulatory environment in which *ACLS v. McDonald* was decided.
- [reports/ai-law/enforcement-actions/federal-doj-ai-civil-rights-interagency-2024-10-18.md](federal-doj-ai-civil-rights-interagency-2024-10-18.md) -- DOJ interagency coordination on AI civil rights enforcement, directly relevant to the First and Fifth Amendment theories underlying *ACLS v. McDonald*.
- [reports/ai-law/enforcement-actions/pennsylvania-character-ai-medical-practice-act-2026-05-18.md](pennsylvania-character-ai-medical-practice-act-2026-05-18.md) -- Pennsylvania's novel application of existing professional licensing law to an AI system; parallels the organizational liability theory articulated in *ACLS v. McDonald*.
- [reports/ai-law/federal-regulation/federal-trump-eo-ai-agency-deadlines-missed-2026-04-29.md](../../federal-regulation/federal-trump-eo-ai-agency-deadlines-missed-2026-04-29.md) -- Tracks federal agency compliance with Trump AI executive order mandates, providing context for DOGE's AI deployment within federal agencies.

## Sources

1. [CourtListener: American Council of Learned Societies v. McDonald, 1:25-cv-03657](https://www.courtlistener.com/docket/70035052/american-council-of-learned-societies-v-mcdonald/) -- Official docket confirming correct case name, parties, and case number.
2. [Civil Rights Litigation Clearinghouse: ACLS v. McDonald, 1:25-cv-03657](https://clearinghouse.net/case/46527/) -- Case record confirming correct case name, docket number, and summary of holdings.
3. [NBC News: Judge rules Trump administration's cancellation of humanities grants was unconstitutional](https://www.nbcnews.com/politics/doge/judge-rules-trump-administrations-cancellation-humanities-grants-was-u-rcna344162) -- Primary news coverage of the May 7, 2026 ruling with case holdings and constitutional analysis.
4. [Sidley Austin: When "The Devil Made Me Do It" Is Not a Defense](https://www.sidley.com/en/insights/newsupdates/2026/05/when-the-devil-made-me-do-it-is-not-a-defense-lessons-in-ai-governance) -- Law firm client alert analyzing the AI governance and corporate compliance implications of the decision.
5. [Lexology: Sidley Austin analysis (same article)](https://www.lexology.com/library/detail.aspx?g=fb38c6d8-536b-49fc-a3f1-e21534150b09) -- Lexology repost of the Sidley Austin alert, original source for this finding.
6. [Feldesman LLP: Court Orders Reinstatement of Grants Terminated by AI-Assisted Review](https://www.feldesman.com/federal-court-orders-reinstatement-of-more-than-1400-neh-grants-terminated-through-ai-assisted-review/) -- Government contracts law firm analysis of the court order and reinstatement remedy.
7. [PR Newswire: Discovery reveals ChatGPT-powered process by DOGE](https://www.prnewswire.com/news-releases/discovery-released-in-lawsuit-by-humanities-groups-reveals-chatgpt-powered-process-by-doge-in-cancelling-grants-for-schools-libraries-and-community-organizations-302707495.html) -- Press release disclosing the ChatGPT methodology revealed in discovery.
8. [PBS NewsHour: Judge finds Trump's DOGE-led cancellation of humanities grants unconstitutional](https://www.pbs.org/newshour/politics/judge-finds-trumps-doge-led-cancellation-of-humanities-grants-unconstitutional) -- Independent news coverage corroborating the constitutional holdings.
9. [CNN Politics: DOGE judge cancellation grants unconstitutional](https://www.cnn.com/2026/05/08/politics/doge-judge-cancellation-grants-unconstitutional-hnk) -- Additional news coverage confirming case facts and remedy.
10. [ACLS: Federal Judge Rules to Restore NEH Funding](https://www.acls.org/news/federal-judge-rules-to-restore-national-endowment-of-the-humanities-funding-in-historic-case/) -- Plaintiff organization's official statement confirming outcome.
11. [Inside Higher Ed: Federal Judge Restores Millions in NEH Grants](https://www.insidehighered.com/news/quick-takes/2026/05/07/federal-judge-restores-millions-neh-grants) -- Trade press coverage confirming the date and scope of the ruling.
12. [SVDX Blog: When "The Devil Made Me Do It" Is Not a Defense](https://www.svdx.org/blog/2026/5/13/when-the-devil-made-me-do-it-is-not-a-defense-lessons-in-ai-governance-and-organizational-oversight-from-an-sdny-decision) -- Secondary analysis citing the case citation 2026 WL 1256545; citation could not be independently verified.
