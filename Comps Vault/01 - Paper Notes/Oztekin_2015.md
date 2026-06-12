---
type: paper
status: unread
title: 'Capital Structure Decisions around the World: Which Factors Are Reliably Important?'
authors: Ozde Oztekin
year: 2015
journal: Journal of Financial and Quantitative Analysis
professor: DrJandik
seminar: null
jandik_paper_number: 7
jandik_week: 2
jandik_topic: 'Capital structure: determinants and targets, taxes, and information asymmetry'
jandik_done: true
field: Corporate Finance
literature:
- '[[Capital Structure]]'
methods:
- Dynamic panel GMM
- Partial adjustment model
- Cross-country institutional analysis
- Two-stage regressions
datasets:
- Compustat Global Vantage
- Country-level legal and financial institution indexes
- Elkins McSherry debt and equity trading cost data
identification: Dynamic panel model with firm and year fixed effects, country fixed effects, lagged instruments, two-stage institutional regressions, random effects and IV robustness using legal origin and settler mortality
main_result: Across 37 countries, reliable leverage determinants are firm size, tangibility, industry leverage, profitability, and inflation, while institutional quality affects both leverage levels and adjustment speeds toward target leverage.
exam_relevance: high
must_memorize: true
tags:
- capital-structure
- leverage
- institutions
- international-finance
- dynamic-adjustment
created: 2026-06-03
updated: 2026-06-03
---

# Oztekin 2015

## 1. One-Sentence Takeaway
This paper shows that capital structure determinants are partly portable across countries using a dynamic panel of firms from 37 countries, and the main contribution is showing that institutions affect both target leverage and the speed with which firms adjust toward that target.

## 2. Exam-Ready Abstract
Öztekin asks which firm, industry, macroeconomic, and institutional factors reliably explain capital structure decisions around the world. The setting is an international panel of nonfinancial and unregulated firms from 37 countries over 1991 to 2006. The paper estimates a dynamic partial adjustment model of leverage using system GMM, allowing firms to have target leverage ratios and adjustment costs. The main finding is that profitability, tangibility, firm size, industry leverage, and inflation are the most reliable determinants of leverage across countries. The paper also shows that institutions matter: stronger institutions are associated with lower transaction costs and faster adjustment toward target leverage, while creditor-friendly institutions tend to increase leverage. The paper contributes by combining the reliable capital structure determinant literature with the law-and-finance view that institutional environments shape financial contracting. It connects directly to [[Capital Structure]], [[Dynamic Tradeoff Theory]], [[Law and Finance]], and [[International Corporate Finance]].

## 3. Research Question
What factors reliably determine firms' capital structure choices across countries?

More specifically: do standard firm-level determinants of leverage generalize outside the United States and G-7 countries, and do country-level legal and financial institutions affect both leverage levels and adjustment speeds toward target leverage?

## 4. Core Mechanism
Use a chain that can be memorized for comps:

```text
Institutional quality or financing environment
-> changes in debt and equity transaction costs
-> changes in contracting costs, bankruptcy costs, creditor rights, shareholder rights, and information asymmetry
-> firms choose different target leverage ratios and adjust at different speeds
-> observed cross-country differences in leverage and leverage rebalancing
```

## 5. Main Findings
1. The reliable determinants of leverage across countries are profitability, tangibility, firm size, industry leverage, and inflation.
2. Larger firms, firms with more tangible assets, and firms in high-leverage industries tend to use more debt, while more profitable firms tend to use less debt.
3. Higher quality institutions lead to faster adjustment toward target leverage, consistent with lower refinancing and transaction costs.
4. Creditor-friendly institutions, effective bankruptcy procedures, and stronger creditor protection tend to increase leverage.
5. Stronger shareholder protection, better disclosure, stronger enforcement, and less insider trading tend to reduce leverage, likely because equity finance becomes less costly.
6. Firm size is less reliable in weak institutional environments, suggesting that the meaning of size depends on the institutional setting.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Firm-year |
| Sample period | 1991 to 2006 |
| Main dataset | Compustat Global Vantage |
| Sample | 15,177 nonfinancial and unregulated firms from 37 countries, totaling 101,264 firm-years |
| Key variables | Book leverage, profitability, market-to-book, firm size, tangibility, industry leverage, inflation, institutional indexes |
| Treatment or shock | No single shock. Cross-country variation in legal and financial institutions |
| Outcome variables | Leverage and speed of adjustment toward target leverage |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between institutions and leverage would not be causal because countries differ along many dimensions that also affect financing policies. Legal origin, financial development, macroeconomic stability, industry composition, firm types, investor protection, creditor rights, and disclosure standards may all be jointly determined. Firms may also sort into industries and countries with particular financing environments. There is also dynamic endogeneity because past leverage affects current leverage, and firm characteristics such as profitability, tangibility, and size may be jointly determined with financing choices.

### Identification Approach
- Natural experiment: None.
- Instrument: Uses lagged variables as instruments in system GMM. For institutional robustness, uses legal origin and settler mortality as instruments for country institutions.
- Difference in differences: None.
- Event study: None.
- Fixed effects: Firm fixed effects, year fixed effects, and in some specifications country fixed effects.
- Matching: None.
- Placebo tests: Not central.
- Robustness: Separate country regressions, pooled world regressions, strong versus weak institutional partitions, alternative leverage measures, random effects, and IV specifications.
- Alternative source of variation: Cross-country institutional variation in creditor rights, shareholder rights, bankruptcy efficiency, disclosure, enforcement, insider trading, and debt or equity trading costs.

### Is the Identification Convincing?
- Strength: Strong for documenting robust international patterns and institutional correlations. The dynamic panel model improves on static leverage regressions by accounting for target leverage and adjustment costs.
- Weakness: The institutional analysis is still not fully causal because institutional quality is persistent, multidimensional, and correlated with omitted country characteristics.
- Referee concern: The instruments may violate exclusion restrictions if legal origin or settler mortality affects capital structure through channels other than the measured institutions.

## 8. Main Regression or Model

```text
LEV_ijt = (lambda_j beta_j) X_ijt-1
        + (1 - lambda_j) LEV_ijt-1
        + Firm FE
        + Year FE
        + epsilon_ijt
```

The dependent variable is leverage for firm i in country j at time t. The lagged leverage term captures partial adjustment toward a target leverage ratio. The vector X includes firm, industry, and macroeconomic determinants such as profitability, market-to-book, firm size, tangibility, industry leverage, and inflation. The coefficient on lagged leverage identifies the speed of adjustment, where lambda equals one minus the lagged leverage coefficient.

Institutional adjustment model:

```text
LEV_ijt - LEV_ijt-1 = lambda_j DEV_ijt + epsilon_ijt

lambda_j = Institution_j + MacroControls_jt + FinancialDevelopment_jt + Year FE
```

Here, DEV is the estimated deviation from target leverage. The key institutional coefficient measures whether country-level legal and financial institutions explain faster or slower adjustment toward target capital structure.

Institutional leverage model:

```text
CountryLevelLeverage_jt =
  gamma Institution_j
+ MacroControls_jt
+ FinancialDevelopment_jt
+ Year FE
+ epsilon_jt
```

This second-stage model asks whether the part of leverage explained by country-level factors is systematically related to institutional quality.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Capital Structure]] by identifying which leverage determinants are reliable across a broad international sample.
2. [[Dynamic Tradeoff Theory]] by showing that firms around the world adjust toward target leverage, but adjustment speeds differ by institutional environment.
3. [[Law and Finance]] by showing that creditor rights, shareholder rights, bankruptcy procedures, disclosure, and enforcement shape financing choices.
4. [[International Corporate Finance]] by extending U.S. and G-7 capital structure evidence to 37 countries.

It differs from prior work because it combines global leverage determinants with a dynamic target-adjustment model and explicitly studies how institutions affect both leverage levels and adjustment speeds.

## 10. Closely Related Papers
- [[Rajan and Zingales 1995]]: Studies capital structure determinants in G-7 countries and motivates the cross-country leverage literature.
- [[Frank and Goyal 2009]]: Identifies reliable U.S. capital structure determinants, providing the benchmark for Öztekin's international test.
- [[Fan, Titman, and Twite 2012]]: Studies how institutions affect capital structure and debt maturity across countries.
- [[Flannery and Rangan 2006]]: Provides dynamic tradeoff evidence that firms adjust toward target leverage.
- [[Lemmon, Roberts, and Zender 2008]]: Emphasizes persistent firm effects in capital structure.
- [[La Porta et al. 1997]]: Foundational law-and-finance paper on legal institutions and external finance.
- [[Booth et al. 2001]]: Earlier international capital structure study using developing countries.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on capital structure determinants. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Standard leverage determinants are partly portable across countries, but institutions shape both leverage levels and adjustment speeds.
- Data: Compustat Global Vantage panel of firms from 37 countries over 1991 to 2006.
- Identification: Dynamic panel GMM with firm and year fixed effects, separate and pooled country regressions, two-stage institutional regressions, and IV robustness using legal origin and settler mortality.
- Limitation: Institutional variation is not a clean natural experiment, so the evidence is stronger as broad external validity and mechanism evidence than as definitive causal identification.
- Connection to other papers: Use with [[Rajan and Zingales 1995]], [[Frank and Goyal 2009]], [[Fan, Titman, and Twite 2012]], and [[Flannery and Rangan 2006]].
- Best exam phrase: "Öztekin 2015 shows that the basic capital structure determinants travel internationally, but institutions determine the cost of moving toward target leverage."

## 12. Hypotheses Inspired by This Paper
H1: Firms in countries with stronger creditor protection maintain higher leverage because debt is cheaper and easier to enforce.

H2: Firms in countries with stronger shareholder protection use less leverage because equity financing becomes less costly.

H3: Firms in countries with lower debt and equity transaction costs adjust more quickly toward target leverage after shocks.

H4: Firm size is a weaker predictor of leverage in weak institutional environments because large firms do not receive the same financing-cost advantage when legal and financial systems are underdeveloped.

## 13. Possible Extension or Research Design
- Research question: Do improvements in bankruptcy law cause firms to increase leverage and adjust faster toward target capital structure?
- Hypothesis: Bankruptcy reforms that improve creditor recovery and reduce resolution costs increase leverage and speed of adjustment.
- Data: Firm-level financials from Compustat Global, Worldscope, or Orbis combined with country-level bankruptcy reform dates and creditor-rights indexes.
- Identification: Difference in differences around bankruptcy reforms, comparing treated countries to matched control countries without contemporaneous reforms.
- Expected result: Treated-country firms increase leverage and rebalance more quickly after reform, especially firms with more tangible assets and greater external financing needs.
- Contribution: Provides cleaner causal evidence for the institutional mechanism in Öztekin 2015.

## 14. Critiques

### Major Concern 1
The institutional variables are not randomly assigned. Countries with better institutions differ in many persistent ways, including culture, financial development, investor base, industry composition, and macroeconomic stability. The paper uses controls and IV robustness, but the institutional results should still be interpreted cautiously.

### Major Concern 2
Institutional variables bundle multiple mechanisms. Creditor rights, shareholder rights, bankruptcy efficiency, accounting standards, enforcement, and insider trading rules may simultaneously affect debt supply, equity supply, managerial incentives, and investor protection. This makes it difficult to isolate a single causal channel.

### Minor Concern
The paper focuses on book leverage as the main measure, though it does check alternative leverage definitions. Some theoretical predictions may map differently to book leverage versus market leverage.

### Referee Recommendation
Accept, because the paper provides an important international benchmark for capital structure determinants, improves on static models with dynamic adjustment, and carefully links institutions to financing costs, leverage levels, and adjustment speeds. The causal claims should be framed cautiously, but the paper is highly useful for synthesis.

## 15. Memory Hooks
- "Reliable five": size, tangibility, industry leverage, profits, inflation.
- Institutions affect both where firms want to go and how fast they get there.
- Better institutions mean faster adjustment to target leverage.
- Creditor protection raises debt; shareholder protection lowers debt.
- Think of this as Frank and Goyal 2009 plus law-and-finance plus dynamic adjustment.

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Capital Structure]], [[Dynamic Tradeoff Theory]], [[Law and Finance]], [[International Corporate Finance]], or [[Leverage Adjustment]]. The clean exam answer is: "Öztekin 2015 uses a dynamic panel of firms from 37 countries and shows that the reliable leverage determinants are size, tangibility, industry leverage, profitability, and inflation, while institutions shape leverage levels and adjustment speeds." Use it to argue that capital structure is not purely firm-specific; it also depends on country-level legal and financial contracting environments. In a critique answer, emphasize that institutional variation is not randomly assigned, but note that the paper is stronger than a standard correlation because it uses dynamic GMM, firm and year fixed effects, two-stage institutional regressions, alternative specifications, and IV robustness.
