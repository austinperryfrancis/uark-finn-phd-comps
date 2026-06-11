---
type: paper
status: unread
title: Innovation Activities and Integration through Vertical Acquisitions
authors: Laurent Frésard, Gerard Hoberg, Gordon M. Phillips
year: 2020
journal: Review of Financial Studies
seminar:
field: Corporate Finance
literature:
  - Firm Boundaries
  - Vertical Integration
  - Mergers and Acquisitions
  - Innovation
methods:
  - Text analysis
  - Probit
  - Matched comparisons
  - Event study
  - Heterogeneity tests
datasets:
  - Compustat
  - SEC EDGAR 10-Ks
  - BEA Input-Output Tables
  - SDC Platinum
  - USPTO patents
  - NBER patent data
  - Kogan et al. patent data
  - PatentView
  - USPTO Patent Assignment Database
identification: Observational firm-year acquisition design with controls, year fixed effects, industry-year robustness, matched targets, nonvertical acquisition placebo, mechanism heterogeneity, and event-time evidence around acquisitions.
main_result: R&D-intensive firms are less likely to be acquired by vertically related buyers, while patent-intensive firms are more likely to be acquired vertically.
exam_relevance: high
must_memorize: true
tags:
  - corporate-finance
  - mergers
  - vertical-integration
  - firm-boundaries
  - innovation
  - patents
  - text-analysis
created: 2026-06-05
updated: 2026-06-05
---

# Fresard, Hoberg, and Phillips 2020

## 1. One-Sentence Takeaway
This paper shows that the stage of innovation shapes vertical acquisitions using 10-K text linked to BEA input-output product vocabularies, and the main contribution is to show that unrealized innovation discourages vertical integration while patented innovation encourages it.

## 2. Exam-Ready Abstract
Frésard, Hoberg, and Phillips study whether firms' innovation stage affects the boundaries of the firm. They build a dynamic, directed firm-pair network of vertical relatedness by linking firms' 10-K product descriptions to product vocabulary from BEA input-output tables. The core idea is that R&D represents unrealized innovation, which is difficult to contract on and depends on human capital, so acquiring the innovator can weaken ex ante incentives. Patents represent realized and legally protected innovation, so vertical acquisition can transfer control rights to the party best positioned to commercialize the innovation and reduce holdup. In a sample of public U.S. firms from 1996 to 2013, R&D intensity negatively predicts becoming a vertical acquisition target, while patenting intensity positively predicts becoming a vertical acquisition target. The results are stronger when incentive problems and holdup risks should matter more, and they do not appear in the same way for nonvertical or horizontal acquisitions. This paper connects [[Firm Boundaries]], [[Vertical Integration]], [[Mergers and Acquisitions]], and [[Innovation]].

## 3. Research Question
What determines whether vertically related firms remain separate or integrate through acquisition?

More specifically: does the stage of a target firm's innovation affect its likelihood of being acquired by a vertically related buyer?

The mechanism is the trade-off between:
1. Preserving ex ante innovation incentives when innovation is unrealized.
2. Reducing ex post holdup and improving commercialization incentives when innovation is realized and protected by patents.

## 4. Core Mechanism
Use this chain for comps:

```text
Innovation stage changes
-> R&D is unrealized and noncontractible, while patents are realized and legally protected
-> control rights become more or less valuable to the potential acquirer
-> firms either remain vertically separated or integrate through acquisition
-> vertical acquisitions occur when patents reduce holdup and commercialization becomes more important than preserving independent R&D incentives
```

Alternative shorter version:

```text
Unrealized R&D
-> hard to contract on and tied to employees
-> acquisition weakens innovator incentives
-> vertical separation is optimal
-> lower probability of vertical acquisition
```

```text
Granted patents
-> realized innovation with legal property rights
-> acquirer can commercialize and avoid holdup
-> vertical integration becomes more attractive
-> higher probability of vertical acquisition
```

## 5. Main Findings
1. R&D intensity is negatively related to becoming a target in a vertical acquisition.
2. Patenting intensity is positively related to becoming a target in a vertical acquisition.
3. The R&D result is stronger when post-acquisition incentive provision is harder, especially when inventor mobility is high.
4. The patent result is stronger when holdup risk is higher, and weaker when patent secondary markets are liquid, infringement is common, or many peer firms reduce dependence on a specific trading partner.
5. The results are specific to vertical acquisitions. R&D intensity positively predicts nonvertical and horizontal acquisition targets, while patents do not strongly predict those deals.
6. Around vertical acquisitions, patenting peaks near the acquisition year and R&D falls afterward, which supports the idea that acquisition occurs when innovation has become realized and further independent R&D incentives are less central.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Firm-year for acquisition likelihood tests; firm-pair-year for vertical relatedness network |
| Sample period | 1996 to 2013 |
| Main dataset | Public U.S. firms from Compustat merged to SEC EDGAR 10-K business descriptions |
| M&A data | SDC Platinum, completed and announced U.S. transactions coded as mergers, majority-interest acquisitions, or asset acquisitions |
| Vertical relatedness data | BEA 2002 input-output tables linked to 10-K product text |
| Patent data | USPTO, NBER patent database, Kogan et al. patent data, manual matching for 2011 to 2013 |
| Key variables | R&D/sales, patents/assets, vertical target dummy, nonvertical target dummy, text-based vertical relatedness |
| Treatment or shock | No clean exogenous shock. Main variation is cross-sectional and time-series variation in innovation stage and vertical relatedness |
| Outcome variables | Probability of becoming a vertical acquisition target; degree of firm-level vertical integration |
| Controls | Size, age, PPE/assets, number of segments, market-to-book, cash flow/assets, operating income/sales, sales growth, HHI, end-user exposure |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between innovation and vertical acquisition is not causal because firms choose R&D, patenting, and acquisition timing endogenously. High-R&D firms may differ from low-R&D firms in growth opportunities, managerial quality, product-market position, financing constraints, or acquisition attractiveness. Patents may signal firm quality rather than change control-rights trade-offs. Reverse causality is also possible: firms expecting acquisition might reduce R&D or patent more aggressively to become more attractive targets. There is also measurement concern because R&D and patents imperfectly capture unrealized and realized innovation.

### Identification Approach
- Natural experiment: None.
- Instrument: None.
- Difference in differences: Not the main design.
- Event study: Tracks R&D and patenting from t-3 to t+3 around vertical acquisitions.
- Fixed effects: Year fixed effects in baseline; industry-year fixed effects in robustness; firm fixed effects in vertical integration tests.
- Matching: Compares vertical targets to matched nonmerging firms using propensity score matching based on industry, size, and year.
- Placebo tests: Nonvertical and horizontal acquisitions show different patterns.
- Robustness: Lagged independent variables, OLS linear probability model, text-based measures of R&D and patents, industry-level innovation measures, innovation efficiency controls, NAICS-based vertical relatedness in appendix, upstream and downstream subsamples.
- Alternative source of variation: Heterogeneity by incentive provision and holdup proxies.

### Is the Identification Convincing?
- Strength: Strong mechanism-consistent evidence. The results line up with property-rights theory, appear only for vertical acquisitions, and are stronger exactly where incentive and holdup channels should matter.
- Weakness: Not a clean causal identification design. Innovation stage and acquisition timing remain endogenous.
- Referee concern: Patents may proxy for successful innovation or target quality rather than reduced holdup. The paper addresses this with innovation efficiency controls and event-time patterns, but cannot fully rule out signaling.

## 8. Main Regression or Model

```text
Pr(VerticalTarget_it = 1) =
  Phi(
    beta1 R&D/Sales_it
  + beta2 Patents/Assets_it
  + gamma Controls_it
  + Year FE
  + epsilon_it
  )
```

The dependent variable is an indicator for whether firm i becomes a target in a vertical acquisition in year t. Vertical transactions are identified using the paper's text-based vertical relatedness network. The key coefficients are beta1 and beta2. The prediction is beta1 < 0 because R&D is unrealized innovation and separation preserves incentives. The prediction is beta2 > 0 because patents are realized innovation and integration reduces holdup.

Mechanism heterogeneity version:

```text
Pr(VerticalTarget_it = 1) =
  Phi(
    beta1 R&D/Sales_it
  + beta2 Patents/Assets_it
  + beta3 R&D/Sales_it x HighIncentiveProblem_it
  + beta4 Patents/Assets_it x HighHoldupRisk_it
  + gamma Controls_it
  + Year FE
  + Year x High FE
  + epsilon_it
  )
```

beta3 should be negative when incentive provision is difficult, such as high inventor mobility. beta4 should be positive when holdup risk is high. In the paper's tests, patent effects are weaker when holdup risk is lower, such as when patent markets are more liquid or many peer firms are available.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Firm Boundaries]] by showing that innovation stage affects whether firms integrate or stay separate.
2. [[Vertical Integration]] by providing firm-pair text-based measures of vertical relatedness rather than relying only on NAICS or SIC industry links.
3. [[Mergers and Acquisitions]] by identifying a distinct vertical acquisition motive based on control rights, incentives, and holdup.
4. [[Innovation]] by separating unrealized innovation, measured by R&D, from realized innovation, measured by patents.

It differs from prior work because it studies vertical acquisitions at the firm-pair level using product text and BEA input-output vocabulary, rather than using coarse industry classifications.

## 10. Closely Related Papers
- [[Grossman and Hart 1986]]: Property-rights theory of the firm and residual control rights.
- [[Hart and Moore 1990]]: Incomplete contracts and firm boundaries.
- [[Williamson 1971]]: Vertical integration as a response to holdup and transaction costs.
- [[Aghion and Tirole 1994]]: Innovation incentives and allocation of control rights.
- [[Fan and Goyal 2006]]: Vertical mergers and shareholder wealth effects.
- [[Ahern 2012]]: Bargaining power in customer-supplier relationships and M&A gains.
- [[Ahern and Harford 2014]]: Supply-chain shocks and merger waves.
- [[Atalay, Hortacsu, and Syverson 2014]]: Vertical integration and limited physical shipments within firms.
- [[Acemoglu et al. 2010]]: Vertical integration and innovation in manufacturing.
- [[Bena and Li 2014]]: Innovation and corporate acquisitions.
- [[Hoberg and Phillips 2016]]: Text-based product market networks.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the literature on firm boundaries and vertical integration. How do innovation and intangible assets affect the decision to integrate?

How to use this paper:
- Main finding: R&D-intensive targets are less likely to be acquired vertically, while patent-intensive targets are more likely to be acquired vertically.
- Data: Public U.S. firms, 10-K product text, BEA input-output tables, SDC acquisitions, Compustat, and patent data.
- Identification: Observational probit design with rich controls, text-based vertical relatedness, matched comparisons, mechanism heterogeneity, event-time evidence, and nonvertical acquisition placebo tests.
- Limitation: Not a natural experiment. Results are best interpreted as mechanism-consistent evidence rather than definitive causal estimates.
- Connection to other papers: Extends [[Grossman and Hart 1986]], [[Hart and Moore 1990]], and [[Williamson 1971]] into an empirical corporate finance setting using text-based M&A data.
- Best exam phrase: "Frésard, Hoberg, and Phillips show that vertical acquisitions reallocate control rights when innovation moves from unrealized R&D to realized patents."

## 12. Hypotheses Inspired by This Paper
H1: Firms with higher R&D intensity are less likely to become targets in vertical acquisitions because separation preserves innovation incentives.

H2: Firms with higher patenting intensity are more likely to become targets in vertical acquisitions because patents make control rights transferable and reduce holdup.

H3: The negative R&D effect is stronger when human capital is mobile or difficult to retain after acquisition.

H4: The positive patent effect is stronger when holdup risk is high and weaker when substitute trading partners or liquid patent markets reduce dependence.

H5: Vertical acquisitions should be followed by lower target or combined-entity R&D intensity if the acquisition occurs after the need for independent innovation incentives declines.

## 13. Possible Extension or Research Design
- Research question: Do vertical acquisitions of AI startups follow the same innovation-stage logic as traditional patent-based acquisitions?
- Hypothesis: AI startups with high ongoing model-development intensity but weak intellectual property protection are less likely to be acquired vertically, while startups with more formalized IP, proprietary datasets, or deployed products are more likely to be acquired.
- Data: Crunchbase or PitchBook acquisitions, patent data, GitHub activity, model release data, product descriptions, 10-K AI disclosures, customer-supplier links.
- Identification: Compare vertical versus nonvertical AI acquisitions, using shocks to IP enforceability or data-access regulation as sources of variation if available.
- Expected result: Realized and protectable AI assets should increase vertical acquisition likelihood, while ongoing tacit development should favor separation or partnerships.
- Contribution: Extends the theory from patents to modern intangible assets where legal property rights are weaker and human capital is central.

## 14. Critiques

### Major Concern 1
The paper does not have a clean exogenous shock to innovation stage or vertical acquisition incentives. The evidence is highly consistent with theory, but the design is not a natural experiment.

### Major Concern 2
Patents may measure target quality, successful innovation, or salience to acquirers rather than a shift in holdup risk. The paper addresses this with innovation efficiency controls and mechanism tests, but signaling cannot be fully ruled out.

### Minor Concern
The text-based vertical relatedness measure is innovative but depends on the mapping between 10-K language and BEA commodity vocabularies. It likely improves on NAICS, but measurement error remains possible.

### Referee Recommendation
Accept, because the paper makes a major measurement contribution, ties directly to theory of the firm, and provides a coherent set of mechanism and placebo tests. The identification is not clean enough to claim full causality, but the paper is strong as theory-guided empirical corporate finance.

## 15. Memory Hooks
- "R&D separates, patents integrate."
- "Unrealized innovation needs incentives; realized innovation needs control."
- "Vertical M&A as a control-rights transfer."
- "10-K text plus BEA input-output tables."
- "Patents reduce holdup, R&D preserves autonomy."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Firm Boundaries]], [[Vertical Integration]], [[Mergers and Acquisitions]], [[Innovation]], [[Text Analysis]], or [[Incomplete Contracts]]. The clean exam answer is: "Frésard, Hoberg, and Phillips use 10-K product text linked to BEA input-output tables to identify vertical firm pairs and show that R&D-intensive firms are less likely, while patent-intensive firms are more likely, to be acquired by vertically related buyers." Use it to argue that firm boundaries depend not just on industry structure, but on the stage of intangible asset development. In a critique answer, emphasize that the paper is not a clean natural experiment, but note that it is stronger than a standard correlation because the results are unique to vertical acquisitions, survive innovation efficiency controls, appear in mechanism-relevant subsamples, and are supported by event-time patterns around acquisitions.