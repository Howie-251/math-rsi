# Sixth-cycle/determinant proof obligations

Fresh review of `proofs/dd82/n62/CONNECTED_REPEAT_SIXTH_CYCLES_AND_DETERMINANT.md`, all 290 lines, on 2026-10-11. Reviewer: `/root/proof_review_n62_sixth_trace`. This ledger concerns the stated actual-graph implication; it does not re-certify the historical connectedness classification. No prior audit verdicts were read.

## Quantified scope and symbols

For every actual finite simple graph G on 62 vertices, with maximum degree at most eight and diameter at most two, assume connected positive support of its actual repeat matrix and the declared consequences of the established reductions. Then all equations (1)–(13) in the reviewed note hold.

- A is the symmetric 62-by-62 integer adjacency matrix; A1=8·1, diagonal zero, and G is triangle-free.
- J is the 62-by-62 all-ones matrix; B=A²+A−7I−J is symmetric, integral, nonnegative, zero-diagonal, entrywise at most two, with B1=3·1.
- d is the number of unordered pairs carrying repeat weight two; every such pair is D1 and d is in {1,3,5,7,9}. The imported count is c4=(93+d)/2.
- cj counts unoriented simple j-cycles of G; u counts unordered unit triangles of B; τ=tr(AB²). The integers s,k count nongenerated single-triangle and diamond overlap clusters.
- M=2A+I; S=det(M)/17 is an integer, unrelated to the triangle-set notation in the dependency notes.
- κ(B) is the positive integer weighted spanning-tree count for the connected positive support of B.
- p(t)=det(tI−A)/(t−8) and q(x)=det(xI−B)/(x−3) are monic integer polynomials of degree 61.

No asymptotic, probabilistic, limiting, or infinite-sum claim occurs. There are no analytic interchanges or parameter-uniformity obligations.

## Dependencies and import boundaries

The DAG is acyclic: actual-graph reductions → adjacency walk counts and D1 triangle exclusion → B³ trace → parity and mixed traces; actual matrix identity → determinant square → weighted-tree and mod-17 congruences; actual matrix identity on 1-perp → characteristic identity. The cluster dependency is used only for equation (9).

1. `CONNECTED_REPEAT_REDUCTION.md`, read in full: supplies the explicitly declared reduction hypotheses and c4. Its earlier quotient computations and historical imported exclusions are not rerun or re-certified here. The reviewed note assumes connected repeat support, so it does not require a new proof that connectedness is automatic.
2. `CONNECTED_REPEAT_MIXED_TRACE_AND_ROOT_PATTERNS.md`, read in full: its Section 1 supplies τ=10c5+8d−25048; that expansion was independently recalculated here. No positive-root-pattern exclusion or τ=0 is imported.
3. `D1_MATCH_HARD_BRANCH_REDUCTION.md`, lines 1–106 read: the complete root row B0=2ew+ea and the commutation calculation giving Bwa=0 are the exact local inputs used to exclude a weighted repeat triangle. The generated triangle's three external ports are distinct: b and c are respectively in the disjoint ordinary neighborhoods of w and a, and label 4 is a root neighbor.
4. `CONNECTED_REPEAT_UNIT_TRIANGLE_PATTERNS.md`, read in full: only generated-triangle separation and the single-triangle/diamond overlap classification enter equation (9). Their needed row-budget arguments were checked. The deeper type-zero/type-one restrictions are not needed to prove the audited note.

## Obligations

| ID | Claim and source lines | Required facts and discharge |
|---|---|---|
| ST01 | Nonbacktracking recurrence and F6, 93–101 | Finite simple r-regular graph; F2 subtracts the r immediate returns. For j≥3 the forbidden extension count is r−1. Symbolic recurrence gives exactly the displayed polynomial. |
| ST02 | Closed nonbacktracking length-six classification, 103–115 | A shortest repeated-vertex segment has length at least four. Length five leaves a loop; length four can occupy only indices 1 through 5, since the other positions force an interior immediate reversal. Length six gives a simple cycle. |
| ST03 | Multiplicities 12c6 and 8(r−2)c4, 108; trace formula (5) | Each six-cycle has six starts and two directions. Each four-cycle has four tail attachment points, two directions, and r−2 eligible tail edges. Triangle-freeness excludes a tail endpoint at the opposite cycle vertex; the two cycle-neighbor tails violate nonbacktracking. Substitution yields 48(r−1)c4 and nr(5r²−6r+2). |
| ST04 | Numerical adjacency traces, 121–123 and 148–153 | n=62,r=8,c4=(93+d)/2 give tr(A6)=151528+168d+12c6 and tr(A4)=7812+4d. Triangle-freeness excludes nonsimple length-five closed walks, hence tr(A5)=10c5; tr(A2)=496. |
| ST05 | tr(B3)=6u, 127–132 | Every triangle containing a double edge 0w would have third vertex a by B0=2ew+ea; the checked D1 commutation calculation gives Bwa=0. Thus every repeat triangle has unit weights, and each contributes six oriented rooted walks. |
| ST06 | Q3 expansion and rank-one correction, 134–161 | Q commutes with J because Q1=65·1 and Q is symmetric. The polynomial expansion and the correction −274598 give tr(B3)=tr(A6)+30c5−72d−373984. Checked exactly. |
| ST07 | Equation (1) and cycle parity (8), 163–170 | Combining ST04–ST06 and dividing by six gives u=2c6+5c5+16d−37076. Substitution of the independently checked τ identity gives 2u=4c6+τ+24d−49104. Reduction mod two gives u≡c5. |
| ST08 | Cluster parity (9), 172–180 | Generated triangles are pairwise disjoint and meet no other unit triangle. Row sum three permits only isolated triangle/diamond overlap clusters unless a closed unit K4 occurs; connected order 62 excludes that component. Thus u=d+s+2k, and odd d gives c5≡1+s mod two. |
| ST09 | Mixed trace (10), 182–192 | Ordered repeat squares sum to 2(93−2d)+8d=186+4d; B²1=9·1 gives tr(JB²)=558. Multiply A²=7I+J+B−A by B² and trace to obtain the displayed 1860+28d+6u−τ. |
| ST10 | Integer, nonzero, odd S and determinant (2), 196–219 | M≡I mod two makes det(M) odd and nonzero. M1=17·1 implies the integer characteristic polynomial has factor t−17, so 17 divides det(M). The determinant lemma applies to invertible M² and yields det(M)²(1−248/289)=41S². No connectedness of B is needed here. |
| ST11 | Weighted-tree identity (12), 223–232 | B is symmetric with nonnegative integer edge weights and connected support; its weighted Laplacian is 3I−B and has a simple zero eigenvalue. The weighted matrix-tree theorem therefore gives q(3)=62κ(B). |
| ST12 | Congruences mod 41, 234–251 | Remove the principal factor 29+4·3=41 from (2). The remaining product is −4^61 q(−29/4), an integer coefficient expression after clearing powers of four. Modulo 41 this is −4^61 q(3)=39κ. Since 11²=39 and 11·15=1 mod 41, κ=(15S)² mod 41. No illegal reduction of individual real eigenvalues is needed. |
| ST13 | Congruence mod 17, 253–255 | 29I+4B=4(3I+B) mod 17, 4^62=−1 mod 17, and 41=7 mod 17, so det(3I+B)=−7S²=10S² mod 17. |
| ST14 | Characteristic identity (13), 259–270 | Diameter at most two gives connected G. Symmetric A diagonalizes on 1-perp and B acts there as A²+A−7I. The 61 factors give q(t²+t−7)=−p(t)p(−1−t); the sign is forced by the odd degree. This is a necessary spectral identity, not a realization criterion. |

All 14 obligations close under the declared imports. No extra hypothesis or source correction is required.
