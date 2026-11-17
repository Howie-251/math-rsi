# Fixed seven-hole mask: single shared-pair conditional cycles do not cut a label

2026-11-17. This is one bounded follow-up to `../REPORT.md`, confined to the
explicit seven-hole vector

```
1248 1368 1478 2357 2456 2567 3457
```

Its other 63 states are treated as occupied. The probe did not reject this mask
or establish an actual coloring. It did not test all seven-, ten-, or eleven-hole
vectors. All scientific computation ran on Linux `ubun` in
`/data/ktqiu_hdd/math_agent/reports/n866-joint-holes-20261117/common-pair`, using
`/opt/anaconda3/envs/forktqiu/bin/python3.10`. The preceding evidence is unchanged.

## Exact conditional rule and searched scope

For each occupied strict-inclusion pair A contained in B whose cell difference
has size two or three, inclusion fixes the actual owner order A before B. The
actual pair has one shared label c in B minus A. A branch fixes that single c
throughout the six-order rule: whenever a chronological directed difference is
(A,B), its domain is the singleton {c}; all other directed differences retain
their complete original cell sets.

For an ordered cyclic triple, test all six chronological permutations. If one of
its three forward differences is empty, that chronology is unavailable. Otherwise
the same coordinate-extremum inequality as the original universal-cycle test
must force the sign prescribed by permutation parity. Only triples containing
both A and B can change, and only those are recomputed in each branch. This
reuses the packet-to-weak-eight bridge from
`../../n79-overlap-20261116/EIGHT-CYCLE-TRANSFER.md` Sections 2--3, with the same
fixed conditional label across every affected triple.

DFS anchors at A, allows B anywhere in the remaining cyclic order, and requires
both A and B in the eventual eight-state cycle. Every candidate is tested with
every preceding pair. Rotation to A covers every relevant cycle; pruning a
prefix after B becomes unavailable cannot lose a cycle containing B. Stopping
at length eight is sufficient because every longer conditional positive cyclic
family containing A,B has such an eight-state subset. Cycles missing A or B are
unchanged universal cycles and were already absent on this mask in the first
completed probe.

If a cycle had been found, its eight occupied states, pair, and fixed cell would
have formed a small rejection certificate for that label. Exhausting every cell
of one pair with such certificates would reject this fixed mask. The probe
does not enforce simultaneous labels for all pairs, packet conditions on all
four-point chains, or all possible monochromatic paths. Its negative result is
about this conditional-cycle test only.

## Actual result and limits

Single-thread limits were 180 seconds overall DFS time, two seconds per branch,
and an external timeout of 220 seconds. The job completed in 1.401634 seconds
and exited zero; no branch timed out.

| Item | Actual completed count |
| --- | ---: |
| Inclusion pairs with two-cell difference | 169 |
| Inclusion pairs with three-cell difference | 193 |
| All eligible pairs | 362 |
| Pair/cell branches | 917 |
| DFS nodes over all branches | 237781 |
| Complete branches with no eight-cycle containing the pair | 917 |
| Conditional cycle certificates | 0 |
| Labels cut | 0 |
| Pairs with every cell rejected | 0 |

Thus this specified single-pair strengthening supplies no separating row for the
explicit mask, even after every size-two/three inclusion domain was examined.
This is not evidence that its 63 occupied states admit common actual labels or
a signotope. The eleven/twelve-hole target remains open.

## Returned raw evidence and check scope

`first/result.json` binds the exact input files by SHA256;
`first/branches.json` contains all 917 branch records with pair, cell, nodes,
time and completion flag; `first/pairs.json` lists all pair domains and counts;
`first/certificates.json` is the empty list. `first.log` and `first.exit` retain
the actual outer output and exit code.

The separate standard-library `check.py` recomputes the full eligible pair/cell
domain from the original cell sets, checks hashes, verifies complete coverage
and branch-record consistency, and has an independent six-permutation replay
for any exported positive certificates. `exact-check.json` is PASS, exit zero,
with all 917 expected branches present. Since no certificate was found, its
positive-certificate six-order count is **zero**. The no-cycle exhaustion is
the generator's complete execution evidence, not an independently re-run DFS or
a proof of mask feasibility. No external mathematical review was launched.

Frozen source hashes:

```
e54717354851fa2cc87df1fd01d0bc9cb71139898c5804d3aa320244b0369759  probe.py
b3407c236e2bcfa30913b2bc258779df52738d6da14ec14507fb59b03856d517  check.py
```

The raw returned `evidence.tgz` has matching Linux/local SHA256
`984beb4c58bf9fbb558ca412187d498026827ed72f03911b26031d61055934d3`.
It contains the full `first/` directory, log/exit and exact-check stdout/stderr/
exit. Transport and launch receipts are preserved as `../receipts/common-*.json`;
the launch subshell pid was 3106010. All jobs finished. Windows performed only
control-plane edits, transfers, archive unpacking and file hashes.

Reproduction, on Linux with a fresh output name:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 220 \
 /opt/anaconda3/envs/forktqiu/bin/python3.10 -u probe.py \
 --source ../first --out replay --seconds 180 --branch-seconds 2
/opt/anaconda3/envs/forktqiu/bin/python3.10 check.py ../first replay
```

The caller can use this completed negative probe to choose a stronger common
constraint, such as simultaneous labels or chain packet/path compatibility.
Repeating the same size-two/three single-pair conditional-cycle search on this
same mask has no remaining branch coverage to add.
