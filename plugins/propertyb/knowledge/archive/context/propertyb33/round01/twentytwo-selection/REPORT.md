# Complete 22-point Property B theorem

`TwentyTwoSelection.exists_locks_of_twenty_two` takes any finite vertex type,
exactly 22 vertices, 33 simple five-element edges, and pair coverage. It selects
actual distinct vertices of H with one of the following complete alternatives:

- A degree-six point and a degree-six or degree-seven partner, of codegree one.
- Two degree-seven points of codegree at least three.
- Three degree-seven points with codegrees xy=xz=2, yz=1.
- Four degree-seven points with codegree-two graph a triangle on x,y,z and
  isolated w; or only the edge xy; or no edges, with an actual hyperedge
  containing x,y,z.

All six distinctness relations are included for four selected points. The last
alternative gives a literal original hyperedge and its three memberships,
which implies a large trace without an extra assumed trace certificate.

The structural proof first handles a degree-six vertex by the actual total
incidence budget. Otherwise the seven-degree set S has at least eleven points.
After excluding high pairs and induced paths, `cluster_relations` proves
that the selected closed neighborhood is a clique with codegree one to its
complement. Its cardinality is at most eight, from the actual codegree-excess
budget. An existing edge then yields the triangle-plus-isolate or
edge-plus-two-isolates four-lock pattern. If every pair in S has codegree one,
seven actual edges through a chosen point cover at least ten other points;
cardinality of their union gives an actual edge containing three points of S.

Validation: `lake build Aris4Math.ThirtyThree.TwentyTwoSelection` exited 0.
`ImportAudit.lean` independently imports the built module, checks the exact
22-point caller, and prints the configurations and final theorem. Its only
transitive axioms are `propext`, `Classical.choice`, and `Quot.sound`. Logs are
`build.log` and `import-audit.log`.

## Complete connection to Property B

`ThirtyThree.twenty_two_propertyB` in `TwentyTwoComplete.lean` now proves
Property B for every actual `Fin 22` input with exactly 33 edges and pair
coverage. Its transitive axioms are the standard three, and it has no additional
structure, profile, classification, trace-count, or deletion premise.

`TwentyTwoQuadAssembly` proves five actual high-trace counts are each at most
two, their three-term consumption of each of the six pair inventories is at
most the actual codegree, and a common original edge forces high0+high4≥1.
The local 20-row coverage theorem covers every bounded vector satisfying these
necessary constraints. The actual selected four vertices are then matched to
one of the twenty rows, including every actual degree, pair count and high
trace count. The probability caller proves Property B using actual multiplicity
recovery and pure-single-lock deletion. The total assembly also discharges both
six-degree pairs, the high-codegree pair, and the induced-path triple.

`complete-build.log` records the clean final build. The updated
`ImportAudit.lean` independently checks the literal final statement and audits
its transitive axioms, as well as the complete local-data coverage and actual
four-lock caller. `Assembly.lean` now actually calls this result, reducing its
explicit remaining premise to 23–24 vertices. The full T33 is still unproved.
