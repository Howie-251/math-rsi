# One new quotient trajectory after the pentagon-lift obstruction

**Historical run result: NEW_QUOTIENT_FOUND_NOT_LIFTED; subsequent
mathematical disposition: its target lifts are excluded.** One fresh,
bounded trajectory found the matrix below and stopped immediately. It
passed the necessary conditions implemented at run time and avoided the
literal `D=2K6` predicate. It nevertheless satisfies the more general
structural corollary in
[`CYCLIC5_QUOTIENT_TWELVE_PENTAGONS_EXCLUSION.md`, §1a](CYCLIC5_QUOTIENT_TWELVE_PENTAGONS_EXCLUSION.md#1a-the-subsequent-escape-quotient-also-satisfies-the-broader-condition),
so the same proof excludes every target lift. No voltage assignment,
SAT call, complete 60-vertex graph, or full-domain enumeration was
performed. The original JSON records remain unchanged as run evidence.

## Exact change to the search

The initial state is the saved matrix from
[`cyclic5_full60_quotient_run/best_quotient.json`](../../../computations/dd82/construction/cyclic5_full60_quotient_run/best_quotient.json).
The hard domain remains all symmetric integer matrices with row sum
eight, diagonal entries zero or two, and off-diagonal entries in
`{0,1,2,3}`. A move removes two quotient edge units and reconnects their
four endpoints using one of the two other pairings. A loop contributes
two to its diagonal entry. Upward-energy moves and matrices with
negative defect entries remain allowed.

For `D=M²+M−7I−5J`, the new energy is

```
sum_ab max(0,−D_ab)
  + 8 max(0, 2−number_of_independent_orbits)
  + 2 number_of_odd_cycle_components_in_the_q2_graph
  + 8 [exact_excluded_architecture].
```

The last predicate requires both of the following, without any
reference to the vertex labels:

1. D is precisely the adjacency matrix of two disjoint six-vertex
   cliques: diagonal zero, within-part off-diagonal one, cross-part zero.
2. On each of those parts, M has exactly one diagonal-two vertex,
   isolated within that part; the other five vertices have diagonal
   zero and induce a simple unit-multiplicity five-cycle.

A simple two-regular graph on five vertices is a five-cycle, which is
the implementation's final test. Other matrices with `D=2K6` are
retained. The predicate uses the scope of
[`CYCLIC5_QUOTIENT_TWELVE_PENTAGONS_EXCLUSION.md`](CYCLIC5_QUOTIENT_TWELVE_PENTAGONS_EXCLUSION.md),
not an asserted exclusion of every two-clique defect quotient.

The old matrix was directly checked in both the runner and C++ code:
its former energy is zero, its new structural penalty is eight, and its
initial new energy is eight. The explicit witness is
[`initial_predicate_check.json`](../../../computations/dd82/construction/cyclic5_full60_quotient_escape_run/initial_predicate_check.json).
Thus the initial state could not be returned as a success.

## Actual new matrix and defect

Rows and columns are labeled 0 through 11. The complete machine-readable
matrix, defect, row types, difference components, and support triangles
are in
[`best_quotient.json`](../../../computations/dd82/construction/cyclic5_full60_quotient_escape_run/best_quotient.json).

```
M =
0 1 0 0 1 1 1 0 3 1 0 0
1 0 0 1 0 1 3 1 0 0 0 1
0 0 0 1 1 0 1 0 1 0 3 1
0 1 1 0 3 0 1 1 0 0 0 1
1 0 1 3 0 0 0 1 1 1 0 0
1 1 0 0 0 0 0 3 1 0 1 1
1 3 1 1 0 0 0 0 0 1 1 0
0 1 0 1 1 3 0 0 0 1 1 0
3 0 1 0 1 1 0 0 0 0 1 1
1 0 0 0 1 0 1 1 0 2 1 1
0 0 3 0 0 1 1 1 1 1 0 0
0 1 1 1 0 1 0 0 1 1 0 2

D =
2 0 0 0 0 0 0 1 0 0 1 1
0 2 0 1 0 1 0 0 0 1 0 0
0 0 2 1 0 0 0 0 1 1 0 0
0 1 1 2 0 0 0 0 0 1 0 0
0 0 0 0 2 0 1 0 0 0 1 1
0 1 0 0 0 2 0 0 1 1 0 0
0 0 0 0 1 0 2 1 0 0 0 1
1 0 0 0 0 0 1 2 0 0 0 1
0 0 1 0 0 1 0 0 2 1 0 0
0 1 1 1 0 1 0 0 1 0 0 0
1 0 0 0 1 0 0 0 0 0 2 1
1 0 0 0 1 0 1 1 0 0 1 0
```

Every row of M sums to eight; every row of D sums to five and D is
entrywise nonnegative. The ten independent orbits are
`{0,1,2,3,4,5,6,7,8,10}`. Each has external multiplicities
`(3,1,1,1,1,1)`. Orbits 9 and 11 have internal degree two and six unit
interfaces each. The five triple interfaces are
`(0,8),(1,6),(2,10),(3,4),(5,7)`; there are no double interfaces.
Consequently the double-interface odd-cycle obstruction is absent.

Ten diagonal entries of D are two, so D is not `2K6` and the exact new
predicate is false. The entrywise L1 change from the initial M is 112.
The quotient support has 25 triangles, with multiplicity-weighted count
45; these are quotient statistics, not counts of triangles in a lift.

## One actual execution

The fresh random seed was `2026101303`, with no saved annealer state,
restart, or second starting point. Temperature decreases exponentially
from 3.5 toward 0.25 over the authorized budget. The single process was
pinned to CPU 1; its total budget was 60 CPU seconds including compilation
and runner work, and 120 wall seconds.

| Quantity | Actual value |
|---|---:|
| Proposals | 32,073,527 |
| Accepted moves | 2,644,040 |
| Accepted upward-energy moves | 944,706 |
| Accepted states with some negative D entry | 2,644,008 |
| Compile CPU seconds | 1.024405 |
| Search-process CPU seconds | 30.407936 |
| Search-process wall seconds | 30.964698840 |
| Total CPU seconds | 31.449651254 |
| Total wall seconds | 32.014537714 |

The negative-D count is computed by testing actual entries of the trial
defect, rather than inferring negativity from the combined energy.
The successive record energies were `8,4,2,0`, at proposals
`0,15579588,21364941,32073527`. Success required zero combined energy;
the runner then recomputed all M/D entries, the exact exclusion
predicate, and the remaining conditions from the saved matrix.

The actual resource record is
[`resources.json`](../../../computations/dd82/construction/cyclic5_full60_quotient_escape_run/resources.json),
and the complete trace, initial/best/final matrices and counts are in
[`search.json`](../../../computations/dd82/construction/cyclic5_full60_quotient_escape_run/search.json).
The original experiment's files were not overwritten.

Source:
[`cyclic5_full60_quotient_escape_search.cpp`](../../../computations/dd82/construction/cyclic5_full60_quotient_escape_search.cpp)
and
[`cyclic5_full60_quotient_escape_run.py`](../../../computations/dd82/construction/cyclic5_full60_quotient_escape_run.py).
The run established only passage through its implemented necessary
conditions. The subsequent structural check uses
`U={0,4,6,7,10,11}` and `V={1,2,3,5,8,9}`: `D[U,V]=0`, while each
induced M block is a unit C5 plus an isolated diagonal-two label.
Thus the broader corollary excludes this matrix even though its D is
not two K6 components. The existing direct-check artifact is
[`best_quotient.pentagon_obstruction.json`](../../../computations/dd82/construction/cyclic5_full60_quotient_escape_run/best_quotient.pentagon_obstruction.json).

The original proof has a completed fresh same-family checker report
and Gemini round 3 acceptance. The broader corollary and this second
instance were subsequently checked by root and the author; their same-thread round 4 review is now SUCCESS and accepts the addition
(reviews/dd82/20261013_V3_c5_generalized_obstruction_review.json). The earlier
receipts are not represented as covering that addition. No voltage computation is planned
for this excluded matrix. Neither this experiment nor its subsequent
exclusion settles the full free-C5 family.
