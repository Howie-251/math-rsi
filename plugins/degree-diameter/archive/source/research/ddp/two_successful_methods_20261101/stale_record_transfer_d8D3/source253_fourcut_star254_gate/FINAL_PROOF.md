# CM253 old-edge surgery: final proved scopes and preserved predictions

This final paper connects the actual cached-witness, repair-capacity and coupled-capacity receipts. It performs no source/field/unique-path validation, mask computation, half-choice enumeration, candidate graph, BFS or solver run. The source/provenance and RIGHT action are bound in `HISTORY_SOURCE_GATE.json`; all old raw files and intermediate predictions remain unchanged.

## Actual source and witness obligations

The fixed source is the253-vertex,1012-edge,8-regular diameter-three Comellas–Mitjana graph. Its actual RIGHT Cayley recipe has four positive inverse-pair classes. Vertex transitivity under LEFT multiplication is used to normalize an arbitrary first cut to one of these four canonical edges. No edge-transitivity between classes is assumed.

The old1012-edge cache supplies true unique source3-geodesic witnesses, one per old edge. Normalizing each entire path, with reversal when needed, yields27 distinct cached obligations per canonical class: nine first-cut-position witnesses, nine middle and nine last. The exact positional hit sets are:

- middle u–e–s–v: a star pin must equal u or v;
- first e–s–x–v: a star pin must lie in closed source B1(v);
- last u–x–e–s: a star pin must lie in closed source B1(u).

All first-cut endpoint masks are zero. These are necessary star-hit conditions; a negative on this true subset suffices even though the full set of old3-route bottlenecks is larger. `PAPER_WITNESS_GATE.md` gives their proofs and the precise normalization convention.

## Actual four-cut gate

`GATE_RESULT.json` reports997 other old edges per first class, after excluding the15 edges incident to the first two pins. Every such eligible edge hits at most6 of the27 obligations. Therefore three other cuts hit at most18<27. This excludes all four-vertex-disjoint-cut/eight-star modifications of this source, without a candidate graph or BFS.

The initial prediction that all four complete middle-critical graphs have a seven-edge matching was separately refuted on paper: old vertex-transitive distance-two data force no triangles and at least one four-cycle, and a cut on that four-cycle has an isolated middle row and column. This refutation does not affect the mixed-position27-obligation gate. The numerical cached-middle graph alone was not treated as the complete middle graph.

## Genuine five-cut/one-nonedge-repair rule

Delete five vertex-disjoint source edges, and add one original-source nonedge R={a,b} plus a new vertex adjacent to the eight remaining endpoints. The repair endpoints are released by two different half-cuts a–a',b–b', and are not star pins. Three other deleted edges are full-cuts, with both ends in the star. Degree accounting gives254vertices/1016edges, all8-regular. Restoring one deleted old edge instead would reduce to a previously excluded pure four-cut star; attempting to add an already retained source edge gives no new repair.

For any old–old simple path of length≤3, visiting the new point uses two consecutive star edges. Using R as well would require a repair endpoint to be a star pin, which the rule excludes. Thus a damaged cached witness must be repaired by star OR repair-only, never a short route mixing both new mechanisms.

The star hit masks remain necessary upper bounds, but the old pure-star distance-to-pins equality is not inherited: a half-cut has one endpoint outside the star set. The relaxed repair mask uses G minus the first full-cut, permits either orientation of R, and permits total old-leg length≤2. It ignores all four later cuts and therefore contains every possible actual repair-only route. Both relaxations are safe for a negative capacity bound, not positive certificates.

The first independent-capacity gate maximized star and repair separately. It found mEdge=6,mVertex=6 and maxRepair=11, giving the loose upper bound24+11=35≥27. The capacity-alone exclusion prediction was not supported. That was not a graph and not evidence that compatible half-cuts realize the separate maxima.

## Actual global coupled bound closes the repair rule

Fix a canonical full-cut e–s and an original-source nonedge R={a,b} avoiding those first pins. Choose a'∈N(a),b'∈N(b), requiring{e,s,a,b,a',b'} to have six distinct labels. Define

base = relaxedRepairMask(R) OR V(a') OR V(b').

The two remaining full-cuts must avoid these six vertices and each other. Each belongs to the old eligible source-edge pool and contributes at most6 further hits. Hence every actual candidate must cover its27 obligations within at most popcount(base)+12 bits.

`COUPLED_RESULT.json` records a complete global scan for all four canonical first types. For each type it considers all30378 original-source nonedges and all1910136 legal half-endpoint choices. The maximum base hit is12 in each type. Thus every possible candidate has at most12+6+6=24<27 hits. At least one true old witness remains without any≤3 route, so no candidate can have diameter≤3.

This is a complete necessary-condition NO for the stated five-disjoint-cut, one-source-nonedge-repair, eight-star family. The global scan was complete; no two-fullcut join or actual candidate/BFS stage was reached. The result's stored first/maximizing tuple is capacity witness metadata, not an indication that only one repair was tested. `complete_global_coupling_scan=true` is the relevant global completion flag; the later prototype branch was skipped.

The cumulative numerical terminal is3.686201072/20CPU seconds, preserving all stages and their costs. The literal source was used as input but old source D3/field/unique-word validation was not repeated. There were zero candidate graphs, BFS or solver calls. The independently loose35 bound and the later coupled24 bound are compatible statements about different relaxations; both remain in the history.

## Stronger paper corollary: any at-most-five pure deletions plus one new point

The actual eligible-edge maximum6 extends to **every** source edge without another scan. First-cut pins have V(e)=V(s)=0. For any outside vertex x,8-regular simplicity leaves at least six incident edges x–y avoiding e,s. Each eligible mask V(x) OR V(y) contains V(x), so |V(x)|≤6. Any excluded first-incident edge e–x or s–x has exactly mask V(x), and the first edge itself has zero mask. Therefore all source edges have mask hit count≤6.

Now delete any set F of at most five distinct source edges, allowing shared endpoints and arbitrary unused degree slack. Add one new vertex z with only new–old edges, maintaining maximum degree≤8; no old–old edges are added and no old vertices are removed. Every new neighbor must be an endpoint of some edge of F, because untouched source vertices still have degree8.

If F is nonempty, select and canonically normalize one first edge. Its two endpoints hit no obligation bit. The other at most four source edges together hit at most4*6=24<27. Thus even the union of **all** freed endpoints fails to hit a cached obligation, and the actual neighborhood of z, being a subset, also fails.

This remains a necessary condition when the first-cut endpoints are not new neighbors. For a middle witness any old–old route of length≤3 through z has two star edges and at most one old edge, forcing at least one witness endpoint itself to be a new neighbor. For a first witness e–s–x–v, such a route forces a new neighbor within one old step of v, regardless of whether e is a star pin. The last case is dual. These are exactly the cached hit sets used above, now only as necessary conditions. They do not assume the first pins were attached.

The unique old3-path is destroyed by the first deleted edge, so an unhit witness has no remaining old route or new-star route within3. This contradicts diameter≤3. With no deletions, there is no old spare degree to connect the new point. Therefore **every one-point pure-deletion/new-old-edge augmentation of this fixed source using at most five deleted old edges is impossible at maximum degree8**, even with overlapping cuts, fewer than eight new neighbors and a nonregular result.

For five deletions the full freed-endpoint set can have ten vertices. This proof does not incorrectly claim that joining all ten gives a degree-legal star. It uses the direct necessary hit condition on the actual degree-legal neighborhood and needs no full-star supergraph or distance-to-pin equality.

## Final stopping boundaries

Two scopes are closed: the broader at-most-five pure-deletion/star rule just proved, and the actual five-**matching**-cut/one-genuine-nonedge-repair/eight-star rule proved by the coupled scan. The latter does not classify nonmatching repair cuts with overlapping repair/star roles, multiple old–old repairs, other rewiring, another source or general N(8,3). Such models could have short routes absent from the present decomposition. No alternative rule or extra budget is launched here.

All conclusions are model-specific. There is no new graph, parameter, Lean instance, independent-method count or priority claim. The unused full seam interface remains a valid possible verifier but was not run after these necessary obstructions closed the actual domains.
