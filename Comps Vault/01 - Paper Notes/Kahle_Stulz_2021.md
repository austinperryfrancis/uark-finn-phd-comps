---
type: paper
status: unread
title: Why are corporate payouts so high in the 2000s?
authors: Kathleen Kahle; René M. Stulz
year: 2021
journal: Journal of Financial Economics
seminar:
field: Corporate Finance
literature: Payout Policy; Share Repurchases; Corporate Investment; Financial Flexibility; Agency Costs
methods: Descriptive decomposition; payout regressions; prediction models; firm fixed effects; robustness tests
datasets: CRSP; Compustat; CPI
identification: Predictive and descriptive decomposition using pre-2000 versus post-2000 firm characteristics, not a causal natural experiment
main_result: Higher payouts in the 2000s are driven by both higher operating income and higher payout rates, with repurchases and changing firm characteristics explaining much of the increase.
exam_relevance: high
must_memorize: true
tags:
  - payout-policy
  - repurchases
  - dividends
  - corporate-investment
  - free-cash-flow
  - agency-costs
  - financial-flexibility
  - corporate-finance
  - DrJandik
created: 2026-06-04
updated: 2026-06-04
---

# Kahle and Stulz 2021

## 1. One-Sentence Takeaway
This paper shows that corporate payouts became much higher in the 2000s because firms had more aggregate income and higher payout rates, especially through repurchases, and the main contribution is showing that changing firm characteristics and greater payout sensitivity to free cash flow explain much of the increase rather than a simple story that buybacks crowded out investment.

## 2. Exam-Ready Abstract
Kahle and Stulz ask why U.S. public industrial firms paid out so much more through dividends and repurchases in the 2000s than in earlier decades. Using CRSP/Compustat data from 1971 to 2019, they decompose aggregate payouts into operating income and payout rates, then estimate payout models using pre-2000 firm characteristics to predict post-2000 payout behavior. They find that average annual real payouts in 2000 to 2019 are more than three times larger than in 1971 to 1999, with 37% of the increase explained by higher aggregate operating income and 63% explained by higher payout rates. The increase in payout rates comes almost entirely from repurchases, while dividend payout rates are roughly stable. Older, larger, cash-rich firms with more free cash flow explain a sizable part of the increase, and firms in the 2000s appear to pay out more of their free cash flow. Importantly, capital expenditures fall for both payers and nonpayers, so the paper argues it is not plausible to blame higher payouts alone for the broad decline in capital expenditures. This paper connects to [[Payout Policy]], [[Share Repurchases]], [[Financial Flexibility]], [[Corporate Investment]], and [[Agency Costs of Free Cash Flow]].

## 3. Research Question
Why are corporate payouts so high in the 2000s?

More specifically: is the rise in payouts driven by higher aggregate earnings, higher payout propensities, changing firm characteristics, greater use of repurchases, or a reduction in corporate investment?

## 4. Core Mechanism
Use a chain that can be memorized for comps:

```text
Shift toward older, larger, more profitable public firms
-> higher operating income and more free cash flow
-> repurchases provide flexible payout technology
-> firms pay out a larger share of operating income and free cash flow
-> aggregate payouts rise sharply in the 2000s
```

Alternative political critique mechanism tested indirectly:

```text
High repurchases
-> cash leaves the firm
-> less capital available for investment
-> lower capital expenditures
-> underinvestment
```

The paper weakens this critique because capital expenditures fall similarly for payers and nonpayers.

## 5. Main Findings
1. Aggregate real payouts by U.S. public industrial firms are more than three times higher in 2000 to 2019 than in 1971 to 1999.
2. The increase in aggregate payouts is decomposed into 37% from higher aggregate operating income and 63% from higher payout rates.
3. The increase in payout rates is driven almost entirely by repurchases. Dividend payout rates are roughly unchanged across the two periods.
4. Firm characteristics explain a large fraction of the increase. Important characteristics include firm size, age, cash holdings, leverage, and free cash flow.
5. Models estimated on 1971 to 1999 data explain 56.92% of the increase in the average payout rate for all firms and 35.74% for payers. Excluding the TCJA-affected years improves explanatory power.
6. Firms that initiate payouts in the 2000s, especially through repurchases, have higher payout rates than predicted by their characteristics.
7. Capital expenditures decline in the 2000s, but the decline is similar for payers and nonpayers, so the evidence does not support a simple claim that payouts caused the decline in investment.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Firm-year and aggregate-year |
| Sample period | 1971 to 2019 |
| Main dataset | CRSP/Compustat merged sample of U.S. public industrial firms |
| Sample restrictions | Excludes non-U.S.-incorporated firms, financial firms, utilities, and firms missing key accounting or market data |
| Key variables | Net payouts, dividends, net repurchases, operating income, assets, market capitalization, free cash flow, cash holdings, leverage, firm age, capex, R&D, Tobin's q |
| Treatment or shock | Not a single treatment. Main comparison is pre-2000 versus 2000 to 2019, with attention to 2018 TCJA effects |
| Outcome variables | Aggregate payouts, firm payout rate, net payout over operating income, net payout over lagged assets |
| Important visual evidence | Figure 1 shows aggregate real payouts rising sharply, especially repurchases. Figure 2 shows the payout rate rising over time. Figure 3 compares actual payouts with payouts predicted from pre-2000 aggregate models. |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between repurchases and lower investment is not causal because payout policy, investment, profitability, firm age, growth opportunities, leverage, cash holdings, and governance are jointly determined. Older and more profitable firms naturally have fewer physical investment opportunities and more cash to distribute. Firms with high payouts may look like they underinvest, but they may simply be mature firms with lower marginal returns to capital. There is also omitted-variable risk from changes in the public-firm population, the rise of intangible capital, tax policy, equity compensation, institutional ownership, and macroeconomic conditions. Reverse causality is also possible because firms may pay out after investment opportunities decline rather than cut investment because they pay out.

### Identification Approach
- Natural experiment: No primary natural experiment. The 2018 TCJA is treated as a special year and robustness concern, not the main source of identification.
- Instrument: None.
- Difference in differences: Not a standard DiD. The paper compares pre-2000 and post-2000 periods and contrasts top payers, other payers, and nonpayers.
- Event study: Aggregate time-series figures show the evolution of payouts and payout rates, but this is descriptive rather than causal.
- Fixed effects: Firm fixed effects are used in some firm-level payout regressions.
- Matching: None.
- Placebo tests: Not a formal placebo design. The closest exercise is showing that macroeconomic variables do not explain payouts beyond aggregate earnings.
- Robustness: Uses gross versus net payouts, log payout rates, separate dividend and repurchase regressions, alternative payer definitions, long-lived firms, multinational versus domestic firms, market timing controls, and special treatment of TCJA years.
- Alternative source of variation: Uses firm characteristics estimated in 1971 to 1999 to predict payout rates in 2000 to 2019. Also allows 2000s intercepts and slopes to test whether payout sensitivity to characteristics changed.

### Is the Identification Convincing?
- Strength: Very strong for documenting facts, decomposing aggregate payouts, and showing that changing firm characteristics explain much of the increase.
- Weakness: Not a clean causal design for whether repurchases reduce investment or whether institutional monitoring causes higher payout sensitivity.
- Referee concern: The paper convincingly rejects overly simple narratives, but a referee could ask for stronger causal identification of the monitoring channel and the investment-crowding-out channel.

## 8. Main Regression or Model

The accounting decomposition is:

```text
Payout_t = Payout rate_t x Operating income_t
```

This separates the increase in payouts into a component due to more income and a component due to a higher propensity to pay out income.

A simplified firm-level payout regression is:

```text
PayoutRate_it =
  beta X_it
+ delta D2000s_t
+ gamma D2010s_t
+ theta D2018_t
+ Firm FE
+ epsilon_it
```

Where `PayoutRate_it` is net payout divided by operating income, and `X_it` includes firm characteristics such as market leverage, size, operating cash flow, fixed assets, Tobin's q, R&D, SG&A, advertising, capital expenditures, cash holdings, accounting losses, high-tech status, and firm age.

The main prediction exercise is:

```text
Estimate beta using 1971 to 1999 data
-> apply beta to 2000 to 2019 firm characteristics
-> compare predicted payout rates to actual payout rates
```

The slope-change model is:

```text
PayoutRate_it =
  beta X_it
+ delta D2000s_t
+ theta (D2000s_t x X_it)
+ Firm FE
+ epsilon_it
```

Here, `theta` captures whether the relation between firm characteristics and payout rates becomes stronger in the 2000s. The paper interprets stronger post-2000 sensitivity as consistent with firms paying out more aggressively when characteristics indicate that payout is appropriate, possibly because of stronger shareholder monitoring.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Payout Policy]] by explaining why aggregate payouts rose so sharply in the 2000s.
2. [[Share Repurchases]] by showing that repurchases, not dividends, drive the increase in payout rates.
3. [[Corporate Investment]] by challenging the simple claim that high payouts are the main cause of lower capital expenditures.
4. [[Agency Costs of Free Cash Flow]] by showing that firms with more free cash flow pay out more, especially in the 2000s.
5. [[Financial Flexibility]] by emphasizing the role of repurchases as a flexible payout tool.

It differs from prior work because it directly decomposes the post-2000 payout increase into income growth and payout-rate growth, then asks whether firm characteristics from the earlier period can predict modern payout behavior.

## 10. Closely Related Papers
- [[Fama and French 2001]]: Disappearing dividends and whether lower dividend propensity reflects changing firm characteristics.
- [[DeAngelo, DeAngelo, and Stulz 2006]]: Lifecycle theory of payout policy, where mature firms with retained earnings and fewer growth opportunities pay more.
- [[Grullon and Michaely 2002]]: Repurchases and dividends as substitute payout mechanisms.
- [[Skinner 2008]]: The growing importance of repurchases in corporate payout policy.
- [[Almeida, Fos, and Kronlund 2016]]: The real effects of share repurchases and the concern that repurchases may affect investment.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on payout policy and share repurchases. Do repurchases reduce corporate investment? Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Payouts are much higher in the 2000s, but this reflects both higher income and higher payout rates, with repurchases driving the payout-rate increase.
- Data: CRSP/Compustat U.S. public industrial firms from 1971 to 2019.
- Identification: Descriptive decomposition and prediction using pre-2000 payout models, not a causal shock.
- Limitation: Cannot causally prove that monitoring causes higher payouts or that payouts do not reduce investment at the firm level.
- Connection to other papers: Pair with [[Fama and French 2001]] on disappearing dividends, [[DeAngelo, DeAngelo, and Stulz 2006]] on lifecycle payout theory, and [[Almeida, Fos, and Kronlund 2016]] on repurchases and investment.
- Best exam phrase: "Kahle and Stulz show that the modern payout boom is not just a buyback story. It is also a lifecycle and free-cash-flow story."

## 12. Hypotheses Inspired by This Paper
H1: Older, larger, cash-rich firms with more free cash flow have higher payout rates, especially in the post-2000 period.

H2: The sensitivity of payouts to free cash flow is stronger when institutional ownership or shareholder monitoring is higher.

H3: If buybacks crowd out investment, the decline in capital expenditures should be concentrated among repurchasing firms. If the decline reflects broader technological or intangible-capital shifts, capex should fall among both payers and nonpayers.

H4: Firms that initiate payouts through repurchases should have higher and more flexible payout rates than firms that initiate payouts through dividends.

## 13. Possible Extension or Research Design
- Research question: Does institutional investor monitoring causally increase payout sensitivity to free cash flow?
- Hypothesis: Exogenous increases in institutional ownership cause firms with high free cash flow and low investment opportunities to increase repurchases.
- Data: CRSP/Compustat, Thomson Reuters 13F institutional ownership, Russell 1000/2000 index data, payout data, investment data, and firm fundamentals.
- Identification: Use Russell index reconstitution around the Russell 1000/2000 cutoff as a quasi-exogenous shock to institutional ownership and passive investor attention.
- Expected result: Firms receiving exogenous institutional ownership increases raise payout rates primarily when they have high cash or free cash flow and weak investment opportunities.
- Contribution: This would provide a causal test of the monitoring mechanism that Kahle and Stulz suggest but do not fully identify.

## 14. Critiques

### Major Concern 1
The paper is mostly descriptive and predictive, not causal. It documents that payout increases are associated with firm characteristics and greater payout sensitivity, but it does not cleanly identify whether institutional monitoring causes higher payouts.

### Major Concern 2
The pre-2000 versus post-2000 split captures many overlapping changes: intangible investment, public-firm composition, institutional ownership, tax policy, equity compensation, globalization, and changes in market power. The models may not fully capture changing investment opportunity sets.

### Minor Concern
Measurement of repurchases is difficult because firms both issue and repurchase equity, often because of employee stock compensation. Net repurchases are the right concept, but measurement choices can affect magnitudes.

### Referee Recommendation
Accept, because the paper answers an important policy and corporate finance question with careful data work, clear decomposition, and extensive robustness. The main caveat is that the paper should be cited as strong descriptive evidence rather than clean causal evidence.

## 15. Memory Hooks
- 37% income, 63% payout rate.
- Dividends flat, repurchases up.
- Top 200 payers account for more than 80% of payouts.
- Old, large, cash-rich firms pay out more.
- Capex falls for payers and nonpayers, so buybacks are not the simple villain.
- 2018 TCJA is the trillion-dollar payout year.
- Best phrase: "Modern payouts are a repurchase-driven lifecycle phenomenon."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | Medium |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Payout Policy]], [[Share Repurchases]], [[Corporate Investment]], [[Financial Flexibility]], or [[Agency Costs of Free Cash Flow]]. The clean exam answer is: "Kahle and Stulz use CRSP/Compustat data from 1971 to 2019 to show that the post-2000 payout boom is explained partly by higher operating income and mostly by higher payout rates, with repurchases driving the increase." Use it to argue that higher payouts reflect mature, large, cash-rich firms distributing free cash flow, not necessarily firms starving investment. In a critique answer, emphasize that the paper is not a causal test of whether repurchases reduce investment, but note that it is stronger than a standard correlation because it decomposes aggregate payouts, models firm characteristics using pre-2000 data, and shows that capital expenditures decline similarly for payers and nonpayers.