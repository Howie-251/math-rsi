# D1_MATCH local reduction: proof skeleton

Audited source: `proofs/dd82/n62/D1_MATCH_HARD_BRANCH_REDUCTION.md`, all 209 lines, including the completed transport section (16). The author confirmed this source was stable during review. This is a fresh read-only source review; no source proof was edited.

Review scope is the conditional local reduction at an actual D1_MATCH root. It does not include exclusion of that root, existence of a graph satisfying the reduction, or the arbitrary order-62 upper bound. Requested reviewer: `gpt-6-astra`, effort `ultra`; actual backend identity is not independently attested. Review independence is `same-family`; semantic acceptance is `provisional`.

## Canonical statement and assumptions

For every finite simple undirected graph G with 62 vertices, maximum degree at most eight, and diameter at most two, and every root 0 with the displayed D1_MATCH parent structure, let A be the actual adjacency matrix and B=A²+A−7I−J. Then, after possibly interchanging parent labels 2 and 3, all rows, adjacencies, nonadjacencies, common-neighbor identities, and matching assertions in sections 1–5 and (16) hold. In particular, rerooting at w preserves D1_MATCH; its two light mates a,r are distinct nonadjacent triangle-free vertices with B_ar=0 and N(a)∩N(r)={c}.

Assumptions actually used:

- The original graph assumptions give degree eight, exact B identities, and the triangle budget. The displayed D1 parent partition gives the initial rows and ordinary-class sizes.
- The universal triangle-pairing theorem supplies homogeneity of triangle status along positive B entries. Its proof was inspected, including the S_TOUCH derivation it imports. Its proof does not need globally simple B or elimination of triple repeats.
- Section 1 of `D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md` supplies the D0_MATCH four-vertex component theorem. Its hypotheses are discharged at the actual reroot w. Neither that document's parity/outlet section nor the recovered triple-repeat checker is used in this reduction.
- No globally triangle-free assumption, independent matrix relaxation, SAT result, Lean axiom, or computational enumeration is used.

## Types and dependency graph

G is a finite simple undirected graph; A is its symmetric {0,1} adjacency matrix with zero diagonal. B is its actual symmetric nonnegative integral 62×62 repeat matrix with zero diagonal and row sum three. The notation c(u,v) denotes an integer common-neighbor count; the vertex named c is distinguished by arity/context. All other lower-case vertex symbols denote actual distinct vertices where distinctness is asserted or derived. X is N(0); C_i are the disjoint ordinary singleton-parent classes outside {0}∪X∪{w,a}. H=C1. W and U are the ordinary parts of N(w),N(a). B_Cj,y is a sum of repeat weights, not an adjacency count. Matchings in G use A entries; matchings in B use positive unit B entries. Multisets in (15) retain multiplicity.

Dependency DAG:

1. Original graph → regularity / actual identities / triangle budget.
2. Original graph + local S_TOUCH argument → triangle pairing → triangle-status homogeneity.
3. Actual identities + D1 parent partition + homogeneity → W, distinct r,p,q, rows of a,w.
4. Actual identities + disjoint-parent D0_MATCH template → D0 component theorem; this independent theorem + r∈C4 → contradiction.
5. r∈C2 + complete rows of 2,3 → b,c locations → r adjacent to b,c → exact light-mate common neighbor → persistent D1 reroot and row of r.
6. These local rows → ordinary-neighborhood profiles → the three G matchings and three B matchings → transport identities (15).
7. Rows of 2,3 + neighbor counts → (16) → internal repeat restrictions and two distinct C2–C3 perfect matchings.

There is no path back from a downstream D1 conclusion into triangle pairing or D0_MATCH. Global triple-repeat elimination, parity, and the classification covering arbitrary roots are outside this DAG.

## Micro-claim inventory

All entries are discharged; numbering is local to this review.

| ID | Source lines | Context → conclusion; rule and side-condition discharge |
|---|---:|---|
| MC01 | 11–17 | Graph assumptions → regularity and exact B identities. A degree ≤7 reaches at most 57 vertices; regularity gives zero diagonal, row sum 64+8−7−62=3 and AJ=JA. |
| MC02 | 19 | Actual B → sum over adjacent repeat entries =2t(v)≤3, hence t(v)≤1 and adjacent positive B means a triangle. |
| MC03 | 19 | Universal pairing → every triangle vertex belongs to a closed six-vertex unit-repeat prism; positive B cannot cross triangle status. Saturation at both triangles closes the component. |
| MC04 | 21–35 | Actual D1 parents → stated class sizes and B_X entries. Common neighbors of two labels are root 0 plus precisely their shared exceptional parents. |
| MC05 | 35 | Fixed nonadjacent repeats consume the budget → 0,w,1,2,3 are triangle-free; MC03 along B14 and B0a gives 4,a triangle-free. |
| MC06 | 39 | w triangle-free, parents 123, w not adjacent a → five ordinary neighbors, exactly one per C4,…,C8, and B_wX=0. Each remaining label requires coverage; capacity is exactly five. |
| MC07 | 41–50 | Row sum and (1,w) → B_w=2e0+e_r, r outside X, r≠a, and B_w,C1=0. Nonnegative summands at (1,w) must vanish. |
| MC08 | 50–58 | (0,a),(1,a) → B_X,a=0 and B_C1,a=0. The omitted terms vanish by the actual parent structure and MC07. |
| MC09 | 60–64 | Complete row B1 and N(1)={0,w,a}∪H → equation (1) for every ordinary y; B0y=0. |
| MC10 | 65–69 | MC07–09 and row sums → r,p,q distinct ordinary points in C2∪C3∪C4, unit weights, B_ar=0; MC03 gives r triangle-free. A doubled residual entry or shared endpoint violates a column capacity of one. |
| MC11 | 73–75 | r∈C4 → actual reroot w has heavy parents 123 and two light parents in W, disjoint; 0,r are a nonedge. D0_MATCH theorem gives B_ar=2, contradicting MC10. |
| MC12 | 75–77 | r∈C2∪C3 → label interchange 2↔3 makes r∈C2. This permutation preserves both exceptional parent sets; it asserts no graph automorphism. |
| MC13 | 81–86 | Fixed rows of 2,3 → ordinary residual unit endpoints b,c outside C1 and nonadjacent to their respective labels. Row B0 also excludes endpoint 0; (1,2),(1,3) exclude H. |
| MC14 | 88–92 | Actual (0,y) entry → (5). B_wa=0 and shared parent 1 give W∩U=∅, so b,c each lie in precisely one of W,U. |
| MC15 | 94–101 | (2,w),(3,w), r∈C2 → b∈W and c∈U, hence b≠c and A_cw=0. |
| MC16 | 103–105 | (2,a),(3,a) → B_a,C2=0 and B_a,C3=1; MC10 gives p∈C3,q∈C4 after naming. |
| MC17 | 109–116 | (2,r) → A_br=1+B_C2,r. A is Boolean and B nonnegative, hence A_br=1 and B_C2,r=0. |
| MC18 | 118–124 | (w,c) → A_rc=(AB)_wc≥B3c=1; Boolean A gives A_rc=1. |
| MC19 | 126–128 | a,c,r distinct, both a and r adjacent c, a triangle-free → A_ar=0. Actual CN identity and B_ar=0 then give N(a)∩N(r)={c}. |
| MC20 | 130–139 | (5),(1),(3,r) and row sum → B_r=e_w+e_s+e_t with s∈C3,t∈C4∪…∪C8. Actual CN(w,r)=2 gives parent pair {2,b}; remaining B_w entries give singleton parents at all other outside vertices of the reroot. |
| MC21 | 143–147,157 | a's two parents, triangle-freeness, B_aX=0 → ordinary profile U. r≠u2; c∈U, c≠u3 by triangle-free 3, c≠u2 by independence of C2, hence c∈C5∪…∪C8. |
| MC22 | 149–157 | (a,w) → A_ar=A_pw+A_qw=0, hence q≠W4. Triangle-free a and B_ap>0 give p≠u3. |
| MC23 | 159 | x∈H → x avoids w,a, B_X,x=0, and exactly one G-neighbor in each C2,…,C8. CN(x,j)=1 can only be supplied in C_j. |
| MC24 | 161–163 | CN(1,y)=1 for y∈C2∪C3∪C4 plus MC23 → G matchings H–Cj miss u2,u3,W4 respectively. Each target has at most one H-neighbor. |
| MC25 | 165 | Sum (1) over the 18 target vertices → repeat weight H→(C2∪C3∪C4)=15, exhausting the five H rows. Thus no positive B entry from H leaves these classes. |
| MC26 | 165–171 | b,c each already share w or a with label 1 → no H-neighbor. (2,x),(3,x) give one B unit into C2,C3; row sum gives one into C4. Equation (1) gives target capacities, hence B matchings miss r,p,q. |
| MC27 | 173 | MC19,21,22 → the G and B omitted points differ in each class. This does not identify any matching edges. |
| MC28 | 175–183 | (w,x),(a,x), MC25 → A_rx=B_W4,x and (15). Required mates exist uniquely by MC24,26,27. The second equality is an equality of multiplicity functions on H. |
| MC29 | 193 | Nonedges (2,b),(3,b), their fixed B entries, and b∈W → b has sole C2-neighbor r and no C3-neighbor. |
| MC30 | 193 | c∈C5∪…∪C8, c not adjacent w, and B2c=0,B3c=1 → c has sole C2-neighbor r and two distinct C3-neighbors v1,v2. |
| MC31 | 195–198 | Complete B2,B3 and N(2)={0,w}∪C2,N(3)={0,w}∪C3 → both equations (16) for all ordinary y. The subtraction is exactly B_wy=1_{y=r}. |
| MC32 | 202–203 | (16), MC29,30 → internal C2 repeat row sums all zero; internal C3 row sums one at v1,v2, zero elsewhere. Symmetry, zero diagonal, nonnegativity and integrality force the single unit edge v1v2. |
| MC33 | 204 | (16) gives cross-repeat row sum one on both six-point classes: for C2 targets A_cy=1_{y=r}, for C3 targets A_by=0. Thus B[C2,C3] is a perfect matching, pairing r with s. |
| MC34 | 205 | CN(3,y)=1 on C2 and CN(2,y)=1 on C3; neither root 0 nor w can supply it → original cross edges form a perfect matching. |
| MC35 | 207 | MC03 and B3c=1 make c triangle-free. Therefore v1,v2 avoid u3 and r's G-mate in C3; C3 is independent and B_v1v2=1, giving exactly CN(v1,v2)={3,c}. |
| MC36 | 5–7,185–209 | Final statement matches the derived local constraints. No D1 contradiction, even-double-edge-component theorem, or equality of G and B matchings is claimed. |

There are no limits, integrals, probabilistic modes, asymptotics, hidden constants, or induction claims. All inequalities are finite nonnegative sums or Boolean bounds; their side conditions are included above.
