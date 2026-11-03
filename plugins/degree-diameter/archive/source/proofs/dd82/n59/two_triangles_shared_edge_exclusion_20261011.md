# N15 excludes exactly two triangles sharing an edge

## Claim and status

Let $G$ be an original legal graph on 59 vertices: simple, undirected, maximum degree at most 8, with every distinct pair joined by one or two edges. Assume N15 at every zero-triangle vertex: its actual defect row is 2211 and its support induces the two equal-weight matching edges. Then $G$ cannot have exactly two triangles which share an edge.

Status: complete new paper derivation, pending fresh review and formalization. This excludes the entire shared-edge case of $T=2$ under the explicit N15 premise. It does not exclude two triangles sharing only a vertex, two disjoint triangles, or general H5.

Dependencies: the universal original-graph defect identities; the four-cycle trace identity from `matching_zero_global_trace_obstruction_20261011.md`; and the newly proved endpoint lemma in `n15_heavy_endpoints_avoid_two_triangles_20261011.md`. That endpoint lemma was read in full and checked for this argument. Its proof uses N15 at zeros alone, not an inherited H5 minimality hypothesis.

## Two reusable local facts

Write $A$ for adjacency and $B=A^2+A-7I-J$ for the actual integer defect. The original graph is 8-regular, $AB=BA$, $B$ is nonnegative symmetric with zero diagonal, and each row sums to six.

**Zero-endpoint transport.** If $x$ is a zero vertex and $B_{rx}>0$, then

$$ (BA)_{rx}=(AB)_{rx}=B_{rx}.\tag{1} $$

Indeed, N15 at $x$ says that within the positive support of row $x$, vertex $r$ is adjacent exactly to its same-weight partner. Thus $(BA)_{xr}=B_{xr}$. Commutation and symmetry of $AB$ transport this equality to $(r,x)$.

**Weighted triangle support obstruction.** No row of $B$ can have complete positive support consisting of three vertices $a,b,c$ of weight one that form an actual triangle, a zero vertex $x$ of weight two, and a zero vertex $y$ of weight one.

To prove this, apply (1) at $x$. The value $(BA)_{rx}=2$ is the number of neighbors of $x$ among $a,b,c$, plus $A_{xy}$. A zero vertex has at most one neighbor in an actual triangle. Hence equality forces $A_{xy}=1$. Applying (1) at $y$ now gives $1=(BA)_{ry}\ge2A_{xy}=2$, a contradiction. This local obstruction does not assume that the graph has exactly two triangles or that $r$ is a zero vertex.

## The shared-edge configuration

Let the two triangles be $uvw$ and $uvz$, where $uv$ is the common edge. The tips $w,z$ are nonadjacent: a tip edge would create further triangles. Exactly $u,v$ have triangle count two, exactly $w,z$ have triangle count one, and the other 55 vertices are zero.

The true-edge defect values on these four vertices are

$$B_{uv}=2,\qquad B_{uw}=B_{uz}=B_{vw}=B_{vz}=1.$$

The shared vertices $u,v$ each have nonedge repeat budget two. Every other nonzero vertex is already adjacent to them. All their nonedge repeats therefore lie at zero vertices. The endpoint lemma rules out a weight-two repeat from a zero vertex to a two-triangle vertex, so each of $u,v$ has exactly two nonedge repeats of weight one.

Put $b=B_{wz}$. The tips have the two common neighbors $u,v$, so $b\ge1$.

## The tip-to-tip defect is exactly one

If $b\ge2$, the nonedge pair $w,z$ has at least three common neighbors. Besides $u,v$, choose a common neighbor $x$. It is zero, because the only nonzero vertices are $u,v,w,z$. It is not adjacent to $u$: otherwise $uwx$ would be a third triangle. The vertices $w,z$ are two common neighbors of $u,x$, so $B_{ux}\ge1$.

Since $x$ is zero, its positive defect entries are at most two. Equation (1) gives

$$B_{ux}=(BA)_{ux}\ge B_{uw}A_{wx}+B_{uz}A_{zx}=2.$$

Thus $B_{ux}=2$, contradicting the endpoint lemma because $t(u)=2$. It follows that

$$B_{wz}=1.\tag{2}$$

## Four-cycle integrality forces a forbidden support

For any vertex $r$, write $s_r=\sum_x B_{rx}^2$ and $s=\operatorname{tr}(B^2)=\sum_r s_r$. Each zero row contributes 10. At each shared vertex $u,v$, the true-edge entries are $2,1,1$ and the two nonedge entries are $1,1$, so $s_u=s_v=8$.

At a tip, say $w$, the three nonzero-vertex entries are $B_{wu}=B_{wv}=B_{wz}=1$. The remaining row sum is three and lies entirely at zero vertices, where positive entries are at most two. Its zero-repeat pattern is therefore either 111 or 21, with square sum respectively 3 or 5. Let these square sums at the two tips be $q_w,q_z\in\{3,5\}$. Then

$$s=55\cdot10+8+8+(3+q_w)+(3+q_z)=572+q_w+q_z.$$

The actual four-cycle count $C_4$ obeys

$$8C_4=6n+s-12T.$$

Here $n=59,T=2$, so $s+330$ is divisible by eight, or $s\equiv6\pmod8$. The three possible values of $s$ are 578, 580 and 582. Only 582 has the required residue. Consequently $q_w=q_z=5$, and both tips have zero-repeat pattern 21.

Now row $w$ has the three weight-one vertices $u,v,z$, which form the other actual triangle, together with one zero weight-two endpoint and one zero weight-one endpoint. This is exactly the weighted triangle support obstruction. The contradiction excludes the whole shared-edge configuration. $\square$

## Scope and next obligation

No solver, enumeration, repeat-support disjointness assumption or short-heavy-cycle theorem is used. Both triangles are fully specified only by sharing an edge; all possible neighborhoods outside their four vertices were preserved until the contradiction.

The reusable new mechanism is equation (1) combined with a weighted support whose zero endpoints cannot meet the prescribed internal graph. The shared-edge exclusion still depends on the endpoint lemma's own proof; its newly obtained scope is explicit zero-row N15, not a silent use of old H5-specific N4.
