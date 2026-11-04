# Explicit neighbor-deficiency witnesses remove7483 impossible geometries

2026-11-01. ARIS proof-writer candidate; independent review pending.

## Exact sufficient exclusion

For each record certified in `TWELVE_HALL_witnesses.bin`, there is no
short Q6 matching whose uncovered set is exactly H={0} union Z union W
from that record. These are7483 of the37405 original-label inputs in
`TWELVE_NEW_TYPES_positive_remaining_v{1,7,31}.bin`. No conclusion about
nonexistence of Hamilton paths for an actual matching is asserted.
These records cannot be realized by the original matching in the first
place. Other records are retained without a negative or positive theorem.

## Direct proof from each witness

Let L be the even vertices outside H and R the odd vertices outside H.
Both have26 elements. Every short matching with exactly those holes
must pair every vertex of L with a distinct vertex of R by a cube edge.
The supplied nonempty S is a subset of L. Its supplied T is checked
to equal all cube neighbors of S that lie in R, and |T|<|S|.
All partners of S would lie in T and would be distinct, giving an
injection from the larger finite set S into the smaller T. This is
impossible. This proves the exclusion without trusting a matching solver
or needing the converse of Hall's theorem.

## Exact format and finite obligations

Each21-byte record is little-endian `<BIQQ`:

- normalized target v: one unsigned byte;
- original input record index: uint32;
- S: uint64 bitmask of actual Q6 vertices;
- T: uint64 bitmask of actual Q6 vertices.

Each input record consists of eleven vertex bytes, sorted Z5 then W6,
with root0. The checker must verify source file bindings, legal target
and hole counts, each unique source index, S subset of covered evens,
T equal to the entire covered odd neighborhood, and the strict cardinality
deficiency. Keeping all records not so certified, in source order, must
reproduce each claimed residual byte stream exactly.

| target | input | excluded by explicit witness | remaining |
|---:|---:|---:|---:|
|1|8032|1717|6315|
|7|11661|1581|10080|
|31|17712|4185|13527|
|total|37405|7483|29922|

The producer uses augmenting paths and alternating reachability to find
S,T. Its control flow or maximality is not a premise of the proof: each
positive obstruction is independently checked by the finite inequality
and exact neighborhood equality. No sampling, numerical tolerance or
negative solver verdict is used as a certificate.

## Dependency and union boundary

The local exclusions depend only on the specified input bytes and their
witnesses. Treating the37405 as the complete remaining Q6 domain additionally
requires acceptance of `TWELVE_NEW_TYPES_APPLICATION.md` and its upstream
proof chain. Combining these exclusions with552 new forced-cherry successes
requires exact record-set union, not adding counts; such a union is a
separate application artifact. Full twelve-hole and P6 remain OPEN.
