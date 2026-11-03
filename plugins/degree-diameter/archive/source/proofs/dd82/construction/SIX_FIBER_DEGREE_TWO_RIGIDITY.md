# Six ten-vertex fibers of internal degree two force the K3,3 double interface

Date: 2026-10-12. This is a pure analytic reduction of the full equitable
cross-degree family. No integer-matrix enumeration or graph search is used.

## Claim

Suppose a simple undirected graph of degree eight and diameter at most two
has an equitable partition into six fibers of size ten, each inducing a
two-regular graph. Write $q_{ij}$ for the common number of neighbors in
fiber $j$ of a vertex in fiber $i$, and put $q_{ii}=0$.
Then, after relabeling the fibers,

$$Q=(q_{ij})=2\begin{pmatrix}0&J_3\\J_3&0\end{pmatrix}.$$

The earlier [double-interface reduction](K33_DOUBLE_INTERFACE_MODEL.md)
then shows that every internal graph is $2C_5$ and the whole graph can be
repartitioned into six Petersen graphs, with one perfect matching between
every two of the new fibers. This theorem does not exclude that full
Petersen family. It shows that allowing arbitrary equitable cross degrees
in the internal-degree-two model produces no additional target graphs.

## Cross-fiber capacities and their row sums

Equal fiber sizes give $q_{ij}=q_{ji}$, and the total degree gives
$Q\mathbf1=6\mathbf1$. For distinct fibers $i,j$, the direct edges and
length-two routes from one source in fiber $i$ into fiber $j$ have count

$$h_{ij}=q_{ij}+2q_{ij}+2q_{ij}+(Q^2)_{ij}
        =5q_{ij}+(Q^2)_{ij}.$$

Diameter at most two therefore requires

$$h_{ij}\ge10.\tag{1}$$

Set $s_i=\sum_kq_{ik}^2$. Since the row sum of $Q^2$ is $36$ and its
diagonal entry is $s_i$, summing over $j\ne i$ gives

$$\sum_{j\ne i}h_{ij}=30+36-s_i=66-s_i.\tag{2}$$

These expressions count routes and remain valid when many routes reach
the same vertex; such collisions can only make the coverage requirement
harder to satisfy.

## Every cross degree is at most two

Suppose $q_{ij}=t\ge3$. This particular pair has $h_{ij}\ge5t$, while
the other four pairs in row $i$ each have capacity at least ten. Thus

$$66-s_i\ge40+5t.$$

Every other entry is a nonnegative integer, so $q^2\ge q$ and

$$s_i\ge t^2+\sum_{k\ne j}q_{ik}=t^2+6-t.$$

Combining the two inequalities yields

$$t^2+4t\le20,$$

which fails already at $t=3$. Hence all cross degrees belong to
$\{0,1,2\}$.

## Same-fiber coverage forces three double interfaces per fiber

If a source lies on an internal cycle of length $\ell$, the number of
vertices in its fiber reached by internal routes of length at most two
is $\min(\ell,5)$. A route through fiber $j$ starts with one of $q_{ij}$
neighbors there; each such neighbor has $q_{ij}-1$ neighbors back in the
source fiber other than the source. Consequently same-fiber coverage
requires

$$\min(\ell,5)+\sum_jq_{ij}(q_{ij}-1)\ge10.\tag{3}$$

In particular $\sum_jq_{ij}(q_{ij}-1)\ge5$. With every entry at most two,
this sum equals twice the number $b_i$ of entries equal to two. Hence
$b_i\ge3$. On the other hand the row sum six gives $b_i\le3$. Equality
holds, leaving no entries equal to one: every row has exactly three twos
and two off-diagonal zeros.

Therefore $Q=2F$, where $F$ is the adjacency matrix of a simple cubic
graph on six vertices. Also (3) now excludes every internal three-cycle,
because $3+6<10$. At this stage the only possible internal types are
$C_{10}$, $C_6+C_4$, and $2C_5$.

## The quotient support must be K3,3

If $i,j$ are nonadjacent in $F$, then $q_{ij}=0$ and (1) becomes

$$4|N_F(i)\cap N_F(j)|\ge10.$$

The common-neighbor count is an integer at most three, so it equals
three. Thus every nonadjacent pair has exactly the same neighborhood.

Choose a vertex $v$. Its two nonneighbors $u,w$ both have neighborhood
$N_F(v)$, a set of three vertices disjoint from $\{v,u,w\}$. Hence all
edges between $\{v,u,w\}$ and $N_F(v)$ are present. They already account
for degree three at every vertex, so $F=K_{3,3}$.

This leaves exactly one quotient up to $S_6$ relabeling, or ten labeled
matrices (the ten unordered bipartitions of six labels into two triples).
These counts are mathematical consequences, not enumeration output.

## Internal cycle types and the resulting complete scope

For a double interface across the resulting $K_{3,3}$, exactly ten
direct/internal path slots must cover ten targets. If $D_i,D_j$ are the
internal adjacency matrices and $Y_{ij}$ is the interface matrix, this
forces

$$D_iY_{ij}+Y_{ij}D_j+Y_{ij}=J_{10}.$$

The [existing exact-interface proof](K33_DOUBLE_INTERFACE_MODEL.md) gives
the remaining deductions without an enumeration: summing over a cycle
forces its length to be divisible by five, excluding $C_6+C_4$; a
$C_{10}$ fiber forces antipodal row twins in all its interfaces and reaches
at most six vertices of its own fiber in two steps, so it is impossible.
All fibers are therefore $2C_5$. Pairing the six left five-cycles with the
six right five-cycles gives six Petersen fibers and single matching
interfaces, with all edges preserved.

The result covers all symmetric nonnegative integer cross-degree matrices
of row sum six under the stated equitable partition. It assumes neither
a cyclic/Cayley action nor defect-matrix support components. Irregular
interfaces, unequal fiber sizes, and partitions with different internal
degrees are outside its scope. No public wiki or checkpoint was modified.
