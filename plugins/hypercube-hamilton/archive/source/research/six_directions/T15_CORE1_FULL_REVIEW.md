# T15 core1 full closure: fresh proof review

**Verdict: PASS.** Reviewer: GPT-6.1-sol, high, fresh agent `/root/t15_core1_complete_audit`. ARIS proof-checker applied. Review independence is **same-family** and semantic acceptance remains **provisional**. No production proof, input, or global ledger was modified.

The audited theorem is: for every perfect matching F of the complete graph on the 26 vertices outside {0,1,2,7,11,19} of Q5, there exists a simple cycle on exactly V(Q5) minus {1,2}, containing F, whose other edges are short. All cube-automorphic images of this marked geometry follow by transporting F and the cycle. The conclusion concerns complete core1 only; it does not establish all T15 cores, the full eight-hole integration, or P6.

## Proof obligations and quantifiers

**MC1: Split and total crossing cases. DISCHARGED.** 2|F_A|+c=12 and 2|F_B|+c=14; hence c is precisely one of 0,2,4,6,8,10,12.

**MC2: N14 import and parity. DISCHARGED.** Arbitrary K(Q4) matchings; all two-hole representatives independently rechecked, 270270 positive certificates; cube translations and coordinate permutations preserve new-edge shortness.

**MC3: c0 complete coverage. DISCHARGED.** N14 gives the A s-t path uniformly in F_A. B paired st cases are rejected. All 135135 B inputs regenerated; exact 105 exceptions times all 10395 A inputs equals the complete saved 1091475 list.

**MC4: c2 spectrum quantifiers. DISCHARGED.** For all 62370 A and all 945945 B inputs with nonzero B spectrum, both crossing orientations have a common bit. The A forest may depend on the chosen bit; no common forest across all B is asserted or needed. Exactly 420 zero B inputs, exactly matching B2 list.

**MC5: Double bridge import hypotheses. DISCHARGED.** Retained A holes 3,5,9 are distinct nonzero even labels disjoint from B holes 0,1; c>=4 ensures required remaining auxiliary pairing is nonempty. Five modes exhaust the B status of the two bridge mirrors. Every inverse family and every positive blocker was rerun independently.

**MC6: Residual B intersections and arbitrary C. DISCHARGED.** Coordinate permutations fixing 1 transport the canonical inverse families to all three pairs. Intersections equal the supplied B lists 210,28,1,0,0 for c=4,6,8,10,12. The construction pulls the auxiliary pairing through the actual arbitrary crossing bijection; reduction is uniform in A and C.

**MC7: Complete A short-degree enumeration. DISCHARGED.** Each of 18 bridge choices uses two distinct short neighbors of the third retained hole u, then all short perfect matchings of the remaining required vertices. Enumerating the least remaining vertex is complete without duplication. Repeated original edges and cyclic components are rejected.

**MC8: Duplicate endpoint stubs and isolated vertices. DISCHARGED.** The endpoint list has c+4 distinct stub positions, although the underlying A label can repeat. If a J endpoint is an original port, it is isolated in F_A union N and pairs its crossing stub to its bridge stub; expansion restores this single A vertex. A bridge coinciding with an original crossing yields two parallel compressed edges and is rejected as a two-cycle.

**MC9: Compression and positive transfer. DISCHARGED.** After an accepted forest is attached, all ten terminal B vertices have degree one, all retained interior vertices degree two, and free 0_B degree zero. Acyclicity gives exactly five paths. Their matching is tested in the correct 11-cycle table. Expanding adds 15 A vertices and 4 removed B vertices, giving 30 distinct vertices, all 13 original edges, and only short other edges.

**MC10: Finite fourbridge input coverage. DISCHARGED.** A generation count is binomial(12,c)*(11-c)!!; every residual B input is checked with every one of c! orders of its sorted ports. All spectra may select their own bridge choice, forest and positive table entry. Exact residual byte streams, premature EOF and trailing bytes were checked by the independent adjacency/component implementation.

**MC11: Positive and negative finite table scope. DISCHARGED.** Every one of 18 five-avoided tables contains exactly all 945 arbitrary five-edge matchings on its prescribed ten covered vertices. All positive cycles and all negative short-degree completions rerun. Only positive witnesses are required by the fourbridge argument; a negative entry rejects a construction, not the original matching.

**MC12: Residual positive and final closure. DISCHARGED.** All 1101870 direct certificates were freshly checked against exact original input bytes, 26 covered vertices, 30-vertex cycle support, all 13 matching edges, short added edges, distinct vertices and closing edge. The crossing cases exhaust all inputs; final theorem follows without an eight-hole or full T15 conclusion.

## Fresh finite verification

The C++ checkers were freshly compiled with `g++ -O3 -std=c++17` into `t15_core1_review_trace/`, without `NDEBUG`. The independent fourbridge checker uses degree-limited adjacency lists and component traversal instead of the producer's union-find. The matching/short-edge enumeration recurrence is shared in form and was checked mathematically for exhaustive coverage; graph acceptance and residual equality were rerun independently.

| c | A inputs | B inputs | Full A/B/bijection inputs | Exact residuals |
|---:|---:|---:|---:|---:|
|2|62370|420|52390800|0|
|4|51975|210|261954000|1575|
|6|13860|28|279417600|6300|
|8|1485|1|59875200|2520|

All **653637600** fourbridge inputs passed the fresh rerun. The uncovered lists matched the saved input streams byte-for-byte. All **1101870** direct positive certificates passed fresh verification: 1091475 at c=0 and 1575, 6300, 2520 at c=4,6,8. N14's 270270 certificates, the canonical three-avoided table, the 18 five-avoided tables, all five inverse modes and positive blockers, exact c0 exceptions and complete A product, exact c2 zero-spectrum B list, and the joint-B intersections were independently rerun with outputs redirected to the trace directory.

The original c2 parser lacks explicit bounds and self-loop guards for every edge. A fresh strict scan checked all 62370 actual A and 945945 actual B inputs for bounds, exact excluded holes, distinct endpoints, no endpoint reuse, correct edge count and exact complementary port pair. Combined with the original uniqueness/spectrum checks and the known domain cardinalities, this discharges coverage for the frozen input. It is not an open proof gap. Future input changes must repeat strict validation.

The closure Python file is a manifest/status aggregator, not an independent proof verifier. Its PASS was accepted only after the underlying checkers and all fixed hashes were checked. All 70 predeclared hashes still match. The review JSON additionally fixes the N14 binaries and checker dependencies actually used. Dynamic global coverage ledgers are absent from `audited_input_hashes`; the unrelated prior-review format example is recorded only under `context_snapshot_hashes`.

## Counterexample and dependency checks

Adversarial cases checked: c0 internally paired bridge mirrors; c2 zero B spectrum and reversed crossing orientation; isolated A vertices carrying two distinct stubs; a bridge equal to an original crossing; repeated original/short edges; closed components without terminals; negative table entries; and the smallest c=4 occupied-mirror mode. These cases are explicitly rejected where invalid or included in the exact residual/direct-certificate route. No counterexample or unresolved FATAL/CRITICAL/MAJOR issue was found.

The dependency chain is acyclic: fixed Q4 N14/tables, then c0/c2/R4 reductions, then exact residual B domains, then fourbridge coverage and direct residual certificates, then core1. No downstream theorem or dynamic global ledger is used to prove an upstream obligation. There are no limit, asymptotic, analytic-interchange, or probabilistic qualifications. Uniformity over arbitrary original crossing bijections is explicit in the port-order enumeration and in the inverse-blocking transport.

Reproduction evidence, exact input hashes, and all discharged micro-claims are recorded in `T15_CORE1_FULL_REVIEW.json`. Fresh artifacts are confined to `t15_core1_review_trace/`.
