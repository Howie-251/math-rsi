# T34 low-vertex feasibility: actual formula diagnostics

2026-10-13. This is a bounded feasibility investigation, not a new Goal or Lean result. Existing proof source and old scripts are untouched. All calculations are exact rational arithmetic, and every retained witness has its A/B/C rows checked against the independent labelled-injection implementation. No hypergraphs were enumerated.

## Outcome

19 vertices now have a complete paper-level candidate using existing probability/link lemmas plus the explicit selection argument below. 20 vertices have 8 successful and 6 failed unit-double profiles under the specified nested pure/total quota; failed rows were tested at all 190 increasing placements. This does not refute T34 or stronger deductions.

## Formulas and the scope of the quotas

Let H be simple, 5-uniform, pair-covering, with M=34. The type counts in each row are the exact counts of edges by intersection with the chosen lock set. The probability engine uses the already proved endpoint/pair counting formulas. At each lock, q_total=ceil((4d-(v-1))/3). If there are p singleton-type edges and s locks, q_pure=max(0,ceil((4p-(v-s))/3)). Both count unordered bad pairs. The pure quota is nested inside the total quota: allocate pure pairs first, then only the remaining total demand, using the true capacities and two-direction weights. The quotas are not added as independent deductions.

For a smallest-degree point d and unit-neighbor set W, |W|≥2(v-1)-4d and sum_{y in W}(d(y)-d)≤5M-vd. Thus at least one unit partner has degree at most d+floor((5M-vd)/(2(v-1)-4d)). This guarantees a selected partner, not a bound on every partner.

## 19 vertices: a complete candidate decomposition

Pair covering and total degree 170 imply 5≤δ≤8. If δ=5,6,7, lock that point at position 10. The exact bounds are respectively 23003/24310, 896/935, and 23589/24310, all strictly below 1.

It remains δ=8. Let r be the number of degree-8 vertices. If r≤2, every other vertex has degree at least 9. The baseline total is 8r+9(19-r)=171-r, leaving r-1 extra incidences. Hence every high vertex has degree at most 8+r≤10. A degree-8 point has at least 36-32=4 unit neighbors, at most r-1≤1 of which have degree 8. Choose a high unit neighbor of degree 9 or 10. The already checked unit-double rows have bounds 95881/97240 and 94049/97240 at (7,8).

If r≥3 and two degree-8 vertices have codegree λ≥3, the λ=3,...,8 double-lock rows below all pass at the fixed positions (1,11). If there is no such pair, choose any three degree-8 vertices. Their pair codegrees all belong to {1,2}. Relabeling the three vertices sorts the three pair codegrees, since the action of vertex permutations induces all permutations of the three pairs. The only sorted triples are (1,1,1),(1,1,2),(1,2,2),(2,2,2). The triple-edge multiplicity t lies between 0 and the minimum pair codegree. This gives exactly 9 local types, all checked below.

For ordered pair codegrees (a,b,c)=(λ12,λ13,λ23), the counts are l123=t, l12=a-t, l13=b-t, l23=c-t, l1=8-a-b+t, l2=8-a-c+t, l3=8-b-c+t, l_empty=10+a+b+c-t. These recover 34 edges and three degrees 8, and classify every actual input of this branch; they do not assert that every listed type is realizable.

|19-point local profile|Chosen positions|Exact bound|
|---|---|---|
|v19_unit_triple_t0|[7, 8, 9]|36607/40040|
|v19_unit_triple_t1|[7, 8, 9]|36409/40040|
|v19_triple_(1, 1, 2)_t0|[8, 9, 10]|11311/11440|
|v19_triple_(1, 1, 2)_t1|[7, 8, 9]|1793/1820|
|v19_triple_(1, 2, 2)_t0|[9, 10, 11]|12667/12870|
|v19_triple_(1, 2, 2)_t1|[9, 10, 11]|1389/1430|
|v19_triple_(2, 2, 2)_t0|[9, 10, 11]|707/715|
|v19_triple_(2, 2, 2)_t1|[9, 10, 11]|482/495|
|v19_triple_(2, 2, 2)_t2|[9, 10, 11]|136/143|
|v19_8_8_lambda3|[1, 11]|6989/7293|
|v19_8_8_lambda4|[1, 11]|32858/36465|
|v19_8_8_lambda5|[1, 11]|92383/109395|
|v19_8_8_lambda6|[1, 11]|2614/3315|
|v19_8_8_lambda7|[1, 11]|26737/36465|
|v19_8_8_lambda8|[1, 11]|1142/1683|

All 9 triple rows were tested in five contiguous windows starting at 7,...,11; only a successful witness is needed. The λ≥3 rows were independently checked directly at (1,11). The candidate still needs full mathematical review, a Lean actual-input assembly, and the original coloring conclusion; no new formal theorem is claimed here.

## 20 vertices: complete selected unit-pair domain

The partner guarantee above yields degree rows (5,5..8), (6,6..9), (7,7..10), (8,8..9), exactly 14 profiles. Their empty type has size 35-dx-dy, singleton types dx-1 and dy-1, and the double type has size 1.

|Degrees|Positions attaining reported value|Exact bound|Strict <1|Position scope|
|---|---|---|---|---|
|[5, 5]|[10, 11]|4457/4862|yes|five_contiguous_central_windows|
|[5, 6]|[10, 11]|22557/24310|yes|five_contiguous_central_windows|
|[5, 7]|[10, 11]|23081/24310|yes|five_contiguous_central_windows|
|[5, 8]|[10, 11]|4721/4862|yes|five_contiguous_central_windows|
|[6, 6]|[10, 11]|22829/24310|yes|five_contiguous_central_windows|
|[6, 7]|[10, 11]|2123/2210|yes|five_contiguous_central_windows|
|[6, 8]|[10, 11]|23877/24310|yes|five_contiguous_central_windows|
|[6, 9]|[11, 12]|2474/2431|no|all_increasing_positions|
|[7, 7]|[10, 11]|23877/24310|yes|five_contiguous_central_windows|
|[7, 8]|[10, 11]|1877/1870|no|all_increasing_positions|
|[7, 9]|[11, 12]|453707/437580|no|all_increasing_positions|
|[7, 10]|[11, 12]|736/715|no|all_increasing_positions|
|[8, 8]|[10, 11]|4985/4862|no|all_increasing_positions|
|[8, 9]|[1, 2]|609721/583440|no|all_increasing_positions|

For passing rows the search was limited to five contiguous central windows (start 8,...,12). For each failing row all 190 increasing placements were checked. Reversing the permutation covers the opposite order of the two locks, because the bound and the two nested quotas are invariant under left/right reversal. Thus no placement alone repairs those six profiles for this specific bound. This statement does not cover stronger valid information or other lock sets.

The six residual rows are (6,9), (7,8), (7,9), (7,10), (8,8), (8,9). The closest failure is (7,8): 1877/1870, a deficit of 7/1870. The (8,9) residual is broadest here, 609721/583440. Prioritize a third lock or stronger actual bad-pair correlations for these rows; simply scanning more two-lock placements has no remaining benefit under this bound. A structural selection lemma avoiding selected residual rows could also help, but none is supplied here.

## M=33 controls and independent checks

RESULTS.json contains all retained M=33 and M=34 single/double rows for v=19,20, including actual per-position A/B/C, deductions, active terms, and quota counts. Every M=33 v=20 required unit-double row is strictly below 1, recovering the old branch. Some are stronger than the historical total-quota table because this diagnostic applies the valid pure quota uniformly, not only to (8,8). These controls verify numerical continuity, not the full structural proof.

## Requested 21-point supplementary profiles

The parent supplied candidate obligations (9,9), λ=5..9 and (9,10), λ=8..9. They all pass at (10,12), but structural selection of those pairs is outside this subtask.

|Profile|Positions|Exact bound|
|---|---|---|
|v21_9_9_lambda5|[10, 12]|42945/46189|
|v21_9_9_lambda6|[10, 12]|1078/1235|
|v21_9_9_lambda7|[10, 12]|17143/20995|
|v21_9_9_lambda8|[10, 12]|175686/230945|
|v21_9_9_lambda9|[10, 12]|1715/2431|
|v21_9_10_lambda8|[10, 12]|16177/20995|
|v21_9_10_lambda9|[10, 12]|330351/461890|

## Reproduction

Run `python3 context/propertyb34-feasibility-20261013/low-vertices/diagnose.py` and `python3 context/propertyb34-feasibility-20261013/low-vertices/extra_diagnostics.py` from the project root. The first completed in about 2.05 seconds on this host; the second in under one second. These are tiny formula diagnostics, not a prediction of future Lean or complete-proof runtime.

Source engines: `computations/multilock.py`, `computations/propertyb33/round01/pure_quota.py`, and `computations/independent_structure_bounds.py`. Evidence: `RESULTS.json`, `EXTRA_RESULTS.json`. Existing T32/T33 artifacts remain unchanged.

## Final requested 21-point checks

The old unit-codegree (5,8,8), triple multiplicity 0 profile and the newly selected unit doubles were also checked at M=34. These extra rows use the same exact nested pure/total quota and passed independent A/B/C comparison. None of the tested layouts achieves a strict bound.

|Degrees / intersections|Best tested positions, assigned in degree order|Bound|Actual search scope|
|---|---|---|---|
|(5,8,8), pair codegrees (1,1,1), triple multiplicity 0|(11,9,10)|44215/43758|Six contiguous windows starting 7,...,12; all three locations of the degree-5 lock within each window; the degree-8 locks are interchangeable|
|(6,8), unit pair|(11,12)|336/323|Five adjacent windows starting 8,...,12 and four gap-2 layouts starting 8,...,11|
|(7,8), unit pair|(11,12)|8883/8398|Same nine double layouts|
|(8,8), unit pair|(8,9)|444472/415701|Same nine double layouts|

The triple counts in mask order are l_empty=16, l_1=3, l_2=l_3=6, l_12=l_13=l_23=1, l_123=0. These recover all 34 edges and degrees 5,8,8. A bound above 1 only means these tested layouts with this quota are insufficient. This is not an exhaustive placement result and does not refute the local coloring claim. In particular, success of the high-codegree (9,9)/(9,10) subbranches does not by itself close the proposed 21-point degree-5 decomposition: its old (5,8,8) unit subbranch still needs a stronger bound or a different layout/structure.
