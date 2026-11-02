# Disjoint nonunit complement: fixed K4 / Z20 family

Before execution, 2026-11-01 UTC. The original `../PREDICTION.md`, raw search, and STOP files remain unchanged.

The original g01=1 exhaustive domain rules out every assignment having at least one unit shift, by base relabeling and multiplication of every deck coordinate by a unit. For the remaining family, disconnected assignments cannot satisfy the complete same/nonadjacent NB3 interface. The proof in `SYMMETRY_AND_CONNECTEDNESS.md` reduces every connected assignment whose shifts are all nonunits to g01=5, with the remaining five shifts in

`U=[2,4,5,6,8,10,12,14,15,16,18]`.

Enumerate these five coordinates in the displayed lexicographic order: 11^5=161,051 assignments. Exactly the 3^5=243 assignments whose other shifts all lie in {5,10,15} are disconnected and are skipped by the proved connectivity criterion. Check all remaining 160,808 assignments using the original 600 saved word coefficient rows, with the original exact 296 translation-class NB3 bitset predicate. No rerun of g01=1 or recomputation of its search results.

Prediction: this disjoint complement may also fail completely. A complete failure, combined with the symmetry and connectivity proof and the original complete anchor1 search, closes the entire six-nonzero-shift K4-double-voltage / Z20 family for this NB3 source interface. It does not close all 80-vertex controllers, and an interface failure does not establish a distance claim for any ungenerated fiber graph. A passing candidate instead stops at the first complete witness and is reported for root production decision.

One worker. At most 5 additional CPU seconds including compilation, deducted from the original 30-second total budget after the original 1.094645045 seconds. No other modulus, group, seed, timer continuation, fiber graph, BFS, solver, Lean, installation, hashes, old graph revalidation or accepted-count changes.
