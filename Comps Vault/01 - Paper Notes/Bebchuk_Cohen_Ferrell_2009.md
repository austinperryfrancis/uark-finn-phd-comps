---
type: paper
status: unread
title: What Matters in Corporate Governance?
authors: Lucian Bebchuk, Alma Cohen, Allen Ferrell
year: 2009
journal: Review of Financial Studies
seminar:
field: corporate finance
literature: corporate governance
methods: panel regressions, portfolio return tests, firm fixed effects
datasets: IRRC, Compustat, CRSP, ExecuComp
identification: observational panel with controls, prior valuation controls, and firm fixed effects
main_result: Six entrenching governance provisions explain the negative relation between governance restrictions, firm value, and abnormal returns
exam_relevance: high
must_memorize: true
tags:
  - corporate-finance
  - corporate-governance
  - agency-problems
  - takeovers
  - firm-value
  - DrJandik 
created: 2026-06-03
updated: 2026-06-03
---

# Bebchuk, Cohen, and Ferrell 2009

## 1. One-Sentence Takeaway
This paper shows that a small subset of antitakeover governance provisions predicts lower firm value and lower abnormal returns using IRRC governance data, and the main contribution is the creation of the six-provision Entrenchment Index as a cleaner governance measure than the broader GIM index.

## 2. Exam-Ready Abstract
Bebchuk, Cohen, and Ferrell ask which corporate governance provisions actually matter for firm value. Prior work used the 24-provision Gompers, Ishii, and Metrick index, but this paper argues that not all provisions should be equally informative. The authors create an Entrenchment Index based on six provisions: staggered boards, limits to shareholder bylaw amendments, poison pills, golden parachutes, supermajority merger requirements, and supermajority charter amendment requirements. They use IRRC governance data, Compustat, CRSP, and ExecuComp to study Tobin’s Q and stock returns from the 1990s into 2003. Higher entrenchment is monotonically associated with lower Tobin’s Q and negative abnormal returns, while the other 18 IRRC provisions do not explain valuation or returns in the same way. The paper is important because it turns “governance quality” from a broad kitchen-sink index into a focused measure of managerial entrenchment. This connects to [[Corporate Governance]], [[Agency Problems]], [[Takeover Market]], and [[Firm Valuation]].

## 3. Research Question
Which corporate governance provisions are responsible for the negative association between governance restrictions and firm value?

More specifically: do a small number of provisions that entrench managers drive the relation between the GIM governance index and Tobin’s Q or stock returns?

## 4. Core Mechanism

```text
Adoption or presence of entrenching governance provisions
-> shareholders have less ability to discipline or replace managers
-> takeover threats and shareholder voting power are weakened
-> managers face weaker external governance pressure
-> lower firm value and lower abnormal stock returns
```

## 5. Main Findings
1. The six-provision Entrenchment Index is negatively and monotonically associated with Tobin’s Q. Higher entrenchment corresponds to lower firm valuation.
2. The E-index provisions largely drive the negative relation between the broader GIM index and firm value. The other 18 provisions do not appear to explain lower valuation or lower abnormal returns.
3. A trading strategy long low-entrenchment firms and short high-entrenchment firms earns large abnormal returns during 1990 to 2003, around 7% annually for zero E-index firms versus E-index 5 or 6 firms.

## 6. Data

| Item | Details |
|---|---|
| Unit of observation | Firm-year for valuation tests; firm-month or portfolio-month for return tests |
| Sample period | Governance volumes from 1990, 1993, 1995, 1998, 1999, and 2002; valuation tests mainly 1992 to 2002; return tests 1990 to 2003 |
| Main dataset | IRRC governance provisions |
| Other datasets | Compustat for financials, CRSP for returns, ExecuComp for insider ownership, Fama-French and Carhart factors |
| Key variables | Entrenchment Index, Other Provisions Index, GIM index, Tobin’s Q, abnormal returns |
| Treatment or shock | Not a clean shock. Main explanatory variable is the level of managerial entrenchment |
| Outcome variables | Tobin’s Q, industry-adjusted Tobin’s Q, abnormal stock returns |

## 7. Identification Strategy

### Endogeneity Problem
The main endogeneity concern is reverse causality and selection. Low-value firms may adopt entrenching provisions because managers of poorly performing firms have stronger incentives to protect themselves from removal. Omitted firm characteristics could also drive both governance choices and valuation. For example, firms with weak growth opportunities, mature industries, or entrenched founders may both adopt antitakeover provisions and have lower Tobin’s Q.

### Identification Approach
- Natural experiment: None.
- Instrument: None.
- Difference in differences: Not clear from provided text.
- Event study: Uses abnormal return portfolio tests, but not a clean event-study design around adoption dates.
- Fixed effects: Includes firm fixed effects regressions showing that increases in E-index are associated with decreases in Tobin’s Q.
- Matching: Not clear from provided text.
- Placebo tests: The “Other Provisions Index” functions like a placebo category because the other 18 IRRC provisions do not predict lower valuation or returns.
- Robustness: Controls for the rest of the IRRC provisions, firm characteristics, industry controls, and prior firm valuation.
- Alternative source of variation: Uses 1990 entrenchment to predict later valuation while controlling for 1990 valuation.

### Is the Identification Convincing?
- Strength: Strong descriptive evidence that the E-index is more informative than the broader GIM index. The paper carefully separates the six provisions from the other 18 and shows the latter are mostly noise.
- Weakness: Not fully causal. Governance provisions are endogenous firm choices.
- Referee concern: The E-index may proxy for unobserved firm type, weak investment opportunities, managerial quality, or preexisting firm decline rather than causing lower value.

## 8. Main Regression or Model

```text
Log(Industry-Adjusted Tobin's Q)_it =
  beta E_Index_it
+ gamma O_Index_it
+ Controls_it
+ Industry FE
+ Year FE
+ epsilon_it
```

The main coefficient is beta. It captures whether firms with more entrenching provisions have lower valuation after controlling for the other IRRC provisions and standard firm controls.

A fixed effects version is closer to:

```text
Log(Industry-Adjusted Tobin's Q)_it =
  beta E_Index_it
+ gamma O_Index_it
+ Controls_it
+ Firm FE
+ Year FE
+ epsilon_it
```

Here, beta is identified from within-firm changes in entrenchment over time. This helps address time-invariant omitted firm characteristics, although it does not solve time-varying endogeneity.

For returns:

```text
Abnormal Return_pt =
  alpha_p
+ beta1 Market_t
+ beta2 SMB_t
+ beta3 HML_t
+ beta4 Momentum_t
+ epsilon_pt
```

The key estimate is alpha for long-short portfolios that buy low-entrenchment firms and short high-entrenchment firms.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Corporate Governance]] by identifying which governance provisions matter most.
2. [[Agency Problems]] by linking managerial insulation to lower firm value.
3. [[Takeover Market]] by showing that takeover defenses are central to governance-performance relations.

It differs from prior work because it does not treat all 24 GIM provisions as equally important. Instead, it shows that six provisions drive the governance valuation result, while the remaining 18 provisions add noise.

## 10. Closely Related Papers
- [[Gompers, Ishii, and Metrick 2003]]: Creates the G-index and shows that stronger shareholder rights are associated with higher value and abnormal returns.
- [[Bebchuk and Cohen 2005]]: Focuses specifically on staggered boards and firm value.
- [[Cremers and Nair 2005]]: Studies governance mechanisms and equity prices using internal and external governance.
- [[Bertrand and Mullainathan 2003]]: Shows antitakeover laws allow managers to enjoy the quiet life.
- [[Masulis, Wang, and Xie 2007]]: Uses governance measures to study acquisition decisions and agency costs.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on corporate governance and firm value. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: A small set of entrenching provisions explains the negative governance-value relation.
- Data: IRRC governance data linked to Compustat, CRSP, ExecuComp, and factor returns.
- Identification: Mostly panel correlations with controls, prior Q controls, and firm fixed effects.
- Limitation: Governance is endogenous, so the results are not definitive causal evidence.
- Connection to other papers: Use after [[Gompers, Ishii, and Metrick 2003]] as the refinement paper.
- Best exam phrase: “Bebchuk, Cohen, and Ferrell unpack the G-index and show that governance-performance results are concentrated in six entrenchment provisions, not the full kitchen-sink index.”

## 12. Hypotheses Inspired by This Paper
H1: Firms with higher managerial entrenchment have lower Tobin’s Q because managers face weaker discipline from shareholders and the takeover market.

H2: The negative relation between governance restrictions and firm value should be stronger in industries where takeover threats are more credible.

H3: Entrenchment should matter less for firms with strong alternative monitoring, such as large institutional ownership, activist presence, or concentrated blockholders.

## 13. Possible Extension or Research Design
- Research question: Does reducing entrenchment causally improve firm value?
- Hypothesis: Firms forced to remove antitakeover provisions experience increases in valuation and operating efficiency.
- Data: Governance provision changes from proxy filings, institutional ownership, activist campaigns, Compustat, CRSP, and takeover activity.
- Identification: Difference-in-differences around plausibly exogenous governance reforms, shareholder proposal victories, or legal changes affecting specific provisions.
- Expected result: Firms that remove staggered boards, poison pills, or supermajority requirements should experience higher valuation and stronger takeover sensitivity.
- Contribution: Moves the E-index literature from predictive governance measurement toward causal evidence on governance reform.

## 14. Critiques

### Major Concern 1
The paper does not fully solve endogeneity. Low-value firms may choose entrenching provisions because weak managers want protection, or because firms with poor growth opportunities are less attractive takeover targets.

### Major Concern 2
The return predictability evidence is hard to interpret. Abnormal returns could reflect risk, omitted characteristics, market mispricing, or a time-specific governance premium rather than a stable governance effect.

### Minor Concern
The E-index weights all six provisions equally. Some provisions, such as staggered boards and poison pills, may be more economically meaningful than others.

### Referee Recommendation
Accept, because the paper makes a major measurement contribution and provides strong evidence that governance indices should focus on the provisions that matter. The causal interpretation should be stated carefully.

## 15. Memory Hooks
- “Six provisions, not twenty-four.”
- E-index equals managerial entrenchment.
- G-index includes noise.
- Staggered boards and poison pills are the takeover-defense core.
- Use this paper when asked whether governance indices are valid measures.

## 16. Comps Use Rating

| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | Medium |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Corporate Governance]], [[Agency Problems]], [[Takeover Market]], or [[Firm Valuation]]. The clean exam answer is: “Bebchuk, Cohen, and Ferrell use IRRC governance provisions to create a six-provision Entrenchment Index and show that these provisions, rather than the full GIM index, drive the negative relation between governance restrictions, Tobin’s Q, and abnormal returns.” Use it to argue that governance measurement matters and that broad governance indices can dilute the economically important provisions. In a critique answer, emphasize that the paper is not a clean causal design, but note that it is stronger than a simple correlation because it controls for other governance provisions, examines later valuation conditional on 1990 valuation, and uses firm fixed effects.


