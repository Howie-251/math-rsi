# Exact inherited-neighborhood skips

The skips are VALID when C is a simple four-regular graph on the same 105 literal labels as Q=`extension105_d4/best.edges`, and D is the edge-set symmetric difference C△Q. They do not test unlabeled isomorphism.

If |D|=0, C is the old saved graph. If |D|=4, equal vertex degrees force two removed Q edges and two added edges. The removed edges cannot share a vertex: on three vertices their degree pattern (2,1,1) has only the original simple two-edge realization. Thus they are disjoint, and the new edges are one of the two alternate pairings. Every legal such graph was covered by the old 40,740-case ordinary two-edge-switch enumeration.

Let U={12,13,41,44,48,49,52,53,104}. If every edge of D has both endpoints in U, every outside or boundary edge remains fixed. Reading the actual Q, fixed edge file and inputs confirms that the fixed 202 edges form a subset of Q, contain no internal U edge, and leave exactly the eight listed free edges. Four-regularity therefore fixes the residual degrees to (4,4,1,1,1,1,1,1,2) in the stated U order. Every simple internal realization was included among the old 230 completions.

The input receipt is in `SKIP_SCOPE.json`. No candidate or old neighborhood was generated, and no BFS or solver ran. Producer code was not yet present during this review, so this is a paper and input check rather than an implementation claim.
