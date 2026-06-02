---
type: empirical-design
method: Fixed Effects
use_cases:
common_threats:
tags:
  - empirical-design
  - methods
  - comps
---

# Fixed Effects

## Intuition
Absorb time-invariant unit heterogeneity and common time shocks.

## When to Use
Use as a baseline control structure in panel finance settings.

## Basic Specification
```text
Y_it = beta X_it + FE_i + FE_t + epsilon_it
```

## Identification Assumption
Remaining within-unit changes in X are conditionally exogenous.

## Common Threats
Time-varying omitted variables, bad controls, limited within variation, over-control.

## Diagnostics
- Show pre-trends or balance where relevant.
- Explain treatment assignment and why it is plausibly exogenous.
- Test alternative samples, definitions, timing windows, and standard error choices.
- Report economic magnitudes, not only statistical significance.

## Good Finance Examples
- [[Paper 1]] in [[Fixed Effects]]
- Add seminar-specific examples from [[FINN 6333 Empirical Research in Finance]].

## How to Explain on Comps
Start with the endogeneity problem, identify the source of variation, state the identifying assumption, then explain why the paper partially satisfies it and where it remains vulnerable.

## Memory Hook
Identification is about the source of variation, not the regression table.
