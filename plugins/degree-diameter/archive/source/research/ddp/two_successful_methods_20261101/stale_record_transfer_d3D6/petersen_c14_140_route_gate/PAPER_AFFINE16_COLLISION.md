> Actual closure: all seventeen required deletion matrices are now bound by `AFFINE_F16_RANK_RESULT.json` and the complete proof is in `PAPER_AFFINE16_NO_PROOF.md`. The conditional derivation below is preserved as its earlier prediction.

# Conditional scalar-affine F16 obstruction via seventeen-map collisions

This is a paper statement only. No F16 tables, slope assignments, ranks, words, cover graph, BFS, solver or Lean run are evaluated here. Actual nonadjacent17-word and difference-rank certificates must be supplied separately.

## Exact collision lemma

Let f_i(x)=a_i x+b_i for i=1..17 be affine functions on F16 (in the cover application every a_i is nonzero). Assume that for every x the seventeen outputs cover all sixteen field elements. For each fixed x, the output multiplicities must be exactly one double and fifteen singles. Thus there is exactly one unordered equal-output pair at each x, and the total number of collisions over all sixteen x is16.

Let d be the number of unordered pairs of identical functions. Such a pair contributes16 collisions. Two functions with the same slope and different intercepts contribute0; two with different slopes contribute exactly1. If C counts different-slope pairs, then

16d+C=16.

There are only two cases:

- d=1,C=0: all seventeen slopes agree, and exactly one function-pair is identical;
- d=0,C=16: the slope-class sizes are16+1.

For the second claim, if the largest slope class has size≤15, the maximum possible sum of squared class sizes is15²+2², so the number of cross-class pairs is at least(17²-15²-2²)/2=30. The only nonconstant partition with16 cross pairs is16+1.

The lemma is sharp, not an obstruction by itself. The sixteen functions x↦x+b, one for each b∈F16, already cover the field for every x; adding one affine function with a different nonzero slope gives the16+1 case. Adding a duplicate of one translation gives the all-same-slope case. Merely observing seventeen maps therefore does not rule out coverage. Testing only x=0 would also be insufficient to establish the lemma's premise.

## Spanning-tree gauge and the rank bridge

For scalar-affine edge bijections over the fixed Petersen graph, independent affine changes of coordinate at vertices can make all nine spanning-tree edge maps the identity. Six arbitrary cotree affine maps remain. Their six slopes lie in F16*, a cyclic group of order15. Choose one multiplicative generator and write their exponents as s∈(Z/15)^6.

The slope of a literal word with signed cotree coefficient vector c is the generator raised to c·s. This follows from the scalar linear part of composition; translations do not affect slopes. The gauge changes all word slopes in a fixed ordered endpoint slot by the same nonzero vertex-factor, so equality of those slopes is preserved.

Choose one actual ordered nonadjacent Petersen pair, with its complete seventeen length≤6 reduced words. By the collision lemma, deleting a possible outlier leaves sixteen equal slopes (if all seventeen slopes agree, any deletion works). For each possible deleted index k, choose one remaining reference vector and form the15×6 integer matrix D_k of differences of the other remaining word vectors.

A sufficient finite certificate is: **for every one of the seventeen possible deleted indices k, D_k has column rank6 both modulo3 and modulo5**. It is not enough to check just one arbitrarily deleted index, because the exceptional word is unknown. Under this certificate, whichever k the coverage lemma supplies, D_k s=0 mod15 implies s=0 mod3 and s=0 mod5, hence s=0 mod15. Every cotree slope is1, as are all tree slopes.

The cover is now translation-only on the additive group of F16, which is F2^4. The already established inverse-word argument applies: the actual25 closed reduced words at a controller consist of the empty word plus twelve inverse pairs. Their images contain at most13 return labels, fewer than16. Thus, if the stated actual17-deletion rank certificate is bound, no scalar-affine F16 cover of this fixed Petersen base can have diameter≤6.

This is conditional on the finite rank inputs. It does not assert those ranks, classify any existing cover, or transfer a characteristic-three construction. It does not exclude general16-permutation covers or higher-dimensional affine models with unrelated word linear parts. No new field or voltage-assignment search is requested by this note.
