# HS58: exclusions with few excess ports

Date: 2026-10-12. Let Q be HS50, delete two original edges D, add a
original nonedges A and eight new vertices. Assume degree eight and
diameter two. This note concerns a>=6, with H and all attachments free.
Its arguments use no enumeration or SAT.

Use M=Q-D+A, r_v=d_D(v), a_v=d_A(v), p_v=1+r_v-a_v,
Z={v:p_v=0}, e_v=max(p_v-1,0), E=sum e_v, and T={v:e_v>0}.
Write m=e_Q(Z), d=e_D(Z), R=sum_(v in Z)r_v, and b=e_A(V(Q) minus Z).
From the [general addition bound](HS58_TWO_DELETE_GLOBAL_ADDITION_BOUND.md),

\[
z=E+2a-4,\qquad
e_A(Z)=a+E+R-4+b,\qquad
2e_M(Z)\le W:=\sum_{t\in T}e_t d_M(t,Z).             \tag{1}
\]

The underlying row inequality is

\[
d_M(q,Z)\le\sum_{t\in N_M(q)}e_t\quad(q\in Z).       \tag{2}
\]

In particular every endpoint of an A[Z] edge must have a neighbor in T.
Every ordinary zero (outside the deletion endpoints) has addition degree
one. Every positive-port ordinary vertex has addition degree zero.
HS has no triangle or four-cycle; adjacent pairs have no common Q
neighbor, and nonadjacent distinct pairs have exactly one.

## E=1 is impossible for a>=6

There is one excess vertex t, with p_t=2 and d_M(t)=6. The general
bound m+a<=4+2E-R+d immediately gives a<=6, so equality is required.
It forces m=0 and R-d=0. Since R=2d+e_D(Z,Z-complement), this implies
R=d=0. Thus all zeros are ordinary. Equation (1) now gives

\[
3+b=e_A(Z)=e_M(Z)\le3.
\]

Hence b=0, A[Z] consists of three disjoint edges, and all six old
neighbors of t lie in Z. By (2), the six endpoints of A[Z] must all
be neighbors of t. They therefore equal N_M(t).

If r_t=2, then a_t=1. Its unique added neighbor q lies in Z because
b=0. But q is ordinary and its sole addition joins the positive vertex
t. Since Q[Z] is independent, q has no M neighbor in Z and is not an
endpoint of A[Z]. This contradicts q belonging to N_M(t).

If r_t=1, then a_t=0. Write ty for its deleted edge. Vertex y is
positive, nonexcess, so p_y=1 and its added neighbors all lie in Z
(there may be two when y is the shared deletion endpoint). Choose an
A[Z] endpoint q; its partner q' is also in N_Q(t). The original unique
route from q to y was q-t-y and has been deleted. There is no new
intermediary because q has zero ports. A replacement old route cannot
use an added neighbor w of y: w lies in Z, Q[Z] is independent, and
w cannot have a second added edge to q because it is ordinary with
addition degree one. The only other possible route is q-q'-y with
q'y in Q. This would give the Q triangle t-q'-y, a contradiction.
The direct q-y addition is also impossible because q's unique added
neighbor q' lies in Z and y is positive. This exhausts the repairs.

Together with the general E=0 bound, every a>=6 candidate has E>=2.

## A sole weight-two excess vertex allows at most four additions

If E=2 and T={x} with e_x=2, then x is the common endpoint of
adjacent deletions, p_x=3 and a_x=0. Its five retained old neighbors
are all ordinary. Every A[Z] endpoint belongs to these five neighbors
by (2), and has addition degree one. Consequently A[Z] is a matching
of at most two edges. Equation (1) gives

\[
a-2+R+b=e_A(Z)\le2,
\]

so a<=4. This closes this excess pattern for every a>=5, regardless
of which deleted leaves themselves have zero ports.

## Two weight-one excess vertices cannot be nonadjacent in Q

Let E=2, T={t,u}, e_t=e_u=1, and assume t,u are nonadjacent in Q.
Both have deleted degree one and no addition. Indeed a deleted-degree
two vertex is adjacent to every other deletion endpoint. Let c be the
unique common Q neighbor of t,u. Between N_Q(t) minus {c} and
N_Q(u) minus {c}, Q has exactly a perfect matching of six edges:
each point in the first set has a unique common neighbor with u;
it is neither t nor c, and the same argument in reverse proves
bijectivity. Neither six-set has internal edges.

If k_t=|N_Q(t) intersect Z| and k_u is defined similarly, choosing
points from those six matched pairs therefore gives

\[
W\le k_t+k_u\le m+6+2\mathbf1_{c\in Z}\le m+8.      \tag{3}
\]

On the other hand, (1) gives

\[
W\ge2e_M(Z)=2(m-d+a-2+R+b).
\]

For a>=7 these inequalities contradict m>=0, R-d>=0 and b>=0.
For a=6 they force m=R-d=b=0 and W=k_t+k_u=8. Hence R=d=0,
c lies in Z, and exactly six further points of N_Q(t) union N_Q(u)
lie in Z. There are only seven available zero vertices neighboring T.
But A[Z] has four edges on eight distinct ordinary zeros, and every
one must neighbor T by (2). This is impossible.

## Two weight-one excess vertices cannot form a retained cross edge

Here the deletions are disjoint, D={tx,uy}, with tu an original
retained cross edge, and T={t,u}. Both excess vertices have no
addition. The only possible positive-port addition endpoints are
x and y. Every endpoint q of A[Z] must neighbor t or u in Q. It
cannot be x or y: each lost its possible neighbor in T, and a second
Q adjacency to T would create a triangle. Thus q is ordinary, has
one A neighbor q' in Z, and is adjacent to exactly one of t,u.
Equation (2) forces q to have no Q neighbor in Z.

Say q neighbors t. Its unique original route to x was q-t-x.
A new intermediary is unavailable. Repair through q' would require
q'x in Q, since q' already uses its only A edge. Yet q' also neighbors
t or u. The first option gives a triangle with tx; the second would
make q' a second common neighbor of u and x, whose common neighbor
is already t. Both are impossible.

Alternatively a repair could use an added neighbor w of x. If w is
zero, q cannot neighbor it in Q. If it is positive, it must be y;
but q cannot neighbor both t and y, whose unique common neighbor is
u. A two-added-edge route would again give its ordinary zero
intermediary addition degree two. Direct q-x is incompatible with
q's existing A[Z] partner. There is no repair. Thus A[Z] is empty,
contradicting e_A(Z)>=a-2 for a>=6.

## Adjacent D with two weight-one excess vertices

By the preceding nonadjacent exclusion, write D={xy,xz} and
T={x,y}, with center x. Their ports and additions are
p_x=p_y=2, a_x=1, a_y=0. The other leaf z has p_z<=1.

The only possible positive-port A endpoints are x and, if positive,
z. The edge xz is original and cannot be added, so b=0. If z were
zero, its two A neighbors would both lie in Z, but it has no M
neighbor in T: xz was deleted, yz is not a Q edge, and y has no A.
This contradicts (2). Therefore z is positive, with one A neighbor
q_1 in Z, and x has one A neighbor q_0 in Z.

All zeros are ordinary. The at least a-2 edges of A[Z] form a
matching, and their endpoints are distinct from q_0,q_1. Each such
endpoint q must neighbor x or y in Q, but not both since xy is a
Q edge. Its one excess neighbor and its A[Z] neighbor exhaust (2),
so q has no Q neighbor in Z.

If q neighbors x, repairing the lost pair q,y forces its A partner
q' to neighbor y in Q, since y has no additions. Repairing q,z
through that same partner would require q' to neighbor z too;
the unique common neighbor of y,z is x, which q' is not. Repair
through the added edge zq_1 would require q to neighbor q_1 in Q,
also impossible. No direct or two-added-edge repair exists for
ordinary zeros of A degree one.

Thus no A[Z] endpoint neighbors x. The remaining ones all neighbor
y. Repairing their lost pair with x would require either their
A partner to neighbor x (just excluded), or a Q edge to q_0
(forbidden by their zero-neighbor bound). Again no repair exists.
This contradicts the nonempty A[Z] required by a>=6.

## Adjacent D with three weight-one excess vertices

Now D={xy,xz} and T={x,y,z}, all with p=2. Only x has an A edge,
joining a zero q_0. All zeros are ordinary, b=R=0, and A[Z] is a
matching of size a-1. For any endpoint q of this matching, its
neighbor in T must be a Q neighbor (its sole A neighbor is zero).

If q neighbors x, the two lost routes to y and z would force its
sole A partner to neighbor both leaves in Q. Their unique common
neighbor is x, which is not zero. Hence this case is impossible.
Every remaining endpoint neighbors y or z. To repair its lost route
to x, a route through its A partner would require that partner to
neighbor x, already excluded. The only other route uses xq_0, so
q must neighbor q_0 in Q. For each of y and z there is at most one
such common Q neighbor with q_0. Thus the A[Z] matching has at most
two endpoints, contradicting its 2(a-1)>=10 endpoints.

## Scope of the deductions

For a>=6, E=0, E=1 and the sole-weight-two E=2 pattern are impossible.
If E=2 consists of two weight-one vertices, they must be the endpoints
of a deleted edge; the adjacent-D case is impossible too. Thus the
only possible E=2 setting left by this note is a pair of full endpoints
of one of two disjoint deletions. E=3 and E=4 need their separately
stated results; this note alone does not exclude all two-deletion
extensions or arbitrary 58-point graphs.
