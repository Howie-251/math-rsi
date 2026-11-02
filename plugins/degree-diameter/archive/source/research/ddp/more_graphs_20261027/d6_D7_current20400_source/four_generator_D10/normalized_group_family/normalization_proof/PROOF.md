# Complete degree-four normalization in the fixed source group

The proposed 216 representatives cover every connected undirected Cayley graph of degree four on the actual source group G=(F5^2 x C17) semidirect H48. This concerns this fixed abstract group, not all groups of order 20400. Isomorphic duplicates are allowed.

Use H normal form beta^u alpha^v, with alpha beta alpha^-1=beta^-1. On V=F5^2, A=[[4,2],[1,1]], B=[[0,4],[1,4]], so A^2=3I, A^4=-I, A^8=I, B^3=I. The scalar action on C17 is chi(alpha)=5 and chi(beta)=1. In particular A has irreducible characteristic polynomial X^2-3 over F5.

## Why a connected four-set has two inverse pairs

H has exactly one involution, alpha^8. Its action on V is I. Since N has odd order, any involution of G projects to alpha^8 and its V coordinate must satisfy 2v=0, hence v=0. Four involutions cannot generate the C16 quotient.

Suppose instead there are two involutions and one noninvolution inverse pair. Generation of C16 forces the pair's alpha exponent to be odd. First conjugate by a beta power to remove its beta component. For odd a, both I-A^a on V and 1-5^a on C17 are invertible. Conjugation by N therefore removes both normal coordinates of that generator. The involutions still have V coordinate zero: beta and alpha conjugation preserve zero, and N conjugation adds (I-rho(alpha^8))t=0 to their V coordinates. Thus all generators have V coordinate zero after this conjugation. They cannot generate G. These exhaust the inverse-closed four-set types other than two inverse pairs.

## Normalizing two inverse pairs

At least one generator has odd alpha exponent a. Invert that generator if necessary to choose a in {1,3,5,7}. A beta conjugation removes its beta component, then the unique N conjugation removes its normal coordinates. It is now g=(0,0,alpha^a).

The second generator must have a nonzero beta exponent, or the H images do not generate H. Conjugation by alpha changes its beta exponent's sign and leaves g fixed, so choose the exponent to be 1. Inverting the second generator sends b to -b modulo 16. Its beta exponent becomes -(-1)^b; an alpha conjugation restores it to 1 whenever needed. Hence b may be restricted to {0,...,8}, while g remains unchanged. The resulting normal vector and C17 coordinate remain nonzero in any connected instance. If either were zero, that normal factor would not be generated.

Independent multiplication of V by an element of F5* and of C17 by an element of F17* commutes with the H action and is a group automorphism. Normalize the C17 coordinate to 1 and the first nonzero coordinate of the V vector to 1. There are six directions: (0,1) and (1,t) for t in F5.

Thus the representatives are

    {g,g^-1,h,h^-1},
    g=(0,0,alpha^a), h=(v,1,beta alpha^b),
    a in {1,3,5,7}, b in {0,...,8}, v in P1(F5),

with count 4*9*6=216. Every operation used is either a group automorphism or inversion/reordering of a generating pair.

## All 216 representatives are connected

Since a is odd, g generates alpha. Multiplying h by alpha^-b gives k=(v,1,beta). Since I+B+B^2=0 and beta acts trivially on C17, k^3=(0,3,identity), which generates C17. Remove this coordinate from k. Conjugation by alpha^2 acts as 3I on V and centralizes beta, so (alpha^2 k alpha^-2)k^-1=(2v,0,identity). This is nonzero. Its alpha orbit spans V because X^2-3 is irreducible over F5. Removing the normal coordinate from k then gives beta, so the generated subgroup contains N and H. The four elements are distinct because the two H images have beta coordinates zero and nonzero, and each first generator has order 16.

## Previously evaluated source controls

The algebraic checks in control_normalization_checks.py identify the old AB, AC, BC inverse-pair subsets with (a,b,v)=(1,4,(1,4)), (1,5,(1,1)), and (5,4,(1,3)) respectively. Their previously measured diameter 11 is inherited from ../../RESULT.json. No diameter test was repeated for this proof. The unique producer can skip these three representatives and test the remaining 213. No other case is skipped by this argument.

This file records an algebraic coverage theorem and three literal normalization chains. It performs no graph generation, BFS, or generating-set search. The finite-family producer owns the actual diameter conclusion and its own terminal files.
