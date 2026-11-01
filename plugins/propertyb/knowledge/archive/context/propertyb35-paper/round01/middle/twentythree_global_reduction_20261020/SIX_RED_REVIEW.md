# Six-red lemma and q2 anchor: independent review

review_independence: same-family
acceptance_status: provisional
verdict: PASS_WITH_DECLARED_IMPORTS

Reviewed `SIX_RED_PROOF.md` in full. No mathematical gap found. This review proves neither the entire23-point coloring branch nor the global m(5)≥36 claim. The consequence is: for23 vertices,35 distinct five-edges, and minimum vertex degree at least7, non-Property-B implies minimum degree at least3 in the edge graph Γ of intersections different from1. Its q≤1 part imports the existing theorem in `../twentythree_low_nonunit_degree_20261020/PROOF.md`; q2 uses the newly reviewed six-set lemma and the bounded anchor coverage below. No pair-cover assumption is needed in this q2 argument.

## Analytic proof checks

1. **Graph rank classification.** If the ≥2-intersection graph has rank≤2, every nontrivial component has size≤3 and the total of component sizes minus1 is≤2. Hence precisely empty, one edge, two disjoint edges, a three-vertex path, or a triangle remain. The three rank2 heavy shapes are exhaustive. A ≥3-intersection edge with rank2 can always be included in a two-edge heavy forest, including the triangle case.
2. **A three-intersection pair with heavy rank1.** The heavy graph then consists of that single pair. If the nonempty-intersection graph had rank≤2, its component partitions could only be one pair plus four singletons, two pairs plus two singletons, or one triple plus three singletons. Their support lower bounds21,20,19 are correct: the special pair has union5, another light pair has union7, and a third set adjoining the special pair has at most two points in its union and therefore adds at least2. Supports of different components are disjoint. Thus rank≥3, and the forest deduction1716+2·330+2·120=2616 follows.
3. **Bonferroni directions and triple counts.** With all pair intersections≤2, the total pair-incidence budget m1+2m2≥6 follows from24 union incidences on≤18 points. Triple union size is12 minus pair intersection sum plus the triple intersection, so dropping the last term gives a valid lower union bound and hence an upper event count. The sequences(0,1,8,36), (8,36,120), and the linear allowances12s and96+12s have the stated directions. Each pair belongs to exactly4 of the20 triples.
4. **Heavy path and m1=2.** The unique double-heavy triple has at most120/330 event states according as its closing pair has intersection0/1. The 126 correction is330−(2·96+12). If m1=2 and the closing pair is light, the other6 heavy-containing triples cannot contain that closing pair, so have at most one light pair and contribute≤36 each. The13 no-heavy triples have at most two light pairs, giving≤8 each. Thus330+6·36+13·8=650 and S2=3564, deduction2914. If the closing pair is absent, no positive correction is required and deduction2700 suffices.
5. **Heavy triangle.** Its sole all-heavy triple has union≥6 and event count≤792. The other classes have9 exactly-one-heavy and10 no-heavy triples. The improved bound8+56s holds at s0/1/2, with values8/64/120 dominating8/36/120. Every light pair occurs in4 triples, none in the all-heavy triple; therefore the incidence identity X+Y=4m1 is exact, not an independence claim. S3≤864+224m1 and m1≤12 give S2−S3≥2784.
6. **More than six red sets.** The union-of-six event is a single event. Each added red event has intersection at least120 with that union because it intersects one fixed original event in at least120 states. Iterative union bounds therefore justify2616+120(a−6) without combining incompatible anchors.

All arithmetic deductions in the manuscript were checked directly against the binomial counts. In particular2616 is achieved by the two limiting forest arguments; all stated Bonferroni branches exceed it.

## Independent q2 coverage

Executed `python3 -B context/propertyb35-paper/round01/middle/twentythree_global_reduction_20261020/Q2_INDEPENDENT.py`.

The independent implementation does not import the earlier profile or use S5 orbits. It takes all26 allowed traces (empty or sizes2/3/4), all351 unordered trace pairs with repetition, then all150315 labeled singleton-count compositions. The composition loops use four nondecreasing cuts, independently of the earlier recursive generator. Per-trace composition totals are checked against the direct binomial formula.

For each original F vertex i, the two exceptional indexed edges give h_i incidences. Actual minimum degree7 implies a_i≥6−h_i and the other32 singleton edges give Σa_i=32. Each of the five anchors is evaluated on its own common exterior11-red sample; no anchor deductions are added together. Red attached edges have distinct exterior four-sets because original five-edges are distinct. Exceptional traces are retained with multiplicity; a nonempty exceptional trace containing the red anchor is automatically proper, an absent-anchor trace of sizej has exactly C(13+j,11) blue-bad samples, and an empty trace has1794 mono samples.

Actual result: PASS,351 trace pairs,150315 compositions, zero hard inputs, CPU0.164275 seconds. Constants were independently recomputed by `math.comb`: D31824, R3432, B364, pair intersections120/330/792/1716. The maximum over all profiles of the best anchor bound is31808, margin16.

The limiting profile has traces7 and25 (two triples intersecting at point0), a=(8,6,6,6,6), h=(2,1,1,1,1), and F degrees(11,8,8,8,8). Choosing a noncommon anchor gives6R+26B+4368−2616=31808. The five saved bounds are33336,31808,31808,31808,31808. No eight-set lemma is used.

The bounded necessary trace/composition domain covers every actual q2 input by the exact F traces and edge degree identities. The fact that some abstract profiles may not realize an H does not affect this upper-bound proof, since every profile in the larger domain is strict. Importing the existing q≤1 theorem yields the stated Γ minimum-three consequence. This review and deterministic check are same-family/provisional; no external reviewer was called and no Lean construction was run.

## Additional written threshold proof review

Read the final `Q2_PROOF.md` in full and checked its19 size/intersection rows against the four Venn regions: intersection size r, T1-only size p−r, T2-only size q−r, and outside size5−p−q+r. These produce h=2/1/1/0 and exceptional risks0/e(T2)/e(T1)/(e(T1)+e(T2)), treating an empty trace as constant1794. Each listed sorted threshold row and sum is correct; the minimum forced sum is33>32. The discontinuity in the deduction at a6 does not break monotonicity: f5=26508<f6=27440, while other positive-a increments are2948 and f1−f0=3068. Thus failing all five anchors really implies each of the listed coordinate lower bounds, not merely a disconnected feasible tail.

I agree with the strengthened actual interface in that manuscript: only the five degrees on the selected F need be≥7. No minimum degree condition on its eighteen outside vertices is used anywhere in the six-set lemma, binomial risks, exact equation d(i)=1+a_i+h_i, or the19-row contradiction. The earlier full-composition checker likewise used only these five local bounds despite its more restrictive descriptive scope. The analytic table now supplies a self-contained finite arithmetic proof rather than requiring that checker as a proof premise. No additional computation was run for this reading.
