---
type: paper
status: unread
title: International Trade and the Propagation of Merger Waves
authors: Muhammad Farooq Ahmad; Eric de Bodt; Jarrad Harford
year: 2021
journal: Review of Financial Studies
seminar:
field: Corporate Finance; International Finance
literature: Mergers and Acquisitions; Merger Waves; Cross-Border M&A; International Trade; Networks
methods: Network analysis; Dynamic panel; Arellano-Bond; 2SLS; Granger causality; Event study
datasets: UN ComTrade; Thomson Financial SDC; Datastream; ICRG; World Bank; TIES; Hofstede
identification: Trade-flow shocks from import tariff cuts and trade sanctions; country and year fixed effects; shuffled-network placebo tests; country-pair fixed effects; Granger causality
main_result: Merger waves propagate across countries through trade links, and trade-weighted merger activity in partner countries predicts both cross-border and domestic merger waves.
exam_relevance: high
must_memorize: true
tags:
  - mergers
  - merger-waves
  - cross-border-ma
  - international-trade
  - networks
  - corporate-finance
  - DrJandik
created: 2026-06-04
updated: 2026-06-04
---

# Ahmad, de Bodt, and Harford 2021

## 1. One-Sentence Takeaway
This paper shows that merger waves propagate internationally through trade networks using country and country-industry trade and M&A data from 1989 to 2016, and the main contribution is to show that trade links create learning and exposure channels that transmit both cross-border and domestic merger activity.

## 2. Exam-Ready Abstract
Ahmad, de Bodt, and Harford ask whether international trade relationships transmit merger waves across countries. They build annual global trade networks using UN ComTrade data from 1989 to 2016 and combine them with domestic and cross-border merger data from Thomson Financial SDC. The main finding is that trade-weighted merger activity in partner countries predicts whether a country enters a high M&A state, even after controlling for its own lagged merger activity, country fixed effects, year fixed effects, centrality, and macro controls. The mechanism is that trade gives firms exposure to foreign shocks and teaches them how to operate in foreign markets, making them more likely to respond to merger waves in trading partner countries through acquisitions. To address endogeneity, the paper instruments trade flows using import tariff cuts and trade sanctions, conducts placebo tests with randomly shuffled trade links, and shows that trade flows Granger-cause merger activity but not the reverse. The paper belongs in [[Mergers and Acquisitions]], [[Merger Waves]], [[Cross-Border M&A]], [[International Trade]], and [[Network Effects in Finance]].

## 3. Research Question
What is the paper trying to answer?

Does international trade explain why merger waves propagate across countries?

More specifically: the paper tests whether trade relationships create a learning and exposure channel through which M&A activity in one country affects M&A activity in economically connected countries. It asks whether trade is a substitute for acquisitions or a complement that helps transmit merger waves.

## 4. Core Mechanism

```text
Foreign merger wave in a trade-linked country
-> ownership and competitive structure changes in that foreign market
-> domestic firms are exposed through imports or exports
-> trade experience gives firms information about foreign demand, institutions, customers, and regulations
-> firms respond through cross-border or domestic acquisitions
-> merger waves propagate internationally through the trade network
```

## 5. Main Findings
1. Trade-weighted M&A activity in connected countries positively predicts whether a subject country enters a high M&A state. This holds for both cross-border and domestic merger activity.
2. The result survives attempts to address endogeneity, including 2SLS using import tariff cuts and trade sanctions, controls for economic integration, geographic and cultural proximity, stock market valuation differences, and shuffled-network placebo tests.
3. Evidence supports a learning mechanism: foreign sales Granger-cause cross-border M&A for a cohort of post-IPO firms, cultural distance weakens the trade-M&A link, stronger property rights strengthen it, and foreign sales are associated with more value-creating acquisitions.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Country-year, country-industry-year, country-pair-year, and firm-event in supporting tests |
| Sample period | 1989 to 2016 |
| Main dataset | UN ComTrade for trade flows; Thomson Financial SDC for domestic and cross-border mergers |
| Key variables | Connected M&A, High M&A State, trade-flow weights, import/export shares, degree centrality, eigenvector centrality, GDP, GDP growth, exchange rate variables, institutional quality, cultural distance |
| Treatment or shock | Import tariff cuts and trade sanctions used as instruments for trade-flow variation |
| Outcome variables | Indicator for high cross-border or domestic M&A state; country-pair inbound and outbound cross-border M&A volume; acquirer CARs in value-creation tests |

Important details:
- Trade data cover imports and exports among 100 countries.
- Merger sample includes 49,905 cross-border transactions worth $16.710 trillion and 174,899 domestic transactions worth $41.549 trillion across 74 countries.
- Figure 1 on page 9 shows Cisco export growth and later cross-border M&A, illustrating the learning and exposure mechanism visually.
- Figure 2 on page 13 shows global cross-border merger waves over time.
- Figures 3 to 5 show the densification of trade and merger networks over 1989, 2002, and 2016.

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between trade links and merger activity is not causal because trade links may proxy for broader economic integration, common shocks, cultural proximity, geographic proximity, exchange rate movements, market valuation differences, or global merger cycles. Reverse causality is also possible: mergers could increase trade after firms integrate supply chains or expand internationally. There is also equilibrium sorting because countries with strong institutions, open capital markets, and developed financial systems may simultaneously trade more and merge more.

### Identification Approach
- Natural experiment: Uses shocks to trade relationships from import tariff cuts and trade sanctions.
- Instrument: Instruments trade flows with large import tariff cuts and trade sanctions, then recomputes predicted trade-weighted connected M&A.
- Difference in differences: Not the main design.
- Event study: Used in acquirer CAR analysis around merger announcements.
- Fixed effects: Country and year fixed effects in country-level tests; country-industry fixed effects in industry tests; country-pair fixed effects in bilateral tests.
- Matching: Not central to the design.
- Placebo tests: Randomly shuffles trade links and shows that randomly assigned trade weights do not predict merger waves.
- Robustness: Controls for geography, culture, valuation differences, connected stock returns, exchange rates, economic integration, centrality, trend-adjusted M&A waves, continuous M&A intensity, and exclusion of the United States, Netherlands, and Singapore.
- Alternative source of variation: Granger causality tests show trade flows predict future merger activity, not the reverse.

### Is the Identification Convincing?
- Strength: Stronger than a standard international correlation because the authors combine network structure, dynamic panel methods, country and year fixed effects, instruments, placebo networks, and Granger causality.
- Weakness: Tariff cuts and sanctions may still be correlated with political economy forces, macro shocks, or investment liberalization that also affect M&A directly.
- Referee concern: The exclusion restriction is the key concern. Tariffs and sanctions may change merger incentives through channels other than trade exposure, such as policy uncertainty, foreign investment restrictions, or macro risk.

## 8. Main Regression or Model

```text
High M&A State_i,t =
  alpha_i
+ lambda_t
+ beta High M&A State_i,t-1
+ gamma Connected M&A_i,t
+ theta Controls_i,t
+ epsilon_i,t
```

The dependent variable equals one when a country’s merger activity is in the top quartile of its own sample-period distribution. The key independent variable, Connected M&A, is the merger activity of other countries weighted by the subject country’s trade links to those countries. The main coefficient is gamma. A positive gamma means that merger activity in trade-linked countries predicts merger waves in the subject country.

The connected M&A variable is:

```text
Connected M&A_i,t =
  sum over j not equal i of W_i,j,t x M&A_j,t
```

where `W_i,j,t` is a trade-flow weight, such as the share of country i's imports coming from country j, and `M&A_j,t` is merger intensity in country j.

The 2SLS version is:

```text
Trade Flow_i,j,t =
  alpha
+ beta Tariff Cuts_i,j,t
+ gamma Trade Sanctions_i,j,t
+ error_i,j,t
```

Then predicted trade flows are used to construct fitted connected M&A:

```text
Connected M&A fitted_i,t =
  sum over j not equal i of predicted W_i,j,t x M&A_j,t
```

The second stage estimates whether fitted connected M&A predicts high M&A states. The main economic interpretation comes from the coefficient on fitted Connected M&A.

For learning heterogeneity:

```text
Cross-Border M&A_i,j,t =
  beta1 Trade Link_i,j,t-1
+ beta2 Trade Link_i,j,t-1 x Cultural Distance_i,j
+ beta3 Cultural Distance_i,j
+ Controls
+ Country-Pair FE
+ Year FE
+ epsilon_i,j,t
```

Here beta2 should be negative if cultural distance is a barrier to learning.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Mergers and Acquisitions]] by showing that merger waves are not only domestic or industry-level phenomena.
2. [[Cross-Border M&A]] by showing that trade networks predict international acquisition patterns beyond gravity variables.
3. [[International Trade]] and [[FDI]] by treating acquisitions as a real investment response to trade-induced learning and exposure.

It differs from prior work because it uses the full global trade network rather than only bilateral gravity variables, and it studies how M&A waves propagate through the network over time.

## 10. Closely Related Papers
- [[Ahern and Harford 2014]]: Shows that merger waves propagate across related U.S. industries through product market links.
- [[Erel, Liao, and Weisbach 2012]]: Studies determinants of cross-border mergers, including valuation, exchange rates, and country characteristics.
- [[Ahern, Daminelli, and Fracassi 2015]]: Shows that cultural distance affects cross-border merger volume and synergies.
- [[Harford 2005]]: Classic merger-wave paper emphasizing industry shocks and capital liquidity.
- [[Mitchell and Mulherin 1996]]: Early evidence that industry shocks trigger takeover and restructuring waves.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on merger waves. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Merger waves propagate internationally through trade links.
- Data: UN ComTrade country and industry trade flows plus SDC domestic and cross-border M&A, 1989 to 2016.
- Identification: Dynamic panel regressions, country and year fixed effects, import tariff cuts and trade sanctions as instruments, shuffled trade-network placebo tests, and Granger causality.
- Limitation: Trade links may proxy for broader integration or policy environments, and the instruments may not satisfy a perfect exclusion restriction.
- Connection to other papers: Extends [[Ahern and Harford 2014]] from U.S. industry networks to global trade networks, and complements [[Erel, Liao, and Weisbach 2012]] on cross-border acquisition determinants.
- Best exam phrase: "Ahmad, de Bodt, and Harford show that merger waves are transmitted through the global trade network, consistent with trade-induced learning and exposure."

## 12. Hypotheses Inspired by This Paper
H1: Firms with greater pre-shock trade exposure to a foreign market are more likely to acquire firms in that market after a foreign industry consolidation wave.

H2: The trade-to-M&A transmission effect is weaker when acquirer and target countries have larger cultural, legal, or institutional distance.

H3: The trade-to-M&A transmission effect is stronger when target-country property rights are stronger because firms can better convert learning into value-creating acquisitions.

## 13. Possible Extension or Research Design
- Research question: Do supply-chain links transmit merger waves across firms and countries after geopolitical shocks?
- Hypothesis: Firms with pre-existing supplier or customer exposure to a country experiencing consolidation are more likely to acquire domestically or abroad in response.
- Data: FactSet Revere supply-chain links, SDC M&A, Compustat Global, sanctions data, tariff data, and country-level institutional measures.
- Identification: Difference-in-differences around exogenous trade disruptions, such as Russia sanctions or tariff changes, comparing firms with high versus low pre-shock supply-chain exposure.
- Expected result: Highly exposed firms respond to foreign consolidation or disruption with more acquisitions, especially when alternative suppliers or targets are available in institutionally stronger countries.
- Contribution: Moves the paper from country-level trade networks to firm-level supply-chain networks and directly tests the firm-level mechanism.

## 14. Critiques

### Major Concern 1
The exclusion restriction for tariff cuts and trade sanctions is debatable. These shocks may affect M&A directly through policy uncertainty, foreign investment restrictions, political relationships, or market access, not only through trade-flow exposure.

### Major Concern 2
The core mechanism is firm-level learning, but much of the main evidence is aggregated at the country or country-industry level. The firm-level evidence is suggestive, especially the 85 post-IPO firm test, but it does not fully observe destination-specific export learning and subsequent destination-specific acquisitions.

### Minor Concern
The High M&A State variable is discretized as top-quartile merger activity within country. This helps identify waves but may lose information relative to continuous merger intensity.

### Referee Recommendation
Accept, because the paper makes a clear contribution to the merger-wave and cross-border M&A literatures, uses a novel global network approach, and supports the main mechanism with multiple identification and validation tests. The main caveat is that the causal interpretation depends heavily on whether tariff cuts and trade sanctions affect M&A only through trade links.

## 15. Memory Hooks
- "Merger waves ride trade routes."
- Trade creates both exposure and learning.
- Cisco example: exports grow first, cross-border M&A follows.
- Shuffled trade links kill the result.
- Cultural distance blocks learning; property rights help convert learning into acquisitions.

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Mergers and Acquisitions]], [[Merger Waves]], [[Cross-Border M&A]], [[International Trade]], [[FDI]], or [[Network Effects in Finance]]. The clean exam answer is: "Ahmad, de Bodt, and Harford use the global trade network as a propagation channel and show that trade-weighted merger activity in partner countries predicts domestic and cross-border merger waves." Use it to argue that merger waves are not only caused by domestic industry shocks, but can spread internationally through real economic linkages. In a critique answer, emphasize that trade may proxy for economic integration, but note that the paper is stronger than a standard correlation because it uses tariff cuts and sanctions as instruments, shuffled-network placebo tests, country-pair fixed effects, and Granger causality evidence.