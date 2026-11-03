# Same-fiber obstruction on the literal Michel120 controller

This is a new obstruction for the proposed `(30,3)` candidate of order
`120*5^3=15000`; no such fiber graph was produced.

## Rule covered

Let `C` be the saved simple degree6 Michel120 controller. Each controller
vertex has a full fiber `F5^3`. Each controller edge gives a full5point
affine-line relation, with an invertible linear part. The opposite
orientation is its exact reverse relation. There are no within-fiber
edges. Edge maps, affine offsets, and compatible endpoint port lines can
vary freely by edge. The proposed six conic port directions are a special
case of this rule.

For an oriented edge `a->b`, write the neighbor relation as

    y = A x + c + t d,   t in F5,

where `A` is invertible and `d` is nonzero. The exact reverse relation is

    z = A^-1 y - A^-1 c + s A^-1 d,   s in F5.

Consequently the endpoints of a two-step controller backtrack `a,b,a`
from coordinate `x` are exactly

    x + (t+s) A^-1 d,

one5point affine line through `x`. The offset `c` cancels. This conclusion
does not require a particular `A` or a conic-preserving map.

## Triangle-free vertex lemma

Suppose a controller vertex `a` lies in no triangle. A fiber path of
length at most3 starting and ending in the fiber over `a` projects to a
closed controller walk of length at most3. Simplicity rules out length1.
Every length2 closed walk is `a,b,a`. Every length3 closed walk in a simple
graph would be a triangle, so none exists at `a`.

Thus at most the source point and six lines through that point are
reachable in the same fiber at radius3. Their union has size at most

    1 + 6*(5-1) = 25 < 125 = |F5^3|.

At least100 vertices in that same fiber are farther than3 from every
chosen source coordinate. Hence the proposed lift cannot have diameter
at most3, for any invertible edge maps or affine offsets satisfying the
exact reverse relation. This is a route-capacity exclusion, without any
fiber graph or distance search.

## Actual finite witness

The inherited literal source `research/ddp/m1_sources/graph_6_3_n120.txt`
has120 labels,360 distinct nonloop unordered edges, and degree6 at every
vertex. The new triangle computation finds zero triangles, with vertex
triangle histogram `{0:120}`.

Vertex0 has neighbors `3,78,83,88,92,103`. All15 pairs of these neighbors
are nonedges, so vertex0 alone supplies the lemma's hypothesis. The
complete small witness is saved in `TRIANGLE_FREE_WITNESS.json`; all120
triangle counts and sorted neighbor lists are in
`CONTROLLER_TRIANGLE_PROFILE.json`.

The source's provenance, exact recovered construction, and known
controller diameter3 were inherited from `m1_sources/SOURCE_NOTES.md` and
its saved source records. No source fetch, reconstruction, or all-source
BFS was repeated.

## Exact stopping boundary

This excludes the whole fixed Michel120/full125point-fibers/full5point
edge-line/no-within-fiber-edge rule with true reverse inverse relations,
including affine offsets. It does not exclude changed controllers,
within-fiber edges, or different fiber relations. None of those variants
was tried or scheduled.

The conditional `PGL2(F5)` quotient gate was not reached. In particular,
no q4 permutation domain was reused, no q5 projectivity domain was
enumerated, and no claim of quotient sufficiency was made. The saved
C72 quotient/Hall theory remains inherited and was not rerun.
