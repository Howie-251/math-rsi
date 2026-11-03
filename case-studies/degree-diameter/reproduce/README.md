# Reproducible degree–diameter graph sources

This local source distribution accompanies a frozen catalogue of **153 named graphs in 43 degree/diameter parameter pairs**. The catalogue reports **47 completed concrete-graph Lean instances**. The other **106 graphs have computational or mathematical verification records**; the absence of a Lean proof does not mean absence of a validity argument.

The catalogue counts explicitly named graph instances, including intermediate prefixes of three extension sequences. It does not count 153 distinct algorithms or 153 certified world records. Public comparison and novelty status are retained per instance in `catalog.csv`.

## Compact graph definitions

Each graph is defined deterministically, with integer vertex labels starting at zero. The distribution uses shared input graphs, frozen neighborhood additions, finite input tables, and existing construction programs. It does not require adjacency matrices or a full edge list for every graph.

- `early_d5/`: all **103 early D5 graphs**. Three compressed original adjacency lists are shared across the families. `families.json` gives the exact ordered additions, including vertex labels and complete neighbor sets. `family_generator.py` is the preserved original replay implementation; `reproduce.py` supplies the packaged compressed inputs.
- `late_graphs/`: the other **50 named graphs**, using the existing construction programs and their required small inputs. `cases.csv` identifies the construction adapter and original source for each instance. See its local usage instructions.
- `verification/`: preserved independent checks for the non-Lean cases, D5 checkpoints, and the fresh current-cover replay described below. These files state their own actual scope. Preserved checker sources are historical source evidence; their original project-relative input locations may need explicit adaptation before running them separately.
- `catalog.csv`: the original full catalogue snapshot, with n, m, degree, diameter, formalization and public-comparison status. Paths in this original catalogue refer to the research workspace; use the packaged replay indices to reconstruct graphs from this distribution.
- `reproduce_index.csv`: the source-package reconstruction command for every catalogue entry.

Generation writes a text edge list with one `u v` line per undirected edge. The early generator prefixes this with `n m` and can write directly to a `.gz` output. The late constructors preserve the original format: 42 cases have an `n m` header, and eight use only edge rows with n and m specified in the catalogue. The `edge_format` column in `late_graphs/cases.csv` identifies the format. Rebuilding an edge list does not itself execute distance verification or Lean.

## The 106 cases without completed Lean

| Maximum degree, diameter | Named graphs | Vertices | Edges |
|---|---:|---:|---:|
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

The late constructors' replay coverage is described in `late_graphs/README.txt` and `verification/LATE_SOURCE_REPLAY_CHECKS.json`. Historical Lean completion is reported from the original records; this distribution does not claim a fresh Lean build for all 47 cases.

## Storage and GitHub upload

The original catalogue directly points to 108 existing full text edge files, totaling **3,581,360,970 bytes** (about 3.58 GB). Of these, the 61 directly indexed files for cases without Lean total **204,259,013 bytes** (about 204 MB). Other prefixes are defined by the saved additions, and some original graph files exist outside the catalogue's explicit path fields. These totals exclude duplicate expert packages, caches and intermediate experimental files.

The largest named graph has **414,132 vertices and 19,680,570 edges**. Its uncompressed text edge list is **264,639,454 bytes**. Compact deterministic source data avoid storing overlapping large edge lists repeatedly. See `UPLOAD_README.txt` for the measured final source/ZIP sizes and upload instructions.

Upload this directory's source files, input tables, indices and verification records to the destination GitHub repository. Generated large edge lists can be reconstructed when needed. The accompanying ZIP is a convenient way to transfer the source directory; expanding its contents in the repository makes the programs and inputs directly readable.

Original authorship and source references are retained in the preserved programs and parameter files. The presence of a valid graph and the presence of a public-record improvement are separate statements; use the per-instance public-comparison fields for the latter.
