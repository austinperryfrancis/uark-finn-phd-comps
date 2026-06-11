---
type: paper
status: unread
title: CEO Network Centrality and Merger Performance
authors: Rwan El-Khatib, Kathy Fogel, Tomas Jandik
year: 2015
journal: Journal of Financial Economics
seminar:
field: Corporate Finance
literature: Mergers and Acquisitions; Corporate Governance; Social Networks in Finance; Behavioral Corporate Finance
methods: Network centrality; event study; Probit; OLS; governance interactions; robustness tests
datasets: BoardEx; SDC; CRSP; Compustat; RiskMetrics; ExecuComp; Thomson Reuters insider filings
identification: Cross-sectional variation in CEO network centrality with event-study outcomes and controls
main_result: High-centrality CEOs make more acquisitions, but those acquisitions have lower acquirer returns and lower combined synergies.
exam_relevance: high
must_memorize: true
tags:
  - corporate-finance
  - mergers
  - governance
  - social-networks
  - ceo-traits
created:
updated:
---

# El-Khatib, Fogel, and Jandik 2015

## 1. One-Sentence Takeaway
This paper shows that highly central CEOs make more acquisitions but generate worse acquirer and combined-firm announcement returns using BoardEx network measures and S&P 1500 M&A data, and the main contribution is showing that social-network position can increase CEO entrenchment rather than improve decision quality.

## 2. Exam-Ready Abstract
El-Khatib, Fogel, and Jandik ask whether a CEO's position in the executive social network affects merger decisions and merger performance. The setting is U.S. S&P 1500 acquirers buying public U.S. targets from 2000 to 2009, with CEO centrality measured from BoardEx using closeness, degree, betweenness, and eigenvector centrality. The core hypothesis is ambiguous: central CEOs may have better private information, but they may also have more power to push deals through and avoid discipline. They find the negative governance channel dominates. High-centrality CEOs are more likely to complete acquisitions, but those deals produce lower bidder CARs and lower combined-firm synergies. Internal governance only partly constrains deal frequency and does little to eliminate value loss, while the markets for corporate control and executive labor discipline high-centrality CEOs less effectively. This paper connects to [[Mergers and Acquisitions]], [[Corporate Governance]], [[Social Networks in Finance]], and [[Behavioral Corporate Finance]].

## 3. Research Question
What is the paper trying to answer?

Does CEO network centrality affect acquisition frequency and acquisition performance?

More specifically: does the informational advantage of central CEOs improve M&A outcomes, or does their social power allow them to entrench themselves, override monitoring, and pursue value-destroying acquisitions?

## 4. Core Mechanism

```text
CEO has high network centrality
-> CEO has more information access, influence, and bargaining power
-> board members and external monitors are less able or willing to constrain the CEO
-> CEO completes more acquisitions and receives private benefits
-> acquirer shareholders and the combined entity experience lower announcement returns
```

## 5. Main Findings
1. High-centrality CEOs are more likely to make acquisitions. Moving from the 25th to the 75th percentile of CEO centrality increases acquisition frequency by about 28%.
2. High-centrality CEOs generate worse M&A outcomes. Moving from the 25th to the 75th percentile reduces acquirer CARs by about 3.42 percentage points and combined-firm synergies by about 3.06 percentage points.
3. Governance and external discipline do not fully solve the problem. Internal governance partly reduces acquisition frequency, but high-centrality CEOs are less disciplined by takeover markets and CEO turnover after value-destroying deals.
4. The evidence supports an entrenchment and private-benefits interpretation. High-centrality CEOs receive higher compensation and more non-monetary awards after acquisitions, even when shareholder returns are poor.
5. The results are robust to controls for CEO overconfidence, bidder size, CEO-board ties, bidder-target board ties, and alternative centrality definitions.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Firm-year for acquisition likelihood; deal for announcement returns; CEO-deal for compensation and awards |
| Sample period | CEO centrality from 1999 to 2008; completed M&A deals from 2000 to 2009 |
| Main dataset | BoardEx for CEO networks; SDC for mergers; CRSP for returns; Compustat for accounting data; RiskMetrics and ExecuComp for governance and compensation |
| Key variables | CEO closeness, degree, betweenness, and eigenvector centrality; acquisition indicator; bidder CAR; combined CAR; governance variables |
| Treatment or shock | No clean shock. Main variation is CEO position in the social network |
| Outcome variables | Acquisition likelihood, acquirer announcement CAR, combined-firm CAR, post-deal takeover likelihood, CEO turnover, compensation, awards, insider sales |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between CEO centrality and merger outcomes is not causal because central CEOs differ from peripheral CEOs in many ways. Central CEOs may run larger firms, have better growth opportunities, have different compensation contracts, be more talented, be more overconfident, or be selected by firms that already plan to pursue acquisitions. Firm size is especially important because larger acquirers tend to have lower acquisition returns in the M&A literature. There is also possible reverse causality: CEOs who pursue many deals may become more central over time. Measurement error is possible because BoardEx captures observable professional, educational, and social connections, not the true quality or strength of all CEO relationships.

### Identification Approach
- Natural experiment: No clean natural experiment.
- Instrument: No instrument.
- Difference in differences: Not the main design.
- Event study: Yes. The paper uses announcement-window CARs around M&A announcements to measure market-assessed value creation or destruction.
- Fixed effects: Uses year and industry effects in the main return regressions. Not a firm fixed effects design.
- Matching: Used in the CEO awards analysis, where bidder CEOs are matched to non-bidding CEOs by year, industry, and size.
- Placebo tests: Not a classic placebo design, but the paper uses multiple robustness tests.
- Robustness: Controls for firm characteristics, deal characteristics, governance, CEO overconfidence, bidder size, CEO-board ties, bidder-target board ties, alternative centrality measures, principal components, and orthogonalized centrality measures.
- Alternative source of variation: Cross-sectional variation in network centrality across CEOs.

### Is the Identification Convincing?
- Strength: Strong descriptive and event-study evidence that network position matters beyond bilateral ties. The paper uses multiple centrality measures and addresses obvious confounds like size, overconfidence, and governance.
- Weakness: It is not a clean causal design. Centrality is not randomly assigned, and it may proxy for latent CEO ambition, prestige, firm complexity, or access to acquisition opportunities.
- Referee concern: The strongest concern is omitted CEO quality or firm strategy. High-centrality CEOs may be selected into firms with larger, more complex, or riskier acquisition programs.

## 8. Main Regression or Model

```text
Pr(Deal_it = 1) =
  alpha_t
+ beta Centrality_i,t-1
+ gamma FirmControls_i,t-1
+ epsilon_it
```

This Probit model asks whether firms with more central CEOs are more likely to announce and complete acquisitions. The coefficient beta measures whether CEO network centrality predicts acquisition likelihood after controlling for firm size, Tobin's Q, liquidity, profitability, and leverage.

```text
CAR_i =
  beta Centrality_i
+ gamma FirmControls_i
+ delta DealControls_i
+ Industry FE
+ Year FE
+ epsilon_i
```

This deal-level model asks whether acquisition announcement returns are lower when the bidder CEO is more central. The dependent variable is either bidder CAR or combined CAR over the event window. The main coefficient is beta. A negative beta means that higher CEO centrality is associated with lower market-assessed acquisition value.

```text
CAR_i =
  beta1 HighCentrality_i
+ beta2 Governance_i
+ beta3 HighCentrality_i x Governance_i
+ Controls_i
+ Industry FE
+ Year FE
+ epsilon_i
```

This interaction model asks whether stronger governance mitigates the negative effect of CEO centrality. The key coefficient is beta3, but the paper generally finds that governance has limited power to prevent value destruction by high-centrality CEOs.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Social Networks in Finance]] by shifting attention from bilateral ties to the CEO's position in the entire executive network.
2. [[Mergers and Acquisitions]] by showing that CEO social status predicts both acquisition frequency and acquisition value destruction.
3. [[Corporate Governance]] by showing that central CEOs can partly avoid internal and external discipline.
4. [[Behavioral Corporate Finance]] by treating network centrality as a measurable CEO trait linked to corporate decisions.

It differs from prior work because it studies hierarchy and power in the network, not just whether two parties are connected.

## 10. Closely Related Papers
- [[Malmendier and Tate 2008]]: CEO overconfidence and value-destroying acquisitions.
- [[Masulis, Wang, and Xie 2007]]: Governance and acquirer returns.
- [[Harford and Li 2007]]: CEO compensation and acquisition performance.
- [[Cai and Sevilir 2012]]: Board connections between acquirer and target can reduce information asymmetry in M&A.
- [[Ishii and Xuan 2014]]: Social ties between acquirer and target can weaken due diligence and destroy value.
- [[Fracassi and Tate 2012]]: CEO-director ties weaken monitoring.
- [[Moeller, Schlingemann, and Stulz 2004]]: Large acquirers have lower acquisition returns.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the literature on CEO traits, social networks, and merger performance. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: CEOs with higher network centrality make more acquisitions but generate lower bidder and combined-firm announcement returns.
- Data: BoardEx network data, SDC M&A data, CRSP returns, Compustat accounting data, RiskMetrics governance data, ExecuComp compensation data.
- Identification: Event-study announcement returns combined with Probit and OLS regressions using centrality measures and extensive controls.
- Limitation: Centrality is endogenous and not randomly assigned.
- Connection to other papers: Use with [[Malmendier and Tate 2008]], [[Masulis, Wang, and Xie 2007]], [[Harford and Li 2007]], [[Cai and Sevilir 2012]], and [[Ishii and Xuan 2014]].
- Best exam phrase: "El-Khatib, Fogel, and Jandik show that social networks can be a governance liability: central CEOs have more information, but also more power to entrench themselves."

## 12. Hypotheses Inspired by This Paper
H1: Firms led by CEOs with higher network centrality are more likely to initiate acquisitions than otherwise similar firms.

H2: Acquisitions initiated by high-centrality CEOs generate lower bidder announcement returns than acquisitions initiated by low-centrality CEOs.

H3: Strong external monitoring, such as activist ownership or institutional blockholders, weakens the negative relation between CEO centrality and acquisition returns.

## 13. Possible Extension or Research Design
- Research question: Does CEO network centrality affect how firms respond to activist intervention in M&A policy?
- Hypothesis: Activist intervention reduces acquisition frequency and improves acquisition quality more for high-centrality CEOs than for low-centrality CEOs.
- Data: BoardEx CEO networks, 13D activist filings, SDC M&A data, CRSP announcement returns, Compustat controls.
- Identification: Difference in differences around activist entry, comparing high-centrality and low-centrality CEOs before and after activist intervention.
- Expected result: Activists constrain high-centrality CEOs by increasing the cost of value-destroying empire building.
- Contribution: Converts the paper's centrality-governance channel into a cleaner design using an external monitoring shock.

## 14. Critiques

### Major Concern 1
CEO centrality is endogenous. It may proxy for CEO skill, ambition, prestige, firm complexity, acquisition opportunities, or board quality. Even with many controls, the paper cannot fully prove that centrality itself causes value destruction.

### Major Concern 2
The mechanism is difficult to isolate. Centrality may reflect information access, power, social status, overconfidence, or labor-market reputation. The paper argues that entrenchment dominates information benefits, but the empirical design cannot perfectly separate these channels.

### Minor Concern
BoardEx ties may not capture the true strength of relationships. A weak recorded tie and a deep personal tie may receive similar network treatment, while important informal ties may be missing.

### Referee Recommendation
R&R, because the idea is important and the evidence is broad and compelling, but the paper should be careful not to overstate causality. The strongest version is a governance and mechanism paper, not a clean causal identification paper.

## 15. Memory Hooks
- "Central CEOs do more deals, worse deals."
- "Network position beats bilateral ties."
- "Information access loses to entrenchment."
- "BoardEx plus SDC plus CRSP."
- "High centrality weakens discipline from boards, takeover markets, and CEO labor markets."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Mergers and Acquisitions]], [[Corporate Governance]], [[Social Networks in Finance]], [[CEO Traits]], or [[Behavioral Corporate Finance]]. The clean exam answer is: "El-Khatib, Fogel, and Jandik use BoardEx network centrality as a measure of CEO social power and show that high-centrality CEOs make more acquisitions but generate lower bidder and combined-firm announcement returns." Use it to argue that social connections can either reduce information asymmetry or weaken governance, and in M&A the governance-cost channel appears to dominate. In a critique answer, emphasize that centrality is endogenous, but note that the paper is stronger than a standard correlation because it uses event-study outcomes, multiple centrality measures, governance controls, and robustness checks for size, overconfidence, and bilateral board ties.