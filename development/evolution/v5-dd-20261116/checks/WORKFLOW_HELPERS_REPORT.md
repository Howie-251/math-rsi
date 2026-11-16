# Current facts and DD receipt helpers

Implemented only the four authorized helpers and this software regression set. Source: the read-only 2026-11-16 DD package's framework_snapshot. No historical source, README, site, skill, or live research state was modified; no commit was created.

Generic `base/tools/current_context.py` reads an existing state, renders current facts/request material, blocks fresh requests when an explicitly registered terminal result awaits parent consumption, and atomically replaces current_context before refreshing an optional generated reading view. It contains no DD family/count schema. Optional derived DD result counts now live exclusively in `extension_receipts.py`.

Real fixes: source edge paths in the batch planner/execution guard and prior-review paths in the generic request renderer resolve relative to STATE's directory. Receipt consumption requires the source n/m AND edge-file provenance to match a previously accepted checkpoint with evidence, instead of trusting n membership alone. Accepted checkpoint identities are retained inside the existing family; no hash, extra database or new global state is introduced. Replay/newer-stop semantics remain intact. Native C++ search logic is copied unchanged, with its explicit degree12/core41356/754-plane domain; it is not a generic D5 generator.

## Required caller documentation

Minimal generic state (opt-in on an existing project state):

```json
{"status":"PAUSED","current_context":{"obligation":"actual current question"},"current_context_view":"CURRENT.txt"}
```

`current_context_view` is optional and relative to STATE. `current_context_updated_at` is maintained by write_current. Optional `current_context.current_work.in_flight` is a mapping of jobs; each job may explicitly register `terminal_result` (relative to STATE). Its existence blocks request generation/execution until parent consumption, not mathematical acceptance. Generated request text explicitly states the absolute STATE directory used to resolve declared relative state, review and terminal-result paths, so a downstream reader need not share the caller cwd. Rendering without a request remains available while paused or awaiting consumption.

Request JSON requires `review_mode` in `task/new/delta/reuse`; optional `routes` selects exact keys from current_context.route_stops. `prior_reviews` entries have `path` and nonempty `scope`, with relative paths now based on STATE. Reuse requires nonempty unchanged `reuse_scope`, prior evidence and no `changes`; delta requires actual `changes`. This produces text only, never a model call or authorization.

The DD receipt adapter additionally expects `current_context.families[family]`:

```json
{"degree":12,"diameter":5,"phase_start_order":42402,"accepted_orders":[42403],
 "latest_graph":{"n":42403,"m":245949,"edge_file":"graph.edges","evidence":{"independent":"receipt.json"}},
 "accepted_checkpoints":{"42402":{"n":42402,"m":245937,"edge_file":"source.edges","evidence":{"independent":"source-receipt.json"}}}}
```

`accepted_orders` contains accepted new orders, not unverified author outputs. `accepted_checkpoints` is optional when the receipt source is latest_graph; older consumed source orders require their own accepted checkpoint. The adapter automatically retains the source and accepted final checkpoint; it does not invent paths/evidence for unexported intermediate edge files. A historical receipt must retain its original `construction_inputs.source_raw_edge_file` binding. If a source is relocated, parent may keep the historical logical path in its accepted checkpoint record, separately from latest_graph's runnable local path; do not rewrite immutable receipts or silently treat a basename match as identity. New independent receipts should record the actual local accepted source path. Relative receipt/checkpoint edge paths use STATE's directory.

The supported original independent shape is PASS plus construction_inputs.source_raw_edge_file, source n/m/accepted diameter premise, ordered prefixes with full per-prefix checks, final_graph and exact author_final_graph_comparison. The author needs running=false, source_n, accepted_new_graphs, final_n/m, final_edgefile and status. Original batch01 JSON was copied into a temporary directory and consumed successfully (eight accepted prefix orders42412…42419). This checks receipt FORMAT/consistency, not the underlying graphs anew.

Optional DD `phase_start_counts` with versions/parameters enables `result_counts`; then every family supplies parameter_previously_known and the current object supplies concrete_Lean_count. Without phase_start_counts no derived counts are required or added. Base simply renders any already supplied summary. Shared formal gaps, route stops, Goal status and review requirements remain unchanged.

Batch planning additionally requires family generator_domain=`d12_754_planes_core41356`, source latest_graph matching the largest nonempty accepted_orders, actual source header n/m, exact original plane input headed754, and explicit positive finite batch/CPU/wall limits. This is the existing continuation contract, not a seed initialization tool. `--plan-only` performs no compile/search. Execution rereads ACTIVE state, terminal-result guard and current source binding before creating a new output directory. Output remains `independent_validation:PENDING`; native field accepted_new_graphs is AUTHOR terminology, not parent acceptance. It still requires the independent verifier and parent judgment.

Example commands (all paths caller supplied):

```
python3 base/tools/current_context.py --state /task/STATE.json --request /task/request.json --output /task/INPUT.txt
python3 plugins/degree-diameter/tools/extension_receipts.py --state /task/STATE.json --family 12,5 --author /task/batch/RESULT.json --independent /task/batch/independent/RESULT.json --acceptance-basis 'Parent checked originals and accepted source premise; concrete Lean remains open'
python3 plugins/degree-diameter/tools/d5_blocking_batch.py --state /task/STATE.json --planes /task/RAW_PLANES_ACTUAL_IDS.txt --output /task/new-batch --max-new 8 --cpu-limit 20 --wall-limit 480 --plan-only
```

## Validation

Executed from this integration worktree:

```
python3 development/evolution/v5-dd-20261116/checks/workflow_helpers_test.py --archive plugins/degree-diameter/archive/dd-latest-two-parameters-20261116 --result development/evolution/v5-dd-20261116/checks/WORKFLOW_HELPERS_RESULT.json
```

Seven meaningful tests cover generic state/view and relative review, receipt source count/path/evidence rejection, replay preserving later zero-prefix stop, relative source planning plus paused/terminal-result/stale-source guards before output creation, optional DD counts, actual archived receipt compatibility, and C++17 compilation plus `--control`'s tiny combinatorial oracle/stop-status checks. Final results are in WORKFLOW_HELPERS_RESULT.json.

No production search, graph BFS, Lean, external model, live-state update, scheduler or automatic successor was run. Build/control products and all fixture/state writes use TemporaryDirectory and are removed afterward. Runtime dependencies remain Python standard library, POSIX resource/preexec_fn, g++/C++17 and the actual754-plane data. Source-D5 and geometric domain premises remain inherited; helper consistency checks do not certify mathematics.
