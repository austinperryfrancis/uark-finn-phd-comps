---
type: empirical-design
method: Event Studies
use_cases:
common_threats:
tags:
  - empirical-design
  - methods
  - comps
---

# Event Studies

## Intuition
Estimate outcome dynamics around a dated event or shock.

## When to Use
Use for announcements, fraud revelation, CEO turnover, credit rating changes, or policy events.

## Basic Specification
```text
Y_it = alpha + sum_k beta_k EventTime_{i,t+k} + FE_i + FE_t + epsilon_it
```

## Identification Assumption
The event is not anticipated in a way that drives pre-event trends, and no confounding shock occurs at the same time.

## Common Threats
Confounding events, anticipation, event clustering, abnormal return model choice, window selection.

## Diagnostics
- Show pre-trends or balance where relevant.
- Explain treatment assignment and why it is plausibly exogenous.
- Test alternative samples, definitions, timing windows, and standard error choices.
- Report economic magnitudes, not only statistical significance.

## Good Finance Examples
- [[Paper 1]] in [[Event Studies]]
- Add seminar-specific examples from [[FINN 6333 Empirical Research in Finance]].

## How to Explain on Comps
Start with the endogeneity problem, identify the source of variation, state the identifying assumption, then explain why the paper partially satisfies it and where it remains vulnerable.

## Memory Hook
Identification is about the source of variation, not the regression table.
