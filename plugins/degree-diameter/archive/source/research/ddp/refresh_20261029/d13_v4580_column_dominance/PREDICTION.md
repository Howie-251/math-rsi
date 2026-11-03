# Frozen strict column-dominance gate

2026-10-29, before this mask-containment calculation.

Fixed input: current51457/v4580 prepared masks from `../d13_v4580_fourguard/prepared.json` and `prepared.masks.u64.bin`, containing2755 target rows and13057 unique nonzero currently legal guard columns. All2755 targets and the guard budget≤4 remain unchanged.

Old-scope check: the original `singlefault_star_probe/cover.cpp` uses a map keyed by the complete mask to deduplicate equal columns only. The v4580 prepare/SAT and fractional-gate code retains all13057 representatives. The later route-block work deduplicates masks on a different sufficient block criterion, not strict containment of these complete2755-target masks. No completed exact strict-subset column-dominance pass was found for this scope.

Prediction: deleting proper-subset columns may materially reduce the unchanged full-target cover model. Its size effect is unknown before this run; no feasibility prediction or permission to restart the old solver follows.

Sort columns by descending exact popcount, with original zero-based column ID breaking ties. For each column, test whether a previously retained column is an exact proper superset. Delete it only with such a witness. Higher-popcount-first processing ensures the witness remains retained. Equal-popcount distinct masks cannot strictly dominate each other. Save retained/removed original column IDs, original guard labels, and one retained strict-superset witness for every drop; recheck every witnessed inclusion against the input masks before reporting completion.

Correctness: all guards have unit selection cost, are currently free, and there are no mutual-exclusion constraints. Replacing a selected dominated guard by its dominating guard preserves every target already covered and does not increase cardinality. If that dominator was already selected, simply delete the dominated guard. Thus the reduced columns preserve existence of a≤4 full cover in both directions. This does not transfer to models with unequal costs or additional conflicts.

One worker,≤5CPU seconds including compilation/preparation; no graph/ball read, new target, SAT/LP/MIP, random proposal, or parameter ladder. If a CPU guard interrupts the pass, preserve the actual cursor and do not claim a complete reduced model. If the completed reduction is negligible, stop; any subsequent solver decision belongs to root.
