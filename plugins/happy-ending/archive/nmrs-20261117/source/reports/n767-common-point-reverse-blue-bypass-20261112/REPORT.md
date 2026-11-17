# A 13-point common-point obstruction with a forward bypass and reverse blue five

The requested local obstruction exists as a complete ordered rank-3 signotope on
`V={0,...,12}`. Put `P1=0`, `P2=1`, `Q1=12`, `Q2=11`, and `x=3`.
Red is the positive ordered-triple color; path length counts vertices.
The endpoint order is `P1<P2<Q2<Q1`.

| Actual path | Vertices |
|---|---|
| The unique `R6(P1,Q1)` | `(0,3,5,6,10,12)` |
| The unique `R6(P2,Q2)` | `(1,2,3,4,8,11)` |
| The unique R6 anywhere avoiding x; endpoints `(P1,Q2)` | `(0,4,6,9,10,11)` |
| The unique `B5(P2,Q1)`, also avoiding x | `(1,7,9,10,12)` |

All R6 endpoint pairs in the entire 13-point domain are **exactly**
`{(0,11),(0,12),(1,11)}`. Their bipartite endpoint graph has matching number two,
with the two diagonal edges forming its only size-two matching. Deleting the
physical point `x=3` leaves exactly the single displayed forward R6, so the
endpoint matching number drops to one. A surviving forward bypass and an actual
reverse B5 therefore do not restore a size-two matching after this deletion.

The complete list of ten actual R6 paths is:

```text
0 1 3 4 8 11
0 2 3 4 8 11
0 3 5 6 10 11
0 3 5 6 10 12
0 3 5 7 9 11
0 3 5 7 10 11
0 3 5 9 10 11
0 3 6 9 10 11
0 4 6 9 10 11
1 2 3 4 8 11
```

Other marked endpoints may be internal vertices of a path: for example, the
first path uses P2 internally. No restriction excluding such borrowing was
imposed. All ten R6 have their internal vertices in `{1,...,10}`, and each
displayed diagonal has its four internal vertices in `{2,...,10}`. No seven-point
internal-pool restriction is claimed.

## Exact checks and source data

The complete 286-color literal table is [colors.tsv](colors.tsv). The SAT model,
all packets, every actual red/blue path and same-endpoint maxima are in
[case-003/witness.json](case-003/witness.json).

An independent implementation, [verify_colors.py](verify_colors.py), imports no
generator or solver code. It reads only the literal colors, enumerates every
one of the 8192 vertex subsets (8178 have at least two vertices), and independently
rechecks all 715 rank-3 packets, every actual monochromatic path, all 78 endpoint
pairs and every pair of realized red/blue lengths with those endpoints. It found
513 red paths and 205 blue paths (counting each two-point path in both colors),
with longest lengths six and five. There is no R7, no B6 and no weak7
(opposite-color paths with identical outer endpoints and length sum nine).
All claimed local properties and the complete path enumeration agree with the
first implementation. The independent Linux record is
[independent-verification.json](independent-verification.json), with every
same-endpoint length set recorded rather than only maxima.

This is a finite **abstract signotope** witness. No planar coordinates,
geometric realizability, near-capacity population, seven-point pool, 75-point
witness or global N767 bound is established by it. It disproves the corresponding
unqualified local matching-repair assertion on this abstract object domain.
Additional upstream hypotheses would need to be checked separately before using
or excluding this example in a global argument.

## Search and reproducibility

The fresh [probe.py](probe.py) used one physical color variable per ordered
triple, all packet clauses, explicit R7/B6 prohibitions, and all same-endpoint
red/blue path pairs with length sum nine (including overlapping interiors).
Existential selectors assert the three red paths and the reverse blue five;
all diagonal R6 avoiding x are forbidden. The strict branch additionally forbids
every R6 whose endpoint pair is outside the three designated pairs.

The successful case has 708 variables and 105576 clauses. Its actual DIMACS model
satisfies every clause. The exact CNF SHA256 is
`8a2493737103c4ae6863f407496774ee795fc649fcaa48c13d88bce4aebd2421`.
The first three cases, with endpoint order `P1<P2<Q1<Q2` and x=3,6,9, were
UNSAT and each completed drat-trim successfully. These fixed-order exclusions
are auxiliary observations only. Case 3 was SAT, after which the controller
stopped: four of 120 designed cases were run; 116 were not needed or attempted.
No all-order nonexistence claim is made.

All scientific execution ran on authoritative Linux host `ubun`, with
`/opt/anaconda3/envs/forktqiu3/bin/python3.12`. Kissat and drat-trim were controlled
external processes with process-group termination and hard outer time limits.
There were no in-process solver calls, production encoding edits, sealed-job
changes, external mathematical reviews or new Goals.

Linux evidence root:
`/data/ktqiu_hdd/math_agent/reports/n767-common-point-reverse-blue-bypass-20261112`.
The controller completed in about 22 seconds and is no longer running.
[summary.json](summary.json) lists the actual four statuses; per-case results
retain commands, exit codes, original stdout/stderr and certificate bindings.
[final-bindings.json](final-bindings.json) records the source, SAT formula/model
and executable hashes. The complete four-case evidence is preserved in
[evidence.tar.gz](evidence.tar.gz), including CNFs and the three checked DRATs.

On Linux, rerun the independent literal-color check from an extracted copy:

```bash
/opt/anaconda3/envs/forktqiu3/bin/python3.12 -B verify_colors.py
```

The fixed source filenames and `case-003/witness.json` must be present as in this
directory. It writes its independent JSON and the complete TSV color table.
