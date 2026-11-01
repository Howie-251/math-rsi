# B.4 exact maximum accepted integer budget

Source: `formal/Aris4Math/General/Growth/Budget.lean`.
Target: `proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md`, Definition B.1 and
Lemma B.4. Imports `Seed` and `ParameterControl`; no shared module was edited.

The total noncomputable function is exactly:

```lean
rsBudget k := ((Finset.range (k*2^k)).filter (RSAccepts k)).sup id
```

For `k≥17`, `rsaAccepts_lt` proves every actual accepted integer is below the
finite cutoff. Below `2^k`, this follows from `k≥1`; at or above the seed, the
actual accepted parameter and B.1 give `M/2^(k-1)<2k`. Thus the filter includes
all accepted positive integers; its cutoff is a proved consequence rather than
an external assumption. `seed_rsAccepts` makes this finite set nonempty, so its
supremum is attained by an accepted integer.

Exports:

- `rsaAccepts_lt hk hA : M < k*2^k`.
- `le_rsBudget_of_accepts hk hA : M ≤ rsBudget k`.
- `seed_le_rsBudget hk : 2^k ≤ rsBudget k`.
- `rsBudget_accepts hk : RSAccepts k (rsBudget k)`.
- `rsBudget_lt hk : rsBudget k < k*2^k`.
- `rsBudget_characterization hk`: the budget is accepted and every accepted
  integer is at most the budget.
- `rsBudget_parameter hk`: an actual parameter `p>0`, `p≤1`, satisfying
  `AcceptedAt k (rsBudget k) p`.

Verification from `formal/`:

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
lake env lean Aris4Math/General/Growth/Budget.lean -o .lake/build/lib/lean/Aris4Math/General/Growth/Budget.olean
lake env lean ../context/propertyb-general-lean-growth/budget/Audit.lean
```

Both commands exited 0; `compile.log` has no diagnostics. The independent import
prints the budget definition, checks the exported maximum characterization, and
calls the result with the precise acceptance formulas expanded. It establishes
the seed lower bound, strict upper bound, positive actual parameter, and
maximality against arbitrary accepted positive integers without supplying a
finite cutoff. `audit.log` records all seven declarations' transitive axioms:
only `propext`, `Classical.choice`, and `Quot.sound`. No `sorry`, added axiom,
or `native_decide` is used. No remaining local obligation. Cross-family review
and root's final regular build are outside this worker's verification scope.
