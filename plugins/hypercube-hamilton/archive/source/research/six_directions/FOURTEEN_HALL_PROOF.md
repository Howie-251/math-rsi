# Fourteen-hole exact positive neighbor-deficiency exclusions

2026-11-02. ARIS proof-writer. PROVABLE AS STATED from the finite witness obligations below; independent checking pending.

## Claim and scope

Of the 12,546 original-label configurations in the six frozen
`FOURTEEN_CACHED_remaining_h14_v{1,7,31}_{covered,free}.bin` files,
8,623 cannot be the hole set of a short matching in Q6. The exact complement
has 3,923 covered-target configurations and no free-target configurations.
This is an exclusion of unrealizable input geometries, not a negative
Hamilton-path result. The completeness of the starting domain depends on
the accepted FOURTEEN_CACHED and FOURTEEN_REUSE applications, the full
twelve-hole predecessor, and their explicit imports.

## Direct mathematical proof

A source record lists six distinct even nonroot holes Z followed by seven
distinct odd holes W; root u=0 and H={0} union Z union W. Let E and O be
the covered even and odd vertices. Each has 25 vertices. A short matching
with exactly H uncovered would give a bijection from E to O along cube
edges. Each witness supplies a nonempty S subset E and T equal to the
entire neighborhood of S inside O, with |T|<|S|. The distinct partners of
all vertices in S would belong to T, an impossible injection. Therefore
that input admits no original matching.

This proof uses only explicit neighborhoods and cardinalities. Neither
optimality of the producer matching search nor any negative solver verdict
is a premise. No realizability claim is made for the retained inputs.

## Finite obligations and exact partition

Each witness is 22 bytes in little-endian format `<BBIQQ`: target v,
free-target flag, source record index (uint32), S mask and T mask (uint64).
Inputs are 13-byte records (sorted Z6 then W7). An independent checker
must validate all source records and their status, source hashes, unique
witness indices, S subset E, exact T=N(S) intersect O and |T|<|S|. Deleting
exactly witnessed indices in source order must reproduce every corresponding
`FOURTEEN_HALL_remaining_v{v}_{status}.bin` byte for byte.

| Target and status | Input | Positive exclusions | Remaining |
|---|---:|---:|---:|
| 1 covered | 3105 | 2265 | 840 |
| 1 free | 0 | 0 | 0 |
| 7 covered | 3613 | 2425 | 1188 |
| 7 free | 18 | 18 | 0 |
| 31 covered | 5810 | 3915 | 1895 |
| 31 free | 0 | 0 | 0 |
| Total | 12546 | 8623 | 3923 |

## Free-target assembly consequence

Once the source and finite exclusion gates are accepted, the entire
fourteen-hole free-target branch closes. For a matching of 25 short edges,
the fourteen holes consist of seven vertices of each parity. Normalize a
free endpoint to 0 by a cube automorphism; coordinate permutations send
the opposite-parity free target to 1,7 or31 according to its distance.
The accepted nearbalanced predecessor reduction, using complete twelve
holes for adjacent-hole augmentation, covers all cases outside its exact
residual. Its fourteen-hole free residual has 232,042 records. The accepted
reuse application leaves 318 free records; the cached application leaves
only 18 at v=7. Every one has the explicit obstruction above, so none is
realized by a short matching. Thus every actual matching and any prescribed
free opposite-parity endpoints have the required Hamilton path.

The free branch assembly must independently check that the source reduction
has the full free-target quantifier, that its predecessor is discharged by
TWELVE_HOLE_FULL_REVIEW, and that each consecutive residual is exact.
Full fourteen holes and full P6 remain OPEN because 3,923 covered-target
geometries remain. Same-family audit is not formal proof-assistant checking.
