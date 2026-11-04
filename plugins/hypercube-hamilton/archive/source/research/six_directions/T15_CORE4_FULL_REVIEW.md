# Complete T15 core4: fresh proof review

Verdict: **PASS**, relative to the stated imports. `review_independence: same-family`; `acceptance_status: provisional`. Reviewer route: GPT-6.1-sol / high, explicitly requested by caller, overriding the skill default. No production checker, main state, or dynamic coverage ledger was changed by this review.

Accepted theorem: for every arbitrary complete-graph matching on Q5 with exactly holes [0, 1, 2, 7, 11, 31], there is a simple cycle on Q5 minus [1, 2], containing every original matching edge and using only short new edges. The whole marked cube-automorphism orbit is included. This is one complete core, not complete T15, the eight-hole layer, or P6. Exact reviewed inputs and hashes are in the companion JSON.

## Proof obligations and dependency order

N14_4 plus marked Q4 tables imply the two-bridge construction. Restricted five-mode inverse blocking gives the exact B residual supersets for c=4,6,8 and empty residual sets for c=10,12. Independent small-spectrum enumeration covers c=2 outside its exact zero-spectrum B set. Four-bridge forests and their positive eleven-cycles cover each remaining full input, apart from explicitly listed direct positive residual certificates. At c=0, N14_4 gives the uniform A path; all exceptional B inputs times all A matchings have direct certificates. Every possible c is even and lies in {0,2,4,6,8,10,12}. No edge in this DAG imports a complete-core conclusion from a parent coverage ledger.

The N14_4 domain allows arbitrary same-parity and long original edges: translating the specified omitted hole to zero and permuting coordinates reduces the other hole to 3 or15. Fresh verification checks all 270270 positive certificates, distinct matching ranks, exact support, input-edge containment and shortness of all additional edges. The restricted R4 application uses retained bridge labels {3,5,15} for core4 or {6,10,15} for core24; every label is nonzero and avoids B holes 0,1. Thus the prior PASS_WITH_SCOPE_LIMITS hypothesis is discharged here. Fixed R4 input hashes and joint residual lists were rechecked; a missing blocker is never used as an impossibility certificate.

## Four bridges, isolated vertices and compression

Each of the18 bridge geometries has five marked omissions in B, namely 1 plus its four distinct bridge labels; zero remains the sole retained free vertex. For each table the full945 mate arrays have precisely the six required holes. Every positive record is a simple eleven-cycle on exactly the claimed support, includes the input matching, and has only short other edges. Fresh checking also exhausts degree completions for negative records, although construction soundness needs only positives. The36 tables across these two cores contain34020 records.

The A short graph has degree2 at the remaining retained hole u, degree0 at the omitted vertex and the two extra bridge labels, and degree1 elsewhere. Enumerating both neighbors of u followed by every complementary short perfect matching exhausts this degree domain. Rejecting repeated original edges and cyclic components leaves paths. External endpoints are **incidences indexed by position**, not a set of vertex labels. An extra bridge vertex that is an original A port has two distinct incidences at its isolated A vertex, paired with each other. That zero-length A path retains its vertex during expansion. In core24, omission3 permits port0: generation starts from the full mask minus {3,6,10,15}, and the c2 encoding includes nibble0.

After mapping all original port incidences through the actual crossing bijection, the graph includes the four short bridges and every B matching edge. The separate traversal checker enforces degree at most2, rejects duplicate edges, and rejects every component whose edge count reaches its vertex count. This catches both ordinary closed components and a doubled original-crossing/bridge edge. The surviving quotient has exactly ten terminal covered B vertices, paired into five paths, plus isolated retained B0. Eleven-cycle expansion restores all fifteen A vertices and four B bridge mirrors, hence 11+15+4=30 distinct vertices. All original edges are restored. Four-bridge spectra introduce no artificial required edges; the two-bridge auxiliary edges are all deleted or replaced in the audited five modes. No long auxiliary edge survives as an unrequired new edge.

## Full input domains and finite evidence

For each c, A inputs number binomial(12,c) times (11-c)!!; B is the exact validated residual list, and all c! sorted-port permutations enumerate every crossing bijection. The independent checker rebuilds the A spectra using adjacency traversal rather than the producer's union-find, and compares every uncovered26-byte full input with the saved stream, rejecting early EOF and trailing data. B files were separately checked for valid disjoint edges, exact support, uniqueness, equality with joint blocker residuals or the complete zero-spectrum set.

| c | A | B | full inputs | residual direct certificates |
|---:|---:|---:|---:|---:|
|2|62370|616|76839840|0|
|4|51975|272|339292800|3045|
|6|13860|32|319334400|8820|
|8|1485|1|59875200|2520|

Total four-bridge domain: 795342240. Fresh full traversal reruns completed at c=[2, 4, 6, 8]; remaining classes use the fixed complete independent traversal outputs whose sources, exact domains, streams and hashes were reviewed. Every one of the 1833510 direct certificates was freshly rerun after recompiling the independent C++ verifier in the isolated directory. It checks the exact input bytes, matching validity, thirty distinct target vertices, all thirteen required edges, closing adjacency and shortness of every other edge.

At c=0 the independent suppression checker freshly rebuilds every exceptional B matching and every A matching, then compares the **entire** saved input byte stream. At c=2 all62370 A and945945 B input signatures were freshly recomputed with DSU components; input uniqueness and cardinality give full matching-domain coverage, and both port orientations are checked. The negative text files were independently compared, family by family, with the actual transported exact Q4 negative tables. Thus neither c=0 nor c=2 relies merely on a residual count or unsuccessful search.

Counterexample checks cover an occupied bridge mirror, paired mirrors, duplicate crossings/bridges, a closed path component disjoint from quotient terminals, isolated Aport/bridge coincidence, Aport0 in core24, reversed c=2 orientations and both c=10,12 boundaries. The degree argument and audited mode hypotheses settle these cases; no new counterexample or open fatal/critical issue remains. There are no asymptotic, limit-interchange or measure-theoretic obligations.

## Scope and reproducibility

Fresh evidence and exact commands/results are preserved in `core4_core24_review_run/`. All reruns used isolated copies; the accepted fixed source files are hashed in the review JSON. Dynamic remaining-geometry ledgers are excluded. The core24 manifest by itself does not freeze all proof inputs, so this review's explicit hash dictionary supplies that missing provenance; it is not treated as a mathematical gap in the construction.

One review invocation used a nonexistent core24 negative filename and failed its spectrum assertion; the corrected invocation with `t15_core24_route_negative.txt` passed. This is recorded transparently in the isolated logs. Complete proof acceptance remains same-family/provisional; N14 and the prior restricted semantic import retain their explicit scope. No main-state integration is performed by this audit.

The first received core4 claim incorrectly ended its hole list at19. The construction and all certificates use31. This was reported as C4-01, the author corrected the theorem and regenerated the manifest, and the revised file/hash were reaudited. Only the corrected31 theorem is accepted.
