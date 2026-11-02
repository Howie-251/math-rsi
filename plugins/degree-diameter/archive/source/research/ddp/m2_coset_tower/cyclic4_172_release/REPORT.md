# Four C43 orbits, fixed 4/2/1 base: bounded batch complete

The authorized batch completed all **33 starts and 297 descent segments**. It found no diameter-3 graph. The unique saved best is a simple connected 172-vertex 7-regular graph of diameter 4, with **387 unordered pairs beyond distance 3**, improved from 688 for the old bicayley seed. This bounded search does not exclude the cyclic-voltage family.

## Structural change and seed calibration

The exact derivation is in [DERIVATION.md](DERIVATION.md). Old right multiplication in D86 gives the four orbit labels `(A0,A1,B0,B1)` and the fourteen raw voltages

`[0,4,11,37, 41,16,12,24, 0,24, 0,19, 25,18]`.

The edge array is grouped as `01*4,23*4,02*2,13*2,03,12`. A voltage z on u→v joins `(u,x)` to `(v,x+z)`; the reverse edge uses −z. Coordinates are encoded `43*orbit+x`.

Tree edges 01#0, 02#0, 03#0 (indices 0,8,12) are fixed at zero. For the old graph the gauge is `new_x=old_x+[0,0,0,18]_orbit`, producing seed

`[0,4,11,37, 16,34,30,42, 0,24, 18,37, 0,18]`.

`run.py` rebuilt all 602 old edges from their actual D86 multiplication and matched the saved edge table exactly. It then matched the raw cyclic representation and the explicit tree-gauged permutation, again edge for edge. `calibration.json` records these matches and transfers the old verified distance spectrum; this step did not run another all-root BFS. The new evaluator's single four-root seed diagnostic `(6,6,10,10)` was reused as its first production evaluation.

Raw parameter counts grow from eleven to fourteen. The correct counts after translation gauge are **nine to eleven**, so the actual added freedom is two. In the new tree coordinates the old model imposes `v10=v13` and `v9+v11=v13 mod43`. This batch removes those two equations. No common scalar quotient is imposed on either search state. The source agent independently confirmed the scope and the full necessary symbolic capacity in `CAPACITY_SCOPE.md/json`; no symbolic filter was used to skip a trial here.

## Finite search actually performed

The deterministic RNG seed is **20261026172**. `starts.json` preserves the exact old seed plus 32 distinct legal random starts. Each start receives at most nine segments. Each segment selects a strictly improving move from the entire legal one-coordinate neighborhood, up to thirty such moves; two distinct coordinates are kicked to different legal values between segments.

Only the eleven non-tree coordinates vary. Parallel edges on the same endpoint pair must have distinct voltages; all base endpoints differ, so no loop is possible. Every legal state has degree seven and exactly 602 edges. A full coordinate neighborhood has 462 nontrivial value trials, of which 24 create a duplicate parallel voltage and 438 are legal.

Every evaluated legal state gets **four complete BFS traversals**, from coordinates zero in each orbit. Translation by C43 is transitive within every orbit, giving the exact bad-pair count `43*sum(root_misses)/2`. The old assumption that A0/A1 or B0/B1 have equal scores is not used.

Actual totals:

- 33 starts and 297 segments completed.
- 1,171 complete single-coordinate neighborhoods.
- 874 strict coordinate improvements and 264 two-coordinate kicks.
- 541,002 coordinate value trials; 28,104 illegal duplicate-voltage trials.
- **513,195 legal state evaluations**, including starts and kicks.
- **2,052,780 complete root BFS traversals**.

The counts satisfy `513195=1171*438+33+264`. Also `1171−874=297`, so every segment ended after a complete neighborhood with no strict improvement; none stopped at its thirty-move limit. These are local minima in this fixed coordinate representation, not exclusions of the whole family. No extra seed, base, group, or continuation was started.

## Unique saved best

The best was first encountered at evaluation 464,321, start 29, segment 7, descent step 4. Its voltage array is

`[0,12,33,30, 11,37,16,31, 0,7, 15,39, 0,11]`.

`best.edges` contains the complete 172-vertex, 602-edge graph; `best.json` contains the array, endpoints, exact position and four root distance spectra.

| Root orbit | Distance 0 | Distance 1 | Distance 2 | Distance 3 | Distance 4 |
|---|---:|---:|---:|---:|---:|
| A0 | 1 | 7 | 42 | 118 | 4 |
| A1 | 1 | 7 | 42 | 121 | 1 |
| B0 | 1 | 7 | 42 | 112 | 10 |
| B1 | 1 | 7 | 42 | 119 | 3 |

The summed deficit is 18, hence **387 bad unordered pairs**. All four eccentricities are 4. The old coupling equations both fail (`15≠11` and `7+39≡3≠11 mod43`), and unequal paired orbit scores reflect the lost dihedral symmetry in this partition. Its different invariant bad-pair count proves that this best is not a relabeling of the old 688-defect seed; no stronger graph-isomorphism claim is needed.

Root completed the unique independent final reconstruction and all-root graph check. All 602 reconstructed edges match exactly; all 172 roots confirm a simple connected 7-regular graph of diameter 4 and 387 bad unordered pairs. The ordered distance spectrum is `172,1204,7224,20210,774`, exactly 43 times the sum of the four production root spectra. Evidence is saved in `best.independent_check.json`. No extra final BFS was run by this worker.

## Resource and scope terminal

The run used one worker, no restarts, and **5.325263 process CPU seconds**, including 4.981151 seconds in complete four-root BFS. Preparation, exact edge calibration and compilation cost 1.298212 seconds. Recorded total is **6.626385 CPU seconds**, within the 120-second budget; wall time was 6.637787 seconds.

`search.terminal.json` and `terminal.json` record `COMPLETE_BOUNDED_SEARCH_NO_SOLUTION`, no next position and `family_exhausted=false`. `events.jsonl` preserves each strict move; per-start totals and all initial states are saved. The scope is complete as a bounded search, while existence of a D3 lift on this fixed base remains unresolved. The independent final check cost **0.003179513 CPU seconds**. Total including that check is **6.629564513 CPU seconds**. Pending actions: none.
