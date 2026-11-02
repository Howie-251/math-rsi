# Proof Package: explicit 57-point lower bound

## Claim
There exists a finite simple undirected graph on $57$ vertices with maximum degree at most $8$ such that each distinct pair is adjacent or has a common neighbor. Consequently $N(8,2)\ge57$.

## Status
PROVABLE AS STATED. The finite edge list has also passed an independent all-pairs BFS verification. This file is a paper proof; it is not a compiled Lean theorem.

## Assumptions
Arithmetic takes place in the field $\mathbb F_7$. No assumption is made about arbitrary candidate graphs.

## Notation
Use representatives
$$P=\{(1,a,b):a,b\in\mathbb F_7\}\cup\{(0,1,a):a\in\mathbb F_7\}\cup\{(0,0,1)\}.$$
The first family is ordered lexicographically in $a,b$ and receives indices $0,\ldots,48$; the second receives $49,\ldots,55$; the last receives $56$. For distinct $u,v\in P$, put $u\sim v$ exactly when $u\cdot v=0$ in $\mathbb F_7$.

## Proof Strategy
Projective normalization and a two-equation linear system give the degree and two-step coverage.

## Dependency Map
1. A nonzero vector has exactly one projective representative with first nonzero coordinate $1$.
2. One nonzero linear equation in three variables has a two-dimensional kernel.
3. Two nonproportional coefficient vectors give a rank-two system with a one-dimensional kernel.

## Proof
1. Every nonzero vector has a first nonzero coordinate, and multiplying by its inverse gives exactly one representative in $P$. The three displayed families have disjoint sizes $49,7,1$, so there are $57$ vertices.
2. Symmetry of the dot product gives undirected adjacency; requiring distinct representatives excludes loops, and the adjacency predicate gives no multiple edges.
3. Fix $u\ne0$. The equation $u\cdot z=0$ has $7^2-1=48$ nonzero solutions. Each projective class has exactly $6$ nonzero vectors, hence the kernel contains $8$ projective points. The neighbors of $u$ are these points, with $u$ itself removed if $u\cdot u=0$. Thus its degree is $7$ or $8$.
4. Let $u,v$ be distinct nonadjacent points. Their representative vectors are linearly independent, so the equations $u\cdot z=v\cdot z=0$ have a nonzero solution. Its projective representative $w$ cannot equal $u$: otherwise $v\cdot u=0$, contrary to nonadjacency. The same argument gives $w\ne v$. Hence $u\sim w\sim v$. Adjacent pairs already have a path of length one.

This proves the exact original claim. ∎

## Concrete verification
Generator: `computations/dd82/construction/brown57.py`.
Explicit graph: `computations/dd82/construction/brown57.edges` and `brown57.vertices.json`.
Independent checker: `computations/dd82/construction/verify_edges.py`; it imports no generator or geometry helper and uses ordinary BFS on the supplied edge list.

Command from project root:
```sh
python3 computations/dd82/construction/brown57.py
python3 computations/dd82/construction/verify_edges.py computations/dd82/construction/brown57.edges --out computations/dd82/construction/brown57.verification.json
```
Observed: $224$ edges; $8$ vertices of degree $7$ and $49$ of degree $8$; among the $1596$ unordered distinct pairs, $224$ have distance $1$ and $1372$ have distance $2$; no uncovered pair.

The independently downloaded [UPC adjacency list](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD2/G8_2.adj) is isomorphic to this graph. An explicit bijection is stored in `computations/dd82/construction/upc_isomorphism.json`; every unordered pair was directly checked under that bijection.

## Source and attribution
This is the classical Brown/polarity construction, not a new lower bound. The complete orthogonality rule and proof appear in J. Širáň, J. Šiagiová and M. Ždímalová, *Large graphs of diameter two and given degree*, IWONT 2010 proceedings (published 2011), pp. 347–359, specifically pp. 350–351 ([university-hosted full text](https://upcommons.upc.edu/server/api/core/bitstreams/03389833-adb7-4b2c-b5e8-50f8fd5743fa/content), local `large_graphs_diameter_two.pdf`). The current [UPC record page](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g2.html) separately lists order $57$ for degree $8$, diameter $2$; accessed 2026-10-11.

## Open Risks
No mathematical gap remains in this paper proof. Formal translation into the project's Lean graph specification is still required. This lower bound alone does not identify the optimum.
