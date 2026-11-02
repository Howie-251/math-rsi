# PRED: fixed ovoid-by-spread full-neighborhood packing for cap 26

Written before the new numerical precheck, 2026-11-01 UTC. This is a new structural interface within mechanism A, using the already generated frozen 7242-point 25-regular source. The accepted 25-degree data and 6160 data remain unchanged.

Use the frozen GF4 arithmetic (code 2=w), projective points (u0,u1,v0,v1), symplectic form B=Trace(u*v'+v*u'), ascending point IDs, and fixed 17 slope-spread order from ../PARAMETERS.json. Test exactly

    Q(u0,u1,v0,v1) = u0^2 + u0*v1 + w*v1^2 + u1*(v0+v1).

Prediction, not result: Q is homogeneous quadratic with polar form B; its projective zero set O has 17 points, no two distinct O points are B-collinear, and every one of the 85 isotropic lines contains exactly one O point. A discrepancy stops this fixed rule without alternate Q, ovoid or spread.

The proposed centers are the 289 old vertices (p,l) in O times the original 17 spread lines. Their order is ascending p outer, original spread index inner, and their source labels are 85*p+l. Read the complete literal ../graph_d25_D3_n7242.edges but do not construct a new graph. Test that all 289 full source neighborhoods have size 25, are pairwise disjoint, cover exactly 7225 vertices and leave 17 vertices. The predicted exceptions are the chosen centers that are incident flags. At a flag center the old raw self-neighbor was deleted and replaced by its already present bonus vertex 7225+owner(p), once per owner.

Save the exact ovoid IDs, all ordered centers, each literal ordered neighborhood, all vertex multiplicities/load counts, and the 17 expected/actual exceptions. Prove the raw cross-incidence neighborhood product partition and how the 17 self/bonus substitutions give the literal full-N packing. Since floor(7242/25)=289, this many 25-neighborhoods is optimal for vertex-load at most 1 in this fixed source when one later raises the cap to 26. This is not an upper bound on N(26,3).

Precheck budget: at most 20 CPU seconds, one worker, no R3 check, no source BFS, no solver, no Lean, no install/native compile/hashes. No 26-degree candidate is generated in this stage. Complete graph release requires a further root notice after the public gate.

Conditional later prediction only: clone each of the 289 centers by attaching a new vertex to its full 25-neighborhood, preserving all existing edges. Expected final n=7531 and m=97750, degree histogram 25:306 and 26:7225. Before each actual insertion, a future authorized construction must check the entire current graph's radius-2 coverage from those 25 pins, including every earlier clone, and the cap-26 load. Those predictions are not precheck results and do not certify a global record.

## Stage 2 release: one literal7531 candidate

Root released the one fixed construction after the degree-26 public gate on 2026-11-01. The original precheck history above remains unchanged. The public comparison now gives 7514 from a general published Delorme extension applied to the7225source with its ovoid/spread packing; this is a formula guarantee, not a located7514edge table. No global-record or priority certificate is implied.

Before creating the current graph or inserting any new vertex, save IMMUTABLE_SOURCE_PINS.json with exactly the prechecked289centers and their ORIGINAL7242source full25neighborhoods. Clone order is the precheck order. Every later pin list is read from this immutable snapshot. A current center may acquire new neighbors because some centers are adjacent; do not replace a fixed25pin list by current(center). Check the center-induced graph once, predicting136 disjoint edges and17isolates; the centers need not be independent.

For each of289steps, check all immutable25pins have current degree less than26 and their complete current radius2 union covers every current vertex, including every earlier clone. Add vertex7242+i with these25old-source pins only. No new-new edge is added. Check final7531/97750, degree histogram25:306,26:7225, simple/reciprocal, all90525source edges retained, and one final ordinaryroot0connectivity BFS. Produce only the one candidate; no matching completion or other same-order variant. The producer budget is30CPUseconds/oneworker/0solver, with no source or candidate all-roots BFS. Fresh independent acceptance remains root-owned.
