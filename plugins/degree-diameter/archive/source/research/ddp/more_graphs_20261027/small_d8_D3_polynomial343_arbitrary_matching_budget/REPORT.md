# F7³ source plus an arbitrary matching: strict endpoint-budget exclusion

The fixed polynomial source plus **any one simple complement matching**, including a partial matching, cannot have diameter three. From p=(0,0,0), the resulting closed radius-three ball has at most 302 of the 343 vertices, so at least 41 targets remain outside it.

The parent froze the endpoint-image prediction before its first exact symbolic test. `check_endpoint_budget.py` evaluated all 343 triples (u,v,d) once and found 154 distinct endpoints, 22 for each d. Its saved body CPU was **0.000389805 seconds**. The prediction image<=194 is supported. `ANALYSIS_PROOF.md` separately derives the exact image algebraically: q(q²−q+2)/2, using the involution v↦−e/v.

All short-path types are included: zero new matching edges (154), one new edge first/middle/last (upper bounds 50/48/43), and the only reduced two-new-edge type M-G-M (at most seven). Their sum is 302. These are endpoint upper bounds, not measured graph bad pairs. There was no source adjacency generation, augmented graph, BFS, matching assignment or solver call. Actual graph order, diameter and ordinary unordered bad pairs remain null.

The same algebra gives a strict source-plus-one-matching bound for every odd prime-power q>=7. This is a deductive statement about the same formula and augmentation family, not additional field experiments or independent methods. The involutive-automorphism matching observation in the proof is auxiliary and is weaker than the arbitrary-matching conclusion here.

This record updates the existing `ddp-wave11-polynomial343-matching-scout` source family. The old source-only gap is superseded for this augmentation by a complete matching-independent obstruction. It does not exclude other 343-vertex maximum-degree-eight graphs, several added matchings, arbitrary added edges, deletions or rewiring. Stop this fixed single-matching family; a different connection rule needs a new explicit coverage argument, not matching optimization.

Saved target baseline: (8,3), lower bound 253, as recorded in the parent PREDICTION. All primary data and the paper proof are listed in `wiki_rows.json`; no global Wiki synchronization was performed here.
