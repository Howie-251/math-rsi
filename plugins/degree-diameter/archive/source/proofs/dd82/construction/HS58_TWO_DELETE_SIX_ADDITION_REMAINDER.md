# HS58 with two old deletions: the six-addition remainder

Date: 2026-10-12. This integrates the completed two-deletion results.
The scope is arbitrary eight new vertices, attachments B and auxiliary
graph H, and arbitrary additions A of original HS nonedges. It is not
an exclusion of arbitrary 58-vertex graphs.

Subsequent completion on the same date: both remaining rows below are
now excluded by HS58_A6_TWO_FULL_EXCLUSION.md and
HS58_A6_THREE_FULL_EXCLUSION.md. The complete construction-family theorem
is HS58_TWO_DELETE_ARBITRARY_ADDITIONS_EXCLUSION.md. This file retains
the necessary-domain step in that proof.

Suppose such a construction has degree eight and diameter two. The
following necessary conditions now hold simultaneously:

1. The two deleted edges are disjoint.
2. Exactly six original nonedges are added, and H has eleven edges.
3. A is a matching on twelve old vertices.
4. The excess E=sum max(p_v-1,0) is either two or three. If E=2,
   its two full endpoints belong to the same deleted edge. If E=3,
   three of the four deletion endpoints are full.

Here p_v=1+d_D(v)-d_A(v) is the number of attachments at v, and
full means p_v=2 for a degree-one deletion endpoint.

## Complete case assembly

[The five-addition integration](HS58_TWO_DELETE_FIVE_ADDITIONS_EXCLUSION.md)
excludes a<=5 in all three deletion geometries.
[The global bound](HS58_TWO_DELETE_GLOBAL_ADDITION_BOUND.md)
proves a<=7 without restricting A, B or H.

For a>=6, [the small-excess proof](HS58_TWO_DELETE_SMALL_EXCESS_EXCLUSIONS.md)
excludes E<=1 and all E=2 patterns except two full endpoints of the same
deleted edge in a disjoint deletion pair. In particular it closes E=2
for adjacent deletions. For E=3, its final argument closes the adjacent
pattern (1,1,1), while the final section of
[the seven-addition proof](HS58_SEVEN_ADDITIONS_DISJOINT_EXCLUSION.md)
closes the adjacent pattern (2,1) for every a>=6. These exhaust adjacent
E=3 because the excess at a vertex is at most its deleted degree.

E=4 means every deletion endpoint has its maximum possible port count,
so no addition touches any deletion endpoint. The adjacent full-port
argument in [the nonuniversal four-addition paper](HS58_TWO_DELETE_FOUR_ADDITIONS_NONUNIVERSAL_EXCLUSION.md)
excludes adjacent D with any nonempty A.
For disjoint D, [the saturated structure theorem](HS58_SATURATED_DISJOINT_ALL_ADDITIONS.md)
gives a<=5 in the cross geometry and a<=6 in the no-cross geometry.
The latter equality consists of exactly four zero sets and 56 addition
matchings. All 56, with arbitrary B and H jointly free, are excluded by
the independently checked UNSAT input in
[the saturated completion report](HS58_A6_SATURATED_JOINT_COMPLETION.md).
Thus E=4 is closed in all geometries.

Adjacent D is now completely excluded. For disjoint D, the remaining
E=2 and E=3 patterns at a=7 are both excluded by the seven-addition
proof. This proves the first, second and fourth assertions above.

## Why every surviving A is a matching

In the E=2 pattern write D={tu,vw}, with t,u full. They have no
additions. Neither v nor w can have zero ports: such a vertex would
have two additions, both into Z={p=0}, whereas its number of retained
neighbors among t,u is at most one, since tu is an original edge and
HS has no triangle. It violates

    d_M(q,Z) <= sum_(s in N_M(q)) max(p_s-1,0).

The fact that both additions enter Z follows because the only other
possible positive-port addition endpoint is its partner on vw, and
that original edge cannot be an addition. Hence v,w both have one
port and one addition. All ten zero-port vertices are ordinary and
have addition degree one; the additions from v,w have distinct zero
endpoints. The remaining four additions match eight ordinary zeros.
Every endpoint of A therefore has addition degree one.

For E=3 write D={tu,wv}, with t,u,w full. If v were zero, its two
added neighbors would be zero, while it can retain at most one full
neighbor among t,u and none at w, the same contradiction. Thus v
has one port and one addition into Z. All eleven zeros are ordinary
with addition degree one. Five additions match ten zeros, and the
last joins v to the eleventh. Again A is a matching.

## Remaining constructive obligation

Neither pattern has yet been excluded by this integration. Their
zero-port rows and all actual old-to-old paths must be realizable,
followed by the same B and H meeting all 58-vertex degree and distance
conditions. Dedicated necessary-template investigations are underway;
the earlier unrestricted UNKNOWN/OUTPUT_LIMIT inputs do not decide them.

The complete graph problem at 58,59,60,61 remains open. This integration
has local mathematical and checked-computation support; no new external
review or Lean formalization is claimed.
