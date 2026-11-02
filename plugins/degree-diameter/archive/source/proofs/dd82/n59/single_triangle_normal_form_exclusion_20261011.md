# Proof Package: exclusion of the surviving single-triangle normal form

## Claim and status

Let $G$ be a simple undirected graph on 59 vertices, with maximum degree at most 8 and the explicit one-or-two-edge path property. Suppose that every vertex lying in no triangle satisfies the N15 matching-row condition stated below. Then $G$ cannot have exactly one triangle.

The proof has two parts: the already established single-triangle normal-form theorem, recalled precisely below, and a new contradiction showing that this normal form cannot be jointly realized. Every step of the new contradiction is included here. The normal-form reduction is proved in `h5_nonzero_trace_constraints_20261011.md`, Steps 1–9; this file does not silently replace that dependency with an unproved classification.

Status: complete paper proof; fresh proof-checker-single-triangle-20261011 discharged all32 obligations and Gemini B7 independently accepted the full new argument and its dependency. See reviews/dd82/20261011_B7_single_triangle.json. Lean formalization remains pending.

Combined with `matching_zero_global_trace_obstruction_20261011.md`, this shows that a graph with N15 at all zero-triangle vertices must have at least two triangles. In particular it removes $T=0$ and $T=1$ from H5 after its N15 premise is established. It does not exclude all H5, any other surviving n59 representative, or the whole degree/diameter problem.

## Matrices and the exact N15 premise

The root ball count makes $G$ 8-regular. Let $A$ be the actual integer adjacency matrix and

$$B=A^2+A-7I-J.$$

It is symmetric, has zero diagonal, is entrywise nonnegative, and has every row sum six. For distinct vertices,

$$B_{xy}=|N(x)\cap N(y)|+A_{xy}-1.$$

Call a vertex zero if it lies in no triangle. At every zero vertex $x$, assume that its entire positive $B$ row has values $2,2,1,1$, and that the induced graph on these four support vertices consists exactly of an edge joining the two weight-two vertices and an edge joining the two weight-one vertices. Thus the two light endpoints are adjacent, and so are the two heavy endpoints. A genuine edge incident to a zero vertex has $B$ value zero.

Write $R_2$ for the graph of nonadjacent pairs with $B=2$. All occurrences of $A$, $B$, neighborhoods and repeated endpoints below belong to this same original graph.

## Normal-form input

Assume for contradiction that the unique triangle is $uvw$. The cited normal-form theorem allows these labels to be chosen so that the following hold.

1. The three private neighborhoods
   $$P_u=N(u)\setminus\{v,w\},\quad P_v=N(v)\setminus\{u,w\},\quad P_w=N(w)\setminus\{u,v\}$$
   are disjoint sets of six zero vertices. Each is independent. Between these three sets there are exactly two edges, forming a matching between $P_u$ and $P_v$; there are no $P_u$–$P_w$ or $P_v$–$P_w$ edges.
2. Put
   $$R=V(G)\setminus(\{u,v,w\}\cup P_u\cup P_v\cup P_w),\qquad |R|=38.$$
   Every vertex of $R$ is zero and is adjacent to none of $u,v,w$.
3. Each triangle vertex has four nonedge repeats, all of weight one. Its repeats in $R$ are
   $$R_u=\{x\in R:B_{ux}=1\},\quad R_v=\{x\in R:B_{vx}=1\},\quad R_w=\{x\in R:B_{wx}=1\},$$
   with
   $$|R_u|=|R_v|=2,\qquad |R_w|=4.$$
   The two vertices of $R_u$ are adjacent; the two vertices of $R_v$ are adjacent. The four vertices of $R_w$ induce two disjoint edges. The sets $R_u,R_v,R_w$ are not assumed disjoint.

The proof below uses the displayed cardinality $|R_w|=4$ explicitly. It does not require the short-cycle exclusions for $R_2$, including the C9 argument, or the separate inherited N4 or N5 results.

## Proof of the new contradiction

**1. Exact degrees from $R$ into the three private neighborhoods.** For $x\in R$, its common neighbors with $u$ are exactly its neighbors in $P_u$: it is adjacent to neither $v$ nor $w$. Since $x,u$ are nonadjacent,

$$d_{P_u}(x)=1+B_{ux}=1+\mathbf1_{R_u}(x).\tag{1}$$

The corresponding formulas hold for $P_v$ and $P_w$.

Call the two endpoints in $P_u$ of the actual cross matching active, and call its other four points inactive. Use the same terminology in $P_v$. Because the cross edges form a matching, for $p\in P_u$ the common neighbors of $p$ with $v$ are $u$ and the neighbors of $p$ in $P_v$. Therefore

$$B_{pv}=d_{P_v}(p)=\begin{cases}1,&p\text{ active},\\0,&p\text{ inactive}.\end{cases}\tag{2}$$

The analogous statement holds on the $v$ side.

**2. The defect within $P_u$ and $P_v$.** For distinct $p,q\in P_u$, their common neighbors consist of $u$ and their common neighbors in $R$. There are no other common neighbors: $P_u$ is independent, its edges to $P_v$ form a matching, and it has no edges to $P_w$. Hence

$$B_{pq}=|N(p)\cap N(q)\cap R|.\tag{3}$$

By (1), the only vertices of $R$ with two neighbors in $P_u$ are the two points of $R_u$. They are adjacent to each other, so their two parent pairs in $P_u$ must be disjoint; a shared parent would create an additional triangle. Thus $B[P_u,P_u]$ has exactly two disjoint weight-one edges and no weight-two edge.

None of the four endpoints of these internal light edges can be active. Indeed, if active $p$ has internal light partner $q\in P_u$, then (2) says that $v$ is its other light endpoint. N15 would force $qv$ to be an edge, impossible because $q\in P_u$ is a private neighbor of $u$. Consequently those four endpoints are exactly the four inactive points. The same conclusions hold for $P_v$.

**3. Light entries across the private neighborhoods.** There is no weight-one entry between $P_u$ and $P_w$.

For active $p\in P_u$, the light endpoint $v$ is already present by (2). A second light endpoint in $P_w$ would have to be adjacent to $v$, but no point of $P_w$ is adjacent to $v$.

For inactive $p\in P_u$, one light endpoint is its inactive internal mate $p'\in P_u$ from Step 2. A second light endpoint in $P_w$ would have to be adjacent to $p'$, contradicting the absence of $P_u$–$P_w$ edges.

There are at most two weight-one entries between $P_u$ and $P_v$, counted as unordered cross pairs. If $p\in P_u$ is inactive, its internal light mate is inactive and has no neighbors in $P_v$, so N15 forbids any light endpoint of $p$ in $P_v$. The symmetric argument rules out every inactive endpoint on the $v$ side. Therefore a cross light entry must join active points on both sides. Of their four possible pairs, two are the actual cross matching edges and have $B=0$, because their endpoints are zero vertices. At most the remaining two pairs can have $B=1$.

**4. Two mandatory heavy-edge counts.** Define

$$h_{uv}=|R_u\cap R_v|,\qquad h_{uw}=|R_u\cap R_w|.$$

For a pair in $P_u\times P_v$, every common neighbor lies in $R$. Summing common-neighbor counts and using (1) gives

\[
\begin{aligned}
\sum_{p\in P_u,\,q\in P_v}(A^2)_{pq}
 &=\sum_{x\in R}(1+\mathbf1_{R_u}(x))(1+\mathbf1_{R_v}(x))\\
 &=38+2+2+h_{uv}=42+h_{uv}.
\end{aligned}
\]

There are two actual edges in this block and 36 cross pairs. The defining equation for $B$ therefore gives

$$\sum_{p\in P_u,\,q\in P_v}B_{pq}=42+h_{uv}+2-36=8+h_{uv}.\tag{4}$$

Every entry is zero, one or two, since its endpoints are zero vertices. Step 3 allows at most two entries of value one. If $k_{uv}$ counts the heavy pairs in this block, then

$$2k_{uv}\ge 8+h_{uv}-2\ge6,\qquad k_{uv}\ge3.\tag{5}$$

Similarly, every common neighbor of a $P_u$–$P_w$ pair lies in $R$. There are no actual cross edges here, and $|R_w|=4$, so

\[
\begin{aligned}
\sum_{p\in P_u,\,q\in P_w}B_{pq}
 &=\sum_{x\in R}(1+\mathbf1_{R_u}(x))(1+\mathbf1_{R_w}(x))-36\\
 &=38+2+4+h_{uw}-36=8+h_{uw}.
\end{aligned}
\]

Step 3 excludes all light entries from this block. Thus its number $k_{uw}$ of heavy pairs satisfies

$$2k_{uw}=8+h_{uw}\ge8,\qquad k_{uw}\ge4.\tag{6}$$

These are consequences of common neighbors in the same graph, not independent choices of defect entries or freely assigned overlap parameters.

**5. Six available endpoints cannot carry seven heavy pairs.** The union $P_v\cup P_w$ is an independent set in $G$: each private neighborhood is independent, and there are no edges between these two neighborhoods. At any $p\in P_u$, its two heavy $B$ endpoints must be adjacent by N15. They therefore cannot both lie in $P_v\cup P_w$. Each of the six points in $P_u$ has at most one heavy endpoint in this union, giving

$$k_{uv}+k_{uw}\le6.$$

But (5) and (6) give $k_{uv}+k_{uw}\ge3+4=7$. This contradiction excludes the normal form, and hence excludes exactly one triangle under the stated N15 premise. $\square$

## Scope, verification and next obligation

No finite enumeration was used in this new proof. All inequalities remain valid for arbitrary overlaps among $R_u,R_v,R_w$; no disjointness guard was introduced. The only prior mathematical reduction is the stated single-triangle normal form, whose complete derivation is in the cited file. The short-cycle papers and exploratory computation artifacts are unnecessary dependencies here.

The coordinate-agent check independently confirmed the two block totals $8+h_{uv}$ and $8+h_{uw}$ and the endpoint-capacity contradiction while this proof was being written. Fresh same-family and Gemini reviews now both cover this new argument; their evidence is recorded above. The next unresolved H5 obligation begins with configurations containing at least two triangles, including both intersecting and disjoint triangles; the present proof does not classify those configurations.
