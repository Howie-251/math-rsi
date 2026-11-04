# A conditional finite route for the six remaining root-star geometries

2026-11-02. ARIS proof-writer candidate. The universal finite A witness
obligation below is OPEN. This file proves a proposed reduction, not Q6.

## Original domain

Use the accepted235-record residual and its six normalized representatives:
u=0, v=31, W={1,2,4,8,16,32}, and Z one of

1. {39,43,45,51,53};
2. {39,43,45,51,63};
3. {39,43,45,54,63};
4. {39,43,51,60,63};
5. {39,43,53,57,63};
6. {39,43,53,58,63}.

Let A be the face with bit32 zero, B the other face, and J={1,2,4,8,16}.
Identify A with Q5 and write bar(x)=x xor32. The original holes are
{u} union Z union W. Let M be any realizing short26-edge matching and
L=M internal to A. Put T={bar(z):z in Z}. Every t in T is originally
A-covered and cannot be a crossing port, because its actual short mirror
is a B hole. Thus L covers every vertex of T. A's original covered graph
G is Q5 induced on the15 nonzero even vertices and the11 odd nonunit
vertices. The graph G and T depend only on the displayed representative.

Extend L by ADDING short edges of G to any inclusion-maximal matching
L* of G. Original edges are never changed. Necessarily |L*|<=11 and
its unmatched even vertices number15-|L*|>=4. The candidate finite
enumeration must cover every such L* containing all of T, not a sample.

## The finite positive A obligation

For every inclusion-maximal L* of G covering T, supply:

- q: an unmatched even vertex of G;
- t in T minus {v}, adjacent to q;
- distinct w,b in J, and S=J minus {w,b};
- a legal short forest P on A minus {u,v} with degree one at
  K=A minus {u,q,v,b}, degree two at q,b, no cycle, and edge q-t;
- an accepted B marked input as specified below.

Define L*' by replacing v-h* with w-h* if v is covered by L*, where
h*=L*(v); otherwise put L*'=L*. Require the labelled union P+L*'
to be acyclic. Duplicate required/forest edges count as two-edge cycles.
This positive condition is what must be verified for EVERY enumerated L*.
Neither a deficient rank nor finite random tests establish it.

Let X* be the vertices of G unmatched by L*. Define X*'=X* when v is
covered, and X*'=(X* minus {v}) union {w} otherwise. The path endpoints
of P+L*' are exactly Q*=(X*' minus {q}) union S. Their even/odd counts
are equal: the original unmatched-port surplus is four even vertices,
then q removes one even and S adds three odd vertices. The union has
at least three path components because |X*|>=4 and |Q*|=|X*|+2>=6.

Any bipartite path forest with balanced endpoint counts and at least
three components admits an opposite-parity matching D* of its endpoints
joining all components into one cycle. Indeed orient each even-odd
component consistently and arrange the even-even and odd-odd components
alternately (their numbers are equal), inserting the even-odd components
between them. Pair consecutive exposed ends cyclically. If there are
no same-parity components, orient all components from even to odd and
join cyclically. All added pairs are opposite-parity and join distinct
components, so no two-edge component is created. Hence
C_A=P union L*' union D* is a cycle on A minus {u,v}, with edge q-t.
D* need not be short; every such completion edge will be deleted.

## Why maximal internal matchings suffice

Let h=M(v) be the ACTUAL target mate. Replace original edge v-h in the
global matching by the auxiliary edge w-h, obtaining F. If h is in A,
its internal part L' is L minus {v-h} plus {w-h}. If h is in B then
h=63, L'=L, and the actual crossing v-h is replaced by a virtual crossing
w-h. This is the only potentially long crossing and will be removed
at the final step. Its endpoints, not its direction, are used in gluing.

In every case L' is a submatching of L*'. If v was already L-covered,
its mate cannot change in an extension. If v was originally unmatched
in A but becomes covered by L*, the artificial edge w-h* is simply a
completion pair; no original edge is asserted there. Thus
D=D* union (L*' minus L') is a matching and C_A=P union L' union D.
Its endpoint domain is exactly Q=(X' minus {q}) union S, where X' is
the actual A crossing-port set after the possible replacement v by w.
All added L*' minus L' edges may be treated as completion edges. This
also handles the case of an originally crossing v that becomes internally
matched only in L*. Therefore a certificate for L* supplies the required
A cycle for its original submatching L without changing the original M.

The chosen t belongs to T minus {v}, so it was internally L-covered
even before maximalization. The chosen q remains an actual even crossing
port. This distinction is essential for the next opening operation.

## Open the A cycle and form the exact B input

Delete every edge of D AND the short edge q-t from C_A. These edges
are disjoint: D avoids q, and t is covered by L'. A nonempty proper
edge deletion from a single cycle is a path forest. Attach all actual
F crossings, including the possible long w-63 edge, the three new short
bridges s-bar(s) for s in S, and the new short bridge t-bar(t).

At q, deleting q-t makes room for its original crossing. At t, its
original internal required edge remains, and deleting q-t makes room
for t-bar(t). The vertex bar(t) is an original B hole in Z and is now
consumed; it is not a conflict vertex. Each Y={bar(s):s in S} is an
original internally B-covered vertex, not a port or original hole.
The only conflicts are at these three same-parity Y vertices. Their
original short mates are distinct opposite-parity pendant endpoints
outside every transferred endpoint. Suppress these three conflicts as
in the accepted uniform transfer, retaining their expansion paths.

The resulting arbitrary B matching has holes
{32} union (Z minus {bar(t)}) union Y, with precisely Y omitted by the
desired local cycle. This is T17: one minority hole32, seven majority
holes, and three marked majority omissions. The only remaining short
neighbors of32 after omitting Y are p=bar(w), r=bar(b). Both remain
originally internally B-covered and outside the transferred endpoints,
Y and bar(t). This remains true for a virtual w-63 crossing:63 differs
from these weight-two vertices. Their original B edges are unchanged
and short, so the compressed matching cannot contain the same-parity
edge p-r. Thus an accepted exact local classification with obstruction
p-r supplies the B cycle. The finite witness must verify the simultaneous
marked geometry against an ACCEPTED B registry; no unrestricted T17
claim is used.

Expanding yields a cycle on Q6 minus {u,v} containing the whole modified
matching F, with only short physical edges apart from the auxiliary w-h.
Delete w-h, prepend u-w and append h-v to the resulting Hamilton w--h
path. This gives the desired Hamilton u--v path on all64 vertices,
preserving all original M edges and adding only cube edges.

## Remaining proof obligations

The mathematical reduction requires fresh independent audit, including
the maximalization lift and the covered-source bridge. Its finite premise
still requires exhaustive inclusion-maximal L* enumeration for the six
T sets, with a positive q,t,w,b,P witness for EACH case, and independently
verified B registry transports. Existing force-opening rank8031/7998
files contain useful legal forests, but prove no universal A statement.
A deterministic complete witness cover could suffice even though no
full-rank arbitrary-matching opening theorem has been obtained.

No235-record decrement, complete twelve-hole theorem, or full P6 closure
is asserted by this conditional reduction.
