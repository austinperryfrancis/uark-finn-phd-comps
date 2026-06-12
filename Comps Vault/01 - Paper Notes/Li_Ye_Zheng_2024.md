---
type: paper
status: unread
title: Price Ceilings, Market Structure, and Payout Policies
authors: Xiongshi Li, Mao Ye, Miles Zheng
year: 2024
journal: Journal of Financial Economics
professor: DrJandik
seminar: null
jandik_paper_number: 20
jandik_week: 5
jandik_topic: 'Cash and payouts: cash, dividends, and repurchases'
jandik_done: true
field: Corporate Finance
literature:
- Payout Policy
- Share Repurchases
- '[[Bid-Ask Spreads]]'
methods:
- Difference-in-differences
- event studies
- randomized policy experiment
datasets:
- '[[Compustat]]'
- Daily TAQ
- '[[CRSP]]'
- FINRA Tick Size Pilot assignments
- hand-collected ATS-N dark pool filings
identification: SEC Tick Size Pilot Program and historical market-structure reforms
main_result: Market-structure frictions and Rule 10b-18 price ceilings explain part of the rise in repurchases; the Tick Size Pilot reduced repurchases by 21 percent, and by 45 percent for tick-constrained firms.
exam_relevance: high
must_memorize: true
tags:
- payout-policy
- share-repurchases
- market-microstructure
- regulation
- difference-in-differences
- corporate-finance
created: 2026-06-04
updated: 2026-06-04
---

# Li, Ye, and Zheng 2024

## 1. One-Sentence Takeaway
This paper shows that market-structure reforms increased open-market share repurchases by relaxing Rule 10b-18 price-ceiling constraints, using the randomized Tick Size Pilot and historical market-structure reforms, and the main contribution is to provide a microstructure-based explanation for the secular rise of repurchases over dividends.

## 2. Exam-Ready Abstract
Li, Ye, and Zheng ask why share repurchases grew gradually over recent decades even though dividends historically dominated and the tax advantage of repurchases weakened. Their central argument is that Rule 10b-18 creates a price ceiling for issuer repurchases, so issuers cannot simply outbid other traders when buying back shares. This makes market structure first order: if the trading system gives dealers, fast traders, or displayed queues priority at the bid, firms face difficulty executing repurchases. The main evidence comes from the SEC Tick Size Pilot Program, which randomly increased the tick size for treatment stocks from one cent to five cents, partially reversing prior market-structure reforms. Treated firms reduce repurchases by 21 percent, and the effect is concentrated among tick-constrained firms, whose repurchases fall by 45 percent. Historical reforms such as the Manning Rule, Order Handling Rules, decimalization, and NYSE autoquotes also increased repurchases by relaxing execution frictions. This paper connects [[Payout Policy]], [[Share Repurchases]], [[Market Microstructure]], and [[Corporate Finance Regulation]].

## 3. Research Question
Why did open-market share repurchases rise relative to dividends over recent decades, and why was the shift gradual rather than immediate?

More specifically, the paper tests whether Rule 10b-18 price ceilings interact with market structure to constrain firms' ability to repurchase shares, and whether reforms that reduce queue competition, dealer priority, or compliance costs increase repurchase activity.

## 4. Core Mechanism

```text
Market-structure reform or reversal
-> changes issuer ability to buy shares at the Rule 10b-18 price ceiling
-> affects queue position, dark-pool access, and compliance costs
-> firms execute more or fewer open-market repurchases
-> aggregate payout structure shifts between repurchases and dividends
```

For the Tick Size Pilot specifically:

```text
Tick size rises from 1 cent to 5 cents
-> more traders quote at the same bid price
-> bid depth and queue competition increase
-> issuers cannot outbid because of Rule 10b-18
-> firms reduce the intensity of open-market repurchases
```

## 5. Main Findings
1. The 2016 Tick Size Pilot reduced treatment firms' share repurchases by about 21 percent relative to control firms.
2. The effect is concentrated among tick-constrained firms, where repurchases fall by about 45 percent, while tick-unconstrained firms show little change.
3. The mechanism operates through queue competition and dark-pool constraints: firms with larger increases in bid depth reduce repurchases more, and test group 3 firms subject to the Trade-at Rule reduce repurchases more sharply.
4. Historical reforms that relaxed market-structure frictions increased repurchases: the Manning Rule, Order Handling Rules, tick-size reductions, decimalization, and NYSE autoquotes all increased buyback activity.
5. Tender offers, which are outside the open market and exempt from Rule 10b-18, are not affected, supporting the interpretation that the mechanism is specific to open-market execution frictions.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Firm-quarter for the main Tick Size Pilot tests |
| Sample period | Main Tick Size Pilot window around 2014 Q4 to 2018 Q3; historical event studies around reforms in 1994, 1997, 2001, and 2003 |
| Main dataset | Compustat North America Fundamentals Quarterly for payout and accounting variables |
| Additional datasets | FINRA Tick Size Pilot treatment assignments, Daily TAQ for spreads, depth, and turnover, CRSP for share codes, hand-collected ATS-N dark-pool filings |
| Key variables | Repurchase payout, dividend payout, total payout, payout structure, quoted spread, turnover, market depth |
| Treatment or shock | Tick Size Pilot treatment status, tick-constrained status, Trade-at Rule group, and historical market-structure reforms |
| Outcome variables | Repurchase payout, dividend payout, total payout, payout structure, repurchase dummy, tender offers |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between market structure and repurchases would not be causal because firms with different payout policies may choose different trading venues, brokers, liquidity environments, or listing venues. Firms that repurchase more may also be larger, more liquid, more mature, more profitable, or more likely to have investor demand for buybacks. Market structure may also be correlated with time trends, changing tax rules, algorithmic trading, liquidity, or unobserved shifts in shareholder preferences. Reverse causality is less central, but heavy repurchasers could influence liquidity or market depth, which would bias simple estimates.

### Identification Approach
- Natural experiment: The SEC Tick Size Pilot Program randomly assigned eligible stocks to treatment and control groups.
- Instrument: No formal instrument.
- Difference in differences: Compare treated and control firms before and after the Tick Size Pilot.
- Event study: Historical event studies around the Manning Rule, Order Handling Rules, tick-size reductions, decimalization, and NYSE autoquotes.
- Fixed effects: Firm fixed effects and year-quarter fixed effects in the main DiD.
- Matching: Matched control firms are used in several historical and heterogeneity tests.
- Placebo tests: Tender offers are used as a placebo-like outcome because they are exempt from Rule 10b-18 and occur outside the open market.
- Robustness: Heterogeneity by tick-constrained status, bid-depth increases, dark-pool restrictions, and historical reforms.
- Alternative source of variation: Cross-sectional exposure to whether reforms are binding, such as pre-Pilot quoted spreads below five cents.

### Is the Identification Convincing?
- Strength: The randomized Tick Size Pilot is unusually clean for corporate finance, and the effect concentrates exactly where the mechanism predicts.
- Weakness: The main experiment applies to smaller, lower-volume Pilot-eligible stocks, so external validity to very large firms is not automatic.
- Referee concern: The Tick Size Pilot changes liquidity, spreads, depth, and trading incentives at the same time, so separating the pure Rule 10b-18 price-ceiling channel from broader liquidity effects requires the mechanism tests to carry significant weight.

## 8. Main Regression or Model

```text
Outcome_it =
  beta Treatment_i x Post_t
+ Controls_it
+ Firm FE
+ Time FE
+ epsilon_it
```

The dependent variable is a payout outcome such as repurchase payout, dividend payout, total payout, or payout structure. `Treatment_i` equals one for Tick Size Pilot treatment firms, and `Post_t` equals one after the Pilot begins. The coefficient `beta` measures how treated firms change their payout policy relative to control firms after the tick-size increase.

For heterogeneity:

```text
Outcome_it =
  beta1 Treatment_i x Post_t
+ beta2 Treatment_i x Post_t x TickConstrained_i
+ Controls_it
+ Firm FE
+ Time FE
+ epsilon_it
```

`beta1` captures the average treatment effect for less constrained firms. `beta2` captures whether the effect is stronger for firms whose pre-Pilot quoted spreads were below five cents, where the five-cent tick size should bind. The main economic interpretation comes from the treatment effect among tick-constrained firms, because that is where the market-structure friction should matter most.

For the dark-pool mechanism:

```text
Repurchase_it =
  beta1 TreatmentGroup1or2_i x Post_t
+ beta2 TreatmentGroup3_i x Post_t
+ Controls_it
+ Firm FE
+ Time FE
+ epsilon_it
```

The key comparison is whether firms in test group 3, which faced the Trade-at Rule, reduced repurchases more than firms in test groups 1 and 2. A larger reduction in group 3 supports the dark-pool channel.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Payout Policy]] by explaining why repurchases rose relative to dividends.
2. [[Share Repurchases]] by identifying execution frictions as a cost of buybacks.
3. [[Market Microstructure]] by showing that trading rules affect real corporate payout choices.
4. [[Corporate Finance Regulation]] by showing that Rule 10b-18 shapes firm payout behavior.

It differs from prior work because it does not treat repurchase costs as an abstract residual friction. It provides a concrete mechanism: price ceilings plus market structure make issuer execution difficult when firms cannot outbid other traders.

## 10. Closely Related Papers
- [[Miller and Modigliani 1961]]: Benchmark payout irrelevance in frictionless markets.
- [[Grullon and Michaely 2002]]: Documents the rise of repurchases and substitution between dividends and repurchases.
- [[Fama and French 2001]]: Provides payout definitions and the disappearing dividends context.
- [[Chetty and Saez 2005]]: Dividend tax cut and payout responses.
- [[Farre-Mensa, Michaely, and Schmalz 2014]]: Broad survey of payout policy puzzles and evidence.
- [[Cook, Krigman, and Leach 2003]]: Evidence on execution and compliance around open-market repurchases.
- [[Yao and Ye 2018]]: Queue competition mechanism in markets with discrete prices.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on payout policy. Discuss why firms choose dividends versus repurchases, what frictions matter, and how the papers establish causality.

How to use this paper:
- Main finding: Market-structure frictions and Rule 10b-18 price ceilings help explain why repurchases were historically constrained and why they rose gradually.
- Data: Compustat payout data, FINRA Tick Size Pilot assignment, Daily TAQ microstructure data, CRSP filters, ATS-N dark-pool filings.
- Identification: Randomized Tick Size Pilot DiD plus historical event studies around market-structure reforms.
- Limitation: The main experimental sample consists of Pilot-eligible stocks, not the full universe of large repurchasers.
- Connection to other papers: Complements tax and agency explanations by adding an execution-cost mechanism.
- Best exam phrase: "Li, Ye, and Zheng show that repurchases are not just a boardroom payout choice; they are also an execution problem created by Rule 10b-18 and market structure."

## 12. Hypotheses Inspired by This Paper
H1: Firms facing tighter execution constraints under Rule 10b-18 reduce open-market repurchases relative to otherwise similar firms.

H2: Repurchases are more sensitive to market-structure frictions when firms are tick constrained, face deeper queues, or lose access to dark-pool execution.

H3: Regulatory reforms that raise the price ceiling or allow more passive midpoint or VWAP execution should increase open-market repurchases relative to dividends.

## 13. Possible Extension or Research Design
- Research question: Do modern repurchase disclosure rules or buyback taxes change the importance of execution frictions in open-market repurchases?
- Hypothesis: If firms face greater disclosure risk or tax costs, execution frictions should matter less at the margin because some repurchases are deterred before execution.
- Data: Daily repurchase disclosures if available, Compustat, CRSP, TAQ, 10b5-1 plan disclosures, broker or venue-level trading data if obtainable.
- Identification: Difference-in-differences around a regulatory change that affects disclosure, taxes, or safe-harbor conditions.
- Expected result: The firms most exposed to execution frictions before the rule change should reduce or restructure buybacks more strongly.
- Contribution: Links payout policy, disclosure regulation, market microstructure, and real corporate financial decisions.

## 14. Critiques

### Major Concern 1
The Tick Size Pilot sample is not the entire universe of U.S. firms. Because the Pilot focused on smaller and less liquid stocks, the external validity for mega-cap repurchasers may be limited.

### Major Concern 2
The tick-size shock changes multiple dimensions of liquidity at once, including quoted spreads, depth, turnover, and queue competition. The paper argues that depth and Rule 10b-18 are central, but a referee could ask whether broader liquidity deterioration also explains part of the repurchase decline.

### Minor Concern
The historical event studies are less clean than the randomized Pilot because other market and regulatory changes occurred around the same time.

### Referee Recommendation
Accept, because the randomized Tick Size Pilot provides unusually strong identification for a corporate finance question, the mechanism tests are well aligned with the theory, and the paper offers a novel micro-foundation for repurchase costs.

## 15. Memory Hooks
- "Buybacks are an execution problem."
- "Rule 10b-18 creates a price ceiling, so firms cannot outbid."
- "Five-cent tick creates a longer queue at the bid."
- "Tick-constrained firms drive the result."
- "Dark pools help firms bypass queues, but the Trade-at Rule blocks that channel."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Payout Policy]], [[Share Repurchases]], [[Market Microstructure]], or [[Corporate Finance Regulation]]. The clean exam answer is: "Li, Ye, and Zheng 2024 use the randomized SEC Tick Size Pilot as a shock to market-structure frictions and show that increasing tick sizes reduced share repurchases, especially for tick-constrained firms." Use it to argue that the rise of repurchases is not explained only by taxes, agency, or signaling, but also by the declining execution costs of buying shares under Rule 10b-18. In a critique answer, emphasize external validity and the fact that tick size affects several liquidity dimensions, but note that the paper is stronger than a standard correlation because treatment assignment in the Tick Size Pilot is randomized and the effects concentrate exactly where the price-ceiling mechanism predicts.