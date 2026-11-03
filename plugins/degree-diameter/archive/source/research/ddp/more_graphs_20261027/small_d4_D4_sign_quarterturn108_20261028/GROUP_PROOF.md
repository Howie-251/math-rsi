# Exact scope of the sign-action comparison

Let J(x,y)=(-y,x) over F3 and A=diag(J,-1). Since A^4=I, the operation

    (v,z,j)*(w,t,k)=(v+J^j*w,z+(-1)^j*t,j+k)

is the semidirect-product law on F3^3 semidirect C4. Coordinates have encoding x+3y+9z+27j. Its true inverse is

    (v,z,j)^-1=(-J^-j*v,-(-1)^j*z,-j).

The producer's complete table checks both inverse products and identity products. An inverse-closed set of four distinct nonidentity elements gives a simple undirected 4-regular right Cayley graph. Left translations preserve this adjacency and act transitively; thus complete identity-radius4 coverage is equivalent to global diameter at most4. The degree4 radius3 Moore bound53 is below108, so a positive would have exact diameter4.

There are nine nonidentity involutions: phase2, arbitrary plane vector, z=0. The remaining98 nonidentity elements form49 inverse pairs. Consequently every possible four-element inverse-closed connection set occurs exactly once among 1176 two-pair sets, 1764 one-pair/two-involution sets, and126 four-involution sets. The producer explicitly checked distinct connection sets, true inverse labels, and these counts.

The only numerical quotient gate for this sign-action batch is phase C4, with27 elements over each phase. It counts all reduced source-label words of lengths0 through4, retaining four original labels and their true inverse pairing even when their phase projections coincide. Immediate inverse letters can be deleted without changing the group endpoint, so every radius4 endpoint has such a word. The total labelled count is161. Fewer than27 words in any phase strictly excludes diameter4; this is an upper bound on endpoints, not an assertion that different words give different endpoints.

For every gate passer the producer computed its generated subgroup by closure. A proper subgroup is disconnected. For every connected passer it then computed the complete identity radius4 in the actual108-element group. All such checks failed. The negative global diameters and ordinary bad-pair totals were not measured and remain null.

## Interpretation of the controlled change

For Gplus=F3^3 semidirect diag(J,+1) C4 the abelianization is C12. For Gminus, A-I is invertible on all three normal coordinates, so its abelianization is only C4. The previous C12 obstruction is therefore removed; it was not reused here. Removing that obstruction did not suffice to produce diameter4.

The complete normalization proof is inherited from [ANALYSIS_CONTROLLED_ACTION.md](../small_d4_D4_C3_times_quarterturn108_20261028/ANALYSIS_CONTROLLED_ACTION.md). Every connected Gminus quartic set consists of two inverse pairs. Conjugating an odd-phase generator removes its normal part, inverting it chooses phase1, and the centralizer F9* times F3* normalizes the other cyclic normal vector to(e1,1). Inverting the second generator identifies phase3 with phase1. Thus phases k=0,1,2 give a complete three-profile covering of the connected fixed-group family.

[CANONICAL_CASES.json](CANONICAL_CASES.json) extracts those three rows from the already completed3066-case file, without rerunning any graph. For k=0 the radius4 shells are1,4,9,20,32 and42 vertices are missing. For k=1 each odd phase has only20 labelled reduced words, below its27 lifts, and the quotient gate alone excludes it; no actual108-point BFS or distance is asserted for that row. For k=2 the shells are1,4,11,23,35 and34 vertices are missing.

This is a complete exclusion for these two specified order108 groups, rather than for all order108 groups or all graphs in the(4,4) cell. No claim of literature novelty is made: the parent is checking the existing complete quartic Cayley census separately.
