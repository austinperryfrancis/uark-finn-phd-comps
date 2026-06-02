from __future__ import annotations

import argparse
import json
from pathlib import Path


VAULT_ROOT = Path("Comps Vault")

STATUSES = ["Unread", "Triaged", "Skimmed", "Deep Read", "Mastered", "Needs Review"]

SEMINARS = [
    "FINN 6333 Empirical Research in Finance",
    "FINN 62303 Seminar in Financial Management",
    "FINN 67303 Financial Markets and Institutions",
    "FINN 6133 Investment Theory",
    "FINN 60403 Finance Theory",
]

LITERATURES = [
    "Labor and Finance",
    "Spatial Spillovers",
    "Venture Capital and Entrepreneurship",
    "IPO Real Effects",
    "Private Equity",
    "Machine Learning in Corporate Finance",
    "Innovation",
    "Internal Capital Markets",
    "Customer-Supplier Shock Propagation",
    "Climate Finance and Supply Chains",
    "Managerial and Social Networks",
    "Securitization",
    "Bank Runs and Deposit Insurance",
    "Bank Opacity",
    "P2P Lending and FinTech",
    "Payday Lending",
    "Bank Branching and Deregulation",
    "Market Discipline",
    "Momentum",
    "Bid-Ask Spreads",
    "Mutual Funds and ETFs",
    "Asset Pricing Theory",
    "Derivative Pricing",
    "Stochastic Discount Factors",
]

METHODS = [
    "Difference in Differences",
    "Instrumental Variables",
    "Regression Discontinuity",
    "Event Studies",
    "Matching and PSM",
    "Natural Experiments",
    "Fixed Effects",
    "Placebo Tests",
    "Robustness Tests",
    "Endogeneity Problems",
]

THEORY_DERIVATIONS = [
    "Stochastic Discount Factor",
    "Risk Neutral Pricing",
    "Expected Return Beta Model",
    "Futures Contract Paying S Squared",
    "APT",
    "Consumption Based Asset Pricing",
]

DATASETS = [
    "WRDS",
    "CRSP",
    "Compustat",
    "DealScan",
    "FactSet Revere",
    "Patent Data",
    "HMDA",
    "Call Reports",
    "FDIC Data",
    "Mortgage Data",
]


def yml_tags(*tags: str) -> str:
    return "\n".join(f"  - {tag}" for tag in tags)


PAPER_NOTE_TEMPLATE = """---
type: paper
status: unread
title:
authors:
year:
journal:
seminar:
field:
literature:
methods:
datasets:
identification:
main_result:
exam_relevance: medium
must_memorize: false
tags:
  - paper
  - comps
created:
updated:
---

# {{Title}}

## 1. One-Sentence Takeaway
This paper shows that ___ using ___, and the main contribution is ___.

## 2. Exam-Ready Abstract
Write 5 to 7 sentences covering the question, importance, data, method, result, and contribution.

## 3. Research Question
What is the paper trying to answer?

## 4. Core Mechanism
Shock or treatment -> mechanism -> outcome

## 5. Main Findings
1.
2.
3.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | |
| Sample period | |
| Main dataset | |
| Key variables | |
| Treatment or shock | |
| Outcome variables | |

## 7. Identification Strategy

### Endogeneity Problem
Discuss selection, omitted variables, reverse causality, simultaneity, measurement error, or equilibrium sorting.

### Identification Approach
- Natural experiment:
- Instrument:
- Difference in differences:
- Event study:
- Fixed effects:
- Matching:
- Placebo tests:
- Robustness:

### Is the Identification Convincing?
- Strength:
- Weakness:
- Referee concern:

## 8. Main Regression or Model

```text
Outcome_it = beta Treatment_it + Controls_it + Firm FE + Time FE + epsilon_it
```

Explain the equation in words.

## 9. Contribution to the Literature
This paper contributes to:
1.
2.
3.

It differs from prior work because:

## 10. Closely Related Papers
- [[Paper 1]]:
- [[Paper 2]]:
- [[Paper 3]]:

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on ___. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding:
- Data:
- Identification:
- Limitation:
- Connection to other papers:

## 12. Hypotheses Inspired by This Paper
H1:
H2:
H3:

## 13. Possible Extension or Research Design
- Research question:
- Hypothesis:
- Data:
- Identification:
- Expected result:
- Contribution:

## 14. Critiques

### Major Concern 1

### Major Concern 2

### Minor Concern

### Referee Recommendation
Reject / R&R / Accept, because ___.

## 15. Memory Hooks
-
-
-

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes/No |
| Identification importance | High/Medium/Low |
| Good for synthesis? | High/Medium/Low |
| Good for research design question? | High/Medium/Low |
| Good for critique/referee question? | High/Medium/Low |
"""


LITERATURE_DESCRIPTIONS = {
    "Labor and Finance": "Use this map for papers linking firm finance, financial constraints, labor markets, employment, wages, human capital, and worker outcomes. Include Bernstein, McQuade, and Townsend 2020; Liu, Makridis, Ouimet, and Simintzi 2021; labor markets; firm finance; and causal identification.",
    "Spatial Spillovers": "Use this map for geographic spillovers, local shocks, headquarters effects, neighborhood externalities, agglomeration, and regional propagation of financial or real effects.",
    "Venture Capital and Entrepreneurship": "Use this map for VC financing, monitoring, startup growth, entrepreneurship, innovation, employee entrepreneurship, and financing frictions. Include Bernstein, Giroud, and Townsend 2016; Babina 2020; VC monitoring; entrepreneurship; innovation; and employee entrepreneurship.",
    "IPO Real Effects": "Use this map for how IPOs affect real activity, innovation, employment, disclosure, investment, governance, and private-to-public transitions.",
    "Private Equity": "Use this map for buyouts, operational engineering, leverage, employment effects, governance, productivity, agency conflicts, and real effects of private ownership.",
    "Machine Learning in Corporate Finance": "Use this map for prediction, textual analysis, alternative data, credit scoring, governance signals, interpretability, and causal versus predictive uses of machine learning.",
    "Innovation": "Use this map for patents, R&D, inventor mobility, financing constraints, innovation incentives, knowledge spillovers, and real effects of capital market frictions.",
    "Internal Capital Markets": "Use this map for conglomerates, resource allocation, winner picking, cross-subsidization, segment investment, headquarters incentives, and agency costs.",
    "Customer-Supplier Shock Propagation": "Use this map for supply-chain propagation, customer-supplier links, network spillovers, treatment shocks, CEO turnover, and customer CSR. Include Barrot and Sauvagnat and related papers on how shocks travel through production networks.",
    "Climate Finance and Supply Chains": "Use this map for climate risk, transition risk, physical risk, cap-and-trade, supplier spillovers, green innovation, and emissions regulation. Include Sautner et al. 2023; Ivanov, Kruttli, and Watugala 2024; Hall et al. 2023; and Pankratz and Schiller 2024.",
    "Managerial and Social Networks": "Use this map for boards, executives, peer effects, social ties, information flow, director networks, local networks, and governance or financing outcomes.",
    "Securitization": "Use this map for residential mortgage securitization, originate-to-distribute incentives, screening and monitoring, housing bubble mechanisms, and subprime mortgage credit expansion. Include Purnanandam 2011; Keys et al. 2010; Mian and Sufi 2009; and Nadauld et al. 2013.",
    "Bank Runs and Deposit Insurance": "Use this map for Diamond and Dybvig 1983, liquidity transformation, deposit insurance, lender of last resort, SVB and Signature Bank 2023, uninsured deposits, and bank opacity.",
    "Bank Opacity": "Use this map for bank asset opacity, disclosure, market discipline, supervisory information, loan loss recognition, balance-sheet complexity, and information asymmetry.",
    "P2P Lending and FinTech": "Use this map for Balyuk 2023; Tang 2019; Chava et al. 2021; platform lending; consumer credit access; substitutes versus complements; screening; and future borrowing outcomes.",
    "Payday Lending": "Use this map for high-cost credit, household liquidity, consumer protection, rollover borrowing, regulation, welfare, and short-term credit constraints.",
    "Bank Branching and Deregulation": "Use this map for branching deregulation, interstate banking, competition, local credit supply, entrepreneurship, bank consolidation, and real effects.",
    "Market Discipline": "Use this map for uninsured depositors, subordinated debt, disclosure, bank risk taking, creditor monitoring, and regulatory discipline.",
    "Momentum": "Use this map for return continuation, behavioral explanations, risk-based explanations, crashes, implementation, and cross-sectional asset pricing tests.",
    "Bid-Ask Spreads": "Use this map for market microstructure, liquidity, adverse selection, inventory costs, order processing costs, price impact, and trading frictions.",
    "Mutual Funds and ETFs": "Use this map for delegated asset management, fund flows, performance, fees, incentives, liquidity transformation, ETF arbitrage, and fire sales.",
    "Asset Pricing Theory": "Use this map for CAPM, ICAPM, consumption models, SDF logic, beta representations, no-arbitrage pricing, and equilibrium expected returns.",
    "Derivative Pricing": "Use this map for no-arbitrage, replication, risk-neutral valuation, Black-Scholes, PDE methods, futures, options, and payoff transformations.",
    "Stochastic Discount Factors": "Use this map for SDF existence, Euler equations, Hansen-Jagannathan bounds, risk premia, factor models, and the connection between pricing kernels and expected returns.",
}


METHOD_DETAILS = {
    "Difference in Differences": ("Compare changes in outcomes for treated and control units before and after a shock.", "Y_it = alpha + beta Treat_i x Post_t + gamma X_it + FE_i + FE_t + epsilon_it", "Parallel trends: absent treatment, treated and control units would have followed similar outcome trends.", "Differential pre-trends, anticipation, spillovers, treatment timing bias, compositional changes.", "Use for regulatory shocks, geographic rollouts, bank deregulation, cap-and-trade exposure, or credit supply disruptions."),
    "Instrumental Variables": ("Use external variation in an endogenous regressor that affects the outcome only through that regressor.", "Y_i = beta Xhat_i + gamma Controls_i + epsilon_i, with first stage X_i = pi Z_i + controls + nu_i", "Relevance and exclusion: the instrument predicts treatment and has no direct effect on the outcome.", "Weak instruments, invalid exclusion, monotonicity failures, local average treatment interpretation.", "Use for credit supply, financial constraints, peer effects, or endogenous treatment choice."),
    "Regression Discontinuity": ("Exploit a treatment rule that changes discontinuously at a cutoff.", "Y_i = alpha + tau AboveCutoff_i + f(RunningVariable_i) + epsilon_i", "Units just above and below the cutoff are comparable and cannot precisely manipulate assignment.", "Manipulation, sorting, bandwidth sensitivity, functional form, multiple cutoffs.", "Use for credit scores, index inclusion, regulatory thresholds, or eligibility rules."),
    "Event Studies": ("Estimate outcome dynamics around a dated event or shock.", "Y_it = alpha + sum_k beta_k EventTime_{i,t+k} + FE_i + FE_t + epsilon_it", "The event is not anticipated in a way that drives pre-event trends, and no confounding shock occurs at the same time.", "Confounding events, anticipation, event clustering, abnormal return model choice, window selection.", "Use for announcements, fraud revelation, CEO turnover, credit rating changes, or policy events."),
    "Matching and PSM": ("Construct a comparison group with similar observable characteristics.", "Match treated and control units on propensity score or covariates, then compare outcomes.", "Selection on observables: after conditioning on matched variables, treatment is as good as random.", "Unobserved selection, poor overlap, model dependence, post-treatment matching variables.", "Use when treatment is not randomized but rich observables are available."),
    "Natural Experiments": ("Use an institutional shock that changes incentives or constraints for some units but not others.", "Y_it = alpha + beta Exposure_i x Shock_t + controls + FE_i + FE_t + epsilon_it", "Shock exposure is plausibly exogenous to potential outcomes after controls and fixed effects.", "Endogenous exposure, simultaneous shocks, equilibrium responses, spillovers.", "Use for law changes, geographic shocks, court rulings, climate policies, or banking deregulation."),
    "Fixed Effects": ("Absorb time-invariant unit heterogeneity and common time shocks.", "Y_it = beta X_it + FE_i + FE_t + epsilon_it", "Remaining within-unit changes in X are conditionally exogenous.", "Time-varying omitted variables, bad controls, limited within variation, over-control.", "Use as a baseline control structure in panel finance settings."),
    "Placebo Tests": ("Test whether the design finds effects where it should not.", "Estimate the main specification on fake outcomes, fake treatment timing, or untreated samples.", "A credible design should not produce treatment effects before treatment or on outcomes unrelated to the mechanism.", "Placebos can be underpowered or selected after seeing results.", "Use to support DiD, event studies, IV exclusion restrictions, and mechanism claims."),
    "Robustness Tests": ("Evaluate whether results survive reasonable alternative specifications.", "Re-estimate with alternative samples, controls, windows, definitions, clustering, and functional forms.", "The core result should not depend on one fragile modeling choice.", "Specification searching, weak theory for alternatives, robustness that does not address identification.", "Use to defend a result but explain that robustness is not a substitute for identification."),
    "Endogeneity Problems": ("Identify why a simple correlation may not estimate a causal effect.", "Y_i = beta X_i + controls + epsilon_i, where Cov(X_i, epsilon_i) may not equal zero", "Causal interpretation requires treatment variation unrelated to unobserved determinants of outcomes.", "Selection, omitted variables, reverse causality, simultaneity, measurement error, equilibrium sorting.", "Use in almost every empirical comps answer to motivate research design."),
}


def write_file(path: Path, content: str, overwrite: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        return
    path.write_text(content.strip() + "\n", encoding="utf-8")


def literature_map(topic: str) -> str:
    desc = LITERATURE_DESCRIPTIONS[topic]
    return f"""---
type: literature-map
literature: {topic}
seminar:
related_methods:
related_datasets:
exam_relevance: high
tags:
  - literature-map
  - comps
---

# Literature Map: {topic}

## What Belongs Here
{desc}

## 1. Big Picture
Summarize the central question, the main tradeoff, and why the literature matters for finance.

## 2. Why This Literature Matters
Explain why an examiner might ask about this literature, including its relevance for causality, mechanisms, institutions, or theory.

## 3. Core Mechanisms
1. Financing friction or information problem:
2. Incentive, monitoring, or agency channel:
3. Real effect, price effect, or welfare implication:

## 4. Paper-by-Paper Comparison
| Paper | Question | Data | Method | Identification | Main Finding | Weakness | Exam Use |
|---|---|---|---|---|---|---|---|
| [[Paper 1]] | | | | | | | |

## 5. Main Themes
Group papers by mechanism, data setting, identification strategy, and conclusion.

## 6. Identification Strategies in This Literature
List the major sources of variation, including shocks, instruments, policy changes, cutoffs, event windows, or panel fixed effects.

## 7. Endogeneity Issues
Discuss selection, omitted variables, reverse causality, simultaneity, measurement error, and equilibrium sorting.

## 8. What the Literature Has Established
State the claims that are relatively settled and identify the papers that support them.

## 9. What Remains Unresolved
Identify gaps, conflicting results, measurement problems, external validity limits, and open research questions.

## 10. Likely Comprehensive Exam Questions
- Review the main findings of the literature on {topic}.
- Discuss the data and identification strategies used in this literature.
- Propose a testable hypothesis that extends this literature.

## 11. 10-Minute Answer Outline
1. Define the literature and thesis.
2. Cite two to four core papers.
3. Explain data and identification.
4. Discuss limitations and one extension.

## 12. 30-Minute Answer Outline
1. Opening thesis.
2. Theme 1 with papers and evidence.
3. Theme 2 with papers and evidence.
4. Identification and endogeneity.
5. Gaps, hypotheses, and proposed empirical design.
6. Conclusion.

## 13. Hypotheses for an Original Research Design
H1:
H2:
H3:

## 14. Proposed Empirical Test
- Research question:
- Treatment:
- Control group:
- Data:
- Identification:
- Regression:
- Expected result:
- Contribution:

## 15. Must-Cite Papers
- [[Paper 1]]
- [[Paper 2]]
- [[Paper 3]]

## 16. Memory Hooks
-
-
-
"""


def method_note(method: str) -> str:
    intuition, spec, assumption, threats, examples = METHOD_DETAILS[method]
    return f"""---
type: empirical-design
method: {method}
use_cases:
common_threats:
tags:
  - empirical-design
  - methods
  - comps
---

# {method}

## Intuition
{intuition}

## When to Use
{examples}

## Basic Specification
```text
{spec}
```

## Identification Assumption
{assumption}

## Common Threats
{threats}

## Diagnostics
- Show pre-trends or balance where relevant.
- Explain treatment assignment and why it is plausibly exogenous.
- Test alternative samples, definitions, timing windows, and standard error choices.
- Report economic magnitudes, not only statistical significance.

## Good Finance Examples
- [[Paper 1]] in [[{method}]]
- Add seminar-specific examples from [[FINN 6333 Empirical Research in Finance]].

## How to Explain on Comps
Start with the endogeneity problem, identify the source of variation, state the identifying assumption, then explain why the paper partially satisfies it and where it remains vulnerable.

## Memory Hook
Identification is about the source of variation, not the regression table.
"""


def theory_note(topic: str) -> str:
    special = ""
    if topic == "Futures Contract Paying S Squared":
        special = """
## Placeholder PDE Derivation
Assume the underlying follows geometric Brownian motion under the risk-neutral measure:

```text
dS = r S dt + sigma S dW
```

Let tau = T - t and guess:

```text
F(S,tau) = A S^2 exp(B tau)
```

For a derivative value V(S,t), the Black-Scholes PDE is:

```text
V_t + r S V_S + 0.5 sigma^2 S^2 V_SS - r V = 0
```

Substitute the guessed form and solve for B. The algebra depends on whether the object is a futures price, forward price, or derivative value. Verify before memorizing.

Candidate result to verify before memorizing:

```text
E_t^Q[S_T^2] = S_t^2 exp((2r + sigma^2) tau)
```
"""
    return f"""---
type: theory-derivation
topic: {topic}
seminar: FINN 60403 Finance Theory
difficulty:
tags:
  - theory
  - derivation
  - comps
---

# {topic}

## Goal
State what must be derived and the final object the exam answer should produce.

## Setup
Define assets, payoffs, information, timing, and preferences or pricing assumptions.

## Assumptions
- No arbitrage or equilibrium pricing condition:
- Complete or incomplete markets:
- Risk preferences:
- Distributional assumptions:

## Notation
- S_t:
- R_i:
- m:
- beta:
- sigma:

## Step-by-Step Derivation
1. Write the pricing condition.
2. Substitute the payoff or return.
3. Rearrange into the target expression.
4. State the final formula clearly.
{special}

## Economic Intuition
Explain why the formula prices risk, discounts cash flows, or maps covariance with marginal utility into expected return.

## Common Mistakes
- Confusing physical and risk-neutral probabilities.
- Forgetting timing.
- Dropping covariance terms without justification.
- Writing a formula without defining notation.

## Final Formula
Write the final formula here after verifying the derivation.

## How to Write This Under Exam Conditions
Begin with assumptions, show the core equation, complete the algebra, then add one sentence of economic intuition.

## Memory Hook
Pricing is a restriction on payoffs across states, not just a discounting shortcut.
"""


def dataset_note(dataset: str) -> str:
    return f"""---
type: dataset
dataset: {dataset}
used_in_literatures:
common_variables:
tags:
  - dataset
---

# {dataset}

## What It Measures
Describe the economic objects captured by {dataset}.

## Unit of Observation
Firm, security, loan, patent, bank, branch, household, deal, or other unit.

## Common Variables
- Identifier:
- Date:
- Main outcome:
- Controls:

## Papers That Use It
- [[Paper 1]]
- [[Paper 2]]

## Strengths
- Coverage:
- Measurement quality:
- Linkability to other datasets:

## Weaknesses
- Selection:
- Measurement error:
- Missing variables:

## How to Discuss on Comps
Explain what the data measure, why they are appropriate, and what limitations affect interpretation.
"""


FILES = {
    "00 - Comps Dashboard/Home.md": f"""# Finance PhD Comps Vault

## Current Priorities
- [[Master Reading Tracker]]
- [[High Priority Papers]]
- [[Weekly Study Plan]]
- [[Exam Strategy]]
- [[Comps Answer Frameworks]]

## High Priority Literatures
- [[Labor and Finance]]
- [[Securitization]]
- [[Bank Runs and Deposit Insurance]]
- [[Customer-Supplier Shock Propagation]]
- [[Climate Finance and Supply Chains]]
- [[Venture Capital and Entrepreneurship]]
- [[P2P Lending and FinTech]]

## Must-Memorize Theory
{"".join(f"- [[{x}]]\n" for x in THEORY_DERIVATIONS)}
## Must-Cite Papers
- [[Must Cite Papers]]
- Add paper notes that appear repeatedly on past exams.

## Methods to Master
{"".join(f"- [[{x}]]\n" for x in METHODS)}
## Exam Answer Practice
- [[FINN 6333 Empirical Research in Finance]]
- [[FINN 62303 Seminar in Financial Management]]
- [[FINN 67303 Financial Markets and Institutions]]
- [[FINN 6133 Investment Theory]]
- [[FINN 60403 Finance Theory]]
- [[Past Exam Pattern Analysis]]
- [[10 Minute Answer Template]]
- [[30 Minute Answer Template]]
- [[Mock Exam Responses]]

## Literature Maps
{"".join(f"- [[{x}]]\n" for x in LITERATURES)}
""",
    "00 - Comps Dashboard/Master Reading Tracker.md": """# Master Reading Tracker

Use this tracker as the single control sheet for the 300-paper workflow. Add every assigned paper here before creating a full note.

## Status Options
- Unread
- Triaged
- Skimmed
- Deep Read
- Mastered
- Needs Review

## Tracker
| Status | Paper | Literature | Seminar | Method | Identification | Dataset | Exam Relevance | Notes |
|---|---|---|---|---|---|---|---|---|
| Unread | [[Paper Title]] | [[Literature Map]] | [[Seminar]] | [[Method]] | | [[Dataset]] | High/Medium/Low | |

## Instructions
1. Start with [[Fast Triage Prompt]] for every paper.
2. Mark high-priority papers for deep notes using [[Paper Ingestion Prompt]].
3. Link each paper to at least one literature map, one method, and one seminar.
4. Move papers to Mastered only when you can cite the question, data, identification, finding, and weakness from memory.
""",
    "00 - Comps Dashboard/High Priority Papers.md": """# High Priority Papers

Use this note for papers that are likely to appear directly on comps or anchor a literature review.

## Must Deep Read
| Paper | Literature | Why It Matters | Memory Hook |
|---|---|---|---|
| [[Paper Title]] | [[Literature Map]] | | |

## Named in Past Exams
- [[Paper Title]]

## Repeated Across Seminars
- [[Paper Title]]
""",
    "00 - Comps Dashboard/Weekly Study Plan.md": """# Weekly Study Plan

## This Week
| Day | Papers | Literature Map | Practice |
|---|---|---|---|
| Monday | | | |
| Tuesday | | | |
| Wednesday | | | |
| Thursday | | | |
| Friday | | | |
| Saturday | | | |
| Sunday | | | |

## Weekly Targets
- Triage:
- Deep notes:
- Literature maps updated:
- Timed answers:
""",
    "00 - Comps Dashboard/Exam Strategy.md": """# Exam Strategy

## Default Empirical Answer Structure
1. State the research question and thesis.
2. Organize papers by mechanism or identification strategy.
3. For each paper, give data, method, identification, result, and limitation.
4. Discuss endogeneity explicitly.
5. Propose a testable extension.

## Default Theory Answer Structure
1. State assumptions and notation.
2. Write the core pricing or optimization condition.
3. Derive step by step.
4. Interpret the final expression.
5. Mention common mistakes or boundary cases.
""",
    "00 - Comps Dashboard/Comps Answer Frameworks.md": """# Comps Answer Frameworks

## Literature Review Framework
Thesis, mechanisms, paper evidence, identification, gaps, and extension.

## Paper-Specific Framework
Question, setting, data, method, identification, finding, contribution, limitation, and exam use.

## Empirical Design Framework
Question, hypothesis, treatment, control group, data, specification, identifying assumption, threats, and robustness.

## Referee Report Framework
Summary, contribution, strengths, major concerns, identification concerns, suggested tests, and recommendation.

## Theory Derivation Framework
Setup, assumptions, notation, derivation, intuition, final formula, and memory version.
""",
    "01 - Paper Notes/_Paper Note Template.md": PAPER_NOTE_TEMPLATE,
    "01 - Paper Notes/_Fast Triage Template.md": """---
type: triage
status: triaged
title:
authors:
year:
journal:
literature:
seminar:
method:
identification:
exam_relevance:
must_deep_read:
tags:
  - triage
  - paper
  - comps
---

# {{Title}}

## One-Sentence Summary

## Literature

## Main Question

## Main Finding

## Method

## Identification

## Datasets

## Why This Matters for Comps

## Priority
High / Medium / Low

## Next Action
Skip / Skim / Deep Read / Add to Literature Map
""",
    "01 - Paper Notes/_Empirical Paper Template.md": """---
type: paper
paper_type: empirical
status: unread
title:
authors:
year:
journal:
literature:
seminar:
methods:
datasets:
exam_relevance: medium
tags:
  - empirical
  - paper
  - comps
---

# {{Title}}

## One-Sentence Takeaway

## Research Question

## Treatment or Shock

## Control Group

## Identifying Variation
What variation identifies beta, and why is it plausibly exogenous?

## Data
| Item | Details |
|---|---|
| Unit of observation | |
| Sample | |
| Treatment variable | |
| Outcome variables | |
| Controls | |

## Empirical Specification
```text
Y_it = beta Treatment_it + gamma Controls_it + FE_i + FE_t + epsilon_it
```

## Fixed Effects
- Unit fixed effects:
- Time fixed effects:
- Industry by time fixed effects:
- Geography by time fixed effects:

## Standard Errors
Explain clustering level and why it matches treatment assignment.

## Main Results

## Threats to Validity
- Selection:
- Omitted variables:
- Reverse causality:
- Measurement error:
- Spillovers:
- Equilibrium sorting:

## Alternative Explanations

## Robustness and Placebos

## External Validity

## How to Use on Comps
State the finding, explain the identification, give one weakness, and connect it to [[Endogeneity Problems]].
""",
    "01 - Paper Notes/_Theory Paper Template.md": """---
type: paper
paper_type: theory
status: unread
title:
authors:
year:
journal:
literature:
seminar:
exam_relevance: medium
tags:
  - theory
  - paper
  - comps
---

# {{Title}}

## One-Sentence Takeaway

## Model Environment

## Agents
- Households:
- Firms:
- Intermediaries:
- Investors:
- Regulator:

## Timing
1.
2.
3.

## Assumptions

## Objective Functions

## Constraints

## Equilibrium Concept

## Propositions
| Proposition | Statement | Intuition | Exam Use |
|---|---|---|---|
| 1 | | | |

## Comparative Statics

## Empirical Predictions

## How to Explain the Model on a Closed-Book Exam
Use simple notation, state the economic friction, derive the core result, and translate the proposition into a testable prediction.

## Critique
Which assumptions drive the result, and how realistic are they?
""",
    "01 - Paper Notes/_Referee Report Template.md": """# Referee Report: {{Paper}}

## Summary

## Contribution

## Major Strengths

## Major Concerns

## Identification Concerns

## Data Concerns

## Interpretation Concerns

## Suggested Tests

## Minor Comments

## Recommendation
Reject / R&R / Accept
""",
    "02 - Literature Maps/_Literature Map Template.md": literature_map("Labor and Finance").replace("Labor and Finance", "{{Topic}}").replace(LITERATURE_DESCRIPTIONS["Labor and Finance"], "What belongs in this literature map? Define scope, core papers, institutions, datasets, and methods."),
    "03 - Exam Question Bank/_Exam Question Template.md": """---
type: exam-question
seminar:
topic:
question_type:
related_literatures:
related_papers:
methods:
difficulty:
status:
tags:
  - exam-question
  - comps
---

# Exam Question: {{Topic}}

## Question Text

## Question Type
Literature review / paper-specific / empirical design / referee report / theory derivation / policy explanation / synthesis

## What the Examiner Is Testing

## Papers to Cite

## Answer Thesis

## Answer Outline

## Identification and Endogeneity Issues

## Hypotheses

## Empirical Design

## Strong Conclusion

## 5-Bullet Memory Version
""",
    "03 - Exam Question Bank/_Answer Blueprint Template.md": """# Answer Blueprint: {{Question}}

## Opening Thesis
A strong answer should argue that ___.

## Roadmap
I will discuss:
1.
2.
3.

## Literature Review

## Data and Methods

## Identification

## Critique

## Proposed Extension

## Conclusion
""",
    "03 - Exam Question Bank/Past Exam Pattern Analysis.md": """# Past Exam Pattern Analysis

## Recurring Question Types
1. Literature review and synthesis
2. Paper-specific summary
3. Data and methodology
4. Identification and endogeneity
5. Hypothesis generation
6. Empirical research design
7. Referee report
8. Theory derivation
9. Institutional explanation

## Recurring Phrases to Watch
- Review the main findings
- Discuss the data used
- How do they build causality?
- Pay attention to causality and identification
- Generate testable hypotheses
- Propose empirical tests
- What questions are left unanswered?
- Produce a referee report
- Derive the expression

## General Strategy
For every empirical paper, memorize:
- question,
- data,
- treatment or variation,
- identification,
- main result,
- weakness,
- how it connects to other papers.

For every theory paper, memorize:
- environment,
- assumptions,
- core derivation,
- intuition,
- predictions.
""",
    "04 - Empirical Designs/_Empirical Design Template.md": """---
type: empirical-design
method:
use_cases:
common_threats:
tags:
  - empirical-design
  - methods
  - comps
---

# {{Method}}

## Intuition

## When to Use

## Basic Specification
```text
Y_it = beta Treatment_it + Controls_it + FE_i + FE_t + epsilon_it
```

## Identification Assumption

## Common Threats

## Diagnostics

## Good Finance Examples

## How to Explain on Comps

## Memory Hook
""",
    "05 - Theory Derivations/_Theory Derivation Template.md": """---
type: theory-derivation
topic:
seminar:
difficulty:
tags:
  - theory
  - derivation
  - comps
---

# {{Derivation}}

## Goal

## Setup

## Assumptions

## Notation

## Step-by-Step Derivation

## Economic Intuition

## Common Mistakes

## Final Formula

## How to Write This Under Exam Conditions

## Memory Hook
""",
    "06 - Authors and Datasets/_Author Template.md": """---
type: author
name:
common_literatures:
papers:
tags:
  - author
---

# {{Author}}

## Main Papers

## Literatures

## Methods Associated With This Author

## How to Cite on Comps
""",
    "06 - Authors and Datasets/_Dataset Template.md": """---
type: dataset
dataset:
used_in_literatures:
common_variables:
tags:
  - dataset
---

# {{Dataset}}

## What It Measures

## Unit of Observation

## Common Variables

## Papers That Use It

## Strengths

## Weaknesses

## How to Discuss on Comps
""",
    "07 - Flashcards/_Flashcard Template.md": """# Flashcards: {{Topic}}

## Paper Recall
Q:
A:

## Identification
Q:
A:

## Main Finding
Q:
A:

## Theory
Q:
A:
""",
    "08 - Synthesis Drafts/_Synthesis Answer Template.md": """# Synthesis Answer: {{Topic}}

## Prompt

## Thesis

## 10-Minute Version

## 30-Minute Version

## Papers Cited

## Identification Discussion

## Original Hypotheses

## Proposed Empirical Design

## Conclusion
""",
    "08 - Synthesis Drafts/10 Minute Answer Template.md": """# 10-Minute Comps Answer Template

## Paragraph 1: Thesis and Roadmap

## Paragraph 2: Literature and Main Findings

## Paragraph 3: Data and Identification

## Paragraph 4: Critique and Gaps

## Paragraph 5: Proposed Extension or Conclusion
""",
    "08 - Synthesis Drafts/30 Minute Answer Template.md": """# 30-Minute Comps Answer Template

## 1. Introduction

## 2. Literature Stream 1

## 3. Literature Stream 2

## 4. Data and Methodology

## 5. Identification and Endogeneity

## 6. Synthesis

## 7. Hypotheses

## 8. Empirical Design

## 9. Conclusion
""",
    "09 - Prompts/Paper Ingestion Prompt.md": "You are my Finance PhD comprehensive exam research assistant.\n\nI am building an Obsidian vault for approximately 300 papers. The goal is not just to summarize papers, but to prepare me to synthesize literatures, answer closed-book comprehensive exam questions, propose empirical tests, discuss identification, and cite papers from memory.\n\nWhen I provide a paper, create a Markdown note using the structure below.\n\nRules:\n- Be concise but exam-useful.\n- Prioritize research question, mechanism, data, identification, contribution, and connection to other papers.\n- Explain endogeneity clearly.\n- Identify how this paper would be used in a comprehensive exam answer.\n- Generate testable hypotheses and a possible empirical extension.\n- Include memory hooks.\n- Use internal Obsidian links where appropriate, using double brackets.\n- Do not invent details. If something is missing, say \"Not clear from provided text.\"\n- End with a \"Comps Use\" section that tells me exactly how to deploy this paper in an exam answer.\n- Avoid em dashes.\n\nOutput in Markdown.\n\n" + PAPER_NOTE_TEMPLATE,
    "09 - Prompts/Fast Triage Prompt.md": """You are helping me triage a large set of Finance PhD comprehensive exam readings.

For the paper I provide, do not create a full summary. Instead, classify it quickly.

Return:
- title,
- authors,
- year,
- journal,
- literature,
- seminar,
- research question,
- main finding,
- method,
- identification,
- datasets,
- whether it is likely to be high, medium, or low priority for comps,
- whether I should deep read it,
- which literature map it belongs in,
- 3 memory hooks.

Output as Markdown using the Fast Triage Template.
""",
    "09 - Prompts/Literature Synthesis Prompt.md": """You are helping me synthesize a Finance PhD literature for a closed-book comprehensive exam.

I will provide multiple paper notes from my Obsidian vault. Your job is to synthesize them into an exam-ready literature map.

Organize the literature around:
1. Big research question
2. Core economic mechanisms
3. Main findings across papers
4. Data sources used in the literature
5. Identification strategies
6. Endogeneity problems
7. How the papers agree or conflict
8. Gaps in the literature
9. Testable hypotheses
10. Possible empirical research design
11. A 10-minute comprehensive exam answer outline
12. A 30-minute comprehensive exam answer outline
13. A list of papers I must cite from memory

Use the Literature Map Template.
""",
    "09 - Prompts/Exam Question Conversion Prompt.md": """You are helping me prepare for Finance PhD comprehensive exams.

I will give you a past comprehensive exam question. Convert it into an answer blueprint.

Your output should include:
1. What type of question this is:
   - literature review
   - paper-specific summary
   - empirical design
   - referee report
   - theory derivation
   - policy or institutional explanation
   - synthesis question
2. What the examiner is really testing.
3. The papers I should cite.
4. The answer structure I should use.
5. A thesis paragraph.
6. A detailed outline.
7. The identification and endogeneity issues I should discuss.
8. Possible hypotheses, if the question asks for them.
9. A strong concluding paragraph.
10. A 5-bullet memory version.

Question:
[PASTE QUESTION]
""",
    "09 - Prompts/Referee Report Prompt.md": """You are helping me answer a Finance PhD comprehensive exam question that asks for a referee report.

Given the paper or paper summary, produce:
- one-paragraph summary,
- contribution,
- strengths,
- major concerns,
- identification concerns,
- data concerns,
- interpretation concerns,
- suggested tests,
- recommendation: reject, revise and resubmit, or accept,
- how to phrase this under exam conditions.

Avoid being vague. Use a top-three-finance-journal standard.
""",
    "09 - Prompts/Theory Derivation Prompt.md": """You are helping me prepare for closed-book Finance Theory comprehensive exam questions.

Given a theory topic or problem, produce:
- setup,
- assumptions,
- notation,
- step-by-step derivation,
- intuition after each major step,
- final formula,
- common mistakes,
- compact version I could write from memory in an exam.

If algebra is uncertain, clearly mark it as "verify before memorizing."
""",
    "09 - Prompts/Paper Comparison Prompt.md": """Compare the following papers for comprehensive exam preparation.

Return:
- shared research question,
- how they differ,
- data comparison,
- method comparison,
- identification comparison,
- main findings,
- which paper is more convincing and why,
- how to cite both in the same exam paragraph,
- memory hook for each.
""",
    "09 - Prompts/Flashcard Generation Prompt.md": """Create active-recall flashcards from the paper or literature notes I provide.

Make cards for:
- paper finding,
- data,
- identification,
- mechanism,
- critique,
- literature connection,
- exam use,
- theory formula if relevant.

Use Q/A format.
""",
    "README.md": """# Finance PhD Comps Obsidian Vault

## Purpose
This vault is designed for closed-book Finance PhD comprehensive exam preparation. It helps you ingest papers, classify literatures, memorize must-cite results, compare identification strategies, and practice exam-style answers under time pressure.

## Folder Structure
- `00 - Comps Dashboard`: navigation, tracker, study plan, and answer frameworks.
- `01 - Paper Notes`: full notes, fast triage, empirical notes, theory notes, and referee reports.
- `02 - Literature Maps`: synthesis notes organized by literature.
- `03 - Exam Question Bank`: past exam prompts and answer blueprints.
- `04 - Empirical Designs`: methods, assumptions, threats, and examples.
- `05 - Theory Derivations`: closed-book derivation practice.
- `06 - Authors and Datasets`: author and dataset reference notes.
- `07 - Flashcards`: active recall notes.
- `08 - Synthesis Drafts`: timed answer templates and mock responses.
- `09 - Prompts`: reusable AI prompts.
- `10 - Attachments`: PDFs, tables, and figures.
- `99 - Archive`: old notes or retired materials.

## Workflow
Use [[Home]] as the entry point and [[Master Reading Tracker]] as the control sheet.

## How to Ingest a Paper
1. Add the paper to [[Master Reading Tracker]].
2. Run [[Fast Triage Prompt]] to classify priority.
3. For high-priority papers, use [[Paper Ingestion Prompt]] and save the output in `01 - Paper Notes`.
4. Link the note to its literature, seminar, method, and dataset.

## How to Triage Papers
Use [[_Fast Triage Template]] to capture the minimum useful facts: question, finding, method, identification, dataset, priority, and next action.

## How to Build Literature Maps
After several paper notes exist in a topic, use [[Literature Synthesis Prompt]] to update the relevant literature map. Focus on mechanisms, identification, gaps, and must-cite papers.

## How to Convert Past Exam Questions
Paste each question into [[Exam Question Conversion Prompt]], then save the output using [[_Answer Blueprint Template]].

## How to Prepare for Timed Answers
Use [[10 Minute Answer Template]] for compact synthesis practice and [[30 Minute Answer Template]] for full exam responses.

## Workflow for 300 Papers

### Pass 1: Triage
Use the Fast Triage Prompt for every paper. Decide whether each paper is high, medium, or low priority.

### Pass 2: Deep Notes
Use the full Paper Ingestion Prompt for high-priority papers and named papers from past exams.

### Pass 3: Literature Maps
After 8 to 20 papers in a topic, use the Literature Synthesis Prompt to build a literature map.

### Pass 4: Exam Question Bank
Convert past exam questions into answer blueprints.

### Pass 5: Timed Practice
Use the 10-minute and 30-minute answer templates to practice writing under exam conditions.
""",
}


def build_files(overwrite: bool) -> None:
    dirs = [
        "00 - Comps Dashboard",
        "01 - Paper Notes",
        "02 - Literature Maps",
        "03 - Exam Question Bank",
        "04 - Empirical Designs",
        "05 - Theory Derivations",
        "06 - Authors and Datasets",
        "07 - Flashcards",
        "08 - Synthesis Drafts",
        "09 - Prompts",
        "10 - Attachments/PDFs",
        "10 - Attachments/Tables",
        "10 - Attachments/Figures",
        "99 - Archive",
    ]
    for directory in dirs:
        (VAULT_ROOT / directory).mkdir(parents=True, exist_ok=True)

    all_files = dict(FILES)

    for literature in LITERATURES:
        all_files[f"02 - Literature Maps/{literature}.md"] = literature_map(literature)

    for seminar in SEMINARS:
        all_files[f"03 - Exam Question Bank/{seminar}.md"] = f"""# {seminar}

## Seminar Scope
Use this page to collect exam questions, must-cite papers, recurring methods, and professor-specific patterns for {seminar}.

## Core Literatures
- [[Literature Map]]

## Past Exam Questions
- [[Exam Question: Topic]]

## Must-Cite Papers
- [[Paper Title]]

## Methods or Derivations to Master
- [[Difference in Differences]]
- [[Instrumental Variables]]
- [[Stochastic Discount Factor]]

## Timed Practice
- [[10 Minute Answer Template]]
- [[30 Minute Answer Template]]
"""

    for method in METHODS:
        all_files[f"04 - Empirical Designs/{method}.md"] = method_note(method)

    for topic in THEORY_DERIVATIONS:
        all_files[f"05 - Theory Derivations/{topic}.md"] = theory_note(topic)

    for dataset in DATASETS:
        all_files[f"06 - Authors and Datasets/{dataset}.md"] = dataset_note(dataset)

    flashcards = {
        "Must Cite Papers": "High-value paper recall cards organized by literature.",
        "Identification Flashcards": "Cards for endogeneity problems, assumptions, and diagnostics.",
        "Theory Flashcards": "Cards for formulas, derivations, and intuition.",
        "Banking Flashcards": "Cards for bank runs, deposit insurance, opacity, lending, and regulation.",
        "Corporate Finance Flashcards": "Cards for governance, labor, innovation, PE, VC, and real effects.",
        "Investments Flashcards": "Cards for asset pricing, momentum, liquidity, derivatives, funds, and SDFs.",
    }
    for name, desc in flashcards.items():
        all_files[f"07 - Flashcards/{name}.md"] = f"""# Flashcards: {name}

{desc}

## Paper Recall
Q:
A:

## Identification
Q:
A:

## Main Finding
Q:
A:

## Theory
Q:
A:
"""

    all_files["08 - Synthesis Drafts/Mock Exam Responses.md"] = """# Mock Exam Responses

Use this note to store dated practice answers.

## Response Log
| Date | Question | Time Limit | Self-Grade | Revision Needed |
|---|---|---|---|---|
| | [[Exam Question: Topic]] | 10 / 30 minutes | | |
"""

    for rel_path, content in all_files.items():
        write_file(VAULT_ROOT / rel_path, content, overwrite)


def write_config(overwrite: bool) -> None:
    config = {
        "vault_root": str(VAULT_ROOT),
        "seminars": SEMINARS,
        "literatures": LITERATURES,
        "methods": METHODS,
        "statuses": STATUSES,
        "tags": ["paper", "triage", "comps", "literature-map", "empirical-design", "methods", "theory", "derivation", "dataset", "author"],
        "template_file_names": [
            "_Paper Note Template.md",
            "_Fast Triage Template.md",
            "_Theory Paper Template.md",
            "_Empirical Paper Template.md",
            "_Referee Report Template.md",
            "_Literature Map Template.md",
            "_Exam Question Template.md",
            "_Answer Blueprint Template.md",
            "_Empirical Design Template.md",
            "_Theory Derivation Template.md",
            "_Author Template.md",
            "_Dataset Template.md",
            "_Flashcard Template.md",
            "_Synthesis Answer Template.md",
        ],
    }
    path = Path("vault_config.json")
    if path.exists() and not overwrite:
        return
    path.write_text(json.dumps(config, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create the Finance PhD comps Obsidian vault scaffold.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing vault files.")
    args = parser.parse_args()
    build_files(overwrite=args.overwrite)
    write_config(overwrite=args.overwrite)
    print(f"Created vault scaffold at {VAULT_ROOT.resolve()}")


if __name__ == "__main__":
    main()
