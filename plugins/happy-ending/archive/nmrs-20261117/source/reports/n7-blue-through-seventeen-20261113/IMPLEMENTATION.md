# Implementation boundary

This directory implements the frozen `SPEC.md` necessary projection only.
The source consists of `probe.py` (builder and a single controlled solve),
`verify.py` (independent schema and physical-color audit), and `transport.ps1`
(create-only Linux transport). All scientific execution is on authoritative
Linux. No existing campaign, production builder, or sealed result is changed.

The gap being tested is feasibility of the 25-point necessary projection for
17 ambient blue-five-through points. The projection includes both fixed blue
anchors, weak-7 avoidance, the K red-five/red-six prohibitions, virtual red-five
extensions, and both complete M0 clauses. Intermediate K vertices receive no
finite blue-five witnesses. Auxiliary flags are one-way closure flags and are
never used for population counts.

Exactly one formula and one Kissat invocation are permitted. Independent
schema reconstruction must pass before that invocation. There are no baseline,
fallback, ablation, retry, or alternate-formula solves. SAT establishes only
feasibility of these necessary conditions. UNSAT credit requires the actual
successful DRAT check against the retained formula and proof.
