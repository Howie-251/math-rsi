# Independent mathematical-domain and exact-arithmetic review: m(9) ≥ 543

## Verdict and scope

**PASS_WITH_DECLARED_IMPORTS.** I found no gap in the original-input reduction, actual lock selection, complete necessary local domains, or final assembly in `../PROOF_M9_GE543.md`. A new standalone implementation reconstructed the complete decision tree and independently recomputed all 3450 accepted leaves. Every rational value equals the submitted value exactly and is strictly below one.

This is a fresh review of the nine-uniform candidate by an executor who did not author it. The executor previously worked on the separate six-uniform result. The mathematical judgment is **same-family / provisional**. The exact arithmetic and coverage tests actually ran locally; this is not a second-machine reproduction, Lean proof, or cross-family model review.

The original statement remains unchanged: every finite simple nine-uniform hypergraph with at most 542 edges has Property B, hence m(9) ≥ 543. This review adds no degree, vertex-count, pair-cover, regularity or prescribed-coloring hypothesis to that statement.

## Sources and coverage receipt

Read directly:

- `../PROOF_M9_GE543.md`, all seven sections;
- `../CANDIDATE.json`, `../SUMMARY.json`, `../profile.py`, `../candidate.py`, `../coverage.py`, `../repair.py`;
- `../../../propertyB_small_k/propertyB_k8_k9_proof.md`, especially §§1–4;
- `../../../propertyB_small_k/propertyB_m9_certificate_v2.py`, the original generic probability implementation;
- the previously reviewed six-uniform independent injection-count method, used only as an implementation starting point.

`check.py` imports **no author numerical, selection, profile, repair, coverage or six-uniform module**. Its runtime imports are Python standard-library modules. The only submitted numerical input it reads is `CANDIDATE.json`; routing and all probabilities are reconstructed rather than imported.

|Source unit|Reviewed obligations|Result|
|---|---|---|
|U01, §1|Original quantifiers, simple finite nine-uniform objects, M=542 and total degree 4878|Aligned|
|U02, §2|Actual vertex identification, padding, balanced coloring, both necessary vertex endpoints|Complete|
|U03, §3|Actual greedy witness, conditional injections, nonnegative pair accounting, eight-set link quota and maximum deduction|Valid in the stated interpretation|
|U04, §4|Minimum-degree unit partner, conditional common unit partner, Caro–Wei low-degree triple, both trace patterns|Hypotheses discharged in all reached branches|
|U05, §5|Complete routing, original minimum-degree intervals, all partner/third-degree intervals, exact leaf-key equality|Independently reconstructed|
|U06, §6|Every original counterexample reaches a strict sufficient bound; coloring returns to original edges|Complete|
|U07, §7|Reproduction and author/independent distinction|Accurate as a description of the pre-review state|

All seven source units were covered. The table records actual source coverage, not a claim of formal proof-kernel certification.

## 1. Original-input reduction

The minimum-vertex counterexample argument is valid. If two vertices never occur in one edge, their identification preserves nine distinct vertices in every image edge; duplicate images may be removed. A coloring of the image pulls back to every original edge, so the image remains a counterexample with fewer vertices. Thus pair coverage follows internally.

Pair coverage gives 8d(x) ≥ v−1, hence v ceil((v−1)/8) ≤ 9M=4878. The left side is nondecreasing. At 195 it is 4875 and at 196 it is 4900, establishing the upper endpoint 195. The new endpoint is not inherited from the older M=541 calculation.

For v≤16, two classes of size at most eight immediately suffice. `check.py` independently evaluates all forty balanced-coloring values for 17≤v≤56 and obtains maximum 6233/6307<1. It also rebuilds the complete set satisfying the pair-cover degree budget and failing this sufficient balanced bound; this set is exactly 57,…,195. Every v in that set satisfies C(v,9)≥542, so adding distinct edges to reach exactly 542 is possible. Pair coverage and non-colorability persist. Subsequent degrees and traces consistently refer to that same padded actual hypergraph.

## 2. Actual lock selection

Let d be the actual minimum degree. Its full interval is rebuilt independently as ceil((v−1)/8)≤d≤floor(4878/v).

For a degree-d point x, the exact row excess is 8d−(v−1). At most this many other vertices can have codegree at least two with x. Therefore the actual unit pool A has size r≥n=2(v−1)−8d. Whenever the proof reaches this selection, the independently generated n is positive.

Choose a minimum-degree member y of A, of degree e. Since every member of A has degree at least e and all other vertices at least d, 4878≥vd+r(e−d)≥vd+n(e−d). Instead of copying the author's floor expression, `check.py` enumerates every integer e satisfying this degree inequality. The resulting intervals and all leaf keys agree exactly.

For a needed third point, A\{y} loses at most 8e−(v−1) vertices that have nonunit codegree with y. Thus its actual common unit pool has size at least t=n−1−(8e−v+1). Since y was a minimum-degree member of A, all common-pool degrees are at least e. Choosing its minimum-degree member z, of degree f, gives 4878≥vd+n(e−d)+t(f−e). Both terms added to vd are nonnegative; no overlapping degree contribution is counted twice because the second increment is only the additional f−e on the common subpool.

The checker independently enumerates every f satisfying this inequality. All 73 reached conditional parents have positive t, with minimum 115; their largest f upper endpoint is 28. There is no unfilled common-pool branch.

At 183≤v≤195 the proof uses L={d≤28}. With r=|L|, the outside degree baseline 29 gives Z=29v−4878>0 and r+2e(G)≤(234−v)r−8Z. The actual upper denominator is positive because it is at least r+2e(G)≥r>0. Caro–Wei followed by Cauchy–Schwarz and the displayed square identity forces independence number greater than two when 16Z−(234−v)²>0. All thirteen vertex values were recomputed; minimum gap is 4263 at v=183. The checker additionally checks the resulting strict quadratic for every integer r from ceil(Z/(29−ceil((v−1)/8))) through v. Thus the selected three locks have actual degree at most 28 and unit pairwise codegree.

## 3. Complete actual trace domains

One lock has its degree-many incident edges and the remaining empty traces. Two unit locks have exactly one shared edge; singleton and empty traces are then determined by the two actual degrees and M=542.

Three unit locks have exactly the two stated possibilities: one edge uses all three pair capacities, or three distinct edges use one pair capacity each. No other multiple-lock trace is possible. Both are included for every degree triple. The checker constructs multiplicities itself, then verifies every supplied row against them, including nonnegativity, sum 542, actual degree marginals, all unit pair marginals, triple-intersection flag and actual distinct positions.

Some necessary local inputs may not be globally realizable; retaining them only strengthens coverage. The final submitted 3450 rows all have nonnegative multiplicities. The proof does not require or infer realization of arbitrary relaxed local parameters.

## 4. Independent probability counting

The original generic conditional-permutation framework was read and its greedy witness argument rechecked: a final all-blue edge B has a first point z; when z was changed blue, some then-all-red edge A ended at z. All other points of A lie before z, and all other points of B lie after z, so A∩B={z}. Final all-red edges are impossible by the same processing rule.

The independent code counts **uniform injections of labelled free vertices**, rather than calling the author's binomial functions. Write (n)_a for the falling factorial. For a free pivot, a fixed pair with r and s free vertices has probability

    (left)_(r−1) (right)_(s−1) / (N)_(r+s−1),

subject to the exact preceding/succeeding lock masks. For a locked pivot it is

    (left)_r (right)_s / (N)_(r+s).

The independent one-edge endpoint probabilities are r(left)_(r−1)/(N)_r at a free pivot, and (left)_r/(N)_r at the appropriate locked pivot; start probabilities use right. Their mask and capacity conditions are explicitly checked in the code. These are algebraically equivalent to the author's binomial probabilities but are separately implemented from the named-vertex injection interpretation.

The pair accounting coefficient is independently formed as ℓ_T(ℓ_U−1[T=U]). Assigning the nonnegative single-intersection weight to non-single pairs is only an overestimate. Eight-element link sets are distinct because original edges are simple, and two different such sets intersect in at most seven points. The count 8f≤N+7Q therefore gives the quota ceil((8f−N)/7), truncated at zero for subfamilies that need not cover their support.

At every locked pivot, the checker independently forms unordered-cell capacities and exact bidirectional weights. It computes the least weight of each individual quota by filling cells in increasing weight order. For the max_R mode it takes their maximum, never their sum; all those bounds constrain the same actual bad-pair cost. The full-pool mode restricts to R empty. This preserves the supplied deduction method for each replayed row.

For zero locks the checker independently obtains Q≥ceil((542 C(9,2)−C(v,2))/C(8,2)), truncated at zero. This is the point-pair surplus bound; simple nine-edges have intersection at most eight, so an unordered multi-intersection edge pair contributes at most C(8,2). The ordered-single-pair upper bound 542·541−2Q is therefore valid. Its probability is counted by the same injection interpretation.

## 5. Independent tree generation and full replay

The checker does not decide branches by testing whether a saved leaf happens to exist. For 135–154 it recomputes every one-lock sufficient inequality at the specified central position. If not strict, it generates the complete actual unit-partner interval and recomputes the two-lock inequality. For 155–182 it recomputes the original full-pool two-lock stopping bound. Every necessary unresolved two-lock input is continued using the independently enumerated third-degree inequality and both actual traces. For 183–195 it enumerates every nondecreasing low-degree triple and both traces.

This entails 319 independently recomputed one-lock routing tests and 1702 two-lock routing tests. The independently reconstructed complete leaf-key set equals the submitted key set, with no missing leaf, extra leaf or duplicate. The checker then replays the supplied successful layout of every leaf and obtains exact equality in all 3450 cases.

|Leaf group|Complete leaves|Largest independent exact bound|
|---|---:|---:|
|Zero locks|78|106487496857099087577/106600839931609480600|
|One lock|287|1972282554392680909022596/1972426008426513683838795|
|Two unit locks|1629|394476918471453327981799/394489458501784689243720|
|Conditional three unit locks|480|896688388734878356588012/904701259945736563545105|
|Three low-degree unit locks|976|41317885902922681304309/41563621287040215236328|
|Total|3450|Every row is strictly below one|

The 181/182 two-lock inputs all continue to actual conditional triples; their absence from the successful-two-leaf vertex span is not a missing branch. The high vertex endpoint 195 occurs in the final triple domain.

## 6. Reproduction, measured cost and declared limits

From the project root:

```sh
python3 context/propertyb-m9-543-20261029/independent/check.py
```

A stratified 25-leaf profile first passed in 0.213 CPU seconds. The final complete run used 30.090 CPU seconds: 8.450 for original-domain/tree reconstruction and 21.640 for all leaf replays and result assembly. `CHECK.json` records all balanced values, actual vertex domain, 73 conditional parents, thirteen low-degree selection checks, every replayed exact value and measured CPU usage. Its status is `PASS_WITH_DECLARED_IMPORTS`.

Declared limits:

- The conditional greedy mechanism and ordinary uniform-permutation interpretation are shared mathematical imports, read and rechecked above. Reusing that theorem does not make this an independent proof framework from first principles.
- The probability arithmetic is a new implementation derived from the previously reviewed six-uniform injection method. It imports none of that executable code and uses k=9, link size eight and maximum link intersection seven throughout. It is independent of this nine-uniform author's numerical implementation, not an unrelated software stack.
- Caro–Wei, Cauchy–Schwarz and ordinary exact Python integer/Fraction semantics are trusted here; there is no Lean or other formal-kernel check.
- Older eight-/nine-uniform certificates and bibliographic metadata of the comparison value 538 were not independently rerun or citation-audited. They are not numerical premises needed to prove this new m(9)≥543 bound.
- No external-model review, second-machine reproduction or world-record claim is supplied by this executor. Root is handling final mathematical review and any cross-family consultation separately.

Every original actual counterexample is connected to one of the exact strict leaves through the reviewed internal reduction and actual choices. Within the stated imports and software trust, the new proof closes its original all-hypergraph statement. ∎
