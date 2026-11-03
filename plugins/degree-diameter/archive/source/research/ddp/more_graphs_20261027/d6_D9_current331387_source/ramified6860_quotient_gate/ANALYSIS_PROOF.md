# Z6860 semidirects: a uniform abelian-quotient obstruction

## Stronger paper closure, added after the retained fixed-vector audit

Let `G_r=Z6860 semidirect_r C49` for ANY valid action, so r is a unit and `r^49=1mod6860`. Reduction modulo20 has unit-group order8, and reduction modulo7 has unit-group order6. Both are coprime to49. Therefore `r=1mod20` and `r=1mod7`, hence `r=1mod140`.

Consequently every such group surjects onto the abelian group `A=C49 x C140`, of order6860. This projection is available regardless of the three generator phases, their normal coordinates, nonunit normals, or whether a source gauge normalization exists.

For ANY three inverse pairs in an abelian group, every word of length at most9 has an endpoint represented by three signed counts with l1 norm at most9. The number of such counts is

`sum_{k=0}^3 2^k*binom(3,k)*binom(9,k)`

`=1+6*9+12*binom(9,2)+8*binom(9,3)=1159`.

Here k counts the nonzero coordinates: choose the coordinates and their signs, then positive magnitudes summing to at most9. The expression is an upper bound on distinct endpoints even when generators are dependent, repeated, self-inverse, or fail to generate A. Since1159<6860, the projected nine-ball cannot cover A. Projection cannot increase distances, so no Cayley graph on any G_r defined by three inverse pairs has diameter at most9.

This is the strengthened closed scope: **normal cyclic group Z6860, split complement C49, every valid action and every three-inverse-pair selection**. It does not depend on a completeness claim for the old normalization. It does not concern other normal moduli, unrelated groups of order336140, or arbitrary degree-six graphs. The original fixed-vector quotient witness below is preserved as a concrete control; no additional integer enumeration, BFS, graph or field image was used for the stronger lemma. The complementary `ANALYSIS_RING_SCOPE` paper records the same scope independently.

## Retained fixed-vector exact-distance witness


Let `G=Z6860 semidirect C49` use any valid action of C49, with fixed positive `(phase,normal)` generators `(1,0),(36,1),(45,1512)` and their true inverses. Since `6860=20*343`, reduction modulo20 is available. Every automorphism of Z20 has order dividing8; the image of C49 has order dividing49. Their gcd is1, so every such action is trivial on this factor. Thus the projection is a graph homomorphism onto the fixed abelian Cayley quotient

`Q=C49 x C20`, with positives `(1,0),(-13,1),(-4,12)`.

This conclusion is independent of the action on Z343. A compatible full action must be defined by CRT, not by copying an integer that fails to be a unit modulo20.

In this abelian quotient a word of length at most9 gives signed generator counts a,b,c satisfying

`|a|+|b|+|c|<=9`, `b+12c=10 mod20`, `a-13b-4c=0 mod49`

if it reaches `(0,10)`. Conversely, any such counts produce a quotient word of their l1 length. Necessarily `-9<=c<=9`. The allowed interval for b has width at most18, so at most one representative of its residue modulo20 can fit. The bounded19-row audit in `RESULT.json` leaves exactly the following positive c; negative c has the same cost by negating all three counts, since10=-10mod20.

| c | b | least-absolute a | minimum total cost |
|---|---|---|---|
| 1 | -2 | -22 | 25 |
| 2 | 6 | -12 | 20 |
| 3 | -6 | -17 | 26 |
| 4 | 2 | -7 | 13 |
| 6 | -2 | -2 | 10 |

For c=0 the least possible |b| is10. For |c|=5,7,8,9 the required |b| already exceeds9-|c|. All other c are outside the nine-step budget. Thus there is no route of length at most9.

The counts `(a,b,c)=(-2,-2,6)` have total cost10, phase `-2+26-24=0`, and normal coordinate `-2+72=70=10mod20`. They give a ten-step route, proving **the target's exact quotient distance is10**. This is not a claim that Q or the full graph has diameter exactly10.

Projection cannot increase distance. Therefore every compatible full-group Cayley graph with this fixed vector fails diameter9 before it is generated. In the hypothetical336140-vertex graph, the343 vertices `(phase0,normal10+20k)`, `0<=k<343`, all project to this target and lie outside the identity radius9. This is a conditional root-fibre obstruction, not an ordinary unordered bad-pair count or a measurement on the published331387 source.

The parent proposed the integer certificate before its finite audit. Only19 integer rows and the explicit witness were checked; no graph, quotient BFS, source BFS, field image or word list was produced. This fixed-vector audit alone had that narrower scope. The subsequently proved abelian-quotient lemma above now excludes every three-pair choice within the same Z6860/C49 semidirect class. Other ring moduli, unrelated groups and general (6,9) constructions remain outside the result.

Independent ring/action scope review: [ANALYSIS_RING_SCOPE](../ANALYSIS_RING_SCOPE.md).
