---
type: paper
status: unread
title: 'Banking on Carbon: Corporate Lending and Cap-and-Trade Policy'
authors: Ivan T. Ivanov; Mathias S. Kruttli; Sumudu W. Watugala
year: 2024
journal: Review of Financial Studies
professor: DrJandik
seminar: Not clear from provided text
jandik_paper_number: 47
jandik_week: 12
jandik_topic: Climate finance
jandik_done: false
field: Corporate Finance; Banking; Climate Finance
literature:
- '[[Climate Finance and Supply Chains]]'
- Bank Lending
- Transition Risk
- Debt Contracting
methods:
- Difference-in-differences
- regulatory natural experiments
- threshold-based treatment
- loan-level panel regressions
datasets:
- EPA GHG Reporting Program
- Federal Reserve Y14
- Shared National Credit Program
identification: California emissions exposure and Waxman-Markey 5% energy-intensity free-permit threshold
main_result: Banks respond to transition risk by shortening loan maturities, reducing term-loan financing, raising interest rates for private emitters, and transferring some exposure to shadow banks.
exam_relevance: high
must_memorize: true
tags:
- climate-finance
- bank-lending
- transition-risk
- debt-contracting
- private-firms
- cap-and-trade
- difference-in-differences
created: 2026-06-12
updated: 2026-06-12
---

# Ivanov, Kruttli, and Watugala 2024

## 1. One-Sentence Takeaway
This paper shows that banks quickly manage climate transition risk by tightening loan contract terms for high-emitting firms using California cap-and-trade exposure and the Waxman-Markey free-permit threshold, and the main contribution is showing that [[Bank Lending]] adjusts through debt structure, not only loan prices.

## 2. Exam-Ready Abstract
Ivanov, Kruttli, and Watugala study whether carbon-pricing policy affects bank credit to greenhouse-gas-emitting firms. They use two U.S. cap-and-trade settings: California’s cap-and-trade program, where treatment intensity is the share of a firm’s emissions located in California, and the Waxman-Markey bill, where manufacturing firms just below a 5% energy-intensity threshold would not receive free permits. They combine EPA facility-level emissions data with Federal Reserve Y14 loan data and Shared National Credit syndicated loan data. The main result is that affected high-emission firms face shorter maturities, less term-loan financing, higher interest rates, and greater shadow-bank participation in loan syndicates. The effects are concentrated among private firms, consistent with private firms being more financially constrained and more emissions-inefficient than public firms. The paper contributes to [[Climate Finance]], [[Bank Lending]], [[Debt Contracting]], and [[Transition Risk]] by showing that banks actively manage climate policy risk through contract flexibility.

## 3. Research Question
What happens to bank lending when climate policy makes high-emitting borrowers riskier?

More specifically, the paper tests whether banks respond to transition risk by:
1. reducing exposure at default through shorter maturities and less permanent credit,
2. increasing compensation through loan rates,
3. shifting exposure toward nonbank lenders,
4. treating private firms differently from public firms.

## 4. Core Mechanism

```text
Cap-and-trade policy becomes likely or legally binding
-> high-emitting firms face higher and more uncertain operating costs
-> borrower cash flow falls or becomes riskier, raising PD and LGD
-> banks reduce EAD and demand flexibility through loan renegotiation
-> affected firms receive shorter maturities, more credit lines, fewer term loans, and higher rates
```

Memory version:

```text
Carbon price
-> cash-flow risk
-> bank expected loss rises
-> banks shorten, reprice, and make credit more revocable
-> private emitters bear the largest financing tightening
```

## 5. Main Findings
1. High-emitting firms affected by California cap-and-trade experience shorter maturities, about 5 months for the full sample, and a large decline in term-loan share, about 25 percentage points.
2. The effects are much stronger for private firms: private treated firms face maturity reductions of roughly 11 to 12 months and large declines in term-loan financing, while public firms are largely unaffected.
3. Treated private firms face higher loan interest rates, up to about 1.6 to 1.7 percentage points in the California setting.
4. In the Waxman-Markey setting, firms below the free-permit threshold face shorter maturities and lower term-loan shares, especially private firms and firms closer to the 5% energy-intensity cutoff.
5. Banks with high ex ante exposure to high-emitting firms reduce exposure more, and shadow banks, including CLOs, take larger syndicate shares in treated firms.
6. After California implementation, private treated firms have lower profitability, higher cash holdings, and lower capital expenditures.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Firm-quarter for California Y14 analysis; firm-year for Waxman-Markey SNC analysis; lender-firm-year for syndicate exposure tests |
| Sample period | California baseline: 2011Q3 to 2011Q4 versus 2012Q3 to 2012Q4; Waxman-Markey baseline: 2008 versus 2009 |
| Main dataset | EPA facility-level GHG emissions; Federal Reserve Y14 loan-level data; Shared National Credit Program syndicated loan data |
| Key variables | California emissions share; free-permit eligibility; committed credit; remaining maturity; term-loan share; interest rates; private/public status; shadow-bank loan share; cash-flow covenants |
| Treatment or shock | California cap-and-trade exposure based on share of firm emissions in California; Waxman-Markey treatment based on being below the 5% energy-intensity free-permit threshold |
| Outcome variables | Log committed credit; loan maturity; term-loan share; interest rate; bank and nonbank syndicate exposure; covenant use; profitability; cash holdings; capital expenditures |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between emissions and loan terms would not be causal because high-emitting firms differ systematically from low-emitting firms. They may be larger, more asset-intensive, more cyclical, more regulated, more dependent on external finance, or concentrated in industries with different credit risk. Banks may also select into lending relationships with polluting firms based on private information. Reverse causality is also possible if financially constrained firms underinvest in cleaner technology and therefore have higher emissions. The paper needs variation in climate policy exposure that is not just a proxy for firm quality, industry risk, or lender selection.

### Identification Approach
- Natural experiment: Two policy shocks, California cap-and-trade and Waxman-Markey, create transition-risk realizations.
- Instrument: No formal instrument.
- Difference in differences: California analysis compares firms with high versus low California emissions share before and after the California bill. Waxman-Markey compares firms below versus above the 5% free-permit cutoff before and after the bill passed the House.
- Event study: Not the central design in the provided text.
- Fixed effects: California regressions include firm fixed effects and industry-quarter fixed effects. Waxman-Markey regressions include firm fixed effects, year fixed effects, and lead-bank fixed effects.
- Matching: EPA emitters are matched to loan data using name and ZIP code with fuzzy matching and manual verification. This is data construction, not the core causal estimator.
- Placebo tests: Nonpolluting firms with California presence do not show the same material loan-term changes, which supports the climate-policy interpretation.
- Robustness: Uses continuous and discrete California emissions treatment; uses two Waxman-Markey bandwidths around the 5% threshold; checks results using only 2011 emissions; examines public versus private firms; addresses concern that energy-price movements confound the Waxman-Markey design.
- Alternative source of variation: The paper has two independent designs with different timing, datasets, and treatment assignment, which is a major strength.

### Is the Identification Convincing?
- Strength: The two-design structure is powerful. California uses geographic policy exposure, while Waxman-Markey uses a threshold rule for free permits. Similar results across both settings make the mechanism more credible.
- Weakness: California emissions exposure may correlate with unobserved California-specific shocks, and the Waxman-Markey threshold may correlate with energy intensity and energy-price exposure.
- Referee concern: The treatment is partly anticipated because legislation moves through a public process. Estimates may therefore be lower bounds. Also, loan terms are equilibrium outcomes of bank-firm renegotiation, so the results do not isolate pure loan supply from borrower demand.

## 8. Main Regression or Model

California design:

```text
LoanTerm_iq =
  lambda CA_Emissions_Share_iq x Post_CA_q
+ beta CA_Emissions_Share_iq
+ Controls_iq
+ Firm FE_i
+ Industry x Quarter FE
+ epsilon_iq
```

The coefficient `lambda` compares the change in loan terms for firms with more California emissions after passage of California’s cap-and-trade bill relative to firms with less California emissions.

Waxman-Markey design:

```text
LoanTerm_it =
  lambda NoFreePermit_i x 1[t = 2009]
+ Controls_it
+ Firm FE_i
+ Year FE_t
+ Lead Bank FE_b
+ epsilon_it
```

Here, `NoFreePermit_i` equals one for manufacturing firms below the 5% energy-intensity threshold that would not receive free permits. The coefficient `lambda` measures whether firms without free permits receive tighter loan terms after Waxman-Markey passed the House.

Heterogeneity version:

```text
LoanTerm_it =
  beta1 Treatment_i x Post_t
+ beta2 Treatment_i x Post_t x Private_i
+ Controls_it
+ Firm FE_i
+ Time FE_t
+ epsilon_it
```

`beta1` captures the treatment effect for the baseline group, usually public firms. `beta2` captures the incremental effect for private firms. The main economic interpretation is that transition-risk tightening is concentrated in private firms.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Climate Finance]] by showing how carbon-pricing transition risk affects corporate credit.
2. [[Bank Lending]] by documenting that banks manage climate risk through maturity, loan type, rates, covenants, and loan sales.
3. [[Debt Contracting]] by showing that nonprice terms are central to how lenders respond to regulatory risk.
4. [[Private Firms]] by showing that private firms bear much larger financing effects than public firms.

It differs from prior work because it studies legally binding or near-binding cap-and-trade policies, uses confidential bank regulatory data, includes both private and public firms, and measures contract structure rather than only prices or public-market valuations.

## 10. Closely Related Papers
- [[Meng 2017]]: Studies Waxman-Markey using public-firm equity valuations; this paper uses the same policy setting but studies bank loan contracts.
- [[Bartram, Hou, and Kim 2022]]: Studies California cap-and-trade and public firms; this paper shows private-firm debt effects are much larger.
- [[Delis et al. Forthcoming]]: Shows fossil-fuel firms face higher loan rates after the Paris Agreement when exposed to climate-policy risk.
- [[Seltzer, Starks, and Zhu 2022]]: Studies environmental profiles, regulation, bond yields, and credit ratings.
- [[Kacperczyk and Peydro 2022]]: Studies bank lending to polluting firms following bank decarbonization commitments.
- [[Diamond 1991]] and [[Rajan and Winton 1995]]: Theoretical foundation for maturity shortening and lender monitoring.
- [[Sufi 2009]]: Credit lines are conditional and fragile forms of liquidity insurance.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the literature on climate transition risk and corporate finance. How do financial intermediaries price and manage regulatory risk?

How to use this paper:
- Main finding: Banks react to carbon-pricing transition risk by shortening maturity, reducing term loans, increasing rates, and shifting exposure to shadow banks.
- Data: EPA emissions plus confidential Federal Reserve Y14 and SNC loan data.
- Identification: California geographic emissions exposure and Waxman-Markey 5% energy-intensity free-permit threshold.
- Limitation: Policy exposure may be anticipated, and loan terms are bank-firm equilibrium outcomes.
- Connection to other papers: Pair with [[Meng 2017]] for public equity valuation effects, [[Bartram, Hou, and Kim 2022]] for relocation/public-firm effects, and [[Delis et al. Forthcoming]] for climate-policy loan pricing.
- Best exam phrase: "Ivanov, Kruttli, and Watugala show that transition risk is managed through debt contract structure, not just loan spreads."

## 12. Hypotheses Inspired by This Paper
H1: Firms with greater exposure to carbon-pricing regulation receive shorter loan maturities and a larger share of credit-line financing relative to term-loan financing.

H2: The effect of transition-risk regulation on bank credit is stronger for private firms than public firms because private firms are more financially constrained and less emissions-efficient.

H3: Banks with greater ex ante exposure to high-emitting borrowers reduce exposure more aggressively and transfer more risk to shadow banks.

## 13. Possible Extension or Research Design
- Research question: Does climate transition risk propagate through supply chains and affect financing terms of firms connected to high-emitting suppliers or customers?
- Hypothesis: Firms that depend on high-emitting suppliers face tighter credit after carbon-pricing shocks, even if they do not directly emit much.
- Data: EPA facility emissions, FactSet Revere customer-supplier links, syndicated loan data or Dealscan, Compustat, and possibly private-firm data from Orbis or Y14 if available.
- Identification: Difference-in-differences around carbon-pricing policy shocks using supplier exposure to regulated emissions as treatment intensity. Include firm fixed effects, industry-time fixed effects, and customer/supplier-region controls.
- Expected result: Direct emitters face the largest loan tightening, but downstream exposed firms also face shorter maturities or higher spreads if banks price supply-chain transition risk.
- Contribution: Extends [[Climate Finance]] from direct polluters to [[Supply Chain Finance]] and shows whether transition risk is transmitted through real economic networks.

## 14. Critiques

### Major Concern 1
California emissions share may capture California-specific economic shocks, local industry trends, or firm operating geography rather than pure climate-policy exposure. The nonpolluting California placebo helps, but a referee may still ask whether affected firms differ on unobservable investment opportunities or regional demand.

### Major Concern 2
The Waxman-Markey design relies on a threshold based on energy intensity. Firms just below and above the threshold may still differ in ways related to energy prices, input costs, technology, or industry cyclicality. Narrow bandwidths and industry controls help, but the threshold is not a random lottery.

### Minor Concern
The paper studies bank loan contracting, but the contract terms are equilibrium outcomes. It is difficult to know whether banks imposed tighter terms, borrowers demanded different contract structures, or both.

### Referee Recommendation
Accept, because the paper uses two independent policy settings, rare regulatory loan data, a clear mechanism, and evidence that effects concentrate exactly where theory predicts: private, emissions-inefficient, financially constrained firms.

## 15. Memory Hooks
- "Carbon makes loans shorter."
- "Banks manage EAD, not just spreads."
- "Private emitters get hit, public emitters mostly do not."
- "California geography plus Waxman 5% threshold."
- "Transition risk moves from banks toward shadow banks."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Climate Finance]], [[Bank Lending]], [[Debt Contracting]], [[Transition Risk]], [[Private Firms]], or [[Difference-in-Differences]]. The clean exam answer is: "Ivanov, Kruttli, and Watugala use California cap-and-trade exposure and the Waxman-Markey free-permit threshold to show that banks respond to transition risk by shortening maturities, reducing term-loan financing, increasing rates, and shifting exposure to shadow banks." Use it to argue that climate policy affects corporate finance through bank balance-sheet risk management and loan contract flexibility, not only through equity prices or bond spreads. In a critique answer, emphasize anticipation, regional confounds, and equilibrium renegotiation, but note that the paper is stronger than a standard correlation because it uses two quasi-experimental policy settings with different treatment assignment and similar results.