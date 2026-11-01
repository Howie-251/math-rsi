# 23 vertices with exactly three degree-six vertices

Final state (2026-10-13): the complete original branch theorem, normal Lake
build and separate post-build import audit all passed. The theorem has exactly
the original branch hypotheses and only `propext`, `Classical.choice`,
`Quot.sound` as transitive axioms. No profile, catalogue, quota, probability
or certificate premise remains. All required normal Lake traces are present;
no process is still running or suspended for this branch.

The verified final declaration is:

```lean
Aris4Math.ThirtyThree.TwentyThreeThreeLowComplete.propertyB_of_three_sixes
  (H : Simple5Hypergraph (Fin 23))
  (cover : H.PairCovering) (edges33 : H.edges.card = 33)
  (count3 : H.sixVertices.card = 3) : PropertyB H
```

## Mathematical route

Actual selection chooses low locks 0,1,2 of degree six and high locks 3,4 of
degree seven. Each of the six low-high pairs has codegree one. Write the low
pair codegrees as `1 + e01`, `1 + e02`, `1 + e12`. Each excess is at most two,
and the sum of either two excesses is at most two, because the total excess
incident to a degree-six vertex is at most two. Thus the labelled excess
triple lies in an explicitly checked list of eleven possibilities.

If the high pair 34 has codegree at least four, the existing high-pair theorem
applies. Otherwise its codegree b is between one and three.

Every large trace except 012 contains a unit low-high pair; its multiplicity
is therefore at most one. The trace 012 has multiplicity at most two: it is
bounded by each relevant low-pair codegree, and the two corresponding excesses
sum to at most two. This exceptional multiplicity must not be collapsed to a
Boolean value.

The full raw high domain is consequently `3 × 2^15`. The ten pair-budget
constraints at maximum low/high budgets leave 131 labelled high configurations.
`TwentyThreeThreeLowHighCatalog.covers` checks coverage of the full raw domain
and passed with the standard three transitive axioms.

For the actual eleven low-excess triples and b in 1..3, there are 1796
admissible labelled inputs. The catalogue maps all of them to 372
representatives using explicit permutations of the three low locks and two
high locks. Restricting first to the five canonical low-excess triples leaves
844 inputs, grouped as 116 + 145 + 151 + 180 + 252; 844 is not the full
labelled eleven-budget domain. The independent count replay is saved in
`LABELED_DOMAIN_COUNTS.json`. Its permutation direction is representative
labels to actual labels. The exact intended conclusion records preservation of
the degree data, transported pair codegrees and every large-trace multiplicity.
That finite map passed direct kernel verification; its `classify` theorem
has only the standard three transitive axioms.

After relabeling, the actual multiplicities of all 32 traces are recovered from
total edge count 33, the five degrees, ten pair codegrees and large traces.
The finite recovered formulas and actual-H recovery interface have been checked.
Each center has at most two nonzero avoided-lock quota multipliers. The actual
bad-pair deduction supplies the loss, and the final sum of the minima of the
ABC upper bounds is strictly below one. The largest exact result among all
372 representatives is `43753/43758`.

The data reproduce the round01 `THREE_LOW_TWO_HIGH_V23.json` family; no new
restriction on the original hypergraph was added. Raw data alone do not prove
coverage, which is why the separate catalogue and input-recovery connections
are required.

## Evidence and reproducibility

Data, HighCatalog, Facts, ABC, Dual, Numeric and the actual probability wrapper
have normal Lake build logs in this directory. In particular:

- `TwentyThreeThreeLowABC-build.log`: exact ABC values, standard three axioms.
- `TwentyThreeThreeLowDual-build.log`: full nonnegative dual obligations and quotas.
- `TwentyThreeThreeLowFacts-build.log`: recovered profile, validity and counts.
- `numeric-build.log`: exact strict bound, standard three axioms, exit 0.
- `wrapper-build.log`: `propertyB_of_counts`, standard three axioms, exit 0.
- `high-build.log`: full high-domain coverage, standard three axioms, exit 0.
- `catalog-first.log`: complete representative map, standard three axioms, exit 0.
- `complete-first.log`: complete original branch, standard three axioms, exit 0.
- `import-audit.log`: separate import, exact original branch type, standard three axioms, exit 0.
- `final-build.log`: final normal managed build, 1020 jobs, exit 0.
- `import-audit-final.log`: separate post-build import, exact branch type and standard three axioms, exit 0.

Use the project toolchain:

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
cd /Users/rfy_naiveai/Desktop/aris4math/formal
lake build Aris4Math.ThirtyThree.TwentyThreeThreeLowComplete
lake env lean ../context/propertyb33/round02/twentythree-three-low/ImportAudit.lean
```

Both final commands ran and returned exit 0. The normal build included the
catalogue (1081 seconds) and Complete (2.9 seconds); the independent import
audit was repeated after that managed build. The earlier successful direct
checks remain in their own logs. No concurrent duplicate was started and no
trace was fabricated.

The root agent coordinates global assembly and all cross-model review. No new
external-model call was made by this worker. This result closes exactly the
three-degree-six branch at 23 vertices; the whole T33 theorem is assembled and
audited separately by the root team.
