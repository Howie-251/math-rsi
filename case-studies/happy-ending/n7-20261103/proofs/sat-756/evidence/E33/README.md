# Certificate conventions and independent verification

The theorem endpoints remain ES(7) ≤ 81 and ES(8) ≤ 319. The parameter order in `M_n(a,b)` is always **cap, cup**. The heptagon state certificates use **cup, cap** cell coordinates; the octagon certificates use **cap, cup**. No stored data have been transposed in this revision.

## Octagon state and row data

`balanced.json` has all 252 Ferrers ideals in [5] × [5], represented as five column heights, in its pinned catalogue order. `residual.json` has the 154 allowed ideals in [4] × [6], represented by four column heights **plus one padding zero**. A state with first column 6 and second column less than 6 is excluded. An index is a catalogue index, not an assumed chronological position.

The 2,685 balanced rows and 1,164 residual cycle rows have occupied capacity seven. All 973 historical `mixed_cut` residual rows are certified directly as cycles in `formal/sources/ES8ResidualCycleData.lean`. The other 191 cycles were already cyclic in the JSON. Their original JSON classification remains provenance; it is not a different proof assumption.

For every triple in every stored cycle, `tools/check_octagon_finite.py` examines all six chronological permutations. It reconstructs directed differences from cells and forces the appropriate orientation or excludes that order by an empty difference. It independently compares all 87,220 directed boxes with the literal Lean tables. Every residual row is covered exactly once, by a cycle or a block.

## The 23 block maps: JSON and Lean

For a JSON block `map`, the row with zero-based index `rho-1` contains

```
[f_rho(0), f_rho(1), f_rho(2)]
```

These are three increasing horizontal thresholds for source row widths 0, 1, 2, with six rows in total. Mapping all 28 ideals of [2] × [6] by these row widths gives the stored 28-state `support`. The occupied capacity is 22 by Baek's four-cap theorem, giving the omission demand 6.

The same row is represented by a Lean `ES8BlockCompression.Block` as follows:

- `rowId`: its zero-based index in the residual constraint list.
- `support`: the same 28 catalogue indices.
- `thresholds[rho-1] = f_rho(1)`.
- `active`: every cell `(x,rho)` with `f_rho(0) < x ≤ f_rho(2)`.

The compressed cap label of an active cell is 1 if `x ≤ thresholds[rho-1]`, and 2 otherwise. The JSON representation records the entire state map. Lean's representation records exactly the cell-domain and growth information used by its proof. The independent checker verifies the two representations agree, reconstructs every image, covers every directed difference, and tests every necessary compressed-growth implication. Row IDs are 973 and 1165 through 1186; no IDs are imported into another source.

## Complete arithmetic and heptagon replays

The octagon checker also compares every used Lean row, leaf and tree node with JSON, verifies all branches cover both assignments, and checks every exact weighted contradiction. It does not run a solver or Lean. The geometric transfer to arbitrary planar sets remains a mathematical obligation discharged by the manuscript and formalization.

`tools/check_heptagon_replays.py` extracts all five literal refutations, compiles the separate C++ checker, and records hashes. Four proofs pass strict replay unchanged. The coverage proof has one redundant satisfied hint: clause 473786 at addition 473998. The original strict rejection is reproduced before the normalized replay omits that one hint. Clause contents, all other hints, and every sealed Lean file are unchanged. The normalization is explicit and reproducible; it is not an unreported repair to the source formula. This C++ checker is not itself formally verified.

The coverage CNF consists of 91,720 derived hole clauses, 1,448 cardinality clauses, and one padding tautology: 93,169 clauses over 461 variables, with 381,647 proof additions. All five extracted CNFs have no empty numeric row, including no trailing blank source line. The supplemental Lean module proves the corresponding general parser guard. These syntactic checks supplement the existing geometric source-necessity proofs.

Commands and trust boundaries are in the root README. The individual JSON files retain their original hashes; new audit reports are under `audit/`.

## Exact lower controls

The existing `restricted_25_points.json` uses integer homogeneous coordinates with positive denominators. The checker confirms general position, maximum cup length five, maximum cap length four, and no convex heptagon among all 480,700 seven-point subsets. This is the lower half of the restricted equality; the upper half is formalized in Lean.

The additional `residual_26_points.json` records a previously retained planar example, with its original research-archive source hash. It uses coordinates `[x,y,1]`, ordered by increasing abscissa. The convention is positive determinant for a cup. `tools/check_residual_lower.py` checks every triple for general position, computes maximum cup six and cap four, and independently enumerates all five- and four-point subsets to confirm the actual five-cup endpoints and four-cap starts. Their sets are disjoint. It also checks all 657,800 seven-point convex hulls. A genuine junction control and invalid-coordinate controls test the relevant rejection conditions.

Thus the example belongs to the residual class and proves D7 ≥ 26. It sharpens the unconditional limitation on the independently optimized additive bound to 58. It is not a lower bound of 58 on ES(7), not a new upper-bound certificate, and not claimed to have been formalized in Lean. The coordinates and checker are standalone; the historical research archive is not required to run them.
