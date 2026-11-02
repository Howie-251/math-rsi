# Core-route discriminator: actual partition and route obligations

This is one new structural readout of the inherited49core labels and unchanged source adjacency; no source validity, common-neighbor all-pair test, BFS, color refinement, solver or isomorphism search was rerun. The previous duplicate-signature interface remains a failed uniqueness prediction, not a no-C7 theorem.

Actual signature partition: 42 classes, size histogram {1: 35, 2: 7}. The prediction of seven size-seven classes is REFUTED. All classes, actual internal degrees, intergroup edges and each physical core row's neighbor-group counts are saved in SIGNATURE_CLASSES.json / CORE_GROUP_EDGE_BLOCKS.json / CORE_ROW_DEGREE_PROFILES.json. These data are not silently treated as automorphism orbits. Any7vertex4regular class is checked only for the exact complement-C7 certificate; absence of that form is not a general noncirculant classification.

Core8 and10 share small neighbors [0, 31, 42, 55, 71, 82, 96], but have core neighbors [21, 49, 66, 79] and [20, 45, 80, 104] respectively. Their same small signature therefore leaves different physical edges and different source route payloads unresolved.

The targeted route witness, using the existing unique-route profile for8, is:

```json
{
  "target": 12,
  "route_from8": [
    8,
    21,
    12
  ],
  "unique_from8_inherited_from_profile": true,
  "routes_from10": [
    [
      10,
      20,
      12
    ]
  ],
  "small_common_route_absent_reason": "8 and10 have identical small neighbors; the inherited unique8 route uses a core middle.",
  "changed_physical_middle_edges": true
}
```

The unique-from8 statement is inherited from the saved profile, not recomputed by common-neighbor enumeration. The10 routes were read only along its four core neighbors for that one target. This is a route discriminator, not a second full-source D2 check.

## Concrete consequence for internal-pin changes

If an original nonadjacent pair(v,u) has unique common middlew, deletingv-w loses that source route. In the current rule onlyG[S] changes. Ifv,u both lie inS, newz repairs them; ifv∈S andu outside, any replacement must be a chosen internal neighbora∈S that is an ORIGINAL neighbor ofu, givingv-a-u. Merely selecting another vertex with the same small signature asv does not preserve that physical core edge or its inherited unique-target payload. When deleting the displayed8-middle edge, the target in the witness must be selected too or receive an explicit replacement2route; the10-middle route cannot simply be substituted without a genuine edge from8 to that middle.

This directly changes the next selection/edge rule: track the actual4core-neighbor choices and their directional private-target lists, not just small-signature class membership. A duplicate-signature class can still have an automorphism acting on it together with other core classes; differing labeled neighborhoods neither prove nor refute that. Consequently nox8=x10 orbit constraint, arbitrary replacement of one by the other, orC7-invariant pin-set reduction is justified by this partition alone.

The data stop at structural route obligations. No S is selected, no core/sector permutation is enumerated, no rewiring or graph is generated, and no further timer follows. Root may use the concrete intergroup blocks and route payloads to formulate a separately authorized prediction; this result does not resolve the previous internal-rewiring UNKNOWN model or claim any new107graph.
