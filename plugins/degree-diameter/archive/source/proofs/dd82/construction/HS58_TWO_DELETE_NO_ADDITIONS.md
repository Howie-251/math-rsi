# HS50 to order 58 with exactly two deletions: already excluded

Date: 2026-10-12. Status: previously closed family located during the
requested initial check. No new graph experiment, enumeration, SAT,
optimization, or independent review was started.

The existing proof is the section **“Addendum: deletion-only HS
extensions to order 58”** in
[CONSTRUCTION_CASE_STUDY_ACTIONS_20261011.md](CONSTRUCTION_CASE_STUDY_ACTIONS_20261011.md).
Its equation (4) excludes every deletion-only case with one through five
deleted original edges. The result is also explicitly indexed as item 5
in [HOFFMAN_SINGLETON_AUGMENTATION.md](HOFFMAN_SINGLETON_AUGMENTATION.md).
Thus the present exactly-two-deletion family is already covered.

For clarity, specializing that existing bound gives the precise
obstruction. A hypothetical target is eight-regular; with two old edges
deleted and no old-old additions it has 54 old-new incidences and an
eight-vertex auxiliary graph H with five edges. Its 28 new-vertex pairs
can be covered by at most

\[
|E(H)|+\sum_a\binom{d_H(a)}2+
\sum_v\binom{1+r_v}2
\le 5+\binom52+4+\binom22=20.
\]

Here r_v is the deleted degree at old vertex v. The shared-old term is
five for adjacent deletions and four for disjoint deletions, so even
this upper bound is generous in the disjoint case. Overlapping witnesses
can only reduce actual coverage. The contradiction requires no
automorphism or embedding classification.

The same companion note already records that each deleted edge breaks
thirteen old-pair routes and forces the corresponding attachment rows
to intersect. Those additional necessary constraints cannot rescue a
family already failing the new-new coverage count. They were not
re-enumerated here.

No actual 58-vertex candidate was generated in this task. The result is
a provenance record for an existing restricted-family theorem, not a
new exclusion of arbitrary order-58 graphs.
