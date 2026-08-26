---
title: "SDNY Denies Coinbase Motion to Dismiss, Clearing Path for SEC Crypto Enforcement Action"
date: 2024-03-27
jurisdiction: "Federal"
category: "cybersecurity"
development_type: "court-decision"
finding_id: "SCAN-20240422-005"
topic_key: "new-york-6df18223-2024"
topic_type: "enforcement"
first_reported: 2024-04-22
last_updated: 2024-04-22
status_history: []
cluster: "SEC v. Coinbase: Crypto Asset Securities Enforcement"
cluster_slug: "sec-crypto-enforcement-coinbase"
---

# SDNY Denies Coinbase Motion to Dismiss, Clearing Path for SEC Crypto Enforcement Action

**Jurisdiction:** Federal (S.D.N.Y.) | **Category:** Cybersecurity / Securities Enforcement | **Date:** March 27, 2024

> **Note on Categorization:** This finding was originally tagged as "privacy" in the pipeline. The subject matter — SEC securities enforcement against a cryptocurrency exchange — falls outside privacy law. It is categorized here under "cybersecurity" as the closest available project category; the development is primarily a federal securities enforcement action.

## Executive Summary [HIGH confidence]

On March 27, 2024, [Judge Katherine Polk Failla](https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1:2023cv04738/599908/105/) of the U.S. District Court for the Southern District of New York (S.D.N.Y.) denied Coinbase's motion for judgment on the pleadings in *SEC v. Coinbase, Inc.*, No. 1:23-cv-04738. The ruling held that the SEC had adequately pleaded that Coinbase operates as an unregistered national securities exchange, broker, and clearing agency, and that transactions in 13 named crypto tokens and Coinbase's Staking Program constitute investment contracts under the *Howey* test. The court dismissed only the SEC's claims regarding Coinbase's self-custodial Wallet application. The decision reinforced the SEC's authority to regulate secondary crypto asset trading without requiring contractual privity between token issuers and secondary buyers — a significant doctrinal expansion. The litigation was subsequently resolved by voluntary dismissal with prejudice in February 2025, after the SEC's new leadership under the Trump administration abandoned the enforcement action in favor of rulemaking through its Crypto Task Force.

## Background [HIGH confidence]

The SEC filed its complaint against Coinbase, Inc. and Coinbase Global, Inc. in the S.D.N.Y. on June 6, 2023, following a Wells Notice issued in March 2023. The [SEC's press release](https://www.sec.gov/newsroom/press-releases/2023-102) describes the charges as alleging that Coinbase had "since at least 2019" made "billions of dollars unlawfully facilitating the buying and selling of crypto asset securities." The 101-page complaint asserted three core violations:

1. **Unregistered National Securities Exchange** — Coinbase provided a marketplace for trading crypto asset securities without registering as a national securities exchange under Section 5 of the Securities Exchange Act of 1934.
2. **Unregistered Broker** — Coinbase acted as a broker by soliciting and executing transactions in crypto asset securities without registering under Section 15(a) of the Exchange Act.
3. **Unregistered Clearing Agency** — Coinbase provided facilities for comparison and settlement of crypto asset securities transactions without registering as a clearing agency under Section 17A of the Exchange Act.
4. **Unregistered Offer and Sale of Securities** — Coinbase's Staking Program, through which it pooled customers' crypto assets for blockchain transaction validation and distributed rewards, constituted the unregistered offer and sale of securities under Sections 5(a) and 5(c) of the Securities Act of 1933.

The SEC sought injunctive relief, disgorgement of ill-gotten gains plus prejudgment interest, civil penalties, and other equitable relief. Coinbase responded to the complaint in July 2023, denying the allegations and requesting dismissal with prejudice. The case proceeded to briefing on Coinbase's motion for judgment on the pleadings, with oral argument held in January 2024.

The *SEC v. Coinbase* litigation arose in tandem with the SEC's companion action against [Binance](https://www.debevoisefintechblog.com/2023/07/21/sec-v-binance-holdings-limited-et-al-and-sec-v-coinbase-inc/), also filed in June 2023, signaling a coordinated enforcement surge against major centralized crypto exchanges under then-Chair Gary Gensler's leadership. The SEC's enforcement theory rested principally on the argument that existing securities laws — specifically the *Howey* test for "investment contracts" — were broad enough to encompass most crypto tokens traded on secondary markets, without the need for congressional action.

## Detailed Analysis [HIGH confidence]

### The Howey Test and Secondary Market Transactions

The central doctrinal issue was whether crypto asset transactions on secondary markets — where no direct relationship exists between the token issuer and the purchaser — could satisfy the *Howey* investment contract test. Coinbase argued that the absence of a contractual relationship between the issuer and the secondary buyer precluded a finding of an "investment contract" because buyers cannot rely on the "efforts of others" in any legally cognizable sense once tokens trade freely on open markets.

Judge Failla rejected this argument. Per [Mintz's analysis](https://www.mintz.com/insights-center/viewpoints/2024-04-18-secs-enforcement-authority-over-crypto-asset-transactions), she held that "there need not be a formal contract between transacting parties for an investment contract to exist under *Howey*." The SEC adequately pleaded that purchasers in the secondary market still held a reasonable expectation of profits derived from the continued efforts of token issuers, developers, and ecosystem participants, regardless of whether those purchasers dealt directly with the issuer.

### The "Ecosystem" Theory of Common Enterprise

The court adopted an ecosystem-focused analytical approach to satisfy the "common enterprise" prong of *Howey*. Judge Failla distinguished crypto tokens from commodities or collectibles, writing that "a crypto-asset is necessarily intermingled with its digital network — a network without which no token can exist." Because token issuers and developers "frequently represented that proceeds from crypto-asset sales would be pooled to further develop the tokens' ecosystems" and "promised that these improvements would benefit all token holders by increasing the value of the tokens themselves," the court found that secondary buyers and token issuers share a sufficiently interlinked financial stake to constitute a common enterprise. This [ecosystem theory](https://www.akingump.com/en/insights/alerts/coinbase-court-embraces-ecosystem-approach-to-identifying-crypto-asset-securities) is analytically distinct from the "horizontal commonality" and "vertical commonality" tests previously applied by courts.

### The 13 Named Tokens

The 13 crypto assets at issue — SOL, ADA, MATIC, FIL, SAND, AXS, CHZ, FLOW, ICP, NEAR, VGX, DASH, and NEXO — were found to be sufficiently pleaded as investment contracts under *Howey*. The ruling did not hold that any of these tokens definitively *are* securities; it held only that the SEC's complaint plausibly alleged facts sufficient to survive a motion to dismiss. The question of whether these specific tokens are securities in fact remained open for discovery and trial.

### The Staking Program

Judge Failla also declined to dismiss the SEC's staking claims. Coinbase argued that customers' deposits of digital assets into its Staking Program do not satisfy the "investment of money" prong of *Howey* because customers retain ownership of their tokens. The court rejected this, finding that customers effectively transfer economic control over their assets to Coinbase to pool and deploy for staking operations, satisfying the investment-of-money requirement. The staking program analysis drew on the SEC's earlier action against [Kraken's staking program](https://fortune.com/crypto/2024/03/03/sec-coinbase-insider-trading-kraken-howey-binance-ripple-terra/) (settled in February 2023 for $30 million), which the court treated as persuasive precedent.

### The Major Questions Doctrine — Rejected

Coinbase invoked the Major Questions Doctrine, arguing that the SEC's assertion of regulatory authority over crypto — an industry of "vast economic and political significance" — required clear congressional authorization beyond the existing Exchange Act framework. The court rejected this argument. Per [Norton Rose Fulbright's analysis](https://www.nortonrosefulbright.com/en/knowledge/publications/9da04ce0/secs-crypto-enforcement-authority-sustained-over-coinbases-vigorous-challenges), the court found that the SEC was "exercising its Congressionally bestowed enforcement authority to regulate virtually any instrument that might be sold as an investment" and was asserting "neither a transformative expansion in its regulatory authority, nor a highly consequential power beyond what Congress could reasonably be understood to have granted it." The court further held that the crypto industry "falls far short of being a portion of the American economy bearing vast economic and political significance" as required to trigger Major Questions analysis under *West Virginia v. EPA* (2022).

### The Wallet Dismissal — Coinbase's Partial Win

The only claim dismissed was the SEC's allegation that Coinbase acted as an unregistered broker by making its self-custodial Wallet application available to customers. The court found that the Wallet — which allows users to hold and transfer their own crypto assets without Coinbase acting as intermediary in the transaction — did not satisfy the definition of "broker" under the Exchange Act. This partial win for Coinbase was limited; the core exchange, broker, clearing agency, and staking claims all survived.

## Litigation Trajectory [HIGH confidence]

Following the March 27, 2024 ruling, the litigation proceeded through 2024 with ongoing discovery. On January 7, 2025, Judge Failla granted Coinbase's motion for an [interlocutory appeal](https://skrypto.sewkis.com/sec-v-coinbase-on-to-the-second-circuit-we-go), certifying a controlling question of law to the U.S. Court of Appeals for the Second Circuit: whether secondary market crypto transactions can constitute "investment contracts" under *Howey*. Certification of an interlocutory appeal is rare and was itself treated as a signal that substantial grounds for disagreement existed among the courts.

The Second Circuit appeal never reached a substantive ruling. On February 27, 2025, the [SEC announced](https://www.sec.gov/newsroom/press-releases/2025-47) that it had filed a joint stipulation with Coinbase to dismiss the enforcement action with prejudice. The dismissal followed the formation of the SEC's Crypto Task Force — led by Commissioner Hester Peirce and announced by Acting Chairman Mark T. Uyeda in January 2025 — which was charged with developing a comprehensive, rulemaking-based regulatory framework for crypto assets. Acting Chairman Uyeda characterized the Gensler-era enforcement strategy as "regulation by enforcement" and stated the need for a more transparent policy process.

The dismissal with prejudice means the SEC cannot refile the same claims against Coinbase. However, it does not resolve the underlying legal questions; no appellate court has ruled on whether secondary market crypto transactions constitute investment contracts under *Howey*.

## Impact Assessment [MEDIUM confidence]

### For Cryptocurrency Exchanges

The March 2024 ruling, while ultimately mooted by the 2025 dismissal, established an influential doctrinal framework. The ecosystem theory of common enterprise and the rejection of the privity requirement represent the most developed judicial analysis to date of how *Howey* applies to secondary crypto markets. These holdings may be cited by plaintiffs and regulators in future enforcement actions or private litigation, even absent binding appellate authority.

The [dismissal of the Wallet claims](https://natlawreview.com/article/secs-enforcement-authority-over-crypto-asset-transactions-upheld-again-case-against) provides some comfort to operators of non-custodial wallet services, suggesting that providing the infrastructure for users to manage their own assets — without acting as a trading intermediary — does not constitute broker activity under existing securities law.

### For Crypto Regulation Broadly

The February 2025 dismissal is part of a broad policy reversal. The SEC also moved to stay or dismiss enforcement actions against Binance, Ripple, and other industry participants in early 2025, consistent with the [new administration's pro-industry stance](https://www.manatt.com/insights/newsletters/client-alert/sec-strategy-shift-coinbase-case-collapse-binance-stay-mark-crypto-regulatory-turning-point). Pending Congressional action — including potential passage of the FIT21 Act or a successor digital asset market structure bill — the legal status of most crypto tokens remains unresolved at the federal level.

### The Howey Question Remains Open

No federal circuit court has ruled on whether secondary market crypto transactions satisfy *Howey*. The Second Circuit's interlocutory review was mooted by the 2025 dismissal. This means that the doctrinal questions Judge Failla resolved at the district court level have no binding appellate authority, leaving the issue open for future litigation.

## Action Items

- Crypto exchanges and trading platforms should continue monitoring Congressional activity on digital asset market structure legislation (FIT21 Act and successors), which may resolve the securities/commodity classification question legislatively.
- Non-custodial wallet operators may draw limited comfort from the Wallet dismissal, but should not treat it as a blanket safe harbor given its district court status and absence of appellate review.
- Legal and compliance teams at crypto firms should track the SEC Crypto Task Force's rulemaking activity, including any forthcoming guidance on token classification, registration exemptions, or safe harbors.
- Firms relying on the SEC's 2025 enforcement retreat should note that the underlying legal questions are unresolved and remain subject to re-litigation by a future administration or by state securities regulators.
- Monitor the Second Circuit and other federal circuits for any future cases presenting the secondary-market *Howey* question, which will provide the binding appellate guidance that *SEC v. Coinbase* did not ultimately produce.

## Related Reports

No related reports found in the knowledge base matching the SEC crypto enforcement subject matter. The existing cybersecurity enforcement reports in this knowledge base address different regulatory bodies (CCPA enforcement, CIRCIA) and are not thematically connected to federal securities enforcement against crypto exchanges.

## Sources

1. [SEC Press Release: SEC Charges Coinbase (June 2023)](https://www.sec.gov/newsroom/press-releases/2023-102) — Official SEC announcement of the original enforcement action, charges, and relief sought.
2. [Justia: S.D.N.Y. Document 105 — March 27, 2024 Order](https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1:2023cv04738/599908/105/) — Official docket entry for Judge Failla's ruling denying Coinbase's motion for judgment on the pleadings.
3. [Latham & Watkins / Fintech & Digital Assets Blog: Ruling for SEC Clears Path for Continued Litigation](https://www.fintechanddigitalassets.com/2024/04/ruling-for-sec-clears-path-for-continued-litigation-in-sec-v-coinbase/) — Primary source law firm analysis from Latham & Watkins summarizing the ruling.
4. [Mintz: SEC's Enforcement Authority Over Crypto Asset Transactions Upheld](https://www.mintz.com/insights-center/viewpoints/2024-04-18-secs-enforcement-authority-over-crypto-asset-transactions) — Law firm analysis of the *Howey* test application and ecosystem theory.
5. [Norton Rose Fulbright: SEC's Crypto Enforcement Authority Sustained](https://www.nortonrosefulbright.com/en/knowledge/publications/9da04ce0/secs-crypto-enforcement-authority-sustained-over-coinbases-vigorous-challenges) — Analysis of Major Questions Doctrine rejection and exchange/broker/clearing agency holdings.
6. [Akin Gump: Coinbase Court Embraces 'Ecosystem' Approach](https://www.akingump.com/en/insights/alerts/coinbase-court-embraces-ecosystem-approach-to-identifying-crypto-asset-securities) — Detailed analysis of the ecosystem theory of common enterprise.
7. [National Law Review: SEC's Enforcement Authority Over Crypto Upheld](https://natlawreview.com/article/secs-enforcement-authority-over-crypto-asset-transactions-upheld-again-case-against) — Overview of the ruling including Wallet dismissal details.
8. [Sewkis Skrypto Blog: SEC v. Coinbase — "On to the Second Circuit We Go"](https://skrypto.sewkis.com/sec-v-coinbase-on-to-the-second-circuit-we-go) — Analysis of the January 2025 interlocutory appeal certification.
9. [SEC Press Release: Dismissal of Civil Enforcement Action Against Coinbase (Feb. 27, 2025)](https://www.sec.gov/newsroom/press-releases/2025-47) — Official SEC announcement of the 2025 voluntary dismissal with prejudice.
10. [Manatt: SEC Strategy Shift — Coinbase Case Collapse](https://www.manatt.com/insights/newsletters/client-alert/sec-strategy-shift-coinbase-case-collapse-binance-stay-mark-crypto-regulatory-turning-point) — Analysis of the 2025 enforcement retreat and Crypto Task Force context.
11. [Debevoise FinReg Blog: SEC's Offensive Against Binance and Coinbase](https://www.debevoisefintechblog.com/2023/07/21/sec-v-binance-holdings-limited-et-al-and-sec-v-coinbase-inc/) — Background on the parallel enforcement actions against Coinbase and Binance.
12. [CourtListener: SEC v. Coinbase Docket](https://www.courtlistener.com/docket/67478179/securities-and-exchange-commission-v-coinbase-inc/) — Full case docket for reference.
