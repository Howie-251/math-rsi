# Order61 component proofs: fresh proof audit

**Verdict: WARN — one minor status-wording inconsistency; no mathematical gap found in the checked claims.** Base review is **same-family / provisional**. This is one fresh Codex review, not an external acceptance or a whole-order61 exclusion.

Reviewer: `/root/n61_components_proof_check`, `gpt-6-astra`, reasoning `ultra`. Completed 2026-10-13T10:52:09Z. Read-only obligation shard: `/root/n61_components_proof_check/exact_computation_obligations`; it inspected the finite computation sources/results and did not execute code or give an overall verdict. No earlier reviewer verdict was supplied or consulted.

Applied the project-local proof-checker skill with the V3 DD82 adaptation. No proof edits, scores, rendering, Lean, external backend, wiki changes, historical62–65 review, or benchmark repetition were performed. Root owns any subsequent external discussion and wiki claim status.

## Inputs and exact scope

Read directly and completely:

- `proofs/dd82/n61/GENERAL_THREE_DEFECT_COMPONENT_QUOTIENTS.md`, including section5, lines1–198.
- `proofs/dd82/n61/THREE_COMPONENT_6_25_30_EXCLUSION.md`, lines1–234.
- `computations/dd82/n61/component_quotient_three.py` and its `.result.json`.
- `computations/dd82/n61/component_6_25_30_resonance.py` and its `.result.json`.

Instructions read: `AGENTS.md`, `.agents/skills/proof-checker/SKILL.md`, and `context/dd82/DD82_V3_ARIS_GEMINI_PLAN_20261013.md`.

The checked object is every finite mathematical claim in the two new proofs: the actual weighted-defect quotient reduction; its complete three-component table; its shared-block lifting equivalence; the four necessary R cycle types for `(12,21,28)`; and the exclusion of `(6,25,30)`. The historical CP02 paragraph was read as context; its archived factual claims were not recertified and are not dependencies of these arguments. No claim about existence or nonexistence of an arbitrary graph of order58–61 follows from this audit.

## Issue

**I1 — MINOR / UNCLEAR / COSMETIC / SCOPE_OVERCLAIM (status wording).** Location: `GENERAL_THREE_DEFECT_COMPONENT_QUOTIENTS.md:20–25`, especially “Both remain unlifted and unexcluded.” The present-tense overview is stale relative to the companion exclusion and the later link at line188. The necessary-quotient classification remains correct; neither mathematical dependency chain is affected. No counterexample is involved. Minimal fix: label this sentence as the state immediately after the initial enumeration, then state that the companion draft excludes `(6,25,30)` subject to its review status, while `(12,21,28)` remains open. **Open; reviewer did not modify either proof.**

There are no FATAL, CRITICAL or MAJOR issues.

## Quantified claims and hypothesis discharge

Throughout, G is finite, simple, undirected, has61 vertices, maximum degree at most8 and diameter at most2; A is its one actual adjacency matrix. B means only `A²+A−7I−J`, a symmetric nonnegative integral matrix with zero diagonal and row sum4. Components refer to positive support. Sizes n_i are positive integers; Q is the corresponding integral adjacency quotient. S,T,R are actual symmetric binary diagonal adjacency blocks; X,Y are their actual binary incidence blocks. In the Fourier argument vectors may be complex, but every Y entry is real and binary.

| ID | Quantified claim / location | Checked application and conclusion |
|---|---|---|
| Q1 | General §2, lines54–64: every such G is eight-regular and has the stated B. | A degree-at-most7 vertex reaches at most `1+7+7·7=57<61`; hence degree8, 244 edges, diagonal B=0, off-diagonal B≥0 and row sum4. Regularity discharges AJ=JA and thus AB=BA. |
| Q2 | General §2, lines66–86: every actual support partition is equitable and obeys (1),(2). | Weighted maximum propagation identifies the real B-eigenspace at4 with the component indicators, including a two-vertex component with edge weight4. Commutation gives invariance; neighbor counts give integral Q, row sum8 and balance `n_i q_ij=n_j q_ji`. Restricting the same matrix identity gives `Q²+Q−11I=1nᵀ`. |
| Q3 | General §2, lines88–99: c is odd and at most17. | `D^(1/2)QD^(−1/2)` is symmetric for D=diag(n). Balance also gives `nᵀQ=8nᵀ`, so n-perpendicular is invariant. Connectedness of G makes eigenvalue8 simple. All remaining eigenvalues are the two roots of `x²+x−11`; irreducibility over Q forces equal multiplicities m. Thus `c=2m+1`, trace `8−m≥0`, and m≤8, including c=1. |
| Q4 | General §3: every c=3 target gives one of exactly two quotient pairs, up to simultaneous permutation. | All45 row compositions are present, so the labeled domain has91,125 elements. Every filter is necessary, all arithmetic exact, and both sizes and quotient are permuted together. Independent recomputation confirms counts91,125/9,108/72/12/12 and precisely the12 stated labeled pairs. This is necessary classification, not a realization claim. |
| Q5 | General §4: the stated shared-block system is necessary and sufficient for an actual graph with that component partition. | Multiplication of the displayed A gives all three off-diagonal equations and all three diagonal B formulas. Prescribed degrees ensure diagonal0 and row sum4. Nonnegative defects give an edge or common neighbor for every pair; connected support of each B_i gives exactly those three components. Every block is retained from the same A in both directions. |
| Q6 | General §5: every target of type `(12,21,28)` has exactly one of the four listed R cycle partitions. | S is a six-edge matching, hence S²=I. For every R cycle, `(S+3I)r=q1` has the unique solution `(q/4)1`, so4 divides q. The space E has dimension5. Nonnegative symmetric row-four B_1 has spectrum in [−4,4], so on E, `vᵀXXᵀv=vᵀ(B_1+5I)v≥||v||²`. This makes Xᵀ injective. The transposed actual block equation sends its image into R's eigenvalue−2 space. Each even cycle contributes dimension1. Thus at least five cycles; partitions of28 into at least five positive multiples of4 give exactly the four stated types. No B_1–S commutation is needed. |
| E1 | Exclusion §§1–2, lines32–88: its cubic-six block must be the complement of C6. | Column sum1 and binary X give XXᵀ=5I. A cubic-six complement is either C6 or2C3. For K3,3 the actual B_1 is two disjoint weight-two triangles, violating the explicitly assumed component connectivity. The remaining labeling is legitimate because arbitrary vertex relabeling preserves all matrix identities. |
| E2 | Exclusion §2, lines90–107: R covers C6 and all its cycle lengths divide into multiples of6. | Each column has exactly one fiber label and each label has five preimages. Entrywise use of SX+XR+X=J gives exactly one R neighbor over each of the two base neighbors. Nonbacktracking traversal therefore consistently follows one cyclic direction in C6; closing a component requires6 to divide its length. |
| E3 | Exclusion §3: R=C30 and every T cycle has length in `{5,10,15,20,25}`. | For every actual T/R cycle pair its Y block satisfies the restricted equation. Both shifted cycle matrices have spectrum in [1,5] and row sum5. The unique block row/column counts are q/5 and p/5, which are integers. Thus5 divides each cycle length; combining with E2 and total30 forces R=C30. No cycle pair or partition is omitted. |
| E4 | Exclusion §4: every row of Y is a sum of period5 and period6 functions. | The recurrence yields the cycle characteristic polynomial for p≥3 with the correct endpoint/interior multiplicities. All five rational GCDs were independently recomputed from explicit cycle adjacency matrices. For every nonconstant C30 Fourier vector, Jv=0; the block equation gives `(C_p+(1+mu)I)Zv=0`. The GCDs exhaust all resonances. The possible Fourier orders are exactly5,6,3; order3 is included in period6, and constants can be included in either summand. The full Fourier basis discharges the passage from vanished forbidden modes to row decomposition. |
| E5 | Exclusion §5, lines203–220: any binary additive row has period5 or6, and weight6 leaves five possibilities. | CRT is bijective because gcd(5,6)=1. A nonzero difference of two a-values equals the same binary difference at every b-index, so it is ±1 and forces b constant. The reasoning holds over C as stated. Period6 weight is divisible by5, excluding weight6. Period5 repeats six times and therefore has exactly one occupied residue. |
| E6 | Exclusion §5, lines222–230: no target with the stated quotient exists. | Two identical Y rows imply at least six common neighbors, hence actual B_uv≥5. Nonnegativity of every entry and row sum4 imply B_uv≤4. The contradiction makes all25 rows distinct, incompatible with E5's five possibilities. No assumption of binary B, group action or historical CP02 condition enters. |

Dependency trace: Q1 → Q2 → Q3 → Q4 → Q5 → Q6; Q1,Q5 → E1 → E2; Q5,E2 → E3 → E4 → E5; Q1,E5 → E6. The companion links are navigational, not circular dependencies. The exclusion can start directly from its stated actual quotient without using Q4's enumeration.

All inequalities have the required directions and hypotheses: the degree57 bound is an upper bound; the B_1 spectrum bound uses symmetry and entrywise nonnegativity; `B_1+5I` is positive definite with lower bound I; the final B_uv lower bound contradicts the nonnegative row budget. There are no limits, interchanges, probabilities, asymptotics, uniformity claims or hidden limiting constants to audit.

## Counterexample checks

- Weighted and minimal support: `[[0,4],[4,0]]` has eigenvalues±4. It confirms the lower bound used in Q6 can be sharp and that a binary-defect assumption cannot be inserted; adding5I still gives the required positive lower bound.
- Cubic-six alternative: K3,3 explicitly gives the disconnected `2 A(2K3)`, so the connectivity hypothesis at E1 is both present and necessary for that step.
- Shared-block equations alone are insufficient, as the proofs require: take S=complement(C6), T=C25, R=C30, `X_(a,z)=1[z=a mod6]`, and `Y_(t,z)=1[z=2t mod5]`. CRT and the five residues `2t,2t±1,2t±2` verify the degrees and all three cross equations. Y has repeated rows, and the actual B_2 has value5 at difference5 but value−1 at difference3. Thus it fails exactly the actual nonnegative-defect hypothesis and is not a counterexample to the stated theorem.
- Complex additive cancellation does not evade E5: all a-differences are differences of actual binary values, so every nonzero such difference is real±1 and forces b constant.

No counterexample to a claim with all its stated hypotheses was found. These checks clarify necessary assumptions; their failure to refute the proofs is not itself used as proof.

## Exact check and trace

One independent exact-algebra run: `python3 reviews/dd82/proof-checker-n61-components-20261013/trace/independent_exact_check.py`, exit0, observed wall time0.42951316 seconds. It uses explicit cycle adjacency characteristic polynomials instead of the submitted recurrence, and trace-first diagonal enumeration instead of the submitted row-product iteration. It checks the five GCDs, all saved polynomial/cofactor coefficients, every surviving quotient and its permutation orbit. No graph realization search or solver was run, and neither submitted computation nor its result was overwritten.

The script and full output are retained in `trace/independent_exact_check.py` and `trace/independent_exact_check.result.json`. The source-inspection shard separately checked exact Fraction arithmetic, all loop domains and filters; its independent hand calculation gives the trace-seven count9,108. This audit records the semantic review and all real issues; `PROOF_AUDIT.json` records the structured scope and reviewer identifiers.

The accepted local mathematical content remains provisional pending the root's actual external review. `(12,21,28)` realization, c=1, and c=5,7,…,17 remain open in these inputs. No complete graph of order58–61 or whole-order exclusion was produced by this review.
