# Conditional sixteen/eighteen-hole reuse and positive Hall reductions

2026-11-02. ARIS proof-writer candidate; independent checking pending.

## Exact claim and dependency boundary

Assuming the complete fourteen-hole prescribed-endpoint theorem, the
sixteen-hole problem reduces to 1,211 covered-target geometries. Assuming
the complete sixteen-hole theorem, the eighteen-hole problem reduces to
150 covered-target geometries. Both reductions leave no free-target
geometries. Neither predecessor assumption nor either full layer is proved
by this document. The finite application and exclusions also await fresh
independent verification.

The starting source streams are the already reviewed
`HIGHER_Q5_FULL_residual_h{16,18}_v{1,7,31}_{covered,free}.bin` files.
Their use as complete remaining domains has the preceding-layer condition
stated in HIGHER_Q5_FULL_NEARBALANCED.md. Records consist of sorted Z(k-1)
then W(k), with root0, 2k holes and the named opposite-parity target.

## Reused universal local inputs

The registry is exactly the FOURTEEN_REUSE accepted registry plus the twenty
new local inputs explicitly accepted by FOURTEEN_CACHED_REVIEW. The latter
are ordinary universal local cycle inputs. Their 47,015 normalized keys
transport minority, majority and omitted vertices by one common cube map.
The old packed T26/T15/T17/T63 registries and analytical T44/T15/T63 split
routes are unchanged. The fresh reviewer must reconstruct this union from
the accepted marked inputs, not merely trust a generated lookup file.

For each original geometry, try all six target-facing cuts and all legal
source subsets. In the even row s=a+1-b, the B local hole counts are
(k-a-1,k-b+s); in the odd row s=b-a-1 they are (k-b,k-a-1+s).
The omitted vertices are the mirrors of the sources. Odd sources exclude
the root mirror and a free target. Every mirror is an originally covered
vertex. The full balanced Q5 endpoint theorem supplies the A completion,
including arbitrary artificial matching edges and prescribed endpoints.
The already accepted generic transfer then applies for each k. Forced
single-pair inputs retain all generic hypotheses, including s>=3 and root
not among the obstruction endpoints. No new root-in-obstruction route or
unreviewed local rank input is used.

Each positive record is certified by the original 32-byte witness format:
uint32 source index; uint8 cut/family; uint16 exact local ID; uint64 actual
source mask; uint32 minority/majority/omitted masks and forced endpoint
mask. The finite checker must independently check every actual projection,
lookup, root/target restriction, and complete byte partition. These
geometrical witnesses establish a route for every realizing original short
matching, with its A completion and paths allowed to depend on that matching.

## Positive impossibility exclusions

The subsequent Hall witnesses use the 22-byte `<BBIQQ` format: target,
free-target flag, source index, S and T masks. For 2k holes, the covered
parity classes each have 32-k vertices. Each S is a nonempty subset of the
covered even class; T is its entire covered odd neighborhood, and
|T|<|S|. Any original short matching would inject S into T. Thus that input
is unrealizable. No maximal-matching search result is itself a premise.
Retained inputs carry no automatic realizability claim.

## Exact producer counts, pending audit

| Layer and target | Initial covered | After reuse | Hall exclusions | Final covered |
|---|---:|---:|---:|---:|
|16,1|725370|4290|4190|100|
|16,7|834303|5760|5469|291|
|16,31|912495|8150|7330|820|
|18,1|22260|2040|2040|0|
|18,7|27735|2400|2400|0|
|18,31|30810|2760|2610|150|

Sixteen-hole free inputs 42,846 (0/15,786/27,060) all have positive reuse
witnesses. The eighteen-hole source has zero free inputs. The sixteen-hole
total source is 2,515,014; reuse covers 2,496,814 and leaves18,200; Hall
excludes16,989 and leaves1,211. The eighteen-hole source is80,805; reuse
covers73,605 and leaves7,200; Hall excludes7,050 and leaves150.

The generated scanners differ from the original fourteen-hole producer in
hole-count/record-width parameters, source/output filenames and the expanded
accepted registry. This is an implementation description, not a proof of
correctness. Independent audit must specifically rule out unchanged hardcoded
fourteen-hole bounds and must bind all inputs, witnesses and complements.
Full Q6/P6 remains OPEN.
