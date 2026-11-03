# Residual nonunit-a phases: all18 frames fail

The new prediction was refuted. All18 previously uncovered controller frames fail radius4, missing4..19 of216 states. There were0 coarse passers,0 actual17496-vertex fiber graphs,0 fiber-root BFS and0 new lower bounds. No ordinary bad-pair count or global diameter was measured.

The tested frames have a-phase A in{0,3,6}, b-phase1 and two distinct projected central inverse classes selected from{1,2,3,4}. The exact chart, SL2 matrices, gamma=-x+(2,0,2,2), vertex encoding and native kernel are inherited from `../bphase_route_synthesis/`; these are18 new frames, not repeated tests of its54 frames. Four fiber parity lifts would have been evaluated only after a coarse pass.

For each frame, the complete216-state controller adjacency was traversed to depth4 from the identity, with all8 named darts and all step patterns. Every path in a fiber lift projects to an equally long controller path. Thus one unreachable controller state proves that no parity lift of that frame has D4. Left multiplication makes the controller transitive, but only the one identity-root traversal is needed to reject it.

Missing counts in pair order{1,2},{1,3},{1,4},{2,3},{2,4},{3,4} are:

| A | Missing controller states |
|---|---|
|0|11,10,19,4,9,8|
|3|9,4,11,8,19,10|
|6|19,8,9,10,11,4|

The first frame A0/B1/classes{1,2} has layers[1,8,30,72,94], reaches205 and misses controller14=(SL2 matrix[0,1;2,0], phase5). All18 per-frame layer sequences and first witnesses are retained in RESULT.json. Native CPU was0.000275 seconds, below the1CPU coarse budget; compilation1.123087 seconds; parent plus children1.125929 seconds. The native whole-process hard limit was3CPU. No case is UNKNOWN or untested.

## Why these were the only missing phase classes

The prerequisite paper argument was supplied as VALID by debruijn_check before this numeric run. The unchanged SL2 matrices have no -I word shorter than3. At length3 only bbb/BBB reach -I, giving central phases±3B. At length4 the only such words give±2(A+B). Therefore, with projected plain steps S, the complete≤4 phases at -I are

`{±3B, ±2(A+B)} union ({±3B}+S) mod9`.

If B is divisible by3, the first pair collapses to0, so two distinct projected inverse classes give at most1+4+2=7 phases, below9. No numeric frame is needed for these B values.

For a unit central phase, use multiplication by its inverse modulo9. Its unique odd lift U modulo18 is a unit modulo18, and the controller relabeling `(X,i)->(X,Ui)` sends each global plain power P^e to P^(Ue). Because U is odd, gamma parity and its affine offset are preserved. It also permutes the global inverse-power pairs represented by1..8, including both parity lifts of every projected class. Thus every unit-A case is represented by the earlier54 A1 frames. For nonunitA and unitB, normalize B to1; A remains in{0,3,6}. These are exactly the18 new frames now rejected.

Two power pairs with the same projected inverse class have only S={±r}, giving at most2+4+2=8 phases at -I. One inverse pair plus the P9 matching has S={0,±r} and likewise at most6+2=8. These are paper exclusions, not additional graphs or numeric frames.

Combining these facts with the preceding54-frame result closes the fixed source-operator, m9 family for **all a/b phases modulo9 and the specified two global plain inverse-power pairs**, including repeated projected classes. The P9 matching alternative is also obstructed. This is not an upper bound for arbitrary N(16,4), nor a claim about other moduli, SL2 generators, chart rules or topologies. The family is stopped without a further grid or local repair.

Reproduce this new18-frame pass with `python run.py`. The PREDICTION/MODEL were frozen before execution. No original9720 source all-root BFS, prior54-frame rerun or external review was performed.
