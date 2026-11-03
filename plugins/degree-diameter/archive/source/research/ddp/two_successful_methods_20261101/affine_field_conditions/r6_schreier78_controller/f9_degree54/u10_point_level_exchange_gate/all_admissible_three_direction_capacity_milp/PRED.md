# One new necessary count model, independent of W

Question before execution: with the same four retained fullplanes, do the already proved three-direction line constraints force totalcenter count<=810, or can any countvector still exceed810? This model allows arbitrary center coordinates in each admissible fiber; it does not expand or enumerate the729point pool.

Retained31/59/60/72 each81, all15admissible layers w in0..81, all othercontrollers0. For each target, totalincoming count<=81. Add positive indicator y iff w>0 and large indicator z iff w>=21. Each actual rank3 incoming triple satisfies sumw+8sumy<=97 and sumz<=2. These give sum<=73 when allpositive and at leastone w<=20, without incorrectly restricting zero families. Rank3 is inherited from the accepted six-conic-direction certificate; only actualport/direction identifiers are bound, no all-rank or field checks.

Actual triples are targets9/12/19/29/32/48/77. Include64/71. Single scipy.milp maximizes sumw, one worker<=20CPU including imports/model/solver/aggregation, time_limit16wallseconds, threads1. No previouspointMIP restart, newLP, solver continuation, largegraph/BFS/Lean, field/projection test or old wholelayeropt search.

If solver gives a vector>810, do only the512scalar support triples a,b,c in1..8 for each threepositive counttriple, checking A<=bc,B<=a(9-c),C<=(9-a)(9-b). Zero-family triples are outside this particular threepositive check. Any failedprofile is one concrete new necessary incompatibility, not a license to rerun the solver. Passing allprofiles is not an actualsourcepacking. If solverupper<=810, record only thisnecessarymodel's numericalMIP evidence andscope; no formal/global nonexistence claim.
