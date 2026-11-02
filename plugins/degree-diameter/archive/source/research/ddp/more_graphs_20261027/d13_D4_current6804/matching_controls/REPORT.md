# Two fixed controls on the actual 6804-point source

Both predictions were supported by the first required root, so neither
control proceeded to other fiber sources. No new lower bound resulted.
The original author's diameter-4 fact was reused, without any original
graph BFS. Its edge list was parsed once. Both controls constructed
their actual modified adjacency, with distinct edges and the expected
degree at every vertex, before their depth-4 check.

| Control | Vertices | Edges | Degree | Root | Targets outside R4 |
|---|---:|---:|---:|---:|---:|
| A: remove all z matching edges | 6804 | 40824 | 12 | 0 | 1519 |
| B: replace gamma(x)=-x+c by -x | 6804 | 44226 | 13 | 0 | 920 |

Here root 0 is the identity controller element and zero fiber vector.
Both controls first miss old vertex 11, namely the same identity
controller with fiber vector (2,0,1,0). This proves that their diameters
are not at most 4; their exact diameters and connectedness were not
computed. In particular, A does not give a (12,4) graph of order 6804.
B is a mechanism control at the same order, not a new-record proposal.

The unchanged line relations contribute 40824 undirected edges. The
3402 original matching edges were identified from the actual source:
they join controller g to g+42, with fiber map -x+(0,0,1,0). Their
endpoints give degree one at each of the 6804 vertices. A removes
exactly these edges. B replaces them by the distinct 3402-edge matching
with the same controller pairing and fiber map -x, retaining all line
edges. There is no added parameter search or offset optimization.

The missing classes separate two roles of the matching. A misses
points in 22 controller fibers, including 17 entire 81-point fibers
not touched by radius 4. B reaches at least one point in every one of
the 84 controller fibers, but still has missing points in the same
22 fibers. Thus the zero-offset z matching repairs 599 target points
and the controller-level holes, while the nonzero affine offset of
the original source remains necessary for complete coverage with
these fixed line charts and controller. This does not prove that all
other affine offsets or charts fail.

In the identity fiber, both controls reach exactly 77 of the 81
points and miss fiber IDs [11,19,27,54]. The complete missing fiber
IDs, decoded controller elements, first witnesses and distance-layer
counts from the tested root are saved separately in
A_delete_all_z.json and B_zero_affine_offset.json. Since original D4
is inherited, these targets were originally within four steps; this
comparison did not recompute the original root ball.

The author already explains the affine hyperplane-complementarity
principle. This experiment does not register it as a new theorem or
recompute the 36 packet profiles. Its contribution is the two fixed
actual-graph interventions and their exact first-root consequences.

If control A had passed its first root, left multiplication
L_h(g,x)=(hg,x) would preserve its right-generator controller edges
and constant fiber relations, and the 81 identity-controller fiber
roots would suffice to represent every graph root. The same action
survives control B. Neither inference was needed to extend execution:
both stopped on the first root as specified.

Total CPU was 0.106975 seconds, including the one source parse and
both adjacency constructions; the two control sections used 0.012000
and 0.007228 seconds respectively. There were zero downloads,
original-source BFS runs, all-source BFS runs, new candidate sweeps
or changes to the separate C9 experiment. RESULT.json and terminal.json
are complete, with no pending work. run.py reproduces this exact scope.
