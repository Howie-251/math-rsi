# One fixed E-S cut: exact prepared positive family

Status: PREPARED_NOT_SOLVED. The fixed family is compiled, with no SAT invocation, chosen voltage assignment or graph BFS. The original parent-directory no-cut model remains strictly excluded and its CNF/RESULT/PREDICTION were not changed.

## Actual deterministic binding

Use the existing thirteen projective F3 vectors and twenty-four orthogonality edges. The lexicographically first external-secant edge is(0,7). Its external endpoint is0, its secant endpoint7. The new spanning tree explicitly contains this edge and is completed by lexicographic Kruskal. All tree shifts are0; delete only its sheet0 lifted edge(0,21). Thus71 original lifted edges remain, rather than the original72.

Helpers are a=39,b=40,c=41 with fixed path a-b-c. The released external vertex e=0 is fixed adjacent to a. The lexicographically first absolute base not adjacent to cut-secant7 is T=8; c is fixed adjacent to its full fibre(24,25,26). The other released vertex s=21 must pair with an unused absolute lift whose base is not adjacent to7. Of the two such absolute bases, T is already used by c; the remaining choices are27,28,29.

The other nine absolute ports are otherwise free. Leaf a chooses two of them in addition to e. Middle b chooses two. Vertex s chooses one of27,28,29. The four ports then unused by those spokes/pair are partitioned into two old-old pairs. No s-helper edge is present in the domain. Every added old-old edge is absent from every old lift: absolute bases are mutually nonadjacent, and the allowed s-mates have a nonadjacent base.

Each old absolute port gets exactly one new edge. The released e and s regain their missing degree. Helpers have degrees1(path)+1(e)+2(A)=4 at a,2(path)+2(A)=4 at b, and1(path)+3(T)=4 at c. Every structural assignment is therefore simple4regular with42 vertices and84 edges:

    71 retained oldedges +2 helperedges +8 spokes +3 newoldoldedges.

There are93 structural Boolean variables:36 shared shift selectors and57 new-port selectors(36 absolute pairs,3 released-S pairs,18 a/b spokes). The exact labeled domain is3^12 times3780=2008846980 structural assignments. Here3780=3 choices for s-mate times C(8,2) choices for a times C(6,2) for b times3 pairings of the four leftovers. These are potential assignments, not executed graph trials.

## Gauge and exact scope

The selected cut edge is included in the tree before fixing its shift to0. Fibre coordinate translations kill all tree shifts; the global residual translation can identify this selected cut match with sheet0. All remaining old-port domains are closed under the applicable fibre relabelings: fullT fibre is fixed as a set, and all allowed lifts of the other base types are included. Nevertheless the scope claimed here is only the explicitly fixed basecut/T/e-to-a/P3 family, not all possible single-edge cuts or all42 graphs.

The parent no-cut exclusion relied on preserving every old lift edge and on new helpers only attaching to absolute ports. Both hypotheses are changed: e is now a degree-three external old vertex and attaches directly to a. Hence b-a-e gives b a two-step external target and one further step gives targets over the other two external bases. This supplies the missing three-state buddy route that did not exist in the excluded originalP3 rule. It is a changed route mechanism, not another voltage sample of that original model.

## A genuine uniform positive root certificate

Leaf c is adjacent to all three lifts of T=8. Every base vertex has a base path of length at most2 from T. Because T is not adjacent to S_cut and is absolute(so not adjacent to E_cut), such a path cannot use the E_cut-S_cut edge. C_FULL_FIBER_GUARANTEE.json saves one actual cut-avoiding base path for each of the13 target bases.

For any target sheet, lift that short path backwards. Its starting point is one of the three T-fibre vertices joined to c, so c reaches every old vertex in at most3 steps. The new helpers a,b are at distances2 and1 along the path. Thus c has uniform R3 coverage of all42 vertices for every structural assignment. This is not R2 coverage; no Y2(c,target) literal is asserted merely because this R3 proof is available.

For b, the external budget is tight rather than automatic. Its two absolute spokes each supply at most one length-three route per external base. The route through a and e supplies one more endpoint per external base: e itself and its two retained external neighbors. To cover all nine external lifts, all those per-base endpoints must be distinct and neither absolute-spoke route may be destroyed by the cut. The generic exact model, not a partial hand certificate, must check these and every other pair.

In particular a successful c-root certificate does not establish the graph diameter. All old-old and other new-root pairs remain part of the complete SAT model and the literal decoder checks all42 roots for any later SAT witness.

## Exact compiled reachability and measured preparation

The old compiler's CNF class is reused without invoking its old build or rewriting its files. Shared old-edge selectors are preserved. A selectable Y_uv claim of distance at most2 must have a real direct edge or a real two-edge witness; every AND witness implies each argument. Each unordered pair's D3 clause requires Y_uv or a real first edge followed by such a Y. These are existential sound witnesses. Reverse implications are unnecessary because every real D3 graph extends to the auxiliary assignment of its true paths.

Only genuinely fixed paths of length at most2 make Y a constant true. The c-root R3 certificate is not inserted into Y. The model retains the generic diameter checks rather than silently substituting one-root or sampled coverage.

The actual prepared file has6403 variables and13226 clauses, with682 structural clauses,206 potential edges and41 fixed true edges;178659 bytes. Compiler-body CPU was0.110873466 seconds. The saved INPUT/VARIABLE_MAP/REACH2_MAP and self-contained compile.py/decode.py bind all labels and selectors. The decoder is not run now; on a later supplied satisfying assignment it checks every CNF clause, exact84-edge4regularity, the deleted-edge absence and complete all-root D3 before export.

No solver budget is consumed by preparation. A separate bounded execution must be frozen by the parent before any SAT call. This document neither reports a candidate nor changes the original strict negative result.
