---
type: paper
status: unread
title: 'Mergers, Product Prices, and Innovation: Evidence from the Pharmaceutical Industry'
authors: Alice Bonaimé and Ye (Emma) Wang
year: 2024
journal: Journal of Finance
professor: DrJandik
seminar: null
jandik_paper_number: 40
jandik_week: 10
jandik_topic: 'M&A: sources of synergies'
jandik_done: false
field: Corporate Finance
literature:
- '[[Mergers and Acquisitions]]'
- Product Market Competition
- '[[Innovation]]'
- Market Power
methods:
- Difference-in-differences
- event study
- propensity score matching
- triple differences
datasets:
- NADAC
- '[[SDC Platinum]]'
- FDA Orange Book
- FDA New Drug Approval database
- Medicaid SDUD
- '[[CRSP-Compustat]]'
- WHO ATC codes
identification: Within-deal product-level DID comparing acquirer drugs in consolidating product markets to matched same-acquirer control drugs not directly affected by the merger
main_result: Pharmaceutical mergers raise prices in consolidating drug markets by about 2%, especially where acquirer-target products are similar and competition is weak, while increasing follow-on labeling/manufacturing applications but not new drug creation.
exam_relevance: high
must_memorize: true
tags:
- mergers-and-acquisitions
- market-power
- product-markets
- innovation
- pharmaceuticals
- difference-in-differences
created: 2026-06-05
updated: 2026-06-05
---

# Bonaimé and Wang 2024

## 1. One-Sentence Takeaway
This paper shows that pharmaceutical mergers raise prices in product markets where the acquirer and target overlap using within-deal product-level difference-in-differences, and the main contribution is to show that M&A value creation can come from market power rather than consumer-benefiting synergies or new drug innovation.

## 2. Exam-Ready Abstract
Bonaimé and Wang ask whether pharmaceutical mergers create value through efficiency and innovation or through increased market power. They use detailed product-level drug prices from NADAC over 2013 to 2019 and match these data to pharmaceutical M&A announcements from SDC. Their identification compares acquirer drugs whose product markets consolidate because the target has overlapping drugs to matched same-acquirer drugs whose markets do not consolidate. Prices of affected drugs rise about 2.2% more than matched control drugs and remain elevated for about one year. The price effects are larger when product similarity is higher, when the product market has fewer firms, and when there is no generic competition. Acquirer announcement returns are positive and larger for deals with more product overlap, while innovation gains are concentrated in secondary FDA applications such as labeling and manufacturing changes rather than new drug applications. This paper fits in [[Mergers and Acquisitions]], [[Product Market Competition]], [[Market Power]], [[Innovation]], and [[Antitrust]].

## 3. Research Question
Do pharmaceutical mergers primarily generate consumer-benefiting synergies, such as lower prices and more innovation, or do they increase market power and allow firms to raise prices?

More specifically: the paper tests whether prices rise more for drugs in product markets where the acquirer and target overlap, whether these effects are stronger in less competitive markets, and whether any price increases are accompanied by real new drug innovation.

## 4. Core Mechanism

```text
Pharmaceutical merger with acquirer-target product overlap
-> product market consolidation
-> fewer close substitutes and greater pricing power
-> acquiring firm raises prices on overlapping drugs
-> shareholders gain, consumers/government pay more, and innovation gains are mostly follow-on rather than new-drug creation
```

## 5. Main Findings
1. Acquirer drugs in consolidating product markets experience about 2.2% higher price increases than matched same-firm control drugs, and the effect persists for roughly one year.
2. The price effect is stronger when acquirer-target product similarity is higher and when product markets are less competitive, especially markets with fewer participants or no generic competition.
3. Mergers create shareholder value, with positive five-day acquirer CARs, especially for horizontal deals and deals with more economically meaningful product overlap.
4. Innovation does not rise in the sense of new drugs. Increases in FDA applications are driven by secondary applications, labeling changes, and manufacturing-related changes.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Main price analysis: drug-quarter at the NDC-deal level. Innovation analysis: firm-year at the deal-firm level. |
| Sample period | Drug price sample: 2013 to 2019. Extended innovation analysis: FDA applicants from 1990 to 2020. |
| Main dataset | NADAC drug prices from CMS; SDC M&A announcements; FDA Orange Book; FDA New Drug Approval data; Medicaid SDUD; CRSP/Compustat; WHO ATC classifications. |
| Key variables | Ln drug price; Consolidate; Post; ATC overlap; patent/exclusivity; brand/generic; prescription/OTC; Medicaid units reimbursed; FDA application counts; acquirer CARs. |
| Treatment or shock | A pharmaceutical merger that consolidates a drug product market because the target has a drug or pipeline drug in the same ATC-defined market as the acquirer. |
| Outcome variables | Drug prices; acquirer announcement returns; FDA new drug applications, including initial, secondary, new drug, labeling, and other/manufacturing-related applications. |

## 7. Identification Strategy

### Endogeneity Problem
A simple comparison of drug prices before and after mergers would not be causal because merger targets and acquirers are selected, product markets that consolidate may already have different price trends, and pharmaceutical firms may time mergers around expected demand, regulatory changes, patent expirations, or competitive entry. A simple comparison across firms would also be problematic because acquirers differ from nonacquirers in size, product portfolio, innovation pipeline, and pricing strategy. At the product level, drugs that overlap with target products are not randomly chosen, so they may differ in brand status, generic status, patent protection, and demand.

### Identification Approach
- Natural experiment: Not a clean external shock. The paper uses product-market consolidation around mergers as plausibly differential treatment within the same deal.
- Instrument: None.
- Difference in differences: Main design compares price changes for acquirer drugs in consolidating product markets to matched control drugs produced by the same acquirer but not directly affected by the merger.
- Event study: Estimates event-time coefficients around merger announcements and shows no significant pre-trends before the merger.
- Fixed effects: Product-deal fixed effects and deal-event-time fixed effects in price regressions. Deal-firm and deal-event-time fixed effects in innovation regressions.
- Matching: Sample drugs are matched to same-acquirer control drugs on brand/generic status, prescription/OTC status, patent status, exclusivity status, and closest lagged Medicaid reimbursement volume. Innovation analysis matches acquirers to nonacquirers using Harford (1999) acquisition propensity.
- Placebo tests: Not clear from provided text as a formal placebo, but the event-study pre-trend tests serve a similar diagnostic role.
- Robustness: Alternative product market definitions using narrower ATC levels, MoA, and EPC; cleaner samples excluding drugs affected by multiple mergers; target-drug analysis; alternative event timing around rumors and negotiation periods.
- Alternative source of variation: Cross-sectional heterogeneity in product market concentration, absence of generic competition, pipeline overlap, and economic importance of overlap.

### Is the Identification Convincing?
- Strength: The within-deal, same-acquirer design is strong because it holds constant firm-level merger motives and general pricing policy while comparing affected and unaffected products in the same firm at the same time.
- Weakness: Product overlap is still endogenous. Firms may choose targets because particular overlapping drugs have expected future price growth, regulatory changes, or anticipated changes in demand.
- Referee concern: The matched control drug may not be a true counterfactual if overlapping products are strategically different from non-overlapping products in unobservable ways, such as expected entry, payer mix, or patent cliffs.

## 8. Main Regression or Model

```text
ln(Price_i,k,t) =
  theta Consolidate_i,k x Post_k,t
+ Product-Deal FE
+ Deal-Event-Time FE
+ epsilon_i,k,t
```

The dependent variable is the log inflation-adjusted NADAC price of drug i in deal k at event quarter t. `Consolidate` equals one for acquirer drugs whose product market overlaps with the target's product market. `Post` equals one during and after the merger announcement quarter. The coefficient `theta` is the DID estimate: the differential change in log prices for affected drugs relative to matched same-acquirer control drugs after the merger.

Event-study version:

```text
ln(Price_i,k,t) =
  sum_t theta_t Consolidate_i,k x EventQuarter_k,t
+ Product-Deal FE
+ Deal-Event-Time FE
+ epsilon_i,k,t
```

This checks parallel trends and estimates the dynamic price response around the merger. The main interpretation is that pre-merger `theta_t` coefficients should be close to zero, while post-merger coefficients show whether consolidating drugs become more expensive.

Heterogeneity version:

```text
ln(Price_i,k,t) =
  beta1 Consolidate_i,k x Post_k,t
+ beta2 Consolidate_i,k x Post_k,t x Heterogeneity_i
+ Product-Deal FE
+ Deal-Event-Time FE
+ epsilon_i,k,t
```

`beta2` captures whether the price effect is stronger in markets where market power should matter more, such as concentrated markets or markets without generic competition.

Innovation regression:

```text
Innovation_j,k,t =
  theta Merger_j,k x Post_k,t
+ Deal-Firm FE
+ Deal-Event-Time FE
+ epsilon_j,k,t
```

The innovation outcome is log one plus FDA application counts. `theta` compares acquiring firms to matched nonacquiring firms around the merger.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Mergers and Acquisitions]] by showing that shareholder value creation can reflect market power rather than efficiency gains.
2. [[Product Market Competition]] by using product-level price data and product overlap to identify price effects of consolidation.
3. [[Innovation]] by distinguishing true new drug creation from follow-on applications such as labeling and manufacturing changes.
4. [[Antitrust]] by showing that approved pharmaceutical mergers can still raise prices in affected product markets.

It differs from prior work because it studies an entire industry with granular product-level prices, uses within-deal variation rather than only cross-firm comparisons, and jointly examines prices, shareholder returns, and innovation.

## 10. Closely Related Papers
- [[Bena and Li 2014]]: M&A and innovation; useful contrast because Bonaimé and Wang find limited evidence of new-drug innovation gains.
- [[Cunningham Ederer and Ma 2021]]: Killer acquisitions in pharmaceuticals; related market-power channel through acquisition of potential competitors.
- [[Fathollahi Harford and Klasa 2022]]: Horizontal acquisitions and product similarity; related evidence that product similarity strengthens market power effects.
- [[Hoberg and Phillips 2010]]: Product market synergies and competition in mergers; related text-based view of product similarity and M&A outcomes.
- [[Dafny 2009]]: Hospital mergers and price effects; classic industry-specific evidence on merger-induced price increases.
- [[Sheen 2014]]: Consumer product mergers and possible efficiency gains; useful contrast where prices may fall if synergies dominate.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the literature on mergers, product market competition, and consumer welfare. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Pharmaceutical mergers increase prices in product markets where acquirer and target overlap.
- Data: Product-level NADAC drug prices, SDC merger data, FDA data, Medicaid utilization, CRSP/Compustat, ATC product-market classifications.
- Identification: Within-deal product-level DID comparing affected acquirer drugs to matched same-acquirer unaffected drugs.
- Limitation: Product overlap is not randomly assigned and overlapping drugs may have different unobserved expected trends.
- Connection to other papers: Pair with [[Cunningham Ederer and Ma 2021]] for pharmaceutical M&A and innovation suppression; [[Bena and Li 2014]] for M&A and innovation; [[Fathollahi Harford and Klasa 2022]] for horizontal M&A and product similarity; [[Dafny 2009]] for healthcare merger price effects.
- Best exam phrase: "Bonaimé and Wang use within-deal variation in drug-level product-market overlap to show that pharmaceutical mergers raise prices where market power increases, with little evidence of new-drug innovation gains."

## 12. Hypotheses Inspired by This Paper
H1: Mergers increase product prices more when acquirer-target overlap is high than when overlap is low.

H2: Merger-induced price increases are larger in markets with fewer competitors or weaker generic competition.

H3: If merger value comes from market power rather than synergies, acquirer announcement returns should be larger for deals with more economically important product-market overlap.

## 13. Possible Extension or Research Design
- Research question: Do pharmaceutical merger-induced price increases ultimately pass through to patients' out-of-pocket costs and insurance premiums?
- Hypothesis: Drugs in consolidating product markets experience larger increases in patient out-of-pocket spending and payer reimbursements after mergers than matched control drugs.
- Data: NADAC prices, Medicare Part D claims, Medicaid claims, insurer formulary tiers, copayment data, SDC mergers, FDA drug classifications.
- Identification: Drug-level DID comparing affected overlapping drugs to matched same-acquirer controls, with payer-by-drug or plan-by-drug fixed effects where possible.
- Expected result: Pass-through should be partial but positive, especially for drugs without close generic substitutes.
- Contribution: Links product-market M&A effects to household welfare and public finance costs, rather than stopping at pharmacy acquisition costs.

## 14. Critiques

### Major Concern 1
The key treatment, product-market consolidation, is endogenous. Acquirers may target firms because overlapping products are about to experience favorable demand shocks, patent-related changes, or competitive entry dynamics.

### Major Concern 2
The control drugs are produced by the same acquirer, which is a major strength, but they may not be close substitutes for the treated drugs. The same firm may have different pricing strategies across therapeutic areas, especially if drugs differ in payer mix, medical necessity, or competitive threats.

### Minor Concern
NADAC measures pharmacy acquisition costs and excludes off-invoice rebates and concessions. This is useful for studying manufacturer-to-pharmacy pricing, but it is not the final consumer price.

### Referee Recommendation
Accept, because the paper has a clean and creative within-deal identification strategy, granular product-level data, and a strong contribution to M&A, market power, and antitrust. The main caveat is that treatment is not randomly assigned, but the matching, fixed effects, event studies, and heterogeneity tests make the market-power interpretation persuasive.

## 15. Memory Hooks
- "Same acquirer, treated drug vs control drug."
- "2% price increase for overlapping drugs, about one year."
- "Bigger overlap means bigger price hike."
- "No generic competition equals more pricing power."
- "Innovation rises only in labels and manufacturing, not new drugs."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Mergers and Acquisitions]], [[Product Market Competition]], [[Market Power]], [[Innovation]], [[Antitrust]], or [[Difference-in-Differences]]. The clean exam answer is: "Bonaimé and Wang 2024 use within-deal variation in pharmaceutical product-market overlap as a treatment and show that acquirer drugs in consolidating markets experience about 2% higher price increases than matched same-acquirer control drugs." Use it to argue that M&A gains can come from increased market power rather than efficiency gains passed through to consumers. In a critique answer, emphasize that product overlap is endogenous, but note that the paper is stronger than a standard correlation because it compares treated and control drugs within the same acquirer and deal, uses detailed product matching, includes product-deal and deal-event-time fixed effects, and verifies parallel pre-trends.
