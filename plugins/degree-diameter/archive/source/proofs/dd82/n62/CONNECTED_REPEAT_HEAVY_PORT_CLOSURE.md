# Connected repeat support forbids complete saturation of heavy ports

## Claim and status

**PROVABLE AS STATED.** New paper proof awaiting independent review.
In the actual connected-repeat order-62 case, let $d$ be the number
of double-repeat pairs and let $L_3$ count vertices with three heavy
endpoints as their unit repeat neighbors. Then

$$\boxed{3L_3<2d},\qquad
\boxed{L_3\le\left\lfloor\frac{2d-1}{3}\right\rfloor}.\tag{1}$$

Consequently the mixed-trace bound improves to

$$
\boxed{\tau\le248-24d+
2\left\lfloor\frac{2d-1}{3}\right\rfloor},
\qquad \tau=\operatorname{tr}(AB^2).
\tag{2}
$$

In particular, if $d=9$, then $\tau\le42$ and the number $c_5$ of
unoriented original five-cycles satisfies

$$\boxed{2498\le c_5\le2501}.\tag{3}$$

This does not require an assumption about the number of type-one
nongenerated unit triangles. It does not exclude the $d=9$ case.

## Assumptions and notation

Use the actual order-62 graph, the exact repeat matrix
$B=A^2+A-7I-J$, and connected positive repeat support. The established
connected-case reductions give triangle-freeness of $G$, $B\le2$,
only D1 double repeats, and

$$d\in\{1,3,5,7,9\}.$$

Let $D$ be the set of $2d$ heavy endpoints. Every $x\in D$ has a
unique heavy mate $h(x)\in D$ and a unique unit mate $a(x)$, with

$$B_x=2e_{h(x)}+e_{a(x)}.$$

The established D1 light-mate theorem puts $a(x)$ outside $D$ and
outside the union $S$ of the generated unit triangles. The global
disjointness theorem gives $|S|=3d$ and $S\cap D=\varnothing$.
Put $W=V(G)\setminus(D\cup S)$, and for $w\in W$ define

$$\ell(w)=|\{x\in D:a(x)=w\}|,\qquad
W_3=\{w\in W:\ell(w)=3\},\qquad L_3=|W_3|.$$

These are actual repeat incidences, not a prescribed abstract port
assignment. Since each heavy endpoint has one unit mate,

$$\sum_{w\in W}\ell(w)=2d.\tag{4}$$

The repeat row sum is three, so $0\le\ell(w)\le3$. If $w\in W_3$,
its repeat row consists exactly of its three unit entries to heavy
endpoints.

The source dependencies are `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`,
`D1_MATCH_HARD_BRANCH_REDUCTION.md`, and
`D1_MATCH_C4_TRANSPORT_REFINEMENT.md`. The connected-case hypothesis
and possible values of $d$ are collected in
`CONNECTED_REPEAT_REDUCTION.md`.

## Proof strategy

Equality in the port-capacity bound would make the heavy endpoints
and the saturated unit mates form a nonempty proper closed set in
the positive support of $B$. Connectedness rules this out. The
mixed-trace and five-cycle consequences are then integer substitutions
into the earlier verified identities.

## 1. Equality closes a proper repeat-support set

Equation (4) first gives $3L_3\le2d$. Suppose equality holds. Since
all terms in (4) are nonnegative, every heavy endpoint's unit mate
then belongs to $W_3$. Consider

$$Z=D\cup W_3.$$

For each $x\in D$, both positive repeat neighbors $h(x)$ and $a(x)$
lie in $Z$. For each $w\in W_3$, all three positive repeat neighbors
are heavy endpoints and therefore lie in $Z$. Thus no positive repeat
edge leaves $Z$.

The set $Z$ is nonempty because $d>0$. It is proper because it is
disjoint from the generated-triangle union $S$, whose size $3d$ is
positive. This contradicts connected positive repeat support.

Therefore $3L_3<2d$, proving (1). Equivalently, at least one heavy
unit incidence must end at a light mate with at most two heavy repeat
neighbors:

$$\sum_{\substack{w\in W\\\ell(w)\le2}}\ell(w)
=2d-3L_3>0.\tag{5}$$

No bound on the number of nongenerated unit triangles or on their
vertices was used.

## 2. Mixed trace and the five-cycle improvement

`CONNECTED_REPEAT_MIXED_TRACE_AND_ROOT_PATTERNS.md` proves

$$
0\le\tau\le248-24d+2L_3,\qquad
\tau=10c_5+8d-25048.
\tag{6}
$$

Substitution of (1) gives (2). The upper bounds for the five possible
values of $d$ become

| $d$ | $1$ | $3$ | $5$ | $7$ | $9$ |
|---|---|---|---|---|---|
| Upper bound on $\tau$ | $224$ | $178$ | $134$ | $88$ | $42$ |

Only the $d=3$ and $d=9$ upper bounds change from the non-strict
port estimate. When $d=9$, equation (6) is

$$\tau=10c_5-24976.$$

The conditions $0\le\tau\le42$ imply
$24976\le10c_5\le25018$. Since $c_5$ is an integer, this is exactly
the range (3). Equivalently, the possible mixed-trace values in this
case are restricted to $4,14,24,34$; the earlier value $44$ is removed.

## 3. A componentwise multigraph restriction

Let $L$ be the set of all distinct unit mates of heavy endpoints.
Construct a multigraph $F$ with vertex set $L$ and one edge for every
heavy pair $\{x,h(x)\}$, joining its two unit mates
$a(x),a(h(x))$. The D1 hard-branch theorem says those mates are
distinct, so $F$ has no loops. Parallel edges are allowed; their
exclusion is neither needed nor claimed. Its degree at $w$ is
$\ell(w)\in\{1,2,3\}$.

No connected component of $F$ can have all its vertices of degree
three. If such a component existed, take its light-mate vertices and
all heavy endpoints corresponding to its edges. Every chosen heavy
endpoint has both its heavy mate and unit mate in that set. Every
chosen light mate has all three repeat neighbors among the chosen
heavy endpoints. The set would again be nonempty, repeat-closed, and
disjoint from $S$, contradicting connectedness.

Thus every connected component of $F$ contains a vertex of degree
one or two. This is a necessary structural condition on the actual
heavy-port incidence multigraph, not a realizability assertion for
arbitrary multigraphs satisfying it.

## Scope

The strict closure argument uses only the actual D1 repeat rows,
their port separation, positivity, and connectedness. It does not
assume that all unit repeat triangles are generated or that positive
mixed-trace root patterns have been excluded. All remaining values
of $d$ are still open.

The earlier mixed-trace and unit-triangle sources are unchanged. No
solver, graph enumeration, or new formal theorem was used or created.
Independent review of this new strict bound remains outstanding.
