# Balanced A1 event repair by compatible chordal triangles

## Result and exact scope

There is a valid general clique-Euler upper bound when the chosen event graph has an ordering in which every earlier neighborhood is a clique. In particular a triangle attachment to an existing edge is safe. For three original five-edges meeting pairwise in three points, a triangle attachment improves its compatible parent-forest deduction by exactly 0, 440 or 550 balanced colorings according as their common intersection has size 1, 2 or 3.

This yields the explicit conditional A1 coloring criteria in §4. No present argument forces the needed compatible triangles from all remaining A1 inputs. The residual moment profiles record pair intersections, not these three-edge geometries, so they cannot by themselves be declared eliminated by this refinement. No new lock domain, original-H enumeration or negative-layout search was performed.

The already accepted near-saturation result was copied separately to [THREE_INTERSECTION_MIDDLE_NEAR_SATURATION.md](../../../../../proofs/propertyb35/THREE_INTERSECTION_MIDDLE_NEAR_SATURATION.md). Its original evidence and the earlier shared-middle canonical were preserved.

## 1. General pointwise clique-Euler inequality

Let E1,...,Em be arbitrary events on a common probability space. Choose a graph K on their original indices and an ordering 1,...,m such that the earlier neighbors Ni of every i form a clique. Empty earlier neighborhoods and disconnected graphs are allowed. This explicit ordering is the certificate used here; a chordal graph may be supplied by a reversed perfect elimination order. Define

    Y = sum_i 1_Ei product_{j in Ni}(1-1_Ej).

For a fixed outcome with at least one active event, its earliest active index contributes one. Every other summand is zero or one. Hence, pointwise,

    1_{union Ei} <= Y.                                             (1)

Expanding each product, every nonempty clique is counted exactly once, at its largest index. Conversely every expanded term is a clique because Ni is a clique. Thus

    Y = sum_{nonempty cliques Q of K} (-1)^(|Q|+1) 1_{intersection_{i in Q} Ei}.       (2)

This proves the clique-Euler union upper bound without independence or a probabilistic association assumption. It also explains its graph condition: adding a vertex whose earlier active neighbors form a nonempty clique joins exactly one active component, so Y equals the number of components in the active induced graph. If that neighborhood is empty it creates one component.

For a construction whose earlier neighborhoods have size at most two, (2) has only singleton, pair and triangle terms. Such a graph can be constructed by introducing isolated vertices, attaching a new vertex to one old vertex, or attaching a new vertex to the two ends of an existing edge. These operations suffice for every certificate below. The graph need not contain every actual intersecting event pair; omitted event-pair terms are simply not used.

The hypothesis cannot be dropped. Four identical active events with the chosen graph a chordless four-cycle give singleton sum minus pair sum equal to 4-4=0 although the union indicator is one. Filling triangles arbitrarily or adding gains from unrelated cycles is therefore invalid.

## 2. A triangle attachment and its compatible parent forest

For every attachment of a new vertex v to the old edge ab, retain either va or vb as its parent-forest edge. Retain the single edge for a one-neighbor attachment. These retained edges form a forest F having exactly the same components as K. In a triangle attachment, if va is retained, its additional deduction beyond F is

    count(Ev intersect Eb) - count(Ev intersect Ea intersect Eb).  (3)

This quantity is nonnegative, since the triple event is a subset of the pair event. Each attachment has a distinct new vertex, so every selected pair and every selected triangle is counted once by (2). In particular no pair-intersection probability is subtracted a second time without its required triple-event correction.

One may extend F to a spanning forest inside any larger graph by edges joining its components. Because F and K have the same components, the identical edges are bridges between components of K, preserve the ordering property, and add only their pair deductions. This gives a useful compatibility rule: a forest extension of this particular F is safe. The globally maximum Hunter tree need not contain F. Its weight cannot simply be added to all the gains (3).

## 3. Exact three-edge geometry and balanced counts

Let A,B,C be three distinct five-sets with each pair intersection of size three. Set t=|A intersect B intersect C|. Their seven Venn atoms have sizes

    common atom t;
    each of three pair-only atoms 3-t;
    each of three single-only atoms t-1.

Nonnegativity gives t in {1,2,3}, and their union has size 6+t. This is the full local classification, up to relabeling. All three pair intersections are nonempty, so simultaneous monochromaticity forces the same color on their whole union. On a fixed 20-point ground colored uniformly 10/10, its numerator is

    2 binom(20-(6+t),10-(6+t)).

The exact values are:

| t | union | triple-event numerator | each pair numerator | attachment gain |
|---:|---:|---:|---:|---:|
|1|7|572|572|0|
|2|8|132|572|440|
|3|9|22|572|550|

For t=1 there is one common point and three pair-only two-sets. Each of A,B,C is the seven-point union with one of those disjoint two-sets removed. Two monochromatic members already force the third monochromatic. Their three pair events are identical, and subtracting the third pair without adding the triple would give a false improvement. These are genuine simple five-set configurations and are not ruled out just by the current point-pair cap four.

For t=2 the common two-set, three pair-only points and three private points give the eight-point configuration. For t=3 there is a common three-set and three disjoint private two-sets. Both yield a strictly positive attachment gain. No four-set occurs in all three edges in either configuration, so the existing four-core multiplicity-three repair does not automatically eliminate these configurations.

## 4. Actual A1 conditional coloring theorem

Let H have the reduced A1 roles, let x be its six-degree point, and let Hbar be its 29 original edges avoiding x. Use the same balanced 10/10 sample space on V minus {x}. From [the balanced-star forest theorem](../../../../../proofs/propertyb35/TWENTYONE_A1_BALANCED_STAR_FOREST.md), the star-compatible event C has at least 164896 colorings. The 29 monochromatic events have total numerator 174174; therefore any valid deduction D satisfying

    D > 9278                                                     (4)

produces a coloring in C proper on Hbar. Assigning x a color with no monochromatic link then makes every original edge proper. The argument uses the union bound Pr(C intersect proper) >= Pr(C)-Pr(union bad), not conditional independence.

Supply a graph construction from §1, with its compatible forest F, whose triangle attachments all consist of pairwise-three-intersecting original edges. Write g2,g3 for attachment counts of triple-intersection size two and three. Attachments of common size one are allowed but give zero gain. Complete F by compatible bridges to a spanning tree T. With pair weights

    w0=506, w1=22, w2=132, w3=572, w4=2002,

a sufficient criterion is exactly

    sum_{e in T} w_{|intersection(e)|} + 440g2 + 550g3 > 9278.      (5)

All terms refer to original Hbar edge indices. This is a conditional original-H theorem, not an assertion that such a certificate always exists.

There is a convenient rank-assisted version. Suppose every edge of F has non-one intersection and r=|F|<=11. The general Gram-rank lemma already proved in the linked theorem gives forest rank at least 11 for the graph of non-one intersections of Hbar. Extend this particular F to 11 edges there; all newly used weights are at least 132. Complete to a spanning tree using 17 further edges of weight at least 22. If F has q0,q2,q3,q4 edges of the indicated intersection types, then

    D >= 1826 + 374q0 + 440q3 + 1870q4 + 440g2 + 550g3,            (6)
    1826 = 11*132 + 17*22.

Every extension edge is a bridge between components of the construction graph, so (6) is compatible with the triangle corrections. The threshold remains strictly greater than 9278.

Examples of sufficient certificates are:

| parent forest counts (q4,q3), other counts zero | g2 | g3 | guaranteed D |
|---:|---:|---:|---:|
|(3,3)|0|1|9306|
|(3,3)|2|0|9636|
|(3,4)|1|0|9636|
|(2,7)|2|0|9526|
|(2,8)|1|0|9526|
|(0,11)|6|0|9306|

A triangle attachment uses two parent vertices and a new vertex; hence these numerical rows require an actual construction realizing the listed numbers. In particular they do not assert that every forest with those edge types admits the indicated attachments. The near-equality margin 28 in the first and last rows is exact.

## 5. A small book diagnostic and actual capacity interaction

A particularly transparent construction fixes one three-intersection edge A,B of the event graph and attaches distinct original Hbar edges C as pages, each with |A intersect C|=|B intersect C|=3. This is a valid two-tree irrespective of unused intersections between pages. Write m1,m2,m3 for page counts of the three common-core types in §3.

Let K=A intersect B, |K|=3. A type-one page contains the exclusive four-set (A minus B) union (B minus A), and one point of K. There are only three possible distinct type-one pages. In a remaining non-B A1 input the four-core multiplicity-three repair forbids all three, so m1<=2. A type-two page contains exactly one pair of K; a type-three page contains all K. For each of the three pairs P in K, the two original edges A,B already use two of the cap lambda(P)<=4. Thus

    m2 + 3m3 <= 6.                                               (7)

This is a shared capacity constraint; the looser independent bounds m2<=6,m3<=2 must not be saturated simultaneously.

With only the book parent forest and baseline 22-weight bridges, its exact lower deduction is

    1166 + 550m1 + 990m2 + 1100m3 <= 8206.

With the guaranteed non-one forest rank 11, (6) gives at most 8426 under the same scalar constraints. These are maxima of these lower-bound formulas, not upper bounds on the best actual coloring deduction. They show that a generic single-book certificate, ignoring further page intersections, does not suffice uniformly.

There is one useful conditional strengthening. If m1=2, the two type-one pages meet in four points. Start the construction with that four-intersection pair, attach A to that edge, then attach B along A and one of the pages; attach all remaining pages along AB. The first two triangles have triple numerator 572 and retained extra pair weight 572, so their gains are zero. The compatible forest now contains one weight-2002 edge instead of one weight-572 edge, a gain of 1430. If also m2=6 (necessarily m3=0 by (7)), the nine-edge parent forest plus two non-one extension edges gives

    D >= 1826 + 1870 + 8*440 + 6*440 = 9856 > 9278.

Thus this saturated eight-page book is repaired without an additional lock table. Existence of such a book is not established for every residual input.

## 6. What remains missing for a global consequence

With the earlier n4<=11 import, the strengthened C3<=13n3 middle capacity and the intersection moments left 80 aggregate profiles, with minimum (n3+n4)=33; one minimum profile had n3=22,n4=11,tau=0. The later scalar update below uses the stronger n4<=8 import and leaves 25 profiles. These counts concern all 35 original edges, whereas the chordal certificate concerns the particular 29 Hbar indices and their actual joint intersections. Neither the moments nor the current n4<=11 bound specify g2,g3 or compatibility with a high-weight parent forest.

A sufficient next structural statement would be: every remaining actual input admits one of the construction certificates satisfying (6), or an equally strong full clique-Euler certificate. No such statement is proved here. A large triangle count alone is insufficient without excluding the type-one degeneration and arranging compatible attachments. A high pair-graph rank alone supplies only Hunter deductions already available. The three local geometries above locate exactly which additional three-edge information the new method can use.

The scalar and local-geometry checks are [CHECK.py](CHECK.py) and [CHECK.json](CHECK.json). They verify the three Venn realizations, event numerators, the pointwise inequality for explicit small construction graphs, the chordless-cycle failure, threshold arithmetic and book capacity maxima. These are deterministic checks of this conditional argument, not a generated A1 classification or a new global non-B exclusion. Review status: same-family, provisional.

## 7. Subsequent cheap shared-capacity filtration

Parent-supplied, root-checked updates give at most three original singleton-graph vertices with sF=34 and original n4<=8. This section only evaluates their consequences; it does not independently prove those two imports or claim new cross-family acceptance. The linear path budget becomes

    P <= (132 n1+198)/5,

while the already proved singleton-graph threshold majorant T(35,n1,0) must still be retained. We therefore recompute Pbound=min(T,(132n1+198)/5), not a blanket subtraction from the old greedy objective. The corresponding purely linear necessary inequality is

    494 n3+1175 n4-313 tau >=21736.

[CAPACITY_FILTER.py](CAPACITY_FILTER.py) independently loops the full 21615 integer moment profiles with tau in0..140, n4 in0..8, nonnegative n0..n4, and 397<=n1<=546. It uses C3<=13n3 and the other unchanged Cj caps, the exact rational greedy highest-weight allocation, and the frozen threshold-majorant values from the earlier verified recurrence. The before/after linear constants594 and198 both leave exactly25 profiles: **no additional profile is removed**. All25 surviving profiles are threshold-bound rather than linear-bound, which explains the lack of gain. CPU0.659 seconds.

The residual extrema are min n3=29, min(n3+n4)=37, max tau=7. A minimum-high example is

    (n0,n1,n2,n3,n4)=(34,519,5,29,8), tau=0,
    Pbound=13074 < (132*519+198)/5=68706/5,
    (C0,C1,C2,C3,C4)=(0,12545,120,377,32),
    L=2730456 >=2722720.

This is a feasible aggregate allocation, not an original H. The full25 keys and exact values are in [CAPACITY_FILTER.json](CAPACITY_FILTER.json). A genuinely joint singleton-graph bound imposing at most three vertices of degree34 could be stronger than taking the minimum of the independent threshold and linear bounds, but is not proved or computed here. No further domain expansion follows from this zero-gain result.
