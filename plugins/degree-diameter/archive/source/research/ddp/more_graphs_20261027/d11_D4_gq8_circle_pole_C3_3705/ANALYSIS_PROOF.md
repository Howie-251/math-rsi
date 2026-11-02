# General diameter5 bound and the one q8 control

Use the actual generalized quadrangle W(8), its chosen spread, three cyclic incidence sheets, a K3 on each old-line fiber, and three twins for each spread line. Each twin has exactly the point-neighborhood of its corresponding old-line copy, and each triple of twins is a separate K3. No point matching or point clique is assumed for this q8 model.

For arbitrary incidence voltages, near same-part and point-line pairs are within4: collinear points and same-base point copies can change sheet through a line clique; nonincident point-line pairs use a base3-incidence path plus one line-clique correction. A twin-to-point path uses the twin clique first to choose the necessary starting sheet, then at most3 incidence steps, giving at most4. Same-base twin-to-line pairs use a shared point and the old-line clique, at most3.

The only remaining opposite same-part cases have a base4-incidence geodesic. Lift any one such path and correct its final sheet by inserting a line-clique step. For point-point paths use an intermediate line; for old-line/twin endpoints use the available endpoint clique, replacing an old-line endpoint by its twin without changing either incident point edge. This costs at most5. Different spread lines are disjoint, so this argument also covers their twin pairs. Hence the whole graph always has diameter at most5 for every voltage function; no uniform-function assumption is needed.

For the displayed four-incidence path S0,p,M,q,S_infinity, with point-to-line voltages tau, the directed voltage is exactly

    -tau(p,S0)+tau(p,M)-tau(q,M)+tau(q,S_infinity) mod3.

The source has9 such geodesics. The observed histogram[2,3,4] means this one line-pair's phases cover all C3 and all sheets of that pair, including the copied twin endpoints, have4-step routes. It is not a test of every opposite line/point pair and is not a diameter4 certificate.

Here v=(8+1)(8^2+1)=585, and the spread has65 lines. The order is3*(2*585+65)=3705. The1755 point copies have degree10; the1950 line/twin vertices have degree11. The edge count is3*585*11+3*65=19500.

The sole actual control is simple with maximum degree11 and has a complete root0 radius4 miss of19 targets, first220=(point73,sheet1). The general upper bound5 above therefore proves exact global diameter5. The individual9-phase prediction is supported, while the complete diameter4 prediction is refuted. This is one fixed circle/pole control, not an exclusion of other poles, voltage functions or three-sheet models. No independent graph/BFS, alternative pole or numerical field test was run for this proof.
