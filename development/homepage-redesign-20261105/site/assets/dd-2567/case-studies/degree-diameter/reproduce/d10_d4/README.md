# Ten frozen (10,4) graphs

The new (10,4) result was obtained with **MathRSI v2 and the degree–diameter
plugin**, including the subsequent handoff repair. See the
[execution-version record](../../evidence/execution_version.md).

This directory reconstructs the ten accepted graphs of orders **2558–2567**,
using only Python's standard library and these packaged files. Start in the
parent `reproduce/` directory:

```bash
python3 d10_d4/reproduce.py --order 2567 --output d10_D4_n2567.edges
python3 d10_d4/reproduce.py --all --output-dir rebuilt_d10_d4
```

Every output begins with `n m`, followed by one `u v` line for each undirected
edge, on labels `0..n-1`. Each graph has `m = 5n` edges. The program performs
finite edge edits; it does not perform search, distance checks or a Lean build.

`source_2557.edges.gz` is the shared 2557-vertex input, taken from the source
saved with the accepted 2558 construction. Its published source is the
[Comellas degree–diameter collection](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD4/deg10-dia4-n2557.edges).
The package preserves the source labels and edges, with a size header added.
This is the construction baseline, not the later public comparison value 2566.

`edits.json` records the literal unordered edge-set difference between each
accepted graph and its predecessor. It also preserves the five selected cuts,
the explicit old-only switch where present, and the original graph, parameter,
generator and evidence locations as attribution. Those historical paths are
descriptive; the replay program does not access them.

Each step deletes five disjoint old edges and attaches a new vertex to their
ten endpoints. **Only the steps producing 2565 and 2566 then apply an old-only
2-switch.** Their stored deltas include those two removed and two added old
edges. The final **2567 step has no subsequent switch**: it removes
`(193,2362), (192,2363), (417,2555), (2508,2565), (2511,2528)` from our local
2566 graph and attaches vertex 2566 to all ten endpoints. Thus its delta is
exactly five removed edges and ten added edges.

The publication packaging run replayed the whole chain once and compared
every reconstructed unordered edge set against its accepted saved graph.
All ten matched. See
[`D10_D4_SOURCE_REPLAY.json`](../verification/D10_D4_SOURCE_REPLAY.json).
This comparison did not rerun mathematical validation.

Historical independent all-root BFS summaries for all ten graphs are in
[`verification/d10_d4/`](../verification/d10_d4/). They report simple,
connected, 10-regular graphs of exact diameter four. Completed original-target
Lean results and independent imports are recorded for **2558 and 2567**;
the eight intermediate graphs have no separately completed concrete-graph
Lean entry in the catalogue. The final 2567 result has passed the Lean kernel
and independent import. Its final external formal review C is incomplete;
this is a review-status limitation, not a failed graph check or kernel proof.

Only compact verification receipts are included here. This package does not
include the full Lean development or its dependencies and therefore does not
offer a standalone rebuild of those formal proofs. No Lean or BFS was rerun
for this publication update.
