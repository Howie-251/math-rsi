# Fixed3840 graph: every original edge is essential for diameter3

The fixed accepted graph is the original20regular graph on60×F4³ defined by
`../f4_c60_edge_projective/PARAMETERS.json`; its original38400-edge table and
all prior acceptance/Lean evidence are unchanged.

**Every one of its38400 undirected edges lies on a unique path of length at
most3 between some pair of original vertices.** Therefore any nonempty pure
edge deletion, retaining all3840 vertices, destroys diameter≤3. In particular
purely thinning it to maximumdegree19 cannot produce a valid19degree D3 graph.
This conclusion does not exclude rewiring, vertex deletion, changed charts or
other19degree graphs.

## Inheritance and the falsifiable prediction

The unique-controller-route criterion already exists for the different fixed
F5/3750 graph in
`research/ddp/refresh_20261029/f5_d20_edge_criticality_20261029/EDGE_CRITICALITY.md`.
It is inherited, not a new general lemma. The new question is whether its
sufficient condition survives transfer to the actual60controller and its
edge-dependent F4 matrices. PRED.json was saved before this finite test.

The prediction was that every directed controller edge begins a unique
controller-distance3 route, with an invertible actual noise map. Failure of
that first-position condition would have refuted the prediction without
proving that an edge was deletable.

## Actual controller and rank test

`check_controller.py` reads only the saved actual controller, inverse ports,
five directions and all dart matrices. It enumerates all60·5³=7500 controller
walks of length3 and separately computes all controller endpoints reachable
in at most2 steps. Among the ordered endpoint pairs,1260 have distance3 and
exactly one length3 walk. All1260 corresponding actual3×3 F4 noise matrices
are invertible: determinant values1,2,3 occur434,410,416 times.

These routes begin with every one of the300 directed controller darts. The
number of eligible witnesses per first dart is3 for100 darts,4 for80 darts,
5 for80 darts and6 for40 darts. No dart is missing. The complete list of1260
routes and one selected witness for each of300 darts are in
CONTROLLER_CERTIFICATE.json. This is not an assumption of uniform edge charts.
Every noise matrix is computed from that route's three actual saved matrices.

## Why every lifted edge is forced

Take an arbitrary directed edge of the fixed lifted graph, written

    (a,x) → (b,y),  b=C[a][p],
    y=T[a,p]x + λ L[inv(p)],  λ∈F4.

Select the certified controller route a→b→c→d with ports(p,q,r), for which d
has controller distance exactly3 from a and no other length3 controller walk
exists. Continue the chosen edge with noise0 on each of the last two steps:

    (a,x) → (b,y) → (c,T[b,q]y) → (d,T[c,r]T[b,q]y).

Every lifted path of length≤3 between these endpoints projects to a controller
walk of the same length: the original controller has no loops and each graph
edge joins its prescribed distinct controller layers. Hence every candidate
path must have length3 and use this one controller route. For this route, the
endpoint depends on its three noise coefficients by an affine map with columns

    T[c,r]T[b,q] L[inv(p)],
    T[c,r] L[inv(q)],
    L[inv(r)].

Its determinant is nonzero in the explicit polynomial field F4, so the map is
a bijection F4³→F4³. The selected target already arises from(λ,0,0); no other
noise triple can reach it. Thus the displayed lifted path is the unique
length≤3 path for that pair, and it uses the arbitrarily chosen original edge.

This argument covers every source coordinate x and every λ on every dart,
therefore all300·64·4=76800 directed graph edges, equivalently all38400
undirected edges. Removing one of them breaks its witness pair. Further edge
deletions cannot create a missing short path, so any nonempty deletion set
fails. The statement is about the actual graph, not only the survival of its
previous sufficient certificate.

## One literal endpoint check and resource scope

As a small independent-of-formula comparison, the script reads the original
literal edge table once and enumerates only the length≤3 walks between the
single selected zero-coordinate endpoint pair in
LITERAL_SINGLE_PAIR_CHECK.json. The count is exactly1 and agrees with the
four zero-coordinate labels of its certified controller route. No old root
BFS, graph generation, single-edge-deletion graph, solver or Lean build is
performed. Full gate CPU is0.063980878 seconds within60CPU, singleworker.

## Decision changed by the test

Stop all pure edge thinning, perfect-matching deletion and same-vertex
degree19 subgraph searches on this fixed3840 graph. The apparent redundancy
in adjacent-layer pencils cannot remove the unique distant route obligations.
A useful next rule would have to replace lost distant routes with genuinely
new edges, change the projection mechanism or remove endpoint obligations by
deleting vertices; none of those domains is excluded or searched here.

New complete graphs:0. New general lemmas:0. New fixed-source strict domain
closed:all nonempty pure edge deletions of the accepted3840 graph. No global
optimality, new public record or additional Lean theorem is claimed.
