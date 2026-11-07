# Bridges becomes the default C_r encoding

## User authorization and evidence boundary

On 2026-10-06 the user explicitly requested changing the code to bridges and
using it for future C_r solves. This is a manual adoption instruction after
the C1 timings and the A[6,10] 4.43x solve-time improvement. It supersedes the
earlier requirement to leave the production default unchanged during trials.
The experiment controllers retain their `never_automatic` policy and immutable
receipts. A[6,10] proof checking was still pending when this deployment began;
adoption does not claim a completed check or new theorem acceptance.

## Production behavior

`state_charging/cardinality_layers.py` now exposes:

```python
DEFAULT_CARDINALITY_ENCODING = "legacy_exact_with_state_path_bridges_v1"
built = materialize_cell(environment, cell)  # bridges enabled
baseline = materialize_cell(environment, cell, bridges=False)  # explicit replay
```

The default appends exactly the measured state-to-terminal-path clauses after
the unchanged e/m counters, with first-occurrence boundary-unit deduplication.
The original variables, clause order, exact definitions and counters remain.
It applies to every registered r/e cell in strict and target-allowed modes.
The shared environment is not mutated. The explicit false option reproduces
the original CNF and original formula/cardinality metadata.

The built object records the selected profile. Default formula metadata adds
`cardinality.pruning` with the encoding name, bridge count and clause hash;
the full formula hash incorporates the bridges. SAT auditing rebuilds the
selected profile and rejects a profile/formula mismatch before accepting a
model. Unsupported non-boolean options fail before materialization.

The production bridge helper is `state_path_bridge_clauses(encoding)`. Its
general entailment is the common-predecessor path-extension argument retained
in the [optimization proposal](legacy-rollback-and-optimization-plan-20261006.md).
No count assumption or target-free premise is needed for those clauses.

## Future campaign preparation

Project `AGENTS.md`, README and encoding documentation now require new C_r
campaigns to snapshot the active bridges builder and verify its encoding
constant. Old dated C2–C6 generators copy their predecessor's sealed runtime;
copying them unchanged would retain an old encoder and is not the procedure
for a new search. Existing sealed campaigns, CNFs, proofs and processes keep
their own versions. Historical replay must use those versions or the explicit
baseline option with appropriate formula bindings. No current experiment is
restarted by this deployment.

## Validation and deployment record

All execution is on the Linux server in `forktqiu3`. The staged runtime is
`/data/ktqiu_hdd/math_agent/tmp/bridges_default_deploy_20261006`.

The 28 focused unit/regression tests passed without failures, errors or skips
in 26.023 seconds. Coverage includes the existing cardinality/manifest tests,
exact A[1,1] original/bridges DIMACS hashes, append-only behavior, exact count
boundaries, audit-profile tampering, option types, and six nonvacuous small
strict/relaxed implication checks. The first stage run lacked a test-only
import closure for `typed_pair_proofs`; supplying those unchanged dependencies
resolved the import error. No production source repair was required.

Additional hard-formula parity checks and fresh external bounded proofs are
recorded below after validation, followed by the observed deployment receipt.

### Completed validation and deployment

The additional parity run reproduced the measured bridges and original
baseline DIMACS bytes for A[1,2], A[1,10], and A[6,10]. Together with the
A[1,1] regression this covers all four measured cases. The production bridge
helper also produced **six fresh checked UNSAT counterexample proofs** at
N=7,8,9 in strict/relaxed mode, each with a separately solved and clause-audited
SAT base control. All six passed the repaired external checker. These bounded
checks supplement the general entailment argument; they are not new C_r
theorem proofs.

At **2026-10-06 18:19:56 UTC+8**, the tested module and new test were installed
in `/data/ktqiu_hdd/math_agent`, together with the corresponding documentation
and future-campaign policy. A new Python process imported the active workspace
module and confirmed that `materialize_cell` has `bridges=True` by default.

Installed production module SHA-256:
`2a4600ba21a57cb1e50e8686e66c86a43ee33ad281664128b19ab3b9442ff1fe`.
Original baseline module SHA-256:
`b1da1bda9c13d2486740ccb16e65a46a7096754999aab7580ff76a10b7405a89`.
New regression module SHA-256:
`dd85e3c377782d0c54a5460ab06f098987dac0e869d1aedd2683a484d1eb094c`.

Original source and documentation bytes were backed up before replacement;
the baseline is retained on Linux under the stage's `baseline/` directory
and in the local evidence bundle. All twelve original modules matched the
rollback manifest before deployment; only `cardinality_layers.py` changed
among them. Post-deployment verification matched every sealed runtime file
for the C1 ablation, A[6,10] bridges trial, and ongoing compact C6 campaign.
No new search was launched or existing search restarted.

Local retained evidence:

- [Deployment receipt](evidence/bridges-default-deployment-20261006/deployment_receipt.json)
- [Validation receipt](evidence/bridges-default-deployment-20261006/deployment_validation.json)
- [Formula parity](evidence/bridges-default-deployment-20261006/formula_parity01.json)
- [Six-proof summary](evidence/bridges-default-deployment-20261006/production_bridge_proofs01/summary.json)
- [Original production module](evidence/bridges-default-deployment-20261006/baseline/state_charging/cardinality_layers.py)

The evidence ZIP is 2,012,254 bytes, SHA-256
`c2e454fa4b3bc2cd8cb28a0bb3959ac84e93f94fa6b523a1abb935c2f0a1edaf`.
