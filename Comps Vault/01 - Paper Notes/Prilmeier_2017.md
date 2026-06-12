---
type: paper
status: unread
title: Why Do Loans Contain Covenants? Evidence from Lending Relationships
authors: Robert Prilmeier
year: 2017
journal: Journal of Financial Economics
professor: DrJandik
seminar: null
jandik_paper_number: 14
jandik_week: 4
jandik_topic: 'Debt contracts: covenants, social capital, lender hold-up, and creditor control'
jandik_done: true
field: Corporate Finance
literature:
- Debt Contracting
- Loan Covenants
- Relationship Lending
methods:
- OLS
- Poisson regressions
- instrumental variables
- propensity score matching
- structural probit
datasets:
- '[[DealScan]]'
- '[[Compustat]]'
- DirectEDGAR
- '[[Call Reports]]'
- National Information Center
identification: Relationship lending variation, IV using borrower proximity to syndication-active banks, matching, robustness to loan pricing-covenant simultaneity
main_result: Covenant tightness falls with relationship duration, especially for opaque borrowers, while covenant intensity follows an inverted U in relationship intensity.
exam_relevance: high
must_memorize: true
tags:
- debt-contracting
- loan-covenants
- relationship-lending
- banking
- monitoring
created: 2026-06-04
updated: 2026-06-04
---

# Prilmeier 2017

## 1. One-Sentence Takeaway
This paper shows that lending relationships shape non-price loan terms using DealScan corporate loan contracts, and the main contribution is showing that covenant tightness and covenant intensity serve different contracting roles.

## 2. Exam-Ready Abstract
Prilmeier studies why corporate loans contain covenants by asking how covenant design changes as banks learn about borrowers through repeated lending relationships. The setting is U.S. syndicated and large sole-lender loans from DealScan, merged with Compustat borrower data, from 1995 to 2008. The paper separates covenant design into tightness, measured as the ex ante probability of covenant violation, and intensity, measured as the number of financial covenants. Covenant tightness declines over the duration of the bank-borrower relationship, especially for small and unrated borrowers, which supports information-asymmetry models such as Gârleanu and Zwiebel. Covenant intensity, however, is highest at medium relationship intensity and lower when the lender is either not the main relationship lender or is the exclusive lender. The identification strategy uses controls, fixed effects, IVs based on geographic proximity to syndication-active banks, propensity score matching, and robustness to covenant-price simultaneity. This paper connects to [[Debt Contracting]], [[Loan Covenants]], [[Relationship Lending]], and [[Financial Intermediation]].

## 3. Research Question
What role do lending relationships play in shaping the use of financial covenants in corporate loan contracts?

More specifically: does lender learning reduce the need for strict covenants, and are covenants used to incentivize monitoring when borrowers have multiple bank relationships?

## 4. Core Mechanism
Use a chain that can be memorized for comps:

```text
Repeated lending relationship
-> bank learns private information about borrower
-> information asymmetry between bank and borrower falls
-> lender needs less covenant protection
-> covenant tightness declines over relationship duration
```

Second mechanism:

```text
Borrower uses multiple bank lenders
-> each lender may free-ride on others' monitoring
-> main relationship lender has lower monitoring cost and stronger information advantage
-> borrower gives more covenants to main relationship lender
-> covenant intensity is highest at medium relationship intensity
```

## 5. Main Findings
1. Covenant tightness decreases monotonically over the duration of a lending relationship, especially for opaque borrowers such as small and unrated firms.
2. Covenant intensity follows an inverted U shape in relationship intensity: medium-intensity relationship lenders receive the most covenants, while low-intensity and exclusive lenders receive fewer.
3. The inverted U pattern is more consistent with monitoring-incentive explanations than pure information asymmetry or hold-up explanations, because it is stronger in sole-lender loans and loans with only one lead arranger.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Loan deal |
| Sample period | 1995 to 2008 |
| Main dataset | DealScan corporate loan data merged with Compustat |
| Key variables | Covenant tightness, covenant intensity, relationship intensity, relationship duration, borrower opacity, loan terms |
| Treatment or shock | No single shock. Variation comes from bank-borrower relationship status and geography-based instruments for relationship formation. |
| Outcome variables | Covenant tightness, number of financial covenants, yield spreads, collateral, maturity, nonfinancial covenants |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between relationship lending and covenant design is not causal because firms choose their lenders and relationship structures. Safer borrowers may obtain looser covenants and also maintain longer lending relationships. Opaque borrowers may select into relationship lending and also face different covenant packages. Banks may also choose to preserve relationships with firms that have unobserved positive private information, creating selection bias. Covenant tightness, covenant intensity, interest rates, maturity, collateral, and syndicate structure may also be jointly determined in equilibrium.

### Identification Approach
- Natural experiment: Not a clean natural experiment.
- Instrument: Borrower distance to the nearest syndication-active bank, number of syndication-active banks within 100 miles, and distance to the nearest highly syndication-active bank.
- Difference in differences: Not the core design.
- Event study: Not the core design.
- Fixed effects: Industry, year, loan purpose, and loan type fixed effects.
- Matching: Propensity score matching comparing loans with different relationship intensities.
- Placebo tests: Tests loan terms that should not create monitoring incentives and finds no analogous inverted U.
- Robustness: Structural approach for price-covenant trade-off, alternative covenant-count definitions, clustering, one-loan-per-firm resampling, excluding or including jointly determined loan terms.
- Alternative source of variation: Borrower-lender geographic proximity as a predictor of relationship formation.

### Is the Identification Convincing?
- Strength: The paper recognizes relationship choice is endogenous and attacks it several ways: IV, matching, contract-term placebo tests, and simultaneity correction.
- Weakness: The IV relies on geography. Borrower location may correlate with unobserved firm characteristics, local banking markets, or industry clustering that also affect covenant design.
- Referee concern: The geography instrument may affect loan contracting through local credit-market competition rather than only through relationship status.

## 8. Main Regression or Model

```text
CovenantTightness_i =
  beta RelationshipDuration_i
+ gamma RelationshipIntensity_i
+ Controls_i
+ Industry FE
+ Year FE
+ Loan Purpose FE
+ Loan Type FE
+ epsilon_i
```

This regression tests whether longer bank-borrower relationships are associated with looser covenants. The key coefficient is beta. A negative beta means covenant tightness falls as the lender learns about the borrower.

For covenant intensity, the core specification is a count model:

```text
log(FinancialCovenants_i) =
  beta1 LowRelationship_i
+ beta2 HighRelationship_i
+ Controls_i
+ Industry FE
+ Year FE
+ Loan Purpose FE
+ Loan Type FE
+ epsilon_i
```

Medium relationship intensity is the omitted category. Negative beta1 and beta2 imply an inverted U: covenant count is highest for medium relationship lenders.

A heterogeneity version:

```text
log(FinancialCovenants_i) =
  beta1 LowRelationship_i
+ beta2 HighRelationship_i
+ beta3 LowRelationship_i x SoleLender_i
+ beta4 HighRelationship_i x SoleLender_i
+ Controls_i
+ Fixed Effects
+ epsilon_i
```

The monitoring-incentive interpretation is strongest if covenant intensity rises more for main relationship lenders when the lender captures more of the benefits of monitoring, such as in sole-lender loans or loans with one lead arranger.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Loan Covenants]] by separating covenant tightness from covenant intensity.
2. [[Relationship Lending]] by showing that bank relationships affect non-price loan terms, not just spreads, collateral, or credit availability.
3. [[Financial Intermediation]] by connecting covenants to delegated monitoring and lender information production.

It differs from prior work because it shows that the number of covenants and the tightness of covenants do not behave the same way. Tightness is about information asymmetry and learning. Intensity appears more related to monitoring incentives and free-rider problems among lenders.

## 10. Closely Related Papers
- [[Diamond 1984]]: Banks as delegated monitors.
- [[Rajan 1992]]: Relationship lending, informed lenders, and hold-up.
- [[Rajan and Winton 1995]]: Covenants as incentives for lender monitoring.
- [[Chava and Roberts 2008]]: Covenant violations and creditor control rights.
- [[Nini Smith and Sufi 2012]]: Creditor control rights and governance after covenant violations.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on debt covenants and relationship lending. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Relationship lending changes covenant structure. Tightness falls with relationship duration, while covenant count is highest for main but nonexclusive relationship lenders.
- Data: DealScan loans to U.S. public firms, merged with Compustat.
- Identification: Controls, fixed effects, IV using proximity to syndication-active banks, matching, and robustness to covenant-price simultaneity.
- Limitation: Relationship formation is endogenous, and the geography instrument may not be perfectly excludable.
- Connection to other papers: Connect to Diamond on delegated monitoring, Rajan on relationship lending and hold-up, Rajan and Winton on covenants as monitoring incentives, and Chava and Roberts or Nini Smith and Sufi on covenant violations as creditor control events.
- Best exam phrase: "Prilmeier separates covenant tightness from covenant intensity and shows they map to different economic mechanisms: lender learning relaxes tightness, while monitoring incentives shape the number of covenants."

## 12. Hypotheses Inspired by This Paper
H1: Covenant tightness declines with the length of a lending relationship, especially for borrowers with high information opacity.

H2: Covenant intensity is highest when the lender is the main relationship lender but the borrower still uses multiple lenders.

H3: The relationship between covenant intensity and relationship lending is stronger when monitoring benefits are concentrated in one lender, such as in sole-lender loans or loans with one lead arranger.

## 13. Possible Extension or Research Design
- Research question: Do covenant-light loans weaken the monitoring role of relationship banks after the rise of private credit?
- Hypothesis: Relationship lenders reduce covenant tightness as they learn about borrowers, but private credit lenders maintain higher covenant intensity when monitoring is centralized.
- Data: DealScan, private credit loan databases, SEC credit agreement exhibits, Compustat, covenant violation data.
- Identification: Compare covenant design before and after shocks to bank lending capacity or private credit entry, using borrower fixed effects and lender-market exposure.
- Expected result: Private credit lenders may use fewer but more customized covenants, while banks rely more on relationship history to relax tightness.
- Contribution: Extends Prilmeier from bank relationship lending to the modern private credit and cov-lite environment.

## 14. Critiques

### Major Concern 1
Relationship status is endogenous. Borrowers do not randomly form relationships, maintain multiple lenders, or borrow exclusively from one bank. The paper uses IV and matching, but selection remains a central concern.

### Major Concern 2
The exclusion restriction for the geography-based IV is debatable. Proximity to syndication-active banks may proxy for local banking competition, regional economic conditions, firm quality, or industry clustering.

### Minor Concern
The measure of covenant tightness requires estimating ex ante violation probabilities using accounting ratios, slack, and historical volatility. Measurement error is likely because covenant definitions vary across contracts.

### Referee Recommendation
R&R, because the paper makes a strong conceptual contribution by separating covenant tightness and covenant intensity, but the causal interpretation depends heavily on relationship-status instruments and robustness tests.

## 15. Memory Hooks
- "Tightness equals learning."
- "Intensity equals monitoring incentives."
- "Medium relationship lenders get the most covenants."
- "Exclusive relationship lowers covenant count because free-riding is reduced."
- "Prilmeier is the paper where covenant tightness and covenant count mean different things."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Loan Covenants]], [[Debt Contracting]], [[Relationship Lending]], [[Bank Monitoring]], or [[Financial Intermediation]]. The clean exam answer is: "Prilmeier 2017 uses DealScan loan contracts and relationship-lending measures to show that covenant tightness falls as lenders learn about borrowers, while covenant intensity is highest for main nonexclusive relationship lenders." Use it to argue that covenants are not a single-dimensional contract term. Some covenant features transfer control rights in response to information asymmetry, while others create incentives for banks to monitor. In a critique answer, emphasize endogenous relationship formation and the exclusion restriction of the proximity instruments, but note that the paper is stronger than a standard correlation because it uses IV, matching, placebo contract terms, and robustness to the price-covenant trade-off.