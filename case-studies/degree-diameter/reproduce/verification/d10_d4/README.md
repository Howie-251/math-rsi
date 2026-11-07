# Preserved verification records

The ten `n*_ALL_ROOTS.json` files are unmodified copies of the accepted graphs'
historical `independent_audit/RESULT.json` summaries. Each reports a complete
ordinary BFS from every vertex of the literal graph, including old–old pairs.
These are preserved results, not new publication-run computations.

`n2558_LEAN_FORMAL_RESULT.json` records the unconditional concrete claim on
`Fin 2558`, its final kernel build and audit import. The independent original
existence-statement import is separately recorded in
`n2558_LEAN_INDEPENDENT_IMPORT.json`.

`n2567_LEAN_FINAL_ASSEMBLY.json` records successful builds of `Final2567` and
`Final2567Audit`, with the original target complete. The associated
`n2567_ROOT_GRAPH_RELEASE.json` records the exact five-cut construction, full
independent graph check, final original-target theorem and its independent
import. It also records the distinct mathematical and external formal review
states. `n2567_FORMAL_C_DISPOSITION.md` preserves the incomplete final C review
and its actual scope.

Original source paths and build commands inside these records describe the
research workspace at the time of verification. The complete Lean sources,
dependency graph and build cache are not bundled. These receipts support an
accurate account of completed work; they are not a standalone Lean project.
The eight intermediate orders 2559–2566 remain without separately completed
concrete-graph Lean entries in the catalogue.

The separate `../D10_D4_SOURCE_REPLAY.json` records this publication run's
finite reconstruction and full unordered edge-set comparisons only. No
distance check, solver, search or formal proof was rerun.
