# Fresh review of the S_TOUCH three-case reduction

**Verdict: PASS for the stated conditional coverage theorem.** No FATAL, CRITICAL, MAJOR, or MINOR proof issue was found. This is a same-family, provisional semantic review, not a cross-family acceptance or a formal proof.

- Date: 2026-10-11.
- Reviewer task: `/root/proof_review_s_touch_three`.
- Requested reviewer route: `gpt-6-astra`, reasoning effort `ultra`, backend `codex`.
- Actual model, reasoning effort, and backend: **notattested**. No resolved backend metadata was supplied to this reviewer.
- Skill: project-local `.agents/skills/proof-checker/SKILL.md`. The caller limits artifacts to Markdown/JSON and overrides the skill's rendering and hash defaults.
- Reviewed source: `proofs/dd82/n62/S_TOUCH_THREE_CASE_REDUCTION.md`, lines 1–100.
- Dependencies read: `proofs/dd82/n62/RECOVERED_REDUCTION.md`, particularly Step 1 and the S_TOUCH part of Step 6; the S_TOUCH object in `context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/theory/n62/n62_root_templates.json`.

The conditional theorem starts with an actual order-62 graph **already in S_TOUCH**. This review does not re-audit the triple-edge finite enumeration or the seven-template coverage theorem. It does not recover historical eight-leaf assumptions, verify a CNF map or unit-clause file, run a solver, establish that any case exists, or exclude S_TOUCH or order 62. The final paragraph's future certificate instructions are not evidence used in this review.

## Quantified statement and assumptions

For every finite simple undirected graph G on vertices 0,…,61 with maximum degree at most 8 and diameter at most 2, if G is labeled according to the archived S_TOUCH template and its exact matrix B=A²+A−7I−J is simple, then there is a simultaneous relabeling of A and B preserving that template for which the full ninth rows have one of the following supports. All row entries outside the displayed supports are zero.

| Case | Full support of A[9,*] | Full support of B[9,*] |
|---|---|---|
| A | {1,3,21,27,34,41,48,55} | {0,3,21} |
| C2 | {1,3,27,28,34,41,48,55} | {0,4,15} |
| C3 | {1,3,27,28,34,41,48,55} | {0,4,21} |

The root is fixed as 0, w=9, X={1,…,8}, and Y={9,…,61}. Inside X the only edge is 12. The exceptional vertex w has parent set {1,3}; every other Y vertex has one parent. The classes C_i are disjoint sets of vertices with that unique parent. Their sizes are (5,6,6,7,7,7,7,7). These are explicit properties of S_TOUCH, not deductions from an arbitrary cubic B.

| Symbol | Type and meaning |
|---|---|
| A | Symmetric 62×62 zero-diagonal adjacency matrix with entries in {0,1} |
| B | Exact symmetric matrix A²+A−7I−J; in this template entries lie in {0,1}, diagonal zero, row sum 3 |
| c(x,y) | Nonnegative integer number of common G-neighbors of distinct x,y |
| t(x) | Nonnegative integer number of triangles containing x |
| n_i | Integer |N_G(w)∩C_i| |
| b | The unique remaining B-neighbor after 0 and the doubled-class parent in cases C2/C3 |

Regularity and the exact identities were independently checked from Step 1: a vertex of degree at most 7 sees at most 1+7+49=57 vertices, so every degree is 8. Hence B has row sum 64+8−7−62=3, zero diagonal, and nonnegative off-diagonal entries by diameter two. Since AJ=JA=8J, AB=BA. For x≠y, c(x,y)+A_xy=1+B_xy. Finally, 2t(x)=Σ_{y∈N_G(x)}B_xy≤3, so t(x)≤1. The assumption that B is simple is explicitly part of S_TOUCH; this review does not import the general triple-edge exclusion to obtain it.

## Dependency and proof-obligation ledger

The dependency graph is acyclic:

`original graph + S_TOUCH data → exact identities and known rows → saturated row 1 → forbidden B targets → six-neighbor split → exact B9 support → simultaneous canonical relabeling`.

| ID | Source location | Obligation and hypothesis discharge | Result |
|---|---|---|---|
| ST01 | lines 10–16 | The graph and template hypotheses give the partition, exact parent sets, cubic simple B, commutation, and the triangle bound; these agree with the JSON and the derivation above. | Discharged |
| ST02 | lines 31–35 | N_G(1)={0,2,w}∪C1. Vertices 0 and w are common neighbors of 1 and 3; 2 is not adjacent to 3, and no C1 vertex is adjacent to 3 by its singleton parent set. Thus c(1,3)=2 exactly and B13=1. The triangle gives B10=B12=1, saturating row 1. | Discharged |
| ST03 | lines 37–43 | With N_B(1)={0,2,3}, (BA)1w=A0w+A2w+A3w=1. Meanwhile (AB)1w=1+B2w+Σ_C1 Byw. Nonnegativity implies B2w=0 and Bwy=0 on C1. | Discharged |
| ST04 | lines 44–49 | For y∈C4∪…∪C8, (BA)1y=A0y+A2y+A3y=0 because y has its unique parent outside {2,3}. Every summand of (AB)1y is nonnegative, and the summand from w is Bwy. Thus Bwy=0. | Discharged |
| ST05 | lines 53–58 | w has degree 8 and exactly two parents, hence six Y-neighbors. A C1 neighbor would form triangle 1wy in addition to 012. For each x=4,…,8, every common neighbor of w and x is in Cx; diameter two therefore forces n_x≥1. | Discharged |
| ST06 | lines 60–63 | For the nonadjacent pair (w,2), the common neighbors are 1 and the selected C2 vertices. Thus c(w,2)=1+n2 and B_w2=n2. ST03 forces n2=0; the proposed sixth point in C2 is impossible. | Discharged |
| ST07 | lines 65–67 | If n3=1, the other five selected vertices occupy C4,…,C8 once each. The triangle w3a gives B_w3=B_wa=1. With B_w0=1 these exhaust the cubic B row, proving all zeros as well as all positives in case A. | Discharged |
| ST08 | lines 69–77 | Otherwise n3=0 and precisely one of C4,…,C8 has count 2. After moving that parent to 4, exact common counts determine B_wx for every x∈X. The remaining B-neighbor must lie in C2∪C3 by ST03–ST04. Both classes have n_i=0, so this neighbor is nonadjacent to w. | Discharged |
| ST09 | lines 24–27, 81–92 | Permutations of parent labels 4,…,8, transported to their equally sized singleton classes, preserve the template. Arbitrary bijections within classes then send the selected points to the stated labels. The shared A/B point in case A is moved once; in C2/C3 the B point lies in a class containing no selected A point. | Discharged |
| ST10 | lines 83–92 | The original JSON class labels match 21∈C3, 27,28∈C4, 34∈C5, 41∈C6, 48∈C7, 55∈C8, and 15∈C2. Adding fixed A-neighbors 1,3 and B-neighbor 0 gives exactly the three complete rows above. | Discharged |

No step uses a solver answer, a probabilistic transition, a limit interchange, asymptotic notation, or an untracked parameter. Those checklist categories do not apply.

## Exact common counts and exhaustiveness

Once the complete A-neighborhood of w is known, unknown edges between other Y vertices cannot change c(w,x) for x∈X: x's entire neighborhood is fixed by the root template. Directly,

`c(w,0)=2; c(w,1)=n1; c(w,2)=1+n2; c(w,3)=n3; c(w,x)=n_x for x=4,…,8.`

The adjacency correction in c(w,x)+A_wx=1+B_wx is essential at the parents 1 and 3. It yields B_w1=n1 and B_w3=n3, while B_w2=n2 and B_wx=n_x−1 for x=4,…,8. Thus the exact root-and-parent rows are:

| Case | c(w,x), ordered x=0,1,…,8 | B(w,x), ordered x=0,1,…,8 |
|---|---|---|
| A | (2,0,1,1,1,1,1,1,1) | (1,0,0,1,0,0,0,0,0) |
| C2/C3 | (2,0,1,0,2,1,1,1,1) | (1,0,0,0,1,0,0,0,0) |

Because n1=n2=0, n4,…,n8≥1, and Σ n_i=6, exactly six count profiles remain: one with n3=1, and five with n3=0 and a doubled class among C4,…,C8. The latter five form one orbit under the allowed parent permutations. Its remaining B point lies in C2 or C3, producing the stated two further cases. Case A and the other cases differ by n3; C2 and C3 differ by the parent of their remaining B point. This establishes coverage under relabeling, without claiming a partition of all labeled completions or an automorphism of a fixed G.

In case A, extend the assignment a↦21 to a permutation of C3 and send the five selected points to the first labels of their classes. This sends both the A and B occurrence of a to 21. In cases C2/C3, first send the doubled parent to 4 and transport whole classes; send its two distinct points to 27 and 28, the other selected points to 34,41,48,55, and b to 15 or 21. These assignments have disjoint domains apart from the deliberately shared point in case A, so they extend to a bijection of all vertices. Conjugating A and its polynomial B by this same permutation preserves every exact identity.

## Counterexample attempts and direct check

The following alternatives were challenged rather than silently omitted:

- A sixth C1 point creates a second triangle at 1.
- A sixth C2 point forces B_w2=1, contradicting the saturated-row commutation equation.
- A missing class among C4,…,C8 leaves the corresponding root neighbor at distance greater than two from w; more than one extra selected point exceeds degree 8.
- In case A, an additional or different B target exceeds the already saturated row {0,3,a}.
- In the doubled-class case, a remaining B target in X contradicts the exact common counts; a target in C1 or C4,…,C8 contradicts ST03 or ST04; w itself is excluded by the zero diagonal.
- A simultaneous-label collision does not occur: the two C4 points are distinct, and b is in a class unused by the A row. The shared point in case A is sent to the same canonical label in both matrices.

No counterexample was found; the algebraic exclusions above, rather than failed search, discharge the obligations.

A short direct Python check loaded the original S_TOUCH JSON, verified all class intervals and each complete selected A row, and recomputed the displayed common-neighbor counts and B values on 0,…,8 from the known template edges. All checks passed. Unknown Y–Y edges were irrelevant to these counts. This check did not construct a completed candidate, certify the remaining Y entries of B independently of the proof, or use a SAT solver. The semantic argument for those entries is ST03–ST08.

## Closure

There are no open proof issues at the audited conditional scope and no requested source fix. The resulting theorem is precisely: every actual S_TOUCH candidate has a simultaneous relabeling into one of the three complete A9/B9 rows. CNF correspondence, branch contradictions, a Lean bridge, the historical eight leaves, and full order-62 exclusion remain separate obligations. The source proof was left unchanged.
