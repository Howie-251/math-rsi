# Degree11 common-old-anchor block: all210 frozen pairs fail

The proposed shared-anchor construction has no complete extension in its fixed finite scope. All210pairs of the21unused degree-legal Qline pinsets were checked against all315 old vertices of degree at most9, for66150 complete anchor tests. Every pair passed the old-pin degree check; none had a shared anchor satisfying the full coverage condition. The entire producer used0.500147 CPU seconds. No candidate graph, new lower bound, solver call or full-source BFS was produced.

The source is the independently verified37631-vertex,205329-edge graph, with maximum degree11 and diameter5. Keep every source edge. For two distinct frozen10pin Qline neighborhoods A,B, add distinct new points z,w with neighborhoods A union{h} and B union{h}, where h is an old vertex outside A union B of degree at most9. There is no edge zw. Both new degrees are11 and z,w have distance2 through h. Each other old pin must have enough degree for its multiplicity in A,B; this is checked exactly. The target would be37633vertices and205351edges.

Let Rk(S) denote the closed radius-k union in the fixed37631 source. The exact new-to-old condition is

    R4(h) covers M,
    M = (V minus (R4(A) union R2(B)))
        union (V minus (R4(B) union R2(A))).

Indeed a path from z to an old target that avoids w uses A or h followed by at most4 source steps. If it uses w, replace its prefix by the length2 path z-h-w; after leaving w it has at most2 source steps left, giving R2(B) or R2(h). The latter is already contained in R4(h). The reverse implication uses those explicit paths. The same argument applies to w. Old-to-old diameter stays at most5 and z,w have distance2, so the condition is both necessary and sufficient for this exact construction.

The21 frozen neighborhoods are the canonical pins-lexicographic indices0..23 excluding the already used3,17,21. Their actual-current37631 R4 missing sets and R3 distance rows were reused from h9_d11_two_qline_block/cache_metadata.json and line_R3_rows.u8.bin. Metadata source order37631 and edge count205329 were checked, as were the canonical pool indices and all current pin degrees. Closed R2 unions come directly from distance<=2 in those exact current R3 rows; no new line-ball BFS was needed.

The315 anchor R4 rows were recovered from the original37628 coverage cache by three exact append updates, not reused unchanged on a larger graph. For an appended point z with neighbor set S, put k=d_old(a,S). An old radius4 ball gains R_(2-k)(S) when k<=2 and gains z when k<=3. This is exact because a path through z between old endpoints has length at least k+2+d_old(S,target); conversely those source paths and the two new edges realize every included target. Applied sequentially, the formula includes all interactions with previously added vertices. Each update computed only the required bounded multisource depth3 data. After all three updates, every adjacency row was compared with the actual verified37631 source. cache_binding.json records the literal update neighborhoods and cache paths.

Each pair forms its exact missing set M once. Every old anchor of degree at most9 outside the pinsets is then tested for complete containment M subset R4(h). All315 candidates were eligible for each pair, yielding210*315=66150 tests. run.py records each pair and its failure; RESULT.json and terminal.json preserve the exhaustive finite terminal state. The prediction was frozen before the pair tests in PREDICTION.json.

This closes only the common-single-old-anchor rule on these frozen21 line neighborhoods and this fixed source. It does not exclude different line pools, different source graphs, different anchors for the two points, an edge between the new points, larger blocks or arbitrary degree11 constructions. No such extension was attempted in this batch. There were no additional rounds or continuation after the210pair limit.
