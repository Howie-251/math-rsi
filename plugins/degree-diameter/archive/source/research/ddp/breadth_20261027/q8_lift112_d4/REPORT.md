# Fourteen-base-vertex Q8 lift: completed112-point D4 trial

The authorized finite construction trial is complete without a diameter-four graph. The saved best is a simple four-regular112-vertex graph with224 edges; the parent's unique independent all112-root saved-edge check confirms exact diameter five and480 unordered pairs farther than four. See best.independent_check.json. No new lower bound or entire voltage-family exclusion is claimed. The C8 variant only received a necessary capacity screen; it was not searched or excluded.

## Actual structural change

The base is the square of the14-cycle: vertex i has neighbors i+1,i-1,i+2,i-2 modulo14. Its28 undirected edges are stored exactly in sorted endpoint order. This is a14-vertex degree-four base containing triangles, and the target diameter is four. The old Q64 branch instead used four base vertices, degree eight and diameter three. This is an actual change of base, fiber and route length inside the same voltage-lift method; it is not presented as a wholly unrelated construction mechanism.

The fiber is Q8 with labels[1,i,j,k,-1,-i,-j,-k]. For each oriented base edge u<v with group voltage h_e, join( u,g ) to( v,g*h_e ) for all eight g. A base edge is a perfect matching between distinct orbits, with no parallel base edges or base loops, so every assignment is a simple four-regular graph. The output has14*8=112 vertices, exceeding the saved(4,4) bound104 if diameter four is attained.

The spanning tree is the thirteen edges(i,i+1), i=0..12; these have identity voltage. All fifteen remaining voltages are free. For any original assignment, independent coordinate changes in the base fibers can make all tree voltages identity, so this normalization does not lose lifted graphs up to relabeling. The exact edge IDs, tree and free indices are in CAPACITY.json and group_and_graph_definition.json. In particular the wraparound edges are oriented by smaller endpoint, not by a guessed cyclic direction.

Left multiplication(i,g)->(i,a*g) preserves all lifted edges and is transitive in each of the fourteen fibers. Fourteen full BFS roots therefore give the exact diameter and radius-four deficits by proven symmetry. If their deficits sum to M, the bad unordered pair count is8*M/2=4*M.

## Exact short-word function capacity screen

All nonbacktracking named base walks of lengths zero through four are enumerated from every root:1+4+12+36+108=161 walks per root. Immediate reversal can be removed from any shorter path without changing its endpoint, so these walks contain a representative of every reachable lifted endpoint. Walks are separated by ordered base endpoints and their exact group-valued functions of the fifteen free voltages are deduplicated.

For C8, each walk is an exact linear coefficient vector modulo eight. Two such functions are equal precisely when their coefficient vectors agree, since independent variables can be evaluated at zero and at unit-coordinate inputs.

For Q8 write each variable as i^a j^b(-1)^c with a,b,c in F2. The product of(a,b,c) and(u,v,d) is(a+u,b+v,c+d+a*u+b*v+b*u), all modulo two; inversion adds a+b+a*b to the center bit. Thus each path's two low bits are linear forms and its center is a degree-at-most-two Boolean polynomial in the45 independent bits. The producer stores its unique multilinear algebraic normal form, reducing repeated variables by x*x=x. Equal signatures are exactly equal Q8-valued functions, rather than a sample-based test.

Both groups have minimum slot capacity eight, so neither is excluded at this necessary stage. In fact both yield2254 total different functions across all slots, equal to the raw14*161 count: Q8 does not improve this symbolic capacity on this base. Some slots are tight with exactly eight available path functions. Passing capacity does not mean a common voltage assignment makes these functions simultaneously cover all eight group elements. Only Q8 received the following actual graph trial.

## Finite actual construction profile

Twelve fresh starts use seed20261027142. Each assigns all fifteen free Q8 voltages uniformly, with no old source. Each start has three descent segments, each permitting at most twelve strict full-coordinate moves. A neighborhood contains15*7=105 legal one-coordinate changes. Between segments, seed20261027143 selects two distinct free coordinates and changes both to different group elements. There are no extra starts, additional bases, C8 actual searches, restarts or continuation runs.

All12 starts and36 segments completed:161 full105-neighbor scans,125 strict moves,24 two-distinct-coordinate kicks,16941 fourteen-root evaluations and237174 BFS roots. The best has root deficits[7,9,7,7,8,10,6,10,6,9,11,10,9,11], sum120 and480 bad unordered pairs. Its28 edge voltages in the saved edge order are[0,5,1,2,0,7,6,0,4,0,6,0,7,0,2,0,6,0,4,0,3,0,2,0,4,0,6,0]. The complete224-edge output is best.edges. This closes only the specified finite trial.

## Calibration, budget and terminal state

Python independently expands the first actual start using Hamilton multiplication of four-coordinate signed unit quaternions, verifies all448 directed adjacencies, and runs fourteen ordinary full BFS traversals. C++ uses the three-bit multiplication formula above. Every adjacency and all1568 distances agree; first_cpp_check.json records this and the first score is reused. No extra pilot graph or independent final all112-root BFS was run by the producer.

Capacity screening used0.010119020 CPU seconds. Driver preparation and compilation used0.899287000 CPU seconds, production0.318365000 CPU seconds, and the measured total including capacity is1.230129020 CPU seconds, below the60-second single-worker budget. The driver wall time is1.239259504 seconds, excluding the separately completed capacity command. No process remains running. terminal.json is COMPLETE_12_START_PROFILE_NO_D4, with pending=[] after the parent's unique all112-root independent saved-edge check. That separate final verification used0.006385785 CPU seconds and is not included in the search-driver total. The method was stopped after its profile rather than extended to further seeds or local-neighborhood proofs.
