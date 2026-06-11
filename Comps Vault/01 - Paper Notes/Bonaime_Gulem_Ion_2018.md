---
type: paper
status: unread
title: Does Policy Uncertainty Affect Mergers and Acquisitions?
authors:
  - Alice Bonaime
  - Huseyin Gulen
  - Mihai Ion
year: 2018
journal: Journal of Financial Economics
seminar:
field: Corporate Finance
literature:
  - Mergers and Acquisitions
  - Policy Uncertainty
  - Real Options
  - Corporate Investment
methods:
  - VAR
  - Logit
  - Heckman selection model
  - Cross-sectional heterogeneity
  - Policy uncertainty index
datasets:
  - SDC
  - CRSP
  - Compustat
  - Baker Bloom Davis EPU
  - BEA Input-Output Accounts
  - Census concentration data
  - Hoberg-Phillips TNIC
identification: Aggregate policy uncertainty shocks, firm-level acquisition likelihood models, extensive macro and firm controls, mechanism tests, Heckman selection models, and appendix instruments based on partisan conflict and election uncertainty
main_result: Higher policy uncertainty reduces M&A activity, mainly through a real options channel that increases the value of waiting.
exam_relevance: high
must_memorize: true
tags:
  - mergers-acquisitions
  - policy-uncertainty
  - real-options
  - corporate-investment
  - corporate-finance
  - DrJandik
created: 2026-06-05
updated: 2026-06-05
---

# Bonaime, Gulen, and Ion 2018

## 1. One-Sentence Takeaway
This paper shows that policy uncertainty reduces merger and acquisition activity using the Baker, Bloom, and Davis policy uncertainty index and U.S. M&A data, and the main contribution is showing that policy uncertainty works mainly through a [[Real Options]] channel rather than interim risk, empire-building, or risk management.

## 2. Exam-Ready Abstract
Bonaime, Gulen, and Ion study whether uncertainty about government policy affects M&A activity. The setting is U.S. merger activity from 1985 to 2014, with policy uncertainty measured using the [[Baker, Bloom, and Davis 2016]] policy uncertainty index and its components. At the macro level, a VAR shows that a one standard deviation increase in policy uncertainty is followed by lower aggregate deal value and deal count over the next year. At the firm level, logit models show that higher policy uncertainty predicts a lower probability that a public firm announces an acquisition, even after controlling for investment opportunities, valuations, credit conditions, and general macro uncertainty. The mechanism tests support a real options interpretation: firms delay irreversible acquisitions when uncertainty raises the value of waiting, especially when delay is feasible and policy exposure is high. The paper connects directly to [[Mergers and Acquisitions]], [[Policy Uncertainty]], [[Real Options]], and [[Corporate Investment]].

## 3. Research Question
Does uncertainty about government policy reduce merger and acquisition activity?

More specifically: does policy uncertainty affect M&A through a real options channel, an interim risk channel, an empire-building channel, or a risk-management channel?

## 4. Core Mechanism
Use this chain for comps:

```text
Higher policy uncertainty
-> greater uncertainty about target value, synergies, taxes, regulation, and policy-sensitive cash flows
-> value of waiting rises, especially for irreversible deals
-> firms postpone or abandon acquisitions when delay is feasible
-> aggregate deal value, deal count, and acquisition likelihood fall
```

Selection implication:

```text
High policy uncertainty
-> firms that can wait do wait
-> remaining bidders are those with high costs of delay
-> targets gain bargaining power
-> higher premiums, lower termination fees, and more MAC exclusions
```

## 5. Main Findings
1. Policy uncertainty is negatively associated with aggregate M&A activity. A one standard deviation increase in policy uncertainty is associated with a 6.6% decrease in aggregate deal value and a 3.9% decrease in the number of deals over the next 12 months.
2. At the firm level, higher policy uncertainty reduces acquisition likelihood. Depending on the specification, a one standard deviation increase lowers acquisition probability by roughly 1.1 to 1.6 percentage points, about 9% to 12% of the unconditional acquisition probability.
3. The evidence supports a [[Real Options]] channel. The effect is stronger for more irreversible target investments, firms more exposed to policy uncertainty, and settings where delay is easier.
4. Policy uncertainty does not mainly operate through interim risk or empire-building. The paper finds no strong evidence that high policy uncertainty leads to shorter interim periods, more private targets, worse deal quality, weaker governance effects, or CEO incentive effects.
5. Some evidence supports risk management: firms are more likely to do cross-border and vertical mergers when policy uncertainty is high, but this cannot explain the average negative effect.
6. Deal terms become more target-friendly when policy uncertainty is high: acquirers pay higher premiums, targets face lower termination fees, and contracts include more MAC exclusions.
7. The policy categories that matter most are fiscal policy, taxes, government spending, monetary policy, regulation, and especially financial regulation.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Month for aggregate VARs, firm-year for acquisition likelihood, industry-year for merger waves, acquirer-year or deal-level characteristics for mechanisms |
| Sample period | 1985 to 2014 |
| Main dataset | SDC M&A announcements, CRSP, Compustat, Baker-Bloom-Davis policy uncertainty index |
| Key variables | Policy uncertainty index, M&A deal value, number of deals, acquisition indicator, firm controls, macro controls, target irreversibility, industry competition, policy exposure |
| Treatment or shock | Increases in policy uncertainty, measured using the Baker, Bloom, and Davis index and its components |
| Outcome variables | Aggregate deal value, number of deals, acquisition likelihood, merger wave onset, target type, vertical and foreign acquisition indicators, deal premiums, termination fees, MAC exclusions |

Additional data:
- BEA Input-Output Accounts for vertical mergers and government spending sensitivity.
- Census and Compustat concentration measures for industry competition.
- Hoberg-Phillips TNIC industries for product market competition.
- Macro controls from sources such as Shiller CAPE, VIX/VXO, consumer confidence, credit spreads, and macro uncertainty indices.

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between policy uncertainty and M&A is not causal because policy uncertainty is countercyclical. High policy uncertainty may coincide with recessions, weak investment opportunities, low credit supply, poor valuations, stock market volatility, or low CEO confidence. These factors independently reduce M&A, so policy uncertainty may proxy for bad macroeconomic conditions rather than causing lower acquisition activity. There is also selection into observed deals: when uncertainty is high, only firms with strong motives or high delay costs may still announce deals, so observed deal characteristics are not representative of all potential deals. Measurement error is also possible because the BBD index is based partly on newspaper coverage and may capture media attention or crisis salience.

### Identification Approach
- Natural experiment: Not a clean natural experiment in the main paper.
- Instrument: The Internet Appendix uses plausibly exogenous instruments for policy uncertainty, including partisan conflict and gubernatorial election uncertainty. Heckman tests use mechanical mutual fund outflow induced price pressure as an exclusion restriction for selection into becoming an acquirer.
- Difference in differences: No standard DiD design.
- Event study: VAR impulse responses at the aggregate level. Announcement CARs are used to test deal quality under high versus low policy uncertainty.
- Fixed effects: Fama-French 48 industry fixed effects and time trends in the main firm-level logit models.
- Matching: Not central. Selection is handled mainly through Heckman models in target and deal characteristic tests.
- Placebo tests: Tests for delayed rebound, comparison with VIX, private-target tests, governance interactions, CEO incentive interactions, and policy category tests.
- Robustness: Controls for investment opportunities, industry shocks, credit spreads, valuation waves, general macro uncertainty, elections, and firm characteristics.
- Alternative source of variation: Category-specific policy uncertainty indices and cross-sectional exposure to government spending or policy-sensitive returns.

### Is the Identification Convincing?
- Strength: The paper is strong on mechanisms. It does not just show a negative coefficient. It shows the effect is strongest where real options theory predicts it should be strongest.
- Weakness: The main variation is aggregate time-series variation in policy uncertainty, so causal interpretation depends heavily on controls and the plausibility of the policy uncertainty measure.
- Referee concern: The BBD index may capture broader macroeconomic or media uncertainty. A referee would ask whether the results survive cleaner shocks, such as close elections, regulatory deadlines, court decisions, or sector-specific policy exposure interacted with firm-level pre-exposure.

## 8. Main Regression or Model

Main firm-level acquisition likelihood model:

```text
Pr(Acquirer_i,t+1 = 1) =
  F(
    beta PolicyUncertainty_t
  + FirmControls_i,t
  + MacroControls_t
  + Industry FE
  + Time trend
  + epsilon_i,t
  )
```

The dependent variable equals one if firm i announces an acquisition in year t+1. The key coefficient is beta. A negative beta means that higher policy uncertainty in year t predicts a lower probability of announcing an acquisition in the next year, conditional on firm characteristics, macro conditions, valuation waves, industry shocks, and general uncertainty.

Mechanism model with heterogeneity:

```text
Pr(Acquirer_i,t+1 = 1) =
  F(
    beta1 PolicyUncertainty_t
  + beta2 Heterogeneity_i,t
  + beta3 PolicyUncertainty_t x Heterogeneity_i,t
  + FirmControls_i,t
  + MacroControls_t
  + Industry FE
  + Time trend
  + epsilon_i,t
  )
```

The main economic interpretation is beta3. If heterogeneity measures policy exposure or low ability to delay, beta3 shows whether policy uncertainty has a stronger or weaker effect for firms predicted by real options theory.

Aggregate VAR intuition:

```text
M&AActivity_t =
  f(
    lagged M&A activity,
    lagged policy uncertainty,
    market volatility,
    market returns,
    credit spreads,
    CAPE,
    aggregate cash,
    time trend
  )
```

The VAR asks how aggregate M&A value and volume respond over time after a policy uncertainty shock.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Mergers and Acquisitions]] by identifying policy uncertainty as a determinant of merger waves and firm acquisition decisions.
2. [[Policy Uncertainty]] by showing that uncertainty affects not only capital expenditures and equity issuance, but also major corporate control transactions.
3. [[Real Options]] by providing evidence that uncertainty reduces irreversible investment when the option to wait is valuable.

It differs from prior work because it separates policy uncertainty from general uncertainty and shows that different uncertainty measures imply different mechanisms. [[Bhagwat, Dam, and Harford 2016]] emphasize interim risk and the seller's put using VIX. Bonaime, Gulen, and Ion emphasize longer-horizon policy uncertainty and the bidder's option to delay.

## 10. Closely Related Papers
- [[Baker, Bloom, and Davis 2016]]: Provides the policy uncertainty index used as the paper's core treatment variable.
- [[Gulen and Ion 2016]]: Shows policy uncertainty reduces corporate investment, closely related to the real options interpretation.
- [[Julio and Yook 2012]]: Studies political uncertainty and corporate investment around elections.
- [[Harford 2005]]: Merger waves depend on industry shocks and capital liquidity, which this paper controls for and extends.
- [[Bhagwat, Dam, and Harford 2016]]: Shows market volatility affects M&A through interim risk, contrasting with this paper's real options channel.
- [[Garfinkel and Hankins 2011]]: Shows firms use vertical mergers for risk management, related to this paper's vertical merger tests.
- [[Duchin and Schmidt 2013]]: Links merger waves, uncertainty, limited attention, and empire-building, which this paper tests and largely rejects for policy uncertainty.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on uncertainty and corporate investment. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Policy uncertainty reduces M&A activity, especially when deals are irreversible and delay is feasible.
- Data: SDC M&A data linked to CRSP/Compustat, 1985 to 2014, plus the Baker-Bloom-Davis policy uncertainty index.
- Identification: Lagged policy uncertainty in firm-level logit models with rich macro and firm controls, plus VARs, Heckman selection models, cross-sectional mechanism tests, and appendix instruments.
- Limitation: The core policy uncertainty variation is aggregate and may still be correlated with omitted macro shocks.
- Connection to other papers: Use it with [[Gulen and Ion 2016]] for investment, [[Julio and Yook 2012]] for elections, [[Harford 2005]] for merger waves, and [[Bhagwat, Dam, and Harford 2016]] for uncertainty and M&A.
- Best exam phrase: "Bonaime, Gulen, and Ion show that policy uncertainty depresses M&A mainly by increasing the real option value of waiting, not by increasing interim risk."

## 12. Hypotheses Inspired by This Paper
H1: Firms with greater exposure to policy uncertainty are less likely to announce acquisitions when policy uncertainty rises.

H2: The negative effect of policy uncertainty on acquisition likelihood is stronger for acquisitions of targets with more irreversible assets.

H3: Among deals announced during high policy uncertainty periods, target firms receive more favorable contract terms because the remaining bidders are selected from firms with high delay costs.

## 13. Possible Extension or Research Design
- Research question: Do firms substitute flexible investment modes for acquisitions when policy uncertainty rises?
- Hypothesis: When policy uncertainty is high, firms reduce full acquisitions but increase minority stakes, alliances, joint ventures, or option-like investment structures.
- Data: SDC acquisitions, SDC alliances or joint ventures, Compustat, CRSP, firm-level geographic or segment exposure, state or industry policy uncertainty measures.
- Identification: Use close gubernatorial elections, staggered regulatory rulemaking deadlines, or sector-specific policy shocks interacted with pre-determined firm exposure. Include firm fixed effects and industry-year fixed effects.
- Expected result: Policy-exposed firms delay irreversible acquisitions but substitute toward more reversible or staged forms of investment.
- Contribution: Extends [[Real Options]] and [[Mergers and Acquisitions]] by showing that uncertainty changes not only whether firms invest, but also how they structure investment flexibility.

## 14. Critiques

### Major Concern 1
The policy uncertainty index is aggregate and countercyclical. Even with many controls, it may capture broad economic stress, pessimism, political conflict, media attention, or crisis periods rather than an exogenous policy uncertainty shock.

### Major Concern 2
The mechanism tests are compelling but still indirect. Irreversibility, concentration, government spending sensitivity, and return sensitivity are proxies. They support real options theory, but they do not directly observe managers choosing to delay specific acquisition opportunities.

### Minor Concern
Unobserved abandoned or never-initiated acquisition negotiations are hard to measure. SDC captures announced deals, so the paper infers lost or delayed deals from observed acquisition likelihood rather than observing the full set of potential deals.

### Referee Recommendation
Accept, because the paper asks an important corporate finance question, uses strong data, distinguishes competing mechanisms, and provides exam-useful evidence on real options. The causal language should remain careful because the main variation is not a clean natural experiment.

## 15. Memory Hooks
- "Policy uncertainty makes waiting valuable."
- "VIX is short horizon seller's put; EPU is long horizon option to delay."
- "Irreversible targets disappear when policy uncertainty rises."
- "If only no-delay bidders remain, targets gain bargaining power."
- "Fiscal, monetary, and regulatory uncertainty matter most."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Mergers and Acquisitions]], [[Policy Uncertainty]], [[Real Options]], [[Corporate Investment]], or [[Merger Waves]]. The clean exam answer is: "Bonaime, Gulen, and Ion use the Baker-Bloom-Davis policy uncertainty index and U.S. M&A data to show that policy uncertainty reduces acquisition activity, especially for irreversible deals and policy-sensitive firms." Use it to argue that uncertainty can affect corporate policy through the option value of waiting, not just through financing constraints or macro weakness. In a critique answer, emphasize that aggregate policy uncertainty may be endogenous to the macroeconomy, but note that the paper is stronger than a standard correlation because it controls for investment opportunities, valuations, credit conditions, and general uncertainty, then validates the mechanism through cross-sectional real options predictions.