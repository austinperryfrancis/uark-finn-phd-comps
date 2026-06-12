---
type: paper
status: unread
title: Input Specificity and the Propagation of Idiosyncratic Shocks in Production Networks
authors: Jean-Noël Barrot and Julien Sauvagnat
year: 2016
journal: Quarterly Journal of Economics
seminar: Not clear from provided text
field: Corporate Finance, Macro Finance, Industrial Organization
literature: Production Networks, Supply Chain Finance, Firm Shocks and Aggregate Fluctuations
methods: Difference in differences, event study, firm fixed effects, network empirics
datasets: Compustat Segment, Compustat Fundamentals Quarterly, SHELDUS, Infogroup, CRSP, Rauch input specificity classification, Google/Kogan patent data
identification: Major natural disasters hitting supplier headquarters counties
main_result: Supplier shocks reduce customer sales growth by about 2 to 3 percentage points, especially when the supplier produces specific inputs.
exam_relevance: high
must_memorize: true
tags:
  - production-networks
  - supply-chain
  - input-specificity
  - natural-disasters
  - firm-shocks
  - qje
  - DrJandik
created: 2026-06-12
updated: 2026-06-12
---

# Barrot and Sauvagnat 2016

## 1. One-Sentence Takeaway
This paper shows that idiosyncratic shocks propagate through production networks using natural disasters as shocks to suppliers, and the main contribution is showing that [[Input Specificity]] and supplier switching costs determine whether firm-level shocks become real output and valuation losses.

## 2. Exam-Ready Abstract
Barrot and Sauvagnat ask whether firm-level idiosyncratic shocks are absorbed by production networks or transmitted to economically linked firms. They use major U.S. natural disasters from 1978 to 2013 as plausibly exogenous shocks to suppliers and trace their effects through supplier-customer links reported in Compustat Segment data. In a firm-quarter difference-in-differences design with firm and time fixed effects, customers whose suppliers are hit by disasters experience about a 2 to 3 percentage point decline in sales growth. The effect is much stronger when the disrupted supplier produces specific inputs, measured by differentiated goods, high R&D, or patents. The sales losses translate into about a 1% loss in market equity value and spill over horizontally to the customer's other suppliers. The paper contributes to [[Production Networks]], [[Supply Chain Finance]], [[Firm-level Shocks and Aggregate Fluctuations]], and [[Input Specificity]].

## 3. Research Question
Do firm-level idiosyncratic shocks propagate through supplier-customer networks, or are they absorbed because firms can quickly switch suppliers?

More specifically, the paper tests whether propagation is stronger when the shocked supplier produces specific inputs that are harder to replace. The key causal channel is supplier disruption -> customer input shortage -> customer output decline -> valuation loss and spillovers to other suppliers.

## 4. Core Mechanism
Use a chain that can be memorized for comps:

```text
Natural disaster hits supplier headquarters county
-> supplier output and sales fall temporarily
-> customer cannot quickly replace supplier if input is specific
-> customer reduces production and sales
-> lost sales reduce market value and lower demand for other suppliers
```

## 5. Main Findings
1. Suppliers directly hit by natural disasters experience temporary sales-growth declines, validating disasters as real firm-level shocks.
2. Customers of shocked suppliers experience about a 2 to 3 percentage point drop in sales growth, which is large relative to average customer sales growth.
3. Propagation is concentrated among specific suppliers, proxied by differentiated goods, R&D intensity, and patents.
4. The losses are not merely delays: there is no clear overshooting afterward, and customer equity value falls by roughly 1%.
5. Shocks also propagate horizontally to the customer's other suppliers, especially when the original shocked supplier is specific.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Firm-quarter |
| Sample period | 1978 to 2013 |
| Main dataset | Compustat Segment supplier-customer links, Compustat financials, SHELDUS natural disasters, Infogroup establishments, CRSP returns |
| Key variables | Sales growth, COGS growth, supplier shock, direct firm shock, supplier specificity, number of suppliers |
| Treatment or shock | At least one supplier headquartered in a county hit by a major natural disaster |
| Outcome variables | Customer sales growth, customer COGS growth, cumulative abnormal returns, other suppliers' sales growth |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between supplier distress and customer sales is not causal because suppliers and customers are endogenously matched. Weak customers may choose weak suppliers, suppliers may be hit by demand shocks correlated with customer demand, or both firms may be exposed to the same regional or industry shock. There is also selection because Compustat Segment mainly observes suppliers for which a customer accounts for more than 10% of sales, and both customer and supplier are often public firms. Measurement error is also possible because natural disasters are assigned using headquarters counties, while production may occur elsewhere.

### Identification Approach
- Natural experiment: Major natural disasters hitting suppliers' headquarters counties.
- Instrument: No formal IV. Disasters act as an exogenous shock source.
- Difference in differences: Compare customer sales growth when a supplier is hit versus when no supplier is hit, using firm and time fixed effects.
- Event study: Customer stock returns around the first day of a supplier natural disaster.
- Fixed effects: Firm fixed effects, year-quarter fixed effects, fiscal-quarter fixed effects, and in some specifications state-year and industry-year fixed effects.
- Matching: Not central in the baseline design.
- Placebo tests: Inactive supplier-customer links are used to test whether effects are driven by common demand shocks rather than active production links.
- Robustness: Controls for direct firm disasters, establishment-level exposure, distance between supplier and customer, heterogeneous trends, size weighting, eventually treated firms only, local relationships, and alternative Capital IQ network data.
- Alternative source of variation: Input specificity proxies based on Rauch differentiated goods, R&D intensity, and patenting.

### Is the Identification Convincing?
- Strength: The natural disaster shock is plausibly exogenous to customer fundamentals, and the active-link test is especially powerful against common demand-shock stories.
- Weakness: Headquarters location is an imperfect proxy for production exposure, and observed supplier-customer links are selected toward major customers of public suppliers.
- Referee concern: Natural disasters may create regional demand shocks, affect the customer's own facilities, or hit unobserved linked firms, which could contaminate the exclusion restriction.

## 8. Main Regression or Model

```text
SalesGrowth_i,t-4,t =
  beta1 HitsOneSupplier_i,t-4
+ beta2 DisasterHitsFirm_i,t-4
+ Controls_i,t
+ Firm FE
+ Year-Quarter FE
+ epsilon_i,t
```

The dependent variable is customer sales growth from the same quarter in the previous year. `HitsOneSupplier` equals one when at least one supplier is located in a county hit by a major natural disaster in the same quarter of the previous year. The coefficient `beta1` is the main estimate: the effect of a supplier disruption on customer output.

Input specificity version:

```text
SalesGrowth_i,t-4,t =
  betaS HitsSpecificSupplier_i,t-4
+ betaN HitsNonspecificSupplier_i,t-4
+ beta2 DisasterHitsFirm_i,t-4
+ Controls_i,t
+ Firm FE
+ Year-Quarter FE
+ epsilon_i,t
```

`betaS` measures propagation from specific suppliers. `betaN` measures propagation from nonspecific suppliers. The main economic interpretation is that `betaS` is negative and economically large, while `betaN` is small or insignificant, showing that specificity and switching costs drive propagation.

Horizontal propagation version:

```text
SupplierSalesGrowth_i,t-4,t =
  delta DisasterHitsOneCustomersSupplier_i,t-4,t-1
+ Controls_i,t
+ Firm FE
+ Year-Quarter FE
+ epsilon_i,t
```

Here the treated firm is another supplier of the same customer. The coefficient `delta` measures whether a shock to one supplier reduces the sales of the customer's other suppliers through customer production declines.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Production Networks]] by showing that shocks propagate at the firm-to-firm level, not just through sectoral input-output tables.
2. [[Firm-level Shocks and Aggregate Fluctuations]] by giving empirical support to theories where micro shocks can have macro relevance.
3. [[Supply Chain Finance]] by showing that supplier specificity creates real operating risk and market value losses.
4. [[Corporate Policy and Stakeholders]] by linking supplier dependence to risk management, financial flexibility, and distress concerns.

It differs from prior work because it uses repeated natural disasters over 30 years, observes time-varying supplier-customer links, and directly tests the mechanism of input specificity.

## 10. Closely Related Papers
- [[Long and Plosser 1983]]: Theoretical foundation for sectoral linkages and aggregate fluctuations.
- [[Acemoglu Carvalho Ozdaglar and Tahbaz-Salehi 2012]]: Network origins of aggregate fluctuations.
- [[Gabaix 2011]]: Granular origins of aggregate fluctuations from large firms.
- [[Cohen and Frazzini 2008]]: Customer-supplier links and return predictability.
- [[Khwaja and Mian 2008]]: Firm-level propagation of bank liquidity shocks through lending relationships.
- [[Boehm Flaaen and Pandalai-Nayar 2015]]: Supply-chain transmission after the Japanese earthquake.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the literature on production networks and the transmission of firm-level shocks. Discuss how papers establish causality and whether micro shocks can generate aggregate consequences.

How to use this paper:
- Main finding: Supplier-specific shocks reduce customer output, especially when inputs are hard to substitute.
- Data: Compustat Segment supplier-customer links, Compustat firm financials, SHELDUS natural disasters, CRSP returns.
- Identification: Natural disasters provide plausibly exogenous shocks to suppliers, combined with firm and time fixed effects and active-link placebo tests.
- Limitation: Public-firm supplier-customer links are selected, and headquarters-based disaster exposure may mismeasure true production disruptions.
- Connection to other papers: Use with [[Acemoglu Carvalho Ozdaglar and Tahbaz-Salehi 2012]] for theory, [[Gabaix 2011]] for granular shocks, and [[Cohen and Frazzini 2008]] for finance implications of customer-supplier networks.
- Best exam phrase: "Barrot and Sauvagnat turn natural disasters into firm-level supply shocks and show that input specificity makes idiosyncratic shocks propagate through real production networks."

## 12. Hypotheses Inspired by This Paper
H1: Customers with more supplier concentration experience larger output losses after supplier shocks.

H2: Supplier shocks have stronger downstream effects when inputs are specific, customized, patented, or R&D intensive.

H3: Firms with greater financial flexibility, higher inventories, or more diversified supplier bases are less exposed to supplier-disruption shocks.

## 13. Possible Extension or Research Design
- Research question: Do geopolitical shocks to suppliers propagate through global production networks in the same way as natural disasters?
- Hypothesis: EU firms with Russian or sanction-exposed suppliers experience larger post-shock declines in sales, investment, or margins when those suppliers provide specific inputs.
- Data: FactSet Revere supplier-customer links, Orbis or Compustat Global financials, sanctions data, customs or BACI trade data, patent and R&D measures.
- Identification: Difference in differences comparing firms with pre-existing exposed suppliers to similar firms without exposed suppliers, before and after sanctions or conflict escalation.
- Expected result: Stronger negative effects for firms dependent on specific or hard-to-replace inputs, with attenuation for firms holding high inventories or diversified suppliers.
- Contribution: Extends the production-network shock literature from natural disasters to geopolitical and sanctions shocks.

## 14. Critiques

### Major Concern 1
The exclusion restriction may fail if natural disasters affect customer demand, customer facilities, or broader regional supply chains rather than only the supplier's production. The active-link placebo and distance controls help, but they cannot fully eliminate all regional equilibrium channels.

### Major Concern 2
The network is selected because Compustat Segment primarily captures major customers and public firms. This may overrepresent economically important links and underrepresent private or smaller suppliers. The alternative Capital IQ network robustness helps, but the baseline sample is still not the universe of production links.

### Minor Concern
Sales growth mixes quantities and prices. A decline in sales may reflect quantity reductions, price changes, or changes in product mix. Industry-level real output and state-industry GDP robustness reduce this concern.

### Referee Recommendation
Accept, because the paper has a clean shock, strong mechanism tests, multiple robustness checks, and a major contribution to production-network empirics. The main concern is external validity, not internal validity.

## 15. Memory Hooks
- "Natural disasters as supplier shocks."
- "2 to 3 percentage point customer sales decline."
- "Specific inputs are the amplifier."
- "No active link, no propagation."
- "$1 supplier loss leads to about $2.40 customer loss."
- "Vertical to customers, horizontal to other suppliers."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Production Networks]], [[Supply Chain Finance]], [[Firm-level Shocks and Aggregate Fluctuations]], [[Natural Experiments]], or [[Input Specificity]]. The clean exam answer is: "Barrot and Sauvagnat use major natural disasters hitting suppliers as exogenous firm-level supply shocks and show that customers lose 2 to 3 percentage points of sales growth, especially when the supplier produces specific inputs." Use it to argue that production networks do not automatically diversify idiosyncratic shocks because specificity and switching costs can amplify them. In a critique answer, emphasize possible common regional demand shocks and selected public-firm links, but note that the paper is stronger than a standard correlation because it uses plausibly exogenous shocks, firm and time fixed effects, active-link placebos, establishment controls, and specificity-based mechanism tests.