# Independent audit: 55 actual marked T26 orbits

Verdict: **PASS**, same-family / provisional. Reviewer `/root/t26_first_rank_review`, GPT-6.1-sol high, the explicitly requested route. Frozen proof SHA256: 3908f60e884dda47570e652b6448b5ca2c519d8dadb8ba878879201be819cfc4. Frozen manifest SHA256: 8f5980a073c646677c3ddfbf69dc8f300affccecd08d7f1cd9d34a9198fc58de.

The accepted local scope comprises **all 55 registry entries**, each universally quantified over every complete-graph perfect matching on its 24 covered vertices, with the actual prescribed two majority omissions. Every entry gives a simple 30-cycle containing that matching and having only short new edges. Required edges may be long or join equal parities. Common cube automorphisms, including parity reversal, transport the complete marked statement. This does not establish unrestricted T26.

## Independent computational evidence

The first entry was checked in Python as recorded in Q5_T26_RANK_FIRST_REVIEW.md/.json. A new, independently authored C++ checker verifies the other **54 entries**, rather than just the 22 greedy coverage entries. It does not run or import the producer search or checker. Its configuration is compared with each frozen registry geometry. Every frozen manifest artifact is rehashed and its size verified.

For each new entry the C++ checker independently verifies exactly 2048 short forests with 18 distinct edges each: prescribed zero/one/two vertex degrees, omission, acyclicity, and equality of its actual component endpoint pairing with the supplied pairing. Each column matching is verified to use every one of the 24 covered vertices exactly once. The checker contracts each forest pairing into 12 components, recomputes connectivity for all 2048 by 2048 column pairs using DSU, and requires full byte equality with the supplied matrix. Independent increasing-column Gaussian elimination on 64-bit row blocks proves rank 2048 from scratch. The supplied pivot/combination arrays are unnecessary to this independent rank proof; their file hashes remain bound. For the first entry those arrays were additionally checked in Python.

Across the 55 entries this checks **112640 selected forests, 112640 columns, and 230686720 connectivity bits**. No rank-deficient, capped or failed search is treated as positive evidence. No assumption of independent cherries, generator completeness, random sampling, or floating-point rank enters the proof.

The all-entry run is Q5_T26_RANK_BATCH_REVIEW_run.py, calling Q5_T26_RANK_BATCH_REVIEW_check.exe compiled from the independent source of the same basename. The certificate log and checker JSON record the result. A transient log-encoding error after all 54 certificate invocations passed was repaired by explicitly writing UTF-8, and the completed pipeline was rerun. An initial application assertion was also corrected to recognize that the producer projection JSON lists *all* 41236 inputs, including empty witness dictionaries. Neither was a producer mathematical discrepancy.

## Mathematical proof obligations

The local proof is the same valid argument as the independently audited first entry; see Q5_T26_RANK_FIRST_REVIEW.md for the detailed ledger and full transfer replay. The external algebraic premise was freshly verified in the [primary author manuscript](https://pure.tue.nl/ws/portalfiles/portal/99596886/1211.1506.pdf): abstract page 1 defines all complete-graph perfect matchings; Theorem 3.4 and Corollary 3.5 on PDF page 9 give GF(2) rank 2^(t/2-1) for every even t>=2. Substitution t=24 gives the required upper bound 2048, without imposing bipartiteness.

The independently computed full-rank restrictions make the 2048 complete selected rows a basis of H_24's entire row space. Every arbitrary matching column F is nonzero, because linking cyclically the second endpoint of each F edge to the first endpoint of the next edge constructs an alternating Hamilton cycle. Consequently some selected row connects with F. Expanding its disjoint short forest paths gives a connected degree-two graph on precisely the 30 specified vertices. A shared F/pair edge would isolate a labelled two-cycle, so cannot occur in a successful pairing; hence expansion is simple and preserves F. This closes the universal matching quantifier; the supplied 2048 columns are a rank witness, not a finite replacement for all F.

Dependency DAG: primary rank bound + independent finite forest/matrix checks -> each exact local theorem; these + previously accepted uniform transfer, balanced two-hole A endpoint, and exact accepted residual -> Q6 coverage. There is no circular appeal to the desired ten-hole/P6 result.

## Actual Q6 application

For row (2,1), S consists of both even Z holes in A; for row (0,3), S is any two odd W holes in A after excluding the possible source whose mirror is root. These are two distinct *actual short bridges*, and every mirror is internally covered for every realizing original matching: original hole independence excludes another nonroot hole; root is excluded explicitly or by parity; the free bridge source excludes an original crossing edge. Both A completions leave balanced two holes. Their root is u when u is in A; otherwise it is an even bridge source in (2,1), or an even crossing port in (0,3), guaranteed by the port imbalance 3. The covered target remains legal in each completion.

The accepted tag/forest compression proof applies with both bridge conflicts simultaneously. Their original pendant mates are distinct and outside transferred endpoints, because they are internally covered, opposite in parity to the common-parity mirror set, and cannot be crossing ports. Suppression gives an **arbitrary** matching on B, including long or same-parity compressed edges. In (2,1), the actual B minority is Z intersect B, majority is (W intersect B) plus mirrors; in (0,3), minority is W intersect B and majority is (Z intersect B) plus mirrors. Exactly those mirrors are omitted. Each applicable registry theorem permits every such compressed matching. Expand every suppressed path and transferred A path and delete the tag; root/target are unchanged, all original matching edges survive, and all surviving new edges are short. The c=0 boundary remains the previously accepted five-direction case. The construction is uniform over all original short matchings realizing the eligible geometry, not an existence claim for one sample matching.

For coverage, the new Python checker enumerates all coordinate cuts and every legal bridge-source pair directly on the latest **41236** inputs, whose hashes are bound to TEN_COVERED_Q5_ENDPOINT_REVIEW.json. It independently constructs translations and coordinate permutations of every whole marked registry geometry, producing 129280 distinct marked images, checks that entries do not collide, and uses actual marked triple membership rather than the producer's canonicalization function. It validates every record's full set of applicable orbit indices and every supplied cut/source/local marked witness against its own enumeration. It also saves an explicit common automorphism with one independent witness for every newly covered record. No producer module or executable is used.

| Target | Accepted input | New coverage | Still OPEN |
|---:|---:|---:|---:|
|1|12910|12000|910|
|7|12696|11220|1476|
|31|15630|13920|1710|
|Total|41236|37140|4096|

The independent residuals preserve original record order and have both exact byte and exact set equality with the frozen producer residuals. No earlier A10/T63/endpoint class is counted twice.

| Independent residual | SHA256 |
|---|---|
|Q5_T26_RANK_BATCH_REVIEW_remaining_v1.bin|6bf4aa2ad4565ce7e04ebf032c880b4054f8e22e596415b0a9a6aae81659b84f|
|Q5_T26_RANK_BATCH_REVIEW_remaining_v7.bin|86f408e541cc1a5531ddefde2d9c119fec95668c0df8e96a7dd6ce64cbdeeb5a|
|Q5_T26_RANK_BATCH_REVIEW_remaining_v31.bin|766e1d4b809b6a88a18fb02da952caad684604b141e3548c39647e9ff8cc71d9|

All obligations in this declared local-and-application scope are discharged, with no open fatal/critical/major issue. The 4096 residual inputs remain mathematical obligations, not counterexamples. Full T26, full ten-hole covered/free endpoint layers, higher Q6 layers and full P6 remain **OPEN**. The producer artifacts and main state were not edited; only separately named reviewer evidence and residuals were written.
