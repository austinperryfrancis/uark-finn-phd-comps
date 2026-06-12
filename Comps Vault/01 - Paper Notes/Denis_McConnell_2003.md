---
type: paper
status: unread
title: International Corporate Governance
authors: Diane K. Denis and John J. McConnell
year: 2003
journal: Journal of Financial and Quantitative Analysis
professor: DrJandik
seminar: null
jandik_paper_number: 1
jandik_week: 1
jandik_topic: 'Corporate governance: issues and indices'
jandik_done: true
field: corporate finance
literature:
- '[[Corporate Governance]]'
- international corporate governance
- investor protection
- ownership structure
methods:
- literature review
- cross-country synthesis
datasets:
- survey of prior empirical studies
identification: survey paper, not a single causal identification design
main_result: International corporate governance research evolves from studying firm-level mechanisms within individual countries to studying how legal systems and investor protection shape governance structures and outcomes across countries.
exam_relevance: high
must_memorize: true
tags:
- board-monitoring
- corporate-finance
- corporate-governance
created: 2026-06-03
updated: 2026-06-03
---

# Denis and McConnell 2003

## 1. One-Sentence Takeaway
This paper shows that international corporate governance research evolved from country-level studies of boards, ownership, compensation, and takeovers into a law-and-finance literature on legal origins, investor protection, and cross-country governance systems, and the main contribution is organizing global governance research into two generations.

## 2. Exam-Ready Abstract
Denis and McConnell (2003) survey international corporate governance research, focusing mainly on countries outside the United States. The paper asks how governance mechanisms reduce agency costs when ownership and control are separated, and how those mechanisms differ across legal, institutional, and ownership environments. The authors define corporate governance as the set of institutional and market mechanisms that induce corporate controllers to make decisions that maximize value for suppliers of capital. The first generation of research mirrors U.S. corporate governance studies and examines mechanisms such as boards, executive compensation, ownership concentration, privatization, and the takeover market within individual countries. The second generation emphasizes cross-country differences in legal systems, especially investor protection and enforcement, following the law-and-finance literature associated with La Porta, Lopez-de-Silanes, Shleifer, and Vishny. The central lesson is that governance mechanisms are substitutes and complements, so firm-level governance cannot be evaluated separately from country-level legal and institutional context. This paper connects directly to [[Corporate Governance]], [[Law and Finance]], [[Ownership Structure]], [[Agency Theory]], and [[Investor Protection]].

## 3. Research Question
What do we know about corporate governance systems around the world, and how do firm-level governance mechanisms interact with country-level legal and institutional systems?

More specifically, the paper asks whether governance mechanisms such as boards, executive compensation, ownership concentration, privatization, and takeovers work similarly across countries, and whether differences in investor protection and legal enforcement explain cross-country variation in governance structures and outcomes.

## 4. Core Mechanism

```text
Separation of ownership and control
-> agency conflicts between controllers and suppliers of capital
-> need for governance mechanisms
-> boards, compensation, ownership, takeovers, legal protection, and enforcement discipline insiders
-> lower agency costs and potentially higher firm value
```

Second-generation mechanism:

```text
Weak investor protection or weak enforcement
-> minority shareholders face higher expropriation risk
-> firms rely more on concentrated ownership and private monitoring
-> public equity markets remain smaller and less dispersed
-> governance outcomes differ across countries
```

## 5. Main Findings
1. International governance research can be divided into two broad generations: first-generation studies of firm-level mechanisms within countries and second-generation studies of cross-country legal and institutional systems.
2. Ownership concentration is much more common outside the U.S. and U.K., and concentrated ownership is often a response to weak legal protection for outside investors.
3. Boards and executive compensation matter, but the evidence is more limited outside the U.S., and their effectiveness depends on institutional context.
4. Privatization studies generally find improved performance after movement from state ownership to private ownership, especially when governments relinquish control and when outside or foreign owners are present.
5. The market for corporate control is an important governance mechanism in the U.S. and U.K., but it is weaker or less active in many countries with concentrated ownership, bank-centered systems, or weaker shareholder protection.
6. Legal systems, especially investor rights and enforcement, shape ownership structures, capital market development, dividend policy, private benefits of control, and governance effectiveness.
7. The paper does not claim that one governance system is universally optimal. Instead, it emphasizes that governance arrangements may be context-specific and may converge only partially across countries.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Not a primary empirical paper. The survey covers firms, countries, legal regimes, and governance systems from prior studies. |
| Sample period | Prior literature mainly from the 1970s through early 2000s, with non-U.S. governance research expanding in the 1990s. |
| Main dataset | Survey of empirical and theoretical corporate governance studies. |
| Key variables | Board composition, board size, CEO-chair duality, executive compensation, ownership concentration, insider ownership, blockholder identity, state ownership, takeover activity, legal origin, investor protection, enforcement, private benefits of control. |
| Treatment or shock | Not applicable as a single treatment. Reviewed settings include privatization, governance code adoption, legal differences, and ownership changes. |
| Outcome variables | Firm value, profitability, CEO turnover, restructuring, takeover outcomes, capital market development, dividend policy, private benefits of control. |

## 7. Identification Strategy

### Endogeneity Problem
This is a survey paper, so it does not estimate one causal model. The central empirical difficulty across the surveyed literature is that governance mechanisms are endogenous. Firms choose board structure, ownership concentration, compensation contracts, and takeover defenses in response to unobserved firm characteristics, legal environment, managerial quality, investment opportunities, and agency problems. For example, a positive relation between ownership concentration and firm value may mean that blockholders improve monitoring, but it may also mean that blockholders select better firms or that valuable firms choose different ownership structures. Similarly, weak performance may cause board changes or CEO turnover, rather than board independence causing better monitoring. Cross-country studies also face omitted institutional variables because legal origin, enforcement, culture, politics, financial development, and ownership structure are jointly determined.

### Identification Approach
- Natural experiment: Reviewed studies sometimes use legal reforms, codes of best practice, privatization, or governance changes as institutional shocks.
- Instrument: Not central to the survey. Some underlying papers use instruments or institutional variation, but no single instrument defines this paper.
- Difference in differences: Relevant in studies of governance code adoption, privatization, or legal changes, but not the paper's own design.
- Event study: Reviewed in studies of outside CEO appointments, compliance announcements, takeovers, block trades, and privatization events.
- Fixed effects: Discussed indirectly through underlying empirical papers.
- Matching: Relevant in some privatization and governance studies, but not a central method of the survey.
- Placebo tests: Not clear from provided text.
- Robustness: The paper evaluates consistency across countries, methods, and governance mechanisms.
- Alternative source of variation: Cross-country legal differences, legal origin, investor protection, enforcement, and institutional development.

### Is the Identification Convincing?
- Strength: The paper is convincing as a literature map because it synthesizes many settings and shows that governance mechanisms vary systematically with legal and institutional context.
- Weakness: Because it is a survey, its conclusions depend on the identification quality of the underlying papers. Many early studies are correlational.
- Referee concern: The first-generation evidence often suffers from endogenous governance choice, while second-generation legal-origin evidence may bundle many country-level institutions together.

## 8. Main Regression or Model
This is not a primary regression paper. A generic regression from the surveyed first-generation literature would be:

```text
FirmValue_it = beta GovernanceMechanism_it + Controls_it + Industry FE + Time FE + epsilon_it
```

In words, these studies ask whether a governance mechanism such as board independence, board size, managerial ownership, blockholder ownership, or bank ownership is associated with firm value or performance, controlling for observable firm characteristics.

A generic cross-country law-and-finance model from the second-generation literature would be:

```text
GovernanceOutcome_ic =
  beta1 InvestorProtection_c
+ beta2 Enforcement_c
+ beta3 FirmControls_ic
+ Industry FE
+ epsilon_ic
```

Here, `i` indexes firms and `c` indexes countries. `beta1` captures whether stronger investor protection is associated with better governance outcomes, such as more dispersed ownership, larger equity markets, lower private benefits of control, or better minority shareholder treatment. The key economic interpretation is that legal protection and enforcement shape the feasible set of corporate governance arrangements.

For reform-based work, the model can be written as:

```text
Outcome_it =
  beta1 TreatedFirm_i x PostReform_t
+ Controls_it
+ Firm FE
+ Time FE
+ epsilon_it
```

In this setting, `beta1` measures whether firms more affected by a governance reform change outcomes after the reform relative to less affected firms.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Corporate Governance]] by organizing the international governance literature around internal and external mechanisms.
2. [[Law and Finance]] by highlighting the shift from firm-level mechanisms to legal systems and investor protection.
3. [[Ownership Structure]] by emphasizing that concentrated ownership is the global norm rather than the exception.
4. [[Agency Theory]] by applying the ownership-control conflict to cross-country institutional environments.
5. [[Comparative Corporate Governance]] by asking whether governance systems converge or remain institutionally distinct.

It differs from prior work because it is not focused on one mechanism, one country, or one empirical result. It synthesizes boards, compensation, ownership, takeovers, privatization, and legal systems into one international governance framework.

## 10. Closely Related Papers
- [[Jensen and Meckling 1976]]: Agency costs of outside equity and the foundational separation of ownership and control problem.
- [[Shleifer and Vishny 1997]]: Broad survey of corporate governance and investor protection.
- [[La Porta Lopez-de-Silanes Shleifer and Vishny 1998]]: Legal origins and investor protection across countries.
- [[La Porta Lopez-de-Silanes Shleifer and Vishny 1997]]: Legal determinants of external finance.
- [[La Porta Lopez-de-Silanes and Shleifer 1999]]: Corporate ownership around the world.
- [[Faccio and Lang 2002]]: Ultimate ownership in Western Europe.
- [[Megginson and Netter 2001]]: Survey of privatization.
- [[Kaplan and Minton 1994]]: Japanese boards and outside director appointments.
- [[Dahya McConnell and Travlos 2002]]: U.K. Cadbury Code and CEO turnover sensitivity.
- [[Gorton and Schmid 2000]]: German ownership concentration and firm performance.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the international corporate governance literature. How do ownership, boards, legal systems, and investor protection interact to shape governance outcomes across countries?

How to use this paper:
- Main finding: International governance mechanisms cannot be understood without legal and institutional context.
- Data: Survey of international empirical governance studies.
- Identification: Not a primary design. Use it to organize identification strategies from underlying papers.
- Limitation: It summarizes a literature where many studies face endogenous governance choice and bundled country-level institutions.
- Connection to other papers: Pair with [[Shleifer and Vishny 1997]], [[La Porta Lopez-de-Silanes Shleifer and Vishny 1998]], [[Faccio and Lang 2002]], and [[Megginson and Netter 2001]].
- Best exam phrase: Denis and McConnell (2003) distinguish first-generation governance studies of firm-level mechanisms from second-generation law-and-finance studies of investor protection and legal systems.

## 12. Hypotheses Inspired by This Paper
H1: The value effect of board independence is stronger in countries with stronger investor protection because outside directors are more legally and institutionally empowered to discipline insiders.

H2: Ownership concentration is more valuable in weak investor protection countries because blockholders substitute for missing legal protections, but this benefit declines when private benefits of control are high.

H3: Privatization improves firm performance most when state control is fully relinquished and new outside owners have both incentives and legal rights to monitor managers.

## 13. Possible Extension or Research Design
- Research question: Does the effectiveness of board independence depend on country-level investor protection and enforcement quality?
- Hypothesis: Independent directors improve firm value and CEO turnover-performance sensitivity only when legal enforcement gives directors and minority shareholders meaningful power.
- Data: International listed firms from BoardEx or Refinitiv, country-level investor protection measures, financial statements from Compustat Global or Orbis, and CEO turnover data.
- Identification: Difference in differences around staggered governance code reforms requiring independent directors, interacted with baseline enforcement quality.
- Expected result: Board independence has stronger effects in high-enforcement countries and weaker effects where controlling shareholders can bypass board monitoring.
- Contribution: The study would connect first-generation board composition research with second-generation law-and-finance research.

## 14. Critiques

### Major Concern 1
The paper is a survey, so it cannot establish a new causal result. Its conclusions depend on the strength of the underlying literature, much of which is correlational.

### Major Concern 2
The legal-origin literature may over-attribute governance differences to legal systems when legal origin is correlated with political history, culture, economic development, financial openness, and enforcement capacity.

### Minor Concern
The review is necessarily selective. International corporate governance is broad, and the paper may underrepresent non-English studies or country-specific institutional details.

### Referee Recommendation
Accept, because the paper provides an influential and exam-useful synthesis of international corporate governance, even though it is not designed to provide a standalone causal estimate.

## 15. Memory Hooks
- Two generations: firm-level governance first, law-and-finance second.
- Global norm: concentrated ownership, not Berle-Means dispersion.
- Governance mechanisms are substitutes and complements.
- Investor protection shapes ownership, markets, and private benefits.
- Use it as the map of international corporate governance.

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Corporate Governance]], [[International Corporate Governance]], [[Law and Finance]], [[Ownership Structure]], [[Boards of Directors]], [[Privatization]], or [[Investor Protection]]. The clean exam answer is: "Denis and McConnell (2003) survey international corporate governance and distinguish first-generation studies of firm-level mechanisms from second-generation studies of legal systems and investor protection." Use it to argue that boards, ownership, takeovers, and compensation do not operate in an institutional vacuum. In a critique answer, emphasize that many governance mechanisms are endogenous, but note that the paper is stronger than a standard single-country correlation because it synthesizes evidence across countries, mechanisms, and legal regimes.
