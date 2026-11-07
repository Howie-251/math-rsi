# Cardinality encoding rollback, 2026-10-06

New work uses the original exact state/occupancy encoding **plus bridges and
F3-main occupied-rank pruning**, adopted on 2026-10-13. Bridges were
made the default by the user's instruction on 2026-10-06. The compact
experiment did not replace the original encoder. The subsequent bridges
deployment appends entailed clauses after both exact counters and preserves
every original variable and clause. F3-main appends the measured exact prefix
counters with fresh auxiliary IDs after those clauses. Its independent ledger
binds guards, counts, allocation and clause hashes; F2/F23/vertex are excluded.
The current profile is `legacy_exact_with_state_path_bridges_f3_main_v1`.
The public construction path is:

```python
from state_charging.cardinality_layers import (
    CardinalityCell, STRICT_NO_TARGET, prepare_environment, materialize_cell,
)

cell = CardinalityCell(6, 9)
environment = prepare_environment(STRICT_NO_TARGET, cell.order)
built = materialize_cell(environment, cell)
# Only for an explicitly requested original baseline/replay:
baseline = materialize_cell(environment, cell, bridges=False)
# Historical bridges-only replay:
old_bridges = materialize_cell(environment, cell, f3_main=False)
```

Run on the Linux server in `forktqiu3`. This example constructs the formula;
production runs still require a fresh sealed campaign, controlled external
solver, complete SAT audit or a nonempty checked UNSAT proof.
New campaign snapshots must include the current F3-main helper and builder, not the legacy
builder copied from an old campaign. Historical sealed runtimes are unchanged.

The additive compact modules and dedicated test were moved out of active
import/test paths at the user's request:

- `lib/compact_cardinality_cnf.py`
- `state_charging/compact_cardinality.py`
- `tests/test_compact_cardinality.py`

Their exact bytes, hashes and original documentation are retained in
[`retired-compact-20261006`](../.trellis/tasks/09-03-35-state-cardinality-charging/research/retired-compact-20261006/manifest.json).
The old `python -m state_charging.compact_cardinality` entry point is retired.
Replay historical compact results using their own sealed runtime; do not
copy archived modules over a live or sealed campaign.

Same-cell proof-solver wall times, compact versus legacy, were **35.70 versus
33.10 hours** for A[6,9] and **75.93 versus 10.78 hours** for A[6,10]. At the
11:53 UTC+8 checkpoint, legacy A[6,9] proof checking was still running; all
other compared results had passed checking. These single-seed measurements
do not rank every possible instance or establish the causal transformation.

The rollback passed 29 Linux regressions without skips. Fresh construction
of both cells reproduced the legacy-control CNF hashes exactly. Frozen
runtimes, proofs and running campaigns are unchanged. See the
[comparison record](../.trellis/tasks/09-03-35-state-cardinality-charging/research/c6-legacy-comparison-20261004.md)
and [revised proposals](../.trellis/tasks/09-03-35-state-cardinality-charging/research/legacy-rollback-and-optimization-plan-20261006.md).
No new optimization benchmark was launched by this rollback.

## Historical compact interface (archived; unavailable in active imports)

The following describes the retired implementation and its sealed runs. The
commands below require the matching historical runtime, not the restored
workspace.

`compact_cardinality_756_v1` is an explicit encoding for the `(7,5,6)`
signotope cardinality cells. It preserves the projection onto triple colors.
Legacy builders and sealed campaigns retain their original CNFs.

## What changes

- Six direct ternary clauses per signotope packet replace private expression gates.
- Forward outer-path witnesses enforce the blue-5/red-6 bounds and the single
  relevant cap4/cup5 weak-7 prohibition. They are not exact path predicates.
- The original exact terminal recurrence is reused. An exact flag `F[v]`
  means a blue-4 and a red-5 both end at `v`, with independently chosen starts.
- Only `sum(F)=e` is counted. State injection gives `m=25+e-N`; the registered
  cell has `N=26+e-r`, so `m=r-1`. State-type and occupancy variables and the
  separate missing-ordinary counter are unnecessary.
- Optional `--bridges` adds exact cells and entailed state/path clauses. It is
  disabled by default and changes the CNF identity.

The exact counter uses the existing deterministic totalizer helper for both
inequalities. It does not count one-way witnesses.

## Linux entry points

Use `/data/ktqiu_hdd/math_agent` and the `forktqiu3` environment. Output
directories must be fresh. This example exports a formula without solving it:

```bash
python -m state_charging.compact_cardinality generate \
  --r 5 --e 5 --out res/state_charging/compact_example_a5_e5
python -m state_charging.compact_cardinality verify-export \
  --directory res/state_charging/compact_example_a5_e5
```

`generate` defaults to `strict_no_target`. The explicitly named
`--mode target_allowed_relaxed` retains the path bounds and packet axioms but
allows weak targets. Its evidence is mode-specific.

Exports contain canonical ASCII/LF `formula.cnf` and `metadata.json` with
variable roles, clause groups, source/Python/PySAT bindings, and full/base CNF
hashes. `verify-export` rebuilds all of these and rejects drift. For a complete
model from an externally controlled SAT solver:

```bash
python -m state_charging.compact_cardinality audit-sat \
  --directory res/state_charging/compact_example_a5_e5 \
  --solver-output solver.log --out new-sat-audit.json
```

The auditor checks every clause, then recomputes packets, all exact terminal
predicates, endpoint states, injection, weak targets, exceptional flags, and
`e,m` from the triple coloring. One-way marker values are never reported as
actual paths. The API also supports small-order semantic tests:

```python
from lib.compact_cardinality_cnf import build_compact_base
from state_charging.compact_cardinality import encode_exceptional_count

formula = encode_exceptional_count(build_compact_base(7), 1)
```

## Evidence boundary

This module exports and audits formulas; it does not start a campaign or
publish a theorem. Its separate schemas have `production_accepted: false`.
Future campaign integration must bind the new generator, mode, bridge option,
source files and exact CNF, then obtain a fresh nonempty proof and independent
checker result for each UNSAT cell. Existing proofs cannot be reused for a
changed CNF. Active C5 artifacts remain bound to the legacy encoding.

Equivalence does not assert identical auxiliary assignments, propagation,
learned clauses, or solve times. The general argument and bounded audit are
recorded in
[`equivalence-audit-20260927/README.md`](../.trellis/tasks/09-03-35-state-cardinality-charging/research/equivalence-audit-20260927/README.md).
The implementation audit adapter exercises the actual builder, including the
optional bridges, through the retained independent oracle and proof checker.
