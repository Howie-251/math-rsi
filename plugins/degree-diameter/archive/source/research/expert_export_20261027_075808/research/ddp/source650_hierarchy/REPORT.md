# Published 650 graph: exact hierarchy

Input is the existing complete `m1_degree5_transfer/rithwik650_source.edges` (650 vertices, 1,625 edges). No external input or construction search was used. `compress.py` reads the original edge order and the already computed exact single-edge damage table. `compressed_graph.json` preserves every original vertex label and every port-level edge. Reconstructing from this object gives exactly all 1,625 original edges.

Let V0 be the 500 endpoints of the 250 minimum-damage (45) edges, V1 the 125 neighbors outside V0, and V2 the remaining 25 vertices. Every V0 vertex has four V0 neighbors and one V1 neighbor; every V1 vertex has four V0 neighbors and one V2 neighbor; every V2 vertex has five V1 neighbors. The only layer edge classes are V0–V0 (1,000), V0–V1 (500), V1–V2 (125).

The damage classes locate exactly as follows:

| Single-edge damage | Edges | Layer pair |
|---:|---:|---|
| 45 | 250 | V0–V0 |
| 49 | 250 | V0–V0 |
| 65 | 125 | V1–V2 |
| 78 | 500 | V0–V0 |
| 79 | 500 | V0–V1 |

Each V1 vertex defines a disjoint four-vertex V0 block, giving 125 blocks. Every block has zero internal edges. Between two blocks there is at most one V0 edge; the resulting block quotient is a simple 16-regular graph on 125 vertices. Thus the port assignments, not merely the quotient, are needed to recover the 4-regular V0 graph.

Each V2 vertex groups five blocks. No V0 edge joins blocks of the same group. Every pair of the 25 groups is joined: 250 group pairs have three V0 edges and 50 group pairs have five. At the five-block level, all these connections are matchings: a three-edge partial matching or a five-edge perfect matching. The 50 five-edge group pairs form five disjoint K5 components on the group labels. Their explicit components, all block matrices, and every individual port edge are saved.

This is an exact compressed description and exposes substantial nested structure. It does not yet provide an algebraic or parameterized construction rule: the 125-block adjacency, partial-matching choices, and port assignments remain explicit input. No automorphism group or applicability to other orders is claimed.
