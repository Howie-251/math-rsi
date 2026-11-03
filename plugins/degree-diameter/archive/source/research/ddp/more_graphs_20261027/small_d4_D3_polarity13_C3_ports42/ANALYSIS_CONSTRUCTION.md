# Geometry, gauge, and the exact prepared42-vertex model

The construction and its existential CNF encoding are **VALID**, but the whole three-helper completion family is ruled out by [ANALYSIS_EXTERNAL_OBSTRUCTION.md](ANALYSIS_EXTERNAL_OBSTRUCTION.md). No SAT call is needed. This review reads the prepared compiler/decoder only and runs no geometry calculation, word enumeration, solver, graph, or BFS.

## Base and degree accounting

Represent the13 points of PG(2,3) by nonzero vectors of F3^3 up to scalar, with polarity given by the dot product. Join distinct points when their dot product is zero; delete the four absolute loops. A perpendicular projective line has four points. An absolute point therefore has degree3, and each of the other nine points has degree4, giving24 ordinary edges.

The absolute vectors have all three coordinates nonzero. Two distinct absolute points are not orthogonal, so the four absolute vertices are independent. Every C3 voltage lift has39 vertices and72 old edges, with12 absolute lifts of degree3 and27 other vertices of degree4. All66 pairs among those12 ports are therefore nonedges of the old lift, including pairs within the same base fibre.

Add three helpers with induced path a-b-c. The endpoint helpers need three old spokes each and the middle needs two, making eight spokes. Each old port receives exactly one additional edge. The remaining four ports consequently form two old-old matching edges. The total is72+2+8+2=84 edges on42 vertices, all degrees4. The domains of66 old-port pairs and36 port/helper edges are complete for this fixed P3 completion rule.

The degree requirement itself is appropriate: in any maximum-degree4/D3 graph, a root of degree at most3 reaches at most1+3+9+27=40 vertices. Hence a42-vertex target must be4regular. This is a local-root bound, not the smaller maximum-degree3 Moore bound.

## The spanning-tree voltage gauge is lossless

Orient each base edge u-v once. Its trit lambda gives lifted edges (u,s)-(v,s+lambda). Relabel each base fibre independently by s'=s+f(u). The transformed voltage is

    lambda' = lambda + f(v)-f(u).

Since the base is connected, choose any spanning tree with12 edges and recursively set f so every tree voltage becomes zero. The remaining24-12=12 chord voltages are free trits. This is an isomorphism of the whole construction family: it permutes the12 ports within their absolute fibres, while arbitrary port-pair and helper-spoke choices, the helper degrees3/2/3, and the fixed P3 are preserved. No particular spokes, old-port pairing, or deck symmetry was fixed. The gauge therefore loses no graph in the stated family.

An old39-vertex voltage cover need not be connected: the port gadget could join its components. Rejecting it solely for disconnectedness, or inheriting a diameter from the base, would not be valid. The completed graph is also not generally a regular cover of a14-vertex base because its arbitrary port edges and asymmetric helper path break the deck action.

## Prepared compiler and reused edge selectors

The inspected [compile.py](compile.py) fixes the tree shifts, gives each chord three exactly-one shift selectors, and uses a selector for all three lifted edges with that shift. It does not replace these translations by independent edge choices. Its36 trit-selector bits plus66 pair and36 spoke bits are138 structural variables.

The twelve old-port degree equations use only the new pair/spoke variables, excluding the old lift-edge conditions. The helper cardinalities are exactly3/2/3. The compiled potential-edge map contains38 unconditional edges (36 tree lifts and two helper-path edges) and210 conditional edges, with shared voltage-selector aliases, for248 potential edges. An assignment selects exactly84 actual graph edges. The [MODEL_STATS.json](MODEL_STATS.json) reports8436 total variables and19048 clauses; these are the prepared model, not an actual target graph.

## Reachability witnesses cannot invent paths

For every pair u,v, the compiler either recognizes a fixed path of length at most2 or introduces Y_uv. Its soundness clause is

    Y_uv => X_uv OR any two-edge witness through w.

A two-edge AND witness implies both structural edge conditions. Thus Y_uv=true always certifies a genuine path of length at most2. The compiler does not use only the unsafe reverse implication that a path implies reachability while allowing Y to float freely.

For every pair not unconditionally at distance at most2, the diameter clause is

    Y_uv OR any_w (X_uw AND Y_wv).

The three-route AND witness implies the selected first edge and the sound Y_wv flag. Its dependencies terminate at structural conditions; there is no circular reachability assumption. Hence every satisfied diameter clause certifies an actual path of length at most3. Symmetric pair indexing is harmless because the graph is undirected, and all unordered pairs are covered or discharged by unconditional paths.

The one-way AND and Y implications are existentially complete. Given an actual D<=3 graph in the family, set every Y flag according to actual distance<=2 and choose all available two/three-path AND witnesses to be true exactly when their arguments are true. These assignments satisfy the soundness clauses and every coverage clause. Therefore existence of auxiliary values is equivalent to existence of a full D3 structural assignment, despite auxiliaries not being uniquely defined by all clauses.

The [decode.py](decode.py) reconstructs edges exclusively from INPUT.potential_edges and their structural literals. It never treats an AND or reachability auxiliary as an edge. It checks every CNF clause, degree4, and then, only if later supplied a SAT witness, would run full42-root verification and export a literal graph. That decoder has not been executed by this review.

## Scope and decisive outcome

The old deck-symmetric helper-triangle control has a separate valid thin-route obstruction: its helper base vertex has two spokes to two absolute base points, while an unattached absolute point has only one two-edge old route from each. Its helper-to-that-fibre length<=3 words are at most two, insufficient for three lifts. This controls only that ordinary three-sheet cover. It does not alone exclude the P3/arbitrary-port model.

The new model is instead excluded by the stronger external-class/helper-distance theorem linked above. The prepared CNF can therefore be mathematically infeasible while its encoding remains exact. No solver UNSAT, UNKNOWN, or candidate graph is asserted. The original geometric family, not arbitrary42-vertex graphs or the general(4,3) problem, is what the paper obstruction closes. There is no resumption of the paused old D2 project.
