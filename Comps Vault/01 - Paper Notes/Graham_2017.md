---
type: paper
status: unread
title: Tax Rates and Corporate Decision Making
authors: John R. Graham, Michelle Hanlon, Terry Shevlin, Nemit Shroff
year: 2017
journal: Review of Financial Studies
professor: DrJandik
seminar: null
jandik_paper_number: 8
jandik_week: 2
jandik_topic: 'Capital structure: determinants and targets, taxes, and information asymmetry'
jandik_done: true
field: Corporate Finance
literature:
- Corporate Taxes
- '[[Capital Structure]]'
- Behavioral Corporate Finance
- Corporate Investment
methods:
- Survey
- Probit
- Panel Regressions
- Matched Benchmark Sample
- DiD-like Design
datasets:
- Corporate tax executive survey
- '[[Compustat]]'
- LinkedIn education data
identification: Survey evidence plus variation in the gap between marginal tax rates and GAAP effective tax rates, benchmarked against firms using MTR or STR
main_result: Many firms use GAAP effective tax rates rather than marginal tax rates for incremental decisions, and this is associated with suboptimal leverage and weaker investment responsiveness.
exam_relevance: high
must_memorize: true
tags:
- corporate-taxes
- capital-structure
- behavioral-corporate-finance
- investment
- survey-evidence
- corporate-finance
created: 2026-06-03
updated: 2026-06-03
---

# Graham et al. 2017

## 1. One-Sentence Takeaway
This paper shows that many firms use average tax rates rather than marginal tax rates in corporate decision making using a survey of tax executives matched to Compustat data, and the main contribution is showing that incorrect tax inputs can lead to inefficient leverage and investment decisions.

## 2. Exam-Ready Abstract
Graham et al. ask whether firms use the theoretically correct tax rate when making incremental corporate decisions such as capital structure and investment. Standard theory says firms should use the marginal tax rate, but the authors survey corporate tax executives and find that many firms instead use the GAAP effective tax rate or statutory tax rate. The paper interprets statutory tax rate use as a possible heuristic when it approximates the MTR, while GAAP ETR use is linked to salience, especially among public firms and firms with high analyst following. They then combine survey responses with Compustat data from 1997 to 2006 and test whether firms using ETRs make worse decisions when the wedge between MTR and ETR is larger. They find that ETR-using firms make suboptimal leverage choices and are less responsive to investment opportunities when the MTR and ETR differ. The paper contributes to [[Corporate Taxes]], [[Capital Structure]], [[Corporate Investment]], and [[Behavioral Corporate Finance]].

## 3. Research Question
What tax rate do firms actually use when incorporating taxes into corporate decisions, and does using the wrong tax rate lead to inefficient decisions?

More specifically: the paper tests whether managers use theoretically correct marginal tax rates or simpler, more salient rates such as statutory tax rates and GAAP effective tax rates, and whether these choices affect capital structure and investment efficiency.

## 4. Core Mechanism

```text
Managers need tax inputs for incremental decisions
-> theory says use marginal tax rate
-> some managers use GAAP ETR because it is salient in financial reporting
-> incorrect tax input distorts after-tax cash flow or tax shield calculations
-> firms choose suboptimal leverage or respond weakly to investment opportunities
```

## 5. Main Findings
1. Fewer than 13% of firms report using the MTR in any decision-making context. Many firms instead use GAAP ETRs or statutory tax rates.
2. Public firms and firms with high analyst following are more likely to use GAAP ETRs, consistent with financial reporting salience. More educated tax executives and executives with accounting degrees are less likely to use ETRs.
3. Firms using ETRs make worse decisions when their ETR differs from their MTR: they have more suboptimal leverage and lower sensitivity of investment to investment opportunities.

## 6. Data

| Item | Details |
|---|---|
| Unit of observation | Survey firm for tax-rate choice tests; firm-year for decision outcome tests |
| Sample period | Survey conducted in 2007; Compustat panel primarily 1997 to 2006 |
| Main dataset | Survey of corporate tax executives, matched to Compustat financial data |
| Key variables | Use GAAP ETR, Use STR, Use MTR, MTR minus GAAP ETR, analyst following, public firm indicator, education, accounting degree |
| Treatment or shock | No clean shock. Treatment is firm use of GAAP ETR, interacted with the MTR versus ETR wedge |
| Outcome variables | Leverage conservatism, equilibrium leverage factor, total value loss from capital structure, capital expenditure, investment sensitivity to Tobin's Q |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between tax-rate choice and firm outcomes is not causal because firms that use GAAP ETRs may differ systematically from firms that use MTRs or STRs. For example, public firms, firms with analyst pressure, firms with multinational operations, firms with different tax planning opportunities, and firms with different manager education may also differ in leverage and investment behavior. The MTR versus ETR wedge may also proxy for omitted firm characteristics such as NOLs, foreign income, profitability, or tax planning complexity. Survey responses may also be noisy or reflect what tax executives believe should be used rather than what decision makers actually use.

### Identification Approach
- Natural experiment: None.
- Instrument: None.
- Difference in differences: DiD-like benchmark design comparing ETR users to matched MTR or STR users as the MTR versus ETR wedge varies.
- Event study: Not central.
- Fixed effects: Industry and year fixed effects in main tests; firm fixed effects used in robustness.
- Matching: Propensity-score style matched benchmark sample of ETR users and MTR or STR users based on observable determinants of tax-rate choice.
- Placebo tests: They test whether the MTR versus ETR wedge predicts decision inefficiency among firms that use MTR or STR. It should not, and generally does not.
- Robustness: Alternative MTR measures, alternative investment opportunity measures, shorter 2001 to 2006 sample, post-survey tests, domestic-firm subsample, median regressions, and controls for debt and investment determinants.
- Alternative source of variation: Within-firm time-series variation in the gap between estimated MTR and GAAP ETR.

### Is the Identification Convincing?
- Strength: The survey directly observes an otherwise unobservable decision input, which is rare in corporate finance. The MTR versus ETR wedge gives a sharper prediction: ETR use should matter more when the wedge is large.
- Weakness: Tax-rate choice is not randomly assigned, and survey timing creates possible look-ahead concerns because the survey occurs in 2007 while much of the panel is 1997 to 2006.
- Referee concern: The MTR proxy is estimated with measurement error, and the MTR versus ETR wedge could capture multinational tax planning, foreign earnings, NOL status, or omitted investment opportunities.

## 8. Main Regression or Model

Tax-rate choice model:

```text
Pr(Use Tax Rate_i = 1) =
  f(Public_i, Size_i, ForeignAssets_i, AnalystFollowing_i,
    R&D_i, InstitutionalOwnership_i, Competition_i,
    Education_i, AccountingDegree_i, Controls_i)
```

This model asks which firm and manager characteristics predict use of ETR, STR, or MTR. The key interpretation is descriptive, not causal. Public status and analyst following proxy for GAAP salience. Education and accounting background proxy for technical knowledge.

Capital structure consequence model:

```text
LeverageInefficiency_it =
  beta1 (MTR - GAAP ETR)_{i,t-1}
+ Controls_it
+ Industry FE
+ Year FE
+ epsilon_it
```

This is estimated among firms that use GAAP ETR for capital structure decisions. If the ETR is below the MTR, the firm underestimates the tax benefit of debt and should be too conservative. If the ETR is above the MTR, the firm overestimates the tax benefit and should be too aggressive.

Benchmark model:

```text
LeverageInefficiency_it =
  beta1 (MTR - GAAP ETR)_{i,t-1}
+ beta2 Use GAAP ETR_i
+ beta3 Use GAAP ETR_i x (MTR - GAAP ETR)_{i,t-1}
+ Controls_it
+ Industry FE
+ Year FE
+ epsilon_it
```

The main coefficient is beta3. It tests whether the MTR versus ETR wedge matters more for firms that actually use GAAP ETR than for matched firms that use MTR or STR.

Investment model:

```text
Investment_it =
  beta1 InvestmentOpportunities_it
+ beta2 |MTR - GAAP ETR|_{i,t-1}
+ beta3 |MTR - GAAP ETR|_{i,t-1} x InvestmentOpportunities_it
+ Controls_it
+ Industry FE
+ Year FE
+ epsilon_it
```

The main coefficient is beta3. A negative beta3 means that when the MTR and ETR are farther apart, ETR-using firms become less responsive to investment opportunities.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Corporate Taxes]] by showing that the tax rate firms use internally may differ from the theoretically correct MTR.
2. [[Capital Structure]] by linking tax input errors to suboptimal debt policy.
3. [[Behavioral Corporate Finance]] by showing that managerial heuristics and salience affect corporate policies.
4. [[Corporate Investment]] by showing that tax-rate errors reduce investment responsiveness to opportunities.

It differs from prior work because most tax and capital structure papers infer tax incentives from archival proxies, while this paper directly surveys managers about the tax-rate inputs they use.

## 10. Closely Related Papers
- [[Graham 1996]]: Develops simulated marginal tax rates and shows taxes matter for capital structure.
- [[Graham 2000]]: Estimates tax benefits of debt and shows firms appear conservative in debt policy.
- [[Graham and Harvey 2001]]: Uses survey evidence to study corporate finance practice.
- [[van Binsbergen, Graham, and Yang 2010]]: Provides estimates of optimal capital structure and costs of debt.
- [[Baker and Wurgler 2013]]: Calls for behavioral explanations in corporate finance, including capital structure.
- [[Heider and Ljungqvist 2015]]: Examines taxes and corporate leverage.
- [[Hanlon and Heitzman 2010]]: Reviews tax research in accounting and finance.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the literature on taxes and corporate capital structure. How do taxes affect leverage, and what are the empirical challenges in showing that firms respond optimally to tax incentives?

How to use this paper:
- Main finding: Firms often use the wrong tax rate for incremental decisions, especially GAAP ETR instead of MTR, and this is associated with inefficient leverage and investment.
- Data: Survey of tax executives combined with Compustat and manager education data.
- Identification: DiD-like benchmark design using the MTR versus ETR wedge and comparing ETR users to matched MTR or STR users.
- Limitation: Survey responses and tax-rate choice are endogenous; MTRs are estimated rather than observed.
- Connection to other papers: Complements [[Graham 2000]] by explaining why some firms leave tax benefits of debt on the table.
- Best exam phrase: "Graham et al. 2017 show that the relevant tax input is not just hard for researchers to measure. It may also be mismeasured by the managers themselves."

## 12. Hypotheses Inspired by This Paper
H1: Firms with more financially sophisticated executives are less likely to use average tax rates in investment and financing decisions.

H2: Firms facing greater capital market pressure are more likely to use GAAP-based tax measures because financial reporting numbers are more salient.

H3: The negative effect of tax-rate input errors on corporate decisions is larger when firms have weaker governance or less external monitoring.

## 13. Possible Extension or Research Design
- Research question: Did the 2017 Tax Cuts and Jobs Act reduce or increase managerial tax-rate mistakes by making statutory tax rates more salient and changing the gap between statutory, effective, and marginal tax rates?
- Hypothesis: Firms that relied on GAAP ETRs before TCJA exhibit larger changes in leverage and investment after TCJA when their ETR and MTR wedges change.
- Data: Public firms from Compustat, estimated MTRs, GAAP ETRs, 10-K tax disclosures, analyst following, governance data, and possibly survey or text-based proxies for tax sophistication.
- Identification: Difference in differences around TCJA comparing firms with high pre-TCJA MTR versus ETR wedges to firms with low wedges, with heterogeneity by financial reporting pressure and tax sophistication.
- Expected result: Firms with high tax salience but low tax sophistication adjust less efficiently to the tax reform.
- Contribution: Connects behavioral tax-input errors to a major tax policy shock and modern corporate decision making.

## 14. Critiques

### Major Concern 1
Tax-rate choice is endogenous. Firms that use ETRs differ from firms that use MTRs or STRs in ways that may also determine leverage and investment behavior. The matched benchmark design helps, but it cannot fully rule out unobservable differences in sophistication, tax planning, or governance.

### Major Concern 2
The MTR is estimated, not observed. Measurement error in simulated MTRs could mechanically create a wedge between MTR and ETR that is correlated with foreign income, NOLs, or investment opportunities.

### Minor Concern
The survey was conducted in 2007, while the main archival tests use earlier years from 1997 to 2006. If firms changed their tax-rate inputs over time, the survey may not perfectly measure historical decision rules.

### Referee Recommendation
R&R / Accept, because the paper provides rare direct evidence on managerial decision inputs and ties those inputs to economic outcomes, but the causal interpretation depends on strong assumptions about survey validity, MTR measurement, and the benchmark sample.

## 15. Memory Hooks
- "Average versus marginal tax rates in the C-suite."
- "GAAP ETR is salient, but MTR is theoretically correct."
- "Public firms and analyst pressure make accounting numbers more salient."
- "Wrong tax input means wrong debt tax shield and wrong investment cash flows."
- "Survey plus Compustat: managers do not just face tax incentives, they may misunderstand them."

## 16. Comps Use Rating

| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Corporate Taxes]], [[Capital Structure]], [[Behavioral Corporate Finance]], [[Corporate Investment]], or [[Survey Evidence]]. The clean exam answer is: "Graham et al. 2017 survey tax executives and show that many firms use GAAP effective tax rates rather than marginal tax rates, and that firms using ETRs make less efficient leverage and investment decisions when ETRs diverge from MTRs." Use it to argue that firms may fail to optimize not only because of adjustment costs or agency problems, but also because managers use incorrect decision inputs. In a critique answer, emphasize that tax-rate choice is endogenous and MTRs are estimated, but note that the paper is stronger than a standard correlation because it directly observes reported decision inputs and uses a benchmark sample where the MTR versus ETR wedge should not matter.