# One shared order and 28 simultaneous Hall matchings

The full shared-order relaxation is SAT, and so is each exact c=0,1,2,3,4
branch after adding the caller's two boundary pure-source inequalities.
The previous occupancy-only SAT witness is excluded by this stronger layer:
fixing that old occupancy gives UNSAT with a successful, hash-bound DRAT check.
Thus this run removes an actual previous relaxation witness but excludes no
whole c branch. None of the SAT outputs is a signotope or an actual red-path
realization. No external review was requested or performed; acceptance is false.

## Simultaneous formula

The inherited 56-state occupancy CNF remains unchanged and is included whole.
There is one tournament comparison variable for each pair of the 56 states.
For each triple, the two directed triangles are forbidden, yielding a single
strict total order. Ideal inclusion is imposed in its actual direction.
Unoccupied states extend the same order without creating physical points.

The physical first two states are 123,124 and the last two 578,678. The third
occupied state must be 125 or 134, and the third-last must be 478 or 568.
Both choices are made within this same total order, with occupancy conditions.

All 28 coordinate pairs k<l have matching variables simultaneously. Each
occupied vertex of B_k\B_l and B_l\B_k has exactly one incident selected
edge; edges imply both endpoints are occupied. Common occupied states in
B_k intersect B_l are fixed to themselves outside these nontrivial edges.
An edge u->v also requires u<v in the one physical order,
r=k-rank(k,W(u)) < s=l-rank(l,W(v)), and at least one cell of D(v)\D(u)
whose red coordinate j satisfies r+1<=j<=s. Every matching therefore covers
all 15 occupied members on each side, including the fixed common points.

The free formula has 20708 variables and 111948
clauses, including 55440 total-order clauses and 5740 candidate matching
edges across the 28 pairs. No fixed-order template or coordinate-pair subset
replaces the whole formula. The source conditions are the caller's interpretation
of the frozen `../import-joint.md` sections 6 and 7.1.

For each c branch, the formula additionally fixes the number of occupied
states containing both 1 and 8 to c. It requires at least 5-c occupied states
in {123,124,125,126,127}, and at least 5-c in its reversal
{678,578,478,378,278}. These two inequalities were supplied as proved by
the caller in the continuation request; this program implements and checks
them but does not provide an independent mathematical proof of that import.

## Actual Linux results

| Formula | Outcome | Solver seconds |
|---|---|---:|
| free_occupancy | SAT, audited | 0.315 |
| old_occupancy | UNSAT, DRAT verified | 0.065 |
| c0_with_pure_source_bounds | SAT, audited | 0.265 |
| c1_with_pure_source_bounds | SAT, audited | 0.316 |
| c2_with_pure_source_bounds | SAT, audited | 0.566 |
| c3_with_pure_source_bounds | SAT, audited | 0.516 |
| c4_with_pure_source_bounds | SAT, audited | 0.516 |

All runs used the production external AE Kissat at the mandated Linux path,
with a 600-second controlled process-group limit; no limit was reached.
The fixed-old-occupancy proof was checked by the retained external drat-trim,
which returned zero and `s VERIFIED`. Exact CNF and DRAT hashes are in
`old_occupancy/result.json`; proof and checker log are retained.

The free SAT model has c=3 and occupied physical order:

`123 124 134 234 125 135 235 126 136 145 146 147 157 128 345 237 246 238 247 356 158 456 347 167 267 367 457 258 168 268 348 358 567 468 278 568 378 478 578 678`

Every SAT profile contains `model-audit.json`, which supplies the full
56-state order, the occupied 40-state order, all 28 complete matchings,
the fixed common vertices and each edge's admissible cell-label domain.
The audit checks every CNF clause and independently reconstructs total-order
ranks, ideal containment, first/last/third roles, coordinate degrees, complete
matching coverage, strict r<s, actual time direction, and cell differences.
Each c branch also separately checks c and the two boundary counts.

## Exact boundary and reproduction

Actual pair labels shared between different matching uses, internal red-six
path witnesses, full packet/signotope constraints, and the blue-endpoint
alternating Hamilton graph are not encoded. The graph-theoretic Hamilton
orientation has not been confused with physical point order. A separate
`shared-pair-label-diagnostic.json` reports intersections of label domains
for repeatedly selected physical pairs; it is a diagnostic, not an additional
formula constraint or an original-object witness.

`ledger.json` records every variable and all clause groups. Source and formula
hashes bind each result; `MANIFEST.json` binds the full handoff. The initial
launcher syntax error is preserved in `launch-syntax-error.log`; no solver
ran on that failed launch. All reported results come from the corrected source.

Reproduce on Linux in a fresh sibling copy of this directory, preserving the
inherited parent CNF and old model: run
`/opt/anaconda3/envs/forktqiu3/bin/python3.12 -B build_run.py`, then
`/opt/anaconda3/envs/forktqiu3/bin/python3.12 -B run_branches.py`.
The first executes the free and old-fixed formulas, and the second executes
all five c branches. Preserve completed evidence rather than overwriting it.
Windows was used only to edit source and transport files over SSH/SFTP.
