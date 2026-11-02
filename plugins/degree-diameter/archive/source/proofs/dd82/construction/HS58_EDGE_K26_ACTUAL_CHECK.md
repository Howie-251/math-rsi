# Actual HS edge-grid check: the color-class compatibility graph is empty

Date: 2026-10-12.

The proposed HS50 edge surgery with auxiliary graph $K_{2,6}$ fails its
necessary six-color condition. In the actual saved HS50 instance,
**every pair of the 36 remaining vertices is forbidden to have the same
color**. The compatibility graph has no edges and maximum clique size
one; it therefore has no six-vertex color class or six-class partition.

This was checked directly before any clique enumeration or exact-cover
search. Neither search was run. The computation took less than 0.01 CPU
seconds and saved a separate witness for all 630 vertex pairs.

## Actual graph and edge-grid structure

The source is the induced HS50 on original order-60 labels
$0,\ldots,39,50,\ldots,59$ in
`computations/dd82/construction/petersen_all_matchings_run/candidate.best.edges`.
Direct checking gives 175 edges, degree seven at every vertex, no common
neighbor for adjacent pairs, and exactly one for every nonadjacent pair.
Independent BFS gives unordered distance histogram $\{1:175,2:1050\}$.

Choose the actual edge $(u,v)=(0,1)$. Then

$$X=N(u)\setminus\{v\}=(4,5,12,25,37,55),$$
$$Y=N(v)\setminus\{u\}=(2,6,15,29,33,54).$$

The remaining 36 vertices induce a five-regular graph $R$. Every vertex
has exactly one neighbor in $X$ and exactly one in $Y$, and the 36
resulting row/column coordinates are all distinct. With the displayed
orders for $X$ and $Y$, the actual grid is

$$
\begin{pmatrix}
3&9&10&24&34&53\\
7&8&52&19&38&22\\
23&11&17&51&13&30\\
36&20&28&27&56&16\\
14&39&35&26&32&59\\
57&58&18&31&21&50
\end{pmatrix}.
$$

## All-pair incompatibility

The proposed construction requires every grid row and column, and every
closed neighborhood in $R$, to contain all six colors once. Consequently
two same-color vertices must be in different rows and columns and have
distance at least three within $R$.

The direct pair classification is disjoint and complete:

| Reason two vertices cannot have the same color | Pair count |
|---|---:|
| Adjacent within $R$ | 90 |
| A common neighbor within $R$ | 360 |
| Same $X$ row | 90 |
| Same $Y$ column | 90 |
| Total | 630 |

Thus no compatible pair exists. This closes the color-class obligation
for the actual instance without a clique or exact-cover computation.

The underlying reason also holds for any choice of edge in HS50. Any
two distinct vertices of $R$ are adjacent or have a common neighbor
because HS50 has diameter two. In the second case the common neighbor
cannot be $u$ or $v$, since vertices of $R$ are adjacent to neither.
A common neighbor in $R$ violates the closed-neighborhood color rule;
one in $X$ or $Y$ violates the row or column rule. Adjacent vertices
violate the closed-neighborhood rule directly. Hence all 36 vertices
would need different colors. The contradiction is independent of which
perfect matching is added between $X$ and $Y$.

This excludes the specified edge-surgery/$K_{2,6}$/one-leaf-per-$R$-vertex
family, not arbitrary HS-derived constructions or arbitrary order-58
graphs. No 58-point target was generated or claimed.

## Artifacts

The script is
`computations/dd82/construction/hs58_edge_k26_structure.py`.
Its output directory `hs58_edge_k26_structure_run/` contains:

- `hs50.edges`: the full extracted 50-point graph, relabelled consecutively;
- `structure.json`: the relabelling map, selected edge, grid, exact
  structural checks, empty compatibility edge list and all 630 pair witnesses.

Reproduction from the project root:

```sh
python computations/dd82/construction/hs58_edge_k26_structure.py
```
