# Final concrete Lean receipt

`FINAL.json` is the actual terminal receipt for d82_346515 and its independent
Audit. `CHECKPOINT.json` retains every measured attempt, including the one
failed alias rewrite; `HANDLE.json` is terminal and has no active child.
The parent source's full batch was already complete before these four new
modules were compiled.

Reproduction uses the existing pinned Lean4.24.0 executable, explicit LEAN_PATH
from the inherited FORMAL_ENV_COMMAND.json, single-module compilation, a60 CPU
hard limit and64MB Lean thread stack. `run.py` imports cached source/generic
oleans and never invokes lake or rebuilds dependencies. It skips modules with
actual successful receipts and keeps one cumulative300 CPU ledger.

The only data binding is `bind_inputs.py`: it decodes the actual new Lean O65,
point-owner and line-owner tables and compares all4225 center/new-label rows to
the independent literal graph receipt. Full N81 lists, complete old-edge
retention, degree histogram, every prefix and all4225 new-root BFS were already
independently checked in `../independent_acceptance/`; none were rerun here.

No further compilation or validation is needed for this local result. External
reviews, any public priority decision and global instance counts belong to root.
