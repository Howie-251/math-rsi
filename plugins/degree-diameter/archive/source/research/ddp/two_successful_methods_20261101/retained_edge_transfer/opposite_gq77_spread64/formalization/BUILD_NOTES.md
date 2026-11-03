# Direct Lean build of the fixed 160050 incidence graph

Pinned executable: `.tools/lean-4.24.0-linux/bin/lean` (4.24).
`compile.py` reads the already saved explicit LEAN_PATH from
`research/ddp/refresh_20261029/f5_full_d20_D3/FORMAL_ENV_COMMAND.json`, uses `-j1`
and LEAN_NUM_THREADS=1, and writes only each newly owned module's olean. It
sets a per-child CPU hard limit and measures child user+system CPU relative to
the pre-spawn baseline. No lake, dependency install, upgrade or old rebuild.

From the repository root:
```
python research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/formalization/compile.py OppositeGQ77SpreadDefinitions 115
python research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/formalization/run_preparation.py
```
Preparation is one worker; it preserves PASS modules and stops on failure.
After successful representative rows000/399, `compile_remaining_rows.py` checks
the measured extrapolation before starting at most8 independent `-j1` workers
for rows001..398. Each row has115 CPU; all attempts, including failures, are
counted toward15000 CPU with200 CPU reserved for assembly. It stops dispatch on
first failure and has aggregate CPU enforcement. No automatic timer extension.

The first incidence chunk attempt exposed only reducibility during typeclass
inference: `by decide` did not synthesize `Decidable (IncidenceChunkCheck 0)`
without unfolding the named proposition. The chunk proofs now explicitly unfold
that definition before `decide`. This changes no object, data or proposition.
The failed receipt is retained in `build_history/` and counted. Already PASS
Definitions and IncidenceData were not recompiled.

Every module's `*_HANDLE.json`, `*_RESULT.json` and `.log` provide its real
execution state. `INPUT_BINDING_CHECK.json` records readback/formula equality,
which performs no BFS. Parent owns fresh graph acceptance and external A/B/C
reviews; kernel completion and world-record/priority status are separate.

The initial chunk-to-arbitrary-index assembly also needed the explicit product
eta identity `Prod.mk.eta` before the equivalence inverse rule. The failed
assembly receipt (7.554776 CPU) is archived and counted; the corrected
Incidence module PASSes with standard axioms, without rebuilding finite chunks.

During the first8-worker row batch, a real JSON HANDLE read/write race stopped
the dispatcher (not any Lean module). All existing children were allowed to
finish:217 actual row receipts, all exit0. The dispatcher error and stale
handle are retained in batch_history/. Handle/result publication now uses
atomic replace; only183 previously uncompiled rows are resumed, with the
same aggregate15000 CPU budget and no recompilation of PASS rows.

Final actual outcome: all400 input rows plus Inputs/Exact and the separate
Audit import PASS. Inputs31.064020CPU, Exact2.456379CPU, Audit2.346776CPU.
All415 current modules PASS; total Lean CPU6240.278580 includes both historical
failed elaborations9.436508CPU. The final unconditional theorem and final_claim
print only propext/Classical.choice/Quot.sound. No remaining Lean obligation or
background compiler. Source is frozen for root final-C review.
