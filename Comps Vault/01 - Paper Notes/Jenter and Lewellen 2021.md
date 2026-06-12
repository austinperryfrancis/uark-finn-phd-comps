---
type: paper
status: unread
title: Performance-Induced CEO Turnover
authors: Dirk Jenter; Katharina Lewellen
year: 2021
journal: Review of Financial Studies
professor: DrJandik
seminar: null
jandik_paper_number: 56
jandik_week: 14
jandik_topic: Governance
jandik_done: false
field: Corporate Finance
literature:
- CEO Turnover
- '[[Corporate Governance]]'
- Managerial Incentives
- Bayesian Learning
methods:
- Probit
- Two-probit decomposition
- Event analysis
- Turnover classification
datasets:
- '[[ExecuComp]]'
- '[[CRSP]]'
- '[[Compustat]]'
- Factiva
- Thomson Reuters 13F
- WhaleWisdom 13D
- misconduct datasets
identification: Turnover-performance decomposition using high-performance benchmark and two-probit model
main_result: 38% to 55% of CEO turnovers are performance induced, substantially more than forced-turnover classifications imply.
exam_relevance: high
must_memorize: true
tags:
- corporate-governance
- ceo-turnover
- board-monitoring
- managerial-incentives
- bayesian-learning
created: 2026-06-12
updated: 2026-06-12
---

# Jenter and Lewellen 2021

## 1. One-Sentence Takeaway
This paper shows that poor firm performance causes far more CEO turnover than forced-turnover classifications imply using a new measure of performance-induced turnover, and the main contribution is to reframe CEO turnover as the dissolution of bad CEO-firm matches rather than only explicit board firings.

## 2. Exam-Ready Abstract
Jenter and Lewellen revisit the classic question of how strongly CEO turnover responds to firm performance. Instead of classifying departures as forced or voluntary, they define performance-induced turnover as turnover that would not have occurred had performance been good. Using ExecuComp CEO spells from 1993 to 2011, CRSP returns, Compustat controls, and hand-verified turnover data from Factiva, they estimate that 38% to 55% of CEO turnovers are performance induced. This is much larger than the rate of forced turnovers because many departures classified as voluntary are much more common after poor performance. They also test Bayesian learning models and find that boards weight recent performance much more than old performance, suggesting either slow learning or frequent shocks to CEO ability or CEO-firm match quality. Around misconduct, activist campaigns, and institutional exits, increases in turnover are mostly performance induced rather than unrelated to performance. This paper belongs in [[Corporate Governance]], [[CEO Turnover]], [[Managerial Incentives]], and [[Bayesian Learning in Corporate Finance]].

## 3. Research Question
What fraction of CEO turnover is actually caused by poor firm performance?

More specifically, the paper asks whether the literature underestimates performance-related turnover by focusing on forced turnover classifications, and whether the observed turnover-performance relation is consistent with boards learning about CEO ability over time.

## 4. Core Mechanism

```text
Poor firm performance
-> board and CEO receive negative signal about CEO ability or CEO-firm match quality
-> bad match becomes less valuable relative to outside options
-> board fires CEO, CEO retires, or CEO exits under pressure
-> CEO-firm match dissolves
```

For adverse events:

```text
Misconduct, activist campaign, or institutional exit
-> negative signal about governance, CEO quality, or investor confidence
-> board lowers tolerance for poor performance
-> smaller performance decline is enough to trigger turnover
-> higher performance-induced CEO turnover
```

## 5. Main Findings
1. Between 38% and 55% of CEO turnovers are performance induced, roughly twice the fraction identified as forced in prior studies.
2. Many turnovers classified as voluntary are performance related. Voluntary turnover rises sharply at low performance levels, so forced-turnover algorithms understate the importance of performance.
3. Performance-induced turnover depends mostly on the most recent 3 to 4 years of performance. Performance from 4 or more years ago is mostly ignored.
4. Performance-induced turnover declines only slowly with tenure, while forced turnover declines sharply with tenure. This suggests that part of the tenure pattern in forced turnover is a classification artifact.
5. Corporate misconduct, activist campaigns, and institutional exits increase performance-induced turnover, not other turnover. Boards appear to treat these events as negative signals or as pressure to remove underperforming CEOs.

## 6. Data

| Item | Details |
|---|---|
| Unit of observation | CEO-year |
| Sample period | 1993 to 2011 for main ExecuComp sample |
| Main dataset | ExecuComp CEO spells, hand-verified turnover data from Factiva, CRSP returns, Compustat accounting data |
| Key variables | CEO turnover, forced turnover, voluntary turnover, performance-induced turnover, CEO age, CEO tenure, firm size, dividend payer |
| Treatment or shock | Poor industry-adjusted stock performance; adverse corporate events such as misconduct, activism, and institutional exits |
| Outcome variables | CEO turnover probability, performance-induced turnover probability, other turnover probability, forced turnover probability |
| Performance measure | Average industry-adjusted monthly stock returns scaled by return volatility |
| Event data | SEC or DOJ financial misrepresentation enforcement, accounting restatements, securities class actions, option backdating scandals, Schedule 13D activism, 13F institutional ownership declines |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between poor performance and CEO turnover is not automatically causal because poor performance may reflect industry shocks, firm shocks, private board information, CEO ability, or anticipated turnover. Boards observe private signals that researchers do not observe, so lagged public returns may be an incomplete measure of information about the CEO. There is also measurement error in forced versus voluntary turnover classifications because firms and CEOs often have incentives to make forced departures look voluntary. Finally, adverse events such as activism or institutional exits are endogenous because they often follow poor performance and may reflect unobserved governance problems.

### Identification Approach
- Natural experiment: Not a clean natural experiment.
- Instrument: None.
- Difference in differences: Not the main design.
- Event study: Used around misconduct, activist campaigns, and institutional exits to examine whether turnover changes after adverse events.
- Fixed effects: Not central in the provided text. The main models use probit specifications with controls.
- Matching: Not central in the provided text.
- Placebo tests: Not clear from provided text.
- Robustness: Compares two estimation approaches, compares performance-induced turnover with Parrino-style forced turnover, uses alternative performance windows, and examines adverse events.
- Alternative source of variation: Uses high-performance turnover rates as the benchmark for turnover unrelated to performance, then attributes excess turnover at lower performance levels to performance.

### Is the Identification Convincing?
- Strength: The paper directly addresses a measurement problem in the CEO turnover literature. It does not require labeling each turnover as forced or voluntary.
- Weakness: The decomposition depends on assumptions about what turnover would occur at high performance and on functional form in the two-probit model.
- Referee concern: The paper estimates performance-induced turnover rather than a clean causal effect of performance shocks. A referee might worry that the high-performance benchmark and two-probit assumptions mechanically drive the result.

## 8. Main Regression or Model

The conceptual decomposition is:

```text
P_turn(x_t) =
  P_other
+ P_perf_ind(x_t)
- P_other * P_perf_ind(x_t)
```

Rearranged:

```text
P_perf_ind(x_t) =
  [P_turn(x_t) - P_other] / [1 - P_other]
```

The key idea is that observed turnover combines two processes. One is unrelated to performance, such as retirement for reasons unrelated to the firm. The other is performance induced and declines as performance improves.

The conservative decile model is:

```text
P_turn(x_t) =
  Phi(beta_1
     + beta_2 Decile_2
     + ...
     + beta_10 Decile_10
     + gamma Controls_t)
```

Here, the top performance decile estimates other turnover. Any excess turnover in lower performance deciles is interpreted as performance-induced turnover.

The two-probit model is:

```text
P_turn(X_t) =
  Phi_other(alpha_1 + alpha_2 Z_1t)
+ [1 - Phi_other(alpha_1 + alpha_2 Z_1t)]
  * Phi_perf_ind(beta_1 + beta_2 X_t + gamma Z_2t)
```

The coefficient beta_2 is the performance sensitivity of performance-induced turnover. A more negative beta_2 means poor performance more strongly increases the probability that the CEO-firm match ends.

For adverse events:

```text
P_perf_ind =
  Phi(beta_1
     + beta_2 Performance_t
     + beta_3 Event_t
     + beta_4 Performance_t * Event_t
     + gamma Controls_t)
```

beta_3 asks whether the event raises the baseline probability of performance-induced turnover. beta_4 asks whether performance becomes more strongly tied to turnover after the event.

## 9. Contribution to the Literature
This paper contributes to:
1. [[CEO Turnover]] by showing that forced-turnover measures substantially understate the turnover caused by poor performance.
2. [[Corporate Governance]] by reframing board monitoring as the dissolution of bad CEO-firm matches, not only explicit firings.
3. [[Managerial Incentives]] by showing that dismissal incentives are stronger than the prior forced-turnover literature suggested.
4. [[Bayesian Learning in Corporate Finance]] by testing whether boards learn about CEO ability in the way standard models predict.

It differs from prior work because it does not begin by classifying turnovers as forced or voluntary. It instead asks whether the observed turnover would have happened if performance had been good.

## 10. Closely Related Papers
- [[Coughlan and Schmidt 1985]]: Early evidence on CEO turnover and firm performance.
- [[Warner, Watts, and Wruck 1988]]: Classic CEO turnover-performance relation.
- [[Weisbach 1988]]: Board composition and CEO turnover.
- [[Jensen and Murphy 1990]]: CEO incentives and the role of dismissal.
- [[Parrino 1997]]: Forced turnover classification algorithm.
- [[Hermalin and Weisbach 1998]]: Board governance and CEO entrenchment.
- [[Kaplan and Minton 2012]]: CEO turnover and performance sensitivity in later samples.
- [[Taylor 2010]]: Learning and CEO turnover models.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on CEO turnover and firm performance. Discuss how papers measure turnover and how they establish whether boards discipline poorly performing CEOs.

How to use this paper:
- Main finding: 38% to 55% of CEO turnovers are performance induced, more than forced-turnover classifications imply.
- Data: ExecuComp CEO spells, CRSP stock returns, Compustat controls, hand-verified turnover data, and adverse event datasets.
- Identification: Decomposes turnover into performance-induced and other turnover using high-performance turnover rates and a two-probit model.
- Limitation: It is not a clean natural experiment. It relies on assumptions about the turnover process.
- Connection to other papers: Use after [[Jensen and Murphy 1990]], [[Weisbach 1988]], and [[Parrino 1997]] to show how measurement changes conclusions about CEO discipline.
- Best exam phrase: "Jenter and Lewellen show that the classic forced-turnover literature understates board discipline because many apparently voluntary departures are performance induced."

## 12. Hypotheses Inspired by This Paper
H1: CEO turnover classified as voluntary is negatively related to prior firm performance.

H2: If CEO ability or CEO-firm match quality changes over time, recent performance should predict turnover more strongly than older performance.

H3: Adverse corporate events should increase performance-induced turnover mainly among poor performers, not among firms with very high performance.

## 13. Possible Extension or Research Design
- Research question: Do boards distinguish between CEO-driven underperformance and exogenous industry-wide underperformance when replacing CEOs?
- Hypothesis: CEO turnover should respond more strongly to idiosyncratic underperformance than to peer-wide or industry-wide negative shocks.
- Data: ExecuComp, CRSP, Compustat, product market peers, industry shocks, commodity shocks, and BoardEx board characteristics.
- Identification: Triple-difference design comparing low-performing firms hit by plausibly exogenous industry shocks with low-performing firms whose underperformance is idiosyncratic, interacted with governance strength.
- Expected result: Strong boards should punish idiosyncratic underperformance more than exogenous underperformance.
- Contribution: This would separate board learning about CEO ability from board reactions to bad outcomes.

## 14. Critiques

### Major Concern 1
The key decomposition assumes that turnover at high performance is unrelated to performance. If some high-performing CEOs leave because performance was good, such as being hired away, or if some high-performing CEOs still leave because performance could have been even better, the benchmark may mismeasure other turnover.

### Major Concern 2
The two-probit model imposes structure on two latent turnover processes that are not separately observed. The results are informative, but the design is not equivalent to randomly assigning firm performance or CEO quality.

### Minor Concern
The sample is ExecuComp public firms, so the findings may not generalize to private firms, smaller firms, founder-led firms outside ExecuComp, or non-U.S. governance systems.

### Referee Recommendation
Accept, because the paper makes a clear measurement and conceptual contribution to a central corporate governance question, even though the identification is model-based rather than shock-based.

## 15. Memory Hooks
- "38 to 55": the share of all CEO turnovers that are performance induced.
- "Voluntary does not mean unrelated to performance."
- "Boards remember 3 to 4 years, then mostly forget."
- "Forced turnover falls with tenure partly because the algorithm calls older CEO exits voluntary."
- "Adverse events shift the firing threshold."

## 16. Comps Use Rating

| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[CEO Turnover]], [[Corporate Governance]], [[Managerial Incentives]], [[Board Monitoring]], or [[Bayesian Learning]]. The clean exam answer is: "Jenter and Lewellen use a performance-induced turnover decomposition and show that 38% to 55% of CEO turnovers would not have occurred had performance been good." Use it to argue that boards discipline CEOs more than the forced-turnover literature suggests, but that measuring discipline requires care because many performance-related exits look voluntary. In a critique answer, emphasize that the paper is model-based rather than a clean natural experiment, but note that it is stronger than a standard correlation because it directly addresses misclassification in forced versus voluntary turnover.