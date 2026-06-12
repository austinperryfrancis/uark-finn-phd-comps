---
type: empirical-design
tags:
method: Matching and PSM
use_cases:
common_threats:
---

# Matching and PSM

## Intuition
Construct a comparison group with similar observable characteristics.

## When to Use
Use when treatment is not randomized but rich observables are available.

## Basic Specification
```text
Match treated and control units on propensity score or covariates, then compare outcomes.
```

## Identification Assumption
Selection on observables: after conditioning on matched variables, treatment is as good as random.

## Common Threats
Unobserved selection, poor overlap, model dependence, post-treatment matching variables.

## Diagnostics
- Show pre-trends or balance where relevant.
- Explain treatment assignment and why it is plausibly exogenous.
- Test alternative samples, definitions, timing windows, and standard error choices.
- Report economic magnitudes, not only statistical significance.

## Good Finance Examples
- [[Paper 1]] in [[Matching and PSM]]
- Add seminar-specific examples from [[FINN 6333 Empirical Research in Finance]].

## How to Explain on Comps
Start with the endogeneity problem, identify the source of variation, state the identifying assumption, then explain why the paper partially satisfies it and where it remains vulnerable.

## Memory Hook
Identification is about the source of variation, not the regression table.
