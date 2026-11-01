# Independent review: minimum-degree-free low-Γ repair on21/22 points

**Verdict: the stated universal lemma is valid.** For a simple five-uniform H with35 edges on21 or22 vertices, a degree-at-most-one vertex of the graph Γ joining non-one-intersecting original edges gives a proper coloring. No original minimum degree, maximum degree or point-pair coverage is used. The argument only restricts the Γ-degree of the chosen edge F; the exceptional neighbor G may have arbitrary Γ-degree.

Review independence is same-family/provisional. This is an independent mathematical and exact scalar check; it does not modify the main proof or navigation and does not assert a larger vertex-count theorem.

## 1. Exhaustion and the original-degree identity

A Γ-isolated F and a degree-one F with disjoint exceptional G are already covered by the explicit no-degree rows of [the existing transfer proof](../low_nonunit_direct_repair_transfer_20261020/PROOF.md), §§2–3. Those rows were independently recomputed below.

For the only remaining case, q_Γ(F)=1 and j=|F∩G| belongs to{2,3,4}. Intersection one is excluded by the definition of G; intersection five would give G=F, excluded by simplicity. Every other one of the33 original edges meets F exactly once. Double counting point-edge incidences on F therefore gives the exact identity

    sum_{v∈F} d_H(v) =5+33+j=38+j.                          (1)

If a common point v∈F∩G has original degree at most nine, the existing common-point proof applies: take that v as the unique red point in F. G contains both this red point and another blue point of F, hence is already proper. Its other Γ-neighbors are irrelevant.

If no such common point exists, all j common points have integer original degree at least ten. Equation(1) gives

    sum_{v∈F\G}d_H(v) <=38-9j.

There are5-j such points. Consequently some actual v∈F\G has degree at most6,5,2 for j=2,3,4 respectively. These are upper bounds, not assumed degree values. Since F contains v its degree is at least one. With v unique red in F, the number c of the33 singleton edges attached at v is **exactly** d_H(v)-1, as v does not belong to G. Thus0<=c<=5,4,1 respectively. No edge through v is missed: F is removed, G avoids v, and every other original edge through v has singleton F-intersection{v}.

## 2. High-common-degree branch: exact sample and counts

Color F with only v red, its other four points blue. On N=n-5 outside points choose exactly ten red, the rest blue. F is proper. In the current branch G's j points inside F are all blue, so G is bad exactly when all its5-j outside points are blue. Its count is binom(N-5+j,10), including all and only compatible outside samples.

A red-attached singleton edge has outside four-set all red, with count R=binom(N-4,6); a blue-attached one has outside four-set all blue, with count B=binom(N-4,10). The total bad-event union is at most

    cR+(33-c)B+binom(N-5+j,10).                             (2)

Here R>B, so replacing c by its proved cap preserves the upper-bound direction. There is no independence assumption between these events or between G and the singleton edges.

|n|outside colors|sample D|R|B|j|c cap|G count|bound numerator|strict margin|
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
|21|10 red,6 blue|8008|924|66|2|5|286|6754|1254|
|21|10 red,6 blue|8008|924|66|3|4|1001|6611|1397|
|21|10 red,6 blue|8008|924|66|4|1|3003|6039|1969|
|22|10 red,7 blue|19448|1716|286|2|5|1001|17589|1859|
|22|10 red,7 blue|19448|1716|286|3|4|3003|18161|1287|
|22|10 red,7 blue|19448|1716|286|4|1|8008|18876|572|

Every numerator is strictly smaller than D, so an actual coloring of the same H makes every original edge proper. G is not deleted or silently made proper in this branch; its full bad-event probability is explicitly added.

## 3. Independent check of the older cases

For q_Γ(F)=0, choose a smallest of its five attachment groups, so c<=6 and there are34 singleton edges. For q_Γ(F)=1 with G disjoint, there are33 singleton edges and again c<=6; add G's two-color mono event. With outside samples10/6 at21 and10/7 at22, the fixed red-event-tree lower intersections are respectively28/8008 and36/19448, since any two outside four-sets have union at most eight. The elementary Hunter forest inequality on c red-attached event indices subtracts(c-1)_+ such counts on one common sample.

Independent maximization over c=0,...,6 recovers:

|n|isolated F|disjoint exceptional G|
|---:|---:|---:|
|21|259/286|7659/8008|
|22|4531/4862|2337/2431|

All are strict and require no point-degree assumption. G's event in the second column includes both colors.

For the common-degree-at-most-nine case in §1, c=d_H(v)-2<=7. At21 the outside9-red/7-blue sample has D=11440, red count792 and blue count220. Even the bare maximum at c7 is11264<D; this is the root's strict448/455. Keeping the optional red-event tree gives11216/D=701/715. At22 the outside10-red/7-blue sample has D19448 and the bare c7 count is exactly19448, so equality must not be called strict. The seven red-attached events admit a tree of six pairs, each joint count at least binom(9,2)=36. The resulting numerator19448-216=19232 gives2404/2431<1. Additional intersection of the outside four-sets can only increase the safe subtraction.

These are the actual event-index tree deductions of the existing proof, rather than independently subtracting probabilities from incompatible samples. No property of Γ at G is used in any calculation.

## 4. Actual conclusion and check evidence

The cases are exhaustive: q_Γ(F)=0; or q_Γ(F)=1 with j=0; or q_Γ(F)=1 with j∈{2,3,4}, subdivided according to whether a shared point has original degree at most nine. In each case F is proper by construction, all singleton original edges are included, and G is either demonstrably proper or has its exact remaining risk counted. Strict union upper bounds yield at least one proper coloring of all35 original edges.

[CHECK_MIN_DEGREE_FREE.py](CHECK_MIN_DEGREE_FREE.py) uses integer binomial counts and Fraction, rechecks every scalar row and every allowed c, and writes [MIN_DEGREE_FREE_REPAIR_REVIEW.json](MIN_DEGREE_FREE_REPAIR_REVIEW.json), PASS. Runtime is about0.0001 CPU seconds. It does not enumerate H or any outside-set family. No missing hypothesis or gap was found in the proposed universal21/22-point statement.
