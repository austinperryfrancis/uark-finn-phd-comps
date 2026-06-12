---
type: paper
status: unread
title: Institutional Investor Cliques and Governance
authors: Alan D. Crane, Andrew Koch, Sébastien Michenaud
year: 2019
journal: Journal of Financial Economics
seminar: Not clear from provided text
field: corporate finance
literature:
  - Corporate Governance
  - Institutional Investors
  - Shareholder Activism
  - Market Liquidity and Governance
methods:
  - institutional ownership networks
  - shareholder voting regressions
  - instrumental variables
  - difference in differences
  - liquidity shock
datasets:
  - Thomson Reuters 13F
  - ISS voting data
  - CRSP
  - Compustat
  - SEC 13D filings
  - ExecuComp
  - SDC
identification: 2003 mutual fund trading scandal as a shock to institutional investor networks, plus decimalization as a liquidity shock
main_result: Investor coordination strengthens governance by voice but weakens governance by threat of exit.
exam_relevance: high
must_memorize: true
tags:
  - corporate-governance
  - institutional-investors
  - shareholder-activism
  - ownership-networks
  - voice
  - exit
  - DrJandik
created: 2026-06-12
updated: 2026-06-12
---

# Crane, Koch, and Michenaud 2019

## 1. One-Sentence Takeaway
This paper shows that institutional investor coordination improves governance through voice but weakens governance through exit using ownership-network cliques, and the main contribution is showing that coordinated owners can substitute for concentrated blockholders while creating a governance trade-off.

## 2. Exam-Ready Abstract
Crane, Koch, and Michenaud ask whether institutional investors coordinate with each other and whether that coordination improves corporate governance. They identify investor cliques from the network of 13F institutional holdings, where two institutions are connected if they each hold at least 5% in a common firm, and cliques are highly connected groups found using the Louvain community-detection algorithm. They show that clique members vote together, oppose low-quality management proposals, and are more likely to make joint Schedule 13D filings. To address selection, they use the 2003 mutual fund trading scandal as a shock that disrupted investor networks and reduced clique ownership for exposed firms. The main result is a trade-off: clique ownership increases governance through voice, especially voting against bad proposals, but reduces governance through threat of exit because clique owners sell more slowly and firm value responds less positively to liquidity shocks. The paper connects directly to [[Corporate Governance]], [[Institutional Investors]], [[Shareholder Activism]], and [[Market Liquidity and Governance]].

## 3. Research Question
Does coordination among institutional investors affect corporate governance?

More specifically, the paper tests whether investor coordination:
1. Reduces free-rider problems and strengthens governance through voice.
2. Weakens the threat of exit because coordinated investors unwind positions slowly to reduce price impact.
3. Substitutes for traditional block ownership as institutional ownership becomes more dispersed.

## 4. Core Mechanism
```text
Dispersed institutional ownership
-> individual investors have weak incentives to monitor alone
-> investor cliques coordinate across overlapping ownership networks
-> coordinated investors vote together and oppose bad management proposals
-> stronger governance through voice

But:
Investor cliques can coordinate trading
-> investors sell slowly to minimize price impact
-> managers face a weaker threat of rapid price discipline
-> weaker governance through exit
```

## 5. Main Findings
1. Clique ownership increases shareholder opposition to bad management proposals. A one standard deviation increase in clique ownership raises votes against bad management proposals by about 6.2 percentage points, relative to an unconditional average of 5.8%.
2. The 2003 mutual fund trading scandal provides plausibly exogenous variation in clique ownership. IV results support a causal interpretation that clique ownership increases voting against management, especially for low-quality proposals.
3. Coordination has a trade-off. Clique members exit positions more slowly, and firm value responds less positively to the decimalization liquidity shock when clique ownership is high, implying weaker governance through threat of exit.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Institution-year, firm-year, ballot item, institution-stock-quarter, and firm-year around liquidity shocks |
| Sample period | Main 13F sample: 1980 to 2013. Voting data: 2003 to 2013. Decimalization tests use 2000 and 2002, excluding 2001. |
| Main dataset | Thomson Reuters 13F institutional holdings, ISS voting data, CRSP, Compustat, SEC 13D filings, ExecuComp, and SDC |
| Key variables | Clique ownership, Clique Herfindahl, top clique ownership, votes against management, ISS bad proposal indicator, Davis and Kim good proposal indicator, joint 13D filings, trading autocorrelation, Tobin's q |
| Treatment or shock | 2003 mutual fund trading scandal for network disruption; decimalization for liquidity shock |
| Outcome variables | Voting against management, joint activism filings, shareholder proposals, proxy fights, payout initiations, acquisitions, divestitures, trading behavior, and Tobin's q |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between clique ownership and governance is not causal because cliques may select into firms where governance activism is already more likely. Firms with poor governance, upcoming controversial proposals, or activist-friendly investor bases may attract clique investors. There is also an omitted-variable problem: unobserved investor preferences, firm governance culture, or industry trends could drive both clique ownership and votes against management. Reverse causality is also possible if investors form or increase clique positions in anticipation of governance events. Finally, the clique measure could capture correlated information or common preferences rather than actual coordination.

### Identification Approach
- Natural experiment: The 2003 mutual fund trading scandal disrupted institutional investor networks by causing outflows and closures among implicated mutual fund families.
- Instrument: Firm-level exposure to the scandal through ownership by institutions connected to scandal funds. Treatment is interacted with the post-scandal period to instrument for clique ownership.
- Difference in differences: Voting outcomes are compared before and after the scandal for firms with higher versus lower exposure to the network shock.
- Event study: Not clear from provided text for the voting tests. The decimalization analysis uses a before-after liquidity shock design around 2000 and 2002.
- Fixed effects: Firm and year fixed effects in voting regressions. Institution-quarter and stock-quarter fixed effects in trading regressions. Firm fixed effects in decimalization tests.
- Matching: Not clear from provided text.
- Placebo tests: Not clear from provided text.
- Robustness: Controls for institutional ownership, blockholders, ownership concentration, institution types, firm characteristics, Tobit specification, excluding 5% positions from clique ownership, alternative clustering coefficient measures, joint 13D evidence, and Silicon Graphics class-action coordination evidence.
- Alternative source of variation: Decimalization as an exogenous liquidity shock to test governance through exit.

### Is the Identification Convincing?
- Strength: The 2003 scandal is plausibly unrelated to future voting at specific portfolio firms and affects clique ownership through investor-network disruption. The paper also triangulates with voting, 13D filings, trading behavior, and decimalization.
- Weakness: The first-stage F-statistics are modest in some specifications, especially for the good-proposal nondirector sample. The IV identifies effects from a specific network shock, so external validity may be limited.
- Referee concern: The exclusion restriction could fail if scandal-connected funds changed monitoring, voting norms, or ownership composition in ways unrelated to clique coordination.

## 8. Main Regression or Model

```text
VotesAgainst_jlt =
  beta1 CliqueOwnership_j,t-1
+ beta2 CliqueOwnership_j,t-1 x BadProposal_jlt
+ beta3 BadProposal_jlt
+ Controls_j,t-1
+ Firm FE
+ Year FE
+ epsilon_jlt
```

This regression asks whether firms with more clique ownership have more votes against management, especially when the proposal is low quality. The main coefficient is beta2. A positive beta2 means coordinated investors are more likely to oppose management when management proposals are bad.

For the IV design:

```text
CliqueOwnership_jt =
  phi1 Treatment_j x Post_t
+ phi2 Treatment_j
+ Controls_jt
+ Firm FE
+ Year FE
+ error_jt
```

```text
VotesAgainst_jlt =
  beta1 PredictedCliqueOwnership_jt
+ beta2 PredictedCliqueOwnership_jt x ProposalQuality_jlt
+ Controls_jt
+ Firm FE
+ Year FE
+ epsilon_jlt
```

The first stage uses exposure to the mutual fund scandal as a source of exogenous variation in clique ownership. The second stage tests whether the predicted component of clique ownership affects voting.

For exit governance:

```text
Q_jt =
  beta1 Decimalization_t x CliqueOwnership_j,t-1
+ beta2 Decimalization_t x BlockOwnership_j,t-1
+ Controls_j,t-1
+ Firm FE
+ epsilon_jt
```

Here beta1 captures whether the value effect of improved liquidity is weaker when ownership is more coordinated. The key result is negative beta1, meaning liquidity improves governance less when clique ownership is high.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Corporate Governance]] by showing that coordination can substitute for concentrated ownership in monitoring.
2. [[Institutional Investors]] by moving beyond investor type and block size to a network-based measure of investor interaction.
3. [[Shareholder Activism]] by identifying informal coordination before observable activism campaigns.
4. [[Market Liquidity and Governance]] by showing that coordination strengthens voice but weakens exit.

It differs from prior work because it identifies investor coordination ex ante from the ownership network rather than only observing formal activism campaigns, proxy fights, or large individual blockholders.

## 10. Closely Related Papers
- [[Shleifer and Vishny 1986]]: Theoretical benchmark for large shareholder monitoring and the free-rider problem.
- [[Edmans and Manso 2011]]: Theory that multiple independent blockholders strengthen governance through exit, while coordination weakens exit.
- [[Admati and Pfleiderer 2009]]: Exit as a governance mechanism through the Wall Street walk.
- [[Bharath, Jayaraman, and Nagar 2013]]: Empirical evidence on exit governance using liquidity shocks.
- [[Gillan and Starks 2000]]: Shareholder voting and activist governance through proxy proposals.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the literature on institutional investors and corporate governance. How do institutional investors govern firms, and what are the identification challenges in this literature?

How to use this paper:
- Main finding: Institutional investor coordination improves governance through voice but weakens governance through exit.
- Data: 13F ownership networks, ISS voting data, SEC 13D filings, CRSP, Compustat, ExecuComp, and SDC.
- Identification: Uses the 2003 mutual fund trading scandal as a shock to investor networks and decimalization as a liquidity shock.
- Limitation: Clique ownership may capture correlated preferences or information, and the IV first stage is not equally strong across all samples.
- Connection to other papers: Connect to [[Shleifer and Vishny 1986]] on blockholder monitoring, [[Edmans and Manso 2011]] on exit, and [[Bharath, Jayaraman, and Nagar 2013]] on liquidity and governance.
- Best exam phrase: "Crane, Koch, and Michenaud show that coordination solves one governance problem but creates another: it increases voice but reduces exit."

## 12. Hypotheses Inspired by This Paper
H1: Firms with higher institutional clique ownership are more likely to receive votes against low-quality management proposals.

H2: Firms with higher institutional clique ownership experience weaker governance effects from liquidity improvements because coordinated investors exit more slowly.

H3: Specialized investor cliques predict future corporate policy changes, such as dividend initiations, divestitures, and reduced acquisition activity.

## 13. Possible Extension or Research Design
- Research question: Does institutional investor coordination affect firm responses to climate-risk disclosure shocks?
- Hypothesis: Firms with higher climate-focused clique ownership are more likely to improve climate disclosure and reduce emissions after regulatory or investor-pressure shocks.
- Data: 13F holdings, investor climate coalition membership, ISS or shareholder proposal data, CDP emissions, Refinitiv ESG, and firm financials.
- Identification: Use staggered climate disclosure mandates or entry into climate coalitions as shocks to investor coordination.
- Expected result: Coordinated climate-focused investors increase voice through shareholder proposals and voting, but may weaken exit discipline if they coordinate gradual selling.
- Contribution: Extends the voice-versus-exit trade-off to ESG governance and tests whether coordination can change real corporate policies.

## 14. Critiques

### Major Concern 1
The clique measure may capture correlated information or similar preferences rather than actual coordination. The authors address this with joint 13D filings, slow coordinated trading, and weaker exit governance, but the concern is difficult to eliminate completely.

### Major Concern 2
The mutual fund scandal instrument may affect more than clique ownership. If scandal exposure changes the composition, reputation, or voting behavior of institutional owners directly, the exclusion restriction could be violated.

### Minor Concern
The Louvain algorithm approximates clique structure, so measurement error in identifying coordination is possible. This likely attenuates results, but it also makes interpretation less transparent.

### Referee Recommendation
Accept, because the paper asks an important governance question, proposes a novel ownership-network measure, uses multiple empirical settings, and offers a memorable theoretical trade-off between voice and exit.

## 15. Memory Hooks
- "Cliques are hidden blockholders."
- "Coordination solves free riding for voice."
- "Coordination kills the Wall Street walk."
- "2003 mutual fund scandal breaks the network."
- "Figure 2: institutional ownership concentration falls, clique ownership rises."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Corporate Governance]], [[Institutional Investors]], [[Shareholder Activism]], [[Ownership Structure]], or [[Market Liquidity and Governance]]. The clean exam answer is: "Crane, Koch, and Michenaud use institutional ownership networks to identify investor cliques and show that coordination increases governance through voice but weakens governance through exit." Use it to argue that institutional investors are not just isolated owners, since their network position changes how they monitor, vote, and trade. In a critique answer, emphasize selection into cliques and correlated preferences, but note that the paper is stronger than a standard correlation because it uses the 2003 mutual fund trading scandal as a network shock and confirms the mechanism with joint 13D filings, trading behavior, and decimalization tests.