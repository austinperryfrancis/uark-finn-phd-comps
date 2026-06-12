---
type: paper
status: unread
title: "CEO Turnovers and Disruptions in Customer-Supplier Relationships"
authors: "Vincent J. Intintoli, Matthew Serfling, and Sarah Shaikh"
year: 2017
journal: "Journal of Financial and Quantitative Analysis"
seminar: "Not clear from provided text"
field: "Corporate Finance"
literature: "Customer-Supplier Relationships; Supply Chain Risk; CEO Turnover; Corporate Governance"
methods: "Difference-in-differences; panel fixed effects; event study; propensity-score matching; hazard model; cross-sectional heterogeneity"
datasets: "Compustat Segment Customer Files; ExecuComp; Compustat; CRSP; Thomson Reuters Insider Filing Data Feed; RiskMetrics; LexisNexis; U.S. Economic Census"
identification: "Staggered customer CEO turnover events with customer-supplier fixed effects, year fixed effects, controls, event-study evidence, propensity-score matching, placebo tests, and plausibly exogenous turnovers from death, illness, and natural retirement"
main_result: "Customer CEO turnovers disrupt dependent suppliers: suppliers lose customer-specific sales, relationships are more likely to end, supplier total sales fall, and suppliers experience negative announcement returns."
exam_relevance: high
must_memorize: true
tags:
  - customer-supplier
  - supply-chain-risk
  - ceo-turnover
  - corporate-governance
  - difference-in-differences
  - event-study
  - DrJandik
created: 2026-06-12
updated: 2026-06-12
---

# Intintoli, Serfling, and Shaikh 2017

## 1. One-Sentence Takeaway
This paper shows that customer CEO turnovers disrupt dependent suppliers using Compustat customer-supplier links and ExecuComp CEO turnover events, and the main contribution is direct evidence that managerial turnover at a customer is a meaningful source of supply-chain relationship risk.

## 2. Exam-Ready Abstract
The paper asks whether replacing a customer firm's CEO disrupts relationships with suppliers that depend on that customer for a large share of sales. The setting is U.S. public suppliers linked to ExecuComp customers from 1993 to 2011 using Compustat segment customer disclosures. The shock is a customer CEO turnover, and the main design is a staggered difference-in-differences comparing supplier sales to customers before and after turnover relative to customer-supplier pairs without a turnover. Suppliers lose substantial sales to customers after CEO turnover, relationships are more likely to end, and suppliers have negative stock-market reactions around customer CEO turnover announcements. The evidence is strongest when the incoming CEO is an outsider, the turnover is forced, or the predecessor CEO appears entrenched, consistent with successors abandoning old strategies and divesting assets. The paper connects to [[Customer-Supplier Relationships]], [[Supply Chain Risk]], [[CEO Turnover]], and [[Corporate Governance]].

## 3. Research Question
What happens to dependent suppliers when one of their major customers replaces its CEO?

More specifically: does CEO turnover at the customer disrupt existing customer-supplier relationships, and is the effect driven by successor-led strategic change, divestitures, switching suppliers, renegotiation, or the dismantling of entrenched incumbent strategies?

## 4. Core Mechanism
Use a chain that can be memorized for comps:

```text
Customer CEO turnover
-> successor changes strategy, restructures, or divests assets
-> existing supplier relationship becomes less valuable or unnecessary
-> dependent supplier loses customer-specific sales
-> supplier relationship ends or weakens
-> supplier firm value, sales, and operating performance decline
```

## 5. Main Findings
1. Customer CEO turnovers reduce supplier sales to that customer. The baseline estimate implies an 11.9% decline in customer-specific supplier sales, or about $19.1 million for the average supplier.
2. Customer-supplier relationships are more likely to end after a customer CEO turnover. The paper estimates that turnover raises the likelihood of relationship termination by about 12%.
3. Supplier shareholders price the disruption. Supplier announcement CARs around customer CEO turnover announcements are negative, about -0.61% to -0.76% across abnormal return models.
4. The effect is weaker when customers face high switching costs and stronger when suppliers have likely made relationship-specific investments.
5. Losses are larger after outsider successions, forced turnovers, and turnovers of more powerful or less monitored CEOs, consistent with successors unwinding entrenched incumbent strategies.
6. Mechanism tests point mainly to customer divestitures, not better supplier pricing or broad supplier switching.
7. Suppliers that lose sales after customer CEO turnovers experience declines in total sales, firm value, ROA, profit margins, operating margins, and gross margins, plus higher SG&A intensity.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Customer-supplier-year |
| Sample period | 1993 to 2011 |
| Main dataset | Compustat Segment Customer Files matched to ExecuComp customers |
| Sample size | 22,797 customer-supplier-years; 5,876 customer-supplier pairs; 2,998 suppliers; 787 customers |
| Treatment group | Customer-supplier pairs where the customer replaces its CEO during the relationship |
| Control group | Customer-supplier pairs where the customer does not replace its CEO during the relationship, plus not-yet-treated relationships in staggered timing |
| CEO turnover data | ExecuComp, with announcement dates from LexisNexis |
| Stock returns | CRSP |
| Financial variables | Compustat annual files |
| Governance data | Thomson Reuters Insider Filing Data Feed and RiskMetrics |
| Key variables | POST_TURNOVER, PCT_SALES, SIGN_CUST, PCT_ASSETS, supplier CARs, customer switching costs, supplier/customer R&D, outsider succession, forced turnover, CEO power, board busyness, director ownership |
| Treatment or shock | Replacement of the customer's CEO |
| Outcome variables | Supplier sales to customer, relationship termination, supplier total sales, supplier CARs, Tobin's Q, ROA, ROE, margins, SG&A |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between customer CEO turnover and supplier sales is not causal because CEO turnover is endogenous. Poor customer performance, declining business segments, board-led strategic change, or deteriorating customer-supplier relationships could cause both CEO turnover and lower supplier sales. Forced turnover is especially problematic because boards may replace CEOs precisely when they want to change strategy, divest assets, or reduce reliance on particular suppliers. There is also measurement error because suppliers are required to disclose customers accounting for 10% or more of sales, so drops below the threshold can look like zero sales. Finally, relationship life cycles may naturally decay over time, so a post-turnover decline could reflect normal relationship ending rather than CEO turnover.

### Identification Approach
- Natural experiment: Customer CEO turnover is treated as a disruptive event. The paper also studies plausibly exogenous turnovers from death, illness, and natural retirement.
- Instrument: None.
- Difference in differences: Compare supplier sales to treated customers before and after CEO turnover relative to customer-supplier relationships without a turnover during the same period.
- Event study: Examine supplier CARs around customer CEO turnover announcements.
- Fixed effects: Customer-supplier fixed effects and year fixed effects in the baseline. Some specifications add industry-year fixed effects.
- Matching: Propensity-score matched treatment and control customer-supplier pairs.
- Placebo tests: Redefine POST_TURNOVER to begin two years before or two years after the actual event. Results do not mimic the baseline negative effect.
- Robustness: Alternative handling of zero or missing sales, alternative dependent variables, hazard models for relationship termination, shorter event windows, excluding customers with many suppliers, averaging across suppliers for each customer, relationship-length matching.
- Alternative source of variation: Exogenous CEO turnovers due to death, poor health, or natural retirements, plus timing tests showing no pre-turnover decline.

### Is the Identification Convincing?
- Strength: Stronger than a standard correlation because it uses within customer-supplier-pair changes, staggered timing, event returns, many robustness tests, and plausibly exogenous turnover subsamples.
- Weakness: CEO turnover can still proxy for a board's preexisting decision to restructure. In that case, the causal object is the turnover-associated strategic change rather than the CEO personally causing the disruption.
- Referee concern: The Compustat segment disclosure threshold may turn small declines into apparent zeros. The paper addresses this with alternative missing-value assumptions, relationship-ending tests, and hazard models.

## 8. Main Regression or Model

```text
ln(1 + PCT_SALES_ict) =
  alpha POST_TURNOVER_ict
+ Controls_ict
+ Year FE_t
+ Customer-Supplier FE_ic
+ epsilon_ict
```

Here, `PCT_SALES_ict` is sales from supplier `i` to customer `c` in year `t`, scaled by the supplier's total sales. `POST_TURNOVER_ict` equals one after customer `c` replaces its CEO during that customer-supplier relationship. The coefficient `alpha` is the main difference-in-differences estimate. It measures how supplier sales to a specific customer change after that customer's CEO turnover, relative to changes in comparable customer-supplier relationships without a turnover.

For heterogeneity:

```text
ln(1 + PCT_SALES_ict) =
  beta1 POST_TURNOVER_ict
+ beta2 POST_TURNOVER_ict x Heterogeneity_ic
+ Controls_ict
+ Year FE_t
+ Customer-Supplier FE_ic
+ epsilon_ict
```

`Heterogeneity` includes high customer switching costs, high supplier R&D, high customer R&D, outsider succession, forced turnover, high CEO power, busy board, or low board ownership. `beta1` is the turnover effect for the omitted group. `beta2` tells whether the turnover effect is stronger or weaker for that group. The main economic interpretation is that turnover reduces sales, especially when the successor is likely to break from the old CEO's strategy or when the supplier is locked into relationship-specific investments.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Customer-Supplier Relationships]] by showing that relationships are not only sources of efficiency and profitability, but also sources of disruption risk.
2. [[Supply Chain Risk]] by identifying customer CEO turnover as a specific event that damages dependent suppliers.
3. [[CEO Turnover]] by showing that turnover affects nonfinancial stakeholders, not only shareholders and firm policies.
4. [[Corporate Governance]] by linking entrenchment and board monitoring to real effects on supply-chain counterparties.

It differs from prior work because prior supplier-disruption papers often use market reactions to customer bankruptcies, mergers, or LBOs. This paper provides both indirect stock-price evidence and direct customer-specific sales evidence.

## 10. Closely Related Papers
- [[Patatoukas 2012]]: Customer concentration and supplier profitability.
- [[Kale and Shahrur 2007]]: Customer-supplier relationships and capital structure with relationship-specific investments.
- [[Banerjee, Dasgupta, and Kim 2008]]: Dependent suppliers, financial leverage, and customer-supplier relationships.
- [[Hertzel, Li, Officer, and Rodgers 2008]]: Supplier stock-price reactions to customer bankruptcies.
- [[Pan, Wang, and Weisbach 2016]]: CEO turnover, divestitures, and strategic change.
- [[Weisbach 1995]]: CEO turnover and divestiture of poorly performing acquisitions.
- [[Fee and Thomas 2004]]: Horizontal mergers and effects on suppliers and customers.
- [[Brown, Fee, and Thomas 2009]]: Leveraged buyouts and customer-supplier relationships.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on customer-supplier relationships. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Customer CEO turnover disrupts dependent suppliers, reducing customer-specific sales and worsening supplier performance.
- Data: Compustat segment customer disclosures matched to ExecuComp CEO turnover data from 1993 to 2011.
- Identification: Staggered difference-in-differences with customer-supplier fixed effects, event-study CARs, propensity-score matching, placebo timing, and exogenous turnover subsamples.
- Limitation: CEO turnovers are not fully random and can reflect board-led restructuring rather than CEO-specific causal effects.
- Connection to other papers: Complements papers showing customer concentration improves efficiency by emphasizing that dependence creates fragility.
- Best exam phrase: "Intintoli, Serfling, and Shaikh show that customer concentration is a double-edged sword: it creates operating benefits in normal times but exposes suppliers to governance shocks at major customers."

## 12. Hypotheses Inspired by This Paper
H1: Suppliers experience larger sales losses after customer CEO turnovers when they have made more relationship-specific investments.

H2: Customer CEO turnover has a weaker negative effect on supplier sales when the customer faces higher supplier-switching costs.

H3: Supplier stock-price reactions to customer CEO turnover announcements are more negative when the turnover is forced, the successor is an outsider, or the outgoing CEO appears entrenched.

## 13. Possible Extension or Research Design
- Research question: Do suppliers diversify their customer base when a major customer's CEO succession risk rises?
- Hypothesis: Suppliers with customers whose CEOs are near retirement age or lack obvious internal successors begin diversifying earlier, reducing the negative effect of eventual customer CEO turnover.
- Data: FactSet Revere customer-supplier links, ExecuComp CEO age and tenure, BoardEx or proxy data on internal succession candidates, Compustat, CRSP, and possibly RavenPack for succession news.
- Identification: Use CEO age thresholds, unexpected CEO health shocks, or succession-plan disclosures as variation in customer succession risk. Estimate supplier-level changes in customer concentration before and after increases in succession risk.
- Expected result: Suppliers exposed to higher succession risk reduce dependence on the customer, add new customers, or increase cash holdings.
- Contribution: Extends the paper from realized disruption to ex ante risk management by suppliers.

## 14. Critiques

### Major Concern 1
CEO turnover is endogenous to anticipated strategic change. If the board already decided to divest assets or restructure divisions before hiring the new CEO, then the estimated effect may reflect the underlying restructuring decision rather than CEO turnover itself. The paper addresses this with exogenous turnover subsamples and timing tests, but the concern is not fully eliminated.

### Major Concern 2
Customer-specific sales are measured using segment disclosures, and the 10% reporting threshold can create measurement error. A supplier might continue selling to the customer below the threshold, but the data may record the relationship as zero. The paper deals with this using alternative assumptions for missing values, relationship-ending models, and hazard models, but disclosure-based measurement remains imperfect.

### Minor Concern
The sample is limited to public suppliers and ExecuComp-listed customers, so the setting overweights large customers and public-firm supplier relationships. Effects may differ for private suppliers, smaller customers, or international supply chains.

### Referee Recommendation
Accept, because the paper provides a clear research question, a plausible empirical design, strong economic magnitudes, direct sales evidence, market-based validation, and extensive robustness tests. The main caveat is that the causal interpretation is strongest for the plausibly exogenous turnover subset.

## 15. Memory Hooks
- "New CEO, old supplier loses."
- "$19.1 million lost customer sales."
- "Relationship death rises 12%."
- "Switching costs save suppliers."
- "RSI traps suppliers."
- "Outsider or forced CEO means bigger supplier pain."
- "Mechanism: successor divests assets, not just squeezing prices."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Customer-Supplier Relationships]], [[Supply Chain Risk]], [[CEO Turnover]], [[Corporate Governance]], [[Difference-in-Differences]], [[Event Studies]], or [[Compustat Segment Customer Files]]. The clean exam answer is: "Intintoli, Serfling, and Shaikh 2017 use customer CEO turnovers as shocks to customer-supplier relationships and show that dependent suppliers lose customer-specific sales, especially when successors are outsiders, turnovers are forced, or suppliers have made relationship-specific investments." Use it to argue that customer concentration is valuable but fragile, because dependent suppliers are exposed to governance and strategic shocks at their major customers. In a critique answer, emphasize that CEO turnovers are endogenous to restructuring, but note that the paper is stronger than a standard correlation because it uses customer-supplier fixed effects, event-study evidence, propensity-score matching, placebo timing tests, and plausibly exogenous turnovers from death, illness, and natural retirement.