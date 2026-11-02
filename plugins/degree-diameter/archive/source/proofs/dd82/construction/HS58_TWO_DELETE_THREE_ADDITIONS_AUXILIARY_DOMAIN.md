# HS58: the complete auxiliary domain at two deletions and three additions

Date: 2026-10-12. Let Q be HS50. Delete exactly two original edges D,
add exactly three original nonedges A among its old vertices, and add
eight new vertices inducing H. This note classifies the necessary
auxiliary graphs H. It does not construct an HS completion or exclude
the two remaining auxiliary types on its own. The classification below has a pure
mathematical proof; the completed finite screen is recorded separately
as an actual check and source of explicit representatives.

Subsequent status: [the integrated exclusion](HS58_TWO_DELETE_THREE_ADDITIONS_EXCLUSION.md)
closes all three types for every old edit placement. The 2,688 raw
screen survivors per deletion budget remain unchanged below; they count
the auxiliary necessary domain before the later old-new contradiction.

## The necessary port budgets

Any order-58, maximum-degree-eight, diameter-two graph is eight-regular:
a vertex of degree at most seven reaches at most 1+7+7*7=57 vertices
within distance two. Write r_x=d_D(x), a_x=d_A(x), and let B_x be the
set of new neighbors of old vertex x. Then

\[
|B_x|=p_x=1+r_x-a_x,\qquad \sum_xp_x=48,\qquad |E(H)|=8.
\]

Let K(H) consist of the unordered new-vertex pairs whose distance in H
exceeds two, including pairs in different components. Each edge of
K(H) must lie in some clique on B_x: its length-two route needs an old
intermediate vertex. Vertices outside the endpoints of D have p_x<=1
and supply no such pair. Thus:

* If the two deleted edges are disjoint, K(H) must be covered by four
  cliques of order at most two. The resulting auxiliary-only test is
  |E(K(H))|<=4.
* If the deleted edges are adjacent, their center supplies a clique of
  order at most three and their other endpoints supply two cliques of
  order at most two. The auxiliary-only test is the existence of a
  three-element set U with
  |E(K(H)) intersect binom(U,2)| >= |E(K(H))|-2.

These are necessary tests preserving every completion. They do not
impose the actual identities, overlaps, or old-neighborhood constraints
of the port sets. In particular, either test implies b:=|E(K(H))|<=5.

## Analytic completeness: exactly three auxiliary types

A disconnected H would have at least k(8-k)>=7 bad pairs across a
nonempty component of order k. Hence H is connected, and its eight
edges on eight vertices make it unicyclic.

Put W=sum_v binom(d_H(v),2). The number of unordered pairs covered
within distance two is at most 8+W. A triangle forces at least three
overcounts in this total, one length-two route for each already
adjacent pair. A four-cycle forces at least two overcounts, one for
each pair of opposite vertices. There must be at least 28-b>=23
covered pairs.

Suppose the maximum degree is at most five, and let k be the number
of nonleaf vertices. Set x_v=d_H(v)-1. Then sum_v x_v=8,
0<=x_v<=4, and exactly k of the x_v are positive. Convexity of
binom(x+1,2), or transferring one unit toward the larger part, gives:

| Nonleaf count | Upper bound for W | Consequence |
|---|---:|---|
| k=3 | 17, attained by positive x=(4,3,1) | The cycle is a triangle, so coverage <=8+17-3=22. |
| k=4 | 15, attained by positive x=(4,2,1,1) | The cycle has length three or four, so coverage <=8+15-2=21. |
| k>=5 | 14, bounded by positive x=(4,1,1,1,1) | Coverage <=8+14=22. |

A cycle requires k>=3. All cases contradict the required 23 covered
pairs, so H has a vertex h of degree at least six.

If d(h)=7, the only remaining edge joins two leaves: H is a star with
one extra leaf edge. If d(h)=6, let u be its only nonneighbor. There
are exactly two edges outside the six edges incident to h, and
connectedness requires at least one of them to touch u.

* If d(u)=2, both go from u to neighbors of h. This gives a four-cycle
  with four additional leaves at h.
* If d(u)=1, write its neighbor as v. The other edge joins two
  neighbors of h. If it touches v, the result is a triangle through h
  and v, a pendant leaf at v, and four additional leaves at h.
* Otherwise the other edge avoids v. The result has a triangle at h
  and a length-two pendant path h-v-u. Its bad-pair graph is K1,5,
  centered at u. Four K2 cliques cannot cover its five edges. Nor can
  one K3 and two K2: a three-vertex clique contains at most two edges
  of a star, so their combined coverage is at most four.

The last type fails both port budgets. The first three types pass
both auxiliary-only tests, proving the classification without relying
on the finite screen.

## Exact representatives and the completed finite screen

All labels below are 0,...,7. An expression ij denotes edge {i,j}.

| Type | Edges | Degrees in label order | All bad pairs | Labeled count |
|---|---|---|---|---:|
| 1: star plus leaf edge | 01,02,03,04,05,06,07,12 | 7,2,2,1,1,1,1,1 | none | 168 |
| 2: triangle and off-hub pendant leaf | 01,02,04,05,06,07,12,13 | 6,3,2,1,1,1,1,1 | 34,35,36,37 | 1680 |
| 3: four-cycle and four hub leaves | 02,03,04,05,06,07,12,13 | 6,2,2,2,1,1,1,1 | 14,15,16,17 | 840 |

The source
[hs58_two_delete_three_add_auxiliary.cpp](../../../computations/dd82/construction/hs58_two_delete_three_add_auxiliary.cpp)
visits every eight-edge subset of the 28 possible edges, with no
topology or degree pruning. For each graph it computes its exact
distance-at-most-two reachability and applies the two tests above.
Its isomorphism key is exact for the surviving connected unicyclic
graphs: peel off the leaves, encode the rooted tree at each cycle
vertex by sorted recursive parenthesis strings, and minimize the
cyclic sequence over every rotation and reflection. An isomorphism
must preserve the unique cycle, and rooted-tree isomorphisms and these
cycle symmetries account for every possible graph isomorphism.

The single authorized run is recorded in
[enumeration.json](../../../computations/dd82/construction/hs58_two_delete_three_add_auxiliary_run/enumeration.json)
and
[resources.json](../../../computations/dd82/construction/hs58_two_delete_three_add_auxiliary_run/resources.json),
with its bounded launcher in
[hs58_two_delete_three_add_auxiliary_run.py](../../../computations/dd82/construction/hs58_two_delete_three_add_auxiliary_run.py).
It completed all binom(28,8)=3,108,105 labeled inputs. Both deletion
budgets retained exactly the same 2,688 labeled graphs, comprising the
three types above. The JSON preserves the complete bad-pair histogram,
all representative edges and bad pairs, canonical keys, multiplicities,
and witnesses for the adjacent-deletion budget. It reports
complete=true and stop_reason=complete_domain. Actual child CPU time
was 0.353891 seconds, on one pinned CPU, with exit code zero. No second
enumeration was run.

## The remaining domain and a forced addition pattern

The separate pure proof
[HS58_TWO_DELETE_THREE_ADDITIONS_UNIVERSAL_H.md](HS58_TWO_DELETE_THREE_ADDITIONS_UNIVERSAL_H.md)
excludes type 1 for every embedding of D and A. This later result is
not folded into the raw screen counts. The remaining auxiliary domain
is exactly types 2 and 3, representing 2,520 labeled graphs before
isomorphism compression. Each has four bad pairs forming K1,4.

Their four required pairs also force all additions away from the
deletion endpoints. For disjoint D, each of the four endpoint cliques
has capacity one. Covering all four pairs requires four port sets of
size exactly two, each covering a different required pair. For adjacent
D, the center clique of order at most three covers at most two edges
of K1,4, while each other endpoint clique covers at most one. Equality
is necessary in all three capacities, so their port-set sizes are
exactly 3,2,2. In either case p_x=1+r_x at every deletion endpoint,
which forces a_x=0 there.

Every vertex outside those endpoints has r_x=0, so nonnegative
p_x=1-a_x forces a_x<=1. Consequently the three added old edges must
form a matching entirely outside the endpoints of D. Moreover, every
deletion endpoint carries the center label of the bad K1,4. In the
disjoint case the other labels assign its four leaves bijectively to
the four endpoints. In the adjacent case the deleted-edge center
carries two of those leaves, and the other endpoints each carry one
of the remaining leaves.

These explicit two auxiliary shapes, deletion-endpoint port patterns,
and the disjoint three-edge addition matching are the necessary inputs
used by the subsequent integrated exclusion linked above. The screen
alone does not exclude them. No conclusion about four or more additions
is made here.
