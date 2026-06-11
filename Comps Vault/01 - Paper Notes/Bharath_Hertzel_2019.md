---
type: paper
status: unread
title: External Governance and Debt Structure
authors: Sreedhar T. Bharath and Michael Hertzel
year: 2019
journal: Review of Financial Studies
seminar:
field: Corporate Finance
literature: Debt Structure; Corporate Governance; Bank Monitoring; Product Market Competition; Market for Corporate Control
methods: Difference-in-differences; conditional logit; linear probability model; firm fixed effects; covenant strictness tests
datasets: DealScan; SDC; Mergent FISD; Compustat; Hoberg-Phillips industry data; U.S. import tariff data; Murfin covenant strictness data
identification: Quasi-natural experiments using import tariff reductions and state business combination laws
main_result: Firms substitute between external governance mechanisms. Stronger product market governance reduces bank debt use, while weaker takeover governance increases bank debt use.
exam_relevance: high
must_memorize: true
tags:
  - debt-structure
  - bank-monitoring
  - corporate-governance
  - product-market-competition
  - takeover-market
  - difference-in-differences
  - DrJandik
created: 2026-06-03
updated: 2026-06-03
---



# Bharath and Hertzel 2019

## 1. One-Sentence Takeaway
This paper shows that firms substitute between bank monitoring and other external governance mechanisms using import tariff reductions and antitakeover business combination laws, and the main contribution is evidence that debt structure is part of the firm’s endogenous governance system.

## 2. Exam-Ready Abstract
Bharath and Hertzel study whether external governance pressure affects whether firms issue bank loans or public debt. The paper’s core idea is that banks provide creditor governance through monitoring, covenants, and control rights, so firms should demand less bank governance when other external governance mechanisms are strong. Using new debt issues from 1982 to 2010, they compare bank loans from DealScan with public bonds from SDC and Mergent FISD. Their main identification comes from two quasi-natural experiments: import tariff reductions that increase product market competition and business combination laws that reduce takeover market discipline. Firms are less likely to use bank debt after tariff reductions and more likely to use bank debt after antitakeover laws. Covenant strictness tests support the same mechanism: covenants loosen when product market governance rises and tighten when takeover governance falls. This paper connects to [[Debt Structure]], [[Bank Monitoring]], [[Corporate Governance]], and [[Product Market Competition]].

## 3. Research Question
Does external governance pressure affect the type of debt firms issue?

More specifically: do firms substitute between bank creditor governance and other governance mechanisms, such as product market competition and the market for corporate control?

## 4. Core Mechanism

```text
External governance shock
-> product market competition rises or takeover threat falls
-> demand for creditor governance changes
-> firms adjust debt source between bank loans and public bonds
-> debt structure becomes part of the firm’s optimal governance bundle
```

For tariff reductions:

```text
Import tariff reduction
-> foreign competition increases
-> product market discipline reduces managerial slack
-> firms need less bank monitoring
-> firms shift from bank loans toward public debt
```

For business combination laws:

```text
State antitakeover law
-> hostile takeover threat declines
-> external shareholder discipline weakens
-> firms need more alternative governance
-> firms shift from public debt toward bank loans
```

## 5. Main Findings
1. Firms in more competitive industries are less likely to issue bank loans rather than public bonds, consistent with product market competition substituting for bank monitoring.
2. After import tariff reductions, firms issuing new debt are about 11% less likely to choose bank loans, consistent with stronger product market governance reducing demand for creditor governance.
3. After business combination laws reduce takeover threats, firms are more likely to issue bank loans, consistent with bank debt substituting for weakened takeover governance.
4. Covenant strictness tests corroborate the mechanism: bank loan covenants tighten after BC laws and loosen after tariff reductions.
5. The effects are stronger in noncompetitive industries, where product market discipline is initially weaker.
6. Substitution effects are larger in relationship industries where credible governance is more valuable for maintaining stakeholder relationships.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | New debt issue by firm-year |
| Sample period | 1982 to 2010 for debt choice sample; tariff shocks identified over earlier relevant tariff data windows |
| Main dataset | DealScan for bank loans; SDC and Mergent FISD for public bonds; Compustat for accounting variables |
| Key variables | Loan indicator; public bond indicator; product market competition; import penetration shock; BC law indicator; covenant strictness |
| Treatment or shock | Import tariff reductions as increases in product market competition; business combination laws as reductions in takeover governance |
| Outcome variables | Probability of issuing a bank loan rather than public debt; covenant strictness for bank loans |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between product market competition and bank debt choice is not causal. Firms may choose debt structures that affect industry competition, so reverse causality is possible. Omitted variables may also drive both competition and debt choice, such as firm quality, risk, financing constraints, growth opportunities, or industry investment dynamics. There is also equilibrium sorting: firms choose governance, financing, and industry strategy jointly, so observed debt structure reflects an endogenous governance bundle.

### Identification Approach
- Natural experiment: Yes. The paper uses tariff reductions and state antitakeover laws as external shocks to governance pressure.
- Instrument: No formal IV. The shocks serve as plausibly exogenous sources of variation.
- Difference in differences: Yes. The empirical design compares debt choice before and after governance shocks for affected firms.
- Event study: Not the central presentation in the summary text. Not clear from provided text whether full dynamic event-time figures are used.
- Fixed effects: Yes. The paper uses firm fixed effects in linear probability models and conditional logit specifications.
- Matching: Not central. Not clear from provided text.
- Placebo tests: Robustness checks include alternate antitakeover laws, court decisions, and concerns about lobbying around trade policy.
- Robustness: They use multilateral trade agreement windows to reduce lobbying concerns, alternate antitakeover law definitions from Karpoff and Wittry, and covenant strictness tests.
- Alternative source of variation: Covenant strictness provides an intensive-margin test of bank governance for firms that continue using bank loans.

### Is the Identification Convincing?
- Strength: Stronger than standard debt choice regressions because the shocks move external governance in opposite directions and generate symmetric predictions.
- Weakness: Tariff reductions may affect financing needs, risk, and growth opportunities, not only governance. Antitakeover laws may proxy for broader state-level legal or political environments.
- Referee concern: The shocks may change real investment opportunities or risk rather than governance demand. The best response is that the paper controls for firm characteristics, uses opposite-signed shocks, and shows corroborating covenant strictness evidence.

## 8. Main Regression or Model

```text
LoanIssue_it = beta ExternalGovernanceShock_it + Controls_it + Firm FE + Time FE + epsilon_it
```

The dependent variable equals one if the firm issues a bank loan and zero if it issues a public bond. The key coefficient, beta, measures whether an external governance shock changes the probability that the firm chooses bank debt rather than public debt.

For the tariff experiment:

```text
LoanIssue_it = beta ImportPenetration_jt + Controls_it + Firm FE + Time FE + epsilon_it
```

A negative beta means that stronger product market governance reduces demand for bank monitoring.

For the takeover experiment:

```text
LoanIssue_it = beta BCLaw_st + Controls_it + Firm FE + Time FE + epsilon_it
```

A positive beta means that weaker takeover governance increases demand for bank monitoring.

For heterogeneity:

```text
LoanIssue_it =
  beta1 GovernanceShock_it
+ beta2 GovernanceShock_it x LowCompetition_i
+ Controls_it
+ Firm FE
+ Time FE
+ epsilon_it
```

Here beta2 tests whether substitution is stronger when preexisting product market discipline is weak. The main economic interpretation is that bank debt is more valuable as governance when other governance mechanisms are weak.

For covenant strictness:

```text
CovenantStrictness_it = beta ExternalGovernanceShock_it + Firm FE + epsilon_it
```

A positive beta after BC laws means banks tighten covenants when takeover governance weakens. A negative beta after tariff reductions means banks loosen covenants when product market governance strengthens.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Debt Structure]] by showing that the bank loan versus public bond choice depends on governance demand, not only information asymmetry or credit quality.
2. [[Bank Monitoring]] by showing that banks provide governance outside payment default through covenants and control rights.
3. [[Corporate Governance]] by showing that governance mechanisms are endogenous substitutes.
4. [[Product Market Competition]] by showing that competition can substitute for creditor monitoring.
5. [[Market for Corporate Control]] by showing that weakened takeover discipline increases demand for bank governance.

It differs from prior work because it studies new debt issuance as an incremental governance choice and uses external governance shocks to identify substitution across governance mechanisms.

## 10. Closely Related Papers
- [[Denis and Mihov 2003]]: Studies determinants of debt source and shows credit quality helps explain bank versus public debt.
- [[Diamond 1984]]: Provides the classic theory of delegated monitoring and why banks are special.
- [[Nini Smith and Sufi 2012]]: Shows creditors influence firm behavior after covenant violations.
- [[Roberts and Sufi 2009]]: Studies loan renegotiation and the role of covenants in debt contracting.
- [[Giroud and Mueller 2010]]: Uses BC laws and product market competition to study governance and operating performance.
- [[Bertrand and Mullainathan 2003]]: Uses antitakeover laws to study managerial quiet life behavior.
- [[Murfin 2012]]: Provides the covenant strictness measure used in the paper.
- [[Demsetz and Lehn 1985]]: Frames corporate governance as an endogenous equilibrium choice.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the literature on debt structure and corporate governance. How do firms choose between bank loans and public debt, and how do researchers establish causality?

How to use this paper:
- Main finding: Firms use bank debt as a substitute governance mechanism when other governance forces are weak.
- Data: Bank loans from DealScan, public bonds from SDC and Mergent FISD, accounting controls from Compustat, competition data from Hoberg-Phillips, and covenant strictness from Murfin.
- Identification: Difference-in-differences around tariff reductions and business combination laws.
- Limitation: Shocks may affect operating risk or financing needs in addition to governance demand.
- Connection to other papers: Extends [[Denis and Mihov 2003]] by adding governance to debt source choice; connects to [[Nini Smith and Sufi 2012]] on creditor control; connects to [[Giroud and Mueller 2010]] on competition and governance.
- Best exam phrase: “Bharath and Hertzel show that debt structure is not just financing. It is also governance.”

## 12. Hypotheses Inspired by This Paper
H1: Firms facing weaker shareholder governance are more likely to use bank debt rather than public debt.

H2: Firms experiencing stronger product market discipline reduce reliance on bank debt and negotiate looser loan covenants.

H3: Governance substitution between bank debt and external governance is strongest in industries with weak product market competition or high relationship-specific contracting needs.

## 13. Possible Extension or Research Design
- Research question: Do firms substitute between creditor governance and supply chain governance after geopolitical shocks?
- Hypothesis: Firms with fragile or politically risky supply chains increase reliance on bank debt because banks provide monitoring and certification when external stakeholder trust declines.
- Data: DealScan, FISD, Compustat, FactSet Revere supply chain links, sanctions exposure, and covenant data.
- Identification: Difference-in-differences around the Russia-Ukraine invasion comparing firms with Russian supplier exposure to otherwise similar firms.
- Expected result: Exposed firms, especially those in relationship-intensive industries, increase bank borrowing and covenant strictness after the shock.
- Contribution: Extends governance substitution from product and takeover markets to supply chain networks and geopolitical risk.

## 14. Critiques

### Major Concern 1
The tariff shock may affect firms through competition, risk, cash flow volatility, import exposure, and investment opportunities, not just governance. If tariff reductions make firms riskier, debt source changes could reflect financing frictions rather than substitution away from bank monitoring.

### Major Concern 2
Business combination laws may not be clean exogenous shocks for every firm. Firms can opt out, states differ legally and economically, and antitakeover laws may coincide with broader changes in corporate law or local political economy.

### Minor Concern
The dependent variable focuses on the source of new debt issues, not the full debt structure. This is useful for identification but may miss substitution through existing debt, renegotiation, maturity, secured debt, or covenant packages.

### Referee Recommendation
Accept, because the paper has a clear theory, two opposite-signed quasi-natural experiments, strong economic magnitudes, and an independent covenant strictness test. The main caution is that the shocks may operate through channels beyond governance.

## 15. Memory Hooks
- “Bank debt is governance, not just money.”
- Tariff cuts increase competition, so firms need less bank monitoring.
- BC laws weaken takeovers, so firms need more bank monitoring.
- Covenant strictness moves in the same direction as governance demand.
- The paper is a governance-substitution answer for debt structure comps.

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Debt Structure]], [[Bank Monitoring]], [[Corporate Governance]], [[Product Market Competition]], or [[Market for Corporate Control]]. The clean exam answer is: "Bharath and Hertzel use import tariff reductions and business combination laws as shocks to external governance and show that firms substitute between bank debt and other governance mechanisms." Use it to argue that the choice between bank loans and public debt reflects the demand for creditor governance, not only information asymmetry, credit risk, or flotation costs. In a critique answer, emphasize that tariff and takeover shocks may affect risk and investment opportunities, but note that the paper is stronger than a standard correlation because it uses two opposite-signed shocks and confirms the mechanism with covenant strictness.