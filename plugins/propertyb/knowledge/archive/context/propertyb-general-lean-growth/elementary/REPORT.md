# Elementary growth inputs

Completed module: `formal/Aris4Math/General/Growth/Elementary.lean`.

The argument is restricted to the required natural-number range. `pow_two_ge_fourth` proves `k^4 ≤ 2^k` for every natural `k ≥ 16`, by induction from the equality at 16. Its step is the polynomial inequality `(k+1)^4 ≤ 2*k^4`; after substituting `k=16+t` every coefficient in the difference is positive. This is checked by Lean arithmetic, without an external certificate.

For `k ≥ 17` and `2^k ≤ M`, the module proves:

- `sqrt_ge_square`: `k² ≤ sqrt M`.
- `sqrt_gt_eight`: `8 < sqrt M`.
- `gain_denominator_pos`: `0 < 8(1+log k)` (this only needs `k ≥ 17`).
- `gain_denominator_le_sqrt`: `8(1+log k) ≤ sqrt M`, using `log k ≤ k−1`.
- `integerGain_pos`: `1 ≤ integerGain k M`.
- `integerGain_le_quotient`: the natural floor is at most `sqrt M/[8(1+log k)]`; only `k ≥ 17` is needed.
- `integerGain_le_budget`: `integerGain k M ≤ M`.
- `budget_add_integerGain_le_twice`: `M + integerGain k M ≤ 2M`.
- `integerGain_bounds`: the last four conclusions bundled as a conjunction.

The optional structural interface is also complete:

```lean
cliqueBudget_le_twice_sqrt
  (hk : 17 ≤ k) (hM : 2 ^ k ≤ M) (hN : N ≤ 2 * M)
  (hn : n * (n - 1) ≤ k * (k - 1) * N) :
  (cliqueBudget k n : ℝ) ≤ 2 * Real.sqrt (M : ℝ)
```

The first branch of `cliqueBudget` is at most `k²`. For the second, the hypotheses give `(n−1)² ≤ 2k(k−1)M ≤ 4(k−1)²M`; square-root monotonicity and `Nat.cast_div_le` then bound the natural quotient. All natural subtractions and positive-denominator conditions are discharged internally, including `n=0`.

Executed verification:

1. Direct compilation to this module's `.olean`: exit 0.
2. Independent import `ActualCaller.lean`: exit 0. It tests the original boundary `k=17`, `M=131072`, and the separate nontrivial vertex-budget input `n=1000`, `N=131073`.
3. Thirteen printed transitive-axiom lists, including both callers, contain only `propext`, `Classical.choice`, and `Quot.sound`; see `actual-caller.log`.

Reproduction from `formal/`, after root-managed dependencies:

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
lake env lean Aris4Math/General/Growth/Elementary.lean -o .lake/build/lib/lean/Aris4Math/General/Growth/Elementary.olean
lake env lean ../context/propertyb-general-lean-growth/elementary/ActualCaller.lean
```

This is local incremental verification, not external-machine reproduction. No stronger real-variable B.2 estimate, Gram improvement, review acceptance, or final main theorem is claimed by this module.
