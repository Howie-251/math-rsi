# Given U7attains the complete-plane/base0bound

The one given refinement U7=[0,1,7,9,15,18,24] passes the finite interface. It has42distinct neighboring controller labels. All seven source fibers use the same six actual chart indices[0,1,2,3,4,6]as controller0, so the already proved55plane inverse maps apply unchanged. The567ordered centers in those fibers have30618distinct original-source N54pins, exactly42complete729-point target fibers. Repeating each base neighborhood twice gives1134clone rows,61236new incidences, and source load0:26244,2:30618. The conditional cap56target is57996vertices/1596510edges, with degree54:27378anddegree56:30618. No complete U7graph is produced here.

## Exact base0collision predicate

For a base0controller label u modulo26, the six open-neighbor labels occupy three base layers as

    base0: u+2,u−2;
    base1: u,u+5;
    base2: u,u+10.

Hence for distinct u,v, the two open-neighbor sets intersect exactly when v−u is±4,±5or±10 modulo26. The finite check confirms this equivalence for all325distinct base0pairs using the actual declared controller table; it does not enumerate alternative controller subsets.

Since5⁻¹=21 modulo26, put k=21u. The forbidden differences become±1,±2,±6. The given seven k-points are[0,3,7,10,14,17,21], with cyclic gaps3,4,3,4,3,4,5. Their differences avoid all six forbidden values. Multiplying by5and sorting returns exactly the stated U7.

## At most seven base0fibers

For a set of at least8k-points with forbidden differences±1and±2, every cyclic gap is at least3. Nine or more points would force a total gap sum at least27, exceeding26. For exactly8points, the8gaps sum26, so there are only two excess units beyond the baseline all-3sum24. Therefore either one gap is5or two gaps are4, and all remaining gaps are3.

In either case at least6of the8gaps are3, and at most2are not3. If no two3-gaps were adjacent around the cycle, each3-gap would require a different non-3gap as its successor. That would give at most2gaps equal3, a contradiction. Thus two adjacent gaps are3+3, producing a difference6between selected points, forbidden. Eight points are impossible. The finite task also checks all36gap-excess patterns—8single-5patterns and28two-4patterns—and each has an adjacent3+3pair.

The maximum is therefore7for base0controller subsets with disjoint open neighborhoods, attained by the given U7. This is exactly the complete81-point W-plane-per-selected-fiber rule: each plane's port bundle fills a whole target fiber, so any shared target controller precludes disjoint full neighborhoods. The statement is not a global packing optimum in the full56862source, nor a bound for partial planes, other base layers or arbitrary pin sets.

For cap57, only this same base0complete-plane rule with three copies is being bounded: at most7*81=567base centers gives at most56862+3*567=58563vertices. The root-confirmed public guarantee58596is33larger. This closes that rule at cap57without producing or searching a new instance; the only stronger production window proposed here is56.

The inverse-map/full-neighborhood argument is identical to the prior fixed six-Uinterface, now using the42-entry target double-index injection. Labels remain original56862source labels, and the exact uIndex/a/border is in `CENTERS.csv`; `PINS.csv` and `CLONE_RECIPE.csv` contain the finite pin/label recipe. The original U6instance and all its evidence are preserved.

`precheck.py` measured0.145009CPU seconds, one worker, below10CPU. It searched0other Usets and read0large edgefiles; no complete graph, BFS, solver or Lean job was run. All local processes are terminal. Root retains the separate decision to append this stronger complete56instance; no accepted count is changed here.
