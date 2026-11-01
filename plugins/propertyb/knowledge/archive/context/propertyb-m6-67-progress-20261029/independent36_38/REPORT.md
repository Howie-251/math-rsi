# Independent audit of the complete 36–38-point branches

**Verdict: PASS WITH DECLARED IMPORTS, same-family/provisional.** The complete actual selection and local-type coverage in `mid34_38/PROOF36_38.md` is sound under its stated imports. Independent injection-probability arithmetic verifies a strict bound on every retained type. This audit concerns these three internal branches, and does not assert the full m(6)≥67 theorem.

## Inputs and independence

Read in full: `mid34_38/PROOF36_38.md`; `REPORT.md` Lemma 1; the corresponding five final JSON certificates and their generation scripts. The original conditional random-greedy witness mechanism and minimal-counterexample reduction are declared imports.

The probability function is extracted from the pre-existing independent falling-factorial/injection implementation `context/propertyb-m6-66-20261029/independent/check.py`. The submitted conditional-probability module is not imported or called. Four-lock clique multisets are regenerated using an independently written recursion on the first positive pair capacity; the submitted generator instead orders block indices. Full canonical domain sets, rather than only their counts, agree.

The component-support link quota is a declared mathematical import. This auditor authored that separate lemma, so this audit is **not** independent validation of that lemma. Root assigned its verification to another agent. The quota currently imported includes all three proved component bounds: Caro–Wei, feedback-vertex-to-forest, and the unique-complement support bound. This can differ from the weaker quota used in the submitted adaptive calculation, but remains a valid imported strengthening.

## Mathematical selection review

The fixed-unit-edge weak-wedge lemma is correct. Under failure, each unit neighbor of b inside R other than a is a codegree-at-least-three partner of a and is not a unit neighbor of a. Thus the lower row bound counts disjoint sets of entries. Adding the two resulting row inequalities gives the opposite of the stated strict inequality. No arbitrary unit edge is substituted for the specified one.

At v36, minimum degree ten, the actual set R={degree≤12} has at least 24 vertices, by 396≥468−3|R|. A specified minimum-degree point a has at most fifteen nonunit partners, hence at least eight unit neighbors inside R. The chosen unit edge has degree sum at most22 and satisfies 110<114. The weak wedge retains a, so its three degrees are exactly of the required form (10,e,f), 10≤e≤f≤12. Relabelling the other two points is harmless because the certificate includes the position of every possible doubled pair. All 48 degree/codegree/triple-intersection types are present.

At minimum degree eleven all v36 degrees are eleven. Every vertex has at least fifteen unit neighbors, so an actual unit edge exists. Taking R=V gives 110<138. Relabelling the unit-wedge center is valid because all degrees agree. The endpoint codegree-one/two and triple-intersection-zero/one cases are exhaustive. Both codegree-one traces are strict directly; both codegree-two traces are completely continued.

The v37/v38 successive-minimum-unit-neighbor selection is correct: the chosen second point is minimum over the actual first unit pool, and the chosen third is minimum over the actual common pool. Therefore their degree order and budget inequalities both hold. Independently rebuilding the complete minimum-degree/partner ranges gives exactly nine branches at37 and six at38. Every unresolved two-lock branch there has positive common-pool bound; both triple traces and every integer third degree are present.

The fourth-lock lemma correctly removes twice the internal pair excess from the three actual excess rows. At most floor(E/2) outside points have excess≥2, leaving the stated eligible pool. Charging all outside points at the same actual minimum degree gives the fourth-degree bound. The independent checker recalculates those values from the parent degrees and codegrees. All required pools are positive: minimum three for the27 parents at37/38, and minimum two for the19 minimum-ten parents at36. The regular-eleven case has E58 and pool4.

Every actual multi-lock trace is a multiset of clique blocks whose pair multiplicities equal the codegrees. Preserving the exact restricted parent multiset is necessary and is enforced in both the submitted and independent domains. Singleton and empty traces are then forced by actual degree and total-edge equations. No realizability assumption is added.

## Independent finite coverage and arithmetic

`check.py` verifies:

- All adaptive minimum-degree and minimum-unit-partner branches at36,37,38, including equality of every conditional three-lock domain and every recorded failure list.
- All27 failed adaptive parents at37/38, giving all1452+855 fourth-lock types.
- All48 minimum-ten weak-wedge types at36, with all19 failed parents continued to all3048 fourth-lock types.
- Both directly successful regular-eleven traces and all31 fourth-lock continuations of its other two traces.
- The actual degree multiset, trace multiplicities, lock positions, edge count66, pair multiplicities and nonnegative traces.

For four-lock rows the independent calculation uses the old valid quota and the maximum of separately minimized avoided-subset deductions, exactly as the submitted four-lock engine. Every resulting rational equals its submitted value.

Adaptive rows sometimes need the stronger joint deduction rather than this maximum. The independent implementation first computes max_R and uses a separate exact covering dynamic program when max_R alone is not strict. All zero-weight cells may be filled to capacity because constraints are lower bounds and this costs zero. It then recursively processes positive-weight cells, retaining the remaining quota vector. A cell need not exceed the maximum remaining quota it affects: larger values cannot further improve feasibility and have nonnegative cost. This finite capped-state optimization therefore gives the exact joint minimum for the imported quotas. It is separate code from the submitted exceptional-cell enumeration.

The final recorded branch maxima are:

| Vertex count | Independently replayed rows | Largest actual bound |
|---:|---:|---:|
|36|3234|480239/480240|
|37|1495|1334992/1335015|
|38|875|9343777/9345105|

The replay count includes redundant passing adaptive cases where a later broader weak-wedge argument would already suffice. This redundancy does not replace any required branch. The v38 maximum includes adaptive rows; the fourth-lock-only maximum is7563883/7565085, as in the submitted proof.

`REPLAY.json` saves every independent fraction beside the submitted fraction. `RESULTS.json` records execution time and exact comparison counts. The second execution added explicit failure-list equality checks and saved the replay ledger; it was justified by those initially missing audit records, not by changes to the mathematics.

No Lean, external model review, original-hypergraph enumeration, or cross-family acceptance was performed here.
