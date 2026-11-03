# 172-point degree-preserving two-edge-switch neighborhood

The fixed source is the independently checked balanced322 graph:172 vertices,602 edges,7-regular,diameter4,258 unordered pairs farther than3.

Every unordered pair of distinct old edges and both nontrivial reconnections was considered. Four distinct endpoints and absence of both new edges preserve simplicity and every vertex degree. All361802 slots completed:28896 illegal and332906 legal. There were no strictly improving moves.

The score uses all172 roots without assuming cyclic symmetry. For each root,closed radius2 is the union of its own closed neighborhood with the neighborhoods of its neighbors; closed radius3 is radius2 together with radius2 of each neighbor. Missing ordered targets are summed and halved. A partial ordered sum at least twice the current strict bound safely rejects a candidate;332905 such cutoffs and one complete bitset score occurred. Cutoffs are not exact scores. The first actual legal candidate was independently calibrated by ordinary172-root BFS against its uncut bitset score.

The source and final edge sets coincide with the same labels:best.edge_comparison.json. The previous independent all172-root check is reused; zero additional final BFS runs. Actual preparation and productionCPU1.737148 seconds,edge comparisonCPU0.001005844 seconds. The original180CPU budget was not exhausted. terminal.json has no pending work.

This closes only the strict two-edge-switch neighborhood of one graph. It does not exclude sequences with neutral or worsening steps,other cyclic assignments,or arbitrary172-point graphs. Each evaluated improvement would have been saved before undo; best observed and current committed scores have separate terminal fields.
