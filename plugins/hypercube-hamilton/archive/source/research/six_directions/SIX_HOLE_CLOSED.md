# Complete six-hole P6 consequence

Date: 2026-11-01. Status: PROVABLE AS STATED relative to the explicitly
imported source theorems and verified finite certificates. Semantic audit
assurance remains same-family/provisional. Full P6 remains unproved.

## Theorem

Let $M$ be any matching of the short-edge graph $Q_6$ with exactly six
uncovered vertices (equivalently, $|M|=29$). For every uncovered root $u$
and every vertex $v$ of the opposite parity, there is a Hamilton $u$--$v$
path containing every edge of $M$.

## Proof and dependency discharge

`CANONICAL_A4_CLOSURE.md` proves full Q5 A4, with its canonical family
closed by the finite completion lemma and safe/occupied-endpoint transfers.
`CANONICAL_COMPLETION_REVIEW.md/.json` independently checks the finite
tables, forward completion enumeration, both transfers, and their inputs.
The proof has no remaining assumption of A4, E3, or P6.

If $v$ is uncovered, apply C6-free in `SIX_HOLE_FREE_REDUCTION.md`, now
discharging its A4 assumption with the preceding theorem. If $v$ is
covered, apply C6-covered in `SIX_HOLE_COVERED_REDUCTION.md`, discharging
the same assumption. These are the only two possibilities for $v$.
Both results quantify over every six-hole short matching, every free root,
and all corresponding opposite-parity targets. Their auxiliary K4/S7/S9
inputs are recorded in `SIX_HOLE_MIXED_AND_GEOMETRY.md` and the same
covered/free proof packages; their A4 dependencies are now discharged.
The original conditional audits are preserved unchanged, and the new
closure audit checks this downstream dependency direction for circularity.

Thus the statement holds for all required endpoints. This proof does not
rely on the old sample lists or on enumerating only the previously observed
six-hole geometries.

## Root-preserving augmentation corollary

If an original Q6 short matching can be augmented by short matching edges,
while leaving the specified root free, to a matching with at least 29 edges,
then its required P6 path exists. The augmented matching has at most 31
edges because the root remains free; its hole count is therefore 2,4 or6.
Use the corresponding already established full endpoint theorem, and keep
the same Hamilton path after forgetting the extra matching requirements.

## What remains for full P6

The root-preserving maximal reduction has at most 18 holes. The complete
2-,4-,6-hole levels are now established at the stated assurance level.
The 8,10,12,14,16,18-hole levels still require full endpoint proofs. Neither
the six-hole theorem nor the augmentation corollary proves those levels.
The user goal remains active and full_p6_proved must remain false.
