# One red exterior point and d(G)=35 on24 vertices

Let H be a finite simple five-uniform hypergraph on24 points, pair-covering, with at most35 edges and minimum degree at least7. Suppose an edge G has degree sum35, and a coloring of H−G is proper, with G all red and exactly one red exterior point r. Then H has Property B.

This is a complete **conditional branch**, not an assertion that such an initial coloring is always available. It uses the exact four-positive local gate in `FOUR_REPAIR_GATE.md` and its independent replay; the final five-positive step below is a direct counting proof.

## 1. Two direct signed-set lemmas

Positive and negative families in these lemmas retain their original edge indices. The occurrence bound counts memberships in both families, with those indices. A repair is a set meeting every positive set and containing no negative set.

**Lemma A.** Five positive four-sets, at most four negative triples, and at most28 negative four-sets have a repair if each vertex has total indexed occurrence at most14.

Proof. If the five positive sets are pairwise disjoint, choosing one point from each gives1024 different five-point candidates. A negative triple lies in at most16 candidates; a negative four-set lies in at most4. Thus at most4·16+28·4=176 candidates are bad.

Otherwise consider a vertex x in at least two positive sets. If some such x has positive occurrence at least3, at most two positives remain unhit. With zero or one remaining set a repair of size at most2 exists. If two remain and intersect, x and an intersection point suffice. If they are disjoint, their16 point-pairs give16 different repairs of size3 containing x. At most four can be negative triples, so one succeeds; negative four-sets cannot obstruct a three-point candidate.

It remains to consider maximum positive occurrence2. Choose x hitting exactly two positives; all other three avoid x. If these three are pairwise disjoint, there are64 different four-point candidates containing x, choosing one point from each. A negative triple containing x lies in at most4 candidates; one avoiding x lies in at most1. A negative four-set can obstruct only if it contains x, and there are at most14−2=12 such indexed negative sets. Hence at most4·4+12=28 of the64 candidates are bad.

If the three remaining positives are not pairwise disjoint, choose y in two of them. It hits exactly two, because maximum positive occurrence is2, and therefore y occurs in neither of the two positives hit by x. Let A be the last positive; it avoids x,y. Its four vertices give four distinct three-point candidates {x,y,z}, z∈A. Unless one repairs, these candidates must be precisely four indexed negative triples, exhausting all negative triples. In particular every negative triple contains both x and y.

Now forbid x and keep y selected. The two original positives hit by x shrink to three-sets after deleting x; neither contains y. Together with A they are three positive sets of sizes3,3,4, all avoiding x,y. If any two intersect, a point in their intersection and a point of the third, together with y, give a repair of size at most3: it avoids x, hence all the negative triples. If the three sets are pairwise disjoint, they yield36 different four-point candidates, all containing y and avoiding x. Negative triples again cannot obstruct. At y, the positive occurrence2 and the four already forced negative triples leave at most14−2−4=8 indexed negative four-sets. Each obstructs at most one candidate. Thus one succeeds. ∎

**Lemma B.** Five positive sets, each of size3 or4, at most one negative triple, and at most28 negative four-sets have a repair if each vertex has total indexed occurrence at most14.

Proof. If the positive sets are pairwise disjoint, there are at least3^5=243 one-from-each five-point candidates. The negative triple lies in at most4²=16, and each negative four-set in at most4, so at most16+28·4=128 are bad.

Otherwise choose an intersection point x. If its positive occurrence is at least3, at most two positives remain unhit. When two remain, either they intersect, giving a repair of size at most2 with x, or their at-least-nine point-pairs give at least nine three-point candidates containing x. One negative triple cannot obstruct all of them. The cases of zero or one remaining positive are immediate.

If x hits exactly two positives, three remain and all avoid x. If two of these intersect at y, then either y hits all three and {x,y} repairs, or choosing any point in the last positive yields at least three distinct three-point candidates {x,y,z}. Again at most one is a negative triple. If the three are pairwise disjoint, there are at least27 four-point candidates containing x. The negative triple obstructs at most4 of them. At most14−2=12 indexed negative four-sets contain x. Thus at most16 candidates are bad, fewer than27. ∎

These arguments do not assume that the positive sets have small repeated-incidence surplus, that their vertices have equal degrees, or that the negative constraints are independent. Occurrence subtractions at x or y use disjoint positive/negative indexed edge families; in Lemma A's last case the four negative triples were already forced as four different sets.

## 2. Reduction of the actual H to five positive edges per center

Every g∈G has degree7. For a fixed center g let its positive four-sets be the original edges e with e∩G={g} whose other four points are initially blue. Flip g blue and allow only originally blue exterior vertices to turn red. Every original edge avoiding g contributes the nonempty negative set B_f consisting of its originally blue points. A signed repair is exactly a proper coloring of H, as proved in `../LOW_EDGE_REPAIR_INTERFACE.md`.

The low-edge row budget is

9n_1(g)+4n_2(g)+n_3(g)≤24.

The direct small-blocker argument rules out m_g≤2 in a non-B H. The three-positive argument in `REPORT.md` rules out m_g=3. That argument uses the squared-cost bound alone. Thus noncolorability implies m_h≥4 for all five centers.

If some center g has m_g=4, the other four centers supply at least16 indexed negative four-edges and16 incidences with S=G−{g}. The exact S-incidence identity gives

3n_1(g)+2n_2(g)+n_3(g)≤35−7−4−16=8.

The four positive sets have surplus≤5. Positive/negative source edge families are disjoint, and every blue subset U has total degree at most7|U|+7. The complete signed-set gate `FOUR_REPAIR_GATE.md` therefore repairs H. It was independently replayed over all798 positive Venn families and23393 forbidden-point markings; all exact integer counts are strict.

Finally m_g≤5 for every seven-degree center, since pair coverage with the red exterior point r supplies a nongroup edge through g that cannot be positive. Hence noncolorability would require

m_g=5 for all five g∈G.

The fifth constraint has not been discarded; this remaining case is handled next.

## 3. The remaining nongroup G-traces form a true partition

At a center g, the seven incident edges are G, five positive edges, and one remaining edge f_g. Pair coverage of g,r forces r∈f_g. Thus any edge meeting G, other than G and the25 positive edges, contains r. Two different such edges have disjoint nonempty G-traces, since each g has only one such edge. Their traces form a partition Π of G.

Every block has size at most3. A size4 block, together with r, would form a second all-red edge in the original coloring, contradicting the proper coloring of H−G. Every edge disjoint from G contains r as well, because r is the only red exterior point and that edge was proper. Therefore every edge other than G and the25 positive edges contains r. In particular

d(r)=M−26∈{8,9}

Here M∈{34,35} follows from5M≥7·24 and M≤35. The closure below does not need the exact value.

Choose g in a largest block of Π. In its negative family, the20 positive edges of the other centers are negative four-sets. A partition block other than g's block, of size b, contributes a negative set of size4−b. Zero-G edges contribute negative four-sets. Since the chosen block is largest and |G|=5, no other block has size3. Thus there are no negative singletons.

If Π consists of five singletons, there are four negative triples. Otherwise the chosen block has size at least2; the other blocks cover at most3 points. There is at most one negative pair, and at most three negative triples. If a negative pair exists, its size2 block leaves at most one other point, so there is at most one negative triple. Equivalently the possible block-size partitions and resulting(pair,triple) bounds are:

| Π block sizes | Choose block size | Negative pairs | Negative triples |
|---|---:|---:|---:|
|1+1+1+1+1|1|0|4|
|2+1+1+1|2|0|3|
|2+2+1|2|1|1|
|3+1+1|3|0|2|
|3+2|3|1|0|

All remaining negative sets have size4. There are at most M−7≤28 indexed negatives altogether.

## 4. Repair of the partition case

For every vertex v, minimum degree7 and at most35 edges on24 vertices imply

d(v)≤7+(5·35−7·24)=14.

The five positive edges through the chosen center and all negative edges avoiding it are different original edges. Their combined indexed occurrence at any blue vertex is therefore at most14.

If there is no negative pair, Lemma A applies directly: five positive four-sets, at most four negative triples and at most28 negative four-sets. Its signed repair colors H.

If there is a negative pair {u,v}, forbid one endpoint u from the repair. Delete u from each positive set; their sizes become3 or4. Discard every negative set containing u, since it is automatically avoided. **Do not delete u from such a negative set and keep its remainder as a new constraint.** The sole negative pair is now avoided, at most one negative triple remains, and at most28 negative four-sets remain. Indexed occurrence can only decrease. Lemma B applies and gives a repair avoiding u, hence also avoiding the original negative pair. This again colors H.

Both cases contradict noncolorability. This completes the stated conditional branch. It leaves no m=5 local table or partition case unresolved.

## 5. Verification and limits

`ONE_RED_EXTERIOR_CHECK.py/json` checks the finite numerical inequalities used in Lemmas A/B and all five integer partition cases. The proofs themselves are the direct arguments above. No external model is used as a proof step. The four-positive gate has its separate complete-domain, different-candidate-generation standard-library replay.

This theorem does not prove that an arbitrary critical H has one red exterior point in a proper H−G coloring; a=2 or larger is not covered. It does not claim d(G)=36 is covered by the same four-positive budget8. It therefore must be cited with the exact initial-coloring and d(G)=35 hypotheses stated at the start.
