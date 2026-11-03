# Actual repeat-component equitability, 2026-10-11

`DegreeDiameter/N62RepeatComponents.lean` implements the actual-component equitability step of `proofs/dd82/n62/GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`, section 3, needed by the new connected-repeat reduction. It uses only the original order62 graph hypotheses and the actual Defect foundations. It does not import the D1, triple-repeat, parity or exclusion chains.

The main original-domain theorem is:

    n62_repeat_components_equitable
      (G : SimpleGraph V)
      (hdeg : degreeAtMostEight G)
      (hdiam : diameterAtMostTwo G)
      (hcard : Fintype.card V = 62)
      (C D : (repeatSupport G).ConnectedComponent)
      (hx : x ∈ D.supp) (hy : y ∈ D.supp) :
      repeatComponentNeighborCount G C x =
      repeatComponentNeighborCount G C y.

The neighbor counts are actual cardinalities of `G.neighborFinset` filtered by membership in the actual repeat component. No equitable-partition, quotient, harmonicity, component-closure or counting certificate is an extra original caller premise. No global B≤2 assumption is needed.

Definitions and proof chain:

1. `repeatSupport G` has adjacency `x≠y ∧ 0<B[x,y]`, giving a simple graph for every input. `n62_repeat_support_adj_iff` proves this is exactly `0<B[x,y]` under the original order62 assumptions, since the actual defect diagonal is zero.
2. `integer_weighted_harmonic_edge_eq` proves a finite integer Dirichlet identity: for symmetric nonnegative weights with constant row sum k and Bf=kf, the nonnegative sum of B[x,y](f[x]−f[y])² is zero. Hence f is equal across every positive-weight edge.
3. `n62_repeat_harmonic_constant` applies that lemma to the actual B with row sum three and propagates equality along actual support walks.
4. `n62_repeat_component_indicator_harmonic` constructs B1_C=3·1_C from actual component membership. A positive B entry joins vertices in the same actual component, so each summand can replace 1_C(y) by 1_C(x).
5. `adjacency_mul_repeat_indicator` identifies A1_C with the actual original-neighbor count vector. `n62_repeat_component_neighbor_count_harmonic` then uses AB=BA to derive harmonicity of that actual vector.
6. The final equitability theorem follows from actual support reachability. `repeatComponentDegree G D C` chooses a source representative solely to define a concrete natural degree; `n62_repeat_component_degree_spec` proves every source vertex has that degree. `repeatQuotientMatrix G` is its integer cast. The internal-degree corollary proves each component has constant actual original internal degree.

The generic harmonic theorem is for integer vectors, which suffices for component indicators and original-neighbor counts. No real spectral eigenspace classification, quotient quadratic identity, quotient row/balance identity, trace17 formula, component-count restriction, connectedness result or finite enumeration is claimed here. Those are later obligations; the actual quotient-entry construction is now available for them.

Verification (Lean/mathlib 4.24, at most three threads):

```bash
cd formal
source ../.tools/lean-env.sh
export LEAN_NUM_THREADS=3 RAYON_NUM_THREADS=3
lake build DegreeDiameter.N62RepeatComponents
lake env lean ReviewN62RepeatComponents.lean
```

Successful build: `logs/n62-repeat-components-fourth.log`, exit 0, no warnings. Dedicated audit: `logs/n62-repeat-components-type-axiom-audit-final.log`, exit 0. The audit prints all six actual definitions, checks all ten public theorem types and transitive axioms, and compiles raw equitability and quotient-entry callers. All ten theorem chains use only propext, Classical.choice and Quot.sound. Earlier failed API/import attempts are retained but are not verification evidence. No sorry, new axiom, native_decide or hashes were introduced. Shared entry point, STATUS and cross-family final source review remain parent-owned.
