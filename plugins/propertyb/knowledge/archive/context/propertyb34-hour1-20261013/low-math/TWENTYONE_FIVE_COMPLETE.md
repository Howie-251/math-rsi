# T34 on 21 vertices: the complete minimum-degree-five branch

2026-10-13 first-hour sprint. Complete paper candidate; no Lean result. This replaces the previously failing (5,8,8) placement route with a fourth lock and actual incidence constraints.

## Target, assumptions, invariant object

H is simple, pair-covering and five-uniform, with 21 vertices and exactly 34 edges. Suppose x has degree five. Total degree is 170. Pair covering and `sum_(v≠x) λ(x,v)=4*5=20` imply λ(x,v)=1 for every other vertex. Consequently the five edges through x partition the other twenty vertices into five blocks of four after deleting x.

We control the established locked-permutation failure bound `sum min(A,B,C-D)`. Every strict local witness uses the existing probability and bad-link quota lemmas. When a witness fails, the proof retains its exact structural consequences instead of treating the numerical failure as a counterexample.

## Notation and derivation map

λ is pair codegree and τ is common-edge multiplicity of three points. Exact trace multiplicities relative to three or four locks are recovered by inclusion-exclusion from degrees, codegrees and larger traces.

1. A second vertex of degree five or six gives a strict triple witness.
2. Otherwise split by the number r of degree-seven vertices.
3. For r≥3, all residual sevens share one x-edge; a four-lock witness passes.
4. For r=2, add an eight-degree point outside that shared x-edge.
5. For r=1 and r=0, exact four-lock residuals force too few incidences to cover the many eight-degree points.

## Main derivation

### 1. Another point of degree five or six

Let y be a minimum-degree point outside x. If d(y)=5 or 6, choose z of minimum degree outside x,y. Necessarily `d(y)≤d(z)≤8`: otherwise the other nineteen vertices would already have total degree at least 171, exceeding the full degree budget after adding x,y.

For d(y)=5, all three pair codegrees are one, with common triple multiplicity zero or one. For d(y)=6, λ(x,y)=λ(x,z)=1, `1≤λ(y,z)≤6`, and the common triple multiplicity is zero or one; nonnegative exact trace counts exclude impossible combinations. Every such (5,5,d(z)) or (5,6,d(z)) profile has a strict triple witness in `TWENTYONE_FIVE_VERIFIED.json`.

From now on x is the unique degree-five point, and every other vertex has degree at least seven. Let r be the number of degree-seven points and L the degree-eight set.

### 2. Three or more seven-degree points

For any two seven-degree points y,z, the (5,7,7) triple is strict except when `λ(y,z)=2` and `τ(x,y,z)=1`. Thus if no strict witness applies, every pair of seven-degree points shares its unique x-edge. All seven-degree points therefore lie in the same edge through x, and r≤4.

If r≥3, select any three of them with x. The full four-point common multiplicity is one. The only remaining large exact trace parameter is the three-seven trace outside x, which is zero or one. Both (5,7,7,7) profiles pass, with bounds `12119/12155` and `4617/4862`.

### 3. Exactly two seven-degree points

Let y,z be the two sevens. The preceding triple argument again either finishes the proof or gives λ(y,z)=2 and τ(x,y,z)=1. The other eighteen points are at least eight-degree; the baseline degree total is `5+2*7+18*8=163`, leaving seven extra incidences. Thus |L|≥11.

The common x,y,z edge contains at most two points of L. Choose w∈L outside it. Then τ(x,y,w)=τ(x,z,w)=0 by uniqueness of the edges through each x-pair. If λ(y,w) or λ(z,w) is at least three, the corresponding (5,7,8) triple has a strict witness. Otherwise both codegrees are one or two, and the resulting (5,7,7,8) four-lock domain has eight profiles. All eight are strict; their maximal bound is `12151/12155`.

### 4. Exactly one seven-degree point

Let y be that point. The other nineteen points are at least degree eight. The baseline is `5+7+19*8=164`, leaving six extra incidences, so |L|≥13. Remove from L the at most three points in the unique edge containing x,y, and call the remaining set S. Then |S|≥10.

For z∈S, τ(x,y,z)=0. If λ(y,z)≥3, the (5,7,8) triple is strict. Thus suppose all these codegrees are one or two. For any distinct z,w∈S, λ(z,w)≥3 gives a strict (5,8,8) triple with x, regardless of its allowed common triple multiplicity. Hence assume λ(z,w)∈{1,2}.

The complete (5,7,8,8) four-lock domain with τ(x,y,z)=τ(x,y,w)=0 now has a strict witness except for one profile: all x-pair codegrees are one, λ(y,z)=λ(y,w)=1, λ(z,w)=2, and every common triple/quadruple multiplicity is zero.

If no strict witness applies, this same residue holds for every pair z,w∈S. Every point of S is therefore a unit neighbor of y, while no edge contains y and two points of S. The seven edges through y can cover at most seven points of S, contradicting |S|≥10.

### 5. No seven-degree points

All twenty vertices other than x now have degree at least eight. The baseline is 165, so |L|≥15. Any pair of L with codegree at least three is handled by the strict (5,8,8) triple with x. Therefore assume every L-pair codegree lies in {1,2}.

For any three distinct y,z,w∈L, the (5,8,8,8) four-lock domain consists of 62 labelled profiles. Fifty-seven have strict bounds. Every one of the five residuals has common-four-point multiplicity zero. Thus, unless a strict witness has supplied a coloring, no edge containing x can contain three points of L.

Every edge incident to x contains at most two points of L. Its five incident edges can cover at most ten such points, while λ(x,v)=1 for all v∈L and |L|≥15. This contradiction completes the last branch.

## Exact verification and classification

`verify_twentyone_five.py` re-evaluates the retained strict bounds, compares every A/B/C row with the independent labelled-injection implementation, and checks rational avoided-lock certificates from their actual capacities, weights, quotas and penalties. In particular the x-center may have no positive quota; its zero deduction is recorded and independently checked as zero, without invoking an empty LP.

`TWENTYONE_FIVE_VERIFIED.json` contains the retained exact witnesses and the explicitly handled residuals. Raw exploratory domains are `TWENTYONE_FIVE_LOW.json`, `TWENTYONE_FIVE_QUAD.json`, and `TWENTYONE_FIVE_SEVENS.json`. These are local trace classifications using the same nonnegative inclusion-exclusion formulas as the 20-vertex notes. They do not enumerate 21-vertex hypergraphs.

## Status and boundaries

COHERENT AS STATED as a complete paper candidate for minimum degree five on 21 vertices. Cases with minimum degree six, seven or eight remain unclosed in this hour's work. New Lean implementation, formal actual-input connections, and final review are still required. In particular this note does not claim the whole 21-vertex branch or T34.
