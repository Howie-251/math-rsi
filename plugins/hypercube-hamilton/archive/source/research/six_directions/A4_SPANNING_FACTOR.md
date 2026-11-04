# A4 has no degree-completion obstruction: a spanning cycle factor

Date: 2026-11-01. Status: PROVABLE AS STATED relative to N14 and the explicit
finite geometry certificate below; independent review pending at initial writing.
This is a cycle-factor statement. A4 and full P6 remain NOT CURRENTLY JUSTIFIED.

## Claim and assumptions

Let $F$ be any matching of $K(Q_5)$ with exactly four uncovered vertices.
Three holes have one parity and the fourth the other parity. Let $v$ be any
one of the three same-parity holes. There is a simple spanning 2-regular graph
$J$ on $V(Q_5)\setminus\{v\}$ containing every edge of $F$, with all edges of
$J\setminus F$ in $E(Q_5)$. Thus $J$ is a disjoint union of cycles covering
exactly 31 vertices. Connectivity is NOT asserted.

An XOR translation makes the minority hole $a=0$ even; write the majority
holes as distinct odd vertices $b,t,v$. This translation preserves cube
adjacency and all matching conditions, even when the original minority was odd.
Original edges of $F$ may be arbitrary long edges, including same-parity ones.

## Dependencies

1. N14, in `TWO_ODD_HOLES_TRANSFER.md`, handles the case $a$ adjacent to $b$ or
   $t$. It depends on Fink–Mütze Theorem 8 and parity, not on A4 or P6.
2. The finite geometric inequality GF5 below is checked on all 65,535 nonempty
   subsets of the 16 even vertices. No matching enumeration is required.
3. Hall's marriage theorem, applied to an explicitly defined bipartite clone
   graph with 17 vertices on each side.
4. The elementary characterization of finite simple 2-regular graphs as unions
   of vertex-disjoint cycles.

## GF5: the finite geometric inequality

For a nonempty set $S$ of even vertices, let $N_Q(S)$ be its odd neighborhood
in the full $Q_5$, and put $n(S)=|N_Q(S)|$. Define

$$R(S)=\bigl|\{x\in S\setminus\{0\}:\text{some odd }y\text{ has }N_Q(y)\cap S=\{x\}\}\bigr|.$$

Then

$$n(S)-1+\max(0,n(S)-14)-R(S)
\ \ge\ |S|+\mathbf1_{0\in S}.\tag{GF5}$$

The exhaustive integer check `verify_a4_factor_geometry.py` iterates the
bit masks $1,\ldots,2^{16}-1$ of $S$. For each of the 16 odd vertices it
intersects its five-neighbor mask with $S$. A nonempty intersection contributes
one to $n(S)$; a singleton contributes its unique even vertex to a set of leaf
parents. Removing vertex 0 from that set gives $R(S)$. It checks GF5 directly.

The minimum difference between the left and right sides, grouped by $|S|$, is:

| $|S|$ |1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| minimum |2|3|3|2|2|1|1|1|3|4|3|3|3|2|1|0|

The result file `a4_factor_geometry_verification.json` contains an attaining
subset for each column and the checker source hash. This is a finite
computer-assisted lemma, not an analytic derivation of the table. The empty
set will be treated directly; GF5 is not asserted for the empty set.

An additional C++ check `a4_factor_hall.cpp` uses a sharper bound separately
for all 770 choices of the nonadjacent $b,t$ and the distinct forbidden $v$,
and all 65,536 even subsets. It checks 50,462,720 inputs with no negative bound
and the same minimum values. The smaller GF5 check suffices for the proof.

## Proof of the cycle-factor claim

### 1. Adjacent free vertices

If $ab$ or $at$ is short, add that edge to $F$. The enlarged matching has two
same-parity holes, one of which is $v$. By N14 it extends to a cycle through
every vertex except $v$, using only short new edges. This proves the claim
in this case, with a connected factor. In the remainder neither $ab$ nor
$at$ is short.

### 2. The degree-completion graph

Let $G$ have vertices $V(Q_5)\setminus\{v\}$ and edges all short edges on these
vertices except the short edges already in $F$. For each vertex define the
required new degree $r(x)=2$ for $x\in\{a,b,t\}$ and $r(x)=1$ otherwise.
The sum of these requirements on even vertices is $15+2=17$, and on allowed
odd vertices is $13+2+2=17$.

Replace each vertex $x$ of $G$ by $r(x)$ copies and replace every edge $xy$
by every edge between a copy of $x$ and a copy of $y$. The resulting graph
$\widehat G$ is bipartite with 17 vertices in each part.

### 3. Neighborhood lower bound valid for every matching

Fix nonempty $S$ in the even part, and write $N=N_Q(S)$ and $n=|N|$.
An odd vertex $y\in N\setminus\{v\}$ fails to belong to $N_G(S)$ only if
every short edge from $y$ into $S$ was removed as an edge of $F$.
Since $F$ is a matching, this forces exactly one such edge, say $xy\in F$,
and $N_Q(y)\cap S=\{x\}$. Furthermore $x\ne a$, and distinct lost vertices
$y$ have distinct partners $x$. Consequently at most $R(S)$ odd neighbors
are lost this way. The vertex $v$ loses at most one more neighbor count.

The holes $b,t$ meet no edge of $F$, so each belongs to $N_G(S)$ exactly when
it belongs to $N$. At most $16-n$ of the two distinct vertices $b,t$ can lie
outside $N$. Hence at least $\max(0,n-14)$ of them lie in $N_G(S)$.
The total number of odd clones adjacent to the clones of $S$ is therefore

$$\sum_{y\in N_G(S)}r(y)
=|N_G(S)|+\mathbf1_{b\in N_G(S)}+\mathbf1_{t\in N_G(S)}
\ge n-1-R(S)+\max(0,n-14)
\ge |S|+\mathbf1_{a\in S},$$

where the final step is GF5.

### 4. Hall applies to every subset of clones

For any subset $U$ of even clones, let $S$ be the original vertices represented
by at least one clone in $U$. If $U$ is empty, Hall is immediate. Otherwise,
all copies of each original vertex have identical neighbors, so the odd clone
neighborhood of $U$ is exactly the set counted in Step 3. Also
$|U|\le |S|+\mathbf1_{a\in S}$. Thus $|N_{\widehat G}(U)|\ge|U|$.
Hall gives a perfect matching of $\widehat G$.

### 5. Project the matching without parallel edges

Project each clone edge to the corresponding edge of $G$, producing $H$.
A duplicate projected edge would require at least two copies at both endpoints.
The only vertices with two copies are $a,b,t$. There is no edge $bt$ by parity,
and $ab,at$ were excluded by the nonadjacent-case assumption. Hence no edge
of $G$ has both endpoints doubled, so the projection has no duplicates.
Thus $H$ is a simple graph and $\deg_H(x)=r(x)$ for every allowed vertex.
By construction $H$ is short and disjoint from $F$.

Now $J=F\cup H$ is simple, spans all 31 allowed vertices, and has degree two
at every vertex: a covered vertex has one edge from each of $F,H$; a hole
$a,b,t$ has two edges from $H$. This proves the claim.

## Corollary CF1: any one allowed new edge can be prescribed

In the nonadjacent branch, for every $e\in E(G)$ there is such a spanning
cycle factor $J$ containing $F\cup\{e\}$.

Indeed, every nonempty proper subset $U$ of the even clone part satisfies
$|N_{\widehat G}(U)|\ge |U|+1$. If its original support $S$ is proper, this
follows from the table: every column 1 through 15 has minimum at least one.
If $S$ is the entire even part but $U$ is proper, then $|U|\le16$, whereas
its neighborhood has all 17 odd clones, by the Step 3 bound for $|S|=16$.
Choose any clone edge $\hat e=xy$ projecting to $e$. Delete $x$ and $y$.
For every nonempty subset $U$ of the 16 remaining even clones, the strict
Hall inequality before deletion loses at most one neighbor and remains
$|N(U)|\ge|U|$. The empty set also satisfies Hall. The remaining graph has
a perfect matching; adding $\hat e$ gives a perfect matching of $\widehat G$
containing it. Step 5 projects this to the required factor.

This prescribes only ONE new edge. It does not allow prescribing all edges
of a previously chosen component, and therefore does not imply merging or
Hamiltonicity.

## Remaining obligation and source comparison

For the nonadjacent branch, A4 is now equivalent to being able to choose the
degree completion $H$ above so that $F\cup H$ is connected. The proof does not
assert that any particular Hall matching yields a connected graph, nor that
a sequence of local switches always merges its components.

Fink–Mütze, Section 4.4.2, explicitly allows arbitrary numbers of uncovered
vertices in its extending cycle or forest. Its stopping rule therefore cannot
be reused without a spanning constraint to certify A4. Their Section 6 also
asks generally about the gap between cycle-factor and Hamilton extension.
Source: https://tmuetze.de/papers/match.pdf . The present proof establishes a
special cycle-factor result; it does not resolve that general question.

This changes neither the unconditional six-hole status nor the open
8,10,12,14,16,18-hole obligations for P6.
