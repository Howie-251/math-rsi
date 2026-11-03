# Scoped proof-obligation ledger

Reviewer: `/root/proof_review_reductions`. Fresh primary-source review; no prior reviewer verdicts read. Same-family, provisional. Requested configuration: `gpt-6-astra` / `ultra`; the accepted configuration is not independent backend attestation.

## Statements and hypotheses

- **F65:** Every finite simple undirected 65-vertex graph with maximum degree at most 8 has a distinct pair with neither an edge nor a common neighbor.
- **F64-11, F64-5:** The same assertion for 64 vertices, by separate finite-field arguments.
- **R62:** Every 62-vertex original candidate has actual defect entries at most 2 and admits one of the seven displayed root templates. Every candidate in S_DISJOINT admits one of the 80 symmetry representatives with Boolean refinements. This is coverage, not exclusion.
- **H59-L:** For every 59-vertex original candidate whose zero-triangle vertices satisfy the explicitly assumed 2211 matching-row condition, the trace difference is supported on pairs of nonzero-triangle vertices.
- **H59-T1:** Under H59-L's hypotheses and exactly one triangle, the three triangle rows necessarily have type 1111 and, after relabeling, c=(1,1,2), a=(2,2,0). Their full support graphs and private-neighborhood cross edges have the stated forms. No inconsistency of this remaining form is asserted.

All graph-to-matrix hypotheses are discharged by the actual adjacency matrix and root-ball count in `FOUNDATIONS.md`, rather than by assuming an abstract matrix is realizable. H59-L assumes N15 as a row condition; this review does not establish H5 implies N15. H59-T1's optional minimum cycle length additionally uses the specified short-cycle paper proofs.

## Typed symbols

`A,B,I,J`: n by n integer matrices; A is symmetric binary with zero diagonal, B=A²+A−7I−J. B has nonnegative integer entries, zero diagonal and row sum 65−n. Finite-field sections explicitly reduce these matrices to F29, F11 or F5. `M,D,E,X` are matrices over the stated ring, not independent graph data.

For R62, S and E+/E− are disjoint vertex cells of sizes 4 and 4/4; U,V have size 24. `N` is a symmetric 4 by 4 nonnegative integer matrix, zero diagonal, row sum 3. `L,Q` are V by V adjacency/defect blocks. `C=A[E,V]` is 8 by 24 and `D=A[U,V]` is 24 by 24; this local D is unrelated to the finite-field D. The Gram matrix is DᵀD.

For H59, `t(v)` is a nonnegative triangle count, `N={v:t(v)>0}`, and `R₂` is the simple graph of nonedge pairs with B-entry 2. `q_v,a_v,c_v,e_v` are integers. The scalar w in the trace identity and the vertex w in the later single-triangle notation have explicitly separated scopes. Q₂(v) is the weighted support edge count, not a count of components. All statements are finite exact identities; there are no limits, probabilistic modes or asymptotic uniformity obligations.

## Dependency DAG

Root-ball count → 8-regularity → actual defect identities.

- Actual defect at n=65 → B=0 → M²=4J over F29 → power/trace computation + trace Frobenius → F65.
- Actual defect at n=64 → involution B and AB=BA → D²=17I+16B+4J → either triangle-free trace calculation over F11 or explicit pair basis/determinant over F5 → F64.
- Actual defect at n=62 → triangle bound → hypothetical triple edge → five cells → three N-types → eight L-lifts + complete Q enumeration → unique Gram case → row-pattern multiplicities + parity → no triple edge → four-cycle parity → seven templates → S_DISJOINT orbit refinement.
- Actual defect at n=59 + N15 row hypothesis → positive-entry product identity → trace localization. Add T=1 → row types/ranges. Actual fourth/fifth traces + closed-walk counts → four candidate row multisets → private-neighborhood edge equations → unique necessary form → complete support forms. Add independently read short-cycle paper proofs → optional cycle length at least 10.

No dependency returns from an intended n62/n59 exclusion to a reduction used to establish it.

## Micro-claims and discharge

| ID | Context ⊢ conclusion; rule and discharge |
|---|---|
| G1 | Original graph ⊢ n≤1+8 deg(v); union count of genuine length-2 paths. For n>57 and degree≤8, every degree is 8. |
| G2 | G1 ⊢ B≥0, diagonal 0, B1=(65−n)1 and AB=BA; common-neighbor identity and AJ=JA=8J. |
| G3 | G2 ⊢ adjacent-row defect sum=2t(v); each triangle uses exactly two root-incident edges. |
| 65a | δ=0 ⊢ B=0; nonnegative integral zero-sum rows. Thus (2A+I)²=29I+4J. |
| 65b | Reduction mod29 ⊢ tr(M²⁹)=17(4·65)¹⁴=17, while tr(M)=7; J^k=65^(k−1)J and MJ=17J. |
| Frob | Square matrix over Fp ⊢ tr(M^p)=tr(M); prime cyclic orbits have size 1 or p, scalar products commute, constant words use a^p=a. |
| 64a | δ=1 ⊢ B is a fixed-point-free pairing and B²=I; integral row sums and symmetry. |
| 64b | Pairing ⊢ D²=17I+16B+4J; X²=2X, AX=XA and A²+A=7I+J+B. |
| 64c | δ=1 ⊢ triangle-free and tr(AB)=0; a triangle consumes two units of a row with total 1. |
| 64d | Mod11, E=(I−B)/2 ⊢ D^(k+2)=E+4·17^k J for all k≥0; DE=E, DJ=17J, including k=0. Traces at exponent 11 are 5 and 9. |
| 64e | Mod5 pairing ⊢ basis f_i,g_i; 2 is invertible. D² blocks are 33I₃₂+8J₃₂ and I₃₂. |
| 64f | Positive m ⊢ det(aI+bJ)=a^(m−1)(a+mb); multilinearity, no division by a. Hence det(D²)=3, impossible for a square in F5. |
| 62a | δ=3 ⊢ t≤1, adjacent B≤1; G3. A triple edge is nonadjacent and exhausts both endpoint rows. |
| 62b | Triple edge ⊢ S,E,U,V counts and isolated B cells; common-neighbor counts plus energy identity for Bf=3f, and signed row equation for Bg=−3g. |
| 62c | Isolated cells ⊢ quotient R and N=Nᵀ with diagonal 0; count each pair against u,v,S and use AB=BA and G3. |
| 62d | N row sum 3 ⊢ opposite entries equal and three types; the (3,0,0) and (2,1,0) types force Q weight on a forced L edge, contradicting triangle-freeness of V. |
| 62e | N=J−I ⊢ twelve ordered types each of size 2 and eight covering L lifts; each complementary block is a 2-lift of K₂,₂, three matchings gauged to identities by copy relabeling. |
| 62f | Original graph ⊢ Q simple cubic, prescribed label marginals, L∩Q empty and LQ=QL; E,V and V,V commutator blocks and no cross-cell triangles. |
| 62g | Original graph ⊢ DᵀD=7I+J+Q−CᵀC−L²−L and CDᵀ=J; exact V,V and E,U point-pair equations. Gram filters are necessary relaxations. |
| 62h | Checker source ⊢ all allowed Q considered; every local row mask enumerated, branching tries every option, singleton propagation removes only asymmetric choices, completed matrices checked for commutation. Bounded rerun reproduces every table entry. |
| 62i | CDᵀ=J ⊢ derangement row supports and six-row partition per U_s; V has one U_s-neighbor. All 24 candidates and copy strings reproduced. |
| 62j | Resolution ⊢ each of A–F used once; types 01,13,30 force a=b=d=1; types 23,12,03 force c=f=e=1. Eight displayed F2 equations sum to 0=1. |
| 62k | No triple edge ⊢ 2Q₄=93+d−3T and d−T odd; count common-neighbor pairs, including all chorded four-cycles. Simple B therefore supplies a root triangle. |
| 62l | Double root ⊢ parent sets of sizes 3,2 with three intersection orbits and optional wa edge only in disjoint case; Y_w incidences force the stated singleton counts and two b-orbits. Simple root supplies two remaining templates. |
| 62m | S_DISJOINT ⊢ one Aw point in each of six classes; the six required root-label common neighbors exhaust w's six Y-neighbors. Two remaining B-neighbors both lie inside Aw or outside. |
| 62n | Stabilizer of root data and Aw ⊢ twelve pair orbits, four nonswappable and eight swappable; class relabelings preserve all fixed data. Triangle bits and bc edge give 4·4·2+8·3·2=80 coverage cases. |
| 59a | Zero row N15 + positive B_xv ⊢ (BA)_xv=B_xv; only the same-weight partner contributes. AB=BA and symmetry give localization, without replacing full AB by an induced block. |
| 59b | T=1 ⊢ triangle-edge repeats 1 and other repeat total 4 with entries≤2; other endpoints are N15 zero vertices. Hence 22,211,1111. |
| 59c | Two counts of b_vᵀAb_v ⊢ q=a+2c and e=4−c; terms are q+2+a and 2+2a+2c. Unique triangle gives 0≤a≤4 and the displayed local ranges. |
| 59d | Full graph traces ⊢ tr(A⁴)=126n+s−12T and tr(A⁵)=428n+w−2s+102T. Walk support counts give tr(A⁴)=120n+8C₄ and tr(A⁵)=10C₅+210T. |
| 59e | N15 zero rows ⊢ s_v=10, 2Q₂(v)=10; fifth trace yields Σe+T≡4 mod5. R₂ handshake gives even n211. Fourth trace at T=1 yields n211+2n1111≡2 mod4. |
| 59f | 59c–e ⊢ exactly four row-multiset candidates; exact small arithmetic independently reproduced. |
| 59g | Unique triangle ⊢ disjoint six-point private neighborhoods and B_ux=|N(x)∩P_u| for x∈P_v; the only other common neighbor is v. Hence a_u=m_uv+m_uw and cyclic equations. Nonnegative m eliminates three candidates. |
| 59h | Remaining all-1111 form ⊢ m_uv=2, other m=0, and two cross edges form a matching; B≤1 bounds endpoint degrees. Positive-entry product identity gives degree 1 at every zero point within the relevant six-point support. Hence two K₁,₃+K₂ and one 3K₂. |
| 59i | All three triangle points have R₂ degree 0 ⊢ R₂ on the other 56 points is 2-regular. The separately read C3–C9 arguments exclude its shorter cycles under the same local matching-row assumptions. |

## Unproved objectives outside these statements

No branch contradiction or graph-to-CNF equivalence for arbitrary n62 graphs is supplied. H5→N15 is an explicit inherited premise, not proved here. The single-triangle normal form and general triangle-containing n59 range are not excluded. No Lean/kernel acceptance follows from this ledger.
