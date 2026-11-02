# Concrete full-neighborhood extension17/2016

The published source is Ryosuke Mizuno's literal30-controller edge-local
F4³ graph,1920 vertices and15360 edges, simple16-regular with diameter3.
Its actual cached construction, proof,780 full-rank plus120 adjacent-pencil
certificates and previous independent all-source report are linked in
`../LOCAL_SOURCE_INTERFACE_NOTE.md`. Those source algebra/BFS results are
inherited. The source raw table here is one materialization of that recipe,
not a new source construction or a rerun of the author's verifier.

Select the actual controller layers I=[0,3,5,7,9,16]. Their literal open
neighborhoods are pairwise disjoint, covering24 of the30 controller layers.
`../CONTROLLER_PACKING_RESULT.json` supplies the selected neighbor lists
and the one exact373-node search (optimum6). Optimality of that restricted
controller packing is not needed for legality of this selected code.

Inside each selected layer use W={(a,b,a+b):a,b in F4}. The normal111 has
value1 on e0,e1,e2,111 in characteristic2. Thus W meets each of the four
input port lines only at zero. If two of its points had the same neighbor
through edge e, their difference would be in
T_e^-1(<ell_reverse>)=<ell_port>, hence would be zero. Each layer therefore
has16 centers with disjoint source neighborhoods; their256 neighbors
exhaust the four neighboring fibers. Across selected layers disjoint
controller open neighborhoods prevent any common old neighbor. All96
complete source neighborhoods of size16 are consequently disjoint.

For each center c append one new vertex c' joined to exactly the old
source neighborhood N_G(c). Keep all15360 source edges, with no new-new
edges. Actual labels and ordered neighbor lists are in PARAMETERS.json
and ALL_96_NEW_ROLE_NEIGHBORS.json. There are96*16=1536 new edges and
1536 old pins of load1. Thus n=2016, m=16896, with degree histogram
{16:480,17:1536}. Maximum degree is exactly17.

For old-old pairs retain the source Walk. For one new endpoint c' and
an old vertex v!=c, replace the first endpoint of a source shortest Walk
from c to v; its next vertex belongs to N_G(c). To join c' to c itself,
use any old neighbor of c for a two-edge Walk. For two new endpoints
c',d': if source centers have distance2 or3 replace both endpoints of
the old Walk; its interior vertices remain old. If c and d are adjacent,
use c'--d--c--d'. If the centers coincide (not needed in this96-role
instance), use their common nonempty neighborhood to obtain length2.
These are genuine Walks in the constructed graph of length at most3.
They use no other new vertices, so every insertion prefix has the same
diameter bound, and pin loads remain at most1 at every prefix. Equivalently,
the16 pins of each next point cover the CURRENT complete prefix with
closed radius2 balls, as the general retained-edge expansion lemma requires.

Distinct new vertices are nonadjacent and have disjoint neighborhoods,
so have no Walk of length<=2. The preceding Walk construction gives
distance exactly3 for every pair of distinct new vertices. Each new
vertex is distance exactly2 from its old center. These route predictions
are checked by the fresh96-new-root ordinary BFS batch. No old-root BFS
is needed to reprove the already accepted source.

This is a new complete candidate generated from the combination of the
affine-layer and retained-edge mechanisms. It is not a new general
cloning lemma, not a new source1920 graph, and not a proven optimum for
all point-level clone codes or for N(17,3). The currently read Comellas
table has no degree17 row;1920 is only a located monotone guarantee.
Global competitive threshold and exact priority remain UNKNOWN. Lean
for the literal C30 source and this final2016 graph is not yet complete;
the existing C60/3840 theorems cannot be substituted for it. Independent
acceptance and root release are separate from this producer proof.
