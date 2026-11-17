# A real blue five inside the actual blue-through set: verified SAT

Date: 2026-11-12. This fresh, position-free twenty-one-point model is **SAT and independently physically verified**. It gives a genuine complete 767 coloring whose actual B5-through set is exactly `{11,13,14,15,16}`, and those five points themselves form a B5. Every required incoming/outgoing B5 anchor lies in the same finite coloring. There is also an actual R6.

This disproves universal absence of an internal B5 in the actual blue-through set. It does **not** disprove a population bound of twenty on that set, since this witness has only five through points. It is not a seventy-five-point counterexample and provides no geometric coordinates. No external review occurred.

## Actual paths

The central blue path is `(11,13,14,15,16)`. Its five actual through points have these physical blue-five anchors:

| Point | Incoming B5 | Outgoing B5 |
|---:|---|---|
| 11 | (1,2,5,6,11) | (11,13,14,15,16) |
| 13 | (8,9,10,12,13) | (13,17,19,20,21) |
| 14 | (8,9,10,12,14) | (14,17,19,20,21) |
| 15 | (8,9,10,12,15) | (15,17,19,20,21) |
| 16 | (1,3,9,13,16) | (16,17,19,20,21) |

A red-six witness is `(1,2,4,7,17,19)`. Maximum red length is six and maximum blue length five. Every actual pair of through points has no ambient R5 between it, and none of the five points is an R6 source or terminal; these stronger predicates were independently re-extracted and passed.

## Exact formula and independent check

There is one physical color variable per triple, true meaning red: 1330 colors. The formula has 42721 variables and 699857 distinct clauses. It asserts all rank-three packets, no R7, no B6, and the same-actual-endpoint weak-seven splits R6+B3, R5+B4, R4+B5. Each candidate B5 has a selector equivalent to its actual consecutive triple colors. B5 source and terminal flags are exact disjunctions of those selectors; K is exactly their intersection. A witness selector requires one real B5 whose five vertices all lie in this exact K. See [SCOPE.md](SCOPE.md).

The necessary no-R5-between-K and K-no-R6-endpoint clauses follow from real opposite-color anchors and are included as pruning. There are no virtual ambient flags or fixed arm placements. Any physical coloring with the target property has its canonical exact auxiliary assignment, so these clauses do not replace the target with a stronger guessed order pattern.

The independent checker imports no builder. It reconstructed the entire normalized CNF, with missing=extra=0. It then checked the complete SAT literal assignment and recomputed all exact monochromatic path lengths by physical DP on `(first,penultimate,last)`. All 210 outer pairs, all their red/blue exact-length sums, all packets, the actual B5 endpoint sets and the exact K intersection were checked. The central B5 and each displayed anchor were recovered from physical colors. All checks passed.

Kissat exited 10 in 12.397 seconds; the independent audit wrapper exited 0 in 5.078 seconds. Both processes were controlled external Linux processes, with no timeout. No UNSAT or DRAT exclusion credit is claimed for this SAT result.

## Retained evidence and reproduction

- [colors.tsv](colors.tsv): all 1330 physical triple colors.
- [physical-witness.json](physical-witness.json): exact K, all central B5 witnesses, both real anchors at every K point, an actual R6, and every endpoint/color-length witness.
- [independent-verification.json](independent-verification.json), [schema-audit.json](schema-audit.json), [result.json](result.json), [runtime.json](runtime.json), [solve.stdout](solve.stdout): actual checks, commands, exit codes and hashes.
- [formula.cnf](formula.cnf): 16092680 bytes, SHA-256 `05d5dcf562dffccc07b84d5ff5901249fd3806f0f010cedfa0da8c296e8b9e68`.
- [probe.py](probe.py), [verify.py](verify.py): independent builder and verifier snapshots.
- [final-bindings.json](final-bindings.json): completed-file bindings. As in earlier probes, the final manifest replaces the early controller-stdout snapshot after its final line.

All scientific work occurred under `/data/ktqiu_hdd/math_agent/reports/n7-blue-through-local-20261112/full-k21`, with Python `/opt/anaconda3/envs/forktqiu3/bin/python3.12`, workspace Kissat SHA-256 `c2e44161cd142694f2b612e0be2dcc59cb656df6d42f8713adc4d05b9a22f5fa`, and the existing pinned SSH chain. Large combined transfer hit the sixty-second transport limit; physical evidence and compressed CNF were successfully retrieved separately. All essential SAT evidence is unpacked locally. The unused 12430382-byte SAT trace `proof.drat` remains on Linux, hash `3c9b0ad7c5978cb1ba5ccf21007b751627e97384aa069b8979de6fd28b5ca1de`; it is not an UNSAT certificate and is not required to audit this coloring.

To audit the retained model on Linux without solving again, run `python3 -B verify.py --schema`, then `python3 -B verify.py --sat` in a copy of this directory. The original builder refuses an in-place rerun. The exact mathematical scope and the finite anchor-union limits are recorded in the [research note](../../../.trellis/tasks/10-19-nr7-structure-capacity/research/N7_BLUE_THROUGH_LOCAL_20261112.md). No additional experiment was launched after this SAT witness.
