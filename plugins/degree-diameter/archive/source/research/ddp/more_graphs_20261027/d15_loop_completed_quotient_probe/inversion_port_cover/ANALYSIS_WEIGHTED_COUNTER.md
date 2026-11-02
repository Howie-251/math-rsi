# Cost-one/cost-two symmetric port cover: paper scope

Let one selector choose one actual zero port, with weight1, and another choose both actual distinct ports v,-v, with weight2. A standard sequential at-most15 counter may receive a list with the pair selector repeated twice. Its semantics count **positions**, not distinct variables. Setting that selector true contributes one at each occurrence. The usual prefix-count assignment is a witness for every selection of total weight<=15; the counter implications forbid selections whose repeated-input total exceeds15. The helper must not deduplicate its input list. Deduplicating literals within an individual clause does not change clause truth.

For a fixed accepted graph G of diameter<=D, append a distinct vertex z joined exactly to selected ports S. Old-old paths are retained, and

    d_new(z,t) = 1 + min_{s in S} d_G(s,t).

A shortest z-to-t path never revisits z, so both directions are exact. Therefore the cover constraints must require every old target to lie in R_(D-1)(S). The clause for a target is the OR of selectors whose selected one/two-port union covers that target. Selecting a pair selector must actually add both spokes; a pair's cover is the union of the two real cached balls.

Every selected old port must have an available degree slot in the exact source used by those cached balls. If selector port sets are mutually disjoint, weighted count equals the new vertex degree. If they overlap, the weighted model remains sound as an upper bound on distinct spokes but is not a complete description of all union-size<=15 sets. Actual decoded distinct-pins cardinality and old degrees must be checked before export.

This note proves the abstract reduction only. It does not assert that a particular counter implementation, cache binding, SAT result or generated graph has been checked. Static code review is pending the producer's READY message. No source traversal, graph, solver or candidate is run here.
