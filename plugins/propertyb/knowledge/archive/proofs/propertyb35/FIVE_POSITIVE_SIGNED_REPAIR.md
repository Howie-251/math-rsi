# Five-positive signed repair

These lemmas apply directly to finite signed set systems. A repair set R must meet every positive set and contain no negative set. Every constraint is nonempty and retains its index; equal sets at different indices count repeatedly in all occurrence bounds. No critical hypergraph, pair coverage, degree regularity or ground-set size is assumed.

## 1. Five positives with occurrence bound14

Positive and negative families in these lemmas retain their original edge indices. The occurrence bound counts memberships in both families, with those indices. A repair is a set meeting every positive set and containing no negative set.

**Lemma A.** Five positive four-sets, at most four negative triples, and at most28 negative four-sets have a repair if each vertex has total indexed occurrence at most14.

Proof. If the five positive sets are pairwise disjoint, choosing one point from each gives1024 different five-point candidates. A negative triple lies in at most16 candidates; a negative four-set lies in at most4. Thus at most4·16+28·4=176 candidates are bad.

Otherwise consider a vertex x in at least two positive sets. If some such x has positive occurrence at least3, at most two positives remain unhit. With zero or one remaining set a repair of size at most2 exists. If two remain and intersect, x and an intersection point suffice. If they are disjoint, their16 point-pairs give16 different repairs of size3 containing x. At most four can be negative triples, so one succeeds; negative four-sets cannot obstruct a three-point candidate.

It remains to consider maximum positive occurrence2. Choose x hitting exactly two positives; all other three avoid x. If these three are pairwise disjoint, there are64 different four-point candidates containing x, choosing one point from each. A negative triple containing x lies in at most4 candidates; one avoiding x lies in at most1. A negative four-set can obstruct only if it contains x, and there are at most14−2=12 such indexed negative sets. Hence at most4·4+12=28 of the64 candidates are bad.

If the three remaining positives are not pairwise disjoint, choose y in two of them. It hits exactly two, because maximum positive occurrence is2, and therefore y occurs in neither of the two positives hit by x. Let A be the last positive; it avoids x,y. Its four vertices give four distinct three-point candidates {x,y,z}, z∈A. Unless one repairs, these candidates must be precisely four indexed negative triples, exhausting all negative triples. In particular every negative triple contains both x and y.

Now forbid x and keep y selected. The two original positives hit by x shrink to three-sets after deleting x; neither contains y. Together with A they are three positive sets of sizes3,3,4, all avoiding x,y. If any two intersect, a point in their intersection and a point of the third, together with y, give a repair of size at most3: it avoids x, hence all the negative triples. If the three sets are pairwise disjoint, they yield36 different four-point candidates, all containing y and avoiding x. Negative triples again cannot obstruct. At y, the positive occurrence2 and the four already forced negative triples leave at most14−2−4=8 indexed negative four-sets. Each obstructs at most one candidate. Thus one succeeds. ∎

**Lemma B.** Five positive sets, each of size3 or4, at most two negative triples, and at most28 negative four-sets have a repair if each vertex has total indexed occurrence at most14.

Proof. If the positive sets are pairwise disjoint, there are at least3^5=243 one-from-each five-point candidates. Each negative triple lies in at most4²=16 candidates, and each negative four-set in at most4. Thus at most2·16+28·4=144 candidates are bad.

Otherwise choose a point x in at least two positives. If its positive occurrence is at least3, at most two positives remain unhit. With zero or one remaining, a repair of size at most2 exists. If two remain and intersect, x and an intersection point suffice. If they are disjoint, their at-least-nine point-pairs give at least nine three-point candidates containing x. At most two can be negative triples; negative four-sets cannot obstruct such a candidate.

It remains that maximum positive occurrence is2. Choose x hitting exactly two positives. Three remain, all avoiding x. If two intersect at y, then either y hits all three and {x,y} repairs, or choosing a point from the last positive gives at least three distinct three-point candidates {x,y,z}. At most two are negative triples. If the three remaining positives are pairwise disjoint, one-from-each choices give at least27 four-point candidates containing x. Each negative triple obstructs at most4, and at most14−2=12 indexed negative four-sets contain x. Total bad count is at most2·4+12=20<27. ∎

These arguments do not assume that the positive sets have small repeated-incidence surplus, that their vertices have equal degrees, or that the negative constraints are independent. Occurrence subtractions at x or y use disjoint positive/negative indexed edge families; in Lemma A's last case the four negative triples were already forced as four different sets.

## 2. At most five positives with occurrence bound10

**Corollary A.** Suppose there are m≤5 positive four-sets, at most four negative triples, and at most28 negative four-sets. If every vertex has original total indexed occurrence at most10, then a repair exists.

**Corollary B.** The same conclusion holds for m≤5 positive sets of sizes3 or4, at most two negative triples, and at most28 negative four-sets, with the same occurrence bound10.

If m=0, take R empty. If1≤m≤5, choose any existing positive set and add5−m indexed copies of it. This leaves the hitting requirement unchanged. A vertex gains at most5−m≤4 occurrences, so its padded total occurrence is at most14. Apply Lemma A or B to the exactly-five-positive system. The resulting repair also repairs the original system. The padding has a proved occurrence allowance; it is not a general assertion that arbitrary positive duplication preserves a fixed degree bound.

In particular, an actual signed system with occurrence bound7 can add up to four copies and still remain within11, which is stronger than the needed14. Conversely these corollaries do not allow padding an arbitrary occurrence14 system without rechecking the bound.

## 3. A useful zero-triple corollary for at most eight positives

Suppose there are at most eight positive four-sets, no negative triples, at most27 negative four-sets, and total indexed occurrence at most7 at every vertex. Then a repair exists.

If some point x has positive occurrence a_x≥3, fix x in R. At most five positive four-sets remain unhit. Each negative four-set containing x becomes a negative triple after deleting x; there are at most7−a_x≤4 such indexed sets. The other negatives remain four-sets. The new signed system on the remaining vertices has occurrence at most7, so Corollary A repairs it. Adjoining x gives the original repair. This operation fixes x red; it is different from forbidding a vertex, in which case entire negative constraints containing it are discarded.

Otherwise every positive occurrence is at most2. Independently choose a uniform point from every positive set and take their union R. The joint occupancy lemma [RANDOM_TRANSVERSAL_REPAIR.md](RANDOM_TRANSVERSAL_REPAIR.md) gives, for every fixed negative four-set B,

Pr(B⊆R)≤∏_(x∈B)[1−(3/4)^{a_x}]≤(7/16)^4.

Thus the union bound is at most

27(7/16)^4=64827/65536<1.

This gives a repair. The case of no positive sets is immediate. The probability uses independent selections from the positive sets, not independence among original hypergraph edges.

## 4. Actual-H occurrence interface

To apply these statements to a colored hypergraph, specify which original edges produce the positive sets, which different original edges produce the negative sets, and why hitting/avoiding them gives a proper coloring. If the two indexed source-edge families are disjoint, each vertex's combined occurrence is at most its original degree. Constraints already proper under fixed colors may be discarded. No omitted zero-trace or opposite-sign bad edge is implicitly covered by this interface.

A complete example is [ONE_RED_EXTERIOR_DG35_CLOSURE.md](../../context/propertyb35-paper/round01/twentyfive/three_positive_cost/ONE_RED_EXTERIOR_DG35_CLOSURE.md). The numerical branch checks there are supplementary; the proofs of Lemmas A/B and their padding corollaries are the direct arguments above.
