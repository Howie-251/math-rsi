# Proof-obligation ledger: seven triangles and heavy cross slack

Review date: 2026-10-11. Reviewer: `/root/proof_review_seven_triangle_slack`.
Requested route: `gpt-6-astra`, reasoning `ultra`, fresh context. Backend model/effort attestation is unavailable. This is a same-family, provisional semantic review.

## Inputs and canonical statements

The primary inputs are the full files:

- `proofs/dd82/n59/seven_triangles_twenty_core_exclusion_20261011.md` (abbreviated **S**).
- `proofs/dd82/n59/heavy_cross_repeat_slack_20261011.md` (**H**).

The dependencies read in full are:

- `proofs/dd82/n59/zero_heavy_global_capacity_20261011.md` (**G**).
- `proofs/dd82/n59/nonzero_support_transport_20261011.md` (**P**).
- `proofs/dd82/n59/matching_zero_global_trace_obstruction_20261011.md` (**F**).

Let `LegalN15(G)` mean: G is a finite simple undirected graph on exactly 59 vertices, maximum degree at most 8, diameter at most 2, and for every vertex lying in no triangle the actual defect row has weights 2,2,1,1 and its positive support induces exactly the two equal-weight edges. No N15 assumption is imposed on other rows.

The three quantified claims are:

1. For every G satisfying `LegalN15(G)`, it is impossible to have T=7 and m=20. Consequently T=7 implies m=21 and the seven triangles are vertex-disjoint.
2. For every G satisfying `LegalN15(G)`, the number K of unordered weight-two defect pairs meeting both N and Z satisfies K≤R_NZ≤2(4m−3T−59).
3. For every G satisfying `LegalN15(G)`, T=7 and m=21 imply the existence of distinct nonadjacent u,v in N with B_uv>0.

These are conditional graph-theoretic claims. They neither establish N15 for arbitrary legal graphs nor exclude all T=7 graphs, H5, or all order-59 graphs.

## Typed symbols and hypothesis ledger

| Symbol | Type and meaning |
|---|---|
| A | Actual symmetric 59×59 adjacency matrix with entries in {0,1} and zero diagonal. |
| B | Actual integer matrix A²+A−7I−J; symmetric, nonnegative, diagonal zero, row sum 6. |
| t(v), T | Nonnegative integers: triangles at v and total triangles; Σ_v t(v)=3T. |
| N, Z, m | N={v:t(v)>0}, Z=V\N, m=|N|. |
| q(n,z) | Number of common neighbors of n,z lying in Z, for a cross nonedge; 0≤q≤2. |
| r(n,z) | B_nz−binom(q(n,z),2)−1_{B_nz=2}, an integer in {0,1}. |
| R_n, R_NZ | Nonnegative integer sums of pointwise slack; R_NZ uses each cross pair once, at its N endpoint. |
| K | Number of unordered heavy cross defect pairs; not the row quantity K_r of P. |
| Q_2(v), s_v, e_v | Weighted support-edge sum, row square sum, and Q_2(v)−s_v+5. |
| K_r | In P only: weighted sum over original edges in the zero part of row r's support. |
| a | Under the additional repeat-free-core assumption, number of N roots with zero-repeat pattern 22. |
| p_n, b | p_n counts matching edges in a 1111 zero support; b=Σ(2−p_n). |
| C_4,C_5 | Unoriented simple cycles, counted up to cyclic shift and reversal; chords allowed. |

Simple undirected graph, order 59, maximum degree 8 and diameter 2 are used to obtain regularity, the actual defect identity, nonnegativity and common-neighbor interpretations. Exact N15 on Z is used for endpoint weights, equal-weight adjacency, support transport, and the zero-row fifth-trace contribution. T=7,m=20 is used only in the equality-case exclusion. T=7,m=21 and zero defect on N–N nonedges are used only in H's bounded consequence. All applications retain the actual common graph; no independently assigned matrices are substituted.

## Dependency graph

`LegalN15 → regularity/actual B → row budgets`

`N15 endpoint adjacencies → independent-zero matching classes → q≤2`

`row budgets + q≤2 + zero heavy incidences → global slack identity → equality consequences / cross-slack bound`

`exact zero-row N15 + AB=BA → transport at every root → isolated equal-weight support edges / isolated-vertex equation`

`equality consequences → no N–N nonedge repeat → T=7,m=20 triangle structure → no cross heavy repeat → fourth-trace contradiction`

`q≤2 + row budgets + transport → a light target for every q=2 heavy source → injective charging → K≤R_NZ`

`T=7,m=21 + repeat-free core + transport → row patterns + isolated-light terms → disjointness from heavy charges → a+b≤4`

`actual B → fourth/fifth trace identities; exact N15 → zero-row remainders vanish`

`row patterns + traces + a+b≤4 → a=b=0 → light-incidence contradiction`

No cycle or hidden dependence on either new conclusion occurs in this graph. The general charging bound does not use the equality-case exclusion or either trace congruence.

## Micro-claim inventory

Each entry is a finite sequent: the left side states its additional context, the right side its obligation. The detailed discharges are recorded in `PROOF_AUDIT.md`.

| ID | Context ⇒ obligation; rule and source |
|---|---|
| F01 | Legal graph ⇒ every degree is 8; two-step root bound 1+7+7·7=57<59. G19. |
| F02 | F01 + actual adjacency ⇒ B is symmetric, nonnegative, diagonal zero, row sum 6 and commutes with A. G19–23; P20. |
| F03 | F02 ⇒ neighbor defect budget 2t(v), nonedge budget 6−2t(v). G23–28. |
| G01 | Independent U⊆Z + N15 ⇒ each defect-weight class on U is a matching; no positive-defect triangle. G42. |
| G02 | G01 ⇒ any two distinct vertices have at most two common zero neighbors. G44–48. |
| G03 | U_n=N_G(n)∩Z ⇒ ℓ_n+2h_n=Σ_y binom(q_y,2); count the common neighbors other than n. G50–64. |
| G04 | F03 + G02 ⇒ each pointwise R_n summand is nonnegative. G66–76,110–114. |
| G05 | G03–G04 + zero heavy incidences ⇒ 2(4m−3T−59)=Σℓ_n+2D+ΣR_n with D≥0. G78–94,106–121. |
| G06 | G05 + m≤3T ⇒ m≥20 and T≥7. G96–104. |
| G07 | T=7,m=20 + G05 ⇒ all equality facts used in S29–37, including exact heavy-ZZ multiplicity and pointwise equality. G123–130. |
| X01 | G07 ⇒ no positive N–N nonedge defect; two common zero neighbors would have an impossible light/heavy defect pair. S48–52. |
| X02 | T=7,m=20 ⇒ one vertex has t=2, nineteen have t=1; no shared triangle edge. S54–56. |
| P01 | Exact N15 at x∈Z, B_vx>0 ⇒ Σ_{w∼x}B_vw=B_vx for arbitrary v, including v∈N. S58–62; P20–22. |
| P02 | P01 + nonnegative weights ⇒ zero support edges have equal weights and are isolated in the full support; isolated zero support vertices see an independent nonzero support set of the required weight. P24–30. |
| X03 | A nonzero root with two heavy zero nonedge repeats ⇒ t=1 and these exhaust its nonedge support; its two unit triangle partners cannot supply weight two to a zero vertex, so the heavy repeats are adjacent. S64–68; H45. |
| X04 | G07 + hypothetical heavy cross repeat + X03 ⇒ contradiction at two common zero neighbors; excludes all heavy cross repeats in the equality case. S70–76. |
| X05 | X01–X04 ⇒ s=20·6+39·10=510. S78–80. |
| T01 | F01–F03 ⇒ 8C_4=6·59+tr(B²)−12T; actual fourth-walk count. S82–94; F53–63. |
| X06 | X05 + T01 ⇒ 8C_4=780, impossible modulo 8; G06 then gives T=7 ⇒ m=21. S96–102. |
| C01 | Cross nonedge + N15 + G02 ⇒ r∈{0,1}, with all q=0,1,2 cases covered. H19–31. |
| C02 | Heavy source with q≤1 ⇒ its own cross term has r=1. H41. |
| C03 | Heavy source with q=2 ⇒ at least one of the two derived cross repeats is light, by X03; that pair has exactly one common neighbor in each of N,Z. H43–47. |
| C04 | C03 ⇒ light target has r=1; its common neighbors recover the source uniquely. H47–49. |
| C05 | C02–C04 ⇒ charging is injective, and self-heavy targets are disjoint from light targets; hence K≤R_NZ. H49–53. |
| C06 | G05 + pointwise nonnegativity ⇒ R_NZ≤ΣR_n≤2(4m−3T−59). H29–31. |
| B01 | T=7,m=21 + repeat-free N-core ⇒ each N row has one unit triangle edge in support and zero-repeat pattern 22,211 or 1111. H57–63. |
| B02 | B01 + P02 ⇒ 211 is impossible; 22 is paired and isolated; 1111 has p_n∈{0,1,2}. H63–67. |
| B03 | B01–B02 ⇒ 2b isolated-light cross terms, each with a nonzero common neighbor and r=1. H69. |
| B04 | Repeat-free N-core + B02 + C03 ⇒ every light target charged by a heavy source is paired at its target root; hence it is disjoint from the isolated-light terms. H71–73. |
| B05 | C05–C06 + B03–B04 ⇒ 2a+2b≤R_NZ≤8, hence a+b≤4. H75–77. |
| T02 | Actual B and trace cyclicity ⇒ tr(A^5)=428·59+w−2s+102T. F65–79. |
| T03 | Simple 8-regular graph ⇒ tr(A^5)=10C_5+210T, with each non-simple five-walk belonging to exactly one traversed triangle. F81–89. |
| T04 | T02–T03 + exact zero N15 ⇒ 5C_5=209·59+Σ_{n∈N}e_n−54T and Σe_n+T≡4 (mod 5). F91–109. |
| B06 | B01–B02 + support transport ⇒ e_n=0 for 22, e_n=4−p_n for 1111; Σe_n=42−2a+b. H89–91; P32–38. |
| B07 | T01 + row squares ⇒ a is even; T04 + B06 ⇒ b≡2a (mod 5). H79–95. |
| B08 | Nonnegative integers a,b + B05 + B07 ⇒ a=b=0 by the three cases a=0,2,4. H97. |
| B09 | a=0 ⇒ 84 cross light incidences, but 38 zero rows supply at most 76; contradiction. H99. |

There are 37 obligations. There are no analytic limits, probability-mode changes, interchanges of infinite operations, or asymptotic uniformity claims. All sums are finite. No additional computation or formalization is needed for these obligations.
