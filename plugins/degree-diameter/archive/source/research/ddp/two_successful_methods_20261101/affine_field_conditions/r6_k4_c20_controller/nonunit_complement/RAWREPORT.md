# Disjoint nonunit complement: complete STOP

**STOP_EXHAUSTED_NONUNIT_COMPLEMENT.** The one new bounded run considered all 161,051 assignments with g01=5 and the other five shifts in U=[2,4,5,6,8,10,12,14,15,16,18]. It skipped exactly 243 disconnected assignments, proved by the gcd criterion, and evaluated every one of the remaining 160,808 connected assignments. None passed the complete 296-class NB3 predicate. The last considered shift vector was `[5,18,18,18,18,18]`.

The program loaded the original 600 coefficient rows from `../WORD_COEFFICIENTS.tsv`; it did not rerun the anchor1 search. All connected candidates failed while checking root base0. Their first-failure counts by target base were:

| Target base | Assignments rejected first here |
|---|---:|
| 0 | 136,892 |
| 1 | 22,412 |
| 2 | 1,496 |
| 3 | 8 |

The four counts sum to 160,808. These are assignment counts, not missing ordered-pair counts. Root bases1..3 were not reached after these complete rejection tests; their zero first-failure counters do not assert universal coverage.

New CPU: compilation 0.525241 seconds, coefficient loading and search 0.030264 seconds, measured driver total 0.558159354 seconds. Adding the original 1.094645045 seconds gives 1.652804399 seconds, below the original shared 30-second budget and the separate 5-second additional allowance. One worker. No graph, BFS, solver, Lean, hash, installation, old-graph revalidation or other parameter domain was used. No passing controller files were emitted.

`SYMMETRY_AND_CONNECTEDNESS.md` independently proves the necessary normalization and exact connectivity criterion. Together with the original anchor1 STOP, this result closes the complete specified six-nonzero-shift K4 / Z20 family for the required NB3 interface; the combined statement is in `../COMBINED_SCOPE.md`. The original raw STOP and its restricted-scope report are unchanged.
