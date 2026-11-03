# Delta review: a direct S_TOUCH contradiction

**Verdict: PASS for the new mathematical argument, same-family/provisional.** No proof defect was found. This separately reviews the short argument sent by the parent after the three-case coverage audit was complete. It does not rewrite the scope or historical verdict of `PROOF_AUDIT.md`.

- Date: 2026-10-11.
- Reviewer task: `/root/proof_review_s_touch_three`.
- Requested route: `gpt-6-astra`, effort `ultra`, backend `codex`.
- Actual model, effort, and backend: **notattested**.
- Input: the parent's proposed short proof, the original S_TOUCH template, and the exact original-graph identities checked in the preceding audit.
- Claim: no actual order-62 candidate can satisfy S_TOUCH.
- No SAT computation, CNF correspondence, or Lean proof is used or claimed. This excludes one template, not all order-62 candidates.

## Explicit proof with all local counts

Assume an actual S_TOUCH candidate G. Write w=9. The exact repeat matrix B is nonnegative integral with zero diagonal and row sum 3, and AB=BA. Every vertex is on at most one triangle. The fixed original neighborhoods are

`N_G(0)={1,…,8}, N_G(1)={0,2,w}∪C1, N_G(2)={0,1}∪C2, N_G(3)={0,w}∪C3.`

The only edge within X={1,…,8} is 12, and w has precisely parents 1 and 3.

The root triangle and the two parents of w give

`N_B(0)={1,2,w}, N_B(1)={0,2,3}.`

For the second identity, c(1,3)=2 with common neighbors exactly 0,w; this gives B13=1. Triangle edges give B10=B12=1, saturating row 1. The first identity similarly follows from B01=B02=B0w=1 and row sum 3.

**1. Locate the remaining repeat of vertex 2.** Triangle 012 gives B20=B21=1. For each x∈{3,…,8}, the only common neighbor of 2 and x is 0: vertex 1 is not adjacent to x, and every vertex of C2 has unique parent 2, so none is adjacent to x. The pair 2,x is nonadjacent, hence B2x=c(2,x)−1=0. The remaining row weight is exactly one, so there is a unique b∈Y with

`B2b=1, N_B(2)={0,1,b}.`

The word “unique” uses nonnegative integrality and residual weight one. It does not assume that an arbitrary cubic matrix has a prescribed support.

**2. Exclude C2 as the location of b.** If b∈C2, then 2 and b are adjacent, and B2b=1 forces a common neighbor. This gives a triangle containing 2 and b, distinct from 012 because b∈Y. That contradicts t(2)≤1. Equivalently, the already adjacent repeat entries B20=B21=1 exhaust the even sum 2t(2)≤3, so no further B-positive neighbor of 2 can be adjacent to 2.

**3. Apply commutation at (1,b).** Since 1 is adjacent to 2,

`(AB)1b ≥ B2b = 1,`

while the saturated row of B gives

`(BA)1b = A0b+A2b+A3b.`

If b=w, the right side equals 1, but the left side also contains B0w=1 because 1 is adjacent to 0. Thus `(AB)1w≥B2w+B0w=2`, a contradiction. Therefore b is an ordinary singleton-parent vertex.

For such b, A0b=0. The right side is 1 exactly when the parent of b is 2 or 3, and is 0 otherwise. It must be at least 1. Step 2 excludes C2, so

`b∈C3.`

**4. Apply commutation at (0,b).** The two saturated neighborhoods of 0 give

`Σ_{x=1}^8 Bxb = (AB)0b = (BA)0b = A1b+A2b+Awb = Awb,`

because b∈C3 has neither 1 nor 2 as a parent. The sum on the left contains B2b=1, so Awb=1. Then w,3,b form a triangle: w is adjacent to 3, b∈C3 is adjacent to 3, and w is adjacent to b. The pair 3,b is an edge with common neighbor w, so B3b=c(3,b)≥1. Returning to the same equation gives

`2 ≤ B2b+B3b ≤ Σ_{x=1}^8 Bxb = Awb = 1,`

a contradiction.

Thus an actual S_TOUCH candidate cannot exist.

## Delta obligations and adversarial checks

| ID | Obligation | Check |
|---|---|---|
| DX01 | Exact root and vertex-1 B rows | Three forced weight-one entries exhaust each row; c(1,3)=2 is fixed by parent sets. |
| DX02 | B2x=0 for x=3,…,8 | Intersect N_G(2)={0,1}∪C2 with each fixed parent neighborhood; the intersection is exactly {0}. |
| DX03 | Unique remaining B2 neighbor lies in Y | Root and X entries plus diagonal account for every other location; nonnegative integer residual weight is one. |
| DX04 | That neighbor is not in C2 | Otherwise B2b on an original edge supplies a second triangle at 2. |
| DX05 | It is not w | The (1,w) commutation equation would have two distinct summands B0w=B2w=1 on the left and exactly 1 on the right. |
| DX06 | The ordinary neighbor must lie in C3 | The (1,b) right side equals the indicator of the unique parent being 2 or 3; C2 was excluded. |
| DX07 | The (0,b) equation forces w adjacent to b | Its right side is the 0/1 entry Awb; the left side contains B2b=1. |
| DX08 | The same equation then contradicts itself | Triangle w3b gives the additional distinct nonnegative summand B3b≥1, so the left side is at least 2. |

All eight obligations are discharged. The argument is acyclic: DX01–DX04 precede the (1,b) localization, then the (0,b) forced edge precedes the final return to that same equality. Reusing an equality after deducing an additional lower bound is not circular reasoning.

Potential escapes were checked explicitly: b=0,1,2 or another root label is excluded before the split; b=w is handled separately because it has two parents; an ordinary b outside C2∪C3 makes the (1,b) right side zero; a C2 point creates a distinct triangle; a nonadjacent C3 point violates the first use of the root equation; an adjacent C3 point creates the extra B3b term and violates its second use. Unknown edges between other Y vertices can only add nonnegative terms to the displayed left sides and cannot repair the contradiction. Symmetry identifies B2b and Bb2, and the two decisive summands are indexed by different root neighbors 2 and 3.

Global simplicity of B is available in S_TOUCH but is not needed in this particular argument: exact triangle-edge weights and the row sums already force all saturated rows used. No broader theorem is asserted here. No candidate counterexample survived the algebraic case analysis, and no proof fix or additional hypothesis is required.

## Remaining scope

This delta establishes the paper-level contradiction for S_TOUCH under the actual graph assumptions. It does not close the other six templates, certify historical solver records, connect a CNF to graphs, or supply a Lean declaration. Cross-family semantic acceptance remains pending; this review is same-family and provisional.
