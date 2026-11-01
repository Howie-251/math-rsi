# Independent exact arithmetic and real-domain check for m(6) ≥ 66

Status: **PASS for the stated numerical and mathematical coverage obligations.**
`review_independence: same-family`; `acceptance_status: provisional`.
No Lean, external reviewer, whole-hypergraph enumeration, wiki changes, or v2 access.

`check.py` is a new implementation importing no original numerical module. It passed with **379 final necessary local profiles** and **621579 complete avoided-cell integer vectors** in **1.49 CPU seconds**. Reproduce from project root:

```
python3 context/propertyb-m6-66-20261029/independent/check.py
```

`RESULTS.json` contains every input type, winning layout, exact value, the independently recovered K4 patterns, and selection arithmetic. Input certificates supply layouts but do not supply computed probabilities. All final values and comparisons are `Fraction`/integer. Every imported exact U matched the independently computed value. The two v32/minimum12 cases are new independently computed entries.

## Independently counted probability terms

For a uniform injection of named free vertices into N available slots, write `(a)_r=a!/(a-r)!`. An edge with r free vertices ends at a free position h with probability `r(a)_(r−1)/(N)_r`, provided all its locked vertices are before h; at a locked endpoint it has probability `(a)_r/(N)_r`, provided its locks fit. Start probabilities use the free slots b after h.

A single-intersection ordered pair with its common vertex free uses r+u−1 free vertices. Its common vertex is fixed at h, with the remaining named vertices on the two sides, so its weight is `(a)_(r−1)(b)_(u−1)/(N)_(r+u−1)`. A locked common vertex gives `(a)_r(b)_u/(N)_(r+u)`. These direct injection counts were used, with the appropriate lock-compatibility checks. They are derived separately from the original binomial implementation.

The greedy argument is valid: initially all red, turn a processed vertex blue exactly when an all-red edge ends there. No final red edge survives. A final blue edge B has a first vertex x; the red edge A that forced x blue ends at x. All other vertices of A are earlier and all other vertices of B later, hence A∩B={x}. Thus endpoint, start and critical-pair unions bound the same failure event at each h, allowing their minimum. All ordered distinct type pairs provide a nonnegative overcount of the genuine single-intersection pairs.

## True bad-pair subtraction

For a center x and edges avoiding a subset R of the other locks, their f distinct five-point links lie on at most n=v−1−|R| vertices. Their incidence multiplicities a_y satisfy

`5f = Σ a_y ≤ n + Σ C(a_y,2) ≤ n + 4B`,

where B counts unordered link pairs with nonempty intersection. The last factor is four because distinct links of a simple six-uniform hypergraph cannot share five vertices. This establishes every quota used in the new certificate, without requiring the avoiding subfamily itself to cover those n vertices.

Actual beyond-center-overlap pairs form a single feasible integer vector in the unordered type cells, with the declared capacities. All avoidance constraints hold for that same vector. Minimizing one weighted objective over this joint feasible set gives a lower bound on its actual removable weight. This does not sum separately optimized, incompatible quotas.

The independent v37 replay enumerates **every coordinate including the singleton/singleton core**, scales rational weights to exact integer costs, checks every quota, and minimizes the whole objective. Across 70 profiles and 210 centers it inspects **621579** integer vectors. All 70 U values match V37_THREE.json; maximum **2458/2465**. It does not reuse the submitted forced-core formula. Removing weights at different center positions is valid because those are separate position-indexed probability bounds; a non-single-intersection pair is never a genuine critical witness at any of them.

For the other lock domains the weaker whole-link quota is sufficient. Independently sorting the full unordered-pair weight multiset and taking its q cheapest copies gives a lower bound on the weight of any actual set of at least q bad pairs. In particular zero-weight cells remain in this minimization. Both directions of each unordered pair are present in the ordered bookkeeping sum, so their sum is exactly its removable weight.

## Original-domain reduction and small/large point ranges

A counterexample chosen with the fewest vertices covers every vertex pair: identifying a pair absent from every edge preserves six-uniformity, noncolorability and the edge bound, contradicting minimality. Duplicate images may be collapsed without affecting noncolorability. For its actual degree and codegree, `5d(x)=Σ_(y≠x) λ_xy ≥ v−1` and `Σd≤390`.

Balanced sampling gives `65[C(floor(v/2),6)+C(ceil(v/2),6)]/C(v,6)<1` throughout 11≤v≤26; the independent program checks all these exact fractions. At v≤10, two color classes of size at most five work. For v≥44, `v ceil((v−1)/5)≥44·9=396>390`. Thus only 27≤v≤43 remains. At those sizes there are more than 65 possible six-edges, so padding to exactly65 preserves pair coverage and noncolorability.

For 27≤v≤31, `Σ_(x<y) C(λ_xy,2) ≥ 975−C(v,2)`. A pair of distinct edges contributes at most C(5,2)=10. Consequently at least q=ceil((975−C(v,2))/10) unordered pairs meet at least twice, and there are at most 65·64−2q ordered single-intersection pairs. The new injection-count implementation checks all five corresponding zero-lock bounds strictly below one.

## Complete two-lock domains, v32–36

Let d be the minimum degree, and let e=5d−(v−1). At most e other vertices have codegree≥2 with a fixed minimum-degree vertex x. If all its codegree-one partners had degree≥t+1, total degree would be at least

`d + (v−1−e)(t+1) + ed`.

Whenever this is >390 a partner of degree at most t must exist. Every such partner has degree≥d. For every minimum degree allowed by `ceil((v−1)/5)≤d≤floor(390/v)`, the independent program reconstructs the smallest sufficient t, verifies that ROOT_TWO_LOCKS.json contains exactly all e-partner degrees d,…,t, and independently checks each winning layout. The sole replacement is v32/d12, treated next. This produces 33,26,21,17,13 cases at v32,…,36 respectively; no minimum-degree branch is omitted.

At v32/minimum12, total degree390 permits excess only6 above the baseline384. Thus at least26 vertices have degree12. Fix one such x. If all other at least25 degree12 vertices had codegree≥3 with x, then `Σ_(y≠x)(λ_xy−1)≥50`, contradicting its exact excess `5·12−31=29`. A second degree12 vertex y therefore has codegree1 or2. These two profiles have respective type counts `(ell0,ellx,elly,ellxy)=(42,11,11,1)` and `(43,10,10,2)`. At positions(16,17), independent exact values are **294523/300150** and **898423/900450**. The λ2 profile uses the same valid whole-link deletion, without assuming pairwise unit codegree.

## Selection of triples and quadruples

Let L contain the vertices of degree≤D, r=|L|, and G on L join pairs with codegree≥2. Put `Z=(D+1)v−390`, `T=5(D+1)−v+2`. Pair coverage and total degree give

`r+2|E(G)|≤Tr−5Z`.

The actual left side is positive, so its upper bound is positive. Caro–Wei, followed by Cauchy–Schwarz, yields `α(G)≥r²/(r+2e)≥r²/(Tr−5Z)`. For n selected vertices, `20Z>(n−1)T²` implies `r²>(n−1)(Tr−5Z)` by completing the square, hence α(G)>n−1. The independent program checks this strict sufficient condition for (v,D,n)=(37,12,3),(38,11,3),(39,10,3),(40,10,4),(41,9,4),(42,9,4),(43,9,4). In particular v37 has 1820>1800. It also explicitly checks the resulting inequality at every allowed integer r.

Every pair of chosen vertices has codegree exactly one, using pair coverage. For triples the two possibilities are one common triple edge or three distinct pair edges. The independent domain comparison checks all sorted degree tuples and both patterns: **70,40,20** cases for v37,38,39. Sorting the degrees loses no input because the tuple may be relabeled; at v37 the actual degree-order permutation and layout recorded in each certificate are independently used. All profiles have a valid winning permutation, while no uniform winning order is presumed.

For four locks, each edge meeting at least two locks defines a clique on its lock intersection. Those clique edge-sets partition K4 because every lock pair has codegree one. A clique of size three excludes any other triple or larger clique; its three remaining pairs must be separate 2-cliques. A clique of size four covers all pairs. Otherwise all six are 2-cliques. Hence the complete labelled classification consists of six separate pairs, one of four possible triangles plus its three complementary pairs, or one K4: **six labelled patterns**.

The independent implementation instead enumerates all 2048 subsets of the eleven possible K4 cliques and accepts precisely those whose incidence at each pair equals one. It obtains those six patterns. It then checks equality of the submitted domain with every sorted degree tuple and every labelled pattern, with counts **90,30,6,6** at v40,…,43. This includes every triangle label relative to unequal sorted degrees. No extra type of size≥2 or multiplicity>1 is possible; singleton and empty counts are fixed by degrees and total edge count.

## Exact maxima

| Domain | Cases | Maximum U |
|---|---:|---:|
| v27–31 zero locks |5|5518669/5582790|
| v32 two locks, minimum7–11 |33|179393/180090|
| v32 minimum12, codegree1/2 |2|898423/900450|
| v33 two locks |26|7361359/7443720|
| v34 two locks |21|7417903/7443720|
| v35 two locks |17|682298/682341|
| v36 two locks |13|22662778/22695255|
| v37 three locks, joint avoided quotas |70|2458/2465|
| v38 three locks |40|1725092/1730575|
| v39 three locks |20|6205343/6230070|
| v40 four locks |90|3141/3190|
| v41 four locks |30|1375025/1397046|
| v42 four locks |6|241664898/243318845|
| v43 four locks |6|12775536/12806255|

Every maximum is strictly below one; the global maximum is **682298/682341** at v35, degrees(10,12), positions(17,18). This independently verifies the final finite arithmetic and its complete necessary local parameter domain. Together with the reduction and probabilistic arguments checked above, it supports the stated computer-assisted proof of every ≤65-edge finite simple six-uniform hypergraph being two-colorable. It is not a Lean theorem or a cross-family final review.

## Root readback and exact rerun

The root read the full assembled proof and this independent implementation. An explicit degree-permutation equality check and legal/distinct position checks were added, then the complete verifier was rerun successfully; see `ROOT_REPLAY.log`. The accepted v37 layouts are (17,18,19) for 68 profiles and (15,16,17) for the two all-degree-12 profiles. The original JSON certificates already recorded these positions; an earlier prose assertion that all 70 used the central layout was corrected. The final bound and all 379 numerical witnesses are unchanged. The rerun used approximately 1.40 CPU seconds.
