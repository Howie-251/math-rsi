# Six fixed source fibers give486 disjoint full neighborhoods

This is an actual finite interface PASS for the accepted original56862-vertex,54-regular F9/controller78 graph. It does not produce a new complete graph or Lean instance. `PRED.md` was saved before the computation. The fixed selection is U=[0,1,2,3,9,15]; no alternative controller set or packing optimum was searched.

## Actual controller and chart checks

The36target controller labels are all different:

| Source u | p0 | p1 | p2 | p3 | p4 | p5 |
|---|---:|---:|---:|---:|---:|---:|
|0|2|24|26|52|31|62|
|1|3|25|27|53|32|63|
|2|4|0|28|54|33|64|
|3|5|1|29|55|34|65|
|9|11|7|35|61|40|71|
|15|17|13|41|67|46|77|

All selected source labels lie below26, and their six actual dart-chart indices are exactly[0,1,2,3,4,6], matching controller0. Consequently the actual coordinate map on each selected fiber and port is precisely the existing55plane map

    L_p(a,b,t) = T_p*(a,b,4*a) + t*ell_reverse(p),

with GF9multiplication. The six literal inverse matrices are read from the already compiled `F9PlaneClone55.pinInverse` definition. Its unconditional `pinInverse_left` theorem makes every L_p injective; its existing theorem was not recompiled. The finite task also checked all26244new pin inverse readbacks against(a,b,t).

## Ordered centers and full-neighborhood packing

For uIndex=0..5, a=0..8, b=0..8 in that nested order, take

    baseIndex = 81*uIndex+9*a+b,
    center = (U[uIndex],(a,b,GF9mul(4,a))),
    oldLabel = 729*U[uIndex]+a+9*b+81*GF9mul(4,a).

These486distinct labels appear in `CENTERS.csv`; the order is the stated coordinate order, not numerical sorting. `PINS.csv` lists all54original-source neighbors per center, port outer and noise inner. The accepted source `adj_iff_forward` and exact54degree theorem identify these54distinct forward images with the full immutable original neighborhood, without reading an edgefile.

Suppose two proposed pins coincide. Their controller labels first coincide. Injectivity of the36-entry controller double index forces the same uIndex and port. Applying the reused inverse map then forces equal a,b,noise, and hence the same base center. Therefore the486full neighborhoods are pairwise disjoint. For each of the36target fibers,81centers times9noise values give729distinct coordinates, so each such fiber is covered completely. The direct finite check confirms all26244pins are distinct and explicitly checks every coordinate0..728in each target fiber.

Centers are not assumed independent. The finite pin rows contain162source edges between centers; this does not affect the disjoint-neighborhood argument. In particular, no step may replace an immutable54-neighbor source row by an evolving center neighborhood containing earlier clones.

## Exactly two copies and the conditional cap56 target

Use two copies, with copy outer, cloneIndex=486*copy+baseIndex and proposed new label56862+cloneIndex. Each clone connects only to its center's54original-source neighbors. The972ordered center/new-label rows are in `CLONE_RECIPE.csv`; no new-new edge is included.

The direct load check covers every56862source label. The26244used pins have load exactly2; the other30618source vertices have load0. Thus any later complete production preserving the accepted source exactly would have

    n=56862+972=57834,
    m=1535274+52488=1587762,
    degree54:30618old+972new=31590,
    degree56:26244old,
    new-new edges=0.

At every prefix, old loads are bounded by their final value2. For copy0/1, each newly used pin has degree54+copy before its insertion and55+copy after it; distinct base neighborhoods do not interfere.

The already closed arbitrary-center full-neighborhood clone Walk lemma applies to every prefix and to the final graph. It allows repeated and adjacent centers. Explicitly, for an earlier clone with the same center, any proposed pin reaches it in one edge. If centers are adjacent, the old target center itself is a proposed pin and reaches the earlier clone in two edges through the other old center. A source center-distance3path supplies a two-edge pin-to-clone route; distance2gives a common pin. Old targets follow by removing the first edge of a source Walk of length at most3, with the center itself handled by any source neighbor. All intermediate endpoints are old source vertices. This proves the current pin-radius2coverage conceptually, not by BFS. The collapse map preserves old-old bounded walks and inherits source nonD2.

## Execution and limits

`precheck.py` returned `PASS_FIXED_SIX_U_PLANE_PACKING_AND_DOUBLE_LOAD_INTERFACE` in0.182565measuredCPU seconds, one worker, below10CPU. It read only small parameter, declaration and receipt files and wrote the three local recipe tables. It read0large edgefiles, generated0complete graphs, and ran0BFS, solver or Lean jobs. The original source and55formalization remain unchanged.

No claim is made about maximum packing in the whole source, arbitrary pin rules, another U, another degree, or public priority. Public56comparison remains root's separate pending primary-source gate. This local PASS does not authorize production or alter accepted counts; `TERMINAL.json` records the task complete with no active process.
