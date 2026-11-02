# Exceptional49 affine g4 resource gate

The315 regular-source domain was bounded by211 full27 affine blocks, with175 sources capable of g4. This finite extension checked only the49 exceptions:28 sources with a self port/P, and21 nonself/noP sources whose M coordinate permutation is nonaffine. The purpose was to decide whether the11 additional g4-capable sources needed for213 full blocks exist. This is a local resource gate, with no global packing solver or graph construction.

## Self-loop correction holds on all28 literal loci

For each self port, its actual loop locus L was read from the saved author-chart analysis. Direct F3 rank and span checks give dim L=3, |L|=27, and dim(L intersect W)=1. The input noise line is that W-line. The literal bases and intersections are in LOOP_GEOMETRY.json.

If H is a3-dimensional linear complement to W, then dim(H intersect L)<=2: equality H=L would put a W-line in H. Every affine coset H+c therefore meets L in at most9 points. Its ordinary raw output is an81-point affine hyperplane; deleting its self loops removes at most9 of those points. Incoming sources at each target are four distinct sources with four distinct noise lines in W; at most one provider is the self source of that target.

Distinct-normal affine hyperplanes intersect in27 points. Removing at most9 points from the self provider leaves a nonempty intersection. Therefore two disjoint ordinary providers must still have the same normal, and that normal kills two distinct lines of W. An output not containing W remains an exclusive ordinary provider even at an exceptional target. The spare matching P only adds load.

For s ordinary providers and binary matching provider x at a target, literal volume requires81s+27x-9<=243, where the subtraction is allowed optimistically even without a self provider. With s in{0,1,2,3,4} and x in{0,1}, this still forces s+x<=3. All364 matching fiber maps were checked to be an involution without fixed points, and each M target is also one of its source's ordinary targets. Thus summing these rows remains valid across all364 sources.

## Stronger cost and its precise logic

Let B count non-W ordinary outputs and Bm count those that are the source's matching port. Each is exclusive at its target. For a bad matching output, the source is itself the M provider at that target, so the row has s+x=2 and loses at least1 from capacity3. For a bad nonmatching output, selecting that target's M mate would create a second ordinary provider there, because every M target is also an ordinary target of the same source. Exclusivity forbids this. Hence x=0, s+x=1, and the row loses at least2. These target rows are distinct, so

    5T + 2B - Bm <=1092,
    sum_selected [13 - 2g(H) - 1_{matching port bad}] <=1092.

Reducing the already evaluated regular729-slope masks gives175 sources of minimum cost5 and140 of minimum cost6. Every minimum-cost g3 witness makes its matching port bad. Thus the sharper cost does not further reduce the previous315-source upper211.

## Complete exceptional g4 gate

For every exceptional source, all729 slope matrices R:F3^3->W were filtered by its four ordinary g=4 linear equations. Exactly28 sources have27 solutions each; the other21 have no slope solution. The latter are complete g4-negative results before any phase test, rather than243 failed local graphs.

For each of the28 positive sources, only the nine canonical affine phases c in W were eligible. Testing stopped at the first locally legal block per source. Across all28 sources154 phase blocks were actually checked. Every saved witness uses27 centers whose complete actual old neighborhoods contain351 distinct vertices, with13 neighbors per center. This includes literal M/P data, self-loop deletion, and edge deduplication. Four ordinary output normals and constants are saved with each witness and kill target W. The only center-neighborhood precomputation was49*243=11907 local records; no88452-point graph or BFS was generated.

The28 positives comprise14 self/P sources and14 nonself/nonaffine-M sources. For example source7, R=[[2,2,1],[2,0,0]], phase0, has324 raw ordinary points,3 deleted loops,27 M points,3 P points, and351 distinct old neighbors. Source13 has the same R and phase0 with no loop/P adjustment and likewise351 distinct old neighbors. Exact center lists and all49 records are in EXCEPTIONAL_SOURCE_RESULTS.json.

## What the necessary gate now says

There are203 g4-capable sources in all:175 regular plus28 exceptional. The other161 may be optimistically assigned cost6 without checking their g3 phase legality. The cheapest215 blocks cost203*5+12*6=1087;216 cost1093>1092. Therefore every packing in this full364-source affine full27-block domain satisfies T<=215, hence clone count<=5805 and final order<=94257.

This upper bound exceeds the213 blocks needed to beat saved14D5=94186. It is not a feasibility result. The earlier proposed requirement of at least11 exceptional g4 sources is met by28 local witnesses, so source-dependent affine geometry remains open. The next unresolved interface is cross-source ordinary hyperplanes: at each target all selected ordinary outputs must share a normal and use different affine layers, with their exact matching/spare images also disjoint. Volume, g4 counts, and isolated local witnesses do not certify that packing.

This batch is closed. It used one worker and0.78853205 CPU seconds, no solver, no source BFS, no complete source graph, no cloned graph, no seed extension, and no pending process. The previous uniform-H terminal and root project state were preserved. Nonlinear or partial W-transversals, different sources, and other clone rules remain outside the stated domain.
