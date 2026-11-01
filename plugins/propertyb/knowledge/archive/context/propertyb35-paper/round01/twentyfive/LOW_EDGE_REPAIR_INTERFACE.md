# CriticalLowEdgeRepair: five small positive sets from a real low-degree edge

For the23- and24-point minimum-degree-seven branches, the useful interface is an edge-critical hypergraph and an actual low-total-degree edge chosen **after** criticality. It gives at most five four-point positive constraints, with a total repeated-incidence budget6 or5. Negative singleton and pair constraints remain the principal unresolved obstruction. No free five-lock inventory is needed for this reduction.

## 1. The original counterexample must be made critical before choosing G

Assume a counterexample to the at-most35-edge assertion exists. Among all counterexamples choose one with the least number of nonisolated vertices, then the least number M of edges. Deleting any edge must make it colorable: otherwise a counterexample with fewer vertices, or the same number of vertices and fewer edges, results. Thus H is edge-critical. Identifying an uncovered pair would preserve five-uniformity and pullback colorability while reducing the vertex number, so the usual minimal-vertex argument also gives pair coverage.

The already established at-most33-edge theorem excludes M≤33. Hence M is34 or35. This normalization never adds edges. In particular, an internally padded35-edge H cannot be declared critical, and a low edge selected before taking a critical subhypergraph need not survive it.

Hereafter restrict to the actual branches n=23 or24 and δ(H)=7. Write d(G)=Σ_{g∈G}d(g). The four relevant low-edge bounds are:

| n | M | Total excess E=5M−7n | Selected actual G excess | d(G) | Seven-degree points in G |
|---:|---:|---:|---:|---:|---:|
|23|35|14|≤3|≤38=M+3|at least2|
|23|34|9|≤2|≤37=M+3|at least3|
|24|35|7|≤1|≤36=M+1|at least4|
|24|34|2|0|35=M+1|all5|

The M=35 bounds are the actual-edge selection theorem in `../literature-degree/GLOBAL_LOW_EDGE_REDUCTION.md`. For M=34,n=23, if the positive-excess set has at most four points, it cannot cover a non-B H, so an all-seven edge exists. Otherwise its size is at least5. For a maximum excess a, the general same-H second moment gives, on the27−a edges avoiding that point,

Σ T(e) ≤(a+7)(9−a)−4a <3(27−a),

because the difference is a²−a+18>0. Therefore some actual edge has T≤2. For M=34,n=24, E=2 means the positive-excess set has at most two points; its failure to cover a non-B H supplies an all-seven edge. These arguments select G inside the critical H.

This table covers exactly the four(n,M) pairs displayed. It does not cover21 points at minimum degree8: there the relevant G degree sum40 or41 does not satisfy d(G)≤M+3, and an eight-degree center has a different star budget.

## 2. The critical coloring makes G the unique bad edge

Since H is critical, color H\{G} properly. G must be monochromatic, or H would be colorable. Complement colors if needed so all five points of G are red. Let L be the initially blue points, all outside G.

The number m0 of actual edges disjoint from G satisfies

m0 ≥ M+4−d(G) ≥1.

Indeed incidences with G count G five times, so the number of different edges meeting G is at most d(G)−4. A zero-G edge is proper in the initial coloring, hence contains both a red and a blue exterior point. Thus the exterior is not all blue or all red.

Choose any seven-degree g∈G. There are at least two such choices in every row of the table. Flip g to blue, leaving all other colors unchanged. A newly blue monochromatic edge through g must have G-trace exactly{g} and all four exterior points initially blue. For every such indexed edge e define the positive four-set

A_e=e\{g} ⊆L.

There are initially at most d(g)−1=6 candidates. Choose an initially red exterior point x, supplied by the zero-G edge. Pair coverage gives an edge containing g,x; it is not G and cannot be one of these all-blue-exterior candidates. Therefore

m=number of positive four-sets ≤5.

This is a consequence of the actual low-edge degree bound, pair coverage and critical coloring together; it is not a property of an arbitrary five-lock trace inventory.

## 3. A second global budget: positive repetitions are at most6 or5

For x∈L let a_x be the number of positive A_e containing x. Then a_x≤λ(g,x), and pair coverage gives

Σ_{x∈L}(a_x−1)_+ ≤Σ_{v≠g}(λ(g,v)−1)
 =4d(g)−(n−1)=29−n.

Thus the positive family has at most five four-sets, at most twenty indexed incidences, and repeated-incidence surplus at most6 for n=23 or5 for n=24. In particular its union has size at least4m−(29−n). These budgets concern the same actual g-star and hold for every eligible seven-degree point of G.

For later use they can be kept symbolically rather than classifying the family. Under independent uniform selection from each positive four-set,

q_x=1−(3/4)^{a_x},   Σ(a_x−1)_+≤29−n,   Σa_x=4m≤20.

A nonuniform selection can instead use the exact occupancy lemma without changing the reduction.

## 4. Every negative constraint, including zero-G edges, is retained

After flipping g blue, allow only initially blue exterior vertices to turn red. For every original edge f avoiding g define the indexed negative set

B_f=f∩L.

It is nonempty because f was proper in H\{G}, and it has size at most4 because f also initially contained a red point. All M−7 edges avoiding g are included:27 for M=34,28 for M=35. This includes every zero-G edge. Identical sets at different edges retain their indices. If b_x counts negative occurrences of x, then a_x+b_x≤d(x): positive edges contain g and negative edges avoid g, so no original edge is counted in both families. This improved budget is legitimate specifically after the proper initial coloring, rather than from a fresh coloring of the exterior.

If R⊆L hits every positive A_e and contains no B_f, then flip precisely R to red. The common edge G now has g blue and its other four vertices red. An edge through g was either a newly blue bad edge repaired by hitting A_e, or already had an initially red point which remains red. It cannot become all red because g stays blue. An edge avoiding g cannot become all blue because red vertices never change, and cannot become all red because B_f is not contained in R. Thus this is a genuine completion to Property B of the original critical H.

Consequently, for any distributions π_e supported on the at-most-five positive four-sets, it suffices to prove

Σ_{f:g∉f} ∏_{x∈B_f}[1−∏_e(1−π_e(x))] <1.

This is exactly the general occupancy criterion in `proofs/propertyb35/RANDOM_TRANSVERSAL_REPAIR.md`, with no lost blue-bad alternative. A zero-G edge has no blue constraint in this **second-stage** repair because its initial proper coloring already contains red and the repair only turns blue to red; it is still explicitly a negative constraint.

## 5. The remaining mathematical obligation

The above is a proved interface, not a completed coloring theorem. The negative sets B_f may have size1 or2. For example a negative singleton{x} means x is forbidden in R; if a positive A_e consists entirely of such forbidden points, this one-direction repair is impossible from that starting coloring and center. Merely bounding the positive family by five sets does not remove this obstruction.

What remains is to exploit the freedom to choose the proper coloring of H\{G}, one of the at-least-two/four seven-degree centers in G, or a subsequent critical-edge transfer, so that the signed system satisfies the occupancy condition or another deterministic repair criterion. The positive repetition surplus6/5 and the actual low G degree budget are available as common constraints. No claim is made that these budgets alone force the probability sum below1.

## 6. Two additional precise boundaries

First, changing only the distribution of the colors of a protected G cannot solve the existing first-moment relaxation. On23 points consider the indexed trace model consisting of G itself, six singleton-trace edges per G point, and four zero-G edges. It has35 total edges, exact G degrees7, thirty singleton incidences, cross-G/outside incidence120≥90 and the required aggregate outer incidence/capacity budgets. Under any distribution on proper colors of G independent of a uniformly9/9 exterior, a singleton-trace edge has bad probability7/170 regardless of its G point's color, and a zero-trace edge has probability1/34. The sum is

30·7/170+4/34=23/17>1.

This is a precise moment-domain witness, without a claimed actual H realization. It shows that a purely independent reweighting of G colors cannot remove this obstruction. The critical repair interface instead uses a coloring of the actual H\{G} and its real blue parts.

Second, one can protect G in a different balanced color family and obtain exactly one possible bad edge. On23 points use2/3 colors in G and9/9 outside; on24 use total red12 and G red2 or3, so exterior red10 or9. For any nongroup edge, the bad-probability profiles by G-trace size0,…,4 are respectively

(1/34,7/170,7/170,2/85,0),
(21/646,7/170,62/1615,2/95,0).

Both have maximum7/170, so at most34 nongroup edges have expected bad count at most7/5<2. A state with at most one bad edge exists while G stays proper. On23 points allow all within-G and within-exterior opposite-color swaps plus the three G flips preserving its2/3 quota: ninety actions. A bad edge with trace size t is destroyed by45−6t actions; a critical1/4 edge creates a new monochromatic edge in4−t actions when its minority lies in G, and5+t when outside. On24 points all total-balance swaps preserving G quota2/3 give126 actions, destroy a bad edge at least42 times, and any critical edge creates a new bad edge at most8 times. These counts provide actual one-step blocker necessities, not a proof that a plateau exits.

`LOW_EDGE_REPAIR_INTERFACE_CHECK.py/json` checks these two finite probability profiles and exhausts all local color/group composition orbits for the90/126 action counts. It runs no hypergraph, five-lock inventory or free-point search. The critical-low-edge interface in §§1–4 is established by the preceding direct mathematical proof; the supplementary computation is not its substitute.
