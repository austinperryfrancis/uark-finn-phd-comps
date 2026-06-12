---
type: paper
status: unread
title: "What Is CEO Overconfidence? Evidence from Executive Assessments"
authors: Steven N. Kaplan, Morten Sorensen, Anastasia A. Zakolyukina
year: 2020
journal: NBER Working Paper No. 27853
seminar:
field: Corporate Finance
literature: Behavioral Corporate Finance; CEO Traits; Managerial Overconfidence; Investment-Cash Flow Sensitivity
methods: Executive assessments; validation exercise; factor analysis; EPS forecast measures; investment-cash flow regressions
datasets: ghSMART executive assessments; DEF 14A; SEC EDGAR; Equilar; CRSP; Compustat; IBES
identification: Correlational validation using ex ante executive assessments and later CEO overconfidence proxies
main_result: Longholder CEOs score lower on several traits associated with overconfidence and lower on general ability; Longholder and lower ability CEOs have higher investment-cash flow sensitivities.
exam_relevance: high
must_memorize: true
tags:
  - behavioral-corporate-finance
  - ceo-overconfidence
  - ceo-traits
  - investment-cash-flow-sensitivity
  - executive-assessments
  - DrJandik
created: 2026-06-12
updated: 2026-06-12
---

# Kaplan, Sorensen, and Zakolyukina 2020

## 1. One-Sentence Takeaway
This paper shows that the widely used [[Longholder]] measure of CEO overconfidence maps to independent executive personality assessments, and the main contribution is to validate Longholder as capturing overconfidence rather than merely option exercise frictions or firm characteristics.

## 2. Exam-Ready Abstract
Kaplan, Sorensen, and Zakolyukina ask what the common option-based measure of CEO overconfidence, Longholder, actually captures. They use proprietary ghSMART assessments of more than 2,600 executive candidates, then track which candidates later become public-company CEOs. Among 67 public CEOs, 9 are classified as Longholders, meaning they hold vested options that are at least 40 percent in the money until the final year before expiration. Longholder CEOs score lower on traits associated with overconfidence, including network, organization, commitments, analytical skills, work ethic, listening skills, and openness to criticism. Longholder is also negatively related to a factor interpreted as general ability, consistent with a CEO version of the [[Dunning-Kruger Effect]]. The paper further shows that optimistic earnings guidance produces similar patterns, and that investment-cash flow sensitivities are larger for Longholder and less able CEOs. This paper connects [[Behavioral Corporate Finance]], [[CEO Traits]], [[Managerial Overconfidence]], and [[Corporate Investment]].

## 3. Research Question
What does the Longholder measure of CEO overconfidence actually measure?

More specifically, does holding deep-in-the-money options until expiration reflect CEO overconfidence, or could it simply reflect other explanations such as risk tolerance, tax deferral, private information, hedging, board restrictions, or firm-specific compensation design?

The mechanism tested is whether CEOs classified as Longholders have independently assessed personality traits that psychology and behavioral finance associate with overconfidence.

## 4. Core Mechanism
Use a chain that can be memorized for comps:

```text
CEO holds deep-in-the-money options until expiration
-> CEO remains exposed to firm-specific risk despite diversification benefits
-> this behavior may reveal overoptimism about the firm
-> overconfident CEO exhibits lower assessed ability, weaker listening, weaker planning, and weaker openness to feedback
-> firm investment becomes more sensitive to internal cash flow
```

## 5. Main Findings
1. Longholder CEOs have lower scores on traits that prior psychology literature associates with overconfidence: weaker networks, weaker organization, lower calm under pressure, slower or less effective action, weaker commitment, lower analytical skills, lower creativity, lower work ethic, worse listening, and less openness to criticism.
2. Longholder is significantly negatively related to Factor 1 from Kaplan and Sorensen's factor structure, which the paper interprets as general talent or ability. This supports the idea that overconfidence and lower ability are linked.
3. Investment-cash flow sensitivities are larger for firms led by Longholder CEOs and by CEOs with lower general ability. The Longholder effect remains when the factors are included, suggesting Longholder captures overconfidence beyond general ability.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | CEO for trait and Longholder tests; CEO-quarter for earnings guidance tests; CEO-firm-year for investment-cash flow tests |
| Sample period | ghSMART assessments primarily 2001 to 2012; firm and investment data cover 2001 to 2016 |
| Main dataset | Proprietary ghSMART executive assessments matched to public-company CEOs |
| Key variables | Longholder, High Forecast, Point Estimate, ghSMART traits, Kaplan-Sorensen factors, investment, cash flow, Q, size, stock ownership, vested options |
| Treatment or shock | No external shock. Main variable is CEO overconfidence as measured by Longholder |
| Outcome variables | Executive trait scores, factor scores, optimistic EPS forecasts, point EPS forecasts, investment-cash flow sensitivity |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between Longholder and firm outcomes is not clearly causal. CEOs may select into firms with particular compensation structures, growth opportunities, governance, risk, or exercise constraints. Firms may also select certain CEO types into option-heavy contracts. Longholder may reflect risk tolerance, tax deferral, hedging opportunities, private information about undervaluation, or board policies rather than overconfidence. There is also measurement error because Longholder is an indirect behavioral proxy and ghSMART does not directly rate overconfidence.

### Identification Approach
- Natural experiment: None.
- Instrument: None.
- Difference in differences: None.
- Event study: Not central in provided text.
- Fixed effects: Investment-cash flow specifications include year fixed effects and year fixed effects interacted with cash flow. The provided text does not indicate firm fixed effects.
- Matching: Not clear from provided text.
- Placebo tests: Not clear from provided text.
- Robustness: They compare Longholder and non-Longholder firms and find few differences in firm characteristics. They show non-Longholders had sufficiently in-the-money options, so they had a chance to become Longholders. They also use alternative overconfidence proxies from earnings guidance.
- Alternative source of variation: EPS guidance optimism, High Forecast, and overprecision, Point Estimate.

### Is the Identification Convincing?
- Strength: The key strength is measurement validation. Personality assessments are conducted ex ante, before the executive becomes a public CEO, and are independent of later option exercise behavior.
- Weakness: The design is not causal. It validates a proxy by showing correlations with traits predicted by theory, but it cannot prove that overconfidence causes corporate policies.
- Referee concern: Small sample. Only 67 public CEOs and 9 Longholders, which limits power, controls, and heterogeneity tests.

## 8. Main Regression or Model

The first empirical idea is a validation regression:

```text
Longholder_i = alpha + beta Trait_i + epsilon_i
```

Here, `Trait_i` is one ghSMART characteristic or one Kaplan-Sorensen factor for CEO `i`. A negative beta means that Longholder CEOs score lower on that assessed characteristic. The key result is that Longholder is negatively related to several traits and especially to Factor 1, general ability.

The second empirical idea uses earnings guidance:

```text
OverconfidenceForecast_iq = alpha + beta Trait_i + epsilon_iq
```

`OverconfidenceForecast_iq` is either High Forecast, an optimistic EPS forecast, or Point Estimate, a measure of forecast precision. High Forecast behaves more like Longholder than Point Estimate does, suggesting that Longholder captures optimism more than overprecision.

The investment-cash flow specification is:

```text
Investment_it =
  beta1 CashFlow_it
+ beta2 CEO_Trait_i
+ beta3 CashFlow_it x CEO_Trait_i
+ Controls_it
+ Controls_it x CashFlow_it
+ Year FE
+ Year FE x CashFlow_it
+ epsilon_it
```

`beta3` is the main coefficient. If CEO_Trait is Longholder, a positive `beta3` means investment is more sensitive to cash flow under overconfident CEOs. If CEO_Trait is Factor 1, a negative interaction means higher general ability reduces investment-cash flow sensitivity, or equivalently, lower-ability CEOs have more cash-flow-sensitive investment.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Behavioral Corporate Finance]] by validating the Longholder proxy used in studies of CEO overconfidence.
2. [[CEO Traits]] by linking independent executive assessments to later CEO behavior and corporate policies.
3. [[Corporate Investment]] by showing that investment-cash flow sensitivity is related not only to financing frictions but also to managerial traits.

It differs from prior work because it does not simply assume Longholder equals overconfidence. It opens the black box by comparing Longholder CEOs to independently assessed personalities.

## 10. Closely Related Papers
- [[Malmendier and Tate 2005]]: Introduces CEO overconfidence and investment-cash flow sensitivity using option exercise behavior.
- [[Malmendier and Tate 2008]]: Shows overconfident CEOs are more likely to make value-destroying acquisitions.
- [[Malmendier and Tate 2015]]: Surveys the behavioral CEO literature and discusses Longholder as the dominant proxy.
- [[Kaplan, Klebanov, and Sorensen 2012]]: Uses executive assessments to study which CEO characteristics matter for performance.
- [[Ben-David, Graham, and Harvey 2013]]: Measures managerial miscalibration using CFO forecasts.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on managerial overconfidence. Discuss how overconfidence is measured and whether these measures are credible.

How to use this paper:
- Main finding: Longholder CEOs look overconfident in independent executive assessments.
- Data: ghSMART personality assessments matched to public CEOs, option holdings from DEF 14A, firm data from CRSP and Compustat, and EPS guidance from IBES.
- Identification: Not causal. It is a validation exercise using ex ante assessments and alternative overconfidence proxies.
- Limitation: Small sample and no direct overconfidence rating.
- Connection to other papers: Use after [[Malmendier and Tate 2005]] to defend the Longholder measure.
- Best exam phrase: "Kaplan, Sorensen, and Zakolyukina validate Longholder by showing that Longholder CEOs have independently assessed traits that psychology associates with overconfidence, including lower general ability and weaker openness to feedback."

## 12. Hypotheses Inspired by This Paper
H1: CEOs classified as Longholders will issue more optimistic management forecasts than non-Longholder CEOs.

H2: Firms led by overconfident CEOs will display higher investment-cash flow sensitivity, especially when external financing is costly.

H3: The effect of CEO overconfidence on corporate investment will be weaker in firms with stronger boards, higher institutional monitoring, or more restrictive investment governance.

## 13. Possible Extension or Research Design
- Research question: Does governance discipline attenuate the effect of CEO overconfidence on investment distortions?
- Hypothesis: Overconfident CEOs increase investment-cash flow sensitivity and potentially overinvestment, but the effect is weaker when board monitoring is stronger.
- Data: ExecuComp option holdings for Longholder, BoardEx or ISS governance data, Compustat investment data, CRSP returns, and management forecast data from IBES or I/B/E/S Guidance.
- Identification: Interact Longholder with plausibly exogenous changes in monitoring intensity, such as institutional ownership shocks, index inclusion, or governance reforms. Use firm and year fixed effects where feasible.
- Expected result: Longholder CEOs have stronger cash-flow-sensitive investment, but the relation is muted when monitoring increases.
- Contribution: Links behavioral corporate finance to governance as a constraint on managerial biases.

## 14. Critiques

### Major Concern 1
The paper is primarily correlational. It shows Longholder is associated with traits related to overconfidence, but it cannot establish that overconfidence causes option holding or corporate investment behavior.

### Major Concern 2
The sample is small. The key Longholder validation uses 67 public-company CEOs and only 9 Longholders, limiting statistical power and making it difficult to include rich controls or study heterogeneity.

### Minor Concern
The ghSMART data are proprietary and based on assessed candidates, not a random sample of executives. External validity may be limited if assessed executives differ from the broader CEO population.

### Referee Recommendation
R&R, because the data are unique and the question is important for a large behavioral corporate finance literature, but the paper should be careful not to oversell causal claims given the small sample and indirect measurement.

## 15. Memory Hooks
- "Longholder gets a personality test."
- "67 CEOs, 9 Longholders."
- "Longholder means lower network, planning, analytics, listening, and openness."
- "Factor 1 negative equals CEO Dunning-Kruger."
- "Investment-cash flow sensitivity survives ability controls."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | Medium |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Behavioral Corporate Finance]], [[Managerial Overconfidence]], [[CEO Traits]], or [[Corporate Investment]]. The clean exam answer is: "Kaplan, Sorensen, and Zakolyukina use proprietary ghSMART executive assessments to validate Longholder and show that Longholder CEOs have traits associated with overconfidence, including lower general ability, weaker listening, and weaker openness to criticism." Use it to argue that Longholder is not just an arbitrary option-exercise proxy, but a behavior linked to independently measured personality traits. In a critique answer, emphasize the small sample and correlational nature of the evidence, but note that the paper is stronger than a standard correlation because the personality assessments are ex ante and independent of later CEO option exercise behavior.