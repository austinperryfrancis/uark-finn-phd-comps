---
type: paper
status: unread
title: "Understanding the Rise in Corporate Cash: Precautionary Savings or Foreign Taxes"
authors: Michael W. Faulkender, Kristine W. Hankins, Mitchell A. Petersen
year: 2019
journal: Review of Financial Studies
seminar:
field: Corporate Finance
literature: Corporate Cash Holdings; Corporate Taxes; Multinational Firms; Financial Flexibility
methods: Panel regressions; decomposition; subsidiary-level analysis; heterogeneity by R&D and related-party sales
datasets: BEA BE-10 and BE-11 surveys; Compustat; KPMG and Comtax corporate tax rates
identification: Location of cash across domestic and foreign subsidiaries, effective foreign tax-rate variation, and heterogeneity by R&D and related-party sales
main_result: The rise in U.S. corporate cash is concentrated in foreign subsidiaries of multinational firms and is mainly explained by foreign tax incentives and income shifting, not precautionary savings.
exam_relevance: high
must_memorize: true
tags:
  - corporate-cash
  - tax-avoidance
  - multinational-firms
  - income-shifting
  - financial-flexibility
  - DrJandik
  - corporate-finance
created: 2026-06-04
updated: 2026-06-04
---

# Faulkender, Hankins, and Petersen 2019

## 1. One-Sentence Takeaway
This paper shows that the rise in U.S. corporate cash is concentrated in the foreign subsidiaries of multinational firms using confidential BEA subsidiary-level data, and the main contribution is showing that foreign tax incentives and income shifting, rather than precautionary savings, explain most of the increase.

## 2. Exam-Ready Abstract
Faulkender, Hankins, and Petersen ask why U.S. corporations accumulated so much cash in the late 1990s and 2000s. The standard explanation is precautionary savings: firms hold cash to avoid costly external finance when investment opportunities arrive. The paper separates total cash into domestic and foreign cash using confidential BEA data on U.S. multinational foreign affiliates and Compustat data on total cash. This location-based approach shows that precautionary variables explain domestic cash holdings, but not foreign cash holdings. Foreign cash rises when firms face lower foreign effective tax rates, especially among firms with R&D and high related-party sales, consistent with income shifting to low-tax jurisdictions. The paper contributes by showing that what looks like a broad cash-hoarding puzzle is actually concentrated in foreign subsidiaries of multinationals with strong tax incentives. It connects to [[Corporate Cash Holdings]], [[Precautionary Savings]], [[Corporate Taxes]], [[Income Shifting]], and [[Multinational Firms]].

## 3. Research Question
What explains the dramatic rise in U.S. corporate cash holdings?

More specifically: is the rise in cash driven by precautionary savings motives, such as financing frictions and investment uncertainty, or by foreign tax incentives that encourage U.S. multinationals to keep cash abroad?

The key mechanism tested is whether falling foreign tax rates, combined with firms' ability to shift income through intangible assets and related-party sales, cause cash to accumulate in foreign subsidiaries.

## 4. Core Mechanism

```text
Falling foreign tax rates relative to U.S. tax rates
-> stronger incentive to earn and retain income in low-tax foreign jurisdictions
-> intangible assets and related-party sales make income shifting easier
-> multinational firms accumulate earnings abroad rather than repatriating them
-> foreign subsidiary cash rises sharply, while domestic cash follows precautionary motives
```

## 5. Main Findings
1. The rise in corporate cash is not uniform across firms or locations. It is concentrated in the foreign subsidiaries of U.S. multinational firms.
2. Precautionary savings variables explain domestic cash holdings but do not explain foreign cash holdings.
3. Lower foreign effective tax rates predict higher foreign cash, and the effect is strongest for firms with R&D and related-party sales.
4. The authors estimate that roughly 79% of the increase in foreign cash is explained by reductions in foreign tax rates.
5. About 92% of the growth in foreign cash is concentrated in firms with both significant related sales and intangible assets.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Firm-year and foreign subsidiary-year |
| Sample period | 1998 to 2008 for the key BEA foreign cash data |
| Main dataset | Confidential BEA surveys of U.S. multinational firms, especially BE-10 and BE-11 |
| Other datasets | Compustat for total cash and firm characteristics; KPMG and Comtax for corporate tax rates |
| Key variables | Total cash, domestic cash, foreign cash, effective tax rate, R&D, related sales, sales, PPE, leverage, market-to-book, cash flow volatility |
| Treatment or shock | Declining foreign corporate tax rates relative to the U.S. tax rate, plus ability to shift income through related-party sales |
| Outcome variables | Total cash/assets, domestic cash/assets, foreign cash/assets, subsidiary cash/assets |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between cash holdings and tax rates is not automatically causal. Firms that choose low-tax jurisdictions may differ systematically from other firms in profitability, industry, growth opportunities, multinational scale, access to capital markets, and intangible asset intensity. Reverse causality is less likely for statutory foreign tax rates, but selection into countries and the endogenous location of income are major concerns. There is also measurement error because foreign cash is not directly observable in public data and must be measured using confidential BEA affiliate data.

### Identification Approach
- Natural experiment: Not a clean natural experiment. The paper uses changes in foreign tax rates and regulatory conditions, especially the post-1997 check-the-box environment, as economically meaningful variation.
- Instrument: None.
- Difference in differences: Not a canonical DiD, but the logic compares domestic versus foreign cash and firms with different exposure to foreign tax incentives.
- Event study: Not the main design.
- Fixed effects: Baseline regressions include year effects and controls. Subsidiary-level analyses exploit within-firm and across-subsidiary variation more directly.
- Matching: Not central.
- Placebo tests: The strongest placebo logic is that precautionary variables should matter for both domestic and foreign cash if precautionary savings is the explanation, but they mainly explain domestic cash.
- Robustness: Results are robust to using benchmark survey years and alternative precautionary-savings controls.
- Alternative source of variation: Heterogeneity by R&D and related-party sales tests whether firms with greater income-shifting ability are more responsive to low foreign tax rates.

### Is the Identification Convincing?
- Strength: The strongest feature is the ability to observe where cash is held, which public datasets generally cannot do. Separating domestic and foreign cash is central to distinguishing precautionary savings from tax motives.
- Weakness: The design is not a clean shock-based causal design. Firms choose where to operate, where to locate intangible assets, and how to structure related-party sales.
- Referee concern: Low tax rates may proxy for unobserved business strategy, multinational complexity, industry trends, or global growth opportunities rather than tax avoidance alone.

## 8. Main Regression or Model

```text
Cash_it / Assets_it =
  beta EffectiveTaxRate_it
+ gamma FirmControls_it
+ Year FE
+ epsilon_it
```

The paper estimates cash holdings as a function of a firm's effective tax rate and standard determinants of cash. The key dependent variables are total cash, domestic cash, and foreign cash. If the tax story is correct, lower effective tax rates should predict more foreign cash. If the precautionary story is correct, variables such as cash flow volatility, R&D, market-to-book, weak access to capital markets, and low asset tangibility should predict cash holdings.

The heterogeneity version is:

```text
ForeignCash_it / Assets_it =
  beta1 EffectiveTaxRate_it
+ beta2 RelatedSales_it
+ beta3 EffectiveTaxRate_it x RelatedSales_it
+ beta4 R&D_i
+ Controls_it
+ Year FE
+ epsilon_it
```

The main economic interpretation is in beta1 and beta3. A negative beta1 means lower foreign tax rates increase foreign cash. A negative beta3 means the tax sensitivity of foreign cash is stronger when related-party sales are high, which is consistent with transfer pricing and income shifting. R&D matters because intangible assets make income shifting easier.

A subsidiary-level version is:

```text
SubsidiaryCash_ijt / FirmAssets_it =
  beta1 SubsidiaryTaxRate_jt
+ beta2 RelatedSales_ijt
+ beta3 SubsidiaryTaxRate_jt x RelatedSales_ijt
+ Controls_ijt
+ Fixed Effects
+ epsilon_ijt
```

This asks whether cash accumulates specifically in low-tax subsidiaries with high related-party sales, rather than simply in subsidiaries with more real business activity.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Corporate Cash Holdings]] by showing that aggregate cash growth hides major location differences between domestic and foreign cash.
2. [[Precautionary Savings]] by showing that precautionary motives explain domestic cash but not foreign cash.
3. [[Corporate Taxes]] and [[Income Shifting]] by documenting that low foreign tax rates and transfer-pricing ability explain foreign cash accumulation.

It differs from prior work because it uses confidential BEA data to observe foreign subsidiary cash directly and separates total cash into domestic and foreign components.

## 10. Closely Related Papers
- [[Opler et al. 1999]]: Baseline determinants of corporate cash holdings and the tradeoff/precautionary motives for cash.
- [[Bates, Kahle, and Stulz 2009]]: Shows that U.S. firms increased cash holdings and links the rise to risk and precautionary savings.
- [[Foley et al. 2007]]: Earlier evidence that repatriation taxes affect foreign cash holdings.
- [[Faulkender and Petersen 2012]]: Related work on taxes, capital structure, and repatriation incentives.
- [[Graham and Leary 2018]]: Broad historical perspective on corporate cash and leverage patterns.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on corporate cash holdings. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: The rise in cash is mainly a foreign subsidiary tax phenomenon, not simply a precautionary savings phenomenon.
- Data: Confidential BEA data on U.S. multinational foreign affiliates combined with Compustat.
- Identification: Separates domestic and foreign cash, then tests whether precautionary variables and tax variables explain each location differently.
- Limitation: Not a clean quasi-natural experiment because firms choose foreign operations and income-shifting structures.
- Connection to other papers: Contrasts with [[Bates, Kahle, and Stulz 2009]], which emphasizes precautionary savings; extends [[Foley et al. 2007]] by using later tax-regime variation and location-specific cash data.
- Best exam phrase: "Faulkender, Hankins, and Petersen show that the cash puzzle is largely a foreign cash puzzle."

## 12. Hypotheses Inspired by This Paper
H1: Multinational firms with greater exposure to low-tax foreign jurisdictions hold more foreign cash than similar firms with higher foreign effective tax rates.

H2: The tax sensitivity of foreign cash is stronger for firms with more intangible assets because intangible assets facilitate income shifting.

H3: Related-party sales amplify the relation between low foreign tax rates and foreign cash accumulation because they provide a transfer-pricing channel.

## 13. Possible Extension or Research Design
- Research question: Did the Tax Cuts and Jobs Act of 2017 reduce foreign cash accumulation and alter investment, payout, or domestic borrowing behavior?
- Hypothesis: Firms with the largest pre-TCJA foreign cash balances should experience the largest post-TCJA changes in repatriation, payouts, and domestic liquidity management.
- Data: Compustat, firm 10-K foreign cash disclosures where available, BEA aggregate data, tax footnotes, payout data, and segment-level foreign income measures.
- Identification: Difference-in-differences comparing high trapped-cash firms to low trapped-cash firms before and after TCJA.
- Expected result: High trapped-cash firms repatriate more and reduce foreign cash, but may increase payouts more than real investment.
- Contribution: Connects the trapped-cash literature to tax reform, payout policy, and real effects of corporate tax changes.

## 14. Critiques

### Major Concern 1
The empirical design is not a clean causal shock. Firms select into low-tax countries, foreign subsidiaries, R&D-intensive business models, and related-party sales structures. This makes it difficult to fully separate tax incentives from broader multinational strategy.

### Major Concern 2
R&D is used as a proxy for intangible assets and transfer-pricing ability, but R&D also proxies for growth opportunities, uncertainty, and financing frictions. The paper's contribution is to show that R&D predicts different cash behavior depending on cash location, but the interpretation still depends on R&D capturing income-shifting ability.

### Minor Concern
Foreign cash and marketable securities are partly estimated from BEA categories, especially outside benchmark survey years. Measurement error could attenuate or distort some subsidiary-level findings.

### Referee Recommendation
Accept, because the paper uses uniquely strong confidential data to separate domestic and foreign cash and provides a powerful reinterpretation of the corporate cash puzzle. The identification is not perfect, but the data advantage and mechanism tests make the contribution substantial.

## 15. Memory Hooks
- "Foreign cash, not domestic cash."
- "Precautionary savings explains domestic cash; taxes explain foreign cash."
- "R&D is not just growth. It is also income-shifting ability."
- "Related sales plus low taxes equals trapped cash."
- "The cash puzzle is a multinational tax puzzle."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Corporate Cash Holdings]], [[Precautionary Savings]], [[Corporate Taxes]], [[Income Shifting]], or [[Multinational Firms]]. The clean exam answer is: "Faulkender, Hankins, and Petersen use confidential BEA data to separate domestic and foreign cash and show that the rise in corporate cash is concentrated in foreign subsidiaries of multinationals, where lower foreign tax rates and income-shifting ability explain cash accumulation." Use it to argue that aggregate cash holdings can be misleading because the motive for holding cash depends on where the cash is located. In a critique answer, emphasize selection into low-tax countries and R&D-intensive multinational structures, but note that the paper is stronger than a standard correlation because it directly observes foreign subsidiary cash and shows that precautionary motives explain domestic cash but not foreign cash.