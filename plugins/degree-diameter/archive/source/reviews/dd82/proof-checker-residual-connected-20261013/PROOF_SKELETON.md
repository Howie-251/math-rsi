# Residual-cover connectivity: proof obligations

Review date: 2026-10-13. Reviewer: `/root/residual_connected_review`, fresh Codex context; `review_independence: same-family`, `acceptance_status: provisional`. One bounded round. No Lean checking. The representation remains an explicit imported dependency, whose §§1–2 were checked here.

## Actual input and scope

- Read project `AGENTS.md` and `.agents/skills/proof-checker/SKILL.md` in full; apply the V3/user overrides supplied with this task.
- Read `proofs/dd82/construction/FALSE_TWINS58_RESIDUAL_CONNECTED.md`, all lines 1–209.
- Read `proofs/dd82/construction/FALSE_TWINS58_EIGHT_SIX_FIBERS.md`, all lines 1–268; only §§1–2 (lines 16–113) are mathematical dependencies and audited here. Its later symmetry specialization and computational claims are outside this review.
- No other review reports or reviewer opinions were read. No new backend, solver, search, or source edit was used.

## Quantified statement and types

For every finite simple graph G with |V(G)|=58, maximum degree ≤8, diameter ≤2, and a pair of distinct nonadjacent vertices with equal open neighborhoods, take the representation in §§1–2. Then E is connected; every eigenvalue λ of H restricted to W lies strictly between β=(-1−√57)/2 and α=(-1+√57)/2 and outside (−1,0). If E is bipartite, both parts contain three vertices of each fibre and every H vertex has three same-part and four opposite-part neighbors. In all cases H is invertible over ℝ.

| Symbol | Type / meaning |
| --- | --- |
| F_j | Eight disjoint vertex sets of size six |
| H, E | Symmetric 48×48 matrices with entries 0 or 1; zero diagonal; both 7-regular |
| D | diag(J_6,…,J_6); not an orthogonal projection |
| J | J_48 |
| W | {x∈ℝ^48: ∑_{v∈F_j}x_v=0 for every j}; dimension 40 |
| C_i, c | E-components and their number |
| t_i | |C_i∩F_j|∈ℤ_{≥1}, independent of j; ∑_i t_i=6 |
| Q | c×c integer nonnegative equitable quotient of H by C_i |
| t | Column vector (t_1,…,t_c)^T |
| z | Bipartition sign vector, entries ±1, when E is bipartite |

## Dependency DAG and assumption discharge

Graph hypotheses → R1 regularity/defect budget → R2 eight-fibre representation and coverage → M1 residual adjacency/commutation/H connectivity → M2 component balance and quotient → M3 integer spectral restriction → M4–M7 disconnected-case contradictions → M8 E connectivity and spectral bounds → M9 bipartite distribution → M10 H invertibility. No backward dependency or cycle occurs.

All regularity, symmetry, integrality and nonnegativity assumptions below are supplied by R1–R2/M1 before use. Equitable partitioning is derived in M2, not assumed. Component relabeling conjugates Q by a permutation and reorders t, preserving every equation; hence sorted profiles and the reordered a-vector lose no cases.

## Micro-obligation ledger

| ID | Context ⇒ obligation; justification and location | Result |
| --- | --- | --- |
| R1 | n=58, Δ≤8, diam≤2 ⇒ d(v)=8: 58≤1+d(v)+7d(v), so d(v)≥8. Then B=A_G²+A_G−7I−J has zero diagonal, nonnegative integer off-diagonal entries, row sum seven. Representation lines 18–26. | Checked import |
| R2 | False twins use defect budget seven against each other ⇒ S independent, each residual vertex has one S-neighbor; budgets at S imply independent six-vertex fibres and pairwise H perfect matchings. Different-fibre coverage has no route outside H, so each block of H²+H−J is a permutation. Representation lines 28–113. | Checked import |
| M1 | R2 ⇒ H² has diagonal blocks 7I_6; E has zero diagonal blocks and permutation off-diagonal blocks, hence is symmetric simple 7-regular. HD=DH=J−D and HJ=JH imply HE=EH. Cross-fibre coverage joins all H vertices, including same-fibre vertices via a third vertex. Target lines 38–70. | Discharged |
| M2 | E matching F_j↔F_k preserves each E-component in both directions ⇒ t_i independent of fibre, positive, sum six. Symmetric 7-regular E has ker(E−7I) equal to component-constant vectors. Commutation preserves this space, giving integer q_ij and equitable partition. Edge counts yield t_i q_ij=t_j q_ji. Target lines 72–85. | Discharged |
| M3 | On component coordinates, D=1 t^T, J=8·1 t^T, E=7I ⇒ Q²+Q=14I+7·1 t^T. With T=diag(t), T^(1/2)QT^(−1/2) symmetric; t^TQ=7t^T. Connected H gives simple eigenvalue 7. On t^T x=0, eigenvalues solve x²+x−14=0. Its irreducibility over ℚ and integer characteristic polynomial force equal α,β multiplicities. Thus c=1+2m∈{1,3,5}, tr Q=7−m. Target lines 87–102. | Discharged |
| M4 | c=3, positive integer t_i summing six ⇒ sorted profiles (4,1,1),(3,2,1),(2,2,2), exhaustively. For (2,2,2), symmetric integer Q would have odd total off-diagonal sum 21−6=15. Target lines 104–107. | Discharged |
| M5 | t=(4,1,1): balance and row degree imply a,b∈{0,1}. Trace gives 5(a+b)+2d=15. Parity forces a+b=1, d=5; a small row then contains 4+5>7. Target lines 109–118. | Discharged |
| M6 | t=(3,2,1): integer balance gives listed 2a,3a,b,3b,d,2d with a,b≤2,d≤3. Trace 5a+4b+3d=15 and a=0,1,2 leave only (1,1,2). Its Q has (Q²+Q)_11=16+6+3+4=29≠35. Target lines 120–138. | Discharged |
| M7 | c=5 ⇒ only profile (2,1,1,1,1). Trace B=A−2 and nonnegative q_00 give 2≤A≤7; symmetry of B makes 30−3A even ⇒ A∈{2,4,6}. Diagonal equation: (7−A)(8−A)+2∑a_i²=28. A=2 violates nonnegativity; A=6 violates square parity; A=4 gives sum four, squares eight, hence (2,2,0,0). Every (Q²+Q)_0j is then even, contradicting required seven. Target lines 140–163. | Discharged |
| M8 | M4–M7 ⇒ c=1. Fibre-constant subspace and W are invariant under symmetric H,E. D and J vanish on W. Real λ of H|W gives E-eigenvalue λ²+λ−7. For connected 7-regular E, spectrum lies in [−7,7] with simple top eigenvalue supported outside W; hence −7≤λ²+λ−7<7. Roots give strict β<λ<α and λ∉(−1,0). Target lines 165–178. | Discharged |
| M9 | Connected bipartite E: every matching reverses its two parts, so r_i=6−r_j for i≠j. Three distinct fibres force all r_i=3. Thus z∈W and spans the simple E-eigenspace at −7. HE=EH gives Hz=λz; M8 identity gives λ∈{0,−1}. Seven ±1 summands make every coordinate of Hz odd, excluding zero and forcing Hz=−z and the 3/4 H split. Target lines 182–194. | Discharged |
| M10 | Nonbipartite connected E has no eigenvalue −7, excluding H|W eigenvalues 0 and −1. In the bipartite case any zero H|W vector would lie in span(z), where H acts as −1. On fibre constants, H acts as J_8−I_8, with eigenvalues 7,−1, and thus is nonsingular on the full space. Target lines 180–196. | Discharged |

No limits, derivatives, integrals, expectations, stochastic modes, asymptotic notation, or uniformity parameters occur. Their associated checks are not applicable. All inequalities are exact and finite dimensional.
