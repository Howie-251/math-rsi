# Actual715 source: P3 correction and cooperative-helper stop

2026-11-01. Status `SUPPORTED_FIXED_PETERSEN10_CLASS_OBSTRUCTION_STOP`.0newgraphs/parameters/Lean. The old source and local structural certificates are inherited; no adjacency parsing, sourceBFS, R2/Steiner recomputation, solver, or candidate graph is run.

## Actual source, not the independent-twin prediction

The actual complete public source is `research/ddp/more_graphs_20261027/d3d4_transfer/source715.implicit_adj.txt`, obtained2026-10-27 from the official [n715d11k3.txt](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD3/n715d11k3.txt). Existing SOURCES.json credits C. Delorme, adjacency V. Pelekhaty, maintained by F. Comellas. Existing RESULT.json/source715 and screen.py document the actual local tests.

The saved literal has715 vertices,3770edges and degrees9:130,10:65,11:520. The195 eligible vertices form65 classes of3, sharing the same8 saturated core neighbors per class. Each class internally is P3: e.g.[0,585,650] has edges0–585 and0–650. Distinct classes have no eligible-old edge between them; each core vertex has all its3 eligible neighbors in one class. Every eligible pin's old closedR2 reaches exactly its own3 eligible class targets, established by all195 saved certificates.

Thus the initial prediction of195 independent degree8 twins is **REFUTED**. Bare full-N copying twice would have3640edges and no internal class edges; the actual file has130 additional internal P3 edges. The center has degree10/spare1, the leaves degree9/spare2 each, total5 free slots per class. These facts are copied from the previous actual structure evidence, not inferred from715=585+2×65.

The source is related to the Delorme585 replication construction, but the old files did not save an explicit delete130/label-equality certificate against the separate585 literal. We do not pretend that binding exists. It is unnecessary for the obstruction below, whose premises are all in the old715 certificate itself.

## Existing exclusions and the genuinely new question

The previous `d3d4_transfer/REPORT.md` excludes one added vertex and any helper block of size≤5 at cap11, by requiring at least65 old-new spokes. It did not exclude a10-helper block. The separate585/cap9 all-edge-preserving theorem is not applied at cap11/715. Likewise, the65Delta complete-replication bound in `polarity585_replication/DERIVATION_PACKAGE.md` permits no external helper vertices and does not directly settle the proposedPetersen block.

The proposed rule retains every715 source edge, adds no old-old edges, adds10 helper vertices inducingPetersen, and attaches each helper to8 old eligible vertices. Core vertices are already degree11. The proposed725-point graph is only a rule; no candidate is generated.

## Core-only route interface

Let A_h be the classes pinned by helperh, N_a the8 core neighbors of classa, and T_a the core vertices in the old radius2 of any pin in classa. T_a is independent of which of the3 class members is pinned: they have the same core neighbors, and any internalP3 step merely supplies those same already-direct8 neighbors.

Any≤3 route fromh to a core target either enters the old graph immediately and uses≤2 old steps, or first goes to one ofh's three helper neighbors and then enters old with one remaining old step. A return through another helper would end at a core vertex, but core vertices cannot have helper edges. Therefore the exact necessary core cover is

    core ⊆ union_{a∈A_h} T_a ∪ union_{g∼h} union_{a∈A_g} N_a.

The N_a partition the520 core vertices. Hence, afterh's ownT coverage, every class that owns at least one still-missed core target must occur in the pin-class union ofh's helper neighbors. There are at most8 own classes and24 neighbor classes. This specifies a class-level constraint, not a feasible assignment.

The separate saved585 Steiner3-(65,9,1) certificate would give own8 coverage≤380, at least140 missed core vertices, and at least18 external owner classes. Because the saved715↔585 exact quotient/label binding is absent, those numerical bounds are retained as **conditional only**, not silently applied to715. No core-only solver or existence/nonexistence claim is made. The next class-target argument already stops the complete proposed rule.

## Actual class-target obstruction: at least195 spokes, but only80

Fix one of the65 actual eligible classes C. Let e(C) count its helper-to-old spokes, and X(C) be the helper vertices owning any of these spokes. Suppose e(C)≤2. Since C contains3 vertices, some f∈C is completely unpinned, i.e. has no helper neighbor.

Attack all possible≤3 routes from an arbitrary helperh to thisf:

* If the route starts by entering old at a pinq and then stays old, the remaining≤2 old steps reach an eligible target only inq's own class. The saved715 certificate forcesq∈C, so h∈X(C).
* If it first takes anH-edgeh–g, then enters old atq, at most one old step remains. Againq is inC, so g∈X(C) andh is anH-neighbor ofX(C).
* A route that returns through an old pin to another helper and then ends atf would require a helper–f edge, which does not exist. The same excludes two initialH-edges followed byf. Shared old pins therefore introduce no missing≤3 route.

Consequently every helper within3 off lies in closedN_H[X(C)]. SincePetersen has degree3,

    |N_H[X(C)]| ≤4|X(C)| ≤4e(C) ≤8 <10.

At least two helpers would fail to reachf within3. Therefore e(C)≥3 for everyclassC. The65 disjoint classes demand at least65×3=195 spokes, but the10 helpers have only10×8=80. Contradiction.

This proof does not need a class to be independent or require aPetersen-specific domination calculation; its only local metric premise is the inherited actual715 eligible-R2 separation. The center/leaf distinction is correctly retained in the source degree data, and no unattached-target route is omitted. It even excludes any10-helper graph of maximum internal degree3 with≤80 spokes under the same old-edge rule. It does not exclude a different number/degree of helpers or additional old-old rewiring.

## Meaning and stop

The original independent-class prediction failed, and the actualP3 data changed the proof. The complete fixedPetersen10 proposal is strictly impossible; the isolated core-only cover problem was not solved or claimed impossible. No blind assignment search is useful for the stopped complete rule. Other source variants, changing old edges or adding old-old edges, and general(11,3) improvement above715 remain outside this scope.

The metadata preparation process used0.035727CPU seconds under the20CPU cap. Brief prior local report/code reads were not individually metered. There were0source adjacency parses/BFS,0old local-data recomputations,0solver/Lean/review calls. Everything is terminal; no automatic new helper template or degree ladder follows.

Evidence: PRED.md, BUDGET.json, SOURCE_CLASS_INTERFACE.json, prepare_interface.py, RESULT.json, TERMINAL.json; inherited `d3d4_transfer/{SOURCES.json,RESULT.json,REPORT.md,screen.py}` and the literal715 source remain unchanged.
