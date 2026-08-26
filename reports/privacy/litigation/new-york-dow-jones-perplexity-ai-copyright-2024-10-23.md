---
title: "Dow Jones and New York Post Sue Perplexity AI for Copyright Infringement and Trademark Dilution Over AI-Powered Search"
date: 2024-10-23
jurisdiction: "New York"
category: "privacy"
development_type: "litigation"
finding_id: "SCAN-20241023-001"
topic_key: "new-york-c7667fc3-2024"
topic_type: "enforcement_action"
topic_key_confidence: "low"
first_reported: 2024-10-23
last_updated: 2026-04-16
status_history:
  - "2026-04-16: Revised per reviewer feedback — corrected all four discovery/trial dates; added April 2026 user-activity log order; added Second Amended Complaint (Jan 28, 2025); added DMCA dismissal; added open-access RAG citation; added inline citation for NYT v. Perplexity."
  - "2026-04-16: Round 2 revision — removed unverified DMCA dismissal claim from Hot News Misappropriation section and Amended Complaints/Jurisdictional Ruling section; Document 65 (Aug 21, 2025) addressed only jurisdiction and venue, not DMCA claims."
cluster: "News Publisher AI Copyright Litigation (RAG and Scraping Claims)"
cluster_slug: "news-publisher-ai-copyright-litigation"
---

# Dow Jones and New York Post Sue Perplexity AI for Copyright Infringement and Trademark Dilution Over AI-Powered Search

**Jurisdiction:** New York (S.D.N.Y.) | **Category:** Privacy / AI Law / Copyright | **Date:** October 23, 2024

## Executive Summary [HIGH confidence]

On October 21, 2024, Dow Jones & Company, Inc. (publisher of The Wall Street Journal) and NYP Holdings, Inc. (publisher of the New York Post) filed suit against Perplexity AI, Inc. in the U.S. District Court for the Southern District of New York, case number [1:24-cv-07984](https://www.courtlistener.com/docket/69280523/dow-jones-company-inc-v-perplexity-ai-inc/). The complaint alleges "massive" copyright infringement, trademark dilution, and false designation of origin arising from Perplexity's AI-powered "answer engine," which the plaintiffs allege scrapes and reproduces their copyrighted articles without authorization. The case is notable as the first major copyright lawsuit targeting retrieval-augmented generation (RAG) technology — a distinct AI architecture that differs from the large language model training disputes already pending against OpenAI and Google. As of April 2026, the case is in active discovery, with document and fact discovery due May 18, 2026, before Judge Katherine Polk Failla.

## Background [HIGH confidence]

The lawsuit arrives amid a broader wave of publisher litigation against AI companies. Perplexity AI is a San Francisco-based generative AI company that operates an "answer engine" — a search product that synthesizes information from multiple web sources into a single conversational response rather than returning a list of links. Unlike traditional search engines, Perplexity explicitly encourages users to "Skip the Links," directly summarizing content from news websites.

News Corp's subsidiaries sent a notice letter to Perplexity in July 2024, identifying the unauthorized use of copyrighted works and offering to negotiate a licensing arrangement. According to the complaint, [Perplexity did not respond](https://www.cnbc.com/2024/10/21/murdoch-firms-dow-jones-and-new-york-post-sue-perplexity-ai.html). This pre-suit conduct is procedurally significant: under established copyright practice, it establishes actual notice and supports a claim of willful infringement, which can trigger enhanced statutory damages under 17 U.S.C. § 504(c)(2).

The litigation joins a broader field of publisher claims against Perplexity. [Multiple publishers have filed suit](https://www.contentgrip.com/publishers-sue-perplexity-ai/), including Encyclopedia Britannica, Merriam-Webster, Nikkei, and Reddit. [The New York Times filed its own separate suit against Perplexity on December 5, 2025](https://www.cnbc.com/2025/12/05/the-new-york-times-perplexity-copyright.html), alleging the same core scraping and verbatim reproduction theories. [Bloomberg Law has characterized these suits as striking at an existential threat to the news industry](https://news.bloomberglaw.com/ip-law/news-outlets-perplexity-ai-suits-strike-at-existential-threat), as AI search engines send roughly 96% less referral traffic to news sites compared with conventional search engines.

## Detailed Analysis [HIGH confidence]

### The RAG Technology at Issue

The lawsuit's most legally significant feature is its focus on retrieval-augmented generation (RAG) technology rather than model training data. Prior AI copyright lawsuits (e.g., The New York Times v. OpenAI) center on whether copyrighted text was used to train the underlying large language model. This case is structured differently.

[Perplexity's answer engine uses a RAG index](https://www.loeb.com/en/insights/publications/2025/08/dow-jones-and-company-inc-v-perplexity-ai-inc): a database of external content — including full or partial reproductions of news articles — that is queried at inference time to supplement the language model's response with up-to-date information. The plaintiffs allege Perplexity copies their articles into this RAG index without permission. The copying occurs at two stages: (1) input — when Perplexity scrapes and stores articles to build its RAG database; and (2) output — when Perplexity's answer engine surfaces "full or partial verbatim reproductions" of the plaintiffs' articles in responses to user queries.

Legal commentators, including [analysis published by LeetSai](https://www.leetsai.com/u-s-first-copyright-lawsuit-against-rag-based-ai-service-news-giants-sue-perplexity) and the [Lexology analysis by Tilleke & Gibbins](https://www.lexology.com/library/detail.aspx?g=b00618c5-4541-4830-a738-1ff9fc2a994d), have identified this as the first copyright action in the United States specifically targeting the RAG retrieval and reproduction pipeline rather than model training.

### Copyright Infringement Claims

The complaint asserts two counts of copyright infringement under the Copyright Act, 17 U.S.C. § 101 et seq.:

- **Count 1 (Input copying):** Perplexity's automated crawlers systematically copy plaintiffs' copyrighted articles to populate its RAG index without authorization, license, or compensation.
- **Count 2 (Output reproduction):** Perplexity's answer engine produces responses that contain full or partial verbatim reproductions of plaintiffs' articles, depriving users of any reason to visit the source websites.

[Cloudflare's independent investigation](https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/) corroborated the scraping allegations, finding that Perplexity used undeclared crawlers — including a stealth crawler impersonating a generic Chrome browser on macOS — to access content even after publishers disallowed PerplexityBot in their robots.txt files. This evasion evidence strengthens the willfulness argument.

### Trademark and Lanham Act Claims

The complaint includes a Lanham Act count for false designation of origin and trademark dilution, 15 U.S.C. §§ 1125(a), (c). The theory is that Perplexity's outputs sometimes attribute fabricated statements to the Wall Street Journal or New York Post — so-called "hallucinations" — which falsely implies those publications are the source of content they never wrote. The plaintiffs argue this misuse of their marks dilutes the reputation of trusted news brands and exposes them to liability for false information they did not create.

### "Hot News" Misappropriation

The original complaint invoked the doctrine of "hot news" misappropriation, drawing on [International News Service v. Associated Press, 248 U.S. 215 (1918)](https://supreme.justia.com/cases/federal/us/248/215/). Under this doctrine, a party that invests in gathering timely information may have a quasi-property right preventing a competitor from free-riding on that investment. However, in the amended proceedings, [the court dismissed the hot news misappropriation claim](https://natlawreview.com/article/generative-ai-meets-generative-litigation-news-corp-continues-its-battle-against), finding the plaintiffs failed to plausibly allege the elements necessary to escape Copyright Act preemption under 17 U.S.C. § 301 for the common law unfair competition by misappropriation theory.

### Amended Complaints and Jurisdictional Ruling

On December 11, 2024, [plaintiffs filed a First Amended Complaint](https://www.afslaw.com/perspectives/ai-law-blog/generative-ai-meets-generative-litigation-news-corp-continues-its-battle) adding seven appendices and expanding the registered works at issue. On January 28, 2025, plaintiffs filed a [Second Amended Complaint (SAC)](https://chatgptiseatingtheworld.com/2025/01/31/dow-jones-files-second-amended-complaint-v-perplexity-ai/), which became the operative pleading. Perplexity moved to dismiss the SAC for lack of personal jurisdiction and, alternatively, to transfer venue to the Northern District of California. The court's August 21, 2025 ruling addressed the Second Amended Complaint.

On August 21, 2025, the court [denied Perplexity's motion in full](https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1:2024cv07984/630270/65/). Judge Failla held that Perplexity has sufficient contacts with New York — including corporate officers and engineers physically present in the state — to satisfy both state long-arm jurisdiction and federal due process requirements. The court also declined to transfer venue, rejecting Perplexity's convenience arguments. Separately, the court declined to dismiss copyright claims for 10 newly registered works added in the amended pleadings, finding the amendment was timely. The core copyright infringement and Lanham Act claims proceed to discovery.

### Perplexity's Defense

Perplexity has advanced several defenses. The company has argued that its conduct constitutes fair use under 17 U.S.C. § 107, characterizing AI synthesis as transformative. Perplexity has also alleged that the plaintiffs engaged in [deliberate "entrapment" — making targeted queries designed to elicit verbatim reproductions](https://pressgazette.co.uk/media_law/perplexity-claims-news-corp-tried-to-entrap-chatbot-to-make-copyright-case/) rather than engaging with the product in an ordinary manner. Perplexity sought discovery into the pre-suit queries the plaintiffs made to build their evidentiary record.

## Impact Assessment [HIGH confidence]

### First-Mover Legal Significance of the RAG Theory

This case will likely produce the first judicial ruling on whether RAG-based retrieval and reproduction of copyrighted text at inference time constitutes fair use. That analysis differs meaningfully from model-training cases. Training cases turn on whether ingestion of text to build statistical weights is transformative; RAG cases involve near-real-time copying and verbatim reproduction at the output layer — a much harder fair use argument for Perplexity to sustain.

### Industry-Wide Implications for AI Search Products

Every AI company operating an answer engine, AI-powered search, or RAG-based product that incorporates current news or web content faces potential liability under this theory. Products potentially affected include Microsoft Copilot (Bing integration), Google's AI Overviews, You.com, and similar services. The remedial stakes are high: statutory damages for willful copyright infringement can reach $150,000 per registered work, and the plaintiffs have registered many works in their appendices.

### Licensing Negotiations as Precedent

The failed July 2024 pre-suit licensing approach by News Corp reflects the broader industry push to compel licensing deals. If the plaintiffs prevail or obtain a favorable injunction, it would create strong leverage for news publishers in licensing negotiations with all AI search platforms. Conversely, a Perplexity win on fair use would substantially undermine publishers' negotiating position.

### Referral Traffic and Economic Disruption

The economic theory underlying the case is that AI answer engines convert traffic that would otherwise go to source websites, destroying the advertising and subscription revenue models that fund journalism. [A TollBit study](https://news.bloomberglaw.com/ip-law/news-outlets-perplexity-ai-suits-strike-at-existential-threat) found AI search engines deliver approximately 96% less referral traffic than conventional search. At scale, this is a material threat to the business models of every web publisher.

### Discovery and Trial Timeline [HIGH confidence]

As of April 2026, the case is in active discovery. The operative court-ordered schedule is:
- Document and fact discovery: May 18, 2026
- Depositions and fact discovery: July 20, 2026
- Expert discovery: October 19, 2026
- Pretrial conference: September 15, 2026 at 11:00 AM, before Judge Failla, Courtroom 618, 40 Centre Street, New York

In a significant April 7, 2026 development, [a Manhattan federal judge ordered Perplexity to produce seven additional months of internal user-activity logs](https://www.law360.com/articles/2462537), rejecting Perplexity's argument that producing the data would be unduly burdensome. This order suggests the plaintiffs are building a detailed evidentiary record of the scope and frequency of the alleged scraping and reproduction conduct.

No settlement has been reported. The source code protocol stipulation suggests the parties are engaged in substantive technical discovery about Perplexity's crawler and RAG infrastructure.

## Action Items

- **AI search and RAG product operators:** Audit whether your product's retrieval pipeline copies or stores copyrighted news content. If so, assess whether publisher robots.txt directives are being honored by all crawlers, including undeclared or third-party agents.
- **News publishers and content owners:** Evaluate whether your robots.txt configuration and server-side blocking are effective against stealth crawlers. Pre-suit notice letters (as News Corp sent in July 2024) are important to establish willfulness for enhanced damages.
- **Licensing counsel:** Monitor the discovery and summary judgment phases of this case for the court's preliminary views on the fair use defense in RAG contexts — this will be the first significant judicial signal on RAG liability.
- **AI companies relying on fair use:** The RAG-specific theory narrows the scope of potential fair use arguments compared to training data cases. Prepare legal analysis of output-layer reproduction separately from input-layer ingestion.
- **All AI developers:** Track related litigation: the New York Times v. Perplexity case (filed December 5, 2025), Reddit v. Perplexity (filed October 2025), and the broader pattern of copyright suits documented in the [Copyright Alliance's 2025 year-in-review](https://copyrightalliance.org/ai-copyright-lawsuit-developments-2025/).

## Related Reports

- [reports/privacy/litigation/california-x-corp-bright-data-web-scraping-2024-05-09.md](reports/privacy/litigation/california-x-corp-bright-data-web-scraping-2024-05-09.md) -- Addresses the legality of web scraping under contract and tort theories; the Bright Data ruling's permissive stance on scraping public data contrasts with the copyright-specific claims at issue in this case.
- [reports/privacy/childrens-privacy/california-meta-coppa-mdl3047-ruling-2024-10-22.md](reports/privacy/childrens-privacy/california-meta-coppa-mdl3047-ruling-2024-10-22.md) -- Major AI platform litigation in federal court; shares procedural context (S.D.N.Y./N.D. Cal. tech company jurisdiction issues) and illustrates the broader trend of courts permitting complex platform-liability claims to proceed past the motion-to-dismiss stage.

## Sources

1. [Dow Jones & Company, Inc. v. Perplexity AI, Inc., 1:24-cv-07984 — CourtListener Docket](https://www.courtlistener.com/docket/69280523/dow-jones-company-inc-v-perplexity-ai-inc/) -- Official case docket for the S.D.N.Y. action; primary source for case number, filing date, procedural history, and current discovery schedule.
2. [Dow Jones and New York Post Sue AI Startup Perplexity, Alleging 'Massive' Copyright Infringement — Variety](https://variety.com/2024/biz/news/news-corp-dow-jones-ny-post-sue-perplexity-copyright-infringement-1236184900/) -- News coverage of the original complaint; describes core allegations and initial legal theories.
3. [Murdoch's Dow Jones, New York Post Sue Perplexity AI for 'Illegal' Copying of Content — CNBC](https://www.cnbc.com/2024/10/21/murdoch-firms-dow-jones-and-new-york-post-sue-perplexity-ai.html) -- Early coverage including details of the July 2024 pre-suit notice letter and Perplexity's non-response.
4. [Perplexity AI Responds to News Corp's Dow Jones, NY Post Lawsuit — Variety](https://variety.com/2024/digital/news/perplexity-ai-responds-lawsuit-news-corp-dow-jones-1236190651/) -- Covers Perplexity's public response to the complaint and its entrapment defense theory.
5. [Generative AI Meets Generative Litigation: News Corp Continues Its Battle Against Perplexity AI — ArentFox Schiff](https://www.afslaw.com/perspectives/ai-law-blog/generative-ai-meets-generative-litigation-news-corp-continues-its-battle) -- Law firm analysis of the amended complaint and court's ruling on jurisdiction; covers hot news misappropriation dismissal.
6. [Generative AI Meets Generative Litigation: News Corp Continues Its Battle Against Perplexity AI — National Law Review](https://natlawreview.com/article/generative-ai-meets-generative-litigation-news-corp-continues-its-battle-against) -- Detailed legal analysis of copyright infringement and hot news doctrine claims; covers amended complaint and procedural posture.
7. [Dow Jones & Company, Inc. et al v. Perplexity AI, Inc., No. 1:2024cv07984, Document 65 — Justia](https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1:2024cv07984/630270/65/) -- Court opinion denying Perplexity's motion to dismiss for lack of personal jurisdiction and motion to transfer venue (August 21, 2025).
8. [Dow Jones & Company Inc. v. Perplexity AI Inc. — Loeb & Loeb LLP](https://www.loeb.com/en/insights/publications/2025/08/dow-jones-and-company-inc-v-perplexity-ai-inc) -- Law firm case tracker with summary of claims, procedural history, and discovery timeline.
9. [Dow Jones & Company, Inc. v. Perplexity AI, Inc. — BakerHostetler](https://www.bakerlaw.com/dow-jones-company-inc-v-perplexity-ai-inc/) -- Case tracker maintained by BakerHostetler; includes case status updates.
10. [U.S. First Copyright Lawsuit Against RAG-Based AI Service: News Giants Sue Perplexity — Lexology (Tilleke & Gibbins)](https://www.lexology.com/library/detail.aspx?g=b00618c5-4541-4830-a738-1ff9fc2a994d) -- Analysis identifying this as the first copyright action targeting RAG technology specifically.
11. [U.S. First Copyright Lawsuit Against RAG-Based AI Service: News Giants Sue Perplexity — LeetSai](https://www.leetsai.com/u-s-first-copyright-lawsuit-against-rag-based-ai-service-news-giants-sue-perplexity) -- Open-access secondary analysis corroborating the "first RAG copyright lawsuit" characterization; same underlying firm analysis as Lexology item 10, publicly accessible.
12. [Perplexity is Using Stealth, Undeclared Crawlers to Evade Website No-Crawl Directives — Cloudflare Blog](https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/) -- Technical investigation corroborating the scraping evasion allegations; Cloudflare's independent findings on PerplexityBot conduct.
13. [Perplexity Claims News Corp Tried to 'Entrap' Its AI Chatbot — Press Gazette](https://pressgazette.co.uk/media_law/perplexity-claims-news-corp-tried-to-entrap-chatbot-to-make-copyright-case/) -- Coverage of Perplexity's entrapment defense and its requests for pre-suit query records.
14. [News Outlets' Perplexity AI Suits Strike at Existential Threat — Bloomberg Law](https://news.bloomberglaw.com/ip-law/news-outlets-perplexity-ai-suits-strike-at-existential-threat) -- Industry-level analysis of publisher litigation strategy and TollBit referral traffic study data.
15. [AI Copyright Lawsuit Developments in 2025: A Year in Review — Copyright Alliance](https://copyrightalliance.org/ai-copyright-lawsuit-developments-2025/) -- Overview of the broader AI copyright litigation landscape; tracks all major publisher suits against AI companies.
16. [International News Service v. Associated Press, 248 U.S. 215 (1918) — Justia Supreme Court](https://supreme.justia.com/cases/federal/us/248/215/) -- Original Supreme Court opinion establishing the hot news misappropriation doctrine invoked in the original complaint.
17. [Dow Jones Files Second Amended Complaint v. Perplexity AI — Chat GPT Is Eating the World](https://chatgptiseatingtheworld.com/2025/01/31/dow-jones-files-second-amended-complaint-v-perplexity-ai/) -- Coverage of the January 28, 2025 Second Amended Complaint filing, which became the operative pleading.
18. [Dow Jones Wins Order For More Months Of Perplexity AI Logs — Law360](https://www.law360.com/articles/2462537) -- Reports on the April 7, 2026 court order compelling Perplexity to produce seven additional months of internal user-activity logs.
19. [The New York Times Sues Perplexity, Alleging Copyright Infringement — CNBC](https://www.cnbc.com/2025/12/05/the-new-york-times-perplexity-copyright.html) -- Coverage of the December 5, 2025 NYT complaint against Perplexity in S.D.N.Y.
