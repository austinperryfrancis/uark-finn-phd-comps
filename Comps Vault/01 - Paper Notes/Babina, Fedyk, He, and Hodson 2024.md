---
type: paper
status: unread
title: Artificial Intelligence, Firm Growth, and Product Innovation
authors: Tania Babina, Anastassia Fedyk, Alex He, James Hodson
year: 2024
journal: Journal of Financial Economics
professor: DrJandik
seminar: null
jandik_paper_number: 52
jandik_week: 13
jandik_topic: Innovation and machine learning
jandik_done: false
field: Corporate Finance
literature:
- Technological Change
- Artificial Intelligence
- Intangible Capital
- '[[Innovation]]'
- Superstar Firms
methods:
- Long differences
- Instrumental variables
- Textual analysis
- Human capital measurement
datasets:
- Cognism resumes
- Burning Glass job postings
- '[[Compustat]]'
- USPTO trademarks
- '[[Patent Data]]'
- Hoberg-Phillips product text
identification: Long differences and IV using firms' ex ante exposure to AI-strong universities
main_result: Firms that invest more in AI grow faster in sales, employment, and market value, mainly through product innovation rather than productivity gains.
exam_relevance: high
must_memorize: true
tags:
- ai
- innovation
- intangible-capital
- firm-growth
- superstar-firms
- product-innovation
- technology-adoption
created: 2026-06-12
updated: 2026-06-12
---

# Babina, Fedyk, He, and Hodson 2024

## 1. One-Sentence Takeaway
This paper shows that firms investing more in AI grow faster in sales, employment, and market value using resume-based measures of AI-skilled labor, and the main contribution is showing that AI-powered growth operates primarily through [[Product Innovation]] rather than process efficiency.

## 2. Exam-Ready Abstract
Babina, Fedyk, He, and Hodson study whether firm-level investments in artificial intelligence generate real economic growth. They construct a new measure of firm-level AI investment from AI-skilled employees in Cognism resume data and validate it against Burning Glass job postings. The main empirical design is a 2010 to 2018 long-differences regression linking changes in the share of AI workers to changes in firm outcomes among U.S. public firms. They find that a one-standard-deviation increase in AI investment is associated with higher sales, employment, and market value, with IV estimates using exposure to AI-strong universities producing similar or larger magnitudes. The mechanism is product innovation: AI-investing firms produce more trademarks, more product patents, and changes in product portfolios, but do not show higher sales per worker, TFP, or process patents. The gains are stronger for initially larger firms and are associated with higher industry concentration, making the paper central for [[Technological Change]], [[Intangible Capital]], [[Product Innovation]], and [[Superstar Firms]].

## 3. Research Question
What is the economic impact of firm-level AI adoption?

More specifically: does AI adoption increase firm growth, and does it operate through product innovation, process innovation, labor-saving automation, or scale advantages for large firms?

## 4. Core Mechanism
Use this chain for comps:

```text
Increase in AI-skilled human capital
-> better prediction and faster learning from data
-> lower cost and uncertainty of product development
-> firms create or improve products and expand product scope
-> sales, employment, and market value rise
-> large firms benefit more, increasing industry concentration
```

## 5. Main Findings
1. AI investment rises sharply from 2010 to 2018 across sectors, not just in technology firms.
2. Firms with greater increases in AI-skilled workers experience higher growth in sales, employment, and market value.
3. The growth mechanism is product innovation: AI investment predicts more trademarks and product patents, but not higher productivity, sales per worker, TFP, or process patents.
4. AI benefits are concentrated among initially larger firms, consistent with data scale advantages and [[Superstar Firms]].
5. Industry-level AI investment is associated with higher industry sales, employment, HHI, and top-firm market share.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Firm-year and firm long-difference observations |
| Sample period | Main analysis: 2010 to 2018. Resume and job postings data also cover 2007 and 2010 to 2018 |
| Main dataset | Cognism employee resumes, Burning Glass job postings, Compustat |
| Key variables | Share of firm employees classified as AI-related, share of AI job postings, sales, employment, market value |
| Treatment or shock | Increase in firm-level AI-skilled human capital |
| Outcome variables | Sales growth, employment growth, market value growth, trademarks, product patents, product mix, COGS, operating expenses, sales per worker, TFP, process patents, industry concentration |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between AI investment and firm growth is not causal because high-growth firms may be more likely to hire AI workers. Firms may adopt AI because they already have better managers, better data, more cash, stronger intangible capital, or better investment opportunities. Reverse causality is also plausible: firms that expect future growth may hire AI workers in advance. Measurement error is also important because AI investment is difficult to observe directly. Equilibrium sorting is another concern because AI workers may choose firms with better growth prospects.

### Identification Approach
- Natural experiment: Not a clean natural experiment.
- Instrument: Firms' pre-2010 exposure to universities that were historically strong in AI research, interacted with the later supply of AI graduates. The idea is that firms historically hiring from AI-strong universities could more easily hire AI talent after AI became commercially important.
- Difference in differences: Not the primary design. The main design is long differences from 2010 to 2018.
- Event study: Distributed lead-lag model around AI investments. The paper finds no pre-trends and effects that appear after two to three years.
- Fixed effects: Industry fixed effects, plus rich firm, industry, and commuting-zone controls measured as of 2010.
- Matching: Not central.
- Placebo tests: Tests show firms exposed to AI-strong universities were not growing faster before 2010.
- Robustness: Controls for past firm and industry growth, Tobin's Q, robotics, non-AI IT, and non-AI data analytics. Also validates resume-based AI measure with job postings.
- Alternative source of variation: Job postings-based AI measure and IV-based predicted AI investment.

### Is the Identification Convincing?
- Strength: The paper combines a novel AI measure, long differences, dynamic timing tests, many controls, and an IV based on pre-existing university hiring networks.
- Weakness: The IV may violate exclusion if firms connected to AI-strong universities differ in unobserved innovation culture, managerial quality, or access to elite labor markets more generally.
- Referee concern: Exposure to AI universities may proxy for broader exposure to high-skill talent, innovation networks, or growth-oriented firms, even with controls for CS-strong and top-ranked universities.

## 8. Main Regression or Model

```text
ΔOutcome_i,2010-2018 =
  beta ΔShareAI_i,2010-2018
+ Controls_i,2010
+ Industry FE
+ epsilon_i
```

The paper regresses long-run changes in firm outcomes on long-run changes in the share of AI workers. The key coefficient is beta. It measures whether firms that increase AI-skilled human capital more also grow more in sales, employment, valuation, or innovation outcomes.

For heterogeneity by firm size:

```text
ΔOutcome_i,2010-2018 =
  beta1 ΔShareAI_i x Small_i
+ beta2 ΔShareAI_i x Medium_i
+ beta3 ΔShareAI_i x Large_i
+ Controls_i,2010
+ Industry-by-size-tercile FE
+ epsilon_i
```

Here beta3 is the key superstar-firm coefficient. The paper finds that the AI-growth relation is strongest among initially large firms, consistent with AI complementing scale and data.

For the IV:

```text
ΔShareAI_i,2010-2018 =
  pi ExposureToAIStrongUniversities_i,pre-2010
+ Controls_i,2010
+ Industry FE
+ eta_i
```

```text
ΔOutcome_i,2010-2018 =
  beta PredictedΔShareAI_i,2010-2018
+ Controls_i,2010
+ Industry FE
+ epsilon_i
```

The first stage asks whether firms historically connected to AI-strong universities hire more AI workers after AI becomes commercially valuable. The second stage asks whether that predicted AI adoption increases growth.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Technological Change]] by providing firm-level evidence on AI as a general purpose technology.
2. [[Intangible Capital]] by measuring technology adoption through AI-skilled human capital rather than accounting expenditures.
3. [[Product Innovation]] by showing that AI affects growth through new products, trademarks, and product patents.
4. [[Superstar Firms]] by showing that AI advantages are concentrated among large firms and associated with industry concentration.

It differs from prior work because it studies broad firm-level AI adoption across sectors rather than AI invention, occupation-level exposure, or specific AI applications like robo-advising, loan underwriting, or financial analysts.

## 10. Closely Related Papers
- [[Kogan, Papanikolaou, Seru, and Stoffman 2017]]: Uses patent-based measures of technological innovation and links innovation to firm value.
- [[Acemoglu and Restrepo 2020]]: Studies automation and labor-market effects of robots, useful contrast because AI here does not mainly reduce labor.
- [[Benmelech and Zator 2022]]: Robotics and labor or firm outcomes, useful contrast with AI as human-capital-intensive intangible technology.
- [[Autor et al. 2020]]: Superstar firms and concentration, connected to AI scale advantages.
- [[Crouzet and Eberly 2019]]: Intangible capital and concentration, connected to AI as an intangible asset.
- [[Hoberg and Phillips 2016]]: Product market text and product similarity, relevant for product portfolio measures.
- [[Fedyk and Hodson 2023]]: Resume data and human capital measurement.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the literature on technological change, intangible capital, and firm growth. How do recent papers measure technology adoption, and how do they establish causality?

How to use this paper:
- Main finding: AI adoption predicts higher sales, employment, and market value growth.
- Data: Cognism resumes to measure AI workers, Burning Glass job postings for validation, Compustat for firm outcomes, patents and trademarks for product innovation.
- Identification: Long differences plus IV based on pre-2010 exposure to AI-strong universities.
- Limitation: Firms connected to AI universities may differ in other unobserved ways.
- Connection to other papers: Contrasts with automation papers where technology replaces labor. Connects to intangibles and superstar firms because AI is human-capital-intensive and benefits large firms.
- Best exam phrase: "Babina et al. show that AI looks less like labor-saving automation and more like a product-innovation technology that scales large firms."

## 12. Hypotheses Inspired by This Paper
H1: Firms with larger increases in AI-skilled human capital experience greater subsequent product innovation, measured by trademarks and product patents.

H2: The growth effect of AI investment is stronger for firms with more proprietary data or larger customer bases.

H3: AI adoption increases industry concentration because large firms are better able to combine AI talent with data, capital, and product distribution.

## 13. Possible Extension or Research Design
- Research question: Does generative AI adoption after 2022 increase firm innovation and productivity differently from pre-generative AI adoption?
- Hypothesis: Generative AI has stronger short-run productivity effects in white-collar tasks than earlier AI, but product innovation effects remain strongest for data-rich firms.
- Data: Firm job postings mentioning LLMs, generative AI, prompt engineering, and foundation models; earnings call text; patent and trademark data; Compustat; GitHub or software vacancy data.
- Identification: Use differential exposure to the release of foundation models based on pre-2022 task composition, local AI labor supply, or pre-existing cloud/AI infrastructure.
- Expected result: Generative AI increases product experimentation and may also raise sales per worker in text-intensive industries.
- Contribution: Distinguishes pre-2022 prediction AI from post-2022 generative AI and tests whether the productivity J-curve begins to reverse.

## 14. Critiques

### Major Concern 1
The IV may not fully satisfy the exclusion restriction. Firms historically hiring from AI-strong universities may also be better managed, more innovative, more connected to elite labor markets, or more likely to adopt new technologies generally.

### Major Concern 2
AI-skilled workers may be a proxy for broader intangible investment. Although the paper controls for robotics, non-AI IT, and data analytics, AI hiring may still coincide with unmeasured organizational capital, data infrastructure, or managerial transformation.

### Minor Concern
The resume-based measure captures AI-skilled human capital but may miss outsourced AI, vendor-provided AI, cloud AI services, or internal AI use by workers whose job titles do not contain AI-related terms.

### Referee Recommendation
Accept, because the paper provides a novel measurement contribution, strong cross-validation with job postings, credible timing tests, an innovative IV, and a clear mechanism through product innovation. The causal claim should be framed as suggestive but stronger than a standard correlation.

## 15. Memory Hooks
- "AI workers, not AI patents": the paper measures adoption through human capital.
- "Prediction technology becomes product innovation": AI helps firms learn faster and develop products.
- "Not robots": AI does not mainly show up as lower labor or higher productivity.
- "Universities as AI labor supply": IV uses pre-2010 exposure to AI-strong universities.
- "Bigger firms win": AI growth is strongest for large firms and linked to concentration.

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Technological Change]], [[Artificial Intelligence]], [[Intangible Capital]], [[Product Innovation]], [[Superstar Firms]], or [[Instrumental Variables]]. The clean exam answer is: "Babina, Fedyk, He, and Hodson use AI-skilled workers in resume data as a firm-level measure of AI investment and show that AI adoption increases sales, employment, and market value primarily through product innovation." Use it to argue that new technologies need not work mainly through productivity or labor substitution. In a critique answer, emphasize that selection into AI adoption is a serious concern, but note that the paper is stronger than a standard correlation because it uses long differences, no-pretrend tests, controls for other technologies, and an IV based on firms' pre-existing exposure to AI-strong universities.