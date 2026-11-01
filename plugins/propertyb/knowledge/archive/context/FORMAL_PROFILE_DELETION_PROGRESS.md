# All-position deletion family

`formal/Aris4Math/ProfileDeletion.lean` is frozen and successfully built on 2026-10-06. The four explicit axiom audits report only `propext`, `Classical.choice`, and `Quot.sound`.

`correctionDeleted H vertices positions p k` is the actual ordered bad-link pair set of the unique locked vertex at a correction position, and is empty away from correction positions. The definition uses a finite union; injectivity of the position embedding proves the unique-center equality.

- `correctionDeleted_subset`: every selected ordered pair is in the actual `H.edges.offDiag`.
- `correctionDeleted_bad`: each selected pair has nonsingleton intersection, hence zero actual critical probability by `CriticalCounting`.
- `correction_is_locked`: the actual `RealizesProfile` and profile validity ensure that every listed correction center is a real lock.
- `all_position_deletion_lower`: given the local actual deletion inequality at each correction lock, derives the exact all-position `Numeric.deduction` lower bound required by `ConditionalUnion.propertyB_of_weighted_position_bounds`.

The argument does not assume that a symbolic slot corresponds to an actual edge pair. Its deletion set is constructed directly from the actual hypergraph. Profile-specific local inequalities are supplied by the eight theorems in `LinkWeightCertificates.lean`; endpoint and pair probability aggregation remains in `ProfileApplication.lean`.

Evidence: `.aris/traces/proof-checker/2026-10-06_run08/lean-profile-deletion-build.log` and matching metadata.
