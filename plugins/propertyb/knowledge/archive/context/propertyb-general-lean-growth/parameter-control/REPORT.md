# B.1 accepted-parameter control

Source: `formal/Aris4Math/General/Growth/ParameterControl.lean`.
Mathematical target: `proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md`, Lemma B.1.

The exported theorem is:

```lean
acceptedAt_parameter_control {k M : ℕ} {p : ℝ}
  (hk : 17 ≤ k) (hM : 2^k ≤ M) (hAcc : AcceptedAt k M p) :
  1/(k:ℝ)^2 < p ∧
  1/(2*(k:ℝ)^2) ≤ jk k p ∧
  (M:ℝ)/(2:ℝ)^(k-1) < 2*(k:ℝ) ∧
  -2*Real.log (k:ℝ) < ((M:ℝ)/(2:ℝ)^(k-1))*Real.log (ak k p)
```

The proof uses the actual `AcceptedAt` inequality. Put `d=2^(k-1)` and `t=M/d`.
From `M≥2^k`, it derives `t≥2`, `M≥2`, and
`t²/2 ≤ M(M-1)/d²`. Bernoulli gives the reusable helper `ak_le_mul`.

For `0≤y≤1/k²`, `rs_integrand_ge_half` proves the integrand is at least `1/2`.
`jk_lower_small` integrates this estimate. `jk_mono_unit` connects the short
integration interval to the actual parameter `p`.

If `p≤1/k²`, then `t≥2` and `0≤a≤1` imply
`a^t≤a²≤(kp)²≤p`, whereas the actual left side is at least `2J≥p`.
This contradicts strict acceptance, including when `p=0`. It avoids exponent
`t-1` entirely. Hence `p>1/k²`, and integrating over `[0,1/k²]` yields
`J≥1/(2k²)`. Acceptance now gives `a^t>t²/(4k²)≥1/k²`.
Since `a^t≤1`, this also yields `t<2k`. Positivity of `a` is derived from
`p>0`; applying the logarithm gives the final inequality.

Verification from `formal/`:

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
lake env lean Aris4Math/General/Growth/ParameterControl.lean -o .lake/build/lib/lean/Aris4Math/General/Growth/ParameterControl.olean
lake env lean ../context/propertyb-general-lean-growth/parameter-control/Audit.lean
```

Both final commands exited 0. `compile.log` contains no diagnostics.
`Audit.lean` independently imports the compiled module, checks the exported type,
checks transitive axioms of all five declarations, and supplies an actual caller
with `AcceptedAt` and `ak` expanded to their raw formulas. All five declarations
use only `propext`, `Classical.choice`, `Quot.sound`. No `sorry`, additional
axiom, or `native_decide` is present. This worker did not perform cross-family
review or another-machine reproduction. There is no remaining local B.1
mathematical or Lean obligation.
