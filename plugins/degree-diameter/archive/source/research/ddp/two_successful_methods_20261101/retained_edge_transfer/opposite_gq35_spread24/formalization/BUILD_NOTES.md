# Build and representation notes

Use the original project `formal/`, pinned Lean4.24 and cached imports. The local
compile.py reads saved FORMAL_ENV_COMMAND.json's LEAN_PATH and invokes the
pinned binary directly with-j1. It never invokes lake, installs, fetches or hashes.

Existing old F4/source/clone modules are read only and not rebuilt. Only new
OppositeGQ35Spread*.lean modules are owned here. Generic/Definitions compile
before the finite tables; FastTables→InputData/Incidence→InputChecks→64Rows→Inputs;
Walks/Slots/LowerGeneric are separate compiled generic arguments. Final callers:
Inputs→Degree,Diameter→Lower→Exact→independent Audit import.

A new directory replay with existing cached dependencies uses those source
imports and that order. The row modules can run independently after InputChecks.
Current successful row bodies00/63 use the original indexed projection row;
01..62 additionally prove `projectionData p = localProjectionDataXX` by rfl
before the check. These are equal evaluation layouts, not alternate graphs.
All64 row results are required; neither a representative nor an unproved
finite-data premise is passed to the final theorem.

Observed finite performance led to representation repairs: flat6144-witness
array hit recursion depth; nested witness rows compiled but cost23CPU/row;
768 actual-table equalities plus positive-incidence proofs and3 explicit
incidence indices reduced representative rows to6–8CPU. Old attempts/logs are
preserved. No successful unchanged source was rebuilt simply to get a cleaner
receipt. Root revised the same total1200CPU to750finite+450generic and allowed
3-j1 workers after row00/63 measurements. Batch has115CPU/module hard limits,
aggregate750finite monitoring and first-failure stop dispatch/no automatic retry.

The current harness subtracts child rusage at entry from its exit reading.
An earlier Slots result inherited previous shell children's CPU and overreports
its own cost. It is retained conservatively in the total instead of rebuilding
that unchanged module. This timing issue does not change any Lean proof result.

`check_binding.py` directly reads original literal arrays back from Lean source,
checks16 ordered pin lists/new labels and compares the formula's73920 edges
with the original edge table. It does no distance traversal. This external
binding plus existing independent acceptance is not an ASCII-parser theorem.
