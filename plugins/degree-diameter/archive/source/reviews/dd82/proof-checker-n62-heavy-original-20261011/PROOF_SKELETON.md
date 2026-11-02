# Heavy-original-subgraph proof obligations

Reviewed input: `proofs/dd82/n62/CONNECTED_REPEAT_HEAVY_ORIGINAL_SUBGRAPH.md`, full 307-line version read on 2026-10-11. This is a bounded review of the new deductions and the directly used source statements, not a rerun of earlier quotient classifications.

## Context and symbols

The quantified context is an actual simple graph on 62 vertices, maximum degree at most eight, diameter at most two, with connected positive repeat support. Its adjacency matrix is $A$; its actual repeat matrix is $B=A^2+A-7I-J$. The imported reductions give 8-regularity, repeat row sum three, commutation, triangle-freeness, only D1 doubles, and $d\in\{1,3,5,7,9\}$.

- $D\subseteq V(G)$: the $2d$ double-repeat endpoints; $h:D\to D$: their fixed-point-free mate involution; $a:D\to V(G)\setminus D$: unit mate map, not assumed injective.
- $D_i$: the $i$-th heavy pair; $S_i=N_G(x)\cap N_G(h(x))$: its generated unit repeat triangle; $S=\bigcup_iS_i$; $W=V(G)\setminus(D\cup S)$.
- $Q=A[D]$, $H$: the heavy-mate permutation matrix; $F$: the simple original-adjacency quotient on the $d$ pairs; $r_i=\deg_F(i)$; $m=|E(F)|$.
- $Z\in\mathbb Z^{d\times d}$: signed adjacency on the antisymmetric mate subspace. It is different from the original adjacency $Q$, the repeat matrix $B$, and the heavy-port multigraph in the separate port-closure paper.
- $e_B(S,W)$, $e_B(W)$: unordered positive repeat-edge counts, whose weights are one in the stated sets. These are not original-edge counts.

## Imported hypotheses and source discharge

| Import | Source read | Use |
|---|---|---|
| Actual identities and connected-case reductions | `CONNECTED_REPEAT_REDUCTION.md`, especially Section 4 | Context, range of $d$, triangle-freeness and D1 coverage |
| Exact D1 rows, distinct nonheavy unit mates, normalization at either heavy endpoint; distinct ports $4,b,c$, with $4\sim_G0$, $b\sim_Gw$ | `D1_MATCH_HARD_BRANCH_REDUCTION.md`, context and Sections 1–5 | Repeat-row algebra, unrestricted choice of heavy root, port positions |
| Fully unit row $B_4=e_1+e_f+e_g$; light mates in no unit repeat triangle | `D1_MATCH_C4_TRANSPORT_REFINEMENT.md`, Sections 1, 2, 5 | Degree bound four and absence of repeat edges from $D$ to $S$ |
| Exact generated triples, their disjointness, separation from $D$, no repeat edges $D$–$S$ | `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`, Sections 1 and 5 | Lift blocks, four-cycle argument, pair counting, size and port accounting |

The hard-branch statements were checked against their displayed commutation derivations. The connected-reduction classification and its earlier theorem imports remain established upstream inputs; this review does not certify their entire recursive source chain anew. `CONNECTED_REPEAT_HEAVY_PORT_CLOSURE.md` was read only to check that its multigraph is correctly distinguished from $F$.

## Dependency order and discharged obligations

The dependency order is imported actual/D1 facts → O1–O4 → O5–O6 → O7–O9; O1–O4 and source port facts → O10–O12. There is no dependency on a conclusion of this note in its imported hypotheses.

| ID | Explicit obligation | Discharge |
|---|---|---|
| O1 | For every $x,y\in D$, commutation implies mate symmetry and unit-mate reciprocity, including equal or mate indices. | Integer equation (2u=v), $u\in\{-1,0,1\}$, $v\in\{-1,0,1\}$, forces $u=v=0$; replace $y$ by $h(y)$. |
| O2 | $G[D]$ is a two-fold lift of a simple $d$-vertex graph and has $2m$ edges. | Mate-symmetric $2\times2$ blocks have form $[[p,q],[q,p]]$; both entries one would give a heavy pair a common neighbor in $D$. No within-pair edge exists. |
| O3 | $G[D]$ has neither a triangle nor a four-cycle. | Triangle-freeness is imported. Opposite four-cycle vertices are either mates, with no heavy common neighbor, or nonmates with $B_{xy}=0$ and at most one common neighbor in all of $G$. |
| O4 | Every $r_i\le4$, and each base triangle or four-cycle has negative sign product. | At an arbitrary D1 root, labels 1–3 are nonheavy and label 4 has a fully unit repeat row. Positive short-cycle product would give a short cycle in the lift. |
| O5 | $\sum_i r_i^2\le2d(d-1)$, and equality yields equation (6). | Count two-edge paths by unordered endpoint pair; adjacent and mate pairs contribute zero and each remaining pair at most one. Equality forces every remaining pair to contribute exactly one. Diagonal and mate entries of $6$ checked separately. |
| O6 | At equality, $Z^2+Z=\operatorname{diag}(r_i)$, so edges of $F$ join equal-degree vertices. | On the mate-antisymmetric subspace $H=-I,J=0$; pair degrees agree. Commuting $Z$ with its polynomial gives $(r_j-r_i)Z_{ij}=0$. |
| O7 | If $d=5$, $m\le6$. | Cauchy gives $m\le7$. At 7, the unique permitted degree multiset is $3^4,2$; equality and O6 leave the degree-two vertex no possible neighbor. |
| O8 | If $d=7$, $m\le11$. | Cauchy gives $m\le12$. At 12, degrees are $4^3,3^4$; each degree-four vertex would have at most two eligible neighbors. |
| O9 | If $d=9$, $m\le17$; together with $d=1,3$, original-edge bounds are $0,6,12,22,34$. | At $m=18$, all degrees are four and $Z^2+Z=4I_9$. The irreducible rational polynomial $t^2+t-4$ requires even dimension for a rational matrix satisfying it. For $d=1,3$, simplicity suffices. |
| O10 | If distinct $i,j$ have base distance at most two, $E_G(D_i,S_j)=\varnothing$. | A lifted edge gives a forbidden triangle; a lifted two-edge path and a putative edge into $S_j$ give two distinct common neighbors of nonmate heavy endpoints. Distinctness uses $D\cap S=\varnothing$. |
| O11 | If all base vertices are within distance two, $\lvert E_G(D,W)\rvert=10d-4m$. | Degree sum $16d$ minus internal contribution $4m$ and own-generated-triangle contribution $6d$. No unconditional diameter assertion is used. |
| O12 | If additionally $d=9$, $e_B(W)\le7$. | Each generated triple has two external repeat ports in $W$, hence $e_B(S,W)\ge18$. Its parity is odd since the 27 external incidences subtract twice the inter-triple edges, so it is at least 19. Then $2e_B(W)+18+e_B(S,W)=51$. |

No asymptotic statements, probability claims, analytic interchanges, or parameter-uniformity obligations occur. Relabeling is used only through the established D1 normal form, with reroot coverage at both heavy endpoints.
