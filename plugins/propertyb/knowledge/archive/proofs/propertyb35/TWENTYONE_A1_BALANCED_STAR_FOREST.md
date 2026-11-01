# 二十一点A1：平衡删星森林与四交边对上界

## 定理

Let H be a simple five-uniform hypergraph on 21 vertices with 35 edges, covering every pair of distinct vertices. Assume the reduced A1 roles: x is the unique degree-six point, p the unique degree-seven point, B and U have respectively four and five degree-eight points, and V9 has ten degree-nine points. The codegrees from x are two to every point of B and one to p and every point of U and V9.

Write n4 for the number of unordered pairs of distinct original edges whose intersection has size exactly four. **If H is not two-colorable, then n4≤11.** Equivalently, an H with these actual roles and n4≥12 has Property B.

The proof uses the complete balanced-star count, the general rank lemma in §4, Hunter's elementary forest inequality, and the two actual repair imports specified in §6. It gives a necessary structural bound and does not assert that all A1 inputs have Property B. The universal star minimum is164896 out of184756 balanced colorings; its exact finite domain and original-H interface are proved below.

## 1. Actual A1 star and complete finite representation

H has 21 vertices, 35 distinct five-element edges, covers all point pairs, and has the reduced A1 roles: x6,p7,nine8,ten9. Exactly four eight-degree points B have codegree2 from x; the other16 vertices have codegree1. Deleting x from its six original edges gives six distinct four-sets L0,…,L5 on 20 vertices. Every B point occurs twice and each other point once.

Represent each of the four repeated B points by a loopless edge between its two link indices. This gives a four-edge multigraph on six labeled block vertices. A block's remaining places are filled by distinct private points. Conversely this graph determines the star up to relabeling its four repeated and sixteen private points. Each graph degree is at most four automatically. The already proved repair for a four-intersection kernel containing x excludes three parallel graph edges: they would mean two links share at least three B points. Thus multiplicities are at most two.

All fifteen possible block pairs with four repeated choices give3060 multisets before the cap. Exactly2835 remain after multiplicity≤2. No further graph was discarded: the star alone forces no twice-covered888 triple (that would require three parallel graph edges), and a double graph edge only forces the still-allowed x+B+B three-core with B/B codegree initially at least two. Outside-star incidences could change that codegree; they cannot be guessed from this graph.

The complete S6 action on block labels gives eighteen orbits. Count C depends only on the star, so uniform coloring is invariant under all necessary point renamings. This does not assert that the relabelings are automorphisms of H, or that all private vertices have the same original degree.

## 2. Exact balanced count

Color the20 vertices other than x uniformly with ten red and ten blue; D=binom(20,10)=184756. Define C as the event that at least one color has **no** monochromatic link. If Hbar=H−x is proper on such a coloring, assign x a color having no monochromatic link; then all35 original edges are proper.

For selected disjoint red-link and blue-link index sets I,J, let R=union_{i∈I}Li and B=union_{j∈J}Lj. If R and B overlap, the imposed event is impossible. Otherwise the number of compatible red ten-sets is

    binom(20−|R|−|B|,10−|R|).

Inclusion–exclusion over nonempty I and nonempty J computes the count with at least one red and at least one blue monochromatic link; subtracting this from D gives |C|. There are only3^6 assignments of each link to red,blue,or unselected. Invalid binomial terms are zero.

The eighteen complete orbit results are below; pairs ij denote repeated-point graph edges. All unlisted block vertices are isolated.

|repeated graph edges|orbit size|C count|
|---|---:|---:|
|01,01,02,02|60|164896|
|01,01,23,23|45|165512|
|01,01,02,03|180|165640|
|01,01,02,13|180|165802|
|01,01,02,23|360|166052|
|01,01,02,12|60|166072|
|01,01,02,34|360|166138|
|01,01,23,24|180|166360|
|01,01,23,45|45|166480|
|01,02,03,04|30|166588|
|01,02,03,14|360|166936|
|01,02,13,23|45|166956|
|01,02,03,45|60|167026|
|01,02,03,12|180|167066|
|01,02,13,24|360|167082|
|01,02,34,35|90|167174|
|01,02,13,45|180|167188|
|01,02,12,34|60|167298|

The minimum is uniquely the first orbit: two adjacent doubled edges, link-graph degrees(4,2,2,0,0,0). The next orbit has two disjoint doubled edges. Every other orbit has C≥165640.

## 3. Hunter forest on the same sample space

There are29 original Hbar edges. For one such five-set e, its monochromatic event Ae has numerator2*binom(15,5)=6006, so the sum of the29 unconditional bad-event counts is174174.

For two different Hbar edges meeting in j points, the simultaneous monochromatic-event count is

|j|0|1|2|3|4|
|---:|---:|---:|---:|---:|---:|
|D Pr(Ae∩Af)|506|22|132|572|2002|

For j≥1 both edges must have the same color, giving2*binom(10+j,j). For j=0, same-color events contribute2 and opposite-color events contribute2*binom(10,5)=504. Thus the less intuitive disjoint count506 is correct.

For any forest T on the29 original edge indices, pointwise

    1_{union Ae} ≤ sum_e 1_Ae − sum_{ef∈T}1_{Ae∩Af}.

Indeed the forest induced on the active event vertices has at most one fewer edge than vertices whenever it is nonempty. Taking expectations gives

    D Pr(C ∩ proper(Hbar)) ≥ |C|−174174 + sum_{ef∈T} w(|e∩f|).

A strictly positive right side produces a proper coloring of the original H by the x-color extension in §2. There is no independence assumption between events or between C and the bad edges.

In particular a forest of five four-intersection pairs deducts10010>9278=174174−164896. Thus a non-B H has Hbar four-intersection forest rank at most four.

All pair weights are at least22. Any four-edge four-intersection forest can be completed to a spanning tree on29 event vertices, adding24 edges and giving deduction at least

    4*2002+24*22=8536.

For the sixteen orbits with C≥165640 this already gives a positive margin at least2. Hence those orbits require Hbar four-intersection rank at most three in a counterexample.

## 4. General nonunit-intersection forest-rank lemma

**Lemma.** Let E1,…,Em be distinct k-subsets of an n-element set, where k≥1, m>n and n<k². Form a simple graph Γ on the m original sets, joining two sets exactly when their intersection size differs from one. Then the size r of a spanning forest of Γ satisfies

    r ≥ m−n+2.

No point-pair coverage, degree bound, coloring hypothesis or connectedness assumption is required.

**Proof.** Let A be the real m-by-n incidence matrix, and let J denote the all-ones matrix of the appropriate size. Since every row sum is k,

    B=AAᵀ−J_m = A Q Aᵀ,       Q=I_n−J_n/k².

The matrix Q is positive definite: its eigenvalues are1 on the subspace perpendicular to the all-ones vector, and1−n/k²>0 on that vector. Thus B is positive semidefinite, rank(B)=rank(A)≤n, and the same rank equality holds for every principal submatrix and the corresponding row submatrix of A. The equality follows also directly from ker(AQAᵀ)=ker(Aᵀ), by positive definiteness.

Any one, two or three distinct rows of A are linearly independent. A single row is nonzero. For two rows, summing coordinates of a linear relation makes the two coefficients sum to zero; distinctness then makes both zero. For three rows, any dependence with a zero coefficient reduces to this case. Otherwise, summing coordinates and normalizing the coefficient of the third row gives

    w=t u+(1−t)v

for three distinct equal-weight zero-one rows. Equal weight and u≠v give a coordinate with u=1,v=0 and another with u=0,v=1. Since w is zero-one, t must be0 or1. This would make w equal v or u in every coordinate, a contradiction.

The diagonal entries of B are k−1 and its off-diagonal entries are |Ei∩Ej|−1. Hence B is block diagonal on the connected components of Γ. A component of size s has block rank at least min(s,3), by the row independence and rank equality just proved. In particular, size-one and size-two blocks are nonsingular.

The nullity of B is at least m−n>0. If all components had size at most two, every block would be nonsingular, a contradiction. Thus at least one component has size at least three. If component sizes are s1,…,sc, then r=Σ(si−1), and

    m−n ≤ nullity(B)
          ≤ Σ_{si≥3}(si−3)
          ≤ r−2.

The last inequality pays two from at least one component of size≥3, while every size-two component contributes one to r and zero to the displayed nullity upper bound. This proves r≥m−n+2. ∎

The strict inequality n<k² matters: it makes Q positive definite and preserves the independence ranks of the incidence rows. The hypothesis m>n is also explicit; the stated lower bound is not asserted for arbitrary m≤n.

## 5. Uniform Hunter repair when the four-intersection rank is at least four

Apply the lemma to the29 original Hbar edges on the20 points other than x, with k=5. Since29>20 and20<25, the graph Γ of non-one intersections has spanning-forest rank at least11.

Suppose the Hbar graph of four-intersection pairs has a forest of four edges. These four edges belong to Γ. Extend this particular forest inside Γ until it has eleven edges; this is possible by the elementary forest extension property, since Γ has rank at least eleven. Every one of the seven newly selected edges has intersection type0,2,3 or4, and hence event-intersection weight at least132 from §3. Complete the eleven-edge forest to a spanning tree on all29 event indices using seventeen further edges; every such edge has weight at least22.

The resulting single compatible tree gives Hunter deduction at least

    4*2002+7*132+17*22=9306.

Using the universal star minimum from §2,

    D Pr(C ∩ proper(Hbar)) ≥164896−174174+9306=28>0.

Thus some actual balanced coloring is proper on Hbar and has a color with no monochromatic link; assigning x that color gives a proper coloring of all H. No exceptional-star split is used.

Consequently, under the non-B hypothesis, the Hbar four-intersection graph has forest rank at most three. Every simple graph of forest rank r has at most binom(r+1,2) edges: for component ranks ri, each component has ri+1 vertices, so its edge count is at most binom(ri+1,2), and summing is at most binom(Σri+1,2). Hence

    n4(Hbar)≤6.

This step uses neither a common-neighborhood condition nor a prohibition on K5.

## 6. At most five four-intersection pairs cross the x-star

Only two original-H repair theorems are needed for the main proof:

- [TWENTYONE_HIGH_FOUR_CORE_LOW.md](TWENTYONE_HIGH_FOUR_CORE_LOW.md), including its strong-pair lemma: under the non-B hypothesis all point-pair codegrees are at most four, and no four-intersection kernel contains x or p.
- [TWENTYONE_HIGH_FOUR_CORE_MULTIPLICITY_THREE.md](TWENTYONE_HIGH_FOUR_CORE_MULTIPLICITY_THREE.md): a four-set of eight/nine-degree points with these codegree caps cannot be contained in three different original edges of a non-B H.

There are no four-intersection pairs among the six x-edges, because their kernel would contain x. For an x-edge E=x+L and an Hbar edge F, intersection size four means L⊆F. If L contains p, this is excluded by the first repair theorem. Otherwise L consists entirely of eight/nine-degree points. Since E itself contains L, the second theorem permits at most one other original edge containing L. Thus this x-edge has at most one Hbar four-intersection neighbor.

The unit codegree lambda(x,p)=1 means precisely one x-edge has p in its link, and that edge has no neighbor of this type. The remaining five x-edges have at most one each. Therefore

    n4(H) ≤ n4(Hbar)+5 ≤6+5=11.

This completes the theorem. In particular the main proof does not require the all-eight four-core repair, the full-six or five-of-six top repairs, any diamond-free graph argument, or the two-exceptional-star analysis. It retains all eighteen star types through the universal minimum.

Combining this theorem with [the earlier global two-flip necessary condition](GLOBAL_TWO_FLIP_PATH_REPAIR.md#63-the-resulting-sufficient-criterion-and-necessary-structure) also gives n3≥8 in a non-B A1 input: 17826*11+8838*7<259248, even before the nonnegative tau penalty. A1 remains open.

## 7. Independent finite evidence

[GENERATE.py](../../context/propertyb35-paper/round01/middle/a1_balanced_star_forest_20261020/GENERATE.py) enumerates all3060 multichoose keys, keeps the2835 cap-valid ones, covers them by the full S6 action, and saves every orbit member. It computes C by the red-nonempty/blue-nonempty inclusion–exclusion and directly enumerates184756 bitmask colorings for each of the three worst orbits.

[VERIFY.py](../../context/propertyb35-paper/round01/middle/a1_balanced_star_forest_20261020/VERIFY.py) does not import that generator. It independently generates multiplicities0/1/2 with total four, recovers the same2835 full keys, and produces every orbit by breadth-first closure under adjacent transpositions. It checks all eighteen C counts with the alternative identity C=2*(no red mono link)−(no mono link of either color), and independently enumerates the three worst families using red ten-subsets. It checks the uniform 9306 deduction and margin28. It also retains scalar and five-vertex graph checks for the earlier alternative proof in the appendix; those are not dependencies of the main rank proof. Actual independent result PASS, approximately0.443CPU seconds; original calculation approximately0.119CPU seconds. No H or negative-layout enumeration was performed.

Reproduction:

```sh
.tools/math-python/bin/python context/propertyb35-paper/round01/middle/a1_balanced_star_forest_20261020/VERIFY.py
```

The complete orbit data and direct checks are [RESULT.json](../../context/propertyb35-paper/round01/middle/a1_balanced_star_forest_20261020/RESULT.json) and [VERIFY.json](../../context/propertyb35-paper/round01/middle/a1_balanced_star_forest_20261020/VERIFY.json). These finite certificates cover only the six-edge link incidence, the stated exact balanced counts and the small graph bound. The original-H coverage and repair implications are established in §§1–6. ∎

## Appendix: retained earlier alternative proof

The following earlier route is preserved for its valid weighted-forest interfaces and extremal observations. It is not needed for the theorem above and has additional all-eight/five-top imports. The finite evidence remains unchanged.

### A1. Exact uniform weighted-forest interface

Let r4 be the graphic rank of the Hbar graph of four-intersection pairs; r34 the rank using intersections3 or4; r034 the rank using0,3,or4; and r0234 the rank using every type except1. Graphic rank means the size of a spanning forest, including all29 event vertices in the definition.

Kruskal's algorithm on the complete weighted event graph gives maximum tree deduction exactly

    Wtree =616 +110*r0234 +374*r034 +66*r34 +1430*r4.

This follows from baseline28*22 and successive weight increments132−22,506−132,572−506,2002−572. The rank levels are nested, so the formula uses jointly compatible tree choices. Therefore Wtree>174174−|C| is one uniform sufficient criterion; the universal sufficient condition is Wtree>9278.

For example r4=4 and r34≥6 already suffice by the lower bound616+1430*4+550*6=9636. With r4=4, two additional forest edges of type0 or3 also suffice. This argument does not assume those additional ranks or edges exist.

### A2. Earlier repair imports and the four-intersection graph

The following original-H theorems are imported:

- [TWENTYONE_HIGH_FOUR_CORE_LOW.md](TWENTYONE_HIGH_FOUR_CORE_LOW.md): a four-intersection kernel containing x or p gives Property B.
- [TWENTYONE_A1_FOUR_EIGHT_CORE.md](TWENTYONE_A1_FOUR_EIGHT_CORE.md): an all-eight-degree four-intersection kernel gives Property B.
- [TWENTYONE_HIGH_FOUR_CORE_MULTIPLICITY_THREE.md](TWENTYONE_HIGH_FOUR_CORE_MULTIPLICITY_THREE.md): a four-set of8/9-degree points contained in at least three original edges gives Property B, provided its pair codegrees are at most four. The actual A1 strong-pair reductions provide this cap.
- [TWENTYONE_A1_FIVE_TOP.md](TWENTYONE_A1_FIVE_TOP.md): five or more of the six five-subsets of one six-set give Property B. Its full-six case uses [TWENTYONE_K6_TOP.md](TWENTYONE_K6_TOP.md). This is a separate complete original-H repair theorem; it is not inferred from the present star enumeration.

Under a non-B hypothesis these imply every four-set is in at most two edges; kernels containing x/p or all8 are in at most one.

For adjacent four-intersection edges E=K+u,F=K+v, a common neighbor either contains K, or is (K−a)+u+v for a∈K. The first possibility would put K in three edges and is excluded. All possible remaining common neighbors are five-subsets of the same six-set K+u+v and are pairwise adjacent. Thus every edge's common neighborhood in the four-intersection graph is a clique.

There is no K5 in that graph: five pairwise adjacent original edges, using the preceding description on one adjacent pair, would be five five-subsets of the same six-set, contrary to the five-top repair.

For a graph with these two properties and forest rank≤4, there are at most seven edges. Each component has at most five vertices. On five vertices, a K4 permits at most one attachment to the fifth vertex (two attachments would force K5 via the common-neighborhood property), giving at most7 edges. With a triangle but no K4, each other point has at most one triangle neighbor, giving at most6; triangle-free graphs have at most6 by the elementary five-point Mantel bound. Components of ranks1,2,3 have at most1,3,6 edges. The partitions of total rank≤4 give at most7 overall. Equality has precisely K4 plus a pendant edge on five points, or a K4 component and a disjoint K2 component.

It follows that Hbar has n4bar≤7 in all orbits, and n4bar≤6 in the sixteen orbits whose rank is at most three. Forest rank has not been replaced by edge count at any earlier step.

### A3. Earlier exceptional-star treatment

The six original x-edges have no four-intersection pairs among themselves, by the low-x kernel repair. Fix one such edge E=x+L. Every Hbar neighbor intersecting E in four points must contain its entire link L. The multiplicity-three repair and low-kernel repairs give at most one such neighbor.

More is true for two particular star edges:

- p lies in exactly one link Lp, since lambda(x,p)=1. This x-edge has no four-intersection neighbor at all: its kernel Lp would contain p.
- Any link with graph degree four consists entirely of B points and has no private point. It has no four-intersection neighbor because its kernel is all8. Such an edge differs from the p-edge, since p is private in the link system.

Thus at most five four-intersection pairs cross from the star to Hbar. In the unique worst orbit, graph degrees(4,2,2,0,0,0) force one all-B link, improving this to four.

Together with Appendix A2, the sixteen nonexceptional orbits have total n4≤6+5=11, and the worst orbit has n4≤7+4=11. Only the second orbit, the two disjoint double edges, could still permit n4=12 via n4bar=7 and five cross pairs.

### A4. The second-orbit extremum

In the second orbit, C=165512, and the rank-four completed-tree deduction8536 leaves a deficit126. Contract all four-intersection components of Hbar.

Any cross-component pair of type0 or3 could be added to the quad forest in place of a baseline22 edge, gaining at least506−22=484>126; this would repair H. Thus every cross-component pair in a non-B input has type1 or2. If type2 occurs between two different pairs of contracted components, those two edges form a forest on the contracted graph; they can be selected simultaneously and gain2*(132−22)=220>126. Thus all cross-component type2 pairs lie between one fixed pair of components.

If n4bar=7 and its rank is four, the graph classification in Appendix A2 leaves just K4+pendant or K4 disjoint K2, plus isolated vertices. There are at most ten intra-component vertex pairs, seven of type4, so their total intersection surplus sum(|e∩f|−1) is at most7*3+3*2=27. In the first shape, one pair of components has at most5*1 original pairs; in the second at most4*2=8. Therefore the sole possible cross-component type2 class adds at most8 to the surplus. All remaining cross-component pairs have type1 and add zero. Hence

    sum_{unordered Hbar edge pairs} (|e∩f|−1) ≤27+8=35.

But the actual deleted degrees are six at p and the four B points, seven at the five U points, and eight at the ten nine-degree points. Thus

    Wbar=5*binom(6,2)+5*binom(7,2)+10*binom(8,2)=460,
    Wbar−binom(29,2)=460−406=54,

contradicting the upper bound35. The second orbit therefore cannot have n4bar=7, so it too has total n4≤11.

This proves the stated new necessary bound n4≤11 for every non-B reduced-A1 input, subject to the exact repair imports in Appendix A2. It does not prove H is colorable. Together with [the global two-flip weighted condition](GLOBAL_TWO_FLIP_PATH_REPAIR.md#63-the-resulting-sufficient-criterion-and-necessary-structure) it forces n3≥8, even if tau=0, because17826*11+8838*7<259248.

