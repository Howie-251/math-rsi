# Two six-degree points and two eight-degree points: the single-K5 branch

Let H be a25-point,35-edge pair-covering simple five-uniform hypergraph of degree spectrum6²,8²,7²¹. Suppose five seven-degree points form a positive-weight K5. Their weighted rows4 force internal λ=2 and exterior λ=1, giving an actual group G. Then H has Property B.

There are four special points outside G: two degree6 and two degree8; the remaining16 exterior points have degree7. A six-degree point is globally unit, a seven-degree weighted row is4, and an eight-degree row is8. In particular a pair with one six has λ=1, a7/8 pair has λ≤5, and an8/8 pair has λ≤9. No8/8≤5 assumption is made.

As in Case A, the G inventory and the20 exterior partition marginals are unchanged. The complete27→22 inventory reduction applies, with every actual exterior point represented by its nonempty G partition Π and empty degree d(v)−|Π|. Existing raw certificates apply whenever the actual selected locked degrees match; they do not require unlocked vertices to have a common degree.

## A weighted special-point incidence obstruction

For any collection E* of real edges with nonempty G-traces T_e, suppose all their exterior points lie in a fixed special set S. Then

Σ_{e∈E*}|T_e|(5−|T_e|) ≤5|S|.

Indeed charge |T_e| to each exterior endpoint of e. A fixed exterior point appears in G-traces forming a partition of G, so its total charge from these selected edges is at most5. This proves the inequality without assuming that the selected traces are disjoint or distinct.

Apply it to the complete old strict-trace lists for identifiers14,20,22. Their costs are respectively36,30,24, all greater than5·4=20. Thus at least one such real edge has a seven-degree exterior endpoint, and the old seven-degree six-lock certificate applies.

Identifiers15,16,19,21 have at least three old strict G-triple edges. An exterior point is in at most one G-triple edge, because any two triples of G intersect. Three triple edges with no seven-degree endpoints would require six distinct special points, so these four classes also retain a true seven-degree caller.

For11,13,17 the old strict list has two triple edges. If either has a seven-degree endpoint use the old certificate. Otherwise their four exterior endpoints are the four special points, hence at least one endpoint is six-degree. For every strict triple T, its exterior endpoint's partition contains T and is either {T,G\T} or T together with the two complementary singletons, when those slots exist. The complete six-degree inputs are4 for11,2 for13,2 for17. All eight are raw strict, maximum20773/20995. Thus the ten old direct exclusions are all restored for this degree spectrum.

## Triple-orbit choices for the remaining eight straightforward classes

The exact group automorphism orbits from the earlier single-K5 proof give selected triple-edge counts2 for1,5,8,10,26;4 for7,9; and5 for18. Every orbit edge has two distinct exterior endpoints, and exterior endpoint sets of different triple edges are disjoint.

For1,5,8,10 the selected trace forces each endpoint into additional common unique G slots, so neither endpoint can be six-degree. Four endpoints across two orbit edges cannot all be the two eight-degree points. Hence choose an orbit edge with at least one seven-degree endpoint; its pair is7/7 or7/8. Old certificates cover7/7. The7/8 interfaces have the forced partitions {13,18}, {11,20}, {25,2,4}, {13,2,16} respectively. The complete new joint domains have4,4,3,7 inputs, all raw strict. The common trace of the selected edge is counted once; each other common unique slot is forced once, and the remaining shared-slot/empty counts range over all nonnegative capacities subject to λ≤5.

For7,9 there are four orbit edges, so one can avoid both eight-degree points. In7, T=22 forces Π={22,1,8}; singleton slots1 and8 are unique, so an endpoint cannot be six-degree either. Therefore a selected edge has two seven-degree endpoints and the old certificate applies. In9, T=19 admits partitions {19,12} and {19,4,8}. If a selected endpoint is six-degree, its pair has degrees6/6 or6/7 and λ=1; the two endpoints must use the opposite partition types, since the identical types would repeat another unique slot. These give exactly four new inputs (two directions for each degree pair), all raw strict, maximum96098/109395.

For18 the five orbit edges exceed the four special points, so a seven/seven edge exists and the old certificate applies.

For26 there are two orbit edges. They cannot both have endpoint degrees8/8 since the four endpoints are distinct and only two points have degree8. Choose an edge with a non-eight endpoint. The possibilities are6/6,6/7,6/8,7/7,7/8. The first two and7/7 are covered by Case A or earlier certificates. Both nonempty stars are forced to {1,8,22}. The new6/8 input has sole joint trace22 and λ=1; the new7/8 domain has16 inputs, with q22=1, q1,q8∈{0,1}, and q0=0,…,4−q1−q8. All17 are raw strict, maximum402587/437580.

For23 the unchanged partition moment still gives at least ten B points, each in two G-pair-trace edges. Removing four special points leaves at least six seven-degree B points, with at least12 incidences on only ten pair-trace edges. Hence a real seven/seven B–B pair exists and the old36 strict inputs apply.

## Inventory12: the two D=1 points may both be eight-degree

Use the exact same D(Π)=number of non-singleton blocks−1−1_{6∈Π} as in Case A, where6 is a G-subset bitmask. The group marginal gives ΣD=2; every seven-degree star has D≤0 in a non-B candidate; and every allowed partition has D≤1, with equality only at V1={5,26} or V2={3,28}. At least two special points therefore have D=1.

If one is six-degree, choose it and another D=1 special point. The pair is6/6 or6/8, has opposite V-types and λ=1, and is covered by Case A or the one-six proof. Otherwise both eight-degree points have D=1. This requires an actual8/8 interface, without assuming a six-degree point is among the D=1 points.

For the two eights, p0=r0=6. Equal V-types share both of their unique nonempty slots, so both shared-slot counts are1 and q0 ranges from0 to6, seven inputs per V-type. Opposite V-types have no common nonempty slot and q0 ranges from1 to6 (pair coverage), six inputs per ordered direction. Thus the complete domain has26 inputs, all raw strict, maximum396221/437580. Their codegrees range at most8, as forced by slot capacities; the general upper limit used is9.

## Inventories25 and24

For25 the unique four-trace30 exterior endpoint has Π={1,30} and degree6,7 or8. Each is already covered by the one-six proof's explicit degree-bound inputs. No global uniqueness of the eight-degree point is used by those conditional certificates.

For24 the unique triple28 edge has stars A={1,2,28} or B={3,28}. Pair degrees are6/6,6/7,6/8,7/7,7/8,8/8. The first five degree patterns have already been explicitly covered by Case A or the one-six proof. The8/8 case is new and uses the full row8 bound λ≤9.

For AA, q28=1, q1,q2∈{0,1}, and q0=0,…,5, giving24 inputs. For AB and BA, only q28 is nonzero among nonempty shared slots and q0=0,…,5, giving12 combined. BB forces q28=q3=1 and q0=0,…,6, giving seven. All43 inputs have nonnegative slot capacities and λ≤8 automatically, and all raw bounds are strict, maximum2295133/2450448.

## Complete finite gate and the r=2 conclusion

The new forced inputs number116:8 single-six inputs for11/13/17,18 seven/eight inputs for1/5/8/10,4 for9,17 for26,26 double-eight inputs for12, and43 for24. All are raw strict, with global maximum20773/20995. `MIXED_TWO_SIX_K5_B_PILOT.py/json` preserves the exact inputs, concrete layouts and all25 probability rows; the bounded computation took9.56 seconds. No free external-point domain or whole hypergraph is enumerated.

`MIXED_TWO_SIX_K5_B_REPLAY.py/json` independently generates all51 nontrivial G set partitions, conditions them on the actual selected trace, and restores every new input using all0/1 nonempty joint choices and all possible empty joint counts followed by exact slot tests. This differs from the original forced-complement and capacity-range generator. It checks complete equality with the116 certificates, every degree and codegree (including all-six unit conditions), and recomputes all25 raw ABC rows by direct binomial coefficients. It also checks the three strict-trace costs36,30,24. No original generator, DP, probability or quota code is imported. The full replay passed in1.11 seconds.

This covers all22 actual group inventories for spectrum6²,8²,7²¹. Together with Case A and the no-seven-degree-K5 Brooks caller in `MIXED_TWO_SIX_UNIT8.md`, both possible spectra with exactly two six-degree points are now covered. Thus every25-point,35-edge pair-covering simple five-uniform H with minimum degree6 and exactly two degree-six points has Property B. This result does not cover three or more six-degree points.
