---
type: paper
status: unread
title: 'Competing for Talent: Firms, Managers, and Social Networks'
authors: Isaac Hacamo; Kristoph Kleiner
year: 2022
journal: Review of Financial Studies
professor: DrJandik
seminar: null
jandik_paper_number: 24
jandik_week: 6
jandik_topic: Networks in corporate finance
jandik_done: true
field: Corporate Finance
literature:
- Managerial Labor Markets
- '[[Managerial and Social Networks]]'
- '[[Labor and Finance]]'
- '[[Corporate Governance]]'
methods:
- Randomized peer assignment
- conditional logit
- survey evidence
- placebo tests
datasets:
- Indiana University Kelley MBA records
- LinkedIn employment histories
- MBA admissions data
- survey data
identification: Random assignment of MBA students to cohorts and teams creates exogenous firm connections through former employees
main_result: Social networks increase the likelihood firms hire high-ability managers, especially for less-known, nonlocal firms and strong ties, with little effect on low-ability hires.
exam_relevance: high
must_memorize: true
tags:
- managerial-labor-markets
- social-networks
- human-capital
- corporate-governance
- recruitment
created: 2026-06-04
updated: 2026-06-04
---

# Hacamo and Kleiner 2022

## 1. One-Sentence Takeaway
This paper shows that social networks help firms recruit high-ability managers using random assignment of MBA students to teams and cohorts, and the main contribution is to identify former employees' social networks as a causal recruitment asset for firms.

## 2. Exam-Ready Abstract
Hacamo and Kleiner study whether social networks help firms recruit talented managers. The setting is the Indiana University Kelley MBA program, where students are randomly assigned to small teams and larger cohorts, creating plausibly exogenous connections between job seekers and firms through teammates or cohort members who previously worked at those firms. The authors merge MBA admissions records, GMAT scores, team and cohort assignments, LinkedIn employment histories, and survey evidence. Using a discrete choice model of firm selection, they find that connections increase the likelihood that a manager joins a connected firm, especially for high-ability managers, less-known firms, nonlocal firms, and stronger ties. The mechanism appears to be information transmission: connected peers help applicants learn about firm fundamentals and influence application choices. The paper contributes to [[Managerial Labor Markets]], [[Social Networks]], [[Human Capital]], and [[Corporate Governance]] by showing that networks can improve managerial talent allocation rather than merely creating favoritism or weak monitoring.

## 3. Research Question
Do social networks help firms recruit talented managers?

More specifically: do exogenously assigned peer connections to former employees increase the probability that MBA graduates join those firms, and are the effects stronger for high-ability managers, less-known firms, nonlocal firms, and stronger social ties?

## 4. Core Mechanism
Use a chain that can be memorized for comps:

```text
Random assignment to MBA team or cohort
-> student becomes connected to a former employee of a prospective employer
-> former employee transmits information about firm fundamentals, culture, and job quality
-> connected applicant is more likely to apply to and accept a job at that firm
-> firm gains access to higher-ability managerial talent
```

## 5. Main Findings
1. Team connections to former employees increase the probability that an MBA graduate joins the connected firm. The baseline effect is economically meaningful for both top-tier and mid-tier firms.
2. The effect is concentrated among high-ability managers, measured primarily by quantitative GMAT score, with little evidence that networks increase hiring of low-ability managers.
3. Network effects are stronger for less-known, nonlocal, infrequent-recruiting firms and for stronger ties, such as team members rather than cohort members, nearby peers, and same-gender peers.
4. Survey evidence shows connected students are more likely to apply to the connected firm, supporting an information transmission channel rather than only a pure referral or favoritism channel.
5. Placebo team tests and industry-level placebo tests suggest the results are not driven by team balancing, general industry preferences, or broad job-search skill spillovers.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | MBA graduate by potential employer choice |
| Sample period | IU Kelley MBA graduating classes 2003 to 2013, with employment tracked up to 5 years after graduation |
| Main dataset | Indiana University Kelley MBA admissions, team and cohort assignments, LinkedIn employment histories, and survey data from later MBA classes |
| Key variables | Team connection, cohort connection, prior employee indicator, GMAT quantitative score, combined GMAT score, MBA classroom performance, firm tier |
| Treatment or shock | Exogenous connection to a firm through random assignment to a team or cohort with a former employee of that firm |
| Outcome variables | Employment at connected firm within 1 year and 5 years, applications to connected firms, referrals, job tenure |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between social networks and employment would not be causal because people choose networks strategically. High-ability students may seek out better-connected classmates, students with similar preferences may form ties, and peers may share unobserved shocks or career goals. There is also equilibrium sorting: firms that attract certain types of students may also be more likely to have alumni or former employees in the MBA program. In normal observational data, it would be hard to know whether networks cause employment or simply reflect pre-existing preferences and ability.

### Identification Approach
- Natural experiment: MBA students are assigned to teams and cohorts by the MBA program, creating quasi-random exposure to peers with prior employment at specific firms.
- Instrument: No formal instrument.
- Difference in differences: Not the core design.
- Event study: Not the core design.
- Fixed effects: Firm by graduation year fixed effects control for time-varying firm demand for MBA hires. Demographic and GMAT controls address the variables used in team balancing.
- Matching: Not the core design.
- Placebo tests: Placebo teams do not predict employment. Industry-level connections do not predict employment at other firms in the same industry.
- Robustness: Results hold for cohort networks, nested logit, alternative ability measures, 1-year and 5-year outcomes, and alternative standard error assumptions.
- Alternative source of variation: Strength of tie, firm visibility, firm locality, former employee tenure, and team cognitive ability.

### Is the Identification Convincing?
- Strength: The randomized MBA team assignment is unusually clean for a social network paper and directly targets the central selection problem in networks.
- Weakness: The setting is one MBA program, so external validity to senior executives, non-MBA managers, and broader labor markets is uncertain.
- Referee concern: Team assignment is balanced rather than purely random, so remaining correlation between assigned peers and career preferences could matter. The authors address this with controls and placebo team tests, but this would still be a natural referee concern.

## 8. Main Regression or Model

```text
Pr(Y_i = j) =
  exp(alpha + beta Connection_ij + Firm x Year FE + Manager Controls_i)
  /
  sum_k exp(alpha + beta Connection_ik + Firm x Year FE + Manager Controls_i)
```

The paper estimates a conditional logit discrete choice model where each MBA graduate chooses among potential employers. The key variable is `Connection_ij`, which equals one if graduate `i` has a randomly assigned team or cohort peer who previously worked at firm `j`. The coefficient `beta` measures whether a connection to a specific firm increases the probability that the graduate joins that firm relative to other alternatives.

For heterogeneity by ability:

```text
Pr(Y_i = j) =
  f(
    beta1 Connection_ij x HighAbility_i
  + beta2 Connection_ij x MidAbility_i
  + beta3 Connection_ij x LowAbility_i
  + Firm x Year FE
  + Manager Controls_i
  )
```

`beta1` is the key coefficient for the paper's talent mechanism. If networks merely create nepotism, the effect should also appear for low-ability managers. Instead, the strongest effects are for high-ability and mid-ability managers, which supports the interpretation that networks improve talent allocation.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Managerial Labor Markets]] by showing how firms acquire managerial talent through former employee networks.
2. [[Social Networks]] by providing causal evidence from randomized peer assignment rather than observational network formation.
3. [[Human Capital]] by showing that former employees' networks can remain valuable to firms after employees leave.
4. [[Corporate Governance]] by contrasting beneficial recruitment networks with prior work showing that CEO-board connections may weaken monitoring.

It differs from prior work because it studies connections between applicants and former employees, not connections between CEOs and boards. This distinction matters because networks can either reduce information frictions in hiring or create agency problems in monitoring.

## 10. Closely Related Papers
- [[Bertrand and Schoar 2003]]: Shows managers matter for firm policy and performance, motivating why managerial talent is valuable.
- [[Cziraki and Jenter 2020]]: Documents that many CEO hires have prior connections to the hiring firm.
- [[Fracassi and Tate 2012]]: Shows CEO-board social ties can reduce monitoring and harm governance.
- [[Kramarz and Thesmar 2013]]: Studies social networks in corporate governance and monitoring.
- [[Shue 2013]]: Uses random assignment in MBA sections to identify peer effects among executives.
- [[Lerner and Malmendier 2013]]: Uses MBA peer assignment to study entrepreneurship outcomes.
- [[Dustmann et al. 2015]]: Labor networks and referrals in worker-firm matching.
- [[Pallais and Sands 2016]]: Referral information and worker productivity.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on managerial labor markets and social networks. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Social networks causally improve managerial recruitment, especially for high-ability managers.
- Data: IU Kelley MBA records, team assignments, GMAT scores, LinkedIn employment histories, and survey evidence.
- Identification: Random assignment to MBA teams and cohorts creates exogenous firm-specific connections through former employees.
- Limitation: One MBA program and early-career managers, so external validity to CEOs and non-MBA labor markets is imperfect.
- Connection to other papers: Pair with [[Bertrand and Schoar 2003]] for why managers matter, [[Cziraki and Jenter 2020]] for connected CEO hires, and [[Fracassi and Tate 2012]] for the negative side of managerial social ties.
- Best exam phrase: "Hacamo and Kleiner use randomized MBA team assignment to show that former employee networks reduce information frictions in managerial hiring and help firms recruit high-ability managers."

## 12. Hypotheses Inspired by This Paper
H1: Firms with stronger former employee alumni networks hire higher-ability managers and experience better subsequent operating performance.

H2: Network-based recruitment is more valuable for firms with greater information opacity, such as private firms, young firms, geographically distant firms, or firms outside major labor markets.

H3: Social networks improve match quality when they transmit information about firm fundamentals, but harm governance when they create loyalty or monitoring frictions after the hire.

## 13. Possible Extension or Research Design
- Research question: Do former employee networks improve long-run firm performance by helping firms hire better managers?
- Hypothesis: Firms connected to high-ability managerial labor pools through former employees experience better post-hire productivity, retention, and growth.
- Data: LinkedIn or Revelio employment histories, firm financials from Compustat or Orbis, MBA alumni networks, and manager ability proxies such as school rank, test scores, prior employer quality, or career progression.
- Identification: Use exogenous variation in network exposure from class cohorts, office closures, alumni moves, or sudden changes in local labor supply.
- Expected result: Network-connected firms hire higher-ability managers and have better match quality, especially when firms are opaque or geographically distant.
- Contribution: Extends the paper from hiring outcomes to real firm outcomes and links social networks to firm value through human capital acquisition.

## 14. Critiques

### Major Concern 1
External validity is limited. The setting is a single MBA program, and the workers are young managers rather than CEOs or senior executives. The paper argues the setting is informative because many graduates become managers and some become executives, but the labor market for senior executives may operate differently.

### Major Concern 2
The ability measure is imperfect. GMAT scores and first-semester grades proxy for cognitive ability and predicted job performance, but managerial quality also includes leadership, communication, risk preferences, industry fit, and interpersonal skills.

### Minor Concern
LinkedIn employment histories are self-reported. The match rate is high, but measurement error in employment dates, job titles, or omitted jobs could affect the estimated timing and firm choices.

### Referee Recommendation
Accept, because the paper has a clean and creative identification strategy, a clear mechanism, strong robustness tests, and an important contribution to social networks, managerial labor markets, and human capital. The main caveat is external validity, not internal validity.

## 15. Memory Hooks
- "Random MBA teams create random firm connections."
- "Former employee network equals recruitment asset."
- "High-ability hires, not low-ability nepotism."
- "Stronger for nonlocal and less-known firms."
- "Survey channel: networks make students apply."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Managerial Labor Markets]], [[Social Networks]], [[Human Capital]], [[Corporate Governance]], or [[Peer Effects]]. The clean exam answer is: "Hacamo and Kleiner use random assignment of MBA students to teams as exogenous variation in firm-specific social connections and show that former employee networks help firms recruit high-ability managers." Use it to argue that social networks can create value by reducing information frictions in labor markets, not just by enabling favoritism. In a critique answer, emphasize the single-school MBA setting and imperfect ability proxies, but note that the paper is stronger than a standard correlation because the relevant network links are generated by randomized peer assignment.
