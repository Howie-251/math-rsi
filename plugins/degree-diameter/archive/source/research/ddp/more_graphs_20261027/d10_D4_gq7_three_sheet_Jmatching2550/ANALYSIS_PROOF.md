# Conditional three-sheet GQ coverage lemma and the actual J control

## Exact hypotheses and degree count

Take a generalized quadrangle of order(q,q), with v=(q+1)(q^2+1) points and the same number of lines, and an actual spread S of q^2+1 pairwise skew lines partitioning the points. Give every point-line incidence an arbitrary directed voltage omega(p,L) in Z3; its lift joins P_p^s to L_L^(s+omega). Reverse steps subtract the voltage.

Join the three copies of each old line into K3. For every spread line L add three twins T_L^s, with exactly the same point neighbors as old line copy L_L^s, and join the three twins into a separate K3. There are no direct old-line-to-twin edges. Then n=3(2v+q^2+1). Point copies have degreeq+2; old lines and twins have degreeq+3. The edge count is3v(q+3)+3(q^2+1).

The proposed sufficient condition is: for every two noncollinear base points, and separately for every two disjoint base lines, the voltages of their q+1 four-step incidence geodesics cover all Z3. Both sides are required. A successful point-side test alone does not establish the line/twin classes. This is a hypothesis on the actual voltage function, not a property inferred merely from using norms or RREF coordinates.

## Coverage by pair type

- Two copies of one point are at distance at most3: point, adjacent line copy, line-fiber clique edge, target point copy. Collinear distinct base points use their common line and the same adjustment, also at most3. Noncollinear points use the four-incidence geodesic condition, at most4 for every sheet pair.
- Copies of one line are adjacent. Distinct intersecting lines use their common point and, if necessary, one line-clique edge, at most3. Disjoint lines use the line-side four-geodesic condition, at most4.
- A point and incident line need at most2. For a nonincident point and line there is a base3-step incidence path; lift it and adjust the final line sheet by one clique edge, at most4.
- A twin and point on its spread line need at most2, by first changing the twin index in its own K3 if needed. For a nonincident point, choose the starting twin index giving the required endpoint sheet of a base3-step line-to-point path. One twin-clique step followed by that path costs at most4. An old-line clique edge must not be silently treated as a twin-to-old-line edge.
- A twin and an old line of the same base line need at most3 via a shared point and the old line clique. For different intersecting base lines, replace the start of the corresponding2-incidence path and adjust the old-line endpoint, at most3. For disjoint lines, replace the first endpoint of the pure4-incidence geodesic; the line-side condition gives at most4 without another clique step.
- Twins on one spread line are adjacent. Distinct spread lines are disjoint, so their pure4-incidence geodesics cover all sheets under the line-side condition. Replacing both old-line endpoints by twins preserves length4 because their point-neighborhoods are exactly copied.

This exhausts all vertex types. Therefore the proposed geodesic-voltage condition is sufficient for diameter at most4. It does not claim that every voltage function satisfies the condition, nor that failing it excludes every graph with additional shortcuts.

## General upper bound5 without that condition

For any voltage function, every base4-incidence path can be lifted and its sheet difference corrected by one line-clique step. For point-to-point paths insert this step at an intermediate line. For line/twin endpoints, correct at an available line/twin endpoint clique. All the near and mixed-type routes above remain at most4. Hence the base construction always has diameter at most5, independent of any phase-cover condition. Added edges preserve this upper bound.

## The actual q7 J matching

For q7, v400 and |S|50, the graph above has2550 vertices and12150 edges, with1200 point copies of degree9 and1350 line/twin copies of degree10. The actual extra rule joins each point copy to its same-sheet J partner. The supplied coordinate check gives J(a,b,c,d)=(3b,a,3d,c), J^2=3I, and3 is a nonsquare modulo7; hence J has no fixed projective point and is an involution on those labels. It preserves the symplectic form up to scalar3. The600 matching edges produce a simple10-regular graph with12750 edges. These coordinate/model facts are inherited from the producer and expert checks; no additional numerical audit was run here.

If B(Jp,r)=0 for an opposite point pair, a J step followed by two incidence steps and a line-clique sheet adjustment reaches every sheet pair within4. Likewise M intersect J(L) nontrivially gives a line-to-line J shortcut with endpoint sheet adjustment. But J preserves every spread line setwise, so those observations do not automatically cover opposite spread-line/twin classes. They are partial geometric guarantees, not a complete diameter proof.

For an opposite point pair p,r with B(Jp,r) nonzero, the ordinary4-incidence geodesic phase set is in fact decisive. A route with one J edge and total length at most4 would require Jp collinear with r, or p collinear with Jr; these conditions are equivalent here and are excluded. Two J edges with two incidence steps would require Jp collinear with Jr, hence p collinear with r, also excluded. Consecutive J edges cancel projectively. With no J edge, a four-step point-to-point route uses two intermediate line-like vertices. Replacing a spread-line vertex by its copied twin changes no phase, and using a line/twin clique in only four steps forces collinear endpoints. Thus the remaining opposite-pair routes have exactly the original four-geodesic phase values, possibly duplicated by twins. This is a conditional route classification, not a new voltage computation.

## Actual terminal and scope

The one actual2550-vertex control has exact global diameter5: producer roots0..5 passed radius4, but root6 missed70 targets, first171. The general upper bound5 above turns that actual radius4 miss into exact5 without another graph BFS. The predicted geometric J-repaired opposite-pair class count9800 was supported; the full diameter4 prediction was refuted. No independent negative-case BFS or further seed/voltage was run.

A norm/RREF counterexample to the geodesic phase condition refutes that particular assignment, not the sufficient lemma or every possible three-sheet voltage construction. The target(10,4) and its2550 order remain conditional goals rather than a new bound. The q8 variant is not being executed. This file supplies proof and scope only; no graph, reflection or voltage search was performed by its author.

A subsequent exact subfamily result is recorded in [RREF_J_UNIFORM_F_CLOSURE.md](RREF_J_UNIFORM_F_CLOSURE.md). For the fixed RREF coefficient convention and fixed J, a single uniform coefficient function f gives only two possible phases on the eight geodesics of the displayed unrepaired opposite point pair. Combined with the short-route classification above and the general upper bound5, this closes that entire uniform-f/RREF/fixed-J template at diameter5. It is a mathematical family conclusion, not additional generated graphs or tests. Arbitrary incidence-by-incidence voltage functions and other J/spread rules are not excluded by it.
