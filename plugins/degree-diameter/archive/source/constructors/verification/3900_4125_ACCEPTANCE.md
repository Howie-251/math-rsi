# Independent acceptance of the two terminal graphs

Executed 2026-11-01. **PASS** for both literal terminal edge lists. The standard-library checker was written independently of the producer and run once, on one worker. Total measured CPU time was **0.342881714 seconds**, within the predeclared 45-second budget; no old-root BFS was rerun.

| Target | Actual vertices | Actual edges | Degree histogram | Old edges retained | New roots fully checked | Exact diameter | Per-graph CPU seconds |
|---|---:|---:|---|---:|---:|---:|---:|
| (21,3) | 3,900 | 40,500 | 900 degree-20; 3,000 degree-21 | 37,500 / 37,500 | 150 / 150 | 3 | 0.103998768 |
| (22,3) | 4,125 | 45,000 | 375 degree-20; 3,750 degree-22 | 37,500 / 37,500 | 375 / 375 | 3 | 0.183998183 |

Both headers agree with every parsed edge row. Both graphs are simple, have legal vertex labels, and have symmetric adjacency reconstructed from unordered edge rows. There are no loops or duplicate unordered edges. The maximum degrees are exactly 21 and 22 respectively.

The complete distance argument has two parts. The old source has a previously accepted independent all-3,750-root D3 result, and all 37,500 source edges remain in each terminal graph. Hence every old-old pair retains a path of length at most 3. Independently executed BFS from every newly labeled vertex reaches every vertex of its terminal graph within three steps. This covers every pair having a new endpoint, and undirectedness covers either order. Some checked vertices occur at distance 3, so the diameter is exactly 3. There is no counterexample.

The machine-readable result stores every new root, its four BFS layer counts, reached count, and eccentricity. Inputs are only the three literal edge lists and the selected old validation fields. No production recipe, generator, formula, or cached ball was used by the checker.

This same-family review accepts the deterministic graph evidence. Subjective assessments remain provisional. Only the **two terminal graphs** are accepted here: the 525 roots checked across them do not constitute independent validation of 525 construction prefixes. Public maximum orders for degrees 21 and 22 remain unknown in this task, novelty remains pending, no global-record claim is made, and neither new graph has completed Lean formalization. No further search was opened.

Artifacts:

- [Pre-execution scope](SCOPE.md)
- [Independent checker](check_literal_terminal_graphs.py)
- [Full measured result](INDEPENDENT_ACCEPTANCE.json)
