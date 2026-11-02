# Eight old deletions still cannot extend Brown57 to order58

Status: complete paper proof; fresh proof-checker and Gemini B6 found no gap.
See reviews/dd82/proof-checker-brown8-20261011/ and
reviews/dd82/20261011_B6_upper63_brown9_n62.json. This is an edit-distance
obstruction for the explicit Brown graph, not order58 exclusion; Lean is pending.

## Statement

Any degree-at-most8, diameter-at-most2 graph on the 57 labelled Brown vertices
plus one new vertex must delete at least9 Brown edges and add exactly as many
old-old edges. The earlier proof excluded at most7 deletions; below excludes8.

## Explicit finite premises and notation

Use the complete graph in `computations/dd82/construction/brown57.edges`.
Its vertices partition into C (8 absolute points, degree7), I (21 degree8
points with no C neighbor), and E (28 remaining degree8 points). All C edges
go to E. Every E vertex has exactly2 C neighbors and3 I neighbors. Every I
vertex has exactly4 I neighbors.

There are14 triangles wholly in I and42 of type IEE. Each I lies in exactly
two III triangles and two IEE triangles. Every old edge belongs to at most
one triangle. An II edge belongs to one III triangle; an IE or EE edge belongs
to one IEE triangle; a CE edge lies in none. These are finite facts of this
specific graph, also derivable from its projective coordinates; their exact
check is `computations/dd82/construction/brown_eight_delete_facts.py`.

Suppose the proposed graph G deletes exactly8 old edges. It is 8-regular by
the original root bound. Its new vertex x has a set S of8 old neighbors, and
the number of newly added old-old edges is8 by edge counting.

Let d_v be the number of deleted edges incident to old vertex v, and let

    k_v = d_v + [v in C].

After deletion, k_v is the exact degree deficit to8. Hence S is contained in
{v:k_v>0}; for s in S, exactly k_s-1 new old-old incidences are available.
Write

    j=|S intersect I|, e=|S intersect E|, sigma=sum_(s in S)(k_s-1).

Old edges from S to C can only come from S intersect E. There are j+e points
of C outside S. If old edges from S cover at most h of them, at least
max(0,j+e-h) distinct added S-C edges are needed. These use that many of the
sigma available incidences. Each remaining added incidence can cover at most
one previously unreached I point in a path of length2 from x. This resource
inequality permits arbitrary added edges and arbitrary overlaps of neighborhoods.

## Only two triangle cases

Every I point initially lies in4 triangles but can lie in at most3 in G,
because its original repeat budget is65-58=7 and each triangle consumes2.
Thus the deleted edges destroy at least one old triangle at every I point.

Let a be the number of distinct destroyed III triangles and b the number of
distinct destroyed IEE triangles. Then

    a+b <= 8,   3a+b >= 21,

so a>=7. If a=8, all deleted edges are one edge from each of8 distinct III
triangles. If a=7, choose one deleted edge from each of those triangles as
seven base edges; precisely one extra deleted edge remains. Its old type is
II, CE, IE, or EE. The following cases are exhaustive.

## Case A: eight distinct III triangles

The8 destroyed triangles cover I. Their24 incidences on21 points, and the fact
that each I point lies in at most2 III triangles, show that exactly3 points
are covered twice. Every d_i is at most2, and at most3 points have d_i=2.
No E has a deficit, so e=0. No old S-C edge exists. The j missing C points
need at least j added incidences, but sigma<=j. Therefore all j I vertices
in S have d_i=2, j<=3, and every spare incidence is spent on C.

Such an I vertex retains just2 old I neighbors after deletion. Including
itself, it can cover at most3 I points. All8 C vertices have no old I neighbor,
and there are no spare added S-I incidences. At most3j<=9 of the21 I points
can be reached, a contradiction.

## Case B: seven III triangles and an extra II edge

There is no destroyed IEE triangle, so the seven III triangles cover all I
and therefore partition I. Their seven base edge deletions form a matching.
The extra II edge must be in one of these already destroyed triangles, or
there would be an eighth distinct destroyed III triangle. It shares exactly
one endpoint with the deleted edge of that triangle. Thus exactly one I
vertex has d_i=2, all others have d_i<=1, and e=0, sigma<=1.

The same C budget as Case A forces j<=1 and spends every spare incidence on C.
The at most one I point in S can cover at most3 I points. Contradiction.

## Case C: seven III triangles and an extra CE edge

Again the seven III triangles partition I and their base edges form a matching.
Only one C vertex can have k_c=2; only one E vertex can have positive deficit,
with k_e=1. Thus e<=1 and sigma<=1. If that E point is in S, its deleted CE
edge leaves it only one old C neighbor. Consequently h<=e, and the missing-C
requirement uses at least j spare incidences. In particular j<=1.

Each I vertex in S lost one II edge, so it covers at most4 old I points
including itself. The E vertex covers at most3. At most sigma-j added
incidences remain for I. Total I coverage is at most

    4j+3e+sigma-j <= 7 < 21.

## Case D: seven III triangles and an extra IE edge

At most one IEE triangle is additionally destroyed. Thus the seven III
triangles cover at least20 I points. Since they have21 incidences, at most
one I point lies in two selected III triangles. Let d_i^0 be the number of
base deleted edges incident to i. Then d_i^0<=2, with at most one entry2.

There is at most one deficient E vertex, so e<=1. Let epsilon be1 if the I
endpoint of the extra IE edge belongs to S, and0 otherwise. On S intersect I,

    sigma = sum d_i^0 + epsilon - j <= 2.

The last inequality follows because the seven base deletions have at most one
repeated endpoint and the extra edge can create at most one further spare
incidence. All C deficits are1; E's deficit is1 and adds no spare incidence.

Old E-C coverage is at most2e, so at least max(0,j-e) spare incidences are
needed for C. Hence j<=e+sigma<=3. An I point i in S covers at most5-d_i^0
old I points including itself; the extra IE deletion does not change its
number of I neighbors. The sole E endpoint has only2 remaining I neighbors.
Thus the number of reachable I points is at most

    5j - sum d_i^0 + 2e + sigma - max(0,j-e)
      = 4j + 2e + epsilon - max(0,j-e).

If j>=e this is3j+3e+epsilon<=13. If j<e, then(j,e)=(0,1) and the bound is2.
Both are below21.

## Case E: seven III triangles and an extra EE edge

The seven III triangles again cover at least20 I points, so their base edge
deletions have at most one repeated endpoint. Here e<=2 and sigma<=1.
All positive I deficits are precisely d_i^0 and

    sigma = sum_(i in S intersect I) d_i^0 - j.

As before, C requires at least max(0,j-e) added incidences, so j<=e+1<=3.
Deleting an EE edge does not change either E endpoint's3 I neighbors.
The I coverage bound is therefore

    5j - sum d_i^0 + 3e + sigma - max(0,j-e)
      = 4j+3e-max(0,j-e).

For j>=e this is3j+4e<=17; for j<e it is at most10. Again not all21 I points
can be reached.

Every possible eight-deletion case is impossible. Combined with
`BROWN_EXTENSION_OBSTRUCTION.md`, every such extension requires at least9
old deletions and9 old-old additions. No obstruction to nine or more deletions,
nor to arbitrary order58 graphs, is proved here.
