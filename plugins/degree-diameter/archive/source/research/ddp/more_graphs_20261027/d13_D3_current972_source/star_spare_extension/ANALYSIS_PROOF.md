# Exact hub-and-nine-leaves extension criterion

Let H be the accepted972-vertex source of diameter at most3. Its free set F has108 degree12 vertices, three in each of36 blocks of27. The other864 vertices have degree13. The actual source profile gives every full vertex at least one neighbor in F. The induced graph on F consists of paths, each vertex having induced degree1 or2. These are inherited source facts, not new BFS conclusions.

Add hub h and nine leaves l0,...,l8 with exactly the nine hub-leaf edges. Partition all108 vertices of F, once each, into hub pins C and leaf pins A0,...,A8, with |C|<=4 and every |Ai|<=12. Join each pin only to its owning helper. Keep the source induced graph unchanged.

## Exact path conditions

Each old free target is a selected pin. Any helper reaches its owner within at most two star edges, followed by the pin edge, so every helper reaches every free target within3. Helper pairs have distance at most2. For any full old target t, choose an adjacent free pin p. The hub reaches p through at most one helper edge and its spoke, then t in at most3. Thus hub-old coverage is automatic as well.

For a leaf li and full target t, the exact condition is

    t belongs to R2_H(Ai) union R1_H(C).

Indeed a direct spoke from li gives one step plus an old path of length at most2. A hub spoke gives li-hub-p plus at most one old step. Another leaf's spoke already costs three steps before entering the old graph, and its endpoint is free rather than the full target t, so that route cannot reach t within3. No additional route type is omitted: the pin sets are disjoint, so a route between distinct helpers through old vertices has length at least3 and can be shortened to their star path of length at most2. A shortest helper-to-old path can therefore be taken as a star prefix, one spoke, and an H-only suffix.

Consequently the complete diameter3 requirement reduces exactly to these nine leaf coverage equations on the864 full targets. Old-old distances remain at most3 by retaining every source edge. This criterion is sufficient for the whole new graph, not merely for the new roots.

## Degree, order and the number of leaves

The hub has degree9+|C|<=13; each leaf has degree1+|Ai|<=13. Every old free vertex receives exactly its one spare edge and becomes degree13. All other old vertices keep degree13. There are982 vertices and6264+108+9=6381 edges. The total degree deficit below13 is4, shared among the helpers.

Nine leaves provide108 leaf spokes, matching108/12 when C is empty, and allow up to four pins to move to the hub. More formally a maxdegree13 star with k leaves can offer at most12k+(13-k)=11k+13 old spokes. Eight leaves allow only101, fewer than108. Thus nine is the smallest star that can assign every free pin under these degree rules.

The nine leaf labels are interchangeable. Each leaf is nonempty in any feasible solution: C has at most44 full neighbors, so at least820 full targets need that leaf's own R2 coverage. The leaves may therefore be ordered by their distinct smallest pin labels without losing a solution. This does not fix any geometric block to a leaf.

## Why the free triples must be split

The inherited star_spare_budget/RESULT.json reports75 full targets whose R2 free-pin support meets fewer than9 original blocks; the minimum block count is6. It does not say all75 meet exactly6. Each free pin has degree12 and at least one free neighbor, hence at most11 full neighbors. Thus four hub pins cover at most44 full targets in R1. At least31 of those75 thin targets remain outside R1(C), for every C.

Suppose the nonhub free pins of each original block are all assigned to one leaf color. Any remaining thin target then sees at most8 leaf colors in its R2 pin support, while all nine leaves must cover it. This is impossible. Therefore an allocation by whole free triples cannot work, even with arbitrary allowed hub pins; some triples must be distributed across leaves. The unrestricted per-pin model is a substantive change of the generating rule.

The general full-target R2 support minimum13 is at least9, so it does not itself forbid nine colors when blocks may split. This is only an individual-row capacity allowance, not evidence of a simultaneous feasible coloring. Likewise the earlier K6 LP failure does not support the new star prediction.

This file performs no LP/MIP, graph generation or source BFS. It proves the exact interpretation of the fixed star model. Only a complete positive producer graph triggers the assigned one independent literal degree/old-edge check and full982-source diameter verification; a negative or unknown result triggers no candidate BFS.

Producer disposition: the LP subwindow ended with status1 at its3-second time limit, and the single MIP also ended at its original remaining time with status1 and no incumbent; total19.541689 CPU seconds. No candidate or independent BFS followed. The base relaxation without leaf-minimum symmetry has an explicit rational feasible point: put1/9 of every pin at each leaf and zero at the hub. Each assignment sum is1, each leaf total12, and each full-target row is at least13/9 by the inherited minimum support13. This is fractional feasibility only and says nothing about an integral partition. The fixed star construction remains OPEN/UNKNOWN; no larger star or other helper topology was started.
