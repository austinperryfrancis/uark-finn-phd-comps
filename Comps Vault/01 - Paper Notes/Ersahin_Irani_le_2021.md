---
type: paper
status: unread
title: Creditor Control Rights and Resource Allocation Within Firms
authors: Nuri Ersahin, Rustom M. Irani, Hanh Le
year: 2021
journal: Journal of Financial Economics
seminar:
field: Corporate Finance
literature: Creditor governance, debt covenants, internal capital markets, restructuring
methods: Difference-in-differences, establishment-level regressions, regression discontinuity robustness, matching, placebo tests
datasets: US Census LBD, Census of Manufactures, Annual Survey of Manufactures, Compustat, Nini et al. covenant violations, Dealscan
identification: New covenant violations as shifts in creditor control rights, with flexible controls, firm FE, industry-state-year FE, RDD around covenant thresholds, and matching robustness
main_result: Covenant violations lead firms to cut employment, investment, and establishments mainly in peripheral, unproductive, risky, and agency-prone units, especially when lenders have industry experience.
exam_relevance: high
must_memorize: true
tags:
  - creditor-governance
  - debt-covenants
  - internal-capital-markets
  - restructuring
  - corporate-governance
  - DrJandik
created: 2026-06-04
updated: 2026-06-04
---

# Ersahin, Irani, and Le 2021

## 1. One-Sentence Takeaway
This paper shows that creditor control rights improve within-firm resource allocation using establishment-level Census data around debt covenant violations, and the main contribution is opening the black box of how creditor governance changes firm operations.

## 2. Exam-Ready Abstract
Ersahin, Irani, and Le ask whether creditors merely force distressed firms to cut resources or whether creditor control helps firms reallocate resources more efficiently. The setting is US public firms from 1996 to 2009 that violate debt covenants, which shifts control rights toward creditors through technical default. The authors merge covenant-violation data with confidential US Census establishment-level data, allowing them to observe which plants or establishments lose employment, investment, or close. They find that covenant violations are followed by resource cuts concentrated in peripheral business lines, unproductive establishments, risky and unproductive establishments, CEO-favored units, and firms with greater manager-shareholder agency problems. The effects are strongest when lenders have industry experience, consistent with creditors using expertise rather than simply imposing blunt liquidation pressure. The paper contributes to [[Creditor Governance]], [[Debt Covenants]], [[Internal Capital Markets]], and [[Corporate Restructuring]].

## 3. Research Question
What happens inside firms when debt covenant violations transfer control rights to creditors?

More specifically: do creditors improve operating efficiency by forcing managers to reallocate resources away from inefficient, peripheral, risky, or privately beneficial establishments?

## 4. Core Mechanism
Use a chain that can be memorized for comps:

```text
Debt covenant violation
-> creditors gain bargaining power and monitoring rights
-> creditors pressure management to restructure
-> resources are withdrawn from peripheral, unproductive, risky, or agency-prone establishments
-> firm becomes more focused and efficient
-> creditor governance can benefit both creditors and shareholders
```

## 5. Main Findings
1. Covenant violations reduce firm-level employment and increase establishment closures, confirming that technical default affects real operating decisions.
2. Within firms, cuts are concentrated in peripheral business lines and unproductive establishments, suggesting a refocusing and efficiency channel.
3. Risky establishments are cut mainly when they are also unproductive, which suggests creditors are not only reducing risk but also improving productive efficiency.
4. Effects are stronger where manager-shareholder agency problems are more severe, including concentrated industries, unrated firms, CEO projects, and establishments close to the CEO's hometown.
5. Lender industry experience matters: the strongest restructuring effects occur when relationship lenders have prior lending experience in the borrower's industry.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Firm-year and establishment-year |
| Sample period | 1996 to 2009 |
| Main dataset | US Census Longitudinal Business Database for establishments, Census of Manufactures and Annual Survey of Manufactures for manufacturing productivity and investment, Compustat for firm financials |
| Key variables | Covenant violation, employment growth, payroll, establishment closure, investment rate, core versus peripheral establishment, productivity, operating risk, lender industry experience |
| Treatment or shock | New debt covenant violation, defined as a reported covenant violation in the current year but not the previous year |
| Outcome variables | Employment cuts, investment cuts, establishment closures, within-firm reallocation across establishment types |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between covenant violations and resource cuts would not be causal because firms violate covenants when their financial condition deteriorates. Poor performance could directly cause layoffs, plant closures, reduced investment, and divestitures even without creditor intervention. There is also selection into covenant strictness, since riskier borrowers may receive tighter covenants, and lender specialization may be correlated with borrower industry, distress, or loan structure. The key concern is that covenant violations proxy for worsening fundamentals rather than creditor control rights.

### Identification Approach
- Natural experiment: New covenant violations create a discrete shift in creditor bargaining power through technical default.
- Instrument: No formal instrument.
- Difference in differences: Compares changes in resource allocation after violations for violators versus nonviolators, with flexible controls.
- Event study: The paper checks for pretrends and placebo effects before violations.
- Fixed effects: Firm fixed effects in establishment-level tests; industry, state, and year interactions at the establishment level.
- Matching: Difference-in-differences matching estimator pairs violators with similar nonviolators based on financial condition.
- Placebo tests: Finds no comparable resource allocation effects before covenant violations, supporting the interpretation that changes occur after control rights shift.
- Robustness: Uses Dealscan covenant thresholds and regression discontinuity-style tests around current ratio and net worth covenant thresholds.
- Alternative source of variation: Lender industry experience from Dealscan lead arranger data.

### Is the Identification Convincing?
- Strength: Very strong microdata design because the paper observes establishment-level reallocation within the same firm, not just aggregate firm cuts.
- Weakness: Covenant violations are still not randomly assigned, and the main treatment occurs during financial distress.
- Referee concern: Even with flexible controls and RDD robustness, some unobserved deterioration could coincide with violations and explain part of the restructuring.

## 8. Main Regression or Model

```text
Outcome_it = beta CovenantViolation_it
           + Controls_it
           + Industry FE
           + Year FE
           + epsilon_it
```

The firm-level regression estimates whether firms reduce employment or close establishments after a new covenant violation, controlling for financial condition and industry and time shocks.

The key establishment-level model is:

```text
Outcome_ijt = beta1 CovenantViolation_it x Core_jt
            + beta2 CovenantViolation_it x Peripheral_jt
            + Controls_ijt
            + Firm FE
            + Industry x State x Year FE
            + epsilon_ijt
```

Here, the outcome is establishment-level employment growth, investment, or closure. The key comparison is whether beta2 is larger in magnitude than beta1. A larger negative beta2 means that after covenant violations, firms cut peripheral establishments more than core establishments.

For productivity, risk, and agency heterogeneity, the model becomes:

```text
Outcome_ijt =
  beta1 CovenantViolation_it x Core_jt x Productive_jt
+ beta2 CovenantViolation_it x Core_jt x Unproductive_jt
+ beta3 CovenantViolation_it x Peripheral_jt x Productive_jt
+ beta4 CovenantViolation_it x Peripheral_jt x Unproductive_jt
+ Controls_ijt
+ Firm FE
+ Industry x State x Year FE
+ epsilon_ijt
```

The main economic interpretation is in the coefficients on unproductive and peripheral-unproductive establishments. The paper finds that resource cuts are especially concentrated in unproductive units, particularly when those units are peripheral.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Debt Covenants]] by showing that covenant violations affect real operations, not just financial policy.
2. [[Creditor Governance]] by showing that creditors can improve efficiency and mitigate managerial agency costs.
3. [[Internal Capital Markets]] by showing how external creditors reshape resource allocation across establishments within firms.

It differs from prior work because prior covenant-violation papers mostly study firm-level outcomes. This paper uses establishment-level Census data to show which units are cut and why those cuts can be efficiency-improving.

## 10. Closely Related Papers
- [[Chava and Roberts 2008]]: Shows that covenant violations reduce investment.
- [[Roberts and Sufi 2009]]: Shows covenant violations affect financing and debt policy.
- [[Nini, Smith, and Sufi 2009]]: Shows creditor control affects investment policy.
- [[Nini, Smith, and Sufi 2012]]: Shows covenant violations can improve operating performance and equity value.
- [[Bharath and Hertzel 2019]]: Connects bank debt and external governance.
- [[Giroud and Mueller 2010]]: Product market competition and managerial slack.
- [[Bertrand and Mullainathan 2003]]: Quiet life agency problems and reluctance to restructure.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on creditor governance and debt covenants. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Creditors can discipline managers and improve within-firm resource allocation after covenant violations.
- Data: Establishment-level Census data merged to Compustat, covenant violations, and Dealscan.
- Identification: New covenant violations as shifts in control rights, with fixed effects, flexible controls, matching, placebo tests, and RDD robustness.
- Limitation: Covenant violations occur during distress, so isolating creditor control from deteriorating fundamentals is difficult.
- Connection to other papers: Builds directly on [[Chava and Roberts 2008]], [[Roberts and Sufi 2009]], and [[Nini, Smith, and Sufi 2012]] by showing the micro mechanism inside the firm.
- Best exam phrase: "Ersahin, Irani, and Le open the black box of covenant violations by showing that creditor control reallocates resources away from peripheral and unproductive establishments."

## 12. Hypotheses Inspired by This Paper
H1: Firms with more covenant-heavy debt contracts will respond to distress by cutting peripheral establishments more aggressively than firms with covenant-light debt.

H2: Creditor control improves operating performance most when lenders have industry-specific information or prior restructuring experience.

H3: Covenant violations reduce managerial private benefits by reversing CEO-favored investment projects, especially in firms with weak external governance.

## 13. Possible Extension or Research Design
- Research question: Has the rise of covenant-light lending weakened the governance role of creditors in corporate restructuring?
- Hypothesis: Covenant-light borrowers will show weaker post-distress resource reallocation than borrowers with maintenance covenants.
- Data: Dealscan loan contract data, Compustat, establishment-level data if available, syndicated loan covenant-light indicators, bankruptcy or restructuring outcomes.
- Identification: Compare distressed firms with covenant-light versus covenant-heavy loans, controlling for borrower risk and loan characteristics; use lender-level exposure to covenant-light lending as a source of variation.
- Expected result: Covenant-light loans weaken creditors' ability to force operational restructuring before bankruptcy.
- Contribution: Extends the creditor governance literature into modern loan markets where creditor control rights may be weaker.

## 14. Critiques

### Major Concern 1
Covenant violations are endogenous to worsening firm fundamentals. The authors address this with flexible controls, matching, placebo tests, and RDD robustness, but the treatment still occurs exactly when firms are deteriorating.

### Major Concern 2
The efficiency interpretation depends on measuring productivity, core status, and risk well. Establishment-level productivity is rich but partly limited to manufacturing firms, so some results may not generalize fully outside manufacturing.

### Minor Concern
Lender industry experience may proxy for other lender or borrower characteristics, such as loan size, relationship strength, or borrower sophistication.

### Referee Recommendation
Accept, because the paper makes a clear contribution by using rare establishment-level data to identify the operating mechanism behind creditor governance. The identification is not perfect, but the combination of within-firm comparisons, establishment heterogeneity, placebo tests, matching, RDD robustness, and lender-experience heterogeneity makes the evidence compelling.

## 15. Memory Hooks
- "Creditors open the black box."
- Covenant violation = control-right shift.
- Cut the bad plants: peripheral, unproductive, risky.
- Industry-expert lenders matter.
- Creditor governance can help shareholders by reducing managerial slack.

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Creditor Governance]], [[Debt Covenants]], [[Internal Capital Markets]], or [[Corporate Restructuring]]. The clean exam answer is: "Ersahin, Irani, and Le use covenant violations as shifts in creditor control rights and show that creditors induce firms to cut peripheral, unproductive, risky, and agency-prone establishments." Use it to argue that debt covenants are not only contractual tripwires but also governance mechanisms that shape real resource allocation. In a critique answer, emphasize that covenant violations are endogenous to distress, but note that the paper is stronger than a standard correlation because it uses establishment-level within-firm comparisons, flexible controls, matching, placebo tests, and RDD-style robustness around covenant thresholds.