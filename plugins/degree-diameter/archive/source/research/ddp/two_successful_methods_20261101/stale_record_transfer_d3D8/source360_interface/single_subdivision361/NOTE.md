# Chen360 single-edge subdivisions: actual bounded batch

Actual status:COMPLETE_NO_FIXED_CHEN360_ALL540_SINGLE_SUBDIVISIONS. Candidates finished:540/540.
NewrootR8 passes:0; newroot rejections:540;
old-old rejections:0.
Prediction for first rawedge{1,141} tested:True,
supported:False.

Only this fixed source's literal single-edge subdivisions were considered. Each
candidate has361 vertices/541 edges, source raw1..360 maps to0..359, newroot360.
The primary literal had two parse attempts: an initial0candidate/0BFS attempt
incorrectly required increasing numeric neighbor labels, then this corrected
successful binding only requires each undirected edge occur once. The source
input is simple360/540 cubic; the prior2.419079713CPU cost is inherited. The
one successful normalized source input is saved; sourceD8 is not reverified.
There was only one HTTP source download. Every candidate receives actual final
newroot BFS, and only passes receive ordinary old-labelled BFS until failure.
No symmetry inference, random seed, hillclimb or second source is used.

The exact newroot gate is R7_(G-e)({u,v})=allold, equivalently R7_G({u,v})=allold;
old-old preservation is separate. A complete all540 negative excludes exactly
this source and edit rule. Incomplete budgets remain UNKNOWN. A complete hit
still requires root's fresh independent acceptance and latest baseline gate.

First newroot failure: {"stage": "FAIL_NEWROOT_R8", "removed_edge_normalized": [0, 140], "removed_edge_raw": [1, 141], "inserted_normalized_newlabel": 360, "added_edges": [[0, 360], [140, 360]], "failed_source": 360, "failed_target": 22, "distance": 9, "actual_final_shortest_path_normalized": [360, 0, 141, 2, 145, 6, 153, 13, 169, 22], "actual_final_shortest_path_raw_old1to360_new361": [361, 1, 142, 3, 146, 7, 154, 14, 170, 23]}

One worker; prior readgate,preparation,compile,run and driver are charged under
the same20CPU case. No field,solver,Lean,ARIS,install or hash. Stop here; no
automatic continuation to another cut/source/template. Root alone updates
global graph counts and public claims.

All540 CSV rows are distinct tested source edges and FAIL_NEWROOT_R8; recorded failed-target distances:{"9": 540}. Final canonical cumulativeCPU:3.760862073/20. No old-old candidate or old-source pair diagnostic was reached. Stop this exact complete family.
