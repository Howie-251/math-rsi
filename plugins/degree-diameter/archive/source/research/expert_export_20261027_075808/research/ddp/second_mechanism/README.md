# New lower bounds for the degree-diameter problem from Cayley graphs, orbit graphs and lifts

Author: Rishabh Rajiv (ORCID 0009-0000-8626-5234)
DOI: 10.5281/zenodo.22928337
License: CC BY 4.0

This deposit accompanies the paper of the same title. It gives graphs that improve the known lower
bounds for the degree-diameter problem, the largest order N(d,k) of a graph of maximum degree d and
diameter k, in 21 cases with d <= 20 and k <= 10:

    (d,k)    new order    previous     (d,k)    new order    previous
    (16,2)         216         201     (8,7)       136329      135621
    (6,3)          119         111     (9,7)       298840      286770
    (5,4)          252         212     (10,7)      602863      589734
    (6,4)          441         390     (11,7)     1071928     1031240
    (20,4)       35328       34952     (12,7)     2007474     2006692
    (8,5)         5334        5253     (6,8)        78561       77343
    (13,5)       44232       43890     (8,8)       735175      735105
    (14,5)       61887       61307     (9,8)      1698630     1697688
    (18,5)      197316      174564     (7,9)      1224680     1223050
    (19,5)      222972      222684     (6,10)     1254594     1253751
    (7,7)        56952       53456

The previous bound is the largest published order of a graph of maximum degree at most d and
diameter k, as of September 2026. Of these graphs, 15 are Cayley graphs of metacyclic groups
Z_m x|_t Z_q with explicit generating sets; one is a bi-Cayley graph over Z_6 x Z_18 at (16,2); two
are affine line lifts, at (20,4) and (18,5); and three are orbit graphs of finite groups acting with
three vertex orbits: (6,3) from PGL(2,7), (5,4) from A7 and (6,4) from PSU(3,3).

## Files

- `new-lower-bounds-degree-diameter-cayley-orbit-graphs-lifts.pdf`: the paper.
- `data-and-verification.zip`, which contains:
  - `witnesses/`: one JSON file per graph with a complete description (the group parameters and
    generating set of a Cayley graph; the generators of the group on each orbit and a pair from
    each orbital of an orbit graph; the sets H, S, T and R of the bi-Cayley graph; the labelled
    base graph, the field and the chart of a lift, with the SHA-256 hash of its edge set).
  - `verify_witness.py`: a standalone verifier (Python 3; numpy optional, for speed).
  - `allsources.c`: an independent all-sources breadth-first search in C with OpenMP.
  - `graph_dD_kK_nN.adj.xz`: an explicit adjacency list of every Cayley graph and lift,
    xz-compressed: line i lists the neighbours of vertex i, with the vertices numbered from 0 as
    the verifier numbers them (the group element (a,b) of a Cayley graph is a + mb).
  - `graph_dD_kK_nN.edges`: the edge list of each orbit graph and of the bi-Cayley graph, one edge
    "u v" per line, its SHA-256 hash pinned in the witness.

Each data file agrees with the graph the verifier rebuilds from the witness.

## Verification

`python3 verify_witness.py` rebuilds every graph from its witness, checks that it is simple,
d-regular and of diameter exactly k, and prints `ALL CHECKS PASS`. It runs breadth-first search
from the identity for the Cayley graphs (which are vertex-transitive), from every vertex for the
orbit graphs, the bi-Cayley graph and the (20,4) lift, and from a fixed sample of vertices for the
(18,5) lift; `--full` searches from every vertex of the (18,5) lift as well. Without numpy, both
lifts are searched from the fixed sample. For the orbit graphs it also checks the order of the
group and its transitivity on each orbit, for the bi-Cayley graph the hypotheses of the paper's
diameter-two criterion, and for each lift that its base graph is the one described in the paper.

`allsources.c` is a second, independent program that searches from every vertex.
`python3 verify_witness.py --csr witnesses/<file>.json PREFIX` writes the graph in its input
format; then `gcc -O2 -fopenmp allsources.c -o allsources` and `./allsources PREFIX n k` print
`bad_sources=0` when every vertex is within distance k of all others.

The intermediate graphs listed in Appendix B of the paper are not included.
