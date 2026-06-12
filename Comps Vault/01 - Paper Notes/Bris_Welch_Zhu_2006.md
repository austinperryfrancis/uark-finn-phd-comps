---
type: paper
status: unread
title: 'The Costs of Bankruptcy: Chapter 7 Liquidation versus Chapter 11 Reorganization'
authors: Arturo Bris, Ivo Welch, Ning Zhu
year: 2006
journal: Journal of Finance
professor: DrJandik
seminar: null
jandik_paper_number: 9
jandik_week: 3
jandik_topic: 'Capital structure: bankruptcy, product markets, debt ownership, and debt maturity'
jandik_done: true
field: Corporate Finance
literature:
- Bankruptcy Costs
- Financial Distress
- Creditor Recovery
- '[[Capital Structure]]'
methods:
- Hand-collected court records
- OLS
- probit
- treatment effects
- Heckman selection correction
- judge fixed effects
datasets:
- PACER bankruptcy court filings from Arizona and Southern District of New York
identification: Observational comparison of Chapter 7 and Chapter 11 with controls for endogenous chapter choice
main_result: Chapter 7 is not meaningfully faster or cheaper than Chapter 11, while Chapter 11 preserves more estate value and produces higher creditor recoveries.
exam_relevance: high
must_memorize: true
tags:
- bankruptcy
- financial-distress
- chapter-11
- chapter-7
- creditor-recovery
- capital-structure
created: 2026-06-03
updated: 2026-06-03
---

# Bris, Welch, and Zhu 2006

## 1. One-Sentence Takeaway
This paper shows that Chapter 7 liquidation is not the cheap and fast alternative to Chapter 11 reorganization using hand-collected PACER bankruptcy cases from Arizona and New York, and the main contribution is showing that bankruptcy costs are heterogeneous, measurement-sensitive, and shaped by endogenous procedure choice.

## 2. Exam-Ready Abstract
Bris, Welch, and Zhu study whether Chapter 7 liquidation and Chapter 11 reorganization differ in direct costs, indirect costs, creditor recovery, and absolute priority violations. They use a hand-collected sample of corporate bankruptcies filed in Arizona and the Southern District of New York from 1995 to 2001, including both private and public firms. The key comparison is between firms that enter Chapter 7 and firms that enter Chapter 11, with attention to the fact that firms self-select into procedures based on size, creditor structure, bank presence, and financial condition. They find that Chapter 7 cases are not meaningfully fast or cheap, often take roughly two years, and frequently leave little for unsecured creditors. Chapter 11 appears to preserve asset value better and produces higher creditor recoveries, especially for unsecured creditors. The paper also shows that courts approve almost all requested professional fees and that bankruptcy costs depend heavily on how costs are measured. This paper connects to [[Bankruptcy Costs]], [[Financial Distress]], [[Capital Structure]], and [[Creditor Rights]].

## 3. Research Question
What are the direct and indirect costs of bankruptcy, and how do Chapter 7 liquidations compare with Chapter 11 reorganizations?

More specifically: does liquidation save time and legal expenses relative to reorganization, or does Chapter 11 preserve more estate value and generate higher creditor recovery despite being a more complex procedure?

## 4. Core Mechanism
Use a chain that can be memorized for comps:

```text
Firm enters bankruptcy
-> choice between Chapter 7 liquidation and Chapter 11 reorganization
-> procedure affects asset retention, delay, professional fees, and bargaining among claimants
-> creditors recover from the remaining estate after fees and priority rules
-> Chapter 11 preserves more value, while Chapter 7 often leaves little for unsecured creditors
```

## 5. Main Findings
1. Chapter 7 is not the simple cheap liquidation benchmark. Chapter 7 cases still take a long time to resolve, with median duration around 672 days, compared with about 866 days for Chapter 11, so liquidation is not a quick cash auction in practice.
2. Chapter 11 preserves estate value better. Median post-bankruptcy, pre-fee assets are about 86.9% of pre-bankruptcy assets in Chapter 11, compared with only 0.8% under reported Chapter 7 recovery and 38.0% even under the authors' optimistic Chapter 7 secured-creditor recovery assumption.
3. Creditor recovery is much better in Chapter 11. Unsecured creditors receive nothing in 95% of Chapter 7 cases, while unsecured creditors in Chapter 11 recover a mean of 52% and median of 40%.
4. Direct costs are highly measurement-sensitive. Professional fees are proportionally much larger for small firms, and after correcting for selection, Chapter 11 is not intrinsically more expensive.
5. Courts mostly approve fee requests. The mean reimbursement approval rate is about 98.7% for debtor requests and 97.5% for unsecured creditor committee requests, suggesting limited court discipline over professional fees.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Unique corporate bankruptcy case |
| Sample period | 1995 to 2001 filings, tracked through September 2004 |
| Main dataset | Hand-coded PACER bankruptcy records from Arizona and Southern District of New York federal bankruptcy courts |
| Key variables | Chapter choice, assets at filing, assets at exit, debt/assets, secured debt share, number of creditors, bank presence, management ownership, court-approved expenses, judge identity |
| Treatment or shock | Bankruptcy procedure, Chapter 7 liquidation versus Chapter 11 reorganization |
| Outcome variables | Asset retention, days in bankruptcy, professional fees, creditor recovery rates, APR violations |

## 7. Identification Strategy

### Endogeneity Problem
A simple comparison of Chapter 7 and Chapter 11 is not causal because firms choose bankruptcy procedures endogenously. Larger firms, firms with more secured creditors, firms with different creditor coordination problems, and firms with different bank relationships may select into Chapter 11 rather than Chapter 7. This means raw differences in costs or recovery could reflect firm quality, asset tangibility, creditor structure, bargaining power, or viability rather than the legal procedure itself. There is also measurement error because assets are based on bankruptcy filings, and Chapter 7 secured creditor recoveries may occur outside the bankruptcy record.

### Identification Approach
- Natural experiment: None.
- Instrument: No clean external instrument. The paper uses first-stage predicted chapter choice based on observables rather than a strong excluded instrument.
- Difference in differences: None.
- Event study: None.
- Fixed effects: Judge effects and jurisdiction controls in some specifications.
- Matching: Not the main approach.
- Placebo tests: Not central.
- Robustness: Alternative treatment-effect and Heckman specifications, controls for firm size, creditor structure, bank presence, debt/assets, jurisdiction, and judge identity.
- Alternative source of variation: Cross-sectional variation in bankruptcy procedure, creditor structure, and court/judge assignment.

### Is the Identification Convincing?
- Strength: Strong data contribution, rich controls, and explicit recognition of endogenous procedure choice.
- Weakness: Chapter choice is not randomly assigned, and the selection correction relies on observables and functional-form assumptions.
- Referee concern: The key causal claim that Chapter 11 preserves more value could still be biased if firms with more viable assets choose Chapter 11 for unobservable reasons.

## 8. Main Regression or Model

```text
Outcome_i =
  beta Chapter11_i
+ gamma FirmCharacteristics_i
+ delta CreditorStructure_i
+ theta CourtControls_i
+ epsilon_i
```

The outcome is asset retention, duration, professional fees, creditor recovery, or APR violation for bankruptcy case `i`. The coefficient `beta` compares Chapter 11 with Chapter 7 after controlling for observable firm and creditor characteristics.

Selection-corrected version:

```text
Chapter11_i =
  1[pi Z_i + u_i > 0]

Outcome_i =
  beta InstrumentedChapter11_i
+ gamma X_i
+ rho InverseMills_i
+ epsilon_i
```

The first stage predicts whether a firm enters Chapter 11 using variables such as asset size, secured creditor count, bank presence, debt/assets, secured debt share, management ownership, and jurisdiction. The second stage estimates whether Chapter 11 affects outcomes after controlling for endogenous selection. The coefficient `beta` carries the main economic interpretation: whether the Chapter 11 procedure itself is associated with different asset retention, costs, time, or recovery after accounting for selection.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Bankruptcy Costs]] by showing that direct and indirect costs are heterogeneous and sensitive to measurement.
2. [[Financial Distress]] by comparing liquidation and reorganization outcomes in a broad sample of ordinary bankruptcies.
3. [[Creditor Rights]] by documenting creditor recovery and APR violations across bankruptcy procedures.

It differs from prior work because it studies both Chapter 7 and Chapter 11, includes private as well as public firms, uses hand-collected court records, and directly addresses endogenous selection into bankruptcy procedure.

## 10. Closely Related Papers
- [[Warner 1977]]: Early evidence on direct bankruptcy costs using railroad bankruptcies.
- [[Altman 1984]]: Estimates bankruptcy costs and emphasizes costs of financial distress.
- [[Weiss 1990]]: Studies bankruptcy resolution, priority violations, and Chapter 11 outcomes.
- [[Pulvino 1998]]: Shows that fire sales can depress asset values in distressed aircraft sales.
- [[Thorburn 2000]]: Studies Swedish bankruptcy auctions and provides a contrasting view that auction-based bankruptcy can be fast and cheap.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on bankruptcy costs. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Chapter 7 is not necessarily cheaper or faster than Chapter 11, and Chapter 11 appears to preserve more estate value.
- Data: Hand-collected PACER records for Arizona and Southern District of New York corporate bankruptcies from 1995 to 2001.
- Identification: Cross-sectional comparison with rich controls and selection correction for endogenous chapter choice.
- Limitation: Chapter choice is not randomly assigned, and asset values are measured from court filings.
- Connection to other papers: Use with [[Warner 1977]], [[Altman 1984]], [[Weiss 1990]], [[Pulvino 1998]], and [[Thorburn 2000]].
- Best exam phrase: "Bris, Welch, and Zhu show that the costs of bankruptcy depend heavily on measurement, and that Chapter 7 liquidation is not the low-cost benchmark assumed in simple theory."

## 12. Hypotheses Inspired by This Paper
H1: Bankruptcy systems with stronger trustee incentives to resolve cases quickly have shorter liquidation durations and higher unsecured creditor recoveries.

H2: Fixed professional costs make bankruptcy disproportionately expensive for small firms, leading to lower creditor recovery and greater liquidation inefficiency.

H3: Creditor coordination problems increase bankruptcy duration, reduce asset retention, and make deviations from absolute priority more likely.

## 13. Possible Extension or Research Design
- Research question: Does judicial fee oversight causally affect bankruptcy costs and creditor recovery?
- Hypothesis: Stricter judges reduce professional fees without reducing creditor recovery.
- Data: PACER bankruptcy filings across many districts after 2001, linked to judge assignment, fee requests, fee approvals, case duration, and recovery outcomes.
- Identification: Use quasi-random judge assignment within court and filing period. Construct leave-one-out judge stringency measures for fee approval or case speed.
- Expected result: Stricter judges reduce direct costs, especially in small-firm bankruptcies, but the effect on recovery depends on whether professional fees reflect waste or useful restructuring services.
- Contribution: Moves from selection-adjusted cross-sectional comparison toward causal evidence on court governance in bankruptcy.

## 14. Critiques

### Major Concern 1
Procedure choice is endogenous. Firms do not randomly enter Chapter 7 or Chapter 11, so estimated differences may reflect unobserved viability, asset quality, relationship banking, or bargaining conditions.

### Major Concern 2
Asset values are noisy and potentially strategic. Filing values and exit values come from court documents and may be overstated or understated by parties with incentives. Chapter 7 secured creditor recoveries are especially hard to observe because collateral may be seized outside the bankruptcy estate.

### Minor Concern
The sample covers only Arizona and Southern District of New York from 1995 to 2001 and does not include a recession, so external validity may be limited.

### Referee Recommendation
Accept, because the paper provides a rare hand-collected dataset, compares Chapter 7 and Chapter 11 directly, and is careful about selection and measurement. The causal claims should be framed cautiously, but the descriptive and institutional contribution is very strong.

## 15. Memory Hooks
- "Chapter 7 is not quick and cheap."
- "Chapter 11 preserves value."
- "Unsecured creditors get zero in 95% of Chapter 7 cases."
- "Bankruptcy costs are measurement-sensitive."
- "Courts rubberstamp fees."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Bankruptcy Costs]], [[Financial Distress]], [[Creditor Recovery]], or [[Capital Structure]]. The clean exam answer is: "Bris, Welch, and Zhu use hand-collected PACER bankruptcy records from Arizona and Southern New York and show that Chapter 7 liquidation is not meaningfully faster or cheaper than Chapter 11, while Chapter 11 better preserves estate value and produces higher creditor recoveries." Use it to argue that bankruptcy costs are not a single number and that legal institutions shape recovery outcomes. In a critique answer, emphasize endogenous selection into Chapter 7 versus Chapter 11 and noisy asset measurement, but note that the paper is stronger than a standard correlation because it explicitly models procedure selection and uses unusually detailed court-level data.
