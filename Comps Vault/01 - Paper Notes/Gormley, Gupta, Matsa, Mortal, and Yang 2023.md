---
type: paper
status: unread
title: 'The Big Three and Board Gender Diversity: The Effectiveness of Shareholder Voice'
authors: Todd A. Gormley, Vishal K. Gupta, David A. Matsa, Sandra C. Mortal, Lukai Yang
year: 2023
journal: Journal of Financial Economics
professor: DrJandik
seminar: null
jandik_paper_number: 59
jandik_week: 15
jandik_topic: Governance
jandik_done: false
field: Corporate Finance
literature:
- '[[Corporate Governance]]'
- Institutional Investors
- Board Diversity
- ESG
methods:
- Difference-in-differences
- event study
- triple differences
- fixed effects
datasets:
- '[[BoardEx]]'
- Thomson Reuters 13F
- '[[CRSP]]'
- '[[ISS Voting Analytics]]'
- MSCI ESG KLD
identification: Cross-sectional variation in 2016 Big Three ownership interacted with post-2016 campaign period
main_result: Big Three gender-diversity campaigns substantially increased female board representation and pushed firms to broaden director search criteria.
exam_relevance: high
must_memorize: true
tags:
- corporate-governance
- institutional-investors
- board-diversity
- shareholder-voice
- esg
created: 2026-06-12
updated: 2026-06-12
---

# Gormley, Gupta, Matsa, Mortal, and Yang 2023

## 1. One-Sentence Takeaway
This paper shows that the Big Three's 2017 board gender-diversity campaigns increased female board representation using pre-campaign Big Three ownership as cross-sectional exposure, and the main contribution is showing that large index investors can use shareholder voice to create broad, substantive governance change.

## 2. Exam-Ready Abstract
Gormley, Gupta, Matsa, Mortal, and Yang study whether shareholder voice by large passive institutions can change corporate board composition. The setting is the 2017 campaigns by State Street, Vanguard, and BlackRock to increase gender diversity on U.S. public company boards. The empirical design compares firms with different levels of Big Three ownership in 2016 before and after the campaigns, using firm and year fixed effects. Firms with greater Big Three ownership added more female directors, retained more female directors, and became more likely to have at least one woman on the board. The response was not mere tokenism because female directors became more likely to chair or serve on important committees, especially nominating committees. Mechanism tests suggest boards expanded search beyond existing CEO and director networks and placed less emphasis on CEO experience. This paper connects to [[Corporate Governance]], [[Institutional Investors]], [[Board Diversity]], and [[ESG Activism]].

## 3. Research Question
Can large index investors use shareholder voice to induce firms to increase board gender diversity?

More specifically: do the Big Three's campaigns change board composition because their voting power pressures firms to broaden director search processes, relax traditional executive-experience requirements, and elevate women into substantive board roles?

## 4. Core Mechanism
Use this chain for comps:

```text
Big Three gender-diversity campaign and threat of negative votes
-> firms with higher Big Three ownership face stronger voting pressure
-> boards expand candidate searches beyond existing networks and CEO-only profiles
-> firms add and retain more female directors
-> female board representation and substantive committee influence increase
```

## 5. Main Findings
1. Firms with higher 2016 Big Three ownership increased female board representation after the campaigns. One standard deviation higher Big Three ownership is associated with a 76% increase in the net flow of female directors and an 11% increase in the female director share.
2. The effect is tied to the campaigns' timing and targeting. State Street ownership matters earlier, Vanguard and BlackRock matter later, and effects are stronger among firms targeted by each institution's stated policy.
3. The response went beyond tokenism. Female directors became more likely to chair committees, especially nominating and audit committees, and firms added women from outside existing board networks and with less CEO experience.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Firm-year for board diversity outcomes; director-firm-year for committee roles and new-director characteristics |
| Sample period | Main outcomes 2014-2019; BoardEx data from 2013-2019 used to construct changes |
| Main dataset | BoardEx for board composition, gender, experience, and connections |
| Ownership data | Thomson Reuters 13F, Big Three ownership measured at end of 2016 and scaled by CRSP market value |
| Voting data | ISS Voting Analytics for Big Three votes against directors |
| Key variables | Big3_2016, StateStreet_2016, Vanguard_2016, BlackRock_2016, Post2016, female director share, change in number of female directors |
| Treatment or shock | 2017 Big Three gender-diversity campaigns and voting-policy threats |
| Outcome variables | Female director share, net change in female directors, new female director hiring, female director departures, committee roles, director connections, CEO experience |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between Big Three ownership and board diversity is not causal. Big Three ownership is higher in larger firms and firms in major indexes, and these firms may face more public scrutiny, stronger labor-market pressure, different governance norms, or greater exposure to the Me Too movement. There could also be omitted firm culture, prior diversity commitment, or investor sorting into firms that were already likely to diversify. Reverse causality is less severe because ownership is measured before the campaigns, but selection into high Big Three ownership remains the key concern.

### Identification Approach
- Natural experiment: The 2017 public Big Three campaigns create a sharp change in shareholder pressure.
- Instrument: None.
- Difference in differences: Compare pre-post changes in board diversity across firms with different 2016 Big Three ownership.
- Event study: Year-specific interactions show no pre-trends in 2015 or 2016, with increases appearing after campaign launch.
- Fixed effects: Firm FE and year FE; director analyses use firm-by-year FE.
- Matching: Not central to the design.
- Placebo tests: Pre-trend tests; differential timing across State Street, Vanguard, and BlackRock; targeted-firm heterogeneity.
- Robustness: Controls for size trends, industry trends, B2C exposure, index inclusion, free-float adjustment, firm culture, and California's mandate.
- Alternative source of variation: Separate institution-specific timing and targeting thresholds, such as State Street targeting zero-woman boards and BlackRock targeting boards with fewer than two women.

### Is the Identification Convincing?
- Strength: Strong timing, pre-trend, and targeting evidence. Measuring ownership before the campaign helps mitigate reverse causality.
- Weakness: Big Three ownership is not random and is correlated with size, index membership, visibility, and governance environment.
- Referee concern: The identifying variation may still partly capture unobserved post-2016 pressure on larger or more visible firms rather than only Big Three pressure.

## 8. Main Regression or Model

```text
GenderDiv_it =
  beta Big3_i,2016 x Post2016_t
+ gamma1 ZeroFemale_i,2016 x Post2016_t
+ gamma2 OneFemale_i,2016 x Post2016_t
+ Firm FE
+ Year FE
+ epsilon_it
```

The dependent variable is a board diversity outcome for firm i in year t. The key coefficient is beta, which measures whether firms with higher pre-campaign Big Three ownership experience larger increases in gender diversity after the Big Three campaigns begin. The zero and one female director interactions allow firms with different baseline diversity levels to have different post-2016 trends.

For committee and mechanism tests, the paper uses a triple-differences style model:

```text
Outcome_ijt =
  theta1 Big3_i,2016 x Post2016_t x Female_j
+ theta2 Post2016_t x Female_j
+ theta3 Big3_i,2016 x Female_j
+ theta4 Female_j
+ Firm-Year FE
+ epsilon_ijt
```

For committee outcomes, theta1 measures whether female directors at high-Big-Three-ownership firms became more likely to hold important board roles after 2016. For new-director characteristics, theta1 measures whether newly hired female directors at high-Big-Three-ownership firms became less connected to existing directors or less likely to have CEO experience after the campaigns.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Institutional Investors]] by showing that large index investors are not always passive owners and can affect broad governance outcomes.
2. [[Corporate Governance]] by showing that shareholder voice can change board composition through voting threats.
3. [[Board Diversity]] by providing evidence that underrepresentation reflects search frictions, networks, and narrow experience requirements rather than only candidate supply.

It differs from prior work because it studies a large-scale investor campaign rather than a government quota, and it shows substantive changes in committee leadership rather than only numerical diversity.

## 10. Closely Related Papers
- [[Appel, Gormley, and Keim 2016]]: Passive investors are not passive owners and affect governance.
- [[Appel, Gormley, and Keim 2019]]: Passive investors can influence activism and governance through ownership structure.
- [[Adams and Ferreira 2009]]: Female directors are associated with different monitoring and governance behavior.
- [[Farrell and Hersch 2005]]: Studies gender and additions to corporate boards.
- [[Giannetti and Wang 2022]]: Public attention to gender equality affects board gender diversity.
- [[Field, Souther, and Yore 2020]]: Diverse directors may reach the board but still face barriers to leadership roles.
- [[Azar et al. 2021]]: Big Three ownership and broad ESG-related corporate behavior.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the literature on institutional investors and corporate governance. Can large passive investors meaningfully influence firm governance, and how do papers establish causality?

How to use this paper:
- Main finding: Big Three campaigns increased female board representation and substantive female board influence.
- Data: BoardEx, 13F institutional ownership, CRSP, ISS Voting Analytics.
- Identification: Pre-campaign Big Three ownership interacted with post-2016 campaign timing, plus firm and year FE.
- Limitation: Big Three ownership is correlated with firm size, index membership, and public visibility.
- Connection to other papers: Pair with [[Appel, Gormley, and Keim 2016]], [[Appel, Gormley, and Keim 2019]], and [[Azar et al. 2021]] for the broader argument that passive investors can exert governance pressure.
- Best exam phrase: "Gormley et al. use pre-campaign Big Three ownership as exposure to shareholder voice and show that passive investors can induce firms to adopt easy-to-monitor governance changes."

## 12. Hypotheses Inspired by This Paper
H1: Firms with higher passive institutional ownership are more likely to adopt governance reforms after large index investors announce explicit voting policies.

H2: The effect of shareholder voice is strongest when the requested governance outcome is simple, observable, and tied to director-election consequences.

H3: Investor pressure increases diversity more by changing candidate search and screening criteria than by changing the underlying supply of qualified candidates.

## 13. Possible Extension or Research Design
- Research question: Can Big Three voting campaigns change harder-to-monitor ESG outcomes, such as racial diversity disclosures, director overboarding, or climate transition planning?
- Hypothesis: Big Three campaigns have larger effects on checklist-style outcomes than on costly or ambiguous operational changes.
- Data: 13F ownership, ISS votes, proxy statements, BoardEx, sustainability disclosures, Execucomp, and firm outcomes.
- Identification: Difference-in-differences using pre-campaign Big Three ownership interacted with the timing of new voting guidelines; strengthen with Russell index inclusion or free-float variation.
- Expected result: Stronger effects for disclosure and board-composition outcomes, weaker effects for real investment or emissions outcomes.
- Contribution: Tests the boundary of index-investor governance power and whether shareholder voice changes real behavior or primarily observable governance metrics.

## 14. Critiques

### Major Concern 1
Big Three ownership is not randomly assigned. It is correlated with size, index inclusion, free float, visibility, and governance environment. The paper addresses these concerns with controls and timing tests, but a skeptical referee could still worry that high-Big-Three firms were also more exposed to post-2016 social or labor-market pressure.

### Major Concern 2
The outcome is easy to monitor, so the paper may not generalize to complex governance or operating choices. The Big Three may be effective on board diversity because it is visible, measurable, and directly tied to director elections.

### Minor Concern
The paper infers candidate-search mechanisms from BoardEx connections and experience. These are useful proxies, but they do not directly observe the private search process, candidate pool, or board deliberations.

### Referee Recommendation
Accept, because the paper has a clear shock, strong institutional detail, clean timing and targeting evidence, and useful mechanism tests. The remaining concern is external validity to less observable governance outcomes.

## 15. Memory Hooks
- Fearless Girl equals State Street's 2017 public campaign.
- Big Three ownership in 2016 times post-2016 equals shareholder voice exposure.
- Main numbers: 2.5 times as many female directors in 2019 as 2016; 76% increase in net flow; 11% increase in female director share.
- Mechanism: less old-boy network, less CEO-experience filter.
- Not tokenism: women gain committee roles, especially nominating committees.
- Best synthesis phrase: passive investors can be powerful when governance outcomes are cheap to monitor and votes create career consequences.

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Institutional Investors]], [[Corporate Governance]], [[Board Diversity]], [[ESG Activism]], or [[Shareholder Voting]]. The clean exam answer is: "Gormley et al. use pre-campaign Big Three ownership as exposure to the 2017 gender-diversity campaigns and show that firms with greater Big Three ownership added more female directors after the campaign." Use it to argue that passive investors can exert meaningful governance influence when the requested change is easy to monitor and backed by voting threats. In a critique answer, emphasize that Big Three ownership is correlated with size and visibility, but note that the paper is stronger than a standard correlation because it uses pre-campaign ownership, firm and year fixed effects, pre-trend tests, institution-specific timing, targeted-firm heterogeneity, and robustness to alternative post-2016 trends.
