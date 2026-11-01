# General pair-covering reduction

Owned implementation: `formal/Aris4Math/General/Structure/Reduction.lean`.

The checked interface starts with an arbitrary finite vertex type, an actual finite simple edge family, arbitrary uniformity `k`, arbitrary edge bound `N`, and failure of the original existential Bool bichromatic coloring. It produces a `Fin n` counterexample with the same uniformity, at most `N` edges, and pair coverage. Pair coverage is a conclusion obtained by minimizing the number of vertices among all such counterexamples and identifying any uncovered pair. Image edges are deduplicated, so the number of edges may decrease. Edgewise injectivity proves preservation of uniformity; pulling back the two actual color witnesses proves preservation of noncolorability.

The exported declarations in namespace `Aris4Math.General.RS` are:

- `exists_pair_covering_counterexample E hU hM hB`: `∃ n K, Uniform K k ∧ K.card ≤ N ∧ ¬ PropertyB K ∧ PairCovering K`.
- `pairCovering_count K hU hpair`: `n * (n - 1) ≤ k * (k - 1) * K.card`.
- `not_propertyB_card_pos K hB`: `0 < K.card`.
- `uniform_le_vertices_of_not_propertyB K hU hB`: `k ≤ n`.
- `pairCovering_vertex_bound K hU hM hB hpair`: `0 < K.card ∧ k ≤ n ∧ n * (n - 1) ≤ k * (k - 1) * N`.

The counting argument covers the actual ordered off-diagonal vertex pairs by the union of the actual ordered off-diagonal edge pairs and uses the cardinality upper bound for a union. No assumption `2 ≤ k` is needed. There is no five-uniform object, old Property B theorem, probability estimate, external certificate, or hypothetical structure in this dependency route.

Verification performed locally in the pinned existing project:

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
cd /Users/rfy_naiveai/Desktop/aris4math/formal
lake env lean Aris4Math/General/Structure/Reduction.lean -o .lake/build/lib/lean/Aris4Math/General/Structure/Reduction.olean
lake env lean ../context/propertyb-general-lean-growth/reduction/Audit.lean
```

The direct module compilation completed with exit status 0 (`compile02.log`), after the parent supplied the compiled shared Definitions dependency. The subsequent independent import/caller file completed with exit status 0 (`audit.log`); it combines all five exports on an arbitrary original input. Printed transitive axioms are only `propext`, `Classical.choice`, and `Quot.sound`. The initial `compile01.log` retains a fixed elaboration failure from an unspecified predicate in `Fintype.card_subtype_lt`; it is not final acceptance evidence.

Self-audit: the least-vertex property quantifies over all finite-label counterexamples under the original edge budget; it does not minimize only pair-covering examples. Identifying two uncovered vertices is proved injective on every actual edge before invoking uniform image preservation. Noncolorability follows by pulling both true and false witnesses back along the map. Ordered pairs are counted with multiplicity only in the upper bound sum, so edge intersections and repeated witnesses cause no undercount. The result is valid for all natural `k,N`, including the degenerate parameters; no extra positivity assumption is silently used. This is local checked code and self-review, not an external cross-family review or a second-machine reproduction.

Remaining implementation obligations in this owned scope: none. Full integration/build and requested reviewer routing remain with the parent.
