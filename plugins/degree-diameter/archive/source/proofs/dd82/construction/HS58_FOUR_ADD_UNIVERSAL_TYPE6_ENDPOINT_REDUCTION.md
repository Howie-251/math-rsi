# HS58 universal type 6: complete endpoint closure outside the addition set

Date: 2026-10-12. **Complete argument checked locally by the root agent;
external delta review remains unfinished after authentication errors.**
This is the analytic closure of the last auxiliary type in
[the full four-addition exclusion](HS58_TWO_DELETE_FOUR_ADDITIONS_EXCLUSION.md).
It excludes every case with seven addition endpoints, every case where
the unique old center neighbor is a deletion endpoint, and every case
where it is not. The separate center-neighbor-in-W proof completes the
type-6 argument. The integrated document now includes this closure;
it does not claim completed external review.

This note was written after the stable ten-type result and the separate
[center neighbor in the addition set](HS58_FOUR_ADD_UNIVERSAL_TYPE6_V_IN_W.md)
argument. It is a subsequent proof, not part of the earlier review of
those files. No enumeration or solver is used in its arguments.

## Setting and incidence equalities

Let Q be HS50, D two original edges, A four original nonedges, and
M=Q-D+A. Write r_x=d_D(x), a_x=d_A(x), and
p_x=|B_x|=1+r_x-a_x. The auxiliary graph H is the star on eight new
vertices, with two disjoint extra edges among its seven leaves.
Its center c has exactly one old neighbor v. Three leaves are ordinary
(degree one in H); four are special (degree two).

Put W=V(A). The good-leaf argument in the ten-type exclusion proves
that every ordinary leaf occurs at an old vertex in W union {v}.
The branch v in W is closed in the separate note above. Assume here
that v is outside W. There are

\[
I=|W|-8+r(W)+r_v\ge3,\qquad r(W)=\sum_{x\in W}r_x
\]

leaf incidences on W union {v}. Since r(W)+r_v<=4, one has |W|>=7.

Let Z be the zero-port old vertices and E=sum_x max(p_x-1,0).
The total old-new incidence is 46, so |Z|=E+4. Every zero-port
vertex must be adjacent to v in M to reach c. As v has no added
edge, Z is a subset of its retained Q neighbors. Since p_v=1+r_v,

\[
r_v+4\le |Z|\le7-r_v.
\]

Consequently r_v<=1. In particular v cannot be the shared endpoint
of adjacent deletions.

## Seven addition endpoints are impossible

Suppose |W|=7. The four-edge graph A is P3 plus two independent edges.
Let t be its unique degree-two vertex. Nonnegative ports force
r_t>=1. Equality I=3 forces every deletion endpoint into W union {v},
and the three leaf incidences there are exactly the three distinct
ordinary labels.

### Disjoint deletions, with v not a deletion endpoint

Vertex t has zero ports. The other three deletion endpoints in W
each have one port; the three ordinary vertices of W also have zero
ports. Thus every old vertex has at most one port. A zero-port vertex
needs all eight old neighbors to have positive ports in order to
reach all eight new vertices. In particular A cannot join two
zero-port vertices.

However the zero-port vertices have total added degree 2+3=5,
whereas the three positive-port vertices in W have total added
degree 3. An edge between zero-port vertices is unavoidable. This
is a contradiction.

### Disjoint deletions, with v a deletion endpoint

Vertex t is zero-port and must be a retained Q neighbor of v, so
it is not v's deleted partner. Write D={vy,tw}. The positive-port
vertices of W are y,w, each with a distinct ordinary label. Vertex
v has c and the third ordinary label. The remaining five vertices
Z of W, including t, have zero ports and lie in N_Q(v).

Only v has two ports. Thus a zero-port vertex can have at most one
zero-port old neighbor. Since Q[N_Q(v)] is empty, t's two added
neighbors cannot both be zero-port. Its only possible positive
added neighbor is y: tw is an original edge and cannot be added.
Therefore A contains ty, ts, wq for distinct s,q in Z minus {t},
and an edge between the remaining two zero-port vertices.

The deleted pair tw has no shared new neighbor because B_t is empty.
It has no Q two-step path, since it was an edge of the triangle-free Q.
The only potential old repairs use one added edge:

* Through ty, a Q edge yw would create the four-cycle v-y-w-t-v.
* Through ts, a Q edge sw would give v,w a second common Q neighbor
  in addition to t.
* Through wq, a Q edge qt would lie inside N_Q(v).

All are impossible. Two added edges cannot join t to w in two steps
in this P3 plus two-edge pattern. Thus tw is unrepairable.

### Adjacent deletions

Write D={xy,xz}. If t=x, its sole port is an ordinary leaf. Its two
added neighbors are ordinary zero-port vertices: xy,xz cannot be
added, and v is not in W. Its five retained Q neighbors are outside
the deletion endpoints and have at most one leaf port each.
Consequently x reaches at most six leaf labels by direct or old
routes. Its ordinary leaf adds only c through H, so the seventh
leaf is missed.

If t=y, exchanging y,z if needed, then y has zero ports. Vertex x
has two ordinary ports. The possibility v=z is already impossible:
y,z are nonadjacent in Q and v has no added edge, so y cannot reach
c. Hence v lies outside the deletion endpoints. The only old vertex
with more than one port is x; y cannot be adjacent to it in M because
xy was deleted and cannot be added back. All old neighbors of y
therefore have at most one port. Among W, its only possible positive
added neighbor is z (the other positive vertex x is forbidden).
Its two added neighbors consequently include a zero-port vertex.
The eight old neighbors of y supply at most seven new labels,
again a contradiction. These cases exhaust |W|=7.

## Eight endpoints: a general zero-port edge obstruction

Now |W|=8, so A is a matching. Put

\[
\delta=4-r(W)-r_v\in\{0,1\}.
\]

If delta=1, exactly one deletion endpoint of deleted degree one
lies outside W union {v}; if delta=0, none does. Every vertex of
Z=W minus V(D) has zero ports, and every other old vertex has positive
ports. As before Z is a subset of the retained N_Q(v).

Suppose v is a deletion endpoint. Then |W intersect V(D)|<=3 and
|Z|>=5. The matching A must therefore contain a zero-zero edge tt'.
Choose a deleted partner y of v. Vertex y has positive ports and
is different from t,t'. Both old pairs ty,t'y had unique Q two-step
paths through v, destroyed by deleting vy. Neither pair has a new
common neighbor, because t,t' have zero ports.

Their own added edge tt' cannot repair either pair: both t and t'
are Q neighbors of v, and neither is a Q neighbor of y, by
triangle-freeness with vy. Nor is either pair directly added, since
t and t' are already matched to each other. Thus both old repairs
would have to use y's same added partner q. If y has no added edge
they fail immediately. Otherwise q must be a Q neighbor of both
t and t'. Their unique Q common neighbor is v, so q=v. But vy is
an original edge and cannot be added. This contradiction closes
every case with v in V(D), for adjacent as well as disjoint D.

In particular, a proposed five-cycle v-y-w-z-m-v with deleted vy,zw
does not certify a surviving template. It repairs a selected pair,
but its unavoidable zero-zero added edge produces the obstruction
above. No graph completion is claimed from that five-cycle.

## Eight endpoints and v outside the deletion endpoints

Let P=W intersect V(D), and k=|P|. Then Z=W minus V(D) has 8-k
vertices. For a deletion endpoint in W, its port count is r_x; for
one outside W, it is 1+r_x. Consequently the total positive port
excess is

\[
E=\sum_{x\in P}(r_x-1)+\sum_{x\notin W}r_x=4-k.
\]

Let Z_0 be the endpoints of those A edges with both endpoints in Z.
At most k vertices of Z can be paired to P, so

\[
|Z_0|\ge(8-k)-k=8-2k=2E.                         \tag{1}
\]

For q in Z_0, all seven Q edges at q are retained: q is not a
deletion endpoint. Its only added neighbor has zero ports, and q
itself has zero ports. To reach eight new vertices, its seven Q
neighbors must supply at least eight ports, so

\[
\sum_{t\in N_Q(q)}\max(p_t-1,0)\ge1.              \tag{2}
\]

This bound remains necessary if some of those seven neighbors have
zero ports; such a neighbor only makes the coverage harder.

Every vertex of Z_0 lies in N_Q(v). Every positive-excess vertex t
is different from v, because v is outside V(D) and outside W and
therefore has p_v=1. HS50 has at most one common Q neighbor for any
two distinct vertices, so

\[
|N_Q(t)\cap Z_0|\le |N_Q(t)\cap N_Q(v)|\le1.
\]

Summing (2), and then exchanging the order of summation, gives

\[
|Z_0|\le
\sum_t\max(p_t-1,0)|N_Q(t)\cap Z_0|
\le E.                                             \tag{3}
\]

Equations (1) and (3) imply 2E<=E. Hence E=0 and k=4.
In particular all adjacent-deletion cases are excluded, since
they have only three deletion endpoints. The only remaining case
has disjoint D, with all four endpoints in W.

## The zero-excess case

All four deletion endpoints P now lie in W and have one leaf port
each. The other four vertices Z of W have zero ports.
All old ports are at most one, including the sole center port at v.
Thus no zero-zero edge is allowed in M, and A is a perfect matching
between P and Z. The four leaf incidences on P include all three
distinct ordinary labels. Therefore at least one of the two deleted
edges has two distinct ordinary labels on its endpoints: among the
four endpoints include all three ordinary labels. If neither deleted
edge carried two distinct ordinary labels, each edge would contain
at most one distinct ordinary label, giving at most two in total.

An endpoint of that edge reaches no additional leaf through its
ordinary H neighbor, while its added old neighbor has zero ports.
Its six retained Q neighbors must supply the other six leaf labels.
Each old vertex has at most one leaf port. Hence the endpoint has
no Q neighbor in Z. The same holds at the other endpoint. Their
deleted edge has disjoint port sets and cannot be repaired through
either added partner in Z. This is a contradiction.

## Scope and proof status

The case v in W is excluded in the cited separate proof. For v
outside W, the ordinary-leaf incidence bound permits only |W|=7
or 8. The seven-endpoint argument exhausts adjacent/disjoint D
and every possible location of the degree-two addition endpoint.
With eight endpoints, the zero-port edge obstruction excludes v
in V(D); the excess argument and zero-excess argument exclude v
outside V(D). There is therefore no remaining type-6 endpoint case.

Combining this locally checked argument with the earlier ten-type
result excludes exactly two HS deletions and exactly four
old nonedge additions. Together with the already established
zero-through-three addition exclusions, this makes at least
five additions necessary at exactly two deletions. It makes no claim
for five or more additions.

The separately run full-edit type-6 SAT returned UNKNOWN and supplies
no exclusion. This note introduces no further SAT, graph generation,
or search. Its conclusion is an analytic proof, not a consequence of
the solver's resource limit or the failure of a proposed seed.
