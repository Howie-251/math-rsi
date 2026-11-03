# Complete D64 / Q64 phase-capacity comparison

Both **8192-mask ranges are complete**. The common four-orbit base has
cross counts (3,3,2,2,3,3), sixteen edges, three tree voltages fixed to
the identity, and thirteen free group voltages.

| Group | Capacity passes | Tight 32-form slots in survivors | Best minimum | Leading phase mask |
|---|---:|---:|---:|---:|
| D64 | 1953 | 3024 | 36 | 239 |
| Q64 | 7930 | 144 | 52 | 1205 |

The required minimum is 32 in every root–target–phase slot. These are
necessary symbolic counts; no coordinate assignment or graph has been
tested. **Zero actual graphs and zero BFS roots** were produced.

The nonabelian multiplication separates some short-word collisions
present in cyclic lifts. Q64 additionally separates a closed odd-phase
walk from its inverse by the central displacement 16, while D64 merges
them. This distinction is included explicitly in the affine forms.
Q64's counts are at least D64's in all 262144 slots, and it adds 5977
passing phase masks. This is a structural capacity difference, not a
claim that an actual D3 graph exists.

The leading patterns' matrices below list the even/odd phase capacities
for each root and target orbit.

    D64 mask 239:
    (51,36) (39,55) (45,55) (57,37)
    (39,55) (51,36) (37,57) (55,45)
    (45,55) (37,57) (51,36) (62,37)
    (57,37) (55,45) (62,37) (51,36)

    Q64 mask 1205:
    (59,64) (52,59) (52,59) (54,52)
    (52,59) (59,64) (54,52) (52,59)
    (52,59) (54,52) (59,64) (52,59)
    (54,52) (52,59) (52,59) (59,64)

CPU recorded for compilation, preparation, and both runs was
**2.365815 seconds**, including D64 0.673705 and Q64 0.628332 seconds.
The completed-table comparison added 0.331696818 seconds, totaling
**2.697511818 CPU seconds** in this task. Both processes exited 0.
No phase permutation or unproved projective reduction was used.

Read [STRUCTURE_SCOPE.md](STRUCTURE_SCOPE.md) for group multiplication,
inverses, full tree-gauge coverage, coefficient/constant propagation,
four-root symmetry, and the exact remaining coverage condition.

Files and interface:

- [topology.json](topology.json): edge IDs, tree IDs, free coordinate
  order, and phase-mask convention.
- [d64/results.json](d64/results.json), [q64/results.json](q64/results.json):
  full summaries and minimum-capacity histograms.
- Each group directory contains `all_patterns.jsonl`, `survivors.json`,
  `best_phase.json`, and `paths.json`.
- Each `forms_tight.jsonl` records every exactly-32-form slot of a
  passing mask. Each form has thirteen signed coefficients interpreted
  modulo 32 and a separate constant 0 or 16. The fixed order is in
  `topology.json`; these files can feed necessary ring congruences.
- [comparison.json](comparison.json): comparison of the already saved
  tables; it does not evaluate any voltage assignment.
- [capacity.cpp](capacity.cpp), [run.py](run.py), [terminal.json](terminal.json):
  deterministic producer, sequential budgeted runner, and completed scope.

The separate ring-congruence analysis, if used, has its own output and
timing. It does not change the phase counts recorded here.

The paper-only [Q64 self/odd reduction](Q64_SELF_ODD_COVERAGE.md) gives exact modulo-16 coverage and the safe full-graph lower bound `64*sum(delta_i)`. It performs no extra computation and does not guarantee a positive defect.

## Observed central-quotient obstruction in the later saved best

The separately completed Q64 graph batch saved a D4 graph with 832 bad
pairs. Its four self/odd slots are complete, so the preceding self/odd
bound is zero there. The saved diagnosis instead has an entire missing
central pair: orbit 0 to orbit 3, odd phase, x=3 and 19, and the reverse
class pair. Quotienting by the central element (16,0) gives a four-orbit
D32 graph on 128 vertices. The quotient's four-root deficits are
(1,0,0,1), with distance-four missing targets.

Holding the current phases and all coordinates modulo 16 fixed leaves
this quotient unchanged under all 2^13 central flips. Every legal such
lift therefore has at least four representative misses and **at least
128 unordered bad pairs**. The appendix to
[Q64_SELF_ODD_COVERAGE.md](Q64_SELF_ODD_COVERAGE.md) proves the walk-lifting
identity and this bound. It is a paper consequence of the saved data;
no central assignments or BFS were run. Other modulo-16 assignments
remain outside this exclusion. Quotient-first optimization and binary
lifting remain unexecuted proposals.
