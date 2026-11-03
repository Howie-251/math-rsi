# Joint boundary completion on actual order58 and order60 graphs

## Problem and selection

Find a complete simple graph with maximum degree8 and diameter2 at order58 or60. Success is a full independently checked graph, not a lower repair loss. General58–61 and the exact-value goal remain open. This is a construction search with an explicitly frozen outside induced subgraph, not a complete arbitrary-graph decision.

The prior dynamic-weight full60 two-switch loop is closed: it changed many original edges and broke the known original C5 action, but best20/last26 bad pairs remained. The saved order58 deflation graph has21 bad pairs. Read these actual complete edge lists:
- computations/dd82/construction/twin59_to_58_deflation_run/component.path1.edges (58 vertices/232 edges)
- computations/dd82/construction/fullgraph60_weighted_run/candidate.current.edges (60 vertices/240 edges)

A direct read-only bitset count in the present turn gives24 distinct endpoints of21 bad pairs at58 and25 endpoints of26 bad pairs at60. This diagnostic is not a new BFS acceptance or new graph. Both source BFS records already exist. Prior literature method notes motivate replacing the failed component and then testing the full graph; no new literature novelty claim is made. Sources are reused, not regenerated. The order58 source was also considered in old local-switch work; the change here must be judged by the new joint domain, not the seed name.

## Exact domain and purpose

For each saved source G0, let R be ALL endpoints of its actual uncovered unordered pairs, and O=V minus R. Freeze precisely A[O,O] to the actual source values, including both edges and nonedges. Allow EVERY edge with at least one endpoint in R to be independently chosen. No edit-count bound, group action, fixed matching, old fiber internal graph, port assignment, fixed R/O degree split, or nonworsening intermediate path is imposed. All vertices must have degree exactly8 (the accepted general regularity reduction applies above57). Every distinct pair must have an edge or a real common neighbor in this SAME A.

This is one simultaneous boundary completion: every original bad-pair endpoint can change all its neighbors at once, and O vertices can change their entire R interface. It is not another two-switch trajectory or a larger cap on that trajectory. Source A[O,O] is still an artificial restriction, explicitly24/34 or25/35 partition sizes; failure closes at most this anchored domain and UNKNOWN closes nothing. Do not automatically expand R after failure or begin a radius ladder.

## Encoding and bounded experiment

Reuse existing CNF emitter, unary degree counters, CaDiCaL and independent BFS/LRAT tools. Emit one edge Boolean per free pair; constants for O/O entries. Simplify true length-two path products with constants: zero if either edge zero, remaining edge if the other is one, true if both one, otherwise a real AND auxiliary with all equivalence clauses. Coverage clauses are ORs of direct edges and these paths; degree counters include fixed contributions. Count all unordered pairs, while omitting only coverage tautologies with a genuinely fixed path. Do not substitute relaxed B for graph coverage or assume the actual positive-defect conclusions for invalid source graphs.

Before substantive solve, independently review the source and one source assignment sanity: omit just the original bad-pair coverage clauses and require the actual saved graph to satisfy every remaining constraint. Also inspect a directly constructed target on a small graph for the generic helper, without pretending that proves the58/60 domain. Full target inputs will retain ALL coverage obligations. Two bounded single-CPU target profiles, one per structurally distinct order/source; actual caps selected after preparation size. No unchanged restart. SAT gets independent BFS from the decoded full edge list; UNSAT gets exact-input LRAT checking before any anchored exclusion. UNKNOWN and truncated proof traces never certify exclusion.

## Research loop and decisions

Current stage: concrete direction review before solver investment. Gemini existing Antigravity only, requested gemini-3.8-flash-high/high, full raw metadata saved. Same run/thread, max4 substantive reviews. Next actual code/preparation/profile depends on direction critiques; then submit actual code and results to the same thread. No whole-domain theorem, acceleration claim, automatic larger neighborhood, old62–65 work, Lean, score, rendering, hashes or scheduler.

Local parallel exploration of internal double-defect vertices at61 is not part of this mechanism, has no accepted new claim, and will not borrow its reviewer verdict.

## Actual diagnosis during direction review

The new read-only diagnostic fullgraph60_boundary_patch_diagnostic.py/.result.json found that allthree saved60 graphs have a literal induced seven-regular Moore50 graph on the complement of one chosen minimum10-point cover of their bad-pair graph. In particular, the final26-bad graph still contains such a kernel despite the previous loss of its original C5 action. This is newly observed structure, not a claim that prior tests had found it. A minimum-cover patch would freeze that known forbidden kernel. The58 source's minimum8-point cover instead leaves zero-port capacity failures at3,12,45.

The selected ALL-endpoints patches avoid these specific frozen obstructions. At58, R24/O34 leaves84 fixed edges, O port-degree histogram{2:7,3:18,4:9},1092 free edge bits and1230 nonconstant coverage obligations (138 for O/O). At60, R25/O35 leaves94 fixed edges, O port-degree histogram{2:13,3:22},1175 free edge bits and1261 nonconstant coverage obligations (86 for O/O). All O vertices have ports; identified kernel vertices and incident kernel edges are released. This does not prove feasibility or absence of a different fixed-boundary obstruction.

Because every bad-pair endpoint belongs to R, the source already covers every pair with at least one endpoint in O. A joint repair must preserve that coverage while repairing R/R; a count of free variables alone is no existence argument. The full source assignment sanity deliberately retains and reports the21/26 false badpair clauses in the actual target input, rather than solving a relaxed input.

## Actual first preparation and a pending representation improvement

After fresh source review, both actual preparations passed. At58:53169 variables,169580 clauses,1092 primary edges, full1653 pairs accounted for (1230 clauses,423 fixed witnesses). At60:57104 variables,181845 clauses,1175 primary edges, full1770 pairs accounted for (1261 clauses,509 fixed witnesses). Source assignments violate precisely the21/26 original badpair clauses, all of which remain in the target. Each tiny128-assignment check matches independent graph semantics. Actual preparation child CPU0.965312/1.102271 seconds, wall1.016241178/1.116520189 seconds. Two first target profiles were then launched on CPUs1/2,300CPU360wall each; their results are not assumed in this section.

A possible subsequent change is now explicitly derived, not yet encoded or externally reviewed: the arbitrary labels within R contribute an entire symmetric-group redundancy. With O in fixed increasing order, any target has a representative whose R-to-O binary rows are lexicographically nondecreasing. Choose any permutation of R that sorts these rows; relabel ALL its incident edges, including R/R, consistently. Every O/O entry stays fixed, degrees and true pair distances are invariant, and no other label-dependent requirement on R exists. Ties are allowed and internal R/R edges remain unconstrained beyond the original model. Thus at least one representative of every target in the anchored domain survives. This is a choice of labels, not an assertion of a graph automorphism.

For two consecutive R rows x,y, let p0=true and p(k+1) iff p(k) AND (x(k)=y(k)). The exact lex constraint is p(k) implies (NOT x(k) OR y(k)). Only prefixes through the penultimate column need variables. A direct equivalence encoding uses, for k>0, (-q,p),(-q,-x,y),(-q,x,-y),(-p,-x,-y,q),(-p,x,y,q), where q is the next prefix. For the first prefix p=true, omit the first clause and the -p literals. These clauses are exactly q iff p AND (x=y), as checked by its Boolean cases; no implication-only relaxation is intended. The next prefix is unnecessary for the final column.

This would append759 variables/4554 clauses at58 and816 variables/4896 clauses at60 to the unchanged full-input prefix. No computational speedup is claimed in advance. It changes representation without enlarging the artificial anchor; it is a candidate for the actual-result review if the initial inputs remain undecided. It is not permission for an unchanged longer solve or a new run ID. No sorted input has yet been generated or solved.

## Additional necessary local triangle budget (not yet encoded or executed)

A possible stronger propagation constraint keeps the SAME full anchored domain. For any actual degree8 diameter2 target of order n, the already established defect identity gives B=A²+A−7I−J nonnegative, with row sum65−n. For an adjacent pair u,v, B_uv equals its number of common neighbors. Summing these entries over v adjacent to u counts each triangle at u twice. Thus if t(u) is the number of triangles containing u, 2t(u)<=65−n. Every58 target has t(u)<=3 and every60 target has t(u)<=2. This is a direct consequence of inherited Moore/defect counting, not a new claimed mathematical theorem or a triangle-free assumption.

The current CNFs imply this indirectly through exact degrees and allpair coverage, but do not explicitly couple triangle indicators into these small per-vertex upper budgets. An explicit extension could define one exact AND of the actual three edges for each possible triangle (simplifying O/O constants), then count the same triangle indicator once at each of its three vertices and impose the proven upper bound. Every indicator would represent the SAME original A. Such an extension removes no target graph, unlike assuming all triangles absent. It could improve propagation, but no speedup is established.

An actual direct count of the saved source graphs in this turn gives58 triangle-per-vertex histogram{0:44,1:13,2:1} and60 histogram{0:60}; both sources already obey these bounds despite their badpairs. R-only row sorting preserves these counts. Thus the source-sanity contract can still require exactly the original relabelled badpair clauses to fail if this extension is adopted. No new triangle input or solve has occurred. The next actual-result review should decide whether one final bounded substantive representation change is warranted or whether to close the undecided mechanism; do not fill a fourth round merely for the count.


## Current execution checkpoint (2026-10-13 15:00 UTC)

Earlier pending phrases in this chronological note describe their time of writing. Base inputs have both terminated OUTPUT_LIMIT_UNKNOWN; sorted inputs were actually prepared, independently delta-reviewed, accepted by Gemini round2, and solved once each. Both sorted cases terminated UNKNOWN after soft298seconds: n58CPU289.591445/wall298.139517788; n60CPU290.448306/wall298.150858495. No target or anchored exclusion, no LRAT check. Same-thread round3 now reviews actual results and the triangle-budget proposal.

The optional triangle delta is now implemented and explicitly reused-source-reviewed without blockers. Actual preparation completed while round3 was in flight; this is reversible input work after local review, not external acceptance or solver execution. Actual n58:228092variables828328clauses,13424triangleindicators,16334335bytes, preparationCPU2.439641/wall2.518858053. n60:209240variables744101clauses,15150indicators,14394918bytes, preparationCPU2.296622/wall2.368450206. All source extension clauses hold, whole input has exactly original21/26 falsebadpair clauses retained; new24-assignment AND sanity passed. Old graph/lex sanity inherited, not rerun. No triangle solve yet. Large counter growth may offset stronger propagation, so no speedup claim; any final profile retains the existing bounded resource limits and is a changed input within this same mechanism.
