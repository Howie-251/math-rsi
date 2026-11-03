# Parallel-triangle 33-controller rule: complete80-setting gate fails

All80 prescribed settings were generated and checked once. There are0 raw NB3 passers and0 untested settings. The existence prediction is REFUTED for this fixed rule. Stop: no field matrices, target2112 graph, solver, controller BFS or source BFS was run.

Every setting passed the structural predictions:33vertices/66edges, simplequartic, eleven specified disjoint triangles, with exactly three original externalC5s extended toC6 and three originalC5s retained. All source paths that avoid the three deleted edges survive literally. This preservation alone did not supply all required replacement routes.

The complete domain is ten actual old source triangles, each with two choices of external edge at each of its three vertices. These are80 distinct labeled graphs. The three new vertices30,31,32 form a newtriangle; each subdivides one chosen old externaledge. CASES.json saves all parameters, cuts, newedges, exact66edge lists and missing-route witnesses. PASSERS.json is empty.

The first failed ordered pair is old-old in66 settings and new-old in14. Across all settings the missed nonadjacent/equal NB3 slots contain5460 old-old and3612 new-old occurrences, and no new-new/self occurrences. Each setting misses102..132 required ordered NB3 slots. These are controller route-support counts; they are not ordinary distance badpairs and do not establish the controller's exact diameter.

For example candidate0 chooses source triangle[0, 2, 18], cuts[[0, 9], [1, 2], [4, 18]], and first fails{'u': 0, 'v': 3, 'class': 'old-old', 'NB3_count': 0}. The exact list is preserved rather than choosing a best score or continuing a neighborhood.

## Why this is a necessary gate for the stated zero-offset F4 lift

For a nonadjacent distinct controller pair with no NB3 route, no length3 controller walk exists: a backtrack in a3walk would end adjacent to its start. At source fiber coordinate0, every remaining length2 route in a zero-offset linear line lift has image a linear subspace of size at most4^2=16 and contains0. A simple quartic controller has at most4 length2 routes to a distinct endpoint. Their union therefore has size at most1+4*(16-1)=61<64. This excludes complete F4^3 coverage for that pair regardless of the linear matrices, so entering a search for one exceptional turn per edge cannot rescue any of these80 controllers.

Each saved first failure is a nonadjacent distinct pair. The bound applies to this zero-offset four-neighbor-controller/fiber-width4 construction, not to arbitrary affine offsets, internal fiber edges, extra controller relations, arbitrary2112graphs, or all(16,3)graphs.

The necessary gate is stronger than treating ordinary controller diameter3 as enough, and remains distinct from the sufficient complete good-route/pencil certificate. A passer would still require a simultaneous edge-map certificate or exact full fiber coverage.

## Closest prior scopes

The old n31 rule was345 pairs of old vertices from different triangles/C5s, each with8 specified rearrangements, total2760. It moved old vertices into an overlapping newtriangle and produced31points. This rule creates three genuinely new vertices, retains every old triangle, and subdivides one edge in each of three oldC5s.

The old33 rule sampled eight starting external2factors followed by800000 two-switch proposals under fixed elevenK3s. It did not enumerate the entire external2factor domain. Our80 settings are a complete small source-derived slice of that wider family, tested by an exact relevant gate. The old cyclic3-layer voltage capacity exclusion is not silently extended to arbitrary external2factors.

Worker PID1172576; process CPU0.056890040s, wall0.059029974s,20CPU budget. No target graph or new lower bound exists; target n/D and ordinary badpair counts remain null. All work is terminal with no pending cases. The separate F5 local positive control is in ../f5_complementary_triples/ and is not counted as this experiment.

## Stronger saved-case followup

CUT_PAIR_OBSTRUCTION.md proves every selected cutpair has exactlyone2walk andno3walk; all240 pairs were checked directly from saved edges. Therefore anyq^3-fiber lift withbranching atmostq perarc andnointernalfiberedges misses thattargetfiber, even witharbitrarymaps/offsets. This stronger scope supersedes only the earlier zero-offset restriction for these80controllers. Main80 execution statistics remain unchanged; the read-only followup CPU is0.001872806 separately. No newtemplate was generated.
