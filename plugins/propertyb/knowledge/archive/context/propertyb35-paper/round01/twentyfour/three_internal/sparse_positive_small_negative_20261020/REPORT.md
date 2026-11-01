# Five sparse positive four-sets and small negative constraints

The proposed general signed lemma holds. This is an analytic proof, with only seven scalar occurrence profiles; no outside layout or hypergraph enumeration is used.

**Theorem.** Let five indexed positive four-sets have union of size at least17. Let the indexed negative family have at most four pairs, one triple and22 four-sets. If each point has total positive-plus-negative indexed occurrence at most seven, there is a set R meeting every positive set and containing no negative set. The ambient finite ground set is unrestricted.

First remove duplicate negative pair constraints. This preserves precisely the repair requirement and only decreases occurrence counts. The negative triple and four-set indices retain their multiplicities. In particular a specified pair of points is now a negative pair at most once.

Independently select a uniform point from each positive set and take their union R. Write a_v for positive occurrence and p_v=1−(3/4)^{a_v}. The [occupancy product lemma](../../../../../../proofs/propertyb35/RANDOM_TRANSVERSAL_REPAIR.md) gives Pr(F⊆R)≤∏_{v∈F}p_v for every negative set F. Points of positive occurrence zero have probability zero. Put

q=1/4, p=7/16, r=37/64, s=175/256.

The positive repeated-incidence surplus is Σ_{a_v≥1}(a_v−1)=20−|∪A_i|≤3. Hence the repeated points have exactly one of the seven profiles below. All other points have probability at most q.

|Repeated positive occurrences|Upper bound on total negative bad probability|
|---|---:|
|none|45/128|
|one2|315/512|
|one3|1665/2048|
|two2|1701/2048|
|one4|6987/8192|
|three2|981/1024|
|one3 and one2|8181/8192|

For the first three rows use respectively the uniform-private baseline, or bounds pq/rq per negative pair, pq²/rq² per triple and pq³/rq³ per four-set. For two double points, uniqueness of the negative pair on these points gives the bound p²+3pq+p²q+22p²q². For one quadruple point, its negative occurrence is at most3, so at most three negative pairs use it; the valid overestimate is 3sq+q²+sq²+22sq³. These give the displayed exact values.

For three double points, their total negative incidence is at most15. A negative k-set containing j double points has product bound p^j q^{k−j}. Convexity of this geometric sequence gives chord slopes

A₂=(p²−q²)/2, A₃=(p³−q³)/3, A₄=(p³q−q⁴)/3,

where for four-sets j≤3. These satisfy A₂>A₃>A₄>0. At most eight double incidences occur in negative pairs and at most three in the negative triple. Allocate the total budget15 first to those two types: the bad sum is at most

45/128+8A₂+3A₃+4A₄=981/1024.

Finally suppose x has positive occurrence3 and y has positive occurrence2. Put Δx=r−q=21/64 and Δy=p−q=3/16. For a negative k-set the product bound is at most

q^k+1_{x∈F}Δx q^{k−1}+1_{y∈F}Δy q^{k−1}+1_{x,y∈F}ΔxΔy q^{k−2}.

The negative occurrence budgets of x,y are at most4,5. Since k≥2, the two first-order sums are at most4qΔx and5qΔy. At most four negative indices contain both points. Among them at most one is a pair and at most one is a triple. The weighted joint-occurrence sum is therefore at most1+q+2q², even if some categories are absent. Consequently the total bad sum is at most

45/128+4qΔx+5qΔy+ΔxΔy(1+q+2q²)=8181/8192<1.

All seven profiles are strict. The union bound gives positive probability of avoiding every indexed negative constraint, proving the theorem.

`CHECK.py` independently evaluates these rational formulas, checks the chord ordering and the finite scalar resource allocation, and writes `CHECK.json`. It does not enumerate set systems. In the intended actual caller, five positive four-sets covering17 points, at most four negative pairs, one negative triple,22 negative four-sets and the total occurrence bound seven suffice directly. This report does not by itself assert that every original P-side inventory produces that caller; that separate actual selection connection remains with the parent proof.
