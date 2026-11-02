# Independent zero sets and common-neighbor capacity under N15

## Claim and provisional status

Assume an original legal order59 graph and N15 at every zero-triangle vertex. Let $Z$ denote the zero vertices and $N=V\setminus Z$. The following is a new candidate proof, pending independent review. It derives constraints for all triangle counts, rather than only one small configuration.

## 1. Positive defect on an independent zero set has no triangle

Let $U\subseteq Z$ be independent in the original graph. At any $u\in U$, N15 gives two light defect endpoints which are adjacent in the original graph, and two heavy defect endpoints which are likewise adjacent. Thus at most one light endpoint and at most one heavy endpoint can belong to $U$.

Consequently the positive defect graph restricted to $U$ has edges of weights one and two, with each weight class a matching. It has no triangle: the three edges of a triangle cannot be properly colored with two colors. More generally its nontrivial components are paths or even cycles whose weights alternate.

For any two distinct vertices $r,s$, their common zero neighbors form an independent set (an edge between two of them would form a triangle through one of those zero vertices). If there were three such common zero neighbors $u,v,w$, every pair among $u,v,w$ would have the two common neighbors $r,s$. Since these pairs are nonedges, their defect entries would all be positive. This is the forbidden defect triangle. Therefore

$$|N_G(r)\cap N_G(s)\cap Z|\le2.\tag{1}$$

In particular, every heavy defect edge with a zero endpoint has a nonzero common neighbor: the endpoints are nonadjacent, their defect entry is two, and hence they have exactly three common neighbors.

## 2. Every zero vertex has at least two nonzero neighbors

Fix $z\in Z$, and let $u,v$ be its two heavy endpoints. N15 gives $uv\in E(G)$. By (1), there are nonzero common neighbors of $z,u$ and of $z,v$. Thus $z$ has at least one nonzero neighbor.

Suppose it has only one, $n$. Then $n$ is adjacent to both $u$ and $v$, so $nuv$ is a triangle. Hence $u,v$ are nonzero. The zero-heavy endpoint lemma gives $t(u),t(v)\le1$, so $t(u)=t(v)=1$. In particular $B_{un}=1$.

Apply the zero-support transport theorem to row $u$ at its zero repeat $z$, of weight two. If $z$ were paired with another zero repeat in that row, the paired-edge isolation statement would prohibit every other positive-support neighbor of $z$, including $n$ (which has row weight $B_{un}=1$). Thus $z$ is isolated in the zero part of that support. Its neighbors in the nonzero support must then have row weights totaling two. But its only nonzero neighbor is $n$, whose weight is one. This is a contradiction. Therefore

$$|N_G(z)\cap N|\ge2\qquad(z\in Z).\tag{2}$$

This argument uses the actual endpoint lemma and general transport theorem; it does not assume N15 at a nonzero root.

## 3. Global consequence: at least five triangles

Put $m=|N|$, and let $T$ be the number of triangles. Each nonzero vertex has at least two neighbors in $N$ (the other two vertices of one of its triangles), so has at most six neighbors in $Z$. Counting edges between $N$ and $Z$ and using (2) gives

$$2(59-m)\le e(N,Z)\le6m.$$

Hence $m\ge15$. Every nonzero vertex is in a triangle, so $m\le3T$. It follows that $T\ge5$.

Thus all cases with at most four triangles are excluded under the explicit global zero-row N15 hypothesis. In particular this subsumes the disjoint-two-triangle case as well as the previously proved intersecting cases. It does not prove N15 for arbitrary original graphs, or exclude higher triangle counts or all of H5.

## 4. Structure if exactly five triangles remain

If $T=5$, the inequalities force $m=15$. The five triangles must therefore be vertex-disjoint. Write $e(N)=15+k$, where $k$ counts additional edges among different triangles. Then

$$e(N,Z)=8\cdot15-2(15+k)=90-2k.$$

There are 44 zero vertices, each with at least two nonzero neighbors, so $k\le1$. The total excess of zero-to-nonzero degree over two is

$$\sum_{z\in Z}(d_N(z)-2)=2-2k.$$

Thus either $k=1$ and every zero vertex has exactly two nonzero neighbors, or $k=0$ and the total excess is two. In the latter case the possible degree multisets are one degree-four zero vertex or two degree-three zero vertices, with every other zero vertex of degree two. These are necessary shared-graph constraints, not candidate graph constructions.

## Dependencies and scope

Use the actual integer defect matrix, its nonnegative row sum six, and N15 from the stated graph hypotheses. The endpoint lemma is `n15_heavy_endpoints_avoid_two_triangles_20261011.md`; transport is `nonzero_support_transport_20261011.md`. No fifth-trace identity, cycle-length restriction, computation, or H5-minimal-root theorem is used. All conclusions remain conditional on N15 holding at all zero vertices.
