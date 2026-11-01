# Independent common-x-star reduction and47 fixed certificates

All47 supplied six-lock inputs are strict with zero quota. The maximum is **428/429<1**. Every certificate has an independent original35-index /1190 ordered distinct pair replay, agreeing in all21 individual minimum rows and the final exact Fraction. The recorded run used0.135621 CPU seconds. No position DP, new H domain, quotas or permutations were used.

## 1. Actual common-star arithmetic

The intended input is the parent's actual A2/A3 necessary setting:21 vertices,35 simple five-edges, paircover, unique degree6 point x, respectively two or three degree7 points, and the already-proved six-unit-degree8-pool exclusion. Write b for the total number of degree8 points and e for total degree excess above9. The complete role relation is b=11−2a+e, where a is the degree7 count. Since every vertex distinct from x has λ(x,v)≥1 and the six actual x-edges have24 neighbor incidences,

`Σ_{v≠x}(λ(x,v)−1)=24−20=4`.

At most five degree8 vertices can be unit with x, so at least b−5 degree8 vertices must consume this row excess. In particular b≤9. This rules out A2 whenever e≥3.

For each of the four remaining five-lock inventories, all five F-point degrees exceed6, so x lies outside F. There is no empty F-trace. Hence all six actual x-edges meet F; the original edge F itself cannot contain x. Let a selected multi-trace T denote an exceptional original edge containing x. If the x-star contains only singleton F-traces, its six incidences cover all five F points, so the count vector is exactly `(1,1,1,1,1)+e_v`. If it contains a size3 trace, the other five edges are singleton traces and F-row excess is3. If it contains a size4 trace, F-row excess is4. Two multi-traces would give F-row excess at least5, impossible. These statements use the same actual x-star, not independent choices of λ at its five points.

The parent's four residuals have these degree data:

|Source|F degrees|Total e|A3 b|F degree8 positions|
|---|---|---:|---:|---|
|A|(9,10,10,9,7)|2|7|none|
|B|(7,10,10,10,9)|3|8|none|
|C|(8,10,10,9,9)|2|7|0|
|D|(13,8,8,9,9)|4|9|1,2|

A in A2 has b9 and all four necessarily nonunit degree8 points outside F. They exhaust all four row-excess units, while six x-edges meeting five F points require F-excess≥1. Thus A2-A is impossible. For A3-A, at least two required nonunit degree8 points are outside F, leaving F-excess≤2 and excluding every multi-trace; five singleton-double choices cover it.

B is necessarily A3 since e3 would give A2 b10. Its at least three nonunit degree8 points are outside F, leaving F-excess≤1. Only the five singleton-double choices remain.

C in A3 allows all five singleton-double choices. A size3 chosen exception consumes F-excess3, leaving one excess outside F. At least two degree8 points must be nonunit, so the only F-degree8 point v0 must also be nonunit: λ(x,v0)≥2. The two size3 traces are7 and25; both contain v0. In either case the two points outside T require singleton counts≥1, v0 requires another singleton count≥1, and the other two counts are nonnegative. There are five singleton selections in total: three forced units plus two arbitrary units, hence C(6,4)=15 choices for each T. The size4 exception consumes F-excess4 and would leave no outside excess, while F contains only one degree8 point, so it cannot supply the two required nonunit degree8 points. C therefore contributes5+15+15=35 inputs. **C can also occur in A2**: then b9, and its four nonunit degree8 points exhaust all excess. The singleton doubled point must be v0; this one key is already among the five singleton keys above. Its triple choices are impossible. Thus the35-key domain covers both roles without asserting C is only A3.

D is necessarily A3. Its b9 forces exactly four nonunit degree8 points, each using one excess; every other point has unit λ with x. No multi-trace is possible because F has only two degree8 points and therefore F-excess≤2. In its singleton-only star, the doubled point must be one of the two F-degree8 points, giving two inputs.

The resulting common-star domain is5+5+35+2=47. Extra necessary restrictions can only shrink it.

## 2. Independent finite-domain generation

`SIX_LOCK_COMMON_STAR47.py` constructs these47 keys in two ways. The first uses the preceding direct singleton/triple count formulas. The second enumerates the eight subsets of the three actual exceptional edges and all weak singleton compositions of the remaining x-edge count, then imposes the derived membership, capacity, unit coverage and row-excess restrictions. Their key sets agree separately for A/B/C/D. This is a small trace-choice/count domain, not an enumeration of H or outside set placements.

For an original five-lock trace mask m, the six-lock mask is2m when the actual edge avoids x and2m+1 when it contains x. Bit0 represents x; bits1…5 represent F. Chosen counts are subtracted from the same original multiplicity and added exactly once at its x-containing mask. All35 original indices are thereby preserved; selected degrees equal the old five degrees together with x-degree6. There is no full six-lock trace, empty trace or x-only trace.

## 3. Fixed menus and strict certificates

For each source, retain its previously recorded best five-lock profile. Add x only at one of the fixed slots1,9,10,11,20,21 that is not already occupied. The five-lock point labels are unchanged. The production injection evaluation has every pair quota set to zero. No paircover deduction is used in the probability arithmetic; paircover enters only the actual common-star coverage above.

All47 cases pass. The largest428/429 occurs for source B singleton-only stars with the doubled F point1,2 or4. One common successful maximum profile has x/F positions `(20,11,3,2,12,1)`.

Each selected profile is independently checked using35 expanded original edge indices,1190 ordered distinct edge-index pairs, and falling-factorial injection probabilities. The zeta/count production result and expanded independent result agree for every one of21 row minima. The exact A/B/C rows, trace counts, selected original indices, chosen star counts, menus and final rational bounds are all in `SIX_LOCK_COMMON_STAR47.json`.

Reproduction: `python3 SIX_LOCK_COMMON_STAR47.py`.

This establishes the finite actual trace-certificate obligation conditional on the specified role and six-unit8-pool imports. Final assembly with the earlier91-orbit threshold classification and79 five-lock certificates remains with the parent. It is not a statement about arbitrary q3 hypergraphs or the complete36 target. Same-family review status is provisional; the supplied complete finite domains and exact independent arithmetic are the substantive evidence.
