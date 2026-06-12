---
type: paper
status: unread
title: Selecting Directors Using Machine Learning
authors: Isil Erel, Léa H. Stern, Chenhao Tan, Michael S. Weisbach
year: 2021
journal: Review of Financial Studies
seminar: Not clear from provided text
field: Corporate Finance
literature: Corporate Governance, Boards of Directors, Machine Learning in Finance
methods: Supervised machine learning, out-of-sample prediction, quasi-label validation, event study, SHAP, probit
datasets: BoardEx, ISS Voting Analytics, director appointment announcements, governance data
identification: Out-of-sample prediction plus quasi-label comparison to realistic alternative director candidates
main_result: Machine learning predicts which directors will perform poorly, and weakly governed firms are more likely to nominate predictably bad directors.
exam_relevance: high
must_memorize: true
tags:
  - corporate-governance
  - boards
  - director-selection
  - machine-learning
  - agency
  - shareholder-voting
  - DrJandik
created: 2026-06-12
updated: 2026-06-12
---

# Erel, Stern, Tan, and Weisbach 2021

## 1. One-Sentence Takeaway
This paper shows that machine learning can predict poor corporate director appointments using director, board, and firm characteristics, and the main contribution is to show that director selection failures are partly predictable and concentrated in weak-governance firms.

## 2. Exam-Ready Abstract
Erel, Stern, Tan, and Weisbach study whether algorithms can help firms select corporate directors and what algorithmic mistakes reveal about the director nomination process. The setting is independent director appointments at publicly traded U.S. firms from 2000 to 2014, using BoardEx director and board data and ISS Voting Analytics shareholder voting data. The authors train machine learning models on director appointments from 2000 to 2011 and test out-of-sample performance on appointments from 2012 to 2014. The main outcome is excess shareholder support in director reelections over the first three years, with robustness using strong dissent, director turnover, and appointment announcement returns. A key identification problem is selective labels, since performance is only observed for nominated directors, so the paper constructs realistic candidate pools from directors who joined smaller nearby firms and uses their observed performance as quasi-labels. The main result is that algorithms identify predictably bad directors, who tend to be male, busy, and highly networked, and weak-governance firms are more likely to nominate them. This paper connects to [[Corporate Governance]], [[Boards of Directors]], [[Shareholder Monitoring]], and [[Machine Learning in Finance]].

## 3. Research Question
Can machine learning improve corporate director selection, and what do algorithmic predictions reveal about why firms choose directors who later receive low shareholder support?

More specifically, the paper tests whether board nomination decisions overvalue observable status signals, such as gender, networks, and prior directorships, and whether agency problems in weak-governance firms help explain the nomination of predictably poor directors.

## 4. Core Mechanism

```text
Director nomination problem with many nonlinear candidate, board, and firm features
-> boards rely partly on status, networks, and familiar director profiles
-> some directors are predictably poor fits for the focal board
-> shareholders give lower support, directors turn over sooner, and appointment CARs are worse
-> weak governance allows boards to keep making these predictable nomination mistakes
```

## 5. Main Findings
1. Machine learning models predict out-of-sample director performance better than AIC-selected OLS. XGBoost and Lasso separate low-approval directors from high-approval directors, while OLS has little predictive power.
2. The selective-labels problem is addressed using realistic alternative candidates. Directors in the bottom decile of predicted performance rank around the 23rd percentile of quasi-labels, while top-decile directors rank around the 80th percentile.
3. Alternative outcomes validate the prediction. Directors predicted to perform poorly have lower appointment announcement returns, more shareholder dissent, and higher early turnover.
4. Predictably bad directors are more likely to be male, have larger networks, and hold more current and past directorships.
5. Firms with weaker governance, higher entrenchment, more co-opted boards, and fewer independent directors are more likely to nominate predictably bad directors.

## 6. Data

| Item | Details |
|---|---|
| Unit of observation | Independent director appointment to a public U.S. firm |
| Sample period | 2000 to 2014, with 2000 to 2011 training sample and 2012 to 2014 test sample |
| Main dataset | BoardEx for director and board characteristics, ISS Voting Analytics for shareholder votes |
| Key variables | Director characteristics, board composition, firm characteristics, predicted director performance, excess votes, dissent, turnover |
| Treatment or shock | No exogenous treatment. Main variation is algorithm-predicted director quality and board-selected versus algorithm-suggested candidates |
| Outcome variables | Excess shareholder votes, strong dissent below 90 percent support, director turnover within two years, appointment announcement CARs |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between director characteristics and performance is not causal because director appointments are highly selected. Boards observe private information about candidates, candidates select into firms, and firms with different governance quality may choose different kinds of directors. There is also a selective-labels problem: researchers observe performance only for directors who were actually nominated, not for the candidates who were passed over. Shareholder votes may also reflect proxy-advisor recommendations or investor preferences rather than true director productivity.

### Identification Approach
- Natural experiment: No clean natural experiment.
- Instrument: None.
- Difference in differences: Not the main design.
- Event study: Uses announcement returns around director appointments as an external validation of predicted director quality.
- Fixed effects: OLS benchmark specifications include standard controls and fixed effects, but these are not the main identification strategy.
- Matching: Constructs realistic candidate pools from directors who joined smaller neighboring firms within one year of the focal appointment.
- Placebo tests: Governance measures predict predictably bad directors but not directors who are bad only ex post and not predicted to be bad.
- Robustness: Alternative outcomes include total votes, strong dissent, two-year or three-year turnover, and appointment CARs. Results also hold in settings where large institutional investors are less likely to follow proxy advisors mechanically.
- Alternative source of variation: Out-of-sample train-test design and quasi-label comparison to feasible alternative candidates.

### Is the Identification Convincing?
- Strength: Very convincing for the predictive claim that algorithms can identify directors likely to underperform.
- Weakness: Less convincing for the causal claim that replacing board choices with algorithm choices would improve firm value, because counterfactual director performance at the focal firm is not directly observed.
- Referee concern: The quasi-label approach may not fully solve match-specific selection because a director’s performance at a nearby smaller firm may not equal performance at the focal firm.

## 8. Main Regression or Model

This is mainly a prediction paper, not a causal regression paper. The core model is:

```text
PredictedPerformance_if = f(Director_i, Board_f, Firm_f)
```

where the algorithm uses director, board, and firm characteristics available at the time of nomination to predict future director performance at firm f. The model is trained on 2000 to 2011 director appointments and tested on 2012 to 2014 appointments.

A useful exam-style validation equation is:

```text
ObservedPerformance_if =
  alpha
+ beta PredictedPerformanceDecile_if
+ epsilon_if
```

Here, beta captures whether directors predicted to perform better actually receive higher shareholder support, lower dissent, lower turnover, or better announcement returns out of sample.

The selective-labels validation can be summarized as:

```text
Rank_if =
  percentile rank of ObservedPerformance_if
  within the quasi-label distribution of feasible alternative candidates
```

The key test is whether Rank_if increases across predicted-performance deciles. A positive relationship means the algorithm is not just predicting absolute performance among selected directors, but also identifying better candidates relative to realistic alternatives.

The governance test can be summarized as:

```text
Pr(PredictablyBadDirector_f = 1) =
  Phi(beta GovernanceWeakness_f + Controls_f + epsilon_f)
```

The main economic interpretation is beta. A positive beta means weak-governance firms are more likely to nominate directors the algorithm predicts will perform poorly and who later do perform poorly.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Corporate Governance]] by showing that director selection errors are predictable and related to agency problems.
2. [[Boards of Directors]] by studying the underexplored nomination process rather than only board structure or board outcomes.
3. [[Machine Learning in Finance]] by using prediction methods to study governance choices and decision-making failures.

It differs from prior work because it treats director selection as a prediction problem and uses machine learning to identify ex ante poor candidates rather than estimating a structural governance parameter.

## 10. Closely Related Papers
- [[Hermalin and Weisbach 1998]]: Board selection and CEO bargaining power.
- [[Shivdasani and Yermack 1999]]: CEO involvement and director selection.
- [[Kramarz and Thesmar 2013]]: Social networks and board appointments.
- [[Cai Nguyen and Walkling 2017]]: Director elections and shareholder voting.
- [[Kleinberg et al. 2017]]: Prediction policy problems and selective labels.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the literature on corporate boards and director selection. How do researchers measure director quality, and what are the main identification problems?

How to use this paper:
- Main finding: Algorithms can predict poor director performance, and weak-governance firms are more likely to nominate predictably bad directors.
- Data: BoardEx director appointments linked to ISS Voting Analytics shareholder votes.
- Identification: Out-of-sample prediction, alternative outcomes, and quasi-labels from realistic candidate pools.
- Limitation: Prediction is not the same as causal evidence that algorithm-selected directors would increase firm value.
- Connection to other papers: Use with [[Hermalin and Weisbach 1998]], [[Shivdasani and Yermack 1999]], and [[Kramarz and Thesmar 2013]] to discuss agency, networks, and board capture.
- Best exam phrase: "Erel, Stern, Tan, and Weisbach turn director selection into a prediction problem and show that weak boards choose directors who are predictably unpopular with shareholders."

## 12. Hypotheses Inspired by This Paper
H1: Firms with weaker shareholder rights are more likely to nominate directors with low algorithm-predicted shareholder support.

H2: Director status signals, such as large networks and multiple board seats, increase nomination probability but decrease subsequent shareholder support conditional on nomination.

H3: Boards that use broader search processes or external candidate pools nominate less busy, more diverse, and higher predicted-performance directors.

## 13. Possible Extension or Research Design
- Research question: Does increased institutional monitoring improve the quality of director nominations?
- Hypothesis: Firms exposed to stronger passive institutional monitoring are less likely to nominate predictably bad directors.
- Data: BoardEx director appointments, ISS votes, 13F institutional ownership, Russell index assignment data.
- Identification: Regression discontinuity around the Russell 1000 and Russell 2000 cutoff, using index assignment as variation in passive institutional ownership and monitoring pressure.
- Expected result: Firms just inside the index with stronger passive ownership pressure nominate fewer directors with low predicted shareholder support.
- Contribution: Links algorithmic measures of director quality to an external governance shock and moves from prediction toward causal governance evidence.

## 14. Critiques

### Major Concern 1
The main outcome, shareholder voting support, may not fully measure director quality. It may partly reflect proxy-advisor guidelines, investor tastes, or governance fashions rather than the director’s true contribution to monitoring or advising.

### Major Concern 2
The quasi-label solution is clever but imperfect. Directors who join smaller nearby firms may differ from candidates who would have joined the focal firm, and director performance is match-specific.

### Minor Concern
The algorithm is trained on historical shareholder preferences and may embed historical biases. It can identify patterns but does not fully explain the structural mechanism behind good director performance.

### Referee Recommendation
Accept, because the paper makes a clear methodological contribution, addresses selective labels creatively, validates predictions using multiple outcomes, and connects predictably poor nominations to agency problems. The main caveat is that the welfare interpretation of algorithmic replacement should be framed carefully.

## 15. Memory Hooks
- "Director selection is a prediction problem."
- "XGBoost beats OLS."
- "Bottom predicted directors rank 23rd percentile, top predicted directors rank 80th percentile."
- "Predictably bad directors are busy, male, and highly networked."
- "Weak governance hires predictably bad directors."

## 16. Comps Use Rating

| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Corporate Governance]], [[Boards of Directors]], [[Machine Learning in Finance]], or [[Shareholder Voting]]. The clean exam answer is: "Erel, Stern, Tan, and Weisbach use machine learning on BoardEx and ISS director voting data to predict director quality and show that weak-governance firms nominate predictably bad directors." Use it to argue that board selection failures are not merely random mistakes but are partly predictable and linked to agency problems. In a critique answer, emphasize the selective-labels problem and the fact that votes are an imperfect quality measure, but note that the paper is stronger than a standard correlation because it uses out-of-sample prediction, realistic candidate pools, and multiple validation outcomes.