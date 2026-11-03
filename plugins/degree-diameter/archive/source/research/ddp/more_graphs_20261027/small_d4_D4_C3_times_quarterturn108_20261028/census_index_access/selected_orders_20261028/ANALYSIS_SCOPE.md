# Scope of the selected quartic Cayley census filter

Verdict: **VALID**. The69 selected order files cover every simple undirected Cayley graph of maximum degree at most4 that could improve the saved (4,3) lower bound41 or the saved (4,4) lower bound104. This is a scope proof, not a filter result. No census member is downloaded, decoded, or traversed by this review.

## The published completeness matches the graph class

Evans–Potočnik's [A census of Cayley graphs](https://arxiv.org/html/2512.05406v1) states in its abstract and introduction that their generated lists include all4-valent Cayley graphs through order1025, up to graph isomorphism. Section2 specifies simple undirected graphs and inverse-closed generating sets, hence connected Cayley graphs. The [authors' census page](https://graphsym.net/) separately identifies its tetravalent archive as complete through1025 and states that it contains one sparse6 file per order5..1025. These primary passages were read directly for this review.

The classification is not restricted to abelian groups, graphical regular representations, arc-transitive graphs, or a chosen list of group presentations. A graph need not preserve a particular group labelling to occur: one representative of its graph-isomorphism class suffices because order, degree, and diameter are isomorphism invariants. Different left/right Cayley conventions likewise do not restrict the graph class.

The local [index summary](../INDEX_SUMMARY.json) and [access report](../REPORT.md) bind archive members to the orders5..1025. They are metadata evidence only and do not establish any diameter exclusion by themselves.

## Why exactly these69 orders are enough

For a simple graph of maximum degree Delta and diameter at most D, the breadth-first tree gives the Moore bound

    n <= 1 + Delta * sum_{i=0}^{D-1}(Delta-1)^i.

For maximum degree4 this is53 at D3 and161 at D4. A strict improvement over41 therefore has order42..53; a strict improvement over104 has order105..161. These are12 and57 order files, respectively, totalling69.

Lower valencies cannot be missing from this reduction. For maximum degree at most3, the corresponding bounds are22 at D3 and46 at D4, already below41 and104. A Cayley graph is regular; thus any Cayley graph of maximum degree at most4 capable of either improvement has degree exactly4 and belongs to the cited quartic census. Disconnected graphs cannot have the required finite diameter. No orders above53 or161 need data inspection, and no smaller orders can improve the respective saved lower bound.

Consequently, using only the files42..53 for radius3 and105..161 for radius4 is mathematically complete for the two no-improvement questions. It does not require downloading the rest of the roughly24GB archive.

## What a filter failure proves

For any decoded graph, if one actual root r has a vertex outside its closed radius-D ball, that graph has diameter greater than D. This negative implication needs no Cayley or transitivity assumption. It does not give the exact larger diameter, nor a total count of ordinary unordered bad pairs.

If the authorized extraction and filter actually process every graph in all69 selected members, with no unparsed or untested graphs, and every graph has such a radius failure, then the result is:

* By the cited census completeness and the complete selected-member computation, no simple connected Cayley graph of maximum degree at most4 improves41 at D3.
* By the same reasoning, no such Cayley graph improves104 at D4.

The extraction receipt and producer's complete processing counts are the computational premises of that statement; they must be read from their actual terminal evidence. A timeout or partial member traversal cannot support the full conclusion. This paper does not assert that those premises have already completed.

A radius pass is a provisional candidate for the parent's independent all-n-roots check before a positive result is announced. The mathematical Cayley property would give vertex-transitivity, but this acceptance step also checks the actual decoded/exported graph. A positive check is small here because n<=161. If a checked candidate has D<=3 at n>41, its diameter is exactly3 since the degree4/D2 Moore bound is17; likewise a checked D<=4 candidate at n>104 has exact diameter4 since the degree4/D3 bound is53.

## Precise limits and credit

An all-negative completed filter is a **census-based complete Cayley no-improvement result**, combining the authors' existing classification with the new diameter filtering. It is not a new classification of Cayley graphs, a universal degree/diameter upper bound for arbitrary graphs, or an exclusion of all vertex-transitive graphs. Cayley graphs form a subclass of vertex-transitive graphs; the converse does not hold.

Nor would these selected files establish that the largest Cayley graph has order exactly41 or104: smaller census orders were not filtered for extrema, and the public graphs attaining those numbers need not be Cayley. The supported statement is only the absence of an improvement above those thresholds in the Cayley class.

This review performs zero member downloads, census decodes, BFS calls, solver calls, or graph constructions. Producer computation and any positive validation are separate evidence. No general Goal-completion claim follows.
