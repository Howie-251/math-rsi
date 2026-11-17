# 866 eleven/twelve-hole probe: the universal cycle rows add no constraints

2026-11-17. Scope: the 70 Ferrers states in a 4 by 4 box for an actual ordered
rank-3 signotope avoiding blue six, red six and weak eight. This is the bounded
local obligation in
`../../.trellis/tasks/10-19-nr7-structure-capacity/research/NMRS_STRUCTURAL_ROADMAP_20261117.md`
Section 7. No eleven- or twelve-hole lower bound was obtained.

All scientific execution was on the authoritative Linux server `ubun`, under
`/data/ktqiu_hdd/math_agent/reports/n866-joint-holes-20261117`, using
`/opt/anaconda3/envs/forktqiu/bin/python3.10` and SciPy 1.15.3. The initial
sandboxed SSH attempt returned Permission denied; the explicitly escalated
attempt used the same recorded connection fields, existing askpass credentials,
and strict existing host-key file and succeeded. No endpoint mapping or trust was
changed. Receipts are under `receipts/`; no credential values are stored here.

## Actual input and valid necessary rows

States are the four-element subsets W of [8], in lexicographic order, represented
by descending column heights `(w4-4,w3-3,w2-2,w1-1)`. For every directed pair of
ideals, the generator uses the exact destination-minus-source cells. It tests
each ordered triple in all six chronological orders, using precisely the
coordinate-extremum predicate of
`../n79-overlap-20261116/seven-cycle-lp/generate_757.py` with the universe changed
to four columns of height four. The six-order rule connects to actual owners
through `../n79-overlap-20261116/EIGHT-CYCLE-TRANSFER.md` Sections 2--3. Every
exported cyclic support K therefore has at most seven occupied states and gives
the necessary hole inequality `sum(h[v] for v in K) >= |K|-7`.

DFS anchors each support at its minimum state id, tests each appended point with
every pair of preceding points, and retains all successors even when a support
was already seen. Every cyclic ordering can be rotated to such an anchor. The
remaining-candidate count is the sole cardinality prune. Actual completion
without a budget hit therefore enumerates all supports accepted by this exact
universal six-order predicate. This is not enumeration of arbitrary weak-convex
supports or actual signotopes.

The native trace generator is adapted from
`../n79-overlap-20261116/direct-cycle-lp/direct_lp.py`. For descending triples q
in [1,4], let p_i be q_i or q_i+1, subject to p being descending and
`p_i <= (4,q1,q2)_i`. Set S=(p1-1,p2-1,p3-1,0), E=(4,q1,q2,q3).
The column-fill chain `E[:i]+S[i:]`, i=0,...,4, and horizontal-fill chain
`max(S_j,min(E_j,h))`, h=0,...,4, each have five states and share just S,E.
Their consecutive differences have respectively nonincreasing y and x ranges,
forcing the two opposite colors. Inclusion forces actual chronological order.
If their eight distinct states were all occupied, these are same-end opposite
five-point paths, hence weak eight. Each union thus needs one hole.

Finally, the 20 ordinary rows use an interior triple K in {2,...,7}: states W
with K contained in W, or W contained in K union {1,8}. Each has eight states and
needs one hole. No new short-cap numerical import was silently added. The
existing Baek 2 by 6 blocks used for the 154-state residual have no supplied
compression into this 4 by 4 domain; those numerical rows are not transferred
without such a map. No real-D-only early/late gate or inherited 757 block was
copied into ordinary 866.

## Executed bounded result

The single-thread run had DFS limits 90 seconds / 50000 supports, LP 90 seconds,
MILP 45 seconds for each total-hole budget <=10 and <=11, and external timeout
360 seconds. It exited zero without hitting a budget. Actual DFS time was
0.023781 seconds, 13208 nodes, 656880 raw six-order predicate items.

| Exported family | Rows | Support sizes | Hole demand |
| --- | ---: | --- | --- |
| All certified universal cycles | 63 | eight only | one |
| Native traces | 63 | eight | one |
| Ordinary same-end rows | 20 | eight | one |

There are 146 listed rows but only **63 different supports**. Exact Linux
comparison in `row-diagnostic.json` establishes that the entire cycle family
equals the native trace family, and the 20 ordinary supports are contained in it.
There is no longer universal cycle in this universe under this predicate.

The bounded LP optimum was 5. Its exported exact nonnegative row dual has
denominator 2, adjusted right-hand side 10 and zero asserted improvement above
10 or 11. The two MILPs both found this same seven-hole vector:

```
1248 1368 1478 2357 2456 2567 3457
```

Every listed row meets it: 76 listed rows contain exactly one of these holes,
58 contain two, and 12 contain three. Thus the existing necessary total-hole
constraint >=7 can also be imposed without eliminating this vector. These
universal cycle/native trace rows cannot prove even an eight-hole lower bound,
and in particular cannot prove eleven or twelve holes. Repeating or enlarging
this same cycle enumeration cannot improve this conclusion, since it completed.

This seven-hole vector is an exact obstruction to the proposed **row method**.
It is not a 63-point coloring, actual-owner realization, signotope, geometric
construction, or counterexample to an eleven/twelve-hole theorem. No MILP
infeasibility occurred, and no unchecked UNSAT result is used as proof.

## Exact replay and evidence binding

`check_866.py` is a separate standard-library implementation: it constructs cell
sets, recomputes every actual six-permutation condition by permutation parity,
reconstructs every trace, checks its actual difference ranges and eight states,
checks ordinary supports, and recomputes every integer dual load and both hole
vectors. The Linux result `first-exact-check.json` is PASS, exit zero, with 6930
nonvacuous chronological checks, 63 cyclic supports and 146 rows. This is
independent implementation replay, not independent external mathematical review
or an acceptance upgrade of the packet bridge.

Frozen generator SHA256:
`20824ddbb9e41cc891e0dff1c5a3f785fc417a3dc44f2b298e1ca1c1c3f314aa`.

Frozen replay script SHA256:
`919d5b4c81785970b88eaeecd1781971fba120a68c6fea033bf47d39e6de82f3`.

The returned raw archive `first-evidence.tgz` has identical Linux and local
SHA256 `5a8bc219322b9a226ae7420e0c0c9e677fbc2e242b16e7ae522cd3c8cd1f2c19`.
It includes the complete `first/` input/output directory, outer log and exit,
and exact-check stdout/stderr/exit. `row-diagnostic.json` and its exit are
additional separately fetched raw outputs; execution/transport commands and
stdout are preserved in their individual receipts. Source scripts are alongside
this report. Windows performed only transport, file edits, file hashes and
archive unpacking; no research computation ran there.

Reproduction in a fresh Linux output directory:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 360 \
 /opt/anaconda3/envs/forktqiu/bin/python3.10 -u generate_866.py \
 --out replay --seconds 90 --max-rows 50000 --milp-seconds 45
/opt/anaconda3/envs/forktqiu/bin/python3.10 check_866.py replay
/opt/anaconda3/envs/forktqiu/bin/python3.10 diagnose_rows.py replay
```

The current eleven/twelve-hole obligation remains open. A useful next step must
exploit common actual owner order/pair labels or another proved conditional row
family that cuts this explicit seven-hole vector; a further universal-cycle run
in this same domain has no remaining coverage to add. No further job is running,
no production builder/CNF/proof was touched, and no historical certificate was
modified.
