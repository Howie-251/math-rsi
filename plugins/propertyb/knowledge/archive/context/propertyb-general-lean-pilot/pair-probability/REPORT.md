# Exact probability of the actual RS pair event

Source: `formal/Aris4Math/General/RS/PairProbability.lean`.
Namespace: `Aris4Math.General.RS`.

The full actual-event probability formula is proved. No external pair-probability assumption is used.

```
sampleProb_pairEvent {n k : ℕ} (f g : Finset (Fin n))
  (hfg : (f ∩ g).card = 1) (hf : f.card = k) (hg : g.card = k)
  (hk : 1 ≤ k) (q : Bool) (p : ℝ) :
  sampleProb p (fun c b σ => PairEvent f g c b σ q) =
    jk k p / (2 : ℝ)^(2*k-1)
```

`sampleProb_pairEvent_singleton` takes the explicit common vertex and `f∩g={x}`. `sampleProb_pairEvent_eq_zero` proves probability zero for non-single-intersection pairs. `sampleProb_pairEvent_formula` combines both into the exact formula with an `if (f∩g).card=1` branch.

The equalities are finite weighted-sum identities for every real `p`. Probability applications use `0≤p≤1`, as elsewhere in the stage; the formula itself needs no extra sign premise. The edge-size premise is `k≥1`, so the stage's `k≥2` calls apply directly.

## Connection to the actual algorithm

`PairEvent` is imported directly from `Algorithm.lean`. `pairEvent_iff_local` proves its equivalence to the following event for `F=f.erase x`, `G=g.erase x`:

- The pivot has initial color `!q` and is eligible.
- Every `F` vertex of initial color `!q` is eligible and precedes the pivot.
- Every `G` vertex has initial color `!q`; each eligible one follows the pivot.

For fixed colors and eligibility bits, let `A` be the vertices of `F` having initial color `!q`, and let `B` be the eligible vertices of `G`. After factoring out the non-order conditions, the remaining event is exactly `BeforeAfter A B x`. The sets are disjoint and exclude the pivot because the original edges meet exactly at `x`.

`permProb_pairLocal` uses `beforeAfter_ratio` for the actual global permutation, then `beta_nat`, proving that this fixed-bit probability is the integral of a finite product of local factors. Inactive vertices are included in the original permutation sample and are eliminated only through the proved relative-order ratio.

## Finite averaging and the integral

`bernoulliExpect_intervalIntegral` proves finite weighted expectation/integral interchange for continuous functions by finite-sum linearity. `pairIntegrand_continuous` supplies its actual hypothesis.

`bernoulliExpect_two_coordinate_prod` factors the independent initial-color and eligibility coordinates. It does not declare independence between edges. At fixed integration variable `t`, the averaged factors are:

- Pivot: `p/2`.
- Each vertex of `F`: `(1+p*t)/2`.
- Each vertex of `G`: `(1-p*t)/2`.

`pairIntegrand_average` proves this calculation for arbitrary disjoint `F,G`. Consequently the actual sample probability is

\[
\int_0^1 \frac p2\left(\frac{1+pt}{2}\right)^{|F|}
\left(\frac{1-pt}{2}\right)^{|G|}\,dt.
\]

For two `k`-edges, both exponents equal `k−1`. `sampleProb_pairLocal_eq_jk` extracts `2^{2k−1}` and calls `jk_rescale`, yielding the exact stated probability for one specified color. The final `sampleProb_pairEvent` invokes this chain from the original `PairEvent`, rather than taking the local-event formula as an unproved premise.

## Verification

With project-local `ELAN_HOME` and `PATH`, from `formal`:

```
lake env lean -o .lake/build/lib/lean/Aris4Math/General/RS/PairProbability.olean Aris4Math/General/RS/PairProbability.lean
lake env lean ../context/propertyb-general-lean-pilot/pair-probability/Audit.lean
```

The final source compilation exited zero with no warnings. `build-final.log` records 18.69 seconds wall and 7.29 seconds user CPU. The macOS `time -l` maximum resident set size was 2,272,919,552 bytes; peak memory footprint was 126,069,592 bytes (different platform counters).

`Audit.lean` independently imports the produced module, prints actual final types and transitive axioms, and calls the singleton theorem from arbitrary actual `k`-edges and `k≥2`. The audit exited zero. All five audited declarations depend only on `propext`, `Classical.choice`, and `Quot.sound`; see `audit.log`. No `sorry`, new axiom, or `native_decide` is present in this module.

This module discharges the pair-probability obligation; overall RS failure coverage, residual probability averaging, pair summation, and the 17-uniform caller are parent-stage assembly obligations. Cross-family review is arranged by the parent; this worker did not initiate a separate review call.
