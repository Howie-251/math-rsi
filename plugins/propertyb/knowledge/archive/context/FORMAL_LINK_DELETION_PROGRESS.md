# Actual link deletion: Lean status

`formal/Aris4Math/LinkDeletion.lean` is frozen and compiled on 2026-10-06 (Lean 4.24.0, pinned Mathlib). The build and eleven explicit axiom audits succeeded; all audited theorems use only `propext`, `Classical.choice`, and `Quot.sound`. No `sorry`, new axiom, or `native_decide` is used.

## Established statements

- `directedBadPairs H x` is the disjoint union of the two ordered directions of each actual unordered `H.badLinkPairs x`.
- `directed_bad_card` proves exactly twice the unordered count. `directed_bad_subset` places these directions in the actual edge `offDiag`; `directed_bad_intersection` proves every direction has intersection cardinality different from one.
- `unorderedWeight_pair` gives the sum of the forward and reverse weights, without assuming symmetry.
- `uniform_bad_weight_lower` and `covering_bad_weight_lower` turn a genuine bad-pair count, including P8, into a weighted deletion.
- `exceptional_bad_weight_lower` permits an explicitly bounded family of zero-weight exceptions. `two_exceptional_edges_weight_lower` proves that at most two exceptional actual edges cost at most one unordered slot.
- `critical_sum_le_link_deletion` applies this actual deletion to the true locked-permutation probability sum through `ConditionalUnion`.

## Choice of the finite argument

The application needs the uniform lower bounds in P9 and exactly one exceptional slot for the final center in the 23-point three-lock branch. These statements suffice directly; a general theorem about sorting arbitrary `Numeric.linkSlots` is not a dependency of the chosen proof. The finite type weight certificates will establish the closed deductions used by `Numeric`, using the direct P9 argument rather than an unnecessary general optimization theorem.

## Next interface

`LinkWeightCertificates.lean` is being developed separately: finite table type comparisons and actual `TableRealization` will discharge the incident-edge weight hypotheses. This module does not itself prove those profile-specific inequalities or the original theorem.

Evidence: `.aris/traces/proof-checker/2026-10-06_run08/lean-link-deletion-build.log` and matching metadata.
