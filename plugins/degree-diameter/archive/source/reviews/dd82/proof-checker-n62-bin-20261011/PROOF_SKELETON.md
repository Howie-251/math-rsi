# D0_EDGE_BIN proof obligations

Canonical statement: For every finite simple undirected graph G with |V(G)|=62, maximum degree at most 8 and diameter at most 2, there is no labeling satisfying D0_EDGE_BIN: root-neighbor set X={1,…,8} independent, Y=V\({0}∪X), distinct w,a in Y with parent sets 123 and 45, every other Y vertex with one parent, edge wa, and actual repeat entry B_wb=1 at b∈{4,5}. Here A is G's adjacency matrix and B=A²+A−7I−J. Relabeling within {4,5} sets b=4.

## Types and assumption ledger

| Symbol / hypothesis | Type and source | Used where |
|---|---|---|
| G | Finite simple undirected graph; 62 vertices; maximum degree ≤8; diameter ≤2. Recovered reduction lines 5, 28, 44–52. | F1 actual repeat identities |
| A | Symmetric 62×62 zero-diagonal {0,1} matrix. | All finite product equations; upper bounds on adjacency entries |
| B | Actual symmetric 62×62 integer matrix A²+A−7I−J; nonnegative with zero diagonal and row sum 3. | F2–F9 |
| AB=BA | From regularity and AJ=JA. | F5, F6, F7, F9 |
| X,Y | X=N(0)={1,…,8}; Y complement of {0}∪X; disjoint. | Parent counts; c∈Y implies A_c0=0 |
| P(y) | N(y)∩X; exact sets from original template JSON. | F2, F4; A_ab=1 |
| w,a | Distinct vertices 9,10 in Y; P(w)=123, P(a)=45. | F2–F8 |
| b | Vertex 4 in X and P(a); B_wb=1 from JSON fixed_B and recovered reduction lines 215–219. | F3, F5, F7–F9 |
| i,j,k | Fixed vertices 1,2,3 in X. | F4–F9 |
| c | Existentially determined vertex with B_ic=1 outside {0}∪X∪{w}. | F5–F9 |
| e_v | Unit row vector indexed by V at v. | Notation for complete B rows |
| Global repeat simplicity / B≤2 | Not assumed or used. | None |
| At most one triangle per vertex | Follows from 2t(v)=Σ_{u∈N(v)}B_vu≤3; true but not used after branch data. | None in the contradiction |

## Acyclic dependency graph

`G assumptions → F1; F1 + parent data → F2; F1 + F2 + B_wb=1 → F3; F1 + F3 + parent data → F4; F3 + F4 → F5; F2 + F4 + F5 → F6; F3 + F4 → F7; F6 + F7 + b∈P(a) → F8; F2 + F4 + F5 + F6 + F8 → F9.`

No node uses the target exclusion or another branch exclusion. No triple-edge elimination node is present.

## Micro-claims

| ID | Sequent and rule | Discharged conditions / proof location |
|---|---|---|
| F1 | Original graph hypotheses ⊢ regularity, nonnegative integral symmetric zero-diagonal B of row sum 3, AB=BA. | Moore count 57<62; finite matrix algebra. Audit derivation 1. |
| F2 | F1, X independent and exact parent sets ⊢ B₀=2e_w+e_a. | B₀y=|P(y)|−1; B₀x=0; exact singleton data. Audit 2; target lines 14–23. |
| F3 | F1,F2,B_wb=1 ⊢ B_w=2e₀+e_b. | Symmetry and 2+1 exhaust nonnegative row sum 3. Audit 2. |
| F4 | F1,F3 and exact parent sets ⊢ ∃!c∈Y\{w}: B_i=e_j+e_k+e_c. | Pair common-neighbor counts give exact X entries; B_i0=0; integrality of residual one; B_iw=0 from F3. Audit 3; target lines 27–37. |
| F5 | F1,F3,F4 ⊢ A_cw=0. | At (i,w): 2=2+A_cw; symmetry used for columns. Audit 4; target lines 41–49. |
| F6 | F1,F2,F4,F5 ⊢ A_ac=1 and c≠a. | At (0,c): 1≤(AB)_0c=(BA)_0c=A_ac≤1; zero diagonal. Audit 5; target lines 51–56. |
| F7 | F1,F3,F4 ⊢ A_cb=1. | At (c,w): A_cb=(BA)_cw≥B_ci A_iw=1; A_c0=0 and A_cb≤1. Audit 6; target lines 58–62. |
| F8 | F1,F6,F7,b∈P(a) ⊢ B_bc≥1. | a,b,c distinct; a common neighbor of adjacent b,c; actual repeat identity. Audit 7; target lines 63–64. |
| F9 | F1,F2,F4,F5,F6,F8 ⊢ 2≤1, contradiction. | Distinct summation indices i,b; all summands nonnegative; commuting products. Audit 8; target lines 66–71. |

All obligations are discharged. Limits, interchange theorems, asymptotics, and probability modes are not applicable. One theorem is audited; the intermediate claims above inventory its complete argument.
