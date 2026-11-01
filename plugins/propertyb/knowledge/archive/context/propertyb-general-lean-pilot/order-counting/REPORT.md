# Relative-order count module

Source: `formal/Aris4Math/General/RS/OrderCounting.lean`.
Namespace: `Aris4Math.General.RS`.

The processing permutation maps a vertex to its processing position. `BeforeAfter A B x σ` means every vertex of `A` has position below `σ x`, and every vertex of `B` has position above `σ x`.

## Exported interfaces

- `card_orderPattern vertices τ`: for any embedding `vertices : Fin r ↪ Fin n`, the number of global permutations realizing the active relative rank permutation `τ` is `n.choose r * (n-r)!`.
- `relativeRank vertices σ`: actual rank permutation of the active vertices, obtained by sorting their actual occupied positions.
- `relativeRank_lt_iff`: relative-rank comparisons are exactly comparisons of the actual global processing positions.
- `card_relativeEvent` and `relativeEvent_ratio`: any event `P` on this actual active rank has uniform fibres; its global normalized count is `card {τ // P τ} / r!`.
- `card_beforeAfter A B x hAB hxA hxB`: exact actual global event count, `(A.card! * B.card!) * (n.choose r * (n-r)!)`, where `r=A.card+B.card+1`.
- `beforeAfter_ratio A B x hAB hxA hxB`: actual global event count divided by `card (Equiv.Perm (Fin n))` is `(A.card! : ℝ) * B.card! / r!`.

Only the original assumptions `Disjoint A B`, `x ∉ A`, and `x ∉ B` are required. The active vertices need not exhaust `Fin n`; inactive vertices are unrestricted. Empty `A` and/or `B` are allowed. In particular, no upper bound on `n` and no permutation enumeration is used.

## Proof connection

For a fixed active relative order, decompose by the actual occupied position set, sort it, and use `Counting.card_prescribed_images` to count each image fibre as `(n-r)!`. There are `n.choose r` possible occupied sets. `relativeRank` supplies the actual unique relative order of every global permutation. A before/pivot/after order on the active domain is equivalent to preserving the lower block and fixing its endpoint; independent permutations of the before and after blocks give `A.card! * B.card!`. `blockEmbedding` internally numbers arbitrary input `A,x,B` in block order and is proved to reproduce those actual vertex sets and pivot.

## Verification

`compile16.log` records successful compilation of the full arbitrary-set ratio theorem, with each audited declaration using only `propext`, `Classical.choice`, and `Quot.sound`. `BUILD.log` is the final source compilation and olean generation, including the integer-count convenience theorem. `CALLER.log` is an independent import and a literal global-position statement normalized by `n!`.

The final status and actual command results are appended after completion. Intermediate compiler errors are retained in numbered logs as implementation history; no incomplete proof is accepted in the final module. Cross-family review of these new interfaces is delegated to the root workflow and is not claimed here.

Reproduce from `formal/` with the project-local Lean 4.24.0 environment:

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
lake env lean -o .lake/build/lib/lean/Aris4Math/General/RS/OrderCounting.olean Aris4Math/General/RS/OrderCounting.lean
lake env lean ../context/propertyb-general-lean-pilot/order-counting/Caller.lean
```

Final verification: `BUILD.log` exit 0, 41.97 s wall, 6.48 s user CPU, 2.09 s system CPU; maximum resident set size 1,346,060,288 bytes. The four audited exports have exactly `propext`, `Classical.choice`, and `Quot.sound`. The generated olean is available at `formal/.lake/build/lib/lean/Aris4Math/General/RS/OrderCounting.olean`.

Independent actual-position caller: `CALLER.log` exit 0, 16.52 s wall, 1.50 s user CPU, 1.92 s system CPU; maximum resident set size 1,313,570,816 bytes. Both `actual_position_caller` and the integer-count theorem have only the same three axioms. These timings occurred alongside root-controlled dependency builds and are not isolated benchmarks.

Lean API note: when restating `BeforeAfter` literally, different `Decidable` instances can produce non-definitionally-equal `Fintype` dictionaries. `Caller.lean` resolves this with an explicit `@Fintype.card_congr _ _ _ _ (Equiv.refl _)` before rewriting; no mathematical assumption is added. The module locally disables `Nat.decidableForallFin` only within the `card_orderPattern` theorem command to align with the existing `Counting.card_prescribed_images` compiled interface. The attribute change does not escape that command.

No open mathematical or formalization obligation remains in this delegated relative-order count task. Root integration and the explicitly requested cross-family workflow remain the root's responsibility.
