# GF9 free cross-link B family — complete, no D8 graph

All162 frozen scalar/vector cases have exact global diameter9: **160 newly constructed graphs plus2 strictly inherited controls**. Each graph has n=19440, m=48600 and degree5. The target was (5,8), saved baseline18810. No new lower bound was obtained. Both embeddings scalar4/8 and all81 GF9² values of the one free B normal vector are covered; no unknown or untried case remains.

The actual new graphs were checked by two complete BFS runs each, from0 and9720 (320 new root BFS total). The free left-deck action has exactly these two base orbits, so the maximum of the two representative eccentricities is the exact global diameter. The B_vector_id19=(1,2) graph of each scalar was already checked by q9_D8_controls and was not rerun; those two old graphs and four old representative BFS results are inherited literally. The source D7 BFS was not repeated. Ordinary unordered bad-pair counts were not measured; all R8 counts below refer to individual representative roots.

The pre-execution hypothesis was that the centered source B=(1,−1) becomes beta-fixed in characteristic3, reducing its H-orbit from the source24 to8, and that freeing B outside this line might restore D8. This was a concrete prediction recorded before the run, not a post-hoc explanation. Actual cached strata are: one zero orbit, one nonzero beta-fixed orbit of size8, and three distinct outside-line H-orbits of size24 for each embedding. Every one of the144 outside-line cases across both embeddings still has D9. Thus the prediction that leaving the fixed line repairs the coverage is refuted; orbit enlargement alone was insufficient. This does not assert that orbit size is irrelevant to the route counts.

| scalar | H-orbit representative ID | orbit size | beta-fixed | new cases | inherited | root0 / root9720 R8-missing range |
|---|---|---|---|---|---|---|
| 4 | 0 | 1 | True | 1 | 0 | 367–367 / 425–425 |
| 4 | 11 | 8 | True | 7 | 1 | 43–303 / 54–294 |
| 4 | 1 | 24 | False | 24 | 0 | 39–297 / 44–300 |
| 4 | 12 | 24 | False | 24 | 0 | 30–421 / 43–500 |
| 4 | 15 | 24 | False | 24 | 0 | 28–208 / 33–232 |
| 8 | 0 | 1 | True | 1 | 0 | 302–302 / 329–329 |
| 8 | 11 | 8 | True | 7 | 1 | 47–419 / 55–456 |
| 8 | 1 | 24 | False | 24 | 0 | 46–355 / 48–391 |
| 8 | 12 | 24 | False | 24 | 0 | 41–297 / 40–291 |
| 8 | 15 | 24 | False | 24 | 0 | 38–315 / 28–296 |

These strata were aggregated only from saved RESULT.json records and the two saved controls; no graph or BFS was rerun. ORBIT_STRATA.json contains every stratum's B IDs, actual/inherited counts, diameter histogram and root-count ranges.

All other GF9 field/group matrices, voltage phases, C5 coordinates and normal voltages were fixed. Only the B cross-link normal vector changed; its reverse voltage was recomputed with the true inverse formula. The finite scope is exactly2×81 choices, not arbitrary cross-links or degree5 graphs. Recorded process CPU was7.90845825 seconds, within the15-second budget. RUN_HANDLE/checkpoint have been corrected from their stale running labels to this completed result. The family is closed; no extra vector, phase, scalar, field or best-missing continuation is proposed.
