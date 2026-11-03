---
type: paper
node_id: paper:przybocki2026_doubly_saturated_ramsey
title: "Doubly Saturated Ramsey Graphs: A Case Study in Computer-Assisted Mathematical Discovery"
authors: ["Benjamin Przybocki", "John Mackey", "Marijn J. H. Heule", "Bernardo Subercaseaux"]
year: 2026
venue: "arXiv preprint2604.21187"
external_ids:
  arxiv: null
  doi: null
  s2: null
tags: ["dd82", "construction"]
added: 2026-10-11T14:54:31Z
---

# Doubly Saturated Ramsey Graphs: A Case Study in Computer-Assisted Mathematical Discovery

## One-line thesis
Read1.2/3: infer a useful family from actual graphs, then dedicated search and a uniform rule. Original https://arxiv.org/abs/2604.21187 ; local literature/dd82/arxiv_2604.21187.pdf ; DD82 actions in CONSTRUCTION_CASE_STUDY_ACTIONS_20261011.md.

## Problem / Gap
A doubly saturated R(s,t)-good graph avoids an s-clique and a t-independent set, but every edge addition or deletion destroys that property. Beyond a few examples known since 1982, the existence of infinite families remained unresolved (§1.1).

## Method
Small SAT instances reveal candidate graphs, which motivate a restricted circulant search implemented by bespoke LLM-generated code. Rewriting isomorphic distance sets exposes a uniform construction; a mathematical proof is then developed and formalized in Lean. The SAT encoding uses O(n^4) clauses for double saturation, while the separate Ramsey-goodness constraints can still become large (§§1.2, 2–3).

## Key Results
- For every t ≥ 4, there is a doubly saturated R(4,t)-good graph on 6t − 11 vertices (Theorem 1, reported with a Lean formalization).
- The smallest doubly saturated R(3,7)-good and R(4,5)-good graphs have 20 and 19 vertices, respectively (§1.1).
- The paper also proves the general lower bound 2s + 2t − 7 on the order of a doubly saturated R(s,t)-good graph and reports diagonal examples for 3 ≤ s ≤ 20 (§§4–5).

## Assumptions
- Graphs are finite and simple; complete and empty graphs are excluded from the double-saturation definition.
- The proven infinite family has s = 4 and t ≥ 4. With m = t − 2 and n = 6m + 1, one circulant description uses distances {m} ∪ [2m + 1, 3m].
- Circulant symmetry is a construction choice suggested by actual examples, not a classification of all doubly saturated graphs.

## Limitations / Failure Modes
- This is a Ramsey construction, not a degree/diameter construction; its circulant family supplies no DD82 witness or bound.
- A 19-vertex SAT instance did not terminate after a day on one core, and larger direct encodings became unwieldy; these observations motivated a different search representation, not nonexistence claims (§3).
- Broad existence remains conjectural. The odd-t R(3,t) family is checked through t = 63 but not proved in the paper (§4.1). This enrichment did not rerun the authors' SAT or Lean artifacts.

## Reusable Ingredients
- Infer a tractable family from complete graph examples, then test it with an implementation matched to that representation.
- Normalize isomorphic descriptions before looking for a general rule; additive structure of the distance sets exposed the eventual family (§3).
- Keep experimental instances, a general conjecture, its mathematical proof and formal verification as distinct stages (§1.2).

## Open Questions
- Does a doubly saturated R(s,t)-good graph exist for every 3 ≤ s ≤ t except (3,4) and (3,6), as Conjecture 1 proposes?
- Does the odd-t circulant R(3,t) construction hold for every odd t ≥ 17, beyond the finite checks of Conjecture 2?

## Claims
_No claims tracked yet — populate via /proof-checker._

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

## Relevance to This Project
For DD82, reuse the sequence “actual graphs → justified representation → bounded computation → general rule and proof,” rather than importing circulant symmetry merely because it succeeded here. The [project case-study note](../../proofs/dd82/construction/CONSTRUCTION_CASE_STUDY_ACTIONS_20261011.md) records the separate DD82 application; its HS obstruction must not be attributed to this Ramsey paper. Source used for enrichment: [local primary text](../../literature/dd82/arxiv_2604.21187.txt), §§1.1–1.2, 3 and 4.
