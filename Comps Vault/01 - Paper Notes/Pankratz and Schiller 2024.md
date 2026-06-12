---
type: paper
status: unread
title: Climate Change and Adaptation in Global Supply-Chain Networks
authors: Nora M. C. Pankratz; Christoph M. Schiller
year: 2024
journal: Review of Financial Studies
professor: DrJandik
seminar: null
jandik_paper_number: 48
jandik_week: 12
jandik_topic: Climate finance
jandik_done: false
field: Climate finance; corporate finance; supply chains
literature:
- '[[Climate Finance and Supply Chains]]'
- Supply Chain Networks
- '[[Customer-Supplier Shock Propagation]]'
- Physical Climate Risk
- Experience-Based Learning
methods:
- Linear probability model
- Logit
- Cox hazard model
- High-dimensional fixed effects
- Weather shock identification
datasets:
- '[[FactSet Revere]]'
- Worldscope
- FactSet Fundamentals
- Orbis
- ECMWF ERA5
- CMIP5
- ND-GAIN
- Dartmouth Flood Observatory
identification: Supplier-location heat realizations relative to historical expectations, with supplier industry-year, customer industry-year, and supplier-country by customer-country by year fixed effects.
main_result: When supplier heat exposure exceeds historical expectations, customers are about 7% more likely to terminate the relationship and tend to choose less heat-exposed replacement suppliers.
exam_relevance: high
must_memorize: true
tags:
- climate-finance
- supply-chains
- physical-risk
- firm-adaptation
- production-networks
created: 2026-06-12
updated: 2026-06-12
---

# Pankratz and Schiller 2024

## 1. One-Sentence Takeaway
This paper shows that firms adapt global supply chains when suppliers experience unexpectedly high heat exposure using global supplier-customer links and local weather data, and the main contribution is showing that physical climate risk affects not only firm performance but also the formation and termination of production networks.

## 2. Exam-Ready Abstract
Pankratz and Schiller study whether firms learn about and adapt to physical climate risk through their supplier networks. They combine global supply-chain links from FactSet Revere with Worldscope financials, FactSet and Orbis locations, ECMWF local temperature data, CMIP5 climate projections, and ND-GAIN country adaptation readiness. The key variation is whether realized heat days at supplier locations exceed historical heat exposure measured before the supplier-customer relationship begins. They first show that heat at supplier locations reduces supplier operating performance and propagates downstream to customer operating income. Their main result is that customers are more likely to terminate supplier relationships when realized heat exposure exceeds ex ante expectations, especially when the signal is repeated, stronger, and suppliers are in lower-adaptation countries. Customers also raise inventories, cash, and R&D, and replacement suppliers have lower realized and expected heat exposure. This paper connects [[Climate Finance]], [[Supply Chain Networks]], [[Production Networks]], and [[Experience-Based Learning]].

## 3. Research Question
What is the paper trying to answer?

Do firms adjust their supply-chain relationships in response to perceived increases in suppliers' physical climate risk?

More specifically: the paper tests whether customers treat unexpectedly high supplier heat exposure as a learning signal about persistent climate risk, leading them to terminate existing supplier relationships, adjust inventories and cash, and choose less exposed replacement suppliers.

## 4. Core Mechanism

```text
Supplier location experiences more heat than historical expectations
-> supplier operating performance falls and disruptions propagate downstream
-> customer updates beliefs about supplier's persistent physical climate exposure
-> customer increases buffers and reassesses supplier relationship
-> customer terminates the supplier and selects a less exposed replacement
```

## 5. Main Findings
1. Heat exposure at supplier locations reduces supplier operating income and propagates to customers, reducing customer operating income over assets by about 0.6% relative to the mean.
2. When realized supplier heat exposure exceeds historical expectations, customers are about 7% more likely to terminate supplier relationships. The effect is stronger after the first relationship year, with repeated exceedances, and with larger deviations from priors.
3. Customers adapt on other margins: they increase inventory, COGS, R&D, and cash, show weak evidence of supplier diversification, and choose replacement suppliers with lower realized and expected heat exposure. Similar patterns hold for floods.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Supplier-customer pair-year for adaptation tests; supplier firm-quarter and customer firm-quarter for operating performance tests |
| Sample period | 2003 to 2016 for main supply-chain sample; financial data from 2000 to 2016; historical weather priors use earlier temperature data |
| Main dataset | FactSet Revere global supply-chain links |
| Key variables | Supplier heat days, realized versus expected heat exposure, relationship termination, operating income over assets, inventory, COGS, R&D, cash, supplier replacement exposure |
| Treatment or shock | Realized supplier heat days exceeding historical expected heat exposure at supplier location |
| Outcome variables | Supplier operating income, customer operating income, last relationship year, supplier diversification, inventories, cash, R&D, replacement supplier heat exposure |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between supplier heat exposure and relationship termination is not causal because firms choose suppliers and locations endogenously. Hot locations may differ systematically in labor markets, infrastructure, institutions, industry composition, or exposure to macro shocks. Customers may select suppliers partly based on geography, costs, quality, or reliability, and suppliers in hotter regions may already price climate risk into contracts. Relationship terminations may reflect demand shocks, supplier distress, contract expiration, reporting changes, or unobserved relationship quality rather than customer learning about climate risk. There is also measurement error because headquarters may not perfectly represent production exposure, although the authors use Orbis establishment locations for robustness.

### Identification Approach
- Natural experiment: Short-run local heat realizations at supplier locations are treated as plausibly exogenous conditional on location, seasonality, industry, country-pair, and time controls.
- Instrument: None.
- Difference in differences: Not a classic DiD, but conceptually compares supplier relationships where realized exposure exceeds historical expectations to those where it does not, net of high-dimensional fixed effects.
- Event study: Used around supplier heatwaves for customer operating income dynamics.
- Fixed effects: Supplier industry-year FE, customer industry-year FE, supplier-country by customer-country by year FE in termination tests. Direct and propagation tests use firm by fiscal-quarter FE, industry by year-quarter FE, country trends, and Barrot-Sauvagnat style size, age, and profitability time controls.
- Matching: Replacement supplier analysis matches terminated suppliers to new suppliers with the same four-digit SIC code that begin relationships with the same customer within one year.
- Placebo tests: Transitory realized heat days do not predict termination once the historical expectation channel is removed. Inactive relationship tests do not show similar propagation effects.
- Robustness: Alternative prior windows of 5 and 15 years, alternative heat definitions, all-location Orbis exposure, logit, Cox hazard models, exclusions for EM-DAT disasters, country adaptation readiness, CMIP5 projections, and flood exposure.
- Alternative source of variation: Flood days from the Dartmouth Flood Observatory.

### Is the Identification Convincing?
- Strength: The paper improves on simple heat-performance correlations by using deviations from supplier-specific historical expectations, not just heat levels. The fixed effects absorb broad industry, time, country-pair, and location-level confounds.
- Weakness: The authors do not observe managers' beliefs, contract terms, prices, insurance, or actual renegotiations. Thus, the mechanism is inferred from behavior rather than directly observed.
- Referee concern: The main critique is whether terminations reflect customer learning about persistent climate risk or other unobserved shocks that both increase heat-related disruptions and end relationships. The transitory heat placebo and replacement supplier tests help, but do not fully eliminate this concern.

## 8. Main Regression or Model

Main supplier termination model:

```text
1(End)_sct =
  beta 1(Realized > Expected Exposure)_sct
+ Supplier industry x Year FE
+ Customer industry x Year FE
+ Supplier country x Customer country x Year FE
+ epsilon_sct
```

The unit is supplier-customer pair-year. The dependent variable equals one if the supplier-customer relationship ends after year t. The main coefficient beta measures whether a customer is more likely to terminate a supplier after realized heat days at the supplier location exceed the expected heat days based on the pre-relationship benchmark period.

Supplier and customer operating performance model:

```text
Operating Income_it =
  sum beta_k Heat Days_i,t-k
+ Firm x Fiscal Quarter FE
+ Industry x Year-Quarter FE
+ Country trends
+ Size/Age/Profitability x Year-Quarter FE
+ epsilon_it
```

For suppliers, Heat Days are local heat days at the supplier location. For customers, supplier heat exposure is aggregated across the customer's suppliers. The coefficients beta_k measure the direct and downstream propagation effects of supplier-location heat on operating income.

Replacement supplier model:

```text
1(Exposure New < Old)_sc =
  beta 1(Realized > Expected Exposure)_st
+ Supplier industry x Year FE
+ Customer industry x Year FE
+ Country-pair x Year FE
+ epsilon_sc
```

Here beta measures whether customers that terminate unexpectedly heat-exposed suppliers choose replacement suppliers with lower heat exposure.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Climate Finance]] by showing that physical climate risk affects real firm decisions and supply-chain structure, not just asset prices or disclosures.
2. [[Supply Chain Networks]] by showing that moderate climate exposure, not only major natural disasters, propagates through supplier-customer links.
3. [[Experience-Based Learning]] by documenting behavior consistent with firms updating beliefs from realized local climate signals.
4. [[Production Networks]] by showing that climate change can reshape the endogenous matching of customers and suppliers.

It differs from prior work because it studies gradual and noisy climate risk adaptation in global supply chains, rather than only direct weather shocks, natural disasters, or investor pricing responses.

## 10. Closely Related Papers
- [[Barrot and Sauvagnat 2016]]: Natural disasters propagate through production networks. Pankratz and Schiller extend the idea to heat exposure and climate adaptation.
- [[Carvalho et al. 2021]]: Production networks transmit localized shocks. This paper studies global supply-chain adaptation rather than only propagation.
- [[Boehm et al. 2019]]: Supply-chain disruptions affect production. This paper connects disruptions to climate learning and supplier replacement.
- [[Addoum, Ng, and Ortiz-Bobea 2020]]: Weather affects firm earnings. Pankratz and Schiller add indirect exposure through suppliers.
- [[Choi, Gao, and Jiang 2020]]: Investors update beliefs about climate change after unusual weather. This paper applies experience-based learning to corporate supply-chain decisions.
- [[Dessaint and Matray 2017]]: Firms increase cash after disaster risk salience. Pankratz and Schiller similarly find increased cash holdings after supplier climate exposure exceeds expectations.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on climate risk and firm behavior. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Firms respond to perceived increases in supplier physical climate risk by terminating suppliers and selecting less exposed replacements.
- Data: Global supplier-customer links from FactSet Revere, Worldscope financials, FactSet and Orbis locations, ECMWF heat data, CMIP5 projections, ND-GAIN readiness.
- Identification: Local supplier heat realizations relative to pre-relationship historical expectations, with supplier industry-year, customer industry-year, and supplier-country by customer-country by year fixed effects.
- Limitation: Priors and beliefs are not directly observed, and relationship terminations may reflect unobserved contractual or operational shocks.
- Connection to other papers: Use with [[Barrot and Sauvagnat 2016]] and [[Carvalho et al. 2021]] for shock propagation, and with [[Choi, Gao, and Jiang 2020]] for experience-based climate learning.
- Best exam phrase: "Pankratz and Schiller show that physical climate risk is not just priced or disclosed. It changes the actual architecture of global production networks."

## 12. Hypotheses Inspired by This Paper
H1: Customers are more likely to terminate supplier relationships when suppliers experience climate exposure above historical expectations.

H2: The termination response is stronger when suppliers are easier to replace, such as when supplier-industry competition is high or relationship-specific investments are low.

H3: Customers with greater financial flexibility are more likely to adapt by switching suppliers, while constrained customers absorb more downstream operating losses.

## 13. Possible Extension or Research Design
- Research question: Does financial flexibility determine whether firms can adapt to supplier physical climate risk?
- Hypothesis: Cash-rich or less financially constrained customers are more likely to replace unexpectedly climate-exposed suppliers, while constrained customers remain exposed and experience larger performance declines.
- Data: FactSet Revere supplier links, Compustat or Worldscope financials, ECMWF ERA5 heat data, CMIP5 projections, credit ratings or KZ/SA/WW constraint measures.
- Identification: Interact realized supplier heat exposure exceeding expectations with customer financial flexibility, using customer FE, supplier industry-year FE, customer industry-year FE, and supplier-country by customer-country by year FE.
- Expected result: Financially flexible customers switch faster, hold more inventory, and suffer smaller downstream operating income losses.
- Contribution: Connects [[Climate Finance]], [[Financial Flexibility]], and [[Supply Chain Networks]] by showing that adaptation capacity is partly financial, not just technological or geographic.

## 14. Critiques

### Major Concern 1
The paper does not directly observe beliefs. The expected exposure measure is constructed from historical heat days before the relationship starts, but firms may use more sophisticated forecasts, supplier disclosures, climate models, insurance prices, or private information. Therefore, the evidence is consistent with experience-based learning but cannot prove the exact belief-updating process.

### Major Concern 2
Relationship termination is a reduced-form outcome. The data do not fully reveal whether the customer terminated the supplier, the supplier exited, the contract expired, prices were renegotiated, or disclosure coverage changed. The authors address this with transitory heat tests, replacement supplier analysis, and contract discussion, but the exact contractual channel remains partly unobserved.

### Minor Concern
Headquarters-based heat exposure may mismeasure the true operational exposure of firms with geographically dispersed production. The paper mitigates this using Orbis establishment data and excluding firms with low headquarters concentration, but facility-level production weights are still not clear from provided text.

### Referee Recommendation
Accept, because the paper combines a novel global supply-chain dataset with granular weather data and provides a strong reduced-form design showing that physical climate risk affects network formation. The main caveat is that the learning mechanism is inferred rather than directly observed.

## 15. Memory Hooks
- "Expected versus realized heat" is the key variable, not raw temperature.
- 7% more likely to terminate when supplier heat exceeds expectations.
- Heat propagates: supplier heat hurts customer operating income.
- Transitory heat does not predict termination, which supports the learning interpretation.
- Replacement suppliers are less heat-exposed, but long-run projection results are weaker.

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Climate Finance]], [[Supply Chain Networks]], [[Production Networks]], [[Physical Climate Risk]], or [[Experience-Based Learning]]. The clean exam answer is: "Pankratz and Schiller 2024 use deviations of supplier heat exposure from historical expectations as quasi-random learning signals and show that customers are more likely to terminate and replace suppliers when climate exposure rises unexpectedly." Use it to argue that physical climate risk changes real firm policies and the structure of production networks, not just asset prices. In a critique answer, emphasize that managerial beliefs and contract terms are not observed, but note that the paper is stronger than a standard correlation because it uses supplier-specific historical priors, granular local weather data, high-dimensional fixed effects, transitory shock tests, replacement-supplier evidence, and flood robustness.
