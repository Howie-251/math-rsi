# Exact girth>=5 subfamily and route budget

Verdict: **VALID**. Restricting both internal matchings to noncollinear pairs and adding the6480 mixed-rectangle clauses defines exactly the girth>=5 subfamily of the original arbitrary-two-perfect-matchings construction. The filtered coverage clauses remain exact for D<=3. The actual [worker.py](worker.py) was read once for remapping and witness semantics; no numerical computation, graph, solver, or BFS is run by this review.

The unchanged source is W(3,3) with40 points,40 lines,160 incidence edges, incidence degree4 and girth8. Add one perfect matching P of the points and one Q of the lines. The full target has80 vertices,200 edges, degree5. The [original model proof](../../../breadth_20261027_wave11/gq80_paired_matchings/REPORT.md) and [previous direct-CNF review](../direct_cnf_20261028/ANALYSIS_CNF_REVIEW.md) are inherited rather than regenerated.

## Triangle and four-cycle restrictions are necessary and sufficient

A triangle has either zero or two incidence edges. Three edges in the internal matching alone cannot form a triangle. With two incidence edges, its remaining edge joins two collinear points, or two intersecting lines. Thus forbidding precisely the collinear same-side matching variables is exactly the triangle-free restriction.

Each old vertex has27 noncollinear choices. There are540 allowed internal edges per side, giving1080 variables. The80 perfect-matching equations now have27 choices each, still describing arbitrary perfect matchings within this restricted edge set; none is fixed.

A four-cycle has zero, two, or four incidence edges. The source has no four-cycle, and a matching alone has none. With two incidence edges, two matching edges on the same side would force an immediate return through the same unique matching neighbor, rather than a simple four-cycle. Hence every genuine new four-cycle uses one P edge and one Q edge in alternating order:

    p --P-- q --incidence-- M --Q-- L --incidence-- p.

It exists exactly when both P_pq and Q_LM are selected and p is incident with L while q is incident with M, or with L,M swapped. Therefore each mixed-rectangle prohibition is exactly the binary clause not(P_pq) or not(Q_LM).

For a nonintersecting line pair L,M, its16 cross point pairs contain exactly four collinear pairs: each of the four points on L has exactly one point on M collinear with it. The remaining12 are allowed P variables. The540 allowed Q edges therefore give540*12=6480 distinct P/Q prohibitions. A selected P/Q pair determines its rectangle uniquely because L,M are disjoint. These are all the four-cycle prohibitions; they do not impose another hidden matching restriction.

Thus triangle-free matching choices plus these clauses are equivalent to girth>=5 for this template. Indeed any selected noncollinear P edge closes an old incidence geodesic of length4 into a five-cycle, so every completed graph satisfying these restrictions actually has girth exactly5. This does not imply D3.

## The filtered29-literal far-pair clauses remain complete

For an old same-side far pair x,y, the two own-side route families each initially contain13 variables. Exactly four of each family are collinear and have now been set false, leaving9+9 choices with the common variable xy counted twice. Hence there are17 distinct own-side variables.

The16 opposite-side relay choices consist of lines incident with x paired to lines incident with y. Exactly four line pairs intersect, one through each common collinear point of x,y, and are now forbidden. Thus12 relay variables remain and each far clause has17+12=29 literals. The dual line-side calculation is identical.

All1080 original far-pair clauses are retained after substituting false for the deleted variables. Cross-side pairs still have original incidence distance at most3, and same-side collinear pairs at most2. Under the matching equations, the only remaining path types are matching-first, matching-last, and opposite-matching-middle. Therefore the29-literal rows are still equivalent to D<=3 in this restricted family; they are not a sampling of targets or a relaxed coverage test.

The complete CNF counts are80 ALO clauses,80*C(27,2)=28080 pairwise AMO clauses,1080 positive far clauses, and6480 negative rectangle clauses:35720 clauses on1080 variables. No fixed edge, symmetry condition, or additional cardinality cut is part of this batch.

## Why the new constraint has a positive routing rationale

In a simple5regular graph of girth at least5, every root has five distinct neighbors and20 distinct second neighbors, with no collisions with earlier layers. Its closed radius2 ball therefore has size26. A D3 graph on80 vertices must supply the other54 vertices in the third layer. This protects the first two layers from the triangle/four-cycle losses allowed by the original model; it is not a full third-layer coverage guarantee.

A sharper necessary budget is available without changing this batch. Fix a point x, and let y=P(x), necessarily noncollinear with x. Among the27 old far points of x, y is already its matching neighbor. Consider the remaining26. The own-first routes through y can reach exactly eight of them: C(y) minus C(x) has nine points, one of which is y.

Let Sx=C(x) minus {x}, the12 old collinear neighbors. Let a_x be the number of selected P edges having both endpoints in Sx. Of the12 images P(Sx), exactly2*a_x remain inside Sx; none can be x or y because x is matched only to y. Consequently own-last routes contribute exactly12-2*a_x distinct old-far endpoints other than y.

The four opposite-side relay lines contribute at most12 old-far endpoints. None can be y: a relay from x to y together with the selected xy edge would be one of the prohibited four-cycles. These three route families must cover the26 remaining far points, so

    26 <= 8 + (12-2*a_x) + 12,
    a_x <= 3.

This is a pointwise necessary condition, not an average or a sufficient covering criterion. There are54 possible noncollinear edges inside Sx, since its four groups of three points on the lines through x have every cross-group pair noncollinear. The dual line-root condition also holds. The resulting at-most-three constraints are not added to this CNF, and this review does not evaluate them or propose another solver call.

## Actual remapping and terminal boundary

The worker filters original variables by the cached closed-collinearity relation, assigns dense DIMACS IDs1..1080, and stores the explicit map in [VARIABLE_MAP.json](VARIABLE_MAP.json). Degree and cover rows are mapped through old_to_new. SAT decoding maps each true DIMACS variable back through its original_variable_id; it does not mistakenly use the previous full-model old-ID-plus-one convention after filtering. The line-side export correctly adds40 to vertex IDs.

On SAT, the code checks all35720 literal clauses, all original80 degree and1080 coverage rows, all rectangle prohibitions, and the existing3120 overlap cuts. The constructed graph is checked for degree5, no triangles, no common-neighbor pair of size2, and closed radius2 size26. These local checks are consistent with the encoding; a first positive would still receive the parent's independent complete D3 check.

[MODEL_STATS.json](MODEL_STATS.json) records the expected1080 variables,27 choices,29-literal clauses and6480 unique rectangles. The producer's [RESULT.json](RESULT.json) reports one normally completed30-second call with UNKNOWN, no witness and no graph. That is not UNSAT and does not refute even this restricted family. A hypothetical raw UNSAT without a checked proof would likewise remain uncertified; it could not exclude the unrestricted original family in any event.

This review's scope is encoding, geometry, and route reasoning only. It runs zero graph generation, BFS, word enumeration, or solver calls. The evidence belongs to the existing GQ80 mechanism as a restricted-family variant, not a new independent construction method.
