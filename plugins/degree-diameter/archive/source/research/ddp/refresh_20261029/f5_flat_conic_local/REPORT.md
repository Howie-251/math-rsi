# Flat conic-color lift: one fixed local control fails

The frozen single-candidate prediction was refuted. Replacing all four matrices by I removes the old source-dependent holonomy drift, but this particular proper six-color rule still fails same-fiber radius-four coverage at all five checked roots. It is stopped without a graph-production batch, color search, noise adjustment, or whole-graph BFS.

## Difference from previously closed scopes

The previous `f5_d10_closed_route_diagnosis/PROOF_PACKAGE.md` excludes all10^60 edgewise coefficient choices with the old four matrices and their port directions fixed. Its rank(H-I) argument and finite odd-cycle gap conditions use those transported noise columns. They do not automatically extend to this rule, which sets every edge map to I and assigns one shared undirected vector to each edge.

The earlier `m3_translation/DERIVATION_PACKAGE.md` concerns F3^3, full three-element noise on each edge, degree12/D3, and a prepared31–33-controller evaluator. Its actual checks were two small K5 regression graphs; it did not fully search this fixed F5,3/2-noise,D4 domain. The binary72 `translation_bound_check/REPORT.md` closes offset-only repairs for a specific pair of fixed rank-three binary route images, not this new identity-map family. No complete prior execution of the present domain was found in the relevant ledger entries and these actual scope files. This is a scope comparison, not a claim that every historical file was audited.

## One actual direction rule

The fixed30-controller decomposes into ten vertex-disjoint triangles and six external pentagons. For each sorted triangle a<b<c, colors0,1,2 are assigned to edgesab,ac,bc. Each pentagon is rotated to its least vertex, given the lexicographically smaller orientation, and receives cyclic edge colors[3,4,3,4,5]. This completely determines all60 edge directions without a search.

The six vectors are

    v_t=(1,t,t^2), t=0,1,2,3,4;  v_5=(0,0,1), over F5.

Every three distinct colors are independent, by the conic/Vandermonde determinant. The worker checked all20 such determinants, all30 proper-color conditions, and the exact60-edge binding. Each triangle uses three independent vectors; each controller vertex has four directions in general position. These are genuine rank guarantees, not complete coverage guarantees.

The edge relation is

    (a,x) ~ (b,x+t*v_e),

with triangle coefficient set{0,1,-1}, external set{1,-1}, and negative coefficients in reverse. Both sets are symmetric, so reverse consistency is automatic. The rule defines3750 vertices and degree10, since each base vertex has two edges of each type, all directions are nonzero, and controller neighbors are distinct. No adjacency list was expanded. Connectivity and exact global diameter were not measured.

All external scalar gaps have shape{±2}. The entire graph rule has global translation automorphisms `(a,x)->(a,x+z)`. Hence each checked same-fiber endpoint set applies to every source coordinate in that fiber, not just coordinate zero.

## Exact local criterion and result

For a closed controller word w, identity maps give precisely

    displacement = sum_i sign_i*t_i*v_(edge_i).

There is no x-dependent term. The exact necessary same-fiber criterion at root a is that the union of these images, over all controller words of length at most4 returning to a, equal F5^3.

The worker reused the complete saved word lists for roots0,20,28,22,9. Each has word counts1,0,4,2,28 at lengths0,1,2,3,4. It replaced their old matrices/transported columns with the new literal translation vectors. Immediate backtracks and repeated visits to the same edge are retained with independent coefficients; in particular a fourfold traversal is not collapsed to one difference set.

| Root | Even closed-word union | Triangle union | Triangle points added | Full local union | Missing |
|---|---:|---:|---:|---:|---:|
|0 |109 |27 |2 |111 |14 |
|20 |109 |27 |2 |111 |14 |
|28 |103 |27 |4 |107 |18 |
|22 |109 |27 |2 |111 |14 |
|9 |103 |27 |2 |105 |20 |

For example, root0 cannot reach displacement(0,2,0) within four steps. Thus for every x, `(0,x)` and `(0,x+(0,2,0))` have no path of length at most4 in this formula graph. This already disproves D<=4 for the single rule; exact distances, global diameter, and ordinary total bad-pair counts are not asserted.

## Why removing holonomy was not enough

Here H=I, so the old intersection over im(H-I) has only the zero shift. The drift obstruction is indeed removed. However, the symmetric triangle set is

    Z={t0*v0+t1*v1+t2*v2 : ti in {0,±1}},

with27 points, and Z=-Z. The two reverse triangle traversals therefore give exactly the same set, rather than two complementary sets. Most of it is already in the even closed-word images: it adds only2–4 points at the checked roots. Proper conic coloring guarantees independence, but not that these restricted coefficient images cover the remaining targets.

The test produced no root with equal external gap shapes and full local coverage. Consequently it does not provide a counterexample to an analogous alternating-gap necessity in the new family. Conversely, failure of this one rule does not prove that such necessity holds for all identity-map lifts or all direction assignments. Only the original fixed-matrix family and this one separate flat candidate are closed by their respective evidence.

## Terminal scope and cost

`INPUT.json` saves all60 directions, coefficient sets, and deterministic coloring. `ROOT_a.json` saves every evaluated word image and missing displacement. `RESULT.json` records one candidate, five local roots, zero new controller-word enumerations, zero full graphs, zero BFS, and zero coloring searches. Actual CPU was0.019305658 seconds, one worker, within30 seconds. The prediction remains recorded in `PREDICTION.md`; this single control is complete and stopped, with no new lower bound.
