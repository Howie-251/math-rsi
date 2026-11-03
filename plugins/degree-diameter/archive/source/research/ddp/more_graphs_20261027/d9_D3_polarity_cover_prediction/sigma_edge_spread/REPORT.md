# The fixed involution has32 suitable old edges, but no four-edge spread

2026-10-27. The local edge-signature prediction is supported, while the frozen four-spread existence prediction is refuted. No new graph was generated.

Using only the saved actual585 source, its520 port blocks, and the previously verified permutation sigma fixing p=0, the check selected every old unordered core edge{v,sigma(v)}. There are exactly32. For all32, both endpoints are at distance3 from p (not in its R2, with the sourceD3 inherited); the two nine-port sets intersect in2 ports, and their union has16 ports excluding p. Every union is sigma-invariant and corresponds to exactly8 of the32 nonfixed port-pairs.

A complete exact-cover-of-four test over these32 saved masks has no solution. It used only17 recursive nodes, choosing a required uncovered port-pair and considering every still-compatible old edge containing it. Every possible four-block partition must appear in such a branch, so failure is exact for the fixed mask family.

A small follow-up on these same masks explains the obstruction more strongly. Among the496 pairs of masks,144 are disjoint,160 intersect in2 port-pairs, and192 intersect in3 port-pairs. No three masks are pairwise disjoint: for every disjoint pair, every third mask intersects at least one of them. Thus the maximum number of compatible blocks is exactly2. No alternative blocks or coverage optimization were introduced. The count is in COMPATIBILITY.json, reproduced by compatibility.py.

The source/involution scan and exactcover used0.001002951 CPU seconds; the saved-mask compatibility calculation used0.000267263 seconds. There was no BFS, source download, automorphism search, helper search, compiler invocation or graph-candidate generation. SIGMA_EDGES.json retains all32 literal old edges and their port sets/masks. RESULT.json and terminal.json retain the complete negative outcome.

This excludes the proposed four-edge-spread rule for this fixed source and verified sigma. It is not a nonexistence statement for arbitrary586-point graphs, other source automorphisms, different anchor families, or general(9,3) construction. The conditional graft producer receives no spread input and must not generate its proposed candidates. This finite rule is now stopped; no replacement block family is started.
