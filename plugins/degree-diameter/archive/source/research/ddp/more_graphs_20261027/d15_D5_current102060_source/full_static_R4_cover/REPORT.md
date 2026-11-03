# Complete102060-target static R4 cover: UNKNOWN, no MIP return

The first complete static model was built for all102060 actual current targets and all810 degree14 eligible pins. It has102061 rows including cardinality<=15, with19735110 cover nonzeros and19735920 total nonzeros. Its CSC arrays occupy236834284 bytes in memory. Preparation took0.8175429999999999 CPU seconds; no known row/column deduplication, source BFS or R4-ball computation was repeated.

This differs from the old10CPU constraint-generation experiment: that earlier model ended at751target rows and its intermediate15-pin selection missed3510actual targets. Neither that partial result nor an LP could be accepted as a complete graph. The present variant constructs every row once, in fixed input order, with no samples, CG loop, seed change or reencoding.

## Binding and full model

The existing current-source cache is ../monotone_R4_cover/. Its810 rows of radius4.u64le.bin are indexed by eligible.txt and have1595 little-endian uint64words; bits are actual vertex IDs. The corresponding target_rows file has102060 rows of13words with bits indexed by eligible column. The same source CSR has102060vertices and1530090arcs; all810 eligible degrees are14. The scout's CACHE_INTERFACE_REVIEW and CODE_REVIEW describe the binding without running another model or ball traversal.

For each eligible column, this run unpacked the full cached ball, inserted every real target bit into its CSC column, and appended the cardinality row. Actual row counts were checked against the cached support array70..309. No target was omitted. Persistent full_csc_indices.i32le.bin and full_csc_indptr.i32le.bin preserve the complete sparsity pattern; MIP values are allone, target lower bounds areone, and the final row has upper bound15. MODEL_DIMENSIONS.json gives all paths and dimensions.

## Actual solver receipt

There was exactly one full LP and one full MIP attempt, with one worker/thread. The full LP returned raw status1, time limit, no fractional objective; its call used24.083450000000003CPU seconds, including interface setup. Its configured limit was20seconds. The complete MIP was then called once with70.91655seconds configured. It never returned a solver status or an incumbent.

The worker exited−9 with observed child CPU128.085535seconds, at its configured128CPU hard limit. Driver plus child CPU was128.11086108799998, below the130aggregate budget. The last live stage was FULL_MIP_RUNNING; all live handles and checkpoints are now explicitly terminal. There is no accessible integer selection, graph, new-root BFS, or new lower bound.

The95solver sub-budget had no separate external CPU deadline in this executed harness. Configured solver limits summed to90.91655seconds, but the native-call phase did not stop at those limits: LP-call CPU plus CPU observed after the MIP checkpoint was127.248521000seconds. That includes interface/native work, which cannot be separated further after the killed call. This is an execution gap, not a reason to describe the95sub-budget as respected. BUDGET_COMPLIANCE.json preserves the actual figures. No renewal or second call followed.

## Mathematical disposition

The result is **UNKNOWN** for the fixed current102060source and at most15 free pins. No solver infeasibility status was returned for the MIP, and no strict exclusion follows. In particular the entire complete model remains unresolved; no ordinary graph bad-pair count or exact candidate diameter was measured. Actual_n and actual_D remain null.

A returned integer vector would have required exact binary values, distinct literal pins, actual CSR degrees below15, and the exact OR of the selected complete R4balls over all102060targets. Only then would the retained-edge extension lemma justify102061/maximum15/D5 and graph export. That acceptance phase was never entered.

The executed implementation is worker.executed.py plus run.py. After this run, worker.py received a future-only OS solver-stage deadline correction documented in FUTURE_TIMER_FIX.md; it was neither run nor tested. The execution snapshot and actual receipt are preserved rather than retroactively assigning the new timer to this experiment.

This variant updates the existing monotone-extension family record; it is not a new independent method. Source construction credit remains Dharunish Yugeswardeenoo as in the original source receipts. This experiment contributes no new examples or parameter cells and leaves the previously accepted103 examples intact. Stop this static model at its actual budget: no time renewal, additional LP/MIP, seed or reencoding follows. No global Wiki/HTML/delivery files were modified here.
