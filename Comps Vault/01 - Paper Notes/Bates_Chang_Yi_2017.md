---
type: paper
status: unread
title: Why Has the Value of Cash Increased Over Time?
authors: Thomas W. Bates, Ching-Hung Chang, Jianxin Daniel Chi
year: 2017
journal: Journal of Financial and Quantitative Analysis
seminar:
field: Corporate Finance
literature: Corporate Cash Holdings; Financial Flexibility; Financing Frictions
methods: Valuation regressions; partial adjustment model; cross-sectional heterogeneity; robustness tests
datasets: CRSP/Compustat; Thomson SDC; Thomson Reuters 13F; FRED corporate bond yields; RiskMetrics
identification: Time-series and cross-sectional variation in firm characteristics and macro-financial conditions
main_result: The marginal value of corporate cash rose from $0.61 in the 1980s to $1.04 in the 1990s and $1.12 in the 2000s, largely because precautionary motives and financing frictions became more important.
exam_relevance: high
must_memorize: true
tags:
  - corporate-finance
  - cash-holdings
  - financial-flexibility
  - financing-frictions
  - capital-structure
  - DrJandik
created: 2026-06-04
updated: 2026-06-04
---

# Bates, Chang, and Chi 2017

## 1. One-Sentence Takeaway
This paper shows that the marginal value of corporate cash increased sharply from the 1980s to the 2000s using CRSP/Compustat valuation regressions, and the main contribution is showing that rising cash balances were valued positively because precautionary demand and financing frictions increased over time.

## 2. Exam-Ready Abstract
Bates, Chang, and Chi ask why the market value of corporate cash increased over time even as U.S. firms accumulated much larger cash balances. Using U.S. nonfinancial public firms from 1980 to 2009, they estimate the marginal value of cash using the Faulkender and Wang return-based valuation framework and robustness tests based on Pinkowitz and Williamson. The core finding is that an additional dollar of cash was worth $0.61 in the 1980s, $1.04 in the 1990s, and $1.12 in the 2000s. The increase is strongest for firms with high investment opportunities, high cash-flow volatility, greater financial constraints, exposure to competitive product markets, and exposure to wider credit spreads. The paper also estimates cash speed-of-adjustment models and finds that adjustment toward target cash holdings slowed over time, especially for financially constrained firms with cash deficits. The main interpretation is that firms wanted more precautionary liquidity, but capital market frictions prevented them from quickly reaching optimal cash levels. This connects to [[Corporate Cash Holdings]], [[Financial Flexibility]], [[Financing Frictions]], and [[Capital Structure]].

## 3. Research Question
Why has the value of corporate cash increased over time?

More specifically: does the rising marginal value of cash reflect stronger precautionary demand for liquidity, changing firm composition, credit market risk, product market competition, declining diversification, investor sentiment, or agency conflicts?

## 4. Core Mechanism
Use a chain that can be memorized for comps:

```text
More volatile investment environment and tighter external finance
-> firms have stronger precautionary demand for liquidity
-> cash helps avoid underinvestment when external capital is costly
-> investors place a higher marginal value on incremental cash
-> the market value of cash rises over time despite larger cash balances
```

For the speed-of-adjustment part:

```text
Rising target cash needs
-> firms with cash deficits need to raise or retain liquidity
-> financing frictions slow adjustment toward target cash
-> cash-deficit and constrained firms remain below optimal cash
-> each additional dollar of cash becomes especially valuable
```

## 5. Main Findings
1. The marginal value of cash rises substantially over time: $0.61 in the 1980s, $1.04 in the 1990s, and $1.12 in the 2000s.
2. The 1990s increase is mainly explained by investment opportunities, cash-flow volatility, product market competition, IPO composition, declining diversification, and investor sentiment.
3. The 2000s increase is mainly explained by credit market risk and financing frictions, especially for firms with cash deficits and greater financial constraints.
4. Agency conflicts help explain cross-sectional variation in the value of cash, but do not explain the secular increase over time.
5. The speed of adjustment toward target cash holdings declines over time, especially for financially constrained firms with negative excess cash.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Firm-year |
| Sample period | 1980 to 2009 |
| Main dataset | CRSP/Compustat merged database |
| Key variables | Cash, change in cash, excess stock returns, earnings, net assets, R&D, interest expense, dividends, leverage, net financing, market-to-book, cash-flow volatility, SA index, credit spread, HHI, multisegment dummy, investor sentiment |
| Treatment or shock | No single treatment shock. Main variation comes from time, decade indicators, firm characteristics, and macro-financial conditions |
| Outcome variables | Excess stock returns for valuation regressions; cash ratio for speed-of-adjustment regressions |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between cash and firm value is not causal because firms choose cash policies endogenously. Firms with better investment opportunities, higher expected profitability, lower risk, better governance, or different financing access may both hold more cash and receive higher valuations. Reverse causality is also possible because high-valued firms may raise cash more easily or retain more liquidity. There is also a simultaneity concern because changes in cash and stock returns may both respond to omitted news about future firm fundamentals.

### Identification Approach
- Natural experiment: None.
- Instrument: None.
- Difference in differences: Not a clean DiD. The paper uses decade interactions and heterogeneity rather than a shock-based design.
- Event study: Not a central event-study design.
- Fixed effects: Uses valuation regressions with extensive controls and standard errors robust to heteroskedasticity and firm and year clustering. Not clear from provided text that the main valuation regressions include firm fixed effects.
- Matching: Not a central design.
- Placebo tests: Uses robustness checks against extreme returns, alternative cash valuation models, profitability trends, and future earnings explanations.
- Robustness: Pinkowitz and Williamson alternative valuation model, winsorizing excess returns, excluding outlier years such as 1999 and 2003, controlling for future profitability, controlling for profitability trends, alternative financial constraint measures.
- Alternative source of variation: Cross-sectional heterogeneity by investment opportunities, cash-flow volatility, financial constraints, IPO cohorts, credit spreads, product market competition, diversification, sentiment, and governance.

### Is the Identification Convincing?
- Strength: Strong descriptive and mechanism-consistent evidence. The result survives alternative valuation models and many plausible omitted-variable checks.
- Weakness: The paper does not have a clean exogenous shock spanning the full 1980 to 2009 period, so the evidence is not fully causal.
- Referee concern: The paper explains a secular trend with variables that are themselves trending, so the concern is whether the mechanisms are causal or simply correlated with time.

## 8. Main Regression or Model

The main valuation regression follows Faulkender and Wang:

```text
Excess_Return_it =
  gamma0
+ gamma1 * Delta_Cash_it / Market_Value_i,t-1
+ gamma2 * Delta_Earnings_it / Market_Value_i,t-1
+ gamma3 * Delta_NetAssets_it / Market_Value_i,t-1
+ gamma4 * Delta_RD_it / Market_Value_i,t-1
+ gamma5 * Delta_Interest_it / Market_Value_i,t-1
+ gamma6 * Delta_Dividends_it / Market_Value_i,t-1
+ gamma7 * Cash_i,t-1 / Market_Value_i,t-1
+ gamma8 * Leverage_it
+ gamma9 * Net_Financing_it / Market_Value_i,t-1
+ epsilon_it
```

The key coefficient is `gamma1`, which estimates the marginal value of one additional dollar of cash. The dependent variable is the firm's excess annual stock return relative to a benchmark portfolio. The controls capture changes in fundamentals that investors may value directly, so the change in cash coefficient is interpreted as the market value of incremental cash.

The time-trend version interacts cash changes with decade indicators:

```text
Excess_Return_it =
  beta1 * Delta_Cash_it
+ beta2 * Delta_Cash_it x DUM_1990
+ beta3 * Delta_Cash_it x DUM_2000
+ Controls_it
+ epsilon_it
```

`beta1` gives the marginal value of cash in the 1980s. `beta2` and `beta3` show the incremental value of cash in the 1990s and 2000s relative to the 1980s.

The speed-of-adjustment model is:

```text
Cash_it =
  gamma0
+ gamma1 * Cash_i,t-1
+ beta * X_it
+ epsilon_it
```

The speed of adjustment is `1 - gamma1`. A lower speed of adjustment means firms adjust more slowly toward target cash holdings.

The excess-cash version is:

```text
Cash_it =
  gamma0
+ gamma1 * Cash_i,t-1
+ gamma2 * Excess_Cash_i,t-1 x Cash_i,t-1
+ gamma3 * Excess_Cash_i,t-1
+ beta * X_it
+ epsilon_it
```

Here the speed of adjustment is:

```text
SOA = 1 - (gamma1 + gamma2 * Excess_Cash_i,t-1)
```

This model tests whether firms with cash deficits adjust more slowly than firms with cash surpluses.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Corporate Cash Holdings]] by explaining not just why firms hold more cash, but why investors value cash more over time.
2. [[Financial Flexibility]] by showing that cash becomes more valuable when external financing is costly and investment opportunities are valuable.
3. [[Financing Frictions]] by linking the rising value of cash to slower adjustment toward target liquidity, especially among constrained firms.
4. [[Product Market Competition]] by showing that cash has strategic value in more competitive industries.
5. [[Corporate Governance]] by showing that agency conflicts matter cross-sectionally but do not explain the long-run increase in cash value.

It differs from prior work because it focuses on the secular change in the marginal value of cash rather than the cross-sectional value of cash or the level of cash holdings.

## 10. Closely Related Papers
- [[Opler, Pinkowitz, Stulz, and Williamson 1999]]: Classic determinants of corporate cash holdings.
- [[Faulkender and Wang 2006]]: Provides the return-based method for estimating the marginal value of cash.
- [[Bates, Kahle, and Stulz 2009]]: Shows that U.S. firms hold much more cash over time, largely due to precautionary motives.
- [[Denis and Sibilkov 2010]]: Shows that cash is more valuable for financially constrained firms.
- [[Dittmar and Mahrt-Smith 2007]]: Shows that governance affects the value of cash.
- [[Duchin, Ozbas, and Sensoy 2010]]: Links cash and investment during the financial crisis.
- [[Harford, Klasa, and Maxwell 2014]]: Links refinancing risk and debt maturity to cash policy.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on corporate cash holdings. Why do firms hold cash, and how do investors value cash?

How to use this paper:
- Main finding: The marginal value of cash increased from the 1980s to the 2000s, even as firms held more cash.
- Data: U.S. nonfinancial public firms from CRSP/Compustat, 1980 to 2009.
- Identification: Return-based valuation regressions with decade interactions, heterogeneity by firm characteristics, robustness checks, and speed-of-adjustment models.
- Limitation: Not a clean causal design because there is no exogenous shock spanning the full sample.
- Connection to other papers: Use after [[Bates, Kahle, and Stulz 2009]] to say that not only did cash holdings rise, but the market increasingly valued cash.
- Best exam phrase: "Bates, Chang, and Chi show that the rise in corporate cash should not be read simply as agency-driven hoarding. Investors increasingly valued cash because precautionary liquidity became more important."

## 12. Hypotheses Inspired by This Paper
H1: The value of cash should increase more for firms exposed to external financing disruptions than for firms with stable financing access.

H2: The value of cash should be higher for firms facing product market threats because liquidity allows them to defend market share and continue investment when rivals are constrained.

H3: Firms with negative excess cash and high financing constraints should display slower adjustment toward target cash and larger investment sensitivity to liquidity shocks.

## 13. Possible Extension or Research Design
- Research question: Did the value of cash increase after COVID-19 supply chain disruptions, especially for firms exposed to input-market fragility?
- Hypothesis: Cash became more valuable after COVID for firms with high supply chain exposure, high working-capital needs, and limited credit access.
- Data: CRSP/Compustat, FactSet Revere supply chain links, syndicated loan data, and firm-level credit ratings.
- Identification: Difference in differences comparing firms with high versus low pre-COVID supply chain exposure before and after March 2020, with firm and quarter fixed effects.
- Expected result: Cash is valued more after the shock for firms with fragile supply chains, especially financially constrained firms.
- Contribution: Extends the precautionary cash literature from financing frictions to real-side supply chain frictions.

## 14. Critiques

### Major Concern 1
The paper is not causally identified in the modern shock-based sense. The mechanisms are convincing, but many determinants trend over time, so it is hard to separate true causal channels from correlated secular changes.

### Major Concern 2
The marginal value of cash is inferred from stock returns and accounting changes. If the model does not fully control for changing expectations about growth, risk, profitability, or intangible investment, the cash coefficient may partly capture omitted information.

### Minor Concern
The decade framing is intuitive but somewhat coarse. Important variation may occur around specific episodes such as the dot-com boom, the 2001 recession, or the 2008 financial crisis.

### Referee Recommendation
R&R, because the question is important and the evidence is broad and carefully checked, but the causal interpretation should be framed as mechanism-consistent evidence rather than definitive identification.

## 15. Memory Hooks
- "$0.61, $1.04, $1.12": value of $1 cash in the 1980s, 1990s, and 2000s.
- "Not hoarding, flexibility": rising cash balances were valued positively by investors.
- "1990s growth and volatility": investment opportunities, R&D, cash-flow volatility, competition.
- "2000s credit risk": credit spreads and financing frictions matter more.
- "Cash deficits adjust slowly": constrained firms below target cash cannot catch up quickly.

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Corporate Cash Holdings]], [[Financial Flexibility]], [[Financing Frictions]], [[Precautionary Savings]], or [[Capital Structure]]. The clean exam answer is: "Bates, Chang, and Chi use U.S. public-firm valuation regressions from 1980 to 2009 and show that the marginal value of cash rose from $0.61 in the 1980s to more than $1 in later decades." Use it to argue that rising corporate cash balances are not necessarily agency-driven waste, because cash can become more valuable when investment opportunities, cash-flow risk, product market competition, and credit market risk increase. In a critique answer, emphasize that the design is not a clean natural experiment, but note that the paper is stronger than a standard correlation because it uses a validated cash valuation framework, alternative valuation models, many robustness checks, and mechanism-based heterogeneity.