---
type: paper
status: unread
title: 'Information Sharing, Holdup, and External Finance: Evidence from Private Firms'
authors: Andrew Bird, Stephen A. Karolyi, Thomas G. Ruchti
year: 2019
journal: Review of Financial Studies
professor: DrJandik
seminar: null
jandik_paper_number: 15
jandik_week: 4
jandik_topic: 'Debt contracts: covenants, social capital, lender hold-up, and creditor control'
jandik_done: true
field: Corporate Finance
literature:
- Relationship Lending
- Private Debt
- Voluntary Disclosure
- Financial Constraints
methods:
- Fixed effects regressions
- instrumental variables
- IPO timing variation
datasets:
- '[[DealScan]]'
- Kenney-Patton IPO database
identification: Borrower, lender, and year fixed effects plus IPO-timing IV based on Altonji and Shakotko style quality-adjusted disclosure trends
main_result: Private borrowers that voluntarily disclose financial information reduce lender holdup, switch lenders more often, borrow from broader syndicates, pay lower spreads, and receive larger loan amounts.
exam_relevance: high
must_memorize: true
tags:
- relationship-lending
- lender-holdup
- voluntary-disclosure
- private-debt
- financial-constraints
- syndicated-loans
- information-asymmetry
created: 2026-06-04
updated: 2026-06-04
---

# Bird, Karolyi, and Ruchti 2019

## 1. One-Sentence Takeaway
This paper shows that voluntary disclosure by private borrowers reduces relationship-lender holdup using LPC Dealscan loan disclosures, and the main contribution is showing that information sharing can increase lender competition and relax financing constraints for private firms.

## 2. Exam-Ready Abstract
Bird, Karolyi, and Ruchti study whether private borrowers can reduce incumbent lender holdup by publicly sharing financial information in loan documents. The setting is the syndicated loan market, where relationship lenders learn private information about borrowers, making outside lenders wary of competing because of adverse selection and winner's curse concerns. The authors use LPC Dealscan data on private borrower loan facilities from 1995 to 2012 and identify voluntary disclosures of financial metrics such as sales, leverage, Debt/EBITDA, Senior Debt/EBITDA, fixed charge coverage, and interest coverage. They show that disclosing borrowers are more likely to switch lenders, borrow from larger syndicates, have lower lead-bank retained shares, attract more institutional participants, pay lower spreads, and receive larger loan amounts. The main identification concern is that disclosure is voluntary, so disclosing firms may differ from nondisclosing firms in unobserved quality. The authors address this with borrower, lender, and year fixed effects, loan controls, proprietary cost tests, and an IPO-timing IV based on the idea that disclosure costs fall as mandatory IPO disclosure approaches. This paper connects to [[Relationship Lending]], [[Financial Constraints]], [[Voluntary Disclosure]], and [[Private Debt]].

## 3. Research Question
What is the paper trying to answer?

Do private borrowers voluntarily disclose financial information in loan documents to reduce relationship-lender holdup and improve access to external finance?

More specifically: what mechanism, heterogeneity, or causal channel does the paper test?

The paper tests whether disclosure reduces the information disadvantage of potential outside lenders, thereby increasing lender competition and improving borrower bargaining power. It also studies why only some firms disclose, focusing on the trade-off between financing benefits and proprietary disclosure costs.

## 4. Core Mechanism

```text
Private borrower has an informed relationship lender
-> outside lenders face information disadvantage and winner's curse risk
-> incumbent lender has bargaining power and can hold up the borrower
-> borrower voluntarily discloses financial information through loan documents
-> outside lenders become more informed and willing to compete
-> borrower can switch lenders or credibly threaten to switch
-> lender competition improves loan terms
-> spreads fall and loan amounts rise
```

## 5. Main Findings
1. Voluntary disclosure increases lender competition. Disclosing borrowers are about 16 percentage points more likely to switch lenders in the preferred specification.
2. Disclosure changes syndicate structure. Future loans have more lenders, lower retained shares by lead arrangers, and greater participation by nonbank institutions.
3. Disclosure improves financing outcomes. Disclosing borrowers receive roughly 4% lower spreads and 8% higher loan amounts.
4. Disclosure is less likely when proprietary or legal costs are high. Borrowers disclose less in R&D-intensive industries, concentrated markets, industries with persistent margins, and high litigation-risk industries.
5. In the IPO subsample, disclosure becomes more likely as the IPO approaches, consistent with disclosure costs falling when mandatory public disclosure becomes inevitable.
6. IPO-timing IV estimates are generally larger than OLS estimates, suggesting that lower-quality or more constrained firms may benefit more from disclosure.
7. Disclosure also improves IPO outcomes: the IV estimates suggest larger IPO proceeds and lower underpricing.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Loan facility or loan package for private borrowers |
| Sample period | 1995-2012 |
| Main dataset | LPC Dealscan |
| IPO dataset | Kenney-Patton IPO database |
| Main sample | 30,628 loan facilities issued by private borrowers |
| IPO subsample | 1,683 loan facilities for private borrowers that later complete an IPO |
| Key variables | Disclose indicator, lender switching, number of lenders, lead-bank retained share, number of nonbank institutions, loan spread, loan amount |
| Treatment or shock | Voluntary disclosure of at least one financial metric in loan documentation |
| Disclosure metrics | Sales, Debt/EBITDA, Senior Debt/EBITDA, Leverage, Senior Leverage, Fixed Charge Coverage, Interest Coverage |
| Outcome variables | New lender indicator, syndicate size, retained share, institutional participation, future spreads, future loan amounts, IPO amount, IPO underpricing |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between disclosure and better loan outcomes is not causal because disclosure is a borrower choice. Higher-quality borrowers may disclose to separate themselves from worse firms, and those same borrowers might receive better loan terms even without disclosure. Alternatively, lower-quality or more financially constrained borrowers may have more to gain from marginal lender attention, which could make them more likely to disclose. The direction of bias is theoretically ambiguous. Other concerns include omitted borrower quality, unobserved lender information, strategic lender behavior, and time-varying financing needs.

### Identification Approach
- Natural experiment: Not a clean natural experiment. The closest source of quasi-experimental variation is the IPO setting, where disclosure costs fall as mandatory IPO disclosure approaches.
- Instrument: IPO-timing IV based on the Altonji and Shakotko approach. The instrument uses the firm-specific fraction of time elapsed between first appearance in the loan sample and the IPO, creating a quality-adjusted disclosure trend.
- Difference in differences: Not the primary design.
- Event study: The paper uses time to IPO to show disclosure probability rises as the IPO approaches, but this is not a standard event-study design.
- Fixed effects: Borrower fixed effects, lender fixed effects, and year fixed effects in baseline loan outcome regressions.
- Matching: Not clear from provided text.
- Placebo tests: Not clear from provided text.
- Robustness: Loan controls, borrower and lender fixed effects, timing controls in the IPO subsample, IV estimates, controls for covenant use, and tests of disclosure-cost determinants.
- Alternative source of variation: Cross-sectional proprietary cost measures, including R&D intensity, HHI, number of competitors, margin persistence, profit margin, sales growth, growth dispersion, and litigation risk.

### Is the Identification Convincing?
- Strength: The mechanism is directly observable. Disclosure predicts lender switching, syndicate expansion, lower retained shares, and better loan terms, which all line up with the lender competition channel.
- Strength: Borrower fixed effects absorb time-invariant borrower quality, lender fixed effects address lender-level disclosure tendencies, and loan controls capture lender-private information embedded in loan terms.
- Strength: The IPO-timing IV is clever because disclosure costs plausibly fall as firms approach mandatory public disclosure.
- Weakness: Disclosure remains voluntary, and the IV exclusion restriction is debatable because approaching an IPO may affect lender competition and loan terms through channels other than disclosure.
- Weakness: The IPO subsample may not generalize to all private borrowers because eventual IPO firms are a selected group.
- Referee concern: The paper needs to convince readers that voluntary disclosure is borrower-driven rather than lender-driven or mechanically tied to contracting needs.

## 8. Main Regression or Model

```text
Y_is = theta Disclose_it + rho X_it + Borrower FE_i + Lender FE_j + Year FE_t + epsilon_it
```

Here, `Y_is` is a future loan outcome for borrower `i` on the next loan made after the disclosure decision. `Disclose_it` equals one if borrower `i` voluntarily discloses at least one financial measure in the current loan. `X_it` includes loan controls such as sole lender, spread, facility amount, maturity, and number of covenants. The main coefficient is `theta`, which measures whether disclosure predicts future lender competition or better loan terms after controlling for borrower, lender, and time effects.

Key outcomes include:

```text
NewLender_is
NumLenders_is
RetainedShare_is
NumInstitutions_is
lnSpread_is
lnLoanAmount_is
```

The disclosure-cost regression is:

```text
Disclose_it = beta CostBenefit_it + tau X_it + epsilon_it
```

This tests whether borrowers are less likely to disclose when proprietary or legal disclosure costs are higher.

The IPO-timing IV model is conceptually:

```text
TimeToIPO_it = delta0 + delta1 FractionElapsed_it + Controls_it + Year FE_t + e_it

Disclose_it = predicted TimeToIPO_it + Controls_it + Year FE_t + epsilon_it

Y_is = theta predicted Disclose_it + Controls_it + Year FE_t + xi_it
```

The key coefficient is again `theta`. It estimates the effect of disclosure on future loan or IPO outcomes using variation in disclosure induced by firm-specific progress toward IPO.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Relationship Lending]] by showing that private borrowers can actively reduce lender information monopolies.
2. [[Financial Constraints]] by showing that disclosure can increase credit supply and reduce borrowing costs.
3. [[Voluntary Disclosure]] by identifying a lender-competition channel distinct from the usual cost-of-capital or risk-reduction channel.
4. [[Private Debt]] by showing that information flows through syndicated loan databases can affect future bargaining outcomes.
5. [[IPO Literature]] by showing that pre-IPO private disclosure can improve IPO financing outcomes.

It differs from prior work because:
- It studies private firms rather than public firms.
- It focuses on voluntary disclosure in loan documents rather than mandatory disclosure.
- It directly observes the mechanism through lender switching and syndicate structure.
- It frames disclosure as a tool for reducing lender holdup, not just reducing investor uncertainty.

## 10. Closely Related Papers
- [[Schenone 2010]]: IPOs reduce lender information advantage, lowering borrowing costs after firms become public.
- [[Bharath, Dahiya, Saunders, and Srinivasan 2007]]: Relationship lending creates benefits but can also generate information rents.
- [[Petersen and Rajan 1994]]: Relationship lending and lender competition affect credit availability.
- [[Sharpe 1990]]: Inside banks gain informational advantages that can create lender lock-in.
- [[Rajan 1992]]: Relationship lending can create borrower holdup by informed lenders.
- [[Sufi 2007]]: Syndicate structure reflects information asymmetry between lead arrangers and participants.
- [[Ivashina and Sun 2011]]: Institutional investors use loan market information in trading.
- [[Healy and Palepu 2001]]: Review of voluntary disclosure and capital market consequences.
- [[Altonji and Shakotko 1987]]: Methodological source for quality-adjusted tenure or timing instrument.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on relationship lending and lender holdup. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Private borrowers can reduce lender holdup by voluntarily sharing financial information, which increases lender competition and improves loan terms.
- Data: LPC Dealscan private loan facilities, 1995-2012, plus IPO data from Kenney-Patton.
- Identification: Borrower, lender, and year fixed effects; loan controls; disclosure-cost tests; IPO-timing IV.
- Limitation: Disclosure is voluntary, so unobserved borrower quality remains a concern.
- Connection to other papers: Complements [[Schenone 2010]] by showing that firms can reduce information asymmetry before becoming public.
- Best exam phrase: "Bird, Karolyi, and Ruchti show that private borrowers can strategically disclose information to break an incumbent lender's information monopoly."

## 12. Hypotheses Inspired by This Paper
H1: Private firms with greater dependence on relationship lending are more likely to voluntarily disclose financial information when seeking new external finance.

H2: The benefit of voluntary disclosure is stronger when outside lender competition is high but outside lender information is poor.

H3: Firms facing higher proprietary disclosure costs are less likely to disclose, even when disclosure would improve financing terms.

## 13. Possible Extension or Research Design
- Research question: Does voluntary disclosure reduce supplier or customer financing constraints in supply chain relationships?
- Hypothesis: Private firms that disclose more financial information obtain better trade credit terms and more stable supplier relationships.
- Data: Private firm loan disclosures from Dealscan matched to FactSet Revere supply chain links and Compustat or Orbis financials.
- Identification: Use shocks to lender competition or credit registry coverage as external variation in the value of disclosure. Alternatively, use within-firm changes around mandatory reporting thresholds.
- Expected result: Disclosure improves financing terms most for firms with concentrated banking relationships and high dependence on external finance.
- Contribution: Extends the information-sharing and holdup mechanism from bank lending to broader supply chain finance.

## 14. Critiques

### Major Concern 1
Disclosure is endogenous. Firms choose whether to disclose, and this choice may reflect unobserved quality, hidden financing needs, bargaining sophistication, or unmeasured growth opportunities. Borrower fixed effects help, but they do not eliminate time-varying selection.

### Major Concern 2
The IPO-timing IV may violate the exclusion restriction. As firms approach IPO, many things change besides disclosure costs: firm quality becomes more visible, investment banks become involved, governance changes, investor attention rises, and future financing needs become more salient. These factors could affect loan terms directly.

### Minor Concern
The disclosure measure may miss private information sharing outside LPC. Some borrowers may privately disclose to selected lenders, which means nondisclosure in the data is not the same as no information sharing.

### Referee Recommendation
R&R, because the mechanism is compelling and the data are novel, but the causal interpretation depends heavily on showing that disclosure is borrower-driven and not simply a proxy for unobserved borrower quality or changing financing needs.

## 15. Memory Hooks
- "Disclosure breaks the bank's information monopoly."
- "Private firms can advertise to lenders without going public."
- "Six percent disclose, but they get more competition."
- "Holdup solution: share information, switch lenders, lower spreads."
- "IPO timing IV: disclosure costs fall as mandatory disclosure approaches."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Relationship Lending]], [[Lender Holdup]], [[Financial Constraints]], [[Voluntary Disclosure]], [[Private Debt]], or [[Syndicated Loans]]. The clean exam answer is: "Bird, Karolyi, and Ruchti use voluntary disclosure in private loan agreements as a mechanism for reducing incumbent lender holdup and show that disclosing borrowers switch lenders more often, attract broader syndicates, pay lower spreads, and receive larger loan amounts." Use it to argue that information asymmetry in lending markets is not only a friction imposed on firms, but also a strategic margin firms can manage through disclosure. In a critique answer, emphasize selection into disclosure and the IPO-IV exclusion restriction, but note that the paper is stronger than a standard correlation because it observes both the mechanism, lender competition, and the outcome, improved loan terms.
