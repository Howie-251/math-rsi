No substantive gap in the requested range. The §3.3 forbid-w step, the three new fractions, the five-high excess-3 caller, and the pure-pair reduction to one degree-8 point all hold. This does not accept m(5)≥36.

Nothing was executed. The fractions below were recomputed by hand.

**Read.** `SIX_POSITIVE_SIX_TRIPLES_REPAIR.md` whole. `SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md` §C, together with the A.1–A.3 and B.2–B.7 passages §C cites. `TWENTYFOUR_FIVE_HIGH_ANALYTIC.md` whole. `TWENTYFOUR_SIX_HIGH_TWO_INTERNAL.md` whole, with the audit on §§2–4 and §9; §§5–8 were not re-proved. Corollary A/B statements in `FIVE_POSITIVE_SIGNED_REPAIR.md` were checked only as the cited repair interface.

## Six positive, six triples

The lemma holds for at most six indexed positive 4-sets, six negative triples, 35 negative quads, and total occurrence at most 7, on any finite ground.

Low occurrence is the double-incidence budget. At most 12 double points, each in at most five negatives, give budget 60. Triples hold at most 18 of those incidences, so the chord puts 18 on triples and 42 on quads. Then

6q³+35q⁴+18α₃+42α₄ = 6p³+(21/2)p⁴+(49/2)q⁴ = 128821/131072 < 1,

with p=7/16 and q=1/4. The α₃>α₄ allocation is the same convex chord as in the seven-positive low-occurrence argument.

Occurrence at least 4 leaves at most two unhit 4-sets. A red set of size at most 2 meets no negative. Two disjoint unhit sets give 16 three-point candidates, and triples through the fixed point number at most 7−aₓ≤3.

Occurrence exactly 3 with at most two unhit sets gives the same 16 candidates against at most four negative indices through x. Three pairwise disjoint unhit sets give 64 four-point candidates against at most 6·4+4=28.

The swap is forced only when all four {x,y,z}, z∈A, are negative triples. Those four indices contain x, so making x blue discards them. It does not replace any of them by a smaller negative. At most two triples remain. The point y already has two positive occurrences and these four negative occurrences, so its remaining negative budget is r+b≤1.

§3.3 is the case where that remaining budget is exactly the one triple T={y,z,w}. Keeping y and z red and forbidding w is the right distinction: U and V are positive, so w is deleted and the remainders, each of size at least 2, must still be hit; T contains w, so T is discarded and is not replaced by {y,z}. If the remainders still meet at u, then {y,z,u} has size 3, is not T, cannot contain a quad, and cannot contain a triple that misses y. If the remainders are disjoint, they give at least four four-point candidates. None contains T. There is no quad through y. A quad that misses y is not contained in a four-point set that contains y. The only possible blocker is the at most one remaining triple that misses y, and that triple blocks at most one candidate.

§3.4 then has the three shrunk 3-sets and A. The 108 five-point candidates meet at most 16r+4(2−r)+4b+(35−b)=43+12r+3b≤55. The 16 is a size-4 majorant; on sizes 3,3,3,4 the true maximum for a triple through y is 12, and 55<108 either way. Quads through the already-forbidden x are counted inside the 35 and cannot meet a candidate that avoids x.

## Section C only

The old double-incidence budgets stay 60 and 70, and the triple cap stays 12. Raising the quad cap from 22 to 35 does not move the optimum, because 4·22 already exceeds the residual 48 or 58. Only the baseline grows, by 13q⁴=13/256. The resulting bounds are

4p³+12p⁴+23q⁴ = 14163/16384,

4p³+(29/2)p⁴+(41/2)q⁴ = 124029/131072.

Both are strictly below 1. They are the old values 53324/65536 and 117373/131072 plus 13/256.

In the six-positive high-occurrence warmup, three-point candidates and the 64-candidate bound use only triples and quads through the fixed point. After the swap every triple contains the newly blue point, so the 27-candidate and 9-candidate branches are blocked only by the at most one quad through y. The disjoint 108-candidate branch becomes 4b+(35−b)≤38<108 for b≤1.

In the seven-positive argument, B.2’s bound 19 is local: at most three quads through a point of positive occurrence at least 4. B.3’s sets of size at most 4 contain the fixed red point, while every active quad misses that point, so those branches stay safe. Its disjoint branch has at least 81 candidates and each active quad blocks one, so 35<81. B.4’s disjoint branch becomes 4·16+35·4=204<256. Its triple-point branch calls this extended B.3. For t=0,1,2 the blocking count is as+u+v+b, and only quads through both fixed points appear; equality still routes to B.3. For t=3 at most one quad contains x. For t=4 none does, and the argument calls B.3.

## Five high points

The degree sum is 175, the 19 outer points contribute 133, and the five high degrees sum to 42. Their excess over 8 is 2, so the spectrum is (10,8,8,8,8) or (9,9,8,8,8). At least three points have degree 8, and at most two do not.

If P is not an edge, color P red and the outer 19 points blue. Every edge meets P, and the only 5-subset of P is P itself, so every edge also meets the outer set.

If P is an edge, it is the unique internal edge. The other 34 edges carry 37 incidences with P, hence total trace excess 3. The only solutions are three pairs, one triple plus one pair, or one four-trace, with 31, 32, and 33 singletons. A trace of size 3 or 4 meets at least three high points, so it contains a degree-8 point. Color that point blue and the other four high points red. The internal edge, the unique higher trace, and every pair through the blue point are already mixed.

The signed rows are then (m,t,b)=(7−s,3−s,24+s), (6−s,1−s,26+s), and (6,0,27). Every row satisfies m≤7, t≤3, and b≤27, with outer occurrence at most 7, so the §C corollary applies. No pair cover and no 650/81 catalogue enters this branch.

## Six high points, two internal edges

§1’s seven rows are the complete nonnegative solutions of n₂+2n₃+3n₄=6. Sections 3 and 4 use that list as follows.

For pure pairs, C has four points and P has only one degree-9 point, so C has a degree-8 point q. Color q blue. Both internal edges are proper, and so is every pair through q. The remaining system is exactly 6−s positive 4-sets, 6−s negative triples, and 27−m negative quads, with occurrence at most 7. That is inside the six-positive theorem. The matching, attachment, star, and 18-point local-graph arguments are not used.

For exactly one higher trace, a degree-8 point of C∩T gives at most 5−s positives, at most four triples, and at most 27 quads: the triple inventory has N₁=28 and m≥1, while the four-trace inventory has N₁=29 and m≥2. Corollary A applies. A four-trace meets C in at least two points, so it always has such a degree-8 point. A triple with no degree-8 point of C is exactly {h,a,b}. For s≥1 that choice gives at most five positives, at most three triples, and at most 26 quads, and Corollary A applies. For s=0 the system is exactly six positive 4-sets, four triples, and 22 quads, which the new six-positive theorem takes. This is the only one-higher call to that theorem.

Sections 5–8 still cite Corollary A, the two-triple Corollary B, and the zero-triple five-small lemma. They were not re-audited. Section 9 is right that the pure-pair case now depends on §3, and that the old matching proof is only an alternate. The writeup claims only the 24-point, six-high, two-internal branch under pair cover, minimum degree 7, and no all-seven edge.
