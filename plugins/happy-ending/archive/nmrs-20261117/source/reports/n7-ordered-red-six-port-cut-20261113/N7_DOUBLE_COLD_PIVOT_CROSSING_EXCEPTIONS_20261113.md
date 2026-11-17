# A double-cold pivot has an empty inner crossing rectangle

Date: 2026-11-13. Status: complete same-session analytic working proof,
independently self-checked within the current author session; **no external
review and no acceptance of the original global upper bound**. This proof
does not depend on the 12-, 14-, or 22-point SAT experiments in this directory.

## 1. Exact ambient setting

Let X be one complete ordered rank-3 signotope with no red seven-path,
no blue six-path, and no weak7. A path is an increasing sequence whose
consecutive triples have its color; length counts vertices. Weak7 forbids
opposite-color paths with the same actual outer endpoints and total length
at least nine. None of the arguments below requires an additional interior
disjointness hypothesis.

Write S for the actual ambient red-six sources and E for the actual ambient
red-six terminals. Let c be **double cold**: no ambient blue four-path ends
at c and no ambient blue four-path starts at c. Membership c in S intersect E
is not needed for the local theorem, although it can be supplied by a caller.

Two elementary actual-hat rules will be used. If
R6(l1,l2,l3,l4,l5,e) is real, then chi(l5,e,y)=B for every y>e,
since red would append y and form R7. If R6(s,r2,r3,r4,r5,r6) is real,
then chi(x,s,r2)=B for every x<s, since red would prepend x and form R7.
All selected vertices in the displayed paths below are distinct and have
the displayed strict order.

## 2. The common strong/short branches

Suppose R5(e,p,c,q,s) is an actual red path, e has an actual incoming R6,
and c cannot end B4. Fix L=R6(l1,l2,l3,l4,l5,e).
Then at least one of the following actual paths exists:

1. Strong left: R6(l1,e,p,c,q,s).
2. Short left: R5(l5,p,c,q,s).

Indeed, inspect chi(l4,l5,p). If it is red, replacing the final vertex e
of L with p gives R6(l1,l2,l3,l4,l5,p). Weak7 with the same endpoints
(l1,p) then forces chi(l1,e,p)=R, yielding the strong-left path.
If chi(l4,l5,p)=B, then chi(l5,p,c) must be red: blue would give the
forbidden B4(l4,l5,p,c) ending at c. This gives the short-left path.

The completely reversed argument, using an actual outgoing
R=R6(s,r2,r3,r4,r5,r6) and the prohibition on B4 starting at c,
gives at least one of:

1. Strong right: R6(e,p,c,q,s,r6).
2. Short right: R5(e,p,c,q,r2).

For clarity, the right split is chi(q,r2,r3). In its red branch,
R6(q,r2,r3,r4,r5,r6) and weak7 force chi(q,s,r6)=R. In its blue
branch, chi(c,q,r2)=R follows from the prohibition on B4(c,q,r2,r3).
These are actual branches on the same fixed red core (p,c,q), so their
supplies may be combined without changing any chosen path or endpoints.

This rederives, rather than assumes, the strong/short argument of
[the ordered cold-arm proof §2](../../.trellis/tasks/10-19-nr7-structure-capacity/research/N7_NEUTRAL29_ORDERED_COLD_ARMS_20261112.md).

## 3. A red five with this endpoint supply is impossible

**Lemma.** There is no actual R5(e,p,c,q,s) with e in E, s in S,
and c double cold.

**Proof.** Fix the actual L and R above. Apply both branch arguments of §2.
Their four possible combinations are all impossible:

| Left/right supply | Actual red path obtained | Contradiction |
|---|---|---|
| strong / strong | R7(l1,e,p,c,q,s,r6) | red-seven prohibition |
| strong / short | R6(l1,e,p,c,q,r2) | same-endpoint B3(l1,s,r2) |
| short / strong | R6(l5,p,c,q,s,r6) | same-endpoint B3(l5,e,r6) |
| short / short | R5(l5,p,c,q,r2) | same-endpoint B4(l5,e,s,r2) |

In the second row, chi(l1,s,r2)=B is the true outgoing hat at s.
In the third, chi(l5,e,r6)=B is the true incoming hat at e.
In the final row, both consecutive blue triples are true hats:
chi(l5,e,s)=B and chi(e,s,r2)=B. The opposite-color lengths in all
three rows sum to nine, with exactly the same actual outer endpoints.
Each red path uses only consecutive triples already supplied by its two
branches; no unsupported bridge between unrelated path witnesses appears.
Thus every branch is excluded. QED.

## 4. The empty inner rectangle for actual crossing red sixes

**Theorem.** Fix any e<p<c<q<s with e in E and s in S. Then
chi(p,c,q)=B, and there is no actual ambient red-six path with outer
endpoints (p,q).

**Proof.** Take the real incoming hat at e, with penultimate point f.
It forces chi(f,e,p)=B. If chi(e,p,c) were blue,
B4(f,e,p,c) would end at c, so chi(e,p,c)=R.
Likewise, take the real outgoing hat at s, with second point t.
It forces chi(q,s,t)=B. If chi(c,q,s) were blue,
B4(c,q,s,t) would start at c, so chi(c,q,s)=R.

If chi(p,c,q)=R, these two forced triples and the supposed red middle
triple form exactly R5(e,p,c,q,s), excluded by §3. Hence chi(p,c,q)=B.
An R6 with endpoints (p,q) would share its endpoints with the actual
B3(p,c,q), violating weak7. QED.

In particular, for any fixed actual e in E and s in S with e<c<s, the
entire open endpoint rectangle (e,c) times (c,s) contains no crossing R6.
The outer vertices e,s can be chosen separately for each application;
the proof never requires uniform left or right red-six suppliers.

## 5. Exact outside-endpoint cover and remaining global obligation

Suppose E and S are nonempty, and put a=min E and b=max S.
When a<c<b, every red six strictly crossing c has source p<=a or
terminal q>=b, since a<p<c<q<b is excluded by §4. Consequently the
actual physical set

    C_out = (S intersect (-infinity,a]) union (E intersect [b,infinity))

hits every red six strictly crossing c. More generally, the same formula
with any e in E before c and s in S after c gives a valid, possibly larger,
outer-endpoint cover. This proves a cover, not an unproved bound on its size.

For an exact conditional global statement, let C_side be any actual physical
set of at most 11 points hitting every R6 strictly to one side of this same
c. Then

    C_side union {c} union C_out

hits every ambient R6: the three cases are strictly same-side, containing c,
and strictly crossing c. Its size is at most 12+|C_out|. Therefore the
desired 25-point cover follows **if |C_out|<=13 and if that same-side cover
can be chosen at this double-cold c**. Neither condition is established here.
In particular, a previously chosen center z cannot simply be declared equal
to c; nor does the empty inner rectangle bound the number of outside endpoints.

The earlier proposal to pay at most three deep exceptions on each side is
unnecessary for the open inner rectangle: its crossing paths are all absent.
That does not remove the outside-endpoint obligation. This standalone proof
closes only the local red-five exclusion, the exact empty rectangle, and the
displayed conditional physical covering interface.

## 6. Exact gluing after an arbitrary outside-path cover

Keep a=min E<c<b=max S. Let Y be any actual physical set hitting **every**
R6 whose source is at most a or whose terminal is at least b, including
paths wholly to one side of c. Y need not consist of endpoints: internal
vertices are allowed. The explicit outer-endpoint set C_out of §5 always
meets this premise, including for wholly one-sided outside paths.

Every R6 surviving deletion of Y has both endpoints in (a,b). By §4 it
cannot strictly cross c, so it lies wholly in exactly one of the closed
wings

    W_L = X intersect (a,c],       W_R = X intersect [c,b).

Their surviving vertex sets meet only at c when c is not in Y. For any
finite induced domain W, write tau(W) for its red-six transversal number.
Let T_Y be the minimum size of a transversal of all ambient R6 that is
required to contain all of Y.

If c is not in Y, define, for j=L,R,

    m_j = tau(W_j minus Y),
    k_j = tau(W_j minus (Y union {c})),
    f_j = minimum size of a transversal of W_j minus Y that avoids c.

The two exhaustive choices, selecting or avoiding c, give the exact formula

    T_Y = |Y| + min(1+k_L+k_R, f_L+f_R).                 (G1)

Indeed, after selecting c the remaining two domains are disjoint and need
exactly k_L+k_R further vertices. When c is forbidden, the two available
vertex sets are disjoint and need exactly f_L+f_R. Points outside the two
wings hit no surviving path and cannot improve either minimum. This proves
both the lower bound and an actual construction attaining (G1); independent
local solutions need no compatibility beyond their sole shared point c.

Put epsilon_j=m_j-k_j. Deleting one vertex lowers a transversal number by
zero or one, so epsilon_j is in {0,1}. Moreover,

    epsilon_j=1  iff some minimum transversal of that closed wing contains c.

To see the equivalence, the minimum cost among its transversals containing
c is exactly 1+k_j, while m_j=min(1+k_j,f_j). Thus (G1) simplifies to

    T_Y = |Y| + m_L+m_R - epsilon_L*epsilon_R.           (G2)

If both epsilons are one, minimum covers of both wings may contain c and
their union saves exactly this shared point. If both are zero, avoiding c
attains m_L+m_R and saves one against unnecessarily selecting c. If exactly
one is one, selecting c attains m_L+m_R: its extra unit in the other wing
cancels the overlap saving. These cases also cover an empty wing or a wing
with no R6; such a wing has m=k=f=0 and epsilon=0.

If c is already in Y, its cost has already been paid and the exact formula
is simply

    T_Y = |Y| + tau(W_L minus Y) + tau(W_R minus Y).      (G3)

In particular, suppose c is not in Y and the independent closed-wing sum
is |Y|+m_L+m_R=26. The best transversal **forced to contain Y** has size 25
if and only if epsilon_L=epsilon_R=1; otherwise its size is exactly 26.
This is the precise net-one test. It does not rule out a smaller global
transversal that omits some points of Y.

Using the separately supplied balanced capacity 49, a sufficient criterion
for n<=74 is that the right-hand side of (G2), or of (G3) when applicable,
is at most 25: deleting the constructed transversal leaves at most 49
points. This corollary assumes neither z=c nor a bound on |Y| or either
wing minimum. To conclude the general 74 bound, those actual numerical
conditions still have to be proved for an admissible Y in every required
input class. No such global numerical assertion or external review is
added by this gluing lemma.

An equivalent path-supply test is useful. epsilon_L=1 precisely when
**every** minimum transversal of the open left wing W_L minus (Y union {c})
misses at least one actual R6 in W_L minus Y ending at c. Mirror this for
epsilon_R=1 using actual R6 starting at c. Indeed, a minimum open-wing
transversal that also hits every surviving c-incident path is a closed-wing
transversal of size k_j, and conversely every size-k_j closed-wing
transversal must avoid c and is such an open-wing minimum. The universal
quantifier over open-wing minima is essential; one failed minimum does not
prove epsilon_j=1. All paths in this test must survive deletion of Y.
