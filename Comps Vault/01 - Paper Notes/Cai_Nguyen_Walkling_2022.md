---
type: paper
status: unread
title: 'Director Appointments: It Is Who You Know'
authors: Jay Cai, Tu Nguyen, Ralph Walkling
year: 2022
journal: Review of Financial Studies
professor: DrJandik
seminar: null
jandik_paper_number: 23
jandik_week: 6
jandik_topic: Networks in corporate finance
jandik_done: true
field: Corporate Finance
literature:
- '[[Corporate Governance]]'
- '[[Managerial and Social Networks]]'
- Director Labor Market
methods:
- Logit
- Event Study
- 2SLS
- Instrumental Variables
- Shareholder Voting Regressions
datasets:
- '[[BoardEx]]'
- '[[Compustat]]'
- '[[CRSP]]'
- '[[RiskMetrics]]'
identification: Death-induced network loss and merger-induced network gain as instruments for connected director appointments
main_result: Connected directors are much more likely to be appointed, especially when coordination and search costs are high, but CEO-connected appointees are viewed negatively by markets and shareholders.
exam_relevance: high
must_memorize: true
tags:
- corporate-governance
- boards
- director-labor-market
- social-networks
- instrumental-variables
created: 2026-06-04
updated: 2026-06-04
---

# Cai, Nguyen, and Walkling 2022

## 1. One-Sentence Takeaway
This paper shows that board networks strongly shape outside director appointments using 9,801 uncontested director appointments from 2003 to 2014, and the main contribution is to show that director connections can create value through coordination and search-cost channels but destroy value when they reflect CEO cronyism.

## 2. Exam-Ready Abstract
Cai, Nguyen, and Walkling study how incumbent board networks affect the appointment of outside directors. Using BoardEx director appointment data from 2003 to 2014 matched to Compustat, CRSP, and ISS voting data, they show that 69% of new directors have professional ties to incumbent boards, even though connected candidates represent only about 13% of the potential director pool. The paper tests whether connections reflect efficient coordination, lower search costs, homophily, or agency problems. Connected candidates are more likely to be appointed, and connections help boards add female directors, new skills, and new industry backgrounds. Market reactions and shareholder votes are more positive for connected appointments at complex firms and firms facing more competitive environments, consistent with coordination and search-cost benefits. However, CEO-connected appointments receive lower announcement returns and shareholder votes, consistent with agency costs. This paper connects to [[Corporate Governance]], [[Boards of Directors]], [[Social Networks]], [[Board Diversity]], and [[Agency Problems]].

## 3. Research Question
What role do professional connections between director candidates and incumbent boards play in director appointments?

More specifically, the paper asks whether connected director appointments reflect:
1. efficient coordination among board members,
2. lower search and information costs in the opaque director labor market,
3. homophily and groupthink,
4. agency problems from CEO influence over board nominations.

## 4. Core Mechanism
Use a chain that can be memorized for comps:

```text
Opaque director labor market
-> boards rely on professional networks
-> connections reduce information asymmetry and coordination costs
-> connected candidates are more likely to be appointed
-> appointments are value-enhancing when firm complexity or competition makes coordination valuable
```

Agency version:

```text
CEO influence over board nominations
-> CEO-connected candidate enters board network
-> monitoring independence falls
-> shareholders perceive cronyism
-> lower announcement returns and lower shareholder votes
```

## 5. Main Findings
1. Connections dominate director appointments: about 69% of new outside directors are professionally connected to the incumbent board, while the average board is connected to only about 13% of the potential BoardEx director pool.
2. Connected candidates are more likely to be appointed, and connections facilitate diversity by increasing the odds of appointing women to all-male boards, candidates with new skills, and candidates from different industries.
3. Connected appointments are valued more positively when coordination and search costs are high, especially in complex firms and competitive environments, but CEO-connected appointments receive lower announcement returns and lower shareholder votes.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Outside director appointment and director candidate |
| Sample period | 2003 to 2014 |
| Main dataset | BoardEx director appointments and professional networks |
| Other datasets | Compustat, CRSP, RiskMetrics ISS voting data |
| Sample | 9,801 uncontested outside director appointments |
| Shareholder-vote sample | 6,559 appointments with ISS voting data |
| Key variables | Connected appointee, first-degree tie, second-degree tie, CEO-connected tie, board complexity, product market fluidity, shareholder votes, announcement returns |
| Treatment or shock | Appointment of a director connected to the incumbent board |
| Instruments | Death-induced network loss and merger-induced network gain |
| Outcome variables | Appointment probability, announcement abnormal returns, excess shareholder votes, board diversity outcomes |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between connected appointments and firm value is not causal because firms do not randomly appoint directors. High-quality firms may attract better-connected candidates, complex firms may both need connected directors and have different returns, and CEOs may strategically select friends when governance is weak. Director quality, candidate willingness to serve, firm complexity, board culture, and unobserved governance quality could all affect both the likelihood of appointing a connected director and the market reaction. There is also equilibrium sorting: directors and firms match through networks, so observed connections may proxy for unobservable fit rather than causal effects of connections.

### Identification Approach
- Natural experiment: Shocks to the board's available network from deaths and mergers.
- Instrument:  
  1. Network loss from deaths of connected directors or executives outside the appointing firm.  
  2. Network gain from mergers completed by firms connected to the appointing firm.
- Difference in differences: Not the central design.
- Event study: Three-day abnormal returns around director appointment announcements.
- Fixed effects: Year and industry fixed effects in key specifications.
- Matching: Candidate-choice design compares appointed directors with plausible counterfactual candidates appointed around the same time to similarly sized firms in the same MSA.
- Placebo tests: Not clear from provided text.
- Robustness: Uses shareholder votes, ISS recommendations, institutional voting, different definitions of networks, and overidentification tests.
- Alternative source of variation: Departing-director bad-term departures and recommender reputation for second-degree ties.

### Is the Identification Convincing?
- Strength: The IV strategy is creative because deaths contract networks and mergers expand networks in ways plausibly unrelated to the value of a later appointment except through the availability of connected candidates.
- Weakness: The exclusion restriction is debatable. Director deaths or M&A activity in a firm's network could proxy for broader industry, network, or elite labor-market shocks.
- Referee concern: Network shocks may affect firm information environments or director labor-market quality beyond the appointment of a connected director. The instruments are stronger for appointment availability than for shareholder-value interpretation.

## 8. Main Regression or Model

Candidate appointment model:

```text
Appointed_ij =
  beta Connected_ij
+ gamma CandidateControls_ij
+ delta FirmBoardControls_j
+ Year FE
+ Industry FE
+ epsilon_ij
```

This model asks whether candidate i is more likely to be appointed by firm j when candidate i has a professional connection to the incumbent board. The key coefficient is beta, which captures whether connected candidates are more likely to be selected from a pool of plausible candidates.

Value and voting model:

```text
Outcome_j =
  beta1 ConnectedAppointee_j
+ beta2 ConnectedAppointee_j x CoordinationNeed_j
+ gamma Controls_j
+ Year FE
+ Industry FE
+ epsilon_j
```

The outcome is either announcement abnormal returns or excess shareholder votes. `beta1` captures the average valuation or voting effect of a connected appointment. `beta2` captures whether connected directors are more valuable when coordination needs are high, such as in complex firms, large boards, fast-growing industries, or competitive product markets.

Instrumental-variable version:

```text
ConnectedAppointee_j =
  pi1 DeathInducedNetworkLoss_j
+ pi2 MergerInducedNetworkGain_j
+ Controls_j
+ error_j

Outcome_j =
  beta PredictedConnectedAppointee_j
+ Controls_j
+ error_j
```

The first stage uses exogenous network contractions and expansions to predict whether the appointed director is connected. The second stage asks whether the predicted connected appointment affects announcement returns or shareholder votes.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Corporate Governance]] by showing how boards actually select directors in an opaque market.
2. [[Social Networks]] by distinguishing beneficial professional ties from agency-driven CEO ties.
3. [[Board Diversity]] by showing that networks can help boards appoint women, new skills, and new industry backgrounds rather than merely reinforcing homogeneity.

It differs from prior work because it focuses on whether the appointed director is connected to the incumbent board, not just whether the director is generally well connected.

## 10. Closely Related Papers
- [[Hermalin and Weisbach 1998]]: Theory of endogenous board composition and CEO influence over board structure.
- [[Shivdasani and Yermack 1999]]: CEO involvement in director selection and weaker monitoring.
- [[Fracassi and Tate 2012]]: CEO-director social ties and agency costs.
- [[Coles, Daniel, and Naveen 2014]]: Co-opted boards and weakened monitoring.
- [[Adams and Ferreira 2009]]: Board diversity, monitoring, and firm outcomes.
- [[Cai, Garner, and Walkling 2009]]: Shareholder voting in director elections.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on boards of directors and corporate governance. Discuss how board composition is determined and how papers establish causality.

How to use this paper:
- Main finding: Board appointments are heavily network-driven, but connections can be efficient or agency-driven depending on who is connected and the firm's needs.
- Data: BoardEx director appointments from 2003 to 2014, matched with Compustat, CRSP, and RiskMetrics ISS.
- Identification: Candidate-choice logit design plus IVs based on death-induced network loss and merger-induced network gain.
- Limitation: The IV exclusion restriction is plausible but not airtight because network shocks may correlate with broader director labor-market conditions.
- Connection to other papers: Use with CEO-board agency papers, board diversity papers, and social-network governance papers.
- Best exam phrase: "Cai, Nguyen, and Walkling show that board networks are not automatically bad governance. They are valuable when they reduce search and coordination costs, but costly when they connect new directors to the CEO."

## 12. Hypotheses Inspired by This Paper
H1: Connected director appointments are more value-enhancing in firms with high information-processing needs, such as firms with more segments, faster product-market change, or higher technological complexity.

H2: CEO-connected director appointments are associated with weaker future monitoring, lower CEO turnover-performance sensitivity, and more favorable CEO compensation.

H3: Network-based appointments can increase board diversity when underrepresented candidates face greater information asymmetry or uncertainty about board fit.

## 13. Possible Extension or Research Design
- Research question: Do connected director appointments affect firms' responses to major strategic shocks?
- Hypothesis: Connected appointments improve speed and coherence of decision-making after shocks, but CEO-connected appointments weaken monitoring.
- Data: BoardEx director appointments, RavenPack or Factiva firm news shocks, Compustat outcomes, CRSP returns, ExecuComp CEO turnover and pay.
- Identification: Use death-induced network loss and merger-induced network gain as instruments for connected appointments, then examine post-appointment responses to exogenous shocks such as supply-chain disruptions or regulatory changes.
- Expected result: Professionally connected non-CEO appointments improve response speed and operating outcomes after shocks, while CEO-connected appointments reduce discipline.
- Contribution: Links board-network structure to real corporate flexibility and crisis response.

## 14. Critiques

### Major Concern 1
The exclusion restriction for the instruments is contestable. Deaths and mergers in the board network may affect more than the availability of connected candidates. They could alter the quality of information, the elite director labor market, or industry-level network structure.

### Major Concern 2
The market reaction tests identify investor perceptions of value, not necessarily long-run causal effects on firm performance. Announcement returns can be noisy for director appointments and may reflect signaling rather than actual governance improvements.

### Minor Concern
The paper focuses on professional ties and largely sets aside educational and social ties because they are much less common and often overlap with professional ties. That is empirically reasonable, but it may understate informal social channels.

### Referee Recommendation
Accept, because the paper documents a first-order fact about the director labor market, provides a strong theoretical framing around coordination, search costs, homophily, and agency, and uses a creative IV strategy to move beyond simple correlations.

## 15. Memory Hooks
- "The best way to get on a board is to know someone on a board."
- 69% of appointed directors are professionally connected to incumbent boards.
- Connections are good when they solve coordination and search-cost problems.
- CEO connections are bad because they look like cronyism.
- Deaths shrink networks, mergers expand networks.

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Corporate Governance]], [[Boards of Directors]], [[Director Labor Market]], [[Social Networks]], [[Board Diversity]], or [[Agency Problems]]. The clean exam answer is: "Cai, Nguyen, and Walkling use BoardEx director appointments and network shocks from deaths and mergers to show that board connections strongly predict director appointments and can create value when they reduce coordination and search costs." Use it to argue that social ties in governance are not inherently bad: the same connection can either improve board function or entrench management depending on whether the tie is to the board broadly or to the CEO specifically. In a critique answer, emphasize the exclusion restriction of the network-shock instruments, but note that the paper is stronger than a standard correlation because it combines plausible counterfactual candidate pools, announcement returns, shareholder votes, and instrumental variables.
