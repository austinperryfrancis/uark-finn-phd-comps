---
type: empirical-design
method: Regression Discontinuity
use_cases:
common_threats:
tags:
  - empirical-design
  - methods
  - comps
---

# Regression Discontinuity

## Intuition
Exploit a treatment rule that changes discontinuously at a cutoff.

## When to Use
Use for credit scores, index inclusion, regulatory thresholds, or eligibility rules.

## Basic Specification
```text
Y_i = alpha + tau AboveCutoff_i + f(RunningVariable_i) + epsilon_i
```

## Identification Assumption
Units just above and below the cutoff are comparable and cannot precisely manipulate assignment.

## Common Threats
Manipulation, sorting, bandwidth sensitivity, functional form, multiple cutoffs.

## Diagnostics
- Show pre-trends or balance where relevant.
- Explain treatment assignment and why it is plausibly exogenous.
- Test alternative samples, definitions, timing windows, and standard error choices.
- Report economic magnitudes, not only statistical significance.

## Good Finance Examples
- [[Paper 1]] in [[Regression Discontinuity]]
- Add seminar-specific examples from [[FINN 6333 Empirical Research in Finance]].

## How to Explain on Comps
Start with the endogeneity problem, identify the source of variation, state the identifying assumption, then explain why the paper partially satisfies it and where it remains vulnerable.

## Memory Hook
Identification is about the source of variation, not the regression table.
