---
type: paper
status: unread
title: New Evidence and Perspectives on Mergers
authors: Gregor Andrade, Mark Mitchell, Erik Stafford
year: 2001
journal: Journal of Economic Perspectives
seminar:
field: Corporate Finance
literature:
  - Mergers and Acquisitions
  - Market for Corporate Control
  - Industry Shocks
  - Event Studies
methods:
  - Descriptive evidence
  - Event study
  - Abnormal returns
  - Industry shock analysis
  - Fama-MacBeth style operating performance regressions
datasets:
  - CRSP
  - Compustat
identification:
  - Event study around merger announcements
  - Industry deregulation windows
  - Industry benchmarked operating performance
main_result: Mergers occur in industry waves, deregulation explains a large share of 1990s merger activity, and mergers create positive combined shareholder value mostly captured by target shareholders.
exam_relevance: high
must_memorize: true
tags:
  - mergers
  - acquisitions
  - corporate-control
  - event-studies
  - industry-shocks
  - deregulation
  - stock-financing
  - DrJandik
  - corporate-finance
created: 2026-06-05
updated: 2026-06-05
---

# Andrade Mitchell and Stafford 2001

## 1. One-Sentence Takeaway
This paper shows that U.S. merger waves are strongly clustered by industry and partly driven by deregulation using CRSP merger data from 1973 to 1998, and the main contribution is to connect merger activity, announcement returns, payment method, and post-merger performance in one exam-useful survey.

## 2. Exam-Ready Abstract
Andrade, Mitchell, and Stafford study why mergers occur, who gains from them, and whether they create value. They focus on completed mergers between publicly traded U.S. acquirers and targets from 1973 to 1998 using CRSP, with Compustat used for operating performance tests. The paper emphasizes two facts: mergers occur in waves and merger waves cluster strongly by industry. They argue that industry shocks, especially deregulation, help explain when and where mergers occur. In the 1990s, deregulated industries account for nearly half of merger activity after the late 1980s, making deregulation central to that merger wave. Event studies show positive combined announcement returns, large target gains, and roughly zero or slightly negative acquirer gains, especially in stock-financed deals. This paper connects to [[Mergers and Acquisitions]], [[Market for Corporate Control]], [[Event Studies]], and [[Industry Shocks]].

## 3. Research Question
What explains merger waves, and do mergers create shareholder value?

More specifically: the paper asks whether merger activity reflects industry-level shocks, especially deregulation, and whether value creation differs across targets, acquirers, payment methods, and post-merger performance measures.

## 4. Core Mechanism

```text
Industry shock or deregulation
-> new investment opportunities and removal of barriers to consolidation
-> industry restructuring pressure
-> firms merge, often within the same industry
-> target shareholders capture large gains, combined firms create modest value
-> long-run value creation is harder to identify, but operating margins improve slightly
```

## 5. Main Findings
1. Merger activity occurs in waves and clusters by industry. The industry composition of merger waves changes across decades, suggesting that common industry shocks help explain merger timing.
2. Deregulation is a major driver of 1990s merger activity. Industries such as airlines, broadcasting, entertainment, natural gas, trucking, banks and thrifts, utilities, and telecommunications experienced large merger activity around deregulation windows.
3. Announcement returns imply that mergers create modest combined shareholder value, but gains accrue mostly to targets. Targets earn about 16 percent over the three-day announcement window, while acquirer returns are near zero or negative.
4. Payment method matters. Stock-financed mergers have lower combined and acquirer returns, consistent with adverse selection or overvaluation concerns from equity issuance.
5. Long-run abnormal return evidence is difficult to interpret because expected returns are hard to estimate over long horizons and merger events are clustered through time and industry.
6. Operating performance evidence is more favorable: post-merger operating margins improve by roughly 1 percentage point relative to industry benchmarks after controlling for pre-merger performance.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Completed merger deal, with acquirer and target publicly traded U.S. firms |
| Sample period | Main CRSP merger sample from 1973 to 1998; aggregate merger activity shown from the early 1960s |
| Main dataset | CRSP for stock prices and listed firms; Compustat for accounting performance |
| Key variables | Merger activity, deal value, payment method, hostile bid indicator, same-industry indicator, announcement abnormal returns, operating margins |
| Treatment or shock | Industry deregulation windows, defined as three years before to six years after major deregulation events |
| Outcome variables | Merger frequency, merger value, target abnormal returns, acquirer abnormal returns, combined abnormal returns, post-merger abnormal operating performance |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between mergers and performance is not causal because firms choose to merge. Merger targets are selected, acquirers may buy firms when they expect synergies, and industries may consolidate precisely when they are hit by shocks that would have changed performance even without mergers. Payment method is also endogenous because managers may use stock when they believe their equity is overvalued. Long-run return tests face additional endogeneity and inference problems because mergers cluster by industry and time, so abnormal returns are cross-correlated rather than independent.

### Identification Approach
- Natural experiment: Deregulation is used as a relatively well-timed industry shock, but the paper is mostly descriptive rather than a clean causal design.
- Instrument: None.
- Difference in differences: Not a formal DiD paper.
- Event study: Yes. The paper uses short-window announcement returns around merger announcements to infer expected value creation.
- Fixed effects: Not the central design.
- Matching: Not central. Operating performance is benchmarked against industry medians.
- Placebo tests: Not clear from provided text.
- Robustness: Discusses short-window versus long-window returns, payment method splits, industry benchmarking, and long-run return inference problems.
- Alternative source of variation: Industry deregulation windows and differences between stock-financed and non-stock-financed deals.

### Is the Identification Convincing?
- Strength: The short-window event study is persuasive for market expectations because expected returns over three days are near zero and confounding events are less likely.
- Weakness: It does not prove that mergers cause real efficiency gains because merger selection and industry shocks remain endogenous.
- Referee concern: Deregulation windows may capture broader industry trends, technology, demand shocks, or financial market conditions rather than deregulation alone.

## 8. Main Regression or Model

This is not a single-equation causal paper. For comps, use two equations.

### Event-study logic

```text
CAR_i[-1,+1] = Actual Return_i[-1,+1] - Expected Return_i[-1,+1]
```

This measures the abnormal stock return for target, acquirer, or combined firms around the merger announcement. The key interpretation is that, under semi-strong market efficiency, the short-window CAR captures the market's expectation of value created or destroyed by the deal.

### Operating performance logic

```text
AOP_i,t+1 = alpha + beta AOP_i,t-1 + epsilon_i,t
```

Where abnormal operating performance is the firm's operating margin minus the corresponding industry median operating margin. The intercept alpha captures post-merger operating performance after controlling for pre-merger operating performance. The paper finds alpha around 1 percent, suggesting that merged firms improve operating performance relative to industry benchmarks.

### Industry shock intuition

```text
Merger Activity_j,t = alpha + beta Deregulation Window_j,t + epsilon_j,t
```

This is the exam-useful way to express the paper's logic, even though the paper mainly documents deregulation windows descriptively. The coefficient beta would capture whether industries exposed to deregulation experience more merger activity.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Mergers and Acquisitions]] by updating the evidence through the 1990s merger wave.
2. [[Market for Corporate Control]] by showing that targets capture most announcement gains while acquirer gains are small.
3. [[Industry Shocks]] by emphasizing that merger waves cluster by industry and are partly explained by deregulation.
4. [[Event Studies]] by defending short-window announcement returns against noisy long-run abnormal return tests.

It differs from prior work because it combines descriptive merger wave evidence, deregulation-based industry shock evidence, payment method splits, announcement returns, long-run return critiques, and operating performance evidence in one synthesis.

## 10. Closely Related Papers
- [[Jensen and Ruback 1983]]: Classic survey showing that corporate control transactions create gains, mostly for targets.
- [[Jarrell Brickley and Netter 1988]]: Reviews takeover evidence from the 1980s and discusses whether shareholder gains reflect real efficiency or wealth transfers.
- [[Mitchell and Mulherin 1996]]: Key industry shock paper linking takeover activity to deregulation, oil shocks, foreign competition, and financial innovation.
- [[Healy Palepu and Ruback 1992]]: Finds operating performance improvements after large mergers using industry benchmarks.
- [[Loughran and Vijh 1997]]: Long-run return paper finding poor post-merger performance for stock acquirers.
- [[Rau and Vermaelen 1998]]: Long-run return paper emphasizing glamour versus value acquirers.
- [[Mitchell and Stafford 2000]]: Critiques long-run event study inference and accounts for cross-sectional dependence.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on mergers and acquisitions. Discuss why mergers occur, who gains, and how the literature establishes value creation.

How to use this paper:
- Main finding: Mergers cluster by industry, deregulation explains much of the 1990s wave, and combined firms create modest shareholder value with most gains captured by targets.
- Data: CRSP mergers involving publicly traded U.S. acquirers and targets from 1973 to 1998, plus Compustat for accounting performance.
- Identification: Short-window event studies for expected value creation; deregulation windows for industry shock evidence; industry-benchmarked operating performance for real effects.
- Limitation: The deregulation analysis is not a clean causal DiD, and merger choice remains endogenous.
- Connection to other papers: Use with [[Mitchell and Mulherin 1996]] for industry shocks, [[Jensen and Ruback 1983]] for target gains, and [[Healy Palepu and Ruback 1992]] for operating performance.
- Best exam phrase: "Andrade, Mitchell, and Stafford show that mergers are not randomly scattered corporate events, but industry-clustered responses to shocks, with deregulation central to the 1990s wave."

## 12. Hypotheses Inspired by This Paper
H1: Industries exposed to deregulation experience higher merger activity than otherwise similar industries not exposed to deregulation.

H2: Mergers financed with stock generate lower acquirer announcement returns than mergers financed without stock because stock payment conveys negative information about acquirer valuation.

H3: Same-industry mergers following industry shocks generate larger operating performance improvements than diversifying mergers because industry shocks create clearer consolidation and efficiency motives.

## 13. Possible Extension or Research Design
- Research question: Do modern regulatory shocks cause merger waves and real efficiency gains?
- Hypothesis: Regulatory liberalization increases same-industry merger activity, and deals in treated industries improve operating performance relative to matched untreated industries.
- Data: SDC or Refinitiv M&A data, CRSP, Compustat, regulatory event dates, industry concentration data, possibly Census plant-level productivity data.
- Identification: Staggered difference-in-differences comparing treated industries around regulatory shocks to matched untreated industries, with industry and year fixed effects.
- Expected result: Treated industries experience higher merger rates, positive combined announcement returns, and modest post-merger operating improvements.
- Contribution: Converts the Andrade, Mitchell, and Stafford industry-shock intuition into a cleaner causal design.

## 14. Critiques

### Major Concern 1
The deregulation analysis is mostly descriptive. Deregulated industries may differ from other industries in technology, demand growth, capital intensity, political economy, or financial constraints. Without a formal counterfactual, it is difficult to isolate deregulation from other contemporaneous shocks.

### Major Concern 2
Event-study evidence captures expected value creation, not necessarily realized real efficiency. If investors are overly optimistic during merger waves, short-window abnormal returns may overstate true gains.

### Minor Concern
The sample is restricted to public U.S. acquirers and targets. Results may not generalize to private targets, private acquirers, cross-border mergers, or small transactions outside CRSP coverage.

### Referee Recommendation
Accept, because the paper is a high-value synthesis that organizes major M&A facts and frames merger waves around industry shocks. For a modern causal paper, I would ask for a cleaner deregulation design, but as a JEP review and evidence paper, it is highly useful.

## 15. Memory Hooks
- "1990s equals decade of deregulation."
- "Merger waves cluster by industry, not just by time."
- "Targets win big, acquirers break even."
- "Stock deals look worse because a stock merger is also an equity issue."
- "Short-window event studies are cleaner than long-run drift tests."
- "Operating margins improve by about 1 percent relative to industry benchmarks."

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | Medium |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Mergers and Acquisitions]], [[Market for Corporate Control]], [[Industry Shocks]], [[Deregulation]], or [[Event Studies]]. The clean exam answer is: "Andrade, Mitchell, and Stafford use CRSP merger data from 1973 to 1998 and show that merger waves cluster by industry, deregulation explains a large share of 1990s merger activity, and mergers create modest combined shareholder value mostly captured by targets." Use it to argue that mergers are often responses to industry shocks rather than isolated managerial decisions. In a critique answer, emphasize that merger choice and deregulation exposure are endogenous, but note that the paper is stronger than a standard correlation because it combines industry timing, announcement returns, payment-method heterogeneity, and operating performance evidence.