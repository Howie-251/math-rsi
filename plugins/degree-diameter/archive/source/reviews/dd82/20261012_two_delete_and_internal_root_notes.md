# Local root checks, 2026-10-12 continuation

These are local checks by the executor plus the separately recorded
same-family agent reviews. They are not external Gemini acceptance or
Lean formalization. No completed external verdict is available from the
preceding three failed review calls; no additional call is represented here.

## Five additions and deletion normalization

Read the actual adjacent/cross joint source, complete-coverage construction,
exact-cardinality helper, metadata and terminal result records. All 1050 A,
400 B and 28 H edges are included. Exactly one of the 67 representatives is
chosen and forces both its edges and nonedges. Deleted original edges are
fixed false; the source does not permit accidentally re-adding them.
The 1653-pair coverage is complete, including B-B and H-H paths for new
pairs. Each actual LRAT result is VERIFIED on the corresponding saved input.
The second agent's independent read and scope check is in
HS58_A5_REMAINING_JOINT_ENCODING_REVIEW.md.

Read the remaining-orbit code and proof. The six previously verified
automorphisms are reused, their complete images act on actual original
edges, and each visited pair lies in the directly generated geometry.
Equality of orbit and direct domains is established with zero omissions.
1050+6300+7875=C(175,2); inverse words followed by independent H relabeling
preserve arbitrary A/B choices. The 67-to-1 no-cross reduction is not used
for adjacent or cross formulas. Thus the combined a>=6 statement has the
stated family-wide scope, with the earlier a<=4 dependencies retained.

## Addition upper bound and saturated branches

Read HS58_TWO_DELETE_GLOBAL_ADDITION_BOUND.md in full. Independently checked:
z=E+2a-4; the rowwise zero-port requirement; 2e_M(Z)<=6E; the A degree
balance; and m+a<=4+2E-r(Z)+e_D(Z). The last correction is nonpositive
since r(Z)-e_D(Z)=e_D(Z)+e_D(Z,Z-complement)>=0.

The exact HS identity Q^2=6I-Q+J gives eigenvalues 2,-3 on the constant
orthogonal space and m>=z(z-15)/10. For a=9+s the combined polynomial is
E^2-7E+36+4sE+36s+4s^2>0. This proves a<=8 without a catalog.

At a=8, E<=1 contradicts the preceding nonnegative-m bound. E=2 forces
an independent 14-set and two weight-one excess vertices with all six old
neighbors zero. At least one has deleted degree one and no addition, so
its Q-neighbor count is six; this contributes 12 to a sum of nonnegative
integer terms (k-2)(k-3) totaling only six. E=3 has exactly the two listed
weight patterns, and the outside variance is 10m-s_2<=8m. The Cauchy lower
bounds exceed this by 4((m-1)^2+3)/3 and (2m-5)^2/5 respectively. Their
subtraction of at most one incident added edge in the three-vertex case
is justified by total deleted degree four. E=4 is saturated and uses the
valid all-a adjacent obstruction or independent-Z disjoint argument.
Hence a<=7 is established, with no assumption on H.

Read HS58_SATURATED_DISJOINT_ALL_ADDITIONS.md in full. Its tau-pairing and
independence proof never uses a=5. Checked the explicit coordinates of the
two C8 cycles and the four double-neighbor cells. The common-neighbor
argument proves there are no missing induced edges. Therefore saturated
cross has at most ten zeros; saturated no-cross at most twelve, with four
equality zero sets and 24+4+4+24=56 actual old-addition matchings. This is
only a necessary finite domain and leaves attachment/H feasibility open.

## Larger joint experiment

Read the new source and the three terminal results. Using h=a+5 makes the
11..13 H threshold exactly a=6..8; auxiliary degree ordering can always be
obtained by independently relabeling the eight new points. No later
spectral/saturated inequalities were injected into the actual inputs.
All three calls terminated without a decision (two OUTPUT_LIMIT, one
UNKNOWN); partial LRAT is not a certificate. Do not relaunch unchanged.

## Sixty-point construction feedback

Read PETERSEN_INTERNAL_REASSEMBLY.md and its actual required-neighbor
witness. With the indicated matching edges and fixed P2, source 0 reaches
only six distinct F2 targets outside the P0 route. Four targets remain but
the source has only three internal neighbors; this excludes the proposed
boundary domain independently of enumeration. The 111-bad-pair changed
graph is a failed full graph, and the stopped P1 and 4/5 stages are not
reported as exhaustively searched.

Read the subsequent all-internal fixed-route obstruction. The displayed
five external routes from 29 to F5 reach only 51 and 55. Even six distinct
internal-route endpoints would cover at most eight of ten targets. This
applies to all six varying cubic internal graphs with those fixed matching
edges. The canceled CNF and SAT are correctly counted as not run.
Changing those external matchings is a necessary next construction step;
neither this witness nor the prior fixed-seven-route palette closes the
full six-Petersen family.

## Repaired external matching completion

Read PETERSEN_FIXED_ROUTE_REPAIR_AND_INTERNAL_COMPLETION.md, the entire
petersen_repaired_external_completion.py, actual encoding/result and LRAT
checker log. All270 internal pairs are free; exact cubic is encoded by
forbidding four true and seven false among each nine incident bits. All
triangle and three C4 cyclic orders per four-set are included. An uncovered
cross pair has exactly the two displayed internal-edge choices, and neither
can be a loop because the direct matching would then cover the pair.
The 815 clauses cover all remaining cross pairs; cubic/girth-five on ten
vertices makes every internal radius-two ball have1+3+6=10 points.
Thus the checked270/15035 UNSAT excludes every six-Petersen completion of
this actual new external skeleton. The140 distinct original LRAT
antecedents include both girth groups; no broader arbitrary-cubic conclusion
is inferred. No repeated solve/check was performed by the root.

## Saturated a6 port-palette reduction

Read HS58_A6_SATURATED_PORT_PALETTES.md in full. Each positive singleton
T_p vertex must use a label from the deleted partner's port pair; each
singleton zero has exactly eight neighbor slots and so needs all distinct.
The two-list C4 condition is necessary and sufficient only for this local
subset, not for the full zero rows. If both endpoint pairs repeat, the
lists force the two palettes to be disjoint, and each must dominate H.

The old-column quotas give the stated degree bounds2+2k and6-2k. Pure
L/R cases are immediately impossible. In the mixed case the four neutral
vertices require at least8 palette incidences and the palette cross graph
requires an edge cover, hence at least2 edges. With exactly11 H edges the
three listed(c,r,e) cases exhaust everything, including possible internal
palette edges and neutral-neutral edges. In the3/8/0 case only the two
listed W types can reach all palette vertices, and mixing them creates an
unrepairable W bad pair. In2/9/0 the unique degree-three neutral vertex
needed to cover the opposite missing cross pair forces a palette degree5.
In2/8/1 an internal-palette extra edge still leaves on-matching neutral
types unable to reach the opposite palette vertex; a neutral extra edge
cannot repair the disjoint neighborhoods of its opposite-type endpoint
and either untouched neutral vertex. These contradictions prove only the
repeated-pair subcase. Unequal intersecting port pairs remain explicit.

During construction discussion, two proposed auxiliary H choices were
rejected before any flow or SAT: the8-cycle plus three diameters has a bad
pair of degree sum4, and a root-proposed11-edge two-palette graph has six
bad pairs, not the guessed two. The latter's (1,4),(1,5),(3,4),(3,5)
witnesses were caught by both agents and root direct neighbor inspection.
Neither proposal enters an accepted proof or a solver input. The final
palette exclusion uses a complete symbolic edge budget instead of either
incorrect auxiliary shortcut.

The HS construction agent independently read the entire final palette
proof, including both possibilities for the last extra H edge, and found
no gap. A final direct a6 assignment was expanded once, without flow or
search, into58/232/eight-regular:89 bad pairs, all old-new. It intentionally
retains the demonstrated repeated-color failure at zero33. Root read the
actual generator, its forced columns and the exact-degree identities;
this failed seed is not promoted to a surviving target candidate.
