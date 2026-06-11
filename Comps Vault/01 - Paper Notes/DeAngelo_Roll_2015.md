---
type: paper
status: unread
title: How Stable Are Corporate Capital Structures?
authors: Harry DeAngelo and Richard Roll
year: 2015
journal: Journal of Finance
seminar:
field: Corporate Finance
literature: Capital Structure
methods: Long-horizon panel analysis, variance decomposition, cross-sectional persistence tests, simulations
datasets: CRSP/Compustat, hand-collected DJIA annual report data, Moody's manuals
identification: Descriptive long-horizon evidence, not causal identification
main_result: Corporate leverage is much less stable than prior fixed-effect evidence suggests. Leverage stability is temporary, mostly occurs at low leverage, and credible target leverage models must allow wide time variation.
exam_relevance: high
must_memorize: true
tags:
  - capital-structure
  - leverage
  - target-leverage
  - financial-flexibility
  - corporate-finance
  - DrJandik
created: 2026-06-03
updated: 2026-06-03
---

# DeAngelo and Roll 2015

## 1. One-Sentence Takeaway
This paper shows that corporate capital structures are usually unstable over long horizons using long-run CRSP/Compustat and hand-collected leverage data, and the main contribution is to challenge the view that firm leverage is highly persistent because firm fixed effects explain much of leverage variation.

## 2. Exam-Ready Abstract
DeAngelo and Roll ask whether corporate capital structures are actually stable over long horizons or whether prior evidence of stability is an artifact of empirical design. They study U.S. industrial firms using CRSP/Compustat data from 1950 to 2008, with special attention to firms listed for at least 20 years and a constant-composition sample, plus hand-collected long-run data for 24 DJIA firms. The paper shows that leverage cross-sections more than a few years apart become increasingly dissimilar, with firms moving substantially across leverage quartiles over time. Stable leverage regimes exist, but they are uncommon, temporary, and concentrated among low-leverage firms. The paper also shows that firm fixed effects do not prove leverage stability because they capture time-series average differences across firms, while firm-time interactions reveal substantial firm-specific changes over time. Simulations suggest that credible target leverage models must allow either time-varying targets, flexible target zones, or slow adjustment rather than tight adherence to a fixed leverage ratio. This paper belongs in [[Capital Structure]], [[Target Leverage]], [[Financial Flexibility]], and [[Dynamic Corporate Finance]].

## 3. Research Question
What is the paper trying to answer?

Are corporate capital structures stable over long horizons, or do firms frequently move across leverage levels in ways that contradict the standard view of stable leverage targets?

More specifically: the paper tests whether high or low leverage today predicts high or low leverage in future cross-sections, whether firm fixed effects really imply persistent leverage, and which classes of target leverage models can match observed long-horizon instability.

## 4. Core Mechanism
Use a chain that can be memorized for comps:

```text
Long horizon firm evolution
-> investment opportunities, expansion needs, industry conditions, and financing choices change
-> firm-specific leverage targets or target zones shift over time
-> firms move across leverage quartiles rather than staying in fixed leverage positions
-> capital structures appear unstable even when firms may still behave as if they have broad target regions
```

## 5. Main Findings
1. Leverage cross-sections lose similarity quickly. Cross-sections more than a few years apart differ sharply, and the similarity continues to erode rather than reverting to a stable structure.

2. Firm fixed effects do not prove capital structure stability. They show that firms have different average leverage over the sample, but they do not show that firms maintain the same relative leverage position over time.

3. Stable leverage is the exception, not the rule. When stable regimes occur, they are usually temporary and concentrated at low leverage. Very few firms maintain high leverage persistently.

4. Long-horizon leverage migration is pervasive. Many firms experience both high and low leverage at different points in their lives.

5. Credible target leverage models must allow large movement. Models with time-varying targets, wide target zones, or slow adjustment better match the evidence than models with tight leverage targets or rapid rebalancing.

6. Industry leverage also varies substantially over time, which implies that both firm-level and industry-level time-varying determinants matter for capital structure.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Firm-year |
| Sample period | Main CRSP/Compustat sample from 1950 to 2008; hand-collected DJIA data extend back before the Great Depression |
| Main dataset | CRSP/Compustat industrial firms, plus hand-collected data from annual reports and Moody's manuals for 24 DJIA firms |
| Key variables | Book leverage, market leverage, net debt ratio, firm fixed effects, year effects, firm-decade interaction effects, industry-median leverage |
| Treatment or shock | No treatment. The paper studies long-horizon leverage dynamics and compares observed leverage behavior to alternative theoretical models |
| Outcome variables | Leverage levels, leverage ranges, leverage cross-section similarity, quartile migration, stable leverage regime indicators, simulation fit |

## 7. Identification Strategy

### Endogeneity Problem
This is not a causal treatment paper. The main empirical problem is interpretive rather than causal: prior studies treat high explanatory power from firm fixed effects as evidence that capital structure is stable, but firm fixed effects can mechanically summarize average leverage differences even when firms move substantially through the leverage distribution. A simple correlation between current and future leverage may also be misleading if short panels, survivorship, industry conditions, and firm life-cycle changes obscure long-run migration. Selection matters because firms with long histories differ from short-lived or recently listed firms, and Compustat panels include many firms with short histories, which can overstate apparent persistence.

### Identification Approach
- Natural experiment: None.
- Instrument: None.
- Difference in differences: None.
- Event study: Not a causal event study, though the paper studies leverage changes around departures from stable regimes and during the post-war expansion.
- Fixed effects: Uses firm and year effects, and emphasizes firm-decade interactions to show that firm-specific time-series variation is important.
- Matching: None.
- Placebo tests: Not central.
- Robustness: Uses multiple leverage definitions, different samples, long-horizon subsamples, constant-composition samples, and simulations of alternative leverage models.
- Alternative source of variation: Long-horizon within-firm variation, cross-sectional migration, industry-median leverage variation, and simulation-based comparison of capital structure models.

### Is the Identification Convincing?
- Strength: Very convincing as descriptive evidence against the strong claim that firms maintain stable leverage ratios over long horizons.
- Weakness: It does not identify a causal reason why leverage changes. It narrows the set of plausible theories but does not isolate one mechanism.
- Referee concern: The paper shows that leverage is unstable, but one might ask whether instability reflects changing optimal targets, financial flexibility, market timing, investment shocks, measurement choices, or sample composition.

## 8. Main Regression or Model

```text
Leverage_it = alpha_i + gamma_t + epsilon_it
```

This is the standard firm and year fixed-effect leverage specification. The paper argues that a high R-squared from this model does not imply that firms keep stable capital structures. It only means that firms differ in their average leverage over the panel.

A more relevant specification allows firm-specific time variation:

```text
Leverage_it = alpha_i + gamma_t + delta_i,decade + epsilon_it
```

Here, `alpha_i` captures persistent firm-level average leverage, `gamma_t` captures common time effects, and `delta_i,decade` captures firm-specific leverage changes across decades. The key interpretation is that significant firm-decade interactions mean that time-varying firm-specific leverage determinants are economically important.

The paper also uses cross-section persistence logic:

```text
Leverage_i,t+k = alpha_k + beta_k Leverage_it + epsilon_i,t+k
```

The key coefficient is `beta_k`. If capital structures are stable, `beta_k` should remain high even at long horizons. The paper finds that the predictive power of current leverage for future relative leverage positions declines sharply as the horizon lengthens.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Capital Structure]] by challenging the empirical premise that firms maintain stable leverage ratios over long horizons.
2. [[Target Leverage]] by showing that plausible target models must permit wide leverage variation.
3. [[Financial Flexibility]] by suggesting that low leverage stability may reflect temporary flexibility or conservative financing policies rather than permanent targets.
4. [[Dynamic Corporate Finance]] by emphasizing firm life-cycle dynamics, investment needs, and time-varying financing behavior.

It differs from prior work because prior studies often interpret firm fixed effects as evidence of leverage persistence. DeAngelo and Roll show that fixed effects can coexist with large within-firm movements across the leverage distribution.

## 10. Closely Related Papers
- [[Lemmon Roberts and Zender 2008]]: Finds strong firm fixed effects in leverage and argues for persistent leverage differences. DeAngelo and Roll directly challenge the stability interpretation.
- [[Rajan and Zingales 1995]]: Canonical empirical capital structure determinants such as size, profitability, tangibility, and market-to-book.
- [[Frank and Goyal 2009]]: Studies reliable determinants of leverage and highlights industry leverage as important.
- [[Chang and Dasgupta 2009]]: Shows that estimated speeds of adjustment may arise mechanically from financing behavior, complicating target leverage interpretation.
- [[Denis and McKeon 2012]]: Studies proactive leverage increases and dynamic debt issuance, consistent with large leverage movements.
- [[Strebulaev and Yang 2013]]: Studies zero-leverage behavior and conservative capital structures, closely related to the finding that stable regimes often occur at low leverage.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on capital structure dynamics. Discuss the data used and how the papers establish whether firms have target leverage ratios.

How to use this paper:
- Main finding: Corporate leverage is not stable over long horizons. Firms frequently migrate across leverage quartiles.
- Data: U.S. industrial firms in CRSP/Compustat from 1950 to 2008, with long-run hand-collected data for DJIA firms.
- Identification: Descriptive long-horizon evidence using cross-sectional persistence, firm-decade interactions, stable regime analysis, industry-median leverage, and simulations.
- Limitation: It does not identify the causal determinants of leverage changes.
- Connection to other papers: Use it against a simple reading of [[Lemmon Roberts and Zender 2008]] and alongside [[Frank and Goyal 2009]], [[Denis and McKeon 2012]], and [[Strebulaev and Yang 2013]].
- Best exam phrase: "Firm fixed effects show persistent average differences across firms, not necessarily stable capital structures."

## 12. Hypotheses Inspired by This Paper
H1: Firms with larger investment opportunity shocks experience greater long-horizon leverage migration than firms with stable investment opportunities.

H2: Firms with high financial flexibility needs are more likely to maintain low leverage temporarily, but less likely to maintain stable leverage permanently.

H3: Industry-level shocks explain a meaningful share of time-series variation in target leverage, but firm-specific expansion and financing needs explain departures from stable leverage regimes.

## 13. Possible Extension or Research Design
- Research question: Do supply-chain shocks cause firms to abandon stable leverage regimes?
- Hypothesis: Firms exposed to major input disruptions or geopolitical supplier shocks increase leverage when internal funds are insufficient to finance supplier replacement, inventory buildup, or relocation.
- Data: Compustat, FactSet Revere supply-chain links, sanctions exposure data, and debt issuance data.
- Identification: Difference in differences comparing firms with high exposure to shocked suppliers against otherwise similar firms with low exposure, with firm and quarter fixed effects.
- Expected result: Exposed firms should show larger leverage changes, especially when financially constrained or when replacement investment needs are high.
- Contribution: This would connect capital structure instability to real-side shocks and [[Supply Chain Finance]], providing a causal mechanism for the instability documented by DeAngelo and Roll.

## 14. Critiques

### Major Concern 1
The paper is primarily descriptive. It powerfully rejects the claim that leverage is stable, but it does not identify a single causal mechanism behind leverage instability.

### Major Concern 2
The simulations narrow the set of plausible models but may not uniquely distinguish among time-varying targets, flexible target zones, and slow adjustment. Multiple theories can fit the same instability pattern.

### Minor Concern
Long-horizon samples raise survivorship and selection concerns. Firms with 20-plus years of data are economically important, but they are not representative of all listed firms.

### Referee Recommendation
Accept, because the paper makes a major conceptual and empirical contribution by overturning a widely accepted interpretation of firm fixed effects in leverage regressions. The paper is strongest as a discipline-setting fact paper rather than as a causal identification paper.

## 15. Memory Hooks
- "Fixed effects are averages, not stability."
- "Stable leverage is temporary and mostly low leverage."
- "Capital structures migrate across quartiles."
- "Targets must be flexible, slow, or time-varying."
- "The capital structure puzzle is dynamic, not just cross-sectional."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Capital Structure]], [[Target Leverage]], [[Financial Flexibility]], [[Dynamic Corporate Finance]], or [[Firm Fixed Effects]]. The clean exam answer is: "DeAngelo and Roll 2015 use long-horizon CRSP/Compustat and hand-collected DJIA leverage data to show that corporate leverage is far less stable than prior fixed-effect evidence suggests." Use it to argue that capital structure theories must explain large within-firm leverage movements over time, not just cross-sectional differences in average leverage. In a critique answer, emphasize that the paper is descriptive rather than causal, but note that it is stronger than a standard correlation because it directly tests long-horizon cross-sectional persistence, examines stable leverage regimes, adds firm-decade interactions, and compares the data to alternative leverage-targeting models.