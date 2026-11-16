# DD deterministic reproduction and bounded audit — 2026-11-16

The supplied portable reconstruction and specified-root verification both passed. Independent parsing and finite-array checks found no discrepancy. This is a bounded computational check with inherited geometric/source premises, not an independent proof of the entire theorem or a new concrete Lean certification.

| Final graph | vertices | edges | maximum degree | complete BFS roots | maximum checked eccentricity |
|---|---:|---:|---:|---:|---:|
| D11 | 37,632 | 205,366 | 11 | 37,471…37,631 inclusive (161) | 5 |
| D12 | 42,433 | 246,309 | 12 | 42,402…42,432 inclusive (31) | 5 |

Both edge lists are simple and exactly equal, as sets with identical vertex counts, to reconstruction from the direct inputs. The independent parser does not import supplied Python code; it additionally compares the reconstructed graphs, computes every degree, and checks all declared rows. Degree distributions are in INDEPENDENT_RESULT.json.

D12 retains the entire 245,937-edge, 42,402-vertex source as an exact induced subgraph. The 31 insertions contribute exactly 372 edges; every insertion's earlier neighbors exactly match its supplied 12 pins. The supplied constructor checks available degree at each insertion, and the independent checker verifies final degrees. All 31 new vertices are BFS roots in the FINAL graph, so every pair with at least one new vertex is covered. Old–old D<=5 remains an inherited accepted-source premise; neither wrapper nor this check proves it afresh.

D11 keeps exactly the source's 1,608 edges touching its 160 old exterior vertices. Its changed core removes 186 source edges and adds 212; the new vertex adds 11 edges (223 total additions relative to the source). Therefore source-edge retention cannot establish D11 core distances. The 161 complete BFS roots cover exactly all pairs touching the 160 old exterior vertices or the new vertex. Core–core distance depends on the actual H9 incidence diameter and the sigma/pi projection theorem. The path conversion stated in PROOF_AND_RESULTS.txt is consistent: a point-to-line odd path of length at most five becomes an undirected graph walk by replacing each intermediate line L by sigma^-1(L); projection pi removes stays without increasing length. This requires actual incidence distance <=6 and the claimed binding, which the wrapper does not establish from scratch.

Additional independent checks on all bundled arrays passed: tau is a permutation, swaps the two parts, has fourth power identity and 728 tau²-fixed entries across both parts; pi covers every one of the 37,471 core labels; all 66,430 lines have ten distinct in-range points; every point is on ten lines; tau reverses every incidence flag; colors are constant on tau² fibers. These checks establish structural consistency, not that an arbitrary such incidence structure has diameter six.

## Inherited premises and original evidence

Paths below are relative to the supplied source package. These original receipts were inspected, not rerun.

- `originals/ar4math/research/ddp/expert15_20261114/d5_resume_20261115/resume_workflow_20261115/h9_exact_binding/build.cpp` and `RESULT.json`: original regeneration from GF(9) coordinates/kernel projective lines, tau order/incidence checks and literal core construction. The result is an earlier TEN-pin candidate with 205,365 edges, explicitly not a final accepted graph. Its geometric/core evidence must be combined with the later final binding; it must not itself be described as final D11 acceptance.
- Same parent directory, `h9_independent_completion/other37632/BINDING.json`: sigma bijection, phi-consistent colors, exact 203,747-edge core, exact 1,608 exterior edges and final pins; explicitly reuses already bound true geometry.
- Same parent, `h9_n37632/independent/RAW_CHECK_RESULT.json`: original final 205,366-edge graph, simple, maximum degree 11, all 161 required roots passing; explicitly requires separately inspected true-sigma binding for core–core pairs.
- Same parent, `h9_cross_finite_binding_20261116/check.cpp` and `RESULT.json`: all 66,430 normalized null points, full projective lines with cross-zero bases, incidence degree 10 and local stars 91; does not itself perform source BFS or regenerate geometry. Universal geometric routing/completeness remains mathematical evidence outside this wrapper.
- D12 source lineage is recorded in `originals/ar4math/research/ddp/more_graphs_20261027/h9_redei15/production/continuation/RESULT.json`. The 31 new-step receipts are the four independent RESULT.json locations explicitly enumerated in PROOF_AND_RESULTS.txt (1+8+8+14). This audit uses the final-graph 31-root cover instead of rerunning the historical prefixes or recertifying the ultimate source.

No use of the 91-line plane candidate-generation argument is needed for final new-root BFS acceptance. That geometric mechanism was not independently recertified here. Concrete H9/Fin37632 and D12 source-D5 Lean assumptions remain open as declared in README; the wrapper's PASS string is conditional on these inherited mathematical/source premises.

## Actual execution

Code inspected before execution: README.txt, PROOF_AND_RESULTS.txt, reproduce.py, verify.py, check_roots.cpp; existing clean reproduction cost was approximately 3.50 seconds wall (receipt: checks/CLEAN_REPRODUCTION_PROCEDURE.json), with specified BFS CPU about 0.215 and 0.057 seconds.

Only scripts, inputs and final graphs were copied to `checks/portable_work/`. Commands ran there:

```
python3 reproduce.py --compare --output-dir /Users/rfy_naiveai/Desktop/aris4math/context/dd-latest-20261116/checks/reconstructed
python3 verify.py --output-dir /Users/rfy_naiveai/Desktop/aris4math/context/dd-latest-20261116/checks/verified
```

TMPDIR pointed to `checks/tmp/`; Python bytecode writing was disabled. Compiler products, generated graphs and receipts therefore stayed in the sole write directory. Both exit codes were zero. RUNS.json records exact arguments and measured process/child CPU: reproduce 1.120 CPU / 1.133 wall seconds; verify 1.993 CPU / 2.889 wall seconds, including compilation and children. The separately executed `python3 checks/independent_check.py` used 1.931 process CPU seconds. Combined substantive compute was about 5.05 CPU seconds, well below the five-minute cap.

Actual logs/results: `reproduce.stdout.json`, `reproduce.stderr.txt`, `verify.stdout.json`, `verify.stderr.txt`, `GRAPH_CHECK_RESULT.json`, `RUNS.json`, `INDEPENDENT_RESULT.json`, `independent.stdout.json`; independent implementation: `independent_check.py`.

No all-root run, Lean build, graph search, external model, source edit, Git operation, or unrelated project write was performed. No discrepancy warrants a further computation in this bounded task.
