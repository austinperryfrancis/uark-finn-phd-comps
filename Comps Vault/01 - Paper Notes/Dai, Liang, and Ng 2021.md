---
type: paper
status: unread
title: Socially Responsible Corporate Customers
authors: Rui Dai, Hao Liang, Lilian Ng
year: 2021
journal: Journal of Financial Economics
professor: DrJandik
seminar: null
jandik_paper_number: 44
jandik_week: 11
jandik_topic: Suppliers and customers
jandik_done: false
field: Corporate Finance
literature:
- CSR
- Supply Chains
- Stakeholder Governance
methods:
- Panel regressions
- RDD
- event study
- mechanism tests
datasets:
- '[[FactSet Revere]]'
- Thomson Reuters ASSET4
- MSCI IVA
- Sustainalytics
- ISS Voting
- RepRisk
- Worldscope
- '[[Patent Data]]'
- '[[BoardEx]]'
- FactSet Ownership
identification: Close-call CSR proposal RDD and product-safety scandal shocks
main_result: Customer CSR propagates downstream to suppliers, but supplier CSR does not symmetrically affect customers.
exam_relevance: high
must_memorize: true
tags:
- csr
- supply-chains
- stakeholder-governance
- rdd
- corporate-customers
- esg
created: 2026-06-12
updated: 2026-06-12
---

# Dai, Liang, and Ng 2021

## 1. One-Sentence Takeaway
This paper shows that socially responsible corporate customers push suppliers to improve CSR using global customer-supplier links, ESG ratings, close-call CSR shareholder votes, and product-safety scandals, and the main contribution is showing that CSR can propagate through real supply-chain relationships rather than only through regulation, investors, or peer effects.

## 2. Exam-Ready Abstract
Dai, Liang, and Ng ask whether corporate customers influence the CSR behavior of their suppliers in global supply chains. They merge FactSet Revere customer-supplier links with ASSET4 ESG ratings for 34,117 customer-supplier pairs across 50 countries from 2003 to 2015. The baseline result is unilateral: customer CSR predicts future supplier CSR, but supplier CSR does not predict future customer CSR. The identification concern is that high-CSR customers may simply select high-CSR suppliers, so the paper uses close-call CSR shareholder proposals at customer firms as quasi-random variation in customer CSR commitment and product-safety scandals as shocks that increase customer incentives to discipline suppliers. The mechanisms include positive assortative matching, customer bargaining power, supplier decision-making, common ownership, and board connectedness. Collaborative CSR improves operating efficiency and firm valuation for both sides, while increasing future sales growth mainly for customers. This paper connects to [[Corporate Social Responsibility]], [[Supply Chains]], [[Stakeholder Governance]], and [[ESG and Firm Value]].

## 3. Research Question
What is the paper trying to answer?

Do socially responsible corporate customers cause their suppliers to adopt higher CSR standards?

More specifically, the paper tests whether CSR propagation is:
1. Directional from customers to suppliers rather than suppliers to customers.
2. Driven by customer pressure, relationship formation, and network connectedness.
3. Economically valuable for customers and suppliers.

## 4. Core Mechanism

```text
High customer CSR or shock increasing customer CSR salience
-> customer faces reputational and stakeholder pressure from supplier behavior
-> customer screens, pressures, or coordinates with suppliers
-> supplier improves CSR to preserve the customer relationship
-> higher supplier CSR, better supply-chain alignment, and improved operating efficiency or valuation
```

For the scandal setting:

```text
Product-safety scandal
-> public concern about supply-chain responsibility rises
-> customers face reputation risk from supplier failures
-> customers pressure suppliers to improve product responsibility
-> supplier product-responsibility ratings rise
-> reputation risk and CSR become transmitted through the supply chain
```

## 5. Main Findings
1. Customer CSR positively predicts future supplier CSR, but supplier CSR does not predict future customer CSR. The effect is economically meaningful: a one-standard-deviation increase in customer CSR generates about an 8% aggregate increase in supplier CSR through the customer's direct network.
2. Close-call CSR proposal passage at customer firms leads suppliers to improve CSR, supporting a causal interpretation. The supplier's next-year CSR is about 24% of a standard deviation higher when the customer narrowly passes rather than narrowly fails a CSR proposal.
3. Product-safety scandals, including the 2008 Chinese milk scandal and the 2013 Takata airbag and Toyota recalls, strengthen the customer-to-supplier CSR effect. Supplier product responsibility rises more when customers have high product responsibility in the scandal year.
4. Mechanisms include assortative matching, customer bargaining power, lower supplier relationship-specific investment, industry structure, common institutional ownership, and common directors.
5. Collaborative CSR improves operating efficiency and valuation for both customers and suppliers, but future sales growth increases mainly for customers.

## 6. Data
| Item | Details |
|---|---|
| Unit of observation | Customer-supplier pair-year |
| Sample period | 2003 to 2015 |
| Main dataset | FactSet Revere global customer-supplier links merged with Thomson Reuters ASSET4 ESG ratings |
| Sample size | 34,117 unique customer-supplier pairs from 50 countries |
| Key variables | Customer CSR score, supplier CSR score, environmental score, social score, product-responsibility score |
| Treatment or shock | Customer CSR, close-call customer CSR proposal passage, product-safety scandals |
| Outcome variables | Supplier future CSR, supplier product-responsibility score, RepRisk, SG&A, future sales growth, market-to-book |
| Other datasets | MSCI IVA, Sustainalytics, Vigeo country CSR, ISS Voting, RepRisk, Worldscope, PATSTAT, FactSet Ownership, BoardEx, SDC Platinum |

## 7. Identification Strategy

### Endogeneity Problem
A simple correlation between customer CSR and supplier CSR is not causal because customers may select suppliers that already have high CSR or are more likely to improve CSR. This is a positive assortative matching problem. Omitted variables could also matter: high-quality management, industry norms, country institutions, supply-chain complexity, stakeholder pressure, or exposure to global consumers may jointly affect both customer and supplier CSR. Reverse causality is less likely but possible if customers choose high-CSR policies because they already source from responsible suppliers. There is also equilibrium sorting: firms with similar ESG preferences may match in the supply-chain market.

### Identification Approach
- Natural experiment: Product-safety scandals, especially the 2008 Chinese milk scandal and 2013 Takata airbag and Toyota recalls, increase public concern about supply-chain responsibility.
- Instrument: Not clear from provided text.
- Difference in differences: Scandal regressions compare CSR propagation around event years using event indicators and interactions with customer product-responsibility scores.
- Event study: RepRisk analysis around ESG scandal announcement months shows supplier scandals increase customer reputation risk.
- Fixed effects: Customer-supplier industry, customer-supplier country, year fixed effects, and in some specifications customer-supplier firm fixed effects.
- Matching: Pseudo supplier falsification tests match true suppliers to industry or country peers that are not linked to the customer.
- Placebo tests: No customer CSR effect on pseudo suppliers. Interactions with other year dummies around scandals are not statistically significant.
- Robustness: Alternative CSR databases, differential CSR measures, environmental and social components, location splits, and falsification tests.
- Alternative source of variation: Close-call CSR proposal votes at customer firms using RDD.

### Is the Identification Convincing?
- Strength: The close-call CSR proposal RDD is the strongest design because narrowly passing versus narrowly failing CSR proposals is plausibly quasi-random near the threshold.
- Weakness: CSR proposal passage may be partly symbolic if firms do not implement the proposal, though the paper addresses this with fuzzy RDD and implementation definitions.
- Referee concern: Product-safety scandals may affect both customers and suppliers through broad industry-wide attention rather than only through customer pressure.

## 8. Main Regression or Model

Baseline propagation model:

```text
CSR_Supplier_{i,j,t+1}
=
alpha
+ beta CSR_Customer_{i,j,t}
+ Controls_{i,j,t}
+ Customer-Supplier Industry FE
+ Customer-Supplier Country FE
+ Year FE
+ epsilon_{i,j,t+1}
```

The dependent variable is the supplier's future CSR score. The key coefficient is beta. If beta is positive, higher customer CSR predicts higher supplier CSR in the next period. The paper also reverses the regression to test whether supplier CSR predicts future customer CSR and finds no symmetric effect.

RDD model:

```text
CSR_Supplier_{t+1}
=
alpha
+ beta Pass_Customer_CSR_Proposal_t
+ gamma VoteShareForCSRProposal_t
+ epsilon_{t+1}
```

Here, `Pass_Customer_CSR_Proposal` equals one if the customer narrowly passes a CSR proposal. The running variable is vote share for the CSR proposal centered around the relevant passage threshold. The main coefficient is beta, which captures the discontinuous jump in supplier CSR when the customer barely passes rather than barely fails a CSR proposal.

Scandal mechanism model:

```text
ProductCSR_Supplier_{t+1}
=
alpha
+ beta1 ProductCSR_Customer_t x Event_t
+ beta2 ProductCSR_Customer_t
+ beta3 Event_t
+ Controls_t
+ Fixed Effects
+ epsilon_{t+1}
```

The main coefficient is beta1. It measures whether customer product responsibility matters more for supplier product responsibility during major product-safety scandal years.

Performance model:

```text
Performance_{Supplier or Customer,t+1}
=
alpha
+ beta1 CSR_Customer_{t-1} x CSR_Supplier_t
+ beta2 CSR_Customer_{t-1}
+ beta3 CSR_Supplier_t
+ Controls_t
+ Fixed Effects
+ epsilon_{t+1}
```

The main coefficient is beta1. For SG&A, a negative beta1 means collaborative CSR improves operating efficiency. For future sales growth and market-to-book, a positive beta1 means collaborative CSR improves growth or valuation.

## 9. Contribution to the Literature
This paper contributes to:
1. [[Corporate Social Responsibility]] by showing that CSR is shaped by economically linked stakeholders, not only by managers, investors, regulators, or peers.
2. [[Supply Chains]] by showing that nonfinancial corporate policies can propagate through production networks.
3. [[Stakeholder Governance]] by showing that customers discipline suppliers through reputational and relational channels.
4. [[ESG and Firm Value]] by linking supply-chain CSR alignment to operating efficiency, valuation, and sales growth.

It differs from prior work because it studies voluntary CSR propagation through customer-supplier relationships and uses quasi-random CSR shareholder votes plus product-safety scandals, rather than only studying regulation, disclosure mandates, or firm-level CSR choices.

## 10. Closely Related Papers
- [[Flammer 2015]]: Close-call CSR proposal RDD and the value implications of CSR.
- [[Dyck et al. 2019]]: Institutional investors and CSR around the world.
- [[Liang and Renneboog 2017]]: Country institutions, legal origins, and CSR.
- [[Cao et al. 2019]]: Peer effects and CSR through product-market connections.
- [[Barrot and Sauvagnat 2016]]: Shock propagation through production networks.
- [[Masulis and Reza 2015]]: CSR as potential agency problem through corporate philanthropy.
- [[Cen et al. 2017]]: Spillovers of corporate policies through supply chains.

## 11. How This Paper Could Appear on Comps
Possible exam question:

> Review the main findings of the literature on CSR propagation and stakeholder governance. Discuss the data used and how the papers establish causality.

How to use this paper:
- Main finding: CSR propagates from customers to suppliers, but not from suppliers to customers.
- Data: Global FactSet Revere customer-supplier links merged with ASSET4 ESG ratings from 2003 to 2015.
- Identification: Close-call customer CSR proposal RDD and product-safety scandal shocks.
- Limitation: Customer-supplier matching and broad industry shocks may still complicate interpretation outside the RDD.
- Connection to other papers: Links [[CSR]], [[Stakeholder Governance]], [[Supply Chains]], and [[Production Networks]].
- Best exam phrase: "Dai, Liang, and Ng show that customers are a disciplining stakeholder in global supply chains: CSR flows from customers to suppliers, not the other way around."

## 12. Hypotheses Inspired by This Paper
H1: Suppliers improve CSR more after their largest customers experience negative ESG news than after unrelated industry ESG news.

H2: Customer-to-supplier CSR propagation is stronger when suppliers are financially dependent on the customer and weaker when suppliers have high relationship-specific investment.

H3: CSR propagation is stronger when customer and supplier share institutional owners, board members, or operate in countries with similar CSR norms.

## 13. Possible Extension or Research Design
- Research question: Do sanctions, geopolitical shocks, or forced-sourcing disruptions weaken customer-driven ESG discipline in global supply chains?
- Hypothesis: When customers lose supplier choice after a geopolitical shock, customer-to-supplier CSR propagation weakens because customers have less credible threat of exit.
- Data: FactSet Revere or Orbis supply-chain links, ESG ratings, sanctions exposure, supplier country risk, firm financials.
- Identification: Difference in differences around Russia sanctions or other geopolitical shocks comparing exposed customer-supplier links to similar unexposed links.
- Expected result: Customer CSR has a weaker effect on supplier CSR when supply-chain substitution is costly or politically constrained.
- Contribution: Extends Dai, Liang, and Ng by showing when stakeholder discipline breaks down due to supply-chain frictions.

## 14. Critiques

### Major Concern 1
The baseline panel relation may reflect endogenous matching. High-CSR customers may choose suppliers already likely to improve CSR. The RDD helps address this, but the baseline economic magnitude still partly reflects equilibrium sorting.

### Major Concern 2
CSR ratings are noisy and partly based on disclosure. If customers pressure suppliers to disclose more rather than actually behave better, measured CSR improvement may overstate real CSR improvement. The product-safety and RepRisk tests help, but this concern remains.

### Minor Concern
The global setting is broad, which improves external validity but makes mechanisms harder to isolate. Country institutions, industry norms, and customer power may vary substantially across pairs.

### Referee Recommendation
R&R leaning accept, because the paper asks an important question, uses unique supply-chain and ESG data, and has multiple identification strategies. The main remaining concern is whether measured CSR improvements represent real operational changes rather than disclosure or selection.

## 15. Memory Hooks
- "CSR flows downstream": customers influence suppliers, not vice versa.
- "Customer as stakeholder": customers are not just buyers, they govern supplier behavior.
- "Close-call CSR votes": narrow passage at customer firms moves supplier CSR.
- "Milk and airbags": scandals make customer pressure stronger.
- "BMW supplier map": Revere lets them observe global supply-chain links.

## 16. Comps Use Rating
| Category | Rating |
|---|---|
| Must memorize? | Yes |
| Identification importance | High |
| Good for synthesis? | High |
| Good for research design question? | High |
| Good for critique/referee question? | High |

## 17. Comps Use
Deploy this paper when asked about [[Corporate Social Responsibility]], [[Supply Chains]], [[Stakeholder Governance]], [[ESG and Firm Value]], or [[Regression Discontinuity]]. The clean exam answer is: "Dai, Liang, and Ng use global customer-supplier links from FactSet Revere merged with ASSET4 ESG ratings and show that CSR propagates from customers to suppliers, but not from suppliers to customers." Use it to argue that stakeholders can discipline firms through product-market relationships, not just through capital markets or regulation. In a critique answer, emphasize endogenous customer-supplier matching and noisy ESG measurement, but note that the paper is stronger than a standard correlation because it uses close-call CSR proposal votes and product-safety scandals as quasi-exogenous variation.