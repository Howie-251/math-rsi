# T34 on 20 vertices: minimum degree eight

2026-10-13 first-hour sprint. Complete paper candidate based on an exact four-lock residual list and a short graph/incidence argument. No Lean completion is claimed.

## Target and invariant object

Let H be simple, pair-covering and five-uniform, with 20 vertices and exactly 34 edges, and minimum degree eight. Let L be its degree-eight vertex set and r=|L|. Since `sum d=170` and the all-eight baseline is 160, at most ten vertices have degree greater than eight. Thus `r≥10`.

The invariant object is the established conditional greedy-coloring failure upper bound `sum_k min(A_k,B_k,C_k-D_k)`. Assume that no strict witness in the explicitly checked local tables has yet supplied a coloring. We prove that the resulting actual incidence constraints are inconsistent.

## Notation and derivation map

λ(u,v) is actual pair codegree. A common trace of a selected subset is the number of edges containing that subset; an exact trace is the number whose intersection with the whole lock set equals that subset. The unit graph G on L joins u,v exactly when λ(u,v)=1.

1. Strict doubles restrict all low-low codegrees to at most three.
2. Strict triples and four-lock tables leave sixteen exact local orbits.
3. Any codegree-three pair would make one eight-degree vertex unable to cover the other low points, so all low-low codegrees are one or two.
4. The residual unit graphs impose small forbidden induced graphs, and link an induced four-cycle to an actual common edge.
5. These restrictions, together with degree eight and actual edge incidences, contradict r≥10.

## Main derivation

### 1. Complete local trace domain

The (8,8) double-lock profiles with λ=4,5,6,7,8 all have strict witnesses, so all low-low codegrees can be assumed in {1,2,3}. For any four selected low points, let q be the exact four-point trace, and let t_123,t_124,t_134,t_234 be exact triple traces. Recover every remaining count by

`l_ij = λ_ij-q-sum_(T contains ij) t_T`,

`l_i = 8-sum_(S contains i, |S|≥2) l_S`,

`l_empty = 34-sum_(S nonempty) l_S`.

All counts must be nonnegative and `0≤q≤min λ_ij`. This gives 12,103 labelled local profiles. Applying already strict three-lock profiles leaves 976 labelled profiles in 95 permutation orbits. Pure/total and exact avoided-lock dual witnesses handle 79 of those orbits, leaving the sixteen in `EIGHT_VERIFIED.json`.

These counts concern only four selected locks and exact integer trace identities. They are not an enumeration of H and do not assert realizability of every retained profile.

### 2. Exclude any codegree-three pair

Inspection of the verified sixteen-orbit residue gives this precise property: **every residual containing any codegree-three pair has all common triple and quadruple multiplicities zero**.

Suppose p,q∈L have λ(p,q)=3. For any other two distinct z,w∈L, apply the four-lock alternatives to {p,q,z,w}. Its residual must have all common triple counts zero. In particular no edge can contain p,z,w, and no edge can contain p,q,z. Since r≥10, an extra point is always available when extending a triple containing p,q to such a quadruple.

It follows that every edge incident to p contains at most one other point of L. There are eight such edges. Pair covering requires that they meet all r−1≥9 other points of L, a contradiction. Therefore every low-low codegree is one or two.

### 3. Exact consequences for the unit graph

A triangle in G has pair codegrees (1,1,1); both possible triple multiplicities already have strict witnesses. Hence G is triangle-free.

On four vertices the surviving unit graphs are exactly among:

- the empty graph;
- a single edge;
- the four-vertex path P4;
- the claw K1,3;
- the four-cycle C4.

This statement follows by translating each residual whose codegrees are all one/two; it does not discard trace data. In particular G has no induced disjoint pair of edges (2K2), and no induced three-vertex path plus an isolated vertex (P3+P1).

The residual common-four-edge multiplicity is **one for C4 and zero for each of the other four graph types**. Consequently an induced C4 is contained in an actual hyperedge, whereas an induced claw is not contained in any hyperedge.

### 4. At most two common unit neighbors

Suppose distinct p,q have three common unit neighbors a,b,c. Triangle-freeness implies p,q are nonadjacent and a,b,c are pairwise nonadjacent. The induced graphs on {p,q,a,b} and {p,q,a,c} are C4, so there are actual edges E and F containing these respective quadruples.

Both E and F contain p,a. Since λ(p,a)=1, these edges are equal. Their common value contains all five points p,q,a,b,c. But its four-point subset {p,a,b,c} induces a claw, whose residual common-four-edge multiplicity is zero. This is a contradiction. Thus any two vertices of G have at most two common neighbors.

The claw step is essential: merely putting five points in a five-edge would not be a contradiction.

### 5. A unit vertex of degree at least three forces a universal star

Let x have unit-graph degree k≥3, and let N be its k neighbors. They are pairwise nonadjacent. If z is outside {x}∪N, then z must be adjacent to at least k−1 members of N. Otherwise choose two members a,b of N not adjacent to z; the induced graph on {x,a,b,z} would be P3+P1.

If k≥4, this would give x,z at least three common neighbors, which Step 4 excludes. Therefore x is universal whenever k≥4.

If k=3 and x is not universal, every outside z shares exactly two of the three neighbors: at least two by the preceding argument and at most two by Step 4. Call the shared neighbors a,b and the third c. The induced graph on {a,z,b,c} is P3+P1, since a,b,c are pairwise nonadjacent and z is not adjacent to c. This is forbidden. A universal degree-three vertex has r=4, so is also impossible here.

Thus, if any unit-graph degree is at least three, G has a universal vertex x. By triangle-freeness all other vertices are pairwise nonadjacent, so G is exactly a star.

### 6. Exclude the universal star by actual incidence counting

Let S=L\{x} be its leaves, of size s=r−1≥9. Every pair of leaves has actual codegree two. Four leaves induce the empty unit graph, whose common-four-edge multiplicity is zero; hence every actual edge contains at most three leaves.

Write j_E=|E∩S|. Counting degrees and pairs gives

`sum_E j_E = 8s`,

`sum_E C(j_E,2) = 2 C(s,2) = s(s−1)`.

For j∈{0,1,2,3}, `C(j,2)≤j`. Therefore s(s−1)≤8s and s≤9. Since s≥9, equality holds and every edge with any leaf has exactly three leaves: equality in the pointwise inequality occurs only at j=0 or j=3.

But x and any three leaves induce a claw, so no edge containing x contains three leaves. Pair covering nevertheless requires an edge containing x and a leaf. Such an edge would have one or two leaves, contradicting the equality conclusion. The universal star is impossible.

### 7. Exclude maximum unit degree at most two

After Step 6 the maximum degree of G is at most two. If some vertex b has two neighbors a,c, they are nonadjacent by triangle-freeness. Every outside vertex must be adjacent to at least one of a,b,c, or it would form P3+P1 with them. It cannot be adjacent to b, whose degree is already two. Each of a,c has at most one remaining neighbor, so there are at most two outside vertices. This gives r≤5, impossible. Thus G has maximum degree at most one.

Since G has no induced 2K2, it has at most one edge. Let its edge count be e≤1. It has no induced C4, so every four-low subset has common-edge multiplicity zero. Hence every actual edge contains at most three points of L.

With j_E=|E∩L|, counting all low degrees and low pairs now gives

`sum_E j_E = 8r`,

`sum_E C(j_E,2) = 2 C(r,2)-e = r(r−1)-e`.

The same pointwise inequality gives `r(r−1)-e≤8r`, i.e. `r(r−9)≤e≤1`. For r≥10 the left side is at least ten. This final contradiction completes the candidate proof.

## Exact arithmetic and classification verification

`verify_eight.py` independently checks every retained strict A/B/C row using labelled injections, and rechecks rational avoided-lock multipliers, subfamily quotas, actual type-pair capacities, two-direction weights, and capacity penalties. It also rebuilds the 12,103-profile domain, the 976 profiles after triple elimination, and their binding to the 95 stored orbits, and mechanically verifies the stated common-trace/induced-graph properties of all sixteen residuals.

Evidence: `EIGHT_VERIFIED.json`; generating scans are `EIGHT_QUAD_DOMAIN.json`, `EIGHT_QUAD_SCAN.json`, and `EIGHT_DUAL.json`. The graph/incidence argument in Steps 2–7 is the general coverage argument; there is no enumeration of graphs on r vertices in this proof.

## Status, boundaries, and open risks

COHERENT AS STATED at complete paper-candidate level. Together with the three minimum-degree-seven notes and `LOW_DEGREE_SIX.md`, this supplies all possible minimum degrees 5,6,7,8 for 20 vertices. New Lean formalization and actual-H connections remain outstanding. Cross-model review must attack the trace-table scope, common/exact multiplicities, and the graph/incidence implications; arithmetic success alone is not reported as acceptance of the complete proof or the full T34 theorem.
