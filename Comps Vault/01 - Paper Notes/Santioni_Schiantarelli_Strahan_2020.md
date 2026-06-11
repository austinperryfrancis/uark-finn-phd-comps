---
type: paper
status: unread
title: "Internal Capital Markets in Times of Crisis: The Benefit of Group Affiliation"
authors: Raffaele Santioni, Fabio Schiantarelli, Philip E. Strahan
year: 2020
journal: Review of Finance
seminar:
field: Corporate Finance
literature: Internal Capital Markets; Business Groups; Financial Constraints; Bank Lending Channel; Crisis Finance
methods: Discrete-time hazard model; linear probability model; firm-bank-quarter lending regressions; high-dimensional fixed effects; placebo pseudogroups
datasets: Gruppi Italiani; Centrale dei Bilanci; Italian Credit Register; Bank of Italy Supervisory Reports
identification: Bank health shocks interacted with group affiliation and firm fundamentals
main_result: Group-affiliated firms survive crises better because internal capital markets substitute for distressed bank finance.
exam_relevance: high
must_memorize: true
tags:
  - internal-capital-markets
  - business-groups
  - financial-constraints
  - bank-lending-channel
  - crisis-finance
  - corporate-finance
  - DrJandik
created: 2026-06-05
updated: 2026-06-05
---

# Santioni, Schiantarelli, and Strahan 2020

## 1. One-Sentence Takeaway
This paper shows that Italian business-group affiliates survive financial crises better than standalone firms using granular firm-bank and intragroup-transfer data, and the main contribution is direct evidence that internal capital markets substitute for distressed bank finance.

## 2. Exam-Ready Abstract
Santioni, Schiantarelli, and Strahan ask whether internal capital markets become more valuable when external capital markets are impaired. The setting is Italy during the global financial crisis and euro sovereign debt crisis, when bank balance sheets deteriorated and credit supply contracted. The authors combine data on Italian business groups, firm financial statements, firm-bank credit links, bank balance sheets, and intragroup financial transfers. They show that group-affiliated firms are more likely to survive than unaffiliated firms, and that their survival depends less on the health of their banks. The mechanism is internal reallocation: cash-rich affiliates transfer funds to cash-poor affiliates, especially when the recipient firm’s banks are distressed. The paper contributes direct evidence on the value of internal capital markets during crises and connects to [[Internal Capital Markets]], [[Financial Constraints]], [[Bank Lending Channel]], and [[Business Groups]].

## 3. Research Question
What is the paper trying to answer?

Do business groups help firms survive financial crises because group affiliates can access internal capital markets when banks become distressed?

More specifically: the paper tests whether group affiliation insulates firms from bank credit-supply shocks, whether intragroup transfers increase when bank health deteriorates, and whether funds flow from cash-rich to cash-poor firms with some evidence of allocation toward better investment opportunities.

## 4. Core Mechanism

```text
Bank balance-sheet deterioration
-> external credit supply contracts
-> standalone firms become more exposed to financing constraints
-> group-affiliated firms substitute toward internal capital transfers
-> cash-rich affiliates fund cash-poor affiliates
-> affiliated firms are less likely to fail during the crisis
```

## 5. Main Findings
1. Group-affiliated firms are more likely to survive the crisis. Kaplan-Meier estimates imply survival from 2006 to 2013 of about 56% for group firms versus about 50% for unaffiliated firms.
2. Bank distress matters less for group firms. A one-standard-deviation increase in bank bad loans raises annual failure risk by about 0.48 percentage points for unaffiliated firms but only about 0.27 percentage points for group-affiliated firms.
3. Group-wide resources predict survival. A firm is less likely to fail when other firms in the same group have stronger cash flow or sales growth; placebo pseudogroups do not show this pattern.
4. Internal transfers respond to bank distress. Cash-poor affiliates borrow more from the internal capital market when their banks are weak, while cash-rich affiliates supply funds.
5. Transfers look partly efficient. Firms with above-median sales growth receive more support when cash flow is low, suggesting that groups are not simply propping up weak firms.
6. Groups also appear to share debt capacity. Firms borrow more internally when other affiliates have more bank debt capacity.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Firm-year for survival and transfer analysis; firm-bank-quarter for credit supply validation |
| Sample period | Annual firm panel from 2004 to 2014; survival analysis from 2006 to 2013 |
| Main dataset | Gruppi Italiani for business-group structure; Centrale dei Bilanci for firm financials; Italian Credit Register for firm-bank credit links; Bank of Italy Supervisory Reports for bank health |
| Key variables | Group affiliation; firm failure; Bad Loans; Cash Flow/Assets; Sales Growth; Other Cash Flow; Other Sales Growth; Intragroup Net Financial Position |
| Treatment or shock | Firm exposure to distressed banks, measured by the weighted average bad-loans ratio of the firm’s lending banks |
| Outcome variables | Firm failure, bank loan growth, intragroup net financial borrowing, intragroup financial plus trade position |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between group affiliation and survival is not causal because firms in business groups differ from standalone firms in size, age, industry, governance, access to collateral, managerial quality, and selection into ownership structures. Bank health is also endogenous because firms may match with particular banks based on risk, region, industry, or relationship lending. Internal transfers are endogenous because firms receive transfers when they are weak, but transfers may also affect future performance. Sales growth is an imperfect proxy for investment opportunities and may itself respond to internal financing.

### Identification Approach
- Natural experiment: The global financial crisis and euro sovereign debt crisis create large shocks to Italian bank balance sheets.
- Instrument: No central instrument. The authors mention using lagged sales growth as instruments in unreported robustness for transfer regressions.
- Difference in differences: Not a clean two-by-two design, but the logic compares how bank distress affects group versus unaffiliated firms and how transfer sensitivities vary with bank distress.
- Event study: Kaplan-Meier survival analysis and year-varying transfer sensitivity to cash flow; not a conventional event-study design.
- Fixed effects: Industry-year, region-year, province-year, firm-size-year, firm fixed effects, group-year fixed effects in transfer regressions, bank fixed effects and firm-quarter fixed effects in lending regressions.
- Matching: The authors report that propensity-score-matched survival results are similar, but matching is not the core design.
- Placebo tests: Pseudogroups are constructed from unaffiliated firms. Other cash flow and other sales growth do not predict survival in these fake groups.
- Robustness: Logit hazard model; no-ownership-switch sample; broader bank health index; main-bank-share controls; number-of-banks fixed effects.
- Alternative source of variation: Firm-specific exposure to bad banks based on preexisting lending relationships.

### Is the Identification Convincing?
- Strength: The paper has unusually direct data on firm-bank relationships and intragroup financial transfers, which lets it test the mechanism rather than infer it from investment or valuation alone.
- Weakness: Group affiliation is not randomly assigned, and distressed-bank exposure may still correlate with unobserved borrower risk or local economic shocks.
- Referee concern: The survival advantage may reflect unobserved group quality, implicit guarantees, collateral sharing, or better governance rather than internal capital markets alone.

## 8. Main Regression or Model

```text
Failure_it =
  beta1 Group_i
+ beta2 BadLoans_i,t-1
+ beta3 Group_i x BadLoans_i,t-1
+ beta4 SalesGrowth_i,t-1
+ beta5 CashFlow_i,t-1
+ beta6 LogAssetRatio_i,t-1
+ beta7 LogAge_i
+ Fixed Effects
+ epsilon_it
```

This is a discrete-time hazard model estimated as a linear probability model. The outcome is whether the firm fails in year t, conditional on having survived to the start of the year. The key coefficient is beta3. A negative beta3 means that group affiliation reduces the effect of bank distress on firm failure, consistent with internal capital markets substituting for external finance.

```text
NetTransfer_it =
  beta1 SalesGrowth_it
+ beta2 OtherSalesGrowth_it
+ beta3 CashFlow_it
+ beta4 OtherCashFlow_it
+ beta5 BadLoans_i,t-1 x SalesGrowth_it
+ beta6 BadLoans_i,t-1 x OtherSalesGrowth_it
+ beta7 BadLoans_i,t-1 x CashFlow_it
+ beta8 BadLoans_i,t-1 x OtherCashFlow_it
+ beta9 BadLoans_i,t-1
+ Firm FE
+ Industry-Year FE
+ Province-Year FE
+ Group-Year FE
+ epsilon_it
```

The dependent variable is intragroup net borrowing. Positive values mean the firm borrows from the internal capital market; negative values mean the firm lends to affiliates. The main coefficient is beta7. A negative beta7 means that when banks are distressed, the sensitivity of transfers to own cash flow becomes more negative, so cash-poor firms borrow more internally and cash-rich firms lend more internally.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Internal Capital Markets]] by showing direct intragroup transfers, not just investment sensitivities.
2. [[Financial Constraints]] by showing that internal capital markets become more valuable when external finance is impaired.
3. [[Bank Lending Channel]] by linking firm outcomes to the health of each firm’s actual lending banks.

It differs from prior work because it observes business-group affiliation, intragroup financial flows, firm-bank links, and bank health in the same setting.

## 10. Closely Related Papers
- [[Stein 1997]]: Theoretical benchmark for efficient internal capital markets reallocating funds toward better uses.
- [[Scharfstein and Stein 2000]]: Agency-cost view of internal capital markets and divisional rent seeking.
- [[Lamont 1997]]: Internal capital markets and inefficient cross-subsidization in oil firms.
- [[Shin and Stulz 1998]]: Segment-level investment and internal capital markets in diversified firms.
- [[Gopalan, Nanda, and Seru 2007]]: Indian business groups and financial support among affiliates.
- [[Almeida, Kim, and Kim 2015]]: Korean chaebols and internal capital markets during the Asian financial crisis.
- [[Matvos and Seru 2014]]: Resource allocation within firms during financial market dislocation.
- [[Kuppuswamy and Villalonga 2015]]: Diversification value during the 2007 to 2009 financial crisis.
- [[Khwaja and Mian 2008]]: Firm-bank matched data design for separating credit supply from credit demand.
- [[Chava and Purnanandam 2011]]: Real effects of banking crises on bank-dependent borrowers.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the literature on internal capital markets. Are internal capital markets efficient, and when do they create value?

How to use this paper:
- Main finding: Internal capital markets are especially valuable when external finance is constrained.
- Data: Italian business groups, firm-bank credit relationships, bank balance sheets, and direct intragroup transfers.
- Identification: Compare group and standalone firms exposed to different levels of bank distress; validate bank bad loans as a credit-supply shock using firm-bank-quarter loan regressions.
- Limitation: Group affiliation and bank relationships are endogenous; sales growth is only a proxy for investment opportunities.
- Connection to other papers: Use it after [[Stein 1997]] and before agency critiques like [[Scharfstein and Stein 2000]] and [[Lamont 1997]].
- Best exam phrase: “Santioni, Schiantarelli, and Strahan provide direct evidence that internal capital markets act as a substitute for bank finance when external capital markets are distressed.”

## 12. Hypotheses Inspired by This Paper
H1: Firms affiliated with business groups are less sensitive to bank credit-supply shocks than unaffiliated firms.

H2: Within business groups, cash-poor affiliates receive larger internal transfers when their banks become distressed.

H3: Internal transfers are more likely to support firms with stronger investment opportunities, proxied by high sales growth.

## 13. Possible Extension or Research Design
- Research question: Do multinational business groups reallocate liquidity across borders when local banks become distressed?
- Hypothesis: Affiliates in countries hit by bank distress receive larger internal transfers from affiliates in less distressed countries, especially when the receiving affiliate has high growth opportunities.
- Data: Orbis ownership links, firm financials, bank balance-sheet data, syndicated loan exposures, and country-level bank stress measures.
- Identification: Use bank stress or sovereign-bank exposure shocks interacted with group affiliation and within-group liquidity availability. Include affiliate fixed effects, group-year fixed effects, industry-country-year fixed effects, and pre-shock bank relationships.
- Expected result: Internal transfers rise for constrained affiliates, and survival or investment declines less for affiliates with cash-rich group members.
- Contribution: Extends the internal-capital-market substitution mechanism from domestic groups to multinational firm networks.

## 14. Critiques

### Major Concern 1
Group affiliation is endogenous. Groups may contain firms with better managers, stronger implicit guarantees, more collateral, or better governance. These traits may explain survival even without internal capital transfers.

### Major Concern 2
Bank distress exposure may not be fully exogenous. Firms connected to bad banks may be systematically riskier, located in weaker regions, or concentrated in industries with worse demand shocks.

### Minor Concern
Ownership structure is observed only in 2006, 2010, and 2014, so group affiliation must be assigned across intervening years. Transfers to foreign affiliates are not observable. Sales growth is an imperfect measure of investment opportunities.

### Referee Recommendation
Accept, because the paper combines unusually granular data with a clear mechanism test. The identification is not perfect, but the direct evidence on intragroup transfers, bank health, placebo pseudogroups, and robustness tests makes the contribution strong.

## 15. Memory Hooks
- “Internal capital markets are private lenders of last resort.”
- “Bad banks hurt standalone firms more than group firms.”
- “Cash-rich siblings fund cash-poor siblings.”
- “Pseudo-siblings do nothing.”
- “Italy lets them see the mechanism: banks, groups, and transfers.”

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Internal Capital Markets]], [[Financial Constraints]], [[Bank Lending Channel]], [[Business Groups]], or [[Crisis Finance]]. The clean exam answer is: “Santioni, Schiantarelli, and Strahan use Italian business-group and firm-bank matched data to show that internal capital markets substitute for bank finance when banks are distressed.” Use it to argue that internal capital markets may create value precisely when external capital markets break down. In a critique answer, emphasize endogenous group affiliation and bank-firm matching, but note that the paper is stronger than a standard correlation because it observes actual intragroup transfers and shows that transfer activity increases when the firm’s own banks deteriorate.