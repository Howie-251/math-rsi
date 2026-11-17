# Authorized necessary-minor gate: raw execution report

## Scope and pre-execution correction

Main owns the mathematics. Before writing or running the scientific adapter,
the original sixteen-point wording was flagged: P5 + Q4 + six marked points
gives fifteen distinct vertices. Main corrected `../FINITE_GATE_SPEC.md` to
fifteen, with no extra vertex and unchanged requirements. No solver ran before
that correction. The unused `../minor16/` contains preparation notes and a
transport wrapper only, with no generated formula or launch artifact.

Order and zero-based names are:

`0..14 = p1,p2,p3,p4,p5,a,q1,q2,q3,q4,b,c,d,f,g`.

This is one finite calibration, not independent review or acceptance. No
existing source, result, task, run or acceptance file was changed. No retry,
restart, fallback, proof replay or follow-up search occurred.

## Actual result and resources

`result.json` records `status=SAT_FORMULA_AND_SEMANTIC_CHECKED`,
`solver_invocations=1`, `assignment_complete=true`,
`clausewise_checked=19500`, `semantic_valid=true`, `theorem_credit=false`,
`production_accepted=false`, `independent_review=false`.

Authoritative command:

```text
/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat --time=59 /data/ktqiu_hdd/math_agent/tmp/d7_critical_full_core_20261027/minor15/minor15.cnf /data/ktqiu_hdd/math_agent/tmp/d7_critical_full_core_20261027/minor15/minor15.drat
```

Exit 10; timed_out=false; elapsed 0.020225148007739335 seconds. Controlled
external process PID/PGID 354725, CPU limit 59 seconds, wall watchdog 59
seconds, address space 3,221,225,472 bytes, single CPU affinity. The enclosing
Linux adapter command exited 0 in its SSH receipt.

Formula: 2,460 variables, 19,500 clauses; unchanged D7 base has 19,424 clauses,
followed by 76 distinct red triple units for the exact three required R6 sets
and six right-root predicates. There are no positive auxiliary flags, E-count
constraint or tau constraint. The historical base's static schema mentions
order30; the final binding explicitly records actual n15 and 1,365 packets.

## Direct color-only result

All 455 triple colors and 1,365 packets are present. `bad_packets=[]`,
`weak_witnesses=[]`, `forbidden_joint=[]`; longest red has six vertices,
longest blue four; maximum same-endpoint red/blue length sum is eight.
Every required red triple and right-root condition holds. The existing
independent DP checker and exhaustive ordered-subset enumeration agree.
Exhaustive enumeration also checks consecutive-path/all-triple equivalence
for every ordered subset in this packet-valid coloring.

All actual R6 endpoints and all right roots are exactly:

`E = {a,b,c,d,f,g} = {5,10,11,12,13,14}`.

All actual R6 sources are `{p1,a}`. Actual EndR5 is
`{p5,a,q4,b,c,d,f,g}`; actual SrcB4 is `{p1,p2,p3,p4}`. All actual source and
endpoint sets for every nonempty color/length are preserved in
`sat_semantic_result.json`.

The complete family of ten actual R6 subsets is:

1. `(p1,p2,p3,p4,p5,a)`
2. `(a,q1,q2,q3,q4,b)`
3. `(a,q1,q2,q3,q4,c)`
4. `(a,q1,q2,q3,q4,d)`
5. `(a,q1,q2,q3,q4,f)`
6. `(a,q1,q2,q3,q4,g)`
7. `(a,q1,q2,q3,f,g)`
8. `(a,q1,q2,d,f,g)`
9. `(a,q1,c,d,f,g)`
10. `(a,b,c,d,f,g)`

Exact exhaustive transversal enumeration gives `tau=1`; the only minimum
transversal is `{a}`. Thus `alpha6=14`; the only maximum R6-free subset is all
vertices except a. These values are computed from actual R6 colors, not from
forward auxiliary flags or any assumed bound.

## Primary artifacts and fixed identities

- `execution.json`: Linux adapter command, exit and raw stdout/stderr.
- `solver_launch.json`, `solver.stdout`, `solver.stderr`: exact external run.
- `binding.json`, `minor15.cnf`, `variable_ledger.json`,
  `positive_triple_requirements.json`: complete formula and variable binding.
- `complete_solver_assignment.json`: all 2,460 variable truth values.
- `sat_colors.json`: all 455 actual triple colors with ordered names.
- `sat_semantic_result.json`: exhaustive actual paths/endpoints/R6/tau/alpha.
- `fixture_checks.json`: 24 retained deterministic checker controls passed;
  no additional solver invocation.
- `upload_sources.json`, `fetch_result.json`: source transport and fetched
  artifact byte/hash receipts.

SHA256:

| Artifact | SHA256 |
|---|---|
| `minor15.py` | `d4a47ed0d7cde7254339ef70437d333cb45c4c3e9b850b463f86afd8da9b15b6` |
| unchanged `base_D7_builder.py` | `237b780c8eacacec85e8b23c94945bffa7f6058f05582f81649e2385b71510b1` |
| unchanged `semantic_check.py` | `6ddee9b04ee2b77bb5727a5a06f55aaca12774e76c066ebd88d5cce885c1ab70` |
| corrected `FINITE_GATE_SPEC.md` | `9a5fd66b51c0b56a616f462706e3e55272cc2698a2b7cbacb183ab07473626a2` |
| AE executable | `c2e44161cd142694f2b612e0be2dcc59cb656df6d42f8713adc4d05b9a22f5fa` |
| CNF | `9d978aecbc9958ae2957feb22c1430faa67cd0f93994e3996544b20139d18443` |
| complete SAT assignment | `b158ce7d7390395ee450440f407880fe9e1332adf45e8575145cc9e7e932aa18` |
| triple coloring | `52811269a70bfe6c28a591f3f02b6d29b16befff82aaf413f4bc8624f31bd967` |
| semantic result | `f0e01178ea39a0b4834511bcec2082c117c62ff289e57fea540f63e3f61529d4` |
| result receipt | `c542d8487bdd60359b0a8e707fa627accb68131863f4b7b93acfd9a34643b3bc` |

The raw result is a verified SAT instance of the stated necessary minor.
Mathematical interpretation remains with main; no independent review,
global bound update or acceptance is asserted by this executor.
