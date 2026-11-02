# Cyclic28 source with joint right factor: bounded58 completion

2026-10-18. HISTORICAL PLAN, FORMAL COMPUTATION CANCELLED. A complete paper obstruction in CYCLIC28_COMPLETION_OBSTRUCTION.md now excludes this source and all six-set cyclic sources covering left far pairs. No production input or solver ran. Only unused, unexecuted encode.py exists; see IMPLEMENTATION_PAUSED.md. The direction was actually accepted before the new obstruction was found. The new proof has its own actual SCOPED ACCEPT in reviews/dd82/20261018_cyclic28_completion_obstruction_review.json. Original proposed scope and budget remain below for provenance.

## Mathematical source and actual change

Use the hand-proved six-set A={0,3,6,10,14,19} in Z28 from ../nonuniform58_run/CYCLIC28_SIX_SET_FRONT.md. C0(i,j)=1 iff i-j belongs to A. Its28 rows and28 columns all have degree6; every left C28 far pair has a common column, while circle-distance1/2 pairs do not. This28-column source is not a graph solving58.

The previous affine front, all its arbitrary three-row additions, and the precisely independent one-trade-per-special repair are impossible. The new source has different intersection geometry and no designated25-row affine core/three special rows. Its degree and cover obligations must still be realized jointly after two columns are added.

The old complete input fixed both C28 and C30 with all crossbits free. Here left C28 remains induced, old cross support is constrained by the explicit source, and the entire right2factor is free, including every cycle decomposition. The graph's right order cannot be normalized to C30 while keeping source columns fixed. This is a structural change, not an extra seed or longer solve of the previous input.

## Exact family

Left L=Z28, right R={0,...,29}; whole graph has58vertices. Left induced graph is exactly C28.

- Old crossbits i,j with j<28 are free only if i-j mod28 lies in A; all other old crossbits are absent. There are168 allowed old bits, so the source may lose edges but not gain other old incidences.
- Both new columns28,29 have all56 crossbits free.
- Right base factor F is a free simple2regular graph on all30vertices; all435possible undirected edges free.
- Right matching M has all435possible edges free, degree at most1 per vertex and is edge-disjoint from F. The actual right adjacency is exactly F union M.
- Every left cross row has6edges. At each right vertex, cross degree plus matching degree equals6. These imply total graph degree8, exactly6matching edges,12crossdegree5columns and18crossdegree6columns. May enforce the redundant total6 explicitly, but no additional restriction.
- Each old column consequently loses zero or one of its original6incidences. The new columns have5or6neighbors each, so a total10to12old incidences are removed. Their supports may overlap; a left row may lose two old edges. Do NOT impose disjoint new supports, fixed new-column degree5, prescribed matching endpoints, fixed F cycle type, cyclic symmetry of the finished graph, P=I, or special row q bounds.
- Every one of the1653actual unordered vertex pairs must be adjacent or have an actual common neighbor in the SAME graph. Include all real F/M paths using actual right adjacency. No partial left-only screening accepted as target.

A successful model is a58vertex232edge8regular diameter2 graph and must be decoded to an explicit edge list and independently BFS-checked. F may be disconnected, but the complete graph must meet the actual diameter requirement. The family is restricted by C0 and the left/right decomposition, not all58graphs.

## One bounded discovery profile

Reuse generic CNF primitives, degree counters, full-assignment semantic checking and bounded process runner. Write new source-specific builder; do not edit old inputs/results. Before production, require exact small assignment semantics including positive and negative cases where available, actual right-union semantics, and fresh gpt-6-astra/xhigh source review (same-family provisional). Direct graph checks must include original degree/distance semantics, not just compare two encoders.

Only one formal input and one solver invocation. No proof logging. Budget30CPU/45wall seconds, one CPU,4GiBaddress space,256MiBper file; use existing solver with normal soft28 stop if supported. Preparation/checks measured separately. No A-list, right-cycle template, seed, added-column-degree, trade-count or time ladder. If a decisive paper obstruction appears before production, cancel the run rather than compute the ruled-out source.

SAT requires saved explicit graph and independent acceptance. UNSAT without proof remains RAW for this precise input; no automatic certification. UNKNOWN leaves this exact completion family open and supplies no candidate. Next action must use actual evidence, not assume a short profile exhausted the source.

## Workflow

Existing nonuniform58 paper mechanism has three completed review rounds; final same-thread review will check the new trade theorem and this concrete next direction. New completion stage is separately tracked because its source and right-factor variables change. Keep the same reviewer memory and report actual metadata, without treating an old direction receipt as review of unrun code/results. No old61SAT, oldLean, newGeminiCLI or hashes. HTML remains research/progress.html; hourly reporting is not a hypothesis quota.

