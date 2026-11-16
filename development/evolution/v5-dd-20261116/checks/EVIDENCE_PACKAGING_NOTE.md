# Evidence packaging note

Historical REPORT.md, RUNS.json, INDEPENDENT_RESULT.json and WORKFLOW_TOOL_AUDIT.md retain their original execution scope, commands, timing and intake provenance. Source archive paths relative to the original package can now be found under `plugins/degree-diameter/archive/dd-latest-two-parameters-20261116/` at repository root. Original intake absolute paths are historical command records, not runtime dependencies for the portable tools.

The original `verified/CHECK_RESULT.json` is packaged here as `GRAPH_CHECK_RESULT.json`; REPORT.md's artifact reference uses that packaged name. Original stdout/stderr logs are beside it. Generated graph duplicates and compiler products are intentionally omitted: reconstruct them from the archived source. Original copied `workflow_smoke.py` is historical test provenance with intake paths, not the portable maintained regression command; use `workflow_helpers_test.py` and WORKFLOW_HELPERS_REPORT.md for the integrated tests. `workflow_copy/` referred to by the historical smoke program was a temporary copied layout of the four source helpers; the unchanged originals remain in the archive's framework_snapshot and maintained variants in base/tools plus plugins/degree-diameter/tools.

`independent_check.py` retains the original arithmetic and structural checks; only its path selection became required explicit --archive/--reconstructed/--output arguments. A portability-only rerun used the integration archive plus the already reconstructed original graphs, and wrote an external intake JSON path before copying its separate result here as INDEPENDENT_PORTABILITY_RESULT.json. Exit0; measured process CPU 1.590843s. Original INDEPENDENT_RESULT.json and its timing were not overwritten. The associated captured stdout is independent_portability.stdout.json.

Executed from repository root:

```
python3 development/evolution/v5-dd-20261116/checks/independent_check.py --archive plugins/degree-diameter/archive/dd-latest-two-parameters-20261116 --reconstructed /Users/rfy_naiveai/Desktop/aris4math/context/dd-latest-20261116/checks/reconstructed --output /Users/rfy_naiveai/Desktop/aris4math/context/dd-latest-20261116/checks/INDEPENDENT_PORTABILITY_RESULT.json
```

To replay on another machine, first run the archive's reproduce.py --compare with an explicit external --output-dir; pass that generated directory to --reconstructed and another external JSON destination to --output. No graph BFS, search or Lean is performed by this independent checker.
