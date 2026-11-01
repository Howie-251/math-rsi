# Maximum-blue sources at an all-seven edge

Status: **NOT CURRENTLY JUSTIFIED** for the requested whole coloring repair.
The zero-heavy-trace reduction below is proved; the repair for two or three
exterior red points remains open. This note uses no new layout table, whole
hypergraph search, Lean, or v2 material.

## 1. Scope and source convention

Let $H$ be a simple five-uniform hypergraph on $24$ vertices, with exactly
$35$ edges, minimum degree at least $7$, and covering every vertex pair.
Fix an edge $G$ whose five vertices all have degree $7$. Assume that $H-G$
has a proper coloring with $G$ all red. This source exists when $H$ is
edge-critical, but criticality is not needed after the source is supplied.

Write $A$ for the red vertices outside $G$, $B$ for the blue vertices, and
$a=|A|$. Choose a source maximizing $|B|$, equivalently minimizing $a$,
with this same specified $G$. No optimization over other bad edges is
assumed. Define
$$
q=\sum_{\substack{e\ne G\\e\cap G\ne\varnothing}}(|e\cap G|-1),
\qquad m_0=|\{e:e\cap G=\varnothing\}|.
$$
The $30$ nongroup incidences with $G$ give
$$
34-m_0=30-q,\qquad m_0=4+q.
$$
Every $x\in A$ has a private zero-$G$ edge: otherwise recoloring only $x$
blue preserves propriety of $H-G$. Such private edges are distinct for
different $x$, so $a\le m_0$. This is a maximum-blue statement, not a
minimum-blue statement. The earlier globally minimum-blue $b=13$ domain
is not used.

All numerical conclusions here concern $M=35$. For $M=34$ the identity is
$m_0=3+q$, and the total excess above degree seven is $2$, rather than $7$.
No $M=34$ repair claim is inferred.

## 2. Complete zero-heavy-trace reduction

**Proposition.** If $q=0$, the minimum possible $a$ is exactly the
transversal number of the four zero-$G$ edges, and in particular $a\le3$.

Indeed, all $30$ nonzero nongroup traces are singletons, six at each
vertex of $G$. Four five-subsets of the $19$ exterior vertices cannot be
pairwise disjoint. Choose a vertex in two intersecting zero-$G$ edges and
one vertex in each remaining zero-$G$ edge. This gives a transversal of
size at most three. Color those vertices red and all other exterior
vertices blue. A zero-$G$ five-edge is hit and cannot be all red. A
singleton-$G$ edge has four exterior vertices, so cannot be all red either.
Thus this is a proper coloring of $H-G$.

Every proper source must hit the zero-$G$ edges. Conversely a minimum
transversal has size at most three and gives the proper source just
constructed. This proves the equality, including the quantifier over
maximum-blue sources.

If $a=1$, the existing complete conditional theorem
[ONE_RED_EXTERIOR_DG35_CLOSURE.md](../../twentyfive/three_positive_cost/ONE_RED_EXTERIOR_DG35_CLOSURE.md)
colors $H$. Its degree-sum assumption is exactly
$\sum_{g\in G}d(g)=35$. Therefore, in a putative non-B hypergraph, the
entire $q=0$ branch reduces to $a=2$ or $a=3$.

When $a=3$, no exterior point lies in three zero-$G$ edges: such a point
and one point of the fourth would give a two-point transversal. Also the
intersection graph of the four zero-$G$ edges has matching number at most
one, since two disjoint intersecting pairs give a two-point transversal.
Its nontrivial edges therefore form a star or a triangle. In particular
every exterior point lies in at most two zero-$G$ edges.

## 3. What the same-source five-center constraints give

For $g\in G$, let $m_g$ count singleton-$G$ edges at $g$ whose exterior
four-set is entirely blue. These are its positive sets in the exact
one-center repair interface. There are six singleton edges at $g$.
Pair coverage with $A\ne\varnothing$ forces at least one to meet $A$, so
$m_g\le5$. Put $k_g=6-m_g$.

For $a=3$, it is impossible that all $m_g=5$. Every center would then
have one nonpositive edge, which must contain all three vertices of $A$.
Each $x\in A$ occurs in exactly five such edges and at most two zero-$G$
edges. These edges cover at most $5+2\cdot4=13$ vertices of $B$, fewer
than $|B|=16$. This contradicts pair coverage with $x$.

More precisely, **conditionally on $m_g\ge4$ for all five centers**, at
least three centers have $m_g=4$. Let their number be $s$. A center with
$m_g=5$ contributes at most three incidences covering pairs in $A\times B$.
A center with $m_g=4$ has two nonpositive edges; an edge containing $k$
vertices of $A$ contributes $k(4-k)\le4$, hence at most eight altogether.
The three private zero-$G$ edges of the three red exterior points have
one red point each and contribute twelve. The fourth contributes at most
six. Consequently
$$
48=|A||B|\le 3(5-s)+8s+18=33+5s,
\qquad s\ge3.
$$
The conditional premise has not been proved: the old exclusion of
$m_g\le3$ uses a signed-cost bound available at $a=1$; it cannot simply
be imported at $a=3$.

## 4. Exact point where the existing repair gates stop

For a selected center $g$, let $n_j(g)$ count indexed negative sets of
size $j$, and set
$$
C_g=9n_1(g)+4n_2(g)+n_3(g).
$$
For $q=0$ and $a\le3$, put
$$
U=\sum_{x\in A}d(x),\quad
V=\sum_{\{x,y\}\subset A}\lambda_{xy},\quad
z=\sum_{e\cap G=\varnothing}|e\cap A|.
$$
An edge with singleton $G$-trace and $k$ exterior red vertices contributes
$k^2$ to this cost when it avoids $g$. A zero-$G$ edge contributes
$(k-1)^2$. Since $k^2=k+2\binom{k}{2}$, the exact identity is
$$
C_g=U+2V-\sum_{\substack{e\ne G\\g\in e}}|e\cap A|^2-2z+4.
$$
This does not generally give $C_g\le24$, the hypothesis of the existing
three-positive cost lemma. The four-positive gate also requires a
stronger linear negative budget than is presently established.

Here is a precise aggregate obstruction to deriving those hypotheses
from just the available row totals. It is **not** a realized hypergraph
or a counterexample to Property B. Take $a=3$, all five $m_g=4$, and at
each center two nonpositive edges with red-$A$ traces of size two.
Across the ten traces let the three pair types occur $3,3,4$ times.
Let the four zero-$G$ red traces be the three singletons and $A$ itself.
Then
$$
U=26,\quad V=13,\quad z=6,\quad
\sum_{e\ni g,e\ne G}|e\cap A|^2=8,\quad C_g=36
$$
at every center. The exterior red degrees are $9,9,8$, using five of the
seven global excess units; the $16$ blue vertices have total degree
$114$, leaving exactly two excess units. Each center has four exterior
red incidences and twenty blue incidences, consistent with its five
row-repeat units. For a selected center this gives
$$
(n_1,n_2,n_3,n_4)=(0,9,0,19),
\qquad 3n_1+2n_2+n_3=18.
$$
Thus neither $C_g\le24$ nor the old four-positive linear budget $\le8$
follows from those joint totals. Realizability and repair of this
aggregate pattern have not been decided. No local failure is asserted.

The independent-transversal inequality in
[RANDOM_TRANSVERSAL_REPAIR.md](../../../../../proofs/propertyb35/RANDOM_TRANSVERSAL_REPAIR.md)
remains applicable to actual signed sets, but the present arguments do
not establish a uniform strict bound for the remaining two/three-red
sources.

## 5. The $q=1$ boundary and handoff

For $q=1$ there are five zero-$G$ edges, one trace of size two, and
$28$ singleton traces. Maximum blue still gives $a\le5$. A transversal
of the five zero-$G$ edges of size at most four follows from an
intersecting pair, but it need not immediately be a proper source: it
can contain the three exterior vertices of the size-two-trace edge or
an entire singleton exterior four-set. This note therefore does not
claim $a\le4$ in that branch.

The concrete missing obligation is a simultaneous-center repair for
the actual $q=0$, $a=2/3$ sources (including the small negative sets),
or a source transfer that strictly reduces $a$ while preserving a
proper $H-G$ coloring. The argument above closes no whole $24$-vertex
branch. It supplies a small genuine source reduction, and stops before
another unbounded signed-set classification.

Verification: a fresh same-family read-only agent independently checked the
$a=\tau\le3$ source construction, the private-zero-edge bound, and
$48\le33+5s$. Its conclusion was that these reductions are valid and do
not establish repair. The displayed aggregate arithmetic and both local
dependency links were also checked directly. No new probabilistic
certificate or realized signed counterexample was generated.
