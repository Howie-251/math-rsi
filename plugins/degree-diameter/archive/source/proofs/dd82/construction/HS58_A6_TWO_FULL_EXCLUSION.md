# HS58 a6: two full endpoints on one deleted edge are impossible

Date: 2026-10-12. Pure combinatorial exclusion of the remaining
disjoint-D, a=6, E=2 branch, after the small-excess reductions locate
the two full endpoints on one deleted edge. The argument does not
use the number of matching additions, and therefore also excludes
this same endpoint pattern for any addition count. H, attachments,
and all original-nonedge additions remain unrestricted.

Let D={tu,vw} be disjoint original edges of HS50 Q. Assume t,u are
the only positive-excess old vertices, each with two new neighbors
and no added old edge. Write B_x for an old vertex's new neighbors,
Z for the zero-port set, and M=Q-D+A for the old graph after edits.
The target graph has degree eight everywhere and diameter two.
For an ordinary old vertex, its addition degree plus its port count
equals one. Every ordinary positive vertex thus has exactly one
port and no addition. Each zero q satisfies

\[
d_M(q,Z)\le |N_M(q)\cap\{t,u\}|.                  \tag{1}
\]

Indeed zeros among q's eight old neighbors remove baseline port
slots, whereas each full endpoint supplies only one extra slot.

## Two distinct exceptional added neighbors

Neither v nor w can be zero. If v were zero, its addition degree
would be two. Its added neighbors cannot be full or ordinary positive
vertices, all of which have addition degree zero. The only other
possible positive addition endpoint is w, but vw is an original
edge and cannot be an added original nonedge. Both added neighbors
of v would therefore be in Z. Vertex v can Q-neighbor at most one
of t,u, since tu is an original edge; neither full endpoint can be
an added neighbor. Thus (1) gives a contradiction of at least two
against at most one. The same reasoning applies to w.

Consequently

\[
B_v=\{c\},\quad B_w=\{d\},\quad
N_A(v)=\{q_v\},\quad N_A(w)=\{q_w\},
\]

where q_v,q_w are ordinary zeros. They are distinct, since an
ordinary zero has addition degree one. In particular wq_w and
vq_v are original nonedges. Every remaining added edge lies inside
Z, and these edges form a matching on the other zeros. For a=6
there are four such edges, but that count will not be used.

Set T=N_Q(t) minus {u} and U=N_Q(u) minus {t}. For an endpoint q
of an internal added edge qq', the left side of (1) is at least one.
Its only added neighbor q' is zero, so q must Q-neighbor t or u.
It cannot neighbor both, by triangle-freeness. Inequality (1) also
shows that q has no Q neighbor in Z. If q neighbors t, its original
route to u used the deleted edge tu. There is no new intermediary,
and full u has no addition. The replacement must use qq', forcing
q' Q-adjacent to u. Thus all internal matching edges cross T to U,
and in particular

\[
Z\setminus\{q_v,q_w\}\subseteq T\cup U.           \tag{2}
\]

No relative position of q_v,q_w, and no particular matching of the
chosen T/U vertices, has been assumed.

## A repeated label near w bounds the degree of c

Let epsilon indicate the Q edge wq_v. Let h be the number of full
endpoints t,u that Q-neighbor w, and let k bound the number of
internal-matching zeros that Q-neighbor w. Vertex w has six retained
Q neighbors. At most h are full and at most k+epsilon are zero:
its own added neighbor q_w is not Q-adjacent to w. Therefore at
least 6-h-k-epsilon of these neighbors are ordinary positive vertices.

Take such a vertex r. Its sole original two-step route to v was
r-w-v, now broken. Vertex r has no addition. The only added edge
incident to v is vq_v, so the only possible new old two-step route
uses the Q edge rq_v. A direct added edge rv is impossible because
r has no addition; a route with two added edges is impossible for
the same reason. If rq_v is absent, a new intermediary is required,
forcing r's sole port to equal c.

There are at most 1-epsilon exceptions: w and q_v have no common
Q neighbor when adjacent, and exactly one when nonadjacent. Thus at
least

\[
F=6-h-k-\epsilon-(1-\epsilon)=5-h-k              \tag{3}
\]

ordinary vertices besides v carry label c. Exact degree eight at
the new vertex c gives

\[
|B^c|\ge1+F,\qquad d_H(c)\le7-F.                 \tag{4}
\]

The labels c,d are not assumed distinct; coincidence only strengthens
the old-neighbor count for c.

## At most two labels through old neighbors of v

We will orient the names v,w so that v has no Q neighbor among
t,u. Any positive retained Q neighbor r of v is then ordinary.
Its old pair with w lost its unique original route r-v-w. Its only
possible replacement old route uses w's unique added edge wq_w,
and hence requires rq_w in Q. Otherwise r must carry label d.
As before, no direct or two-added-edge repair is available at r.

Let eta indicate vq_w in Q. At most 1-eta such ordinary neighbors
can be exceptions, by the common-neighbor count of v and q_w.
Consequently all positive old intermediates from v supply at most
two labels: d and possibly the label of one exceptional vertex.
Zero old neighbors supply none, and v's added neighbor q_v is zero.

Every new vertex within two steps of v is therefore contained in
the union of its own label c, the H neighbors of c, and at most two
old-intermediate labels. The number reachable is at most

\[
1+d_H(c)+2.                                       \tag{5}
\]

The two exceptional neighbors used in the proof are kept distinct:
q_v controls exceptions among Q-neighbors of w in (3), while q_w
controls exceptions among Q-neighbors of v in (5). Neither was
identified with the other or assumed to have a specified position.

## Both deletion geometries contradict eight-label coverage

Two disjoint edges of Q have at most one cross edge. Two sharing
cross edges would make a triangle, and two disjoint cross edges
would make a four-cycle.

If there is no cross edge, h=0. The unique common neighbors of w
with t and with u bound its neighbors in T union U by two, so (2)
allows k=2. Equations (3)-(4) give F>=3 and d_H(c)<=4. Vertex v
has no full Q neighbor, as required above. Bound (5) is at most
1+4+2=7, contradicting coverage of all eight new vertices.

If there is a cross edge, interchange v,w if necessary so that it
meets w; interchange t,u if necessary so it is wt. These exchanges
also exchange c,d and q_v,q_w consistently. They preserve all the
structural assumptions and ensure that v has no full Q neighbor.
Here h=1 and k=0. A point of T cannot Q-neighbor w, by the triangle
through t; the unique common neighbor of w,u is t, which is excluded
from U, so no point of U can Q-neighbor w either. Therefore F>=4
and d_H(c)<=3. Bound (5) is now at most 1+3+2=6, again impossible.

This excludes the requested E=2, full-deleted-edge branch at a=6.
Since neither the count four of internal matching edges nor |E(H)|
was used, the same proof excludes this endpoint pattern for any
addition count. It does not rely on an auxiliary catalog, a chosen
port pair, symmetry of H, a solver outcome, or the q_v/q_w placements.
