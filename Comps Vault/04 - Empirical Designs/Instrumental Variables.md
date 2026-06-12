---
type: empirical-design
tags:
method: Instrumental Variables
use_cases:
common_threats:
---

# Instrumental Variables

## Intuition
Use external variation in an endogenous regressor that affects the outcome only through that regressor.

## When to Use
Use for credit supply, financial constraints, peer effects, or endogenous treatment choice.

## Basic Specification
```text
Y_i = beta Xhat_i + gamma Controls_i + epsilon_i, with first stage X_i = pi Z_i + controls + nu_i
```

## Identification Assumption
Relevance and exclusion: the instrument predicts treatment and has no direct effect on the outcome.

## Common Threats
Weak instruments, invalid exclusion, monotonicity failures, local average treatment interpretation.

## Diagnostics
- Show pre-trends or balance where relevant.
- Explain treatment assignment and why it is plausibly exogenous.
- Test alternative samples, definitions, timing windows, and standard error choices.
- Report economic magnitudes, not only statistical significance.

## Good Finance Examples
- [[Paper 1]] in [[Instrumental Variables]]
- Add seminar-specific examples from [[FINN 6333 Empirical Research in Finance]].

## How to Explain on Comps
Start with the endogeneity problem, identify the source of variation, state the identifying assumption, then explain why the paper partially satisfies it and where it remains vulnerable.

## Memory Hook
Identification is about the source of variation, not the regression table.
