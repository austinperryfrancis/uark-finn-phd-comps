---
type: empirical-design
method: Natural Experiments
use_cases:
common_threats:
tags:
  - empirical-design
  - methods
  - comps
---

# Natural Experiments

## Intuition
Use an institutional shock that changes incentives or constraints for some units but not others.

## When to Use
Use for law changes, geographic shocks, court rulings, climate policies, or banking deregulation.

## Basic Specification
```text
Y_it = alpha + beta Exposure_i x Shock_t + controls + FE_i + FE_t + epsilon_it
```

## Identification Assumption
Shock exposure is plausibly exogenous to potential outcomes after controls and fixed effects.

## Common Threats
Endogenous exposure, simultaneous shocks, equilibrium responses, spillovers.

## Diagnostics
- Show pre-trends or balance where relevant.
- Explain treatment assignment and why it is plausibly exogenous.
- Test alternative samples, definitions, timing windows, and standard error choices.
- Report economic magnitudes, not only statistical significance.

## Good Finance Examples
- [[Paper 1]] in [[Natural Experiments]]
- Add seminar-specific examples from [[FINN 6333 Empirical Research in Finance]].

## How to Explain on Comps
Start with the endogeneity problem, identify the source of variation, state the identifying assumption, then explain why the paper partially satisfies it and where it remains vulnerable.

## Memory Hook
Identification is about the source of variation, not the regression table.
