---
type: paper
status: unread
title: Firm-Level Climate Change Exposure
authors: Zacharias Sautner, Laurence van Lent, Grigory Vilkov, Ruishen Zhang
year: 2023
journal: Journal of Finance
seminar:
field: climate finance
literature: climate risk, textual analysis, green innovation, asset pricing
methods: machine learning keyword discovery, earnings call textual analysis, Poisson regressions, variance decomposition, option-implied risk tests, conditional asset pricing
datasets: Refinitiv Eikon earnings call transcripts, S&P Global Trucost, Wall Street Journal climate attention index, Burning Glass green jobs, Google Patents, OptionMetrics, Compustat, Ken French factors
identification: predictive panel regressions with controls and fixed effects; validation design rather than clean causal shock
main_result: Firm-level climate change exposure measured from earnings calls predicts green-tech hiring, green patenting, option-implied tail risk, and conditional equity risk premia.
exam_relevance: high
must_memorize: true
tags:
  - climate-finance
  - textual-analysis
  - green-innovation
  - asset-pricing
  - options
  - machine-learning
  - DrJandik
created: 2026-06-12
updated: 2026-06-12
---

# Sautner et al. 2023

## 1. One-Sentence Takeaway
This paper shows that firm-level climate change exposure can be measured from earnings calls using machine-learning keyword discovery, and the main contribution is a global, disaggregated measure of climate opportunities, regulatory exposure, and physical exposure that predicts green innovation and is priced in options and equity markets.

## 2. Exam-Ready Abstract
Sautner et al. ask how to measure firm-level climate change exposure when climate risk is multidimensional and not captured well by emissions alone. They use English-language earnings call transcripts for more than 10,000 firms in 34 countries from 2002 to 2020 and construct exposure measures based on climate-related bigrams discovered by adapting the King, Lam, and Roberts keyword discovery algorithm. The measures capture overall climate exposure plus three topics: opportunities, regulatory shocks, and physical shocks. The authors validate the measure using face validity of bigrams, a human audit of transcript snippets, correlations with emissions and public climate attention, and a variance decomposition showing most variation is firm-level rather than just industry or country variation. They show that higher exposure predicts more green-tech hiring and more green patents in the next year, especially through opportunity and regulatory exposure. They also show that exposure is related to option-implied tail risk and variance risk premia, and that an aggregate climate exposure factor earns a conditional risk premium. This paper connects to [[Climate Finance]], [[Textual Analysis]], [[Green Innovation]], and [[Asset Pricing]].

## 3. Research Question
What is the paper trying to answer?

How can researchers measure firm-level climate change exposure in a way that captures market participants' attention to climate opportunities, regulatory shocks, and physical shocks?

More specifically: do textual measures of climate exposure from earnings calls contain economically meaningful information about real firm responses, such as green hiring and green patenting, and financial market pricing, such as options and equity risk premia?

## 4. Core Mechanism

```text
Climate change becomes economically salient
-> managers and analysts discuss climate topics in earnings calls
-> textual climate exposure measure captures perceived firm-level exposure
-> firms with opportunity or regulatory exposure shift resources toward green technologies
-> markets price the resulting uncertainty through options and expected returns
```

## 5. Main Findings
1. The paper constructs firm-level climate exposure from earnings call bigrams, including overall exposure, opportunity exposure, regulatory exposure, and physical exposure.
2. Most variation is firm-level: 69.7% of overall exposure, 79.1% of opportunity exposure, 89.9% of regulatory exposure, and 96.2% of physical exposure is not explained by year, industry, industry-year, or country fixed effects.
3. A one-standard-deviation increase in overall climate exposure predicts a 109% increase in green-tech jobs and a 72% increase in green patents over the following year.
4. The real effects are mainly driven by opportunity and regulatory exposure, not physical exposure.
5. The measures are priced in options markets: high-exposure firms have more expensive tail protection and upside exposure, and a climate exposure factor earns a conditional equity risk premium.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Primarily firm-year for real outcomes; firm-quarter for option-implied outcomes; monthly for equity factor tests |
| Sample period | 2002 to 2020 for earnings call measures |
| Main dataset | Refinitiv Eikon English-language earnings call transcripts |
| Coverage | 86,152 firm-year observations, 10,673 firms, 34 countries |
| Key variables | CCExposure, CCExposureOpp, CCExposureReg, CCExposurePhy |
| Treatment or shock | Not a clean treatment. Main variation is measured attention to climate exposure in earnings calls |
| Outcome variables | Green-tech jobs, green patents, nongreen tech jobs, nongreen patents, option-implied variance, skewness, kurtosis, implied volatility slopes, variance risk premium, stock returns |
| Other datasets | S&P Global Trucost emissions, WSJ climate attention index from Engle et al., Burning Glass jobs, Google Patents, OptionMetrics, Compustat, Ken French factors |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between climate exposure and green outcomes is not automatically causal. Firms that talk about climate change may already be greener, larger, more innovative, more regulated, or more likely to be covered by analysts. Managers may strategically discuss climate change to distract from poor performance. Reverse causality is also possible: firms planning green jobs or green patents may talk more about climate because they are already innovating. Measurement error is another concern because textual measures may capture noise, boilerplate, investor relations language, or general energy discussion rather than true climate exposure.

### Identification Approach
- Natural experiment: None. This is mainly a measurement and predictive-validity paper, not a clean causal shock paper.
- Instrument: For measurement error, they use alternative 10-K MD&A climate exposure measures and lags as instruments to estimate the share of measurement error.
- Difference in differences: None in the main tests.
- Event study: Not central in the paper.
- Fixed effects: Industry-year fixed effects in green jobs and green patents regressions; firm-level variance decomposition; options tests include controls and industry-time structure.
- Matching: Patent assignees are matched to firms by name; Trucost emissions are matched using GVKEYs, ISINs, names, fuzzy names, and tickers.
- Placebo tests: Green exposure predicts green jobs and green patents but does not simply predict nongreen tech hiring or nongreen patenting.
- Robustness: Alternative specifications, Q&A-only exposure, TFIDF versions, controlling for emissions, initial-bigram-zero subsamples, human audit of transcript snippets.
- Alternative source of variation: Topic-specific measures separate opportunity, regulatory, and physical exposure.

### Is the Identification Convincing?
- Strength: Very strong as a measurement paper. The measure is validated through human audit, industry patterns, emissions correlations, public climate attention, green jobs, green patents, and option market pricing.
- Weakness: The real-outcome regressions are predictive associations, not causal estimates of climate exposure on innovation.
- Referee concern: Managers may strategically disclose climate talk, and omitted firm characteristics may drive both climate discussions and green innovation. The authors address this partly with controls, fixed effects, sentiment/performance controls, and placebo outcomes, but it remains a limitation for causal interpretation.

## 8. Main Regression or Model

Green outcome prediction:

```text
GreenOutcome_{i,t+1}
= exp(
    alpha_i
  + beta log(1 + CCExposure_{i,t})
  + gamma X_{i,t}
  + Industry x Year FE
  + epsilon_{i,t+1}
)
```

The dependent variable is next-year green-tech jobs or green patents. The key coefficient is beta. It captures whether firms with more climate discussion in year t have more green hiring or patenting in year t+1, conditional on firm controls and industry-year shocks. The main interpretation is predictive, not strictly causal.

Topic heterogeneity:

```text
GreenOutcome_{i,t+1}
= exp(
    alpha_i
  + beta1 log(1 + CCExposureOpp_{i,t})
  + beta2 log(1 + CCExposureReg_{i,t})
  + beta3 log(1 + CCExposurePhy_{i,t})
  + gamma X_{i,t}
  + Industry x Year FE
  + epsilon_{i,t+1}
)
```

Here beta1 captures climate opportunities, beta2 captures regulatory exposure, and beta3 captures physical exposure. The main economic result is that opportunity and regulatory exposure predict green jobs and green patents, while physical exposure is weaker.

Options-market regression:

```text
OptionOutcome_{i,t+1}
= alpha_i
+ beta log(1 + CCExposure_{i,t})
+ gamma X_{i,t}
+ Industry x Time FE
+ epsilon_{i,t+1}
```

The dependent variable is an option-implied measure such as implied skewness, implied kurtosis, downside slope, upside slope, or variance risk premium. Beta captures whether markets price climate-related uncertainty into option prices.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Climate Finance]] by creating firm-level measures of climate exposure that are broader than emissions.
2. [[Textual Analysis]] by applying machine-learning keyword discovery to earnings calls and specialized climate language.
3. [[Green Innovation]] by showing that climate exposure predicts green-tech hiring and green patents.
4. [[Asset Pricing]] by linking climate exposure to option-implied risk and conditional equity risk premia.

It differs from prior work because it measures firm-level climate exposure globally, separates opportunity, regulatory, and physical channels, and emphasizes soft information in earnings calls rather than only hard data such as emissions, weather events, or location.

## 10. Closely Related Papers
- [[Hassan et al. 2019]]: Measures firm-level political risk from earnings calls; methodological ancestor.
- [[Engle et al. 2020]]: Measures aggregate climate news attention; related climate attention index.
- [[Ilhan, Sautner, and Vilkov 2021]]: Carbon tail risk in options markets; closely related option-pricing channel.
- [[Bolton and Kacperczyk 2021]]: Carbon emissions and expected returns; hard-information climate pricing benchmark.
- [[Li et al. 2021]]: Earnings-call climate risk measurement; narrower U.S. focus on physical and regulatory risks.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on climate finance. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Earnings-call climate exposure predicts green innovation and is priced in financial markets.
- Data: Global earnings calls from Refinitiv Eikon, plus Burning Glass green jobs, Google Patents, OptionMetrics, Trucost, and Compustat.
- Identification: Not a clean causal design. Use it as a measurement and predictive-validity paper with strong validation and fixed-effect controls.
- Limitation: Climate talk may be endogenous to firm strategy, disclosure incentives, and investor attention.
- Connection to other papers: Pair with [[Bolton and Kacperczyk 2021]] for emissions-based climate pricing, [[Ilhan, Sautner, and Vilkov 2021]] for option pricing, and [[Hassan et al. 2019]] for earnings-call textual measurement.
- Best exam phrase: "Sautner et al. move climate finance from aggregate or emissions-based measures to a firm-level, multidimensional, text-based measure of perceived climate exposure."

## 12. Hypotheses Inspired by This Paper
H1: Firms with higher climate opportunity exposure increase green capex, green hiring, and green patenting relative to firms in the same industry-year.

H2: Firms with higher regulatory exposure face higher option-implied tail risk because investors price uncertainty about future climate regulation.

H3: Physical climate exposure is more strongly associated with risk management, insurance, supply-chain relocation, and disclosure than with green innovation.

## 13. Possible Extension or Research Design
- Research question: Does climate exposure propagate through customer-supplier networks?
- Hypothesis: A firm's climate exposure increases the climate disclosure, green hiring, and supplier-switching behavior of its major customers and suppliers.
- Data: Sautner et al. climate exposure measures, FactSet Revere customer-supplier links, Compustat, earnings calls, patent data, job postings.
- Identification: Use supplier-level climate exposure shocks interacted with preexisting network links, with firm fixed effects, year fixed effects, industry-year fixed effects, and placebo tests using nonlinked firms.
- Expected result: Customers and suppliers linked to high-exposure firms adjust their own green innovation and disclosure more strongly after exposure increases.
- Contribution: Connects [[Climate Finance]] to [[Supply Chains]], [[Network Propagation]], and [[Real Effects of Disclosure]].

## 14. Critiques

### Major Concern 1
The main real-outcome tests are not causal. Climate-exposed firms may already be planning green innovation, and earnings-call discussion may simply reveal preexisting strategy.

### Major Concern 2
The measure captures attention or perceived exposure, not fundamental exposure. That is useful for markets, but it may conflate climate fundamentals with analyst attention, disclosure strategy, and investor demand for climate narratives.

### Minor Concern
The measure relies on English-language earnings calls, so international coverage may be biased toward firms with better disclosure, larger analyst following, or more global capital-market presence.

### Referee Recommendation
Accept, because the paper makes a major measurement contribution, validates the measure carefully, and demonstrates usefulness across real and financial outcomes. The main caveat is that the paper should be framed as measurement and predictive validity rather than causal evidence that climate exposure causes green innovation.

## 15. Memory Hooks
- "Climate exposure from earnings calls, not emissions."
- "Four measures: overall, opportunity, regulation, physical."
- "109% more green jobs, 72% more green patents."
- "Most variation is firm-level, not just industry climate risk."
- "Good for measurement, textual analysis, and climate asset pricing comps."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Climate Finance]], [[Textual Analysis]], [[Green Innovation]], [[Options Markets]], or [[Asset Pricing]]. The clean exam answer is: "Sautner et al. use earnings-call transcripts to construct firm-level climate exposure measures and show that these measures predict green-tech hiring, green patenting, and financial market pricing of climate uncertainty." Use it to argue that climate risk is multidimensional and firm-specific, not just an emissions or industry-level phenomenon. In a critique answer, emphasize that the paper is not a clean causal design, but note that it is stronger than a standard correlation because it validates the text measure through human audit, variance decomposition, placebo outcomes, robustness to alternative specifications, and links to both real and market outcomes.