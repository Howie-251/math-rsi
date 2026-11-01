# M=65: first exact 0–3-lock pilot

**Latest local follow-up:** FOUR_REPORT.md proves the four-unit-lock selection and records all 132 high-vertex profiles passing, closing this pilot's v40…43 arithmetic domain. The historical 0–3-lock failures below remain valid observations about those weaker certificate choices. Root handles the low-vertex branches.

**Sharper three-lock domain:** tighten.py / tightened.json use degree cap10 at v39,40 and cap9 at v41. For v39,40 the independent-triple polynomial is respectively (r−18)²+66 and (r−17)²+211. For v41 with cap9 it is (r−11)²+79, with r≥10. Thus 123 profiles cover this sharper necessary domain; after the saved local placement witnesses 38 remain non-strict. In particular v39 closes entirely. The following 195-profile counts are the complete initial, deliberately wider domain.

This is exploratory arithmetic, not a proof that m(6)≥66. The checked domain is a covering **necessary profile relaxation** under the stated selection argument. A failed profile is not an actual noncolorable hypergraph. Original M64 source files are unchanged.

## Recomputed structural domain

Assume a minimum-vertex counterexample with at most 65 edges. Identifying a noncovered pair preserves 6-uniformity and noncolorability, so every pair is covered. Consequently 5d(x)≥v−1 and ∑d(x)≤390. The function v·ceil((v−1)/5) increases: v=43 gives 387≤390 and v=44 gives 396>390. Thus v≤43. Balanced sampling gives 65p(v)<1 for 11≤v≤26; at v=25,26 its maximum is 780/805. Up to 10 vertices a split into classes of size at most five works. Therefore 27≤v≤43. Since C(v,6)≥65 in this range, pad to exactly 65 distinct edges. All following degree constraints apply to that padded hypergraph.

The possible minimum degree intervals are:

|v|minimum degree d|
|---|---|
|27–31|6–floor(390/v)|
|32–34|7–floor(390/v)|
|35|7–11|
|36|7–10|
|37–39|8–10|
|40–41|8–9|
|42–43|9|

(The zero-lock branch below does not need its degree interval.)

The partition checked is:

- v=27…33: zero locks.
- v=34: one minimum-degree lock d=7…11.
- v=35,36 and d≤9: one minimum-degree lock d=7,8,9.
- v=35,36 and d≥10: two locks with codegree one and degree pairs (v35) (10,10),(10,11),(10,12),(11,11), and (v36) (10,10),(10,11).
- v=37: two codegree-one locks, pairs (8,8),(8,9),(8,10),(9,9),(9,10),(9,11),(10,10).
- v=38…41: three pairwise-codegree-one vertices with each degree between 8 and 11, sorted degrees, both possible triple-incidence patterns. Forty necessary profiles per v.
- v=42,43: three degree-nine pairwise-codegree-one vertices; both triple-incidence patterns.

For the two-lock assertion, let x have minimum degree d and e=5d−(v−1). At least v−1−e vertices y have λxy=1. If every such y had degree at least t+1, the degree sum would be at least

`d+(v−1−e)(t+1)+ed`.

The smallest t making this exceed 390 gives precisely the partner intervals above. This includes the new v35/d11 case: the forced sum at t=11 is 398>390. The script recomputes the t values; it does not reuse M64's old upper degree 13/12.

For v=38…41, let L be vertices of degree at most 11 and r=|L|. Degree sum gives r≥ceil((12v−390)/4), namely 17,20,23,26. In the graph joining pairs in L with codegree≥2,

`2e(G) ≤ (61−v)r+1950−60v`.

Indeed ∑L(5d−(v−1)) bounds 2e(G), and ∑L d≤390−12(v−r). For every integer r in the stated interval through v, exact arithmetic verifies

`r² > 2[(62−v)r+1950−60v]`.

Caro–Wei/Cauchy therefore gives an independent triple in L. The script checks **all r**, not a sample. At v42,43 the degree-nine populations are at least 30 and 40 respectively, because excess over 9v is 12 and 3. The codegree≥2 graph on these vertices has maximum degree at most 45−(v−1), namely 4 and 3. Hence an independent triple exists. This proves the new v43 input domain.

## Exact arithmetic with the original bound

`pilot.py` imports the old functions, sets M=65, and separately rewrites the zero-lock formula to use gamma=65·64−2ceil((975−C(v,2))/10). Other formulas and old full-pool link deletion are unchanged. Baseline positions retain the old centered placement. Every comparison uses Fraction.

195 profiles were checked completely in 0.314 CPU seconds. 98 pass and 97 fail.

|Class|profiles|failures|
|---|---:|---:|
|v27…31 zero|5|0|
|v32,33 zero|2|2|
|v34 one|5|3|
|v35,36 one|6|6|
|v35,36 two|6|0|
|v37 two|7|4|
|v38 three|40|0|
|v39 three|40|4|
|v40 three|40|34|
|v41 three|40|40|
|v42,43 three|4|4|

All exact values and type parameters are in `baseline.json`. The zero-lock failures are 4512833/4466232 at v32 and 4529447/4466232 at v33. The old-formula worst is 11749597/11481470 at v43, tri=0 (about 1.023353). The high-minimum-degree v35/36 two-lock cases all pass; the worst is about 0.99993698.

## Placement and degree-order search

`positions.py` evaluates all single-lock positions for the failing one-lock profiles. For failing two/three-lock profiles it evaluates all distinct degree orders and all sorted positions in the seven slots floor(v/2)−3 through floor(v/2)+3. This is **complete for that local placement menu only**, not an all-position exclusion. Zero-lock failures are untouched. The run completed 9,492 exact evaluations in 17.750 CPU seconds, well below the initial 120 CPU-second limit.

Five necessary profiles acquire strict certificates:

|v|degrees|tri|ordered degrees at positions|positions|U|
|---|---|---|---|---|---|
|39|8,11,11|1|11,11,8|18,19,20|24844951/24920280|
|39|9,11,11|1|11,11,9|18,19,20|1777387/1780020|
|40|8,8,10|1|8,10,8|19,20,21|1380429227/1383075540|
|40|8,9,10|1|9,10,8|19,20,21|115245832/115256295|
|41|9,9,9|1|9,9,9|20,21,22|48658198/48663769|

Thus 90 nonzero-lock profiles remain non-strict under the searched menu, plus the two untouched zero-lock cases: 92 unresolved relaxed profiles overall. No failing one-lock profile is rescued even after checking every position. The partner and triple choices above prove coverage of the relaxed domain, but these arithmetic failures mean the full M65 theorem does not follow from this pilot.

## Reproduction

From project root:

```
python3 context/propertyb-m6-66-20261029/pilot/pilot.py
python3 context/propertyb-m6-66-20261029/pilot/positions.py
```

Outputs: `baseline.json`, `positions.json`. The original certificate file is a required local dependency; no source is modified. No Lean, v2, wiki, main manuscript, or AGENTS changes were made.
