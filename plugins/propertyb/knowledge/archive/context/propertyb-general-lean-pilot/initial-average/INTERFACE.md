# Actual initial-color mean and residual probability

Source: `formal/Aris4Math/General/RS/InitialAverage.lean`.
Namespace: `Aris4Math.General.RS`.

The module defines `monoCount E c` as the number of actual edges of E that are
monochromatic under the initial coloring c. It proves the following complete
interfaces for every finite vertex type, with no overlap/degree restrictions:

* `initial_monoCount_average E k hk hE` gives
  `bernoulliExpect (1/2) (fun c => (monoCount E c : ℝ)) = (E.card : ℝ)/2^(k-1)`.
  The hypotheses are `hk : 1 ≤ k` and `hE : Uniform E k`.
* `initial_power_average E k hk hE ha` gives
  `a^((E.card : ℝ)/2^(k-1)) ≤ bernoulliExpect (1/2) (fun c => a^(monoCount E c : ℝ))`
  for any real `a>0`. No `a≤1` premise is needed for Jensen.
* `initial_residual_conditional E k hE hp hp1 c` gives the fixed-c eligibility
  bound by `1-(ak k p)^(monoCount E c)`.
* `initial_residual_average E k hk hE hp hp1` averages the actual residual event
  over initial colors, giving `≤1-(ak k p)^((E.card : ℝ)/2^(k-1))` for `0<p≤1`.

The residual event is written as
`∃ e ∈ E, (∃ q : Bool, Mono e c q) ∧ ∀ x ∈ e, b x = false`.
It is exactly `Algorithm.lean`'s `ResidualEvent E c` on `Fin n`; the independent
`Audit.lean` contains this actual caller without any event-probability premise.

The mean uses coordinate product factorization to prove the probability of
one prescribed initial color on an actual edge. The two colors are disjoint
because k≥1 ensures the edge is nonempty. Linearity then gives the exact mean.
Finite Jensen applies the existing convexity of exp to X log a and the already
normalized nonnegative Bernoulli weights. The conditional residual estimate uses
Harris on the actual family of initially monochromatic edges; it never assumes
independence between overlapping edges.

Final source build: `build05.log` (exit 0, no diagnostics), producing
`.lake/build/lib/lean/Aris4Math/General/RS/InitialAverage.olean`.
Independent import/type/axiom audit and actual `ResidualEvent` caller:
`Audit.lean` / `audit.log` (exit 0). All four exported target lemmas use
only `propext`, `Classical.choice`, and `Quot.sound`. The independent actual
`Algorithm.ResidualEvent` caller compiled without additional premises.

Reproduce from `formal/` using the project's local toolchain:

```
lake env lean -o .lake/build/lib/lean/Aris4Math/General/RS/InitialAverage.olean Aris4Math/General/RS/InitialAverage.lean
lake env lean ../context/propertyb-general-lean-pilot/initial-average/Audit.lean
```

This closes the first summand of the RS failure bound. The single-intersection
witness probability and the final weighted union bound remain separate main-chain
obligations; this module does not claim the complete RS theorem.
