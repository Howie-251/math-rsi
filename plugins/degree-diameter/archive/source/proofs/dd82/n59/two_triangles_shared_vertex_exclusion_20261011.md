# Exactly two triangles sharing one vertex are impossible under zero-row N15

## Claim and status

Assume an original legal graph on 59 vertices, with the actual N15 matching row at every zero-triangle vertex. Its triangles cannot consist of exactly two triangles sharing one vertex. This is a complete candidate paper proof, pending fresh independent review and Lean formalization. It leaves the disjoint-two-triangle case, all higher triangle counts, and the upstream applicability of N15 open.

The proof uses the original defect identity, zero-support transport, the zero-heavy endpoint lemma, and the four-cycle trace identity. It does not require the fifth-trace congruence or the three-template classification in `two_triangles_shared_vertex_reduction_20261011.md`.

## 1. A local obstruction to two heavy zero repeats

Let a root $r$ have exactly one triangle $ruv$. Write $P=N(r)$ and $P_0=P\setminus\{u,v\}$, so $|P_0|=6$ and the graph induced on $P$ consists of the single edge $uv$. Suppose all six vertices of $P_0$ are zero-triangle vertices. Suppose the complete nonedge repeat row of $r$ consists of exactly two zero vertices $x,y$ of weight two. Thus the full positive row support is

$$B_{ru}=B_{rv}=1,\qquad B_{rx}=B_{ry}=2.$$

By zero-support transport, $x$ must be adjacent to $y$: otherwise its support neighbors lie in the weight-one edge $uv$, whose independent subsets have total weight at most one, whereas the transport equation requires weight two. Once $xy$ is an edge, the same transport equation shows that neither $x$ nor $y$ is adjacent to $u$ or $v$.

Since $x,y$ are nonneighbors of $r$ and $B_{rx}=B_{ry}=2$, each has exactly three neighbors in $P$, all in $P_0$. Their parent triples $S_x,S_y$ are disjoint: a common parent would form a triangle with the edge $xy$, contradicting that $x$ is zero. They therefore partition $P_0$.

Every vertex outside $N[r]$ other than $x,y$ has exactly one neighbor in $P$, since its defect entry at $r$ is zero. For distinct $p,q\in P_0$, the vertex $r$ is a common neighbor; there is no common neighbor inside $P$, since each vertex of $P_0$ is isolated in the induced graph on $P$. The only possible further common neighbors are $x,y$. Consequently

$$B_{pq}=\mathbf1_{\{p,q\}\subseteq S_x}+\mathbf1_{\{p,q\}\subseteq S_y}.$$

Fix $p\in S_x$. Its two other companions $q,q'$ in $S_x$ give $B_{pq}=B_{pq'}=1$. By N15 at the zero vertex $p$, these are its entire light pair, which must be adjacent in the original graph. But $P_0$ is independent. This is a contradiction.

Thus this local configuration is impossible. The argument permits triangles elsewhere in the graph, provided the six private neighbors and the two heavy repeats satisfy the stated zero-vertex hypotheses.

## 2. Apply the obstruction to the shared-vertex case

Suppose the only triangles are $oab$ and $ocd$. The nonzero vertices are precisely $o,a,b,c,d$; $t(o)=2$, and each outer vertex has triangle count one. The other 54 vertices are zero.

The nonedge repeat budget of $o$ is two. The zero-heavy endpoint lemma excludes a weight-two zero endpoint at $o$, so its nonedge repeats have pattern 11.

For two outer vertices from different triangles, say $a,c$, the vertex $o$ is a common neighbor. If $B_{ac}>0$, there must be another common neighbor $z$, which is zero. It is not adjacent to $o$, because that would give an additional triangle. Hence $B_{oz}\ge1$ from the two common neighbors $a,c$. Zero-endpoint transport then gives

$$B_{oz}=(BA)_{oz}\ge B_{oa}A_{az}+B_{oc}A_{cz}=2.$$

This contradicts the zero-heavy endpoint lemma at $o$. Therefore every cross-triangle outer defect entry vanishes.

For any outer root $r$, its nonzero support consists exactly of $o$ and its triangle mate, each of weight one; these two vertices are adjacent. Its remaining defect sum four lies at zero vertices, with weights at most two. The possible patterns are 22, 211, and 1111. Pattern 211 is impossible by zero-support transport: its sole heavy zero repeat cannot have an equal-weight zero mate, and cannot find an independent subset of the nonzero support of total weight two. Pattern 22 is impossible by Section 1: the six private neighbors of $r$ are all zero, since the only two triangles have already been listed.

Thus all four outer rows must have zero-repeat pattern 1111. The center has row square sum $4+2=6$; each outer row has row square sum $2+4=6$; every zero row has square sum ten. Hence

$$s=\operatorname{tr}(B^2)=54\cdot10+5\cdot6=570.$$

The actual four-cycle identity is

$$8C_4=6n+s-12T.$$

With $n=59,T=2$ it yields $8C_4=354+570-24=900$, impossible because $900$ is not divisible by eight. This excludes the entire shared-vertex case. $\square$

## Scope and dependencies

The zero-support transport theorem is `nonzero_support_transport_20261011.md`; the endpoint bound is `n15_heavy_endpoints_avoid_two_triangles_20261011.md`; the trace identities are derived in `matching_zero_global_trace_obstruction_20261011.md`. All refer to the actual adjacency and defect matrices of the same graph. No abstract row certificate is substituted for an original graph.

Together with the separate shared-edge exclusion, exactly two triangles under zero-row N15 must be vertex-disjoint if any such graph exists. This does not yet eliminate that remaining case or establish N15 for all original 59-vertex graphs.
