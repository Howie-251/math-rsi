# Actual final receipts and bounded reproduction

`FINAL.json` and each graph directory's formalization/FINAL.json contain the two
actual k1 target receipts. `CHECKPOINT_B/C.json` also points to the separately
budgeted83 receipt. All current HANDLE/CHECKPOINT/STAGE_STATE records are
terminal with no active child. No further compilation is needed locally.

`compile.py ModuleName` uses the pinned existing Lean4.24.0 executable, explicit
LEAN_PATH from the inherited FORMAL_ENV_COMMAND.json, -j1/-s65536 and a60 CPU
hard limit. It never invokes lake or rebuilds imported modules. Every failed
attempt is retained, successful modules are refused on repeated invocation,
and the cumulative600 CPU ledger is not reset. The separate83 compiler has its
own150 CPU ledger. No hash or checksum is generated.

New sources are the five DiagonalFillReallocation generic modules and four
Q4DiagonalFill/four Q8DiagonalFill modules, including standalone Audits. The
new-role83 sources are four Q8DiagonalFill83 modules. All old source, finite
geometry, projection, field, ovoid and generic modules remain unchanged and
were imported only. `generate_cases.py` preserves the successful dependency
shape: q8 Definitions imports only old data/ovoid Definitions; concrete source
Exact is delayed until the new Exact. Its graph alias is transparent and the
source card proof is reused. The actual q8 source retains harmless static
stderr progress markers used for the one performance diagnosis.

The external bind scripts read only already accepted small tables and ordered
independent clone-label recipes. They assert no formal ASCII graph parser.
The producer and independent whole graph/BFS tasks have separate receipts;
none were rerun in this formalization batch. The only new kernel finite checks
are670 point-to-owner membership witnesses and670 line-two-point inequalities.

No future k, graph, public record or resolved priority is implied by these
three fixed local Lean targets. Reviews and authoritative counts belong to root.
