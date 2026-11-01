# Twenty-one vertices with at least two degree-six points

2026-10-13. Complete paper candidate under the established permutation/quota lemmas. H is simple, pair-covering, five-uniform, has 21 vertices and 34 edges, and has minimum degree six with at least two degree-six vertices. We prove Property B. This is not yet a Lean theorem.

Write λ for codegree and τ for common-three multiplicity. Every degree-six point x satisfies

$$\sum_{v\ne x}(\lambda(x,v)-1)=4,$$

by pair coverage and $\sum_{v\ne x}\lambda(x,v)=4d(x)=24$. In particular a pair incident to a degree-six point has codegree at most five.

## 1. Three low points

Choose distinct degree-six vertices x,y and a minimum-degree vertex z outside them. Its degree is at most eight, since otherwise $6+6+19\cdot9>170$.

A pair of codegree at least five incident to a degree-six vertex immediately has a strict two-lock bound (the retained double witnesses cover partner degrees six, seven and eight). We may therefore take all pair codegrees among x,y,z in {1,2,3,4}. They satisfy the excess constraints: any two pair codegrees at a degree-six point have sum at most six. Enumerate $0\leq\tau(x,y,z)\leq\min\lambda$ and retain precisely nonnegative exact trace counts.

The complete local domains are:

| Degrees | Profiles | Residual profiles |
|---|---:|---:|
|(6,6,6)|90|0|
|(6,6,7)|103|0|
|(6,6,8)|105|4|

The four residuals, with pair order (xy,xz,yz), are

$$(1,1,1;\tau=0),\quad(2,1,1;\tau=0),\quad(2,1,2;\tau=1),\quad(2,2,1;\tau=1).$$

Thus only the case where x,y are the two six-degree vertices and all other vertices have degree at least eight remains. Let L be the eight-degree set. Its size is at least thirteen: the baseline degree total is $6+6+19\cdot8=164$, leaving only six excess degrees. The triple argument applies to each z∈L, so λ(x,y) is either one or two.

## 2. The unit xy case

If λ(x,y)=1, the residual list forces λ(x,z)=λ(y,z)=1 and τ(x,y,z)=0 for every z∈L. If z,w∈L have codegree at least three, the strict (6,8,8) triple (x,z,w) from the frozen unique-six reduction applies. Therefore suppose every L-pair has codegree one or two.

Select (x,y,z,w). Its degrees are (6,6,8,8), pair codegrees are $(1,1,1,1,1,b)$ with b∈{1,2}, and every common triple containing x,y vanishes. The four-lock table is strict except for b=2 with every common triple and quadruple zero. Hence, if no selected strict witness applies, no edge through x can contain two L points. Its six incident edges can cover at most six L points, contradicting |L|≥13 and pair coverage with x.

## 3. The double xy case

Suppose λ(x,y)=2. The excess identity at x leaves at most three nonunit neighbors besides y, and similarly at y. Hence

$$U=\{z\in L:\lambda(x,z)=\lambda(y,z)=1\}$$

has size at least $13-3-3=7$. The three-lock residual list gives τ(x,y,z)=0 for every z∈U.

As before, a U-pair of codegree at least three has a strict (6,8,8) witness with x. The (6,6,8,8) four-lock table is strict whenever the U-pair has codegree one. Consequently all pairs within U may be assumed to have codegree exactly two.

The two edges containing x,y contain no U point. The other four edges through x must cover all at least seven U points. Some such edge therefore contains two distinct U points u,v. Choose any third U point w. The locks (x,y,u,v,w) have degrees (6,6,8,8,8), with pair-codegree vector in lexicographic index order

$$(2,1,1,1,1,1,1,2,2,2).$$

All traces containing x,y and an additional lock vanish. At least one edge contains x,u,v, so its common-three multiplicity is one (bounded by λ(x,u)=1). These conditions leave exactly fourteen nonnegative exact-trace profiles. Every one has a strict five-lock bound, the largest being $102547/102960<1$.

This completes the remaining case and proves the stated branch.

## Exact evidence and scope

`TRIPLE_LOW.json` records the complete three-lock domains; `TWO_SIX_QUAD.json` records fourteen four-lock profiles (nine strict, five explicitly used residues); `TWO_SIX_FIVE.json` records the fourteen final profiles. The five-lock generator fixes all ten pair codegrees, enumerates only higher exact traces within their pair capacities, reconstructs singletons from degrees and the empty trace from 34 edges, and filters the stated actual-input conditions. This is local classification, not enumeration of H.

`MULTIPLE_SIX_WITNESSES.json` collects 323 retained strict witnesses. Running `verify_exact.py MULTIPLE_SIX_WITNESSES.json` checks every A/B/C row independently by labelled injections, complete bad-slot capacity penalties, exact rational quotas, actual degrees and total edge count. All checks passed, with overall maximal bound $12151/12155$. The strong unit-root (6,8,8) witnesses for codegree≥3 are reused from the frozen `TWENTYONE_SIX_REDUCTION_VERIFIED.json` (eleven profiles, two triple multiplicities as allowed by nonnegative traces).

Useful review targets: complete coverage of the three-lock domain; orientation of the two six-degree points in its four residues; the |U|≥7 excess argument; exclusion of U from both xy-edges; and the existence of the actual x,u,v triple required by the final fourteen-profile classification. No claim is made here about the unique-six/with-seven cases, minimum degree seven or eight, or the full T34 theorem.
