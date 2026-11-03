# Proof audit: the actual 12/20/30 component quotient

Date: 2026-10-11. Reviewer: fresh Codex agent `/root/proof_review_n62_12_20_30`.

**Verdict: PASS — same-family, provisional.** The complete target proof discharges its obligations relative to its explicitly imported order-62 results. No FATAL, CRITICAL, MAJOR, or MINOR mathematical issue was found. No proof changes were needed or made. This is a paper-proof review, not a Lean verification or a cross-family acceptance.

## Exact reviewed scope

Input: `proofs/dd82/n62/THREE_COMPONENT_12_20_30_EXCLUSION.md`, all 232 lines as read in this review.

The statement checked is: for every actual finite simple undirected graph G with 62 vertices, maximum degree at most eight, and diameter at most two, its actual repeat matrix B = A² + A − 7I − J cannot have exactly three positive-support components C,D,E of sizes 12,20,30, whose original-graph quotient, in that order, is

    R = [[3,0,5], [0,2,6], [2,4,2]].

The result excludes this specific actual quotient. It does not certify any quotient enumeration, exclude all three-component quotients, exclude a connected repeat matrix, classify larger D1 components, exclude all order-62 graphs, or determine N(8,2). No order-63–65 argument was reopened.

The project proof-checker skill was read and applied. User overrides restrict outputs to Markdown/JSON and forbid hashes/checksums and TeX/PDF/HTML. The dependency/assumption ledger and micro-claims are included below. No prior target audit was read. Imported claims were checked against their actual source text; their existing audits were not substituted for source statements.

## Dependency alignment

The review distinguishes checking an imported statement and its application from reopening the complete earlier proof chain.

| Imported source and relevant location | Claim actually read | Discharge at the target application |
|---|---|---|
| `RECOVERED_REDUCTION.md`, Step 1 and the explicit conclusion of the triple-repeat proof | Actual G is eight-regular; B is symmetric, nonnegative integral, zero-diagonal, row-sum three; AB=BA; c(u,v)+Auv=1+Buv; Buv≤2 | The target uses the same actual adjacency and exact B, never an independent matrix model. These give its common-neighbor and block identities. The prior bounded triple-repeat computation is an imported dependency, not rerun here. |
| `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`, assumptions and Sections 2–3 | Double edges are D0 or D1 after the cited local exclusions; D0 has a closed four-vertex component; the B-component partition is equitable for A | C,D,E are whole positive-support components. Consequently the displayed quotient yields P cubic, Z two-regular, X of row sum five and column sum two, and A[C,D]=0. |
| `D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md`, first two statements | Both surviving D0 forms force a whole four-vertex B-component | No component of the specified sizes is four, so a double in C cannot be D0. The stronger existence-of-D1 conclusion is not used. |
| `TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md`, Sections 1–4, especially lines 105–108 | The paired original triangles have three distinct matched repeat mates; the six rows are exhausted by the two triangles and their matching | Those six vertices form a connected closed B-component. Therefore absence of a size-six component forces the whole G to be triangle-free. The pairing proof does not assume B simple. |
| `D1_COMPONENT_MINIMUM_SIZES.md`, Sections 1, 6, 7 | H=K implies size at least 14; otherwise a size-12 heavy component has exactly five possible (k,a,b) triples: (12,4,4), (16,4,3), (20,5,3), (24,6,3), (28,7,3) | This is the correct heavy-component notion for a double inside C. It does not merely bound the component containing its generated triangle. |
| `D1_TWELVE_COMPONENT_EXTERIOR_EXCLUSION.md`, statement; `D1_TWELVE_EXTERIOR_MOMENT_REFINEMENT.md`, statement table | The size-12 partner is excluded; the remaining lists are seven size-16 internal-degree pairs, two size-20 pairs, one size-24 pair, and no size-28 pairs | Actual claims align with the five-choice list; no missing partner size is silently discarded. |
| `D1_TWELVE_TWO_LARGE_PARTNER_EXCLUSIONS.md`, statement; `D1_TWELVE_TWENTY_ZERO_TWO_EXCLUSION.md`, statement | Exclusion of (h,k,a,b,s,t)=(12,20,5,3,1,2), (12,24,6,3,0,2), and (12,20,5,3,0,2) | These remove both size-20 cases and the size-24 case. |
| `D1_TWELVE_SIXTEEN_PARTNER_EXCLUSION.md`, complete proof and consequence, especially lines 279–298 | All seven remaining size-16 cases are excluded; combined with the preceding sources, every D1 heavy H has size at least 14; generated-triangle K also has size at least 14 | Thus a double inside C would make its heavy component C have both size 12 and size at least 14. Only the heavy bound is required by the target. |

The relevant source claims match the target. Earlier proof validity remains the declared imported basis; this audit is not a fresh audit of every transitive dependency. None of the inspected dependency steps uses the new 12/20/30 exclusion. The target's dependency graph is acyclic: actual identities and local component theorems → simplicity of B_C and triangle-freeness → connected P and W identity → connected F → incidence-kernel control and spectrum bound → trace contradiction.

An optional dependency reduction is available, without changing the verdict or the proof: Section 4 of `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md` alone rules out a D1 heavy pair in C. Its generated-triangle component cannot equal C because r_CC=3<4, cannot be D because r_CD=0<4, and cannot be E because r_EC=2<3. The written proof's stronger heavy-size import is nevertheless correctly applied.

## Symbols and hypotheses

| Symbol | Type and properties verified before use |
|---|---|
| A, B | Real symmetric 62×62 matrices arising from G; A is a simple adjacency matrix, B its exact integral repeat matrix |
| C,D,E | All three B-support components, respectively of sizes 12,20,30 |
| P, B_C | Real symmetric 12×12 matrices; both become simple cubic connected adjacency matrices, for different graphs |
| X | A[C,E], a binary 12×30 matrix, row sum five, column sum two |
| Z | A[E,E], a binary symmetric zero-diagonal 30×30 matrix, row sum two; connectedness is not assumed |
| F,W | Loopless multigraph interpreted as a weighted support graph on C; W=XXᵀ−5I is symmetric, nonnegative integral, zero-diagonal, row sum five |
| U,q,S | U consists of F-component-constant vectors, q=dim U; S is the integer row-sum-three quotient representing B_C restricted to U |
| f,λ | In the nonzero incidence-kernel case, f is the ±1 bipartition vector and λ its P-eigenvalue |
| p | Exact polynomial p(t)=(t−1)(t+3)²=t³+5t²+3t−9 |

The symbols do not change their meanings. All arguments are finite-dimensional and exact. There are no limit/integral/expectation interchanges, probability-mode upgrades, asymptotic statements, or uniformity obligations.

## Proof-obligation ledger

| ID | Target location | Obligation and checked justification |
|---|---|---|
| MC-01 | Lines 28–47 | Actual component equitability gives every claimed block dimension and degree, with quotient orientation r_ij = neighbors in j of a vertex in i. In particular 12·5=30·2 and 20·6=30·4. |
| MC-02 | Lines 68–73 | Triangle pairing forces a size-six component; D0 forces size four; D1 heavy size is at least 14. Together with B≤2 these make G triangle-free and B_C simple cubic connected. |
| MC-03 | Lines 75–87 | Internal common neighbors in P are a subset of actual common neighbors. Thus none of its pairs can have three common neighbors. Each cubic component has even order at least four; order four is K4, and a triangle-free cubic graph of order six is K3,3. Both are excluded. Every P-component has at least eight vertices, so twelve vertices permit only one. |
| MC-04 | Lines 91–108 | Each X-column has two distinct endpoints. Its outer product contributes one to both endpoint diagonal entries and one to both off-diagonal pair entries. Hence W=XXᵀ−5I is exactly weighted adjacency, W1=5·1, and the C,C block identity gives W=2I+J+B_C−P²−P. |
| MC-05 | Lines 110–113 | Because B has no cross-component entries, (AB)[C,C]=PB_C and (BA)[C,C]=B_CP. Regularity and symmetry give commutation with J, so W commutes with P and B_C. This does not assume that A preserves an individual B-component. |
| MC-06 | Lines 115–125 | The weighted Laplacian energy identity proves ker(W−5I)=U even with repeated edge columns. Commutation makes U invariant. The indicator basis then proves B_C-equitability of the F-component partition, not merely invariance of one aggregate vector. |
| MC-07 | Lines 125–130 | If q>1, each proper F-component has a B_C-edge to its complement because B_C is connected. Equitability and integrality make the external count at every vertex at least one. Thus each diagonal quotient entry is at most two and tr S≤2q. |
| MC-08 | Lines 132–152 | Since P is regular symmetric and preserves U, it preserves U∩1⊥. Here W=5I and J=0, so B_C=P²+P+3I. Its q−1 eigenvalues on that subspace are at least 11/4, while its remaining eigenvalue is three. Trace is invariant under the component-indicator change of basis, even though S need not be symmetric. Thus tr S≥3+11(q−1)/4, exceeding 2q by (3q+1)/4. F is connected. |
| MC-09 | Lines 156–169 | The C,E block has no A[C,D]A[D,E] term and no B[C,E] term, giving PX+XZ+X=J. For v⊥1, transposition yields ZXᵀv=−(λ+1)Xᵀv. If Xᵀv≠0, nonnegative symmetric row-sum-two Z has spectrum in [−2,2], so λ∈[−3,1]. |
| MC-10 | Lines 171–179 | Kernel equations are f_u+f_v=0 for every support edge. Connectedness makes all values determined by one value. An odd cycle makes that value zero; otherwise the kernel is the one-dimensional bipartition-sign span. Weighted five-regularity forces equal bipartition sizes, hence f⊥1. |
| MC-11 | Lines 180–192 | Equation (6) gives XᵀPf=0 for the kernel sign vector. Its one-dimensional kernel is P-invariant. Cubic binary P yields λ∈{−3,−1,1,3}; P-connectedness excludes nonconstant eigenvalue-three vectors. Hence the previously omitted kernel direction also satisfies λ≤1. No eigenvector is lost. |
| MC-12 | Lines 196–209 | Simplicity, cubic degree, and triangle-freeness give tr P=0, tr P²=36, tr P³=0. Polynomial expansion and trace linearity give tr p(P)=72=p(3). |
| MC-13 | Lines 211–223 | Every nonprincipal p(λ_i)≤0, so their zero sum makes each zero. The only roots in the allowed interval are 1 and −3. Trace zero then requires an integer multiplicity b to satisfy 14−4b=0, impossible. The conclusion exactly excludes the displayed quotient. |

## Counterexample and degenerate-case pass

These are adversarial tests of the proof, not graph enumeration. No counterexample satisfying the full hypotheses was found.

1. **Disconnected P:** try the possible small cubic component obstructions. K4 produces triangles. K3,3 produces a pair with three common neighbors, violating the exact bound (1). In particular a 6+6 split does not evade the connectedness proof. Larger components cannot fit twice into twelve vertices.
2. **Disconnected auxiliary F despite a connected original graph:** original connectedness alone would not suffice. A weighted matching, for example, has six components and valid weighted degree five. The actual identity and commutation force a quotient with trace at most 12 but at least 67/4. Thus the argument specifically uses the missing actual-graph constraints; it does not infer F-connectedness from original connectedness.
3. **Unequal F-component sizes and nonsymmetric S:** neither invalidates the trace argument. S is the matrix of the restriction in the indicator basis, while the spectral calculation is in the induced Euclidean inner product. Similarity preserves trace. The contradiction holds for every q>1, with no equal-size assumption.
4. **Repeated X columns / parallel F edges:** repeated equations do not change the unsigned-incidence kernel, and the Laplacian energy uses their positive weights correctly. There are no loop columns because X is binary with column sum two.
5. **Bipartite F / singular Xᵀ:** this is retained explicitly. The sign kernel need not vanish. Unbalanced sides are impossible by weighted degree counting, and λ=3 is excluded using the already-proved connectedness of P. The other three possible odd eigenvalues are all allowed by the claimed bound.
6. **Nonbipartite F:** an odd-cycle equation forces the kernel parameter to equal its negative and hence zero, so no additional unseen eigenvectors remain.
7. **Disconnected Z:** the spectral interval [−2,2] uses only its actual nonnegative symmetric degree-two adjacency, not connectedness or the lengths of its cycles.
8. **Spectral boundary and cancellation:** λ=−3 and λ=1 both make p vanish. Every interior value makes p negative; no positive terms can cancel them. Allowing any multiplicity of either endpoint still requires b=7/2, so multiplicity and boundary cases do not evade the contradiction.

## Exact arithmetic check

One short standard-library Python process used exact integers and `Fraction`; no solver, numerical eigensolver, graph generator, or large computation was used. It verified:

- R has row sum eight and satisfies size balance and R²+R=10I+1(12,20,30).
- R²+R equals `[[22,20,30],[12,30,30],[12,20,40]]`.
- The polynomial coefficients are `[-9,3,5,1]` in increasing degree, and p(3)=5·36−9·12=72.
- For every integer q from 2 through 12 the exact trace gap is (3q+1)/4>0.
- No integer b from 0 through 11 solves 14−4b=0.

This corroborates the finite arithmetic; the semantic proof obligations are discharged by the derivations above. No source change, replacement assumption, or weakened conclusion was needed.

## Disposition

All target obligations are closed modulo the stated, previously reviewed imports; the imports' claim alignment was independently checked here. There are zero open issues and zero implemented fixes. The target may be recorded as a **same-family provisional PASS** for exclusion of this one actual quotient. Cross-family review, Lean formalization, quotient enumeration completeness, and the whole N8 goal are separate matters and are not claimed by this audit.
