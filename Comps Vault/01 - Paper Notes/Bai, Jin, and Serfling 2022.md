---
type: paper
status: unread
title: Management Practices and Mergers and Acquisitions
authors: John (Jianqiu) Bai, Wang Jin, Matthew Serfling
year: 2022
journal: Management Science
seminar:
field: Corporate Finance
literature: Mergers and Acquisitions, Management Practices, Organizational Capital, Productivity
methods: Difference-in-differences in changes, gravity model, OLS, completed versus withdrawn deal comparison, cross-sectional heterogeneity
datasets: U.S. Census MOPS, LBD, ASM, SDC M&A
identification: Establishment ownership changes from 2006 to 2010, management-practice changes from 2005 to 2010, completed versus withdrawn announced deals
main_result: Acquirers with more structured management practices buy less structured establishments, impose more structured practices after acquisition, and these changes are associated with better establishment performance.
exam_relevance: high
must_memorize: true
tags:
  - mergers-and-acquisitions
  - management-practices
  - organizational-capital
  - productivity
  - establishment-data
  - synergies
  - DrJandik
created: 2026-06-05
updated: 2026-06-05
---

# Bai, Jin, and Serfling 2022

## 1. One-Sentence Takeaway
This paper shows that M&A creates value partly by transferring structured management practices from acquirers to target establishments using U.S. Census establishment-level management data, and the main contribution is direct evidence on a concrete operational source of merger synergies.

## 2. Exam-Ready Abstract
Bai, Jin, and Serfling study whether mergers create value by improving the management practices of acquired establishments. The setting is U.S. manufacturing establishments, using the 2010 Management and Organizational Practices Survey, which asks about management practices in both 2005 and 2010, matched to Census ownership changes from the Longitudinal Business Database. They show that firms with more structured management practices are more likely to become acquirers, while establishments with less structured practices are more likely to become targets. In a difference-in-differences design in changes, acquired establishments adopt more structured monitoring, target-setting, and incentive practices relative to nonacquired establishments. The effects are stronger when acquirers have more structured practices, managers have greater decision control, industries are more competitive, and acquirer-target operations are more complementary. Performance improves more when acquired establishments adopt more structured practices, suggesting that management-practice transfer is a source of M&A value creation. This paper connects to [[Mergers and Acquisitions]], [[Organizational Capital]], [[Management Practices]], and [[Productivity]].

## 3. Research Question
What are the sources of value creation in mergers and acquisitions?

More specifically, the paper asks whether acquirers create value by transferring more structured management practices to acquired establishments, and whether this channel improves postacquisition performance.

## 4. Core Mechanism

```text
Acquisition of an establishment
-> new owner has more structured management practices
-> acquirer imposes more formal monitoring, production targets, and incentives
-> target establishment becomes easier to track, control, and integrate
-> workers respond through better effort, selection, and coordination
-> establishment productivity, value added, and profitability improve
```

## 5. Main Findings
1. Firms with more structured management practices are more likely to become acquirers, and establishments with less structured management practices are more likely to be acquired.
2. After acquisition, target establishments adopt more structured management practices. The effect appears in monitoring, production targets, and incentives.
3. Target establishments' management practices converge toward the acquirer's practices after acquisition, including in cosine similarity across the 16 management-practice questions.
4. The effect is stronger when acquirers have high initial management scores, managers have more decision authority, product-market competition is high, and target and acquirer operate in the same industry.
5. Postacquisition performance improvements are larger when acquired establishments adopt more structured management practices, especially for TFP, value added per employee, value added per production hour, and profit margin.

## 6. Data

| Item | Details |
|---|---|
| Unit of observation | Establishment, with some firm-level and acquirer-target pair analyses |
| Sample period | Management practices measured for 2005 and 2010; acquisitions from 2006 to 2010; performance changes from 2005 to 2011 |
| Main dataset | U.S. Census Management and Organizational Practices Survey, Longitudinal Business Database, Annual Survey of Manufacturers, SDC M&A |
| Key variables | Management-practice score, monitoring score, production-target score, incentive score, ownership-change indicator, acquirer management score |
| Treatment or shock | Establishment ownership change through acquisition |
| Outcome variables | Change in management-practice score, convergence to acquirer practices, TFP, value added per employee, value added per production worker hour, profit margin, return on capital |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between acquisition and better management would not be causal because targets and acquirers are selected. Better-managed firms may choose different targets, targets may already be improving before acquisition, and establishments that are easier to improve may be more likely to be sold. Industry shocks, state-level shocks, firm restructuring, and mean reversion could also jointly affect acquisition probability and management-practice changes. The 2005 management data are also recalled in 2010, which creates potential recall bias or ex post rationalization.

### Identification Approach
- Natural experiment: Completed announced acquisitions are compared with withdrawn announced acquisitions, following a Seru-style design.
- Instrument: None.
- Difference in differences: Change in management practices from 2005 to 2010 is compared between acquired and nonacquired establishments.
- Event study: Not a full event study because the MOPS has only 2005 and 2010 management observations. The paper uses acquisition timing, 2006 to 2008 versus 2009 to 2010, as a timing check.
- Fixed effects: Industry and state fixed effects in change regressions; firm fixed effects in target likelihood tests; target-establishment fixed effects in convergence tests.
- Matching: Fuzzy matching of SDC announced targets to Census establishments for completed versus withdrawn deal tests.
- Placebo tests: Tests whether prior management-practice changes predict later acquisition. They do not find evidence consistent with pre-existing trends.
- Robustness: Controls for respondent tenure, recall error in employment, online versus mail survey mode, respondent-position fixed effects, and possible response manipulation.
- Alternative source of variation: Cross-sectional variation in acquirer capability and incentive to impose changes, including high acquirer management score, centralized decision control, industry competition, and same-industry relatedness.

### Is the Identification Convincing?
- Strength: The paper uses rare establishment-level data, directly observes management practices, tracks ownership changes within Census data, and can observe partial acquisitions that standard public-firm M&A data miss.
- Weakness: Acquisition is not random, the main management change is measured only between 2005 and 2010, and the 2005 management practices are recalled in 2010.
- Referee concern: Acquirers may select targets that are already easy to improve, and the performance interaction with management-practice changes is harder to interpret causally because postacquisition practice adoption is itself endogenous.

## 8. Main Regression or Model

```text
Delta MPScore_i =
  beta OwnershipChange_i
+ Gamma Delta Controls_i
+ Psi Controls_i,2005
+ Industry FE
+ State FE
+ epsilon_i
```

This regression asks whether establishments acquired between 2006 and 2010 experience larger increases in management-practice scores from 2005 to 2010 than otherwise similar nonacquired establishments. The coefficient beta is the paper's core difference-in-differences-in-changes estimate.

Performance specification:

```text
Delta Performance_i,2005-2011 =
  beta1 OwnershipChange_i
+ beta2 OwnershipChange_i x Delta MPScore_i,2005-2010
+ beta3 Delta MPScore_i,2005-2010
+ Controls_i
+ Industry FE
+ State FE
+ epsilon_i
```

Here beta2 is the key economic coefficient. It asks whether acquired establishments improve more when they also adopt more structured management practices. A positive beta2 supports the mechanism that management-practice transfer is not just cosmetic but tied to performance gains.

Heterogeneity version:

```text
Delta MPScore_i =
  beta1 OwnershipChange_i
+ beta2 OwnershipChange_i x Heterogeneity_i
+ Controls_i
+ Industry FE
+ State FE
+ epsilon_i
```

Heterogeneity includes high acquirer management score, centralized decision control, low industry HHI, and same-industry acquirer-target pairing. The coefficient beta2 tells whether acquisitions change management practices more when the acquirer has greater ability or incentive to impose operational change.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Mergers and Acquisitions]] by opening the synergy black box and showing a specific source of value creation.
2. [[Organizational Capital]] by treating management practices as transferable organizational capital.
3. [[Management Practices]] and [[Productivity]] by showing that structured practices can be adopted through changes in ownership.

It differs from prior work because it uses direct establishment-level survey measures of management practices rather than indirect proxies such as Tobin's Q, governance indices, or SG&A-based organizational capital.

## 10. Closely Related Papers
- [[Lang et al. 1989]]: High-Q firms acquiring low-Q firms as evidence that better-managed firms create value through acquisitions.
- [[Servaes 1991]]: Tobin's Q and acquisition gains, another indirect proxy for managerial quality.
- [[Maksimovic and Phillips 2001]]: Resource allocation, plant-level productivity, and comparative advantage in asset sales and acquisitions.
- [[Devos, Kadapakkam, and Krishnamurthy 2009]]: Decomposes sources of merger gains such as operating synergies and tax shields.
- [[Bloom and Van Reenen 2007]]: Foundational evidence that structured management practices are linked to firm productivity.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on merger synergies. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: M&A creates value partly through the transfer of structured management practices to acquired establishments.
- Data: Census MOPS plus LBD ownership changes, with establishment-level management practices for 2005 and 2010.
- Identification: Difference-in-differences in changes, controls and fixed effects, pre-trend checks, and completed versus withdrawn announced acquisitions.
- Limitation: Acquisition selection and two-period recalled management-practice data make perfect causal interpretation difficult.
- Connection to other papers: Complements high-Q acquirer papers and organizational-capital papers by directly observing the mechanism.
- Best exam phrase: "Bai, Jin, and Serfling open the M&A synergy black box by showing that better-managed acquirers transfer structured monitoring, targets, and incentives to acquired plants."

## 12. Hypotheses Inspired by This Paper
H1: Acquired establishments experience larger productivity gains when the acquirer-target management-practice gap is larger before acquisition.

H2: The effect of acquisition on management-practice adoption is stronger in competitive industries because competition increases the payoff to efficiency improvements.

H3: Same-industry acquisitions produce faster management-practice convergence because acquirers have more relevant operating knowledge.

## 13. Possible Extension or Research Design
- Research question: Does the transfer of organizational capital through M&A operate similarly outside U.S. manufacturing and among private firms?
- Hypothesis: Acquisitions by firms with higher organizational capital lead to stronger postacquisition improvements in target productivity, especially when targets are operationally related to acquirers.
- Data: Orbis ownership changes, private-firm financials, industry-country ownership histories, and proxies for organizational capital such as management quality surveys, ISO adoption, job-posting text, or process-control language.
- Identification: Difference-in-differences around ownership changes, with target firm fixed effects, country-industry-year fixed effects, and completed versus withdrawn deal comparisons where available.
- Expected result: Targets acquired by high-organizational-capital firms improve margins, labor productivity, and revenue growth more than targets acquired by lower-quality acquirers.
- Contribution: Extends the management-practice transfer mechanism to international private-firm M&A and tests whether organizational capital is portable across institutional settings.

## 14. Critiques

### Major Concern 1
Acquisition selection remains important. Better-managed acquirers may select targets that are easier to improve, and low-management targets may be sold precisely when parent firms expect operational changes.

### Major Concern 2
The MOPS longitudinal component relies on 2010 respondents recalling 2005 practices. This creates possible measurement error, recall bias, or ex post rationalization after acquisition outcomes are known.

### Minor Concern
The sample is U.S. manufacturing establishments, so the mechanism may not generalize cleanly to services, tech, finance, or cross-border acquisitions.

### Referee Recommendation
Accept, because the paper uses rare microdata to directly observe a plausible M&A synergy mechanism. The main caveat is that acquisition is not randomly assigned, but the completed versus withdrawn deal test, pre-trend checks, and respondent-bias robustness make the evidence much stronger than a standard correlation.

## 15. Memory Hooks
- "Better managers buy worse-managed plants."
- "M&A synergy black box equals management-practice transfer."
- "Monitoring, targets, incentives."
- "MOPS plus LBD lets them track plants across owners."
- "Completed versus withdrawn deals helps with selection."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Mergers and Acquisitions]], [[Organizational Capital]], [[Management Practices]], or [[Difference-in-Differences]]. The clean exam answer is: "Bai, Jin, and Serfling use U.S. Census establishment-level management data matched to ownership changes and show that better-managed acquirers buy less structured establishments, impose more structured management practices, and realize performance improvements." Use it to argue that M&A synergies can come from portable organizational capital rather than only market power, tax shields, or financial restructuring. In a critique answer, emphasize acquisition selection and recalled survey data, but note that the paper is stronger than a standard correlation because it observes the mechanism directly, uses establishment-level changes, checks for pre-trends, and compares completed with withdrawn announced deals.