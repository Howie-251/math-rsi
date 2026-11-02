# Frozen prediction and scope

2026-10-29; written before the endpoint-count computation.

Test the actual strongest accepted sources, without regenerating or rechecking their D5 claim:

| Source | Literal input | Cover threshold | Saved D6 lower bound |
|---|---|---:|---:|
| 37631, max degree 11 | `research/ddp/more_graphs_20261027/h9_d11_followups/graph_d11_D5_n37631.edges` | 5 | 186033 |
| 42402, max degree 12 | `research/ddp/more_graphs_20261027/h9_redei15/production/continuation/graphs/graph_d12_D5_n42402.edges` | 9 | 364032 |
| 51457, max degree 13 | `research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/continuation/graphs/graph_d13_D5_n51457.edges` | 11 | 538740 |

Prediction to test: at least one requested source has a target fiber with fewer than its threshold many nonbacktracking base walks of length at most 6, obstructing every ordinary cover at or above that threshold. This prediction is not an asserted result; short self-fiber capacity is a possible obstruction, not assumed.

Read each literal once. For each graph use roots, in order: 0; the smallest label attaining minimum degree; the last-added vertex n−1. Deduplicate these labels and stop that graph immediately at its first root with any endpoint count below its threshold. Do not add roots. Save the actual minimum, witness, and root closed-walk counts by length. The same accumulation also saves the minimum through length 5 and its witness; no separate run is authorized.

For a directed arc v→w, exact next message is the total incoming current messages at v minus the current reverse-arc message w→v. Include the length-0 walk at the root. Use exact unsigned 64-bit integers, no saturation. Every shortest path in an ordinary graph cover projects to a nonbacktracking walk; unique path lifting gives at most one lifted endpoint per base walk. Thus a count c<k rules out diameter at most 6 in every k-sheet ordinary cover, including nonregular covers of these irregular base graphs. A passing gate is only necessary support.

Old-scope check: targeted reads of `research-wiki/DDP_METHOD_LEDGER.md` for these three orders and ordinary-cover/short-route terms, plus searches in the three corresponding source directory trees, found their accepted graph/extension/guard records but no completed ordinary-cover NB≤6 exclusion for these actual final sources. Other literal sources' cover exclusions are not transferred here.

Budget: one worker, at most 10 CPU seconds including preparation/compilation, at most three sources × three roots. No source D5 BFS, cover graph, voltage assignment, SAT, random choices, or new template. Orders k*n are prospective only. Stop after this gate.
