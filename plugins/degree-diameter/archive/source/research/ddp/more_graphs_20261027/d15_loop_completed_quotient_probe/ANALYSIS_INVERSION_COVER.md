# Fixed selfline inversion atoms: exact cover scope

Status: the automorphism, atom costs and full-target cover formulation are valid. This paper performs no numerical check or solver call. It relies on the already certified source affine tables and the parent's saved assertion that every translation c is zero.

For each controller arc the source relation is Q_v(y)=B*x, over F3. Linearity gives Q_v(-y)=B*(-x), so the map i,x -> i,-x preserves every loop-completed directed relation. It also preserves the condition that an entry is a virtual selfloop: both controller and offset agree before the map exactly when they agree afterwards. Deleting these selfentries therefore leaves an automorphism of the actual simple source. Degrees, free status and graph distances are preserved. This proves only source symmetry, not the diameter of an altered construction.

For each specified zero selfline triangle in a loop controller i, the allowed old vertices are (i,0), (i,v_i), (i,-v_i). The two inversion orbits are the singleton Z_i={0} and pair P_i={v_i,-v_i}. They have costs1 and2. All these atoms are disjoint, including between controllers; hence the total weighted cost is exactly the cardinality of the expanded neighbor set, with no multiplicity correction. All atom vertices are actual free pins by the previous source binding.

There are two atoms per specified controller:48 variables for the24 controllers in the15552 source,60 for the30 in the102060 source. This is the complete inversion-invariant neighborhood family within these specified selfline triangles. It is not the family of all inversion-invariant subsets of the648/810 free vertices: each27-point free fiber has additional nonzero inversion pairs away from this one line. It is also a relaxation of choosing exactly five whole selfline triangles. It may take just a zero or just a pair, and use more than five controllers while respecting fifteen total pins.

For target t and atom O, set its cover coefficient to one exactly when at least one p in O has d_G(p,t)<=D-1. Its column is the OR of the existing radius balls of its members, not their intersection. With one binary variable z_O per atom, the exact fixed-family model is

    for every old target t: sum_{O covering t} z_O >= 1,
    sum_O |O| z_O <= 15.

No extra relation between the zero and pair variable of the same triangle is needed for inversion invariance. Requiring them equal would unnecessarily return to the already rejected whole-triangle subfamily. If a cardinality encoder repeats a pair variable twice, both positions represent the same truth value and its contribution must be two when selected; it is not two independent choices.

For any model witness expand its atoms to the distinct old-pin set S. Adding one new point x adjacent to exactly S retains all old edges. Each old pin gains one edge and remains within cap15; x has degree |S|<=15, and the graph is simple. For every old target t, its distance from x is exactly1+d_G(S,t), so full radius-(D-1) coverage is necessary and sufficient for the new root to have eccentricity at mostD. Old-old diameter remains at mostD. Thus a true model witness, followed by full cached-OR and actual degree checks, gives a complete retained-edge extension on this fixed source. Partial coverage, an LP point or solver status without a witness gives no graph.

The earlier cache probes remain separately scoped. All24/30 zero singletons together miss528/300 old targets, so no zero-only subset works. All selfline triangles together cover, but all42504/142506 five-controller subsets fail; this excludes the specified homogeneous nine-helper rule at its zero helper, and also the corresponding five-whole-triangle neighbor choice. Those failures do not settle the larger independently selectable zero/pair model above.

The parent's bounded solver experiment decides only this specified atom domain. A returned assignment requires literal expansion and full-target verification; an interrupted or unknown result is not a family exclusion. No broader free-pin set, other affine coordinate, triangle offset, source modification or helper rule is implied by this paper.

Evidence: affine_relation_recovery/{RESULT.json,ANALYSIS_AFFINE_CERTIFICATE.md}; canonical_zero_port_probe/{PREDICTION.json,RESULT.json}; selfline_helper9_probe/{PREDICTION.json,RESULT.json}. The numerical probes and any later atom-model call belong to their producers; this paper runs zero graph, ball, BFS or solver operations.

Inherited terminal solver outcomes: the48/60 atom models both return raw UNSAT. The same72/90 pins without inversion ties initially return UNKNOWN; one explicitly authorized unchanged-CNF continuation gives restricted72-pin raw UNSAT for D4 and90-pin UNKNOWN for D5. These are producer receipts, with no independent UNSAT proof check. They do not reject the full648/810 free-pin domains and trigger no further experiment here.
