# Balanced four-orbit cyclic graph: fixed batch complete

All **64 starts and 576 descent segments** completed. No D3 graph was found. The unique saved best has **172 vertices, 602 edges, degree 7 and diameter 4**, with **258 unordered pairs beyond distance 3**. Root independently reconstructed all edges and checked all 172 roots once, confirming these values.

The mathematical change is the K4 base multiplicity pattern `(3,2,2)` in place of `(4,2,1)`. The 01/23 endpoint pairs have three edges each; the other four pairs have two each. This changes short-route capacity and uses entirely new starts. The fixed base still has fourteen voltages and eleven independent coordinates after tree gauge.

## Capacity and first actual calibration

[DERIVATION.md](DERIVATION.md) gives the analytic route count and tree normalization. Direct symbolic enumeration of all length-at-most-three nonbacktracking walks gives the complete matrix

`[[83,68,74,74],[68,83,74,74],[74,74,83,68],[74,74,68,83]]`.

It matches both the analytic formulas and the counts after dropping the tree coordinates. The minimum is 68, versus 63 in the prior base; the diagonal rises from 63 to 83. Every fiber needs 43, so the test permits this family but does not prove a graph exists. Evidence is `CAPACITY_CHECK.json`.

One formal random start was independently expanded by Python into 602 edges and scored from four roots, giving misses `(34,31,30,33)`. All four complete distance arrays agree pointwise with C++ (`first.python_check.json`, `first.four_root_check.json`). The C++ result was reused as production evaluation one. No additional all-root preflight occurred.

## Exact bounded search performed

The 64 distinct legal starts are saved in `starts.json`. Their generator is Python `random.Random`, seed **20261026322**. Between-segment kicks use C++ `mt19937_64`, seed **20261026323**; both deterministic streams are recorded. No old (4,2,1) state is used.

Tree indices 0,6,10, corresponding to the first 01,02,03 edges, remain zero. The other eleven coordinates are free. Each completed one-coordinate neighborhood tries all 462 nontrivial value changes: 16 create a duplicate voltage within a parallel class and 446 are legal. Every legal trial receives four complete BFS traversals. Only strict score reductions are accepted; kicks change two distinct coordinates to different legal values. At most nine segments per start and thirty strict moves per segment were permitted.

Actual totals:

- **64 starts; 576 completed segments**.
- **2,228 full single-coordinate neighborhoods**.
- **1,652 strict coordinate moves; 512 two-coordinate kicks**.
- **1,029,336 coordinate trials; 35,648 illegal duplicate-voltage trials**.
- **994,264 legal states evaluated; 3,977,056 complete production root BFS traversals**.

The exact count identity is `994264=2228*446+64+512`. Also `2228−1652=576`, so all segments ended at a full-neighborhood local minimum rather than their thirty-move cap. The four Python preflight roots and the final independent all-root check are separate from the production BFS count.

## Saved best and independent final check

The best first appeared at evaluation 42,325, start 2, segment 4, descent step 2. Its edge groups are `01*3,23*3,02*2,13*2,03*2,12*2`, and its voltage array is

`[0,14,34, 20,10,7, 0,17, 31,35, 0,42, 14,30]`.

A voltage z on u→v adds z to the F43 coordinate. Vertex label is `43*orbit+x`. The only retained complete graph is `best.edges`; `best.json` holds its voltages, endpoint arrays, position and four spectra.

| Root | Distance 0 | Distance 1 | Distance 2 | Distance 3 | Distance 4 |
|---|---:|---:|---:|---:|---:|
| 0 | 1 | 7 | 42 | 120 | 2 |
| 1 | 1 | 7 | 42 | 117 | 5 |
| 2 | 1 | 7 | 42 | 119 | 3 |
| 3 | 1 | 7 | 42 | 120 | 2 |

The deficit sum is 12, giving `43*12/2=258` bad unordered pairs. This improves the previous base's best 387 bad pairs, while still failing D3. No claim of a new lower bound is made.

Root's unique independent check rebuilt all 602 edges exactly and performed one generic BFS from every one of the 172 vertices. It confirmed a simple connected 7-regular graph, diameter 4, and the ordered spectrum **172,1204,7224,20468,516**. This equals 43 times the sum of the four production root spectra. Evidence is `best.independent_check.json`; this worker did not repeat the final check.

## Budget and scope terminal

Single-worker production used **10.614251 CPU seconds**, including 10.045513 seconds in the complete four-root BFS calls. Capacity, first calibration, preparation and compilation were included in **1.228350 CPU seconds**; total through production was **11.845884 CPU seconds**. Root's final independent check used **0.003280041 CPU seconds**, giving **11.849164041 CPU seconds** including final validation, below the authorized 180-second budget.

The status is `COMPLETE_BOUNDED_SEARCH_NO_SOLUTION`, next position null, no restart and `family_exhausted=false`. All actual initial states, accepted strict moves, per-start counts and terminal records are saved. Pending actions are empty. No new seeds, other multiplicity pattern, or other modulus were started; the full balanced voltage family remains open.
