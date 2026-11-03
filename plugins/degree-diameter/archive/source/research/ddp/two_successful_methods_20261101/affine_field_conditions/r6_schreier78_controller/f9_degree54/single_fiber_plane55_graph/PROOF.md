# Complete plane-clone extension:56943 vertices, maximum degree55, diameter3

The complete literal graph is `graph_d55_D3_n56943.edges`, with1539648 edges in global lexicographic order, no header, each undirected edge stored once as a<b. This production scope uses exactly one accepted source and one checked pin rule. It ran no BFS, solver or Lean. Fresh independent acceptance and final formalization are separate obligations.

## Source and exact recipe

The immutable source is `../graph_d54_D3_n56862.edges`, the accepted54-regular56862-vertex F9/C78 graph. Its complete literal/formula binding and all-pairs D3 proof were already independently accepted. This production does not rerun that source's806 BFS roots or its finite-field/controller checks.

In F9=F3[w]/(w²+1), code a+3b means a+bw. Put eta=4=1+w and choose the plane W={(a,b,eta*a):a,b∈F9} in controller fiber0. For j=9*a+b, a outer0..8 and b inner0..8, define

    center_j = old label a+9*b+81*GF9mul(4,a).

Keep all original1535274 source edges and original labels0..56861. Add vertex56862+j with the exact54 old neighbors N_G(center_j), with no new-new edges. Thus the new graph has56862+81=56943 vertices and1535274+81*54=1539648 edges. `PARAMETERS.json` and `ORDERED_PINS.tsv` fix the literal order and all54 pins per clone.

## Why the pin sets are disjoint

The preproduction interface in `../single_fiber_plane55_interface/PROOF.md` proves and actually checks the concrete plane. The square set of F9 is{0,1,2,3,6}, so eta=4 is a nonsquare. The plane normal(8,0,1) pairs with the six actual port directions to(1,8,6,6,7,7), all nonzero. Therefore W avoids all six port lines except at0.

For a source dart p out of controller0, two old fiber coordinates x,y have a common neighbor over that dart exactly when x−y lies in its source port line: invert the actual dart matrix and use its exact direction transport. Different ports lead to different controller fibers. Hence the81 complete source neighborhoods are pairwise disjoint. Their4374 pins exactly partition the729 vertices of each of the six neighboring controller fibers[2,24,26,52,31,62].

Production additionally binds the finite interface to the actual accepted source edge file: it reads all1535274 old edges and reconstructs each of the81 centers' literal54-neighbor set. All81 sets equal the declared pins exactly. It then retains every parsed old edge and appends precisely4374 clone incidences.

## Degree and current-prefix spare checks

All source degrees are54. Since all4374 pins are distinct, each old pin is used exactly once and goes from degree54 to55; all other old vertices stay54. Every new clone has exactly54 neighbors. The actual final histogram is

    degree54:52569 vertices; degree55:4374 vertices.

No center in fiber0 is itself a pin, since every pin is in a neighboring controller fiber. At each actual insertion the new54 pins are still unused and all have current degree54. The production program checks this prefix-by-prefix and records all81 rows in `PREFIX_LOADS.csv`. Thus the maximum degree bound holds throughout the sequential construction, not only in the final graph.

## Current full radius2 coverage, including previous clones

Suppose clones0,...,j−1 are already present. Put S=N_G(center_j). For every old target y≠center_j, a source shortest path from center_j to y has length at most3; deleting its first edge leaves a path of length at most2 from some member of S to y. For y=center_j, use any member of S and its old incident edge.

For an earlier clone i, the two source centers are distinct and in the same controller fiber, so they are not adjacent. The pin packing says they have no common old neighbor. Their source distance is therefore exactly3. Choose a source path

    center_j — a — b — center_i.

Then a∈S, b∈N_G(center_i), and `a — b — clone_i` is a current two-step path from S to that earlier clone. All interior vertices are old source vertices; no future clone is used. Consequently S has full current radius2 coverage, and the inherited retained-edge extension lemma applies at every one of the81 actual steps.

The final graph therefore has diameter at most3. Its order56943 exceeds the cap55 radius2 Moore bound1+55+55*54=3026, so its diameter is exactly3. The conclusion is a genuine all-pairs path argument, not an extrapolation from sampled BFS roots.

## Falsifiable distance prediction for fresh acceptance

The accepted source's saved BFS data already contain all81 selected source centers, each with histogram(1,54,2476,54331). No source BFS is rerun here. For a new clone, the old center appears at distance2, and all old source distances through its pin set coincide with those from the source center, apart from replacing the root and this center. No other clone can occur at distance2 because pin sets are disjoint; all other80 clones occur at distance3. Thus every one of the81 new roots is predicted to have histogram

    (1,54,2477,54411).

The producer does not claim to have run those BFS checks; they belong to the fresh independent validator.

## Public comparison, scope and execution

The root completed the bounded public55 gate before authorizing this production. The best-located published-source guarantee is56375=33825+22*1025;56943 exceeds that guarantee by568. No global highest-order or priority certification is claimed. See `../../../../public_baseline_audit/DEGREE55_SINGLE_FIBER_TARGET_GATE_20261101.md`.

The single-fiber full-neighborhood capacity bound81 is attained: each center consumes9 vertices in a fixed729-vertex neighboring fiber. This is not a whole-source optimum, a bound for arbitrary pin sets, or an upper bound on N(55,3). No other plane, source fiber, degree, controller or field was tried.

The actual single-worker preparation, compile, complete source/pin binding, edge production and aggregation used1.242568592CPU seconds, below the30CPU cap. Both compile and generation exited0; all local processes are terminal. The only complete graph created is this56943-vertex extension. `RESULT.json` and `TERMINAL.json` preserve the actual checks and measurement boundary. No hashing or installation was performed.
