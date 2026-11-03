# q8 concrete source closure

The actual driver state is `CHECKPOINT.json`; `DRIVER_HANDLE.json` records its
current PID and every active Lean child. Each child has a 60 CPU hard limit.
Every attempt, including the explicit cost-reassessment barrier, has a separate
log and wait4 CPU receipt under `attempts/`. The 12000 CPU ledger is cumulative.
The preceding two-module pilot is separately recorded in `../formalization_pilot`
and is imported without recompilation.

Final status is `COMPLETE_KERNEL_AUDIT_AND_EXTERNAL_BINDING_PASS`; no resume is
needed after that receipt. The two Inputs use pure core Fin.cases terms. Their
actual compilation costs were26.291560 and34.449886 CPU. The final new
Exact/Audit commands use Lean's `-s65536` thread-stack option after a recorded
native-stack overflow; the60 CPU hard limit did not change. A missing tactic
import, its stalled cached import, the stack failure and a graph-alias instance
error remain in the failed-attempt history. Final graph aliases are transparent
abbreviations of the original concrete graphs, and final Audit contains no
sorryAx.

Run from the repository root using the existing pinned environment:

```
python3 research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/formalization_full/driver.py --resume --workers 8
```

Resume only after checking that the recorded prior driver is terminal and there
are no unreconciled active children. The driver refuses another active driver or
unreconciled child handles. `STOP_REQUEST` requests a clean drain at the next
loop; remove it before an intentional continuation. `--take 1 --workers 1`
limits a diagnostic continuation to one new attempt. Successful new modules are
not recompiled. The explicit LEAN_PATH is read from the existing
`research/ddp/refresh_20261029/f5_full_d20_D3/FORMAL_ENV_COMMAND.json`; no lake,
fetch, installation or old dependency build occurs.

Encoding and finite scope:

- Pilot: Derived point511/all640 lines; Balanced point584/all585 lines; the
  respective final line and spread certificates are reused.
- Full leaves: remaining1095 rows/668680 pairs. The initial47 successful new
  rows keep their original witness NatTable representation. The rest use the
  same witness words in base4194304 blocks of32, reducing declaration cost.
- New hline certificates check all10368 remaining line positions, and howner
  certificates all1080 remaining spread positions. Their bridge proofs reuse
  the pilot boundary certificates.
- Per-case Inputs assemble every point row. Exact applies the previously
  compiled Walk-based generic theorem, with all finite premises now proved.
- Standalone Audit imports the final module and prints each original graph,
  explicit Fin label, FinalClaim, theorem body and axioms.

`EXTERNAL_TABLE_BINDING.json` decodes actual Lean literal trees and compares them
to the physical small incidence tables and independently validated ordered
helper-pin rows. It reads no large graph and asserts no Lean ASCII parser
theorem. The independent full literal graph validation and129 actual helper
BFS runs remain in `../independent_acceptance/`; no such work is repeated here.

The original targets concern order, maximum degree and genuine Walk diameter
exactly3. Full regularity equality was externally checked, but is not asserted
by the current generic Lean interface. Located public-source gains are64 and65;
exact spread-fill priority and global priority remain unknown.
