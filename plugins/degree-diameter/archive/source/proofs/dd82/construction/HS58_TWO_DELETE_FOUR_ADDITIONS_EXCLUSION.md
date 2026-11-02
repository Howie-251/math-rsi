# HS58 at two deletions and four additions: all eleven auxiliary types excluded

Date: 2026-10-12. **Complete exclusion within the specified HS58 family,
checked locally by the root agent; external review remains unfinished.**
All eleven necessary auxiliary types in the completed
[H(8,9) domain](HS58_TWO_DELETE_FOUR_ADDITIONS_AUXILIARY_DOMAIN.md)
are impossible for every old edit placement. Together with the earlier
zero-through-three addition exclusions, exactly two original HS edge
deletions therefore require at least five old nonedge additions.
The finite dependency is the complete eleven-type auxiliary catalog.
This does not exclude arbitrary 58-vertex graphs.

The setting is HS50 with exactly two original edges D deleted, exactly
four original nonedges A added among the old vertices, and eight new
vertices. For M=Q-D+A and old-new port sets B_x, put
r_x=d_D(x), a_x=d_A(x), p_x=|B_x|=1+r_x-a_x. Regularity gives
sum_xp_x=46, sum_xr_x=4, sum_xa_x=8, and |E(H)|=9.

## The nine nonuniversal types are closed

The complete proofs are in
[HS58_TWO_DELETE_FOUR_ADDITIONS_NONUNIVERSAL_EXCLUSION.md](HS58_TWO_DELETE_FOUR_ADDITIONS_NONUNIVERSAL_EXCLUSION.md).
They use the actual old graph M and cover all placements of D and A:

- Types 5,7,9,10 have a four-edge bad star. Saturated endpoint ports
  force A to be a matching outside D. An isolated vertex of the bad
  leaves' induced H graph gives a missed new label in the disjoint
  case; an old zero-port obstruction closes the adjacent case.
- Types 4,11 have a bad C4. All endpoint ports lie in its four-point
  support. The H entrances to the other four labels cannot all be
  supplied by a degree-one deletion endpoint's two ports.
- Types 2,3,8 have a three-edge bad star. The disjoint case follows
  from the absence of two Q cross-edges between two disjoint Q edges.
  In the adjacent case the proof covers full ports, one added edge
  at the deleted center, and one or two additions at a deleted leaf.
  The final type-3 branch would require seven old incidences at a new
  vertex of old capacity five.

The finite dependency is only the completeness of the eleven-type
auxiliary catalog. These exclusions do not rely on any SAT result,
fixed HS labeling, or asserted HS automorphism orbit.

## A good ordinary leaf is impossible in either universal type

Now suppose H has a universal vertex c. It is a star on eight vertices
with two further edges among its leaves. Let v be c's unique old
neighbor and W the endpoints of A. A leaf of H-degree one will be
called ordinary; it has seven old neighbors. The other leaves have
smaller old columns. There are four ordinary leaves in type 1 and
three in type 6.

Call an ordinary leaf good if its old seven-set S avoids W union {v}.
To reach that leaf, every old vertex other than v must belong to S
or have an M neighbor in S. Since no addition meets S, it dominates
Q-v. The existing [seven-point domination lemma](HS59_SPARSE_AUXILIARY_REMAINDER.md)
gives either S=N_Q(v), or S=N_Q(x) with dist_Q(x,v)=2.

The latter case cannot cover all seven new leaf labels at x. As in
the three-addition proof, direct attachments and old intermediates
supply at most

\[
4-a_x+\sum_{y\in N_A(x)}r_y.                          \tag{1}
\]

Retained Q neighbors share the good leaf and their total deleted
degree is at most 2-r_x. Added neighbors y have p_y<=r_y. At most
two additional leaf labels can be supplied by the two H leaf edges;
if p_x=0, this H contribution is zero. The complete small degree
case split is:

| a_x | r_x | Old/direct bound | H leaf contribution | Total bound |
| ---: | --- | ---: | ---: | ---: |
| 0 | 0,1,2 | 4 | 2 | 6 |
| 1 | 0 | 5 | 0 | 5 |
| 1 | 1 | 4 | 2 | 6 |
| 1 | 2 | 3 | 2 | 5 |
| 2 | 1 | 5 | 0 | 5 |
| 2 | 2 | 2 | 2 | 4 |
| 3 | 2 | 1 | 0 | 1 |

All other pairs violate p_x>=0. For the sharper entries: when r_x=2,
every other deletion endpoint is a Q neighbor of x and hence cannot
be an added neighbor, so the sum in (1) is zero. When r_x=1, a vertex
of deleted degree two would be x's deleted Q neighbor; it cannot
be x's added neighbor either. All bounds therefore follow from the
two-edge D and the requirement that A consists of original nonedges.
None reaches seven.

Thus a good ordinary leaf would have S=N_Q(v), avoiding W. Let z be
the number of old zero-port vertices and E=sum_x max(p_x-1,0). Since
the port sum is 46,

\[
z=E+4.
\]

No addition touches N_Q(v), so E>=sum_(s in N_Q(v))r_s>=r_v. The
center attachment gives p_v>=1, hence a_v<=r_v. Every zero-port
vertex lies outside N_Q(v) union {v}, but must be adjacent to v in
M to reach c. Each therefore uses an added edge at v, so z<=a_v.
The contradiction r_v+4<=z<=a_v<=r_v proves:

**Every ordinary leaf in either universal type touches W union {v}.**

## Equality structure for universal type 1

If v is outside W, the number of leaf incidences on W union {v} is

\[
|W|-8+\sum_{x\in W}r_x+r_v\le |W|-4\le4.             \tag{2}
\]

If v belongs to W, this number is

\[
|W|-9+\sum_{x\in W}r_x\le |W|-5\le3.                \tag{3}
\]

Type 1 has four ordinary leaves, all of which must touch this set.
Equality is consequently necessary in (2). It forces:

1. v is outside W, and |W|=8, so A is a four-edge matching.
2. Every deletion endpoint belongs to W union {v}.
3. Exactly four leaf incidences occur on W union {v}; they are the
   four distinct ordinary labels, once each.

In particular the leaf-port sets of distinct deletion endpoints are
disjoint. Only v has the center port. Thus no deleted edge has a
shared new neighbor and every deleted old edge needs an old repair.
All zero-port vertices belong to W and must lie in N_Q(v) minus the
deleted neighbors of v, because v has no added edge.

## Universal type 1 with adjacent deletions

Let D={xy,xz}, with shared endpoint x.

If v=x, its excess above one port is two, so z>=6 while v has only
five retained old neighbors. All zero-port vertices need to be among
those neighbors, a contradiction.

If v=y (the case v=z is identical), the center x has two leaf ports,
z one, and v has its center port and one ordinary leaf. All four
ordinary incidences are distinct. The zero-port set Z has six vertices
and equals N_Q(v) minus {x}. The matching A pairs x and z with
distinct members of Z: xz is an original edge and cannot be added.
No vertex of Z is a Q neighbor of x, by triangle-freeness with xv.
No vertex of Z is a Q neighbor of z, since v,z have the unique Q
common neighbor x, which is not in Z. Thus neither added partner can
repair the deleted old pair xz. Its ports are disjoint, a contradiction.

Finally suppose v is not a deletion endpoint. The matching endpoints
are x,y,z and five zero-port vertices Z. The only possible addition
between deletion endpoints is yz. If yz is added, old repair of
both xy and xz forces x's one added partner to be a Q neighbor of
both y and z; their only common neighbor is x itself, impossible.

Otherwise each of x,y,z is paired by A with a zero-port vertex. At x,
its two direct new neighbors are ordinary leaves; they provide no
further leaf via H. Its added old neighbor has zero ports. Its five
retained Q neighbors each have at most one leaf port, so covering
all seven leaves forces all five neighbors to have a leaf port.
In particular x has no Q neighbor in Z. Repair of xy must therefore
use x's added partner, not y's; repair of xz must use that same added
partner, not z's. It would again be a Q common neighbor of y and z,
which is impossible. This exhausts adjacent D.

## Universal type 1 with disjoint deletions

Under exactly the equality hypotheses just proved, the two positions
of v, inside or outside the four deletion endpoints, are excluded in
[HS58_FOUR_ADD_UNIVERSAL_TYPE1_DISJOINT.md](HS58_FOUR_ADD_UNIVERSAL_TYPE1_DISJOINT.md).
That proof uses the forced zero-port matching and ordinary leaf
incidences; it neither enumerates embeddings nor assumes an HS orbit.
Together with the adjacent argument above, it closes type 1.

## Closure of the last universal type

Auxiliary type 6 is the last type in the proof assembly. In the catalog
labels its edges are

```
01,02,03,04,05,06,07,14,23.
```

Thus 0 is universal, the leaf edges are the disjoint pairs 14 and 23,
and ordinary leaves 5,6,7 each have seven old neighbors. The center's
unique old neighbor v and the addition endpoint set W must satisfy
that all three ordinary labels touch W union {v}. Equations (2)-(3)
imply |W|>=7; further endpoint templates follow from their equality
cases. The subsequent scoped argument excludes
[v in W](HS58_FOUR_ADD_UNIVERSAL_TYPE6_V_IN_W.md).
A further [complete endpoint closure](HS58_FOUR_ADD_UNIVERSAL_TYPE6_ENDPOINT_REDUCTION.md)
handles v outside W, including the seven-endpoint cases and a
zero-port/excess counting obstruction for eight endpoints. The root
agent has read and checked the complete argument, including the final
zero-excess case. The two center-neighbor cases exhaust type 6.
The completed proof closes all eleven types; C17 and its delta review
have not supplied a verdict because the Google calls failed with 401
authentication errors. No external acceptance is claimed.

The one bounded full-edit type-6 solver run returned UNKNOWN. That
execution status remains unchanged. The analytic proof closes its
domain independently; the run is not a dependency of any proof above.

The original catalog's 48,160 labeled survivors and eleven types
remain unchanged as its raw output. Eleven later type exclusions are
recorded separately here. The actual complete graphs and checked
fixed-domain SAT experiment are construction feedback, not additional
proof obligations in these mathematical arguments.
