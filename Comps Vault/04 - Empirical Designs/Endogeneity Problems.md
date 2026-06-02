---
type: empirical-design
method: Endogeneity Problems
use_cases:
common_threats:
tags:
  - empirical-design
  - methods
  - comps
---

# Endogeneity Problems

## Intuition
Identify why a simple correlation may not estimate a causal effect.

## When to Use
Use in almost every empirical comps answer to motivate research design.

## Basic Specification
```text
Y_i = beta X_i + controls + epsilon_i, where Cov(X_i, epsilon_i) may not equal zero
```

## Identification Assumption
Causal interpretation requires treatment variation unrelated to unobserved determinants of outcomes.

## Common Threats
Selection, omitted variables, reverse causality, simultaneity, measurement error, equilibrium sorting.

## Diagnostics
- Show pre-trends or balance where relevant.
- Explain treatment assignment and why it is plausibly exogenous.
- Test alternative samples, definitions, timing windows, and standard error choices.
- Report economic magnitudes, not only statistical significance.

## Good Finance Examples
- [[Paper 1]] in [[Endogeneity Problems]]
- Add seminar-specific examples from [[FINN 6333 Empirical Research in Finance]].

## How to Explain on Comps
Start with the endogeneity problem, identify the source of variation, state the identifying assumption, then explain why the paper partially satisfies it and where it remains vulnerable.

## Memory Hook
Identification is about the source of variation, not the regression table.
