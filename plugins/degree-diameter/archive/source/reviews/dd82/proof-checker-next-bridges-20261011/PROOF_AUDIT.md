# Fresh review of four DD82 paper bridges

Verdict: **PASS for the four stated paper results, same-family and provisional.** No mathematical gap or counterexample was found in the reviewed scope. This is not a compiled Lean certification, a cross-family acceptance, a proof of all nine-deletion Brown branches, or a solution of the exact degree–diameter problem.

The reviewer read the complete primary proofs and the dependencies listed below, without consulting previous review verdicts. The requested/accepted reviewer configuration was `gpt-6-astra` / `ultra`; the actual backend identity is not exposed. Reviewer identifier: `/root/proof_review_next_bridges`.

The project proof-checker skill was applied with the explicit overrides: review artifacts only, no source or wiki edits, no TeX/PDF/HTML, no hashes, no Lean edits/builds, and no large Brown deletion-profile rerun.

## Exact accepted scope

1. `proofs/dd82/n59/n15_heavy_endpoints_avoid_two_triangles_20261011.md`: in an actual legal order-59 graph, N15 at **all** zero-triangle vertices rules out a weight-two defect entry from a zero vertex to a vertex in two or three triangles. No H5 minimal-root premise is used.
2. `proofs/dd82/construction/BROWN_R9_EIGHT_III_OBSTRUCTION.md`: an order-58 Brown57 extension cannot delete exactly one edge from each of eight distinct III triangles and one EE edge. Added old–old edges are unrestricted subject to the original graph conditions. Other nine-deletion branches are outside this theorem.
3. `formal/N63_ALGEBRAIC_ROUTE.md`: the rational-characteristic-polynomial route is a complete paper argument excluding an original legal order-63 graph, using the checked finite coefficient/norm table and standard algebraic theorems. The enumerated Lean obligations remain implementation work.
4. `proofs/dd82/n59/two_triangles_shared_edge_exclusion_20261011.md`: under full induced-matching N15 at every zero vertex, exactly two triangles sharing an edge are impossible. The zero-endpoint transport and weighted-triangle-support lemmas also hold in their stated broader local scope.

## 1. Heavy endpoints: both potentially delicate steps hold

At a hypothetical two-triangle heavy endpoint v, the two edges of H=G[N(v)] are either disjoint or a two-edge path. The independent three-parent set S of the zero vertex z therefore contains a point p isolated in H. The nonedge repeat budget at v is exactly two and is exhausted by z, so every other point outside N[v] has one parent.

The eight neighbors of p are v, z, and six ordinary children y. No such child meets z, since pzy would be a triangle at z. At (v,y), commutation gives

`sum(q in N(v)) B[q,y] = sum(q in N(v)) deg_H(q) A[q,y] + 2 A[z,y] = 0`.

Every summand on the left is nonnegative. In particular B[p,y]=0 for every child. Also B[p,v]=B[p,z]=0. These exhaust all edges incident with p, so p is a zero vertex. Applying N15 to p is thus justified by the global zero-row assumption, not by an extremal-root transfer.

For q in N(v) other than p, p and q are nonadjacent. Their common neighbors are v and, precisely when q belongs to S minus p, the vertex z: no other outside point has two parents, and p has no neighbor in H. Thus exactly the two vertices S minus p have B[p,q]=1. N15 says that this entire light pair is adjacent. Independence of S contradicts it. The three-triangle endpoint case has nonedge budget zero and needs no additional lemma.

The proof actually uses only the zero-row 2211 counts and adjacency of the two light endpoints. The induced absence of cross-weight edges, heavy-pair adjacency, H5 minimality, N9, a K bound, and a global t≤2 assumption are not needed here.

Counterexample attacks: allowing the two H edges to meet still leaves independence number two on their nonisolated support; allowing extra triangles at p is blocked edge by edge by the commutation calculation; additional light endpoints at p violate the stated exact 2211 row. None produces a counterexample.

## 2. Brown branch: arbitrary additions and all small families checked

The order-58 root bound gives 8-regularity. Deletion deficits are d_v+[v in C]. In this branch C and the two deficient E vertices have deficit one, so the only spare incidences at S are the sigma internal points with deletion degree two. The number of C vertices outside S is j+e, while retained E-to-C coverage is at most 2e. At least max(0,j-e) spare incidences are consumed by C. Any other added incidence covers at most one new I vertex at distance two from the new vertex. This is an upper bound allowing overlaps, edges between vertices of S, and arbitrary added old–old edges; it does not presume those edges form a matching.

Every original I vertex belongs to four triangles and the target graph permits at most three. The EE deletion can destroy one IEE triangle and hence help only one internal vertex. The eight III triangles must therefore cover 20 or 21 internal vertices.

For a full-cover family the three repeated points form a selected central triangle. Its single deletion hits at most two of them, giving sigma≤2, e≤2 and j≤4. The internal-coverage bound is

`4j + 3e - max(0,j-e)`.

For j≥e this is 3j+4e≤20. For j<e, the maximum is 10. Both miss the required 21 points.

For a twenty-cover family, the uncovered m has deficit zero and cannot belong to S. The checked set Z consists of two triangles plus a unique cross edge, with six vertices. Double-deletion points and the permitted E endpoints have no old neighbors in Z. With e≤1 the previous bound is at most 19. With e=2, put k=j−sigma. The C demand forces k≤2 and leaves at most 2−k useful new incidences. Only these k single-deletion I points can supply old coverage of Z. Each covers at most three Z points; two cover at most five, since the only two candidates with size three are the cross-edge endpoints and their closed neighborhoods overlap in both endpoints. Thus the total coverage bounds for k=0,1,2 are respectively 2,4,5, all less than six.

The reviewer independently reconstructed the graph and checked every small family against the full edge list. Results in `independent_checks.json`:

- 57 vertices, 224 distinct simple edges; class sizes 8,21,28; all required neighborhood and triangle facts.
- All 3,003 eight-triangle subsets; 14 full-cover families and 42 twenty-cover families.
- All 84 permitted EE alternatives and all six structural predicates, with exact agreement with every stored family record.
- The stored coverage histograms were also checked.
- Execution used one CPU and a 30-second CPU/wall bound; actual runtime was about 0.025 seconds. No edge-choice profile, SAT call, or added-edge completion search was run.

Counterexample attacks: spare incidences at C/E do not exist in this branch; an added edge can provide only one endpoint on a length-two route from the new vertex; the uncovered m cannot be selected because its deficit is zero; two exceptional Z neighborhoods overlap rather than covering six points. These are exact obstructions under the stated branch, not assumptions about general extensions.

## 3. Rational n63 route: complete paper algebra, pending formal implementation

The actual nonnegative integral defect has zero diagonal and row sum two. A weight-two entry exhausts both endpoint rows and forms a doubled edge. All remaining components are finite simple 2-regular graphs, hence cycles. Orienting those cycles and transposing each doubled edge constructs B=P+P⁻¹. The permutation is a representation of B; it need not preserve adjacency in G.

The recurrence R_r(P+P⁻¹)=P^r+P^−r follows by multiplication and cancellation of the commuting powers. Each orbit has an actual length r≤63, so its own factor R_r(B)−2 kills its coordinate subspace. The product H kills the whole space because its factors commute. This preserves the conductor bound: every divisor ell of an actual r is ≤63. Replacing this with unrestricted divisors of an lcm would not justify the same table, and the source explicitly avoids that mistake.

The checked factor identities express H using only the C_ell. The existing Chebyshev checker was read in full; its exact recurrence, multiplication, and composition tests cover precisely the displayed 63 identities and coefficients. Those already checked small identities were not rerun in this review. Separately, the reviewer independently reconstructed all 63 cyclotomic polynomials and checked all 61 nontrivial Laurent lifts, both degree-one special cases, all 63 exact norm values, all 62 nonsquare witnesses and square brackets, and the entire Markdown table against the JSON.

For completeness, the Laurent lift has a direct algebraic proof. If f has degree a,

`L(f) = sum_j f_j T^(a-j) (T²+1)^j`.

Every exponent is nonnegative. Only j=a contributes degree 2a, with nonzero coefficient f_a, so deg L(f)=2a. Inside Q(T), L(f)=T^a f(T+T⁻¹), and deg(fg)=deg f+deg g yields L(fg)=L(f)L(g). Polynomial embedding into Q(T) is injective. A nontrivial factorization of C_ell would therefore factor its checked lift Phi_ell into two nonconstant rational polynomials, contradicting cyclotomic irreducibility. This proves the required irreducibility without a real-subfield theorem.

Alternatively, the source's tower proof is also sound: zeta solves a quadratic over Q(mu); the degree-2d cyclotomic field therefore forces [Q(mu):Q]≥d, and the monic degree-d annihilator gives the reverse bound. Neither argument uses the norm nonsquareness it is later meant to establish, so there is no cycle.

For K=Q[alpha]/(C_ell), multiplication by alpha has characteristic polynomial C_ell in the power basis. Consequently

`Norm(29+4 alpha) = det(29I+4M) = (-4)^d C_ell(-29/4)`.

The sign and scaling in this identity are correct. A square in K has square rational norm. A rational square that is an integer is an integer square, so the checked nonsquare residues prove nonsquareness for all ell except 3. For ell=1,2 the same reasoning takes place in Q. The ell=3 discriminant is 25 and its composition factors as (X−2)(X+3).

The irreducible-composition step can also be established without an API claim: if beta solves q(X)−alpha over K, nonsquare discriminant gives degree two over K. Since alpha=q(beta), Q(beta) contains K; its degree over Q is 2d, equal to the degree of C_ell(q(X)). Hence that composition is irreducible. The cited Lean interfaces are implementation suggestions, not mathematical premises of this audit.

On the rational sum-zero space W, dimension is 62, trace(T)=−8, and q(T)=U. The annihilator H(q(T)) vanishes. To justify characteristic-factor support directly, take a root beta of an irreducible characteristic factor in an algebraic closure. The vanishing determinant gives a nonzero eigenvector; applying the annihilator to it yields H(q(beta))=0. The minimal polynomial of beta, that characteristic factor, therefore divides H(q(X)). This supplies the claimed factor support without diagonalizability or equal-multiplicity assertions.

Every nonexceptional composition is monic of degree 2d with next coefficient d. Monic degree and next-coefficient addition yield

`62 = p+q+sum(2d e)` and `8 = -2p+3q+sum(d e)`.

Their difference gives 46=5(p−q), impossible. The sign of the trace coefficient and the constants were checked independently.

Counterexample attacks: doubled edges, short ordinary cycles, the exceptional conductor 3, the constant direction, possible repeated annihilator factors, and the lcm/conductor distinction are all handled. No unproved equal-eigenvalue multiplicity assertion is needed.

The six Lean obligations listed by the source remain uncompiled in this audit. No new build was performed, and no current declaration or upper-bound status is inferred from a concurrent build. A complete paper proof and an incomplete Lean implementation are consistent here.

## 4. Shared-edge T=2: the local obstruction closes the proof

Full induced-matching N15 is essential for the transport identity. If x is zero and B[r,x]>0, r has exactly one neighbor in the support of row x, its equal-weight partner. Hence (BA)[x,r]=B[x,r]. Since A and B are symmetric and commute, BA is symmetric, giving (BA)[r,x]=B[r,x]. This use is stronger than the reduced hypotheses sufficient for the heavy-endpoint lemma, and the shared-edge theorem explicitly supplies it.

For a complete row support consisting of triangle vertices a,b,c of weight one, a zero x of weight two and a zero y of weight one, transport at x gives

`2 = number of neighbors of x in {a,b,c} + A[x,y]`.

A zero vertex meets an actual triangle in at most one neighbor. Thus A[x,y]=1. Transport at y then forces `1≥2 A[x,y]=2`, a contradiction. No global two-triangle assumption is used by this reusable local lemma.

For the diamond uvw,uvz, the shared vertices have only zero vertices available for nonedge repeats. The reviewed heavy-endpoint lemma forces their budget-two residual row to be 11. If B[w,z]≥2, an extra common neighbor x is zero and nonadjacent to u. Its common neighbors w,z give B[u,x]>0. Transport and the two unit entries from u to w,z then force B[u,x]≥2, and zero-row N15 bounds it above by two. This contradicts the heavy-endpoint lemma. Therefore B[w,z]=1.

There are exactly 55 zero vertices. Their row square sums are ten; each shared vertex contributes eight. The tips contribute 3+q_w and 3+q_z, with q_w,q_z in {3,5}, giving s=572+q_w+q_z. The universal trace derivation in the dependency gives tr(A⁴)=126n+s−12T. Independently, a simple 8-regular graph has

`tr(A⁴) = 2|E| + 4 sum_v choose(8,2) + 8 C4 = 120n + 8 C4`.

Therefore 8C4=6n+s−12T, and with n=59,T=2 one has s≡6 mod 8. Of 578,580,582 only 582 qualifies. Both tips have zero-repeat pattern 21. Each tip row now contains the opposite triangle with weights 111 and zeros with weights 21, contradicting the local obstruction.

Counterexample attacks: cross-weight support edges would invalidate transport, but the theorem explicitly excludes them; an extra common neighbor of the tips would force the forbidden heavy zero-to-shared-vertex entry; adding a tip edge creates additional triangles; the row sum permits exactly 111 or 21 at the remaining zero endpoints. No other case survives the stated hypotheses.

## Dependencies read and remaining scope

Complete primary documents: the four named sources above; `proofs/dd82/FOUNDATIONS.md`; `proofs/dd82/construction/BROWN_EIGHT_DELETE_OBSTRUCTION.md`; `proofs/dd82/construction/N63_CYCLOTOMIC_SPECTRAL_OBSTRUCTION.md`; and `proofs/dd82/n59/matching_zero_global_trace_obstruction_20261011.md`.

Complete checker sources: `brown_eight_delete_facts.py`, `brown_r9_eight_iii_facts.py`, `n63_cyclotomic_norms.py`, and `formal/check_n63_chebyshev.py`. The full edge list and all data records of `brown_r9_eight_iii_facts.json`, `n63_cyclotomic_norms.json`, and its Markdown table were read/validated. Historical status sentences embedded in primary proofs were not used as evidence; prior review files were not opened.

The Brown eight-deletion paper was used for its exact graph facts and degree-resource setup; its earlier branch exclusions are not needed to prove the present nine-deletion branch. The original n63 spectral paper supplied the actual-graph and arithmetic dependencies; the rational argument supplies its own replacement for the real-eigenspace trace step. Only the universal fourth-trace identity is imported from the global trace document; no fifth-cycle classification is required by the shared-edge proof.

No paper gap remains for these statements. The following remain outside their conclusions: deriving N15 for every original order-59 graph, excluding all T=2 configurations or H5, excluding the six-III/seven-III nine-deletion Brown branches, excluding arbitrary order-58 graphs, finishing the n63 Lean caller, and determining the exact extremal value.
