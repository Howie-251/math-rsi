# A1 balanced six-star and Hunter forest: complete count and n4 bound

**Updated main proof:** the canonical now uses the general nonunit-intersection rank lemma below (§9) and only the low-four-core/strong-pair plus multiplicity-three imports. Sections1–8 retain the earlier valid five-top/exceptional-star route as a historical alternative; those additional dependencies are no longer needed for n4≤11.

The universal balanced-star count is **164896**, not 167174, out of 184756 equally likely colorings. The complete domain has 2835 labeled repeated-point multigraphs and eighteen S6-orbits. Exact inclusion–exclusion on all eighteen orbits and two independent direct enumerations of the three worst color families agree.

Combining this count with Hunter's forest inequality and the explicit existing repair imports below proves the following structural statement:

> In a non-Property-B reduced-A1 H, the number n4 of unordered original edge pairs intersecting in exactly four vertices is at most eleven.

This is a necessary counterexample bound, not a proof that A1 is colorable. The five-top repair is an explicit imported theorem; its separate parent-agent/cross-family acceptance is not asserted by this report.

## 1. Actual A1 star and complete finite representation

H has21 vertices,35 distinct five-element edges, covers all point pairs, and has the reduced A1 roles: x6,p7,nine8,ten9. Exactly four eight-degree points B have codegree2 from x; the other16 vertices have codegree1. Deleting x from its six original edges gives six distinct four-sets L0,…,L5 on20 vertices. Every B point occurs twice and each other point once.

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

## 4. Exact uniform weighted-forest interface

Let r4 be the graphic rank of the Hbar graph of four-intersection pairs; r34 the rank using intersections3 or4; r034 the rank using0,3,or4; and r0234 the rank using every type except1. Graphic rank means the size of a spanning forest, including all29 event vertices in the definition.

Kruskal's algorithm on the complete weighted event graph gives maximum tree deduction exactly

    Wtree =616 +110*r0234 +374*r034 +66*r34 +1430*r4.

This follows from baseline28*22 and successive weight increments132−22,506−132,572−506,2002−572. The rank levels are nested, so the formula uses jointly compatible tree choices. Therefore Wtree>174174−|C| is one uniform sufficient criterion; the universal sufficient condition is Wtree>9278.

For example r4=4 and r34≥6 already suffice by the lower bound616+1430*4+550*6=9636. With r4=4, two additional forest edges of type0 or3 also suffice. This report does not assume those additional ranks or edges exist.

## 5. Exact repair imports and the four-intersection graph

The following original-H theorems are imported:

- `TWENTYONE_HIGH_FOUR_CORE_LOW.md`: a four-intersection kernel containing x or p gives Property B.
- `TWENTYONE_A1_FOUR_EIGHT_CORE.md`: an all-eight-degree four-intersection kernel gives Property B.
- `TWENTYONE_HIGH_FOUR_CORE_MULTIPLICITY_THREE.md`: a four-set of8/9-degree points contained in at least three original edges gives Property B, provided its pair codegrees are at most four. The actual A1 strong-pair reductions provide this cap.
- `TWENTYONE_A1_FIVE_TOP.md`: five or more of the six five-subsets of one six-set give Property B. Its full-six case uses `TWENTYONE_K6_TOP.md`. The parent is separately validating this new import; it is not proved by the present star enumeration.

Under a non-B hypothesis these imply every four-set is in at most two edges; kernels containing x/p or all8 are in at most one.

For adjacent four-intersection edges E=K+u,F=K+v, a common neighbor either contains K, or is (K−a)+u+v for a∈K. The first possibility would put K in three edges and is excluded. All possible remaining common neighbors are five-subsets of the same six-set K+u+v and are pairwise adjacent. Thus every edge's common neighborhood in the four-intersection graph is a clique.

There is no K5 in that graph: five pairwise adjacent original edges, using the preceding description on one adjacent pair, would be five five-subsets of the same six-set, contrary to the five-top repair.

For a graph with these two properties and forest rank≤4, there are at most seven edges. Each component has at most five vertices. On five vertices, a K4 permits at most one attachment to the fifth vertex (two attachments would force K5 via the common-neighborhood property), giving at most7 edges. With a triangle but no K4, each other point has at most one triangle neighbor, giving at most6; triangle-free graphs have at most6 by the elementary five-point Mantel bound. Components of ranks1,2,3 have at most1,3,6 edges. The partitions of total rank≤4 give at most7 overall. Equality has precisely K4 plus a pendant edge on five points, or a K4 component and a disjoint K2 component.

It follows that Hbar has n4bar≤7 in all orbits, and n4bar≤6 in the sixteen orbits whose rank is at most three. Forest rank has not been replaced by edge count at any earlier step.

## 6. Four-intersection pairs incident to the x-star

The six original x-edges have no four-intersection pairs among themselves, by the low-x kernel repair. Fix one such edge E=x+L. Every Hbar neighbor intersecting E in four points must contain its entire link L. The multiplicity-three repair and low-kernel repairs give at most one such neighbor.

More is true for two particular star edges:

- p lies in exactly one link Lp, since lambda(x,p)=1. This x-edge has no four-intersection neighbor at all: its kernel Lp would contain p.
- Any link with graph degree four consists entirely of B points and has no private point. It has no four-intersection neighbor because its kernel is all8. Such an edge differs from the p-edge, since p is private in the link system.

Thus at most five four-intersection pairs cross from the star to Hbar. In the unique worst orbit, graph degrees(4,2,2,0,0,0) force one all-B link, improving this to four.

Together with §5, the sixteen nonexceptional orbits have total n4≤6+5=11, and the worst orbit has n4≤7+4=11. Only the second orbit, the two disjoint double edges, could still permit n4=12 via n4bar=7 and five cross pairs.

## 7. The second-orbit extremum is impossible

In the second orbit, C=165512, and the rank-four completed-tree deduction8536 leaves a deficit126. Contract all four-intersection components of Hbar.

Any cross-component pair of type0 or3 could be added to the quad forest in place of a baseline22 edge, gaining at least506−22=484>126; this would repair H. Thus every cross-component pair in a non-B input has type1 or2. If type2 occurs between two different pairs of contracted components, those two edges form a forest on the contracted graph; they can be selected simultaneously and gain2*(132−22)=220>126. Thus all cross-component type2 pairs lie between one fixed pair of components.

If n4bar=7 and its rank is four, the graph classification in §5 leaves just K4+pendant or K4 disjoint K2, plus isolated vertices. There are at most ten intra-component vertex pairs, seven of type4, so their total intersection surplus sum(|e∩f|−1) is at most7*3+3*2=27. In the first shape, one pair of components has at most5*1 original pairs; in the second at most4*2=8. Therefore the sole possible cross-component type2 class adds at most8 to the surplus. All remaining cross-component pairs have type1 and add zero. Hence

    sum_{unordered Hbar edge pairs} (|e∩f|−1) ≤27+8=35.

But the actual deleted degrees are six at p and the four B points, seven at the five U points, and eight at the ten nine-degree points. Thus

    Wbar=5*binom(6,2)+5*binom(7,2)+10*binom(8,2)=460,
    Wbar−binom(29,2)=460−406=54,

contradicting the upper bound35. The second orbit therefore cannot have n4bar=7, so it too has total n4≤11.

This proves the stated new necessary bound n4≤11 for every non-B reduced-A1 input, subject to the exact repair imports in §5. It does not prove H is colorable. Together with the earlier global weighted condition it forces n3≥8, even if tau=0, because17826*11+8838*7<259248.

## 8. Independent finite evidence and stopping scope

`GENERATE.py` enumerates all3060 multichoose keys, keeps the2835 cap-valid ones, covers them by the full S6 action, and saves every orbit member. It computes C by the red-nonempty/blue-nonempty inclusion–exclusion and directly enumerates184756 bitmask colorings for each of the three worst orbits.

`VERIFY.py` does not import that generator. It independently generates multiplicities0/1/2 with total four, recovers the same2835 full keys, and produces every orbit by breadth-first closure under adjacent transpositions. It checks all eighteen C counts with the alternative identity C=2*(no red mono link)−(no mono link of either color), and independently enumerates the three worst families using red ten-subsets. It also checks the scalar forest margins, Wbar=460, and the small five-vertex graph bound (the proof is in §5). Actual independent result PASS, approximately0.443CPU seconds; original calculation approximately0.119CPU seconds. No H or negative-layout enumeration was performed.

Reproduction:

```sh
.tools/math-python/bin/python context/propertyb35-paper/round01/middle/a1_balanced_star_forest_20261020/VERIFY.py
```

The complete orbit data, direct checks and CPU logs are `RESULT.json` and `VERIFY.json`. No lock table, Lean, MCP, wiki or navigation was changed. New proof/caller review and acceptance belong to the parent; this task asserts no new cross-family PASS and no full A1 closure. Further Hunter-rank subdivisions were intentionally not pursued.

## 9. Simplified uniform proof through incidence rank

The new general lemma is fully proved in canonical §4. For m distinct k-subsets of an n-set with m>n and n<k², the graph Γ joining original sets exactly when their intersection differs from one has forest rank at least m−n+2. The proof uses B=AAᵀ−J=A(I−J/k²)Aᵀ. The middle matrix is positive definite, so B and each principal block have the rank of the corresponding incidence rows. Any three distinct equal-positive-weight zero-one rows are independent: a relation gives w=t u+(1−t)v by row sums; coordinates in the two set differences force t∈{0,1}, making two rows equal.

B is block diagonal on Γ-components. Size-one/two blocks are nonsingular; a size-s≥3 block has nullity at most s−3. Since nullity(B)≥m−n>0, there is at least one component of size≥3, and total nullity is at most r−2. Thus r≥m−n+2. The explicit m>n assumption prevents extending this conclusion to the wrong parameter range.

For the29 original Hbar edges on20 points, Γ has rank≥11. Any four-edge quad forest extends to eleven edges inside Γ; its seven new edges have weights at least132. Complete to a tree with seventeen more edges of weights at least22. The single compatible tree gives

    4*2002+7*132+17*22=9306.

Even for the worst star count the good-coloring count is at least164896−174174+9306=28>0. Therefore a non-B input has Hbar quad rank≤3 and hence at most6 quad edges, without any K5/common-neighborhood or exceptional-star argument. The unique p-star has no quad neighbor; the other five stars each have at most one by the multiplicity-three repair. This gives total n4≤11 uniformly.

The canonical file preserves the whole earlier weighted/diamond/two-exception proof in an explicit appendix. Its main proof no longer imports the all-eight four-core theorem, complete-six top, five-top, or the earlier exact35-edge surplus54>35 argument. The complete2835/18 star-count evidence is unchanged. The verifier was rerun after adding the exact11/9306/28 scalar checks and passed in about0.427CPU seconds. The rank proof is general paper mathematics, not inferred from finite matrix examples. No new H/lock domain or search was introduced.
