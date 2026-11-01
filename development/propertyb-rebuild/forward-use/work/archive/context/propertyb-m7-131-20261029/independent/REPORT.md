# Independent feasibility check: m(7) ≥ 131

**PASS for the complete stated local numerical domain and its coverage.** The check finds no numerical or mathematical coverage gap in the 130-edge candidate. This is an initial independent implementation and same-family mathematical review, not Lean verification or a cross-family final acceptance.

`review_independence: same-family`; `acceptance_status: provisional`.

The independent `check.py` imports no probability, endpoint, type-profile, weight, or bad-pair function from the submitted programs. It computes probabilities by direct falling-factorial injection counts, reconstructs the final degree/type domains, and uses the recorded successful layouts. It enumerates every integer coordinate of the avoided-pair cell problem, including the core coordinate, rather than using the submitted forced-core optimization. Every resulting exact U equals the submitted CANDIDATE.json value.

Actual run: **424 profiles**, **2115296 complete avoided-cell integer vectors**, **2.47 CPU seconds**, all strict. Full reproducible inputs and exact outputs are retained in `check.py` and `RESULTS.json`. Run from the project root:

```
python3 context/propertyb-m7-131-20261029/independent/check.py
```

| Final domain | Profiles | Maximum U |
|---|---:|---:|
| v37–53, no locks |17|1286556007/1291140102|
| v54–66, two unit-codegree locks, avoided quotas |337|2257893910847/2257897608351|
| v67–70, three unit-codegree locks, avoided quotas |64|16888049333821/17060323720440|
| v71–73, three degree12 unit-codegree locks, whole-link quota |6|382700286307/383907604080|

The global maximum is at **v66, degrees(13,14), positions(33,34)**. Its exact margin below one is **3697504/2257897608351**, so using exact rational arithmetic matters.

## Probability and subtraction checks

Write `(a)_r=a!/(a−r)!`. Conditional on the fixed lock positions, named free vertices form a uniform injection into the N free positions. An edge with r free vertices ends at a free position h with probability `r(a)_(r−1)/(N)_r`, and at a locked endpoint with probability `(a)_r/(N)_r`, subject to its lock-position compatibility. Start events use the b free positions after h. An ordered single-intersection pair with r and u free vertices has critical weight `(a)_(r−1)(b)_(u−1)/(N)_(r+u−1)` at a free common vertex, or `(a)_r(b)_u/(N)_(r+u)` at a locked common vertex. These injection formulas, independently programmed, replace the original binomial functions.

The greedy failure witness remains valid for seven-edges: a final blue edge B has earliest vertex x, whose blue recoloring was forced by an all-red edge A ending at x. All other A vertices precede x, all other B vertices follow x, and A∩B={x}. No red edge remains. Thus the endpoint, start and critical-pair sums bound the same position-indexed bad event, allowing their minimum. The ordered type-pair count includes every actual distinct ordered edge pair and may overcount with nonnegative weights.

For a fixed center and a set R of other locks to avoid, f distinct incident edges give distinct six-element links on at most `n=v−1−|R|` vertices. If B is the number of unordered intersecting link pairs, incidence multiplicities satisfy

`6f = Σa_y ≤ n + ΣC(a_y,2) ≤ n + 5B`.

Distinct links have intersection size at most five by simplicity. Therefore every actual bad-pair vector satisfies the quota

`q_R=max(0,ceil((6f−v+1+|R|)/5))`.

This argument does not require the restricted avoiding subfamily to cover all n vertices. Each actual unordered pair occupies exactly one type cell, with capacity C(ell_T,2) or ell_T ell_U. Its removable coarse weight is the sum of both ordered weights. The independent program enumerates the entire rectangular integer cell domain and retains exactly vectors meeting every avoidance quota simultaneously. Its minimum objective is therefore a rigorous lower bound for the weight of actual bad pairs. No separately optimized quota values are added together, and zero-weight cells remain available. Subtraction is made only in the corresponding position's critical-pair bound.

At v71–73, the weaker whole-link quota suffices; independently taking the cheapest q copies in the full unordered pair weight multiset gives a valid lower bound on any actual set of q bad pairs.

## Reduction and complete original vertex domain

A counterexample with the fewest vertices must cover every vertex pair: otherwise identifying a pair absent from every edge preserves seven-uniformity, noncolorability and the edge budget. Duplicate images can be collapsed. Hence `6d(x)≥v−1` and `Σd≤7·130=910`.

For v≤12, take both color classes of size at most six. Every exact balanced-color union bound is <1 for 13≤v≤36; the independent program checks all 24 fractions. If v≥74, `v ceil((v−1)/6)≥74·13=962>910`. Thus every remaining counterexample has 37≤v≤73. Adding distinct edges to obtain exactly130 is possible since C(v,7)>130 throughout this range; it preserves noncolorability and pair coverage.

For v37–53, at least `ceil((130 C(7,2)−C(v,2))/C(6,2))` unordered edge pairs meet at least twice. This follows by summing C(lambda_xy,2), bounded below by `130 C(7,2)−C(v,2)`, and using intersection≤6 for distinct edges. Their two directions can be removed from the uniform no-lock ordered-pair count. All17 resulting exact bounds pass independently.

## Complete two-lock partner domains

For v54–66, let x have minimum degree d. Every possible d obeys `ceil((v−1)/6)≤d≤floor(910/v)`. Its codegree surplus is `e=6d−(v−1)`. At most e other vertices have codegree≥2 with x; at least `s=v−1−e=2(v−1)−6d` have codegree exactly one. The program checks s>0 for every actual minimum-degree case.

If all those unit-codegree neighbors had degree≥b+1, total degree would be at least

`d + ed + s(b+1) = vd+s(b+1−d)`.

Choose the first b≥d making this exceed910. A unit-codegree neighbor of degree in d,…,b exists. The independent script derives this bound from the degree contradiction directly, reconstructs every degree pair, and compares its complete key set against the submitted domain. This produces exactly337 profiles. With a unit-codegree pair the exact counts are `ell_xy=1`, `ell_x=d−1`, `ell_y=dy−1`, and `ell_empty=131−d−dy`. Both central adjacent position orientations are legitimate conditional permutation distributions. Every recorded winning layout is one of `(floor(v/2), floor(v/2)±1)` and independently passes; the proof requires existence of one good layout for each actual type, not a uniform choice for all types.

## Three-lock selection and incidence coverage

For v67–70, take degree ceilings D=14,13,13,13 respectively. Let L be vertices of degree≤D, r=|L|, and G join pairs in L of codegree≥2. Put `Z=(D+1)v−910` and `T=6(D+1)−v+2`. Total degree and point-pair coverage give

`r+2e(G)≤Tr−6Z`.

The actual left side is positive. Caro–Wei and Cauchy–Schwarz give `alpha(G)≥r²/(r+2e(G))≥r²/(Tr−6Z)`. The condition `24Z>2T²` implies `r²>2(Tr−6Z)` by completing the square, so alpha(G)>2. These exact conditions hold:

|v|D|Z|T|24Z|2T²|lower bound on r|
|---:|---:|---:|---:|---:|---:|---:|
|67|14|95|25|2280|1250|24|
|68|13|42|18|1008|648|21|
|69|13|56|17|1344|578|28|
|70|13|70|16|1680|512|35|

Thus three vertices of pairwise codegree one exist. At v67 their degree range is11,…,14; at v68–70 it is12,…,13. Relabeling allows sorted degrees. There are only two exact incidence patterns: one common triple edge, or three separate pair edges. The program independently reconstructs all sorted degree triples and both patterns, giving40+8+8+8=64 profiles, all strict at the stated central positions with avoided quotas.

For v71–73 every degree is at least12. At least `r=13v−910` vertices have degree exactly12: respectively13,26,39. Within this set the graph of codegree≥2 has maximum degree at most `73−v`, respectively2,1,0. Its independence number is at least `ceil(r/(74−v))`, respectively5,13,39, so three pairwise unit-codegree degree12 vertices exist in every case. Both incidence patterns are checked at each v, giving the final6 profiles. The 130-edge empty counts are96 in the common-triple pattern and97 in the separate-pair pattern, and these were independently reconstructed.

These cases partition all possible vertex counts after the original counterexample reduction and cover every necessary local degree/type input. No remaining parameter branch was found. This supports a complete computer-assisted proof candidate for **m(7)≥131**, subject to the project's further final-review process. No Lean, main plot, wiki, AGENTS, m6 evidence, or v2 file was changed by this task.
