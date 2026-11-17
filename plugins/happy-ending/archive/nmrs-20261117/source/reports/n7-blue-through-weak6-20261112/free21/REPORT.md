# Actual blue-through set containing weak six: verified counterexample

Date: 2026-11-12. A freely positioned twenty-one-point complete767 coloring gives an **actual weak six entirely inside its actual blue-five-through set**. Literal and independent physical-DP checks passed. No external review occurred, and no additional model was launched after this witness.

Let H denote the points that both receive and emit a real B5 in the same finite coloring. The exact set is

`H={5,10,11,12,14,16,17}`.

The same actual outer endpoints `(10,17)` support:

- Red three: **(10,11,17)**.
- Blue five: **(10,12,14,16,17)**.

Every point of both arms is in H, and all anchors below are physical paths in this one coloring. Thus the proposed universal H-no-weak6 statement is false: H cannot in general be treated as a six-convex-free domain. This does not refute a population bound on H, does not produce a75-point counterexample, and does not assert a geometric realization. The witness targets R3+B5; the audit found no R4+B4 target in this H, so the narrower R4+B4-only question is not disproved here.

## Real anchors and surviving red six

| H point | Incoming B5 | Outgoing B5 |
|---:|---|---|
| 5 | (1,2,3,4,5) | (5,6,7,8,10) |
| 10 | (1,2,3,4,10) | (10,12,14,16,17) |
| 11 | (1,2,3,8,11) | (11,12,14,16,17) |
| 12 | (1,2,4,8,12) | (12,13,19,20,21) |
| 14 | (1,2,4,8,14) | (14,18,19,20,21) |
| 16 | (1,2,5,9,16) | (16,18,19,20,21) |
| 17 | (10,12,14,16,17) | (17,18,19,20,21) |

An actual red six is `(1,2,6,13,18,19)`. The whole coloring has maximum red length6 and blue length5. None of H is an R6 source or terminal, and no actual R5 joins any pair of H points; these necessary ambient properties were independently verified and coexist with the displayed weak six.

## Exact finite model and checks

There is one physical color variable per triple, true meaning red. Complete packets, no R7, no B6 and all actual same-endpoint weak-seven splits are imposed. Exact B5 path selectors define exact finite B5 source/end flags and their intersection H. The target is the disjunction of a real same-endpoint R3+B5 or R4+B4 entirely in H. H-arm witnesses imply every actual path color and every H membership, and selected endpoint flags must select actual paths. No virtual ambient anchor, fixed role order, disjointness assumption or padded outside point is used. See [SCOPE.md](SCOPE.md).

The independent whole-clause reconstruction passed with zero missing/extra: **57281 variables, 819375 clauses**. CNF SHA-256: `819f4ef987ae9900d7b7a233cf6605f83a4fa6cea20b38b29a4cdddc58375484`.

Kissat exited10 in10.702 seconds, no timeout. The separate verifier exited0 in6.482 seconds. It imports no generator, checks the complete literal assignment, then reconstructs every exact physical path length by DP at all210 outer pairs. All same-endpoint color-length sums are below9. It recomputes all actual H points, both target families within H, their actual arms, and every H point's real B5 anchors. All checks passed. In the JSON files the inherited field name K denotes this same actual H.

## Retained evidence

- [colors.tsv](colors.tsv): every one of the1330 physical triple colors.
- [physical-witness.json](physical-witness.json): exact H, the weak-six arms, all pointwise real anchors, a red-six witness, every endpoint's exact color lengths and corresponding actual paths.
- [independent-verification.json](independent-verification.json), [schema-audit.json](schema-audit.json), [solve.stdout](solve.stdout), [result.json](result.json), [runtime.json](runtime.json): actual checks, commands, timings and bindings.
- [formula.cnf](formula.cnf), [probe.py](probe.py), [verify.py](verify.py): saved literal formula and independently snapshotted builder/auditor.
- [final-bindings.json](final-bindings.json): completed-file hashes; it records the controller stdout after its final line.

All scientific work ran under `/data/ktqiu_hdd/math_agent/reports/n7-blue-through-weak6-20261112/free21` with Linux Python `/opt/anaconda3/envs/forktqiu3/bin/python3.12` and the controlled workspace Kissat. The binary SHA-256 is `c2e44161cd142694f2b612e0be2dcc59cb656df6d42f8713adc4d05b9a22f5fa`. Physical data and CNF are downloaded separately to avoid a large combined transfer. The solver's unused SAT trace `proof.drat` remains on Linux; it supplies no UNSAT certificate credit and is unnecessary for physical witness replay. No local or global UNSAT statement is claimed.

For replay on Linux, in a copy of the evidence run `python3 -B verify.py --schema` and `python3 -B verify.py --sat`; no solver is required. The original builder deliberately refuses in-place reruns. The earlier actual-H witness with H of size5 had an all-blue H and no internal weak six; this fresh result is a distinct, stronger counterexample, not a relabeling of that earlier data.
