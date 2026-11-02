# Independent delta review: heavy-port closure

**Outcome: PASS under the declared actual-graph imports after one minor heading clarification. Same-family/provisional.** No gap affects the stated bounds or the multigraph necessary condition.

Input: `proofs/dd82/n62/CONNECTED_REPEAT_HEAVY_PORT_CLOSURE.md`, read in full on 2026-10-11. Reviewer: `/root/proof_review_n62_sixth_trace`. This independently checks the new root-conceived paper in the reviewer's reused context; it is not a new fresh-context review round. The earlier sixth-trace and short-component receipts are preserved separately.

## Obligations checked

| ID | Obligation | Finding |
|---|---|---|
| HP01 | Count heavy unit incidences | Every heavy endpoint has precisely one unit mate, and the declared D1 light-mate theorem puts that mate in W. Thus ∑wℓ(w)=2d. Symmetry and row sum three give 0≤ℓ(w)≤3, and each W3 row is exhausted by three distinct unit edges to D. |
| HP02 | Equality yields a closed set | If 3L3=2d, nonnegativity forces ℓ(w)=0 outside W3. Therefore every heavy endpoint's unit mate lies in W3. Both positive repeat neighbors of each heavy vertex lie in Z=D∪W3, while every positive neighbor of a W3 vertex lies in D. No positive repeat edge leaves Z. |
| HP03 | The closed set is nonempty and proper | d∈{1,3,5,7,9} gives D nonempty and |S|=3d>0. D is disjoint from S and W3⊆W is disjoint from S, so Z is proper. Connected repeat support therefore contradicts equality. Integer strictness gives L3≤floor((2d−1)/3). |
| HP04 | Mixed-trace substitution and d=9 | Substitution into τ≤248−24d+2L3 gives 224,178,134,88,42 for d=1,3,5,7,9. At d=9, τ=10c5−24976 and 0≤τ≤42 give 2498≤c5≤2501, with τ restricted to 4,14,24,34. No type-one triangle statistic occurs in the proof. |
| HP05 | Multigraph definition and degree | One multigraph edge per heavy pair joins its two distinct unit mates. Their distinctness is exactly the D1 hard-branch theorem, so there are no loops. Parallel edges remain allowed. Degree at w counts heavy endpoints whose unit mate is w, so it equals ℓ(w), between one and three on the chosen vertex set. |
| HP06 | No cubic multigraph component | For a cubic component, take its light-mate vertices and the heavy endpoints of its edges. Every heavy pair and all incident unit mates are included; cubic degree exhausts each chosen light-mate repeat row. This is again a nonempty closed set disjoint from S, contradicting connectedness. Hence each component has a degree-one or degree-two vertex. |

All six mathematical obligations close. Only finite exact row-counting and integer substitutions are involved; no probabilistic, limiting, asymptotic, or analytic interchange occurs. No new computation or search is needed.

## Imports and counterexample checks

The required actual-graph imports are the D1 complete heavy rows, light mates outside D∪S, disjoint generated triangles with |S|=3d, connected positive repeat support, and the positive odd d range. These are the same declared reductions read in the earlier task. For the mixed-trace consequence, the exact identity and port upper bound are imported from `CONNECTED_REPEAT_MIXED_TRACE_AND_ROOT_PATTERNS.md`, already read in full in this reused context. No assertion that all repeat triangles are generated is used.

Potential failures were checked directly: d=0 would invalidate the nonempty/proper argument but is explicitly excluded; repeated light mates are allowed and handled by ℓ; parallel multigraph edges are allowed; and membership in W3 exhausts the row, so an uncounted exit from a supposedly saturated light mate is impossible. These checks expose no counterexample to the actual-graph claims.

## Minor wording issue corrected

**HP-W01 — MINOR, UNCLEAR, COSMETIC, scope wording; Section 3 heading.** “An equivalent multigraph restriction” could be read as claiming equivalence with the global strict inequality 3L3<2d. The no-cubic-component condition is stronger for arbitrary incidence multigraphs: K4 disjoint union K2 has d=7, L3=4, and 3L3=12<14=2d, while it has a cubic component. This abstract example is not an actual-graph counterexample; it only distinguishes the two formulations.

At the parent’s explicit instruction, Section 3 was retitled “A componentwise multigraph restriction.” The body proves the stronger necessary condition correctly and does not claim or use a reverse implication. This wording fix does not change any mathematical result.

The issue was reported before editing. Exactly that heading was changed; the rest of the source is unchanged, and the corrected heading was checked. The original and earlier delta receipts remain unchanged. Cross-family review and acceptance remain the parent's separate responsibility.
