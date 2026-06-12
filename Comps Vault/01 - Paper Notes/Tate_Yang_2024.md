---
type: paper
status: unread
title: 'The Human Factor in Acquisitions: Cross-industry Labor Mobility and Corporate Diversification'
authors: Geoffrey Tate; Liu Yang
year: 2024
journal: Review of Financial Studies
professor: DrJandik
seminar: null
jandik_paper_number: 32
jandik_week: 8
jandik_topic: Internal capital markets and diversification
jandik_done: true
field: Corporate Finance
literature:
- '[[Internal Capital Markets]]'
- '[[Mergers and Acquisitions]]'
- '[[Labor and Finance]]'
- Internal Labor Markets
methods:
- OLS
- event study
- worker-firm matched data
- linear probability model
- triple interaction
datasets:
- U.S. Census LBD
- LEHD
- Census Business Register/SSEL
- '[[SDC]]'
- '[[CRSP]]'
- Compustat Segment
- BEA Input-Output tables
- Starr noncompete index
identification: Cross-industry labor mobility predicts diversifying acquisitions; postdeal performance tests use deal controls and cross-state variation in noncompete enforceability
main_result: Diversifying acquisitions are more common, more productive, less divested, and involve more high-skill worker retention and internal transfers when acquirer and target industries have high human capital transferability.
exam_relevance: high
must_memorize: true
tags:
- corporate-finance
- mergers-and-acquisitions
- diversification
- labor-finance
- internal-labor-markets
- human-capital
created: 2026-06-05
updated: 2026-06-05
---

# Tate and Yang 2024

## 1. One-Sentence Takeaway
This paper shows that firms diversify into industries where worker skills transfer more easily using Census worker-firm matched data on cross-industry labor flows, and the main contribution is to recast corporate diversification as potentially value-creating through [[Internal Labor Markets]] rather than only as an agency problem.

## 2. Exam-Ready Abstract
Tate and Yang ask whether transferable human capital helps determine firm boundaries in diversifying acquisitions. They construct a Human Capital Transferability index from LEHD job-to-job flows across Fama-French 49 industries and link it to acquisitions identified in the Census Longitudinal Business Database. Firms are more likely to make diversifying acquisitions into industries with high worker mobility from their existing industries, especially when the mobility measure is based on high-wage workers. High-HCT diversifying deals have larger postdeal labor productivity gains, roughly 18 percentage points using all workers and about 30 percentage points using high-skill workers. To strengthen identification, they show that high-HCT deals perform especially well when acquirers are located in states with stricter noncompete enforcement, where external hiring frictions make internal labor markets more valuable. Worker-level evidence supports the mechanism: acquirers retain more high-skill target workers and move more workers across industries inside the merged firm. This connects [[Corporate Diversification]], [[Mergers and Acquisitions]], [[Internal Labor Markets]], and [[Labor and Finance]].

## 3. Research Question
What role does human capital transferability play in firms' decisions to diversify through acquisitions?

More specifically, the paper tests whether firms choose target industries that use similar worker skills, whether those deals create value, and whether value creation operates through internal worker retention and redeployment.

## 4. Core Mechanism

```text
High cross-industry human capital transferability
-> workers can be moved across divisions with lower skill mismatch costs
-> diversified firm has a stronger internal labor market
-> firm can retain scarce high-skill workers and redeploy labor after shocks
-> higher productivity, higher announcement returns, lower divestiture risk
```

Key intuition: if workers can move between industries without losing too much productivity, diversification creates an option to reallocate human capital internally.

## 5. Main Findings
1. Diversifying acquisitions are more frequent between industry pairs with high Human Capital Transferability, measured using prior cross-industry job-to-job flows.
2. High-HCT diversifying deals generate larger postdeal labor productivity gains, especially when HCT is measured using high-wage workers.
3. The effect is stronger when acquirers operate in strict noncompete states, consistent with internal labor markets becoming more valuable when external hiring is costly.
4. High-HCT deals have higher combined announcement returns in the SDC public-firm sample.
5. At the worker level, high-HCT deals retain more high-skill target workers and are more likely to transfer workers to other industries inside the merged firm.
6. Existing diversified firms are more likely to jointly operate industries with high HCT, suggesting the mechanism matters for firm scope beyond merger events.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Industry-pair-year for acquisition frequency; deal for productivity and returns; worker-deal for retention and internal mobility |
| Sample period | Main Census acquisition sample: 1995 to 2007; HCT built using worker moves beginning in 1990; SDC sample: 1994 to 2008 |
| Main dataset | U.S. Census LBD for acquisitions and establishments; LEHD for worker-firm matched data; Census Business Register/SSEL for sales; SDC and CRSP for announcement returns |
| Key variables | Human Capital Transferability index, diversifying acquisition indicator, high-HCT indicator, sales per employee, sales per payroll, retention, internal worker movement |
| Treatment or shock | High transferability between acquirer and target industries; stronger noncompete enforcement as variation in external labor market frictions |
| Outcome variables | Acquisition intensity, labor productivity change, announcement CARs, worker retention, worker movement across industries inside the merged firm, subsequent divestiture |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between HCT and acquisition outcomes is not causal because firms may select into high-HCT deals for unobserved reasons. High-HCT industries may also have better growth opportunities, stronger product-market complementarities, better asset overlap, or more attractive acquisition targets. Worker flows may reflect external labor market conditions rather than true skill transferability. At the deal level, acquirers may choose both target industries and target locations strategically, so target-side legal environments are endogenous.

### Identification Approach
- Natural experiment: Cross-state variation in noncompete enforceability changes the value of internal labor markets by raising external hiring frictions.
- Instrument: No formal instrument.
- Difference in differences: Not a standard DiD. The closest design is a triple interaction of diversifying deal, high HCT, and high noncompete enforceability.
- Event study: Postdeal labor productivity is measured over a three-year event window from t-1 to t+1.
- Fixed effects: Industry-pair acquisition tests include acquirer industry-year fixed effects and target industry fixed effects. Worker-level models include year, state, and target industry fixed effects.
- Matching: Not central to the design.
- Placebo tests: Robustness includes product-market relatedness, asset overlap, customer and supplier overlap, occupation overlap, industry-pair fixed effects, alternative HCT construction, and excluding highly input-output related industry pairs.
- Robustness: Results hold for high-skill HCT, sales per payroll, firm-count acquisition intensity, longer productivity windows, divestiture hazards, and public-firm announcement returns.
- Alternative source of variation: Strict noncompete states create stronger predicted productivity gains from high-HCT deals.

### Is the Identification Convincing?
- Strength: The mechanism is supported at three levels: industry-pair acquisition choices, deal-level productivity, and worker-level retention and movement.
- Weakness: HCT is not randomly assigned. Cross-industry labor flows may proxy for broader industry relatedness or unobserved demand shocks.
- Referee concern: Strict noncompete states may differ systematically in business environment, firm types, or industry composition, so the noncompete interaction may not isolate labor-market frictions perfectly.

## 8. Main Regression or Model

Industry-pair acquisition frequency:

```text
Y_ijt =
  alpha
+ beta HCT_ij,t-1
+ Controls_ijt
+ Acquirer industry-year FE
+ Target industry FE
+ epsilon_ijt
```

Here, Y_ijt is the intensity with which acquirers in industry i diversify into industry j in year t, measured by target employment or number of firms. The key coefficient is beta, which tests whether industries with greater worker-skill transferability are more likely to be combined through diversifying acquisitions.

Deal-level productivity:

```text
Delta Productivity_i =
  alpha
+ beta1 Divers_i
+ beta2 Divers_i x High_HCT_i,t-1
+ Controls_i,t-1
+ Year FE
+ epsilon_i
```

beta1 compares low-HCT diversifying deals to within-industry deals. beta2 is the main coefficient: it measures whether high-HCT diversifying deals outperform other diversifying deals.

Noncompete heterogeneity:

```text
Delta Productivity_i =
  alpha
+ beta1 Divers_i
+ beta2 Divers_i x High_HCT_i
+ beta3 Noncompete_i
+ beta4 Divers_i x Noncompete_i
+ beta5 Divers_i x High_HCT_i x Noncompete_i
+ Controls_i
+ Year FE
+ epsilon_i
```

beta5 carries the main identification interpretation. It tests whether the high-HCT productivity premium is larger when the acquirer faces stricter external labor market frictions.

Worker retention:

```text
Retain_ij =
  alpha
+ beta1 Divers_i x Low_HCT_i
+ beta2 Divers_i x High_HCT_i
+ beta3 Skill_j
+ beta4 Skill_j x Divers_i x Low_HCT_i
+ beta5 Skill_j x Divers_i x High_HCT_i
+ Controls_ij
+ Year FE
+ State FE
+ Target industry FE
+ epsilon_ij
```

beta5 tests whether skilled target workers are more likely to be retained after high-HCT diversifying deals.

Worker movement:

```text
Move_ij =
  alpha
+ beta High_HCT_i
+ Controls_ij
+ Year FE
+ State FE
+ Target industry FE
+ epsilon_ij
```

beta tests whether retained target workers are more likely to move into a different acquirer industry after high-HCT deals.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Corporate Diversification]] by showing diversification can create value through internal labor markets, not only destroy value through agency problems.
2. [[Mergers and Acquisitions]] by identifying human capital complementarities as a determinant of target-industry choice and deal performance.
3. [[Labor and Finance]] by linking worker mobility, noncompetes, skill scarcity, and firm boundaries.
4. [[Theory of the Firm]] by treating human capital transferability as a determinant of organizational scope.
5. [[Internal Labor Markets]] by showing that internal redeployment is not just a feature of existing conglomerates but a motive for acquisitions.

It differs from prior work because it measures relatedness using actual worker flows rather than product-market links, occupation overlap, SIC codes, or managerial industry experience.

## 10. Closely Related Papers
- [[Tate and Yang 2015]]: Shows diversified firms use internal labor markets to move workers toward better opportunities. This paper explains why firms choose to diversify in the first place.
- [[Stein 1997]]: Internal capital markets create value by reallocating capital. Tate and Yang provide the labor-market analogue.
- [[Ahern and Harford 2014]]: Product-market links predict merger waves. Tate and Yang focus on input-market links through human capital.
- [[Rhodes-Kropf and Robinson 2008]]: Merger matching and asset complementarities. Tate and Yang extend the complementarities logic to worker skills.
- [[Ouimet and Zarutskie 2020]]: Acquiring labor focuses on scale and labor acquisition. Tate and Yang focus on scope and internal redeployment.
- [[Lee Mauer and Xu 2018]]: Human capital relatedness and M&A, but emphasizes redundancy and employment reductions rather than productivity-improving reallocation.
- [[Berger and Ofek 1995]]: Classic diversification discount paper. Tate and Yang provide a counterpoint showing a channel through which diversification can create value.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on corporate diversification. Discuss whether diversification destroys value and how papers establish causality.

How to use this paper:
- Main finding: Diversification can create value when industries share transferable human capital.
- Data: Census LBD and LEHD worker-firm matched data, plus SDC and CRSP for public-firm returns.
- Identification: HCT from prior external job flows, fixed effects and controls, plus noncompete enforcement as variation in external labor market frictions.
- Limitation: HCT is still an endogenous industry-pair characteristic and may correlate with unobserved complementarities.
- Connection to other papers: Pair with [[Berger and Ofek 1995]] for the diversification discount, [[Stein 1997]] for internal capital markets, and [[Tate and Yang 2015]] for internal labor markets.
- Best exam phrase: "Tate and Yang reinterpret diversification as an internal labor market synergy: unrelated product markets may still be related labor markets."

## 12. Hypotheses Inspired by This Paper
H1: Diversifying acquisitions are more likely between industries with high preexisting cross-industry worker mobility.

H2: The productivity gains from diversifying acquisitions are larger when acquirer and target industries share transferable high-skill labor.

H3: The value of high-HCT diversification is increasing in external labor market frictions, such as strict noncompete enforcement or local skill scarcity.

H4: High-HCT deals should retain more skilled workers and shift more workers across industries inside the merged firm.

H5: If human capital transferability is a true firm-boundary determinant, diversified firms should be more likely to contain high-HCT industry pairs even outside M&A event windows.

## 13. Possible Extension or Research Design
- Research question: Does generative AI change the value of human capital transferability in acquisitions?
- Hypothesis: AI adoption reduces the cost of transferring knowledge across some industries, increasing the value of diversification into industries with complementary analytical or technical labor.
- Data: SDC or Refinitiv M&A deals, Burning Glass job postings, LinkedIn worker histories, patent or AI exposure measures, Compustat segment data, and earnings-call AI exposure.
- Identification: Compare acquisition behavior before and after the release of major generative AI tools across industries with high versus low AI task exposure. Use industry-pair worker mobility and AI-complementarity as cross-sectional heterogeneity.
- Expected result: Firms in high-AI-exposure industries are more likely to acquire targets in industries with transferable technical labor, and those deals have stronger productivity or innovation outcomes.
- Contribution: Extends [[Labor and Finance]] and [[Corporate Diversification]] by studying how technology changes the boundaries of human-capital-related firms.

## 14. Critiques

### Major Concern 1
The HCT index may capture unobserved industry relatedness rather than transferable human capital. Industries with more worker flows may also have stronger product links, common technologies, similar customers, or common local labor markets. The paper addresses this with input-output controls, asset overlap, customer and supplier overlap, occupation overlap, industry fixed effects, and alternative HCT measures, but residual relatedness remains a concern.

### Major Concern 2
The noncompete strategy strengthens the causal story but is not a clean natural experiment. States with strict noncompete enforcement may differ in firm composition, industry mix, growth prospects, or legal environment. The authors avoid target-state variation because target location is chosen endogenously, but acquirer location may still be correlated with long-run firm strategy.

### Minor Concern
The paper uses broad Fama-French 49 industries. This reduces measurement error in product-market classification, but it may hide more granular skill transferability or within-industry heterogeneity.

### Referee Recommendation
Accept, because the paper combines a clear mechanism, novel worker-flow measurement, deal-level outcomes, worker-level evidence, and a plausible external-friction test. The identification is not perfect, but the triangulation across outcomes makes the contribution strong.

## 15. Memory Hooks
- "Unrelated products, related workers."
- HCT equals prior job-to-job flows across industries.
- High-skill HCT matters most because scarce skills make internal redeployment more valuable.
- Noncompetes make internal labor markets more valuable by raising external hiring costs.
- The worker-level smoking gun is retention plus cross-industry movement inside the merged firm.
- This is the labor-market version of Stein's internal capital market logic.

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Corporate Diversification]], [[Mergers and Acquisitions]], [[Internal Labor Markets]], [[Labor and Finance]], or [[Theory of the Firm]]. The clean exam answer is: "Tate and Yang use Census worker-firm matched data to construct industry-pair human capital transferability from job-to-job flows and show that firms diversify into industries where labor can be redeployed more easily." Use it to argue that diversification is not necessarily value-destroying, because product-market unrelatedness can coexist with labor-market relatedness. In a critique answer, emphasize that HCT may proxy for broader industry complementarities, but note that the paper is stronger than a standard correlation because it shows the same mechanism in acquisition choices, productivity, announcement returns, divestitures, worker retention, worker movement, and noncompete heterogeneity.
