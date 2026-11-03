# Polarity73 monotone reduction — actual bounded delivery

Status2026-10-18: all assigned solver profiles are terminal; final same-thread round4 returned SUCCESS and closed the bounded loop at4/4. Original exact DD82 Goal remains ACTIVE and unresolved,57≤N(8,2)≤61. No legal graph above57 and no arbitrary58–61 exclusion.

## Mathematical scope and accepted assets

Ambient73 GF8 orthogonality graph,324edges,degree8×9/9×64,maxcommonneighbor1,84triangles. The studied family chooses survivors, preserves ALL surviving old edges and adds missing edges. This monotonicity is an artificial construction restriction. Complete monotone60/61 exclusion and f≥8outer deletions at58/59, scoped two-fiber failures and the first two SAT deletion-candidate contradictions are in POLARITY73_REDUCTION_CANDIDATE.md and actual round1–2 reviews. No full58/59 family exclusion.

On2026-10-18 the requested unit-deficit choice refinement actually ran. New58 SAT deletionD=[8,16,21,22,23,27,28,31,51,52,54,56,63,64,69] has449oldbadpairs and40edges needed. All its monotone completions are impossible: saturated5/61 force unit0 to choose2; after0–2,0/2 are saturated with disjoint neighborhoods, while unit1 must reach both with one new edge. The proof does not use arbitrary screen choice overflow72 or the unnecessary forced43–53. A fresh same-family recomputation and actual Gemini round3 accepted the precise fixedD proof. See POLARITY73_REFINED58_FORCED_EDGE.md and refined/n58/FIXED_DELETION_PROOF_CHECK.md.

## Actual profiles

| Input | Variables / clauses | Result | CPU s / wall s |
| --- | --- | --- | --- |
| Original58 necessary screen |2830 /12508|SAT checked; savedD later excluded|0.013380 /0.115486|
| Original59 necessary screen |2772 /12277|SAT checked; savedD later excluded|0.060981 /0.187628|
| Refined58 unit-neighbor screen |18325 /73630|SAT checked; savedD later excluded|0.963712 /1.134302|
| Refined59 unit-neighbor screen |18267 /73399|UNKNOWN exit0 atsoft28s|27.996050 /28.192344|
| Complete variable-D58 graph model |173093 /558930|UNKNOWN exit0 atsoft28s|28.043004 /28.198339|

The three new2026-10-18 solver profiles total57.002766 CPU seconds; parallel wall times and total research time are different quantities. Each profile had30CPU/45wall seconds,4GiB address-space limit,256MiB per-file bound. New discovery runs emitted no proof logs. No UNSAT result, no certificate checker and no target verification run occurred.58 refined decode was successful; other new profiles had no model.

## Complete共同实现 was actually attempted

complete_variable/encode.py uses all73 survivor bits and2304 possible new-edge bits without fixing a deletion set or screen choices. Both degree bounds are conditional on retaining the vertex; old edges are implicit conjunctions of the two retained bits. The coverage of every surviving ambient nonedge uses its retained unique old common neighbor, actual mixed old/new paths, or actual two-new-edge paths. This is exact for the full monotone family, not another necessary screen.

Source was freshly checked; root corrected candidate.json integration to include n/edges for the independent BFS tool. Eight explicit full-adjacency assignments passed, including a deleted vertex whose auxiliary old-neighbor count exceeds the target degree, required mixed paths and required two-new paths. Actual58 input preparation was2.829600CPU/2.870178wall seconds. The one short full58 run returned UNKNOWN. Full59 source support exists but no59 input or solve was prepared. Fixed-D completion code likewise was not run, because that savedD already has a shorter contradiction.

## Research decision and correction of reviewer overreach

Stop further unchanged or minor-clause profiles of this mechanism after this bounded delivery. This is a resource/direction decision, not proof that the family is exhausted or impossible. No hidden budget enlargement and no loop reset by renaming. The next constructive direction must change actual graph generation, potentially relaxing old-edge preservation, and address the observed forced-saturation obstacle rather than just append another weak filter.

Round3's formula sum(old-neighbor K)+sum(newX)=8K for all vertices is wrong at deleted vertices; source instead uses K implies exact8, guarding both thresholds. Its almost-certainUNKNOWN forecast was unsupported; the actual new short UNKNOWN is reported without converting it into a general complexity theorem. Not every ambient edge belongs to a triangle; arbitrary matching deletion4–8 neither guarantees triangle removal nor removal of the concrete obstruction. Unchanged Brown57+hub work is not resumed.

Existing review thread836dc422-ed04-4f1d-99f2-216fb8d7bae5, requested/CLI-reported gemini-3.8-flash-high/high. Actual rounds1–4 are saved; finalround4 accepts the scoped delivery, complete model and UNKNOWN result. Human feedback remains in research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md; readable reporting in research/progress.html. Updating these records does not pause the Goal.62–65 and oldLean remain frozen.
