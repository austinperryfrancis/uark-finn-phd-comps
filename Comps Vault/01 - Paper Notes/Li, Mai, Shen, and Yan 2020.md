---
type: paper
status: unread
title: Measuring Corporate Culture Using Machine Learning
authors: Kai Li, Feng Mai, Rui Shen, Xinyan Yan
year: 2020
journal: Review of Financial Studies
professor: DrJandik
seminar: null
jandik_paper_number: 51
jandik_week: 13
jandik_topic: Innovation and machine learning
jandik_done: false
field: Corporate Finance
literature:
- Corporate Culture
- Textual Analysis
- '[[Machine Learning in Corporate Finance]]'
- '[[Mergers and Acquisitions]]'
methods:
- word2vec
- semisupervised machine learning
- textual analysis
- validation regressions
- OLS
- LPM
- conditional logit
datasets:
- Thomson Reuters StreetEvents
- '[[Compustat]]'
- '[[CRSP]]'
- '[[Patent Data]]'
- KLD
- Audit Analytics
- '[[SDC M&A]]'
identification: Measurement validation plus associational outcome tests; crisis and M&A settings provide suggestive but not clean causal evidence
main_result: Corporate culture can be measured from earnings-call QA text using word embeddings, and strong culture is associated with efficiency, risk-taking, lower earnings management, compensation design, firm value, crisis resilience, and M&A matching.
exam_relevance: high
must_memorize: true
tags:
- corporate-culture
- textual-analysis
- machine-learning
- word2vec
- earnings-calls
- mergers-and-acquisitions
created: 2026-06-12
updated: 2026-06-12
---

# Li, Mai, Shen, and Yan 2020

## 1. One-Sentence Takeaway
This paper shows that corporate culture can be measured from earnings-call QA transcripts using word2vec, and the main contribution is a scalable culture measure that links latent organizational values to firm policies, performance, and M&A behavior.

## 2. Exam-Ready Abstract
Li, Mai, Shen, and Yan ask whether corporate culture can be measured systematically in large samples and whether that measured culture relates to firm outcomes. They train a word embedding model on 209,480 earnings-call transcripts and construct dictionaries for five cultural values: innovation, integrity, quality, respect, and teamwork. Their measure is based on the QA section of calls because it is less scripted than management presentations and should be harder to manipulate through cheap talk. They validate the culture scores against external markers such as patents, R&D, restatements, backdating, KLD strengths and concerns, Fortune best-employer status, and joint ventures or strategic alliances. They then show that strong culture is associated with higher operational efficiency, more risk-taking, less earnings management, longer-term and risk-taking executive compensation incentives, higher Tobin's q, better returns in bad times, and culturally closer merger pairs. The paper is best viewed as a measurement and large-sample evidence paper, not a clean causal identification paper. It connects to [[Corporate Culture]], [[Textual Analysis]], [[Machine Learning in Finance]], and [[Mergers and Acquisitions]].

## 3. Research Question
Can researchers measure corporate culture in a scalable, time-varying way using corporate disclosures, and does that measure help explain firm behavior and outcomes?

More specifically, the paper tests whether managers' language in earnings-call QA sections reveals latent organizational values, and whether those values correlate with operational efficiency, risk-taking, earnings management, compensation design, valuation, bad-times performance, and M&A matching.

## 4. Core Mechanism
Use a chain that can be memorized for comps:

```text
Earnings-call QA language
-> word2vec learns context-specific meanings of words and phrases
-> culture dictionary scores innovation, integrity, quality, respect, and teamwork
-> strong culture proxies for shared values and coordination norms
-> employees and managers make more consistent long-term decisions
-> better efficiency, risk-taking, lower earnings management, higher valuation, and better crisis performance
```

For the M&A setting:

```text
Acquirer and target have similar or distant culture vectors
-> expected integration costs differ
-> culturally similar firms are easier to coordinate post-merger
-> culturally similar pairs are more likely to merge
-> post-merger acquirer culture partly reflects target premerger culture
```

## 5. Main Findings
1. A word2vec-based culture dictionary can score five values from earnings-call QA text: innovation, integrity, quality, respect, and teamwork.
2. The culture measures validate against external markers: innovation predicts patents/R&D/KLD innovation, integrity predicts fewer restatements and less option backdating, quality predicts product safety and top-brand status, respect predicts diversity and best-employer status, and teamwork predicts employee involvement and JVs/SAs.
3. Strong culture is associated with higher asset and inventory turnover, higher stock return volatility, lower discretionary accruals, higher CEO delta and vega, longer CEO pay duration, and higher Tobin's q.
4. The culture-performance relation is stronger in bad times: strong-culture financial firms perform better during the financial crisis, and strong-culture oil firms perform better around the BP oil spill.
5. Culture matters for M&A: innovation and respect are positively related to becoming an acquirer, integrity and quality are negatively related, culturally similar firm pairs are more likely to merge, and acquirer culture after the merger is related to the target's premerger culture.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Firm-year for culture measures; firm-year for outcome tests; firm-pair/deal for M&A tests |
| Sample period | Earnings calls from 2001 to 2018; M&A deals from 2003 to 2018 |
| Main dataset | 209,480 Thomson Reuters StreetEvents earnings-call QA sections, matched to Compustat |
| Key variables | Innovation, integrity, quality, respect, teamwork, strong culture indicator, cultural similarity, cultural distance |
| Treatment or shock | No primary exogenous treatment; strong culture is measured from text. Bad-times tests use the financial crisis and BP oil spill as adverse environments |
| Outcome variables | Validation markers, asset turnover, inventory turnover, stock return volatility, discretionary accruals, CEO delta, CEO vega, CEO pay duration, Tobin's q, abnormal returns, acquirer status, merger pairing, post-merger culture |

## 7. Identification Strategy

### Endogeneity Problem
The core endogeneity problem is that corporate culture is not randomly assigned. Firms with better managers, stronger governance, better products, superior technology, or more valuable growth opportunities may both talk differently and perform better. Reverse causality is also plausible: successful firms may develop or advertise stronger cultural language. Measurement error is important because earnings-call language may capture disclosure style, investor relations strategy, industry vocabulary, or managerial hype rather than actual internal culture. In M&A, culturally similar firms may merge because of product-market similarity or geography rather than culture itself. Therefore, most outcome tests should be interpreted as associations, not causal estimates.

### Identification Approach
- Natural experiment: Not the main design. The financial crisis and BP oil spill are used as adverse environments where culture may matter more.
- Instrument: None.
- Difference in differences: Bad-times tests interact strong culture with crisis-period indicators for financial firms and oil firms.
- Event study: Not clear from provided text.
- Fixed effects: Industry and year fixed effects are common; bad-times tests include firm and year fixed effects in some specifications.
- Matching: M&A tests use industry-size and industry-size-book-to-market matched control firms.
- Placebo tests: Not clear from provided text.
- Robustness: Uses QA section rather than full calls, seed-word alternatives, MD&A-based alternatives, removal of emotion-laden paragraphs, and removal of multisense words.
- Alternative source of variation: M&A acculturation tests use target-specific culture residuals after controlling for acquirer culture and characteristics.

### Is the Identification Convincing?
- Strength: Very strong as a measurement paper because it creates a transparent large-sample text measure and validates it against many external markers.
- Weakness: Weak as a causal paper because culture is endogenous and likely correlated with unobserved management quality, governance, industry strategy, and growth opportunities.
- Referee concern: The key concern is whether earnings-call language captures real culture or strategic disclosure. The QA focus and validation tests help, but they do not fully solve this concern.

## 8. Main Regression or Model

Measurement idea:

```text
CultureValue_it =
  tf-idf weighted frequency of words and phrases associated with value k
  in firm i's earnings-call QA section, averaged over a 3-year window
```

The five values are innovation, integrity, quality, respect, and teamwork. The model first trains word2vec on earnings-call text, then finds words and phrases close to seed words for each value, then scores each firm-year using weighted word counts.

Generic outcome regression:

```text
Outcome_it =
  beta StrongCulture_i,t-k
+ Controls_it
+ Industry FE
+ Year FE
+ epsilon_it
```

Here, `StrongCulture` equals one if the sum of the five culture values is in the top quartile across Compustat firms in a year. The coefficient `beta` captures whether firms with stronger measured culture have different future outcomes. It should be interpreted as predictive or associational rather than causal.

Bad-times specification:

```text
AbnormalReturn_it =
  beta1 StrongCulture_i
+ beta2 Crisis_t
+ beta3 StrongCulture_i x Crisis_t
+ Controls_it
+ Factor loadings
+ Firm FE
+ Year FE
+ epsilon_it
```

The main coefficient is `beta3`. A positive `beta3` means firms with strong culture perform better during adverse periods, consistent with the idea that culture is more valuable when formal contracts and rules cannot fully guide behavior.

M&A pairing specification:

```text
DealPair_ijt =
  beta CulturalSimilarity_ijt
+ Controls_acquirer
+ Controls_target
+ Deal controls
+ Deal FE
+ epsilon_ijt
```

A positive `beta` means culturally similar acquirer-target pairs are more likely to merge than matched counterfactual pairs.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Corporate Culture]] by creating a large-sample, firm-year measure of culture rather than relying only on surveys, interviews, or indirect proxies.
2. [[Textual Analysis]] by introducing word embeddings to capture semantic meaning beyond dictionary word counts.
3. [[Machine Learning in Finance]] by showing how semisupervised NLP can measure subtle firm attributes.
4. [[Mergers and Acquisitions]] by documenting that cultural fit predicts merger pairing and that culture changes after M&A.

It differs from prior work because it measures culture directly from managerial language at scale, rather than using CEO traits, scandals, surveys, or static website values.

## 10. Closely Related Papers
- [[Guiso, Sapienza, and Zingales 2015]]: Corporate culture, stated values, and integrity.
- [[Graham, Grennan, Harvey, and Rajgopal 2018]]: Survey evidence on corporate culture and its importance.
- [[Graham et al. 2019]]: Executive survey/interview evidence on culture, performance, and M&A fit.
- [[Loughran and McDonald 2011]]: Finance-specific textual dictionaries and the importance of domain-specific language.
- [[Kogan et al. 2017]]: Patent-based innovation measures used in validation tests.
- [[Hoberg and Phillips 2016]]: Product-market similarity, useful for comparison in M&A pairing tests.
- [[Lins, Servaes, and Tamayo 2017]]: Social capital and firm performance during the financial crisis, closely related to the bad-times test.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the literature on corporate culture and firm outcomes. Discuss how papers measure culture and whether they establish causality.

How to use this paper:
- Main finding: Culture can be measured from earnings-call QA text using word2vec, and strong culture is associated with multiple firm outcomes.
- Data: 209,480 earnings-call transcripts, 62,664 firm-years, 7,501 firms, 2001 to 2018.
- Identification: Strong measurement validation, weaker causal identification. Bad-times and M&A tests provide suggestive settings.
- Limitation: Culture is endogenous and may proxy for management quality, disclosure strategy, industry trends, or firm strategy.
- Connection to other papers: Pair with [[Guiso, Sapienza, and Zingales 2015]] for stated values, [[Graham et al. 2018]] for surveys, and [[Loughran and McDonald 2011]] for textual methods.
- Best exam phrase: "Li, Mai, Shen, and Yan use word2vec on earnings-call QA transcripts to turn corporate culture from a survey concept into a scalable firm-year variable."

## 12. Hypotheses Inspired by This Paper
H1: Firms with stronger integrity culture scores have lower future misconduct, restatement, and enforcement risk, especially in weak governance environments.

H2: Cultural similarity between supply-chain partners predicts relationship durability, lower disruption risk, and faster recovery after shocks.

H3: The value of strong culture is higher when external uncertainty rises because shared values substitute for incomplete contracts and formal monitoring.

## 13. Possible Extension or Research Design
- Research question: Does corporate culture causally affect firm resilience during supply-chain disruptions?
- Hypothesis: Firms with stronger teamwork and respect cultures recover more quickly from supplier shocks because internal coordination and employee cooperation reduce adjustment frictions.
- Data: Earnings-call culture scores, FactSet Revere supplier-customer links, Compustat quarterly outcomes, shipping disruptions, natural disasters, or sanctions shocks.
- Identification: Difference in differences comparing firms exposed to plausibly exogenous supplier shocks, interacted with pre-shock culture scores measured before the shock.
- Expected result: High teamwork/respect firms experience smaller sales declines, faster inventory adjustment, and less margin compression after supplier disruptions.
- Contribution: Moves the culture literature from broad associations to a setting with clearer exogenous shocks and a mechanism tied to coordination.

## 14. Critiques

### Major Concern 1
Culture may be confounded with management quality or business strategy. Better managers may both build stronger firms and speak in ways that score high on culture. The validation tests show the measure is meaningful, but they do not isolate causal effects of culture.

### Major Concern 2
Earnings-call QA language may capture disclosure style, investor relations, analyst questioning, or industry vocabulary rather than actual employee beliefs and norms. The paper mitigates this by focusing on QA, using tf-idf weights, removing emotion-laden paragraphs, and validating against external markers, but measurement error remains.

### Minor Concern
The five cultural values come from S&P 500 website values in Guiso, Sapienza, and Zingales. These are useful and interpretable, but they may omit other important cultural dimensions such as hierarchy, adaptability, customer orientation, or risk tolerance.

### Referee Recommendation
Accept, because the paper makes a major measurement contribution and opens a large empirical literature on corporate culture, but frame the performance and M&A findings as suggestive associations rather than causal estimates.

## 15. Memory Hooks
- "Culture from calls": earnings-call QA text becomes firm-year culture scores.
- "Five values": innovation, integrity, quality, respect, teamwork.
- "Word2vec beats bag-of-words": context-specific phrases like teamwork-related idioms matter.
- "Strong culture works in bad times": financial crisis and BP oil spill tests.
- "Culture fits deals": culturally similar firms are more likely to merge, and target culture shows up post-merger.

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Corporate Culture]], [[Textual Analysis]], [[Machine Learning in Finance]], [[Mergers and Acquisitions]], or [[Firm Resilience]]. The clean exam answer is: "Li, Mai, Shen, and Yan use word2vec on earnings-call QA transcripts to measure five corporate values and show that strong culture predicts efficiency, risk-taking, lower earnings management, higher valuation, better bad-times returns, and culturally matched M&A." Use it to argue that machine learning can convert soft organizational concepts into measurable firm-year variables. In a critique answer, emphasize that culture is endogenous and the outcome regressions are mainly associational, but note that the paper is stronger than a standard correlation because it validates the measure externally, uses less-scripted QA text, compares alternative text measures, and tests settings where culture should matter most.
