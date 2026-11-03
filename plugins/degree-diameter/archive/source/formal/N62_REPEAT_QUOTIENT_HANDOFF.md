# Actual repeat quotient identities, 2026-10-11

`DegreeDiameter/N62RepeatQuotient.lean` connects the actual quotient constructed in N62RepeatComponents to the exact identities needed by the new connected-repeat reduction. It imports the completed component module and Mathlib's finite connected-component API, without changing the component module or shared entry points.

For the actual integer matrix `R = repeatQuotientMatrix G`, and actual sizes `n_C = repeatComponentSize G C`, the original degree/diameter/card62 hypotheses alone prove:

- `n62_repeat_quotient_quadratic`: R*R+R = 10•I + repeatSizeMatrix G. The latter matrix has entry n_C in every row of column C, so this is exactly R²+R=10I+1 nᵀ.
- `n62_repeat_quotient_row_sum`: every row sum of R is eight.
- `n62_repeat_quotient_balance`: n_D R[D,C] = n_C R[C,D].
- `n62_repeat_component_sizes_sum`: the actual component sizes sum to 62.
- `repeat_component_size_pos` and `repeat_quotient_nonnegative`: sizes are positive and entries are nonnegative integers.

The component index is the actual type `(repeatSupport G).ConnectedComponent`, with its Fintype constructed by Mathlib's WalkCounting/connected-component API from finite V and actual adjacency. No finite index, size vector, equitable partition or quotient matrix is supplied by the caller. No B≤2 premise occurs.

The proof uses the actual vertex/component membership matrix S, whose entry is the previously defined component indicator. Multiplication by S evaluates a component matrix at the unique component containing a given vertex. Existing equitability gives AS=SR; actual component harmonicity gives BS=3S; summing actual component indicators gives JS=S·(1 nᵀ). Substituting these into the actual definition B=A²+A−7I−J and evaluating at an actual vertex of each component gives the quadratic identity. Row sums follow because each original vertex lies in exactly one component. Balance is proved by summing actual symmetric adjacency over both component indicators and reversing the two summation indices.

This module does not prove component-size evenness, the spectral trace17 identity, parity or bounds for the number of components, connectedness, or any finite quotient enumeration. Those remain separate obligations. The requested row, balance and quadratic identities are fully connected to original graph inputs.

Verification (Lean/mathlib 4.24, at most three threads):

```bash
cd formal
source ../.tools/lean-env.sh
export LEAN_NUM_THREADS=3 RAYON_NUM_THREADS=3
lake build DegreeDiameter.N62RepeatQuotient
lake env lean ReviewN62RepeatQuotient.lean
```

Successful build: `logs/n62-repeat-quotient-second.log`, exit 0, no warnings. Dedicated audit: `logs/n62-repeat-quotient-type-axiom-audit.log`, exit 0. The audit prints the actual size, membership, column-size and quotient definitions, checks all eleven public theorem types and transitive axioms, and compiles original-graph quadratic and row/balance callers. All eleven theorem chains use only propext, Classical.choice and Quot.sound. The earlier failed rectangular-matrix rewrite attempt is retained and is not proof evidence. No sorry, new axiom, native_decide or hashes were introduced. Shared imports, STATUS and cross-family source review remain parent-owned.
