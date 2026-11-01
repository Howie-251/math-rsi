# Complete 25-point branch for T33

`Aris4Math.ThirtyThree.twenty_five_propertyB` proves Property B for every simple
5-uniform hypergraph on `Fin 25` with exactly 33 edges and pair coverage. There
are no extra lock-set, classification, profile, degree or probability premises.

The actual input chain is:

1. `TwentyFiveStructure.exists_six_large_or_eight_triples` derives at least ten
   degree-six vertices and chooses either six locks with a block of size at
   least four, or eight locks whose triple family has at least five members and
   covers every lock.
2. The six-lock branch uses the existing analytic six-point classification.
   The large-block hypothesis forces indices 6,7,8, whose 33-edge profiles are
   built by increasing only the empty-trace count.
3. The eight-lock branch calls the complete `classify_eight` through
   `EightTraceClassification.exists_full_labeled_eight`. The relabeling acts on
   the actual input vertices, and all uncovered two-point blocks are recovered.
4. `TraceProfileBridge.realizes_of_recovered_counts` binds every actual edge
   fiber to the numeric table. The edge total is 33 throughout. Its row-sort
   equality follows from computable nodup/order certificates.
5. `SixLargeProfiles` checks all three strict bounds. `EightProfiles` checks all
   fourteen strict bounds and all 14×256 abstract label-subset counts. These are
   kernel calculations on fixed local tables and exact rational formulas.
6. `ProfileApplication.propertyB_of_uncorrected_profile` supplies the actual
   coloring existence theorem, and `TwentyFive.lean` joins both branches.

Validation: `lake build Aris4Math.ThirtyThree.TwentyFive` exited 0. The split
fourteen-case `EightProfiles` compilation took 245 seconds and the final
`TwentyFive` assembly 1.4 seconds. The final theorem and its numeric dependencies
report only `propext`, `Classical.choice`, and `Quot.sound`. `ImportAudit.lean`
independently imports the built module, checks the literal intended 25-point
statement, and audits the final theorem and both numeric-count/strict families.
See `build.log` and `import-audit.log`.

The earlier monolithic forall computation was stopped after 607 seconds because
of observed memory pressure (32 GB machine, roughly 15 GB compressed memory,
falling CPU throughput). `build-monolithic.log` preserves that termination; it
was a resource-management stop, not a failed mathematical certificate. The
successful proof uses `fin_cases` to check the same fourteen representatives
separately. The original initial `eight-build.log` was interrupted after a row
sorting computability issue was identified in the parallel six-lock check;
`RowCertificate` fixes the issue without altering the mathematical tables.

The full arbitrary-vertex T33 is not asserted here. The actual remaining
finite branches after the separately completed 19,20,21,25 cases are 22–24.
