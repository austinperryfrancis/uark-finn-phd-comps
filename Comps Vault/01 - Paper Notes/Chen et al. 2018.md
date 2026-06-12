---
type: paper
status: unread
title: 'Clarity Begins at Home: Internal Information Asymmetry and External Communication Quality'
authors: Chen Chen; Xiumin Martin; Sugata Roychowdhury; Xin Wang; Matthew T. Billett
year: 2018
journal: The Accounting Review
professor: DrJandik
seminar: null
jandik_paper_number: 53
jandik_week: 14
jandik_topic: Governance
jandik_done: false
field: Accounting; Corporate Finance
literature:
- Internal Information Environment
- Disclosure
- Financial Reporting Quality
- '[[Internal Capital Markets]]'
- Insider Trading
methods:
- Panel regressions
- validation tests
- 2SLS
- logit
- event-style tests
datasets:
- TFN Insider Filing Database
- '[[Compustat]]'
- Compustat Segments
- First Call
- Audit Analytics
- hand-collected division data
- T-100 Domestic Segment Database
- GARMAISE non-compete index
identification: DIFRET insider-trading-based measure of internal information asymmetry, validated with division characteristics, flight-time shocks, non-compete enforceability changes, CEO turnover, routine-trade placebo, and 2SLS using flight time and non-compete enforceability
main_result: Higher internal information asymmetry between divisional and top managers predicts lower-quality management forecasts and more error-driven accounting restatements.
exam_relevance: high
must_memorize: true
tags:
- disclosure
- internal-information-environment
- management-forecasts
- restatements
- conglomerates
- insider-trading
- accounting
created: 2026-06-12
updated: 2026-06-12
---

# Chen et al. 2018

## 1. One-Sentence Takeaway
This paper shows that external communication quality deteriorates when top managers are informationally disadvantaged relative to divisional managers, using insider-trading profits to measure internal information asymmetry, and the main contribution is linking within-firm information frictions to disclosure quality and financial reporting errors.

## 2. Exam-Ready Abstract
Chen et al. study whether information asymmetry inside conglomerate firms affects the quality of external communication. The setting is multi-segment public firms where top executives rely on divisional managers for local operating information, but divisional managers may have private information that does not flow cleanly to headquarters. The key measure is DIFRET, the difference between divisional managers' and top managers' abnormal trading profits from opportunistic insider trades. Higher DIFRET means divisional managers appear to have a stronger private information advantage over top managers. The paper finds that higher DIFRET is associated with less accurate, more pessimistic, less specific, and less frequent management forecasts, plus a higher probability of error-driven restatements. The authors validate DIFRET using division-level operating volatility, listed peer availability, flight-time changes, non-compete enforceability, CEO turnover, routine-trade placebos, and 2SLS. This paper connects [[Internal Information Environment]], [[Voluntary Disclosure]], [[Financial Reporting Quality]], and [[Conglomerates]].

## 3. Research Question
What happens to a firm's external communication when information inside the firm is not evenly shared between divisional managers and top managers?

More specifically, the paper tests whether top managers produce lower-quality forecasts and financial statements when divisional managers hold value-relevant private information that top managers do not fully observe or synthesize.

## 4. Core Mechanism
Use this chain for comps:

```text
Greater internal information asymmetry
-> top managers lack divisional operating information
-> headquarters has weaker inputs for forecasts and accounting estimates
-> managers issue less precise, more conservative, and less frequent guidance
-> external disclosure quality falls and accounting errors become more likely
```

## 5. Main Findings
1. Higher DIFRET is associated with lower management forecast accuracy, lower forecast specificity, lower forecast frequency, and more pessimistic forecast bias.
2. Higher DIFRET predicts more error-driven accounting restatements, but not irregularity-driven restatements.
3. DIFRET appears to capture internal information asymmetry because it varies predictably with divisional volatility, public peer information, flight-time changes, non-compete enforceability, and outsider CEO turnovers.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Forecast-level observations for forecast tests; firm-year observations for restatement tests; division-level observations for validation tests |
| Sample period | Forecast tests: 1994 to 2011. Restatement tests: 1997 to 2011 |
| Main dataset | TFN Insider Filing Database matched to Compustat Annual, Compustat Segments, First Call management forecasts, and Audit Analytics restatements |
| Key variables | DIFRET, DIV_RET, TOP_RET, ACCURACY, BIAS, SPEC, FREQ, RES_ERR, RES_IRR |
| Treatment or shock | Not a single treatment. Main variation is DIFRET, plus validation from flight-time changes, GARMAISE non-compete changes, and CEO turnover |
| Outcome variables | Management forecast accuracy, bias, specificity, frequency, error-driven restatements, irregularity-driven restatements |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between internal information asymmetry and disclosure quality may not be causal. Firms with more complex operations may both have higher internal information asymmetry and worse disclosure quality. Poor disclosure practices could also cause managers to gather more or less internal information, creating reverse causality. Insider-trading-based DIFRET could also reflect trading constraints, litigation risk, or measurement error rather than true information gaps. Finally, firms with better governance, better systems, or better managers may both reduce IIA and produce higher-quality disclosures.

### Identification Approach
- Natural experiment: Changes in flight time between headquarters and divisions from airline route changes, and state-level changes in non-compete enforceability.
- Instrument: FLIGHT_TIME and GARMAISE are used as instruments for DIFRET in 2SLS.
- Difference in differences: Not a canonical DiD design, but event-style before-after comparisons around flight-time changes, GARMAISE changes, and CEO turnover.
- Event study: CEO turnover tests compare DIFRET before and after outsider versus insider CEO appointments.
- Fixed effects: Forecast regressions include firm and year fixed effects. Some validation tests use firm-by-year fixed effects. Restatement logit tests use industry and year fixed effects.
- Matching: Not central to the research design.
- Placebo tests: DIFRET constructed from routine trades does not predict disclosure outcomes.
- Robustness: Results remain in 2SLS, are stronger when DIFRET is positive, and hold when partitioning on top versus divisional trading patterns.
- Alternative source of variation: Division-level operating volatility and number of listed industry peers validate whether DIFRET varies with information opacity.

### Is the Identification Convincing?
- Strength: The paper does more than show a raw correlation. It validates the measure in multiple ways and uses plausible shocks to internal information flow.
- Weakness: DIFRET is only observable when both top and divisional managers trade opportunistically, so the sample is selected on insider trading activity.
- Referee concern: Flight time and non-compete enforceability may affect firm operations, monitoring, talent allocation, or local managerial incentives through channels other than IIA.

## 8. Main Regression or Model

```text
DisclosureQuality_it =
  beta DIFRET_it
+ Controls_it
+ Firm FE
+ Year FE
+ epsilon_it
```

For forecast tests, `DisclosureQuality` is forecast accuracy, bias, specificity, or frequency. The key coefficient is `beta`. A negative `beta` means that higher internal information asymmetry reduces forecast quality.

```text
Pr(Restatement_it = 1) =
  F(beta DIFRET_it
+ Controls_it
+ Industry FE
+ Year FE)
```

For restatement tests, the dependent variable is an indicator for error-driven restatements or irregularity-driven restatements. The main coefficient is `beta`. A positive `beta` for error restatements means internal information asymmetry makes unintentional accounting errors more likely.

```text
DisclosureQuality_it =
  beta1 DIFRET_it
+ beta2 DIFRET_it x POS_it
+ beta3 POS_it
+ Controls_it
+ Fixed Effects
+ epsilon_it
```

`POS` equals one when DIFRET is positive. `beta2` tests whether the effect is stronger when divisional managers appear better informed than top managers. The paper finds that the negative relation between DIFRET and communication quality is more pronounced when DIFRET is positive.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Internal Information Environment]] by measuring information asymmetry within the firm rather than treating internal information quality as a black box.
2. [[Voluntary Disclosure]] by showing that management forecast quality depends on headquarters' access to divisional information.
3. [[Financial Reporting Quality]] by linking internal information frictions to error-driven restatements.

It differs from prior work because it uses insider-trading profitability to infer relative private information across managerial layers, rather than relying only on organizational complexity, internal control weaknesses, or disclosure outcomes as proxies for internal information quality.

## 10. Closely Related Papers
- [[Cohen Malloy and Pomorski 2012]]: Classifies insider trades into routine and opportunistic trades, which supports the construction of DIFRET.
- [[Giroud 2013]]: Uses travel-time reductions to study headquarters monitoring of plants, closely related to the flight-time validation.
- [[Duchin and Sosyura 2013]]: Studies internal capital allocation and social ties between CEOs and divisional managers.
- [[Shroff Verdi and Yu 2014]]: Examines parent-subsidiary information problems in multinational investment.
- [[Feng Li and McVay 2009]]: Links internal control weaknesses to management forecast quality.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the literature on firms' internal information environments and explain how internal information problems affect disclosure and financial reporting quality.

How to use this paper:
- Main finding: When top managers are informationally disadvantaged relative to divisional managers, external communication quality falls.
- Data: Insider trading, Compustat segments, First Call management forecasts, and Audit Analytics restatements.
- Identification: DIFRET measure, extensive validation tests, routine-trade placebo, and 2SLS using flight time and non-compete enforceability.
- Limitation: DIFRET exists only for firms with enough opportunistic insider trades by both divisional and top managers.
- Connection to other papers: Connect to [[Giroud 2013]] on headquarters monitoring, [[Cohen Malloy and Pomorski 2012]] on informed insider trades, and [[Feng Li and McVay 2009]] on internal control and forecasts.
- Best exam phrase: "Clarity begins at home: external disclosure quality depends on whether headquarters actually knows what divisions know."

## 12. Hypotheses Inspired by This Paper
H1: Firms with greater internal information asymmetry issue less accurate and less specific management guidance.

H2: Internal information asymmetry increases error-driven restatements because headquarters has worse inputs for accounting estimates.

H3: The effect of internal information asymmetry on disclosure quality is stronger when divisional managers are geographically distant from headquarters or when managerial incentives to withhold information are stronger.

## 13. Possible Extension or Research Design
- Research question: Does enterprise resource planning adoption reduce the effect of internal information asymmetry on disclosure quality?
- Hypothesis: ERP adoption improves upward information flow from divisions to headquarters, weakening the negative relation between DIFRET and disclosure quality.
- Data: Public firm ERP implementation data, TFN insider trading, First Call management forecasts, Audit Analytics restatements, and Compustat segments.
- Identification: Difference in differences around ERP adoption, comparing multi-segment firms with high versus low pre-adoption DIFRET.
- Expected result: Forecast accuracy and specificity increase after ERP adoption, especially among firms with high pre-treatment DIFRET.
- Contribution: Shows whether information technology can reduce internal information frictions and improve external reporting.

## 14. Critiques

### Major Concern 1
DIFRET may capture something other than internal information asymmetry. For example, it may reflect differential legal risk, trading windows, managerial sophistication, or compensation structures across top and divisional managers.

### Major Concern 2
The sample is selected on observable opportunistic insider trades by both top and divisional managers. Firms with no such trades may still have severe internal information asymmetry, but the paper cannot measure it.

### Minor Concern
The non-compete and flight-time instruments may have direct effects on operations, monitoring intensity, or managerial labor markets beyond internal information flow.

### Referee Recommendation
R&R, because the paper has a creative measure and rich validation tests, but the authors should be pushed hardest on the exclusion restrictions for FLIGHT_TIME and GARMAISE and on selection into the DIFRET sample.

## 15. Memory Hooks
- "Clarity begins at home" means external disclosure depends on internal information flow.
- DIFRET equals divisional managers' trading profits minus top managers' trading profits.
- Positive DIFRET means divisional managers appear more informed than headquarters.
- Higher IIA means worse forecasts and more error restatements.
- Routine trades are the placebo and do not predict disclosure quality.

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Internal Information Environment]], [[Voluntary Disclosure]], [[Financial Reporting Quality]], [[Conglomerates]], or [[Insider Trading]]. The clean exam answer is: "Chen et al. 2018 use the difference between divisional and top managers' informed insider-trading profits as a measure of internal information asymmetry and show that external communication quality deteriorates when headquarters is informationally disadvantaged." Use it to argue that disclosure quality is not only about managers' incentives to reveal information, but also about whether top managers possess the information needed to communicate accurately. In a critique answer, emphasize selection into insider trading and the exclusion restrictions behind flight time and non-compete instruments, but note that the paper is stronger than a standard correlation because it validates DIFRET with multiple settings and shows that routine-trade DIFRET does not predict disclosure quality.
