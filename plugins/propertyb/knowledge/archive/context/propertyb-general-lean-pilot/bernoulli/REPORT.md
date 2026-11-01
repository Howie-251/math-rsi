# Bernoulli product probability and weighted Harris

Source: `formal/Aris4Math/General/RS/Bernoulli.lean`.
Namespace: `Aris4Math.General.RS`.

The module proves finite product Bernoulli association for arbitrary real `p∈[0,1]` and arbitrary finite coordinate type `V`. It does not assume independence of edge-hit events. The induction removes one coordinate through `Option V`; the final step is the nonnegative two-point covariance `p(1-p)(F₁-F₀)(G₁-G₀)`.

## Stable definitions

- `bitWeight p b = if b then p else 1-p`.
- `bernoulliWeight p b = ∏ v, bitWeight p (b v)`.
- `bernoulliExpect p f = ∑ b, bernoulliWeight p b * f b`.
- `bernoulliProb p P = bernoulliExpect p (fun b => if P b then 1 else 0)`.

All coordinate-indexed declarations use `{V : Type*} [Fintype V]`; no nonemptiness, edge-size, or coordinate-cardinality assumption is present.

## Proved interfaces

`sum_bernoulliWeight` gives total weight one (algebraically even without parameter inequalities); `bernoulliWeight_nonneg` supplies nonnegativity under `0≤p≤1`. Expectation has constant, addition, scalar multiplication, monotonicity, nonnegativity, reindexing, and one-coordinate decomposition lemmas.

`bernoulli_harris hp hp1 f g hf hg` proves `E f * E g ≤ E (fun b => f b*g b)` for arbitrary increasing real-valued `f,g`, without sign restrictions on those functions. `bernoulli_harris_event` and `bernoulli_harris_events` specialize this to two events and any finite family of increasing events.

`bernoulliProb_all_false p e` gives `(1-p)^e.card`; `bernoulliProb_hits p e` gives `1-(1-p)^e.card`. The actual edge-family caller

```
bernoulliProb_all_edges_hit hp hp1 edges :
  (∏ e ∈ edges, (1-(1-p)^e.card)) ≤
  bernoulliProb p (fun b => ∀ e ∈ edges, ∃ v ∈ e, b v=true)
```

therefore applies directly to the family of initially monochromatic actual edges in the RS argument, including overlaps. Additional probability interfaces include complement, union bound, and an actual assignment witness from probability below one.

`bernoulli_jensen` uses Mathlib finite convex Jensen with these same normalized weights. `bernoulli_exp_jensen` and `bernoulli_rpow_jensen` derive the exponential and positive-base real-power versions needed to average the initial monochromatic-edge count.

## Verification

Command (inside `formal`, after setting the project-local `ELAN_HOME` and `PATH`):

```
lake env lean -o .lake/build/lib/lean/Aris4Math/General/RS/Bernoulli.olean Aris4Math/General/RS/Bernoulli.lean
lake env lean ../context/propertyb-general-lean-pilot/bernoulli/Audit.lean
```

Both commands exited zero. The final source compile has no errors or warnings; `build-final.log` records 12.05 seconds wall, 3.61 seconds user CPU. The macOS `/usr/bin/time -l` maximum resident set size is 1,939,128,320 bytes (peak memory footprint 124,119,776 bytes; these are distinct platform counters).

`Audit.lean` independently imports the produced module, checks the key signatures, invokes the arbitrary-edge-family hit theorem, and prints transitive axioms. The audited Harris, finite-family Harris, actual edge caller, and real-power Jensen depend only on `propext`, `Classical.choice`, and `Quot.sound`. No `sorry`, new axiom, or `native_decide` occurs in the module.

This is a local module proof and import check, not a complete RS failure-bound proof or the 17-uniform pilot. The parent stage must still connect the actual RS algorithm and initial monochromatic-edge counting, and arrange the requested cross-family review of the new encoding. No cross-family review was initiated by this worker.
