---
type: paper
status: unread
title: "Buying products from whom you know: personal connections and information asymmetry in supply chain relationships"
authors: Ting Chen, Hagit Levy, Xiumin Martin, Ron Shalev
year: 2021
journal: Review of Accounting Studies
seminar:
field: Corporate Finance, Accounting, Supply Chain
literature: Supply Chain Finance, Social Networks, Information Asymmetry, Contracting
methods: Mahalanobis matching, linear probability model, Cox hazard model, cross-sectional interaction tests, WLS event study
datasets: Compustat Segment, BoardEx, Compustat, CRSP, 10-K Wizard, hand-collected procurement contracts
identification: Predetermined executive education and prior-work connections, matched nonsupplier vendors, customer-year fixed effects, executive departure shock, information-asymmetry heterogeneity
main_result: Personally connected vendors are more likely to be selected as suppliers, especially when information asymmetry is high.
exam_relevance: high
must_memorize: true
tags:
  - supply-chain-finance
  - social-networks
  - information-asymmetry
  - contracting
  - supplier-selection
  - BoardEx
  - DrJandik
created: 2026-06-12
updated: 2026-06-12
---

# Chen, Levy, Martin, and Shalev 2021

## 1. One-Sentence Takeaway
This paper shows that executive personal connections increase the probability that a vendor is chosen as a supplier using BoardEx connections matched to Compustat customer-supplier links, and the main contribution is to show that social ties reduce information frictions in real operating decisions, not just financing or investing decisions.

## 2. Exam-Ready Abstract
Chen, Levy, Martin, and Shalev study whether personal connections between executives affect supplier selection. They use Compustat Segment data to identify first-time major customer-supplier relationships among U.S. public firms from 2000 to 2011, and BoardEx to identify education-based and prior-work-based executive connections that predate the business relationship. For each actual supplier, they construct a set of comparable nonsupplier vendors using Mahalanobis matching within four-digit SIC industries on size, ROA, and sales. They find that connected vendors are more likely to become suppliers, with the effect equal to about a 60 percent increase over the baseline selection probability. The effect is stronger for high-rank executives, especially customer COOs, and stronger when information asymmetry is high, measured by geographic distance and poor accounting quality. They also show that connected executive departures predict earlier supply-chain termination, connected contracts are less restrictive and longer, and connected suppliers are followed by improved customer operating efficiency. This paper belongs in [[Supply Chain Finance]], [[Social Networks]], [[Information Asymmetry]], [[Contracting]], and [[Corporate Operating Decisions]].

## 3. Research Question
Does an executive personal connection between a customer and a potential supplier increase the likelihood that the vendor is selected as an actual supplier?

More specifically, the paper tests whether personal connections reduce information asymmetry in supplier selection by transmitting soft information, increasing trust, improving monitoring, and reducing the need for restrictive procurement contracts.

## 4. Core Mechanism
Use this chain for comps:

```text
Predetermined executive personal connection
-> more trust and soft information between customer and vendor
-> lower information asymmetry about supplier quality, reliability, and risk
-> customer is more willing to select the connected vendor
-> supply-chain relationship forms, contracts are less restrictive, and operating efficiency improves
```

Alternative shock version:

```text
Departure of connected executive
-> loss of informal information channel
-> higher information asymmetry and weaker trust
-> customer-supplier relationship becomes less valuable
-> higher hazard of supply-chain termination
```

## 5. Main Findings
1. Connected vendors are more likely to be selected as suppliers. The coefficient on CONNECTED is about 0.210 in the baseline LPM, implying a 21 percentage point higher selection probability, or roughly 60 percent above the 35 percent baseline probability.
2. The effect is stronger when the connection is more relevant to supplier choice. CEO-to-CEO and C-level connections matter more than lower-level connections, and customer COO connections have a particularly large effect.
3. The information-asymmetry channel is supported by cross-sectional tests. The connection effect is stronger when customer and vendor are farther apart and when the vendor has poorer accounting quality, measured using abnormal accruals.
4. Executive departures matter. A connected executive departure increases the hazard of relationship termination relative to an unconnected executive departure.
5. Consequences are economically meaningful. Connected procurement contracts are less restrictive, last longer, and connected relationships are followed by lower inventory and COGS volatility, higher sales efficiency, and higher ROA.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Customer-vendor-year for supplier-selection tests; executive-customer-supplier for departure tests; contract for procurement-contract tests; customer-year for operating-efficiency tests |
| Sample period | 2000 to 2011 for main supplier-selection sample |
| Main dataset | Compustat Segment for major customer-supplier relationships, BoardEx for executive connections, Compustat and CRSP for financials and returns |
| Key variables | SUPPLIER, CONNECTED, CON_EDU, CON_WORK, DISTANCE, ABN_ACCRUALS_S |
| Treatment or shock | Predetermined education or prior-work executive connection; departure of a connected executive |
| Outcome variables | Supplier selection, relationship duration, contract restrictiveness, contract duration, inventory volatility, COGS volatility, sales-to-assets, ROA |
| Contract sample | 154 hand-collected procurement contracts from SEC filings using 10-K Wizard |
| Main matching method | Up to two nonsupplier vendors matched to each selected supplier within four-digit SIC and fiscal year using Mahalanobis distance on total assets, ROA, and sales |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between personal connections and supplier selection is not causal. Connected firms may differ systematically from unconnected firms. For example, high-quality vendors may be more likely to attract both business relationships and executive ties. Customers may select suppliers based on unobservable product quality, reputation, reliability, or managerial quality, and these same traits may correlate with executives’ networks. Reverse causality is also a major issue because a business relationship could generate later personal ties. There is also a matched-counterfactual problem because the true set of vendors considered by the customer is unobserved.

### Identification Approach
- Natural experiment: Departure of a connected executive severs the personal connection and predicts earlier relationship termination.
- Instrument: No formal instrument.
- Difference in differences: Not the main supplier-selection design. The operating-performance test uses a pre/post event-study style design around supply-chain formation.
- Event study: Customer operating outcomes before versus after relationship formation, interacted with CONNECTED.
- Fixed effects: Customer-year fixed effects in supplier-selection regressions; year and industry fixed effects in contract tests; customer and year-industry fixed effects in operating-efficiency tests.
- Matching: Mahalanobis matching identifies nonsupplier vendors that resemble the chosen supplier within the same four-digit SIC and fiscal year.
- Placebo tests: Not clear from provided text.
- Robustness: Alternative propensity-score matching, distance-balanced samples, additional fixed effects, longer required time gaps between personal and business connections, three or four matched vendors, all four-digit SIC vendors, Hoberg-Phillips text-based industries, and Heckman correction for contract sample selection.
- Alternative source of variation: Heterogeneity by executive rank, executive function, geographic distance, accounting quality, and local vendor availability.

### Is the Identification Convincing?
- Strength: The paper is stronger than a standard cross-sectional correlation because it focuses on connections likely formed before the business relationship, uses matched nonsupplier vendors, includes customer-year fixed effects, and validates the mechanism with executive departures and information-asymmetry heterogeneity.
- Weakness: The true vendor consideration set is unobserved, and the matched nonsupplier vendors may not be the firms the customer actually considered.
- Referee concern: Even education and prior-work ties may proxy for elite networks, managerial quality, geography, industry specialization, or unobserved social capital that independently affects supplier choice.

## 8. Main Regression or Model

Baseline supplier-selection regression:

```text
SUPPLIER_ijt =
  beta1 CONNECTED_ijt
+ beta2 DISTANCE_ijt
+ Vendor Controls_jt
+ Customer-Year FE_it
+ epsilon_ijt
```

The dependent variable equals one if vendor j is the actual supplier of customer i in year t, and zero if vendor j is a matched nonsupplier vendor. The key coefficient is beta1. A positive beta1 means that connected vendors are more likely to be selected as suppliers after comparing them to similar vendors for the same customer-year.

Information-asymmetry heterogeneity:

```text
SUPPLIER_ijt =
  beta1 CONNECTED_ijt
+ beta2 IA_PROXY_ijt
+ beta3 CONNECTED_ijt x IA_PROXY_ijt
+ Controls
+ Customer-Year FE
+ epsilon_ijt
```

The main mechanism coefficient is beta3. If beta3 is positive, personal connections matter more when information asymmetry is high. The paper uses distance and abnormal accruals as information-asymmetry proxies.

Executive departure hazard model:

```text
Hazard(Termination after departure) =
  f(CONNECTED_EXEC,
    DISTANCE,
    DURATION_PRE,
    CONNECTED_FIRM,
    Supplier Controls,
    Customer Controls,
    Year FE)
```

CONNECTED_EXEC equals one if the departing executive was personally connected to an executive at the supply-chain counterparty. A hazard ratio greater than one means connected executive departures accelerate relationship termination.

Operating-efficiency event-study style model:

```text
OUTCOME_Cijt =
  beta1 CONNECTED_ijt
+ beta2 POST_ijt
+ beta3 CONNECTED_ijt x POST_ijt
+ beta4 DISTANCE_ijt
+ beta5 DISTANCE_ijt x POST_ijt
+ Customer Controls
+ Customer FE
+ Year-Industry FE
+ epsilon_ijt
```

The coefficient beta3 carries the main interpretation. For inventory volatility and COGS volatility, beta3 should be negative. For sales efficiency and ROA, beta3 should be positive.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Supply Chain Finance]] by showing that supplier selection depends not only on prices and observable fundamentals but also on executive social ties.
2. [[Social Networks]] by extending the literature on personal connections from investing, lending, and board decisions to real operating decisions.
3. [[Information Asymmetry]] by showing that personal connections matter most when hard information is weak or costly to acquire.
4. [[Contracting]] by showing that informal relationships can substitute for formal restrictive contract terms.

It differs from prior work because it studies the formation of customer-supplier relationships, not only financing, governance, or investment outcomes. It also connects selection, contract design, relationship survival, and customer operating performance in one setting.

## 10. Closely Related Papers
- [[Cohen, Frazzini, and Malloy 2008]]: Social connections transmit information in mutual fund portfolio decisions.
- [[Engelberg, Gao, and Parsons 2012]]: Personal connections affect lending and financing relationships.
- [[Duchin and Sosyura 2013]]: Social connections affect internal capital allocation and managerial decisions.
- [[Fracassi 2017]]: Corporate social networks affect board monitoring and firm value.
- [[Costello 2013]]: Procurement contracts respond to information asymmetry and monitoring costs.
- [[Kale and Shahrur 2007]]: Supplier-customer relationships affect capital structure.
- [[Cohen and Li 2014]]: Customer-supplier relationships affect liquidity management.
- [[Hui, Klasa, and Yeung 2012]]: Product-market relationships affect financial reporting policy.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the literature on social networks and information asymmetry in corporate finance. How do personal connections affect real firm decisions?

How to use this paper:
- Main finding: Executive ties increase the probability that a vendor is selected as a supplier.
- Data: BoardEx executive connections matched to Compustat Segment customer-supplier links.
- Identification: Predetermined education and prior-work ties, matched nonsupplier vendors, customer-year fixed effects, executive departures, and information-asymmetry heterogeneity.
- Limitation: The actual vendor consideration set is unobserved, so the matched nonsupplier vendors may not be perfect counterfactuals.
- Connection to other papers: Use with Cohen et al. 2008 and Engelberg et al. 2012 to argue that social networks transmit soft information across market settings.
- Best exam phrase: "Chen et al. 2021 show that social ties operate as an informal information channel in supplier selection, especially when hard information is weak."

## 12. Hypotheses Inspired by This Paper
H1: The positive effect of executive connections on supplier selection is stronger when the customer faces greater supply-chain complexity or input specificity.

H2: Connected supplier relationships are less likely to experience disruption during aggregate supply shocks because personal ties facilitate faster private communication and coordination.

H3: The value of executive connections is larger for private suppliers than public suppliers because private firms are more opaque and have weaker public information environments.

## 13. Possible Extension or Research Design
- Research question: Do personal connections make supply chains more resilient during major disruptions such as COVID-19, the Russia-Ukraine war, or port shutdowns?
- Hypothesis: Customers with connected suppliers experience smaller disruptions in sales, inventory, or production after supply-chain shocks.
- Data: FactSet Revere or Compustat Segment supplier-customer links, BoardEx executive connections, COVID exposure measures, shipping disruptions, RavenPack news, and firm outcomes from Compustat.
- Identification: Difference in differences comparing connected versus unconnected customer-supplier pairs before and after an exogenous disruption, with customer fixed effects, supplier industry-by-time fixed effects, and pre-trend tests.
- Expected result: Connected relationships should show smaller increases in inventory volatility, fewer production delays, and faster recovery.
- Contribution: Extends the paper from supplier selection to supply-chain resilience and shock propagation.

## 14. Critiques

### Major Concern 1
The actual supplier choice set is unobserved. The paper constructs nonsupplier vendors using Mahalanobis matching, but customers may have considered different firms based on product compatibility, private quality signals, capacity, or prior informal bids.

### Major Concern 2
Connections may proxy for unobserved quality or elite networks. Education and prior-work connections may indicate common training, industry specialization, reputation, or managerial ability rather than causal soft-information transmission.

### Minor Concern
The Compustat Segment data identify only major customers, generally those accounting for at least 10 percent of supplier sales, so the observed start of the relationship may lag the true start.

### Referee Recommendation
R&R, because the mechanism is plausible and the paper provides multiple supporting tests, but the matched-vendor design and possible unobserved selection into connections should be discussed carefully. The paper is publishable because it triangulates the mechanism using rank heterogeneity, COO relevance, executive departures, contract terms, and operating outcomes.

## 15. Memory Hooks
- "Buying from whom you know" equals supplier selection through executive ties.
- BoardEx plus Compustat Segment equals personal networks plus supply-chain links.
- Main number: connected vendors are about 60 percent more likely to be selected relative to the baseline probability.
- Mechanism check: effect is stronger when distance is greater and accounting quality is worse.
- COO hook: customer COO connections matter especially because COOs oversee operations and supply chains.
- Consequence hook: connected contracts are less restrictive and connected relationships improve operations.

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Supply Chain Finance]], [[Social Networks]], [[Information Asymmetry]], [[Contracting]], [[Relationship Lending]], or [[Corporate Operating Decisions]]. The clean exam answer is: "Chen, Levy, Martin, and Shalev 2021 use BoardEx education and prior-work connections matched to Compustat customer-supplier links and show that connected vendors are more likely to become suppliers, especially when information asymmetry is high." Use it to argue that informal social ties can substitute for hard information and formal contracting in real operating decisions. In a critique answer, emphasize that the true vendor choice set is unobserved and that connections may proxy for elite networks or quality, but note that the paper is stronger than a standard correlation because it uses predetermined ties, matched nonsupplier vendors, customer-year fixed effects, executive departures, mechanism heterogeneity, and downstream contract and performance tests.