# All40 accepted neighborhoods independently work on original B0

The frozen prediction is **SUPPORTED**. Every one of the40 literal neighborhoods independently R4-dominates original B0, and all780 unordered neighborhood pairs have B0 set-distance at most3. Consequently the40 accepted additions are a feasible incumbent for a static joint repacking model; their validity does not require earlier-added helper routes.

One read of the accepted final51457-vertex edge list recovered:

- B0: labels0,…,51416, exactly324451 old-old edges.
- Additions: labels51417,…,51456, exactly412 new-old edges and0 new-new edges.
- Used old ports:397 distinct labels;382 used once,15 used twice. No B0 degree-plus-usage exceeds13; actual final maximum degree13.
- All40 multi-source radius4 searches on B0:0 missing old targets in every case.
- All780 pair distances from those same distance arrays:12 pairs at distance0,124 at distance2,644 at distance3; no other distance and no incompatible pair.

The preexisting scope did not already establish this result. The saved mechanism ledger explicitly mentioned only one original-B0 control and said the other39 were not recomputed there. Earlier sequential success used the changed current graph and is logically weaker than this independent-base certificate.

## Static certificate and its limit

For any selected neighborhood family satisfying these same three requirements—each S_i R4-dominates B0, every d_B0(S_i,S_j)≤3, and total port usage stays within13−degree_B0—attach a separate new vertex to each S_i. Old-old distances retain the inherited B0 diameter5 bound. New-old distances are at most1+4=5, and distinct new-new distances are at most1+3+1=5. Each new vertex must separately have at most13 neighbors. The actual40 sets satisfy all these conditions, so this supplies the requested static incumbent and permits their arbitrary ordering or taking subsets.

This does not assert existence of41 jointly feasible sets. No joint model, optimizer, new pool, new graph, or new bound was produced.

## Evidence and cost

`RESULT.json` stores all40 literal neighborhoods, their radius4 distance histograms/missing counts, the40×40 set-distance matrix, and all397 used ports with B0 degrees, spare capacity, and multiplicity. Matrix entry5 would mean greater than4 rather than an exact distance; no such pair occurred. `PREDICTION.md` predates the computation. `TERMINAL.json` is complete with no pending work.

Exactly one literal source read and40 authorized multi-source radius4 calculations; no source diameter BFS or old current-R4/guard search was repeated. Worker CPU0.096530 seconds; compilation plus execution0.767456 seconds, within the5CPU budget.

## Follow-up: exact40-set multiplicity pool has maximum40

Using only the saved calibration data, every one of the40 neighborhoods has an old member v with original spare capacity `13−degree_B0(v)=1`. Thus each multiplicity is individually bounded by k_i≤1. Summing gives at most40 added vertices, and the existing all-one vector attains40. The exact optimum of this fixed multiplicity pool is therefore40; it cannot produce a41st addition by duplicating its members, even after removing/reallocating other members.

There is no directly repeatable set. `MULTIPLICITY_RESULT.json` stores each complete S_i, all its capacity1 witness ports, current residual-capacity blockers, and the upper-bound histogram `{1:40}`. The follow-up PRED was appended before this calculation. CPU0.001134505 seconds;0 graph reads,0 BFS,0 solver calls,0 new graphs. No optimization call was needed. This excludes only multiplicities of these exact40 neighborhoods, not other neighborhoods or a larger pool.
