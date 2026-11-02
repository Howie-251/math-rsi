# HS58 a5: checked joint completion failure for the remaining type 3

Date: 2026-10-12. The final separately authorized residual query
returned **checked UNSAT**. It fixed the HS deletion pair
D={(0,1),(10,11)} and the actual type-3 auxiliary graph below, while
all five old nonedge additions and all old-new attachments remained
free. No target graph was found and no further query was run.

## Why this was a new residual input

The completed
[construction pass and type-14 query](HS58_TWO_DELETE_FIVE_ADDITIONS_CONSTRUCTION.md)
had already saved actual full graphs in 22 retained H types.
Subsequently the repaired
[no-cross endpoint coverage argument](HS58_NO_CROSS_ENDPOINT_COVERAGE.md)
gave a necessary bad-pair degree-sum condition for two disjoint HS
deletions whose endpoints have no original cross-edge.
Reading the 67 existing representatives with that condition left
only type 3; the exact derived list is
[no_cross_filter.json](../../../computations/dd82/construction/hs58_two_delete_five_add_auxiliary_run/no_cross_filter.json).
This was a new analytic reduction, not another raw H enumeration.

The actual deletion pair in the saved graphs has no such cross-edge.
Its existing
[type3.best.json](../../../computations/dd82/construction/hs58_two_delete_five_add_switch_run/type3.best.json)
provides the complete 58-vertex, 232-edge, eight-regular seed. The
[independent BFS](../../../computations/dd82/construction/hs58_two_delete_five_add_switch_run/type3.best.verification.json)
records diameter three and all 81 bad pairs: one old-old and 80
old-new. This is a failed concrete graph, not a witness of existence.

The new input used exactly its labeled H:

```
02,03,04,05,06,07,12,13,16,17.
```

H consists of two vertices with four common neighbors and two
additional leaves on the degree-six vertex. It is isomorphic to
a5 catalog type 3; the explicit map is in the seed JSON. Neither
its old additions nor its attachments were frozen in the query.

## Exact CNF and result

The encoding uses the existing exact cardinality and conjunction
helpers. Its primary variables are all 1,050 original HS nonedges
as possible additions, and all 400 old-new edges. It enforces exactly
five additions, degree eight everywhere, and all 1,653 pairwise
distance-at-most-two obligations. Precisely 1,225 pairs are already
covered by fixed edges, leaving 26 old-old, 400 old-new, and two
new-new coverage clauses. No normalization or additional mathematical
pruning clauses were imposed, including the new no-cross theorem:
that theorem selected H but was not encoded as a shortcut.

The saved input has 33,344 variables and 105,990 clauses. CaDiCaL
returned exit code 20. The existing LRAT checker independently checked
the saved proof against that CNF and returned exit code 20 with
`s VERIFIED`. There was one attempt, with a 30 CPU-second budget,
4 GiB address-space limit, and 128 MiB proof-file limit.

CNF preparation used 0.136159 CPU seconds and 0.146608 wall seconds.
Actual solver time was 7.295349 CPU seconds and 7.799073 wall seconds.
LRAT verification took 0.307517 CPU seconds and 0.332365 wall seconds.

* [Source](../../../computations/dd82/construction/hs58_two_delete_five_add_type3_joint.py).
* [Input and variable mapping](../../../computations/dd82/construction/hs58_two_delete_five_add_type3_joint_run/encoding.json).
* [CNF](../../../computations/dd82/construction/hs58_two_delete_five_add_type3_joint_run/input.cnf)
  and [LRAT proof](../../../computations/dd82/construction/hs58_two_delete_five_add_type3_joint_run/proof.lrat).
* [Solver output](../../../computations/dd82/construction/hs58_two_delete_five_add_type3_joint_run/solver.log),
  [checker output](../../../computations/dd82/construction/hs58_two_delete_five_add_type3_joint_run/certificate_check.log),
  and [result/resources](../../../computations/dd82/construction/hs58_two_delete_five_add_type3_joint_run/result.json).

## Scope of the combined conclusion

For this exact HS labeling and deletion pair, the prior general
auxiliary reductions and the no-cross theorem leave only type 3.
Any labeling of that H type is equivalent for this existence question
by relabeling the eight new vertices; all attachments are free.
The checked query therefore finishes the two-deletion/five-addition
completion question for **D={(0,1),(10,11)}**.

No HS automorphism transitivity or classification of deletion-pair
orbits is assumed. The certificate does not by itself exclude other
disjoint no-cross deletion positions, deletion pairs with a Q
cross-edge, or adjacent deletions. It says nothing about six or more
additions. The earlier type-14 query was not rerun, the type-54 query
was never launched, and this residual query ends the authorized
construction experiment.
