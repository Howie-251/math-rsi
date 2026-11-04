# A8 consequences: full balanced-eight-hole endpoints and ten-hole progress

2026-11-01. ARIS proof-writer. Acceptance requires complete A8 final PASS
and a separate review of these consequences. Full ten-hole P6 remains open.

## 1. Exact endpoint theorem

Let F be any matching of K(Q5) with four holes of each parity. For every
free root r and every opposite-parity vertex y, covered or free, there is
a Hamilton r-y path containing F, with all edges outside F short.

If y is free, add the auxiliary edge ry. The resulting matching has three
holes of each parity. The already accepted K6 full-cycle theorem applies
even when ry is long, since its required matching edges are arbitrary.
Delete ry from that cycle to obtain the desired path.

If y is covered, put h=F(y) and F'=F-yh+hr. Its holes are the old holes
minus r plus y, with counts3:5 and y a majority hole. Complete A8 gives
a cycle on exactly Q5-y containing F'. Delete hr and append the original
edge hy at h. This is a Hamilton r-y path restoring all original edges.
The auxiliary edge hr disappears and all other new edges are short.

This theorem includes every possible mate h and every arbitrary complete-
graph matching, so it is suitable for the long edges created by Q6 path
compression. It fills the prescribed-covered-target part that K8 alone
did not supply. Taking y to be a short neighbor of r and closing the path
also gives a full cycle; K8 had already been independently established.

## 2. Six unconditional ten-hole cut rows

For a Q6 short27-edge matching, free root u=0 and covered odd target v,
use Z,W,A,B,a,b from TEN_HOLE_COVERED_PARTIAL_A8_TRANSFER.md. After the
standard short augmentation, Z union W is independent. The six rows

$$ (0,1),(1,1),(0,2),(3,4),(4,4),(3,5) $$

are now sufficient without any additional local marked-geometry test.
The first row uses K8, the next two use complete A8 at the bridge mirror,
and the final three use the full balanced-eight-hole endpoint theorem
above. All completion, root selection, optional bridge, tagged closure,
conflict suppression and expansion steps are exactly those already
audited in TEN_HOLE_COVERED_PARTIAL_REVIEW. The only former additional
hypothesis was membership in the accepted partial A8 geometries; complete
A8 removes that hypothesis for every marked geometry arising in these rows.

The existence of an admissible bridge source remains automatic where
required: among two or five original odd holes at most one mirrors to the
root, and v is covered so it is not one of those sources. Required matching
edges are preserved, and both the free root and covered target remain the
prescribed global endpoints.

## 3. Exact additional coverage obligation

The accepted TEN_HOLE_COVERED_PARTIAL_REVIEW fixed the remaining covered-
target domain at91225 normalized geometries (26880,29955,34390 for
v=1,7,31). Its frozen independent residual files are the inputs here.
For every record, test all six actual cuts for one of the six rows above.
If such a cut exists, Section2 supplies a path for every matching realizing
that geometry. Keep every other record unchanged as an open obligation.

The producer ten_covered_after_full_A8.py records every chosen row/cut and
the exact remaining input bytes. Its predicted additional coverage is37003,
leaving54222 (16920,17022,20280). These are complete hole-geometry counts,
not numbers of sampled matchings. A separate independent enumeration and
fixed-input hash check are required before accepting these exact counts.

## 4. What this does and does not establish

Complete A8 supplies a reusable local endpoint theorem and expands the
accepted ten-hole covered-target domain. The remaining54222 geometric
cases, once independently confirmed, still need universal matching proofs.
Multiple-omission local cycle inputs and b=0 exposed-port cases are not
automatically covered by A8. Full A10, complete12--18-hole Q6 layers and
full P6 remain open. No claim of mathematical novelty is made here.
