# Three improved parameter cells, 103 complete graph examples

The complete lower bounds are **N(11,5)≥37631**, **N(12,5)≥42402**, and **N(13,5)≥51457**. There are3 degree11 prefixes37629..37631,60 degree12 prefixes42343..42402, and40 degree13 prefixes51418..51457. These are103 different-order examples in3 cells, without optimality, public-adoption or completed-Lean claims.

The fixed public source orders are37628,42342 and51417, checked on2026-10-27. Original complete source graphs are credited to Dharunish Yugeswardeenoo; H9 duality/partial-fold foundations to Rishabh Rajiv. Degree13 uses the actual official51417 adjacency, not an assumed reconstruction of its raw geometry.

## Common extension lemma

Let B be simple with maximum degree≤Δ and diameter≤5. Choose distinct existing pins S with |S|≤Δ and degree_B(s)<Δ for all s∈S. Retain every old edge and add z adjacent exactly to S. If closedR4_B(S) covers all vertices of B, the new graph has maximum degree≤Δ and diameter≤5.

Old-old paths remain. For every old v, some s∈S has distance_B(s,v)≤4; the edge z-s followed by that old path has length≤5. Distinct old pins introduce no loops or repeated edges. Apply the lemma in the actual successive graph, including all prior additions.

Every saved step satisfies this complete-currentR4/degree obligation. Induction proves each literal prefix; no prefix validity is inferred by deleting vertices from the largest graph. The corresponding D4 Moore bounds are12222,17569 and24506. All listed orders exceed them, so their diameters are exactly5.

## First degree13 graph

The published51417 source has324451 edges, maximum degree13 and diameter5. At prototype51013, omit saturated neighbor11352 from the proposed new star, while retaining the old edge itself. Keep the other9 neighbors and add guard50577. The new vertex51417 has neighbor set

    [2813,9214,15101,25662,33884,38121,38574,42842,48533,50577]

The ten original degrees, in this pin order, are11,12,11,12,12,12,12,12,11,11. The expanded graph has51418 vertices,324461 edges and maximum degree13.

Root independently rebuilt the original official raw edge set and read the complete new edge list. It checked simplicity, exact retention of all324451 old edges, ten new edges and actual degrees, then one complete new-root BFS. The eccentricity was5; distance counts were1,10,99,1032,9840,40436, totaling51418. See [independent_newroot51418.json](d13_D5_h9_transfer/singlefault_star_probe/independent_newroot51418.json).

Old-old diameter≤5 is inherited from the published valid source; new-old diameter≤5 is independently checked. This is the complete graph argument without rerunning old-source allpairs, proving a new raw-point map, or invoking a line/blocking-set theorem.

## Remaining degree13 prefixes

The finite continuation accepts39 further steps, ending at51457 vertices and324863 edges. Each checks actual current degree and completeR4, including all earlier new points. Literal source_n/m uses actual_base_n/m, not frozen original-source metadata.

[accepted_family40.json](d13_D5_h9_transfer/singlefault_star_probe/accepted_family40.json) and [families.json](delivery/families.json) contain the40 steps. Added cardinalities sum to412, giving324451+412=324863 final edges. Later steps are accepted by production complete-currentR4 induction, not described as separate independent new-root or allsource verifications.

The degree13 neighbor rule is near-complete old-star plus available guards. It differs from degree12 Q-line, Baer13 and Rédei15 pin selection; all share the retained-edge complete-R4 proof principle.

## Existing families and delivery scope

Degree11/12 literal steps remain unchanged. Degree12 orders42399..42402 use saved Rédei15 blocking neighborhoods plus actual whole-currentR4 completion; the inherited polar lemma gives a core guarantee, while actual coverage discharges extra vertices. Earlier full-allsource checkpoints include37631 and42377. Later steps follow the user's once-only degree/coverage policy.

[family_generator.py](delivery/family_generator.py) reproduces each listed example using only the three original sources and literal steps. The only new option is degree13; its first51418 dry-run matched the saved edges exactly without BFS. See [dry_run_d13_51418.json](delivery/dry_run_d13_51418.json).

Historicalreviewed_example_count remains38. Focused new-rule review does not claim all103 graphs were individually reviewed or every old root rerun. The focused D13 review disposition is [d13_singlefault_star_20261027.disposition.json](../../../reviews/ddp/d13_singlefault_star_20261027.disposition.json). Complete Lean graph instances remain0; generic extension interfaces and concrete graph binding remain separate. Goal stays active.

Historical63- and59-example proofs are retained as [FINAL_RESULTS_PROOF_63.md](FINAL_RESULTS_PROOF_63.md) and [FINAL_RESULTS_PROOF_59.md](FINAL_RESULTS_PROOF_59.md).
