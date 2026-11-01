# C.1 actual single-intersection family bound

Implemented `formal/Aris4Math/General/Structure/Clique.lean` in namespace
`Aris4Math.General.RS`, using the shared `Uniform`, `SingleIntersecting`,
`cliqueBudget`, and `singleGraph` definitions.

- `singleIntersecting_star_card_le`: if a family member misses `x`, the star at
  `x` has at most `k` members. The injection assigns each star member its unique
  intersection with that missing member; equality of images forces equality of
  members by their common `x`.
- `singleIntersecting_card_le_of_no_common`: with no common vertex, fix a member
  `e`. The stars at its `k` vertices cover all other members. Erasing `e` from each
  star leaves at most `k-1` members, giving `q-1 ≤ k(k-1)`. The empty family is
  explicitly covered.
- `singleIntersecting_common_point_bound`: erasing a common vertex makes all
  members disjoint. Their union lies in `univ.erase x`, giving
  `q*(k-1)+1 ≤ Fintype.card V`.
- `singleIntersecting_card_le_cliqueBudget`: combines these cases using exact
  natural-number division, for `2 ≤ k`.
- `singleGraph_isClique_card_le_cliqueBudget`: images a finite clique under
  `Subtype.val`, proves uniformity and actual pairwise single intersections,
  preserves its cardinality, and applies the family bound. No realization,
  Gram, probability, or additional certificate premise is supplied.

This is the complete C.1 interface requested from this worker. The Turan worker
owns the finite-clique-bound to `CliqueFree` conversion. No other source module
was edited by this worker.

Verification from `formal/`, after root built shared dependencies:

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
lake env lean Aris4Math/General/Structure/Clique.lean -o .lake/build/lib/lean/Aris4Math/General/Structure/Clique.olean
lake env lean ../context/propertyb-general-lean-growth/clique/Audit.lean
```

Both final commands exited 0. Final `compile.log` is empty (no diagnostics).
The independent import in `Audit.lean` also checks the raw expanded maximum
bound as an actual caller. `audit.log` records all four main declarations and
their transitive axioms: only `propext`, `Classical.choice`, and `Quot.sound`.
No `sorry`, extra axiom, or `native_decide` is used. This is a local Lean check;
no cross-family review or second-machine reproduction was performed by this
worker.
