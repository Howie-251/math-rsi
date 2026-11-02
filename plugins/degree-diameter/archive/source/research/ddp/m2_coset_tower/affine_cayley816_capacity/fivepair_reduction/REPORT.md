# Five-pair scope: complete

**Final update:** the subsequently authorized four-worker dimension-six production also completed all 10,747,252,152 inputs without full fiber coverage. All 16,375 five-pair symbolic modes are now closed, and combining the saved four-pair and six-pair terminals closes the fixed group's degree-12 Cayley scope. See [the complete final report](full_dimension_production/REPORT.md), [the scope accounting](full_dimension_production/FAMILY_CLOSURE.json), and `CURRENT_SCOPE_STATUS.json`. No graph or new record was obtained. The sections below retain the earlier preprocessing and reduced-production snapshots; their remaining-scope statements describe the state before the final batch.

The phase automorphism and iterated tight-fiber constraints reduced the remaining five-pair scope. The subsequently authorized complete search of all genuinely reduced representatives found no degree-12, diameter-3 graph. The dimension-six representatives remain unsearched.

The original input was exactly 16,375 saved five-pair/two-reflection symbolic survivors in `F17 semidirect_3 C48`, order 816. The actual saved maximin inputs and per-mode terminal confirm that 28 had already been fully excluded. This task did not recheck the four-pair or six-pair branches.

## Complete preprocessing

The group automorphism `(x,j) -> (x,17j mod48)` was proved and checked against every saved mode and all 48 capacity entries. It gives 8,397 phase-mode orbits: 7,978 pairs and 419 fixed modes. The 28 completed modes occupy 16 orbits, leaving 8,381 unsearched representatives. No additional unsearched mode is closed solely by transferring the old 28 results. Fixed modes retain their whole projective parameter space.

There were 3,280 original modes with an exact-17 fiber, represented by 1,663 unsearched orbits. All 1,663 representatives underwent the iterated sum-of-all-17-forms condition, nullspace restriction, and form deduplication. This rejected 166 orbit representatives, representing 314 original modes. The remaining dimensions are:

| Nullspace dimension | Surviving representatives | Original modes represented | Marked inputs per representative | Total marked inputs |
|---:|---:|---:|---:|---:|
| 3 | 3 | 6 | 307 | 921 |
| 4 | 143 | 282 | 5,220 | 746,460 |
| 5 | 945 | 1,880 | 88,741 | 83,860,245 |
| 6 | 7,124 | 13,865 | 1,508,598 | 10,747,252,152 |

Thus the preproduction marked scope fell from 24,661,051,506 original-mode inputs to 10,831,859,778 inputs after selecting automorphism representatives and applying the necessary linear conditions. These are marked projective counts, not isomorphism-class counts or actual graph evaluations.

The three dimension-three representatives have pair phases `[1,10,17,18,18]`, `[4,5,8,16,22]`, and `[7,7,9,13,16]`. The latter two include phase 16, which has trivial scalar action and was correctly skipped as a translation anchor. No phase-16 pair was dropped.

Every matrix, rank, basis, final count, and rejection witness is retained in `tight_results.jsonl`. Six representatives required three recorded iterations; newly tight fibers were used only after an actual restriction. No arbitrary subset of 17 forms from a larger fiber was selected. The proof and coordinate maps are in `SCOPE.md`; complete explicit mode maps are in `phase17_mappings.json` and `orbits.json`.

Preprocessing used 21.808847449 CPU seconds, plus 0.158416547 seconds to prepare the production-plan summary, within the 120-second authorization. It evaluated no field assignment, constructed no graph, and ran no BFS. `terminal.json` records the preprocessing snapshot; it is not overwritten by later production.

## Complete reduced production

Following separate authorization, all 1,091 representatives of dimension at most five were enumerated, exactly 84,607,626 marked projective inputs. The complete result is in `reduced_production/REPORT.md`:

- Legal actual generator sets: 78,408,267.
- Illegal assignments: 6,199,359.
- Assignments covering all 48 exact fibers: 0.
- Full BFS calls: 0; saved graphs: 0.

The production took 8.193481 CPU seconds, or 19.716619 including preparation and compilation, within its separate 60-second budget. The required calibration was an actual member of the production prefix: `z=(1,0,1)` restored fields `(0,3,11,7,1,0,1)`. Its original first nonzero field is 3, and it was retained; all 48 actual short-word masks matched the restricted forms.

The completed reduced batch excludes another 2,168 original modes. The exact accounting is

`16,375 = 28 previously completed + 314 newly symbolic-rejected + 2,168 newly fully searched + 13,865 remaining`.

The remaining 13,865 original modes have 7,124 phase-17 orbit representatives and 10,747,252,152 marked inputs. Of those representatives, 406 have exact-17 fibers but no nonzero linear sum constraint; 6,718 have no exact-17 fiber. Their actual assignments were not started. `REMAINING_AFTER_PRODUCTION.json` records the current remaining cursors. The earlier `PRODUCTION_PLAN.json` is the proposal snapshot whose dimension-at-most-five batch has now been completed, not an active queue.

No new graph or record was obtained. No independent final graph check is pending because no candidate reached full fiber coverage. The two authorized CPU totals together are 41.683882996 seconds; no restart, additional random seed, or dimension-six production was run.
