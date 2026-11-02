# Static review of the canonical inversion-orbit cover model

Verdict: no blocking issue found in the actual run.py. This was a read-only implementation review; no ball, solver, graph or BFS was executed here.

The expanded cardinality input list retains each cost-one selector once and each cost-two selector twice. The counter allocates distinct auxiliary variables for every position and threshold1..16. Its clauses propagate previous prefix counts, force threshold1 when the current input is true, and increment each prior threshold for a true input. The final negative threshold16 clause enforces at most15 positions. A repeated selector therefore contributes two. Initially unconstrained higher thresholds cause no unsoundness: valid inputs extend by assigning the true prefix-count predicates, while a count of16 forces the final threshold by induction.

Each group's actual port ball is the union of its one or two cached R3/R4 balls. Per-target selector supports are ORed in uint64 and there are fewer than64 groups in either model. Equal target-support rows are deduplicated without losing constraints. The complete nonzero support assertion binds every old target.

Groups are checked globally disjoint by comparing the distinct port count with total costs. Selected SAT groups are expanded to actual pins; the code again checks uniqueness, cardinality=sumweights<=15, all target clauses and the explicit union of selected cached balls equal to the complete n-bit target mask. Port eligibility is inherited from membership in the existing eligible-port ball caches: every wanted pin must be present. Actual source/cache provenance is inherited rather than revalidated by this static review.

With the retained-edge extension lemma, a fully decoded/cache-verified neighbor set gives the required new-root distance bound. The code deliberately reports a literal candidate rather than claiming an exported/newly independently accepted graph. This review does not independently check any solver UNSAT proof or establish a bound outside the stated canonical48/60-group family.

The per-source single CaDiCaL call, requested five-second limit and OS CPU7/8 guard are explicit. No second solver, changed seed or model is introduced by this review.
