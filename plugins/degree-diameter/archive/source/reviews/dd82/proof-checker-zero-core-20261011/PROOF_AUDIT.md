# Independent proof audit: zero neighbors and triangle-bearing core

Verdict: **PASS — same-family, provisional.** The two submitted papers establish their stated conditional conclusions. No open mathematical gap or counterexample was found. The strongest conclusion reviewed is that an actual legal order-59 graph satisfying N15 at every zero-triangle vertex has at least 17 triangle-bearing vertices and at least six triangles.

This is a fresh paper-proof review by `/root/proof_review_zero_core`, requested through `gpt-6-astra` with reasoning effort `ultra` and no inherited conversation. The backend did not provide separate model/effort attestation; those names record the requested route, not independently observed runtime identity. This is not cross-family acceptance or Lean verification.

## Submitted scope

The complete contents of these two papers were reviewed directly:

1. `proofs/dd82/n59/independent_zero_common_neighbors_20261011.md`, lines 1–55.
2. `proofs/dd82/n59/zero_core_pair_coverage_20261011.md`, lines 1–86.

The load-bearing source chain was read directly, with the following checked scope:

- `proofs/dd82/n59/n15_heavy_endpoints_avoid_two_triangles_20261011.md`, complete file. The endpoint proof and its two-intersecting-triangles consequence were checked; only the endpoint theorem is needed here.
- `proofs/dd82/n59/nonzero_support_transport_20261011.md`, complete file. The local transport equation, statements 1–3, and finite support-counting consequences were checked. The imported fifth-trace identity and congruence in lines 46–52 are not used by either submitted paper and are outside this verdict.
- `proofs/dd82/FOUNDATIONS.md`, sections 1–2, lines 17–43: actual-graph regularity, defect identities and triangle-repeat budget. The file was opened in full, but its order-64/65 arguments and historical status statements were not audited or used.
- `proofs/dd82/n59/zero_matching_cycle_contract_20261011.md`, line 3, and `proofs/dd82/n59/single_triangle_normal_form_exclusion_20261011.md`, lines 13–25: precise meaning of the actual N15 matching-row premise. The former was read in full and the latter's opening was read; neither paper's cycle or single-triangle exclusions are dependencies of this audit.
- `proofs/dd82/n59/matching_zero_global_trace_obstruction_20261011.md`, lines 1–64 were inspected solely for notation and the definition of the weighted support-edge sum. No trace or cycle-count result was imported.

Prior audit judgments were not used as mathematical premises. No author paper, formal file, or wiki page was changed. Per the task override, artifacts are Markdown/JSON only; no compilation or fingerprinting was performed.

## Exact hypothesis contract

Throughout, $G=(V,E)$ is one finite simple undirected graph, $|V|=59$, maximum degree at most eight, and every distinct pair is adjacent or has a common neighbor. $A$ is its integer adjacency matrix and $B=A^2+A-7I-J$ is its actual integer defect matrix. Let $t(v)$ count triangles containing $v$, $Z=\{v:t(v)=0\}$, $N=V\setminus Z$, $m=|N|$, and $T$ be the total number of triangles.

N15 is **assumed**, not derived: for every $z\in Z$, its positive $B$-row consists of four distinct entries of weights $2,2,1,1$; the induced original graph on those four vertices consists exactly of the equal-weight pair edges. In particular, cross-weight support edges are absent. N15 is never imposed on a vertex in $N$.

The graph hypothesis gives $59\le1+8\deg(v)$, so every degree is eight. Thus (B_{vv}=0), (B_{uv}=|N_G(u)\cap N_G(v)|+A_{uv}-1\ge0) for $u\ne v$, each row sums to six, and (AB=BA) because (AJ=JA=8J). On a true edge $B$ counts common neighbors, so (\sum_{u\sim v}B_{vu}=2t(v)), and the remaining nonedge budget is $6-2t(v)$. These identities were rederived from the same graph; an independently selected matrix does not suffice.

## Load-bearing dependency checks

**Heavy endpoint theorem.** Suppose $z\in Z$ and (B_{zv}=2). The pair (zv) is a nonedge. The row budget excludes $t(v)=3$ and bounds $t(v)\le3$, leaving only $t(v)=2$ to refute. In that case $H=G[N_G(v)]$ has exactly two edges, and $z$ uses the whole nonedge budget. Its three parents form an independent set $S$. Whether the two $H$-edges meet or are disjoint, their nonisolated vertices contain no independent set of size three; hence some $p\in S$ is isolated in $H$.

The eight neighbors of $p$ are $v,z$ and six ordinary children, all with sole parent $p$. None of those children is adjacent to $z$. At each child $y$, the actual equation ((AB)_{vy}=(BA)_{vy}=0), together with nonnegativity, gives (B_{py}=0). The other incident edges (pv,pz) also have defect zero, so $p\in Z$. For $q\in N_G(v)\setminus\{p\}$, the only common neighbors of $p,q$ are $v$, and additionally $z$ precisely when $q\in S\setminus\{p\}$. Therefore the two members of $S\setminus\{p\}$ are exactly the two light endpoints of $p$, which N15 makes adjacent. This contradicts independence of $S$. All uses of N15 are at verified zero vertices. Thus $t(v)\le1$.

**Transport theorem.** If $x\in Z$ and (B_{rx}>0), then $r$ belongs to the support of row $x$. Its only neighbor within that support is its equal-weight mate. Consequently ((BA)_{xr}=B_{xr}). Since $A,B$ are symmetric and commute, (BA) is symmetric, so

\[
\sum_y A_{xy}B_{ry}=(BA)_{rx}=B_{rx}.
\]

Set (b_y=B_{ry}). For adjacent zero support vertices $x,y$, this equality yields $b_x\ge b_y\ge b_x$. Equality and positivity exclude every additional positive-support neighbor of either endpoint. Thus zero support edges are isolated equal-weight pairs in the full support. A zero support vertex without such a mate has only nonzero support neighbors, with total weight exactly its own weight. Those neighbors are independent because it is zero. The paper's weighted support decomposition for statement 3 follows by counting isolated-zero contributions $b_x^2$ and paired-zero contributions $k^2,2k^2$; it introduces no extra premise. Only statements 1–2 are needed in the submitted proofs.

## Submitted derivations

**Independent zero sets and common neighbors.** For an independent $U\subseteq Z$, any $u\in U$ has at most one light and one heavy defect endpoint in $U$, because the two endpoints of either weight are adjacent in $G$. Symmetry therefore makes each weight class a matching on $U$. The union has alternating paths and even cycles, and cannot contain a triangle.

For distinct $r,s$, their common zero neighbors are independent: an edge between two would create a triangle at a zero vertex. Three such neighbors would give three nonadjacent pairs, each having common neighbors $r,s$, hence three positive defect edges. This would be a forbidden defect triangle. Thus at most two common neighbors of any distinct pair are zero. A heavy defect pair incident to a zero vertex is a nonedge with exactly three common neighbors, so at least one common neighbor belongs to $N$.

**At least two nonzero neighbors.** Let $u,v$ be the heavy endpoints of $z\in Z$. They are adjacent, and the previous conclusion gives a nonzero common neighbor for each of (zu,zv). If $z$'s only nonzero neighbor were $n$, then (nuv) would be a triangle. Hence $u,v\in N$; the endpoint theorem gives $t(u)=t(v)=1$, and therefore (B_{un}=1).

In row $u$, $z$ is a zero support vertex of weight two, while $n$ is a positive-support neighbor of $z$ of weight one. If $z$ had a zero support mate, paired-edge isolation would exclude $n$, a contradiction. Otherwise isolated-zero transport requires weight two among the nonzero support neighbors of $z$, while $n$ is its only nonzero neighbor and contributes one. This is a contradiction. Therefore $d_N(z)\ge2$. This argument never assumes N15 at root $u\in N$.

**Initial global bound and the five-triangle conditional case.** Each vertex of $N$ has at least two neighbors in $N$, so at most six in $Z$. Hence $2(59-m)\le e(N,Z)\le6m$, giving $m\ge15$, and the incidence bound $m\le3T$ gives $T\ge5$. If $T=5$, the bounds force $m=15$; equality in the union bound for five three-element triangle vertex sets makes them vertex-disjoint. Writing $e_N=15+k$ gives $e(N,Z)=90-2k\ge88$, hence $k\in\{0,1\}$. The zero-degree excess is $2-2k$, and its stated partitions are exhaustive. This conditional description becomes vacuous after the second paper excludes $T=5$; it is not a circular input to that exclusion.

**Pair coverage.** Every vertex satisfies $2\le d_N(v)\le8$, and regularity gives $\sum_v d_N(v)=8m$. The cut count gives $e_N\le5m-59$. The polynomial identity

\[
1+\tfrac92(d-2)-\binom d2=\tfrac12(d-2)(8-d)\ge0
\]

on $[2,8]$ gives $\sum_v\binom{d_N(v)}2\le36m-472$. Each term counts unordered endpoint pairs of length-two paths through that middle vertex, including middle vertices in either $N$ or $Z$.

Each adjacent pair in $N$ has its direct edge as a cover, so all its length-two covers may be deleted without uncovering the pair. Across all such pairs, the deleted covers number exactly $3T$: triangles are entirely in $N$, and a triangle contributes three edge/opposite-vertex incidences even when triangles share edges or vertices. Each nonadjacent pair still has a length-two cover by diameter two. Therefore

\[
\binom m2\le e_N+\sum_v\binom{d_N(v)}2-3T
\le(5m-59)+(36m-472)-m=40m-531.
\]

Both substitutions have the correct inequality direction: $e_N$ and the path sum are bounded above, while $3T\ge m$ bounds the negative term from above by $-m$. At $m=15,16$, the claimed inequalities would be $105\le69$ and $120\le109$. Both fail. Thus $m\ge17$, and $T\ge6$.

The equivalent defect-sum identity was also checked pair by pair: for $r\ne s$, (A_{rs}+|N_G(r)\cap N_G(s)|=1+B_{rs}). Summing over unordered $N$-pairs gives the paper's identity; the edge-pair defect sum is exactly $3T$, with nonedge terms nonnegative.

## Counterexample and boundary attacks

| Attempt | Outcome |
|---|---|
| Put three positive defect edges on an independent zero triple, allowing mixed weights | Every edge has weight one or two; a triangle has two equally weighted incident edges at some vertex. Their two endpoints would need to be adjacent by N15, contrary to independence. No candidate survives the stated hypotheses. |
| Choose adjacent $r,s$ in the common-zero-neighbor claim | Such a pair has no common zero neighbor at all, because that neighbor would lie in a triangle. Nonadjacent pairs are handled by the three-vertex argument. |
| Let the two heavy pairs of $z$ use different nonzero common neighbors | This already gives two nonzero neighbors of $z$; the contradiction assumes exactly one and only then identifies both neighbors with $n$. |
| Permit the heavy endpoint to lie in two or three triangles | Three is excluded by the actual nonedge budget. The complete $t=2$ parent proof covers both ways the two neighborhood edges can meet. |
| Pair the heavy zero repeat to absorb its weight in row $u$ | Isolation would forbid the already forced positive-support neighbor $n$. If no pair is present, the exact weight-two equation contradicts the available weight one. |
| Omit the absence of cross-weight support edges from N15 | The transport equality can acquire extra positive summands; this weakens the assumption beyond the submitted matching-row contract. It is a genuine premise boundary, not a counterexample to the stated result. |
| Use $Z=\varnothing$, or a row rooted at a nonzero vertex | With $Z=\varnothing$, the core bound is trivially satisfied and the lower degree bound comes from triangles. At a nonzero root transport uses N15 at the zero support endpoint, not at the root. |
| Use triangles sharing edges, so that subtracting $3T$ might overcount removable covers | Covers are indexed by an edge and a distinct middle vertex. Shared edges with different opposite vertices give distinct covers, all removable because the direct edge remains. |
| Let nonadjacent core pairs have many common neighbors | Extra nonadjacent covers only increase the right-hand side before bounding it. No uniqueness claim is used. |
| Test the chord at $d=2,8$ and the excluded core sizes $m=15,16$ | The chord is exact at both degree endpoints and dominates in between. Both displayed contradictions use exact integer arithmetic. |

These are algebraic/combinatorial attacks, not graph enumeration or computational certificates. None supplies a counterexample to the stated hypotheses. Failed searches are not used as a substitute for the derivations above.

## Closure and limits

All 37 obligations in the accompanying ledger are discharged by finite paper arguments under the explicit N15 premise. The dependency graph is acyclic. There are no limit exchanges, analytic convergence claims, probability-mode changes, asymptotic notation, or hidden parameter-dependent constants. No correction to the submitted papers was required.

The verdict concerns these two submitted papers and the necessary dependency portions described above. It does not establish N15 for arbitrary legal order-59 graphs, prove H5 implies the requisite global N15 condition, exclude six or more triangles, produce an order-58-or-larger graph, exclude arbitrary order 59, or determine the exact degree-diameter value. Any subsequent six-triangle work is unaudited here. Known order-63–65 exclusions were not developed, and no formal or computational result is claimed.
