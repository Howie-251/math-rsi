# Exact zero-support transport at every root

## Claim and status

In an original legal 59-vertex graph, assume the actual N15 matching row at every zero-triangle vertex. Then the following statements hold at every root $r$, including roots that lie in triangles. N15 is not assumed at such nonzero roots.

1. The zero-triangle vertices in the positive support of row $B_r$ induce a matching plus isolated vertices. Every matching edge joins equal weights. Its endpoints have no other neighbors anywhere in the positive support of $B_r$.
2. For each isolated zero support vertex $x$, its neighbors in the nonzero support form an independent set whose total $B_r$ weight is exactly $B_{rx}$.
3. If $N=\{v:t(v)>0\}$ and
   $$Q_N(r)=\sum_{\{a,b\}\subseteq N,\ A_{ab}=1}B_{ra}B_{rb},\qquad s_N(r)=\sum_{a\in N}B_{ra}^2,$$
   $$K_r=\sum_{\{x,y\}\subseteq V\setminus N,\ A_{xy}=1}B_{rx}B_{ry},$$
   then the actual row remainder satisfies the exact formula
   $$e_r=Q_2(r)-\sum_x B_{rx}^2+5=5+Q_N(r)-s_N(r)-K_r.$$
   Here $K_r=m_1(r)+4m_2(r)$, where $m_i(r)$ counts the zero support matching edges whose endpoints have weight $i$.

Status: complete new paper proof, pending independent review and Lean formalization. It is a general transport theorem under explicit zero-row N15, not a claim that every original graph satisfies N15 or that all nonzero rows have the N15 shape.

## Proof

The actual defect $B=A^2+A-7I-J$ is symmetric and nonnegative, with row sum six, and commutes with $A$. At a zero vertex $x$, its positive row has values 2211 and its support induces the two equal-weight matching edges. If $B_{rx}>0$, this gives $(BA)_{xr}=B_{xr}$. Symmetry and commutation therefore give

$$\sum_y A_{xy}B_{ry}=(BA)_{rx}=B_{rx}.\tag{1}$$

Fix $r$ and write $b_y=B_{ry}$. Suppose zero support vertices $x,y$ are adjacent. Nonnegativity and (1) give

$$b_x\ge b_y,\qquad b_y\ge b_x.$$

Hence $b_x=b_y$. Each inequality is an equality, so every other positive-support neighbor of either endpoint is absent. Thus this edge is an isolated edge in the full support graph, proving statement 1. Its equal weight is one or two because both endpoints are zero vertices.

If a zero support vertex $x$ belongs to no such edge, all its support neighbors lie in $N$. Equation (1) gives their total weight exactly $b_x$. These neighbors are independent in the original graph: an edge between two of them would give a triangle through the zero vertex $x$. This proves statement 2.

Partition the zero support into its isolated vertices and its matching edges. An isolated zero vertex $x$ contributes $b_x^2$ to the weighted sum of edges from zero support to nonzero support, by statement 2. An edge in the zero support of equal weight $k$ contributes $k^2$ to $Q_2(r)$ and $2k^2$ to the row square sum. Its endpoints contribute nothing to the cross-support sum, by statement 1. Therefore

$$Q_2(r)=Q_N(r)+\sum_{x\text{ isolated zero support}}b_x^2+K_r,$$

$$\sum_xb_x^2=s_N(r)+\sum_{x\text{ isolated zero support}}b_x^2+2K_r.$$

Subtracting proves statement 3. $\square$

## Consequences useful beyond small triangle counts

Every zero isolated repeat has weight one or two. Its actual neighbor set in the weighted nonzero support must therefore be an independent set of total weight respectively one or two. If the nonzero support is a clique of weight-one vertices, no isolated zero repeat of weight two is possible; all weight-two zero repeats must be paired with another weight-two zero repeat. In particular a complete support consisting of such a clique and zero weights 21 is impossible.

More generally the isolated-zero choices are determined by weighted independent sets in the actual graph induced on nonzero support. This supplies a finite local interface for any proposed nonzero triangle structure without imposing N15 on nonzero rows.

The global trace relation from `matching_zero_global_trace_obstruction_20261011.md` consequently becomes

$$5C_5=209\cdot59+\sum_{r\in N}\bigl(5+Q_N(r)-s_N(r)-K_r\bigr)-54T,$$

and in particular

$$\sum_{r\in N}\bigl(Q_N(r)-s_N(r)-K_r\bigr)+T\equiv4\pmod5.$$

All quantities still come from the same graph. The matching counts $K_r$ cannot be assigned independently for different roots: they refer to edges in one common zero-vertex graph. Summing them gives the explicit coupling

$$\sum_{r\in N}K_r=\sum_{\{x,y\}\subseteq V\setminus N,\ A_{xy}=1}\ \sum_{r\in N}B_{rx}B_{ry}.$$

This theorem uses no triangle-count bound, no heavy-cycle classification, no H5 root minimality, and no computation. Its application to the shared-edge $T=2$ case appears in `two_triangles_shared_edge_exclusion_20261011.md`; the shared-vertex case remains only partly reduced in the companion followup.
