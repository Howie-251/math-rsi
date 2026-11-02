# Fixed AFY70 three-cover cannot have diameter7

The new210-point(3,7) proposal is excluded by short-route capacity, before any voltage assignment or linear elimination. The obstruction is stronger than a failure of cyclicC3 voltages: it excludes every ordinary3-sheet cover of this fixed70-point source.

The already-downloaded fresh [Comellas table](https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html) still gives(3,7)=200 and a nonbold cell. BASELINE.json records the reused snapshot, exact cell and original reading time; no extra network request was made. The source is the same fixed [official AFY70 integer adjacency](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD5/AlFiYe70_Z_adjlist.txt), not a new70-point graph. Its complete edge list and36-variable spanning-tree gauge are inherited from the precedingD6 preflight, which remains unchanged.

This step had a separate rationale: theD6 test ruled out nontrivial closed routes through length6, so length7 was the next possible place for a closed route and its inverse to supply two nonzeroC3 displacements alongside identity. The new prediction was that all endpoint slots would now support at least3 formal voltages.

All nonbacktracking walks of lengths0..7 were enumerated from all70 roots. The counts by length are[70,210,420,840,1680,3360,6720,13440]. Canonically directed edges have F3 coefficient+1; reverse edges have−1=2, and route coefficients are added coordinatewise modulo3. The36 cotree coordinates represent all cyclicC3 assignments up to vertex sheet switches. They are not F2 parity forms.

| Distinct F3 forms per ordered slot | Slots | Raw reduced-route count |
|---|---:|---:|
| 1 | 364 | 1 |
| 3 | 672 | 3 |
| 5 | 1008 | 5 |
| 6 | 1344 | 6 |
| 7 | 1176 | 7 |
| 9 | 336 | 9 |

All70 diagonal slots have only the empty route, not merely several routes whoseF3 coefficients coincide. Another294 distinct-endpoint ordered slots also have only1 route. For the first witness0→0, the sole route is[0], with zero coefficients.

In any ordinary cover, a base walk lifts uniquely from a specified lifted source. A lifted route of length≤7 can have all immediate edge reversals cancelled without changing its endpoints. Since no nonempty reduced base route of length≤7 returns to0, the other two vertices above0 cannot be reached within7 from its first sheet. This argument does not require commutativity or cyclic edge permutations. Thus every3-sheet cover of this fixed source has diameter at least8, or is disconnected.

The capacity prediction is refuted. No voltage assignment was tested and no210-point graph was generated, so actual_n and actual_D remain null. The conditional tight3-form linear stage was not run. Its planned necessary condition remains correctly stated: threeF3 values are distinct exactly when their sum iszero and the first two differ; consistent tight necessities alone would not have been a graph witness.

Recorded route/check CPU was0.04134s, below5CPU. No source BFS, dependency, hash, alternative source, fiber count or subsequent search was used. Evidence: PREDICTION.json, BASELINE.json, route_forms.json, capacity_witness.json, RESULT.json, terminal.json and check.py. This is a fixed-source covering obstruction, not an impossibility result for arbitrary(3,7)210-point graphs.
