# A reusable unit-neighbor lemma at a degree-six point

Let H be a simple pair-covering five-uniform hypergraph on 21 vertices with 34 edges. Let x have degree six, and let U be a set of at least seven degree-eight points such that λ(x,u)=1 for every u∈U.

**Claim.** Either an already established strict local permutation witness supplies Property B, or every U-pair has codegree two and every edge through x contains at most two U points.

For λ(u,v)≥3, the eleven allowed (6,8,8) profiles with x-pair codegrees one are strict; see the frozen `TWENTYONE_SIX_REDUCTION_VERIFIED.json`. Thus all U-pair codegrees may be assumed to be one or two. For x plus any three U points, the complete 62-profile (6,8,8,8) table has 50 strict profiles and twelve residues. Every residue has zero common-four multiplicity; the three U-pair codegrees are either (2,2,2), or a permutation of (1,1,2) whose every common triple multiplicity is zero.

The common-four conclusion gives the asserted at-most-two bound on each x-edge. Form the graph G on U whose edges are unit-codegree pairs. Every three vertices induce an empty graph or a path of length two. If G has an edge a-b, each remaining point is adjacent to exactly one of a,b. Points assigned to the same side are nonadjacent (otherwise there is a triangle); points assigned to opposite sides are adjacent (otherwise there is a three-vertex graph with exactly one edge). Therefore G is complete bipartite with two nonempty parts.

Any two U points can then be extended to a length-two path: for a pair in the same part choose a point opposite; for a cross pair choose a third point in a part of size at least two. Such a third point exists since |U|≥7. The (1,1,2) residue says the common-edge multiplicity of x with this pair is zero. Hence no x-edge contains two U points. Six x-edges cover at most six U points, contradicting unit pair coverage and |U|≥7. Thus G is empty, proving all U-pair codegrees are two.

This is a generalization of the frozen equality-case argument: it requires only |U|≥7, not |U|=12, uniqueness of x among six-degree points, or absence of seven-degree vertices. Its numerical inputs are exactly the prior verified 61 strict witnesses. It is a paper lemma until the corresponding actual-input and finite-classification interfaces are formalized.
