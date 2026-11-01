# 23 vertices with exactly two degree-six vertices

The complete branch is kernel checked. Its final declaration is:

```lean
Aris4Math.ThirtyThree.TwentyThreeTwoLowComplete.propertyB_of_two_sixes
  (H : Simple5Hypergraph (Fin 23))
  (cover : H.PairCovering) (edges33 : H.edges.card = 33)
  (count2 : H.sixVertices.card = 2) : PropertyB H
```

The final theorem has no profile, numerical bound, dual certificate, type
catalogue, or choice of locks as an extra premise. The independent import audit
checks this exact type and prints its transitive axioms: `propext`,
`Classical.choice`, and `Quot.sound` only.

## Mathematical connection

Actual structural selection gives two degree-six and three degree-seven locks,
with every pair having codegree one except possibly the low pair 01 and high
pair 23. If the latter codegree is at least four, the existing high-pair branch
applies. Otherwise both exceptional codegrees lie between one and three.

Any trace on at least three locks contains a unit-codegree pair, so its
multiplicity is at most one. The complete 16-Boolean high-trace domain is
classified by the two exceptional pair budgets. The maximum budgets admit 55
labelled high configurations; the nine actual budget choices have 412
admissible labelled inputs. A checked finite map sends each to one of 208
representatives through a permutation preserving the two low locks and three
high locks. Permutations map representative labels to actual labels.

The proof transports actual traces along that permutation, recovers every
low-order multiplicity from the total edge count, degrees and codegrees, and
uses the actual recovered profile. For each center, at most two avoided-lock
quotas feed the already proved real bad-pair deduction. Nonnegative dual
multipliers, capacities, penalties, all ABC values and the final minimum bound
are checked exactly in Lean. The largest final bound is `7292/7293 < 1`.
This establishes the original coloring conclusion for the entire branch.

The 208 data rows reuse 204 original baseline successes and four refined
replacements (groups 56, 57, 58, 64). The generator independently recomputed
all records; Python results supply data, while coverage, input binding and
inequalities are proved by Lean.

## Executed verification

All commands used project Lean 4.24 with:

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
cd /Users/rfy_naiveai/Desktop/aris4math/formal
```

Direct `lake env lean -o ...` checks succeeded for Data, Facts, Catalog,
Numeric, the actual probability wrapper and Complete. The shared HighCatalog
also completed a normal Lake build. Final executed commands:

```sh
lake env lean -o .lake/build/lib/lean/Aris4Math/ThirtyThree/TwentyThreeTwoLowNumeric.olean Aris4Math/ThirtyThree/TwentyThreeTwoLowNumeric.lean
lake env lean -o .lake/build/lib/lean/Aris4Math/ThirtyThree/TwentyThreeTwoLow.olean Aris4Math/ThirtyThree/TwentyThreeTwoLow.lean
lake env lean -o .lake/build/lib/lean/Aris4Math/ThirtyThree/TwentyThreeTwoLowComplete.olean Aris4Math/ThirtyThree/TwentyThreeTwoLowComplete.lean
lake env lean ../context/propertyb33/round02/twentythree-two-low/ImportAudit.lean
```

All four returned exit 0. See `numeric-first.log`, `wrapper-first.log`,
`complete-first.log`, and `import-audit.log`. The final audit was performed in
a separate Lean process importing the produced Complete module.

The normal managed build of the final chain subsequently passed as well:
`lake build Aris4Math.ThirtyThree.TwentyThreeTwoLowComplete` returned exit 0
(1018 jobs). A second independent import audit after that build also returned
exit 0 with the exact same original branch type and standard three axioms.
See `final-build.log` and `import-audit-final.log`. Every required module now
has a normal Lake trace; no trace was manufactured or copied from a direct
check. Earlier scratch probes remain only as development evidence.

## Scope

This proves exactly the two-degree-six branch at 23 vertices. It does not by
itself close all 23-vertex cases or T33. Cross-model review is coordinated by
the root agent; no new Grok/Gemini review was called by this worker.
