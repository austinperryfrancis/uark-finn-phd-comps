---
type: paper
status: unread
title: Technological Innovation, Resource Allocation, and Growth
authors: Leonid Kogan, Dimitris Papanikolaou, Amit Seru, Noah Stoffman
year: 2017
journal: Quarterly Journal of Economics
professor: DrJandik
seminar: null
jandik_paper_number: 49
jandik_week: 13
jandik_topic: Innovation and machine learning
jandik_done: false
field: Innovation, Macro Finance, Corporate Finance, Asset Pricing
literature:
- Technological Innovation
- Creative Destruction
- Firm Growth
- Productivity
methods:
- patent event study
- panel regressions
- aggregate predictive regressions
- instrumental variables
datasets:
- '[[Patent Data]]'
- '[[CRSP]]'
- '[[Compustat]]'
- Nicholas patent citations
- GDP
- utilization-adjusted TFP
identification: stock market response to patent grants, industry-year variation, R&D tax credit instrument
main_result: Privately valuable patents predict own firm growth, competitor decline, resource reallocation, and medium-run aggregate output and TFP growth.
exam_relevance: high
must_memorize: true
tags:
- innovation
- patents
- creative-destruction
- firm-growth
- productivity
- qje
created: 2026-06-12
updated: 2026-06-12
---

# Kogan, Papanikolaou, Seru, and Stoffman 2017

## 1. One-Sentence Takeaway
This paper shows that privately valuable patents, measured using stock market reactions around patent grants, predict firm growth, productivity, resource reallocation, and aggregate TFP growth, and the main contribution is a dollar-based measure of innovation quality that captures creative destruction better than citation-weighted patent counts.

## 2. Exam-Ready Abstract
Kogan, Papanikolaou, Seru, and Stoffman ask whether technological innovation causes firm growth, resource reallocation, and aggregate productivity growth. They build a patent-level measure of private economic value by combining U.S. patent grants from 1926 to 2010 with CRSP stock returns around patent issuance dates. The key idea is that a patent grant reveals information about the private value of the innovation, and the stock price response can be filtered to estimate the dollar value of the patent. At the firm level, own innovation predicts higher future profits, output, capital, employment, and TFPR, while innovation by competitors predicts lower growth, consistent with Schumpeterian creative destruction. At the aggregate level, value-weighted innovation predicts medium-run output and TFP growth. The paper belongs in [[Technological Innovation]], [[Creative Destruction]], [[Firm Growth]], [[Productivity]], and [[Asset Pricing and Real Effects]].

## 3. Research Question
What is the economic value of innovation, and does privately valuable innovation predict firm growth, resource allocation, creative destruction, and aggregate productivity growth?

More specifically: the paper tests whether stock-market-valued patents capture the private economic importance of innovation and whether this private value predicts both own-firm expansion and competitor contraction.

## 4. Core Mechanism

```text
Patent grant to public firm
-> stock market updates about private value of the patent
-> firm gains monopoly rents, product quality, or new product varieties
-> innovating firm expands profits, output, capital, labor, and productivity
-> rival firms lose business or face factor-price pressure
-> industry resources reallocate toward innovators and aggregate TFP rises
```

## 5. Main Findings
1. Patent-level private value is positively related to forward citations. An additional citation is associated with a 0.1% to 3.2% increase in estimated patent value, depending on controls.
2. Own innovation predicts firm growth. A one standard deviation increase in own innovation is associated over five years with about 4.6% higher profits, 3.2% higher output, 3.8% higher capital, 2.5% higher employment, and 2.4% higher TFPR.
3. Competitor innovation predicts creative destruction. A one standard deviation increase in competitors' innovation is associated over five years with about 3.8% lower profits, 5.1% lower output, 3.8% lower capital, 2.7% lower employment, and 1.7% lower TFPR.
4. Citation-weighted patents predict own firm growth but do not capture competitor-driven creative destruction as strongly.
5. The aggregate innovation index predicts medium-run output and TFP growth, suggesting that value-weighted innovation captures more than simple patent counts.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Patent-level for innovation value; firm-year for firm growth; annual aggregate for macro tests |
| Sample period | Patent data from 1926 to 2010; firm-year growth sample mainly 1950 to 2010 |
| Main dataset | Google Patents matched to CRSP public firms, CRSP stock returns, Compustat firm fundamentals, patent citations, Nicholas citation data |
| Key variables | Patent value, citation-weighted patents, own innovation, competitor innovation, profits, output, capital, employment, TFPR |
| Treatment or shock | Patent grant event and associated stock market reaction |
| Outcome variables | Patent citations, firm growth, productivity, aggregate output growth, aggregate TFP growth |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between patenting and firm growth is not causal. High-growth firms may invest more in R&D, receive more investor attention, have better managers, or operate in expanding industries. Reverse causality is plausible because expected growth can cause innovation rather than innovation causing growth. Omitted demand shocks could raise both stock prices and future growth. Measurement error is also central because stock returns around patent grant dates may include unrelated news, market-wide movements, discount-rate shocks, or changes in the probability that the patent is approved.

### Identification Approach
- Natural experiment: Not a clean natural experiment. The patent grant date is used as a narrow information event.
- Instrument: Uses an R&D price variable based on state-level R&D tax credits from Bloom, Schankerman, and Van Reenen as an instrument for own and competitor innovation. The first stage is negative, and second-stage results are qualitatively similar and stronger.
- Difference in differences: Not the main design.
- Event study: The innovation measure is built from stock returns in a three-day window around patent grants.
- Fixed effects: Firm-level regressions include industry fixed effects and time fixed effects. Patent citation regressions include grant-year, technology-class-year, firm, and firm-year fixed effects in some specifications.
- Matching: Not a main method.
- Placebo tests: Randomly assigns placebo patent grant dates within the same grant year and reconstructs the measure. Placebo coefficients are centered near zero.
- Robustness: Alternative event windows, alternative return adjustments, alternative scaling by market capitalization, controls for R&D, controls for investor attention, and comparisons to citation-weighted patents.
- Alternative source of variation: Post-2000 patent application publication rules and R&D tax-credit-based R&D price variation.

### Is the Identification Convincing?
- Strength: The measure is forward-looking, dollar-based, comparable across industries and time, and tied to high-frequency market reactions around patent grants.
- Weakness: The firm-growth regressions remain partly correlational. Stock returns around patent grants may capture other information, and the private value of a patent is not the same as social value.
- Referee concern: The R&D tax credit instrument may affect firm growth through channels other than innovation, such as investment, hiring, or location decisions. Competitor innovation may also proxy for unobserved industry shocks.

## 8. Main Regression or Model

Patent value construction:

```text
R_j = v_j + epsilon_j

xi_j = (1 - pi_bar)^(-1) * (1 / N_j) * E[v_j | R_j] * M_j
```

`R_j` is the market-adjusted stock return around patent grant `j`. `v_j` is the patent-value component of the return, `epsilon_j` is unrelated news, `M_j` is market capitalization, `N_j` is the number of patents granted to the same firm on the same day, and `pi_bar` adjusts for the ex ante probability of patent approval.

Firm growth regression:

```text
log(X_f,t+tau) - log(X_f,t)
  = a_tau Innovation_f,t
  + b_tau CompetitorInnovation_I\f,t
  + c Controls_f,t
  + Industry FE
  + Time FE
  + epsilon_f,t+tau
```

`X` is profits, output, capital, employment, or TFPR. `a_tau` measures how own innovation predicts future firm growth. `b_tau` measures creative destruction, or how competitors' innovation predicts the firm's future growth. The central economic interpretation is that `a_tau > 0` and `b_tau < 0`.

Aggregate prediction regression:

```text
x_t+tau - x_t
  = a_0
  + a_tau log(AggregateInnovation_t)
  + lags of x_t
  + epsilon_t+tau
```

`x` is log output or log TFP. `a_tau` measures whether waves of privately valuable innovation forecast medium-run aggregate growth.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Technological Innovation]] by creating a patent-level dollar measure of innovation value.
2. [[Creative Destruction]] by showing that competitor innovation reduces incumbent growth.
3. [[Firm Growth]] by linking privately valuable innovation to profits, output, capital, labor, and productivity.
4. [[Productivity]] by showing that value-weighted innovation predicts aggregate TFP.

It differs from prior work because it uses stock market reactions to patent grants to value patents directly, rather than relying only on patent counts, R&D spending, or citation-weighted patents.

## 10. Closely Related Papers
- [[Hall, Jaffe, and Trajtenberg 2005]]: Uses citation-weighted patents to study market value and innovation.
- [[Pakes 1985]]: Early work linking patent arrivals to stock market returns.
- [[Bloom, Schankerman, and Van Reenen 2013]]: Separates technology spillovers from product-market rivalry using R&D.
- [[Aghion and Howitt 1992]]: Schumpeterian growth model with creative destruction.
- [[Klette and Kortum 2004]]: Firm dynamics and innovation in endogenous growth.
- [[Romer 1990]]: Endogenous growth through technological change.
- [[Olley and Pakes 1996]]: Productivity estimation and reallocation.
- [[Shea 1999]]: Direct measures of technology shocks using patents and R&D.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on innovation, firm growth, and productivity. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: Privately valuable innovation predicts own-firm growth, competitor decline, and aggregate productivity growth.
- Data: U.S. patents matched to CRSP and Compustat, 1926 to 2010.
- Identification: Patent grant event returns identify private patent value; firm panel regressions relate value-weighted innovation to future outcomes; robustness uses R&D tax-credit-based instruments.
- Limitation: The firm-level growth results are not a pure causal design and the measure captures private, not social, patent value.
- Connection to other papers: Use with [[Hall, Jaffe, and Trajtenberg 2005]], [[Bloom, Schankerman, and Van Reenen 2013]], [[Aghion and Howitt 1992]], and [[Klette and Kortum 2004]].
- Best exam phrase: "Kogan et al. convert patent grants into a dollar measure of private innovation value using stock market reactions, then show that own innovation creates growth while rival innovation destroys it."

## 12. Hypotheses Inspired by This Paper
H1: Firms with higher value-weighted innovation experience higher subsequent sales, employment, capital investment, and productivity growth than otherwise similar firms.

H2: Competitor innovation has a negative effect on incumbent growth, and this effect is stronger in industries with greater product-market overlap.

H3: Value-weighted patent measures forecast aggregate TFP growth better than simple patent counts or citation-weighted patent counts.

## 13. Possible Extension or Research Design
- Research question: Does innovation create social spillovers that differ from private patent value?
- Hypothesis: Patents with high private value but negative competitor reactions generate business stealing, while patents with positive competitor reactions generate spillovers.
- Data: Patent grants matched to CRSP, Compustat, product-market similarity, patent citations, and competitor stock returns.
- Identification: Estimate stock price reactions of both the patenting firm and its product-market competitors around the patent grant window.
- Expected result: Own-firm reaction measures private value; competitor reaction separates creative destruction from spillovers.
- Contribution: Extends Kogan et al. from private value to a measure closer to social value.

## 14. Critiques

### Major Concern 1
The firm-growth regressions are not fully causal. High-growth firms may innovate more, and expected future growth could raise stock price reactions around patent grants.

### Major Concern 2
Patent grant-day returns may include other news, investor attention, changing discount rates, or anticipated information. The measure depends on assumptions used to filter patent-related returns from noise.

### Minor Concern
The sample focuses on public firms with patents, so the results may miss private firms, nonpatented innovation, trade secrets, and process improvements that are not patented.

### Referee Recommendation
Accept, because the paper creates a powerful and reusable measure of innovation value and provides evidence consistent with Schumpeterian growth, but interpret the firm-growth regressions as strongly suggestive rather than fully causal.

## 15. Memory Hooks
- "Stock market votes on patent day."
- "Private value is not the same as scientific value."
- "Own patents grow the firm, rival patents shrink it."
- "Citation counts miss creative destruction."
- "Three waves: 1930s, 1960s, 1990s."
- "Patent value is a dollar weight, not just a count."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Technological Innovation]], [[Creative Destruction]], [[Firm Growth]], [[Productivity]], [[Asset Pricing and Real Effects]], or [[Patent Data]]. The clean exam answer is: "Kogan, Papanikolaou, Seru, and Stoffman use stock market reactions to patent grants as a dollar-based measure of private innovation value and show that valuable innovation predicts own-firm growth, competitor decline, and medium-run aggregate productivity growth." Use it to argue that innovation affects both the level and allocation of economic activity. In a critique answer, emphasize that the firm-level results are not a clean natural experiment, but note that the paper is stronger than a standard patent-count correlation because it uses high-frequency market reactions, placebo patent dates, rich controls, and R&D tax-credit-based instruments.