# Read-only primary-evidence audit, 2026-10-27

This audit reads existing local receipts and sources and hashes existing local files. It performs no scientific execution, replay, solver call, download, SSH call, review, acceptance update, task update, or mutation of an existing file. It is an evidence inventory, not a mathematical review. Paths below are relative to `D:/科研/math agent/erdos-szekeres-sat-main` unless explicitly Linux absolute.

## Scoped b=25 acceptance

Primary raw snapshot: `tmp/d7_global_critical_20261027/preflight.json`, fields `b25_current_status`, `b25_acceptance`, `b25_authorization`. Independently repeated status snapshot: `tmp/d7_tau_critical_20261027/preflight.json`, field `b25`.

Linux status path: `/data/ktqiu_hdd/math_agent/res/state_charging/20261026_c8_row_acceptance_v1/current_status.json`, SHA256 `0d50ba15437db4a6ade429d85739d2791c80fc23bc01a3e7f91ed6b1a49ada8c`, 4,819 bytes.

Linux acceptance path: `/data/ktqiu_hdd/math_agent/res/state_charging/20261026_c8_row_acceptance_v1/campaign_acceptance_audit.json`, SHA256 `70b32da5fe33e0e2e20e6bdb12684bd69ac45aeb765bcf51f5e00c83153ccc68`, 12,348 bytes.

Linux authorization path: `/data/ktqiu_hdd/math_agent/res/state_charging/20261026_c8_row_acceptance_v1/human_acceptance_20261026_v1/human_authorization.json`, SHA256 `9d588d14c2c4267b2274928c97068ce95a263685d3c350c284ef7ca67bfb30e9`, 1,441 bytes.

Raw status fields:

- `status = C8_ACCEPTED_ALL_TEN_ROWS_SCOPED_BOUND25_HUMAN_AUTHORIZED`
- `acceptance_authority = human_user`, `certified_upper_bound = 25`, `theorem_credit = true`
- `accepted_rows = [1,2,3,4,5,6,7,8,9,10]`, `pending_rows = []`, `full_charging_m_ge_e = true`
- `review_assurance = same-family/provisional`
- `backend_verification = unknown/unverifiable`, `effort_verification = unknown/unverifiable`
- `scope.domain = complete ordered rank-3 signotope; blue-path-5/red-path-6 bounds; no weak 7-gon`
- `scope.quantification = Every X in this domain at every finite order N`
- `scope.count_identity = N=25+e-m`, `scope.conditional_row_theorem = e>=8 implies m>=8`
- `scope.not_a_global_geometric_erdos_szekeres_bound = true`, `scope.order25_existence_claim = false`
- `task_remains_in_progress = true`

Raw authorization text: `接受这次 GPT 审查结果，正式验收 C8，将限定模型域内的上限更新为 25，保留 same-family/provisional 说明。` Its `backend_model` and `actual_effort` are null. Its proof-body reads, formula replays, fresh checks and new solver authorizations are false. No acceptance is inferred here beyond these raw fields.

## Separate actual 25-point fixture verification

Files: `tmp/d7_global_critical_20261027/check_D26_fixture.py`, `D26_fixture_execution.json`, `D26_fixture_result.json`, `semantic_check.py`.

The existing Linux execution receipt invokes `/opt/anaconda3/envs/forktqiu3/bin/python3.12 -B /data/ktqiu_hdd/math_agent/tmp/d7_global_critical_20261027/check_D26_fixture.py` under `timeout 50s`, with exit 0 and elapsed 1.0996665954589844 seconds. This audit does not rerun it.

Raw result: `schema = D26_classical_middle_insert_deterministic_fixture_v1`, `status = PASS`, `solver_invocations = 0`, `acceptance = false`, `scope = One D26 fixture and its explicitly supplied 25-point deletion; no R23 byte-identity claim`.

`fixtures[1]`: `n=25`, `all_triples=2300`, `all_packets=12650`, `bad_packets=[]`, longest red witness `[0,1,2,3,10]` (five vertices), longest blue `[0,3,4,15]` (four), `max_same_endpoint_sum=8`, `weak_witnesses=[]`, `forbidden_joint=[]`, `D7_valid=true`, `fixture_expected_conditions_pass=true`. Its exhaustive transversal record has `tau=0`, `red6_count=0`, `red6_masks=[]`, `uses_b25_or_tau5_as_search_assumption=false`.

Source constructs the B20 recursive `(4,4)` fixture, inserts an all-red A block between B indices 9 and 10, and separately supplies A sizes 6 and 5. It stores every triple color for each fixture. The A5 fixture is the explicit order-25 deletion. This is separate from the scoped acceptance record, whose existence claim is false.

Locally checked result SHA256: `68b7d0f92125e3d134ef3a7879234a203f4f22e0db23399dde06b5d8375f473d`.
Recorded source SHA256: `7a29d0b1c86e3d6f9d6fda41e386394e7299930d0194078933bf1b3f175109d4`.
Recorded checker SHA256: `6ddee9b04ee2b77bb5727a5a06f55aaca12774e76c066ebd88d5cce885c1ab70`.

## Joint17: current local source versus old Linux replay

`tmp/balanced49_abstract_port_20261026/joint17_transport_result.json`: `status=source_identity_verified`, `plain_bytes=38734663`, `received_bytes=10190435`, SHA256 `22950a14595f72b93a769261738d029b2aa27d04aa27e1f44fa2dce77775da2a`. The local `ES7Joint17Literal.lean` SHA256 was freshly checked and agrees.

`tmp/balanced49_abstract_port_20261026/small_literals_execution_02.json` is an execution envelope with exit 0, but its embedded combined result has `status=FAILED`, `error.type=URLError`, `error.detail=<urlopen error [Errno 101] Network is unreachable>`. Terminal20 succeeds first; Joint17 has source-index metadata only, with no replay result. The envelope exit 0 does not change the embedded failed status.

Latest inspected Linux snapshot is `tmp/d7_global_critical_20261027/preflight.json`, UTC `2026-10-27T03:18:47.544888+00:00`; `balanced49_inventory` contains Through14 and Terminal20 literal sources and replay receipts, but no Joint17 literal or replay receipt. This is a dated snapshot, not a live inventory.

## Through14 and Terminal20 strict RUP receipts

`tmp/balanced49_abstract_port_20261026/through14_replay_result.json`: `status=PASS`; scope explicitly says fixed-byte finite strict RUP replay only, no semantic transfer or mathematical acceptance. Source SHA before/after is `640acebb5128073f1731f88893fe4178fb73d9259577fc562f4579c66650e250`; CNF SHA `8a59bfc9ee2a64987b41fb9fc7251fb25c20a70388508afcd5478b1d51a4812b`; proof SHA `1c98ef23e6584ea17badddf79555e3d634dc40ecd82a56fb17f038d63ee033ac`. Replay exit 0; checker reports `variables=12156`, `source_clauses=5077`, `additions=3009`, `strict_hints=81736`.

Terminal20 raw replay is embedded in `small_literals_execution_02.json`, and also in the authoritative Linux inventory snapshot `tmp/balanced49_fan_joint_deficit_20261026/linux_inventory_01.json`. Terminal20 fields: `status=PASS`, `source_unchanged=true`, literal SHA `31dd7141eb732644b4c47ac628f1732aa93307c92c0294eb1bc67d5278d35e32`, CNF SHA `8aba4bbec848299d073911bc23adcbf22a009d59e9acc4f2047671c4b17711c6`, proof SHA `01d4855b0b4f49af6380937956724d233c2cf44a922e437cfe0a3a264e6ca943`, replay exit 0; checker reports `variables=12722`, `source_clauses=25074`, `additions=79173`, `strict_hints=3957546`.

Both use recorded checker executable SHA `e6635afdf4a9d2447a0d8c1d1a5eb820b4980f0c86871eba1685d0bcfb6f98b2`. Through14 receipt includes one positive and six deliberately invalid controls with the expected success/rejections. These finite checks do not establish the common semantic assignment/frame.

## Closure provenance and semantic status

`tmp/balanced49_transfer_20261026/retrieval_receipt_network.json`: `scope=source_text_retrieval_only`, `status=source_text_acquisition_complete`, `full_archive_sha256_checked=false`, `retrieved_code_executed=false`, `lean_compiled=false`, `certificate_replayed=false`. Public archive URL is `https://zenodo.org/api/records/22842891/files/es7_es8_bounds_81_319_v1.zip/content`.

Its deferred `ES7ClosureLiteral.lean` entry: 732,220,946 uncompressed bytes, 163,629,410 compressed, archive offset 8,689,045, CRC32 1,346,279,322; manifest SHA `0c4ddc5ab3aa65bed742b9f34d1bab65589e70c2108c21d5b935d9086a0f08ed`; `hash_status=manifest_declared_only_not_download_verified`, `reason=exceeds 8 MiB source-text acquisition limit`, `proof_data_obligation_open=true`. `tmp/balanced49_abstract_port_20261026/dependency_audit_result.json` also lists ClosureLiteral as a missing source with that declared hash.

The acquired `tmp/balanced49_transfer_20261026/sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureData.lean` contains `acceptedCheck`, `accepted := by native_decide`, and `impossible (m : Model c realStates)`, applying `checked_sound` and `ES7ClosureLiteral.unsat (assignment d (meaning m))`. This identifies source dependencies; it is not a compilation or semantic-soundness receipt.

`tmp/balanced49_fan_joint_deficit_20261026/ENGINEERING_STATUS.json` raw fields: `abstract_semantic_bridge=not established`, `balanced49=not established by these receipts`, `independent_review=not run, per explicit user skip`, `acceptance=unchanged`. No inspected primary receipt establishes one actual assignment/frame jointly satisfying all four certificate models or a complete joint source/schema binding.

## Lean download, upload, deployment, compilation

`tmp/balanced49_abstract_port_20261026/lean_windows_resume_result.json`: `status=downloaded_hash_verified`, `actual_bytes=564056221`, expected and actual SHA `ce6e79dd19ea03c0bc17f9d565c3bac20cd2884561e3b431e5b293c1fbb2b5b3`, Linux v4.32.0-rc1 archive URL. Fresh local archive hash agrees.

`lean_fast_transport_result.json`: `status=FAILED`, `chunks=[]`, `preserved_interrupted_upload_bytes=61964288`, `error.type=TimeoutError`, `error.detail=bounded upload elapsed`. `lean_setup_execution.json`: old setup command under timeout 600s exited 124 with no stdout/stderr.

Latest inspected Linux preflight `tmp/d7_global_critical_20261027/preflight.json`: `lean_on_path=null`, `lean_bin_candidates=[]`; inventory lists only interrupted archive/chunk files. The archive downloaded locally is not evidence of completed Linux upload, extraction, deployment, or compilation. No successful Lean primitive compilation receipt was found among the inspected artifacts.

## Old D7 finite searches

`tmp/d7_global_critical_20261027/decision_result.json`: `schema=D7_order30_single_decision_result_v1`, `n=30`, `variables=24965`, `clauses=387004`, `no_extra_criticality_or_template=true`, `status=TIMEOUT_UNDECIDED`; exactly one allowed invocation. Command uses default Linux Kissat with `--time=300`; exit -9, `timed_out=false`, elapsed 300.0054334389861 seconds. Keep those raw fields as recorded, including the false timeout flag. `theorem_credit=false`, `independent_review=false`, `production_accepted=false`. CNF SHA `b59fea8b3b300555e695da8e77620db5ee739df8f20d9d844f3e5f69f5f9ebac`. Fresh local result SHA `085d9516ea4013b5f63f4eb0908b9402548749c7cdf1dd58fa7282325fb599ad`.

`tmp/d7_tau_critical_20261027/critical18_result.json`: `schema=one_shot_order18_D7_tau5_decision_v1`; binding `complete_D7_order18_exact_all_red6_all_four_deletions_v1`, `n=18`, `variables=23167`, `clauses=436338`, `H6_flags=18564`, `four_deletion_clauses=3060`, `all_positive_flags_exact=true`, `no_endpoint_or_template_assumptions=true`. `status=TIMEOUT_UNDECIDED`, `solver_invocations=1`; Kissat `--time=180`, exit -15, `timed_out=true`, elapsed 180.01252167799976 seconds. `independent_review=false`, `production_acceptance=false`, binding `theorem_credit=false`. Scope: exact order18 target only; no other-order or global upper bound. CNF SHA `9f6b9ee6c0ac0f489b50e11958adc6664ef7f85fc8730f5f4d72a7ccfb1362b5`. Fresh local result SHA `9e4e436d6fc53bd0f1facbf4edee816495691631692ad3af2b4ea715fe0d86ea`.

## Existing access metadata for separately authorized later work

`tmp/d7_tau_critical_20261027/transport.py` imports the established helper `tmp/balanced49_abstract_port_20261026/remote.py`, changing its receipt/output root and Linux target. The helper uses bundled Paramiko from `tmp/c7_transport_dependencies`, SFTP upload/fetch, and explicit SSH commands; it refuses to overwrite local receipt/fetched files. Credentials are read from an existing external connection-info file; this audit did not open it or reveal credentials. No connection was attempted.

Authoritative Python in recorded Linux commands: `/opt/anaconda3/envs/forktqiu3/bin/python3.12`.
Authoritative workspace: `/data/ktqiu_hdd/math_agent`.
Default solver: `/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat`, recorded SHA `c2e44161cd142694f2b612e0be2dcc59cb656df6d42f8713adc4d05b9a22f5fa`.

All later scientific checks must target Linux and require their own explicit bounded scope; this inventory authorizes none.
