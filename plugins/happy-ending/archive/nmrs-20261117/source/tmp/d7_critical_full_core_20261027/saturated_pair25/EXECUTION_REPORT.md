# Single full25 saturated-pair gate: execution evidence

`result.json` records `SAT_FORMULA_AND_SEMANTIC_CHECKED`. Exactly one default
AE invocation completed with exit 10 in 5.686718667973764 seconds. Limits were
59 CPU seconds, a 59-second wall watchdog and 3 GiB address space. There was
no retry, fallback, proof check, independent review or acceptance update.

## Complete quantifiers and formula

The unchanged D7 builder was configured privately at N25. Every actual R6
reach flag was prohibited. Positive existence is encoded using all 53,130
five-subsets with exact all-ten-red-triple H5 definitions, all 25 exact
later-pair color-conjunction roots, all 53,130 exact K=H5&root gates, and all
16 cuts 4..19. Selected cuts imply direct positive left-H5 and right-K5
disjunctions. No A/B position, equality type, e or m was fixed.

Formula: 120,081 variables and 926,637 clauses. The complete assignment
satisfies every clause. The audit independently recollects every H5, K5 and
root flag from triple colors. Original forward flags are used only in domain
prohibitions. The old base's historical static order30 label is disclosed in
the final binding; actual order25 and all 12,650 packets are recorded there.

## Actual witness

All indices here are zero-based:

`A=(1,2,3,6,8)`, `B=(12,15,17,18,20)`.

Every one of the ten triples in A and every one of the ten triples in B is
red, and `max A=8 < min B=12`. Boundary `t=20` is a nonvacuous actual right
root: each of the following six triples is red:

```text
(20,21,22) (20,21,23) (20,21,24)
(20,22,23) (20,22,24) (20,23,24)
```

All actual right roots are `[12,20,21,23,24]` (the final two are vacuous).
The full actual R5 family is retained in `sat_semantic_result.json`.

All 2,300 triple colors and 12,650 packets were checked. There are no bad
packets, blue-five paths, red-six paths, same-endpoint weak-seven witnesses
or forbidden EndR5/SrcB4 intersections. Longest red has five vertices,
longest blue four; maximum same-endpoint color-length sum is eight.

The original one-based terminal-pair state extractor computes `e=m=10`,
injective states and the exact `N=25+e-m` identity. Its complete profile is
retained in `full_profile.json`.

This verified full coloring supplies the requested SAT calibration of SP.
It does not supply a critical tau5 extension and does not change any global
bound or existing acceptance.

## Artifacts and bindings

- `SATURATED_PAIR_GATE_SPEC.md`: main's exact scope and existential reduction.
- `decision.py`, `base_D7_builder.py`, `semantic_check.py`,
  `downset_state_snapshot.py`: bound sources, with existing sources unchanged.
- `binding.json`, `query.cnf`, `variable_ledger.json`: complete formula binding.
- `complete_solver_assignment.json`: all variable truth values.
- `sat_colors.json`, `sat_semantic_result.json`, `full_profile.json`: complete
  actual colors, positive witnesses, boundary triples and state recollection.
- `solver_launch.json`, `solver.stdout`, `solver.stderr`, `execution.json`:
  exact command, limits, process identity and execution envelope.
- `upload_sources.json`, `fetch_result.json`, `fetch_formula_assignment.json`:
  source/result byte identities and transport receipts.

CNF SHA256: `034a133f7456b3cc5f792c68b80813f356d8a40564874f6c2ea762ae4ca81649`.
Source adapter SHA256: `765d9ad3f900a601150290108b4f156413eb869e0c0fb8e88ca56749f3a3e45d`.
Coloring SHA256: `86ac1e372c85073e0fac11daa40bfc57e49bbe91cacd4a2a8d7476e2302f727c`.
Semantic receipt SHA256: `370b8b7a11d95694a35920d617f2a97dfcbc80361e0c5ccfb8a09a6e13ef4b94`.
Result receipt SHA256: `b05fa26a8b61044844b63942ef8f8a3c464fb3a1db72dfbdab86877d7b8d5841`.

No existing file or running job was modified by this gate.
