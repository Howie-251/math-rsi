# C11-invariant 33-controller: one complete finite route test

Target: the same 11K3 plus disjoint simple external2factor controller, with every distinct nonadjacent ordered pair joined by a length3 nonbacktracking walk. A passing controller transfers the existing fixed F5 certificate to4125 vertices, degree20, D3; no such graph exists locally yet.

Fix vertices (a,l), a in Z11, l in {0,1,2}; triangles have equal a. Extra edges are invariant under a -> a+1. Their label multigraph has degree2, counting a loop twice, so has exactly three types:

1. Three loops, each step represented by1..5: 125 settings.
2. One label loop and two distinct parallel edges between the remaining labels, each nonzero shift in1..10: 3*5*C(10,2)=675.
3. One three-label triangle, with three nonzero shifts: 10^3=1000.

Total1800 legal literal settings. Cross-label shift0 is forbidden because it repeats a fixed K3 edge. There is no half-turn loop since11 is odd. Independent phase changes per label do NOT preserve the fixed triangles and are not used as a gauge.

Specific prediction before computation: in triangle type with oriented shifts (a,b,c)=(1,3,5), all same-label phase targets have NB3 routes, and rootlabel0 to label1 covers all its nonadjacent phases; rootlabel1 to label2 misses phase7, rootlabel2 to label0 misses phases7 and9. This tests actual route complementarity rather than a total bad-pair score. The formula for0->1 phases is {-c,-a,b,c,-b,a+b,2a,a-b,a-c,c+a}; other pairs rotate labels.

The feasibility question is whether another legal setting satisfies all rootlabel/targetphase requirements simultaneously. Check all1800 once (stop at first complete hit). This is the first complete test found for this exact scope: the previous800000 proposals were finite general local search, and both full SAT encodings were UNKNOWN. No old seed/timer is resumed.

Compute explicit33-point adjacency, assert simple4regular/66edges, enumerate all NB3 walks from roots(0,0),(0,1),(0,2). Translation symmetry covers all33 roots. Save each tested setting's exact missing targets, not just an aggregate score. On a hit, save full controller and immediately report; otherwise close only this C11-invariant family. Budget2 CPU seconds, single worker, no SAT/BFS in a large graph. Do not start another subgroup or controller-order ladder automatically.
