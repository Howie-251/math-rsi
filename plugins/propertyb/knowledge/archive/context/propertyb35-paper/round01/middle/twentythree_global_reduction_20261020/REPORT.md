# 23-point whole-branch reduction: handoff

The new result covers the entire23-point minimum-seven class: a non-B simple five-uniform hypergraph with35 edges must have minimum degree at least three in the graph of original edge pairs whose intersection is not one. The23-point coloring branch itself remains open.

The exact local theorem is slightly stronger: only the five points of a selected edge $F$ need degree at least seven; if that edge has exactly two non-unit-intersection neighbors, the original $H$ is colorable. No outside minimum degree, pair-cover, edge-criticality, maximum degree, or point-pair codegree hypothesis is needed. The q≤1 part of the Γ-minimum-three conclusion imports the existing unconditional23-point repair.

## Proof and independent scope

- [Q2_PROOF.md](Q2_PROOF.md): actual35-edge inventory, a single common anchor sample, and all19 trace types. If all five anchors failed the bound, their forced singleton counts would sum to at least33, contradicting the exact sum32.
- [SIX_RED_PROOF.md](SIX_RED_PROOF.md): the new universal six-four-set lemma on18 outside points,11 red: red-event union at most6·3432−2616. The proof uses compatible forests and upper third-order Bonferroni; it does not enumerate set families or H.
- [SIX_RED_REVIEW.md](SIX_RED_REVIEW.md): complete independent written review of the six-set proof and the19-row actual-caller proof. Same-family/provisional, no cross-family or Lean claim.
- [SIX_RED_CHECK.json](SIX_RED_CHECK.json): PASS;36 feasible triple Venn rows, all141 rank≤2 heavy graphs, complete case arithmetic, CPU0.095865s.
- [Q2_THRESHOLD_CHECK.json](Q2_THRESHOLD_CHECK.json): PASS; all19 size/intersection types, minimum forced sum33, CPU0.000090s.
- [Q2_INDEPENDENT.json](Q2_INDEPENDENT.json): PASS; all351 unordered labeled exceptional trace pairs, repeated traces retained, all150315 necessary singleton-count compositions, no S5 quotient or discovery-table import. Maximum31808/31824, success margin16, CPU0.164275s.

The profile scripts retain the earlier hypothetical six/eight-set thresholds as discovery evidence. The accepted new interface uses only the proved six-set2616 deduction, not an unproved eight-set lemma.

## One bounded global scalar test

Only the original balanced minimum-seven spectrum $7^9,8^{14}$ was retested with the new Γ-minimum-three box31. The exact necessary moment domain still has64220 keys. Non-strict keys decrease from6633 to4902;1731 keys become strict, but no whole spectrum is closed. The maximum is19918800 against threshold18811520. The complete4902 remaining keys are saved in [MIN7_GAMMA3_PILOT.json](MIN7_GAMMA3_PILOT.json); CPU0.200012s. [SCALAR_METHOD.md](SCALAR_METHOD.md) records every bound and the necessary integer domain.

The new vertex flag-square capacity does not improve the old five-bin shared P bound anywhere in this balanced spectrum. The two rare minimum-six spectra in [SCALAR_PILOT.json](SCALAR_PILOT.json) likewise remain non-strict. These failures justify stopping the moment extension: no scan of all135 minimum-seven degree spectra, new locking layout, LP, or whole-H search was performed. The old [CORE2_PILOT.json](CORE2_PILOT.json) also retains its five non-strict tiny fixed-layout checks; it is not a theorem or an actualH counterexample.

## Cross-branch reuse at22 points

[TWENTYTWO_Q3_EIGHT_CALL.md](TWENTYTWO_Q3_EIGHT_CALL.md) directly applies the existing eight-red-foursets-on17-points theorem to actual22-point q3 sources20–23. All three exceptional traces7,27,29 contain point0 and are proper when it alone is red in F; a0=8 leaves exactly eight distinct red four-sets and23 indexed blue four-sets. The old quantitative deduction1218 gives bad≤19088<19448, leaving360 samples. [EIGHT_RED_22_CALL_REVIEW.md](EIGHT_RED_22_CALL_REVIEW.md) independently verifies the old proof and the exact source fields.

Thus the old three role classes reduce to source24, a=(9,5,5,6,6). Its pairwise-linear nine-red branch is also eliminated:36 incidences on17 points force at least21 one-point intersections, and upper Bonferroni gives deduction2619 and bad≤19117<19448. [NINE_LINEAR_CHECK.json](NINE_LINEAR_CHECK.json) checks this conditional arithmetic. A non-B realization of source24 must therefore contain a red outside four-set pair intersecting in at least two points. The remaining heavy branch is assigned to root's separate nine-red lemma effort; it is not closed here.

The17-point six-set1044 variant was independently derived and checked before the old eight-red import was noticed. Its optional proof remains in [SIX_SEVENTEEN_REVIEW.md](SIX_SEVENTEEN_REVIEW.md), with [SIX_SEVENTEEN_CHECK.json](SIX_SEVENTEEN_CHECK.json). It is unnecessary for the direct22-point source20–23 closure, which should cite the stronger existing eight-red theorem.

## Remaining scope and handoff

Whole23 minimum-six and minimum-seven coloring remain open. The minimum-seven line now has the general Γ-minimum-three reduction. The minimum-six line is handed to the common L6 effort; this directory adds no L6 coloring claim. A useful elementary handoff is that if x is six-degree and U is its unit-neighbor set, every non-U edge meets K={x}∪D, where D comprises the one or two repeated-codegree partners. Since a non-B five-uniform H has transversal number at least five, τ(H[U])≥5−|K|: at least three for |D|=1 and at least two for |D|=2. If those minima equal the number of U-edges, the U-edges must be pairwise disjoint. This is only a structural condition, not a coloring repair.

All new work is confined to this directory. No Lean, v2 access, frozen-proof edit, navigation change, or globalm(5)≥36 claim was made. The new23-point proof is paper-provisional with deterministic local coverage and a same-family independent read; designated cross-family acceptance remains a separate project step.
