# Improved lower bounds for the degree-diameter problem from metacyclic groups, coset graphs and affine lifts

Author: Rishabh Rajiv (ORCID 0009-0000-8626-5234)
DOI: 10.5281/zenodo.22073603
License: CC BY 4.0

This deposit accompanies the note of the same title. It presents graphs that
improve the best published lower bounds for the degree-diameter problem, the
largest order N(d,k) of a graph of maximum degree d and diameter k, in eighteen
parameter pairs with d <= 20 and k <= 10:

    (d,k)   new order   previous     (d,k)   new order   previous
    (14,3)        1053        1032    (20,5)      450000      281820
    (20,3)        2750        1958    (7,7)        53456       53020
    (6,5)         1518        1404    (8,7)       133887      133446
    (10,5)       14047       13734    (10,7)      589734      583083
    (13,5)       43890       42900    (12,7)     2006692     2005819
    (15,5)       80704       80190    (6,8)        77343       77257
    (17,5)      142044      133144    (7,8)       254268      249660
    (18,5)      174564      171828    (8,8)       735105      734820
    (19,5)      222684      221676    (6,10)     1253751     1253615

Fifteen graphs are Cayley graphs of metacyclic groups Z_m x|_t Z_q with
explicit generating sets. One is a coset graph of a simple group: PSL(2,23)
at (6,5). Two are affine line lifts, a construction defined in the note, at
(20,3) and (20,5); the (20,5) graph on 450000 vertices exceeds the previous
bound by 59.7 percent. Baselines were checked against the table of
F. Comellas (2026-08-23) and the Combinatorics Wiki general table (2026-08-24).

## Files

- `improved-lower-bounds-degree-diameter-metacyclic-coset-affine-lifts.pdf`
  the note.
- `data-and-verification.zip` — the complete dataset:
  - `witnesses/` — 18 JSON files, one per record, each a complete
    machine-readable description of its graph;
  - `verify_witness.py` — standalone verifier (Python 3, standard library
    only, no dependence on any search code). Running
    `python3 verify_witness.py` rebuilds every graph from its witness and
    checks it is simple, connected, d-regular, and of diameter exactly k;
    it prints `ALL CHECKS PASS`. Non-vertex-transitive graphs are checked
    by breadth-first search from every vertex; `--full` extends this to all
    450000 sources of the largest lift (slow in Python; see `allsources.c`,
    the C program used for that sweep: every eccentricity equals 5 exactly);
  - adjacency data: an explicit adjacency list for every record graph,
    `graph_dD_kK_nN.adj` (one vertex per line, 0-indexed, plain text for
    n <= 3000 and `.adj.xz` above), plus a canonical `.edges` list for the
    coset graph, sha256-pinned in its witness. Every graph is also
    regenerated exactly by the verifier from its witness alone.

This deposit supersedes "Four new largest known graphs of diameter three"
(doi:10.5281/zenodo.21180071) at two of its four cells, d = 14 and d = 20,
which appear here with larger orders.
