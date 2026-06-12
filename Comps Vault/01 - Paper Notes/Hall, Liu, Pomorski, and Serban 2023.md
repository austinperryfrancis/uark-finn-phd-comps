---
type: paper
status: unread
title: Supply Chain Climate Exposure
authors: Greg Hall; Kate Liu; Lukasz Pomorski; Laura Serban
year: 2023
journal: Financial Analysts Journal
seminar: Not clear from provided text
field: Asset Pricing; Climate Finance; Sustainable Finance
literature: Climate Finance; ESG Measurement; Supply Chain Networks; Carbon Risk
methods: Measurement; Portfolio Sorts; Event Study; Fama-MacBeth; Factor Regressions
datasets: Supply chain vendor data; Trucost; MSCI ESG; XpressFeed; MCCC climate news sentiment; Ken French factors; AQR factors
identification: Validation using climate news sentiment, climate event studies, industry and country neutral portfolios, and orthogonalization to traditional climate metrics
main_result: A revenue-weighted measure of customers' climate exposure captures climate-related stock return co-movement and predicts green-minus-brown portfolio performance better than traditional emissions metrics.
exam_relevance: high
must_memorize: true
tags:
  - climate-finance
  - esg
  - supply-chains
  - asset-pricing
  - carbon-risk
  - scope-3
  - measurement
  - DrJandik
created: 2026-06-12
updated: 2026-06-12
---

# Hall, Liu, Pomorski, and Serban 2023

## 1. One-Sentence Takeaway
This paper shows that firms can have material climate risk through their customers and suppliers using a revenue-weighted customer climate exposure measure, and the main contribution is to shift climate-risk measurement from a firm's own emissions to its economically linked supply chain.

## 2. Exam-Ready Abstract
Hall, Liu, Pomorski, and Serban ask whether traditional carbon metrics miss climate exposure that comes through supply chain relationships. They argue that even a "green" firm can be exposed to climate risk if it derives substantial revenue from carbon-intensive customers. Their main measure is downstream supply chain climate exposure, defined as the revenue-weighted average of customers' Scope 1 + 2 carbon intensity. Using large-cap developed-market stocks from May 2009 to December 2021, supply chain linkage data, Trucost emissions, MSCI ESG metrics, XpressFeed financials, and climate news sentiment, they validate the measure against traditional emissions data, climate news, event studies, portfolio returns, and earnings or sales surprises. The measure is correlated with but distinct from Scope 1, 2, and 3 emissions, and long-short portfolios based on greener downstream exposure earn strong abnormal returns that are not explained by standard factor models. The paper is not a clean causal shock paper, but it is exam-useful as a measurement and validation paper showing that climate risk can propagate through production networks. It connects to [[Climate Finance]], [[ESG Measurement]], [[Supply Chain Networks]], and [[Asset Pricing Anomalies]].

## 3. Research Question
What is the paper trying to answer?

Can investors measure a firm's climate risk more accurately by incorporating the climate exposure of its customers and suppliers, rather than relying only on the firm's own emissions or Scope 3 emissions?

More specifically: what mechanism, heterogeneity, or causal channel does the paper test?

The paper tests whether climate risk is transmitted through economic linkages. The downstream mechanism is that firms with revenue exposure to carbon-intensive customers are indirectly exposed to climate transition risk, demand disruption, regulatory pressure, and repricing when climate news arrives. The upstream analogue is that firms relying on carbon-intensive suppliers may face disruption or cost shocks if those suppliers are affected by climate risk.

## 4. Core Mechanism
Use a chain that can be memorized for comps:

```text
Climate news, transition risk, or physical climate risk
-> carbon-intensive customers face valuation, demand, or regulatory pressure
-> supplier firms with revenue exposure to those customers inherit indirect climate risk
-> investors reprice those supplier firms or fundamentals deteriorate
-> downstream supply chain climate exposure predicts returns, climate-news sensitivity, and earnings or sales surprises
```

## 5. Main Findings
1. Downstream supply chain climate exposure is correlated with traditional climate metrics, but the correlations are imperfect, so the measure captures information not contained in Scope 1, Scope 2, Scope 3, or MSCI climate scores.
2. Firms classified as greener on downstream supply chain exposure outperform browner firms when climate concerns increase. The correlation between the green-minus-brown factor and climate news sentiment is about 0.15 to 0.20.
3. Long-short portfolios based on downstream supply chain exposure earn strong historical returns, with a Sharpe ratio of about 0.85 in the broad version and above 0.7 in the country-adjusted within-industry version. The alphas remain economically large after standard factor adjustments.
4. The measure helps predict fundamentals: greener downstream exposure is associated with larger EPS surprises, and to a weaker extent sales surprises.
5. The measure is similar to Scope 3 in spirit, but it is designed for financial risk exposure rather than carbon accounting.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Firm-month or firm-quarter, depending on the test |
| Sample period | May 2009 to December 2021 for main sample; climate sentiment tests through June 2018 |
| Main dataset | Large-cap developed stocks roughly equivalent to MSCI World constituents |
| Supply chain data | Blended commercial linkage data from multiple third-party vendors using regulatory filings, earnings transcripts, company and industry publications, and news |
| Emissions data | Trucost Scope 1 + 2 carbon intensity for customers and suppliers; Scope 1, 2, and 3 comparisons |
| ESG data | MSCI E-pillar, climate change theme, and Low Carbon Transition scores |
| Financial and return data | XpressFeed, Ken French factor data, AQR factor data |
| Climate news data | Media Climate Change Concern index from Ardia et al. 2021 |
| Key variables | Downstream supply chain climate exposure, Scope 1 + 2 carbon intensity, Scope 3 emissions, climate sentiment, stock returns, EPS surprises, sales surprises |
| Treatment or shock | Not a single treatment. Main variation comes from cross-sectional exposure to carbon-intensive customers and time-series climate news or climate events |
| Outcome variables | Climate-news return sensitivity, event-study returns, long-short portfolio returns, factor-adjusted alphas, EPS surprises, sales surprises |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between supply chain climate exposure and returns is not causal because firms do not randomly choose customers. Firms with carbon-intensive customers may differ systematically in industry, country, size, value, profitability, risk, or growth opportunities. There may also be omitted variables, such as production technology, customer quality, investor clientele, or broader ESG preferences, that jointly determine supply chain exposure and returns. Reverse causality is less central because current stock returns do not mechanically determine historical customer emissions, but equilibrium sorting is important: high-emission customers may match with particular suppliers, regions, or sectors. Measurement error is also a major issue because customer-supplier linkages and revenue weights are incomplete, and missing customers may not be missing at random.

### Identification Approach
- Natural experiment: Not a clean natural experiment. The paper uses climate-related news and major climate events as validation shocks.
- Instrument: None.
- Difference in differences: None in the standard causal sense.
- Event study: Yes. The paper studies returns around macro climate news events, such as the G8 emissions-reduction declaration and the U.S. withdrawal from the Paris Agreement.
- Fixed effects: The paper uses sector and region indicators in validation regressions and constructs country-neutral and industry-neutral portfolios.
- Matching: None.
- Placebo tests: Not a formal placebo design. The closest checks are comparisons with traditional emissions metrics and orthogonalization to Scope 1, 2, 3, and MSCI Low Carbon Transition scores.
- Robustness: Industry-neutral portfolios, country-neutral portfolios, beta-neutral portfolios, factor regressions, orthogonalization to traditional climate data, alternative climate sentiment data, and fundamentals tests using EPS and sales surprises.
- Alternative source of variation: Cross-sectional variation in customer emissions weighted by revenue exposure, plus time-series changes in climate news sentiment.

### Is the Identification Convincing?
- Strength: Strong as a measurement validation paper. The measure behaves as expected around climate news and appears to contain information beyond traditional carbon metrics.
- Weakness: It does not isolate a fully exogenous shock to supply chain climate exposure, so causal claims about climate exposure causing returns should be cautious.
- Referee concern: The abnormal returns may reflect a quality, growth, or supply-chain efficiency premium rather than pure climate-risk repricing.

## 8. Main Regression or Model

The key object is the measure:

```text
Downstream Supply Chain Climate Exposure_i =
  sum_j w_ij * C_j
```

where `w_ij` is the share of firm `i`'s revenue coming from customer `j`, and `C_j` is customer `j`'s own climate exposure, usually Scope 1 + 2 carbon intensity.

The upstream analogue is:

```text
Upstream Supply Chain Climate Exposure_i =
  sum_j v_ij * C_j
```

where `v_ij` is the share of firm `i`'s supply costs or business done with supplier `j`, and `C_j` is supplier `j`'s climate exposure.

A validation regression can be summarized as:

```text
DownstreamExposure_iq =
  beta1 Scope1_iq
+ beta2 Scope2_iq
+ beta3 Scope3_iq
+ beta4 ESGScore_iq
+ Sector FE
+ Region FE
+ epsilon_iq
```

This asks whether the new measure is merely a repackaging of existing emissions and ESG data. The important result is that traditional climate measures explain some variation, but far from all of it.

The climate-news test can be summarized as:

```text
GreenMinusBrownReturn_t =
  alpha
+ gamma DeltaClimateNewsSentiment_t
+ epsilon_t
```

Here, `gamma` tests whether the green-minus-brown portfolio based on downstream exposure performs better when climate concern rises. A positive `gamma` supports the interpretation that the measure captures market-relevant climate exposure.

The fundamentals test can be summarized as:

```text
Surprise_iq =
  beta DownstreamExposure_iq
+ Controls_iq
+ epsilon_iq
```

where `Surprise_iq` is EPS or sales surprise, and controls include analyst revisions, profitability, changes in profitability, and momentum. The key coefficient is `beta`; because greener downstream exposure is coded as lower carbon exposure, the interpretation is that greener customer exposure predicts better earnings news.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Climate Finance]] by showing that climate risk can be indirect and network-based rather than limited to the firm's own emissions.
2. [[ESG Measurement]] by proposing a financially motivated alternative to Scope 3 emissions.
3. [[Supply Chain Networks]] by applying customer-supplier economic links to climate-risk propagation.
4. [[Asset Pricing]] by showing that a climate-linked supply chain characteristic predicts climate-news sensitivity and long-short portfolio returns.

It differs from prior work because it treats supply chain climate exposure as a risk measure based on economic link strength, not as carbon accounting. Scope 3 tries to assign product-related emissions; this paper asks whether a firm's cash flows and valuation are exposed to climate risk through its customers and suppliers.

## 10. Closely Related Papers
- [[Cohen and Frazzini 2008]]: Customer-supplier links predict returns because investors underreact to economically linked firms.
- [[Menzly and Ozbas 2010]]: Product market links generate cross-predictability across industries.
- [[Engle et al. 2020]]: Uses climate news to construct hedging portfolios for climate risk.
- [[Pastor, Stambaugh, and Taylor 2021]]: Green-minus-brown returns and the pricing of climate concerns.
- [[Pedersen, Fitzgibbons, and Pomorski 2021]]: ESG-efficient frontier and repricing from investor preferences or information.
- [[Kolay, Lemmon, and Tashjian 2016]]: Supply chain distress spillovers, useful analogy for climate-risk spillovers.
- [[Garvey, Iyer, and Nash 2018]]: Carbon footprint may also capture productivity or efficiency.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the literature on climate-risk measurement in asset pricing. How do researchers measure climate exposure, and what are the identification challenges?

How to use this paper:
- Main finding: Firms inherit climate exposure through customers and suppliers, and a revenue-weighted customer emissions measure captures climate-news sensitivity better than traditional emissions data.
- Data: Supply chain links, customer revenue weights, Trucost emissions, MSCI ESG, XpressFeed returns and financials, climate news sentiment.
- Identification: Not a clean causal design. The paper validates the measure using climate news, event studies, factor adjustments, industry-neutral portfolios, and orthogonalization to other climate metrics.
- Limitation: Customer links and revenue weights are incomplete; returns may reflect quality or efficiency rather than climate-risk repricing.
- Connection to other papers: Combine with [[Engle et al. 2020]] for climate hedging, [[Pastor, Stambaugh, and Taylor 2021]] for green returns, and [[Cohen and Frazzini 2008]] for supply chain return predictability.
- Best exam phrase: "Hall et al. 2023 move climate-risk measurement from the firm's own emissions to the firm's economically weighted network exposure."

## 12. Hypotheses Inspired by This Paper
H1: Firms with higher revenue exposure to carbon-intensive customers experience lower abnormal returns around negative climate-transition news.

H2: The relation between downstream climate exposure and returns is stronger when customer relationships are more concentrated, because concentrated customer exposure makes indirect climate risk more material.

H3: Firms with high upstream climate exposure experience larger cost shocks, inventory disruptions, or margin declines after climate regulation or physical climate events affecting suppliers.

## 13. Possible Extension or Research Design
- Research question: Does supply chain climate exposure predict real corporate outcomes after climate policy shocks?
- Hypothesis: Suppliers with high revenue exposure to carbon-intensive customers experience larger sales declines, investment cuts, or customer losses after transition-risk shocks.
- Data: FactSet Revere customer-supplier links, firm financials from Compustat, emissions from Trucost or MSCI, and policy shocks such as carbon-tax changes, emissions trading rule changes, or major climate regulation announcements.
- Identification: Difference-in-differences comparing firms with high versus low revenue-weighted exposure to treated carbon-intensive customers before and after a specific climate policy shock.
- Expected result: High-exposure suppliers experience lower sales growth, lower margins, and lower abnormal returns after shocks that hurt carbon-intensive customers.
- Contribution: Converts the paper's validation framework into a cleaner causal design for real effects of climate-risk propagation through supply chains.

## 14. Critiques

### Major Concern 1
The paper is not a clean causal design. Climate news and event-study evidence validate the measure, but they do not prove that downstream exposure causes returns or fundamentals. Climate exposure may proxy for unobserved quality, sector trends, customer quality, or investor preferences.

### Major Concern 2
Supply chain data are incomplete. The authors impute missing revenue weights and normalize observed links to 100%, which may introduce bias if missing customers differ systematically from observed customers. This is especially relevant for retail customers, private firms, emerging-market firms, and emissions offshoring.

### Minor Concern
The empirical implementation focuses mainly on downstream exposure. The upstream cost-weighted version is conceptually important, but not analyzed in the same depth.

### Referee Recommendation
R&R, because the paper proposes a useful, intuitive, and practitioner-relevant measure with several validation tests, but the interpretation should be disciplined: the evidence is stronger for measurement validity than for causal climate-risk pricing.

## 15. Memory Hooks
- "Green firm, brown customers."
- "Scope 3 is carbon accounting; supply chain exposure is financial risk."
- "Revenue-weight the customers' Scope 1 + 2 emissions."
- "Climate risk travels through economic links."
- "Measurement paper, not clean causal identification."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Climate Finance]], [[ESG Measurement]], [[Supply Chain Networks]], [[Scope 3 Emissions]], or [[Asset Pricing Anomalies]]. The clean exam answer is: "Hall, Liu, Pomorski, and Serban 2023 use revenue-weighted customer carbon intensity as a measure of downstream supply chain climate exposure and show that it captures climate-news return sensitivity and portfolio performance beyond traditional emissions metrics." Use it to argue that climate risk is not only a firm-level characteristic but also a network exposure transmitted through customers and suppliers. In a critique answer, emphasize that the paper is a validation and measurement paper rather than a fully causal shock design, but note that it is stronger than a standard correlation because it uses climate-news sentiment, event studies, industry and country neutral portfolios, factor adjustments, and orthogonalization to traditional climate measures.