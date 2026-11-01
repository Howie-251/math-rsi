# Low positive occurrence in the six-positive residual

For the residual six positive four-sets, at most four negative triples and at most22 negative four-sets, suppose total indexed occurrence at every point is at most7 and maximum positive occurrence is at most2. This low-occurrence case is always repairable, without a ground-size or positive-union assumption.

Select a uniform point from each positive set independently and let R be their union. Call a point double if its positive occurrence is2. There are at most12 such points, because the six positive four-sets have24 indexed incidences. Their combined negative occurrence is at most5·12=60. A double point has occupancy probability at most p=7/16; every other point has occupancy probability at most q=1/4, with inactive points having probability0. The joint occupancy lemma bounds the probability that a fixed negative t-set, containing j double points, lies in R by p^j q^(t−j).

For t=3,4 this geometric sequence is convex in j. Its endpoint-chord bound is

p^j q^(t−j) ≤ q^t + (j/t)(p^t−q^t).

The chord slope for triples is( p^3−q^3 )/3=93/4096, larger than the four-set slope( p^4−q^4 )/4=2145/262144. The triples can use at most12 double-point incidences. Allocate those12 units at the larger slope and the remaining at-most48 of the60 units at the smaller slope. This yields the valid upper bound

4q^3+22q^4+12(p^3−q^3)/3+48(p^4−q^4)/4
=4p^3+10q^4+12p^4
=53324/65536<1.

Hence there is a repair. Using fewer negative sets or fewer double-point incidences can only lower this bound.

In the actual one-higher-trace residual, the union of the six positives is at least16, so the number of double points is at most8. Replacing60 by40 gives the stronger bound

4p^3+15q^4+7p^4=42599/65536<1.

This note handles only maximum positive occurrence≤2. It does not claim a theorem for a vertex occurring in three or more positives.
