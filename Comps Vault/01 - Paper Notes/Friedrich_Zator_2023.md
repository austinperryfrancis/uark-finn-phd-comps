---
type: paper
status: unread
title: 'Flexibility Costs of Debt: Danish Exporters During the Cartoon Crisis'
authors: Benjamin U. Friedrich; Michał Zator
year: 2023
journal: Journal of Financial Economics
professor: DrJandik
seminar: null
jandik_paper_number: 12
jandik_week: 3
jandik_topic: 'Capital structure: bankruptcy, product markets, debt ownership, and debt maturity'
jandik_done: true
field: Corporate Finance; International Trade
literature:
- Capital structure
- financial flexibility
- product-market shocks
- exporting
methods:
- Difference-in-differences
- triple differences
- event study
- loan maturity shock
- administrative microdata
datasets:
- Danish administrative firm data
- Danish Foreign Trade Statistics Register
- Accounting Register
- Danish Business Register
- employer-employee data
- loan-level bank data
identification: Unexpected boycott of Danish products in Muslim countries after 2005 Muhammad cartoon publication
main_result: Low-leverage firms redirect sales to new non-Muslim product-destination markets and offset the demand shock, while high-leverage firms do not expand and instead downsize.
exam_relevance: high
must_memorize: true
tags:
- corporate-finance
- capital-structure
created: 2026-06-03
updated: 2026-06-03
---

# Flexibility Costs of Debt: Danish Exporters During the Cartoon Crisis

## 1. One-Sentence Takeaway
This paper shows that financial flexibility allows firms to adapt to negative demand shocks using Danish exporters hit by the 2006 Muslim-country boycott, and the main contribution is direct evidence that debt limits product-market adjustment, especially entry into new markets. 

## 2. Exam-Ready Abstract
Friedrich and Zator study whether capital structure affects firms’ ability to adapt to an unexpected product-market shock. The shock is the 2006 boycott of Danish products in Muslim countries after publication of Muhammad cartoons. Using Danish administrative data on firms, exports, financial statements, workers, and loans, they compare exposed exporters to other exporters before and after the boycott. Exposed firms lose a large share of exports to Muslim markets, but average sales fall less than mechanically expected because some firms redirect sales elsewhere. The key heterogeneity is leverage: low-leverage firms enter new non-Muslim product-destination markets, increase product variety, invest, borrow, and offset lost demand, while high-leverage firms fail to expand and reduce employment. The paper contributes to [[Capital Structure]], [[Financial Flexibility]], and [[Corporate Finance and Product Markets]] by showing that debt has real flexibility costs even outside bankruptcy. 

## 3. Research Question
Does debt reduce firms’ ability to adapt to a negative product-market demand shock?

More specifically: when firms suddenly lose access to export markets, do low-leverage firms respond differently than high-leverage firms in redirecting sales, entering new markets, adjusting products, investing, borrowing, and changing employment?

## 4. Core Mechanism
Unexpected demand shock  
-> loss of exports to Muslim countries  
-> firms need costly adjustment through new markets, product changes, marketing, SG&A, and investment  
-> low-leverage firms have financial slack and can finance adjustment  
-> high-leverage firms face financing constraints and short-term cash pressure  
-> low-leverage firms expand elsewhere, high-leverage firms downsize.

## 5. Main Findings
1. Exposed Danish exporters lose a large share of exports to Muslim countries, but average total sales fall less than expected because some firms increase sales in non-Muslim markets. 
2. Low-leverage firms enter new non-Muslim product-country markets and largely offset the demand shock, while high-leverage firms do not expand and lose more total sales. 
3. Low-leverage firms increase SG&A, investment, and debt, consistent with financing costly market entry; high-leverage firms reduce employment and increase outsourcing, consistent with substitution toward operational flexibility. 

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Mainly firm-year; some analyses use firm-product-country-year |
| Sample period | Baseline 2001 to 2006, with some extended analyses to 2010 |
| Main dataset | Danish administrative data on firm exports, accounting statements, business register information, workers, and bank loans |
| Key variables | Export destinations, product-country pairs, total sales, wages, employment, SG&A, investment, debt, leverage |
| Treatment or shock | Exposure to Muslim-country export markets before the 2006 boycott of Danish goods |
| Outcome variables | Exports to Muslim countries, exports to non-Muslim countries, total sales, new markets, product variety, employment, wages, investment, SG&A, debt, outsourcing |

## 7. Identification Strategy

### Endogeneity Problem
The main endogeneity concern is that leverage is not randomly assigned. High-leverage firms may differ from low-leverage firms in management quality, growth opportunities, product mix, risk, prior expansion, customer networks, or industry exposure. Reverse causality is less concerning because leverage is measured before an unexpected boycott, so firms could not easily choose capital structure in anticipation of the shock. Selection is still important because firms exporting to Muslim countries differ from other exporters, and low-leverage exposed firms may have been more adaptable even without the boycott.

### Identification Approach
- Natural experiment: 2006 boycott of Danish products in Muslim countries after the cartoon crisis.
- Instrument: No traditional IV in the main design.
- Difference in differences: Compares exposed exporters to non-exposed exporters before and after 2006.
- Event study: Shows pre-trends and timing of export and sales responses.
- Fixed effects: Firm fixed effects, industry-year fixed effects, and high-leverage-by-year fixed effects in triple-difference models.
- Matching: Robustness using matched firms based on pre-boycott characteristics.
- Placebo tests: Uses pre-trend/event-study evidence and controls for alternative heterogeneity channels.
- Robustness: Uses debt maturing soon as a quasi-exogenous financing-constraint shock, following the logic of Almeida et al. (2011). Firms with debt maturing soon behave like high-leverage firms: they lose Muslim exports but do not expand to new non-Muslim markets. 

### Is the Identification Convincing?
- Strength: The shock is sudden, politically driven, and plausibly unrelated to individual firm leverage choices.
- Weakness: Leverage may proxy for unobserved adaptability, managerial quality, or product-market opportunities.
- Referee concern: The paper must show that low-leverage firms are not simply better firms with better latent growth options. The debt-maturity evidence and rich controls help, but one could still worry that financing constraints and firm type are hard to fully separate.

## 8. Main Regression or Model

```text
Outcome_it = beta Exposed_i x Post_t + Controls_it + Firm FE + Industry-Year FE + epsilon_it
````

This estimates whether firms exposed to Muslim markets changed outcomes after the boycott relative to non-exposed exporters in the same industry-year.

For leverage heterogeneity:

```text
Outcome_it =
  beta1 Exposed_i x Post_t
+ beta2 Exposed_i x Post_t x HighLeverage_i
+ Controls_it
+ Firm FE
+ Industry-Year FE
+ HighLeverage-Year FE
+ epsilon_it
```

Here, `beta1` is the effect for low-leverage exposed firms, while `beta2` is the additional effect for high-leverage exposed firms. A negative `beta2` for new markets or sales means high leverage reduces adaptation to the shock.

## 9. Contribution to the Literature

This paper contributes to:

1. [[Capital Structure]] by showing that debt has real flexibility costs, not just expected bankruptcy or tax effects.
2. [[Financial Constraints]] by showing that financing constraints shape firms’ response to real demand shocks.
3. [[International Trade and Finance]] by linking capital structure to export-market entry and product-destination adjustment.

It differs from prior work because it studies how debt affects entry into new product-market destinations, not just pricing, investment, employment, or bankruptcy outcomes. It also uses a clean real shock rather than a banking or credit supply shock.

## 10. Closely Related Papers

* [[Graham and Harvey 2001]]: CFOs say financial flexibility is a major determinant of capital structure.
* [[Giroud and Mueller 2017]]: High-leverage firms experience larger employment losses during the Great Recession.
* [[Almeida et al. 2011]]: Debt maturity creates variation in refinancing needs and financial constraints.
* [[Chevalier 1995]]: Debt affects product-market behavior and competition.
* [[Paravisini et al. 2015]]: Credit shocks affect exports.
* [[Foley and Manova 2015]]: Review of finance and international trade.

## 11. How This Paper Could Appear on Comps

Possible exam question:

> Review the main findings of the literature on capital structure and product-market outcomes. Discuss the data used and how the papers establish causality.

How to use this paper:

* Main finding: Debt reduces flexibility. Low-leverage firms redirect sales after a shock, while high-leverage firms downsize.
* Data: Danish administrative data linking exports, product-country markets, financial statements, workers, and loans.
* Identification: Unexpected boycott of Danish products in Muslim countries, DiD and triple differences by leverage, plus debt-maturity robustness.
* Limitation: Leverage is endogenous and may proxy for unobserved firm adaptability.
* Connection to other papers: Use with [[Giroud and Mueller 2017]] for employment effects of leverage, [[Graham and Harvey 2001]] for financial flexibility motives, and [[Paravisini et al. 2015]] for finance and exporting.

## 12. Hypotheses Inspired by This Paper

H1: Firms with lower pre-shock leverage are more likely to enter new product-destination markets after a negative demand shock.

H2: High-leverage firms respond to demand shocks by reducing employment and increasing outsourcing rather than by expanding into new markets.

H3: The flexibility cost of debt is larger in industries where market entry requires higher fixed costs, product adaptation, or customer-specific investment.

## 13. Possible Extension or Research Design

* Research question: Does financial flexibility affect firms’ ability to rewire supply chains after geopolitical shocks?
* Hypothesis: Low-leverage firms are more likely to replace sanctioned suppliers or customers and maintain sales after a geopolitical disruption.
* Data: FactSet Revere supply chain links, Compustat Global, Orbis, sanctions exposure, firm financials.
* Identification: Difference-in-differences around Russia’s 2022 invasion of Ukraine, comparing firms exposed to Russian suppliers or customers to similar non-exposed firms, interacted with pre-shock leverage or cash holdings.
* Expected result: Low-leverage or high-cash firms adjust relationships faster and suffer smaller sales declines.
* Contribution: Extends flexibility-cost logic from export demand shocks to global supply-chain resilience.

## 14. Critiques

### Major Concern 1

Leverage is endogenous. Firms with low leverage may have better managers, better products, more slack capacity, or stronger growth opportunities. The paper addresses this with fixed effects, controls, matching, and debt-maturity tests, but this remains the main identification concern.

### Major Concern 2

Exposure to Muslim markets may not be random. Firms exporting to these markets may differ in product type, demand volatility, or global orientation. Industry-year fixed effects and firm fixed effects help, but product-level demand differences may still matter.

### Minor Concern

The boycott is temporary and culturally specific, so external validity may be limited. The mechanism likely generalizes to demand shocks, but the exact setting is unusual.

### Referee Recommendation

R&R leaning accept, because the setting is compelling, the data are unusually rich, and the findings speak directly to capital structure theory. The main request would be more evidence that leverage is not proxying for unobserved adaptability.

## 15. Memory Hooks

* “Debt blocks detours”: low-debt firms find new routes when Muslim markets close.
* Cartoon crisis = clean demand shock to Danish exporters.
* Low leverage expands, high leverage contracts.
* Financial flexibility shows up in product-market entry, not just survival.
* High leverage substitutes operational flexibility for financial flexibility through outsourcing.

## 16. Comps Use Rating

| Category                            | Rating |
| ----------------------------------- | ------ |
| Must memorize?                      | Yes    |
| Identification importance           | High   |
| Good for synthesis?                 | High   |
| Good for research design question?  | High   |
| Good for critique/referee question? | High   |

## 17. Comps Use

Deploy this paper when asked about [[Capital Structure]], [[Financial Flexibility]], [[Financial Constraints]], [[Product Market Competition]], or [[International Trade and Finance]]. The clean exam answer is: “Friedrich and Zator use the Danish cartoon-crisis boycott as an unexpected demand shock and show that low-leverage firms can redirect sales to new product-country markets, while high-leverage firms cannot and instead downsize.” Use it to argue that debt has an ex ante cost: it reduces the option value of future adaptation. In a critique answer, emphasize that leverage is endogenous, but the paper is stronger than a standard leverage-outcome regression because it uses a shock, firm fixed effects, industry-year fixed effects, triple differences, event studies, matching, and debt maturity variation.


