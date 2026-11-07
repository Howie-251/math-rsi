# Reproducible degree–diameter graph sources

This local source distribution accompanies the catalogue of **163 named graphs in 44 degree/diameter parameter pairs**, as of **5 November 2026**. The catalogue reports **49 completed concrete-graph Lean instances**. The other **114 graphs have computational or mathematical verification records**; the absence of a Lean proof does not mean absence of a validity argument.

The catalogue counts explicitly named graph instances, including intermediate extension graphs. It does not count 163 distinct algorithms or 163 certified world records. The 49 completed Lean entries are the earlier 47 plus the new (10,4) graphs of orders 2558 and 2567; no separate completed Lean entry is assigned to orders 2559–2566. Public comparison and novelty status are retained per instance in `catalog.csv`.

The newest graph has maximum degree 10, diameter 4 and **2567 vertices**, exceeding the current Comellas main-table value **2566 by one vertex** in the case study's public-source check. This is a comparison with that table, without a claim of global optimality or priority. The comparison evidence is linked from the [case study](../README.md).

## Compact graph definitions

Each graph is defined deterministically, with integer vertex labels starting at zero. The distribution uses shared input graphs, frozen neighborhood additions, finite input tables, and existing construction programs. It does not require adjacency matrices or a full edge list for every graph.

- `early_d5/`: all **103 early D5 graphs**. Three compressed original adjacency lists are shared across the families. `families.json` gives the exact ordered additions, including vertex labels and complete neighbor sets. `family_generator.py` is the preserved original replay implementation; `reproduce.py` supplies the packaged compressed inputs.
- `late_graphs/`: the original later **50 named graphs**, using the existing construction programs and their required small inputs. `cases.csv` identifies the construction adapter and original source for each instance. See its local usage instructions.
- `d10_d4/`: **10 additional graphs of orders 2558–2567**, reconstructed from one compressed public 2557-vertex input and the exact finite edits between the accepted graphs. Only orders 2565 and 2566 include an old-only 2-switch. The final 2567 step is exactly five disjoint edge deletions followed by ten spokes to one new vertex, with no subsequent switch.
- `verification/`: preserved independent checks for the non-Lean cases, D5 checkpoints, formal completion receipts for 2558 and 2567, and source-package replay results. These files state their own actual scope. Preserved checker sources are historical source evidence; their original project-relative input locations may need explicit adaptation before running them separately.
- `catalog.csv`: the current full catalogue snapshot, with n, m, degree, diameter, formalization and public-comparison status. Paths in the catalogue refer to the research workspace; use the packaged replay indices to reconstruct graphs from this distribution.
- `reproduce_index.csv`: the source-package reconstruction command for every catalogue entry.

Generation writes a text edge list with one `u v` line per undirected edge. The early generator prefixes this with `n m` and can write directly to a `.gz` output. The late constructors preserve the original format: 42 cases have an `n m` header, and eight use only edge rows with n and m specified in the catalogue. The `edge_format` column in `late_graphs/cases.csv` identifies the format. All ten `d10_d4/` outputs have an `n m` header. Rebuilding an edge list does not itself execute distance verification or Lean.

```bash
# Run from this reproduce/ directory; Python standard library only.
python3 d10_d4/reproduce.py --order 2567 --output d10_D4_n2567.edges
python3 d10_d4/reproduce.py --all --output-dir rebuilt_d10_d4
```

## The 114 cases without completed Lean

| Maximum degree, diameter | Named graphs | Vertices | Edges |
|---|---:|---:|---:|
| (10,4) | 8 | 2,559–2,566 | 12,795–12,830 |
| (11,5) | 3 | 37,629–37,631 | 205,307–205,329 |
| (12,5) | 60 | 42,343–42,402 | 245,229–245,937 |
| (13,5) | 40 | 51,418–51,457 | 324,461–324,863 |
| (21,3) | 1 | 3,900 | 40,500 |
| (22,3) | 1 | 4,125 | 45,000 |
| (35,3) | 1 | 20,580 | 360,150 |

For each D5 addition, all previous edges remain. Every selected old neighbor has spare degree, and its radius-four ball in the **current entire graph** jointly covers every existing vertex. Therefore the added vertex is at distance at most five from every previous vertex; old–old distances retain their previous bound. Induction proves the complete sequence, using the original sources' D5 bounds. The order exceeds the corresponding diameter-four Moore bound, so the diameter is exactly five.

Historical independent all-root BFS checkpoints are preserved for orders 37,629, 37,631, 42,343, 42,345 and 42,377; there are also independent new-root checks for selected later first instances. This is not a claim that all 103 prefixes separately underwent all-root BFS.

For the 3,900- and 4,125-vertex graphs, the independent checker read the literal graphs, checked labels/simplicity/degrees and retained source edges, and checked **all 150 / 375 new roots**. Old–old distances follow from the accepted all-3,750-root source result and inclusion of all source edges. Together these facts cover all vertex pairs. The 20,580-vertex graph has an independent **all-20,580-root** distance check, with exact diameter three.

### Fresh checks of this source package

The packaging run reconstructed the D5 family endpoints of orders 37,631, 42,402 and 51,457 and compared their **complete edge sets** with the saved literal graphs: all three comparisons passed.

It also independently traversed the packaged base graphs and all 103 frozen additions, recomputing every current-graph radius-four union and degree condition: **103/103 passed**, approximately **2.851 CPU seconds**. The original source D5 bounds were inherited; this was not an all-source BFS rerun. The full result is `verification/D5_CURRENT_COVER_REPLAY.json`.

```bash
python3 early_d5/reproduce.py --degree 12 --order 42402 --output graph_d12_D5_n42402.edges.gz
python3 early_d5/verify_covers.py --output checked_covers.json
```

The late constructors' replay coverage is described in `late_graphs/README.txt` and `verification/LATE_SOURCE_REPLAY_CHECKS.json`.

For this publication update, the ten new (10,4) graphs were replayed once from the packaged source and edits; **10/10 complete unordered edge sets matched the accepted saved graphs**. The result is `verification/D10_D4_SOURCE_REPLAY.json`. Historical independent full BFS summaries for all ten graphs and the completed 2558/2567 Lean receipts are preserved under `verification/d10_d4/`. The final 2567 external formal review C remains incomplete; its kernel proof and independent import passed. No search, BFS or Lean was rerun for this publication update. The complete Lean developments are not bundled as a standalone project.

## Storage and GitHub upload

The current catalogue directly points to 118 existing full text edge files, totaling **3,582,531,330 bytes** (about 3.58 GB). Of these, the 69 directly indexed files for cases without Lean total **205,195,301 bytes** (about 205 MB). Other prefixes are defined by the saved additions, and some original graph files exist outside the catalogue's explicit path fields. These totals exclude duplicate expert packages, caches and intermediate experimental files.

The largest named graph has **414,132 vertices and 19,680,570 edges**. Its uncompressed text edge list is **264,639,454 bytes**. Compact deterministic source data avoid storing overlapping large edge lists repeatedly. See `UPLOAD_README.txt` for source-package guidance.

This directory contains the source files, input tables, indices and verification records. Generated large edge lists can be reconstructed when needed. No ZIP is required or generated by this update.

Original authorship and source references are retained in the preserved programs and parameter files. The presence of a valid graph and the presence of a public-record improvement are separate statements; use the per-instance public-comparison fields for the latter.
