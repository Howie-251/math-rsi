# Numerical RS pilot at k=17 and p=1/17

Module: `formal/Aris4Math/General/RS/PilotEstimates.lean`.
Namespace: `Aris4Math.General.RS`.

* `pilot_ak_gt_half` proves `1/2 < ak 17 (1/17)` by exact rational arithmetic.
* `pilot_jk_le` proves `jk 17 (1/17) ≤ 1/17` using the checked integral bound.
* `pilot_estimate_sq m γ hm hγ` proves the desired strict RS bound assuming
  only `m≤2^17` and the stronger allowance `γ≤m²`.
* `pilot_estimate` accepts the standard bound `γ≤m(m−1)`.
* `gamma_le_edges_sq` applies the finite-filter cardinal bound to the actual
  original edge pair set; it has no structural assumption.
* `pilot_estimate_actual E hm` supplies the numerical strict RS bound directly
  for the actual `E.card` and `gamma E`. It includes an empty edge family and
  needs no separate probability or gamma-bound premise.

For the proof, the exponent m/2^16 is at most 2. Since 1/2<a≤1, the a-power
term is at least a²>1/4. The directed-pair coefficient is at most 4, so its
integral term is at most 4/17<1/4. Thus the combined failure bound is strictly
below one. There is no exhaustive search over hypergraphs or initial colorings.

Final build `build03.log` and independent import audit `audit.log` both exited 0,
with no diagnostics in the build. The audit restates the actual-E caller; both
`pilot_estimate_actual` and `pilot_estimate` depend only on `propext`,
`Classical.choice`, and `Quot.sound`.
Reproduce from `formal/` with the project-local Lean toolchain:

```
lake env lean -o .lake/build/lib/lean/Aris4Math/General/RS/PilotEstimates.olean Aris4Math/General/RS/PilotEstimates.lean
lake env lean ../context/propertyb-general-lean-pilot/pilot-estimates/Audit.lean
```

This module establishes the numerical input to the RS criterion. It does not
supply the independent algorithmic RS probability theorem or itself produce the
actual final coloring; those remain obligations of the main pilot assembly.
