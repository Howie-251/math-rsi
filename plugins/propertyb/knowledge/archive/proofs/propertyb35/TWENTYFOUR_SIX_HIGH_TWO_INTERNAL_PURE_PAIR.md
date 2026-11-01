# Twenty-four points: six high points, two internal edges, pure pair traces

Let H be a finite simple five-uniform hypergraph on24 vertices, with35 edges, pair coverage and minimum degree at least7. Put P={v:d(v)>7}. Assume:

- |P|=6 and H has no edge whose five vertices all have degree7;
- exactly two edges are contained in P;
- every other edge meets P in at most two points.

Then H has Property B.

In particular this proves the two-internal-edge, pure-six-pair-trace branch. Edges with three- or four-point noninternal P-traces are outside this theorem.

## 1. Actual P inventory and the coloring interface

The total excess above degree7 is5·35−7·24=7. Since there are six high points, their degrees are one9 and five8; call the nine-degree point h. All18 points of L=V−P have degree7. The absence of a full-seven edge implies that P hits **every** edge: an edge avoiding P would consist entirely of points of degree7.

The two different internal five-edges are P−{a} and P−{b}, for different a,b∈P. Put C=P−{a,b}, of size4. A point of C lies in both internal edges and a,b each lie in one; denote these internal degrees by c_v=2 or1.

The total P degree is49. Therefore

Σ_(e∈H)(|e∩P|−1)=49−35=14.

The two internal edges use8 of these units. Since all other traces have size1 or2, exactly six original edges have two-point P-traces and the remaining27 have singleton P-traces. The six pair traces form a loopless multigraph J on P, retaining different edge indices as parallel edges. Put s_v=d_J(v). The exact number of private singleton-trace edges at v is

u_v=d_H(v)−c_v−s_v.

For each partial coloring of P below, choose an exterior red set R⊆L and leave L−R blue. An edge whose P-trace already has both colors stays proper. An all-blue P-trace contributes its exterior set as a **positive** constraint, to be hit by R; an all-red P-trace contributes its exterior set as a **negative** constraint, not to be contained in R. Internal edges are checked separately. This exhausts all actual edges because P is a hitting set; no zero-P edge or other monochromatic alternative is omitted.

The positive and negative indexed source-edge families are disjoint. Each outer point's combined occurrence in the signed constraints is consequently at most its original degree7.

We use the following proved repair results:

1. [Five-positive signed repair](FIVE_POSITIVE_SIGNED_REPAIR.md), Corollary A: at most five positive four-sets, at most four negative triples and at most28 negative four-sets, with occurrence bound10, have a repair. The proved padding allowance applies to the actual bound7 here.
2. Its zero-triple corollary: at most eight positive four-sets and at most27 negative four-sets, with occurrence bound7, have a repair, without a ground-size restriction.
3. [Eighteen-point eight-four-positive repair](EIGHT_POSITIVE_18_ONE_TRIPLE.md): exactly eight positive four-sets, at most one negative triple and at most19 negative four-sets, on at most18 points with occurrence bound7, have a repair.
4. [Seven-mixed positive repair](SEVEN_MIXED_POSITIVE_ZERO_TRIPLE.md): at most seven positives of sizes3 or4, at most one a triple, at most21 negative four-sets, and occurrence bound7, have a repair.
5. [Eighteen-point eight-mixed repair](EIGHT_MIXED_POSITIVE_EIGHTEEN_REPAIR.md): exactly seven positive four-sets and one positive triple, at most20 negative four-sets, on at most18 points with occurrence bound7, have a repair.

The exact positive counts in results3 and5 will be preserved.

## 2. A single-blue center whenever s_p≥2 on C

Suppose some p∈C has s_p≥2. Color p blue and all other P points red. Both internal edges contain p and four red points. Every pair-trace edge incident with p is mixed and proper; the other6−s_p≤4 pair traces give negative triples. The private edges of p give

u_p=d_H(p)−2−s_p≤5

positive four-sets. This includes d_H(p)=9,s_p=2, which gives exactly five positives and four negative triples. All other private edges give27−u_p≤27 negative four-sets.

Result1 repairs the signed system. If u_p=0, take R empty. Thus H is colorable. We may henceforth assume

s_p≤1 for every p∈C.

## 3. The pair traces become a matching and two attachment families

The edges of J within C form a matching of size z∈{0,1,2}. Each unmatched C point is either isolated or has one edge attached to a or b. Let k_a,k_b count these attachments, k=k_a+k_b. All remaining J edges are ab, of multiplicity

x=6−z−k.

Since2z+k≤4, x≥2+z. These facts describe every actual J under the preceding degree restriction. They do not assume that an arbitrary trace multigraph has a full hypergraph realization.

Choose two blue P points {p,q}, with p∈C and q∈{a,b}, such that p is not attached to q. Let q' be the other point of {a,b}. The blue pair is independent in J, so there are no all-blue pair-trace edges and hence no positive triples. Each internal five-edge meets the two-point blue set and has at least three red points, so is proper.

Let η=1 if h∈{p,q}, zero otherwise. The number of all-red pair-trace edges is

t=z+k_(q')−s_p.

Indeed every ab edge meets q; the red matching and attachments are exactly those not removed by p or q. The number of private positive four-sets is

m=u_p+u_q
=13+η−s_p−x−k_q
=7+η+t.

The private negative four-set count is27−m. Thus:

- if t=0, m is7 or8, and result2 applies;
- if t=1 and η=0, m=8 exactly, with one negative triple and19 negative four-sets, and result3 applies on L of size18.

The following choices cover every nonstar shape.

## 4. Explicit selection by z and the attachments

**z=2.** There are no attachments. Choose p among the matching endpoints and q among a,b, both different from h. Then t=2−1=1 and η=0.

**z=1.** If all attachments lie at one endpoint q, choose p among the matching endpoints. Then t=1−1=0. This also covers no attachments. Otherwise k_a=k_b=1, since at most two C points are unmatched. Choose q≠h and a matching endpoint p≠h; then t=1+1−1=1 and η=0.

**z=0 and min(k_a,k_b)=0.** If k≤3, take q at the attached endpoint, or either if k=0, and choose an isolated C point p. Then t=0. If k=4, all four C points attach to the same endpoint q; this is the star case treated in §5.

**z=0 and min(k_a,k_b)=1.** Choose q so that q' has exactly one attachment and take p at that attachment. Then t=1−1=0.

**z=0 and min(k_a,k_b)=2.** Necessarily k_a=k_b=2. Choose q≠h and choose p among the two attachments to q', with p≠h. Then t=2−1=1 and η=0.

All choices exist. A matching has at least two endpoints, and the last case has two attachments at q', so a single nine-degree point cannot exclude all eligible p. The t=0 cases permit h in the blue pair, since either7 or8 positives satisfy result2. Every chosen pair is independent in J by construction. Therefore the applications in §3 color every nonstar shape.

## 5. The four star degree placements

The only remaining pair-trace multigraph has star center q∈{a,b}, with one edge qp for each p∈C and two edges ab. Then

s_p=1 (p∈C), s_q=6, s_(q')=2.

Choose p∈C different from h and color p,q blue, leaving the other P points red. Both internal edges are proper. The pair trace pq is all blue and gives exactly one positive exterior triple. Every other pair trace meets blue q and a red P point, so is already proper; there are no negative triples.

The chosen p has degree8 and two internal incidences, hence u_p=8−2−1=5. At the star center,

u_q=d_H(q)−1−6=d_H(q)−7.

If q has degree8, this is1. Thus there are exactly six positive four-sets and one positive triple, while the remaining27−6=21 private edges give negative four-sets. Result4 applies. This includes both cases h∈C and the case h=q', without a separate unproved symmetry assumption about the degree-nine point.

If q=h has degree9, then u_q=2. The signed system has exactly seven positive four-sets and one positive triple, no negative triples, and27−7=20 negative four-sets. Its ground set is the18-point L, and its indexed occurrence bound is7. Result5 applies with its exact counts.

For reference, fixing C={0,1,2,3}, a=4,b=5, and placing h at0 or4 yields the complete four labeled degree placements:

| h | Star center | Blue P points | Positive family | Negative family |
|---:|---:|---|---|---|
|0|4|{1,4}|6 four-sets +1 triple|21 four-sets|
|0|5|{1,5}|6 four-sets +1 triple|21 four-sets|
|4|4|{0,4}|7 four-sets +1 triple|20 four-sets|
|4|5|{0,5}|6 four-sets +1 triple|21 four-sets|

No positive triple is discarded or enlarged. The last row and the first two use the seven-positive theorem; the third uses the exact eight-positive mixed theorem.

## 6. Conclusion and verification scope

In every case the repair gives R⊆L meeting all positive constraints and containing no negative constraint. Coloring R red and L−R blue completes the fixed P colors to a proper coloring of every original edge, by the actual-edge interface of §1. This proves the theorem.

The proof of structural coverage is §§2–5, not a table of hypergraphs. The auxiliary [six-high-point report](../../context/propertyb35-paper/round01/twentyfive/k6_two_internal/REPORT.md) preserves the short exploratory multigraph profiles with their actual scopes. Its independent `SELECTOR_REPLAY.py/json` generates exactly the matching-and-attachment domain and checks all selected signed counts. `PURE_PAIR_FINAL_CHECK.py/json` independently restores the actual degree/private-edge counts for the230 zero-triple,42 one-triple and4 star labeled inputs, and checks their exact repair theorem interfaces. Those parameter counts are supplementary to the analytic case split.

The repair theorems carry their own stated dependencies and local exact count checks, including the seven and59 graph-orbit counts in the two eighteen-point gates. No claim of the entire six-high-point/two-internal branch is made when noninternal three- or four-point P-traces occur. No point outside P is freely added to the trace domain, and no original hypergraph is enumerated.
