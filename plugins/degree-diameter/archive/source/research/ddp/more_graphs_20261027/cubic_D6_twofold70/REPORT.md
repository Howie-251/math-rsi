# Fixed AFY70 ordinary two-cover cannot have diameter6

The complete route-capacity check excludes every ordinary2-cover of this fixed70-point source as a degree3/D6 candidate. No voltage assignment, linear solver or140-point graph was run. The graph family is excluded by the same-fiber obstruction before any search.

Fresh [Comellas table](https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html) reading confirms(3,6)=132 and its cell is not bold; the table defines bold entries as optimal. The proposed140 points would therefore exceed the current listed lower bound. The exact cell HTML and reading time are saved in BASELINE.json.

One source was fixed before the route check: the official D5 page's integer-labeled [AFY70 adjacency](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD5/AlFiYe70_Z_adjlist.txt), link6 of the [official description](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g5.html). Credit: I.Alegre, M.A.Fiol and J.L.A.Yebra. The literal graph is simple, connected, nonbipartite and3-regular, with70 vertices and105 edges. Its known diameter5 is inherited from that description; no ordinary-source BFS was repeated. Neither another70 adjacency source nor an alternative base graph was tried.

The unique method-ledger/Wiki check found the earlier cubic exact-NB controller bounds, not this specific ordinary70-point two-cover profile. The source was parsed from its NetworkX-style upper adjacency rows into source70.edges; SOURCE.json preserves all edge IDs, the spanning tree and the36 cotree variables.

For any F2 edge voltage assignment, cancelling an immediate reverse pair of base edges preserves both its endpoint and sheet voltage. Consequently every lift walk of length≤6 reduces to one of the enumerated nonbacktracking base walks of length≤6. A spanning-tree gauge sets69 voltages tozero; the remaining36 variables represent all2-covers up to vertex sheet switches. Route forms were deduplicated as actual F2 edge-parity forms, so a closed walk and its reverse were not falsely counted as independent sheet choices.

All70 roots were enumerated once. Reduced-walk counts by length0..6 are[70,210,420,840,1680,3360,6720]. The4900 ordered base-pair slots have distinct-form histogram:

| Number of formal endpoint voltages | Ordered slots |
|---:|---:|
| 1 | 1204 |
| 2 | 336 |
| 3 | 2016 |
| 4 | 1344 |

All70 diagonal slots have only the zero form, and1134 distinct-endpoint ordered slots also have capacity1. For the first witness0→0, the complete reduced-route list is just the empty path[0], with form0. Thus in every two-cover, the two vertices above base0 cannot be joined within6 steps. Immediate backtracking cannot repair that obstruction because its voltage cancels. Every ordinary two-cover of this source therefore has diameter at least7, or is disconnected; it cannot supply the proposed(3,6)140 graph.

The capacity prediction was refuted. The conditional linear stage was not entered, and voltage_assignments_tested=0. Actual candidate order and diameter remain null because no lift graph was generated. Recorded computation CPU was0.02555s, below the5CPU budget; no dependencies or hashes were added. The fixed source rule stops here, with no alternate70 source, seeds or voltage search.

Evidence: PREDICTION.json; BASELINE.json; SOURCE.json; source70.adjlist.txt; source70.edges; route_forms.json; capacity_witness.json; RESULT.json; terminal.json; check.py.
