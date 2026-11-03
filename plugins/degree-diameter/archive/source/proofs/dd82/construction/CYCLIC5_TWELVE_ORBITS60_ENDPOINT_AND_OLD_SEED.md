# Bad-endpoint diagnostic and the distinct known C5 seed

The proposed unique lifting of an automorphism of the twenty bad
endpoints fails for the actual 20-bad-pair graph: its forty other vertices
have only ten distinct neighbour pairs in that set, each repeated four
times. This does not exclude a semiregular order-five automorphism of the
full graph. The earlier unrestricted diagnostic remains UNKNOWN.

The separate old 50-bad-pair seed does have the previously proved C5
symmetry. Its actual permutation was verified on all 240 edges and its
complete twelve-orbit voltage representation is now saved, with all 354
possible edge orbits and the 48 selected ones. This export reproduces the
old 50-bad graph; it is not a new graph or a representation of the 20-bad
seed.

Source:
[cyclic5_twelve_orbits60_endpoint_diagnose.py](../../../computations/dd82/construction/cyclic5_twelve_orbits60_endpoint_diagnose.py).
Run record:
[diagnosis.json](../../../computations/dd82/construction/cyclic5_twelve_orbits60_endpoint_run/diagnosis.json).

## Actual twenty-endpoint signatures

The input is the complete graph in
[petersen_all_matchings_run/candidate.best.edges](../../../computations/dd82/construction/petersen_all_matchings_run/candidate.best.edges).
Its saved independent BFS identifies the bad-endpoint set S={40,...,59}.
The graph induced on S and the bad-pair relation are exact automorphism
invariants. Every other vertex has exactly two neighbours in S, but these
signatures are not unique:

| Neighbour pair in S | Vertices with exactly this signature |
| --- | --- |
| 40,55 | 0,18,21,31 |
| 41,50 | 9,14,28,38 |
| 42,51 | 3,12,29,39 |
| 43,56 | 7,10,25,33 |
| 44,58 | 6,19,23,35 |
| 45,57 | 2,11,27,34 |
| 46,54 | 1,16,22,30 |
| 47,52 | 5,15,20,32 |
| 48,59 | 8,17,24,37 |
| 49,53 | 4,13,26,36 |

These are direct intersections with the actual input adjacency lists;
the full induced edges, twenty bad pairs and all signature classes are
stored in
[endpoint_structure.json](../../../computations/dd82/construction/cyclic5_twelve_orbits60_endpoint_run/endpoint_structure.json).
An automorphism on S can therefore determine only these four-element
classes, not the images of their individual vertices. Enumerating
automorphisms of the two-colored graph on S and selecting an arbitrary
lift would not be candidate-preserving. The diagnostic stopped this
lifting route as instructed, without running another full-graph
GraphMatcher search or claiming nonexistence of order-five automorphisms.

## Verified voltage representation of the old fifty-bad seed

The separate source is
[petersen_six_fibers.best.edges](../../../computations/dd82/construction/petersen_six_fibers.best.edges),
with its already completed independent check in
[petersen_six_fibers.best.verification.json](../../../computations/dd82/construction/petersen_six_fibers.best.verification.json).
The existing checker
[petersen_six_fibers_check.py](../../../computations/dd82/construction/petersen_six_fibers_check.py)
contains the actual symmetry formula. On the five external fibres it
sends 10i+u to 10(i+1 mod 5)+u. On the infinity fibre it rotates each
five-vertex Petersen layer by one. The twelve cycles are

\[
 (a,a+10,a+20,a+30,a+40)\quad(0\leq a<10),
 \quad(50,51,52,53,54),\quad(55,56,57,58,59).
\]

The new script checks that this is a permutation of cycle type 5^12 and
that its image of the complete edge set is exactly the original edge
set. Numbering each listed cycle by a and positions by t identifies its
vertices with (a,t), or integer label 5a+t. This gives:

- [Actual permutation, cycles and relabelling](../../../computations/dd82/construction/cyclic5_twelve_orbits60_endpoint_run/seed50/automorphism.json).
- [Complete relabelled edge table](../../../computations/dd82/construction/cyclic5_twelve_orbits60_endpoint_run/seed50/seed.edges)
  and [graph JSON](../../../computations/dd82/construction/cyclic5_twelve_orbits60_endpoint_run/seed50/seed.json).
- [All 354 possible edge orbits](../../../computations/dd82/construction/cyclic5_twelve_orbits60_endpoint_run/seed50/palette.json).
- [Actual voltage table and 48 selected orbit indices](../../../computations/dd82/construction/cyclic5_twelve_orbits60_endpoint_run/seed50/voltages.json).

The 354-orbit catalogue partitions K60: 330 matching orbits between
different five-vertex cycles and 24 internal five-cycle orbits. Every
orbit has five edges. Exactly 48 are selected, their union reconstructs
all 240 source edges, and the twelve weighted quotient degrees are all
eight. The complete free-variable definition and degree/coverage
equations are in
[CYCLIC5_TWELVE_ORBITS60_DIAGNOSIS.md](CYCLIC5_TWELVE_ORBITS60_DIAGNOSIS.md).
Allowing those variables to change would not preserve the old six
Petersen fibres unless that restriction were separately imposed.

As an additional direct check of the voltage conversion, form
C_ab=D_ab union the sets D_ac+D_cb over all intermediate orbits c.
The missing shifts are:

| Orbit pair | Missing shift |
| --- | --- |
| 0,1 | 3 |
| 0,4 | 2 |
| 1,2 | 3 |
| 2,3 | 3 |
| 3,4 | 3 |
| 5,6 | 3 |
| 5,9 | 2 |
| 6,7 | 3 |
| 7,8 | 3 |
| 8,9 | 3 |

Each missing shift lifts to five unordered bad pairs. These fifty pairs
agree exactly, after relabelling, with the previously saved independent
BFS witnesses. No BFS was rerun, and no improvement to the seed is claimed.

## Resources and stopping boundary

The whole new diagnostic and old-seed export used 0.012009412 CPU seconds
and 0.019569192 wall seconds, pinned to one CPU with a ten-CPU-second
limit and 1 GiB address-space limit. The uniqueness test failed, so zero
colored endpoint automorphisms were enumerated. No solver, optimization
or full BFS ran; no job remains active. The 20-bad seed still has no
established twelve-orbit voltage representation, while the 50-bad seed
has the explicit verified representation above.
