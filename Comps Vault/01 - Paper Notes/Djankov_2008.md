---
type: paper
status: unread
title: The Law and Economics of Self-Dealing
authors: Simeon Djankov, Rafael La Porta, Florencio Lopez-de-Silanes, Andrei Shleifer
year: 2008
journal: Journal of Financial Economics
seminar:
field: Corporate Finance
literature: Law and Finance; Corporate Governance; Investor Protection; Financial Development
methods: Cross-country legal index construction; OLS; IV using legal origin; robustness tests
datasets: Lex Mundi legal survey; World Development Indicators; Dyck and Zingales control premium data; IPO data; ownership concentration data
identification: Cross-country legal variation, with common law legal origin used as an instrument for anti-self-dealing protections
main_result: Stronger private enforcement protections against self-dealing predict larger and deeper stock markets, while public enforcement measures do not predict financial development as well.
exam_relevance: high
must_memorize: true
tags:
  - law-and-finance
  - corporate-governance
  - investor-protection
  - self-dealing
  - legal-origin
  - financial-development
  - DrJandik
created: 2026-06-03
updated: 2026-06-03
---

# Djankov et al. 2008

## 1. One-Sentence Takeaway
This paper shows that countries with stronger legal protection of minority shareholders against self-dealing have more developed stock markets using a new cross-country anti-self-dealing index, and the main contribution is a theoretically grounded measure of investor protection that improves on the older anti-director rights index.

## 2. Exam-Ready Abstract
Djankov et al. ask how legal systems regulate corporate self-dealing by controlling shareholders and whether those rules predict financial market development. They construct a new anti-self-dealing index for 72 countries using responses from Lex Mundi law firms about a standardized related-party transaction involving a controlling shareholder, Buyer, and Seller. The index measures private enforcement protections, including disclosure, approval by disinterested shareholders, litigation rights, rescission, liability, and access to evidence. The paper finds that common law countries generally provide stronger anti-self-dealing protections than civil law countries, especially French civil law countries. Stronger anti-self-dealing protections are associated with higher stock-market-capitalization-to-GDP, lower control premiums, more listed firms, more IPO activity, and in some specifications lower ownership concentration. Public enforcement through fines and prison terms is not strongly related to stock market development. This paper belongs in [[Law and Finance]], [[Corporate Governance]], [[Investor Protection]], and [[Financial Development]].

## 3. Research Question
What legal rules best protect minority shareholders from self-dealing by controlling shareholders, and do those rules help explain cross-country differences in stock market development?

More specifically: the paper tests whether private enforcement mechanisms such as disclosure, approval rules, and shareholder litigation are more strongly associated with financial development than public enforcement mechanisms such as fines and prison terms.

## 4. Core Mechanism

```text
Weak legal protection against self-dealing
-> controlling shareholders can divert firm value through related-party transactions
-> minority shareholders expect expropriation and demand discounts or avoid equity markets
-> firms face weaker outside equity financing and ownership remains concentrated
-> stock markets are smaller, less liquid, and less developed
```

Alternative positive version:

```text
Stronger anti-self-dealing law
-> more disclosure, disinterested approval, and litigation rights
-> lower expected private benefits of control
-> greater minority shareholder confidence
-> more outside equity participation and IPO activity
-> deeper stock markets and broader ownership
```

## 5. Main Findings
1. The anti-self-dealing index is much higher in common law countries than in civil law countries, especially French civil law countries.
2. Stronger anti-self-dealing protections predict more developed stock markets, including larger market capitalization, more listed firms, more IPOs, and lower control premiums.
3. Private enforcement matters more than public enforcement. Fines and prison terms are not robust predictors of stock market development.
4. The anti-self-dealing index is a more theoretically grounded and often more robust predictor than the older anti-director rights index.
5. Securities-law measures such as prospectus disclosure and prospectus liability are also powerful predictors, sometimes stronger than the anti-self-dealing index.

## 6. Data

| Item | Details |
|---|---|
| Unit of observation | Country |
| Sample period | Legal rules as of 2003; financial development outcomes mostly 1996 to 2003 depending on variable |
| Main dataset | Lex Mundi legal survey covering a hypothetical self-dealing transaction |
| Key variables | Anti-self-dealing index; ex ante private control; ex post private control; public enforcement index; legal origin |
| Treatment or shock | Cross-country variation in legal rules protecting minority shareholders from self-dealing |
| Outcome variables | Stock-market-capitalization-to-GDP; control premium; listed firms per population; IPOs-to-GDP; ownership concentration |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between investor protection and financial development may not be causal. Countries with more developed stock markets may demand stronger legal protections, creating reverse causality. Omitted institutional quality may drive both legal rules and financial development. Legal rules may also proxy for broader governance, tax enforcement, media scrutiny, political institutions, judicial quality, or economic development. Measurement error is also possible because the index captures law on the books rather than actual enforcement in practice.

### Identification Approach
- Natural experiment: Not clear from provided text.
- Instrument: Common law legal origin is used as an instrument for the anti-self-dealing index.
- Difference in differences: Not used.
- Event study: Not used.
- Fixed effects: Not applicable because the main design is cross-country.
- Matching: Not used.
- Placebo tests: Not clear from provided text.
- Robustness: Controls for income per capita and judicial efficiency; compares private enforcement with public enforcement; compares anti-self-dealing with anti-director rights, prospectus disclosure, prospectus liability, tax evasion, media, and political variables.
- Alternative source of variation: Legal origin and principal components of several shareholder protection indices.

### Is the Identification Convincing?
- Strength: The paper improves measurement by using a standardized hypothetical transaction, making legal rules comparable across countries. The common law instrument is historically predetermined relative to modern stock market outcomes.
- Weakness: Legal origin may violate the exclusion restriction because it affects many institutions beyond anti-self-dealing law, including courts, securities regulation, contract enforcement, and political institutions.
- Referee concern: The results are best interpreted as strong cross-country institutional evidence, not clean causal identification.

## 8. Main Regression or Model

```text
StockMarketDevelopment_c =
  beta AntiSelfDealing_c
+ gamma LnGDPperCapita_c
+ delta JudicialEfficiency_c
+ epsilon_c
```

The dependent variable is a country-level measure of stock market development, such as stock-market-capitalization-to-GDP, control premium, listed firms per population, IPOs-to-GDP, or ownership concentration. The key coefficient is beta. A positive beta for market capitalization, listed firms, and IPOs means stronger anti-self-dealing rules are associated with deeper equity markets. A negative beta for control premium or ownership concentration means stronger investor protection is associated with lower private benefits of control and more dispersed ownership.

IV version:

```text
First stage:
AntiSelfDealing_c =
  pi CommonLaw_c
+ gamma LnGDPperCapita_c
+ delta JudicialEfficiency_c
+ u_c

Second stage:
StockMarketDevelopment_c =
  beta PredictedAntiSelfDealing_c
+ gamma LnGDPperCapita_c
+ delta JudicialEfficiency_c
+ epsilon_c
```

The first stage uses common law legal origin to predict anti-self-dealing protections. The second stage estimates whether the legally predicted component of investor protection explains financial development. The main economic interpretation is beta in the second stage.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Law and Finance]] by creating a more theoretically grounded investor protection index than the original anti-director rights index.
2. [[Corporate Governance]] by focusing directly on self-dealing and tunneling by controlling shareholders.
3. [[Financial Development]] by showing that legal protection of minority shareholders predicts the size and activity of equity markets.

It differs from prior work because it does not rely only on broad corporate law variables. Instead, it asks lawyers in many countries how the law treats the same concrete related-party transaction.

## 10. Closely Related Papers
- [[La Porta et al. 1997]]: Introduces the law and finance view that legal rules and legal origin shape external finance.
- [[La Porta et al. 1998]]: Develops the anti-director rights index and shows legal origin predicts investor protection.
- [[Shleifer and Vishny 1997]]: Frames corporate governance as the problem of investors getting returns from managers or controlling shareholders.
- [[Dyck and Zingales 2004]]: Measures private benefits of control using control premiums.
- [[La Porta et al. 2006]]: Studies securities laws, disclosure, liability, and stock market development.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the law and finance literature on investor protection and financial development. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Stronger private enforcement against self-dealing predicts deeper stock markets.
- Data: Lex Mundi legal survey for 72 countries, combined with country-level stock market development outcomes.
- Identification: Cross-country regressions with legal origin as an instrument, but causal interpretation is limited by broad institutional confounding.
- Limitation: Law on the books may differ from enforcement in practice.
- Connection to other papers: Use after [[La Porta et al. 1997]] and [[La Porta et al. 1998]] as a measurement improvement.
- Best exam phrase: “Djankov et al. sharpen the law and finance mechanism by measuring the legal hurdles that a controlling shareholder must overcome to tunnel value through a related-party transaction.”

## 12. Hypotheses Inspired by This Paper
H1: Countries with stronger anti-self-dealing laws have lower private benefits of control, as reflected in lower control premiums.

H2: The effect of anti-self-dealing laws on IPO activity is stronger in countries with higher judicial quality.

H3: Private enforcement mechanisms predict equity market development more strongly than public enforcement mechanisms.

## 13. Possible Extension or Research Design
- Research question: Do reforms that strengthen related-party transaction rules increase minority shareholder participation and IPO activity?
- Hypothesis: Countries that adopt stricter disclosure and disinterested shareholder approval rules experience higher IPO activity and lower control premiums after reform.
- Data: Country-level legal reform dates; IPO data; ownership concentration; control premiums; firm-level valuation data.
- Identification: Difference in differences comparing reforming countries to non-reforming countries, with event-study tests for pre-trends.
- Expected result: Market development improves after reforms, especially where courts are effective and media scrutiny is high.
- Contribution: Moves the law and finance literature from cross-country correlations toward reform-based causal evidence.

## 14. Critiques

### Major Concern 1
The identification is not clean. Legal origin may affect stock market development through many channels other than anti-self-dealing law, so the IV strategy may not isolate the causal effect of shareholder protection.

### Major Concern 2
The index measures formal legal rules, not actual enforcement. A country may have strong laws on paper but weak courts, corruption, or low practical enforcement.

### Minor Concern
The hypothetical transaction is useful for comparability, but it may not capture all important forms of tunneling, such as pyramids, transfer pricing, freezeouts, insider loans, or political self-dealing.

### Referee Recommendation
Accept, because the paper makes a major measurement contribution and provides strong cross-country evidence linking legal protection from self-dealing to financial development, even though the causal design is not definitive.

## 15. Memory Hooks
- “James buys trucks”: remember the stylized Buyer and Seller transaction.
- Anti-self-dealing equals legal hurdles against tunneling.
- Private enforcement beats public enforcement.
- Common law protects minority shareholders more strongly.
- Better investor protection means deeper stock markets and lower control premiums.

## 16. Comps Use Rating

| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Law and Finance]], [[Corporate Governance]], [[Investor Protection]], or [[Financial Development]]. The clean exam answer is: "Djankov et al. 2008 use a standardized legal survey of self-dealing rules across 72 countries to construct an anti-self-dealing index and show that stronger private enforcement protections predict deeper stock markets." Use it to argue that legal protection matters because outside investors need assurance that controlling shareholders cannot easily tunnel value. In a critique answer, emphasize that the paper is cross-country and vulnerable to omitted institutional variables, but note that it is stronger than a standard correlation because the legal index is built from a concrete hypothetical transaction and the authors compare it to alternative legal, tax, media, and political explanations.