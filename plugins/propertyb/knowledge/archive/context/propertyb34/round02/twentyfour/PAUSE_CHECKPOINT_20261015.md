# 24-point T34 Lean checkpoint — 2026-10-15

Parent requested a stop while the user considers pausing T34 Lean and pursuing higher-bound paper work. No new implementations or probes should start from this checkpoint without the parent/user continuation. All subagent lightweight processes have ended. No claim that the entire 24-point branch, T34 Main, or m(5)≥35 has passed Lean acceptance.

## 1. Frozen complete branch: no six-degree vertex

`TwentyFourNoLow.propertyB_of_no_six` has regular PASS from actual H on Fin 24, pair covering, exactly 34 edges, and zero six-degree vertices to Property B. All actual selection, complete local classification, original counts, exact probabilities and coloring witness are internal. Standard three axioms. Root has independently read the regular log and integrated this into the shrinking Assembly obligation.

Do not rerun or rewrite the passed NoLow modules. The 352/467 local domains and 46 numerical profiles are complete, not a graph search. Sparse support/explicit row coverage solved the old lookup-per-64-types bottleneck. The previous slow attempts remain historical evidence only.

## 2. Six-low nonunit pair branch: numeric half complete, coverage kernel still open

Parent regular results at stop:

- All 181 exact numerical certificates, split into `TwentyFourSixLowBadNumericCases0` through `Cases18`, PASS.
- Recovery0 through Recovery5, aggregate Recovery, BadNumeric and Bad actual-counts caller PASS. The final exact μ→profile binding and all avoided quotas/overlap penalties are retained.
- `TwentyFourSixLowBadData` sparse representation PASS earlier, 69.82 s.
- Latest `TwentyFourSixLowBadCoverageData` PASS 10.02 s.
- Latest `TwentyFourSixLowBadSparseData` PASS 9.09 s.
- Latest `TwentyFourSixLowBadSparseBridge` PASS 30.32 s.
- **`TwentyFourSixLowBadCoverageKernel` timed out at 240 s. It has NOT passed.** Do not infer that Actual/Complete passed from the preceding layers.

The mathematical domain remains the original 467/611/787 high-trace allocations, 1,870 in total, mapped to the original 37+90+54 = 181 representatives. Fixed original certificate sources are the three hour1 `MIXED_SIX_v24_low6_bad*.json` files. No layouts were searched again. Current representation uses explicit `(values, case, permutation)` rows and sparse support comparisons, not repeated linear choose lookups inside every type test.

Regular resume order after diagnosing the concrete Kernel cost:

1. CoverageKernel only; retain the prior timeout log and passed inputs.
2. `TwentyFourSixLowBadActual`.
3. `TwentyFourSixLowPairPatterns` / `TwentyFourSixLowSelection` if not already regular built.
4. `TwentyFourSixLowBadComplete` and the bare finite-edge/Bool `SixLowBadReviewAudit.lean`.

Endpoint source: `TwentyFourSixLowBadComplete.propertyB_of_nonunit_low_pair` and `unit_of_not_propertyB`. The endpoint is **not accepted until the remaining dependency chain builds**. Earlier same-family static review found and fixed the missing Bad caller import; that review did not execute any enumeration or probability check.

Detailed numeric build map and generation commands: `SIX_LOW_BAD_BUILD_MAP.md`. The passed NoLow/BadData/Numeric/Recovery sources are frozen. Do not regenerate them while resuming the coverage diagnostic.

## 3. Unit six-low classification and five strict canonical types

### Complete actual classification, lightweight verified

`TwentyFourSixLowUnitData` and `TwentyFourSixLowUnitActual.actual_classification` reuse the already complete NoLow six-lock catalogue. For any actual six unit degree-six locks, the theorem produces a genuine common relabeling and one of nine canonical full trace inventories. All singleton/empty counts are recovered at degree six, rather than reusing degree-seven counts accidentally.

Combined actual-classification light probe PASS 10.20 s / 3.39 GB, standard three axioms. Data alone light PASS 9.09 s. These were requested for regular build but no regular result has been reported to this subagent at stop.

### Canonical type 6: original one-layout certificate

`TwentyFourSixLowUnitFiveBlockData`, `...Numeric`, `TwentyFourSixLowUnitFiveBlock` contain the original 47649/48620 certificate, including quota/capacity repair and the actual-counts-to-PropertyB caller. Combined lightweight PASS 10.02 s / 3.16 GB, standard three axioms. No new search. Generator: `generate_unit_fiveblock.py`.

`TwentyFourSixLowUnitStrict.five_block_counts` is the final equality identifying this one-case certificate with canonical UnitData type 6; it is in the not-yet-built aggregate caller.

### Generic average interfaces

- `TwentyFourActualSlotAverage`: choose one real bad pair at each low center before varying layouts, then average its deleted contribution. No independence between layouts or centers is assumed.
- `TwentyFourSlotAverageTable`: reduce to a complete finite list of admissible real slots, up to interchanging the two actual edges.
- `TwentyFourSlotAverageCache`: connect exact cached A/B/C/free expressions to the original Numeric formulas via `CachedRows.rows_eq`.

ActualSlotAverage + Table combined light PASS 2.71 s. Cache has been exercised by all subsequent successful inline numeric pilots. Regular builds were requested but not yet reported here. No generic interface replaces the obligation to supply its finite certificate.

### Canonical types 2, 4, 7: sources ready, pilots distinguish their actual scope

The generator `generate_unit_averages.py 7 4 2` reads the existing hour1 exact certificates. Types 2/7 use the stored automorphism averages; their stored source relabeling is absorbed into the explicit positions, retaining the original canonical UnitData μ. Type 4 uses the stored 25-layout rational mixture. Fraction replay exactly reproduces:

| Type | Layouts | Admissible unordered slots | Bound |
|---|---:|---:|---:|
| 2 | 48 | 58 | 11954/12155 |
| 4 | 25 | 54 | 242899731/243095138 |
| 7 | 12 | 47 | 12107/12155 |

For each type, generated source modules are `TwentyFourSixLowUnitAverage{type}Data`, `Core`, `Rows{batch}`, `Slots{batch}`, and an aggregate caller without the suffix. Batches have at most five layouts. All actual μ→profile equalities, valid profiles, fixed-slot completeness and strict bounds are present in source; the full chains have **not** been regularly built yet.

Actual lightweight evidence:

- Type 7 complete Data/API/Core (all profiles, all slot coverage and final average): PASS 8.40 s / 2.91 GB.
- Type 7 first five layouts' full A/B/C/free equalities: PASS 15.97 s / 3.35 GB.
- Type 7 first layout's all 47 slot contributions: PASS 5.69 s / 2.43 GB.
- Type 4 first layout's full A/B/C/free: PASS 10.54 s / 2.95 GB.
- Type 4 complete Data/API/Core after per-slot splitting: PASS 15.84 s / 2.64 GB.
- Type 4 first layout's all 54 slot contributions: PASS 7.69 s / 2.67 GB.
- Type 2 first-row inline probe hit 20 s at 2.48 GB; **not PASS**. Its full 48-layout Data prefix was included in that cost. The next useful check is a standalone regular Data build, then bounded rows/slots against its olean.

Performance corrections retained: an initial all-64-by-64 slot coverage probe hit the 4 GB ceiling. Positive trace support is now proved complete before enumerating pairs. Type 4's monolithic final average also hit 4 GB; splitting its universal slot bound using `fin_cases` made the complete Core pass. These changes preserve the exact finite domains and formulas.

Regular resume order per type: Data → Core → Rows batches → Slots batches → aggregate caller. Start with 7, then 4; for 2 build only Data initially to measure its independent cost. Group 7 and 4 source was explicitly frozen after passing pilots.

## 4. Canonical all-pair type 0: exact average reduced, full chain still unverified

Original paper certificate averages all 720 label permutations and gives 2203/2210. A deterministic family of 120 permutations from explicit invertible 2×2 matrices over the five residue classes (acting on five labels plus an infinity label) has been extracted. These are all members of the old 720-layout family. Direct Fraction replay of every admissible slot gives **the identical bound 2203/2210**, with per-center bound 679/6630. This was a prescribed finite compression, not a new layout optimization search. The Lean certificate does not need to trust a group-theory theorem; it checks the explicit positions and averages themselves.

Sources `TwentyFourSixLowUnitAverage0*` are prepared, with these representations:

- Data: explicit 120 layouts and 90 unordered slots; dense slot values stored as integer arrays divided by the common denominator 2210. A-values use denominator 340, C-values 2210. γ=1/120 and free=13/34 are constant functions.
- `p` is the exact proposed literal profile immediately available for arithmetic. Its original μ→computed-profile binding has been moved to 24 `Profile{batch}` modules of five layouts each, then combined by `Profile`. This binding is not omitted or assumed.
- `TwentyFourCachedCongruence.rows` proves cached rows unchanged by reordering the actual type list when v, positions and the type Finset agree. Lightweight PASS 2.16 s.
- `...Average0Rows` computes one canonical profile's 24 rows and uses the above generic congruence plus exact position/type-set identities to recover all 120 layouts. This replacement is source-complete but not yet independently compiled. The old generated Rows0…Rows23 files remain on disk as unused fallback, not dependencies of the final aggregate.
- Slot contribution certificates remain split in 24 batches of at most five layouts. The exact average and full μ→profile binding remain independent obligations.

Actual light evidence:

- Data/API + first full probability row PASS 18.31 s / 2.81 GB.
- Data/API + first actual μ→profile binding PASS 13.76 s / 2.54 GB.
- An inline full 120-layout geometry prefix hit 20 s at 2.49 GB; **not PASS**. This repeated the entire Data elaboration. No standalone Rows result exists yet.

Next regular prefix requested: `TwentyFourCachedCongruence` then `TwentyFourSixLowUnitAverage0Data`. After its olean exists, run bounded independent Core / geometry / reference-row / slot / Profile checks. Do not assume all 120 layouts passed from the first-layout pilot.

Canonical generation order for this optimized source (do not run against in-flight builds):

```sh
python3 context/propertyb34/round02/twentyfour/generate_unit_averages.py 0
python3 context/propertyb34/round02/twentyfour/optimize_unit_zero_data.py
python3 context/propertyb34/round02/twentyfour/compress_unit_zero_rows.py
```

## 5. Actual structural contradictions, lightweight verified

`TwentyFourSharedSingletons.at_most_three` is generic in n and v. For three pairwise-unit high vertices, suppose each uses a singleton-low edge at every label in S, and each such singleton fiber contains at most two edges. A collision pair of highs at each low label gives an injection from S to the three high pairs; hence |S|≤3. This is an actual edge-counting theorem, not a numerical type-table assertion. Lightweight PASS 2.16 s / 1.91 GB, standard three axioms.

`TwentyFourSixLowResidualContradictions.impossible_three_typeA` applies it to the same four small singleton labels in canonical unit types 3 and 5, unifying the two separate paper contradictions. `impossible_binary_opposites` excludes three highs that are pairwise opposite A/B types. Combined lightweight PASS 3.94 s / 1.91 GB, standard three axioms.

The remaining one/two-high classification must still supply these occurrence / A/B / pairwise-unit hypotheses. These conditional structural theorems alone do not close the six-low branch.

## 6. One/two-high actual classification: next implementation, not yet delivered

The original remaining canonical low types are 1,3,5,8. Their complete first-high domains have 50,32,37,12 labelled inputs (131 total). Only 17 of the labelled one-layout certificates are strict directly; the remaining labels compress to 22 colored orbits, of which 17 have strict mixed-layout certificates and five remain.

Do not incorrectly describe this step as only 131 cheap numerical rows: it includes actual-promotion coverage, canonical relabeling, 17 mixed-layout certificates, and then the second-high restrictions on the same H. Sources:

- `context/propertyb34/round01/high-math/SIX_LOW_EXTENSION.json`
- `SIX_EXTENSION_JOINT.json` and independent replay
- `SIX_LOW_TWO_HIGH.json`
- `SIX_LOW_HIGHER_CODEGREE.json`
- `SIX_LOW_THREE_HIGH.json`
- paper `CANDIDATE_SIX_LOW.md`

Existing generic `PromotionCatalog`, `PromotionReconstruction`, `LockExtension` already supply most actual-input machinery. Newly added `TwentyFourUnitPromotionBase.decoded_codegree` and `promotion_le_one` are lightweight PASS 2.16 s. They prove exact low-new unit codegrees on a decoded promotion vector and cap every nonempty actual promotion by one. **No new 131-input Data/coverage module was created before stopping.** That is the next coding task, not an already implemented obligation.

`TwentyFourSixLowUnitStrict` is a source-level aggregate joining the five strict type callers to the complete actual nine-type classification, returning only types 1,3,5,8 under noB. It has not been compiled because its average dependencies are still pending.

## 7. Other 24-point branches and reuse boundary

- At least seven unit six-degree vertices: original fourteen seven-low triple orbits, strict six-projections, two seven-auto averages, and two residual mixed averages still need their complete actual Lean connection. Paper is `CANDIDATE_SEVEN_LOW.md`; do not call this branch finished from six-low classification alone.
- r=1…5: not implemented by this continuation. Existing actual eight-matching selection and paper/JSON evidence remain available. No new search was started.
- r=5 final nine-unit-lock step can reuse the 25-point q5 numerical endpoint after adding one isolated vertex. The 25 agent confirms its source endpoint `TwentyFiveFiveLow.propertyB` assumes only size34 and `TwentyFiveSelection.MixedLocks H 5 4`, **not PairCovering**. The full q5 endpoint was not yet accepted at stop; root had only some groups passed and agent25 was compressing families. Do not use the 25-point pair-covering main branch on the isolated-vertex extension.

## 8. Build discipline and provenance

Parent alone runs regular/heavy builds. This subagent used `run_short_probe.py`, capped at 20 seconds or 4 GB process-group RSS. A timeout or cap hit is not a theorem failure or acceptance. No own probe is in flight. All numeric profiles, finite domain generators, finite coverage, generic actual bridges and end-to-end callers remain separate artifacts.

Original NoLow and the passed BadData/Numeric/Recovery modules stay frozen. New unit modules and generic interfaces have the precise provisional status listed above; no aggregate acceptance or new final cross-family review has been claimed. Root coordinates Grok/Gemini and the global wiki/Assembly.
