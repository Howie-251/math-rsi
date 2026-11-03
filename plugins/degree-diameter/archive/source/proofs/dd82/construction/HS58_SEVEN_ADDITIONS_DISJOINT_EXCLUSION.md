# HS58: seven additions with disjoint deletions are impossible

Date: 2026-10-12. Pure combinatorial proof, with arbitrary auxiliary
H and arbitrary original-nonedge additions. No SAT, enumeration, or
assumed auxiliary type is used. Together with the separate adjacent-D
argument, this closes the seven-addition count. This file proves the
entire disjoint-D case and a useful adjacent excess pattern.

Use the notation of `HS58_TWO_DELETE_GLOBAL_ADDITION_BOUND.md`:
Z is the zero-port set, z=|Z|, e_t=max(p_t-1,0), E=sum e_t,
m=e_Q(Z), r(Z)=sum_(q in Z)d_D(q), d=e_D(Z), and M=Q-D+A.
Set R=r(Z)-d and b=e_A(V(Q) minus Z). For every zero q,

\[
d_M(q,Z)\le\sum_{t\in N_M(q)}e_t.                 \tag{1}
\]

This is the necessary count of eight new labels through old
neighbors. The exact addition count and its summed consequence are

\[
e_A(Z)=z+r(Z)-a+b,\qquad
2e_M(Z)\le W:=\sum_t e_t d_M(t,Z).                 \tag{2}
\]

For disjoint D every positive excess is one, occurs at a deletion
endpoint of port count two, and has addition degree zero. Such an
endpoint is called full below. For a=7, the existing global bounds
give E>=2. E=4 is excluded by
`HS58_SATURATED_DISJOINT_ALL_ADDITIONS.md`, which bounds a by six
in that case. Only E=2 or E=3 remains.

## Two excess endpoints

Here z=12, exactly two endpoints t,u are full, and

\[
e_M(Z)=m+5+R+b,\qquad
10+2m+2R+2b\le W\le12.                            \tag{3}
\]

Thus m+R+b<=1. Write k_t=|N_Q(t) intersect Z|, and similarly k_u.

The general two-excess arguments in
`HS58_TWO_DELETE_SMALL_EXCESS_EXCLUSIONS.md` exclude nonadjacent
t,u and a retained Q edge tu for every a>=6. Therefore only the
case that tu itself is a deleted edge remains.

The other deleted edge
is xy. At most one of x,y is zero: if both were zero, their original
edge would give m>=1 and R>=1, contradicting (3). Moreover b=0.
Indeed the only possible positive addition endpoints are x,y; when
both are positive their mutual edge is an original edge and cannot
be added, and when one is zero there is only one positive addition
endpoint.

The two six-sets

\[
T=N_Q(t)\setminus\{u\},\qquad U=N_Q(u)\setminus\{t\}
\]

are disjoint and their union is independent: edges within either
make a triangle, and edges across them make a four-cycle through tu.
If m=1, equation (3) forces k_t=k_u=6, so Z=T union U is independent,
a contradiction. If R=1, then m=0 and again Z=T union U. Exactly one
endpoint, say x, is zero. Formula (2) gives six internal additions
and one crossing addition from the positive endpoint y to some
zero q. This q is not x, since xy is an original edge, so q has
addition degree one. If q is in T, its broken route to u forces
its added partner y to be Q-adjacent to u. But every neighbor of u
other than t is in Z and y is positive, impossible. The U case is
symmetric.

Finally m=R=0, so Z is independent and k_t+k_u>=10. Put
l=|Z minus (T union U)|=12-k_t-k_u, hence 0<=l<=2. Let h_t,h_u
be the numbers of omitted vertices of T,U; h_t+h_u=l. Any zero
outside T union U has a unique common Q neighbor with each of t,u.
Those two common neighbors must be omitted vertices, since Z is
independent. Different outside zeros cannot give the same pair of
omitted vertices, because two vertices of Q have at most one common
neighbor. Thus

\[
l\le h_t h_u\le\lfloor l^2/4\rfloor.
\]

For l=1 or 2 this is impossible, so l=0 and Z=T union U. Both x,y
are positive, and the two crossing additions from x,y end at ordinary
zeros. Each such zero's broken path to the opposite full endpoint
again requires its positive added partner to belong to T or U,
although both sets consist entirely of zeros. This contradiction
finishes E=2.

## Three excess endpoints

Now z=13. One deleted edge, say tu, has both endpoints full; write
the other as wv with w full and v not full. The only possible
positive addition endpoint is v, when it is positive.

If v is zero, it has two additions, both to zeros. It has no retained
edge to w, and can Q-neighbor at most one of t,u because tu is an
original edge. No full endpoint has an addition. Consequently
d_M(v,Z)>=2 while the right side of (1) is at most one. This is
impossible.

Therefore v has one port and one addition vq0, where q0 is zero.
All remaining additions are six A[Z] edges on the other twelve
zeros, each an ordinary vertex of addition degree one. If an A[Z]
endpoint q Q-neighbors t, its broken original route to u forces its
added partner q' to Q-neighbor u, since u has no addition and q
has no port. The converse and the interchange t/u hold as well.
Each A[Z] edge therefore either joins a t-neighbor to a u-neighbor,
or has both endpoints outside N_Q(t) union N_Q(u).

The latter alternative is impossible. For such an endpoint q,
equation (1) and its internal added edge force it to Q-neighbor w,
and force its Q[Z] degree to be zero. The same holds for q'.
Its original q-w-v route has been broken. A replacement through
q' would require q' Q-adjacent to v, a triangle with wv because q'
also Q-neighbors w. A replacement through v's added neighbor q0
would require a Q edge q-q0 within Z, contrary to its zero Q[Z]
degree. There is no new intermediary or direct added edge qv.

All twelve A[Z] endpoints are consequently in the disjoint six-sets
T=N_Q(t) minus {u} and U=N_Q(u) minus {t}. They fill T union U
exactly, and q0 is outside it. This also forces w,v outside T union U;
in particular a cross edge between the deletions cannot occur.

The unique common Q neighbor of q0 with t lies in T, and the unique
common neighbor with u lies in U. They are distinct zeros. Thus
d_M(q0,Z)>=2. But q0 Q-neighbors neither t nor u, its added neighbor
v has only one port, and it can neighbor only the one remaining
excess vertex w. The right side of (1) is at most one, giving the
final contradiction. This closes E=3 and all disjoint-D a=7 cases.

## Adjacent excess pattern (2,1), for every a>=6

For use with the separate adjacent-D proof, suppose D={xu,xv},
with x of port count three, u of port count two, and no other excess.
Then A_x=A_u=0 and v has either one port and addition degree one,
or zero ports and addition degree two. Its entire added neighborhood
T_v is in Z, because there is no other positive addition endpoint.

Take q in N_M(x) intersect Z. It is ordinary and has one addition,
to q'. Repairing its broken route to u forces q' Q-adjacent to u.
Its route to v cannot be repaired through q', since that would make
q' a common neighbor of u,v, whose unique common neighbor is x.
Nor can q'=v repair the route to u, since u,v are nonadjacent.
It follows that q must Q-neighbor some vertex of T_v. Each member
of T_v has at most one common Q neighbor with x, hence

\[
d_M(x,Z)\le |T_v|=a_v,\qquad W\le2a_v+6.
\]

If v is positive, r(Z)=0 and a_v=1. If v is zero, r(Z)=1 and a_v=2.
In either case d=e_D(Z)=0 and a_v=1+r(Z). Formula (2) gives
e_M(Z)>=a-1+r(Z). Thus

\[
2a-2+2r(Z)\le W\le8+2r(Z),
\]

forcing a<=5. This excludes the entire adjacent weight-(2,1)
branch for a>=6, independently of H and independently of the
seven-addition disjoint proof above.
