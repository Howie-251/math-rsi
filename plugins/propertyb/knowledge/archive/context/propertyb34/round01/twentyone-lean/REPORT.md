# T34 twenty-one-point formalization

Updated 2026-10-13 14:48 UTC. **The full twenty-one-point degree-five branch has been proved in Lean and connected to the original-target reduction.** The other twenty-one-point degrees and the 22–25-point branches remain open formal obligations.

## Exact exported statement

`Aris4Math.ThirtyFour.TwentyOneFive.propertyB_of_degree_five` takes an actual simple five-uniform hypergraph H on Fin 21, actual pair coverage, exactly 34 edges, and an actual vertex x with degree five, and returns `PropertyB H`. There is no profile, local-classification, probability, incidence-capacity or no-Property-B assumption in its final type.

`ThirtyFour.Assembly.target_iff_remaining_goal` now proves the equivalence of the original arbitrary-finite ≤34 target with precisely:

1. Actual pair-covering 21-point, 34-edge inputs with minimum degree at least six.
2. Actual pair-covering 22–25-point, 34-edge inputs.

This is a conditional reduction, not a completed T34 theorem.

## Mathematical coverage and actual inputs

Paper source: `context/propertyb34-hour1-20261013/low-math/TWENTYONE_FIVE_COMPLETE.md` and `TWENTYONE_FIVE_VERIFIED.json`.

- Pair coverage and degree five force every other point to have codegree one with x, so actual x-pair edges are unique.
- If another point has degree at most six, `TwentyOneFiveStructure.other_low` chooses the minimum-degree y and then z outside x,y, obtains degree(z)≤8 from the actual degree budget, proves the pair/triple inventory, and invokes full local coverage.
- Otherwise every point other than x has degree at least seven. The actual degree sum proves `15 ≤ 2*r+|L|`, where r counts sevens and L counts eights.
- Three or more sevens: every selected pair either has a strict triple witness or forces codegree two and an actual common edge with x. Uniqueness of the actual x-y edge joins two triples into one common four-point edge; both possible four-lock profiles are strict.
- Exactly two sevens: |L|≥11 supplies an eight outside the common x-y-z edge. Actual x-pair uniqueness excludes the two forbidden common triples. All resulting four-lock profiles are strict.
- Exactly one seven y: |L|≥13. Remove the actual x-y edge to obtain S. The proof uses the weaker sufficient estimate |S|≥8 after removing all five vertices, rather than needing the sharper |S|≥10. Every pair from S has the classified four-lock residue, which excludes any actual y-edge containing both. Pair coverage then requires at least eight incidences through only seven edges.
- No sevens: |L|≥15. Complete four-lock classification forces common-four count zero for every three L points together with x. Hence every actual x-edge contains at most two L points, so the five x-edges cover at most ten such points, contradiction.

The local classifiers consume actual trace multiplicities through `QuadProfiles.actual_recovered`, `high_inventory`, `QuadIncidence.triple_count` and actual incident-edge counting. No classification is assumed as an input.

## Numeric evidence and source map

- `TwentyOneFiveTriples.lean`: 74 labelled local profiles. Generator `generate_five_triples.py` independently recomputes exact total/pure deductions; maximum 24231/24310. Lean checks the real profile and all quota/numeric obligations.
- `TwentyOneFiveQuadData/Numeric/Quad.lean`: 95 retained four-lock witnesses. Generator `generate_five_quad.py` independently recalculates the saved avoided-subfamily dual inequalities; maximum 9723/9724. Lean verifies the exact rational certificates and actual-input coloring caller. Data compilation 21 seconds, numeric checks 235 seconds on this run.
- `TwentyOneFiveClassData.lean`: complete bounded local classification for the four degree patterns 5777, 5778, 5788, 5888, with actual pair inventories and the relevant common-edge premises; compilation 20 seconds.
- `TwentyOneFiveClassification.lean`: transfers that coverage to the real H.
- `TwentyOneFiveStructure/Local/Five.lean`: actual selection, budgets, unit-edge uniqueness, common-edge and capacity contradictions, complete degree-five dispatcher.

## Acceptance and reproducibility

- `build-five-triples-final.log`: success, 1004 jobs.
- `build-five-structure-final.log`: success, 1006 jobs.
- `build-five-quad.log`: success, 1011 jobs.
- **`build-five-assembly.log`: success, 1068 jobs; final source has no PANIC diagnostic.**
- **`FiveAudit.lean` / `five-audit.log`** independently restates the actual degree-five branch using a raw Finset of five-element edges and the original Bool-coloring condition. It also proves the conditional original target from bare `[Finite V]` and the precisely reduced remaining goal. All four transitive-axiom queries report only `propext`, `Classical.choice`, `Quot.sound`.

From the project root:

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
cd formal
lake build Aris4Math.ThirtyFour.Assembly
lake env lean ../context/propertyb34/round01/twentyone-lean/FiveAudit.lean
```

Earlier development logs are retained. A Lean simplifier procedure produced internal PANIC diagnostics while still returning kernel-checked proofs; the final two small actual-structure modules disable that simplifier acceleration and use explicit elementary reductions instead. The final build and independent import are the acceptance evidence. Numeric certificate modules retain their kernel checks unchanged.

## Remaining work

Continue with the complete degree-six paper map in `../twentyone-math/REPORT.md`: multiple sixes, unique six with no seven, unique six with sevens. The last subbranch requires five shared-bad-vector mixed-layout certificates, motivating the reusable weak-dual/actual-input interface described in `../middle-math/CANDIDATE_TWENTYTWO_SEVEN.md` §4. No formal strong-duality theorem or floating-point solver trust is needed.

All new modules are under `formal/Aris4Math/ThirtyFour/`; T32/T33 remain frozen. Parent owns cross-model review and global wiki/navigation updates. This report is local formalization evidence, not a cross-model acceptance claim.


## Degree-six continuation (2026-10-13, after the degree-five checkpoint)

The generic ordinary-quota mixed-layout interface and all five difficult 67888 local callers have now passed kernel builds and independent import/axiom checks. Details and exact scope are in `MIXED_LAYOUT_INTERFACE.md`; this supersedes any earlier statement that this interface was still outstanding. Final paper certificates use ordinary avoided-family quotas, so weighted-overlap strengthening is not a required formal dependency.

`TwentyOneSixStructure.lean` has built successfully (`build-six-Structure-r3.log`, 1037 jobs). In particular `propertyB_of_666` and `propertyB_of_667` start with actual H, pair coverage, 34 edges and three distinct points of the stated degrees, and conclude Property B with no table premise. The same module proves the actual residual conditions for degree triples 668, 677 and 678; a unit-root 688 pair has codegree at most two under non-Property-B; two degree-six points force every other point to have degree at least eight and at least thirteen points have degree eight. The transitive axiom prints for the two principal exports are the standard three.

The actual pair branch (incident degree 6 or 7, partner degree at most 8, codegree at least 5) is built in `TwentyOneSixPairs.lean`. Its count/profile realization is inherited from the proved arbitrary-codegree two-lock interface. The six ordinary three-lock datasets have respectively 90,103,101,118,105,11 strict profiles for 666,667,668,677,678,688; all are kernel checked. The generator reconstructs exact nested/avoided quota duals and repeats the rational formulas before emitting Lean. Local coverage and true multiplicities are supplied by `TwentyOneSixLocalTriples.lean`, not assumed as a classification hypothesis.

The independent helper `TwentyOneSixUnitSet.lean` passed its first regular build (`build-six-UnitSet-r1.log`, 1023 jobs, new module 1.2 seconds). Its scope is the analytic incidence consequence of explicit local residual premises; actual 6888 classification premises still must be supplied by its caller. `UNIT_SET_HELPER.md` documents this precise interface. Equality selection and the three-seven branch helpers are source drafts awaiting their next scheduled build, and are not yet counted as accepted results.

Ongoing work: finish actual four/five-lock classification callers, consume unit-set and equality selection, and close all three degree-six configurations. The complete degree-six branch is not yet assembled. Degree seven/eight and vertices 22–25 remain later formal obligations. T34 is not complete.

## 2026-10-13 16:06 UTC: complete actual minimum-six branch

`ThirtyFour/TwentyOneSix.lean` now exports
`TwentyOneSix.propertyB_of_degree_six H cover size minimum x dx : PropertyB H`,
where `H : Simple5Hypergraph (Fin 21)`, `size : H.edges.card=34`,
`minimum : ∀v,6≤H.degree v`, and `dx : H.degree x=6`.
The caller supplies no local trace, profile, probability, witness table, or graph
classification. The proof dispatches over another six, then zero, one, two,
or at least three seven-degree points. Every input is selected from H.
`build-queue-TwentyOneSix-r7.log` is the successful build (standard three axioms).

All four-lock finite coverage modules, all three five-lock exact domains,
and the five ordinary mixed-layout certificates used by the one-seven branch
have now been connected to actual inputs. `TwentyOneSixFiveLocal` closes the
fourteen 66888 and fourteen 67888 profiles; `TwentyOneSixFive67788Local` closes
the eleven 67788 profiles. Each high trace is derived from actual edge filters,
then the exact low traces are recovered, and the existing actual bad-vector
probability interfaces yield the original Bool coloring.

The actual selections use three convenient equivalent or weaker contradictions:

1. In the two-six unit-pair case, the established actual unit-set theorem gives
   capacity two on each six-point edge. Thirteen eight-degree unit neighbors
   already contradict total capacity twelve. No additional cap-one proof is needed.
2. The common five-lock selection for two-six and one-seven uses a set of at least
   seven unit neighbors. Six incident edges cannot all contain at most one; this
   selects the required actual common triple directly, without subtracting the
   forbidden root-pair edges first.
3. In the one-seven/double-root-pair case, the real unit set has at least eleven
   members, every root edge has capacity two, and either root-pair edge contains
   no member. Even charging just one additional unit for each root-pair edge
   gives `|U|+2≤12`, enough for contradiction. The sharper bound `|U|≤8` is not needed.

The two-seven implementation further selects its eight-degree vertices by
removing the union of all actual edges through the seven-degree pair. There are
exactly two such edges, each contains at most three eight-degree vertices, and
at least eight unit neighbors of the six-degree point exist. At least two
remain, which supplies the final two locks and every required clean triple.
This avoids an unnecessary intermediate choice of a third vertex.

`Assembly.lean` is being rebuilt with the exact remaining 21-point regime
`∀x,7≤H.degree x`; vertices 22–25 remain wholly in RemainingGoal. The new raw
Finset/Bool and bare-Finite conditional audit is `SixAudit.lean`. A successful
local branch is not a complete T34 proof. New audit/build results are recorded
below when the commands return.

Final commands returned successfully: `build-six-assembly.log` is exit 0,
`SixAudit.lean` / `six-audit.log` is exit 0. The four exported branch/assembly/raw
original/conditional-original declarations each have precisely `propext`,
`Classical.choice`, and `Quot.sound` as transitive axioms. The printed
RemainingGoal confirms 21-point minimum seven and all 22–25 inputs; this
conditional equivalence does not claim the unfinished T34 theorem.

## 2026-10-13 16:22 UTC: degree-eight compression and actual structure

The equal-degree lock permutations compress the saved single-layout numerical
witnesses for degree eight from 38 triple labels to 14 representatives and from
356 quadruple labels to 31 representatives. The 3 triple joint labels and
24 quadruple joint labels each form one orbit. The two five-lock star profiles
remain separate, one single-layout and one three-layout joint certificate.
All these representative probability modules have now built successfully;
see `build-eight-TwentyOneEight*.log`.

This compression does not assume a preferred order for actual vertices.
`LockRelabel.count_comp_perm` proves the exact relation
`count H (sigma.toEmbedding.trans f) T = count H f (T.map sigma.toEmbedding)`.
`TwentyOneEightTripleCoverage` and `TwentyOneEightQuadCoverage` check every
admissible local input and supply an explicit representative and permutation.
The lookup is just a proposed finite witness; Lean checks the entire bounded
parameter domain and every transported multiplicity. In particular the quad
coverage checks the full `Fin 6 -> Fin 2` pair domain and `Fin 5 -> Fin 3` high
trace domain under the actual triangle and pair-inventory restrictions.
No complete hypergraph is enumerated. Generators are `generate_eight_single.py`,
`generate_eight_joint.py`, and `generate_eight_coverage.py`.

Actual callers `TwentyOneEightTriples`, `TwentyOneEightQuads`, and
`TwentyOneEightStructure` have passed. Starting only with actual H, 34 edges,
pair coverage, minimum eight, and an internal assumption of no coloring, they
prove all pairs in the eight-degree set have codegree at most two, its unit graph
is triangle-free, and every four selected eight-degree vertices satisfies the
precise residual implications. The graph-counting helper
`TwentyOneEightGraph` has also passed: at least 19 eight-degree vertices, at
least six unit neighbors at each, and a contradiction from the actual C4/claw
and path-isolate rules. Its Rules input must still be fully supplied.
The two-profile star probability endpoint `TwentyOneEightStarLocal` has passed;
selection and exact trace binding of the actual claw extension are still in
progress. Accordingly the complete degree-eight branch is not yet claimed.

Cross-project reusable helpers built in the same exclusive queue:
`WeightedSubsetSelection`, `WeightedSubsetExtension`, `TwentyThreeSevenSelection`,
`WeightedThreePartition`, `FiveVertexClusterBound`, `TwentyFourMatchingSelection`,
and `LockRelabel`. The parent maintains their final reports and consumers.
The independent 23-point raw-selection audit returned exit 0 with eight standard
three-axiom declarations in `twentythree-seven-math/selection-audit.log`.

## 21-point minimum-eight branch closed (2026-10-13 UTC)

`TwentyOneEight.propertyB_of_minimum_eight H cover size minimum8` now proves the actual 34-edge, pair-covering, minimum-eight branch without auxiliary profile assumptions. The proof internally recovers triple and quadruple exact traces, uses equal-degree label permutations to transport strict local certificates, derives the actual unit-graph rules, and uses actual edge uniqueness to derive the graph contradiction. `TwentyOneEightClaw` closes the nontrivial claw obligation from the actual common edge and the two five-lock certificates.

The regular r16 builds of `TwentyOneEightClaw` and `TwentyOneEight` passed. `build-eight-assembly.log` passed after changing the exact remaining 21-point obligation to minimum degree **exactly seven** (minimum at least seven together with an attained degree seven). `EightAudit.lean` and `eight-audit.log` independently restate the eight-branch with raw five-element Finset edges and Bool colors, and call the conditional original theorem on an arbitrary `[Finite V]`. Four transitive axiom queries contain only `propext`, `Classical.choice`, and `Quot.sound`.

This is not the unconditional T34 result. The remaining actual obligations are 21 points of minimum degree seven and all 22–25 point inputs. Work is continuing on their finite local coverage and actual input bindings.

## Minimum-seven local interfaces in progress

The ordinary strict certificate modules now kernel-check 42 canonical `(7,7,7)` profiles, 88 `(7,7,8)`, 11 `(7,8,8)`, 18 `(7,8,8,8)`, 52 `(7,7,7,7)` and 10 `(7,7,7,7,7)` representatives. Corresponding numeric module times were 47, 106, 10, 32, 110 and 33 seconds in the regular serial build. The nine mixed-layout quadruple representatives also passed; their 71 labelled rows are recovered only through the pending permutation-complete coverage.

`TwentyOneSevenTriples` passed in r18. Its original-hypergraph statements derive that all codegrees in actual degree `(7,7,7)` and `(7,7,8)` triples are at most two, and that two degree-eight unit neighbors of a degree-seven point have mutual codegree at most two. The caller proves the preliminary pair bound and the three degree-inventory inequalities internally. The first coverage draft omitted these inventory constraints and kernel evaluation rejected it; the corrected complete domain and actual caller both pass. This was an interface-domain error, not an assumed additional restriction on H.

The quadruple classification is being connected to actual inputs. The five/six-lock stage will use a complete capacity-pruned local allocation generator and actual trace projection/splitting, rather than an unconstrained Cartesian product over all counts. Numeric certificates alone are not counted as solved 21-point branches.

### Local classification execution notes

The initial full `(7,7,7,7)` coverage evaluation was terminated by the system with exit 137. Splitting into 64 pair-vector declarations bounded the observed memory but still spent over 15 minutes evaluating a sparse natural-number pattern matcher; that precise owned process was deliberately terminated and its r19 log retained. The lookup representation was changed to a dense array on the 15,552 possible encodings. Data, kernel coverage, and actual callers were separated so that an API correction cannot invalidate the expensive finite kernel proof. These are representation changes; the 674 actual local profiles and 70 representatives are unchanged. Neither interrupted attempt counts as verification.

For the unique-seven branch, all high traces on five degree-eight tails fit in 925 complete pair-capacity allocations. The fixed actual root promotions retain 316; 205 use 39 ordinary plus one joint six-lock representative, while 111 already have one of two strict five-lock projections. The exact replay and source are `UNIQUE_CATALOGUE_REPLAY.json` and `generate_unique_catalogue.py`. The new formal source checks the complete allocation catalogue and its coverage in blocks of at most 100 allocations. These sources and the actual caller are not reported as passed until the corresponding regular build succeeds.

## 2026-10-13 17:42 UTC — degree-seven input interfaces and complete four-lock cover

The actual triple inputs (777, 778, and 788 with a common unit neighbor), actual 7888 unit-set structure, degree-seven counting budgets and the unique-seven six-lock selection now compile. The selected actual root-last locks have five degree-eight points, one degree-seven point, pair codegrees 2 among the five and 1 to the root, and exact root promotions 4 on the empty trace and 1 on each of {0,1}, {2,3}, {4}.

`TwentyOneSevenQuads.residual` now derives one of nine exact four-seven residual tables from arbitrary actual H, point-pair covering, 34 edges, four degree-seven locks and a contradiction hypothesis. Every one of the 674 local profiles is covered by kernel-checked statements. Build `build-quads-actual-r26.log` passes and the exported residual theorem has only the standard three axioms. No user-supplied local classification premise was added.

Performance experiment: the previous sparse Nat-pattern lookup plus 64 kernel statements ran for about 15 minutes and was explicitly interrupted. A 15,552-element dense array failed during data elaboration after 84 seconds with a stack overflow; that approach is rejected. The final associative list stores only 673 non-default choices, with the same 674-profile coverage domain. Data builds in 4.22 real seconds; the complete kernel builds in 87.75 real seconds, 83.93 user seconds, max RSS 8,123,957,248 bytes (`build-quad-kernel-r24.log`). This is a measured improvement of the complete coverage check, not just a data-generation comparison.

Shared actual `BoundedAllocations`, `PromotionCatalog`, `PromotionReconstruction`, `ActualAllocations`, and `LockLiftRelabel` all pass r22. The 23-point four-lock strict callers (75 pure, 5 joint) also pass, but their full original-input assembly belongs to the separate 23-point work.

The unique-seven allocation domain has 925 profiles, with 316 respecting the exact root promotions: 205 match strict six-lock profiles and 111 have strict five-lock projections. Data and the strict dispatch callers compile. The first full kernel attempt verified all ten certificate statements and the catalogue equality, then failed in the final disjunction dispatcher; the expensive certificates are now separated from that small caller, and the final proof is still pending. This is not yet an unconditional completed degree-seven branch or T34.

## 2026-10-13 17:53 UTC — complete unique-seven branch

`TwentyOneSevenOne.propertyB_of_one_seven` is now formally proved for every actual H on Fin 21 with 34 edges, pair covering, minimum degree at least seven, and exactly one degree-seven vertex. There is no local table, witness, capacity or probability premise. The proof internally chooses the six locks, derives their exact root promotions, puts the actual five-tail inventory into the full 925-allocation catalogue, checks all retained cases, and uses either a strict six-lock certificate or an actual five-lock projection. The exact 925-domain certificates compiled in 152 seconds, separately from the final actual caller.

`build-unique-one-r35.log` records `UniqueActual` in 1.7 seconds and `One` in 1.5 seconds, with the standard three axioms. `Assembly` now removes this branch, leaving minimum-seven inputs with at least two sevens plus all 22–25-point inputs. `build-one-assembly.log` and `OneAudit.lean` / `one-audit.log` both pass; the independent bare Finset/Bool restatement and conditional [Finite V] original statement also use only the standard three axioms.

A specific Lean performance issue was resolved: `have matched := coverage values …` tried to reduce the symbolic catalogue conclusion and exhausted heartbeats. A local irreducibility annotation on `Matched` prevents unnecessary elaborator unfolding. The kernel still hit deep recursion when the dispatch proof was inlined after substituting the actual edge-count vector. Proving `propertyB_of_matched` first for an abstract `values : List ℕ`, then applying it to the actual vector, fixes that excessive reduction. This changes proof organization only; the catalogue, accepted domain and mathematical conclusion remain identical. The failed and interrupted attempts are retained, and only r35 plus the independent audit are success evidence.

## 2026-10-13 17:58 UTC — final checkpoint: many-sevens and exact assembly

`TwentyOneSevenMany.propertyB_of_many_sevens` now proves Property B from actual H21, pair covering, 34 edges and at least five degree-seven points. The full 3,618-capacity-allocation cover is kernel-checked; the finite dispatch either uses one of the ten strict five-lock representatives or a strict four-lock projection. `TwentyOneSevenQuads.residual`, real promotion membership, full count reconstruction, permutation lifting, actual projection and the original coloring are all connected internally. No graph-shape or local-catalogue premise remains in the exported branch theorem.

The expensive `TwentyOneSevenManyCatalogueCertificates` module passed in 357 seconds (`build-many-kernel-r31.log`, full command 360.32 real seconds, max RSS 8,989,097,984 bytes). The first small dispatcher needed explicit finite labels after `fin_cases`; after correction the immutable numerical module was reused. `build-many-r38.log` passes: Kernel 1.5 seconds, ActualCore 1.0 seconds, Actual 1.3 seconds and Many 1.3 seconds. ActualCore exposes its classification function only as a modular helper; Actual instantiates it with the checked complete catalogue and Many exports the original branch with no such parameter.

`Assembly.target_iff_remaining_goal` is now verified with exactly these remaining obligations:

- H on 21 points, 34 edges, pair covering, minimum degree seven, and **two to four** degree-seven vertices.
- H on each of 22–25 points, 34 edges and pair covering.

`build-many-assembly.log` is PASS. `ManyAudit.lean` / `many-audit.log` independently restate the raw Finset/Bool at-least-five-sevens conclusion and conditional original [Finite V] goal. `OneAudit.lean` was rerun against the final Assembly in `one-audit-final.log`. All eight audited declarations have only propext, Classical.choice and Quot.sound. This is a partial T34 assembly, not a proof of T34 or m(5)≥35.

The separate 23-point 3-to-4-lock connection is also complete within its stated scope: `TwentyThreeFewLowFourNumeric` passes in 46 seconds (`build-23-four-numeric-r37.log`, 47.41 real seconds, max RSS 5,838,061,568 bytes), and `TwentyThreeFewLowFourClassified` passes r39 with actual complete coverage, role-preserving relabelling, 75 pure plus 5 mixed strict callers, and 22 / 19 residual cases. `actual_residual` requires the actual old three-lock inventory and new pair capacities as stated; it does not by itself close the 23-point branch.

No new large domain is started after this checkpoint. Continue using `DEGREE_SEVEN_CONTINUATION.md`, the root progress page and these successful logs. The root agent owns the final Goal status, navigation and cross-model review records.
