---
type: empirical-design
tags:
method: Robustness Tests
use_cases:
common_threats:
---

# Robustness Tests

## Intuition
Evaluate whether results survive reasonable alternative specifications.

## When to Use
Use to defend a result but explain that robustness is not a substitute for identification.

## Basic Specification
```text
Re-estimate with alternative samples, controls, windows, definitions, clustering, and functional forms.
```

## Identification Assumption
The core result should not depend on one fragile modeling choice.

## Common Threats
Specification searching, weak theory for alternatives, robustness that does not address identification.

## Diagnostics
- Show pre-trends or balance where relevant.
- Explain treatment assignment and why it is plausibly exogenous.
- Test alternative samples, definitions, timing windows, and standard error choices.
- Report economic magnitudes, not only statistical significance.

## Good Finance Examples
- [[Paper 1]] in [[Robustness Tests]]
- Add seminar-specific examples from [[FINN 6333 Empirical Research in Finance]].

## How to Explain on Comps
Start with the endogeneity problem, identify the source of variation, state the identifying assumption, then explain why the paper partially satisfies it and where it remains vulnerable.

## Memory Hook
Identification is about the source of variation, not the regression table.
