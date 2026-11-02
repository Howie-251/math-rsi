# Triangle-witness refinement: original-scope obligations

Reviewed source: `proofs/dd82/n62/CONNECTED_REPEAT_TRIANGLE_WITNESS_REFINEMENT.md`, all 307 lines, on 2026-10-11. Reviewer: `/root/proof_review_n62_triangle_witnesses`. This is a fresh same-family review; acceptance remains provisional.

## Assumptions and typed notation

The quantified domain is every actual finite simple order-62 graph of maximum degree eight and diameter at most two satisfying the source's explicit connected-repeat-support assumption and cited reductions. In particular, the original graph is triangle-free, `A` is its 8-regular adjacency matrix, and `B=A²+A−7I−J` is symmetric, nonnegative integral, zero-diagonal, has row sum three, entries at most two, and commutes with `A`. Every double repeat has the normalized D1 structure. This review does not independently remove the connectedness assumption or re-audit the finite quotient classifications behind another paper's connectedness theorem.

`D` is the set of double-repeat endpoints, `S_gen` the union of generated unit triangles, `U` the set of all unit-triangle vertices, and `W=V\(D∪S_gen)`. Thus `|D|=2d`, `|S_gen|=3d`, `D∩U=∅`, and `|W|=62−5d`. A type-one triangle `T` has its unique original common neighbor `c(T)`; `C1` is the set of these distinct centers, `U1` the union of their triangles, and `c_out=|C1\U|`. Both `C1` and `U1` lie in `W`. For `w∈W`, `m(w)` counts original edges among its three unit repeat neighbors, `ell(w)` counts heavy repeat neighbors, and `L3=|{w∈W:ell(w)=3}|`. All counts are nonnegative integers. Ports are vertices and need not be distinct across different rows.

## Dependency structure

Original D1 root rows and light-mate facts + original generated-triangle separation → exact heavy-neighborhood restriction → all-witness nonheavy theorem → type-one center/witness isolation and vertex bound → strengthened packing and mixed trace.

Original type-one center row and injectivity + overlap-cluster classification → symmetric center relation → component classification and refinements → the stated `d=9, v_extra=11` restriction.

Diamond saturated rows + actual repeat polynomial → signed-vector equation → perfect matching. Diamond commutation + the new type-one vertex bound → tip-adjacency type-zero consequence.

No circular dependency is needed. The original triangle-pattern paper's center-injectivity and center-outside-generated-triangles arguments precede, and do not use, this refinement. No limits, asymptotics, probability-mode changes, or analytic interchanges occur.

## Obligations and discharge

| ID | Quantified conclusion / obligation | Discharge |
|---|---|---|
| TW01 | For every heavy endpoint `h`, `B[N_G(h)]` is triangle `123`, edge `14`, and four isolates. | Each pair has common neighbor `h`; its only possible additional common neighbors are the D1 exceptional parent triple and pair. Their intersection has size one, so no pair receives both additions. Source lines 67–83. |
| TW02 | For every nongenerated unit triangle `T` and every pair in `T`, every original common neighbor is outside `D`. | `T` is disjoint from the generated triangle of every heavy pair. Every positive entry in TW01 meets that generated triangle. This proves `|N_G(h)∩T|≤1` for every `h∈D`, with the universal witness quantifier intact. Lines 85–99. |
| TW03 | Every type-one center has `ell=0`, `m=0`, and is not a heavy endpoint's light mate. | Original complete row `B_u=e_a+e_b+e_c`; TW02 excludes heavy `a,b,c`; triangle-freeness makes them independent. The original source also gives `u∈W`, so the local functions are defined. Lines 103–119. |
| TW04 | The center is isolated in the original graph on each of its three other witnesses' repeat neighborhoods; `B[{u,a,b,c},T]=0`. | `(AB)_{au}=0`, `AB=BA`, and nonnegative summands give `A_uv=0` for every repeat neighbor `v` of `a`, including the other two besides `u`. Repeat for `b,c`. Each witness is nonheavy and has three unit neighbors. Lines 121–136. |
| TW05 | Every `v∈U1` has `m(v)≤1`; every `v∈U` has `ell(v)=0`. | Two possible original port edges at `x` would make its port one of the exact witnesses `{u,b}` for `y,z`, forbidden by TW04. The light-mate theorem excludes a heavy repeat neighbor at any unit-triangle vertex. Lines 138–147. |
| TW06 | `17d+3v_extra+3c_out≤186`. | Count all `2d` unit incidences from heavy endpoints into `V\(D∪U∪C1)`, allowing collisions and capacity three per recipient. `D` is disjoint from the other two sets, and `|U∪C1|=3d+v_extra+c_out`. Lines 151–159. |
| TW07 | `tau+4t1+2|U1\C1|≤248−24d+2L3`. | In the original sum over `W`, save two units of `m` at each of the `t1` distinct centers and one at each vertex in `U1\C1`. These sets are disjoint; multiply the resulting sum by two. Lines 161–170. |
| TW08 | `c(T)∈T'` iff `c(T')∈T`; any triangle containing a type-one center is type one, and related triangles are disjoint. | A triangle containing `u` uses two of `a,b,c`. Exact pair intersections `N(u)∩N(a)={x,y}`, etc., give its unique center in `T`. All four witnesses lie outside `T`. Lines 174–184. |
| TW09 | Center graph degrees are at most two, and isolated vertices number `c_out`. | Neighbors contain the given center, which lies on at most two unit triangles; every triangle containing it is type one by TW08. Lines 185–190. |
| TW10 | Every center-graph component is `K1`, `K2`, `P3`, `P4`, or `C4`. | Five consecutive distinct vertices force three triangles into one overlap cluster. A 3-cycle conflicts with disjointness of adjacent triangles; longer cycles contain the forbidden five-vertex path. Finite maximum-degree-two components exhaust paths and cycles. Lines 192–206. |
| TW11 | In a `P3`, the middle triangle is an isolated overlap cluster; `P4`/`C4` occupy exactly two diamond clusters. | Two distinct neighbor-centers lie in the middle triangle. Any triangle overlapping it contains at least one, hence is type one and creates an extra center-graph edge. Alternating positions in `P4`/`C4` overlap and exhaust the two-triangle clusters. Lines 208–221. |
| TW12 | `d=9, v_extra=11` implies some nongenerated triangle is type zero; if `d=9` and `t1>0`, then `c5≤2501`. | `3s+4k=11` gives `(s,k)=(1,2)` and TW06 gives `c_out=0`. Five type-one triangles would form `P3+K2`; TW11 leaves the remaining `K2` on one diamond, contradicting related-triangle disjointness. For the trace claim, TW07 gives `tau<44`, and `tau=10c5−24976≥0` gives `tau∈{4,14,24,34}`. Lines 225–252. |
| TW13 | For a diamond's shared endpoints `x,y`, the original graph between `X=N(x)\N(y)` and `Y=N(y)\N(x)` is a perfect matching; other nonendpoint vertices balance their neighbors in `X,Y`. | Saturated symmetric rows give `B(e_x−e_y)=−(e_x−e_y)`. Thus `Ar=6f−r`, where `r=1_X−1_Y`; `x,y∉X∪Y`, both sets are independent, and both have six vertices. Evaluating on `X`, `Y`, and the complement proves the claims. Lines 256–276. |
| TW14 | Diamond commutation gives `A_xp=A_yp=A_xq=A_yq=A_zw`; if `z~_G w`, both diamond triangles are type zero. | At `(x,z)`, the two sides are respectively `A_xp` and `A_wz`; the other three positions are identical derivations. Tip adjacency gives two original edges in each tip's three-unit repeat neighborhood, violating TW05 if its triangle were type one. Overlap excludes generated/type-two triangles. This proof permits `p=q`. Lines 278–298. |

Necessary original sources read directly: `CONNECTED_REPEAT_UNIT_TRIANGLE_PATTERNS.md`, `CONNECTED_REPEAT_MIXED_TRACE_AND_ROOT_PATTERNS.md`, `D1_MATCH_HARD_BRANCH_REDUCTION.md`, `D1_MATCH_C4_TRANSPORT_REFINEMENT.md`, and `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`, all under `proofs/dd82/n62/`. `CONNECTED_REPEAT_REDUCTION.md` was also read for the original count context; its computational connectedness argument is outside this audit's acceptance scope. No prior audit verdict was consulted.
