# Fifty-five marked T37 inputs certified by short-forest rank

2026-11-01. ARIS proof-writer. Status: PROVABLE AS STATED conditional on
the explicit finite certificate checks below; independent review pending.

## Exact claim and scope

Let H be the union of the minority and majority sets in a row of
`Q5_T37_INDEPENDENT_summary.json` with `full_rank=true`, and let U be
that row's omitted set. For every perfect matching F of the complete
graph on K=V(Q5) minus H, there is a simple cycle on exactly V(Q5) minus U
containing F, whose edges outside F are cube edges. The conclusion also
holds for every common cube automorphic image of (H,U).

There are exactly 55 claimed rows, indices 4,5,7,8,9,10,11 and 16 through
63. Every H has ten vertices, split 3:7 by parity, and U consists of two
majority vertices. Required matching edges need not be short or bipartite.
The nine other indices 0,1,2,3,6,12,13,14,15 are OPEN. Their deficient
producer ranks are neither counterexamples nor negative classifications.
This statement is not full T37, full twelve-hole Q6, or full P6.

## Proof from the finite witnesses

Fix a claimed row. There are 22 covered endpoints K and eight included
holes H minus U. Each supplied S has nineteen distinct cube edges,
degree one at every K vertex, degree two at every included hole, zero
degree at U, and no cycle. Thus S consists of eleven vertex-disjoint
paths covering all thirty retained vertices. Write P(S) for the perfect
matching of K obtained by pairing their endpoints.

Let H_K be the binary matching-connectivity matrix indexed by all
perfect matchings of the complete graph on K: entry (P,F) is one iff
their labelled multigraph union is a single alternating cycle. By
Cygan--Kratsch--Nederlof, Corollary 3.5 (GF(2)), its rank is
2^(22/2-1)=1024. The precise primary-source import is recorded in
`A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md`; see
https://arxiv.org/abs/1211.1506 and DOI 10.1145/3148227.
The bound applies to arbitrary complete-graph perfect matchings.

For this row, 1024 legal forests S_i and 1024 arbitrary perfect matching
columns X_j are supplied. Their connectivity submatrix has exact GF(2)
rank 1024, as verified by the checks below. Consequently the corresponding
complete rows H_K[P(S_i),:] span the whole row space of H_K.
Every column of H_K is nonzero: if F={(a_i,b_i):1<=i<=11}, the pairing
{(b_i,a_(i+1)):1<=i<=11}, with cyclic indices, is connected with F.
Therefore not all selected rows can vanish at F. Choose S_i with
P(S_i)+F a single cycle. Expand its eleven pairing edges back to the
vertex-disjoint paths of S_i. This gives the stated thirty-vertex cycle.
No physical required edge can be duplicated: a common pair in F and
P(S_i) would constitute an isolated labelled two-edge component on K,
contradicting connectedness on 22 endpoints. All added edges are short.

This proof needs only the selected positive forests. It does not require
an exhaustive forest search, a complete automorphism classification, or
any interpretation of unsuccessful searches.

## Frozen finite obligations and file format

Each claimed row has prefix `Q5_T37_INDEPENDENT_orbit_XX` matching its
two-digit index in the summary. Endpoints are actual Q5 vertices 0..31.
All listed records are unsigned bytes. Matrix bits are little-bit-first.

- `_forests.bin`: 1024 records of 38 bytes (nineteen edge pairs).
- `_pairs.bin`: 1024 records of 22 bytes (eleven endpoint pairs).
- `_columns.bin`: 1024 records of 22 bytes (eleven matching pairs).
- `_matrix.bin`: 1024 records of 128 bytes.
- `_pivots.bin`, `_combos.bin`: 1024 records of 128 bytes. Pivot j has
  highest set bit j and is the XOR of matrix rows indicated by combo j.
- `_config.txt` and `.json`: geometry and producer metadata.

The checker must independently verify all forest degrees, short edges,
absence of cycles and omissions, derive each endpoint pairing, validate
each column, reconstruct all 1,048,576 connectivity bits per geometry,
and verify binary rank 1024. Producer metadata is not a substitute.
Across 55 rows this is 56,320 forests and 57,671,680 connectivity bits.
The source uses N=22, R=1024, ten holes, two omissions and nineteen short
edges. Frozen earlier sources were not changed.

`Q5_T37_INDEPENDENT_geometry.py/.json` records a supplementary 64-orbit
classification when the eight included holes are independent: normalize
one minority vertex to zero, then its three-vertex set under cube
automorphisms, then normalize (majority,U) jointly under the minority
stabilizer. That exhaustive classification is not needed for the 55
positive local claims; it also does not imply closure of the other nine.

## Dependency boundary

This local proof depends on the primary matching-connectivity rank
bound and the frozen finite witnesses, not on any new Q6 residual count.
Applications to Q6 require separate verification of their actual cut,
source selection, simultaneous (H,U) identification and uniform transfer.
In particular a local rank certificate alone does not close twelve holes.
