import json
from pathlib import Path

D=Path(__file__).resolve().parent
mods=['OppositeGQ77SpreadDefinitions','OppositeGQ77SpreadIncidenceData']
mods += [f'OppositeGQ77SpreadIncidenceChunk{i}' for i in range(8)]
mods += ['OppositeGQ77SpreadIncidence','OppositeGQ77SpreadInputInterface']
mods += [f'OppositeGQ77SpreadInputRow{i:03}' for i in range(400)]
mods += ['OppositeGQ77SpreadInputs','OppositeGQ77SpreadExact','OppositeGQ77SpreadAudit']
receipts=[json.loads((D/f'{m}_RESULT.json').read_text()) for m in mods]
assert all(r['exit_code']==0 for r in receipts)
historical=[json.loads(p.read_text()) for p in (D/'build_history').glob('*_RESULT.json')]
assert all('CPU_seconds' in r and 'module' in r for r in historical)
binding=json.loads((D/'INPUT_BINDING_CHECK.json').read_text())
assert binding['literal_edges_compared_one_by_one']==5121600
exactlog=(D/'OppositeGQ77SpreadExact.log').read_text()
auditlog=(D/'OppositeGQ77SpreadAudit.log').read_text()
for log in [exactlog,auditlog]:
    assert 'sorryAx' not in log
    for name in ['propext','Classical.choice','Quot.sound']:
        assert name in log
assert '160050' in auditlog and 'graph.degree' in auditlog
total=sum(r['CPU_seconds'] for r in receipts+historical)
assert total<=15000
result={
 'kernel_status':'PASS_UNCONDITIONAL_CONCRETE_ORDER_DEGREE_TRUE_WALK_D3_NON_D2',
 'entrypoint':'formal/DegreeDiameter/Portfolio/OppositeGQ77SpreadExact.lean',
 'theorem':'DegreeDiameter.Portfolio.OppositeGQ77Spread.concrete_order_degree_and_exact_D3',
 'claim':'card Vertex=160050 and every graph degree<=64 and DiameterAtMost graph3 and not DiameterAtMost graph2',
 'user_hypotheses':[],
 'carrier':'Fin160000 sum Fin50',
 'label_equivalence':'label:Vertex equiv Fin160050; old400p+l; new160000+j',
 'separate_import_audit':'formal/OppositeGQ77SpreadAudit.lean',
 'transitive_axioms':['propext','Classical.choice','Quot.sound'],
 'current_modules_PASS':len(receipts),
 'historical_failed_attempts_retained':len(historical),
 'harness_dispatcher_error_retained':'batch_history/attempt01_ERROR.log and attempt01_DRIVER_RESULT.json',
 'harness_recovery':'observed JSON publication race fixed by atomic replace; all217 existing PASS rows retained, only183 unfinished rows dispatched; same aggregate CPU limit',
 'CPU_seconds_current_PASS_modules':sum(r['CPU_seconds'] for r in receipts),
 'CPU_seconds_historical_attempts':sum(r['CPU_seconds'] for r in historical),
 'CPU_seconds_all_Lean_attempts':total,
 'CPU_budget_all_Lean_attempts':15000,
 'CPU_seconds_external_literal_binding':binding['CPU_seconds']+binding.get('owner_membership_bridge_CPU_seconds',0),
 'max_CPU_any_module':max(r['CPU_seconds'] for r in receipts+historical),
 'max_compiler_workers':8,
 'old_sources_or_cache_modified_or_recompiled':False,
 'BFS_solver_install_hash_native_decide_new_axiom':False,
 'input_binding':'INPUT_BINDING_CHECK.json',
 'ASCII_parser_theorem':False,
 'external_A_B_C_review':'ROOT_OWNS_SCOPE_AND_CURRENT_DISPOSITION; do not infer from kernel PASS',
 'fresh_literal_acceptance':'ROOT_OWNS_SEPARATE_RECEIPT; this compilation does not independently accept graph',
 'global_record_or_priority':'NOT_CERTIFIED',
 'next_unclosed_Lean_obligation':None,
 'receipts':receipts,
 'historical_receipts':historical
}
(D/'FINAL_COMPILE_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(D/'CHECKPOINT_C.md').write_text(f'''# GQ160050 final checkpoint C: actual closed theorem and import audit

Read actual definition bodies and the exported type before this summary. This
is the fixed GQ(7,7) instance; prior7242/6160 review verdicts do not cover it.

Final entrypoint:
`formal/DegreeDiameter/Portfolio/OppositeGQ77SpreadExact.lean`.
Actual declaration:
```
DegreeDiameter.Portfolio.OppositeGQ77Spread.concrete_order_degree_and_exact_D3 :
  Fintype.card Vertex = 160050 ∧ (∀ v, graph.degree v ≤ 64) ∧
    DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
```
No input, geometry, projection, capacity or success hypothesis remains on it.
`final_claim : FinalClaim` is the same proposition. DiameterAtMost is the
project's actual Walk-length definition, not a numerical success predicate.

Actual definitions:
- `OppositeGQ77SpreadDefinitions.lean`: carrier Fin160000⊕Fin50, typed Inc
  membership, graph body, oldEquiv and label equivalence to Fin160050.
- `OppositeIncidenceSpreadSlots.lean`: generic Inc and graph wrapper.
- `OppositeGQ35SpreadGeneric.lean`: actual graph cases (cross-incidence between
  distinct old pairs; flag+spread incidence for old-new; no new-new edges).
All these Portfolio paths begin `formal/DegreeDiameter/Portfolio/`.
Old(p,l) has label400*p+l; newj has160000+j. The theorem is on the Sum carrier
with an explicit Fin label equivalence, not a separately transported Fin graph.
The field explanation is external; Lean uses the actual literal incidence graph,
without a ZMod49 substitution or a field-existence premise.

Concrete caller closure:
- IncidenceData/Chunk0..7/Incidence kernel-check all6400 positive inverse-position
  equalities, cover all Fin400 labels via the actual8×50 index equivalence, and
  check all50×8 owner entries. The two initial elaboration failures were fixed;
  their archived logs are historical, not accepted theorem dependencies.
- InputInterface proves the projection-to-Inc bridge. Every InputRow000..399
  actually compiles its400 finite equalities. Inputs closes the universal
  quantifier over all400 original point labels. No representative-row assumption
  is used by the final caller.
- Exact applies the unchanged arbitrary-a,b Family theorem at8,8 and supplies
  every actual hypothesis. Shared Slots proves degree≤64; shared Walks supplies
  D3; shared LowerGeneric proves non-D2 from the finite-neighbor bound4161<160050.

Actual execution evidence, in this formalization directory:
- FINAL_COMPILE_RESULT.json: all{len(receipts)} current modules exit0.
- OppositeGQ77SpreadInputs.log and its RESULT: universal finite assembly.
- OppositeGQ77SpreadExact.log and its RESULT: actual unconditional theorem.
- OppositeGQ77SpreadAudit.log and its RESULT: a separate process imports Exact,
  prints the actual graph/type/body and transitive axioms.
The final theorem and final_claim depend only on
`[propext, Classical.choice, Quot.sound]`; no sorryAx/native_decide/new axiom.
All Lean attempts, including the2 historical failed elaborations, measured
{total:.6f}CPU of15000. Old graph/generic sources and cache were not changed or
rebuilt. No old/full-source BFS, solver, install or hash was run.

INPUT_BINDING.md and INPUT_BINDING_CHECK.json give exact readback of6400
incidence entries,50 original spread labels,400 owners,160000 ordered triples,
all50×64 ordered pins, and every5121600 literal formula edge. Blocking is20×20
row-major lookup of the same Fin400 label, with no permutation. The owner lookup
also equals actual spread membership at each point. This is explicit external
correspondence, not an ASCII-parser theorem or independent graph acceptance.

The observed Python status-file publication race and its recovery are separately
retained in batch_history/; it caused no Lean row failure or recompilation of
the217 already PASS rows. Metadata publication became atomic and only183
unfinished rows were resumed under the same CPU limit.

Root owns A/B/C raw records and dispositions. B198 actually PASSed the finite
connection at its stated scope; it is not final C. This file is the new final-C
packet after actual kernel and import completion. Global record/priority remains
uncertified; Lean validity does not establish novelty.
''')
(D/'NEXT_FORMAL_OBLIGATION.md').write_text('''Original target and source: fixed160050/degree64 incidence-spread graph from actualPARAMETERS.
Main module: formal/DegreeDiameter/Portfolio/OppositeGQ77SpreadExact.lean.
Closed: all400 projection rows, actual Incidence/owner, universal caller, unconditional card/degree/trueWalkD3/nonD2, separate import/type/standard3axiom audit.
Next unclosed Lean obligation: none.
Execution: FINAL_COMPILE_RESULT.json and individual receipts; historical failures retained and counted.
Reviews: root owns actual new-scope A/B/C records; CHECKPOINT_C.md is ready for final review, not a claimed completed C.
No old source/cache rebuild, no BFS/solver/install/hash/native_decide/new axiom. Do not restart completed rows or another parameter ladder.
''')
print(json.dumps({k:v for k,v in result.items() if k not in ['receipts','historical_receipts']},indent=2))
