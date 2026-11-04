# 111 marked Q5 local inputs from full-rank forest certificates

2026-11-01. ARIS proof-writer candidate. Independent review pending.

## Exact statement

For each index in `TWELVE_NEW_TYPES_greedy_registry.json`, take its exact
minority set, majority set and marked omissions U from the corresponding
row of `TWELVE_NEW_TYPES_summary.json`; put H=minority union majority.
For EVERY perfect matching F of the complete graph on K=V(Q5) minus H,
there exists a simple cycle on exactly V(Q5) minus U containing F, with
every edge outside F a cube edge. Every common cube automorphic image
of (H,U) has the same conclusion. Required edges may be long or join
vertices of the same parity. There are precisely111 claimed marked inputs.

| type | minority/majority holes | omitted majority holes | endpoints | rank | short forest edges | cycle vertices |
|---|---:|---:|---:|---:|---:|---:|
|T28|2/8|3|22|1024|18|29|
|T19|1/9|4|22|1024|17|28|
|T84|0/8|4|24|2048|16|28|
|T105|0/10|5|22|1024|16|27|

Only these explicit marked inputs are asserted, not all inputs of any
type. Other successful producer rows and deficient ranks are not imported.
The greedy choice is merely a way to select useful claims; its optimality
or global coverage is not a premise of the local theorem.

## Uniform proof

Fix a claimed row and write n=|K|, r=2^(n/2-1). Each supplied short forest
S has degree one at every K vertex, degree two at every included hole
H minus U, no omitted vertex and no cycle. It therefore consists of n/2
vertex-disjoint paths covering every retained vertex. Its endpoint
pairing P(S) is a perfect matching of K.

The complete matching-connectivity matrix H_K on all complete-graph
perfect matchings of K has GF(2) rank r by Cygan--Kratsch--Nederlof,
Corollary3.5 (arXiv1211.1506, DOI10.1145/3148227). The exact general
primary-source import, without a bipartite restriction, is documented in
`A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md` and already used at both n=22
and n=24 in accepted local certificates.

The supplied r forests and r arbitrary matching columns X_j have a
connectivity submatrix of exact binary rank r. Hence the complete rows
H_K[P(S_i),:] span the full row space. For an arbitrary prescribed F its
column is nonzero: orient its n/2 edges as (a_i,b_i), then pair b_i to
a_(i+1) cyclically. This gives a matching connected with F. At least one
selected P(S_i) must therefore also be connected with F.

Expand that endpoint pairing back to its short forest paths. The resulting
graph is a single simple cycle on all retained vertices and contains F.
An original required edge cannot duplicate a forest edge: a common pair
of F and P(S_i) would be an isolated labelled two-edge component of the
matching union, impossible because n>=22 and the union is connected.
All nonrequired physical edges come from S_i and are short. This proves
the claimed local theorem under exactly the finite checks below.

## Certificate obligations and independence boundary

Every selected index has prefix `TWELVE_NEW_TYPES_orbit_XXX`, with
three decimal digits, and geometry/type as specified in the registry.
All vertex records are unsigned bytes. Every pairing/column record has
n bytes, listing n/2 actual vertex pairs. Each forest record has twice
the short-edge count in the table. All binary matrix records have r/8
bytes, with bit order little-bit-first.

- `_forests.bin`: r short forest records.
- `_pairs.bin`: r endpoint pairing records.
- `_columns.bin`: r arbitrary matching records.
- `_matrix.bin`: r connectivity rows.
- `_pivots.bin` and `_combos.bin`: r rows; pivot j has highest set bit j
  and equals the XOR of matrix rows selected by combo j.
- `_config.txt` and `.json`: exact input and producer metadata.

A checker must validate every short forest edge, vertex degree, omitted
vertex and absence of cycles; independently derive its pairing; validate
all columns; reconstruct every connectivity bit; and check rank over
GF(2). Stored producer ranks alone are not a proof. The selected finite
certificates do not require exhaustion of the forest generator or the
actual Q6 geometry domain.

`TWELVE_NEW_TYPES_LOCAL_MANIFEST.json` binds exactly these111 positive
families and their source registry. The application to the215243 Q6
geometries has a separate proof and acceptance gate. No Q6 coverage count,
complete twelve-hole theorem, or full P6 is asserted by this local proof.
