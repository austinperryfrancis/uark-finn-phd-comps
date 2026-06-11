---
type: paper
status: unread
title: Tracing the International Transmission of a Crisis through Multinational Firms
authors: Marcus Biermann and Kilian Huber
year: 2024
journal: Journal of Finance
seminar:
field: Corporate Finance, International Finance, Macrofinance
literature: Internal Capital Markets, Multinational Firms, Financial Constraints, Shock Transmission
methods: Difference-in-differences, event study, panel regressions, heterogeneity tests
datasets: MiDi, Ustan, Creditreform relationship bank data, Orbis Historical Financials
identification: Commerzbank lending cut during the 2008/09 financial crisis as an exogenous credit supply shock to German multinational parents
main_result: German multinational parents transmit credit shocks abroad through internal capital markets. Foreign affiliates lend to affected parents, become financially constrained, and reduce real activity.
exam_relevance: high
must_memorize: true
tags:
  - internal-capital-markets
  - multinational-firms
  - financial-constraints
  - shock-transmission
  - relationship-banking
  - difference-in-differences
  - DrJandik
  - corporate-finance
created:
updated:
---

# Biermann and Huber 2024

## 1. One-Sentence Takeaway
This paper shows that multinational firms transmit financial shocks internationally through internal capital markets using Commerzbank's 2008/09 lending cut to German parent firms, and the main contribution is to provide causal micro evidence that internal capital flows can reduce real activity in foreign affiliates.

## 2. Exam-Ready Abstract
Biermann and Huber study whether multinational firms transmit parent-level financial shocks to foreign affiliates through internal capital markets. The setting is the 2008/09 financial crisis, when Commerzbank suffered large losses in trading and investment activities and cut lending to German corporate borrowers. The shock directly affected German parent firms with preexisting Commerzbank relationships but did not directly affect their foreign affiliates, since Commerzbank corporate lending was concentrated in Germany. Using MiDi data on German multinationals' foreign affiliates, Ustan parent balance sheets, and Creditreform relationship bank data, the authors compare affiliates whose parents had higher Commerzbank dependence to affiliates whose parents had lower or zero dependence. They find that affected affiliates increased internal lending to parents, became financially constrained, and experienced lower sales, employment, and short-term assets from 2008 to 2010 before recovering. The effects are strongest for affiliates with prior internal lending ties to the parent, weaker in countries with developed credit markets, and much weaker after a nonfinancial flood shock to parents. This paper connects to [[Internal Capital Markets]], [[Multinational Firms]], [[Financial Constraints]], [[Relationship Banking]], and [[International Shock Transmission]].

## 3. Research Question
What is the paper trying to answer?

Do multinational firms transmit financial shocks across countries through their internal capital markets?

More specifically: when a parent firm experiences an external credit supply shock, does it draw resources from foreign affiliates, and do those affiliates experience real declines in sales, employment, and working-capital-related assets?

The paper also tests several mechanisms and heterogeneity channels:
- Whether internal lending from affiliates to parents drives transmission.
- Whether weak or low-growth affiliates are hit more strongly.
- Whether home-country affiliates are protected relative to foreign affiliates.
- Whether developed local credit markets attenuate the real effects.
- Whether financial shocks transmit more strongly than nonfinancial shocks.

## 4. Core Mechanism
Use a chain that can be memorized for comps:

```text
Commerzbank lending cut to German parent firms
-> parent loses relationship-bank credit and cannot quickly replace it
-> parent draws liquidity from foreign affiliates through internal loans
-> foreign affiliates become financially constrained
-> affiliates cut working capital, inputs, employment, and sales
-> financial shock is transmitted internationally through the multinational network
```

## 5. Main Findings
1. Parent firms with higher Commerzbank dependence experienced a negative credit supply shock, including lower bank debt and lower sales from 2008 to 2010.
2. Foreign affiliates of affected parents experienced lower sales, employment, and short-term production-related assets, even though they were not directly exposed to Commerzbank.
3. The sales decline is concentrated among affiliates that had previously lent to the parent and then increased internal lending after the shock.
4. Internal trade also contributed to lower affiliate sales, but it does not fully explain the effect. Internal capital markets remain central.
5. Managers appear "Darwinist" abroad, because weak international affiliates are hit more strongly, but "Socialist" at home, because domestic German affiliates are relatively protected.
6. Developed local credit markets attenuate the real effects, while currency differences, geographic distance, capital controls, and local business cycles matter less.
7. A nonfinancial flood shock to parents has much weaker effects on foreign affiliates because affected parents can still access external credit.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Affiliate-year, mainly foreign affiliates of German multinational parents |
| Sample period | 2002 to 2015 |
| Main dataset | Deutsche Bundesbank MiDi for foreign affiliates and internal capital market positions |
| Parent data | Ustan balance sheets, supplemented with Orbis Historical Financials |
| Relationship bank data | Creditreform data on German firms' relationship banks in 2006 |
| Key variables | Parent Commerzbank dependence, affiliate sales, employment, short-term assets, internal loans, short-term claims, bank debt, equity |
| Treatment or shock | Parent Commerzbank dependence in 2006 interacted with the post-lending-cut period |
| Outcome variables | Affiliate sales, employment, assets, short-term assets, internal lending to parent, external financing, affiliate exit, parent outcomes |
| Main sample size | 655 German parents and 2,695 international affiliates in the core MiDi sample |
| Treatment definition | Fraction of a parent's relationship banks that were Commerzbank branches in 2006 |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between parent distress and affiliate decline would not be causal because parent firms and affiliates are exposed to common shocks. They may produce similar products, use similar inputs, face common demand shocks, share productivity trends, or belong to industries hit by the same macro shock. Parent-affiliate comovement could therefore reflect omitted product-market shocks rather than internal capital market transmission. There is also selection: parents with Commerzbank relationships may differ systematically from parents using other banks. Finally, internal lending could be endogenous if affiliates lend to parents because both are responding to the same underlying shock.

### Identification Approach
- Natural experiment: Commerzbank's lending cut after losses in trading and investment divisions during the 2008/09 crisis.
- Instrument: No formal IV. Parent Commerzbank dependence is used as reduced-form exposure to the credit supply shock.
- Difference in differences: Compare affiliates of parents with high Commerzbank dependence to affiliates of parents with low or zero dependence before and after the lending cut.
- Event study: Estimate year-by-year effects of parent Commerzbank dependence relative to 2006.
- Fixed effects: Affiliate fixed effects, year fixed effects, country-by-time controls, industry-by-time controls, size-bin-by-time controls, leverage-bin-by-time controls.
- Matching: Not the central design. Identification relies more on differential exposure and fixed effects.
- Placebo tests: No pretrends before 2008. Low Commerzbank dependence has little effect because parents can use other relationship banks. Nonfinancial flood shock has weak affiliate effects.
- Robustness: Controls for affiliate and parent characteristics, country-industry-time fixed effects, alternative samples, and tests showing affiliates did not borrow directly from Commerzbank.
- Alternative source of variation: 2013 flood shock to parents, used to compare financial versus nonfinancial shocks.

### Is the Identification Convincing?
- Strength: Strong. The shock is plausibly exogenous to German corporate borrowers because Commerzbank's losses came from trading and investment exposures, not its corporate loan portfolio.
- Strength: The affiliate credit supply was not directly shocked because the treated affiliates are outside Germany and Commerzbank corporate lending was concentrated in Germany.
- Strength: The paper has direct data on internal capital market positions, which is rare and helps identify the mechanism.
- Weakness: Treatment is measured using relationship bank shares, not actual loan quantities, loan rates, or loan maturities.
- Weakness: Internal trade and parent-affiliate product-market linkages are hard to fully separate from financial transmission.
- Referee concern: The identifying variation is at the parent-bank relationship level during the global financial crisis, so one must believe that treated and control affiliates would have followed parallel trends absent the Commerzbank lending cut.

## 8. Main Regression or Model

```text
log(y_act) =
  sum_tau beta_tau Parent_CB_Dep_p x 1(t = tau)
+ Affiliate FE
+ Year FE
+ Controls_2006 x Year FE
+ epsilon_act
```

The outcome is an affiliate-level real or financial variable for affiliate `a` in country `c` and year `t`. `Parent_CB_Dep_p` is the 2006 fraction of the parent firm's relationship banks that were Commerzbank branches. The event-time coefficients `beta_tau` trace whether affiliates of more exposed parents grew differently before and after Commerzbank's lending cut. The key identification check is that the pre-2008 coefficients are close to zero.

A simpler post-period version is:

```text
Outcome_act =
  beta1 Parent_CB_Dep_p x 2008_to_2010
+ beta2 Parent_CB_Dep_p x 2011_to_2015
+ Affiliate FE
+ Year FE
+ Controls_2006 x Period FE
+ epsilon_act
```

`beta1` measures the short-run effect of parent exposure to the Commerzbank lending cut. This is the main coefficient for real effects because the credit shock binds most strongly from 2008 to 2010. `beta2` measures whether effects persist or recover after 2011.

For internal capital market heterogeneity:

```text
Outcome_act =
  beta1 Parent_CB_Dep_p x 2008_to_2010
+ beta2 Parent_CB_Dep_p x 2008_to_2010 x Previous_Internal_Loan_a
+ beta3 Parent_CB_Dep_p x 2011_to_2015
+ beta4 Parent_CB_Dep_p x 2011_to_2015 x Previous_Internal_Loan_a
+ Affiliate FE
+ Year FE
+ Controls_2006 x Period FE
+ epsilon_act
```

`beta2` is the key mechanism coefficient. It asks whether affiliates with preexisting internal lending infrastructure respond more strongly to the parent's credit shock. A positive coefficient for internal loans and a negative coefficient for sales imply that affiliates used as internal lenders are the ones that transmit the shock into real activity.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Internal Capital Markets]] by showing that internal capital flows can transmit negative financial shocks, not just reallocate capital efficiently.
2. [[Multinational Firms]] by showing that multinational networks transmit financial shocks across borders through parent-affiliate links.
3. [[Financial Constraints]] by showing that parent-level credit constraints can bind at the affiliate level through internal financing demands.
4. [[International Shock Transmission]] by documenting a micro-level channel through which one bank's lending cut affects real activity in other countries.
5. [[Relationship Banking]] by using bank relationship dependence to identify exposure to a credit supply shock.

It differs from prior work because:
- It uses direct microdata on internal capital positions between parents and foreign affiliates.
- It isolates a financial shock to the parent rather than relying on correlations in multinational outcomes.
- It separates financial transmission from nonfinancial shock transmission using the 2013 flood comparison.
- It distinguishes foreign affiliate treatment from domestic affiliate treatment, showing Darwinism abroad and Socialism at home.

## 10. Closely Related Papers
- [[Lamont 1997]]: Uses oil price shocks to study internal capital markets inside diversified firms.
- [[Shin and Stulz 1998]]: Studies whether internal capital markets allocate resources efficiently across segments.
- [[Rajan Servaes and Zingales 2000]]: Provides theory on internal capital markets, diversity, power struggles, and inefficient allocation.
- [[Scharfstein and Stein 2000]]: Models internal capital markets with rent-seeking and socialism across divisions.
- [[Matvos and Seru 2014]]: Shows evidence of "Socialism" in conglomerate capital allocation.
- [[Giroud and Mueller 2015]]: Related to internal networks and propagation of local shocks through firms.
- [[Huber 2018]]: Closely related identification setting using Commerzbank's lending cut as a credit supply shock.
- [[Desai Foley and Forbes 2008]]: Related to multinational affiliates and internal capital markets during crises.
- [[Boehm Flaaen and Pandalai-Nayar 2019]]: Related to multinational production networks and international shock transmission.
- [[Bena Dinc and Erel 2022]]: Related to multinational firms transmitting shocks across countries.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on internal capital markets. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Multinationals transmit parent credit shocks to foreign affiliates through internal capital markets.
- Data: MiDi affiliate-level data with direct parent-affiliate internal capital positions, combined with Ustan parent balance sheets and Creditreform relationship bank data.
- Identification: Commerzbank's 2008/09 lending cut creates differential exposure based on parent dependence on Commerzbank relationship banks.
- Limitation: Treatment is reduced-form exposure to bank relationships, not actual loan-level exposure. Internal trade and financial transmission are related and difficult to fully separate.
- Connection to other papers: Complements [[Lamont 1997]], [[Shin and Stulz 1998]], and [[Matvos and Seru 2014]] by moving from domestic conglomerates to multinational firms and from allocation efficiency to international crisis transmission.
- Best exam phrase: "Biermann and Huber show that internal capital markets can be a transmission mechanism for financial shocks, not merely a buffer against external capital market frictions."

## 12. Hypotheses Inspired by This Paper
H1: Foreign affiliates with preexisting internal lending relationships to the parent experience larger sales and employment declines after a parent credit supply shock.

H2: The real effects of parent financial shocks on affiliates are weaker in countries with deeper external credit markets.

H3: Parent firms protect domestic affiliates more than foreign affiliates during financial distress, consistent with home bias and domestic rent-seeking.

H4: Financial shocks transmit more strongly through internal capital markets than nonfinancial shocks because external credit access determines whether the parent must draw liquidity from affiliates.

## 13. Possible Extension or Research Design
- Research question: Do multinational firms transmit geopolitical or sanctions shocks across countries through internal capital markets and supply-chain links?
- Hypothesis: EU firms with parent or affiliate exposure to Russian suppliers after the 2022 invasion reallocate liquidity internally, causing exposed affiliates to reduce investment, employment, or working capital.
- Data: Orbis ownership data, FactSet Revere supply-chain links, Compustat Global, Bureau van Dijk financials, sanctions exposure measures, and country-level credit market depth.
- Identification: Difference-in-differences comparing affiliates of firms with high Russia exposure to affiliates of similar firms with low exposure before and after February 2022, with firm, country-industry-time, and parent fixed effects.
- Expected result: Affiliates connected to exposed parents experience real declines, especially where local credit markets are weak or where affiliates previously provided financing to the parent.
- Contribution: Extends Biermann and Huber from a bank credit shock to a geopolitical shock and links internal capital markets to sanctions, supply-chain fragility, and international corporate networks.

## 14. Critiques

### Major Concern 1
The Commerzbank shock occurs during the global financial crisis, so treated affiliates might have been exposed to other unobserved shocks correlated with parent Commerzbank dependence. The paper addresses this with pretrend tests, affiliate fixed effects, year fixed effects, country-time and industry-time controls, and tests showing affiliates were not directly affected by Commerzbank. Still, the crisis setting makes residual correlated shocks a natural concern.

### Major Concern 2
The treatment variable measures the fraction of relationship banks that were Commerzbank branches, not actual loan exposure. This is reasonable in the German relationship-banking context, but it means the coefficient is best interpreted as reduced-form exposure to a lending cut, not as the elasticity of affiliate outcomes with respect to loan supply.

### Minor Concern
The paper has unusually rich data, but the setting is German multinationals with reporting thresholds in MiDi. External validity may differ for smaller affiliates, non-German multinationals, bank-based versus market-based financial systems, or periods outside financial crises.

### Referee Recommendation
Accept, because the paper combines rare internal capital market data with a credible quasi-experiment and directly addresses a major identification problem in the multinational shock transmission literature. The main caveat is that relationship-bank exposure and internal trade channels make interpretation partly reduced-form, but the mechanism evidence is strong enough for publication.

## 15. Memory Hooks
- "Commerzbank shock travels abroad through the parent."
- "Foreign affiliates become the parent's emergency bank."
- "Darwinist abroad, Socialist at home."
- "Financial shock transmits, flood shock does not."
- "Internal capital markets can amplify crises, not just insure affiliates."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Internal Capital Markets]], [[Multinational Firms]], [[Financial Constraints]], [[Relationship Banking]], [[International Shock Transmission]], [[Difference-in-Differences]], or [[Event Studies]]. The clean exam answer is: "Biermann and Huber 2024 use Commerzbank's 2008/09 lending cut as an exogenous credit supply shock to German multinational parents and show that foreign affiliates lend internally to affected parents, become financially constrained, and reduce real activity." Use it to argue that internal capital markets can transmit financial shocks across countries rather than merely smooth local shocks. In a critique answer, emphasize that parent-affiliate comovement is usually hard to interpret causally because of common shocks, but note that the paper is stronger than a standard correlation because the shock directly affects parent credit supply, not foreign affiliate credit supply, and because the authors observe internal capital flows directly.