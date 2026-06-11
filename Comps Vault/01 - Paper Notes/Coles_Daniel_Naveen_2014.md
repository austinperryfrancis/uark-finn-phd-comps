---
type: paper
status: unread
title: Co-opted Boards
authors: Jeffrey L. Coles, Naveen D. Daniel, Lalitha Naveen
year: 2014
journal: Review of Financial Studies
seminar:  
field: Corporate Finance
literature: Corporate Governance
methods: Panel regressions, logistic regression, firm fixed effects, modified difference-in-differences
datasets: RiskMetrics, Execucomp, Compustat, CRSP
identification: Firm and year fixed effects; post-SOX exchange-rule variation
main_result: Co-opted boards monitor CEOs less effectively than non-co-opted independent boards
exam_relevance: high
must_memorize: true
tags:
  - corporate-finance
  - corporate-governance
  - board-monitoring
  - ceo-power
  - executive-compensation
  - DrJandik
created: 2026-06-03
updated: 2026-06-03
---




# Coles, Daniel, and Naveen 2014

Source: Coles, Daniel, and Naveen, "Co-opted Boards," Review of Financial Studies, 2014.

## 1. One-Sentence Takeaway
This paper shows that CEOs face weaker board monitoring when more directors were appointed after the CEO took office, using S&P 1500 board, compensation, accounting, and return data from 1996 to 2010, and the main contribution is a new measure of board capture that explains monitoring better than conventional board independence.

## 2. Exam-Ready Abstract
Coles, Daniel, and Naveen study whether independent directors are truly independent monitors when they were appointed after the CEO assumed office. They define **Co-option** as the fraction of the board appointed after the CEO took office, arguing that these directors may owe allegiance to the CEO and monitor less aggressively. Using RiskMetrics director data, Execucomp compensation data, Compustat accounting data, and CRSP returns for S&P 1500 firms from 1996 to 2010, they show that higher co-option is associated with weaker CEO turnover-performance sensitivity, higher CEO pay, weaker or unchanged pay-performance sensitivity, and higher investment. The paper also develops **Non-Co-opted Independence**, defined as the fraction of directors who are independent and were appointed before the CEO, and finds that this measure predicts stronger monitoring. The identification is mostly panel-based with firm and year fixed effects, plus a modified difference-in-differences design around post-SOX exchange listing rules that forced noncompliant firms to add independent directors. This paper belongs in [[Corporate Governance]], [[Board Monitoring]], [[CEO Power]], and [[Executive Compensation]].

## 3. Research Question
Do directors appointed after the CEO takes office become less effective monitors, even when they are formally classified as independent?

More specifically, the paper tests whether CEO influence over board appointments reduces monitoring through four channels:

1. Lower likelihood of firing the CEO after poor performance.
2. Higher CEO pay.
3. Lower or weaker CEO pay-performance sensitivity.
4. Higher investment, consistent with managerial discretion or empire building.

## 4. Core Mechanism

```text
CEO tenure and director appointments
-> more directors owe their board seat to the incumbent CEO
-> board becomes co-opted and less willing to discipline management
-> CEO receives weaker monitoring, higher pay, and more discretion
-> lower turnover-performance sensitivity, weaker incentives, and higher investment
```

## 5. Main Findings
1. **Co-option weakens CEO discipline.** Higher co-option reduces the sensitivity of forced CEO turnover to poor stock performance. The authors estimate that a one-standard-deviation increase in co-option attenuates turnover-performance sensitivity by about two-thirds.

2. **Co-option is associated with higher CEO pay.** CEO pay increases with co-option, but this is not matched by stronger pay-performance sensitivity. This supports a rent-extraction or weak-monitoring interpretation rather than a risk-compensation interpretation.

3. **Conventional independence is not enough.** Co-opted independent directors behave more like captured directors, while non-co-opted independent directors are associated with stronger monitoring, lower pay, higher pay-performance sensitivity, and lower investment.

## 6. Data

| Item | Details |
|---|---|
| Unit of observation | Firm-year |
| Sample period | 1996 to 2010 |
| Main dataset | RiskMetrics director data for S&P 500, S&P MidCap, and S&P SmallCap firms |
| Additional datasets | Execucomp for compensation, Compustat for accounting, CRSP for returns |
| Key variables | Co-option, Tenure-Weighted Co-option, Residual Co-option, Non-Co-opted Independence, Independence |
| Treatment or shock | Fraction of board appointed after the CEO took office; post-SOX exchange-rule shock for modified DiD |
| Outcome variables | Forced CEO turnover, CEO pay, CEO pay-performance sensitivity, investment |

Variable definitions: Co-option equals the number of directors appointed after the CEO assumed office divided by board size. Non-Co-opted Independence equals independent directors who were already on the board before the CEO assumed office divided by board size.

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between board co-option and firm outcomes is not causal. CEOs may become powerful because firms are already doing well, because boards deliberately give successful CEOs more discretion, or because omitted firm culture affects both director appointments and monitoring. Reverse causality is also plausible: firms with high CEO pay, weak discipline, or aggressive investment may select board structures that protect the CEO. CEO tenure is another concern because co-option mechanically rises as CEOs stay longer and have more opportunities to appoint directors.

### Identification Approach
- Natural experiment: Post-SOX NYSE and NASDAQ listing-rule changes forced firms that lacked majority-independent boards to appoint independent directors, creating an exogenous increase in co-option for noncompliant firms.
- Instrument: Not clear from provided text.
- Difference in differences: Modified DiD using pre-SOX noncompliant firms as firms more affected by the rule change.
- Event study: Not central in the provided text.
- Fixed effects: Main regressions include firm and year fixed effects.
- Matching: Not clear from provided text.
- Placebo tests: Not clear from provided text.
- Robustness: Alternative measures include Tenure-Weighted Co-option, Residual Co-option, and Residual Tenure-Weighted Co-option.
- Alternative source of variation: Exchange-rule changes following SOX.

### Is the Identification Convincing?
- Strength: The paper improves on standard board-independence regressions by introducing a measure with clear institutional content, using firm fixed effects, and exploiting an external governance shock.
- Weakness: Co-option is still partly endogenous because CEO tenure, CEO success, firm culture, and board appointment processes may jointly evolve.
- Referee concern: The SOX-induced appointments may affect monitoring through independence itself, compliance pressure, regulatory scrutiny, or broader governance changes, not only through co-option.

## 8. Main Regression or Model

```text
Forced_Turnover_it =
  alpha1 Co-option_it x Prior_Abnormal_Return_it
+ alpha2 Prior_Abnormal_Return_it
+ alpha3 Co-option_it
+ alpha4 Independence_it
+ Controls_it
+ Firm FE
+ Year FE
+ epsilon_it
```

This regression asks whether the likelihood of forced CEO turnover becomes less sensitive to poor prior performance when the board is more co-opted. The main coefficient is `alpha1`. Since poor performance should increase forced turnover, a positive interaction means co-option weakens the negative relation between performance and turnover.

```text
Outcome_it =
  beta1 Co-option_it
+ beta2 Independence_it
+ Controls_it
+ Firm FE
+ Year FE
+ epsilon_it
```

The outcomes include CEO pay, CEO pay-performance sensitivity, and investment. A positive `beta1` for pay or investment means that co-opted boards are associated with greater CEO rents or discretion. A negative `beta1` for pay-performance sensitivity would mean weaker incentive alignment.

Modified DiD version:

```text
Outcome_it =
  beta1 Noncompliant_i x PostSOX_t
+ Controls_it
+ Firm FE
+ Year FE
+ epsilon_it
```

Here, `Noncompliant_i x PostSOX_t` captures the effect of exchange-rule changes on firms forced to appoint new independent directors after SOX. The identifying idea is that these firms experienced an externally induced increase in co-option because newly appointed independent directors joined after the incumbent CEO.

## 9. Contribution to the Literature
This paper contributes to:

1. [[Corporate Governance]] by showing that formal independence is an incomplete measure of monitoring quality.
2. [[Board Monitoring]] by distinguishing independent directors who predate the CEO from those appointed during the CEO’s tenure.
3. [[Executive Compensation]] by linking board capture to CEO pay levels and incentive strength.
4. [[Agency Theory]] by connecting board capture to managerial discretion and investment policy.

It differs from prior work because it does not simply ask whether independent boards monitor better. It asks whether some independent directors are functionally captured because they were appointed under the current CEO.

## 10. Closely Related Papers
- [[Weisbach 1988]]: Board composition and CEO turnover.
- [[Hermalin and Weisbach 1998]]: CEO bargaining power and board independence.
- [[Core, Holthausen, and Larcker 1999]]: Corporate governance and CEO compensation.
- [[Gompers, Ishii, and Metrick 2003]]: Governance index and shareholder rights.
- [[Adams, Hermalin, and Weisbach 2010]]: Survey of boards and governance.
- [[Coles, Daniel, and Naveen 2008]]: Board structure and firm complexity.
- [[Morse, Nanda, and Seru 2011]]: Powerful CEOs and manipulated incentive contracts.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on board independence and CEO monitoring. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Board independence is not enough; whether directors were appointed before or after the CEO matters.
- Data: RiskMetrics, Execucomp, Compustat, and CRSP for S&P 1500 firms from 1996 to 2010.
- Identification: Firm and year fixed effects, alternative co-option measures, and a modified DiD around post-SOX exchange-rule changes.
- Limitation: Director appointment timing may still proxy for CEO tenure, success, or unobserved firm governance culture.
- Connection to other papers: Links Weisbach-style turnover monitoring to CEO power and executive compensation literatures.
- Best exam phrase: “Coles, Daniel, and Naveen show that nominally independent directors may not be substantively independent if they were appointed during the CEO’s tenure.”

## 12. Hypotheses Inspired by This Paper
H1: Firms with higher board co-option are less likely to discipline CEOs after negative performance shocks.

H2: Co-option has stronger effects in firms with weak external governance, such as low institutional ownership, staggered boards, or weak takeover threats.

H3: Co-option may increase firm value in high-human-capital or high-innovation firms if insulation allows CEOs to invest in long-term projects.

## 13. Possible Extension or Research Design
- Research question: Does board co-option affect firms’ responses to activist hedge fund campaigns?
- Hypothesis: Co-opted boards are less likely to settle with activists, less likely to replace CEOs, and more likely to resist governance reforms.
- Data: RiskMetrics or BoardEx director data, 13D activist filings, Execucomp, Compustat, CRSP.
- Identification: Difference-in-differences around activist campaign announcements, comparing high-co-option and low-co-option firms within industry and year.
- Expected result: High-co-option firms show weaker governance responses and smaller operating improvements after activism.
- Contribution: Extends co-option from internal monitoring to external governance pressure.

## 14. Critiques

### Major Concern 1
Co-option may proxy for CEO tenure rather than capture. Long-tenured CEOs mechanically appoint more directors, and tenure may reflect CEO quality, firm stability, or past performance.

### Major Concern 2
The SOX listing-rule shock may affect outcomes through multiple channels. New independent directors may change board expertise, regulatory compliance, investor attention, or governance norms, not only co-option.

### Minor Concern
Forced turnover is approximated using whether the departing CEO is younger than 60. This is common in the literature, but it can misclassify some voluntary departures as forced and some forced retirements as voluntary.

### Referee Recommendation
R&R, because the measure is important and the results are consistent across several outcomes, but the causal interpretation should be framed carefully. The paper is stronger than a standard correlation because it uses firm fixed effects, alternative co-option measures, and post-SOX listing-rule variation.

## 15. Memory Hooks
- “Independent on paper, captured in practice.”
- Co-option equals directors appointed after the CEO.
- Non-Co-opted Independence equals independent directors who predate the CEO.
- Main outcomes: turnover, pay, incentives, investment.
- Best comps line: “Not all independent directors are effective monitors.”

## 16. Comps Use Rating

| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Corporate Governance]], [[Board Monitoring]], [[CEO Power]], [[Executive Compensation]], or [[Agency Problems]]. The clean exam answer is: “Coles, Daniel, and Naveen use the fraction of directors appointed after the CEO takes office as a measure of board co-option and show that co-opted boards monitor less effectively.” Use it to argue that governance variables should measure actual monitoring incentives, not just formal independence. In a critique answer, emphasize that director appointment timing may be endogenous to CEO tenure and firm success, but note that the paper is stronger than a standard correlation because it uses firm fixed effects, alternative residualized measures, and post-SOX exchange-rule variation.

