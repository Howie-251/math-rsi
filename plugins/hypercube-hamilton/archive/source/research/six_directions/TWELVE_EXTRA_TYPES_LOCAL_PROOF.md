# Eleven additional marked Q5 local inputs

2026-11-01. ARIS proof-writer candidate. Independent review pending.

## Exact statement

Use precisely the eleven indices in `TWELVE_EXTRA_TYPES_greedy_registry.json`:
0,3,5,51,77,183,32,18,58,52,12. For each, take its exact marked minority,
majority and omitted sets in `TWELVE_EXTRA_TYPES_summary.json`, and put
H=minority union majority and K=V(Q5) minus H. For EVERY perfect matching
F of the complete graph on K, there is a simple cycle on exactly
V(Q5) minus U containing F and adding only cube edges. The same holds
for all common cube automorphic images of (H,U). Matching edges may
be long or same-parity. The exact hole and omission sets matter.

The first ten listed indices are T26 (2:6 holes, two majority omissions).
Index12 is T17 (1:7 holes, three majority omissions). All have24 covered
endpoints. No unrestricted T26/T17 claim or old-registry extrapolation
is made. The remaining producer rows are not premises of this theorem.

## Proof

For each claimed row, the certificate supplies2048 forests S_i of short
edges on the retained vertices. They have degree one at K, degree two
at H minus U, and no cycles. A T26 forest has18 edges and covers30
vertices; a T17 forest has17 edges and covers29 vertices. Each is the
disjoint union of twelve paths, with endpoint pairing P(S_i) on K.

The complete matching-connectivity matrix on all complete-graph perfect
matchings of K has GF(2) rank2^(24/2-1)=2048 by Cygan--Kratsch--Nederlof,
Corollary3.5. The general primary theorem and version are recorded in
`A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md` (arXiv1211.1506,
DOI10.1145/3148227). It has no bipartite restriction on the matchings.

The2048 supplied forests and2048 arbitrary matching columns yield a
connectivity submatrix of exact binary rank2048. Thus their complete
rows span the full matching-connectivity row space. Every column F is
nonzero: orient the twelve F edges and join the end of each to the start
of the next cyclically. Therefore some selected P(S_i) is connected with
the arbitrary required F. Expand its paths to obtain one cycle on all
retained vertices. A common required/forest physical edge would give
an isolated labelled two-edge component of P(S_i)+F, impossible on24
endpoints in a connected union. All new physical edges are short.

This proves the exact local claim subject to the finite checks below.
Exhaustiveness of the producer search, the complete geometry census and
the greedy selection algorithm are not dependencies of this local proof.

## Finite certificates

Prefixes are `TWELVE_EXTRA_TYPES_orbit_XXX`, using the selected index.
There are2048 records per file. Forest records contain36 bytes for T26,
34 bytes for T17. Pairings and matching columns contain24 vertex bytes.
Matrix, pivot and combo rows contain256 bytes, little-bit-first.
The respective suffixes are `_forests.bin`, `_pairs.bin`, `_columns.bin`,
`_matrix.bin`, `_pivots.bin`, `_combos.bin`, `_config.txt`, and `.json`.

The independent checker must reconstruct all short forests and endpoint
pairings, validate every column, recompute every connectivity bit, and
verify binary rank2048. Metadata is insufficient. Totals are22528 forests
and46137344 connectivity bits. The frozen existing T26/T17 generator
sources are reused with new prefixes and inputs; none was modified.

Q6 application and the exact remaining domain require a separate review.
This local theorem alone closes no complete Q6 hole layer. Full twelve-
hole and P6 remain OPEN.
