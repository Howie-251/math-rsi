# DD mathematical extraction for the MathRSI evolution intake

**Coverage status: preliminary mechanism extraction, not a whole-archive audit.** The subsequent user clarification requires all unique source content to be read by family. The truthful per-file continuation map is [late/READ_LEDGER.tsv](late/READ_LEDGER.tsv); broader findings and remaining unread scope are in [late/SOURCE_AUDIT_LATE.md](late/SOURCE_AUDIT_LATE.md). All461 trajectory metadata rows are mapped, but metadata parsing is not primary-proof reading. Do not create final skills on the assumption that this first seven-mechanism selection is exhaustive.

This is a source-grounded design input, not a resumed degree–diameter research run. The source root, abbreviated **A** below, is /Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff. All research/, formal/, constructors/ and guide/ paths in this document are relative to A. The destination is MathRSI; historical budgets, owner releases and run states in A do not authorize new work.

The extraction checked the actual proofs and representative implementation, rather than treating guide/02_RESEARCH_TRAJECTORIES.md as mathematical evidence. Its seven central mechanisms are: current-graph retained-edge extension; affine route coverage and its field obstruction; release of global parameter sharing; frozen full-neighborhood cloning with controller load compression; opposite-GQ spread filling and ovoid packing; diagonal reallocation followed by frozen-role replication; and joint-parameter conflict/coupled-capacity diagnosis. These suffice for a useful initial DD plugin without copying every historical experiment.

No search, graph production, solver or Lean build was launched. The original extraction executed one cheap, read-only replay: constructors/early_d5/verify_covers.py, without --output. It returned PASS_ALL_SELECTED_CURRENT_GRAPH_COVERS, 103 extension checks, 1.593565 local CPU seconds. It inherited the original source D5 bounds and did not run all-source BFS. The continuation additionally ran a readonly exact Mizuno dual receipt check (0.008125 CPU; missing LP_INPUT reconstructed in memory from present MODEL) and constructor integer-data structural parsing (0.116239 CPU; no distance check). These are detailed in late/SOURCE_AUDIT_LATE.md with exact limits and missing dependencies. Other execution costs below are historical evidence.

## 1. The domain contract to carry into a DD plugin

A degree–diameter construction problem asks for a finite simple undirected graph G with |V(G)|=n, maximum degree at most d, and diameter at most D. A valid n-vertex graph proves N(d,D)≥n. It is not an upper bound or an optimality proof. Exact diameter needs a lower argument as well: for example n greater than the degree-d Moore bound for diameter D−1, a literal pair without a shorter path, or a distance-preserving source embedding.

The plugin should keep four different objects explicit.

1. The actual graph, including labels, field arithmetic, inverse-edge convention and edge format.
2. A construction family, including the parameters that are shared globally and those allowed to depend on an edge or vertex.
3. A certificate domain: a sufficient route/rank/coverage test can be narrower than the full graph family.
4. The public comparison: a graph can remain valid after a newly located source destroys its claimed record advantage.

Actual retained-edge inheritance is unusually valuable here. If every accepted source edge survives, old–old distance bounds survive without rerunning old roots. When edges are removed, this implication disappears; checking new roots alone is insufficient. Each invocation should state which pair classes are covered by inherited source walks, new-root checks, symbolic route proofs and literal binding. There is no single unqualified “verifier passed” result.

The general walk definitions are in formal/DegreeDiameter/Portfolio/SingleExtension.lean. Its old introductory comment is a historical stage snapshot; the definitions and theorem hypotheses are the reusable content. The formal objects are formula graphs. The archive does not claim a kernel-verified parser of the text edge files.

## 2. Mechanism I — retained edges turn a new-point problem into a current-radius cover

### Precise lemma and caller

Let G be a simple graph with diameter at most D. Add a new vertex z adjacent exactly to S⊆V(G), preserving every edge of G. If every old vertex is within G-distance r of some pin in S, then the extended graph has diameter at most max(D,r+1). For a degree cap d, separately require |S|≤d and deg_G(s)<d for each s∈S. This is exactly the generic theorem singleVertexExtension_diameter; the degree obligation is not hidden in its distance statement.

Proof: old–old walks embed unchanged; a new–old walk is the new edge z–s followed by the supplied pin-to-target walk; the reverse handles old–new. For an iterative D5 construction use r=4 **in the whole current graph before insertion**, including all earlier new vertices.

Actual callers include the 37629→37630→37631 degree-11 sequence and all 103 packaged D5 additions. The two final degree-11 additions use ten mandatory Q-line pins plus one anchor:

- for new label 37629: 947,24390,25310,26311,26519,27439,28431,28855,29775,30779,37123;
- for new label 37630: 8261,31641,31791,31850,31924,32071,32135,32172,32315,32372,37345.

These labels are the neighbor sets for graphs of order 37630 and 37631, respectively. All eleven pins had actual pre-insertion degree at most ten and their actual closed R4 union covered the current graph. The independent strongest checkpoint later checked all 37631 roots. The producer report itself predates that independent checkpoint; the plugin must consume the later receipt rather than copy its old “pending” sentence.

### Exact cache update, and why a stale cache can only be used with care

Suppose the current G gains z on S. For an existing old anchor a put k=d_G(a,S). A newly shortened simple a-to-old-target path through z has length k+2+d_G(S,target). Thus its newly available old targets within R4 are precisely those in R_(2−k)^G(S), when k≤2, in union with the old R4_G(a). Also z enters R4(a) iff k≤3. Finally,

    R4_(G+z)(z) = {z} ∪ R3_G(S).

The distances and the balls on the right are in the actual G, which may already contain previous additions. A shortest path uses z only once. This proves the update, rather than assuming that adding a vertex cannot affect old balls. The implementation removed saturated anchors and separately directly checked every accepted pin union in the current adjacency. Positives therefore did not depend solely on the cache.

### Failure → corrected action

On the 37628-point source, 2504 vertices had spare degree, total spare capacity 3316. Eight fixed starting profiles were each completed to **eleven** pins, followed by a full coordinate-replacement pass. The best missed 115 old targets, confirmed by independent multi-source R4. This excludes those eight starts plus that local pass; it does not exclude all eleven-pin covers. Preparing R4 took about 0.310 CPU s; the profile body about 1.019 CPU s; the fixed scoring batch made 419352 scores.

The productive change was to derive mandatory geometric pins covering the old core, then use exact small anchor completion for the residual. It was not an arbitrary increase in random restarts. In the later frozen twenty-entry degree-11 follow-up, two succeeded and eighteen had no one-anchor completion on their **then-current** bases. Later additions can change that failure, so those eighteen are not a theorem about the final base. That bounded follow-up cost 0.513024 CPU s.

### Files and executable behavior

- Proof/caching: research/ddp/more_graphs_20261027/h9_d11_followups/REPORT.md.
- Original failed scope: research/ddp/breadth_20261027_wave4/record37628_single_extension/REPORT.md and independent_cover_check.json.
- General theorem: formal/DegreeDiameter/Portfolio/SingleExtension.lean.
- Self-contained actual inputs/checker: constructors/early_d5/families.json, bases/degree11.adjlist.txt.gz, bases/degree12.adjlist.txt.gz, bases/degree13.adjlist.txt.gz and verify_covers.py.

The packaged checker reads the compressed labeled adjacency lists, rejects loops/duplicate neighbors/asymmetry, verifies n,m, checks exact ordered pre-insertion degrees and source_n/source_m, performs depth-four multi-source BFS, then mutates the local adjacency only after success. It is a useful executable example of consuming a construction recipe back into an inductive proof.

## 3. Mechanism II — affine lifts need both full-rank routes and adjacent pencils

### Precise positive interface

Let C be a simple s-regular controller with labeled ports and actual reverse-port pairs. Let V=F_q³. Fix nonzero port directions L_p. On each directed controller edge e:u→v with source port p and reverse port r choose T_e∈GL₃(F_q), with T_reverse=T_e⁻¹ and T_e L_p a nonzero multiple of L_r. Define neighbors by

    (u,x) ~ (v,T_e x+t L_r),  t∈F_q.

These conditions give a simple undirected sq-regular graph on |C|q³ vertices. The inverse condition is a relation on the actual reverse dart, including the two ends of a self-inverse matching port; it need not imply a globally shared involutory matrix.

For a nonbacktracking three-edge controller word a→u→v→b with middle dart e, incoming reverse direction L_i and outgoing direction L_j, applying the inverse of the final chart reduces the three noise columns to

    [T_e L_i | L_r | L_j].

If this matrix has rank three, the three independent noise coefficients cover every coordinate of the endpoint fiber for **any** starting coordinate; the deterministic affine part only translates the image. To use this as a D3 proof, bind a good word to every required ordered controller pair.

Adjacent fibers can instead be covered by backtrack pencils. Before and after e, their attainable affine planes have common center T_e x and common line span(L_r):

    span(T_e L_i,L_r), i≠p;    span(L_r,L_j), j≠r.

If their quotient directions exhaust PG(1,q), their union is all F_q³. These two route families must use the same actual matrices and inverse pairing. Proving them separately with incompatible parameters does not give a graph.

Actual caller: C30/F5 yields 3750 vertices, degree 20, 37500 edges. Its same/nonadjacent controller pairs have good rank-three words; its adjacent pencils consist of six distinct planes, of union size 5+6(25−5)=125. All 900 controller pairs are covered. The full 3750-root independent check and later formula-graph Lean are distinct additional receipts.

### Strong field obstruction, not just failure of a sufficient certificate

Assume four directions form a projective frame: any three are independent. For a dart e let A_e and B_e be the two triples of quotient directions above, and k_e=|A_e∩B_e|. Each triple has three distinct points. The nine central turns have exactly k_e rank-two failures. The pencil has 6−k_e distinct planes and exact union size

    q+(6−k_e)(q²−q).

All turns full rank requires k_e=0. Full pencil coverage requires 6−k_e=q+1. Together these certificate requirements force q=5.

For a controller edge in no triangle and no four-cycle, there are no extra nonbacktracking ≤3 routes to that adjacent fiber. Thus the pencil is the **entire** actual short-route image. When q>5,

    |R≤3(u,x;v)| ≤ 6q²−5q < q³,
    missing ≥ q(q−1)(q−5).

This excludes D3 in this fixed four-port straight-line family even if T_e is chosen separately on every edge. Inverse-compatible constant translations only shift the common pencil center and do not fix it. The saved C30 has thirty such undirected external edges. The binding check classified all 900 ordered controller pairs and all 2550 words of lengths zero to three.

This does **not** exclude q=2,3,4 graphs, multiple rank-deficient image unions, controllers with additional short routes, more ports, other dimensions, or nonlinear/nonfull fibers. At smaller q the all-turn-rank certificate can fail while a different collection of actual routes succeeds.

### Concrete refutation and cost

Embed the F5 matrices into F25=F5[α]/(α²−2). Every inverse identity and all 36 nonzero turn determinants survive. Yet from (controller 0,zero) the target (controller 20,(0,1,α)) is absent from all six actual planes. Their normalized normals are

    (0,1,3), (0,1,2), (0,1,1), (0,0,1), (0,1,0), (0,1,4).

Their dot products are 1+3α,1+2α,1+α,α,1,1+4α, all nonzero. The fiber coverage is only 3625/15625, with 12000 missing. This was a point test, not a BFS on the prospective 468750-vertex graph.

The route binding used 0.039213342 CPU s and the single F25 point check 0.000116998 CPU s. The corrected action is to change port count or controller short-route resources before producing a large graph. “The field embedding preserves rank” is specifically an insufficient prediction.

### Files

- research/ddp/two_successful_methods_20261101/affine_field_conditions/DERIVATION_PACKAGE.md, check_once.py, check_F25_counterexample.py, ALL_CONTROLLER_ROUTE_CLASSES.json, F25_COUNTEREXAMPLE.json.
- The literal F5 source: research/ddp/refresh_20261029/f5_full_d20_D3/PARAMETERS.json and generate.py; independent record INDEPENDENT_VALIDATION.json.
- Its compact packaged generator and parameters also exist below constructors/late_graphs/materials/.

The inspected F25 code really computes the six normals from the saved matrices; it represents a+bα as a two-coordinate F5 pair and checks a nonzero dot product. It does not silently treat GF25 as arithmetic modulo 25.

## 4. Mechanism III — prove a shared-parameter failure, then release exactly that sharing

### Exact old domain and necessity proof

Fix the saved C60 controller, inverse ports (1,0,3,2,4), F4=F2[w]/(w²+w+1), and the five conic directions

    (0,0,1), (1,0,0), (1,1,1), (1,w,w+1), (1,w+1,w).

The old excluded family assigns one global invertible T_p to each port, with inverse-port matrices inverse to each other and T₄²=I. It uses all four scalar values along each target line. It does not restrict invisible longitudinal/shear entries.

Project onto the two-dimensional quotient by the central direction. All central rank tests depend only on a member of PGL(2,4), which has sixty elements. Ports 0/1 and 2/3 give sixty paired projectivities each. The self-inverse port admits sixteen projectivities that have involutory lifts; the square-root scaling argument in F4 makes this domain complete. Therefore 60×60×16=57600 combinations suffice.

Why does a failed rank certificate prove a graph-class NO here? At zero starting coordinate, all route images are linear subspaces through zero. For each of the 3300 same/nonadjacent ordered pairs, the actual controller word count bounds the union of all rank-at-most-two images by at most 1+4(16−1)=61<64. The self-layer case uses five backtrack lines plus at most three deficient NB3 images, with the same bound. Thus some rank-three NB3 is **necessary** for each pair in this pure-linear fixed-controller family.

The complete enumeration found six combinations passing the forced-cell gate and zero covering all 3300 rank requirements. Ports 2/3 lie on triangles, so they have an extra NB2 route; the proof does not falsely call every adjacent edge a pure pencil edge. The rank-only NO already suffices.

### New freedom and actual successful caller

The successful family keeps the same field, directions and controller but chooses a projectivity independently for each of its 150 undirected edges. A chosen orientation u<v gets

    T_(u→v)=H_r⁻¹ diag(1,Q) H_p;

the reverse dart receives its actual inverse. Port 4 is a matching: its two endpoints may use T and T⁻¹ instead of one global involution. Each edge has forty-eight full-pencil projectivities among all sixty PGL possibilities. SAT enforces one per edge and all 3300 rank-route requirements simultaneously.

The saved solution yields 3840 vertices, degree 20, 38400 edges. Every one of the 300 darts exhausts the five quotient directions for an adjacent pencil, covering 4+5(16−4)=64 coordinates; every required nonadjacent/self pair has a literal rank-three word. The actual parameters, not solver status, constitute the positive witness.

The inspected run_once.py enumerates 7200 selectors, constructs the pair clauses, and after the single SAT call re-evaluates the CNF assignment and every reverse, direction, pencil and route condition before writing the parameters. The independent literal checker later checked all 3840 roots, zero exceptions. Formula-graph Lean later completed; a fresh plugin import does not rerun that build or confer a Lean theorem on another parameter choice.

### Scope/cost correction

The old 57600-domain exclusion cost 0.084363529 CPU s. A prior normalization bug chose “first entry” instead of “first nonzero entry” and evaluated zero combinations; its unrecorded CPU must not be presented as zero. The successful edge-dependent preparation/search/production scope used 1.609514885 CPU s, including 0.233523 solver CPU; the all-root independent check used 0.087418572 CPU s. Later kernel verification was much more expensive: the saved Rows01–59 finite batch alone used about 2020.31 CPU s.

The failure should trigger “release global sharing while keeping actual inverses and check the joint model,” not “the old proof was wrong,” “F4 is impossible,” or “generate another global matrix sample.”

### Files

- research/ddp/two_successful_methods_20261101/f4_c60_global_projective/REPORT.md and check_once.py.
- research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/PROOF.md, run_once.py, PARAMETERS.json, MODEL_CODE.md, EXACT_CERTIFICATE_CONTROLLER_TRACE.json and independent_acceptance/SUMMARY.json.
- Positive replay: constructors/late_graphs/original_wrappers/two_methods.py and materials/research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/PARAMETERS.json.

Archive portability issue: the historical proof names ROUTE_CERTIFICATE.json and PAIR_COVERAGE.json, but neither exists in the supplied top-level research directory. The positive parameters, original synthesis source and full-root receipt do exist. A plugin must reconstruct/check the route witnesses from the parameters, or carry an actual regenerated certificate; it must not publish dead links as if the certificate files were present. The controller trace is not a substitute for all positive rank witnesses.

## 5. Mechanism IV — frozen fullN clones, exact loads and transversal plane compression

### General theorem, including non-D2 preservation

Let G have no isolated vertices and diameter at most D with D≥3. Let J index new vertices and center:J→V(G), allowing repeated centers. Keep G induced on the old vertices, give j the exact **original** open neighborhood N_G(center(j)), and add no new–new edges. Then the graph still has diameter at most D. For finite graphs,

    deg_new(j)=deg_G(center(j)),
    deg_old(v)=deg_G(v)+load(v),
    load(v)=#{j : G.Adj(v,center(j))}.

Hence deg_G≤δ and load≤k imply maximum degree≤δ+k.

The edge-preserving collapse fixing old vertices and mapping every clone to its center is a graph homomorphism. Together with the old-vertex inclusion it proves every old–old walk bound is equivalent before/after cloning. A source non-D2 witness therefore survives without a new large non-D2 search.

Proof cases matter. Same-center clones use a common old neighbor in two steps. Source-center distance two or three permits endpoint replacement. Adjacent centers c,d require the three-walk clone(c)–d–c–clone(d), not a nonexistent clone–clone edge. Thus center independence is unnecessary. The actual generic source code formal/DegreeDiameter/Portfolio/FullNeighborhoodClones.lean includes these cases in diameterAtMost, old_walk_bound_iff, not_diameterAtMost, degree_old, degree_new and degree_le.

### Exact planar load compression

For an affine source with direction lines L_p and compatible charts, choose a hyperplane P=ker(n) transverse to every L_p. For each controller a select r_a copies of the complete P-block. Each selected center gets its complete original neighborhood, not only one port.

For a dart a→b, T(P) is complementary to the target direction line. Thus the |P| parallel q-point neighbor lines partition that whole q³ target fiber. Each selected controller block adds exactly r_a to every target point, so the full old-vertex load problem is exactly

    load_b=Σ_(a∈N_C(b)) r_a≤k.

The compression is justified by a partition, not by averaging. The final clone count is q²Σr_a; the degree constraint is now one per controller.

Actual F5 caller: normal (1,1,1), q²=25, thirty controller variables. With cap21, a complete 243-node branch-and-bound found maximum Σr=6 for this block rule, giving 150 clones and n3900. With cap22, the saved vector has Σr=15 and every controller load two, yielding 375 clones and n4125. It reaches the full-source slot bound 20t≤3750·2, so 375 is optimal **within the fixed full-original-neighborhood clone rule**, not N(22,3).

Actual F4 caller: normal (1,1,w), dot products (w,1,w,w,1), q²=16. All 300 darts/4800 neighbor lines were bound to the literal 3840 source. Saved feasible controller loads Σr=9 and 22 give n3984 and n4192 at caps21/22; adding the two actual load vectors yields Σr=31 and n4336 at cap23, with multiplicities retained. The simple counting bounds are Σr≤12k. HiGHS's “optimal” status alone was not used to turn 9 or 22 into independently proved maxima; the documented mathematical intervals remain [9,12] and [22,24].

### Frozen versus current is a mathematical distinction

The production sequence may update current adjacency for degree and radius checks, but the pin lists must already have been materialized from G. If two selected centers are adjacent, after the first clone is added the second center's current neighborhood contains a new clone. Reading that as fullN changes the defined family, introduces new–new edges and invalidates the old load formula. Repeated centers must likewise produce different new labels with the same frozen tuple; deduplicating them loses the intended multiplicity.

The q4 ovoid example in the next mechanism has 136 actual adjacent center pairs, making this a real reachable issue. The safe implementation serializes IMMUTABLE_SOURCE_PINS.json before constructing mutable current adjacency. The packaged two_methods.py similarly constructs adjacency from the old source only and reads every owner row from that fixed array; it does not append new neighbors to that array.

### Files/costs

- research/ddp/two_successful_methods_20261101/retained_edge_transfer/PROOF.md.
- research/ddp/two_successful_methods_20261101/retained_edge_transfer/f4_c60_plane_blocks/PROOF.md, SEARCH_k1.json, SEARCH_k2.json, LITERAL_PLANE_BINDING.json.
- formal/DegreeDiameter/Portfolio/FullNeighborhoodClones.lean; F4PlaneBlockClonesDefinitions.lean, F4PlaneBlockClonesPlane.lean, F4PlaneBlockClonesLoad.lean and F4PlaneBlockClonesFamily.lean show the actual formula caller and load injection.
- Packaged saved RECIPE_d21.json/RECIPE_d22.json and the cap23 recipe are under constructors/late_graphs/materials/.

F5 production for both endpoints used 0.399614746 CPU s; independent validation 0.342881714 CPU s. The latter checks all 150/375 new roots plus all retained source edges and inherits the accepted all-3750-root source result. It is complete pair coverage without pretending to rerun old roots. F4 block production/search used 1.589214495 CPU s. Neither cost measures discovering the source or its Lean development.

## 6. Mechanism V — opposite-GQ spread fill followed by ovoid×spread packing

### General geometric interface and source proof

Take an actual generalized quadrangle with point set P, line set L, incidence, and the unique projection property for a nonincident point/line pair. The opposite-product graph U has vertices (p,l)∈P×L, with distinct (p,l),(q,m) adjacent iff p∈m and q∈l.

For balanced GQ(q,q), raw degree is (q+1)². At a flag p∈l the raw relation includes its own vertex, so the loopless degree is (q+1)²−1; nonflags have degree (q+1)². This one-slot deficit at flags is the fill resource.

The source D≤3 proof is explicit. For endpoints (p,l),(q,m), choose a∈l collinear with q and b∈m collinear with p. Choose k through a,q and n through b,p, using any through-point line in coincidence cases. Then

    (p,l), (a,n), (b,k), (q,m)

satisfies cross incidence. Suppress consecutive equal vertices to obtain a genuine walk. This last conversion matters because raw incidence formulas can contain self-entries.

Let a spread partition P into lines L_j. Add filler f_j on all flags (a,b) with a∈L_j and a∈b. These pin sets partition all flags; in the balanced case each has (q+1)² pins. Projection shows a pin at distance≤2 from any old target. Between distinct fillers choose collinear a∈L_i,c∈L_j, with joining line b; f_i,(a,b),(c,b),f_j is a three-walk. Thus old edges plus the new filler pins yield a (q+1)²-regular D3 graph H.

### Actual q4 caller and literal premises

For q4, field arithmetic is F2[w]/(w²+w+1), not modulo four. The saved GF16 trace construction generates 85 points and 85 totally isotropic five-point lines; the code checks all 6800 nonincident projection pairs. A Desarguesian spread consists of seventeen lines. U has 7225 vertices, 425 degree24 flags, 6800 degree25 nonflags and 90100 edges. The spread fill gives H with 7242 vertices, 90525 edges, all degree25.

The q4 proof includes the field tables, exact projective normalization, point/line labels, spread order and owner indices. Those are part of a usable caller; “take the standard GQ” without any binding would not identify its literal edge table.

### Ovoid product packing and the self/bonus correction

Let O meet every line exactly once. Product centers O×spread have raw cross-incidence neighborhoods

    R_(p,l) = {(q,m):q∈l and p∈m}.

They partition all P×L: for any (q,m), choose its unique spread owner l and m's unique ovoid point p. At the q²+1 diagonal flag centers, the raw set contains the center itself. In the **filled loopless H**, the actual full neighborhood substitutes the corresponding filler:

    N_H(c)=(R_c minus {c}) ∪ {f_owner(c)}.

The owners are all different, so disjointness survives. This is the connection between the clean geometric partition and actual simple-graph fullN.

The explicit q4 ovoid is the seventeen projective zeros of

    Q(u0,u1,v0,v1)=u0²+u0*v1+w*v1²+u1*(v0+v1).

Its polar form is the actual symplectic B. Setting x=u0,y=v1,r=u1,s=v0+v1 writes Q=x²+xy+wy²+rs. The binary form is anisotropic; the direct count gives 51 nonzero zeros and hence seventeen projective points. A two-dimensional totally singular subspace would contain an r=0 vector, forcing x=y=0, and polar orthogonality then forces the entire subspace onto one axis, contradiction. Thus no two zero points are collinear; counting 17·5=85 incidences proves every line meets O once.

The 289 actual full 25-neighborhoods are disjoint, cover 7225 of 7242 vertices and have maximum old load one. The centers themselves induce 136 disjoint edges and seventeen isolates. Frozen fullN cloning therefore yields n7531, m97750, cap26; 25t≤7242 gives t≤289, attained. This is fixed-source/fullN optimality only.

### Transfer and costs

The same source/fill interface has actual q3,5 order6160 and balanced q7 order160050 callers, with different incidence inputs. For q7, independent acceptance reconstructed all 400 points/400 lines, checked all 160000 projection premises and bound all 5121600 edges, plus BFS from fifty new roots. It did not perform all-160050-root BFS.

The q4 geometry/ovoid precheck cost 0.161736872 CPU s; producing7531 cost 0.787637899 CPU s. Scaling to q8 first used a small finite-geometry pilot, rather than generating a large graph on speculation. The q8 sources' later full finite Lean work cost 8413.702687 CPU s. This is direct evidence to prefer small premise probes and symbolic route reuse, not a claim of a universal speed factor.

### Files and usable split

- research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq44_spread25/PROOF.md, PARAMETERS.json, FIELD_TABLES.json, prepare_geometry.py.
- Its ovoid_product26/PROOF.md, precheck_once.py, generate_once.py, ORDERED_CENTERS.json, IMMUTABLE_SOURCE_PINS.json, CENTERS_INDUCED_CHECK.json and independent_acceptance/SUMMARY.json.
- constructors/late_graphs/original_wrappers/gq_spread.py and the corresponding materials/ geometry and immutable-pin JSON are the compact deterministic replay inputs.

The generic geometry is classical and the spread/Delorme framework has prior sources. The plugin can teach the explicit caller and its corrections without claiming to have invented the framework.

## 7. Mechanism VI — change the load-bearing adjacency, then freeze the new source

### A useful genuine obstruction

The accepted7531 graph has L of306 degree25 vertices and H of7225 saturated degree26 vertices. Every low vertex has twenty-five neighbors in H. Equal neighborhoods partition L into289 classes:272 singletons and seventeen doubletons. The corresponding twenty-five-point H-neighborhoods partition H.

If one new vertex x is added while preserving every7531 edge at cap26, its neighbors must lie in L. Each chosen low pin spends its only spare edge on x; its H neighbors are already saturated. Any x-to-low path of length≤3 can reach only the low class of its first pin. Thus x needs a pin in each of289 classes, contradicting degree≤26. The argument permits any additional old–old edges that respect the retained-edge/cap hypotheses: none can touch a chosen pin or a saturated H vertex.

This excludes exactly a one-point retained-edge augmentation of this fixed graph. It is not N(26,3)≤7531, does not exclude simultaneous cooperative additions, and does not apply once old clone edges may be deleted. The literal structural diagnostic cost 0.086647286 CPU s without BFS.

### Corrected adjacency and actual caller

Preserve every edge of the earlier filled source H7242, rather than every edge of7531. Give each clone the open neighborhood in the **unfilled** U7225. At seventeen diagonal centers, delete the clone's own-filler edge. Add one hub joined to all seventeen fillers. The new graph has7532 vertices and the same97750 edges, with degree histogram

    degree17:1, degree24:17, degree25:289, degree26:7225.

Old H paths survive. U/clone pairs follow the fullN argument inside U. For the omitted own-filler adjacency, choose another line m through p: filler_j–(p,m)–clone(p,L_j) is a two-walk. A different filler cannot force the excluded last-edge case because spread pin sets are disjoint. The hub reaches a flag in two steps through its owner filler and any nonflag or clone in three through a suitable flag. These are complete pair cases; “only17 edge deletions” alone proves nothing.

The q8 version deletes65 diagonal clone/filler edges, adds a hub on65 fillers, keeps all13862745 H edges and gives346516 vertices/14204970 edges. Fresh acceptance bound all4225 raw-U clone neighborhoods and the exact edge delta; it BFS-checked only65 changed diagonal roots plus the hub. The unchanged4160 off-diagonal roots and old roots use literal binding plus the U/H-interior route proof. This is an explicit valid incremental scope, not all-346516-root BFS.

### Freeze G1 roles, rather than reusing an outdated source identity

Now treat G1=346516 as the source. Its4225 clones plus hub are4226 first roles, independent, with pairwise disjoint **complete G1 neighborhoods** in old H. Their union has342225 vertices; the other65 old H vertices remain outside. Copy each first role r times using those frozen rows. Added vertices number4226r, added edges342225r, and cap is82+r. New-role degrees are their fixed source degrees65,80 or81.

At any within-block prefix every old vertex has at most one role owner, so after b complete copy blocks its load is b; projection of the new adjacency index to its copy coordinate proves load≤r. General fullN walks and the collapse-to-G1 transfer D3 and the non-D2 witness. No future clone is needed as an interior. The collapse target is G1, not H or U. Existing role-copy proofs instantiate r=8/12 and other named endpoints; they do not claim every possible parameter was generated.

The corrected strategy is to state exactly which old adjacency invariant blocks progress, change that invariant deliberately, reprove only the affected pair classes and then freeze the new accepted source for the next rule. It is neither “ignore the obstruction” nor “rerun everything.”

### Files/costs

- q4 obstruction: research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq44_spread25/ovoid_product26/same_cap_single_extension_gate/PROOF.md.
- q4 successful replacement: sibling diagonal_fill_reallocation/PROOF_DRAFT.md, produce.py, EDGE_DELTA.json and independent_acceptance/NOTE.md.
- q8 analogue: research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/balanced_full_ovoid_copy82/diagonal_fill_reallocation/PROOF_DRAFT.md.
- Its multiplicity9_degree90/PROOF.md states the general frozen-role prefix proof and actual r8/r12 instances.

q4 replacement production cost0.195131966 CPU s; q8 replacement production cost0.940117171 CPU s including compilation/preparation. These are sparse-delta production scopes, not total discovery or formalization costs. Generic FullNeighborhoodClones is genuinely reused; the q8 literal bridge and its new source premises are separate obligations.

## 8. Mechanism VII — distinguish route capacity, individual realizability and joint compatibility

### A complete shared-parameter conflict

Fix the group C8 acting by multiplication by3 on Z32, RIGHT product

    (a,b)*(c,d)=(a+c,b*3^c+d),

and four positive generator phases1,2,3,4 with four normals b_i∈Z32. Use the true inverse (-a,−3^(−a)b). Empty words plus inverse-code nonbacktracking words of lengths1,2,3 total457. The route recurrence is L'=3^a L+d over Z32, not XOR.

All-even normals disconnect the graph. A common odd-unit automorphism uniquely normalizes the first odd normal to1, giving61440 cases. The parity relation b_i≡phase_i*b0 mod2 accounts for4096 disconnected representatives. Otherwise an odd pure translation together with the phase-one generator gives full connectivity. The complete connected domain is therefore57344, including3072 actual degree-seven degenerations where the phase-four generator equals its inverse; the family was not silently narrowed to exactly degree eight.

Each phase has46–63 different coefficient forms, so all individual formal-capacity gates pass. Every phase separately has actual parameter tuples covering all32 normal values. But exhaustive actual endpoint evaluation found no common tuple covering all eight phases. A read-only compatibility pass found minimum inconsistent subset{0,2}:

- phase0 alone has320 witnesses; b=[1,1,2,23] gives coverages [32,31,31,29,26,29,31,31];
- phase2 alone has1344 witnesses; b=[1,0,2,10] gives [27,29,32,32,29,32,32,29];
- phase0 and phase2 together have zero witnesses.

Those proper-subset witnesses establish that the failure is shared compatibility, not absence of enough routes or an impossible individual phase. The C++ source evaluates all eight actual masks for each visited tuple; it does not early-stop after the first missing phase, and complete=true requires the exact61440/4096/57344 counts. Named inverse letters may alias in degree-seven cases, but every actual ≤3 walk can be reduced to the named words, so the union still represents actual R3.

The NO applies only to this group/action, phases and four-normal Cayley rule, maximum degree≤8. It says nothing about other actions, phases, non-Cayley graphs or general N(8,3). The complete main batch cost2.080238239 CPU s; compatibility postprocessing0.144041528 CPU s plus an explicit0.05 preparation charge, case total2.274279767. No candidate graph or BFS was needed.

### A second correction: separate maxima are not a coupled upper bound

On the fixed253-point8-regular Comellas–Mitjana source, left translations normalize the first cut to one of four inverse-pair types; no inter-type edge transitivity is assumed. A source cache supplies27 true unique three-geodesic obligations per first cut: nine with it first, nine middle, nine last. A star pin must hit the witness endpoints for the middle case, or a closed B1 of the far endpoint for the first/last case. A subset of true witnesses suffices for a negative proof.

Every other eligible cut hits at most six obligations. Three cuts give18<27, excluding the four-disjoint-cut/eight-star family. For five matching cuts plus one genuine old nonedge repair, separate maxima initially gave a loose35≥27. That **refutes the proposed capacity-only exclusion**; it is not a positive graph or evidence of simultaneous realizability.

The corrected joint model binds repair{a,b} to its two actual half-cut partners a'∈N(a),b'∈N(b), all six labels distinct. Its relaxed mask is repairMask(a,b) OR V(a') OR V(b'). Complete scanning of all30378 old nonedges and1910136 legal half choices per first type found maximum twelve. The remaining two full cuts add at most6+6, so total24<27. This closes the exact five-matching-cut/one-nonedge-repair/eight-star rule.

The proof also derives a broader pure-deletion corollary: for any≤5 deleted old edges, overlapping allowed, a degree-legal new vertex may only use freed endpoints; all freed endpoints from four other cuts hit at most24 obligations while the first-cut endpoints hit none. Thus no such one-point pure-deletion/new-old-edge augmentation works. Multiple old repairs, overlapping repair/star roles or different sources are outside the repair theorem. The full numerical case cost3.686201072 CPU s. No graph/BFS stage was reached.

This is a useful domain search order: formal capacity → actual per-target image → common parameter compatibility → exact literal graph. A necessary obstruction may stop the pipeline early. When a relaxation passes, progress to a stronger joint model, not directly to a success claim.

### Files, and an important missing artifact

- research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/global_c8_z32_action3_256/NOTE.md, gate.cpp, run_once.py, RESULT.json, compatibility_once.py and COMPATIBILITY.json.
- research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/source253_fourcut_star254_gate/FINAL_PROOF.md, PAPER_WITNESS_GATE.md, COUPLED_RESULT.json and the actual coupled-scan source.

The original global256 ALL_NORMALIZED_CONNECTED_PARAMETERS.tsv is **not included** in A, despite its historical link in NOTE.md. So compatibility_once.py cannot run directly against this archive alone. gate.cpp can regenerate the whole table cheaply into a scratch directory; the source proof plus saved aggregate COMPATIBILITY.json remains readable. A useful plugin must include either the table or the complete regeneration command and a fresh small compatibility consumer. It must not pretend that archive navigation equals executable self-containment.

## 9. What belongs in domain skills, and what merits a base change

The DD plugin should have a substantial front door explaining N(d,D), graph definitions, max-degree versus regularity, source families, route direction, Moore lower/exact-diameter arguments, public comparisons and evidence inheritance. Below it, three working domain skills are enough initially; splitting every lemma into a new skill would obscure the actual methods.

**dd-construct-and-transfer** should serve route-loop and prove. Given a fixed graph/family and target pair classes, it executes the appropriate mathematical reduction: retained-edge pin coverage; affine rank/pencil synthesis; frozen fullN load packing; GQ fill/ovoid or diagonal load rewrite. Its return includes the new theorem/proof or literal graph recipe, exact discharged conditions, any changed family hypothesis and next unresolved joint obligation. The derivations in §§2–7 should be included as actual domain references, with their explicit callers, not replaced by a two-page catalogue.

**dd-route-obstructions** should serve route-loop and local prove. Given a failed construction and actual route expressions, it asks which level failed: count, image collision, shared compatibility, old-path destruction or degree-owner capacity. It can return a restricted NO, an actual failed target, a minimum incompatible subset, or a weaker model that still passes. Its reference examples should include F25, global C60→edge C60, global256, CM253 and one cut-star old–old/new-root conflict. The result records precisely which condition was released next; it does not automatically launch that new family.

**dd-literal-acceptance** should serve verify. It reads the recipe, graph format, labels and inherited source evidence; checks actual simplicity/degrees/retained edges; checks exactly the uncovered pair classes by BFS or a complete literal route certificate; and returns what remains. It should include the immutable-pin/source-binding check and an example of a sparse edge delta. Embedded use returns to the owning verify obligation, not another final proof-checker loop.

Optional literature functionality can extend the same domain entry instead of a fourth thin skill. It needs known controller/geometry provenance and examples where public comparison changed the source: 51457 D5 was surpassed by a located88452 graph; the GF7 cubic22 partial ovoid was surpassed by a published33-point object. These are dated source corrections, not current public-record certificates.

The following are credible **cross-domain base deltas**, each tied to a concrete observable behavior rather than a new universal score or schema.

| Evidence | Base behavior to consider | Acceptance probe |
| --- | --- | --- |
| F4 global NO followed by edge-dependent SAT | On a failed route, distinguish an obstruction in the problem from one in shared family parameters; propose the smallest meaningful released condition | A new agent must preserve the old NO and state the new family correctly before trying it |
| global256 phase0/phase2 and CM25335→24 | When several obligations share one choice, test the common choice; separately achievable witnesses or separate maxima cannot be conjoined | Agent returns proper-subset witnesses or a joint bound, not eight independent “passes” |
| immutable fullN and evolving R4 | Identify the source/version relative to which a derived object is defined; mutation invalidation depends on its mathematics | Agent uses frozen pin rows but current distance balls, and explains why these differ |
| new roots plus old-edge preservation, q8 changed-root delta | Reuse unaffected evidence after proving literal inheritance and exhaustively partitioning the obligation | Agent covers every pair class without rerunning all source roots or silently omitting old–old pairs |
| field/growth premise pilot; old rule stopped on necessary NO | Run a cheap probe that can change the route before expensive production; stop a stronger test once the weaker necessary gate closes the current scope | Probe produces an actual counterexample/NO and the unused downstream search is not launched |
| dated public33 correction and cancelled degree24 candidate | Public comparison can cause cancellation or source replacement without invalidating the mathematical construction | Agent preserves validity and corrects only the comparison/next decision |
| fixed rule “optimal” versus full task | State optimum relative to the actual finite family; a solver result and a mathematical bound are different evidence | Agent distinguishes F5 exact375 clone optimum from F4 feasible22 and counting upper24 |

Existing base contracts already cover several of these ideas. Evolution should patch the precise missing decision or example, not duplicate the entire plugin into base, add a rigid state machine, or declare “RSI improved” from this retrospective extraction. DD-specific ranks, GQ geometry, clone routes and path-damage masks remain in the plugin.

## 10. Minimum primary-source/code set for a genuinely useful self-contained plugin

The archive is deliberately much larger than the useful minimum. Preserve source attribution and import the following coherent slices, not all461 records or47 Lean builds. A path in this section names an actual inspected file or a clearly marked data subtree; historical dead links are not promised as included artifacts.

### A. Small runnable core

1. constructors/early_d5/verify_covers.py, reproduce.py, family_generator.py, families.json and all three compressed bases. Include constructors/verification/D5_CURRENT_COVER_REPLAY.json and the strongest source/checkpoint receipts, since current-cover replay imports the original base distance bound.
2. constructors/late_graphs/rebuild.py, cases.csv and original_wrappers/two_methods.py, gq_spread.py. The unmodified rebuild dispatcher also names other wrappers, so either carry the whole small wrapper directory and materials tree as supplied, or explicitly trim and test its supported cases; do not delete dependencies and leave their cases listed.
3. For a minimal selected-case materials slice: F5 PARAMETERS.json/generate.py; F4 PARAMETERS.json/generate.py; RECIPE_d21/22 for F5 and F4 plus cap23 recipe; q4 GQ PARAMETERS.json; ovoid ORDERED_CENTERS.json/IMMUTABLE_SOURCE_PINS.json/PARAMETERS.json; diagonal delta PARAMETERS.json/produce.py. The materials tree already supplies this dependency order and avoids large prebuilt edge tables.
4. A checker for the selected small explicit graphs: preserve the literal checker source beside its acceptance receipt, or write a short standalone header-aware BFS checker with its precise scope. Rebuild alone does not verify diameter. The existing constructors/verification/3900_4125_check_literal_terminal_graphs.py has historical path assumptions and must not be advertised as relocatable unchanged.

This core can replay current-radius induction, affine F4 generation, frozen cloning, GQ filling and the q4 sparse delta on a normal Python installation. No solver or Lean is needed to replay saved parameters.

### B. Mathematical references required alongside the core

Carry the complete proof texts listed in §§2–8: generic retained extension/cache; affine_field_conditions/DERIVATION_PACKAGE.md; F4 global-domain REPORT.md and edge-projective PROOF.md; fullN PROOF.md and F4 plane PROOF.md; q4 GQ and ovoid PROOF.md; q4 obstruction and diagonal proof; global256 NOTE.md; CM253 FINAL_PROOF.md/PAPER_WITNESS_GATE.md. Include a short terminology/source map and dated public-comparison corrections. These are not interchangeable summaries: they supply the actual assumptions, case splits and negative-scope boundaries.

For optional formula-graph formalization, carry formal/DegreeDiameter/Portfolio/SingleExtension.lean and FullNeighborhoodClones.lean with their fixed project toolchain/manifest and actual imported definitions. A lone copied Lean file is useful as source reading, but is not a self-contained compilable project without dependencies. The present intake does not request copying or rebuilding all concrete formal instances.

### C. Tiny diagnostic replay slices

- F25: check_F25_counterexample.py plus literal F5 PARAMETERS.json; for the full controller binding also check_once.py and its cached controller_structure.json dependency.
- Global F4: f4_c60_global_projective/check_once.py, f7_c60_d35/PARAMETERS.json and f4_c60_forced_turn_gate/FORCED_TURNS.json. Its proof explains why these quotient representatives are complete. The script writes outputs beside itself, so execute only a scratch copy preserving these relative siblings.
- Shared phase conflict: global256 gate.cpp, NOTE.md, RESULT.json and COMPATIBILITY.json. The TSV is omitted from A; regenerate it from gate.cpp rather than claiming compatibility_once.py alone is self-contained.
- CM253 joint obstruction: the actual source recipe/cache, exact witness mask generator and coupled scan source must accompany any advertised executable replay. The proof text alone remains a valid readable conditional/finite-proof reference, but copying only FINAL_PROOF.md and COUPLED_RESULT.json is not a runnable checker.

For the first plugin release, F25/global256 plus the saved positive replay core provide enough genuine small execution. Do not block useful delivery on porting every CM253 or q8 historical driver. Mark those deeper cases as source-backed mathematical references until their full input closure is packaged and actually tested.

## 11. Cheap replay commands and exact claims

These are concrete commands derived from inspected argument handling. Only command1 was run in this intake. The others are proposed acceptance probes for the plugin author; they write new scratch outputs and must not be executed in the frozen research directories. They do not authorize the old Goal, public searching, new solver searches or Lean.

### Command 1 — actual read-only replay, already executed

From A:

~~~sh
python3 -B constructors/early_d5/verify_covers.py
~~~

Observed exit0; 103 checks; local CPU1.593565; inherited_source_D5=true; all-source_BFS=false. A future output report can be sent to a new path with --output, but the read-only form is enough for a cheap smoke probe.

### Command 2 — reproduce the saved F4 and clone graphs in a new workspace

~~~sh
scratch=$(mktemp -d /tmp/dd-plugin-replay.XXXXXX)
python3 -B constructors/late_graphs/rebuild.py --case d20_D3_n3840 --workspace "$scratch/source" --output "$scratch/g3840.edges"
python3 -B constructors/late_graphs/rebuild.py --case d22_D3_n4192 --workspace "$scratch/source" --output "$scratch/g4192.edges"
~~~

The first executes the saved literal finite-field formula. The second first reuses/rebuilds3840, then uses the fixed recipe. It invokes no SAT/MILP search. It can validate a future plugin's input closure and immutable owner-neighborhood emission, but these commands themselves do not establish diameter. Header format is n m followed by sorted unordered edges.

### Command 3 — reproduce the q4 ovoid and sparse-delta instance

~~~sh
scratch=$(mktemp -d /tmp/dd-gq-replay.XXXXXX)
python3 -B constructors/late_graphs/rebuild.py --case d26_D3_n7531 --workspace "$scratch/source" --output "$scratch/g7531.edges"
python3 -B constructors/late_graphs/rebuild.py --case d26_D3_n7532 --workspace "$scratch/source" --output "$scratch/g7532.edges"
~~~

The wrapper constructs the required H source from incidence inputs and uses saved frozen pins; the delta producer checks the exact seventeen deletions/additions. Compare edges and pin sets, then accept distance via the complete GQ/delta route proof or the fresh selected-root checker. There is no reason to start with the large q8 replicas for a plugin smoke test.

### Command 4 — rebuild the missing global256 endpoint table and inspect joint conflict

From A, using an existing C++17 compiler:

~~~sh
case_dir=research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/global_c8_z32_action3_256
scratch=$(mktemp -d /tmp/dd-conflict-replay.XXXXXX)
c++ -O2 -std=c++17 "$case_dir/gate.cpp" -o "$scratch/gate"
"$scratch/gate" "$scratch" 10
python3 -B - "$scratch" <<'PY'
import csv, itertools, json, sys
from pathlib import Path
p = Path(sys.argv[1])
native = json.loads((p / "NATIVE_RESULT.json").read_text())
assert native["connected_domain_complete"] is True
assert native["connected_parameters_checked"] == 57344
assert native["full_hit"] is False
frequency = [0] * 256
with (p / "ALL_NORMALIZED_CONNECTED_PARAMETERS.tsv").open() as f:
    for row in csv.DictReader(f, delimiter="\t"):
        mask = sum(1 << j for j in range(8) if int(row["cover"+str(j)]) == 32)
        frequency[mask] += 1
count = lambda mask: sum(n for m,n in enumerate(frequency) if m & mask == mask)
assert sum(frequency) == 57344
assert count(1) == 320 and count(4) == 1344 and count(5) == 0
for size in range(1,9):
    bad = [s for s in itertools.combinations(range(8),size)
           if count(sum(1 << j for j in s)) == 0]
    if bad:
        print({"smallest_incompatible_size":size, "sets":bad,
               "phase0_full":count(1), "phase2_full":count(4)})
        break
PY
~~~

The historical driver measured about2.08 total CPU seconds including its compilation/preparation scope; this command has not been timed here. Its native ten-second limit returns UNKNOWN if exhausted, and the Python assertion then refuses a NO. It creates the missing table in scratch; it does not mutate old RESULT.json or incorrectly combine a fresh run with historical timing. The compiled program writes a graph only on a full hit; the expected saved-domain outcome is complete NO. It is a finite family replay, not an unrestricted D3 search.

### Command 5 — a read-only F25 local counterexample probe

This form recomputes the six plane normals from the actual F5 parameters without the historical script's in-place JSON write:

~~~sh
python3 -B - <<'PY'
import json
from pathlib import Path
p = Path("research/ddp/refresh_20261029/f5_full_d20_D3/PARAMETERS.json")
P = json.loads(p.read_text()); T=P["matrices"][1]; L=P["directions"]
assert P["controller"][0][1] == 20 and P["inverse_ports"][1] == 0
def mv(A,x): return [sum(a*b for a,b in zip(r,x)) % 5 for r in A]
def normal(a,b):
    n=[(a[1]*b[2]-a[2]*b[1])%5,
       (a[2]*b[0]-a[0]*b[2])%5,
       (a[0]*b[1]-a[1]*b[0])%5]
    c=pow(next(x for x in n if x),-1,5)
    return tuple(c*x%5 for x in n)
ns=[normal(L[0],mv(T,L[i])) for i in range(4) if i!=1]
ns += [normal(L[0],L[j]) for j in range(4) if j!=0]
assert len(set(ns)) == 6 and all(n[0]==0 and (n[1],n[2])!=(0,0) for n in ns)
print({"target":"(controller20,(0,1,alpha))", "six_normals":ns,
       "all_dot_products_nonzero":True, "q25_missing_by_formula":12000})
PY
~~~

It proves that this target lies outside the six saved planes. To conclude actual unreachability, also use the controller short-word classification from §3. A local normal calculation alone does not prove that no other controller route exists.

## 12. Intake conclusion and unresolved implementation work

The strongest reusable DD contribution is a connected proof-and-execution chain: derive the actual route/owner/load object, test a cheap necessary gate, release only an identified family restriction, synthesize one common witness, bind it to literal labels, and reuse unaffected source evidence while checking every newly exposed pair class. The extracted mathematics provides real operations an agent can perform, not only research etiquette.

This document does not create the DD plugin or change base. The subsequent maintainer should select the small input closure above, author the three substantive domain skills, port only the advertised cheap diagnostics, and have an independent agent consume a real frozen-clone or shared-parameter task fragment. Primary acceptance questions are whether that agent uses the correct source neighborhood, common parameters, scope of NO and actual pair coverage. Formats and links are supporting checks.

Open archive gaps affecting that work are explicit: some named positive F4 certificate JSON and the global256 per-parameter TSV are absent; several historical standalone checkers have original absolute/path assumptions; big graph bodies are intentionally replaced by compact constructors. The existing reconstruction source resolves positive generation, and the complete global256 gate resolves its missing TSV. None of these facts upgrades historical paper/computational/Lean/public-comparison statuses or demonstrates an end-to-end MathRSI speedup.

## 13. Continuation: an additional cheap exact certificate replay

The deeper source audit adds several substantial mathematical interfaces beyond the initial seven, especially D2 helper-capacity/excess-dual/parity and exact old-edge rewiring. Their assumptions, real callers, evolution and missing inputs are in [late/SOURCE_AUDIT_LATE.md](late/SOURCE_AUDIT_LATE.md); [late/READING_MAP_BY_FAMILY.tsv](late/READING_MAP_BY_FAMILY.tsv) summarizes the actual reading ledger. These are authoring inputs, not a declaration that final plugin design or whole-project understanding is complete.

The saved Mizuno13 dual can be replayed without LP solver, graph generation or archive writes. The original `verify_exact.py` expects missing `LP_INPUT.json` and writes beside itself. This command instead reconstructs its365 declared inequality rows in memory from the present `MODEL.json`; its arithmetic is the one already checked in [late/MIZUNO_DUAL_CHEAP_REPLAY.json](late/MIZUNO_DUAL_CHEAP_REPLAY.json). It proves the dual's numerical implication after importing the geometric derivation of those model rows.

```bash
python3 -B - <<'PY'
from pathlib import Path
from fractions import Fraction
from collections import Counter
import json
D = Path('/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff/research/ddp/two_successful_methods_20261101/mizuno13_clone_interface/source_dependent_geometry/controller213_capacity_gate')
M = json.loads((D/'MODEL.json').read_text())
C = json.loads((D/'lp_exact_bound/SIMPLIFIED_DUAL_CERTIFICATE.json').read_text())
n = M['binary_variables']
assert n == M['controller_rows'] == 364
A = [[0]*n for _ in range(n)]
for i, row in enumerate(M['row_sparse_coefficients']):
    for j, coefficient in row:
        A[i][j] += coefficient
assert all(sum(row) == 5 for row in A)
assert all(sum(row[j] for row in A) == 5 for j in range(n))
assert all(sorted(v for v in row if v) == [1,1,1,2] for row in A)
assert Counter(M['source_cost']) == {5:203, 6:161}
A.append(M['source_cost'])
B = [3]*n + [M['cost_upper']]
assert B[-1] == 1092
Q = C['common_denominator']
Y = C['controller_and_cost_row_numerators']
Z = C['upper_bound_row_numerators']
assert Q > 0 and len(Y) == len(A) == len(B) == 365 and len(Z) == 364
assert all(isinstance(v, int) and v >= 0 for v in Y+Z)
columns = [sum(row[j]*y for row,y in zip(A,Y))+Z[j] for j in range(n)]
rhs = sum(b*y for b,y in zip(B,Y))+sum(Z)
assert columns == C['column_coefficient_numerators'] and min(columns) >= Q
assert rhs == C['RHS_numerator'] and rhs < 207*Q
assert Fraction(rhs,Q) == Fraction(C['exact_upper_bound'])
print({'columns':n, 'min_coefficient':min(columns), 'denominator':Q,
       'RHS':rhs, 'bound':str(Fraction(rhs,Q)), 'integer_blocks_at_most':206})
PY
```

Expected:364columns, minimum10001, denominator10000, RHS2061908, bound515477/2500, integer blocks≤206. This excludes the complete364-source affine full27-transversal block domain described in the proof, not nonlinear/partial blocks or general14-degree graphs. The original missing input remains documented rather than silently added to the source archive.
