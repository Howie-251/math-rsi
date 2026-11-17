# Isolated joint-extension/H49 work, 2026-10-27

Main mathematical record:
[D7_JOINT_EXTENSIONS_AND_H49_COMMON_CORE_20261027.md](../../.trellis/tasks/10-19-nr7-structure-capacity/research/D7_JOINT_EXTENSIONS_AND_H49_COMMON_CORE_20261027.md).

- [Frozen single-root specification](SINGLE_OUTER_ROOT_SPEC.md).
- [One Linux execution report](single_root26/EXECUTION_REPORT.md).
- [Raw result](single_root26/result.json), [full coloring](single_root26/sat_colors.json), [color audit and all actual R6](single_root26/sat_semantic_result.json).
- [Y25 colors](single_root26/Y25_colors.json) and [full recomputed state profile](single_root26/Y25_full_profile.json).
- [Complete R30 mathematical model, NOT RUN](FULL_R30_MODEL_NOT_RUN.md).

One complete SAT counterexample refutes the single-outer-root candidate:
zero-based a=5 simultaneously ends (0,1,2,3,4,5) and starts
(5,6,9,10,11,17); deletion Y25 is safe, e=m=2.
All265 R6 contain a, so this is tau1, not a critical tau5 example.

No complete E5/E6 or H–R target exclusion. No new global numerical bound.
New main-session proofs and nativeSol/high execution remain unreviewed and
unaccepted. No Claude review, no new balanced49 replay/compile, no additional
SAT order, no restart of old runs, and no acceptance/task-pointer changes.
