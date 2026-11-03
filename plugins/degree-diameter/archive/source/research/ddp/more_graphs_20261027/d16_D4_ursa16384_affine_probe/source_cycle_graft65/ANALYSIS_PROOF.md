# Permutation insertion, universal return rank and the projected counterexample

This is the one source-aware graft selected by the producer, not a search over return words or edges. The original type permutations are a=type0, A=type3, b=type1, B=type2. The original paired fiber relations are retained; canonical line matrices can be singular, so their reverse charts are used as inverse relations, not obtained by pretending to invert a canonical matrix.

## Exact permutation insertion

For an old a-edge u->v insert a fresh controller w by a'(u)=w and a'(w)=v; all other a images remain. Its inverse has A'(w)=u and A'(v)=w, with every other old inverse image unchanged. Independently insert w on the old b-edge c->t by b'(c)=w, b'(w)=t; consequently B'(w)=c and B'(t)=w. Both new maps are permutations.

The frozen literal is u0,v16,c48,t46,w64. Put q=b(v)=57. The definition t=A(q),c=B(t) gives

    64 --a'-->16 --b'-->57 --A'-->46 --B'-->64.

The four old endpoints are distinct. Thus each affected old controller port merely replaces one old neighbor by w, while w has the four distinct neighbors16,0,46,48. The resulting controller is simple4-regular on65 vertices with130 edges. The reciprocal type relations make the corresponding fiber edges undirected.

## What the cached rank actually guarantees

The saved WORD_IMAGES.json record0132, meaning abAB, has output image rank4 and image basis[1,4,16,64] in F4^4; image size256. This cached record was read, not recomputed. Its separate linear_rank2 describes dependence on the starting coordinate and is not the route-parameter rank.

For a length4 word the endpoint is Fx+c+C*lambda, with four free F4 parameters. Rank(C)=4 implies every target coordinate is available for every fixed input x, regardless of whether F or any canonical step matrix is singular. Therefore the closed controller word above fills the entire w fiber within4 from every w-fiber coordinate. This verifies the intended local prediction.

It does not prove global coverage. For example insertion changes the selected original b4 cycle into a b5 cycle, so its four old controllers no longer retain their former bbbb full-rank self-return through that cycle. Preserving one return at w cannot be used to inherit the source's old-old distances, since two old controller edge blocks were removed.

A sufficient universal certificate would assign, to every ordered controller pair among65^2 pairs, a length-at-most4 word with full route-parameter rank4. More generally a complete union certificate must cover all256 target coordinates for every source coordinate at every such pair. A union checked only at source coordinate0 is insufficient without a separately proved symmetry. The graft supplies no inherited transitive deck action on its new controller; source representative-root reductions must not be assumed to survive.

## The actual coarse obstruction ends this control

The producer's complete new65-controller radius4 check finds24 ordered,12 unordered coarse pairs farther than4, including0->11. Any path in the hypothetical fiber lift projects to a controller walk of the same length. Hence every pair from controller0's fiber to controller11's fiber is farther than4. No fiber image, offset or favorable return at w can repair an absent controller path.

Consequently the proposed16640=65*256 graph cannot have diameter4. No16640-vertex graph or fiber BFS was generated, and no global fiber-graph diameter or ordinary unordered bad-pair total is claimed. Conditional on the recipe, it would be16-regular with133120 edges, but the producer stopped at the earlier necessary controller gate. The one graft is stopped; no alternate return word, edge, offset or controller was tried by this analysis.
