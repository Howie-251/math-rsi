# Degree10 fixed-source single extension: four exact dual exclusions and one raw solver infeasibility

No33398-vertex candidate was found. All five lossless symmetry cases have now been processed: four are rigorously excluded by saved integer duals, and the remaining case returned HiGHS Infeasible. The last result has no independently checkable solver proof, so it is recorded as an exploratory infeasibility result, not as a fully certified mathematical exclusion of the entire fixed-source family. No candidate graph, new lower bound, or new BFS was produced.

The source is the nonregular33397-vertex geometric fold, with166425edges and degree distribution6:28,7:336,10:33033. The only eligible old neighbors for a new degree-at-most10 vertex are all364 H3 spare vertices. The exact model has364binary variables, one for each possible old neighbor, cardinality at most10, and a cover constraint for each of33397 targets using their actual closed R4 balls. Identical coverer rows reduce these to26117. The target was33398, one above the saved33397 bound. All old source edges remain fixed.

The verified coordinate permutations from symmetry_g2_root give five actual pin orbits, sizes84,84,28,84,84, represented by pins0,1,2,52,390. Case j excludes every earlier orbit and selects the current representative. This is a complete disjunction: a nonempty cover has an earliest selected orbit, and a verified group word transports a selected member to its representative while preserving cardinality and the entire coverer rowset. No second pin was fixed and no named group was assumed.

The cases were processed in order4,3,2,1,0. Each substituted the fixed columns, removed already satisfied rows, repeated singleton propagation, omitted unused columns and deduplicated equal rows. No additional selected pins were forced. Every reduced model records its exact original-row representatives and free columns.

| Case | Fixed representative | Excluded columns | LP total optimum | Exact integer total-pin lower bound | Final status |
|---|---:|---:|---:|---:|---|
|4|390|280|28|28|Exact integer dual excludes cap10|
|3|52|196|13.5333333333|14|Exact integer dual excludes cap10|
|2|2|168|12.9618644068|13|Exact integer dual excludes cap10|
|1|1|84|11.0971283784|12|Exact integer dual excludes cap10|
|0|0|0|9.98549891174|10 (earlier exact global dual)|Raw HiGHS Infeasible, no trusted proof|

For each exact dual, the common denominator is1000000. The total positive integer row weights for cases4,3,2,1 are26999996,12533258,11961765,10096984. Each case already fixes one pin, leaving budget9. Every free column's total weight is at most1000000, while each displayed total exceeds9000000. Thus every remaining cover exceeds that budget. verify_integer_duals.py rebinds all reduced rows to the original26117 rows, recomputes the substitutions and deduplication, and checks every column load using integer0/1 arithmetic. The results are in integer_duals_checked.json. Consequently any possible10-pin cover must meet the first84-pin orbit and can be transported to one containing pin0.

Case0's first LP hit a conservative8second internal limit. That history is retained in early_terminal.json and case0/LP_result.json. Because the authorized120CPU batch had used only18.989590 CPU seconds and no MIP had run, the still unresolved case0 LP was completed under the same unchanged model and original global budget. The parent explicitly confirmed this allocation. This second LP returned optimal9.985498911740056 in13.315501 CPU seconds. The case's only MIP then returned status2, HiGHS Infeasible, after46.902988 CPU seconds, before its79.385667second limit. There was no incumbent, second MIP, new seed or further case. The MIP log is a raw solver conclusion only; no proof logging or trust promotion was added.

The two model processes used about79.507947 CPU seconds in total, below the original120CPU limit. A separate small integer certificate check took about0.23seconds. The batch made six LP calls including the preserved case0 timeout, and one MIP call. All heavy processes have exited. The earlier unrestricted UNKNOWN remains historical evidence; this new symmetry-broken batch adds four strict case exclusions and one uncertified solver infeasibility. This source's single-vertex family should not be mechanically rerun with new seeds or time slices. Any future work requires a genuinely new reason or a proof-completion decision.
