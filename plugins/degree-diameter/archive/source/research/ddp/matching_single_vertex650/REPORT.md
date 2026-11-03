# Complete 650-to-651 single-vertex, two-matching-edge check

The entire specified finite family is excluded: **every pair of disjoint old edges leaves at least 19 old vertices farther than five steps from the new vertex**. All 1,319,500 unordered old-edge pairs were visited; 6500 shared an endpoint and were rejected, leaving **1,313,000 legal two-edge matchings**. None passed the exact new-root coverage condition. This excludes this extension of the specified 650-vertex source, not arbitrary graphs of maximum degree 5 on 651 vertices.

## Construction and exact necessary condition

Read the existing source `research/ddp/m1_degree5_transfer/rithwik650_source.edges`, a simple 5-regular, diameter-5 graph on 650 vertices with 1625 edges. Delete two edges with four distinct endpoints `T`, and add one new vertex `w=650` adjacent to all four endpoints. The old vertices retain degree 5, while the new vertex has degree 4. Thus the graph is simple, has **maximum degree 5**, and has 651 vertices and 1627 edges. Regularity is not an acceptance requirement. Connectivity follows by replacing a deleted edge `a-b` by `a-w-b` in any original walk.

Let `H` denote the old graph after the two deletions. A shortest original path from any old `x` to the set `T` cannot traverse either deleted edge: it would already have reached a member of `T` before doing so. Hence

```
d_H(x,T)=d_G(x,T),
d_F(w,x)=d_G(x,T)+1.
```

The new root covers all old vertices within five steps **if and only if** the union of the original radius-4 closed balls around the four endpoints is all 650 vertices. The implementation computes these original balls exactly, packs them into 11 words, and tests the union for every unordered pair of edges with disjoint endpoints.

For completeness, the intended second filter uses the union of the exact single-edge damage sets `D_e={ {x,y}:d_(G−e)(x,y)>5 }`. For a pair in that union, the only new shortcut has length `d_G(x,T)+d_G(y,T)+2`; a sum greater than 3 therefore proves that the old pair remains bad. Only candidates passing both necessary conditions would receive full 651-root BFS in the enumeration. **No candidate reached this second filter**, because every legal pair failed the new-root test.

## Complete enumeration result

| Quantity | Result |
|---|---:|
| All unordered edge pairs | 1319500 |
| Shared-endpoint pairs | 6500 |
| Disjoint edge pairs | 1313000 |
| New-root coverage failures | 1313000 |
| New-root coverage passes | 0 |
| Second-filter evaluations | 0 |
| Full candidate BFS runs inside enumeration | 0 |
| Minimum new-root missing count | 19 |
| Pairs attaining that minimum | 250 |
| Maximum new-root missing count | 52 |

The 6500 incompatible pairs also equal `650*binomial(5,2)`, as expected for a simple 5-regular source. Every legal candidate has between 19 and 52 new–old bad pairs. The full histogram is stored in `complete.summary.json`.

The completed cursor contains all 1624 nonempty outer rows and all 1,319,500 edge pairs. The terminal state is `COMPLETE_NO_SOLUTION`; CPU time was **0.361017 seconds**, including 0.011999 seconds of preprocessing, and wall time was 0.364596 seconds. The run was single-core with a 119-second internal allowance and a 120-second process CPU limit. No random seed, extra group, or follow-on queue was used.

## Saved complete failure graph

The first candidate achieving the minimum new-root missing count deletes edges with source IDs `1,527`:

```
(0,251), (105,371).
```

The new vertex 650 is joined to `0,251,105,371`. Its complete edge list is `complete.best_filtered.edges`; exact parameters are in `complete.best_filtered.json`. It has exactly 19 new–old pairs at distance greater than 5.

After the enumeration finished, the root agent independently ran the existing full edge-list verifier from all 651 roots. Its result in `complete.best_filtered.independent_bfs.json` confirms a simple connected graph with minimum degree 4, maximum degree 5, diameter **6**, and **59 total bad unordered pairs**. Thus this saved graph has 19 new–old and 40 old–old bad pairs. **The value 59 is not a global minimum over the family**: the enumeration minimized the exact new-root missing count, not total bad pairs, and did not evaluate every graph by full BFS.

More generally, every graph in this family has diameter at most 6. Given an original shortest path of length at most 5, if it uses deleted edges, replace the segment from the first deleted edge's entry endpoint to the last deleted edge's exit endpoint by the two-edge route through `w`. That segment originally has length at least one, so the replacement increases the path length by at most one. New-root distances are also at most 6 by the exact formula. Combined with the coverage failures, every legal candidate has diameter exactly 6, without requiring a separate all-root BFS for each one.

## Files and scope

All files are in `research/ddp/matching_single_vertex650/`:

- `enumerate_pairs.cpp`, `enumerate_pairs`: the complete fixed-source enumeration.
- `critical_upto5_pairs.txt`, `critical_export.json`, `export_critical_pairs.cpp`: the independently prepared complete single-deletion damage sets. Their 110125 edge/pair incidences agree with the earlier 650-source diagnosis. They were loaded, but the second filter was never needed.
- `complete.summary.json`, `complete.progress.jsonl`, `complete.log`, `process.json`: terminal counts, full first-filter histogram, completed cursor, command and process record.
- `complete.best_filtered.edges`, `complete.best_filtered.json`: the saved full failure graph, selected by new-root coverage.
- `complete.best_filtered.independent_bfs.json`: the root agent's independent all-651-root verification of that one saved graph.

An independent Python integer-bitset enumeration also compared the entire coverage histogram over all 1,313,000 disjoint edge pairs with the C++ result. Every entry matched, including minimum 19, its multiplicity 250, and zero fully covered cases. This check took 0.844 CPU seconds and did not rerun candidate BFS; see `independent_coverage_check.json` and its Python source.

The source graph was not changed. The enumeration is finished; it does not rule out different insertions, more deleted edges, or arbitrary nonregular 651-vertex graphs of maximum degree 5.
