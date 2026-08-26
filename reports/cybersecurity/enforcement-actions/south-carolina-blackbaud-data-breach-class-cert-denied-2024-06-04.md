---
title: "In re Blackbaud: South Carolina Federal Court Denies Class Certification in Massive Consumer Data Breach Case"
date: 2024-06-04
jurisdiction: "South Carolina"
category: "cybersecurity"
development_type: "court-decision"
finding_id: "SCAN-20240604-004"
topic_key: "south-carolina-a5aea5e0-2024"
topic_type: "enforcement"
first_reported: 2024-06-04
last_updated: 2026-04-15
status_history: []
cluster: "Blackbaud 2020 Data Breach: MDL Class Action and Regulatory Enforcement"
cluster_slug: "blackbaud-2020-data-breach-litigation"
---

# In re Blackbaud: South Carolina Federal Court Denies Class Certification in Massive Consumer Data Breach Case

**Jurisdiction:** South Carolina (D.S.C.) | **Category:** Cybersecurity | **Date:** May 14, 2024

## Executive Summary [HIGH confidence]

On May 14, 2024, U.S. District Judge Joseph F. Anderson, Jr. of the District of South Carolina denied class certification in [*In re Blackbaud, Inc., Customer Data Breach Litigation*](https://dd80b675424c132b90b3-e48385e382d2e5d17821a5e1d8e4c86b.ssl.cf1.rackcdn.com/external/blackbaud-class-certification-denied-decision-5-14-24.pdf), MDL No. 2972, Case No. 3:20-MN-02972, 2024 WL 2155221 (D.S.C. May 14, 2024). The court found that plaintiffs failed to satisfy the ascertainability requirement of [Federal Rule of Civil Procedure 23](https://www.law.cornell.edu/rules/frcp/rule_23) — they could not demonstrate an administratively feasible method to identify the estimated 1.5 billion putative class members whose data was exposed in Blackbaud's 2020 ransomware attack. The ruling is significant because it is one of the largest data breach MDLs ever to fail at the class certification stage, and it underscores that even cases involving massive, documented breaches can falter when plaintiffs cannot identify their class with precision and reliability. Parallel regulatory action — including a [finalized FTC consent order](https://www.ftc.gov/news-events/news/press-releases/2024/05/ftc-finalizes-order-blackbaud-related-allegations-firms-security-failures-led-data-breach) and a [$49.5 million multistate AG settlement](https://news.delaware.gov/2023/10/12/ag-jennings-announces-49-5-million-blackbaud-data-breach-settlement/) — demonstrates that regulatory enforcement against security failures can succeed even where private class actions collapse.

## Background [HIGH confidence]

### The 2020 Blackbaud Ransomware Breach

[Blackbaud, Inc.](https://www.blackbaud.com) is a South Carolina-headquartered cloud software company serving more than 13,000 nonprofit organizations, educational institutions, healthcare entities, and other social-sector clients. Its platform manages donor records, patient data, alumni databases, and similar sensitive datasets on behalf of those clients.

In early 2020, a hacker exploited weaknesses in Blackbaud's network infrastructure — remaining undetected for approximately three months. The company became aware of suspicious activity on May 14, 2020, but did not notify affected customers until July 16, 2020, weeks after the breach window closed. According to the [FTC's complaint](https://www.ftc.gov/legal-library/browse/cases-proceedings/2023181-blackbaud-inc), the attacker removed massive amounts of unencrypted sensitive consumer data, including Social Security numbers and bank account information. Estimates of affected individuals range as high as 1.5 billion donors, patients, and other data subjects — making this one of the largest B2B data breaches on record.

### MDL Formation and Prior Dismissals

Beginning in January 2021, affected individuals filed putative class action complaints in multiple federal districts. The [Judicial Panel on Multidistrict Litigation](https://www.jpml.uscourts.gov/) centralized the cases in the District of South Carolina as MDL No. 2972. The consolidated action named plaintiffs from more than 20 states alleging that Blackbaud failed to implement reasonable security measures.

Early in the litigation, U.S. District Judge Julia Childs dismissed several consolidated claims — including consumer protection claims brought under New Jersey, Pennsylvania, and South Carolina law — while allowing allegations under the California Consumer Privacy Act (CCPA) and certain negligence theories to proceed. That pruning did not end the litigation; a large set of claims remained for class certification briefing.

### FTC and Multistate Regulatory Enforcement

Concurrent with the MDL, federal and state regulators pursued parallel tracks:

- The **FTC** announced a [proposed consent order](https://www.ftc.gov/news-events/news/press-releases/2024/02/ftc-order-will-require-blackbaud-delete-unnecessary-data-boost-safeguards-settle-charges-its-lax) on February 1, 2024, citing Blackbaud's failures to monitor intrusion attempts, segment networks, implement adequate multifactor authentication, and delete data it no longer needed. The FTC voted 3-0-2 to [finalize the order](https://www.ftc.gov/news-events/news/press-releases/2024/05/ftc-finalizes-order-blackbaud-related-allegations-firms-security-failures-led-data-breach) in May 2024. No monetary penalty was imposed, but Blackbaud must develop a comprehensive information security program and implement a formal data retention schedule.
- **Forty-nine state attorneys general plus the District of Columbia** reached a [$49.5 million settlement](https://news.delaware.gov/2023/10/12/ag-jennings-announces-49-5-million-blackbaud-data-breach-settlement/) with Blackbaud in October 2023 over its breach response and disclosure failures.
- **California** separately secured a [$6.75 million settlement](https://oag.ca.gov/news/press-releases/attorney-general-bonta-secures-675-million-settlement-against-blackbaud-over) from Blackbaud, approved in 2024.
- The **SEC** reached a [$3 million settlement](https://www.sec.gov/newsroom/press-releases/2023-48) with Blackbaud in March 2023 over misleading disclosures about the scope of the breach.

## Detailed Analysis [HIGH confidence]

### The Ascertainability Requirement Under Rule 23

Federal Rule of Civil Procedure 23(a) requires that a putative class be sufficiently definite that it is administratively feasible to determine whether any particular person is a class member — the so-called ascertainability (or "implicit ascertainability") requirement recognized across many circuits, including the Fourth Circuit. In practical terms, plaintiffs must propose a method for identifying class members that is (1) objective, (2) reliable, and (3) administratively manageable.

The challenge in *Blackbaud* was geometric: plaintiffs sought to certify classes and subclasses on behalf of individuals whose personal data was held by one of roughly 13,000 Blackbaud clients, each with different data architectures, record systems, and data-sharing relationships with Blackbaud. The total putative class was estimated at 1.5 billion individuals across multiple states, data types, and client relationships.

### Rejection of Plaintiffs' Four Ascertainability Arguments

Plaintiffs advanced four distinct methods to demonstrate ascertainability; the court rejected each.

**1. Expert Testimony (Matthew Curtin).** Plaintiffs retained Matthew Curtin, a computer scientist and cybersecurity consultant, to propose a methodology for identifying which individuals' data was exposed and which specific data elements were compromised. The court excluded this testimony under [*Daubert v. Merrell Dow Pharmaceuticals, Inc.*, 509 U.S. 579 (1993)](https://www.law.cornell.edu/supct/html/92-102.ZS.html), finding that Curtin's methodology was not replicable, lacked a documented error rate, was not sufficiently tested, and was not documented in a way that permitted Blackbaud's rebuttal expert to evaluate or reproduce it. The court stated Curtin's method was excluded because of his "inability to provide this Court with an error rate and a statement about its occurrence consistent with generally accepted statistical practices," his "failure to sufficiently test his method," and the "non-replicability of his method." Without an admissible expert methodology, the centerpiece of the ascertainability case collapsed.

**2. Blackbaud's Discovery Responses.** Plaintiffs argued that Blackbaud had itself identified specific types of exposed data in response to discovery requests — proof, they contended, that the class could be identified using Blackbaud's own records. The court disagreed, finding that the company's discovery responses "were the result of a manual and time-consuming process that was not designed to be used on a large scale" and therefore did not establish an administratively feasible class-identification mechanism.

**3. Blackbaud's Customer Notification Process.** Plaintiffs pointed to Blackbaud's post-breach notifications to its institutional clients as evidence of an existing identification framework. The court rejected this analogy, holding that notifying 13,000 B2B customers was "not comparable to the steps" required to identify which of billions of end consumers whose data those 13,000 customers maintained were class members — a fundamentally different and far more complex undertaking.

**4. Wirewheel Privacy Management Software.** Plaintiffs argued that Blackbaud used a data management tool called Wirewheel that could be repurposed to trace class membership. The court found this argument unpersuasive; the record did not establish that Wirewheel could accomplish the identification task at the scale and granularity required by Rule 23.

### Declining to Join the Minority View

At the time of the ruling, a minority of federal courts had certified classes in large-scale consumer data breach cases without requiring the stringent ascertainability showing the court applied here. The court expressly declined to join that minority, reaffirming that the plaintiffs in the District of South Carolina must demonstrate an administratively feasible identification method — not merely that the class is theoretically definable.

### Subsequent Denial of Leave to Re-File

Following the May 2024 denial, plaintiffs sought leave to file a second certification motion. A federal judge denied that request in December 2024, ruling that permitting renewed class certification argument based on a substantially unchanged factual record — late in the litigation — would be prejudicial to Blackbaud and contrary to the interests of judicial economy. This double defeat effectively ends the prospect of class-wide relief through the MDL for the estimated 1.5 billion putative class members. Individual plaintiffs retain the ability to pursue their own claims.

## Impact Assessment [MEDIUM confidence]

### Implications for Data Breach Defendants

The *Blackbaud* ruling is among the most significant data breach class certification defeats in recent memory, given the scale of the underlying breach. It offers several concrete takeaways for corporate defendants facing similar actions:

- **Ascertainability is a live defense even in massive MDLs.** Courts will not presume that a large breach produces an identifiable class. The burden remains on plaintiffs to demonstrate a concrete, replicable identification methodology.
- **Expert testimony quality is outcome-determinative.** The exclusion of the plaintiffs' cybersecurity expert under *Daubert* was the pivotal event. Defendants should aggressively challenge expert identification methodologies on reliability, replicability, and error-rate grounds.
- **B2B data architectures create structural class-definition barriers.** When the breached entity holds data indirectly — as a processor for thousands of institutional clients — tracing which consumers' data was exposed through which clients creates layered complexity that is difficult to resolve at the class level.

### Regulatory Enforcement Remains Robust

The private class action defeat does not diminish the regulatory enforcement exposure that Blackbaud faced — or that peer companies face after large breaches. The FTC consent order, multistate AG settlement, and SEC penalty together imposed tens of millions of dollars in liability and binding behavioral remediation. Companies experiencing breaches should not interpret the *Blackbaud* class certification denial as reducing their overall risk profile; regulatory authorities operate under different standards and do not face Rule 23 ascertainability constraints.

### Fourth Circuit Class Action Landscape

The [Ellis & Winters 2024 Fourth Circuit class certification review](https://www.elliswinters.com/classactions/class-certification-review-in-the-fourth-circuit-in-2024-an-encouraging-year-for-class-action-defendants/) characterizes 2024 as "an encouraging year for class action defendants" in the circuit, highlighting heightened scrutiny of ascertainability and standing at the certification stage. The *Blackbaud* denial fits squarely within this trend and may signal that the Fourth Circuit's district courts will continue to apply rigorous standards in consumer data breach MDLs.

### Nonprofit and Healthcare Sector Considerations

Because Blackbaud's client base consists predominantly of nonprofit organizations, universities, and healthcare entities — including those handling HIPAA-covered data — the decision has particular relevance to those sectors. Organizations that use third-party cloud platforms to manage donor, patient, or student data should evaluate whether their vendor agreements and data processing arrangements create exposure in the event of a breach at the vendor level. The *Blackbaud* litigation demonstrates that both regulatory enforcement and private litigation will follow the data upstream to the original data processor.

## Action Items

- Conduct a vendor due diligence review for cloud platforms that process personal data on behalf of your organization; assess whether contracts include adequate breach notification, security standard, and indemnification provisions.
- If your organization was a Blackbaud customer affected by the 2020 breach, assess whether individual claims remain viable given the MDL's class certification failure; consult litigation counsel on applicable statutes of limitations.
- Track potential appeal of the class certification denial if plaintiffs seek Fourth Circuit review; the appellate outcome could reshape ascertainability doctrine in the circuit.
- Review data minimization practices in light of the FTC consent order's emphasis on deleting data no longer needed; the FTC's Blackbaud action signals continued agency focus on data retention as a security and enforcement issue.
- Monitor the *Blackbaud* MDL docket for any residual individual claims and settlement discussions, which may produce additional precedents on damages theories in the absence of class certification.

## Related Reports

- [reports/cybersecurity/enforcement-actions/california-ccpa-cybersecurity-audit-class-litigation-2026-04-14.md](reports/cybersecurity/enforcement-actions/california-ccpa-cybersecurity-audit-class-litigation-2026-04-14.md) — Analyzes how California's mandatory cybersecurity audit rule creates discoverable documentation that may be used in data breach class actions, directly intersecting with the class-certification dynamics seen in *Blackbaud*.
- [reports/cybersecurity/tennessee-hb2434-data-breach-safe-harbor-2024-05-21.md](reports/cybersecurity/tennessee-hb2434-data-breach-safe-harbor-2024-05-21.md) — Tennessee's class action safe harbor for cybersecurity events takes a legislative approach to limiting the same type of data breach class litigation at issue in *Blackbaud*.

## Sources

1. [*In re Blackbaud, Inc., Customer Data Breach Litigation* — Court Opinion (D.S.C. May 14, 2024)](https://dd80b675424c132b90b3-e48385e382d2e5d17821a5e1d8e4c86b.ssl.cf1.rackcdn.com/external/blackbaud-class-certification-denied-decision-5-14-24.pdf) — Full text of the class certification denial opinion authored by Judge Joseph F. Anderson, Jr.
2. [South Carolina Federal Court Denies Class Certification In Massive Data Breach Class Action — Duane Morris Class Action Defense Blog (May 19, 2024)](https://blogs.duanemorris.com/classactiondefense/2024/05/19/south-carolina-federal-court-denies-class-certification-in-massive-data-breach-class-action/) — Detailed legal analysis of the ascertainability ruling and its tactical implications for defendants.
3. [South Carolina Federal Court Denies Class Certification in Consumer Data Breach Case — Inside Class Actions (May 30, 2024)](https://www.insideclassactions.com/2024/05/30/south-carolina-federal-court-denies-class-certification-in-consumer-data-breach-case/) — Independent coverage including analysis of plaintiffs' four rejected ascertainability arguments.
4. [South Carolina Federal Court Denies Class Certification in Massive Data Breach — Lexology / Covington & Burling LLP (June 4, 2024)](https://www.lexology.com/library/detail.aspx?g=503faa6d-06d5-4454-a7f2-0b53ac3c756a) — Law firm client alert summarizing the ruling and defense implications.
5. [FTC Finalizes Order with Blackbaud — FTC Press Release (May 2024)](https://www.ftc.gov/news-events/news/press-releases/2024/05/ftc-finalizes-order-blackbaud-related-allegations-firms-security-failures-led-data-breach) — Official FTC announcement of the finalized consent order against Blackbaud.
6. [FTC Order Proposed — FTC Press Release (February 1, 2024)](https://www.ftc.gov/news-events/news/press-releases/2024/02/ftc-order-will-require-blackbaud-delete-unnecessary-data-boost-safeguards-settle-charges-its-lax) — FTC's proposed settlement terms including data deletion and security program requirements.
7. [Blackbaud, Inc. FTC Case Docket](https://www.ftc.gov/legal-library/browse/cases-proceedings/2023181-blackbaud-inc) — Official FTC docket entry for the Blackbaud matter.
8. [AG Jennings Announces $49.5 Million Blackbaud Data Breach Settlement — Delaware AG Office (October 12, 2023)](https://news.delaware.gov/2023/10/12/ag-jennings-announces-49-5-million-blackbaud-data-breach-settlement/) — Multistate AG settlement announcement confirming 49 states plus DC participation.
9. [Attorney General Bonta Secures $6.75 Million Settlement Against Blackbaud — California DOJ (2024)](https://oag.ca.gov/news/press-releases/attorney-general-bonta-secures-675-million-settlement-against-blackbaud-over) — California's separate settlement with Blackbaud.
10. [Judge Denies Class Certification in Blackbaud Lawsuit — HIPAA Journal](https://www.hipaajournal.com/class-certification-denied-blackbaud-lawsuit/) — Analysis of the ruling with healthcare-sector focus.
11. [Class Action Denied in Blackbaud Data Breach Case — The NonProfit Times](https://thenonprofittimes.com/npt_articles/class-action-denied-in-blackbaud-data-breach-case/) — Nonprofit-sector perspective on the ruling's implications.
12. [Blackbaud Again Defeats Class Certification in Data Breach Suit — Bloomberg Law (December 2024)](https://news.bloomberglaw.com/privacy-and-data-security/blackbaud-again-defeats-class-certification-in-data-breach-suit) — Coverage of the court's December 2024 denial of leave to file a second certification motion.
13. [Class Certification Review in the Fourth Circuit in 2024 — Ellis & Winters LLP](https://www.elliswinters.com/classactions/class-certification-review-in-the-fourth-circuit-in-2024-an-encouraging-year-for-class-action-defendants/) — Annual review characterizing 2024 as favorable for defendants on class certification in the Fourth Circuit.
14. [Federal Rule of Civil Procedure 23 — Cornell LII](https://www.law.cornell.edu/rules/frcp/rule_23) — Official text of the class action rule governing certification requirements including ascertainability.
15. [SEC Press Release 2023-48 — Blackbaud to Pay $3 Million to Settle Charges for Misleading Disclosures About Ransomware Attack (March 9, 2023)](https://www.sec.gov/newsroom/press-releases/2023-48) — Official SEC press release announcing the civil penalty for misleading disclosures about the scope of the 2020 data breach.
