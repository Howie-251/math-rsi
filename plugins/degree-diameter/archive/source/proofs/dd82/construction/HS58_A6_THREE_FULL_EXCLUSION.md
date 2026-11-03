# HS58 a6: three full deletion endpoints are impossible

Date: 2026-10-12. Pure combinatorial exclusion of the remaining
disjoint-D, a=6, E=3 branch. H is arbitrary; no auxiliary catalog,
SAT, flow, or matching enumeration is used.

Let Q be HS50 and D={tu,wv} two disjoint original edges. Assume an
eight-regular diameter-two extension by eight new vertices with six
added original nonedges A and total port excess E=3. Label the three
full endpoints t,u,w, each having two ports and no addition. The
fourth endpoint v has at most one port. Write B_x for the set of new
neighbors of an old x and Z for the zero-port set. The degree identity
gives |Z|=11. Ordinary old vertices have at most one addition; any
positive ordinary vertex has exactly one port and no addition.

We repeatedly use the zero-row inequality

\[
d_{Q-D+A}(q,Z)\le |N_{Q-D+A}(q)\cap\{t,u,w\}|
\quad(q\in Z).                                      \tag{1}
\]

Indeed each old neighbor provides one baseline port except zeros,
and each of t,u,w supplies exactly one extra port. A zero vertex has
eight old neighbors and must reach all eight new vertices through
their ports. This is a necessary count, not a claim of distinctness.

## Reduction to five cross-neighborhood matching edges

If v were zero, it would have two additions, both to zeros: no
positive old vertex could have an addition. It has no retained edge
to w and is Q-adjacent to at most one of t,u, since tu is a Q edge.
It has no added neighbor among the full endpoints either. Inequality
(1) would read at least two on the left and at most one on the right.
Therefore v is positive, B_v={c}, and its sole added neighbor is
an ordinary zero q0. All other additions form five matching edges
inside Z on the other ten zeros. Their endpoints have addition
degree exactly one.

Put

\[
T=N_Q(t)\setminus\{u\},\qquad
U=N_Q(u)\setminus\{t\}.
\]

These disjoint six-sets induce an independent set: a within-set edge
would make a triangle, and an edge across them a four-cycle through
tu. If an internal added edge qq' has q Q-adjacent to t, the broken
original q-t-u route can only be replaced through q'; full u has
no addition and zero q has no new intermediary. Hence q' is
Q-adjacent to u. The reverse implication and t/u interchange hold.
Thus each internal added edge either joins T to U, or has both
endpoints outside T union U.

The second possibility is impossible. By (1), either endpoint q
must then neighbor w, and its internal added edge exhausts its one
available excess neighbor. Consequently q has no Q neighbor in Z.
The same holds for q'. The broken q-w-v route cannot be repaired
through q', since a Q edge q'v would form a triangle with w. It
cannot be repaired through v's added neighbor q0, since qq0 would
be a Q edge within Z. Direct qv and a two-added-edge route are
excluded by the unique addition of each endpoint. No new intermediary
is available. Therefore all five internal additions join T to U,
using five vertices on each side. In particular

\[
Z\setminus\{q0\}\subseteq T\cup U.                 \tag{2}
\]

The argument below does not require deciding which vertex of each
six-set is omitted, how the five pairs are matched, or where q0 lies.

## Repeated color around the third full endpoint

Let epsilon indicate the Q edge wq0. Let h be the number of t,u
that Q-neighbor w, and let k be an upper bound for the number of
zeros in Z minus {q0} that Q-neighbor w. Since w is full, its six
retained old neighbors consist of h full endpoints, at most k+epsilon
zeros, and ordinary positive vertices. Thus it has at least
6-h-k-epsilon ordinary positive retained neighbors.

Consider any such neighbor r. Its sole original two-step route to
v was r-w-v, and wv was deleted. Vertex r has no addition; v's sole
addition is vq0. Except when rq0 is a Q edge, the pair rv has no
replacement old route or direct added edge. Hence it must be repaired
through the new vertices, forcing B_r={c}.

There are at most 1-epsilon exceptions among these r: if w and q0
are adjacent, they have no common Q neighbor; otherwise they have
exactly one. Therefore at least

\[
F=6-h-k-\epsilon-(1-\epsilon)=5-h-k               \tag{3}
\]

ordinary old vertices besides v have label c. The new vertex c
has at least 1+F old neighbors. Its exact total degree eight gives

\[
d_H(c)\le7-F.                                     \tag{4}
\]

## New-label reach from v

Every ordinary positive retained Q neighbor r of v has its sole
label in B_w. Its old pair with full w originally had the unique
route r-v-w, now broken; both r and w have no additions, so only a
shared new neighbor can replace it. Zero neighbors contribute no
label, and the added neighbor q0 contributes none.

If v has no Q neighbor among t,u, every old intermediary from v
therefore supplies a label in B_w, a set of size two. If v has a
Q neighbor x in {t,u}, the old labels lie in B_w union B_x. Moreover
B_w intersects B_x: the old pair x,w lost its unique route x-v-w,
and both endpoints are full with no additions. In this case their
union has size at most three.

The complete set of new vertices reachable from v within two steps
is consequently contained in

\[
\{c\}\cup N_H(c)\cup B_w
\]

or, when the cross neighbor x exists, in the same set with B_x
included. We now apply (3)-(4) in all possible deletion positions.

## The three positions all contradict eight-label coverage

Two disjoint Q edges have at most one cross edge. Two cross edges
sharing an endpoint make a triangle; two disjoint cross edges make
a four-cycle. There are therefore exactly three cases up to swapping
t,u and the descriptions below.

1. **No cross edge.** Here h=0. Since w has a unique common Q
   neighbor with each of t,u, (2) gives k<=2. Formula (3) gives
   F>=3 and hence d_H(c)<=4. Vertex v has no full old neighbor,
   so its new reach has size at most 1+4+2=7.

2. **The cross edge meets w**, say wt. Here h=1 and k=0. No point
   of T neighbors w, by triangle-freeness; the unique common neighbor
   of w,u is t, which is not in U, so no point of U neighbors w
   either. Thus F>=4 and d_H(c)<=3. Vertex v has no other full
   neighbor, giving at most 1+3+2=6 new labels.

3. **The cross edge meets v**, say vt. Here h=0 and k<=1. The
   unique common neighbor of w,t is v, which is positive, so it
   supplies no zero in T; there is at most one zero common neighbor
   of w,u. Thus F>=4 and d_H(c)<=3. The possible full neighbor t
   supplies B_t, but B_t intersects B_w as proved above. The total
   new reach is at most 1+3+3=7.

Each case misses at least one of the eight new vertices, contradicting
diameter two. Hence the disjoint-D, a=6, E=3 branch is impossible.
No candidate is removed by fixing an auxiliary graph, a particular
matching, a port-pair pattern, or a position of q0. This proof addresses
the requested three-full branch; other excess patterns require their
separate arguments.
