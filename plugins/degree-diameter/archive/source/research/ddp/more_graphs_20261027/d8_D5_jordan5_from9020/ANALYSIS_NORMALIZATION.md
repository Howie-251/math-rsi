# Complete module normalization for the specified Jordan frame

The actual source recipe in `../d9_D5_current9020_source/AUTHOR_construction.json` uses LEFT action and positive normal/phase pairs `(1,1),(316,6),(13,7),(426,9)` in `Z451 semidirect_46 C20`, plus the involution y10. Modulo11 these four pairs are `(1,1),(8,6),(2,7),(8,9)`. The proposed degree-eight frame removes the involution and keeps exactly those projected pairs. Its module V is F5^2, with `A_lambda=[[lambda,1],[0,lambda]]`, lambda2 or3.

Use coordinates `(n,v,j)` and law

`(n,v,j)(m,w,k)=(n+2^j*m, v+A^j*w, j+k)`.

The normal factors are C11 and V, and the phase is C20. The order is5500. Every specified generator phase and inverse phase is distinct: `[1,6,7,9]` versus `[19,14,13,11]`. Thus every vector assignment defines a simple8regular Cayley recipe, with22000 edges if generated. This alone asserts no diameter.

## Exact-order20 representation scope

Put `N=[[0,1],[0,0]]`, so A=lambda*I+N and N^2=0. The identity `A^k=lambda^k*I+k*lambda^(k-1)*N` gives A^20=I, while `A2^4=I+2N` and `A3^4=I+3N` have order5; A^5=lambda*I has order4. Hence both A have exact order20. Also A-I is invertible because lambda is not1.

These are precisely the two GL2(F5) conjugacy classes of matrices of exact order20. A semisimple split element has order dividing4; an irreducible semisimple element has order dividing24. Neither admits order20. A nonsemisimple element has one Jordan block with eigenvalue lambda in F5*, and order `5*ord(lambda)`, which is20 exactly for lambda2 or3. The two eigenvalues give distinct conjugacy classes. This classification does not cover matrices of other orders or different phase/action frames.

## Removing module gauge without losing a connected case

Let the four free module vectors be v1 through v4. Conjugation by the module translation `(0,c,0)` changes vi to `vi+(I-A^ji)c`. Since j1=1 and A-I is invertible, `c=(A-I)^-1*v1` uniquely makes v1=0. This operation leaves the C11 coordinates untouched. Any further module translation preserving v1=0 is zero.

The invertible matrices centralizing A are exactly

`B=[[a,b],[0,a]], a!=0`.

They form a20-element group. A vector `(x,y)` is cyclic for A exactly when y!=0, since `det(v,Av)=-y^2`. The centralizer acts simply transitively on these20 vectors. Explicitly the unique matrix sending v to e2 is `a=y^-1,b=-x*y^-2`.

After v1=0, choose the first cyclic vector among v2,v3,v4 and send it to e2. Earlier vectors must lie in the invariant line L=span(e1); later vectors are arbitrary. The three strata therefore have

- first cyclic v2: `25^2=625` representatives;
- first cyclic v3: `5*25=125`;
- first cyclic v4: `5^2=25`.

The total is775 for each lambda,1550 across the two specified classes. Equivalently `(25^3-5^3)/20=775`. The centralizer fixing e2 is trivial, so there is no missing residual basis choice. This is a complete covering list under the stated module conjugacy/centralizer normalization, not a claim that all1550 graphs are pairwise nonisomorphic under every possible automorphism.

If all remaining vectors lie in L, every generated module coordinate stays in L and the full5500vertex graph is disconnected. Such tuples are correctly omitted.

## Every retained tuple is connected: isolate the translations first

After normalization write the generators as gi with v1=0, j1=1. The word `zi=gi*g1^(-ji)` has phase zero and lies in C11 x V. Because every power of g1 has module coordinate zero, the module coordinate of zi is exactly vi. Raising zi to the eleventh power kills its C11 component and multiplies its V component by11, which equals1 in F5. Thus

`zi^11=(0,vi,0)`.

This genuinely isolates pure module translations. A retained cyclic vi and its conjugate Avi span V, so the generated subgroup contains all of V.

The projection onto `C11 semidirect_2 C20` is onto: g1 has phase1, and g1g3 versus g3g1 have the same phase8 but normal coordinates5 and9. Their quotient gives a pure normal coordinate7 modulo11, generating C11. Therefore the subgroup contains the full kernel V and maps onto the entire220-element quotient; it is the whole5500-element group. Connectivity is proved without a graph BFS and is not inferred from A's order alone.

## Coverage remains a separate question

The unique controller DP in `controller_capacity/` removes the involution and uses eight true inverse darts. It counts22409 prefixes through length5, with minimum78 at first slot110 `(phase10,normal11=0)`, so the necessary25-point module capacity gate passes. That slot is the location of the deleted source involution, making it a natural preselected module-image gate. This is not a module-image or full diameter certificate.

The proof closes the normalization and connectivity obligations for the fixed source C11 coordinates/phases and the two exact-order20 Jordan classes only. It does not inherit diameter5 from the degree-nine source, cover other action orders or alter the projected generators. This analysis generated no module vectors, parameter graphs or BFS; only the separate raw DP was executed.
