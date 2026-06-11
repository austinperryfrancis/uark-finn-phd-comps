---
type: paper
status: unread
title: "Cross-Subsidization in Conglomerate Firms: Evidence from Government Spending Shocks"
authors: Darren J. Kisgen; Lei Kong
year: 2024
journal: Journal of Financial and Quantitative Analysis
seminar:
field: Corporate Finance
literature: Internal Capital Markets; Conglomerates; Corporate Diversification; Investment
methods: Segment-level panel regressions; continuous difference-in-differences; triple differences; matching; instrumental variables
datasets: Compustat Historical Segments; Compustat Fundamentals Annual; BEA Benchmark Input-Output Accounts; OMB federal spending; County Business Patterns; Compustat customer data
identification: Industry government dependence interacted with lagged aggregate nondefense federal spending, plus segment fixed effects, year fixed effects, matched stand-alone firms, and political-party IV
main_result: Government-dependent segments in conglomerates underreact to positive government spending shocks relative to matched stand-alone firms, while less government-dependent segments inside the same conglomerates invest more when other segments receive positive shocks. This cross-subsidization lowers operating performance and increases the diversification discount.
exam_relevance: high
must_memorize: true
tags:
  - internal-capital-markets
  - conglomerates
  - cross-subsidization
  - diversification-discount
  - investment
  - government-spending
  - DrJandik
  - corporate-finance
created: 2026-06-05
updated: 2026-06-05
---

# Kisgen and Kong 2024

## 1. One-Sentence Takeaway
This paper shows that conglomerates cross-subsidize across segments using industry-level exposure to federal government spending shocks, and the main contribution is direct evidence that internal capital markets can distort investment and destroy value.

## 2. Exam-Ready Abstract
Kisgen and Kong study whether conglomerate internal capital markets allocate resources efficiently across business segments. The setting is U.S. public firms from 1977 to 2016, using Compustat Historical Segments and industry-level exposure to nondefense federal government spending. The key shock is the interaction between an industry's predetermined government dependence and lagged aggregate government spending, which creates variation in segment-level demand. They show that government-dependent stand-alone firms increase investment more after positive shocks than comparable conglomerate segments. Within conglomerates, low government-dependent segments invest more when other segments in the same firm receive positive government spending shocks, consistent with cross-subsidization. This cross-subsidization is associated with weaker operating performance and a larger diversification discount. This paper connects to [[Internal Capital Markets]], [[Corporate Diversification]], [[Investment]], and [[Agency Problems]].

## 3. Research Question
What is the paper trying to answer?

Do conglomerate internal capital markets allocate capital efficiently across segments, or do they cross-subsidize weaker divisions at the expense of stronger ones?

More specifically: the paper tests whether positive demand shocks to government-dependent segments are retained by those segments or redistributed to less government-dependent segments inside the same conglomerate.

## 4. Core Mechanism
Use a chain that can be memorized for comps:

```text
Increase in aggregate nondefense federal government spending
-> industries with higher predetermined government dependence receive stronger demand shocks
-> government-dependent conglomerate segments generate better investment opportunities or cash flow
-> headquarters reallocates some resources to less government-dependent companion segments
-> high-shock segments underinvest relative to stand-alone firms, low-shock segments overinvest, operating performance falls, and the diversification discount increases
```

## 5. Main Findings
1. Government spending shocks are real investment-opportunity shocks: segments in industries with higher government dependence invest more when aggregate government spending rises.
2. Government-dependent conglomerate segments respond less to positive spending shocks than matched stand-alone firms in the same industry, consistent with internal redistribution.
3. Low government-dependent segments invest more when other segments in the same conglomerate are more exposed to government spending shocks, providing direct evidence of cross-subsidization.
4. Cross-subsidization is costly: conglomerate segments experience weaker profitability gains than matched stand-alone firms, and more government-dependent conglomerates trade at larger diversification discounts in high-spending years.
5. The results are robust to alternative government-dependence measures and an IV strategy based on political control of the federal government.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Firm-segment-year, firm-year, and industry-year |
| Sample period | 1977 to 2016 |
| Main dataset | Compustat Historical Segments |
| Other datasets | Compustat Fundamentals Annual, BEA Benchmark Input-Output Accounts, OMB nondefense discretionary federal spending, County Business Patterns, Compustat customer data |
| Key variables | Segment investment, segment ROA, segment Q, OWN_GD, OTHER_GD, FIRM_GD, GOVSPEND, excess value |
| Treatment or shock | Industry government dependence interacted with lagged aggregate nondefense discretionary federal spending scaled by GDP |
| Outcome variables | Segment investment, industry employment growth, segment ROA, matched ΔROA, firm excess value, diversification discount |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between conglomerate status and investment would not be causal because firms endogenously choose whether to diversify. Conglomerates may differ from stand-alone firms in size, governance, growth opportunities, managerial quality, financing constraints, or segment composition. There is also a measurement problem because traditional tests of internal capital markets often rely on Tobin's Q, which may be noisy or endogenous at the segment level. Government spending itself may also respond to macroeconomic conditions that affect investment.

### Identification Approach
- Natural experiment: Uses changes in aggregate federal government spending as demand shocks that matter more for industries with higher predetermined government dependence.
- Instrument: Uses Democratic control of the executive branch and at least one chamber of Congress as an instrument for nondefense discretionary government spending.
- Difference in differences: Compares high versus low government-dependent segments across high versus low government spending periods.
- Triple differences: Compares government-dependent segments in conglomerates versus stand-alone firms as government spending changes.
- Event study: Not central in the provided text.
- Fixed effects: Segment fixed effects, year fixed effects, and in some tests firm-by-year fixed effects and industry fixed effects.
- Matching: Matches conglomerate segments to stand-alone firms in the same 4-digit SIC industry based on prior investment or sales.
- Placebo tests: Not clear from provided text.
- Robustness: Alternative government-dependence measure using Compustat customer data, industry-level employment tests, time-invariant OTHER_GD and FIRM_GD, and IV estimates.
- Alternative source of variation: Political-party instrument for government spending.

### Is the Identification Convincing?
- Strength: The paper improves on standard Q-sensitivity tests by using a more tangible demand shock. The interaction of aggregate spending with predetermined industry dependence makes the shock less likely to be driven by segment-specific investment demand.
- Weakness: Government dependence is partly measured at the industry level, so within-industry firm heterogeneity may be imperfectly captured.
- Referee concern: The political-party IV may violate the exclusion restriction if party control affects investment through taxes, regulation, uncertainty, or macroeconomic policy rather than only through nondefense spending.

## 8. Main Regression or Model

```text
Investment_ijt =
  beta1 OWN_GD_ijt x GOVSPEND_t-1
+ beta2 OWN_GD_ijt
+ beta3 Segment_Q_ijt-1
+ Segment FE
+ Year FE
+ epsilon_ijt
```

This baseline regression asks whether segments in more government-dependent industries invest more when aggregate government spending rises. The coefficient beta1 captures whether spending shocks create stronger investment responses in government-dependent industries.

The main conglomerate comparison is:

```text
Investment_ijt =
  beta1 OWN_GD_ijt x GOVSPEND_t-1 x Industry_Dispersion_jt
+ beta2 OWN_GD_ijt x GOVSPEND_t-1
+ beta3 GOVSPEND_t-1 x Industry_Dispersion_jt
+ beta4 OWN_GD_ijt x Industry_Dispersion_jt
+ Controls
+ Segment FE
+ Year FE
+ epsilon_ijt
```

Here beta1 is the key coefficient. A negative beta1 means that government-dependent segments in more diversified firms respond less to government spending shocks than similar segments in less diversified or stand-alone firms.

The direct cross-subsidization test is:

```text
Investment_ijt =
  beta1 OTHER_GD_ij x GOVSPEND_t-1 x LOW_GD_ij
+ beta2 OTHER_GD_ij x GOVSPEND_t-1
+ beta3 OWN_GD_ijt x GOVSPEND_t-1
+ Controls
+ Segment FE
+ Year FE
+ epsilon_ijt
```

LOW_GD equals 1 when a segment's own government dependence is lower than the government dependence of the other segments in the same firm. The coefficient beta1 carries the main cross-subsidization interpretation: low-exposure segments invest more when high-exposure companion segments receive positive shocks.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Internal Capital Markets]] by providing direct evidence that resources flow across divisions after identifiable segment-level demand shocks.
2. [[Corporate Diversification]] by showing that diversification can impose a value cost through inefficient internal redistribution.
3. [[Investment]] by replacing noisy segment Q with a government spending shock tied to industry demand.
4. [[Agency Problems]] by supporting the corporate socialism view of conglomerate resource allocation.

It differs from prior work because it identifies the mechanism behind lower investment sensitivity in conglomerates. Rather than only showing that conglomerate investment is less Q-sensitive, it shows that shocks to one segment predict investment in other segments.

## 10. Closely Related Papers
- [[Lamont 1997]]: Uses oil price shocks to study cash flow spillovers inside diversified firms.
- [[Shin and Stulz 1998]]: Tests whether internal capital markets allocate investment efficiently across segments.
- [[Rajan Servaes and Zingales 2000]]: Develops the cost-of-diversity argument and links diversity to inefficient investment.
- [[Scharfstein and Stein 2000]]: Provides a theory of divisional rent-seeking and the dark side of internal capital markets.
- [[Ozbas and Scharfstein 2010]]: Provides evidence on inefficient internal capital allocation.
- [[Matvos and Seru 2014]]: Shows internal capital markets can be useful during financial market dislocation.
- [[Kuppuswamy and Villalonga 2016]]: Finds conglomerates may create value during the financial crisis.
- [[Berger and Ofek 1995]]: Establishes the diversification discount using imputed stand-alone values.
- [[Campa and Kedia 2002]]: Argues diversification discounts partly reflect endogenous selection into diversification.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the literature on internal capital markets. Are conglomerates efficient allocators of capital? Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Conglomerates cross-subsidize across segments after government spending shocks, and this appears value-destroying.
- Data: Compustat Historical Segments from 1977 to 2016, BEA input-output measures of government dependence, and aggregate nondefense federal spending.
- Identification: Predetermined industry government dependence interacted with lagged aggregate government spending, plus matched stand-alone firms and triple differences.
- Limitation: Industry-level government dependence may not perfectly measure firm-level government exposure, and political-party IV exclusion is debatable.
- Connection to other papers: Use with [[Lamont 1997]], [[Shin and Stulz 1998]], [[Rajan Servaes and Zingales 2000]], [[Scharfstein and Stein 2000]], and [[Matvos and Seru 2014]].
- Best exam phrase: Kisgen and Kong use government spending shocks as cleaner segment-level investment-opportunity shocks and show that conglomerate headquarters spreads shocks across divisions in a way that looks like inefficient cross-subsidization.

## 12. Hypotheses Inspired by This Paper
H1: Cross-subsidization is stronger in conglomerates with greater dispersion in segment investment opportunities.

H2: Cross-subsidization is weaker when headquarters has stronger governance, more segment-level disclosure, or more performance-sensitive compensation.

H3: The value cost of cross-subsidization is larger when the shocked segment has high marginal returns to capital and the recipient segment has low marginal returns to capital.

## 13. Possible Extension or Research Design
- Research question: Does segment-level AI adoption create internal cross-subsidization inside diversified firms?
- Hypothesis: Segments receiving positive AI productivity shocks subsidize non-AI-intensive companion segments, reducing the treated segment's investment response.
- Data: Segment disclosures, firm-level AI exposure measures, job postings, patents, 10-K text, Compustat segments, and market valuation.
- Identification: Interact predetermined segment AI exposure with a shock to AI technology availability, such as the post-2022 generative AI shock, and compare conglomerate segments to matched stand-alone firms.
- Expected result: High-AI-exposure stand-alone firms invest more than high-AI-exposure conglomerate segments, while low-AI-exposure companion segments inside conglomerates increase investment.
- Contribution: Extends the internal capital markets literature to technology shocks and intangible investment.

## 14. Critiques

### Major Concern 1
The government-dependence measure is primarily industry-level, so it may misclassify firms within the same industry. The paper addresses this with Compustat customer data, but customer disclosure is imperfect and may capture only major customers.

### Major Concern 2
The IV based on Democratic political control may not satisfy the exclusion restriction. Political control could affect investment through taxes, regulation, uncertainty, monetary-fiscal interactions, or sector-specific policy expectations, not only through nondefense federal spending.

### Minor Concern
Segment data are noisy because firms reorganize segments over time and segment reporting rules changed during the sample. The authors apply filters, but segment-level comparability remains a standard concern.

### Referee Recommendation
R&R, leaning accept, because the paper provides a clever shock-based test of cross-subsidization and links it to performance and valuation. The main revision would be to further address the exclusion restriction and show more evidence that the results are not driven by industry-specific political economy or firm-level procurement exposure.

## 15. Memory Hooks
- "Government spending shock beats Q."
- "OWN_GD gets the shock, OTHER_GD reveals the subsidy."
- "High government-dependent segments underreact inside conglomerates."
- "Low government-dependent segments invest when their sibling segments get shocked."
- "Dark side in normal times, insurance value in crisis times."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Internal Capital Markets]], [[Corporate Diversification]], [[Investment]], or [[Difference-in-Differences]]. The clean exam answer is: "Kisgen and Kong use industry exposure to federal government spending as a segment-level demand shock and show that conglomerates redistribute positive shocks across divisions, causing government-dependent segments to underinvest relative to stand-alone firms while less exposed companion segments increase investment." Use it to argue that internal capital markets can destroy value when headquarters engages in corporate socialism rather than winner-picking. In a critique answer, emphasize measurement error in government dependence and the exclusion restriction of the political-party IV, but note that the paper is stronger than a standard correlation because it compares shocked and less-shocked segments across conglomerate and stand-alone organizational forms using fixed effects, matching, and an external demand shock.