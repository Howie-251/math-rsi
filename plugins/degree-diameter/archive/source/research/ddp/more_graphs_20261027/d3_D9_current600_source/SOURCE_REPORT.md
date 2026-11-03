# Current (3,9) Exoo600: the bipartite premise is false

The [current primary diameter-9 description](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g9.html) lists Exoo600 as a voltage graph and supplies an [implicit adjacency literal](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD9/Exoo_600.txt). Its 600 rows already use labels 0 through 599; row number is the vertex and each row contains its three neighbours.

The downloaded literal is saved unchanged as `source600.author.adj`. Exact local checks give 600 vertices, 900 edges, simple reciprocal adjacency, and degree 3 everywhere. Union-find verifies connectedness. Parity union-find over all 900 edges proves **non-bipartiteness**, with its first parity contradiction on edge `(215,465)`. This did not compute graph distances. `source600.edges` contains the same literal as sorted zero-based edges, preceded by header `600 900`; the source profile CPU was about 0.0025 seconds. The published diameter 9 is inherited, not rechecked.

The proposed bipartite/odd-diameter reason for automatic subdivision-root coverage therefore does not apply to this actual source. No single-edge or cooperative graft was generated or tested; non-bipartiteness alone does not prove that every such graft fails. The requested branch stops at the false premise.

The current page supplies no concrete voltage assignment or symmetry order. Its Sage link points to `adjD7/600_exoo_SageMath.txt` and returns 404, so edge/vertex transitivity remain unbound. In particular the two symmetric C600 graphs in Conder's census, whose diameters are 12 and 20, must not be substituted for this Exoo diameter-9 source. No automorphism search or fallback source was started.

A targeted exact-source ledger lookup found the older source360/Q8 experiment targeting (3,9), but no Exoo600 source/operation record. That different-source failure is not inherited as an exclusion here. The correct conditional subdivision-root statement is saved in `CONDITIONAL_SUBDIVISION_LEMMA.md` for reuse, with its hypothesis explicitly unsatisfied here.
