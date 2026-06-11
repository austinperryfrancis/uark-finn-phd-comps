---
type: paper
status: unread
title: "Social Capital and Debt Contracting: Evidence from Bank Loans and Public Bonds"
authors: Iftekhar Hasan, Chun Keung Hoi, Qiang Wu, Hao Zhang
year: 2017
journal: Journal of Financial and Quantitative Analysis
seminar:
field: Corporate Finance
literature: Debt Contracting; Social Capital; Bank Loans; Public Debt; Local Norms
methods: OLS; difference in differences; instrumental variables; logistic regression; PCA
datasets: DealScan; Compustat; NRCRD social capital data; BEA county data; SEC 10-K headquarters data; SDC New Issues
identification: County-level social capital, headquarters relocation DiD, and IV using distance to Canadian border and ethnic homogeneity
main_result: Firms headquartered in high-social-capital counties face lower loan spreads, less restrictive loan terms, lower bond spreads, and greater use of public bonds relative to bank loans.
exam_relevance: high
must_memorize: true
tags:
  - debt-contracting
  - social-capital
  - bank-loans
  - public-bonds
  - moral-hazard
  - local-norms
  - DrJandik
  - difference-in-differences
created: 2026-06-04
updated: 2026-06-04
---

# Hasan, Hoi, Wu, and Zhang 2017

## 1. One-Sentence Takeaway
This paper shows that local social capital lowers firms' cost of debt using U.S. county-level social capital, bank loan contracts, bond issuances, headquarters relocations, and IV tests, and the main contribution is showing that lenders price local cooperative norms as an external constraint on borrower moral hazard.

## 2. Exam-Ready Abstract
Hasan, Hoi, Wu, and Zhang ask whether the local social environment affects debt contracting for public firms. They measure social capital at the U.S. county level using cooperative norms and social network density, then link this measure to bank loan facilities, bond issuances, and debt financing choices from 1990 to 2012. The baseline result is that firms headquartered in counties with higher social capital receive lower bank loan spreads, with a one standard deviation increase in social capital reducing loan spreads by about 4.33 basis points. The paper argues that lenders view social capital as an informal governance mechanism that raises managers' cost of opportunistic behavior against creditors. Identification comes from social-capital-changing headquarters relocations and an IV strategy using distance to the Canadian border and ethnic homogeneity. The paper also finds looser collateral and covenant requirements, lower public bond spreads, and a lower likelihood of choosing bank loans over bonds. This connects to [[Debt Contracting]], [[Moral Hazard]], [[Social Capital]], [[Bank Loans]], and [[Public Debt]].

## 3. Research Question
Does local social capital affect the terms on which firms obtain debt financing?

More specifically: do cooperative norms and dense local social networks reduce creditor concerns about borrower moral hazard, leading to lower loan spreads, less restrictive nonprice loan terms, lower bond spreads, and greater use of public debt?

## 4. Core Mechanism

```text
Higher county-level social capital
-> stronger cooperative norms and denser local networks
-> higher internal and external sanctions for opportunistic behavior
-> managers face a higher perceived cost of expropriating debt holders
-> banks and bond investors perceive lower moral hazard risk
-> lenders offer lower spreads and less restrictive debt contract terms
```

## 5. Main Findings
1. Firms in high-social-capital counties pay lower bank loan spreads. In the baseline model, the coefficient on social capital is negative and significant, and a one standard deviation increase in social capital reduces loan spreads by about 4.33 basis points.
2. The relation is supported by identification tests. Firms relocating to higher-social-capital counties experience larger reductions in loan spreads than firms relocating to lower-social-capital counties. The key DiD coefficient is about -0.128 in the full relocation sample.
3. Social capital affects the full debt contract. High-social-capital firms face lower collateral use, lower covenant use, lower covenant intensity, lower public bond spreads, and are less likely to choose bank loans over public bonds.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Loan facility-year for main loan spread tests; bond-year for bond spread tests; firm-year for debt choice tests |
| Sample period | 1990 to 2012 |
| Main dataset | Thomson Reuters LPC DealScan for bank loans; Compustat for firm financials and headquarters; NRCRD for county social capital; BEA for county demographics; SEC 10-K filings for historical headquarters; SDC New Issues for bonds |
| Key variables | Social capital, loan spread, collateral dummy, covenant dummy, covenant intensity, bond spread, loan versus bond financing choice |
| Treatment or shock | County-level social capital; social-capital-changing headquarters relocations |
| Outcome variables | ln loan spread, collateral requirement, covenant requirement, covenant intensity, ln bond spread, dummy for bank loan versus public bond |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between social capital and debt spreads may not be causal. Firms do not randomly choose headquarters locations, so safer, better governed, or more transparent firms may sort into high-social-capital counties. County social capital may also proxy for unobserved local economic conditions, legal quality, lender competition, education, wealth, or regional industry composition. Reverse causality is less likely, since one firm's loan terms are unlikely to determine county social capital, but omitted variables and equilibrium sorting are serious concerns. Measurement error is also possible because county social capital is observed only in selected years and then filled across missing years.

### Identification Approach
- Natural experiment: Headquarters relocations that change the social capital environment faced by the firm.
- Instrument: Distance to the Canadian border and county ethnic homogeneity.
- Difference in differences: Compare changes in loan spreads before and after relocation for firms moving to higher-social-capital counties versus firms moving to lower-social-capital counties.
- Event study: Not a full event-time graph. The paper uses pre and post relocation windows, including a four-year window robustness test.
- Fixed effects: State, year, industry, loan purpose, and loan type fixed effects in the baseline loan regressions.
- Matching: Not the central design. The relocation diagnostic compares pre-relocation firm characteristics across increasing and decreasing relocation groups.
- Placebo tests: Not clear from provided text.
- Robustness: Controls for religiosity, CSR, accounting quality, tax avoidance, organ donation as an alternative social capital measure, interpolation of social capital, first-time borrower-lender loans, and IV regressions.
- Alternative source of variation: Bond market tests help rule out the idea that the bank loan results are driven only by personal relationships between banks and borrowers.

### Is the Identification Convincing?
- Strength: The headquarters relocation design is intuitive because the same type of firm enters a new social capital environment, and the paper shows similar pre-relocation observable characteristics across relocation groups.
- Weakness: Headquarters moves are endogenous. A firm moving to a higher-social-capital county may also be changing labor markets, tax environments, legal regimes, growth strategy, or local lender access.
- Referee concern: The IV exclusion restriction is debatable. Distance to Canada and ethnic homogeneity may affect credit spreads through regional economic development, local banking markets, demographics, or industry composition, not only through social capital.

## 8. Main Regression or Model

```text
ln(Spread_lit) =
  beta SocialCapital_c,t-1
+ FirmControls_i,t-1
+ LoanControls_l,t
+ CountyControls_c,t-1
+ State FE
+ Industry FE
+ Year FE
+ LoanPurpose FE
+ LoanType FE
+ epsilon_lit
```

The main coefficient is beta. It measures whether firms headquartered in counties with higher social capital pay lower loan spreads, conditional on firm risk, loan characteristics, local demographics, and fixed effects.

For the relocation design:

```text
ln(Spread_lit) =
  beta1 Post_it
+ beta2 SocialCapitalIncreasingRelocation_i
+ beta3 Post_it x SocialCapitalIncreasingRelocation_i
+ Controls
+ State FE
+ Industry FE
+ LoanPurpose FE
+ LoanType FE
+ epsilon_lit
```

Here, beta3 is the main causal coefficient. It measures whether loan spreads fall more after relocation for firms moving to higher-social-capital counties relative to firms moving to lower-social-capital counties. The paper finds beta3 is negative and significant.

For the IV design:

```text
SocialCapital_c,t =
  pi1 ln(BorderDistance_c)
+ pi2 EthnicHomogeneity_c,t
+ Controls
+ Fixed Effects
+ u_c,t
```

```text
ln(Spread_lit) =
  beta FittedSocialCapital_c,t-1
+ Controls
+ Fixed Effects
+ epsilon_lit
```

The second-stage coefficient on fitted social capital is negative and significant, supporting the interpretation that social capital lowers loan spreads.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Debt Contracting]] by showing that informal local institutions affect loan pricing, collateral, covenants, and public bond yields.
2. [[Social Capital]] by showing that local cooperative norms generate measurable corporate financing benefits.
3. [[Moral Hazard]] and [[Corporate Governance]] by treating local social norms as an external governance mechanism that constrains opportunistic behavior.

It differs from prior work because it studies nonreligious social capital rather than formal legal institutions, firm-level governance, accounting quality, or religiosity. It also examines both private bank debt and public bonds, which helps distinguish relationship-lending explanations from broader creditor pricing of local norms.

## 10. Closely Related Papers
- [[Bharath, Sunder, and Sunder 2008]]: Accounting quality affects debt contracting, especially loan spreads and contract terms.
- [[Graham, Li, and Qiu 2008]]: Corporate misreporting affects bank loan spreads, collateral, and covenant restrictions.
- [[Guiso, Sapienza, and Zingales 2004]]: Social capital affects financial development and trust-based financial behavior.
- [[Engelberg, Gao, and Parsons 2012]]: Personal relationships between borrowers and lenders affect loan contracting.
- [[Denis and Mihov 2003]]: Firms choose among bank debt, nonbank private debt, and public debt based on information and agency problems.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on debt contracting and borrower agency problems. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Local social capital lowers debt costs and relaxes loan terms because creditors perceive lower moral hazard.
- Data: DealScan bank loans, Compustat firms, NRCRD county social capital, BEA county controls, SEC headquarters relocations, and SDC bond issuances.
- Identification: Baseline OLS with rich controls and fixed effects, DiD using headquarters relocations, and IV using distance to Canada and ethnic homogeneity.
- Limitation: Headquarters relocations and instruments may be correlated with other local economic changes.
- Connection to other papers: Use with [[Bharath, Sunder, and Sunder 2008]], [[Graham, Li, and Qiu 2008]], and [[Engelberg, Gao, and Parsons 2012]] to show that lenders price accounting quality, misreporting risk, relationships, and local norms.
- Best exam phrase: "Hasan et al. show that informal local institutions act like an external governance mechanism in debt contracting."

## 12. Hypotheses Inspired by This Paper
H1: The effect of social capital on loan spreads should be stronger for opaque firms, because lenders rely more on informal governance when hard information is weaker.

H2: The effect of social capital on nonprice loan terms should be stronger when formal creditor rights or lender monitoring are weaker.

H3: If social capital constrains opportunism, high-social-capital firms should experience smaller spread increases after negative information shocks such as restatements, covenant violations, or credit downgrades.

## 13. Possible Extension or Research Design
- Research question: Does local social capital affect debt renegotiation outcomes after covenant violations?
- Hypothesis: Firms headquartered in high-social-capital counties receive more favorable waivers or renegotiated terms because lenders perceive lower opportunistic intent.
- Data: DealScan covenant data, SEC covenant violation disclosures, Compustat, NRCRD social capital, and loan amendment data.
- Identification: Difference in differences around covenant violations, comparing high-social-capital and low-social-capital counties, with firm and lender fixed effects if data allow.
- Expected result: High-social-capital firms face lower waiver fees, smaller spread step-ups, and less severe collateral tightening after violations.
- Contribution: Extends the paper from initial contract terms to ex post renegotiation and creditor control rights.

## 14. Critiques

### Major Concern 1
Headquarters relocation is not random. Firms may move because of strategic, tax, labor, industry, or financing changes that also affect loan spreads. The DiD helps, but the identifying assumption is still that firms moving to higher versus lower social capital counties would have had parallel spread trends absent the relocation.

### Major Concern 2
The IV exclusion restriction is contestable. Distance to Canada and ethnic homogeneity may affect credit markets through regional economic development, local banking competition, legal culture, demographics, or industry mix.

### Minor Concern
County-level social capital is a broad environmental measure. It is not obvious that the relevant decision makers, lenders, or executives are actually embedded in the county's cooperative networks.

### Referee Recommendation
R&R, because the paper has a novel contribution and a broad set of consistent results, but the causal interpretation depends on relocation and IV assumptions that need careful defense.

## 15. Memory Hooks
- "Social capital as informal creditor protection."
- "County norms lower loan spreads by 4.33 bps."
- "Move to higher social capital, spreads fall more."
- "Not just bank relationships, public bond spreads fall too."
- "Moral hazard channel: norms raise the cost of opportunism."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Debt Contracting]], [[Bank Loans]], [[Moral Hazard]], [[Social Capital]], [[Local Norms]], or [[Public Debt]]. The clean exam answer is: "Hasan, Hoi, Wu, and Zhang use county-level social capital as an informal governance mechanism and show that firms in high-social-capital counties receive lower loan spreads, looser loan terms, lower bond spreads, and rely more on public bonds." Use it to argue that creditors price not only firm fundamentals and formal governance, but also the social environment surrounding the borrower. In a critique answer, emphasize endogenous headquarters sorting and questionable IV exclusion restrictions, but note that the paper is stronger than a standard correlation because it uses social-capital-changing headquarters relocations, alternative social capital measures, and both bank loan and public bond markets.