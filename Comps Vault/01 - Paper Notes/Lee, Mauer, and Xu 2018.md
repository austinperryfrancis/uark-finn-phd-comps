---
type: paper
status: unread
title: Human capital relatedness and mergers and acquisitions
authors: Kyeong Hun Lee, David C. Mauer, Emma Qianying Xu
year: 2018
journal: Journal of Financial Economics
professor: DrJandik
seminar: null
jandik_paper_number: 37
jandik_week: 10
jandik_topic: 'M&A: sources of synergies'
jandik_done: false
field: Corporate Finance
literature:
- '[[Mergers and Acquisitions]]'
- '[[Labor and Finance]]'
- Theory of the Firm
methods:
- Probit
- OLS
- event study
- matched nonmerging pairs
- falsification test
datasets:
- '[[SDC M&A]]'
- '[[Compustat]]'
- '[[CRSP]]'
- Compustat Industry Segment
- BLS Occupational Employment Statistics
- Hoberg-Phillips product similarity
identification: Matched-pair merger prediction, announcement-return event study, postmerger outcome changes, asset-sale falsification test
main_result: Mergers are more likely and create more value when acquirer and target human capital profiles are related, especially in diversifying acquisitions.
exam_relevance: high
must_memorize: true
tags:
- corporate-finance
- mergers-and-acquisitions
- human-capital
- labor-finance
- theory-of-the-firm
- product-market
- falsification-test
created: 2026-06-12
updated: 2026-06-12
---

# Lee, Mauer, and Xu 2018

## 1. One-Sentence Takeaway
This paper shows that human capital relatedness predicts merger likelihood, merger synergies, and postmerger performance using occupation-based firm human capital profiles, and the main contribution is showing that labor complementarities help explain the boundaries of the firm.

## 2. Exam-Ready Abstract
Lee, Mauer, and Xu ask whether related human capital between acquirers and targets encourages mergers and creates value. They construct a human capital relatedness measure by combining BLS Occupational Employment Statistics occupation profiles with firms' segment industries from Compustat. The setting is US public mergers from 1997 to 2012, with merger likelihood tested against matched nonmerging firm pairs and merger gains measured through announcement returns and postmerger operating performance. They find that firms with more related human capital are more likely to merge, earn higher combined announcement returns, and show better postmerger operating performance. The effects are strongest in diversifying or product-market-unrelated acquisitions, where overlapping worker skills give the merged firm bargaining power to reduce redundant employment and labor costs. The main identification support is not a clean shock, but rather extensive controls, matched nonmerging pairs, product-market controls, and an asset-sale falsification test showing HCR matters only when employees are likely transferred. This paper connects to [[Mergers and Acquisitions]], [[Human Capital]], [[Theory of the Firm]], and [[Product Market Competition]].

## 3. Research Question
What role does human capital relatedness play in mergers and acquisitions?

More specifically: do firms with overlapping employee skill profiles become more likely merger partners, and does this overlap generate value by improving postmerger bargaining power, workforce selection, wage discipline, and labor cost savings?

## 4. Core Mechanism
Use a chain that can be memorized for comps:

```text
High acquirer-target human capital relatedness
-> overlapping worker skills and job functions
-> postmerger firm has more bargaining power over employees
-> firm can retain better workers, lay off duplicates, reduce wages or SG&A, or winner-pick ideas
-> higher merger likelihood, higher announcement synergy, and better postmerger performance
```

For related product-market mergers:

```text
High HCR plus high product-market overlap
-> merger reduces competition for human capital
-> employee innovation incentives may weaken
-> value gains from HCR are attenuated
-> weaker or negative effect in horizontal or product-market-related mergers
```

## 5. Main Findings
1. Human capital relatedness predicts merger likelihood. This effect is distinct from Hoberg-Phillips product-market relatedness.
2. HCR predicts higher combined acquirer-target announcement returns and better postmerger operating performance.
3. The gains are concentrated in diversifying or product-market-unrelated mergers, not in horizontal or product-market-related deals.
4. High HCR predicts lower postmerger employment and lower labor-cost proxies, especially SG&A, consistent with workforce rationalization.
5. The paper finds little reliable evidence that HCR increases measured labor productivity.
6. Asset-sale falsification: HCR predicts acquirer returns when employees likely transfer with the asset, but not when little or no labor transfers.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Acquirer-target pair, matched nonmerging firm pair, and postmerger firm outcome |
| Sample period | Main M&A sample: 1997 to 2012. Asset-sale falsification: 1997 to 2013 |
| Main dataset | SDC M&A for deals, Compustat and CRSP for financials and returns, Compustat Industry Segment for segment industries, BLS OES for occupation profiles |
| Key variables | Human capital relatedness, product-market relatedness, combined announcement return, postmerger operating performance, employment, SG&A |
| Treatment or shock | No exogenous shock. Main variable is pairwise HCR between acquirer and target |
| Outcome variables | Merger probability, synergy return, acquirer CAR, target CAR, postmerger operating performance, employment change, SG&A change, asset-sale acquirer CAR |

## 7. Identification Strategy

### Endogeneity Problem
The core endogeneity problem is endogenous matching. Firms do not randomly merge with firms that have related human capital. High-HCR firms may also share technologies, industries, cultures, growth opportunities, or managerial strategies that independently predict merger likelihood and value creation. Omitted variables such as industry shocks, acquisition waves, product-market similarity, and management quality could drive both HCR and merger gains. Reverse causality is less direct because HCR is measured before the deal, but anticipatory restructuring or strategic positioning could still contaminate interpretation. Measurement error is also important because firm-level human capital profiles are inferred from industry occupation profiles, not actual worker-level data.

### Identification Approach
- Natural experiment: None.
- Instrument: None.
- Difference in differences: Not the main design. The paper studies postmerger changes relative to premerger levels, but not a clean DiD with random treatment.
- Event study: Uses announcement-window combined acquirer-target CARs as market-based merger synergy.
- Fixed effects: Includes year fixed effects and many acquirer, target, and deal controls.
- Matching: Compares merging firm pairs to matched nonmerging firm pairs based on vertical relation, product similarity, number of segments, size, and market-to-book.
- Placebo tests: Not a standard placebo, but the asset-sale falsification test is similar in spirit.
- Robustness: Controls for product-market relatedness, HCR x PMR interactions, merger-type splits, robust regressions, and exclusion of cases where HCR equals one.
- Alternative source of variation: Asset sales where human capital may or may not transfer.

### Is the Identification Convincing?
- Strength: Strong measurement contribution, strong cross-sectional patterns, market-based outcome, matched nonmerging pairs, and a clever falsification test.
- Weakness: HCR is not randomly assigned, and it may proxy for unobserved industry or technology complementarities.
- Referee concern: The big concern is that HCR captures product-market relatedness or general relatedness rather than human capital. The paper directly addresses this by controlling for Hoberg-Phillips product similarity and showing HCR matters less when no labor transfers in asset sales.

## 8. Main Regression or Model

```text
Pr(Merger_ij,t = 1) =
  Phi(beta1 HCR_ij,t-1
     + beta2 PMR_ij,t-1
     + beta3 HCR_ij,t-1 x PMR_ij,t-1
     + Controls_ij,t-1
     + Year FE)
```

This probit model asks whether two firms are more likely to merge when their inferred occupation profiles are more similar. `beta1` captures the merger-likelihood effect of human capital relatedness when product-market relatedness is low. `beta3` tests whether the effect of HCR is weaker when firms also have high product-market relatedness.

```text
Synergy_ij,t =
  beta1 HCR_ij,t-1
+ beta2 PMR_ij,t-1
+ beta3 HCR_ij,t-1 x PMR_ij,t-1
+ Deal Controls
+ Acquirer Controls
+ Target Controls
+ Year FE
+ epsilon_ij,t
```

`Synergy` is the value-weighted combined acquirer-target abnormal return around the announcement. The main economic interpretation is `beta1`: whether high-HCR deals create more value. The interaction `beta3` is important because the paper argues HCR is most valuable in diversifying deals, while high product-market overlap attenuates the benefits.

```text
Postmerger Outcome_i =
  beta HCR_ij,t-1
+ beta2 PMR_ij,t-1
+ beta3 HCR_ij,t-1 x PMR_ij,t-1
+ Controls
+ Year FE
+ epsilon_i
```

Postmerger outcomes include industry-adjusted operating performance, employment changes, and SG&A changes. These regressions test whether the valuation gains map into real postmerger changes.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Mergers and Acquisitions]] by showing that labor-relatedness helps explain merger partner selection and merger gains.
2. [[Theory of the Firm]] by extending asset complementarity arguments from physical and product assets to rented human capital.
3. [[Labor and Finance]] by showing that workforce composition matters for corporate boundary decisions.
4. [[Product Market Competition]] by showing that human capital relatedness has different implications depending on product-market overlap.

It differs from prior work because it creates a pairwise, occupation-based human capital relatedness measure and uses it to study merger likelihood, announcement returns, postmerger real outcomes, and asset-sale falsification.

## 10. Closely Related Papers
- [[Grossman and Hart 1986]]: Property rights theory of the firm.
- [[Hart and Moore 1990]]: Incomplete contracting and asset ownership.
- [[Rhodes-Kropf and Robinson 2008]]: Assortative matching and merger theory.
- [[Hoberg and Phillips 2010]]: Product-market relatedness and merger synergies.
- [[Fulghieri and Sevilir 2011]]: Mergers, human capital, and innovation incentives.
- [[Tate and Yang 2016]]: Human capital transferability and diversifying acquisitions.
- [[Gao and Ma 2016]]: Acquiring employees through M&A.
- [[Ouimet and Zarutskie 2016]]: Acqui-hiring and labor in acquisitions.
- [[Bena and Li 2014]]: Technological overlap and innovation in mergers.
- [[Eisfeldt and Papanikolaou 2013]]: Organizational capital and asset pricing.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on merger synergies. Discuss how papers measure synergies and how they establish causality.

How to use this paper:
- Main finding: Human capital relatedness predicts merger likelihood, synergy returns, and postmerger performance.
- Data: SDC M&A, Compustat, CRSP, BLS OES, Compustat segment data, Hoberg-Phillips product similarity.
- Identification: Matched nonmerging pairs, event-study returns, controls for product-market relatedness, and asset-sale falsification.
- Limitation: HCR is inferred from industry occupation profiles, not actual employee-level data, and merger matching is endogenous.
- Connection to other papers: Pair with [[Hoberg and Phillips 2010]] for product complementarity, [[Rhodes-Kropf and Robinson 2008]] for assortative matching, and [[Tate and Yang 2016]] for human capital transferability.
- Best exam phrase: "Lee, Mauer, and Xu show that merger synergies are not only about products or physical assets. They also depend on whether the acquirer and target have related human capital that can be redeployed, rationalized, or used to strengthen bargaining power."

## 12. Hypotheses Inspired by This Paper
H1: Acquirers with greater human capital overlap with targets will experience larger announcement returns when the deal is diversifying rather than horizontal.

H2: Postmerger layoffs will be concentrated in occupational categories with the greatest acquirer-target overlap.

H3: The value of HCR will be larger when labor markets are thick, nonunionized, and less protected by employment law, because acquirers can more easily replace or bargain with workers.

## 13. Possible Extension or Research Design
- Research question: Does actual employee movement after mergers validate occupation-based human capital relatedness measures?
- Hypothesis: High-HCR mergers lead to more targeted retention of high-skill workers and larger layoffs among duplicate support occupations.
- Data: SDC M&A, LinkedIn resume data, Revelio Labs, Burning Glass job postings, Compustat, CRSP, and BLS OES.
- Identification: Compare employee retention, departures, and job postings around mergers using matched low-HCR deals, occupation fixed effects, firm fixed effects, and local labor-market controls.
- Expected result: HCR predicts selective retention and occupational restructuring, especially in diversifying acquisitions.
- Contribution: Moves the paper from inferred industry-level human capital to actual worker-level flows, strengthening the causal interpretation of the mechanism.

## 14. Critiques

### Major Concern 1
HCR may proxy for unobserved technological, operational, or strategic relatedness rather than human capital itself. The paper controls for Hoberg-Phillips product-market relatedness, but some latent relatedness could remain.

### Major Concern 2
The HCR measure is built from industry occupation profiles rather than firm-specific worker data. This is a clever solution to data scarcity, but it may mismeasure firms with unusual labor forces relative to their industry.

### Minor Concern
SG&A is used as a proxy for labor expense because Compustat labor expense coverage is limited. SG&A is correlated with labor expense, but it also includes nonlabor costs.

### Referee Recommendation
R&R, leaning accept, because the question is important and the measure is novel, but the authors must convince readers that HCR is not just another proxy for product or technology relatedness. The asset-sale falsification test and PMR controls make the paper much stronger than a standard correlation.

## 15. Memory Hooks
- "Human capital is rented, not owned."
- HCR equals cosine similarity between acquirer and target occupation profiles.
- Value comes from bargaining power, layoffs, wage discipline, and winner-picking.
- Strongest in diversifying mergers, weaker in horizontal/product-related mergers.
- Asset-sale falsification: HCR matters only when labor likely transfers.

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Mergers and Acquisitions]], [[Human Capital]], [[Theory of the Firm]], [[Labor and Finance]], [[Product Market Competition]], or [[Event Studies]]. The clean exam answer is: "Lee, Mauer, and Xu use occupation-based human capital relatedness as a measure of labor complementarity and show that high-HCR firms are more likely to merge and generate higher merger synergies, especially in diversifying acquisitions." Use it to argue that merger synergies are not only about product-market overlap, market power, or physical assets. They can also come from the structure of the workforce. In a critique answer, emphasize that HCR is measured indirectly and merger matching is endogenous, but note that the paper is stronger than a standard correlation because it uses matched nonmerging pairs, product-market controls, announcement returns, postmerger real outcomes, and an asset-sale falsification test.