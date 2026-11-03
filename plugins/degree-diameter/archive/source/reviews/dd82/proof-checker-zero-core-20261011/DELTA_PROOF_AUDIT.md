# Delta proof audit: global heavy-repeat capacity

Verdict: **PASS — same-family, provisional.** The complete new paper `proofs/dd82/n59/zero_heavy_global_capacity_20261011.md`, lines 1–134, proves

\[
59\le4m-3T,\qquad m\ge20,\qquad T\ge7
\]

under its explicit N15 hypothesis. The exact slack identity and all four stated necessary conditions for $T=7,m=20$ are also justified. No open gap, invalid step, or counterexample was found.

This delta was requested after the original two-paper audit was completed. The original `PROOF_AUDIT.*`, `PROOF_SKELETON.md`, `PROOF_OBLIGATIONS.json`, and `PROOF_CHECK_STATE.json` remain a separate, frozen review of those two papers. This delta adds exactly one submitted paper; it does not retroactively change that earlier input set.

The reviewer is the same `/root/proof_review_zero_core` agent as the immediately preceding audit, initially spawned with the requested `gpt-6-astra` / `ultra` / no-history route. This delta is not a second independent reviewer or a fresh context relative to that audit. The complete new artifact was read directly, and its argument was checked independently of the parent message's proposed derivation. Backend model and effort were not separately attested. This remains same-family provisional paper review, without cross-family or formal acceptance.

## Exact scope and assumptions

The sole additional submitted source is the complete global-capacity paper. Its proof is self-contained apart from elementary graph counting, which is explicitly derived. The earlier endpoint theorem, transport theorem, lower bound $d_N(z)\ge2$, pair-coverage inequality, and all trace or short-cycle results are **not dependencies** of this new theorem.

The graph is finite, simple, undirected, of order 59, maximum degree eight and diameter at most two. $A$ and $B=A^2+A-7I-J$ are the actual matrices of that one graph. At each zero-triangle vertex, N15 requires exactly two entries of weight two and two of weight one, with the two endpoints of each equal weight adjacent in the original graph.

The absence of mixed-weight support edges is unnecessary here. The row sum is six, so the specified entries already consume the entire nonnegative row sum and no additional positive entries can occur. Thus this paper's weaker wording still guarantees the exact $2211$ positive row needed by its proof.

Write $Z=\{v:t(v)=0\}$, $N=V\setminus Z$, $m=|N|$, and let $T$ count triangles. The actual-graph identities yield eight-regularity, $B\ge0$, zero diagonal, row sum six, and the nonedge budget $6-2t(n)$. They also give $\sum_{n\in N}t(n)=3T$ and $m\le3T$.

## Direct proof review

**Common zero neighbors.** On any independent subset of $Z$, the defect edges of each weight are a matching: two same-weight endpoints must be adjacent in the original graph, so cannot both belong to that independent subset. The positive defect graph on that subset therefore has no triangle. For any distinct $r,s$, their common zero neighbors are independent. Three would create a positive defect triangle because every pair among them is nonadjacent and has common neighbors $r,s$. Thus every pair has at most two common zero neighbors.

Any $B=2$ pair with a zero endpoint is a nonedge and has exactly three common neighbors. At least one of those belongs to $N$. This conclusion needs no endpoint triangle-count bound or transport identity.

**Exact local count.** Fix $n\in N$, and set $U_n=N_G(n)\cap Z$. This is independent. Let $\ell_n,h_n$ count unordered pairs in $U_n$ with defects one and two, respectively. For $y\notin N_G[n]$, write $q_{n,y}=|N_G(y)\cap U_n|\le2$, with the bound supplied by the preceding common-zero result for the distinct pair $n,y$.

For $z,w\in U_n$, $n$ is a common neighbor. No other common neighbor lies in $N_G[n]$: any such vertex adjacent to $z$ would form a triangle with $n,z$. Since (zw) is a nonedge, (B_{zw}) counts precisely those remaining common neighbors. Therefore

\[
\ell_n+2h_n=\sum_{y\notin N_G[n]}\binom{q_{n,y}}2.
\]

The right side counts each pair and middle vertex exactly once. It does not presume uniqueness of a common neighbor.

Let (k_n=|\{y\in Z:B_{ny}=2\}|). All these endpoints lie outside $N_G[n]$, since true edges incident to a zero have defect zero. For every $y\notin N_G[n]$, define

\[
\rho_{n,y}=B_{ny}-\binom{q_{n,y}}2
-\mathbf1_{\{y\in Z,\ B_{ny}=2\}}.
\]

Every $\rho_{n,y}\ge0$. If $q_{n,y}\le1$, the binomial term is zero and the indicator either vanishes or subtracts one from the value two. If $q_{n,y}=2$, the nonedge (ny) has at least two common neighbors, so (B_{ny}\ge1); in the indicator-one case its value is exactly two and the residual is zero. Hence, with $R_n=\sum_y\rho_{n,y}\ge0$, the exact local equation is

\[
6-2t(n)=\ell_n+2h_n+k_n+R_n.
\]

Dropping $\ell_n,R_n\ge0$ gives precisely $2h_n+k_n\le6-2t(n)$. No heavy endpoint is omitted from the sum, and the coefficient of $k_n$ is one.

**Global accounting.** Let (H_{ZZ}) count unordered heavy pairs within $Z$ and (K_{ZN}) count heavy pairs across $Z,N$. Each zero vertex has exactly two heavy endpoints, giving

\[
2|Z|=2H_{ZZ}+K_{ZN},\qquad K_{ZN}=\sum_{n\in N}k_n.
\]

For a heavy pair $e=\{z,w\}\subseteq Z$, let $a_e=|N_G(z)\cap N_G(w)\cap N|\ge1$. Its contribution to $\sum_n h_n$ is exactly $a_e$. Thus

\[
\sum_n h_n=\sum_e a_e\ge H_{ZZ},\qquad
D=\sum_n h_n-H_{ZZ}=\sum_e(a_e-1)\ge0.
\]

Multiple nonzero common neighbors increase this quantity; no injection or unique assignment of pairs to roots is assumed. Summing the local inequality consequently yields

\[
2(59-m)=2H_{ZZ}+K_{ZN}
\le2\sum_nh_n+\sum_nk_n
\le6m-6T.
\]

This is $59\le4m-3T$. Since $m\le3T$, both $4m-3T\le3m$ and $4m-3T\le9T$ hold, so integrality yields $m\ge20$, $T\ge7$. These are lower bounds under the explicit global zero-row premise, not an exclusion of all such graphs.

## Slack and equality case

Summing the **exact** local equations gives

\[
6m-6T=\sum_n\ell_n+2\sum_nh_n+K_{ZN}+\sum_nR_n.
\]

Subtracting (2|Z|=2H_{ZZ}+K_{ZN}) produces exactly

\[
2(4m-3T-59)=\sum_n\ell_n+2D+\sum_nR_n.
\]

All terms are nonnegative integers. At $T=7,m=20$, the left side is zero. Thus each $\ell_n=0$, $D=0$, and each $R_n=0$. Because the individual residuals $\rho_{n,y}\ge0$, each of them is also zero. The four conclusions follow separately:

1. A light (ZZ) pair with a nonzero common neighbor $n$ would contribute to $\ell_n$, impossible.
2. $D=\sum_e(a_e-1)=0$, with each $a_e\ge1$, forces every heavy (ZZ) pair to have exactly one nonzero common neighbor. Its total is three, leaving exactly two zero common neighbors.
3. For a zero heavy endpoint $y$ of $n\in N$, the pointwise residual is $1-\binom{q_{n,y}}2=0$. Since $q_{n,y}\le2$, it equals two, giving exactly two zero common neighbors.
4. For a positive nonedge repeat (ny) that is not a zero heavy endpoint, the indicator is zero and (B_{ny}=\binom{q_{n,y}}2\le1). Positivity forces (B_{ny}=1) and $q_{n,y}=2$. The nonedge has exactly (1+B_{ny}=2) common neighbors, so both are zero and there is no other common neighbor. In particular a heavy nonedge with both endpoints in $N$ is impossible in this equality case.

The paper does not claim these conclusions for $T=7,m=21$, nor does it claim that the $T=7,m=20$ case has been excluded. Both scope distinctions are necessary and are respected.

## Adversarial checks

| Attack | Resolution |
|---|---|
| Allow mixed-weight support edges under the weaker N15 wording | None of the proof's steps uses their absence. Independence only needs same-weight adjacency. |
| Allow extra positive defect values beyond the four stated entries | They are impossible because $2+2+1+1=6$ exhausts the actual nonnegative row sum. |
| Count common neighbors of a zero pair from within the root neighborhood | Any such neighbor would create a triangle at one of the zero endpoints, so none is available. |
| Let a zero heavy repeat occur as a true neighbor of the nonzero root | A true edge incident to a zero has defect zero; all $k_n$ endpoints really belong to the nonedge budget. |
| Give a heavy (ZZ) pair several nonzero common neighbors | It contributes several times to $\sum h_n$, with the surplus exactly recorded by $D$; the inequality direction remains correct. |
| Try $q_{n,y}=0,1,2$ in each indicator case | All residuals are nonnegative. In the zero-heavy case equality requires $q=2$; in the other positive-repeat case it forces $B=1,q=2$. |
| Hide cancellation in the equality case | The proof uses nonnegative pointwise residuals, nonnegative light counts, and $D=\sum_e(a_e-1)\ge0$; no cancellation is possible. |
| Use an all-zero graph or an all-nonzero graph | In the all-zero case heavy pairs would need a nonzero common neighbor, giving the intended contradiction. In the all-nonzero case the zero-pair counts vanish and the bounds remain valid. |
| Let heavy pairs between nonzero vertices be actual graph edges | They are outside (H_{ZZ},K_{ZN}) and outside the nonedge sums. The equality conclusion only excludes heavy **nonedges** within $N$, exactly as stated. |
| Mistakenly extend the smallest-case conditions to every seven-triangle graph | The slack vanishes only for the specified $T=7,m=20$ case; no such extension is made. |

No verified counterexample or unresolved candidate remains. These checks support, but do not replace, the explicit finite derivation.

## Obligations and closure

The 22 delta sequents in `DELTA_PROOF_OBLIGATIONS.json` cover the graph identities, weaker N15 premise, local and global counting, both numerical bounds, exact slack, and all equality conclusions. The dependency graph is acyclic. The new symbols are finite integer counts; $q_{n,y}$ in this report makes the root dependence of the paper's local $q_y$ explicit. No symbol changes meaning within an application.

There are no limits, analytic interchanges, probability modes, asymptotic estimates, computations, or hidden constants. No source edit was needed. The remaining open claims are N15 for arbitrary legal order-59 graphs, applicability to any larger inherited hypothesis such as H5, exclusion of all remaining N15 graphs, arbitrary order-59 exclusion, and the exact degree-diameter value. No Lean, compilation, wiki change, or order-63–65 work is part of this delta.
