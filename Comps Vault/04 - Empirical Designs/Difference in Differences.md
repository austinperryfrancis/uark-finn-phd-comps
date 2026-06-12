---
type: empirical-design
tags:
method: Difference in Differences
use_cases:
common_threats:
---

# Difference in Differences

## Intuition
Compare changes in outcomes for treated and control units before and after a shock.

## When to Use
Use for regulatory shocks, geographic rollouts, bank deregulation, cap-and-trade exposure, or credit supply disruptions.

## Basic Specification
```text
Y_it = alpha + beta Treat_i x Post_t + gamma X_it + FE_i + FE_t + epsilon_it
```

## Identification Assumption
Parallel trends: absent treatment, treated and control units would have followed similar outcome trends.

## Common Threats
Differential pre-trends, anticipation, spillovers, treatment timing bias, compositional changes.

## Diagnostics
- Show pre-trends or balance where relevant.
- Explain treatment assignment and why it is plausibly exogenous.
- Test alternative samples, definitions, timing windows, and standard error choices.
- Report economic magnitudes, not only statistical significance.

## Good Finance Examples
- [[Paper 1]] in [[Difference in Differences]]
- Add seminar-specific examples from [[FINN 6333 Empirical Research in Finance]].

## How to Explain on Comps
Start with the endogeneity problem, identify the source of variation, state the identifying assumption, then explain why the paper partially satisfies it and where it remains vulnerable.

## Memory Hook
Identification is about the source of variation, not the regression table.
