# Seven-triangle nonzero-repeat budget: proof-obligation ledger

Review date: 2026-10-11. Fresh reviewer task: `/root/proof_review_seven_repeat_budget`.
Review independence: **same-family**. Semantic acceptance: **provisional**.
The skill names `gpt-6-astra` / `ultra` as requested reviewer settings; the worker has no backend attestation and does not represent those settings as observed backend metadata.

## Scope and sources

The complete mathematical content of these files was read, including their boundary and consequence sections:

- `proofs/dd82/n59/seven_triangle_nonzero_repeat_budget_20261011.md` (main, lines 1–194).
- `proofs/dd82/n59/zero_heavy_global_capacity_20261011.md` (capacity, lines 1–140).
- `proofs/dd82/n59/heavy_cross_repeat_slack_20261011.md` (cross, lines 1–103).
- `proofs/dd82/n59/nonzero_support_transport_20261011.md` (transport, lines 1–58).
- `proofs/dd82/n59/matching_zero_global_trace_obstruction_20261011.md` (trace, lines 1–117).

Existing review verdicts mentioned in the sources were not treated as evidence. The fourth-cycle walk count was derived directly below; no additional external theorem is needed. The review changes no proof source, formal file, wiki, shared state, or known order-63–65 work. Only the present review directory receives Markdown/JSON ledgers.

## Quantified theorem and hypotheses

For every finite simple undirected graph G on 59 vertices with maximum degree at most 8 and diameter at most 2, assume that at every vertex in no triangle the positive actual-defect row consists of weights 2,2,1,1, and its induced original support graph consists exactly of the two equal-weight edges. If G has seven triangles and exactly 21 vertices belonging to triangles, then:

1. Its weighted positive nonedge defect total W on those 21 vertices satisfies 1 ≤ W ≤ 6 and 2W + K ≤ 12, where K counts heavy cross repeats.
2. W = 5 forces a unit defect triangle and two other distinct unit defect edges.
3. W = 6 forces two unit defect triangles sharing at most one vertex, and all cross repeats are light with exactly two zero common neighbors and no nonzero common neighbor.
4. In the disjoint-triangle case all six repeat roots have two isolated light zero supports, exactly one adjacent to each repeat endpoint.
5. In the one-shared-vertex case the four outer vertices have exactly two original matching edges between the two outer pairs; every outer root has two isolated light zero supports, one adjacent to the shared root and one to its outer repeat partner.

All conclusions concern the same original graph. They are necessary conditions, not existence or a complete exclusion theorem. The N15 premise is assumed, not established for arbitrary legal graphs.

## Symbol and assumption ledger

| Symbol | Type and meaning |
|---|---|
| A | 59 by 59 symmetric {0,1} adjacency matrix with zero diagonal |
| B | Actual integer defect A² + A − 7I − J; symmetric, nonnegative, zero diagonal, row sum 6 |
| Z, N | Vertices in no triangle and their complement; disjoint, cardinalities 38 and 21 in the main theorem |
| t(v), T | Nonnegative integers: triangles through v and total triangles |
| W | Nonnegative integer, sum of B_uv over unordered nonedges within N |
| K | Number of cross pairs n∈N,z∈Z with B_nz=2; each pair counted once |
| q_uv | Number of zero common neighbors of u,v; integer in {0,1,2} |
| l_i | Number of light zero-zero defect edges with i nonzero common neighbors, i=0,1,2 |
| h_i | Number of heavy zero-zero defect edges with i nonzero common neighbors, i=1,2,3 |
| P | Number of unordered nonedges in N having two zero common neighbors |
| R_NN | Twice the sum of B_uv−binom(q_uv,2) over unordered nonedges in N |
| R_NZ | Sum of B_nz−binom(q_nz,2)−1_{B_nz=2} over cross nonedges, counted once |
| F | Sum of B_uv(B_uv−1) over unordered nonedges in N |
| s, s_N(r) | Sum of squares of all entries of B, and sum of squares of row-r entries in N |
| Q_N(r) | Sum B_ra B_rb over unordered original edges {a,b} within N |
| K_r | Weighted sum of original zero-zero support edges at root r; distinct from global cross count K |
| e_r | Exact integer Q_2(r)−sum_x B_rx²+5 = 5+Q_N(r)−s_N(r)−K_r |
| j_vw | Number of isolated zero repeats of v adjacent to nonedge repeat endpoint w |
| q in §4 | Number of active repeat roots; different from pairwise common-neighbor count q_uv |
| c_0,c_a | Number of original edges between outer pairs in the shared case, and original matching degree of a |

Regularity follows from the two-step ball bound 1+7+7·7=57<59. The actual defect formula and diameter hypothesis imply all entry, row-sum, and commutation properties. Seven triangles on 21 triangle-bearing vertices imply t(n)=1 for every n∈N, hence disjoint original triangles, two unit triangle-partner entries, and nonedge budget 4. The full induced-support N15 premise is used for transport and traces; the common-zero-neighbor and capacity lemmas need only the equal-weight endpoint adjacencies. Each application in the main proof is within the stronger premise.

## Dependency DAG

Legal graph → regularity and actual-defect identities.

N15 + defect identities → at most two zero common neighbors → local capacity → exact global slack.

Exact induced N15 + AB=BA → support transport → exact remainder formula.

Common-zero bound + transport → injective heavy-cross charging → K ≤ R_NZ.

Defect identities + finite closed-walk counts → fourth and fifth trace identities.

Charging + transport + traces → W=0 exclusion.

Global slack + pair bijection + charging → exact 8=2W+l_1−2h_3+R_NZ → W≤6.

W=5 equality + fourth trace + transport + AB=BA + fifth trace → unit-edge classification.

W=6 equality + transport + AB=BA + fifth trace → both incidence restrictions.

No cycle or dependency on either W=5 or W=6 conclusions occurs in a predecessor.

## Micro-claim ledger

Every entry below was discharged by reading and rederiving the indicated source argument. IDs P refer to predecessor obligations; IDs M refer to the main paper.

| ID | Context ⊢ obligation; rule and checked side conditions |
|---|---|
| P01 | Legal graph ⊢ 8-regular; two-step ball bound for any hypothetical degree≤7 root |
| P02 | P01 ⊢ B symmetric, nonnegative, zero diagonal, row sum 6, AB=BA, nonedge budget 6−2t; actual matrix identity and diameter |
| P03 | N15 ⊢ any pair has ≤2 zero common neighbors; common zero set independent, each weight class a matching, no two-colored positive defect triangle |
| P04 | P03 ⊢ l_n+2h_n+k_n+R_n=6−2t(n), R_n≥0; double count zero-neighbor pairs and additional common neighbors outside the root neighborhood |
| P05 | P04 ⊢ 59≤4m−3T, m≥20, T≥7; zero heavy incidence identity and m≤3T |
| P06 | P04 ⊢ exact global slack 2(4m−3T−59)=sum l_n+2D+sum R_n; subtract 2 card(Z)=2H_ZZ+K |
| P07 | Exact induced N15 and AB=BA ⊢ sum_{y∼x}B_ry=B_rx for each positive zero support x; same-weight support mate computes the transposed matrix entry |
| P08 | P07 ⊢ isolated equal-weight zero matching edges, isolated-zero transport, and e_r=5+Q_N−s_N−K_r; nonnegative summands and exact partition of weighted support edges |
| P09 | Heavy cross pair ⊢ one unit slack term; if q=2, both induced cross pairs cannot be heavy because a unit triangle edge cannot transport weight 2 to an isolated zero |
| P10 | P09 ⊢ injective charging and K≤R_NZ; a charged light pair's unique N and Z common neighbors recover its source heavy pair |
| P11 | W=0 ⊢ zero row shapes 22 or 1111 at nonzero roots; exclude 211 and pair 22 by transport, retaining isolated light supports in 1111 |
| P12 | W=0 ⊢ heavy charges disjoint from isolated-light terms; a charged light pair has no neighbor in its root's nonzero support, hence is paired |
| P13 | P11,P12 and traces ⊢ W≠0; a+b≤4, a even, b≡2a mod5 force a=b=0, then 84>76 light cross incidences |
| P14 | Actual defect traces ⊢ 8C4=6n+s−12T; tr A4=126n+s−12T and direct walk count tr A4=120n+8C4 |
| P15 | 8-regular simple graph ⊢ tr A5=10C5+210T; five-distinct-position walks and uniquely assigned triangle/backtrack walks, 30+18·10 per triangle |
| P16 | P15 and exact induced zero rows ⊢ fifth trace and congruence; tr A5=428n+w−2s+102T, zero rows s_v=10,Q2=5; also the all-zero contradiction |
| M01 | T=7,m=21 ⊢ disjoint original triangles and nonedge budget 4; equality in sum t(n)=21≥m |
| M02 | P06,M01 ⊢ 8=l1+2l2+2h2+4h3+R_NN+R_NZ; identify multiplicities and oriented N-N contributions |
| M03 | P03 ⊢ P=l2+h2+3h3 and W=P+R_NN/2; bijection between N-pair/zero-common-pair rectangles, and nonadjacency at zero vertices |
| M04 | M02,M03 ⊢ 8=2W+l1−2h3+R_NZ; exact substitution, no inequality or pairing assumption |
| M05 | M02–M04,P10,P13 ⊢ 1≤W≤6 and 2W+K≤12; h3≤2, nonnegative l1,R_NZ, and K≤R_NZ |
| M06 | W=6 ⊢ h3=2,l1=R_NZ=K=l2=h2=R_NN=0,P=6; equality in preceding nonnegative bounds |
| M07 | M06 ⊢ two unit repeat triangles sharing ≤1 vertex, no other N-N repeats, and no nonzero common neighbor on them; two distinct zero pairs cannot give a shared N-pair without ≥3 zero common neighbors |
| M08 | R_NZ=K=0 ⊢ every positive cross repeat is light and q=2, with no nonzero common neighbor; pointwise nonnegative slack |
| M09 | W=5 ⊢ h3=1,l1=R_NZ=K=0; h3≥1 from M04 and h3≤1 from W≥3h3 |
| M10 | Row sums and zero-row squares ⊢ s=506+2F+2K; count N-N excess twice, cross-heavy excess once per N row |
| M11 | W=5,M10,P14 ⊢ only two doubled triangle edges or two new distinct unit edges; enumerate the two leftover weight units and require F≡0 mod4 |
| M12 | Doubled-edge pattern ⊢ x_v∼w,x_w∼v and neither adjacent to u; singleton zero supports isolated, triangle partners excluded by M08, weight-2 endpoint unavailable to a unit zero |
| M13 | M12 ⊢ p_uv=q_uv=0 and p_uw=q_uw=0; full AB/BA expansions and p+q≤1 from unique N common neighbor and disjoint original triangles |
| M14 | M13 ⊢ e_u=−4,e_v=e_w=−1, all other 18 remainders 2; Q_N=1, square sums 10,7,7, no zero pair at u,v,w; other roots' four zeros paired |
| M15 | M14,P16 ⊢ doubled pattern impossible; sum e=30 and 30+7≠4 mod5 |
| M16 | W=6 ⊢ degree-0 remainder 2; degree-2 remainder 1 paired or 2 isolated; triangle-partner cross edges forbidden by absence of N common neighbors |
| M17 | Disjoint repeat triangles ⊢ j_vw=j_wv and row sums 0 or 2; full AB/BA expansion, paired supports supply no j terms |
| M18 | M17,P16 ⊢ all six active and all directional j=1; each triangle excludes active count 1, fifth trace forces total q∈{1,6}, so q=6, then solve three degree-2 equations |
| M19 | Shared repeat triangles ⊢ original edges between outer pairs form a matching; two incident edges would create a forbidden N common neighbor for a repeat pair |
| M20 | M19 ⊢ e_u=c0 and sum e=36+c0+q; Q_N(u)=1+c0,s_N(u)=6,K_u=0 and other 20 row contributions |
| M21 | Shared case ⊢ j_au=c_a, j_ab=j_ba, and counterparts; complete AB/BA expansions at central and outer repeat edges |
| M22 | M21,P16 ⊢ c0=2,q=4 and each outer root splits its two isolated zero repeats one per endpoint; parity excludes c0=1, trace excludes c0=0 |

No limits, integrals, probability modes, asymptotics, or hidden constants occur. All sums and case splits are finite.
