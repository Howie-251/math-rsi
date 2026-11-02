# Proof Package: global heavy-repeat capacity under N15

## Claim

Let $G$ be a simple undirected graph on $59$ vertices, of maximum degree at most $8$, in which every two distinct vertices are joined by a path of length at most $2$. Suppose that every vertex lying in no triangle satisfies the actual N15 condition: its defect row has exactly two entries equal to $2$ and two entries equal to $1$, and the two endpoints of each equal weight are adjacent in $G$.

Let $Z$ be the vertices lying in no triangle, $N=V(G)\setminus Z$, $m=|N|$, and $T$ the number of triangles. Then

$$59\le4m-3T,\qquad m\ge20,\qquad T\ge7.$$

The hypothesis may in particular be the exact induced-matching version of N15 used elsewhere in this project; this proof only needs the equal-weight endpoint adjacencies.

## Status

PROVABLE AS STATED under the explicit N15 hypothesis. Complete new paper derivation, awaiting independent review. The root agent supplied the global heavy-capacity argument; this file gives its complete derivation and a nonnegative-slack identity. The argument does not use the zero-heavy endpoint lemma, the zero-support transport theorem, the separate lower bound on $d_N(z)$, or a classification of triangle configurations.

## Assumptions and notation

A degree-at-most-$7$ root would reach at most $1+7+7\cdot7=57$ vertices in two steps, so $G$ is $8$-regular. Let $A$ be its adjacency matrix, $I$ the identity matrix, $J$ the all-ones matrix, and

$$B=A^2+A-7I-J.$$

Then $B$ is symmetric, has zero diagonal, is nonnegative, and has row sum $6$. For distinct vertices $x,y$, write $c(x,y)$ for their number of common neighbors. Thus $B_{xy}=c(x,y)$ on an edge and $B_{xy}=c(x,y)-1$ on a nonedge. Let $t(x)$ be the number of triangles through $x$. Since each triangle through $x$ contributes to exactly two incident edges,

$$\sum_{y\sim x}B_{xy}=2t(x),\qquad
\sum_{y\notin N_G[x]}B_{xy}=6-2t(x).\tag{1}$$

Here $N_G[x]=N_G(x)\cup\{x\}$ is the closed neighborhood. In particular $\sum_{n\in N}t(n)=3T$.

A pair $\{x,y\}$ with $B_{xy}=2$ is called a heavy defect edge, whether or not it is an original graph edge. When one endpoint is zero, the pair is necessarily a nonedge of $G$: a genuine edge incident with a zero vertex has no common neighbor and has defect value zero.

## Proof strategy and dependency map

1. N15 restricts each weight class of defect edges on an independent zero set to a matching.
2. This forbids three zero common neighbors of any pair of distinct vertices.
3. At a nonzero root, its zero neighbors have a controlled weighted defect total. Every zero heavy repeat of the root consumes one unit of otherwise unavailable capacity.
4. Every heavy defect edge between zeros is seen in at least one nonzero root neighborhood. Summing the local bound therefore pays for all heavy incidences of zero vertices.
5. Triangle incidence then gives the numerical lower bounds.

## Proof

**Step 1. Common zero neighbors are at most two.** Let $U\subseteq Z$ be independent in $G$. For each $u\in U$, its two weight-one defect endpoints are adjacent, so at most one of them belongs to $U$. Its two weight-two endpoints are adjacent, giving the same conclusion for weight two. Consequently, each weight class in the positive defect graph on $U$ is a matching. This positive defect graph has no triangle: on three vertices, a triangle whose edges use only two weights has two incident edges of one weight, contradicting the matching condition.

Now let $r\ne s$. Their common zero neighbors form an independent set, because an edge between two of them would give a triangle containing a zero vertex. If they had three common zero neighbors $u,v,w$, every pair from $\{u,v,w\}$ would be a nonedge with the two common neighbors $r,s$, and therefore would have positive defect. This is the forbidden defect triangle. Hence

$$|N_G(r)\cap N_G(s)\cap Z|\le2.\tag{2}$$

A heavy defect edge with a zero endpoint is a nonedge with exactly three common neighbors. By (2), at least one of these common neighbors lies in $N$.

**Step 2. Exact counting at a nonzero root.** Fix $n\in N$ and put

$$U_n=N_G(n)\cap Z.$$

This set is independent. Let $\ell_n$ and $h_n$ count, respectively, its unordered pairs with defect value $1$ and $2$. N15 excludes any other positive defect value at a zero endpoint. Let

$$k_n=|\{y\in Z:B_{ny}=2\}|.$$

For $y\notin N_G[n]$, set $q_y=|N_G(y)\cap U_n|$. By (2), $q_y\le2$.

For any distinct $z,w\in U_n$, the root $n$ is one common neighbor. Every other common neighbor lies outside $N_G[n]$. Indeed, if $y\in N_G(n)$ were adjacent to $z$, then $n,y,z$ would be a triangle containing the zero vertex $z$. Since $z,w$ are nonadjacent, their defect counts exactly the common neighbors other than $n$. Double counting gives

$$\ell_n+2h_n
=\sum_{\{z,w\}\subseteq U_n}B_{zw}
=\sum_{y\notin N_G[n]}\binom{q_y}{2}.\tag{3}$$

For every $y$ in the last sum, $B_{ny}$ is nonnegative. If $q_y\le1$, then $\binom{q_y}{2}=0\le B_{ny}$. If $q_y=2$, the two vertices counted by $q_y$ are common neighbors of the nonedge $n,y$, so $B_{ny}\ge1=\binom{q_y}{2}$. Thus

$$\binom{q_y}{2}\le B_{ny}.$$

For each of the $k_n$ zero heavy endpoints $y$, one has $B_{ny}=2$ while $\binom{q_y}{2}\le1$, improving this bound by at least one. Summing and using (1) and (3) proves

$$\ell_n+2h_n+k_n\le6-2t(n),$$

and in particular

$$2h_n+k_n\le6-2t(n).\tag{4}$$

**Step 3. Summing the capacity.** Let $H_{ZZ}$ be the number of heavy defect edges with both endpoints in $Z$, and let $K_{ZN}$ be the number with one endpoint in each of $Z,N$. N15 gives every zero vertex exactly two heavy endpoints, so

$$2|Z|=2H_{ZZ}+K_{ZN}.\tag{5}$$

By the conclusion of Step 1, every heavy defect edge between two zeros has at least one common neighbor in $N$. For every such common neighbor $n$, the edge is counted by $h_n$. Therefore

$$H_{ZZ}\le\sum_{n\in N}h_n.\tag{6}$$

Also $K_{ZN}=\sum_{n\in N}k_n$. Sum (4) over $n\in N$, then use (5), (6), and $\sum_n t(n)=3T$ to obtain

$$2(59-m)=2|Z|
\le2\sum_{n\in N}h_n+\sum_{n\in N}k_n
\le6m-6T.$$

Rearranging gives

$$59\le4m-3T.\tag{7}$$

Every vertex of $N$ lies in at least one triangle, so $m\le3T$. Hence

$$59\le4m-3T\le3m,$$

which gives $m\ge20$. The same incidence bound also yields

$$59\le4m-3T\le9T,$$

which gives $T\ge7$. $\square$

## Exact slack and the smallest remaining case

The proof also identifies all slack in (7). Define

$$R_n=\sum_{y\notin N_G[n]}
\left(B_{ny}-\binom{q_y}{2}
-\mathbf1_{\{y\in Z,\ B_{ny}=2\}}\right).$$

The pointwise argument in Step 2 shows $R_n\ge0$. Let

$$D=\sum_{n\in N}h_n-H_{ZZ}\ge0.$$

Subtracting (5) from the exact sum of (3) and the nonedge row budgets gives

$$2(4m-3T-59)
=\sum_{n\in N}\ell_n+2D+\sum_{n\in N}R_n.\tag{8}$$

In particular, if $T=7$ and $m=20$, then every term on the right of (8) vanishes. Thus:

- No light defect edge between two zeros has a nonzero common neighbor.
- Every heavy defect edge between two zeros has exactly one nonzero common neighbor, and consequently exactly two zero common neighbors.
- For every nonzero root $n$ and every zero heavy endpoint $y$, the pair $n,y$ has exactly two zero common neighbors.
- Every nonedge repeat of a nonzero root that is not a zero heavy endpoint has defect at most one; when its defect is one, it has exactly two zero common neighbors and no other common neighbor.

The last two statements follow pointwise from $R_n=0$ and $q_y\le2$. In particular there are no heavy defect nonedges with both endpoints in $N$ in this equality case. These are necessary conditions, not an exclusion of $T=7,m=20$.

## Scope and open risks

The proof excludes every triangle count $T\le6$ under the stated global N15 hypothesis, and requires at least twenty vertices to lie in triangles. It does not prove N15 for arbitrary legal graphs, exclude all remaining N15 graphs, or close H5. The entire new argument is finite counting on the actual graph; it does not use an independently assigned defect matrix, a matrix relaxation, computation, or an unproved short-cycle classification. Independent paper review passed; exact scope remains as stated.

## Current review status

Fresh same-family delta audit PASS22 obligations in reviews/dd82/proof-checker-zero-core-20261011/DELTA_PROOF_AUDIT.md. Gemini B11 accepted the complete argument (reviews/dd82/20261011_B11_global_capacity_lean.json), with zero reviewer commands. Global count not yet Lean.

Gemini B11 read and accepted the complete paper; raw response is saved in reviews/dd82/20261011_B11_global_capacity_lean.json. The reviewer executed no commands.
