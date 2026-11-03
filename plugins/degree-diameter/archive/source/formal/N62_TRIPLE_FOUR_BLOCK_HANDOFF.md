# Four-label triple-repeat block classification

The requested generic matrix classification is complete in
`DegreeDiameter/N62TripleFourBlock.lean`. It is the four-label algebraic
case coverage used in Step 3 of `proofs/dd82/n62/RECOVERED_REDUCTION.md`.
This module does not construct the matrix from an original graph and
does not assert an actual-graph exclusion.

For a supplied matrix `N : Matrix (Fin 4) (Fin 4) ℤ`, the hypotheses are
exactly symmetry, zero diagonal, nonnegative entries, and every row sum
equal to 3. The final theorem `n62_four_block_classification` gives an
actual permutation `σ : Equiv.Perm (Fin 4)` fixing 0, such that the
relabelled matrix `fun i j => N (σ i) (σ j)` has one of the three
patterns 300, 210, or 111.

The definition `tripleFourPattern N a b c` specifies all six upper
off-diagonal entries:

```
N01 = a, N02 = b, N03 = c,
N12 = c, N13 = b, N23 = a.
```

The supplied symmetry and zero diagonal determine the remaining ten
entries, also after the relabeling. Thus the conclusion concerns the
four matrix labels, not a free permutation of three unrelated weights.

Exported results:

* `n62_four_block_opposite_entries`: symmetry, zero diagonal, and row
  sums alone give opposite-entry equality and `N01 + N02 + N03 = 3`.
* `n62_four_block_weight_cases`: adding nonnegativity gives the ten
  ordered integer triples for those actual three matrix entries.
* `n62_four_block_classification`: explicit permutations of the four
  labels, fixing 0, put the whole off-diagonal pattern into 300, 210,
  or 111. The permutations use swaps of labels 1, 2, and 3.

The proof normalizes the four finite row sums, uses integer linear
arithmetic for opposite-entry equality and the bounded weight cases,
and verifies explicit permutation witnesses. No external enumeration
script, `native_decide`, `sorry`, or new axiom is used.

The dedicated target build exited 0 without warnings in
`logs/n62-triple-four-block-build-third.log` (Lean module time 9.6s).
The separate import audit `ReviewN62TripleFourBlock.lean` prints the
pattern definition, all three exported types, and their transitive
axioms, and applies the final theorem to a caller with exactly the
requested matrix hypotheses. It exited 0 without warnings in
`logs/n62-triple-four-block-type-axiom-audit.log`. All three theorems
depend only on `[propext, Classical.choice, Quot.sound]`.

Earlier logs are historical development evidence: the first build was
stopped while an overly broad tactic import was compiling unrelated
uncached dependencies; the second found the row-expression normalization
and one-shot arithmetic timeout repaired in the final source. Neither
is a successful verification record. The final imports are narrow.

Reproduction from `formal/`, coordinated with other authors so that at
most three Lean threads are active in total:

```bash
source ../.tools/lean-env.sh
export LEAN_NUM_THREADS=3 RAYON_NUM_THREADS=3
lake build DegreeDiameter.N62TripleFourBlock
lake env lean ReviewN62TripleFourBlock.lean
```

The existing toolchain is Lean 4.24.0 with the pinned Mathlib v4.24.0.
This was an incremental target build plus a separate import audit,
not a clean rebuild of the whole project. Shared imports, shared status
files, and existing modules were not edited. Parent integration and
cross-family source review remain separate; no such review is claimed
in this handoff. The next graph-level obligation is to construct the
actual `E` block and discharge these four matrix premises from it.
