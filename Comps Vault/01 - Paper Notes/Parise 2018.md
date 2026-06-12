---
type: paper
status: unread
title: "Threat of Entry and Debt Maturity: Evidence from Airlines"
authors: Gianpaolo Parise
year: 2018
journal: Journal of Financial Economics
professor: DrJandik
seminar: null
jandik_paper_number: 10
jandik_week: 3
jandik_topic: 'Capital structure: bankruptcy, product markets, debt ownership, and debt maturity'
jandik_done: true
field: Corporate Finance
literature:
  - "[[Capital Structure]]"
  - Debt Maturity
  - Product Market Competition
  - Rollover Risk
methods:
  - panel regressions
  - route-level threat measure
  - firm fixed effects
  - year fixed effects
  - debt issuance analysis
datasets:
  - U.S. DOT T-100 Domestic Market
  - "[[Compustat]]"
  - Form 41
  - Mergent
  - "[[DealScan]]"
  - O&D Survey
identification: Predictable low-cost carrier route expansion through second-endpoint airport entry
main_result: Incumbent airlines lengthen debt maturity when exposed to entry threats from low-cost competitors, without significantly changing leverage.
exam_relevance: high
must_memorize: true
tags:
  - capital-structure
  - debt-maturity
  - rollover-risk
  - product-market-competition
  - airlines
  - threat-of-entry
created: 2026-06-12
updated: 2026-06-12
---

# Parise 2018

## 1. One-Sentence Takeaway
This paper shows that incumbent airlines lengthen debt maturity when low-cost competitors are likely to enter their routes using predictable route-network expansion as variation, and the main contribution is to show that firms adjust debt structure before competitive shocks to reduce rollover risk.

## 2. Exam-Ready Abstract
Parise studies whether firms adjust financial structure in anticipation of tougher product market competition. The setting is U.S. domestic airlines from 1990 to 2014, where low-cost carrier expansion creates observable threats to incumbent routes. A route is treated as threatened when a low-cost carrier enters the second endpoint airport but has not yet entered the route itself, which sharply raises the probability of future route entry. The main firm-level treatment is the passenger-weighted share of an incumbent airline's routes that are threatened. The paper finds that a one standard deviation increase in threat of entry increases the share of long-term debt by about 6 percentage points, roughly a 10% increase from the baseline, but has no significant effect on leverage. The effect is stronger for speculative-grade and financially constrained airlines, consistent with a rollover-risk channel. This paper connects [[Capital Structure]], [[Debt Maturity]], [[Financial Flexibility]], [[Product Market Competition]], and [[Rollover Risk]].

## 3. Research Question
Do firms change their debt maturity structure before expected product market competition increases?

More specifically: do incumbent airlines exposed to likely entry by low-cost competitors lengthen debt maturity to reduce rollover risk, and is the effect strongest among firms most exposed to refinancing frictions?

## 4. Core Mechanism

```text
Low-cost carrier enters the second endpoint airport of a route
-> probability of future route entry rises sharply
-> expected future fares, margins, and cash flows decline
-> incumbent anticipates worse refinancing conditions
-> incumbent lengthens debt maturity before entry
-> rollover risk falls, while leverage remains mostly unchanged
```

## 5. Main Findings
1. Threatened airlines increase debt maturity. A one standard deviation increase in threat of entry is associated with a 6.0 percentage point increase in the proportion of long-term debt, about 10% relative to the baseline.
2. Threat of entry does not significantly reduce book leverage, suggesting firms adjust debt composition more flexibly than debt levels.
3. The response is stronger for financially constrained and speculative-grade airlines, consistent with rollover risk rather than a generic capital structure story.
4. Debt issuance evidence supports the mechanism: threatened airlines issue debt with longer maturity, especially through loans.
5. Entry threats are economically meaningful because actual low-cost carrier entry lowers route fares by about 7.3%.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Mainly airline-year; route-year for threat construction; debt-issue level for issuance analysis |
| Sample period | 1990 to 2014 for flight and airline data; main regression sample 1991 to 2014 |
| Main dataset | U.S. DOT T-100 Domestic Market, Compustat North America, Form 41, Mergent, Dealscan |
| Key variables | Debt maturity, threat of entry, leverage, long-term debt issuance, Maturity5, investment |
| Treatment or shock | Passenger-weighted share of incumbent routes threatened by low-cost carrier second-endpoint airport entry |
| Outcome variables | Debt maturity, book leverage, long-term debt issuance, issue maturity, future investment |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between competition and debt maturity would not be causal because airlines with certain financial policies may choose routes that are more or less exposed to low-cost carrier entry. Omitted demand shocks could attract low-cost carriers and also affect incumbent financing. Reverse causality is possible if low-cost carriers strategically enter markets where incumbents appear financially weak. There is also equilibrium sorting: route networks, financial structure, and competitive exposure are jointly determined over time.

### Identification Approach
- Natural experiment: Predictable low-cost carrier network expansion creates quasi-exogenous variation in threat at the route level.
- Instrument: No formal instrument.
- Difference in differences: Not a standard DiD, but the firm-year panel uses within-airline variation in exposure to threatened routes.
- Event study: Figure 4 shows average debt maturity around high-threat episodes.
- Fixed effects: Airline fixed effects and year fixed effects.
- Matching: Not central in the main design.
- Placebo tests: Simulated maturity choices show the result is unlikely to arise mechanically.
- Robustness: Controls for actual entry, recent entry, recession years, ticket prices, expected demand, rural routes, and Acela train threat.
- Alternative source of variation: Acela Express introduction affects airlines exposed to routes where high-speed rail becomes a substitute.

### Is the Identification Convincing?
- Strength: The second-endpoint entry measure is intuitive, observable to incumbents, and strongly predicts actual route entry.
- Weakness: Low-cost carriers may still enter second endpoints based on anticipated demand or incumbent weakness.
- Referee concern: The threat variable might proxy for demand growth, route quality, incumbent distress, or actual competition rather than expected future competition.

## 8. Main Regression or Model

```text
DebtMaturity_it =
  beta ThreatOfEntry_it
+ Controls_it
+ Airline FE
+ Year FE
+ epsilon_it
```

The coefficient beta measures whether airline i lengthens debt maturity in year t when a larger passenger-weighted share of its route network is exposed to likely entry by low-cost competitors.

```text
DebtMaturity_it =
  beta1 ThreatOfEntry_it
+ beta2 ThreatOfEntry_it x RolloverRiskProxy_it
+ Controls_it
+ Airline FE
+ Year FE
+ epsilon_it
```

The interaction terms test whether the debt maturity response is stronger for airlines with higher exposure to rollover risk. Rollover risk is proxied by speculative-grade debt status and financial constraints using the SA index. The main economic interpretation is that beta2 should be positive for financially constrained firms and negative for investment-grade firms.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Capital Structure]] by showing that firms adjust debt composition even when leverage is sticky.
2. [[Debt Maturity]] by identifying competitive threats as a determinant of maturity choice.
3. [[Product Market Competition]] by showing that firms respond financially before actual entry occurs.
4. [[Rollover Risk]] by providing empirical support for theories where firms lengthen debt maturity before bad news arrives.

It differs from prior work because it focuses on expected competition, not just realized competition, and uses route-level airline networks to construct a firm-level threat measure.

## 10. Closely Related Papers
- [[Goolsbee and Syverson 2008]]: Uses Southwest second-endpoint entry to study incumbent price responses to threat of entry.
- [[Brunnermeier and Yogo 2009]]: Theory of maturity choice and rollover risk.
- [[Diamond 1991]]: Debt maturity and borrower quality.
- [[Almeida et al. 2012]]: Debt maturity and investment during refinancing shocks.
- [[Rauh and Sufi 2010]]: Heterogeneity in debt structure beyond leverage.
- [[Custódio, Ferreira, and Laureano 2013]]: Corporate debt maturity trends.
- [[Harford, Klasa, and Maxwell 2014]]: Refinancing risk and maturity structure.
- [[Bolton and Scharfstein 1990]]: Deep pockets, predation, and financial constraints.
- [[Zingales 1998]]: Leverage and survival in competitive environments.
- [[Frésard and Valta 2016]]: Competitive threats and corporate policy.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on product market competition and corporate financial policy. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Expected entry by low-cost competitors causes airlines to extend debt maturity.
- Data: U.S. airline route networks, DOT flight data, Compustat financials, Mergent bonds, Dealscan loans.
- Identification: Low-cost carrier second-endpoint airport entry predicts future route entry and creates firm-level variation in competitive threat.
- Limitation: Low-cost carrier expansion may still be correlated with anticipated demand or route quality.
- Connection to other papers: Complements Goolsbee and Syverson on price responses and extends rollover-risk theories into empirical corporate finance.
- Best exam phrase: "Parise 2018 shows that firms do not only adjust prices when competition is expected, they also adjust the maturity structure of liabilities to avoid refinancing in bad states."

## 12. Hypotheses Inspired by This Paper
H1: Firms exposed to credible future product market competition lengthen debt maturity before competition materializes.
H2: The maturity response is stronger for firms with greater rollover risk, lower credit quality, or tighter financing constraints.
H3: Firms adjust debt maturity more than leverage because debt composition is more flexible than total capital structure.
H4: The real effects of entry threats are muted when firms can preemptively reduce rollover risk.
H5: Competitive threats should affect loan maturity more strongly than bond maturity when private lenders can coordinate and monitor more effectively.

## 13. Possible Extension or Research Design
- Research question: Do firms exposed to foreign import competition adjust debt maturity before tariff reductions or trade shocks?
- Hypothesis: Firms facing predictable future import competition lengthen debt maturity, especially if financially constrained.
- Data: Compustat, Capital IQ debt structure, Dealscan, Mergent, import penetration by industry, tariff schedules, product-level trade data.
- Identification: Use plausibly exogenous tariff phase-downs or scheduled trade liberalization as anticipated competition shocks.
- Expected result: Firms with greater exposure to future import competition extend debt maturity without materially lowering leverage.
- Contribution: Generalizes Parise beyond airlines and links [[Trade Shocks]] to [[Debt Maturity]] and [[Financial Flexibility]].

## 14. Critiques

### Major Concern 1
Low-cost carrier second-endpoint entry may not be exogenous. It may reflect unobserved expected demand growth, route profitability, airport-level changes, or weakness of incumbents.

### Major Concern 2
The sample is small. The main Compustat sample has 239 observations, which raises concerns about statistical power, external validity, and sensitivity to influential airlines.

### Minor Concern
Debt maturity is measured from accounting data as the fraction of debt maturing in more than three years. This is standard, but it may miss lease obligations, unobserved private debt, or finer maturity timing.

### Referee Recommendation
R&R / Accept, because the paper has a clean and memorable setting, strong economic mechanism, and many robustness checks, but identification still depends on whether low-cost carrier endpoint expansion is plausibly unrelated to omitted determinants of incumbent debt maturity.

## 15. Memory Hooks
- "Southwest at both endpoints means the route is threatened."
- "Threatened airlines buy time by lengthening debt maturity."
- "Competition shock affects maturity, not leverage."
- "The effect is strongest for speculative-grade and financially constrained airlines."
- "7.3% fare drop from low-cost entry versus thin airline margins."
- "Figure 3: IAD-CLE route becomes threatened when Southwest enters Dulles."
- "Figure 4: debt maturity rises around high-threat episodes."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Capital Structure]], [[Debt Maturity]], [[Product Market Competition]], [[Financial Flexibility]], [[Rollover Risk]], or [[Airline Industry Identification]]. The clean exam answer is: "Parise 2018 uses low-cost carrier second-endpoint airport entry as a measure of expected route-level competition and shows that incumbent airlines lengthen debt maturity before actual entry occurs." Use it to argue that firms manage the structure of liabilities, not just leverage, in anticipation of real shocks. In a critique answer, emphasize that second-endpoint entry may still reflect anticipated demand or route quality, but note that the paper is stronger than a standard correlation because the threat measure is built from route-network expansion, predicts future entry, varies across firms within years, and survives controls for actual entry, prices, demand, rural routes, recessions, and an Acela placebo-style alternative.
