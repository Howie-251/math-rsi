# Five positive sets of size at least two and negative four-sets

Let a finite indexed positive family have at most five sets, each of size at least2. Let a finite indexed negative family consist entirely of four-sets, with no bound on its number. Suppose every point's combined positive and negative occurrence is at most7. Then there exists R hitting every positive set and containing no negative set.

Indices are retained even when different constraints give equal sets. The ground set has no prescribed size. If there are no positive constraints, R empty suffices.

## A repeated positive point

If some point x has positive occurrence at least3, choose it. At most two positive sets remain, so choosing one point from each gives a repair of size at most3, too small to contain a negative four-set.

Otherwise suppose some x has positive occurrence2. At most three positive sets remain. With at most two, a repair of size at most3 again exists. With three, if two intersect, choose an intersection point and a point of the third; together with x the result has size at most3. If the three are pairwise disjoint, each has size at least2 and avoids x. Their point selections give at least2^3=8 different four-point candidates containing x. Since x has two positive occurrences, at most7−2=5 negative four-set indices contain it. Every bad candidate would have to equal one of these, so at least one repairs.

## Pairwise disjoint positives

It remains that the positive sets A_i are pairwise disjoint. Independently choose a uniform point from each and let R be the selected union. For x∈A_i write q_x=1/|A_i|. A negative four-set containing a point outside the positive union, or two points in one positive group, has probability zero of being contained in R. Every other negative four-set B uses four different groups and has exact probability

Pr(B⊆R)=∏_(x∈B)q_x≤(1/4)Σ_(x∈B)q_x^4,

by arithmetic-geometric mean. The active points have one positive occurrence, so each has negative occurrence at most6. Summing over the negative indices, even with repetition, gives

Σ_BPr(B⊆R)
≤(1/4)Σ_x b_xq_x^4
≤(6/4)Σ_i |A_i|^(−3)
≤(6/4)·5/8=15/16<1.

Consequently one choice avoids all negative sets and proves the theorem. The number of negatives is controlled through actual point occurrences, rather than through an assumed independent edge model.

## Forbidding exterior points in an actual caller

If a signed system initially has positive four-sets and one or two negative pairs or singletons, choose forbidden points that meet those small negatives. Removing at most two different forbidden points from each positive leaves size at least2. Discard entire negative constraints containing a forbidden point; do not retain their smaller remainders. If all remaining negatives are four-sets, occurrence only decreases and this theorem applies. The repair on the remaining ground set avoids every original small negative and every original four-set. Any such use still has to account for all original monochromatic risks and the original indexed occurrence bound.
