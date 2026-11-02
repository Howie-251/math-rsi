# Proposed full original-graph model for an internal double-path vertex

## Status and exact target

**Mathematical design reviewed; implementation underway.** The reused local
DELTA_PORT_MODEL_AUDIT.md and actual Gemini round2 accepted this complete
representation, with full records under reviews/dd82/. This document is
a mathematical specification, not an emitted input or solver result.
Source checking and actual computation have separate acceptance records.

Decide whether an actual simple order-$61$, degree-$8$, diameter-two graph
can have a vertex $v$ with two double-defect neighbors $u,w$, where
$B=A^2+A-7I-J$. All edges and all common neighbors below refer to this
same original $A$. The dependencies are
[INTERNAL_DOUBLE_PATH_LOCAL.md](INTERNAL_DOUBLE_PATH_LOCAL.md),
[INTERNAL_DOUBLE_PATH_FOLLOWUP.md](INTERNAL_DOUBLE_PATH_FOLLOWUP.md), and
[INTERNAL_DOUBLE_ENDPOINT_ADJACENCY_EXCLUSION.md](INTERNAL_DOUBLE_ENDPOINT_ADJACENCY_EXCLUSION.md).
The last note reduces the original six necessary types to
$$ (r,h,\beta)=(0,1,0),\ (1,0,0),\ (2,0,1),\qquad \epsilon=0. \tag{1} $$
Its local review and external acceptance have their own receipts; this
design must not silently upgrade either status.

The three inputs cover every actual graph with an internal vertex of $D$,
conditional on those mathematical reductions. A checked contradiction in
all three would prove that $D$ has no internal vertex: it would consist
only of isolated vertices and isolated edges. It would not settle the
still-open adjacent isolated-double branch or all order-$61$ graphs.
This is a different structural target from the earlier adjacent-double
model and the closed boundary-completion loop, not a restart of either.

## 1. Canonical core and fixed parent classes

Use $v=0,u=1,w=2$ and $T=(t_0,\ldots,t_7)=(3,\ldots,10)$.
Take $U=\{t_0,t_1,t_2\}$ and set
$$\begin{array}{c|c}
r&W\\\hline
0&\{t_3,t_4,t_5\}\\
1&\{t_0,t_3,t_4\}\\
2&\{t_0,t_1,t_3\}.
\end{array}$$
Every ordered pair of three-element subsets of $T$ with intersection
size $r$ can receive these labels: map its intersection, $U$-only,
$W$-only and neutral parts separately. This fixes no original-graph
automorphism and does not require exchanging the two endpoints.

Give $Z_t$ consecutive labels in $\{11,\ldots,60\}$, in increasing
$T$ order, with size $m_t=7-1_{t\in U}-1_{t\in W}$. Fix precisely
the following incidences before choosing any $Z$ edge:

- $N(v)=T$; $u,v,w$ are pairwise nonadjacent.
- $A[T]=0$, $N(u)\cap T=U$, and $N(w)\cap T=W$.
- Every point of $Z_t$ has $t$ as its unique $T$ neighbor and is
  nonadjacent to $v$.

The sizes are $(6^6,7^2)$ for $r=0$, $(5,6^4,7^3)$ for $r=1$,
and $(5^2,6^2,7^4)$ for $r=2$, each totaling $50$.

## 2. A lossless simultaneous labeling of P and Q

Here $|P|=|Q|=5$. The local theorem gives exactly one $P$ point in
each class outside $U$ and none in $U$, and exactly one $Q$ point in
each class outside $W$ and none in $W$. Hence a common $P/Q$ point
can occur only in a neutral class $t\notin U\cup W$, at most once
in each such class.

There are $2+r$ neutral classes. Their parent labels are still mutually
interchangeable after fixing $U,W$. Map the $h$ classes that actually
contain common attachments to the first $h$ neutral labels. For the
three surviving types this means choosing the first neutral class when
$(r,h)=(0,1)$, and no shared class when $h=0$. No unrelated class,
cross-class matching or incidence map has yet been fixed.

Within each class independently, assign labels as follows:

- With only a $P$ point or only a $Q$ point, use its first label.
- With a common $P/Q$ point, use the first label for that one point.
- With distinct $P$ and $Q$ points, use the first label for $P$ and
  the second for $Q$.
- All remaining labels are its ordinary points, in arbitrary order.

This uses only the available parent-category permutation and then
independent within-class permutations. It consistently relabels all
$Z$ edges and fixes the complete $u$–$Z$ and $w$–$Z$ blocks. It does
**not** assume an attachment overlap without proof: every original
overlap of the prescribed cardinality has been explicitly mapped to
the representative. The actual $P,Q$ sets therefore become constants.

At this point every adjacency touching $\{u,v,w\}\cup T$ is fixed.
Only pairs within the original $50$-point set $Z$ can remain variables.

## 3. Ordinary vertices, saturated parent rows, and two stronger labels

Write $p_z=1_{z\in P}$, $q_z=1_{z\in Q}$, $e_z=p_z+q_z$.
Every ordinary point $z\in Z_t\setminus(P\cup Q)$ has no neighbor
in its own class and exactly one in each of the other seven classes.
Fix all same-class pairs with at least one ordinary endpoint to zero.
The only remaining possible same-class edge is between the distinct
$P,Q$ points in a nonshared neutral class.

For $r>0$, let $c\in U\cap W$. Its row in the actual $B[T]$
has total weight four, so $B_{cz}=0$ for every $z\in Z$.
An exceptional point has $e_z=1$ because $h=0$, and cannot have
parent $c$. The exact local formula then gives
$$0=B_{cz}=d_{Z_c}(z)+e_z-1=d_{Z_c}(z). \tag{2}$$
Thus every exceptional point avoids every shared-parent class $Z_c$.
These are additional fixed-zero $Z$ pairs, not selected matchings.

For $r>0$, each class has exactly five ordinary points: a shared-parent
class has size five and no exceptional point; a one-sided parent class
has size six and one; a neutral class has size seven and two. Choose
$c=t_0\in U\cap W$. All five points of $Z_c$ are ordinary. Between
$Z_c$ and the five ordinary points of any other class, every vertex
on both sides has degree one: the ordinary color rule gives degree
one to the whole opposite class, and (2) excludes its exceptional
points. Therefore this actual bipartite block is a perfect matching.

Label $Z_c$ arbitrarily by $0,\ldots,4$. Independently label the five
ordinary points in each other class by their unique $Z_c$ neighbor.
The previously assigned exceptional labels are untouched. This fixes
**seven** $5\times5$ blocks to identity, $175$ original adjacency
pairs. Matchings and edges between the other seven classes remain
variable. In particular a second reference matching is not also set
to identity, and no graph automorphism is imposed. These labels
preserve the attachment normalization from section2.

Two further directly justified zero sets are available:

1. When $h=1$, let $s$ be the common attachment. Commutation gives
   $\sum_{t\in T}B_{ts}=4$, so the entire row of $s$ is supported on
   $T$. In particular $B_{su}=B_{sw}=0$. An edge from $s$ to another
   point of $P$ would form a triangle through the adjacent pair $s,u$,
   contradicting $B_{su}=0$; the same applies to $Q$. Hence $s$ avoids
   the eight other points of $P\cup Q$.
2. When $\beta=1$, row $u$ spends two units at $v$ and one at $w$.
   If two points of $P$ were adjacent, the resulting triangle would
   require two distinct additional positive entries in row $u$, beyond
   its one remaining unit. Thus $P$ is independent. The argument at
   $w$ makes $Q$ independent. This does not make the full graph
   triangle-free. Here $h=0$, so these give twenty distinct zero pairs.

## 4. Actual primary variable and edge counts

Before the preceding zeros, there are $\binom{50}{2}=1225$ possible
$Z$ pairs. Same-class zeros remove
$\sum_t\binom{m_t}{2}-(2+r-h)$ pairs, where
$\sum_t\binom{m_t}{2}=132+r$. The subsequent zero sets and reference
blocks are disjoint from those removed pairs and from each other.
Thus the proposed free original-adjacency counts are:

| $(r,h,\beta)$ | After ordinary same-class zeros | Extra saturation zeros | Reference block pairs fixed | Final free A bits |
|---|---:|---:|---:|---:|
| $(0,1,0)$ | 1094 | 8 | 0 | 1086 |
| $(1,0,0)$ | 1095 | 50 | 175 | 870 |
| $(2,0,1)$ | 1095 | 100+20 | 175 | 800 |

These are algebraic predictions, not emitted counts or runtime evidence.
There are exactly $74$ fixed edges touching the eleven-point core:
$8$ from $v$ to $T$, six endpoint-to-$T$ edges, $50$ parent edges,
and ten endpoint attachments. Each graph on $Z$ must have $170$
edges because its degrees are $7-e_z$ and $\sum_z e_z=10$.
The reference normalization fixes $35$ of those edges when $r>0$;
the remaining edge counts are respectively $170,135,135$. The full
graph then has $244$ edges. These totals do not replace degree or
pair-coverage constraints.

## 5. Complete original-A constraints

Use one Boolean for each remaining $Z$ pair, constants for every other
original adjacency, and no loop variable. Decode all $61$ vertices.

**Degrees.** Every exceptional $z$ has exact $Z$ degree $7-e_z$.
Every ordinary $z\in Z_t$ has exact degree one into every other
class and zero into its own. These enforce its $Z$ degree seven
and, with its fixed parent, total degree eight. The eleven core
vertices and any fully normalized reference vertices already have
their full degree-eight neighborhoods fixed; preparation must check
their actual counts. A redundant all-vertex degree counter is optional,
not required to establish degree eight for every vertex.

**Every original pair.** For all $1830$ unordered original pairs,
require a direct edge or an actual two-edge path through an original
third vertex. Simplify fixed zeros/ones faithfully. A path with two
free edges uses the full three-clause AND equivalence. A path with
one fixed-one edge is its other literal; a fixed direct edge or fixed
two-edge path makes only that coverage clause a tautology. Record
every pair, including those with constant witnesses. No pseudo path,
chosen quotient incidence or independently guessed B is permitted.

The core constants themselves already give
$$\mu(v,u)=\mu(v,w)=3,\qquad A_{vu}=A_{vw}=0,$$
and $\mu(v,x)+A_{vx}=1$ for every other $x\ne v$. Therefore the
actual row $B_{v*}$ is exactly $2e_u^T+2e_w^T$ in every model.
They also give $B_{uw}=\beta$, the stated $B[T]$, and
$B[T,u]=B[T,w]=0$. Preparation should verify these identities
directly from the fixed neighborhoods; they require no large counters.

**Short actual port counts.** For $z\in Z_t$, the only nonconstant
parts of the following actual entries are small color/attachment counts:
$$\begin{aligned}
B_{xz}&=d_{Z_x}(z)+1_{x\in U}p_z+1_{x\in W}q_z-1+1_{x=t}
 &&(x\in T),\\
B_{uz}&=d_P(z)+1_{t\in U}+p_z-1,\\
B_{wz}&=d_Q(z)+1_{t\in W}+q_z-1.
\end{aligned} \tag{3}$$
The ordinary color rule already makes $B[T,z]=0$ there, so the
$T$-to-$Z$ counters need only exceptional points. The endpoint counters
$B_{uz},B_{wz}$ and the counts $d_P,d_Q$, however, must be encoded for
**all fifty** points of $Z$: an ordinary point need not have zero
endpoint defect. Encode these small counts, their nonnegativity and
inherited upper bound two. Exact threshold bits may represent $[B\ge1]$ and
$[B\ge2]$ only when they are equivalent to the displayed actual-A
counts; their sum is then the actual B weight. Useful redundant budgets
are
$$\sum_{z\in Z}B_{xz}=4-2(1_{x\in U}+1_{x\in W}),\quad
\sum_{x\in T}B_{xz}=2e_z,$$
$$\sum_{z\in Z}B_{uz}=\sum_{z\in Z}B_{wz}=2-\beta.$$
No input length in the counts $d_{Z_x},d_P,d_Q$ exceeds seven.

For $h=1$, the common attachment's saturated row additionally gives
$B_{sz}=0$ for all other $z\in Z$. These are exact constraints
$\mu(s,z)+A_{sz}=1$ on the same actual paths, with at most $49$
pair counters. They are a meaningful strong port condition.

There is no need to build a generic B-upper counter on **every**
$Z$ pair. Omitting that redundant all-pair strengthening enlarges the
intermediate CNF description; all satisfying assignments still satisfy
the original exact degrees and genuine diameter-two coverage. Thus any
independently verified SAT graph is a genuine target, and every true
target survives. A purported target contradicting an inherited theorem
must be retained for diagnosis, not rejected merely to preserve a lemma.

## 6. Size estimate and reuse boundaries

After fixing the core and attachments, every core-to-$Z$ common-neighbor
count is a linear sum of existing $Z$ edge variables; it needs no new
two-free-edge path conjunction. Before the optional reference constants,
the number of $Z$ pairs with no fixed common core neighbor is
$$1225-\left(132+r+20-\binom h2\right)
=1073-r+\binom h2.$$
For the three surviving types these are $1073,1072,1071$. Each needs
at most $48$ possible $Z$ middle vertices, and fixed-zero simplification
removes many. Even the loose bound is $51504$ path conjunctions, rather
than the old unconditional $107970$ all-61-pair construction. The shared
attachment's exact counters require at most fourteen additional formerly
covered pairs, adding at most $672$ conjunctions if none are shared.
The reference classes further reduce this number for $r>0$.

With small degree/port counters, a straightforward implementation should
remain on the order of $70000$ variables and a few hundred thousand
clauses, subject to actual emitted counts. This is an algebraic sizing
estimate, **not** a measured speedup, a runtime promise, or evidence that
the constraints are satisfiable. It avoids the earlier roughly half-million
variable pattern mainly by omitting redundant generic all-pair B counters
and by constant-folding actual fixed neighborhoods.

Reuse only generic emitter, exact/upper cardinality helpers, actual-AND
definitions, decoding, bounded process handling and independent BFS/LRAT
tools. Do not reuse adjacent-double labels, seven C selectors, S/T port
matching equations, or its triangle restrictions. The joint-boundary
constant-folding logic is useful, but its R/O-only fixed-mask constructor
does not express this model's richer fixed adjacency map unchanged.
Any implementation must retain all original pairs and its explicit fixed
map, not silently reinterpret an old domain.

## 7. A finite complete decision and minimal meaningful sanity

Three separately prepared inputs are simpler than a joint guarded input:
their class sizes, attachment constants and reference normalizations differ.
The mathematical type table and the labeling proof above supply coverage.
All three checked contradictions would exclude every internal-double
target; one incomplete or UNKNOWN branch leaves that claim open. A single
valid full graph in any branch is already a genuine construction.

Before a substantive profile, preparation should check actual vertex and
fixed-edge partitions, core row identities, free counts and the reference
matching maps against this specification. One deterministic complete
assignment to the remaining edge variables can be used as an encoding
sanity even though it is not a target: independently recompute its full
adjacency, degrees and all1830 common-neighbor/coverage values, extend the
actual emitted auxiliaries, and compare each declared constraint group
with these exact original-graph semantics. Do not claim that such an
invalid graph supplies a satisfying source witness. Reuse existing tiny
generic-helper receipts where unchanged; new guarded or counter definitions
would need a direct Boolean check only for their actual new logic.

Independent full-edge-list BFS is still required for SAT, and an exact-input
certificate plus reviewed complete reduction is required for UNSAT. No
code, generator, solver, external call, graph candidate, certificate or
runtime result accompanies this proposed design.
