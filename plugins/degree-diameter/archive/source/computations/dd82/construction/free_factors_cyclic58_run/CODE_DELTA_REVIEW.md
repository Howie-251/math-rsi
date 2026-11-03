# Proved-cut delta review: PASS

2026-10-18. **PASS; no blocking issue found.** This fresh same-family, provisional source review covers only the latest changes in `encode.py` and their specification in `PROVED_CUT_DELTA.md`. It inherits the already accepted source-specific 5+5 and 5+6 exclusions as mathematical premises; it does not reprove them or accept any production outcome. The earlier 12-assignment small semantic review remains applicable.

The new counters are guarded by `a == 28 and offsets == OFFICIAL_OFFSETS`, after conversion of offsets to a tuple. Exactly columns 28 and 29 receive an exact-six constraint, each over its 28 genuine cross variables. No small instance or different source receives these constraints. The existing cross-plus-matching degree equations then force matching degree zero at the two new vertices. No overlap, left-path, factor type or additional endpoint condition has been introduced.

All primary variables and actual-right union variables are allocated before the added counters. Their IDs therefore remain unchanged: H starts at 1, F at 379, M at 814, cross incidences at 1249, and R at 1473. Only subsequent auxiliaries and clause positions change; these are stored and read using their actual generated counts and records, not hard-coded positions. Saving and decode remain consistent.

`right_new_cross_degree` correctly reads `graph['right_cross_degrees'][vertex]` in the explicit-assignment checker. For 28 inputs with target six, the existing exact-count helper emits two final units. At actual count five, only the positive sixth-threshold unit fails; the negative seventh-threshold unit holds. Consequently the original 5+5 fixture should produce two failed counters and exactly two additional false clauses beyond its actual uncovered pairs, as the new preparation assertions require. At count six both units hold. This is a source-level check of the forthcoming CNF assertions; no formal CNF was built in this review.

The only execution was direct graph checking of the two deterministic fixtures, with no builder, preparation or solver call. I also compared their edges and cross entries to verify that the delta changes precisely the four documented cross entries and the two documented matching edges while preserving H and F.

| Actual graph check | Original 5+5 | Revised 6+6 |
|---|---:|---:|
| Vertices / edges | 58 / 232 | 58 / 232 |
| Every vertex degree | 8 | 8 |
| New cross-column degrees | 5, 5 | 6, 6 |
| New matching degrees | 1, 1 | 0, 0 |
| Actual BFS bad pairs | 287 | 299 |
| L0–L27 remains bad | yes | yes |
| R0 covers all 28 left vertices | yes | yes |

Both graphs satisfy the original structural family, have no forbidden source incidence or F/M overlap, and are not targets. Keeping `graph_check`'s `in_scope` predicate on the original structural family is consistent with retaining the old object as a negative fixture: the separately recorded counter failures describe its failure of the new necessary cuts.

The revised preparation checks the old negative fixture, then uses the 6+6 fixture's full assignment for DIMACS readback and requires its false clauses to be exactly its BFS bad pairs. That is the appropriate update. Neither the formal preparation nor these formal-CNF comparisons have been executed by this reviewer. No additional test batch, cut, patch or budget is requested.
