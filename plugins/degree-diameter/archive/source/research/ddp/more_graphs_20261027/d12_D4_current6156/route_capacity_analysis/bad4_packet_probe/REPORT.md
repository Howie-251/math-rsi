# Four bad rank-three routes do not form a covering pencil

Prediction frozen in `PREDICTION.json`: for root base 0, the words AABa, Abaa, Babb, BBAb were expected to cover the entire 81-point fiber when their controller endpoints coalesce. The prediction is refuted.

For va=(0,x,y,0), vb=(z,0,0,1), their endpoints are respectively base 0 at phases −(y+1), +(y+1), +(y+1), −(y+1). Thus at modulus 20 and y=9 all four do reach the same controller vertex (0,10), independently of x and z.

In the word order above, their projectively normalized hyperplane normals, with coordinates ordered x0,x1,x2,x3, are

    (0,1,2,2), (0,1,1,2), (1,0,1,2), (1,0,1,1).

They are four distinct projective normals, but their span has rank four rather than the rank two required for a pencil. Each individual route reaches exactly 27 fiber states from any source. For every one of the 81 source coordinates, the union of the four images has size 65, leaving 16 states.

This uniform count also follows directly from the independent normals. Write the four affine hyperplanes for a given source as n_i·v=c_i. The map v↦(n_1·v−c_1,...,n_4·v−c_4) is an affine bijection of F3^4. A point misses every hyperplane precisely when all four coordinates are nonzero, giving 2^4=16 uncovered points and union size 81−16=65. Hence different affine centers cannot repair this particular packet.

At source (0,0,0,0), the target (1,1,0,0), fiber ID 4 in base-three little-endian coordinates, is one explicit miss; every displayed normal evaluates to 1. The complete missing-ID list and all 81 source outcomes are in `RESULT.json`.

The existing `universal_*` profile fields in the parent analysis were not a test of this packet. They are the hypothetical endpoint coverage obtained if all 108 reduced four-letter words had full-rank route images. Under the actual Mizuno chart eight words have rank three. Therefore the decrease from 54 wide-certificate missing slots to 46 hypothetical universal-wide missing slots was only a capacity comparison. Actual current-chart zero-source coverage is stored under `x0_*` fields. This distinction is now explicitly annotated in the parent result and numeric profiles.

The new packet computation used 0.007853988 CPU seconds, no graph generation, no BFS, and no voltage-grid assignments. It excludes only this fixed four-word packet as a complete route certificate. Other routes to the same controller target were not assessed in this probe. No alternate packet or further search is started.
