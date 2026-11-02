# DD82 N63 and n59 trace/cycle proof skeleton

Fresh reviewer: `/root/proof_review_n63_trace`. Requested route: `gpt-6-astra`, `ultra`; backend model and effort are not independently attested. Review independence: same-family; semantic acceptance: provisional. Sources were read directly and completely; prior reviews and `N63_SPECTRAL_ROUTE_REVIEW` were not read. No source or `formal/` edits were made by this reviewer.

## Statements and assumptions

| ID | Canonical statement | Hypotheses used and discharge |
|---|---|---|
| F | Every finite simple undirected graph with maximum degree ≤8 and a path of length ≤2 between each distinct pair has order ≤65; order >57 forces degree 8; orders 64 and 65 are impossible. | Original graph assumptions are explicit in `FOUNDATIONS.md:9–11`; root-ball coverage and degree counting in lines 19–23; actual defect derived in lines 27–43. |
| N63 | No graph satisfying F's original graph assumptions has exactly 63 vertices. | Regularity follows from the root bound; all subsequent matrices are derived from that same graph, not independently selected. No symmetry/classification/SAT assumptions. |
| TR | Every such graph of order 59 whose zero-triangle vertices have the stated 2211 matching support satisfies `5 C5 = 209·59 + Σ[t(v)>0] e_v − 54 T`. Its triangle-free subcase is impossible. | Regularity, symmetry, and row sum 6 follow from F. The matching condition is assumed only where `t(v)=0`; nonzero rows retain their actual correction terms. |
| C5 | No such graph of order 59 contains a simple R2 cycle of length 5 entirely on zero-triangle vertices with matching 2211 rows. | Only the five selected rows are constrained. Cycle vertices are pairwise distinct, as inherent in the stated cycle/point-set interpretation. |
| C7 | Same exclusion for length 7. | Only seven selected rows are constrained; no classification of all remaining vertices is assumed. |
| C8 | Same exclusion for length 8. | Only eight selected rows are constrained; parity is local cycle indexing, not global bipartiteness. |
| C9 | Same exclusion for length 9. | Only nine selected rows are constrained; neither deletion of step-three chords nor classification of external neighborhoods is assumed. |

The H5+N15 applications remain conditional on those external definitions/results. They are not needed for these directly stated original-graph theorems and were not independently audited here. The audit does not establish H5 impossibility, n59 impossibility, an exact extremal value, or a formal upper bound 62.

## Typed symbols

`G`: finite simple undirected graph; `n`: its integer order; `A∈{0,1}^{n×n}`: symmetric adjacency matrix with zero diagonal; `I,J∈Z^{n×n}`: identity/all-ones matrices; `B=A²+A−7I−J∈Z^{n×n}`: actual symmetric defect matrix after regularity; `δ=65−n`: defect row sum.

For N63, `μ∈R` is a B eigenvalue, `ℓ∈{1,…,63}` its root-of-unity conductor, `K=Q(μ)⊂R`, `C_ℓ∈Z[x]` its monic minimal polynomial, `N_ℓ∈Z_{>0}` the discriminant norm, and `U_μ` is a real eigenspace inside the coordinate-sum-zero subspace. The associated K-kernel is a different scalar-field realization of the same equations, with the same dimension after extension to R. `p,q∈Z_{≥0}` are multiplicities of A-eigenvalues 2 and −3 on `U_{−1}`.

For n59, `t(v),T,C5∈Z_{≥0}` count triangles at v, all triangles, and unoriented simple five-cycles (chords allowed). `s_v=Σ_u B_vu²`, `Q2(v)=½ b_v^T A b_v∈Z`, where `b_v=B unit_v` and `unit_v` is the v-th standard basis vector; `e_v=Q2(v)−s_v+5∈Z` is a scalar correction. The original source used `e_v` for both the basis vector and the correction: cosmetic notation collision PC-01, now corrected by the author using a bold basis vector and an explicit definition. `R2` consists of actual nonedges with B-entry 2. `Z` is the selected cycle's vertex set; external neighborhood sets and `X_i` are actual G-neighborhood classes.

## Dependency DAG

`original graph → root bound → 8-regularity → actual defect identities`.

`defect identities → row-two component classification → cycle/doubled-edge spectrum → conductor coverage`;
`cyclotomic identities + exact table → discriminant nonsquares`;
`K-linear quadratic lemma + scalar-extension kernel argument + conductor coverage → trace on each nonexceptional B-eigenspace`;
`exception μ=−1 + constant direction + zero diagonal → N63 contradiction`.

`n59 defect identities → fourth/fifth trace identities`; `simple closed-walk classification → combinatorial fifth trace`; both, plus `matching zero-row moments → TR identity/congruence`.

Each of `C5,C7,C8,C9` depends only on the actual n59 identities, the selected zero/matching rows, and its own local argument. None uses another cycle exclusion. There is no logical cycle in these dependency chains.

## Micro-claims and applications

| ID | Context ⊢ conclusion; rule and side conditions |
|---|---|
| F1 | Root-ball coverage and degree≤8 ⊢ `n≤1+8 deg(v)`; count a union, with each neighbor contributing ≤7 second neighbors. Empty graph handled separately. |
| F2 | n>57 ⊢ all degrees 8; integrality and upper degree bound. Then diagonal, nonnegativity, symmetry, row sums, commutation of B follow from actual adjacency/path counts. |
| F3 | Rational `T²+T−kI=0`, irreducible quadratic ⊢ even dimension and trace `−dim/2`; expand a basis over the quadratic field. |
| F4 | n=65 ⊢ B=0 and trace A=−24; n=64 ⊢ B pairs, a 31-dimensional rational invariant kernel, contradicting F3 for k=8. |
| N1 | Symmetric nonnegative integral B, zero diagonal, row sum 2 ⊢ components are doubled edges or ordinary cycles. An entry 2 exhausts both incident rows; otherwise every component is simple 2-regular. |
| N2 | These components ⊢ every eigenvalue has conductor ≤63; a cycle eigenvalue's primitive conductor divides its length, and doubled edges give μ=±2. |
| N3 | Primitive nonreal ζ of order ℓ≥3 ⊢ `[Q(ζ):Q(ζ+ζ⁻¹)]=2`; nonreality excludes degree 1 and the displayed quadratic bounds degree by 2. Standard cyclotomic irreducibility gives degree φ(ℓ). |
| N4 | Minimal polynomial plus multiplication norm ⊢ `Norm(29+4μ)=(-4)^d C_ℓ(-29/4)`; all real conjugates lie in [−2,2], so norm is positive. Primitive choices are conjugate and have the same norm. |
| N5 | Exact divisor products, polynomial lifts, and 63 exact determinant/residue checks ⊢ norm is nonsquare for every ℓ≠3; ℓ=3 has μ=−1 and discriminant 25. Only the necessary implication square element⇒square norm is used. |
| N6 | Nonsquare discriminant over K ⊢ qμ irreducible; a K-linear operator killed by qμ makes its space a quadratic-field module and has trace `−dim_K/2`, including dimension zero. |
| N7 | Equations `Bv=μv`, `Σv_i=0` over K ⊢ scalar extension gives the full real eigenspace with unchanged dimension/trace; Gaussian elimination over K proves rank invariance. A has rational entries and preserves both equations. |
| N8 | Spectral decomposition on W, separate constant line, and roots 2/−3 at μ=−1 ⊢ `0=−23+5(p−q)/2`, impossible. No real-root pairing shortcut is used. |
| T1 | Regular actual n59 matrices ⊢ `tr AB=6T`, `tr A²B=s−6T+6n`, `tr A⁴=126n+s−12T`; expand definitions and use J row sums. |
| T2 | Same identities ⊢ `tr A³B=48T+42n+w−s` and `tr A⁵=428n+w−2s+102T`; all traces are finite sums. |
| T3 | Simple loopless graph ⊢ each nonsimple five-step closed walk has a unique triangle among its used edges, plus a doubled extra edge. Internal triangle walks contribute 30; each external incident edge contributes 10. At degree 8 the coefficient is 210 per triangle. |
| T4 | T2+T3 ⊢ `10C5=428n+w−2s−108T`; under a matching zero row, `s_v=10`, `w_v=10`, `Q2(v)=5`. |
| T5 | Matching condition only at zero vertices ⊢ retain each nonzero row as `e_v`; divide by 2 and reduce modulo 5 to get the claimed exact remainder. If every vertex is zero, `10C5=24662` is impossible. |
| C5a | Forced heavy-pair edges ⊢ G[Z] is the complementary step-two C5, with one internal common neighbor for consecutive R2 vertices. |
| C5b | Their two additional common neighbors x,y ⊢ two light entries at that internal common neighbor; the row budget leaves exactly those entries. Matching light-pair edge xy contradicts the selected zero vertex. |
| C7a | Heavy-pair edges and zero triangles ⊢ exactly step-two C7; mixed heavy/light nonadjacency excludes all step-three B entries. |
| C7b | Exact internal counts ⊢ every external two-neighbor set is a consecutive R2 pair, each X_i has size 3, and degree saturation excludes private neighbors. |
| C7c | Diameter two from x∈X_i to z_(i+4) ⊢ a neighbor in X_(i+3) or X_(i+4), creating an external B-entry of at least 1. Twenty-one distinct x require ≥21 units but Z has only 14 external units. |
| C8a | Antipodes already have two internal common neighbors ⊢ an antipodal light entry; mixed-support nonadjacency then eliminates every step-three edge, without assuming this conclusion. |
| C8b | Mixed-support restriction excludes step-three B entries; exact antipodal counts exclude two external neighbors in one parity class. |
| C8c | Four opposite-parity nonneighbors require `3+3+1+1=8` external common-neighbor incidences, while six external neighbors provide at most six. |
| C9a | Heavy-pair edges and zero triangles ⊢ only step-three chords remain free. Relabeling by a dihedral symmetry preserves all hypotheses. |
| C9b | Chord 0–3 ⊢ light pair 3–7; heavy pair 0–1 must have an external common neighbor x; x is the other light endpoint at 3, forcing x–7 and a triangle through 0. Thus no chord exists. |
| C9c | Six external neighbors per z_i are exhausted by its two disjoint groups of three heavy-pair common neighbors ⊢ every external neighborhood induces a 1-regular subgraph of R2. |
| C9d | Triangle avoidance forces ≥2 unselected positions between its selected edges. Nine positions permit only one edge or two edges in the orbit of {0,1,4,5}; three edges require ≥12 positions. |
| C9e | Two-edge neighborhood forces 4 and 5 to be the light pair at 0, but 4–5 is an actual nonedge. Thus only single-edge neighborhoods occur, leaving pair 0,3 uncovered by any two-step path. |

All inequalities are finite cardinality/budget inequalities with direction checked. No limits, analytic interchanges, probabilistic mode changes, asymptotic constants, or uniformity conditions occur. The computations check finite subclaims; they do not substitute for the graph-to-field argument or prove graph nonexistence by enumeration.
