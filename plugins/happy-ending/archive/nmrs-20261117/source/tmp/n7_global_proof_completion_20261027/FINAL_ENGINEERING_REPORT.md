# Final isolated P0 engineering evidence

2026-10-27. Requested native executor: gpt-6.1-sol/high; this is not an independent backend/effort attestation. Engineering PASS does not establish independent mathematical review or acceptance. All scientific/checker execution was on authoritative Linux under the new root `/data/ktqiu_hdd/math_agent/tmp/n7_global_proof_completion_20261027/`. Only this new root and its local counterpart were written.

## Completed Joint17 certificate edge

The full local source was uploaded once (38,734,663 bytes), then verified against SHA256 `22950a14595f72b93a769261738d029b2aa27d04aa27e1f44fa2dce77775da2a`. No old interrupted prefix was treated as complete. The isolated checker binary, checker source and extraction parser matched their fixed input hashes. Source/checker hashes remained unchanged after execution.

The extracted CNF has 1,430,689 bytes and exactly 59,479 source rows. SHA256 `9a70c9ce1aa47c1a7127a3393a8159c7276c371fb523161b38e838feb6e0b467` equals the earlier complete schema/formula binding. The extracted proof has 37,141,401 bytes, 102,563 rows, and SHA256 `967f022d44e230bddff7b1234e93d7bde718230841d03100f0d6fed1b2506e0b`.

The original seven checker controls completed: the valid empty-conclusion fixture was accepted; no-conflict, missing-prior-hint, nonunit-hint, satisfied-hint, hints-after-conflict and blank-source-row fixtures were rejected. One complete strict-RUP invocation then exited 0 and checked the final empty clause. Raw checker stdout:

```json
{"status":"PASS","variables":91738,"source_clauses":59479,"additions":102563,"strict_hints":5166479,"seconds":0.420317}
```

Controller-measured checker time was 0.469515 seconds; the Linux source/extraction/control/full-check driver took 1.270027 seconds, under the 240-second outer / 180-second checker / 4-GiB limits. Total SSH/upload/check/fetch envelope took 127.109 seconds. Input `source_upload_wall_seconds=600`; only one complete upload and one full-proof invocation occurred. The seven controls are separately counted, rather than hidden as additional full-proof attempts.

Primary evidence: `joint17/result.json`, `joint17/checker.stdout`, `joint17/checker.stderr`, `joint17/transport_receipt.json`. Result SHA256: `d5f21ece0e607b384fd30dc18d6035612e61beec995293306ad259a4a7d05be7`.

## Completed Closure fixed-rule/control repair

The new validator retains the old all-row Valid and symbolic dictionary checks. It completed all 190,932 fixed rows and all 12 negative controls in 8.693406 seconds, under 120 seconds / 3 GiB. Eleven negative fixtures mutate actual fixed rows. Because sourceAttain has no actual row, one separately marked synthetic complete-successor fixture first passed Valid; removing one required successor was then rejected. This synthetic test grants no actual-row or formula-binding credit.

Absent schema constructors are explicit zeroes: core.sourceForward=0, core.sourceAttain=0, counting.internalBound=0 (low.impossible is also explicit). The old FAIL and its original validator remain unchanged; their copied originals are in `closure/` for comparison. The successful new result does not retroactively change the old failure status.

Primary evidence: `closure/result.json`, `closure/REPORT.md`, `closure/transport_receipt.json`, `closure/original_failure.json`, and the Linux `closure/mapped_rule_rows.jsonl`. Result SHA256: `3f9ad9ef8683473f96020c16ae94469615b166b0486f8fcaedf47c9f8e3dbe81`; exact mapped-row SHA256: `0ad49d462a9c48a45c8ec4fedd95e678e4d69d7335983cedb27251daa776e238`.

## Closure acquisition stopped for budget feasibility

Main separately authorized one fixed ZIP-member Range acquisition, then ordered an early controlled stop because the measured rate could not finish the member within the fixed 900-second budget. The original last checkpoint records 3,145,820 received bytes, 15,799,377 uncompressed bytes and 297.187266 seconds. It retains `status=STARTED` / `stage=ES7ClosureLiteral.lean:stream_download_decompress_hash`; it is progress, not a final acquisition result.

The controlled stop identified only the exact new acquisition Python command, sent SIGTERM to PID 385947 and confirmed no matching owned process remained. Its 15,799,377-byte `.unverified.part` was preserved. Complete `ES7ClosureLiteral.lean`, `closure.cnf` and `closure.rup` do not exist. Full manifest SHA/CRC was not verified. No actual-CNF binding or Closure proof checker was dispatched. Prepared binding code/specification remains unexecuted.

The derived control verdict is **ABORTED_BUDGET_FEASIBILITY**, with original pre/post progress snapshots preserved separately. `TRANSPORT_COMPLETE` in the acquisition SSH envelope refers only to returning the process status and fetching its partial receipt; it does not mean source acquisition completed. No retry, extension, second member transfer or whole-archive download occurred.

Primary evidence: `closure_acquisition/abort_receipt.json`, `acquisition_progress_before_abort.json`, `acquisition_progress_after_abort.json`, `transport_receipt.json`, and `abort_transport_receipt.json`. Abort-receipt SHA256: `66cdec8e9b98db3fac72a9a7f9dd43db9766e35ed3d0e8341c1df38e0e8e0177`.

## Preserved boundaries

The initial local connection-fragment NameError and subsequent sandbox socket denial preceded any remote directory/upload/scientific dispatch. Their receipts remain separate; main explicitly authorized the local repair and first actual connection. No scientific invocation was retried.

Seven protected local source/receipt paths match their initial SHA256 values. No existing task/index/stage summary, history, source, proof, CNF, acceptance, running job or pointer was changed. There were zero SAT solver calls, zero Lean installations/compilations, no Claude review, no commit and no archive. Main owns all mathematical consequences and any subsequent source acquisition or proof-check budget decision.
