# Two natural H3 copies with a twisted cross matching

## Source and exact scope

The source is the natural364-vertex H3 polarity graph with714 edges, degree3 at28 absolute vertices and degree4 at336 others. It is bound by ../d4_D5_polarity_extensions/source_and_single/PORT_BINDING.json to Q_data.json['H3_graph']. Its diameter is at most5 by the existing polarity-quotient argument: a point-to-polar-line walk has odd length at most5 in the diameter6 H3 incidence graph and projects to a source walk. The Moore bound for maximumdegree4/diameter4 is161<364, so the source diameter is exactly5. This source evidence is inherited; no source all-root BFS is repeated. The separate regular364/728-edge public graph is not used.

The ledger search found no exact prior experiment on this same two-copy, natural714-edge source and arbitrary twisted cross matching. The old maxdegree4 helper range and the binary-branch364 matching MILP have different adjacency rules and are not restarted by this construction.

Let pi be an actually supplied bijection of the364 source vertices. Take two disjoint copies of the source G and add exactly x0--pi(x)1 for every x. Reverse matching steps use pi^-1. No involution or fixed-point-free assumption is required: even pi(x)=x joins distinct vertices in different sheets. If a geometric reflection is used, its point-label permutation and its binding to this actual source must be supplied, not inferred from a different labeling or from ambient orthogonality alone.

## General graph and distance guarantees

The result is simple and connected on728 vertices with2*714+364=1792 edges. Every vertex gains exactly one degree, so it has56 vertices of degree4 and672 of degree5. Same-sheet distances are at most5 because every source edge remains. Every cross pair has the route x0--pi(x)1 followed by an old path to y1, of length at most6. Therefore the global diameter is at most6, for every bijection pi.

If an actual complete radius5 check misses any cross target, that distance and the global diameter are exactly6. A failed search among only routes crossing once is not such a check: three matching crossings can create a shorter route. A simple shortest cross path of length at most5 has either one matching crossing, or exactly the pattern cross-old-cross-old-cross. Five crossings within5 steps are immediate matching backtracks and reduce. For example three crossings from x0 can reach labels in pi(N_G(pi^-1(N_G(pi(x))))). The producer's full new-graph distance check must include these routes.

If all364^2 cross pairs pass radius5, same-sheet inheritance proves the entire graph has diameter at most5. It is then exactly5 because the degree5/diameter4 Moore bound426 is below728. An unproved source automorphism does not justify reducing those pairs to one root. A positive result receives the separately assigned single finite independent728-vertex verification; a negative result needs no old-source revalidation.

## Why source automorphisms are the wrong matching

If pi is a graph automorphism of G, relabel sheet1 vertex y as pi^-1(y). The old edges remain a copy of G and every cross edge becomes vertical. The graph is G Cartesian-product K2, whose distances are d_G(x,y)+sheet_difference and whose diameter is6. Thus a chance of diameter5 requires a matching outside Aut(G). One literal old edge mapped to a nonedge is a valid nonautomorphism witness. Preserving the ambient quadric alone does not prove or refute source-graph automorphism.

## The pointwise-two-ball obstruction

Suppose source vertices p,q satisfy d_G(p,q)=5 and pi fixes every vertex of B2_G(p) union B2_G(q) pointwise. Then p0 cannot reach q1 within5, so the entire graph has diameter6. This lemma does not require p,q to be ports or pi to be involutory; those are source-specific conveniences for testing its hypotheses.

For a one-cross path let the old prefix and suffix lengths be a,b, so a+b<=4. If a<=2, its crossing source z lies in B2(p), hence pi(z)=z. If b<=2, its crossing image pi(z) lies in B2(q), which also forces z=pi(z), since pi is bijective and fixes that image. At least one of a,b is at most2, so the entire path would give a source p-to-q walk of length a+b<=4, a contradiction.

For a reduced three-cross path of length at most5 the pattern must be cross-old-cross-old-cross. The first crossing fixes p; after its first old step the label is in B1(p), fixed also by pi^-1; after the second old step it is in B2(p), fixed by pi. Its final label cannot be q. The five-cross case reduces as above. Hence all possible short cross routes are excluded, rather than merely the one-cross subset.

The hypothesis is pointwise vertex-label fixation, not setwise preservation of the balls. It does not exclude an entire reflection type unless the actual coordinate action proves the condition for each member. Whether a candidate had already been selected before this selector was derived must remain explicit. This file performs no coordinate recovery, reflection selection, candidate graph construction, solver or BFS.

Producer terminal: after the selector was explicitly revised before graph production, the single chosen nonautomorphism reflection gave a simple728/1792 graph with degree4 at56 vertices and degree5 at672. Its actual complete root0 radius5 check misses78 cross targets, first vertex448=(sheet1,label84). The general upper bound6 therefore proves exact global diameter6. No independent negative-case BFS, alternate reflection or further graph was run. The final selected reflection has norm1 and fixes no full port B2 ball; the two-ball lemma is a valid selector obstruction, not an explanation of every failure of the selected surviving class.
