# HS58 a5: the no-cross deletion orbit and its exclusion

Date: 2026-10-12. All unordered pairs of disjoint HS50 edges with no
HS cross-edge between their endpoints belong to one explicitly verified
automorphism orbit. Combining this fact with the saved auxiliary
classification, endpoint coverage theorem, and checked type-3 CNF
excludes every order-58 extension with exactly two such original
deletions and exactly five added original nonedges.

This is a computer-assisted exclusion of this HS-edit family. It does
not address adjacent deletions, disjoint deletions with a cross-edge,
other addition counts, or arbitrary order-58 graphs. No complete
automorphism-group calculation or external orbit classification is
used.

## Explicit automorphisms of the actual HS labeling

Write U(i,j)=5i+j and V(k,l)=25+5k+l, with coordinates modulo five.
The saved HS graph has U pentagon edges j to j+1, V pentagram edges
l to l+2, and U(i,j)-V(k,l) exactly when l=ik+j. The first five
generators are:

| Generator | Image of U(i,j) | Image of V(k,l) |
|---|---|---|
| Common translation | U(i,j+1) | V(k,l+1) |
| U-track translation | U(i+1,j) | V(k,l+k) |
| V-track translation | U(i,j-i) | V(k+1,l) |
| Inverse track scaling | U(2i,j) | V(3k,l) |
| Side exchange | V(i,2j) | U(3k,2l) |

One bounded NetworkX isomorphism query supplied a sixth permutation.
Its images of labels 0,...,49, in order, are

```text
 0  1 31 14 40 49 11 12 27 17
 3 28  8  9 48 44  6 32 19 15
39 21 20 24 37  4 26 34 29 16
30 46 33 13  7 25 41  5 10 43
45  2 18 47 42 35 36 22 38 23
```

In particular it fixes 0,1 and sends (10,11) to (3,28). NetworkX was
used only to discover this explicit permutation. Each of all six
generators was then checked to be a bijection of the 50 labels and
to send the entire 175-edge set exactly to itself. These checks do
not rely on the isomorphism searcher's correctness or on a claimed
automorphism-group order. All six full arrays and their validation
fields are saved in
[generators.json](../../../computations/dd82/construction/hs58_no_cross_deletion_orbit_run/generators.json).

## Complete orbit coverage

The source
[hs58_no_cross_deletion_orbit.py](../../../computations/dd82/construction/hs58_no_cross_deletion_orbit.py)
directly considers every unordered pair of the 175 original edges.
It records 1,050 pairs sharing an endpoint, 6,300 disjoint pairs with
a cross-edge, and **7,875 disjoint pairs without a cross-edge**.

Starting from D0={(0,1),(10,11)}, the program applies the six verified
generators to deletion pairs. Every newly reached pair is checked to
belong to the directly enumerated no-cross domain. The saved
[orbit.json](../../../computations/dd82/construction/hs58_no_cross_deletion_orbit_run/orbit.json)
contains every reached deletion pair, its earlier predecessor, and
the generator used to reach it. Thus each entry has an explicit word
in actual automorphisms mapping D0 to that pair.

The orbit contains exactly 7,875 distinct pairs, is closed under all
six generators, and its set equals the complete directly enumerated
domain. The actual
[result.json](../../../computations/dd82/construction/hs58_no_cross_deletion_orbit_run/result.json)
reports complete=true and missing_domain_size=0. Inverting a recorded
automorphism word maps any pair in this domain back to D0.

This was one run under a ten-CPU-second cap, with one pinned CPU.
The single extra-isomorphism query used 0.039986 CPU seconds. The
internal result timer records 0.165001902 CPU seconds and 0.187943991
wall seconds; it starts after imports and does not include all final
serialization. Total
child resources, including imports and saved output, were 0.350923
CPU seconds and 0.375489 wall seconds, exit code zero; see
[resources.json](../../../computations/dd82/construction/hs58_no_cross_deletion_orbit_run/resources.json)
and the
[bounded launcher](../../../computations/dd82/construction/hs58_no_cross_deletion_orbit_run.py).
No additional automorphism query, solver, or orbit rerun was performed.

## Candidate-preserving connection to the existing type-3 CNF

Consider any target graph in the stated edit family. The eight new
vertices induce ten edges, so the completed
[a5 auxiliary catalog](../../../computations/dd82/construction/hs58_two_delete_five_add_auxiliary_run/README.md)
applies. Under disjoint deletions its port budget allows 72 types.
The five universal types are excluded by
[HS58_TWO_DELETE_UNIVERSAL_H_EXCLUSION.md](HS58_TWO_DELETE_UNIVERSAL_H_EXCLUSION.md),
leaving the recorded 67-type necessary domain.

For no-cross D, the fully proved
[endpoint coverage theorem](HS58_NO_CROSS_ENDPOINT_COVERAGE.md)
requires degree sum at least five for each auxiliary bad pair. The
saved
[read-only derived filter](../../../computations/dd82/construction/hs58_two_delete_five_add_auxiliary_run/no_cross_filter.json)
gives a violating bad pair for each of 66 types, leaving only type 3.

Use an inverse automorphism word above to map the old deletion pair
to D0. This preserves original HS edges and nonedges, so it preserves
the meaning and number of the five added old nonedges. Independently
relabel the eight new vertices to the actual type-3 auxiliary labeling
in the saved encoding, whose edges are

\[
02,03,04,05,06,07,12,13,16,17.
\]

These two independent relabelings transport every old-new attachment
without restricting it. The source
[hs58_two_delete_five_add_type3_joint.py](../../../computations/dd82/construction/hs58_two_delete_five_add_type3_joint.py)
has all 1,050 original-nonedge addition variables and all 400 attachment
variables free. It fixes only D0 and this labeled H, has no attachment
or addition normalization, enforces exactly five additions, and
encodes exact degrees and every pair's adjacency-or-two-step coverage.
Thus any transformed target extends to a satisfying assignment of
that actual CNF. In particular, no automorphism of H needs to extend
to an automorphism of Q: their labels are chosen independently and
the attachment matrix remains unrestricted.

The saved
[type-3 result.json](../../../computations/dd82/construction/hs58_two_delete_five_add_type3_joint_run/result.json)
records 33,344 variables and 105,990 clauses, CHECKED_UNSAT, solver
exit code 20, and a verified LRAT check. The solver used 7.295349 CPU
seconds and the checker 0.307517 CPU seconds. Its recorded
[certificate check](../../../computations/dd82/construction/hs58_two_delete_five_add_type3_joint_run/certificate_check.log)
concerns that same input.cnf and proof.lrat. These pre-existing results
were read, not rerun, for the orbit task.

Every candidate in the stated no-cross deletion family therefore
maps to this checked-unsatisfiable instance. The complete connection
uses the actual finite H catalog, the analytic endpoint theorem,
the verified 7,875-pair orbit, and the existing LRAT-checked CNF;
it is not an assertion based solely on graph symmetry or an assumed
literature orbit. No new external-review acceptance is claimed here.

Together with the existing
[two-deletion addition budget](HS58_TWO_DELETE_ADDITION_BUDGET.md),
[two-addition exclusion](HS58_TWO_DELETE_TWO_ADDITIONS_EXCLUSION.md),
[three-addition exclusion](HS58_TWO_DELETE_THREE_ADDITIONS_EXCLUSION.md),
and [four-addition exclusion](HS58_TWO_DELETE_FOUR_ADDITIONS_EXCLUSION.md),
this proves the cumulative statement: **an HS58 extension deleting
exactly two disjoint original edges with no Q cross-edge requires at
least six added original nonedges**. It does not assert such an
extension exists at six additions.
