# Signed short cycles exclude seventeen heavy-pair edges when d is nine

## Claim and status

**PROVABLE AS STATED.** New paper proof awaiting independent review.
In the actual connected-repeat order-62 setting, let $F$ be the simple
signed graph on the heavy pairs whose two-fold lift is $G[D]$, as
constructed in `CONNECTED_REPEAT_HEAVY_ORIGINAL_SUBGRAPH.md`.
If there are nine heavy pairs, then

$$\boxed{|E(F)|\le16},\qquad
\boxed{|E(G[D])|\le32}.\tag{1}
$$

This improves the preceding bounds $17$ and $34$. It does not exclude
$d=9$ or establish existence of any remaining signed base graph or
original graph.

## Assumptions and notation

Use the actual connected-repeat graph and the heavy-pair lift theorem
from `CONNECTED_REPEAT_HEAVY_ORIGINAL_SUBGRAPH.md`. Its conclusions
needed here are:

- $F$ is a simple graph on $d$ vertices, with degrees $r_i\le4$;
- each edge has sign $+1$ or $-1$;
- every triangle and every four-cycle in $F$ has negative sign product,
  because a positive product would lift to an original triangle or
  four-cycle in $G[D]$;
- $|E(G[D])|=2|E(F)|$;
- for $d=9$, the preceding proof already gives $|E(F)|\le17$.

Signs on a cycle are multiplied around its edges. A common-neighbor
count, or codegree, in this note always refers to the simple base graph
$F$, not to the original graph or the repeat graph.

Write $m=|E(F)|$ and $t$ for its number of triangles. Let $a$ count
edges that belong to no triangle. Among unordered nonedges, let $b$
count pairs with exactly one common neighbor and let $c$ count pairs
with no common neighbor. Their vertex-incidence counts are denoted
$a_i,b_i,c_i$. Let $t_i$ count triangles containing vertex $i$.

## Strategy

Negative signs on all short cycles prohibit two triangles sharing an
edge, three common neighbors, and a triangular-prism subgraph. An
exact degree identity then forces a hypothetical seventeen-edge base
to contain four or five triangles. The prism obstruction eliminates
five. With four triangles, local degree identities contradict both
possible degree multisets.

No candidate graphs are enumerated. The proof applies to the signed
base as a necessary consequence of an actual graph, and does not
identify signed-base feasibility with original-graph feasibility.

## 1. Three general short-cycle restrictions

### 1.1. Every pair has at most two common neighbors

Suppose vertices $i,j$ had three distinct common neighbors $x,y,z$.
The sign products on the three two-edge paths from $i$ to $j$ are
three values in $\{+1,-1\}$. At least two are equal. Joining those
two paths gives a four-cycle of positive sign product, a contradiction.
Therefore every pair has codegree at most two.

### 1.2. An edge belongs to at most one triangle

If two triangles shared an edge $ij$, multiplying their two negative
sign products would give a positive sign product on the four-cycle
through their two distinct third vertices. This is forbidden.
Consequently an adjacent pair has codegree at most one, all triangles
are edge-disjoint, and

$$a=m-3t,\qquad a_i=r_i-2t_i.\tag{2}$$

Since $r_i\le4$, every vertex belongs to at most two triangles.

### 1.3. There is no triangular-prism subgraph

Suppose there were two vertex-disjoint triangles
$a_1a_2a_3$ and $b_1b_2b_3$, together with edges $a_i b_i$ for
$i=1,2,3$. The three four-cycles using consecutive pairs of these
matching edges all have negative sign. Multiplying their signs
cancels each matching edge twice and leaves exactly the product of
the signs of the two triangles. The former product is $-1$, whereas
the latter is $+1$. This contradiction excludes the prism as a
subgraph; inducedness is not required.

## 2. An exact local degree identity

For each vertex $i$, put

$$\varepsilon_i=2d-2-\sum_{j\sim i}r_j.$$

Counting two-edge paths from $i$ by their other endpoints gives

$$\boxed{\varepsilon_i=a_i+b_i+2c_i}.\tag{3}$$

Here are all terms of the count. Among the $r_i$ adjacent vertices,
exactly $r_i-a_i$ have one common neighbor with $i$, and the others
have none. Among the $d-1-r_i$ nonadjacent vertices, exactly $b_i$
have one common neighbor, $c_i$ have none, and the rest have two by
Section 1.1. Therefore

$$
\begin{aligned}
\sum_{j\sim i}(r_j-1)
&=(r_i-a_i)+b_i+2(d-1-r_i-b_i-c_i)\\
&=2d-2-r_i-a_i-b_i-2c_i,
\end{aligned}
$$

which rearranges to (3). Summing over all vertices yields

$$\boxed{2d(d-1)-\sum_i r_i^2=2(a+b+2c)}.\tag{4}$$

In particular all $\varepsilon_i$ are nonnegative. This identity
refines the squared-degree bound from the original heavy-lift paper.

For completeness, if distinct base vertices have distance at least
three, their closed neighborhoods are disjoint. Thus

$$r_i+r_j\le d-2.\tag{5}$$

For $d=9$, this excludes a distance-at-least-three pair of degrees
$4,4$, but it does not exclude degrees $4,3$. No stronger inference
from (5) alone is used below.

## 3. Consequences of seventeen edges on nine vertices

Suppose $d=9$ and $m=17$. Since all degrees are at most four and their
sum is $34$, exactly two possibilities exist:

$$
\text{A: }\{4,4,4,4,4,4,4,3,3\},\qquad
\text{B: }\{4,4,4,4,4,4,4,4,2\}.
\tag{6}
$$

Their squared-degree sums are $130$ and $132$, respectively. Equations
(2) and (4) give

$$
\begin{array}{ll}
\text{A:}& a+b+2c=7,\\
\text{B:}& a+b+2c=6,
\end{array}
\qquad a=17-3t.
\tag{7}
$$

Since $a,b,c\ge0$, these equations force $t\ge4$. Edge-disjointness
of triangles gives $3t\le17$, so

$$t\in\{4,5\}.\tag{8}$$

## 4. Five triangles would force the forbidden prism

Construct the triangle-intersection graph $I$: its vertices are the
triangles of $F$, and two are adjacent if they share a base vertex.
Two triangles cannot share more than one vertex, since they would
then share an edge. Every base vertex belongs to at most two triangles,
so an edge of $I$ corresponds to exactly one shared base vertex.

The graph $I$ is triangle-free. Three pairwise intersecting triangles
cannot all share a single base vertex, since that would require six
distinct incident edges at that vertex. Otherwise their three
intersection vertices are distinct and form a triangle using one
edge from each original triangle. Each such edge would then belong
to two triangles, contradicting Section 1.2.

Suppose $t=5$. If $v_\triangle$ counts the base vertices belonging
to at least one triangle, then

$$v_\triangle=15-|E(I)|\le9.$$

Thus $|E(I)|\ge6$. A triangle-free graph on five vertices has at
most six edges, and equality forces $K_{2,3}$. One direct verification
is to choose a maximum-degree vertex: degree at most two permits at
most five edges; degree four permits only its four incident edges;
degree three leaves three independent neighbors and one other vertex,
with at most three additional edges. Equality in the last case is
exactly $K_{2,3}$.

Therefore $I=K_{2,3}$. Let its two degree-three vertices correspond
to the disjoint triangles $A=\{a_1,a_2,a_3\}$ and
$B=\{b_1,b_2,b_3\}$. Each of the other three triangles intersects
$A$ and $B$ once, and consequently contains an edge $a_i b_i$
after relabeling. These six vertices and three edges form the
triangular-prism subgraph excluded in Section 1.3.

Hence $t=5$ is impossible, and

$$t=4,\qquad a=5.\tag{9}$$

## 5. Degree pattern B is impossible

Pattern B has a unique degree-two vertex $z$; all its neighbors have
degree four. Thus

$$\varepsilon_z=16-(4+4)=8.$$

Equations (7) and (9) give $b+2c=1$, hence $b=1$ and $c=0$.
But (3) gives

$$\varepsilon_z=a_z+b_z\le r_z+b=2+1=3,$$

a contradiction.

## 6. Degree pattern A is impossible

Let $u,v$ be its two degree-three vertices, and put
$k=\mathbf1_{u\sim v}$. Every other vertex has degree four.
For each $z\in\{u,v\}$,

$$\varepsilon_z=16-(12-k)=4+k.$$

Using $a_z=3-2t_z$ in (3) gives

$$\boxed{b_z+2c_z=1+k+2t_z}.\tag{10}$$

Equations (7) and (9) now give $b+2c=2$. There are only two cases.

### 6.1. Suppose $b=2$ and $c=0$

Equation (10) becomes $b_z=1+k+2t_z$.
If $k=1$, both $b_u,b_v$ are at least two. Since $u,v$ are adjacent,
neither of the two counted nonedges can contain both of them. Those
two nonedges can supply at most two total incidences at $u,v$,
contradicting $b_u+b_v\ge4$. Therefore $k=0$.

Since $b_z\le b=2$, equation (10) now forces $t_u=t_v=0$.
All four triangles lie on the seven degree-four vertices. Their
triangle-intersection graph $I$ is triangle-free, as proved above,
and has four vertices. It has at most four edges: maximum degree
at most two gives this bound immediately, while degree three forces
its three neighbors to be independent and permits only three edges.
Thus the four triangles cover

$$12-|E(I)|\ge8$$

base vertices, whereas only seven are available. This is a contradiction.

### 6.2. Suppose $b=0$ and $c=1$

Equation (10) becomes

$$2c_z=1+k+2t_z,\qquad c_z\in\{0,1\}.$$

It forces $k=1$, $t_z=0$, and $c_z=1$ for both $z=u,v$.
There is only one nonedge with no common neighbor. Being incident to
both $u$ and $v$, it would have to be the pair $\{u,v\}$. But $k=1$
says that pair is an edge, a contradiction.

Both alternatives are impossible, completing the exclusion of
seventeen edges. The preceding bound $m\le17$ therefore sharpens to
$m\le16$, and the lift gives $|E(G[D])|\le32$.

## Consequences for the actual graph and remaining scope

For $d=9$, summing original degrees over the eighteen heavy endpoints
now gives

$$|E_G(D,V\setminus D)|=144-4m\ge80.$$

Their nine own generated triangles account for $6d=54$ of these
edges. Hence at least $26$ original incidences from heavy endpoints
go either to $W=V\setminus(D\cup S)$ or to generated triangles of
other heavy pairs. The existing base-distance lemma permits the
latter only at base distance at least three. If $F$ additionally has
diameter at most two, all $26$ or more incidences go to $W$.

No universal diameter bound is assumed. The conditional repeat-edge
bound $e_B(W)\le7$ from the earlier paper remains conditional on
that diameter hypothesis. It is not converted into an unconditional
bound here.

The proof uses a signed base as an actual-graph consequence. It does
not show that a signed graph with sixteen or fewer edges can be
realized by an order-62 graph. No enumeration, solver, new formal
axiom, or change to a previously reviewed source is involved.
Independent review of this new seventeen-edge exclusion is outstanding.
