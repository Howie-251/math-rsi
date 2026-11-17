# Shared-pivot rows: exact matrix minimum eight holes

2026-11-17. The 63 universal cycle supports plus 30 new shared-pivot rows have
**no hole vector of size at most seven**, certified by an actual successful
external proof checker. An explicit eight-hole vector satisfies every row, so
the strengthened matrix has exact minimum eight. It cannot force the original
eleven/twelve-hole targets.

All scientific code ran on Linux `ubun` under
`/data/ktqiu_hdd/math_agent/reports/n866-joint-holes-20261117/pivot-rows`, with
`/opt/anaconda3/envs/forktqiu/bin/python3.10`. The finite calculation and its
checked CNF are local evidence. The mathematical conclusion for ordinary 866
still uses the actual-input state/label interface and the shared-pivot row
argument below; no geometric realization or independent external mathematical
acceptance is claimed.

## New rows and their exact replay

For each of the 15 four-subsets Omega of I={2,...,7}, order its elements
v1>v2>v3>v4 and let C_i=Omega minus {v_i}. Include all eight private states
`{1} union C_i` and `{8} union C_i`. Add all ordinary four-subsets W of I
containing C_1 or C_4. The latter union has five states because the two
three-state ordinary-red interiors intersect at Omega. Thus each support has
13 states and needs one hole, by
`../../n79-overlap-20261116/EIGHT-TWOPRIVATE.md` Section 2.

Take the 15 true transposes as well, using
`W*={9-v : v in [8] minus W}`. The exact replay verifies on all 70 cell sets
that this operation is genuine grid transpose and an involution.

`check.py` reconstructs every shared-pivot proof rather than merely trusting a
support list. For each original Omega, it reconstructs both ordinary red-five
paths and all private states, takes the complete actual cell domain of
S_4 to T_1, and tests **each** possible pivot cell. A cell in the fourth column
forces the private blue five S_1,S_2,S_3,S_4,T_1; a cell in the first column
forces S_4,T_1,T_2,T_3,T_4. For each case, it verifies the nonempty actual
directed cell differences and the nonincreasing height ranges, and matches
the resulting blue five to the appropriate opposite-color ordinary red five
with identical external owners and disjoint interiors. Both paths are wholly
inside the exported support. It transports all supports by the verified true
transpose. All **30 rows and 84 pivot-cell branches** passed.

The prior 63 complete universal cycle supports are unchanged. The optimization
input has 94 listed inequalities: those 63, the 30 new rows, and the existing
total-hole lower bound seven. The proof run below deliberately omits the
imported total-hole row and instead proves impossibility directly for the
93 cycle/pivot rows under an at-most-seven budget.

## Checked exclusion and explicit eight-hole witness

The strengthened matrix has the following exact feasible hole vector:

```
1248 1258 1278 1358 1368 2347 3567 4567
```

`first/cover.json` retains its state ids and subsets. Every row was replayed
with integer set intersections; it has five blue-internal and three
red-internal holes, no private holes. It is a matrix vector, not an actual
62-point signotope construction.

The controlled MILP initially reported objective eight in 0.629730 seconds.
That floating optimization result was not used as a rigorous infeasibility
proof. `certify7.py` separately encoded the 93 one-hole rows and the budget
`sum(h_1,...,h_70)<=7` as an exact small SAT problem. The 532 auxiliary
threshold variables s(i,j), j<=8, obey

```
h_i -> s(i,1)
s(i-1,j) -> s(i,j)
h_i AND s(i-1,j-1) -> s(i,j)
NOT s(70,8).
```

Induction on i makes s(i,j) true whenever the actual prefix has at least j
holes; conversely, assigning each s its actual prefix threshold extends every
at-most-seven vector. Thus this is an exact existential encoding of the
required upper budget. It does not assume seven-hole color classifications or
the conditional blue/red degree lower bounds.

The resulting CNF has **602 variables and 1150 clauses**, SHA256
`503258563d5048f04895964a99648faefb30ab6cefb16195dd37690a9bf216dd`.
The project-default external solver
`/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat` returned UNSAT,
exit 20, in 0.365273 seconds. The existing external
`/data/ktqiu_hdd/math_agent/cadical-sc2025/build/drat-trim` returned exit zero
and **s VERIFIED** in 0.365548 seconds. The proof is
`budget7/proof.drat`, 394540 bytes, SHA256
`68297255e036d1561743a9f037bd3f2a4d7e48546963cbb0e38f531fcc5954bb`.

`check_bound.py` independently compared every row and threshold-counter clause,
checked the exact formula/proof hashes and successful checker log, and verified
the eight-hole witness against all 94 rows. `bound7-audit.json` is PASS, exit
zero. Consequently the matrix minimum eight is exact. Via the stated valid
actual-input rows, this supplies an eight-hole / ordinary-866-at-most-62
candidate improvement for the parent caller. It neither reaches eleven/twelve
holes nor changes the existing assurance status of the mathematical bridges.

## Regression, execution history and complete evidence

The original seven-hole vector
`1248 1368 1478 2357 2456 2567 3457` violates nine new rows. In particular it
is cut by the transpose of Omega={4,5,6,7}, the natural reflection of the
specified Omega={2,3,4,5} regression. `first/old-mask-regression.json` retains
every violated support.

The initial checker invocation had a syntax typo in the transpose expression.
After correcting it, a regression assertion initially tested only Omega2345
and failed; the caller had explicitly allowed its natural reflection, and the
final assertion tests both. The final replay is `exact-check-final.json` PASS,
exit zero. All initial failed outputs and the successful final output are
preserved separately; the row generator, optimization output and bound proof
were not rewritten to hide those failures.

`evidence.tgz` has matching Linux/local SHA256
`86366b1efafac197bfa9b05f4ea68dd69767429b0ff501b5b34ab5f81a6c4c11`.
It returns the full 94-row matrix, witness, regression, every checker outcome,
the budget-seven CNF, proof, metadata, solver/checker logs, complete bound
audit, exits and source hashes. Individual actual execution and transfer
receipts are in the parent `receipts/pivot-*.json`. Scientific computation did
not run on Windows. All jobs finished; no production code, sealed certificate,
prior evidence or parent `SHARED_PIVOT.md` was modified.

Linux reproduction:

```bash
/opt/anaconda3/envs/forktqiu/bin/python3.10 check.py
/opt/anaconda3/envs/forktqiu/bin/python3.10 check_bound.py
/data/ktqiu_hdd/math_agent/cadical-sc2025/build/drat-trim \
 budget7/formula.cnf budget7/proof.drat
```

The explicit eight-hole vector is now the relevant obstruction for this matrix.
Further improvement needs a new valid constraint that cuts it; repeating these
same 93 rows cannot obtain eleven or twelve holes.
