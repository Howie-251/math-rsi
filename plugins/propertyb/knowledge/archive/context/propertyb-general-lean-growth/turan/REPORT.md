# Actual single-intersection count and Turán bound

Scope completed: `formal/Aris4Math/General/Structure/Turan.lean`.

The file imports the fixed Mathlib Turán theorem rather than developing a new graph extremal argument. The actual ordered single-intersection finset is put in explicit bijection with the darts of the graph on the original edge subtype (`singlePairsDartEquiv`). Its cardinality is therefore twice the undirected graph edge count (`gamma_eq_twice_singleGraph_edges`). No counting identity is an externally supplied hypothesis.

`singleGraph_gamma_bound E hr hcf` proves, for arbitrary original `E`, natural `r ≥ 1` and `CliqueFree (r+1)`,

`(gamma E : ℝ) ≤ (1 - 1/(r:ℝ)) * (E.card:ℝ)^2`.

The fixed Mathlib APIs are `SimpleGraph.CliqueFree.card_edgeFinset_le`, `SimpleGraph.card_edgeFinset_turanGraph`, `SimpleGraph.mul_card_edgeFinset_turanGraph_le`, and `SimpleGraph.dart_card_eq_twice_card_edges`. Their native-number inequality is cast to the reals; positivity of `r` justifies division.

`singleGraph_cliqueFree_of_card_le` converts a finite-clique cardinality bound to the forbidden-clique interface. `gamma_le_cliqueBudget` then uses the actual uniform-family result from `Clique.lean` and proves the positive clique-budget premise internally. Its only hypotheses are `[Fintype V]`, `Uniform E k`, and `2 ≤ k`; it has no certificate, assumed graph realization, or assumed clique bound.

Executed verification:

- Direct Lean compilation of `Aris4Math/General/Structure/Turan.lean` to its own package `.olean`: exit 0.
- Subsequent independent import and two actual nonempty callers in `ActualCaller.lean`: exit 0. One caller discharges the clique premise from the original three-edge family. The other applies the complete `gamma_le_cliqueBudget` theorem to the finite uniform triangle edge family on `Fin 3`.
- Seven printed transitive-axiom lists, including both original-family callers, contain only `propext`, `Classical.choice`, and `Quot.sound`; see `actual-caller.log`.
- No `sorry`, custom axiom, or `native_decide` is used.

Reproduction from `formal/` (after the root-managed dependencies are built):

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
lake env lean Aris4Math/General/Structure/Turan.lean -o .lake/build/lib/lean/Aris4Math/General/Structure/Turan.olean
lake env lean ../context/propertyb-general-lean-growth/turan/ActualCaller.lean
```

The independent import is a local incremental check, not a clean build or external-machine reproduction. Cross-family review and final downstream package assembly remain the root agent's workflow responsibilities.
