---
type: paper
status: unread
title: Financial versus Strategic Buyers
authors: Marc Martos-Vila, Matthew Rhodes-Kropf, Jarrad Harford
year: 2019
journal: Journal of Financial and Quantitative Analysis
professor: DrJandik
seminar: null
jandik_paper_number: 36
jandik_week: 9
jandik_topic: Internal capital markets, diversification, and M&A basics
jandik_done: true
field: Corporate Finance
literature:
- M&A
- '[[Private Equity]]'
- Debt Misvaluation
- '[[Mergers and Acquisitions]]'
methods:
- Theory
- Tobit regressions
- Logistic regressions
- Industry fixed effects
datasets:
- '[[SDC Platinum]]'
- Moody's Average Position
- '[[Compustat]]'
- macro controls
identification: Theory plus suggestive empirical tests using ex post debt rating accuracy as a proxy for debt market overvaluation
main_result: Debt overvaluation shifts acquisition activity toward financial buyers because PE can exploit mispriced debt more than strategic buyers, especially relative to conglomerate acquirers.
exam_relevance: high
must_memorize: true
tags:
- mergers-and-acquisitions
- private-equity
- debt-misvaluation
- merger-waves
- capital-structure
- corporate-governance
created: 2026-06-05
updated: 2026-06-05
---

# Martos-Vila, Rhodes-Kropf, and Harford 2019

## 1. One-Sentence Takeaway
This paper shows that debt market overvaluation can shift M&A activity toward financial buyers using a theory of coinsurance, monitoring, and debt misvaluation, and the main contribution is explaining why private equity activity rises relative to strategic acquirers when debt is overpriced.

## 2. Exam-Ready Abstract
Martos-Vila, Rhodes-Kropf, and Harford ask why financial buyers, especially private equity acquirers, sometimes dominate strategic buyers in merger waves. The paper develops a model in which investors misperceive default probabilities, so debt can be overvalued or undervalued. Strategic buyers combine target assets with existing assets, which creates coinsurance, but this also reduces their ability to exploit debt market mistakes because the perceived default benefit is partly offset. Private equity buyers evaluate the target more like a stand-alone project and have stronger monitoring technology, so debt overvaluation increases their willingness to pay and their ability to lever the deal. Empirically, the paper uses SDC M&A data and Moody's ex post rating accuracy measure, Average Position, to show that lower rating accuracy, interpreted as more debt overvaluation, predicts a larger PE share of acquisition activity. The evidence is especially strong when comparing PE buyers to conglomerate strategic buyers, which supports the coinsurance mechanism. This paper connects to [[M&A]], [[Private Equity]], [[Capital Structure]], and [[Market Timing]].

## 3. Research Question
What explains the shifting dominance of financial buyers versus strategic buyers in M&A markets?

More specifically: does debt market misvaluation affect which organizational form owns assets, and does it favor private equity buyers through coinsurance and monitoring channels?

## 4. Core Mechanism
Use a chain that can be memorized for comps:

```text
Debt market overvaluation
-> investors underestimate default risk and lend too cheaply
-> PE buyers can exploit cheap debt more directly than strategic buyers
-> strategic buyers lose some misvaluation rents because project coinsurance reduces perceived default benefits
-> PE monitoring also relaxes moral hazard and financing constraints
-> PE buyers can use more leverage, pay more, and win more targets
-> PE share of M&A rises relative to strategic buyers
```

## 5. Main Findings
1. Debt overvaluation favors financial buyers over strategic buyers because strategic acquirers combine projects, and coinsurance reduces the extent to which they can exploit investors' mistaken beliefs about debt risk.
2. Debt overvaluation increases the value of monitoring because investors perceive agency problems as less severe, which allows PE buyers to raise more debt and increases their willingness to pay.
3. Debt overvaluation expands the set of firms that can be acquired, especially by PE buyers, by loosening financing constraints.
4. Empirically, lower Moody's Average Position, meaning lower ex post rating accuracy and more debt overvaluation, predicts a higher PE share of M&A activity.
5. The effect is stronger when PE buyers are compared with conglomerate acquirers, consistent with the paper's coinsurance prediction.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Mainly industry-year and aggregate-year M&A activity |
| Sample period | SDC M&A activity from 1984 to 2010 in descriptive figures; Moody's AP evidence mainly 1984 to 2006 |
| Main dataset | SDC Platinum M&A transactions, Moody's Average Position rating accuracy data, Compustat, macro controls |
| Key variables | PE share of deal value, PE/(PE + conglomerate) share, Moody's Average Position, high-yield spread, 5-year Treasury rate, C&I loan spread, market-to-book, GDP growth |
| Treatment or shock | Debt market overvaluation proxied by low Moody's Average Position |
| Outcome variables | Fraction of M&A value acquired by PE buyers, high PE activity indicator, PE share relative to conglomerate acquirers |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between credit conditions and PE activity is not causal because credit markets, PE fundraising, macroeconomic conditions, target selection, and merger waves are jointly determined. Low spreads may reflect real improvements in fundamentals rather than debt overvaluation. Moody's Average Position may capture rating mistakes, changing issuer quality, or realized default shocks, not necessarily mispriced debt. PE activity itself may also rise in periods when targets are cheaper, strategic buyers are constrained, or investor risk appetite is high.

### Identification Approach
- Natural experiment: None. The empirical section is suggestive rather than a clean natural experiment.
- Instrument: None.
- Difference in differences: Not a formal DiD.
- Event study: Not central to the paper.
- Fixed effects: Industry fixed effects in some specifications.
- Matching: Not clear from provided text.
- Placebo tests: Not clear from provided text.
- Robustness: Controls for credit conditions, equity valuations, GDP, alternative PE activity measures, high PE activity logit, industry fixed effects, and PE fundraising controls in untabulated tests.
- Alternative source of variation: Moody's Average Position at the aggregate and Fama-French 12-industry level; downgrade-to-upgrade ratio as an alternative debt misvaluation proxy.

### Is the Identification Convincing?
- Strength: The theory generates sharp cross-sectional predictions. The empirical evidence tests not just PE activity generally, but PE activity relative to conglomerate strategic buyers, which is a distinctive prediction of the coinsurance mechanism.
- Weakness: Moody's AP is an ex post proxy. It may measure rating accuracy, default realization, or issuer composition rather than debt market mispricing known to investors at the time.
- Referee concern: The empirical evidence may not isolate debt misvaluation from broader credit supply, risk appetite, or macro-financial conditions.

## 8. Main Regression or Model

```text
PEShare_jt = alpha
           + beta AP_jt
           + gamma CreditConditions_t
           + delta EquityValuation_t
           + theta MacroControls_t
           + Industry FE
           + epsilon_jt
```

The dependent variable is the share of M&A activity accounted for by private equity buyers. AP is Moody's Average Position, where lower AP means lower rating accuracy and more debt overvaluation. The key coefficient is beta. The theory predicts beta < 0 because lower AP should correspond to greater PE activity.

For the coinsurance channel:

```text
PE_CONG_jt = alpha
           + beta AP_jt
           + gamma Controls_t
           + epsilon_jt
```

PE_CONG is PE activity divided by PE plus conglomerate strategic activity. The key prediction is again beta < 0. If PE gains especially against conglomerate acquirers when debt is overvalued, that supports the mechanism that strategic diversification and coinsurance reduce the ability to exploit cheap debt.

For the monitoring and debt issuance channel:

```text
PEShare_jt = alpha
           + beta1 AP_t
           + beta2 HighDebtIssuance_t
           + beta3 AP_t x HighDebtIssuance_t
           + Controls_t
           + epsilon_jt
```

The interaction tests whether debt misvaluation matters more when aggregate debt issuance is high. The coefficient beta3 carries the monitoring and financing constraint interpretation.

Core theoretical result:

```text
Debt overvaluation: p'_H > p_H
-> V_PE > V_s
```

When investors overestimate the probability of success, PE willingness to pay exceeds strategic willingness to pay because PE can exploit overvalued debt more directly.

## 9. Contribution to the Literature
This paper contributes to:
1. [[M&A]] by explaining why acquirer type varies across merger waves.
2. [[Private Equity]] by linking buyout activity to debt misvaluation, not just cheap credit or fundraising.
3. [[Capital Structure]] by showing how mispriced debt affects ownership structure and asset allocation.
4. [[Corporate Governance]] by modeling how PE monitoring interacts with overvalued debt and moral hazard.

It differs from prior work because it focuses on financial versus strategic buyer dominance rather than only total merger volume, bidder premiums, or equity misvaluation.

## 10. Closely Related Papers
- [[Harford 2005]]: Merger waves require economic shocks plus capital liquidity.
- [[Rhodes-Kropf and Viswanathan 2004]]: Equity misvaluation can drive merger waves through stock-financed acquisitions.
- [[Shleifer and Vishny 2003]]: Stock market misvaluation affects merger activity.
- [[Axelson, Jenkinson, Stromberg, and Weisbach 2013]]: Buyout leverage and pricing are strongly related to debt market conditions.
- [[Kaplan and Stromberg 2009]]: Overview of private equity governance, leverage, and value creation.
- [[Gorbenko and Malenko 2014]]: Strategic and financial bidders differ because strategic bidders seek synergies while financial buyers seek undervalued assets.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on merger waves and private equity activity. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Debt overvaluation shifts acquisitions toward private equity buyers.
- Data: SDC M&A transactions, Moody's rating accuracy data, Compustat, macro controls.
- Identification: Mostly theory plus supportive correlations using a novel debt misvaluation proxy.
- Limitation: The empirical design is not a clean causal design.
- Connection to other papers: Complements [[Harford 2005]] on liquidity-driven merger waves and [[Rhodes-Kropf and Viswanathan 2004]] on misvaluation-driven merger activity.
- Best exam phrase: "Martos-Vila, Rhodes-Kropf, and Harford show that debt misvaluation changes not only the level of M&A, but also who owns the assets."

## 12. Hypotheses Inspired by This Paper
H1: Debt market overvaluation increases the share of acquisitions completed by PE buyers relative to strategic buyers.

H2: The effect of debt overvaluation on PE activity is stronger when the relevant strategic alternative is a diversifying conglomerate acquirer.

H3: The effect of debt overvaluation on PE activity is stronger when debt issuance is high and targets require external financing.

## 13. Possible Extension or Research Design
- Research question: Does debt market overvaluation affect whether targets are acquired by PE buyers versus strategic buyers in modern leveraged loan markets?
- Hypothesis: PE buyer dominance rises when leveraged loan or private credit markets become overpriced relative to realized default risk.
- Data: SDC or Refinitiv M&A data, leveraged loan issuance data, CLO demand measures, ratings transitions, post-deal leverage, realized default outcomes.
- Identification: Use plausibly exogenous shocks to credit supply, such as CLO demand shocks, regulatory capital changes, or institutional investor flows into private credit.
- Expected result: PE acquirers gain share when debt is unusually cheap, especially for targets with low internal cash, high collateral value, and low strategic synergy.
- Contribution: Extends the paper from public bond rating misvaluation to the modern private credit and leveraged loan environment.

## 14. Critiques

### Major Concern 1
The empirical proxy for debt overvaluation is ex post Moody's Average Position. A low AP may indicate that rating agencies made mistakes, but it does not prove that bond investors mispriced debt at issuance.

### Major Concern 2
PE activity may increase because PE funds have more dry powder or because strategic acquirers are constrained, not because PE buyers uniquely exploit debt misvaluation. The paper partly addresses this with fundraising controls, but causal separation remains difficult.

### Minor Concern
The model is stylized and treats PE monitoring as a clean governance advantage. In practice, PE governance, operational expertise, tax benefits, and target selection may all contribute to PE willingness to pay.

### Referee Recommendation
R&R / Accept, because the theory is novel and exam-useful, and the empirical evidence is aligned with the model's sharp predictions, but the empirical design should be interpreted as supportive rather than causal.

## 15. Memory Hooks
- "Debt misvaluation changes the owner, not just the deal count."
- "PE can exploit cheap debt more directly than strategic buyers."
- "Coinsurance helps real default risk but reduces mispricing rents."
- "Monitoring plus overvaluation relaxes PE financing constraints."
- "Low Moody's AP means high debt overvaluation and more PE activity."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[M&A]], [[Private Equity]], [[Capital Structure]], [[Merger Waves]], [[Market Timing]], or [[Corporate Governance]]. The clean exam answer is: "Martos-Vila, Rhodes-Kropf, and Harford use a theory of debt misvaluation and supportive M&A evidence to show that overvalued debt shifts acquisitions toward PE buyers because PE can exploit cheap debt through leverage and monitoring, while strategic buyers lose some mispricing rents through coinsurance." Use it to argue that financial market mispricing can affect real asset ownership, not just security issuance. In a critique answer, emphasize that Moody's AP is an ex post proxy and not a randomized shock, but note that the paper is stronger than a standard correlation because the PE versus conglomerate result maps tightly to the model's coinsurance mechanism.