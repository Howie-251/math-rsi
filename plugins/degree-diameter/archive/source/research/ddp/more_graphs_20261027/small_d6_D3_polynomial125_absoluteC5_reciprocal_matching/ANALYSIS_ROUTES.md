# Absolute C5 plus reciprocal matching: four-path review

Status: **VALID paper review of the frozen rule and four specified targets**. No parameter evaluation, graph, BFS or solver was run for this review. Full diameter-three coverage is not established by these four paths.

The unchanged q=5 source is the loop-deleted graph

    (a,b,c) ~ (s,a*s-b,a^2*s+a*s^2-c).

Use y=b-a^2/2 and h=c-a^3-4*a*y. With t=s-a, direct substitution gives exactly the frozen old-edge rule

    (a,y,h) -> (a+t,-y-t^2/2,-h+4*t*y+t^3).

The five absolute vertices have (y,h)=(0,0). They have old degree four and are independent: adjacency between two absolutes would require (a-d)^2=0. Adding their a-step-one C5 therefore gives each absolute two distinct, new edges.

For nonzero v=(y,h), write v=s*rep_L with the first nonzero coordinate of rep_L normalized to one, and define tau(v)=kappa_L/s. Then tau(-v)=-tau(v), so (a,v) -> (a+tau(v),-v) is a fixed-point-free involution. An old edge from v to -v must have t=0, because its y equation forces t^2/2=0. The new shift tau is nonzero, so this matching duplicates no old edge. The retained source has 310 edges; the absolute C5 adds five and the nonabsolute matching adds sixty. Thus the rule gives 125 vertices, 375 edges, all degrees six, independently of diameter or connectivity.

All arithmetic below is modulo five. Take kappa_(1,3)=4 and all other projective-direction coefficients one. Write G for an old edge, C for an absolute-C5 edge, and M for a new reciprocal-matching edge. The four literal paths from p=(0,0,0), in the original coordinates, are:

* c=1: p --C--> (4,3,4) --G--> (2,0,4) --G--> (0,0,1).
* c=4: p --C--> (1,3,1) --G--> (3,0,1) --G--> (0,0,4).
* c=2: p --G--> (2,0,0) --M--> (4,0,3) --G--> (0,0,2).
* c=3: p --G--> (1,0,0) --M--> (3,0,2) --G--> (0,0,3).

The c=1 and c=4 paths need no matching coefficient. Their intermediate absolute vertices are respectively a=4 and a=1, adjacent to zero in the new C5. Negating a and c preserves the source and this C5, which explains the paired paths; it is not necessary to assert that this reflection preserves the complete chosen reciprocal matching.

For the c=2 path, (2,0,0) has v=(3,3)=3*(1,1), so tau=1/3=2. Its matching endpoint has a=4, v=(2,2), which converts back to (4,0,3). For the c=3 path, (1,0,0) has v=(2,1)=2*(1,3), so tau=4/2=2. Its endpoint has a=3, v=(3,4), which converts back to (3,0,2). Substitution into the old neighbour rule verifies the two final edges.

Every old vertical target (0,0,c), c!=0, was outside the old B3(p), since the old formal endpoint formula e=v*(d-u), f=e*(v+d+u) forces f=0 when the endpoint has d=e=0. The four paths therefore repair a precise formerly missing target class, rather than merely exhibit old routes.

The a-translation action is an automorphism of the new-coordinate old-edge rule, the absolute C5, and the reciprocal matching (tau depends only on v). Its 25 orbits are the five a-values for each fixed v. Consequently, if the producer proves radius-three coverage from all 25 a=0 representatives, this proves global diameter at most three. Degree checks alone and the four routes above do not prove that coverage.

This rule is outside the already excluded single-matching augmentation family: each absolute receives two new C5 edges, whereas one matching can supply at most one new edge there. The earlier root route bound therefore cannot be applied to the whole new augmentation. Scope remains exactly the fixed source, absolute step-one C5 and six-direction reciprocal-matching family; no conclusion is drawn for arbitrary augmentations or all 125-vertex graphs.

Evidence reviewed: `PREDICTION.json`. This file records a paper validity result, not a production run or a new full graph.

## Final producer disposition

The inherited `RESULT.json` reports the complete fixed 4096-coefficient family tested once: 4096 actual candidates, each simple degree-six model of order125/size375, all rejected at the first representative root; zero untested settings and zero hits. `PRED_CONTROL.json` confirms all four listed canonical paths are present and their four vertical target distances are three. Thus the targeted local prediction is **SUPPORTED**, while the joint diameter-three existence prediction for this exact family is **REFUTED**. The canonical candidate still misses18 targets from root0; its first missing gauge target is (0,2,0). This is not an ordinary unordered bad-pair count or an exact global diameter.

Producer receipt: native0.024836 CPU seconds, aggregate child processes1.1875749999999998 CPU seconds including compilation; zero old-source BFS and zero solver calls. These values are read from the saved production outputs, not reproduced here. No added parameter, alternate C5, field, matching topology, external review or follow-up search is part of this paper task. The closure is not for all absolute-C5 augmentations or all125-vertex graphs.
