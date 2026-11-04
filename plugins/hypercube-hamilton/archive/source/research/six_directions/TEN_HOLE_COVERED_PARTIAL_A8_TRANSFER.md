# Ten-hole covered targets using the accepted partial A8 and K8 inputs

2026-11-01. ARIS proof-writer. Proposed sufficient classes; independent
review pending. This is not full ten-hole P6.

## Domain and imports

Let M be any short 27-edge matching of Q6, u a free root, and v a covered
target of opposite parity. Normalize u=0. Its other even holes Z have size4,
and its odd holes W size5. If Z-W has a short edge, add it and apply full
eight-hole P6; assume henceforth that Z union W is independent.

Use the notation A,B,a,b,delta,c of HIGHER_HOLE_UNIFIED_TRANSFER.md.
The target v is in A. For c=0 the imported five-direction theorem applies.
The accepted inputs are the complete eight-hole theorem, the accepted
uniform transfer and its original eight ten-hole rows, the 24 complete
marked T15 cores and full T15 split case, Q5 K8 from Q5_K8_REVIEW, and
the partial A8 results accepted in A8_PARTIAL_REVIEW and
A8_DELTA4_FIRST_ORBIT_REVIEW. No complete A8 is imported.

Call a marked Q5 geometry (minority set L of size3, majority set J of size5,
omitted hole y in J) admissible if either of these conditions holds:

1. a coordinate face containing y has majority-minus-minority count 1,2,3;
2. a coordinate face containing y has all five majority holes and one minority.

In the applications below L and J minus y are nonadjacent, as they come
from the original independent Z,W. The two audited partial A8 theorems
therefore provide the required 31-cycle for every arbitrary matching on
the complement of each admissible marked geometry.

## Local endpoint conversion

Suppose F is any matching of K(Q5) with four holes of each parity,
r is an even hole, and y is a covered odd vertex. Write h=F(y) and form
F'=F-yh+hr. Its holes are the old holes minus r plus y. If this marked
3:5 geometry, omitting y, is admissible, partial A8 gives its 31-cycle.
Delete hr and append the original edge hy at h. This gives a Hamilton
r-y path preserving F with short new edges. This works for every h and
does not require knowing the mate h from the hole geometry.

## Six additional cut rules

All coordinates in a local admissibility test are the five coordinates
other than the original Q6 cut. All parities below are global parities.

* (a,b)=(0,1): use the uniform no-bridge transfer. A needs the accepted
  balanced-two-hole endpoint theorem; B has four holes of each parity,
  after the tagged closure consumes the root if necessary. Apply K8.
* (1,1): let z be the unique Z hole in A and let y be its mirror in B.
  Use one even-hole bridge. A needs the two-hole endpoint theorem.
  The B hole geometry is minority Z intersect B (three vertices),
  majority (W intersect B) union {y} (five vertices), omitted y.
  This cut succeeds whenever that actual geometry is admissible.
* (0,2): choose w in W intersect A with mirror y different from u.
  At least one choice exists. Use one odd-hole bridge. The B geometry
  has minority W intersect B, majority (Z intersect B) union {y},
  omitted y. Its admissibility suffices.
* (3,4): use no bridges. The A completed matching has balanced eight holes.
  In the local endpoint conversion, the root is removed and v added,
  leaving minority Z intersect A and majority (W intersect A) union {v}.
  If this geometry omitting v is admissible, the required A path exists;
  B needs only its already accepted balanced-two-hole cycle theorem.
* (4,4): choose z in Z intersect A as the even bridge source. The A endpoint
  conversion has minority (Z intersect A) minus {z}, majority
  (W intersect A) union {v}, omitted v. Its admissibility suffices.
  B has exactly two odd holes, one the bridge mirror; use N14 avoiding it.
* (3,5): choose w in W intersect A whose mirror differs from u.
  The A endpoint conversion has minority Z intersect A, majority
  ((W intersect A) minus {w}) union {v}, omitted v. Its admissibility
  suffices. B has two even holes; N14 omits the bridge mirror.

These are complete statements for every matching realizing each eligible
geometry, not just for a sampled matching. The choices of z,w and a local
admissibility cut depend only on the original marked hole geometry.

## Endpoint and forest bookkeeping

For the first three rows, the accepted uniform transfer applies directly;
only its precise B input is replaced by the new accepted theorem.

For the last three rows, repeat its completion D and bridge construction.
If delta=1, the A root r is u. If delta=0 and there is no even bridge,
it is an even crossing port, which exists by the port imbalance. If delta=0
in row (4,4), it is the chosen even bridge source z. In all three cases
the completed A matching has four holes of each parity, and removing r
and adding v leaves exactly the geometry displayed above. This equality
does not depend on the chosen artificial D or crossing port.

The covered global target v stays covered in the completed A matching:
an internal original edge covers it, or it is an odd crossing port paired
by D. It cannot be the even root, nor an original free bridge source.
Thus the local endpoint conversion applies. Once the A path is supplied,
all remaining steps of the uniform transfer are unchanged: remove D,
attach original crossings and the optional single bridge, join the global
endpoints by a tagged edge, compress the forest and its bridge conflict,
apply the stated B theorem, expand, and remove the tag. The root/target
degrees, preservation of every original matching edge, and shortness of
all surviving new edges follow from that already audited bookkeeping.

## Exact finite coverage task

The independent census should enumerate all Z of four nonzero even Q6
vertices, and all W of five odd vertices nonadjacent to Z, for normalized
covered target v=1,7,31 with v outside W. For every input it tests the
eight old basic rows, all actual accepted T15 projections, and the six new
rules above. Any remaining input stays OPEN.

The producer chain gives 145248180 eligible covered-target geometries,
121690 remaining after the old rows and conservative T15 lookup, and
91225 after the new rules (26880,29955,34390 at targets1,7,31). These numbers
are unaudited producer evidence until independently reconstructed.
No feasibility exclusion was used for the ten-hole final remainder.

Relevant producer files are higher_hole_geometry_census.cpp,
higher_hole_t15_lookup.py, higher_hole_t15_filter.cpp, and
ten_covered_partial_a8_filter.cpp. No unrestricted same-face T15 shortcut
is used by that conservative lookup. The exact remaining bytes are in
ten_covered_after_partial_a8_v1.bin, v7.bin, and v31.bin.

Even after this partial coverage is audited, the remaining geometries
still require proofs for all their realizing matchings. No complete ten-
hole covered-target, A8, A10, or P6 conclusion is asserted.
