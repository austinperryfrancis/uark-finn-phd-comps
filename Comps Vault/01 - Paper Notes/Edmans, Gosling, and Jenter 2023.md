---
type: paper
status: unread
title: 'CEO Compensation: Evidence from the Field'
authors: Alex Edmans, Tom Gosling, Dirk Jenter
year: 2023
journal: Journal of Financial Economics
professor: DrJandik
seminar: null
jandik_paper_number: 58
jandik_week: 15
jandik_topic: Governance
jandik_done: false
field: Corporate Finance
literature:
- Executive Compensation
- '[[Corporate Governance]]'
- Survey Evidence
methods:
- Survey
- Interviews
- Descriptive Evidence
datasets:
- Survey of UK non-executive directors and institutional investors
identification: Survey evidence, no causal identification
main_result: CEO pay is shaped by fairness, reputation, investor pressure, and controversy constraints, not just participation and incentive constraints.
exam_relevance: high
must_memorize: true
tags:
- executive-compensation
- corporate-governance
- CEO-incentives
- survey-evidence
- fairness
- proxy-advisors
created: 2026-06-12
updated: 2026-06-12
---

# Edmans, Gosling, and Jenter 2023

## 1. One-Sentence Takeaway
This paper shows that CEO pay is shaped by fairness concerns, reputation, investor pressure, and controversy constraints using a survey of UK directors and institutional investors, and the main contribution is to show that real-world compensation design is richer than standard principal-agent models of participation and incentives.

## 2. Exam-Ready Abstract
Edmans, Gosling, and Jenter study how CEO compensation is actually set, focusing on the objectives, constraints, and determinants perceived by directors and investors. The setting is UK public firms, where say-on-pay, remuneration committees, institutional investor oversight, and proxy advisor pressure make CEO pay highly salient. The authors survey 203 non-executive directors of FTSE All-Share firms and 159 institutional investors in UK equities in late 2020, supplemented with free-text responses and 14 interviews. The main result is that boards face constraints beyond participation and incentive compatibility, especially investor approval, proxy advisor pressure, employee controversy, and public legitimacy. A central mechanism is fairness: CEO pay matters not only for consumption incentives, but also as recognition of contribution, a signal of status, and a benchmark relative to peers and past pay. The paper contributes to [[Executive Compensation]], [[Corporate Governance]], [[Contract Theory]], and [[Survey Evidence in Corporate Finance]].

## 3. Research Question
What do directors and investors believe determines CEO pay, and how does the real-world pay-setting process differ from standard executive compensation theory?

More specifically: the paper tests whether CEO pay is governed only by participation and incentive constraints, or whether fairness, reputation, controversy avoidance, proxy advisors, investors, and internal equity also shape pay levels and pay structures.

## 4. Core Mechanism
Use this chain for comps:

```text
Investor, proxy advisor, employee, and public scrutiny of CEO pay
-> boards face controversy and approval constraints beyond IR and IC
-> boards reduce pay levels or use more standardized pay structures
-> CEOs interpret pay relative to fairness reference points, peers, past pay, and perceived contribution
-> motivation, retention, recognition, and pay design depend on fairness and reputation, not just consumption incentives
```

Alternative mechanism for flow pay:

```text
Good CEO performance
-> board awards higher realized or expected flow pay
-> CEO receives public and internal recognition
-> fairness concerns are satisfied and intrinsic motivation is preserved
-> pay-for-performance exists even when portfolio incentives are already strong
```

## 5. Main Findings
1. Directors and investors disagree about the key constraint: directors emphasize attracting and retaining the CEO, while investors emphasize incentive design and long-term shareholder value.
2. Boards face non-standard constraints. A large share of directors would sacrifice shareholder value to avoid CEO pay controversy, and many report being forced into lower pay or inferior, more standardized pay structures.
3. Fairness is central. CEO pay affects motivation because CEOs compare pay to peers, past pay, perceived contribution, and internal status. Flow pay provides recognition in a way that equity portfolio gains do not.
4. Intrinsic motivation and reputation are viewed as stronger CEO motivators than incentive pay, while career concerns such as being fired or moving to a bigger firm receive relatively low support.
5. Standard agency predictions are incomplete. Risk aversion and firm risk receive little support as determinants of fixed versus variable pay, and relative performance evaluation is not universally used because of fairness and implementation concerns.
6. Directors and investors disagree sharply on pay cuts and incentive horizon. Investors think pay can often be reduced and incentives lengthened; directors worry about demotivation, retention, and effectiveness.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Survey respondent, either non-executive director or institutional investor |
| Sample period | Survey fielded in November and December 2020 |
| Main dataset | Anonymous Qualtrics survey of 203 non-executive directors of FTSE All-Share firms and 159 institutional investors in UK equities |
| Key variables | Survey responses on CEO pay objectives, constraints, pay levels, variable pay, fairness, peer benchmarking, investor influence, proxy advisors, intrinsic motivation, reputation |
| Treatment or shock | No treatment or shock. The study uses elicited beliefs and reported practices |
| Outcome variables | Perceived determinants of CEO pay, willingness to sacrifice shareholder value, consequences of pay cuts, reasons for variable pay, views on long-term incentives and relative performance evaluation |

## 7. Identification Strategy

### Endogeneity Problem
The paper is not designed as a causal archival study. A simple correlation between observed CEO pay and firm outcomes would be difficult to interpret because CEO pay is chosen endogenously by boards, reflects CEO ability, firm complexity, labor market conditions, shareholder preferences, firm performance, and governance quality. Reverse causality is also plausible because good performance can raise pay, while high-powered pay can affect performance. Omitted variables such as CEO talent, bargaining power, board beliefs, private labor market information, investor pressure, and firm culture are difficult to observe. Measurement error is important because standard datasets observe the final compensation contract but not the latent objective function or constraints behind it.

### Identification Approach
- Natural experiment: None.
- Instrument: None.
- Difference in differences: None.
- Event study: None.
- Fixed effects: None.
- Matching: None.
- Placebo tests: Not an archival placebo design.
- Robustness: Survey design choices include anonymity, practitioner beta-testing, randomized answer order, free-text fields, and follow-up interviews.
- Alternative source of variation: Cross-respondent differences between directors and investors, plus differences in views across compensation topics.

### Is the Identification Convincing?
- Strength: Very useful for mechanism discovery. The paper directly asks directors and investors about unobservable beliefs, constraints, and motives that archival data cannot capture.
- Weakness: It identifies perceived mechanisms, not causal effects. Respondents may rationalize, misremember, interpret questions differently, or give socially acceptable answers.
- Referee concern: The sample is UK-based and fielded during COVID-19, so external pressure on pay may be unusually salient. The authors argue many findings likely generalize, but this cannot be formally proven.

## 8. Main Regression or Model

This is a survey paper, not a regression-based causal design. A useful way to write the implicit empirical object is:

```text
SurveyResponse_iq =
  f(RespondentType_i, PayIssue_q, Beliefs_i, Constraints_i, FirmContext_i) + epsilon_iq
```

In words, each response reflects the respondent’s role, the specific pay-setting issue, beliefs about CEO motivation, perceived constraints, and context.

A comps-friendly conceptual model is:

```text
CEO Utility =
  ConsumptionUtility(Pay)
+ RecognitionUtility(FlowPay, Performance)
- FairnessLoss(PeerPay, PastPay, PerceivedContribution, InternalStatus)

Board Objective =
  ShareholderValue
- CEOCompensation
- ControversyCost(Investors, ProxyAdvisors, Employees, Customers, Policymakers)
- FairnessCost(EmployeePay, PeerCEOPay, ShareholderReturns)
```

The key insight is that compensation does not only solve a standard IR and IC problem. Pay also manages fairness reference points and external controversy. Flow pay matters because it provides recognition, even when the CEO already has large portfolio incentives.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Executive Compensation]] by showing that actual pay-setting departs from standard agency models.
2. [[Corporate Governance]] by showing that investors and proxy advisors constrain boards, sometimes in ways boards believe reduce shareholder value.
3. [[Contract Theory]] by motivating models with fairness, reference points, recognition, and multiple principals.
4. [[Survey Evidence in Corporate Finance]] by using field evidence from directors and investors to uncover mechanisms not visible in archival data.

It differs from prior work because it studies the pay-setting process directly rather than inferring it from observed pay contracts. It also surveys both directors and investors, which lets the authors show disagreement between the parties that jointly shape CEO pay.

## 10. Closely Related Papers
- [[Murphy 2013]]: Reviews executive compensation facts and theories; Edmans, Gosling, and Jenter provide field evidence on which theories practitioners actually believe.
- [[Edmans and Gabaix 2016]]: Modern primer on executive compensation theory; this paper challenges and enriches the standard theoretical objective function.
- [[Edmans, Gabaix, and Jenter 2017]]: Survey of theory and evidence on executive compensation; this paper supplies new practitioner evidence on mechanisms.
- [[Gabaix and Landier 2008]]: Talent assignment model of CEO pay; this paper supports ability as important but adds fairness and reference-point channels.
- [[Bebchuk and Fried 2004]]: Rent extraction view of pay without performance; this paper offers a third view, disagreement and constraints rather than only optimal contracting or managerial capture.
- [[Graham and Harvey 2001]]: Classic corporate finance survey; this paper is analogous in method but applied to CEO compensation.
- [[Malenko and Shen 2016]]: Proxy advisors affect voting outcomes; this paper shows directors perceive proxy advisors as a binding constraint on pay design.
- [[Daniel, Li, and Naveen 2020]]: Pay-for-luck can be symmetric; this paper provides a fairness-based explanation for why pay-for-luck may persist.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the executive compensation literature. Discuss how firms set CEO pay, how the literature establishes causality, and what mechanisms remain difficult to observe.

How to use this paper:
- Main finding: CEO pay is not just participation plus incentives. Fairness, recognition, reputation, investors, proxy advisors, and controversy constraints are central.
- Data: Survey of UK FTSE All-Share non-executive directors and institutional investors, plus interviews.
- Identification: Not causal. Use it as field evidence on mechanisms and beliefs, not as proof that pay causes performance.
- Limitation: Survey responses may reflect perceptions, rationalizations, UK institutions, and COVID-era salience.
- Connection to other papers: Use with [[Gabaix and Landier 2008]] for CEO talent, [[Bebchuk and Fried 2004]] for rent extraction, [[Edmans and Gabaix 2016]] for theory, and [[Malenko and Shen 2016]] for proxy advisors.
- Best exam phrase: "Edmans, Gosling, and Jenter survey directors and investors and show that CEO compensation is constrained by fairness, controversy, and investor approval, so observed contracts cannot be interpreted as a clean solution to a simple agency model."

## 12. Hypotheses Inspired by This Paper
H1: CEO pay increases following strong performance are larger when the performance is more publicly attributable to the CEO, even controlling for changes in equity wealth.

H2: Firms with higher exposure to proxy advisor influence use more standardized CEO pay structures and offer less upside for exceptional performance.

H3: CEO pay cuts are less demotivating when they are framed as external or shared sacrifices, such as COVID, financial constraints, or workforce-wide cuts, than when they are framed as poor CEO performance.

## 13. Possible Extension or Research Design
- Research question: Do proxy advisor constraints lead to more standardized CEO pay structures, and does this standardization reduce firm value or CEO retention?
- Hypothesis: Firms more dependent on proxy advisor support adopt more conventional pay contracts with lower upside and more performance conditions, even when firm-specific optimal contracts would differ.
- Data: ISS and Glass Lewis recommendations, say-on-pay votes, ExecuComp or UK remuneration reports, CEO turnover, firm performance, and compensation structure variables.
- Identification: Use close say-on-pay votes, changes in proxy advisor policies, or discontinuities in proxy advisor recommendations as shocks to board constraints.
- Expected result: Stronger proxy advisor pressure increases conformity in pay structure and reduces contract tailoring.
- Contribution: Tests whether the "one-size-fits-all" constraint reported in the survey has real effects on pay design and firm outcomes.

## 14. Critiques

### Major Concern 1
The paper identifies beliefs and reported constraints, not causal mechanisms. Directors may say pay cuts reduce motivation because that justifies high pay, while investors may say pay is too high because they face client pressure.

### Major Concern 2
The UK setting is institutionally distinctive. Binding policy votes, UK governance codes, and lower CEO pay levels relative to the US may affect how directors and investors perceive constraints.

### Minor Concern
COVID-19 may have made pay cuts, employee fairness, and controversy unusually salient, even though the authors ask about pay practices in general.

### Referee Recommendation
Accept, because the paper provides rare and useful field evidence on the hidden objective functions and constraints behind CEO compensation. It should not be read as causal evidence, but it is highly valuable for theory discipline, mechanism discovery, and interpreting archival pay regressions.

## 15. Memory Hooks
- "Beyond IR and IC": CEO pay is constrained by controversy, fairness, and investor approval.
- "Flow pay is recognition": bonuses and pay increases matter even when the CEO already owns lots of equity.
- "Directors vs. investors": directors worry about retention and motivation; investors worry about incentives and excessive pay.
- "Fairness reference points": peer CEOs, past pay, internal hierarchy, worker pay, shareholder returns, perceived contribution.
- "Not just rent extraction": the paper offers a third view, boards and investors may both want shareholder value but disagree about how to maximize it.

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Executive Compensation]], [[CEO Incentives]], [[Corporate Governance]], [[Proxy Advisors]], [[Say-on-Pay]], [[Contract Theory]], or [[Survey Evidence in Corporate Finance]]. The clean exam answer is: "Edmans, Gosling, and Jenter use a survey of UK directors and institutional investors to show that CEO pay is shaped by fairness, recognition, reputation, and controversy constraints, not just participation and incentive constraints." Use it to argue that observed compensation contracts should not be interpreted mechanically as optimal agency contracts or pure rent extraction. In a critique answer, emphasize that the evidence is based on perceptions rather than causal variation, but note that the paper is stronger than a standard correlation because it directly reveals the latent beliefs and constraints that archival data cannot observe.
