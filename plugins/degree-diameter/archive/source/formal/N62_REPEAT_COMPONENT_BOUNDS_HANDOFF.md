# Actual order-62 repeat-component bounds

Target: the actual support components of `defectMatrix G` for an arbitrary finite original simple graph `G`, assuming `degreeAtMostEight G`, `diameterAtMostTwo G`, and `Fintype.card V = 62`.

Source: `DegreeDiameter/N62RepeatComponentBounds.lean`, importing the existing actual-component quotient construction. No supplied component, equitable-matrix, parity, or counting certificate is a hypothesis.

Completed exports:

- `n62_repeat_component_defect_row`: the actual defect row restricted to its actual component sums to 3.
- `n62_repeat_component_size_even`: every actual component has even cardinality.
- `n62_repeat_component_size_ge_four`: every actual component has at least 4 vertices under the explicit additional premise `∀ x y, defectMatrix G x y ≤ 2`.
- `n62_repeat_quotient_reverse_positive`: positive actual quotient entries have positive reverse entries.
- `n62_repeat_quotient_budget_term_nonnegative`: each `R_CD * (R_DC - 1)` is nonnegative.
- `n62_repeat_quotient_budget`: `∑ D, R_CD * (R_DC - 1) = size(C) + 2 - R_CC`.
- `n62_repeat_component_size_ge_internal_square_sub_two`: `R_CC ^ 2 - 2 ≤ size(C)` over integers.

Proof connections: restricted rows come from the proved actual component indicators. Symmetry and zero diagonal pair the weighted square `C × C` under endpoint swap in `ZMod 2`; its total is `3 * size(C)`, so size is even. Positive size and evenness reduce size below 4 to exactly 2, contradicting row sum 3 and the explicit bound 2. Actual quotient balance and positive actual sizes imply reverse positivity; the diagonal of the proved quadratic identity minus row sum 8 gives the exact budget, and the diagonal summand gives the square bound.

Executed targeted build:

```bash
cd formal
source ../.tools/lean-env.sh
export LEAN_NUM_THREADS=3 RAYON_NUM_THREADS=3
lake build DegreeDiameter.N62RepeatComponentBounds
lake env lean ReviewN62RepeatComponentBounds.lean
```

Build exit 0: `logs/n62-repeat-component-bounds-second.log`. The sole warning is an unused `Fintype V` section variable in the private generic weighted-symmetry lemma. The first build log preserves the three repaired API/simplification errors; it is not a success record.

Dedicated original-input callers and printed public types/transitive axioms are in `ReviewN62RepeatComponentBounds.lean`; execution evidence is `logs/n62-repeat-component-bounds-type-axiom-audit.log` (exit 0). All seven exported theorems use only `[propext, Classical.choice, Quot.sound]`; all three actual original-input example callers compile.

Scope: no spectral trace 17, component classification, connectedness conclusion, enumeration, or unconditional order-62 exclusion is asserted. No `B ≤ 2` premise is used by evenness or the budget. No shared entrypoint, STATUS, existing component/quotient modules, or order-63–65 files were edited. Parent owns integration and cross-family review.
