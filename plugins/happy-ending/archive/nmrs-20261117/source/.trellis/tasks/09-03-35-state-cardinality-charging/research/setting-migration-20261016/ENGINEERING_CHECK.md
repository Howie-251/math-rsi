# Engineering check — setting migration, 2026-10-16

Verdict: no blocking engineering defect found in the inspected implementation and tested scope. This is a bounded Sol engineering check. It is not independent scientific review, production acceptance, a general production/prototype projection-equivalence certificate, or evidence of a new numerical bound. Requested executor: native gpt-6.1-sol/high; backend model/effort were not independently reported by the host. Claude review remains disabled/unavailable.

## Artifacts and boundaries

Local root: D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/setting-migration-20261016/
Linux root: /data/ktqiu_hdd/math_agent/res/state_charging/20261016_setting_migration_probe_v1/
Scientific interpreter: /opt/anaconda3/envs/forktqiu3/bin/python3.12.

Read AGENTS.md, execution-dispatch.md, trellis-check, backend general-setting-migration and semantic-encoding-equivalence specs, focused migration plan, production rank builder, signotope clauses, baseline profile extractor, prototype.py and run_probe.py. This checker changed only its own new engineering scripts/evidence/report. Production sources, live jobs and implementation files were not modified.

Final inspected prototype SHA-256: 56be6b1c50f24613ae9cd6676669fd2d19fdd52c279deeb42ef2aae51b53124b.
Final runner SHA-256: cd0ad9aec8419622b74d92a15bc0481c602737a377ee53fa5d2e3046ec9652f1.

## Findings and disposition

1. P2, resolved for final external evidence: initial runner receipts did not bind prototype/runner bytes or all profile flags. Final run_probe.py:228-232 records bridges, f3, signotope, cell, source hashes and runtime-manifest hash. Every one of the 15 existing run receipts matches these final sources and actual input/log hashes in the independent receipt verification.
2. P2 coverage gap, closed within an explicitly narrower profile: initial N5 oracle and N4 canonical tests cannot exercise a weak seven-point target. Initial nonvacuous omitted-pair control exercised only (3,6). engineering_pair_check.py independently covers all 12 setting/pair combinations at N7 with bridges=True, f3=False. For each, it verifies nondegenerate geometry, signotope packet changes, explicit subset-path enumeration versus DP, a nonempty sole active pair, full strict rejection, and omitted-pair canonical acceptance plus semantic audit. These are canonical checks, not 12 new solver/proof runs.
3. P2 false-credit hazard, addressed by scope: run_probe.py:122 and :153 compare the 756 catalog and 896 valid N5 state profiles. They do not compare existential CNF projections against the public production builder. Neither equal SAT statuses nor these profile checks establish that general equivalence. Final claims must retain this limitation.
4. Provenance limitation: initial semantics ran v1, not the final v2 source. Preserved source_v1_semantics bytes have hashes 06841724f16984e4fed96538b3ab953e1bbf9896ccfd3ebd1fb8f3028383bd80 (prototype) and 875a78cd2505188e8466120fa587d251f5af04005bc3bc7e359458fc49987bef (runner). These are post-phase captures, not contemporaneous start hashes. Inspection of v1/v2 differences finds only two prototype profile attributes, runner receipt bindings, a stricter solver-budget admission check, and whitespace; the semantic test routine is unchanged. Do not relabel initial semantics as a final-v2 rerun.
5. P3 documentation precision: TECHNICAL.md and original primary_inventory source-difference wording omit the stricter budget-admission change. The executed difference is benign and more conservative: SOLVER_TIME>=280 became SOLVER_TIME+22>300. Describe it explicitly when summarizing revisions.

No remaining P1/P2 engineering defect was identified in the tested default profiles. Mutable research objects and post-hoc inventories are not hardened production replay APIs; fresh production campaigns would require their own sealed source/CNF/proof/checker bindings.

## Static semantic reasoning

- Setting derives W=a-2,H=b-2; catalogs contain all nonincreasing W-tuples in [0,H]. Ordinary bbox width+height<=6 includes empty; the catalog totals and all feasible d+f=9 pairs match all five settings.
- Both terminal and fixed-start path recurrences have exact AND/OR definitions. Empty-path base cases, bounds and shared outer start/end restrictions are consistent with independent path enumeration. The six signotope clauses match production add_signotope; model audit separately counts packet sign changes.
- A state is the full Boolean cell pattern; occupancy is an exact OR of vertex states. Counts use occupied exceptional types and missing ordinary types, not one-way witnesses. Exact cells enforce N=O+e-m and m<=O-1; the numerical O+1 spine has e<=min(E,O).
- Every cell in D(u), u<v, extends one terminal color along (w,u,v); the dynamic boundary bridge clauses are entailed by path bounds. The terminal signature at (u,v) belongs to D(v) but cannot belong to D(u), because its presumed witness would extend one color past the longest length at (u,v). Hence D(v) is not a subset of D(u), giving injection and the occupied proper-subset/superset rank directions.
- Consequently proper occupied subsets of D(v) occur earlier and supersets later. F3 bounds v-1 and N-v have the correct directions. The reused exact prefix recurrence defines canonical thresholds for every old assignment. This entailment does not assume target UNSAT.

## Executed evidence

Implementation's raw Linux receipts, inspected here:

- semantics.json: 43 checks; 1024 N5 colorings per setting (5120 total), 896 valid 756 production-profile comparisons, and 16 N4 canonical default-profile colorings per setting (80 total). This is the preserved v1 phase.
- solver_results.json and runs/*: 15 sequential external AE solves, 11 complete SAT assignments and four UNSAT controls with actual repaired-checker exit 0 and exact s VERIFIED lines; no timeouts. Total solver wall 7.070242840796709 seconds.
- Five strict N8 default-profile exceptional models all have e=2, with m=19,20,24,25,26 for 756,757,766,767,777. Five corresponding exact-cell formulas are SAT under those fixed colors. The omitted-pair positive is explicitly marked as a negative-control target profile.
- Four checked UNSAT controls concern fixed-color full-target exclusion, state reverse equivalence, occupancy reverse equivalence and wrong exact counts. They are local regression queries and grant no setting bound.
- supplementary_semantics.json: five known strict exceptional N7 canonical models with F3 disabled; incomplete/nonboolean model rejection; deterministic 756 N3 DIMACS; a deliberately removed occupancy reverse clause accepts a fabricated exceptional occupied type while semantic audit rejects it.

Checks this engineering agent independently executed on Linux:

1. engineering_pair_check.py: all 12 setting/pair controls pass. No solver call. Output engineering_pair_controls.json SHA-256 150365ab388e0317f808bd99107c784a35aafab46bf66ed34981274eacd2e20a.
2. engineering_receipt_check.py: actual runtime-source and solver/checker executable hashes verified; all 15 individual receipts equal aggregate entries; every CNF and stdout/stderr hash verified; all four proof hashes, sizes and retained checker logs verified; all 11 SAT outputs independently parsed as complete, duplicate-free Boolean models and streamed through every actual DIMACS clause, including extra assumptions. No new solver or checker launch. Output engineering_receipt_verification.json SHA-256 40a97b0c2e5a8fa3e782cc0795ec03b62ab687e9ba8f91f26ce43fbf0824a1f0.
3. The four engineering script/evidence file hashes were compared after Linux-to-desktop retrieval and match. Final prototype and runner hashes match the solver receipts.

Reproduction commands (create-only output files; use a fresh isolated copy for reruns):
/opt/anaconda3/envs/forktqiu3/bin/python3.12 engineering_pair_check.py
/opt/anaconda3/envs/forktqiu3/bin/python3.12 engineering_receipt_check.py

The independent receipt checker replays SAT clauses, not the scientific proof checker; retained checker verification remains the implementation's four actual checker executions. The implementation's semantic model replay and this static inspection support the bounded semantics claim.

## Practical limits

The 777 N8 no-cell default-profile formula has 2,455,858 variables and 9,795,033 clauses, of which F3 adds 2,449,602 variables and 9,725,716 clauses. Small solve times do not establish scalability to the numerical spine or new research bounds. Pair controls explicitly disable F3; F3 nonvacuity is instead evidenced by the five N8 default-profile SAT models and exact-cell runs. No old 756 charging theorem, shadow/orientation interface, accepted campaign, or proof credit transfers to these new settings.
