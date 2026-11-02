# D0_EDGE_BIN saturated-row proof review

Verdict: **PASS**, with `review_independence: same-family` and `acceptance_status: provisional`. The proof excludes actual graphs realizing D0_EDGE_BIN. No mathematical gap or counterexample was found; all obligations below are discharged. This is a paper proof judgment, not a Lean result or a whole-order-62 exclusion.

Reviewed on 2026-10-11 by fresh reviewer task `/root/proof_review_n62_bin`. Requested configuration: `gpt-6-astra`, reasoning `ultra`. The backend's actual model and reasoning effort were not independently exposed to this reviewer; the request is not reported as backend attestation. No prior review verdict was used as evidence.

The applied skill is `.agents/skills/proof-checker/SKILL.md`. This bounded task overrides its default output locations and TeX/PDF/HTML, wiki, and artifact-fingerprinting steps: only Markdown/JSON review files are written in this review directory. No source, formal, archive, or wiki files were changed. No SAT solver or additional agent was launched.

## Reviewed input and source alignment

The complete target is `proofs/dd82/n62/D0_EDGE_BIN_SATURATED_ROW_EXCLUSION.md`, lines 1–79. Its actual-graph premises were checked against `proofs/dd82/n62/RECOVERED_REDUCTION.md`, Step 1 (lines 42–52) and the double-branch derivation in Step 6 (lines 205–235), and the original `D0_EDGE_BIN` object in `context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/theory/n62/n62_root_templates.json`.

The original object sets root 0, `root_neighbors=[1,...,8]`, `H_edges=[]`, w=9 with parents 123, and a=10 with parents 45. Every other Y vertex has a singleton parent set. Its `fixed_B` is exactly `[[0,9,2],[0,10,1],[4,9,1]]`; `fixed_extra_edges=[[9,10]]`; and `w_single_repeat_neighbor_in_X=4`. Therefore the complete rows B₀=2e_w+e_a and B_w=2e₀+e_b used in the proof agree with the original template after row saturation, and a is adjacent to b=4. The JSON's `global_B_mode="0/1/2"` is stronger than what this argument needs and is not used.

The recovered reduction derives the inside/outside choice from actual graphs: w has five neighbors outside S=123. When a is among them, their parent incidences total six over R=45678. Every R label must occur, and the remaining repeat weight of w is one, so it identifies a unique extra label b. The BIN branch is precisely b in P(a). Swapping parent labels 4 and 5 and transporting all vertex labels makes b=4; this is a relabeling, not an automorphism assumption.

An exact read-only JSON check independently confirmed these fields, all singleton parent sets, and the resulting X entries of row 1: `(B₁₂,B₁₃,B₁₄,B₁₅,B₁₆,B₁₇,B₁₈)=(1,1,0,0,0,0,0)`. This check aligns the inputs; the mathematical derivations below establish the contradiction.

## Complete derivation check

1. **Actual matrix identities.** A finite simple undirected graph on 62 vertices with maximum degree at most 8 and diameter at most 2 is 8-regular: a vertex of degree at most 7 reaches at most 1+7+7·7=57 vertices in distance at most 2. For B=A²+A−7I−J, its diagonal is 8−7−1=0, its row sum is 64+8−7−62=3, and its off-diagonal entries are nonnegative integers because every nonadjacent pair has a common neighbor. Symmetry is inherited from A. Regularity gives AJ=JA and hence AB=BA. For distinct u,v, B_uv equals the common-neighbor count plus A_uv−1. These are sufficient matrix foundations; no triple-repeat exclusion is imported.

2. **The two original saturated rows.** Since X is independent, B₀x=0 for x in X. For y in Y, B₀y=|P(y)|−1. Thus the parent sets give B₀=2e_w+e_a. Symmetry gives B_w0=2, and the BIN template gives B_wb=1. Nonnegative row sum 3 leaves no other positive entry in row w. Also b in P(a) gives A_ab=1.

3. **The further endpoint c really lies in Y.** Put i=1,j=2,k=3. For distinct p,q in X, their common neighbors are root 0 and exactly those Y vertices whose parent sets contain p,q; no common neighbor lies in X. Hence B_ij=B_ik=1 and B_ix=0 for x in X outside {j,k}, including the zero diagonal. Also B_i0=0 because 0,i have no common neighbor when X is independent. The residual row weight is exactly one. Nonnegative integrality supplies one unique endpoint c with B_ic=1; it cannot be a repeated contribution at j or k because their entries are already exactly one. Therefore c is in Y. Since row w vanishes at i, symmetry gives B_iw=0, so c≠w. This establishes B_i=e_j+e_k+e_c without assuming B globally simple.

4. **Entry (i,w).** Symmetry of B permits using its complete w row as its w column. Thus `(AB)_iw=2A_i0+A_ib=2`, because A_i0=1 and i,b are distinct members of independent X. The complete i row gives `(BA)_iw=A_jw+A_kw+A_cw=2+A_cw`, since j,k are parents of w. Commutation yields A_cw=0; symmetry of A also gives A_wc=0.

5. **Entry (0,c).** The i summand is A₀i B_ic=1, and every other summand is nonnegative, so `(AB)_0c≥1`. The root row gives `(BA)_0c=2A_wc+A_ac=A_ac`. Commutation and A_ac in {0,1} force A_ac=1. In particular c≠a because A_aa=0. No equality of the left side was assumed prematurely.

6. **Entry (c,w).** Since c lies in Y, A_c0=0. The w column therefore gives `(AB)_cw=2A_c0+A_cb=A_cb`. The i summand of the opposite product is B_ci A_iw=1: B_ci=B_ic=1 by symmetry and i is a parent of w. All other terms are nonnegative, so commutation forces A_cb≥1, hence A_cb=1.

7. **The triangle produces a repeat weight.** Vertices a,c lie in Y, b lies in X, and c≠a; all three are distinct. The edges ab,ac,bc just proved form a genuine triangle. Consequently a is a common neighbor of b,c. Since bc is an edge, the actual identity gives B_bc=(A²)_bc≥1. Neither a global bound B≤1 nor the at-most-one-triangle bound is needed here.

8. **The final sum has two distinct terms.** Indices i=1 and b=4 are distinct, and both are neighbors of 0. Thus `(AB)_0c≥A₀i B_ic+A₀b B_bc≥1+1=2`. Its commuting partner remains `(BA)_0c=2A_wc+A_ac=1`. This is the required contradiction 2≤1. Symmetry, nonnegativity and the distinct indices discharge every inequality hypothesis.

## Counterexample attempts and boundary checks

| Attempt | Resolution |
|---|---|
| Put the residual repeat weight at j or k again | Their exact parent-based entries are already one; this would change a fixed entry. |
| Split the residual weight between several endpoints | Nonnegative integral entries with total one cannot split. |
| Take c=0, c in X, or c=w | Excluded by B_i0=0, the complete X entries, or symmetry with the saturated w row. |
| Take c=a | The (0,c) equality would force the forbidden diagonal A_aa=1. Equivalently the earlier A_cw=0 conflicts with the template edge aw. |
| Make the final two summands the same summand | i in 123 and b in 45 ensure i≠b. |
| Permit repeat weights two or three elsewhere | Such weights never appear with a negative coefficient; every lower bound remains valid. |
| Replace BIN by BOUT | Then b is outside P(a), so A_ab=1 is unavailable. This proof does not close BOUT. |

These are direct algebraic attempts, not a numerical graph search. No candidate survives the actual hypotheses. An unsuccessful attempt alone is not used to discharge an obligation; the explicit derivations do so.

## Acceptance and limits

There are zero FATAL, CRITICAL, MAJOR or MINOR issues and no source fixes. The dependency graph in `PROOF_SKELETON.md` is acyclic. Every product is a finite sum; there are no limits, derivatives, integrals, probability modes or asymptotic constants to audit. The canonical theorem matches the conclusion exactly: no actual graph realizes this one branch.

The proof's opening triangle bound is correct but is not needed once the template rows are available. The description of N(i) is also correct but is not subsequently used. Neither observation calls for an edit.

The review makes no claim about other branch contradictions, complete order-62 nonexistence, or the final degree–diameter value. Global seven-template coverage and the triple-edge enumeration are not re-certified by this bounded audit; the contradiction for this branch does not depend on them. Semantic acceptance remains same-family/provisional until separately assessed by an appropriate cross-family review.
