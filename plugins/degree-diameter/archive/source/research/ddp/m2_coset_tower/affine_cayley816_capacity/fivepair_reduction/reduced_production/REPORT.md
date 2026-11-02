# Complete reduced five-pair production

All 1,091 authorized phase-mode representatives and all 84,607,626 marked projective inputs were processed. None covered all 48 exact fibers, so no diameter-3 candidate, graph artifact, or BFS call was produced.

The group is `F17 semidirect_3 C48`, with product `(x,j)(y,k)=(x+3^j*y,j+k)`, degree 12 and target diameter 3. Each mode has five true inverse pairs and two phase-24 reflections. The scope consists exactly of the surviving representatives from `../reduced_dimension_inputs.json` with final nullspace dimension 3, 4, or 5. These 1,091 representatives cover 2,168 original phase modes via the explicitly proved phase-17 automorphism. The 7,124 dimension-six representatives were not included.

| Nullspace dimension | Representatives | Marked input scope |
|---:|---:|---:|
| 3 | 3 | 921 |
| 4 | 143 | 746,460 |
| 5 | 945 | 83,860,245 |
| Total | 1,091 | 84,607,626 |

The iterator sets only the first nonzero nullspace coordinate `z` to 1, restores the six anchored fields through the saved basis, and inserts zero at the saved nontrivial-action anchor. It does not normalize the restored fields again. Every candidate is checked for 12 distinct, nonidentity actual group elements, including repeated pair phases and the two reflection coordinates. Actual inverse elements use the group operation, including phase 16 with trivial scalar action.

For each legal assignment, the evaluator tests the complete restricted coefficient-form set in each fiber for coverage of all 17 field values. Fibers are ordered by increasing number of distinct forms, then phase. This is an exact length-at-most-three reachability test, not a form-count bound. Full root BFS and a complete edge table would be produced only after all 48 fibers covered. None did.

The totals are:

- 78,408,267 legal assignments; 6,199,359 illegal assignments.
- Rejections at tested fibers 1, 2, 3, and 4: respectively 78,383,837; 20,558; 3,840; and 32.
- Full 48-fiber passes, BFS calls, and saved graphs: all zero.

The generic generator check and exact mask evaluation include a required calibration at production global index 1, source mode 51078, pair phases `[1,10,17,18,18]`. Its `z=(1,0,1)` restores `(0,3,11,7,1,0,1)`, a legal set whose first nonzero original field is 3. Direct multiplication of all words of length at most three agrees with every one of the 48 evaluated masks. This member is included in the actual enumeration; it is not an extra search or BFS. The evidence is `in_prefix_mask_calibration.jsonl`.

The unique run was session 83738, production PID 3126455, with start cursor zero and no restart. `terminal.json` records all 1,091 completed modes and a null next cursor. Search CPU was 8.193481 seconds; preparation and compilation took 11.489086 seconds; the measured complete driver total was 19.716619 seconds, below the 60-second authorization. The first-100,000 log includes fixed input-loading cost, so its naive rate extrapolation was not a prediction of the measured final runtime.

Files: `inputs.json` and `inputs.txt` retain the exact bases, slot order, fiber forms, and scopes; `metadata.json` records semantics and budget; `terminal.json` gives per-mode exact counts; `by_dimension.json` aggregates those counts; `run.json` and `summary.json` give execution status and timing. No graph verification remains pending. This closes only the specified reduced subrange, not the remaining five-pair family.
