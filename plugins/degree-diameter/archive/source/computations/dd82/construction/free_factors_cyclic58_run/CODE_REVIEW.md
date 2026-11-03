# Fresh code review: PASS

2026-10-18. **PASS; no blocking or non-blocking correctness defect found in the reviewed implementation.** This is the fresh same-family review requested by the project-local ARIS `experiment-bridge` workflow, dispatched as gpt-6-astra/xhigh. The reviewer did not author this production code. The result is provisional code assurance, separate from the mathematical direction review, production execution and any result acceptance.

Reviewed `PLAN.md`, `MATH_SCOPE.md`, `SCOPE.md`, `encode.py`, `runner.py`, the actual small JSON/CNF artifacts, and directly used generic CNF/assignment/process/BFS helpers. Read project `AGENTS.md` and the latest human research comments. Verification was limited to the stated family and existing small evidence; no formal preparation, solver, old experiment, hash, manifest or Lean task was run.

## Family and encoding

The implementation matches the intended 28+30 family. All 378 left edges are primary choices, constrained only to a simple 2-factor. The 435 right-factor and 435 right-matching choices are free; exact factor degree 2, matching degree at most 1 and edge-disjointness implement the intended right layers. `R ↔ (F ∨ M)` is a genuine union, used throughout the actual right adjacency.

The old cross mask is exactly `(i-j) mod 28 ∈ {0,3,6,10,14,19}` with 168 deletable incidences, and both new columns supply 56 free bits. Cross rows have degree 6; each right cross degree plus matching degree is 6. Summing these equations gives six matching edges, so their explicit total constraint is redundant and valid. The 1472 primary-variable count is correct. New-column overlap and two old deletions in one row are permitted. There is no imposed circle order, connectedness, cycle decomposition, prescribed matching endpoint set, completed-graph symmetry or `P=I` normalization.

The coverage loop visits all 1653 unordered actual pairs and every possible middle vertex, omitting only paths containing fixed source nonedges. Each remaining path is a two-way conjunction of actual graph edges. Free H edges occur in left-left and cross-side paths; all right-side paths use R, including paths with two right-internal edges. In particular, the implementation does not assume that all right nonedges require cross-side common neighbors. No pending private-pair observation has been added as a cut.

The generic exact-count helper uses the correct two-way threshold recurrence; its final threshold units enforce exact degree, and the matching counters enforce degree at most 1. The complete-assignment evaluator determines auxiliaries from their defining clauses and subsequently evaluates all complete clauses again. The actual graph checker reconstructs edges as sets and uses graph degrees plus all-source BFS.

## Actual finite checks by this reviewer

A separate read-only check imported only the current 4+6 and 6+8 builders and read the saved artifacts. The actual saved CNFs equal their current generated clause lists directly: 655 variables / 2041 clauses and 1382 variables / 4340 clauses. No formal 28+30 builder was called.

All 12 saved complete assignments were independently decoded through those maps into H, F, M and C. Their saved edge lists agreed exactly. Direct degree and scope predicates, all-source BFS distances, every union auxiliary, every path auxiliary, and every actual saved clause agreed with the recorded results. The possible path index sets were also checked against the complete actual-edge domain, including the old-source mask. All 8 AND and 8 OR truth assignments passed. This additional read-only check took about 0.030 CPU seconds.

The four positive small graphs pass. They include a noncanonical left circle and overlapping new supports. The degree-valid altered-cross graph has exactly one bad pair and one failed coverage clause. The disconnected left two-factor has valid structural degrees and exactly 25 bad pairs, corresponding to exactly 25 failed coverage clauses; no spurious connectedness restriction rejects it. The overlapping F/M case uses the correct actual union and fails the two required disjointness clauses, in addition to its eight actual uncovered pairs. The shared-endpoint matching case retains its real two-matching-edge path while failing the proper degree restrictions. Degree perturbations fail the corresponding degree counters. These are finite semantic checks, not a small-domain exhaustive proof or evidence of an order-58 target.

## Saving, decoding and execution

Source inspection confirms that the official variable-map serialization and decode arithmetic agree: H starts at 1, F at 379, M at 814, allowed cross incidences at 1249, and R at 1473. Decode checks the saved complete DIMACS model before recovering the same H/F/M/C adjacency, retains both factor cycle decompositions and then saves the expanded graph. The runner invokes the independent graph verifier on that saved graph and checks 58 vertices, 232 edges, degree 8 and no BFS bad pair before reporting a verified target. The production decode path has not yet been executed; its review here is source-level, supplemented by the actual small saved-assignment reconstruction above.

The runner imports only the generic bounded-process function from the old runner; it does not call an old model or overwrite old run results. Its unique launch record and prior-output checks prevent a normal second invocation. The sole solver command has soft limit 28 seconds, hard CPU/wall limits 30/45 seconds, one CPU, 4 GiB address space and 256 MiB per file, with no proof argument or restart. Preparation, decode and independent BFS have separately recorded limits. RAW UNSAT and UNKNOWN remain correctly distinguished from an exclusion.

No patch or additional test batch is requested. This PASS permits root to consider the already scoped one-shot execution, subject to the continuing mathematical check that no decisive obstruction has appeared. It does not itself launch that execution, accept a candidate, certify UNSAT or establish feasibility of the family.
