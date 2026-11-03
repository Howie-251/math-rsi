# Cyclic scalar head-triangle towers: necessary parameter filter

This is a small parameter-selection calculation, not a graph search or a new
degree–diameter bound. It uses the saved 2026-10-26 public lower-bound snapshot.
The scope is exactly a one-dimensional finite-field scalar action and a central
head triangle; it excludes neither higher-dimensional actions nor other towers.

For degree d put h=d−1, k=h(h−1), A=F_q×C3, K=C_k and
H=⟨k^(h−1)⟩ of order h. An element j of K acts as multiplication by r^j,
where r has order m dividing both k and q−1. Leaves, blocks and heads have
orders 3qk, 3q(h−1), 3q, respectively. Add a triangle on the three heads with
each fixed field coordinate. The resulting order is n=3qh²; the leaf set must
have h distinct inverse-closed nonidentity generators.

There are c=(q−1)/m nonzero field K-orbits. A head-to-head path of length at
most five can use either a triangle edge at the same field coordinate or one
leaf edge; it cannot combine a triangle edge with that leaf route. Consequently
every nonzero field orbit must occur among generators at each w=0,1,2.
At least c cross-w inverse pairs are needed, costing 2c slots. Cross pairs are
represented uniquely by their w=1 element. Let s be the number of internal
w=0 elements. Its parity is h mod 2. The following are necessary lower bounds
on s:

* In characteristic two, pure translations supply nonzero involutions. For odd
  q, nonzero involutions exist precisely when m is even and k/m is odd: the
  unique order-two K element then acts as −1. In either situation each internal
  component meets only one field orbit, and
  s ≥ c + ((h−c) mod 2).
* For odd q and odd m, −1 is outside ⟨r⟩. The c orbits form pairs under
  negation; an internal noninvolution inverse pair meets both colors in one such
  pair. Here c is even, no nonzero involution exists, and s ≥ c+(h mod 2).
* For odd q, even m and even k/m, −1 belongs to the scalar group but the
  order-two K element acts trivially. There are no nonzero involutions and an
  internal inverse pair stays in a single color. Thus s ≥ 2c+(h mod 2).

In the last two cases the sole nonidentity involution has zero field coordinate,
so it cannot supply a missing nonzero color. These statements follow directly
from (x,j)²=((1+r^j)x,2j) and inverse (−r^(−j)x,−j).
The filter requires 2c+s_min≤h. In particular, replacing an action by one of
half its order does not automatically double the internal slot requirement:
when m is odd, inverse pairs exchange two colors.

For each d=4,…,12, the size inequality is restricted to

    saved_lower_bound(d,5) < 3qh² ≤ 1+d*(1+h+h²+h³+h⁴).

The right side is the ordinary radius-five Moore bound. Enumerating all prime
powers in this finite interval and all m dividing gcd(k,q−1) gives the following
surviving tuples (these have not all been searched):

| d | q | action order m | field colors c | n |
|---:|---:|---:|---:|---:|
| 7 | 31 | 15 | 2 | 3348 |
| 7 | 31 | 30 | 1 | 3348 |
| 7 | 61 | 30 | 2 | 6588 |
| 8 | 43 | 21 | 2 | 6321 |
| 8 | 43 | 42 | 1 | 6321 |
| 9 | 113 | 56 | 2 | 21696 |
| 11 | 181 | 90 | 2 | 54300 |
| 11 | 271 | 90 | 3 | 81300 |
| 12 | 331 | 110 | 3 | 120153 |

No tuple survives this necessary filter for d=4,5,6,10 in this specified scalar
triangle family above the saved baselines. Surviving HH slot counts do not prove
BB, BL, LL or diameter five. Existing faithful c31/c43 experiments are recorded
in their own directories. This note creates no production queue for the other
tuples, and does not supersede the separately proposed q11 two-dimensional
Borel action.

`cyclic_triangle_parameter_filter.py` and `CYCLIC_TRIANGLE_PARAMETER_FILTER.json`
record the exact finite intervals and counts. No generator sets or graphs are
enumerated by this calculation.
