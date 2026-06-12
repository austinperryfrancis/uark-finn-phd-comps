---
type: paper
status: unread
title: Does Asymmetric Information Drive Capital Structure Decisions?
authors: Sreedhar T. Bharath; Paolo Pasquariello; Guojun Wu
year: 2009
journal: Review of Financial Studies
professor: DrJandik
seminar: null
jandik_paper_number: 5
jandik_week: 2
jandik_topic: 'Capital structure: determinants and targets, taxes, and information asymmetry'
jandik_done: true
field: Corporate Finance
literature:
- '[[Capital Structure]]'
- Pecking Order Theory
- Information Asymmetry
methods:
- Principal components index
- financing deficit regressions
- firm fixed effects
- two-way sorts
datasets:
- '[[Compustat]]'
- '[[CRSP]]'
- microstructure adverse selection measures
- SEC ORS insider trading data
identification: Cross-sectional conditioning on time-varying adverse selection, not a natural experiment
main_result: Firms with greater adverse selection fund more of their financing deficits with debt. High adverse selection firms issue about 30 cents more debt per dollar of deficit than low adverse selection firms.
exam_relevance: high
must_memorize: true
tags:
- capital-structure
- pecking-order
- information-asymmetry
- adverse-selection
- market-microstructure
- corporate-finance
created: 2026-06-03
updated: 2026-06-03
---

# Bharath, Pasquariello, and Wu 2009

## 1. One-Sentence Takeaway
This paper shows that information asymmetry helps explain capital structure choices using a market microstructure-based adverse selection index, and the main contribution is showing that the [[Pecking Order Theory]] works best when its core assumption, severe adverse selection, is actually present in the data.

## 2. Exam-Ready Abstract
Bharath, Pasquariello, and Wu ask whether asymmetric information actually drives firms' capital structure decisions, rather than simply testing whether firms follow a strict pecking order on average. They build a firm-year adverse selection index from market microstructure measures such as bid-ask spread components, return-volume relations, probability of informed trading, illiquidity, liquidity, and return reversal. Using U.S. nonfinancial, nonutility firms from COMPUSTAT and CRSP over 1973 to 2002, they test whether firms with higher adverse selection finance deficits with more debt. The main finding is that firms in the highest adverse selection decile issue about 30 cents more debt per dollar of financing deficit than firms in the lowest adverse selection decile. They also find that both the level and change in adverse selection predict leverage and changes in leverage, even after controlling for size, tangibility, Q, profitability, turnover, volatility, and insider trading. The paper does not strongly support the strict pecking order, but it supports a conditional or modified pecking order where information asymmetry matters most when adverse selection is severe. This connects directly to [[Capital Structure]], [[Pecking Order Theory]], [[Information Asymmetry]], and [[Market Microstructure]].

## 3. Research Question
What is the paper trying to answer?

Does asymmetric information, measured directly from market perceptions of adverse selection, explain firms' capital structure decisions?

More specifically: does the sensitivity of debt issuance to financing deficits increase when a firm faces greater information asymmetry, as predicted by the [[Pecking Order Theory]]?

## 4. Core Mechanism
Use a chain that can be memorized for comps:

```text
Higher adverse selection about firm value
-> equity becomes more information-sensitive and more costly to issue
-> managers avoid issuing undervalued equity
-> firms rely more heavily on debt when financing deficits arise
-> high information asymmetry firms show stronger debt-deficit sensitivity and higher leverage
```

## 5. Main Findings
1. Firms with higher adverse selection fund a larger share of financing deficits with debt. High adverse selection decile firms issue about 30 cents more debt per dollar of financing deficit than low adverse selection decile firms.
2. Changes in adverse selection also matter. Firms experiencing larger increases in adverse selection fund more of their current financing deficits with debt.
3. The results survive conventional leverage controls, firm fixed effects, alternative adverse selection measures, and controls for size, tangibility, Q, profitability, turnover, volatility, and insider trading.
4. The strict pecking order is not fully supported because debt-deficit coefficients are below one and firms still issue equity. The modified pecking order is supported because the theory works better when adverse selection is high.
5. The adverse selection effect is strongest for low-Q firms, consistent with Myers and Majluf-style intuition that adverse selection over assets in place makes equity issuance especially costly.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Firm-year |
| Sample period | Adverse selection index built over 1972 to 2002; main capital structure tests focus on 1973 to 2002 |
| Main dataset | COMPUSTAT for accounting and financing variables; CRSP for stock returns, volume, and liquidity measures |
| Key variables | ASY, change in ASY, financing deficit, net debt issuance, leverage, tangibility, Q, sales, profitability, turnover, volatility |
| Treatment or shock | No exogenous shock. Main conditioning variable is firm-level adverse selection, measured using market microstructure proxies |
| Outcome variables | Net debt issuance, debt issuance response to financing deficits, leverage, change in leverage |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between asymmetric information and leverage is not causal because firms with high adverse selection may differ systematically from other firms. They may be smaller, riskier, less liquid, less profitable, more financially constrained, or more reliant on external finance. Reverse causality is also possible because capital structure choices could affect stock liquidity and information production. Measurement error is another issue because microstructure measures may capture inventory risk, volatility, or liquidity effects rather than pure adverse selection.

### Identification Approach
- Natural experiment: None.
- Instrument: None.
- Difference in differences: None.
- Event study: None.
- Fixed effects: Firm fixed effects in conventional leverage regressions.
- Matching: None.
- Placebo tests: Not a formal placebo design, but the paper uses many robustness and two-way sort tests.
- Robustness: Alternative index construction, individual adverse selection proxies, subperiods, controls for size, tangibility, Q, profitability, volatility, turnover, and insider trading.
- Alternative source of variation: Uses both the level of adverse selection and year-on-year changes in adverse selection.

### Is the Identification Convincing?
- Strength: The paper improves on prior capital structure tests by measuring the pecking order's core friction directly, rather than proxying information asymmetry with size, tangibility, or growth opportunities.
- Weakness: It is not a clean causal design. The index may still capture correlated liquidity, risk, or omitted firm characteristics.
- Referee concern: The main concern is whether market microstructure adverse selection is really the same friction as managerial private information in Myers and Majluf.

## 8. Main Regression or Model

```text
Delta Debt_it = alpha + beta DEF_it + epsilon_it
```

This is the Shyam-Sunder and Myers-style debt-deficit regression. Delta Debt is net debt issuance, and DEF is the financing deficit, defined as dividends plus capital expenditures plus change in working capital minus cash flow. A strict pecking order predicts beta close to one.

The paper's key conditional version is:

```text
Delta Debt_it =
  alpha
+ beta DEF_it
+ gamma DEF_it x ASY_it
+ epsilon_it
```

Here, gamma is the key coefficient. A positive gamma means firms with higher adverse selection use more debt to fund financing deficits.

The conventional leverage regression is:

```text
Leverage_it =
  alpha
+ b1 ASY_it
+ b2 Tangibility_it
+ b3 Q_it
+ b4 LogSales_it
+ b5 Profitability_it
+ Firm FE
+ epsilon_it
```

The change specification is:

```text
Delta Leverage_it =
  alpha
+ b1 Delta ASY_it
+ b2 Delta Tangibility_it
+ b3 Delta Q_it
+ b4 Delta LogSales_it
+ b5 Delta Profitability_it
+ b6 Leverage_i,t-1
+ Firm FE
+ epsilon_it
```

The main economic interpretation is carried by gamma in the debt-deficit model and b1 in the leverage models. Positive estimates mean adverse selection is associated with more debt financing, consistent with the modified pecking order.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Capital Structure]] by testing whether information asymmetry is actually related to financing choices.
2. [[Pecking Order Theory]] by showing that the theory performs better when adverse selection is high.
3. [[Market Microstructure]] by importing adverse selection measures into corporate finance.
4. [[Empirical Corporate Finance]] by using a time-varying, market-based measure of information asymmetry rather than static firm characteristics.

It differs from prior work because it does not simply ask whether all firms follow the pecking order on average. It asks whether firms follow the pecking order more closely when the theory's key assumption holds.

## 10. Closely Related Papers
- [[Myers and Majluf 1984]]: The theoretical foundation for adverse selection and equity issuance costs.
- [[Myers 1984]]: Introduces the pecking order theory of capital structure.
- [[Shyam-Sunder and Myers 1999]]: Provides the classic debt-deficit regression test of the pecking order.
- [[Frank and Goyal 2003]]: Shows that the pecking order performs poorly in broad samples, especially as equity issuance becomes common.
- [[Fama and French 2002]]: Tests tradeoff and pecking order predictions for dividends and debt.
- [[Rajan and Zingales 1995]]: Provides conventional leverage regressions using size, tangibility, profitability, and market-to-book.
- [[Leary and Roberts 2004]]: Tests financing hierarchies and financial slack, finding limited support for pecking order behavior.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on capital structure. Discuss the evidence for and against the pecking order theory.

How to use this paper:
- Main finding: Firms with more adverse selection behave more like pecking order firms.
- Data: U.S. firm-year panel from COMPUSTAT and CRSP, with microstructure-based adverse selection measures.
- Identification: Not a natural experiment, but strong cross-sectional conditioning on theory-based, time-varying adverse selection.
- Limitation: The information asymmetry measure may still capture liquidity or risk, and causal interpretation is limited.
- Connection to other papers: Reconciles [[Shyam-Sunder and Myers 1999]] with [[Frank and Goyal 2003]] by arguing that pecking order evidence is conditional.
- Best exam phrase: "Bharath, Pasquariello, and Wu show that the pecking order works where it should work, among firms with high adverse selection."

## 12. Hypotheses Inspired by This Paper
H1: Firms with greater adverse selection will fund a larger share of financing deficits with debt rather than equity.

H2: Increases in adverse selection will lead firms to increase debt reliance in the following fiscal year.

H3: The effect of adverse selection on debt financing will be stronger for low-Q firms because their value depends more on assets in place, making equity more vulnerable to undervaluation.

## 13. Possible Extension or Research Design
- Research question: Does an exogenous improvement in firms' information environments reduce their reliance on debt financing?
- Hypothesis: Firms experiencing a reduction in information asymmetry will use less debt and more equity to fund financing deficits.
- Data: U.S. public firms around an information disclosure shock such as XBRL adoption, Reg FD, analyst coverage shocks, EDGAR dissemination changes, or brokerage closures.
- Identification: Difference in differences comparing opaque treated firms to less affected control firms before and after the information environment shock.
- Expected result: Treated firms should show lower debt-deficit sensitivity after information asymmetry falls.
- Contribution: This would add causal evidence to Bharath, Pasquariello, and Wu by moving from market-based conditioning to quasi-exogenous variation in information asymmetry.

## 14. Critiques

### Major Concern 1
The paper is not causally identified. Firms with high adverse selection may differ in unobserved ways that also affect capital structure, such as financial constraints, debt capacity, asset risk, or investment opportunities.

### Major Concern 2
The adverse selection index may capture liquidity, volatility, inventory risk, or trading frictions rather than managerial private information. The authors address this with controls and robustness tests, but the measurement concern cannot be eliminated entirely.

### Minor Concern
The interpretation of the 1990s evidence is complicated because equity issuance became much more common during that period, weakening the strict pecking order benchmark.

### Referee Recommendation
Accept, because the paper provides a clear conceptual advance, a novel measure, and extensive robustness. The causal claim should be framed carefully as evidence that adverse selection helps explain capital structure, not definitive proof that it exogenously causes capital structure choices.

## 15. Memory Hooks
- "30 cents": high adverse selection firms issue about 30 cents more debt per dollar of financing deficit.
- "Pecking order works where it should": the theory performs best when adverse selection is high.
- "Microstructure meets corporate finance": adverse selection is measured from trading and liquidity data, not firm size.
- "Strict no, modified yes": strict pecking order fails, conditional pecking order survives.
- "Low Q stronger": the effect is strongest when assets in place dominate growth opportunities.

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Capital Structure]], [[Pecking Order Theory]], [[Information Asymmetry]], or [[Market Microstructure]]. The clean exam answer is: "Bharath, Pasquariello, and Wu use market microstructure measures of adverse selection to show that firms with higher information asymmetry finance more of their deficits with debt." Use it to argue that the pecking order should be evaluated as a conditional theory, not as a universal description of all firms. In a critique answer, emphasize that the design is not a natural experiment, but note that the paper is stronger than a standard correlation because it measures adverse selection directly, uses firm fixed effects, tests changes in adverse selection, and shows robustness across many alternative specifications.