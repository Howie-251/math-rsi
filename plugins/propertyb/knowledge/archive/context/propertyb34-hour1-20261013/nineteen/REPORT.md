# T34 first hour: nineteen-vertex formalization

2026-10-13. The complete actual nineteen-vertex branch is now checked in Lean.

`Aris4Math.ThirtyFour.nineteen_propertyB` takes an actual simple five-uniform hypergraph on `Fin 19`, pair coverage, and at most 34 edges, and returns the original `PropertyB H`. There is no supplied probability bound, local table or numeric certificate premise. Pair covering is an internal reduction condition; this branch alone is not the all-vertex T34 theorem.

## Checked chain

- `NineteenSelection.exists_selected` proves coverage by degree 5–7, a unit `(8,9)`/`(8,10)` pair, a degree-eight pair of codegree 3–8, or three degree-eight vertices whose pair codegrees lie in `{1,2}`. Its small-low-set branch derives every high degree ≤10 from the true total incidence 170 and obtains a high unit neighbor from the true good-partner budget.
- `NineteenSingle.propertyB_of_degree_five_to_seven` recovers the two actual type counts and supplies the actual bad-pair deletion. All three numeric inequalities are kernel checked.
- `NineteenPairs.propertyB_of_high_pair` recovers the four actual pair type counts for 34 edges, prunes zero rows, and applies the eight kernel-checked uncorrected profiles.
- `NineteenTriples.propertyB_of_three_eights` handles all 17 labelled codegree/triple-count profiles. This is the complete labelled expansion of the nine isomorphism types, avoiding any assumed symmetry quotient. Actual eight type multiplicities are recovered by the existing general inclusion-exclusion theorem. The finite coverage theorem proves every actual `(a,b,c,t)` is in the list.
- For each three-lock center, the proof chooses either the actual total bad-link quota or the actual pure-link quota, whichever gives the recorded stronger bound. It does not add overlapping quotas. The pure case instantiates the already proved avoided-lock dual with one quota avoiding both other locks. This simpler bound suffices for every profile; the largest selected bound remains `707/715 < 1`.
- `nineteen_propertyB_of_eq` assembles these actual inputs. `nineteen_propertyB` reuses the old 33-edge theorem only when the number of edges is below 34.

## Executed verification

From `formal/`, with the project-local elan environment:

```sh
lake build Aris4Math.ThirtyFour.Nineteen
lake env lean ../context/propertyb34-hour1-20261013/nineteen/Audit.lean
```

The explicit build completed successfully (1010 jobs, exit 0). `build-nineteen.log` contains the actual final declarations' transitive axiom output: only `propext`, `Classical.choice`, `Quot.sound`. The independent import in `Audit.lean` restates the claim using a bare finite edge set, literal pair coverage and an actual Bool coloring with 1–4 red vertices in each edge; `audit.log` records exit-0 output and the same three axioms.

Earlier failed development builds remain in `build-triples.log` and `build-small.log`; they are not acceptance evidence. No `sorry`, new axiom or `native_decide` is present in the new sources. `generate_triples.py` chooses local positional witnesses and writes `TRIPLE_DATA.json`; Lean checks the resulting data and binds it to actual hypergraphs. The Python generator is outside the theorem's trust basis.

Old T32/T33 source and delivered files were not changed. This is a local incremental build and independent import, not another-machine reproduction. Cross-family review is being coordinated by the parent agent.

## Original-input reduction also completed

`ThirtyFour/Target.lean` defines the unchanged original object and coloring semantics at 34 edges. It is a target declaration, not a theorem claiming T34.

`ThirtyFour/SmallVertices.lean` proves `propertyB_of_vertices_le_eighteen` for every actual hypergraph with at most 34 edges. For 17/18 vertices, a balanced red set is constructed making any selected two five-edges both monochromatic: when disjoint, put them in opposite colors; when intersecting, contain their at-most-nine-vertex union in a nine-vertex blue set. Identity belongs to both actual bad-permutation events. The cardinality of their union is therefore strictly below the sum, and the weak numerical boundary 34*(1/34)=1 becomes strict. The proof does not require enumerating colorings or calculating the exact overlap probability.

`ThirtyFour/Reduction.lean` proves the actual minimal-counterexample reduction, the ≤25 vertex bound, padding to exactly 34 edges, and the equivalence

```lean
Aris4Math.ThirtyFour.target_iff_remaining_goal :
  Aris4Math.Target34 ↔ Aris4Math.ThirtyFour.RemainingGoal
```

`RemainingGoal` requires coloring only pair-covering hypergraphs with exactly 34 edges on `Fin v`, for 20≤v≤25. The nineteen-vertex theorem has been internally discharged. This is an equivalence with an explicitly **unproved remaining obligation**, not a theorem of T34.

Executed `lake build Aris4Math.ThirtyFour.Reduction`: 1017 jobs, exit 0, recorded in `build-reduction.log`. Its exported reduction and small-vertex declarations have only the three standard transitive axioms. `ReductionAudit.lean` independently imports this module and invokes the conditional assembly from bare `[Finite V]`, a finite set of five-element edges, and ≤34 edges; the remaining theorem is an explicit hypothesis. `reduction-audit.log` records the expanded target/remaining definitions, successful elaboration and standard axioms.

### Remaining work

The mathematical branches v=20,21,22,23,24,25 remain open globally. Other agents may close selected subbranches during this hour; this formal report records only the modules above. No full T34 proof or new m(5)≥35 lower bound has been established.

## Twenty-vertex minimum degree at most six also completed

The parent then supplied `../low-math/LOW_DEGREE_SIX.md` and its seventeen exact numerical witnesses. The new modules `TwentyLow.lean` and `TwentyLowComplete.lean` prove

```lean
Aris4Math.ThirtyFour.TwentyLow.propertyB_of_low_degree
  (H : Simple5Hypergraph (Fin 20))
  (cover : H.PairCovering) (edges34 : H.edges.card = 34)
  (small : ∃ x, H.degree x ≤ 6) : PropertyB H
```

All actual degree, codegree, multiplicity and probability assumptions are derived internally. The seventeen local configurations already pass with the ordinary total bad-link quota alone; their strict bounds are sometimes weaker than the paper's nested-quota numbers but remain <1. The Lean theorem does not claim the stronger numbers.

For a degree-five point, at least eighteen unit neighbors and the total degree budget force one of degree ≤8. For a degree-six point, a second degree-six/seven point supplies one of the full arbitrary-codegree cases. If no such point exists, the other nineteen degrees are at least eight; at least fourteen unit neighbors exist. If all unit neighbors had degree ≥9, the sum would be at least `6+14*9+5*8=172>170`. Hence an actual unit degree-eight partner exists. This gives a shorter direct derivation of the same final pair as the paper's degree-eight-set argument.

Executed `lake build Aris4Math.ThirtyFour.TwentyLowComplete`: 1002 jobs, exit 0 (`build-twenty-low-complete-r2.log`). The exact conditional theorem's transitive axioms are only the standard three. `TwentyLowAudit.lean` spells out the actual edge set, pair coverage, raw filtered-edge degree, and Bool coloring; `twenty-low-audit.log` records its successful separate import and identical axiom audit. Earlier failed development log is preserved separately.

The six-vertex-count RemainingGoal above remains the canonical overall reduction. This additional theorem closes its 20-point minimum-degree-five/six branches; it does not close minimum degree seven/eight or the entire 20-point case.

## Twenty vertices with at least three degree-seven points completed

`TwentySevenMany.propertyB_of_many_sevens` now proves the whole actual-input branch:

```lean
(H : Simple5Hypergraph (Fin 20)) (cover : H.PairCovering)
(edges34 : H.edges.card = 34) (minimum : ∀ x, 7 ≤ H.degree x)
(many : 3 ≤ (TwentySevenMany.sevens H).card) : PropertyB H
```

The accompanying `propertyB_of_four_sevens` only needs at least four degree-seven points, without a minimum-degree hypothesis. These are original coloring conclusions, not conditional numeric-profile results.

The proof first eliminates a unit seven-seven pair and a seven-seven/seven-eight pair of codegree at least four using nine actual pair profiles. If a seven-seven codegree is three, a third seven-point and a complete three-lock classification provide the coloring. Therefore all seven-seven codegrees may be assumed two. Four seven-points then fall into the complete 26-case four-lock table.

If exactly three seven-points exist, the total incidence budget forces an eight-point: otherwise the degree sum is at least `3*7+17*9=174>170`. Three-lock bounds force its three codegrees with the seven-points to agree and equal either one or two. The corresponding four-lock families have eleven and twenty-six high-trace inputs. Every input has a strict corrected probability bound.

`TwentySevenTriples.lean` checks 39 labelled profiles and their complete input domain (22 all-seven profiles and 17 mixed profiles), while `TwentySevenQuad.lean` checks 63 profiles. The latter proves every bounded actual high-trace vector satisfying the six actual pair inventories belongs to the list, then recovers **all sixteen actual multiplicities**. Per-center deletion uses either total or pure bad-pair quotas, not their sum. The apparent size of the finite table is not a hypergraph enumeration.

Executed builds:

```sh
lake build Aris4Math.ThirtyFour.TwentySevenTriples
lake build Aris4Math.ThirtyFour.TwentySevenQuad
lake build Aris4Math.ThirtyFour.TwentySevenMany
lake env lean ../context/propertyb34-hour1-20261013/nineteen/TwentySevenAudit.lean
```

The accepted logs are `build-twenty-seven-triples-r2.log` (1004 jobs), `build-twenty-seven-quad-r2.log` (1009 jobs), `build-twenty-seven-many.log` (1016 jobs), and `twenty-seven-audit.log`, all exit zero. The final two branch theorems and independent bare-edge-set original-coloring audit have only `propext`, `Classical.choice`, `Quot.sound`. Earlier unsuccessful generation/build logs remain historical and are not acceptance evidence.

The remaining 20-vertex cases are minimum degree seven with one or two seven-points, and minimum degree eight. The other vertex counts remain outside this local formal result. No T34 main theorem or new global lower bound has been claimed.

## Final first-hour assembly and precise remaining theorem

The current formal entry point is now `formal/Aris4Math/ThirtyFour/Assembly.lean`, whose

```lean
Aris4Math.ThirtyFour.Assembly.target_iff_remaining_goal :
  Aris4Math.Target34 ↔ Aris4Math.ThirtyFour.Assembly.RemainingGoal
```

incorporates all results above. Its remaining proposition consists of:

- On `Fin 20`, pair-covering H with exactly 34 edges whose minimum degree is seven and which has exactly one or two seven-degree vertices, **or** whose minimum degree is exactly eight.
- All pair-covering, exactly-34-edge H on `Fin v` for 21≤v≤25.

Here “minimum degree exactly eight” includes both the universal ≥8 condition and existence of a degree-eight point. “Minimum seven with one/two seven-points” similarly has the full ≥7 condition and the exact cardinality, hence no implicit missing existence assumption. The assembly derives all these conditions from the actual total incidence and previously completed branches.

`lake build Aris4Math.ThirtyFour.Assembly` completed 1032 jobs, exit zero (`build-assembly.log`). `AssemblyAudit.lean` separately imports the actual module and applies the conditional equivalence from a bare `[Finite V]`, a finite set of five-element edges, and at most 34 edges. Its remaining proposition is explicitly a premise. `assembly-audit.log` shows the actual definitions and transitive axioms, all only `propext`, `Classical.choice`, `Quot.sound`.

The general all-vertex T34 remains unproved. This partial assembly is useful because subsequent branch implementations can be connected directly to its precisely stated residual goal instead of reconstructing the already completed original-input route.

## Separate static review of the degree-eight candidate

At the parent's request, `EIGHT_STATIC_REVIEW.md` reviews Steps 2–7 of the new paper candidate. Within those graph and incidence arguments no mathematical error was found. `review_eight_residues.py` recomputes the stated common-trace and induced-graph consequences from the sixteen supplied residual representatives; `EIGHT_RESIDUE_REVIEW.json` reports PASS for exactly that scope. The complete local classification and probability witnesses were not re-executed by this review, and the degree-eight branch has not been proved in Lean. The review is same-family/provisional.

## Reproduction of the delivered partial formal chain

The entire new chain is imported by Assembly. From the project root:

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
cd formal
lake build Aris4Math.ThirtyFour.Assembly
lake env lean ../context/propertyb34-hour1-20261013/nineteen/AssemblyAudit.lean
lake env lean ../context/propertyb34-hour1-20261013/nineteen/Audit.lean
lake env lean ../context/propertyb34-hour1-20261013/nineteen/TwentyLowAudit.lean
lake env lean ../context/propertyb34-hour1-20261013/nineteen/TwentySevenAudit.lean
```

The delivered sources contain fifteen new modules, 1,731 lines (generated data vectors share source lines). All are part of the successfully built dependency chain. The new source directory contains no `sorry`, `native_decide`, or new `axiom` declaration. Standard project imports remain in the proof dependency, as reflected by the final transitive axiom audits. Old T32/T33 source and delivery artifacts were not edited.
