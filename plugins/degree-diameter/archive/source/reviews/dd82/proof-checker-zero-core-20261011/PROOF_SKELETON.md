# Proof skeleton and assumption ledger

This ledger belongs to the fresh provisional review of exactly the two zero-core papers listed in `PROOF_AUDIT.md`. All statements below concern one actual graph. The machine-readable sequents and dependency edges are in `PROOF_OBLIGATIONS.json`.

## Typed symbols

| Symbol | Type and meaning |
|---|---|
| $G=(V,E)$ | Finite simple undirected graph; $|V|=59$, maximum degree at most eight, diameter at most two |
| $A,B,I,J$ | Integer $V\times V$ matrices; $A$ is actual adjacency, $B=A^2+A-7I-J$, $I$ identity, $J$ all ones |
| $t(v),T$ | Nonnegative integers: triangles through $v$, and all triangles respectively |
| $Z,N$ | Disjoint subsets of $V$: $t(v)=0$, and $t(v)>0$; $N$ as a set is distinct from the notation $N_G(v)$ for a neighborhood |
| $m$ | Integer $|N|\in[0,59]$ |
| $d_N(v)$ | Integer $|N_G(v)\cap N|\in[0,8]$, subsequently proved at least two |
| $e_N,e(N,Z)$ | Integer edge counts in $G[N]$, and across the $N,Z$ cut |
| $U$ | Any subset of $Z$ independent in $G$ |
| $P,Y,H,S$ | Local endpoint proof objects: $P=N_G(v)$, $Y=V\setminus(P\cup\{v\})$, $H=G[P]$, $S=N_G(z)\cap P$ |
| $b_y$ | At a fixed root $r$, actual integer row entry (B_{ry}\ge0) |
| $Q_2(r),Q_N(r),s_N(r),K_r$ | Finite weighted sums in the transport source, with each graph edge counted unordered once; (Q_2(r)=\sum_{\{x,y\}\in E}b_xb_y) |
| $k$ | Only in the conditional $T=5$ description: integer $e_N-15\ge0$ |

## Assumptions and where they are discharged

| Assumption/application | Verification |
|---|---|
| Simple undirected graph on 59 vertices, maximum degree eight, diameter two | Explicit in second submitted paper, line 5; this is the meaning of “original legal order59 graph” in the first and its dependency papers |
| Degree exactly eight | Root ball inequality $59\le1+8\deg(v)$; degree integrality and the upper bound |
| $B$ nonnegative, symmetric, diagonal zero, row sum six, commuting with $A$ | Actual adjacency formula and regularity; derived in audit and foundations sections 1–2 |
| N15 at every zero vertex | Explicit theorem premise; support induces exactly two equal-weight edges, including absence of cross-weight edges |
| N15 at selected parent $p$ in endpoint proof | Every actual incident edge at $p$ has $B=0$, proving $t(p)=0$ before N15 is applied |
| Endpoint theorem at (zu,zv) | $z\in Z$, actual (B_{zu}=B_{zv}=2), and the same global N15 premise |
| Transport at root $u\in N$ and repeat $z\in Z$ | The transport theorem allows every root; N15 is used at $z$, whose positive weight is two |
| (B_{un}=1) in the unique-neighbor contradiction | (un) is an edge in triangle (nuv); endpoint theorem bounds $t(u)\le1$, so this edge has exactly one common neighbor |
| Chord inequality applied to $d_N(v)$ | Zero vertices use the proved neighbor lemma; nonzero vertices use their triangle; maximum degree gives the upper bound eight |
| Coverage of core pairs | The actual diameter-two condition; finite unordered paths have a unique middle vertex for counting purposes |
| Deleting $3T$ duplicate covers | Every deleted path has adjacent endpoints in $N$, whose direct-edge cover is retained; every triangle lies in $N$ |
| Incidence inequality $3T\ge m$ | Every member of $N$ lies in at least one triangle, by definition |

## Canonical quantified conclusions

For every graph satisfying the graph and global N15 assumptions above:

1. For every independent $U\subseteq Z$, the positive defect graph on $U$ is a union of isolated vertices, alternating paths, and alternating even cycles, with weights one and two.
2. For all distinct $r,s\in V$, $|N_G(r)\cap N_G(s)\cap Z|\le2$.
3. For every $z\in Z$ and every $u\in V$ with (B_{zu}=2), at least one common neighbor of $z,u$ lies in $N$.
4. For every $z\in Z$, $d_N(z)\ge2$.
5. $m\ge15$ and $T\ge5$.
6. If $T=5$, then $m=15$, the five triangles are vertex-disjoint, $e_N=15+k$ for $k\in\{0,1\}$, and $\sum_{z\in Z}(d_N(z)-2)=2-2k$. For $k=1$ every zero degree is two; for $k=0$ there is either one zero degree four or two zero degrees three, all remaining zero degrees being two.
7. $\binom m2\le40m-531$.
8. $m\ge17$ and $T\ge6$.

The sixth statement is a valid conditional intermediate statement whose premise is excluded by the eighth. It is never used to prove the seventh or eighth.

## Dependency graph

\[
\text{actual graph}\to\text{regularity}\to\text{defect identities/budget}.
\]

\[
\text{defect identities/budget + global N15}\to
\begin{cases}
\text{heavy endpoint theorem},\\
\text{zero-support transport},\\
\text{independent-zero defect structure}\to\text{common-zero bound}.
\end{cases}
\]

\[
\text{common-zero bound + heavy endpoint + transport}
\to d_N(z)\ge2
\to
\begin{cases}
m\ge15,\ T\ge5\to(T=5\text{ conditional structure}),\\
\text{degree chord + pair coverage + triangle incidence}\to
\binom m2\le40m-531\to m\ge17,\ T\ge6.
\end{cases}
\]

The optional support-remainder identity depends on transport only and has no outgoing edge to either submitted proof. Fifth-trace formulas, cycle exclusions, H5 minimality, and any six-triangle followup are absent from this DAG.

## Obligation groups

| IDs | Content | Outcome |
|---|---|---|
| F01–F05 | Actual graph foundations and exact N15 premise | Discharged; F05 is an explicit assumption, not an inferred theorem |
| E01–E07 | Complete heavy-endpoint derivation | Discharged |
| X01–X05 | Transport symmetry, paired/isolated support and weighted decomposition | Discharged |
| I01–I11 | First submitted paper, including its conditional $T=5$ description | Discharged |
| C01–C09 | Second submitted paper, both coverage derivations and final bound | Discharged |

All 37 sequents include their supporting rule and dependency IDs in `PROOF_OBLIGATIONS.json`. “Discharged” is a paper-review finding under the stated premise, not kernel evidence. There are no limiting operations, probability modes or asymptotic parameters, so the limit-order map is empty.
