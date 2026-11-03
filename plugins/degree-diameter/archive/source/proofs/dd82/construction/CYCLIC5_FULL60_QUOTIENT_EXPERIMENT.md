# Full free-C5 mechanism: an actual quotient subsequently excluded

Run `dd82-v3-c5-full60-20261013`. After the one full-C5 CNF attempt
returned UNKNOWN, the authorized quotient stage found the explicit
matrix below and stopped immediately. It satisfies the quotient and
same-orbit difference conditions implemented at run time. **The later
pure proof excludes every target lift of this matrix:** see
[CYCLIC5_QUOTIENT_TWELVE_PENTAGONS_EXCLUSION.md](CYCLIC5_QUOTIENT_TWELVE_PENTAGONS_EXCLUSION.md).
That original argument has a completed fresh same-family checker report
and Gemini round 3 acceptance, as linked in the proof manuscript; it is
not a Lean or machine-checked proof certificate. No voltage assignment
or complete degree/diameter graph was obtained, and the proposed fixed-M
voltage preparation and solver run were cancelled before implementation.
The original experiment data below remain unchanged.

## Domain and single trajectory

The existing C5 quotient program was a bounded four-orbit replacement
profile around the old seed; it was not a general quotient search.
The new compact sources are
[`cyclic5_full60_quotient_search.cpp`](../../../computations/dd82/construction/cyclic5_full60_quotient_search.cpp)
and [`cyclic5_full60_quotient_run.py`](../../../computations/dd82/construction/cyclic5_full60_quotient_run.py).

A state is a symmetric integer matrix $M$ with row sum eight, diagonal
entries zero or two, and off-diagonal entries between zero and three.
It is represented by 48 multigraph edge units: an internal loop
contributes two to its diagonal entry, and a cross edge contributes one
to both symmetric entries. A proposal removes two units and re-pairs
their four endpoints using either nontrivial pairing. Thus all row
sums are preserved. Only the stated diagonal and cross-multiplicity
caps are hard requirements; no row type or quotient is fixed.

The starting matrix is read from the actual 20-bad-pair seed voltages.
It has twelve internal cycles and quotient $2I+A(K_{6,6})$. This is
explicitly disallowed as a success because at least two independent
orbits are required.

Write $D=M^2+M-7I-5J$ and let $z$ count zero diagonal entries. Let $o$
count odd-cycle connected components in the simple graph whose edges
are the interfaces with $q_{ab}=2$. The integer score is

$$
\sum_{a,b}\max(0,-D_{ab})+8\max(0,2-z)+2o.
$$

The last condition was added before the run began, following the
complete proof in
[CYCLIC5_WITHIN_ORBIT_DIFFERENCE_CONSTRAINTS.md](CYCLIC5_WITHIN_ORBIT_DIFFERENCE_CONSTRAINTS.md).
It is sufficient and necessary for same-orbit coverage to be achievable
on the allowed row types; cross-orbit coverage remains unresolved.

One trajectory uses RNG seed 20261013 and Metropolis acceptance. Its
temperature decreases exponentially from 3.5 toward 0.25 as the single
budget is consumed. States with negative entries of $D$, or failing
the difference condition, remain allowed during the trajectory. There
are no state resets, additional seeds or restarts. A zero score is the
stopping criterion, not evidence of complete enumeration.

## The first successful quotient

With rows and columns numbered 0 through 11, the saved matrix is

```text
0 0 1 2 1 2 1 0 0 0 1 0
0 0 1 1 1 0 2 0 1 0 0 2
1 1 2 0 1 0 0 1 1 0 1 0
2 1 0 0 0 0 1 1 0 0 2 1
1 1 1 0 0 2 0 0 0 1 0 2
2 0 0 0 2 0 1 1 1 1 0 0
1 2 0 1 0 1 0 1 2 0 0 0
0 0 1 1 0 1 1 2 0 1 0 1
0 1 1 0 0 1 2 0 0 2 1 0
0 0 0 0 1 1 0 1 2 0 2 1
1 0 1 2 0 0 0 0 1 2 0 1
0 2 0 1 2 0 0 1 0 1 1 0
```

The exact recomputed defect matrix is

```text
0 1 0 0 1 0 0 1 1 0 1 0
1 0 0 0 1 0 0 1 1 0 1 0
0 0 0 1 0 1 1 0 0 1 0 1
0 0 1 0 0 1 1 0 0 1 0 1
1 1 0 0 0 0 0 1 1 0 1 0
0 0 1 1 0 0 1 0 0 1 0 1
0 0 1 1 0 1 0 0 0 1 0 1
1 1 0 0 1 0 0 0 1 0 1 0
1 1 0 0 1 0 0 1 0 0 1 0
0 0 1 1 0 1 1 0 0 0 0 1
1 1 0 0 1 0 0 1 1 0 0 0
0 0 1 1 0 1 1 0 0 1 0 0
```

Every row of $M$ sums to eight; $D$ is entrywise nonnegative with row
sum five and zero diagonal. Its support is two copies of $K_6$, on
$\{0,1,4,7,8,10\}$ and $\{2,3,5,6,9,11\}$.

Only orbits 2 and 7 have internal degree two. Their external row type
is $1^6$. The other ten orbits are independent and each has external
row type $(2,2,1,1,1,1)$. No row is all even. These row types were
outcomes, not restrictions imposed on the search.

The double-interface support consists of the ten-cycle

$$
0-3-10-9-8-6-1-11-4-5-0
$$

and the isolated vertices 2 and 7. Therefore it has no odd-cycle
component and its double-interface difference labels can alternate.
No numerical shift assignment was performed in this stage.

The quotient support has 25 triangles, and the sum of the products of
the three interface multiplicities over these triangles is 50. These
are **quotient statistics**, not triangle counts in a 60-vertex lift.
The full-matrix entrywise absolute difference from the initial quotient
is 112; its internal-cycle count changed from twelve to two. In
particular the saved success is not the unchanged old all-internal
$K_{6,6}$ quotient.

## Actual execution and evidence

The search stopped at its first zero-score state, after 17,953,317
proposals. It accepted 2,494,848 moves, including 901,009 uphill moves;
2,494,847 accepted states had a negative defect entry. Thus it actually
crossed the old hard-filter barrier. The successive best scores were
16, 4, 2, 0, at proposals 0, 8, 16,737,098 and 17,953,317.

The run was pinned to CPU 1. Compilation used 1.008595 CPU seconds,
the search process used 18.490345 CPU seconds, and the whole batch
including parent work used **19.512925058 CPU seconds and
19.805862270 wall seconds**, below its 60-CPU/120-wall limits. The
single C++ trajectory received the remaining budget after compilation
with a two-second reserve. It stopped on success, not at that limit.

Actual data are in
[`cyclic5_full60_quotient_run/`](../../../computations/dd82/construction/cyclic5_full60_quotient_run/):

- `search.json`: initial, first departed, best and final matrices,
  the best and final defect matrices, improvement trace and counts;
- `best_quotient.json`: the complete verified $M,D$, row types,
  independent orbits, all-even-row check, double-interface components
  and triangle statistics;
- `resources.json`: actual process and batch resource measurements;
- `initial.json`, `last_quotient.json`, `input.txt`, and execution logs.

The Python wrapper recomputes all 144 defect entries directly from the
returned matrix and checks them against the C++ result. It checks the
domain, row sums and zero score before recording success. No SAT call,
voltage search or graph BFS was performed.

At the end of this run the quotient was a proposed input for voltage
completion. The subsequent pure exclusion linked above superseded that
plan, so no voltage stage was implemented or run for this matrix. The
experiment itself proves neither liftability nor impossibility of other
quotients. No search completeness, full free-C5 exclusion, or improvement
in the full 60-vertex bad-pair count is claimed.
