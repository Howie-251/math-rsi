# Prime-order automorphisms of arbitrary 60- and 61-vertex targets

Let G be a finite simple undirected graph of order n in {60,61}, maximum
degree at most eight, and diameter at most two. No vertex-transitivity,
prescribed fibres or other construction hypothesis is assumed.

**Theorem.** G has no automorphism of order seven. If n=60, every prime
divisor of |Aut(G)| belongs to {2,3,5}.

This is a restriction on any possible target graph, not an existence or
nonexistence conclusion for the entire order. The proof is purely
mathematical and uses no enumeration, SAT result or formalization.

## Regularity and the exact repetition budget

For any vertex x of degree d, its radius-two ball has at most

\[
 1+d+\sum_{y\in N(x)}(\deg(y)-1)\leq 1+8d
\]

vertices. Diameter at most two makes this ball all of G. If d≤7, then
n≤57, a contradiction. Hence G is eight-regular and connected.

Let A be its adjacency matrix, I the identity, J the all-ones matrix,
and define

\[
 B=A^2+A-7I-J.
\]

Since (A²)xx=8, the diagonal entries of B are zero. For distinct x,y,
write μ(x,y)=|N(x)∩N(y)|. Then

\[
 B_{xy}=\mu(x,y)+A_{xy}-1\geq0,
 \qquad
 B\mathbf1=(64+8-7-n)\mathbf1=(65-n)\mathbf1.
\]

The inequality follows from diameter two: a nonadjacent pair has a
common neighbour, while an adjacent pair has Axy=1. Thus every row is a
nonnegative integer budget of five when n=60 and four when n=61. In
particular, for a nonadjacent pair,

\[
 1\leq\mu(x,y)=B_{xy}+1\leq66-n\leq6.
\]

## Excluding an automorphism of order seven

Suppose g has order seven and let F be its fixed-vertex set. Every g-orbit
has size one or seven, so

\[
 |F|\equiv n\pmod7\in\{4,5\}.
\]

In particular F is nonempty. If distinct fixed vertices x,y are
nonadjacent, their common-neighbour set is g-invariant, nonempty, and
has at most six elements by the budget above. Its orbits cannot have
size seven, so every common neighbour is fixed. Consequently the
induced graph G[F] has diameter at most two.

For any x∈F, g permutes the eight-element neighbourhood N(x). That
neighbourhood consists either of eight fixed vertices or of one orbit
of size seven and one fixed vertex. Therefore

\[
 \deg_{G[F]}(x)\in\{1,8\}.
\]

Since g is not the identity, F is a proper subset of V(G). Connectivity
and F≠∅ give an edge from F to its complement. At its fixed endpoint u,
the nonfixed neighbour has an orbit of seven neighbours. Thus u has
exactly one neighbour v in F.

Every vertex of F must be within distance two of u inside G[F]. Since
u's only neighbour there is v, v is adjacent to every vertex of F other
than itself. Hence

\[
 |F|=1+\deg_{G[F]}(v)\in\{2,9\}.
\]

Both possibilities are congruent to two modulo seven, contradicting
|F|≡4 or 5 modulo seven. This proves the first assertion.

## Prime divisors larger than eight

More generally, let h be a nonidentity automorphism of prime order p>8
of any connected graph of maximum degree at most eight. If h fixes a
vertex x, it acts on N(x), whose cardinality is smaller than p. Every
neighbour of x is therefore fixed. Repeating this argument along paths
fixes every vertex, a contradiction. Thus h has no fixed vertices and
all its vertex orbits have size p; in particular p divides the order of
the graph.

For n=60, no prime p>8 divides n, so no such automorphism exists. The
order-seven case was excluded above. Since Aut(G) is finite, Cauchy's
theorem now gives

\[
 \{p\text{ prime}:p\mid|\operatorname{Aut}(G)|\}
 \subseteq\{2,3,5\}.
\]

For n=61 this same argument leaves the prime 61 possible; together
with the order-seven exclusion it only gives the prime-divisor set
{2,3,5,61}. No exclusion of order-61 automorphisms is claimed here.
