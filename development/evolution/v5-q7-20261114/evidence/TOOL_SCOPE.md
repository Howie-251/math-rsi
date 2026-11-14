# Q7 evidence/tool implementation scope

Before implementation, 2026-11-14.

- Extend the existing forest consumer, preserving the positional Python `check(dim, root, holes, forests, columns)` and CLI `--root` route. Explicit `--omitted U...` selects multiple omitted holes; exactly one route is supplied. Source: user-authorized task.
- The geometry is `(H,U)`, with `U ⊆ H`. Forest degrees are zero on U, one on K=V\H, two on H\U. Every non-omitted component must be a path with exactly two K endpoints. Required GF(2) rank remains `2^(|K|/2-1)`. Source: mathematical contract in the original T63 proof.
- Marked transport remains in the original frozen plan consumer and mathematical reference: one permutation and XOR must carry both H and U. The forest tool validates its supplied (H,U) and does not introduce another canonicalizer or transport CLI. Root confirmed this thinner interface; the real S3 target4 consumer supplies the marked-transport regression.
- Copy only the frozen direct input set of the existing S3/S2 consumers plus named proof sources, preserving source-relative paths and original bytes. No full transitive certificate or 23GB archive claim. Source: parent-authorized packaging scope.
- Measure the current algorithm on a bounded actual T63 prefix before deciding whether to rerun one complete target. Do not rerun all six targets. Successful partial rank does not certify the universal gate. Source: parent budget.

No commits, pushes, producer searches, new mathematical Goal, or source-archive edits.
