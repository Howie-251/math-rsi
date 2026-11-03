# Equal fibers with one matching per pair: the capacity obstruction

Date: 2026-10-11. This note evaluates the proposed alternatives of four
15-vertex fibers with internal degree five, and three 20-vertex fibers with
internal degree six. Both are impossible before choosing any internal graph
or cross matching. No candidate search or solver was run.

## Model and cross-fiber bound

Let a graph have $r\geq2$ equal fibers of size $m$, with one perfect matching
between every two distinct fibers. Its internal graphs may differ, and the
matchings may be arbitrary permutations; no cyclic action, Cayley structure,
or internal vertex transitivity is assumed.

For orders $58$ through $61$, maximum degree eight and diameter at most two
force degree exactly eight: a vertex of degree at most seven has at most
$1+8\cdot7=57$ vertices in its radius-two ball. Every vertex has $r-1$
external neighbors, so every internal graph has degree

$$d=8-(r-1)=9-r.$$

Fix a source vertex in fiber $i$ and a distinct target fiber $j$. The paths
of length at most two to that target fiber have exactly these possible
types:

* one direct matching edge;
* $d$ routes using an internal edge in $i$ before the matching;
* $d$ routes using an internal edge in $j$ after the matching;
* one route through each of the other $r-2$ fibers.

Consequently the number of distinct reachable target vertices is at most

$$1+2d+(r-2)=17-r.$$

Repeated endpoints can only lower this number. Thus a necessary condition
for diameter two is

$$\boxed{m\leq17-r.}$$

More quantitatively, every graph in the declared model has at least

$$\binom r2 m\max(0,m-17+r)$$

unordered cross-fiber vertex pairs with distance greater than two, counting
an unreachable pair as a failure too. For each unordered fiber pair, count
missing targets from all $m$ source vertices in one of the two fibers.

## The proposed order-60 alternatives

| Fibers | Internal degree | Cross-target capacity | Consequence |
| --- | ---: | ---: | --- |
| $2\times30$ | $7$ | $15$ | At least $450$ bad cross-fiber pairs |
| $3\times20$ | $6$ | $14$ | At least $360$ bad cross-fiber pairs |
| $4\times15$ | $5$ | $13$ | Capacity fails; also $15\cdot5$ is odd, so the required internal graph does not exist |
| $5\times12$ | $4$ | $12$ | Capacity is exact; this is a previously studied direction |
| $6\times10$ | $3$ | $11$ | Capacity permits it, but the internal graph is forced to be Petersen |

These are all possibilities with $r\geq2$: equal fibers give $r\mid60$,
while the external degree gives $r\leq9$. In particular, choosing more
efficient internal graphs or non-circulant matchings cannot rescue the two
proposed alternatives.

At order $58$, the only divisor $2\leq r\leq9$ is $r=2$, with $m=29>15$,
so this mechanism fails there too. At the prime orders $59$ and $61$, there
is no nontrivial equal-fiber decomposition with $2\leq r\leq9$.

## Why six ten-vertex fibers force Petersen internally

A two-step route leaving a fiber and returning to it along the same
perfect matching returns to its original vertex. Thus distinct vertices
of one fiber must achieve distance at most two entirely inside its
internal graph.

For $r=6$, each internal graph is cubic on ten vertices. Its radius-two
Moore count is $1+3+3\cdot2=10$, so all these slots are distinct. There are
no triangles or four-cycles. A short uniqueness argument is as follows.
Choose a vertex $v$, name its neighbors $a,b,c$, and split the other six
vertices into the two children of each of $a,b,c$. Each child has two
remaining neighbors. These must be in the other two child pairs, one in
each: an edge within its own pair creates a triangle, and two neighbors
in another pair create a four-cycle through their parent. The edges
between each two child pairs therefore form a perfect matching. On the
six children their union is either a six-cycle or two triangles; the
triangle case is forbidden. This determines the graph uniquely up to
relabeling and is the Petersen graph.

Hence replacing the six internal graphs with other cubic graphs cannot
escape the existing [six-Petersen-fiber model](PETERSEN_SIX_FIBERS.md).
The matchings in that larger model may already be arbitrary; this argument
does not exclude the full six-Petersen-fiber family.

## Exact archive boundary for five twelve-vertex fibers

The existing [Round 11 report, §3.2](../../../context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/materials/n60/20260910_round11.md)
identifies `Q_C05_018` with five internally four-regular 12-vertex blocks,
one matching between every two blocks, **and each block a true connected
component of the support of the defect matrix $B$**. Its four stated
branches are recorded as historical `RAW_UNSAT`, not as independently
checked certificates. This bounded task does not reopen that direction.

The elementary path count alone does not supply the additional support
connectivity. The following lemma supplies it, without a graph catalog or
new search. Thus the reduction to the exact archived model is valid, while
the archived solver evidence remains at its stated `RAW_UNSAT` level.

### Internal support-connectivity lemma

Let $P$ be the adjacency matrix of any four-regular graph on twelve vertices
with diameter at most two, and put

$$B_0=P^2+P-3I-J_{12}.$$

Then the support of $B_0$ is connected.

First, $B_0$ is a symmetric nonnegative integer matrix with zero diagonal
and row sum five. Every off-diagonal entry is at most three: at an edge it
counts common neighbors, at most three; at a nonedge it is the number of
common neighbors minus one, at most three. Each support component has even
order, because its total row sum is five times its order and also twice
the sum of its edge weights. A component of order two would require an
entry equal to five, which is impossible. Thus each component has at least
four vertices, and the number $c$ of components is at most three.

The eigenspace of $B_0$ for eigenvalue five consists exactly of vectors
constant on each support component. Indeed a maximum coordinate in any
component propagates to all its neighbors in the equation $B_0x=5x$, and
then throughout that component. Since $P$ commutes with $B_0$, this space
is invariant under $P$. Consequently the support-component partition is
equitable for $P$, with a nonnegative integer quotient matrix $R$ of row
sum four. Let $n=(n_1,\ldots,n_c)^T$ be the vector of component orders.
Restricting $P^2+P=3I+J+B_0$ to component-constant vectors gives

$$R^2+R=8I_c+\mathbf1 n^T.$$

Undirected edge counting gives $n_iR_{ij}=n_jR_{ji}$, and hence
$n^TR=4n^T$. Therefore the codimension-one space $n^Tx=0$ is $R$-invariant.
On it, every eigenvalue is a root of $t^2+t-8$, namely

$$\theta_\pm=\frac{-1\pm\sqrt{33}}2.$$

The complementary constant vector has eigenvalue four. As the
characteristic polynomial of $R$ has integer coefficients, the two
irrational conjugate roots have equal multiplicity. Thus $c$ is odd.
If the support were disconnected, $c\leq3$ would force $c=3$ and
$n_1=n_2=n_3=4$. The quotient is then symmetric and has spectrum
$4,\theta_+,\theta_-$. Its trace is three. Its total entry sum is twelve,
so its off-diagonal entry sum would be $12-3=9$. A symmetric integer
matrix has even off-diagonal entry sum. This contradiction proves the
lemma.

### Application to the full five-fiber graph

As already shown, each internal graph $D_i$ must itself have diameter at
most two. For $r=5,m=12$, every cross-fiber row has exactly twelve path
slots for twelve targets. In a diameter-two target all are distinct, so
every cross block of $B=A^2+A-7I-J$ is zero. The diagonal blocks are

$$B_{ii}=D_i^2+D_i-3I-J_{12},$$

because the four external matching excursions contribute $4I$ to the
corresponding block of $A^2$. The lemma makes each of these five blocks
support-connected. Thus the five proposed fibers really are exactly the
five support components of $B$, as required by `Q_C05_018`.

This is a new analytic verification of the scope reduction. It is not a
new certificate check or a new proof of the archived `RAW_UNSAT` result.

## Outcome

The proposed $3\times20$ and $4\times15$ construction mechanisms are
strictly obstructed. No CPU search budget was spent and no failed candidate
was generated. Within the complete-quotient, single-matching model, any
remaining order-60 effort returns to the previously studied five-fiber or
six-Petersen-fiber directions. A new mechanism must change the interface
pattern, the number of cross neighbors, or the equality of fiber sizes.

## External discussion C6

Gemini read this proof and found no mathematical gap, via the existing
Antigravity conversation with requested/CLI-selected gemini-3.8-flash-high/high.
Root independently read the substantive argument. Raw response:
`reviews/dd82/20261011_C6_hs59_layer_capacity.json`; response wording and the
rejected unrelated C5 construction suggestion are recorded in
`reviews/dd82/20261011_C6_root_notes.md`. This is corroborating discussion,
not a Lean proof or independent backend model attestation.
