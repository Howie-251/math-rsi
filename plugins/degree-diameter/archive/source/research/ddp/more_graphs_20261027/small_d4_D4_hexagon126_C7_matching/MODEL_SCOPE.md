# Exact C7 matching/girth-six/diameter-four model on126 vertices

Use the direct primaryLCF source saved in SOURCE_LCF_PRIMARY.json and source126.edges, not an unproved localtriad labeling. It has126vertices/189edges/degree3. Primarygirth12/D6 are inherited. The explicit sigma(v)=v+18 modulo126 maps every sourceedge to an edge and has18orbits of size7, nine in each oldbipartition. Only this automorphism is used; no fullAut or Cayley claim is made.

An equivariant perfectmatching cannot match an odd7orbit to itself. If a vertex matched its shift by delta, equivariance and involution would force2delta=0 modulo7, hence a loop. Thus its18orbits must pair into9 distinct-orbit pairs, each with one relative shift. The compiler includes every such pair r<s and shift0..6 whose seven actual edges all lie outside oldR4. Actual matchingselector count is696. Selecting exactly one incident variable at each orbit describes the complete stated equivariant perfectmatching domain. Any selected graph retains189oldedges, adds63newedges and is simple4regular126/252.

## Exact girth restriction

A simple cycle of length<=5 can contain at most two matchingedges, because adjacent matchingedges would immediately return to a mate. Oldgirth12 excludes zeromatching cycles; the oldR4 domain excludes a singlematching edge closed by at most4oldedges. A cycle with two matchingedges has two positive-length old connectors with total length<=3. Both endpoint pairings must therefore be checked for(1,1),(1,2),(2,1).

For two disjoint matchingedges in the eligible domain, connector paths of these lengths cannot overlap internally without making one matched pair olddistance<=4; hence the forbidden positiveconnector condition is sound as well as complete. Pairs of selectoratoms incompatible already by orbitdegree constraints may add redundant clauses but cannot remove a valid perfectmatching. Every49actualedge combination between two atoms is covered up to sigma by fixing one edge of the first atom and testing seven translates of the other. The same selector's six nonidentical translates are separately checked; three actual selectors are excluded by unit clauses. There are10230 pairconflicts, of which1842 duplicate existing orbit-AMO clauses and8388 give newclauses.

This exactly selects augmentedgirth>=6 inside the restrictedmatchingdomain; oldR4 separation alone was not mistaken for the entire girth proof.

## Sound, existentially complete two-step claims

There are1125 unorderedpair orbits under sigma. For olddistance<=2, Y(p,q) is fixedtrue; diagonals Y(p,p) aretrue. For another pair, a length<=2 newroute can use only one matchingedge, since two successive matchingedges return to the initial vertex. Therefore its complete selector support is

    M(p,x), x in closedB1_G(q), or M(q,x), x in closedB1_G(p).

The closed balls include the endpoint, so directM is not lost. An emptysupport givesfalse. Otherwise Y implies the OR of its matchingselectors. The actualsupport sets are checked invariant on all seven pairtranslates. This yields81 fixedtrue pairs,108 emptysupport pairs and936 variableYclaims. A trueY always has a real path; reverse implications are unnecessary because an actualgraph can be extended by setting its true reachabilities and true witnesses.

All pairs within oldR4 already satisfy D4 because oldedges are retained. The5040 other pairs form720 canonicalorbits. For each representative(p,q), require

    OR over every w=0..125 of(Y(p,w) AND Y(w,q)).

A real length<=4 path splits into two pieces of length<=2, so no0/1/2matching route is omitted. Conversely, two trueclaims concatenate into a real length<=4 walk. Each sharedAND witness z implies both operands; identicalliterals and constants are simplified, and no phantom reachability is allowed. Existential auxiliary assignment is therefore exact for the graph family. There are58434 sharedANDvariables.

The completed model has60066variables and178695clauses, with0emptyclauses. It contains no erroneous one-M64 budget cut. The original paperestimate was corrected to76/74 and preserved in ORIGINAL_PREDICTION_BEFORE_COUNT_CORRECTION.json/ONE_M_CACHE_DIAGNOSTIC; it never changed an encodedconstraint.

A true SAT literal would be checked for allclauses,63matchingedges/252totaledges/degree4, augmentedgirth>=6, actualC7invariance and18representative R4roots before export. Only then could the parent independently check all126roots. This batch returnedUNKNOWN and no such literal or graph was produced.

## Outcome boundary

The sole CaDiCaL-t60 call returnedexit0 with noSAT/UNSATstatus or model. This is UNKNOWN, not an exclusion of even the restrictedfamily. A separate firstlegal mixedmatching control supportsB2 protection and exhibits five exclusive-two-M oldfar endpoints, but fails root0R4 and is only one sample. It supplies no family nonexistence result. Generalmatchings, otheractions and general126-point graphs are outside this model in any case.
