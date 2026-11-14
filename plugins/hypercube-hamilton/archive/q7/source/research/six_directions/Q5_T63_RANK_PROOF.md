# Seven actual T63 marked inputs from short-forest rank certificates

2026-11-01. ARIS proof-writer candidate. Independent verification pending.

## Exact statement

For each row below, let $F$ be any matching of $K(Q_5)$ whose holes are
exactly $H$. There is a simple cycle on precisely $Q_5\setminus U$
containing $F$, with all edges outside $F$ short. Every common cube
automorphism of $(H,U)$ transports the conclusion. Required edges may
be long or have equal-parity endpoints. These are seven marked inputs,
not a claim about every six-hole/three-omission input.

| index | $H$ | $U$ |
|---:|---|---|
|0|0,3,5,10,20,30|0,3,5|
|1|0,3,5,10,12,23|0,3,23|
|2|0,3,5,10,29,30|0,29,30|
|3|0,3,5,10,29,30|0,3,5|
|4|0,3,5,6,24,27|0,5,6|
|5|0,3,5,6,9,27|0,5,6|
|6|0,3,5,10,12,23|0,10,12|

## Proof and exact dependencies

Fix one row and put $K=Q_5\setminus H$, so $|K|=26$. A supplied forest
$S$ has sixteen distinct short edges on $Q_5\setminus U$, degree one
at every vertex of $K$, degree two at the three vertices of $H\setminus U$,
and no cycle. It therefore consists of thirteen paths whose endpoints
are exactly $K$. Let $P(S)$ be their endpoint pairing.

The complete matching-connectivity matrix on all perfect matchings of
$K$ has GF(2) rank at most $2^{26/2-1}=4096$. This is the same general
Corollary 3.5 of Cygan--Kratsch--Nederlof used in the accepted A10 rank
proof, now at 26 endpoints. See `A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md`
and the [primary paper](https://arxiv.org/abs/1211.1506). The theorem is
about arbitrary complete-graph matchings, with no bipartite restriction.

For this row the certificate supplies 4096 forests $S_i$ and 4096 matching
columns $X_j$ on $K$. The matrix with entries one exactly when
$P(S_i)+X_j$ is one labelled alternating cycle has GF(2) rank 4096.
Thus the complete rows indexed by $P(S_i)$ span the complete matrix's
row space. Every column indexed by an arbitrary $F$ is nonzero: orient
its thirteen edges as $(a_i,b_i)$ and use the matching $b_i a_{i+1}$,
cyclically, to form one alternating cycle with $F$.

If every selected row were zero at column $F$, their span would also
be zero there, contradicting that nonzero column. Hence some $F+P(S_i)$
is connected. Expanding each $P(S_i)$ edge to its forest path gives
one simple cycle on the required 29 vertices. Interiors of those paths
partition the three included holes. A common edge of $F$ and $P(S_i)$
would be an isolated labelled two-edge component, impossible in a
connected 26-cycle; therefore a one-edge forest path cannot duplicate
an original required edge in a successful pair. Every required edge
survives, and every newly introduced edge is short.

This proves the stated universal claim once the listed finite forest
and rank hypotheses have been independently verified. Exhaustiveness
of the forest generator is not required. Rank deficiency would not
be a counterexample; here all seven producer ranks are 4096.

## Certificate format

Each prefix is `Q5_T63_RANK_orbit_XX`, for XX=00 through 06.
All records use unsigned bytes and all bit matrices use low-bit-first
order within each byte. The prefix files are:

- `_forests.bin`: 4096 records of 32 bytes, sixteen short edge pairs.
- `_pairs.bin`: 4096 records of 26 bytes, thirteen endpoint pairs.
- `_columns.bin`: 4096 records of 26 bytes, thirteen arbitrary matching pairs.
- `_matrix.bin`: 4096 records of 512 bytes, connectivity matrix rows.
- `_pivots.bin` and `_combos.bin`: 4096 records of 512 bytes; pivot j
  has highest set bit j and equals the XOR of matrix rows selected by combo j.
- `_config.txt` and `.json`: exact H/U and producer rank metadata.

An independent verifier must check every forest, derive its endpoint
pairing, check every column, reconstruct all 16777216 connectivity bits
for each row of the geometry table, and verify rank with exact binary
arithmetic. Stored rank metadata alone is not evidence of a completed
check. The source generator is a separate parameterized copy of the
earlier T26 generator, with N=26, rank bound 4096, H-size six, U-size
three and sixteen short edges. No frozen T26 source was modified.

## Actual Q6 application

Start from the 4096 residual geometries independently accepted in
`Q5_T26_RANK_BATCH_REVIEW.json`; no producer-only universe is assumed.
Apply the accepted uniform transfer for rows $(a,b)=(4,2)$ or $(1,5)$.
In the first row choose three even hole sources in A. In the second
choose three odd sources excluding the mirror of the root. The A
completion has balanced four holes and hence its endpoint input is
already accepted. The B input has six same-parity holes, with exactly
the three mirror holes omitted. Its required matching may be arbitrary.

If that actual marked $(H_B,U_B)$ is a common automorphic image of a
row in the table, the new local theorem applies. Expand the transferred
paths and remove the tag as in the accepted uniform transfer. This
preserves every original short matching edge for every realization of
the geometry. Zero original crossing is handled by the same accepted
five-direction import. These steps introduce no additional matching
restriction or unsatisfied omission condition.

The producer `Q5_T63_RANK_coverage.py` enumerates all six cuts and legal
source triples, recording an actual marked witness for each accepted
record. It uses common translation by an omitted hole and coordinate
permutation to normalize both H and U together. Its counts are:

| target | input | newly covered | remaining |
|---:|---:|---:|---:|
|1|910|330|580|
|7|1476|693|783|
|31|1710|720|990|
|total|4096|1743|2353|

These are geometry counts uniformly covering all realizing matchings.
They require independent exact witness and residual-byte checks before
ledger acceptance. Other new T15/T17 routes may overlap and must be
combined by exact sets, not by adding these counts. Full ten-hole and
P6 remain open.
