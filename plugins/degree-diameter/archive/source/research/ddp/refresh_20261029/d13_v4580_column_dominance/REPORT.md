# v4580 full-target column dominance: only96 columns removed

The complete strict-subset pass leaves **12961 of13057 columns** and removes96, about0.74%. This is a negligible reduction for the previous unresolved model. Stop here: no SAT/LP/MIP call or old-timer restart was made.

The scope remains the exact current51457/v4580 problem: all2755 prepared missing targets, the saved nine mandatory pins, currently free guard representatives, and at most4 unit-cost guards with no additional conflicts. The original prepare code only deduplicated identical complete masks; the later route-block calculations used a different sufficient criterion. This precise strict-subset pass was not previously completed.

## Complete filter and certificate

Process all13057 columns by descending popcount, breaking ties by original column index. A column is removed precisely when an earlier retained column is an exact proper superset. Distinct equal-popcount masks cannot strictly contain one another. A later smaller/equal column cannot dominate a retained column, so all saved witnesses remain retained and the final set consists of the inclusion-maximal original columns.

There were83741594 candidate subset comparisons and83903597 word tests. Each of the96 deleted columns has a saved still-retained superset witness; all96 proper containments were rechecked exactly against the input's44-word masks. No target or guard eligibility was changed. `RESULT.json` contains retained/removed original zero-based column IDs, corresponding actual guard labels, all2755 original target labels, and every witness with both popcounts. Column IDs index the unchanged `prepared.json` representative list; they are not one-based SAT variables.

Replacing a chosen deleted guard by its saved superset preserves all covered targets and does not increase the number of chosen guards. If that superset guard was already chosen, drop the dominated guard without replacement. Conversely every retained-column cover is an original-column cover. Thus existence of a full cover with at most4 guards is preserved exactly. This does not decide whether such a cover exists.

## Cost and terminal scope

One mask-file read and the prepared metadata only; no source graph or ball was read or computed. Worker CPU0.161755 seconds; compilation plus execution0.768575 seconds, within5CPU. All13057 columns completed;0 solver calls,0 new graphs,0 restarts, no pending work. `PREDICTION.md` was saved before the calculation, and `TERMINAL.json` records the actual completion.
