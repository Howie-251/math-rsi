# Proof audit — 2026-10-11

**PASS within the stated scope; same-family / provisional.** No mathematical issue requiring a source change was found in the four complete files below. This is one fresh paper-proof review plus short independent exact checks, not cross-family acceptance or Lean verification.

Reviewer: `/root/proof_review`. The caller-requested `gpt-6-astra` / `ultra` / `fork_turns:none` routing was accepted by the spawn tool; no separate backend identity attestation was available. The project-local proof-checker skill and its reviewer routing/independence instructions were read. Prior review outputs were not read. Proof sources were not edited.

## Audited sources

- `C4`: `/inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/n59/h5_zero_r2_c4_interface_20261011.md`
- `Brown57`: `/inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/construction/BROWN57_PROOF.md`
- `Edit`: `/inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/construction/BROWN_EXTENSION_OBSTRUCTION.md`
- `Foundations`: `/inspire/hdd/global_user/mahaitong-240108120090/ar4math/proofs/dd82/FOUNDATIONS.md`

`PROOF_SKELETON.md` records canonical statements, typed symbols, hypotheses, applications, dependency edges, and the nontrivial counting steps. There are no open FATAL, CRITICAL, MAJOR, or MINOR issues. No fix is proposed or applied.

## Mathematical findings

**C4 exclusion (C4 L46–80).** The statement's B=2 cyclic pairs are indeed G nonedges: if either were an edge, its zero-triangle endpoint would force the corresponding B entry to vanish. The matching rows force the two G diagonals, and all external adjacency types then follow exactly. Step3 excludes a positive off-incident z–X B entry using mixed-weight nonadjacency; Step4 uses already-existing common neighbors, not an unsupported triangle-free assumption. The private graph contains its cycle before any diagonal is ruled out.

The charge at C4 L62–64 is valid. With exactly one X neighbor, its two covered labels are consecutive, so the two uncovered labels are also consecutive and force an actual private edge inside N(w). With no X neighbor all four private vertices are required. Summing gives H≥6, then at least12 private triangle incidences. Initially the correct global bound is t≤3; this first rules out private diagonals. Only afterward do opposite private vertices force a nonedge repeat and give t≤2. Thus the proof does not silently assume global t≤2. The contradiction is 12≤Σ_P t≤8.

**C4 interface (L84–111).** Direct block multiplication validates (1)–(5), including `Σ_W L_iw=2−δ_i` and `e(P,W)=20−Σ_i δ_i`. D retains its declared meaning as a 0/1 adjacency matrix (L28). The converse requires all graph degrees and the entire B matrix, so the note does not infer a graph from necessary integer counts alone. The H5 corollary remains conditional on H5⇒N15; that implication was not included in this review. The exclusion uses no assumption on the other55 rows. Light–light pairing is available but not needed for the exclusion itself.

**Brown57 (L26–31).** The 57 normalized projective representatives are distinct and exhaustive. A nonzero linear functional has48 nonzero kernel vectors and hence8 projective points; removing the isotropic self-point gives degree7, otherwise degree8. Distinct normalized points give independent coefficient rows. A common orthogonal point for a nonadjacent pair cannot be either endpoint. These arguments establish the complete graph claim independently of the supplied edge list.

**Brown extension (Edit L29–39).** Both regularity and edge balance are correct. The local radius-two triangle bound gives t_G≤3. For r=7 the counting chain is tight in every place: exactly seven destroyed old triangles partition I, each uses only I vertices, and each contains exactly one deleted edge. Therefore deletion endpoints are14 distinct I vertices. All22 deficient old vertices have deficit one; joining x consumes the entire deficit of every S vertex, so no added old edge can touch S. Since no old C–(C∪I) edge exists, coverage of C forces S=C, and then I cannot be covered. This proves r≥8 under the explicitly verified finite Brown premises; it does not prove absence of58-vertex graphs.

**Foundations (L19–59).** The Moore count includes the empty case and establishes regularity before all defect identities. Integer B is nonnegative off-diagonal by the original path condition. The rational quadratic lemma correctly uses irreducibility to form a quadratic field action. At65 vertices the sum-zero dimension64 gives trace−32 and hence total trace−24, contradicting zero diagonal. At64 vertices the defect matching gives an A-invariant rational sum-zero subspace of dimension31 annihilated by X²+X−8, contradicting even dimension. The resulting upper bound is63, without excluding63 itself.

## Counterexample attempts and exact checks actually executed

One independent inline Python program ran from the project root, with a60 CPU-second resource limit, using only Python standard-library integer/set operations. It imported no project generator, helper, solver, or prior review. It completed successfully in **0.069512464 CPU seconds**, with one process and no assertion failure.

1. **Charging inequality:** independently enumerated `d=(d_0,…,d_3)∈{0,1,2,3}⁴` and every private-neighbor subset P_w. Retained exactly the patterns with `Σd_i+|P_w|≤8` and `d_(i−1)+d_i+1_(i∈P_w)≥1` for every label i. For each of the four private-diagonal choices, there were1928 retained patterns; all satisfied `Σd_i+e(P[P_w])≥2`, with minimum2. The retained counts by total d_X=0,…,8 were `[1,16,80,208,400,536,456,200,31]`. This verifies the claimed local enumeration, not existence or nonexistence of whole59-vertex graphs.

2. **Apparent low-charge candidates:** one X_i neighbor with only one of the two missing-label private vertices, or no X neighbor with fewer than all four private vertices, can have too little charge but fails the four-label coverage premise. Such patterns were rejected before evaluation. Sharp valid local patterns exist: e.g. one X_0 neighbor plus s_2,s_3 has charge2. Adding either private diagonal can only increase h, so optional diagonals do not create a counterexample.

3. **Brown finite premises and source alignment:** read `computations/dd82/construction/brown57.edges`; checked57 vertices,224 distinct loop-free edges, exact equality to an independently generated F7 orthogonality edge set, degree distribution8 vertices of degree7 /49 of degree8, and every1596 unordered pair. The pair distances were224 at1 and1372 at2. Checked `|C|,|I|,|E|=(8,21,28)`, no C–(C∪I) edge,56 triangles (14 III and42 IEE), at most one triangle per old edge, and exactly four triangles at every I vertex.

4. **Edit-obstruction equality attack:** independently enumerated all3432 seven-subsets of the14 III triangles, found exactly two partitions of I, and all `2·3⁷=4374` ways to delete one edge in each partition triangle. Every pattern has14 distinct deletion endpoints in I and22 unit-deficit vertices, and no c∈C has an old neighbor in that deficit set. Thus every such pattern triggers the proved necessary condition S=C, which leaves every I vertex uncovered. Zero patterns survive this necessary coverage test. This was not enumeration of all added-old-edge matchings or all58-vertex graphs; those choices are eliminated uniformly by the unit-deficit proof.

5. **Other key-lemma boundary attacks:** checked the Brown common-neighbor endpoint possibility explicitly against nonadjacency; the isotropic self-point is excluded from degree counts. Checked the zero-dimensional case of the quadratic lemma, the empty graph in the root bound, and the odd-dimensional +1/sum-zero space in the64 case. None violates its verified premises. No genuine counterexample was found.

The existing C++ search, its runtime/node count, external historical record/attribution, and UPC-isomorphism report were not rerun or used as proof premises. The independent finite check above supplies all computational premises needed by the reviewed edit proof.

## Scope and remaining work

The positive result covers these paper proofs and the independently checked finite Brown facts. It neither supplies Lean declarations/build evidence nor accepts prior claims about formal verification. It leaves H5⇒N15 imported for the conditional corollary; the four-row lemma itself is self-contained. It establishes neither H5 as a whole nor n59 nonexistence, neither any r≥8 extension exclusion nor the exact value N(8,2). The audited elementary endpoints imply only `57≤N(8,2)≤63`.

Per task instructions, output is limited to these compact Markdown/JSON review artifacts; HTML rendering is disabled, and no TeX/PDF or wiki mutation was performed.
