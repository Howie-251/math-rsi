# External checking of the saved connected-D1 UNSAT proofs

Both saved binary LRAT certificates passed official lrat-trim 0.2.0:

| Case | Exit/status | Clauses checked | Wall seconds | CPU seconds | Peak RSS KiB |
|---|---|---:|---:|---:|---:|
| b=28 | 20 / VERIFIED | 1,344,762 | 1.106 | 1.000 | 247,276 |
| b=41 | 20 / VERIFIED | 1,463,908 | 1.459 | 1.294 | 276,764 |

Driver: `computations/dd82/n62/check_d1_connected_certificates.py`.
Official release source, version record, build logs and upstream test output:
`.tools/dd82-lrat-check/`. Both checks used:

    .tools/dd82-lrat-check/lrat-trim-rel-0.2.0/lrat-trim --no-trim <saved.cnf> <saved.bounded120.lrat>

Full commands and exact resource measurements are in `results.json` and the
per-case JSON/log files. The checker parsed the two formula headers as
444,839 variables and respectively 1,633,418 / 1,633,419 clauses. It checked
all added proof clauses, in the backward mode reported by release0.2.0.
Both checks read the original saved binary traces directly; neither proof
nor input CNF was modified. No solver reruns occurred.

The wrapper initially tried `/usr/bin/time`, which is absent. This failed
before any checker started; that launch record is retained separately.
The wrapper then used standard-library `os.wait4` to collect resource use.
Each actual checker ran exactly once on pinned CPU0, with 120-second CPU and
wall limits, four-GiB address-space limit and 512-MiB output-file limit.

These results establish externally checked UNSAT for the two saved CNFs.
They are not Lean-kernel certificate checks. The complete original-graph-to-CNF
bridge remains missing, and no arbitrary order62 exclusion is asserted here.
The old solver reports retain their historically accurate RAW status; the
new checker reports separately record `proof_checked=true`.
