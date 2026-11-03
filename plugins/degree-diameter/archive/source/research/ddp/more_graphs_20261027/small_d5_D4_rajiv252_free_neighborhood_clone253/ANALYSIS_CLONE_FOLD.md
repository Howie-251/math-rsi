# Clone folding and the exact single-edge criticality gate

Verdict: **VALID**. The actual [criticality.py](criticality.py) implements the stated complete NB<=4 endpoint-intersection gate. Together with its terminal630/630 critical-edge result, the folding argument excludes the entire fixed-source clone/cut rule, without enumerating cut sets or generating253-vertex graphs. This paper review runs no source audit, word enumeration, BFS, solver, or graph construction.

## Fixed source and operation

The source is the existing [rajiv252.edges](../../second_mechanism/rajiv252.edges), with252 vertices and630 edges, all degrees5, and inherited D4. It is not the old254-vertex modified graph. Its actual source binding and edge IDs are saved in [INPUT.json](INPUT.json).

Choose any old prototype x. Let F be a set of old edges which avoids every edge incident with x and touches each old neighbor of x at least once. Delete F and add a new vertex y adjacent to exactly the five vertices N_G(x), with no other new edges. Every selected neighbor loses at least one edge before receiving its y-spoke, so the operation respects maximum degree5. Since all five old neighbors need a freed slot, F is nonempty.

The important restriction is that x's whole old star is retained and y duplicates exactly that neighborhood. Neither a cut-budget bound nor a matching assumption is required for the negative argument below.

## Exact old-pair distance equality

Put H=G-F and let K be the augmented graph. Since no x-star edge was deleted, N_H(x)=N_G(x). Define f:K->H by fixing every old vertex and sending y to x. Each old edge of K belongs to H. Each new edge y-v maps to the retained edge x-v of H. Thus f is a graph homomorphism that fixes H pointwise.

For old vertices u,v, H is a subgraph of K, so d_K(u,v)<=d_H(u,v). Conversely, f sends every K path from u to v to an H walk of the same length, so d_H(u,v)<=d_K(u,v). Hence the exact equality

    d_K(u,v) = d_(G-F)(u,v)

holds for every old pair, including the possibility of infinite distance. The clone cannot repair any old-old route lost by deleting F: every apparent shortcut through y can be folded through the retained x at the same cost.

This explains the difference from a degree-slack false-twin extension. When no old edges need deletion, cloning can preserve old distances. Here the cuts are required for degree capacity, and their old-distance damage cannot be repaired by this same-neighborhood clone.

## Why all NB<=4 walks give an exact critical-edge test

For root r and endpoint v, let W(r,v) be all nonbacktracking source walks of lengths0 through4 ending at v. For each walk w, let E(w) be the set of its undirected source edges; repeated use of an edge is recorded only once. Define

    I(r,v) = intersection of E(w) over every w in W(r,v).

The inherited source D4 ensures these endpoint collections are nonempty. The empty walk is included for r=v and has edge set empty, making I(r,r) empty as required.

For an old edge e, e belongs to I(r,v) precisely when every source NB walk from r to v of length at most4 uses e. A path in G-e of length at most4 is itself one of the source NB walks avoiding e. Conversely, any source NB walk avoiding e is a walk of G-e and yields a path no longer than it. More generally immediate backtracks may be cancelled without creating a new edge, so restricting to nonbacktracking walks loses no possible short avoiding route. Therefore

    e in I(r,v)  iff  d_(G-e)(r,v)>4.

The test must include all lengths at most4, rather than only shortest walks or only length4. It must also use the same edge ID in both directions; arc-specific IDs would not express deletion of an undirected edge.

The source is simple5regular. Each root has1+5+20+80+320=426 nonbacktracking prefixes through length4, including the empty prefix. The producer enumerated all such prefixes for all252 roots. This is a new criticality computation, not a repeated old all-root BFS or an enumeration of modified graphs.

## Actual implementation review and inherited result

The code assigns one ID to each sorted undirected source edge and stores that ID in both adjacency directions. Its stack visits every prefix, with the only next-step restriction v!=previous_vertex, stopping expansion at depth4. On every arrival it initializes an endpoint intersection with that walk mask or ANDs the next mask into it. The root empty prefix contributes mask0. It asserts the full depth counts (1,5,20,80,320) and that every source endpoint was seen. The support mask is formed by OR-ing edge bits, which is the correct deletion criterion even if a longer walk uses an edge more than once.

The saved [RESULT.json](RESULT.json) records107352 prefixes,630 critical edges, and zero noncritical edges. [CRITICAL_WITNESSES.json](CRITICAL_WITNESSES.json) binds each edge to an actual root/target pair and its full-route-intersection evidence; [NONZERO_ROUTE_INTERSECTIONS.jsonl](NONZERO_ROUTE_INTERSECTIONS.jsonl) retains the nonempty intersections. These counters are words, edges, and ordered endpoint records, not candidate graphs or ordinary bad-pair totals. This review reads the code and terminal result without rerunning them.

For any legal F, choose any e in its nonempty edge set. The saved criticality witness gives old u,v with d_(G-e)(u,v)>4. Since G-F is a subgraph of G-e,

    d_(G-F)(u,v)>4.

The clone-fold equality transfers this failure unchanged to the253-vertex graph K. Therefore every legal F and every prototype x in this fixed source fail the target, irrespective of the number of cuts. No separate list of258k cut choices, optimizer, or candidate BFS is needed.

If some edges had instead been noncritical, that would have been only a necessary gate: every deleted edge would have to be individually noncritical, but several such deletions could still destroy all short alternatives jointly. Such a result would not establish safe F or a successful clone. The actual all-critical result makes that unexecuted branch unnecessary.

## Scope and limits

The closed rule is exactly this old252 source, retaining a prototype's entire old star, deleting a nonempty old edge set to free its neighbors, and adding one false twin with precisely the original neighborhood. It does not exclude arbitrary253-vertex maximum-degree5/D4 graphs, another source, cutting the prototype star, a different new neighborhood, additional old-old edges, or multiple cooperating new vertices. Those changes can invalidate the folding map and are not licensed or searched here.

No253-vertex graph was generated. Actual target n, exact diameter, and ordinary unordered bad-pair totals remain null. The finding is a source-specific strict gate and reusable folding explanation, not a claim of a new general classification or a completed overall Goal. It belongs with the producer's same source-augmentation family record, rather than a separate method count.
