# Parallel task-set protocol v2 (2026-09-12)

This supersedes the unsuccessful first parallel migration design. The first
generation stopped before sending any signal because Conda Python lacks
`os.pidfd_open`. Its only result file is `protocol_seal.json`, SHA-256
`5227b6ebccab9c55a7703a194af365c0f25f9b4ff32a059ec1f76247d511fbb6`.
That root and its original controller remain frozen. Neither e9 nor the old
serial runner was stopped by that failed attempt.

## User-authorized five-layer contract

1. e8/e7/e6 each has one controlled external solver and distinct artifacts.
   There are no solver, checker or shell execution deadlines.
2. Ownership is a set of unique tasks, not a canonical completed prefix.
   Completion order is arbitrary; effective rows are sorted by e.
3. One supervisor owns all workers. Audited SAT and operational ERROR trigger
   a single global stop and peer cancellation. Parent-death handling prevents
   live solver children from surviving a lost worker/supervisor.
4. Finalization checks exact coverage, unique ownership, per-cell evidence,
   artifact inventories and frozen predecessors. The independent auditor
   performs fresh predecessor replay, fresh proof checks and byte-equal final
   reconstruction. No C1/N<=34 credit is published before acceptance.
5. One controlled old-run handoff prevents duplicate e8/e7/e6 dispatch. It
   uses tested system-Python pidfds to suspend OS scheduling briefly, terminate
   the old checker, and retire the old scheduler. There is no ptrace, code
   injection, interpreter-memory modification or fabricated exit record.

## e9 handoff policy

The current e9 checker has no committed status. Rather than transferring its
internal state or reconstructing missing metadata, retain its nonempty proof
and old logs and launch one new independent checker under the amended protocol.
This is a proof-check rerun, not a solver rerun. The three requested solvers
and this checker are all supervised together. e10 is inherited from its
original verified status; e1-e5 come from accepted v2 evidence.

## Runtime and output isolation

- New controller: `tmp/c1_parallel_protocol_20260912_v2.py`.
- System-Python handoff helper: `tmp/c1_parallel_handoff_20260912_v2.py`.
- Fresh root: `res/state_charging/20260903_35_state_cardinality_c1_timeout_resolution_v3_parallel_20260912_v2`.
- Original registered v3 runtime and seal bytes are not edited. New workers
  reuse its pure per-case encoder/evidence contracts with a disjoint layout.
- The original serial finalizer/auditor must never be invoked after handoff.
- New controller modes are `prepare`, `handoff`, `run`, `finalize`, `audit`.
  Each stage is create-only and is never retried after production failure.
- The old scheduler lock and naturally produced nonzero shell marker after
  retirement remain historical handoff evidence, not a clean original run.

## Regression findings

The exact pidfd signal-zero operation and disposable-process handoff are
tested on the server's system Python before creating a production root.
The new suite also exercises out-of-order completion, duplicate/missing
tasks, claim ownership, SAT/error global stop, real child cancellation,
retained-proof validation, ten-row final construction and fresh-auditor
accept/reject paths. No production formula is solved by these fixtures.

A cancellation regression exposed reentrant `Popen.wait` locking inside a
signal handler. The handler now only sends signals and raises; it never polls
or waits under the interrupted waitpid lock. Normal unwinding reaps children.
