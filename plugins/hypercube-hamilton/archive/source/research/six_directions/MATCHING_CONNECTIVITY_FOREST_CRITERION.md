# A reusable sufficient certificate for arbitrary-matching cycle extension

2026-11-01. Generalization of the last-A10 rank argument. This document
does not itself accept any new hole geometry or Q6 layer.

## Statement

Let $G$ be a finite simple graph, let $W\subseteq V(G)$, and let
$K\subseteq W$ have even size $2m\ge4$. A required matching $F$ may be
any perfect matching of the complete graph on $K$, including pairs not
in $E(G)$. Vertices of $W\setminus K$ have no required edges.

An admissible short-complement witness is a spanning path forest $S$
on $W$, with edges in $E(G)$, degree one at every vertex of $K$, and
degree two at every vertex of $W\setminus K$. Its components have
exactly the vertices of $K$ as endpoints. Let $P(S)$ pair endpoints
of the same component. Put $r=2^{m-1}$.

Suppose we supply $r$ such witnesses $S_1,\ldots,S_r$ and $r$ arbitrary
perfect matchings $X_1,\ldots,X_r$ on $K$. Define $B_{ij}=1$ if the
labelled union $P(S_i)+X_j$ is one alternating cycle, and zero otherwise.
If $B$ has rank $r$ over $\mathrm{GF}(2)$, every required matching $F$
has a simple spanning cycle on $W$ containing all of $F$, whose other
edges belong to $G$.

## Proof and external dependency

The matching connectivity matrix $H_{2m}$ on all perfect matchings of
$K$ has rank at most $r$ over $\mathrm{GF}(2)$ by Corollary 3.5 of
Cygan, Kratsch and Nederlof, *Fast Hamiltonicity checking via bases of
perfect matchings*, [primary paper](https://arxiv.org/abs/1211.1506),
[published version](https://doi.org/10.1145/3148227).
The entries use the complete graph and impose no parity or adjacency
restriction on its required matchings.

The full rows indexed by $P(S_i)$ are independent because their
restrictions to the supplied columns form the full-rank matrix $B$.
They therefore span every row of $H_{2m}$.

For each fixed $F$, its column is nonzero: orient and order its edges
as $(a_i,b_i)$ and take $R=\{b_i a_{i+1}:1\le i\le m\}$, cyclically.
Then $F+R$ is a single alternating cycle. If all selected rows were
zero at column $F$, their span would also be zero there, contradicting
the row indexed by $R$. Some $P(S_i)+F$ is thus one alternating cycle.

Expand each $P(S_i)$ edge along its stored path in $S_i$. The interiors
are disjoint and partition $W\setminus K$, so the expansion visits
every vertex of $W$ once. Since $2m\ge4$, a common pair of $F$ and
$P(S_i)$ would be an isolated labelled two-edge component and is
impossible in the connected union. In particular no length-one forest
edge duplicates a required edge. The expansion is a simple cycle,
preserves $F$, and adds only edges of $G$.

## What a finite verifier must check

Verify the exact vertex sets, each forest's edge uniqueness and
adjacency in $G$, degrees, acyclicity and endpoint pairing; verify every
column is a perfect matching on exactly $K$; recompute all connectivity
bits and perform exact binary elimination. The list of supplied forests
need not exhaust all possible forests. A heuristic may find them, but
the final witness and full-rank check are deterministic.

A rank deficit proves neither failure of the extension theorem nor
existence of a counterexample. It only means this sufficient certificate
has not been obtained with the supplied forest set. Each application
needs its own independent verification and exact quantifier accounting.
