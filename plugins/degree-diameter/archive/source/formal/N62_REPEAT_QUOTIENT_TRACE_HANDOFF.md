# Actual order-62 quotient trace identity

Original target: from a finite original simple graph `G` with degree at most 8, diameter at most 2, and order exactly 62, derive `c + 2 * trace R = 17` and oddness of `c`, where `c` counts the actual positive-defect support components and `R` is their constructed original-adjacency quotient.

Source: `DegreeDiameter/N62RepeatQuotientTrace.lean`. The actual objects and their construction are inherited unchanged from `N62RepeatQuotient`. No `B ≤ 2`, supplied equitable quotient, dimension formula, trace equality, or spectral certificate is assumed.

Proof route: use the actual size matrix `N_CD = |D|`, with `N² = 62N`, `RN = NR = 8N`, and `R² + R = 10I + N`. Put `S = 2R + I` and `P = 62S - 17N`. Then `P³ = 157604P`, where `157604 = 41 * 62²`, and `trace P = 62(c + 2 trace R - 17)`. In `ZMod 1063`, the exact kernel-checked value `157604^531 = -1`, together with the finite-field matrix trace formula, forces `trace P = 0`. Hence 1063 divides `c + 2 trace R - 17`. Actual component nonemptiness gives `c ≤ 62`; actual nonnegative quotient rows of sum 8 give `0 ≤ trace R ≤ 8c`. The divisible integer lies between -17 and 1037 and therefore vanishes. Oddness follows from the integer identity.

This replaces the longer proposed rational invariant-subspace implementation with a direct finite-field trace argument. It is symbolic in the arbitrary original graph and uses only fixed numerical modular arithmetic; no graph enumeration or external certificate is used.

Public interfaces:

- `cubic_157604_trace_mod_1063`: generic integer-matrix cubic identity implies trace divisibility.
- `n62_repeat_size_matrix_square` and `n62_repeat_quotient_size_actions`: actual size-matrix algebra.
- `centeredRepeatQuotient`, `n62_centered_repeat_quotient_cubic`: actual construction and derived cubic.
- `n62_repeat_quotient_trace_bounds`, `n62_repeat_component_count_le`: actual bounds.
- `n62_repeat_quotient_trace_identity`, `n62_repeat_component_count_odd`: original-input conclusions.

Reproduction commands:

```bash
cd formal
source ../.tools/lean-env.sh
export LEAN_NUM_THREADS=3 RAYON_NUM_THREADS=3
lake build DegreeDiameter.N62RepeatQuotientTrace
lake env lean ReviewN62RepeatQuotientTrace.lean
```

Dedicated audit: `ReviewN62RepeatQuotientTrace.lean`, with actual original-input callers for both final conclusions. Targeted build exit 0 without warnings: `logs/n62-repeat-quotient-trace-third.log` (Lean reports 16s). Dedicated audit exit 0: `logs/n62-repeat-quotient-trace-type-axiom-audit.log`. All eight public theorems depend only on `[propext, Classical.choice, Quot.sound]`; both original-input example callers compile. The first two build logs preserve repaired elaboration/interface errors and are not success records.

Scope: no claim of connectedness, component classification, or order-62 exclusion. Existing modules, shared entrypoints/STATUS, and order-63–65 files are unchanged. Parent owns shared integration and cross-family source review.
