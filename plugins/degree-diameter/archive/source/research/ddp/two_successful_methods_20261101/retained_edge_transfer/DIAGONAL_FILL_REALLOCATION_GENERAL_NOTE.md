# Diagonal fill reallocation for a spread and a partial ovoid

2026-11-01. This note records the mathematical rule extracted from the fresh accepted7532 test. It is a paper derivation, not a claim that all indicated graphs have been generated, kernel-certified, or established as new in the literature. The accepted filled source, incidence geometry, partial ovoid and spread are genuine hypotheses; no arbitrary field or parameter formula is substituted for them.

## Interface and exact rule

Let a finite generalized quadrangle of order(s,t), s,t>=2, have a line spread S indexed by J, |J|=R=st+1. Put delta=(s+1)(t+1). The old vertex set U=P x L has delta R^2 vertices. Its simple opposite-incidence graph joins distinct(p,L),(q,M) precisely when p lies on M and q lies on L. An incident flag has degree delta-1; every other old vertex has degree delta. The accepted source H retains U and adds F_j for each spread line, adjacent to exactly the flags(q,M) with q on S_j. These pinsets partition the flags; |N_H(F_j)|=delta and H is delta-regular and diameter at most3 by the inherited source theorem.

Choose an actual partial ovoid O of p points, so each line contains at most one selected point. Use C=O x S as pR centers. For integer k>=1, retain every H edge; for each center c add k independent clones whose neighbors are exactly N_U(c), not N_H(c). Finally add k independent hubs, each adjacent to all R original fillers. There are no other added edges. Require R<=delta+k, which holds here since R<delta.

An incident center c=(o,S_owner(o)) contributes one omitted clone-to-filler edge per copy compared with full-H-neighborhood copying. There are exactly p such centers. Every hub uses R filler edges. This is a change in the generation rule, outside the previous barriers that retain all mandatory full-H-clone edges.

## Full coverage, with no future-vertex dependence

The opposite-incidence graph U itself has diameter at most3 from the accepted GQ projection interface. It has no isolated vertex. Full-neighborhood cloning on U therefore covers U--U, clone--U and clone--clone pairs within3, including adjacent centers. Two distinct copies of the same center use clone(c,r)--u--clone(c,r') for any u in N_U(c), in2 steps. All these walk interiors lie in U.

For a nonincident center, N_H(c)=N_U(c), so replace the first vertex of its H-to-filler walk by its clone. For an incident center c=(o,S_j), the omitted own-filler edge has an alternative length2 walk clone--(o,M)--F_j, using another line M through o. For any other filler F_l, l!=j, an H walk of length<=3 from c to F_l cannot start via F_j: distinct fillers have no edge and their flag pinsets are disjoint, so F_j and F_l have no walk of length<=2. Its first edge therefore lies in U and can still be inherited by the clone. This proves all clone--filler pairs.

Every old vertex has an incident-flag neighbor in U: for a nonflag use the point-to-line projection and its connector; for a flag choose a distinct incident line or point. Every clone likewise has a flag in N_U(c). Thus hub--owner filler--flag--target is a walk of length<=3 to every U vertex and clone. Hubs reach all fillers in1 and each other in2 through any filler. All pairs are covered.

These arguments apply to every prefix that adds the modified clones directly to H, followed by any subset of the hubs. They do not infer prefix diameter by deleting vertices from a final graph. Each new point's required covering routes already exist at insertion.

## Load, degree, order and edge formulas

Distinct center U-neighborhoods are disjoint. A shared neighbor(v,N) would put two selected ovoid points on N, forcing the same ovoid index; it would also put v on two spread lines, forcing the same spread index. Excluding the center self-slot only removes the p diagonal flags and never creates an overlap.

There are p diagonal centers of U-degree delta-1 and pR-p off-diagonal centers of U-degree delta. The clone-pin union has size delta*pR-p. Each of its old U vertices gains k edges; each original filler gains k hub edges. All other source vertices keep degree delta. Each clone has degree delta-1 or delta, each hub degree R. Consequently maxdegree is exactly delta+k, attained at every original filler, and

    n = delta*R^2 + R + k*(pR+1),
    m = delta*(delta*R^2+R)/2 + k*(delta*pR+R-p).

For distinct degree values, the exact histogram is

    degree delta+k : delta*pR-p+R,
    degree delta   : delta*R^2-delta*pR+p + k*(pR-p),
    degree delta-1 : k*p,
    degree R       : k.

If p=R (a full ovoid), the edge count is identical to full-H-neighborhood copying while order increases by k. If p<R, order increases by k and edges by k*(R-p). This latter rule includes the existing actual q7/P33 geometry in principle, but no new P33 endpoint is produced by this note.

At fixed final cap Delta=delta+k and p=R, the order simplifies to n=Delta*(R^2+1)-(s+t). Thus source choice at the same R is governed by s+t, once actual full-ovoid/spread hypotheses and the degree window are available. The actual balanced(8,8) source has R65 and constant-16; a conditional(4,16) source with the required interfaces would have the same R but constant-20 and would start four degrees later. Its larger unexpanded order does not improve this rule. This algebra directs the next parameter choice toward the already verified balanced source; it proves neither the missing(4,16) interfaces nor optimality among other construction rules. The separate finite public comparison window84..98 records the checked competing formulas without generating any further graph.

## Reusing the k1 graph for every higher multiplicity

There is a useful exact identification, not just a numerical coincidence. Let G1 be the accepted k1 reallocation graph. Its new-role set J consists of all pR clones and the one hub. This is an independent vertex set. Every clone-role vertex has its entire G1-neighborhood exactly N_U(c); the hub-role vertex has its entire G1-neighborhood exactly the original fillers. These neighborhoods are pairwise disjoint, by the partial-ovoid/spread packing and the separation U versus fillers.

Consequently G_k is precisely G1 with k-1 full, immutable G1-neighborhood copies of every vertex in J. The generic FullNeighborhoodClones diameter, degree-load and nonD2 theorems apply directly to this source. No truncated-neighborhood theorem has to be reproved for each multiplicity. The new-role centers themselves have no new neighbors during this repetition, since all pins remain in original H.

For the single degree83 test, G1 is the actual346516 graph, J has4226vertices, and one full copy gives n350742/m14547195 while retaining every346516 edge. J is ordered as the4225existing clones followed by the existing hub; the new labels346516+h and350741 match that exact clone graph. The copied center for a new clone is the existing first clone, not its old GQ coordinate center. This distinction makes the higher-multiplicity Lean obligation a direct application of the existing full-neighborhood framework after the new k1 theorem closes.

## Exact diameter and actual scope

When p>0, exactness has an immediate stronger witness: choose any hub and any clone. They are not adjacent, and the hub's neighborhood lies entirely in the filler block while the clone's neighborhood lies entirely in U. These disjoint blocks preclude a common neighbor and hence any walk of length<=2. The coverage proof already supplies a length3 walk. This purely structural witness applies to both actual full-ovoid instances, without a finite witness search or a hub collapse map.

For s,t>=2, st>=s+t, R>=5 and delta=R+s+t<=2R-1. Hence R^2-delta>0 and |U|=delta R^2>delta^2+1. Fix any root a in U: its entire H radius2 ball, including fillers, has at most delta^2+1 vertices. U alone is larger, so choose b in U outside that H ball; H diameter<=3 makes its H-distance exactly3. A new clone cannot create a length2 shortcut between old U vertices: a common clone neighbor implies the corresponding original center was already a common H neighbor. Hubs have only filler neighbors and cannot be common neighbors of two U vertices. Thus this fixed old U pair retains distance3 for any k, proving exact diameter3 under the stated hypotheses. No collapse homomorphism sending hubs to H is asserted.

Actual produced and independently accepted examples: s=t=4, R=p=17, delta25,k1, giving7532vertices/97750edges/maxdegree26/exactD3; all290new-root predictions matched. The q8 second-scale case s=t=8,R=p=65,delta81,k1 also passed fresh mathematical acceptance at346516/14204970/maxdegree82/exactD3, with complete4225N_U literal binding and actual65changed diagonal roots plus hub matching their predictions; no off4160/old-root BFS was repeated. Their acceptance is in the respective receipts, not supplied merely by this note. No new field, geometry or graph-BFS experiment was needed for this derivation.

Independent paper attack in diagonal_fill_general_review/NOTE.md supports the stated arbitrary partial-ovoid and k>=1 scope. The clarifications above make same-center copies, exact maximum degree and fixed-root Moore counting explicit. This is paper-level acceptance, separate from the new concrete Lean batch and external review.

This general derivation changes the next computation: test one second-scale case using the same omitted-edge rule, then reuse the accepted finite geometry for a new generic/concrete Lean proof. Do not restart fixed-adjacency searches that these graphs deliberately leave. Public attribution and exact literature priority remain UNKNOWN, separate from mathematical correctness.
