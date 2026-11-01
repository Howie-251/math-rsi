# A shared-capacity weak dual for the six-remaining-positive repair

This note gives a sufficient **general rational certificate**, not a claim that all77 residual six-label classes admit one. It does not regenerate the six-label domain or the original P census.

## 1. Exact fixed-point interface

Start with nine indexed positive four-sets, negative triples and four-sets of total count at most20, at most three negative triples, and total indexed occurrence at most seven. Fix a point x of positive occurrence three red. Its three positive sets are hit. Let the six remaining positive four-sets lie in U, avoid x, and let their maximum positive occurrence be at most two. A candidate S⊆U must hit these six sets; the final red set is {x}∪S.

The negative indices have four distinct origins, even though two residual types have the same size:

|Type|Original negative edge|Residual target F|Indexed count|
|---|---|---|---|
|2|triple containing x|original triple minus x, size2|u|
|3|triple avoiding x|original triple, size3|w|
|x3|four-set containing x|original four-set minus x, size3|v|
|4|four-set avoiding x|original four-set, size4|z|

Every actual indexed family satisfies

u+w≤3, u+v≤4, u+w+v+z≤20.                         (1)

The middle bound is x's three positive occurrences subtracted from D7. For y∈U let fy be its **original** positive occurrence; the residual negative occurrence at y is at most cy=7−fy. If only the six remaining positives are represented, their frequencies gy≤fy give the safe weaker choice cy=7−gy, namely5 at double points and6 at private points. Original positives hit by x must not be treated as nonexistent when a sharper capacity is claimed.

## 2. Weak-dual lemma

Let C be any finite family of subsets S⊆U hitting every remaining positive set. One may use all three-/four-point transversals, or any convenient subfamily. Assign nonnegative rational weights λS and write

Λ=ΣS∈C λS,  W(F)=ΣS∈C,F⊆S λS.

Choose nonnegative rational multipliers a,b,c and hy for y∈U. Suppose the following inequalities hold for **every possible active residual target** of each indicated type:

W(F)≤a+b+c+Σy∈F hy                 (type2),
W(F)≤a+c+Σy∈F hy                   (type3),
W(F)≤b+c+Σy∈F hy                   (typex3),
W(F)≤c+Σy∈F hy                     (type4).       (2)

If

Λ>3a+4b+20c+Σy∈U cy hy,                           (3)

then some candidate S is unblocked, and {x}∪S repairs the original signed system.

**Proof.** A negative index blocks exactly those S containing its residual F. Summing its blocked weight, using (2) separately for each original index, and retaining multiplicities, gives

Σnegative indices j W(Fj)
≤a(u+w)+b(u+v)+c(u+w+v+z)+Σy hy·negative_occurrence(y)
≤3a+4b+20c+Σy cy hy<Λ.

The weight of the union of the blocked candidates is at most this sum. Since all weights are nonnegative, at least one positive-weight candidate is not blocked. Its six positive constraints are hit; x hits the other three; all four types of original negative constraints are avoided. No independence of negative events, integrality of an optimization optimum, or solver feasibility theorem is used. ∎

## 3. Full negative domain and transport

For a universal certificate based only on the represented positives and budgets, a safe domain is **all** F⊆U of size2 for type2, all size3 subsets for each of types3 andx3 separately, and all size4 subsets for type4. At |U|≤17 this means136+2·680+2380=3876 inequalities at most. Removing a type/target needs an actual impossibility argument; for example type3 and typex3 cannot be merged just because both are triples, since their shared count budgets differ.

An original negative target involving a point outside U is automatically avoided: S never selects that point, and x has already been removed only in types2/x3. Such indices may be omitted from the active domain, while their consumption of global/point capacities may safely be ignored or explicitly subtracted. No original edge that blocks a candidate is lost by restricting the active target domain to subsets of U.

Targets need not equal candidates. A pair blocks all containing three-/four-point candidates; a triple blocks an equal three-point candidate and every containing four-point candidate; a four-set blocks only an equal four-point candidate and no three-point candidate. The inclusion definition of W handles all of these cases. Applying an equality-only blocker rule to pairs or triples would be incorrect.

Repeated type2 targets are permitted. Keeping every original index in the sum proves the result without assuming they are distinct. Identical residual targets can also occur in different types, notably one original triple F and one original four-set {x}∪F; these remain separate indices with different costs in (2). Logical deduplication is optional, not an unproved simplicity assumption. The domain relaxation can even permit more repetitions than an actual input: that strengthens the certificate requirement and is safe.

Any bijection of U transports candidates, all target types, point capacities and weights together, preserving (2),(3). A six-label permutation must transport its represented shared/private points in this same way. It is not valid to relabel different negative target types independently while retaining a single candidate family.

## 4. Exact integer certificate format

Clear a common denominator. A complete certificate consists of the explicitly represented six positive sets (or their intersection multigraph and private points), candidate list, nonnegative integer candidate weights LS, nonnegative integers A,B,C and Hy, and valid capacities cy. Check

ΣS⊇F LS≤A+B+C+ΣF Hy,             type2;
ΣS⊇F LS≤A+C+ΣF Hy,               type3;
ΣS⊇F LS≤B+C+ΣF Hy,               typex3;
ΣS⊇F LS≤C+ΣF Hy,                 type4;

and the single integer strictness condition

ΣS LS≥3A+4B+20C+Σy cy Hy+1.                     (4)

Every listed candidate must be checked to hit all six positives. Every target-domain inequality must be checked, not just a sampled or maximal-extension target. The certificate does not need the full candidate family to be complete: a verified subfamily suffices. Floating LP output can discover multipliers, but acceptance requires rational reconstruction and these finite exact inequalities. A failed fractional relaxation neither supplies an indexed negative obstruction nor a signed counterexample.

## 5. Optional target-upper-bound multipliers

For each of the four types separately, merge identical residual negative targets. This leaves exactly the same repair requirement and only decreases each count and point occurrence in (1). Do **not** merge across types when retaining their distinct budget accounting. The resulting multiplicity of each pair `(type,F)` is either zero or one. Equal residual triples of types3 andx3 may still both be present.

Assign another nonnegative rational multiplier γtype,F to each allowed typed target. Replace its inequality in (2) by

W(F)≤its three-budget cost+Σy∈F hy+γtype,F.

Then the sufficient strict condition is

Λ>3a+4b+20c+Σy cy hy+Σall allowed (type,F) γtype,F.       (5)

Indeed every deduplicated typed target uses its upper-bound multiplier at most once. Summing over the actual targets contributes at most the full displayed γ sum. This is precisely the valid weak dual when a covering LP includes an upper bound one for each typed negative-target variable. It is not justified to use such an upper bound without either the preceding logical deduplication or a separate uniqueness argument.

An integer certificate adds a nonnegative integer Gtype,F to the corresponding target inequality and adds ΣG to the right side of (4). All listed G must be included in that sum, even when their target is absent from an actual input; unlisted targets mean G=0. Each target must belong to the allowed domain, and type3/typex3 entries with the same residual set are distinct entries. With no upper multipliers the original indexed-multiplicity proof applies directly, without deduplication.

## 6. Low-parameter choices and conditional shared-core repair

One inexpensive starting family sets λS=λ3 for every three-transversal and λS=λ4 for every four-transversal. Then W(F)=λ3d3(F)+λ4d4(F), using the exact extension numbers already computed in the six-label census. Try point prices constant on represented point types: η1 on private points and η2 on double points. Their capacity cost is6nprivateη1+5ndoubleη2 when only remaining-positive frequencies are known. This leaves only seven scalar quantities λ3,λ4,a,b,c,η1,η2; all target inequalities still require exact checking. Finer classes can be automorphism orbits or a small intersection-pattern partition, rather than one price per arbitrary exterior layout.

More generally a symmetry group preserving the positive representation, candidate domain and chosen capacities allows simultaneous averaging of λ and h over the group. The three scalar budget multipliers are unchanged. Every translated target remains in the same type domain, so all inequalities and the strict gap are preserved. This justifies orbit-constant weights/prices when that precise group is used; grouping merely by positive frequency is a useful restriction to try, not an automatic averaging theorem unless an actual symmetry supports it.

There is also a useful **conditional** version. Reveal any actual subfamily K of negative indices, restrict C to candidates avoiding every target in K, and subtract K's indexed resource consumption from each bound in (1) and from every cy. Apply the same lemma with the resulting nonnegative remaining budgets (T0,X0,M0,cy′): replace the right side of (3) by T0a+X0b+M0c+Σcy′hy. Weights may depend on the revealed actual targets. Remaining unknown targets still range over their complete possible domain. This is a quantified actual-family argument, not a universal weight chosen after seeing an unknown obstruction and then forgetting its costs.

The already proved two-isolated-label lemma illustrates why this version can outperform an unconditional extension sum: after three maximal type2 targets are revealed and avoided, the residual sixteen candidates share a pair Z. Their two double points each have negative capacity at most five, so any active type4 target consumes that core capacity. The same mechanism suggests a targeted certificate for a 77-residual class only if its surviving candidate family can be shown to have such a common point/pair or a small weighted core. This note does not establish that property for any additional entire residual class.

## Relation to the current residual domain

The census records417328 labelled six-label graphs and981 orbits; its sum bounds plus the separate two-isolated proof leave77. The above lemma is applicable to any of these represented six-positive families, with (1) exactly the original three shared budgets, and optionally sharper original positive frequencies. No new class has been declared solved here. The gain is a single checkable shared-capacity certificate interface that uses both candidate sizes under the **same** budget multipliers and retains all four negative origins.
