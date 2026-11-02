# An actual order-seven source automorphism

The inherited seven double signature groups form one connected four-regular
quotient. Each directed quotient edge is an actual two-vertex matching, its
reverse is its inverse, and the two identity-image propagations are consistent.
The small sectors determine all signature-group images. The thirty-five
singleton groups are forced; the double groups require only one initial flip,
after which matching propagation either forces all fourteen images or rejects
a cycle disagreement. No 2^7 enumeration or generic isomorphism procedure was
used.

The first order-seven permutation in ORDER7_GENERATOR_AND_ORBITS.json is a
106-vertex bijection checked against all 582 actual source edges. Its edge
images have the same finite cardinality as the original edge set, so this gives
adjacency equivalence and a genuine automorphism, not a sampled homomorphism.
The exact tested prefix, attempted extensions, accepted maps and CPU are saved
separately; the search stops at this first order-seven witness and does not
claim the full automorphism group. Earlier failed unique-signature and partial
propagation predictions remain unchanged historical results.

## Paper consequence for the current internal-pin rewiring rule

When the recorded cycle shape is fourteen seven-cycles and the eight fixed
labels {7,17,23,34,46,54,59,105}, an invariant S of size10 or11 must be one
seven-orbit and respectively three or four fixed vertices. This restricts only
solutions required to preserve this particular C7; arbitrary solutions need
not have invariant S.

For a graph of order107, maximum degree11 and diameter2, every vertex has
degree at least10: a root of degree d reaches at most1+11d vertices in two
steps. Suppose only old G[S] is changed, new z is adjacent to S, and the C7 is
preserved while fixing z. A selected fixed vertex is adjacent either to all
seven orbit vertices or to none. Changing that bundle adds or deletes seven
neighbors, while changing its other selected-fixed incidences changes at most
r-1<=3 neighbors, and z adds one. Starting from degree10 or11, adding the bundle
forces degree at least10+1-3+7=15>11; deleting forces degree at most
11+1+3-7=8<10. Thus every fixed/orbit bundle is unchanged.

Each of the seven selected orbit vertices originally has degree11. An
undirected C7-invariant graph on one seven-orbit has even degree (a union of
cyclic-difference rings). All its other old incidences are unchanged, and z
adds one, so its final degree is even; the allowed interval[10,11] forces
degree10. Equivalently its old orbit-internal degree decreases by two. This
also excludes selecting an originally independent orbit under this symmetric
rule.

For |S|=10, z has seven neighbors of final degree10 and at most three of degree11.
Therefore its two-ball has at most
1+10+7*(10-1)+3*(11-1)=104<107 vertices. This proves that the C7-preserving
internal-S size10 rule cannot yield the desired107 graph. For |S|=11, the same
bound is115 and does not exclude a candidate; old selected/outside route
obligations still matter. No S11 or other symmetric rewiring was enumerated,
and no new graph, solver, source-D2 validation, or distance BFS was run.

