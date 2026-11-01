# Independent complete P-side verification for at least three high traces

The twelve necessary domains contain **159318 inputs**; every input has an accepted repair witness. The independent generator used3.256761 CPU seconds. Of the witnesses,159297 use two blue P points and21 use three. This implementation was rebuilt from the mathematical input and does not read or import the discovery implementation. Comparison of saved JSON was performed only after generation.

## Mathematical input and complete domain

Let H be a simple five-uniform hypergraph on24 points with35 edges, pair coverage and minimum degree seven. Suppose there is no all-seven-degree edge and exactly seven points have degree above seven. Their total degree is56, so these seven points P all have degree eight; the remaining seventeen points L all have degree seven. Every edge meets P.

There are exactly three edges contained in P. Their omitted pairs form one of

F={01,12,34} or F={01,23,45}.

Their common intersection C is respectively {5,6} or {6}; put D=P\C. The present domain assumes that all higher noninternal P traces lie in D and that there are at least three such traces. They are indexed three- or four-sets, so repeated trace sets are allowed. Let n3,n4 count them, r=n3+n4, and let n2,n1 count noninternal pair and singleton traces. Summing P degrees and subtracting the three internal edges gives

n2+2n3+3n4=9, n1=23+n3+2n4.

Thus r≤4. For r=4, n4 is0 or1; for r=3, n4 is0,1,2 or3. These are exactly six budgets for each shape, twelve altogether.

Let ci=3−degF(i), hi be higher-trace indexed occurrence, wi=Σ_{T∋i}(|T|−1), and si be degree in the pair-trace multigraph J. The private singleton count is

ui=8−ci−hi−si≥0.

The number of incidences with L among the eight edges through i is

4ui+3si+Σ_{T∋i}(5−|T|)=32−4ci−si−wi.

Pair coverage of i with all17 points of L forces this to be at least17. Hence every actual input satisfies

si≤min(8−ci−hi,15−4ci−wi).

Every P pair not covered by an internal edge or a higher trace must also occur as an edge of J. The independent run tests **every** J satisfying these conditions, with exactly n2 edges counted with multiplicity. It does not apply any extra undisclosed realization filter. It does not claim to verify the larger domain obtained by dropping the PL incidence bound.

For each shape, `VERIFY.py` generates all5040 permutations and retains those preserving F, giving actual automorphism orders8 and48. It lists every unordered repeat-allowed collection of n3 three-traces and n4 four-traces inside D, and takes the minimum mask tuple under this one shared action. For every such representative it separately lists all labelled J edge multisets of size n2 among21 pairs. The singleton counts are forced by ui. Thus no independent reorientation of different higher traces is used, and no quotient is applied to J. Transport by the chosen P permutation preserves all constraints and carries the resulting coloring back to the original labels.

## Exact coverage

|F|r|n4|n2|Higher-trace orbits|Necessary inputs|Uncovered|
|---|---:|---:|---:|---:|---:|---:|
|P3+K2|4|0|1|221|1532|0|
|P3+K2|4|1|0|326|105|0|
|P3+K2|3|0|3|74|54779|0|
|P3+K2|3|1|2|90|7820|0|
|P3+K2|3|2|1|53|63|0|
|P3+K2|3|3|0|16|0|0|
|3K2|4|0|1|261|3171|0|
|3K2|4|1|0|584|298|0|
|3K2|3|0|3|54|78514|0|
|3K2|3|1|2|99|12844|0|
|3K2|3|2|1|75|189|0|
|3K2|3|3|0|32|3|0|
|Total|||||159318|0|

Empty high-trace domains and zero-input orbits are generated and recorded; they are not silently skipped. `SUMMARY.json` records every orbit, including zero-input ones.

## Direct classification of all35 actual edge indices

For each input, try all21 two-point blue subsets of P, followed by all35 three-point subsets. All other P points are red. The program reconstructs exactly35 P traces: the three internal traces, indexed higher traces, J pair traces and ui indexed singleton traces. For each trace S and chosen blue set B:

- if S meets both colors, the original edge is already proper;
- if S⊆B, the exterior set is a positive set of size5−|S|;
- if S∩B is empty, the exterior set is a negative set of size5−|S|.

The implementation explicitly retains the size before deciding whether a repair gate applies. In particular, a blue higher triple produces a positive pair; an unhit higher triple produces a negative pair; an unhit higher four-trace produces a negative singleton; an all-red internal edge produces an empty negative set. Such risks are never deleted. A candidate with a constraint size outside its chosen gate is rejected. Positive pairs are allowed only by an applicable small-positive gate with its precise bound of at most three positive pairs. All accepted witnesses in this run happen to have zero positive pairs; this is an output check, not a premise imposed on candidate recovery.

Each witness file row contains

`[higher masks, J edge ids, blue P points, gate, [P2,P3,P4,N3,N4], all35 source-index categories]`.

Here the35 categories retain the trace index order: three internal edges in F order, higher traces in mask order, J in pair-id order, and singleton traces by their P point. `.` marks an already proper edge. Thus the category counts do not merely come from an aggregate formula.

## Gates actually used

|Independent gate label|Inputs|Exact existing repair theorem|
|---|---:|---|
|SMALL4_T3|5003|FOUR_SMALL_POSITIVE_THREE_TRIPLE_REPAIR.md: ≤4 positives of size≥2, ≤3 negative triples, D7|
|SMALL5_T2|26397|FIVE_SMALL_POSITIVE_TWO_TRIPLES_REPAIR.md: ≤5 positives of sizes2..4, ≤3 positive pairs, ≤2 negative triples, D7|
|PURE7_T4_B35|95981|SEVEN_POSITIVE_FOUR_TRIPLES_REPAIR.md,35-negative-four extension|
|PURE8_T3_B20|24879|EIGHT_POSITIVE_FOUR_SET_REPAIR.md,20-negative-four extension, L17|
|PURE8_T0_B27|3|FIVE_POSITIVE_SIGNED_REPAIR.md §3, ≤8 positive fours, zero negative triples, ≤27 negative fours|
|MIXED7_TWO3_T1_ANYB|7019|SEVEN_MIXED_TWO_SMALL_ONE_TRIPLE_REPAIR.md, main theorem|
|MIXED7_FOUR3_T0_ANYB|15|Same file, zero-negative-triple extension with ≤4 positive triples|
|ELEVEN_P4_T0_B17|21|ELEVEN_POSITIVE_FOUR_SET_REPAIR.md, ground≤18|

All these gates count indexed occurrences. Since every original edge meets P, each unfinished original edge contributes precisely one signed constraint and each already proper edge contributes none. Each point of L therefore has total constraint occurrence at most its actual degree seven. The ground has17 points, meeting every used ground bound. No positive set is duplicated to pad a gate.

The21 three-blue witnesses lie in the 3K2 budget r4,n4=0, for the single Pasch higher-trace orbit. Each has11 positive fours, no negative triples and16 negative fours, so the eleven-positive gate applies. All other necessary inputs accept a two-blue choice.

The repair theorem returns R⊆L meeting all positive exterior sets and containing no negative exterior set. Color R red and L\R blue, retaining the selected P coloring. An all-blue P trace now has a red exterior point; an all-red P trace has a blue exterior point; mixed P traces were already proper. Thus **every one of the35 actual original edges is proper**. Applying the inverse P relabeling gives the original H coloring.

## Independent comparison and scope

After independent generation, `COMPARE_JSON.py` reads only this directory's JSON and the discovery JSON under `../higher_at_least_three_remaining_20261020/with_three_blue/`. Besides all twelve counts and every nonzero orbit count, it actually compares the complete saved key sets `(canonical higher-trace multiset, fully labelled J multiset)` for each budget. All159318 keys coincide, and no duplicate input key occurs. This is stronger than inferring equality from matching totals. Blue selections and gate priorities need not coincide and are not required to coincide.

Reproduction:

```sh
python3 -B context/propertyb35-paper/round01/twentyfour/three_internal/higher_at_least_three_independent_20261020/VERIFY.py
python3 -B context/propertyb35-paper/round01/twentyfour/three_internal/higher_at_least_three_independent_20261020/COMPARE_JSON.py
```

This is an independent deterministic local-domain implementation and complete actual-input connection, not a whole-H enumeration or a new cross-family review. It covers only these two missing shapes, r≥3 and higher traces avoiding C. The parent maintains the surrounding branch wrapper and designated external review. No canonical theorem, navigation, Lean or other project was changed by this run.
