# Complete quotient profile of at most four orbit replacements

The single bounded profile completed all 5,249,475 parameter choices.
Although 165,915 choices satisfy the diagonal, row-type and nonnegative
quotient-defect conditions, every one has twelve internal cycles. That
entire voltage family is already excluded by
[CYCLIC5_K66_QUOTIENT_EXCLUSION.md](CYCLIC5_K66_QUOTIENT_EXCLUSION.md).
There are zero surviving choices with any independent vertex orbit.

Consequently no target can be obtained from the actual twenty-bad-pair
seed by deleting at most four selected C5 edge orbits and inserting the
same number of new ones, while preserving its given twelve-orbit C5
action. Any successful repair in this invariant domain must replace at
least five selected edge orbits. This is a finite neighbourhood result,
not an exclusion of the entire twelve-orbit domain or of arbitrary
60-vertex graphs.

Source:
[cyclic5_four_orbit_quotient_profile.cpp](../../../computations/dd82/construction/cyclic5_four_orbit_quotient_profile.cpp),
[runner](../../../computations/dd82/construction/cyclic5_four_orbit_quotient_run.py).
Actual data:
[profile.json](../../../computations/dd82/construction/cyclic5_four_orbit_quotient_run/profile.json),
[resources.json](../../../computations/dd82/construction/cyclic5_four_orbit_quotient_run/resources.json).

## Actual input and finite domain

The input is the verified C5 representation of the **twenty-bad-pair**
graph in
[cyclic5_twelve_orbits60_signature_lift_run/seed20](../../../computations/dd82/construction/cyclic5_twelve_orbits60_signature_lift_run/seed20/).
It is not the old fifty-bad-pair seed. Its selected edge-orbit set has
48 members: twelve internal cycles and 36 cross-orbit matchings. Its
degree quotient is 2I+A(K6,6), with the two parts

\[
 \{0,2,5,7,9,10\},\qquad\{1,3,4,6,8,11\}.
\]

The exact selected orbit IDs, endpoint pairs and shifts are retained in
[input.txt](../../../computations/dd82/construction/cyclic5_four_orbit_quotient_run/input.txt).
The profile did not search or modify their voltages.

Every target with this C5 action has at least two independent orbits,
by the cited pure proof. Therefore it must delete at least two of the
seed's twelve internal edge orbits. The profile selects four distinct
old orbits for deletion, with at least two internal ones. The counts are

| Internal / cross orbits deleted | Deletion sets |
| --- | ---: |
| 2 / 2 | C(12,2) C(36,2) = 41,580 |
| 3 / 1 | C(12,3)·36 = 7,920 |
| 4 / 0 | C(12,4) = 495 |
| Total | 49,995 |

For each deletion set, retain its eight quotient endpoint occurrences,
including both occurrences contributed by an internal orbit. All 105
perfect matchings of these eight labelled occurrences are generated
recursively, using the least unmatched occurrence and every possible
partner. Each pairing gives four new quotient edges. Repeated vertex
labels may give duplicate parameterizations of a quotient matrix; the
profile keeps these counts and does not claim graph or matrix uniqueness.
Repeated quotient edges are allowed.

The resulting degree quotient always has row sum eight. A new quotient
loop adds two on the diagonal, while a nonloop adds one in each symmetric
off-diagonal position. Thus the parameter domain contains exactly
49,995·105=5,249,475 choices.

## Candidate preservation for the “at most four” scope

Let S be the seed's 48 selected edge orbits and T any target's 48 selected
edge orbits for the same action. Suppose |S\T|=|T\S|≤4. There are at
least two original internal orbits in S\T, since at least two target
orbits must be independent. Extend S\T to a four-element subset D of S
by including orbits that remain selected in T. Reinsert those extra
deleted orbits along with T\S. This describes T as deleting four old
orbits, at least two internal, and adding four.

Because both S and T have weighted quotient degree eight at every
vertex, the deleted and added quotient edges have the same multiset of
eight endpoint occurrences. Their new pairing occurs among the 105
pairings examined. Thus padding with reinserted old orbits loses no
target at distance less than four.

The quotient profile intentionally forgets voltages. For an off-diagonal
quotient pair there are five different matching shifts; an internal
pair has two cycle shifts. Requiring the final multiplicities to fit
these capacities is sufficient for assigning some simple edge orbits
while retaining the undeleted ones. In particular, the stronger final
diagonal requirement zero or two permits at most one internal cycle.
Every actual target maps into this necessary quotient domain, even
though most surviving quotients need not have diameter-two voltages.

## Necessary filters and actual counts

The program applies the following stages in order:

1. Diagonal entries must be zero or two, and off-diagonal entries at most
   five, respecting simple edge-orbit capacity.
2. Every row must have one of the seven necessary types proved in
   [the general quotient note](CYCLIC5_ORBIT_SWITCH_AND_QUOTIENT.md):
   for diagonal two, external multiset 1^6 or 2,1^4; for diagonal zero,
   external multiset 2^2,1^4; 2^3,1^2; 2^4; 3,1^5; or 3,2,1^3.
3. Compute every entry of D=M²+M−7I−5J and require D≥0.

For choices passing all three stages, the program separately records
the number of independent orbits. This makes explicit which results
are already closed by the zero/one-independent-orbit theorem.

| Stage | Parameter choices retained |
| --- | ---: |
| Raw pairings | 5,249,475 |
| Diagonal and orbit capacities | 5,083,155 |
| Seven row types | 1,195,155 |
| Nonnegative full quotient defect | 165,915 |
| Of these: zero independent orbits | 165,915 |
| Of these: one or more independent orbits | 0 |
| Target-relevant choices with at least two independent orbits | 0 |

The computation finished every deletion set and every pairing; the
complete flag is true and the stop reason is `full_domain_exhausted`.
All 165,915 numerical quotient survivors belong to the already excluded
all-internal-cycle domain. They are not new feasible targets. Therefore
there is no target-relevant matrix to save among the allotted first
twenty distinct matrices, and no new complete graph or BFS run is needed.
No voltage SAT or voltage enumeration was launched.

## Additional useful necessity: the off-diagonal support has a triangle

For completeness, the proposed triangle necessity follows directly from
the same proved row and defect conditions. Let a be an independent orbit,
which every target has, and suppose the off-diagonal support of M is
triangle-free. Then for any adjacent quotient pair a,b, there is no
common quotient neighbour, so

\[
 D_{ab}=(r_a+r_b+1)q_{ab}-5.
\]

If r_b=0, this is q_ab−5<0, since independent-orbit rows have q≤3.
Hence every neighbour b of a has r_b=2. Such interfaces have q≤2, and
3q_ab−5≥0 forces q_ab=2. Orbit a therefore has four double interfaces.
Its diagonal defect is D_aa=4, and each of the four incident off-diagonal
defects is at least one, violating row sum five. Thus every actual
target's off-diagonal quotient support must contain a triangle.
This statement was not used as an extra hard filter in the profile.

## Resources and stopping condition

The one-CPU episode had a total ten-CPU-second budget, including
compilation and the reserved possibility of one independent BFS.
The profile process used a 1 GiB address-space limit.

| Component | CPU seconds |
| --- | ---: |
| Compilation | 0.810718 |
| Profile process | 0.912758 |
| Python runner | 0.004812318 |
| Total | 1.728296102 |

The internal profile measured 0.910667 CPU seconds and 0.911611147 wall
seconds, within its 8.185796746-second allocation. Total wall time was
1.738710642 seconds. The complete input and final cursor are retained in
the run directory. No retry, additional profile, graph optimization,
voltage search, SAT or BFS ran; no job remains active.
