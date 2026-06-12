---
type: paper
status: unread
title: 'Paying by Donating: Corporate Donations Affiliated with Independent Directors'
authors: Ye Cai, Jin Xu, Jun Yang
year: 2021
journal: Review of Financial Studies
professor: DrJandik
seminar: null
jandik_paper_number: 55
jandik_week: 14
jandik_topic: Governance
jandik_done: false
field: Corporate Finance
literature:
- '[[Corporate Governance]]'
- Boards
- Executive Compensation
- CSR and Agency
methods:
- Panel regressions
- fixed effects
- propensity score matching
- instrumental variables
- event-style tests
datasets:
- '[[BoardEx]]'
- Foundation Directory Online
- IRS Forms 990-PF/990
- '[[ExecuComp]]'
- '[[Compustat]]'
- '[[CRSP]]'
- '[[RiskMetrics]]'
- Thomson Reuters
identification: Within-firm changes, compensation committee heterogeneity, director appointment/departure tests, and forced college coach turnover IV
main_result: Affiliated charitable donations are associated with higher CEO pay, weaker CEO turnover-performance sensitivity, and worse firm performance.
exam_relevance: high
must_memorize: true
tags:
- corporate-governance
- boards
- executive-compensation
- csr
- agency
- instrumental-variables
created: 2026-06-12
updated: 2026-06-12
---

# Cai, Xu, and Yang 2021

## 1. One-Sentence Takeaway
This paper shows that CEOs can weaken independent director monitoring by channeling corporate charitable donations to directors' affiliated charities using S&P 500 donation-board data, and the main contribution is to identify a hidden nonfinancial tie that compromises board independence.

## 2. Exam-Ready Abstract
Cai, Xu, and Yang study whether nominally independent directors are less independent when firms donate to charities with which those directors are affiliated. The setting is S&P 500 firms from 2003 to 2012, matched between BoardEx director-charity affiliations and Foundation Directory Online corporate donation data. The key treatment is an affiliated donation, meaning a corporate charitable contribution to a tax-exempt organization connected to an independent director. Firms making affiliated donations pay CEOs about 9.4% more on average, with stronger effects when the donation is tied to the compensation committee chair or a large fraction of the compensation committee. The authors address endogeneity using within-firm changes around donation initiation and termination, firm and CEO fixed effects, propensity score matching, director appointment and departure tests, and an IV based on forced college football or basketball coach turnovers at director-affiliated universities. The paper contributes to [[Corporate Governance]], [[Boards of Directors]], [[Executive Compensation]], and [[CSR and Agency Problems]] by showing that corporate philanthropy can operate as a hidden side payment that weakens monitoring.

## 3. Research Question
Does corporate charitable giving to independent directors' affiliated charities compromise board independence and weaken monitoring of the CEO?

More specifically: the paper tests whether affiliated donations create a material relationship between CEOs and independent directors, reducing directors' incentives to bargain hard over CEO pay or fire poorly performing CEOs.

## 4. Core Mechanism

```text
Corporate donation to independent director-affiliated charity
-> director benefits through fundraising success, prestige, or nonprofit obligations
-> director becomes less willing to challenge CEO
-> compensation committee or board monitors less aggressively
-> CEO receives higher pay and faces weaker performance-based dismissal
```

## 5. Main Findings
1. Firms with affiliated donations pay CEOs about 9.4% more than firms without affiliated donations, after controlling for standard determinants of CEO compensation.
2. The CEO pay effect is concentrated when the affiliated donation involves compensation committee members, especially the compensation committee chair or a large fraction of the committee.
3. Affiliated donations are associated with weaker monitoring: forced CEO turnover becomes less sensitive to poor stock performance when donations are large or involve a large fraction of independent directors.
4. Affiliated donations tend to begin after an independent director joins the board and end after an exogenous director departure, suggesting donations target directors rather than charitable causes.
5. Firms with weaker governance and weaker shareholder monitoring are more likely to make affiliated donations and make larger affiliated donations.

## 6. Data

| Item | Details |
|---|---|
| Unit of observation | Mainly firm-year; also director-year and firm-director-year-charity in some tests |
| Sample period | 2003 to 2012 |
| Main dataset | S&P 500 firms matched across BoardEx, Foundation Directory Online, ExecuComp, Compustat, CRSP, RiskMetrics, and Thomson Reuters |
| Key variables | Affiliated donation dummy and amount; CEO total pay; compensation committee affiliation; forced CEO turnover; stock returns; governance controls |
| Treatment or shock | Corporate donations to charities affiliated with independent directors; IV uses forced college football and basketball coach turnovers at director-affiliated universities |
| Outcome variables | CEO compensation, forced CEO turnover-performance sensitivity, firm performance, donation initiation and termination |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between affiliated donations and CEO pay is not causal because weakly governed firms may both overpay CEOs and engage in opportunistic philanthropy. Omitted variables such as CEO power, free cash flow, firm size, CSR culture, director social networks, and board quality could jointly determine donations and compensation. There is also selection: CEOs who already have influence over the board may be more likely to direct donations to director-affiliated charities. Reverse causality is possible if highly paid CEOs have more discretion over charitable budgets or use donations to maintain board support. Measurement error is also relevant because many charitable links are not formally disclosed in SEC filings.

### Identification Approach
- Natural experiment: Forced college coach turnover creates fundraising pressure at director-affiliated universities.
- Instrument: Indicator for forced basketball or football head coach turnover at universities affiliated with multiple independent directors.
- Difference in differences: Not a clean canonical DiD, but the paper uses changes around initiation and termination of affiliated donations.
- Event study: Tests whether donations start after independent director appointment and end after exogenous departure.
- Fixed effects: Industry and year fixed effects in baseline; firm fixed effects, firm-by-CEO fixed effects, and director fixed effects in robustness.
- Matching: Propensity score matching compares affiliated-donation firms to similar non-donating firms.
- Placebo tests: Unforced coach turnovers do not significantly predict affiliated donations.
- Robustness: Controls for unaffiliated donations, CEO-affiliated donations, inside director-affiliated donations, CEO-director charity ties, free cash flow, governance variables, and firm characteristics.
- Alternative source of variation: Compensation committee heterogeneity, especially whether donations involve the committee chair or a large fraction of committee members.

### Is the Identification Convincing?
- Strength: The strongest evidence is the convergence of multiple designs: committee-specific effects, donation initiation and termination, director appointment and departure timing, and the coach-turnover IV.
- Weakness: The IV identifies a local average treatment effect for firms donating to universities after coach turnovers, not necessarily the average effect for all affiliated donations.
- Referee concern: The exclusion restriction for coach turnovers may be questioned if universities with major sports programs are connected to local economic conditions, alumni networks, or firm-level CEO networks that independently affect CEO pay.

## 8. Main Regression or Model

```text
Ln(CEO Pay_it) =
  beta AffiliatedDonation_it
+ Controls_it
+ Industry FE
+ Year FE
+ epsilon_it
```

The baseline regression asks whether CEO pay is higher in firm-years with affiliated donations, controlling for CEO characteristics, governance, firm financials, industry effects, and year effects. The coefficient beta is the paper's main pay result: a positive beta means CEOs are paid more when the firm donates to independent director-affiliated charities.

Key heterogeneity specification:

```text
Ln(CEO Pay_it) =
  beta1 DonationToCompCommittee_it
+ beta2 DonationNotToCompCommittee_it
+ Controls_it
+ Industry FE
+ Year FE
+ epsilon_it
```

Here beta1 captures the effect of donations involving compensation committee members, while beta2 captures donations involving other independent directors. The main economic interpretation comes from beta1 because the compensation committee directly influences CEO pay.

Turnover sensitivity specification:

```text
ForcedTurnover_it =
  beta1 StockReturn_it
+ beta2 IntensiveAffiliatedDonation_it
+ beta3 StockReturn_it x IntensiveAffiliatedDonation_it
+ Controls_it
+ Industry FE
+ Year FE
+ epsilon_it
```

The key coefficient is beta3. A positive beta3 weakens the normal negative relation between stock returns and forced CEO turnover, meaning poorly performing CEOs are less likely to be removed when affiliated donations are intensive.

IV structure:

```text
First stage:
AffiliatedDonation_it =
  pi ForcedCoachTurnover_it
+ Controls_it
+ Industry FE
+ Year FE
+ u_it

Second stage:
Ln(CEO Pay_it) =
  beta PredictedAffiliatedDonation_it
+ Controls_it
+ Industry FE
+ Year FE
+ epsilon_it
```

The first stage uses forced college coach turnovers as a shock to fundraising demand at director-affiliated universities. The second stage asks whether the predicted component of affiliated donations increases CEO pay.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Corporate Governance]] by showing that formal independence rules miss economically meaningful hidden ties between CEOs and directors.
2. [[Executive Compensation]] by identifying a channel through which CEOs may obtain excess pay.
3. [[CSR and Agency Problems]] by showing that charitable giving can camouflage agency-motivated side payments.
4. [[Boards of Directors]] by linking director incentives to compensation and CEO turnover decisions.

It differs from prior work because it does not rely only on social ties, CEO-appointed directors, or broad CSR categories. It directly matches corporate donations to charities affiliated with independent directors and shows that these donation links move with director appointments and departures.

## 10. Closely Related Papers
- [[Core, Holthausen, and Larcker 1999]]: Weak governance and CEO compensation.
- [[Weisbach 1988]]: Board independence and CEO turnover.
- [[Hwang and Kim 2009]]: Social ties and board independence.
- [[Fracassi and Tate 2012]]: CEO-director networks and governance.
- [[Masulis and Reza 2015]]: Corporate charitable giving as an agency problem.
- [[Coles, Daniel, and Naveen 2014]]: CEO-appointed directors and monitoring.
- [[Flammer 2015]]: CSR and firm value, useful contrast because CSR can also be value-enhancing.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the literature on board independence and CEO compensation. Discuss how papers establish whether independent directors actually monitor managers.

How to use this paper:
- Main finding: Affiliated donations compromise independent director monitoring and are associated with higher CEO pay.
- Data: S&P 500 firms from 2003 to 2012, matching BoardEx director-charity affiliations to corporate charitable donations.
- Identification: Compensation committee heterogeneity, initiation and termination tests, firm and CEO fixed effects, PSM, director appointment and departure timing, and a coach-turnover IV.
- Limitation: The key treatment is not randomly assigned, and the IV is best interpreted as a local effect for donations to universities affected by coach turnover shocks.
- Connection to other papers: Use with [[Core, Holthausen, and Larcker 1999]] on weak governance and CEO pay, [[Weisbach 1988]] on CEO turnover, and [[Masulis and Reza 2015]] on charitable giving as agency.
- Best exam phrase: "Cai, Xu, and Yang show that director independence is not just a formal classification. CEOs can create hidden dependence by donating shareholder money to directors' charities."

## 12. Hypotheses Inspired by This Paper
H1: Firms that donate to charities affiliated with compensation committee members pay CEOs higher abnormal compensation than firms donating to unaffiliated charities.

H2: The sensitivity of forced CEO turnover to poor performance is lower when a firm makes large donations to charities affiliated with a large fraction of independent directors.

H3: Mandatory disclosure of director-affiliated donations reduces affiliated giving and increases the sensitivity of CEO pay to performance.

## 13. Possible Extension or Research Design
- Research question: Does mandatory disclosure of corporate charitable donations to director-affiliated nonprofits improve board monitoring?
- Hypothesis: Disclosure reduces affiliated donations and weakens the positive relation between affiliated donations and CEO pay.
- Data: Proxy statements, nonprofit Form 990 data, BoardEx charity affiliations, ExecuComp, CRSP, Compustat, and state-level nonprofit disclosure shocks if available.
- Identification: Difference-in-differences around regulatory or exchange-level disclosure changes, comparing firms more exposed to director-affiliated nonprofit ties to firms with fewer such ties.
- Expected result: Treated firms reduce affiliated donations, CEO pay becomes less excessive, and forced CEO turnover becomes more sensitive to performance.
- Contribution: Moves from detecting hidden side payments to testing whether transparency can improve board monitoring.

## 14. Critiques

### Major Concern 1
Affiliated donations are endogenous. Weak governance, CEO power, or free cash flow may cause both charitable donations and high CEO pay. The authors address this with extensive controls, fixed effects, PSM, initiation and termination tests, and an IV, but complete random assignment is not available.

### Major Concern 2
The IV exclusion restriction is debatable. Forced coach turnovers at universities may increase fundraising demand, but they could also be correlated with alumni networks, local elite connections, or firm-university relationships that affect CEO pay through channels other than affiliated donations.

### Minor Concern
The sample is limited to S&P 500 firms, so the findings may not generalize to smaller firms, private firms, or firms with less visible philanthropic programs.

### Referee Recommendation
Accept, because the paper identifies a novel and economically important governance channel, assembles difficult donation-director data, and triangulates the evidence with several complementary identification approaches. A referee should still ask for careful discussion of the IV exclusion restriction and external validity.

## 15. Memory Hooks
- "Paying by donating" means the CEO pays directors indirectly through their charities.
- 9.4% higher CEO pay is the headline number.
- Strongest mechanism: donations tied to the compensation committee, especially the chair.
- Director appointments start donation links; exogenous departures end them.
- Coach firing IV: universities need money after costly football or basketball coach turnovers.

## 16. Comps Use Rating

| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Corporate Governance]], [[Boards of Directors]], [[Executive Compensation]], [[CSR and Agency Problems]], [[Instrumental Variables]], or [[CEO Turnover]]. The clean exam answer is: "Cai, Xu, and Yang use corporate donations to independent director-affiliated charities as a hidden channel of director dependence and show that these donations are associated with higher CEO pay and weaker CEO turnover-performance sensitivity." Use it to argue that formal board independence can overstate true monitoring independence when directors have indirect private benefits. In a critique answer, emphasize omitted governance quality and the IV exclusion restriction, but note that the paper is stronger than a standard correlation because it uses compensation committee heterogeneity, within-firm donation changes, director appointment and departure timing, fixed effects, PSM, and a forced coach-turnover instrument.
