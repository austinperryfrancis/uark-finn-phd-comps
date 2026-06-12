---
type: paper
status: unread
title: International Asset Pricing with Strategic Business Groups
authors: Massimo Massa, James O'Donovan, Hong Zhang
year: 2022
journal: Journal of Financial Economics
professor: DrJandik
seminar: null
jandik_paper_number: 27
jandik_week: 7
jandik_topic: Networks, internal capital markets, and diversification
jandik_done: true
field: Asset Pricing
literature:
- International Asset Pricing
- '[[Internal Capital Markets]]'
- Ownership Structure
methods:
- Fama-MacBeth regressions
- portfolio sorts
- Bayesian asset pricing tests
- Sharpe ratio model comparison
- shock sensitivity tests
datasets:
- Orbis
- Bureau van Dijk
- Datastream/Worldscope
- '[[Compustat]]'
- FactSet Fundamentals
- sovereign ratings
identification: Industry shocks, commodity shocks, and sovereign downgrade shocks combined with centrality variation within business groups
main_result: Central firms in business groups are protected in bad times, earn lower expected returns, and generate a centrality factor that improves international asset pricing models.
exam_relevance: high
must_memorize: true
tags:
- international-asset-pricing
- business-groups
- ownership-structure
- internal-capital-markets
- risk-sharing
- factor-models
- corporate-finance
created: 2026-06-05
updated: 2026-06-05
---

# Massa, O'Donovan, and Zhang 2022

## 1. One-Sentence Takeaway
This paper shows that strategic business groups protect central firms in bad times using internal risk and resource reallocation, and the main contribution is a new international asset pricing factor based on firm centrality within ownership networks.

## 2. Exam-Ready Abstract
Massa, O'Donovan, and Zhang ask whether business group ownership changes the cross section of international stock returns. The paper argues that ultimate owners of business groups care especially about firms that are central to retaining control over the group, so they reallocate resources toward those firms when bad states threaten control. Using worldwide ownership data from Orbis for 2002 to 2012, the authors construct a firm-level centrality measure equal to the fraction of group value the owner would lose if control of that firm were lost. They show that central firms are less sensitive to negative industry shocks, commodity shocks, and exogenous sovereign downgrade shocks. Central firms also earn lower future returns, and central minus peripheral portfolio sorts generate significant negative alphas after standard international factors. The paper then shows that a centrality factor improves model performance in Barillas-Shanken style Bayesian asset pricing tests and squared Sharpe ratio comparisons. This connects to [[International Asset Pricing]], [[Business Groups]], [[Internal Capital Markets]], and [[Ownership Structure]].

## 3. Research Question
What is the paper trying to answer?

Does the strategic behavior of business groups create a distinct international asset pricing factor beyond standard US-based factor models?

More specifically: what mechanism, heterogeneity, or causal channel does the paper test?

The mechanism is that ultimate owners of business groups strategically protect firms that are central to group control. Central firms receive implicit insurance in bad states because losing them would cause the owner to lose control over a large share of group assets. This lowers central firms' risk premium and induces common movement among central firms, generating a centrality-based intertemporal risk factor.

## 4. Core Mechanism
Use a chain that can be memorized for comps:

```text
Bad economic state or financing shock
-> central firm becomes more vulnerable
-> loss of central firm threatens control of the entire business group
-> ultimate owner reallocates resources and risk within the group
-> central firms are protected, peripheral firms bear more risk
-> central firms earn lower expected returns
-> centrality factor helps price international stocks
```

## 5. Main Findings
1. Central firms are less exposed to bad shocks. Centrality offsets part of the adverse valuation effect of negative industry and commodity shocks, and central firms are insulated from sovereign downgrade shocks.
2. Centrality predicts lower future returns. In Fama-MacBeth regressions, a one standard deviation increase in centrality predicts about 14 bps lower monthly raw returns and 12 bps lower monthly DGTW-adjusted returns.
3. High-centrality portfolios earn lower risk-adjusted returns than low-centrality portfolios. The high-minus-low centrality spread is about -67 bps per month in the overall sort and -36 bps per month in the between-group sort after four-factor adjustment.
4. A central minus peripheral factor improves international factor models. Bayesian model comparison and squared Sharpe ratio tests favor models that include the centrality factor.
5. The effect appears to be about group-control protection rather than tunneling. E1 top firms show related effects, but E2 apex or extractor firms do not predict returns significantly.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Firm-year for ownership and shock tests; firm-month for return predictability; portfolio-month for factor tests |
| Sample period | Mainly 2002 to 2012 |
| Main dataset | Orbis ownership data from Bureau van Dijk, plus Datastream/Worldscope, Compustat, and WRDS FactSet Fundamentals |
| Key variables | Centrality, E1 top firm dummy, E2 apex/extractor dummy, returns, DGTW-adjusted returns, market-to-book, leverage, size, book-to-market, momentum |
| Treatment or shock | Negative industry shocks, commodity shocks, sovereign downgrade shocks |
| Outcome variables | Market-to-book, idiosyncratic returns, annual returns around downgrades, monthly stock returns, DGTW-adjusted returns, portfolio alphas, idiosyncratic volatility |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between centrality and returns is not causal because central firms are not randomly assigned. Central firms are larger, older, more visible, and potentially different in profitability, risk, political connections, financing access, industry exposure, or governance quality. Business groups may choose central firms precisely because they are safer or more important ex ante. There is also equilibrium sorting: firms with lower risk or lower expected returns may be placed in central control positions. Finally, measured centrality could proxy for omitted ownership characteristics, size, liquidity, or tunneling incentives rather than strategic protection.

### Identification Approach
- Natural experiment: Sovereign downgrades create plausibly exogenous financing shocks for firms whose ratings are bound by the sovereign ceiling.
- Instrument: None.
- Difference in differences: The sovereign downgrade test compares bound versus non-bound firms around downgrade events.
- Event study: Not a classic event-study design, but downgrade timing provides shock-based variation.
- Fixed effects: Firm, time, country, industry, group, and year fixed effects are used across specifications.
- Matching: Not central to the main design.
- Placebo tests: E2 apex or extractor firms serve as a placebo for tunneling or cash-flow-rights explanations.
- Robustness: Controls for size, book-to-market, momentum, lagged returns, leverage, group characteristics, funding liquidity proxies, VIX, default spread, intermediary capital risk, and alternative centrality measures.
- Alternative source of variation: Industry ROA shocks, commodity shocks, and cross-sectional centrality portfolio sorts.

### Is the Identification Convincing?
- Strength: The paper combines mechanism tests, cross-sectional return predictability, shock-based evidence, and factor model tests. The sovereign downgrade triple-difference test is the cleanest causal evidence.
- Weakness: Centrality is still an endogenous network position, and the asset pricing tests show priced covariance rather than fully causal reallocation.
- Referee concern: The main concern is whether centrality proxies for size, liquidity, investor attention, political connections, country governance, or latent safety rather than strategic group protection.

## 8. Main Regression or Model

```text
MB_it =
  beta1 NegShock_it
+ beta2 Centrality_it
+ beta3 Centrality_it x NegShock_it
+ Controls_it
+ Firm FE
+ Time FE
+ epsilon_it
```

This regression tests whether central firms are less harmed by negative industry shocks. The key coefficient is beta3. A negative beta3 means central firms' valuations fall less when the industry experiences a bad shock, consistent with protection by the business group.

```text
Return_it =
  beta Centrality_i,t-1
+ gamma Controls_i,t-1
+ epsilon_it
```

This Fama-MacBeth regression tests whether centrality predicts future stock returns. The paper finds beta is negative, meaning central firms earn lower expected returns.

```text
Return_it =
  beta1 Bound_i x Downgrade_t
+ beta2 Centrality_i x Bound_i x Downgrade_t
+ Controls_it
+ Year FE
+ Country FE
+ Business Group FE
+ epsilon_it
```

This triple-difference specification tests whether centrality mitigates the negative effect of sovereign downgrade shocks on firms bound by the sovereign ceiling. beta1 captures the negative effect of being bound during a downgrade. beta2 is the key coefficient: a positive beta2 means central firms are protected from the shock.

```text
CMP_t = Return_high-centrality,t - Return_low-centrality,t
```

The centrality factor is a central minus peripheral mimicking portfolio. Since high-centrality firms earn lower returns, the high-minus-low portfolio has a negative alpha relative to standard factors.

## 9. Contribution to the Literature
This paper contributes to:
1. [[International Asset Pricing]] by showing that global ownership structures can create risk factors not captured by standard US-based factor models.
2. [[Business Groups]] by moving beyond internal capital markets and tunneling to show asset pricing implications of strategic risk reallocation.
3. [[Ownership Structure]] by using network centrality to measure the importance of a firm for retaining group control.
4. [[Intertemporal CAPM]] by proposing that business group behavior changes investors' opportunity set and creates a new intertemporal risk factor.

It differs from prior work because it treats business groups not only as governance or tunneling structures, but as strategic risk allocators that can alter the cross section of expected returns.

## 10. Closely Related Papers
- [[Merton 1973]]: Intertemporal CAPM logic. State variables affect investment opportunities and generate hedging demand.
- [[Bertrand, Mehta, and Mullainathan 2002]]: Tunneling in business groups and internal transfer of resources.
- [[Almeida and Wolfenzon 2006]]: Theory of pyramidal ownership and why business groups exist.
- [[Almeida et al. 2011]]: Business group structure and centrality in Korean chaebol.
- [[Aminadav and Papaioannou 2020]]: Corporate control around the world and ownership network measurement.
- [[Fama and French 2012]]: International factor models used as benchmarks.
- [[Barillas and Shanken 2018]]: Bayesian comparison of asset pricing models.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on international asset pricing. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Business group centrality predicts lower expected returns and creates a factor that improves international asset pricing models.
- Data: Worldwide ownership data from Orbis for 2002 to 2012, matched to accounting and stock return data.
- Identification: Uses centrality within ownership networks plus industry shocks, commodity shocks, and sovereign downgrade shocks.
- Limitation: Centrality is endogenous and may proxy for other firm characteristics, though the paper addresses this with controls, fixed effects, and placebo tests.
- Connection to other papers: Use with Merton 1973 for ICAPM, Almeida and Wolfenzon for pyramids, Bertrand et al. for tunneling, and Fama-French international factor models.
- Best exam phrase: "Massa, O'Donovan, and Zhang show that ownership structure itself can be a priced state variable in international markets."

## 12. Hypotheses Inspired by This Paper
H1: Firms that are more central to business group control have lower downside beta during bad aggregate states than peripheral affiliated firms.

H2: The centrality discount should be stronger in countries with weaker investor protection because ultimate owners have more discretion to reallocate resources within the group.

H3: The centrality factor should be stronger during periods of financial distress, high VIX, high default spreads, or constrained intermediary capital.

## 13. Possible Extension or Research Design
- Research question: Does centrality within global supply-chain networks have similar asset pricing effects to centrality within ownership networks?
- Hypothesis: Firms that are central to a buyer-supplier network receive implicit support or priority during disruptions and earn lower expected returns if investors price that protection.
- Data: FactSet Revere supply-chain links, Compustat Global, Orbis ownership data, Datastream returns, sanctions or shipping disruption shocks.
- Identification: Difference-in-differences around exogenous supply-chain shocks, comparing central versus peripheral firms within the same industry and country.
- Expected result: Central firms in critical network positions experience smaller negative shock responses and lower future expected returns.
- Contribution: Extends the paper from ownership networks to real production networks and connects [[Supply Chains]] to [[Asset Pricing]].

## 14. Critiques

### Major Concern 1
Centrality is endogenous. Ultimate owners may place safer, larger, more profitable, or more liquid firms in central positions. The paper controls for many observables, but unobserved safety or governance quality could still explain lower expected returns.

### Major Concern 2
The paper infers strategic reallocation rather than observing transfers directly. The shock evidence is consistent with protection, but the paper does not directly show the internal capital movement from peripheral to central firms.

### Minor Concern
The sample is international and excludes the US emphasis, which is appropriate for the question, but it also raises concerns about data quality, accounting comparability, ownership reporting differences, and country-level institutional heterogeneity.

### Referee Recommendation
Accept, because the paper identifies a novel and economically meaningful international asset pricing channel, uses a large ownership network dataset, and triangulates the mechanism with shocks, return predictability, portfolio sorts, and model comparison. The key caveat is that the strongest interpretation requires accepting that centrality captures strategic protection rather than unobserved safety.

## 15. Memory Hooks
- "Central firms are the control keystones."
- "Bad times make groups protect the firms they cannot afford to lose."
- "Centrality equals counterfactual loss of group value if control is lost."
- "Central firms are safer, so they earn lower expected returns."
- "CMP is an ownership-network ICAPM factor."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[International Asset Pricing]], [[Business Groups]], [[Internal Capital Markets]], [[Ownership Structure]], or [[Intertemporal CAPM]]. The clean exam answer is: "Massa, O'Donovan, and Zhang use worldwide ownership networks to measure centrality within business groups and show that central firms are protected in bad states, earn lower expected returns, and generate a centrality factor that improves international asset pricing models." Use it to argue that international asset pricing differs from US asset pricing because firms outside the US are often embedded in ownership groups that strategically reallocate resources and risk. In a critique answer, emphasize that centrality is endogenous and internal transfers are not directly observed, but note that the paper is stronger than a standard correlation because it combines shock tests, sovereign downgrade variation, portfolio sorts, alternative factor models, and placebo tests using apex or extractor firms.