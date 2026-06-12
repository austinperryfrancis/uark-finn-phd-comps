---
type: paper
status: unread
title: Proxy Advisory Firms and Corporate Shareholder Engagement
authors: Aiyesha Dey, Austin Starkweather, Joshua T. White
year: 2024
journal: Review of Financial Studies
professor: DrJandik
seminar: null
jandik_paper_number: 60
jandik_week: 15
jandik_topic: Governance
jandik_done: false
field: Corporate Finance
literature:
- '[[Corporate Governance]]'
- Proxy Advisors
- Shareholder Engagement
- Say-on-Pay
methods:
- Regression discontinuity
- difference-in-differences
- event study
- textual analysis
- OLS
- Poisson
datasets:
- '[[ISS Voting Analytics]]'
- SEC proxy statements
- '[[CRSP]]'
- '[[Compustat]]'
- '[[ISS]]'
- '[[IBES]]'
- Thomson Reuters Institutional Holdings
identification: Quasi-natural experiment around ISS's 70 percent say-on-pay support threshold
main_result: Firms just below ISS's 70 percent say-on-pay threshold sharply increase shareholder engagement, especially where director agency conflicts and ISS sanction threats are stronger.
exam_relevance: high
must_memorize: true
tags:
- corporate-governance
- proxy-advisors
- shareholder-engagement
- say-on-pay
- regression-discontinuity
- board-monitoring
created: 2026-06-12
updated: 2026-06-12
---

# Dey, Starkweather, and White 2024

## 1. One-Sentence Takeaway
This paper shows that ISS can causally increase firms' shareholder engagement using the discontinuity created by ISS's 70 percent say-on-pay support threshold, and the main contribution is to identify a positive governance channel through which proxy advisors shape information flows between firms and investors.

## 2. Exam-Ready Abstract
Dey, Starkweather, and White study whether Institutional Shareholder Services affects how firms engage with shareholders. The setting is U.S. public firms with say-on-pay votes from 2011 to 2019, where ISS applies heightened scrutiny when SOP support falls below 70 percent. The empirical design compares firms narrowly below and above the 70 percent threshold, using OLS, regression discontinuity, difference-in-differences, and event-study evidence. Firms receiving ISS treatment increase both the extensive margin of engagement, measured by whether proxy statements disclose engagement, and the intensive margin, measured by engagement-related discussion in proxy statements. The effect is stronger when directors face greater agency conflicts or are more exposed to ISS sanctions, and less responsive treated firms are more likely to receive ISS against recommendations for directors. The market reaction is positive when treatment coincides with an ISS against recommendation, suggesting investors value engagement when ISS's enforcement threat is credible. This paper belongs in [[Corporate Governance]], [[Shareholder Activism]], [[Proxy Advisors]], [[Say-on-Pay]], and [[Information Intermediaries]].

## 3. Research Question
What is the paper trying to answer?

Does ISS influence firms' real governance behavior by inducing shareholder engagement after low say-on-pay support?

More specifically: the paper tests whether ISS's 70 percent SOP threshold creates a credible threat of future negative voting recommendations, causing managers and directors to engage more with shareholders, disclose that engagement, and potentially improve firm-shareholder information flows.

## 4. Core Mechanism
Use a chain that can be memorized for comps:

```text
SOP support falls just below ISS's 70 percent threshold
-> ISS places the firm under heightened scrutiny
-> directors face risk of future ISS against recommendations
-> firm increases engagement with shareholders and discloses response
-> richer two-way information flow and improved governance responsiveness
```

## 5. Main Findings
1. ISS treatment increases shareholder engagement. In the narrow 67.5 to 72.5 percent window, treated firms are more likely to disclose engagement, have higher engagement counts, are more likely to reference the prior SOP vote, are more likely to provide engagement tables, and contact or speak with more shareholders.
2. The RD estimates imply a 19.7 to 33.4 percentage point increase in the probability of engagement for firms just below the 70 percent threshold.
3. The mechanism is credible threat and director incentives. Less responsive treated firms are more likely to receive ISS against recommendations for compensation committee members and directors.
4. Engagement persists beyond the first post-treatment year, suggesting ISS-induced engagement is not merely a one-year compliance response.
5. Investors appear to value the intervention when the ISS threat is strongest: treated firms with prior ISS against SOP recommendations earn positive abnormal returns of roughly 2 to 3 percent around SOP vote disclosure.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Firm-year around annual SOP votes |
| Sample period | 2011 to 2019 |
| Main dataset | ISS Voting Analytics SOP outcomes matched to SEC proxy statements |
| Key variables | SOP voting support, ISS treatment, ISS against SOP, engagement indicator, engagement count, engagement references SOP, engagement table, shareholders contacted, shareholders spoken with |
| Treatment or shock | SOP support below 70 percent, which triggers ISS review of shareholder engagement response |
| Outcome variables | Engagement disclosures, engagement intensity, breadth and depth of engagement, ISS against recommendations for directors, abnormal returns around SOP vote disclosure |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between ISS pressure and engagement would not be causal because firms with poor governance, controversial CEO pay, weak performance, or dissatisfied investors may both receive low SOP support and increase engagement. Reverse causality is also plausible: firms anticipating shareholder dissent may engage before the vote. Omitted variables such as institutional ownership, board quality, investor activism, compensation complexity, or firm visibility could jointly determine ISS scrutiny and engagement. Measurement error is also relevant because engagement is based on voluntary proxy disclosures, which may not perfectly reflect private conversations.

### Identification Approach
- Natural experiment: ISS policy creates a discontinuity at 70 percent SOP support.
- Instrument: None.
- Difference in differences: Dynamic panel tests compare treated and control firms before and after the low SOP vote.
- Event study: Abnormal returns around SOP vote disclosure test whether investors value anticipated ISS-induced engagement.
- Fixed effects: Industry and year fixed effects in main ATE models, firm and year fixed effects in panel/event-time tests.
- Matching: Not the core design.
- Placebo tests: Threshold placebo tests from 50 to 90 percent show the engagement jump is specific to 70 percent.
- Robustness: RD bandwidths, polynomial choices, density tests around the cutoff, covariate balance tests, staggered DiD robustness.
- Alternative source of variation: Cross-sectional heterogeneity in director vulnerability, compensation committee tenure, classified boards, and whether firms are less responsive.

### Is the Identification Convincing?
- Strength: The 70 percent threshold is institutionally meaningful and externally imposed by ISS. Firms just below and just above 70 percent are plausibly comparable, and the paper tests manipulation using density tests and covariate balance.
- Weakness: Firms may understand the threshold and try to influence voting outcomes, although the paper finds no evidence of precise manipulation. Engagement is measured from voluntary disclosures, not direct observation of meetings.
- Referee concern: The biggest concern is whether the outcome is actual engagement or disclosure tailored to satisfy ISS. A second concern is SUTVA, since control firms just above 70 percent might learn from treated firms or respond preemptively.

## 8. Main Regression or Model

```text
Engagement_i,t+1 =
  alpha
+ theta ISS_Treatment_i,t
+ Controls_i,t
+ Industry FE
+ Year FE
+ epsilon_i,t
```

ISS_Treatment equals one if SOP support is between 67.50 and 69.99 percent, and zero if SOP support is between 70.00 and 72.50 percent. The coefficient theta measures whether falling just below the ISS threshold increases engagement in the next proxy year relative to firms just above the threshold.

RD version:

```text
Engagement_i,t+1 =
  alpha
+ tau 1[SOP_Support_i,t < 70%]
+ f(SOP_Support_i,t - 70%)
+ Controls_i,t
+ epsilon_i,t
```

Here, tau is the local treatment effect at the 70 percent cutoff. It captures the discontinuous jump in engagement caused by ISS treatment.

Dynamic DiD version:

```text
Engagement_i,t+1 =
  alpha
+ sum_k beta_k ISS_Treatment_i x EventYear_k
+ Controls_i,t
+ Firm FE
+ Year FE
+ epsilon_i,t
```

The pre-treatment beta coefficients test parallel trends. The post-treatment beta coefficients show whether engagement rises after treatment and whether the effect persists.

Heterogeneity version:

```text
Engagement_i,t+1 =
  alpha
+ beta1 ISS_Treatment_i,t
+ beta2 Agency_Conflict_i,t
+ beta3 ISS_Treatment_i,t x Agency_Conflict_i,t
+ Controls_i,t
+ Industry FE
+ Year FE
+ epsilon_i,t
```

The key coefficient is beta3. A positive beta3 means ISS treatment has a stronger effect when agency problems are higher, such as long compensation committee tenure or classified boards.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Proxy Advisors]]: Shows ISS affects firms not only through voting recommendations but also by inducing engagement.
2. [[Corporate Governance]]: Provides evidence that private governance intermediaries can discipline boards through reputational and voting-related sanctions.
3. [[Shareholder Engagement]]: Introduces disclosure-based measures of engagement breadth and depth.
4. [[Say-on-Pay]]: Shows SOP votes generate governance consequences even though the votes are nonbinding.

It differs from prior work because prior proxy-advisor papers often focus on voting outcomes, standardized pay policies, or value destruction. This paper identifies a channel where ISS facilitates firm-investor communication and potentially improves governance.

## 10. Closely Related Papers
- [[Malenko and Shen 2016]]: Proxy advisor recommendations affect voting outcomes, useful background for why ISS threats are credible.
- [[Ertimur, Ferri, and Oesch 2013]]: Studies shareholder voting and proxy advisors in the SOP setting.
- [[Larcker, McCall, and Ormazabal 2015]]: Argues proxy advisors may induce one-size-fits-all pay practices and reduce value.
- [[Albuquerque, Carter, and Gallani 2020]]: Proxy advisor quality and governance role.
- [[McCahery, Sautner, and Starks 2016]]: Institutional investor engagement and governance preferences.
- [[Kakhbod et al. 2023]]: Theory of engagement and belief convergence between management and shareholders.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the literature on proxy advisors and shareholder governance. Do proxy advisors improve or distort corporate governance? Discuss data, identification, and mechanisms.

How to use this paper:
- Main finding: ISS induces more shareholder engagement after firms fall below the 70 percent SOP threshold.
- Data: ISS Voting Analytics, SEC proxy statements, CRSP, Compustat, and governance/institutional ownership data.
- Identification: RD and DiD around the 70 percent ISS policy threshold.
- Limitation: Engagement is based on voluntary disclosure, not observed private conversations.
- Connection to other papers: Contrasts with one-size-fits-all proxy advisor critiques and complements papers showing proxy advisors influence voting.
- Best exam phrase: "Dey, Starkweather, and White use ISS's 70 percent say-on-pay threshold as a quasi-experiment and show that proxy advisors can improve governance by inducing two-way shareholder engagement, not merely by shifting votes."

## 12. Hypotheses Inspired by This Paper
H1: Firms that narrowly trigger proxy advisor scrutiny increase both the probability and intensity of shareholder engagement disclosures.

H2: The engagement response is stronger when directors face higher personal or reputational costs from negative proxy advisor recommendations.

H3: ISS-induced engagement improves information flow and investor confidence, leading to positive market reactions when the threat of ISS enforcement is credible.

## 13. Possible Extension or Research Design
- Research question: Does ISS-induced engagement lead to real changes in compensation policy, board composition, or shareholder proposal outcomes?
- Hypothesis: Treated firms not only disclose more engagement but also make more shareholder-aligned compensation and governance changes in the following year.
- Data: ISS Voting Analytics, proxy statements, ExecuComp, BoardEx, shareholder proposal data, director election outcomes, and compensation plan features.
- Identification: Use the same 70 percent RD threshold, but replace engagement outcomes with changes in compensation design, pay-performance sensitivity, CEO pay levels, clawback adoption, board refreshment, or subsequent SOP support.
- Expected result: Treated firms make more observable compensation and governance changes, especially where institutional ownership is high and prior ISS against recommendations exist.
- Contribution: Distinguishes symbolic engagement disclosure from real governance change.

## 14. Critiques

### Major Concern 1
The main outcome is disclosure-based. Firms may write more about engagement to satisfy ISS without materially changing private interactions with shareholders. The paper partly addresses this with breadth measures such as shareholders contacted and spoken with, but those are still proxy disclosures.

### Major Concern 2
The threshold may not be perfectly as-good-as-random if sophisticated firms manage SOP support around 70 percent. The paper addresses this with density tests and covariate balance, but precise vote management remains the most natural identification critique.

### Minor Concern
The setting is specific to ISS, SOP votes, and U.S. public firms from 2011 to 2019. External validity to other proxy advisors, countries, or governance issues is not automatic.

### Referee Recommendation
Accept, because the paper has a clean institutional setting, credible threshold-based identification, novel measurement of shareholder engagement, and a clear contribution to the debate over whether proxy advisors improve or distort governance.

## 15. Memory Hooks
- "70 percent ISS threshold."
- "Proxy advisors do more than recommend votes, they trigger engagement."
- "Low SOP support becomes a governance shock."
- "Economic sanctions for directors make the threat credible."
- "Engagement jumps, persists, and is valued when ISS threat is strongest."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Corporate Governance]], [[Proxy Advisors]], [[Shareholder Engagement]], [[Say-on-Pay]], [[Board Accountability]], or [[Regression Discontinuity]]. The clean exam answer is: "Dey, Starkweather, and White use ISS's 70 percent say-on-pay threshold as a quasi-natural experiment and show that ISS treatment increases firms' shareholder engagement." Use it to argue that proxy advisors can improve governance through an information-intermediary channel, not just through mechanical voting recommendations. In a critique answer, emphasize that engagement is measured from voluntary proxy disclosures, but note that the paper is stronger than a standard correlation because the 70 percent ISS threshold creates sharp, institutionally grounded variation in treatment.