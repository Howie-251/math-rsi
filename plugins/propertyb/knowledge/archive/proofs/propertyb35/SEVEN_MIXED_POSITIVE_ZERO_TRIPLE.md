# Seven mixed positive sets and negative four-sets

Let the positive family have at most seven indexed sets, each of size3 or4, with at most one three-set. Let the negative family have at most21 indexed four-sets. Suppose every vertex's combined occurrence in the positive and negative families is at most7. Then there is a set R meeting every positive set and containing no negative set.

The ground set may have any finite size. Different indices may represent the same set; all occurrence and constraint counts retain those indices. There are no negative triples or smaller negative constraints in this statement.

## 1. A vertex occurs in at least three positive sets

Choose such a vertex x, put it in R, and let a_x≥3 be its positive occurrence. At most four positive sets remain unhit, all avoiding x and all of size at least3. At most

b_x≤7−a_x≤4

negative four-set indices contain x.

If at most two positive sets remain, choose one point from each; the resulting R has size at most3 and cannot contain a negative four-set.

If exactly three remain and two intersect, choose an intersection point and a point of the third. Together with x, this again has size at most3. If the three sets are pairwise disjoint, one point from each gives at least27 different four-point candidates containing x. A negative four-set can equal one of these candidates only if it contains x, so at most b_x≤4 candidates are bad.

Suppose exactly four remain. If an intersection point y hits at least two of them, select y as well. At most two positives remain. If at most one remains, or the two remaining sets intersect, a set of at most3 points repairs. If two disjoint sets remain, each has at least3 points and avoids x,y, giving at least9 different four-point candidates containing x,y. At most b_x≤4 can be negative four-sets.

Finally, if the four remaining sets are pairwise disjoint, their one-from-each choices give at least3^4=81 different five-point candidates containing x. A negative four-set containing x fixes three points from the four disjoint groups, and hence obstructs at most4 candidates. A negative four-set avoiding x fixes a point in every group and obstructs at most one. Thus at most

4b_x+(21−b_x)=21+3b_x≤33<81

candidates are bad. This completes the high-occurrence case.

## 2. Every positive occurrence is at most two

Independently choose a uniform point from each positive set, and let R be their union. R always hits all positive sets. For a fixed negative set B, the [joint occupancy lemma](RANDOM_TRANSVERSAL_REPAIR.md) gives

Pr(B⊆R)≤∏_(v∈B)q_v,

q_v=1−∏_(A_i∋v)(1−1/|A_i|).

The independence is between these newly chosen points; the original constraints need not be independent.

If there is no positive three-set, q_v≤p=7/16 everywhere. The bad-event sum is at most21p^4=50421/65536<1.

Otherwise let T be the unique positive three-set. For v∈T, at most one additional positive set contains v, and that set is a four-set. Hence q_v≤1−(2/3)(3/4)=1/2. For v∉T, q_v≤p=7/16. A negative four-set B contains j=|B∩T| points of T, where0≤j≤3, and its bad probability is at most

w_j=(1/2)^j p^(4−j).

This is a convex geometric sequence in j, so its values at the four integers satisfy the endpoint-chord bound

w_j≤w_0+(j/3)(w_3−w_0).

Every point of T has at least one positive occurrence, so it occurs in at most6 negative indices. Therefore

Σ_(negative B)|B∩T|≤18.

Summing the chord bound over at most21 negative indices gives

Σ_BPr(B⊆R)
≤21w_0+6(w_3−w_0)
=15(7/16)^4+6(1/2)^3(7/16)
=57519/65536<1.

Thus some choice of R avoids every negative set. If there are no positive constraints, R empty suffices. This proves the theorem.

## 3. Actual three-star caller in the six-high-point branch

Use the exact actual-H setting and labels of [the six-high-point report](../../context/propertyb35-paper/round01/twentyfive/k6_two_internal/REPORT.md): P={0,…,5} hits every edge, its degree pattern is one9 and five8, the internal edges are P−{4},P−{5}, and the six pair traces form a star centered at q∈{4,5}, with one edge qi for each i∈{0,1,2,3} and two edges45. Every outer point belongs to L=V−P and has degree7.

For the following three degree placements choose the indicated two blue P points, leaving the other P points red:

| Nine-degree point | Star center | Blue P points |
|---:|---:|---|
|0|4|{1,4}|
|0|5|{1,5}|
|4|5|{0,5}|

Both blue points have degree8. The C point belongs to two internal edges and one pair-trace edge, so it has5 private single-trace edges. The star center belongs to one internal edge and all6 pair-trace edges, so it has1 private single-trace edge. These give six indexed positive four-sets. The pair trace between the two blue points gives one positive three-set. Every other pair trace is mixed and already proper. The remaining27−6=21 private edges give negative four-sets. Both internal edges are already proper. The signed source-edge families are disjoint, so each outer vertex's combined occurrence is at most7.

The theorem supplies R⊆L. Color R red and L−R blue. Positive constraints repair precisely the all-blue risks and negative constraints avoid precisely the all-red risks; P is a hitting set, so there is no omitted zero-P edge. Thus every actual H with any of these three star degree placements is colorable.

The fourth placement, nine-degree point4 and star center4, gives seven positive four-sets plus one positive three-set and20 negative four-sets. That is eight positives and is **not** covered by this theorem. Its exact input remains recorded separately; no fourth-star conclusion is inferred here.

## 4. Exact small checks

[SEVEN_MIXED_CHECK.py](../../context/propertyb35-paper/round01/twentyfive/k6_two_internal/SEVEN_MIXED_CHECK.py) and its JSON output check every numerical branch above, the two nontrivial endpoint-chord inequalities using rational arithmetic, the two strict union bounds, and the actual indexed counts for the three stated star inputs. No hypergraph or outer-edge enumeration is used. The proof is the direct argument in §§1–2, with the explicitly cited joint occupancy lemma.
