# Independent fourteen-hole cached-positive review

**PASS for the twenty explicit new local inputs and their actual application.** All38,912 forests,77,594,624 connectivity bits,20 independent full GF(2) ranks,278,524 actual all-hit witnesses and35,665 chosen witnesses pass. The exact remainder is12,546:12,528 covered-target and18 free-target geometries. Complete fourteen holes and full P6 remain OPEN.

Reviewer `/root/fourteen_reuse_review`, user-selected GPT-6.1-sol/high, is independent of the producer. ARIS proof-checker applied; same-family/provisional acceptance relative to explicit imports, with no Lean or cross-family formalization. The first-stage actual application is now accepted by `FOURTEEN_REUSE_REVIEW.json`. Its full12 predecessor import is the finalized PASS at SHA256 `405b019235810d8df75d58354b10c6d8ed42c1129a942940311555277a9382ce`. Thus the historical source-reduction condition is discharged. Producer and RUN_STATE files remain unchanged.

Proof SHA256 `236ec40a547b1a0084d4351dfc7ba18d23e7df596ed715c1052d4ca861b84341`; manifest SHA256 `4852582087a3b3c06eaf26a9b8eec5b1b63b26e192cdd3e901e23ba3d59902e6`. Every manifest hash matches. Formal imports and exact scope are hash-bound in the JSON.

## Twenty local statements, not403 new rank premises

For each selected explicit marked geometry, every arbitrary perfect matching of the covered terminals has a cycle on Q5 minus exactly its marked omissions, containing that matching with only short new edges. Auxiliary required edges may be long or same-parity. The selected exact codes are1040,1007,1186,1156,1016,1248,1148,1041,1300,1132,1118,1069,1246,1006,1251,1252,1288,161,1205,318; code1000+i denotes EXTRA i, and a code below1000 denotes NEW i. Canonical marked sets and certificate prefixes are explicitly listed in JSON `accepted_marked_inputs`. This is not full T26, T17 or T28.

`FOURTEEN_CACHED_REVIEW_local_check.cpp` adapts the earlier independent local checker. It takes the exact selected geometry table, checks sorted config hole sets and marked omissions, validates every short forest edge, rejects duplicates and cycles, checks degrees0/2/1 at omitted/included-hole/covered vertices, and derives the actual terminal path pairings by DSU. Every stored pair and column is independently checked as a perfect matching on precisely the covered terminal set. Every matrix bit is rebuilt by a fresh labeled matching-union connectivity computation. Low-pivot Gaussian elimination on rebuilt rows gives full rank independently of producer pivots/flags. All supplied combination equations and pivot-leading-position assertions also pass.

| Type | Exact inputs | Terminals | Rank each | Forests | Rebuilt bits |
|---|---:|---:|---:|---:|---:|
|T26|10|24|2048|20480|41943040|
|T17 unconditional|8|24|2048|16384|33554432|
|T28 unconditional|2|22|1024|2048|2097152|
|Total|20|—|—|38912|77594624|

The mathematical rank import is the generic upper bound rank(H_t)<=2^(t/2-1) over GF(2) for all even t, on arbitrary complete-graph perfect matchings, from [Cygan, Kratsch and Nederlof](https://arxiv.org/abs/1211.1506). The primary source was independently reopened during this review; its abstract explicitly confirms the generic bound and complete-graph scope. Here the import is used at t=22 and t=24; the older A10 source note's original t=22-only application does not restrict the published generic theorem.

The verified submatrix has rank equal to that upper bound, so its selected endpoint-pairing rows span the entire matching-connectivity row space. For any arbitrary required matching F, a matching P that joins its oriented edges cyclically gives a nonzero H-column. Therefore a selected row must also be nonzero in that column. Its actual forest and F form one connected2-regular labeled graph on the included vertices and hence the required cycle. Any common forest/F edge would give a separate labeled two-edge component and fail connectivity because there are at least22 terminals. Thus all surviving added physical edges are short. This is a deterministic universal proof modulo the generic rank theorem, not a sampled-matching inference.

## Actual application and exact unions

The source is the accepted first-stage48,211-record original-label domain. The independent application checker uses the k7 construction and completion/suppression/expansion proof in `FOURTEEN_REUSE_REVIEW.md`. Selected type rows are T26 even(a,b)=(4,3)/odd(2,5), T17 even(5,3)/odd(2,6), and T28 even(4,2)/odd(1,5). Their balanced A holes are3:3,3:3 and2:2. Every realizing original matching is short, the actual sources exclude free target/root mirror, and the synchronous actual marked B geometry is within the exact universal local input. No forced obstruction or unreviewed A theorem is used.

`FOURTEEN_REVIEW_prepare.py` independently expands all403 explicit geometry predicates and the20 selected predicates using common anchored translations/permutations. It does not use producer positive-rank flags as acceptance. `FOURTEEN_REVIEW_application_check.cpp . 2` enumerates actual legal cuts/source subsets for every record, verifies all278,524 record/orbit witnesses against their named exact geometry, and compares the complete recomputed orbit-hit set with the supplied all-hit set record by record. It checks that selected20 and all403 geometry predicates have exactly the same covered-record union. It replays every selected witness, requires its exact row among the20 accepted rows, and verifies the complete residual byte/order partition. The other383 local-rank claims are not premises and are not accepted by this report.

| v/status | Source | Positive | Exact remaining |
|---|---:|---:|---:|
|1 covered|9285|6180|3105|
|1 free|0|0|0|
|7 covered|16108|12495|3613|
|7 free|18|0|18|
|31 covered|22500|16690|5810|
|31 free|300|300|0|
|Total|48211|35665|12546|

Counterexample attempts covered same-parity/long required edges, forest cycles, false stored endpoint pairing, a common required/forest edge, rank achieved only by producer pivots, wrong omitted marks, source exclusions, mismatched original source indices, omitted candidate-orbit hits, overlap double counting and a selected registry with a smaller union. Direct deterministic checks and the rank argument discharge these. Greedy minimality is neither required nor claimed. Failed predicates on the final12,546 records do not show nonexistence of a desired extension.

To reproduce, run the reviewer preparation, compile/run `FOURTEEN_CACHED_REVIEW_local_check.cpp`, compile/run `FOURTEEN_REVIEW_application_check.cpp . 2`, and run `FOURTEEN_REVIEW_import_check.py`. There are zero open issues within the declared local/sufficient-application scope.
