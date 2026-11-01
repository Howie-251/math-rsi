# T34 on 20 vertices: exactly two degree-seven points

2026-10-13 first-hour sprint. Complete paper candidate for this degree branch, using actual trace constraints to rule out the only surviving local profile.

## Target and invariant object

Prove Property B for simple pair-covering five-uniform H with 20 vertices, exactly 34 edges, minimum degree seven, and exactly two degree-seven vertices x,y. We continue to bound greedy-coloring failure by `sum min(A,B,C-D)`.

## Assumptions, notation, and degree budget

Write L for the degree-eight points and λ for codegree. The degree-sum baseline is `2*7+18*8=158`; the remaining surplus is 12. Hence at least `18-12=6` vertices have degree exactly eight: `|L|≥6`.

All probability witnesses below use established conditional-permutation counts and pure/total or avoided-lock subfamily bad-pair quotas. A finite profile that passes is sufficient; if it does not pass we retain it and use actual structural constraints.

## Derivation strategy and map

Good pairs and triples restrict the codegrees. Four locks reduce the remaining possibility to a single exact profile. Requiring this same profile for every pair of points in L then contradicts the actual seven incident edges at x.

## Main derivation

If λ(x,y)=1, the known unit (7,7) bound is strict. If λ(x,y)≥4, use a strong (7,7) double witness. If λ(x,y)=3, choose z∈L: either a (7,8) codegree is at least four and its double witness passes, or all three codegrees lie in {1,2,3}; every resulting (7,7,8) triple profile with λ(x,y)=3 has a strict witness. Thus assume λ(x,y)=2.

For each z∈L, a (7,8) codegree at least four is again a strict double. For codegrees in {1,2,3}, the exact (7,7,8) triple table is strict except these cases:

1. `λ(x,z)=λ(y,z)=1` and no edge contains x,y,z;
2. `λ(x,z)=λ(y,z)=2`, with arbitrary allowed triple multiplicity.

Suppose some z∈L is of the second kind. Choose another w∈L. A codegree λ(z,w)≥4 gives a strict (8,8) double. Otherwise λ(z,w)∈{1,2,3}; the four-lock table of degrees (7,7,8,8), with the two cross-codegrees for z equal to two and those for w equal to one or two, is strict for every allowed exact trace profile. This finishes that case.

We can therefore assume every z∈L is of the first kind: it has unit codegree with each of x,y, and no edge contains x,y,z.

Take distinct z,w∈L. If λ(z,w)≥4, use a strong (8,8) double. If λ(z,w)=1 or 3, all corresponding four-lock profiles pass. For λ(z,w)=2, the pure/total table plus the existing avoided-lock dual certificates passes every actual profile except the following one:

`λ(x,y)=2`, `λ(z,w)=2`, all four cross-codegrees are one, and **every exact trace of size three or four has multiplicity zero**.

Thus, unless a strict probability witness has already supplied a coloring, this residual must hold for every distinct z,w∈L. Consequently no edge containing x can contain two points of L. Also, the two edges containing both x and y contain no point of L, by the preceding triple restriction. Only five of the seven edges incident to x can therefore meet L, and each meets it in at most one point.

But λ(x,z)=1 for every z∈L, so these five edges must cover all of L. This gives `|L|≤5`, contradicting `|L|≥6`.

## Exact verification

`verify_seven_two.py` recomputes every retained witness needed by this argument, checks strictness, and compares every A/B/C row to the independent labelled-injection implementation. For avoided-lock certificates it additionally recomputes each quota, nonnegative rational dual multiplier, type-pair capacity, two-direction weight, and capacity penalty exactly. Numerical linear programming only proposed multipliers; the retained rational inequality is checked without assuming LP optimality.

The output `SEVEN_TWO_VERIFIED.json` contains the strict witnesses and the single surviving exact four-lock profile. `QUAD_MIXED.json` and `DUAL_REFINEMENT.json` retain the earlier pure and dual calculations separately. The residual bound is greater than one, so it is eliminated only by the preceding actual-H argument, not by pretending its probability bound passed.

## Status and boundaries

COHERENT AS STATED as a paper candidate. This closes minimum degree seven with exactly two seven-degree points at the mathematical-candidate level. Together with `SEVEN_MANY.md`, only the unique-seven case remains within minimum degree seven. Minimum degree eight, other vertex numbers, formalization, and final theorem assembly remain separate open obligations.
