# C9 external core with length3 chords: the T-lift misses an E target

**The three positive route guarantees are valid, but the declared joint D3 existence prediction is refuted.** This is a uniform paper obstruction. The producer has not compiled an actual new model; this analysis generated no graph, decoded no candidate, and ran no BFS or SAT. The two earlier family exclusions are unchanged.

## The three positive guarantees

E-to-E coverage holds: C9 paths cover offsets1,2,3; the S-pair chords supply every offset4 pair in3steps. The removed chord0 is replaced by E0-a-E4 in2steps.

Helperc reaches all42: its threeT spokes reach allT-adjacent S endpoints in2steps, alltheir S mates in3, and everyA fibre by T-S-A in3. For i!=0 the route c-T-s_i-E_i has3steps. The deleted E0 branch is restored by c-b-a-E0. Helpersa/b are within2steps.

Helpera reaches allnineE: use its E0/E4neighbors, then at most2cycle steps. The cycle balls are{7,8,0,1,2}and{2,3,4,5,6}, whose union is allE. These three statements use compatible routes in the same declared structure. They do not imply globalD3.

## Uniform missing route class

Let t be the unique lift of absolute baseT adjacent to s0 through the preserved A-S lift. It exists for every voltage choice, since each projected A-S edge lifts to a perfect matching. Its new port is already occupied by c, and its other three neighbors are oldS. One is s0; denote the others s_j,s_k.

A path of length<=3 from t must begin with one of these four neighbors. After its first step, at most2steps remain. The full E-target budget is:

| First neighbor | E endpoints in the remaining<=2steps | Reason |
| --- | ---: | --- |
| s0 | 0 | Bothend E-Sedges of pair0 were removed. s0 and itsmate now meet only S/A; the replacement S-Aedges create noA-Eedge. |
| c | 0 | c meets T-lifts andb. Neither anA nor b has anEneighbor. The c-b-a-E route needs3steps after c. |
| s_j | at most4 | Its attached E; the two C9neighbors of thatE; the Eattached to its S-Smate. |
| s_k | at most4 | The same complete local classification. |

Branches through the other A-neighbors of S cannot add anE at this depth because A has noEneighbor. An S-to-A-to-a route ends at helpera; reaching E0/E4 then needs a fourthstep from t. Similarly t-S-E-a ends at a after3steps. Thus the new E-neighbors of a create no omitted3step E-target route.

Consequently |R3(t) intersect E|<=0+0+4+4=8<9. At least one oldEvertex is farther than3 from t in every allowed assignment. More explicitly, the two uncut branches have endpoints contained in F(j)union F(k), where F(i)={i−1,i,i+1,i+4} modulo9. Any E outside that at-most8-element set is a counterexample target. No particular voltage, pairing, or candidate graph is chosen.

The positive c-full-cover statement is not contradicted: t-c consumes one extra step, turning a c-to-E3route into a4route. The obstruction therefore concerns joint old/new coverage, rather than c's own eccentricity. Expert_brief_evidence independently confirmed the complete branch classification and the8<9 contradiction by paper review.

This closes only the declared C9/chord4/two-endcut/fullT-helper family. It is not a statement about arbitrary42graphs or all polarity modifications. The separately proposed a-to-A capacity attack is unnecessary for this decision and is not claimed solved here. No further spoke retuning, template, solver, or source is executed.
