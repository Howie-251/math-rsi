# Semantic Encoding Equivalence

## 1. Scope / Trigger

Apply when changing the state-cardinality encoding, removing path definitions,
or eliminating auxiliaries. The explicit `compact_cardinality_756_v1` builder
implements the audited simplification, but was retired from active imports
on 2026-10-06 after slower same-cell solves. Use the original
`cardinality_layers.prepare_environment` / `materialize_cell` path for new
work; from 2026-10-13 its default is original exact plus bridges and F3-main. The historical bridges deployment below describes its old profile.
The compact APIs below describe archived code and sealed runtimes.
Existing sealed campaigns retain their original builders; compact exports
are not campaign acceptance receipts.

## 2. Signatures

The public entry points are:

```text
build_compact_base(order, *, mode="strict_no_target", bridges=False) -> CompactBase
encode_exceptional_count(base, count) -> CompactFormula
build_compact_cell(raw_cell, *, mode="strict_no_target", bridges=False) -> CompactCell
export_compact_cell(built, directory) -> dict
replay_compact_export(directory) -> CompactCell
audit_compact_assignment(formula, model, *, cell=None) -> dict
python -m state_charging.compact_cardinality generate --r R --e E --out NEW_DIR [--bridges]
python -m state_charging.compact_cardinality verify-export --directory DIR
python -m state_charging.compact_cardinality audit-sat --directory DIR --solver-output LOG --out NEW_JSON
```

The retained research checker is
`.trellis/tasks/09-03-35-state-cardinality-charging/research/equivalence-audit-20260927/audit.py`:

```text
audit.py --runtime <sealed-runtime> --out <fresh-root> --solver <AE> --checker <repaired-checker>
```

Its result contract includes `tests`, `verified_unsat`, `audited_sat`,
`unknown`, and an explicit bounded-audit limitation. It is not a campaign
acceptance receipt. The sibling
`compact-implementation-validation-20260927.py` adapts that unchanged oracle
to the actual builder; `--bridges` validates the optional clause layer too.

## 3. Contracts

- Equivalence means `forall coloring x: exists old_aux Phi_old iff exists
  new_aux Phi_new`. Equality of two overall SAT statuses is insufficient.
- Exact exceptional flags require full terminal-path and Boolean equivalences.
- In the 3-by-4 bounded domain, exceptional means `h1=4 and h3>=1`. State
  injection gives `e=sum(F_v)` and `m=25+sum(F_v)-N`.
- One-way outer-path witnesses can support prohibitions, but must not feed
  exact counts, path-existence reports, or legacy consumers of `cap.solution()`.
- Eliminate private expression gates only after accounting for every consumer.
- Renumbered or changed CNFs require fresh proof binding. DRAT proofs cannot
  be reused merely because formulas have equivalent semantic projections.
- `CompactBase` uses immutable clauses/maps and exposes no legacy `cap`/`cup`
  API. Triples/outer witnesses use zero-based keys; exact terminal predicates
  and cells use the original one-based down-set keys.
- Small-order API accepts plain integer `1<=N<=35`; count is a plain integer
  `0<=e<=min(10,N)`. Registered cells use the unchanged `normalize_cell` registry.
- `compact_cardinality_export_v1` binds the complete variable ledger, clause
  groups, full/base hashes and runtime/source hashes. Export is create-only.
  Replay rebuilds every field and the canonical ASCII/LF CNF. It rejects
  symlink files, changed metadata, source drift and changed CNF bytes.
- SAT auditing requires a complete assignment and a fresh canonical formula;
  it recomputes exact paths, flags, optional cells, states, injection, and both
  counts from triple colors. Strict mode rejects weak targets; relaxed mode
  reports them. Both schemas explicitly keep `production_accepted=false`.

## 4. Validation & Error Matrix

| Condition | Required interpretation |
|---|---|
| SAT mismatch witness | Reject the proposed equivalence or fix the implementation |
| Timeout or unchecked UNSAT | Inconclusive, never an equivalence certificate |
| UNSAT of a canonical-lifting query | Also justify that canonical definitions extend every coloring |
| Same SAT status for two formulas | Smoke evidence only |
| Bounded checks pass | Record tested orders separately from the general mathematical proof |
| Existing caller expects exact outer paths | Retain its exact semantics or introduce a separate interface |
| Invalid mode, integer/bool confusion or cell order/count mismatch | Reject before export/audit |
| Altered clause/variable metadata or partial SAT assignment | Reject; no audited receipt |
| Changed optional bridge flag | A different CNF requiring a new proof |

## 5. Good / Base / Bad Cases

- Good: exact terminal flags for counting, one-way outer witnesses for
  prohibitions, and independent recomputation from triple colors.
- Base: N=7 has a legal exceptional endpoint without a shared-outer-endpoint
  weak 7-gon; both encodings must retain such SAT examples.
- Bad: red triples are exactly the triples inside `{3,4,5,6,7}` at N=7. The
  real exceptional set is `{7}`, but one-way outer witnesses can report
  `{6,7}` if incorrectly used for counting.

## 6. Tests Required

Retain two-direction domain projection checks against independently enumerated
paths, exact-terminal and exceptional-flag mismatch queries, both count
identities, SAT nonvacuity, and negative controls for unsafe counting and a
missing weak target. Check negative queries by DRAT and positive assignments
both clause-wise and semantically. Use controlled external solver processes.
`tests/test_compact_cardinality.py` additionally checks exhaustive five-point
projections, deterministic full exports, metadata/model rejection, exact count
controls, the unsafe-marker regression and strict/relaxed target behavior.

## 7. Wrong vs Correct

Wrong: delete all reverse path definitions and count the remaining outer
cap/cup flags as if they were actual path existence.

Correct: preserve separate exact predicates for counting; interpret a one-way
witness as a closure marker only. The 2026-09-27 audit found a concrete SAT
counterexample to the wrong variant and passed all 46 intended checks.

## Same-cell performance controls

### 1. Scope / Trigger

When claiming speedup for an equivalent encoder, compare the exact logical
cell. Same-N cells from different C_r rows change both counts and are not
controlled encoding comparisons. Preserve ongoing campaigns and create a
separate, explicitly authorized result root.

### 2. Signatures

The October 4 two-cell adapter is `tmp/c6_legacy_comparison_20261004.py`:

```text
prepare --root NEW_ROOT --validation PASSING_TEST_RECEIPT
launch --root SEALED_ROOT --seal-sha256 EXTERNAL_SHA
run --root SEALED_ROOT --seal-sha256 EXTERNAL_SHA
```

### 3. Contracts

- Exact cells are A[6,9]/A[6,10], N=29/30, missing count 5.
- Bind the completed compact cell, mode/bridges, command, exit and log hashes.
  Retaining old proof hashes for timing is not independently rechecking proofs.
- Use the same AE binary/default seed/proof mode and repaired checker options.
  Preserve the same SAT-first stage, measuring proof solve/check separately.
- Reuse immutable process/worker code in an isolated imported module. Configure
  only task coverage and a separate receipt schema; grant no theorem credit.
- `comparison_results.json` stores old/new wall-time ratios, available solver
  CPU times and proof sizes. Ratio >1 means compact faster on that cell/seed.
- Record resource conditions and describe historical-load and single-seed
  limitations. Formula size and conflicts/second are not complete-run speedup.

### 4. Validation & Error Matrix

| Condition | Required behavior |
|---|---|
| Different cell/counts, binary, proof options or seed | Reject a controlled comparison |
| Formula replay mismatch, invalid SAT or checker rejection | Stop/reap owned comparison peers only |
| Existing result root or stale launch artifact | Refuse an in-place rerun |
| Interrupted or unfinished solve | Report censored elapsed time; do not invent a speedup ratio |

### 5. Good / Base / Bad Cases

Good: old and compact A[6,9] have identical coordinates and bound executable.
Base: two cases/one seed support only those measurements, not a general claim.
Bad: divide C5 A[5,8] time by C6 A[6,9] time and call it an encoding speedup.

### 6. Tests Required

Validate exact coordinates and baseline options, real solver/checker execution,
concurrent ownership and cancellation, drift/empty-proof/SAT rejection, and
reused process-helper behavior. Fresh-rebuild every production CNF before a
common start barrier. Retain observed real launch identities.

### 7. Wrong vs Correct

Wrong: extrapolate a 60-second initial rate using the old full conflict count.
Correct: measure the completed same-cell solve and check, preserving raw
receipts and acknowledging that propagation and proof-search work can change.

## Legacy restoration and subsequent performance experiments

- Archived compact source/test bytes and original documentation live in
  `.trellis/tasks/09-03-35-state-cardinality-charging/research/retired-compact-20261006/`.
  Keep this outside production imports and ordinary test discovery. Hash-bind
  archived files; do not rewrite previous deployment or campaign seals.
- Restore against a verified source seal, not a repository-wide reset. The
  October 6 rollback validates the legacy C5 module hashes and regenerates
  A[6,9]/A[6,10] to the exact legacy-control CNF hashes. Retain the repaired
  checker; reverting encoding is not authorization to reintroduce its bug.
- A future optimization is opt-in and changes one family at a time. Preserve
  exact path/state/count semantics unless a new projection proof justifies a
  change. Entailed pruning clauses require a domain-level derivation and
  nonvacuous small-order tests, not an UNSAT query against an already UNSAT
  full research cell as its sole justification.
- Track original and post-preprocessing formula size, complete solver/checker
  wall and CPU time, conflicts, decisions, propagations, proof bytes, and RSS.
  Smaller CNF, fewer auxiliaries, short-run throughput and lower propagation
  totals are not substitutes for faster complete solves.
- For strength comparisons use matched partial assignments over triple colors
  or exact shared semantic predicates; compare propagated shared facts and
  conflicts, not raw auxiliary counts with different meanings.
- Benchmark fresh proof-bound CNFs on the same cells, solver and proof mode,
  paired across several seeds and completed controls. Unknown/timeouts remain
  censored. More variables/clauses may be worthwhile if their propagation
  reduces actual search. No speedup claim precedes measured completion.

### Isolated C1 ablation contract (2026-10-06)

`tmp/c1_encoding_ablation_20261006.py prepare/run` seals original C5 runtime
bytes and separately generated A[1,1], A[1,2], A[1,10] formulas. Baseline
CNFs must byte-match historical C1. `cardinality_variants_20261006.py` never
patches a builder: bridges append clauses; packets replace only a verified
contiguous private-gate block and reject any outside gate consumer. Preserve
all variable IDs and declared count; report used variables separately.

Nine seed-0 controls precede any additional seeds. Only checked candidates
with geometric-mean solve ratio <0.95 and maximum case ratio <=1.05 advance
to paired seeds 1,2. Uniform external solve/check limits are 14400/21600
seconds; timeout/unchecked results cannot win. Checker concurrency is three.
The report cannot promote code or grant theorem credit. Existing production
sources and campaigns remain unchanged, including when a candidate loses.

Validation covers actual generated bridge counterexample proofs with SAT
base controls, packet projection, no outside gate consumer, full CNF identity,
paired-ratio gating and real worker cancellation. Register dynamically loaded
helper modules in `sys.modules` before sending their functions through a
multiprocessing Pool; test that exact adapter path, not just the original
helper's separately loaded capability test.

### Historical-only hard bridges control (2026-10-06)

1. **Scope:** When the user asks to reuse an existing original timing, do not
   launch a fresh baseline. The hard trial is A[6,10], N=30, m=5, seed 0.
2. **Signatures:** `tmp/c6_bridges_comparison_20261006.py prepare --root NEW
   --validation JSON`, then sealed `run --root ROOT --seal-sha256 SHA`.
3. **Contracts:** Exactly one `bridges` formula/worker; seal field
   `baseline_policy=historical_only_no_new_solve`. Original CNF bytes must
   equal the bridges prefix before 4,814 append-only clauses. Original
   variables/counts/clauses persist. The adapter configures a private import
   of the unchanged C1 worker engine, never the running C1 process or files.
   Solver/checker limits are each 172,800 seconds; theorem credit and
   automatic promotion remain false. Report field
   `new_baseline_solver_invocations=0` and the historical receipt binding.
4. **Validation/error matrix:** Wrong cell, variant, seed, deadline or extra
   formula → reject. Historical log/hash/verdict drift → reject. Timeout or
   unchecked result → inconclusive. Existing root/claim → refuse rerun.
5. **Good/base/bad:** Good: compare complete proof-solve times and separately
   report checks and historical load differences. Base: one checked cell at
   one seed. Bad: equate workflow totals when the original had SAT-first and
   the new trial begins directly with the proof solve.
6. **Tests:** `test_c6_bridges_comparison_20261006.py` verifies byte identity,
   append-only structure, protocol rejection, Pool capability, a real tiny
   bridges-only solve/check with the extended limits, and censored comparisons.
7. **Wrong/correct:** Wrong: silently rerun the original for a cleaner paired
   control after the user excluded it. Correct: bind its retained evidence,
   run only bridges, and state the resource-condition limitation.

## Default bridges deployment (2026-10-06)

### 1. Scope / Trigger

The user's explicit adoption instruction makes bridges the default for new
C_r searches. Earlier benchmark `never_automatic` policies still govern those
experiments; this separate manual deployment does not rewrite their receipts.

### 2. Signatures

```python
materialize_cell(environment, cell, *, bridges=True) -> BuiltCardinalityCell
state_path_bridge_clauses(encoding) -> tuple[tuple[int, ...], ...]
DEFAULT_CARDINALITY_ENCODING = "legacy_exact_with_state_path_bridges_v1"
```

### 3. Contracts

- Append bridges after the four original exact e/m counter components. Retain
  all original variables, base clauses, reverse definitions and counter IDs.
- The environment stays immutable. The bridge helper deduplicates boundary
  units in first-occurrence order, matching measured experiment CNF bytes.
- Bridges are entailed by exact cells/terminal paths and blue-5/red-6 bounds;
  they also apply to target-allowed formulas and do not depend on r/e counts.
- `bridges=False` explicitly reproduces original baseline CNF and formula
  metadata. Baseline use is for requested comparisons/replay, not new defaults.
- `BuiltCardinalityCell.bridges` selects SAT audit reconstruction. Default
  formula metadata includes `cardinality.pruning` with the encoding name,
  bridge count and clause hash; full formula digest includes bridge clauses.
- New campaign snapshots must take the current production builder and check
  the default encoding constant. Dated predecessor-copy scripts are historical
  protocols, not a source of new default runtime bytes. Preserve every existing
  sealed runtime and use its own version for historical manifest replay.

### 4. Validation / Error Matrix

| Condition | Behavior |
|---|---|
| Non-boolean bridges option | Reject before materialization |
| Unsupported state specification/order | Reject bridge construction |
| Audited object switches bridges profile without changing its formula | Reject fresh replay |
| Formula hash changes | Require a new proof binding |
| Hard-case proof checking pending | Keep pending; deployment grants no theorem credit |

### 5. Good / Base / Bad Cases

Good: A[6,10] generates the exact tested bridges CNF, adding 4,814 clauses.
Base: A[1,1] defaults to 327,276 variables and 1,206,420 clauses, with the
original 1,202,820-clause formula available explicitly. Bad: add bridges
before counters and silently change the measured clause ordering, or replace
files inside a live campaign's runtime.

### 6. Tests Required

`tests/test_state_charging_cardinality_bridges.py` covers exact tested bytes,
append-only behavior, baseline preservation, both counter boundaries, profile
tampering, option types, small strict/relaxed SAT bases and violated-bridge
UNSAT queries. `tmp/validate_default_bridges_20261006.py` additionally checks
the remaining measured C1/C6 formula bytes and six fresh external proofs for
the production helper, reusing the bounded proof oracle.

### 7. Wrong vs Correct

Wrong: copying the legacy predecessor runtime and assuming an edited active
workspace changes its formula. Correct: snapshot the current bridges builder,
verify its profile, and freshly reconstruct/hash the new campaign's formulas.

## F3-main default contract (2026-10-13)

The explicit adoption instruction changes only future C_r materialization to
`legacy_exact_with_state_path_bridges_f3_main_v1`. Historical sealed builders
and result credit remain unchanged.

- `materialize_cell(environment, cell, *, bridges=True, f3_main=None)` resolves
  `None` to the bridges flag. Pure exact and historical bridges-only replay use
  `bridges=False` and `f3_main=False`, respectively. True F3 without bridges is rejected.
- The original base and exact e/m clauses/IDs precede bridges and the measured
  F3-main clauses. Preserve the frozen prefix recurrence, allocation and clause
  order. F2, F23 and vertex-count constraints are excluded.
- If vertex v has state h, all proper occupied subsets of h precede v and all
  proper occupied supersets follow v. Hence their counts are at most v-1 and N-v.
  Exact prefix thresholds admit a unique canonical lift of every base model;
  guarded rank clauses are entailed. This argument applies to r6/m5/e10 and
  strict/relaxed bases and does not rely on a target formula already being UNSAT.
- Keep exact-cardinality and F3 metadata separate. F3 auxiliaries are contiguous
  fresh IDs starting after exact-cardinality.num_vars. Bridge counts exclude F3.
  Built cells retain resolved flags and immutable F3 ledgers; full SAT audit
  reconstructs the same profile and rejects metadata drift.
- Campaign records require the known F3 schema for the new profile, canonical
  counter/guard/aux/clause hashes, matching base/final variable and clause counts,
  and agreement between formula and exact-cardinality metadata. Rehashing the
  outer record does not repair tampering. Fresh formula replay remains mandatory.
- Future runtime snapshots must include `state_charging/f3_main_rank.py` via the
  actual automatic import closure. Do not copy an older sealed builder forward.
- Verify the four measured F3-main BM CNF hashes, both historical opt-outs,
  generic guards/thresholds, nonempty small SAT lift/replay, metadata negative
  controls, source closure and existing focused regressions on Linux. This
  deployment does not create checked UNSAT credit or start a new campaign.