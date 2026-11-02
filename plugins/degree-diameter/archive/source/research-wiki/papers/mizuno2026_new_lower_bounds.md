---
type: paper
node_id: paper:mizuno2026_new_lower_bounds
title: "New lower bounds for the degree/diameter problem via interaction with a browser-accessible LLM"
authors: ["Ryosuke Mizuno"]
year: 2026
venue: "arXiv preprint2606.15860"
external_ids:
  arxiv: null
  doi: null
  s2: null
tags: ["dd82", "construction"]
added: 2026-10-11T14:54:31Z
---

# New lower bounds for the degree/diameter problem via interaction with a browser-accessible LLM

## One-line thesis
Read2.2/4/5/appendix: separate route coverage and fiber coverage, redesign stalled components. Exact NB2 controller impossible for simple graphs, so diameter5 scheme cannot directly transfer. Original https://arxiv.org/abs/2606.15860 ; local literature/dd82/arxiv_2606.15860.pdf.

## Problem / Gap
Most degree/diameter parameters still lack exact values. This case study seeks explicit graphs improving recorded lower bounds, while examining what a browser-accessible LLM can achieve under human direction without a preinstalled research orchestration system (§§1–2).

## Method
The route-chart lift separates two obligations: a small controller must connect every ordered pair by a nonbacktracking walk of exactly five steps, and every reduced five-symbol route must give an invertible fiber controllability matrix. A 144-vertex, 4-regular controller is constructed from a six-vertex multibase with C4 × C6 voltages; affine charts over F3^5 and F4^5 then expand each controller route into coverage of a whole fiber. The appendix supplies explicit data and finite verification conditions (§2.3, §4, Appendix A).

## Key Results
- N(12,5) ≥ 34,992, improving the paper's recorded baseline 29,621 by 5,371 (18.13%).
- N(16,5) ≥ 147,456, improving its recorded baseline 132,496 by 14,960 (11.29%).
- Both constructed graphs have diameter exactly 5; their orders exceed the corresponding diameter-4 Moore bounds (§2.2, Theorem A.12).

## Assumptions
- The lift theorem requires a simple regular controller with the exact-NB-s property for every ordered vertex pair, including equal endpoints.
- Edge labels must be inverse-consistent, and the affine chart must satisfy the inverse-symbol identities and nonsingularity conditions for every reduced word of length s.
- The concrete results use s = 5 and finite fields of orders 3 and 4; the transcript discussion concerns one visible research dialogue.

## Limitations / Failure Modes
- The paper does not construct a degree-8, diameter-2 graph or determine N(8,2). Successful fiber charts alone did not resolve the controller bottleneck in several attempted parameter ranges (§4.4–4.6).
- Directly setting s = 2 cannot work with a nonempty simple controller: every two-step closed walk immediately backtracks. This transfer obstruction is the project's own argument in [the case-study note](../../proofs/dd82/construction/CONSTRUCTION_CASE_STUDY_ACTIONS_20261011.md), not a theorem attributed to Mizuno.
- The process analysis is observational and explicitly does not establish causal benefits of individual interventions (§5); this enrichment did not rerun the paper's verification package.

## Reusable Ingredients
- Separate coarse routing from within-fiber coverage and state the precise joint obligations before implementing a large graph.
- Replace stalled local repair with a redesigned controller or representation, supported by an a priori coverage reason (§4.6).
- Preserve explicit construction data and verify the finite conditions that connect the compact representation to the full graph (Appendix A.8).

## Open Questions
- Can a diameter-2 construction use a different same-fiber coverage rule that avoids the exact-NB-2 obstruction? This is a DD82 transfer question, not a result of the paper.
- Which other parameter pairs admit compatible controller and universal-chart data after the bottlenecks recorded in §4.6?

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
The transferable ingredient is a verifiable construction mechanism and an explicit decision to redesign a blocked component, not the paper's diameter-5 formulas. The [DD82 case-study note](../../proofs/dd82/construction/CONSTRUCTION_CASE_STUDY_ACTIONS_20261011.md) applies that lesson to coverage obligations and an induced-HS obstruction; that obstruction is project work, and neither reading this paper nor closing that family settles the open orders 58–61. Source used for enrichment: [local primary text](../../literature/dd82/arxiv_2606.15860.txt), §§2.2–2.3, 4–5 and Appendix A.7–A.8.
