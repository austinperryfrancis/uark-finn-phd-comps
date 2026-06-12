---
type: theory-derivation
seminar: FINN 60403 Finance Theory
tags:
topic: Futures Contract Paying S Squared
difficulty:
---

# Futures Contract Paying S Squared

## Goal
State what must be derived and the final object the exam answer should produce.

## Setup
Define assets, payoffs, information, timing, and preferences or pricing assumptions.

## Assumptions
- No arbitrage or equilibrium pricing condition:
- Complete or incomplete markets:
- Risk preferences:
- Distributional assumptions:

## Notation
- S_t:
- R_i:
- m:
- beta:
- sigma:

## Step-by-Step Derivation
1. Write the pricing condition.
2. Substitute the payoff or return.
3. Rearrange into the target expression.
4. State the final formula clearly.

## Placeholder PDE Derivation
Assume the underlying follows geometric Brownian motion under the risk-neutral measure:

```text
dS = r S dt + sigma S dW
```

Let tau = T - t and guess:

```text
F(S,tau) = A S^2 exp(B tau)
```

For a derivative value V(S,t), the Black-Scholes PDE is:

```text
V_t + r S V_S + 0.5 sigma^2 S^2 V_SS - r V = 0
```

Substitute the guessed form and solve for B. The algebra depends on whether the object is a futures price, forward price, or derivative value. Verify before memorizing.

Candidate result to verify before memorizing:

```text
E_t^Q[S_T^2] = S_t^2 exp((2r + sigma^2) tau)
```


## Economic Intuition
Explain why the formula prices risk, discounts cash flows, or maps covariance with marginal utility into expected return.

## Common Mistakes
- Confusing physical and risk-neutral probabilities.
- Forgetting timing.
- Dropping covariance terms without justification.
- Writing a formula without defining notation.

## Final Formula
Write the final formula here after verifying the derivation.

## How to Write This Under Exam Conditions
Begin with assumptions, show the core equation, complete the algebra, then add one sentence of economic intuition.

## Memory Hook
Pricing is a restriction on payoffs across states, not just a discounting shortcut.
