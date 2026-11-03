# Fresh proof audit: single-triangle normal-form exclusion

Verdict: **PASS for the theorem as stated**. Review independence: **same-family**. Acceptance status: **provisional**. No FATAL, CRITICAL, MAJOR, or MINOR mathematical issue was found in the audited dependency chain. This is a paper-proof judgment, not Lean certification or a cross-family verdict.

The reviewer was a fresh Codex agent, `/root/proof_review_single_triangle`, with the requested `gpt-6-astra` / `ultra` configuration accepted by the spawning interface. The actual serving model/backend was not independently disclosed. No previous review outputs were used as evidence. Statements in the proof about prior reviews were not accepted as proof premises.

## Exact audited statement and inputs

For every finite simple undirected graph G with 59 vertices, maximum degree at most 8, and a path of length one or two between every distinct pair, suppose that every vertex in no triangle has an actual B row with positive values 2,2,1,1, whose induced support in the same original graph is exactly the two same-weight matching edges, where B=A²+A−7I−J. Then G does not have exactly one triangle.

The following sources were read and checked directly:

- `proofs/dd82/n59/single_triangle_normal_form_exclusion_20261011.md`, complete theorem and Steps 1–5.
- `proofs/dd82/n59/h5_nonzero_trace_constraints_20261011.md`, Steps 1–9 through the support and remainder-set conclusions at line 153.
- `proofs/dd82/n59/matching_zero_global_trace_obstruction_20261011.md`, complete trace identities, closed-walk counting, and zero-row contributions.

The optional short-cycle consequence at H5 line 155 is not used by the main theorem and is outside this audit. In particular, no C9 exclusion, inherited N4/N5, spectral approximation, independent 6-by-6 block realizability, or SAT result is an input.

The trace-obstruction dependency additionally proves T≠0 under the same original-graph and N15 assumptions, so the combined conclusion is T≥2. This audit does not establish N15 from arbitrary n59 hypotheses, exclude all H5, exclude any other n59 representative, or determine the degree/diameter extremal value.

## Original-graph foundations

The root-ball argument is valid at every vertex x: 59≤1+d(x)+7d(x)=1+8d(x), so d(x)≥8; the given upper bound makes the graph 8-regular. Hence B has zero diagonal, nonnegative integer off-diagonal entries, and row sum 64+8−7−59=6. Nonnegativity uses the path premise when a pair is nonadjacent. Regularity gives AJ=JA=8J and therefore AB=BA; AB is symmetric. For an edge incident to a zero-triangle vertex, there is no common neighbor, so B=0 on that edge.

These facts connect every later matrix entry to the actual original graph. N15 is only applied at a zero-triangle endpoint, including the private-neighborhood vertices and all vertices of R. It is never applied as a row-shape assumption at a triangle vertex.

## Dependency audit

The fifth-trace computation is correct. From B=A²+A−7I−J one obtains tr(AB)=6T, tr(A²B)=s−6T+6n, tr(A⁴)=126n+s−12T, tr(A³B)=48T+42n+w−s, and tr(A⁵)=428n+w−2s+102T. All traces are finite sums, and every use of a constant row sum follows from regularity.

For five-step closed walks, a nonsimple cyclic word has a two-step backtrack, whose deletion leaves a triangle. Its used-edge support identifies a unique triangle, including when unused graph edges form additional triangles. A fixed triangle contributes 30 internal walks and 10 for each of its 18 edges to an external vertex, giving 210 walks. Thus tr(A⁵)=10C₅+210T, with chorded cycles allowed. At a zero row, s_v=10 and 2Q₂(v)=10; the resulting identity 5C₅=209·59+Σe_v−54T and congruence Σe_v+T≡4 (mod 5) are correct. The all-zero specialization gives the integral contradiction 10C₅=24662.

H5 Steps 1–2 correctly use the complete induced N15 support: for a positive repeat at a zero vertex x, (BA)_{xy}=B_{xy}; commutation and symmetry transfer this to either endpoint. Consequently the trace difference localizes to pairs of nonzero vertices while AB is still computed in the full graph.

Under exactly one triangle, each triangle row has two actual triangle-edge entries equal to one and residual nonedge mass four. Every positive nonedge endpoint is zero, hence its entry is at most two. The partitions 22, 211, 1111 exhaust the possibilities. The two evaluations of b_vᵀAb_v give q_v+2+a_v=2+2a_v+2c_v, so q_v=a_v+2c_v and e_v=4−c_v. A zero repeat cannot be adjacent to both other triangle vertices, giving 0≤a_v≤4 and the stated necessary c ranges.

Parity of the actual B=2 nonedge graph gives an even number of 211 triangle rows. The fourth-trace identity and the usual four-walk count yield n₂₁₁+2n₁₁₁₁≡2 (mod 4). Together with Σc_v≡4 (mod 5), these leave exactly the four displayed candidates. For the same original graph, a_u=m_uv+m_uw and its two cyclic versions; the triangle inequalities eliminate the other three candidates. Relabeling the unique c=2 triangle vertex as w is lossless; u and v are interchangeable. The surviving values are all1111, c=(1,1,2), a=(2,2,0), and m=(2,0,0). The entries B_ux=d_{P_u}(x) bound each cross degree by one, so the two cross edges form a matching.

H5 Step 9 supplies precisely the support information needed by the new proof. For a zero repeat x of triangle vertex r, the six positive entries of row r are all one, and (BA)_{rx}=1 counts its degree within that actual support. The four repeats of w have no adjacency to u or v and induce a matching of size two. For u, the two repeats in P_v already have their sole support neighbor v; the remaining two repeats have no triangle-vertex neighbor and must be adjacent to each other. They lie in R, and similarly for v. Thus |R|=38, |R_u|=|R_v|=2, and **|R_w|=4**. These conclusions do not assume that the three repeat sets are disjoint.

## New contradiction: detailed checks

For x∈R, the common neighbors of x and u are exactly N(x)∩P_u, since x is adjacent to no triangle vertex. Hence d_{P_u}(x)=1+1_{R_u}(x), and likewise for v,w. For p∈P_u, the common neighbors with v are u plus its cross neighbors in P_v, giving B_pv=1 exactly at the two active endpoints.

For distinct p,q∈P_u, the only common neighbor outside R is u. Neither v nor w is adjacent to p or q; P_u is independent; no P_v vertex meets two points of P_u because the cross edges are a matching; and there are no P_u–P_w edges. Thus B_pq counts their common neighbors in R exactly. Only the two points of R_u can contribute a parent pair. Since those points are adjacent, their parent pairs are disjoint, or a second triangle would result. The internal B block therefore consists of two disjoint light pairs. An active endpoint of such a pair would have light endpoints q and v, forcing the impossible edge qv by N15. Therefore these four endpoints are exactly the inactive points.

There can be no light entry from P_u to P_w. At an active p, the already present light endpoint v has no neighbor in P_w; at an inactive p, its internal light mate has no neighbor in P_w. N15 pairs the two light endpoints in either case. For a light P_u–P_v entry, neither endpoint can be inactive: its inactive internal mate has no cross neighbor. Only four active-active pairs remain, and two are actual edges with B=0. Thus the cross block has at most two light entries.

For a P_u–P_v pair or a P_u–P_w pair, every common neighbor is in R. In particular, there is no uncounted triangle vertex, private-neighborhood vertex, or cross-matching contribution to A² in these blocks. Double counting the incidences through R gives

\[
\sum_{P_u\times P_v} B=38+2+2+|R_u\cap R_v|+2-36=8+h_{uv},
\]

\[
\sum_{P_u\times P_w} B=38+2+4+|R_u\cap R_w|-36=8+h_{uw}.
\]

All entries are 0,1,2, since each endpoint is zero. If ℓ_uv≤2 counts the light pairs, then 2k_uv=8+h_uv−ℓ_uv≥6, so k_uv≥3. The second block has no light pairs and gives 2k_uw=8+h_uw≥8, so k_uw≥4. No special value of either overlap was used. An odd h_uw would itself already contradict this equality; the proof does not need to classify this stronger restriction.

Finally P_v∪P_w is an independent set of actual graph vertices. Each p∈P_u has exactly two distinct heavy endpoints, which N15 requires to be adjacent. At most one can lie in that union. Summing over the six distinct p counts each cross heavy pair exactly once, hence k_uv+k_uw≤6, contradicting k_uv+k_uw≥7. There is no division-by-two or orientation error.

## Adversarial attempts and exact checks

The review attempted the following potential failures: omitted 211 or 22 row cases; a missed support edge in H5 Step 9; common neighbors outside R; coinciding parent pairs; active endpoints among internal light pairs; light entries through an inactive endpoint; overlaps among all three remainder repeat sets; and double counting in the final capacity bound. Each is ruled out above using the stated original-graph hypotheses. None yields a counterexample, and no extra hypothesis was introduced.

A supplementary single-CPU Python exact check took approximately 0.1 seconds. It enumerated the seven necessary row-type/c-value options in triples and recovered exactly the four displayed candidates, with only the stated normal form satisfying the triangle inequalities. Separately, all 1,024 simple labeled graphs on five vertices satisfied the general formulas

\[
\operatorname{tr}(A^4)=\sum_vd_v+4\sum_v\binom{d_v}{2}+8C_4,
\quad
\operatorname{tr}(A^5)=10C_5+\sum_{\{u,v,w\}\text{ triangle}}(10(d_u+d_v+d_w)-30).
\]

These finite checks supplement the analytic counting proofs; they are not claimed to prove the n59 theorem or graph-realizability conditions. No SAT search or long-running computation was used.

There are no asymptotic limits, probability-mode transitions, analytic interchanges, or hidden parameter-dependent constants in this proof. The dependency order is acyclic. The proof ends at exactly the conditional statement it begins with.

## Artifacts and disposition

No proof source was changed and no fix round was needed. User overrides were respected: no hashes, checksum files, TeX/PDF/HTML rendering, or wiki changes. The only generated files are this audit, its structured verdict/state, and the obligation ledger in the requested review directory. Cross-family acceptance and Lean formalization, if desired, are separate from this fresh same-family paper audit.
