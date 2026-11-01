# Complete labelled mixed five-lock caller

Acceptance: the complete mixed five-lock branch is built and independently imported locally.
`lake build Aris4Math.ThirtyThree.TwentyFourMixed` completed successfully (1010 jobs);
`ImportAudit.lean` restates the original Bool-color count conclusion and passed.
Both final exports depend only on `propext`, `Classical.choice`, `Quot.sound`.
This is a completed 24-point branch, not a claim that the entire T33 theorem is finished.

## Mathematical scope

The target branch is `Fin 24`, exactly 33 edges, and point-pair coverage.
`TwentyFourSelection.MixedLocks H` provides five distinct actual vertices
labelled 0,1,2,3,4, of degrees 6,6,7,7,7, with every pair having codegree one.
For each low center, every actual bad edge pair has an edge avoiding all three
high vertices. The final wrapper also accepts the already-proved sufficient
condition that at least 18 vertices have degree seven.

No whole-hypergraph enumeration occurs. The only finite tables are the complete
local intersection types and rational positional certificates.

## Actual input chain

1. Unit codegrees imply that every positive large trace has multiplicity one,
   different large traces intersect in at most one label, and there are at most
   two. `FiveLockClassification` proves analytic completeness and then maps the
   actual trace family to one of all 32 labelled possibilities.
2. Total edge count, five actual degrees and ten actual codegrees determine all
   remaining type multiplicities through `MultiLockRecovery`. The exact
   recovered counts agree with the literal `counts` table by kernel computation.
3. Actual degree-six link counting supplies a real bad pair at each low center.
   `ActualBadSlot` proves its two traces have exactly the common low label,
   correct positive capacities, and the required avoidance. `slot_complete`
   covers every such trace pair, in either orientation, by an eight-slot list.
   Shorter lists repeat their first valid slot; this padding changes no coverage.
4. Both actual low slots are fixed before choosing lock positions. The total
   selection map chooses a row and one of 48 position/profile configurations.
   This preserves the adaptive logic of the saved witnesses without assuming
   independence between slot types and the later choice of positions.
5. `slot_weight_lower` charges both ordered directions of each actual chosen bad
   pair. At high centers, and in baseline rows at low centers, nonnegative dual
   multipliers combine the total-link quota and pure-edge quota. Their exact
   deficit penalty is checked against all ordered type capacities; this is the
   actual avoided-edge theorem of `RefinedDeletion`, not an assumed numeric loss.
6. `CustomDeletion` applies the proved actual losses to the same realized profile.
   Its strict sum of min(A,B,C-loss) gives an actual Property B coloring.

## Data and exact arithmetic

Source: `context/propertyb33/round01/small-math/V24_SMALL_R_CERTIFICATES.json`.
Generator: `computations/propertyb33/round02/generate_v24_mixed.py`.
Expanded evidence: `LABELLED_CERTIFICATES.json` in this directory.

The generator explicitly transports saved representatives to all 32 labelled
families. Lean checks every labelled case directly, so no unproved claim that a
color-preserving permutation preserves the certificate is needed. There are 48
unique positional profiles and 210 unique loss rows. The selection map covers all
32*8*8 = 2048 padded pairs of low slots. Python Fraction replay exactly reproduces
all saved selected bounds, with largest bound 75421/75582. The generator's output
is subsequently treated as untrusted data by the Lean kernel.

`TwentyFourMixedFacts.lean` verifies count recovery, complete slot coverage,
profile identity and validity. `TwentyFourMixedNumeric.lean` independently checks
all 48*24 A/B/C triples, all five duals per profile, each selection-map loss
relation and each strict final inequality. The finite computations use
`decide +kernel`; no native decision procedure is trusted.

## Exported interfaces

`TwentyFourMixed.propertyB_of_structured_locks` takes actual degrees, unit
codegrees and actual low-pair avoidance. `propertyB_of_mixed_locks` consumes the
selection module's existing structure. `propertyB_of_many_sevens` takes H,
point-pair coverage, exactly 33 edges and at least 18 degree-seven vertices.
No certificate, type profile, bad-slot count or probability assumption remains in either wrapper.

## Reproduction

From `formal/`, with project `.tools/elan` configured as `ELAN_HOME`:

```
lake build Aris4Math.ThirtyThree.TwentyFourMixed
lake env lean ../context/propertyb33/round02/mixed/ImportAudit.lean
```

The exact build/audit results are saved in `final-build.log` and `import-audit.log`, both exit 0.
The direct final check is `mixed-third.log`, also exit 0. The same-family
implementation and local import do not constitute independent human or cross-family review.
