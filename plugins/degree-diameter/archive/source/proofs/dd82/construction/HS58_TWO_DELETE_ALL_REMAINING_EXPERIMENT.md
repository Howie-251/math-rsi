# HS58: one joint experiment for all remaining addition counts

Date: 2026-10-12. Three bounded calls produced no decision. Their partial
proof files are not UNSAT certificates and no target graph was found.

The [completed low-addition exclusion](HS58_TWO_DELETE_FIVE_ADDITIONS_EXCLUSION.md)
requires at least six old additions when exactly two original HS edges are
deleted. The new [uniform upper bound](HS58_TWO_DELETE_GLOBAL_ADDITION_BOUND.md)
first established at most eight additions. This motivated a single joint
input for a=6,7,8 in each of the three complete deletion orbits, instead of
enumerating another auxiliary-graph catalog or querying individual types.
The subsequent pure proof excludes a=8 too. The actual formulas retain
their original 6..8 range and were not regenerated or restarted.

All 1050 old nonedges, 400 old-new edges and 28 new-new edges are variables.
Old and new degrees are exactly eight. Summing them gives B=54-2a and
2h+B=64, so h=a+5. Exact unary thresholds on the 28 auxiliary edges require
11<=h<=13, equivalent to 6<=a<=8. Ordering the eight auxiliary degrees
nonincreasingly is the sole new-label normalization; independent new
relabeling preserves every candidate because all attachment columns are
free. There is no auxiliary catalog, fixed A, full-port assumption,
matching restriction or extra zero-set inequality in these formulas.

For all 1653 vertex pairs the input either has a fixed retained-HS path or
encodes the direct edge and every two-edge route through all 58 vertices.
The same complete AND and exact-cardinality helpers used in the preceding
checked formulas are retained. The independent
[source review](HS58_TWO_DELETE_ALL_REMAINING_ENCODING_REVIEW.md) checked
candidate preservation and the actual metadata/headers without repeating
the computation.

Actual source: `computations/dd82/construction/hs58_two_delete_all_remaining.py`.
Evidence directory: `hs58_two_delete_all_remaining_run/` under the same path.

| Geometry | Variables / clauses | Preparation CPU | Solver CPU | Solver wall | Terminal status |
| --- | --- | ---: | ---: | ---: | --- |
| Adjacent | 33205 / 101997 | 0.134970 s | 148.810399 s | 151.510576 s | OUTPUT_LIMIT (-25) |
| Cross | 33249 / 102131 | 0.125326 s | 175.291769 s | 180.107638 s | UNKNOWN (0) |
| No cross | 33249 / 102131 | 0.126234 s | 159.593651 s | 162.692594 s | OUTPUT_LIMIT (-25) |

Each was one attempt with a 180-second solver limit, a separate 180/181 CPU
limit, 8 GiB address-space limit and 768 MiB output-file limit. The cross
solver's time limit ended before the CPU limit. The other two reached the
proof-output limit. All processes have finished. No LRAT checker was called
because none supplied a completed UNSAT proof; no learned solver state is
retained. Inputs, metadata, solver logs and partial proof files are saved.
The three calls overlapped on separate CPUs; their elapsed wall times must
not be summed as research elapsed time.

Consequently the remaining mathematical frontier is still a=6 or a=7.
The [all-addition saturated lemma](HS58_SATURATED_DISJOINT_ALL_ADDITIONS.md)
further excludes full-port cross deletions at these counts and full-port
no-cross at a=7. The saturated no-cross a=6 branch has four possible zero
sets and 56 necessary addition templates. These mathematical results do
not retroactively turn any of the above solver statuses into UNSAT.
