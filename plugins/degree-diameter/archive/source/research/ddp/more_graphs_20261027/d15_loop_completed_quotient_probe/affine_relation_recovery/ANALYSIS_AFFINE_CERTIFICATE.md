# Exact affine-line relation certificate

The proposed certificate is sufficient to recover each relation of the fixed source, provided the producer performs its stated exact check on every source row. Fitting the origin and basis inputs alone is not a certificate. This paper runs no fit, graph, BFS, solver or coordinate search.

Fix one directed controller arc i->j and local coordinates x,y in V=F3^d, where d=4 for the81-point fibers and d=5 for the243-point fibers. Let a nonzero normalized vector v specify the candidate common line direction. Choose a pivot r with v_r=1 and define Qv(y)=(y_k-v_k y_r) for k different from r. This linear map has rank d-1 and kernel exactly <v>. Every fiber of Qv therefore contains exactly three points, differing by the multiples0,1,2 of v.

The relation specified by (v,B,c) is

    R(i,j) = {(x,y): Qv(y)=B*x+c}.

The output c is determined from the candidate target coset at x=0. Column k of B is the difference between the candidate coset at x=e_k and c. These values uniquely specify a candidate affine map V->F3^(d-1). They do not assert the other input rows are affine.

For each of all3^d input rows, the actual three target points must be distinct and must equal the complete solution set of this displayed equation. Equivalently, after a separately verified three-point size, all three images under Qv equal B*x+c: the complete quotient fiber has size exactly three, so containment forces equality. The stated explicit exact3set comparison is sufficient. If every row passes, the stored matrices reproduce every adjacency entry for this controller arc. Repeating this for every directed arc of the already verified five-target-controller partition certifies the whole loop-completed relation; it is not a sample or a rank-only heuristic.

A particular right inverse L of Qv gives a compact enumerator y=L(B*x+c)+t*v, t in F3. Alternatively one can retain one pivot-normalized representative per quotient value. The choice of representative changes no target set. No full-rank condition on B is needed for this row-wise statement; symmetry, reverse relations and actual degrees follow from the exact matching to the original source, rather than from assuming arbitrary new B would be valid.

The virtual loop is a single self-entry for this relation statistic, not an additional edge or a claim about the usual graph-theoretic degree contribution of a loop. To recover the original simple graph, omit an enumerated entry exactly when both its controller label and local offset equal the source label and offset. An identical local offset in a different controller is still a real edge and must remain. The previously saved loop labels and all actual source rows provide the binding of these deletions; no source is modified by the fitting process.

Passing this certificate would recover the fixed source's explicit affine relation recipe. It does not certify the diameter of a changed controller, field, direction, matrix or translation. The original source diameter is inherited separately, and no new graph or improved lower bound follows merely from recipe recovery.

Evidence interfaces: ../RESULT.json and ../REPORT.md for the fixed81/243 quotient and virtual-loop binding; this directory's producer run and eventual RESULT for the actual all-row fit. This is only the mathematical sufficiency review, with zero numerical runs.

Inherited actual outcome: the producer subsequently completed all960/2100 directed arcs and77760/510300 literal rowsets on the two sources, with no counterexample. Its aggregate CPU receipt is0.803465985 seconds. Thus the stated sufficiency conditions were actually met for these fixed sources. This is inherited RESULT.json data, not a new computation by this paper.
