# Frozen complete one-extra-line-edge extension

Keep exactly the original six central matching edges M and their 12 endpoints T from ../PARAMETERS.json. Reuse ../DISTANCES_TO_T.json; its 312 entries with distance 4 are the fixed uncovered set U. Do not rerun the original 12-degree hub graph or its multi-source distance calculation.

For each original line edge v--q with v in T and q outside T, delete M and that one line edge, and add w=6804 adjacent to T union {q}. The predicted literal domain has 12*12=144 incident line edges. Group by q while preserving every source endpoint v, so any repeated q may share its new-root gate but not silently lose a different removed-edge candidate.

The resulting graph has 6,805 vertices and 44,232 edges. Vertex v has degree 12; all other old vertices and w have degree 13. All seven removed edges lie inside T'=T union {q}, hence distances to T' are unchanged by those removals. New-root eccentricity at most 4 is therefore equivalent to U being a subset of the original-graph B3(q), since the other old vertices already have distance at most 3 to T.

Predictions to test: at least one q covers all 312 old gaps; for a passing q, at least one corresponding changed graph has every distance at most 4. Neither prediction is assumed. The complete first gate evaluates every distinct q in the fixed 144-edge domain. If no q passes, immediately stop with zero candidate graphs and zero candidate BFS runs.

If some q passes, check each corresponding actual changed graph in deterministic (q,v) order, stopping a candidate at its first failing root/pair. If none fails, save its full edge list and parameters and immediately notify the parent. No unproved symmetry pruning is used. All actual candidates may be checked within a single 30-CPU-second budget; on budget exhaustion preserve the actual cursor and stop, without restart.

This rule uses the one remaining degree slot of the previously proposed hub and releases q's endpoint slot by deleting the additional line edge. It does not change the original matching, add a second line-edge deletion, choose another fiber coordinate, or add seeds.
