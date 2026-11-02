# Independent acceptance proof for two q8 filled sources

**Actual execution: both filled graph candidates PASS complete mathematical acceptance.** RESULT.json and TERMINAL.json record one successful compiler/validator batch. No graph is accepted from helper BFS alone: complete graph binding, all old-pair routes, helper routes, prefix preservation and nonD2 are all included below.

## 1. Actual geometry and complete graph definition

The original geometry is the already accepted585-point/585-line q8 generalized quadrangle; the derived geometry has its own512-point/640-line ordering. The accepted q8 pilot verified all336960 and322560 nonincident projections, respectively. This batch uses those incidence data and their physical IDs, without rechecking field laws or the small projection statements.

Old vertices are ordered pairs(p,L), labelled p*nl+L. For distinct vertices, the declared old adjacency is

    (p,L) ~ (q,M) iff Inc(q,L) and Inc(p,M).

There are exactly delta=(s+1)(t+1) possible(q,M) pairs satisfying this relation before removing the possible selfloop; hence old degree is delta−Inc(p,L). The code streams both complete unfilled and filled edge files, checking exact n m headers, a<b, strict global lex order, every old-edge incidence formula, and every vertex degree. Every old edge of the filled graph is simultaneously matched to the next unfilled edge, with both streams exhausted. Since all actual neighbors are allowed, simple and equal in number to all allowed neighbors, each actual old-neighbor set is complete. This proves the entire old graph definition, rather than just checking a subset of edges.

Helper f_j has exactly the old flags(p,L) with p on the jth spreadline. For each edge to a helper the validator checks that literal formula. The entire pin list is also explicitly compared against all corresponding flags. There are delta such pins. No helper-helper edge is allowed. These flag pin sets are disjoint because every geometry point has a unique spreadowner. Every flag receives its single helper edge, restoring old degree delta−1 to delta; other old vertices retain degree delta and each helper has degree delta. The actual filled CSR is built from that complete literal filled file, without a producer adjacency cache.

The original geometry's derivation point has physical pointID2. The derived source uses derivedpointIDs0..511, not original pointIDs and not field arithmetic modulo512. INPUT_DATA_BINDING.json records the accepted coordinate/order input used to interpret each physical graph label.

## 2. Every old pair has a genuine walk of length at most3

Let u=(p,L), v=(q,M). The verified generalized-quadrangle projection property supplies a point a on L collinear with q, and a line B through q and a. If q is on L, choose a=q and any line B through q. Likewise choose b on M collinear with p and a line A through p and b; if p is on M choose b=p and any line A through p.

Then the old graph relation allows the sequence

    (p,L), (a,A), (b,B), (q,M).

Indeed a is on L and p on A; b on A and a on B; q on B and b on M. A consecutive repeated vertex is only a deleted selfloop. Contract consecutive repetitions to obtain a genuine SimpleGraph walk of length at most3. Nonconsecutive repetition is allowed in a walk. This covers every ordered old-vertex pair, with no old-root BFS or assumption of a vertex orbit.

All these old edges remain in every filled prefix. Therefore all old-old pairs remain within3 throughout the actual helper insertion sequence.

## 3. New-helper distances and per-distance prediction

Each filled endpoint additionally receives ordinary queue BFS from every helper:64 roots in the derived graph and65 in the balanced graph. These BFS traversals use the actual complete literal CSR and count every newly discovered vertex through radius3. A vertex discovered at depth3 need not enter the queue because its neighbors are never expanded. Each root must reach the entire endpoint and match all four predicted distance counts.

For a root helper associated with spreadline S, its delta flag pins are distance1. An old pair(x,M) is at distance2 precisely when M meets S in an appropriate flag point and x is collinear with that point, excluding vertices already in distance1.

If M=S, all geometry points x give routes except the s+1 flags already at distance1. This contributes np−(s+1)=st(s+1). For the (s+1)t other lines M meeting S at p, there are s(t+1) choices of x distinct from p and collinear with p. Thus

    R2 = st(s+1) + (s+1)t*s(t+1) = s(s+1)t(t+2).

A different helper is not at distance1 or2: there are no helper-helper edges and the pin sets are disjoint. Therefore the prediction for each derived helper is(1,80,5544,322119), and for each balanced helper(1,81,5760,336448). The remaining R3 counts are measured by BFS, not substituted from this formula without traversing the actual graph. Every root's predicted and actual rows are retained.

Combining all old-old routes with every helper's measured full eccentricity≤3 establishes every pair in each full filled graph lies within3.

## 4. Why maximum-endpoint helper BFS proves every actual prefix here

A shortest walk of length≤3 starting at a helper has only old-source interior vertices. Its first interior vertex is an old flag. Its second interior vertex cannot be another helper, since that would give a common pin of two helper pin sets. It cannot revisit the root in a shortest walk either. A helper target can occur only as the endpoint.

Consequently, for any current prefix containing a measured helper and a target old vertex or present helper, the maximum-endpoint BFS witness survives: all interior vertices belong to the old source, and the relevant endpoint is present. Paths to helpers not yet inserted are not needed. This is the specific reason deleting future helpers is valid; no general monotonicity of diameter under vertex deletion is assumed.

Before helper j is inserted, every one of its pins still has old degree delta−1. It belongs to no earlier helper pin set. Adding the helper increases each such pin to delta and gives the new helper degree delta. Every actual prefix therefore retains the same degree cap and diameter≤3.

## 5. Exact diameter3

For each case choose the first two actual distinct ovoid points and their old diagonal pair vertices(point, its spreadline). One literal filled-CSR check verifies these vertices are distinct, nonadjacent and have no common neighbor; the actual labels and both full neighbor lists are saved in ACTUAL_NON_D2_WITNESS.json.

Thus their distance exceeds2 in the maximum filled graph. A prefix cannot acquire a new length≤2 path by deleting later helpers. Along with the all-pair upper proof, every actual prefix and each final filled endpoint has exact diameter3.

The unfilled graphs are classical-source reproductions, not new results. No new concrete Lean, globalrecord or priority certification is claimed. Root owns acceptance counters, comparison and any new formalization.

## 6. Closed actual run and evidence boundary

|Case|Classical unfilled n/m|New filled n/m|Degree|Actual helper BFS roots|Measured histogram per root|
|---|---|---|---:|---:|---|
|Payne derived|327680 /13104640|327744 /13109760|80|64|(1,80,5544,322119)|
|Balanced|342225 /13857480|342290 /13862745|81|65|(1,81,5760,336448)|

All four complete literal files were parsed once each. Both unfilled edge bodies were retained exactly in the corresponding filled graph, with no extra or missing old edges. The5120 derived and5265 balanced new edges all bind to the complete declared flag pin sets; there are no helper-helper edges. Every old and filled vertex's degree agrees with its complete neighbor formula. The actual nonD2 witnesses are[0,713] in the derived graph and[42705,43363] in the balanced graph, with zero adjacency and zero common neighbors; both literal neighbor lists are saved.

All129 individual helper roots reached all vertices and matched every distance class, with no assumption of an orbit. The combined BFS CPU was0.288545seconds. Each helper pin list and every same-cap prefix step are independently recorded in ORDERED_HELPER_PIN_BINDING.tsv and INDEPENDENT_PREFIX_PIN_CHECKS.csv. The entire graph-level and prefix proof thus applies to the physical labelled edge tables, not only to an abstract isomorphic geometry.

Measured total executable CPU was10.520798412seconds of150, including accepted-data coordinate/index binding, compiler, all four complete streams, actual CSR builds,129BFS roots, two nonD2 checks and driver aggregation. Compilation took1.593599148CPU and validation-plus-driver8.915584080CPU. There were zero failed compiles or runtime experiments, and all processes are terminal. Interactive authoring and initial read-only inspection are outside this explicit batch boundary.

There was no field-law, small generalized-quadrangle projection, old-rootR3, GF7/P33 graph, Lean, solver or external review rerun. Only the two filled candidates are new mathematical graph results here; their two unfilled sources are reproductions. Concrete Lean, latest-public comparison and priority are separate root-owned obligations. This actual source-D3 acceptance supplies the source premise previously left conditional in the q8 saturation-barrier note; no full-product clone batch is instantiated by this run.
