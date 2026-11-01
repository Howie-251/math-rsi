# RS probability and pilot assembly

Sources: `formal/Aris4Math/General/RS/ProbabilityBound.lean` and `PilotMain.lean`.

The intended final exported chain is:

1. `pair_probability_sum`: sum over the same actual `singlePairs E` and both colors is exactly `gamma E / (2^(k-1))² * jk k p`, using the proved exact `sampleProb_pairEvent` for each actual pair. This accounts for the one-color denominator `2^(2*k-1)` and the two colors explicitly.
2. `rs_recoloring_failure_le_fin`: `rs_union_bound` followed by that exact sum identity gives the complete actual finite-index algorithm failure bound.
3. `rsFailureProbability E p`: for arbitrary bare `[Finite V]`, use `Fintype.ofFinite V` and the actual relabeled family under `Fintype.equivFin V` in the same finite-index algorithm. This is the specified internal finite representation, not an abstract probability supplied as a premise.
4. `rs_recoloring_failure_le`: generic actual finite vertices, uniformity, edge count, and gamma transported exactly by Lift.
5. `propertyB_of_rsFailureProbability_lt_one`: an actual successful algorithm coloring is pulled back to the original vertex type.
6. `propertyB_of_rs_bound`: the explicit RS numerical bound strictly below one implies original Property B, with all event coverage and probability estimates inside the dependency chain.
7. `propertyB_seventeen_of_at_most_two_pow : PilotTarget`: invoke that same proved general criterion at k=17, p=1/17, using `pilot_estimate_actual E hm`. There is no extra pair probability, positive-association, vertex-number, certificate, or coverage premise.

The generic bound's original assumptions are `k ≥ 2`, `Uniform E k`, and `0 < p ≤ 1`. The pilot has exactly the original `[Finite V]`, 17-uniformity, and at most `2^17` edges, and produces Bool witnesses of both colors on every edge. The available crude gamma bound by `m²` suffices for the numerical caller, including the empty family.

Final executed build results, type/axiom evidence, and remaining integration items are appended after compilation. No pending imported module or uncompiled source is counted as a proof here.

Executed final results:

- `PROBABILITY_BUILD.log`: exit 0, no diagnostics; 7.97 s wall, 4.12 s user CPU, 2.02 s system CPU, max RSS 2,337,193,984 bytes. The original-object `rs_recoloring_failure_le` and `propertyB_of_rs_bound` both depend only on `propext`, `Classical.choice`, and `Quot.sound`.
- `PILOT_BUILD.log`: exit 0, no diagnostics; 7.21 s wall, 2.65 s user CPU, 2.14 s system CPU, max RSS 2,306,326,528 bytes. `propertyB_seventeen_of_at_most_two_pow` has exactly those same three axioms.
- `CALLER.log`: exit 0; 9.63 s wall, 4.65 s user CPU, 2.08 s system CPU, max RSS 2,293,563,392 bytes. Independent import restates the pilot with arbitrary bare `[Finite V]`, a literal 17-edge-card condition, at most `2^17` actual edges, and explicit true and false witnesses for every original edge. It prints the actual probability definition and the complete P/C/Pilot types. The literal original-form caller also uses only the three standard axioms.

Both final oleans are available in `formal/.lake/build/lib/lean/Aris4Math/General/RS/`. The delegated assembly has no remaining proof or interface obligation. Root retains responsibility for the specified normal Lake build, final independent audit, required cross-family reviews, wiki/state integration, and phase delivery. This assembly proves the RS core and pilot; it does not claim that the complete general growing-integer-gain theorem has been formalized.

A concrete Lean implementation issue was eliminated at the actual pair caller: `singlePairs` uses a classical decidable equality internally, while the fixed-index pair theorem uses the standard `Fin n` equality. The original actual intersection is bridged by a proved Finset membership equivalence (singleton characterization and extensionality), preserving the exact same vertices and intersection cardinality. No equality-instance compatibility premise is exposed.

Reproduce from `formal/`, using the already built actual imported modules:

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
lake env lean -o .lake/build/lib/lean/Aris4Math/General/RS/ProbabilityBound.olean Aris4Math/General/RS/ProbabilityBound.lean
lake env lean -o .lake/build/lib/lean/Aris4Math/General/RS/PilotMain.olean Aris4Math/General/RS/PilotMain.lean
lake env lean ../context/propertyb-general-lean-pilot/assembly/Caller.lean
```

The specified entry now also imports `SampleLaw.lean`, which explicitly defines the common joint sample mass, proves its nonnegativity for `0≤p≤1`, proves `sampleExpect` equals the actual triple weighted sum, and proves the common joint mass sums to one. The mathematical definition supplied by root was retained. `sample-law-build.log` records its source/olean build exit 0 (2.67 s); `sample-law-audit.log` independently imports the exact module, prints all three statement types, and confirms exactly the standard three axioms, exit 0 (2.52 s). The implementation fix proves equality of `univ` finsets extensionally when their Fintype dictionaries differ, and distributes the inner multiplication over the actual sum. `PilotMain.olean` was regenerated with the additional probability-law import; the latest result is in `PILOT_BUILD.log`.
