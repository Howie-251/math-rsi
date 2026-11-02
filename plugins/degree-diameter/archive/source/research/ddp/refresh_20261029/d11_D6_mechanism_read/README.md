# New lower bounds for the degree-diameter problem from generalized quadrangles and hexagons

Author: Rishabh Rajiv (ORCID 0009-0000-8626-5234)
DOI: 10.5281/zenodo.23052995
License: CC BY 4.0

This deposit accompanies the paper of the same title. It gives 13 graphs that improve the known
lower bounds for the degree-diameter problem, the largest order N(d,k) of a graph of maximum degree at
most d and diameter at most k, in 14 cases with d <= 20 and k <= 10:

    (d,k)   new order    previous     (d,k)   new order    previous
    (14,3)        1088        1053     (17,4)       19121       19040
    (15,3)        1539        1458     (18,4)       23956       23800
    (19,3)        2783        2470     (19,4)       25050       23970
    (20,3)        2783        2750     (11,6)      182618      156864
    (13,4)        6611        6600     (13,6)      534234      531440
    (14,4)        8288        8266     (15,6)     1424472     1417248
    (15,4)       11780       11759     (16,6)     1779528     1771560

The previous bound is the largest published order of a graph of maximum degree at most d and
diameter at most k, as of September 2026. The (20,3) bound is given by the (19,3) graph.

The graphs come from two constructions on generalized polygons: fibre extensions of the symplectic
quadrangle W(q), of diameter 3 (at (15,3) repaired by a matching on the points), and new vertices
attached to incidence graphs of generalized quadrangles and hexagons, namely a tower of hexagons at
(11,6) and surgery on compound graphs of Gomez and Fiol at the other cells of diameter 4 and 6.

## Files

- `new-lower-bounds-degree-diameter-generalized-quadrangles-hexagons.pdf`: the paper.
- `data-and-verification.zip`, which contains:
  - `witnesses/`: one JSON file per graph. For a fibre extension it gives the defining data (q, the
    field, X, X' and the class graph; at (15,3) also the gadget as a voltage lift, the matching and the
    number of pairs the matching repairs); for an attachment graph it gives the construction (the polygon,
    the blocks or levels, the tournament design, the cut sets and the attached vertices) and the
    SHA-256 hash of its edge list (of the uncompressed file).
  - `verify_witness.py`: a standalone verifier (Python 3 with numpy).
  - `allsources.c`: a bit-parallel all-sources breadth-first search in C with OpenMP, used by the
    verifier when gcc is available.
  - `graph_dD_kK_nN.adj`: the fibre extensions at (14,3) and (19,3), one vertex per line (its
    neighbours), vertices numbered from 0.
  - `graph_dD_kK_nN.edges.xz`: the other graphs, xz-compressed; a line "n m", then one edge "u v" per
    line, vertices numbered from 0. Each is byte-identical to the file verified when the graph was
    found.

## Verification

`python3 verify_witness.py` rebuilds every fibre extension from its witness and runs breadth-first search
from every vertex; at (15,3) it also checks that the pairs at distance four without the matching are
exactly the ones the paper describes. For every attachment graph it checks the construction edge by edge against the edge
list, which together with the theorems of the paper gives the diameter, and runs breadth-first search
from a sample of vertices. It prints `ALL CHECKS PASS`. With `--full` it also runs breadth-first search
from every vertex of every graph, which takes hours for the largest graphs. The other graphs listed in
Appendix B of the paper are not included.
