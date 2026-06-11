---
type: empirical-design
method: Placebo Tests
use_cases:
common_threats:
tags:
  - empirical-design
  - methods
  - comps
---

# Placebo Tests

## Intuition
Test whether the design finds effects where it should not.

## When to Use
Use to support DiD, event studies, IV exclusion restrictions, and mechanism claims.

## Basic Specification
```text
Estimate the main specification on fake outcomes, fake treatment timing, or untreated samples.
```

## Identification Assumption
A credible design should not produce treatment effects before treatment or on outcomes unrelated to the mechanism.

## Common Threats
Placebos can be underpowered or selected after seeing results.

## Diagnostics
- Show pre-trends or balance where relevant.
- Explain treatment assignment and why it is plausibly exogenous.
- Test alternative samples, definitions, timing windows, and standard error choices.
- Report economic magnitudes, not only statistical significance.

## Good Finance Examples
- 
- 

## How to Explain on Comps
Start with the endogeneity problem, identify the source of variation, state the identifying assumption, then explain why the paper partially satisfies it and where it remains vulnerable.

## Memory Hook
Identification is about the source of variation, not the regression table.
