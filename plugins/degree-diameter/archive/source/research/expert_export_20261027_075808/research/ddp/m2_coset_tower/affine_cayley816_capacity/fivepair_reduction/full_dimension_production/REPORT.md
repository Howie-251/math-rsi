# Remaining dimension-six production: complete

All four workers completed their disjoint scopes: **7,124 representatives and 10,747,252,152 marked projective inputs**. No legal assignment covered all 48 exact fibers, so there was no D3 candidate, full BFS, or generated graph.

| Worker | Marked inputs | Legal inputs | Illegal inputs | CPU seconds |
|---:|---:|---:|---:|---:|
| 0 | 2,686,813,038 | 2,524,338,704 | 162,474,334 | 301.633262 |
| 1 | 2,686,813,038 | 2,517,155,898 | 169,657,140 | 245.199662 |
| 2 | 2,686,813,038 | 2,509,388,445 | 177,424,593 | 222.914323 |
| 3 | 2,686,813,038 | 2,490,679,741 | 196,133,297 | 193.550242 |

The aggregate counts are 10,041,562,788 legal and 705,689,364 illegal assignments. First-failure positions in the per-mode count/phase ordering were 1: 9,911,686,444, 2: 123,242,874, 3: 6,009,976, 4: 567,826, 5: 46,890, 6: 7,240, 7: 1,266, 8: 206, 9: 50, 10: 10, 11: 6. These are tested-fiber positions, not common quotient phases. Each worker retained its complete per-mode counts and has a null next cursor.

The run used four workers from one driver, session 77572, with production PIDs 3197240 through 3197243. Preparation and compilation used 2.327555000 CPU seconds; workers together used 963.297489000; total measured driver-plus-child CPU was 965.724383000. The authorized aggregate limit was 1,800 CPU seconds, with 440 per worker. No process was restarted and no extra profile was run. The formal first-100,000 records are actual production prefixes.

The on-the-fly coefficient generator retained all seven component variables, including the two independent reflection slots. It compared every original 48-fiber form-count vector to saved capacity, then deleted the correct nontrivial-action anchor and checked that deduplication did not change the counts. All retained bases were identity. Actual group inverse, nonidentity, and 12-element distinctness checks preceded exact fiber evaluation.

Two legal members of worker0's formal prefix supplied the required independent direct-word-mask comparison. Source 31886, phases `[0,5,15,16,18]`, restored fields `[1,0,0,0,0,0,1]`; source 91986, phases `[5,15,16,18,18]`, restored `[0,1,0,0,1,0,1]`. All 48 masks matched in each case. Together these cover phase zero, the phase-16 action kernel, and repeated phases. There was no extra field assignment or BFS outside the formal cursor.

## Scope closure

The current run closes only the remaining 7,124 representative modes by itself. Combining the explicitly checked saved terminals now closes the entire fixed-group degree-12 Cayley scope:

| Inverse pairs / reflections | Complete reduction and actual coverage |
|---|---|
| 0/12 through 3/6 | All 2,925 composition modes fail original plain capacity. |
| 4/4 | Of 12 symbolic survivors, 2 fail iterative tight capacity and all reduced assignments of 10 were completed. |
| 5/2 | 28 old modes + 314 linear-rejected modes + 2,168 modes covered by reduced production + 13,865 covered here = 16,375. |
| 6/0 | 48 old modes + 50,680 remaining completed modes = 50,728. |

The original complete composition table had 593,775 modes, 131,540 plain survivors, and 67,115 symbolic survivors. Necessary capacity failures account for modes outside the table's symbolic survivors. The phase-17 map transfers only along the explicitly saved valid automorphism orbits; fixed modes were not mechanically halved. Actual total production across the five saved batches was 15,390,839,950 marked assignments, comprising 14,582,049,507 legal and 808,790,443 illegal assignments. These are marked input counts, not distinct-graph counts.

Accordingly this complete finite calculation finds no simple undirected degree-12 diameter-at-most-3 Cayley graph on `F17 semidirect_3 C48`. It does not exclude arbitrary 816-vertex graphs or other groups, and is not a formal Lean certificate. No construction or new record was obtained. No independent final graph validation is pending because every actual candidate failed exact fiber coverage. `FAMILY_CLOSURE.json` records the cross-stage accounting; `SCOPE.md` gives the precise current iterator and route criterion.

## Extension to degree at most12

The group has17 distinct nonidentity involutions `(x,24)`,one for each x inF17. Any inverse-closed nonidentity set S of size below12 can be enlarged to size12 by adding unused involutions from this pool. Every added element preserves inverse closure and simplicity,and adding edges cannot increase diameter. Consequently the completed degree12 exclusion also excludes diameter-at-most3 Cayley graphs of this fixed group of any degree at most12. This does not extend to a different group or arbitrary816-point graphs.
