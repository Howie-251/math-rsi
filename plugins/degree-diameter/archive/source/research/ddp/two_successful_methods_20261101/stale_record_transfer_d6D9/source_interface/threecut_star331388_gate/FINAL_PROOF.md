# Final old-route obstruction for the fixed331387 source

This connects the actual completed `OLD_RESULT.json`/`OLD_RAW_RESULT.json` to the paper interface. It does not rerun their edge scan, masks, critical pairs, source support/count DP, graph, BFS or solver. The last section is a paper corollary wider than the numerically filtered matching-cut pool; its extra scope is not represented as another experiment.

## Actual inherited source and critical-pair meaning

The source is the fixed Rodriguez–Canale331387-vertex,994161-edge,6-regular diameter-nine graph. Work in its already bound RIGHT Cayley recipe, with generators in the three inverse pairs and positive representatives

s0=(25,1254), s1=(18,541), s2=(47,4642).

Left multiplication is the source automorphism used below. The author-left/working-right inversion convention, labels6763*j+n and actual group law are fixed in `HISTORY_SOURCE_GATE.json` and `PAPER_INTERFACE.md`.

For the canonical first cut{e,s_i}, the profile has a set K_i of actual critical old pairs(u,v): d(u,e)=4, d(s_i,v)=4, d(u,v)=9, with all source9-geodesics through that cut. The exact shortest-count factorization and orientation proof are in `PAPER_INTERFACE.md`; the original arrays and profile results are retained. The three K sizes are32,21,32.

Define V_i(x) to contain a critical pair bit exactly when x lies in B3(u) union B3(v). An additional old edge f={a,b} has hit mask M_i(f)=V_i(a) OR V_i(b). For a three-cut/six-star candidate retaining all other old edges, the other four pins repair each critical pair exactly when they hit that radius-three union. Therefore two other cuts must have mask union ALL_i. This condition is necessary for diameter≤9 even though the K_i list is not a full seam enumeration.

## Actual complete edge-scan bounds

For each first type the finite owner scanned all994161 undirected source edges through the three positive generator parameters. It first excluded the11 edges incident to e or s_i, before grouping. The remaining994150-edge pool is exactly the pool of possible other edges for a vertex-disjoint first cut.

| First type | Critical obligations | Eligible mask classes | Zero-mask edges | Maximum hit by one eligible edge | Twice that maximum |
|---|---:|---:|---:|---:|---:|
|0|32|431|940914|11|22|
|1|21|203|956564|7|14|
|2|32|419|939533|12|24|

In every row twice the maximum is strictly smaller than the number of obligations. Any two edge masks have union cardinality at most the sum of their cardinalities, so no two eligible edges can cover ALL_i, even before disjointness between those two edges is considered. The actual computation therefore performed zero maskpair OR checks and zero representative-edgepair checks: all maskpair possibilities were rejected by the strict bound. It did not rely on sampling or on a later failure of a candidate graph.

The twelve-representative completeness lemma remains valid as the prepared general gate (`PAPER_OLD_OBLIGATION_GATE.md`), with zero classes and same-class pairs included, but it was not numerically needed for this actual negative result. The stricter measured max-hit bound already settles the entire necessary edge-pair question.

## Complete NO for three disjoint cuts

Every undirected source edge is a left translate of one of the three positive representatives, after reversing it if necessary. Take any hypothetical successful three-disjoint-cut/six-star candidate and select any one of its cuts. Left-translate the whole old source and pin set so that this first cut is{e,s_i}; fix the new star vertex. Its two other edges are eligible and must jointly hit every critical pair in K_i. The complete bound above makes that impossible.

Thus this fixed source has no degree-six, diameter-at-most-nine extension by deleting three vertex-disjoint old edges and adding one vertex adjacent to their six endpoints. The actual new graph count is zero. The cumulative numerical case terminal is4.575818955/20CPU seconds. The last edge-mask gate made no new BFS/DP/field/source-D9 validation; the earlier single identity support/count export is separately recorded in the profile stage, not described as zero work. No normal-shift search, complete seam verifier or candidate BFS followed this necessary obstruction.

## Paper dominance extends the bound to every old edge

For any critical pair, the first-cut endpoints have distances4 and5 to its two ends. Therefore

V_i(e)=V_i(s_i)=0.

An excluded source edge other than the first edge has the form{e,x} or{s_i,x}, with x outside{e,s_i}. Its mask is just V_i(x). Because the source is simple6-regular, x has at most two neighbors among the two first-cut endpoints, and hence at least four incident edges{x,y} with both endpoints outside that first pair. Each such edge is eligible and has mask

V_i(x) OR V_i(y) containing V_i(x).

The first edge itself has zero mask. Consequently every source-edge mask, including the eleven excluded edges, has hit count at most the corresponding eligible maximum11,7 or12. This uses no new scan or data values. In fact the eligible pool is already a subset of all source edges, so the maxima agree, but only the upper bound is needed.

## Broader pure-star corollary: at most three arbitrary cuts

Let F be any nonempty set of at most three distinct source edges, now allowed to share endpoints. Put P equal to all their endpoints, so |P|≤6. Form the full-star graph J by deleting F and adjoining one new vertex z adjacent to every point of P, with no other edge changes.

This is a legitimate maximum-degree-six graph: every old endpoint x has degree6−deg_F(x)+1≤6, every nonendpoint retains degree6, and z has degree|P|≤6. No regularity or disjoint-cut assumption is needed for this corollary.

Choose one edge of F as the first cut and left-translate it to canonical type i. The first two pins hit no K_i bits. There are at most two remaining edges, and by the dominance argument each has hit count at most the measured m_i. Their union hits at most2m_i<|K_i|. Some certified critical pair(u,v) is therefore unhit by every endpoint in P.

Its nearest-pin source distances are exactly4 and4: the first edge supplies those upper bounds, while absence of a hit rules out distance≤3. The distance-from-P lemma d_(G−F)(P,x)=d_G(P,x) uses only that deleted edges have both ends in P and remains valid when cuts share endpoints. Its star route therefore has length10. Every source9-geodesic uses the first cut, which was removed, so G−F has no old route of length≤9. The pair has distance10 in the full-star graph. Thus J is not diameter≤9.

Any candidate with new neighborhood N⊆P is a subgraph of this full-star graph on the same vertices and has no shorter distances. It cannot repair the failed pair. In a maximum-degree-six one-point extension with only old-edge deletions, every new neighbor must belong to P anyway, because an untouched old vertex still has degree6. The empty-cut case cannot connect the new vertex at this cap.

Therefore the obstruction covers **all modifications of this fixed source obtained by deleting at most three old edges and adding one new vertex with any neighborhood among their endpoints**, even with repeated cut endpoints and nonregular final degree distributions. No old vertices are removed and no old–old edges are added. The full-star supergraph is degree-legal for |F|≤3, so the monotonicity comparison stays inside the intended maximum-degree scale.

## Exact stopping scope

A successful one-point pure-deletion/star modification of this same source would have to delete at least four old edges, or change the allowed rule (for example by adding old–old repair edges). This is a necessary rule-change statement, not an authorization or evidence that either alternative succeeds.

The proof does not cover additional old–old repairs, arbitrary one-point rewiring, multiple new helpers, deletion of old vertices, another source, or general N(6,9). Added old–old edges could create routes absent from the source geodesic/star decomposition and lie outside the monotonicity comparison. The source is a published inherited object, not a new portfolio graph. This paper corollary is attached to the same mechanism node, with no new experiment/method/graph/parameter/Lean or priority claim. All old predictions, source/profile boundaries and unused seam interface remain intact as historical evidence.
